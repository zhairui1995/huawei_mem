# mem_analyze-v2 使用说明
[[华为项目]]

`mem_analyze-v2.c` 是一个 Linux 进程内存分析工具。它读取 `/proc/<pid>/maps`、`smaps`、`pagemap`、`exe` 等信息，生成 Markdown 报告，用来观察进程的 VMA、RSS/PSS、present/not present 页、text/data/bss/heap/stack 等逻辑分段。

## 1. 编译

在当前目录执行：

```bash
gcc -Wall -Wextra -std=c11 -o mem_analyze-v2 mem_analyze-v2.c
```

建议使用 `sudo` 运行。否则现代 Linux 可能会隐藏 `/proc/<pid>/pagemap` 中的 PFN，部分页级信息会受限。

## 2. 单次分析

分析一个 PID：

```bash
sudo ./mem_analyze-v2 <pid>
```

指定输出文件名：

```bash
sudo ./mem_analyze-v2 <pid> -o report.md
```

一次分析多个 PID：

```bash
sudo ./mem_analyze-v2 <pid1> <pid2> <pid3> -o report.md
```

## 3. 连续监控

按 app 关键字监控，例如 Firefox：

```bash
sudo ./mem_analyze-v2 --watch-app firefox --duration 60 --interval 2 -o firefox_watch.md
```

按固定 PID 监控：

```bash
sudo ./mem_analyze-v2 --watch 60 --interval 2 <pid1> <pid2> -o watch.md
```

参数含义：

| 参数 | 含义 |
| --- | --- |
| `--watch-app firefox` | 扫描 `/proc`，监控进程名或命令行包含 `firefox` 的进程 |
| `--watch 60` | 监控固定 PID，持续 60 秒 |
| `--duration 60` | app 监控模式下指定监控时长 |
| `--interval 2` | 每 2 秒采样一次 |
| `-o report.md` / `--output report.md` | 指定输出 Markdown 文件名 |

## 4. 输出目录

每次运行都会自动创建一个子目录，避免覆盖旧报告。

例如：

```bash
sudo ./mem_analyze-v2 1234 -o report.md
```

实际输出类似：

```text
mem_analyze_run_20260514_161110/report.md
```

如果指定：

```bash
sudo ./mem_analyze-v2 1234 -o logs/report.md
```

实际输出类似：

```text
logs/mem_analyze_run_20260514_161110/report.md
```

## 5. 单次报告内容

单次分析报告主要包含：

| 章节 | 内容 |
| --- | --- |
| `进程总览` | PID、进程名、可执行文件、页大小、pagemap 状态 |
| `分段汇总` | 按 text/data/bss/heap/stack/file/anon 等逻辑分段统计 Size、RSS、Present 等 |
| `重点分段字段` | 展示 text、data、bss、heap、file、stack 的详细字段 |
| `VMA 明细（逻辑切分）` | 按报告内部逻辑区间展示地址范围、原始 VMA、分段和内存指标 |
| `VMA 页状态序列` | 每个原始 VMA 的 pagemap 页状态 bitmap |
| `字段含义` | 解释 maps/smaps/pagemap 字段 |

## 6. 逻辑切分 VMA

工具不会改变 Linux 内核中的 VMA，只在报告内部把 VMA 按 ELF 边界拆成更细的逻辑区间。

例如原始 VMA 是：

```text
0x400000-0x405000 rw-p /a.out
```

如果 ELF 判断：

```text
data: 0x400000-0x403000
bss : 0x403000-0x405000
```

报告中会拆成：

| 逻辑区域 | 地址范围 |
| --- | --- |
| data | `0x400000-0x403000` |
| bss | `0x403000-0x405000` |

注意：`smaps` 的 RSS/PSS/Swap 是内核按原始 VMA 给出的，逻辑区间拆分时会按区间大小比例分摊；`pagemap` 页级统计会按逻辑区间重新读取统计。

## 7. pagemap_bitmap

报告会输出每个区间或 VMA 的页状态序列，例如：

```text
PPPPPPPPPPPPPPPPPPPPPPNNNNNNNNNNN
```

每个字符对应一个虚拟页，按地址从低到高排列：

| 字符 | 含义 |
| --- | --- |
| `P` | present，当前有物理页驻留 |
| `N` | not present，虚拟地址存在，但当前没有物理页 |
| `S` | swapped，页面已换出 |
| `?` | pagemap 读取失败 |

例如 heap 中可能看到：

````md
- pagemap_bitmap：

```text
PPPPPPPPPPPPPPPPPPPPPPNNNNNNNNNNN
```
````

这表示 heap 前半部分已经真正驻留在物理内存中，后半部分只是虚拟地址空间保留，还没有实际物理页。

新版报告还会在 `逻辑区间 PFN 序列` 中输出两种机器可读序列：

| 字段 | 含义 |
| --- | --- |
| `page_code_sequence` | 每个数字对应一个虚拟页位置，适合导出为纯 txt 后做对比。 |
| `pfn_sequence` | 每个数字对应一个虚拟页当前映射到的 PFN；`0` 表示未驻留、换出、读取失败，或内核没有暴露 PFN。 |

`page_code_sequence` 使用位掩码：

| 位值 | 含义 |
| ---: | --- |
| `0` | not-present / 无标志 |
| `1` | present |
| `2` | soft-dirty |
| `4` | swapped |
| `8` | exclusive |
| `16` | file/shared |
| `32` | PFN 可见 |

例如 `3 = 1 + 2`，表示该页 present 且 soft-dirty；`11 = 1 + 2 + 8`，表示 present、soft-dirty、exclusive。

## 8. 连续监控报告内容

监控模式会把内容拆成多个文件，避免 Firefox 这类多进程应用生成一个巨大的 Markdown。

输出结构类似：

```text
mem_analyze_run_20260514_170751/
├── firefox_watch.md
└── processes/
    ├── pid_2644_firefox.md
    ├── pid_2806_crashhelper.md
    └── pid_10943_Isolated_Web_Co.md
```

如果某个 PID 的详情文件超过 1 MB，工具会继续拆分到 PID 专属子文件夹中：

```text
mem_analyze_run_20260514_170751/
├── firefox_watch.md
└── processes/
    └── pid_3985_firefox/
        ├── index.md
        ├── first_snapshot.md
        └── last_snapshot.md
```

其中 `index.md` 保存曲线和 sample 表，`first_snapshot.md` 和 `last_snapshot.md` 保存体积较大的首尾完整 VMA/pagemap 报告。

主文件 `firefox_watch.md` 只包含总览和进程索引：

| 内容 | 说明 |
| --- | --- |
| 监控目标 | app 关键字或固定 PID |
| 监控时长 | 总监控秒数 |
| 采样间隔 | 每次采样间隔 |
| 进程索引 | 每个 PID 的开始/结束 RSS、Present，以及详情链接 |

每个 `processes/pid_*.md` 子报告包含：

| 内容 | 说明 |
| --- | --- |
| Mermaid 折线图 | `RSS/PSS/Present` 和 `Size/NotPresent/Swap` 两组趋势 |
| sample 表格 | 每次采样的 Size、RSS、PSS、Present、NotPresent、Swap 等 |
| 首尾详细快照 | 每个进程只保留第一次采样和最后一次采样的完整分析报告 |

`首尾详细快照` 的内容和单次分析报告类似，适合对比开始和结束时的 VMA、分段、页状态序列变化。

## 9. 常用命令示例

分析当前 shell：

```bash
sudo ./mem_analyze-v2 $$ -o report.md
```

分析 Firefox 主进程：

```bash
pgrep -a firefox
sudo ./mem_analyze-v2 <firefox_pid> -o firefox_report.md
```

监控 Firefox 60 秒：

```bash
sudo ./mem_analyze-v2 --watch-app firefox --duration 60 --interval 2 -o firefox_watch.md
```

监控指定 PID：

```bash
sudo ./mem_analyze-v2 --watch 30 --interval 1 10943 -o pid_10943_watch.md
```

导出首尾快照的逐页数字状态到纯 txt。参数既可以是单个 `pid_*.md`，也可以是拆分后的 PID 目录；如果传目录，脚本会自动读取里面的 `first_snapshot.md` 和 `last_snapshot.md`：

```bash
python3 export_page_codes.py mem_analyze_run_x/processes/pid_10943_xxx.md -o page_codes --with-pfn
python3 export_page_codes.py mem_analyze_run_x/processes/pid_10943_xxx -o page_codes --with-pfn
```

输出类似：

```text
page_codes/
├── before/
│   ├── heap_codes.txt
│   └── heap_pfns.txt
├── after/
│   ├── heap_codes.txt
│   └── heap_pfns.txt
└── manifest.tsv
```

可视化首尾物理页变化：

```bash
python3 draw_pfn_delta.py mem_analyze_run_x/processes/pid_10943_xxx.md -o pfn_delta.png
python3 draw_pfn_delta.py mem_analyze_run_x/processes/pid_10943_xxx -o pfn_delta.png
```

## 10. 注意事项

- 报告读取的是采样瞬间的 `/proc` 信息，进程运行中变化可能造成少量不一致。
- `maps`、`smaps`、`pagemap` 不是原子快照。
- 如果进程在分析过程中退出，报告可能出现读取失败。
- 非 root 环境下通常仍可统计 present/not present，但 PFN 可能被内核隐藏。
- 监控 `--watch-app` 会匹配进程名和命令行，可能把辅助进程也纳入报告。
