# mem_analyze-v3 使用说明

`mem_analyze-v3` 是 `mem_analyze-v2` 的 section-aware 版本。它仍然以运行时
VMA/segment 作为一级分类，同时对 ELF 文件映射读取 section header，通过
`sh_name` 增加二级 section 细分。

## 1. 为什么仍以 segment 为一级分类

Linux 装载 ELF 时依赖 Program Header 里的 `PT_LOAD` segment；运行时
`/proc/<pid>/maps` 暴露的是 VMA，而不是 section。section header 更像链接期
和文件内部视角，运行时不一定完整保留，也可能被 strip。

所以 v3 使用：

| 层级 | 来源 | 例子 |
| --- | --- | --- |
| 一级 segment | `/proc/<pid>/maps`、权限、路径、ELF `PT_LOAD` | `text`、`data`、`bss`、`file`、`anon` |
| 二级 section | ELF section header 的 `sh_name` | `libc.so.6:.text`、`libxul.so:.rodata` |

如果某个 ELF 没有可用 section header，v3 会回退到一级 segment。

## 2. 编译

```bash
gcc -Wall -Wextra -std=c11 -o mem_analyze-v3 mem_analyze-v3.c
```

建议使用 `sudo` 运行，否则现代 Linux 可能隐藏 `/proc/<pid>/pagemap` 中的 PFN。

## 3. 单次分析

```bash
sudo ./mem_analyze-v3 <pid> -o report.md
```

也可以像 v2 一样按 app 关键字查找进程并逐个分析：

```bash
sudo ./mem_analyze-v3 --app firefox -o firefox.md
sudo ./mem_analyze-v3 firefox -o firefox.md
```

匹配逻辑会检查 `/proc/<pid>/comm` 和 `/proc/<pid>/cmdline` 是否包含该关键字。

单次报告会拆分为主索引和详细文件，避免一个 Markdown 过大：

```text
mem_analyze_run_x/
├── report.md
└── details/
    └── pid_<pid>_<name>_details/
        ├── index.md
        ├── page_data.tsv
        ├── full_report.md  # 可选
        ├── fields.md       # 可选
        └── part_001.md ... # 可选
```

主索引 `report.md` 保留总览矩阵、二级 section 汇总，并链接到详细报告。
`part_*.md` 是给人阅读的分块文件；`page_data.tsv` 是机器可读的逐页数据，
`export_page_codes.py` 会优先读取它。打开 `--with-full-report` 后才会额外生成
`full_report.md`，用于人工追溯完整 Markdown 报告。

默认输出是 compact 模式：Markdown 只写总览/汇总表，始终生成
`page_data.tsv` 供后续导出和可视化使用。需要更多 Markdown 细节时可以打开：

```bash
sudo ./mem_analyze-v3 <pid> -o report.md --md-preset standard
sudo ./mem_analyze-v3 <pid> -o report.md --md-preset full
sudo ./mem_analyze-v3 <pid> -o report.md --with-vma-details --with-pfn-markdown
```

可选开关包括 `--with-target-segments`、`--with-vma-details`、
`--with-page-bitmaps`、`--with-pfn-markdown`、`--with-fields`、
`--with-full-report` 和 `--with-all-markdown`。

详细报告中会包含：

| 章节 | 内容 |
| --- | --- |
| `总览矩阵` | 按 `maps`、`smaps`、`pagemap` 行分组，列为总进程和一级 segment |
| `Section 细分汇总` | 一级 segment 下的二级 section 汇总 |
| `VMA 明细（逻辑切分）` | 每个逻辑区间的一级段和二级 section |
| `逻辑区间 PFN 序列` | 每个逻辑区间的 bitmap、page code、PFN |
| `page_data.tsv` | 独立机器可读逐页数据，避免后续脚本解析超大 Markdown |

## 4. 连续监控

```bash
sudo ./mem_analyze-v3 --watch 30 --interval 1 <pid> -o watch.md
sudo ./mem_analyze-v3 --watch-app firefox --duration 30 --interval 1 -o watch.md
```

监控输出结构沿用 v2。若单个 PID 报告很大，会拆成：

```text
processes/
└── pid_xxx_name/
    ├── index.md
    ├── first_snapshot.md
    └── last_snapshot.md
```

## 5. 导出纯数字页状态

```bash
python3 export_page_codes.py <pid_report.md-or-pid_dir> -o page_codes --with-pfn
python3 export_page_codes.py details/pid_<pid>_<name>_details -o page_codes --with-pfn
```

输出示例：

```text
page_codes/
├── snapshot/file__libxul.so_.text_codes.txt
├── snapshot/file__libxul.so_.text_pfns.txt
└── manifest.tsv
```

`manifest.tsv` 字段：

| 字段 | 含义 |
| --- | --- |
| `phase` | `before`、`after`、`before_pfn`、`after_pfn` |
| `segment` | 一级段 |
| `section` | 二级 section |
| `pages` | 页数 |
| `path` | txt 文件路径 |

## 6. page_code 位掩码

每个数字对应一个虚拟页位置：

| 位值 | 含义 |
| ---: | --- |
| `0` | not-present / 无标志 |
| `1` | present |
| `2` | soft-dirty |
| `4` | swapped |
| `8` | exclusive |
| `16` | file/shared |
| `32` | PFN 可见 |

例如 `3 = 1 + 2`，表示该页 present 且 soft-dirty。

## 7. 可视化

```bash
python3 draw_pfn_delta.py <pid_report.md-or-pid_dir> -o pfn_delta.png --top 20
```

可视化需要两个快照。单次分析目录只有 `page_data.tsv`/`full_report.md` 一个快照，
会被拒绝；请传入监控生成的 PID 目录，或显式使用 `--before first_snapshot.md --after last_snapshot.md`。

图中每行是一个“一级 segment + 二级 section”。默认展示变化页数最大的
20 个二级 section。
