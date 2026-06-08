# mem_analyze v6
[[华为项目]]
v6 是从 v5 中单独拆出来的最小 Referenced 工作流版本，只保留这一条链路：

```text
clear_refs -> 执行用户操作脚本 -> 读取 smaps -> 输出 Referenced 表
```

echo 1 | sudo tee /proc/<pid>/clear_refs 本质上就是通过 Linux 的 /proc 虚拟文件系统，调用内核提供的一个控制接口，让内核清除该进程页的访问标记。

## 编译


```bash
gcc -Wall -Wextra -std=c11 -o mem_analyze-v6 mem_analyze-v6.c
```

## 推荐用法

修改 `user_operation.sh`，把你要观察的用户操作写进去。然后运行：

```bash
./run_referenced_workflow.sh <pid> -o referenced.md
./run_referenced_workflow.sh --app firefox -o firefox_referenced.md
```

启动脚本会自动执行：

1. `sudo ./mem_analyze-v6 --clear-refs <pid>`
2. `./user_operation.sh <pid>`
3. `sudo ./mem_analyze-v6 <pid> -o referenced.md`

也可以指定另一个操作脚本：

```bash
./run_referenced_workflow.sh <pid> -s ./open_doc.sh -o doc_referenced.md
./run_referenced_workflow.sh --app firefox -s ./open_doc.sh -o firefox_referenced.md
```

默认报告只输出报告头和 `Referenced 段汇总`。如果需要 VMA 级明细，增加
`--with-vma`：

```bash
./run_referenced_workflow.sh <pid> -o referenced.md --with-vma
./run_referenced_workflow.sh --app firefox -o firefox_referenced.md --with-vma
```

## 手动用法

```bash
sudo ./mem_analyze-v6 --clear-refs <pid>
# 执行你要观察的用户操作
sudo ./mem_analyze-v6 <pid> -o referenced.md
sudo ./mem_analyze-v6 <pid> -o referenced.md --with-vma
```

按 app 关键字匹配 `/proc/<pid>/comm` 和 `/proc/<pid>/cmdline`：

```bash
sudo ./mem_analyze-v6 --clear-refs --app firefox
# 执行你要观察的用户操作
sudo ./mem_analyze-v6 --app firefox -o firefox_referenced.md
sudo ./mem_analyze-v6 --app firefox -o firefox_referenced.md --with-vma
```

如果 `--app` 匹配到多个进程，v6 会分别输出文件，例如：

```text
firefox_referenced_pid_1234.md
firefox_referenced_pid_5678.md
```

## 输出

默认报告只包含：

- `Referenced 段汇总`：按 text/data/bss/heap/stack/file/anon/special 汇总

打开 `--with-vma` 后会额外输出：

- `Referenced VMA 定位`：按原始 VMA 列出 Referenced，默认从大到小排序

`Referenced(KiB)` 来自 `/proc/<pid>/smaps`。如果没有先执行 `--clear-refs`，
它就不是某次操作窗口内的访问结果。
