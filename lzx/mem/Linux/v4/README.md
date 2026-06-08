# mem_analyze v3

`mem_analyze-v3` 是 `mem_analyze-v2` 的 section-aware 版本。它仍然以运行时
VMA/segment 作为一级分类，同时对 ELF 文件映射读取 section header，并用
`sh_name` 增加二级 section 标签，例如 `libc.so.6:.text` 或
`libxul.so:.rodata`。

一级 segment 包括：

- `text`
- `data`
- `bss`
- `heap`
- `stack`
- `file`
- `anon`
- `special`

统计以页为最小单位，不再往页内继续细分。对于文件页中落在 `.bss/.tbss`
section 名下、但一级段不是匿名 bss 的区域，报告按 `.data` 口径显示。

## 编译

```bash
gcc -Wall -Wextra -std=c11 -o mem_analyze-v3 mem_analyze-v3.c
```

建议用 `sudo` 运行，否则现代 Linux 可能隐藏 `/proc/<pid>/pagemap` 里的真实 PFN。

## 单进程分析

```bash
sudo ./mem_analyze-v3 <pid> -o report.md
```

默认是 compact 模式：Markdown 只保留总览矩阵和 section 汇总表，并始终写出
`page_data.tsv`。这个 TSV 是机器可读的逐页数据，后续导出页状态和绘制 delta 图
都会优先使用它。

## Markdown 输出开关

需要更多人工阅读用的 Markdown 细节时，可以选择预设：

```bash
sudo ./mem_analyze-v3 <pid> -o report.md --md-preset standard
sudo ./mem_analyze-v3 <pid> -o report.md --md-preset full
```

也可以单独打开某些章节：

```bash
sudo ./mem_analyze-v3 <pid> -o report.md --with-vma-details --with-pfn-markdown
```

可用开关：

- `--md-preset compact`：默认模式，只写轻量表格和 `page_data.tsv`
- `--md-preset standard`：额外写重点分段、VMA 明细和字段说明
- `--md-preset full`：写出所有 Markdown 细节
- `--with-target-segments`：写出重点分段字段
- `--with-vma-details`：写出 VMA 明细表
- `--with-page-bitmaps`：写出原始 VMA 页状态序列
- `--with-pfn-markdown`：写出逻辑区间 PFN 序列
- `--with-fields`：写出字段说明
- `--with-full-report`：写出完整 `full_report.md`
- `--with-all-markdown`：等同于 `--md-preset full`

## 按应用名分析

```bash
sudo ./mem_analyze-v3 --app firefox -o firefox.md
sudo ./mem_analyze-v3 firefox -o firefox.md
```

匹配逻辑会检查 `/proc/<pid>/comm` 和 `/proc/<pid>/cmdline` 是否包含该关键字。

## 单次输出结构

```text
mem_analyze_run_x/
├── report.md
└── details/
    └── pid_<pid>_<name>_details/
        ├── index.md
        ├── page_data.tsv
        ├── fields.md          # 可选
        ├── full_report.md     # 可选
        └── part_001.md ...    # 可选
```

主 `report.md` 使用总览矩阵：行按 `maps`、`smaps`、`pagemap` 分组，列是总进程
和一级 segment。`details/.../index.md` 保存该 PID 的轻量详情。

`part_*.md` 是给人阅读的分块 Markdown，只在开启相关输出开关时生成。
`page_data.tsv` 是推荐的机器可读逐页数据文件。

## 连续监控

监控指定 PID：

```bash
sudo ./mem_analyze-v3 --watch 30 --interval 1 <pid> -o watch.md
```

监控匹配应用名的所有进程：

```bash
sudo ./mem_analyze-v3 --watch-app firefox --duration 30 --interval 1 -o watch.md
```

## 导出页状态数字文件

```bash
python3 export_page_codes.py <pid_report.md-or-pid_dir> -o page_codes --with-pfn
```

对于单次分析产生的拆分输出，建议直接传入 PID 详情目录。脚本会读取其中的
`page_data.tsv`，并写出 `snapshot/` 结果：

```bash
python3 export_page_codes.py mem_analyze_run_x/details/pid_<pid>_<name>_details -o page_codes --with-pfn
```

## 绘制物理页变化图

```bash
python3 draw_pfn_delta.py <pid_report.md-or-pid_dir> -o pfn_delta.png --top 20
```

delta 图需要两个快照。单次分析目录只有一个快照，会被 delta 工具拒绝。请使用
watch 输出中的 PID 目录，或显式传入两个快照：

```bash
python3 draw_pfn_delta.py --before first_snapshot.md --after last_snapshot.md -o pfn_delta.png
```

默认会生成两张图：

- `pfn_delta.png`：变化最大的二级 section
- `pfn_delta_segments.png`：一级 segment 聚合
