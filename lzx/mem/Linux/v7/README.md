# page_idle referenced pages v7

v7 用 `pagemap + /sys/kernel/mm/page_idle/bitmap` 精确定位一次用户操作期间
哪些物理页被访问过，并输出类似 `v3/pfn_delta_segments.png` 的 segment 聚合图。

## 原理

```text
1. 找到目标 PID / VMA
2. 读取 pagemap，得到每个虚拟页对应的 PFN
3. 把这些 PFN 写入 page_idle bitmap，标记为 idle
4. 执行用户操作
5. 再读 page_idle bitmap
6. idle bit 被清掉的页，就是期间被访问过的页
```

需要 root/CAP_SYS_ADMIN，否则 pagemap 可能隐藏 PFN，page_idle bitmap 也可能无法写入。

## 编译

```bash
cd /home/lzx/桌面/513test/v7
gcc -Wall -Wextra -std=c11 -O2 -o page_idle_collect page_idle_collect.c
chmod +x run_page_idle_workflow.sh user_operation.sh draw_page_idle.py
```

## 用法

```bash
cd /home/lzx/桌面/513test/v7
sudo ./run_page_idle_workflow.sh <pid> -o page_idle_segments.png
```

默认扫描目标进程所有 VMA。也可以缩小范围：

```bash
sudo ./run_page_idle_workflow.sh <pid> --segment heap -o heap_idle.png
sudo ./run_page_idle_workflow.sh <pid> --vma 7f0000000000-7f0000100000 -o vma_idle.png
```

按 app 匹配：

```bash
sudo ./run_page_idle_workflow.sh --app firefox -o firefox_idle.png
```

`--app` 必须只匹配到一个 PID，避免误标记多个进程共享 PFN。

## 用户操作脚本

默认调用 `user_operation.sh`。你可以修改这个文件，或者指定其他脚本：

```bash
sudo ./run_page_idle_workflow.sh <pid> -s ./open_doc.sh -o doc_idle.png
```

脚本会收到两个参数：

```text
$1 = PID
$2 = app 关键字，非 --app 模式为空
```

如果你用 `sudo ./run_page_idle_workflow.sh ...` 启动，v7 会在执行用户操作脚本时
自动降回 `$SUDO_USER`，这样打开 GUI、访问用户目录等操作仍按普通用户身份执行。

## 输出文件

假设输出为 `page_idle_segments.png`，还会生成：

- `page_idle_segments.md`：segment 汇总表
- `page_idle_segments.tsv`：逐页状态，包含虚拟地址、segment、PFN、状态、路径
- `page_idle_segments_bitmap.txt`：C 程序输出的 v3 风格 bitmap 文本，Python 根据它绘图

状态含义：

- `referenced`：操作期间访问过，idle bit 被清掉
- `idle`：操作后仍 idle
- `not_present`：虚拟页未驻留
- `pfn_hidden`：PFN 不可见
- `error`：读取失败

## 单独运行两步

如果不想用 bash 总入口，也可以手动分两步：

```bash
sudo ./page_idle_collect <pid> -s ./user_operation.sh -o page_idle_segments.tsv --bitmap page_idle_segments_bitmap.txt
python3 ./draw_page_idle.py page_idle_segments_bitmap.txt -o page_idle_segments.png --summary page_idle_segments.md
```
