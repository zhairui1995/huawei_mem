# mem_analyze 使用说明

本文档说明 `mem_analyze.c` 和 `malloc_stress.c` 的用途、编译方式、运行方式以及报告字段含义。

## 1. 文件说明

当前目录下主要文件：

| 文件 | 作用 |
| --- | --- |
| `mem_analyze.c` | 进程内存分析工具源码 |
| `mem_analyze` | 编译后的分析工具 |
| `malloc_stress.c` | 交互式 malloc 测试进程源码 |
| `malloc_stress` | 编译后的测试进程 |
| `mem_analyze_guide.md` | 本说明文档 |

`mem_analyze` 只能分析 Linux/WSL/Ubuntu 里的进程，不能直接分析 Windows 原生进程。

## 2. 编译

在 Ubuntu/WSL 中执行：

```bash
cd /mnt/d/lzx/Linux
gcc -std=c11 -O2 -Wall -Wextra -o mem_analyze mem_analyze.c
gcc -std=c11 -O2 -Wall -Wextra -o malloc_stress malloc_stress.c
```

建议使用 `sudo` 运行 `mem_analyze`，否则现代 Linux 通常会隐藏 `/proc/<pid>/pagemap` 里的真实 PFN。

## 3. 单次分析模式

分析一个进程：

```bash
sudo ./mem_analyze <pid>
```

默认输出：

```text
mem_analyze_<pid>.md
```

指定输出文件：

```bash
sudo ./mem_analyze <pid> -o report.md
```

也可以一次分析多个 PID：

```bash
sudo ./mem_analyze <pid1> <pid2> <pid3> -o multi_process_report.md
```

## 4. 监控模式

### 4.1 按 app 名称监控

例如监控 Ubuntu 中正在运行的 Firefox：

```bash
sudo ./mem_analyze --watch-app firefox --duration 60 --interval 2 -o firefox_watch.md
```

含义：

| 参数 | 含义 |
| --- | --- |
| `--watch-app firefox` | 自动扫描 `/proc`，找到进程名或命令行包含 `firefox` 的所有进程 |
| `--duration 60` | 总共监控 60 秒 |
| `--interval 2` | 每 2 秒采样一次 |
| `-o firefox_watch.md` | 输出 Markdown 报告 |

### 4.2 按 PID 监控

如果已经知道要监控哪些 PID：

```bash
sudo ./mem_analyze --watch 30 --interval 1 3700 3976 5416 -o firefox_selected.md
```

含义：

| 参数 | 含义 |
| --- | --- |
| `--watch 30` | 监控 30 秒 |
| `--interval 1` | 每 1 秒采样一次 |
| `3700 3976 5416` | 要监控的 PID 列表 |

## 5. 监控报告内容

监控模式生成的 Markdown 报告包含：

1. 监控目标、时长、采样间隔、页大小。
2. 每个进程的 PID、进程名、命令行。
3. 每个进程的 Mermaid 折线图。
4. 每个进程的采样数据表。

默认图表包含两组：

| 图表 | 字段 |
| --- | --- |
| 驻留内存相关 | `RSS`、`PSS`、`Present` |
| 虚拟空间相关 | `Size`、`NotPresent`、`Swap` |

图中单位都是 KiB。

如果 Markdown 查看器支持 Mermaid，可以直接看到折线图。常见选择：

- VS Code + Mermaid 插件
- Typora
- Obsidian
- 支持 Mermaid 的 Markdown 预览器

如果查看器不支持 Mermaid，仍然可以看报告中的采样数据表。

## 6. 数据来源

`mem_analyze` 会直接读取 Linux `/proc` 伪文件，而不是调用 `ps`、`pmap` 等外部命令获取内存信息。

读取流程：

```text
1. /proc/<pid>/maps
   -> 建立 VMA 列表
   -> 获取 address、perms、offset、dev、inode、pathname

2. /proc/<pid>/smaps
   -> 按 VMA 地址匹配
   -> 补充 Size、Rss、Pss、Swap、Referenced 等字段

3. /proc/<pid>/pagemap
   -> 按页读取 64-bit pagemap entry
   -> 统计 present、swapped、not_present、PFN 等页级状态

4. /proc/<pid>/comm
   -> 获取进程名

5. /proc/<pid>/cmdline
   -> 监控模式中获取完整命令行

6. /proc/<pid>/exe
   -> 获取可执行文件路径，用于辅助识别 text/data/bss
```

## 7. maps、smaps、pagemap 的区别

| 来源 | 作用 | 典型字段 |
| --- | --- | --- |
| `maps` | 描述虚拟地址空间布局 | address、perms、offset、dev、inode、pathname |
| `smaps` | 描述每个 VMA 的内存统计 | Size、Rss、Pss、Swap、Referenced、Private/Shared |
| `pagemap` | 描述每个虚拟页的页级状态 | present、swapped、PFN、soft_dirty、exclusive |

简单理解：

```text
maps    告诉你：这个进程有哪些虚拟内存区域。
smaps   告诉你：每个区域占用了多少虚拟空间、多少 RSS、多少 PSS、多少 Swap。
pagemap 告诉你：每个虚拟页当前是否真的有物理页。
```

## 8. 报告中的核心字段

| 字段 | 含义 |
| --- | --- |
| `Size` | VMA 虚拟地址空间大小，不等于真实物理内存占用 |
| `Rss` | Resident Set Size，当前实际驻留在物理内存中的大小 |
| `Pss` | Proportional Set Size，共享页按共享进程数均摊后的大小 |
| `Swap` | 已经换出到 swap 的大小 |
| `Referenced` | 最近被访问过的驻留页大小 |
| `Present` | pagemap 统计出的真实驻留页大小 |
| `NotPresent` | 虚拟地址存在，但当前没有真实物理页的大小 |
| `PFN` | 物理页帧号，需要 root/CAP_SYS_ADMIN 才通常可见 |

`Size` 和 `Present/Rss` 的区别很重要：

```text
Size    = 申请或映射出来的虚拟地址空间大小
Present = 当前真的有物理页驻留的大小
Rss     = 内核在 smaps 中统计的驻留大小
```

例如只执行 `malloc(1GB)` 但不写入，`Size` 可能增加很多，但 `Present/Rss` 不一定同步增加。

## 9. 分段识别

工具会把 VMA 分类为：

| 分段 | 含义 |
| --- | --- |
| `text/代码段` | 主程序中可执行的映射，通常是代码 |
| `data/已初始化数据段` | 主程序中可写的文件私有映射，通常是已初始化全局/静态变量 |
| `bss/未初始化数据段` | 未初始化全局/静态变量，对应运行时清零区域 |
| `heap/堆` | `[heap]`，常由 `brk/malloc` 使用 |
| `stack/栈` | `[stack]` 或 `[stack:<tid>]` |
| `file/文件映射` | 共享库、普通文件 mmap、动态链接器、locale 等 |
| `anon/匿名映射` | 无文件路径、inode 为 0 的匿名内存 |
| `special/内核特殊映射` | `[vdso]`、`[vvar]`、`[vsyscall]` 等 |

注意：`bss` 不一定能被完全拆分。因为 `/proc/<pid>/maps` 是按 VMA/页粒度展示的，如果 `data` 的末尾和 `bss` 的开头落在同一个 4 KiB 页里，`maps` 无法把同一页再拆成前半页 data、后半页 bss。

## 10. Firefox 分析建议

Ubuntu 中 Firefox 通常是多进程结构。可以先查看：

```bash
pgrep -a firefox
```

或在 Firefox 地址栏打开：

```text
about:processes
```

常见 Firefox 进程类型：

| 类型 | 含义 |
| --- | --- |
| 主进程 | 浏览器主窗口、进程管理、标签页管理 |
| tab/content | 网页内容进程，包含 HTML、CSS、JS、DOM 等 |
| rdd | 媒体解码相关进程 |
| socket | 网络/socket 相关进程 |
| utility | 辅助服务进程 |
| crashhelper | 崩溃报告辅助进程 |

要监控所有 Firefox 进程：

```bash
sudo ./mem_analyze --watch-app firefox --duration 60 --interval 2 -o firefox_watch.md
```

要只分析一个具体 tab 进程：

```bash
sudo ./mem_analyze <tab_pid> -o firefox_tab_<tab_pid>.md
```

## 11. malloc_stress 测试程序

`malloc_stress` 是一个交互式测试进程，用来观察虚拟地址空间和物理页分配的变化。

运行：

```bash
cd /mnt/d/lzx/Linux
./malloc_stress
```

启动后会显示自己的 PID。

支持命令：

| 命令 | 作用 |
| --- | --- |
| `status` | 显示当前 malloc 块数量、总大小、PID |
| `alloc <MB> [count]` | 分配 count 个块，每块 MB MiB，只 malloc 不写入 |
| `touch [index|all]` | 写入每一页，触发真实物理页分配 |
| `free <index|all>` | 释放一个块或全部块 |
| `pause` | 保持运行，方便另开终端分析 |
| `quit` | 退出 |

推荐实验：

```text
1. ./malloc_stress
2. 记录 PID
3. sudo ./mem_analyze <PID> -o before.md
4. 在 malloc_stress 中输入：alloc 64 4
5. sudo ./mem_analyze <PID> -o after_alloc.md
6. 在 malloc_stress 中输入：touch all
7. sudo ./mem_analyze <PID> -o after_touch.md
8. 对比 before.md、after_alloc.md、after_touch.md
```

预期现象：

```text
alloc 后：Size 增加明显，Present/Rss 不一定明显增加。
touch 后：Present/Rss 增加明显。
free 后：对应匿名映射和驻留页可能下降。
```

## 12. 注意事项

1. 需要在 Linux/WSL/Ubuntu 中运行。
2. 不能直接分析 Windows 原生进程。
3. 建议使用 `sudo`，否则 PFN 可能不可见。
4. `maps/smaps/pagemap` 不是原子快照，运行中的进程可能在采样时变化。
5. Firefox、Chrome 等浏览器是多进程架构，一个 tab 不一定严格对应一个 PID，一个 PID 也可能承载多个页面或 iframe。
6. Mermaid 图表需要 Markdown 查看器支持 Mermaid；不支持时仍可查看表格数据。

