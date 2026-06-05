#!/usr/bin/env bash
set -euo pipefail

# 这个文件只放“要观察的用户操作”。
# run_referenced_workflow.sh 会在 clear_refs 之后调用它。
# 第一个参数是 PID 模式下的目标 PID；第二个参数是 --app 模式下的 app 关键字。
#
# 你可以把默认交互替换成自己的命令，例如：
#   xdg-open /path/to/document.pdf
#   sleep 5

TARGET_PID="${1:-}"
TARGET_APP="${2:-}"

echo "目标 PID: ${TARGET_PID:-未提供}"
echo "目标 app: ${TARGET_APP:-未提供}"
echo "现在请执行你要观察的用户操作。"
echo "操作完成后回到这个终端按 Enter，工作流会立即读取 smaps。"
read -r -p "按 Enter 继续采样..."
