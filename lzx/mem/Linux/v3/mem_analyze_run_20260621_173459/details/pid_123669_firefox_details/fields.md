## 字段含义

| 字段 | 含义 |
| --- | --- |
| `maps.address` | VMA 的虚拟地址范围，左闭右开。 |
| `逻辑地址范围` | 报告内部按 ELF 边界切出的子区间；不会改变 Linux 内核中的原始 VMA。 |
| `原始 VMA` | `/proc/<pid>/maps` 中真实存在的 VMA，同一个原始 VMA 可能对应多条逻辑区间。 |
| `maps.perms` | `r/w/x` 表示读/写/执行；`p` 表示私有 COW 映射；`s` 表示共享映射。 |
| `maps.offset` | 文件映射在文件中的偏移；匿名映射通常为 0。 |
| `maps.dev/inode/pathname` | 映射来源文件的设备号、inode 和路径；`inode=0` 且无路径通常是匿名映射。 |
| `smaps.Size` | 这段 VMA 的虚拟地址空间大小，不等于真实占用内存。 |
| `smaps.Rss` | Resident Set Size，当前实际驻留在物理内存中的大小。 |
| `smaps.Pss` | Proportional Set Size，共享页按共享进程数均摊后的大小。 |
| `smaps.Referenced` | 最近被访问过的驻留页大小。 |
| `smaps.Swap` | 已换出到 swap 的大小。 |
| `smaps.SwapPss` | 共享 swap 页均摊后的大小。 |
| `pagemap.present` | 为 1 表示该虚拟页当前有物理页驻留；`present页 * 页大小` 就是这段真实物理驻留大小。 |
| `pagemap.swapped` | 为 1 表示该虚拟页被换出。 |
| `pagemap.not_present` | `present=0` 且 `swapped=0`，表示虚拟地址保留了，但当前没有真实物理页。 |
| `pagemap_bitmap` | 每个字符对应一个虚拟页：`P=present`、`N=not present`、`S=swapped`、`?=读取失败`。 |
| `pagemap.PFN` | 物理页帧号；现代 Linux 通常要求 `root/CAP_SYS_ADMIN` 才能看到真实 PFN。 |

## 分段识别说明

| 分段 | 识别方式 |
| --- | --- |
| `text/代码段` | 主可执行文件中带 `x` 权限的映射。 |
| `data/已初始化数据段` | 主可执行文件中可写的文件私有映射，通常保存已初始化全局变量/静态变量。 |
| `bss/未初始化数据段` | 主程序 `data` 后紧邻的匿名私有可写映射，或 ELF 中 `filesz < memsz` 的零填充尾部；报告会按 ELF 边界在内部切分逻辑区间。 |
| `heap/堆` | `pathname` 为 `[heap]`，或 `[anon:*]` 名称中包含 `heap`、`jemalloc`、`malloc` 的分配器/运行时堆映射。 |
| `file/文件映射` | 共享库、普通文件 `mmap`、locale、动态链接器等文件来源映射。 |
| `stack/栈` | `pathname` 为 `[stack]` 或 `[stack:<tid>]` 的映射。 |
