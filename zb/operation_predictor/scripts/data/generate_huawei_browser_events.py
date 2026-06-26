#!/usr/bin/env python3
"""Generate synthetic Huawei Browser operation events by user group."""

from __future__ import annotations

import argparse
import csv
import json
import random
from datetime import datetime, timedelta
from pathlib import Path


SCENE_TYPES = [
    "daily",
    "deep_work",
    "collaboration",
    "search",
    "settings",
    "interrupt",
    "linked",
]


BASE_PATTERNS = {
    "daily": [
        "打开华为浏览器",
        "查看新闻推荐",
        "打开网页",
        "新建标签页",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "收藏网页",
        "切换标签页",
        "查看历史记录",
        "关闭标签页",
        "关闭浏览器",
    ],
    "deep_work": [
        "打开华为浏览器",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "页面内查找",
        "开启阅读模式",
        "复制链接",
        "新建标签页",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "下载文件",
        "查看下载列表",
        "收藏网页",
        "关闭浏览器",
    ],
    "collaboration": [
        "打开华为浏览器",
        "输入网址",
        "打开网页",
        "复制链接",
        "分享网页",
        "新建标签页",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "分享网页",
        "关闭标签页",
        "关闭浏览器",
    ],
    "search": [
        "打开华为浏览器",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "返回上一页",
        "点击搜索结果",
        "打开网页",
        "页面内查找",
        "新建标签页",
        "输入搜索词",
        "点击搜索结果",
        "关闭浏览器",
    ],
    "settings": [
        "打开华为浏览器",
        "打开设置",
        "设置默认搜索引擎",
        "查看书签",
        "查看历史记录",
        "清除浏览记录",
        "打开无痕模式",
        "输入搜索词",
        "点击搜索结果",
        "关闭无痕模式",
        "关闭浏览器",
    ],
    "interrupt": [
        "打开华为浏览器",
        "输入搜索词",
        "点击搜索结果",
        "打开网页",
        "新建标签页",
        "切换标签页",
        "返回上一页",
        "刷新网页",
        "前进下一页",
        "关闭标签页",
        "查看历史记录",
        "关闭浏览器",
    ],
    "linked": [
        "打开华为浏览器",
        "扫描二维码",
        "打开网页",
        "复制链接",
        "分享网页",
        "新建标签页",
        "输入网址",
        "打开网页",
        "下载文件",
        "查看下载列表",
        "关闭浏览器",
    ],
}


ROLE_FOCUS = {
    "学生": ["输入搜索词", "点击搜索结果", "打开网页", "开启阅读模式", "收藏网页", "下载文件"],
    "程序员": ["输入搜索词", "页面内查找", "切换电脑版网页", "复制链接", "下载文件", "新建标签页"],
    "工程师": ["输入搜索词", "打开网页", "下载文件", "查看下载列表", "页面内查找", "收藏网页"],
    "网红": ["查看新闻推荐", "打开网页", "复制链接", "分享网页", "扫描二维码", "收藏网页"],
    "办公人群": ["输入网址", "打开网页", "复制链接", "分享网页", "下载文件", "查看书签"],
    "游戏用户": ["输入搜索词", "查看新闻推荐", "打开网页", "新建标签页", "切换标签页", "分享网页"],
    "影音娱乐用户": ["查看新闻推荐", "输入搜索词", "点击搜索结果", "打开网页", "分享网页", "收藏网页"],
    "金融用户": ["输入网址", "打开无痕模式", "打开网页", "刷新网页", "查看历史记录", "关闭无痕模式"],
    "通用用户": ["查看新闻推荐", "输入搜索词", "点击搜索结果", "打开网页", "查看历史记录", "关闭标签页"],
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def next_interval_seconds(operation: str, rng: random.Random) -> int:
    if operation in {"点击搜索结果", "切换标签页", "返回上一页", "前进下一页", "刷新网页", "关闭标签页"}:
        return rng.randint(2, 10)
    if operation in {"打开网页", "查看新闻推荐", "页面内查找", "查看书签", "查看历史记录", "查看下载列表"}:
        return rng.randint(10, 120)
    if operation in {"下载文件", "开启阅读模式", "打开设置", "设置默认搜索引擎", "清除浏览记录"}:
        return rng.randint(120, 600)
    return rng.randint(5, 90)


def scenario_start(base_date: datetime, scene_idx: int, rng: random.Random) -> datetime:
    day = scene_idx // 4
    slot = scene_idx % 4
    hour_choices = {
        0: [8, 9, 10],
        1: [13, 14, 15],
        2: [17, 18, 19],
        3: [20, 21],
    }
    hour = rng.choice(hour_choices[slot])
    minute = rng.randint(0, 45)
    second = rng.randint(0, 59)
    return base_date + timedelta(days=day, hours=hour, minutes=minute, seconds=second)


def expand_pattern(pattern: list[str], focus_ops: list[str], valid_ops: set[str], steps: int, rng: random.Random) -> list[str]:
    result: list[str] = []
    middle_ops = [op for op in pattern[1:-1] if op in valid_ops]
    focus_ops = [op for op in focus_ops if op in valid_ops]
    while len(result) < steps:
        if not result:
            result.append(pattern[0])
            continue
        if len(result) == steps - 1:
            result.append("关闭浏览器")
            continue
        if rng.random() < 0.68:
            result.append(rng.choice(middle_ops))
        else:
            result.append(rng.choice(focus_ops))
    return result


def generate_rows(args: argparse.Namespace) -> list[dict[str, str]]:
    user_groups = load_json(Path(args.user_group_vocab))
    op_vocab = load_json(Path(args.op_vocab))
    if args.app not in op_vocab:
        raise ValueError(f"app not found in op vocab: {args.app}")

    valid_ops = {op for op in op_vocab[args.app] if not op.startswith("<")}
    rng = random.Random(args.seed)
    rows: list[dict[str, str]] = []
    base_date = datetime.strptime(args.start_date, "%Y-%m-%d")

    for user_idx, user_group in enumerate(user_groups.keys(), start=1):
        user_id = f"u{user_idx:03d}"
        role_base = base_date + timedelta(days=user_idx - 1)
        scene_plan = [scene_type for scene_type in SCENE_TYPES for _ in range(args.scenes_per_type)]
        rng.shuffle(scene_plan)

        for scene_idx, scene_type in enumerate(scene_plan):
            timestamp = scenario_start(role_base, scene_idx, rng)
            steps = rng.randint(args.min_steps, args.max_steps)
            pattern = BASE_PATTERNS[scene_type]
            focus_ops = ROLE_FOCUS.get(user_group, ROLE_FOCUS["通用用户"])
            operations = expand_pattern(pattern, focus_ops, valid_ops, steps, rng)

            for operation in operations:
                rows.append(
                    {
                        "user_id": user_id,
                        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        "app": args.app,
                        "operation": operation,
                        "user_group": user_group,
                    }
                )
                timestamp += timedelta(seconds=next_interval_seconds(operation, rng))

    rows.sort(key=lambda row: (row["user_id"], row["timestamp"]))
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Huawei Browser operation events.")
    parser.add_argument("--user-group-vocab", default="data/vocab/user_group_vocab.json")
    parser.add_argument("--op-vocab", default="data/vocab/op_vocab.json")
    parser.add_argument("--app", default="华为浏览器")
    parser.add_argument("--output", default="data/raw/op_events_huawei_browser_generated.csv")
    parser.add_argument("--start-date", default="2026-06-08")
    parser.add_argument("--scenes-per-type", type=int, default=10)
    parser.add_argument("--min-steps", type=int, default=70)
    parser.add_argument("--max-steps", type=int, default=74)
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
