# 进程内存映射分析报告索引

> 单次分析在 v3 中拆分为主索引和 `details/` 下的详细报告；主文件保留总览、一级 segment 汇总和二级 section 汇总。

## PID 123669 `firefox`

| 项目 | 值 |
| --- | --- |
| 可执行文件 | `/snap/firefox/8504/usr/lib/firefox/firefox` |
| 页大小 | `4096 bytes` |
| pagemap 状态 | pagemap 已读取。注意：非 root/CAP_SYS_ADMIN 环境下 PFN 可能被内核置 0。 |
| 详细报告 | [打开](details/pid_123669_firefox_details/index.md) |

## 总览矩阵

> 列为总进程与一级 segment；行为 `maps`、`smaps`、`pagemap` 指标。`路径/来源` 显示 file/anon/special 来源计数；分段列中的 VMA 数量按逻辑区间统计。

| 来源 | 指标 | 总进程 | heap/堆 | text/代码段 | data/已初始化数据段 | bss/未初始化数据段 | stack/栈 | file/文件映射 | anon/匿名映射 | special/内核特殊映射 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| maps | VMA数量 | 2618 | 1358 | 3 | 2 | 1 | 1 | 1206 | 327 | 3 |
| maps | 地址范围 | `001f72c00000-ffffffffff601000` | `001f72c00000-7942a0d00000` | `5a8459e26000-5a8459e99000` | `5a8459e9b000-5a8459e9d000` | `5a8459e9d000-5a8459e9f000` | `7fffd9e2e000-7fffd9e5d000` | `3cbab7384000-7942a132a000` | `79422ac00000-7fffd9e61000` | `7942a12e8000-ffffffffff601000` |
| maps | 权限 | rwx p/s | rw- p | r-x p | rw- p | rw- p | rw- p | rwx p/s | rwx p | r-x p |
| maps | 路径/来源 | file:2287 anon:328 special:3 | file:1358 anon:0 special:0 | file:3 anon:0 special:0 | file:2 anon:0 special:0 | file:0 anon:1 special:0 | file:1 anon:0 special:0 | file:1206 anon:0 special:0 | file:0 anon:327 special:0 | file:0 anon:0 special:3 |
| maps | 文件 inode | 897 | 0 | 3 | 2 | 0 | 0 | 1175 | 0 | 0 |
| smaps | 虚拟地址空间 Size | 4105440 KiB | 818176 KiB | 460 KiB | 8 KiB | 8 KiB | 188 KiB | 3043220 KiB | 262936 KiB | 28 KiB |
| smaps | RSS | 654600 KiB | 368348 KiB | 460 KiB | 8 KiB | 4 KiB | 188 KiB | 282836 KiB | 4112 KiB | 8 KiB |
| smaps | PSS | 551475 KiB | 368204 KiB | 65 KiB | 8 KiB | 4 KiB | 188 KiB | 178865 KiB | 4104 KiB | 0 KiB |
| smaps | Swap | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB |
| smaps | SwapPSS | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB | 0 KiB |
| smaps | Referenced | 597720 KiB | 315128 KiB | 460 KiB | 8 KiB | 4 KiB | 188 KiB | 277824 KiB | 4104 KiB | 8 KiB |
| pagemap | 虚拟页 | 1031255 | 204544 | 115 | 2 | 2 | 47 | 760805 | 65734 | 6 |
| pagemap | present页 | 163991 / 655964 KiB | 92087 / 368348 KiB | 115 / 460 KiB | 2 / 8 KiB | 1 / 4 KiB | 47 / 188 KiB | 70709 / 282836 KiB | 1028 / 4112 KiB | 2 / 8 KiB |
| pagemap | swap页 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pagemap | 未驻留页 | 867264 | 112457 | 0 | 0 | 1 | 0 | 690096 | 64706 | 4 |
| pagemap | present占比 | 15.90% | 45.02% | 100.00% | 100.00% | 50.00% | 100.00% | 9.29% | 1.56% | 33.33% |
| pagemap | PFN min | 13350 | 13350 | 1104144 | 630775 | 599493 | 63622 | 19312 | 14172 | 1985870 |
| pagemap | PFN max | 2358789 | 2322171 | 2273747 | 630776 | 599493 | 2130496 | 2358789 | 2321528 | 1985871 |
| pagemap | 连续区段数 | 92925 | 56979 | 115 | 2 | 1 | 46 | 34942 | 885 | 1 |

## Section 细分汇总

> 一级分类仍使用 v2 的 segment；二级分类在 ELF 映射中使用 section header 的 `sh_name`，无法匹配 section 的区域显示为对应 segment 的 fallback 名称。

| 一级段 | 二级 section | Size(KiB) | Rss(KiB) | Present(KiB) | NotPresent(KiB) | Present% |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| text/代码段 | `firefox:.text` | 452 | 452 | 452 | 0 | 100.00% |
| text/代码段 | `firefox:.plt` | 8 | 8 | 8 | 0 | 100.00% |
| data/已初始化数据段 | `firefox:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| data/已初始化数据段 | `firefox:.data` | 4 | 4 | 4 | 0 | 100.00% |
| bss/未初始化数据段 | `bss/未初始化数据段` | 8 | 4 | 4 | 4 | 50.00% |
| heap/堆 | `heap` | 818176 | 368348 | 368348 | 449828 | 45.02% |
| stack/栈 | `stack` | 188 | 188 | 188 | 0 | 100.00% |
| file/文件映射 | `file` | 2849660 | 174424 | 174424 | 2675236 | 6.12% |
| file/文件映射 | `libxul.so:.text` | 114496 | 79500 | 79500 | 34996 | 69.43% |
| file/文件映射 | `libxul.so:.rodata` | 37212 | 13512 | 13512 | 23700 | 36.31% |
| file/文件映射 | `libxul.so:.eh_frame` | 14412 | 0 | 0 | 14412 | 0.00% |
| file/文件映射 | `libgkcodecs.so:.text` | 6428 | 72 | 72 | 6356 | 1.12% |
| file/文件映射 | `libxul.so:.data.rel.ro` | 5820 | 5820 | 5820 | 0 | 100.00% |
| file/文件映射 | `libxul.so:.eh_frame_hdr` | 2348 | 20 | 20 | 2328 | 0.85% |
| file/文件映射 | `libc.so.6:.text` | 1612 | 1612 | 1612 | 0 | 100.00% |
| file/文件映射 | `libgkcodecs.so:.rodata` | 1316 | 44 | 44 | 1272 | 3.34% |
| file/文件映射 | `libmozsqlite3.so:.text` | 1228 | 1056 | 1056 | 172 | 85.99% |
| file/文件映射 | `libfreeblpriv3.so:.text` | 944 | 880 | 880 | 64 | 93.22% |
| file/文件映射 | `libxul.so:.data` | 916 | 916 | 916 | 0 | 100.00% |
| file/文件映射 | `libm.so.6:.text` | 496 | 392 | 392 | 104 | 79.03% |
| file/文件映射 | `libnss3.so:.text` | 448 | 448 | 448 | 0 | 100.00% |
| file/文件映射 | `libgkcodecs.so:.eh_frame` | 364 | 0 | 0 | 364 | 0.00% |
| file/文件映射 | `libm.so.6:.rodata` | 312 | 284 | 284 | 28 | 91.03% |
| file/文件映射 | `libopus.so.0.9.0:.text` | 296 | 64 | 64 | 232 | 21.62% |
| file/文件映射 | `libssl3.so:.text` | 264 | 264 | 264 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.text` | 236 | 236 | 236 | 0 | 100.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.text` | 196 | 64 | 64 | 132 | 32.65% |
| file/文件映射 | `ld-linux-x86-64.so.2:.text` | 168 | 168 | 168 | 0 | 100.00% |
| file/文件映射 | `libgkcodecs.so:.data.rel.ro` | 160 | 160 | 160 | 0 | 100.00% |
| file/文件映射 | `libc.so.6:.rodata` | 156 | 108 | 108 | 48 | 69.23% |
| file/文件映射 | `libmozsandbox.so:.text` | 124 | 124 | 124 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.text` | 124 | 124 | 124 | 0 | 100.00% |
| file/文件映射 | `libxul.so:.got` | 124 | 124 | 124 | 0 | 100.00% |
| file/文件映射 | `libfreeblpriv3.so:.rodata` | 116 | 116 | 116 | 0 | 100.00% |
| file/文件映射 | `liblgpllibs.so:.text` | 116 | 104 | 104 | 12 | 89.66% |
| file/文件映射 | `libmozsqlite3.so:.eh_frame` | 112 | 0 | 0 | 112 | 0.00% |
| file/文件映射 | `libxul.so:.relr.dyn` | 112 | 4 | 4 | 108 | 3.57% |
| file/文件映射 | `libc.so.6:.eh_frame` | 104 | 24 | 24 | 80 | 23.08% |
| file/文件映射 | `libgcc_s.so.1:.text` | 92 | 68 | 68 | 24 | 73.91% |
| file/文件映射 | `libsmime3.so:.text` | 92 | 92 | 92 | 0 | 100.00% |
| file/文件映射 | `libmozsqlite3.so:.rodata` | 88 | 84 | 84 | 4 | 95.45% |
| file/文件映射 | `libnss3.so:.eh_frame` | 80 | 0 | 0 | 80 | 0.00% |
| file/文件映射 | `libnss3.so:.rodata` | 80 | 80 | 80 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.text` | 80 | 80 | 80 | 0 | 100.00% |
| file/文件映射 | `libc.so.6:.dynsym` | 68 | 68 | 68 | 0 | 100.00% |
| file/文件映射 | `libxul.so:.dynstr` | 68 | 68 | 68 | 0 | 100.00% |
| file/文件映射 | `libxul.so:.dynsym` | 68 | 68 | 68 | 0 | 100.00% |
| file/文件映射 | `firefox:.eh_frame` | 60 | 36 | 36 | 24 | 60.00% |
| file/文件映射 | `libxul.so:.rela.plt` | 60 | 60 | 60 | 0 | 100.00% |
| file/文件映射 | `libgkcodecs.so:.eh_frame_hdr` | 56 | 0 | 0 | 56 | 0.00% |
| file/文件映射 | `libopus.so.0.9.0:.rodata` | 52 | 0 | 0 | 52 | 0.00% |
| file/文件映射 | `libfreeblpriv3.so:.eh_frame` | 48 | 40 | 40 | 8 | 83.33% |
| file/文件映射 | `libmp3lame.so.0.0.0:.rodata` | 48 | 0 | 0 | 48 | 0.00% |
| file/文件映射 | `libsoftokn3.so:.eh_frame` | 48 | 0 | 0 | 48 | 0.00% |
| file/文件映射 | `libsoftokn3.so:.rodata` | 44 | 44 | 44 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.eh_frame` | 44 | 0 | 0 | 44 | 0.00% |
| file/文件映射 | `libxul.so:.plt` | 44 | 44 | 44 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.rodata` | 36 | 36 | 36 | 0 | 100.00% |
| file/文件映射 | `firefox:.rodata` | 32 | 32 | 32 | 0 | 100.00% |
| file/文件映射 | `libc.so.6:.dynstr` | 32 | 32 | 32 | 0 | 100.00% |
| file/文件映射 | `libc.so.6:.rela.dyn` | 32 | 32 | 32 | 0 | 100.00% |
| file/文件映射 | `libm.so.6:.eh_frame` | 32 | 0 | 0 | 32 | 0.00% |
| file/文件映射 | `libnssutil3.so:.rodata` | 32 | 32 | 32 | 0 | 100.00% |
| file/文件映射 | `ld-linux-x86-64.so.2:.rodata` | 28 | 28 | 28 | 0 | 100.00% |
| file/文件映射 | `libc.so.6:.eh_frame_hdr` | 28 | 0 | 0 | 28 | 0.00% |
| file/文件映射 | `libm.so.6:.dynsym` | 28 | 28 | 28 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.dynstr` | 28 | 28 | 28 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.dynsym` | 28 | 28 | 28 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.data.rel.ro` | 28 | 28 | 28 | 0 | 100.00% |
| file/文件映射 | `firefox:.dynstr` | 24 | 24 | 24 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.eh_frame` | 24 | 16 | 16 | 8 | 66.67% |
| file/文件映射 | `libc.so.6:.gnu.hash` | 20 | 16 | 16 | 4 | 80.00% |
| file/文件映射 | `libmozsandbox.so:.eh_frame` | 20 | 20 | 20 | 0 | 100.00% |
| file/文件映射 | `libmozsqlite3.so:.data` | 20 | 20 | 20 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.data.rel.ro` | 20 | 20 | 20 | 0 | 100.00% |
| file/文件映射 | `libpciaccess.so.0.11.1:.text` | 20 | 20 | 20 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.eh_frame` | 20 | 12 | 12 | 8 | 60.00% |
| file/文件映射 | `libxul.so:.got.plt` | 20 | 20 | 20 | 0 | 100.00% |
| file/文件映射 | `libxul.so:.rela.dyn` | 20 | 4 | 4 | 16 | 20.00% |
| file/文件映射 | `firefox:.dynsym` | 16 | 16 | 16 | 0 | 100.00% |
| file/文件映射 | `libgkcodecs.so:.data` | 16 | 12 | 12 | 4 | 75.00% |
| file/文件映射 | `liblgpllibs.so:.rodata` | 16 | 16 | 16 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.data.rel.ro` | 16 | 16 | 16 | 0 | 100.00% |
| file/文件映射 | `ld-linux-x86-64.so.2:.eh_frame` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libgcc_s.so.1:.eh_frame` | 12 | 0 | 0 | 12 | 0.00% |
| file/文件映射 | `libgkcodecs.so:.got` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `liblgpllibs.so:.eh_frame` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libm.so.6:.gnu.hash` | 12 | 8 | 8 | 4 | 66.67% |
| file/文件映射 | `libm.so.6:.hash` | 12 | 0 | 0 | 12 | 0.00% |
| file/文件映射 | `libmozsandbox.so:.dynstr` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libmozsqlite3.so:.data.rel.ro` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libmozsqlite3.so:.eh_frame_hdr` | 12 | 0 | 0 | 12 | 0.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.eh_frame` | 12 | 0 | 0 | 12 | 0.00% |
| file/文件映射 | `libnspr4.so:.dynsym` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.rodata` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.eh_frame_hdr` | 12 | 0 | 0 | 12 | 0.00% |
| file/文件映射 | `libnss3.so:.rela.plt` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.eh_frame` | 12 | 4 | 4 | 8 | 33.33% |
| file/文件映射 | `libopus.so.0.9.0:.eh_frame` | 12 | 0 | 0 | 12 | 0.00% |
| file/文件映射 | `libplc4.so:.text` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.data.rel.ro` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.dynstr` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.dynsym` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.dynstr` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.dynsym` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `libxul.so:.gcc_except_table` | 12 | 12 | 12 | 0 | 100.00% |
| file/文件映射 | `firefox:.eh_frame_hdr` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `ld-linux-x86-64.so.2:.data.rel.ro` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libc.so.6:.gnu.version` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libc.so.6:__libc_freeres_fn` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libfreeblpriv3.so:.data.rel.ro` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libfreeblpriv3.so:.eh_frame_hdr` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libgcc_s.so.1:.dynsym` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libgkcodecs.so:.dynsym` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `liblgpllibs.so:.data.rel.ro` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libm.so.6:.dynstr` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libm.so.6:.eh_frame_hdr` | 8 | 0 | 0 | 8 | 0.00% |
| file/文件映射 | `libmozsandbox.so:.dynsym` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libmozsandbox.so:.rodata` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libmozsqlite3.so:.dynsym` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libmozsqlite3.so:.rela.dyn` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.dynstr` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.rela.dyn` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.dynstr` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.rela.plt` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.gnu.hash` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.plt` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libnss_mdns4_minimal.so.2:.text` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.dynstr` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.dynsym` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libpciaccess.so.0.11.1:.eh_frame` | 8 | 0 | 0 | 8 | 0.00% |
| file/文件映射 | `libplds4.so:.text` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.eh_frame_hdr` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.eh_frame_hdr` | 8 | 0 | 0 | 8 | 0.00% |
| file/文件映射 | `libssl3.so:.plt` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `libxul.so:protodesc_cold` | 8 | 8 | 8 | 0 | 100.00% |
| file/文件映射 | `firefox:.data.rel.ro` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `firefox:.gnu.hash` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `firefox:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `firefox:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `ld-linux-x86-64.so.2:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `ld-linux-x86-64.so.2:.eh_frame_hdr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `ld-linux-x86-64.so.2:.rela.dyn` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libfreeblpriv3.so:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libgcc_s.so.1:.dynamic` | 4 | 0 | 0 | 4 | 0.00% |
| file/文件映射 | `libgcc_s.so.1:.got.plt` | 4 | 0 | 0 | 4 | 0.00% |
| file/文件映射 | `libgcc_s.so.1:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libgcc_s.so.1:.rodata` | 4 | 0 | 0 | 4 | 0.00% |
| file/文件映射 | `libgkcodecs.so:.dynstr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libgkcodecs.so:.plt` | 4 | 0 | 0 | 4 | 0.00% |
| file/文件映射 | `libgkcodecs.so:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libgkcodecs.so:.relr.dyn` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `liblgpllibs.so:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `liblgpllibs.so:.dynstr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `liblgpllibs.so:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `liblgpllibs.so:.eh_frame_hdr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `liblgpllibs.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libm.so.6:.dynamic` | 4 | 0 | 0 | 4 | 0.00% |
| file/文件映射 | `libm.so.6:.gnu.version` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libm.so.6:.got.plt` | 4 | 0 | 0 | 4 | 0.00% |
| file/文件映射 | `libm.so.6:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozgtk.so:.data` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozgtk.so:.dynstr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozgtk.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozgtk.so:.text` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozsandbox.so:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozsandbox.so:.data.rel.ro` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozsandbox.so:.eh_frame_hdr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozsandbox.so:.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozsandbox.so:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozsandbox.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozsqlite3.so:.dynstr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozsqlite3.so:.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozwayland.so:.data` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozwayland.so:.dynstr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozwayland.so:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozwayland.so:.eh_frame` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozwayland.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmozwayland.so:.text` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.data.rel.ro` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.dynsym` | 4 | 0 | 0 | 4 | 0.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.eh_frame_hdr` | 4 | 0 | 0 | 4 | 0.00% |
| file/文件映射 | `libmp3lame.so.0.0.0:.gnu.hash` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.data` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.data.rel.ro` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.eh_frame_hdr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.gnu.hash` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.got.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnspr4.so:.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.data` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.gnu.version` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.got.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.rela.dyn` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss3.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss_mdns4_minimal.so.2:.data` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss_mdns4_minimal.so.2:.dynamic` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss_mdns4_minimal.so.2:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnss_mdns4_minimal.so.2:.eh_frame` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.eh_frame_hdr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.gnu.hash` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.got.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libnssutil3.so:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libopus.so.0.9.0:.data.rel.ro` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libopus.so.0.9.0:.dynstr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libopus.so.0.9.0:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libopus.so.0.9.0:.got.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libopus.so.0.9.0:.rela.dyn` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libpciaccess.so.0.11.1:.dynamic` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libpciaccess.so.0.11.1:.dynstr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libpciaccess.so.0.11.1:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libpciaccess.so.0.11.1:.got.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libplc4.so:.data` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libplc4.so:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libplc4.so:.eh_frame` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libplc4.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libplds4.so:.data` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libplds4.so:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libplds4.so:.eh_frame` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libplds4.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.eh_frame_hdr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.rela.dyn` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsmime3.so:.rodata` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.data` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.data.rel.ro` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.dynstr` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.dynsym` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libsoftokn3.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.bss` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.rela.plt` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libssl3.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libxul.so:.gnu.version` | 4 | 4 | 4 | 0 | 100.00% |
| file/文件映射 | `libxul.so:.relro_padding` | 4 | 4 | 4 | 0 | 100.00% |
| anon/匿名映射 | `anon` | 262936 | 4112 | 4112 | 258824 | 1.56% |
| special/内核特殊映射 | `special` | 28 | 8 | 8 | 16 | 33.33% |

