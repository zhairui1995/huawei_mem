#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare two mem_analyze-v2 snapshots and visualize per-segment physical page changes.

Examples:
    python3 draw_pfn_delta.py mem_analyze_run_x/processes/pid_1234_app.md -o pfn_delta.png
    python3 draw_pfn_delta.py --before first_snapshot.md --after last_snapshot.md -o pfn_delta.png
"""

from __future__ import annotations

import argparse
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


PAGE_SIZE_RE = re.compile(r"\| 页大小 \| `(\d+) bytes` \|")
SNAPSHOT_START_RE = re.compile(r"^### 开始快照", re.MULTILINE)
SNAPSHOT_END_RE = re.compile(r"^### 结束快照", re.MULTILINE)
PFN_SECTION_RE = re.compile(r"^## 逻辑区间 PFN 序列\s*$", re.MULTILINE)
NEXT_H2_RE = re.compile(r"^## ", re.MULTILINE)
REGION_HEADER_RE = re.compile(r"^### `([0-9a-fA-F]+)-([0-9a-fA-F]+)` ([^\n]+)$", re.MULTILINE)
CODE_AFTER_RE = r"- {label}：\s*```text\s*(.*?)\s*```"


SEGMENT_ORDER = [
    "text",
    "data",
    "bss",
    "heap",
    "stack",
    "file",
    "anon",
    "special",
    "unknown",
]

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
    "stable_present": "#c62828",
    "stable_absent": "#eeeeee",
    "added": "#fdae61",
    "removed": "#74add1",
    "pfn_changed": "#7b3294",
    "virtual_added": "#1b9e77",
    "virtual_removed": "#999999",
}

STATE_LABELS = {
    "stable_present": "驻留未变",
    "stable_absent": "未驻留未变",
    "added": "新增驻留",
    "removed": "释放/换出",
    "pfn_changed": "PFN 改变",
    "virtual_added": "新增虚拟页",
    "virtual_removed": "移除虚拟页",
}

STATE_PRIORITY = {
    "pfn_changed": 7,
    "added": 6,
    "removed": 5,
    "virtual_added": 4,
    "virtual_removed": 3,
    "stable_present": 2,
    "stable_absent": 1,
}


@dataclass(frozen=True)
class PageInfo:
    segment: str
    status: str
    pfn: int


@dataclass
class SegmentStats:
    before_pages: int = 0
    after_pages: int = 0
    stable_present: int = 0
    stable_absent: int = 0
    added: int = 0
    removed: int = 0
    pfn_changed: int = 0
    virtual_added: int = 0
    virtual_removed: int = 0

    @property
    def changed(self) -> int:
        return self.added + self.removed + self.pfn_changed + self.virtual_added + self.virtual_removed


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


def normalize_segment(raw: str) -> str:
    token = raw.strip().split("/", 1)[0].strip()
    if token == "data":
        return "data"
    if token in SEGMENT_ORDER:
        return token
    return "unknown"


def parse_page_size(texts: Iterable[str]) -> int:
    for text in texts:
        match = PAGE_SIZE_RE.search(text)
        if match:
            return int(match.group(1))
    return 4096


def split_snapshots(report_path: Path) -> Tuple[str, str]:
    if report_path.is_dir():
        before_path = report_path / "first_snapshot.md"
        after_path = report_path / "last_snapshot.md"
        if not before_path.exists() or not after_path.exists():
            raise ValueError(f"{report_path} 是目录，但没有找到 first_snapshot.md 和 last_snapshot.md")
        return (
            before_path.read_text(encoding="utf-8", errors="ignore"),
            after_path.read_text(encoding="utf-8", errors="ignore"),
        )

    text = report_path.read_text(encoding="utf-8", errors="ignore")
    start = SNAPSHOT_START_RE.search(text)
    end = SNAPSHOT_END_RE.search(text)
    if not start or not end or start.start() >= end.start():
        raise ValueError(f"{report_path} 中没有找到开始/结束快照；可改用 --before 和 --after")
    return text[start.end() : end.start()], text[end.end() :]


def section_after_pfn_heading(text: str) -> str:
    match = PFN_SECTION_RE.search(text)
    if not match:
        raise ValueError("快照中没有 `## 逻辑区间 PFN 序列`，请重新编译并运行新版 mem_analyze-v2")
    next_h2 = NEXT_H2_RE.search(text, match.end())
    return text[match.end() : next_h2.start() if next_h2 else len(text)]


def code_block(block: str, label: str) -> str:
    pattern = re.compile(CODE_AFTER_RE.format(label=re.escape(label)), re.S)
    match = pattern.search(block)
    return match.group(1).strip() if match else ""


def parse_snapshot(text: str, page_size: int) -> Dict[int, PageInfo]:
    section = section_after_pfn_heading(text)
    headers = list(REGION_HEADER_RE.finditer(section))
    pages: Dict[int, PageInfo] = {}

    for idx, header in enumerate(headers):
        start = int(header.group(1), 16)
        segment = normalize_segment(header.group(3))
        block_start = header.end()
        block_end = headers[idx + 1].start() if idx + 1 < len(headers) else len(section)
        block = section[block_start:block_end]

        bitmap = "".join(code_block(block, "pagemap_bitmap").split())
        pfn_text = code_block(block, "pfn_sequence")
        pfn_values: List[int] = []
        if pfn_text and pfn_text != "unavailable":
            for token in pfn_text.split():
                try:
                    pfn_values.append(int(token, 16))
                except ValueError:
                    pfn_values.append(0)

        count = max(len(bitmap), len(pfn_values))
        if len(bitmap) < count:
            bitmap = bitmap + "?" * (count - len(bitmap))
        if len(pfn_values) < count:
            pfn_values.extend([0] * (count - len(pfn_values)))

        for page_index in range(count):
            addr = start + page_index * page_size
            pages[addr] = PageInfo(segment=segment, status=bitmap[page_index], pfn=pfn_values[page_index])

    return pages


def classify(before: PageInfo | None, after: PageInfo | None) -> Tuple[str, str]:
    if before is None and after is not None:
        return after.segment, "virtual_added"
    if before is not None and after is None:
        return before.segment, "virtual_removed"
    assert before is not None and after is not None
    segment = after.segment if after.segment != "unknown" else before.segment
    before_present = before.status == "P" and before.pfn != 0
    after_present = after.status == "P" and after.pfn != 0
    if before_present and after_present and before.pfn != after.pfn:
        return segment, "pfn_changed"
    if not before_present and after_present:
        return segment, "added"
    if before_present and not after_present:
        return segment, "removed"
    if after_present:
        return segment, "stable_present"
    return segment, "stable_absent"


def compare_pages(before: Dict[int, PageInfo], after: Dict[int, PageInfo]) -> Tuple[Dict[str, SegmentStats], Dict[str, List[str]]]:
    stats = {seg: SegmentStats() for seg in SEGMENT_ORDER}
    states_by_segment = {seg: [] for seg in SEGMENT_ORDER}

    for info in before.values():
        stats[info.segment].before_pages += 1
    for info in after.values():
        stats[info.segment].after_pages += 1

    for addr in sorted(set(before) | set(after)):
        segment, state = classify(before.get(addr), after.get(addr))
        if segment not in stats:
            segment = "unknown"
        setattr(stats[segment], state, getattr(stats[segment], state) + 1)
        states_by_segment[segment].append(state)

    return stats, states_by_segment


def downsample_states(states: List[str], max_cells: int = 180) -> List[str]:
    if len(states) <= max_cells:
        return states
    sampled = []
    for i in range(max_cells):
        left = math.floor(i * len(states) / max_cells)
        right = math.floor((i + 1) * len(states) / max_cells)
        bucket = states[left : max(right, left + 1)]
        sampled.append(max(bucket, key=lambda s: STATE_PRIORITY[s]))
    return sampled


def write_summary(path: Path, stats: Dict[str, SegmentStats], page_size: int) -> None:
    lines = [
        "# 物理页变化摘要",
        "",
        "| 分段 | 操作前页数 | 操作后页数 | 新增驻留 | 释放/换出 | PFN 改变 | 新增虚拟页 | 移除虚拟页 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for seg in SEGMENT_ORDER:
        s = stats[seg]
        if s.before_pages == 0 and s.after_pages == 0:
            continue
        lines.append(
            f"| {SEGMENT_LABELS[seg]} | {s.before_pages} | {s.after_pages} | "
            f"{s.added} | {s.removed} | {s.pfn_changed} | {s.virtual_added} | {s.virtual_removed} |"
        )
    lines.extend(
        [
            "",
            f"> 页大小：{page_size} bytes。PFN 为 0 时无法判断真实物理页帧，通常需要 sudo/root 或 CAP_SYS_ADMIN。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def draw(stats: Dict[str, SegmentStats], states_by_segment: Dict[str, List[str]], out_path: Path, page_size: int, title: str) -> None:
    setup_chinese_font()
    visible = [seg for seg in SEGMENT_ORDER if stats[seg].before_pages or stats[seg].after_pages]
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

    legend_x = 0.4
    legend_y = fig_h - 1.08
    for i, key in enumerate(["stable_present", "stable_absent", "added", "removed", "pfn_changed", "virtual_added", "virtual_removed"]):
        x = legend_x + i * 1.75
        ax.add_patch(Rectangle((x, legend_y), 0.16, 0.16, facecolor=STATE_COLORS[key], edgecolor="#777777", linewidth=0.4))
        ax.text(x + 0.22, legend_y + 0.08, STATE_LABELS[key], fontsize=8, va="center")

    max_pages = max(max(stats[seg].before_pages, stats[seg].after_pages, 1) for seg in visible)
    y = fig_h - 1.65

    for seg in visible:
        s = stats[seg]
        ax.text(0.25, y + 0.28, SEGMENT_LABELS[seg], ha="left", va="center", fontsize=10, fontweight="bold")
        ax.text(2.05, y + 0.28, f"{s.before_pages} -> {s.after_pages} 页", ha="left", va="center", fontsize=8.5)
        ax.text(3.35, y + 0.28, f"变化 {s.changed} 页", ha="left", va="center", fontsize=8.5, color="#7b3294" if s.changed else "#555555")

        bar_x = 4.35
        bar_w = 2.5
        cursor = bar_x
        denominator = max(sum(getattr(s, key) for key in STATE_COLORS), 1)
        for key in ["stable_present", "stable_absent", "added", "removed", "pfn_changed", "virtual_added", "virtual_removed"]:
            value = getattr(s, key)
            width = bar_w * value / denominator
            if width > 0:
                ax.add_patch(Rectangle((cursor, y + 0.14), width, 0.28, facecolor=STATE_COLORS[key], edgecolor="none"))
                cursor += width
        ax.add_patch(Rectangle((bar_x, y + 0.14), bar_w, 0.28, facecolor="none", edgecolor="#666666", linewidth=0.5))

        heat_x = 7.1
        heat_w = 5.55
        cells = downsample_states(states_by_segment[seg])
        cell_gap = 0.006
        cell_w = (heat_w - max(len(cells) - 1, 0) * cell_gap) / max(len(cells), 1)
        for i, state in enumerate(cells):
            ax.add_patch(
                Rectangle(
                    (heat_x + i * (cell_w + cell_gap), y + 0.08),
                    cell_w,
                    0.4,
                    facecolor=STATE_COLORS[state],
                    edgecolor="none",
                )
            )
        ax.add_patch(Rectangle((heat_x, y + 0.08), heat_w, 0.4, facecolor="none", edgecolor="#777777", linewidth=0.45))
        y -= row_h

    fig.savefig(out_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="可视化 mem_analyze-v2 操作前后每个段的物理页变化")
    parser.add_argument("report", nargs="?", type=Path, help="包含开始/结束快照的 PID 监控详情 Markdown，或含 first_snapshot.md/last_snapshot.md 的目录")
    parser.add_argument("--before", type=Path, help="操作前快照 Markdown")
    parser.add_argument("--after", type=Path, help="操作后快照 Markdown")
    parser.add_argument("-o", "--output", type=Path, default=Path("pfn_delta.png"), help="输出 PNG 路径")
    parser.add_argument("--summary", type=Path, help="输出 Markdown 摘要路径，默认与 PNG 同名 .md")
    parser.add_argument("--title", default="操作前后物理页变化", help="图片标题")
    args = parser.parse_args()

    if args.before and args.after:
        before_text = args.before.read_text(encoding="utf-8", errors="ignore")
        after_text = args.after.read_text(encoding="utf-8", errors="ignore")
    elif args.report:
        before_text, after_text = split_snapshots(args.report)
    else:
        parser.error("需要传入 report，或同时传入 --before 和 --after")

    page_size = parse_page_size([before_text, after_text])
    before_pages = parse_snapshot(before_text, page_size)
    after_pages = parse_snapshot(after_text, page_size)
    stats, states_by_segment = compare_pages(before_pages, after_pages)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    draw(stats, states_by_segment, args.output, page_size, args.title)
    summary_path = args.summary or args.output.with_suffix(".md")
    write_summary(summary_path, stats, page_size)
    print(f"wrote {args.output}")
    print(f"wrote {summary_path}")


if __name__ == "__main__":
    main()
