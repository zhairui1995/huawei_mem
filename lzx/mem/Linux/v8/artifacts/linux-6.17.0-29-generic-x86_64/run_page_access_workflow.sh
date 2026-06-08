#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
COLLECTOR="${SCRIPT_DIR}/page_access_collect"
DRAWER="${SCRIPT_DIR}/draw_page_access.py"
OP_SCRIPT="${SCRIPT_DIR}/user_operation.sh"
OUT_PATH="page_access_segments.png"
SUMMARY_PATH=""
TSV_PATH=""
BITMAP_PATH=""
TITLE="v8 young/accessed bit 操作期间访问页"
TARGET_ARGS=()
COLLECT_ARGS=()

usage() {
    cat <<EOF
用法:
  $0 <pid> [-o page_access_segments.png] [-s user_operation.sh] [--vma start-end] [--segment heap]
  $0 --app firefox [-o page_access_segments.png] [-s user_operation.sh] [--vma start-end] [--segment heap]

说明:
  v8 不使用 /sys/kernel/mm/page_idle/bitmap。
  它调用自定义内核模块 /dev/v8_page_access：
    clear 阶段清除目标虚拟页 PTE/PMD young(accessed) bit
    query 阶段检查这些 bit 是否又被硬件/内核置位
  输出格式与 v7 保持一致：TSV、bitmap 文本、Markdown、PNG。

示例:
  $0 12345 -o page_access_segments.png
  $0 12345 --segment heap -o heap_access.png
  $0 --app firefox --vma 7f0000000000-7f0000100000 -o firefox_access.png

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
        --vma|--segment|--device)
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

if ((${#TARGET_ARGS[@]} == 1)) && [[ "${TARGET_ARGS[0]}" =~ ^[0-9]+$ ]]; then
    PID="${TARGET_ARGS[0]}"
    if [[ ! -d "/proc/${PID}" ]]; then
        echo "目标进程不存在: /proc/${PID}" >&2
        echo "请确认 PID 是否还活着，或改用 --app 重新匹配目标进程" >&2
        exit 1
    fi
    if [[ ! -r "/proc/${PID}/maps" ]]; then
        echo "无法读取目标进程 maps: /proc/${PID}/maps" >&2
        echo "请确认这是用户态进程，并用 sudo 运行" >&2
        exit 1
    fi
fi

if [[ ! -x "$COLLECTOR" ]]; then
    echo "找不到可执行用户态采集器: $COLLECTOR" >&2
    echo "请先运行: make user" >&2
    exit 1
fi

if [[ ! -e /dev/v8_page_access ]]; then
    echo "找不到 /dev/v8_page_access，请先加载内核模块:" >&2
    echo "  sudo insmod ${SCRIPT_DIR}/v8_page_access.ko" >&2
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
