# huawei_mem — 鸿蒙 PC 应用内存页快照采集工具

## 项目概述

本项目的目标是在 **Windows 主机端**，通过 **hdc (HarmonyOS Device Connector)** 连接鸿蒙 PC 设备，对指定进程 PID 进行一次性的内存页快照采集，输出 CSV 数据供后续分析。

**当前阶段：** 单文件 C 程序，每次运行做一次瞬时快照。不做高频监控，不做 ArkTS 应用。

## 技术路线

```
人工操作应用 → 主机端记录 sample_id/operation_id → hdc shell 获取 PID
→ 运行设备侧 C 程序 memcap → 读取 maps/smaps/pagemap
→ 输出 CSV → hdc file recv 拉回 → 后处理分析
```

## 核心概念

- **memcap**: 设备端 C 程序，编译后通过 `hdc file send` 推送到 `/data/local/tmp/memcap/`
- **3 张自动采集表**: `snapshot_index.csv`, `vma_memory_snapshot.csv`, `pagemap_snapshot.csv`
- **3 张人工/主机端维护表**: `app_list.csv`, `operation_list.csv`, `future_need_label.csv`

## 6 张数据表说明

| 表名 | 维护方式 | 粒度 |
|------|---------|------|
| `app_list.csv` | 人工维护 | 每个应用一行 |
| `operation_list.csv` | 人工/主机端维护 | 每次操作一行 |
| `snapshot_index.csv` | C 程序追加一行 | 每次快照一行 |
| `vma_memory_snapshot.csv` | C 程序追加多行 | 每个 VMA 一行，合并 maps + smaps |
| `pagemap_snapshot.csv` | C 程序追加多行 | 每个 VMA 一行，按 VMA 聚合 pagemap |
| `future_need_label.csv` | 先只生成表头，后续人工/模型填写 | 按 VMA 标注 |

## 一键采集（推荐）

```bash
# 在 Windows 主机端（Git Bash），一行完成：编译 → 推送 → 采集 → 拉回
./scripts/collect.sh <PID> [应用名]

# 示例
./scripts/collect.sh 42820 斗鱼
./scripts/collect.sh 42820 斗鱼 -o op_launch
./scripts/collect.sh 42820                # 自动从设备获取进程名
```

脚本自动完成 4 步：
1. 交叉编译 memcap.c
2. `hdc file send` 推送到 `/data/local/tmp/memcap/`
3. `hdc shell` 运行采集（auto 生成 sample_id / operation_id）
4. `hdc file recv` 拉回结果到 `memcap_out/`

## 手动编译与部署

```bash
# 交叉编译（使用 DevEco Studio / HarmonyOS SDK 的 native clang）
"$OHOS_SDK/native/llvm/bin/clang.exe" -O2 -std=c11 -Wall -Wextra \
    -target aarch64-linux-ohos \
    --sysroot="$OHOS_SDK/native/sysroot" \
    -o memcap memcap.c

# 推送到设备
hdc shell mkdir -p /data/local/tmp/memcap
hdc file send memcap /data/local/tmp/memcap/memcap
hdc shell chmod 755 /data/local/tmp/memcap/memcap

# 运行快照采集
hdc shell '/data/local/tmp/memcap/memcap <pid> /data/local/tmp/memcap/out <sample_id> <operation_id> <app_id> <app_name> <process_name> <snapshot_index> <foreground_state>'

# 拉回结果
hdc file recv /data/local/tmp/memcap/out ./memcap_out
```

> Windows Git Bash 下注意：所有 hdc 命令前需加 `MSYS_NO_PATHCONV=1`，否则 Unix 路径会被 MSYS2 错误转换。

## 关键实现要点

1. **page_size** 必须用 `sysconf(_SC_PAGESIZE)`，不要写死 4096
2. **pagemap 读取**按 VMA 聚合，不要每页一行输出 CSV
3. **pagemap bit 规则**: bit63=present, bit62=swapped, bit61=file/shared-anon, bit56=exclusive, bit55=soft-dirty
4. **PFN** 不作为第一版指标（受 CAP_SYS_ADMIN 限制，权限不足时被置零）
5. **pagemap 权限失败不崩溃**，scan_status 字段写 `open_pagemap_failed`
6. **smaps 读取不到的字段默认填 0**（不填 -1），避免 CSV 分析时误判
7. **VMA 和 pagemap 输出先写 `.tmp.<pid>` 临时文件**，写完再追加到共享 CSV，防止两个 memcap 并发写同一文件时交叉损坏
8. **不要同时运行两个 memcap 到同一个 out_dir**，虽然已用临时文件降低风险，但 snapshot_index 的追加仍可能交叉

## 文件结构（规划）

```
huawei_mem/
├── memcap.c               # 主程序（设备端 C 采集程序）
├── CLAUDE.md              # 本规则文件
├── .gitignore
├── scripts/
│   └── collect.sh         # 一键采集脚本（编译+推送+采集+拉回）
├── docs/                  # 后续添加，文档
└── memcap_out/            # 拉回的 CSV 结果（gitignore）
```

## 工作约定

- 每次 git 提交写清楚改动内容和原因，方便回溯
- 代码修改优先保留可运行的单文件形态，后续再拆分模块
- 涉及 /proc 接口的行为以 Linux 内核文档和 HarmonyOS 实际表现为准
- C 代码风格：C11 标准，简洁优先，不引入不必要的外部依赖
