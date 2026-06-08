import re
import sys
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch
from matplotlib import font_manager
import random

font_manager.fontManager.addfont("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK JP"]
plt.rcParams["axes.unicode_minus"] = False

# =========================
# 1. 从 mem_analyze-v2 生成的 watch markdown 中读取数据
# =========================

def parse_backtick_value(text, key):
    pattern = rf"\| {re.escape(key)} \| `([^`]+)` \|"
    match = re.search(pattern, text)
    return match.group(1) if match else ""


def parse_sample_row(line, headers):
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    if len(cells) != len(headers):
        return None
    row = {}
    for key, value in zip(headers, cells):
        try:
            row[key] = int(value)
        except ValueError:
            return None
    return row


def parse_processes_from_text(text):
    processes = []
    current = None
    headers = None
    in_sample_table = False

    for line in text.splitlines():
        pid_match = re.match(r"^#{1,3} PID (\d+) `([^`]+)`", line)
        if pid_match:
            current = {
                "pid": int(pid_match.group(1)),
                "comm": pid_match.group(2),
                "cmdline": "",
                "samples": [],
            }
            processes.append(current)
            headers = None
            in_sample_table = False
            continue

        if current is None:
            continue

        if line.startswith("- 命令行：`") and line.endswith("`"):
            current["cmdline"] = line[len("- 命令行：`"):-1]
            continue

        if line.startswith("| sample |"):
            headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
            in_sample_table = True
            continue

        if in_sample_table and line.startswith("| ---"):
            continue

        if in_sample_table:
            if not line.startswith("|"):
                in_sample_table = False
                continue
            row = parse_sample_row(line, headers)
            if row is not None:
                current["samples"].append(row)

    return [proc for proc in processes if proc["samples"]]


def parse_watch_report(path):
    text = path.read_text(encoding="utf-8")
    metadata = {
        "target": parse_backtick_value(text, "监控目标"),
        "duration": parse_backtick_value(text, "监控时长"),
        "interval": parse_backtick_value(text, "采样间隔"),
    }

    processes = parse_processes_from_text(text)
    if not processes:
        linked_reports = re.findall(r"\]\((processes/[^)]+\.md)\)", text)
        for link in linked_reports:
            linked_path = path.parent / link
            if linked_path.exists():
                processes.extend(parse_processes_from_text(linked_path.read_text(encoding="utf-8")))
    if not processes:
        raise ValueError(f"没有在 {path} 或它的 processes 子报告中找到 sample 表格")

    return metadata, processes


def choose_process(processes, requested_pid=None):
    if requested_pid is not None:
        for proc in processes:
            if proc["pid"] == requested_pid:
                return proc
        available = ", ".join(str(proc["pid"]) for proc in processes)
        raise ValueError(f"报告中没有 PID {requested_pid}，可用 PID: {available}")

    for proc in processes:
        if proc["comm"] == "firefox":
            return proc
    return max(processes, key=lambda proc: proc["samples"][-1].get("RSS", 0))


def make_stats(row, label):
    return {
        "title": f"{label}（sample {row['sample']}）",
        "Size": row["Size"],
        "Present": row["Present"],
        "NotPresent": row["NotPresent"],
        "RSS": row["RSS"],
        "PSS": row["PSS"],
        "Swap": row["Swap"],
    }


def trend_word(start_value, end_value):
    if end_value > start_value:
        return "增加"
    if end_value < start_value:
        return "减少"
    return "不变"


def clamp(value, low, high):
    return max(low, min(high, value))

# =========================
# 2. 虚拟地址空间的逻辑分区
#    height 只表示画图比例，不是实际 KiB
# =========================

segments = [
    {"name": "text/\n代码段",        "height": 1.0, "density_weight": 2.2, "color": "#fde9e7"},
    {"name": "data/\n已初始化数据段", "height": 0.9, "density_weight": 1.3, "color": "#fff2dc"},
    {"name": "bss/\n未初始化数据段",  "height": 0.9, "density_weight": 0.9, "color": "#fff9d9"},
    {"name": "heap/堆",             "height": 1.0, "density_weight": 1.1, "color": "#eaf7dc"},
    {"name": "file mappings/\n文件映射", "height": 1.6, "density_weight": 0.55, "color": "#e5f1ff"},
    {"name": "anon mmap/\n匿名映射",     "height": 2.1, "density_weight": 0.75, "color": "#f0e6ff"},
    {"name": "stack/栈",            "height": 0.8, "density_weight": 0.95, "color": "#e2f8ff"},
    {"name": "special/\n特殊映射",   "height": 0.7, "density_weight": 1.0, "color": "#eeeeee"},
]


def configure_segment_densities(start_stats, end_stats):
    for seg in segments:
        weight = seg["density_weight"]
        start_ratio = start_stats["Present"] / start_stats["Size"] if start_stats["Size"] else 0
        end_ratio = end_stats["Present"] / end_stats["Size"] if end_stats["Size"] else 0
        seg["start_density"] = clamp(start_ratio * weight, 0.03, 0.95)
        seg["end_density"] = clamp(end_ratio * weight, 0.03, 0.95)

# =========================
# 3. 画每个分段里的页格子
# =========================

def draw_page_grid(ax, x, y, w, h, density, seed):
    """
    x, y, w, h: 分段中页格子的区域
    density: red/present 页比例
    seed: 固定随机种子，保证每次画出来一样
    """
    random.seed(seed)

    cols = 14
    rows = max(2, int(h / 0.12))
    gap = 0.018

    cell_w = (w - (cols + 1) * gap) / cols
    cell_h = min(0.085, (h - (rows + 1) * gap) / rows)

    for r in range(rows):
        for c in range(cols):
            px = x + gap + c * (cell_w + gap)
            py = y + gap + r * (cell_h + gap)

            is_present = random.random() < density

            face = "#ff2b2b" if is_present else "#ffffff"
            edge = "#b8b8b8"

            ax.add_patch(
                Rectangle(
                    (px, py),
                    cell_w,
                    cell_h,
                    facecolor=face,
                    edgecolor=edge,
                    linewidth=0.5,
                )
            )

# =========================
# 4. 画一个完整虚拟地址空间面板
# =========================

def draw_memory_panel(ax, x0, y0, width, height, stats, side="left"):
    """
    画一个大块连续虚拟地址空间
    """
    label_w = width * 0.32
    grid_w = width - label_w

    # 标题
    ax.text(
        x0 + width / 2,
        y0 + height + 0.35,
        stats["title"],
        ha="center",
        va="bottom",
        fontsize=17,
        fontweight="bold",
    )

    # 外框
    ax.add_patch(
        Rectangle(
            (x0, y0),
            width,
            height,
            facecolor="none",
            edgecolor="black",
            linewidth=1.5,
        )
    )

    # 纵向标注：连续虚拟地址空间
    if side == "left":
        bx = x0 - 0.45
        text_x = x0 - 0.65
    else:
        bx = x0 - 0.35
        text_x = x0 - 0.55

    ax.plot([bx, bx], [y0, y0 + height], color="black", linewidth=1.4)
    ax.plot([bx - 0.12, bx + 0.12], [y0, y0], color="black", linewidth=1.4)
    ax.plot([bx - 0.12, bx + 0.12], [y0 + height, y0 + height], color="black", linewidth=1.4)

    ax.text(
        text_x,
        y0 + height / 2,
        "连续\n虚拟\n地址\n空间",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
    )

    total_h = sum(seg["height"] for seg in segments)
    cur_y = y0 + height

    for i, seg in enumerate(segments):
        seg_h = height * seg["height"] / total_h
        cur_y -= seg_h

        # 分段背景
        ax.add_patch(
            Rectangle(
                (x0, cur_y),
                width,
                seg_h,
                facecolor=seg["color"],
                edgecolor="#888888",
                linewidth=0.8,
            )
        )

        # 标签区域
        ax.add_patch(
            Rectangle(
                (x0, cur_y),
                label_w,
                seg_h,
                facecolor=seg["color"],
                edgecolor="#888888",
                linewidth=0.8,
            )
        )

        ax.text(
            x0 + label_w / 2,
            cur_y + seg_h / 2,
            seg["name"],
            ha="center",
            va="center",
            fontsize=10.5,
            fontweight="bold",
        )

        # 页格子区域
        density = seg["start_density"] if side == "left" else seg["end_density"]
        draw_page_grid(
            ax,
            x0 + label_w + 0.05,
            cur_y + 0.04,
            grid_w - 0.1,
            seg_h - 0.08,
            density,
            seed=1000 + i + (0 if side == "left" else 100),
        )

    # 统计框
    box_w = 2.3
    box_h = 1.15
    if side == "left":
        bx = x0 - 2.15
    else:
        bx = x0 + width + 0.25

    by = y0 + 0.05

    ax.add_patch(
        FancyBboxPatch(
            (bx, by),
            box_w,
            box_h,
            boxstyle="round,pad=0.08,rounding_size=0.08",
            facecolor="white",
            edgecolor="#1f5fbf",
            linewidth=1.2,
        )
    )

    lines = [
        ("Size", stats["Size"], "black"),
        ("Present", stats["Present"], "#ff0000"),
        ("NotPresent", stats["NotPresent"], "black"),
        ("RSS", stats["RSS"], "black"),
        ("PSS", stats["PSS"], "black"),
        ("Swap", stats["Swap"], "#0050ff"),
    ]

    ty = by + box_h - 0.18
    for name, value, color in lines:
        ax.text(bx + 0.12, ty, f"{name}:", ha="left", va="center", fontsize=8.8, fontweight="bold")
        ax.text(
            bx + 1.05,
            ty,
            f"{value:,} KiB" if name != "Swap" else f"{value}",
            ha="left",
            va="center",
            fontsize=8.8,
            color=color,
            fontweight="bold" if name in ["Present", "Swap"] else "normal",
        )
        ty -= 0.18

def draw_picture(report_path, png_path, pdf_path, requested_pid=None):
    metadata, processes = parse_watch_report(report_path)
    process = choose_process(processes, requested_pid=requested_pid)
    start_row = process["samples"][0]
    end_row = process["samples"][-1]
    start_stats = make_stats(start_row, "开始")
    end_stats = make_stats(end_row, "结束")
    configure_segment_densities(start_stats, end_stats)

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    left_x = 2.3
    right_x = 10.0
    panel_y = 0.85
    panel_w = 3.6
    panel_h = 7.2

    draw_memory_panel(ax, left_x, panel_y, panel_w, panel_h, start_stats, side="left")
    draw_memory_panel(ax, right_x, panel_y, panel_w, panel_h, end_stats, side="right")

    arrow = FancyArrowPatch(
        (6.6, 4.7),
        (9.2, 4.7),
        arrowstyle="simple",
        mutation_scale=35,
        linewidth=1.2,
        facecolor="#2f6dcc",
        edgecolor="#1f4f99",
    )
    ax.add_patch(arrow)

    duration = metadata["duration"] or "监控"
    target = metadata["target"] or process["comm"]
    ax.text(
        7.9,
        5.35,
        f"{duration} 变化\n{target} PID {process['pid']}",
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
    )

    note_x, note_y = 6.55, 1.25
    note_w, note_h = 2.7, 1.2
    ax.add_patch(
        FancyBboxPatch(
            (note_x, note_y),
            note_w,
            note_h,
            boxstyle="round,pad=0.08,rounding_size=0.08",
            facecolor="white",
            edgecolor="#1f5fbf",
            linestyle="--",
            linewidth=1.2,
        )
    )

    ax.text(note_x + 0.15, note_y + 0.85, "从 Markdown sample 表读取", fontsize=10.5, fontweight="bold")
    ax.text(note_x + 0.15, note_y + 0.57, "present", fontsize=10.5, fontweight="bold", color="#ff0000")
    ax.text(note_x + 0.85, note_y + 0.57, f"页{trend_word(start_stats['Present'], end_stats['Present'])}，", fontsize=10.5, fontweight="bold")
    ax.text(note_x + 0.15, note_y + 0.29, "not present", fontsize=10.5, fontweight="bold", color="#0050ff")
    ax.text(note_x + 1.25, note_y + 0.29, f"页{trend_word(start_stats['NotPresent'], end_stats['NotPresent'])}。", fontsize=10.5, fontweight="bold")

    legend_x = 14.1
    legend_y = 5.6

    ax.add_patch(Rectangle((legend_x, legend_y), 0.28, 0.28, facecolor="#ff2b2b", edgecolor="#b8b8b8"))
    ax.text(legend_x + 0.45, legend_y + 0.14, "红色 = present", va="center", fontsize=10.5)

    ax.add_patch(Rectangle((legend_x, legend_y - 0.55), 0.28, 0.28, facecolor="#ffffff", edgecolor="#b8b8b8"))
    ax.text(legend_x + 0.45, legend_y - 0.41, "白色 = not present", va="center", fontsize=10.5)

    ax.text(
        legend_x,
        legend_y - 1.05,
        f"swap = {start_stats['Swap']} -> {end_stats['Swap']}",
        fontsize=10.5,
        color="#0050ff",
        fontweight="bold",
    )

    plt.tight_layout()
    plt.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.savefig(pdf_path, bbox_inches="tight")
    print(f"读取报告: {report_path}")
    print(f"选择进程: PID {process['pid']} `{process['comm']}`")
    print(f"开始 sample: {start_row['sample']}，结束 sample: {end_row['sample']}")
    print(f"已生成: {png_path}")
    print(f"已生成: {pdf_path}")
    plt.show()


# =========================
# 5. 主画图逻辑
# =========================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="从 firefox_watch.md 的 sample 表格生成内存变化示意图")
    parser.add_argument("report", nargs="?", default="firefox_watch.md", help="输入 markdown 报告路径")
    parser.add_argument("output", nargs="?", default="virtual_memory_demo", help="输出文件名前缀")
    parser.add_argument("--pid", type=int, help="指定要绘制的 PID；不指定时优先选择进程名为 firefox 的 PID")
    args = parser.parse_args()

    output_stem = Path(args.output)
    draw_picture(
        Path(args.report),
        output_stem.with_suffix(".png"),
        output_stem.with_suffix(".pdf"),
        requested_pid=args.pid,
    )
