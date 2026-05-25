#!/bin/bash
# memcap 一键采集脚本
# 用法: ./collect.sh <PID> [app_name] [options]
#
# 示例:
#   ./collect.sh 42820 斗鱼
#   ./collect.sh 42820 斗鱼 -o op_launch    # 指定操作ID
#   ./collect.sh 42820                      # 不指定应用名，自动查询
#
# 选项:
#   -o <operation_id>   操作ID（默认 auto_YYYYMMDD_HHMMSS）
#   -a <app_id>         应用ID（默认 app_auto）
#   -f <fg_state>       前后台状态（默认 foreground）
#   -d <out_dir>        设备端输出目录（默认 /data/local/tmp/memcap/out）
#   --no-push           跳过推送 memcap 二进制
#   --no-pull           跳过拉回结果

set -euo pipefail
export MSYS_NO_PATHCONV=1

# ====== 配置 ======
CLANG="/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native/llvm/bin/clang"
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MEMCAP_SRC="$PROJECT_DIR/memcap.c"
MEMCAP_BIN="$PROJECT_DIR/memcap"
DEVICE_BIN="/data/local/tmp/memcap/memcap"
DEVICE_OUT="/data/local/tmp/memcap/out"
LOCAL_OUT="$PROJECT_DIR/memcap_out"

# ====== 默认值 ======
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
OPERATION_ID="auto_${TIMESTAMP}"
APP_ID="app_auto"
FG_STATE="foreground"
DO_PUSH=true
DO_PULL=true
SAMPLE_INDEX="1"

# ====== 解析参数 ======
PID=""
APP_NAME=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -o) OPERATION_ID="$2"; shift 2 ;;
        -a) APP_ID="$2"; shift 2 ;;
        -f) FG_STATE="$2"; shift 2 ;;
        -d) DEVICE_OUT="$2"; shift 2 ;;
        --no-push) DO_PUSH=false; shift ;;
        --no-pull) DO_PULL=false; shift ;;
        -*)
            echo "未知选项: $1"
            echo "用法: $0 <PID> [app_name] [-o op_id] [-a app_id] [-f fg_state] [--no-push] [--no-pull]"
            exit 1
            ;;
        *)
            if [[ -z "$PID" ]]; then
                PID="$1"
            elif [[ -z "$APP_NAME" ]]; then
                APP_NAME="$1"
            else
                echo "多余参数: $1"
                exit 1
            fi
            shift
            ;;
    esac
done

if [[ -z "$PID" ]]; then
    echo "用法: $0 <PID> [app_name]"
    echo ""
    echo "示例:"
    echo "  $0 42820 斗鱼"
    echo "  $0 42820 斗鱼 -o op_launch"
    echo "  $0 42820            # 自动从设备获取进程名"
    echo ""
    echo "查看可用进程:"
    echo "  hdc shell ps -A -o PID,ARGS"
    exit 1
fi

# ====== 获取进程名 ======
PROCESS_NAME=""
if [[ -z "$APP_NAME" ]]; then
    # 从设备自动获取
    PROCESS_NAME="$(hdc shell "cat /proc/$PID/cmdline 2>/dev/null | tr '\0' ' '" 2>/dev/null || echo "unknown")"
    APP_NAME="$PROCESS_NAME"
else
    PROCESS_NAME="$(hdc shell "cat /proc/$PID/cmdline 2>/dev/null | tr '\0' ' '" 2>/dev/null || echo "unknown")"
fi
SAMPLE_ID="sample_${TIMESTAMP}"

echo "============================================"
echo "  memcap 内存快照采集"
echo "============================================"
echo "  PID:            $PID"
echo "  进程名:         $PROCESS_NAME"
echo "  应用名:         $APP_NAME"
echo "  Sample ID:      $SAMPLE_ID"
echo "  Operation ID:   $OPERATION_ID"
echo "  App ID:         $APP_ID"
echo "  前后台:         $FG_STATE"
echo "  设备输出目录:   $DEVICE_OUT"
echo "============================================"
echo ""

# ====== 编译 ======
if [[ "$DO_PUSH" == true ]]; then
    echo "[1/4] 编译 memcap..."
    if [[ ! -f "$CLANG" ]]; then
        echo "错误: 找不到 clang: $CLANG"
        exit 2
    fi
    "$CLANG" -O2 -std=c11 -Wall -Wextra \
        -target aarch64-linux-ohos \
        --sysroot="/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/native/sysroot" \
        -o "$MEMCAP_BIN" "$MEMCAP_SRC"
    echo "      编译完成: $MEMCAP_BIN"

    # ====== 推送 ======
    echo "[2/4] 推送 memcap 到设备..."
    hdc shell "mkdir -p /data/local/tmp/memcap"
    hdc file send "$MEMCAP_BIN" "$DEVICE_BIN"
    hdc shell "chmod 755 $DEVICE_BIN"
    echo "      推送完成"
else
    echo "[1/4] 跳过编译"
    echo "[2/4] 跳过推送"
fi

# ====== 运行采集 ======
echo "[3/4] 运行内存采集..."

# 递增 snapshot_index（如果已有采集记录）
EXISTING_COUNT="$(hdc shell "wc -l < $DEVICE_OUT/snapshot_index.csv 2>/dev/null" 2>/dev/null || echo "0")"
EXISTING_COUNT="${EXISTING_COUNT//[$'\r\n']/}"
if [[ "$EXISTING_COUNT" =~ ^[0-9]+$ ]] && [[ "$EXISTING_COUNT" -gt 0 ]]; then
    SAMPLE_INDEX="$EXISTING_COUNT"
fi

hdc shell "$DEVICE_BIN $PID $DEVICE_OUT $SAMPLE_ID $OPERATION_ID $APP_ID '$APP_NAME' '$PROCESS_NAME' $SAMPLE_INDEX $FG_STATE"
echo "      采集完成"

# ====== 拉回结果 ======
if [[ "$DO_PULL" == true ]]; then
    echo "[4/4] 拉回结果..."
    rm -rf "$LOCAL_OUT"
    hdc file recv "$DEVICE_OUT" "$LOCAL_OUT"
    echo "      结果保存到: $LOCAL_OUT"
    echo ""
    echo "============================================"
    echo "  采集完成!"
    echo "============================================"
    echo "  结果目录: $LOCAL_OUT"
    echo ""
    echo "  CSV 文件:"
    for f in "$LOCAL_OUT"/*.csv; do
        lines=$(wc -l < "$f" 2>/dev/null || echo "0")
        size=$(du -h "$f" 2>/dev/null | cut -f1 || echo "0")
        printf "    %-35s %6s 行  %s\n" "$(basename "$f")" "$lines" "$size"
    done
    echo ""
    echo "  查看快照索引:"
    echo "    cat $LOCAL_OUT/snapshot_index.csv"
    echo ""
    echo "  快速统计:"
    echo "    awk -F',' '\$6==$PID && \$19>0 {rss+=\$19; n++} END{printf \"VMA数=%d RSS=%d KB (%.1f MB)\\n\", n, rss, rss/1024}' $LOCAL_OUT/vma_memory_snapshot.csv"
fi
