#!/usr/bin/env bash
set -euo pipefail

# v7 会先把目标页对应的 PFN 标记为 idle，然后调用本脚本。
# 第一个参数是 PID，第二个参数是 --app 模式下的 app 关键字。

TARGET_PID="${1:-}"
TARGET_APP="${2:-}"

echo "目标 PID: ${TARGET_PID:-未提供}"
echo "目标 app: ${TARGET_APP:-未提供}"
echo "现在请执行你要观察的用户操作。"
echo "操作完成后回到这个终端按 Enter，v7 会读取 page_idle bitmap 并画图。"
read -r -p "按 Enter 继续..."
