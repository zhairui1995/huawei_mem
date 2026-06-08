# huawei_mem — 鸿蒙 PC 应用内存页快照采集工具

## 项目概述

通过 **hdc** 连接鸿蒙 PC 设备，对目标进程做内存页快照采集（单次瞬时），输出 CSV 供分析。

- 主机端：macOS (MacBook Air) 或 Windows，通过 hdc USB/网络连接设备
- 设备端：HUAWEI MateBook Pro HAD-W32，HongMeng Kernel 1.12.0，aarch64
- 采集程序：单文件 C11（memcap.c），交叉编译为 aarch64 ELF

## 环境初始化（重要）

所有 hdc 相关命令前，先 source 环境脚本：

```bash
source scripts/device/setup_env.sh
```

此后 `hdc` 直接可用，无需每次指定完整路径。

## 快速采集

```bash
source scripts/device/setup_env.sh

# 按进程名搜索并采集
bash scripts/device/collect.sh douyu
bash scripts/device/collect.sh 斗鱼 --all          # 采集所有子进程

# 指定 PID
bash scripts/device/collect.sh 9376 斗鱼
bash scripts/device/collect.sh 9376 斗鱼 -f background -o op_switch_room

# 跳过推送（设备上已有 memcap 二进制）
bash scripts/device/collect.sh 9376 斗鱼 --no-push
```

## 对比分析

```bash
# 对比所有斗鱼快照（自动选择 exact/fuzzy 模式）
python3 scripts/analysis/analyze_memory.py -i memcap_out/ --pid 9376

# fuzzy 模式（跨重启，PID 不同）
python3 scripts/analysis/analyze_memory.py -i memcap_out/ --mode fuzzy --threshold 0.8

# 只对比指定快照
python3 scripts/analysis/analyze_memory.py -i memcap_out/ \
    --sample sample_001 sample_002 sample_003

# 输出完整列表
python3 scripts/analysis/analyze_memory.py -i memcap_out/ --full
```

**匹配模式**：
- `exact`：按 (vma_start, vma_end) 匹配 → PID 不变时用
- `fuzzy`：按 (pathname, region_type, perms) 匹配 → PID 变化时用
- `auto`：自动检测（默认）

## 常用 hdc 命令速查

```bash
source scripts/device/setup_env.sh

hdc list targets                    # 查看连接设备
hdc shell "ps -A -o PID,ARGS"      # 列出所有进程
hdc shell "pidof com.douyu.ho.app" # 查找应用 PID
hdc shell "cat /proc/9376/cmdline | tr '\0' ' '"  # 查看进程命令行
```

## 项目文件结构

```
huawei_mem/
├── memcap.c                       # 设备端 C 采集程序（342行）
├── .gitignore
├── scripts/
│   ├── device/
│   │   ├── setup_env.sh           # 环境初始化（hdc/clang PATH）
│   │   └── collect.sh             # 一键采集脚本（编译+推送+采集+拉回）
│   ├── analysis/
│   │   └── analyze_memory.py      # 跨快照持久性对比分析
│   └── pipeline/
│       └── run_first_stage.sh     # 第一阶段流水线入口脚本
├── docs/
│   ├── douyu_experiment_report.html  # 斗鱼三次采集实验报告
│   ├── progress_dashboard.html       # 项目进展看板
│   ├── progress_report.md            # 项目进展文档
│   └── report_001_douyu.md           # 斗鱼首次采集报告
└── memcap_out/                    # CSV 采集结果（gitignore）
```

## 6 张 CSV 表

| 表 | 维护 | 粒度 |
|----|------|------|
| snapshot_index.csv | C 程序追加 | 每次快照一行 |
| vma_memory_snapshot.csv | C 程序追加 | 每个 VMA 一行（maps+smaps） |
| pagemap_snapshot.csv | C 程序追加 | 每个 VMA 一行（pagemap 聚合） |
| app_list.csv | 人工 | 每个应用一行 |
| operation_list.csv | 人工 | 每次操作一行 |
| future_need_label.csv | 待定 | 按 VMA 标注 |

## 关键实现要点

1. page_size 用 `sysconf(_SC_PAGESIZE)`，不写死 4096
2. pagemap 按 VMA 聚合，不逐页输出 CSV
3. pagemap bit: 63=present, 62=swapped, 61=file/shared, 56=exclusive, 55=soft-dirty
4. pagemap 权限失败不崩溃，写 `scan_status=open_pagemap_failed`
5. smaps 读取不到的字段填 0，不填 -1
6. VMA/pagemap 先写 `.tmp.PID` 临时文件再追加，防并发交叉损坏
7. 不要同时跑两个 memcap 到同一 out_dir

## 工作约定

- 提交信息写清改动原因
- C 代码 C11 标准，不引入外部依赖；Python 纯 stdlib
- 涉及 /proc 行为以 Linux 内核文档和 HarmonyOS 实际表现为准
- hdc 命令先 `source scripts/device/setup_env.sh`
