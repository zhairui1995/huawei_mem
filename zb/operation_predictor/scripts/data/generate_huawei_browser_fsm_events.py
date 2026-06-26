#!/usr/bin/env python3
"""Generate FSM-constrained Huawei Browser operation events."""

from __future__ import annotations

import argparse
import csv
import json
import random
from datetime import datetime, timedelta
from pathlib import Path


APP = "华为浏览器"

SCENE_GROUPS = {
    "G1": [
        "打开华为浏览器",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "开启阅读模式",
        "返回上一页",
    ],
    "G2": [
        "打开华为浏览器",
        "输入网址",
        "打开网页",
        "开启阅读模式",
        "页面内查找",
        "收藏网页",
        "返回上一页",
    ],
    "G3": [
        "打开华为浏览器",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "页面内查找",
        "下载文件",
        "查看下载列表",
        "收藏网页",
    ],
    "G4": [
        "打开华为浏览器",
        "查看新闻推荐",
        "打开网页",
        "开启阅读模式",
        "刷新网页",
        "返回上一页",
    ],
    "G5": [
        "打开华为浏览器",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "页面内查找",
        "复制链接",
        "分享网页",
        "返回上一页",
    ],
    "G6": [
        "打开华为浏览器",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "新建标签页",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "切换标签页",
        "页面内查找",
        "收藏网页",
    ],
    "G7": [
        "打开华为浏览器",
        "查看历史记录",
        "打开网页",
        "收藏网页",
        "查看书签",
        "取消收藏网页",
        "返回上一页",
    ],
    "G8": [
        "打开华为浏览器",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "刷新网页",
        "返回上一页",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
    ],
}

ROLE_SUFFIXES = {
    "学生": ["页面内查找", "收藏网页"],
    "程序员": ["页面内查找", "切换电脑版网页"],
    "工程师": ["页面内查找", "下载文件", "查看下载列表"],
    "网红": ["复制链接", "分享网页"],
    "办公人群": ["复制链接", "分享网页"],
    "游戏用户": ["查看新闻推荐", "分享网页"],
    "影音娱乐用户": ["查看新闻推荐", "收藏网页"],
    "金融用户": ["打开无痕模式", "输入网址", "打开网页", "刷新网页", "关闭无痕模式"],
    "通用用户": ["查看历史记录", "收藏网页", "查看书签"],
}

LOW_FREQ_CHAINS = [
    ["打开华为浏览器", "打开设置", "设置默认搜索引擎", "关闭浏览器"],
    ["打开华为浏览器", "打开无痕模式", "输入搜索词", "点击搜索结果", "打开网页", "关闭无痕模式", "关闭浏览器"],
    ["打开华为浏览器", "查看历史记录", "清除浏览记录", "关闭浏览器"],
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def step_seconds(operation: str, rng: random.Random) -> int:
    if operation in {"点击搜索结果", "返回上一页", "前进下一页", "刷新网页", "切换标签页", "关闭标签页"}:
        return rng.randint(2, 8)
    if operation in {"输入搜索词", "输入网址", "扫描二维码"}:
        return rng.randint(5, 20)
    if operation in {"打开网页", "开启阅读模式", "页面内查找", "查看新闻推荐"}:
        return rng.randint(30, 300)
    if operation in {"下载文件", "查看下载列表", "收藏网页", "查看书签", "查看历史记录"}:
        return rng.randint(20, 180)
    return rng.randint(5, 60)


def scene_start(base_date: datetime, user_idx: int, scene_idx: int, rng: random.Random) -> datetime:
    day = (scene_idx // 4) + user_idx - 1
    slot = scene_idx % 4
    hours = {
        0: [8, 9, 10],
        1: [13, 14, 15],
        2: [18, 19],
        3: [20, 21, 22],
    }[slot]
    hour = rng.choice(hours)
    minute = rng.randint(0, 25 if hour == 22 else 55)
    return base_date + timedelta(days=day, hours=hour, minutes=minute, seconds=rng.randint(0, 59))


def can_append_suffix(current: list[str], suffix: list[str]) -> bool:
    has_page = "打开网页" in current
    has_download = "下载文件" in current
    has_favorite = "收藏网页" in current
    page_count = current.count("打开网页")
    tab_count = 1 + current.count("新建标签页") - current.count("关闭标签页")
    for op in suffix:
        if op in {"页面内查找", "开启阅读模式", "收藏网页", "下载文件", "复制链接", "分享网页", "刷新网页", "返回上一页", "前进下一页"} and not has_page:
            return False
        if op == "查看下载列表" and not has_download:
            return False
        if op in {"取消收藏网页", "查看书签"} and not has_favorite:
            return False
        if op in {"切换标签页", "关闭标签页"} and not (page_count >= 2 and tab_count >= 2):
            return False
    return True


def extend_scene(base_chain: list[str], user_group: str, target_steps: int, rng: random.Random) -> list[str]:
    ops = list(base_chain)
    trailing_return = False
    if ops and ops[-1] == "返回上一页":
        ops = ops[:-1]
        trailing_return = True
    suffix = ROLE_SUFFIXES.get(user_group, ROLE_SUFFIXES["通用用户"])
    controlled_cycles = [
        ["页面内查找", "开启阅读模式", "返回上一页", "输入搜索词", "点击搜索结果", "打开网页"],
        ["复制链接", "分享网页", "返回上一页", "输入搜索词", "点击搜索结果", "打开网页"],
        ["新建标签页", "输入搜索词", "点击搜索结果", "打开网页", "切换标签页"],
        ["收藏网页", "查看书签", "返回上一页", "输入搜索词", "点击搜索结果", "打开网页"],
        ["下载文件", "查看下载列表", "返回上一页", "输入搜索词", "点击搜索结果", "打开网页"],
    ]
    if can_append_suffix(ops, suffix):
        ops.extend(suffix)
    while len(ops) < target_steps - 1:
        candidates = [cycle for cycle in controlled_cycles if can_append_suffix(ops, cycle)]
        cycle = rng.choice(candidates)
        final_steps = 2 if trailing_return else 1
        if len(ops) + len(cycle) + final_steps > target_steps:
            break
        ops.extend(cycle)
    if trailing_return and len(ops) < target_steps - 1:
        ops.append("返回上一页")
    if ops[-1] != "关闭浏览器":
        ops.append("关闭浏览器")
    return ops[:target_steps]


def build_scene_plan(rng: random.Random, min_scenes_per_group: int, max_scenes_per_group: int) -> list[str]:
    plan: list[str] = []
    for group in SCENE_GROUPS:
        plan.extend([group] * rng.randint(min_scenes_per_group, max_scenes_per_group))
    rng.shuffle(plan)
    return plan


def generate_rows(args: argparse.Namespace) -> list[dict[str, str]]:
    user_groups = load_json(Path(args.user_group_vocab))
    op_vocab = load_json(Path(args.op_vocab))
    valid_ops = {op for op in op_vocab[APP] if not op.startswith("<")}
    rng = random.Random(args.seed)
    base_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    rows: list[dict[str, str]] = []

    for user_idx, user_group in enumerate(user_groups, start=1):
        user_id = f"u{user_idx:03d}"
        scene_plan = build_scene_plan(rng, args.min_scenes_per_group, args.max_scenes_per_group)
        current_time = base_date + timedelta(days=user_idx - 1, hours=8, minutes=rng.randint(0, 45))
        for scene_idx, scene_group in enumerate(scene_plan):
            if rng.random() < args.low_freq_scene_rate:
                operations = list(rng.choice(LOW_FREQ_CHAINS))
            else:
                target_steps = rng.randint(args.min_steps, args.max_steps)
                operations = extend_scene(SCENE_GROUPS[scene_group], user_group, target_steps, rng)
            timestamp = current_time
            intervals = [step_seconds(operation, rng) for operation in operations]
            scene_end = timestamp + timedelta(seconds=sum(intervals))
            day_end = timestamp.replace(hour=22, minute=30, second=0, microsecond=0)
            if scene_end > day_end:
                timestamp = (timestamp + timedelta(days=1)).replace(
                    hour=rng.choice([8, 9, 10]),
                    minute=rng.randint(0, 45),
                    second=rng.randint(0, 59),
                    microsecond=0,
                )
            for operation in operations:
                if operation not in valid_ops:
                    raise ValueError(f"operation not in vocab: {operation}")
                rows.append(
                    {
                        "user_id": user_id,
                        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        "app": APP,
                        "operation": operation,
                        "user_group": user_group,
                    }
                )
                timestamp += timedelta(seconds=intervals.pop(0))
            current_time = timestamp + timedelta(minutes=rng.randint(30, 180))
            day_end = current_time.replace(hour=22, minute=30, second=0, microsecond=0)
            day_start = current_time.replace(hour=8, minute=0, second=0, microsecond=0)
            if current_time.time() < day_start.time():
                current_time = current_time.replace(
                    hour=rng.choice([8, 9, 10]),
                    minute=rng.randint(0, 45),
                    second=rng.randint(0, 59),
                    microsecond=0,
                )
            elif current_time > day_end:
                current_time = (current_time + timedelta(days=1)).replace(
                    hour=rng.choice([8, 9, 10]),
                    minute=rng.randint(0, 45),
                    second=rng.randint(0, 59),
                    microsecond=0,
                )
    rows.sort(key=lambda row: (row["user_id"], row["timestamp"]))
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate FSM-constrained Huawei Browser events.")
    parser.add_argument("--user-group-vocab", default="data/vocab/user_group_vocab.json")
    parser.add_argument("--op-vocab", default="data/vocab/op_vocab.json")
    parser.add_argument("--output", default="data/raw/op_events_huawei_browser_fsm.csv")
    parser.add_argument("--start-date", default="2026-06-08")
    parser.add_argument("--min-scenes-per-group", type=int, default=6)
    parser.add_argument("--max-scenes-per-group", type=int, default=7)
    parser.add_argument("--min-steps", type=int, default=35)
    parser.add_argument("--max-steps", type=int, default=42)
    parser.add_argument("--low-freq-scene-rate", type=float, default=0.04)
    parser.add_argument("--seed", type=int, default=20260618)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = generate_rows(args)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["user_id", "timestamp", "app", "operation", "user_group"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"saved: {output}")
    print(f"rows: {len(rows)}")


if __name__ == "__main__":
    main()
