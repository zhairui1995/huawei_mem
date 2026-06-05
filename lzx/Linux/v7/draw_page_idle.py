#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 page_idle_collect.c 输出的 bitmap/TSV 绘制 segment 聚合图。"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


SEGMENT_ORDER = ["text", "data", "bss", "heap", "stack", "file", "anon", "special", "unknown"]
SEGMENT_LABELS = {
    "text": "text/代码段",
    "data": "data/已初始化数据段",
    "bss": "bss/未初始化数据段",
    "heap": "heap/堆",
    "stack": "stack/栈",
    "file": "file/文件映射",
    "anon": "anon/匿名映射",
    "special": "special/特殊映射",
    "unknown": "unknown/未知",
}

STATE_COLORS = {
    "referenced": "#c62828",
    "idle": "#eeeeee",
    "not_present": "#bdbdbd",
    "pfn_hidden": "#8c6bb1",
    "error": "#fdae61",
}
STATE_LABELS = {
    "referenced": "操作期间访问",
    "idle": "仍 idle",
    "not_present": "未驻留",
    "pfn_hidden": "PFN 不可见",
    "error": "读取失败",
}
STATE_PRIORITY = {
    "referenced": 5,
    "error": 4,
    "pfn_hidden": 3,
    "not_present": 2,
    "idle": 1,
}

CODE_TO_STATE = {
    "R": "referenced",
    "I": "idle",
    "N": "not_present",
    "H": "pfn_hidden",
    "E": "error",
}


@dataclass
class Page:
    addr: int
    segment: str
    vma_label: str
    state: str
    pfn: int
    path: str


@dataclass
class Stats:
    total_pages: int = 0
    tracked_pages: int = 0
    referenced: int = 0
    idle: int = 0
    not_present: int = 0
    pfn_hidden: int = 0
    error: int = 0


def setup_chinese_font() -> None:
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["font.sans-serif"] = [
        "Noto Sans CJK SC",
        "Noto Sans CJK JP",
        "Source Han Sans SC",
        "Microsoft YaHei",
        "SimHei",
        "WenQuanYi Zen Hei",
        "DejaVu Sans",
    ]


def read_pages(path: Path) -> List[Page]:
    pages: List[Page] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines()):
        if line_no == 0 or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 6:
            continue
        addr, segment, vma, state, pfn, page_path = parts[:6]
        try:
            pages.append(Page(int(addr, 16), segment, vma, state, int(pfn, 16), page_path))
        except ValueError:
            continue
    return pages


def read_bitmap_pages(path: Path) -> Tuple[List[Page], int]:
    pages: List[Page] = []
    page_size = 4096
    current_segment = ""
    synthetic_addr = 0

    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# page_idle_bitmap_v1"):
            continue
        if line.startswith("page_size\t"):
            try:
                page_size = int(line.split("\t", 1)[1])
            except ValueError:
                page_size = 4096
            continue
        if line.startswith("## segment\t"):
            parts = line.split("\t")
            current_segment = parts[1] if len(parts) > 1 else "unknown"
            continue
        if line.startswith("#") or line.startswith("pid\t") or line.startswith("legend\t"):
            continue
        if not current_segment:
            continue
        for code in line:
            state = CODE_TO_STATE.get(code)
            if state is None:
                continue
            pages.append(Page(synthetic_addr, current_segment, "", state, 1 if state in {"referenced", "idle"} else 0, ""))
            synthetic_addr += page_size
    return pages, page_size


def read_input(path: Path) -> Tuple[List[Page], int]:
    with path.open("r", encoding="utf-8", errors="ignore") as fp:
        first_line = fp.readline()
    if first_line.startswith("# page_idle_bitmap_v1"):
        return read_bitmap_pages(path)
    return read_pages(path), 4096


def summarize_pages(pages: Sequence[Page]) -> Dict[str, Stats]:
    stats: Dict[str, Stats] = {}
    for page in pages:
        s = stats.setdefault(page.segment, Stats())
        s.total_pages += 1
        if page.pfn > 0:
            s.tracked_pages += 1
        if page.state == "referenced":
            s.referenced += 1
        elif page.state == "idle":
            s.idle += 1
        elif page.state == "not_present":
            s.not_present += 1
        elif page.state == "pfn_hidden":
            s.pfn_hidden += 1
        else:
            s.error += 1
    return stats


def write_summary(path: Path, pages: Sequence[Page], page_size: int) -> None:
    stats = summarize_pages(pages)
    lines = [
        "# page_idle 访问页定位摘要",
        "",
        "| 项目 | 值 |",
        "| --- | --- |",
        f"| 页大小 | `{page_size} bytes` |",
        f"| 总页数 | `{len(pages)}` |",
        "",
        "## Segment 汇总",
        "",
        "| 一级段 | 总页数 | 可跟踪 PFN 页 | 操作期间访问 | 仍 idle | 未驻留 | PFN 不可见 | 错误 | 访问占比 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for seg in sorted(stats, key=lambda s: SEGMENT_ORDER.index(s) if s in SEGMENT_ORDER else len(SEGMENT_ORDER)):
        s = stats[seg]
        pct = 100.0 * s.referenced / s.tracked_pages if s.tracked_pages else 0.0
        lines.append(
            f"| {SEGMENT_LABELS.get(seg, seg)} | {s.total_pages} | {s.tracked_pages} | "
            f"{s.referenced} | {s.idle} | {s.not_present} | {s.pfn_hidden} | {s.error} | {pct:.2f}% |"
        )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def downsample_states(states: List[str], max_cells: int = 180) -> List[str]:
    if len(states) <= max_cells:
        return states
    sampled = []
    for i in range(max_cells):
        left = math.floor(i * len(states) / max_cells)
        right = math.floor((i + 1) * len(states) / max_cells)
        bucket = states[left : max(right, left + 1)]
        sampled.append(max(bucket, key=lambda state: STATE_PRIORITY.get(state, 0)))
    return sampled


def draw_segments(pages: Sequence[Page], out_path: Path, title: str, page_size: int) -> None:
    setup_chinese_font()
    by_segment: Dict[str, List[str]] = {}
    stats = summarize_pages(pages)
    for page in pages:
        by_segment.setdefault(page.segment, []).append(page.state)

    visible = [
        seg
        for seg in sorted(by_segment, key=lambda s: SEGMENT_ORDER.index(s) if s in SEGMENT_ORDER else len(SEGMENT_ORDER))
        if stats[seg].total_pages
    ]
    if not visible:
        raise RuntimeError("没有可绘制的页数据")

    row_h = 0.9
    fig_h = 1.7 + row_h * len(visible)
    fig, ax = plt.subplots(figsize=(13, fig_h))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, fig_h)
    ax.axis("off")

    ax.text(6.5, fig_h - 0.35, title, ha="center", va="center", fontsize=15, fontweight="bold")
    ax.text(6.5, fig_h - 0.72, f"每格代表虚拟页位置抽样；页大小 {page_size} bytes", ha="center", va="center", fontsize=9)

    legend_x = 0.5
    legend_y = fig_h - 1.08
    for i, key in enumerate(["referenced", "idle", "not_present", "pfn_hidden", "error"]):
        x = legend_x + i * 2.0
        ax.add_patch(Rectangle((x, legend_y), 0.16, 0.16, facecolor=STATE_COLORS[key], edgecolor="#777777", linewidth=0.4))
        ax.text(x + 0.22, legend_y + 0.08, STATE_LABELS[key], fontsize=8, va="center")

    y = fig_h - 1.65
    for seg in visible:
        s = stats[seg]
        pct = 100.0 * s.referenced / s.tracked_pages if s.tracked_pages else 0.0
        ax.text(0.25, y + 0.32, SEGMENT_LABELS.get(seg, seg), ha="left", va="center", fontsize=9.3, fontweight="bold")
        ax.text(2.05, y + 0.28, f"{s.total_pages} 页 / 跟踪 {s.tracked_pages} 页", ha="left", va="center", fontsize=8.5)
        ax.text(3.9, y + 0.28, f"访问 {s.referenced} 页 ({pct:.1f}%)", ha="left", va="center", fontsize=8.5, color="#c62828" if s.referenced else "#555555")

        bar_x = 5.35
        bar_w = 1.75
        cursor = bar_x
        denominator = max(s.total_pages, 1)
        for key in ["referenced", "idle", "not_present", "pfn_hidden", "error"]:
            value = getattr(s, key)
            width = bar_w * value / denominator
            if width > 0:
                ax.add_patch(Rectangle((cursor, y + 0.14), width, 0.28, facecolor=STATE_COLORS[key], edgecolor="none"))
                cursor += width
        ax.add_patch(Rectangle((bar_x, y + 0.14), bar_w, 0.28, facecolor="none", edgecolor="#666666", linewidth=0.5))

        heat_x = 7.35
        heat_w = 5.25
        cells = downsample_states(by_segment[seg])
        cell_gap = 0.006
        cell_w = (heat_w - max(len(cells) - 1, 0) * cell_gap) / max(len(cells), 1)
        for i, state in enumerate(cells):
            ax.add_patch(Rectangle((heat_x + i * (cell_w + cell_gap), y + 0.08), cell_w, 0.4, facecolor=STATE_COLORS.get(state, "#fdae61"), edgecolor="none"))
        ax.add_patch(Rectangle((heat_x, y + 0.08), heat_w, 0.4, facecolor="none", edgecolor="#777777", linewidth=0.45))
        y -= row_h

    fig.savefig(out_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="根据 C 采集器输出的 page_idle bitmap/TSV 绘图")
    parser.add_argument("input", type=Path, help="page_idle_collect 生成的 bitmap 文本；也兼容 TSV")
    parser.add_argument("-o", "--output", type=Path, default=Path("page_idle_segments.png"), help="输出 PNG")
    parser.add_argument("--summary", type=Path, help="输出 Markdown 摘要，默认与 PNG 同名 .md")
    parser.add_argument("--page-size", type=int, default=4096, help="页大小")
    parser.add_argument("--title", default="page_idle 操作期间访问页", help="图片标题")
    args = parser.parse_args()

    pages, detected_page_size = read_input(args.input)
    page_size = args.page_size if args.page_size != 4096 else detected_page_size
    args.output.parent.mkdir(parents=True, exist_ok=True)
    draw_segments(pages, args.output, args.title, page_size)
    write_summary(args.summary or args.output.with_suffix(".md"), pages, page_size)
    print(f"wrote {args.output}")
    print(f"wrote {args.summary or args.output.with_suffix('.md')}")


if __name__ == "__main__":
    main()
