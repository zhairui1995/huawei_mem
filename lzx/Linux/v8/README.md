# young/accessed bit referenced pages v8

v8 是只针对当前 Linux 内核的 young/accessed bit 页级访问定位版本。

它的输出与 v7 一致：生成逐页 TSV、bitmap 文本、Markdown 汇总和类似
`v3/pfn_delta_segments.png` 的 segment 聚合图。

区别是：v8 **不使用** `/sys/kernel/mm/page_idle/bitmap`，也不依赖 PFN。
它通过自定义 Linux 内核模块 `/dev/v8_page_access` 直接对目标进程虚拟地址范围的
PTE/PMD young(accessed) bit 做 clear/query。

## 原理

```text
用户态:
  /proc/<pid>/maps -> 选定 VMA / segment / vaddr range -> ioctl 调 Linux 内核模块

内核态:
  pid + vaddr range
    -> task_struct / mm_struct
    -> 手动遍历页表 PTE/PMD
    -> clear 阶段清除 young(accessed) bit
    -> query 阶段检查 young(accessed) bit 是否又被置位

用户态:
  referenced / idle / not_present / error -> TSV + bitmap 文本 -> Python 绘图
```

## 编译

需要当前 Linux 内核对应的 kernel headers：

```bash
cd /home/lzx/桌面/513test/v8
make
chmod +x run_page_access_workflow.sh user_operation.sh draw_page_access.py
```

绘图阶段需要 Python 的 `matplotlib`：

```bash
sudo apt install python3-matplotlib
```

如果只想先编译用户态程序：

```bash
make user
```

保存当前 Linux 构建产物：

```bash
make save-linux
```

重新编译并自动保存当前 Linux 版本：

```bash
make linux-artifact
```

默认保存到：

```text
artifacts/linux-<当前内核版本>-<当前架构>/
```

## 加载内核模块

```bash
sudo insmod v8_page_access.ko
ls -l /dev/v8_page_access
```

卸载：

```bash
sudo rmmod v8_page_access
```

## 用法

```bash
cd /home/lzx/桌面/513test/v8
sudo ./run_page_access_workflow.sh <pid> -o page_access_segments.png
```

按 segment 缩小范围：

```bash
sudo ./run_page_access_workflow.sh <pid> --segment heap -o heap_access.png
sudo ./run_page_access_workflow.sh <pid> --segment data -o data_access.png
```

按虚拟地址范围缩小：

```bash
sudo ./run_page_access_workflow.sh <pid> --vma 7f0000000000-7f0000100000 -o vma_access.png
```

按 app 关键字匹配：

```bash
sudo ./run_page_access_workflow.sh --app firefox -o firefox_access.png
```

## 用户操作脚本

默认调用 `user_operation.sh`。你可以直接修改它，或者指定其他脚本：

```bash
sudo ./run_page_access_workflow.sh <pid> -s ./open_doc.sh -o doc_access.png
```

脚本会收到两个参数：

```text
$1 = PID
$2 = app 关键字，非 --app 模式为空
```

## 输出文件

假设输出为 `page_access_segments.png`，还会生成：

- `page_access_segments.md`：segment 汇总表
- `page_access_segments.tsv`：逐页状态
- `page_access_segments_bitmap.txt`：v7 兼容的 bitmap 文本，Python 根据它绘图

状态含义：

- `referenced`：clear 后到 query 前，该页 young/accessed bit 又被置位
- `idle`：query 时该页 present，但 young/accessed bit 没有再次置位
- `not_present`：页表中没有 present PTE/PMD
- `error`：内核遍历或 ioctl 失败

## 注意

v8 需要 root/CAP_SYS_ADMIN，因为内核模块 ioctl 会直接操作其他进程页表。
这版不使用 `/sys/kernel/mm/page_idle/bitmap`，因此不会有 v7 的 page_idle bitmap
写入开销，也不会依赖 pagemap 暴露 PFN。

当前实现为了能作为外部 `.ko` 编译，手动遍历页表并用页表宏清除 young bit。
Linux 没有向外部模块导出完整的 `walk_page_range()`、`ptep_test_and_clear_young()`
和进程 TLB flush 接口，所以严格生产版最好做成内核树内补丁或内核内置模块。
外部模块版本可能对已经停留在 TLB 中的页产生低估，适合实验验证和对比分析。
