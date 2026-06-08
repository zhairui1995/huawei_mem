# collect_hdc_v6.ps1 阅读文档

本文用于阅读和维护 `collect_hdc_v6.ps1`。它解释脚本做了什么、每个参数的作用、关键变量如何流转，以及排查问题时应该看哪里。

## 1. 脚本定位

`collect_hdc_v6.ps1` 是 v6-Homeny 的 Windows PowerShell 主入口。

它负责把本地 C 采集器编译成鸿蒙设备可执行文件，通过 `hdc` 推送到设备，在设备上执行 v6 的 Referenced 采集流程，并把报告拉回本地。

核心链路是：

```text
mem_analyze-v6.c
  -> OpenHarmony clang 交叉编译
  -> mem_analyze-v6-ohos
  -> hdc file send 到设备
  -> hdc shell 执行 clear_refs
  -> 用户操作或 OperationCommand
  -> hdc shell 执行 smaps 采样
  -> 设备端生成 Markdown 报告
  -> hdc file recv 拉回本地
```

这版脚本不是 Python 主机端解析方案。真正读取 `/proc/<pid>/smaps` 并生成报告的是设备侧二进制：

```text
/data/local/tmp/mem_analyze_v6/mem_analyze-v6
```

## 2. 参数说明

脚本参数位于文件开头的 `param(...)`：

```powershell
param(
    [Parameter(Position = 0)]
    [string]$Target,

    [string]$Out = "",
    [string]$DeviceDir = "/data/local/tmp/mem_analyze_v6",
    [string]$DeviceOut = "/storage/media/100/local/files/Docs/Desktop/output-lzx",
    [string]$OperationCommand = "",

    [switch]$WithVma,
    [switch]$NoBuild,
    [switch]$NoPush,
    [switch]$Help
)
```

### `Target`

目标进程。可以是 PID，也可以是应用/包名关键字。

- 纯数字：按 PID 处理，例如 `29616`
- 非纯数字：按 `--app <keyword>` 传给设备侧采集器，例如 `com.douyu.ho.app`

脚本中的判断逻辑：

```powershell
if ($Target -match '^[0-9]+$') {
    $TargetArgs += $Target
} else {
    $TargetArgs += "--app"
    $TargetArgs += $Target
}
```

### `Out`

本地输出目录。

默认值是空字符串，后续会被设置为脚本同目录下的 `hdc_out`：

```powershell
if ([string]::IsNullOrWhiteSpace($Out)) {
    $Out = Join-Path $ScriptDir "hdc_out"
}
```

最终拉回本地时使用：

```powershell
hdc file recv $DeviceOut $Out
```

### `DeviceDir`

设备侧二进制工作目录，默认：

```text
/data/local/tmp/mem_analyze_v6
```

脚本会把设备侧可执行文件放到：

```text
/data/local/tmp/mem_analyze_v6/mem_analyze-v6
```

### `DeviceOut`

设备侧报告输出目录，当前默认：

```text
/storage/media/100/local/files/Docs/Desktop/output-lzx
```

采集报告会写成：

```text
/storage/media/100/local/files/Docs/Desktop/output-lzx/referenced_YYYYMMDD_HHMMSS.md
```

使用单独的 `output-lzx` 目录有一个好处：`hdc file recv` 不会把整个 `Docs/Desktop` 目录里其他文件一起拉回。

### `OperationCommand`

在 `clear_refs` 后、采样 `smaps` 前执行的本机命令。

例如：

```powershell
-OperationCommand 'hdc shell "aa start -a EntryAbility -b com.example.app"'
```

如果不传这个参数，脚本会暂停，等待用户手动操作设备，然后按 Enter 继续。

### `WithVma`

是否输出 VMA 级明细表。

启用后，脚本会给设备侧采集器追加：

```text
--with-vma
```

报告中会多出 `Referenced VMA 定位` 表。

### `NoBuild`

跳过交叉编译。

适合本地已经有可用的：

```text
mem_analyze-v6-ohos
```

### `NoPush`

跳过推送设备侧二进制。

适合设备上已经存在最新的：

```text
/data/local/tmp/mem_analyze_v6/mem_analyze-v6
```

### `Help`

打印帮助文本并退出。

## 3. 关键变量

脚本根据参数拼出几个核心路径：

```powershell
$Source = Join-Path $ScriptDir "mem_analyze-v6.c"
$LocalBin = Join-Path $ScriptDir "mem_analyze-v6-ohos"
$DeviceBin = "$DeviceDir/mem_analyze-v6"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$DeviceReport = "$DeviceOut/referenced_$Timestamp.md"
```

含义：

- `$Source`：C 源码
- `$LocalBin`：本地交叉编译产物
- `$DeviceBin`：设备侧可执行文件路径
- `$Timestamp`：本次采样时间戳
- `$DeviceReport`：设备端最终报告路径

## 4. 函数说明

### `Show-Usage`

打印脚本用法、参数说明和示例。

触发方式：

```powershell
.\collect_hdc_v6.ps1 -Help
```

### `Invoke-External`

统一执行外部命令，并检查 `$LASTEXITCODE`。

核心逻辑：

```powershell
& $FilePath @Arguments
if ($LASTEXITCODE -ne 0) {
    throw "Command failed ..."
}
```

脚本中所有关键外部命令都通过它执行，例如：

- `clang.exe`
- `hdc list targets`
- `hdc shell ...`
- `hdc file send ...`
- `hdc file recv ...`

### `Get-DefaultSdkPath`

在没有设置 `$env:OHOS_SDK` 时，尝试使用默认 DevEco Studio SDK 路径：

```text
D:\Program Files\Huawei\DevEco Studio\sdk\default\openharmony\native
```

如果你的 SDK 不在这个位置，需要先设置环境变量：

```powershell
$env:OHOS_SDK = "你的 openharmony native SDK 路径"
```

## 5. 执行流程详解

### 5.1 参数校验

如果传入 `-Help`，直接打印帮助并退出。

如果没有 `Target`，脚本会打印帮助并报错：

```powershell
throw "Missing -Target <pid|app_keyword>."
```

### 5.2 确定本地输出目录

如果没有显式传 `-Out`，默认输出到：

```text
v6-Homeny/hdc_out
```

### 5.3 编译设备侧采集器

如果没有传 `-NoBuild`，脚本会查找 OpenHarmony native SDK。

优先级：

1. `$env:OHOS_SDK`
2. DevEco Studio 默认路径

编译命令等价于：

```powershell
clang.exe -O2 -std=c11 -Wall -Wextra `
  -target aarch64-linux-ohos `
  --sysroot=<OHOS_SDK>\sysroot `
  -o mem_analyze-v6-ohos mem_analyze-v6.c
```

这里生成的是鸿蒙设备可执行的 AArch64 ELF 文件。

### 5.4 检查本地二进制

无论是否跳过编译，脚本都会确认本地存在：

```text
mem_analyze-v6-ohos
```

如果不存在，会提示先编译或去掉 `-NoBuild`。

### 5.5 推送设备侧二进制

如果没有传 `-NoPush`，脚本执行：

```powershell
hdc shell "mkdir -p '$DeviceDir' '$DeviceOut'"
hdc file send $LocalBin $DeviceBin
hdc shell "chmod 755 '$DeviceBin'"
```

这里会同时创建：

- 设备侧二进制目录 `$DeviceDir`
- 设备侧报告目录 `$DeviceOut`

### 5.6 生成目标参数

如果 `Target` 是纯数字：

```text
29616
```

设备侧命令会直接传 PID：

```text
mem_analyze-v6 29616 ...
```

如果 `Target` 不是纯数字：

```text
com.douyu.ho.app
```

设备侧命令会变成：

```text
mem_analyze-v6 --app com.douyu.ho.app ...
```

### 5.7 设备和权限检查

脚本会执行：

```powershell
hdc list targets
hdc shell "id; ls -l /proc/self/smaps /proc/self/clear_refs"
```

这一步用于确认：

- 设备是否在线
- `hdc shell` 当前身份
- 是否能访问 `smaps`
- 是否能写 `clear_refs`

### 5.8 清空 Referenced 标记

脚本拼出：

```powershell
$clearCmd = @("'$DeviceBin'", "--clear-refs") + $TargetArgs
```

然后执行：

```powershell
hdc shell "<DeviceBin> --clear-refs <target>"
```

这一步会让设备侧程序写：

```text
/proc/<pid>/clear_refs
```

注意：如果目标进程仍在运行，它会马上重新访问一些内存页。因此“没有手动操作”不等于 `Referenced` 必然为 0。

### 5.9 执行观察窗口内操作

如果没有传 `-OperationCommand`，脚本会暂停：

```text
Referenced bits are cleared. Perform the target operation on the HarmonyOS device now.
Press Enter to sample smaps
```

你在设备上完成要观察的操作后，回到终端按 Enter。

如果传了 `-OperationCommand`，脚本会执行：

```powershell
Invoke-Expression $OperationCommand
```

例如：

```powershell
-OperationCommand 'hdc shell echo noop'
```

### 5.10 采样 smaps 并生成报告

脚本拼出：

```powershell
$sampleCmd = @("'$DeviceBin'") + $TargetArgs + @("-o", "'$DeviceReport'")
```

如果传了 `-WithVma`，追加：

```text
--with-vma
```

最终执行类似：

```powershell
hdc shell "/data/local/tmp/mem_analyze_v6/mem_analyze-v6 29616 -o /storage/media/100/local/files/Docs/Desktop/output-lzx/referenced_20260531_201403.md --with-vma"
```

设备侧程序会读取：

```text
/proc/<pid>/smaps
```

并在设备端生成 Markdown 报告。

### 5.11 拉回报告

脚本执行：

```powershell
New-Item -ItemType Directory -Force -Path $Out
hdc file recv $DeviceOut $Out
```

如果 `$DeviceOut` 是：

```text
/storage/media/100/local/files/Docs/Desktop/output-lzx
```

本地输出通常会落到：

```text
v6-Homeny/hdc_out/output-lzx/referenced_YYYYMMDD_HHMMSS.md
```

具体目录结构取决于 `hdc file recv` 对目录名的保留方式。

## 6. 常用命令

### 按 PID 采集

```powershell
.\collect_hdc_v6.ps1 -Target 29616 -WithVma
```

### 按包名/关键字采集

```powershell
.\collect_hdc_v6.ps1 -Target com.douyu.ho.app -WithVma
```

### 不重新编译

```powershell
.\collect_hdc_v6.ps1 -Target 29616 -NoBuild -WithVma
```

### 不重新推送

```powershell
.\collect_hdc_v6.ps1 -Target 29616 -NoBuild -NoPush -WithVma
```

### 自动执行一个空操作

用于测后台基线：

```powershell
.\collect_hdc_v6.ps1 -Target 29616 -OperationCommand 'hdc shell echo noop' -WithVma
```

### 修改设备报告目录

```powershell
.\collect_hdc_v6.ps1 -Target 29616 -DeviceOut /storage/media/100/local/files/Docs/Desktop/output-lzx -WithVma
```

## 7. 输出报告怎么理解

报告中的核心字段：

- `Size`：VMA 虚拟地址空间大小
- `Rss`：当前驻留物理内存
- `Pss`：按共享比例折算后的驻留内存
- `Referenced`：观察窗口内被访问过的驻留页
- `Swap`：换出内存

`Referenced` 的语义最重要：

```text
Referenced = clear_refs 之后，到 smaps 采样时，这段时间内被访问过的驻留页
```

它不是“用户手动操作独占产生的访问量”。即使你没有触摸屏幕，目标进程的后台线程、系统回调、播放器、渲染、GC、日志等也可能访问内存。

要分析某个用户操作的增量，建议：

1. 先跑一次 `OperationCommand = hdc shell echo noop` 得到后台基线。
2. 再跑真实操作。
3. 对比两次报告中的 `Referenced` 差异。

## 8. 常见问题和定位方式

### 设备未连接

现象：

```text
hdc list targets
```

为空或报错。

处理：

```powershell
hdc kill
hdc start
hdc list targets
```

同时检查 USB 调试授权。

### 编译失败

常见原因：

- `$env:OHOS_SDK` 没设置
- DevEco Studio SDK 不在默认路径
- `clang.exe` 或 `sysroot` 不存在

检查：

```powershell
$env:OHOS_SDK
Test-Path "$env:OHOS_SDK\llvm\bin\clang.exe"
Test-Path "$env:OHOS_SDK\sysroot"
```

### 推送失败

检查设备目录是否可创建：

```powershell
hdc shell "mkdir -p /data/local/tmp/mem_analyze_v6 && ls -ld /data/local/tmp/mem_analyze_v6"
```

### `clear_refs` 失败

通常是权限不足或 PID 不存在。

检查：

```powershell
hdc shell "ls -l /proc/<pid>/clear_refs"
hdc shell "ps -A -o PID,ARGS | grep <keyword>"
```

### `smaps` 读取失败

检查：

```powershell
hdc shell "ls -l /proc/<pid>/smaps"
hdc shell "cat /proc/<pid>/smaps | head"
```

### 设备端有文件但桌面看不到

`/storage/media/100/local/files/Docs/Desktop/output-lzx` 是文件系统路径，不一定等价于 Launcher 桌面图标区域。

直接用命令确认：

```powershell
hdc shell "ls -l /storage/media/100/local/files/Docs/Desktop/output-lzx"
```

### 本地拉回了多余文件

如果把 `DeviceOut` 设置成公共目录本身，例如：

```text
/storage/media/100/local/files/Docs/Desktop
```

那么 `hdc file recv` 会拉回这个目录下所有文件。

因此推荐使用子目录：

```text
/storage/media/100/local/files/Docs/Desktop/output-lzx
```

## 9. 维护建议

- 如果只改报告保存位置，优先改 `$DeviceOut`，不要改 `$DeviceDir`。
- 如果只想复用已部署二进制，用 `-NoBuild -NoPush`。
- 如果修改了 `mem_analyze-v6.c`，不要使用 `-NoBuild`。
- 如果设备侧二进制可能是旧的，不要使用 `-NoPush`。
- 如果要调试脚本命令，先使用 `-OperationCommand 'hdc shell echo noop'` 降低变量。
