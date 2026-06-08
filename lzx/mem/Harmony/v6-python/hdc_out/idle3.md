# Referenced 操作后访问定位报告

| 项目 | 值 |
| --- | --- |
| PID | `29616` |
| 进程名 | `om.douyu.ho.app` |
| 命令行 | `com.douyu.ho.app` |
| 可执行文件 | `/system/bin/appspawn` |
| 采样时间 | `2026-05-31 19:59:05` |
| VMA 数 | `6510` |
| Size | `48585904 KiB` |
| Rss | `629416 KiB` |
| Pss | `464393 KiB` |
| Referenced | `40176 KiB / 10044 页` |
| Swap | `56988 KiB` |

> 使用方法：先清空 `clear_refs`，再执行用户操作，然后立即采样。本报告中的 `Referenced` 表示观察窗口内被访问过的驻留页规模。

## Referenced 段汇总

| 一级段 | VMA 数 | Size(KiB) | Rss(KiB) | Pss(KiB) | Referenced(KiB) | Swap(KiB) | Referenced/Size | Referenced/Rss |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ark ts heap | 335 | 105728 | 100228 | 94377 | 3760 | 88 | 3.56% | 3.75% |
| native heap | 164 | 393656 | 244032 | 234640 | 22672 | 32916 | 5.76% | 9.29% |
| AnonPage other | 11 | 1590028 | 11172 | 11172 | 4 | 8 | 0.00% | 0.04% |
| FilePage other | 1366 | 705148 | 39272 | 31006 | 2896 | 3968 | 0.41% | 7.37% |
| stack | 2 | 8184 | 100 | 100 | 32 | 0 | 0.39% | 32.00% |
| .so | 3749 | 709736 | 188592 | 65599 | 9932 | 14840 | 1.40% | 5.27% |
| .hap | 23 | 178448 | 8348 | 8229 | 64 | 0 | 0.04% | 0.77% |
| .ttf | 6 | 67444 | 10976 | 1838 | 0 | 0 | 0.00% | 0.00% |
| dev | 230 | 41100 | 14140 | 13465 | 76 | 0 | 0.18% | 0.54% |
| GL | 177 | 71716 | 10764 | 3767 | 524 | 5012 | 0.73% | 4.87% |
| Graph | 44 | 5864 | 1772 | 188 | 216 | 132 | 3.68% | 12.19% |
| guard | 403 | 44708852 | 20 | 12 | 0 | 24 | 0.00% | 0.00% |

## Referenced VMA 定位

| VMA | 一级段 | 权限 | Size(KiB) | Rss(KiB) | Pss(KiB) | Referenced(KiB) | Referenced页 | Referenced/Size | 路径 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `005d24388000-005d24b88000` | native heap | `rw-p` | 8192 | 7724 | 7724 | 7212 | 1803 | 88.04% | `[anon:native_heap:jemalloc]` |
| `005d25585000-005d25f85000` | native heap | `rw-p` | 10240 | 6224 | 6224 | 3112 | 778 | 30.39% | `[anon:native_heap:jemalloc]` |
| `005c542f9000-005c54ff9000` | native heap | `rw-p` | 13312 | 9016 | 9016 | 2572 | 643 | 19.32% | `[anon:native_heap:jemalloc]` |
| `005ad3111000-005ad38ba000` | .so | `r-xp` | 7844 | 5052 | 219 | 1628 | 407 | 20.75% | `/system/lib64/platformsdk/libark_jsruntime.so` |
| `005d1c67f000-005d1e27f000` | native heap | `rw-p` | 28672 | 26900 | 26900 | 1504 | 376 | 5.25% | `[anon:native_heap:jemalloc]` |
| `005afa5d2000-005afb5d2000` | native heap | `rw-p` | 16384 | 12960 | 12960 | 1272 | 318 | 7.76% | `[anon:native_heap:jemalloc]` |
| `005d2208a000-005d2408a000` | native heap | `rw-p` | 32768 | 26764 | 26764 | 1268 | 317 | 3.87% | `[anon:native_heap:jemalloc]` |
| `005ae8180000-005ae83d8000` | .so | `r-xp` | 2400 | 1688 | 617 | 1192 | 298 | 49.67% | `/vendor/lib64/passthrough/libhvgr_v210.so` |
| `005ae8849000-005aeb449000` | native heap | `rw-p` | 45056 | 16092 | 12561 | 1128 | 282 | 2.50% | `[anon:native_heap:jemalloc]` |
| `005d2e18a000-005d37761000` | .so | `r-xp` | 153436 | 27324 | 11179 | 1080 | 270 | 0.70% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so` |
| `005afd869000-005afe0dd000` | .so | `r-xp` | 8656 | 3188 | 3188 | 896 | 224 | 10.35% | `/data/storage/el1/bundle/libs/arm64/libdyplayer.so` |
| `005c50052000-005c51452000` | native heap | `rw-p` | 20480 | 19648 | 19648 | 672 | 168 | 3.28% | `[anon:native_heap:jemalloc]` |
| `005a49c01000-005a49e00000` | native heap | `rw-p` | 2044 | 1580 | 1568 | 652 | 163 | 31.90% | `[anon:native_heap:jemalloc meta]` |
| `005a4962c000-005a497a2000` | FilePage other | `r-xp` | 1496 | 1264 | 9 | 584 | 146 | 39.04% | `/system/lib/ld-musl-aarch64.so.1` |
| `005d17436000-005d18c36000` | native heap | `rw-p` | 24576 | 23916 | 23916 | 580 | 145 | 2.36% | `[anon:native_heap:jemalloc]` |
| `005aeeb0b000-005aef92f000` | FilePage other | `r-xp` | 14480 | 1276 | 62 | 516 | 129 | 3.56% | `/system/lib64/module/arkcompiler/stub.an` |
| `005d26d8e000-005d2958e000` | native heap | `rw-p` | 40960 | 39384 | 39384 | 468 | 117 | 1.14% | `[anon:native_heap:jemalloc]` |
| `005aee704000-005aee904000` | native heap | `rw-p` | 2048 | 1888 | 1830 | 428 | 107 | 20.90% | `[anon:native_heap:jemalloc]` |
| `005c521c4000-005c52544000` | native heap | `rw-p` | 3584 | 3052 | 3052 | 344 | 86 | 9.60% | `[anon:native_heap:jemalloc]` |
| `005a4af69000-005a4aff2000` | .so | `r-xp` | 548 | 520 | 4 | 300 | 75 | 54.74% | `/system/lib64/ndk/libffrt.so` |
| `005d18e01000-005d19600000` | native heap | `rw-p` | 8188 | 432 | 432 | 264 | 66 | 3.22% | `[anon:native_heap:jemalloc meta]` |
| `00260cbc0000-00260cc00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 256 | 64 | 100.00% | `[anon:ArkTS Heapsemi space]` |
| `005aee401000-005aee600000` | native heap | `rw-p` | 2044 | 332 | 316 | 216 | 54 | 10.57% | `[anon:native_heap:jemalloc meta]` |
| `005ad0f80000-005ad0fdd000` | .so | `r-xp` | 372 | 332 | 8 | 212 | 53 | 56.99% | `/system/lib64/platformsdk/libace_napi.z.so` |
| `005a4a201000-005a4a600000` | native heap | `rw-p` | 4092 | 636 | 632 | 208 | 52 | 5.08% | `[anon:native_heap:jemalloc meta]` |
| `005d1ec46000-005d1eccf000` | .so | `r-xp` | 548 | 548 | 548 | 208 | 52 | 37.96% | `/data/storage/el1/bundle/libs/arm64/libdanmu.so` |
| `005d29e6a000-005d2ce6a000` | native heap | `rw-p` | 49152 | 33792 | 33792 | 196 | 49 | 0.40% | `[anon:native_heap:jemalloc]` |
| `005d2d240000-005d2e18a000` | .so | `r--p` | 15656 | 7200 | 2079 | 192 | 48 | 1.23% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so` |
| `005acc36f000-005acc3c1000` | GL | `r-xp` | 328 | 208 | 1 | 184 | 46 | 56.10% | `/system/lib64/platformsdk/libipc_single.z.so` |
| `005a4ab10000-005a4abae000` | .so | `r-xp` | 632 | 416 | 4 | 180 | 45 | 28.48% | `/system/lib64/chipset-sdk-sp/libc++.so` |
| `005adb201000-005adb800000` | native heap | `rw-p` | 6140 | 248 | 193 | 176 | 44 | 2.87% | `[anon:native_heap:jemalloc meta]` |
| `00260b440000-00260b540000` | ark ts heap | `rw-p` | 1024 | 964 | 964 | 172 | 43 | 16.80% | `[anon:ArkTS Heap]` |
| `00260dcc0000-00260dd80000` | ark ts heap | `rw-p` | 768 | 768 | 768 | 172 | 43 | 22.40% | `[anon:ArkTS Heap]` |
| `005ae7f80000-005ae7ff4000` | .so | `r--p` | 464 | 264 | 87 | 168 | 42 | 36.21% | `/vendor/lib64/passthrough/libhvgr_v210.so` |
| `003800004000-003800174000` | FilePage other | `rw-p` | 1472 | 468 | 468 | 160 | 40 | 10.87% | `[anon:partition_alloc]` |
| `005afd580000-005afd868000` | .so | `r--p` | 2976 | 1608 | 1608 | 160 | 40 | 5.38% | `/data/storage/el1/bundle/libs/arm64/libdyplayer.so` |
| `005acce14000-005acce41000` | .so | `r-xp` | 180 | 164 | 2 | 148 | 37 | 82.22% | `/system/lib64/chipset-sdk-sp/libeventhandler.z.so` |
| `00260edc0000-00260ee00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 136 | 34 | 53.12% | `[anon:ArkTS Heapsemi space]` |
| `005ace8b3000-005ace905000` | Graph | `r-xp` | 328 | 260 | 12 | 136 | 34 | 41.46% | `/system/lib64/chipset-sdk-sp/libsurface.z.so` |
| `005afe0dd000-005afe14b000` | .so | `r--p` | 440 | 440 | 440 | 128 | 32 | 29.09% | `/data/storage/el1/bundle/libs/arm64/libdyplayer.so` |
| `005c4e71d000-005c4ea1d000` | native heap | `rw-p` | 3072 | 2952 | 2952 | 128 | 32 | 4.17% | `[anon:native_heap:jemalloc]` |
| `005c4f4e7000-005c4f5e7000` | FilePage other | `rw-p` | 1024 | 1024 | 1024 | 124 | 31 | 12.11% | `[anon:async_stack_table]` |
| `005acc27f000-005acc2f2000` | .so | `r-xp` | 460 | 244 | 3 | 120 | 30 | 26.09% | `/system/lib64/platformsdk/libwant.z.so` |
| `005c4db9a000-005c4de1a000` | native heap | `rw-p` | 2560 | 1756 | 1756 | 120 | 30 | 4.69% | `[anon:native_heap:jemalloc]` |
| `00260bf00000-00260bf40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 116 | 29 | 45.31% | `[anon:ArkTS Heap]` |
| `00260f380000-00260f3c0000` | ark ts heap | `rw-p` | 256 | 256 | 57 | 112 | 28 | 43.75% | `[anon:ArkTS Heapappspawn space]` |
| `005a49e01000-005a4a001000` | native heap | `rw-p` | 2048 | 788 | 363 | 112 | 28 | 5.47% | `[anon:native_heap:jemalloc]` |
| `005ad2f00000-005ad3111000` | .so | `r--p` | 2116 | 612 | 29 | 112 | 28 | 5.29% | `/system/lib64/platformsdk/libark_jsruntime.so` |
| `005afe152000-005afe44b000` | FilePage other | `rw-p` | 3044 | 276 | 276 | 112 | 28 | 3.68% | `[anon:libdyplayer.so.bss]` |
| `003c00004000-003c001fc000` | FilePage other | `rw-p` | 2016 | 1620 | 1620 | 108 | 27 | 5.36% | `[anon:partition_alloc]` |
| `005ae3ea7000-005ae3f62000` | .so | `r-xp` | 748 | 180 | 28 | 108 | 27 | 14.44% | `/system/lib64/platformsdk/libav_codec_client.z.so` |
| `00260fb00000-00260fb40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 104 | 26 | 40.62% | `[anon:ArkTS Heap]` |
| `005d37761000-005d37fdc000` | .so | `r--p` | 8684 | 8668 | 8668 | 100 | 25 | 1.15% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so` |
| `003c00a04000-003c00bf8000` | FilePage other | `rw-p` | 2000 | 968 | 968 | 96 | 24 | 4.80% | `[anon:partition_alloc]` |
| `00260b880000-00260b8c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 92 | 23 | 35.94% | `[anon:ArkTS Heap]` |
| `00260b240000-00260b2c0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 88 | 22 | 17.19% | `[anon:ArkTS Heapshared old space]` |
| `00260f780000-00260f7c0000` | ark ts heap | `rw-p` | 256 | 148 | 97 | 80 | 20 | 31.25% | `[anon:ArkTS Heapshared appspawn space]` |
| `005ad1010000-005ad102f000` | .so | `r-xp` | 124 | 124 | 3 | 80 | 20 | 64.52% | `/system/lib64/platformsdk/libuv.so` |
| `005d380d1000-005d3824e000` | FilePage other | `rw-p` | 1524 | 360 | 360 | 80 | 20 | 5.25% | `[anon:libarkweb_engine.so.bss]` |
| `001e60080000-001e60100000` | ark ts heap | `rw-p` | 512 | 456 | 456 | 76 | 19 | 14.84% | `[anon:ArkTS Heapshared huge object space]` |
| `005a4ad52000-005a4ad83000` | .so | `r-xp` | 196 | 100 | 0 | 76 | 19 | 38.78% | `/system/lib64/libhilog_inner.so` |
| `005ada666000-005ada68c000` | GL | `r-xp` | 152 | 152 | 9 | 76 | 19 | 50.00% | `/system/lib64/libEGL.so` |
| `005ae3638000-005ae368e000` | .so | `r-xp` | 344 | 116 | 20 | 76 | 19 | 22.09% | `/system/lib64/platformsdk/libaudio_common.z.so` |
| `002608d40000-002608dc0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 72 | 18 | 14.06% | `[anon:ArkTS Heap]` |
| `00178ffc0000-001790000000` | ark ts heap | `rw-p` | 256 | 252 | 252 | 68 | 17 | 26.56% | `[anon:ArkTS Heapnon movable space]` |
| `003c00804000-003c009fc000` | FilePage other | `rw-p` | 2016 | 1660 | 1660 | 68 | 17 | 3.37% | `[anon:partition_alloc]` |
| `005a4ac17000-005a4ac36000` | .so | `r-xp` | 124 | 112 | 0 | 68 | 17 | 54.84% | `/system/lib64/chipset-sdk-sp/libutils.z.so` |
| `00260f200000-00260f240000` | ark ts heap | `rw-p` | 256 | 256 | 53 | 64 | 16 | 25.00% | `[anon:ArkTS Heapappspawn space]` |
| `005ad6dd9000-005ad6e14000` | .so | `r-xp` | 236 | 76 | 2 | 64 | 16 | 27.12% | `/system/lib64/platformsdk/libdatashare_common.z.so` |
| `005b4d432000-005b4dc7e000` | .hap | `r--p` | 8496 | 7536 | 7533 | 64 | 16 | 0.75% | `/data/storage/el1/bundle/entry.hap` |
| `00260a380000-00260a400000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 60 | 15 | 11.72% | `[anon:ArkTS Heap]` |
| `00260fa80000-00260fac0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 60 | 15 | 23.44% | `[anon:ArkTS Heap]` |
| `005a49593000-005a4962c000` | FilePage other | `r--p` | 612 | 260 | 3 | 60 | 15 | 9.80% | `/system/lib/ld-musl-aarch64.so.1` |
| `005ad1c43000-005ad1c95000` | .so | `r-xp` | 328 | 300 | 10 | 60 | 15 | 18.29% | `/system/lib64/platformsdk/libruntime.z.so` |
| `005adb187000-005adb1fe000` | FilePage other | `rw-p` | 476 | 352 | 28 | 60 | 15 | 12.61% | `/system/etc/abc/framework/stateMgmt.abc` |
| `005ae40f9000-005ae413d000` | .so | `r-xp` | 272 | 128 | 25 | 60 | 15 | 22.06% | `/system/lib64/platformsdk/libaudio_stream_client.z.so` |
| `005b0a58d000-005b0a5b1000` | .so | `r-xp` | 144 | 132 | 19 | 60 | 15 | 41.67% | `/system/lib64/module/libworker.z.so` |
| `00178fe80000-00178fec0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 56 | 14 | 21.88% | `[anon:ArkTS Heapnon movable space]` |
| `00260e9c0000-00260ea40000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 56 | 14 | 10.94% | `[anon:ArkTS Heap]` |
| `005afb891000-005afb92b000` | .so | `r-xp` | 616 | 248 | 248 | 56 | 14 | 9.09% | `/data/storage/el1/bundle/libs/arm64/libc++_shared.so` |
| `00260be40000-00260be80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 52 | 13 | 20.31% | `[anon:ArkTS Heapshared old space]` |
| `00260f3c0000-00260f400000` | ark ts heap | `rw-p` | 256 | 256 | 53 | 52 | 13 | 20.31% | `[anon:ArkTS Heapappspawn space]` |
| `005acc6d8000-005acc6f0000` | .so | `r-xp` | 96 | 76 | 0 | 52 | 13 | 54.17% | `/system/lib64/platformsdk/libcesfwk_core.z.so` |
| `005ad2646000-005ad26ba000` | .so | `r-xp` | 464 | 152 | 13 | 52 | 13 | 11.21% | `/system/lib64/platformsdk/libmedia_foundation.z.so` |
| `003c00204000-003c003f4000` | FilePage other | `rw-p` | 1984 | 1316 | 1316 | 48 | 12 | 2.42% | `[anon:partition_alloc]` |
| `005acd1c6000-005acd1d5000` | .so | `r-xp` | 60 | 48 | 0 | 48 | 12 | 80.00% | `/system/lib64/platformsdk/libzuri.z.so` |
| `005acec61000-005acecc5000` | .so | `r-xp` | 400 | 184 | 5 | 48 | 12 | 12.00% | `/system/lib64/platformsdk/libdatashare_consumer.z.so` |
| `00260c440000-00260c480000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 44 | 11 | 17.19% | `[anon:ArkTS Heap]` |
| `00260ee80000-00260eec0000` | ark ts heap | `rw-p` | 256 | 256 | 93 | 44 | 11 | 17.19% | `[anon:ArkTS Heapappspawn space]` |
| `00260f1c0000-00260f200000` | ark ts heap | `rw-p` | 256 | 256 | 57 | 44 | 11 | 17.19% | `[anon:ArkTS Heapappspawn space]` |
| `003c00404000-003c005f8000` | FilePage other | `rw-p` | 2000 | 1084 | 1084 | 44 | 11 | 2.20% | `[anon:partition_alloc]` |
| `003c00604000-003c007c0000` | FilePage other | `rw-p` | 1776 | 1056 | 1056 | 44 | 11 | 2.48% | `[anon:partition_alloc]` |
| `005ad38ba000-005ad38d5000` | .so | `r--p` | 108 | 84 | 2 | 44 | 11 | 40.74% | `/system/lib64/platformsdk/libark_jsruntime.so` |
| `00260fd40000-00260fd80000` | ark ts heap | `rw-p` | 256 | 256 | 124 | 40 | 10 | 15.62% | `[anon:ArkTS Heapshared appspawn space]` |
| `005a497af000-005a49a9b000` | FilePage other | `rw-p` | 2992 | 64 | 64 | 40 | 10 | 1.34% | `[anon:ld-musl-aarch64.so.1.bss]` |
| `005a4aec3000-005a4aecf000` | .so | `r-xp` | 48 | 48 | 0 | 40 | 10 | 83.33% | `/system/lib64/chipset-sdk-sp/libsec_shared.z.so` |
| `005acd286000-005acd291000` | .so | `r-xp` | 44 | 40 | 0 | 40 | 10 | 90.91% | `/system/lib64/platformsdk/libipc_common.z.so` |
| `005ada71f000-005ada754000` | GL | `r-xp` | 212 | 40 | 5 | 40 | 10 | 18.87% | `/system/lib64/libGLESv3.so` |
| `005b0a10b000-005b0a12c000` | .so | `r-xp` | 132 | 40 | 3 | 40 | 10 | 30.30% | `/system/lib64/module/libsettings.z.so` |
| `00178f600000-00178f680000` | ark ts heap | `rw-p` | 512 | 392 | 392 | 36 | 9 | 7.03% | `[anon:ArkTS Heapnon movable space]` |
| `0026093c0000-002609400000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 36 | 9 | 14.06% | `[anon:ArkTS Heapsemi space]` |
| `00260a200000-00260a240000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 36 | 9 | 14.06% | `[anon:ArkTS Heapshared old space]` |
| `00260cc80000-00260cd40000` | ark ts heap | `rw-p` | 768 | 768 | 768 | 36 | 9 | 4.69% | `[anon:ArkTS Heapshared old space]` |
| `00260ee00000-00260ee40000` | ark ts heap | `rw-p` | 256 | 188 | 75 | 36 | 9 | 14.06% | `[anon:ArkTS Heapappspawn space]` |
| `00260f800000-00260f840000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 36 | 9 | 14.06% | `[anon:ArkTS Heap]` |
| `005a4a0c5000-005a4a0d1000` | .so | `r-xp` | 48 | 36 | 0 | 36 | 9 | 75.00% | `/system/lib64/chipset-sdk-sp/libhitrace_meter.so` |
| `005a4aff8000-005a4b009000` | FilePage other | `rw-p` | 68 | 40 | 40 | 36 | 9 | 52.94% | `[anon:libffrt.so.bss]` |
| `005ae2f9d000-005ae3345000` | .so | `r--p` | 3744 | 1752 | 169 | 36 | 9 | 0.96% | `/system/lib64/platformsdk/libace_compatible.z.so` |
| `005afe4a1000-005afe4cc000` | .so | `r-xp` | 172 | 72 | 5 | 36 | 9 | 20.93% | `/system/lib64/ndk/libohaudio.so` |
| `00178f780000-00178f7c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 32 | 8 | 12.50% | `[anon:ArkTS Heapnon movable space]` |
| `00178ff80000-00178ffc0000` | ark ts heap | `rw-p` | 256 | 44 | 28 | 32 | 8 | 12.50% | `[anon:ArkTS Heapshared read only space]` |
| `00260a540000-00260a580000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 32 | 8 | 12.50% | `[anon:ArkTS Heap]` |
| `00260ef40000-00260ef80000` | ark ts heap | `rw-p` | 256 | 256 | 57 | 32 | 8 | 12.50% | `[anon:ArkTS Heapappspawn space]` |
| `00260f9c0000-00260fa00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 32 | 8 | 12.50% | `[anon:ArkTS Heap]` |
| `005a4ac00000-005a4ac17000` | .so | `r--p` | 92 | 52 | 1 | 32 | 8 | 34.78% | `/system/lib64/chipset-sdk-sp/libutils.z.so` |
| `005acd20e000-005acd232000` | .so | `r-xp` | 144 | 68 | 2 | 32 | 8 | 22.22% | `/system/lib64/libhap_restorecon.z.so` |
| `005aded9d000-005adedc8000` | GL | `r-xp` | 172 | 100 | 28 | 32 | 8 | 18.60% | `/system/lib64/platformsdk/libaudio_renderer.z.so` |
| `005ae3fa0000-005ae3fe8000` | .so | `r-xp` | 288 | 120 | 21 | 32 | 8 | 11.11% | `/system/lib64/platformsdk/libaudio_utils.z.so` |
| `005af8206000-005af8506000` | FilePage other | `rw-p` | 3072 | 48 | 48 | 32 | 8 | 1.04% | `[anon:ffrt_coroutine_stack]` |
| `005b09fcc000-005b09fd7000` | .so | `r-xp` | 44 | 40 | 4 | 32 | 8 | 72.73% | `/system/lib64/platformsdk/libsensor_utils.z.so` |
| `005d1fc7a000-005d2047b000` | FilePage other | `rw-p` | 8196 | 48 | 48 | 32 | 8 | 0.39% | `[anon:stack:30256]` |
| `005d37fe0000-005d380d1000` | .so | `rw-p` | 964 | 580 | 580 | 32 | 8 | 3.32% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so` |
| `007f686cb000-007f68ec8000` | stack | `rw-p` | 8180 | 100 | 100 | 32 | 8 | 0.39% | `[stack]` |
| `00178fac0000-00178fb00000` | ark ts heap | `rw-p` | 256 | 252 | 252 | 28 | 7 | 10.94% | `[anon:ArkTS Heapnon movable space]` |
| `00178ff40000-00178ff80000` | ark ts heap | `rw-p` | 256 | 160 | 148 | 28 | 7 | 10.94% | `[anon:ArkTS Heapshared non movable space]` |
| `002609880000-0026098c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 28 | 7 | 10.94% | `[anon:ArkTS Heapshared old space]` |
| `00260a180000-00260a200000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 28 | 7 | 5.47% | `[anon:ArkTS Heap]` |
| `00260ad80000-00260ae00000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 28 | 7 | 5.47% | `[anon:ArkTS Heap]` |
| `00260b000000-00260b040000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 28 | 7 | 10.94% | `[anon:ArkTS Heap]` |
| `00260ee40000-00260ee80000` | ark ts heap | `rw-p` | 256 | 256 | 62 | 28 | 7 | 10.94% | `[anon:ArkTS Heapappspawn space]` |
| `00260ef80000-00260efc0000` | ark ts heap | `rw-p` | 256 | 256 | 61 | 28 | 7 | 10.94% | `[anon:ArkTS Heapappspawn space]` |
| `00260efc0000-00260f000000` | ark ts heap | `rw-p` | 256 | 256 | 84 | 28 | 7 | 10.94% | `[anon:ArkTS Heapappspawn space]` |
| `00260f600000-00260f640000` | ark ts heap | `rw-p` | 256 | 256 | 119 | 28 | 7 | 10.94% | `[anon:ArkTS Heapshared appspawn space]` |
| `00260ffc0000-002610000000` | ark ts heap | `rw-p` | 256 | 256 | 81 | 28 | 7 | 10.94% | `[anon:ArkTS Heapshared appspawn space]` |
| `005acc710000-005acc73d000` | .so | `r-xp` | 180 | 124 | 1 | 28 | 7 | 15.56% | `/system/lib64/chipset-sdk-sp/libhicollie.z.so` |
| `005accb1f000-005accb5e000` | .so | `r-xp` | 252 | 40 | 0 | 28 | 7 | 11.11% | `/system/lib64/platformsdk/libos_account_innerkits.z.so` |
| `005acecc5000-005acecd5000` | .so | `r--p` | 64 | 52 | 1 | 28 | 7 | 43.75% | `/system/lib64/platformsdk/libdatashare_consumer.z.so` |
| `005acf308000-005acf314000` | .so | `r-xp` | 48 | 28 | 1 | 28 | 7 | 58.33% | `/system/lib64/platformsdk/libconsole.z.so` |
| `005ae3e40000-005ae3ea7000` | .so | `r--p` | 412 | 136 | 13 | 28 | 7 | 6.80% | `/system/lib64/platformsdk/libav_codec_client.z.so` |
| `005ae3f62000-005ae3f6f000` | .so | `r--p` | 52 | 40 | 15 | 28 | 7 | 53.85% | `/system/lib64/platformsdk/libav_codec_client.z.so` |
| `005b09f90000-005b09faf000` | .so | `r-xp` | 124 | 92 | 11 | 28 | 7 | 22.58% | `/system/lib64/platformsdk/libsensor_client.z.so` |
| `005b0a049000-005b0a06a000` | .so | `r-xp` | 132 | 60 | 22 | 28 | 7 | 21.21% | `/system/lib64/module/libsensor.z.so` |
| `005c4f707000-005c4f725000` | .so | `r-xp` | 120 | 80 | 3 | 28 | 7 | 23.33% | `/system/lib64/libframeawaresched.so` |
| `005d38afe000-005d38bdb000` | GL | `r-xp` | 884 | 240 | 23 | 28 | 7 | 3.17% | `/system/lib64/libohos_adapter_glue_source.z.so` |
| `00178f5c0000-00178f600000` | ark ts heap | `rw-p` | 256 | 180 | 180 | 24 | 6 | 9.38% | `[anon:ArkTS Heapnon movable space]` |
| `00178fcc0000-00178fd00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 24 | 6 | 9.38% | `[anon:ArkTS Heapnon movable space]` |
| `00260be80000-00260bec0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 24 | 6 | 9.38% | `[anon:ArkTS Heapsemi space]` |
| `00260d540000-00260d5c0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 24 | 6 | 4.69% | `[anon:ArkTS Heapshared old space]` |
| `00260f300000-00260f340000` | ark ts heap | `rw-p` | 256 | 256 | 77 | 24 | 6 | 9.38% | `[anon:ArkTS Heapappspawn space]` |
| `003c00c04000-003c00cd4000` | FilePage other | `rw-p` | 832 | 188 | 188 | 24 | 6 | 2.88% | `[anon:partition_alloc]` |
| `005acc78c000-005acc794000` | .so | `r-xp` | 32 | 24 | 0 | 24 | 6 | 75.00% | `/system/lib64/platformsdk/libbase.z.so` |
| `005ace905000-005ace90d000` | Graph | `r--p` | 32 | 24 | 1 | 24 | 6 | 75.00% | `/system/lib64/chipset-sdk-sp/libsurface.z.so` |
| `005ad0fdd000-005ad0fe3000` | .so | `r--p` | 24 | 24 | 0 | 24 | 6 | 100.00% | `/system/lib64/platformsdk/libace_napi.z.so` |
| `005ad38d9000-005ad390a000` | FilePage other | `rw-p` | 196 | 92 | 68 | 24 | 6 | 12.24% | `[anon:libark_jsruntime.so.bss]` |
| `005ada69b000-005ada6c3000` | GL | `rw-p` | 160 | 28 | 28 | 24 | 6 | 15.00% | `[anon:libEGL.so.bss]` |
| `005ae413d000-005ae4144000` | .so | `r--p` | 28 | 28 | 14 | 24 | 6 | 85.71% | `/system/lib64/platformsdk/libaudio_stream_client.z.so` |
| `005d1eccf000-005d1ecd5000` | .so | `r--p` | 24 | 24 | 24 | 24 | 6 | 100.00% | `/data/storage/el1/bundle/libs/arm64/libdanmu.so` |
| `005d20683000-005d20784000` | FilePage other | `rw-p` | 1028 | 52 | 52 | 24 | 6 | 2.33% | `[anon:stack:30279]` |
| `005d2d189000-005d2d193000` | .so | `r-xp` | 40 | 24 | 1 | 24 | 6 | 60.00% | `/system/lib64/ndk/libohcommonevent.so` |
| `00178f740000-00178f780000` | ark ts heap | `rw-p` | 256 | 232 | 232 | 20 | 5 | 7.81% | `[anon:ArkTS Heapnon movable space]` |
| `002608f40000-002609000000` | ark ts heap | `rw-p` | 768 | 768 | 768 | 20 | 5 | 2.60% | `[anon:ArkTS Heap]` |
| `002609a00000-002609a40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 20 | 5 | 7.81% | `[anon:ArkTS Heapsemi space]` |
| `00260af00000-00260af40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 20 | 5 | 7.81% | `[anon:ArkTS Heap]` |
| `00260b2c0000-00260b340000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 20 | 5 | 3.91% | `[anon:ArkTS Heapshared old space]` |
| `00260c600000-00260c640000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 20 | 5 | 7.81% | `[anon:ArkTS Heap]` |
| `00260ca80000-00260cac0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 20 | 5 | 7.81% | `[anon:ArkTS Heap]` |
| `00260e700000-00260e780000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 20 | 5 | 3.91% | `[anon:ArkTS Heap]` |
| `00260ea80000-00260eb00000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 20 | 5 | 3.91% | `[anon:ArkTS Heap]` |
| `00260fc00000-00260fc40000` | ark ts heap | `rw-p` | 256 | 112 | 112 | 20 | 5 | 7.81% | `[anon:ArkTS Heapsemi space]` |
| `005a4aa80000-005a4ab10000` | .so | `r--p` | 576 | 260 | 7 | 20 | 5 | 3.47% | `/system/lib64/chipset-sdk-sp/libc++.so` |
| `005a4abae000-005a4abb9000` | .so | `r--p` | 44 | 28 | 0 | 20 | 5 | 45.45% | `/system/lib64/chipset-sdk-sp/libc++.so` |
| `005a4adc5000-005a4adcd000` | .so | `r-xp` | 32 | 24 | 0 | 20 | 5 | 62.50% | `/system/lib64/chipset-sdk-sp/libhitracechain.so` |
| `005a4af40000-005a4af69000` | .so | `r--p` | 164 | 92 | 0 | 20 | 5 | 12.20% | `/system/lib64/ndk/libffrt.so` |
| `005a4aff2000-005a4aff7000` | .so | `r--p` | 20 | 20 | 0 | 20 | 5 | 100.00% | `/system/lib64/ndk/libffrt.so` |
| `005acc2f2000-005acc2f8000` | .so | `r--p` | 24 | 24 | 0 | 20 | 5 | 83.33% | `/system/lib64/platformsdk/libwant.z.so` |
| `005ad1f45000-005ad1f4b000` | .so | `r-xp` | 24 | 20 | 1 | 20 | 5 | 83.33% | `/system/lib64/ndk/libsync_fence.z.so` |
| `005ad1f4d000-005ad1f7b000` | FilePage other | `rw-p` | 184 | 184 | 184 | 20 | 5 | 10.87% | `[anon:ArkTS Code:396560407104]` |
| `005ad26ba000-005ad26c2000` | .so | `r--p` | 32 | 28 | 6 | 20 | 5 | 62.50% | `/system/lib64/platformsdk/libmedia_foundation.z.so` |
| `005ae4e83000-005ae5183000` | native heap | `rw-p` | 3072 | 400 | 131 | 20 | 5 | 0.65% | `[anon:native_heap:jemalloc]` |
| `005afb65e000-005afb6c6000` | .so | `r-xp` | 416 | 348 | 51 | 20 | 5 | 4.81% | `/system/lib64/module/net/libhttp.z.so` |
| `005afd4c4000-005afd4cb000` | .so | `r-xp` | 28 | 28 | 2 | 20 | 5 | 71.43% | `/system/lib64/libnative_media_vdec.so` |
| `005d1ebc0000-005d1ec46000` | .so | `r--p` | 536 | 448 | 448 | 20 | 5 | 3.73% | `/data/storage/el1/bundle/libs/arm64/libdanmu.so` |
| `005d1f34b000-005d1f358000` | Graph | `r-xp` | 52 | 52 | 15 | 20 | 5 | 38.46% | `/system/lib64/libgameservice_graphic_plugin.z.so` |
| `005d38bdb000-005d38bef000` | GL | `r--p` | 80 | 80 | 80 | 20 | 5 | 25.00% | `/system/lib64/libohos_adapter_glue_source.z.so` |
| `00178f800000-00178f840000` | ark ts heap | `rw-p` | 256 | 252 | 252 | 16 | 4 | 6.25% | `[anon:ArkTS Heapnon movable space]` |
| `00178f840000-00178f880000` | ark ts heap | `rw-p` | 256 | 140 | 140 | 16 | 4 | 6.25% | `[anon:ArkTS Heapnon movable space]` |
| `00178fa00000-00178fa40000` | ark ts heap | `rw-p` | 256 | 180 | 180 | 16 | 4 | 6.25% | `[anon:ArkTS Heapnon movable space]` |
| `00178fe40000-00178fe80000` | ark ts heap | `rw-p` | 256 | 240 | 240 | 16 | 4 | 6.25% | `[anon:ArkTS Heapnon movable space]` |
| `001e60000000-001e60080000` | ark ts heap | `rw-p` | 512 | 456 | 456 | 16 | 4 | 3.12% | `[anon:ArkTS Heaphuge object space]` |
| `002608c80000-002608d00000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 16 | 4 | 3.12% | `[anon:ArkTS Heap]` |
| `00260ab00000-00260ab80000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 16 | 4 | 3.12% | `[anon:ArkTS Heap]` |
| `00260bec0000-00260bf00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 16 | 4 | 6.25% | `[anon:ArkTS Heapshared old space]` |
| `00260e280000-00260e2c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 16 | 4 | 6.25% | `[anon:ArkTS Heapsemi space]` |
| `00260e2c0000-00260e340000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 16 | 4 | 3.12% | `[anon:ArkTS Heap]` |
| `00260ed40000-00260edc0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 16 | 4 | 3.12% | `[anon:ArkTS Heap]` |
| `00260eec0000-00260ef00000` | ark ts heap | `rw-p` | 256 | 256 | 26 | 16 | 4 | 6.25% | `[anon:ArkTS Heapappspawn space]` |
| `00260f100000-00260f140000` | ark ts heap | `rw-p` | 256 | 256 | 26 | 16 | 4 | 6.25% | `[anon:ArkTS Heapappspawn space]` |
| `00260f280000-00260f2c0000` | ark ts heap | `rw-p` | 256 | 256 | 30 | 16 | 4 | 6.25% | `[anon:ArkTS Heapappspawn space]` |
| `00260f6c0000-00260f700000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 16 | 4 | 6.25% | `[anon:ArkTS Heapshared old space]` |
| `00260f700000-00260f740000` | ark ts heap | `rw-p` | 256 | 184 | 184 | 16 | 4 | 6.25% | `[anon:ArkTS Heap]` |
| `00260fdc0000-00260fe00000` | ark ts heap | `rw-p` | 256 | 256 | 69 | 16 | 4 | 6.25% | `[anon:ArkTS Heapshared appspawn space]` |
| `005a4ad40000-005a4ad52000` | .so | `r--p` | 72 | 20 | 0 | 16 | 4 | 22.22% | `/system/lib64/libhilog_inner.so` |
| `005a4ae47000-005a4ae5d000` | .so | `r-xp` | 88 | 24 | 0 | 16 | 4 | 18.18% | `/system/lib64/chipset-sdk-sp/libbacktrace_local.so` |
| `005acc3c1000-005acc3c6000` | GL | `r--p` | 20 | 16 | 0 | 16 | 4 | 80.00% | `/system/lib64/platformsdk/libipc_single.z.so` |
| `005acc556000-005acc564000` | .so | `r-xp` | 56 | 44 | 0 | 16 | 4 | 28.57% | `/system/lib64/platformsdk/libcesfwk_innerkits.z.so` |
| `005acc6f0000-005acc6f6000` | .so | `r--p` | 24 | 24 | 0 | 16 | 4 | 66.67% | `/system/lib64/platformsdk/libcesfwk_core.z.so` |
| `005acc794000-005acc798000` | .so | `r--p` | 16 | 16 | 0 | 16 | 4 | 100.00% | `/system/lib64/platformsdk/libbase.z.so` |
| `005ace880000-005ace8b3000` | Graph | `r--p` | 204 | 84 | 3 | 16 | 4 | 7.84% | `/system/lib64/chipset-sdk-sp/libsurface.z.so` |
| `005ad0f40000-005ad0f80000` | .so | `r--p` | 256 | 140 | 5 | 16 | 4 | 6.25% | `/system/lib64/platformsdk/libace_napi.z.so` |
| `005ad1c00000-005ad1c43000` | .so | `r--p` | 268 | 124 | 4 | 16 | 4 | 5.97% | `/system/lib64/platformsdk/libruntime.z.so` |
| `005ad6f23000-005ad6f48000` | .so | `r-xp` | 148 | 64 | 3 | 16 | 4 | 10.81% | `/system/lib64/platformsdk/libability_context_native.z.so` |
| `005adff72000-005ae2f9d000` | .so | `r-xp` | 49324 | 22600 | 3459 | 16 | 4 | 0.03% | `/system/lib64/platformsdk/libace_compatible.z.so` |
| `005ae3600000-005ae3638000` | .so | `r--p` | 224 | 52 | 6 | 16 | 4 | 7.14% | `/system/lib64/platformsdk/libaudio_common.z.so` |
| `005ae368e000-005ae3694000` | .so | `r--p` | 24 | 20 | 5 | 16 | 4 | 66.67% | `/system/lib64/platformsdk/libaudio_common.z.so` |
| `005ae40c0000-005ae40f9000` | .so | `r--p` | 228 | 80 | 15 | 16 | 4 | 7.02% | `/system/lib64/platformsdk/libaudio_stream_client.z.so` |
| `005ae8580000-005ae860a000` | .so | `r--p` | 552 | 36 | 5 | 16 | 4 | 2.90% | `/vendor/lib64/passthrough/libhvgr_v210.so` |
| `005b0a100000-005b0a10b000` | .so | `r--p` | 44 | 20 | 1 | 16 | 4 | 36.36% | `/system/lib64/module/libsettings.z.so` |
| `005b0a349000-005b0a362000` | .so | `r-xp` | 100 | 88 | 6 | 16 | 4 | 16.00% | `/system/lib64/module/libutil.z.so` |
| `005c4df1a000-005c4e61a000` | FilePage other | `rw-p` | 7168 | 436 | 436 | 16 | 4 | 0.22% | `[anon:ffrt_coroutine_stack]` |
| `005c4f249000-005c4f258000` | .so | `r-xp` | 60 | 60 | 6 | 16 | 4 | 26.67% | `/system/lib64/libaps_client.z.so` |
| `005d1e482000-005d1e782000` | FilePage other | `rw-p` | 3072 | 176 | 176 | 16 | 4 | 0.52% | `[anon:ffrt_coroutine_stack]` |
| `005d21395000-005d21496000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 16 | 4 | 1.56% | `[anon:stack:30326]` |
| `00178fd40000-00178fd80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 12 | 3 | 4.69% | `[anon:ArkTS Heapnon movable space]` |
| `00178fec0000-00178ff00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 12 | 3 | 4.69% | `[anon:ArkTS Heapnon movable space]` |
| `002608bc0000-002608c40000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 12 | 3 | 2.34% | `[anon:ArkTS Heap]` |
| `002608f00000-002608f40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 12 | 3 | 4.69% | `[anon:ArkTS Heapshared old space]` |
| `00260bac0000-00260bb00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 12 | 3 | 4.69% | `[anon:ArkTS Heap]` |
| `00260c040000-00260c100000` | ark ts heap | `rw-p` | 768 | 768 | 768 | 12 | 3 | 1.56% | `[anon:ArkTS Heap]` |
| `00260c180000-00260c200000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 12 | 3 | 2.34% | `[anon:ArkTS Heapshared old space]` |
| `00260de00000-00260de40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 12 | 3 | 4.69% | `[anon:ArkTS Heapsemi space]` |
| `00260de40000-00260dec0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 12 | 3 | 2.34% | `[anon:ArkTS Heap]` |
| `00260e140000-00260e180000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 12 | 3 | 4.69% | `[anon:ArkTS Heap]` |
| `00260ef00000-00260ef40000` | ark ts heap | `rw-p` | 256 | 256 | 26 | 12 | 3 | 4.69% | `[anon:ArkTS Heapappspawn space]` |
| `00260f240000-00260f280000` | ark ts heap | `rw-p` | 256 | 256 | 38 | 12 | 3 | 4.69% | `[anon:ArkTS Heapappspawn space]` |
| `003800204000-003800254000` | FilePage other | `rw-p` | 320 | 92 | 92 | 12 | 3 | 3.75% | `[anon:partition_alloc]` |
| `005a497aa000-005a497af000` | FilePage other | `rw-p` | 20 | 12 | 12 | 12 | 3 | 60.00% | `/system/lib/ld-musl-aarch64.so.1` |
| `005a49a9d000-005a49aa0000` | FilePage other | `r-xs` | 12 | 12 | 0 | 12 | 3 | 100.00% | `[shmm]` |
| `005a4a0c0000-005a4a0c5000` | .so | `r--p` | 20 | 16 | 0 | 12 | 3 | 60.00% | `/system/lib64/chipset-sdk-sp/libhitrace_meter.so` |
| `005a4a183000-005a4a188000` | .so | `r-xp` | 20 | 12 | 0 | 12 | 3 | 60.00% | `/system/lib64/chipset-sdk-sp/libasync_stack.z.so` |
| `005a4abba000-005a4abc1000` | FilePage other | `rw-p` | 28 | 16 | 16 | 12 | 3 | 42.86% | `[anon:libc++.so.bss]` |
| `005a4ac41000-005a4ac44000` | .so | `r-xp` | 12 | 12 | 0 | 12 | 3 | 100.00% | `/system/lib64/chipset-sdk-sp/libhilog_encode.so` |
| `005a4ad83000-005a4ad86000` | .so | `r--p` | 12 | 12 | 0 | 12 | 3 | 100.00% | `/system/lib64/libhilog_inner.so` |
| `005a4ae82000-005a4ae85000` | .so | `r-xp` | 12 | 12 | 0 | 12 | 3 | 100.00% | `/system/lib64/platformsdk/libhilog.so` |
| `005acc340000-005acc36f000` | GL | `r--p` | 188 | 116 | 2 | 12 | 3 | 6.38% | `/system/lib64/platformsdk/libipc_single.z.so` |
| `005acc6c0000-005acc6d8000` | .so | `r--p` | 96 | 28 | 0 | 12 | 3 | 12.50% | `/system/lib64/platformsdk/libcesfwk_core.z.so` |
| `005accb5e000-005accb64000` | .so | `r--p` | 24 | 24 | 0 | 12 | 3 | 50.00% | `/system/lib64/platformsdk/libos_account_innerkits.z.so` |
| `005acce00000-005acce14000` | .so | `r--p` | 80 | 40 | 1 | 12 | 3 | 15.00% | `/system/lib64/chipset-sdk-sp/libeventhandler.z.so` |
| `005acce41000-005acce44000` | .so | `r--p` | 12 | 12 | 0 | 12 | 3 | 100.00% | `/system/lib64/chipset-sdk-sp/libeventhandler.z.so` |
| `005acd232000-005acd235000` | .so | `r--p` | 12 | 12 | 0 | 12 | 3 | 100.00% | `/system/lib64/libhap_restorecon.z.so` |
| `005ad1c95000-005ad1c99000` | .so | `r--p` | 16 | 12 | 0 | 12 | 3 | 75.00% | `/system/lib64/platformsdk/libruntime.z.so` |
| `005ad1f40000-005ad1f45000` | .so | `r--p` | 20 | 16 | 0 | 12 | 3 | 60.00% | `/system/lib64/ndk/libsync_fence.z.so` |
| `005ad5f43000-005ad5f46000` | .so | `r-xp` | 12 | 12 | 0 | 12 | 3 | 100.00% | `/system/lib64/libframe_ui_intf.z.so` |
| `005ad65c0000-005ad65c6000` | .so | `r--p` | 24 | 16 | 0 | 12 | 3 | 50.00% | `/system/lib64/platformsdk/libtimer.z.so` |
| `005ad65c6000-005ad65cc000` | .so | `r-xp` | 24 | 12 | 0 | 12 | 3 | 50.00% | `/system/lib64/platformsdk/libtimer.z.so` |
| `005ad6e14000-005ad6e19000` | .so | `r--p` | 20 | 12 | 0 | 12 | 3 | 60.00% | `/system/lib64/platformsdk/libdatashare_common.z.so` |
| `005ad6e1a000-005ad6e40000` | dev | `rw-s` | 152 | 152 | 152 | 12 | 3 | 7.89% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ada640000-005ada666000` | GL | `r--p` | 152 | 128 | 7 | 12 | 3 | 7.89% | `/system/lib64/libEGL.so` |
| `005adedc8000-005adedcc000` | GL | `r--p` | 16 | 16 | 8 | 12 | 3 | 75.00% | `/system/lib64/platformsdk/libaudio_renderer.z.so` |
| `005ae8809000-005ae880f000` | .so | `rw-p` | 24 | 24 | 17 | 12 | 3 | 50.00% | `/vendor/lib64/passthrough/libhvgr_v210.so` |
| `005ae880f000-005ae8812000` | GL | `rw-p` | 12 | 12 | 12 | 12 | 3 | 100.00% | `[anon:libEGL_impl.so.bss]` |
| `005afb92b000-005afb936000` | .so | `r--p` | 44 | 44 | 44 | 12 | 3 | 27.27% | `/data/storage/el1/bundle/libs/arm64/libc++_shared.so` |
| `005afd449000-005afd457000` | .so | `r-xp` | 56 | 28 | 8 | 12 | 3 | 21.43% | `/system/lib64/libnative_media_core.so` |
| `005afe14b000-005afe152000` | .so | `rw-p` | 28 | 28 | 28 | 12 | 3 | 42.86% | `/data/storage/el1/bundle/libs/arm64/libdyplayer.so` |
| `005afe4cc000-005afe4cf000` | .so | `r--p` | 12 | 12 | 12 | 12 | 3 | 100.00% | `/system/lib64/ndk/libohaudio.so` |
| `005afeae1000-005afebb1000` | .so | `r-xp` | 832 | 224 | 14 | 12 | 3 | 1.44% | `/system/lib64/platformsdk/libnweb_ohos_adapter.z.so` |
| `005b06603000-005b06607000` | .so | `r-xp` | 16 | 16 | 0 | 12 | 3 | 75.00% | `/system/lib64/module/libhilog.z.so` |
| `005b09faf000-005b09fb2000` | .so | `r--p` | 12 | 12 | 3 | 12 | 3 | 100.00% | `/system/lib64/platformsdk/libsensor_client.z.so` |
| `005b0a040000-005b0a049000` | .so | `r--p` | 36 | 20 | 6 | 12 | 3 | 33.33% | `/system/lib64/module/libsensor.z.so` |
| `005b0a12c000-005b0a12f000` | .so | `r--p` | 12 | 12 | 0 | 12 | 3 | 100.00% | `/system/lib64/module/libsettings.z.so` |
| `005b0a580000-005b0a58d000` | .so | `r--p` | 52 | 52 | 6 | 12 | 3 | 23.08% | `/system/lib64/module/libworker.z.so` |
| `005c4da99000-005c4db9a000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 12 | 3 | 1.17% | `[anon:stack:30062]` |
| `005d20986000-005d20a87000` | FilePage other | `rw-p` | 1028 | 20 | 20 | 12 | 3 | 1.17% | `[anon:stack:30292]` |
| `005d20d83000-005d20e84000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 12 | 3 | 1.17% | `[anon:stack:30274]` |
| `005d2118f000-005d21290000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 12 | 3 | 1.17% | `[anon:stack:30324]` |
| `005d21292000-005d21393000` | FilePage other | `rw-p` | 1028 | 20 | 20 | 12 | 3 | 1.17% | `[anon:stack:30325]` |
| `005d383cc000-005d38577000` | .so | `r-xp` | 1708 | 64 | 16 | 12 | 3 | 0.70% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libffmpeg.so` |
| `005d431ea000-005d432ea000` | FilePage other | `rw-p` | 1024 | 16 | 16 | 12 | 3 | 1.17% | `[anon:ffrt_coroutine_stack]` |
| `005d437ea000-005d438ea000` | FilePage other | `rw-p` | 1024 | 80 | 80 | 12 | 3 | 1.17% | `[anon:ffrt_coroutine_stack]` |
| `005d4498c000-005d44b8c000` | FilePage other | `rw-p` | 2048 | 92 | 92 | 12 | 3 | 0.59% | `[anon:ffrt_coroutine_stack]` |
| `00178f7c0000-00178f800000` | ark ts heap | `rw-p` | 256 | 244 | 244 | 8 | 2 | 3.12% | `[anon:ArkTS Heapnon movable space]` |
| `001e60400000-001e60480000` | ark ts heap | `rw-p` | 512 | 452 | 452 | 8 | 2 | 1.56% | `[anon:ArkTS Heaphuge object space]` |
| `0026092c0000-002609300000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 8 | 2 | 3.12% | `[anon:ArkTS Heap]` |
| `00260a940000-00260a980000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 8 | 2 | 3.12% | `[anon:ArkTS Heap]` |
| `00260aa40000-00260aac0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 8 | 2 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260af80000-00260afc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 8 | 2 | 3.12% | `[anon:ArkTS Heapsemi space]` |
| `00260bb40000-00260bc00000` | ark ts heap | `rw-p` | 768 | 528 | 528 | 8 | 2 | 1.04% | `[anon:ArkTS Heap]` |
| `00260bc40000-00260bc80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 8 | 2 | 3.12% | `[anon:ArkTS Heapshared old space]` |
| `00260c700000-00260c780000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 8 | 2 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260df40000-00260df80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 8 | 2 | 3.12% | `[anon:ArkTS Heapsemi space]` |
| `00260e5c0000-00260e640000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 8 | 2 | 1.56% | `[anon:ArkTS Heap]` |
| `00260e640000-00260e700000` | ark ts heap | `rw-p` | 768 | 768 | 768 | 8 | 2 | 1.04% | `[anon:ArkTS Heapshared old space]` |
| `00260f040000-00260f080000` | ark ts heap | `rw-p` | 256 | 256 | 62 | 8 | 2 | 3.12% | `[anon:ArkTS Heapappspawn space]` |
| `00260f680000-00260f6c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 8 | 2 | 3.12% | `[anon:ArkTS Heap]` |
| `00260f8c0000-00260f900000` | ark ts heap | `rw-p` | 256 | 172 | 86 | 8 | 2 | 3.12% | `[anon:ArkTS Heapshared appspawn space]` |
| `005a497a2000-005a497aa000` | FilePage other | `r--p` | 32 | 24 | 1 | 8 | 2 | 25.00% | `/system/lib/ld-musl-aarch64.so.1` |
| `005a4aa46000-005a4aa52000` | .so | `r-xp` | 48 | 24 | 0 | 8 | 2 | 16.67% | `/system/lib64/platformsdk/libdfx_signalhandler.z.so` |
| `005a4ac36000-005a4ac38000` | .so | `r--p` | 8 | 8 | 0 | 8 | 2 | 100.00% | `/system/lib64/chipset-sdk-sp/libutils.z.so` |
| `005a4acd3000-005a4ad0b000` | .so | `r-xp` | 224 | 132 | 7 | 8 | 2 | 3.57% | `/system/lib64/chipset-sdk-sp/libunwinder.z.so` |
| `005acc73d000-005acc73f000` | .so | `r--p` | 8 | 8 | 0 | 8 | 2 | 100.00% | `/system/lib64/chipset-sdk-sp/libhicollie.z.so` |
| `005accb00000-005accb1f000` | .so | `r--p` | 124 | 40 | 1 | 8 | 2 | 6.45% | `/system/lib64/platformsdk/libos_account_innerkits.z.so` |
| `005acd1d5000-005acd1d7000` | .so | `r--p` | 8 | 8 | 0 | 8 | 2 | 100.00% | `/system/lib64/platformsdk/libzuri.z.so` |
| `005acd280000-005acd286000` | .so | `r--p` | 24 | 12 | 0 | 8 | 2 | 33.33% | `/system/lib64/platformsdk/libipc_common.z.so` |
| `005acec40000-005acec61000` | .so | `r--p` | 132 | 36 | 0 | 8 | 2 | 6.06% | `/system/lib64/platformsdk/libdatashare_consumer.z.so` |
| `005acf300000-005acf308000` | .so | `r--p` | 32 | 16 | 0 | 8 | 2 | 25.00% | `/system/lib64/platformsdk/libconsole.z.so` |
| `005acf314000-005acf316000` | .so | `r--p` | 8 | 8 | 0 | 8 | 2 | 100.00% | `/system/lib64/platformsdk/libconsole.z.so` |
| `005ad1000000-005ad1010000` | .so | `r--p` | 64 | 36 | 0 | 8 | 2 | 12.50% | `/system/lib64/platformsdk/libuv.so` |
| `005ad13ca000-005ad13d5000` | .so | `r-xp` | 44 | 20 | 1 | 8 | 2 | 18.18% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_hdi_impl_v1_4.z.so` |
| `005ad144f000-005ad1451000` | dev | `rw-s` | 8 | 8 | 4 | 8 | 2 | 100.00% | `anon_inode:dev/ashmem/server_client_buffer` |
| `005ad38d5000-005ad38d9000` | .so | `rw-p` | 16 | 8 | 4 | 8 | 2 | 50.00% | `/system/lib64/platformsdk/libark_jsruntime.so` |
| `005ad5783000-005ad5788000` | GL | `r-xp` | 20 | 12 | 0 | 8 | 2 | 40.00% | `/system/lib64/libarkweb_glue_base.z.so` |
| `005ad65cc000-005ad65ce000` | .so | `r--p` | 8 | 8 | 0 | 8 | 2 | 100.00% | `/system/lib64/platformsdk/libtimer.z.so` |
| `005ad6742000-005ad6744000` | .so | `r-xp` | 8 | 8 | 0 | 8 | 2 | 100.00% | `/system/lib64/platformsdk/libace_container_scope.z.so` |
| `005ad6dc0000-005ad6dd9000` | .so | `r--p` | 100 | 24 | 0 | 8 | 2 | 8.00% | `/system/lib64/platformsdk/libdatashare_common.z.so` |
| `005ad6f48000-005ad6f4f000` | .so | `r--p` | 28 | 8 | 0 | 8 | 2 | 28.57% | `/system/lib64/platformsdk/libability_context_native.z.so` |
| `005ada68c000-005ada69a000` | GL | `r--p` | 56 | 28 | 4 | 8 | 2 | 14.29% | `/system/lib64/libEGL.so` |
| `005ada756000-005ada77c000` | dev | `rw-s` | 152 | 152 | 152 | 8 | 2 | 5.26% | `anon_inode:dev/ashmem/EXTRawData` |
| `005adae90000-005adb110000` | native heap | `rw-p` | 2560 | 536 | 257 | 8 | 2 | 0.31% | `[anon:native_heap:jemalloc]` |
| `005ae3fe8000-005ae3feb000` | .so | `r--p` | 12 | 8 | 1 | 8 | 2 | 66.67% | `/system/lib64/platformsdk/libaudio_utils.z.so` |
| `005aee2c4000-005aee2c8000` | .so | `r-xp` | 16 | 16 | 0 | 8 | 2 | 50.00% | `/system/lib64/platformsdk/libhdc_register.z.so` |
| `005aee381000-005aee383000` | .so | `r-xp` | 8 | 8 | 0 | 8 | 2 | 100.00% | `/system/lib64/libhispeed_string.so` |
| `005af1728000-005af1829000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 8 | 2 | 0.78% | `[anon:stack:30002]` |
| `005af182b000-005af192c000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 8 | 2 | 0.78% | `[anon:stack:30003]` |
| `005af8105000-005af8206000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30008]` |
| `005af8a54000-005af8b55000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 8 | 2 | 0.78% | `[anon:stack:30011]` |
| `005af9376000-005af9477000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 8 | 2 | 0.78% | `[anon:stack:30635]` |
| `005af957c000-005af967d000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 8 | 2 | 0.78% | `[anon:stack:30023]` |
| `005af967d000-005af975e000` | FilePage other | `rw-p` | 900 | 900 | 900 | 8 | 2 | 0.89% | `[anon:ArkTS MethodLiteral]` |
| `005afb6c6000-005afb6ca000` | .so | `r--p` | 16 | 16 | 16 | 8 | 2 | 50.00% | `/system/lib64/module/net/libhttp.z.so` |
| `005afb937000-005afb93e000` | FilePage other | `rw-p` | 28 | 12 | 12 | 8 | 2 | 28.57% | `[anon:libc++_shared.so.bss]` |
| `005afd457000-005afd459000` | .so | `r--p` | 8 | 8 | 8 | 8 | 2 | 100.00% | `/system/lib64/libnative_media_core.so` |
| `005afd4c0000-005afd4c4000` | .so | `r--p` | 16 | 12 | 0 | 8 | 2 | 50.00% | `/system/lib64/libnative_media_vdec.so` |
| `005afebb1000-005afebc1000` | .so | `r--p` | 64 | 64 | 64 | 8 | 2 | 12.50% | `/system/lib64/platformsdk/libnweb_ohos_adapter.z.so` |
| `005b02203000-005b02205000` | .so | `r--p` | 8 | 8 | 8 | 8 | 2 | 100.00% | `/system/lib64/ndk/libhitrace_ndk.z.so` |
| `005b05401000-005b05404000` | .so | `r-xp` | 12 | 8 | 0 | 8 | 2 | 66.67% | `/system/lib64/ndk/libhilog_ndk.z.so` |
| `005b078b6000-005b07955000` | .so | `r-xp` | 636 | 492 | 27 | 8 | 2 | 1.26% | `/system/lib64/platformsdk/libcurl_shared_http3.z.so` |
| `005b09fc0000-005b09fcc000` | .so | `r--p` | 48 | 16 | 1 | 8 | 2 | 16.67% | `/system/lib64/platformsdk/libsensor_utils.z.so` |
| `005b0a06a000-005b0a06d000` | .so | `r--p` | 12 | 8 | 2 | 8 | 2 | 66.67% | `/system/lib64/module/libsensor.z.so` |
| `005b0a340000-005b0a349000` | .so | `r--p` | 36 | 12 | 0 | 8 | 2 | 22.22% | `/system/lib64/module/libutil.z.so` |
| `005b0a362000-005b0a365000` | .so | `r--p` | 12 | 12 | 0 | 8 | 2 | 66.67% | `/system/lib64/module/libutil.z.so` |
| `005b0a5b1000-005b0a5b4000` | .so | `r--p` | 12 | 12 | 0 | 8 | 2 | 66.67% | `/system/lib64/module/libworker.z.so` |
| `005c4d996000-005c4da97000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 8 | 2 | 0.78% | `[anon:stack:30061]` |
| `005c4f258000-005c4f25c000` | .so | `r--p` | 16 | 16 | 16 | 8 | 2 | 50.00% | `/system/lib64/libaps_client.z.so` |
| `005c4f25f000-005c4f360000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30065]` |
| `005c4f725000-005c4f727000` | .so | `r--p` | 8 | 8 | 8 | 8 | 2 | 100.00% | `/system/lib64/libframeawaresched.so` |
| `005c4f74e000-005c4f84f000` | FilePage other | `rw-p` | 1028 | 20 | 20 | 8 | 2 | 0.78% | `[anon:stack:30068]` |
| `005d1ecd6000-005d1ecd8000` | FilePage other | `rw-p` | 8 | 8 | 8 | 8 | 2 | 100.00% | `[anon:libdanmu.so.bss]` |
| `005d1f358000-005d1f35c000` | Graph | `r--p` | 16 | 16 | 16 | 8 | 2 | 50.00% | `/system/lib64/libgameservice_graphic_plugin.z.so` |
| `005d1f76b000-005d1f86c000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30241]` |
| `005d20e86000-005d20f87000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 8 | 2 | 0.78% | `[anon:stack:30275]` |
| `005d20f89000-005d2108a000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30322]` |
| `005d25186000-005d25287000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30346]` |
| `005d2608a000-005d2618b000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30348]` |
| `005d2688c000-005d2698d000` | FilePage other | `rw-p` | 1028 | 24 | 24 | 8 | 2 | 0.78% | `[anon:stack:30355]` |
| `005d3efc6000-005d3f0c7000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30421]` |
| `005d3f0c9000-005d3f1ca000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30422]` |
| `005d3f2cf000-005d3f3d0000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:30424]` |
| `005d432ec000-005d433ed000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:31124]` |
| `005d433ef000-005d434f0000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 8 | 2 | 0.78% | `[anon:stack:31123]` |
| `00178f700000-00178f740000` | ark ts heap | `rw-p` | 256 | 8 | 8 | 4 | 1 | 1.56% | `[anon:ArkTS Heapread only space]` |
| `00178f900000-00178f940000` | ark ts heap | `rw-p` | 256 | 208 | 208 | 4 | 1 | 1.56% | `[anon:ArkTS Heapnon movable space]` |
| `00178fd00000-00178fd40000` | ark ts heap | `rw-p` | 256 | 252 | 252 | 4 | 1 | 1.56% | `[anon:ArkTS Heapnon movable space]` |
| `00178fd80000-00178fdc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapnon movable space]` |
| `00178fe00000-00178fe40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapnon movable space]` |
| `00178ff00000-00178ff40000` | ark ts heap | `r--p` | 256 | 8 | 0 | 4 | 1 | 1.56% | `[anon:ArkTS Heapread only space]` |
| `001e60700000-001e60780000` | ark ts heap | `rw-p` | 512 | 456 | 456 | 4 | 1 | 0.78% | `[anon:ArkTS Heaphuge object space]` |
| `002608dc0000-002608e00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260a280000-00260a300000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 4 | 1 | 0.78% | `[anon:ArkTS Heap]` |
| `00260a700000-00260a740000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heap]` |
| `00260a800000-00260a840000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260ae40000-00260af00000` | ark ts heap | `rw-p` | 768 | 768 | 768 | 4 | 1 | 0.52% | `[anon:ArkTS Heap]` |
| `00260b3c0000-00260b440000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 4 | 1 | 0.78% | `[anon:ArkTS Heapshared old space]` |
| `00260cfc0000-00260d000000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heap]` |
| `00260d440000-00260d480000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260eb00000-00260eb40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapsemi space]` |
| `00260ebc0000-00260ec00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260f080000-00260f0c0000` | ark ts heap | `rw-p` | 256 | 256 | 46 | 4 | 1 | 1.56% | `[anon:ArkTS Heapappspawn space]` |
| `00260f140000-00260f180000` | ark ts heap | `rw-p` | 256 | 256 | 18 | 4 | 1 | 1.56% | `[anon:ArkTS Heapappspawn space]` |
| `00260f340000-00260f380000` | ark ts heap | `rw-p` | 256 | 256 | 53 | 4 | 1 | 1.56% | `[anon:ArkTS Heapappspawn space]` |
| `00260f840000-00260f880000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260fa40000-00260fa80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heap]` |
| `00260fb40000-00260fb80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260fcc0000-00260fd00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heapshared old space]` |
| `00260fe00000-00260fe40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 4 | 1 | 1.56% | `[anon:ArkTS Heap]` |
| `00260fe40000-00260fe80000` | ark ts heap | `rw-p` | 256 | 48 | 24 | 4 | 1 | 1.56% | `[anon:ArkTS Heapshared appspawn space]` |
| `003800001000-003800002000` | FilePage other | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:partition_alloc]` |
| `003c00001000-003c00003000` | FilePage other | `rw-p` | 8 | 8 | 8 | 4 | 1 | 50.00% | `[anon:partition_alloc]` |
| `003c00201000-003c00203000` | FilePage other | `rw-p` | 8 | 8 | 8 | 4 | 1 | 50.00% | `[anon:partition_alloc]` |
| `003c00401000-003c00403000` | FilePage other | `rw-p` | 8 | 8 | 8 | 4 | 1 | 50.00% | `[anon:partition_alloc]` |
| `003c00601000-003c00603000` | FilePage other | `rw-p` | 8 | 8 | 8 | 4 | 1 | 50.00% | `[anon:partition_alloc]` |
| `003c00801000-003c00803000` | FilePage other | `rw-p` | 8 | 8 | 8 | 4 | 1 | 50.00% | `[anon:partition_alloc]` |
| `003c00a01000-003c00a03000` | FilePage other | `rw-p` | 8 | 8 | 8 | 4 | 1 | 50.00% | `[anon:partition_alloc]` |
| `003c00c01000-003c00c03000` | FilePage other | `rw-p` | 8 | 8 | 8 | 4 | 1 | 50.00% | `[anon:partition_alloc]` |
| `005a49a9c000-005a49a9d000` | FilePage other | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `[kshare]` |
| `005a49ab6000-005a49ab7000` | dev | `r--s` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/dev/__parameters__/u:object_r:i18n_param_tz_override:s0` |
| `005a49ab7000-005a49ab8000` | dev | `r--s` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/dev/__parameters__/u:object_r:time_param:s0` |
| `005a49ab8000-005a49ab9000` | dev | `r--s` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/dev/__parameters__/u:object_r:hitrace_param:s0` |
| `005a49abd000-005a49ac7000` | dev | `r--s` | 40 | 4 | 0 | 4 | 1 | 10.00% | `/dev/__parameters__/u:object_r:hilog_param:s0` |
| `005a49ad1000-005a49ad2000` | dev | `r--s` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/dev/__parameters__/u:object_r:hilog_private_param:s0` |
| `005a49b86000-005a49bcc000` | FilePage other | `r--s` | 280 | 4 | 0 | 4 | 1 | 1.43% | `/system/etc/zoneinfo/tzdata` |
| `005a4a0d1000-005a4a0d2000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libhitrace_meter.so` |
| `005a4a0d2000-005a4a0d3000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libhitrace_meter.so` |
| `005a4a0d3000-005a4a0df000` | native heap | `rw-p` | 48 | 32 | 1 | 4 | 1 | 8.33% | `[anon:native_heap:brk]` |
| `005a4a188000-005a4a189000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libasync_stack.z.so` |
| `005a4a189000-005a4a18a000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libasync_stack.z.so` |
| `005a4aa52000-005a4aa54000` | .so | `r--p` | 8 | 4 | 0 | 4 | 1 | 50.00% | `/system/lib64/platformsdk/libdfx_signalhandler.z.so` |
| `005a4aa54000-005a4aa55000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libdfx_signalhandler.z.so` |
| `005a4abb9000-005a4abba000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libc++.so` |
| `005a4ac3d000-005a4ac40000` | FilePage other | `rw-p` | 12 | 8 | 4 | 4 | 1 | 33.33% | `[anon:ArkTS Code:390359117451]` |
| `005a4ac40000-005a4ac41000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libhilog_encode.so` |
| `005a4ac44000-005a4ac45000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libhilog_encode.so` |
| `005a4ad0b000-005a4ad0d000` | .so | `r--p` | 8 | 8 | 0 | 4 | 1 | 50.00% | `/system/lib64/chipset-sdk-sp/libunwinder.z.so` |
| `005a4ad0d000-005a4ad0e000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libunwinder.z.so` |
| `005a4ad38000-005a4ad39000` | FilePage other | `rw-s` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[shmm]` |
| `005a4ad86000-005a4ad87000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libhilog_inner.so` |
| `005a4ad87000-005a4ad88000` | FilePage other | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:libhilog_inner.so.bss]` |
| `005a4ad88000-005a4ad98000` | native heap | `rw-p` | 64 | 64 | 3 | 4 | 1 | 6.25% | `[anon:native_heap:brk]` |
| `005a4adcd000-005a4adce000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libhitracechain.so` |
| `005a4adce000-005a4adcf000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libhitracechain.so` |
| `005a4adcf000-005a4add0000` | FilePage other | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:libhitracechain.so.bss]` |
| `005a4ae5d000-005a4ae5f000` | .so | `r--p` | 8 | 4 | 0 | 4 | 1 | 50.00% | `/system/lib64/chipset-sdk-sp/libbacktrace_local.so` |
| `005a4ae60000-005a4ae61000` | FilePage other | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:libbacktrace_local.so.bss]` |
| `005a4ae80000-005a4ae82000` | .so | `r--p` | 8 | 4 | 0 | 4 | 1 | 50.00% | `/system/lib64/platformsdk/libhilog.so` |
| `005a4ae85000-005a4ae86000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libhilog.so` |
| `005a4aec0000-005a4aec3000` | .so | `r--p` | 12 | 8 | 0 | 4 | 1 | 33.33% | `/system/lib64/chipset-sdk-sp/libsec_shared.z.so` |
| `005a4aecf000-005a4aed0000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libsec_shared.z.so` |
| `005a4aff7000-005a4aff8000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/ndk/libffrt.so` |
| `005a4b3dc000-005a4b3dd000` | FilePage other | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3e0000-005a4b3e1000` | FilePage other | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3e1000-005a4b3e2000` | FilePage other | `r--p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3e2000-005a4b3e3000` | FilePage other | `r--p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3f3000-005a4b3f4000` | FilePage other | `r--p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:cfi_shadow:musl]` |
| `005acc240000-005acc27f000` | .so | `r--p` | 252 | 160 | 3 | 4 | 1 | 1.59% | `/system/lib64/platformsdk/libwant.z.so` |
| `005acc2f9000-005acc2fa000` | FilePage other | `rw-p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `[anon:libwant.z.so.bss]` |
| `005acc3c6000-005acc3c7000` | GL | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libipc_single.z.so` |
| `005acc564000-005acc566000` | .so | `r--p` | 8 | 8 | 0 | 4 | 1 | 50.00% | `/system/lib64/platformsdk/libcesfwk_innerkits.z.so` |
| `005acc700000-005acc710000` | .so | `r--p` | 64 | 40 | 0 | 4 | 1 | 6.25% | `/system/lib64/chipset-sdk-sp/libhicollie.z.so` |
| `005acc740000-005acc741000` | FilePage other | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:libhicollie.z.so.bss]` |
| `005acc780000-005acc78c000` | .so | `r--p` | 48 | 36 | 0 | 4 | 1 | 8.33% | `/system/lib64/platformsdk/libbase.z.so` |
| `005accb65000-005accb66000` | FilePage other | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:libos_account_innerkits.z.so.bss]` |
| `005acce44000-005acce45000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/chipset-sdk-sp/libeventhandler.z.so` |
| `005acd1c0000-005acd1c6000` | .so | `r--p` | 24 | 12 | 0 | 4 | 1 | 16.67% | `/system/lib64/platformsdk/libzuri.z.so` |
| `005acd1d7000-005acd1d8000` | .so | `rw-p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libzuri.z.so` |
| `005acd291000-005acd292000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libipc_common.z.so` |
| `005acd292000-005acd293000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libipc_common.z.so` |
| `005acdecd000-005acdf4d000` | AnonPage other | `rw-p` | 512 | 8 | 8 | 4 | 1 | 0.78% | `(anonymous)` |
| `005ace90d000-005ace90f000` | Graph | `rw-p` | 8 | 4 | 4 | 4 | 1 | 50.00% | `/system/lib64/chipset-sdk-sp/libsurface.z.so` |
| `005ace90f000-005ace911000` | Graph | `rw-p` | 8 | 4 | 4 | 4 | 1 | 50.00% | `[anon:libsurface.z.so.bss]` |
| `005acecd5000-005acecd6000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libdatashare_consumer.z.so` |
| `005acf316000-005acf317000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libconsole.z.so` |
| `005acf580000-005acf918000` | GL | `r--p` | 3680 | 856 | 41 | 4 | 1 | 0.11% | `/system/lib64/librender_service_base.z.so` |
| `005acfea5000-005acfea8000` | FilePage other | `rw-p` | 12 | 8 | 0 | 4 | 1 | 33.33% | `[anon:ArkTS Code:/system/lib64/module/application/libcontext_napi.z.so_15376_1]` |
| `005acfede000-005acfeec000` | FilePage other | `rw-p` | 56 | 40 | 1 | 4 | 1 | 7.14% | `[anon:ArkTS Code:/system/lib64/module/libbuffer.z.so_85104_1]` |
| `005ad069c000-005ad06a7000` | FilePage other | `rw-p` | 44 | 40 | 4 | 4 | 1 | 9.09% | `[anon:ArkTS Code:/system/lib64/module/libutil.z.so_152960_1]` |
| `005ad0fe3000-005ad0fe4000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libace_napi.z.so` |
| `005ad102f000-005ad1031000` | .so | `r--p` | 8 | 8 | 0 | 4 | 1 | 50.00% | `/system/lib64/platformsdk/libuv.so` |
| `005ad1031000-005ad1032000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libuv.so` |
| `005ad103b000-005ad103f000` | dev | `rw-s` | 16 | 16 | 16 | 4 | 1 | 25.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad13d5000-005ad13d7000` | .so | `r--p` | 8 | 8 | 0 | 4 | 1 | 50.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_hdi_impl_v1_4.z.so` |
| `005ad13fc000-005ad13ff000` | dev | `rw-s` | 12 | 12 | 12 | 4 | 1 | 33.33% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad13ff000-005ad1400000` | dev | `rw-s` | 4 | 4 | 2 | 4 | 1 | 100.00% | `anon_inode:dev/ashmem/status_info_buffer` |
| `005ad1c9a000-005ad1c9b000` | FilePage other | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `[anon:libruntime.z.so.bss]` |
| `005ad1f4b000-005ad1f4c000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/ndk/libsync_fence.z.so` |
| `005ad1f4c000-005ad1f4d000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/ndk/libsync_fence.z.so` |
| `005ad2600000-005ad2646000` | .so | `r--p` | 280 | 112 | 9 | 4 | 1 | 1.43% | `/system/lib64/platformsdk/libmedia_foundation.z.so` |
| `005ad5788000-005ad5789000` | GL | `r--p` | 4 | 4 | 1 | 4 | 1 | 100.00% | `/system/lib64/libarkweb_glue_base.z.so` |
| `005ad5789000-005ad578a000` | GL | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libarkweb_glue_base.z.so` |
| `005ad5f46000-005ad5f47000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/libframe_ui_intf.z.so` |
| `005ad5f47000-005ad5f48000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libframe_ui_intf.z.so` |
| `005ad5f48000-005ad5f57000` | dev | `rw-s` | 60 | 60 | 60 | 4 | 1 | 6.67% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad65ce000-005ad65cf000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libtimer.z.so` |
| `005ad65cf000-005ad65f5000` | dev | `rw-s` | 152 | 152 | 152 | 4 | 1 | 2.63% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6744000-005ad6745000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libace_container_scope.z.so` |
| `005ad6745000-005ad6746000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libace_container_scope.z.so` |
| `005ad6746000-005ad677f000` | dev | `rw-s` | 228 | 228 | 228 | 4 | 1 | 1.75% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6e19000-005ad6e1a000` | .so | `rw-p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libdatashare_common.z.so` |
| `005ada69a000-005ada69b000` | GL | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libEGL.so` |
| `005ada754000-005ada755000` | GL | `r--p` | 4 | 4 | 1 | 4 | 1 | 100.00% | `/system/lib64/libGLESv3.so` |
| `005ada755000-005ada756000` | GL | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libGLESv3.so` |
| `005aded80000-005aded9d000` | GL | `r--p` | 116 | 36 | 4 | 4 | 1 | 3.45% | `/system/lib64/platformsdk/libaudio_renderer.z.so` |
| `005ae3345000-005ae33f9000` | .so | `rw-p` | 720 | 376 | 162 | 4 | 1 | 0.56% | `/system/lib64/platformsdk/libace_compatible.z.so` |
| `005ae33f9000-005ae34b9000` | FilePage other | `rw-p` | 768 | 316 | 286 | 4 | 1 | 0.52% | `[anon:libace_compatible.z.so.bss]` |
| `005ae466e000-005ae46bc000` | .so | `r-xp` | 312 | 312 | 49 | 4 | 1 | 1.28% | `/system/lib64/platformsdk/libaudio_policy_client.z.so` |
| `005ae5f60000-005ae7a38000` | GL | `r-xp` | 27488 | 608 | 113 | 4 | 1 | 0.01% | `/vendor/lib64/passthrough/indirect/libbishenggpucompiler_v210.so.15` |
| `005aee2c8000-005aee2c9000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libhdc_register.z.so` |
| `005af1628000-005af1726000` | dev | `r--p` | 1016 | 12 | 12 | 4 | 1 | 0.39% | `/dev/binder` |
| `005af192e000-005af1a2f000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 4 | 1 | 0.39% | `[anon:stack:30004]` |
| `005af91d6000-005af92d7000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 4 | 1 | 0.39% | `[anon:stack:30020]` |
| `005afb6ca000-005afb6cb000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/module/net/libhttp.z.so` |
| `005afb936000-005afb937000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/data/storage/el1/bundle/libs/arm64/libc++_shared.so` |
| `005afd440000-005afd449000` | .so | `r--p` | 36 | 16 | 0 | 4 | 1 | 11.11% | `/system/lib64/libnative_media_core.so` |
| `005afd4cb000-005afd4cc000` | .so | `r--p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libnative_media_vdec.so` |
| `005afd4cc000-005afd4cd000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libnative_media_vdec.so` |
| `005afe4cf000-005afe4d0000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/ndk/libohaudio.so` |
| `005afe5cd000-005afe695000` | .so | `r-xp` | 800 | 204 | 18 | 4 | 1 | 0.50% | `/system/lib64/libace_ndk.z.so` |
| `005b02200000-005b02202000` | .so | `r--p` | 8 | 8 | 0 | 4 | 1 | 50.00% | `/system/lib64/ndk/libhitrace_ndk.z.so` |
| `005b02202000-005b02203000` | .so | `r-xp` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/ndk/libhitrace_ndk.z.so` |
| `005b0420d000-005b04226000` | .so | `r-xp` | 100 | 88 | 88 | 4 | 1 | 4.00% | `/system/lib64/module/libadvertising.z.so` |
| `005b05404000-005b05405000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/ndk/libhilog_ndk.z.so` |
| `005b061c0000-005b061c1000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libnapi_base_context.z.so` |
| `005b061c1000-005b061c2000` | .so | `r-xp` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libnapi_base_context.z.so` |
| `005b061c2000-005b061c3000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libnapi_base_context.z.so` |
| `005b06600000-005b06603000` | .so | `r--p` | 12 | 8 | 0 | 4 | 1 | 33.33% | `/system/lib64/module/libhilog.z.so` |
| `005b06607000-005b06608000` | .so | `r--p` | 4 | 4 | 0 | 4 | 1 | 100.00% | `/system/lib64/module/libhilog.z.so` |
| `005b09fb2000-005b09fb3000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libsensor_client.z.so` |
| `005b09fd7000-005b09fd9000` | .so | `r--p` | 8 | 8 | 2 | 4 | 1 | 50.00% | `/system/lib64/platformsdk/libsensor_utils.z.so` |
| `005b09fd9000-005b09fda000` | .so | `rw-p` | 4 | 4 | 2 | 4 | 1 | 100.00% | `/system/lib64/platformsdk/libsensor_utils.z.so` |
| `005b0a005000-005b0a00c000` | .so | `r-xp` | 28 | 16 | 2 | 4 | 1 | 14.29% | `/system/lib64/platformsdk/libsensor_agent.z.so` |
| `005b0a06d000-005b0a06e000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/module/libsensor.z.so` |
| `005b0a12f000-005b0a130000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/module/libsettings.z.so` |
| `005b0a365000-005b0a37f000` | .so | `rw-p` | 104 | 8 | 4 | 4 | 1 | 3.85% | `/system/lib64/module/libutil.z.so` |
| `005b0a5b4000-005b0a5b5000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/module/libworker.z.so` |
| `005c4d63a000-005c4d73b000` | FilePage other | `rw-p` | 1028 | 44 | 44 | 4 | 1 | 0.39% | `[anon:stack:30058]` |
| `005c4f25c000-005c4f25d000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libaps_client.z.so` |
| `005c4f700000-005c4f707000` | .so | `r--p` | 28 | 28 | 1 | 4 | 1 | 14.29% | `/system/lib64/libframeawaresched.so` |
| `005c4f727000-005c4f728000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libframeawaresched.so` |
| `005c52749000-005c5284a000` | FilePage other | `rw-p` | 1028 | 24 | 24 | 4 | 1 | 0.39% | `[anon:stack:30074]` |
| `005c53cf9000-005c53dfa000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 4 | 1 | 0.39% | `[anon:stack:31122]` |
| `005d1ecd5000-005d1ecd6000` | .so | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/data/storage/el1/bundle/libs/arm64/libdanmu.so` |
| `005d1ef95000-005d1f096000` | FilePage other | `rw-p` | 1028 | 24 | 24 | 4 | 1 | 0.39% | `[anon:stack:30234]` |
| `005d1f35c000-005d1f35d000` | Graph | `rw-p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/libgameservice_graphic_plugin.z.so` |
| `005d1f35f000-005d1f460000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 4 | 1 | 0.39% | `[anon:stack:30237]` |
| `005d1f86e000-005d1f96f000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 4 | 1 | 0.39% | `[anon:stack:30242]` |
| `005d20580000-005d20681000` | FilePage other | `rw-p` | 1028 | 20 | 20 | 4 | 1 | 0.39% | `[anon:stack:30278]` |
| `005d2d180000-005d2d189000` | .so | `r--p` | 36 | 24 | 2 | 4 | 1 | 11.11% | `/system/lib64/ndk/libohcommonevent.so` |
| `005d2d193000-005d2d194000` | .so | `r--p` | 4 | 4 | 4 | 4 | 1 | 100.00% | `/system/lib64/ndk/libohcommonevent.so` |
| `005d38577000-005d3859f000` | .so | `r--p` | 160 | 160 | 160 | 4 | 1 | 2.50% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libffmpeg.so` |
| `005d385a0000-005d3867f000` | FilePage other | `rw-p` | 892 | 8 | 8 | 4 | 1 | 0.45% | `[anon:libffmpeg.so.bss]` |
| `005d38bef000-005d38bf1000` | GL | `rw-p` | 8 | 8 | 8 | 4 | 1 | 50.00% | `/system/lib64/libohos_adapter_glue_source.z.so` |
| `005d3a9e3000-005d3abe4000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 4 | 1 | 0.19% | `[anon:stack:30360]` |
| `005d3f1cc000-005d3f2cd000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 4 | 1 | 0.39% | `[anon:stack:30423]` |
| `005d3f3d0000-005d3ffd0000` | native heap | `rw-p` | 12288 | 152 | 152 | 4 | 1 | 0.03% | `[anon:native_heap:jemalloc]` |
| `005d438ec000-005d439ed000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 4 | 1 | 0.39% | `[anon:stack:30491]` |
| `005d439ef000-005d43af0000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 4 | 1 | 0.39% | `[anon:stack:30492]` |
| `005d43af2000-005d43bf3000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 4 | 1 | 0.39% | `[anon:stack:30493]` |
| `005d43bf5000-005d43cf6000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 4 | 1 | 0.39% | `[anon:stack:30494]` |
| `000000040000-000000080000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Object Space]` |
| `000000080000-0000000c0000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Non Movable Space]` |
| `0000000c0000-000000100000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Object Space]` |
| `000000100000-000020040000` | AnonPage other | `rw-p` | 523520 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `001760000000-00178f5c0000` | guard | `---p` | 775936 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00178f680000-00178f700000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00178f880000-00178f900000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00178f940000-00178fa00000` | guard | `---p` | 768 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00178fa40000-00178fac0000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00178fb00000-00178fb40000` | ark ts heap | `rw-p` | 256 | 40 | 40 | 0 | 0 | 0.00% | `[anon:ArkTS Heapnon movable space]` |
| `00178fb40000-00178fb80000` | ark ts heap | `rw-p` | 256 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Heapnon movable space]` |
| `00178fb80000-00178fbc0000` | ark ts heap | `rw-p` | 256 | 144 | 144 | 0 | 0 | 0.00% | `[anon:ArkTS Heapnon movable space]` |
| `00178fbc0000-00178fc00000` | ark ts heap | `rw-p` | 256 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Heapread only space]` |
| `00178fc00000-00178fc40000` | ark ts heap | `rw-p` | 256 | 240 | 240 | 0 | 0 | 0.00% | `[anon:ArkTS Heapnon movable space]` |
| `00178fc40000-00178fc80000` | ark ts heap | `rw-p` | 256 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Heapread only space]` |
| `00178fc80000-00178fcc0000` | ark ts heap | `rw-p` | 256 | 240 | 240 | 0 | 0 | 0.00% | `[anon:ArkTS Heapnon movable space]` |
| `00178fdc0000-00178fe00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapnon movable space]` |
| `001e60100000-001e60180000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `001e60180000-001e60300000` | ark ts heap | `rw-p` | 1536 | 1304 | 1304 | 0 | 0 | 0.00% | `[anon:ArkTS Heaphuge object space]` |
| `001e60300000-001e60400000` | guard | `---p` | 1024 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `001e60480000-001e60700000` | guard | `---p` | 2560 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `001e60780000-001e80000000` | guard | `---p` | 516608 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `0025f0000000-002608b80000` | guard | `---p` | 404992 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002608b80000-002608bc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `002608c40000-002608c80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002608d00000-002608d40000` | ark ts heap | `rw-p` | 256 | 144 | 144 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `002608e00000-002608e80000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002608e80000-002608f00000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609000000-002609040000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609040000-002609080000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609080000-0026091c0000` | guard | `---p` | 1280 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `0026091c0000-002609200000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609200000-002609240000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609240000-002609280000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609280000-0026092c0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609300000-002609340000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `002609340000-002609380000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609380000-0026093c0000` | ark ts heap | `rw-p` | 256 | 252 | 252 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609400000-002609500000` | guard | `---p` | 1024 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609500000-002609540000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609540000-002609580000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609580000-0026095c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `0026095c0000-002609600000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609600000-002609640000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609640000-0026096c0000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `0026096c0000-002609700000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609700000-002609740000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609740000-0026097c0000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `0026097c0000-002609800000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609800000-002609840000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609840000-002609880000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `0026098c0000-002609940000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609940000-002609980000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609980000-0026099c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `0026099c0000-002609a00000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609a40000-002609a80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609a80000-002609b40000` | guard | `---p` | 768 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609b40000-002609b80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609b80000-002609bc0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609bc0000-002609c00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609c00000-002609c80000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609c80000-002609cc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609cc0000-002609d40000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609d40000-002609d80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609d80000-002609dc0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609dc0000-002609e00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609e00000-002609e40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609e40000-002609ec0000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609ec0000-002609f40000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `002609f40000-002609f80000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609f80000-002609fc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `002609fc0000-00260a040000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a040000-00260a080000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260a080000-00260a180000` | guard | `---p` | 1024 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a240000-00260a280000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a300000-00260a380000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260a400000-00260a440000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a440000-00260a480000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a480000-00260a4c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260a4c0000-00260a500000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a500000-00260a540000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260a580000-00260a5c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260a5c0000-00260a700000` | guard | `---p` | 1280 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a740000-00260a800000` | guard | `---p` | 768 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a840000-00260a880000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a880000-00260a8c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260a8c0000-00260a900000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260a900000-00260a940000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260a980000-00260a9c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260a9c0000-00260aa40000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260aac0000-00260ab00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ab80000-00260abc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260abc0000-00260ac00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260ac00000-00260acc0000` | guard | `---p` | 768 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260acc0000-00260ad00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ad00000-00260ad80000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ae00000-00260ae40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260af40000-00260af80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260afc0000-00260b000000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260b040000-00260b080000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b080000-00260b0c0000` | ark ts heap | `rw-p` | 256 | 32 | 32 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260b0c0000-00260b100000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b100000-00260b140000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260b140000-00260b1c0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b1c0000-00260b200000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b200000-00260b240000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b340000-00260b3c0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260b540000-00260b580000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b580000-00260b5c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b5c0000-00260b600000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260b600000-00260b640000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260b640000-00260b680000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b680000-00260b6c0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260b6c0000-00260b740000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b740000-00260b780000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260b780000-00260b7c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b7c0000-00260b840000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b840000-00260b880000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b8c0000-00260b980000` | ark ts heap | `rw-p` | 768 | 768 | 768 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260b980000-00260bac0000` | guard | `---p` | 1280 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260bb00000-00260bb40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260bc00000-00260bc40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260bc80000-00260bcc0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260bcc0000-00260bd00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260bd00000-00260bd40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260bd40000-00260bd80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260bd80000-00260bdc0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260bdc0000-00260be00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260be00000-00260be40000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260bf40000-00260bf80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260bf80000-00260c000000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c000000-00260c040000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c100000-00260c140000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260c140000-00260c180000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c200000-00260c280000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c280000-00260c300000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c300000-00260c3c0000` | ark ts heap | `rw-p` | 768 | 768 | 768 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260c3c0000-00260c400000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c400000-00260c440000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c480000-00260c500000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c500000-00260c540000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260c540000-00260c580000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c580000-00260c600000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c640000-00260c680000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c680000-00260c6c0000` | ark ts heap | `rw-p` | 256 | 152 | 152 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260c6c0000-00260c700000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260c780000-00260c7c0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260c7c0000-00260c8c0000` | ark ts heap | `rw-p` | 1024 | 1024 | 1024 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c8c0000-00260c900000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c900000-00260c940000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260c940000-00260c9c0000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260c9c0000-00260ca00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ca00000-00260ca40000` | ark ts heap | `rw-p` | 256 | 128 | 128 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260ca40000-00260ca80000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260cac0000-00260cb00000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260cb00000-00260cb40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260cb40000-00260cb80000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260cb80000-00260cbc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260cc00000-00260cc40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260cc40000-00260cc80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260cd40000-00260cd80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260cd80000-00260cdc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260cdc0000-00260ce00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ce00000-00260ce40000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260ce40000-00260ce80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ce80000-00260cec0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260cec0000-00260cf00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260cf00000-00260cf40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260cf40000-00260cf80000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260cf80000-00260cfc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d000000-00260d040000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d040000-00260d080000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d080000-00260d0c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d0c0000-00260d100000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d100000-00260d140000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d140000-00260d180000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d180000-00260d1c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d1c0000-00260d200000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d200000-00260d240000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d240000-00260d280000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d280000-00260d2c0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d2c0000-00260d300000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d300000-00260d340000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d340000-00260d380000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d380000-00260d3c0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d3c0000-00260d400000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d400000-00260d440000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d480000-00260d4c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d4c0000-00260d540000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d5c0000-00260d600000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d600000-00260d680000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d680000-00260d6c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d6c0000-00260d780000` | guard | `---p` | 768 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d780000-00260d7c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d7c0000-00260d800000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d800000-00260d940000` | guard | `---p` | 1280 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d940000-00260d980000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260d980000-00260d9c0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260d9c0000-00260da40000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260da40000-00260da80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260da80000-00260db00000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260db00000-00260db40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260db40000-00260dc40000` | guard | `---p` | 1024 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260dc40000-00260dc80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260dc80000-00260dcc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260dd80000-00260ddc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ddc0000-00260de00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260dec0000-00260df00000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260df00000-00260df40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260df80000-00260e000000` | ark ts heap | `rw-p` | 512 | 508 | 508 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e000000-00260e040000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e040000-00260e080000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260e080000-00260e0c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e0c0000-00260e140000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e180000-00260e1c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e1c0000-00260e200000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e200000-00260e280000` | guard | `---p` | 512 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e340000-00260e380000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e380000-00260e3c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e3c0000-00260e400000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e400000-00260e440000` | ark ts heap | `rw-p` | 256 | 96 | 96 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e440000-00260e480000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e480000-00260e4c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e4c0000-00260e500000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e500000-00260e540000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e540000-00260e580000` | ark ts heap | `rw-p` | 256 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260e580000-00260e5c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e780000-00260e7c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e7c0000-00260e800000` | ark ts heap | `rw-p` | 256 | 80 | 80 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260e800000-00260e840000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e840000-00260e880000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e880000-00260e900000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260e900000-00260e940000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260e940000-00260e9c0000` | ark ts heap | `rw-p` | 512 | 512 | 512 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ea40000-00260ea80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260eb40000-00260eb80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260eb80000-00260ebc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260ec00000-00260ec40000` | ark ts heap | `rw-p` | 256 | 216 | 216 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260ec40000-00260ec80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ec80000-00260ecc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260ecc0000-00260ed00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260ed00000-00260ed40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260f000000-00260f040000` | ark ts heap | `rw-p` | 256 | 256 | 18 | 0 | 0 | 0.00% | `[anon:ArkTS Heapappspawn space]` |
| `00260f0c0000-00260f100000` | ark ts heap | `rw-p` | 256 | 256 | 34 | 0 | 0 | 0.00% | `[anon:ArkTS Heapappspawn space]` |
| `00260f180000-00260f1c0000` | ark ts heap | `rw-p` | 256 | 256 | 34 | 0 | 0 | 0.00% | `[anon:ArkTS Heapappspawn space]` |
| `00260f2c0000-00260f300000` | ark ts heap | `rw-p` | 256 | 256 | 46 | 0 | 0 | 0.00% | `[anon:ArkTS Heapappspawn space]` |
| `00260f400000-00260f440000` | ark ts heap | `rw-p` | 256 | 216 | 216 | 0 | 0 | 0.00% | `[anon:ArkTS Heapsemi space]` |
| `00260f440000-00260f480000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260f480000-00260f4c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260f4c0000-00260f500000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260f500000-00260f540000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260f540000-00260f580000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260f580000-00260f5c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260f5c0000-00260f600000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260f640000-00260f680000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260f740000-00260f780000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260f7c0000-00260f800000` | ark ts heap | `rw-p` | 256 | 160 | 160 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260f880000-00260f8c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260f900000-00260f940000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260f940000-00260f980000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260f980000-00260f9c0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260fa00000-00260fa40000` | ark ts heap | `rw-p` | 256 | 32 | 12 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared appspawn space]` |
| `00260fac0000-00260fb00000` | ark ts heap | `rw-p` | 256 | 252 | 252 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260fb80000-00260fbc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260fbc0000-00260fc00000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260fc40000-00260fc80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260fc80000-00260fcc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260fd00000-00260fd40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260fd80000-00260fdc0000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared old space]` |
| `00260fe80000-00260fec0000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260fec0000-00260ff00000` | guard | `---p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260ff00000-00260ff40000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260ff40000-00260ff80000` | ark ts heap | `rw-p` | 256 | 256 | 256 | 0 | 0 | 0.00% | `[anon:ArkTS Heap]` |
| `00260ff80000-00260ffc0000` | ark ts heap | `rw-p` | 256 | 176 | 63 | 0 | 0 | 0.00% | `[anon:ArkTS Heapshared appspawn space]` |
| `003800000000-003800001000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003800002000-003800004000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003800174000-003800201000` | guard | `---p` | 564 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003800201000-003800202000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003800202000-003800204000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003800254000-003c00001000` | guard | `---p` | 16774836 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00003000-003c00004000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c001fc000-003c00201000` | guard | `---p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00203000-003c00204000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c003f4000-003c00401000` | guard | `---p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00403000-003c00404000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c005f8000-003c00601000` | guard | `---p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00603000-003c00604000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c007c0000-003c00801000` | guard | `---p` | 260 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00803000-003c00804000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c009fc000-003c00a01000` | guard | `---p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00a03000-003c00a04000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00bf8000-003c00c01000` | guard | `---p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00c03000-003c00c04000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `003c00cd4000-004000000000` | guard | `---p` | 16764080 | 0 | 0 | 0 | 0 | 0.00% | `[anon:partition_alloc]` |
| `0055e5a24000-0055e5a2f000` | FilePage other | `r--p` | 44 | 44 | 1 | 0 | 0 | 0.00% | `/system/bin/appspawn` |
| `0055e5a2f000-0055e5a42000` | FilePage other | `r-xp` | 76 | 72 | 2 | 0 | 0 | 0.00% | `/system/bin/appspawn` |
| `0055e5a42000-0055e5a44000` | FilePage other | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/bin/appspawn` |
| `0055e5a44000-0055e5a45000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/bin/appspawn` |
| `005840759000-00584075a000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `00584075a000-005840763000` | native heap | `rw-p` | 36 | 36 | 36 | 0 | 0 | 0.00% | `[anon:native_heap:meta]` |
| `005a49a9b000-005a49a9c000` | AnonPage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005a49aa0000-005a49aa1000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49aa1000-005a49ab5000` | dev | `r--s` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/param_selinux` |
| `005a49ab5000-005a49ab6000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:musl_param:s0` |
| `005a49ab9000-005a49abb000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49abb000-005a49abc000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:versiontype_param:s0` |
| `005a49abc000-005a49abd000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:hook_param:s0` |
| `005a49ac7000-005a49ad1000` | native heap | `rw-p` | 40 | 40 | 2 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49ad2000-005a49ad4000` | native heap | `rw-p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49ad4000-005a49ad6000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005a49ad6000-005a49add000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:683]` |
| `005a49add000-005a49af5000` | native heap | `rw-p` | 96 | 96 | 12 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49af5000-005a49af6000` | dev | `r--s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:const_i18n_param:s0` |
| `005a49af6000-005a49af7000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:debug_param:s0` |
| `005a49af7000-005a49af8000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:arkcompiler_param:s0` |
| `005a49af8000-005a49af9000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:devinfo_type_param:s0` |
| `005a49af9000-005a49afa000` | native heap | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49afa000-005a49afc000` | native heap | `rw-p` | 8 | 8 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49afc000-005a49afd000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:arkui_param:s0` |
| `005a49afd000-005a49b02000` | native heap | `rw-p` | 20 | 20 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b02000-005a49b03000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:ark_writeable_param:s0` |
| `005a49b03000-005a49b0d000` | native heap | `rw-p` | 40 | 40 | 9 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b0d000-005a49b2d000` | dev | `r--s` | 128 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:develop_private_param:s0` |
| `005a49b2d000-005a49b2f000` | native heap | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b2f000-005a49b30000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/app/ability/libabilitystage.z.so_15392_1]` |
| `005a49b30000-005a49b34000` | native heap | `rw-p` | 16 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b34000-005a49b3d000` | native heap | `rw-p` | 36 | 36 | 5 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b3d000-005a49b3e000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:hichecker_writable_param:s0` |
| `005a49b3e000-005a49b61000` | native heap | `rw-p` | 140 | 136 | 15 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b61000-005a49b67000` | native heap | `rw-p` | 24 | 12 | 12 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b67000-005a49b68000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:web_private_param:s0` |
| `005a49b68000-005a49b6a000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b6a000-005a49b75000` | native heap | `rw-p` | 44 | 36 | 5 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b75000-005a49b7e000` | native heap | `rw-p` | 36 | 36 | 5 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b7e000-005a49b7f000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/global/resmgr.abc]` |
| `005a49b7f000-005a49b80000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49b80000-005a49b81000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libconfigpolicy_util.z.so` |
| `005a49b81000-005a49b83000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libconfigpolicy_util.z.so` |
| `005a49b83000-005a49b85000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libconfigpolicy_util.z.so` |
| `005a49b85000-005a49b86000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libconfigpolicy_util.z.so` |
| `005a49bcc000-005a49bfe000` | native heap | `rw-p` | 200 | 192 | 10 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49bfe000-005a49c00000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a49c00000-005a49c01000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005a49e00000-005a49e01000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005a4a001000-005a4a040000` | native heap | `rw-p` | 252 | 240 | 28 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a040000-005a4a043000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libcjson.z.so` |
| `005a4a043000-005a4a049000` | .so | `r-xp` | 24 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libcjson.z.so` |
| `005a4a049000-005a4a04a000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libcjson.z.so` |
| `005a4a04a000-005a4a04b000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libcjson.z.so` |
| `005a4a04b000-005a4a07f000` | native heap | `rw-p` | 208 | 208 | 26 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a07f000-005a4a080000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:390359113583]` |
| `005a4a080000-005a4a081000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_helper.z.so` |
| `005a4a081000-005a4a082000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_helper.z.so` |
| `005a4a082000-005a4a083000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_helper.z.so` |
| `005a4a083000-005a4a084000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_helper.z.so` |
| `005a4a084000-005a4a0c0000` | native heap | `rw-p` | 240 | 232 | 17 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a0df000-005a4a0e1000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a0e1000-005a4a0fe000` | native heap | `rw-p` | 116 | 112 | 21 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a0fe000-005a4a100000` | native heap | `rw-p` | 8 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a100000-005a4a107000` | .so | `r--p` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdfx_dumpcatcher.z.so` |
| `005a4a107000-005a4a116000` | .so | `r-xp` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdfx_dumpcatcher.z.so` |
| `005a4a116000-005a4a117000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdfx_dumpcatcher.z.so` |
| `005a4a117000-005a4a118000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdfx_dumpcatcher.z.so` |
| `005a4a118000-005a4a119000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libdfx_dumpcatcher.z.so.bss]` |
| `005a4a119000-005a4a11f000` | native heap | `rw-p` | 24 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a11f000-005a4a127000` | native heap | `rw-p` | 32 | 20 | 20 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a127000-005a4a13e000` | native heap | `rw-p` | 92 | 72 | 11 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a13e000-005a4a140000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkstepper.abc]` |
| `005a4a140000-005a4a145000` | .so | `r--p` | 20 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsystemparam.z.so` |
| `005a4a145000-005a4a146000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsystemparam.z.so` |
| `005a4a146000-005a4a150000` | .so | `r-xp` | 40 | 36 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsystemparam.z.so` |
| `005a4a150000-005a4a151000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsystemparam.z.so` |
| `005a4a151000-005a4a152000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsystemparam.z.so` |
| `005a4a152000-005a4a153000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libsystemparam.z.so.bss]` |
| `005a4a153000-005a4a180000` | native heap | `rw-p` | 180 | 160 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a180000-005a4a183000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libasync_stack.z.so` |
| `005a4a18a000-005a4a200000` | native heap | `rw-p` | 472 | 464 | 40 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4a200000-005a4a201000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005a4a600000-005a4a601000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005a4a601000-005a4a801000` | dev | `r--s` | 2048 | 64 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/param_sec_dac` |
| `005a4a801000-005a4aa01000` | dev | `r--s` | 2048 | 72 | 2 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:devinfo_public_param:s0` |
| `005a4aa01000-005a4aa40000` | native heap | `rw-p` | 252 | 232 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aa40000-005a4aa46000` | .so | `r--p` | 24 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdfx_signalhandler.z.so` |
| `005a4aa55000-005a4aa59000` | FilePage other | `rw-p` | 16 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libdfx_signalhandler.z.so.bss]` |
| `005a4aa59000-005a4aa69000` | native heap | `rw-p` | 64 | 64 | 3 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aa69000-005a4aa6b000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkcolumnsplit.abc]` |
| `005a4aa6b000-005a4aa7f000` | native heap | `rw-p` | 80 | 80 | 19 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aa7f000-005a4aa80000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkflowitem.abc]` |
| `005a4abc1000-005a4abfd000` | native heap | `rw-p` | 240 | 240 | 28 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4abfd000-005a4abfe000` | native heap | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4abfe000-005a4ac00000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkrowsplit.abc]` |
| `005a4ac38000-005a4ac39000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libutils.z.so` |
| `005a4ac39000-005a4ac3d000` | native heap | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ac45000-005a4ac46000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhilog_encode.so` |
| `005a4ac46000-005a4ac5a000` | native heap | `rw-p` | 80 | 72 | 11 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ac5a000-005a4ac5d000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkrating.abc]` |
| `005a4ac5d000-005a4ac5e000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ac5e000-005a4ac7a000` | native heap | `rw-p` | 112 | 112 | 21 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ac7a000-005a4ac7f000` | FilePage other | `rw-p` | 20 | 4 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkcheckbox.abc]` |
| `005a4ac7f000-005a4ac80000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkmenuitemgroup.abc]` |
| `005a4ac80000-005a4ac84000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libstack_printer.z.so` |
| `005a4ac84000-005a4ac8e000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libstack_printer.z.so` |
| `005a4ac8e000-005a4ac8f000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libstack_printer.z.so` |
| `005a4ac8f000-005a4ac90000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libstack_printer.z.so` |
| `005a4ac90000-005a4ac91000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libstack_printer.z.so.bss]` |
| `005a4ac91000-005a4acb9000` | native heap | `rw-p` | 160 | 160 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4acb9000-005a4acbd000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkcheckboxgroup.abc]` |
| `005a4acbd000-005a4acbf000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4acbf000-005a4acc0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/base_sdk.abc` |
| `005a4acc0000-005a4acd3000` | .so | `r--p` | 76 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libunwinder.z.so` |
| `005a4ad0e000-005a4ad10000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libunwinder.z.so.bss]` |
| `005a4ad10000-005a4ad38000` | native heap | `rw-p` | 160 | 160 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ad39000-005a4ad3a000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ad3a000-005a4ad3e000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkgauge.abc]` |
| `005a4ad3e000-005a4ad3f000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005a4ad3f000-005a4ad40000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/shared_memory/94CD5B6F2C41FAE18F96D8F59925CC86` |
| `005a4ad98000-005a4ad99000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:ark_profile:s0` |
| `005a4ad99000-005a4ad9a000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:update_updater_param:s0` |
| `005a4ad9a000-005a4ad9c000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkfolderstack.abc]` |
| `005a4ad9c000-005a4ad9d000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/resource.abc` |
| `005a4ad9d000-005a4ada9000` | native heap | `rw-p` | 48 | 48 | 17 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ada9000-005a4adaa000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/app/appstartup/libstartupconfigentry_napi.z.so_21400_2]` |
| `005a4adaa000-005a4adb2000` | native heap | `rw-p` | 32 | 32 | 1 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4adb2000-005a4adbc000` | dev | `r--s` | 40 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:hiviewdfx_hiview_param:s0` |
| `005a4adbc000-005a4adc0000` | native heap | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4adc0000-005a4adc5000` | .so | `r--p` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhitracechain.so` |
| `005a4add0000-005a4adfe000` | FilePage other | `rw-p` | 184 | 132 | 44 | 0 | 0 | 0.00% | `/system/etc/abc/framework/jsEnumStyle.abc` |
| `005a4adfe000-005a4ae00000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkstepperitem.abc]` |
| `005a4ae00000-005a4ae05000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdfx_procinfo.z.so` |
| `005a4ae05000-005a4ae0e000` | .so | `r-xp` | 36 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdfx_procinfo.z.so` |
| `005a4ae0e000-005a4ae0f000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdfx_procinfo.z.so` |
| `005a4ae0f000-005a4ae10000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdfx_procinfo.z.so` |
| `005a4ae10000-005a4ae21000` | FilePage other | `rw-p` | 68 | 36 | 1 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/uicontext.abc]` |
| `005a4ae21000-005a4ae2c000` | FilePage other | `rw-p` | 44 | 28 | 1 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/arktheme.abc]` |
| `005a4ae2c000-005a4ae2f000` | GL | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arksymbolglyph.abc]` |
| `005a4ae2f000-005a4ae33000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ae33000-005a4ae38000` | FilePage other | `rw-p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkradio.abc]` |
| `005a4ae38000-005a4ae40000` | native heap | `rw-p` | 32 | 32 | 1 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ae40000-005a4ae47000` | .so | `r--p` | 28 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbacktrace_local.so` |
| `005a4ae5f000-005a4ae60000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbacktrace_local.so` |
| `005a4ae61000-005a4ae71000` | FilePage other | `rw-p` | 64 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arksearch.abc]` |
| `005a4ae71000-005a4ae79000` | native heap | `rw-p` | 32 | 32 | 1 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4ae79000-005a4ae7d000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arktimepicker.abc]` |
| `005a4ae7d000-005a4ae80000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkmenuitem.abc]` |
| `005a4ae86000-005a4ae87000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhilog.so` |
| `005a4ae87000-005a4ae91000` | FilePage other | `rw-p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkricheditor.abc]` |
| `005a4ae91000-005a4ae99000` | FilePage other | `rw-p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkslider.abc]` |
| `005a4ae99000-005a4aea1000` | native heap | `rw-p` | 32 | 32 | 1 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aea1000-005a4aea3000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkhyperlink.abc]` |
| `005a4aea3000-005a4aea4000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/@hms.hds.hdsPhysics2d.abc` |
| `005a4aea4000-005a4aea9000` | native heap | `rw-p` | 20 | 20 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aea9000-005a4aeb0000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkalphabetindexer.abc]` |
| `005a4aeb0000-005a4aeb4000` | native heap | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aeb4000-005a4aeb8000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arksidebarcontainer.abc]` |
| `005a4aeb8000-005a4aec0000` | native heap | `rw-p` | 32 | 32 | 1 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aed0000-005a4aed1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsec_shared.z.so` |
| `005a4aed1000-005a4aed8000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkwaterflow.abc]` |
| `005a4aed8000-005a4aedd000` | FilePage other | `rw-p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkcalendarpicker.abc]` |
| `005a4aedd000-005a4aee1000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkmenu.abc]` |
| `005a4aee1000-005a4aeed000` | native heap | `rw-p` | 48 | 32 | 1 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aeed000-005a4aef1000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arkmarquee.abc]` |
| `005a4aef1000-005a4aef5000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aef5000-005a4aef8000` | dev | `r--s` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:samgr_writable_param:s0` |
| `005a4aef8000-005a4aef9000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/app/appstartup/libstartuptask_napi.z.so_21368_1]` |
| `005a4aef9000-005a4aefa000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4aefa000-005a4aefe000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/@hms.hds.hdsDrawable.abc` |
| `005a4aefe000-005a4aeff000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/@hms.hds.symbolRegister.abc` |
| `005a4aeff000-005a4af00000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/Permission_Request_Result.abc` |
| `005a4af00000-005a4af0a000` | .so | `r--p` | 40 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/liblzma.z.so` |
| `005a4af0a000-005a4af2e000` | .so | `r-xp` | 144 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/liblzma.z.so` |
| `005a4af2e000-005a4af2f000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/liblzma.z.so` |
| `005a4af2f000-005a4af30000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/liblzma.z.so` |
| `005a4af30000-005a4af39000` | FilePage other | `rw-p` | 36 | 4 | 0 | 0 | 0 | 0.00% | `[anon:liblzma.z.so.bss]` |
| `005a4af39000-005a4af3d000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/@ohos.multimedia.MovingPhotoView.abc` |
| `005a4af3d000-005a4af40000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/@ohos.test.PerfTest.abc` |
| `005a4b009000-005a4b011000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4b011000-005a4b013000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005a4b013000-005a4b01a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30002]` |
| `005a4b01a000-005a4b01b000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4b01b000-005a4b01e000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/DataShareExtensionAbilityAni.abc` |
| `005a4b01e000-005a4b020000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/DataShareResultSetAni.abc` |
| `005a4b020000-005a4b021000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_ability_abc.abc` |
| `005a4b021000-005a4b025000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4b025000-005a4b027000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005a4b027000-005a4b02e000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30003]` |
| `005a4b02e000-005a4b030000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005a4b030000-005a4b037000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30004]` |
| `005a4b040000-005a4b04c000` | .so | `r--p` | 48 | 36 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbegetutil.z.so` |
| `005a4b04c000-005a4b065000` | .so | `r-xp` | 100 | 92 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbegetutil.z.so` |
| `005a4b065000-005a4b067000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbegetutil.z.so` |
| `005a4b067000-005a4b068000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbegetutil.z.so` |
| `005a4b068000-005a4b06a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005a4b06a000-005a4b071000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30008]` |
| `005a4b071000-005a4b073000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005a4b073000-005a4b07a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30006]` |
| `005a4b07a000-005a4b07e000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/Metaball.abc` |
| `005a4b07e000-005a4b080000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_delegator_ability_monitor_abc.abc` |
| `005a4b080000-005a4b087000` | .so | `r--p` | 28 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhisysevent.z.so` |
| `005a4b087000-005a4b098000` | .so | `r-xp` | 68 | 68 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhisysevent.z.so` |
| `005a4b098000-005a4b09a000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhisysevent.z.so` |
| `005a4b09a000-005a4b09b000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhisysevent.z.so` |
| `005a4b09b000-005a4b0a3000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005a4b0a3000-005a4b0a4000` | FilePage other | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/hiappevent/databases/appevent.db-dwr` |
| `005a4b0a4000-005a4b0aa000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/SelectionPanel.abc` |
| `005a4b0aa000-005a4b0b4000` | FilePage other | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_access_ctrl.abc` |
| `005a4b0b4000-005a4b0b8000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_application.abc` |
| `005a4b0b8000-005a4b0be000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_delegator_abc.abc` |
| `005a4b0be000-005a4b0bf000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_delegator_application_testRunner_abc.abc` |
| `005a4b0bf000-005a4b0c0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_delegator_args_abc.abc` |
| `005a4b0c0000-005a4b0c2000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libclang_rt.ubsan_minimal.so` |
| `005a4b0c2000-005a4b0c4000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libclang_rt.ubsan_minimal.so` |
| `005a4b0c4000-005a4b0c5000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libclang_rt.ubsan_minimal.so` |
| `005a4b0c5000-005a4b0c6000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libclang_rt.ubsan_minimal.so` |
| `005a4b0c6000-005a4b0ec000` | FilePage other | `r--p` | 152 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/@ohos.UiTest.abc` |
| `005a4b0ec000-005a4b0ed000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_delegator_registry_abc.abc` |
| `005a4b0ed000-005a4b0ee000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_first_frame_state_data_abc.abc` |
| `005a4b0ee000-005a4b0ef000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_first_frame_state_observer_abc.abc` |
| `005a4b0ef000-005a4b0f0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_foreground_state_observer_abc.abc` |
| `005a4b0f0000-005a4b0f4000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_info.abc` |
| `005a4b0f4000-005a4b0f6000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_AbilityRunningInfo_abc.abc` |
| `005a4b0f6000-005a4b0f7000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_abc.abc` |
| `005a4b0f7000-005a4b0fe000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_constant_abc.abc` |
| `005a4b0fe000-005a4b100000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_context_constant_abc.abc` |
| `005a4b100000-005a4b103000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libfaultloggerd.z.so` |
| `005a4b103000-005a4b108000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libfaultloggerd.z.so` |
| `005a4b108000-005a4b109000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libfaultloggerd.z.so` |
| `005a4b109000-005a4b10a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libfaultloggerd.z.so` |
| `005a4b10a000-005a4b3b9000` | guard | `---p` | 2748 | 0 | 0 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3b9000-005a4b3ba000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3ba000-005a4b3dc000` | guard | `---p` | 136 | 0 | 0 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3dd000-005a4b3e0000` | guard | `---p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3e3000-005a4b3ec000` | guard | `---p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3ec000-005a4b3ed000` | FilePage other | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3ed000-005a4b3f2000` | guard | `---p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3f2000-005a4b3f3000` | FilePage other | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3f4000-005a4b3f5000` | FilePage other | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005a4b3f5000-005acb10a000` | guard | `---p` | 2094164 | 0 | 0 | 0 | 0 | 0.00% | `[anon:cfi_shadow:musl]` |
| `005acb10a000-005acb10d000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_dialogRequest_abc.abc` |
| `005acb10d000-005acb10e000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_lifecycle_callback_abc.abc` |
| `005acb10e000-005acb115000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_manager.abc` |
| `005acb115000-005acb11a000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_mission_manager_abc.abc` |
| `005acb11a000-005acb11b000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_result_abc.abc` |
| `005acb11b000-005acb11c000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_stage_abc.abc` |
| `005acb11c000-005acb11d000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_stage_context_abc.abc` |
| `005acb11d000-005acb11e000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_stage_monitor_abc.abc` |
| `005acb11e000-005acb11f000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_start_callback_abc.abc` |
| `005acb11f000-005acb120000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_state_data_abc.abc` |
| `005acb120000-005acb122000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_system_configuration_updated_callback_abc.abc` |
| `005acb122000-005acb123000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ability_utils_abc.abc` |
| `005acb123000-005acb124000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_action_extension_ability_abc.abc` |
| `005acb124000-005acb132000` | FilePage other | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_app_manager_abc.abc` |
| `005acb132000-005acb133000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_app_state_data_abc.abc` |
| `005acb133000-005acb138000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_application_context_abc.abc` |
| `005acb138000-005acb139000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_application_state_change_callback_abc.abc` |
| `005acb139000-005acb13a000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_fill_extension_ability_abc.abc` |
| `005acb13a000-005acb13c000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_fill_extension_context_abc.abc` |
| `005acb13c000-005acb13d000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_fill_manager_abc.abc` |
| `005acb13d000-005acb13f000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_fill_popup_config_abc.abc` |
| `005acb13f000-005acb140000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_fill_rect_abc.abc` |
| `005acb140000-005acb15f000` | .so | `r--p` | 124 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libfdleak_tracker.so` |
| `005acb15f000-005acb19f000` | .so | `r-xp` | 256 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libfdleak_tracker.so` |
| `005acb19f000-005acb1a2000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libfdleak_tracker.so` |
| `005acb1a2000-005acb1a3000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libfdleak_tracker.so` |
| `005acb1a3000-005acb1a5000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libfdleak_tracker.so.bss]` |
| `005acb1a5000-005acb3a5000` | dev | `r--s` | 2048 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:startup_init_param:s0` |
| `005acb3a5000-005acb3a8000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_fill_request_abc.abc` |
| `005acb3a8000-005acb3a9000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_fill_trigger_type_abc.abc` |
| `005acb3a9000-005acb3ab000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_fill_type_abc.abc` |
| `005acb3ab000-005acb3ac000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_startup_callback_abc.abc` |
| `005acb3ac000-005acb3ae000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_startup_info_abc.abc` |
| `005acb3ae000-005acb3b0000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_auto_startup_manager_abc.abc` |
| `005acb3b0000-005acb3b1000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_base_context_abc.abc` |
| `005acb3b1000-005acb3b5000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_caller_callee_abc.abc` |
| `005acb3b5000-005acb3b6000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_child_process_args_abc.abc` |
| `005acb3b6000-005acb3b9000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_child_process_manager_abc.abc` |
| `005acb3b9000-005acb3ba000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_child_process_options_abc.abc` |
| `005acb3ba000-005acb3bb000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_completionHandler_callback_abc.abc` |
| `005acb3bb000-005acb3bc000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_completion_handler_abc.abc` |
| `005acb3bc000-005acb3c0000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acb3c0000-005acb3c2000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfwmark_client.z.so` |
| `005acb3c2000-005acb3c5000` | .so | `r-xp` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfwmark_client.z.so` |
| `005acb3c5000-005acb3c6000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfwmark_client.z.so` |
| `005acb3c6000-005acb3c7000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfwmark_client.z.so` |
| `005acb3c7000-005acbdc7000` | dev | `r--s` | 10240 | 76 | 1 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:default_param:s0` |
| `005acbdc7000-005acbdc9000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_configuration_abc.abc` |
| `005acbdc9000-005acbdcb000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_configuration_constant_abc.abc` |
| `005acbdcb000-005acbdcc000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_connect_options_abc.abc` |
| `005acbdcc000-005acbdce000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_context_abc.abc` |
| `005acbdce000-005acbdcf000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_custom_data_abc.abc` |
| `005acbdcf000-005acbdd0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_data_ability_helper_abc.abc` |
| `005acbdd0000-005acbdd1000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_data_uri_utils_abc.abc` |
| `005acbdd1000-005acbdd4000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_dialog_session_abc.abc` |
| `005acbdd4000-005acbdd5000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_embedded_uiextension_ability_abc.abc` |
| `005acbdd5000-005acbdd6000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_environment_callback_abc.abc` |
| `005acbdd6000-005acbdd7000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_error_code_abc.abc` |
| `005acbdd7000-005acbdd8000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_event_hub_abc.abc` |
| `005acbdd8000-005acbdd9000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_extension_ability_abc.abc` |
| `005acbdd9000-005acbdda000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_extension_context_abc.abc` |
| `005acbdda000-005acbddc000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_extension_running_info_abc.abc` |
| `005acbddc000-005acbddd000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_hyper_snap_manager_abc.abc` |
| `005acbddd000-005acbddf000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_insight_intent_abc.abc` |
| `005acbddf000-005acbde1000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_insight_intent_context_abc.abc` |
| `005acbde1000-005acbde8000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_insight_intent_driver_abc.abc` |
| `005acbde8000-005acbdea000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_insight_intent_executor_abc.abc` |
| `005acbdea000-005acbdeb000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_insight_intent_provider_abc.abc` |
| `005acbdeb000-005acbded000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_interop_ability_lifecycle_callback_abc.abc` |
| `005acbded000-005acbdef000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_kiosk_manager_abc.abc` |
| `005acbdef000-005acbdf0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_kiosk_status_abc.abc` |
| `005acbdf0000-005acbdf2000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_mission_info_abc.abc` |
| `005acbdf2000-005acbdf3000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_mission_listener_abc.abc` |
| `005acbdf3000-005acbdf4000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_mission_snapshot_abc.abc` |
| `005acbdf4000-005acbdf5000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_multi_app_mode_abc.abc` |
| `005acbdf5000-005acbdf6000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_openLink_options_abc.abc` |
| `005acbdf6000-005acbdf8000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_page_node_info_abc.abc` |
| `005acbdf8000-005acbdf9000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_process_data_abc.abc` |
| `005acbdf9000-005acbdfb000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_process_information_abc.abc` |
| `005acbdfb000-005acbdfc000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_running_app_clone_abc.abc` |
| `005acbdfc000-005acbdfd000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_running_multi_appinfo_abc.abc` |
| `005acbdfd000-005acbdfe000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_running_multi_instance_info_abc.abc` |
| `005acbdfe000-005acbdff000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_share_extension_ability_abc.abc` |
| `005acbdff000-005acbe00000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_shell_cmd_result_abc.abc` |
| `005acbe00000-005acbe13000` | .so | `r--p` | 76 | 36 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsamgr_proxy.z.so` |
| `005acbe13000-005acbe2f000` | .so | `r-xp` | 112 | 60 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsamgr_proxy.z.so` |
| `005acbe2f000-005acbe36000` | .so | `r--p` | 28 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsamgr_proxy.z.so` |
| `005acbe36000-005acbe37000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libsamgr_proxy.z.so` |
| `005acbe37000-005acbe38000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_start_options_abc.abc` |
| `005acbe38000-005acbe39000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_startup_config_abc.abc` |
| `005acbe39000-005acbe3a000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_startup_config_entry_abc.abc` |
| `005acbe3a000-005acbe3b000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_startup_listener_abc.abc` |
| `005acbe3b000-005acbe3c000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_startup_manager_abc.abc` |
| `005acbe3c000-005acbe3d000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_startup_task_abc.abc` |
| `005acbe3d000-005acbe3e000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_startup_task_executor_abc.abc` |
| `005acbe3e000-005acbe3f000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_trigger_info_abc.abc` |
| `005acbe3f000-005acbe40000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ui_service_extension_ability_abc.abc` |
| `005acbe40000-005acbe7c000` | GL | `r--p` | 240 | 64 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libglobal_resmgr.z.so` |
| `005acbe7c000-005acbee3000` | GL | `r-xp` | 412 | 352 | 15 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libglobal_resmgr.z.so` |
| `005acbee3000-005acbee7000` | GL | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libglobal_resmgr.z.so` |
| `005acbee7000-005acbee8000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libglobal_resmgr.z.so` |
| `005acbee8000-005acbee9000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libglobal_resmgr.z.so.bss]` |
| `005acbee9000-005acbeeb000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ui_ability_abc.abc` |
| `005acbeeb000-005acbefa000` | FilePage other | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_ui_ability_context_abc.abc` |
| `005acbefa000-005acbefc000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_vertical_panel_manager_abc.abc` |
| `005acbefc000-005acbefe000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_view_data_abc.abc` |
| `005acbefe000-005acbf00000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_want_agent_info_abc.abc` |
| `005acbf00000-005acbf01000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtokensetproc_shared.z.so` |
| `005acbf01000-005acbf04000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtokensetproc_shared.z.so` |
| `005acbf04000-005acbf05000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtokensetproc_shared.z.so` |
| `005acbf05000-005acbf06000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtokensetproc_shared.z.so` |
| `005acbf06000-005acbf0d000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_want_abc.abc` |
| `005acbf0d000-005acbf13000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_want_agent_abc.abc` |
| `005acbf13000-005acbf16000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ability_runtime_want_constant_abc.abc` |
| `005acbf16000-005acbf1f000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/accessibility.abc` |
| `005acbf1f000-005acbf2c000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/accessibility_config.abc` |
| `005acbf2c000-005acbf2f000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/accessibility_extension_ability.abc` |
| `005acbf2f000-005acbf3d000` | FilePage other | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/accessibility_extension_context.abc` |
| `005acbf3d000-005acbf3e000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_extension_abc.abc` |
| `005acbf3e000-005acbf3f000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_extension_connect_callback_abc.abc` |
| `005acbf3f000-005acbf40000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_extension_context_abc.abc` |
| `005acbf40000-005acbffe000` | .so | `r--p` | 760 | 164 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_core.z.so` |
| `005acbffe000-005acc10b000` | .so | `r-xp` | 1076 | 336 | 11 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_core.z.so` |
| `005acc10b000-005acc12d000` | .so | `r--p` | 136 | 36 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_core.z.so` |
| `005acc12d000-005acc12e000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_core.z.so` |
| `005acc12e000-005acc12f000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libappexecfwk_core.z.so.bss]` |
| `005acc12f000-005acc134000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_card_abc.abc` |
| `005acc134000-005acc135000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_host_proxy_abc.abc` |
| `005acc135000-005acc137000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_manager_abc.abc` |
| `005acc137000-005acc138000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_proxy_abc.abc` |
| `005acc138000-005acc139000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_ui_extension_ability_abc.abc` |
| `005acc139000-005acc13a000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/agent_runtime_agent_utils_abc.abc` |
| `005acc13a000-005acc13d000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/animator_ani.abc` |
| `005acc13d000-005acc13f000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/appRecovery_abc.abc` |
| `005acc13f000-005acc140000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/app_foreground_state_observer_abc.abc` |
| `005acc140000-005acc149000` | .so | `r--p` | 36 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libpcre2.z.so` |
| `005acc149000-005acc16a000` | .so | `r-xp` | 132 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libpcre2.z.so` |
| `005acc16a000-005acc16b000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libpcre2.z.so` |
| `005acc16b000-005acc16c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libpcre2.z.so` |
| `005acc16c000-005acc172000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/app_control.abc` |
| `005acc172000-005acc177000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/app_domain_verify_ets.abc` |
| `005acc177000-005acc178000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/app_processInfo_abc.abc` |
| `005acc178000-005acc17a000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/app_provision_info.abc` |
| `005acc17a000-005acc17d000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/app_service_extension_ability.abc` |
| `005acc17d000-005acc17e000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/application_state_observer_abc.abc` |
| `005acc17e000-005acc17f000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/arkui_test.abc` |
| `005acc17f000-005acc180000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/atomic_service_options_abc.abc` |
| `005acc180000-005acc181000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtokenid_sdk.z.so` |
| `005acc181000-005acc184000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtokenid_sdk.z.so` |
| `005acc184000-005acc185000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtokenid_sdk.z.so` |
| `005acc185000-005acc186000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtokenid_sdk.z.so` |
| `005acc186000-005acc19b000` | FilePage other | `r--p` | 84 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/app_account_abc.abc` |
| `005acc19b000-005acc1a0000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/application_info.abc` |
| `005acc1a0000-005acc1a6000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/applock_abc.abc` |
| `005acc1a6000-005acc1b1000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/audioHaptic_taihe_abc.abc` |
| `005acc1b1000-005acc1be000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/av_input_cast_picker_ets_abc.abc` |
| `005acc1be000-005acc1c0000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/backup_ext.abc` |
| `005acc1c0000-005acc1c2000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librestorecon.z.so` |
| `005acc1c2000-005acc1c6000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librestorecon.z.so` |
| `005acc1c6000-005acc1c7000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librestorecon.z.so` |
| `005acc1c7000-005acc1c8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librestorecon.z.so` |
| `005acc1c8000-005acc1df000` | FilePage other | `r--p` | 92 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/av_cast_picker_ets_abc.abc` |
| `005acc1df000-005acc1e3000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/av_volume_panel_ets_abc.abc` |
| `005acc1e3000-005acc1f9000` | FilePage other | `r--p` | 88 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/background_task_manager_abc.abc` |
| `005acc1f9000-005acc200000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/backgroundprocessmanager_abc.abc` |
| `005acc200000-005acc203000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libstorage_manager_acl.z.so` |
| `005acc203000-005acc208000` | .so | `r-xp` | 20 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libstorage_manager_acl.z.so` |
| `005acc208000-005acc20a000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libstorage_manager_acl.z.so` |
| `005acc20a000-005acc20b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libstorage_manager_acl.z.so` |
| `005acc20b000-005acc20d000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/backup_transfer.abc` |
| `005acc20d000-005acc215000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/base_transfer.abc` |
| `005acc215000-005acc21c000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/batteryInfo.abc` |
| `005acc21c000-005acc222000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/batterystats_abc.abc` |
| `005acc222000-005acc22a000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bluetoothAccess_abc.abc` |
| `005acc22a000-005acc22e000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acc22e000-005acc239000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bluetoothA2dp_abc.abc` |
| `005acc239000-005acc240000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bluetoothBaseProfile_abc.abc` |
| `005acc2f8000-005acc2f9000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwant.z.so` |
| `005acc2fa000-005acc300000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bluetoothHfp_abc.abc` |
| `005acc300000-005acc304000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhitrace_option.so` |
| `005acc304000-005acc30b000` | .so | `r-xp` | 28 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhitrace_option.so` |
| `005acc30b000-005acc30c000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhitrace_option.so` |
| `005acc30c000-005acc30d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhitrace_option.so` |
| `005acc30d000-005acc327000` | FilePage other | `r--p` | 104 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bluetoothBle_abc.abc` |
| `005acc327000-005acc33b000` | FilePage other | `r--p` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bluetoothConnection_abc.abc` |
| `005acc33b000-005acc340000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/brightness_abc.abc` |
| `005acc3c7000-005acc3d0000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bluetoothConstant_abc.abc` |
| `005acc3d0000-005acc3d6000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bluetoothHid_abc.abc` |
| `005acc3d6000-005acc3db000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bundle_info.abc` |
| `005acc3db000-005acc3e8000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bundle_installer.abc` |
| `005acc3e8000-005acc3e9000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bundle_monitor.abc` |
| `005acc3e9000-005acc3ef000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bundle_pack_info.abc` |
| `005acc3ef000-005acc3f0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bundle_resource_info.abc` |
| `005acc3f0000-005acc3f3000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bundle_resource_manager.abc` |
| `005acc3f3000-005acc3f5000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/business_ability_info_abc.abc` |
| `005acc3f5000-005acc3f7000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/business_ability_router_abc.abc` |
| `005acc3f7000-005acc3fc000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/cache_download.abc` |
| `005acc3fc000-005acc3ff000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/color_space_manager.abc` |
| `005acc3ff000-005acc400000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/commonEventData.abc` |
| `005acc400000-005acc40f000` | .so | `r--p` | 60 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libappspawn_common.z.so` |
| `005acc40f000-005acc427000` | .so | `r-xp` | 96 | 60 | 1 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libappspawn_common.z.so` |
| `005acc427000-005acc429000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libappspawn_common.z.so` |
| `005acc429000-005acc42b000` | .so | `rw-p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libappspawn_common.z.so` |
| `005acc42b000-005acc431000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/camera_picker_taihe_abc.abc` |
| `005acc431000-005acc43e000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/certmanager_abc.abc` |
| `005acc43e000-005acc43f000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/commonEventPublishData.abc` |
| `005acc43f000-005acc440000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/commonEventSubscribeInfo.abc` |
| `005acc440000-005acc450000` | .so | `r--p` | 64 | 32 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_sdk.z.so` |
| `005acc450000-005acc47a000` | .so | `r-xp` | 168 | 64 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_sdk.z.so` |
| `005acc47a000-005acc47e000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_sdk.z.so` |
| `005acc47e000-005acc47f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_sdk.z.so` |
| `005acc47f000-005acc480000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/completion_handler_for_atomic_service_abc.abc` |
| `005acc480000-005acc486000` | .so | `r--p` | 24 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libucollection_client.z.so` |
| `005acc486000-005acc490000` | .so | `r-xp` | 40 | 40 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libucollection_client.z.so` |
| `005acc490000-005acc493000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libucollection_client.z.so` |
| `005acc493000-005acc494000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libucollection_client.z.so` |
| `005acc494000-005acc4b2000` | FilePage other | `r--p` | 120 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/bundle_manager.abc` |
| `005acc4b2000-005acc4b8000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/certmanager_dialog_abc.abc` |
| `005acc4b8000-005acc4bd000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/charger.abc` |
| `005acc4bd000-005acc4c0000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/componentSnapshot.abc` |
| `005acc4c0000-005acc4c4000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_communication_adapter_cxx.z.so` |
| `005acc4c4000-005acc4cd000` | .so | `r-xp` | 36 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_communication_adapter_cxx.z.so` |
| `005acc4cd000-005acc4cf000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_communication_adapter_cxx.z.so` |
| `005acc4cf000-005acc4d0000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_communication_adapter_cxx.z.so` |
| `005acc4d0000-005acc4fd000` | FilePage other | `r--p` | 180 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/cert_framework_ets.abc` |
| `005acc4fd000-005acc4ff000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/curves.abc` |
| `005acc4ff000-005acc500000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/dataSharePredicatesAni.abc` |
| `005acc500000-005acc50f000` | .so | `r--p` | 60 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libsecurity_component_sdk.z.so` |
| `005acc50f000-005acc523000` | .so | `r-xp` | 80 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsecurity_component_sdk.z.so` |
| `005acc523000-005acc527000` | .so | `r--p` | 16 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsecurity_component_sdk.z.so` |
| `005acc527000-005acc528000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsecurity_component_sdk.z.so` |
| `005acc528000-005acc53b000` | FilePage other | `r--p` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/cloudData.abc` |
| `005acc53b000-005acc53f000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/componentUtils.abc` |
| `005acc53f000-005acc540000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/dispatch_info.abc` |
| `005acc540000-005acc556000` | .so | `r--p` | 88 | 56 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcesfwk_innerkits.z.so` |
| `005acc566000-005acc567000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcesfwk_innerkits.z.so` |
| `005acc567000-005acc568000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libcesfwk_innerkits.z.so.bss]` |
| `005acc568000-005acc56a000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/display_sync_ani.abc` |
| `005acc56a000-005acc56e000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acc56e000-005acc574000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/cloudDataCommonType.abc` |
| `005acc574000-005acc57a000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/clouddiskmanager_taihe_abc.abc` |
| `005acc57a000-005acc580000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/continueManager_taihe_abc.abc` |
| `005acc580000-005acc598000` | .so | `r--p` | 96 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libutd_client.z.so` |
| `005acc598000-005acc5dd000` | .so | `r-xp` | 276 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libutd_client.z.so` |
| `005acc5dd000-005acc5e0000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libutd_client.z.so` |
| `005acc5e0000-005acc5e1000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libutd_client.z.so` |
| `005acc5e1000-005acc5e2000` | FilePage other | `rw-p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `[anon:libutd_client.z.so.bss]` |
| `005acc5e2000-005acc5ef000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/cloud_extension_ext.abc` |
| `005acc5ef000-005acc5f6000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/commonEventSubscriber.abc` |
| `005acc5f6000-005acc5fe000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/coordination_abc.abc` |
| `005acc5fe000-005acc5ff000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/distributed_extension_ability_ani.abc` |
| `005acc5ff000-005acc600000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/driverExtensionAbility.abc` |
| `005acc600000-005acc61a000` | .so | `r--p` | 104 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_common.z.so` |
| `005acc61a000-005acc642000` | .so | `r-xp` | 160 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_common.z.so` |
| `005acc642000-005acc644000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_common.z.so` |
| `005acc644000-005acc645000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_common.z.so` |
| `005acc645000-005acc652000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/common_event_manager.abc` |
| `005acc652000-005acc663000` | FilePage other | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/connection.abc` |
| `005acc663000-005acc674000` | FilePage other | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/datashareAni.abc` |
| `005acc674000-005acc678000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/default_app_manager.abc` |
| `005acc678000-005acc67f000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/deviceInfo.abc` |
| `005acc67f000-005acc680000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/errorManager_abc.abc` |
| `005acc680000-005acc681000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_stub_empty.so` |
| `005acc681000-005acc682000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_stub_empty.so` |
| `005acc682000-005acc683000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_stub_empty.so` |
| `005acc683000-005acc684000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_stub_empty.so` |
| `005acc684000-005acc6b3000` | FilePage other | `r--p` | 188 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/crypto_framework_ets.abc` |
| `005acc6b3000-005acc6b7000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/distributed_bundle_manager.abc` |
| `005acc6b7000-005acc6b8000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/faultlog_extension_ability_ani.abc` |
| `005acc6b8000-005acc6bc000` | FilePage other | `rw-p` | 16 | 12 | 1 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/liburi.z.so_121600_1]` |
| `005acc6bc000-005acc6be000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/atomicservice/libnavpushpathhelper.z.so_63816_1]` |
| `005acc6be000-005acc6bf000` | FilePage other | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/hiappevent/databases/appevent.db-dwr` |
| `005acc6bf000-005acc6c0000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acc6f6000-005acc6f7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcesfwk_core.z.so` |
| `005acc6f7000-005acc6f8000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libcesfwk_core.z.so.bss]` |
| `005acc6f8000-005acc6ff000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/device_standby_abc.abc` |
| `005acc6ff000-005acc700000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/focusController.abc` |
| `005acc73f000-005acc740000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhicollie.z.so` |
| `005acc741000-005acc76a000` | FilePage other | `r--p` | 164 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/customtitle_static_abc.abc` |
| `005acc76a000-005acc775000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/device_manager_abc.abc` |
| `005acc775000-005acc777000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/dlp_hide_info.abc` |
| `005acc777000-005acc77c000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/driverExtensionContext_abc.abc` |
| `005acc77c000-005acc780000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acc798000-005acc799000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbase.z.so` |
| `005acc799000-005acc7a8000` | FilePage other | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/display_abc.abc` |
| `005acc7a8000-005acc7b0000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/distributed_account_abc.abc` |
| `005acc7b0000-005acc7bb000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/distributeddata_object.abc` |
| `005acc7bb000-005acc7c0000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/effectKit.abc` |
| `005acc7c0000-005acc7d0000` | .so | `r--p` | 64 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libressched_client.z.so` |
| `005acc7d0000-005acc7f8000` | .so | `r-xp` | 160 | 112 | 3 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libressched_client.z.so` |
| `005acc7f8000-005acc7ff000` | .so | `r--p` | 28 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libressched_client.z.so` |
| `005acc7ff000-005acc800000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libressched_client.z.so` |
| `005acc800000-005acc801000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libressched_client.z.so.bss]` |
| `005acc801000-005acc824000` | FilePage other | `r--p` | 140 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/distributedkvstore.abc` |
| `005acc824000-005acc833000` | FilePage other | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/dmsfwk_taihe_ani.abc` |
| `005acc833000-005acc839000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/download_file_button_ets_abc.abc` |
| `005acc839000-005acc83f000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/drag_abc.abc` |
| `005acc83f000-005acc840000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/form_binding_data.abc` |
| `005acc840000-005acc911000` | .so | `r--p` | 836 | 128 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_base.z.so` |
| `005acc911000-005acca77000` | .so | `r-xp` | 1432 | 364 | 9 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_base.z.so` |
| `005acca77000-005acca86000` | .so | `r--p` | 60 | 52 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_base.z.so` |
| `005acca86000-005acca88000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_base.z.so` |
| `005acca88000-005acca89000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libappexecfwk_base.z.so.bss]` |
| `005acca89000-005accaab000` | FilePage other | `r--p` | 136 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/distributedmissionmanager.abc` |
| `005accaab000-005accac0000` | FilePage other | `r--p` | 84 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/drawing.abc` |
| `005accac0000-005accac6000` | .so | `r--p` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libstring_utils.z.so` |
| `005accac6000-005accad9000` | .so | `r-xp` | 76 | 44 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libstring_utils.z.so` |
| `005accad9000-005accadb000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libstring_utils.z.so` |
| `005accadb000-005accadc000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libstring_utils.z.so` |
| `005accadc000-005accade000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/element_name.abc` |
| `005accade000-005accae2000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/event_emitter_abc.abc` |
| `005accae2000-005accae3000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:ffrt_param:s0` |
| `005accae3000-005accaf2000` | FilePage other | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/drm_framework_taihe_abc.abc` |
| `005accaf2000-005accaf4000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/extension_ability_info.abc` |
| `005accaf4000-005accafa000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/extension_window_ani.abc` |
| `005accafa000-005accaff000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/extension_window_host_ani.abc` |
| `005accaff000-005accb00000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/form_edit_extension_ability.abc` |
| `005accb64000-005accb65000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libos_account_innerkits.z.so` |
| `005accb66000-005accb77000` | FilePage other | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ets2abc_commonsdk_arkts.abc` |
| `005accb77000-005accb7c000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/fbwindow_ani.abc` |
| `005accb7c000-005accb7e000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/formError.abc` |
| `005accb7e000-005accb80000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/form_edit_extension_context.abc` |
| `005accb80000-005accb88000` | .so | `r--p` | 32 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccountkits.z.so` |
| `005accb88000-005accb9a000` | .so | `r-xp` | 72 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccountkits.z.so` |
| `005accb9a000-005accb9e000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccountkits.z.so` |
| `005accb9e000-005accb9f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccountkits.z.so` |
| `005accb9f000-005accba7000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/file_cloud_sync_manager.abc` |
| `005accba7000-005accba8000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/formagent.abc` |
| `005accba8000-005accbac000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005accbac000-005accbba000` | FilePage other | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/file_backup_taihe_abc.abc` |
| `005accbba000-005accbbf000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/file_fileuri_taihe_abc.abc` |
| `005accbbf000-005accbc0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hdr_capability.abc` |
| `005accbc0000-005accc89000` | .so | `r--p` | 804 | 320 | 23 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhmicuuc.z.so` |
| `005accc89000-005accda3000` | .so | `r-xp` | 1128 | 468 | 20 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhmicuuc.z.so` |
| `005accda3000-005accdb9000` | .so | `r--p` | 88 | 48 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhmicuuc.z.so` |
| `005accdb9000-005accdba000` | FilePage other | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libhmicuuc.z.so.bss]` |
| `005accdba000-005accdbb000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhmicuuc.z.so` |
| `005accdbb000-005accdbd000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libhmicuuc.z.so.bss]` |
| `005accdbd000-005accdc0000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/form_extension_ability_ani.abc` |
| `005accdc0000-005accdc3000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_mgr.z.so` |
| `005accdc3000-005accdc7000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_mgr.z.so` |
| `005accdc7000-005accdc9000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_mgr.z.so` |
| `005accdc9000-005accdca000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_mgr.z.so` |
| `005accdca000-005accddb000` | FilePage other | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/file_cloud_sync.abc` |
| `005accddb000-005accde7000` | FilePage other | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/file_picker_taihe_abc.abc` |
| `005accde7000-005accdf0000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/file_share_taihe_abc.abc` |
| `005accdf0000-005accdfb000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/findnetwork_ets.abc` |
| `005accdfb000-005accdfe000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/form_observer_abc.abc` |
| `005accdfe000-005accdff000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hdsPhysics2d_common.abc` |
| `005accdff000-005acce00000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hichecker.abc` |
| `005acce45000-005acce51000` | FilePage other | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/formHost.abc` |
| `005acce51000-005acce5e000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/formInfo.abc` |
| `005acce5e000-005acce64000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/formProvider.abc` |
| `005acce64000-005acce68000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/formmenu_ets_abc.abc` |
| `005acce68000-005acce6c000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/freeInstall.abc` |
| `005acce6c000-005acce75000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/full_screen_launch_ets_abc.abc` |
| `005acce75000-005acce7d000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/fusion_awareness_app_abc.abc` |
| `005acce7d000-005acce7e000` | native heap | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acce7e000-005acce80000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hilog.abc` |
| `005acce80000-005acce83000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_common.z.so` |
| `005acce83000-005acce88000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_common.z.so` |
| `005acce88000-005acce89000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_common.z.so` |
| `005acce89000-005acce8a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappexecfwk_common.z.so` |
| `005acce8a000-005acce92000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/gesture_event.abc` |
| `005acce92000-005acce97000` | GL | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/global.abc` |
| `005acce97000-005acce9a000` | Graph | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/graphic_2d_ext_abc.abc` |
| `005acce9a000-005accea9000` | Graph | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/graphics3d_scene.abc` |
| `005accea9000-005acceb9000` | Graph | `r--p` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/graphics3d_scene_nodes.abc` |
| `005acceb9000-005accebd000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hap_module_info.abc` |
| `005accebd000-005accec0000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hdsPhysics2d_rigidBody.abc` |
| `005accec0000-005accf1c000` | .so | `r--p` | 368 | 84 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhmicui18n.z.so` |
| `005accf1c000-005acd05d000` | .so | `r-xp` | 1284 | 444 | 43 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhmicui18n.z.so` |
| `005acd05d000-005acd06e000` | .so | `r--p` | 68 | 60 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhmicui18n.z.so` |
| `005acd06e000-005acd06f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhmicui18n.z.so` |
| `005acd06f000-005acd070000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libhmicui18n.z.so.bss]` |
| `005acd070000-005acd078000` | Graph | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/graphics3d_scene_post_process_settings.abc` |
| `005acd078000-005acd07f000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hardware_taihe_abc.abc` |
| `005acd07f000-005acd080000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hitrace_meter.abc` |
| `005acd080000-005acd081000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libseccomp.z.so` |
| `005acd081000-005acd083000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libseccomp.z.so` |
| `005acd083000-005acd084000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libseccomp.z.so` |
| `005acd084000-005acd085000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libseccomp.z.so` |
| `005acd085000-005acd09e000` | Graph | `r--p` | 100 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/graphics3d_scene_resources.abc` |
| `005acd09e000-005acd0aa000` | Graph | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/graphics3d_scene_types.abc` |
| `005acd0aa000-005acd0b7000` | Graph | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/graphstore.abc` |
| `005acd0b7000-005acd0bb000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acd0bb000-005acd0c0000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hisysevent.abc` |
| `005acd0c0000-005acd0d3000` | .so | `r--p` | 76 | 36 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libjsoncpp.z.so` |
| `005acd0d3000-005acd0f5000` | .so | `r-xp` | 136 | 116 | 3 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libjsoncpp.z.so` |
| `005acd0f5000-005acd0f7000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libjsoncpp.z.so` |
| `005acd0f7000-005acd0f8000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libjsoncpp.z.so` |
| `005acd0f8000-005acd0ff000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hidebug.abc` |
| `005acd0ff000-005acd100000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_pushDownstreamProcess.abc` |
| `005acd100000-005acd114000` | .so | `r--p` | 80 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdomain_account_innerkits.z.so` |
| `005acd114000-005acd133000` | .so | `r-xp` | 124 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdomain_account_innerkits.z.so` |
| `005acd133000-005acd13a000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdomain_account_innerkits.z.so` |
| `005acd13a000-005acd13b000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdomain_account_innerkits.z.so` |
| `005acd13b000-005acd13e000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hitrace_chain.abc` |
| `005acd13e000-005acd140000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_inner_servicedelivery.abc` |
| `005acd140000-005acd14c000` | .so | `r--p` | 48 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libextractortool.z.so` |
| `005acd14c000-005acd15d000` | .so | `r-xp` | 68 | 48 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libextractortool.z.so` |
| `005acd15d000-005acd15e000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libextractortool.z.so` |
| `005acd15e000-005acd15f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libextractortool.z.so` |
| `005acd15f000-005acd175000` | FilePage other | `r--p` | 88 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hdsBaseComponent.abc` |
| `005acd175000-005acd180000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hiappevent.abc` |
| `005acd180000-005acd182000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapi_cache_manager.z.so` |
| `005acd182000-005acd188000` | .so | `r-xp` | 24 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapi_cache_manager.z.so` |
| `005acd188000-005acd189000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapi_cache_manager.z.so` |
| `005acd189000-005acd18a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapi_cache_manager.z.so` |
| `005acd18a000-005acd18e000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_camerasupplier.abc` |
| `005acd18e000-005acd191000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_collaborationability.abc` |
| `005acd191000-005acd196000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_collaborationservicemanager.abc` |
| `005acd196000-005acd19e000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_devicepicker.abc` |
| `005acd19e000-005acd1a2000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_inner_devicepicker.abc` |
| `005acd1a2000-005acd1a5000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_servicebrowser.abc` |
| `005acd1a5000-005acd1ad000` | GL | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_graphics_spatialRender.abc` |
| `005acd1ad000-005acd1ba000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/http.abc` |
| `005acd1ba000-005acd1bb000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/imagecache.abc` |
| `005acd1bb000-005acd1c0000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/input_event.abc` |
| `005acd1d8000-005acd1df000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/image_loader_taihe_abc.abc` |
| `005acd1df000-005acd1e5000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/infrared_emitter.abc` |
| `005acd1e5000-005acd1ed000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/input_consumer.abc` |
| `005acd1ed000-005acd1fa000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/input_device.abc` |
| `005acd1fa000-005acd1fc000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/inputmethod_extension_ability_ani.abc` |
| `005acd1fc000-005acd1fe000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/inspector.abc` |
| `005acd1fe000-005acd200000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/intelligentscene.abc` |
| `005acd200000-005acd20e000` | .so | `r--p` | 56 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/libhap_restorecon.z.so` |
| `005acd235000-005acd236000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libhap_restorecon.z.so` |
| `005acd236000-005acd23d000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/input_event_client.abc` |
| `005acd23d000-005acd23e000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/launcher_ability_info.abc` |
| `005acd23e000-005acd240000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/launcher_ability_resource_info.abc` |
| `005acd240000-005acd257000` | .so | `r--p` | 92 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_common_cxx.z.so` |
| `005acd257000-005acd25d000` | .so | `r-xp` | 24 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_common_cxx.z.so` |
| `005acd25d000-005acd263000` | .so | `r--p` | 24 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_common_cxx.z.so` |
| `005acd263000-005acd26c000` | .so | `rw-p` | 36 | 36 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libaccesstoken_common_cxx.z.so` |
| `005acd26c000-005acd273000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/input_monitor.abc` |
| `005acd273000-005acd278000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/inputmethod_extraconfig_abc.abc` |
| `005acd278000-005acd27e000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/inputmethod_panel_abc.abc` |
| `005acd27e000-005acd280000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/live_form_extension_ability.abc` |
| `005acd293000-005acd2bd000` | FilePage other | `r--p` | 168 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_rcp.abc` |
| `005acd2bd000-005acd2c0000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/launcher_bundle_manager.abc` |
| `005acd2c0000-005acd2ce000` | .so | `r--p` | 56 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libselinux.z.so` |
| `005acd2ce000-005acd2ec000` | .so | `r-xp` | 120 | 36 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libselinux.z.so` |
| `005acd2ec000-005acd2ee000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libselinux.z.so` |
| `005acd2ee000-005acd2ef000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libselinux.z.so` |
| `005acd2ef000-005acd2f1000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libselinux.z.so.bss]` |
| `005acd2f1000-005acd2f7000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/inputmethod_subtype_abc.abc` |
| `005acd2f7000-005acd2fc000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/intention_code.abc` |
| `005acd2fc000-005acd2fe000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/live_form_extension_context.abc` |
| `005acd2fe000-005acd300000` | GL | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/loglibrary.abc` |
| `005acd300000-005acd306000` | .so | `r--p` | 24 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdlp_fuse.z.so` |
| `005acd306000-005acd30e000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdlp_fuse.z.so` |
| `005acd30e000-005acd310000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdlp_fuse.z.so` |
| `005acd310000-005acd311000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdlp_fuse.z.so` |
| `005acd311000-005acd33a000` | FilePage other | `r--p` | 164 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_service.abc` |
| `005acd33a000-005acd33f000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/key_manager_taihe_abc.abc` |
| `005acd33f000-005acd340000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/metadata.abc` |
| `005acd340000-005acd356000` | .so | `r--p` | 88 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libappspawn_sandbox.z.so` |
| `005acd356000-005acd381000` | .so | `r-xp` | 172 | 132 | 2 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libappspawn_sandbox.z.so` |
| `005acd381000-005acd384000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libappspawn_sandbox.z.so` |
| `005acd384000-005acd385000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libappspawn_sandbox.z.so` |
| `005acd385000-005acd386000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libappspawn_sandbox.z.so.bss]` |
| `005acd386000-005acd3bd000` | FilePage other | `r--p` | 220 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms_collaboration_collaborationdevicepicker.abc` |
| `005acd3bd000-005acd3bf000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/network_security.abc` |
| `005acd3bf000-005acd3c0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_action_button.abc` |
| `005acd3c0000-005acd3cd000` | .so | `r--p` | 52 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfuse.z.so` |
| `005acd3cd000-005acd3ed000` | .so | `r-xp` | 128 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfuse.z.so` |
| `005acd3ed000-005acd400000` | .so | `r--p` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfuse.z.so` |
| `005acd400000-005acd401000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfuse.z.so` |
| `005acd401000-005acdc01000` | FilePage other | `rw-p` | 8192 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libfuse.z.so.bss]` |
| `005acdc01000-005acdc1a000` | FilePage other | `r--p` | 100 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/inputmethod_abc.abc` |
| `005acdc1a000-005acdc2c000` | FilePage other | `r--p` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/inputmethod_dialog_ets_abc.abc` |
| `005acdc2c000-005acdc3a000` | FilePage other | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/key_code.abc` |
| `005acdc3a000-005acdc40000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/local_chat_abc.abc` |
| `005acdc40000-005acdc42000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libevent_reporter.z.so` |
| `005acdc42000-005acdc45000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libevent_reporter.z.so` |
| `005acdc45000-005acdc46000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libevent_reporter.z.so` |
| `005acdc46000-005acdc47000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/common/libevent_reporter.z.so` |
| `005acdc47000-005acdc65000` | FilePage other | `r--p` | 120 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/inputmethod_engine_abc.abc` |
| `005acdc65000-005acdc7b000` | FilePage other | `r--p` | 88 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/intelligent_voice_framework_taihe_abc.abc` |
| `005acdc7b000-005acdc7f000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/network_quality.abc` |
| `005acdc7f000-005acdc80000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_extension_content.abc` |
| `005acdc80000-005acdc81000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/libappspawn_asan.z.so` |
| `005acdc81000-005acdc83000` | .so | `r-xp` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/libappspawn_asan.z.so` |
| `005acdc83000-005acdc84000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/libappspawn_asan.z.so` |
| `005acdc84000-005acdc85000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/libappspawn_asan.z.so` |
| `005acdc85000-005acde85000` | dev | `r--s` | 2048 | 12 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:persist_sys_param:s0` |
| `005acde85000-005acde8c000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/key_event.abc` |
| `005acde8c000-005acdeae000` | FilePage other | `r--p` | 136 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/location_framework_abc.abc` |
| `005acdeae000-005acdeb4000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/metadataBinding_abc.abc` |
| `005acdeb4000-005acdeba000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/motion_abc.abc` |
| `005acdeba000-005acdec0000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/multimodalawareness_devicestatus_abc.abc` |
| `005acdec0000-005acdec4000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuser_controller.z.so` |
| `005acdec4000-005acdecb000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuser_controller.z.so` |
| `005acdecb000-005acdecc000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuser_controller.z.so` |
| `005acdecc000-005acdecd000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuser_controller.z.so` |
| `005acdf4d000-005acdf60000` | FilePage other | `r--p` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/mech_manager_abc.abc` |
| `005acdf60000-005acdf6f000` | FilePage other | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/mindspore_ani_abc.abc` |
| `005acdf6f000-005acdf78000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/mouse_event.abc` |
| `005acdf78000-005acdf7e000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/nearlinkCdsm_abc.abc` |
| `005acdf7e000-005acdf80000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_common_def.abc` |
| `005acdf80000-005acdf82000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhisysevent_report.z.so` |
| `005acdf82000-005acdf87000` | .so | `r-xp` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhisysevent_report.z.so` |
| `005acdf87000-005acdf88000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhisysevent_report.z.so` |
| `005acdf88000-005acdf89000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhisysevent_report.z.so` |
| `005acdf89000-005acdf8f000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/nearlinkConstant_abc.abc` |
| `005acdf8f000-005acdf98000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/nearlinkManager_abc.abc` |
| `005acdf98000-005acdf9e000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/nearlinkRemoteDevice_abc.abc` |
| `005acdf9e000-005acdfa4000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/nfc_fwk_etc_cardEmulation_abc.abc` |
| `005acdfa4000-005acdfa9000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/nfc_fwk_etc_controller_abc.abc` |
| `005acdfa9000-005acdfb3000` | FilePage other | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_content.abc` |
| `005acdfb3000-005acdfb4000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_extension_subscriber_extension_ability.abc` |
| `005acdfb4000-005acdfb5000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_extension_subscriber_extension_context.abc` |
| `005acdfb5000-005acdfb7000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_extension_subscription.abc` |
| `005acdfb7000-005acdfb8000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_extension_subscription_info.abc` |
| `005acdfb8000-005acdfba000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_flags.abc` |
| `005acdfba000-005acdfbc000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_info.abc` |
| `005acdfbc000-005acdfbe000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_slot.abc` |
| `005acdfbe000-005acdfc0000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_sorting.abc` |
| `005acdfc0000-005acdfe0000` | .so | `r--p` | 128 | 124 | 20 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_client.z.so` |
| `005acdfe0000-005ace094000` | .so | `r-xp` | 720 | 332 | 77 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_client.z.so` |
| `005ace094000-005ace09b000` | .so | `r--p` | 28 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_client.z.so` |
| `005ace09b000-005ace09c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_client.z.so` |
| `005ace09c000-005ace09f000` | FilePage other | `rw-p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `[anon:libdevicestatus_client.z.so.bss]` |
| `005ace09f000-005ace0bb000` | FilePage other | `r--p` | 112 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/nfc_fwk_etc_tag_abc.abc` |
| `005ace0bb000-005ace0bc000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_sorting_map.abc` |
| `005ace0bc000-005ace0bd000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_subscribe_info.abc` |
| `005ace0bd000-005ace0be000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_template.abc` |
| `005ace0be000-005ace0bf000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_user_input.abc` |
| `005ace0bf000-005ace0c0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/overlayManager.abc` |
| `005ace0c0000-005ace0dc000` | .so | `r--p` | 112 | 108 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_scene_common.z.so` |
| `005ace0dc000-005ace0fe000` | .so | `r-xp` | 136 | 136 | 9 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_scene_common.z.so` |
| `005ace0fe000-005ace102000` | .so | `r--p` | 16 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_scene_common.z.so` |
| `005ace102000-005ace103000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_scene_common.z.so` |
| `005ace103000-005ace117000` | FilePage other | `r--p` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_manager.abc` |
| `005ace117000-005ace122000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_request.abc` |
| `005ace122000-005ace129000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_subscribe.abc` |
| `005ace129000-005ace131000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/notification_subscriber.abc` |
| `005ace131000-005ace13a000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/observer.abc` |
| `005ace13a000-005ace13c000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ohos_file_environment_abc.abc` |
| `005ace13c000-005ace13e000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ohos_file_hash_abc.abc` |
| `005ace13e000-005ace140000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ohos_file_securityLabel_abc.abc` |
| `005ace140000-005ace144000` | .so | `r--p` | 16 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libpub_utils.z.so` |
| `005ace144000-005ace149000` | .so | `r-xp` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libpub_utils.z.so` |
| `005ace149000-005ace14a000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libpub_utils.z.so` |
| `005ace14a000-005ace14c000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libpub_utils.z.so` |
| `005ace14c000-005ace15e000` | FilePage other | `r--p` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ohos_distributedDeviceManager_abc.abc` |
| `005ace15e000-005ace160000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ohos_file_statvfs_abc.abc` |
| `005ace160000-005ace16e000` | FilePage other | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/onScreen_abc.abc` |
| `005ace16e000-005ace172000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/overlay.abc` |
| `005ace172000-005ace173000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/overlay_module_info.abc` |
| `005ace173000-005ace17a000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/parentControl_ets.abc` |
| `005ace17a000-005ace17b000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/permission_def.abc` |
| `005ace17b000-005ace17c000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/permissions.abc` |
| `005ace17c000-005ace17e000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/photo_editor_extension_ability_ani.abc` |
| `005ace17e000-005ace180000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/plugin_bundle_info.abc` |
| `005ace180000-005ace181000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextractresourcemanager.z.so` |
| `005ace181000-005ace182000` | .so | `r-xp` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextractresourcemanager.z.so` |
| `005ace182000-005ace184000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextractresourcemanager.z.so` |
| `005ace184000-005ace185000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextractresourcemanager.z.so` |
| `005ace185000-005ace1a9000` | FilePage other | `r--p` | 144 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ohos_file_fs_abc.abc` |
| `005ace1a9000-005ace1b7000` | FilePage other | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/pasteboard_taihe_ani.abc` |
| `005ace1b7000-005ace1bd000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/pipcontent_ani.abc` |
| `005ace1bd000-005ace1bf000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/policy.abc` |
| `005ace1bf000-005ace1c0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/print_extension_ability_ani.abc` |
| `005ace1c0000-005ace336000` | .so | `r--p` | 1496 | 128 | 8 | 0 | 0 | 0.00% | `/system/lib64/libddgr.z.so` |
| `005ace336000-005ace6c1000` | .so | `r-xp` | 3628 | 688 | 83 | 0 | 0 | 0.00% | `/system/lib64/libddgr.z.so` |
| `005ace6c1000-005ace6e0000` | .so | `r--p` | 124 | 56 | 2 | 0 | 0 | 0.00% | `/system/lib64/libddgr.z.so` |
| `005ace6e0000-005ace6e1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libddgr.z.so` |
| `005ace6e1000-005ace6fc000` | FilePage other | `rw-p` | 108 | 12 | 8 | 0 | 0 | 0.00% | `[anon:libddgr.z.so.bss]` |
| `005ace6fc000-005ace700000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/pluginComponent.abc` |
| `005ace700000-005ace72d000` | .so | `r--p` | 180 | 56 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmmi-util.z.so` |
| `005ace72d000-005ace762000` | .so | `r-xp` | 212 | 116 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmmi-util.z.so` |
| `005ace762000-005ace765000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmmi-util.z.so` |
| `005ace765000-005ace767000` | .so | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmmi-util.z.so` |
| `005ace767000-005ace770000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/pipwindow_ani.abc` |
| `005ace770000-005ace776000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/power_abc.abc` |
| `005ace776000-005ace780000` | FilePage other | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/preferences_abc.abc` |
| `005ace780000-005ace782000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprocess_options.z.so` |
| `005ace782000-005ace785000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprocess_options.z.so` |
| `005ace785000-005ace786000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprocess_options.z.so` |
| `005ace786000-005ace787000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprocess_options.z.so` |
| `005ace787000-005ace7bb000` | FilePage other | `r--p` | 208 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/os_account_abc.abc` |
| `005ace7bb000-005ace7bc000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/print_extension_context_abc.abc` |
| `005ace7bc000-005ace7bd000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/prompt.abc` |
| `005ace7bd000-005ace7c0000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/quick_fix_manager.abc` |
| `005ace7c0000-005ace7ce000` | .so | `r--p` | 56 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libinputmethod_common.z.so` |
| `005ace7ce000-005ace7df000` | .so | `r-xp` | 68 | 24 | 2 | 0 | 0 | 0.00% | `/system/lib64/libinputmethod_common.z.so` |
| `005ace7df000-005ace7e4000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinputmethod_common.z.so` |
| `005ace7e4000-005ace7e5000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinputmethod_common.z.so` |
| `005ace7e5000-005ace7f7000` | FilePage other | `r--p` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/pointer.abc` |
| `005ace7f7000-005ace7fe000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/privacy_indicator_manager_abc.abc` |
| `005ace7fe000-005ace800000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/recoverable_application_info.abc` |
| `005ace800000-005ace803000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmission_info.z.so` |
| `005ace803000-005ace806000` | .so | `r-xp` | 12 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmission_info.z.so` |
| `005ace806000-005ace807000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmission_info.z.so` |
| `005ace807000-005ace808000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmission_info.z.so` |
| `005ace808000-005ace827000` | FilePage other | `r--p` | 124 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/print.abc` |
| `005ace827000-005ace831000` | FilePage other | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/privacy_manager.abc` |
| `005ace831000-005ace83f000` | FilePage other | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/promptAction.abc` |
| `005ace83f000-005ace840000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/remote_ability_info.abc` |
| `005ace840000-005ace849000` | .so | `r--p` | 36 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindowstage_kit.z.so` |
| `005ace849000-005ace85b000` | .so | `r-xp` | 72 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindowstage_kit.z.so` |
| `005ace85b000-005ace85d000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindowstage_kit.z.so` |
| `005ace85d000-005ace85e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindowstage_kit.z.so` |
| `005ace85e000-005ace866000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/proxychannelmanager_taihe_ani.abc` |
| `005ace866000-005ace87d000` | FilePage other | `r--p` | 92 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/reminder_agent_manager_abc.abc` |
| `005ace87d000-005ace87e000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/scene_session_manager_abc.abc` |
| `005ace87e000-005ace880000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/screen_lock_file_manager.abc` |
| `005ace911000-005ace92c000` | FilePage other | `r--p` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/request.abc` |
| `005ace92c000-005ace93d000` | FilePage other | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/rpc_taihe_abc.abc` |
| `005ace93d000-005ace93f000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/selection_extension_ability_ani.abc` |
| `005ace93f000-005ace940000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/static_subscriber_extension_ability.abc` |
| `005ace940000-005ace95c000` | .so | `r--p` | 112 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpowermgr_client.z.so` |
| `005ace95c000-005ace97d000` | .so | `r-xp` | 132 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpowermgr_client.z.so` |
| `005ace97d000-005ace98e000` | .so | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpowermgr_client.z.so` |
| `005ace98e000-005ace98f000` | .so | `rw-p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpowermgr_client.z.so` |
| `005ace98f000-005ace995000` | GL | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/runningLock_abc.abc` |
| `005ace995000-005ace99f000` | FilePage other | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/scan.abc` |
| `005ace99f000-005ace9a5000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/screenLock_static.abc` |
| `005ace9a5000-005ace9b2000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/screen_abc.abc` |
| `005ace9b2000-005ace9b7000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/screenshot_abc.abc` |
| `005ace9b7000-005ace9c0000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/selectionManager.abc` |
| `005ace9c0000-005ace9c8000` | .so | `r--p` | 32 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributed_sdk.z.so` |
| `005ace9c8000-005ace9d3000` | .so | `r-xp` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributed_sdk.z.so` |
| `005ace9d3000-005ace9d7000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributed_sdk.z.so` |
| `005ace9d7000-005ace9d8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributed_sdk.z.so` |
| `005ace9d8000-005ace9d9000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdistributed_sdk.z.so.bss]` |
| `005ace9d9000-005ace9f7000` | FilePage other | `r--p` | 120 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/sensor_abc.abc` |
| `005ace9f7000-005acea00000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/service_extension_ability.abc` |
| `005acea00000-005acea09000` | .so | `r--p` | 36 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension_connection.z.so` |
| `005acea09000-005acea11000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension_connection.z.so` |
| `005acea11000-005acea14000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension_connection.z.so` |
| `005acea14000-005acea15000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension_connection.z.so` |
| `005acea15000-005acea16000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libui_service_extension_connection.z.so.bss]` |
| `005acea16000-005acea1c000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/settings.abc` |
| `005acea1c000-005acea1f000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/shape_ani.abc` |
| `005acea1f000-005acea21000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/share_bundle_info.abc` |
| `005acea21000-005acea27000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/sharing.abc` |
| `005acea27000-005acea2d000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/short_key.abc` |
| `005acea2d000-005acea30000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/shortcut_info.abc` |
| `005acea30000-005acea34000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/shortcut_manager.abc` |
| `005acea34000-005acea36000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/skill.abc` |
| `005acea36000-005acea3f000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/spatialAwareness_abc.abc` |
| `005acea3f000-005acea40000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/systemprompt.abc` |
| `005acea40000-005acea44000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libability_madvise.z.so` |
| `005acea44000-005acea4b000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libability_madvise.z.so` |
| `005acea4b000-005acea4c000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libability_madvise.z.so` |
| `005acea4c000-005acea4d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libability_madvise.z.so` |
| `005acea4d000-005acea58000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/soundpool_taihe_abc.abc` |
| `005acea58000-005acea5a000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/static_subscriber_extension_context.abc` |
| `005acea5a000-005acea63000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/statistics.abc` |
| `005acea63000-005acea6f000` | FilePage other | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/storage_statistics_taihe_abc.abc` |
| `005acea6f000-005acea71000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/super_privacy_manager_abc.abc` |
| `005acea71000-005acea76000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/systemCapability.abc` |
| `005acea76000-005acea7b000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/systemData.abc` |
| `005acea7b000-005acea7f000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/telephony_observer.abc` |
| `005acea7f000-005acea80000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/telephony_vsim.abc` |
| `005acea80000-005acea9a000` | .so | `r--p` | 104 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/libdlp_permission_sdk.z.so` |
| `005acea9a000-005aceac3000` | .so | `r-xp` | 164 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlp_permission_sdk.z.so` |
| `005aceac3000-005aceacc000` | .so | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlp_permission_sdk.z.so` |
| `005aceacc000-005aceacd000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlp_permission_sdk.z.so` |
| `005aceacd000-005acead3000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/systemParameterEnhance.abc` |
| `005acead3000-005aceaf2000` | FilePage other | `r--p` | 124 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/system_sound_manager_taihe_abc.abc` |
| `005aceaf2000-005aceaf9000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/systemdatetime_abc.abc` |
| `005aceaf9000-005aceaff000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/systemload_abc.abc` |
| `005aceaff000-005aceb00000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/thememanager.abc` |
| `005aceb00000-005aceb49000` | .so | `r--p` | 292 | 100 | 6 | 0 | 0 | 0.00% | `/system/lib64/librosen_text.z.so` |
| `005aceb49000-005acec09000` | .so | `r-xp` | 768 | 512 | 45 | 0 | 0 | 0.00% | `/system/lib64/librosen_text.z.so` |
| `005acec09000-005acec10000` | .so | `r--p` | 28 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/librosen_text.z.so` |
| `005acec10000-005acec11000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/librosen_text.z.so` |
| `005acec11000-005acec12000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:librosen_text.z.so.bss]` |
| `005acec12000-005acec19000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/systemtimer_abc.abc` |
| `005acec19000-005acec21000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/telephony_data.abc` |
| `005acec21000-005acec28000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/telephony_enhanced.abc` |
| `005acec28000-005acec2b000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/telephony_vcard.abc` |
| `005acec2b000-005acec30000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/thermal_abc.abc` |
| `005acec30000-005acec3a000` | FilePage other | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/touch_event.abc` |
| `005acec3a000-005acec3b000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ui_service_extension_connect_callback_abc.abc` |
| `005acec3b000-005acec3e000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ui_service_extension_context_abc.abc` |
| `005acec3e000-005acec3f000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ui_service_host_proxy_abc.abc` |
| `005acec3f000-005acec40000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ui_service_proxy_abc.abc` |
| `005acecd6000-005acecd7000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libdatashare_consumer.z.so.bss]` |
| `005acecd7000-005acecf4000` | FilePage other | `r--p` | 116 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/telephony_radio_abc.abc` |
| `005acecf4000-005acecff000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ui_extension_ability_ani.abc` |
| `005acecff000-005aced00000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/user_auth_extension.abc` |
| `005aced00000-005aced05000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmodal_system_ui_extension_client.z.so` |
| `005aced05000-005aced09000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmodal_system_ui_extension_client.z.so` |
| `005aced09000-005aced0b000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmodal_system_ui_extension_client.z.so` |
| `005aced0b000-005aced0c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmodal_system_ui_extension_client.z.so` |
| `005aced0c000-005aced40000` | FilePage other | `r--p` | 208 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/relationalstore.abc` |
| `005aced40000-005acedd8000` | .so | `r--p` | 608 | 148 | 22 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_native.z.so` |
| `005acedd8000-005acee75000` | .so | `r-xp` | 628 | 552 | 23 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_native.z.so` |
| `005acee75000-005acee80000` | .so | `r--p` | 44 | 44 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_native.z.so` |
| `005acee80000-005acee81000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_native.z.so` |
| `005acee81000-005acee83000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libappkit_native.z.so.bss]` |
| `005acee83000-005acee9f000` | FilePage other | `r--p` | 112 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/telephony_sim.abc` |
| `005acee9f000-005aceebc000` | FilePage other | `r--p` | 116 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/text_engine.abc` |
| `005aceebc000-005aceebf000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/uri_permission_manager.abc` |
| `005aceebf000-005aceec0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/workscheduler_extension_ability_abc.abc` |
| `005aceec0000-005aceec8000` | .so | `r--p` | 32 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapp_domain_verify_common.z.so` |
| `005aceec8000-005aceed2000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapp_domain_verify_common.z.so` |
| `005aceed2000-005aceed5000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapp_domain_verify_common.z.so` |
| `005aceed5000-005aceed6000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapp_domain_verify_common.z.so` |
| `005aceed6000-005aceee9000` | FilePage other | `r--p` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/udmf_components_ets_abc.abc` |
| `005aceee9000-005aceef6000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/uiEffect_taihe_abc.abc` |
| `005aceef6000-005aceefc000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/underageModel_abc.abc` |
| `005aceefc000-005aceefe000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/web_native_messaging_extension_ability.abc` |
| `005aceefe000-005acef00000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/web_native_messaging_extension_context.abc` |
| `005acef00000-005acef6c000` | .so | `r--p` | 432 | 100 | 7 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libprotobuf_lite.z.so` |
| `005acef6c000-005acf01a000` | .so | `r-xp` | 696 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libprotobuf_lite.z.so` |
| `005acf01a000-005acf01f000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libprotobuf_lite.z.so` |
| `005acf01f000-005acf020000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libprotobuf_lite.z.so` |
| `005acf020000-005acf023000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libprotobuf_lite.z.so.bss]` |
| `005acf023000-005acf03e000` | FilePage other | `r--p` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/update_ani.abc` |
| `005acf03e000-005acf03f000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/workscheduler_extension_context_abc.abc` |
| `005acf03f000-005acf040000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/custom_config.abc` |
| `005acf040000-005acf05a000` | .so | `r--p` | 104 | 64 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwantagent_innerkits.z.so` |
| `005acf05a000-005acf076000` | .so | `r-xp` | 112 | 100 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwantagent_innerkits.z.so` |
| `005acf076000-005acf07a000` | .so | `r--p` | 16 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwantagent_innerkits.z.so` |
| `005acf07a000-005acf07b000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwantagent_innerkits.z.so` |
| `005acf07b000-005acf07e000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/web_native_messaging_extension_manager.abc` |
| `005acf07e000-005acf080000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/adminManager.abc` |
| `005acf080000-005acf084000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_handler.z.so` |
| `005acf084000-005acf087000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_handler.z.so` |
| `005acf087000-005acf089000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_handler.z.so` |
| `005acf089000-005acf08a000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_handler.z.so` |
| `005acf08a000-005acf093000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/urpc_ani_abc.abc` |
| `005acf093000-005acf0a8000` | FilePage other | `r--p` | 84 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/usb_manager_abc.abc` |
| `005acf0a8000-005acf0b1000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/usbmanager_serial_abc.abc` |
| `005acf0b1000-005acf0b7000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/user_auth_icon_ets_abc.abc` |
| `005acf0b7000-005acf0be000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/userfile_manager.abc` |
| `005acf0be000-005acf0c0000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/fontManager.abc` |
| `005acf0c0000-005acf0c3000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_forward_compatibility.z.so` |
| `005acf0c3000-005acf0c7000` | .so | `r-xp` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_forward_compatibility.z.so` |
| `005acf0c7000-005acf0c8000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_forward_compatibility.z.so` |
| `005acf0c8000-005acf0c9000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_forward_compatibility.z.so` |
| `005acf0c9000-005acf100000` | FilePage other | `r--p` | 220 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/udmf_abc.abc` |
| `005acf100000-005acf156000` | .so | `r--p` | 344 | 168 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmmi-client.z.so` |
| `005acf156000-005acf212000` | .so | `r-xp` | 752 | 304 | 15 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmmi-client.z.so` |
| `005acf212000-005acf21c000` | .so | `r--p` | 40 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmmi-client.z.so` |
| `005acf21c000-005acf21d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmmi-client.z.so` |
| `005acf21d000-005acf21e000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libmmi-client.z.so.bss]` |
| `005acf21e000-005acf22d000` | FilePage other | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/vibrator_abc.abc` |
| `005acf22d000-005acf234000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/video_processing_engine_taihe_abc.abc` |
| `005acf234000-005acf23c000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/volume_manager_taihe_abc.abc` |
| `005acf23c000-005acf240000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/configPolicy.abc` |
| `005acf240000-005acf242000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdatabase_utils.z.so` |
| `005acf242000-005acf246000` | .so | `r-xp` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdatabase_utils.z.so` |
| `005acf246000-005acf247000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdatabase_utils.z.so` |
| `005acf247000-005acf248000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdatabase_utils.z.so` |
| `005acf248000-005acf251000` | FilePage other | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/wallpapermgr.abc` |
| `005acf251000-005acf25c000` | FilePage other | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/web_innerUI.abc` |
| `005acf25c000-005acf266000` | FilePage other | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/websocket.abc` |
| `005acf266000-005acf26e000` | FilePage other | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/window_animation_manager_ets.abc` |
| `005acf26e000-005acf278000` | FilePage other | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/work_scheduler_abc.abc` |
| `005acf278000-005acf27e000` | FilePage other | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms.hiviewdfx.infosec.abc` |
| `005acf27e000-005acf27f000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/mediaquery.abc` |
| `005acf27f000-005acf280000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/memmgr.abc` |
| `005acf280000-005acf2a5000` | .so | `r--p` | 148 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_thread.z.so` |
| `005acf2a5000-005acf2bf000` | .so | `r-xp` | 104 | 68 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_thread.z.so` |
| `005acf2bf000-005acf2c8000` | .so | `r--p` | 36 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_thread.z.so` |
| `005acf2c8000-005acf2c9000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_thread.z.so` |
| `005acf2c9000-005acf2f8000` | FilePage other | `r--p` | 188 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/web_webview.abc` |
| `005acf2f8000-005acf2fd000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/hms.userIAM.fingerAuthManager.abc` |
| `005acf2fd000-005acf300000` | FilePage other | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/matrix4.abc` |
| `005acf317000-005acf33b000` | FilePage other | `r--p` | 144 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/wifiManager_framework_abc.abc` |
| `005acf33b000-005acf33f000` | FilePage other | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/networkManager.abc` |
| `005acf33f000-005acf340000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/rawFileDescriptor.abc` |
| `005acf340000-005acf345000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libembeddablewindowstage_kit.z.so` |
| `005acf345000-005acf34e000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libembeddablewindowstage_kit.z.so` |
| `005acf34e000-005acf34f000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libembeddablewindowstage_kit.z.so` |
| `005acf34f000-005acf350000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libembeddablewindowstage_kit.z.so` |
| `005acf350000-005acf36a000` | FilePage other | `r--p` | 104 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/window_titlebar_component_abc.abc` |
| `005acf36a000-005acf37e000` | FilePage other | `r--p` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/i18n.abc` |
| `005acf37e000-005acf380000` | FilePage other | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/performanceMonitor.abc` |
| `005acf380000-005acf389000` | .so | `r--p` | 36 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libforeground_app_obs_manager.z.so` |
| `005acf389000-005acf393000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libforeground_app_obs_manager.z.so` |
| `005acf393000-005acf397000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libforeground_app_obs_manager.z.so` |
| `005acf397000-005acf398000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libforeground_app_obs_manager.z.so` |
| `005acf398000-005acf3b9000` | FilePage other | `r--p` | 132 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/zlib.abc` |
| `005acf3b9000-005acf3c0000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/intl.abc` |
| `005acf3c0000-005acf400000` | .so | `r--p` | 256 | 100 | 9 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_napi.z.so` |
| `005acf400000-005acf4b1000` | .so | `r-xp` | 708 | 588 | 107 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_napi.z.so` |
| `005acf4b1000-005acf4bb000` | .so | `r--p` | 40 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_napi.z.so` |
| `005acf4bb000-005acf4bc000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_napi.z.so` |
| `005acf4bc000-005acf4bd000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libimage_napi.z.so.bss]` |
| `005acf4bd000-005acf4be000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/restrictions.abc` |
| `005acf4be000-005acf4bf000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/securityManager.abc` |
| `005acf4bf000-005acf4c0000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ui_appearance_abc.abc` |
| `005acf4c0000-005acf4f9000` | .so | `r--p` | 228 | 128 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_context.z.so` |
| `005acf4f9000-005acf53c000` | .so | `r-xp` | 268 | 252 | 12 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_context.z.so` |
| `005acf53c000-005acf53f000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_context.z.so` |
| `005acf53f000-005acf540000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_context.z.so` |
| `005acf540000-005acf541000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libapp_context.z.so.bss]` |
| `005acf541000-005acf548000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/linkEnhance_taihe_ani.abc` |
| `005acf548000-005acf54d000` | FilePage other | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ohos.userIAM.faceAuth.abc` |
| `005acf54d000-005acf554000` | FilePage other | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ohos.userIAM.userAccessCtrl.abc` |
| `005acf554000-005acf561000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/resourceManager.abc` |
| `005acf561000-005acf572000` | FilePage other | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/usage_statistics_abc.abc` |
| `005acf572000-005acf57f000` | FilePage other | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/user_auth.abc` |
| `005acf57f000-005acf580000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/app/ability/libextensionability_napi.z.so_15424_2]` |
| `005acf918000-005acfde8000` | GL | `r-xp` | 4928 | 1684 | 132 | 0 | 0 | 0.00% | `/system/lib64/librender_service_base.z.so` |
| `005acfde8000-005acfe5c000` | GL | `r--p` | 464 | 264 | 19 | 0 | 0 | 0.00% | `/system/lib64/librender_service_base.z.so` |
| `005acfe5c000-005acfe5d000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/librender_service_base.z.so` |
| `005acfe5d000-005acfe69000` | GL | `rw-p` | 48 | 44 | 44 | 0 | 0 | 0.00% | `[anon:librender_service_base.z.so.bss]` |
| `005acfe69000-005acfe79000` | native heap | `rw-p` | 64 | 64 | 3 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfe79000-005acfe7a000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/app/ability/libuiability.z.so_15360_1]` |
| `005acfe7a000-005acfe7e000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfe7e000-005acfe80000` | FilePage other | `rw-p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/application/libcallee_napi.z.so_15360_1]` |
| `005acfe80000-005acfe89000` | .so | `r--p` | 36 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimage_proxy_2.1.z.so` |
| `005acfe89000-005acfe92000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimage_proxy_2.1.z.so` |
| `005acfe92000-005acfe94000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimage_proxy_2.1.z.so` |
| `005acfe94000-005acfe95000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimage_proxy_2.1.z.so` |
| `005acfe95000-005acfe9d000` | native heap | `rw-p` | 32 | 32 | 28 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfe9d000-005acfe9e000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/app/ability/libuiextensionability_napi.z.so_15440_2]` |
| `005acfe9e000-005acfe9f000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/application/libability_napi.z.so_15376_1]` |
| `005acfe9f000-005acfea0000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/application/libabilitystage_napi.z.so_15408_1]` |
| `005acfea0000-005acfea1000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/application/libabilitystagecontext_napi.z.so_15440_2]` |
| `005acfea1000-005acfea2000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfea2000-005acfea5000` | FilePage other | `rw-p` | 12 | 12 | 1 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/application/libabilitycontext_napi.z.so_15408_1]` |
| `005acfea8000-005acfeab000` | FilePage other | `rw-p` | 12 | 12 | 1 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/application/libcaller_napi.z.so_15360_1]` |
| `005acfeab000-005acfeaf000` | FilePage other | `rw-p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/application/libapplicationcontext_napi.z.so_15440_2]` |
| `005acfeaf000-005acfeb0000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/application/libextensioncontext_napi.z.so_15424_2]` |
| `005acfeb0000-005acfeb1000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/application/libserviceextensionability_napi.z.so_15472_2]` |
| `005acfeb1000-005acfeb3000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/application/libserviceextensioncontext_napi.z.so_15472_2]` |
| `005acfeb3000-005acfeb4000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/application/libwindowstage.z.so_21400_1]` |
| `005acfeb4000-005acfeb5000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfeb5000-005acfebe000` | native heap | `rw-p` | 36 | 36 | 36 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfebe000-005acfec0000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/hms/core/libauthentication.z.so_234736_1]` |
| `005acfec0000-005acfec1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_register.z.so` |
| `005acfec1000-005acfec2000` | .so | `r-xp` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_register.z.so` |
| `005acfec2000-005acfec3000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_register.z.so` |
| `005acfec3000-005acfec4000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_register.z.so` |
| `005acfec4000-005acfec8000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/libcontact.z.so_421360_1]` |
| `005acfec8000-005acfeca000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfeca000-005acfecb000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/libmeasure.z.so_136576_1]` |
| `005acfecb000-005acfecd000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/libpromptaction.z.so_278024_1]` |
| `005acfecd000-005acfece000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfece000-005acfecf000` | FilePage other | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/hiappevent/databases/appevent.db-dwr` |
| `005acfecf000-005acfedb000` | native heap | `rw-p` | 48 | 48 | 17 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfedb000-005acfede000` | native heap | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfeec000-005acfeed000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfeed000-005acfef3000` | FilePage other | `rw-p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/file/libpicker.z.so_177640_1]` |
| `005acfef3000-005acfeff000` | native heap | `rw-p` | 48 | 48 | 17 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acfeff000-005acff00000` | FilePage other | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/hiappevent/databases/appevent.db-dwr` |
| `005acff00000-005acff12000` | .so | `r--p` | 72 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmemmgrclient.z.so` |
| `005acff12000-005acff31000` | .so | `r-xp` | 124 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmemmgrclient.z.so` |
| `005acff31000-005acff37000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmemmgrclient.z.so` |
| `005acff37000-005acff38000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmemmgrclient.z.so` |
| `005acff38000-005acff3c000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acff3c000-005acff40000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acff40000-005acff42000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpixelconvertadapter.z.so` |
| `005acff42000-005acff46000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpixelconvertadapter.z.so` |
| `005acff46000-005acff47000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpixelconvertadapter.z.so` |
| `005acff47000-005acff48000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpixelconvertadapter.z.so` |
| `005acff48000-005acff52000` | native heap | `rw-p` | 40 | 40 | 5 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acff52000-005acff58000` | FilePage other | `rw-p` | 24 | 20 | 1 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/liburl.z.so_219416_1]` |
| `005acff58000-005acff78000` | native heap | `rw-p` | 128 | 128 | 7 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acff78000-005acff80000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acff80000-005acff93000` | .so | `r--p` | 76 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpluginmanager.z.so` |
| `005acff93000-005acffb4000` | .so | `r-xp` | 132 | 48 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpluginmanager.z.so` |
| `005acffb4000-005acffb6000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpluginmanager.z.so` |
| `005acffb6000-005acffb7000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpluginmanager.z.so` |
| `005acffb7000-005acffbf000` | native heap | `rw-p` | 32 | 32 | 1 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005acffbf000-005acffc0000` | FilePage other | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/hiappevent/databases/appevent.db-dwr` |
| `005acffc0000-005ad00d1000` | Graph | `r--p` | 1092 | 304 | 12 | 0 | 0 | 0.00% | `/system/lib64/lib2d_graphics.z.so` |
| `005ad00d1000-005ad02a0000` | Graph | `r-xp` | 1852 | 768 | 53 | 0 | 0 | 0.00% | `/system/lib64/lib2d_graphics.z.so` |
| `005ad02a0000-005ad02b8000` | Graph | `r--p` | 96 | 72 | 3 | 0 | 0 | 0.00% | `/system/lib64/lib2d_graphics.z.so` |
| `005ad02b8000-005ad02b9000` | Graph | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/lib2d_graphics.z.so` |
| `005ad02b9000-005ad02c0000` | Graph | `rw-p` | 28 | 4 | 4 | 0 | 0 | 0.00% | `[anon:lib2d_graphics.z.so.bss]` |
| `005ad02c0000-005ad02c5000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libperm_verification.z.so` |
| `005ad02c5000-005ad02cb000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libperm_verification.z.so` |
| `005ad02cb000-005ad02cc000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libperm_verification.z.so` |
| `005ad02cc000-005ad02cd000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libperm_verification.z.so` |
| `005ad02cd000-005ad02fd000` | native heap | `rw-p` | 192 | 192 | 10 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad02fd000-005ad02fe000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad02fe000-005ad02ff000` | GL | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/database/rdb/Bugly_database.db-dwr` |
| `005ad02ff000-005ad0300000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:accessibility_param:s0` |
| `005ad0300000-005ad031f000` | .so | `r--p` | 124 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/libdistributed_file_daemon_kit_inner.z.so` |
| `005ad031f000-005ad0351000` | .so | `r-xp` | 200 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdistributed_file_daemon_kit_inner.z.so` |
| `005ad0351000-005ad0359000` | .so | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdistributed_file_daemon_kit_inner.z.so` |
| `005ad0359000-005ad035a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdistributed_file_daemon_kit_inner.z.so` |
| `005ad035a000-005ad035b000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libdistributed_file_daemon_kit_inner.z.so.bss]` |
| `005ad035b000-005ad037f000` | native heap | `rw-p` | 144 | 144 | 23 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad037f000-005ad0380000` | dev | `r--s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/shared_memory/94CD5B6F2C41FAE18F96D8F59925CC86` |
| `005ad0380000-005ad0390000` | .so | `r--p` | 64 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsystem_ability_fwk.z.so` |
| `005ad0390000-005ad03a8000` | .so | `r-xp` | 96 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsystem_ability_fwk.z.so` |
| `005ad03a8000-005ad03ac000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsystem_ability_fwk.z.so` |
| `005ad03ac000-005ad03ad000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsystem_ability_fwk.z.so` |
| `005ad03ad000-005ad03bd000` | native heap | `rw-p` | 64 | 64 | 3 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad03bd000-005ad03bf000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/arkts/libutils.z.so_136736_1]` |
| `005ad03bf000-005ad03c0000` | FilePage other | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/mmkv/DY_DEFAULT_MAP_ID.crc` |
| `005ad03c0000-005ad03c7000` | .so | `r--p` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeablemem.z.so` |
| `005ad03c7000-005ad03d1000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeablemem.z.so` |
| `005ad03d1000-005ad03d2000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeablemem.z.so` |
| `005ad03d2000-005ad03d3000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeablemem.z.so` |
| `005ad03d3000-005ad03ff000` | native heap | `rw-p` | 176 | 176 | 24 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad03ff000-005ad0400000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:hiviewdfx_profiler_param:s0` |
| `005ad0400000-005ad0405000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandboxlog.so` |
| `005ad0405000-005ad040f000` | .so | `r-xp` | 40 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandboxlog.so` |
| `005ad040f000-005ad0410000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandboxlog.so` |
| `005ad0410000-005ad0411000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandboxlog.so` |
| `005ad0411000-005ad0439000` | native heap | `rw-p` | 160 | 160 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0439000-005ad0440000` | FilePage other | `rw-p` | 28 | 28 | 28 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/hms/filemanagement/libfilepreview_napi.z.so_15904_2]` |
| `005ad0440000-005ad044e000` | .so | `r--p` | 56 | 36 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libarkweb_core_loader.z.so` |
| `005ad044e000-005ad0467000` | .so | `r-xp` | 100 | 40 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libarkweb_core_loader.z.so` |
| `005ad0467000-005ad0468000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libarkweb_core_loader.z.so` |
| `005ad0468000-005ad0469000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libarkweb_core_loader.z.so` |
| `005ad0469000-005ad0479000` | native heap | `rw-p` | 64 | 64 | 3 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0479000-005ad047a000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad047a000-005ad047b000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad047b000-005ad047d000` | FilePage other | `rw-p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/util/libjson.z.so_21432_1]` |
| `005ad047d000-005ad047f000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/statemanagement.abc]` |
| `005ad047f000-005ad0480000` | FilePage other | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/imsdk_config_1400029396.meta` |
| `005ad0480000-005ad0490000` | .so | `r--p` | 64 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsight_intent_executor.z.so` |
| `005ad0490000-005ad04a2000` | .so | `r-xp` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsight_intent_executor.z.so` |
| `005ad04a2000-005ad04a4000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsight_intent_executor.z.so` |
| `005ad04a4000-005ad04a5000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsight_intent_executor.z.so` |
| `005ad04a5000-005ad04a6000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libinsight_intent_executor.z.so.bss]` |
| `005ad04a6000-005ad04be000` | native heap | `rw-p` | 96 | 96 | 5 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad04be000-005ad04c0000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad04c0000-005ad0507000` | .so | `r--p` | 284 | 88 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_native_kit.z.so` |
| `005ad0507000-005ad05c2000` | .so | `r-xp` | 748 | 332 | 35 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_native_kit.z.so` |
| `005ad05c2000-005ad05cd000` | .so | `r--p` | 44 | 40 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_native_kit.z.so` |
| `005ad05cd000-005ad05ce000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_native_kit.z.so` |
| `005ad05ce000-005ad05cf000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libwindow_native_kit.z.so.bss]` |
| `005ad05cf000-005ad05ff000` | native heap | `rw-p` | 192 | 192 | 10 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad05ff000-005ad0600000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:i18n_param:s0` |
| `005ad0600000-005ad060c000` | .so | `r--p` | 48 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_strings.z.so` |
| `005ad060c000-005ad0618000` | .so | `r-xp` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_strings.z.so` |
| `005ad0618000-005ad0619000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_strings.z.so` |
| `005ad0619000-005ad061a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_strings.z.so` |
| `005ad061a000-005ad063a000` | native heap | `rw-p` | 128 | 128 | 7 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad063a000-005ad063e000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad063e000-005ad063f000` | GL | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/database/rdb/Bugly_database.db-dwr` |
| `005ad063f000-005ad0640000` | GL | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/database/rdb/Bugly_database.db-dwr` |
| `005ad0640000-005ad0659000` | .so | `r--p` | 100 | 100 | 13 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libexif.z.so` |
| `005ad0659000-005ad0670000` | .so | `r-xp` | 92 | 88 | 14 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libexif.z.so` |
| `005ad0670000-005ad0687000` | .so | `r--p` | 92 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libexif.z.so` |
| `005ad0687000-005ad0688000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libexif.z.so` |
| `005ad0688000-005ad0698000` | native heap | `rw-p` | 64 | 64 | 3 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0698000-005ad069c000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad06a7000-005ad06a9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad06a9000-005ad06b0000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30011]` |
| `005ad06b0000-005ad06b2000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad06b2000-005ad06b9000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30012]` |
| `005ad06b9000-005ad06bd000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad06bd000-005ad06c0000` | FilePage other | `rw-p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/telephony/libcall.z.so_258072_1]` |
| `005ad06c0000-005ad06c4000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcolor_space_object_convertor.z.so` |
| `005ad06c4000-005ad06ca000` | .so | `r-xp` | 24 | 24 | 18 | 0 | 0 | 0.00% | `/system/lib64/libcolor_space_object_convertor.z.so` |
| `005ad06ca000-005ad06cc000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libcolor_space_object_convertor.z.so` |
| `005ad06cc000-005ad06cd000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcolor_space_object_convertor.z.so` |
| `005ad06cd000-005ad06cf000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad06cf000-005ad06d6000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30013]` |
| `005ad06d6000-005ad06d8000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad06d8000-005ad06df000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30014]` |
| `005ad06df000-005ad06e1000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad06e1000-005ad06e8000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30015]` |
| `005ad06e8000-005ad06ea000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad06ea000-005ad06f1000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30016]` |
| `005ad06f1000-005ad06f3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad06f3000-005ad06fa000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30018]` |
| `005ad06fa000-005ad06fe000` | native heap | `rw-p` | 16 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad06fe000-005ad06ff000` | GL | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/database/rdb/Bugly_database.db-dwr` |
| `005ad06ff000-005ad0700000` | GL | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/database/rdb/Bugly_database.db-dwr` |
| `005ad0700000-005ad0716000` | .so | `r--p` | 88 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsms.z.so` |
| `005ad0716000-005ad0756000` | .so | `r-xp` | 256 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsms.z.so` |
| `005ad0756000-005ad075e000` | .so | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsms.z.so` |
| `005ad075e000-005ad075f000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsms.z.so` |
| `005ad075f000-005ad0761000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0761000-005ad0768000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30020]` |
| `005ad0768000-005ad076a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad076a000-005ad0771000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30635]` |
| `005ad0771000-005ad0773000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0773000-005ad077a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30022]` |
| `005ad077a000-005ad077e000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad077e000-005ad077f000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad077f000-005ad0780000` | FilePage other | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/database/entry/rdb/RKStorage.db-dwr` |
| `005ad0780000-005ad0784000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_base.z.so` |
| `005ad0784000-005ad0788000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_base.z.so` |
| `005ad0788000-005ad0789000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_base.z.so` |
| `005ad0789000-005ad078a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_base.z.so` |
| `005ad078a000-005ad078c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad078c000-005ad0793000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30023]` |
| `005ad0793000-005ad07b5000` | FilePage other | `rw-p` | 136 | 136 | 136 | 0 | 0 | 0.00% | `[anon:ArkTS MethodLiteral]` |
| `005ad07b5000-005ad07b7000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad07b7000-005ad07be000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30024]` |
| `005ad07be000-005ad07c0000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad07c0000-005ad07c7000` | GL | `r--p` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpost_proc_gl.z.so` |
| `005ad07c7000-005ad07d3000` | GL | `r-xp` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpost_proc_gl.z.so` |
| `005ad07d3000-005ad07d5000` | GL | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpost_proc_gl.z.so` |
| `005ad07d5000-005ad07d6000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpost_proc_gl.z.so` |
| `005ad07d6000-005ad07f0000` | FilePage other | `rw-p` | 104 | 104 | 104 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/modifier.abc]` |
| `005ad07f0000-005ad07f2000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad07f2000-005ad07f9000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30025]` |
| `005ad07f9000-005ad07fc000` | FilePage other | `rw-p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/hms/core/scan/libscanbarcode_napi.z.so_21432_1]` |
| `005ad07fc000-005ad0800000` | FilePage other | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/advertising/libautoadcomponent.z.so_21368_1]` |
| `005ad0800000-005ad0805000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_ipc.z.so` |
| `005ad0805000-005ad080b000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_ipc.z.so` |
| `005ad080b000-005ad080d000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_ipc.z.so` |
| `005ad080d000-005ad080e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_ipc.z.so` |
| `005ad080e000-005ad0836000` | native heap | `rw-p` | 160 | 160 | 160 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0836000-005ad0838000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0838000-005ad083f000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30026]` |
| `005ad083f000-005ad0840000` | FilePage other | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/database/entry/rdb/RKStorage.db-dwr` |
| `005ad0840000-005ad0841000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_spinlock_wait.z.so` |
| `005ad0841000-005ad0842000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_spinlock_wait.z.so` |
| `005ad0842000-005ad0843000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_spinlock_wait.z.so` |
| `005ad0843000-005ad0844000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_spinlock_wait.z.so` |
| `005ad0844000-005ad0872000` | FilePage other | `rw-p` | 184 | 184 | 184 | 0 | 0 | 0.00% | `[anon:ArkTS Code:390493358912]` |
| `005ad0872000-005ad087a000` | FilePage other | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/hiappevent/databases/appevent.db-shm` |
| `005ad087a000-005ad087f000` | FilePage other | `rw-p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/libadvertising.z.so_178384_1]` |
| `005ad087f000-005ad0880000` | FilePage other | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/database/entry/rdb/RKStorage.db-dwr` |
| `005ad0880000-005ad08f7000` | Graph | `r--p` | 476 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libgraphics_effect.z.so` |
| `005ad08f7000-005ad09ab000` | Graph | `r-xp` | 720 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libgraphics_effect.z.so` |
| `005ad09ab000-005ad09b9000` | Graph | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libgraphics_effect.z.so` |
| `005ad09b9000-005ad09bb000` | Graph | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libgraphics_effect.z.so` |
| `005ad09bb000-005ad09bd000` | Graph | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libgraphics_effect.z.so.bss]` |
| `005ad09bd000-005ad09be000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/shared_memory/58A23466990C8FD77E7FE4A96DE2571F` |
| `005ad09be000-005ad09c0000` | FilePage other | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/ShaderCache/data_0` |
| `005ad09c0000-005ad0a84000` | GL | `r--p` | 784 | 180 | 7 | 0 | 0 | 0.00% | `/system/lib64/librender_service_client.z.so` |
| `005ad0a84000-005ad0cbb000` | GL | `r-xp` | 2268 | 1148 | 85 | 0 | 0 | 0.00% | `/system/lib64/librender_service_client.z.so` |
| `005ad0cbb000-005ad0ccd000` | GL | `r--p` | 72 | 60 | 2 | 0 | 0 | 0.00% | `/system/lib64/librender_service_client.z.so` |
| `005ad0ccd000-005ad0cce000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/librender_service_client.z.so` |
| `005ad0cce000-005ad0cd2000` | GL | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:librender_service_client.z.so.bss]` |
| `005ad0cd2000-005ad0ce5000` | FilePage other | `rw-p` | 76 | 76 | 76 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/hms/collaboration/librcp.z.so_320352_1]` |
| `005ad0ce5000-005ad0ce7000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad0ce7000-005ad0cee000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad0cee000-005ad0cf0000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0cf0000-005ad0cf7000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30344]` |
| `005ad0cf7000-005ad0cff000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0cff000-005ad0d00000` | FilePage other | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/database/entry/rdb/RKStorage.db-dwr` |
| `005ad0d00000-005ad0d05000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauto_startup_callback.z.so` |
| `005ad0d05000-005ad0d09000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauto_startup_callback.z.so` |
| `005ad0d09000-005ad0d0b000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauto_startup_callback.z.so` |
| `005ad0d0b000-005ad0d0c000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauto_startup_callback.z.so` |
| `005ad0d0c000-005ad0d3a000` | FilePage other | `rw-p` | 184 | 184 | 184 | 0 | 0 | 0.00% | `[anon:ArkTS Code:390751050560]` |
| `005ad0d3a000-005ad0d3e000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0d3e000-005ad0d3f000` | FilePage other | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el2/database/entry/rdb/RKStorage.db-dwr` |
| `005ad0d3f000-005ad0d40000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad0d40000-005ad0d4b000` | .so | `r--p` | 44 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdevicemanagerjson.z.so` |
| `005ad0d4b000-005ad0d5b000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdevicemanagerjson.z.so` |
| `005ad0d5b000-005ad0d5d000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdevicemanagerjson.z.so` |
| `005ad0d5d000-005ad0d5e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdevicemanagerjson.z.so` |
| `005ad0d5e000-005ad0d72000` | native heap | `rw-p` | 80 | 80 | 80 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0d72000-005ad0d78000` | native heap | `rw-p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0d78000-005ad0d80000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0d80000-005ad0d8e000` | .so | `r--p` | 56 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libastc_encoder_shared.z.so` |
| `005ad0d8e000-005ad0da9000` | .so | `r-xp` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libastc_encoder_shared.z.so` |
| `005ad0da9000-005ad0dab000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libastc_encoder_shared.z.so` |
| `005ad0dab000-005ad0dac000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libastc_encoder_shared.z.so` |
| `005ad0dac000-005ad0db0000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libastc_encoder_shared.z.so.bss]` |
| `005ad0db0000-005ad0dbc000` | native heap | `rw-p` | 48 | 48 | 48 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0dbc000-005ad0dbf000` | FilePage other | `rw-s` | 12 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/log/page_switch/.persist_sandbox_log` |
| `005ad0dbf000-005ad0dc0000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad0dc0000-005ad0dc4000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.4.z.so` |
| `005ad0dc4000-005ad0dc8000` | .so | `r-xp` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.4.z.so` |
| `005ad0dc8000-005ad0dca000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.4.z.so` |
| `005ad0dca000-005ad0dcb000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.4.z.so` |
| `005ad0dcb000-005ad0deb000` | native heap | `rw-p` | 128 | 128 | 128 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0deb000-005ad0df5000` | FilePage other | `rw-p` | 40 | 40 | 40 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/web/libwebview_napi.z.so_1094776_1]` |
| `005ad0df5000-005ad0dfd000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0dfd000-005ad0dfe000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad0dfe000-005ad0dff000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad0dff000-005ad0e00000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad0e00000-005ad0e1c000` | .so | `r--p` | 112 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_delegator.z.so` |
| `005ad0e1c000-005ad0e40000` | .so | `r-xp` | 144 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_delegator.z.so` |
| `005ad0e40000-005ad0e43000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_delegator.z.so` |
| `005ad0e43000-005ad0e44000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_delegator.z.so` |
| `005ad0e44000-005ad0e45000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libappkit_delegator.z.so.bss]` |
| `005ad0e45000-005ad0e51000` | FilePage other | `rw-p` | 48 | 48 | 48 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/file/photoaccesshelper.abc]` |
| `005ad0e51000-005ad0e74000` | FilePage other | `rw-p` | 140 | 140 | 140 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/node.abc]` |
| `005ad0e74000-005ad0e76000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0e76000-005ad0e7d000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30037]` |
| `005ad0e7d000-005ad0e7f000` | FilePage other | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/ShaderCache/data_1` |
| `005ad0e7f000-005ad0e80000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/multimedia/libavcastpickerparam.z.so_21368_1]` |
| `005ad0e80000-005ad0e91000` | .so | `r--p` | 68 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdataobs_manager.z.so` |
| `005ad0e91000-005ad0ea7000` | .so | `r-xp` | 88 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdataobs_manager.z.so` |
| `005ad0ea7000-005ad0eab000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdataobs_manager.z.so` |
| `005ad0eab000-005ad0eac000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdataobs_manager.z.so` |
| `005ad0eac000-005ad0ead000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libdataobs_manager.z.so.bss]` |
| `005ad0ead000-005ad0eaf000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0eaf000-005ad0eb6000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30035]` |
| `005ad0eb6000-005ad0eb8000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0eb8000-005ad0ebf000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30038]` |
| `005ad0ebf000-005ad0ec0000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad0ec0000-005ad0ecc000` | .so | `r--p` | 48 | 48 | 4 | 0 | 0 | 0.00% | `/system/lib64/libimf_hisysevent.z.so` |
| `005ad0ecc000-005ad0ee3000` | .so | `r-xp` | 92 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimf_hisysevent.z.so` |
| `005ad0ee3000-005ad0ee6000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimf_hisysevent.z.so` |
| `005ad0ee6000-005ad0ee7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimf_hisysevent.z.so` |
| `005ad0ee7000-005ad0ee8000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libimf_hisysevent.z.so.bss]` |
| `005ad0ee8000-005ad0eea000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0eea000-005ad0ef1000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30039]` |
| `005ad0ef1000-005ad0ef3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0ef3000-005ad0efa000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30041]` |
| `005ad0efa000-005ad0efb000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad0efb000-005ad0eff000` | AnonPage other | `rw-p` | 16 | 4 | 4 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0eff000-005ad0f00000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad0f00000-005ad0f04000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_callback.z.so` |
| `005ad0f04000-005ad0f07000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_callback.z.so` |
| `005ad0f07000-005ad0f09000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_callback.z.so` |
| `005ad0f09000-005ad0f0a000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_callback.z.so` |
| `005ad0f0a000-005ad0f0c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0f0c000-005ad0f13000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30040]` |
| `005ad0f13000-005ad0f23000` | FilePage other | `rw-p` | 64 | 12 | 12 | 0 | 0 | 0.00% | `[anon:absl]` |
| `005ad0f23000-005ad0f25000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0f25000-005ad0f2c000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30042]` |
| `005ad0f2c000-005ad0f2e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0f2e000-005ad0f35000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30043]` |
| `005ad0f35000-005ad0f37000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0f37000-005ad0f3e000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30036]` |
| `005ad0f3e000-005ad0f40000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/multimedia/libavvolumepanel.z.so_21352_1]` |
| `005ad0fe4000-005ad0fe6000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0fe6000-005ad0fed000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30044]` |
| `005ad0fed000-005ad0fef000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0fef000-005ad0ff6000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30045]` |
| `005ad0ff6000-005ad0ff8000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad0ff8000-005ad0fff000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30046]` |
| `005ad0fff000-005ad1000000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1032000-005ad1034000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1034000-005ad103b000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30047]` |
| `005ad103f000-005ad1040000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1040000-005ad1044000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmmi_rust_key_config.z.so` |
| `005ad1044000-005ad104c000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmmi_rust_key_config.z.so` |
| `005ad104c000-005ad104d000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmmi_rust_key_config.z.so` |
| `005ad104d000-005ad104e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmmi_rust_key_config.z.so` |
| `005ad104e000-005ad104f000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libmmi_rust_key_config.z.so.bss]` |
| `005ad104f000-005ad1051000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1051000-005ad1058000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30048]` |
| `005ad1058000-005ad105a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad105a000-005ad1061000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30049]` |
| `005ad1061000-005ad1063000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1063000-005ad106a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30050]` |
| `005ad106a000-005ad106c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad106c000-005ad1073000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30051]` |
| `005ad1073000-005ad1075000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1075000-005ad107c000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30052]` |
| `005ad107c000-005ad1080000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad1080000-005ad1082000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsocketpair.z.so` |
| `005ad1082000-005ad1085000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsocketpair.z.so` |
| `005ad1085000-005ad1086000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsocketpair.z.so` |
| `005ad1086000-005ad1087000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsocketpair.z.so` |
| `005ad1087000-005ad108f000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad108f000-005ad1091000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1091000-005ad1098000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30053]` |
| `005ad1098000-005ad109a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad109a000-005ad10a1000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30054]` |
| `005ad10a1000-005ad10aa000` | FilePage other | `rw-p` | 36 | 36 | 36 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/advertising/libadcomponent.z.so_21368_1]` |
| `005ad10aa000-005ad10ac000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad10ac000-005ad10b3000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30057]` |
| `005ad10b3000-005ad10b6000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad10b6000-005ad10b9000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad10b9000-005ad10bc000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad10bc000-005ad10be000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad10be000-005ad10bf000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad10bf000-005ad10c0000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad10c0000-005ad10dd000` | .so | `r--p` | 116 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libinputmethod_client.z.so` |
| `005ad10dd000-005ad1137000` | .so | `r-xp` | 360 | 108 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libinputmethod_client.z.so` |
| `005ad1137000-005ad1141000` | .so | `r--p` | 40 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libinputmethod_client.z.so` |
| `005ad1141000-005ad1142000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libinputmethod_client.z.so` |
| `005ad1142000-005ad1168000` | FilePage other | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/log/xlog/DYLog.mmap3` |
| `005ad1168000-005ad116a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad116a000-005ad1171000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30058]` |
| `005ad1171000-005ad1173000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1173000-005ad117a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30059]` |
| `005ad117a000-005ad1180000` | FilePage other | `r--s` | 24 | 16 | 1 | 0 | 0 | 0.00% | `/system/etc/icu_tzdata/timezoneTypes.res` |
| `005ad1180000-005ad1205000` | .so | `r--p` | 532 | 152 | 17 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilitykit_native.z.so` |
| `005ad1205000-005ad12ae000` | .so | `r-xp` | 676 | 380 | 29 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilitykit_native.z.so` |
| `005ad12ae000-005ad12be000` | .so | `r--p` | 64 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilitykit_native.z.so` |
| `005ad12be000-005ad12bf000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilitykit_native.z.so` |
| `005ad12bf000-005ad12c1000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libabilitykit_native.z.so.bss]` |
| `005ad12c1000-005ad12c9000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad12c9000-005ad12cb000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad12cb000-005ad12d2000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30060]` |
| `005ad12d2000-005ad12d4000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad12d4000-005ad12db000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30061]` |
| `005ad12db000-005ad12dd000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad12dd000-005ad12e4000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30062]` |
| `005ad12e4000-005ad12f1000` | FilePage other | `rw-s` | 52 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/imsdk_config_1400029396` |
| `005ad12f1000-005ad12f3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad12f3000-005ad12fa000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30063]` |
| `005ad12fa000-005ad1300000` | native heap | `rw-p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad1300000-005ad1306000` | .so | `r--p` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilitykit_utils.z.so` |
| `005ad1306000-005ad130a000` | .so | `r-xp` | 16 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilitykit_utils.z.so` |
| `005ad130a000-005ad130c000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilitykit_utils.z.so` |
| `005ad130c000-005ad130d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilitykit_utils.z.so` |
| `005ad130d000-005ad1333000` | FilePage other | `rw-s` | 152 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/imsdk_C.mmap2` |
| `005ad1333000-005ad1336000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1336000-005ad1339000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1339000-005ad133a000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad133a000-005ad133d000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad133d000-005ad133e000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad133e000-005ad133f000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad133f000-005ad1340000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1340000-005ad1359000` | .so | `r--p` | 100 | 72 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libresmgr_napi_core.z.so` |
| `005ad1359000-005ad1380000` | .so | `r-xp` | 156 | 156 | 11 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libresmgr_napi_core.z.so` |
| `005ad1380000-005ad1384000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libresmgr_napi_core.z.so` |
| `005ad1384000-005ad1386000` | .so | `rw-p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libresmgr_napi_core.z.so` |
| `005ad1386000-005ad1388000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1388000-005ad138b000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad138b000-005ad138e000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad138f000-005ad13b4000` | FilePage other | `r--s` | 148 | 36 | 5 | 0 | 0 | 0.00% | `/system/etc/icu_tzdata/zoneinfo64.res` |
| `005ad13b4000-005ad13b5000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad13b5000-005ad13b9000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad13b9000-005ad13ba000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad13ba000-005ad13bd000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad13bd000-005ad13c0000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad13c0000-005ad13ca000` | .so | `r--p` | 40 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_hdi_impl_v1_4.z.so` |
| `005ad13d7000-005ad13d8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_hdi_impl_v1_4.z.so` |
| `005ad13d8000-005ad13da000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad13da000-005ad13e1000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30065]` |
| `005ad13e1000-005ad13e3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad13e3000-005ad13ea000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30067]` |
| `005ad13ea000-005ad13ec000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad13ec000-005ad13f3000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30068]` |
| `005ad13f3000-005ad13f6000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad13f6000-005ad13f8000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad13f8000-005ad13fb000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1400000-005ad1409000` | .so | `r--p` | 36 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbeget_proxy.z.so` |
| `005ad1409000-005ad1419000` | .so | `r-xp` | 64 | 64 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbeget_proxy.z.so` |
| `005ad1419000-005ad1420000` | .so | `r--p` | 28 | 28 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbeget_proxy.z.so` |
| `005ad1420000-005ad1421000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbeget_proxy.z.so` |
| `005ad1421000-005ad1429000` | native heap | `rw-p` | 32 | 28 | 28 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad1429000-005ad142b000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad142b000-005ad1432000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30072]` |
| `005ad1432000-005ad1434000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1434000-005ad143b000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30073]` |
| `005ad143b000-005ad143d000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad143d000-005ad143e000` | dev | `r--s` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:sys_param:s0` |
| `005ad143e000-005ad1440000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad1440000-005ad1442000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_info.z.so` |
| `005ad1442000-005ad1444000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_info.z.so` |
| `005ad1444000-005ad1445000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_info.z.so` |
| `005ad1445000-005ad1446000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_info.z.so` |
| `005ad1446000-005ad1448000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1448000-005ad144f000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30074]` |
| `005ad1451000-005ad1452000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1452000-005ad1453000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1453000-005ad1454000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1454000-005ad1455000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1455000-005ad1456000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1456000-005ad1457000` | native heap | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad1457000-005ad1472000` | FilePage other | `rw-p` | 108 | 108 | 108 | 0 | 0 | 0.00% | `[anon:ArkTS Code:396481104256]` |
| `005ad1472000-005ad147a000` | GL | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el2/database/rdb/Bugly_database.db-shm` |
| `005ad147a000-005ad147b000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad147b000-005ad147c000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad147c000-005ad147d000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad147d000-005ad147e000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad147e000-005ad147f000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad147f000-005ad1480000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1480000-005ad14cf000` | .so | `r--p` | 316 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/libFillpSo.z.so` |
| `005ad14cf000-005ad1574000` | .so | `r-xp` | 660 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libFillpSo.z.so` |
| `005ad1574000-005ad1578000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libFillpSo.z.so` |
| `005ad1578000-005ad1579000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libFillpSo.z.so` |
| `005ad1579000-005ad157a000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libFillpSo.z.so.bss]` |
| `005ad157a000-005ad157b000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad157b000-005ad157c000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad157c000-005ad157d000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad157d000-005ad157e000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad157e000-005ad157f000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad157f000-005ad1580000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1580000-005ad159c000` | .so | `r--p` | 112 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libheifparser.z.so` |
| `005ad159c000-005ad15d4000` | .so | `r-xp` | 224 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libheifparser.z.so` |
| `005ad15d4000-005ad15d9000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libheifparser.z.so` |
| `005ad15d9000-005ad15da000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libheifparser.z.so` |
| `005ad15da000-005ad15de000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libheifparser.z.so.bss]` |
| `005ad15e7000-005ad15ea000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad15ea000-005ad15ec000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad15ec000-005ad15ee000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad15f0000-005ad15f2000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad15f2000-005ad15f9000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30092]` |
| `005ad15f9000-005ad15fc000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad15fc000-005ad15fd000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad15fd000-005ad15fe000` | dev | `rw-s` | 4 | 4 | 4 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad15fe000-005ad1600000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1600000-005ad1604000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.1.z.so` |
| `005ad1604000-005ad1609000` | .so | `r-xp` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.1.z.so` |
| `005ad1609000-005ad160b000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.1.z.so` |
| `005ad160b000-005ad160c000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.1.z.so` |
| `005ad160c000-005ad160e000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad160e000-005ad1611000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1613000-005ad161a000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad161a000-005ad161d000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad161d000-005ad1620000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1620000-005ad1623000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1626000-005ad162a000` | dev | `rw-s` | 16 | 16 | 16 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad162a000-005ad162c000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad162c000-005ad162f000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad162f000-005ad1632000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1632000-005ad1636000` | FilePage other | `r--s` | 16 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/heavy_ad_intervention_opt_out.db` |
| `005ad163a000-005ad163d000` | dev | `rw-s` | 12 | 12 | 12 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad163d000-005ad163e000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad163e000-005ad163f000` | dev | `rw-s` | 4 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad163f000-005ad1640000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1640000-005ad1654000` | .so | `r--p` | 80 | 36 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibilityconfig.z.so` |
| `005ad1654000-005ad166c000` | .so | `r-xp` | 96 | 52 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibilityconfig.z.so` |
| `005ad166c000-005ad1673000` | .so | `r--p` | 28 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibilityconfig.z.so` |
| `005ad1673000-005ad1674000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibilityconfig.z.so` |
| `005ad1674000-005ad1676000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1676000-005ad167d000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30093]` |
| `005ad167d000-005ad167f000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1680000-005ad169e000` | .so | `r--p` | 120 | 108 | 11 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbgtaskmgr_innerkits.z.so` |
| `005ad169e000-005ad16c3000` | .so | `r-xp` | 148 | 148 | 9 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbgtaskmgr_innerkits.z.so` |
| `005ad16c3000-005ad16cb000` | .so | `r--p` | 32 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbgtaskmgr_innerkits.z.so` |
| `005ad16cb000-005ad16cc000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbgtaskmgr_innerkits.z.so` |
| `005ad16cc000-005ad16f2000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad16f2000-005ad16f9000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad16fa000-005ad16ff000` | dev | `rw-s` | 20 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/RSSurfaceCapture Data` |
| `005ad1700000-005ad1702000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libjit_code_sign.z.so` |
| `005ad1702000-005ad1706000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libjit_code_sign.z.so` |
| `005ad1706000-005ad1707000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libjit_code_sign.z.so` |
| `005ad1707000-005ad1708000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libjit_code_sign.z.so` |
| `005ad1708000-005ad170a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad170a000-005ad1711000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30094]` |
| `005ad1711000-005ad1719000` | FilePage other | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/1400029396_385041624552325258644f31/im.db-shm` |
| `005ad1719000-005ad1721000` | native heap | `rw-p` | 32 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad1721000-005ad1723000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1723000-005ad172a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30234]` |
| `005ad1733000-005ad173b000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad173e000-005ad1740000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1740000-005ad174b000` | .so | `r--p` | 44 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libapp_domain_verify_mgr_client.z.so` |
| `005ad174b000-005ad175f000` | .so | `r-xp` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapp_domain_verify_mgr_client.z.so` |
| `005ad175f000-005ad1761000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapp_domain_verify_mgr_client.z.so` |
| `005ad1761000-005ad1762000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapp_domain_verify_mgr_client.z.so` |
| `005ad1762000-005ad176a000` | FilePage other | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/1400029396_385041624552325258644f31/msg_0.db-shm` |
| `005ad176a000-005ad176c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad176c000-005ad1773000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30111]` |
| `005ad1773000-005ad177b000` | FilePage other | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el2/database/entry/rdb/RKStorage.db-shm` |
| `005ad177f000-005ad1780000` | AnonPage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1780000-005ad17c4000` | .so | `r--p` | 272 | 44 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicemanagersdk.z.so` |
| `005ad17c4000-005ad1843000` | .so | `r-xp` | 508 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicemanagersdk.z.so` |
| `005ad1843000-005ad184b000` | .so | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicemanagersdk.z.so` |
| `005ad184b000-005ad184c000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicemanagersdk.z.so` |
| `005ad184c000-005ad184d000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdevicemanagersdk.z.so.bss]` |
| `005ad184d000-005ad1875000` | dev | `rw-s` | 160 | 160 | 160 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1875000-005ad1877000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1877000-005ad187e000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30119]` |
| `005ad187e000-005ad1880000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1880000-005ad18ce000` | .so | `r--p` | 312 | 196 | 19 | 0 | 0 | 0.00% | `/system/lib64/libvideoprocessingengine.z.so` |
| `005ad18ce000-005ad196b000` | .so | `r-xp` | 628 | 268 | 27 | 0 | 0 | 0.00% | `/system/lib64/libvideoprocessingengine.z.so` |
| `005ad196b000-005ad1978000` | .so | `r--p` | 52 | 32 | 4 | 0 | 0 | 0.00% | `/system/lib64/libvideoprocessingengine.z.so` |
| `005ad1978000-005ad1979000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvideoprocessingengine.z.so` |
| `005ad1979000-005ad1981000` | FilePage other | `rw-p` | 32 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libvideoprocessingengine.z.so.bss]` |
| `005ad1981000-005ad19a7000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad19a7000-005ad19ae000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad19af000-005ad19bd000` | FilePage other | `rw-p` | 56 | 56 | 56 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/lib64/module/multimedia/libavcastpicker.z.so_21352_1]` |
| `005ad19c0000-005ad19c7000` | .so | `r--p` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_time.z.so` |
| `005ad19c7000-005ad19cf000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_time.z.so` |
| `005ad19cf000-005ad19d1000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_time.z.so` |
| `005ad19d1000-005ad19d2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_time.z.so` |
| `005ad19d2000-005ad19d4000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad19d4000-005ad19db000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30235]` |
| `005ad19db000-005ad19dd000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad19dd000-005ad19e4000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30236]` |
| `005ad19e4000-005ad19e6000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad19e6000-005ad19ed000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30237]` |
| `005ad19ed000-005ad19ef000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad19ef000-005ad19f6000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30238]` |
| `005ad19f6000-005ad19f8000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad19f8000-005ad19ff000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30239]` |
| `005ad19ff000-005ad1a00000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1a00000-005ad1a7a000` | .so | `r--p` | 488 | 48 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_util.z.so` |
| `005ad1a7a000-005ad1b88000` | .so | `r-xp` | 1080 | 228 | 22 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_util.z.so` |
| `005ad1b88000-005ad1b8d000` | .so | `r--p` | 20 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_util.z.so` |
| `005ad1b8d000-005ad1b8e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_util.z.so` |
| `005ad1b8e000-005ad1b91000` | FilePage other | `rw-p` | 12 | 12 | 8 | 0 | 0 | 0.00% | `[anon:libintl_util.z.so.bss]` |
| `005ad1b91000-005ad1b93000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1b93000-005ad1b9a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30240]` |
| `005ad1b9a000-005ad1b9c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1b9c000-005ad1ba3000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30241]` |
| `005ad1ba3000-005ad1ba5000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1ba5000-005ad1bac000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30242]` |
| `005ad1bac000-005ad1bb3000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1bb3000-005ad1bb5000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1bb5000-005ad1bb7000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1bb7000-005ad1bbe000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30244]` |
| `005ad1bbe000-005ad1bc0000` | FilePage other | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/ShaderCache/data_2` |
| `005ad1bc0000-005ad1bc1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_error_convert.z.so` |
| `005ad1bc1000-005ad1bc4000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_error_convert.z.so` |
| `005ad1bc4000-005ad1bc5000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_error_convert.z.so` |
| `005ad1bc5000-005ad1bc6000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_error_convert.z.so` |
| `005ad1bc6000-005ad1bff000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1bff000-005ad1c00000` | dev | `rw-s` | 4 | 0 | 0 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/gralloc_shared_attr` |
| `005ad1c99000-005ad1c9a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libruntime.z.so` |
| `005ad1c9b000-005ad1c9d000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1c9d000-005ad1ca4000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30245]` |
| `005ad1ca4000-005ad1ca6000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1ca6000-005ad1cad000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30256]` |
| `005ad1cad000-005ad1caf000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1caf000-005ad1cb6000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30277]` |
| `005ad1cc0000-005ad1d5c000` | .so | `r--p` | 624 | 256 | 29 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscene_session.z.so` |
| `005ad1d5c000-005ad1eeb000` | .so | `r-xp` | 1596 | 1016 | 181 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscene_session.z.so` |
| `005ad1eeb000-005ad1f26000` | .so | `r--p` | 236 | 104 | 13 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscene_session.z.so` |
| `005ad1f26000-005ad1f27000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscene_session.z.so` |
| `005ad1f27000-005ad1f29000` | FilePage other | `rw-p` | 8 | 8 | 4 | 0 | 0 | 0.00% | `[anon:libscene_session.z.so.bss]` |
| `005ad1f29000-005ad1f31000` | native heap | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad1f31000-005ad1f33000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad1f33000-005ad1f3a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30346]` |
| `005ad1f3a000-005ad1f3e000` | dev | `rw-s` | 16 | 16 | 16 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1f3e000-005ad1f40000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1f7b000-005ad1f7d000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad1f7e000-005ad1f80000` | FilePage other | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/ShaderCache/data_3` |
| `005ad1f80000-005ad210f000` | .so | `r--p` | 1596 | 112 | 16 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilityms.z.so` |
| `005ad210f000-005ad252c000` | .so | `r-xp` | 4212 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilityms.z.so` |
| `005ad252c000-005ad2555000` | .so | `r--p` | 164 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilityms.z.so` |
| `005ad2555000-005ad2556000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabilityms.z.so` |
| `005ad2556000-005ad255a000` | FilePage other | `rw-p` | 16 | 8 | 1 | 0 | 0 | 0.00% | `[anon:libabilityms.z.so.bss]` |
| `005ad255a000-005ad255c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad255c000-005ad2563000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30274]` |
| `005ad2563000-005ad2565000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2565000-005ad256c000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30275]` |
| `005ad256c000-005ad256e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad256e000-005ad2575000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30347]` |
| `005ad2575000-005ad2577000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2577000-005ad257e000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30348]` |
| `005ad257e000-005ad2580000` | FilePage other | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GrShaderCache/data_0` |
| `005ad2580000-005ad258a000` | .so | `r--p` | 40 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_dataability.z.so` |
| `005ad258a000-005ad2594000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_dataability.z.so` |
| `005ad2594000-005ad2597000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_dataability.z.so` |
| `005ad2597000-005ad2598000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_dataability.z.so` |
| `005ad2598000-005ad2599000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnative_dataability.z.so.bss]` |
| `005ad2599000-005ad259b000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad259b000-005ad25a2000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30349]` |
| `005ad25a2000-005ad25a4000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad25a4000-005ad25ab000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30355]` |
| `005ad25b7000-005ad25b9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad25b9000-005ad25c0000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30278]` |
| `005ad25c0000-005ad25c2000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpage_config_manager.z.so` |
| `005ad25c2000-005ad25c5000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpage_config_manager.z.so` |
| `005ad25c5000-005ad25c6000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpage_config_manager.z.so` |
| `005ad25c6000-005ad25c7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpage_config_manager.z.so` |
| `005ad25c7000-005ad2600000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad26c2000-005ad26c3000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_foundation.z.so` |
| `005ad26c3000-005ad26c4000` | FilePage other | `rw-p` | 4 | 4 | 2 | 0 | 0 | 0.00% | `[anon:libmedia_foundation.z.so.bss]` |
| `005ad26c4000-005ad26fd000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad26fd000-005ad26ff000` | FilePage other | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GrShaderCache/data_1` |
| `005ad2700000-005ad278f000` | .so | `r--p` | 572 | 204 | 15 | 0 | 0 | 0.00% | `/system/lib64/libstd.dylib.so` |
| `005ad278f000-005ad281e000` | .so | `r-xp` | 572 | 192 | 20 | 0 | 0 | 0.00% | `/system/lib64/libstd.dylib.so` |
| `005ad281e000-005ad2827000` | .so | `r--p` | 36 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libstd.dylib.so` |
| `005ad2827000-005ad2828000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libstd.dylib.so` |
| `005ad2828000-005ad2829000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libstd.dylib.so.bss]` |
| `005ad2832000-005ad2839000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2839000-005ad2840000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2840000-005ad2887000` | .so | `r--p` | 284 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_dfile.z.so` |
| `005ad2887000-005ad291c000` | .so | `r-xp` | 596 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_dfile.z.so` |
| `005ad291c000-005ad2920000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_dfile.z.so` |
| `005ad2920000-005ad2921000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_dfile.z.so` |
| `005ad2921000-005ad2922000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnstackx_dfile.z.so.bss]` |
| `005ad2922000-005ad292a000` | dev | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad292a000-005ad2932000` | dev | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2932000-005ad2936000` | dev | `rw-s` | 16 | 16 | 16 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2939000-005ad2940000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2940000-005ad295d000` | .so | `r--p` | 116 | 44 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_utils.z.so` |
| `005ad295d000-005ad2991000` | .so | `r-xp` | 208 | 112 | 11 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_utils.z.so` |
| `005ad2991000-005ad2994000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_utils.z.so` |
| `005ad2994000-005ad2995000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_utils.z.so` |
| `005ad2995000-005ad2997000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2997000-005ad299e000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30322]` |
| `005ad299e000-005ad29a0000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad29a0000-005ad29a7000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30323]` |
| `005ad29a7000-005ad29a9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad29a9000-005ad29b0000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30324]` |
| `005ad29b0000-005ad29b2000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad29b2000-005ad29b9000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30325]` |
| `005ad29b9000-005ad29bd000` | native heap | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad29bd000-005ad29bf000` | FilePage other | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GrShaderCache/data_2` |
| `005ad29c0000-005ad29c2000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_runtime_error_util.z.so` |
| `005ad29c2000-005ad29c5000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_runtime_error_util.z.so` |
| `005ad29c5000-005ad29c6000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_runtime_error_util.z.so` |
| `005ad29c6000-005ad29c7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_runtime_error_util.z.so` |
| `005ad29c7000-005ad29c8000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libability_runtime_error_util.z.so.bss]` |
| `005ad29c8000-005ad29d0000` | native heap | `rw-p` | 32 | 28 | 28 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad29d0000-005ad29d2000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad29d2000-005ad29d9000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30359]` |
| `005ad29d9000-005ad29e1000` | FilePage other | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `[anon:tls-mmap-allocator]` |
| `005ad29e1000-005ad29e3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad29e3000-005ad29ea000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30360]` |
| `005ad29ea000-005ad29ec000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad29ec000-005ad29f3000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30361]` |
| `005ad29f3000-005ad29f5000` | FilePage other | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GrShaderCache/data_3` |
| `005ad29f8000-005ad29fa000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad29fb000-005ad29fd000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad29fe000-005ad2a00000` | Graph | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GraphiteDawnCache/data_0` |
| `005ad2a00000-005ad2a03000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhichecker.so` |
| `005ad2a03000-005ad2a06000` | .so | `r-xp` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhichecker.so` |
| `005ad2a06000-005ad2a07000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhichecker.so` |
| `005ad2a07000-005ad2a08000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhichecker.so` |
| `005ad2a08000-005ad2a37000` | FilePage other | `r--p` | 188 | 188 | 188 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNRoomHelperNew-harmony_6083e51/dyrnroomhelpernew.bundle` |
| `005ad2a37000-005ad2a39000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2a39000-005ad2a40000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30362]` |
| `005ad2a40000-005ad2a43000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprivacy_communication_adapter_cxx.z.so` |
| `005ad2a43000-005ad2a4a000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprivacy_communication_adapter_cxx.z.so` |
| `005ad2a4a000-005ad2a4d000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprivacy_communication_adapter_cxx.z.so` |
| `005ad2a4d000-005ad2a4e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprivacy_communication_adapter_cxx.z.so` |
| `005ad2a4e000-005ad2a7e000` | FilePage other | `r--p` | 192 | 192 | 192 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNFansClubEntry-harmony_62bdeb1/dyrnfansclubentry.bundle` |
| `005ad2a7e000-005ad2a80000` | Graph | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GraphiteDawnCache/data_1` |
| `005ad2a80000-005ad2a81000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_raw_logging_internal.z.so` |
| `005ad2a81000-005ad2a83000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_raw_logging_internal.z.so` |
| `005ad2a83000-005ad2a84000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_raw_logging_internal.z.so` |
| `005ad2a84000-005ad2a85000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_raw_logging_internal.z.so` |
| `005ad2a85000-005ad2abe000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2abe000-005ad2ac0000` | Graph | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GraphiteDawnCache/data_2` |
| `005ad2ac0000-005ad2ac5000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.0.z.so` |
| `005ad2ac5000-005ad2acc000` | .so | `r-xp` | 28 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.0.z.so` |
| `005ad2acc000-005ad2ace000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.0.z.so` |
| `005ad2ace000-005ad2acf000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.0.z.so` |
| `005ad2acf000-005ad2ade000` | dev | `rw-s` | 60 | 60 | 60 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2ade000-005ad2ae3000` | FilePage other | `r--s` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/Safe Browsing Cookies` |
| `005ad2ae3000-005ad2ae5000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2ae5000-005ad2aec000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30279]` |
| `005ad2aec000-005ad2aee000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2aee000-005ad2af5000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30292]` |
| `005ad2af5000-005ad2af7000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2af7000-005ad2afe000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30293]` |
| `005ad2afe000-005ad2b00000` | Graph | `rw-s` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GraphiteDawnCache/data_3` |
| `005ad2b00000-005ad2b09000` | .so | `r--p` | 36 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeablemem_plugin.z.so` |
| `005ad2b09000-005ad2b17000` | .so | `r-xp` | 56 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/libpurgeablemem_plugin.z.so` |
| `005ad2b17000-005ad2b19000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeablemem_plugin.z.so` |
| `005ad2b19000-005ad2b1a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libpurgeablemem_plugin.z.so` |
| `005ad2b1a000-005ad2b1c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2b1c000-005ad2b23000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30299]` |
| `005ad2b23000-005ad2b25000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2b25000-005ad2b2c000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30326]` |
| `005ad2b2c000-005ad2b3b000` | dev | `rw-s` | 60 | 60 | 60 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2b3b000-005ad2b40000` | FilePage other | `r--s` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/Cookies` |
| `005ad2b40000-005ad2b67000` | .so | `r--p` | 156 | 76 | 17 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreen_session_manager_client.z.so` |
| `005ad2b67000-005ad2bb9000` | .so | `r-xp` | 328 | 264 | 78 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreen_session_manager_client.z.so` |
| `005ad2bb9000-005ad2bc0000` | .so | `r--p` | 28 | 24 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreen_session_manager_client.z.so` |
| `005ad2bc0000-005ad2bc1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreen_session_manager_client.z.so` |
| `005ad2bc1000-005ad2bc2000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libscreen_session_manager_client.z.so.bss]` |
| `005ad2bc2000-005ad2bfb000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2bfb000-005ad2bff000` | FilePage other | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `[anon:ArkTS Code:/system/etc/abc/arkui/components/arktextclock.abc]` |
| `005ad2c00000-005ad2c02000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtoken_callback_sdk.z.so` |
| `005ad2c02000-005ad2c06000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtoken_callback_sdk.z.so` |
| `005ad2c06000-005ad2c07000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtoken_callback_sdk.z.so` |
| `005ad2c07000-005ad2c08000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtoken_callback_sdk.z.so` |
| `005ad2c08000-005ad2c38000` | dev | `rw-s` | 192 | 192 | 192 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2c38000-005ad2c40000` | dev | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/shared_memory/763802950799AF4AD84500A4483825D0` |
| `005ad2c40000-005ad2c44000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiappevent_innerapi.z.so` |
| `005ad2c44000-005ad2c48000` | .so | `r-xp` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiappevent_innerapi.z.so` |
| `005ad2c48000-005ad2c4a000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiappevent_innerapi.z.so` |
| `005ad2c4a000-005ad2c4b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiappevent_innerapi.z.so` |
| `005ad2c4b000-005ad2c7f000` | FilePage other | `r--p` | 208 | 208 | 208 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNDesertrelic-harmony_d46a82a/dyrndesertrelic.bundle` |
| `005ad2c80000-005ad2c87000` | .so | `r--p` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_time_zone.z.so` |
| `005ad2c87000-005ad2c97000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_time_zone.z.so` |
| `005ad2c97000-005ad2c98000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_time_zone.z.so` |
| `005ad2c98000-005ad2c99000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libabsl_time_zone.z.so` |
| `005ad2c99000-005ad2c9a000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libabsl_time_zone.z.so.bss]` |
| `005ad2c9a000-005ad2ca9000` | dev | `rw-s` | 60 | 60 | 60 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2ca9000-005ad2cab000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2cab000-005ad2cb2000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30363]` |
| `005ad2cb2000-005ad2cb4000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2cb4000-005ad2cbb000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30364]` |
| `005ad2cbb000-005ad2cbd000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2cbe000-005ad2cc0000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2cc0000-005ad2ccb000` | .so | `r--p` | 44 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconnection_obs_manager.z.so` |
| `005ad2ccb000-005ad2cd5000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconnection_obs_manager.z.so` |
| `005ad2cd5000-005ad2cd9000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconnection_obs_manager.z.so` |
| `005ad2cd9000-005ad2cda000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconnection_obs_manager.z.so` |
| `005ad2cda000-005ad2cdc000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2cdc000-005ad2ce3000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30365]` |
| `005ad2ce3000-005ad2ce5000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2ce5000-005ad2cec000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30367]` |
| `005ad2cec000-005ad2cee000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2cee000-005ad2cf5000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30366]` |
| `005ad2cf5000-005ad2cf7000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2cf7000-005ad2cfe000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30368]` |
| `005ad2cfe000-005ad2d00000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2d00000-005ad2d02000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapplication_image_observer_manager.z.so` |
| `005ad2d02000-005ad2d05000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapplication_image_observer_manager.z.so` |
| `005ad2d05000-005ad2d06000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapplication_image_observer_manager.z.so` |
| `005ad2d06000-005ad2d07000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapplication_image_observer_manager.z.so` |
| `005ad2d07000-005ad2d40000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2d40000-005ad2d89000` | .so | `r--p` | 292 | 88 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuiabilitykit_native.z.so` |
| `005ad2d89000-005ad2dce000` | .so | `r-xp` | 276 | 208 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuiabilitykit_native.z.so` |
| `005ad2dce000-005ad2dd4000` | .so | `r--p` | 24 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuiabilitykit_native.z.so` |
| `005ad2dd4000-005ad2dd5000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuiabilitykit_native.z.so` |
| `005ad2dd5000-005ad2dd6000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libuiabilitykit_native.z.so.bss]` |
| `005ad2dd6000-005ad2dd8000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2dd8000-005ad2ddf000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30369]` |
| `005ad2ddf000-005ad2de1000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2de1000-005ad2de8000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30370]` |
| `005ad2de8000-005ad2def000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad2df0000-005ad2dfc000` | native heap | `rw-p` | 48 | 12 | 12 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad2e00000-005ad2e06000` | .so | `r--p` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdi_base.z.so` |
| `005ad2e06000-005ad2e18000` | .so | `r-xp` | 72 | 60 | 3 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdi_base.z.so` |
| `005ad2e18000-005ad2e19000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdi_base.z.so` |
| `005ad2e19000-005ad2e1a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdi_base.z.so` |
| `005ad2e1a000-005ad2e1c000` | native heap | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:native_heap:brk]` |
| `005ad2e1c000-005ad2e1e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2e1e000-005ad2e25000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30371]` |
| `005ad2e25000-005ad2e27000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2e27000-005ad2e2e000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30372]` |
| `005ad2e2e000-005ad2e30000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2e30000-005ad2e37000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30373]` |
| `005ad2e37000-005ad2e39000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2e39000-005ad2e40000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30374]` |
| `005ad2e40000-005ad2e50000` | .so | `r--p` | 64 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcontinuation_ipc.z.so` |
| `005ad2e50000-005ad2e5b000` | .so | `r-xp` | 44 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcontinuation_ipc.z.so` |
| `005ad2e5b000-005ad2e63000` | .so | `r--p` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcontinuation_ipc.z.so` |
| `005ad2e63000-005ad2e64000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcontinuation_ipc.z.so` |
| `005ad2e64000-005ad2e65000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libcontinuation_ipc.z.so.bss]` |
| `005ad2e65000-005ad2e67000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2e67000-005ad2e6e000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30375]` |
| `005ad2e6e000-005ad2e70000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2e70000-005ad2e77000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30376]` |
| `005ad2e77000-005ad2e79000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2e79000-005ad2e80000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30377]` |
| `005ad2e80000-005ad2ea9000` | .so | `r--p` | 164 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libhukssdk.z.so` |
| `005ad2ea9000-005ad2ee7000` | .so | `r-xp` | 248 | 84 | 3 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libhukssdk.z.so` |
| `005ad2ee7000-005ad2eed000` | .so | `r--p` | 24 | 20 | 2 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libhukssdk.z.so` |
| `005ad2eed000-005ad2eee000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libhukssdk.z.so` |
| `005ad2eee000-005ad2ef0000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2ef0000-005ad2ef7000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30378]` |
| `005ad2ef7000-005ad2ef9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad2ef9000-005ad2f00000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30379]` |
| `005ad390a000-005ad393e000` | FilePage other | `r--p` | 208 | 208 | 208 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNSnowRisk-harmony_3ef4bf3/dyrnsnowrisk.bundle` |
| `005ad393e000-005ad3940000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad3940000-005ad3946000` | .so | `r--p` | 24 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextension_manager.z.so` |
| `005ad3946000-005ad394c000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextension_manager.z.so` |
| `005ad394c000-005ad394e000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextension_manager.z.so` |
| `005ad394e000-005ad394f000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextension_manager.z.so` |
| `005ad394f000-005ad396f000` | dev | `rw-s` | 128 | 128 | 128 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/shared_memory/066B43B276B64F62528A924B7EA9A8DF` |
| `005ad396f000-005ad3971000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad3971000-005ad3978000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30380]` |
| `005ad3978000-005ad397f000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad3980000-005ad3984000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_client_sync.z.so` |
| `005ad3984000-005ad3994000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_client_sync.z.so` |
| `005ad3994000-005ad3995000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_client_sync.z.so` |
| `005ad3995000-005ad3996000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_client_sync.z.so` |
| `005ad3996000-005ad39b3000` | FilePage other | `r--s` | 116 | 60 | 60 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/Web Data` |
| `005ad39b3000-005ad39b5000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad39b5000-005ad39bc000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30381]` |
| `005ad39c0000-005ad39d6000` | .so | `r--p` | 88 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libapp_util.z.so` |
| `005ad39d6000-005ad39f4000` | .so | `r-xp` | 120 | 44 | 1 | 0 | 0 | 0.00% | `/system/lib64/libapp_util.z.so` |
| `005ad39f4000-005ad39f6000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapp_util.z.so` |
| `005ad39f6000-005ad39f7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libapp_util.z.so` |
| `005ad39f7000-005ad39f9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad39f9000-005ad3a00000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30382]` |
| `005ad3a00000-005ad3a0d000` | .so | `r--p` | 52 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprivacy_sdk.z.so` |
| `005ad3a0d000-005ad3a2a000` | .so | `r-xp` | 116 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprivacy_sdk.z.so` |
| `005ad3a2a000-005ad3a31000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprivacy_sdk.z.so` |
| `005ad3a31000-005ad3a32000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprivacy_sdk.z.so` |
| `005ad3a32000-005ad3a33000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libprivacy_sdk.z.so.bss]` |
| `005ad3a33000-005ad3a35000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad3a35000-005ad3a3c000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30383]` |
| `005ad3a40000-005ad3a43000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhiprofiler_preload_client.z.so` |
| `005ad3a43000-005ad3a4a000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhiprofiler_preload_client.z.so` |
| `005ad3a4a000-005ad3a4b000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhiprofiler_preload_client.z.so` |
| `005ad3a4b000-005ad3a4c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhiprofiler_preload_client.z.so` |
| `005ad3a4c000-005ad3a4e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad3a4e000-005ad3a55000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30384]` |
| `005ad3a55000-005ad3a60000` | FilePage other | `r--s` | 44 | 44 | 44 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/Shared Dictionary/db` |
| `005ad3a60000-005ad3a62000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad3a62000-005ad3a69000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30386]` |
| `005ad3a69000-005ad3a6b000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad3a6b000-005ad3a72000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30387]` |
| `005ad3a72000-005ad3a74000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad3a74000-005ad3a7b000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30388]` |
| `005ad3a7b000-005ad3a7d000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad3a80000-005ad3a83000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_uicontent.z.so` |
| `005ad3a83000-005ad3a86000` | .so | `r-xp` | 12 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_uicontent.z.so` |
| `005ad3a86000-005ad3a87000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_uicontent.z.so` |
| `005ad3a87000-005ad3a88000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_uicontent.z.so` |
| `005ad3a88000-005ad3abf000` | FilePage other | `r--p` | 220 | 220 | 220 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNAnchorPocketSys-harmony_ecc7669/dyrnanchorpocketsys.bundle` |
| `005ad3ac0000-005ad4968000` | .so | `r--p` | 15008 | 540 | 45 | 0 | 0 | 0.00% | `/system/lib64/libskia_canvaskit.z.so` |
| `005ad4968000-005ad5714000` | .so | `r-xp` | 14000 | 2624 | 485 | 0 | 0 | 0.00% | `/system/lib64/libskia_canvaskit.z.so` |
| `005ad5714000-005ad576c000` | .so | `r--p` | 352 | 136 | 7 | 0 | 0 | 0.00% | `/system/lib64/libskia_canvaskit.z.so` |
| `005ad576c000-005ad5770000` | .so | `rw-p` | 16 | 16 | 12 | 0 | 0 | 0.00% | `/system/lib64/libskia_canvaskit.z.so` |
| `005ad5770000-005ad5779000` | FilePage other | `rw-p` | 36 | 20 | 20 | 0 | 0 | 0.00% | `[anon:libskia_canvaskit.z.so.bss]` |
| `005ad5779000-005ad5780000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5780000-005ad5783000` | GL | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkweb_glue_base.z.so` |
| `005ad578a000-005ad578b000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkweb_glue_base.z.so.bss]` |
| `005ad578b000-005ad57c0000` | FilePage other | `r--p` | 212 | 212 | 212 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNFishballTreasure-harmony_c5e100f/dyrnfishballtreasure.bundle` |
| `005ad57c0000-005ad57e8000` | .so | `r--p` | 160 | 48 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwmutil.z.so` |
| `005ad57e8000-005ad5827000` | .so | `r-xp` | 252 | 104 | 7 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwmutil.z.so` |
| `005ad5827000-005ad582b000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwmutil.z.so` |
| `005ad582b000-005ad582c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwmutil.z.so` |
| `005ad582c000-005ad582d000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libwmutil.z.so.bss]` |
| `005ad582d000-005ad583a000` | FilePage other | `r--s` | 52 | 48 | 48 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/Affiliation Database` |
| `005ad583e000-005ad5840000` | dev | `rw-s` | 8 | 8 | 8 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5840000-005ad5859000` | .so | `r--p` | 100 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreen_session.z.so` |
| `005ad5859000-005ad5884000` | .so | `r-xp` | 172 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreen_session.z.so` |
| `005ad5884000-005ad5887000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreen_session.z.so` |
| `005ad5887000-005ad5888000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreen_session.z.so` |
| `005ad5888000-005ad5892000` | FilePage other | `r--s` | 40 | 36 | 36 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/Login Data` |
| `005ad5892000-005ad589c000` | FilePage other | `r--s` | 40 | 36 | 36 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/Login Data For Account` |
| `005ad589c000-005ad589e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad589e000-005ad58a5000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30390]` |
| `005ad58a5000-005ad58a7000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad58a7000-005ad58ae000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30389]` |
| `005ad58ae000-005ad58b0000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad58b0000-005ad58b7000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30391]` |
| `005ad58b7000-005ad58b9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad58b9000-005ad58c0000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30392]` |
| `005ad58c0000-005ad58c3000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_business_error.z.so` |
| `005ad58c3000-005ad58c4000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_business_error.z.so` |
| `005ad58c4000-005ad58c6000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_business_error.z.so` |
| `005ad58c6000-005ad58c7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_business_error.z.so` |
| `005ad58c7000-005ad5900000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5900000-005ad5921000` | .so | `r--p` | 132 | 52 | 2 | 0 | 0 | 0.00% | `/system/lib64/libvsync.z.so` |
| `005ad5921000-005ad594c000` | .so | `r-xp` | 172 | 64 | 3 | 0 | 0 | 0.00% | `/system/lib64/libvsync.z.so` |
| `005ad594c000-005ad5952000` | .so | `r--p` | 24 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvsync.z.so` |
| `005ad5952000-005ad5953000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libvsync.z.so` |
| `005ad5953000-005ad5954000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libvsync.z.so.bss]` |
| `005ad5954000-005ad5974000` | dev | `rw-s` | 128 | 128 | 118 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/shared_memory/8D433A9A98811E9AA19D8A02B5A48284` |
| `005ad5974000-005ad5976000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5976000-005ad597d000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30393]` |
| `005ad5980000-005ad59c5000` | .so | `r--p` | 276 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libui_extension.z.so` |
| `005ad59c5000-005ad5a00000` | .so | `r-xp` | 236 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_extension.z.so` |
| `005ad5a00000-005ad5a06000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_extension.z.so` |
| `005ad5a06000-005ad5a07000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_extension.z.so` |
| `005ad5a07000-005ad5a08000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libui_extension.z.so.bss]` |
| `005ad5a08000-005ad5a0a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a0a000-005ad5a11000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30422]` |
| `005ad5a11000-005ad5a13000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a13000-005ad5a1a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30423]` |
| `005ad5a1a000-005ad5a1c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a1c000-005ad5a23000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30424]` |
| `005ad5a23000-005ad5a25000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a25000-005ad5a2c000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30421]` |
| `005ad5a2c000-005ad5a2e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a2e000-005ad5a35000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30487]` |
| `005ad5a35000-005ad5a37000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a37000-005ad5a3e000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30491]` |
| `005ad5a40000-005ad5a48000` | .so | `r--p` | 32 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwantagent_manager.z.so` |
| `005ad5a48000-005ad5a51000` | .so | `r-xp` | 36 | 36 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwantagent_manager.z.so` |
| `005ad5a51000-005ad5a55000` | .so | `r--p` | 16 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwantagent_manager.z.so` |
| `005ad5a55000-005ad5a56000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwantagent_manager.z.so` |
| `005ad5a56000-005ad5a58000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a58000-005ad5a5f000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30492]` |
| `005ad5a5f000-005ad5a61000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a61000-005ad5a68000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30493]` |
| `005ad5a68000-005ad5a6a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a6a000-005ad5a71000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30494]` |
| `005ad5a71000-005ad5a73000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a73000-005ad5a7a000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30495]` |
| `005ad5a80000-005ad5a83000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_appdatafwk.z.so` |
| `005ad5a83000-005ad5a88000` | .so | `r-xp` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_appdatafwk.z.so` |
| `005ad5a88000-005ad5a89000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_appdatafwk.z.so` |
| `005ad5a89000-005ad5a8a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_appdatafwk.z.so` |
| `005ad5a8a000-005ad5a8c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a8c000-005ad5a93000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30496]` |
| `005ad5a93000-005ad5a95000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5a95000-005ad5a9c000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:30500]` |
| `005ad5aa3000-005ad5aaa000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5aae000-005ad5ab0000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5ab0000-005ad5ab7000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:31122]` |
| `005ad5ab7000-005ad5abe000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5ac0000-005ad5aca000` | .so | `r--p` | 40 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtime_client.z.so` |
| `005ad5aca000-005ad5add000` | .so | `r-xp` | 76 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtime_client.z.so` |
| `005ad5add000-005ad5ae1000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtime_client.z.so` |
| `005ad5ae1000-005ad5ae2000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtime_client.z.so` |
| `005ad5ae2000-005ad5af7000` | dev | `rw-s` | 84 | 84 | 84 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5af7000-005ad5aff000` | dev | `rw-s` | 32 | 32 | 32 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5b00000-005ad5b1f000` | .so | `r--p` | 124 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_util.z.so` |
| `005ad5b1f000-005ad5b53000` | .so | `r-xp` | 208 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_util.z.so` |
| `005ad5b53000-005ad5b56000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_util.z.so` |
| `005ad5b56000-005ad5b57000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_util.z.so` |
| `005ad5b57000-005ad5b5e000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5b5e000-005ad5b60000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5b60000-005ad5b67000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:31123]` |
| `005ad5b80000-005ad5b87000` | .so | `r--p` | 28 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreenlock_client.z.so` |
| `005ad5b87000-005ad5b95000` | .so | `r-xp` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreenlock_client.z.so` |
| `005ad5b95000-005ad5b99000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreenlock_client.z.so` |
| `005ad5b99000-005ad5b9a000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscreenlock_client.z.so` |
| `005ad5ba9000-005ad5bb0000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5bb4000-005ad5bbb000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5bc0000-005ad5c24000` | .so | `r--p` | 400 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libphonenumber_standard.z.so` |
| `005ad5c24000-005ad5c55000` | .so | `r-xp` | 196 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libphonenumber_standard.z.so` |
| `005ad5c55000-005ad5c58000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libphonenumber_standard.z.so` |
| `005ad5c58000-005ad5c5a000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libphonenumber_standard.z.so` |
| `005ad5c62000-005ad5c64000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005ad5c64000-005ad5c6b000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:signal_stack:31124]` |
| `005ad5c6b000-005ad5c72000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5c80000-005ad5c90000` | .so | `r--p` | 64 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liburi_permission_mgr.z.so` |
| `005ad5c90000-005ad5ca6000` | .so | `r-xp` | 88 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liburi_permission_mgr.z.so` |
| `005ad5ca6000-005ad5cab000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liburi_permission_mgr.z.so` |
| `005ad5cab000-005ad5cac000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liburi_permission_mgr.z.so` |
| `005ad5cac000-005ad5cad000` | FilePage other | `rw-p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `[anon:liburi_permission_mgr.z.so.bss]` |
| `005ad5cb7000-005ad5cbe000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5cc0000-005ad5cd3000` | .so | `r--p` | 76 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_adapter.z.so` |
| `005ad5cd3000-005ad5cf3000` | .so | `r-xp` | 128 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_adapter.z.so` |
| `005ad5cf3000-005ad5cf5000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_adapter.z.so` |
| `005ad5cf5000-005ad5cf6000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_adapter.z.so` |
| `005ad5d00000-005ad5d01000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlp_setconfig_sdk.z.so` |
| `005ad5d01000-005ad5d04000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlp_setconfig_sdk.z.so` |
| `005ad5d04000-005ad5d05000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlp_setconfig_sdk.z.so` |
| `005ad5d05000-005ad5d06000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlp_setconfig_sdk.z.so` |
| `005ad5d06000-005ad5d3f000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5d40000-005ad5dab000` | .so | `r--p` | 428 | 184 | 9 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_native.z.so` |
| `005ad5dab000-005ad5e90000` | .so | `r-xp` | 916 | 464 | 47 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_native.z.so` |
| `005ad5e90000-005ad5e9a000` | .so | `r--p` | 40 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_native.z.so` |
| `005ad5e9a000-005ad5e9b000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_native.z.so` |
| `005ad5e9b000-005ad5e9d000` | FilePage other | `rw-p` | 8 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libimage_native.z.so.bss]` |
| `005ad5e9d000-005ad5ea9000` | FilePage other | `r--s` | 48 | 44 | 44 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/segmentation_platform/ukm_db` |
| `005ad5ea9000-005ad5eb0000` | FilePage other | `r--s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/BrowsingTopicsSiteData` |
| `005ad5eb0000-005ad5ebc000` | FilePage other | `r--s` | 48 | 48 | 48 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/first_party_sets.db` |
| `005ad5ec0000-005ad5ecc000` | .so | `r--p` | 48 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsamgr_common.z.so` |
| `005ad5ecc000-005ad5eec000` | .so | `r-xp` | 128 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsamgr_common.z.so` |
| `005ad5eec000-005ad5eee000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsamgr_common.z.so` |
| `005ad5eee000-005ad5eef000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsamgr_common.z.so` |
| `005ad5eef000-005ad5efe000` | dev | `rw-s` | 60 | 60 | 60 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5f00000-005ad5f02000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapplication_context_manager.z.so` |
| `005ad5f02000-005ad5f04000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapplication_context_manager.z.so` |
| `005ad5f04000-005ad5f05000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libapplication_context_manager.z.so` |
| `005ad5f05000-005ad5f06000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libapplication_context_manager.z.so` |
| `005ad5f06000-005ad5f3f000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5f40000-005ad5f43000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_ui_intf.z.so` |
| `005ad5f57000-005ad5f5e000` | dev | `rw-s` | 28 | 28 | 28 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5f5e000-005ad5f73000` | dev | `rw-s` | 84 | 84 | 84 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5f80000-005ad5f87000` | .so | `r--p` | 28 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libconcurrent_task_client.z.so` |
| `005ad5f87000-005ad5f91000` | .so | `r-xp` | 40 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/libconcurrent_task_client.z.so` |
| `005ad5f91000-005ad5f93000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libconcurrent_task_client.z.so` |
| `005ad5f93000-005ad5f94000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libconcurrent_task_client.z.so` |
| `005ad5f94000-005ad5fba000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad5fc0000-005ad5fcc000` | GL | `r--p` | 48 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_render_info.z.so` |
| `005ad5fcc000-005ad5fe7000` | GL | `r-xp` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_render_info.z.so` |
| `005ad5fe7000-005ad5fe9000` | GL | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_render_info.z.so` |
| `005ad5fe9000-005ad5fea000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_render_info.z.so` |
| `005ad6000000-005ad60d3000` | .so | `r--p` | 844 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddb.z.so` |
| `005ad60d3000-005ad63b9000` | .so | `r-xp` | 2968 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddb.z.so` |
| `005ad63b9000-005ad63ce000` | .so | `r--p` | 84 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddb.z.so` |
| `005ad63ce000-005ad63cf000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddb.z.so` |
| `005ad63cf000-005ad63d2000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdistributeddb.z.so.bss]` |
| `005ad63d2000-005ad63f8000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6400000-005ad6415000` | .so | `r--p` | 84 | 64 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_common.z.so` |
| `005ad6415000-005ad6433000` | .so | `r-xp` | 120 | 88 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_common.z.so` |
| `005ad6433000-005ad6435000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_common.z.so` |
| `005ad6435000-005ad6436000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_common.z.so` |
| `005ad6436000-005ad6437000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnapi_common.z.so.bss]` |
| `005ad6440000-005ad6459000` | .so | `r--p` | 100 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_congestion.z.so` |
| `005ad6459000-005ad6483000` | .so | `r-xp` | 168 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_congestion.z.so` |
| `005ad6483000-005ad6485000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_congestion.z.so` |
| `005ad6485000-005ad6486000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnstackx_congestion.z.so` |
| `005ad6486000-005ad64bf000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad64c0000-005ad64d2000` | .so | `r--p` | 72 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstorage_manager_sa_proxy.z.so` |
| `005ad64d2000-005ad64fb000` | .so | `r-xp` | 164 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstorage_manager_sa_proxy.z.so` |
| `005ad64fb000-005ad6500000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstorage_manager_sa_proxy.z.so` |
| `005ad6500000-005ad6501000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstorage_manager_sa_proxy.z.so` |
| `005ad6501000-005ad653a000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6540000-005ad6547000` | .so | `r--p` | 28 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libxperfservice_client.z.so` |
| `005ad6547000-005ad654f000` | .so | `r-xp` | 32 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libxperfservice_client.z.so` |
| `005ad654f000-005ad6554000` | .so | `r--p` | 20 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libxperfservice_client.z.so` |
| `005ad6554000-005ad6555000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libxperfservice_client.z.so` |
| `005ad6555000-005ad657b000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6580000-005ad6582000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_start_setting.z.so` |
| `005ad6582000-005ad6585000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_start_setting.z.so` |
| `005ad6585000-005ad6587000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_start_setting.z.so` |
| `005ad6587000-005ad6588000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_start_setting.z.so` |
| `005ad6588000-005ad65ae000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6600000-005ad6681000` | .so | `r--p` | 516 | 148 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_manager.z.so` |
| `005ad6681000-005ad671d000` | .so | `r-xp` | 624 | 248 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_manager.z.so` |
| `005ad671d000-005ad6735000` | .so | `r--p` | 96 | 28 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_manager.z.so` |
| `005ad6735000-005ad6736000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_manager.z.so` |
| `005ad6740000-005ad6742000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_container_scope.z.so` |
| `005ad6780000-005ad679c000` | .so | `r--p` | 112 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libipc_napi.z.so` |
| `005ad679c000-005ad67ce000` | .so | `r-xp` | 200 | 48 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libipc_napi.z.so` |
| `005ad67ce000-005ad67d3000` | .so | `r--p` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libipc_napi.z.so` |
| `005ad67d3000-005ad67d4000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libipc_napi.z.so` |
| `005ad67d4000-005ad67d5000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libipc_napi.z.so.bss]` |
| `005ad67d5000-005ad67fb000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6800000-005ad6813000` | .so | `r--p` | 76 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_preferences.z.so` |
| `005ad6813000-005ad6849000` | .so | `r-xp` | 216 | 116 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_preferences.z.so` |
| `005ad6849000-005ad684d000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_preferences.z.so` |
| `005ad684d000-005ad684e000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_preferences.z.so` |
| `005ad684e000-005ad6874000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6880000-005ad6882000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwsutils.z.so` |
| `005ad6882000-005ad6886000` | .so | `r-xp` | 16 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwsutils.z.so` |
| `005ad6886000-005ad6887000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwsutils.z.so` |
| `005ad6887000-005ad6888000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwsutils.z.so` |
| `005ad6888000-005ad68ae000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad68c0000-005ad68ca000` | .so | `r--p` | 40 | 40 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwmutil_base.z.so` |
| `005ad68ca000-005ad68db000` | .so | `r-xp` | 68 | 32 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwmutil_base.z.so` |
| `005ad68db000-005ad68de000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwmutil_base.z.so` |
| `005ad68de000-005ad68df000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwmutil_base.z.so` |
| `005ad6900000-005ad6907000` | .so | `r--p` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_client.z.so` |
| `005ad6907000-005ad6914000` | .so | `r-xp` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_client.z.so` |
| `005ad6914000-005ad6915000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_client.z.so` |
| `005ad6915000-005ad6916000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libappspawn_client.z.so` |
| `005ad6916000-005ad693c000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6940000-005ad694c000` | .so | `r--p` | 48 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdi.z.so` |
| `005ad694c000-005ad6958000` | .so | `r-xp` | 48 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdi.z.so` |
| `005ad6958000-005ad695b000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdi.z.so` |
| `005ad695b000-005ad695d000` | .so | `rw-p` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdi.z.so` |
| `005ad695d000-005ad6972000` | dev | `rw-s` | 84 | 84 | 84 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6980000-005ad6985000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.3.z.so` |
| `005ad6985000-005ad698b000` | .so | `r-xp` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.3.z.so` |
| `005ad698b000-005ad698d000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.3.z.so` |
| `005ad698d000-005ad698e000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.3.z.so` |
| `005ad698e000-005ad69b4000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad69c0000-005ad6a14000` | .so | `r--p` | 336 | 104 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libxml2.z.so` |
| `005ad6a14000-005ad6ae8000` | .so | `r-xp` | 848 | 240 | 9 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libxml2.z.so` |
| `005ad6ae8000-005ad6af0000` | .so | `r--p` | 32 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libxml2.z.so` |
| `005ad6af0000-005ad6af1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libxml2.z.so` |
| `005ad6af1000-005ad6af2000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libxml2.z.so.bss]` |
| `005ad6b00000-005ad6b02000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstart_window_option.z.so` |
| `005ad6b02000-005ad6b06000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstart_window_option.z.so` |
| `005ad6b06000-005ad6b07000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstart_window_option.z.so` |
| `005ad6b07000-005ad6b08000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstart_window_option.z.so` |
| `005ad6b08000-005ad6b2e000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6b40000-005ad6b44000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsightintentcontext.z.so` |
| `005ad6b44000-005ad6b47000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsightintentcontext.z.so` |
| `005ad6b47000-005ad6b49000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsightintentcontext.z.so` |
| `005ad6b49000-005ad6b4a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsightintentcontext.z.so` |
| `005ad6b4a000-005ad6b70000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6b80000-005ad6b84000` | .so | `r--p` | 16 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libopencl_wrapper.so` |
| `005ad6b84000-005ad6b88000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libopencl_wrapper.so` |
| `005ad6b88000-005ad6b8a000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libopencl_wrapper.so` |
| `005ad6b8a000-005ad6b8b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libopencl_wrapper.so` |
| `005ad6b8b000-005ad6bb1000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6bc0000-005ad6bed000` | .so | `r--p` | 180 | 76 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsqlite.z.so` |
| `005ad6bed000-005ad6d41000` | .so | `r-xp` | 1360 | 884 | 19 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsqlite.z.so` |
| `005ad6d41000-005ad6d45000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsqlite.z.so` |
| `005ad6d45000-005ad6d49000` | .so | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsqlite.z.so` |
| `005ad6d49000-005ad6d6f000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6d80000-005ad6d83000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_animation_utils.z.so` |
| `005ad6d83000-005ad6d88000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_animation_utils.z.so` |
| `005ad6d88000-005ad6d8a000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_animation_utils.z.so` |
| `005ad6d8a000-005ad6d8b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_animation_utils.z.so` |
| `005ad6d8b000-005ad6db1000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6e40000-005ad6e4b000` | .so | `r--p` | 44 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libfileuri_native.z.so` |
| `005ad6e4b000-005ad6e66000` | .so | `r-xp` | 108 | 24 | 2 | 0 | 0 | 0.00% | `/system/lib64/libfileuri_native.z.so` |
| `005ad6e66000-005ad6e68000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libfileuri_native.z.so` |
| `005ad6e68000-005ad6e69000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libfileuri_native.z.so` |
| `005ad6e69000-005ad6e6a000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libfileuri_native.z.so.bss]` |
| `005ad6e80000-005ad6e99000` | .so | `r--p` | 100 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextensionwindow_napi.z.so` |
| `005ad6e99000-005ad6ec4000` | .so | `r-xp` | 172 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextensionwindow_napi.z.so` |
| `005ad6ec4000-005ad6ec9000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextensionwindow_napi.z.so` |
| `005ad6ec9000-005ad6eca000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextensionwindow_napi.z.so` |
| `005ad6eca000-005ad6ef0000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6f00000-005ad6f23000` | .so | `r--p` | 140 | 68 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_context_native.z.so` |
| `005ad6f4f000-005ad6f50000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_context_native.z.so` |
| `005ad6f50000-005ad6f76000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad6f80000-005ad6f8d000` | .so | `r--p` | 52 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libremote_file_share_native.z.so` |
| `005ad6f8d000-005ad6faf000` | .so | `r-xp` | 136 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libremote_file_share_native.z.so` |
| `005ad6faf000-005ad6fb1000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libremote_file_share_native.z.so` |
| `005ad6fb1000-005ad6fb2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libremote_file_share_native.z.so` |
| `005ad6fc0000-005ad6fcc000` | .so | `r--p` | 48 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libjs_environment.z.so` |
| `005ad6fcc000-005ad6fd8000` | .so | `r-xp` | 48 | 44 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libjs_environment.z.so` |
| `005ad6fd8000-005ad6fda000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libjs_environment.z.so` |
| `005ad6fda000-005ad6fdb000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libjs_environment.z.so` |
| `005ad7000000-005ad7040000` | .so | `r--p` | 256 | 100 | 5 | 0 | 0 | 0.00% | `/system/lib64/libdm.z.so` |
| `005ad7040000-005ad70bb000` | .so | `r-xp` | 492 | 180 | 7 | 0 | 0 | 0.00% | `/system/lib64/libdm.z.so` |
| `005ad70bb000-005ad70d9000` | .so | `r--p` | 120 | 88 | 3 | 0 | 0 | 0.00% | `/system/lib64/libdm.z.so` |
| `005ad70d9000-005ad70da000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libdm.z.so` |
| `005ad7100000-005ad7110000` | .so | `r--p` | 64 | 64 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_context_utils.z.so` |
| `005ad7110000-005ad7126000` | .so | `r-xp` | 88 | 60 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_context_utils.z.so` |
| `005ad7126000-005ad7128000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_context_utils.z.so` |
| `005ad7128000-005ad7129000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_context_utils.z.so` |
| `005ad7140000-005ad7149000` | .so | `r--p` | 36 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libwindow_animation.z.so` |
| `005ad7149000-005ad7153000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwindow_animation.z.so` |
| `005ad7153000-005ad7157000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwindow_animation.z.so` |
| `005ad7157000-005ad7158000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwindow_animation.z.so` |
| `005ad7158000-005ad7159000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libwindow_animation.z.so.bss]` |
| `005ad7180000-005ad7186000` | .so | `r--p` | 24 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/libweb_configs.z.so` |
| `005ad7186000-005ad7192000` | .so | `r-xp` | 48 | 48 | 3 | 0 | 0 | 0.00% | `/system/lib64/libweb_configs.z.so` |
| `005ad7192000-005ad7194000` | .so | `r--p` | 8 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/libweb_configs.z.so` |
| `005ad7194000-005ad7195000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libweb_configs.z.so` |
| `005ad71c0000-005ad71ca000` | .so | `r--p` | 40 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdf_ipc_adapter.z.so` |
| `005ad71ca000-005ad71da000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdf_ipc_adapter.z.so` |
| `005ad71da000-005ad71dd000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdf_ipc_adapter.z.so` |
| `005ad71dd000-005ad71de000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libhdf_ipc_adapter.z.so` |
| `005ad7200000-005ad7202000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfreeze_util.z.so` |
| `005ad7202000-005ad7207000` | .so | `r-xp` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfreeze_util.z.so` |
| `005ad7207000-005ad7208000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfreeze_util.z.so` |
| `005ad7208000-005ad7209000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfreeze_util.z.so` |
| `005ad7240000-005ad7247000` | .so | `r--p` | 28 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_dfx.z.so` |
| `005ad7247000-005ad725b000` | .so | `r-xp` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_dfx.z.so` |
| `005ad725b000-005ad7263000` | .so | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_dfx.z.so` |
| `005ad7263000-005ad7264000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_dfx.z.so` |
| `005ad7280000-005ad7285000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_analyzer.z.so` |
| `005ad7285000-005ad728c000` | .so | `r-xp` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_analyzer.z.so` |
| `005ad728c000-005ad728e000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_analyzer.z.so` |
| `005ad728e000-005ad728f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libframe_analyzer.z.so` |
| `005ad728f000-005ad7291000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libframe_analyzer.z.so.bss]` |
| `005ad72c0000-005ad72c7000` | .so | `r--p` | 28 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrawable_descriptor.z.so` |
| `005ad72c7000-005ad72d5000` | .so | `r-xp` | 56 | 48 | 7 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrawable_descriptor.z.so` |
| `005ad72d5000-005ad72d6000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrawable_descriptor.z.so` |
| `005ad72d6000-005ad72d7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrawable_descriptor.z.so` |
| `005ad7300000-005ad730f000` | .so | `r--p` | 60 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_manager.z.so` |
| `005ad730f000-005ad733f000` | .so | `r-xp` | 192 | 104 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_manager.z.so` |
| `005ad733f000-005ad7343000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_manager.z.so` |
| `005ad7343000-005ad7344000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_manager.z.so` |
| `005ad7344000-005ad737d000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad7380000-005ad7384000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstartup_util.z.so` |
| `005ad7384000-005ad738d000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstartup_util.z.so` |
| `005ad738d000-005ad738e000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstartup_util.z.so` |
| `005ad738e000-005ad738f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstartup_util.z.so` |
| `005ad73c0000-005ad73c3000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/librtg_interface.z.so` |
| `005ad73c3000-005ad73c7000` | .so | `r-xp` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/librtg_interface.z.so` |
| `005ad73c7000-005ad73c9000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/librtg_interface.z.so` |
| `005ad73c9000-005ad73ca000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/librtg_interface.z.so` |
| `005ad7400000-005ad743d000` | .so | `r--p` | 244 | 64 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libudmf_client.z.so` |
| `005ad743d000-005ad74ee000` | .so | `r-xp` | 708 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libudmf_client.z.so` |
| `005ad74ee000-005ad74f8000` | .so | `r--p` | 40 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libudmf_client.z.so` |
| `005ad74f8000-005ad74f9000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libudmf_client.z.so` |
| `005ad74f9000-005ad74fb000` | FilePage other | `rw-p` | 8 | 4 | 1 | 0 | 0 | 0.00% | `[anon:libudmf_client.z.so.bss]` |
| `005ad7500000-005ad765b000` | .so | `r--p` | 1388 | 612 | 22 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libcrypto_openssl.z.so` |
| `005ad765b000-005ad782d000` | .so | `r-xp` | 1864 | 1084 | 38 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libcrypto_openssl.z.so` |
| `005ad782d000-005ad788e000` | .so | `r--p` | 388 | 340 | 15 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libcrypto_openssl.z.so` |
| `005ad788e000-005ad7891000` | .so | `rw-p` | 12 | 12 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libcrypto_openssl.z.so` |
| `005ad7891000-005ad7894000` | FilePage other | `rw-p` | 12 | 12 | 8 | 0 | 0 | 0.00% | `[anon:libcrypto_openssl.z.so.bss]` |
| `005ad78c0000-005ad78c3000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcj_bind_native.z.so` |
| `005ad78c3000-005ad78c6000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcj_bind_native.z.so` |
| `005ad78c6000-005ad78c7000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcj_bind_native.z.so` |
| `005ad78c7000-005ad78c8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcj_bind_native.z.so` |
| `005ad7900000-005ad7924000` | .so | `r--p` | 144 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_inner.z.so` |
| `005ad7924000-005ad7990000` | .so | `r-xp` | 432 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_inner.z.so` |
| `005ad7990000-005ad799a000` | .so | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_inner.z.so` |
| `005ad799a000-005ad799b000` | .so | `rw-p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddata_inner.z.so` |
| `005ad799b000-005ad799c000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdistributeddata_inner.z.so.bss]` |
| `005ad79c0000-005ad79d7000` | .so | `r--p` | 92 | 44 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibility_common.z.so` |
| `005ad79d7000-005ad79f0000` | .so | `r-xp` | 100 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibility_common.z.so` |
| `005ad79f0000-005ad79f1000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibility_common.z.so` |
| `005ad79f1000-005ad79f2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibility_common.z.so` |
| `005ad79f2000-005ad79f3000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaccessibility_common.z.so.bss]` |
| `005ad7a00000-005ad7a01000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiperf_local.z.so` |
| `005ad7a01000-005ad7a03000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiperf_local.z.so` |
| `005ad7a03000-005ad7a04000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiperf_local.z.so` |
| `005ad7a04000-005ad7a05000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiperf_local.z.so` |
| `005ad7a05000-005ad7a3e000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad7a40000-005ad7b08000` | GL | `r--p` | 800 | 80 | 14 | 0 | 0 | 0.00% | `/system/lib64/libarkweb_core_loader_glue.z.so` |
| `005ad7b08000-005ad7c14000` | GL | `r-xp` | 1072 | 84 | 21 | 0 | 0 | 0.00% | `/system/lib64/libarkweb_core_loader_glue.z.so` |
| `005ad7c14000-005ad7c2a000` | GL | `r--p` | 88 | 32 | 8 | 0 | 0 | 0.00% | `/system/lib64/libarkweb_core_loader_glue.z.so` |
| `005ad7c2a000-005ad7c2d000` | GL | `rw-p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/libarkweb_core_loader_glue.z.so` |
| `005ad7c2d000-005ad7c35000` | GL | `rw-p` | 32 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libarkweb_core_loader_glue.z.so.bss]` |
| `005ad7c40000-005ad7c7e000` | .so | `r--p` | 248 | 40 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_accessor.z.so` |
| `005ad7c7e000-005ad7d50000` | .so | `r-xp` | 840 | 232 | 38 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_accessor.z.so` |
| `005ad7d50000-005ad7d58000` | .so | `r--p` | 32 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_accessor.z.so` |
| `005ad7d58000-005ad7d59000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_accessor.z.so` |
| `005ad7d59000-005ad7d5a000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libimage_accessor.z.so.bss]` |
| `005ad7d80000-005ad7e05000` | .so | `r--p` | 532 | 144 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_manager.z.so` |
| `005ad7e05000-005ad7e96000` | .so | `r-xp` | 580 | 224 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_manager.z.so` |
| `005ad7e96000-005ad7eb8000` | .so | `r--p` | 136 | 48 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_manager.z.so` |
| `005ad7eb8000-005ad7eb9000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_manager.z.so` |
| `005ad7eb9000-005ad7eba000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libapp_manager.z.so.bss]` |
| `005ad7ec0000-005ad7ec3000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcolor_manager.z.so` |
| `005ad7ec3000-005ad7ec7000` | .so | `r-xp` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcolor_manager.z.so` |
| `005ad7ec7000-005ad7ec8000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcolor_manager.z.so` |
| `005ad7ec8000-005ad7ec9000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcolor_manager.z.so` |
| `005ad7ec9000-005ad7eca000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libcolor_manager.z.so.bss]` |
| `005ad7f00000-005ad7f03000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_deps_wrapper.z.so` |
| `005ad7f03000-005ad7f05000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_deps_wrapper.z.so` |
| `005ad7f05000-005ad7f06000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_deps_wrapper.z.so` |
| `005ad7f06000-005ad7f07000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_deps_wrapper.z.so` |
| `005ad7f07000-005ad7f40000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad7f40000-005ad7f47000` | .so | `r--p` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libtask_handler_wrap.z.so` |
| `005ad7f47000-005ad7f4e000` | .so | `r-xp` | 28 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/libtask_handler_wrap.z.so` |
| `005ad7f4e000-005ad7f4f000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libtask_handler_wrap.z.so` |
| `005ad7f4f000-005ad7f50000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libtask_handler_wrap.z.so` |
| `005ad7f80000-005ad7f89000` | .so | `r--p` | 36 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/appspawn/appspawn/libappspawn_ace.z.so` |
| `005ad7f89000-005ad7f95000` | .so | `r-xp` | 48 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/appspawn/libappspawn_ace.z.so` |
| `005ad7f95000-005ad7f97000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/appspawn/libappspawn_ace.z.so` |
| `005ad7f97000-005ad7f98000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/appspawn/appspawn/libappspawn_ace.z.so` |
| `005ad7fc0000-005ad7fd3000` | .so | `r--p` | 76 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_manager_lite.z.so` |
| `005ad7fd3000-005ad7ff6000` | .so | `r-xp` | 140 | 108 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_manager_lite.z.so` |
| `005ad7ff6000-005ad7ffc000` | .so | `r--p` | 24 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_manager_lite.z.so` |
| `005ad7ffc000-005ad7ffd000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_manager_lite.z.so` |
| `005ad8000000-005ad8003000` | GL | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libegl_image.z.so` |
| `005ad8003000-005ad8009000` | GL | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libegl_image.z.so` |
| `005ad8009000-005ad800a000` | GL | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libegl_image.z.so` |
| `005ad800a000-005ad800b000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libegl_image.z.so` |
| `005ad8040000-005ad8059000` | .so | `r--p` | 100 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlpparse.z.so` |
| `005ad8059000-005ad8095000` | .so | `r-xp` | 240 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlpparse.z.so` |
| `005ad8095000-005ad8099000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlpparse.z.so` |
| `005ad8099000-005ad809a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdlpparse.z.so` |
| `005ad809a000-005ad809b000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdlpparse.z.so.bss]` |
| `005ad80c0000-005ad80ce000` | .so | `r--p` | 56 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_manager_helper.z.so` |
| `005ad80ce000-005ad80de000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_manager_helper.z.so` |
| `005ad80de000-005ad80df000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_manager_helper.z.so` |
| `005ad80df000-005ad80e0000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappkit_manager_helper.z.so` |
| `005ad8100000-005ad8105000` | .so | `r--p` | 20 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libview_data.z.so` |
| `005ad8105000-005ad8115000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libview_data.z.so` |
| `005ad8115000-005ad8117000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libview_data.z.so` |
| `005ad8117000-005ad8118000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libview_data.z.so` |
| `005ad8140000-005ad8144000` | .so | `r--p` | 16 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconfiguration_helper.z.so` |
| `005ad8144000-005ad814a000` | .so | `r-xp` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconfiguration_helper.z.so` |
| `005ad814a000-005ad814b000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconfiguration_helper.z.so` |
| `005ad814b000-005ad814c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconfiguration_helper.z.so` |
| `005ad8180000-005ad818e000` | .so | `r--p` | 56 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcodec_proxy_4.0.z.so` |
| `005ad818e000-005ad819f000` | .so | `r-xp` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcodec_proxy_4.0.z.so` |
| `005ad819f000-005ad81a1000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcodec_proxy_4.0.z.so` |
| `005ad81a1000-005ad81a2000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcodec_proxy_4.0.z.so` |
| `005ad81c0000-005ad81c4000` | .so | `r--p` | 16 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpreferred_language.z.so` |
| `005ad81c4000-005ad81c9000` | .so | `r-xp` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpreferred_language.z.so` |
| `005ad81c9000-005ad81ca000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpreferred_language.z.so` |
| `005ad81ca000-005ad81cb000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpreferred_language.z.so` |
| `005ad8200000-005ad8206000` | .so | `r--p` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/librelational_common_base.z.so` |
| `005ad8206000-005ad8214000` | .so | `r-xp` | 56 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/librelational_common_base.z.so` |
| `005ad8214000-005ad8215000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/librelational_common_base.z.so` |
| `005ad8215000-005ad8216000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/librelational_common_base.z.so` |
| `005ad8240000-005ad8241000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_strings_internal.z.so` |
| `005ad8241000-005ad8243000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_strings_internal.z.so` |
| `005ad8243000-005ad8244000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_strings_internal.z.so` |
| `005ad8244000-005ad8245000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libabsl_strings_internal.z.so` |
| `005ad8245000-005ad827e000` | dev | `rw-s` | 228 | 228 | 228 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad8280000-005ad8284000` | .so | `r--p` | 16 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_info.z.so` |
| `005ad8284000-005ad8289000` | .so | `r-xp` | 20 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_info.z.so` |
| `005ad8289000-005ad828a000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_info.z.so` |
| `005ad828a000-005ad828b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsession_info.z.so` |
| `005ad82c0000-005ad8452000` | .so | `r--p` | 1608 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libohosffmpeg.z.so` |
| `005ad8452000-005ad8943000` | .so | `r-xp` | 5060 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libohosffmpeg.z.so` |
| `005ad8943000-005ad898e000` | .so | `r--p` | 300 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libohosffmpeg.z.so` |
| `005ad898e000-005ad8990000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libohosffmpeg.z.so` |
| `005ad8990000-005ad9c8c000` | FilePage other | `rw-p` | 19440 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libohosffmpeg.z.so.bss]` |
| `005ad9cc0000-005ad9cc5000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_connect_callback_stub.z.so` |
| `005ad9cc5000-005ad9cc8000` | .so | `r-xp` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_connect_callback_stub.z.so` |
| `005ad9cc8000-005ad9cca000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_connect_callback_stub.z.so` |
| `005ad9cca000-005ad9ccb000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_connect_callback_stub.z.so` |
| `005ad9ccb000-005ad9ccc000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libability_connect_callback_stub.z.so.bss]` |
| `005ad9d00000-005ad9d28000` | .so | `r--p` | 160 | 84 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiappevent_base.z.so` |
| `005ad9d28000-005ad9d7c000` | .so | `r-xp` | 336 | 308 | 15 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiappevent_base.z.so` |
| `005ad9d7c000-005ad9d80000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiappevent_base.z.so` |
| `005ad9d80000-005ad9d81000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhiappevent_base.z.so` |
| `005ad9d81000-005ad9d85000` | FilePage other | `rw-p` | 16 | 16 | 13 | 0 | 0 | 0.00% | `[anon:libhiappevent_base.z.so.bss]` |
| `005ad9d85000-005ad9dbe000` | FilePage other | `r--p` | 228 | 228 | 228 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNShortMovie-harmony_dd07347/dyrnshortmovie.bundle` |
| `005ad9dc0000-005ad9dd5000` | .so | `r--p` | 84 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktsbase.so` |
| `005ad9dd5000-005ad9e0b000` | .so | `r-xp` | 216 | 44 | 3 | 0 | 0 | 0.00% | `/system/lib64/libarktsbase.so` |
| `005ad9e0b000-005ad9e0e000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktsbase.so` |
| `005ad9e0e000-005ad9e0f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libarktsbase.so` |
| `005ad9e0f000-005ad9e19000` | FilePage other | `rw-p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarktsbase.so.bss]` |
| `005ad9e19000-005ad9e3f000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ad9e40000-005ad9e42000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbuffer_handle.z.so` |
| `005ad9e42000-005ad9e43000` | .so | `r-xp` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbuffer_handle.z.so` |
| `005ad9e43000-005ad9e45000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbuffer_handle.z.so` |
| `005ad9e45000-005ad9e46000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libbuffer_handle.z.so` |
| `005ad9e46000-005ad9e7f000` | FilePage other | `r--p` | 228 | 228 | 228 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNShowGoods-harmony_db6d281/dyrnshowgoods.bundle` |
| `005ad9e80000-005ad9e92000` | .so | `r--p` | 72 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libchild_process_manager.z.so` |
| `005ad9e92000-005ad9ea5000` | .so | `r-xp` | 76 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libchild_process_manager.z.so` |
| `005ad9ea5000-005ad9ea7000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libchild_process_manager.z.so` |
| `005ad9ea7000-005ad9ea8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libchild_process_manager.z.so` |
| `005ad9ec0000-005ad9ed8000` | .so | `r--p` | 96 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextensionkit_native.z.so` |
| `005ad9ed8000-005ad9eef000` | .so | `r-xp` | 92 | 60 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextensionkit_native.z.so` |
| `005ad9eef000-005ad9ef1000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextensionkit_native.z.so` |
| `005ad9ef1000-005ad9ef2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextensionkit_native.z.so` |
| `005ad9ef2000-005ad9ef3000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libextensionkit_native.z.so.bss]` |
| `005ad9f00000-005ad9f05000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconnect_server_manager.z.so` |
| `005ad9f05000-005ad9f0b000` | .so | `r-xp` | 24 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconnect_server_manager.z.so` |
| `005ad9f0b000-005ad9f0c000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconnect_server_manager.z.so` |
| `005ad9f0c000-005ad9f0d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconnect_server_manager.z.so` |
| `005ad9f40000-005ad9f92000` | .so | `r--p` | 328 | 132 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_rdb.z.so` |
| `005ad9f92000-005ada092000` | .so | `r-xp` | 1024 | 752 | 20 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_rdb.z.so` |
| `005ada092000-005ada09f000` | .so | `r--p` | 52 | 52 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_rdb.z.so` |
| `005ada09f000-005ada0a0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnative_rdb.z.so` |
| `005ada0a0000-005ada0a1000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libnative_rdb.z.so.bss]` |
| `005ada0c0000-005ada0ce000` | .so | `r--p` | 56 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_util.z.so` |
| `005ada0ce000-005ada0ef000` | .so | `r-xp` | 132 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_util.z.so` |
| `005ada0ef000-005ada0f1000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_util.z.so` |
| `005ada0f1000-005ada0f2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdevicestatus_util.z.so` |
| `005ada100000-005ada14b000` | .so | `r--p` | 300 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_client.z.so` |
| `005ada14b000-005ada1fa000` | .so | `r-xp` | 700 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_client.z.so` |
| `005ada1fa000-005ada200000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_client.z.so` |
| `005ada200000-005ada202000` | .so | `rw-p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_client.z.so` |
| `005ada202000-005ada23f000` | FilePage other | `r--p` | 244 | 244 | 244 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNFansHome-harmony_e4ce489/dyrnfanshome.bundle` |
| `005ada240000-005ada2ce000` | .so | `r--p` | 568 | 252 | 16 | 0 | 0 | 0.00% | `/system/lib64/libwm.z.so` |
| `005ada2ce000-005ada47a000` | .so | `r-xp` | 1712 | 1028 | 70 | 0 | 0 | 0.00% | `/system/lib64/libwm.z.so` |
| `005ada47a000-005ada4a6000` | .so | `r--p` | 176 | 84 | 3 | 0 | 0 | 0.00% | `/system/lib64/libwm.z.so` |
| `005ada4a6000-005ada4a7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libwm.z.so` |
| `005ada4a7000-005ada4ab000` | FilePage other | `rw-p` | 16 | 12 | 8 | 0 | 0 | 0.00% | `[anon:libwm.z.so.bss]` |
| `005ada4c0000-005ada4ea000` | .so | `r--p` | 168 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibility_interface.z.so` |
| `005ada4ea000-005ada549000` | .so | `r-xp` | 380 | 64 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibility_interface.z.so` |
| `005ada549000-005ada558000` | .so | `r--p` | 60 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibility_interface.z.so` |
| `005ada558000-005ada559000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibility_interface.z.so` |
| `005ada559000-005ada57f000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ada580000-005ada599000` | .so | `r--p` | 100 | 28 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddb_client.z.so` |
| `005ada599000-005ada5df000` | .so | `r-xp` | 280 | 44 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddb_client.z.so` |
| `005ada5df000-005ada5e1000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddb_client.z.so` |
| `005ada5e1000-005ada5e2000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributeddb_client.z.so` |
| `005ada5e2000-005ada5e3000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libdistributeddb_client.z.so.bss]` |
| `005ada600000-005ada602000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libruntime_utils.z.so` |
| `005ada602000-005ada606000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libruntime_utils.z.so` |
| `005ada606000-005ada607000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libruntime_utils.z.so` |
| `005ada607000-005ada608000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libruntime_utils.z.so` |
| `005ada608000-005ada62e000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ada6c3000-005ada6e9000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ada700000-005ada71f000` | GL | `r--p` | 124 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/libGLESv3.so` |
| `005ada780000-005ada790000` | .so | `r--p` | 64 | 40 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbundle_napi_common.z.so` |
| `005ada790000-005ada7ae000` | .so | `r-xp` | 120 | 64 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbundle_napi_common.z.so` |
| `005ada7ae000-005ada7b0000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbundle_napi_common.z.so` |
| `005ada7b0000-005ada7b1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbundle_napi_common.z.so` |
| `005ada7c0000-005ada7c5000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.2.z.so` |
| `005ada7c5000-005ada7ca000` | .so | `r-xp` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.2.z.so` |
| `005ada7ca000-005ada7cc000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.2.z.so` |
| `005ada7cc000-005ada7cd000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdisplay_buffer_proxy_1.2.z.so` |
| `005ada7cd000-005ada7f3000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ada800000-005ada83f000` | GL | `r--p` | 252 | 32 | 2 | 0 | 0 | 0.00% | `/system/lib64/libvulkan.so` |
| `005ada83f000-005ada87f000` | GL | `r-xp` | 256 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvulkan.so` |
| `005ada87f000-005ada882000` | GL | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvulkan.so` |
| `005ada882000-005ada883000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvulkan.so` |
| `005ada883000-005ada8a9000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ada8c0000-005ada8c2000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_trace_intf.z.so` |
| `005ada8c2000-005ada8c4000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_trace_intf.z.so` |
| `005ada8c4000-005ada8c5000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_trace_intf.z.so` |
| `005ada8c5000-005ada8c6000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_trace_intf.z.so` |
| `005ada8c6000-005ada8ec000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ada900000-005ada903000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblz4_shared.z.so` |
| `005ada903000-005ada920000` | .so | `r-xp` | 116 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblz4_shared.z.so` |
| `005ada920000-005ada921000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblz4_shared.z.so` |
| `005ada921000-005ada922000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblz4_shared.z.so` |
| `005ada940000-005ada947000` | .so | `r--p` | 28 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconfiguration.z.so` |
| `005ada947000-005ada954000` | .so | `r-xp` | 52 | 52 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconfiguration.z.so` |
| `005ada954000-005ada955000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconfiguration.z.so` |
| `005ada955000-005ada956000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libconfiguration.z.so` |
| `005ada956000-005ada97c000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005ada980000-005ada98a000` | .so | `r--p` | 40 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libarkweb_utils.z.so` |
| `005ada98a000-005ada9a0000` | .so | `r-xp` | 88 | 28 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libarkweb_utils.z.so` |
| `005ada9a0000-005ada9a2000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libarkweb_utils.z.so` |
| `005ada9a2000-005ada9a3000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libarkweb_utils.z.so` |
| `005ada9c0000-005ada9c4000` | .so | `r--p` | 16 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_start_options.z.so` |
| `005ada9c4000-005ada9ca000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_start_options.z.so` |
| `005ada9ca000-005ada9cc000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_start_options.z.so` |
| `005ada9cc000-005ada9cd000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_start_options.z.so` |
| `005ada9cd000-005ada9f3000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005adaa00000-005adaa05000` | .so | `r--p` | 20 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdlp_permission_common_interface.z.so` |
| `005adaa05000-005adaa16000` | .so | `r-xp` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdlp_permission_common_interface.z.so` |
| `005adaa16000-005adaa17000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdlp_permission_common_interface.z.so` |
| `005adaa17000-005adaa18000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdlp_permission_common_interface.z.so` |
| `005adaa18000-005adaa3e000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005adaa40000-005adaa4a000` | .so | `r--p` | 40 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libshared_libz.z.so` |
| `005adaa4a000-005adaa60000` | .so | `r-xp` | 88 | 84 | 3 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libshared_libz.z.so` |
| `005adaa60000-005adaa61000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libshared_libz.z.so` |
| `005adaa61000-005adaa62000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libshared_libz.z.so` |
| `005adaa80000-005adaa91000` | .so | `r--p` | 68 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libpng.z.so` |
| `005adaa91000-005adaac0000` | .so | `r-xp` | 188 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libpng.z.so` |
| `005adaac0000-005adaac2000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libpng.z.so` |
| `005adaac2000-005adaac3000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libpng.z.so` |
| `005adaac3000-005adaae9000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005adab00000-005adab29000` | .so | `r--p` | 164 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_utils.z.so` |
| `005adab29000-005adab6a000` | .so | `r-xp` | 260 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_utils.z.so` |
| `005adab6a000-005adab6c000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_utils.z.so` |
| `005adab6c000-005adab6f000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoftbus_utils.z.so` |
| `005adab6f000-005adab71000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libsoftbus_utils.z.so.bss]` |
| `005adab80000-005adab82000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libqos.z.so` |
| `005adab82000-005adab84000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libqos.z.so` |
| `005adab84000-005adab85000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libqos.z.so` |
| `005adab85000-005adab86000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libqos.z.so` |
| `005adab86000-005adabac000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005adabc0000-005adabcf000` | .so | `r--p` | 60 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libturbojpeg.z.so` |
| `005adabcf000-005adac27000` | .so | `r-xp` | 352 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libturbojpeg.z.so` |
| `005adac27000-005adac29000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libturbojpeg.z.so` |
| `005adac29000-005adac2a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libturbojpeg.z.so` |
| `005adac40000-005adac42000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhispeed_image.so` |
| `005adac42000-005adac5f000` | .so | `r-xp` | 116 | 112 | 24 | 0 | 0 | 0.00% | `/system/lib64/libhispeed_image.so` |
| `005adac5f000-005adac60000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhispeed_image.so` |
| `005adac60000-005adac61000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhispeed_image.so` |
| `005adac80000-005adac84000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimageformatagent.z.so` |
| `005adac84000-005adac8d000` | .so | `r-xp` | 36 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimageformatagent.z.so` |
| `005adac8d000-005adac8e000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimageformatagent.z.so` |
| `005adac8e000-005adac8f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimageformatagent.z.so` |
| `005adac8f000-005adac90000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libimageformatagent.z.so.bss]` |
| `005adac90000-005adae90000` | dev | `r--s` | 2048 | 40 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:persist_param:s0` |
| `005adb110000-005adb136000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005adb140000-005adb156000` | .so | `r--p` | 88 | 24 | 2 | 0 | 0 | 0.00% | `/system/lib64/ndk/libudmf.so` |
| `005adb156000-005adb181000` | .so | `r-xp` | 172 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libudmf.so` |
| `005adb181000-005adb186000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libudmf.so` |
| `005adb186000-005adb187000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libudmf.so` |
| `005adb200000-005adb201000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005adb800000-005adb801000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005adb801000-005add682000` | FilePage other | `r--s` | 31236 | 568 | 83 | 0 | 0 | 0.00% | `/system/usr/icu/icudt74l.dat` |
| `005add682000-005add6c0000` | FilePage other | `r--p` | 248 | 248 | 124 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRN202309Duel-harmony_6be2120/dyrn202309duel.bundle` |
| `005add6c0000-005add6d0000` | .so | `r--p` | 64 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_haptic.z.so` |
| `005add6d0000-005add6e8000` | .so | `r-xp` | 96 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_haptic.z.so` |
| `005add6e8000-005add6ea000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_haptic.z.so` |
| `005add6ea000-005add6eb000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_haptic.z.so` |
| `005add6eb000-005add6ec000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaudio_haptic.z.so.bss]` |
| `005add700000-005add703000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeable_pixelmap_builder.z.so` |
| `005add703000-005add708000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeable_pixelmap_builder.z.so` |
| `005add708000-005add709000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeable_pixelmap_builder.z.so` |
| `005add709000-005add70a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpurgeable_pixelmap_builder.z.so` |
| `005add70a000-005add730000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005add740000-005add748000` | .so | `r--p` | 32 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_library_common.z.so` |
| `005add748000-005add75d000` | .so | `r-xp` | 84 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_library_common.z.so` |
| `005add75d000-005add75f000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_library_common.z.so` |
| `005add75f000-005add760000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_library_common.z.so` |
| `005add780000-005add782000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libxpower_event_js.z.so` |
| `005add782000-005add784000` | .so | `r-xp` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libxpower_event_js.z.so` |
| `005add784000-005add786000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libxpower_event_js.z.so` |
| `005add786000-005add787000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libxpower_event_js.z.so` |
| `005add787000-005add7ad000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005add7c0000-005add814000` | .so | `r--p` | 336 | 192 | 23 | 0 | 0 | 0.00% | `/system/lib64/libaudio_framework_interface.z.so` |
| `005add814000-005add905000` | .so | `r-xp` | 964 | 436 | 148 | 0 | 0 | 0.00% | `/system/lib64/libaudio_framework_interface.z.so` |
| `005add905000-005add92d000` | .so | `r--p` | 160 | 56 | 9 | 0 | 0 | 0.00% | `/system/lib64/libaudio_framework_interface.z.so` |
| `005add92d000-005add92e000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_framework_interface.z.so` |
| `005add92e000-005add92f000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libaudio_framework_interface.z.so.bss]` |
| `005add940000-005add948000` | .so | `r--p` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_utils.z.so` |
| `005add948000-005add96b000` | .so | `r-xp` | 140 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_utils.z.so` |
| `005add96b000-005add96d000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_utils.z.so` |
| `005add96d000-005add96e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_utils.z.so` |
| `005add980000-005add99c000` | .so | `r--p` | 112 | 36 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibilityclient.z.so` |
| `005add99c000-005add9c9000` | .so | `r-xp` | 180 | 64 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibilityclient.z.so` |
| `005add9c9000-005add9cf000` | .so | `r--p` | 24 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibilityclient.z.so` |
| `005add9cf000-005add9d0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccessibilityclient.z.so` |
| `005add9d0000-005add9f6000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005adda00000-005adda09000` | .so | `r--p` | 36 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_extension_client.z.so` |
| `005adda09000-005adda13000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_extension_client.z.so` |
| `005adda13000-005adda18000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_extension_client.z.so` |
| `005adda18000-005adda19000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindow_extension_client.z.so` |
| `005adda19000-005adda3f000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005adda40000-005adda4a000` | .so | `r--p` | 40 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdisplaymgr.z.so` |
| `005adda4a000-005adda5a000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdisplaymgr.z.so` |
| `005adda5a000-005adda5e000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdisplaymgr.z.so` |
| `005adda5e000-005adda5f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdisplaymgr.z.so` |
| `005adda5f000-005adda60000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libdisplaymgr.z.so.bss]` |
| `005adda80000-005addaab000` | .so | `r--p` | 172 | 120 | 37 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_client.z.so` |
| `005addaab000-005addac2000` | .so | `r-xp` | 92 | 92 | 17 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_client.z.so` |
| `005addac2000-005addac6000` | .so | `r--p` | 16 | 16 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_client.z.so` |
| `005addac6000-005addac7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_client.z.so` |
| `005addac7000-005addaed000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005addb00000-005addb07000` | .so | `r--p` | 28 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfmskit_provider_client.z.so` |
| `005addb07000-005addb12000` | .so | `r-xp` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfmskit_provider_client.z.so` |
| `005addb12000-005addb14000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfmskit_provider_client.z.so` |
| `005addb14000-005addb15000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfmskit_provider_client.z.so` |
| `005addb15000-005addb16000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libfmskit_provider_client.z.so.bss]` |
| `005addb16000-005addb3c000` | dev | `rw-s` | 152 | 152 | 152 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `005addb40000-005addb4f000` | .so | `r--p` | 60 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_engine_manager.z.so` |
| `005addb4f000-005addb61000` | .so | `r-xp` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_engine_manager.z.so` |
| `005addb61000-005addb65000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_engine_manager.z.so` |
| `005addb65000-005addb66000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_engine_manager.z.so` |
| `005addb66000-005addb67000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaudio_engine_manager.z.so.bss]` |
| `005addb80000-005adddfe000` | .so | `r--p` | 2552 | 128 | 21 | 0 | 0 | 0.00% | `/system/lib64/libarkruntime.so` |
| `005adddfe000-005ade615000` | .so | `r-xp` | 8284 | 184 | 27 | 0 | 0 | 0.00% | `/system/lib64/libarkruntime.so` |
| `005ade615000-005ade647000` | .so | `r--p` | 200 | 80 | 3 | 0 | 0 | 0.00% | `/system/lib64/libarkruntime.so` |
| `005ade647000-005ade64e000` | .so | `rw-p` | 28 | 8 | 4 | 0 | 0 | 0.00% | `/system/lib64/libarkruntime.so` |
| `005ade64e000-005ade65e000` | FilePage other | `rw-p` | 64 | 12 | 0 | 0 | 0 | 0.00% | `[anon:libarkruntime.so.bss]` |
| `005ade680000-005ade6a8000` | .so | `r--p` | 160 | 72 | 13 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_policy_manager.z.so` |
| `005ade6a8000-005ade6c6000` | .so | `r-xp` | 120 | 88 | 16 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_policy_manager.z.so` |
| `005ade6c6000-005ade6c9000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_policy_manager.z.so` |
| `005ade6c9000-005ade6ca000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_policy_manager.z.so` |
| `005ade6ca000-005ade6cb000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaudio_policy_manager.z.so.bss]` |
| `005ade700000-005ade715000` | .so | `r--p` | 84 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfmskit_native.z.so` |
| `005ade715000-005ade740000` | .so | `r-xp` | 172 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfmskit_native.z.so` |
| `005ade740000-005ade743000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfmskit_native.z.so` |
| `005ade743000-005ade744000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfmskit_native.z.so` |
| `005ade780000-005ade783000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_service_utils.z.so` |
| `005ade783000-005ade788000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_service_utils.z.so` |
| `005ade788000-005ade789000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_service_utils.z.so` |
| `005ade789000-005ade78a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_service_utils.z.so` |
| `005ade7c0000-005ade7f3000` | .so | `r--p` | 204 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/lib3dWidgetAdapter.z.so` |
| `005ade7f3000-005ade88d000` | .so | `r-xp` | 616 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/lib3dWidgetAdapter.z.so` |
| `005ade88d000-005ade893000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/lib3dWidgetAdapter.z.so` |
| `005ade893000-005ade894000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/lib3dWidgetAdapter.z.so` |
| `005ade894000-005ade89f000` | FilePage other | `rw-p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `[anon:lib3dWidgetAdapter.z.so.bss]` |
| `005ade8c0000-005ade8c4000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_ipc_common.z.so` |
| `005ade8c4000-005ade8cb000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_ipc_common.z.so` |
| `005ade8cb000-005ade8cc000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_ipc_common.z.so` |
| `005ade8cc000-005ade8cd000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_ipc_common.z.so` |
| `005ade900000-005ade90e000` | .so | `r--p` | 56 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/libperfmonitor.z.so` |
| `005ade90e000-005ade931000` | .so | `r-xp` | 140 | 124 | 8 | 0 | 0 | 0.00% | `/system/lib64/libperfmonitor.z.so` |
| `005ade931000-005ade934000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libperfmonitor.z.so` |
| `005ade934000-005ade935000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libperfmonitor.z.so` |
| `005ade940000-005ade94c000` | .so | `r--p` | 48 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_helper_native.z.so` |
| `005ade94c000-005ade967000` | .so | `r-xp` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_helper_native.z.so` |
| `005ade967000-005ade969000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_helper_native.z.so` |
| `005ade969000-005ade96a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_helper_native.z.so` |
| `005ade96a000-005ade96b000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libsandbox_helper_native.z.so.bss]` |
| `005ade980000-005ade985000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_common_info.z.so` |
| `005ade985000-005ade98e000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_common_info.z.so` |
| `005ade98e000-005ade990000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_common_info.z.so` |
| `005ade990000-005ade991000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_common_info.z.so` |
| `005ade9c0000-005ade9ca000` | .so | `r--p` | 40 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextra_config_napi.z.so` |
| `005ade9ca000-005ade9da000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextra_config_napi.z.so` |
| `005ade9da000-005ade9dc000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextra_config_napi.z.so` |
| `005ade9dc000-005ade9dd000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextra_config_napi.z.so` |
| `005adea00000-005adea24000` | .so | `r--p` | 144 | 40 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpasteboard_client.z.so` |
| `005adea24000-005adea8c000` | .so | `r-xp` | 416 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpasteboard_client.z.so` |
| `005adea8c000-005adea9a000` | .so | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpasteboard_client.z.so` |
| `005adea9a000-005adea9b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpasteboard_client.z.so` |
| `005adea9b000-005adea9c000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libpasteboard_client.z.so.bss]` |
| `005adeac0000-005adeae7000` | .so | `r--p` | 156 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_manager.z.so` |
| `005adeae7000-005adeb39000` | .so | `r-xp` | 328 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_manager.z.so` |
| `005adeb39000-005adeb45000` | .so | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_manager.z.so` |
| `005adeb45000-005adeb46000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libform_manager.z.so` |
| `005adeb46000-005adeb47000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libform_manager.z.so.bss]` |
| `005adeb80000-005adeb8a000` | .so | `r--p` | 40 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libpasteboard_framework.z.so` |
| `005adeb8a000-005adeba2000` | .so | `r-xp` | 96 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpasteboard_framework.z.so` |
| `005adeba2000-005adeba6000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpasteboard_framework.z.so` |
| `005adeba6000-005adeba7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpasteboard_framework.z.so` |
| `005adebc0000-005adec3b000` | .so | `r--p` | 492 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_library.z.so` |
| `005adec3b000-005aded54000` | .so | `r-xp` | 1124 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_library.z.so` |
| `005aded54000-005aded5b000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_library.z.so` |
| `005aded5b000-005aded5c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_library.z.so` |
| `005aded5c000-005aded73000` | FilePage other | `rw-p` | 92 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libmedia_library.z.so.bss]` |
| `005adedcc000-005adedcd000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_renderer.z.so` |
| `005adee00000-005adee20000` | .so | `r--p` | 128 | 44 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpasteboard_data.z.so` |
| `005adee20000-005adee86000` | .so | `r-xp` | 408 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpasteboard_data.z.so` |
| `005adee86000-005adee8d000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpasteboard_data.z.so` |
| `005adee8d000-005adee8e000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpasteboard_data.z.so` |
| `005adeec0000-005adeef8000` | .so | `r--p` | 224 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrawing_napi_impl.z.so` |
| `005adeef8000-005adef8d000` | .so | `r-xp` | 596 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrawing_napi_impl.z.so` |
| `005adef8d000-005adef96000` | .so | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrawing_napi_impl.z.so` |
| `005adef96000-005adef97000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrawing_napi_impl.z.so` |
| `005adef97000-005adef98000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdrawing_napi_impl.z.so.bss]` |
| `005adefc0000-005adf088000` | .so | `r--p` | 800 | 36 | 5 | 0 | 0 | 0.00% | `/system/lib64/libarkencoder.so` |
| `005adf088000-005adf246000` | .so | `r-xp` | 1784 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkencoder.so` |
| `005adf246000-005adf261000` | .so | `r--p` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkencoder.so` |
| `005adf261000-005adf263000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkencoder.so` |
| `005adf263000-005adf275000` | FilePage other | `rw-p` | 72 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkencoder.so.bss]` |
| `005adf280000-005adf286000` | .so | `r--p` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpixelmap.so` |
| `005adf286000-005adf291000` | .so | `r-xp` | 44 | 44 | 13 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpixelmap.so` |
| `005adf291000-005adf292000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpixelmap.so` |
| `005adf292000-005adf293000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpixelmap.so` |
| `005adf2c0000-005adf2c4000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpip_ndk.so` |
| `005adf2c4000-005adf2cd000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpip_ndk.so` |
| `005adf2cd000-005adf2ce000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpip_ndk.so` |
| `005adf2ce000-005adf2cf000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpip_ndk.so` |
| `005adf300000-005adf305000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librdb_data_share_adapter.z.so` |
| `005adf305000-005adf310000` | .so | `r-xp` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librdb_data_share_adapter.z.so` |
| `005adf310000-005adf311000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librdb_data_share_adapter.z.so` |
| `005adf311000-005adf312000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librdb_data_share_adapter.z.so` |
| `005adf340000-005adf348000` | .so | `r--p` | 32 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_schedule.z.so` |
| `005adf348000-005adf356000` | .so | `r-xp` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_schedule.z.so` |
| `005adf356000-005adf357000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_schedule.z.so` |
| `005adf357000-005adf358000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_schedule.z.so` |
| `005adf358000-005adf359000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaudio_schedule.z.so.bss]` |
| `005adf380000-005adf387000` | .so | `r--p` | 28 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_engine_plugins.z.so` |
| `005adf387000-005adf396000` | .so | `r-xp` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_engine_plugins.z.so` |
| `005adf396000-005adf398000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_engine_plugins.z.so` |
| `005adf398000-005adf399000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_engine_plugins.z.so` |
| `005adf3c0000-005adf401000` | .so | `r--p` | 260 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_effect_impl.so` |
| `005adf401000-005adf490000` | .so | `r-xp` | 572 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_effect_impl.so` |
| `005adf490000-005adf496000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_effect_impl.so` |
| `005adf496000-005adf497000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libimage_effect_impl.so` |
| `005adf497000-005adf498000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libimage_effect_impl.so.bss]` |
| `005adf4c0000-005adf4dd000` | .so | `r--p` | 116 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_library_manager.z.so` |
| `005adf4dd000-005adf52d000` | .so | `r-xp` | 320 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_library_manager.z.so` |
| `005adf52d000-005adf530000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_library_manager.z.so` |
| `005adf530000-005adf531000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libmedia_library_manager.z.so` |
| `005adf531000-005adf533000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libmedia_library_manager.z.so.bss]` |
| `005adf540000-005adf547000` | .so | `r--p` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkaotmanager.so` |
| `005adf547000-005adf55b000` | .so | `r-xp` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkaotmanager.so` |
| `005adf55b000-005adf55d000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkaotmanager.so` |
| `005adf55d000-005adf55e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkaotmanager.so` |
| `005adf580000-005adf582000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libext2_uuid.z.so` |
| `005adf582000-005adf585000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libext2_uuid.z.so` |
| `005adf585000-005adf586000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libext2_uuid.z.so` |
| `005adf586000-005adf587000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libext2_uuid.z.so` |
| `005adf5c0000-005adff72000` | .so | `r--p` | 9928 | 1976 | 192 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_compatible.z.so` |
| `005ae34c0000-005ae34c7000` | .so | `r--p` | 28 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_monitor_client.z.so` |
| `005ae34c7000-005ae34d5000` | .so | `r-xp` | 56 | 56 | 15 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_monitor_client.z.so` |
| `005ae34d5000-005ae34d7000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_monitor_client.z.so` |
| `005ae34d7000-005ae34d8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_monitor_client.z.so` |
| `005ae3500000-005ae3516000` | .so | `r--p` | 88 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrm_framework.z.so` |
| `005ae3516000-005ae3533000` | .so | `r-xp` | 116 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrm_framework.z.so` |
| `005ae3533000-005ae353b000` | .so | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrm_framework.z.so` |
| `005ae353b000-005ae353c000` | .so | `rw-p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdrm_framework.z.so` |
| `005ae3540000-005ae3543000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_base_want.so` |
| `005ae3543000-005ae354b000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_base_want.so` |
| `005ae354b000-005ae354c000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_base_want.so` |
| `005ae354c000-005ae354d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_base_want.so` |
| `005ae3580000-005ae3597000` | .so | `r--p` | 92 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_service_utils.z.so` |
| `005ae3597000-005ae35cb000` | .so | `r-xp` | 208 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_service_utils.z.so` |
| `005ae35cb000-005ae35ce000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_service_utils.z.so` |
| `005ae35ce000-005ae35cf000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_service_utils.z.so` |
| `005ae3694000-005ae3695000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_common.z.so` |
| `005ae3695000-005ae3696000` | FilePage other | `rw-p` | 4 | 4 | 2 | 0 | 0 | 0.00% | `[anon:libaudio_common.z.so.bss]` |
| `005ae36c0000-005ae36c2000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsonic.z.so` |
| `005ae36c2000-005ae36c5000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsonic.z.so` |
| `005ae36c5000-005ae36c6000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsonic.z.so` |
| `005ae36c6000-005ae36c7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsonic.z.so` |
| `005ae3700000-005ae3724000` | .so | `r--p` | 144 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhistreamer_plugin_base.z.so` |
| `005ae3724000-005ae3759000` | .so | `r-xp` | 212 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhistreamer_plugin_base.z.so` |
| `005ae3759000-005ae375c000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhistreamer_plugin_base.z.so` |
| `005ae375c000-005ae375d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhistreamer_plugin_base.z.so` |
| `005ae3780000-005ae3789000` | .so | `r--p` | 36 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_security_config_if.z.so` |
| `005ae3789000-005ae3793000` | .so | `r-xp` | 40 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_security_config_if.z.so` |
| `005ae3793000-005ae3795000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_security_config_if.z.so` |
| `005ae3795000-005ae3796000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_security_config_if.z.so` |
| `005ae37c0000-005ae37ca000` | .so | `r--p` | 40 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libani_helpers.z.so` |
| `005ae37ca000-005ae37dd000` | .so | `r-xp` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libani_helpers.z.so` |
| `005ae37dd000-005ae37df000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libani_helpers.z.so` |
| `005ae37df000-005ae37e0000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libani_helpers.z.so` |
| `005ae3800000-005ae3809000` | .so | `r--p` | 36 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmiscdevice_utils.z.so` |
| `005ae3809000-005ae3813000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmiscdevice_utils.z.so` |
| `005ae3813000-005ae3816000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmiscdevice_utils.z.so` |
| `005ae3816000-005ae3817000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmiscdevice_utils.z.so` |
| `005ae3840000-005ae385d000` | .so | `r--p` | 116 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoundpool_client.z.so` |
| `005ae385d000-005ae3896000` | .so | `r-xp` | 228 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoundpool_client.z.so` |
| `005ae3896000-005ae389a000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoundpool_client.z.so` |
| `005ae389a000-005ae389b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsoundpool_client.z.so` |
| `005ae38c0000-005ae38cd000` | .so | `r--p` | 52 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libvibrator_native.z.so` |
| `005ae38cd000-005ae38e5000` | .so | `r-xp` | 96 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libvibrator_native.z.so` |
| `005ae38e5000-005ae38e7000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libvibrator_native.z.so` |
| `005ae38e7000-005ae38e8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libvibrator_native.z.so` |
| `005ae38e8000-005ae38e9000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libvibrator_native.z.so.bss]` |
| `005ae3900000-005ae3915000` | .so | `r--p` | 84 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_manager_common.z.so` |
| `005ae3915000-005ae3931000` | .so | `r-xp` | 112 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_manager_common.z.so` |
| `005ae3931000-005ae3934000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_manager_common.z.so` |
| `005ae3934000-005ae3935000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_manager_common.z.so` |
| `005ae3940000-005ae3946000` | .so | `r--p` | 24 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_service_mgr.z.so` |
| `005ae3946000-005ae394d000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_service_mgr.z.so` |
| `005ae394d000-005ae3950000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_service_mgr.z.so` |
| `005ae3950000-005ae3951000` | .so | `rw-p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_service_mgr.z.so` |
| `005ae3980000-005ae398f000` | .so | `r--p` | 60 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libarktsziparchive.so` |
| `005ae398f000-005ae39c1000` | .so | `r-xp` | 200 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktsziparchive.so` |
| `005ae39c1000-005ae39c3000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktsziparchive.so` |
| `005ae39c3000-005ae39c4000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktsziparchive.so` |
| `005ae3a00000-005ae3a3d000` | .so | `r--p` | 244 | 24 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_client.z.so` |
| `005ae3a3d000-005ae3b18000` | .so | `r-xp` | 876 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_client.z.so` |
| `005ae3b18000-005ae3b2b000` | .so | `r--p` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_client.z.so` |
| `005ae3b2b000-005ae3b2c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_client.z.so` |
| `005ae3b2c000-005ae3b2e000` | FilePage other | `rw-p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `[anon:libmedia_client.z.so.bss]` |
| `005ae3b40000-005ae3b49000` | .so | `r--p` | 36 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdata_ability_helper.z.so` |
| `005ae3b49000-005ae3b52000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdata_ability_helper.z.so` |
| `005ae3b52000-005ae3b53000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdata_ability_helper.z.so` |
| `005ae3b53000-005ae3b54000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdata_ability_helper.z.so` |
| `005ae3b80000-005ae3ba5000` | .so | `r--p` | 148 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libarktsfile.so` |
| `005ae3ba5000-005ae3bf1000` | .so | `r-xp` | 304 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktsfile.so` |
| `005ae3bf1000-005ae3bf4000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktsfile.so` |
| `005ae3bf4000-005ae3bf5000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktsfile.so` |
| `005ae3c00000-005ae3c1f000` | .so | `r--p` | 124 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libudmf_data_napi.z.so` |
| `005ae3c1f000-005ae3c7f000` | .so | `r-xp` | 384 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libudmf_data_napi.z.so` |
| `005ae3c7f000-005ae3c85000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libudmf_data_napi.z.so` |
| `005ae3c85000-005ae3c86000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libudmf_data_napi.z.so` |
| `005ae3c86000-005ae3c87000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libudmf_data_napi.z.so.bss]` |
| `005ae3cc0000-005ae3cc4000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librdb_data_ability_adapter.z.so` |
| `005ae3cc4000-005ae3ccf000` | .so | `r-xp` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librdb_data_ability_adapter.z.so` |
| `005ae3ccf000-005ae3cd1000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librdb_data_ability_adapter.z.so` |
| `005ae3cd1000-005ae3cd2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librdb_data_ability_adapter.z.so` |
| `005ae3d00000-005ae3d0a000` | .so | `r--p` | 40 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_foundation.z.so` |
| `005ae3d0a000-005ae3d1a000` | .so | `r-xp` | 64 | 40 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_foundation.z.so` |
| `005ae3d1a000-005ae3d1c000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_foundation.z.so` |
| `005ae3d1c000-005ae3d1d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_foundation.z.so` |
| `005ae3d1d000-005ae3d1e000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaudio_foundation.z.so.bss]` |
| `005ae3d40000-005ae3d46000` | .so | `r--p` | 24 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libuiservice_manager_interface_set.z.so` |
| `005ae3d46000-005ae3d4e000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libuiservice_manager_interface_set.z.so` |
| `005ae3d4e000-005ae3d52000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libuiservice_manager_interface_set.z.so` |
| `005ae3d52000-005ae3d53000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libuiservice_manager_interface_set.z.so` |
| `005ae3d80000-005ae3da4000` | .so | `r--p` | 144 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_policy_client_idl_interface.z.so` |
| `005ae3da4000-005ae3e0e000` | .so | `r-xp` | 424 | 120 | 12 | 0 | 0 | 0.00% | `/system/lib64/libaudio_policy_client_idl_interface.z.so` |
| `005ae3e0e000-005ae3e1e000` | .so | `r--p` | 64 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libaudio_policy_client_idl_interface.z.so` |
| `005ae3e1e000-005ae3e1f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_policy_client_idl_interface.z.so` |
| `005ae3f6f000-005ae3f71000` | .so | `rw-p` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libav_codec_client.z.so` |
| `005ae3f80000-005ae3fa0000` | .so | `r--p` | 128 | 72 | 12 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_utils.z.so` |
| `005ae3feb000-005ae3fec000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_utils.z.so` |
| `005ae4000000-005ae402b000` | .so | `r--p` | 172 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtext_napi_impl.z.so` |
| `005ae402b000-005ae4086000` | .so | `r-xp` | 364 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtext_napi_impl.z.so` |
| `005ae4086000-005ae408c000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtext_napi_impl.z.so` |
| `005ae408c000-005ae408d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtext_napi_impl.z.so` |
| `005ae408d000-005ae408e000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libtext_napi_impl.z.so.bss]` |
| `005ae4144000-005ae4145000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_stream_client.z.so` |
| `005ae4145000-005ae4148000` | FilePage other | `rw-p` | 12 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libaudio_stream_client.z.so.bss]` |
| `005ae4180000-005ae41d6000` | .so | `r--p` | 344 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_media_engine_modules.z.so` |
| `005ae41d6000-005ae4292000` | .so | `r-xp` | 752 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_media_engine_modules.z.so` |
| `005ae4292000-005ae4299000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_media_engine_modules.z.so` |
| `005ae4299000-005ae429a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_media_engine_modules.z.so` |
| `005ae429a000-005ae429b000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libav_codec_media_engine_modules.z.so.bss]` |
| `005ae42c0000-005ae42c8000` | .so | `r--p` | 32 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauto_fill_manager.z.so` |
| `005ae42c8000-005ae42cf000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauto_fill_manager.z.so` |
| `005ae42cf000-005ae42d1000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauto_fill_manager.z.so` |
| `005ae42d1000-005ae42d2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauto_fill_manager.z.so` |
| `005ae4300000-005ae430b000` | .so | `r--p` | 44 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_definitions.z.so` |
| `005ae430b000-005ae4323000` | .so | `r-xp` | 96 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_definitions.z.so` |
| `005ae4323000-005ae4325000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_definitions.z.so` |
| `005ae4325000-005ae4326000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_definitions.z.so` |
| `005ae4340000-005ae4345000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_monitor_common.z.so` |
| `005ae4345000-005ae434c000` | .so | `r-xp` | 28 | 28 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_monitor_common.z.so` |
| `005ae434c000-005ae434d000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_monitor_common.z.so` |
| `005ae434d000-005ae434e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_monitor_common.z.so` |
| `005ae4380000-005ae43a4000` | .so | `r--p` | 144 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_client_idl_interface.z.so` |
| `005ae43a4000-005ae43f7000` | .so | `r-xp` | 332 | 156 | 27 | 0 | 0 | 0.00% | `/system/lib64/libaudio_client_idl_interface.z.so` |
| `005ae43f7000-005ae4401000` | .so | `r--p` | 40 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libaudio_client_idl_interface.z.so` |
| `005ae4401000-005ae4402000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaudio_client_idl_interface.z.so` |
| `005ae4402000-005ae4440000` | FilePage other | `r--p` | 248 | 248 | 124 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRN202309Duel-harmony_6be2120/dyrn202309duel.bundle` |
| `005ae4440000-005ae4458000` | .so | `r--p` | 96 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_capturer.z.so` |
| `005ae4458000-005ae4481000` | .so | `r-xp` | 164 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_capturer.z.so` |
| `005ae4481000-005ae4485000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_capturer.z.so` |
| `005ae4485000-005ae4486000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_capturer.z.so` |
| `005ae44c0000-005ae44c4000` | .so | `r--p` | 16 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpip_web.z.so` |
| `005ae44c4000-005ae44cc000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpip_web.z.so` |
| `005ae44cc000-005ae44cd000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpip_web.z.so` |
| `005ae44cd000-005ae44ce000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpip_web.z.so` |
| `005ae4500000-005ae451b000` | .so | `r--p` | 108 | 20 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_session.z.so` |
| `005ae451b000-005ae453c000` | .so | `r-xp` | 132 | 60 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_session.z.so` |
| `005ae453c000-005ae4541000` | .so | `r--p` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_session.z.so` |
| `005ae4541000-005ae4542000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_session.z.so` |
| `005ae4542000-005ae4543000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libui_session.z.so.bss]` |
| `005ae4580000-005ae4585000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libvibrator_agent.z.so` |
| `005ae4585000-005ae458b000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libvibrator_agent.z.so` |
| `005ae458b000-005ae458d000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libvibrator_agent.z.so` |
| `005ae458d000-005ae458e000` | .so | `rw-p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libvibrator_agent.z.so` |
| `005ae45c0000-005ae45cd000` | .so | `r--p` | 52 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_service_dfx.z.so` |
| `005ae45cd000-005ae45ea000` | .so | `r-xp` | 116 | 24 | 2 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_service_dfx.z.so` |
| `005ae45ea000-005ae45ec000` | .so | `r--p` | 8 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_service_dfx.z.so` |
| `005ae45ec000-005ae45ed000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libav_codec_service_dfx.z.so` |
| `005ae45ed000-005ae45ee000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libav_codec_service_dfx.z.so.bss]` |
| `005ae4600000-005ae4615000` | GL | `r--p` | 84 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_form_render.z.so` |
| `005ae4615000-005ae4638000` | GL | `r-xp` | 140 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_form_render.z.so` |
| `005ae4638000-005ae463e000` | GL | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_form_render.z.so` |
| `005ae463e000-005ae463f000` | GL | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_form_render.z.so` |
| `005ae463f000-005ae4640000` | GL | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libace_form_render.z.so.bss]` |
| `005ae4640000-005ae466e000` | .so | `r--p` | 184 | 124 | 14 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_policy_client.z.so` |
| `005ae46bc000-005ae46c8000` | .so | `r--p` | 48 | 32 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_policy_client.z.so` |
| `005ae46c8000-005ae46c9000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_policy_client.z.so` |
| `005ae46c9000-005ae46ca000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libaudio_policy_client.z.so.bss]` |
| `005ae4700000-005ae4701000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktarget_options.z.so` |
| `005ae4701000-005ae4703000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktarget_options.z.so` |
| `005ae4703000-005ae4704000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktarget_options.z.so` |
| `005ae4704000-005ae4705000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktarget_options.z.so` |
| `005ae4740000-005ae47cf000` | .so | `r--p` | 572 | 208 | 58 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscene_session_manager.z.so` |
| `005ae47cf000-005ae496a000` | .so | `r-xp` | 1644 | 168 | 55 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscene_session_manager.z.so` |
| `005ae496a000-005ae498c000` | .so | `r--p` | 136 | 16 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscene_session_manager.z.so` |
| `005ae498c000-005ae498d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libscene_session_manager.z.so` |
| `005ae498d000-005ae498f000` | FilePage other | `rw-p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `[anon:libscene_session_manager.z.so.bss]` |
| `005ae49c0000-005ae4a81000` | .so | `r--p` | 772 | 36 | 5 | 0 | 0 | 0.00% | `/system/lib64/libarktscompiler.so` |
| `005ae4a81000-005ae4c5b000` | .so | `r-xp` | 1896 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktscompiler.so` |
| `005ae4c5b000-005ae4c7e000` | .so | `r--p` | 140 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktscompiler.so` |
| `005ae4c7e000-005ae4c7f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarktscompiler.so` |
| `005ae4c7f000-005ae4c83000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarktscompiler.so.bss]` |
| `005ae4c83000-005ae4e83000` | dev | `r--s` | 2048 | 8 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:ohos_boot_param:s0` |
| `005ae51c0000-005ae51d4000` | .so | `r--p` | 80 | 24 | 1 | 0 | 0 | 0.00% | `/vendor/lib64/libdisplay_buffer_vdi_impl.z.so` |
| `005ae51d4000-005ae51ff000` | .so | `r-xp` | 172 | 100 | 7 | 0 | 0 | 0.00% | `/vendor/lib64/libdisplay_buffer_vdi_impl.z.so` |
| `005ae51ff000-005ae5201000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/libdisplay_buffer_vdi_impl.z.so` |
| `005ae5201000-005ae5202000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/vendor/lib64/libdisplay_buffer_vdi_impl.z.so` |
| `005ae5240000-005ae5f60000` | GL | `r--p` | 13440 | 640 | 286 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/indirect/libbishenggpucompiler_v210.so.15` |
| `005ae7a38000-005ae7e54000` | GL | `r--p` | 4208 | 24 | 3 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/indirect/libbishenggpucompiler_v210.so.15` |
| `005ae7e54000-005ae7ea1000` | GL | `rw-p` | 308 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/indirect/libbishenggpucompiler_v210.so.15` |
| `005ae7ea1000-005ae7ef5000` | GL | `rw-p` | 336 | 12 | 12 | 0 | 0 | 0.00% | `[anon:libbishenggpucompiler_v210.so.15.bss]` |
| `005ae7f00000-005ae7f01000` | native heap | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdmabufheap.z.so` |
| `005ae7f01000-005ae7f04000` | native heap | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdmabufheap.z.so` |
| `005ae7f04000-005ae7f05000` | native heap | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdmabufheap.z.so` |
| `005ae7f05000-005ae7f06000` | native heap | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk-sp/libdmabufheap.z.so` |
| `005ae7f40000-005ae7f44000` | .so | `r--p` | 16 | 16 | 2 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/indirect/libosalbase.z.so` |
| `005ae7f44000-005ae7f4a000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/indirect/libosalbase.z.so` |
| `005ae7f4a000-005ae7f4b000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/indirect/libosalbase.z.so` |
| `005ae7f4b000-005ae7f4c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/indirect/libosalbase.z.so` |
| `005ae7ff4000-005ae8180000` | .so | `r--p` | 1584 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libhvgr_v210.so` |
| `005ae83d8000-005ae8580000` | .so | `r--p` | 1696 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libhvgr_v210.so` |
| `005ae860a000-005ae8809000` | .so | `r--p` | 2044 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libhvgr_v210.so` |
| `005ae8840000-005ae8843000` | Graph | `r--p` | 12 | 12 | 1 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libgralloc_priv.z.so` |
| `005ae8843000-005ae8847000` | Graph | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libgralloc_priv.z.so` |
| `005ae8847000-005ae8848000` | Graph | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libgralloc_priv.z.so` |
| `005ae8848000-005ae8849000` | Graph | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libgralloc_priv.z.so` |
| `005aeb480000-005aeb4b6000` | .so | `r--p` | 216 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_common.z.so` |
| `005aeb4b6000-005aeb4fb000` | .so | `r-xp` | 276 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_common.z.so` |
| `005aeb4fb000-005aeb4ff000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_common.z.so` |
| `005aeb4ff000-005aeb500000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_common.z.so` |
| `005aeb500000-005aeb541000` | .so | `r--p` | 260 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaccessibility_extension_module.z.so` |
| `005aeb541000-005aeb5c4000` | .so | `r-xp` | 524 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaccessibility_extension_module.z.so` |
| `005aeb5c4000-005aeb5c9000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaccessibility_extension_module.z.so` |
| `005aeb5c9000-005aeb5cb000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaccessibility_extension_module.z.so` |
| `005aeb5cb000-005aeb5cc000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaccessibility_extension_module.z.so.bss]` |
| `005aeb600000-005aeb639000` | .so | `r--p` | 228 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/librpc_taihe.z.so` |
| `005aeb639000-005aeb67d000` | .so | `r-xp` | 272 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librpc_taihe.z.so` |
| `005aeb67d000-005aeb683000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librpc_taihe.z.so` |
| `005aeb683000-005aeb684000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librpc_taihe.z.so` |
| `005aeb684000-005aeb687000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:librpc_taihe.z.so.bss]` |
| `005aeb6c0000-005aeb6c1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libresourceManager_ani.z.so` |
| `005aeb6c1000-005aeb6c4000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libresourceManager_ani.z.so` |
| `005aeb6c4000-005aeb6c5000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libresourceManager_ani.z.so` |
| `005aeb6c5000-005aeb6c6000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libresourceManager_ani.z.so` |
| `005aeb700000-005aeb704000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_window_animation_utils.z.so` |
| `005aeb704000-005aeb70b000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_window_animation_utils.z.so` |
| `005aeb70b000-005aeb70c000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_window_animation_utils.z.so` |
| `005aeb70c000-005aeb70d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_window_animation_utils.z.so` |
| `005aeb740000-005aeb75b000` | .so | `r--p` | 108 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libbms_ani_common.z.so` |
| `005aeb75b000-005aeb788000` | .so | `r-xp` | 180 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libbms_ani_common.z.so` |
| `005aeb788000-005aeb789000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libbms_ani_common.z.so` |
| `005aeb789000-005aeb78a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libbms_ani_common.z.so` |
| `005aeb78a000-005aeb78b000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libbms_ani_common.z.so.bss]` |
| `005aeb7c0000-005aeb7d9000` | .so | `r--p` | 100 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaccessibleability.z.so` |
| `005aeb7d9000-005aeb800000` | .so | `r-xp` | 156 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaccessibleability.z.so` |
| `005aeb800000-005aeb806000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaccessibleability.z.so` |
| `005aeb806000-005aeb807000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaccessibleability.z.so` |
| `005aeb840000-005aeb841000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaccount_logout_extension_module.z.so` |
| `005aeb841000-005aeb843000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaccount_logout_extension_module.z.so` |
| `005aeb843000-005aeb844000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaccount_logout_extension_module.z.so` |
| `005aeb844000-005aeb845000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaccount_logout_extension_module.z.so` |
| `005aeb880000-005aeb888000` | .so | `r--p` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaccount_logout_extension.z.so` |
| `005aeb888000-005aeb892000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaccount_logout_extension.z.so` |
| `005aeb892000-005aeb895000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaccount_logout_extension.z.so` |
| `005aeb895000-005aeb896000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaccount_logout_extension.z.so` |
| `005aeb8c0000-005aeb8c6000` | .so | `r--p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaction_extension.z.so` |
| `005aeb8c6000-005aeb8cc000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaction_extension.z.so` |
| `005aeb8cc000-005aeb8cd000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaction_extension.z.so` |
| `005aeb8cd000-005aeb8ce000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libaction_extension.z.so` |
| `005aeb8ce000-005aeb8cf000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaction_extension.z.so.bss]` |
| `005aeb900000-005aeb902000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaction_extension_module.z.so` |
| `005aeb902000-005aeb904000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaction_extension_module.z.so` |
| `005aeb904000-005aeb905000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaction_extension_module.z.so` |
| `005aeb905000-005aeb906000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libaction_extension_module.z.so` |
| `005aeb940000-005aeb942000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libadsservice_extension_module.z.so` |
| `005aeb942000-005aeb945000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libadsservice_extension_module.z.so` |
| `005aeb945000-005aeb946000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libadsservice_extension_module.z.so` |
| `005aeb946000-005aeb947000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libadsservice_extension_module.z.so` |
| `005aeb980000-005aeb988000` | .so | `r--p` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libadsservice_extension.z.so` |
| `005aeb988000-005aeb98f000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libadsservice_extension.z.so` |
| `005aeb98f000-005aeb991000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libadsservice_extension.z.so` |
| `005aeb991000-005aeb992000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libadsservice_extension.z.so` |
| `005aeb9c0000-005aeb9c7000` | .so | `r--p` | 28 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libagent_extension.z.so` |
| `005aeb9c7000-005aeb9cc000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libagent_extension.z.so` |
| `005aeb9cc000-005aeb9cd000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libagent_extension.z.so` |
| `005aeb9cd000-005aeb9ce000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libagent_extension.z.so` |
| `005aeb9ce000-005aeb9cf000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libagent_extension.z.so.bss]` |
| `005aeba00000-005aeba02000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libagent_extension_module.z.so` |
| `005aeba02000-005aeba05000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libagent_extension_module.z.so` |
| `005aeba05000-005aeba06000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libagent_extension_module.z.so` |
| `005aeba06000-005aeba07000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libagent_extension_module.z.so` |
| `005aeba40000-005aeba42000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libagent_ui_extension_module.z.so` |
| `005aeba42000-005aeba45000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libagent_ui_extension_module.z.so` |
| `005aeba45000-005aeba46000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libagent_ui_extension_module.z.so` |
| `005aeba46000-005aeba47000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libagent_ui_extension_module.z.so` |
| `005aeba80000-005aeba86000` | .so | `r--p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libagent_ui_extension.z.so` |
| `005aeba86000-005aeba8c000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libagent_ui_extension.z.so` |
| `005aeba8c000-005aeba8d000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libagent_ui_extension.z.so` |
| `005aeba8d000-005aeba8e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libagent_ui_extension.z.so` |
| `005aeba8e000-005aeba8f000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libagent_ui_extension.z.so.bss]` |
| `005aebac0000-005aebac2000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libapp_service_extension_module.z.so` |
| `005aebac2000-005aebac5000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libapp_service_extension_module.z.so` |
| `005aebac5000-005aebac6000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libapp_service_extension_module.z.so` |
| `005aebac6000-005aebac7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libapp_service_extension_module.z.so` |
| `005aebb00000-005aebb13000` | .so | `r--p` | 76 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_service_extension.z.so` |
| `005aebb13000-005aebb25000` | .so | `r-xp` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_service_extension.z.so` |
| `005aebb25000-005aebb29000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_service_extension.z.so` |
| `005aebb29000-005aebb2a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libapp_service_extension.z.so` |
| `005aebb40000-005aebb65000` | .so | `r--p` | 148 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libservice_extension.z.so` |
| `005aebb65000-005aebb86000` | .so | `r-xp` | 132 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libservice_extension.z.so` |
| `005aebb86000-005aebb8a000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libservice_extension.z.so` |
| `005aebb8a000-005aebb8b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libservice_extension.z.so` |
| `005aebbc0000-005aebbce000` | .so | `r--p` | 56 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libassetcacheextension.z.so` |
| `005aebbce000-005aebbe7000` | .so | `r-xp` | 100 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libassetcacheextension.z.so` |
| `005aebbe7000-005aebbea000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libassetcacheextension.z.so` |
| `005aebbea000-005aebbeb000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libassetcacheextension.z.so` |
| `005aebbeb000-005aebbec000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libassetcacheextension.z.so.bss]` |
| `005aebc00000-005aebc02000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libauto_fill_extension_module.z.so` |
| `005aebc02000-005aebc04000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libauto_fill_extension_module.z.so` |
| `005aebc04000-005aebc05000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libauto_fill_extension_module.z.so` |
| `005aebc05000-005aebc06000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libauto_fill_extension_module.z.so` |
| `005aebc40000-005aebc55000` | .so | `r--p` | 84 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libauto_fill_extension.z.so` |
| `005aebc55000-005aebc68000` | .so | `r-xp` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libauto_fill_extension.z.so` |
| `005aebc68000-005aebc6a000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libauto_fill_extension.z.so` |
| `005aebc6a000-005aebc6b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libauto_fill_extension.z.so` |
| `005aebc6b000-005aebc6c000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libauto_fill_extension.z.so.bss]` |
| `005aebc80000-005aebcb5000` | .so | `r--p` | 212 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libbackup_extension_ability_native.z.so` |
| `005aebcb5000-005aebd2e000` | .so | `r-xp` | 484 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libbackup_extension_ability_native.z.so` |
| `005aebd2e000-005aebd34000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libbackup_extension_ability_native.z.so` |
| `005aebd34000-005aebd35000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libbackup_extension_ability_native.z.so` |
| `005aebd35000-005aebd39000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libbackup_extension_ability_native.z.so.bss]` |
| `005aebd40000-005aebd6a000` | .so | `r--p` | 168 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbackup_utils.z.so` |
| `005aebd6a000-005aebdd7000` | .so | `r-xp` | 436 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbackup_utils.z.so` |
| `005aebdd7000-005aebddb000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbackup_utils.z.so` |
| `005aebddb000-005aebddc000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbackup_utils.z.so` |
| `005aebddc000-005aebde2000` | FilePage other | `rw-p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libbackup_utils.z.so.bss]` |
| `005aebe00000-005aebe1f000` | .so | `r--p` | 124 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbackup_kit_inner.z.so` |
| `005aebe1f000-005aebe5e000` | .so | `r-xp` | 252 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbackup_kit_inner.z.so` |
| `005aebe5e000-005aebe67000` | .so | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbackup_kit_inner.z.so` |
| `005aebe67000-005aebe68000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbackup_kit_inner.z.so` |
| `005aebe68000-005aebe69000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libbackup_kit_inner.z.so.bss]` |
| `005aebe80000-005aebe82000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcaller_info_query_extension_module.z.so` |
| `005aebe82000-005aebe85000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcaller_info_query_extension_module.z.so` |
| `005aebe85000-005aebe86000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcaller_info_query_extension_module.z.so` |
| `005aebe86000-005aebe87000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcaller_info_query_extension_module.z.so` |
| `005aebec0000-005aebecf000` | .so | `r--p` | 60 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcaller_info_query_extension.z.so` |
| `005aebecf000-005aebede000` | .so | `r-xp` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcaller_info_query_extension.z.so` |
| `005aebede000-005aebee2000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcaller_info_query_extension.z.so` |
| `005aebee2000-005aebee3000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcaller_info_query_extension.z.so` |
| `005aebf00000-005aebf13000` | .so | `r--p` | 76 | 16 | 3 | 0 | 0 | 0.00% | `/system/lib64/libcontent_embed_extension.z.so` |
| `005aebf13000-005aebf29000` | .so | `r-xp` | 88 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcontent_embed_extension.z.so` |
| `005aebf29000-005aebf2f000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcontent_embed_extension.z.so` |
| `005aebf2f000-005aebf30000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcontent_embed_extension.z.so` |
| `005aebf40000-005aebf42000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcontent_embed_extension_module.z.so` |
| `005aebf42000-005aebf46000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcontent_embed_extension_module.z.so` |
| `005aebf46000-005aebf47000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcontent_embed_extension_module.z.so` |
| `005aebf47000-005aebf48000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcontent_embed_extension_module.z.so` |
| `005aebf80000-005aebf97000` | .so | `r--p` | 92 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcontent_embed_document.so` |
| `005aebf97000-005aebfc1000` | .so | `r-xp` | 168 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcontent_embed_document.so` |
| `005aebfc1000-005aebfc3000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcontent_embed_document.so` |
| `005aebfc3000-005aebfc4000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcontent_embed_document.so` |
| `005aebfc4000-005aebfc5000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libcontent_embed_document.so.bss]` |
| `005aec000000-005aec004000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcrypto_extension_module.z.so` |
| `005aec004000-005aec00d000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcrypto_extension_module.z.so` |
| `005aec00d000-005aec00e000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcrypto_extension_module.z.so` |
| `005aec00e000-005aec00f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libcrypto_extension_module.z.so` |
| `005aec040000-005aec04d000` | .so | `r--p` | 52 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libcrypto_extension_ability_native.z.so` |
| `005aec04d000-005aec067000` | .so | `r-xp` | 104 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcrypto_extension_ability_native.z.so` |
| `005aec067000-005aec06b000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcrypto_extension_ability_native.z.so` |
| `005aec06b000-005aec06c000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcrypto_extension_ability_native.z.so` |
| `005aec080000-005aec082000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdatashare_ext_ability_module.z.so` |
| `005aec082000-005aec085000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdatashare_ext_ability_module.z.so` |
| `005aec085000-005aec086000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdatashare_ext_ability_module.z.so` |
| `005aec086000-005aec087000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdatashare_ext_ability_module.z.so` |
| `005aec0c0000-005aec0cc000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdatashare_jscommon.z.so` |
| `005aec0cc000-005aec0ea000` | .so | `r-xp` | 120 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdatashare_jscommon.z.so` |
| `005aec0ea000-005aec0ed000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdatashare_jscommon.z.so` |
| `005aec0ed000-005aec0ee000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdatashare_jscommon.z.so` |
| `005aec100000-005aec132000` | .so | `r--p` | 200 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdatashare_ani_rs.so` |
| `005aec132000-005aec1bc000` | .so | `r-xp` | 552 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdatashare_ani_rs.so` |
| `005aec1bc000-005aec1c1000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdatashare_ani_rs.so` |
| `005aec1c1000-005aec1c2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdatashare_ani_rs.so` |
| `005aec1c2000-005aec1c3000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdatashare_ani_rs.so.bss]` |
| `005aec200000-005aec225000` | .so | `r--p` | 148 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdatashare_provider.z.so` |
| `005aec225000-005aec272000` | .so | `r-xp` | 308 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdatashare_provider.z.so` |
| `005aec272000-005aec278000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdatashare_provider.z.so` |
| `005aec278000-005aec279000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdatashare_provider.z.so` |
| `005aec279000-005aec27a000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdatashare_provider.z.so.bss]` |
| `005aec280000-005aec285000` | .so | `r--p` | 20 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributed_sched_utils.z.so` |
| `005aec285000-005aec28c000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributed_sched_utils.z.so` |
| `005aec28c000-005aec28e000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributed_sched_utils.z.so` |
| `005aec28e000-005aec28f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdistributed_sched_utils.z.so` |
| `005aec2c0000-005aec2d9000` | .so | `r--p` | 100 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdistributed_extension_ability_native.z.so` |
| `005aec2d9000-005aec2f6000` | .so | `r-xp` | 116 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdistributed_extension_ability_native.z.so` |
| `005aec2f6000-005aec2fb000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdistributed_extension_ability_native.z.so` |
| `005aec2fb000-005aec2fc000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdistributed_extension_ability_native.z.so` |
| `005aec300000-005aec303000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libreport_sys_event.z.so` |
| `005aec303000-005aec309000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libreport_sys_event.z.so` |
| `005aec309000-005aec30b000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libreport_sys_event.z.so` |
| `005aec30b000-005aec30c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libreport_sys_event.z.so` |
| `005aec340000-005aec34a000` | .so | `r--p` | 40 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdriver_extension.z.so` |
| `005aec34a000-005aec354000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdriver_extension.z.so` |
| `005aec354000-005aec356000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdriver_extension.z.so` |
| `005aec356000-005aec357000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdriver_extension.z.so` |
| `005aec380000-005aec381000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdriver_extension_module.z.so` |
| `005aec381000-005aec383000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdriver_extension_module.z.so` |
| `005aec383000-005aec384000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdriver_extension_module.z.so` |
| `005aec384000-005aec385000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libdriver_extension_module.z.so` |
| `005aec3c0000-005aec3c2000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libembedded_ui_extension_module.z.so` |
| `005aec3c2000-005aec3c5000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libembedded_ui_extension_module.z.so` |
| `005aec3c5000-005aec3c6000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libembedded_ui_extension_module.z.so` |
| `005aec3c6000-005aec3c7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libembedded_ui_extension_module.z.so` |
| `005aec400000-005aec407000` | .so | `r--p` | 28 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libembedded_ui_extension.z.so` |
| `005aec407000-005aec40f000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libembedded_ui_extension.z.so` |
| `005aec40f000-005aec410000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libembedded_ui_extension.z.so` |
| `005aec410000-005aec411000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libembedded_ui_extension.z.so` |
| `005aec440000-005aec45b000` | .so | `r--p` | 108 | 56 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_conn_manager_if.z.so` |
| `005aec45b000-005aec483000` | .so | `r-xp` | 160 | 124 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_conn_manager_if.z.so` |
| `005aec483000-005aec48e000` | .so | `r--p` | 44 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_conn_manager_if.z.so` |
| `005aec48e000-005aec48f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_conn_manager_if.z.so` |
| `005aec4c0000-005aec4cc000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libenterprise_admin_extension.z.so` |
| `005aec4cc000-005aec4e1000` | .so | `r-xp` | 84 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libenterprise_admin_extension.z.so` |
| `005aec4e1000-005aec4e5000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libenterprise_admin_extension.z.so` |
| `005aec4e5000-005aec4e6000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libenterprise_admin_extension.z.so` |
| `005aec500000-005aec509000` | .so | `r--p` | 36 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_edm_common.z.so` |
| `005aec509000-005aec516000` | .so | `r-xp` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_edm_common.z.so` |
| `005aec516000-005aec518000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_edm_common.z.so` |
| `005aec518000-005aec519000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_edm_common.z.so` |
| `005aec540000-005aec542000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libenterprise_admin_extension_module.z.so` |
| `005aec542000-005aec545000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libenterprise_admin_extension_module.z.so` |
| `005aec545000-005aec546000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libenterprise_admin_extension_module.z.so` |
| `005aec546000-005aec547000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libenterprise_admin_extension_module.z.so` |
| `005aec580000-005aec589000` | .so | `r--p` | 36 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libplugin_kits.z.so` |
| `005aec589000-005aec59c000` | .so | `r-xp` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libplugin_kits.z.so` |
| `005aec59c000-005aec59e000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libplugin_kits.z.so` |
| `005aec59e000-005aec59f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libplugin_kits.z.so` |
| `005aec59f000-005aec5a0000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libplugin_kits.z.so.bss]` |
| `005aec5c0000-005aec5c5000` | .so | `r--p` | 20 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libedm_external_adapters.z.so` |
| `005aec5c5000-005aec5cd000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libedm_external_adapters.z.so` |
| `005aec5cd000-005aec5ce000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libedm_external_adapters.z.so` |
| `005aec5ce000-005aec5cf000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libedm_external_adapters.z.so` |
| `005aec600000-005aec60b000` | .so | `r--p` | 44 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsg_collect_sdk.z.so` |
| `005aec60b000-005aec622000` | .so | `r-xp` | 92 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsg_collect_sdk.z.so` |
| `005aec622000-005aec629000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsg_collect_sdk.z.so` |
| `005aec629000-005aec62a000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsg_collect_sdk.z.so` |
| `005aec640000-005aec652000` | .so | `r--p` | 72 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libusbsrv_client.z.so` |
| `005aec652000-005aec677000` | .so | `r-xp` | 148 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libusbsrv_client.z.so` |
| `005aec677000-005aec67c000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libusbsrv_client.z.so` |
| `005aec67c000-005aec67d000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libusbsrv_client.z.so` |
| `005aec680000-005aec6ad000` | .so | `r--p` | 180 | 20 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libedmservice_kits.z.so` |
| `005aec6ad000-005aec70f000` | .so | `r-xp` | 392 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libedmservice_kits.z.so` |
| `005aec70f000-005aec715000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libedmservice_kits.z.so` |
| `005aec715000-005aec716000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libedmservice_kits.z.so` |
| `005aec716000-005aec718000` | FilePage other | `rw-p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libedmservice_kits.z.so.bss]` |
| `005aec740000-005aec74f000` | .so | `r--p` | 60 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libedm_commom.z.so` |
| `005aec74f000-005aec774000` | .so | `r-xp` | 148 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libedm_commom.z.so` |
| `005aec774000-005aec776000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libedm_commom.z.so` |
| `005aec776000-005aec777000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libedm_commom.z.so` |
| `005aec777000-005aec778000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libedm_commom.z.so.bss]` |
| `005aec780000-005aec78b000` | .so | `r--p` | 44 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfaultlogextension.z.so` |
| `005aec78b000-005aec799000` | .so | `r-xp` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfaultlogextension.z.so` |
| `005aec799000-005aec79c000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfaultlogextension.z.so` |
| `005aec79c000-005aec79d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfaultlogextension.z.so` |
| `005aec79d000-005aec79e000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libfaultlogextension.z.so.bss]` |
| `005aec7c0000-005aec7cd000` | .so | `r--p` | 52 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfence_extension_ability.z.so` |
| `005aec7cd000-005aec7da000` | .so | `r-xp` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfence_extension_ability.z.so` |
| `005aec7da000-005aec7dd000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfence_extension_ability.z.so` |
| `005aec7dd000-005aec7de000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfence_extension_ability.z.so` |
| `005aec7de000-005aec7df000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libfence_extension_ability.z.so.bss]` |
| `005aec800000-005aec802000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfile_access_extension_ability_module.z.so` |
| `005aec802000-005aec807000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfile_access_extension_ability_module.z.so` |
| `005aec807000-005aec808000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfile_access_extension_ability_module.z.so` |
| `005aec808000-005aec809000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libfile_access_extension_ability_module.z.so` |
| `005aec840000-005aec867000` | .so | `r--p` | 156 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfile_access_extension_ability_kit.z.so` |
| `005aec867000-005aec8df000` | .so | `r-xp` | 480 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfile_access_extension_ability_kit.z.so` |
| `005aec8df000-005aec8eb000` | .so | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfile_access_extension_ability_kit.z.so` |
| `005aec8eb000-005aec8ec000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfile_access_extension_ability_kit.z.so` |
| `005aec8ec000-005aec8ee000` | FilePage other | `rw-p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `[anon:libfile_access_extension_ability_kit.z.so.bss]` |
| `005aec900000-005aec902000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libform_edit_extension_module.z.so` |
| `005aec902000-005aec905000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libform_edit_extension_module.z.so` |
| `005aec905000-005aec906000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libform_edit_extension_module.z.so` |
| `005aec906000-005aec907000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libform_edit_extension_module.z.so` |
| `005aec940000-005aec94b000` | .so | `r--p` | 44 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libform_edit_extension.z.so` |
| `005aec94b000-005aec95a000` | .so | `r-xp` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libform_edit_extension.z.so` |
| `005aec95a000-005aec95c000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libform_edit_extension.z.so` |
| `005aec95c000-005aec95d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libform_edit_extension.z.so` |
| `005aec980000-005aec982000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libform_extension_module.z.so` |
| `005aec982000-005aec984000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libform_extension_module.z.so` |
| `005aec984000-005aec985000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libform_extension_module.z.so` |
| `005aec985000-005aec986000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libform_extension_module.z.so` |
| `005aec9c0000-005aec9c8000` | .so | `r--p` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libformutil_napi.z.so` |
| `005aec9c8000-005aec9dc000` | .so | `r-xp` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libformutil_napi.z.so` |
| `005aec9dc000-005aec9dd000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libformutil_napi.z.so` |
| `005aec9dd000-005aec9de000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libformutil_napi.z.so` |
| `005aec9de000-005aec9df000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libformutil_napi.z.so.bss]` |
| `005aeca00000-005aeca17000` | .so | `r--p` | 92 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libform_extension.z.so` |
| `005aeca17000-005aeca38000` | .so | `r-xp` | 132 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libform_extension.z.so` |
| `005aeca38000-005aeca3b000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libform_extension.z.so` |
| `005aeca3b000-005aeca3c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libform_extension.z.so` |
| `005aeca3c000-005aeca3d000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libform_extension.z.so.bss]` |
| `005aeca40000-005aeca42000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libinputmethod_extension_module.z.so` |
| `005aeca42000-005aeca45000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libinputmethod_extension_module.z.so` |
| `005aeca45000-005aeca46000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libinputmethod_extension_module.z.so` |
| `005aeca46000-005aeca47000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libinputmethod_extension_module.z.so` |
| `005aeca80000-005aecab3000` | .so | `r--p` | 204 | 20 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libinputmethod_ability.z.so` |
| `005aecab3000-005aecb1c000` | .so | `r-xp` | 420 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libinputmethod_ability.z.so` |
| `005aecb1c000-005aecb28000` | .so | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libinputmethod_ability.z.so` |
| `005aecb28000-005aecb29000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libinputmethod_ability.z.so` |
| `005aecb29000-005aecb2a000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libinputmethod_ability.z.so.bss]` |
| `005aecb40000-005aecb63000` | .so | `r--p` | 140 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinputmethod_extension.z.so` |
| `005aecb63000-005aecb92000` | .so | `r-xp` | 188 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinputmethod_extension.z.so` |
| `005aecb92000-005aecb98000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinputmethod_extension.z.so` |
| `005aecb98000-005aecb99000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinputmethod_extension.z.so` |
| `005aecb99000-005aecb9a000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libinputmethod_extension.z.so.bss]` |
| `005aecbc0000-005aecbc5000` | .so | `r--p` | 20 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsight_intent_ui_extension.z.so` |
| `005aecbc5000-005aecbca000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsight_intent_ui_extension.z.so` |
| `005aecbca000-005aecbcc000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsight_intent_ui_extension.z.so` |
| `005aecbcc000-005aecbcd000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libinsight_intent_ui_extension.z.so` |
| `005aecc00000-005aecc02000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libinsight_intent_ui_extension_module.z.so` |
| `005aecc02000-005aecc03000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libinsight_intent_ui_extension_module.z.so` |
| `005aecc03000-005aecc05000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libinsight_intent_ui_extension_module.z.so` |
| `005aecc05000-005aecc06000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libinsight_intent_ui_extension_module.z.so` |
| `005aecc40000-005aecc4d000` | .so | `r--p` | 52 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/liblive_form_extension.z.so` |
| `005aecc4d000-005aecc5f000` | .so | `r-xp` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/liblive_form_extension.z.so` |
| `005aecc5f000-005aecc61000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/liblive_form_extension.z.so` |
| `005aecc61000-005aecc62000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/liblive_form_extension.z.so` |
| `005aecc80000-005aecc82000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/liblive_form_extension_module.z.so` |
| `005aecc82000-005aecc85000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/liblive_form_extension_module.z.so` |
| `005aecc85000-005aecc86000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/liblive_form_extension_module.z.so` |
| `005aecc86000-005aecc87000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/liblive_form_extension_module.z.so` |
| `005aeccc0000-005aeccc3000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libnotification_subscriber_extension_module.z.so` |
| `005aeccc3000-005aeccc6000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libnotification_subscriber_extension_module.z.so` |
| `005aeccc6000-005aeccc7000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libnotification_subscriber_extension_module.z.so` |
| `005aeccc7000-005aeccc8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libnotification_subscriber_extension_module.z.so` |
| `005aecd00000-005aecd9d000` | .so | `r--p` | 628 | 216 | 20 | 0 | 0 | 0.00% | `/system/lib64/libans_innerkits.z.so` |
| `005aecd9d000-005aeceb5000` | .so | `r-xp` | 1120 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libans_innerkits.z.so` |
| `005aeceb5000-005aeced0000` | .so | `r--p` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libans_innerkits.z.so` |
| `005aeced0000-005aeced1000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libans_innerkits.z.so` |
| `005aeced1000-005aeced2000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libans_innerkits.z.so.bss]` |
| `005aecf00000-005aecf11000` | .so | `r--p` | 68 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnotification_subscriber_extension.z.so` |
| `005aecf11000-005aecf27000` | .so | `r-xp` | 88 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnotification_subscriber_extension.z.so` |
| `005aecf27000-005aecf2a000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnotification_subscriber_extension.z.so` |
| `005aecf2a000-005aecf2b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnotification_subscriber_extension.z.so` |
| `005aecf2b000-005aecf2c000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnotification_subscriber_extension.z.so.bss]` |
| `005aecf40000-005aecf44000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnotification_subscriber_ipc.z.so` |
| `005aecf44000-005aecf4a000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnotification_subscriber_ipc.z.so` |
| `005aecf4a000-005aecf4c000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnotification_subscriber_ipc.z.so` |
| `005aecf4c000-005aecf4d000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnotification_subscriber_ipc.z.so` |
| `005aecf80000-005aecf83000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libpartner_agent_extension_module.z.so` |
| `005aecf83000-005aecf86000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libpartner_agent_extension_module.z.so` |
| `005aecf86000-005aecf87000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libpartner_agent_extension_module.z.so` |
| `005aecf87000-005aecf88000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libpartner_agent_extension_module.z.so` |
| `005aecfc0000-005aecfc4000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_agent_extension_ipc.z.so` |
| `005aecfc4000-005aecfc8000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_agent_extension_ipc.z.so` |
| `005aecfc8000-005aecfcb000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_agent_extension_ipc.z.so` |
| `005aecfcb000-005aecfcc000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_agent_extension_ipc.z.so` |
| `005aed000000-005aed004000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_device_agent_proxy.z.so` |
| `005aed004000-005aed009000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_device_agent_proxy.z.so` |
| `005aed009000-005aed00b000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_device_agent_proxy.z.so` |
| `005aed00b000-005aed00c000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_device_agent_proxy.z.so` |
| `005aed040000-005aed04c000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_agent_extension.z.so` |
| `005aed04c000-005aed058000` | .so | `r-xp` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_agent_extension.z.so` |
| `005aed058000-005aed05b000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_agent_extension.z.so` |
| `005aed05b000-005aed05c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpartner_agent_extension.z.so` |
| `005aed080000-005aed082000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libphoto_editor_extension_module.z.so` |
| `005aed082000-005aed085000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libphoto_editor_extension_module.z.so` |
| `005aed085000-005aed086000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libphoto_editor_extension_module.z.so` |
| `005aed086000-005aed087000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libphoto_editor_extension_module.z.so` |
| `005aed0c0000-005aed0cd000` | .so | `r--p` | 52 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libphoto_editor_extension.z.so` |
| `005aed0cd000-005aed0df000` | .so | `r-xp` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libphoto_editor_extension.z.so` |
| `005aed0df000-005aed0e1000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libphoto_editor_extension.z.so` |
| `005aed0e1000-005aed0e2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libphoto_editor_extension.z.so` |
| `005aed100000-005aed132000` | .so | `r--p` | 200 | 120 | 7 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libssl_openssl.z.so` |
| `005aed132000-005aed183000` | .so | `r-xp` | 324 | 260 | 9 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libssl_openssl.z.so` |
| `005aed183000-005aed18e000` | .so | `r--p` | 44 | 40 | 2 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libssl_openssl.z.so` |
| `005aed18e000-005aed193000` | .so | `rw-p` | 20 | 20 | 5 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libssl_openssl.z.so` |
| `005aed1c0000-005aed1d8000` | .so | `r--p` | 96 | 44 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_models.z.so` |
| `005aed1d8000-005aed227000` | .so | `r-xp` | 316 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_models.z.so` |
| `005aed227000-005aed22b000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_models.z.so` |
| `005aed22b000-005aed22c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_models.z.so` |
| `005aed22c000-005aed233000` | FilePage other | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libprint_models.z.so.bss]` |
| `005aed240000-005aed242000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libprint_extension_module.z.so` |
| `005aed242000-005aed245000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libprint_extension_module.z.so` |
| `005aed245000-005aed246000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libprint_extension_module.z.so` |
| `005aed246000-005aed247000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libprint_extension_module.z.so` |
| `005aed280000-005aed29e000` | .so | `r--p` | 120 | 32 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_client.z.so` |
| `005aed29e000-005aed2dc000` | .so | `r-xp` | 248 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_client.z.so` |
| `005aed2dc000-005aed2e7000` | .so | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_client.z.so` |
| `005aed2e7000-005aed2e8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_client.z.so` |
| `005aed2e8000-005aed2ef000` | FilePage other | `rw-p` | 28 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libprint_client.z.so.bss]` |
| `005aed300000-005aed322000` | .so | `r--p` | 136 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libcups.z.so` |
| `005aed322000-005aed37e000` | .so | `r-xp` | 368 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcups.z.so` |
| `005aed37e000-005aed389000` | .so | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcups.z.so` |
| `005aed389000-005aed38a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcups.z.so` |
| `005aed3c0000-005aed3d1000` | .so | `r--p` | 68 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_helper.z.so` |
| `005aed3d1000-005aed3fd000` | .so | `r-xp` | 176 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_helper.z.so` |
| `005aed3fd000-005aed400000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_helper.z.so` |
| `005aed400000-005aed401000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libprint_helper.z.so` |
| `005aed401000-005aed40c000` | FilePage other | `rw-p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libprint_helper.z.so.bss]` |
| `005aed440000-005aed45a000` | .so | `r--p` | 104 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libprint_extension_framework.z.so` |
| `005aed45a000-005aed483000` | .so | `r-xp` | 164 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libprint_extension_framework.z.so` |
| `005aed483000-005aed487000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libprint_extension_framework.z.so` |
| `005aed487000-005aed488000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libprint_extension_framework.z.so` |
| `005aed488000-005aed48d000` | FilePage other | `rw-p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libprint_extension_framework.z.so.bss]` |
| `005aed4c0000-005aed4c9000` | .so | `r--p` | 36 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libpush_extension.z.so` |
| `005aed4c9000-005aed4d1000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libpush_extension.z.so` |
| `005aed4d1000-005aed4d4000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libpush_extension.z.so` |
| `005aed4d4000-005aed4d5000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libpush_extension.z.so` |
| `005aed500000-005aed529000` | .so | `r--p` | 164 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpush_utils_common.z.so` |
| `005aed529000-005aed561000` | .so | `r-xp` | 224 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpush_utils_common.z.so` |
| `005aed561000-005aed566000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpush_utils_common.z.so` |
| `005aed566000-005aed567000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpush_utils_common.z.so` |
| `005aed567000-005aed568000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libpush_utils_common.z.so.bss]` |
| `005aed580000-005aed58c000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpush_fwk_base.z.so` |
| `005aed58c000-005aed59b000` | .so | `r-xp` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpush_fwk_base.z.so` |
| `005aed59b000-005aed59d000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpush_fwk_base.z.so` |
| `005aed59d000-005aed59e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpush_fwk_base.z.so` |
| `005aed5c0000-005aed5d4000` | .so | `r--p` | 80 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/libdevice_cert_mgr_sdk.z.so` |
| `005aed5d4000-005aed5e8000` | .so | `r-xp` | 80 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdevice_cert_mgr_sdk.z.so` |
| `005aed5e8000-005aed5f3000` | .so | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdevice_cert_mgr_sdk.z.so` |
| `005aed5f3000-005aed5f4000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdevice_cert_mgr_sdk.z.so` |
| `005aed5f4000-005aed5f5000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libdevice_cert_mgr_sdk.z.so.bss]` |
| `005aed600000-005aed609000` | .so | `r--p` | 36 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libremote_location_extension.z.so` |
| `005aed609000-005aed611000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libremote_location_extension.z.so` |
| `005aed611000-005aed614000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libremote_location_extension.z.so` |
| `005aed614000-005aed615000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libremote_location_extension.z.so` |
| `005aed640000-005aed64d000` | .so | `r--p` | 52 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libremote_notification_extension.z.so` |
| `005aed64d000-005aed65b000` | .so | `r-xp` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libremote_notification_extension.z.so` |
| `005aed65b000-005aed65f000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libremote_notification_extension.z.so` |
| `005aed65f000-005aed660000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libremote_notification_extension.z.so` |
| `005aed680000-005aed693000` | .so | `r--p` | 76 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libselection_extension_ability_native.z.so` |
| `005aed693000-005aed6a9000` | .so | `r-xp` | 88 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libselection_extension_ability_native.z.so` |
| `005aed6a9000-005aed6ab000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libselection_extension_ability_native.z.so` |
| `005aed6ab000-005aed6ac000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libselection_extension_ability_native.z.so` |
| `005aed6c0000-005aed6c1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libservice_extension_module.z.so` |
| `005aed6c1000-005aed6c3000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libservice_extension_module.z.so` |
| `005aed6c3000-005aed6c4000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libservice_extension_module.z.so` |
| `005aed6c4000-005aed6c5000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libservice_extension_module.z.so` |
| `005aed700000-005aed702000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libshare_extension_module.z.so` |
| `005aed702000-005aed704000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libshare_extension_module.z.so` |
| `005aed704000-005aed705000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libshare_extension_module.z.so` |
| `005aed705000-005aed706000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libshare_extension_module.z.so` |
| `005aed740000-005aed746000` | .so | `r--p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libshare_extension.z.so` |
| `005aed746000-005aed74c000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libshare_extension.z.so` |
| `005aed74c000-005aed74d000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libshare_extension.z.so` |
| `005aed74d000-005aed74e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libshare_extension.z.so` |
| `005aed74e000-005aed74f000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libshare_extension.z.so.bss]` |
| `005aed780000-005aed784000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libstatic_subscriber_ipc.z.so` |
| `005aed784000-005aed787000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libstatic_subscriber_ipc.z.so` |
| `005aed787000-005aed789000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libstatic_subscriber_ipc.z.so` |
| `005aed789000-005aed78a000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libstatic_subscriber_ipc.z.so` |
| `005aed7c0000-005aed7cc000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libstatic_subscriber_extension.z.so` |
| `005aed7cc000-005aed7d7000` | .so | `r-xp` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libstatic_subscriber_extension.z.so` |
| `005aed7d7000-005aed7da000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libstatic_subscriber_extension.z.so` |
| `005aed7da000-005aed7db000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libstatic_subscriber_extension.z.so` |
| `005aed800000-005aed803000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libstatic_subscriber_extension_module.z.so` |
| `005aed803000-005aed806000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libstatic_subscriber_extension_module.z.so` |
| `005aed806000-005aed807000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libstatic_subscriber_extension_module.z.so` |
| `005aed807000-005aed808000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libstatic_subscriber_extension_module.z.so` |
| `005aed840000-005aed844000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libstatusbar_view_extension.z.so` |
| `005aed844000-005aed84b000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libstatusbar_view_extension.z.so` |
| `005aed84b000-005aed84c000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libstatusbar_view_extension.z.so` |
| `005aed84c000-005aed84d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libstatusbar_view_extension.z.so` |
| `005aed84d000-005aed84e000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libstatusbar_view_extension.z.so.bss]` |
| `005aed880000-005aed886000` | guard | `r--p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libtime_guard_extension.z.so` |
| `005aed886000-005aed88f000` | guard | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libtime_guard_extension.z.so` |
| `005aed88f000-005aed892000` | guard | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libtime_guard_extension.z.so` |
| `005aed892000-005aed893000` | guard | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libtime_guard_extension.z.so` |
| `005aed8c0000-005aed8c3000` | guard | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libtime_guard_extension_module.z.so` |
| `005aed8c3000-005aed8c8000` | guard | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libtime_guard_extension_module.z.so` |
| `005aed8c8000-005aed8c9000` | guard | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libtime_guard_extension_module.z.so` |
| `005aed8c9000-005aed8ca000` | guard | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libtime_guard_extension_module.z.so` |
| `005aed900000-005aed902000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libui_extension_module.z.so` |
| `005aed902000-005aed903000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libui_extension_module.z.so` |
| `005aed903000-005aed905000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libui_extension_module.z.so` |
| `005aed905000-005aed906000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libui_extension_module.z.so` |
| `005aed940000-005aed942000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libui_service_extension_module.z.so` |
| `005aed942000-005aed946000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libui_service_extension_module.z.so` |
| `005aed946000-005aed947000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libui_service_extension_module.z.so` |
| `005aed947000-005aed948000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libui_service_extension_module.z.so` |
| `005aed980000-005aed99a000` | .so | `r--p` | 104 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension.z.so` |
| `005aed99a000-005aed9b2000` | .so | `r-xp` | 96 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension.z.so` |
| `005aed9b2000-005aed9b7000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension.z.so` |
| `005aed9b7000-005aed9b8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension.z.so` |
| `005aed9b8000-005aed9b9000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libui_service_extension.z.so.bss]` |
| `005aed9c0000-005aed9c5000` | .so | `r--p` | 20 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libuser_auth_extension.z.so` |
| `005aed9c5000-005aed9cc000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libuser_auth_extension.z.so` |
| `005aed9cc000-005aed9ce000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libuser_auth_extension.z.so` |
| `005aed9ce000-005aed9cf000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libuser_auth_extension.z.so` |
| `005aeda00000-005aeda02000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libuser_auth_extension_module.z.so` |
| `005aeda02000-005aeda05000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libuser_auth_extension_module.z.so` |
| `005aeda05000-005aeda06000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libuser_auth_extension_module.z.so` |
| `005aeda06000-005aeda07000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libuser_auth_extension_module.z.so` |
| `005aeda40000-005aeda47000` | .so | `r--p` | 28 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libvoip_extension.z.so` |
| `005aeda47000-005aeda4e000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libvoip_extension.z.so` |
| `005aeda4e000-005aeda51000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libvoip_extension.z.so` |
| `005aeda51000-005aeda52000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libvoip_extension.z.so` |
| `005aeda80000-005aeda82000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libvpn_extension_module.z.so` |
| `005aeda82000-005aeda85000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libvpn_extension_module.z.so` |
| `005aeda85000-005aeda86000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libvpn_extension_module.z.so` |
| `005aeda86000-005aeda87000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libvpn_extension_module.z.so` |
| `005aedac0000-005aedad2000` | .so | `r--p` | 72 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvpn_extension.z.so` |
| `005aedad2000-005aedae2000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvpn_extension.z.so` |
| `005aedae2000-005aedae6000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvpn_extension.z.so` |
| `005aedae6000-005aedae7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libvpn_extension.z.so` |
| `005aedb00000-005aedb0c000` | .so | `r--p` | 48 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_utils.z.so` |
| `005aedb0c000-005aedb17000` | .so | `r-xp` | 44 | 44 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_utils.z.so` |
| `005aedb17000-005aedb18000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_utils.z.so` |
| `005aedb18000-005aedb19000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_utils.z.so` |
| `005aedb19000-005aedb1a000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnapi_utils.z.so.bss]` |
| `005aedb40000-005aedb50000` | .so | `r--p` | 64 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwallpaperextensionability.z.so` |
| `005aedb50000-005aedb62000` | .so | `r-xp` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwallpaperextensionability.z.so` |
| `005aedb62000-005aedb65000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwallpaperextensionability.z.so` |
| `005aedb65000-005aedb66000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwallpaperextensionability.z.so` |
| `005aedb66000-005aedb67000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libwallpaperextensionability.z.so.bss]` |
| `005aedb80000-005aedb82000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libwallpaper_extension_module.z.so` |
| `005aedb82000-005aedb85000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libwallpaper_extension_module.z.so` |
| `005aedb85000-005aedb86000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libwallpaper_extension_module.z.so` |
| `005aedb86000-005aedb87000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libwallpaper_extension_module.z.so` |
| `005aedbc0000-005aedbc6000` | .so | `r--p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwallpaper_utils.z.so` |
| `005aedbc6000-005aedbcc000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwallpaper_utils.z.so` |
| `005aedbcc000-005aedbcd000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwallpaper_utils.z.so` |
| `005aedbcd000-005aedbce000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwallpaper_utils.z.so` |
| `005aedc00000-005aedc0e000` | .so | `r--p` | 56 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwallpapermanager.z.so` |
| `005aedc0e000-005aedc1f000` | .so | `r-xp` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwallpapermanager.z.so` |
| `005aedc1f000-005aedc24000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwallpapermanager.z.so` |
| `005aedc24000-005aedc25000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwallpapermanager.z.so` |
| `005aedc25000-005aedc26000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libwallpapermanager.z.so.bss]` |
| `005aedc40000-005aedc49000` | .so | `r--p` | 36 | 24 | 4 | 0 | 0 | 0.00% | `/system/lib64/libwebview_common.z.so` |
| `005aedc49000-005aedc50000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwebview_common.z.so` |
| `005aedc50000-005aedc52000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwebview_common.z.so` |
| `005aedc52000-005aedc53000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwebview_common.z.so` |
| `005aedc80000-005aedc91000` | .so | `r--p` | 68 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libweb_extension.z.so` |
| `005aedc91000-005aedca8000` | .so | `r-xp` | 92 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libweb_extension.z.so` |
| `005aedca8000-005aedcac000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libweb_extension.z.so` |
| `005aedcac000-005aedcad000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libweb_extension.z.so` |
| `005aedcc0000-005aedcc9000` | .so | `r--p` | 36 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libweb_native_messaging_kit.z.so` |
| `005aedcc9000-005aedcd3000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libweb_native_messaging_kit.z.so` |
| `005aedcd3000-005aedcd9000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libweb_native_messaging_kit.z.so` |
| `005aedcd9000-005aedcda000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libweb_native_messaging_kit.z.so` |
| `005aedd00000-005aedd08000` | .so | `r--p` | 32 | 16 | 3 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohweb.so` |
| `005aedd08000-005aedd16000` | .so | `r-xp` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohweb.so` |
| `005aedd16000-005aedd18000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohweb.so` |
| `005aedd18000-005aedd19000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohweb.so` |
| `005aedd40000-005aedd42000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libweb_native_messaging_extension_module.z.so` |
| `005aedd42000-005aedd45000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libweb_native_messaging_extension_module.z.so` |
| `005aedd45000-005aedd46000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libweb_native_messaging_extension_module.z.so` |
| `005aedd46000-005aedd47000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libweb_native_messaging_extension_module.z.so` |
| `005aedd80000-005aedd82000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libwindow_extension_module.z.so` |
| `005aedd82000-005aedd85000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libwindow_extension_module.z.so` |
| `005aedd85000-005aedd86000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libwindow_extension_module.z.so` |
| `005aedd86000-005aedd87000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libwindow_extension_module.z.so` |
| `005aeddc0000-005aeddd0000` | .so | `r--p` | 64 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/libwindow_extension.z.so` |
| `005aeddd0000-005aedde2000` | .so | `r-xp` | 72 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwindow_extension.z.so` |
| `005aedde2000-005aedde6000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwindow_extension.z.so` |
| `005aedde6000-005aedde7000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libwindow_extension.z.so` |
| `005aedde7000-005aedde8000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libwindow_extension.z.so.bss]` |
| `005aede00000-005aede15000` | .so | `r--p` | 84 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libworkschedextension.z.so` |
| `005aede15000-005aede35000` | .so | `r-xp` | 128 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libworkschedextension.z.so` |
| `005aede35000-005aede3b000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libworkschedextension.z.so` |
| `005aede3b000-005aede3c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/extensionability/libworkschedextension.z.so` |
| `005aede40000-005aede4e000` | .so | `r--p` | 56 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libworkschedclient.z.so` |
| `005aede4e000-005aede65000` | .so | `r-xp` | 92 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libworkschedclient.z.so` |
| `005aede65000-005aede67000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libworkschedclient.z.so` |
| `005aede67000-005aede68000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libworkschedclient.z.so` |
| `005aede68000-005aee168000` | dev | `r--s` | 3072 | 0 | 0 | 0 | 0 | 0.00% | `/dev/__parameters__/u:object_r:startup_appspawn_param:s0` |
| `005aee180000-005aee189000` | .so | `r--p` | 36 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libtp_proxy_1.1.z.so` |
| `005aee189000-005aee191000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libtp_proxy_1.1.z.so` |
| `005aee191000-005aee194000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libtp_proxy_1.1.z.so` |
| `005aee194000-005aee195000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libtp_proxy_1.1.z.so` |
| `005aee1c0000-005aee1c7000` | .so | `r--p` | 28 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libthp_proxy_1.0.z.so` |
| `005aee1c7000-005aee1cd000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libthp_proxy_1.0.z.so` |
| `005aee1cd000-005aee1d0000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libthp_proxy_1.0.z.so` |
| `005aee1d0000-005aee1d1000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libthp_proxy_1.0.z.so` |
| `005aee200000-005aee203000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libthp_extra_innerapi.z.so` |
| `005aee203000-005aee207000` | .so | `r-xp` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libthp_extra_innerapi.z.so` |
| `005aee207000-005aee208000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libthp_extra_innerapi.z.so` |
| `005aee208000-005aee209000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libthp_extra_innerapi.z.so` |
| `005aee240000-005aee24c000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libtp_proxy_1.0.z.so` |
| `005aee24c000-005aee25d000` | .so | `r-xp` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libtp_proxy_1.0.z.so` |
| `005aee25d000-005aee25f000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libtp_proxy_1.0.z.so` |
| `005aee25f000-005aee260000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libtp_proxy_1.0.z.so` |
| `005aee260000-005aee261000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libtp_proxy_1.0.z.so.bss]` |
| `005aee280000-005aee281000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhidebug.so` |
| `005aee281000-005aee282000` | .so | `r-xp` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhidebug.so` |
| `005aee282000-005aee284000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhidebug.so` |
| `005aee284000-005aee285000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhidebug.so` |
| `005aee2c0000-005aee2c4000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhdc_register.z.so` |
| `005aee2c9000-005aee2ca000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhdc_register.z.so` |
| `005aee300000-005aee308000` | .so | `r--p` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtextureEncoderCL.z.so` |
| `005aee308000-005aee30d000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtextureEncoderCL.z.so` |
| `005aee30d000-005aee30e000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtextureEncoderCL.z.so` |
| `005aee30e000-005aee30f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtextureEncoderCL.z.so` |
| `005aee30f000-005aee363000` | .ttf | `r--p` | 336 | 276 | 32 | 0 | 0 | 0.00% | `/system/fonts/HarmonyOS_Sans.ttf` |
| `005aee380000-005aee381000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhispeed_string.so` |
| `005aee383000-005aee385000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhispeed_string.so` |
| `005aee385000-005aee386000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhispeed_string.so` |
| `005aee386000-005aee3db000` | FilePage other | `r--p` | 340 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/audio_framework_taihe_abc.abc` |
| `005aee400000-005aee401000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005aee600000-005aee601000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005aee640000-005aee650000` | .so | `r--p` | 64 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librawplugin.z.so` |
| `005aee650000-005aee69d000` | .so | `r-xp` | 308 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librawplugin.z.so` |
| `005aee69d000-005aee6a0000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librawplugin.z.so` |
| `005aee6a0000-005aee6a1000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librawplugin.z.so` |
| `005aee6a1000-005aee6e5000` | FilePage other | `r--p` | 272 | 272 | 272 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNFameHall-harmony_c788251/dyrnfamehall.bundle` |
| `005aee940000-005aee94c000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libheifimpl.z.so` |
| `005aee94c000-005aee95d000` | .so | `r-xp` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libheifimpl.z.so` |
| `005aee95d000-005aee95f000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libheifimpl.z.so` |
| `005aee95f000-005aee960000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libheifimpl.z.so` |
| `005aee980000-005aee9b9000` | .so | `r--p` | 228 | 44 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextplugin.z.so` |
| `005aee9b9000-005aeea58000` | .so | `r-xp` | 636 | 132 | 22 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextplugin.z.so` |
| `005aeea58000-005aeea5c000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextplugin.z.so` |
| `005aeea5c000-005aeea5d000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextplugin.z.so` |
| `005aeea5d000-005aeea5f000` | FilePage other | `rw-p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `[anon:libextplugin.z.so.bss]` |
| `005aeea80000-005aeea8b000` | .so | `r--p` | 44 | 32 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsecurity_component_client_enhance.z.so` |
| `005aeea8b000-005aeeaa0000` | .so | `r-xp` | 84 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsecurity_component_client_enhance.z.so` |
| `005aeeaa0000-005aeeaa3000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsecurity_component_client_enhance.z.so` |
| `005aeeaa3000-005aeeaa4000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsecurity_component_client_enhance.z.so` |
| `005aeeaa4000-005aeeaef000` | FilePage other | `r--p` | 300 | 300 | 300 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNGiftHall-harmony_aaa6107/dyrngifthall.bundle` |
| `005aeeb0a000-005aeeb0b000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/arkcompiler/stub.an` |
| `005aef92f000-005aefb11000` | FilePage other | `r--p` | 1928 | 508 | 114 | 0 | 0 | 0.00% | `/system/lib64/module/arkcompiler/stub.an` |
| `005aefb11000-005af05ff000` | .so | `r--p` | 11192 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkruntime.so` |
| `005af05ff000-005af0714000` | FilePage other | `rw-p` | 1108 | 404 | 127 | 0 | 0 | 0.00% | `/system/etc/abc/framework/arkComponent.abc` |
| `005af0740000-005af0761000` | .so | `r--p` | 132 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_checkbox.z.so` |
| `005af0761000-005af07ce000` | .so | `r-xp` | 436 | 436 | 24 | 0 | 0 | 0.00% | `/system/lib64/libarkui_checkbox.z.so` |
| `005af07ce000-005af07da000` | .so | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_checkbox.z.so` |
| `005af07da000-005af07db000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_checkbox.z.so` |
| `005af07db000-005af07dd000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_checkbox.z.so.bss]` |
| `005af0800000-005af0815000` | .so | `r--p` | 84 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_rating.z.so` |
| `005af0815000-005af084c000` | .so | `r-xp` | 220 | 216 | 11 | 0 | 0 | 0.00% | `/system/lib64/libarkui_rating.z.so` |
| `005af084c000-005af0853000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_rating.z.so` |
| `005af0853000-005af0854000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_rating.z.so` |
| `005af0854000-005af0855000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_rating.z.so.bss]` |
| `005af0880000-005af0899000` | .so | `r--p` | 100 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_gauge.z.so` |
| `005af0899000-005af08ec000` | .so | `r-xp` | 332 | 328 | 18 | 0 | 0 | 0.00% | `/system/lib64/libarkui_gauge.z.so` |
| `005af08ec000-005af08f5000` | .so | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_gauge.z.so` |
| `005af08f5000-005af08f6000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_gauge.z.so` |
| `005af08f6000-005af08f7000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_gauge.z.so.bss]` |
| `005af0900000-005af090d000` | .so | `r--p` | 52 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_linearsplit.z.so` |
| `005af090d000-005af092e000` | .so | `r-xp` | 132 | 128 | 7 | 0 | 0 | 0.00% | `/system/lib64/libarkui_linearsplit.z.so` |
| `005af092e000-005af0932000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_linearsplit.z.so` |
| `005af0932000-005af0933000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_linearsplit.z.so` |
| `005af0933000-005af0934000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_linearsplit.z.so.bss]` |
| `005af0940000-005af095a000` | .so | `r--p` | 104 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_radio.z.so` |
| `005af095a000-005af099f000` | .so | `r-xp` | 276 | 272 | 15 | 0 | 0 | 0.00% | `/system/lib64/libarkui_radio.z.so` |
| `005af099f000-005af09a6000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_radio.z.so` |
| `005af09a6000-005af09a8000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_radio.z.so` |
| `005af09c0000-005af09f9000` | .so | `r--p` | 228 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_search.z.so` |
| `005af09f9000-005af0ab2000` | .so | `r-xp` | 740 | 736 | 40 | 0 | 0 | 0.00% | `/system/lib64/libarkui_search.z.so` |
| `005af0ab2000-005af0abd000` | .so | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_search.z.so` |
| `005af0abd000-005af0abe000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_search.z.so` |
| `005af0abe000-005af0ac0000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_search.z.so.bss]` |
| `005af0ac0000-005af0b2e000` | .so | `r--p` | 440 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_richeditor.z.so` |
| `005af0b2e000-005af0c74000` | .so | `r-xp` | 1304 | 1304 | 72 | 0 | 0 | 0.00% | `/system/lib64/libarkui_richeditor.z.so` |
| `005af0c74000-005af0c8f000` | .so | `r--p` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_richeditor.z.so` |
| `005af0c8f000-005af0c90000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_richeditor.z.so` |
| `005af0c90000-005af0c94000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_richeditor.z.so.bss]` |
| `005af0cc0000-005af0ceb000` | .so | `r--p` | 172 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_slider.z.so` |
| `005af0ceb000-005af0d76000` | .so | `r-xp` | 556 | 556 | 92 | 0 | 0 | 0.00% | `/system/lib64/libarkui_slider.z.so` |
| `005af0d76000-005af0d83000` | .so | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_slider.z.so` |
| `005af0d83000-005af0d84000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_slider.z.so` |
| `005af0d84000-005af0d85000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_slider.z.so.bss]` |
| `005af0dc0000-005af0ded000` | .so | `r--p` | 180 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_timepicker.z.so` |
| `005af0ded000-005af0e83000` | .so | `r-xp` | 600 | 596 | 33 | 0 | 0 | 0.00% | `/system/lib64/libarkui_timepicker.z.so` |
| `005af0e83000-005af0e92000` | .so | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_timepicker.z.so` |
| `005af0e92000-005af0e93000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_timepicker.z.so` |
| `005af0e93000-005af0e95000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_timepicker.z.so.bss]` |
| `005af0ec0000-005af0ed5000` | .so | `r--p` | 84 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_folderstack.z.so` |
| `005af0ed5000-005af0ef8000` | .so | `r-xp` | 140 | 140 | 7 | 0 | 0 | 0.00% | `/system/lib64/libarkui_folderstack.z.so` |
| `005af0ef8000-005af0f03000` | .so | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_folderstack.z.so` |
| `005af0f03000-005af0f04000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_folderstack.z.so` |
| `005af0f04000-005af0f05000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_folderstack.z.so.bss]` |
| `005af0f40000-005af0f57000` | .so | `r--p` | 92 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_stepper.z.so` |
| `005af0f57000-005af0f90000` | .so | `r-xp` | 228 | 224 | 12 | 0 | 0 | 0.00% | `/system/lib64/libarkui_stepper.z.so` |
| `005af0f90000-005af0f9b000` | .so | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_stepper.z.so` |
| `005af0f9b000-005af0f9c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_stepper.z.so` |
| `005af0fc0000-005af0fe9000` | .so | `r--p` | 164 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_indexer.z.so` |
| `005af0fe9000-005af1080000` | .so | `r-xp` | 604 | 604 | 33 | 0 | 0 | 0.00% | `/system/lib64/libarkui_indexer.z.so` |
| `005af1080000-005af108d000` | .so | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_indexer.z.so` |
| `005af108d000-005af108e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_indexer.z.so` |
| `005af108e000-005af108f000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_indexer.z.so.bss]` |
| `005af10c0000-005af10ca000` | .so | `r--p` | 40 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_symbol.z.so` |
| `005af10ca000-005af10e5000` | .so | `r-xp` | 108 | 104 | 11 | 0 | 0 | 0.00% | `/system/lib64/libarkui_symbol.z.so` |
| `005af10e5000-005af10e7000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_symbol.z.so` |
| `005af10e7000-005af10e8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_symbol.z.so` |
| `005af1100000-005af1115000` | .so | `r--p` | 84 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_sidebar.z.so` |
| `005af1115000-005af115a000` | .so | `r-xp` | 276 | 272 | 15 | 0 | 0 | 0.00% | `/system/lib64/libarkui_sidebar.z.so` |
| `005af115a000-005af115f000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_sidebar.z.so` |
| `005af115f000-005af1160000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_sidebar.z.so` |
| `005af1160000-005af1161000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_sidebar.z.so.bss]` |
| `005af1180000-005af11af000` | .so | `r--p` | 188 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_waterflow.z.so` |
| `005af11af000-005af122e000` | .so | `r-xp` | 508 | 504 | 27 | 0 | 0 | 0.00% | `/system/lib64/libarkui_waterflow.z.so` |
| `005af122e000-005af123d000` | .so | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_waterflow.z.so` |
| `005af123d000-005af123e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_waterflow.z.so` |
| `005af123e000-005af1240000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_waterflow.z.so.bss]` |
| `005af1240000-005af1260000` | .so | `r--p` | 128 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_calendarpicker.z.so` |
| `005af1260000-005af12e0000` | .so | `r-xp` | 512 | 512 | 28 | 0 | 0 | 0.00% | `/system/lib64/libarkui_calendarpicker.z.so` |
| `005af12e0000-005af12ed000` | .so | `r--p` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_calendarpicker.z.so` |
| `005af12ed000-005af12ee000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_calendarpicker.z.so` |
| `005af12ee000-005af12f0000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_calendarpicker.z.so.bss]` |
| `005af1300000-005af1343000` | .so | `r--p` | 268 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_menu.z.so` |
| `005af1343000-005af1493000` | .so | `r-xp` | 1344 | 1340 | 104 | 0 | 0 | 0.00% | `/system/lib64/libarkui_menu.z.so` |
| `005af1493000-005af14ac000` | .so | `r--p` | 100 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/libarkui_menu.z.so` |
| `005af14ac000-005af14ad000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_menu.z.so` |
| `005af14ad000-005af14b1000` | FilePage other | `rw-p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_menu.z.so.bss]` |
| `005af14c0000-005af14d6000` | .so | `r--p` | 88 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_hyperlink.z.so` |
| `005af14d6000-005af14fe000` | .so | `r-xp` | 160 | 160 | 8 | 0 | 0 | 0.00% | `/system/lib64/libarkui_hyperlink.z.so` |
| `005af14fe000-005af1507000` | .so | `r--p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_hyperlink.z.so` |
| `005af1507000-005af1508000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_hyperlink.z.so` |
| `005af1508000-005af1509000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkui_hyperlink.z.so.bss]` |
| `005af1540000-005af1553000` | .so | `r--p` | 76 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_marquee.z.so` |
| `005af1553000-005af1588000` | .so | `r-xp` | 212 | 212 | 12 | 0 | 0 | 0.00% | `/system/lib64/libarkui_marquee.z.so` |
| `005af1588000-005af158e000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_marquee.z.so` |
| `005af158e000-005af158f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkui_marquee.z.so` |
| `005af15c0000-005af15cc000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libets_environment.z.so` |
| `005af15cc000-005af15e5000` | .so | `r-xp` | 100 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libets_environment.z.so` |
| `005af15e5000-005af15e7000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libets_environment.z.so` |
| `005af15e7000-005af15e8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libets_environment.z.so` |
| `005af1600000-005af1609000` | .so | `r--p` | 36 | 36 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/libets_interop_js_napi.z.so` |
| `005af1609000-005af1625000` | .so | `r-xp` | 112 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libets_interop_js_napi.z.so` |
| `005af1625000-005af1627000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libets_interop_js_napi.z.so` |
| `005af1627000-005af1628000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libets_interop_js_napi.z.so` |
| `005af1726000-005af1728000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30002]` |
| `005af1829000-005af182b000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30003]` |
| `005af192c000-005af192e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30004]` |
| `005af1a2f000-005af1a31000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30006]` |
| `005af1a31000-005af1b32000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30006]` |
| `005af1b40000-005af1c40000` | FilePage other | `rw-p` | 1024 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Code Space]` |
| `005af1c40000-005af1d40000` | FilePage other | `rw-p` | 1024 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Compiler Space]` |
| `005af1d40000-005af1d42000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1d42000-005af1d43000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1d43000-005af1d82000` | FilePage other | `rw-p` | 252 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1d82000-005af1d83000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1d83000-005af1dc2000` | FilePage other | `rw-p` | 252 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1dc2000-005af1dc3000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1dc3000-005af1e02000` | FilePage other | `rw-p` | 252 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1e02000-005af1e03000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1e03000-005af1f80000` | FilePage other | `rw-p` | 1524 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Native Stacks Space]` |
| `005af1f80000-005af4f80000` | FilePage other | `rw-p` | 49152 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Frames Space]` |
| `005af4f80000-005af4fc0000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Internal Space]` |
| `005af4fc0000-005af7fc0000` | FilePage other | `rw-p` | 49152 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Frames Space]` |
| `005af7fc0000-005af8000000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[anon:ArkTs Static Internal Space]` |
| `005af8103000-005af8105000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30008]` |
| `005af8706000-005af8906000` | FilePage other | `rw-p` | 2048 | 44 | 44 | 0 | 0 | 0.00% | `[anon:ffrt_coroutine_stack]` |
| `005af8a40000-005af8a46000` | .so | `r--p` | 24 | 20 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcj_environment.z.so` |
| `005af8a46000-005af8a50000` | .so | `r-xp` | 40 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcj_environment.z.so` |
| `005af8a50000-005af8a51000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcj_environment.z.so` |
| `005af8a51000-005af8a52000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcj_environment.z.so` |
| `005af8a52000-005af8a54000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30011]` |
| `005af8b80000-005af8b97000` | .so | `r--p` | 92 | 72 | 7 | 0 | 0 | 0.00% | `/system/lib64/nativestartuptask/liboh_wrapper.z.so` |
| `005af8b97000-005af8bba000` | .so | `r-xp` | 140 | 40 | 1 | 0 | 0 | 0.00% | `/system/lib64/nativestartuptask/liboh_wrapper.z.so` |
| `005af8bba000-005af8bc0000` | .so | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/nativestartuptask/liboh_wrapper.z.so` |
| `005af8bc0000-005af8bc1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/nativestartuptask/liboh_wrapper.z.so` |
| `005af8bc1000-005af8bc2000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:liboh_wrapper.z.so.bss]` |
| `005af8bc2000-005af8bc4000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30012]` |
| `005af8bc4000-005af8cc5000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30012]` |
| `005af8cc5000-005af8cc7000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30013]` |
| `005af8cc7000-005af8dc8000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30013]` |
| `005af8dc8000-005af8dca000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30014]` |
| `005af8dca000-005af8ecb000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30014]` |
| `005af8ecb000-005af8ecd000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30015]` |
| `005af8ecd000-005af8fce000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30015]` |
| `005af8fce000-005af8fd0000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30016]` |
| `005af8fd0000-005af90d1000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30016]` |
| `005af90d1000-005af90d3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30018]` |
| `005af90d3000-005af91d4000` | FilePage other | `rw-p` | 1028 | 24 | 24 | 0 | 0 | 0.00% | `[anon:stack:30018]` |
| `005af91d4000-005af91d6000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30020]` |
| `005af9300000-005af9302000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/liblayered_parameters_manager.z.so` |
| `005af9302000-005af9305000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/liblayered_parameters_manager.z.so` |
| `005af9305000-005af9306000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/liblayered_parameters_manager.z.so` |
| `005af9306000-005af9307000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/liblayered_parameters_manager.z.so` |
| `005af9340000-005af9351000` | .so | `r--p` | 68 | 40 | 3 | 0 | 0 | 0.00% | `/system/lib64/libbundle_ndk.z.so` |
| `005af9351000-005af9371000` | .so | `r-xp` | 128 | 96 | 3 | 0 | 0 | 0.00% | `/system/lib64/libbundle_ndk.z.so` |
| `005af9371000-005af9373000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libbundle_ndk.z.so` |
| `005af9373000-005af9374000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libbundle_ndk.z.so` |
| `005af9374000-005af9376000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30635]` |
| `005af9477000-005af9479000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30022]` |
| `005af9479000-005af957a000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30022]` |
| `005af957a000-005af957c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30023]` |
| `005af9780000-005af9781000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartupconfigentry_napi.z.so` |
| `005af9781000-005af9784000` | .so | `r-xp` | 12 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartupconfigentry_napi.z.so` |
| `005af9784000-005af9785000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartupconfigentry_napi.z.so` |
| `005af9785000-005af9786000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartupconfigentry_napi.z.so` |
| `005af97c0000-005af97c1000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartuptask_napi.z.so` |
| `005af97c1000-005af97c4000` | .so | `r-xp` | 12 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartuptask_napi.z.so` |
| `005af97c4000-005af97c5000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartuptask_napi.z.so` |
| `005af97c5000-005af97c6000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartuptask_napi.z.so` |
| `005af9800000-005af9846000` | .so | `r--p` | 280 | 172 | 172 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmmkv.so` |
| `005af9846000-005af98ba000` | .so | `r-xp` | 464 | 168 | 168 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmmkv.so` |
| `005af98ba000-005af98c2000` | .so | `r--p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmmkv.so` |
| `005af98c2000-005af98c3000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmmkv.so` |
| `005af98c3000-005af98c4000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libmmkv.so.bss]` |
| `005af9900000-005af9901000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/events/libemitter.z.so` |
| `005af9901000-005af9904000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/events/libemitter.z.so` |
| `005af9904000-005af9905000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/events/libemitter.z.so` |
| `005af9905000-005af9906000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/events/libemitter.z.so` |
| `005af9940000-005af9945000` | .so | `r--p` | 20 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libemitter_interops.z.so` |
| `005af9945000-005af9951000` | .so | `r-xp` | 48 | 40 | 5 | 0 | 0 | 0.00% | `/system/lib64/libemitter_interops.z.so` |
| `005af9951000-005af9953000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libemitter_interops.z.so` |
| `005af9953000-005af9954000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libemitter_interops.z.so` |
| `005af9980000-005af998e000` | .so | `r--p` | 56 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libobserver.z.so` |
| `005af998e000-005af99da000` | .so | `r-xp` | 304 | 128 | 24 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libobserver.z.so` |
| `005af99da000-005af99dd000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libobserver.z.so` |
| `005af99dd000-005af99de000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libobserver.z.so` |
| `005af99de000-005af99df000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libobserver.z.so.bss]` |
| `005af9a00000-005af9a08000` | .so | `r--p` | 32 | 20 | 6 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libcomponentsnapshot.z.so` |
| `005af9a08000-005af9a22000` | .so | `r-xp` | 104 | 52 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libcomponentsnapshot.z.so` |
| `005af9a22000-005af9a25000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libcomponentsnapshot.z.so` |
| `005af9a25000-005af9a26000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libcomponentsnapshot.z.so` |
| `005af9a40000-005af9a45000` | .so | `r--p` | 20 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/atomicservice/libnavpushpathhelper.z.so` |
| `005af9a45000-005af9a4d000` | .so | `r-xp` | 32 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/module/atomicservice/libnavpushpathhelper.z.so` |
| `005af9a4d000-005af9a4f000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/atomicservice/libnavpushpathhelper.z.so` |
| `005af9a4f000-005af9a52000` | .so | `rw-p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/atomicservice/libnavpushpathhelper.z.so` |
| `005af9a80000-005af9a97000` | .so | `r--p` | 92 | 52 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/libtaskpool.z.so` |
| `005af9a97000-005af9ada000` | .so | `r-xp` | 268 | 200 | 25 | 0 | 0 | 0.00% | `/system/lib64/module/libtaskpool.z.so` |
| `005af9ada000-005af9add000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/libtaskpool.z.so` |
| `005af9add000-005af9ade000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libtaskpool.z.so` |
| `005af9ade000-005af9adf000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libtaskpool.z.so.bss]` |
| `005af9adf000-005af9ae1000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30024]` |
| `005af9ae1000-005afa2e2000` | FilePage other | `rw-p` | 8196 | 64 | 64 | 0 | 0 | 0.00% | `[anon:stack:30024]` |
| `005afa2e2000-005afa2e4000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30025]` |
| `005afa2e4000-005afa3e5000` | FilePage other | `rw-p` | 1028 | 28 | 28 | 0 | 0 | 0.00% | `[anon:stack:30025]` |
| `005afa400000-005afa402000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtask_signal_native.z.so` |
| `005afa402000-005afa405000` | .so | `r-xp` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtask_signal_native.z.so` |
| `005afa405000-005afa406000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtask_signal_native.z.so` |
| `005afa406000-005afa407000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtask_signal_native.z.so` |
| `005afa440000-005afa478000` | .so | `r--p` | 224 | 64 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/file/libfs.z.so` |
| `005afa478000-005afa59d000` | .so | `r-xp` | 1172 | 964 | 43 | 0 | 0 | 0.00% | `/system/lib64/module/file/libfs.z.so` |
| `005afa59d000-005afa5af000` | .so | `r--p` | 72 | 72 | 72 | 0 | 0 | 0.00% | `/system/lib64/module/file/libfs.z.so` |
| `005afa5af000-005afa5b0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/file/libfs.z.so` |
| `005afa5b0000-005afa5b3000` | FilePage other | `rw-p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `[anon:libfs.z.so.bss]` |
| `005afa5c0000-005afa5c6000` | .so | `r--p` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librust_file.z.so` |
| `005afa5c6000-005afa5cf000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librust_file.z.so` |
| `005afa5cf000-005afa5d0000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librust_file.z.so` |
| `005afa5d0000-005afa5d1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librust_file.z.so` |
| `005afa5d1000-005afa5d2000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:librust_file.z.so.bss]` |
| `005afb600000-005afb60c000` | .so | `r--p` | 48 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstack_utils_common.z.so` |
| `005afb60c000-005afb62c000` | .so | `r-xp` | 128 | 108 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstack_utils_common.z.so` |
| `005afb62c000-005afb62e000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstack_utils_common.z.so` |
| `005afb62e000-005afb62f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libstack_utils_common.z.so` |
| `005afb640000-005afb65e000` | .so | `r--p` | 120 | 68 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/net/libhttp.z.so` |
| `005afb700000-005afb727000` | .so | `r--p` | 156 | 96 | 96 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmakeurl.so` |
| `005afb727000-005afb783000` | .so | `r-xp` | 368 | 244 | 244 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmakeurl.so` |
| `005afb783000-005afb786000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmakeurl.so` |
| `005afb786000-005afb787000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmakeurl.so` |
| `005afb787000-005afb788000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libmakeurl.so.bss]` |
| `005afb7c0000-005afb7c2000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libdeviceinfo_ndk.z.so` |
| `005afb7c2000-005afb7c3000` | .so | `r-xp` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libdeviceinfo_ndk.z.so` |
| `005afb7c3000-005afb7c5000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libdeviceinfo_ndk.z.so` |
| `005afb7c5000-005afb7c6000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libdeviceinfo_ndk.z.so` |
| `005afb800000-005afb891000` | .so | `r--p` | 580 | 324 | 324 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libc++_shared.so` |
| `005afb940000-005afb959000` | .so | `r--p` | 100 | 48 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/bundle/libbundlemanager.z.so` |
| `005afb959000-005afb9a2000` | .so | `r-xp` | 292 | 112 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/bundle/libbundlemanager.z.so` |
| `005afb9a2000-005afb9a4000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/bundle/libbundlemanager.z.so` |
| `005afb9a4000-005afb9a5000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/bundle/libbundlemanager.z.so` |
| `005afb9c0000-005afb9cc000` | .so | `r--p` | 48 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/libbundle_manager_common.z.so` |
| `005afb9cc000-005afb9e2000` | .so | `r-xp` | 88 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libbundle_manager_common.z.so` |
| `005afb9e2000-005afb9e4000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libbundle_manager_common.z.so` |
| `005afb9e4000-005afb9e5000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libbundle_manager_common.z.so` |
| `005afba00000-005afba05000` | .so | `r--p` | 20 | 12 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/security/libasset_napi.z.so` |
| `005afba05000-005afba16000` | .so | `r-xp` | 68 | 60 | 15 | 0 | 0 | 0.00% | `/system/lib64/module/security/libasset_napi.z.so` |
| `005afba16000-005afba19000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/security/libasset_napi.z.so` |
| `005afba19000-005afba1a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/security/libasset_napi.z.so` |
| `005afba40000-005afba41000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk.z.so` |
| `005afba41000-005afba44000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk.z.so` |
| `005afba44000-005afba45000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk.z.so` |
| `005afba45000-005afba46000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk.z.so` |
| `005afba80000-005afba85000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk_ffi.z.so` |
| `005afba85000-005afba8f000` | .so | `r-xp` | 40 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk_ffi.z.so` |
| `005afba8f000-005afba90000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk_ffi.z.so` |
| `005afba90000-005afba91000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk_ffi.z.so` |
| `005afba91000-005afba92000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libasset_sdk_ffi.z.so.bss]` |
| `005afbac0000-005afbacd000` | .so | `r--p` | 52 | 32 | 2 | 0 | 0 | 0.00% | `/system/lib64/libsamgr.dylib.so` |
| `005afbacd000-005afbadd000` | .so | `r-xp` | 64 | 32 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsamgr.dylib.so` |
| `005afbadd000-005afbae2000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/libsamgr.dylib.so` |
| `005afbae2000-005afbae3000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsamgr.dylib.so` |
| `005afbb00000-005afbb15000` | .so | `r--p` | 84 | 52 | 2 | 0 | 0 | 0.00% | `/system/lib64/libipc.dylib.so` |
| `005afbb15000-005afbb29000` | .so | `r-xp` | 80 | 56 | 3 | 0 | 0 | 0.00% | `/system/lib64/libipc.dylib.so` |
| `005afbb29000-005afbb2b000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libipc.dylib.so` |
| `005afbb2b000-005afbb2c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libipc.dylib.so` |
| `005afbb2c000-005afbb2d000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libipc.dylib.so.bss]` |
| `005afbb40000-005afbb4d000` | .so | `r--p` | 52 | 40 | 1 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk.dylib.so` |
| `005afbb4d000-005afbb5f000` | .so | `r-xp` | 72 | 40 | 3 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk.dylib.so` |
| `005afbb5f000-005afbb62000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk.dylib.so` |
| `005afbb62000-005afbb63000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libasset_sdk.dylib.so` |
| `005afbb80000-005afbb98000` | .so | `r--p` | 96 | 48 | 2 | 0 | 0 | 0.00% | `/system/lib64/libutils_rust.dylib.so` |
| `005afbb98000-005afbbac000` | .so | `r-xp` | 80 | 20 | 3 | 0 | 0 | 0.00% | `/system/lib64/libutils_rust.dylib.so` |
| `005afbbac000-005afbbad000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libutils_rust.dylib.so` |
| `005afbbad000-005afbbae000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libutils_rust.dylib.so` |
| `005afbbae000-005afbbaf000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libutils_rust.dylib.so.bss]` |
| `005afbbc0000-005afbbcc000` | .so | `r--p` | 48 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/libpromptaction.z.so` |
| `005afbbcc000-005afbc01000` | .so | `r-xp` | 212 | 76 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/libpromptaction.z.so` |
| `005afbc01000-005afbc03000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/libpromptaction.z.so` |
| `005afbc03000-005afbc07000` | .so | `rw-p` | 16 | 16 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/libpromptaction.z.so` |
| `005afbc40000-005afbc4b000` | .so | `r--p` | 44 | 24 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libwantagent_napi.z.so` |
| `005afbc4b000-005afbc57000` | .so | `r-xp` | 48 | 48 | 15 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libwantagent_napi.z.so` |
| `005afbc57000-005afbc59000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libwantagent_napi.z.so` |
| `005afbc59000-005afbc5a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libwantagent_napi.z.so` |
| `005afbc80000-005afbc87000` | .so | `r--p` | 28 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_manager_sdk.z.so` |
| `005afbc87000-005afbc96000` | .so | `r-xp` | 60 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_manager_sdk.z.so` |
| `005afbc96000-005afbc98000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_manager_sdk.z.so` |
| `005afbc98000-005afbc99000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_manager_sdk.z.so` |
| `005afbcc0000-005afbccb000` | .so | `r--p` | 44 | 32 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/libfileshare.z.so` |
| `005afbccb000-005afbcf3000` | .so | `r-xp` | 160 | 112 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/libfileshare.z.so` |
| `005afbcf3000-005afbcf7000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/libfileshare.z.so` |
| `005afbcf7000-005afbcf8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libfileshare.z.so` |
| `005afbcf8000-005afbcf9000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libfileshare.z.so.bss]` |
| `005afbd00000-005afbd06000` | .so | `r--p` | 24 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_manager_communication_adapter_cxx.z.so` |
| `005afbd06000-005afbd10000` | .so | `r-xp` | 40 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_manager_communication_adapter_cxx.z.so` |
| `005afbd10000-005afbd12000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_manager_communication_adapter_cxx.z.so` |
| `005afbd12000-005afbd13000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsandbox_manager_communication_adapter_cxx.z.so` |
| `005afbd40000-005afbd49000` | .so | `r--p` | 36 | 24 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/data/libuniformtypedescriptor_napi.z.so` |
| `005afbd49000-005afbd61000` | .so | `r-xp` | 96 | 52 | 6 | 0 | 0 | 0.00% | `/system/lib64/module/data/libuniformtypedescriptor_napi.z.so` |
| `005afbd61000-005afbd63000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/data/libuniformtypedescriptor_napi.z.so` |
| `005afbd63000-005afbd64000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/data/libuniformtypedescriptor_napi.z.so` |
| `005afbd80000-005afbd81000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/filemanagement/libfilepreview_napi.z.so` |
| `005afbd81000-005afbd82000` | .so | `r-xp` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/filemanagement/libfilepreview_napi.z.so` |
| `005afbd82000-005afbd83000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/filemanagement/libfilepreview_napi.z.so` |
| `005afbd83000-005afbd91000` | .so | `rw-p` | 56 | 36 | 13 | 0 | 0 | 0.00% | `/system/lib64/module/hms/filemanagement/libfilepreview_napi.z.so` |
| `005afbdc0000-005afbdc3000` | .so | `r--p` | 12 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libdialogrequest_napi.z.so` |
| `005afbdc3000-005afbdc6000` | .so | `r-xp` | 12 | 12 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libdialogrequest_napi.z.so` |
| `005afbdc6000-005afbdc7000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libdialogrequest_napi.z.so` |
| `005afbdc7000-005afbdc8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libdialogrequest_napi.z.so` |
| `005afbe00000-005afbe02000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libsystemparameterenhance.z.so` |
| `005afbe02000-005afbe04000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libsystemparameterenhance.z.so` |
| `005afbe04000-005afbe06000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/libsystemparameterenhance.z.so` |
| `005afbe06000-005afbe07000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libsystemparameterenhance.z.so` |
| `005afbe40000-005afbe42000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libwantconstant_napi.z.so` |
| `005afbe42000-005afbe46000` | .so | `r-xp` | 16 | 16 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libwantconstant_napi.z.so` |
| `005afbe46000-005afbe47000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libwantconstant_napi.z.so` |
| `005afbe47000-005afbe48000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libwantconstant_napi.z.so` |
| `005afbe80000-005afbe9b000` | .so | `r--p` | 108 | 44 | 14 | 0 | 0 | 0.00% | `/system/lib64/module/useriam/libuserauth.z.so` |
| `005afbe9b000-005afbeef000` | .so | `r-xp` | 336 | 108 | 22 | 0 | 0 | 0.00% | `/system/lib64/module/useriam/libuserauth.z.so` |
| `005afbeef000-005afbef3000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/useriam/libuserauth.z.so` |
| `005afbef3000-005afbef4000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/useriam/libuserauth.z.so` |
| `005afbef4000-005afbef5000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libuserauth.z.so.bss]` |
| `005afbf00000-005afbf08000` | .so | `r--p` | 32 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/liblbsbase_module.z.so` |
| `005afbf08000-005afbf15000` | .so | `r-xp` | 52 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/liblbsbase_module.z.so` |
| `005afbf15000-005afbf19000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/liblbsbase_module.z.so` |
| `005afbf19000-005afbf1a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/liblbsbase_module.z.so` |
| `005afbf40000-005afbf48000` | .so | `r--p` | 32 | 24 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libgeofence_sdk.z.so` |
| `005afbf48000-005afbf55000` | .so | `r-xp` | 52 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libgeofence_sdk.z.so` |
| `005afbf55000-005afbf57000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libgeofence_sdk.z.so` |
| `005afbf57000-005afbf58000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libgeofence_sdk.z.so` |
| `005afbf80000-005afbf90000` | .so | `r--p` | 64 | 48 | 2 | 0 | 0 | 0.00% | `/system/lib64/liblocator_interface_proxy.z.so` |
| `005afbf90000-005afbfb6000` | .so | `r-xp` | 152 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/liblocator_interface_proxy.z.so` |
| `005afbfb6000-005afbfb9000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/liblocator_interface_proxy.z.so` |
| `005afbfb9000-005afbfba000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/liblocator_interface_proxy.z.so` |
| `005afbfba000-005afbfbb000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:liblocator_interface_proxy.z.so.bss]` |
| `005afbfc0000-005afbfe3000` | .so | `r--p` | 140 | 80 | 20 | 0 | 0 | 0.00% | `/system/lib64/module/libgeolocationmanager.z.so` |
| `005afbfe3000-005afc04f000` | .so | `r-xp` | 432 | 100 | 23 | 0 | 0 | 0.00% | `/system/lib64/module/libgeolocationmanager.z.so` |
| `005afc04f000-005afc05c000` | .so | `r--p` | 52 | 52 | 52 | 0 | 0 | 0.00% | `/system/lib64/module/libgeolocationmanager.z.so` |
| `005afc05c000-005afc05d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libgeolocationmanager.z.so` |
| `005afc05d000-005afc05f000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libgeolocationmanager.z.so.bss]` |
| `005afc080000-005afc0a2000` | .so | `r--p` | 136 | 88 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblbsservice_common.z.so` |
| `005afc0a2000-005afc0df000` | .so | `r-xp` | 244 | 80 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblbsservice_common.z.so` |
| `005afc0df000-005afc0e4000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblbsservice_common.z.so` |
| `005afc0e4000-005afc0e5000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblbsservice_common.z.so` |
| `005afc0e5000-005afc0e7000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:liblbsservice_common.z.so.bss]` |
| `005afc100000-005afc114000` | .so | `r--p` | 80 | 52 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblocator_sdk.z.so` |
| `005afc114000-005afc134000` | .so | `r-xp` | 128 | 52 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblocator_sdk.z.so` |
| `005afc134000-005afc13c000` | .so | `r--p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblocator_sdk.z.so` |
| `005afc13c000-005afc13d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liblocator_sdk.z.so` |
| `005afc13d000-005afc13e000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:liblocator_sdk.z.so.bss]` |
| `005afc140000-005afc149000` | .so | `r--p` | 36 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/liberrormanager.z.so` |
| `005afc149000-005afc155000` | .so | `r-xp` | 48 | 44 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/liberrormanager.z.so` |
| `005afc155000-005afc157000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/liberrormanager.z.so` |
| `005afc157000-005afc158000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/liberrormanager.z.so` |
| `005afc180000-005afc182000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libapprecovery_napi.z.so` |
| `005afc182000-005afc185000` | .so | `r-xp` | 12 | 12 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libapprecovery_napi.z.so` |
| `005afc185000-005afc186000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libapprecovery_napi.z.so` |
| `005afc186000-005afc187000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libapprecovery_napi.z.so` |
| `005afc1c0000-005afc1f4000` | .so | `r--p` | 208 | 156 | 8 | 0 | 0 | 0.00% | `/system/lib64/libconnection_if.z.so` |
| `005afc1f4000-005afc226000` | .so | `r-xp` | 200 | 96 | 6 | 0 | 0 | 0.00% | `/system/lib64/libconnection_if.z.so` |
| `005afc226000-005afc22c000` | .so | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/libconnection_if.z.so` |
| `005afc22c000-005afc22d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libconnection_if.z.so` |
| `005afc240000-005afc249000` | .so | `r--p` | 36 | 32 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnet_connection.so` |
| `005afc249000-005afc255000` | .so | `r-xp` | 48 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnet_connection.so` |
| `005afc255000-005afc257000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnet_connection.so` |
| `005afc257000-005afc258000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnet_connection.so` |
| `005afc280000-005afc28f000` | .so | `r--p` | 60 | 44 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/net/libconnection.z.so` |
| `005afc28f000-005afc2aa000` | .so | `r-xp` | 108 | 40 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/net/libconnection.z.so` |
| `005afc2aa000-005afc2ad000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/net/libconnection.z.so` |
| `005afc2ad000-005afc2ae000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/net/libconnection.z.so` |
| `005afc2c0000-005afc2e6000` | .so | `r--p` | 152 | 72 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwifi_sdk.z.so` |
| `005afc2e6000-005afc341000` | .so | `r-xp` | 364 | 88 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwifi_sdk.z.so` |
| `005afc341000-005afc34c000` | .so | `r--p` | 44 | 44 | 44 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwifi_sdk.z.so` |
| `005afc34c000-005afc34d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwifi_sdk.z.so` |
| `005afc34d000-005afc34e000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libwifi_sdk.z.so.bss]` |
| `005afc380000-005afc390000` | .so | `r--p` | 64 | 64 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwifi_utils.z.so` |
| `005afc390000-005afc3b9000` | .so | `r-xp` | 164 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwifi_utils.z.so` |
| `005afc3b9000-005afc3bd000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwifi_utils.z.so` |
| `005afc3bd000-005afc3be000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwifi_utils.z.so` |
| `005afc3be000-005afc3bf000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libwifi_utils.z.so.bss]` |
| `005afc3c0000-005afc3cc000` | .so | `r--p` | 48 | 40 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/libwifimanager.z.so` |
| `005afc3cc000-005afc3fb000` | .so | `r-xp` | 188 | 76 | 10 | 0 | 0 | 0.00% | `/system/lib64/module/libwifimanager.z.so` |
| `005afc3fb000-005afc403000` | .so | `r--p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/system/lib64/module/libwifimanager.z.so` |
| `005afc403000-005afc404000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libwifimanager.z.so` |
| `005afc404000-005afc405000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libwifimanager.z.so.bss]` |
| `005afc405000-005afc407000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30026]` |
| `005afc407000-005afcc08000` | FilePage other | `rw-p` | 8196 | 56 | 56 | 0 | 0 | 0.00% | `[anon:stack:30026]` |
| `005afcc40000-005afcc4f000` | .so | `r--p` | 60 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmarsxlog.so` |
| `005afcc4f000-005afccba000` | .so | `r-xp` | 428 | 92 | 92 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmarsxlog.so` |
| `005afccba000-005afccbc000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmarsxlog.so` |
| `005afccbc000-005afccbd000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libmarsxlog.so` |
| `005afccbd000-005afccbe000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libmarsxlog.so.bss]` |
| `005afccc0000-005afccd6000` | .so | `r--p` | 88 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/librcp.z.so` |
| `005afccd6000-005afcd09000` | .so | `r-xp` | 204 | 72 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/librcp.z.so` |
| `005afcd09000-005afcd0e000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/librcp.z.so` |
| `005afcd0e000-005afcd3c000` | .so | `rw-p` | 184 | 88 | 13 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/librcp.z.so` |
| `005afcd40000-005afcd50000` | .so | `r--p` | 64 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/libha_app_event.z.so` |
| `005afcd50000-005afcd8e000` | .so | `r-xp` | 248 | 164 | 10 | 0 | 0 | 0.00% | `/system/lib64/libha_app_event.z.so` |
| `005afcd8e000-005afcd91000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/libha_app_event.z.so` |
| `005afcd91000-005afcd92000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libha_app_event.z.so` |
| `005afcd92000-005afcd94000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libha_app_event.z.so.bss]` |
| `005afce97000-005afce99000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30344]` |
| `005afce99000-005afcf9a000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30344]` |
| `005afcfc0000-005afcfea000` | .so | `r--p` | 168 | 56 | 17 | 0 | 0 | 0.00% | `/system/lib64/module/net/libsocket.z.so` |
| `005afcfea000-005afd0ce000` | .so | `r-xp` | 912 | 112 | 29 | 0 | 0 | 0.00% | `/system/lib64/module/net/libsocket.z.so` |
| `005afd0ce000-005afd0d5000` | .so | `r--p` | 28 | 28 | 28 | 0 | 0 | 0.00% | `/system/lib64/module/net/libsocket.z.so` |
| `005afd0d5000-005afd0d7000` | .so | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/net/libsocket.z.so` |
| `005afd100000-005afd110000` | .so | `r--p` | 64 | 64 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/libharmonyshare_napi.z.so` |
| `005afd110000-005afd149000` | .so | `r-xp` | 228 | 204 | 25 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/libharmonyshare_napi.z.so` |
| `005afd149000-005afd151000` | .so | `r--p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/libharmonyshare_napi.z.so` |
| `005afd151000-005afd152000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/libharmonyshare_napi.z.so` |
| `005afd152000-005afd161000` | FilePage other | `rw-p` | 60 | 60 | 60 | 0 | 0 | 0.00% | `[anon:libharmonyshare_napi.z.so.bss]` |
| `005afd180000-005afd18d000` | .so | `r--p` | 52 | 48 | 12 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_channel.z.so` |
| `005afd18d000-005afd1a0000` | .so | `r-xp` | 76 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_channel.z.so` |
| `005afd1a0000-005afd1a5000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_channel.z.so` |
| `005afd1a5000-005afd1a6000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_channel.z.so` |
| `005afd1c0000-005afd1d0000` | .so | `r--p` | 64 | 64 | 8 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_jskits.z.so` |
| `005afd1d0000-005afd1fb000` | .so | `r-xp` | 172 | 108 | 14 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_jskits.z.so` |
| `005afd1fb000-005afd1ff000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_jskits.z.so` |
| `005afd1ff000-005afd200000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_jskits.z.so` |
| `005afd200000-005afd201000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libsystemshare_jskits.z.so.bss]` |
| `005afd240000-005afd249000` | .so | `r--p` | 36 | 36 | 9 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_base.z.so` |
| `005afd249000-005afd25c000` | .so | `r-xp` | 76 | 40 | 3 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_base.z.so` |
| `005afd25c000-005afd25d000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_base.z.so` |
| `005afd25d000-005afd25e000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_base.z.so` |
| `005afd25e000-005afd25f000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libsystemshare_base.z.so.bss]` |
| `005afd280000-005afd28d000` | .so | `r--p` | 52 | 48 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_innerkits.z.so` |
| `005afd28d000-005afd2a4000` | .so | `r-xp` | 92 | 40 | 3 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_innerkits.z.so` |
| `005afd2a4000-005afd2a7000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_innerkits.z.so` |
| `005afd2a7000-005afd2a8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsystemshare_innerkits.z.so` |
| `005afd2c0000-005afd2d6000` | .so | `r--p` | 88 | 76 | 9 | 0 | 0 | 0.00% | `/system/lib64/libshare_client.z.so` |
| `005afd2d6000-005afd30f000` | .so | `r-xp` | 228 | 224 | 30 | 0 | 0 | 0.00% | `/system/lib64/libshare_client.z.so` |
| `005afd30f000-005afd315000` | .so | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/libshare_client.z.so` |
| `005afd315000-005afd316000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libshare_client.z.so` |
| `005afd316000-005afd322000` | FilePage other | `rw-p` | 48 | 48 | 48 | 0 | 0 | 0.00% | `[anon:libshare_client.z.so.bss]` |
| `005afd340000-005afd341000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/libsystemshare.z.so` |
| `005afd341000-005afd343000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/libsystemshare.z.so` |
| `005afd343000-005afd344000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/libsystemshare.z.so` |
| `005afd344000-005afd345000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/collaboration/libsystemshare.z.so` |
| `005afd380000-005afd38d000` | .so | `r--p` | 52 | 40 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/arkts/libutils.z.so` |
| `005afd38d000-005afd39f000` | .so | `r-xp` | 72 | 60 | 6 | 0 | 0 | 0.00% | `/system/lib64/module/arkts/libutils.z.so` |
| `005afd39f000-005afd3a1000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/arkts/libutils.z.so` |
| `005afd3a1000-005afd3a6000` | .so | `rw-p` | 20 | 16 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/arkts/libutils.z.so` |
| `005afd3c0000-005afd3c3000` | .so | `r--p` | 12 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avsource.so` |
| `005afd3c3000-005afd3c6000` | .so | `r-xp` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avsource.so` |
| `005afd3c6000-005afd3c8000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avsource.so` |
| `005afd3c8000-005afd3c9000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avsource.so` |
| `005afd400000-005afd402000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libavcodec_hiappevent.so` |
| `005afd402000-005afd406000` | .so | `r-xp` | 16 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libavcodec_hiappevent.so` |
| `005afd406000-005afd407000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libavcodec_hiappevent.so` |
| `005afd407000-005afd408000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libavcodec_hiappevent.so` |
| `005afd459000-005afd45a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_core.so` |
| `005afd480000-005afd499000` | .so | `r--p` | 100 | 76 | 36 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohavsession.so` |
| `005afd499000-005afd4ba000` | .so | `r-xp` | 132 | 44 | 34 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohavsession.so` |
| `005afd4ba000-005afd4bc000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohavsession.so` |
| `005afd4bc000-005afd4bd000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohavsession.so` |
| `005afd4cd000-005afd4ce000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libnative_media_vdec.so.bss]` |
| `005afd500000-005afd502000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpixelmap_ndk.z.so` |
| `005afd502000-005afd506000` | .so | `r-xp` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpixelmap_ndk.z.so` |
| `005afd506000-005afd507000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpixelmap_ndk.z.so` |
| `005afd507000-005afd508000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpixelmap_ndk.z.so` |
| `005afd540000-005afd544000` | .so | `r--p` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_media_acodec.so` |
| `005afd544000-005afd549000` | .so | `r-xp` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_media_acodec.so` |
| `005afd549000-005afd54b000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_media_acodec.so` |
| `005afd54b000-005afd54c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_media_acodec.so` |
| `005afd868000-005afd869000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libdyplayer.so` |
| `005afe480000-005afe4a1000` | .so | `r--p` | 132 | 100 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohaudio.so` |
| `005afe500000-005afe530000` | .so | `r--p` | 192 | 124 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_drawing_ndk.z.so` |
| `005afe530000-005afe579000` | .so | `r-xp` | 292 | 60 | 2 | 0 | 0 | 0.00% | `/system/lib64/libnative_drawing_ndk.z.so` |
| `005afe579000-005afe57c000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/libnative_drawing_ndk.z.so` |
| `005afe57c000-005afe57d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_drawing_ndk.z.so` |
| `005afe57d000-005afe57e000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libnative_drawing_ndk.z.so.bss]` |
| `005afe580000-005afe5cd000` | .so | `r--p` | 308 | 140 | 8 | 0 | 0 | 0.00% | `/system/lib64/libace_ndk.z.so` |
| `005afe695000-005afe69b000` | .so | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/libace_ndk.z.so` |
| `005afe69b000-005afe69c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libace_ndk.z.so` |
| `005afe69c000-005afe69e000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libace_ndk.z.so.bss]` |
| `005afe6c0000-005afe6c4000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_venc.so` |
| `005afe6c4000-005afe6cc000` | .so | `r-xp` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_venc.so` |
| `005afe6cc000-005afe6cd000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_venc.so` |
| `005afe6cd000-005afe6ce000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_venc.so` |
| `005afe700000-005afe708000` | .so | `r--p` | 32 | 28 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_codecbase.so` |
| `005afe708000-005afe70f000` | .so | `r-xp` | 28 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_codecbase.so` |
| `005afe70f000-005afe711000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_codecbase.so` |
| `005afe711000-005afe712000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_codecbase.so` |
| `005afe712000-005afe714000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnative_media_codecbase.so.bss]` |
| `005afe740000-005afe743000` | .so | `r--p` | 12 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avdemuxer.so` |
| `005afe743000-005afe746000` | .so | `r-xp` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avdemuxer.so` |
| `005afe746000-005afe747000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avdemuxer.so` |
| `005afe747000-005afe748000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avdemuxer.so` |
| `005afe780000-005afe786000` | .so | `r--p` | 24 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avmuxer.so` |
| `005afe786000-005afe79a000` | .so | `r-xp` | 80 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avmuxer.so` |
| `005afe79a000-005afe79b000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avmuxer.so` |
| `005afe79b000-005afe79d000` | .so | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libnative_media_avmuxer.so` |
| `005afe7c0000-005afe7d4000` | .so | `r--p` | 80 | 36 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libappmanager.z.so` |
| `005afe7d4000-005afe7ea000` | .so | `r-xp` | 88 | 64 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libappmanager.z.so` |
| `005afe7ea000-005afe7ef000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libappmanager.z.so` |
| `005afe7ef000-005afe7f0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libappmanager.z.so` |
| `005afe7f0000-005afe7f1000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libappmanager.z.so.bss]` |
| `005afe800000-005afe806000` | GL | `r--p` | 24 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglynative.so` |
| `005afe806000-005afe80e000` | GL | `r-xp` | 32 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglynative.so` |
| `005afe80e000-005afe80f000` | GL | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglynative.so` |
| `005afe80f000-005afe810000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglynative.so` |
| `005afe810000-005afe813000` | GL | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libbuglynative.so.bss]` |
| `005afe840000-005afe845000` | Graph | `r--p` | 20 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/graphics/libdisplaysync.z.so` |
| `005afe845000-005afe853000` | Graph | `r-xp` | 56 | 56 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/graphics/libdisplaysync.z.so` |
| `005afe853000-005afe855000` | Graph | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/graphics/libdisplaysync.z.so` |
| `005afe855000-005afe856000` | Graph | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/graphics/libdisplaysync.z.so` |
| `005afe880000-005afe8aa000` | GL | `r--p` | 168 | 120 | 120 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglyxlog.so` |
| `005afe8aa000-005afe930000` | GL | `r-xp` | 536 | 44 | 44 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglyxlog.so` |
| `005afe930000-005afe934000` | GL | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglyxlog.so` |
| `005afe934000-005afe935000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglyxlog.so` |
| `005afe940000-005afe990000` | GL | `r--p` | 320 | 212 | 212 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglydiag.so` |
| `005afe990000-005afe9e8000` | GL | `r-xp` | 352 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglydiag.so` |
| `005afe9e8000-005afe9ee000` | GL | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglydiag.so` |
| `005afe9ee000-005afe9ef000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libbuglydiag.so` |
| `005afe9ef000-005afe9f0000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libbuglydiag.so.bss]` |
| `005afea00000-005afea09000` | .so | `r--p` | 36 | 24 | 24 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libgm.so` |
| `005afea09000-005afea1e000` | .so | `r-xp` | 84 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libgm.so` |
| `005afea1e000-005afea1f000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libgm.so` |
| `005afea1f000-005afea20000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libgm.so` |
| `005afea40000-005afea45000` | .so | `r--p` | 20 | 16 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libdata.z.so` |
| `005afea45000-005afea51000` | .so | `r-xp` | 48 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libdata.z.so` |
| `005afea51000-005afea53000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libdata.z.so` |
| `005afea53000-005afea54000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libdata.z.so` |
| `005afea80000-005afeae1000` | .so | `r--p` | 388 | 360 | 34 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnweb_ohos_adapter.z.so` |
| `005afebc1000-005afebc2000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnweb_ohos_adapter.z.so` |
| `005afebc2000-005afebc5000` | FilePage other | `rw-p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `[anon:libnweb_ohos_adapter.z.so.bss]` |
| `005afec00000-005afec0d000` | .so | `r--p` | 52 | 40 | 15 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_drm.so` |
| `005afec0d000-005afec21000` | .so | `r-xp` | 80 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_drm.so` |
| `005afec21000-005afec23000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_drm.so` |
| `005afec23000-005afec24000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_drm.so` |
| `005afec40000-005afec4b000` | .so | `r--p` | 44 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnative_image.so` |
| `005afec4b000-005afec58000` | .so | `r-xp` | 52 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_image.so` |
| `005afec58000-005afec5a000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libnative_image.so` |
| `005afec5a000-005afec5b000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_image.so` |
| `005afec80000-005afec87000` | .so | `r--p` | 28 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_display_manager.so` |
| `005afec87000-005afec93000` | .so | `r-xp` | 48 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_display_manager.so` |
| `005afec93000-005afec95000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_display_manager.so` |
| `005afec95000-005afec96000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_display_manager.so` |
| `005afecc0000-005afecca000` | .so | `r--p` | 40 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcert_manager_sdk.z.so` |
| `005afecca000-005afecd7000` | .so | `r-xp` | 52 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcert_manager_sdk.z.so` |
| `005afecd7000-005afecd9000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcert_manager_sdk.z.so` |
| `005afecd9000-005afecda000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcert_manager_sdk.z.so` |
| `005afed00000-005afed02000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_media_avcencinfo.so` |
| `005afed02000-005afed06000` | .so | `r-xp` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_media_avcencinfo.so` |
| `005afed06000-005afed07000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_media_avcencinfo.so` |
| `005afed07000-005afed08000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_media_avcencinfo.so` |
| `005afed40000-005afed41000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libasset_ndk.z.so` |
| `005afed41000-005afed44000` | .so | `r-xp` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libasset_ndk.z.so` |
| `005afed44000-005afed45000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libasset_ndk.z.so` |
| `005afed45000-005afed46000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libasset_ndk.z.so` |
| `005afed80000-005afedbf000` | .so | `r--p` | 252 | 96 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/web/libwebview_napi.z.so` |
| `005afedbf000-005afee81000` | .so | `r-xp` | 776 | 188 | 24 | 0 | 0 | 0.00% | `/system/lib64/module/web/libwebview_napi.z.so` |
| `005afee81000-005afee8b000` | .so | `r--p` | 40 | 40 | 40 | 0 | 0 | 0.00% | `/system/lib64/module/web/libwebview_napi.z.so` |
| `005afee8b000-005afee9e000` | .so | `rw-p` | 76 | 44 | 9 | 0 | 0 | 0.00% | `/system/lib64/module/web/libwebview_napi.z.so` |
| `005afee9e000-005afee9f000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libwebview_napi.z.so.bss]` |
| `005afeec0000-005afeec5000` | .so | `r--p` | 20 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/file/libphotoaccesshelpernative.z.so` |
| `005afeec5000-005afeed2000` | .so | `r-xp` | 52 | 48 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/file/libphotoaccesshelpernative.z.so` |
| `005afeed2000-005afeed3000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/file/libphotoaccesshelpernative.z.so` |
| `005afeed3000-005afeed4000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/file/libphotoaccesshelpernative.z.so` |
| `005afeed4000-005afeed6000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libphotoaccesshelpernative.z.so.bss]` |
| `005afef00000-005afef07000` | .so | `r--p` | 28 | 20 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libcamerapicker_napi.z.so` |
| `005afef07000-005afef13000` | .so | `r-xp` | 48 | 24 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libcamerapicker_napi.z.so` |
| `005afef13000-005afef15000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libcamerapicker_napi.z.so` |
| `005afef15000-005afef16000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libcamerapicker_napi.z.so` |
| `005afef40000-005afef45000` | .so | `r--p` | 20 | 16 | 6 | 0 | 0 | 0.00% | `/system/lib64/module/web/libwebnativemessagingextensionmanager_napi.z.so` |
| `005afef45000-005afef4e000` | .so | `r-xp` | 36 | 20 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/web/libwebnativemessagingextensionmanager_napi.z.so` |
| `005afef4e000-005afef50000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/web/libwebnativemessagingextensionmanager_napi.z.so` |
| `005afef50000-005afef51000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/web/libwebnativemessagingextensionmanager_napi.z.so` |
| `005afef80000-005aff149000` | .so | `r--p` | 1828 | 1444 | 1444 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_svg.so` |
| `005aff149000-005aff289000` | .so | `r-xp` | 1280 | 552 | 552 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_svg.so` |
| `005aff289000-005aff2a5000` | .so | `r--p` | 112 | 112 | 112 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_svg.so` |
| `005aff2a5000-005aff2a6000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_svg.so` |
| `005aff2a6000-005aff2a8000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:librnoh_svg.so.bss]` |
| `005aff2c0000-005aff2c8000` | GL | `r--p` | 32 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_imagemanager.so` |
| `005aff2c8000-005aff2d1000` | GL | `r-xp` | 36 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_imagemanager.so` |
| `005aff2d1000-005aff2d3000` | GL | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_imagemanager.so` |
| `005aff2d3000-005aff2d4000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_imagemanager.so` |
| `005aff300000-005aff305000` | .so | `r--p` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohfileuri.so` |
| `005aff305000-005aff30f000` | .so | `r-xp` | 40 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohfileuri.so` |
| `005aff30f000-005aff310000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohfileuri.so` |
| `005aff310000-005aff311000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohfileuri.so` |
| `005aff311000-005aff312000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libohfileuri.so.bss]` |
| `005aff340000-005aff37c000` | GL | `r--p` | 240 | 160 | 160 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_uimanager.so` |
| `005aff37c000-005aff3b2000` | GL | `r-xp` | 216 | 44 | 44 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_uimanager.so` |
| `005aff3b2000-005aff3b6000` | GL | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_uimanager.so` |
| `005aff3b6000-005aff3b7000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_uimanager.so` |
| `005aff3b7000-005aff3c8000` | GL | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libreact_render_uimanager.so.bss]` |
| `005aff400000-005aff401000` | .so | `r--p` | 4 | 4 | 2 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libruntimeexecutor.so` |
| `005aff401000-005aff402000` | .so | `r-xp` | 4 | 4 | 2 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libruntimeexecutor.so` |
| `005aff402000-005aff403000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libruntimeexecutor.so` |
| `005aff403000-005aff404000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libruntimeexecutor.so` |
| `005aff440000-005aff447000` | .so | `r--p` | 28 | 20 | 20 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_netinfo.so` |
| `005aff447000-005aff450000` | .so | `r-xp` | 36 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_netinfo.so` |
| `005aff450000-005aff452000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_netinfo.so` |
| `005aff452000-005aff453000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_netinfo.so` |
| `005aff480000-005aff6b5000` | .so | `r--p` | 2260 | 1608 | 1608 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh.so` |
| `005aff6b5000-005aff8d4000` | .so | `r-xp` | 2172 | 512 | 512 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh.so` |
| `005aff8d4000-005aff8f2000` | .so | `r--p` | 120 | 120 | 120 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh.so` |
| `005aff8f2000-005aff8f3000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh.so` |
| `005aff8f3000-005aff941000` | FilePage other | `rw-p` | 312 | 20 | 20 | 0 | 0 | 0.00% | `[anon:librnoh.so.bss]` |
| `005aff980000-005aff9a8000` | .so | `r--p` | 160 | 120 | 120 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_root.so` |
| `005aff9a8000-005aff9ce000` | .so | `r-xp` | 152 | 20 | 20 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_root.so` |
| `005aff9ce000-005aff9d1000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_root.so` |
| `005aff9d1000-005aff9d2000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_root.so` |
| `005aff9d2000-005aff9e3000` | FilePage other | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:librrc_root.so.bss]` |
| `005affa00000-005affa2d000` | .so | `r--p` | 180 | 136 | 136 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_scrollview.so` |
| `005affa2d000-005affa5c000` | .so | `r-xp` | 188 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_scrollview.so` |
| `005affa5c000-005affa5f000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_scrollview.so` |
| `005affa5f000-005affa60000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_scrollview.so` |
| `005affa60000-005affa71000` | FilePage other | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:librrc_scrollview.so.bss]` |
| `005affa80000-005affab8000` | GL | `r--p` | 224 | 172 | 172 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_scheduler.so` |
| `005affab8000-005affae9000` | GL | `r-xp` | 196 | 88 | 88 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_scheduler.so` |
| `005affae9000-005affaed000` | GL | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_scheduler.so` |
| `005affaed000-005affaee000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_scheduler.so` |
| `005affaee000-005affafe000` | GL | `rw-p` | 64 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libreact_render_scheduler.so.bss]` |
| `005affb00000-005affb03000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_common.so` |
| `005affb03000-005affb08000` | .so | `r-xp` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_common.so` |
| `005affb08000-005affb0a000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_common.so` |
| `005affb0a000-005affb0b000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_common.so` |
| `005affb40000-005affb52000` | GL | `r--p` | 72 | 60 | 60 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_leakchecker.so` |
| `005affb52000-005affb66000` | GL | `r-xp` | 80 | 20 | 20 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_leakchecker.so` |
| `005affb66000-005affb68000` | GL | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_leakchecker.so` |
| `005affb68000-005affb69000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_leakchecker.so` |
| `005affb69000-005affb79000` | GL | `rw-p` | 64 | 12 | 12 | 0 | 0 | 0.00% | `[anon:libreact_render_leakchecker.so.bss]` |
| `005affb80000-005affb87000` | .so | `r--p` | 28 | 24 | 24 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_async_storage.so` |
| `005affb87000-005affb91000` | .so | `r-xp` | 40 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_async_storage.so` |
| `005affb91000-005affb92000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_async_storage.so` |
| `005affb92000-005affb93000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_async_storage.so` |
| `005affb93000-005affb94000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:librnoh_async_storage.so.bss]` |
| `005affbc0000-005affbc1000` | .so | `r--p` | 4 | 4 | 2 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_utils.so` |
| `005affbc1000-005affbc3000` | .so | `r-xp` | 8 | 4 | 2 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_utils.so` |
| `005affbc3000-005affbc4000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_utils.so` |
| `005affbc4000-005affbc5000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_utils.so` |
| `005affc00000-005affc18000` | .so | `r--p` | 96 | 64 | 64 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_gesture_handler.so` |
| `005affc18000-005affc2f000` | .so | `r-xp` | 92 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_gesture_handler.so` |
| `005affc2f000-005affc32000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_gesture_handler.so` |
| `005affc32000-005affc33000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_gesture_handler.so` |
| `005affc33000-005affc34000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:librnoh_gesture_handler.so.bss]` |
| `005affc40000-005affc44000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_packer.so` |
| `005affc44000-005affc4b000` | .so | `r-xp` | 28 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_packer.so` |
| `005affc4b000-005affc4c000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_packer.so` |
| `005affc4c000-005affc4d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_packer.so` |
| `005affc80000-005affcb3000` | GL | `r--p` | 204 | 152 | 152 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_core.so` |
| `005affcb3000-005affce7000` | GL | `r-xp` | 208 | 56 | 56 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_core.so` |
| `005affce7000-005affceb000` | GL | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_core.so` |
| `005affceb000-005affcec000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_core.so` |
| `005affcec000-005affcfc000` | GL | `rw-p` | 64 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libreact_render_core.so.bss]` |
| `005affd00000-005affd27000` | GL | `r--p` | 156 | 112 | 112 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_textlayoutmanager.so` |
| `005affd27000-005affd4f000` | GL | `r-xp` | 160 | 24 | 24 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_textlayoutmanager.so` |
| `005affd4f000-005affd52000` | GL | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_textlayoutmanager.so` |
| `005affd52000-005affd53000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_textlayoutmanager.so` |
| `005affd53000-005affd63000` | GL | `rw-p` | 64 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libreact_render_textlayoutmanager.so.bss]` |
| `005affd80000-005affd86000` | GL | `r--p` | 24 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_graphics.so` |
| `005affd86000-005affd90000` | GL | `r-xp` | 40 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_graphics.so` |
| `005affd90000-005affd91000` | GL | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_graphics.so` |
| `005affd91000-005affd92000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_graphics.so` |
| `005affd92000-005affd93000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libreact_render_graphics.so.bss]` |
| `005affdc0000-005affe1e000` | .so | `r--p` | 376 | 276 | 276 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_reanimated.so` |
| `005affe1e000-005affe61000` | .so | `r-xp` | 268 | 48 | 48 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_reanimated.so` |
| `005affe61000-005affe68000` | .so | `r--p` | 28 | 28 | 28 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_reanimated.so` |
| `005affe68000-005affe69000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_reanimated.so` |
| `005affe69000-005affe6a000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:librnoh_reanimated.so.bss]` |
| `005affe80000-005affe81000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_color_space_manager.so` |
| `005affe81000-005affe83000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_color_space_manager.so` |
| `005affe83000-005affe84000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_color_space_manager.so` |
| `005affe84000-005affe85000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_color_space_manager.so` |
| `005affec0000-005affed1000` | .so | `r--p` | 68 | 56 | 56 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/liblogger.so` |
| `005affed1000-005affee3000` | .so | `r-xp` | 72 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/liblogger.so` |
| `005affee3000-005affee5000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/liblogger.so` |
| `005affee5000-005affee6000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/liblogger.so` |
| `005affee6000-005affef6000` | FilePage other | `rw-p` | 64 | 16 | 16 | 0 | 0 | 0.00% | `[anon:liblogger.so.bss]` |
| `005afff00000-005afff40000` | .so | `r--p` | 256 | 180 | 180 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_view.so` |
| `005afff40000-005afff95000` | .so | `r-xp` | 340 | 72 | 72 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_view.so` |
| `005afff95000-005afff98000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_view.so` |
| `005afff98000-005afff99000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_view.so` |
| `005afff99000-005afffab000` | FilePage other | `rw-p` | 72 | 16 | 16 | 0 | 0 | 0.00% | `[anon:librrc_view.so.bss]` |
| `005afffc0000-005afffee000` | .so | `r--p` | 184 | 136 | 136 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_image.so` |
| `005afffee000-005b0001b000` | .so | `r-xp` | 180 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_image.so` |
| `005b0001b000-005b0001e000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_image.so` |
| `005b0001e000-005b0001f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_image.so` |
| `005b0001f000-005b00030000` | FilePage other | `rw-p` | 68 | 20 | 20 | 0 | 0 | 0.00% | `[anon:librrc_image.so.bss]` |
| `005b00040000-005b0004d000` | GL | `r--p` | 52 | 28 | 28 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_runtimescheduler.so` |
| `005b0004d000-005b0005b000` | GL | `r-xp` | 56 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_runtimescheduler.so` |
| `005b0005b000-005b0005c000` | GL | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_runtimescheduler.so` |
| `005b0005c000-005b0005d000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_runtimescheduler.so` |
| `005b0005d000-005b0005e000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libreact_render_runtimescheduler.so.bss]` |
| `005b00080000-005b000aa000` | GL | `r--p` | 168 | 116 | 116 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_templateprocessor.so` |
| `005b000aa000-005b000d9000` | GL | `r-xp` | 188 | 28 | 28 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_templateprocessor.so` |
| `005b000d9000-005b000db000` | GL | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_templateprocessor.so` |
| `005b000db000-005b000dc000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_templateprocessor.so` |
| `005b000dc000-005b000ed000` | GL | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libreact_render_templateprocessor.so.bss]` |
| `005b00100000-005b00131000` | GL | `r--p` | 196 | 140 | 140 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_animations.so` |
| `005b00131000-005b00172000` | GL | `r-xp` | 260 | 24 | 24 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_animations.so` |
| `005b00172000-005b00175000` | GL | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_animations.so` |
| `005b00175000-005b00176000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_animations.so` |
| `005b00176000-005b00187000` | GL | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libreact_render_animations.so.bss]` |
| `005b001c0000-005b002a0000` | .so | `r--p` | 896 | 700 | 700 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_app.so` |
| `005b002a0000-005b00314000` | .so | `r-xp` | 464 | 332 | 332 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_app.so` |
| `005b00314000-005b00323000` | .so | `r--p` | 60 | 60 | 60 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_app.so` |
| `005b00323000-005b00324000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_app.so` |
| `005b00324000-005b00325000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:librnoh_app.so.bss]` |
| `005b00340000-005b00345000` | .so | `r--p` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpicture.so` |
| `005b00345000-005b0034e000` | .so | `r-xp` | 36 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpicture.so` |
| `005b0034e000-005b0034f000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpicture.so` |
| `005b0034f000-005b00350000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpicture.so` |
| `005b00380000-005b00381000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libqos.so` |
| `005b00381000-005b00383000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libqos.so` |
| `005b00383000-005b00384000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libqos.so` |
| `005b00384000-005b00385000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libqos.so` |
| `005b003c0000-005b003c5000` | .so | `r--p` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/librawfile.z.so` |
| `005b003c5000-005b003cf000` | .so | `r-xp` | 40 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/librawfile.z.so` |
| `005b003cf000-005b003d0000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/librawfile.z.so` |
| `005b003d0000-005b003d1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/librawfile.z.so` |
| `005b00400000-005b0040a000` | GL | `r--p` | 40 | 24 | 24 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_telemetry.so` |
| `005b0040a000-005b00414000` | GL | `r-xp` | 40 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_telemetry.so` |
| `005b00414000-005b00415000` | GL | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_telemetry.so` |
| `005b00415000-005b00416000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_telemetry.so` |
| `005b00416000-005b00417000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libreact_render_telemetry.so.bss]` |
| `005b00440000-005b00441000` | GL | `r--p` | 4 | 4 | 2 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_debug.so` |
| `005b00441000-005b00442000` | GL | `r-xp` | 4 | 4 | 2 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_debug.so` |
| `005b00442000-005b00443000` | GL | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_debug.so` |
| `005b00443000-005b00444000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_debug.so` |
| `005b00480000-005b00490000` | .so | `r--p` | 64 | 32 | 3 | 0 | 0 | 0.00% | `/system/lib64/ndk/librcp_c.so` |
| `005b00490000-005b004a2000` | .so | `r-xp` | 72 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/ndk/librcp_c.so` |
| `005b004a2000-005b004a4000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/librcp_c.so` |
| `005b004a4000-005b004a5000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/librcp_c.so` |
| `005b004c0000-005b00537000` | .so | `r--p` | 476 | 240 | 240 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libhermes.so` |
| `005b00537000-005b0070b000` | .so | `r-xp` | 1872 | 1544 | 1544 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libhermes.so` |
| `005b0070b000-005b00715000` | .so | `r--p` | 40 | 40 | 40 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libhermes.so` |
| `005b00715000-005b00717000` | .so | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libhermes.so` |
| `005b00717000-005b0071a000` | FilePage other | `rw-p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `[anon:libhermes.so.bss]` |
| `005b00740000-005b00747000` | .so | `r--p` | 28 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libjsinspector.so` |
| `005b00747000-005b00750000` | .so | `r-xp` | 36 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libjsinspector.so` |
| `005b00750000-005b00752000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libjsinspector.so` |
| `005b00752000-005b00753000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libjsinspector.so` |
| `005b00780000-005b009ea000` | .so | `r--p` | 2472 | 1156 | 1142 | 0 | 0 | 0.00% | `/system/lib64/libv8_shared.so` |
| `005b009ea000-005b01d66000` | .so | `r-xp` | 19952 | 200 | 112 | 0 | 0 | 0.00% | `/system/lib64/libv8_shared.so` |
| `005b01d66000-005b01db6000` | .so | `r--p` | 320 | 320 | 320 | 0 | 0 | 0.00% | `/system/lib64/libv8_shared.so` |
| `005b01db6000-005b01dc0000` | .so | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libv8_shared.so` |
| `005b01dc0000-005b01e14000` | .so | `rw-p` | 336 | 76 | 76 | 0 | 0 | 0.00% | `/system/lib64/libv8_shared.so` |
| `005b01e14000-005b01e52000` | FilePage other | `rw-p` | 248 | 20 | 20 | 0 | 0 | 0.00% | `[anon:libv8_shared.so.bss]` |
| `005b01e80000-005b01e81000` | .so | `r--p` | 4 | 4 | 2 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_debug.so` |
| `005b01e81000-005b01e82000` | .so | `r-xp` | 4 | 4 | 2 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_debug.so` |
| `005b01e82000-005b01e83000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_debug.so` |
| `005b01e83000-005b01e84000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_debug.so` |
| `005b01ec0000-005b01ec8000` | .so | `r--p` | 32 | 24 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_source.so` |
| `005b01ec8000-005b01ed6000` | .so | `r-xp` | 56 | 52 | 3 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_source.so` |
| `005b01ed6000-005b01ed8000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_source.so` |
| `005b01ed8000-005b01ed9000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libimage_source.so` |
| `005b01f00000-005b01f31000` | .so | `r--p` | 196 | 148 | 148 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_textinput.so` |
| `005b01f31000-005b01f62000` | .so | `r-xp` | 196 | 40 | 40 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_textinput.so` |
| `005b01f62000-005b01f65000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_textinput.so` |
| `005b01f65000-005b01f66000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_textinput.so` |
| `005b01f66000-005b01f77000` | FilePage other | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:librrc_textinput.so.bss]` |
| `005b01f80000-005b01f99000` | .so | `r--p` | 100 | 88 | 88 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_linear_gradient.so` |
| `005b01f99000-005b01fad000` | .so | `r-xp` | 80 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_linear_gradient.so` |
| `005b01fad000-005b01fb0000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_linear_gradient.so` |
| `005b01fb0000-005b01fb1000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_linear_gradient.so` |
| `005b01fb1000-005b01fb2000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:librnoh_linear_gradient.so.bss]` |
| `005b01fc0000-005b01fe6000` | .so | `r--p` | 152 | 100 | 100 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_nativemodule_core.so` |
| `005b01fe6000-005b0200b000` | .so | `r-xp` | 148 | 36 | 36 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_nativemodule_core.so` |
| `005b0200b000-005b0200e000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_nativemodule_core.so` |
| `005b0200e000-005b0200f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_nativemodule_core.so` |
| `005b0200f000-005b02010000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libreact_nativemodule_core.so.bss]` |
| `005b02040000-005b0207a000` | .so | `r--p` | 232 | 172 | 172 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_text.so` |
| `005b0207a000-005b020bf000` | .so | `r-xp` | 276 | 40 | 40 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_text.so` |
| `005b020bf000-005b020c3000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_text.so` |
| `005b020c3000-005b020c4000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librrc_text.so` |
| `005b020c4000-005b020d5000` | FilePage other | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:librrc_text.so.bss]` |
| `005b02100000-005b0210b000` | GL | `r--p` | 44 | 28 | 28 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_attributedstring.so` |
| `005b0210b000-005b02119000` | GL | `r-xp` | 56 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_attributedstring.so` |
| `005b02119000-005b0211a000` | GL | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_attributedstring.so` |
| `005b0211a000-005b0211b000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_attributedstring.so` |
| `005b0211b000-005b0211c000` | GL | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libreact_render_attributedstring.so.bss]` |
| `005b02140000-005b02169000` | .so | `r--p` | 164 | 124 | 124 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_spring_scrollview.so` |
| `005b02169000-005b0218a000` | .so | `r-xp` | 132 | 28 | 28 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_spring_scrollview.so` |
| `005b0218a000-005b0218e000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_spring_scrollview.so` |
| `005b0218e000-005b0218f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/librnoh_spring_scrollview.so` |
| `005b0218f000-005b02190000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:librnoh_spring_scrollview.so.bss]` |
| `005b021c0000-005b021c2000` | .so | `r--p` | 8 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_config.so` |
| `005b021c2000-005b021c3000` | .so | `r-xp` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_config.so` |
| `005b021c3000-005b021c4000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_config.so` |
| `005b021c4000-005b021c5000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_config.so` |
| `005b02205000-005b02206000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libhitrace_ndk.z.so` |
| `005b02240000-005b02252000` | GL | `r--p` | 72 | 60 | 60 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_mapbuffer.so` |
| `005b02252000-005b02267000` | GL | `r-xp` | 84 | 16 | 16 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_mapbuffer.so` |
| `005b02267000-005b02269000` | GL | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_mapbuffer.so` |
| `005b02269000-005b0226a000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_mapbuffer.so` |
| `005b0226a000-005b0227b000` | GL | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libreact_render_mapbuffer.so.bss]` |
| `005b02280000-005b022b0000` | .so | `r--p` | 192 | 96 | 94 | 0 | 0 | 0.00% | `/system/lib64/ndk/libjsvm.so` |
| `005b022b0000-005b022f4000` | .so | `r-xp` | 272 | 20 | 10 | 0 | 0 | 0.00% | `/system/lib64/ndk/libjsvm.so` |
| `005b022f4000-005b022f8000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/ndk/libjsvm.so` |
| `005b022f8000-005b022f9000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libjsvm.so` |
| `005b02300000-005b0231e000` | GL | `r--p` | 120 | 76 | 76 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_componentregistry.so` |
| `005b0231e000-005b0233c000` | GL | `r-xp` | 120 | 32 | 32 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_componentregistry.so` |
| `005b0233c000-005b0233e000` | GL | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_componentregistry.so` |
| `005b0233e000-005b0233f000` | GL | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_componentregistry.so` |
| `005b02340000-005b0237a000` | GL | `r--p` | 232 | 176 | 176 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_mounting.so` |
| `005b0237a000-005b023c3000` | GL | `r-xp` | 292 | 24 | 24 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_mounting.so` |
| `005b023c3000-005b023c6000` | GL | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_mounting.so` |
| `005b023c6000-005b023c8000` | GL | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libreact_render_mounting.so` |
| `005b023c8000-005b023d8000` | GL | `rw-p` | 64 | 12 | 12 | 0 | 0 | 0.00% | `[anon:libreact_render_mounting.so.bss]` |
| `005b02400000-005b0242d000` | .so | `r--p` | 180 | 132 | 132 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libjsi.so` |
| `005b0242d000-005b02461000` | .so | `r-xp` | 208 | 56 | 56 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libjsi.so` |
| `005b02461000-005b02464000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libjsi.so` |
| `005b02464000-005b02465000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libjsi.so` |
| `005b02465000-005b02476000` | FilePage other | `rw-p` | 68 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libjsi.so.bss]` |
| `005b02480000-005b02483000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_vsync.so` |
| `005b02483000-005b02487000` | .so | `r-xp` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_vsync.so` |
| `005b02487000-005b02488000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_vsync.so` |
| `005b02488000-005b02489000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_vsync.so` |
| `005b02489000-005b0248b000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30035]` |
| `005b0248b000-005b0258c000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30035]` |
| `005b0258c000-005b0258e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30036]` |
| `005b0258e000-005b0268f000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30036]` |
| `005b0268f000-005b02691000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30037]` |
| `005b02691000-005b02792000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30037]` |
| `005b02792000-005b02794000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30038]` |
| `005b02794000-005b02895000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30038]` |
| `005b02895000-005b02897000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30039]` |
| `005b02897000-005b02998000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30039]` |
| `005b02998000-005b0299a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30040]` |
| `005b0299a000-005b02a9b000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30040]` |
| `005b02a9b000-005b02a9d000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30041]` |
| `005b02a9d000-005b02b9e000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30041]` |
| `005b02b9e000-005b02ba0000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30042]` |
| `005b02ba0000-005b02ca1000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30042]` |
| `005b02ca1000-005b02ca3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30043]` |
| `005b02ca3000-005b02da4000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30043]` |
| `005b02da4000-005b02da6000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30044]` |
| `005b02da6000-005b02ea7000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30044]` |
| `005b02ea7000-005b02ea9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30045]` |
| `005b02ea9000-005b02faa000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30045]` |
| `005b02faa000-005b02fac000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30046]` |
| `005b02fac000-005b030ad000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30046]` |
| `005b030ad000-005b030af000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30047]` |
| `005b030af000-005b031b0000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30047]` |
| `005b031b0000-005b031b2000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30048]` |
| `005b031b2000-005b032b3000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30048]` |
| `005b032b3000-005b032b5000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30049]` |
| `005b032b5000-005b033b6000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30049]` |
| `005b033b6000-005b033b8000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30050]` |
| `005b033b8000-005b034b9000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30050]` |
| `005b034b9000-005b034bb000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30051]` |
| `005b034bb000-005b035bc000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30051]` |
| `005b035bc000-005b035be000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30052]` |
| `005b035be000-005b036bf000` | FilePage other | `rw-p` | 1028 | 28 | 28 | 0 | 0 | 0.00% | `[anon:stack:30052]` |
| `005b036c0000-005b036dd000` | .so | `r--p` | 116 | 60 | 30 | 0 | 0 | 0.00% | `/system/lib64/module/net/libwebsocket.z.so` |
| `005b036dd000-005b03744000` | .so | `r-xp` | 412 | 68 | 34 | 0 | 0 | 0.00% | `/system/lib64/module/net/libwebsocket.z.so` |
| `005b03744000-005b03747000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/net/libwebsocket.z.so` |
| `005b03747000-005b03748000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/net/libwebsocket.z.so` |
| `005b03748000-005b03749000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libwebsocket.z.so.bss]` |
| `005b03780000-005b03787000` | .so | `r--p` | 28 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/libfont.z.so` |
| `005b03787000-005b0379c000` | .so | `r-xp` | 84 | 52 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/libfont.z.so` |
| `005b0379c000-005b0379e000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/libfont.z.so` |
| `005b0379e000-005b0379f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libfont.z.so` |
| `005b037c0000-005b037cc000` | .so | `r--p` | 48 | 32 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/libaccessibility_napi.z.so` |
| `005b037cc000-005b037eb000` | .so | `r-xp` | 124 | 60 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/libaccessibility_napi.z.so` |
| `005b037eb000-005b037ed000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/libaccessibility_napi.z.so` |
| `005b037ed000-005b037ee000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libaccessibility_napi.z.so` |
| `005b037ee000-005b037ef000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libaccessibility_napi.z.so.bss]` |
| `005b03800000-005b03814000` | .so | `r--p` | 80 | 72 | 18 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_call_manager_api.z.so` |
| `005b03814000-005b03849000` | .so | `r-xp` | 212 | 80 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_call_manager_api.z.so` |
| `005b03849000-005b0384f000` | .so | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_call_manager_api.z.so` |
| `005b0384f000-005b03850000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_call_manager_api.z.so` |
| `005b03880000-005b0388c000` | .so | `r--p` | 48 | 40 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libcall.z.so` |
| `005b0388c000-005b038bb000` | .so | `r-xp` | 188 | 68 | 20 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libcall.z.so` |
| `005b038bb000-005b038bf000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libcall.z.so` |
| `005b038bf000-005b038c4000` | .so | `rw-p` | 20 | 16 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libcall.z.so` |
| `005b03900000-005b039fd000` | .so | `r--p` | 1012 | 436 | 436 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libImSDK.so` |
| `005b039fd000-005b03e8e000` | .so | `r-xp` | 4676 | 2548 | 2548 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libImSDK.so` |
| `005b03e8e000-005b03ea1000` | .so | `r--p` | 76 | 76 | 76 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libImSDK.so` |
| `005b03ea1000-005b03ea3000` | .so | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libImSDK.so` |
| `005b03ea3000-005b03eaa000` | FilePage other | `rw-p` | 28 | 28 | 28 | 0 | 0 | 0.00% | `[anon:libImSDK.so.bss]` |
| `005b03eaa000-005b03eac000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30053]` |
| `005b03eac000-005b03fad000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30053]` |
| `005b03fad000-005b03faf000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30054]` |
| `005b03faf000-005b040b0000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30054]` |
| `005b040c0000-005b040c1000` | .so | `r--p` | 4 | 4 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanbarcode_napi.z.so` |
| `005b040c1000-005b040c4000` | .so | `r-xp` | 12 | 8 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanbarcode_napi.z.so` |
| `005b040c4000-005b040c5000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanbarcode_napi.z.so` |
| `005b040c5000-005b040ca000` | .so | `rw-p` | 20 | 16 | 9 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanbarcode_napi.z.so` |
| `005b04100000-005b04101000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscancore_napi.z.so` |
| `005b04101000-005b04104000` | .so | `r-xp` | 12 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscancore_napi.z.so` |
| `005b04104000-005b04105000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscancore_napi.z.so` |
| `005b04105000-005b04106000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscancore_napi.z.so` |
| `005b04140000-005b0414d000` | .so | `r--p` | 52 | 32 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanuiextservice_napi.z.so` |
| `005b0414d000-005b0416d000` | .so | `r-xp` | 128 | 40 | 20 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanuiextservice_napi.z.so` |
| `005b0416d000-005b0416f000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanuiextservice_napi.z.so` |
| `005b0416f000-005b04170000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanuiextservice_napi.z.so` |
| `005b04170000-005b04171000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libscanuiextservice_napi.z.so.bss]` |
| `005b04180000-005b04188000` | .so | `r--p` | 32 | 16 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanha_napi.z.so` |
| `005b04188000-005b0419d000` | .so | `r-xp` | 84 | 24 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanha_napi.z.so` |
| `005b0419d000-005b0419f000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanha_napi.z.so` |
| `005b0419f000-005b041a0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/scan/libscanha_napi.z.so` |
| `005b041a0000-005b041a2000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libscanha_napi.z.so.bss]` |
| `005b041c0000-005b041c1000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/advertising/libautoadcomponent.z.so` |
| `005b041c1000-005b041c4000` | .so | `r-xp` | 12 | 8 | 6 | 0 | 0 | 0.00% | `/system/lib64/module/advertising/libautoadcomponent.z.so` |
| `005b041c4000-005b041c5000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/advertising/libautoadcomponent.z.so` |
| `005b041c5000-005b041c9000` | .so | `rw-p` | 16 | 16 | 14 | 0 | 0 | 0.00% | `/system/lib64/module/advertising/libautoadcomponent.z.so` |
| `005b04200000-005b0420d000` | .so | `r--p` | 52 | 40 | 40 | 0 | 0 | 0.00% | `/system/lib64/module/libadvertising.z.so` |
| `005b04226000-005b0422b000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/module/libadvertising.z.so` |
| `005b0422b000-005b04235000` | .so | `rw-p` | 40 | 28 | 28 | 0 | 0 | 0.00% | `/system/lib64/module/libadvertising.z.so` |
| `005b04235000-005b04237000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libadvertising.z.so.bss]` |
| `005b04240000-005b04243000` | .so | `r--p` | 12 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libconfigpolicy.z.so` |
| `005b04243000-005b04249000` | .so | `r-xp` | 24 | 20 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/libconfigpolicy.z.so` |
| `005b04249000-005b0424a000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libconfigpolicy.z.so` |
| `005b0424a000-005b0424b000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libconfigpolicy.z.so` |
| `005b04280000-005b04281000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/advertising/libadcomponent.z.so` |
| `005b04281000-005b04284000` | .so | `r-xp` | 12 | 8 | 6 | 0 | 0 | 0.00% | `/system/lib64/module/advertising/libadcomponent.z.so` |
| `005b04284000-005b04285000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/advertising/libadcomponent.z.so` |
| `005b04285000-005b0428e000` | .so | `rw-p` | 36 | 36 | 34 | 0 | 0 | 0.00% | `/system/lib64/module/advertising/libadcomponent.z.so` |
| `005b042c0000-005b042c1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/liblightweightmap.z.so` |
| `005b042c1000-005b042c4000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/liblightweightmap.z.so` |
| `005b042c4000-005b042c5000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/util/liblightweightmap.z.so` |
| `005b042c5000-005b042ca000` | .so | `rw-p` | 20 | 12 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/util/liblightweightmap.z.so` |
| `005b04300000-005b04304000` | .so | `r--p` | 16 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartupmanager_napi.z.so` |
| `005b04304000-005b0430a000` | .so | `r-xp` | 24 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartupmanager_napi.z.so` |
| `005b0430a000-005b0430b000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartupmanager_napi.z.so` |
| `005b0430b000-005b0430c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/appstartup/libstartupmanager_napi.z.so` |
| `005b0430c000-005b0450c000` | FilePage other | `rw-s` | 2048 | 1200 | 1200 | 0 | 0 | 0.00% | `/data/storage/el2/base/files/mmkv/DY_DEFAULT_MAP_ID` |
| `005b04540000-005b04545000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnet_bundle_utils.z.so` |
| `005b04545000-005b0454b000` | .so | `r-xp` | 24 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnet_bundle_utils.z.so` |
| `005b0454b000-005b0454c000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnet_bundle_utils.z.so` |
| `005b0454c000-005b0454d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnet_bundle_utils.z.so` |
| `005b0454d000-005b045b7000` | FilePage other | `r--p` | 424 | 424 | 424 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNMagicAwakening-harmony_4bbe186/dyrnmagicawakening.bundle` |
| `005b045c0000-005b0478f000` | FilePage other | `r--p` | 1852 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/etsstdlib_bootabc.abc` |
| `005b0478f000-005b04d9a000` | FilePage other | `r--p` | 6188 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/arkoala.abc` |
| `005b04d9a000-005b050fe000` | FilePage other | `r--p` | 3472 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/assembled_advanced_ets_abc.abc` |
| `005b050fe000-005b05142000` | FilePage other | `r--p` | 272 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/avsession_taihe_abc.abc` |
| `005b05142000-005b051d0000` | FilePage other | `r--p` | 568 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/camera_framework_taihe_abc.abc` |
| `005b051d0000-005b05210000` | FilePage other | `r--p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/ets2abc_commonsdk_api.abc` |
| `005b05210000-005b05266000` | FilePage other | `r--p` | 344 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/image_framework_taihe_abc.abc` |
| `005b05266000-005b052a7000` | FilePage other | `r--p` | 260 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/media_taihe_abc.abc` |
| `005b052a7000-005b052f4000` | FilePage other | `r--p` | 308 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/photo_access_helper.abc` |
| `005b052f4000-005b05349000` | FilePage other | `r--p` | 340 | 0 | 0 | 0 | 0 | 0.00% | `/system/framework/window_stage_ani.abc` |
| `005b05380000-005b05392000` | .so | `r--p` | 72 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libarkts_frontend.z.so` |
| `005b05392000-005b053be000` | .so | `r-xp` | 176 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkts_frontend.z.so` |
| `005b053be000-005b053c3000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkts_frontend.z.so` |
| `005b053c3000-005b053c4000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkts_frontend.z.so` |
| `005b05400000-005b05401000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libhilog_ndk.z.so` |
| `005b05405000-005b05406000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libhilog_ndk.z.so` |
| `005b05440000-005b05587000` | .so | `r--p` | 1308 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libArkoalaNative_ark.z.so` |
| `005b05587000-005b05826000` | .so | `r-xp` | 2684 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libArkoalaNative_ark.z.so` |
| `005b05826000-005b05837000` | .so | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libArkoalaNative_ark.z.so` |
| `005b05837000-005b05838000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libArkoalaNative_ark.z.so` |
| `005b05838000-005b05839000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libArkoalaNative_ark.z.so.bss]` |
| `005b05840000-005b05876000` | .so | `r--p` | 216 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libimage_taihe.z.so` |
| `005b05876000-005b0594b000` | .so | `r-xp` | 852 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimage_taihe.z.so` |
| `005b0594b000-005b05951000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimage_taihe.z.so` |
| `005b05951000-005b05952000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libimage_taihe.z.so` |
| `005b05952000-005b0595b000` | FilePage other | `rw-p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libimage_taihe.z.so.bss]` |
| `005b05980000-005b05981000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_base_context.z.so` |
| `005b05981000-005b05984000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_base_context.z.so` |
| `005b05984000-005b05985000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_base_context.z.so` |
| `005b05985000-005b05986000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_base_context.z.so` |
| `005b059c0000-005b059c3000` | .so | `r--p` | 12 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libani_color_space_object_convertor.so` |
| `005b059c3000-005b059ca000` | .so | `r-xp` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libani_color_space_object_convertor.so` |
| `005b059ca000-005b059cb000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libani_color_space_object_convertor.so` |
| `005b059cb000-005b059cc000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libani_color_space_object_convertor.so` |
| `005b05a00000-005b05a10000` | .so | `r--p` | 64 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtext_engine_ani.z.so` |
| `005b05a10000-005b05a42000` | .so | `r-xp` | 200 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtext_engine_ani.z.so` |
| `005b05a42000-005b05a46000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtext_engine_ani.z.so` |
| `005b05a46000-005b05a47000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtext_engine_ani.z.so` |
| `005b05a47000-005b05a48000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libtext_engine_ani.z.so.bss]` |
| `005b05a80000-005b05a83000` | .so | `r--p` | 12 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextra_config_ani.z.so` |
| `005b05a83000-005b05a89000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextra_config_ani.z.so` |
| `005b05a89000-005b05a8a000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextra_config_ani.z.so` |
| `005b05a8a000-005b05a8b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libextra_config_ani.z.so` |
| `005b05ac0000-005b05b9c000` | .so | `r--p` | 880 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libudmf_taihe_native.z.so` |
| `005b05b9c000-005b05cfb000` | .so | `r-xp` | 1404 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libudmf_taihe_native.z.so` |
| `005b05cfb000-005b05d09000` | .so | `r--p` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libudmf_taihe_native.z.so` |
| `005b05d09000-005b05d0a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libudmf_taihe_native.z.so` |
| `005b05d0a000-005b05d15000` | FilePage other | `rw-p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libudmf_taihe_native.z.so.bss]` |
| `005b05d40000-005b05d78000` | .so | `r--p` | 224 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libdrawing_ani.so` |
| `005b05d78000-005b05dd5000` | .so | `r-xp` | 372 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdrawing_ani.so` |
| `005b05dd5000-005b05ddb000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdrawing_ani.so` |
| `005b05ddb000-005b05ddc000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libdrawing_ani.so` |
| `005b05ddc000-005b05ddd000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdrawing_ani.so.bss]` |
| `005b05e00000-005b05e1e000` | .so | `r--p` | 120 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libarkoala_native_ani.so` |
| `005b05e1e000-005b05e6e000` | .so | `r-xp` | 320 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkoala_native_ani.so` |
| `005b05e6e000-005b05e73000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkoala_native_ani.so` |
| `005b05e73000-005b05e74000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libarkoala_native_ani.so` |
| `005b05e74000-005b05e75000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libarkoala_native_ani.so.bss]` |
| `005b05e80000-005b05ebd000` | .so | `r--p` | 244 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_ability_ani.z.so` |
| `005b05ebd000-005b05f04000` | .so | `r-xp` | 284 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_ability_ani.z.so` |
| `005b05f04000-005b05f0a000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_ability_ani.z.so` |
| `005b05f0a000-005b05f0b000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libui_ability_ani.z.so` |
| `005b05f40000-005b05f43000` | .so | `r--p` | 12 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_ui_extension_callback.z.so` |
| `005b05f43000-005b05f48000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_ui_extension_callback.z.so` |
| `005b05f48000-005b05f49000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_ui_extension_callback.z.so` |
| `005b05f49000-005b05f4a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libani_ui_extension_callback.z.so` |
| `005b05f80000-005b05f82000` | .so | `r--p` | 8 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_info_ani_kit.z.so` |
| `005b05f82000-005b05f86000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_info_ani_kit.z.so` |
| `005b05f86000-005b05f87000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_info_ani_kit.z.so` |
| `005b05f87000-005b05f88000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdialog_request_info_ani_kit.z.so` |
| `005b05fc0000-005b05fc4000` | .so | `r--p` | 16 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/librpc_ani.so` |
| `005b05fc4000-005b05fc7000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librpc_ani.so` |
| `005b05fc7000-005b05fc9000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librpc_ani.so` |
| `005b05fc9000-005b05fca000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librpc_ani.so` |
| `005b06000000-005b06005000` | .so | `r--p` | 20 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libcaller_complex_ani.so` |
| `005b06005000-005b0600d000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcaller_complex_ani.so` |
| `005b0600d000-005b0600f000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcaller_complex_ani.so` |
| `005b0600f000-005b06010000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcaller_complex_ani.so` |
| `005b06040000-005b0609c000` | .so | `r--p` | 368 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindowstageani_kit.z.so` |
| `005b0609c000-005b06146000` | .so | `r-xp` | 680 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindowstageani_kit.z.so` |
| `005b06146000-005b06150000` | .so | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindowstageani_kit.z.so` |
| `005b06150000-005b06151000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libwindowstageani_kit.z.so` |
| `005b06180000-005b06185000` | .so | `r--p` | 20 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension_connection_ani.z.so` |
| `005b06185000-005b0618b000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension_connection_ani.z.so` |
| `005b0618b000-005b0618d000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension_connection_ani.z.so` |
| `005b0618d000-005b0618e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libui_service_extension_connection_ani.z.so` |
| `005b061c3000-005b061c4000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_base_context.z.so` |
| `005b061c4000-005b061c5000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnapi_base_context.z.so.bss]` |
| `005b06200000-005b06216000` | .so | `r--p` | 88 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_stage_ani.z.so` |
| `005b06216000-005b06229000` | .so | `r-xp` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_stage_ani.z.so` |
| `005b06229000-005b0622b000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_stage_ani.z.so` |
| `005b0622b000-005b0622c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libability_stage_ani.z.so` |
| `005b0622c000-005b0622d000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libability_stage_ani.z.so.bss]` |
| `005b06240000-005b06257000` | .so | `r--p` | 92 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/ability/libfeatureability.z.so` |
| `005b06257000-005b06279000` | .so | `r-xp` | 136 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/ability/libfeatureability.z.so` |
| `005b06279000-005b0627c000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/ability/libfeatureability.z.so` |
| `005b0627c000-005b0627d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/ability/libfeatureability.z.so` |
| `005b0627d000-005b0627e000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libfeatureability.z.so.bss]` |
| `005b06280000-005b062ad000` | .so | `r--p` | 180 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_ability_common.z.so` |
| `005b062ad000-005b062e2000` | .so | `r-xp` | 212 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_ability_common.z.so` |
| `005b062e2000-005b062e6000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_ability_common.z.so` |
| `005b062e6000-005b062e7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_ability_common.z.so` |
| `005b062e7000-005b062e8000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnapi_ability_common.z.so.bss]` |
| `005b06300000-005b06306000` | .so | `r--p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_napi_common.z.so` |
| `005b06306000-005b0630e000` | .so | `r-xp` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_napi_common.z.so` |
| `005b0630e000-005b06310000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_napi_common.z.so` |
| `005b06310000-005b06311000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_napi_common.z.so` |
| `005b06340000-005b06346000` | .so | `r--p` | 24 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauthorization_napi.z.so` |
| `005b06346000-005b0634f000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauthorization_napi.z.so` |
| `005b0634f000-005b06351000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauthorization_napi.z.so` |
| `005b06351000-005b06352000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauthorization_napi.z.so` |
| `005b06380000-005b06394000` | .so | `r--p` | 80 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_iam_napi.z.so` |
| `005b06394000-005b063b1000` | .so | `r-xp` | 116 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_iam_napi.z.so` |
| `005b063b1000-005b063b4000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_iam_napi.z.so` |
| `005b063b4000-005b063b5000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_iam_napi.z.so` |
| `005b063b5000-005b063b6000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaccount_iam_napi.z.so.bss]` |
| `005b063c0000-005b063c9000` | .so | `r--p` | 36 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdomain_account_napi.z.so` |
| `005b063c9000-005b063dc000` | .so | `r-xp` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdomain_account_napi.z.so` |
| `005b063dc000-005b063de000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdomain_account_napi.z.so` |
| `005b063de000-005b063df000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdomain_account_napi.z.so` |
| `005b06400000-005b0640d000` | .so | `r--p` | 52 | 16 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauthorization_innerkits.z.so` |
| `005b0640d000-005b0641b000` | .so | `r-xp` | 56 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauthorization_innerkits.z.so` |
| `005b0641b000-005b06423000` | .so | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauthorization_innerkits.z.so` |
| `005b06423000-005b06424000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libauthorization_innerkits.z.so` |
| `005b06440000-005b0645e000` | .so | `r--p` | 120 | 24 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuserauth_client.z.so` |
| `005b0645e000-005b064a3000` | .so | `r-xp` | 276 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuserauth_client.z.so` |
| `005b064a3000-005b064b2000` | .so | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuserauth_client.z.so` |
| `005b064b2000-005b064b3000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libuserauth_client.z.so` |
| `005b064b3000-005b064b4000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libuserauth_client.z.so.bss]` |
| `005b064c0000-005b064d4000` | .so | `r--p` | 80 | 20 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_iam_innerkits.z.so` |
| `005b064d4000-005b064ed000` | .so | `r-xp` | 100 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_iam_innerkits.z.so` |
| `005b064ed000-005b064f8000` | .so | `r--p` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_iam_innerkits.z.so` |
| `005b064f8000-005b064f9000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaccount_iam_innerkits.z.so` |
| `005b06500000-005b0650d000` | .so | `r--p` | 52 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/account/libosaccount.z.so` |
| `005b0650d000-005b06527000` | .so | `r-xp` | 104 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/account/libosaccount.z.so` |
| `005b06527000-005b06529000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/account/libosaccount.z.so` |
| `005b06529000-005b0652b000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/account/libosaccount.z.so` |
| `005b0652b000-005b0652c000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libosaccount.z.so.bss]` |
| `005b06540000-005b0654f000` | .so | `r--p` | 60 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpinauth_framework.z.so` |
| `005b0654f000-005b06576000` | .so | `r-xp` | 156 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpinauth_framework.z.so` |
| `005b06576000-005b0657b000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpinauth_framework.z.so` |
| `005b0657b000-005b0657c000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libpinauth_framework.z.so` |
| `005b06580000-005b06587000` | .so | `r--p` | 28 | 28 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libanimator.z.so` |
| `005b06587000-005b0659f000` | .so | `r-xp` | 96 | 96 | 20 | 0 | 0 | 0.00% | `/system/lib64/module/libanimator.z.so` |
| `005b0659f000-005b065a2000` | .so | `r--p` | 12 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libanimator.z.so` |
| `005b065a2000-005b065a3000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libanimator.z.so` |
| `005b065c0000-005b065c1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libabilitystage.z.so` |
| `005b065c1000-005b065c2000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libabilitystage.z.so` |
| `005b065c2000-005b065c3000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libabilitystage.z.so` |
| `005b065c3000-005b065c5000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libabilitystage.z.so` |
| `005b06608000-005b06609000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libhilog.z.so` |
| `005b06640000-005b06641000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libconfigurationconstant.z.so` |
| `005b06641000-005b06643000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libconfigurationconstant.z.so` |
| `005b06643000-005b06644000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libconfigurationconstant.z.so` |
| `005b06644000-005b06645000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libconfigurationconstant.z.so` |
| `005b06680000-005b06681000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libextensionability_napi.z.so` |
| `005b06681000-005b06682000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libextensionability_napi.z.so` |
| `005b06682000-005b06683000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libextensionability_napi.z.so` |
| `005b06683000-005b06685000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libextensionability_napi.z.so` |
| `005b066c0000-005b066c1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libuiability.z.so` |
| `005b066c1000-005b066c2000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libuiability.z.so` |
| `005b066c2000-005b066c3000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libuiability.z.so` |
| `005b066c3000-005b066c6000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libuiability.z.so` |
| `005b06700000-005b06701000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcallee_napi.z.so` |
| `005b06701000-005b06702000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcallee_napi.z.so` |
| `005b06702000-005b06703000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcallee_napi.z.so` |
| `005b06703000-005b06708000` | .so | `rw-p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcallee_napi.z.so` |
| `005b06740000-005b06745000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librpc.z.so` |
| `005b06745000-005b0674f000` | .so | `r-xp` | 40 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/librpc.z.so` |
| `005b0674f000-005b06750000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librpc.z.so` |
| `005b06750000-005b06751000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librpc.z.so` |
| `005b06780000-005b0678b000` | .so | `r--p` | 44 | 20 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/libabilityaccessctrl.z.so` |
| `005b0678b000-005b067bd000` | .so | `r-xp` | 200 | 88 | 13 | 0 | 0 | 0.00% | `/system/lib64/module/libabilityaccessctrl.z.so` |
| `005b067bd000-005b067c1000` | .so | `r--p` | 16 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libabilityaccessctrl.z.so` |
| `005b067c1000-005b067c2000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libabilityaccessctrl.z.so` |
| `005b067c2000-005b067c3000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libabilityaccessctrl.z.so.bss]` |
| `005b06800000-005b06802000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libabilityconstant.z.so` |
| `005b06802000-005b06805000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libabilityconstant.z.so` |
| `005b06805000-005b06806000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libabilityconstant.z.so` |
| `005b06806000-005b06807000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libabilityconstant.z.so` |
| `005b06840000-005b06841000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libuiextensionability_napi.z.so` |
| `005b06841000-005b06842000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libuiextensionability_napi.z.so` |
| `005b06842000-005b06843000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libuiextensionability_napi.z.so` |
| `005b06843000-005b06845000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libuiextensionability_napi.z.so` |
| `005b06880000-005b06881000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libcontextconstant_napi.z.so` |
| `005b06881000-005b06883000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libcontextconstant_napi.z.so` |
| `005b06883000-005b06884000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libcontextconstant_napi.z.so` |
| `005b06884000-005b06885000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libcontextconstant_napi.z.so` |
| `005b068c0000-005b068c1000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/application/libability_napi.z.so` |
| `005b068c1000-005b068c2000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libability_napi.z.so` |
| `005b068c2000-005b068c3000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libability_napi.z.so` |
| `005b068c3000-005b068c6000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libability_napi.z.so` |
| `005b06900000-005b06901000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitycontext_napi.z.so` |
| `005b06901000-005b06902000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitycontext_napi.z.so` |
| `005b06902000-005b06903000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitycontext_napi.z.so` |
| `005b06903000-005b06909000` | .so | `rw-p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitycontext_napi.z.so` |
| `005b06940000-005b06941000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcontext_napi.z.so` |
| `005b06941000-005b06942000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcontext_napi.z.so` |
| `005b06942000-005b06943000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcontext_napi.z.so` |
| `005b06943000-005b06949000` | .so | `rw-p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcontext_napi.z.so` |
| `005b06980000-005b06981000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcaller_napi.z.so` |
| `005b06981000-005b06982000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcaller_napi.z.so` |
| `005b06982000-005b06983000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcaller_napi.z.so` |
| `005b06983000-005b06989000` | .so | `rw-p` | 24 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libcaller_napi.z.so` |
| `005b069c0000-005b069c1000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitystage_napi.z.so` |
| `005b069c1000-005b069c2000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitystage_napi.z.so` |
| `005b069c2000-005b069c3000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitystage_napi.z.so` |
| `005b069c3000-005b069c5000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitystage_napi.z.so` |
| `005b06a00000-005b06a01000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitystagecontext_napi.z.so` |
| `005b06a01000-005b06a02000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitystagecontext_napi.z.so` |
| `005b06a02000-005b06a03000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitystagecontext_napi.z.so` |
| `005b06a03000-005b06a05000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libabilitystagecontext_napi.z.so` |
| `005b06a40000-005b06a41000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libapplicationcontext_napi.z.so` |
| `005b06a41000-005b06a42000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libapplicationcontext_napi.z.so` |
| `005b06a42000-005b06a43000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libapplicationcontext_napi.z.so` |
| `005b06a43000-005b06a4a000` | .so | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libapplicationcontext_napi.z.so` |
| `005b06a80000-005b06a81000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libextensioncontext_napi.z.so` |
| `005b06a81000-005b06a82000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libextensioncontext_napi.z.so` |
| `005b06a82000-005b06a83000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libextensioncontext_napi.z.so` |
| `005b06a83000-005b06a85000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libextensioncontext_napi.z.so` |
| `005b06ac0000-005b06ac1000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/application/libserviceextensionability_napi.z.so` |
| `005b06ac1000-005b06ac2000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libserviceextensionability_napi.z.so` |
| `005b06ac2000-005b06ac3000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libserviceextensionability_napi.z.so` |
| `005b06ac3000-005b06ac5000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libserviceextensionability_napi.z.so` |
| `005b06b00000-005b06b01000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libserviceextensioncontext_napi.z.so` |
| `005b06b01000-005b06b02000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libserviceextensioncontext_napi.z.so` |
| `005b06b02000-005b06b03000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libserviceextensioncontext_napi.z.so` |
| `005b06b03000-005b06b08000` | .so | `rw-p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libserviceextensioncontext_napi.z.so` |
| `005b06b40000-005b06b41000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/application/libwindowstage.z.so` |
| `005b06b41000-005b06b44000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libwindowstage.z.so` |
| `005b06b44000-005b06b45000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libwindowstage.z.so` |
| `005b06b45000-005b06b47000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/application/libwindowstage.z.so` |
| `005b06b80000-005b06b83000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbatteryinfo.z.so` |
| `005b06b83000-005b06b88000` | .so | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbatteryinfo.z.so` |
| `005b06b88000-005b06b89000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbatteryinfo.z.so` |
| `005b06b89000-005b06b8a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbatteryinfo.z.so` |
| `005b06bc0000-005b06bc5000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbatterysrv_client.z.so` |
| `005b06bc5000-005b06bce000` | .so | `r-xp` | 36 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbatterysrv_client.z.so` |
| `005b06bce000-005b06bcf000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbatterysrv_client.z.so` |
| `005b06bcf000-005b06bd0000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbatterysrv_client.z.so` |
| `005b06bd0000-005b06bd1000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libbatterysrv_client.z.so.bss]` |
| `005b06c00000-005b06c05000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbuffer.z.so` |
| `005b06c05000-005b06c12000` | .so | `r-xp` | 52 | 52 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/libbuffer.z.so` |
| `005b06c12000-005b06c14000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbuffer.z.so` |
| `005b06c14000-005b06c37000` | .so | `rw-p` | 140 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbuffer.z.so` |
| `005b06c40000-005b06c43000` | Graph | `r--p` | 12 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbundlemgr_graphics.z.so` |
| `005b06c43000-005b06c48000` | Graph | `r-xp` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbundlemgr_graphics.z.so` |
| `005b06c48000-005b06c49000` | Graph | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbundlemgr_graphics.z.so` |
| `005b06c49000-005b06c4a000` | Graph | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libbundlemgr_graphics.z.so` |
| `005b06c4a000-005b06c4b000` | Graph | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libbundlemgr_graphics.z.so.bss]` |
| `005b06c80000-005b06c8f000` | .so | `r--p` | 60 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libbundle.z.so` |
| `005b06c8f000-005b06cb9000` | .so | `r-xp` | 168 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbundle.z.so` |
| `005b06cb9000-005b06cbd000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbundle.z.so` |
| `005b06cbd000-005b06cbe000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libbundle.z.so` |
| `005b06cbe000-005b06cbf000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libbundle.z.so.bss]` |
| `005b06cc0000-005b06cc1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libcommoneventmanager.z.so` |
| `005b06cc1000-005b06cc4000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libcommoneventmanager.z.so` |
| `005b06cc4000-005b06cc5000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libcommoneventmanager.z.so` |
| `005b06cc5000-005b06cc6000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libcommoneventmanager.z.so` |
| `005b06d00000-005b06d1e000` | .so | `r--p` | 120 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnapi_commoneventmanager.z.so` |
| `005b06d1e000-005b06d3c000` | .so | `r-xp` | 120 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnapi_commoneventmanager.z.so` |
| `005b06d3c000-005b06d3f000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnapi_commoneventmanager.z.so` |
| `005b06d3f000-005b06d40000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnapi_commoneventmanager.z.so` |
| `005b06d40000-005b06d41000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnapi_commoneventmanager.z.so.bss]` |
| `005b06d80000-005b06d94000` | .so | `r--p` | 80 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libcontact.z.so` |
| `005b06d94000-005b06de4000` | .so | `r-xp` | 320 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libcontact.z.so` |
| `005b06de4000-005b06de6000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libcontact.z.so` |
| `005b06de6000-005b06def000` | .so | `rw-p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libcontact.z.so` |
| `005b06e00000-005b06e03000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libdeviceinfo.z.so` |
| `005b06e03000-005b06e08000` | .so | `r-xp` | 20 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libdeviceinfo.z.so` |
| `005b06e08000-005b06e0a000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libdeviceinfo.z.so` |
| `005b06e0a000-005b06e0b000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libdeviceinfo.z.so` |
| `005b06e0b000-005b06e0c000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libdeviceinfo.z.so.bss]` |
| `005b06e40000-005b06e51000` | .so | `r--p` | 68 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdatashare.z.so` |
| `005b06e51000-005b06e91000` | .so | `r-xp` | 256 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdatashare.z.so` |
| `005b06e91000-005b06e97000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdatashare.z.so` |
| `005b06e97000-005b06e98000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdatashare.z.so` |
| `005b06ec0000-005b06ec1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdatasharepredicates.z.so` |
| `005b06ec1000-005b06ec4000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdatasharepredicates.z.so` |
| `005b06ec4000-005b06ec5000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdatasharepredicates.z.so` |
| `005b06ec5000-005b06ec6000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdatasharepredicates.z.so` |
| `005b06f00000-005b06f1d000` | .so | `r--p` | 116 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdistributedkvstore.z.so` |
| `005b06f1d000-005b06f70000` | .so | `r-xp` | 332 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdistributedkvstore.z.so` |
| `005b06f70000-005b06f78000` | .so | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdistributedkvstore.z.so` |
| `005b06f78000-005b06f79000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libdistributedkvstore.z.so` |
| `005b06f80000-005b06f89000` | .so | `r--p` | 36 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libpreferences.z.so` |
| `005b06f89000-005b06fa7000` | .so | `r-xp` | 120 | 76 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/data/libpreferences.z.so` |
| `005b06fa7000-005b06fa9000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libpreferences.z.so` |
| `005b06fa9000-005b06faa000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/data/libpreferences.z.so` |
| `005b06fc0000-005b06fc8000` | .so | `r--p` | 32 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpreferences_jscommon.z.so` |
| `005b06fc8000-005b06fd4000` | .so | `r-xp` | 48 | 36 | 2 | 0 | 0 | 0.00% | `/system/lib64/libpreferences_jscommon.z.so` |
| `005b06fd4000-005b06fd6000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libpreferences_jscommon.z.so` |
| `005b06fd6000-005b06fd7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libpreferences_jscommon.z.so` |
| `005b07000000-005b0701c000` | .so | `r--p` | 112 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/data/librelationalstore.z.so` |
| `005b0701c000-005b070b1000` | .so | `r-xp` | 596 | 336 | 36 | 0 | 0 | 0.00% | `/system/lib64/module/data/librelationalstore.z.so` |
| `005b070b1000-005b070b9000` | .so | `r--p` | 32 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/data/librelationalstore.z.so` |
| `005b070b9000-005b070ba000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/data/librelationalstore.z.so` |
| `005b070c0000-005b070d0000` | .so | `r--p` | 64 | 64 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libdisplay_napi.z.so` |
| `005b070d0000-005b070f6000` | .so | `r-xp` | 152 | 152 | 11 | 0 | 0 | 0.00% | `/system/lib64/module/libdisplay_napi.z.so` |
| `005b070f6000-005b070f9000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libdisplay_napi.z.so` |
| `005b070f9000-005b070fa000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libdisplay_napi.z.so` |
| `005b07100000-005b07109000` | .so | `r--p` | 36 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/file/libfileuri.z.so` |
| `005b07109000-005b07135000` | .so | `r-xp` | 176 | 44 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/file/libfileuri.z.so` |
| `005b07135000-005b07138000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libfileuri.z.so` |
| `005b07138000-005b07139000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/file/libfileuri.z.so` |
| `005b07139000-005b0713a000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libfileuri.z.so.bss]` |
| `005b07140000-005b0714d000` | .so | `r--p` | 52 | 24 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfilemgmt_libn.z.so` |
| `005b0714d000-005b0716f000` | .so | `r-xp` | 136 | 40 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfilemgmt_libn.z.so` |
| `005b0716f000-005b07172000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfilemgmt_libn.z.so` |
| `005b07172000-005b07173000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libfilemgmt_libn.z.so` |
| `005b07180000-005b07188000` | .so | `r--p` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libhash.z.so` |
| `005b07188000-005b0719b000` | .so | `r-xp` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libhash.z.so` |
| `005b0719b000-005b0719e000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libhash.z.so` |
| `005b0719e000-005b0719f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libhash.z.so` |
| `005b071c0000-005b071c8000` | .so | `r--p` | 32 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libpicker.z.so` |
| `005b071c8000-005b071e8000` | .so | `r-xp` | 128 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libpicker.z.so` |
| `005b071e8000-005b071eb000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libpicker.z.so` |
| `005b071eb000-005b071f7000` | .so | `rw-p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/file/libpicker.z.so` |
| `005b071f7000-005b071f8000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libpicker.z.so.bss]` |
| `005b07200000-005b07206000` | .so | `r--p` | 24 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libremote_uri_native.z.so` |
| `005b07206000-005b07210000` | .so | `r-xp` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libremote_uri_native.z.so` |
| `005b07210000-005b07211000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libremote_uri_native.z.so` |
| `005b07211000-005b07212000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libremote_uri_native.z.so` |
| `005b07212000-005b07213000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libremote_uri_native.z.so.bss]` |
| `005b07240000-005b0725a000` | .so | `r--p` | 104 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libfileio.z.so` |
| `005b0725a000-005b072bd000` | .so | `r-xp` | 396 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libfileio.z.so` |
| `005b072bd000-005b072c1000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libfileio.z.so` |
| `005b072c1000-005b072c2000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libfileio.z.so` |
| `005b072c2000-005b072c3000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libfileio.z.so.bss]` |
| `005b07300000-005b07304000` | .so | `r--p` | 16 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libhiappevent.z.so` |
| `005b07304000-005b0730d000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libhiappevent.z.so` |
| `005b0730d000-005b0730e000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libhiappevent.z.so` |
| `005b0730e000-005b0730f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libhiappevent.z.so` |
| `005b0730f000-005b07310000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libhiappevent.z.so.bss]` |
| `005b07340000-005b07342000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libhitracemeter_napi.z.so` |
| `005b07342000-005b07345000` | .so | `r-xp` | 12 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libhitracemeter_napi.z.so` |
| `005b07345000-005b07346000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libhitracemeter_napi.z.so` |
| `005b07346000-005b07347000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libhitracemeter_napi.z.so` |
| `005b07380000-005b0738d000` | .so | `r--p` | 52 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/hiviewdfx/libhiappevent_napi.z.so` |
| `005b0738d000-005b073b2000` | .so | `r-xp` | 148 | 92 | 14 | 0 | 0 | 0.00% | `/system/lib64/module/hiviewdfx/libhiappevent_napi.z.so` |
| `005b073b2000-005b073b4000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hiviewdfx/libhiappevent_napi.z.so` |
| `005b073b4000-005b073b5000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hiviewdfx/libhiappevent_napi.z.so` |
| `005b073b5000-005b073b7000` | FilePage other | `rw-p` | 8 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libhiappevent_napi.z.so.bss]` |
| `005b073c0000-005b073d1000` | .so | `r--p` | 68 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/libauthentication.z.so` |
| `005b073d1000-005b073f6000` | .so | `r-xp` | 148 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/libauthentication.z.so` |
| `005b073f6000-005b073f9000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/libauthentication.z.so` |
| `005b073f9000-005b073fc000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/libauthentication.z.so` |
| `005b073fc000-005b073fd000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libauthentication.z.so.bss]` |
| `005b07400000-005b07415000` | .so | `r--p` | 84 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_innerkits_ndk.z.so` |
| `005b07415000-005b0744a000` | .so | `r-xp` | 212 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_innerkits_ndk.z.so` |
| `005b0744a000-005b0744e000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_innerkits_ndk.z.so` |
| `005b0744e000-005b0744f000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_innerkits_ndk.z.so` |
| `005b07480000-005b07494000` | .so | `r--p` | 80 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_napi_base.z.so` |
| `005b07494000-005b074ba000` | .so | `r-xp` | 152 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_napi_base.z.so` |
| `005b074ba000-005b074be000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_napi_base.z.so` |
| `005b074be000-005b074bf000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_napi_base.z.so` |
| `005b074bf000-005b074c0000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libhuaweiid_napi_base.z.so.bss]` |
| `005b074c0000-005b074cc000` | .so | `r--p` | 48 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_native_base.z.so` |
| `005b074cc000-005b074e4000` | .so | `r-xp` | 96 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_native_base.z.so` |
| `005b074e4000-005b074e7000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_native_base.z.so` |
| `005b074e7000-005b074e8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_native_base.z.so` |
| `005b07500000-005b07514000` | .so | `r--p` | 80 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_sa_client.z.so` |
| `005b07514000-005b07547000` | .so | `r-xp` | 204 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_sa_client.z.so` |
| `005b07547000-005b0754a000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_sa_client.z.so` |
| `005b0754a000-005b0754b000` | .so | `rw-p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libhuaweiid_sa_client.z.so` |
| `005b07580000-005b0758e000` | .so | `r--p` | 56 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_bsl.z.so` |
| `005b0758e000-005b075a0000` | .so | `r-xp` | 72 | 28 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_bsl.z.so` |
| `005b075a0000-005b075a2000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_bsl.z.so` |
| `005b075a2000-005b075a5000` | .so | `rw-p` | 12 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_bsl.z.so` |
| `005b075c0000-005b075c7000` | .so | `r--p` | 28 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnetwork_profiler.z.so` |
| `005b075c7000-005b075d7000` | .so | `r-xp` | 64 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnetwork_profiler.z.so` |
| `005b075d7000-005b075d8000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnetwork_profiler.z.so` |
| `005b075d8000-005b075d9000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnetwork_profiler.z.so` |
| `005b07600000-005b07612000` | .so | `r--p` | 72 | 12 | 3 | 0 | 0 | 0.00% | `/system/lib64/libha_client_expand.z.so` |
| `005b07612000-005b0763c000` | .so | `r-xp` | 168 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libha_client_expand.z.so` |
| `005b0763c000-005b07642000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libha_client_expand.z.so` |
| `005b07642000-005b07643000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libha_client_expand.z.so` |
| `005b07643000-005b07645000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libha_client_expand.z.so.bss]` |
| `005b07680000-005b0769c000` | .so | `r--p` | 112 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_tls.z.so` |
| `005b0769c000-005b076c3000` | .so | `r-xp` | 156 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_tls.z.so` |
| `005b076c3000-005b076c6000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_tls.z.so` |
| `005b076c6000-005b076c7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_tls.z.so` |
| `005b07700000-005b07713000` | .so | `r--p` | 76 | 20 | 3 | 0 | 0 | 0.00% | `/system/lib64/libha_ace_engine.z.so` |
| `005b07713000-005b0775f000` | .so | `r-xp` | 304 | 88 | 4 | 0 | 0 | 0.00% | `/system/lib64/libha_ace_engine.z.so` |
| `005b0775f000-005b07762000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/libha_ace_engine.z.so` |
| `005b07762000-005b07763000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libha_ace_engine.z.so` |
| `005b07763000-005b07766000` | FilePage other | `rw-p` | 12 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libha_ace_engine.z.so.bss]` |
| `005b07780000-005b0778c000` | .so | `r--p` | 48 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_pki.z.so` |
| `005b0778c000-005b077ab000` | .so | `r-xp` | 124 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_pki.z.so` |
| `005b077ab000-005b077ad000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_pki.z.so` |
| `005b077ad000-005b077af000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_pki.z.so` |
| `005b077c0000-005b077ce000` | .so | `r--p` | 56 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/libhianalytics_napi.z.so` |
| `005b077ce000-005b077fa000` | .so | `r-xp` | 176 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/libhianalytics_napi.z.so` |
| `005b077fa000-005b077fc000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/libhianalytics_napi.z.so` |
| `005b077fc000-005b077fd000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/libhianalytics_napi.z.so` |
| `005b077fd000-005b077ff000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libhianalytics_napi.z.so.bss]` |
| `005b07800000-005b0780b000` | .so | `r--p` | 44 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/librcp_network_listener.z.so` |
| `005b0780b000-005b07814000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librcp_network_listener.z.so` |
| `005b07814000-005b07819000` | .so | `r--p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librcp_network_listener.z.so` |
| `005b07819000-005b0781a000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librcp_network_listener.z.so` |
| `005b07840000-005b07854000` | .so | `r--p` | 80 | 40 | 3 | 0 | 0 | 0.00% | `/system/lib64/libnetmanager_enhanced_service_if.z.so` |
| `005b07854000-005b0786f000` | .so | `r-xp` | 108 | 44 | 2 | 0 | 0 | 0.00% | `/system/lib64/libnetmanager_enhanced_service_if.z.so` |
| `005b0786f000-005b0787b000` | .so | `r--p` | 48 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/libnetmanager_enhanced_service_if.z.so` |
| `005b0787b000-005b0787c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnetmanager_enhanced_service_if.z.so` |
| `005b07880000-005b078b6000` | .so | `r--p` | 216 | 100 | 7 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcurl_shared_http3.z.so` |
| `005b07955000-005b0795b000` | .so | `r--p` | 24 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcurl_shared_http3.z.so` |
| `005b0795b000-005b0795e000` | .so | `rw-p` | 12 | 8 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcurl_shared_http3.z.so` |
| `005b07980000-005b079a4000` | .so | `r--p` | 144 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcrypto_openssl_plugin_lib.z.so` |
| `005b079a4000-005b079e7000` | .so | `r-xp` | 268 | 52 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcrypto_openssl_plugin_lib.z.so` |
| `005b079e7000-005b079ea000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcrypto_openssl_plugin_lib.z.so` |
| `005b079ea000-005b079ec000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcrypto_openssl_plugin_lib.z.so` |
| `005b07a00000-005b07a0a000` | .so | `r--p` | 40 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcrypto_framework_lib.z.so` |
| `005b07a0a000-005b07a1b000` | .so | `r-xp` | 68 | 40 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcrypto_framework_lib.z.so` |
| `005b07a1b000-005b07a1d000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcrypto_framework_lib.z.so` |
| `005b07a1d000-005b07a1e000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcrypto_framework_lib.z.so` |
| `005b07a40000-005b07aae000` | .so | `r--p` | 440 | 132 | 9 | 0 | 0 | 0.00% | `/system/lib64/libcollaboration_rcp_native.z.so` |
| `005b07aae000-005b07b1b000` | .so | `r-xp` | 436 | 68 | 2 | 0 | 0 | 0.00% | `/system/lib64/libcollaboration_rcp_native.z.so` |
| `005b07b1b000-005b07b24000` | .so | `r--p` | 36 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcollaboration_rcp_native.z.so` |
| `005b07b24000-005b07b25000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libcollaboration_rcp_native.z.so` |
| `005b07b25000-005b07b26000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libcollaboration_rcp_native.z.so.bss]` |
| `005b07b40000-005b07b4f000` | .so | `r--p` | 60 | 32 | 2 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libnghttp2_shared.z.so` |
| `005b07b4f000-005b07b62000` | .so | `r-xp` | 76 | 76 | 4 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libnghttp2_shared.z.so` |
| `005b07b62000-005b07b65000` | .so | `r--p` | 12 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libnghttp2_shared.z.so` |
| `005b07b65000-005b07b66000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libnghttp2_shared.z.so` |
| `005b07b80000-005b07bde000` | .so | `r--p` | 376 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_crypto.z.so` |
| `005b07bde000-005b07c74000` | .so | `r-xp` | 600 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_crypto.z.so` |
| `005b07c74000-005b07c78000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_crypto.z.so` |
| `005b07c78000-005b07c7a000` | .so | `rw-p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopenhitls_crypto.z.so` |
| `005b07c80000-005b07c84000` | .so | `r--p` | 16 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_interceptor.z.so` |
| `005b07c84000-005b07c8a000` | .so | `r-xp` | 24 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_interceptor.z.so` |
| `005b07c8a000-005b07c8b000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_interceptor.z.so` |
| `005b07c8b000-005b07c8c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_interceptor.z.so` |
| `005b07c8c000-005b07c8d000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libhttp_interceptor.z.so.bss]` |
| `005b07cc0000-005b07cc4000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/librcp_dfx.z.so` |
| `005b07cc4000-005b07cc7000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librcp_dfx.z.so` |
| `005b07cc7000-005b07cc8000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librcp_dfx.z.so` |
| `005b07cc8000-005b07cc9000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/librcp_dfx.z.so` |
| `005b07d00000-005b07d72000` | .so | `r--p` | 456 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libbrotli_shared.z.so` |
| `005b07d72000-005b07db9000` | .so | `r-xp` | 284 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libbrotli_shared.z.so` |
| `005b07db9000-005b07dbb000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libbrotli_shared.z.so` |
| `005b07dbb000-005b07dbc000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libbrotli_shared.z.so` |
| `005b07dc0000-005b07de2000` | .so | `r--p` | 136 | 64 | 3 | 0 | 0 | 0.00% | `/system/lib64/libha_client_core.z.so` |
| `005b07de2000-005b07e59000` | .so | `r-xp` | 476 | 476 | 42 | 0 | 0 | 0.00% | `/system/lib64/libha_client_core.z.so` |
| `005b07e59000-005b07e5e000` | .so | `r--p` | 20 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/libha_client_core.z.so` |
| `005b07e5e000-005b07e5f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libha_client_core.z.so` |
| `005b07e5f000-005b07e63000` | FilePage other | `rw-p` | 16 | 16 | 9 | 0 | 0 | 0.00% | `[anon:libha_client_core.z.so.bss]` |
| `005b07e80000-005b07e83000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnetsys_client.z.so` |
| `005b07e83000-005b07e88000` | .so | `r-xp` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnetsys_client.z.so` |
| `005b07e88000-005b07e89000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnetsys_client.z.so` |
| `005b07e89000-005b07e8a000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnetsys_client.z.so` |
| `005b07e8a000-005b07f09000` | FilePage other | `rw-p` | 508 | 508 | 508 | 0 | 0 | 0.00% | `[anon:libnetsys_client.z.so.bss]` |
| `005b07f40000-005b07f47000` | .so | `r--p` | 28 | 28 | 3 | 0 | 0 | 0.00% | `/system/lib64/libha_client.z.so` |
| `005b07f47000-005b07f5b000` | .so | `r-xp` | 80 | 80 | 6 | 0 | 0 | 0.00% | `/system/lib64/libha_client.z.so` |
| `005b07f5b000-005b07f5d000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libha_client.z.so` |
| `005b07f5d000-005b07f5e000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libha_client.z.so` |
| `005b07f5e000-005b07f60000` | FilePage other | `rw-p` | 8 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libha_client.z.so.bss]` |
| `005b07f80000-005b07f9a000` | .so | `r--p` | 104 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_napi.z.so` |
| `005b07f9a000-005b07fc0000` | .so | `r-xp` | 152 | 72 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_napi.z.so` |
| `005b07fc0000-005b07fc3000` | .so | `r--p` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_napi.z.so` |
| `005b07fc3000-005b07fc4000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libintl_napi.z.so` |
| `005b08000000-005b0800a000` | .so | `r--p` | 40 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libi18n_sa_client.z.so` |
| `005b0800a000-005b08017000` | .so | `r-xp` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libi18n_sa_client.z.so` |
| `005b08017000-005b0801b000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libi18n_sa_client.z.so` |
| `005b0801b000-005b0801c000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libi18n_sa_client.z.so` |
| `005b08040000-005b0805d000` | .so | `r--p` | 116 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libi18n.z.so` |
| `005b0805d000-005b08094000` | .so | `r-xp` | 220 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libi18n.z.so` |
| `005b08094000-005b08098000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libi18n.z.so` |
| `005b08098000-005b08099000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libi18n.z.so` |
| `005b08099000-005b0809a000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libi18n.z.so.bss]` |
| `005b080c0000-005b080c2000` | .so | `r--p` | 8 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/identifier/liboaid.z.so` |
| `005b080c2000-005b080c6000` | .so | `r-xp` | 16 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/identifier/liboaid.z.so` |
| `005b080c6000-005b080c7000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/identifier/liboaid.z.so` |
| `005b080c7000-005b080c8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/identifier/liboaid.z.so` |
| `005b08100000-005b08106000` | .so | `r--p` | 24 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liboaid_client.z.so` |
| `005b08106000-005b0810e000` | .so | `r-xp` | 32 | 28 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liboaid_client.z.so` |
| `005b0810e000-005b08112000` | .so | `r--p` | 16 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liboaid_client.z.so` |
| `005b08112000-005b08113000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/liboaid_client.z.so` |
| `005b08140000-005b0815a000` | .so | `r--p` | 104 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libinputmethod.z.so` |
| `005b0815a000-005b08199000` | .so | `r-xp` | 252 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libinputmethod.z.so` |
| `005b08199000-005b0819f000` | .so | `r--p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libinputmethod.z.so` |
| `005b0819f000-005b081a0000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libinputmethod.z.so` |
| `005b081a0000-005b081a1000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libinputmethod.z.so.bss]` |
| `005b081c0000-005b081c1000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libintl.z.so` |
| `005b081c1000-005b081c2000` | .so | `r-xp` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libintl.z.so` |
| `005b081c2000-005b081c3000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libintl.z.so` |
| `005b081c3000-005b081c4000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libintl.z.so` |
| `005b08200000-005b08207000` | .so | `r--p` | 28 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libmeasure.z.so` |
| `005b08207000-005b0821f000` | .so | `r-xp` | 96 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libmeasure.z.so` |
| `005b0821f000-005b08221000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libmeasure.z.so` |
| `005b08221000-005b08222000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libmeasure.z.so` |
| `005b08222000-005b08223000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libmeasure.z.so.bss]` |
| `005b08240000-005b08247000` | .so | `r--p` | 28 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_toneplayer.z.so` |
| `005b08247000-005b08250000` | .so | `r-xp` | 36 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_toneplayer.z.so` |
| `005b08250000-005b08252000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_toneplayer.z.so` |
| `005b08252000-005b08253000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_toneplayer.z.so` |
| `005b08280000-005b08288000` | .so | `r--p` | 32 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_loopback.z.so` |
| `005b08288000-005b08295000` | .so | `r-xp` | 52 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_loopback.z.so` |
| `005b08295000-005b08297000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_loopback.z.so` |
| `005b08297000-005b08298000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libaudio_loopback.z.so` |
| `005b08298000-005b08299000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libaudio_loopback.z.so.bss]` |
| `005b082c0000-005b08303000` | .so | `r--p` | 268 | 68 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_core_service_api.z.so` |
| `005b08303000-005b08384000` | .so | `r-xp` | 516 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_core_service_api.z.so` |
| `005b08384000-005b08390000` | .so | `r--p` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_core_service_api.z.so` |
| `005b08390000-005b08391000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_core_service_api.z.so` |
| `005b08391000-005b08392000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libtel_core_service_api.z.so.bss]` |
| `005b083c0000-005b08414000` | .so | `r--p` | 336 | 192 | 61 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libaudio.z.so` |
| `005b08414000-005b08555000` | .so | `r-xp` | 1284 | 784 | 329 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libaudio.z.so` |
| `005b08555000-005b0856a000` | .so | `r--p` | 84 | 52 | 11 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libaudio.z.so` |
| `005b0856a000-005b0856b000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libaudio.z.so` |
| `005b0856b000-005b08572000` | FilePage other | `rw-p` | 28 | 12 | 9 | 0 | 0 | 0.00% | `[anon:libaudio.z.so.bss]` |
| `005b08580000-005b08588000` | .so | `r--p` | 32 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_cellular_data_api.z.so` |
| `005b08588000-005b0859d000` | .so | `r-xp` | 84 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_cellular_data_api.z.so` |
| `005b0859d000-005b0859f000` | .so | `r--p` | 8 | 8 | 6 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_cellular_data_api.z.so` |
| `005b0859f000-005b085a0000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_cellular_data_api.z.so` |
| `005b085a0000-005b085a1000` | FilePage other | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libtel_cellular_data_api.z.so.bss]` |
| `005b085c0000-005b085e5000` | .so | `r--p` | 148 | 76 | 9 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcurl_shared.z.so` |
| `005b085e5000-005b08660000` | .so | `r-xp` | 492 | 376 | 40 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcurl_shared.z.so` |
| `005b08660000-005b08664000` | .so | `r--p` | 16 | 16 | 3 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcurl_shared.z.so` |
| `005b08664000-005b08668000` | .so | `rw-p` | 16 | 16 | 10 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcurl_shared.z.so` |
| `005b08680000-005b08699000` | .so | `r--p` | 100 | 64 | 10 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_common.z.so` |
| `005b08699000-005b086ba000` | .so | `r-xp` | 132 | 76 | 12 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_common.z.so` |
| `005b086ba000-005b086be000` | .so | `r--p` | 16 | 16 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_common.z.so` |
| `005b086be000-005b086bf000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_common.z.so` |
| `005b086c0000-005b086dc000` | .so | `r--p` | 112 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/libidl_avsession_service_interface_stub.z.so` |
| `005b086dc000-005b086ff000` | .so | `r-xp` | 140 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libidl_avsession_service_interface_stub.z.so` |
| `005b086ff000-005b08707000` | .so | `r--p` | 32 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libidl_avsession_service_interface_stub.z.so` |
| `005b08707000-005b08708000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libidl_avsession_service_interface_stub.z.so` |
| `005b08740000-005b08788000` | .so | `r--p` | 288 | 152 | 33 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavsession_napi.z.so` |
| `005b08788000-005b0887c000` | .so | `r-xp` | 976 | 508 | 138 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavsession_napi.z.so` |
| `005b0887c000-005b0888c000` | .so | `r--p` | 64 | 44 | 9 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavsession_napi.z.so` |
| `005b0888c000-005b0888d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavsession_napi.z.so` |
| `005b0888d000-005b08890000` | FilePage other | `rw-p` | 12 | 8 | 4 | 0 | 0 | 0.00% | `[anon:libavsession_napi.z.so.bss]` |
| `005b088c0000-005b088f7000` | .so | `r--p` | 220 | 144 | 18 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_client.z.so` |
| `005b088f7000-005b08959000` | .so | `r-xp` | 392 | 328 | 74 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_client.z.so` |
| `005b08959000-005b08967000` | .so | `r--p` | 56 | 44 | 7 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_client.z.so` |
| `005b08967000-005b08968000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_client.z.so` |
| `005b08980000-005b08989000` | .so | `r--p` | 36 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_cast_client.z.so` |
| `005b08989000-005b08999000` | .so | `r-xp` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_cast_client.z.so` |
| `005b08999000-005b0899c000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_cast_client.z.so` |
| `005b0899c000-005b0899d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_cast_client.z.so` |
| `005b089c0000-005b089cd000` | .so | `r--p` | 52 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_utils.z.so` |
| `005b089cd000-005b089f4000` | .so | `r-xp` | 156 | 12 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_utils.z.so` |
| `005b089f4000-005b089f6000` | .so | `r--p` | 8 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_utils.z.so` |
| `005b089f6000-005b089f7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libavsession_utils.z.so` |
| `005b08a00000-005b08a6e000` | .so | `r--p` | 440 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libcamera_napi_base.z.so` |
| `005b08a6e000-005b08b44000` | .so | `r-xp` | 856 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcamera_napi_base.z.so` |
| `005b08b44000-005b08b53000` | .so | `r--p` | 60 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcamera_napi_base.z.so` |
| `005b08b53000-005b08b54000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcamera_napi_base.z.so` |
| `005b08b54000-005b08b59000` | FilePage other | `rw-p` | 20 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libcamera_napi_base.z.so.bss]` |
| `005b08b80000-005b08c81000` | .so | `r--p` | 1028 | 176 | 22 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcamera_framework.z.so` |
| `005b08c81000-005b08e48000` | .so | `r-xp` | 1820 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcamera_framework.z.so` |
| `005b08e48000-005b08e86000` | .so | `r--p` | 248 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcamera_framework.z.so` |
| `005b08e86000-005b08e87000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcamera_framework.z.so` |
| `005b08e87000-005b08e8e000` | FilePage other | `rw-p` | 28 | 4 | 0 | 0 | 0 | 0.00% | `[anon:libcamera_framework.z.so.bss]` |
| `005b08ec0000-005b09012000` | .so | `r--p` | 1352 | 268 | 45 | 0 | 0 | 0.00% | `/system/lib64/libmedialibrary_nutils.z.so` |
| `005b09012000-005b094af000` | .so | `r-xp` | 4724 | 212 | 43 | 0 | 0 | 0.00% | `/system/lib64/libmedialibrary_nutils.z.so` |
| `005b094af000-005b094c8000` | .so | `r--p` | 100 | 60 | 3 | 0 | 0 | 0.00% | `/system/lib64/libmedialibrary_nutils.z.so` |
| `005b094c8000-005b094ca000` | .so | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libmedialibrary_nutils.z.so` |
| `005b094ca000-005b09536000` | FilePage other | `rw-p` | 432 | 88 | 5 | 0 | 0 | 0.00% | `[anon:libmedialibrary_nutils.z.so.bss]` |
| `005b09540000-005b0959c000` | .so | `r--p` | 368 | 40 | 8 | 0 | 0 | 0.00% | `/system/lib64/libcamera_utils.z.so` |
| `005b0959c000-005b0962a000` | .so | `r-xp` | 568 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcamera_utils.z.so` |
| `005b0962a000-005b09645000` | .so | `r--p` | 108 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcamera_utils.z.so` |
| `005b09645000-005b09646000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libcamera_utils.z.so` |
| `005b09646000-005b09648000` | FilePage other | `rw-p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `[anon:libcamera_utils.z.so.bss]` |
| `005b09680000-005b09696000` | .so | `r--p` | 88 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdm_lite.z.so` |
| `005b09696000-005b096b5000` | .so | `r-xp` | 124 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdm_lite.z.so` |
| `005b096b5000-005b096c6000` | .so | `r--p` | 68 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdm_lite.z.so` |
| `005b096c6000-005b096c7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libdm_lite.z.so` |
| `005b09700000-005b09701000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcamera_vendor_tag_proxy_1.0.z.so` |
| `005b09701000-005b09703000` | .so | `r-xp` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcamera_vendor_tag_proxy_1.0.z.so` |
| `005b09703000-005b09704000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcamera_vendor_tag_proxy_1.0.z.so` |
| `005b09704000-005b09705000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libcamera_vendor_tag_proxy_1.0.z.so` |
| `005b09740000-005b0974b000` | .so | `r--p` | 44 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libmetadata.z.so` |
| `005b0974b000-005b09757000` | .so | `r-xp` | 48 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libmetadata.z.so` |
| `005b09757000-005b09759000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libmetadata.z.so` |
| `005b09759000-005b0975b000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libmetadata.z.so` |
| `005b09780000-005b09784000` | .so | `r--p` | 16 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libcamera_napi.z.so` |
| `005b09784000-005b0978f000` | .so | `r-xp` | 44 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libcamera_napi.z.so` |
| `005b0978f000-005b09790000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libcamera_napi.z.so` |
| `005b09790000-005b09791000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libcamera_napi.z.so` |
| `005b09791000-005b09792000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libcamera_napi.z.so.bss]` |
| `005b097c0000-005b097c2000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libimage.z.so` |
| `005b097c2000-005b097c5000` | .so | `r-xp` | 12 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libimage.z.so` |
| `005b097c5000-005b097c6000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libimage.z.so` |
| `005b097c6000-005b097c7000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libimage.z.so` |
| `005b09800000-005b09827000` | .so | `r--p` | 156 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libmedia.z.so` |
| `005b09827000-005b098cd000` | .so | `r-xp` | 664 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libmedia.z.so` |
| `005b098cd000-005b098d7000` | .so | `r--p` | 40 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libmedia.z.so` |
| `005b098d7000-005b098d8000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libmedia.z.so` |
| `005b098d8000-005b098db000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libmedia.z.so.bss]` |
| `005b09900000-005b09910000` | .so | `r--p` | 64 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_soundpool.z.so` |
| `005b09910000-005b0992f000` | .so | `r-xp` | 124 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_soundpool.z.so` |
| `005b0992f000-005b09931000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_soundpool.z.so` |
| `005b09931000-005b09932000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_soundpool.z.so` |
| `005b09940000-005b09968000` | .so | `r--p` | 160 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_avplayer.z.so` |
| `005b09968000-005b099bd000` | .so | `r-xp` | 340 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_avplayer.z.so` |
| `005b099bd000-005b099c4000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_avplayer.z.so` |
| `005b099c4000-005b099c5000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libmedia_avplayer.z.so` |
| `005b09a00000-005b09a0a000` | .so | `r--p` | 40 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimodalinput/libinputdevice.z.so` |
| `005b09a0a000-005b09a41000` | .so | `r-xp` | 220 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimodalinput/libinputdevice.z.so` |
| `005b09a41000-005b09a43000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimodalinput/libinputdevice.z.so` |
| `005b09a43000-005b09a44000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/multimodalinput/libinputdevice.z.so` |
| `005b09a80000-005b09a82000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_wantagent_common.z.so` |
| `005b09a82000-005b09a86000` | .so | `r-xp` | 16 | 16 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_wantagent_common.z.so` |
| `005b09a86000-005b09a87000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_wantagent_common.z.so` |
| `005b09a87000-005b09a88000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnapi_wantagent_common.z.so` |
| `005b09ac0000-005b09b02000` | .so | `r--p` | 264 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libnotificationmanager.z.so` |
| `005b09b02000-005b09b74000` | .so | `r-xp` | 456 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libnotificationmanager.z.so` |
| `005b09b74000-005b09b7b000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libnotificationmanager.z.so` |
| `005b09b7b000-005b09b7c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libnotificationmanager.z.so` |
| `005b09b7c000-005b09b7e000` | FilePage other | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libnotificationmanager.z.so.bss]` |
| `005b09b80000-005b09b99000` | .so | `r--p` | 100 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libpasteboard_napi.z.so` |
| `005b09b99000-005b09bdd000` | .so | `r-xp` | 272 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libpasteboard_napi.z.so` |
| `005b09bdd000-005b09be4000` | .so | `r--p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libpasteboard_napi.z.so` |
| `005b09be4000-005b09be6000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libpasteboard_napi.z.so` |
| `005b09c00000-005b09c05000` | .so | `r--p` | 20 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libprocess.z.so` |
| `005b09c05000-005b09c11000` | .so | `r-xp` | 48 | 48 | 6 | 0 | 0 | 0.00% | `/system/lib64/module/libprocess.z.so` |
| `005b09c11000-005b09c13000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libprocess.z.so` |
| `005b09c13000-005b09c14000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libprocess.z.so` |
| `005b09c40000-005b09c5b000` | .so | `r--p` | 108 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/librequest.z.so` |
| `005b09c5b000-005b09cb4000` | .so | `r-xp` | 356 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librequest.z.so` |
| `005b09cb4000-005b09cb8000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librequest.z.so` |
| `005b09cb8000-005b09cba000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librequest.z.so` |
| `005b09cba000-005b09cbb000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:librequest.z.so.bss]` |
| `005b09cc0000-005b09cd9000` | .so | `r--p` | 100 | 20 | 3 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librequest_native.z.so` |
| `005b09cd9000-005b09d03000` | .so | `r-xp` | 168 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librequest_native.z.so` |
| `005b09d03000-005b09d07000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librequest_native.z.so` |
| `005b09d07000-005b09d08000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/librequest_native.z.so` |
| `005b09d40000-005b09d44000` | .so | `r--p` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libresourcemanager.z.so` |
| `005b09d44000-005b09d4a000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libresourcemanager.z.so` |
| `005b09d4a000-005b09d4b000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libresourcemanager.z.so` |
| `005b09d4b000-005b09d4c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libresourcemanager.z.so` |
| `005b09d4c000-005b09d4d000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libresourcemanager.z.so.bss]` |
| `005b09d80000-005b09d86000` | .so | `r--p` | 24 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/librouter.z.so` |
| `005b09d86000-005b09d99000` | .so | `r-xp` | 76 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librouter.z.so` |
| `005b09d99000-005b09d9b000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librouter.z.so` |
| `005b09d9b000-005b09d9c000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/librouter.z.so` |
| `005b09dc0000-005b09dd4000` | .so | `r--p` | 80 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/security/libcert.z.so` |
| `005b09dd4000-005b09e29000` | .so | `r-xp` | 340 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libcert.z.so` |
| `005b09e29000-005b09e2c000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libcert.z.so` |
| `005b09e2c000-005b09e2d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libcert.z.so` |
| `005b09e2d000-005b09e3d000` | FilePage other | `rw-p` | 64 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libcert.z.so.bss]` |
| `005b09e40000-005b09e66000` | .so | `r--p` | 152 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcertificate_framework_core.z.so` |
| `005b09e66000-005b09ea7000` | .so | `r-xp` | 260 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcertificate_framework_core.z.so` |
| `005b09ea7000-005b09eaa000` | .so | `r--p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcertificate_framework_core.z.so` |
| `005b09eaa000-005b09eab000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libcertificate_framework_core.z.so` |
| `005b09ec0000-005b09ed1000` | .so | `r--p` | 68 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/security/libcryptoframework_napi.z.so` |
| `005b09ed1000-005b09f0f000` | .so | `r-xp` | 248 | 72 | 6 | 0 | 0 | 0.00% | `/system/lib64/module/security/libcryptoframework_napi.z.so` |
| `005b09f0f000-005b09f12000` | .so | `r--p` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libcryptoframework_napi.z.so` |
| `005b09f12000-005b09f13000` | .so | `rw-p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libcryptoframework_napi.z.so` |
| `005b09f13000-005b09f1c000` | FilePage other | `rw-p` | 36 | 12 | 1 | 0 | 0 | 0.00% | `[anon:libcryptoframework_napi.z.so.bss]` |
| `005b09f40000-005b09f4d000` | .so | `r--p` | 52 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libhuks.z.so` |
| `005b09f4d000-005b09f76000` | .so | `r-xp` | 164 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libhuks.z.so` |
| `005b09f76000-005b09f78000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libhuks.z.so` |
| `005b09f78000-005b09f7a000` | .so | `rw-p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/security/libhuks.z.so` |
| `005b09f7a000-005b09f7d000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libhuks.z.so.bss]` |
| `005b09f80000-005b09f90000` | .so | `r--p` | 64 | 28 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsensor_client.z.so` |
| `005b0a000000-005b0a005000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsensor_agent.z.so` |
| `005b0a00c000-005b0a00e000` | .so | `r--p` | 8 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsensor_agent.z.so` |
| `005b0a00e000-005b0a00f000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsensor_agent.z.so` |
| `005b0a080000-005b0a085000` | .so | `r--p` | 20 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsensor_ipc.z.so` |
| `005b0a085000-005b0a08b000` | .so | `r-xp` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsensor_ipc.z.so` |
| `005b0a08b000-005b0a08c000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsensor_ipc.z.so` |
| `005b0a08c000-005b0a08d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libsensor_ipc.z.so` |
| `005b0a0c0000-005b0a0c4000` | .so | `r--p` | 16 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libsettings_common.z.so` |
| `005b0a0c4000-005b0a0c8000` | .so | `r-xp` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsettings_common.z.so` |
| `005b0a0c8000-005b0a0ca000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsettings_common.z.so` |
| `005b0a0ca000-005b0a0cb000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libsettings_common.z.so` |
| `005b0a130000-005b0a131000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libsettings.z.so.bss]` |
| `005b0a140000-005b0a146000` | .so | `r--p` | 24 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libsystemdatetime.z.so` |
| `005b0a146000-005b0a151000` | .so | `r-xp` | 44 | 40 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/libsystemdatetime.z.so` |
| `005b0a151000-005b0a153000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libsystemdatetime.z.so` |
| `005b0a153000-005b0a154000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libsystemdatetime.z.so` |
| `005b0a180000-005b0a194000` | .so | `r--p` | 80 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libradio.z.so` |
| `005b0a194000-005b0a1c2000` | .so | `r-xp` | 184 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libradio.z.so` |
| `005b0a1c2000-005b0a1d2000` | .so | `r--p` | 64 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libradio.z.so` |
| `005b0a1d2000-005b0a1d3000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libradio.z.so` |
| `005b0a1d3000-005b0a1d4000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libradio.z.so.bss]` |
| `005b0a200000-005b0a210000` | .so | `r--p` | 64 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_common.z.so` |
| `005b0a210000-005b0a230000` | .so | `r-xp` | 128 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_common.z.so` |
| `005b0a230000-005b0a232000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_common.z.so` |
| `005b0a232000-005b0a233000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libtel_common.z.so` |
| `005b0a233000-005b0a234000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libtel_common.z.so.bss]` |
| `005b0a240000-005b0a24b000` | .so | `r--p` | 44 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libsim.z.so` |
| `005b0a24b000-005b0a273000` | .so | `r-xp` | 160 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libsim.z.so` |
| `005b0a273000-005b0a275000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libsim.z.so` |
| `005b0a275000-005b0a276000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/telephony/libsim.z.so` |
| `005b0a276000-005b0a277000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libsim.z.so.bss]` |
| `005b0a280000-005b0a285000` | .so | `r--p` | 20 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/liburi.z.so` |
| `005b0a285000-005b0a29b000` | .so | `r-xp` | 88 | 72 | 9 | 0 | 0 | 0.00% | `/system/lib64/module/liburi.z.so` |
| `005b0a29b000-005b0a29d000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/liburi.z.so` |
| `005b0a29d000-005b0a2a5000` | .so | `rw-p` | 32 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/liburi.z.so` |
| `005b0a2c0000-005b0a2c8000` | .so | `r--p` | 32 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/liburl.z.so` |
| `005b0a2c8000-005b0a2f3000` | .so | `r-xp` | 172 | 80 | 5 | 0 | 0 | 0.00% | `/system/lib64/module/liburl.z.so` |
| `005b0a2f3000-005b0a2f5000` | .so | `r--p` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/liburl.z.so` |
| `005b0a2f5000-005b0a301000` | .so | `rw-p` | 48 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/liburl.z.so` |
| `005b0a380000-005b0a381000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libarraylist.z.so` |
| `005b0a381000-005b0a384000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libarraylist.z.so` |
| `005b0a384000-005b0a385000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libarraylist.z.so` |
| `005b0a385000-005b0a38b000` | .so | `rw-p` | 24 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libarraylist.z.so` |
| `005b0a3c0000-005b0a3c1000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/util/libhashmap.z.so` |
| `005b0a3c1000-005b0a3c4000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libhashmap.z.so` |
| `005b0a3c4000-005b0a3c5000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libhashmap.z.so` |
| `005b0a3c5000-005b0a3c8000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libhashmap.z.so` |
| `005b0a400000-005b0a401000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/util/libhashset.z.so` |
| `005b0a401000-005b0a404000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libhashset.z.so` |
| `005b0a404000-005b0a405000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libhashset.z.so` |
| `005b0a405000-005b0a408000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libhashset.z.so` |
| `005b0a440000-005b0a441000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/liblist.z.so` |
| `005b0a441000-005b0a444000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/liblist.z.so` |
| `005b0a444000-005b0a445000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/liblist.z.so` |
| `005b0a445000-005b0a44c000` | .so | `rw-p` | 28 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/liblist.z.so` |
| `005b0a480000-005b0a481000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/util/libqueue.z.so` |
| `005b0a481000-005b0a484000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libqueue.z.so` |
| `005b0a484000-005b0a485000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libqueue.z.so` |
| `005b0a485000-005b0a488000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libqueue.z.so` |
| `005b0a4c0000-005b0a4c1000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/util/libjson.z.so` |
| `005b0a4c1000-005b0a4c4000` | .so | `r-xp` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libjson.z.so` |
| `005b0a4c4000-005b0a4c5000` | .so | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libjson.z.so` |
| `005b0a4c5000-005b0a4c8000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/util/libjson.z.so` |
| `005b0a500000-005b0a508000` | .so | `r--p` | 32 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libvibrator.z.so` |
| `005b0a508000-005b0a51e000` | .so | `r-xp` | 88 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libvibrator.z.so` |
| `005b0a51e000-005b0a520000` | .so | `r--p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libvibrator.z.so` |
| `005b0a520000-005b0a521000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libvibrator.z.so` |
| `005b0a540000-005b0a552000` | .so | `r--p` | 72 | 12 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/libwindow_napi.z.so` |
| `005b0a552000-005b0a577000` | .so | `r-xp` | 148 | 20 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/libwindow_napi.z.so` |
| `005b0a577000-005b0a57c000` | .so | `r--p` | 20 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libwindow_napi.z.so` |
| `005b0a57c000-005b0a57d000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libwindow_napi.z.so` |
| `005b0a5c0000-005b0a5e3000` | .so | `r--p` | 140 | 64 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/libzlib.z.so` |
| `005b0a5e3000-005b0a655000` | .so | `r-xp` | 456 | 392 | 127 | 0 | 0 | 0.00% | `/system/lib64/module/libzlib.z.so` |
| `005b0a655000-005b0a65c000` | .so | `r--p` | 28 | 28 | 7 | 0 | 0 | 0.00% | `/system/lib64/module/libzlib.z.so` |
| `005b0a65c000-005b0a65d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libzlib.z.so` |
| `005b0a680000-005b0a82b000` | .so | `r--p` | 1708 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libark_jsoptimizer.so` |
| `005b0a82b000-005b0b6f5000` | .so | `r-xp` | 15144 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libark_jsoptimizer.so` |
| `005b0b6f5000-005b0b752000` | .so | `r--p` | 372 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libark_jsoptimizer.so` |
| `005b0b752000-005b0b753000` | .so | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libark_jsoptimizer.so` |
| `005b0b753000-005b0b7ec000` | FilePage other | `rw-p` | 612 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libark_jsoptimizer.so.bss]` |
| `005b0b800000-005b0bf2f000` | .so | `r--p` | 7356 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/libark_llvmcodegen.so` |
| `005b0bf2f000-005b0d2fa000` | .so | `r-xp` | 20268 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libark_llvmcodegen.so` |
| `005b0d2fa000-005b0d3f0000` | .so | `r--p` | 984 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libark_llvmcodegen.so` |
| `005b0d3f0000-005b0d3f3000` | .so | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `/system/lib64/libark_llvmcodegen.so` |
| `005b0d3f3000-005b0d432000` | FilePage other | `rw-p` | 252 | 0 | 0 | 0 | 0 | 0.00% | `[anon:libark_llvmcodegen.so.bss]` |
| `005b0d432000-005b4d432000` | AnonPage other | `rw-p` | 1048576 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005b4dc7e000-005b4e4ca000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b4e4ca000-005b4ed16000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b4ed16000-005b4ee76000` | FilePage other | `r--p` | 1408 | 1164 | 1164 | 0 | 0 | 0.00% | `/system/app/appServiceFwk/HwMapKitHsp/mapLibrary.hsp` |
| `005b4ee76000-005b4f6c2000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b4f6c2000-005b4ff0e000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b4ff0e000-005b5075a000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b5075a000-005b50fa6000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b50fa6000-005b517f2000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b517f2000-005b5203e000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b5203e000-005b5288a000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b5288a000-005b530d6000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b530d6000-005b53922000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b53922000-005b5416e000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b5416e000-005b549ba000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b549ba000-005b55206000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b55206000-005b55a52000` | .hap | `r--p` | 8496 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b55a52000-005b5629e000` | .hap | `r--p` | 8496 | 4 | 1 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005b5629e000-005b56aea000` | .hap | `r--p` | 8496 | 4 | 1 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/entry.hap` |
| `005c4d432000-005c4d434000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30056]` |
| `005c4d434000-005c4d535000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30056]` |
| `005c4d535000-005c4d537000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30057]` |
| `005c4d537000-005c4d638000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30057]` |
| `005c4d638000-005c4d63a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30058]` |
| `005c4d740000-005c4d74f000` | .so | `r--p` | 60 | 40 | 9 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnetwork_boost.so` |
| `005c4d74f000-005c4d75a000` | .so | `r-xp` | 44 | 32 | 7 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnetwork_boost.so` |
| `005c4d75a000-005c4d762000` | .so | `r--p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnetwork_boost.so` |
| `005c4d762000-005c4d763000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnetwork_boost.so` |
| `005c4d780000-005c4d784000` | .so | `r--p` | 16 | 12 | 6 | 0 | 0 | 0.00% | `/system/lib64/libhttp_handover.z.so` |
| `005c4d784000-005c4d78b000` | .so | `r-xp` | 28 | 20 | 2 | 0 | 0 | 0.00% | `/system/lib64/libhttp_handover.z.so` |
| `005c4d78b000-005c4d78d000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libhttp_handover.z.so` |
| `005c4d78d000-005c4d78e000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libhttp_handover.z.so` |
| `005c4d78e000-005c4d790000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30059]` |
| `005c4d790000-005c4d891000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30059]` |
| `005c4d891000-005c4d893000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30060]` |
| `005c4d893000-005c4d994000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30060]` |
| `005c4d994000-005c4d996000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30061]` |
| `005c4da97000-005c4da99000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30062]` |
| `005c4e61a000-005c4e61c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30063]` |
| `005c4e61c000-005c4e71d000` | FilePage other | `rw-p` | 1028 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30063]` |
| `005c4ea1d000-005c4ea1f000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30064]` |
| `005c4ea1f000-005c4f220000` | FilePage other | `rw-p` | 8196 | 64 | 64 | 0 | 0 | 0.00% | `[anon:stack:30064]` |
| `005c4f240000-005c4f249000` | .so | `r--p` | 36 | 24 | 2 | 0 | 0 | 0.00% | `/system/lib64/libaps_client.z.so` |
| `005c4f25d000-005c4f25f000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30065]` |
| `005c4f380000-005c4f3b0000` | .so | `r--p` | 192 | 136 | 32 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_fwk_client.z.so` |
| `005c4f3b0000-005c4f414000` | .so | `r-xp` | 400 | 168 | 23 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_fwk_client.z.so` |
| `005c4f414000-005c4f419000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_fwk_client.z.so` |
| `005c4f419000-005c4f41a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_fwk_client.z.so` |
| `005c4f41a000-005c4f41b000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libgamecontroller_fwk_client.z.so.bss]` |
| `005c4f440000-005c4f44e000` | .so | `r--p` | 56 | 40 | 8 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_client.z.so` |
| `005c4f44e000-005c4f466000` | .so | `r-xp` | 96 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_client.z.so` |
| `005c4f466000-005c4f46c000` | .so | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_client.z.so` |
| `005c4f46c000-005c4f46d000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_client.z.so` |
| `005c4f480000-005c4f481000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_event.z.so` |
| `005c4f481000-005c4f484000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_event.z.so` |
| `005c4f484000-005c4f485000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_event.z.so` |
| `005c4f485000-005c4f486000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libgamecontroller_event.z.so` |
| `005c4f4c0000-005c4f4ce000` | .so | `r--p` | 56 | 40 | 4 | 0 | 0 | 0.00% | `/system/lib64/libark_connect_inspector.z.so` |
| `005c4f4ce000-005c4f4e4000` | .so | `r-xp` | 88 | 56 | 5 | 0 | 0 | 0.00% | `/system/lib64/libark_connect_inspector.z.so` |
| `005c4f4e4000-005c4f4e6000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libark_connect_inspector.z.so` |
| `005c4f4e6000-005c4f4e7000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libark_connect_inspector.z.so` |
| `005c4f5e7000-005c4f5e9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30067]` |
| `005c4f5e9000-005c4f6ea000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30067]` |
| `005c4f740000-005c4f745000` | .so | `r--p` | 20 | 16 | 1 | 0 | 0 | 0.00% | `/system/lib64/libframe_ui_utils.z.so` |
| `005c4f745000-005c4f749000` | .so | `r-xp` | 16 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libframe_ui_utils.z.so` |
| `005c4f749000-005c4f74b000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libframe_ui_utils.z.so` |
| `005c4f74b000-005c4f74c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libframe_ui_utils.z.so` |
| `005c4f74c000-005c4f74e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30068]` |
| `005c4f84f000-005c4f851000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30069]` |
| `005c4f851000-005c50052000` | FilePage other | `rw-p` | 8196 | 40 | 40 | 0 | 0 | 0.00% | `[anon:stack:30069]` |
| `005c51480000-005c5148c000` | .so | `r--p` | 48 | 36 | 1 | 0 | 0 | 0.00% | `/system/lib64/libdvsync.z.so` |
| `005c5148c000-005c5149e000` | .so | `r-xp` | 72 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libdvsync.z.so` |
| `005c5149e000-005c5149f000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libdvsync.z.so` |
| `005c5149f000-005c514a0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libdvsync.z.so` |
| `005c514a0000-005c514a1000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libdvsync.z.so.bss]` |
| `005c514a1000-005c51f8f000` | .so | `r--p` | 11192 | 1096 | 945 | 0 | 0 | 0.00% | `/system/lib64/libarkruntime.so` |
| `005c51fc0000-005c51fc1000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libdrawabledescriptor.z.so` |
| `005c51fc1000-005c51fc2000` | .so | `r-xp` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libdrawabledescriptor.z.so` |
| `005c51fc2000-005c51fc3000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libdrawabledescriptor.z.so` |
| `005c51fc3000-005c51fc4000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libdrawabledescriptor.z.so` |
| `005c52000000-005c52001000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/lib_cpuboost.so` |
| `005c52001000-005c52003000` | .so | `r-xp` | 8 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/lib_cpuboost.so` |
| `005c52003000-005c52004000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/lib_cpuboost.so` |
| `005c52004000-005c52005000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/lib_cpuboost.so` |
| `005c52005000-005c52007000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30072]` |
| `005c52007000-005c52108000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30072]` |
| `005c52140000-005c52143000` | .so | `r--p` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.0.z.so` |
| `005c52143000-005c52146000` | .so | `r-xp` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.0.z.so` |
| `005c52146000-005c52148000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.0.z.so` |
| `005c52148000-005c52149000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.0.z.so` |
| `005c52149000-005c521b6000` | FilePage other | `r--p` | 436 | 436 | 436 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNRacinghorizon-harmony_6a0e998/dyrnracinghorizon.bundle` |
| `005c52544000-005c52644000` | dev | `rw-s` | 1024 | 1024 | 1024 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/Create PixelMap` |
| `005c52644000-005c52646000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30073]` |
| `005c52646000-005c52747000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30073]` |
| `005c52747000-005c52749000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30074]` |
| `005c5294d000-005c53cf7000` | .ttf | `r--p` | 20136 | 10336 | 1613 | 0 | 0 | 0.00% | `/system/fonts/HarmonyOS_Sans_SC.ttf` |
| `005c53cf7000-005c53cf9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:31122]` |
| `005c53e00000-005c53e02000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmetadata_service_1.1.z.so` |
| `005c53e02000-005c53e05000` | .so | `r-xp` | 12 | 12 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmetadata_service_1.1.z.so` |
| `005c53e05000-005c53e06000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmetadata_service_1.1.z.so` |
| `005c53e06000-005c53e07000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmetadata_service_1.1.z.so` |
| `005c53e40000-005c53e42000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.2.z.so` |
| `005c53e42000-005c53e44000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.2.z.so` |
| `005c53e44000-005c53e45000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.2.z.so` |
| `005c53e45000-005c53e46000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.2.z.so` |
| `005c53e80000-005c53e82000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.3.z.so` |
| `005c53e82000-005c53e84000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.3.z.so` |
| `005c53e84000-005c53e86000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.3.z.so` |
| `005c53e86000-005c53e87000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/vendor/lib64/passthrough/libmapper_service_1.3.z.so` |
| `005c53ec0000-005c53ec9000` | .so | `r--p` | 36 | 36 | 34 | 0 | 0 | 0.00% | `/system/lib64/module/libpipwindow_napi.z.so` |
| `005c53ec9000-005c53ede000` | .so | `r-xp` | 84 | 84 | 82 | 0 | 0 | 0.00% | `/system/lib64/module/libpipwindow_napi.z.so` |
| `005c53ede000-005c53ee1000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/module/libpipwindow_napi.z.so` |
| `005c53ee1000-005c53ee2000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libpipwindow_napi.z.so` |
| `005c53f00000-005c53f03000` | .so | `r--p` | 12 | 12 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_xcomponent_controller.z.so` |
| `005c53f03000-005c53f06000` | .so | `r-xp` | 12 | 12 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_xcomponent_controller.z.so` |
| `005c53f06000-005c53f07000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_xcomponent_controller.z.so` |
| `005c53f07000-005c53f08000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_xcomponent_controller.z.so` |
| `005c53f40000-005c53f41000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavcastpicker.z.so` |
| `005c53f41000-005c53f44000` | .so | `r-xp` | 12 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavcastpicker.z.so` |
| `005c53f44000-005c53f45000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavcastpicker.z.so` |
| `005c53f45000-005c53f54000` | .so | `rw-p` | 60 | 60 | 21 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavcastpicker.z.so` |
| `005c53f8a000-005c54211000` | FilePage other | `r--p` | 2588 | 2588 | 2588 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNHarmonyBase-harmony_0e9fe2c/dyrnharmonybase.bundle` |
| `005c54240000-005c5424e000` | .so | `r--p` | 56 | 40 | 7 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_network.z.so` |
| `005c5424e000-005c54267000` | .so | `r-xp` | 100 | 48 | 9 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_network.z.so` |
| `005c54267000-005c5426a000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_network.z.so` |
| `005c5426a000-005c5426b000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libace_network.z.so` |
| `005c54280000-005c54283000` | .so | `r--p` | 12 | 12 | 8 | 0 | 0 | 0.00% | `/system/lib64/libpreload_napi.z.so` |
| `005c54283000-005c54288000` | .so | `r-xp` | 20 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libpreload_napi.z.so` |
| `005c54288000-005c54289000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libpreload_napi.z.so` |
| `005c54289000-005c5428a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libpreload_napi.z.so` |
| `005c5428a000-005c542d6000` | .ttf | `r--p` | 304 | 100 | 39 | 0 | 0 | 0.00% | `/system/fonts/HarmonyOS_Sans_Italic.ttf` |
| `005c54ff9000-005c54ffb000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30092]` |
| `005c54ffb000-005c550fc000` | FilePage other | `rw-p` | 1028 | 80 | 80 | 0 | 0 | 0.00% | `[anon:stack:30092]` |
| `005c550fc000-005c550fe000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30093]` |
| `005c550fe000-005c551ff000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30093]` |
| `005c551ff000-005c552ff000` | AnonPage other | `rw-p` | 1024 | 28 | 28 | 0 | 0 | 0.00% | `(anonymous)` |
| `005c55300000-005c55305000` | .so | `r--p` | 20 | 16 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libcomponentutils.z.so` |
| `005c55305000-005c55318000` | .so | `r-xp` | 76 | 56 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libcomponentutils.z.so` |
| `005c55318000-005c5531a000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libcomponentutils.z.so` |
| `005c5531a000-005c5531b000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/arkui/libcomponentutils.z.so` |
| `005c55340000-005c5534a000` | .so | `r--p` | 40 | 24 | 7 | 0 | 0 | 0.00% | `/system/lib64/libupdatemanager_client.z.so` |
| `005c5534a000-005c5535a000` | .so | `r-xp` | 64 | 48 | 34 | 0 | 0 | 0.00% | `/system/lib64/libupdatemanager_client.z.so` |
| `005c5535a000-005c5535d000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/libupdatemanager_client.z.so` |
| `005c5535d000-005c5535e000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libupdatemanager_client.z.so` |
| `005c55380000-005c55391000` | .so | `r--p` | 68 | 44 | 14 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/appgalleryservice/libupdatemanager_napi.z.so` |
| `005c55391000-005c553ba000` | .so | `r-xp` | 164 | 112 | 38 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/appgalleryservice/libupdatemanager_napi.z.so` |
| `005c553ba000-005c553bc000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/appgalleryservice/libupdatemanager_napi.z.so` |
| `005c553bc000-005c553bd000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/hms/core/appgalleryservice/libupdatemanager_napi.z.so` |
| `005c553bd000-005c553be000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libupdatemanager_napi.z.so.bss]` |
| `005c553be000-005c553fe000` | dev | `rw-s` | 256 | 4 | 2 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/shared_memory/56CD25A8F02C64C6E0C3E47B1E3739D1` |
| `005c55400000-005c55814000` | AnonPage other | `rw-p` | 4176 | 92 | 92 | 0 | 0 | 0.00% | `(anonymous)` |
| `005c55814000-005c55815000` | guard | `---p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `(anonymous)` |
| `005c55815000-005c55c14000` | AnonPage other | `rw-p` | 4092 | 4092 | 4092 | 0 | 0 | 0.00% | `(anonymous)` |
| `005c55c14000-005c55c15000` | guard | `---p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `(anonymous)` |
| `005c55c15000-005c56014000` | AnonPage other | `rw-p` | 4092 | 4092 | 4092 | 0 | 0 | 0.00% | `(anonymous)` |
| `005c56014000-005c56015000` | guard | `---p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `(anonymous)` |
| `005c56015000-005c56400000` | AnonPage other | `rw-p` | 4012 | 2852 | 2852 | 0 | 0 | 0.00% | `(anonymous)` |
| `005c56400000-005d16400000` | guard | `---p` | 3145728 | 0 | 0 | 0 | 0 | 0.00% | `(anonymous)` |
| `005d16400000-005d16402000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30094]` |
| `005d16402000-005d16503000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30094]` |
| `005d16540000-005d1664a000` | .so | `r--p` | 1064 | 156 | 9 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopencv_imgproc.z.so` |
| `005d1664a000-005d16819000` | .so | `r-xp` | 1852 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopencv_imgproc.z.so` |
| `005d16819000-005d1682a000` | .so | `r--p` | 68 | 68 | 68 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopencv_imgproc.z.so` |
| `005d1682a000-005d16832000` | .so | `rw-p` | 32 | 32 | 32 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopencv_imgproc.z.so` |
| `005d16832000-005d168d0000` | FilePage other | `rw-p` | 632 | 552 | 552 | 0 | 0 | 0.00% | `[anon:libopencv_imgproc.z.so.bss]` |
| `005d16900000-005d169e9000` | .so | `r--p` | 932 | 300 | 17 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopencv_core.z.so` |
| `005d169e9000-005d16b78000` | .so | `r-xp` | 1596 | 172 | 10 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopencv_core.z.so` |
| `005d16b78000-005d16b87000` | .so | `r--p` | 60 | 60 | 60 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopencv_core.z.so` |
| `005d16b87000-005d16b8b000` | .so | `rw-p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/chipset-sdk/libopencv_core.z.so` |
| `005d16b8b000-005d16b90000` | FilePage other | `rw-p` | 20 | 16 | 16 | 0 | 0 | 0.00% | `[anon:libopencv_core.z.so.bss]` |
| `005d16bc0000-005d16be9000` | .so | `r--p` | 164 | 108 | 40 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappgallery_sa_client.z.so` |
| `005d16be9000-005d16c2c000` | .so | `r-xp` | 268 | 80 | 40 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappgallery_sa_client.z.so` |
| `005d16c2c000-005d16c31000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappgallery_sa_client.z.so` |
| `005d16c31000-005d16c32000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libappgallery_sa_client.z.so` |
| `005d16c32000-005d16c33000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libappgallery_sa_client.z.so.bss]` |
| `005d16c33000-005d16c35000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30102]` |
| `005d16c35000-005d17436000` | FilePage other | `rw-p` | 8196 | 36 | 36 | 0 | 0 | 0.00% | `[anon:stack:30102]` |
| `005d18c40000-005d18c58000` | .so | `r--p` | 96 | 64 | 60 | 0 | 0 | 0.00% | `/system/lib64/libpreload_native.z.so` |
| `005d18c58000-005d18c61000` | .so | `r-xp` | 36 | 32 | 32 | 0 | 0 | 0.00% | `/system/lib64/libpreload_native.z.so` |
| `005d18c61000-005d18c63000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libpreload_native.z.so` |
| `005d18c63000-005d18c64000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libpreload_native.z.so` |
| `005d18c80000-005d18c9f000` | .so | `r--p` | 124 | 96 | 5 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_client.z.so` |
| `005d18c9f000-005d18cce000` | .so | `r-xp` | 188 | 164 | 13 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_client.z.so` |
| `005d18cce000-005d18cd1000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_client.z.so` |
| `005d18cd1000-005d18cd2000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_client.z.so` |
| `005d18d00000-005d18d04000` | .so | `r--p` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_interceptor_http.z.so` |
| `005d18d04000-005d18d0a000` | .so | `r-xp` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_interceptor_http.z.so` |
| `005d18d0a000-005d18d0b000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_interceptor_http.z.so` |
| `005d18d0b000-005d18d0c000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhttp_interceptor_http.z.so` |
| `005d18d0c000-005d18d0d000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libhttp_interceptor_http.z.so.bss]` |
| `005d18d40000-005d18d61000` | .so | `r--p` | 132 | 68 | 36 | 0 | 0 | 0.00% | `/system/lib64/libpreload_native_rust.z.so` |
| `005d18d61000-005d18da3000` | .so | `r-xp` | 264 | 240 | 175 | 0 | 0 | 0.00% | `/system/lib64/libpreload_native_rust.z.so` |
| `005d18da3000-005d18da8000` | .so | `r--p` | 20 | 20 | 20 | 0 | 0 | 0.00% | `/system/lib64/libpreload_native_rust.z.so` |
| `005d18da8000-005d18da9000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libpreload_native_rust.z.so` |
| `005d18da9000-005d18daa000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libpreload_native_rust.z.so.bss]` |
| `005d18daa000-005d18def000` | FilePage other | `r--p` | 276 | 276 | 138 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNDreamJourney-harmony_4c2dfd5/dyrndreamjourney.bundle` |
| `005d18e00000-005d18e01000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005d19600000-005d19601000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005d19601000-005d19603000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30111]` |
| `005d19603000-005d19704000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30111]` |
| `005d19704000-005d1ab07000` | .ttf | `r--p` | 20492 | 20 | 6 | 0 | 0 | 0.00% | `/system/fonts/HYQiHeiL3.ttf` |
| `005d1ab07000-005d1b48c000` | .ttf | `r--p` | 9748 | 112 | 37 | 0 | 0 | 0.00% | `/system/fonts/HarmonyOS_Sans_TC.ttf` |
| `005d1b48c000-005d1c497000` | .ttf | `r--p` | 16428 | 132 | 111 | 0 | 0 | 0.00% | `/system/fonts/HMOSColorEmojiCompat.ttf` |
| `005d1c4c0000-005d1c4c1000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavcastpickerparam.z.so` |
| `005d1c4c1000-005d1c4c4000` | .so | `r-xp` | 12 | 12 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavcastpickerparam.z.so` |
| `005d1c4c4000-005d1c4c5000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavcastpickerparam.z.so` |
| `005d1c4c5000-005d1c4c6000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavcastpickerparam.z.so` |
| `005d1c500000-005d1c507000` | .so | `r--p` | 28 | 28 | 3 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libapplication_napi.z.so` |
| `005d1c507000-005d1c511000` | .so | `r-xp` | 40 | 40 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libapplication_napi.z.so` |
| `005d1c511000-005d1c512000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libapplication_napi.z.so` |
| `005d1c512000-005d1c513000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/app/ability/libapplication_napi.z.so` |
| `005d1c513000-005d1c558000` | FilePage other | `r--p` | 276 | 276 | 138 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNDreamJourney-harmony_4c2dfd5/dyrndreamjourney.bundle` |
| `005d1c57c000-005d1c57e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30119]` |
| `005d1c57e000-005d1c67f000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30119]` |
| `005d1e280000-005d1e281000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libconfiguration.z.so` |
| `005d1e281000-005d1e283000` | .so | `r-xp` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/module/libconfiguration.z.so` |
| `005d1e283000-005d1e284000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libconfiguration.z.so` |
| `005d1e284000-005d1e285000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/libconfiguration.z.so` |
| `005d1e2c0000-005d1e2d3000` | .so | `r--p` | 76 | 64 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/resourceschedule/libbackgroundtaskmanager_napi.z.so` |
| `005d1e2d3000-005d1e2f6000` | .so | `r-xp` | 140 | 140 | 11 | 0 | 0 | 0.00% | `/system/lib64/module/resourceschedule/libbackgroundtaskmanager_napi.z.so` |
| `005d1e2f6000-005d1e2fa000` | .so | `r--p` | 16 | 16 | 16 | 0 | 0 | 0.00% | `/system/lib64/module/resourceschedule/libbackgroundtaskmanager_napi.z.so` |
| `005d1e2fa000-005d1e2fb000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/resourceschedule/libbackgroundtaskmanager_napi.z.so` |
| `005d1e300000-005d1e301000` | .so | `r--p` | 4 | 4 | 1 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavvolumepanel.z.so` |
| `005d1e301000-005d1e304000` | .so | `r-xp` | 12 | 12 | 2 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavvolumepanel.z.so` |
| `005d1e304000-005d1e305000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavvolumepanel.z.so` |
| `005d1e305000-005d1e307000` | .so | `rw-p` | 8 | 8 | 4 | 0 | 0 | 0.00% | `/system/lib64/module/multimedia/libavvolumepanel.z.so` |
| `005d1e307000-005d1e379000` | FilePage other | `r--p` | 456 | 456 | 456 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNSuperFans2-harmony_a9af3d0/dyrnsuperfans2.bundle` |
| `005d1e882000-005d1e982000` | FilePage other | `rw-p` | 1024 | 80 | 80 | 0 | 0 | 0.00% | `[anon:ffrt_coroutine_stack]` |
| `005d1ea82000-005d1eb82000` | FilePage other | `rw-p` | 1024 | 12 | 12 | 0 | 0 | 0.00% | `[anon:ffrt_coroutine_stack]` |
| `005d1ed00000-005d1ee40000` | .so | `r--p` | 1280 | 1084 | 1084 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libsvga.so` |
| `005d1ee40000-005d1ef81000` | .so | `r-xp` | 1284 | 1136 | 1136 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libsvga.so` |
| `005d1ef81000-005d1ef90000` | .so | `r--p` | 60 | 60 | 60 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libsvga.so` |
| `005d1ef90000-005d1ef91000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/libs/arm64/libsvga.so` |
| `005d1ef91000-005d1ef93000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libsvga.so.bss]` |
| `005d1ef93000-005d1ef95000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30234]` |
| `005d1f096000-005d1f098000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30235]` |
| `005d1f098000-005d1f199000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30235]` |
| `005d1f199000-005d1f19b000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30236]` |
| `005d1f19b000-005d1f29c000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30236]` |
| `005d1f2c0000-005d1f2d8000` | .so | `r--p` | 96 | 96 | 10 | 0 | 0 | 0.00% | `/system/lib64/libstylus_innerapi.z.so` |
| `005d1f2d8000-005d1f2f6000` | .so | `r-xp` | 120 | 120 | 25 | 0 | 0 | 0.00% | `/system/lib64/libstylus_innerapi.z.so` |
| `005d1f2f6000-005d1f300000` | .so | `r--p` | 40 | 40 | 40 | 0 | 0 | 0.00% | `/system/lib64/libstylus_innerapi.z.so` |
| `005d1f300000-005d1f301000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libstylus_innerapi.z.so` |
| `005d1f301000-005d1f302000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libstylus_innerapi.z.so.bss]` |
| `005d1f340000-005d1f34b000` | Graph | `r--p` | 44 | 44 | 11 | 0 | 0 | 0.00% | `/system/lib64/libgameservice_graphic_plugin.z.so` |
| `005d1f35d000-005d1f35f000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30237]` |
| `005d1f460000-005d1f462000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30238]` |
| `005d1f462000-005d1f563000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30238]` |
| `005d1f563000-005d1f565000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30239]` |
| `005d1f565000-005d1f666000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30239]` |
| `005d1f666000-005d1f668000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30240]` |
| `005d1f668000-005d1f769000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30240]` |
| `005d1f769000-005d1f76b000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30241]` |
| `005d1f86c000-005d1f86e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30242]` |
| `005d1f96f000-005d1f971000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30487]` |
| `005d1f971000-005d1fa72000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30487]` |
| `005d1fa72000-005d1fa74000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30244]` |
| `005d1fa74000-005d1fb75000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30244]` |
| `005d1fb75000-005d1fb77000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30245]` |
| `005d1fb77000-005d1fc78000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30245]` |
| `005d1fc78000-005d1fc7a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30256]` |
| `005d2047b000-005d2047d000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30277]` |
| `005d2047d000-005d2057e000` | FilePage other | `rw-p` | 1028 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30277]` |
| `005d2057e000-005d20580000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30278]` |
| `005d20681000-005d20683000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30279]` |
| `005d20784000-005d20786000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30299]` |
| `005d20786000-005d20887000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30299]` |
| `005d20887000-005d20932000` | FilePage other | `r--p` | 684 | 684 | 684 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNChristmas2024-harmony_d207b4b/dyrnchristmas2024.bundle` |
| `005d20932000-005d20973000` | FilePage other | `rw-s` | 260 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/ShaderCache/index` |
| `005d20984000-005d20986000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30292]` |
| `005d20a87000-005d20a89000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30293]` |
| `005d20a89000-005d20b8a000` | FilePage other | `rw-p` | 1028 | 4 | 4 | 0 | 0 | 0.00% | `[anon:stack:30293]` |
| `005d20b8a000-005d20bfa000` | FilePage other | `r--p` | 448 | 448 | 448 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNTheGreatVoyage-harmony_bae377c/dyrnthegreatvoyage.bundle` |
| `005d20bfa000-005d20c67000` | FilePage other | `r--p` | 436 | 436 | 436 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNInterstellarRocket-harmony_e739baa/dyrninterstellarrocket.bundle` |
| `005d20d81000-005d20d83000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30274]` |
| `005d20e84000-005d20e86000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30275]` |
| `005d20f87000-005d20f89000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30322]` |
| `005d2108a000-005d2108c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30323]` |
| `005d2108c000-005d2118d000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30323]` |
| `005d2118d000-005d2118f000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30324]` |
| `005d21290000-005d21292000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30325]` |
| `005d21393000-005d21395000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30326]` |
| `005d21496000-005d21793000` | FilePage other | `rw-s` | 3060 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d21793000-005d21a90000` | FilePage other | `rw-s` | 3060 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d21a90000-005d21d8d000` | FilePage other | `rw-s` | 3060 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d21d8d000-005d2208a000` | FilePage other | `rw-s` | 3060 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d2408a000-005d24388000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d24b88000-005d24e86000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d24e86000-005d25184000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d25184000-005d25186000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30346]` |
| `005d25287000-005d25585000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d25f85000-005d25f87000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30347]` |
| `005d25f87000-005d26088000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30347]` |
| `005d26088000-005d2608a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30348]` |
| `005d2618b000-005d2618d000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30349]` |
| `005d2618d000-005d2628e000` | FilePage other | `rw-p` | 1028 | 24 | 24 | 0 | 0 | 0.00% | `[anon:stack:30349]` |
| `005d2628e000-005d2658c000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d2658c000-005d2688a000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d2688a000-005d2688c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30355]` |
| `005d2698d000-005d26a67000` | FilePage other | `r--p` | 872 | 872 | 218 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNAnnual2023Q4-harmony_a8cdccc/dyrnannual2023q4.bundle` |
| `005d26a90000-005d26d8e000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d2958e000-005d2988c000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d29a92000-005d29d90000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d29d90000-005d29e6a000` | FilePage other | `r--p` | 872 | 872 | 218 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNAnnual2023Q4-harmony_a8cdccc/dyrnannual2023q4.bundle` |
| `005d2ce6a000-005d2cf44000` | FilePage other | `r--p` | 872 | 872 | 218 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNAnnual2023Q4-harmony_a8cdccc/dyrnannual2023q4.bundle` |
| `005d2cf44000-005d2d01e000` | FilePage other | `r--p` | 872 | 872 | 218 | 0 | 0 | 0.00% | `/data/storage/el2/base/haps/entry/files/rn/bundle/DYRNAnnual2023Q4-harmony_a8cdccc/dyrnannual2023q4.bundle` |
| `005d2d040000-005d2d042000` | .so | `r--p` | 8 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtelephony_radio.so` |
| `005d2d042000-005d2d045000` | .so | `r-xp` | 12 | 8 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtelephony_radio.so` |
| `005d2d045000-005d2d046000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtelephony_radio.so` |
| `005d2d046000-005d2d047000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtelephony_radio.so` |
| `005d2d080000-005d2d082000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_rdb_ndk_utils.z.so` |
| `005d2d082000-005d2d086000` | .so | `r-xp` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/libnative_rdb_ndk_utils.z.so` |
| `005d2d086000-005d2d087000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_rdb_ndk_utils.z.so` |
| `005d2d087000-005d2d088000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_rdb_ndk_utils.z.so` |
| `005d2d0c0000-005d2d0cd000` | .so | `r--p` | 52 | 32 | 16 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_runtime.so` |
| `005d2d0cd000-005d2d0dc000` | .so | `r-xp` | 60 | 24 | 12 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_runtime.so` |
| `005d2d0dc000-005d2d0df000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_runtime.so` |
| `005d2d0df000-005d2d0e0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_runtime.so` |
| `005d2d100000-005d2d101000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohvibrator.z.so` |
| `005d2d101000-005d2d104000` | .so | `r-xp` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohvibrator.z.so` |
| `005d2d104000-005d2d105000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohvibrator.z.so` |
| `005d2d105000-005d2d106000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohvibrator.z.so` |
| `005d2d140000-005d2d149000` | .so | `r--p` | 36 | 20 | 10 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohpreferences.so` |
| `005d2d149000-005d2d158000` | .so | `r-xp` | 60 | 8 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohpreferences.so` |
| `005d2d158000-005d2d159000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohpreferences.so` |
| `005d2d159000-005d2d15a000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohpreferences.so` |
| `005d2d194000-005d2d195000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohcommonevent.so` |
| `005d2d1c0000-005d2d1c2000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnet_ssl.so` |
| `005d2d1c2000-005d2d1c6000` | .so | `r-xp` | 16 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnet_ssl.so` |
| `005d2d1c6000-005d2d1c7000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnet_ssl.so` |
| `005d2d1c7000-005d2d1c8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnet_ssl.so` |
| `005d2d200000-005d2d207000` | .so | `r--p` | 28 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpasteboard.so` |
| `005d2d207000-005d2d211000` | .so | `r-xp` | 40 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpasteboard.so` |
| `005d2d211000-005d2d214000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpasteboard.so` |
| `005d2d214000-005d2d215000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libpasteboard.so` |
| `005d37fdc000-005d37fe0000` | .so | `r--p` | 16 | 0 | 0 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so` |
| `005d38280000-005d3828b000` | .so | `r--p` | 44 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnative_avscreen_capture.so` |
| `005d3828b000-005d3829e000` | .so | `r-xp` | 76 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/libnative_avscreen_capture.so` |
| `005d3829e000-005d3829f000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_avscreen_capture.so` |
| `005d3829f000-005d382a0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libnative_avscreen_capture.so` |
| `005d382a0000-005d382a1000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libnative_avscreen_capture.so.bss]` |
| `005d382c0000-005d382c5000` | .so | `r--p` | 20 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohhicollie.so` |
| `005d382c5000-005d382cb000` | .so | `r-xp` | 24 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohhicollie.so` |
| `005d382cb000-005d382cc000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohhicollie.so` |
| `005d382cc000-005d382cd000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohhicollie.so` |
| `005d38300000-005d38307000` | .so | `r--p` | 28 | 20 | 1 | 0 | 0 | 0.00% | `/system/lib64/libhiappevent_ndk.z.so` |
| `005d38307000-005d38310000` | .so | `r-xp` | 36 | 20 | 0 | 0 | 0 | 0.00% | `/system/lib64/libhiappevent_ndk.z.so` |
| `005d38310000-005d38311000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libhiappevent_ndk.z.so` |
| `005d38311000-005d38312000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libhiappevent_ndk.z.so` |
| `005d38312000-005d38313000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libhiappevent_ndk.z.so.bss]` |
| `005d38340000-005d383cc000` | .so | `r--p` | 560 | 268 | 132 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libffmpeg.so` |
| `005d3859f000-005d385a0000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libffmpeg.so` |
| `005d38680000-005d38694000` | .so | `r--p` | 80 | 32 | 14 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libadapter_ndk_stub.so` |
| `005d38694000-005d386b6000` | .so | `r-xp` | 136 | 52 | 26 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libadapter_ndk_stub.so` |
| `005d386b6000-005d386b9000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libadapter_ndk_stub.so` |
| `005d386b9000-005d386ba000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el1/bundle/arkwebcore/libs/arm64/libadapter_ndk_stub.so` |
| `005d386ba000-005d386bc000` | FilePage other | `rw-p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `[anon:libadapter_ndk_stub.so.bss]` |
| `005d386c0000-005d386c2000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhuks_ndk.z.so` |
| `005d386c2000-005d386c6000` | .so | `r-xp` | 16 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhuks_ndk.z.so` |
| `005d386c6000-005d386c7000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhuks_ndk.z.so` |
| `005d386c7000-005d386c8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libhuks_ndk.z.so` |
| `005d38700000-005d38702000` | .so | `r--p` | 8 | 8 | 1 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_ssl.z.so` |
| `005d38702000-005d38705000` | .so | `r-xp` | 12 | 8 | 2 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_ssl.z.so` |
| `005d38705000-005d38707000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_ssl.z.so` |
| `005d38707000-005d38708000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/platformsdk/libnet_ssl.z.so` |
| `005d38740000-005d38754000` | .so | `r--p` | 80 | 52 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohinput.so` |
| `005d38754000-005d3877f000` | .so | `r-xp` | 172 | 44 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohinput.so` |
| `005d3877f000-005d38781000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohinput.so` |
| `005d38781000-005d38782000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohinput.so` |
| `005d38782000-005d38783000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libohinput.so.bss]` |
| `005d387c0000-005d387ca000` | .so | `r--p` | 40 | 24 | 1 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_window_manager.so` |
| `005d387ca000-005d387e4000` | .so | `r-xp` | 104 | 12 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_window_manager.so` |
| `005d387e4000-005d387e7000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_window_manager.so` |
| `005d387e7000-005d387e8000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_window_manager.so` |
| `005d38800000-005d38801000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtime_service_ndk.so` |
| `005d38801000-005d38804000` | .so | `r-xp` | 12 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtime_service_ndk.so` |
| `005d38804000-005d38805000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtime_service_ndk.so` |
| `005d38805000-005d38806000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtime_service_ndk.so` |
| `005d38840000-005d38856000` | .so | `r--p` | 88 | 52 | 1 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_rdb_ndk.z.so` |
| `005d38856000-005d38881000` | .so | `r-xp` | 172 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_rdb_ndk.z.so` |
| `005d38881000-005d38883000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_rdb_ndk.z.so` |
| `005d38883000-005d38884000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libnative_rdb_ndk.z.so` |
| `005d388c0000-005d388cf000` | .so | `r--p` | 60 | 32 | 1 | 0 | 0 | 0.00% | `/system/lib64/libavplayer.so` |
| `005d388cf000-005d388eb000` | .so | `r-xp` | 112 | 16 | 0 | 0 | 0 | 0.00% | `/system/lib64/libavplayer.so` |
| `005d388eb000-005d388ed000` | .so | `r--p` | 8 | 8 | 8 | 0 | 0 | 0.00% | `/system/lib64/libavplayer.so` |
| `005d388ed000-005d388ee000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libavplayer.so` |
| `005d388ee000-005d388ef000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libavplayer.so.bss]` |
| `005d38900000-005d38901000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_access_control.so` |
| `005d38901000-005d38904000` | .so | `r-xp` | 12 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_access_control.so` |
| `005d38904000-005d38905000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_access_control.so` |
| `005d38905000-005d38906000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libability_access_control.so` |
| `005d38940000-005d38941000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohbattery_info.so` |
| `005d38941000-005d38944000` | .so | `r-xp` | 12 | 8 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohbattery_info.so` |
| `005d38944000-005d38945000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohbattery_info.so` |
| `005d38945000-005d38946000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohbattery_info.so` |
| `005d38980000-005d38981000` | .so | `r--p` | 4 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtelephony_data.so` |
| `005d38981000-005d38984000` | .so | `r-xp` | 12 | 8 | 6 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtelephony_data.so` |
| `005d38984000-005d38985000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtelephony_data.so` |
| `005d38985000-005d38986000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libtelephony_data.so` |
| `005d389c0000-005d389ce000` | .so | `r--p` | 56 | 36 | 18 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohinputmethod.so` |
| `005d389ce000-005d389e5000` | .so | `r-xp` | 92 | 12 | 6 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohinputmethod.so` |
| `005d389e5000-005d389e8000` | .so | `r--p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohinputmethod.so` |
| `005d389e8000-005d389e9000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohinputmethod.so` |
| `005d38a00000-005d38a02000` | .so | `r--p` | 8 | 8 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohsensor.so` |
| `005d38a02000-005d38a06000` | .so | `r-xp` | 16 | 4 | 0 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohsensor.so` |
| `005d38a06000-005d38a07000` | .so | `r--p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohsensor.so` |
| `005d38a07000-005d38a08000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/ndk/libohsensor.so` |
| `005d38a40000-005d38afe000` | GL | `r--p` | 760 | 604 | 78 | 0 | 0 | 0.00% | `/system/lib64/libohos_adapter_glue_source.z.so` |
| `005d38bf1000-005d38bf4000` | GL | `rw-p` | 12 | 12 | 12 | 0 | 0 | 0.00% | `[anon:libohos_adapter_glue_source.z.so.bss]` |
| `005d38bf4000-005d395f1000` | .hap | `r--s` | 10228 | 648 | 538 | 0 | 0 | 0.00% | `/system/app/ArkWebCore/ArkWebCore.hap` |
| `005d395f1000-005d395f3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30359]` |
| `005d395f3000-005d397f4000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30359]` |
| `005d397f4000-005d39af2000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d39af2000-005d39bfb000` | .hap | `r--s` | 1060 | 8 | 8 | 0 | 0 | 0.00% | `/system/app/ArkWebCore/ArkWebCore.hap` |
| `005d39bfb000-005d39d65000` | .hap | `r--s` | 1448 | 8 | 8 | 0 | 0 | 0.00% | `/system/app/ArkWebCore/ArkWebCore.hap` |
| `005d39d65000-005d39de5000` | .hap | `r--s` | 512 | 104 | 104 | 0 | 0 | 0.00% | `/system/app/ArkWebCore/ArkWebCore.hap` |
| `005d39de5000-005d3a9e1000` | .hap | `r--s` | 12272 | 36 | 36 | 0 | 0 | 0.00% | `/system/app/ArkWebCore/ArkWebCore.hap` |
| `005d3a9e1000-005d3a9e3000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30360]` |
| `005d3abe4000-005d3abe6000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30361]` |
| `005d3abe6000-005d3ade7000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30361]` |
| `005d3ade7000-005d3ade9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30362]` |
| `005d3ade9000-005d3afea000` | FilePage other | `rw-p` | 2052 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30362]` |
| `005d3afea000-005d3afec000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30363]` |
| `005d3afec000-005d3b1ed000` | FilePage other | `rw-p` | 2052 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30363]` |
| `005d3b1ed000-005d3b1ef000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30364]` |
| `005d3b1ef000-005d3b3f0000` | FilePage other | `rw-p` | 2052 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30364]` |
| `005d3b3f0000-005d3b3f2000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30365]` |
| `005d3b3f2000-005d3b5f3000` | FilePage other | `rw-p` | 2052 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30365]` |
| `005d3b5f3000-005d3b5f5000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30366]` |
| `005d3b5f5000-005d3b7f6000` | FilePage other | `rw-p` | 2052 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30366]` |
| `005d3b7f6000-005d3b7f8000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30367]` |
| `005d3b7f8000-005d3b9f9000` | FilePage other | `rw-p` | 2052 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30367]` |
| `005d3b9f9000-005d3b9fb000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30368]` |
| `005d3b9fb000-005d3bbfc000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30368]` |
| `005d3bbfc000-005d3bbfe000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30369]` |
| `005d3bbfe000-005d3bdff000` | FilePage other | `rw-p` | 2052 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30369]` |
| `005d3bdff000-005d3be01000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30370]` |
| `005d3be01000-005d3c002000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30370]` |
| `005d3c002000-005d3c004000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30371]` |
| `005d3c004000-005d3c205000` | FilePage other | `rw-p` | 2052 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30371]` |
| `005d3c205000-005d3c207000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30372]` |
| `005d3c207000-005d3c408000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30372]` |
| `005d3c408000-005d3c40a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30373]` |
| `005d3c40a000-005d3c60b000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30373]` |
| `005d3c60b000-005d3c60d000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30374]` |
| `005d3c60d000-005d3c80e000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30374]` |
| `005d3c80e000-005d3c810000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30375]` |
| `005d3c810000-005d3ca11000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30375]` |
| `005d3ca11000-005d3ca13000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30376]` |
| `005d3ca13000-005d3cc14000` | FilePage other | `rw-p` | 2052 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30376]` |
| `005d3cc14000-005d3cc16000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30377]` |
| `005d3cc16000-005d3ce17000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30377]` |
| `005d3ce17000-005d3ce19000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30378]` |
| `005d3ce19000-005d3d01a000` | FilePage other | `rw-p` | 2052 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30378]` |
| `005d3d01a000-005d3d01c000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30379]` |
| `005d3d01c000-005d3d21d000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30379]` |
| `005d3d21d000-005d3d21f000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30380]` |
| `005d3d21f000-005d3d420000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30380]` |
| `005d3d420000-005d3d422000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30381]` |
| `005d3d422000-005d3d623000` | FilePage other | `rw-p` | 2052 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30381]` |
| `005d3d623000-005d3d625000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30382]` |
| `005d3d625000-005d3d826000` | FilePage other | `rw-p` | 2052 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30382]` |
| `005d3d826000-005d3d828000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30383]` |
| `005d3d828000-005d3da29000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30383]` |
| `005d3da29000-005d3da2b000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30384]` |
| `005d3da2b000-005d3dc2c000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30384]` |
| `005d3dc2c000-005d3dc2e000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30386]` |
| `005d3dc2e000-005d3de2f000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30386]` |
| `005d3de2f000-005d3de31000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30387]` |
| `005d3de31000-005d3e032000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30387]` |
| `005d3e032000-005d3e034000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30388]` |
| `005d3e034000-005d3e235000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30388]` |
| `005d3e235000-005d3e237000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30389]` |
| `005d3e237000-005d3e438000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30389]` |
| `005d3e438000-005d3e43a000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30390]` |
| `005d3e43a000-005d3e63b000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30390]` |
| `005d3e63b000-005d3e63d000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30391]` |
| `005d3e63d000-005d3e83e000` | FilePage other | `rw-p` | 2052 | 16 | 16 | 0 | 0 | 0.00% | `[anon:stack:30391]` |
| `005d3e83e000-005d3e840000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30392]` |
| `005d3e840000-005d3ea41000` | FilePage other | `rw-p` | 2052 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30392]` |
| `005d3ea41000-005d3ea43000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30393]` |
| `005d3ea43000-005d3ec44000` | FilePage other | `rw-p` | 2052 | 20 | 20 | 0 | 0 | 0.00% | `[anon:stack:30393]` |
| `005d3ec44000-005d3ef42000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d3ef42000-005d3ef83000` | FilePage other | `rw-s` | 260 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GrShaderCache/index` |
| `005d3ef83000-005d3efc4000` | Graph | `rw-s` | 260 | 4 | 4 | 0 | 0 | 0.00% | `/data/storage/el2/base/cache/web/GraphiteDawnCache/index` |
| `005d3efc4000-005d3efc6000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30421]` |
| `005d3f0c7000-005d3f0c9000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30422]` |
| `005d3f1ca000-005d3f1cc000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30423]` |
| `005d3f2cd000-005d3f2cf000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30424]` |
| `005d40000000-005d40001000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005d40001000-005d40200000` | native heap | `rw-p` | 2044 | 84 | 84 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005d40200000-005d40201000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc meta]` |
| `005d40201000-005d42a01000` | native heap | `rw-p` | 40960 | 0 | 0 | 0 | 0 | 0.00% | `[anon:native_heap:jemalloc]` |
| `005d42a40000-005d42a4c000` | .so | `r--p` | 48 | 36 | 15 | 0 | 0 | 0.00% | `/system/lib64/libsafe_browsing_client.z.so` |
| `005d42a4c000-005d42a5c000` | .so | `r-xp` | 64 | 40 | 10 | 0 | 0 | 0.00% | `/system/lib64/libsafe_browsing_client.z.so` |
| `005d42a5c000-005d42a62000` | .so | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/libsafe_browsing_client.z.so` |
| `005d42a62000-005d42a63000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libsafe_browsing_client.z.so` |
| `005d42a63000-005d42d61000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d42d61000-005d4305f000` | FilePage other | `rw-s` | 3064 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `005d43080000-005d43099000` | .so | `r--p` | 100 | 56 | 56 | 0 | 0 | 0.00% | `/system/lib64/libarkui_textclock.z.so` |
| `005d43099000-005d430e2000` | .so | `r-xp` | 292 | 208 | 208 | 0 | 0 | 0.00% | `/system/lib64/libarkui_textclock.z.so` |
| `005d430e2000-005d430e8000` | .so | `r--p` | 24 | 24 | 24 | 0 | 0 | 0.00% | `/system/lib64/libarkui_textclock.z.so` |
| `005d430e8000-005d430e9000` | .so | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `/system/lib64/libarkui_textclock.z.so` |
| `005d430e9000-005d430ea000` | FilePage other | `rw-p` | 4 | 4 | 4 | 0 | 0 | 0.00% | `[anon:libarkui_textclock.z.so.bss]` |
| `005d432ea000-005d432ec000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:31124]` |
| `005d433ed000-005d433ef000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:31123]` |
| `005d438ea000-005d438ec000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30491]` |
| `005d439ed000-005d439ef000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30492]` |
| `005d43af0000-005d43af2000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30493]` |
| `005d43bf3000-005d43bf5000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30494]` |
| `005d43cf6000-005d43cf8000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30495]` |
| `005d43cf8000-005d43df9000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30495]` |
| `005d43df9000-005d43dfb000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30496]` |
| `005d43dfb000-005d43efc000` | FilePage other | `rw-p` | 1028 | 12 | 12 | 0 | 0 | 0.00% | `[anon:stack:30496]` |
| `005d43efc000-005d43efe000` | guard | `---p` | 8 | 0 | 0 | 0 | 0 | 0.00% | `[anon:guard:30500]` |
| `005d43efe000-005d43fff000` | FilePage other | `rw-p` | 1028 | 8 | 8 | 0 | 0 | 0.00% | `[anon:stack:30500]` |
| `005d44308000-005d4438c000` | dev | `rw-s` | 528 | 528 | 264 | 0 | 0 | 0.00% | `anon_inode:dev/ashmem/EXTRawData` |
| `006f00000000-007000000000` | guard | `---p` | 4194304 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070d7609000-0070d764e000` | FilePage other | `rw-p` | 276 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070d764e000-0070d7693000` | FilePage other | `rw-p` | 276 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070d7693000-0070d76d8000` | FilePage other | `rw-p` | 276 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070d76d8000-0070d7718000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070d7718000-0070d7758000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070d7758000-0070d7798000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070d7798000-0070d77d8000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070d77d8000-0070df7d8000` | FilePage other | `rw-p` | 131072 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070df7d8000-0070df8e7000` | FilePage other | `-w-p` | 1084 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070df8e7000-0070dfae6000` | FilePage other | `-w-p` | 2044 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfae6000-0070dfbf5000` | FilePage other | `rw-p` | 1084 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfbf5000-0070dfc35000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfc35000-0070dfe34000` | FilePage other | `rw-p` | 2044 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfe34000-0070dfe3d000` | guard | `---p` | 36 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfe3d000-0070dfec9000` | FilePage other | `rw-p` | 560 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfec9000-0070dfecc000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfecc000-0070dfecd000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfecd000-0070dfece000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfece000-0070dfeee000` | FilePage other | `rw-p` | 128 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dfeee000-0070dff7a000` | FilePage other | `rw-p` | 560 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dff7a000-0070dff7d000` | FilePage other | `rw-p` | 12 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dff7d000-0070dff7e000` | FilePage other | `r--p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dff7e000-0070dff7f000` | FilePage other | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dff7f000-0070dff9f000` | FilePage other | `rw-p` | 128 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dff9f000-0070dffdf000` | FilePage other | `rw-p` | 256 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `0070dffdf000-0070dffff000` | FilePage other | `rw-p` | 128 | 0 | 0 | 0 | 0 | 0.00% | `[io]` |
| `007f686c8000-007f686c9000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[guard]` |
| `007f686c9000-007f686ca000` | stack | `rw-p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[stack]` |
| `007f686ca000-007f686cb000` | guard | `---p` | 4 | 0 | 0 | 0 | 0 | 0.00% | `[guard]` |
