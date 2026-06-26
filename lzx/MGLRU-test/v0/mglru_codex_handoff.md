# MGLRU Page Control Handoff

本文档给另一台机器上的 Codex 读取，用来接续当前 MGLRU 页级控制实验。

## 当前状态

- 目标内核已经迁移并启动成功。
- `uname -r` 已显示：`6.17.13-mglru`
- 说明当前机器已经运行我们改过的 Ubuntu HWE 6.17 内核。
- 主要代码修改位于：
  - `/usr/src/linux-hwe-6.17-6.17.0/mm/vmscan.c`
- 原始迁移包在旧机器上曾生成：
  - `内核内存调度/mglru-kernel-transfer-kit.tar.zst`
- patch 文件名：
  - `mglru_page_control.patch`

## 我们做了什么

在 MGLRU 代码路径中增加了一个实验性 debugfs 控制面：

```text
/sys/kernel/debug/lru_gen_pages
```

目标是让用户态可以按 PFN/head PFN 对 folio 做页级控制：

- 手动提升指定 folio 到最新 generation。
- 将指定 folio 加入保护集合，使其在 MGLRU eviction 前被跳过并重新热化。
- 对指定 folio 设置 scan 策略，在指定 `scan_control.priority` 范围内 skip 或 only。

没有修改 `folio->flags` 布局，没有新增 page flag。所有实验状态都保存在 `mm/vmscan.c` 内部的 MGLRU page policy 表中。

## 关键代码位置

在 `/usr/src/linux-hwe-6.17-6.17.0/mm/vmscan.c` 中：

- `MGLRU_PAGE_POLICY_PROTECT/SKIP/ONLY`：约 3317 行。
- `struct mglru_page_policy` 和策略链表/锁：约 3321 行。
- `mglru_promote_folio_locked()`：约 3375 行。
- `mglru_page_policy_reheat()`：约 3433 行。
- `mglru_page_policy_can_isolate()`：约 3462 行。
- debugfs 写入解析：`mglru_page_policy_parse_line()`，约 3673 行。
- debugfs 输出：`mglru_page_policy_show()`，约 3790 行。
- `sort_folio()` 附近的保护/skip 热化插桩：约 5008 行。
- `isolate_folio()` 前的轻量重检：约 5068 行。
- 创建 `/sys/kernel/debug/lru_gen_pages`：约 6312 行。

可以用下面命令快速定位：

```bash
rg -n "lru_gen_pages|MGLRU_PAGE_POLICY|mglru_page_policy|mglru_promote_folio_locked" \
  /usr/src/linux-hwe-6.17-6.17.0/mm/vmscan.c
```

## debugfs 接口

先确认 debugfs 已挂载：

```bash
mount | grep debugfs || sudo mount -t debugfs debugfs /sys/kernel/debug
```

确认接口存在：

```bash
ls -l /sys/kernel/debug/lru_gen_pages
cat /sys/kernel/debug/lru_gen_pages
```

支持的写入命令：

```text
promote <pfn> <nr_pages>
protect add <pfn> <nr_pages>
protect del <pfn> <nr_pages>
scan skip add <prio_min> <prio_max> <pfn> <nr_pages>
scan skip del <prio_min> <prio_max> <pfn> <nr_pages>
scan only add <prio_min> <prio_max> <pfn> <nr_pages>
scan only del <prio_min> <prio_max> <pfn> <nr_pages>
clear all
```

示例：

```bash
sudo sh -c 'echo "promote 123456 1" > /sys/kernel/debug/lru_gen_pages'
sudo sh -c 'echo "protect add 123456 1" > /sys/kernel/debug/lru_gen_pages'
sudo sh -c 'echo "scan skip add 0 12 123456 1" > /sys/kernel/debug/lru_gen_pages'
sudo sh -c 'echo "scan only add 0 12 123456 1" > /sys/kernel/debug/lru_gen_pages'
sudo sh -c 'echo "clear all" > /sys/kernel/debug/lru_gen_pages'
cat /sys/kernel/debug/lru_gen_pages
```

读取 `/sys/kernel/debug/lru_gen_pages` 时会输出策略项，包括 head PFN、flags、priority 范围和 hit 计数。

## 行为设计

### PFN 到 folio

- 用户输入 PFN 或 folio head PFN。
- 内核侧使用 `pfn_to_online_folio()` 找 folio。
- 自动归一化到 `folio_pfn(folio)`。
- 对无效 PFN、离线 PFN、非 LRU folio，会跳过或返回错误。

### promote

`promote <pfn> <nr_pages>` 会尝试把范围内 folio 提升到当前 MGLRU 最新 generation：

```c
lru_gen_from_seq(lrugen->max_seq)
```

更新时不是只改 flag，而是同步调整：

- folio 的 LRU generation bits。
- `lrugen->nr_pages[old_gen][type][zone]`
- `lrugen->nr_pages[new_gen][type][zone]`
- folio 所在 `lrugen->folios[new_gen][type][zone]` 链表。

### protect

`protect add` 添加硬保护规则。命中后：

- 在 MGLRU eviction 路径中跳过 isolate。
- 将 folio 热化到最新 generation。
- 增加 hit 计数。

注意：这不是 `mlock()`，也不是 pin page。它只保护 MGLRU eviction 路径。

### scan skip

`scan skip add <prio_min> <prio_max> <pfn> <nr_pages>` 表示：

- 当前 `scan_control.priority` 落入 `[prio_min, prio_max]` 时，
- 匹配 folio 不进入 isolate/reclaim，
- 并被重新热化。

### scan only

`scan only add <prio_min> <prio_max> <pfn> <nr_pages>` 表示：

- 当前 priority 范围内启用 only 模式。
- 同 priority 下，未命中 only 集合的 folio 不进入 isolate/reclaim。
- 命中 only 集合的 folio 允许继续走 isolate/reclaim。

## 下一步必须验证的内容

### 1. 基础启动验证

```bash
uname -r
zgrep CONFIG_LRU_GEN /proc/config.gz 2>/dev/null || grep CONFIG_LRU_GEN /boot/config-$(uname -r)
ls -l /sys/kernel/debug/lru_gen /sys/kernel/debug/lru_gen_full /sys/kernel/debug/lru_gen_pages
cat /sys/kernel/debug/lru_gen_pages
```

期望：

- `uname -r` 是 `6.17.13-mglru`
- `CONFIG_LRU_GEN=y`
- `lru_gen_pages` 存在且可读写。

### 2. promote 功能验证

需要准备一个用户态工具或脚本拿到目标页的 PFN/head PFN。此前计划优先复用已有 v10 工具输出。

执行：

```bash
sudo sh -c 'echo "promote <head_pfn> 1" > /sys/kernel/debug/lru_gen_pages'
cat /sys/kernel/debug/lru_gen
cat /sys/kernel/debug/lru_gen_pages
```

观察：

- 命令不报错。
- 对应 folio 的 generation 统计有合理变化。
- `lru_gen_pages` 中相关策略或 hit 信息合理。

### 3. protect 功能验证

执行：

```bash
sudo sh -c 'echo "protect add <head_pfn> 1" > /sys/kernel/debug/lru_gen_pages'
cat /sys/kernel/debug/lru_gen_pages
```

然后对目标进程施加内存压力，让 MGLRU 发生 reclaim。

观察：

- 被 protect 的 PFN hit 计数增加。
- 该 folio 不应进入 MGLRU reclaim list。
- 目标页在压力下不应被 MGLRU 换出。

删除规则：

```bash
sudo sh -c 'echo "protect del <head_pfn> 1" > /sys/kernel/debug/lru_gen_pages'
```

### 4. scan skip 验证

执行：

```bash
sudo sh -c 'echo "scan skip add 0 12 <head_pfn> 1" > /sys/kernel/debug/lru_gen_pages'
cat /sys/kernel/debug/lru_gen_pages
```

制造内存压力后观察：

- priority 落入范围时，匹配 folio 被跳过 isolate。
- hit 计数增加。
- folio 被重新热化。

### 5. scan only 验证

执行：

```bash
sudo sh -c 'echo "scan only add 0 12 <head_pfn> 1" > /sys/kernel/debug/lru_gen_pages'
cat /sys/kernel/debug/lru_gen_pages
```

制造内存压力后观察：

- 当前 priority 命中 only 模式时，非匹配 folio 不进入 isolate/reclaim。
- 匹配 folio 仍允许进入 isolate/reclaim。
- hit 计数和 reclaim 行为与预期一致。

### 6. clear all 回归

```bash
sudo sh -c 'echo "clear all" > /sys/kernel/debug/lru_gen_pages'
cat /sys/kernel/debug/lru_gen_pages
```

期望：

- 所有页级策略清空。
- MGLRU 行为恢复默认。
- 原有 `/sys/kernel/debug/lru_gen` 的 `+` aging 和 `-` eviction 命令行为不变。

## 建议测试矩阵

需要覆盖：

- 匿名页。
- 文件页。
- THP/compound folio。
- 无效 PFN。
- 已释放后复用的 PFN。
- 非 LRU folio。
- 不同 memcg。
- 不同 NUMA node/zone。
- priority 边界：`0`、`DEF_PRIORITY`、范围外。

## 注意事项和风险

- 规则按物理 PFN 生效。如果 PFN 后续释放并被复用，规则会作用到新的 folio，直到用户删除规则或 `clear all`。
- 这是实验性 debugfs 接口，不是稳定 ABI。
- `protect` 只覆盖 MGLRU eviction 路径，不等价于 `mlock()` 或长期 pin。
- 如果系统未挂载 debugfs，`/sys/kernel/debug/lru_gen_pages` 不会显示。
- 如果看不到 MGLRU 接口，先确认 `CONFIG_LRU_GEN=y` 和当前运行内核确实是 `6.17.13-mglru`。

## 常用命令

查看 MGLRU：

```bash
cat /sys/kernel/debug/lru_gen
cat /sys/kernel/debug/lru_gen_full
cat /sys/kernel/debug/lru_gen_pages
```

清空策略：

```bash
sudo sh -c 'echo "clear all" > /sys/kernel/debug/lru_gen_pages'
```

查看内核日志：

```bash
dmesg -T | tail -200
```

重新定位代码：

```bash
rg -n "lru_gen_pages|MGLRU_PAGE_POLICY|mglru_page_policy" \
  /usr/src/linux-hwe-6.17-6.17.0/mm/vmscan.c
```

## 给下一位 Codex 的工作建议

1. 先确认目标机运行的是 `6.17.13-mglru`。
2. 确认 `/sys/kernel/debug/lru_gen_pages` 存在。
3. 使用已有 v10 工具或新脚本获取目标 folio head PFN。
4. 依次验证 `promote`、`protect`、`scan skip`、`scan only`。
5. 重点检查 reclaim 压力下 hit 计数和 folio 是否真的避开 isolate/reclaim。
6. 如果行为不符，优先看 `mm/vmscan.c` 中 `sort_folio()` 和 `isolate_folio()` 前的策略判断。
