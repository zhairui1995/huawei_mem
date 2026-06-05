# Referenced 操作后访问定位报告

| 项目 | 值 |
| --- | --- |
| PID | `44183` |
| 进程名 | `HevoNext.B2CApp` |
| 可执行文件 | `/opt/apps/cn.com.10jqka/files/HevoNext.B2CApp` |
| 页大小 | `4096 bytes` |
| VMA 数 | `1878` |
| Size | `4534856 KiB` |
| Rss | `438408 KiB` |
| Pss | `316140 KiB` |
| Referenced | `159472 KiB / 39868 页` |
| Swap | `0 KiB` |

> 使用方法：先运行 `--clear-refs`，再执行用户操作，然后立刻采样。本报告中的 `Referenced` 表示观察窗口内被访问过的驻留页规模。

## Referenced 段汇总

| 一级段 | VMA 数 | Size | Rss | Pss | Referenced | Swap | Referenced/Size | Referenced/Rss |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| text/代码段 | 1 | 128 KiB (32 页) | 128 KiB (32 页) | 42 KiB (11 页) | 4 KiB (1 页) | 0 KiB (0 页) | 3.12% | 3.12% |
| data/已初始化数据段 | 1 | 4 KiB (1 页) | 4 KiB (1 页) | 4 KiB (1 页) | 0 KiB (0 页) | 0 KiB (0 页) | 0.00% | 0.00% |
| heap/堆 | 1 | 64060 KiB (16015 页) | 63484 KiB (15871 页) | 63484 KiB (15871 页) | 16592 KiB (4148 页) | 0 KiB (0 页) | 25.90% | 26.14% |
| stack/栈 | 1 | 132 KiB (33 页) | 108 KiB (27 页) | 108 KiB (27 页) | 48 KiB (12 页) | 0 KiB (0 页) | 36.36% | 44.44% |
| file/文件映射 | 1011 | 592980 KiB (148245 页) | 230120 KiB (57530 页) | 107946 KiB (26987 页) | 27636 KiB (6909 页) | 0 KiB (0 页) | 4.66% | 12.01% |
| anon/匿名映射 | 859 | 3877516 KiB (969379 页) | 144556 KiB (36139 页) | 144556 KiB (36139 页) | 115184 KiB (28796 页) | 0 KiB (0 页) | 2.97% | 79.68% |
| special/内核特殊映射 | 4 | 36 KiB (9 页) | 8 KiB (2 页) | 0 KiB (0 页) | 8 KiB (2 页) | 0 KiB (0 页) | 22.22% | 100.00% |

