# memcap 技术手册

> 面向开发者的技术深度文档，涵盖交叉编译、CSV 指标设计、后处理分析全链路。

---

## 一、交叉编译环境搭建

### 1.1 工具链获取

鸿蒙设备 (aarch64-linux-ohos) 的 C 程序需要在主机端交叉编译。DevEco Studio 自带完整工具链：

| 组件 | macOS 路径 | Windows 路径 |
|------|-----------|-------------|
| clang | `.../sdk/default/openharmony/native/llvm/bin/clang` | `.../sdk/.../llvm/bin/clang.exe` |
| sysroot | `.../sdk/default/openharmony/native/sysroot` | `.../sdk/.../native/sysroot` |
| hdc | `~/Library/OpenHarmony/Sdk/23/toolchains/hdc` | `.../sdk/.../toolchains/hdc.exe` |

### 1.2 编译命令

```bash
clang -O2 -std=c11 -Wall -Wextra \
    -target aarch64-linux-ohos \
    --sysroot="$OHOS_SDK/sysroot" \
    -o memcap memcap.c
```

**参数说明**：
- `-target aarch64-linux-ohos`：目标三元组，指定 ARM64 + Linux + HarmonyOS ABI
- `--sysroot`：指向 OpenHarmony 系统根目录，提供 libc、系统头文件等
- `-O2 -std=c11`：生产级优化 + C11 标准

### 1.3 平台自动检测

`collect.sh` 和 `setup_env.sh` 都内置了平台检测逻辑：

```bash
# macOS
if [[ -d "/Applications/DevEco-Studio.app" ]]; then
    SDK_BASE="/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native"
fi

# Windows
if [[ -d "D:/Program Files/Huawei/DevEco Studio" ]]; then
    SDK_BASE="D:/Program Files/Huawei/DevEco Studio/sdk/default/openharmony/native"
fi
```

### 1.4 hdc 通信架构

hdc (HarmonyOS Device Connector) 是类 adb 的设备通信工具：

```
主机端 hdc client ──USB/TCP──→ 设备端 hdcd daemon
     │                              │
     ├─ hdc shell <cmd> ──────────→ 执行 shell 命令
     ├─ hdc file send <src> <dst> → 推送文件到设备
     └─ hdc file recv <src> <dst> ← 从设备拉取文件
```

`collect.sh` 的完整采集流程：编译 → hdc file send → hdc shell 运行 → hdc file recv 拉回。

---

## 二、CSV 指标设计

### 2.1 设计原则

项目输出 6 张 CSV 表，分两类：

**自动采集表（C 程序写入）**：
- `snapshot_index.csv`：快照元数据索引
- `vma_memory_snapshot.csv`：VMA 级别内存统计（maps + smaps 合并）
- `pagemap_snapshot.csv`：VMA 级别页表分析（pagemap 聚合）

**人工维护表（主机端编辑）**：
- `app_list.csv`：应用注册表
- `operation_list.csv`：用户操作日志
- `future_need_label.csv`：VMA 标注（预留）

### 2.2 表间关联

```
app_list ──→ operation_list ──→ snapshot_index ──→ vma_memory_snapshot
                 app_id            sample_id              │
                                   operation_id           ├─ vma_id（一一对应）
                                                          │
                                                      pagemap_snapshot
```

**核心关联键**：`(sample_id, pid, vma_id)` 将 VMA 统计和页表数据一一对应。设计理由：
- `sample_id`：标识一次采集会话（同一应用可有多进程）
- `pid`：区分不同进程
- `vma_id`：`vma_000001` 格式，在 VMA CSV 和 pagemap CSV 中保持一致

### 2.3 vma_memory_snapshot.csv 列设计

```
sample_id, operation_id, app_id, app_name, process_name, pid,
timestamp_ms, snapshot_index,
vma_id, vma_start, vma_end, vma_size_kb,
perms, offset, dev, inode, pathname, region_type,
rss_kb, pss_kb, referenced_kb, anonymous_kb, swap_kb,
vm_flags, note
```

**数据来源**：

| 列组 | 来源 | 解析方式 |
|------|------|---------|
| vma_start ~ pathname | `/proc/pid/maps` | `sscanf("%lx-%lx %s %lx %s %lu %s")` |
| rss_kb ~ swap_kb | `/proc/pid/smaps` | 按地址区间匹配 VMA，`sscanf("Rss: %ld kB")` |
| region_type | 本地计算 | `classify_region()`：根据 pathname 分类 |
| vm_flags | `/proc/pid/smaps` | `VmFlags:` 行原始输出 |

### 2.4 pagemap_snapshot.csv 列设计

```
sample_id, operation_id, ..., vma_id, vma_start, vma_end,
page_count, present_pages, not_present_pages, swapped_pages,
file_or_shared_pages, exclusive_pages, soft_dirty_pages,
present_ratio, swapped_ratio, scan_status, note
```

**为什么按 VMA 聚合而不是逐页输出？**

逐页输出会导致 CSV 爆炸：斗鱼主进程 1200 万虚拟页，每页一行将产生 ~1GB 的 CSV 文件，无法分析。按 VMA 聚合（6500 行）既保留了分析粒度，又控制了数据量。

**pagemap 64-bit entry 位定义**：

```
Bit 63: PRESENT      — 页面当前在物理 RAM 中
Bit 62: SWAPPED      — 页面被换出到 swap 设备
Bit 61: FILE/SHARED  — 文件映射页或共享内存页
Bit 56: EXCLUSIVE    — 该进程独占（非共享）
Bit 55: SOFT_DIRTY   — 软脏页标记（写追踪）
```

**读取方式**：`pread(fd, &entry, 8, (vaddr / page_size) * 8)`，按虚拟地址计算文件偏移量，逐页读取 8 字节 entry。

### 2.5 region_type 分类规则

```c
static void classify_region(VMA *v) {
    if (strstr(p, "[heap]"))              → "heap"
    else if (strstr(p, "[stack]"))        → "stack"
    else if (strlen(p) == 0)              → "anon"
    else if (strstr(p, ".so"))            → "shared_lib"
    else if (strstr(p, "/"))              → "file"
    else                                  → "other"
}
```

**已知局限**：`[anon:ArkTS Heap]`、`[anon:partition_alloc]` 等 ArkTS 运行时区域被归入 `other`，导致 `other` 占主进程 RSS 的 58.5%。下一步应扩展分类逻辑。

### 2.6 并发写入保护

```c
// 先写临时文件，写完后追加到共享 CSV
snprintf(tmp, sizeof(tmp), "%s/vma_memory_snapshot.csv.tmp.%d", outdir, pid);
FILE *f = fopen(tmp, "w");
// ... 写入 VMA 数据 ...
fclose(f);
append_temp_to_file(tmp, dest);  // 追加 + 删临时文件
```

防止两个 memcap 进程同时写入同一 CSV 文件时交叉损坏。

---

## 三、Python 后处理分析

### 3.1 analyze_memory.py 架构

```
CSV加载层
├── parse_snapshot_index()   → List[SnapshotMeta]
├── parse_vma_csv()          → List[VmaRow]  
├── parse_pagemap_csv()      → List[PagemapRow]
└── build_pagemap_index()    → Dict[(sample_id, vma_id), PagemapRow]

匹配引擎
├── make_exact_key()  → "pid:vma_start-vma_end"    （同 PID）
├── make_fuzzy_key()  → "pathname|region_type|perms" （跨 PID）
└── detect_mode()     → 根据 PID 集合大小自动选择

对比分析
└── match_and_compare()
    ├── 按匹配键分组 VMA
    ├── 每个 VMA 关联 pagemap 数据
    ├── 计算 persistence = present_count / total_snapshots
    └── 排序输出

报告输出
└── print_report()
    ├── Hot   (persistence ≥ 90%)
    ├── Dynamic (30% ≤ p < 90%)
    └── Cold  (p < 30%)
```

### 3.2 匹配策略详解

**Exact 模式** — PID 不变时使用：

```
快照A: PID=9376, [4281a00000-4281a14000] rw-p [anon:ArkTS Heap]
快照B: PID=9376, [4281a00000-4281a14000] rw-p [anon:ArkTS Heap]
匹配键 = "9376:4281a00000-4281a14000" ✓ 精确匹配
```

**Fuzzy 模式** — PID 变化 (ASLR) 时使用：

```
快照A: PID=9376,  [4e800000-4e8a0000] [anon:ArkTS Heap]
快照B: PID=25797, [5f200000-5f2a0000] [anon:ArkTS Heap]
地址不同（ASLR），但 匹配键 = "[anon:ArkTS Heap]|other|rw-p" ✓ 语义匹配
```

**匹配率数据（斗鱼实验）**：
- 同 PID 匹配率 97.7%（仅 2.3% 的 VMA 新增或消失）
- 跨 PID 匹配率 80.3%（约 20% 因 ASLR 无法精确匹配，需 fuzzy）

### 3.3 持久化得分计算

```python
persistence = 0
for snapshot in snapshots:
    pm = pagemap_index[(snapshot.sample_id, vma.vma_id)]
    if pm and pm.present_ratio >= threshold:  # 默认 0.8
        persistence += 1
persistence_score = persistence / len(snapshots)
```

**阈值 0.8 的含义**：VMA 中至少 80% 的虚拟页在物理 RAM 中，才算"有效驻留"。这个阈值过滤掉了只有稀疏分配的 VMA（如 partition_alloc 的 16GB 地址池）。

### 3.4 使用示例

```bash
# 基本用法：自动检测模式
python3 scripts/analyze_memory.py -i memcap_out/

# 指定 PID 过滤
python3 scripts/analyze_memory.py -i memcap_out/ --pid 9376

# 跨重启模糊匹配
python3 scripts/analyze_memory.py -i memcap_out/ --mode fuzzy --threshold 0.7

# 指定快照子集
python3 scripts/analyze_memory.py -i memcap_out/ \
    --sample sample_001 sample_002 sample_003

# 完整输出（不截断 Hot 列表）
python3 scripts/analyze_memory.py -i memcap_out/ --full
```

---

## 四、/proc 接口深入

### 4.1 三个文件的角色

```
/proc/[pid]/maps      → VMA 的"地籍图"：每块地的边界和性质
/proc/[pid]/smaps     → VMA 的"人口普查"：每块地住了多少人
/proc/[pid]/pagemap   → VMA 的"逐户清查"：每个平方米是否有人
```

数据粒度逐级细化：

| 文件 | 粒度 | 斗鱼主进程数据量 |
|------|------|:--------------:|
| maps | VMA (6500 条) | ~500 KB |
| smaps | VMA + 统计 (6500 条) | ~2 MB |
| pagemap | 虚拟页 (1200 万条) | ~96 MB（二进制） |

### 4.2 maps 解析

```
地址范围          权限   偏移    设备    inode  路径名
4281a00000-4281a14000 rw-p 00000000 00:00 0      [anon:ArkTS Heap and GC]
│                  │    │       │       │    │      │
起始地址           结束  读写私有 文件偏移 设备号 inode  映射名称（匿名则显示 [anon:...]）
```

### 4.3 smaps 解析 — 按地址区间匹配

smaps 的输出结构是**按 VMA 分组**的，每个 VMA 先输出一行地址范围（与 maps 相同），再跟若干统计行：

```
4281a00000-4281a14000 rw-p 00000000 00:00 0  [anon:ArkTS Heap]
Rss:        1240 kB    ← 实际物理内存
Pss:         820 kB    ← 按共享比例分摊
Referenced: 1240 kB    ← 被访问过的页
Anonymous:   240 kB    ← 匿名页
Swap:          0 kB    ← 换出量
VmFlags: rd wr mr mw me ac sd
```

memcap 的匹配逻辑：读取到地址行时，在 VMA 数组中 `find_vma()` 精确定位；后续统计行直接填充到当前 VMA。

### 4.4 pagemap 读取性能

pagemap 是二进制文件。读取 1200 万虚拟页（斗鱼主进程）需要 1200 万次 `pread()` 系统调用，耗时约 70 秒。

**优化方向**（未实现）：
- **批量读取**：一次 `pread()` 读多个连续的 8-byte entry（如 512 个 = 4KB），减少系统调用次数
- **跳过未映射区域**：对于 `---p` 权限的 VMA（partition_alloc 预留区），99.9% 的页都是 not present，可抽样确认后跳过

---

## 五、实验工作流

### 5.1 单次采集

```bash
source scripts/setup_env.sh
bash scripts/collect.sh douyu
```

### 5.2 多快照对比实验（完整流程）

```bash
# 1. 初始快照
bash scripts/collect.sh douyu -o op_init -f foreground

# 2. 用户操作后（不关闭应用）
#    在设备上操作：切换直播间、最小化等
bash scripts/collect.sh <PID> 斗鱼 -o op_action -f background

# 3. 重启后
#    关闭并重新打开斗鱼
hdc shell "ps -A -o PID,ARGS" | grep douyu  # 获取新 PID
bash scripts/collect.sh <新PID> 斗鱼 -o op_restart -f foreground

# 4. 分析
python3 scripts/analyze_memory.py -i memcap_out/ --pid <PID>
python3 scripts/analyze_memory.py -i memcap_out/ --mode fuzzy
```

### 5.3 结果解读

| 指标 | 含义 | 关注点 |
|------|------|--------|
| Hot RSS | 跨快照持续驻留的物理内存 | 这是应用的"基础足迹" |
| Dynamic VMA | 间歇驻留的区域 | 前后台切换时的内存抖动 |
| Swap 变化 | 被换出的内存量 | HarmonyOS 后台回收策略强度 |
| VMA 匹配率 | 同 PID 应 >95%，跨 PID 应 >75% | 异常低则说明应用内存布局剧烈变化 |

---

## 六、故障排查

| 问题 | 排查步骤 |
|------|---------|
| `hdc list targets` 为空 | 1. USB 线是否数据线 2. 设备是否开启 USB 调试 3. `hdc kill && hdc start` 重启服务 |
| 编译失败 "clang not found" | `source scripts/setup_env.sh` 或检查 DevEco Studio SDK 是否下载 |
| 采集失败 "open_maps_failed" | PID 是否正确、进程是否仍在运行 |
| pagemap 全是 0 | 检查 `/proc/pid/pagemap` 权限（`ls -la`），可能需要 root |
| analyze_memory.py 报快照不足 | `--min-snapshots 1` 降低阈值，或先多采集几次 |

---

*文档版本: v0.2 | 最后更新: 2026-05-25 | 作者: zhairui1995 + Claude Code*
