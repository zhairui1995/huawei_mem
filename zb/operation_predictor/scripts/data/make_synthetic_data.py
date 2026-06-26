#!/usr/bin/env python3
"""Generate reproducible synthetic app and in-app operation logs."""

from __future__ import annotations

import argparse
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.utils.io_utils import load_json, save_csv, save_json


DEFAULT_GROUP_VOCAB = {
    "学生": 0,
    "程序员": 1,
    "工程师": 2,
    "网红": 3,
    "办公人群": 4,
    "游戏用户": 5,
    "影音娱乐用户": 6,
    "金融用户": 7,
    "通用用户": 8,
}

GROUP_PREFERENCES = {
    "学生": ["知乎", "哔哩哔哩", "米哈游", "明日方舟", "夸克浏览器", "腾讯QQ", "飞书"],
    "程序员": ["华为浏览器", "火狐浏览器", "夸克浏览器", "飞书", "WPS", "百度网盘", "知乎"],
    "工程师": ["WPS", "飞书", "华为浏览器", "百度网盘", "智慧生活", "图库", "像素蛋糕"],
    "网红": ["抖音", "剪映", "图库", "像素蛋糕", "哔哩哔哩", "斗鱼", "虎牙直播"],
    "办公人群": ["WPS", "飞书", "腾讯QQ", "华为浏览器", "百度网盘"],
    "游戏用户": ["米哈游", "逆水寒", "明日方舟", "燕云十六声", "青云诀"],
    "影音娱乐用户": ["抖音", "哔哩哔哩", "腾讯视频", "爱奇艺", "优酷视频", "斗鱼", "虎牙直播"],
    "金融用户": ["同花顺", "华为钱包", "腾讯QQ", "华为浏览器"],
}

GROUP_OPERATION_KEYWORDS = {
    "学生": {
        "搜索": 4,
        "查看": 3,
        "浏览": 3,
        "播放": 3,
        "收藏": 2,
        "评论": 2,
        "加入": 2,
        "领取": 2,
    },
    "程序员": {
        "搜索": 5,
        "查看": 4,
        "文档": 4,
        "上传": 3,
        "下载": 3,
        "同步": 3,
        "设置": 2,
        "分享": 2,
    },
    "工程师": {
        "查看": 4,
        "编辑": 4,
        "保存": 4,
        "导出": 3,
        "同步": 3,
        "设置": 3,
        "调整": 3,
        "连接": 2,
    },
    "网红": {
        "拍摄": 5,
        "剪辑": 5,
        "导入": 4,
        "添加": 4,
        "发布": 4,
        "分享": 4,
        "直播": 3,
        "评论": 3,
        "点赞": 3,
    },
    "办公人群": {
        "消息": 4,
        "会议": 4,
        "文档": 4,
        "任务": 3,
        "审批": 3,
        "保存": 3,
        "分享": 3,
        "打印": 2,
    },
    "游戏用户": {
        "游戏": 5,
        "任务": 4,
        "副本": 4,
        "战斗": 4,
        "抽卡": 3,
        "领取": 3,
        "角色": 3,
        "背包": 2,
    },
    "影音娱乐用户": {
        "播放": 5,
        "暂停": 4,
        "继续": 4,
        "搜索": 3,
        "收藏": 3,
        "评论": 3,
        "弹幕": 3,
        "直播": 3,
        "投屏": 2,
    },
    "金融用户": {
        "查看": 4,
        "搜索": 3,
        "行情": 5,
        "自选": 4,
        "交易": 5,
        "买入": 5,
        "卖出": 5,
        "账单": 4,
        "支付": 4,
        "转账": 4,
        "安全": 3,
    },
    "通用用户": {
        "打开": 2,
        "查看": 2,
        "浏览": 2,
        "搜索": 2,
        "返回": 2,
    },
}

GROUP_SESSION_LENGTH = {
    "学生": (4, 9),
    "程序员": (5, 11),
    "工程师": (5, 10),
    "网红": (6, 13),
    "办公人群": (5, 11),
    "游戏用户": (7, 14),
    "影音娱乐用户": (5, 12),
    "金融用户": (4, 9),
    "通用用户": (3, 9),
}

PHASE_KEYWORDS = {
    "start": {"打开": 4, "进入": 4, "浏览": 2, "查看": 2, "搜索": 2},
    "middle": {"查看": 2, "搜索": 2, "编辑": 2, "播放": 2, "发送": 2, "领取": 2},
    "end": {"保存": 4, "导出": 3, "分享": 3, "返回": 4, "退出": 4, "关闭": 4},
}

START_TERMS = ("打开", "进入", "浏览", "查看", "搜索", "启动")
END_TERMS = ("返回", "退出", "关闭")


def _weighted_apps(app_names: list[str], group: str) -> list[str]:
    preferred = [name for name in GROUP_PREFERENCES.get(group, []) if name in app_names]
    if group == "通用用户" or not preferred:
        return app_names
    weighted = list(preferred)
    for name in preferred:
        weighted.extend([name] * 5)
    return weighted


def _valid_ops(op_vocab: dict[str, dict[str, int]], app: str) -> list[str]:
    return [op for op in op_vocab.get(app, {}) if op not in {"<PAD>", "<UNK>"}]


def _weighted_choice(rng: random.Random, items: list[str], weights: list[int]) -> str:
    total = sum(weights)
    if total <= 0:
        return rng.choice(items)
    point = rng.uniform(0, total)
    cumulative = 0.0
    for item, weight in zip(items, weights):
        cumulative += weight
        if point <= cumulative:
            return item
    return items[-1]


def _phase_for_step(step: int, total_steps: int) -> str:
    if step < min(2, total_steps - 1):
        return "start"
    if step == total_steps - 1:
        return "end"
    return "middle"


def _operation_weight(operation: str, group: str, phase: str) -> int:
    weight = 1
    for keyword, boost in GROUP_OPERATION_KEYWORDS.get(group, {}).items():
        if keyword in operation:
            weight += boost
    for keyword, boost in PHASE_KEYWORDS[phase].items():
        if keyword in operation:
            weight += boost
    return weight


def _ops_for_phase(ops: list[str], phase: str) -> list[str]:
    if phase == "start":
        candidates = [
            op
            for op in ops
            if any(term in op for term in START_TERMS) and not any(term in op for term in END_TERMS)
        ]
    elif phase == "middle":
        candidates = [op for op in ops if not any(term in op for term in END_TERMS)]
    else:
        candidates = [op for op in ops if any(term in op for term in END_TERMS)]
    return candidates or ops


def _choose_operation(rng: random.Random, ops: list[str], group: str, phase: str) -> str:
    candidates = _ops_for_phase(ops, phase)
    weights = [_operation_weight(op, group, phase) for op in candidates]
    return _weighted_choice(rng, candidates, weights)


def _session_op_count(rng: random.Random, group: str) -> int:
    low, high = GROUP_SESSION_LENGTH.get(group, GROUP_SESSION_LENGTH["通用用户"])
    return rng.randint(low, high)


def _choose_foreground_app(rng: random.Random, candidates: list[str], opened: list[str]) -> str:
    if opened and rng.random() < 0.45:
        return rng.choice(opened)
    return rng.choice(candidates)


def _update_opened_apps(rng: random.Random, opened: list[str], foreground_app: str, max_opened: int) -> None:
    if foreground_app not in opened:
        if len(opened) >= max_opened:
            close_candidates = [app for app in opened if app != foreground_app]
            if close_candidates:
                opened.remove(rng.choice(close_candidates))
        opened.append(foreground_app)

    close_candidates = [app for app in opened if app != foreground_app]
    if close_candidates and rng.random() < 0.20:
        opened.remove(rng.choice(close_candidates))


def generate(args: argparse.Namespace) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    if args.max_opened_apps < 1:
        raise ValueError("--max-opened-apps must be >= 1")

    rng = random.Random(args.seed)
    app_vocab = load_json(args.app_vocab)
    op_vocab = load_json(args.op_vocab)
    if Path(args.group_vocab).exists():
        group_vocab = load_json(args.group_vocab)
    else:
        group_vocab = DEFAULT_GROUP_VOCAB
        save_json(group_vocab, args.group_vocab)
        print(f"created default user group vocab: {args.group_vocab}")

    app_names = list(app_vocab.keys())
    op_app_names = [app for app in app_names if app in op_vocab and _valid_ops(op_vocab, app)]
    if not app_names or not op_app_names:
        raise ValueError("app_vocab 或 op_vocab 为空，无法生成模拟数据")

    groups = list(group_vocab.keys())
    base_time = datetime(2026, 6, 8, 9, 0, 0)
    app_rows: list[dict[str, str]] = []
    op_rows: list[dict[str, str]] = []

    for user_index in range(1, args.num_users + 1):
        user_id = f"u{user_index:03d}"
        group = groups[(user_index - 1) % len(groups)]
        current = base_time + timedelta(minutes=user_index * 3)
        end_time = current + timedelta(hours=args.hours)
        opened: list[str] = []

        while current < end_time:
            candidates = _weighted_apps(op_app_names, group)
            foreground_app = _choose_foreground_app(rng, candidates, opened)
            _update_opened_apps(rng, opened, foreground_app, args.max_opened_apps)

            app_rows.append(
                {
                    "user_id": user_id,
                    "timestamp": current.strftime("%Y-%m-%d %H:%M:%S"),
                    "foreground_app": foreground_app,
                    "opened_apps": ";".join(opened),
                    "user_group": group,
                }
            )

            op_time = current
            ops = _valid_ops(op_vocab, foreground_app)
            op_count = _session_op_count(rng, group)
            for step in range(op_count):
                op_time += timedelta(seconds=rng.randint(5, 60))
                phase = _phase_for_step(step, op_count)
                operation = _choose_operation(rng, ops, group, phase)
                op_rows.append(
                    {
                        "user_id": user_id,
                        "timestamp": op_time.strftime("%Y-%m-%d %H:%M:%S"),
                        "app": foreground_app,
                        "operation": operation,
                        "user_group": group,
                    }
                )

            current = max(current + timedelta(minutes=rng.randint(1, 5)), op_time + timedelta(seconds=rng.randint(20, 90)))

    return app_rows, op_rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate synthetic Huawei user behavior logs.")
    parser.add_argument("--num-users", type=int, default=10)
    parser.add_argument("--hours", type=float, default=2.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--app-vocab", default="data/vocab/app_vocab.json")
    parser.add_argument("--op-vocab", default="data/vocab/op_vocab.json")
    parser.add_argument("--group-vocab", default="data/vocab/user_group_vocab.json")
    parser.add_argument("--output-app", default="data/raw/app_events.csv")
    parser.add_argument("--output-op", default="data/raw/op_events.csv")
    parser.add_argument("--max-opened-apps", type=int, default=6)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    app_rows, op_rows = generate(args)
    save_csv(app_rows, args.output_app, ["user_id", "timestamp", "foreground_app", "opened_apps", "user_group"])
    save_csv(op_rows, args.output_op, ["user_id", "timestamp", "app", "operation", "user_group"])
    print(f"generated app events: {len(app_rows)} -> {args.output_app}")
    print(f"generated op events: {len(op_rows)} -> {args.output_op}")


if __name__ == "__main__":
    main()
