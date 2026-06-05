#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ANALYZER="${SCRIPT_DIR}/mem_analyze-v6"
OP_SCRIPT="${SCRIPT_DIR}/user_operation.sh"
OUT_PATH="referenced.md"
PID=""
APP_KEYWORD=""
ANALYZER_ARGS=()

usage() {
    cat <<EOF
用法:
  $0 <pid> [-o referenced.md] [-s user_operation.sh] [--with-vma]
  $0 --app firefox [-o referenced.md] [-s user_operation.sh] [--with-vma]

流程:
  1. sudo mem_analyze-v6 --clear-refs <pid 或 --app>
  2. 执行用户操作脚本
  3. sudo mem_analyze-v6 <pid 或 --app> -o <报告路径>

示例:
  $0 12345
  $0 --app firefox
  $0 12345 -o firefox_referenced.md
  $0 12345 -o referenced.md --with-vma
  $0 12345 -s ./open_doc.sh -o doc_referenced.md
EOF
}

while (($# > 0)); do
    case "$1" in
        -h|--help)
            usage
            exit 0
            ;;
        -o|--output)
            if (($# < 2)); then
                echo "-o/--output 后面需要报告路径" >&2
                exit 1
            fi
            OUT_PATH="$2"
            shift 2
            ;;
        -s|--script)
            if (($# < 2)); then
                echo "-s/--script 后面需要用户操作脚本路径" >&2
                exit 1
            fi
            OP_SCRIPT="$2"
            shift 2
            ;;
        --app)
            if (($# < 2)); then
                echo "--app 后面需要 app 关键字" >&2
                exit 1
            fi
            APP_KEYWORD="$2"
            shift 2
            ;;
        --with-vma)
            ANALYZER_ARGS+=(--with-vma)
            shift
            ;;
        -*)
            echo "未知参数: $1" >&2
            usage >&2
            exit 1
            ;;
        *)
            if [[ -n "$PID" ]]; then
                echo "只能指定一个 PID；已收到 ${PID}，又收到 $1" >&2
                exit 1
            fi
            PID="$1"
            shift
            ;;
    esac
done

if [[ -z "$PID" && -z "$APP_KEYWORD" ]]; then
    echo "请指定目标 PID 或 --app 关键字" >&2
    usage >&2
    exit 1
fi

if [[ -n "$PID" && -n "$APP_KEYWORD" ]]; then
    echo "请不要混用 PID 和 --app" >&2
    exit 1
fi

if [[ -n "$PID" ]] && ! [[ "$PID" =~ ^[0-9]+$ ]]; then
    echo "PID 必须是数字: $PID" >&2
    exit 1
fi

if [[ -n "$PID" && ! -d "/proc/${PID}" ]]; then
    echo "目标进程不存在: /proc/${PID}" >&2
    exit 1
fi

if [[ ! -x "$ANALYZER" ]]; then
    echo "找不到可执行分析器: $ANALYZER" >&2
    echo "请先运行: gcc -Wall -Wextra -std=c11 -o ${ANALYZER} ${SCRIPT_DIR}/mem_analyze-v6.c" >&2
    exit 1
fi

if [[ ! -f "$OP_SCRIPT" ]]; then
    echo "找不到用户操作脚本: $OP_SCRIPT" >&2
    exit 1
fi

if [[ -n "$APP_KEYWORD" ]]; then
    TARGET_ARGS=(--app "$APP_KEYWORD")
    TARGET_LABEL="app ${APP_KEYWORD}"
else
    TARGET_ARGS=("$PID")
    TARGET_LABEL="PID ${PID}"
fi

echo "==> 清空 ${TARGET_LABEL} 的 referenced 标记"
sudo "$ANALYZER" --clear-refs "${TARGET_ARGS[@]}"

echo "==> 执行用户操作脚本: $OP_SCRIPT"
if [[ -x "$OP_SCRIPT" ]]; then
    "$OP_SCRIPT" "${PID:-}" "${APP_KEYWORD:-}"
else
    bash "$OP_SCRIPT" "${PID:-}" "${APP_KEYWORD:-}"
fi

echo "==> 立即读取 smaps 并生成报告: $OUT_PATH"
sudo "$ANALYZER" "${TARGET_ARGS[@]}" -o "$OUT_PATH" "${ANALYZER_ARGS[@]}"

echo "==> 完成"
