# mem_analyze-v5 使用说明
[[华为项目]]

`mem_analyze-v5` 基于 v3，重点新增 `Referenced` 观察窗口：

1. 对目标进程写 `/proc/<pid>/clear_refs=1`
2. 执行要观察的用户操作
3. 读取 `/proc/<pid>/smaps`
4. 按 VMA 和 segment 汇总 `Referenced`

`Referenced` 代表自清空标记后被访问过的驻留页规模，适合做“这次操作访问了哪些
VMA/数据段”的定位。

## 编译

```bash
gcc -Wall -Wextra -std=c11 -o mem_analyze-v5 mem_analyze-v5.c
```

## 基本流程

推荐使用固定启动脚本，把用户操作单独写在 `user_operation.sh` 中：

```bash
./run_referenced_workflow.sh <pid> -o referenced.md
```

`run_referenced_workflow.sh` 会依次清空 referenced、执行 `user_operation.sh`、
然后立即采样。以后测试不同操作时，只改 `user_operation.sh` 即可。

手动流程如下：

```bash
sudo ./mem_analyze-v5 --clear-refs <pid>
# 执行用户操作
sudo ./mem_analyze-v5 <pid> -o referenced.md
```

输出中的重点章节：

| 章节 | 作用 |
| --- | --- |
| `Referenced 段汇总` | 按一级 segment 汇总操作后被访问过的页 |
| `Referenced VMA 定位` | 按原始 VMA 定位访问热点 |
| `Section 细分汇总` | 保留 v3 的 section 视图，并增加 `Referenced(KiB)` |
| `page_data.tsv` | 机器可读逐页数据，供后续脚本使用 |

## 按应用名使用

```bash
sudo ./mem_analyze-v5 --clear-refs --app firefox
# 执行用户操作
sudo ./mem_analyze-v5 --app firefox -o firefox_referenced.md
```

## Markdown 输出

默认 compact 模式只写轻量表格和 `page_data.tsv`。需要更多明细时：

```bash
sudo ./mem_analyze-v5 <pid> -o referenced.md --md-preset standard
sudo ./mem_analyze-v5 <pid> -o referenced.md --md-preset full
sudo ./mem_analyze-v5 <pid> -o referenced.md --with-vma-details --with-pfn-markdown
```

可选开关包括 `--with-target-segments`、`--with-vma-details`、
`--with-page-bitmaps`、`--with-pfn-markdown`、`--with-fields`、
`--with-full-report` 和 `--with-all-markdown`。

## 结果解读

`Referenced(KiB)` 是 smaps 字段，不是 v5 自己做的页级扫描。它适合判断
“访问过多少驻留页”，但不能精确给出每一个虚拟页地址是否被访问。v5 的定位粒度是
VMA 级，并按现有 segment/section 逻辑做汇总。
