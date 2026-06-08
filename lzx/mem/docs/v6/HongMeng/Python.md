# v6-python：主机端 hdc smaps 采集器
[[华为项目]]
`v6-python` 是 v6 的纯 Python 实现。它不交叉编译、不推送设备侧二进制，而是在 Windows/主机端通过 `hdc shell` 直接读取鸿蒙设备的 `/proc/<pid>/maps`、`/proc/<pid>/smaps` 等文本文件，再在本机解析并生成 Markdown 报告。

核心流程：

```text
hdc shell 写 clear_refs -> 执行目标操作 -> hdc shell 读取 smaps -> Python 解析 -> 输出报告
```

## 和 v6-Homeny C 版的区别

- Python 版：更容易修改和排查，不需要 OpenHarmony native SDK，不需要推送可执行文件。
- C 版：设备侧本地解析，通常更快，更适合大进程、高频采样或批量采样。
- 两者都只做 v6 的 `maps/smaps/clear_refs` 文本采集，不做 pagemap、PFN、page_idle。

## 环境要求

- 本机可以运行 `python`。
- `hdc list targets` 能看到鸿蒙设备。
- `hdc shell` 对目标进程有权限：
  - 写 `/proc/<pid>/clear_refs`
  - 读 `/proc/<pid>/smaps`

快速检查：

```powershell
hdc list targets
hdc shell "id; ls -l /proc/self/smaps /proc/self/clear_refs"
```

## 用法

按 PID 采集：

```powershell
python .\lzx-Test1\v6-python\collect_hdc_v6.py --target 12345 --with-vma
```

按应用/包名关键字采集：

```powershell
python .\lzx-Test1\v6-python\collect_hdc_v6.py --target com.example.app --with-vma
```

指定输出目录：

```powershell
python .\lzx-Test1\v6-python\collect_hdc_v6.py --target 12345 --out .\py_out
```

自动执行操作命令：

```powershell
python .\lzx-Test1\v6-python\collect_hdc_v6.py --target com.example.app `
  --operation-cmd "hdc shell echo noop" `
  --with-vma
```

保存原始文件，方便排查解析问题：

```powershell
python .\lzx-Test1\v6-python\collect_hdc_v6.py --target 12345 --save-raw --with-vma
```

如果只想采样当前 `smaps`，不清空 `clear_refs`：

```powershell
python .\lzx-Test1\v6-python\collect_hdc_v6.py --target 12345 --skip-clear-refs
```

## 参数说明

- `--target` / `-t`：目标 PID 或应用/包名关键字。纯数字按 PID 处理，其他内容按关键字匹配。
- `--out` / `-o`：输出目录，默认是 `v6-python/hdc_out`。
- `--operation-cmd`：在清空 `clear_refs` 后、读取 `smaps` 前执行的本机命令。
- `--with-vma`：在报告中追加 VMA 级明细表。
- `--save-raw`：保存原始 `maps/smaps/comm/cmdline/exe` 文本。
- `--skip-clear-refs`：跳过清空 `clear_refs`，只读取当前 `smaps`。

## 输出

默认输出 Markdown 报告：

```text
v6-python/hdc_out/referenced_YYYYMMDD_HHMMSS.md
```

启用 `--save-raw` 后，会额外保存：

```text
v6-python/hdc_out/raw_YYYYMMDD_HHMMSS/pid_<pid>/maps.txt
v6-python/hdc_out/raw_YYYYMMDD_HHMMSS/pid_<pid>/smaps.txt
v6-python/hdc_out/raw_YYYYMMDD_HHMMSS/pid_<pid>/comm.txt
v6-python/hdc_out/raw_YYYYMMDD_HHMMSS/pid_<pid>/cmdline.txt
v6-python/hdc_out/raw_YYYYMMDD_HHMMSS/pid_<pid>/exe.txt
```

## 常见问题

- `clear_refs` 失败：当前 `hdc shell` 对目标进程权限不足，或目标进程已经退出。
- `smaps` 读取失败：PID 不存在、进程退出，或 `/proc` 权限受限。
- 按关键字找不到进程：先启动应用，再用 `hdc shell "ps -A -o PID,ARGS"` 确认关键字是否匹配。
- 采集慢：大进程的 `smaps` 很长，Python 版需要通过 `hdc shell cat` 拉回全文；高频采样建议使用 `v6-Homeny` 的 C 版。
