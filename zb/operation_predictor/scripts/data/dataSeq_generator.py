#!/usr/bin/env python3
"""Generate one user's Bilibili PC operation sequence with a probabilistic FSM.

Example:
  python scripts/data/dataSeq_generator.py \
    --user-id u001 \
    --user-group 学生 \
    --start-date 2026-06-01 \
    --end-date 2026-06-30 \
    --output data/raw/test1/bilibili_u001_student.csv \
    --seed 42
"""

from __future__ import annotations

import argparse
import csv
import random
from collections import Counter, defaultdict
from datetime import date, datetime, time, timedelta
from pathlib import Path


APP = "哔哩哔哩"
FIELDS = ["user_id", "timestamp", "app", "operation", "user_group"]
TIME_FMT = "%Y-%m-%d %H:%M:%S"

BILIBILI_OP_VOCAB = {
    "<PAD>": 0,
    "<UNK>": 1,
    "打开哔哩哔哩": 2,
    "浏览首页推荐": 3,
    "点击视频": 4,
    "播放视频": 5,
    "暂停视频": 6,
    "继续播放": 7,
    "拖动进度条": 8,
    "切换清晰度": 9,
    "开启全屏": 10,
    "退出全屏": 11,
    "发送弹幕": 12,
    "关闭弹幕": 13,
    "点赞视频": 14,
    "投币视频": 15,
    "收藏视频": 16,
    "转发视频": 17,
    "查看评论": 18,
    "发表评论": 19,
    "回复评论": 20,
    "关注UP主": 21,
    "进入UP主主页": 22,
    "搜索视频": 23,
    "查看分区": 24,
    "查看动态": 25,
    "发布动态": 26,
    "查看历史记录": 27,
    "查看稍后再看": 28,
    "缓存视频": 29,
    "切换倍速": 30,
    "返回首页": 31,
    "调整窗口": 32,
    "进入我的页面": 33,
    "点击发布": 34,
    "上传本地文件": 35,
    "点击去发布": 36,
    "选择分区和标签": 37,
    "确认选择": 38,
    "查看稿件": 39,
    "进入分区": 40,
    "最小化窗口": 41,
}

USER_GROUP_VOCAB = {
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

OPEN = "打开哔哩哔哩"
HOME = "浏览首页推荐"
CLICK_VIDEO = "点击视频"
PLAY = "播放视频"
PAUSE = "暂停视频"
RESUME = "继续播放"
SEEK = "拖动进度条"
QUALITY = "切换清晰度"
FULLSCREEN = "开启全屏"
EXIT_FULLSCREEN = "退出全屏"
DANMAKU = "发送弹幕"
CLOSE_DANMAKU = "关闭弹幕"
LIKE = "点赞视频"
COIN = "投币视频"
FAVORITE = "收藏视频"
SHARE = "转发视频"
COMMENTS = "查看评论"
POST_COMMENT = "发表评论"
REPLY_COMMENT = "回复评论"
FOLLOW = "关注UP主"
UP_PAGE = "进入UP主主页"
SEARCH = "搜索视频"
CATEGORIES = "查看分区"
DYNAMIC = "查看动态"
POST_DYNAMIC = "发布动态"
HISTORY = "查看历史记录"
WATCH_LATER = "查看稍后再看"
CACHE = "缓存视频"
SPEED = "切换倍速"
BACK_HOME = "返回首页"
RESIZE = "调整窗口"
MY_PAGE = "进入我的页面"
PUBLISH = "点击发布"
UPLOAD = "上传本地文件"
GO_PUBLISH = "点击去发布"
SELECT_TAG = "选择分区和标签"
CONFIRM = "确认选择"
MANUSCRIPT = "查看稿件"
ENTER_CATEGORY = "进入分区"
MINIMIZE = "最小化窗口"

BASE_TRANSITION_WEIGHTS = {
    OPEN: {HOME: 0.30, SEARCH: 0.25, CATEGORIES: 0.12, DYNAMIC: 0.08, MY_PAGE: 0.15, RESIZE: 0.07, MINIMIZE: 0.03},
    HOME: {CLICK_VIDEO: 0.55, SEARCH: 0.12, CATEGORIES: 0.08, DYNAMIC: 0.08, MY_PAGE: 0.05, RESIZE: 0.04, BACK_HOME: 0.08},
    SEARCH: {CLICK_VIDEO: 0.68, SEARCH: 0.06, CATEGORIES: 0.06, MY_PAGE: 0.04, BACK_HOME: 0.16},
    CATEGORIES: {ENTER_CATEGORY: 0.70, SEARCH: 0.10, HOME: 0.10, BACK_HOME: 0.10},
    ENTER_CATEGORY: {CLICK_VIDEO: 0.65, SEARCH: 0.10, CATEGORIES: 0.10, BACK_HOME: 0.15},
    DYNAMIC: {CLICK_VIDEO: 0.35, UP_PAGE: 0.18, COMMENTS: 0.10, POST_DYNAMIC: 0.07, BACK_HOME: 0.20, MY_PAGE: 0.10},
    MY_PAGE: {HISTORY: 0.22, WATCH_LATER: 0.20, MANUSCRIPT: 0.16, PUBLISH: 0.12, DYNAMIC: 0.10, BACK_HOME: 0.20},
    HISTORY: {CLICK_VIDEO: 0.60, WATCH_LATER: 0.10, MANUSCRIPT: 0.05, BACK_HOME: 0.25},
    WATCH_LATER: {CLICK_VIDEO: 0.65, HISTORY: 0.10, BACK_HOME: 0.25},
    MANUSCRIPT: {CLICK_VIDEO: 0.30, PUBLISH: 0.20, DYNAMIC: 0.15, BACK_HOME: 0.35},
    CLICK_VIDEO: {PLAY: 0.92, BACK_HOME: 0.08},
    PLAY: {
        PAUSE: 0.08, SEEK: 0.08, QUALITY: 0.05, SPEED: 0.06, FULLSCREEN: 0.07,
        DANMAKU: 0.08, CLOSE_DANMAKU: 0.03, LIKE: 0.10, COIN: 0.04,
        FAVORITE: 0.08, SHARE: 0.03, COMMENTS: 0.12, UP_PAGE: 0.05,
        CACHE: 0.02, BACK_HOME: 0.13, MINIMIZE: 0.08,
    },
    PAUSE: {RESUME: 0.78, SEEK: 0.10, MINIMIZE: 0.07, BACK_HOME: 0.05},
    RESUME: {PLAY: 0.80, SEEK: 0.08, COMMENTS: 0.05, BACK_HOME: 0.07},
    SEEK: {PLAY: 0.70, SEEK: 0.10, PAUSE: 0.05, COMMENTS: 0.05, BACK_HOME: 0.10},
    QUALITY: {PLAY: 0.75, FULLSCREEN: 0.10, SEEK: 0.05, BACK_HOME: 0.10},
    SPEED: {PLAY: 0.78, SEEK: 0.08, COMMENTS: 0.04, BACK_HOME: 0.10},
    FULLSCREEN: {PLAY: 0.65, EXIT_FULLSCREEN: 0.20, DANMAKU: 0.08, SEEK: 0.07},
    EXIT_FULLSCREEN: {PLAY: 0.70, COMMENTS: 0.10, BACK_HOME: 0.20},
    DANMAKU: {PLAY: 0.55, COMMENTS: 0.15, CLOSE_DANMAKU: 0.10, LIKE: 0.08, BACK_HOME: 0.12},
    CLOSE_DANMAKU: {PLAY: 0.75, FULLSCREEN: 0.08, BACK_HOME: 0.17},
    LIKE: {COIN: 0.18, FAVORITE: 0.18, COMMENTS: 0.18, UP_PAGE: 0.12, PLAY: 0.14, BACK_HOME: 0.20},
    COIN: {FAVORITE: 0.25, COMMENTS: 0.15, PLAY: 0.25, BACK_HOME: 0.35},
    FAVORITE: {PLAY: 0.25, COMMENTS: 0.15, UP_PAGE: 0.10, BACK_HOME: 0.50},
    SHARE: {PLAY: 0.30, COMMENTS: 0.15, BACK_HOME: 0.55},
    COMMENTS: {POST_COMMENT: 0.18, REPLY_COMMENT: 0.12, LIKE: 0.12, UP_PAGE: 0.10, PLAY: 0.18, BACK_HOME: 0.30},
    POST_COMMENT: {PLAY: 0.35, COMMENTS: 0.25, BACK_HOME: 0.40},
    REPLY_COMMENT: {PLAY: 0.35, COMMENTS: 0.25, BACK_HOME: 0.40},
    UP_PAGE: {FOLLOW: 0.20, DYNAMIC: 0.25, CLICK_VIDEO: 0.20, BACK_HOME: 0.35},
    FOLLOW: {DYNAMIC: 0.30, CLICK_VIDEO: 0.15, BACK_HOME: 0.55},
    PUBLISH: {UPLOAD: 0.95, BACK_HOME: 0.05},
    UPLOAD: {GO_PUBLISH: 0.95, BACK_HOME: 0.05},
    GO_PUBLISH: {SELECT_TAG: 0.95, BACK_HOME: 0.05},
    SELECT_TAG: {CONFIRM: 0.85, SELECT_TAG: 0.10, BACK_HOME: 0.05},
    CONFIRM: {MANUSCRIPT: 0.45, DYNAMIC: 0.20, BACK_HOME: 0.35},
    POST_DYNAMIC: {DYNAMIC: 0.35, BACK_HOME: 0.40, MY_PAGE: 0.25},
    RESIZE: {HOME: 0.30, SEARCH: 0.22, CATEGORIES: 0.12, MY_PAGE: 0.16, RESIZE: 0.10, BACK_HOME: 0.10},
    BACK_HOME: {HOME: 0.38, SEARCH: 0.20, CATEGORIES: 0.12, DYNAMIC: 0.08, MY_PAGE: 0.12, MINIMIZE: 0.10},
    MINIMIZE: {OPEN: 1.0},
}

USER_OPERATION_MULTIPLIER = {
    "学生": {SEARCH: 1.8, CLICK_VIDEO: 1.2, PLAY: 1.2, SPEED: 1.7, FAVORITE: 1.5, WATCH_LATER: 1.6, HISTORY: 1.3, HOME: 1.2, PUBLISH: 0.4, UPLOAD: 0.4, POST_DYNAMIC: 0.5},
    "程序员": {SEARCH: 2.0, SPEED: 1.8, FAVORITE: 1.4, WATCH_LATER: 1.5, HISTORY: 1.4, COMMENTS: 0.7, DANMAKU: 0.6, POST_COMMENT: 0.5, REPLY_COMMENT: 0.5, PUBLISH: 0.4},
    "工程师": {SEARCH: 1.7, CATEGORIES: 1.4, ENTER_CATEGORY: 1.4, HISTORY: 1.4, FAVORITE: 1.3, WATCH_LATER: 1.3, POST_COMMENT: 0.5, PUBLISH: 0.4},
    "网红": {MY_PAGE: 2.0, PUBLISH: 2.3, UPLOAD: 2.0, GO_PUBLISH: 2.0, SELECT_TAG: 2.0, CONFIRM: 2.0, MANUSCRIPT: 2.0, DYNAMIC: 1.8, POST_DYNAMIC: 2.2, COMMENTS: 1.5, POST_COMMENT: 1.5, REPLY_COMMENT: 1.5},
    "办公人群": {RESIZE: 1.8, MINIMIZE: 1.7, BACK_HOME: 1.3, HOME: 1.2, CLICK_VIDEO: 0.9, PLAY: 0.9, POST_COMMENT: 0.5, PUBLISH: 0.4},
    "游戏用户": {CATEGORIES: 1.9, ENTER_CATEGORY: 1.9, FULLSCREEN: 1.8, DANMAKU: 1.6, COMMENTS: 1.5, SEEK: 1.5, SEARCH: 1.5, POST_DYNAMIC: 0.6},
    "影音娱乐用户": {HOME: 1.8, CLICK_VIDEO: 1.4, PLAY: 1.4, FULLSCREEN: 1.5, LIKE: 1.5, FAVORITE: 1.4, DANMAKU: 1.4, PUBLISH: 0.3},
    "金融用户": {SEARCH: 1.9, WATCH_LATER: 1.7, FAVORITE: 1.5, SPEED: 1.4, DANMAKU: 0.5, COMMENTS: 0.6, POST_COMMENT: 0.4, PUBLISH: 0.3},
    "通用用户": {},
}

USER_TIME_PROFILE = {
    "学生": {"weekday_use_prob": 0.70, "weekend_use_prob": 0.90, "weekday_sessions": (1, 3), "weekend_sessions": (2, 5), "session_duration_minutes": (12, 75)},
    "程序员": {"weekday_use_prob": 0.65, "weekend_use_prob": 0.75, "weekday_sessions": (1, 3), "weekend_sessions": (1, 4), "session_duration_minutes": (10, 65)},
    "工程师": {"weekday_use_prob": 0.60, "weekend_use_prob": 0.75, "weekday_sessions": (1, 2), "weekend_sessions": (1, 4), "session_duration_minutes": (8, 55)},
    "网红": {"weekday_use_prob": 0.90, "weekend_use_prob": 0.95, "weekday_sessions": (2, 6), "weekend_sessions": (2, 6), "session_duration_minutes": (8, 90)},
    "办公人群": {"weekday_use_prob": 0.65, "weekend_use_prob": 0.75, "weekday_sessions": (1, 3), "weekend_sessions": (1, 4), "session_duration_minutes": (6, 45)},
    "游戏用户": {"weekday_use_prob": 0.75, "weekend_use_prob": 0.95, "weekday_sessions": (1, 3), "weekend_sessions": (2, 5), "session_duration_minutes": (20, 120)},
    "影音娱乐用户": {"weekday_use_prob": 0.75, "weekend_use_prob": 0.90, "weekday_sessions": (1, 3), "weekend_sessions": (2, 5), "session_duration_minutes": (18, 100)},
    "金融用户": {"weekday_use_prob": 0.60, "weekend_use_prob": 0.55, "weekday_sessions": (1, 3), "weekend_sessions": (1, 2), "session_duration_minutes": (6, 45)},
    "通用用户": {"weekday_use_prob": 0.65, "weekend_use_prob": 0.80, "weekday_sessions": (1, 3), "weekend_sessions": (1, 4), "session_duration_minutes": (10, 70)},
}

ACTIVE_TIME_WINDOWS = {
    "学生": {"weekday": [("12:00", "13:30"), ("17:30", "23:20")], "weekend": [("09:30", "12:00"), ("14:00", "17:30"), ("19:00", "23:40")]},
    "程序员": {"weekday": [("12:00", "14:00"), ("19:00", "00:20")], "weekend": [("10:00", "12:00"), ("14:00", "17:00"), ("19:00", "00:20")]},
    "工程师": {"weekday": [("07:30", "08:40"), ("12:00", "13:30"), ("18:30", "22:50")], "weekend": [("09:30", "12:00"), ("14:00", "17:00"), ("19:00", "22:50")]},
    "网红": {"weekday": [("10:00", "12:00"), ("14:00", "17:30"), ("19:00", "23:30")], "weekend": [("10:00", "12:00"), ("14:00", "17:30"), ("19:00", "23:30")]},
    "办公人群": {"weekday": [("07:30", "08:50"), ("12:00", "13:20"), ("18:00", "23:00")], "weekend": [("10:00", "12:00"), ("14:00", "17:00"), ("19:00", "23:00")]},
    "游戏用户": {"weekday": [("18:30", "00:30")], "weekend": [("10:00", "12:30"), ("14:00", "17:30"), ("19:00", "00:30")]},
    "影音娱乐用户": {"weekday": [("18:00", "23:40")], "weekend": [("10:00", "12:00"), ("14:00", "17:00"), ("19:00", "23:40")]},
    "金融用户": {"weekday": [("07:30", "09:00"), ("11:30", "13:30"), ("18:00", "22:30")], "weekend": [("10:00", "12:00"), ("19:00", "22:30")]},
    "通用用户": {"weekday": [("09:00", "23:30")], "weekend": [("09:00", "23:30")]},
}

ACTION_INTERVAL_SECONDS = {
    "window": (1, 20),
    "play_control": (2, 80),
    "comment": (4, 120),
    "danmaku": (4, 90),
    "publish": (5, 130),
    "browse": (3, 240),
    "normal": (3, 180),
    "interrupt": (1, 30),
    "video_watch": (60, 600),
}

CONTENT_SOURCE_OPS = {HOME, SEARCH, CATEGORIES, ENTER_CATEGORY, HISTORY, WATCH_LATER, MANUSCRIPT, DYNAMIC}
PLAY_CONTROL_OPS = {PAUSE, RESUME, SEEK, QUALITY, SPEED, FULLSCREEN, EXIT_FULLSCREEN, DANMAKU, CLOSE_DANMAKU, CACHE}
COMMENT_OPS = {COMMENTS, POST_COMMENT, REPLY_COMMENT}
PUBLISH_OPS = {PUBLISH, UPLOAD, GO_PUBLISH, SELECT_TAG, CONFIRM, POST_DYNAMIC}
MY_PAGE_OPS = {HISTORY, WATCH_LATER, MANUSCRIPT, PUBLISH}
NO_ADJACENT_REPEAT_OPS = {PLAY, HOME, COMMENTS, SELECT_TAG, CONFIRM, MINIMIZE, PUBLISH, UPLOAD, MY_PAGE, SEARCH, CLICK_VIDEO}
SESSION_END_OPS = {BACK_HOME, MINIMIZE, CONFIRM, MANUSCRIPT, FAVORITE, PLAY}
VALID_OPS = {op for op, idx in BILIBILI_OP_VOCAB.items() if idx >= 2}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate single-user Bilibili PC operation sequence data.")
    parser.add_argument("--user-id", required=True)
    parser.add_argument("--user-group", required=True)
    parser.add_argument("--start-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--end-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--output", required=True)
    parser.add_argument("--seed", type=int, default=None)
    return parser.parse_args()


def validate_user_group(user_group: str) -> None:
    if user_group not in USER_GROUP_VOCAB:
        valid = ", ".join(USER_GROUP_VOCAB)
        raise ValueError(f"unknown user_group: {user_group}; valid values: {valid}")


def normalize_weights(weights: dict[str, float]) -> dict[str, float]:
    total = sum(max(0.0, value) for value in weights.values())
    if total <= 0.0:
        return {}
    return {key: max(0.0, value) / total for key, value in weights.items() if value > 0.0}


def weighted_choice(weights: dict[str, float], rng: random.Random) -> str:
    normalized = normalize_weights(weights)
    if not normalized:
        raise ValueError("empty weighted choice")
    roll = rng.random()
    cumulative = 0.0
    last_key = next(iter(normalized))
    for key, weight in normalized.items():
        cumulative += weight
        last_key = key
        if roll <= cumulative:
            return key
    return last_key


def daterange(start_date: date, end_date: date):
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)


def is_weekend(date_obj: date) -> bool:
    return date_obj.weekday() >= 5


def should_use_today(user_group: str, date_obj: date, rng: random.Random) -> bool:
    profile = USER_TIME_PROFILE[user_group]
    key = "weekend_use_prob" if is_weekend(date_obj) else "weekday_use_prob"
    return rng.random() < profile[key]


def sample_daily_session_count(user_group: str, date_obj: date, rng: random.Random) -> int:
    profile = USER_TIME_PROFILE[user_group]
    lo, hi = profile["weekend_sessions" if is_weekend(date_obj) else "weekday_sessions"]
    return rng.randint(lo, hi)


def parse_hhmm(value: str) -> time:
    hour, minute = map(int, value.split(":"))
    return time(hour % 24, minute)


def window_bounds(date_obj: date, start: str, end: str) -> tuple[datetime, datetime]:
    start_dt = datetime.combine(date_obj, parse_hhmm(start))
    end_dt = datetime.combine(date_obj, parse_hhmm(end))
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)
    return start_dt, end_dt


def choose_session_start_time(user_group: str, date_obj: date, rng: random.Random) -> datetime:
    day_key = "weekend" if is_weekend(date_obj) else "weekday"
    windows = ACTIVE_TIME_WINDOWS[user_group][day_key]
    start_text, end_text = rng.choice(windows)
    start_dt, end_dt = window_bounds(date_obj, start_text, end_text)
    span_seconds = max(1, int((end_dt - start_dt).total_seconds()))
    return start_dt + timedelta(seconds=rng.randint(0, span_seconds - 1))


def sample_session_duration(user_group: str, date_obj: date, rng: random.Random) -> int:
    lo, hi = USER_TIME_PROFILE[user_group]["session_duration_minutes"]
    if is_weekend(date_obj):
        hi = int(hi * 1.15)
    return rng.randint(lo, hi)


def initial_context() -> dict[str, object]:
    return {
        "opened": False,
        "has_content_source": False,
        "clicked_video": False,
        "is_playing": False,
        "has_paused": False,
        "is_fullscreen": False,
        "has_viewed_comments": False,
        "in_my_page": False,
        "in_publish_flow": False,
        "publish_step": None,
        "last_operation": None,
        "current_scene_hint": None,
        "resize_run": 0,
        "seek_run": 0,
    }


def get_legal_next_operations(context: dict[str, object]) -> set[str]:
    legal = set(VALID_OPS)
    if not context["opened"]:
        return {OPEN}
    if not context["has_content_source"]:
        legal -= {CLICK_VIDEO, PLAY}
    if not context["is_playing"]:
        legal -= PLAY_CONTROL_OPS | {LIKE, COIN, FAVORITE, SHARE, CACHE}
    if not context["has_paused"]:
        legal.discard(RESUME)
    if not context["is_fullscreen"]:
        legal.discard(EXIT_FULLSCREEN)
    if not context["has_viewed_comments"]:
        legal -= {POST_COMMENT, REPLY_COMMENT}
    if not context["in_my_page"]:
        legal -= MY_PAGE_OPS
    step = context.get("publish_step")
    if context["in_publish_flow"]:
        return {
            PUBLISH: {UPLOAD},
            UPLOAD: {GO_PUBLISH},
            GO_PUBLISH: {SELECT_TAG},
            SELECT_TAG: {CONFIRM, SELECT_TAG},
            CONFIRM: {MANUSCRIPT, DYNAMIC, BACK_HOME},
        }.get(step, {BACK_HOME})
    return legal


def apply_user_multipliers(weights: dict[str, float], user_group: str) -> dict[str, float]:
    multipliers = USER_OPERATION_MULTIPLIER.get(user_group, {})
    return {op: weight * multipliers.get(op, 1.0) for op, weight in weights.items()}


def apply_context_rules(weights: dict[str, float], context: dict[str, object]) -> dict[str, float]:
    adjusted = dict(weights)
    if not context["has_content_source"]:
        for op in {HOME, SEARCH, CATEGORIES, DYNAMIC, MY_PAGE}:
            if op in adjusted:
                adjusted[op] *= 1.5
    if context["is_playing"]:
        for op in PLAY_CONTROL_OPS | {COMMENTS, LIKE, FAVORITE, BACK_HOME}:
            if op in adjusted:
                adjusted[op] *= 1.25
        if CLICK_VIDEO in adjusted:
            adjusted[CLICK_VIDEO] *= 0.45
    if context["has_paused"] and RESUME in adjusted:
        adjusted[RESUME] *= 2.4
    if context["is_fullscreen"]:
        for op in {EXIT_FULLSCREEN, PLAY, DANMAKU, SEEK}:
            if op in adjusted:
                adjusted[op] *= 1.5
    if context["resize_run"] >= 3:
        adjusted.pop(RESIZE, None)
    if context["seek_run"] >= 3:
        adjusted.pop(SEEK, None)
    last = context.get("last_operation")
    if last in NO_ADJACENT_REPEAT_OPS:
        adjusted.pop(str(last), None)
    return adjusted


def build_candidate_weights(last_operation: str, user_group: str, context: dict[str, object], rng: random.Random) -> dict[str, float]:
    base = dict(BASE_TRANSITION_WEIGHTS.get(last_operation, BASE_TRANSITION_WEIGHTS[BACK_HOME]))
    legal = get_legal_next_operations(context)
    weights = {op: weight for op, weight in base.items() if op in legal}
    if not weights:
        weights = {op: 1.0 for op in (legal & set(BASE_TRANSITION_WEIGHTS[OPEN]))}
    weights = apply_user_multipliers(weights, user_group)
    weights = apply_context_rules(weights, context)
    return normalize_weights(weights)


def sample_next_operation(last_operation: str, user_group: str, context: dict[str, object], rng: random.Random) -> str:
    weights = build_candidate_weights(last_operation, user_group, context, rng)
    if not weights:
        return BACK_HOME
    return weighted_choice(weights, rng)


def update_context(context: dict[str, object], operation: str) -> None:
    context["last_operation"] = operation
    context["resize_run"] = int(context["resize_run"]) + 1 if operation == RESIZE else 0
    context["seek_run"] = int(context["seek_run"]) + 1 if operation == SEEK else 0
    if operation == OPEN:
        context["opened"] = True
    if operation in CONTENT_SOURCE_OPS:
        context["has_content_source"] = True
    if operation == CLICK_VIDEO:
        context["clicked_video"] = True
    if operation == PLAY:
        context["is_playing"] = True
        context["has_paused"] = False
    if operation == PAUSE:
        context["is_playing"] = False
        context["has_paused"] = True
    if operation == RESUME:
        context["is_playing"] = True
        context["has_paused"] = False
    if operation == FULLSCREEN:
        context["is_fullscreen"] = True
    if operation == EXIT_FULLSCREEN:
        context["is_fullscreen"] = False
    if operation == COMMENTS:
        context["has_viewed_comments"] = True
    if operation == MY_PAGE:
        context["in_my_page"] = True
    if operation in {PUBLISH, UPLOAD, GO_PUBLISH, SELECT_TAG}:
        context["in_publish_flow"] = True
        context["publish_step"] = operation
    if operation == CONFIRM:
        context["in_publish_flow"] = False
        context["publish_step"] = CONFIRM
    if operation == BACK_HOME:
        context["in_my_page"] = False
        context["has_content_source"] = True


def operation_category(operation: str) -> str:
    if operation == RESIZE:
        return "window"
    if operation in {PAUSE, RESUME, SEEK, QUALITY, SPEED, FULLSCREEN, EXIT_FULLSCREEN}:
        return "play_control"
    if operation in COMMENT_OPS:
        return "comment"
    if operation in {DANMAKU, CLOSE_DANMAKU}:
        return "danmaku"
    if operation in PUBLISH_OPS:
        return "publish"
    if operation in {HOME, SEARCH, CATEGORIES, DYNAMIC, HISTORY, WATCH_LATER, MANUSCRIPT, ENTER_CATEGORY}:
        return "browse"
    if operation == MINIMIZE:
        return "interrupt"
    if operation == PLAY:
        return "video_watch"
    return "normal"


def sample_action_interval(operation: str, rng: random.Random) -> int:
    lo, hi = ACTION_INTERVAL_SECONDS[operation_category(operation)]
    return rng.randint(lo, hi)


def should_end_session(operation: str, current_time: datetime, session_end: datetime, rng: random.Random) -> bool:
    remaining = (session_end - current_time).total_seconds()
    if remaining <= 0:
        return True
    base = 0.03
    if operation in SESSION_END_OPS:
        base += 0.12
    if remaining < 180:
        base += 0.25
    return rng.random() < base


def make_row(user_id: str, ts: datetime, operation: str, user_group: str, session_id: int) -> dict[str, str]:
    return {
        "user_id": user_id,
        "timestamp": ts.strftime(TIME_FMT),
        "app": APP,
        "operation": operation,
        "user_group": user_group,
        "_session_id": str(session_id),
    }


def generate_session(user_id: str, user_group: str, session_start: datetime, session_end: datetime, rng: random.Random, session_id: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    current_time = session_start
    context = initial_context()
    operation = OPEN
    update_context(context, operation)
    rows.append(make_row(user_id, current_time, operation, user_group, session_id))
    while current_time < session_end:
        next_operation = sample_next_operation(operation, user_group, context, rng)
        current_time += timedelta(seconds=sample_action_interval(next_operation, rng))
        if current_time > session_end:
            break
        rows.append(make_row(user_id, current_time, next_operation, user_group, session_id))
        update_context(context, next_operation)
        operation = next_operation
        if should_end_session(operation, current_time, session_end, rng):
            break
    return rows


def validate_sequence(rows: list[dict[str, str]], user_id: str, user_group: str, start_date: date, end_date: date) -> dict[str, object]:
    checks: dict[str, bool | int | float] = {}
    times = [datetime.strptime(row["timestamp"], TIME_FMT) for row in rows]
    ops = [row["operation"] for row in rows]
    end_limit = datetime.combine(end_date + timedelta(days=1), time.min)
    checks["fields_complete"] = all(all(field in row for field in FIELDS) for row in rows)
    checks["app_valid"] = all(row["app"] == APP for row in rows)
    checks["user_id_valid"] = all(row["user_id"] == user_id for row in rows)
    checks["user_group_valid"] = all(row["user_group"] == user_group for row in rows)
    checks["operation_vocab_valid"] = all(op in VALID_OPS for op in ops)
    checks["no_pad_unk"] = all(op not in {"<PAD>", "<UNK>"} for op in ops)
    checks["timestamp_monotonic"] = all(a < b for a, b in zip(times, times[1:]))
    checks["timestamp_within_range"] = all(datetime.combine(start_date, time.min) <= ts < end_limit for ts in times)
    checks["window_adjust_ratio"] = (ops.count(RESIZE) / len(ops)) if ops else 0.0
    checks["window_adjust_ratio_ok"] = checks["window_adjust_ratio"] <= 0.05
    checks["max_consecutive_resize"] = max_consecutive(ops, RESIZE)
    checks["max_consecutive_seek"] = max_consecutive(ops, SEEK)
    checks["resize_run_ok"] = checks["max_consecutive_resize"] <= 3
    checks["seek_run_ok"] = checks["max_consecutive_seek"] <= 3
    checks["adjacent_repeat_ok"] = all(not (a == b and a in NO_ADJACENT_REPEAT_OPS) for a, b in zip(ops, ops[1:]))
    flow_checks = validate_flows(rows)
    checks.update(flow_checks)
    checks["total_rows"] = len(rows)
    checks["total_sessions"] = len({row["_session_id"] for row in rows})
    return checks


def max_consecutive(values: list[str], target: str) -> int:
    best = run = 0
    for value in values:
        run = run + 1 if value == target else 0
        best = max(best, run)
    return best


def validate_flows(rows: list[dict[str, str]]) -> dict[str, bool]:
    fsm_ok = publish_ok = comment_ok = play_ok = True
    by_session: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        by_session[row["_session_id"]].append(row["operation"])
    for ops in by_session.values():
        ctx = initial_context()
        expected_publish_next: str | None = None
        for op in ops:
            legal = get_legal_next_operations(ctx)
            if op != OPEN and op not in legal:
                fsm_ok = False
            if expected_publish_next and op not in {expected_publish_next, BACK_HOME}:
                publish_ok = False
            if op == PUBLISH:
                expected_publish_next = UPLOAD
            elif op == UPLOAD:
                expected_publish_next = GO_PUBLISH
            elif op == GO_PUBLISH:
                expected_publish_next = SELECT_TAG
            elif op == SELECT_TAG:
                expected_publish_next = CONFIRM
            elif op in {CONFIRM, BACK_HOME}:
                expected_publish_next = None
            if op in {POST_COMMENT, REPLY_COMMENT} and not ctx["has_viewed_comments"]:
                comment_ok = False
            if op in PLAY_CONTROL_OPS and op != RESUME and not ctx["is_playing"]:
                play_ok = False
            if op == RESUME and not ctx["has_paused"]:
                play_ok = False
            update_context(ctx, op)
    return {
        "fsm_legality": fsm_ok,
        "publish_flow_legality": publish_ok,
        "comment_flow_legality": comment_ok,
        "play_control_legality": play_ok,
    }


def write_csv(rows: list[dict[str, str]], output_path: str) -> None:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in FIELDS})


def print_validation_report(rows: list[dict[str, str]], checks: dict[str, object], user_id: str, user_group: str, start_date: date, end_date: date) -> None:
    status = lambda ok: "PASS" if ok else "FAIL"
    daily_sessions = Counter(row["timestamp"][:10] for row in rows if row["operation"] == OPEN)
    op_counts = Counter(row["operation"] for row in rows)
    print("Validation Report")
    print("-----------------")
    print(f"User ID: {user_id}")
    print(f"User Group: {user_group}")
    print(f"Date range: {start_date} ~ {end_date}")
    print(f"Total rows: {checks['total_rows']}")
    print(f"Total sessions: {checks['total_sessions']}")
    print(f"App valid: {status(bool(checks['app_valid']))}")
    print(f"User ID valid: {status(bool(checks['user_id_valid']))}")
    print(f"User group valid: {status(bool(checks['user_group_valid']))}")
    print(f"Operation vocab valid: {status(bool(checks['operation_vocab_valid']))}")
    print(f"No PAD/UNK: {status(bool(checks['no_pad_unk']))}")
    print(f"Timestamp monotonic: {status(bool(checks['timestamp_monotonic']))}")
    print(f"Timestamp within range: {status(bool(checks['timestamp_within_range']))}")
    print(f"FSM legality: {status(bool(checks['fsm_legality']))}")
    print(f"Publish flow legality: {status(bool(checks['publish_flow_legality']))}")
    print(f"Comment flow legality: {status(bool(checks['comment_flow_legality']))}")
    print(f"Play control legality: {status(bool(checks['play_control_legality']))}")
    print(f"Window adjust ratio: {checks['window_adjust_ratio']:.2%} {status(bool(checks['window_adjust_ratio_ok']))}")
    print(f"Max consecutive 调整窗口: {checks['max_consecutive_resize']} {status(bool(checks['resize_run_ok']))}")
    print(f"Max consecutive 拖动进度条: {checks['max_consecutive_seek']} {status(bool(checks['seek_run_ok']))}")
    print(f"Adjacent repeat check: {status(bool(checks['adjacent_repeat_ok']))}")
    print(f"Daily sessions: {dict(sorted(daily_sessions.items()))}")
    print(f"Top operations: {op_counts.most_common(10)}")


def main() -> None:
    args = parse_args()
    validate_user_group(args.user_group)
    start = datetime.strptime(args.start_date, "%Y-%m-%d").date()
    end = datetime.strptime(args.end_date, "%Y-%m-%d").date()
    if end < start:
        raise ValueError("--end-date must be greater than or equal to --start-date")
    rng = random.Random(args.seed)
    range_end_exclusive = datetime.combine(end + timedelta(days=1), time.min)

    session_specs: list[tuple[datetime, datetime]] = []
    for current_date in daterange(start, end):
        if not should_use_today(args.user_group, current_date, rng):
            continue
        for _ in range(sample_daily_session_count(args.user_group, current_date, rng)):
            session_start = choose_session_start_time(args.user_group, current_date, rng)
            session_end = session_start + timedelta(minutes=sample_session_duration(args.user_group, current_date, rng))
            session_specs.append((session_start, session_end))

    rows: list[dict[str, str]] = []
    session_id = 0
    next_available: datetime | None = None
    for session_start, session_end in sorted(session_specs):
        if next_available is not None and session_start <= next_available:
            duration = session_end - session_start
            session_start = next_available + timedelta(seconds=rng.randint(60, 600))
            session_end = session_start + duration
        if session_start >= range_end_exclusive:
            continue
        if session_end > range_end_exclusive:
            session_end = range_end_exclusive
        session_id += 1
        rows.extend(generate_session(args.user_id, args.user_group, session_start, session_end, rng, session_id))
        next_available = session_end

    rows.sort(key=lambda row: row["timestamp"])
    # If independently sampled sessions overlap, shift later duplicate-or-equal timestamps by one second.
    last_ts: datetime | None = None
    for row in rows:
        ts = datetime.strptime(row["timestamp"], TIME_FMT)
        if last_ts is not None and ts <= last_ts:
            ts = last_ts + timedelta(seconds=1)
            row["timestamp"] = ts.strftime(TIME_FMT)
        last_ts = ts

    checks = validate_sequence(rows, args.user_id, args.user_group, start, end)
    write_csv(rows, args.output)
    print(f"saved: {args.output}")
    print_validation_report(rows, checks, args.user_id, args.user_group, start, end)
    failed = [key for key, value in checks.items() if key.endswith("_ok") or key.endswith("_valid") or key.endswith("_legality") or key in {"no_pad_unk", "timestamp_monotonic", "timestamp_within_range", "fsm_legality"} if value is False]
    if failed:
        raise SystemExit(f"validation failed: {', '.join(failed)}")


if __name__ == "__main__":
    main()
