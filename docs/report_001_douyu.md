# memcap 采集报告 #001 — 斗鱼内存快照

> 采集日期：2026-05-25
> 设备：HUAWEI MateBook Pro (HAD-W32)，HongMeng Kernel 1.12.0，aarch64
> 工具版本：memcap v0.2 (commit 958037c)

---

## 1. 采集概况

| 项目 | 值 |
|------|-----|
| 目标应用 | 斗鱼 (com.douyu.ho.app) |
| 采集方式 | hdc shell 运行 memcap，单次瞬时快照 |
| 采集进程 | 主进程 + GPU 进程（共 2 个） |
| Sample ID | sample_002 |
| 采集耗时 | 主进程约 70s，GPU 进程约 20s |
| 数据量 | 8,644 行 VMA + 8,644 行 pagemap |

## 2. 进程概览

```
PID     PPID   进程名
42820    683   com.douyu.ho.app          主进程
43313   6258   com.douyu.ho.app:gpu       GPU 渲染进程
```

> 斗鱼采用 HarmonyOS 标准多进程架构：主进程负责应用逻辑，GPU 进程处理渲染。

## 3. 内存总览 (smaps)

| 指标 | 主进程 (42820) | GPU 进程 (43313) |
|------|:-----------:|:-----------:|
| VMA 数量 | 6,554 | 2,090 |
| **RSS (实际物理内存)** | **618.8 MB** | **49.7 MB** |
| **PSS (按份额分摊)** | **488.3 MB** | **29.4 MB** |
| Referenced | 613.5 MB | 49.7 MB |
| **Swap** | **55.6 MB** | **12.0 MB** |
| 虚拟地址空间 (Anonymous) | ~42 GB | ~35 GB |

> Anonymous 值极大是因为 Chromium partition_alloc 预留了 4 个 ~16GB 的 `---p` 虚拟地址池（RSS=0，不占物理内存）。

## 4. 页表分析 (pagemap)

| 指标 | 主进程 (42820) | GPU 进程 (43313) |
|------|:-----------:|:-----------:|
| 虚拟总页数 | 12,157,159 (47.5 GB) | 10,196,634 (39.8 GB) |
| **Present（在RAM）** | **171,123 页 (668 MB)** | **13,591 页 (53 MB)** |
| Not Present（未分配） | 11,971,808 页 (46.8 GB) | 10,179,965 页 (39.8 GB) |
| Swapped（已换出） | 14,228 页 (55.6 MB) | 3,078 页 (12.0 MB) |
| **物理驻留比例** | **1.41%** | **0.13%** |
| 换出比例 | 0.12% | 0.03% |
| File/Shared 页 | 55,904 页 (218 MB) | — |
| Exclusive 页 | 112,070 页 (438 MB) | — |
| Soft Dirty 页 | 0 | — |

> 两个进程的虚拟地址空间都极大（47/40 GB），但实际物理驻留极低（1.4%/0.1%）。这是 Chromium 系应用的典型特征：大虚拟地址池 + 按需提交。

## 5. 主进程 VMA 区域分类

| 区域类型 | VMA 数量 | RSS | 说明 |
|----------|:-----:|:------|------|
| other | 1,177 | **361.9 MB** | ArkTS 堆、partition_alloc、CFI shadow 等 |
| shared_lib | 4,335 | 195.8 MB | .so 共享库映射 |
| file | 879 | 48.2 MB | 文件映射（字体、资源等） |
| anon | 161 | 12.8 MB | 匿名映射 |
| stack | 2 | 0.1 MB | 线程栈 |
| **合计** | **6,554** | **618.8 MB** | |

> "other" 区域占比最高（58.5% RSS），主要包括 `[anon:ArkTS Heap]`、`[anon:partition_alloc]`、`[anon:cfi_shadow:musl]` 等 ArkTS 运行时内存。当前 `classify_region()` 对这些 `[anon:xxx]` 命名区域统一归为 other，后续可细化分类。

## 6. GPU 进程 VMA 区域分类

| 区域类型 | VMA 数量 | RSS | 说明 |
|----------|:-----:|:------|------|
| shared_lib | 1,795 | **39.5 MB** | 共享库（GPU 驱动、渲染库等） |
| other | 212 | 9.0 MB | 匿名内存区域 |
| file | 41 | 1.3 MB | 文件映射 |
| anon | 41 | 0.1 MB | 匿名映射 |
| stack | 1 | 0.06 MB | 线程栈 |
| **合计** | **2,090** | **49.7 MB** | |

> GPU 进程 86% 的 RSS 来自 shared_lib，说明其内存主要消耗在 GPU 驱动和系统渲染库上。

## 7. 关键发现

1. **物理内存适中**：斗鱼主进程占 ~620 MB，GPU 进程 ~50 MB，合计约 670 MB，在 HarmonyOS PC 上属于正常水平。

2. **Swap 使用明显**：主进程 56 MB 换出（占总虚拟页 0.12%），GPU 进程 12 MB（0.03%），说明系统内存有一定压力。

3. **虚拟地址空间巨大**：主进程虚拟空间 47.5 GB，但 98.5% 未实际分配物理页。这是 Chromium 引擎的 partition_alloc 设计所致（预保留大地址池），不影响实际内存。

4. **ArkTS 运行时是主要内存消费者**："other" 类型（含 ArkTS 堆）占主进程 RSS 的 58.5%，是优化的首要目标。

5. **region_type 分类待细化**：当前 `[anon:ArkTS Heap]`、`[anon:partition_alloc]` 等 ArkTS 相关区域被归为 "other"，需要扩展 `classify_region()` 提高分类精度。

## 8. 后续工作

- [ ] 细化 `classify_region()` 中的区域分类（识别 ArkTS Heap、partition_alloc、jemalloc 等）
- [ ] 对斗鱼做 2-3 次不同操作（冷启动、播放视频、切后台）的快照对比
- [ ] 分析 partition_alloc 的 4 个 ~16GB 预留区域的页分配模式
- [ ] MacBook 上搭建开发环境，实现跨平台编译
- [ ] 补充 operation_list.csv 中的人工操作描述

---

*报告由 memcap 工具自动采集数据生成，人工汇总分析。*
