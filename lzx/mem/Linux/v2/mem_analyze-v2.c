#define _GNU_SOURCE

#include <errno.h>
#include <ctype.h>
#include <fcntl.h>
#include <inttypes.h>
#include <limits.h>
#include <dirent.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

#define MAX_FIELDS 96
#define FIELD_KEY_LEN 64
#define FIELD_VALUE_LEN 128
#define SPLIT_REPORT_THRESHOLD (1024 * 1024)

#define PM_PRESENT   (1ULL << 63)
#define PM_SWAPPED   (1ULL << 62)
#define PM_FILE      (1ULL << 61)
#define PM_SOFT_DIRTY (1ULL << 55)
#define PM_EXCLUSIVE (1ULL << 56)
#define PM_PFN_MASK  ((1ULL << 55) - 1)

#define PAGE_CODE_PRESENT     1U
#define PAGE_CODE_SOFT_DIRTY  2U
#define PAGE_CODE_SWAPPED     4U
#define PAGE_CODE_EXCLUSIVE   8U
#define PAGE_CODE_FILE_SHARED 16U
#define PAGE_CODE_PFN_KNOWN   32U

typedef enum {
    SEG_TEXT = 0,
    SEG_INIT_DATA,
    SEG_BSS,
    SEG_HEAP,
    SEG_STACK,
    SEG_FILE,
    SEG_ANON,
    SEG_SPECIAL,
    SEG_UNKNOWN,
    SEG_COUNT
} SegmentKind;

typedef struct {
    char key[FIELD_KEY_LEN];
    char value[FIELD_VALUE_LEN];
} SmapField;

typedef struct {
    unsigned long long virtual_pages;
    unsigned long long present_pages;
    unsigned long long swapped_pages;
    unsigned long long not_present_pages;
    unsigned long long soft_dirty_pages;
    unsigned long long exclusive_pages;
    unsigned long long file_or_shared_pages;
    unsigned long long pfn_runs;
    uint64_t pfn_min;
    uint64_t pfn_max;
    uint64_t last_pfn;
    bool has_pfn;
    bool available;
} PageStats;

typedef struct {
    uint64_t start;
    uint64_t end;
    uint64_t offset;
    unsigned long long inode;
    char perms[8];
    char dev[32];
    char path[PATH_MAX];
    SegmentKind segment;
    long size_kb;
    long rss_kb;
    long pss_kb;
    long swap_kb;
    long swappss_kb;
    long referenced_kb;
    long private_clean_kb;
    long private_dirty_kb;
    long shared_clean_kb;
    long shared_dirty_kb;
    SmapField fields[MAX_FIELDS];
    size_t field_count;
    PageStats pages;
    char *page_states;
    uint64_t *page_pfns;
    unsigned char *page_codes;
} Vma;

typedef struct {
    Vma *items;
    size_t count;
    size_t cap;
} VmaList;

typedef struct {
    uint64_t vaddr_start;
    uint64_t vaddr_end;
    uint64_t file_backed_end;
    bool valid;
} LoadSeg;

typedef struct {
    LoadSeg loads[16];
    size_t load_count;
    uint64_t load_bias;
    bool is_elf64;
    bool valid;
} ExeLayout;

typedef struct {
    unsigned long long virtual_pages;
    unsigned long long present_pages;
    unsigned long long swapped_pages;
    unsigned long long not_present_pages;
    long size_kb;
    long rss_kb;
    long pss_kb;
    long swap_kb;
} SegmentSummary;

typedef struct {
    const Vma *vma;
    uint64_t start;
    uint64_t end;
    SegmentKind segment;
    PageStats pages;
} LogicalRegion;

typedef struct {
    LogicalRegion *items;
    size_t count;
    size_t cap;
} LogicalRegionList;

typedef struct {
    bool valid;
    pid_t pid;
    char comm[256];
    char cmdline[512];
    long size_kb;
    long rss_kb;
    long pss_kb;
    long swap_kb;
    unsigned long long virtual_pages;
    unsigned long long present_pages;
    unsigned long long swapped_pages;
    unsigned long long not_present_pages;
    unsigned long long present_kb;
    unsigned long long not_present_kb;
} WatchSample;

typedef struct {
    pid_t pid;
    char comm[256];
    char cmdline[512];
    WatchSample *samples;
    size_t sample_count;
    size_t sample_cap;
    char *first_report;
    char *last_report;
    int first_report_sample;
    int last_report_sample;
    char detail_link[PATH_MAX];
} ProcSeries;

typedef struct {
    ProcSeries *items;
    size_t count;
    size_t cap;
} SeriesList;

static const char *segment_name(SegmentKind s)
{
    switch (s) {
    case SEG_TEXT: return "text/代码段";
    case SEG_INIT_DATA: return "data/已初始化数据段";
    case SEG_BSS: return "bss/未初始化数据段";
    case SEG_HEAP: return "heap/堆";
    case SEG_STACK: return "stack/栈";
    case SEG_FILE: return "file/文件映射";
    case SEG_ANON: return "anon/匿名映射";
    case SEG_SPECIAL: return "special/内核特殊映射";
    default: return "unknown/未知";
    }
}

static void usage(const char *argv0)
{
    fprintf(stderr,
            "用法: sudo %s <pid> [-o report.md]\n"
            "也支持多个 PID: sudo %s <pid1> <pid2> ... [-o report.md]\n"
            "监控 app: sudo %s --watch-app firefox --duration 60 --interval 2 -o firefox_watch.md\n"
            "监控 PID: sudo %s --watch 60 --interval 2 <pid1> <pid2> -o watch.md\n",
            argv0, argv0, argv0, argv0);
}

static char *trim_left(char *s)
{
    while (*s == ' ' || *s == '\t') {
        s++;
    }
    return s;
}

static void trim_right(char *s)
{
    size_t n = strlen(s);
    while (n > 0 && (s[n - 1] == '\n' || s[n - 1] == '\r' ||
                     s[n - 1] == ' ' || s[n - 1] == '\t')) {
        s[--n] = '\0';
    }
}

static bool starts_with(const char *s, const char *prefix)
{
    return strncmp(s, prefix, strlen(prefix)) == 0;
}

static bool mkdir_p(const char *path)
{
    char tmp[PATH_MAX];
    size_t len;

    if (path[0] == '\0') {
        return true;
    }
    if (snprintf(tmp, sizeof(tmp), "%s", path) >= (int)sizeof(tmp)) {
        errno = ENAMETOOLONG;
        return false;
    }

    len = strlen(tmp);
    while (len > 1 && tmp[len - 1] == '/') {
        tmp[--len] = '\0';
    }

    for (char *p = tmp + 1; *p != '\0'; p++) {
        if (*p != '/') {
            continue;
        }
        *p = '\0';
        if (mkdir(tmp, 0755) != 0 && errno != EEXIST) {
            return false;
        }
        *p = '/';
    }

    if (mkdir(tmp, 0755) != 0 && errno != EEXIST) {
        return false;
    }
    return true;
}

static bool build_run_output_path(const char *requested, char *buf, size_t len)
{
    char parent[PATH_MAX] = ".";
    const char *filename = requested;
    char run_dir[64];
    time_t now = time(NULL);
    struct tm tm_now;
    const char *slash = strrchr(requested, '/');
    int written;

    if (slash != NULL) {
        size_t parent_len = (size_t)(slash - requested);
        if (parent_len == 0) {
            parent_len = 1;
        }
        if (parent_len >= sizeof(parent)) {
            errno = ENAMETOOLONG;
            return false;
        }
        memcpy(parent, requested, parent_len);
        parent[parent_len] = '\0';
        filename = slash + 1;
    }

    if (filename[0] == '\0') {
        filename = "report.md";
    }
    if (!mkdir_p(parent)) {
        return false;
    }

    localtime_r(&now, &tm_now);
    strftime(run_dir, sizeof(run_dir), "mem_analyze_run_%Y%m%d_%H%M%S", &tm_now);

    if (strcmp(parent, ".") == 0) {
        written = snprintf(buf, len, "%s/%s", run_dir, filename);
    } else {
        written = snprintf(buf, len, "%s/%s/%s", parent, run_dir, filename);
    }
    if (written < 0 || (size_t)written >= len) {
        errno = ENAMETOOLONG;
        return false;
    }

    char out_dir[PATH_MAX];
    const char *last_slash = strrchr(buf, '/');
    if (last_slash == NULL) {
        return true;
    }
    size_t out_dir_len = (size_t)(last_slash - buf);
    if (out_dir_len >= sizeof(out_dir)) {
        errno = ENAMETOOLONG;
        return false;
    }
    memcpy(out_dir, buf, out_dir_len);
    out_dir[out_dir_len] = '\0';
    return mkdir_p(out_dir);
}

static bool is_header_line(const char *line)
{
    unsigned long long a = 0, b = 0;
    char perms[8] = {0};
    return sscanf(line, "%llx-%llx %7s", &a, &b, perms) == 3 &&
           strchr(perms, '-') != NULL;
}

static bool path_equal_ignoring_deleted(const char *a, const char *b)
{
    size_t na = strlen(a);
    size_t nb = strlen(b);
    const char *deleted = " (deleted)";

    if (strcmp(a, b) == 0) {
        return true;
    }
    if (na > strlen(deleted) && strcmp(a + na - strlen(deleted), deleted) == 0) {
        na -= strlen(deleted);
    }
    if (nb > strlen(deleted) && strcmp(b + nb - strlen(deleted), deleted) == 0) {
        nb -= strlen(deleted);
    }
    return na == nb && strncmp(a, b, na) == 0;
}

static bool is_special_path(const char *path)
{
    return starts_with(path, "[vdso]") || starts_with(path, "[vvar]") ||
           starts_with(path, "[vsyscall]") || starts_with(path, "[anon:") ||
           starts_with(path, "[rollup]");
}

static void vma_list_free(VmaList *list)
{
    for (size_t i = 0; i < list->count; i++) {
        free(list->items[i].page_states);
        free(list->items[i].page_pfns);
        free(list->items[i].page_codes);
    }
    free(list->items);
    list->items = NULL;
    list->count = 0;
    list->cap = 0;
}

static void logical_region_list_free(LogicalRegionList *list)
{
    free(list->items);
    list->items = NULL;
    list->count = 0;
    list->cap = 0;
}

static bool vma_list_push(VmaList *list, const Vma *vma)
{
    if (list->count == list->cap) {
        size_t new_cap = list->cap == 0 ? 64 : list->cap * 2;
        Vma *new_items = realloc(list->items, new_cap * sizeof(*new_items));
        if (new_items == NULL) {
            return false;
        }
        list->items = new_items;
        list->cap = new_cap;
    }
    list->items[list->count++] = *vma;
    return true;
}

static bool logical_region_list_push(LogicalRegionList *list, const LogicalRegion *region)
{
    if (list->count == list->cap) {
        size_t new_cap = list->cap == 0 ? 64 : list->cap * 2;
        LogicalRegion *new_items = realloc(list->items, new_cap * sizeof(*new_items));
        if (new_items == NULL) {
            return false;
        }
        list->items = new_items;
        list->cap = new_cap;
    }
    list->items[list->count++] = *region;
    return true;
}

static bool parse_maps_header(const char *line, Vma *vma)
{
    unsigned long long start = 0, end = 0, offset = 0, inode = 0;
    char perms[8] = {0};
    char dev[32] = {0};
    int path_pos = 0;

    memset(vma, 0, sizeof(*vma));
    vma->segment = SEG_UNKNOWN;
    vma->size_kb = -1;
    vma->rss_kb = -1;
    vma->pss_kb = -1;
    vma->swap_kb = -1;
    vma->swappss_kb = -1;
    vma->referenced_kb = -1;
    vma->private_clean_kb = -1;
    vma->private_dirty_kb = -1;
    vma->shared_clean_kb = -1;
    vma->shared_dirty_kb = -1;

    int matched = sscanf(line, "%llx-%llx %7s %llx %31s %llu %n",
                         &start, &end, perms, &offset, dev, &inode, &path_pos);
    if (matched < 6) {
        return false;
    }

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

static void add_smap_field(Vma *vma, const char *key, const char *value)
{
    if (vma->field_count >= MAX_FIELDS) {
        return;
    }
    snprintf(vma->fields[vma->field_count].key, FIELD_KEY_LEN, "%s", key);
    snprintf(vma->fields[vma->field_count].value, FIELD_VALUE_LEN, "%s", value);
    vma->field_count++;
}

static long parse_kb_value(const char *value)
{
    long kb = -1;
    if (sscanf(value, "%ld", &kb) == 1) {
        return kb;
    }
    return -1;
}

static void apply_smap_value(Vma *vma, const char *key, const char *value)
{
    long kb = parse_kb_value(value);

    if (strcmp(key, "Size") == 0) vma->size_kb = kb;
    else if (strcmp(key, "Rss") == 0) vma->rss_kb = kb;
    else if (strcmp(key, "Pss") == 0) vma->pss_kb = kb;
    else if (strcmp(key, "Swap") == 0) vma->swap_kb = kb;
    else if (strcmp(key, "SwapPss") == 0) vma->swappss_kb = kb;
    else if (strcmp(key, "Referenced") == 0) vma->referenced_kb = kb;
    else if (strcmp(key, "Private_Clean") == 0) vma->private_clean_kb = kb;
    else if (strcmp(key, "Private_Dirty") == 0) vma->private_dirty_kb = kb;
    else if (strcmp(key, "Shared_Clean") == 0) vma->shared_clean_kb = kb;
    else if (strcmp(key, "Shared_Dirty") == 0) vma->shared_dirty_kb = kb;
}

static bool parse_maps(pid_t pid, VmaList *list, char *err, size_t err_len)
{
    char path[64];
    FILE *fp = NULL;
    char *line = NULL;
    size_t line_cap = 0;
    bool ok = true;

    snprintf(path, sizeof(path), "/proc/%ld/maps", (long)pid);
    fp = fopen(path, "r");
    if (fp == NULL) {
        snprintf(err, err_len, "cannot read %s: %s", path, strerror(errno));
        return false;
    }

    while (getline(&line, &line_cap, fp) != -1) {
        Vma vma;
        if (!parse_maps_header(line, &vma)) {
            snprintf(err, err_len, "cannot parse maps line: %s", line);
            ok = false;
            break;
        }
        if (!vma_list_push(list, &vma)) {
            snprintf(err, err_len, "out of memory while saving VMA information");
            ok = false;
            break;
        }
    }

    free(line);
    fclose(fp);
    return ok;
}

static Vma *find_matching_vma(VmaList *list, const Vma *header, size_t *next_index)
{
    for (size_t pass = 0; pass < 2; pass++) {
        size_t start = pass == 0 ? *next_index : 0;
        size_t end = pass == 0 ? list->count : *next_index;
        for (size_t i = start; i < end; i++) {
            Vma *v = &list->items[i];
            if (v->start == header->start &&
                v->end == header->end &&
                strcmp(v->perms, header->perms) == 0 &&
                v->offset == header->offset &&
                v->inode == header->inode) {
                *next_index = i + 1;
                return v;
            }
        }
    }
    return NULL;
}

static bool parse_smaps_fields(pid_t pid, VmaList *list, char *err, size_t err_len)
{
    char path[64];
    FILE *fp = NULL;
    char *line = NULL;
    size_t line_cap = 0;
    size_t next_index = 0;
    Vma *current = NULL;
    bool ok = true;

    snprintf(path, sizeof(path), "/proc/%ld/smaps", (long)pid);
    fp = fopen(path, "r");
    if (fp == NULL) {
        snprintf(err, err_len, "cannot read %s: %s", path, strerror(errno));
        return false;
    }

    while (getline(&line, &line_cap, fp) != -1) {
        if (is_header_line(line)) {
            Vma header;
            if (!parse_maps_header(line, &header)) {
                snprintf(err, err_len, "cannot parse smaps header: %s", line);
                ok = false;
                break;
            }
            current = find_matching_vma(list, &header, &next_index);
            continue;
        }

        if (current != NULL) {
            char *colon = strchr(line, ':');
            if (colon != NULL) {
                *colon = '\0';
                char *key = trim_left(line);
                char *value = trim_left(colon + 1);
                trim_right(key);
                trim_right(value);
                add_smap_field(current, key, value);
                apply_smap_value(current, key, value);
            }
        }
    }

    free(line);
    fclose(fp);
    return ok;
}

static void read_comm(pid_t pid, char *buf, size_t len)
{
    char path[64];
    FILE *fp;

    snprintf(path, sizeof(path), "/proc/%ld/comm", (long)pid);
    fp = fopen(path, "r");
    if (fp == NULL) {
        snprintf(buf, len, "unknown");
        return;
    }
    if (fgets(buf, (int)len, fp) == NULL) {
        snprintf(buf, len, "unknown");
    }
    trim_right(buf);
    fclose(fp);
}

static void read_cmdline(pid_t pid, char *buf, size_t len)
{
    char path[64];
    FILE *fp;
    size_t n;

    if (len == 0) {
        return;
    }
    buf[0] = '\0';
    snprintf(path, sizeof(path), "/proc/%ld/cmdline", (long)pid);
    fp = fopen(path, "rb");
    if (fp == NULL) {
        return;
    }
    n = fread(buf, 1, len - 1, fp);
    fclose(fp);
    buf[n] = '\0';
    for (size_t i = 0; i < n; i++) {
        if (buf[i] == '\0') {
            buf[i] = ' ';
        }
    }
    trim_right(buf);
}

static bool read_exe_path(pid_t pid, char *buf, size_t len)
{
    char path[64];
    ssize_t n;

    snprintf(path, sizeof(path), "/proc/%ld/exe", (long)pid);
    n = readlink(path, buf, len - 1);
    if (n < 0) {
        buf[0] = '\0';
        return false;
    }
    buf[n] = '\0';
    return true;
}

static uint16_t rd16(const unsigned char *p)
{
    return (uint16_t)p[0] | ((uint16_t)p[1] << 8);
}

static uint32_t rd32(const unsigned char *p)
{
    return (uint32_t)p[0] | ((uint32_t)p[1] << 8) |
           ((uint32_t)p[2] << 16) | ((uint32_t)p[3] << 24);
}

static uint64_t rd64(const unsigned char *p)
{
    uint64_t v = 0;
    for (int i = 7; i >= 0; i--) {
        v = (v << 8) | p[i];
    }
    return v;
}

static uint64_t page_align_down(uint64_t v, long page_size)
{
    return v & ~((uint64_t)page_size - 1);
}

static uint64_t page_align_up(uint64_t v, long page_size)
{
    uint64_t ps = (uint64_t)page_size;
    return (v + ps - 1) & ~(ps - 1);
}

static bool load_exe_layout(const char *exe_path, const VmaList *list,
                            long page_size, ExeLayout *layout)
{
    FILE *fp = fopen(exe_path, "rb");//打开对应可执行文件
    unsigned char eh[64];
    uint16_t phnum, phentsize;
    uint64_t phoff;
    uint64_t min_vaddr = UINT64_MAX;
    uint64_t first_map_start = UINT64_MAX;

    memset(layout, 0, sizeof(*layout));
    if (fp == NULL) {
        return false;
    }
    if (fread(eh, 1, sizeof(eh), fp) != sizeof(eh)) {
        fclose(fp);
        return false;
    }
    if (eh[0] != 0x7f || eh[1] != 'E' || eh[2] != 'L' || eh[3] != 'F' ||
        eh[4] != 2 || eh[5] != 1) {
        fclose(fp);
        return false;
    }

    layout->is_elf64 = true;
    phoff = rd64(eh + 32);
    phentsize = rd16(eh + 54);
    phnum = rd16(eh + 56);
    if (phentsize < 56 || phnum == 0) {
        fclose(fp);
        return false;
    }

    if (fseek(fp, (long)phoff, SEEK_SET) != 0) {
        fclose(fp);
        return false;
    }

    for (uint16_t i = 0; i < phnum && layout->load_count < 16; i++) {
        unsigned char ph[128];
        if (fread(ph, 1, phentsize, fp) != phentsize) {
            break;
        }
        if (rd32(ph) != 1) {
            continue;
        }
        uint64_t vaddr = rd64(ph + 16);
        uint64_t filesz = rd64(ph + 32);
        uint64_t memsz = rd64(ph + 40);
        LoadSeg *seg = &layout->loads[layout->load_count++];
        seg->vaddr_start = page_align_down(vaddr, page_size);
        seg->vaddr_end = page_align_up(vaddr + memsz, page_size);
        seg->file_backed_end = page_align_up(vaddr + filesz, page_size);
        seg->valid = true;
        if (seg->vaddr_start < min_vaddr) {
            min_vaddr = seg->vaddr_start;
        }
    }
    fclose(fp);

    if (layout->load_count == 0 || min_vaddr == UINT64_MAX) {
        return false;
    }

    for (size_t i = 0; i < list->count; i++) {
        if (path_equal_ignoring_deleted(list->items[i].path, exe_path) &&
            list->items[i].start < first_map_start) {
            first_map_start = list->items[i].start;
        }
    }
    if (first_map_start == UINT64_MAX) {
        return false;
    }

    layout->load_bias = first_map_start - min_vaddr;
    layout->valid = true;
    for (size_t i = 0; i < layout->load_count; i++) {
        layout->loads[i].vaddr_start += layout->load_bias;
        layout->loads[i].vaddr_end += layout->load_bias;
        layout->loads[i].file_backed_end += layout->load_bias;
    }
    return true;
}

static bool overlaps(uint64_t a_start, uint64_t a_end, uint64_t b_start, uint64_t b_end)
{
    return a_start < b_end && b_start < a_end;
}

static bool overlaps_bss_tail(const Vma *vma, const ExeLayout *layout)
{
    if (!layout->valid) {
        return false;
    }
    for (size_t i = 0; i < layout->load_count; i++) {
        const LoadSeg *seg = &layout->loads[i];
        if (seg->vaddr_end > seg->file_backed_end &&
            overlaps(vma->start, vma->end, seg->file_backed_end, seg->vaddr_end)) {
            return true;
        }
    }
    return false;
}

static bool range_overlaps_bss_tail(uint64_t start, uint64_t end, const ExeLayout *layout)
{
    if (!layout->valid) {
        return false;
    }
    for (size_t i = 0; i < layout->load_count; i++) {
        const LoadSeg *seg = &layout->loads[i];
        if (seg->vaddr_end > seg->file_backed_end &&
            overlaps(start, end, seg->file_backed_end, seg->vaddr_end)) {
            return true;
        }
    }
    return false;
}

static void classify_segments(VmaList *list, const char *exe_path,
                              const ExeLayout *layout, long page_size)
{
    (void)page_size;
    for (size_t i = 0; i < list->count; i++) {
        Vma *v = &list->items[i];
        bool is_main = exe_path[0] != '\0' && path_equal_ignoring_deleted(v->path, exe_path);

        if (strcmp(v->path, "[heap]") == 0) {
            v->segment = SEG_HEAP;
        } else if (starts_with(v->path, "[stack")) {
            v->segment = SEG_STACK;
        } else if (is_special_path(v->path)) {
            v->segment = SEG_SPECIAL;
        } else if (is_main && strchr(v->perms, 'x') != NULL) {
            v->segment = SEG_TEXT;
        } else if (is_main && v->perms[0] == 'r' && v->perms[1] == 'w') {
            if (overlaps_bss_tail(v, layout) && v->inode == 0) {
                v->segment = SEG_BSS;
            } else {
                v->segment = SEG_INIT_DATA;
            }
        } else if (v->inode == 0 && v->path[0] == '\0') {
            v->segment = SEG_ANON;
        } else if (v->inode == 0 && overlaps_bss_tail(v, layout)) {
            v->segment = SEG_BSS;
        } else if (v->path[0] != '\0') {
            v->segment = SEG_FILE;
        } else {
            v->segment = SEG_UNKNOWN;
        }
    }

    for (size_t i = 1; i < list->count; i++) {
        Vma *prev = &list->items[i - 1];
        Vma *v = &list->items[i];
        if (prev->segment == SEG_INIT_DATA &&
            v->segment == SEG_ANON &&
            v->perms[0] == 'r' && v->perms[1] == 'w' && v->perms[3] == 'p' &&
            v->start == prev->end) {
            v->segment = SEG_BSS;
        }
    }
}

static int compare_u64(const void *a, const void *b)
{
    uint64_t av = *(const uint64_t *)a;
    uint64_t bv = *(const uint64_t *)b;
    return (av > bv) - (av < bv);
}

static void add_cut(uint64_t *cuts, size_t *count, uint64_t value,
                    uint64_t start, uint64_t end)
{
    if (value <= start || value >= end || *count >= 64) {
        return;
    }
    cuts[(*count)++] = value;
}

static SegmentKind classify_logical_region(const Vma *v, const char *exe_path,
                                           const ExeLayout *layout,
                                           uint64_t start, uint64_t end)
{
    bool is_main = exe_path[0] != '\0' && path_equal_ignoring_deleted(v->path, exe_path);

    if (strcmp(v->path, "[heap]") == 0) {
        return SEG_HEAP;
    }
    if (starts_with(v->path, "[stack")) {
        return SEG_STACK;
    }
    if (is_special_path(v->path)) {
        return SEG_SPECIAL;
    }
    if (is_main && strchr(v->perms, 'x') != NULL) {
        return SEG_TEXT;
    }
    if ((is_main || v->segment == SEG_INIT_DATA || v->segment == SEG_BSS) &&
        v->perms[0] == 'r' && v->perms[1] == 'w' &&
        range_overlaps_bss_tail(start, end, layout)) {
        return SEG_BSS;
    }
    if (is_main && v->perms[0] == 'r' && v->perms[1] == 'w') {
        return SEG_INIT_DATA;
    }
    return v->segment;
}

static bool build_logical_regions(const VmaList *list, const char *exe_path,
                                  const ExeLayout *layout, LogicalRegionList *regions)
{
    for (size_t i = 0; i < list->count; i++) {
        const Vma *v = &list->items[i];
        uint64_t cuts[64];
        size_t cut_count = 0;

        cuts[cut_count++] = v->start;
        cuts[cut_count++] = v->end;

        if (layout->valid) {
            for (size_t j = 0; j < layout->load_count; j++) {
                const LoadSeg *seg = &layout->loads[j];
                if (!overlaps(v->start, v->end, seg->vaddr_start, seg->vaddr_end)) {
                    continue;
                }
                add_cut(cuts, &cut_count, seg->vaddr_start, v->start, v->end);
                add_cut(cuts, &cut_count, seg->file_backed_end, v->start, v->end);
                add_cut(cuts, &cut_count, seg->vaddr_end, v->start, v->end);
            }
        }

        qsort(cuts, cut_count, sizeof(cuts[0]), compare_u64);
        for (size_t j = 1; j < cut_count; j++) {
            if (cuts[j] == cuts[j - 1]) {
                continue;
            }

            LogicalRegion region;
            memset(&region, 0, sizeof(region));
            region.vma = v;
            region.start = cuts[j - 1];
            region.end = cuts[j];
            region.segment = classify_logical_region(v, exe_path, layout,
                                                     region.start, region.end);
            if (!logical_region_list_push(regions, &region)) {
                return false;
            }
        }
    }
    return true;
}

static void analyze_pagemap(pid_t pid, VmaList *list, long page_size,
                            char *status, size_t status_len)
{
    char path[64];
    int fd;

    snprintf(path, sizeof(path), "/proc/%ld/pagemap", (long)pid);
    fd = open(path, O_RDONLY);
    if (fd < 0) {
        snprintf(status, status_len, "无法读取 %s: %s；报告将只使用 maps/smaps 字段。",
                 path, strerror(errno));
        return;
    }

    snprintf(status, status_len,
             "pagemap 已读取。注意：非 root/CAP_SYS_ADMIN 环境下 PFN 可能被内核置 0。");

    for (size_t i = 0; i < list->count; i++) {
        Vma *v = &list->items[i];
        PageStats *ps = &v->pages;
        size_t page_count = (size_t)((v->end - v->start) / (uint64_t)page_size);
        ps->available = true;
        ps->pfn_min = UINT64_MAX;
        ps->pfn_max = 0;
        free(v->page_states);
        free(v->page_pfns);
        free(v->page_codes);
        v->page_states = calloc(page_count + 1, sizeof(*v->page_states));
        v->page_pfns = calloc(page_count == 0 ? 1 : page_count, sizeof(*v->page_pfns));
        v->page_codes = calloc(page_count == 0 ? 1 : page_count, sizeof(*v->page_codes));
        if (v->page_states != NULL) {
            memset(v->page_states, '?', page_count);
            v->page_states[page_count] = '\0';
        }

        for (uint64_t addr = v->start; addr < v->end; addr += (uint64_t)page_size) {
            size_t page_index = (size_t)((addr - v->start) / (uint64_t)page_size);
            uint64_t entry = 0;
            off_t off = (off_t)((addr / (uint64_t)page_size) * sizeof(entry));
            ssize_t n = pread(fd, &entry, sizeof(entry), off);
            if (n != (ssize_t)sizeof(entry)) {
                ps->available = false;
                if (v->page_states != NULL) {
                    v->page_states[page_index] = '?';
                }
                break;
            }

            ps->virtual_pages++;
            if ((entry & PM_PRESENT) != 0) {
                uint64_t pfn = entry & PM_PFN_MASK;
                ps->present_pages++;
                if (v->page_codes != NULL) {
                    v->page_codes[page_index] |= PAGE_CODE_PRESENT;
                }
                if (v->page_states != NULL) {
                    v->page_states[page_index] = 'P';
                }
                if (v->page_pfns != NULL) {
                    v->page_pfns[page_index] = pfn;
                }
                if (pfn != 0) {
                    if (v->page_codes != NULL) {
                        v->page_codes[page_index] |= PAGE_CODE_PFN_KNOWN;
                    }
                    if (!ps->has_pfn) {
                        ps->pfn_min = pfn;
                        ps->pfn_max = pfn;
                        ps->pfn_runs = 1;
                        ps->has_pfn = true;
                    } else {
                        if (pfn < ps->pfn_min) ps->pfn_min = pfn;
                        if (pfn > ps->pfn_max) ps->pfn_max = pfn;
                        if (pfn != ps->last_pfn + 1) ps->pfn_runs++;
                    }
                    ps->last_pfn = pfn;
                }
            } else if ((entry & PM_SWAPPED) != 0) {
                ps->swapped_pages++;
                if (v->page_codes != NULL) {
                    v->page_codes[page_index] |= PAGE_CODE_SWAPPED;
                }
                if (v->page_states != NULL) {
                    v->page_states[page_index] = 'S';
                }
            } else {
                ps->not_present_pages++;
                if (v->page_states != NULL) {
                    v->page_states[page_index] = 'N';
                }
            }
            if ((entry & PM_SOFT_DIRTY) != 0) {
                ps->soft_dirty_pages++;
                if (v->page_codes != NULL) {
                    v->page_codes[page_index] |= PAGE_CODE_SOFT_DIRTY;
                }
            }
            if ((entry & PM_EXCLUSIVE) != 0) {
                ps->exclusive_pages++;
                if (v->page_codes != NULL) {
                    v->page_codes[page_index] |= PAGE_CODE_EXCLUSIVE;
                }
            }
            if ((entry & PM_FILE) != 0) {
                ps->file_or_shared_pages++;
                if (v->page_codes != NULL) {
                    v->page_codes[page_index] |= PAGE_CODE_FILE_SHARED;
                }
            }
        }
    }

    close(fd);
}

static void analyze_logical_pagemap(pid_t pid, LogicalRegionList *regions, long page_size)
{
    char path[64];
    int fd;

    snprintf(path, sizeof(path), "/proc/%ld/pagemap", (long)pid);
    fd = open(path, O_RDONLY);
    if (fd < 0) {
        return;
    }

    for (size_t i = 0; i < regions->count; i++) {
        LogicalRegion *r = &regions->items[i];
        PageStats *ps = &r->pages;
        ps->available = true;
        ps->pfn_min = UINT64_MAX;
        ps->pfn_max = 0;

        for (uint64_t addr = r->start; addr < r->end; addr += (uint64_t)page_size) {
            uint64_t entry = 0;
            off_t off = (off_t)((addr / (uint64_t)page_size) * sizeof(entry));
            ssize_t n = pread(fd, &entry, sizeof(entry), off);
            if (n != (ssize_t)sizeof(entry)) {
                ps->available = false;
                break;
            }

            ps->virtual_pages++;
            if ((entry & PM_PRESENT) != 0) {
                uint64_t pfn = entry & PM_PFN_MASK;
                ps->present_pages++;
                if (pfn != 0) {
                    if (!ps->has_pfn) {
                        ps->pfn_min = pfn;
                        ps->pfn_max = pfn;
                        ps->pfn_runs = 1;
                        ps->has_pfn = true;
                    } else {
                        if (pfn < ps->pfn_min) ps->pfn_min = pfn;
                        if (pfn > ps->pfn_max) ps->pfn_max = pfn;
                        if (pfn != ps->last_pfn + 1) ps->pfn_runs++;
                    }
                    ps->last_pfn = pfn;
                }
            } else if ((entry & PM_SWAPPED) != 0) {
                ps->swapped_pages++;
            } else {
                ps->not_present_pages++;
            }
            if ((entry & PM_SOFT_DIRTY) != 0) ps->soft_dirty_pages++;
            if ((entry & PM_EXCLUSIVE) != 0) ps->exclusive_pages++;
            if ((entry & PM_FILE) != 0) ps->file_or_shared_pages++;
        }
    }

    close(fd);
}

static long region_size_kb(const LogicalRegion *r)
{
    return (long)((r->end - r->start) / 1024);
}

static long prorate_kb(long total_kb, uint64_t part_bytes, uint64_t total_bytes)
{
    if (total_kb < 0) {
        return -1;
    }
    if (part_bytes == total_bytes || total_bytes == 0) {
        return total_kb;
    }
    return (long)(((long double)total_kb * (long double)part_bytes /
                   (long double)total_bytes) + 0.5L);
}

static void print_kb(FILE *out, long kb)
{
    if (kb < 0) {
        fprintf(out, "-");
    } else {
        fprintf(out, "%ld", kb);
    }
}

static void print_page_bitmap_range(FILE *out, const Vma *v,
                                    uint64_t start, uint64_t end,
                                    long page_size)
{
    if (v->page_states == NULL) {
        fprintf(out, "(无法读取 pagemap)");
        return;
    }

    size_t first = (size_t)((start - v->start) / (uint64_t)page_size);
    size_t count = (size_t)((end - start) / (uint64_t)page_size);
    for (size_t i = 0; i < count; i++) {
        char state = v->page_states[first + i];
        fputc(state != '\0' ? state : '?', out);
        if ((i + 1) % 128 == 0 && i + 1 < count) {
            fputc('\n', out);
        }
    }
}

static void print_report_header(FILE *out, pid_t pid, const char *comm,
                                const char *exe_path, const char *pagemap_status,
                                long page_size)
{
    fprintf(out, "# 进程内存映射分析报告\n\n");
    fprintf(out, "| 项目 | 值 |\n");
    fprintf(out, "| --- | --- |\n");
    fprintf(out, "| PID | `%ld` |\n", (long)pid);
    fprintf(out, "| 进程名 | `%s` |\n", comm);
    fprintf(out, "| 可执行文件 | `%s` |\n", exe_path[0] ? exe_path : "(无法读取 /proc/<pid>/exe)");
    fprintf(out, "| 页大小 | `%ld bytes` |\n", page_size);
    fprintf(out, "| pagemap 状态 | %s |\n", pagemap_status);
    fprintf(out, "\n> 采样说明：`maps`、`smaps`、`pagemap` 不是原子快照，进程运行中变化会造成少量误差。\n\n");
}

static void accumulate_summary(const LogicalRegionList *regions, SegmentSummary sums[SEG_COUNT])
{
    for (size_t i = 0; i < regions->count; i++) {
        const LogicalRegion *r = &regions->items[i];
        const Vma *v = r->vma;
        uint64_t part_bytes = r->end - r->start;
        uint64_t total_bytes = v->end - v->start;
        SegmentKind s = r->segment;
        if (s < 0 || s >= SEG_COUNT) {
            s = SEG_UNKNOWN;
        }
        sums[s].virtual_pages += r->pages.virtual_pages;
        sums[s].present_pages += r->pages.present_pages;
        sums[s].swapped_pages += r->pages.swapped_pages;
        sums[s].not_present_pages += r->pages.not_present_pages;
        sums[s].size_kb += region_size_kb(r);
        sums[s].rss_kb += v->rss_kb >= 0 ? prorate_kb(v->rss_kb, part_bytes, total_bytes) : 0;
        sums[s].pss_kb += v->pss_kb >= 0 ? prorate_kb(v->pss_kb, part_bytes, total_bytes) : 0;
        sums[s].swap_kb += v->swap_kb >= 0 ? prorate_kb(v->swap_kb, part_bytes, total_bytes) : 0;
    }
}

static void print_process_summary(FILE *out, const VmaList *list, long page_size)
{
    unsigned long long virtual_pages = 0;
    unsigned long long present_pages = 0;
    unsigned long long swapped_pages = 0;
    unsigned long long not_present_pages = 0;
    long size_kb = 0, rss_kb = 0, pss_kb = 0, swap_kb = 0;

    for (size_t i = 0; i < list->count; i++) {
        const Vma *v = &list->items[i];
        virtual_pages += v->pages.virtual_pages;
        present_pages += v->pages.present_pages;
        swapped_pages += v->pages.swapped_pages;
        not_present_pages += v->pages.not_present_pages;
        if (v->size_kb >= 0) size_kb += v->size_kb;
        if (v->rss_kb >= 0) rss_kb += v->rss_kb;
        if (v->pss_kb >= 0) pss_kb += v->pss_kb;
        if (v->swap_kb >= 0) swap_kb += v->swap_kb;
    }

    fprintf(out, "## 进程总览\n\n");
    fprintf(out, "| 指标 | 值 |\n");
    fprintf(out, "| --- | ---: |\n");
    fprintf(out, "| VMA 数量 | %zu |\n", list->count);
    fprintf(out, "| 虚拟地址空间 Size | %ld KiB |\n", size_kb);
    fprintf(out, "| smaps Rss | %ld KiB |\n", rss_kb);
    fprintf(out, "| smaps Pss | %ld KiB |\n", pss_kb);
    fprintf(out, "| smaps Swap | %ld KiB |\n", swap_kb);
    fprintf(out, "| pagemap 虚拟页 | %llu |\n", virtual_pages);
    fprintf(out, "| pagemap present 页 | %llu 页 / %llu KiB |\n",
            present_pages, present_pages * (unsigned long long)page_size / 1024ULL);
    fprintf(out, "| pagemap swap 页 | %llu |\n", swapped_pages);
    fprintf(out, "| pagemap 未驻留页 | %llu |\n\n", not_present_pages);
}

static void print_segment_summary(FILE *out, const LogicalRegionList *regions, long page_size)
{
    SegmentSummary sums[SEG_COUNT];
    memset(sums, 0, sizeof(sums));
    accumulate_summary(regions, sums);

    fprintf(out, "## 分段汇总\n\n");
    fprintf(out, "> 按报告内部的逻辑区间统计；同一 Linux VMA 可能被 ELF 边界拆成多行。`Rss/Pss/Swap` 来自 smaps 的整段 VMA 数据，拆分时按区间大小比例分摊。\n\n");
    fprintf(out, "| 分段 | Size(KiB) | Rss(KiB) | Present(KiB) | NotPresent(KiB) | Present%% |\n");
    fprintf(out, "| --- | ---: | ---: | ---: | ---: | ---: |\n");

    for (int s = 0; s < SEG_COUNT; s++) {
        if (sums[s].size_kb == 0 && sums[s].virtual_pages == 0) {
            continue;
        }
        double pct = sums[s].virtual_pages == 0 ? 0.0 :
                     100.0 * (double)sums[s].present_pages / (double)sums[s].virtual_pages;
        fprintf(out, "| %s | %ld | %ld | %llu | %llu | %.2f%% |\n",
                segment_name((SegmentKind)s),
                sums[s].size_kb,
                sums[s].rss_kb,
                sums[s].present_pages * (unsigned long long)page_size / 1024ULL,
                sums[s].not_present_pages * (unsigned long long)page_size / 1024ULL,
                pct);
    }
    fprintf(out, "\n");
}

static const char *display_path(const Vma *v)
{
    return v->path[0] ? v->path : "(anonymous)";
}

static void print_md_text_cell(FILE *out, const char *s)
{
    for (const char *p = s; *p != '\0'; p++) {
        if (*p == '|') {
            fputs("\\|", out);
        } else if (*p == '\n' || *p == '\r') {
            fputc(' ', out);
        } else {
            fputc(*p, out);
        }
    }
}

static void print_vma_details(FILE *out, const LogicalRegionList *regions, long page_size)
{
    fprintf(out, "## VMA 明细（逻辑切分）\n\n");
    fprintf(out, "| 逻辑地址范围 | 原始 VMA | 分段 | 权限 | Size(KiB) | Rss(KiB) | Pss(KiB) | Swap(KiB) | Present(KiB) | NotPresent(KiB) | 路径 |\n");
    fprintf(out, "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |\n");

    for (size_t i = 0; i < regions->count; i++) {
        const LogicalRegion *r = &regions->items[i];
        const Vma *v = r->vma;
        uint64_t part_bytes = r->end - r->start;
        uint64_t total_bytes = v->end - v->start;
        fprintf(out, "| `%012" PRIx64 "-%012" PRIx64 "` | `%012" PRIx64 "-%012" PRIx64 "` | %s | `%s` | %ld | %ld | %ld | %ld | %llu | %llu | `",
                r->start, r->end,
                v->start, v->end,
                segment_name(r->segment),
                v->perms,
                region_size_kb(r),
                prorate_kb(v->rss_kb, part_bytes, total_bytes),
                prorate_kb(v->pss_kb, part_bytes, total_bytes),
                prorate_kb(v->swap_kb, part_bytes, total_bytes),
                r->pages.present_pages * (unsigned long long)page_size / 1024ULL,
                r->pages.not_present_pages * (unsigned long long)page_size / 1024ULL);
        print_md_text_cell(out, display_path(v));
        fprintf(out, "` |\n");
    }
    fprintf(out, "\n");
}

static void print_vma_page_bitmaps(FILE *out, const VmaList *list, long page_size)
{
    fprintf(out, "## VMA 页状态序列\n\n");
    fprintf(out, "每个字符对应一个虚拟页，按地址从低到高排列：`P=present`，`N=not present`，`S=swapped`，`?=读取失败`。\n\n");

    for (size_t i = 0; i < list->count; i++) {
        const Vma *v = &list->items[i];

        fprintf(out, "### `%012" PRIx64 "-%012" PRIx64 "` %s\n\n",
                v->start, v->end, segment_name(v->segment));
        fprintf(out, "- 权限：`%s`\n", v->perms);
        fprintf(out, "- 路径：`");
        print_md_text_cell(out, display_path(v));
        fprintf(out, "`\n");
        fprintf(out, "- pagemap_bitmap：\n\n```text\n");
        print_page_bitmap_range(out, v, v->start, v->end, page_size);
        fprintf(out, "\n```\n\n");
    }
}

static void print_pfn_range(FILE *out, const Vma *v, uint64_t start, uint64_t end, long page_size)
{
    if (v->page_pfns == NULL) {
        fprintf(out, "unavailable\n");
        return;
    }

    size_t first = (size_t)((start - v->start) / (uint64_t)page_size);
    size_t count = (size_t)((end - start) / (uint64_t)page_size);
    for (size_t i = 0; i < count; i++) {
        uint64_t pfn = v->page_pfns[first + i];
        if (i > 0) {
            fputc(' ', out);
        }
        fprintf(out, "%" PRIx64, pfn);
        if ((i + 1) % 32 == 0 && i + 1 < count) {
            fputc('\n', out);
        }
    }
    fputc('\n', out);
}

static void print_page_code_range(FILE *out, const Vma *v, uint64_t start, uint64_t end, long page_size)
{
    if (v->page_codes == NULL) {
        fprintf(out, "unavailable\n");
        return;
    }

    size_t first = (size_t)((start - v->start) / (uint64_t)page_size);
    size_t count = (size_t)((end - start) / (uint64_t)page_size);
    for (size_t i = 0; i < count; i++) {
        if (i > 0) {
            fputc(' ', out);
        }
        fprintf(out, "%u", (unsigned int)v->page_codes[first + i]);
        if ((i + 1) % 64 == 0 && i + 1 < count) {
            fputc('\n', out);
        }
    }
    fputc('\n', out);
}

static void print_logical_pfn_sequences(FILE *out, const LogicalRegionList *regions, long page_size)
{
    fprintf(out, "## 逻辑区间 PFN 序列\n\n");
    fprintf(out, "用于自动对比操作前后的物理页变化。`pagemap_bitmap`、`page_code_sequence`、`pfn_sequence` 一一对应，每个位置代表一个虚拟页；PFN 为 `0` 表示该页未驻留、被换出、读取失败，或当前内核没有向本进程暴露 PFN。\n\n");
    fprintf(out, "page_code 是位掩码：`0=not-present/无标志`, `1=present`, `2=soft-dirty`, `4=swapped`, `8=exclusive`, `16=file/shared`, `32=PFN可见`。例如 `3` 表示 present 且 soft-dirty。\n\n");

    for (size_t i = 0; i < regions->count; i++) {
        const LogicalRegion *r = &regions->items[i];
        const Vma *v = r->vma;

        fprintf(out, "### `%012" PRIx64 "-%012" PRIx64 "` %s\n\n",
                r->start, r->end, segment_name(r->segment));
        fprintf(out, "- 原始 VMA：`%012" PRIx64 "-%012" PRIx64 "`\n", v->start, v->end);
        fprintf(out, "- 权限：`%s`\n", v->perms);
        fprintf(out, "- 路径：`");
        print_md_text_cell(out, display_path(v));
        fprintf(out, "`\n");
        fprintf(out, "- pagemap：`virtual=%llu页`, `present=%llu页`, `not_present=%llu页`, `swapped=%llu页`\n",
                r->pages.virtual_pages,
                r->pages.present_pages,
                r->pages.not_present_pages,
                r->pages.swapped_pages);
        fprintf(out, "- pagemap_bitmap：\n\n```text\n");
        print_page_bitmap_range(out, v, r->start, r->end, page_size);
        fprintf(out, "\n```\n");
        fprintf(out, "- page_code_sequence：\n\n```text\n");
        print_page_code_range(out, v, r->start, r->end, page_size);
        fprintf(out, "```\n");
        fprintf(out, "- pfn_sequence：\n\n```text\n");
        print_pfn_range(out, v, r->start, r->end, page_size);
        fprintf(out, "```\n\n");
    }
}

static void print_target_segments(FILE *out, const LogicalRegionList *regions, long page_size)
{
    fprintf(out, "## 重点分段字段\n\n");
    fprintf(out, "下面只列出图中关心的 `text`、`data`、`bss`、`heap`、`file`、`stack`。`Present(KiB)` 是真正驻留在物理内存中的页大小。\n\n");

    for (size_t i = 0; i < regions->count; i++) {
        const LogicalRegion *r = &regions->items[i];
        const Vma *v = r->vma;
        uint64_t part_bytes = r->end - r->start;
        uint64_t total_bytes = v->end - v->start;
        if (!(r->segment == SEG_TEXT || r->segment == SEG_INIT_DATA ||
              r->segment == SEG_BSS || r->segment == SEG_HEAP ||
              r->segment == SEG_FILE || r->segment == SEG_STACK)) {
            continue;
        }

        fprintf(out, "### %s\n\n", segment_name(r->segment));
        fprintf(out, "- 逻辑地址范围：`%012" PRIx64 "-%012" PRIx64 "`\n", r->start, r->end);
        fprintf(out, "- 原始 VMA：`%012" PRIx64 "-%012" PRIx64 "`\n", v->start, v->end);
        fprintf(out, "- 权限：`%s`\n", v->perms);
        fprintf(out, "- 路径：`");
        print_md_text_cell(out, display_path(v));
        fprintf(out, "`\n");
        fprintf(out, "- maps：`offset=0x%" PRIx64 "`, `dev=%s`, `inode=%llu`\n",
                v->offset, v->dev, v->inode);
        fprintf(out, "- smaps：`Size=");
        print_kb(out, region_size_kb(r));
        fprintf(out, " KiB`, `Rss=");
        print_kb(out, prorate_kb(v->rss_kb, part_bytes, total_bytes));
        fprintf(out, " KiB`, `Pss=");
        print_kb(out, prorate_kb(v->pss_kb, part_bytes, total_bytes));
        fprintf(out, " KiB`, `Referenced=");
        print_kb(out, prorate_kb(v->referenced_kb, part_bytes, total_bytes));
        fprintf(out, " KiB`, `Swap=");
        print_kb(out, prorate_kb(v->swap_kb, part_bytes, total_bytes));
        fprintf(out, " KiB`, `SwapPss=");
        print_kb(out, prorate_kb(v->swappss_kb, part_bytes, total_bytes));
        fprintf(out, " KiB`\n");
        fprintf(out, "- pagemap：`virtual=%llu页`, `present=%llu页(%llu KiB)`, `not_present=%llu页(%llu KiB)`, `swapped=%llu页`, `soft_dirty=%llu页`, `exclusive=%llu页`, `file_or_shared=%llu页`\n",
                r->pages.virtual_pages,
                r->pages.present_pages,
                r->pages.present_pages * (unsigned long long)page_size / 1024ULL,
                r->pages.not_present_pages,
                r->pages.not_present_pages * (unsigned long long)page_size / 1024ULL,
                r->pages.swapped_pages,
                r->pages.soft_dirty_pages,
                r->pages.exclusive_pages,
                r->pages.file_or_shared_pages);
        fprintf(out, "- pagemap_bitmap：\n\n```text\n");
        print_page_bitmap_range(out, v, r->start, r->end, page_size);
        fprintf(out, "\n```\n");
        if (r->pages.has_pfn) {
            fprintf(out, "- PFN：`min=%" PRIu64 "`, `max=%" PRIu64 "`, `连续区段数=%llu`\n",
                    r->pages.pfn_min, r->pages.pfn_max, r->pages.pfn_runs);
        } else if (r->pages.present_pages > 0) {
            fprintf(out, "- PFN：未显示，通常是因为没有 `root/CAP_SYS_ADMIN` 权限或内核隐藏 PFN。\n");
        }
        fprintf(out, "\n");
    }
}

static void print_field_explanations(FILE *out)
{
    fprintf(out, "## 字段含义\n\n");
    fprintf(out, "| 字段 | 含义 |\n");
    fprintf(out, "| --- | --- |\n");
    fprintf(out, "| `maps.address` | VMA 的虚拟地址范围，左闭右开。 |\n");
    fprintf(out, "| `逻辑地址范围` | 报告内部按 ELF 边界切出的子区间；不会改变 Linux 内核中的原始 VMA。 |\n");
    fprintf(out, "| `原始 VMA` | `/proc/<pid>/maps` 中真实存在的 VMA，同一个原始 VMA 可能对应多条逻辑区间。 |\n");
    fprintf(out, "| `maps.perms` | `r/w/x` 表示读/写/执行；`p` 表示私有 COW 映射；`s` 表示共享映射。 |\n");
    fprintf(out, "| `maps.offset` | 文件映射在文件中的偏移；匿名映射通常为 0。 |\n");
    fprintf(out, "| `maps.dev/inode/pathname` | 映射来源文件的设备号、inode 和路径；`inode=0` 且无路径通常是匿名映射。 |\n");
    fprintf(out, "| `smaps.Size` | 这段 VMA 的虚拟地址空间大小，不等于真实占用内存。 |\n");
    fprintf(out, "| `smaps.Rss` | Resident Set Size，当前实际驻留在物理内存中的大小。 |\n");
    fprintf(out, "| `smaps.Pss` | Proportional Set Size，共享页按共享进程数均摊后的大小。 |\n");
    fprintf(out, "| `smaps.Referenced` | 最近被访问过的驻留页大小。 |\n");
    fprintf(out, "| `smaps.Swap` | 已换出到 swap 的大小。 |\n");
    fprintf(out, "| `smaps.SwapPss` | 共享 swap 页均摊后的大小。 |\n");
    fprintf(out, "| `pagemap.present` | 为 1 表示该虚拟页当前有物理页驻留；`present页 * 页大小` 就是这段真实物理驻留大小。 |\n");
    fprintf(out, "| `pagemap.swapped` | 为 1 表示该虚拟页被换出。 |\n");
    fprintf(out, "| `pagemap.not_present` | `present=0` 且 `swapped=0`，表示虚拟地址保留了，但当前没有真实物理页。 |\n");
    fprintf(out, "| `pagemap_bitmap` | 每个字符对应一个虚拟页：`P=present`、`N=not present`、`S=swapped`、`?=读取失败`。 |\n");
    fprintf(out, "| `pagemap.PFN` | 物理页帧号；现代 Linux 通常要求 `root/CAP_SYS_ADMIN` 才能看到真实 PFN。 |\n\n");

    fprintf(out, "## 分段识别说明\n\n");
    fprintf(out, "| 分段 | 识别方式 |\n");
    fprintf(out, "| --- | --- |\n");
    fprintf(out, "| `text/代码段` | 主可执行文件中带 `x` 权限的映射。 |\n");
    fprintf(out, "| `data/已初始化数据段` | 主可执行文件中可写的文件私有映射，通常保存已初始化全局变量/静态变量。 |\n");
    fprintf(out, "| `bss/未初始化数据段` | 主程序 `data` 后紧邻的匿名私有可写映射，或 ELF 中 `filesz < memsz` 的零填充尾部；报告会按 ELF 边界在内部切分逻辑区间。 |\n");
    fprintf(out, "| `heap/堆` | `pathname` 为 `[heap]` 的映射，`malloc/brk` 常使用这里；大型 `malloc` 也可能单独出现在匿名映射里。 |\n");
    fprintf(out, "| `file/文件映射` | 共享库、普通文件 `mmap`、locale、动态链接器等文件来源映射。 |\n");
    fprintf(out, "| `stack/栈` | `pathname` 为 `[stack]` 或 `[stack:<tid>]` 的映射。 |\n");
}

static bool analyze_one_pid(pid_t pid, FILE *out)
{
    VmaList list = {0};
    LogicalRegionList regions = {0};
    char err[256] = {0};
    char comm[256];
    char exe_path[PATH_MAX];
    char pagemap_status[256];
    ExeLayout exe_layout;
    long page_size = sysconf(_SC_PAGESIZE);

    if (page_size <= 0) {
        page_size = 4096;
    }

    read_comm(pid, comm, sizeof(comm));
    read_exe_path(pid, exe_path, sizeof(exe_path));

    if (!parse_maps(pid, &list, err, sizeof(err))) {
        fprintf(out, "# PID %ld 分析失败\n\n%s\n\n", (long)pid, err);
        return false;
    }
    if (!parse_smaps_fields(pid, &list, err, sizeof(err))) {
        fprintf(out, "# PID %ld 分析失败\n\n%s\n\n", (long)pid, err);
        vma_list_free(&list);
        return false;
    }

    memset(&exe_layout, 0, sizeof(exe_layout));
    if (exe_path[0] != '\0') {
        load_exe_layout(exe_path, &list, page_size, &exe_layout);
    }
    classify_segments(&list, exe_path, &exe_layout, page_size);
    if (!build_logical_regions(&list, exe_path, &exe_layout, &regions)) {
        fprintf(out, "# PID %ld 分析失败\n\n内存不足，无法构建逻辑分段。\n\n", (long)pid);
        vma_list_free(&list);
        return false;
    }

    pagemap_status[0] = '\0';
    analyze_pagemap(pid, &list, page_size, pagemap_status, sizeof(pagemap_status));
    analyze_logical_pagemap(pid, &regions, page_size);

    print_report_header(out, pid, comm, exe_path, pagemap_status, page_size);
    print_process_summary(out, &list, page_size);
    print_segment_summary(out, &regions, page_size);
    print_target_segments(out, &regions, page_size);
    print_vma_details(out, &regions, page_size);
    print_vma_page_bitmaps(out, &list, page_size);
    print_logical_pfn_sequences(out, &regions, page_size);
    print_field_explanations(out);

    logical_region_list_free(&regions);
    vma_list_free(&list);
    return true;
}

static char *capture_pid_report(pid_t pid)
{
    char *buf = NULL;
    size_t len = 0;
    FILE *mem = open_memstream(&buf, &len);

    if (mem == NULL) {
        return NULL;
    }
    analyze_one_pid(pid, mem);
    fclose(mem);
    return buf;
}

static bool save_watch_snapshot(ProcSeries *series, pid_t pid,
                                int sample_index, bool is_first)
{
    char *report = capture_pid_report(pid);
    if (report == NULL) {
        return false;
    }

    if (is_first) {
        free(series->first_report);
        series->first_report = report;
        series->first_report_sample = sample_index;
    } else {
        free(series->last_report);
        series->last_report = report;
        series->last_report_sample = sample_index;
    }
    return true;
}

static void series_list_free(SeriesList *list)
{
    for (size_t i = 0; i < list->count; i++) {
        free(list->items[i].samples);
        free(list->items[i].first_report);
        free(list->items[i].last_report);
    }
    free(list->items);
    list->items = NULL;
    list->count = 0;
    list->cap = 0;
}

static ProcSeries *find_or_add_series(SeriesList *list, pid_t pid)
{
    for (size_t i = 0; i < list->count; i++) {
        if (list->items[i].pid == pid) {
            return &list->items[i];
        }
    }

    if (list->count == list->cap) {
        size_t new_cap = list->cap == 0 ? 32 : list->cap * 2;
        ProcSeries *items = realloc(list->items, new_cap * sizeof(*items));
        if (items == NULL) {
            return NULL;
        }
        list->items = items;
        list->cap = new_cap;
    }

    ProcSeries *series = &list->items[list->count++];
    memset(series, 0, sizeof(*series));
    series->pid = pid;
    series->first_report_sample = -1;
    series->last_report_sample = -1;
    read_comm(pid, series->comm, sizeof(series->comm));
    read_cmdline(pid, series->cmdline, sizeof(series->cmdline));
    return series;
}

static bool append_sample(ProcSeries *series, const WatchSample *sample)
{
    if (series->sample_count == series->sample_cap) {
        size_t new_cap = series->sample_cap == 0 ? 16 : series->sample_cap * 2;
        WatchSample *samples = realloc(series->samples, new_cap * sizeof(*samples));
        if (samples == NULL) {
            return false;
        }
        series->samples = samples;
        series->sample_cap = new_cap;
    }
    series->samples[series->sample_count++] = *sample;
    if (sample->comm[0] != '\0') {
        snprintf(series->comm, sizeof(series->comm), "%s", sample->comm);
    }
    if (sample->cmdline[0] != '\0') {
        snprintf(series->cmdline, sizeof(series->cmdline), "%s", sample->cmdline);
    }
    return true;
}

static bool collect_watch_sample(pid_t pid, WatchSample *sample, long page_size)
{
    VmaList list = {0};
    char err[256] = {0};

    memset(sample, 0, sizeof(*sample));
    sample->pid = pid;
    read_comm(pid, sample->comm, sizeof(sample->comm));
    read_cmdline(pid, sample->cmdline, sizeof(sample->cmdline));

    if (!parse_maps(pid, &list, err, sizeof(err))) {
        vma_list_free(&list);
        return false;
    }
    if (!parse_smaps_fields(pid, &list, err, sizeof(err))) {
        vma_list_free(&list);
        return false;
    }
    analyze_pagemap(pid, &list, page_size, err, sizeof(err));

    sample->valid = true;
    for (size_t i = 0; i < list.count; i++) {
        Vma *v = &list.items[i];
        if (v->size_kb >= 0) sample->size_kb += v->size_kb;
        if (v->rss_kb >= 0) sample->rss_kb += v->rss_kb;
        if (v->pss_kb >= 0) sample->pss_kb += v->pss_kb;
        if (v->swap_kb >= 0) sample->swap_kb += v->swap_kb;
        sample->virtual_pages += v->pages.virtual_pages;
        sample->present_pages += v->pages.present_pages;
        sample->swapped_pages += v->pages.swapped_pages;
        sample->not_present_pages += v->pages.not_present_pages;
    }
    sample->present_kb = sample->present_pages * (unsigned long long)page_size / 1024ULL;
    sample->not_present_kb = sample->not_present_pages * (unsigned long long)page_size / 1024ULL;

    vma_list_free(&list);
    return true;
}

static bool string_contains(const char *haystack, const char *needle)
{
    return haystack != NULL && needle != NULL && strstr(haystack, needle) != NULL;
}

static int discover_app_pids(const char *keyword, pid_t *pids, int max_pids)
{
    DIR *dir = opendir("/proc");
    struct dirent *ent;
    int count = 0;
    pid_t self_pid = getpid();
    pid_t parent_pid = getppid();

    if (dir == NULL) {
        return 0;
    }

    while ((ent = readdir(dir)) != NULL) {
        char *end = NULL;
        long pid_long = strtol(ent->d_name, &end, 10);
        if (end == ent->d_name || *end != '\0' || pid_long <= 0 || pid_long > INT_MAX) {
            continue;
        }

        pid_t pid = (pid_t)pid_long;
        char comm[256];
        char cmdline[512];
        if (pid == self_pid || pid == parent_pid) {
            continue;
        }
        read_comm(pid, comm, sizeof(comm));
        read_cmdline(pid, cmdline, sizeof(cmdline));
        if (string_contains(comm, keyword) || string_contains(cmdline, keyword)) {
            bool exists = false;
            for (int i = 0; i < count; i++) {
                if (pids[i] == pid) {
                    exists = true;
                    break;
                }
            }
            if (!exists && count < max_pids) {
                pids[count++] = pid;
            }
        }
    }

    closedir(dir);
    return count;
}

static long sample_value(const WatchSample *s, const char *field)
{
    if (strcmp(field, "RSS") == 0) return s->rss_kb;
    if (strcmp(field, "PSS") == 0) return s->pss_kb;
    if (strcmp(field, "Present") == 0) return (long)s->present_kb;
    if (strcmp(field, "NotPresent") == 0) return (long)s->not_present_kb;
    if (strcmp(field, "Swap") == 0) return s->swap_kb;
    if (strcmp(field, "Size") == 0) return s->size_kb;
    return 0;
}

static bool path_parent_dir(const char *path, char *buf, size_t len)
{
    const char *slash = strrchr(path, '/');
    size_t parent_len;

    if (slash == NULL) {
        return snprintf(buf, len, ".") < (int)len;
    }
    parent_len = (size_t)(slash - path);
    if (parent_len == 0) {
        parent_len = 1;
    }
    if (parent_len >= len) {
        errno = ENAMETOOLONG;
        return false;
    }
    memcpy(buf, path, parent_len);
    buf[parent_len] = '\0';
    return true;
}

static void sanitize_filename_component(const char *in, char *out, size_t len)
{
    size_t pos = 0;

    if (len == 0) {
        return;
    }
    for (const unsigned char *p = (const unsigned char *)in; *p != '\0' && pos + 1 < len; p++) {
        if (isalnum(*p) || *p == '-' || *p == '_') {
            out[pos++] = (char)*p;
        } else if (pos > 0 && out[pos - 1] != '_') {
            out[pos++] = '_';
        }
    }
    if (pos == 0) {
        snprintf(out, len, "unknown");
    } else {
        out[pos] = '\0';
    }
}

static void print_mermaid_line(FILE *out, const ProcSeries *series,
                               const char *title, const char **fields, size_t field_count)
{
    fprintf(out, "```mermaid\n");
    fprintf(out, "xychart-beta\n");
    fprintf(out, "    title \"%s\"\n", title);
    fprintf(out, "    x-axis \"sample\" [");
    for (size_t i = 0; i < series->sample_count; i++) {
        if (i > 0) fprintf(out, ", ");
        fprintf(out, "\"%zu\"", i);
    }
    fprintf(out, "]\n");
    fprintf(out, "    y-axis \"KiB\" 0 --> ");

    long max_value = 1;
    for (size_t i = 0; i < series->sample_count; i++) {
        if (!series->samples[i].valid) continue;
        for (size_t f = 0; f < field_count; f++) {
            long v = sample_value(&series->samples[i], fields[f]);
            if (v > max_value) max_value = v;
        }
    }
    fprintf(out, "%ld\n", max_value + max_value / 10 + 1);

    for (size_t f = 0; f < field_count; f++) {
        fprintf(out, "    line \"%s\" [", fields[f]);
        for (size_t i = 0; i < series->sample_count; i++) {
            if (i > 0) fprintf(out, ", ");
            fprintf(out, "%ld", series->samples[i].valid ? sample_value(&series->samples[i], fields[f]) : 0);
        }
        fprintf(out, "]\n");
    }
    fprintf(out, "```\n\n");
}

static void print_process_snapshots(FILE *out, const ProcSeries *series)
{
    fprintf(out, "## 首尾详细快照\n\n");
    fprintf(out, "下面的内容是在监控采样时直接抓取的完整内存映射分析，只保留第一次和最后一次采样。\n\n");

    if (series->first_report != NULL) {
        fprintf(out, "### 开始快照（sample %d）\n\n", series->first_report_sample);
        fputs(series->first_report, out);
        fprintf(out, "\n");
    } else {
        fprintf(out, "### 开始快照\n\n未能采集开始快照。\n\n");
    }

    if (series->last_report != NULL) {
        fprintf(out, "### 结束快照（sample %d）\n\n", series->last_report_sample);
        fputs(series->last_report, out);
        fprintf(out, "\n");
    } else {
        fprintf(out, "### 结束快照\n\n未能采集结束快照，可能是进程在最后一次采样前已经退出。\n\n");
    }
}

static void print_process_watch_report(FILE *out, const ProcSeries *series,
                                       bool include_snapshots)
{
    const char *mem_fields[] = {"RSS", "PSS", "Present"};
    const char *res_fields[] = {"Size", "NotPresent", "Swap"};
    char title[128];

    fprintf(out, "# PID %ld `%s` 监控详情\n\n",
            (long)series->pid, series->comm[0] ? series->comm : "unknown");
    fprintf(out, "- 命令行：`");
    print_md_text_cell(out, series->cmdline[0] ? series->cmdline : "(empty)");
    fprintf(out, "`\n");
    fprintf(out, "- 采样次数：`%zu`\n\n", series->sample_count);

    snprintf(title, sizeof(title), "PID %ld RSS/PSS/Present", (long)series->pid);
    print_mermaid_line(out, series, title, mem_fields, sizeof(mem_fields) / sizeof(mem_fields[0]));
    snprintf(title, sizeof(title), "PID %ld Size/NotPresent/Swap", (long)series->pid);
    print_mermaid_line(out, series, title, res_fields, sizeof(res_fields) / sizeof(res_fields[0]));

    fprintf(out, "## sample 表格\n\n");
    fprintf(out, "| sample | Size | RSS | PSS | Present | NotPresent | Swap | 虚拟页 | Present页 | Swap页 |\n");
    fprintf(out, "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n");
    for (size_t i = 0; i < series->sample_count; i++) {
        const WatchSample *s = &series->samples[i];
        if (!s->valid) {
            fprintf(out, "| %zu | - | - | - | - | - | - | - | - | - |\n", i);
            continue;
        }
        fprintf(out, "| %zu | %ld | %ld | %ld | %llu | %llu | %ld | %llu | %llu | %llu |\n",
                i, s->size_kb, s->rss_kb, s->pss_kb, s->present_kb,
                s->not_present_kb, s->swap_kb, s->virtual_pages,
                s->present_pages, s->swapped_pages);
    }
    fprintf(out, "\n");

    if (include_snapshots) {
        print_process_snapshots(out, series);
    } else {
        fprintf(out, "## 首尾详细快照\n\n");
        fprintf(out, "- [开始快照](first_snapshot.md)\n");
        fprintf(out, "- [结束快照](last_snapshot.md)\n\n");
    }
}

static void print_watch_report(FILE *out, const SeriesList *series_list,
                               const char *target, int duration_sec, int interval_sec,
                               long page_size, const char *process_dir_link)
{
    fprintf(out, "# App 内存变化监控报告\n\n");
    fprintf(out, "| 项目 | 值 |\n");
    fprintf(out, "| --- | --- |\n");
    fprintf(out, "| 监控目标 | `%s` |\n", target);
    fprintf(out, "| 监控时长 | `%d s` |\n", duration_sec);
    fprintf(out, "| 采样间隔 | `%d s` |\n", interval_sec);
    fprintf(out, "| 页大小 | `%ld bytes` |\n", page_size);
    fprintf(out, "| 进程数量 | `%zu` |\n\n", series_list->count);
    fprintf(out, "> 主文件只保留总览索引。每个 PID 的曲线、sample 表格、首尾详细快照会写到 `%s/` 子目录下。\n\n", process_dir_link);

    fprintf(out, "## 进程索引\n\n");
    fprintf(out, "| PID | 进程名 | 采样次数 | 开始 RSS | 结束 RSS | 开始 Present | 结束 Present | 详情 |\n");
    fprintf(out, "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |\n");

    for (size_t p = 0; p < series_list->count; p++) {
        const ProcSeries *series = &series_list->items[p];
        const WatchSample *first = series->sample_count > 0 ? &series->samples[0] : NULL;
        const WatchSample *last = series->sample_count > 0 ? &series->samples[series->sample_count - 1] : NULL;
        fprintf(out, "| %ld | `", (long)series->pid);
        print_md_text_cell(out, series->comm[0] ? series->comm : "unknown");
        fprintf(out, "` | %zu | %ld | %ld | %llu | %llu | [%s](%s) |\n",
                series->sample_count,
                first != NULL && first->valid ? first->rss_kb : 0,
                last != NULL && last->valid ? last->rss_kb : 0,
                first != NULL && first->valid ? first->present_kb : 0,
                last != NULL && last->valid ? last->present_kb : 0,
                "打开",
                series->detail_link[0] ? series->detail_link : process_dir_link);
    }
    fprintf(out, "\n");
}

static bool write_process_watch_reports(const char *out_path, const SeriesList *series_list)
{
    char parent[PATH_MAX];
    char process_dir[PATH_MAX];

    if (!path_parent_dir(out_path, parent, sizeof(parent))) {
        return false;
    }
    if (strcmp(parent, ".") == 0) {
        if (snprintf(process_dir, sizeof(process_dir), "processes") >= (int)sizeof(process_dir)) {
            errno = ENAMETOOLONG;
            return false;
        }
    } else {
        if (snprintf(process_dir, sizeof(process_dir), "%s/processes", parent) >= (int)sizeof(process_dir)) {
            errno = ENAMETOOLONG;
            return false;
        }
    }
    if (!mkdir_p(process_dir)) {
        return false;
    }

    for (size_t p = 0; p < series_list->count; p++) {
        ProcSeries *series = &series_list->items[p];
        char safe_comm[128];
        char path[PATH_MAX];
        char link[PATH_MAX];
        FILE *fp;
        char *full_report = NULL;
        size_t full_len = 0;
        FILE *mem;

        sanitize_filename_component(series->comm[0] ? series->comm : "unknown",
                                    safe_comm, sizeof(safe_comm));
        if (snprintf(path, sizeof(path), "%s/pid_%ld_%s.md",
                     process_dir, (long)series->pid, safe_comm) >= (int)sizeof(path)) {
            errno = ENAMETOOLONG;
            return false;
        }

        mem = open_memstream(&full_report, &full_len);
        if (mem == NULL) {
            return false;
        }
        print_process_watch_report(mem, series, true);
        fclose(mem);

        if (full_len > SPLIT_REPORT_THRESHOLD) {
            char split_dir[PATH_MAX];
            char index_path[PATH_MAX];
            char first_path[PATH_MAX];
            char last_path[PATH_MAX];

            free(full_report);
            full_report = NULL;

            if (snprintf(split_dir, sizeof(split_dir), "%s/pid_%ld_%s",
                         process_dir, (long)series->pid, safe_comm) >= (int)sizeof(split_dir) ||
                snprintf(index_path, sizeof(index_path), "%s/index.md", split_dir) >= (int)sizeof(index_path) ||
                snprintf(first_path, sizeof(first_path), "%s/first_snapshot.md", split_dir) >= (int)sizeof(first_path) ||
                snprintf(last_path, sizeof(last_path), "%s/last_snapshot.md", split_dir) >= (int)sizeof(last_path)) {
                errno = ENAMETOOLONG;
                return false;
            }
            if (!mkdir_p(split_dir)) {
                return false;
            }

            fp = fopen(index_path, "w");
            if (fp == NULL) {
                return false;
            }
            print_process_watch_report(fp, series, false);
            fclose(fp);

            fp = fopen(first_path, "w");
            if (fp == NULL) {
                return false;
            }
            fprintf(fp, "# PID %ld `%s` 开始快照\n\n", (long)series->pid, series->comm[0] ? series->comm : "unknown");
            if (series->first_report != NULL) {
                fputs(series->first_report, fp);
            } else {
                fprintf(fp, "未能采集开始快照。\n");
            }
            fclose(fp);

            fp = fopen(last_path, "w");
            if (fp == NULL) {
                return false;
            }
            fprintf(fp, "# PID %ld `%s` 结束快照\n\n", (long)series->pid, series->comm[0] ? series->comm : "unknown");
            if (series->last_report != NULL) {
                fputs(series->last_report, fp);
            } else {
                fprintf(fp, "未能采集结束快照，可能是进程在最后一次采样前已经退出。\n");
            }
            fclose(fp);

            snprintf(link, sizeof(link), "processes/pid_%ld_%s/index.md", (long)series->pid, safe_comm);
            snprintf(series->detail_link, sizeof(series->detail_link), "%s", link);
            continue;
        }

        fp = fopen(path, "w");
        if (fp == NULL) {
            free(full_report);
            return false;
        }
        fputs(full_report, fp);
        fclose(fp);
        free(full_report);
        snprintf(link, sizeof(link), "processes/pid_%ld_%s.md", (long)series->pid, safe_comm);
        snprintf(series->detail_link, sizeof(series->detail_link), "%s", link);
    }
    return true;
}

static int run_watch(const char *app_keyword, const pid_t *fixed_pids, int fixed_pid_count,
                     int duration_sec, int interval_sec, const char *out_path)
{
    SeriesList series_list = {0};
    long page_size = sysconf(_SC_PAGESIZE);
    int samples = duration_sec / interval_sec + 1;
    FILE *out;

    if (page_size <= 0) page_size = 4096;
    if (samples < 1) samples = 1;

    for (int sample_index = 0; sample_index < samples; sample_index++) {
        pid_t pids[256];
        int pid_count = 0;

        if (app_keyword != NULL) {
            pid_count = discover_app_pids(app_keyword, pids, (int)(sizeof(pids) / sizeof(pids[0])));
        } else {
            pid_count = fixed_pid_count;
            for (int i = 0; i < fixed_pid_count; i++) {
                pids[i] = fixed_pids[i];
            }
        }

        printf("sample %d/%d: %d process(es)\n", sample_index + 1, samples, pid_count);
        for (int i = 0; i < pid_count; i++) {
            ProcSeries *series = find_or_add_series(&series_list, pids[i]);
            WatchSample sample;
            if (series == NULL) {
                series_list_free(&series_list);
                return 1;
            }
            collect_watch_sample(pids[i], &sample, page_size);
            append_sample(series, &sample);
            if (series->first_report == NULL) {
                save_watch_snapshot(series, pids[i], sample_index, true);
            }
            if (sample_index + 1 == samples) {
                save_watch_snapshot(series, pids[i], sample_index, false);
            }
        }

        if (sample_index + 1 < samples) {
            sleep((unsigned int)interval_sec);
        }
    }

    if (!write_process_watch_reports(out_path, &series_list)) {
        fprintf(stderr, "cannot create split watch reports for %s: %s\n", out_path, strerror(errno));
        series_list_free(&series_list);
        return 1;
    }

    out = fopen(out_path, "w");
    if (out == NULL) {
        fprintf(stderr, "cannot create watch report %s: %s\n", out_path, strerror(errno));
        series_list_free(&series_list);
        return 1;
    }
    print_watch_report(out, &series_list,
                       app_keyword != NULL ? app_keyword : "fixed PIDs",
                       duration_sec, interval_sec, page_size, "processes");
    fclose(out);
    printf("watch report written: %s\n", out_path);
    series_list_free(&series_list);
    return 0;
}

int main(int argc, char **argv)
{
    pid_t pids[128];
    int pid_count = 0;
    const char *out_path = NULL;
    const char *watch_app = NULL;
    bool watch_mode = false;
    int watch_duration = 0;
    int watch_interval = 1;
    char auto_out[128];
    char run_out[PATH_MAX];
    FILE *out = NULL;

    if (argc < 2) {
        usage(argv[0]);
        return 1;
    }

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-o") == 0 || strcmp(argv[i], "--output") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "-o/--output 后面需要报告文件路径\n");
                return 1;
            }
            out_path = argv[++i];
            continue;
        }
        if (strcmp(argv[i], "--watch-app") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "--watch-app 后面需要 app 关键字\n");
                return 1;
            }
            watch_mode = true;
            watch_app = argv[++i];
            if (watch_duration <= 0) watch_duration = 30;
            continue;
        }
        if (strcmp(argv[i], "--watch") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "--watch 后面需要监控秒数\n");
                return 1;
            }
            watch_mode = true;
            watch_duration = atoi(argv[++i]);
            if (watch_duration <= 0) {
                fprintf(stderr, "--watch 秒数必须大于 0\n");
                return 1;
            }
            continue;
        }
        if (strcmp(argv[i], "--duration") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "--duration 后面需要秒数\n");
                return 1;
            }
            watch_duration = atoi(argv[++i]);
            if (watch_duration <= 0) {
                fprintf(stderr, "--duration 秒数必须大于 0\n");
                return 1;
            }
            continue;
        }
        if (strcmp(argv[i], "--interval") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "--interval 后面需要秒数\n");
                return 1;
            }
            watch_interval = atoi(argv[++i]);
            if (watch_interval <= 0) {
                fprintf(stderr, "--interval 秒数必须大于 0\n");
                return 1;
            }
            continue;
        }
        char *end = NULL;
        long pid_long = strtol(argv[i], &end, 10);
        if (end == argv[i] || *end != '\0' || pid_long <= 0 || pid_long > INT_MAX) {
            fprintf(stderr, "非法 PID: %s\n", argv[i]);
            usage(argv[0]);
            return 1;
        }
        if (pid_count >= (int)(sizeof(pids) / sizeof(pids[0]))) {
            fprintf(stderr, "PID 数量过多，最多支持 %zu 个\n", sizeof(pids) / sizeof(pids[0]));
            return 1;
        }
        pids[pid_count++] = (pid_t)pid_long;
    }

    if (watch_mode) {
        if (watch_duration <= 0) watch_duration = 30;
        if (watch_app == NULL && pid_count == 0) {
            fprintf(stderr, "--watch 监控指定 PID 时至少需要一个 PID\n");
            usage(argv[0]);
            return 1;
        }
        if (out_path == NULL) {
            if (watch_app != NULL) {
                snprintf(auto_out, sizeof(auto_out), "mem_watch_%s.md", watch_app);
            } else {
                snprintf(auto_out, sizeof(auto_out), "mem_watch_pids.md");
            }
            out_path = auto_out;
        }
        if (!build_run_output_path(out_path, run_out, sizeof(run_out))) {
            fprintf(stderr, "无法创建本次运行输出路径 %s: %s\n", out_path, strerror(errno));
            return 1;
        }
        return run_watch(watch_app, pids, pid_count, watch_duration, watch_interval, run_out);
    }

    if (pid_count == 0) {
        usage(argv[0]);
        return 1;
    }

    if (out_path == NULL) {
        if (pid_count == 1) {
            snprintf(auto_out, sizeof(auto_out), "mem_analyze_%ld.md", (long)pids[0]);
        } else {
            snprintf(auto_out, sizeof(auto_out), "mem_analyze_report.md");
        }
        out_path = auto_out;
    }

    if (!build_run_output_path(out_path, run_out, sizeof(run_out))) {
        fprintf(stderr, "无法创建本次运行输出路径 %s: %s\n", out_path, strerror(errno));
        return 1;
    }

    out = fopen(run_out, "w");
    if (out == NULL) {
        fprintf(stderr, "无法创建报告文件 %s: %s\n", run_out, strerror(errno));
        return 1;
    }

    int ok_count = 0;
    for (int i = 0; i < pid_count; i++) {
        if (i > 0) {
            fprintf(out, "\n\n============================================================\n\n");
        }
        if (analyze_one_pid(pids[i], out)) {
            ok_count++;
        }
    }

    fclose(out);
    printf("报告已写入: %s\n", run_out);
    printf("成功分析 %d/%d 个 PID\n", ok_count, pid_count);
    return ok_count == pid_count ? 0 : 2;
}
