# 鸿蒙 PC 内存页快照采集工具 — 项目进展报告

> 日期：2026-05-25 | 版本：v0.2 | 作者：人+Claude Code 协作

---

## 一、项目定位

在 Windows 主机端，通过 hdc 连接鸿蒙 PC（HUAWEI MateBook Pro HAD-W32），
对目标应用进程做**单次内存页快照采集**，输出 CSV 供后续分析。

./scripts/device/collect.sh 42820 斗鱼   # 输入 PID + 应用名
读取 /proc/[pid]/maps + smaps + pagemap，生成 6 张 CSV 表。

./scripts/device/collect.sh 斗鱼          # 只需应用名，自动找 PID
./scripts/device/collect.sh 斗鱼 --all   # 一键采集斗鱼所有子进程
## 二、当前进度


| 模块 | 状态 | 说明 |
|------|:----:|------|
| memcap.c 核心程序 | ✅ v0.2 | C11，零警告编译，交叉编译为 aarch64 ELF |
| 一键采集脚本 | ✅ | scripts/device/collect.sh，编译→推送→采集→拉回全自动 |
| 6 张 CSV 表 | ✅ | app_list / operation_list / snapshot_index / vma / pagemap / future_need_label |
| maps 解析 | ✅ | parse_maps()，最多 200,000 个 VMA |
| smaps 解析 | ✅ | parse_smaps()，按地址区间合并 Rss/Pss/Referenced/Anonymous/Swap/VmFlags |
| pagemap 按 VMA 聚合 | ✅ | scan_pagemap()，聚合 present/swapped/file_shared/exclusive/soft_dirty |
│   ├── device/
│   │   └── collect.sh          # 一键采集脚本
│   ├── analysis/
│   │   └── analyze_memory.py  # 对比分析脚本
│   └── pipeline/
│       └── run_first_stage.sh  # 流水线入口脚本
| 权限失败容错 | ✅ | pagemap 打不开时 scan_status=open_pagemap_failed，不崩溃 |
| 并发写入保护 | ✅ | VMA/pagemap 先写 .tmp.PID 临时文件，写完再追加到共享 CSV |
| 斗鱼首次采集 | ✅ | 主进程 + GPU 进程，8644 行数据 |
| 采集报告 #001 | ✅ | docs/report_001_douyu.md |
| Git 版本管理 | ✅ | 4 次提交，完整历史 |
| .gitignore | ✅ | memcap（编译产物）、memcap_out/（采集结果）、.claude/ 均忽略 |

### 2.2 斗鱼采集数据摘要

| 指标 | 主进程 | GPU 进程 |
|------|:-----:|:-----:|
| VMA 数 | 6,554 | 2,090 |
| 物理内存 (RSS) | 619 MB | 50 MB |
| 虚拟地址空间 | 47.5 GB | 39.8 GB |
| 物理驻留率 | 1.41% | 0.13% |
| Swap | 56 MB | 12 MB |

> 关键发现：斗鱼内存主要消耗在 ArkTS 运行时（58.5% RSS），
> 虚拟空间巨大但 98.5% 未分配物理页（Chromium partition_alloc 特征）。

---

## 三、当前工作流（改进后）

```bash
# 旧方式（繁琐）
hdc shell "ps -A | grep douyu"    # 手动找 PID
./scripts/device/collect.sh 42820 斗鱼   # 输入 PID + 应用名

# 新方式（改进中）
./scripts/device/collect.sh 斗鱼          # 只需应用名，自动找 PID
./scripts/device/collect.sh 斗鱼 --all   # 一键采集斗鱼所有子进程
```

---

## 四、当前痛点

| 问题 | 影响 | 优先级 |
|------|------|:----:|
| 每次重启应用 PID 就变 | 每次采集前必须手动查 PID | 🔴 高 |
| 多次操作需重复输入命令 | 操作 10 次 = 敲 10 遍命令 | 🔴 高 |
| region_type 分类粗糙 | ArkTS Heap、partition_alloc 等全归为 "other" | 🟡 中 |
| 只能在本机编译采集 | MacBook 上只能编辑代码，不能跑 | 🟡 中 |
| 无多次快照对比能力 | 当前只有单次快照，无法做 diff | 🟢 低 |

---

## 五、下一步计划

### Phase 1：降低采集操作门槛（本周）

1. **进程名自动查找 PID**
   - scripts/device/collect.sh 接受进程名（如 `douyu`），自动 `hdc shell pidof` 查找 PID
   - 支持模糊匹配（`斗鱼` → `com.douyu.ho.app`）

2. **交互式采集会话**
   - `scripts/device/collect.sh --session 斗鱼`
   - 启动后自动查 PID → 做第一次快照 → 等待用户按 Enter → 做第二次快照 → ...
   - 每次快照前用户输入操作描述（如"点击播放按钮"），自动记入 operation_list.csv
   - 连续 10 次操作只需启动脚本一次，中间按 Enter 即可

3. **单命令采集所有子进程**
   - `scripts/device/collect.sh 斗鱼 --all`：自动找到 斗鱼 的所有子进程，逐个采集

### Phase 2：分析能力提升（下周）

4. **细化 region_type 分类**
   - 识别 `[anon:ArkTS Heap]` → `ark_ts_heap`
   - 识别 `[anon:partition_alloc]` → `partition_alloc`
   - 识别 `[anon:jemalloc]` / `[anon:native_heap]` → `native_heap`
   - 识别 `[anon:cfi_shadow]` / `[stack]` / `[vdso]` 等

5. **快照对比工具**
   - 脚本：输入两次快照的 sample_id，输出 VMA 级别 RSS 变化（diff）
   - 识别"持续增长"的 VMA（可能内存泄漏）

### Phase 3：跨设备开发（本月）

6. **MacBook 开发环境搭建**
   - 在 MacBook 上 clone 代码，编辑 + git 提交
   - 编译和采集仍回到 Windows 本机执行
   - 可选：Mac 上安装 DevEco Studio SDK 实现本地编译

---

## 六、项目文件索引

```
huawei_mem/
├── memcap.c                    # 设备端 C 采集程序（350 行）
├── CLAUDE.md                   # 项目规则文档
├── .gitignore
├── scripts/
│   ├── device/
│   │   └── collect.sh          # 一键采集脚本
│   ├── analysis/
│   │   └── analyze_memory.py   # 对比分析脚本
│   └── pipeline/
│       └── run_first_stage.sh  # 流水线入口脚本
├── docs/
│   ├── progress_report.md      # 本文件 — 项目进展报告
│   └── report_001_douyu.md     # 斗鱼内存快照采集报告
└── memcap_out/                 # 采集结果（不纳入版本管理）
   ├── snapshot_index.csv
   ├── vma_memory_snapshot.csv
   ├── pagemap_snapshot.csv
   ├── app_list.csv
   ├── operation_list.csv
   └── future_need_label.csv
```

---

## 七、参考命令速查

```bash
# 查看可用进程
hdc shell "ps -A -o PID,ARGS"

# 查找特定应用 PID
hdc shell "pidof com.douyu.ho.app"

# 一键采集
./scripts/device/collect.sh <PID> <应用名>

# 查看采集结果
cat memcap_out/snapshot_index.csv
awk -F',' '$19>0{rss+=$19;n++} END{printf "VMA=%d RSS=%dKB\n",n,rss}' memcap_out/vma_memory_snapshot.csv

# 推送到 GitHub
git remote add origin git@github.com:用户名/huawei_mem.git
git push -u origin master
```

---

*本报告随项目进展持续更新。*
