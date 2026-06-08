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
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include "page_access_uapi.h"

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
    uint64_t tracked;
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
            "  sudo %s <pid> -o page_access.tsv --bitmap page_access_bitmap.txt [-s user_operation.sh]\n"
            "  sudo %s --app firefox -o page_access.tsv --bitmap page_access_bitmap.txt [-s user_operation.sh]\n\n"
            "说明:\n"
            "  v8 不使用 /sys/kernel/mm/page_idle/bitmap。它通过 /dev/v8_page_access ioctl\n"
            "  调用内核模块清除/查询 PTE young(accessed) bit。\n\n"
            "可选过滤:\n"
            "  --vma start-end      只跟踪指定虚拟地址范围，可重复\n"
            "  --segment heap       只跟踪指定 segment，可重复\n"
            "  --device path        指定内核模块设备，默认 /dev/v8_page_access\n",
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
        fprintf(stderr, "--app `%s` 匹配到 %d 个 PID；为避免误测，要求只匹配一个 PID\n", keyword, count);
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
    if (fp == NULL) {
        perror(path);
        return false;
    }
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

static bool segment_selected(const Vma *v, const bool segment_filter[SEG_COUNT])
{
    bool any_segment = false;
    for (int i = 0; i < SEG_COUNT; i++) if (segment_filter[i]) any_segment = true;
    return !any_segment || segment_filter[v->segment];
}

static PageState convert_kernel_state(uint8_t state)
{
    switch (state) {
    case V8_PAGE_REFERENCED: return PAGE_REFERENCED;
    case V8_PAGE_IDLE: return PAGE_IDLE;
    case V8_PAGE_ABSENT: return PAGE_NOT_PRESENT;
    default: return PAGE_ERROR;
    }
}

static bool each_selected_range(const Vma *v, const RangeList *ranges, uint64_t *start, uint64_t *end, size_t *idx)
{
    if (ranges->count == 0) {
        if (*idx > 0) return false;
        *idx = 1;
        *start = v->start;
        *end = v->end;
        return true;
    }
    while (*idx < ranges->count) {
        const Range *r = &ranges->items[(*idx)++];
        uint64_t s = v->start > r->start ? v->start : r->start;
        uint64_t e = v->end < r->end ? v->end : r->end;
        if (overlaps(v->start, v->end, r->start, r->end) && s < e) {
            *start = s;
            *end = e;
            return true;
        }
    }
    return false;
}

static bool clear_selected_ranges(int dev_fd, pid_t pid, const VmaList *vmas, const RangeList *ranges,
                                  const bool segment_filter[SEG_COUNT], long page_size, size_t *page_count)
{
    *page_count = 0;
    for (size_t i = 0; i < vmas->count; i++) {
        const Vma *v = &vmas->items[i];
        size_t idx = 0;
        uint64_t start, end;
        if (!segment_selected(v, segment_filter)) continue;
        while (each_selected_range(v, ranges, &start, &end, &idx)) {
            struct v8_page_access_range req;
            start &= ~((uint64_t)page_size - 1);
            end = (end + (uint64_t)page_size - 1) & ~((uint64_t)page_size - 1);
            memset(&req, 0, sizeof(req));
            req.pid = pid;
            req.start = start;
            req.end = end;
            if (ioctl(dev_fd, V8_PAGE_ACCESS_CLEAR, &req) != 0) {
                perror("ioctl CLEAR");
                return false;
            }
            *page_count += (size_t)((end - start) / (uint64_t)page_size);
        }
    }
    return true;
}

static bool query_selected_ranges(int dev_fd, pid_t pid, const VmaList *vmas, const RangeList *ranges,
                                  const bool segment_filter[SEG_COUNT], PageList *pages, long page_size)
{
    for (size_t i = 0; i < vmas->count; i++) {
        const Vma *v = &vmas->items[i];
        size_t idx = 0;
        uint64_t start, end;
        char vma_label[40];
        if (!segment_selected(v, segment_filter)) continue;
        snprintf(vma_label, sizeof(vma_label), "%012" PRIx64 "-%012" PRIx64, v->start, v->end);
        while (each_selected_range(v, ranges, &start, &end, &idx)) {
            struct v8_page_access_info *infos;
            struct v8_page_access_query req;
            size_t count;
            start &= ~((uint64_t)page_size - 1);
            end = (end + (uint64_t)page_size - 1) & ~((uint64_t)page_size - 1);
            count = (size_t)((end - start) / (uint64_t)page_size);
            if (count == 0 || count > UINT_MAX) {
                fprintf(stderr, "查询范围过大或为空: %" PRIx64 "-%" PRIx64 "\n", start, end);
                return false;
            }
            infos = calloc(count, sizeof(*infos));
            if (infos == NULL) return false;
            memset(&req, 0, sizeof(req));
            req.pid = pid;
            req.start = start;
            req.end = end;
            req.page_count = (uint32_t)count;
            req.pages_ptr = (uint64_t)(uintptr_t)infos;
            if (ioctl(dev_fd, V8_PAGE_ACCESS_QUERY, &req) != 0) {
                perror("ioctl QUERY");
                free(infos);
                return false;
            }
            for (size_t j = 0; j < count; j++) {
                PageRecord page;
                memset(&page, 0, sizeof(page));
                page.addr = infos[j].vaddr;
                page.segment = v->segment;
                page.path = v->path[0] ? v->path : "(anonymous)";
                page.state = convert_kernel_state(infos[j].state);
                page.tracked = (page.state == PAGE_REFERENCED || page.state == PAGE_IDLE) ? 1 : 0;
                snprintf(page.vma_label, sizeof(page.vma_label), "%s", vma_label);
                if (!page_list_push(pages, &page)) {
                    free(infos);
                    return false;
                }
            }
            free(infos);
        }
    }
    return true;
}

static int run_operation(const char *script, pid_t pid, const char *app)
{
    if (script == NULL) {
        printf("已清除 young/accessed bit。现在执行用户操作，完成后按 Enter 继续查询...");
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
                p->addr, segment_token(p->segment), p->vma_label, state_token(p->state), p->tracked, p->path);
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
    fprintf(out, "source\tv8_young_bit\n");
    fprintf(out, "pid\t%ld\n", (long)pid);
    fprintf(out, "page_size\t%ld\n", page_size);
    fprintf(out, "legend\tR=referenced I=idle N=not_present H=pfn_hidden E=error\n\n");

    for (int seg = 0; seg < SEG_COUNT; seg++) {
        size_t total = 0, referenced = 0, tracked = 0;
        for (size_t i = 0; i < pages->count; i++) {
            const PageRecord *p = &pages->items[i];
            if ((int)p->segment != seg) continue;
            total++;
            if (p->tracked) tracked++;
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
    const char *out_tsv = "page_access.tsv";
    const char *out_bitmap = "page_access_bitmap.txt";
    const char *device = V8_PAGE_ACCESS_DEVICE;
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
        } else if (strcmp(argv[i], "--device") == 0) {
            if (++i >= argc) { usage(argv[0]); return 1; }
            device = argv[i];
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
    int dev_fd;
    size_t target_pages = 0;

    read_exe_path(pid, exe_path, sizeof(exe_path));
    if (!parse_maps(pid, &vmas)) {
        fprintf(stderr, "无法读取目标进程 maps，请确认 PID 存在且是用户态进程\n");
        return 1;
    }
    classify_segments(&vmas, exe_path);

    dev_fd = open(device, O_RDWR);
    if (dev_fd < 0) {
        perror(device);
        fprintf(stderr, "请先编译并加载 v8_page_access.ko，确认存在 %s\n", device);
        return 1;
    }

    if (!clear_selected_ranges(dev_fd, pid, &vmas, &ranges, segment_filter, page_size, &target_pages)) return 1;
    if (target_pages == 0) {
        fprintf(stderr, "没有匹配的页\n");
        return 1;
    }
    printf("cleared young/accessed bit for %zu virtual page(s)\n", target_pages);
    if (run_operation(operation, pid, app) != 0) return 1;
    if (!query_selected_ranges(dev_fd, pid, &vmas, &ranges, segment_filter, &pages, page_size)) return 1;
    if (!write_tsv(out_tsv, &pages)) return 1;
    if (!write_bitmap(out_bitmap, &pages, page_size, pid)) return 1;
    printf("wrote %s\n", out_tsv);
    printf("wrote %s\n", out_bitmap);
    close(dev_fd);
    free(vmas.items);
    free(pages.items);
    free(ranges.items);
    return 0;
}
