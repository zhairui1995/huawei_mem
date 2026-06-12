#!/bin/bash
# Run the first Hypium user journey against the connected HarmonyOS PC.

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HYP_ROOT="$PROJECT_DIR/hypium"
PYTHON="$PROJECT_DIR/.venv-hypium/bin/python"

if [[ ! -x "$PYTHON" ]]; then
    echo "错误: Hypium 环境不存在: $PYTHON"
    echo "请先按 docs/hypium_automation_guide.md 安装。"
    exit 1
fi

source "$PROJECT_DIR/scripts/setup_env.sh"

DEVICE_SN="$(hdc list targets 2>/dev/null | awk 'NF {print $1; exit}')"
if [[ -z "$DEVICE_SN" ]]; then
    echo "错误: 未检测到 HDC 设备。"
    exit 2
fi

RUN_ID="$(date +%Y%m%d_%H%M%S)"
REPORT_DIR="$HYP_ROOT/reports/$RUN_ID"
mkdir -p "$PROJECT_DIR/.hypium-home" "$REPORT_DIR"

echo "设备: ${DEVICE_SN:0:4}...${DEVICE_SN: -4}"
echo "Hypium: $($PYTHON -m pip show hypium | awk '/^Version:/ {print $2}')"
echo "前后台切换次数: ${DOUYU_BACKGROUND_CYCLES:-3}"
echo "报告目录: $REPORT_DIR"

cd "$HYP_ROOT"
HOME="$PROJECT_DIR/.hypium-home" "$PYTHON" -m hypium run \
    -l DouyuUserJourney \
    -c config/user_config.xml \
    -sn "$DEVICE_SN" \
    -tcpath testcases \
    -rp "$REPORT_DIR" \
    -ta screenshot:true

SUMMARY_XML="$REPORT_DIR/summary_report.xml"
if [[ ! -f "$SUMMARY_XML" ]]; then
    echo "错误: Hypium 未生成 summary_report.xml"
    exit 3
fi

if grep -Eq 'failures="[1-9]|unavailable="[1-9]|errors="[1-9]' "$SUMMARY_XML"; then
    echo "错误: Hypium 用例失败，请检查 $REPORT_DIR"
    exit 4
fi

echo "Hypium 用例通过: $REPORT_DIR/summary_report.html"
