# 进程内存映射分析报告

| 项目 | 值 |
| --- | --- |
| PID | `349` |
| 进程名 | `malloc_stress` |
| 可执行文件 | `/mnt/d/lzx/linux/malloc_stress` |
| 页大小 | `4096 bytes` |
| pagemap 状态 | pagemap 已读取。注意：非 root/CAP_SYS_ADMIN 环境下 PFN 可能被内核置 0。 |

> 采样说明：`maps`、`smaps`、`pagemap` 不是原子快照，进程运行中变化会造成少量误差。

## 进程总览

| 指标 | 值 |
| --- | ---: |
| VMA 数量 | 22 |
| 虚拟地址空间 Size | 2680 KiB |
| smaps Rss | 1524 KiB |
| smaps Pss | 227 KiB |
| smaps Swap | 0 KiB |
| pagemap 虚拟页 | 670 |
| pagemap present 页 | 381 页 / 1524 KiB |
| pagemap swap 页 | 0 |
| pagemap 未驻留页 | 289 |

## 分段汇总

| 分段 | Size(KiB) | Rss(KiB) | Present(KiB) | NotPresent(KiB) | Present% |
| --- | ---: | ---: | ---: | ---: | ---: |
| text/代码段 | 4 | 4 | 4 | 0 | 100.00% |
| data/已初始化数据段 | 4 | 4 | 4 | 0 | 100.00% |
| heap/堆 | 132 | 4 | 4 | 128 | 3.03% |
| stack/栈 | 132 | 12 | 12 | 120 | 9.09% |
| file/文件映射 | 2312 | 1464 | 1464 | 848 | 63.32% |
| anon/匿名映射 | 72 | 32 | 32 | 40 | 44.44% |
| special/内核特殊映射 | 24 | 4 | 4 | 20 | 16.67% |

## 重点分段字段

下面只列出图中关心的 `text`、`data`、`bss`、`heap`、`file`、`stack`。`Present(KiB)` 是真正驻留在物理内存中的页大小。

### file/文件映射

- 地址范围：`5c65107d7000-5c65107d8000`
- 权限：`r--p`
- 路径：`/mnt/d/lzx/linux/malloc_stress`
- maps：`offset=0x0`, `dev=00:45`, `inode=2814749768314407`
- smaps：`Size=4 KiB`, `Rss=4 KiB`, `Pss=4 KiB`, `Referenced=4 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=1页`, `present=1页(4 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=1页`, `exclusive=1页`, `file_or_shared=1页`
- PFN：`min=1388290`, `max=1388290`, `连续区段数=1`

### text/代码段

- 地址范围：`5c65107d8000-5c65107d9000`
- 权限：`r-xp`
- 路径：`/mnt/d/lzx/linux/malloc_stress`
- maps：`offset=0x1000`, `dev=00:45`, `inode=2814749768314407`
- smaps：`Size=4 KiB`, `Rss=4 KiB`, `Pss=4 KiB`, `Referenced=4 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=1页`, `present=1页(4 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=1页`, `exclusive=1页`, `file_or_shared=1页`
- PFN：`min=1105257`, `max=1105257`, `连续区段数=1`

### file/文件映射

- 地址范围：`5c65107d9000-5c65107da000`
- 权限：`r--p`
- 路径：`/mnt/d/lzx/linux/malloc_stress`
- maps：`offset=0x2000`, `dev=00:45`, `inode=2814749768314407`
- smaps：`Size=4 KiB`, `Rss=4 KiB`, `Pss=4 KiB`, `Referenced=4 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=1页`, `present=1页(4 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=1页`, `exclusive=1页`, `file_or_shared=1页`
- PFN：`min=1101050`, `max=1101050`, `连续区段数=1`

### file/文件映射

- 地址范围：`5c65107da000-5c65107db000`
- 权限：`r--p`
- 路径：`/mnt/d/lzx/linux/malloc_stress`
- maps：`offset=0x2000`, `dev=00:45`, `inode=2814749768314407`
- smaps：`Size=4 KiB`, `Rss=4 KiB`, `Pss=4 KiB`, `Referenced=4 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=1页`, `present=1页(4 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=1页`, `exclusive=1页`, `file_or_shared=0页`
- PFN：`min=1262226`, `max=1262226`, `连续区段数=1`

### data/已初始化数据段

- 地址范围：`5c65107db000-5c65107dc000`
- 权限：`rw-p`
- 路径：`/mnt/d/lzx/linux/malloc_stress`
- maps：`offset=0x3000`, `dev=00:45`, `inode=2814749768314407`
- smaps：`Size=4 KiB`, `Rss=4 KiB`, `Pss=4 KiB`, `Referenced=4 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=1页`, `present=1页(4 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=1页`, `exclusive=1页`, `file_or_shared=0页`
- PFN：`min=1262267`, `max=1262267`, `连续区段数=1`

### heap/堆

- 地址范围：`5c652ef04000-5c652ef25000`
- 权限：`rw-p`
- 路径：`[heap]`
- maps：`offset=0x0`, `dev=00:00`, `inode=0`
- smaps：`Size=132 KiB`, `Rss=4 KiB`, `Pss=4 KiB`, `Referenced=4 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=33页`, `present=1页(4 KiB)`, `not_present=32页(128 KiB)`, `swapped=0页`, `soft_dirty=33页`, `exclusive=1页`, `file_or_shared=0页`
- PFN：`min=1207588`, `max=1207588`, `连续区段数=1`

### file/文件映射

- 地址范围：`70fa12200000-70fa12228000`
- 权限：`r--p`
- 路径：`/usr/lib/x86_64-linux-gnu/libc.so.6`
- maps：`offset=0x0`, `dev=08:30`, `inode=12801`
- smaps：`Size=160 KiB`, `Rss=156 KiB`, `Pss=15 KiB`, `Referenced=156 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=40页`, `present=39页(156 KiB)`, `not_present=1页(4 KiB)`, `swapped=0页`, `soft_dirty=40页`, `exclusive=0页`, `file_or_shared=39页`
- PFN：`min=1358854`, `max=1419128`, `连续区段数=37`

### file/文件映射

- 地址范围：`70fa12228000-70fa123b0000`
- 权限：`r-xp`
- 路径：`/usr/lib/x86_64-linux-gnu/libc.so.6`
- maps：`offset=0x28000`, `dev=08:30`, `inode=12801`
- smaps：`Size=1568 KiB`, `Rss=976 KiB`, `Pss=82 KiB`, `Referenced=976 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=392页`, `present=244页(976 KiB)`, `not_present=148页(592 KiB)`, `swapped=0页`, `soft_dirty=392页`, `exclusive=0页`, `file_or_shared=244页`
- PFN：`min=1355924`, `max=4120740`, `连续区段数=38`

### file/文件映射

- 地址范围：`70fa123b0000-70fa123ff000`
- 权限：`r--p`
- 路径：`/usr/lib/x86_64-linux-gnu/libc.so.6`
- maps：`offset=0x1b0000`, `dev=08:30`, `inode=12801`
- smaps：`Size=316 KiB`, `Rss=64 KiB`, `Pss=4 KiB`, `Referenced=64 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=79页`, `present=16页(64 KiB)`, `not_present=63页(252 KiB)`, `swapped=0页`, `soft_dirty=79页`, `exclusive=0页`, `file_or_shared=16页`
- PFN：`min=2545866`, `max=2545881`, `连续区段数=1`

### file/文件映射

- 地址范围：`70fa123ff000-70fa12403000`
- 权限：`r--p`
- 路径：`/usr/lib/x86_64-linux-gnu/libc.so.6`
- maps：`offset=0x1fe000`, `dev=08:30`, `inode=12801`
- smaps：`Size=16 KiB`, `Rss=16 KiB`, `Pss=16 KiB`, `Referenced=16 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=4页`, `present=4页(16 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=4页`, `exclusive=4页`, `file_or_shared=0页`
- PFN：`min=1262105`, `max=1262270`, `连续区段数=4`

### file/文件映射

- 地址范围：`70fa12403000-70fa12405000`
- 权限：`rw-p`
- 路径：`/usr/lib/x86_64-linux-gnu/libc.so.6`
- maps：`offset=0x202000`, `dev=08:30`, `inode=12801`
- smaps：`Size=8 KiB`, `Rss=8 KiB`, `Pss=8 KiB`, `Referenced=8 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=2页`, `present=2页(8 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=2页`, `exclusive=2页`, `file_or_shared=0页`
- PFN：`min=1262102`, `max=1262271`, `连续区段数=2`

### file/文件映射

- 地址范围：`70fa12467000-70fa12468000`
- 权限：`r--p`
- 路径：`/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2`
- maps：`offset=0x0`, `dev=08:30`, `inode=12598`
- smaps：`Size=4 KiB`, `Rss=4 KiB`, `Pss=0 KiB`, `Referenced=4 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=1页`, `present=1页(4 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=1页`, `exclusive=0页`, `file_or_shared=1页`
- PFN：`min=1355966`, `max=1355966`, `连续区段数=1`

### file/文件映射

- 地址范围：`70fa12468000-70fa12493000`
- 权限：`r-xp`
- 路径：`/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2`
- maps：`offset=0x1000`, `dev=08:30`, `inode=12598`
- smaps：`Size=172 KiB`, `Rss=172 KiB`, `Pss=15 KiB`, `Referenced=172 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=43页`, `present=43页(172 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=43页`, `exclusive=0页`, `file_or_shared=43页`
- PFN：`min=1383436`, `max=1415620`, `连续区段数=37`

### file/文件映射

- 地址范围：`70fa12493000-70fa1249d000`
- 权限：`r--p`
- 路径：`/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2`
- maps：`offset=0x2c000`, `dev=08:30`, `inode=12598`
- smaps：`Size=40 KiB`, `Rss=40 KiB`, `Pss=3 KiB`, `Referenced=40 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=10页`, `present=10页(40 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=10页`, `exclusive=0页`, `file_or_shared=10页`
- PFN：`min=1415400`, `max=1416125`, `连续区段数=10`

### file/文件映射

- 地址范围：`70fa1249d000-70fa1249f000`
- 权限：`r--p`
- 路径：`/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2`
- maps：`offset=0x36000`, `dev=08:30`, `inode=12598`
- smaps：`Size=8 KiB`, `Rss=8 KiB`, `Pss=8 KiB`, `Referenced=8 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=2页`, `present=2页(8 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=2页`, `exclusive=2页`, `file_or_shared=0页`
- PFN：`min=1262223`, `max=1386819`, `连续区段数=2`

### file/文件映射

- 地址范围：`70fa1249f000-70fa124a1000`
- 权限：`rw-p`
- 路径：`/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2`
- maps：`offset=0x38000`, `dev=08:30`, `inode=12598`
- smaps：`Size=8 KiB`, `Rss=8 KiB`, `Pss=8 KiB`, `Referenced=8 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=2页`, `present=2页(8 KiB)`, `not_present=0页(0 KiB)`, `swapped=0页`, `soft_dirty=2页`, `exclusive=2页`, `file_or_shared=0页`
- PFN：`min=1262255`, `max=1470576`, `连续区段数=2`

### stack/栈

- 地址范围：`7ffe1f791000-7ffe1f7b2000`
- 权限：`rw-p`
- 路径：`[stack]`
- maps：`offset=0x0`, `dev=00:00`, `inode=0`
- smaps：`Size=132 KiB`, `Rss=12 KiB`, `Pss=12 KiB`, `Referenced=12 KiB`, `Swap=0 KiB`, `SwapPss=0 KiB`
- pagemap：`virtual=33页`, `present=3页(12 KiB)`, `not_present=30页(120 KiB)`, `swapped=0页`, `soft_dirty=3页`, `exclusive=3页`, `file_or_shared=0页`
- PFN：`min=1262222`, `max=1470642`, `连续区段数=3`

## VMA 明细

| 地址范围 | 分段 | 权限 | Size(KiB) | Rss(KiB) | Pss(KiB) | Swap(KiB) | Present(KiB) | NotPresent(KiB) | 路径 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `5c65107d7000-5c65107d8000` | file/文件映射 | `r--p` | 4 | 4 | 4 | 0 | 4 | 0 | `/mnt/d/lzx/linux/malloc_stress` |
| `5c65107d8000-5c65107d9000` | text/代码段 | `r-xp` | 4 | 4 | 4 | 0 | 4 | 0 | `/mnt/d/lzx/linux/malloc_stress` |
| `5c65107d9000-5c65107da000` | file/文件映射 | `r--p` | 4 | 4 | 4 | 0 | 4 | 0 | `/mnt/d/lzx/linux/malloc_stress` |
| `5c65107da000-5c65107db000` | file/文件映射 | `r--p` | 4 | 4 | 4 | 0 | 4 | 0 | `/mnt/d/lzx/linux/malloc_stress` |
| `5c65107db000-5c65107dc000` | data/已初始化数据段 | `rw-p` | 4 | 4 | 4 | 0 | 4 | 0 | `/mnt/d/lzx/linux/malloc_stress` |
| `5c652ef04000-5c652ef25000` | heap/堆 | `rw-p` | 132 | 4 | 4 | 0 | 4 | 128 | `[heap]` |
| `70fa12200000-70fa12228000` | file/文件映射 | `r--p` | 160 | 156 | 15 | 0 | 156 | 4 | `/usr/lib/x86_64-linux-gnu/libc.so.6` |
| `70fa12228000-70fa123b0000` | file/文件映射 | `r-xp` | 1568 | 976 | 82 | 0 | 976 | 592 | `/usr/lib/x86_64-linux-gnu/libc.so.6` |
| `70fa123b0000-70fa123ff000` | file/文件映射 | `r--p` | 316 | 64 | 4 | 0 | 64 | 252 | `/usr/lib/x86_64-linux-gnu/libc.so.6` |
| `70fa123ff000-70fa12403000` | file/文件映射 | `r--p` | 16 | 16 | 16 | 0 | 16 | 0 | `/usr/lib/x86_64-linux-gnu/libc.so.6` |
| `70fa12403000-70fa12405000` | file/文件映射 | `rw-p` | 8 | 8 | 8 | 0 | 8 | 0 | `/usr/lib/x86_64-linux-gnu/libc.so.6` |
| `70fa12405000-70fa12412000` | anon/匿名映射 | `rw-p` | 52 | 20 | 20 | 0 | 20 | 32 | `(anonymous)` |
| `70fa1245d000-70fa12460000` | anon/匿名映射 | `rw-p` | 12 | 8 | 8 | 0 | 8 | 4 | `(anonymous)` |
| `70fa12465000-70fa12467000` | anon/匿名映射 | `rw-p` | 8 | 4 | 4 | 0 | 4 | 4 | `(anonymous)` |
| `70fa12467000-70fa12468000` | file/文件映射 | `r--p` | 4 | 4 | 0 | 0 | 4 | 0 | `/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2` |
| `70fa12468000-70fa12493000` | file/文件映射 | `r-xp` | 172 | 172 | 15 | 0 | 172 | 0 | `/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2` |
| `70fa12493000-70fa1249d000` | file/文件映射 | `r--p` | 40 | 40 | 3 | 0 | 40 | 0 | `/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2` |
| `70fa1249d000-70fa1249f000` | file/文件映射 | `r--p` | 8 | 8 | 8 | 0 | 8 | 0 | `/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2` |
| `70fa1249f000-70fa124a1000` | file/文件映射 | `rw-p` | 8 | 8 | 8 | 0 | 8 | 0 | `/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2` |
| `7ffe1f791000-7ffe1f7b2000` | stack/栈 | `rw-p` | 132 | 12 | 12 | 0 | 12 | 120 | `[stack]` |
| `7ffe1f7cd000-7ffe1f7d1000` | special/内核特殊映射 | `r--p` | 16 | 0 | 0 | 0 | 0 | 16 | `[vvar]` |
| `7ffe1f7d1000-7ffe1f7d3000` | special/内核特殊映射 | `r-xp` | 8 | 4 | 0 | 0 | 4 | 4 | `[vdso]` |

## 字段含义

| 字段 | 含义 |
| --- | --- |
| `maps.address` | VMA 的虚拟地址范围，左闭右开。 |
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
| `pagemap.PFN` | 物理页帧号；现代 Linux 通常要求 `root/CAP_SYS_ADMIN` 才能看到真实 PFN。 |

## 分段识别说明

| 分段 | 识别方式 |
| --- | --- |
| `text/代码段` | 主可执行文件中带 `x` 权限的映射。 |
| `data/已初始化数据段` | 主可执行文件中可写的文件私有映射，通常保存已初始化全局变量/静态变量。 |
| `bss/未初始化数据段` | 主程序 `data` 后紧邻的匿名私有可写映射，或 ELF 中 `filesz < memsz` 的零填充尾部；如果 `bss` 与 `data` 共享同一页，`maps` 不一定能单独拆出。 |
| `heap/堆` | `pathname` 为 `[heap]` 的映射，`malloc/brk` 常使用这里；大型 `malloc` 也可能单独出现在匿名映射里。 |
| `file/文件映射` | 共享库、普通文件 `mmap`、locale、动态链接器等文件来源映射。 |
| `stack/栈` | `pathname` 为 `[stack]` 或 `[stack:<tid>]` 的映射。 |
