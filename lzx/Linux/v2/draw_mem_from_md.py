#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
draw_mem_from_md.py

从 mem_analyze-v2 生成的 watch markdown 报告中自动解析每个 PID 的 sample 表格，
选择变化最大的 2~3 个进程，并画出“开始 sample 0 -> 结束 sample N”的虚拟地址空间示意图。

用法：
    python3 draw_mem_from_md.py firefox_watch_bilibili.md --top 3 -o memory_demo.png

依赖：
    pip install matplotlib
"""

import argparse
import hashlib
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch


# =========================
# 1. 数据结构
# =========================

@dataclass
class Sample:
    sample: int
    size: int
    rss: int
    pss: int
    present: int
    not_present: int
    swap: int
    virtual_pages: int
    present_pages: int
    swap_pages: int


@dataclass
class ProcessSeries:
    pid: int
    name: str
    cmdline: str
    samples: List[Sample]


# =========================
# 2. Markdown 解析
# =========================

PID_HEADER_RE = re.compile(r"^#{1,3} PID\s+(\d+)\s+`([^`]*)`", re.MULTILINE)
CMDLINE_RE = re.compile(r"^- 命令行：`(.*?)`", re.MULTILINE)
PROCESS_LINK_RE = re.compile(r"\]\((processes/[^)]+(?:\.md|/index\.md))\)")


def parse_int(s: str) -> int:
    return int(s.strip().replace(",", ""))


def parse_sample_table(section: str) -> List[Sample]:
    """
    解析形如：
    | sample | Size | RSS | PSS | Present | NotPresent | Swap | 虚拟页 | Present页 | Swap页 |
    | 0 | 5893508 | ...
    """
    samples: List[Sample] = []

    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue

        # 跳过表头和分隔行
        if "sample" in line or "---" in line:
            continue

        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 10:
            continue

        # 第一列必须是数字 sample index
        if not re.fullmatch(r"\d+", parts[0]):
            continue

        try:
            samples.append(
                Sample(
                    sample=parse_int(parts[0]),
                    size=parse_int(parts[1]),
                    rss=parse_int(parts[2]),
                    pss=parse_int(parts[3]),
                    present=parse_int(parts[4]),
                    not_present=parse_int(parts[5]),
                    swap=parse_int(parts[6]),
                    virtual_pages=parse_int(parts[7]),
                    present_pages=parse_int(parts[8]),
                    swap_pages=parse_int(parts[9]),
                )
            )
        except ValueError:
            continue

    # 有些报告中同一 PID 只有一个 sample 表格；正常情况返回 31 行
    samples.sort(key=lambda x: x.sample)
    return samples


def parse_process_sections(text: str) -> List[ProcessSeries]:
    matches = list(PID_HEADER_RE.finditer(text))
    processes: List[ProcessSeries] = []

    for i, m in enumerate(matches):
        pid = int(m.group(1))
        name = m.group(2)

        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[start:end]

        cmd_m = CMDLINE_RE.search(section)
        cmdline = cmd_m.group(1) if cmd_m else ""

        samples = parse_sample_table(section)
        if len(samples) >= 2:
            processes.append(ProcessSeries(pid=pid, name=name, cmdline=cmdline, samples=samples))

    return processes


def parse_watch_md(md_path: Path) -> List[ProcessSeries]:
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    processes = parse_process_sections(text)

    if not processes:
        for link in PROCESS_LINK_RE.findall(text):
            child_path = md_path.parent / link
            if child_path.exists():
                child_text = child_path.read_text(encoding="utf-8", errors="ignore")
                processes.extend(parse_process_sections(child_text))

    return processes


# =========================
# 3. 选择变化最大的进程
# =========================

def change_score(p: ProcessSeries) -> int:
    """
    默认按 Present 首尾变化量排序。
    这里取绝对值，既能抓增长，也能抓下降。
    """
    s0 = p.samples[0]
    s1 = p.samples[-1]
    return abs(s1.present - s0.present)


def select_top_processes(processes: List[ProcessSeries], top_k: int) -> List[ProcessSeries]:
    return sorted(processes, key=change_score, reverse=True)[:top_k]


# =========================
# 4. 画图参数
# =========================

SEGMENTS = [
    # name, height_ratio, base_weight, color
    ("text/\n代码段",              1.00, 1.40, "#fde9e7"),
    ("data/\n已初始化数据段",      0.85, 0.95, "#fff2dc"),
    ("bss/\n未初始化数据段",       0.85, 0.85, "#fff9d9"),
    ("heap/堆",                  0.95, 0.95, "#eaf7dc"),
    ("file mappings/\n文件映射",  1.30, 0.40, "#e5f1ff"),
    ("anon mmap/\n匿名映射",      1.70, 0.70, "#f0e6ff"),
    ("stack/栈",                 0.75, 0.70, "#e2f8ff"),
    ("special/\n特殊映射",        0.60, 0.60, "#eeeeee"),
]

# 不同进程行的标题背景
ROW_HEADER_COLORS = ["#e7f2ff", "#eef8eb", "#fff4d8", "#f0ecff", "#f2f2f2"]


def setup_chinese_font() -> None:
    """
    尽量选择系统中的中文字体。若没有中文字体，matplotlib 仍可运行，
    但中文可能显示为方块，需要安装 Noto Sans CJK / SimHei / Microsoft YaHei 等字体。
    """
    plt.rcParams["axes.unicode_minus"] = False
    candidates = [
        "Noto Sans CJK SC",
        "Noto Sans CJK JP",
        "Source Han Sans SC",
        "Microsoft YaHei",
        "SimHei",
        "WenQuanYi Zen Hei",
        "Arial Unicode MS",
        "DejaVu Sans",
    ]
    plt.rcParams["font.sans-serif"] = candidates


def stable_random_01(key: str) -> float:
    """
    生成稳定的 0~1 伪随机数。用于让每次运行画出的页格子布局一致。
    """
    h = hashlib.md5(key.encode("utf-8")).hexdigest()
    return int(h[:8], 16) / 0xFFFFFFFF


def fmt_kib(v: int) -> str:
    return f"{v:,} KiB"


# =========================
# 5. 页格子绘制
# =========================

def draw_page_grid(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    density: float,
    size_ratio: float,
    key_prefix: str,
    compare_density: float | None = None,
    compare_size_ratio: float | None = None,
    highlight_delta: bool = False,
    force_delta_marker: bool = False,
    cols: int = 14,
) -> None:
    """
    density: 已分配格子中 red/present 页的示意比例。
    size_ratio: 相对同一进程最大 Size 的比例，用于决定画出多少格子。
    注意：这是根据总量生成的示意图，不代表真实逐页布局。
    """
    gap = 0.018
    rows = max(2, int(h / 0.12))
    total_cells = rows * cols
    active_cells = max(1, min(total_cells, int(round(total_cells * max(0.0, min(1.0, size_ratio))))))

    cell_w = (w - (cols + 1) * gap) / cols
    cell_h = min(0.080, (h - (rows + 1) * gap) / rows)

    # 防止极端密度让图失真
    density = max(0.01, min(0.92, density))
    if compare_density is not None:
        compare_density = max(0.01, min(0.92, compare_density))

    cell_order = []
    for r in range(rows):
        for c in range(cols):
            rnd = stable_random_01(f"{key_prefix}-order-{r}-{c}")
            cell_order.append((rnd, r, c))
    cell_order.sort()
    active_cells_list = [(r, c) for _, r, c in cell_order[:active_cells]]
    active = set(active_cells_list)

    present_cells = int(round(active_cells * density))
    if density > 0.0 and active_cells > 0 and present_cells == 0:
        present_cells = 1
    present_cells = max(0, min(active_cells, present_cells))
    present_order = sorted(
        active_cells_list,
        key=lambda rc: stable_random_01(f"{key_prefix}-present-{rc[0]}-{rc[1]}"),
    )
    present = set(present_order[:present_cells])

    compare_present = set()
    if compare_density is not None and compare_size_ratio is not None:
        compare_active_cells = max(
            1,
            min(total_cells, int(round(total_cells * max(0.0, min(1.0, compare_size_ratio))))),
        )
        compare_active_cells_list = [(r, c) for _, r, c in cell_order[:compare_active_cells]]
        compare_present_cells = int(round(compare_active_cells * compare_density))
        if compare_density > 0.0 and compare_active_cells > 0 and compare_present_cells == 0:
            compare_present_cells = 1
        compare_present_cells = max(0, min(compare_active_cells, compare_present_cells))
        compare_present_order = sorted(
            compare_active_cells_list,
            key=lambda rc: stable_random_01(f"{key_prefix}-present-{rc[0]}-{rc[1]}"),
        )
        compare_present = set(compare_present_order[:compare_present_cells])

    delta_present = present - compare_present
    if highlight_delta and force_delta_marker and not delta_present and present:
        delta_present = {next(iter(present))}

    for r in range(rows):
        for c in range(cols):
            px = x + gap + c * (cell_w + gap)
            py = y + gap + r * (cell_h + gap)

            if (r, c) not in active:
                face = "#f3f3f3"
                edge = "#dedede"
            else:
                if highlight_delta and (r, c) in delta_present:
                    face = "#ff9f1c"
                elif highlight_delta and (r, c) not in present and (r, c) in compare_present:
                    face = "#d9ecff"
                else:
                    face = "#ff2b2b" if (r, c) in present else "#ffffff"
                edge = "#b8b8b8"

            ax.add_patch(
                Rectangle(
                    (px, py),
                    cell_w,
                    cell_h,
                    facecolor=face,
                    edgecolor=edge,
                    linewidth=0.45,
                )
            )


def segment_density(global_density: float, seg_weight: float) -> float:
    """
    把全局 Present/Size 比例映射到每个分段的示意密度。
    text 相对更容易显得红一些，file/anon 相对更稀疏。
    """
    # 使用近似线性映射，避免 sqrt 把开始/结束差异压平。
    d = max(global_density, 0.0) * 1.35 * seg_weight
    return max(0.02, min(0.88, d))


# =========================
# 6. 单个内存块绘制
# =========================

def draw_stats_box(ax, x: float, y: float, w: float, h: float, sample: Sample) -> None:
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.06,rounding_size=0.06",
            facecolor="white",
            edgecolor="#1f5fbf",
            linewidth=0.9,
        )
    )

    rows = [
        ("Size", sample.size, "black"),
        ("Present", sample.present, "#ff0000"),
        ("NotPresent", sample.not_present, "black"),
        ("RSS", sample.rss, "black"),
        ("PSS", sample.pss, "black"),
        ("Swap", sample.swap, "#0050ff"),
    ]

    ty = y + h - 0.17
    for k, v, color in rows:
        ax.text(x + 0.08, ty, f"{k}", fontsize=7.0, fontweight="bold", ha="left", va="center")
        value_text = fmt_kib(v) if k != "Swap" else str(v)
        ax.text(
            x + 0.72,
            ty,
            value_text,
            fontsize=7.0,
            color=color,
            fontweight="bold" if k in ("Present", "Swap") else "normal",
            ha="left",
            va="center",
        )
        ty -= 0.16


def draw_present_bar(ax, x: float, y: float, w: float, sample: Sample, max_present: int) -> None:
    ratio = sample.present / max(max_present, 1)
    ratio = max(0.0, min(1.0, ratio))

    ax.add_patch(
        Rectangle(
            (x, y),
            w,
            0.11,
            facecolor="#ffffff",
            edgecolor="#777777",
            linewidth=0.55,
        )
    )
    ax.add_patch(
        Rectangle(
            (x, y),
            w * ratio,
            0.11,
            facecolor="#ff2b2b",
            edgecolor="none",
        )
    )
    ax.text(
        x,
        y - 0.08,
        f"Present 绝对量: {fmt_kib(sample.present)}",
        fontsize=6.7,
        ha="left",
        va="top",
        color="#aa0000",
        fontweight="bold",
    )


def draw_memory_panel(
    ax,
    x0: float,
    y0: float,
    width: float,
    height: float,
    sample: Sample,
    title: str,
    pid: int,
    phase: str,
    max_size: int,
    compare_sample: Sample | None = None,
    force_delta_marker: bool = False,
) -> None:
    """
    画一个 sample 的虚拟地址空间块。
    """
    actual_height = height

    label_w = width * 0.35
    grid_w = width - label_w
    size_ratio = sample.size / max(max_size, 1)

    ax.text(
        x0 + width / 2,
        y0 + actual_height + 0.15,
        title,
        ha="center",
        va="bottom",
        fontsize=9.5,
        fontweight="bold",
    )

    # 外框
    ax.add_patch(
        Rectangle(
            (x0, y0),
            width,
            actual_height,
            facecolor="none",
            edgecolor="#333333",
            linewidth=1.0,
        )
    )

    # 连续虚拟地址空间 bracket
    bx = x0 - 0.28
    ax.plot([bx, bx], [y0, y0 + actual_height], color="black", linewidth=0.9)
    ax.plot([bx - 0.06, bx + 0.06], [y0, y0], color="black", linewidth=0.9)
    ax.plot([bx - 0.06, bx + 0.06], [y0 + actual_height, y0 + actual_height], color="black", linewidth=0.9)
    ax.text(
        x0 - 0.45,
        y0 + actual_height / 2,
        "连续\n虚拟\n地址\n空间",
        ha="center",
        va="center",
        fontsize=7.5,
        fontweight="bold",
    )

    global_density = sample.present / max(sample.size, 1)
    compare_global_density = None
    compare_size_ratio = None
    if compare_sample is not None:
        compare_global_density = compare_sample.present / max(compare_sample.size, 1)
        compare_size_ratio = compare_sample.size / max(max_size, 1)
    total_seg_h = sum(seg[1] for seg in SEGMENTS)
    cur_y = y0 + actual_height

    for si, (seg_name, seg_h_ratio, seg_weight, seg_color) in enumerate(SEGMENTS):
        seg_h = actual_height * seg_h_ratio / total_seg_h
        cur_y -= seg_h

        ax.add_patch(
            Rectangle(
                (x0, cur_y),
                width,
                seg_h,
                facecolor=seg_color,
                edgecolor="#888888",
                linewidth=0.55,
            )
        )

        ax.add_patch(
            Rectangle(
                (x0, cur_y),
                label_w,
                seg_h,
                facecolor=seg_color,
                edgecolor="#888888",
                linewidth=0.55,
            )
        )

        ax.text(
            x0 + label_w / 2,
            cur_y + seg_h / 2,
            seg_name,
            ha="center",
            va="center",
            fontsize=5.9,
            fontweight="bold",
        )

        d = segment_density(global_density, seg_weight)
        compare_d = segment_density(compare_global_density, seg_weight) if compare_global_density is not None else None
        draw_page_grid(
            ax,
            x0 + label_w + 0.035,
            cur_y + 0.025,
            grid_w - 0.07,
            seg_h - 0.05,
            d,
            size_ratio,
            key_prefix=f"{pid}-{si}",
            compare_density=compare_d,
            compare_size_ratio=compare_size_ratio,
            highlight_delta=compare_sample is not None,
            force_delta_marker=force_delta_marker and si == 0,
            cols=13,
        )


# =========================
# 7. 整图绘制
# =========================

def draw_infographic(
    processes: List[ProcessSeries],
    out_path: Path,
    title: str = "Firefox + Bilibili 内存监控示意图（变化较大的进程）",
) -> None:
    setup_chinese_font()

    n = len(processes)
    if n == 0:
        raise RuntimeError("没有可绘制的进程。")

    # 横向固定；纵向随进程数量伸缩
    fig_w = 12
    row_h = 4.5
    top_h = 1.0
    bottom_h = 0.35
    fig_h = top_h + bottom_h + row_h * n

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, fig_h)
    ax.axis("off")

    # 标题
    ax.text(
        6,
        fig_h - 0.35,
        title if n != 3 else "Firefox + Bilibili 内存监控示意图（变化较大的 3 个进程）",
        ha="center",
        va="center",
        fontsize=17,
        fontweight="bold",
    )
    ax.text(
        6,
        fig_h - 0.78,
        "格子容量按同进程最大 Size 归一化；结束图中橙色表示相对开始新增的 present",
        ha="center",
        va="center",
        fontsize=9.5,
    )

    # 图例
    lx, ly = 10.25, fig_h - 1.05
    ax.add_patch(
        FancyBboxPatch(
            (lx, ly - 0.55),
            1.55,
            1.12,
            boxstyle="round,pad=0.06,rounding_size=0.06",
            facecolor="white",
            edgecolor="#777777",
            linewidth=0.8,
        )
    )
    ax.add_patch(Rectangle((lx + 0.12, ly + 0.15), 0.16, 0.16, facecolor="#ff2b2b", edgecolor="#999999"))
    ax.text(lx + 0.35, ly + 0.23, "红色 = present", fontsize=7.5, va="center")
    ax.add_patch(Rectangle((lx + 0.12, ly - 0.12), 0.16, 0.16, facecolor="#ffffff", edgecolor="#999999"))
    ax.text(lx + 0.35, ly - 0.04, "白色 = not present", fontsize=7.5, va="center")
    ax.add_patch(Rectangle((lx + 0.12, ly - 0.39), 0.16, 0.16, facecolor="#f3f3f3", edgecolor="#dedede"))
    ax.text(lx + 0.35, ly - 0.31, "灰色 = 未分配容量", fontsize=7.2, va="center")
    ax.add_patch(Rectangle((lx + 0.12, ly - 0.64), 0.16, 0.16, facecolor="#ff9f1c", edgecolor="#999999"))
    ax.text(lx + 0.35, ly - 0.56, "橙色 = 新增 present", fontsize=7.0, va="center", color="#b86100", fontweight="bold")

    # 每行布局
    left_panel_x = 1.90
    right_panel_x = 7.45
    panel_w = 2.05
    panel_h = 3.25
    stats_w = 1.72
    stats_h = 1.05

    for idx, p in enumerate(processes):
        s0 = p.samples[0]
        s1 = p.samples[-1]
        max_present = max(s0.present, s1.present, 1)

        row_top = fig_h - top_h - idx * row_h
        row_bottom = row_top - row_h + 0.2

        # 行 header
        header_y = row_top - 0.25
        header_color = ROW_HEADER_COLORS[idx % len(ROW_HEADER_COLORS)]
        ax.add_patch(
            FancyBboxPatch(
                (0.18, header_y - 0.24),
                9.65,
                0.42,
                boxstyle="round,pad=0.03,rounding_size=0.05",
                facecolor=header_color,
                edgecolor="#b8c8d8",
                linewidth=0.7,
            )
        )
        ax.add_patch(
            FancyBboxPatch(
                (0.33, header_y - 0.17),
                0.23,
                0.27,
                boxstyle="round,pad=0.02,rounding_size=0.03",
                facecolor="#2f6dcc",
                edgecolor="#1c4d93",
                linewidth=0.7,
            )
        )
        ax.text(0.445, header_y - 0.035, str(idx + 1), color="white", ha="center", va="center", fontsize=9, fontweight="bold")

        change_note = "变化最大" if idx == 0 else ""
        ax.text(
            0.75,
            header_y - 0.03,
            f"PID {p.pid}  {p.name}  {change_note}",
            fontsize=10.5,
            fontweight="bold",
            ha="left",
            va="center",
        )

        panel_y = row_bottom + 0.5

        max_size = max(s0.size, s1.size, 1)

        draw_memory_panel(ax, left_panel_x, panel_y, panel_w, panel_h, s0, "开始（sample 0）", p.pid, "start", max_size)
        draw_memory_panel(
            ax,
            right_panel_x,
            panel_y,
            panel_w,
            panel_h,
            s1,
            f"结束（sample {s1.sample}）",
            p.pid,
            "end",
            max_size,
            compare_sample=s0,
            force_delta_marker=s1.present > s0.present,
        )
        draw_present_bar(ax, left_panel_x, panel_y - 0.28, panel_w, s0, max_present)
        draw_present_bar(ax, right_panel_x, panel_y - 0.28, panel_w, s1, max_present)

        # stats boxes
        draw_stats_box(ax, 0.15, panel_y + 0.05, stats_w, stats_h, s0)
        draw_stats_box(ax, 9.75, panel_y + 0.05, stats_w, stats_h, s1)

        # 中间箭头
        arrow_y = panel_y + panel_h * 0.58
        arrow = FancyArrowPatch(
            (5.25, arrow_y),
            (6.55, arrow_y),
            arrowstyle="simple",
            mutation_scale=28,
            linewidth=0.8,
            facecolor="#2f6dcc",
            edgecolor="#1f4f99",
        )
        ax.add_patch(arrow)

        # 变化量
        d_present = s1.present - s0.present
        d_pss = s1.pss - s0.pss
        d_size = s1.size - s0.size

        def signed(v: int) -> str:
            return f"{v:+,} KiB"

        cx = 5.90
        cy = panel_y + panel_h * 0.40
        ax.text(cx, cy + 0.55, "Present", fontsize=8.5, fontweight="bold", ha="center")
        ax.text(cx, cy + 0.32, signed(d_present), fontsize=8.5, color="#ff0000", fontweight="bold", ha="center")
        ax.plot([cx - 0.45, cx + 0.45], [cy + 0.17, cy + 0.17], color="#888888", linewidth=0.6)

        ax.text(cx, cy - 0.05, "PSS", fontsize=8.5, fontweight="bold", ha="center")
        ax.text(cx, cy - 0.28, signed(d_pss), fontsize=8.5, color="#ff0000", fontweight="bold", ha="center")
        ax.plot([cx - 0.45, cx + 0.45], [cy - 0.43, cy - 0.43], color="#888888", linewidth=0.6)

        ax.text(cx, cy - 0.65, "Size", fontsize=8.5, fontweight="bold", ha="center")
        ax.text(cx, cy - 0.88, signed(d_size), fontsize=8.5, color="#0050ff", fontweight="bold", ha="center")

    ax.text(
        6,
        0.18,
        "说明：该图是基于监控总量的示意图，用于帮助理解 virtual memory、present 与 not present 的变化。",
        ha="center",
        va="center",
        fontsize=8.5,
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight")

    # 同时保存 pdf，便于论文/汇报插图
    if out_path.suffix.lower() != ".pdf":
        pdf_path = out_path.with_suffix(".pdf")
        fig.savefig(pdf_path, bbox_inches="tight")

    plt.close(fig)


# =========================
# 8. 命令行入口
# =========================

def main() -> None:
    parser = argparse.ArgumentParser(description="从 mem_analyze-v2 watch markdown 生成虚拟地址空间 present/not-present 示意图")
    parser.add_argument("md", type=str, help="输入 markdown 报告路径，例如 firefox_watch_bilibili.md")
    parser.add_argument("-o", "--output", type=str, default="memory_demo.png", help="输出图片路径，默认 memory_demo.png")
    parser.add_argument("--top", type=int, default=3, help="选择 Present 首尾变化最大的前 K 个进程，默认 3")
    parser.add_argument("--title", type=str, default="Firefox + Bilibili 内存监控示意图（变化较大的进程）", help="图片标题")
    args = parser.parse_args()

    md_path = Path(args.md)
    out_path = Path(args.output)

    processes = parse_watch_md(md_path)
    if not processes:
        raise SystemExit(f"没有从 {md_path} 中解析到有效 PID sample 表格。")

    selected = select_top_processes(processes, max(1, args.top))

    print("选中的进程：")
    for p in selected:
        s0, s1 = p.samples[0], p.samples[-1]
        print(
            f"  PID {p.pid:<6} {p.name:<20} "
            f"Present {s0.present:,} -> {s1.present:,} "
            f"delta={s1.present - s0.present:+,} KiB"
        )

    draw_infographic(selected, out_path, title=args.title)
    print(f"图片已保存：{out_path}")
    if out_path.suffix.lower() != ".pdf":
        print(f"PDF 已保存：{out_path.with_suffix('.pdf')}")


if __name__ == "__main__":
    main()
