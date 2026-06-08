#define _GNU_SOURCE

#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <limits.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#define MAX_FIELDS 96
#define FIELD_KEY_LEN 64
#define FIELD_VALUE_LEN 128

#define PM_PRESENT   (1ULL << 63)
#define PM_SWAPPED   (1ULL << 62)
#define PM_FILE      (1ULL << 61)
#define PM_SOFT_DIRTY (1ULL << 55)
#define PM_EXCLUSIVE (1ULL << 56)
#define PM_PFN_MASK  ((1ULL << 55) - 1)

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
            "也支持多个 PID: sudo %s <pid1> <pid2> ... [-o report.md]\n",
            argv0, argv0);
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

static bool parse_smaps(pid_t pid, VmaList *list, char *err, size_t err_len)
{
    char path[64];
    FILE *fp = NULL;
    char *line = NULL;
    size_t line_cap = 0;
    Vma current;
    bool have_current = false;
    bool ok = true;

    snprintf(path, sizeof(path), "/proc/%ld/smaps", (long)pid);
    fp = fopen(path, "r");
    if (fp == NULL) {
        snprintf(err, err_len, "无法读取 %s: %s", path, strerror(errno));
        return false;
    }

    while (getline(&line, &line_cap, fp) != -1) {
        if (is_header_line(line)) {
            if (have_current && !vma_list_push(list, &current)) {
                snprintf(err, err_len, "内存不足，无法保存 VMA 信息");
                ok = false;
                break;
            }
            if (!parse_maps_header(line, &current)) {
                snprintf(err, err_len, "无法解析 smaps 行: %s", line);
                ok = false;
                break;
            }
            have_current = true;
            continue;
        }

        if (have_current) {
            char *colon = strchr(line, ':');
            if (colon != NULL) {
                *colon = '\0';
                char *key = trim_left(line);
                char *value = trim_left(colon + 1);
                trim_right(key);
                trim_right(value);
                add_smap_field(&current, key, value);
                apply_smap_value(&current, key, value);
            }
        }
    }

    if (ok && have_current && !vma_list_push(list, &current)) {
        snprintf(err, err_len, "内存不足，无法保存 VMA 信息");
        ok = false;
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
    FILE *fp = fopen(exe_path, "rb");
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
        ps->available = true;
        ps->pfn_min = UINT64_MAX;
        ps->pfn_max = 0;

        for (uint64_t addr = v->start; addr < v->end; addr += (uint64_t)page_size) {
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

static long vma_size_kb(const Vma *v)
{
    if (v->size_kb >= 0) {
        return v->size_kb;
    }
    return (long)((v->end - v->start) / 1024);
}

static void print_kb(FILE *out, long kb)
{
    if (kb < 0) {
        fprintf(out, "-");
    } else {
        fprintf(out, "%ld", kb);
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

static void accumulate_summary(const VmaList *list, SegmentSummary sums[SEG_COUNT])
{
    for (size_t i = 0; i < list->count; i++) {
        const Vma *v = &list->items[i];
        SegmentKind s = v->segment;
        if (s < 0 || s >= SEG_COUNT) {
            s = SEG_UNKNOWN;
        }
        sums[s].virtual_pages += v->pages.virtual_pages;
        sums[s].present_pages += v->pages.present_pages;
        sums[s].swapped_pages += v->pages.swapped_pages;
        sums[s].not_present_pages += v->pages.not_present_pages;
        sums[s].size_kb += v->size_kb >= 0 ? v->size_kb : 0;
        sums[s].rss_kb += v->rss_kb >= 0 ? v->rss_kb : 0;
        sums[s].pss_kb += v->pss_kb >= 0 ? v->pss_kb : 0;
        sums[s].swap_kb += v->swap_kb >= 0 ? v->swap_kb : 0;
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

static void print_segment_summary(FILE *out, const VmaList *list, long page_size)
{
    SegmentSummary sums[SEG_COUNT];
    memset(sums, 0, sizeof(sums));
    accumulate_summary(list, sums);

    fprintf(out, "## 分段汇总\n\n");
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

static void print_vma_details(FILE *out, const VmaList *list, long page_size)
{
    fprintf(out, "## VMA 明细\n\n");
    fprintf(out, "| 地址范围 | 分段 | 权限 | Size(KiB) | Rss(KiB) | Pss(KiB) | Swap(KiB) | Present(KiB) | NotPresent(KiB) | 路径 |\n");
    fprintf(out, "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |\n");

    for (size_t i = 0; i < list->count; i++) {
        const Vma *v = &list->items[i];
        fprintf(out, "| `%012" PRIx64 "-%012" PRIx64 "` | %s | `%s` | %ld | %ld | %ld | %ld | %llu | %llu | `",
                v->start, v->end,
                segment_name(v->segment),
                v->perms,
                vma_size_kb(v),
                v->rss_kb,
                v->pss_kb,
                v->swap_kb,
                v->pages.present_pages * (unsigned long long)page_size / 1024ULL,
                v->pages.not_present_pages * (unsigned long long)page_size / 1024ULL);
        print_md_text_cell(out, display_path(v));
        fprintf(out, "` |\n");
    }
    fprintf(out, "\n");
}

static void print_target_segments(FILE *out, const VmaList *list, long page_size)
{
    fprintf(out, "## 重点分段字段\n\n");
    fprintf(out, "下面只列出图中关心的 `text`、`data`、`bss`、`heap`、`file`、`stack`。`Present(KiB)` 是真正驻留在物理内存中的页大小。\n\n");

    for (size_t i = 0; i < list->count; i++) {
        const Vma *v = &list->items[i];
        if (!(v->segment == SEG_TEXT || v->segment == SEG_INIT_DATA ||
              v->segment == SEG_BSS || v->segment == SEG_HEAP ||
              v->segment == SEG_FILE || v->segment == SEG_STACK)) {
            continue;
        }

        fprintf(out, "### %s\n\n", segment_name(v->segment));
        fprintf(out, "- 地址范围：`%012" PRIx64 "-%012" PRIx64 "`\n", v->start, v->end);
        fprintf(out, "- 权限：`%s`\n", v->perms);
        fprintf(out, "- 路径：`");
        print_md_text_cell(out, display_path(v));
        fprintf(out, "`\n");
        fprintf(out, "- maps：`offset=0x%" PRIx64 "`, `dev=%s`, `inode=%llu`\n",
                v->offset, v->dev, v->inode);
        fprintf(out, "- smaps：`Size=");
        print_kb(out, v->size_kb);
        fprintf(out, " KiB`, `Rss=");
        print_kb(out, v->rss_kb);
        fprintf(out, " KiB`, `Pss=");
        print_kb(out, v->pss_kb);
        fprintf(out, " KiB`, `Referenced=");
        print_kb(out, v->referenced_kb);
        fprintf(out, " KiB`, `Swap=");
        print_kb(out, v->swap_kb);
        fprintf(out, " KiB`, `SwapPss=");
        print_kb(out, v->swappss_kb);
        fprintf(out, " KiB`\n");
        fprintf(out, "- pagemap：`virtual=%llu页`, `present=%llu页(%llu KiB)`, `not_present=%llu页(%llu KiB)`, `swapped=%llu页`, `soft_dirty=%llu页`, `exclusive=%llu页`, `file_or_shared=%llu页`\n",
                v->pages.virtual_pages,
                v->pages.present_pages,
                v->pages.present_pages * (unsigned long long)page_size / 1024ULL,
                v->pages.not_present_pages,
                v->pages.not_present_pages * (unsigned long long)page_size / 1024ULL,
                v->pages.swapped_pages,
                v->pages.soft_dirty_pages,
                v->pages.exclusive_pages,
                v->pages.file_or_shared_pages);
        if (v->pages.has_pfn) {
            fprintf(out, "- PFN：`min=%" PRIu64 "`, `max=%" PRIu64 "`, `连续区段数=%llu`\n",
                    v->pages.pfn_min, v->pages.pfn_max, v->pages.pfn_runs);
        } else if (v->pages.present_pages > 0) {
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
    fprintf(out, "| `pagemap.PFN` | 物理页帧号；现代 Linux 通常要求 `root/CAP_SYS_ADMIN` 才能看到真实 PFN。 |\n\n");

    fprintf(out, "## 分段识别说明\n\n");
    fprintf(out, "| 分段 | 识别方式 |\n");
    fprintf(out, "| --- | --- |\n");
    fprintf(out, "| `text/代码段` | 主可执行文件中带 `x` 权限的映射。 |\n");
    fprintf(out, "| `data/已初始化数据段` | 主可执行文件中可写的文件私有映射，通常保存已初始化全局变量/静态变量。 |\n");
    fprintf(out, "| `bss/未初始化数据段` | 主程序 `data` 后紧邻的匿名私有可写映射，或 ELF 中 `filesz < memsz` 的零填充尾部；如果 `bss` 与 `data` 共享同一页，`maps` 不一定能单独拆出。 |\n");
    fprintf(out, "| `heap/堆` | `pathname` 为 `[heap]` 的映射，`malloc/brk` 常使用这里；大型 `malloc` 也可能单独出现在匿名映射里。 |\n");
    fprintf(out, "| `file/文件映射` | 共享库、普通文件 `mmap`、locale、动态链接器等文件来源映射。 |\n");
    fprintf(out, "| `stack/栈` | `pathname` 为 `[stack]` 或 `[stack:<tid>]` 的映射。 |\n");
}

static bool analyze_one_pid(pid_t pid, FILE *out)
{
    VmaList list = {0};
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

    if (!parse_smaps(pid, &list, err, sizeof(err))) {
        fprintf(out, "# PID %ld 分析失败\n\n%s\n\n", (long)pid, err);
        return false;
    }

    memset(&exe_layout, 0, sizeof(exe_layout));
    if (exe_path[0] != '\0') {
        load_exe_layout(exe_path, &list, page_size, &exe_layout);
    }
    classify_segments(&list, exe_path, &exe_layout, page_size);

    pagemap_status[0] = '\0';
    analyze_pagemap(pid, &list, page_size, pagemap_status, sizeof(pagemap_status));

    print_report_header(out, pid, comm, exe_path, pagemap_status, page_size);
    print_process_summary(out, &list, page_size);
    print_segment_summary(out, &list, page_size);
    print_target_segments(out, &list, page_size);
    print_vma_details(out, &list, page_size);
    print_field_explanations(out);

    vma_list_free(&list);
    return true;
}

int main(int argc, char **argv)
{
    pid_t pids[128];
    int pid_count = 0;
    const char *out_path = NULL;
    char auto_out[128];
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

    out = fopen(out_path, "w");
    if (out == NULL) {
        fprintf(stderr, "无法创建报告文件 %s: %s\n", out_path, strerror(errno));
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
    printf("报告已写入: %s\n", out_path);
    printf("成功分析 %d/%d 个 PID\n", ok_count, pid_count);
    return ok_count == pid_count ? 0 : 2;
}
