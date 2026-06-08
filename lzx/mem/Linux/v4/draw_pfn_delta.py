#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare two mem_analyze-v3 snapshots and visualize per-section physical page changes.

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
PRIMARY_SEGMENT_RE = re.compile(r"- 一级段：(.+)")
SECONDARY_SECTION_RE = re.compile(r"- 二级 section：`([^`]*)`")


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
    section: str
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
    if token in SEGMENT_ORDER:
        return token
    for seg in SEGMENT_ORDER:
        if raw.startswith(seg + "/"):
            return seg
    return token or "unknown"


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
        full_path = report_path / "full_report.md"
        if full_path.exists():
            raise ValueError(f"{report_path} 是单次分析目录，只有一个快照，不能直接绘制 delta；请传入包含 first_snapshot.md/last_snapshot.md 的监控目录，或使用 --before/--after")
        if not before_path.exists() or not after_path.exists():
            raise ValueError(f"{report_path} 是目录，但没有找到 first_snapshot.md/last_snapshot.md 或 full_report.md")
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


def read_snapshot_input(path: Path) -> str:
    if path.is_dir():
        page_data = path / "page_data.tsv"
        if page_data.exists():
            return page_data.read_text(encoding="utf-8", errors="ignore")
        full_path = path / "full_report.md"
        if full_path.exists():
            return full_path.read_text(encoding="utf-8", errors="ignore")
    return path.read_text(encoding="utf-8", errors="ignore")


def section_after_pfn_heading(text: str) -> str:
    match = PFN_SECTION_RE.search(text)
    if not match:
        raise ValueError("快照中没有 `## 逻辑区间 PFN 序列`，请重新编译并运行 mem_analyze-v3")
    next_h2 = NEXT_H2_RE.search(text, match.end())
    return text[match.end() : next_h2.start() if next_h2 else len(text)]


def code_block(block: str, label: str) -> str:
    pattern = re.compile(CODE_AFTER_RE.format(label=re.escape(label)), re.S)
    match = pattern.search(block)
    return match.group(1).strip() if match else ""


def parse_region_identity(header_label: str, block: str) -> Tuple[str, str]:
    primary = PRIMARY_SEGMENT_RE.search(block)
    secondary = SECONDARY_SECTION_RE.search(block)
    if primary and secondary:
        return normalize_segment(primary.group(1)), secondary.group(1)
    if " / " in header_label:
        left, right = header_label.split(" / ", 1)
        return normalize_segment(left), right.strip()
    segment = normalize_segment(header_label)
    return segment, segment


def parse_snapshot(text: str, page_size: int) -> Dict[int, PageInfo]:
    if text.startswith("addr\tsegment\tsection\tstatus\tcode\tpfn"):
        pages: Dict[int, PageInfo] = {}
        for line_no, line in enumerate(text.splitlines()):
            if line_no == 0 or not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 6:
                continue
            addr, segment, section, status, _code, pfn = parts[:6]
            try:
                pages[int(addr, 16)] = PageInfo(
                    segment=normalize_segment(segment),
                    section=section,
                    status=status,
                    pfn=int(pfn, 16),
                )
            except ValueError:
                continue
        return pages

    section = section_after_pfn_heading(text)
    headers = list(REGION_HEADER_RE.finditer(section))
    pages: Dict[int, PageInfo] = {}

    for idx, header in enumerate(headers):
        start = int(header.group(1), 16)
        block_start = header.end()
        block_end = headers[idx + 1].start() if idx + 1 < len(headers) else len(section)
        block = section[block_start:block_end]
        segment, section_name = parse_region_identity(header.group(3), block)

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
            pages[addr] = PageInfo(segment=segment, section=section_name, status=bitmap[page_index], pfn=pfn_values[page_index])

    return pages


def page_key(info: PageInfo) -> Tuple[str, str]:
    return info.segment, info.section


def classify(before: PageInfo | None, after: PageInfo | None) -> Tuple[Tuple[str, str], str]:
    if before is None and after is not None:
        return page_key(after), "virtual_added"
    if before is not None and after is None:
        return page_key(before), "virtual_removed"
    assert before is not None and after is not None
    key = page_key(after) if after.segment != "unknown" else page_key(before)
    before_present = before.status == "P" and before.pfn != 0
    after_present = after.status == "P" and after.pfn != 0
    if before_present and after_present and before.pfn != after.pfn:
        return key, "pfn_changed"
    if not before_present and after_present:
        return key, "added"
    if before_present and not after_present:
        return key, "removed"
    if after_present:
        return key, "stable_present"
    return key, "stable_absent"


def compare_pages(before: Dict[int, PageInfo], after: Dict[int, PageInfo]) -> Tuple[Dict[Tuple[str, str], SegmentStats], Dict[Tuple[str, str], List[str]]]:
    stats: Dict[Tuple[str, str], SegmentStats] = {}
    states_by_section: Dict[Tuple[str, str], List[str]] = {}

    for info in before.values():
        stats.setdefault(page_key(info), SegmentStats()).before_pages += 1
    for info in after.values():
        stats.setdefault(page_key(info), SegmentStats()).after_pages += 1

    for addr in sorted(set(before) | set(after)):
        key, state = classify(before.get(addr), after.get(addr))
        stats.setdefault(key, SegmentStats())
        states_by_section.setdefault(key, [])
        setattr(stats[key], state, getattr(stats[key], state) + 1)
        states_by_section[key].append(state)

    return stats, states_by_section


def merge_stats_by_segment(
    stats: Dict[Tuple[str, str], SegmentStats],
    states_by_section: Dict[Tuple[str, str], List[str]],
) -> Tuple[Dict[Tuple[str, str], SegmentStats], Dict[Tuple[str, str], List[str]]]:
    merged_stats: Dict[Tuple[str, str], SegmentStats] = {}
    merged_states: Dict[Tuple[str, str], List[str]] = {}

    for (segment, _section), s in stats.items():
        key = (segment, segment)
        target = merged_stats.setdefault(key, SegmentStats())
        target.before_pages += s.before_pages
        target.after_pages += s.after_pages
        target.stable_present += s.stable_present
        target.stable_absent += s.stable_absent
        target.added += s.added
        target.removed += s.removed
        target.pfn_changed += s.pfn_changed
        target.virtual_added += s.virtual_added
        target.virtual_removed += s.virtual_removed

    for (segment, _section), states in states_by_section.items():
        merged_states.setdefault((segment, segment), []).extend(states)

    return merged_stats, merged_states


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


def section_sort_key(item: Tuple[Tuple[str, str], SegmentStats]) -> Tuple[int, int, str]:
    (segment, section), s = item
    seg_order = SEGMENT_ORDER.index(segment) if segment in SEGMENT_ORDER else len(SEGMENT_ORDER)
    return seg_order, -s.changed, section


def write_summary(path: Path, stats: Dict[Tuple[str, str], SegmentStats], page_size: int, include_section: bool = True) -> None:
    lines = [
        "# 物理页变化摘要",
        "",
    ]
    if include_section:
        lines.extend([
            "| 一级段 | 二级 section | 操作前页数 | 操作后页数 | 新增驻留 | 释放/换出 | PFN 改变 | 新增虚拟页 | 移除虚拟页 |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ])
    else:
        lines.extend([
            "| 一级段 | 操作前页数 | 操作后页数 | 新增驻留 | 释放/换出 | PFN 改变 | 新增虚拟页 | 移除虚拟页 |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ])
    for (seg, section), s in sorted(stats.items(), key=section_sort_key):
        if s.before_pages == 0 and s.after_pages == 0:
            continue
        if include_section:
            lines.append(
                f"| {SEGMENT_LABELS.get(seg, seg)} | `{section}` | {s.before_pages} | {s.after_pages} | "
                f"{s.added} | {s.removed} | {s.pfn_changed} | {s.virtual_added} | {s.virtual_removed} |"
            )
        else:
            lines.append(
                f"| {SEGMENT_LABELS.get(seg, seg)} | {s.before_pages} | {s.after_pages} | "
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


def draw(stats: Dict[Tuple[str, str], SegmentStats], states_by_section: Dict[Tuple[str, str], List[str]], out_path: Path, page_size: int, title: str, top: int) -> None:
    setup_chinese_font()
    visible = [key for key, s in sorted(stats.items(), key=section_sort_key) if s.before_pages or s.after_pages]
    visible.sort(key=lambda key: (-stats[key].changed, SEGMENT_ORDER.index(key[0]) if key[0] in SEGMENT_ORDER else len(SEGMENT_ORDER), key[1]))
    visible = visible[:top]
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

    y = fig_h - 1.65

    for seg, section in visible:
        s = stats[(seg, section)]
        display_section = "" if section == seg else (section if len(section) <= 34 else section[:31] + "...")
        ax.text(0.25, y + 0.33, SEGMENT_LABELS.get(seg, seg), ha="left", va="center", fontsize=9.3, fontweight="bold")
        if display_section:
            ax.text(0.25, y + 0.08, display_section, ha="left", va="center", fontsize=7.2)
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
        cells = downsample_states(states_by_section.get((seg, section), []))
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
    parser = argparse.ArgumentParser(description="可视化 mem_analyze-v3 操作前后每个 segment/section 的物理页变化")
    parser.add_argument("report", nargs="?", type=Path, help="包含开始/结束快照的 PID 监控详情 Markdown，或含 first_snapshot.md/last_snapshot.md 的目录")
    parser.add_argument("--before", type=Path, help="操作前快照 Markdown")
    parser.add_argument("--after", type=Path, help="操作后快照 Markdown")
    parser.add_argument("-o", "--output", type=Path, default=Path("pfn_delta.png"), help="输出 PNG 路径")
    parser.add_argument("--summary", type=Path, help="输出 Markdown 摘要路径，默认与 PNG 同名 .md")
    parser.add_argument("--title", default="操作前后物理页变化", help="图片标题")
    parser.add_argument("--top", type=int, default=20, help="最多展示变化最大的 N 个二级 section")
    parser.add_argument("--segment-output", type=Path, help="一级 segment 聚合图输出路径，默认与 PNG 同名加 _segments")
    parser.add_argument("--segment-summary", type=Path, help="一级 segment 聚合摘要输出路径，默认与 segment 图同名 .md")
    args = parser.parse_args()

    if args.before and args.after:
        before_text = read_snapshot_input(args.before)
        after_text = read_snapshot_input(args.after)
    elif args.report:
        before_text, after_text = split_snapshots(args.report)
    else:
        parser.error("需要传入 report，或同时传入 --before 和 --after")

    page_size = parse_page_size([before_text, after_text])
    before_pages = parse_snapshot(before_text, page_size)
    after_pages = parse_snapshot(after_text, page_size)
    stats, states_by_section = compare_pages(before_pages, after_pages)
    segment_stats, states_by_segment = merge_stats_by_segment(stats, states_by_section)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    draw(stats, states_by_section, args.output, page_size, args.title, max(args.top, 1))
    summary_path = args.summary or args.output.with_suffix(".md")
    write_summary(summary_path, stats, page_size)

    segment_output = args.segment_output or args.output.with_name(f"{args.output.stem}_segments{args.output.suffix}")
    segment_output.parent.mkdir(parents=True, exist_ok=True)
    draw(segment_stats, states_by_segment, segment_output, page_size, f"{args.title}（一级 segment）", len(segment_stats))
    segment_summary = args.segment_summary or segment_output.with_suffix(".md")
    write_summary(segment_summary, segment_stats, page_size, include_section=False)
    print(f"wrote {args.output}")
    print(f"wrote {summary_path}")
    print(f"wrote {segment_output}")
    print(f"wrote {segment_summary}")


if __name__ == "__main__":
    main()
