#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
COLLECTOR="${SCRIPT_DIR}/page_idle_collect"
DRAWER="${SCRIPT_DIR}/draw_page_idle.py"
OP_SCRIPT="${SCRIPT_DIR}/user_operation.sh"
OUT_PATH="page_idle_segments.png"
SUMMARY_PATH=""
TSV_PATH=""
BITMAP_PATH=""
TITLE="page_idle 操作期间访问页"
TARGET_ARGS=()
COLLECT_ARGS=()

usage() {
    cat <<EOF
用法:
  $0 <pid> [-o page_idle_segments.png] [-s user_operation.sh] [--vma start-end] [--segment heap]
  $0 --app firefox [-o page_idle_segments.png] [-s user_operation.sh] [--vma start-end] [--segment heap]

说明:
  v7 先调用 C 程序读取 pagemap 得到 PFN，把 PFN 标记为 idle，执行用户操作脚本，
  再读取 page_idle bitmap，输出逐页 TSV 和类似 v3 bitmap 的文本文件。
  最后 Python 根据 bitmap 文本画出类似 v3/pfn_delta_segments.png 的图。

示例:
  $0 12345 -o page_idle_segments.png
  $0 12345 --segment heap -o heap_idle.png
  $0 --app firefox --vma 7f0000000000-7f0000100000 -o firefox_idle.png

输出:
  默认会生成 <输出名>.png、<输出名>.md、<输出名>.tsv、<输出名>_bitmap.txt
EOF
}

path_stem() {
    local path="$1"
    local dir base stem
    dir="$(dirname -- "$path")"
    base="$(basename -- "$path")"
    stem="${base%.*}"
    if [[ "$dir" == "." ]]; then
        printf '%s' "$stem"
    else
        printf '%s/%s' "$dir" "$stem"
    fi
}

while (($# > 0)); do
    case "$1" in
        -h|--help)
            usage
            exit 0
            ;;
        -o|--output)
            if (($# < 2)); then
                echo "-o/--output 后面需要 PNG 路径" >&2
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
            TARGET_ARGS=(--app "$2")
            shift 2
            ;;
        --vma|--segment|--idle-bitmap)
            if (($# < 2)); then
                echo "$1 后面需要参数" >&2
                exit 1
            fi
            COLLECT_ARGS+=("$1" "$2")
            shift 2
            ;;
        --title)
            if (($# < 2)); then
                echo "--title 后面需要参数" >&2
                exit 1
            fi
            TITLE="$2"
            shift 2
            ;;
        --summary)
            if (($# < 2)); then
                echo "--summary 后面需要 Markdown 路径" >&2
                exit 1
            fi
            SUMMARY_PATH="$2"
            shift 2
            ;;
        --tsv)
            if (($# < 2)); then
                echo "--tsv 后面需要 TSV 路径" >&2
                exit 1
            fi
            TSV_PATH="$2"
            shift 2
            ;;
        --bitmap)
            if (($# < 2)); then
                echo "--bitmap 后面需要 bitmap 文本路径" >&2
                exit 1
            fi
            BITMAP_PATH="$2"
            shift 2
            ;;
        -*)
            echo "未知参数: $1" >&2
            usage >&2
            exit 1
            ;;
        *)
            if ((${#TARGET_ARGS[@]} > 0)); then
                echo "只能指定一个 PID 或 --app" >&2
                exit 1
            fi
            if ! [[ "$1" =~ ^[0-9]+$ ]]; then
                echo "PID 必须是数字: $1" >&2
                exit 1
            fi
            TARGET_ARGS=("$1")
            shift
            ;;
    esac
done

if ((${#TARGET_ARGS[@]} == 0)); then
    echo "请指定 PID 或 --app" >&2
    usage >&2
    exit 1
fi

if [[ ! -x "$COLLECTOR" ]]; then
    echo "找不到可执行 C 采集器: $COLLECTOR" >&2
    echo "请先运行: gcc -Wall -Wextra -std=c11 -O2 -o page_idle_collect page_idle_collect.c" >&2
    exit 1
fi

if [[ ! -f "$DRAWER" ]]; then
    echo "找不到绘图脚本: $DRAWER" >&2
    exit 1
fi

stem="$(path_stem "$OUT_PATH")"
TSV_PATH="${TSV_PATH:-${stem}.tsv}"
BITMAP_PATH="${BITMAP_PATH:-${stem}_bitmap.txt}"
SUMMARY_PATH="${SUMMARY_PATH:-${stem}.md}"

"$COLLECTOR" "${TARGET_ARGS[@]}" -s "$OP_SCRIPT" -o "$TSV_PATH" --bitmap "$BITMAP_PATH" "${COLLECT_ARGS[@]}"
python3 "$DRAWER" "$BITMAP_PATH" -o "$OUT_PATH" --summary "$SUMMARY_PATH" --title "$TITLE"

echo "完成:"
echo "  PNG: $OUT_PATH"
echo "  Markdown: $SUMMARY_PATH"
echo "  TSV: $TSV_PATH"
echo "  Bitmap: $BITMAP_PATH"
