# Hypium UI 自动化与内存采集接入指南

更新时间：2026-06-12

官方资料：
[应用 UI 测试（基于 Python）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines)

本文根据华为官方 Hypium Python 指南整理，目标是让 Hypium 自动执行鸿蒙应用操作序列，并与本项目 `memcap` 内存采集流程配合。

## 1. Hypium 能做什么

Hypium 是 HarmonyOS 的 Python UI 自动化测试框架，支持手机、平板和 PC。它主要负责：

- 启动、停止、安装、卸载和清理应用。
- 按文本、类型、控件 key、XPath、图片或坐标定位控件。
- 点击、长按、滑动、拖动、缩放、鼠标和键盘操作。
- 输入文本、按键和执行连续操作序列。
- 通过 HDC 或设备 shell 执行命令。
- 保存测试报告、设备日志、失败截图和录屏。
- 在 PyCharm 的 UiViewer 中查看控件树、录制操作并生成代码。

推荐定位优先级：

1. 控件属性：文本、类型、key，稳定性最高。
2. 图片匹配：适合无法从控件树识别的内容。
3. 屏幕比例坐标：最后的退化方案，容易受分辨率和窗口布局影响。

## 2. 与物理页采集的边界

Hypium 本身不提供解析 `/proc/kpageflags`、`/proc/kpagecount` 或 `/proc/[pid]/pagemap` 的专用 API。

这些文件属于 Linux/HarmonyOS 内核 procfs 接口，能否读取取决于：

- 当前系统版本是否导出该节点。
- HDC shell 的实际 UID、能力集和 SELinux/访问控制策略。
- 内核是否限制 PFN、页标志或页引用计数信息。
- 目标进程和采集进程之间的权限关系。

Hypium 可以通过 `driver.shell()` 或 `driver.hdc()` 间接执行设备命令，因此可以负责“操作应用”，再调用本项目的 `memcap` 读取可访问的 procfs 数据。Hypium 不会绕过内核权限。

## 3. 环境准备

官方建议使用 Python 3.10 和较新的 PyCharm。当前项目已使用隔离环境
`.venv-hypium` 安装 Hypium 6.1.0.210。

在线安装：

```bash
python3.10 -m venv .venv-hypium
source .venv-hypium/bin/activate
python -m pip install -U pip
python -m pip install hypium -U \
  --trusted-host mirrors.huaweicloud.com \
  -i https://mirrors.huaweicloud.com/repository/pypi/simple
```

当前仓库可直接运行：

```bash
bash scripts/setup_hypium_env.sh
```

确认 HDC 和设备：

```bash
source scripts/setup_env.sh
hdc list targets
hdc shell "id"
```

如果连接多个设备，在 Hypium 配置或运行命令中明确指定设备 SN，不要把真实 SN 写入仓库：

```bash
run -l MemorySequence -sn <device-sn>
```

## 4. Hypium 项目结构

官方模板的典型结构如下：

```text
hypium_project/
├── aw/
│   └── Utils.py
├── config/
│   └── user_config.xml
├── resource/
├── testcases/
│   ├── MemorySequence.py
│   └── MemorySequence.json
└── main.py
```

测试用例通常包含三个生命周期阶段：

- `setup`：连接设备、初始化驱动、启动应用、建立基线。
- `process`：执行点击、输入、滑动等操作序列和检查点。
- `teardown`：恢复应用状态、停止应用、保存日志或清理资源。

设备连接方式在 `config/user_config.xml` 中配置，USB HDC 使用 `usb-hdc`。需要截图或录屏时，可配置 `screenshot`、`screenrecorder` 等任务参数。

## 5. 常用 UI 操作

下面展示官方 API 的常见用法。实际项目应优先使用 UiViewer 获取真实控件属性。

```python
from hypium import BY
from hypium.model import KeyCode, MouseButton

# 按文本、类型和控件 key 定位并点击
driver.touch(BY.text("蓝牙"))
driver.touch(BY.text("蓝牙").type("Button").key("bluetooth_switch"))

# 查找一个或多个控件
component = driver.find_component(BY.key("search_input"))
components = driver.find_all_components(BY.type("ListItem"))

# 输入和清空文本
driver.input_text(BY.key("search_input"), "memory test")
driver.clear_text(BY.key("search_input"))

# 坐标和手势
driver.touch((0.52, 0.98))
driver.swipe((0.5, 0.8), (0.5, 0.2))
driver.drag((0.3, 0.5), (0.8, 0.5))

# 键盘
driver.press_key(KeyCode.ENTER)

# 鸿蒙 PC 鼠标操作
driver.mouse_click((100, 200), MouseButton.MOUSE_BUTTON_LEFT)
driver.mouse_move((400, 300))

# 应用生命周期
driver.start_app("<bundle-name>", "<ability-name>")
driver.stop_app("<bundle-name>")

# 设备 shell、HDC 和文件操作
driver.shell("id")
driver.hdc("list targets")
driver.push_file("<host-file>", "<device-file>")
driver.pull_file("<device-file>", "<host-file>")
```

## 6. 自动操作序列模板

下面是面向本项目的结构模板。控件 key、包名、Ability 名和导入路径需要按实际 Hypium 版本及被测应用替换。

```python
import time

from devicetest.core.test_case import TestCase, Step
from hypium import BY, UiDriver
from hypium.model import KeyCode


class MemorySequence(TestCase):
    def __init__(self, controllers):
        self.tag = self.__class__.__name__
        self.tests = [
            "test_launch",
            "test_search",
            "test_scroll",
        ]
        self.driver = UiDriver(controllers[0])

    def setup(self):
        Step("启动被测应用")
        self.driver.start_app("<bundle-name>", "<ability-name>")
        time.sleep(2)

    def process(self):
        Step("输入搜索内容")
        self.driver.touch(BY.key("<search-input-key>"))
        self.driver.input_text(BY.key("<search-input-key>"), "memory test")
        self.driver.press_key(KeyCode.ENTER)
        time.sleep(2)

        Step("滚动内容列表")
        self.driver.swipe((0.5, 0.8), (0.5, 0.2))
        time.sleep(1)

        Step("打开目标条目")
        self.driver.touch(BY.text("<target-text>"))
        time.sleep(2)

    def teardown(self):
        Step("结束被测应用")
        self.driver.stop_app("<bundle-name>")
```

建议把每个用户动作写成独立 `Step`，并使用稳定的操作 ID，例如：

```text
op_launch
op_search
op_scroll
op_open_item
op_switch_window
op_background
op_restore
```

## 7. 与 memcap 的推荐接入方式

本项目现有职责划分：

- Hypium：执行确定性的应用操作，并记录操作开始和完成时间。
- `scripts/collect.sh`：编译、推送和运行 `memcap`，采集单个时间点。
- `scripts/collect_session.sh`：当前为人工按 Enter 的会话编排，不适合直接嵌入无人值守 Hypium 用例。

自动化实验建议由 Hypium 在每个动作前后调用主机侧 `collect.sh`。仓库路径通过环境变量传入，不在测试代码中硬编码本地绝对路径：

```bash
export HUAWEI_MEM_ROOT="<huawei_mem-repo>"
```

Hypium 用例中的采集辅助函数可以写成：

```python
import os
import subprocess
import time


def collect_snapshot(target, app_label, operation_id, phase):
    repo = os.environ["HUAWEI_MEM_ROOT"]
    full_operation_id = f"{operation_id}_{phase}"
    subprocess.run(
        [
            "bash",
            "scripts/collect.sh",
            target,
            app_label,
            "-o",
            full_operation_id,
            "--no-push",
        ],
        cwd=repo,
        check=True,
        timeout=180,
    )
```

操作和采集顺序：

```python
collect_snapshot("com.example.app", "被测应用", "op_search", "before")

driver.touch(BY.key("search_input"))
driver.input_text(BY.key("search_input"), "memory test")
driver.press_key(KeyCode.ENTER)

collect_snapshot("com.example.app", "被测应用", "op_search", "after_0s")
time.sleep(1)
collect_snapshot("com.example.app", "被测应用", "op_search", "after_1s")
time.sleep(2)
collect_snapshot("com.example.app", "被测应用", "op_search", "after_3s")
time.sleep(2)
collect_snapshot("com.example.app", "被测应用", "op_search", "after_5s")
```

注意：上面的 `sleep` 是相对上一次采集的增量，因此依次等待 `1s + 2s + 2s`，对应操作后的 1、3、5 秒。

首次实验先单独运行一次 `collect.sh`，完成编译和推送：

```bash
source scripts/setup_env.sh
bash scripts/collect.sh <process-name> "<app-label>" -o prepare
```

后续 Hypium 操作序列使用 `--no-push`，避免每个快照都重新编译和传输二进制。

## 8. 直接在设备端调用 memcap

如果不希望从测试进程调用主机侧 `collect.sh`，也可以用 `driver.shell()` 直接执行已经推送到设备的二进制：

```python
driver.shell(
    "/data/local/tmp/memcap/memcap "
    "<pid> /data/local/tmp/memcap/out "
    "<sample-id> <operation-id> <app-id> "
    "'<app-label>' '<process-name>' <sample-index> foreground"
)
```

这种方式需要测试用例自行生成 sample ID、维护 sample index、解析 PID，并在会话结束后拉取结果。优先使用主机侧 `collect.sh`，因为它已经封装了这些逻辑。

## 9. 运行与报告

进入 Hypium 控制台：

```bash
python -m hypium
```

运行用例：

```bash
run -l MemorySequence
```

指定设备、报告目录和失败截图：

```bash
run -l MemorySequence \
  -sn <device-sn> \
  -rp reports/memory_sequence \
  -ta screenshot:true
```

重试某次报告会话：

```bash
run --retry --session <report-session>
```

报告通常包含：

- HTML/XML 汇总报告。
- 用例步骤和断言结果。
- 设备日志。
- 失败截图或录屏。
- 任务和会话记录。

Hypium 报告中的步骤名应与 `memcap_out/` 中的 `operation_id` 对齐，方便把 UI 行为、时间戳和内存快照关联起来。

## 10. 实验可靠性要求

- 第一次运行先用 UiViewer 验证控件 key 和窗口层级，避免依赖中文文本或固定坐标。
- 每个操作开始前等待界面稳定；使用控件存在条件优于固定长时间 sleep。
- 单次实验只允许一个采集流程写入同一设备输出目录。
- UI 操作失败时不要继续记录为有效内存样本；应在报告中标记失败。
- 保存 Hypium Step、操作 ID、应用 PID、前后台状态和采集时间戳。
- 多开应用和内存压力测试应与 UI 功能验证分开，先确认操作序列可复现，再逐步增加压力。
- `/proc/kpageflags`、`/proc/kpagecount` 和 pagemap 权限必须单独记录；节点存在不等于内容可读取。

## 11. 下一步实施建议

1. 安装 Hypium，并用 UiViewer 连接当前鸿蒙 PC。
2. 对一个应用录制“启动、点击、滚动、切换窗口、退后台、恢复”最小序列。
3. 用控件属性替换录制代码中的固定坐标。
4. 先运行纯 UI 用例，确认报告、日志和失败截图正常。
5. 在每个 Step 前后加入 `collect_snapshot()`。
6. 对齐 Hypium Step 名、`operation_id` 和 `sample_id`。
7. 再加入多应用并发和内存压力，观察 page fault、RSS、VMA 和物理页状态变化。
