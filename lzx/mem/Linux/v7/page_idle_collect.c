#define _GNU_SOURCE

#include <ctype.h>
#include <dirent.h>
#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <limits.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define PM_PRESENT  (1ULL << 63)
#define PM_PFN_MASK ((1ULL << 55) - 1)
#define DEFAULT_IDLE_BITMAP "/sys/kernel/mm/page_idle/bitmap"

typedef enum {
    SEG_TEXT = 0,
    SEG_DATA,
    SEG_BSS,
    SEG_HEAP,
    SEG_STACK,
    SEG_FILE,
    SEG_ANON,
    SEG_SPECIAL,
    SEG_UNKNOWN,
    SEG_COUNT
} SegmentKind;

typedef enum {
    PAGE_REFERENCED = 0,
    PAGE_IDLE,
    PAGE_NOT_PRESENT,
    PAGE_PFN_HIDDEN,
    PAGE_ERROR
} PageState;

typedef struct {
    uint64_t start;
    uint64_t end;
    uint64_t offset;
    unsigned long long inode;
    char perms[8];
    char dev[32];
    char path[PATH_MAX];
    SegmentKind segment;
} Vma;

typedef struct {
    Vma *items;
    size_t count;
    size_t cap;
} VmaList;

typedef struct {
    uint64_t addr;
    uint64_t pfn;
    SegmentKind segment;
    char vma_label[40];
    const char *path;
    PageState state;
} PageRecord;

typedef struct {
    PageRecord *items;
    size_t count;
    size_t cap;
} PageList;

typedef struct {
    uint64_t start;
    uint64_t end;
} Range;

typedef struct {
    Range *items;
    size_t count;
    size_t cap;
} RangeList;

static const char *segment_token(SegmentKind s)
{
    switch (s) {
    case SEG_TEXT: return "text";
    case SEG_DATA: return "data";
    case SEG_BSS: return "bss";
    case SEG_HEAP: return "heap";
    case SEG_STACK: return "stack";
    case SEG_FILE: return "file";
    case SEG_ANON: return "anon";
    case SEG_SPECIAL: return "special";
    default: return "unknown";
    }
}

static SegmentKind parse_segment(const char *s)
{
    for (int i = 0; i < SEG_COUNT; i++) {
        if (strcmp(s, segment_token((SegmentKind)i)) == 0) return (SegmentKind)i;
    }
    return SEG_UNKNOWN;
}

static const char *state_token(PageState s)
{
    switch (s) {
    case PAGE_REFERENCED: return "referenced";
    case PAGE_IDLE: return "idle";
    case PAGE_NOT_PRESENT: return "not_present";
    case PAGE_PFN_HIDDEN: return "pfn_hidden";
    default: return "error";
    }
}

static char state_code(PageState s)
{
    switch (s) {
    case PAGE_REFERENCED: return 'R';
    case PAGE_IDLE: return 'I';
    case PAGE_NOT_PRESENT: return 'N';
    case PAGE_PFN_HIDDEN: return 'H';
    default: return 'E';
    }
}

static void usage(const char *argv0)
{
    fprintf(stderr,
            "用法:\n"
            "  sudo %s <pid> -o page_idle.tsv --bitmap page_idle_bitmap.txt [-s user_operation.sh]\n"
            "  sudo %s --app firefox -o page_idle.tsv --bitmap page_idle_bitmap.txt [-s user_operation.sh]\n\n"
            "可选过滤:\n"
            "  --vma start-end      只跟踪指定 VMA 范围，可重复\n"
            "  --segment heap       只跟踪指定 segment，可重复\n",
            argv0, argv0);
}

static char *trim_left(char *s)
{
    while (*s == ' ' || *s == '\t') s++;
    return s;
}

static void trim_right(char *s)
{
    size_t n = strlen(s);
    while (n > 0 && (s[n - 1] == '\n' || s[n - 1] == '\r' || s[n - 1] == ' ' || s[n - 1] == '\t')) {
        s[--n] = '\0';
    }
}

static bool starts_with(const char *s, const char *prefix)
{
    return strncmp(s, prefix, strlen(prefix)) == 0;
}

static void clean_deleted_suffix(const char *in, char *out, size_t len)
{
    const char *suffix = " (deleted)";
    size_t n;
    snprintf(out, len, "%s", in);
    n = strlen(out);
    if (n >= strlen(suffix) && strcmp(out + n - strlen(suffix), suffix) == 0) {
        out[n - strlen(suffix)] = '\0';
    }
}

static bool path_equal_ignoring_deleted(const char *a, const char *b)
{
    char ca[PATH_MAX], cb[PATH_MAX];
    clean_deleted_suffix(a, ca, sizeof(ca));
    clean_deleted_suffix(b, cb, sizeof(cb));
    return strcmp(ca, cb) == 0;
}

static bool is_special_path(const char *path)
{
    return strcmp(path, "[vdso]") == 0 ||
           strcmp(path, "[vvar]") == 0 ||
           strcmp(path, "[vvar_vclock]") == 0 ||
           strcmp(path, "[vsyscall]") == 0;
}

static bool is_heap_path(const char *path)
{
    if (strcmp(path, "[heap]") == 0) return true;
    if (!starts_with(path, "[anon:")) return false;
    return strstr(path, "heap") != NULL || strstr(path, "jemalloc") != NULL || strstr(path, "malloc") != NULL;
}

static bool mkdir_p(const char *path)
{
    char tmp[PATH_MAX];
    size_t len;
    if (path[0] == '\0') return true;
    if (snprintf(tmp, sizeof(tmp), "%s", path) >= (int)sizeof(tmp)) {
        errno = ENAMETOOLONG;
        return false;
    }
    len = strlen(tmp);
    while (len > 1 && tmp[len - 1] == '/') tmp[--len] = '\0';
    for (char *p = tmp + 1; *p != '\0'; p++) {
        if (*p != '/') continue;
        *p = '\0';
        if (mkdir(tmp, 0755) != 0 && errno != EEXIST) return false;
        *p = '/';
    }
    return mkdir(tmp, 0755) == 0 || errno == EEXIST;
}

static bool ensure_parent_dir(const char *path)
{
    char parent[PATH_MAX];
    const char *slash = strrchr(path, '/');
    size_t len;
    if (slash == NULL) return true;
    len = (size_t)(slash - path);
    if (len == 0) len = 1;
    if (len >= sizeof(parent)) {
        errno = ENAMETOOLONG;
        return false;
    }
    memcpy(parent, path, len);
    parent[len] = '\0';
    return mkdir_p(parent);
}

static bool vma_list_push(VmaList *list, const Vma *vma)
{
    if (list->count == list->cap) {
        size_t new_cap = list->cap == 0 ? 64 : list->cap * 2;
        Vma *items = realloc(list->items, new_cap * sizeof(*items));
        if (items == NULL) return false;
        list->items = items;
        list->cap = new_cap;
    }
    list->items[list->count++] = *vma;
    return true;
}

static bool page_list_push(PageList *list, const PageRecord *page)
{
    if (list->count == list->cap) {
        size_t new_cap = list->cap == 0 ? 1024 : list->cap * 2;
        PageRecord *items = realloc(list->items, new_cap * sizeof(*items));
        if (items == NULL) return false;
        list->items = items;
        list->cap = new_cap;
    }
    list->items[list->count++] = *page;
    return true;
}

static bool range_list_push(RangeList *list, Range range)
{
    if (list->count == list->cap) {
        size_t new_cap = list->cap == 0 ? 8 : list->cap * 2;
        Range *items = realloc(list->items, new_cap * sizeof(*items));
        if (items == NULL) return false;
        list->items = items;
        list->cap = new_cap;
    }
    list->items[list->count++] = range;
    return true;
}

static void read_comm(pid_t pid, char *buf, size_t len)
{
    char path[64];
    FILE *fp;
    snprintf(path, sizeof(path), "/proc/%ld/comm", (long)pid);
    fp = fopen(path, "r");
    if (fp == NULL || fgets(buf, (int)len, fp) == NULL) snprintf(buf, len, "unknown");
    trim_right(buf);
    if (fp != NULL) fclose(fp);
}

static void read_cmdline(pid_t pid, char *buf, size_t len)
{
    char path[64];
    FILE *fp;
    size_t n;
    if (len == 0) return;
    buf[0] = '\0';
    snprintf(path, sizeof(path), "/proc/%ld/cmdline", (long)pid);
    fp = fopen(path, "r");
    if (fp == NULL) return;
    n = fread(buf, 1, len - 1, fp);
    fclose(fp);
    buf[n] = '\0';
    for (size_t i = 0; i < n; i++) if (buf[i] == '\0') buf[i] = ' ';
    trim_right(buf);
}

static void read_exe_path(pid_t pid, char *buf, size_t len)
{
    char path[64];
    ssize_t n;
    snprintf(path, sizeof(path), "/proc/%ld/exe", (long)pid);
    n = readlink(path, buf, len - 1);
    if (n < 0) {
        buf[0] = '\0';
        return;
    }
    buf[n] = '\0';
}

static int discover_app_pid(const char *keyword)
{
    DIR *dir = opendir("/proc");
    struct dirent *ent;
    int found = -1;
    int count = 0;
    pid_t self_pid = getpid();
    pid_t parent_pid = getppid();
    if (dir == NULL) return -1;
    while ((ent = readdir(dir)) != NULL) {
        char *end = NULL;
        long pid_long = strtol(ent->d_name, &end, 10);
        if (end == ent->d_name || *end != '\0' || pid_long <= 0 || pid_long > INT_MAX) continue;
        pid_t pid = (pid_t)pid_long;
        char comm[256], cmdline[1024];
        if (pid == self_pid || pid == parent_pid) continue;
        read_comm(pid, comm, sizeof(comm));
        read_cmdline(pid, cmdline, sizeof(cmdline));
        if (strstr(comm, keyword) != NULL || strstr(cmdline, keyword) != NULL) {
            found = pid;
            count++;
        }
    }
    closedir(dir);
    if (count != 1) {
        fprintf(stderr, "--app `%s` 匹配到 %d 个 PID；为避免误标记 PFN，要求只匹配一个 PID\n", keyword, count);
        return -1;
    }
    return found;
}

static bool parse_maps_header(const char *line, Vma *vma)
{
    unsigned long long start = 0, end = 0, offset = 0, inode = 0;
    char perms[8] = {0};
    char dev[32] = {0};
    int path_pos = 0;
    int matched;
    memset(vma, 0, sizeof(*vma));
    matched = sscanf(line, "%llx-%llx %7s %llx %31s %llu %n", &start, &end, perms, &offset, dev, &inode, &path_pos);
    if (matched < 6) return false;
    vma->start = start;
    vma->end = end;
    vma->offset = offset;
    vma->inode = inode;
    snprintf(vma->perms, sizeof(vma->perms), "%s", perms);
    snprintf(vma->dev, sizeof(vma->dev), "%s", dev);
    if (path_pos > 0 && line[path_pos] != '\0') {
        char tmp[PATH_MAX];
        snprintf(tmp, sizeof(tmp), "%s", line + path_pos);
        trim_right(tmp);
        snprintf(vma->path, sizeof(vma->path), "%s", trim_left(tmp));
    }
    return true;
}

static bool parse_maps(pid_t pid, VmaList *list)
{
    char path[64];
    FILE *fp;
    char *line = NULL;
    size_t line_cap = 0;
    bool ok = true;
    snprintf(path, sizeof(path), "/proc/%ld/maps", (long)pid);
    fp = fopen(path, "r");
    if (fp == NULL) return false;
    while (getline(&line, &line_cap, fp) != -1) {
        Vma vma;
        if (!parse_maps_header(line, &vma) || !vma_list_push(list, &vma)) {
            ok = false;
            break;
        }
    }
    free(line);
    fclose(fp);
    return ok;
}

static void classify_segments(VmaList *list, const char *exe_path)
{
    for (size_t i = 0; i < list->count; i++) {
        Vma *v = &list->items[i];
        bool is_main = exe_path[0] != '\0' && path_equal_ignoring_deleted(v->path, exe_path);
        if (is_heap_path(v->path)) v->segment = SEG_HEAP;
        else if (starts_with(v->path, "[stack")) v->segment = SEG_STACK;
        else if (is_special_path(v->path)) v->segment = SEG_SPECIAL;
        else if (is_main && strchr(v->perms, 'x') != NULL) v->segment = SEG_TEXT;
        else if (is_main && v->perms[0] == 'r' && v->perms[1] == 'w') v->segment = SEG_DATA;
        else if (v->inode == 0 && v->path[0] == '\0') v->segment = SEG_ANON;
        else if (v->path[0] != '\0') v->segment = SEG_FILE;
        else v->segment = SEG_UNKNOWN;
    }
    for (size_t i = 1; i < list->count; i++) {
        Vma *prev = &list->items[i - 1];
        Vma *v = &list->items[i];
        if (prev->segment == SEG_DATA && v->segment == SEG_ANON &&
            v->perms[0] == 'r' && v->perms[1] == 'w' && v->perms[3] == 'p' && v->start == prev->end) {
            v->segment = SEG_BSS;
        }
    }
}

static bool parse_range(const char *text, Range *range)
{
    unsigned long long start = 0, end = 0;
    if (sscanf(text, "%llx-%llx", &start, &end) != 2 || end <= start) return false;
    range->start = start;
    range->end = end;
    return true;
}

static bool overlaps(uint64_t a_start, uint64_t a_end, uint64_t b_start, uint64_t b_end)
{
    return a_start < b_end && b_start < a_end;
}

static bool vma_selected(const Vma *v, const RangeList *ranges, const bool segment_filter[SEG_COUNT])
{
    bool any_segment = false;
    for (int i = 0; i < SEG_COUNT; i++) if (segment_filter[i]) any_segment = true;
    if (any_segment && !segment_filter[v->segment]) return false;
    if (ranges->count == 0) return true;
    for (size_t i = 0; i < ranges->count; i++) {
        if (overlaps(v->start, v->end, ranges->items[i].start, ranges->items[i].end)) return true;
    }
    return false;
}

static bool collect_pages(pid_t pid, const VmaList *vmas, const RangeList *ranges,
                          const bool segment_filter[SEG_COUNT], PageList *pages, long page_size)
{
    char path[64];
    int fd;
    snprintf(path, sizeof(path), "/proc/%ld/pagemap", (long)pid);
    fd = open(path, O_RDONLY);
    if (fd < 0) {
        perror(path);
        return false;
    }
    for (size_t i = 0; i < vmas->count; i++) {
        const Vma *v = &vmas->items[i];
        if (!vma_selected(v, ranges, segment_filter)) continue;
        char vma_label[40];
        snprintf(vma_label, sizeof(vma_label), "%012" PRIx64 "-%012" PRIx64, v->start, v->end);
        for (uint64_t addr = v->start; addr < v->end; addr += (uint64_t)page_size) {
            uint64_t entry = 0;
            off_t off = (off_t)((addr / (uint64_t)page_size) * sizeof(entry));
            PageRecord page;
            memset(&page, 0, sizeof(page));
            page.addr = addr;
            page.segment = v->segment;
            page.path = v->path[0] ? v->path : "(anonymous)";
            snprintf(page.vma_label, sizeof(page.vma_label), "%s", vma_label);
            if (pread(fd, &entry, sizeof(entry), off) != (ssize_t)sizeof(entry)) {
                page.state = PAGE_ERROR;
            } else if ((entry & PM_PRESENT) == 0) {
                page.state = PAGE_NOT_PRESENT;
            } else {
                page.pfn = entry & PM_PFN_MASK;
                page.state = page.pfn == 0 ? PAGE_PFN_HIDDEN : PAGE_IDLE;
            }
            if (!page_list_push(pages, &page)) {
                close(fd);
                return false;
            }
        }
    }
    close(fd);
    return true;
}

static bool mark_pfns_idle(const PageList *pages, const char *idle_bitmap, size_t *tracked)
{
    int fd = open(idle_bitmap, O_RDWR);
    if (fd < 0) {
        perror(idle_bitmap);
        return false;
    }
    const uint64_t bits_per_word = (uint64_t)(sizeof(unsigned long) * 8);
    *tracked = 0;
    for (size_t i = 0; i < pages->count; i++) {
        const PageRecord *p = &pages->items[i];
        if (p->pfn == 0) continue;
        unsigned long value = 1UL << (p->pfn % bits_per_word);
        off_t off = (off_t)((p->pfn / bits_per_word) * sizeof(unsigned long));
        if (pwrite(fd, &value, sizeof(value), off) != (ssize_t)sizeof(value)) {
            perror("write page_idle");
            close(fd);
            return false;
        }
        (*tracked)++;
    }
    close(fd);
    return true;
}

static bool update_idle_states(PageList *pages, const char *idle_bitmap)
{
    int fd = open(idle_bitmap, O_RDONLY);
    if (fd < 0) {
        perror(idle_bitmap);
        return false;
    }
    const uint64_t bits_per_word = (uint64_t)(sizeof(unsigned long) * 8);
    for (size_t i = 0; i < pages->count; i++) {
        PageRecord *p = &pages->items[i];
        if (p->pfn == 0) continue;
        unsigned long value = 0;
        off_t off = (off_t)((p->pfn / bits_per_word) * sizeof(unsigned long));
        if (pread(fd, &value, sizeof(value), off) != (ssize_t)sizeof(value)) {
            p->state = PAGE_ERROR;
            continue;
        }
        p->state = (value & (1UL << (p->pfn % bits_per_word))) ? PAGE_IDLE : PAGE_REFERENCED;
    }
    close(fd);
    return true;
}

static int run_operation(const char *script, pid_t pid, const char *app)
{
    if (script == NULL) {
        printf("已标记 PFN 为 idle。现在执行用户操作，完成后按 Enter 继续读取 page_idle...");
        fflush(stdout);
        while (getchar() != '\n') {}
        return 0;
    }

    const char *sudo_user = getenv("SUDO_USER");
    char cmd[PATH_MAX * 2];
    if (geteuid() == 0 && sudo_user != NULL && strcmp(sudo_user, "root") != 0) {
        snprintf(cmd, sizeof(cmd), "sudo -u '%s' -- '%s' '%ld' '%s'", sudo_user, script, (long)pid, app ? app : "");
    } else {
        snprintf(cmd, sizeof(cmd), "'%s' '%ld' '%s'", script, (long)pid, app ? app : "");
    }
    return system(cmd);
}

static bool write_tsv(const char *path, const PageList *pages)
{
    if (!ensure_parent_dir(path)) return false;
    FILE *out = fopen(path, "w");
    if (out == NULL) return false;
    fprintf(out, "addr\tsegment\tvma\tstate\tpfn\tpath\n");
    for (size_t i = 0; i < pages->count; i++) {
        const PageRecord *p = &pages->items[i];
        fprintf(out, "%012" PRIx64 "\t%s\t%s\t%s\t%" PRIx64 "\t%s\n",
                p->addr, segment_token(p->segment), p->vma_label, state_token(p->state), p->pfn, p->path);
    }
    fclose(out);
    return true;
}

static bool write_bitmap(const char *path, const PageList *pages, long page_size, pid_t pid)
{
    if (!ensure_parent_dir(path)) return false;
    FILE *out = fopen(path, "w");
    if (out == NULL) return false;
    fprintf(out, "# page_idle_bitmap_v1\n");
    fprintf(out, "pid\t%ld\n", (long)pid);
    fprintf(out, "page_size\t%ld\n", page_size);
    fprintf(out, "legend\tR=referenced I=idle N=not_present H=pfn_hidden E=error\n\n");

    for (int seg = 0; seg < SEG_COUNT; seg++) {
        size_t total = 0, referenced = 0, tracked = 0;
        for (size_t i = 0; i < pages->count; i++) {
            const PageRecord *p = &pages->items[i];
            if ((int)p->segment != seg) continue;
            total++;
            if (p->pfn != 0) tracked++;
            if (p->state == PAGE_REFERENCED) referenced++;
        }
        if (total == 0) continue;
        fprintf(out, "## segment\t%s\ttotal=%zu\ttracked=%zu\treferenced=%zu\n", segment_token((SegmentKind)seg), total, tracked, referenced);
        size_t col = 0;
        for (size_t i = 0; i < pages->count; i++) {
            const PageRecord *p = &pages->items[i];
            if ((int)p->segment != seg) continue;
            fputc(state_code(p->state), out);
            if (++col % 128 == 0) fputc('\n', out);
        }
        if (col % 128 != 0) fputc('\n', out);
        fputc('\n', out);
    }
    fclose(out);
    return true;
}

int main(int argc, char **argv)
{
    pid_t pid = -1;
    const char *app = "";
    const char *operation = NULL;
    const char *out_tsv = "page_idle.tsv";
    const char *out_bitmap = "page_idle_bitmap.txt";
    const char *idle_bitmap = DEFAULT_IDLE_BITMAP;
    RangeList ranges = {0};
    bool segment_filter[SEG_COUNT] = {0};

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            usage(argv[0]);
            return 0;
        } else if (strcmp(argv[i], "--app") == 0) {
            if (++i >= argc) { usage(argv[0]); return 1; }
            app = argv[i];
            pid = discover_app_pid(app);
            if (pid <= 0) return 1;
        } else if (strcmp(argv[i], "-s") == 0 || strcmp(argv[i], "--operation") == 0) {
            if (++i >= argc) { usage(argv[0]); return 1; }
            operation = argv[i];
        } else if (strcmp(argv[i], "-o") == 0 || strcmp(argv[i], "--output") == 0 || strcmp(argv[i], "--tsv") == 0) {
            if (++i >= argc) { usage(argv[0]); return 1; }
            out_tsv = argv[i];
        } else if (strcmp(argv[i], "--bitmap") == 0) {
            if (++i >= argc) { usage(argv[0]); return 1; }
            out_bitmap = argv[i];
        } else if (strcmp(argv[i], "--idle-bitmap") == 0) {
            if (++i >= argc) { usage(argv[0]); return 1; }
            idle_bitmap = argv[i];
        } else if (strcmp(argv[i], "--vma") == 0) {
            Range r;
            if (++i >= argc || !parse_range(argv[i], &r) || !range_list_push(&ranges, r)) {
                fprintf(stderr, "非法 --vma 参数\n");
                return 1;
            }
        } else if (strcmp(argv[i], "--segment") == 0) {
            if (++i >= argc) { usage(argv[0]); return 1; }
            SegmentKind s = parse_segment(argv[i]);
            if (s == SEG_UNKNOWN && strcmp(argv[i], "unknown") != 0) {
                fprintf(stderr, "非法 segment: %s\n", argv[i]);
                return 1;
            }
            segment_filter[s] = true;
        } else {
            char *end = NULL;
            long pid_long = strtol(argv[i], &end, 10);
            if (end == argv[i] || *end != '\0' || pid_long <= 0 || pid_long > INT_MAX || pid > 0) {
                usage(argv[0]);
                return 1;
            }
            pid = (pid_t)pid_long;
        }
    }

    if (pid <= 0) {
        usage(argv[0]);
        return 1;
    }

    long page_size = sysconf(_SC_PAGESIZE);
    if (page_size <= 0) page_size = 4096;

    VmaList vmas = {0};
    PageList pages = {0};
    char exe_path[PATH_MAX];
    read_exe_path(pid, exe_path, sizeof(exe_path));
    if (!parse_maps(pid, &vmas)) {
        perror("parse maps");
        return 1;
    }
    classify_segments(&vmas, exe_path);
    if (!collect_pages(pid, &vmas, &ranges, segment_filter, &pages, page_size)) return 1;
    if (pages.count == 0) {
        fprintf(stderr, "没有匹配的页\n");
        return 1;
    }
    size_t tracked = 0;
    if (!mark_pfns_idle(&pages, idle_bitmap, &tracked)) return 1;
    printf("marked %zu PFN(s) idle\n", tracked);
    if (run_operation(operation, pid, app) != 0) return 1;
    if (!update_idle_states(&pages, idle_bitmap)) return 1;
    if (!write_tsv(out_tsv, &pages)) return 1;
    if (!write_bitmap(out_bitmap, &pages, page_size, pid)) return 1;
    printf("wrote %s\n", out_tsv);
    printf("wrote %s\n", out_bitmap);
    free(vmas.items);
    free(pages.items);
    free(ranges.items);
    return 0;
}
