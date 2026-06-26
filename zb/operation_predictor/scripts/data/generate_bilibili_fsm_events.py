#!/usr/bin/env python3
"""Generate Bilibili operation events with FSM-style behavior chains."""

from __future__ import annotations

import argparse
import csv
import json
import random
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path


APP = "\u54d4\u54e9\u54d4\u54e9"
GROUP = "\u901a\u7528\u7528\u6237"

OPEN = "\u6253\u5f00\u54d4\u54e9\u54d4\u54e9"
HOME = "\u6d4f\u89c8\u9996\u9875\u63a8\u8350"
CLICK_VIDEO = "\u70b9\u51fb\u89c6\u9891"
PLAY = "\u64ad\u653e\u89c6\u9891"
PAUSE = "\u6682\u505c\u89c6\u9891"
RESUME = "\u7ee7\u7eed\u64ad\u653e"
SEEK = "\u62d6\u52a8\u8fdb\u5ea6\u6761"
QUALITY = "\u5207\u6362\u6e05\u6670\u5ea6"
FULLSCREEN = "\u5f00\u542f\u5168\u5c4f"
EXIT_FULLSCREEN = "\u9000\u51fa\u5168\u5c4f"
DANMAKU = "\u53d1\u9001\u5f39\u5e55"
CLOSE_DANMAKU = "\u5173\u95ed\u5f39\u5e55"
LIKE = "\u70b9\u8d5e\u89c6\u9891"
COIN = "\u6295\u5e01\u89c6\u9891"
FAVORITE = "\u6536\u85cf\u89c6\u9891"
SHARE = "\u8f6c\u53d1\u89c6\u9891"
COMMENTS = "\u67e5\u770b\u8bc4\u8bba"
POST_COMMENT = "\u53d1\u8868\u8bc4\u8bba"
REPLY_COMMENT = "\u56de\u590d\u8bc4\u8bba"
FOLLOW = "\u5173\u6ce8UP\u4e3b"
UP_PAGE = "\u8fdb\u5165UP\u4e3b\u4e3b\u9875"
SEARCH = "\u641c\u7d22\u89c6\u9891"
CATEGORIES = "\u67e5\u770b\u5206\u533a"
DYNAMIC = "\u67e5\u770b\u52a8\u6001"
POST_DYNAMIC = "\u53d1\u5e03\u52a8\u6001"
HISTORY = "\u67e5\u770b\u5386\u53f2\u8bb0\u5f55"
WATCH_LATER = "\u67e5\u770b\u7a0d\u540e\u518d\u770b"
CACHE = "\u7f13\u5b58\u89c6\u9891"
SPEED = "\u5207\u6362\u500d\u901f"
BACK_HOME = "\u8fd4\u56de\u9996\u9875"
RESIZE = "\u8c03\u6574\u7a97\u53e3"
MY_PAGE = "\u8fdb\u5165\u6211\u7684\u9875\u9762"
PUBLISH = "\u70b9\u51fb\u53d1\u5e03"
UPLOAD = "\u4e0a\u4f20\u672c\u5730\u6587\u4ef6"
GO_PUBLISH = "\u70b9\u51fb\u53bb\u53d1\u5e03"
SELECT_TAG = "\u9009\u62e9\u5206\u533a\u548c\u6807\u7b7e"
CONFIRM = "\u786e\u8ba4\u9009\u62e9"
MANUSCRIPT = "\u67e5\u770b\u7a3f\u4ef6"
ENTER_CATEGORY = "\u8fdb\u5165\u5206\u533a"
MINIMIZE = "\u6700\u5c0f\u5316\u7a97\u53e3"

ALL_OPS = {
    OPEN,
    HOME,
    CLICK_VIDEO,
    PLAY,
    PAUSE,
    RESUME,
    SEEK,
    QUALITY,
    FULLSCREEN,
    EXIT_FULLSCREEN,
    DANMAKU,
    CLOSE_DANMAKU,
    LIKE,
    COIN,
    FAVORITE,
    SHARE,
    COMMENTS,
    POST_COMMENT,
    REPLY_COMMENT,
    FOLLOW,
    UP_PAGE,
    SEARCH,
    CATEGORIES,
    DYNAMIC,
    POST_DYNAMIC,
    HISTORY,
    WATCH_LATER,
    CACHE,
    SPEED,
    BACK_HOME,
    RESIZE,
    MY_PAGE,
    PUBLISH,
    UPLOAD,
    GO_PUBLISH,
    SELECT_TAG,
    CONFIRM,
    MANUSCRIPT,
    ENTER_CATEGORY,
    MINIMIZE,
}

NO_ADJACENT_REPEAT = {
    HOME,
    PLAY,
    COMMENTS,
    CATEGORIES,
    LIKE,
    COIN,
    FAVORITE,
    SHARE,
    POST_DYNAMIC,
    PUBLISH,
    UPLOAD,
    GO_PUBLISH,
    SELECT_TAG,
    CONFIRM,
    MINIMIZE,
}

CHAIN_WEIGHTS = {
    "home_watch": 21,
    "search_watch": 15,
    "category_watch": 11,
    "playback_control": 13,
    "comment_interaction": 9,
    "up_dynamic": 5,
    "my_page_review": 8,
    "publish": 5,
    "window_resize": 4,
    "interrupt": 3,
    "bridge_mixed": 6,
}


def mojibake(text: str) -> str:
    return text.encode("utf-8").decode("gbk", errors="ignore")


def load_vocab_ops(path: Path) -> set[str]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8") as f:
        vocab = json.load(f)
    app_vocab = vocab.get(APP) or vocab.get(mojibake(APP))
    if not app_vocab:
        raise ValueError("Bilibili vocab not found in op_vocab.json")
    return {op for op in app_vocab if op not in {"<PAD>", "<UNK>"}}


def source_prefix(rng: random.Random) -> list[str]:
    roll = rng.random()
    if roll < 0.52:
        return [HOME]
    if roll < 0.78:
        return [SEARCH]
    return [CATEGORIES, ENTER_CATEGORY]


def watch_chain(rng: random.Random) -> list[str]:
    return [OPEN, *source_prefix(rng), CLICK_VIDEO, PLAY]


def home_watch(rng: random.Random) -> list[str]:
    variants = [
        [OPEN, HOME, CLICK_VIDEO, PLAY, LIKE, BACK_HOME],
        [OPEN, HOME, CLICK_VIDEO, PLAY, COMMENTS, BACK_HOME],
        [OPEN, HOME, CLICK_VIDEO, PLAY, UP_PAGE, BACK_HOME],
        [OPEN, HOME, CLICK_VIDEO, PLAY, DANMAKU, CLOSE_DANMAKU, BACK_HOME],
        [OPEN, HOME, CLICK_VIDEO, PLAY, SHARE, BACK_HOME],
    ]
    return rng.choice(variants)


def search_watch(rng: random.Random) -> list[str]:
    variants = [
        [OPEN, SEARCH, CLICK_VIDEO, PLAY, SPEED, PLAY, BACK_HOME],
        [OPEN, SEARCH, CLICK_VIDEO, PLAY, QUALITY, PLAY, BACK_HOME],
        [OPEN, SEARCH, CLICK_VIDEO, PLAY, SEEK, PLAY, BACK_HOME],
        [OPEN, SEARCH, CLICK_VIDEO, PLAY, FAVORITE, BACK_HOME],
    ]
    return rng.choice(variants)


def category_watch(rng: random.Random) -> list[str]:
    variants = [
        [OPEN, CATEGORIES, ENTER_CATEGORY, CLICK_VIDEO, PLAY, BACK_HOME],
        [OPEN, CATEGORIES, ENTER_CATEGORY, CLICK_VIDEO, PLAY, LIKE, BACK_HOME],
        [OPEN, CATEGORIES, ENTER_CATEGORY, CLICK_VIDEO, PLAY, UP_PAGE, BACK_HOME],
        [OPEN, CATEGORIES, ENTER_CATEGORY, CLICK_VIDEO, PLAY, COMMENTS, BACK_HOME],
    ]
    return rng.choice(variants)


def playback_control(rng: random.Random) -> list[str]:
    base = watch_chain(rng)
    variants = [
        [PAUSE, RESUME, PLAY, SEEK, PLAY],
        [SPEED, PLAY, QUALITY, PLAY],
        [FULLSCREEN, PLAY, EXIT_FULLSCREEN, PLAY],
        [SEEK, PLAY, SEEK, PLAY, SPEED, PLAY],
        [PAUSE, RESUME, PLAY, FULLSCREEN, EXIT_FULLSCREEN, BACK_HOME],
    ]
    return base + rng.choice(variants)


def comment_interaction(rng: random.Random) -> list[str]:
    base = watch_chain(rng)
    variants = [
        [COMMENTS, POST_COMMENT, BACK_HOME],
        [COMMENTS, REPLY_COMMENT, BACK_HOME],
        [COMMENTS, LIKE, FAVORITE, BACK_HOME],
        [COMMENTS, POST_COMMENT, REPLY_COMMENT, BACK_HOME],
    ]
    return base + rng.choice(variants)


def up_dynamic(rng: random.Random) -> list[str]:
    variants = [
        [OPEN, HOME, CLICK_VIDEO, PLAY, UP_PAGE, FOLLOW, BACK_HOME],
        [OPEN, HOME, CLICK_VIDEO, PLAY, UP_PAGE, DYNAMIC, BACK_HOME],
        [OPEN, DYNAMIC, UP_PAGE, FOLLOW, BACK_HOME],
        [OPEN, HOME, CLICK_VIDEO, PLAY, UP_PAGE, DYNAMIC, POST_DYNAMIC, BACK_HOME],
    ]
    return rng.choice(variants)


def my_page_review(rng: random.Random) -> list[str]:
    variants = [
        [OPEN, MY_PAGE, HISTORY, CLICK_VIDEO, PLAY, BACK_HOME],
        [OPEN, MY_PAGE, WATCH_LATER, CLICK_VIDEO, PLAY, BACK_HOME],
        [OPEN, MY_PAGE, MANUSCRIPT, CLICK_VIDEO, PLAY, BACK_HOME],
        [OPEN, MY_PAGE, HISTORY, CLICK_VIDEO, PLAY, CACHE, BACK_HOME],
    ]
    return rng.choice(variants)


def publish(rng: random.Random) -> list[str]:
    chain = [OPEN, MY_PAGE, PUBLISH, UPLOAD, GO_PUBLISH, SELECT_TAG, CONFIRM]
    if rng.random() < 0.22:
        chain += [SELECT_TAG, CONFIRM]
    if rng.random() < 0.16:
        chain.insert(2, RESIZE)
    return chain


def window_resize(rng: random.Random) -> list[str]:
    variants = [
        [OPEN, RESIZE, RESIZE, HOME, CLICK_VIDEO, PLAY],
        [OPEN, RESIZE, MY_PAGE, HISTORY, CLICK_VIDEO, PLAY],
        [OPEN, HOME, CLICK_VIDEO, PLAY, RESIZE, PLAY],
        [OPEN, RESIZE, SEARCH, CLICK_VIDEO, PLAY],
    ]
    return rng.choice(variants)


def interrupt(rng: random.Random) -> list[str]:
    variants = [
        [OPEN, HOME, CLICK_VIDEO, PLAY, MINIMIZE],
        [OPEN, SEARCH, CLICK_VIDEO, PLAY, MINIMIZE],
        [OPEN, CATEGORIES, ENTER_CATEGORY, CLICK_VIDEO, PLAY, MINIMIZE],
    ]
    return rng.choice(variants)


def bridge_mixed(rng: random.Random) -> list[str]:
    family = rng.choice(["publish_review", "multi_source_watch", "review_to_watch", "control_interrupt"])
    chain = [OPEN]

    if family == "publish_review":
        if rng.random() < 0.35:
            chain += [RESIZE] * rng.randint(1, 2)
        chain += [MY_PAGE, PUBLISH, UPLOAD, GO_PUBLISH, SELECT_TAG, CONFIRM]
        next_step = rng.random()
        if next_step < 0.18:
            chain += [MY_PAGE]
        elif next_step < 0.34:
            chain += [BACK_HOME, MY_PAGE]
        elif next_step < 0.58:
            chain += [DYNAMIC]
        else:
            chain += [BACK_HOME]
        if rng.random() < 0.55:
            chain += [rng.choice([HISTORY, WATCH_LATER, MANUSCRIPT]), CLICK_VIDEO, PLAY]
        return chain

    if family == "multi_source_watch":
        chain += rng.choice([[HOME], [SEARCH], [CATEGORIES, ENTER_CATEGORY]])
        chain += [CLICK_VIDEO, PLAY]
        for _ in range(rng.randint(1, 2)):
            hop = rng.choice([[BACK_HOME, HOME], [SEARCH], [CATEGORIES, ENTER_CATEGORY], [ENTER_CATEGORY], [UP_PAGE], []])
            chain += hop
            if chain[-1] == UP_PAGE:
                chain += [BACK_HOME, SEARCH]
            chain += [CLICK_VIDEO, PLAY]
        if rng.random() < 0.45:
            chain += rng.choice([[LIKE], [COMMENTS], [FAVORITE], [SHARE]])
        return chain

    if family == "review_to_watch":
        if rng.random() < 0.45:
            chain += [RESIZE]
        chain += [MY_PAGE, rng.choice([HISTORY, WATCH_LATER, MANUSCRIPT]), CLICK_VIDEO, PLAY]
        tail = rng.choice(
            [
                [BACK_HOME, HOME, CLICK_VIDEO, PLAY],
                [SEARCH, CLICK_VIDEO, PLAY],
                [CATEGORIES, ENTER_CATEGORY, CLICK_VIDEO, PLAY],
                [CACHE, BACK_HOME],
            ]
        )
        chain += tail
        return chain

    chain += rng.choice([[HOME], [SEARCH], [CATEGORIES, ENTER_CATEGORY]])
    chain += [CLICK_VIDEO, PLAY]
    controls = rng.sample([[SEEK, PLAY], [SPEED, PLAY], [QUALITY, PLAY], [PAUSE, RESUME, PLAY]], k=rng.randint(1, 2))
    for control in controls:
        chain += control
    chain += rng.choice([[BACK_HOME], [COMMENTS], [MINIMIZE], [UP_PAGE, BACK_HOME]])
    return chain


CHAIN_BUILDERS = {
    "home_watch": home_watch,
    "search_watch": search_watch,
    "category_watch": category_watch,
    "playback_control": playback_control,
    "comment_interaction": comment_interaction,
    "up_dynamic": up_dynamic,
    "my_page_review": my_page_review,
    "publish": publish,
    "window_resize": window_resize,
    "interrupt": interrupt,
    "bridge_mixed": bridge_mixed,
}


def clean_chain(chain: list[str]) -> list[str]:
    cleaned: list[str] = []
    for op in chain:
        if cleaned and cleaned[-1] == op and op in NO_ADJACENT_REPEAT:
            continue
        cleaned.append(op)
    return cleaned


def step_seconds(op: str, rng: random.Random) -> int:
    if op in {PLAY, PAUSE, RESUME, SEEK, SPEED, QUALITY, FULLSCREEN, EXIT_FULLSCREEN}:
        return rng.randint(2, 80)
    if op in {COMMENTS, POST_COMMENT, REPLY_COMMENT, DANMAKU, CLOSE_DANMAKU}:
        return rng.randint(4, 120)
    if op in {UPLOAD, GO_PUBLISH, SELECT_TAG, CONFIRM, PUBLISH}:
        return rng.randint(5, 130)
    if op == RESIZE:
        return rng.randint(1, 18)
    if op == MINIMIZE:
        return rng.randint(1, 10)
    return rng.randint(3, 240)


def next_session_start(ts: datetime, rng: random.Random) -> datetime:
    ts += timedelta(minutes=rng.randint(8, 220), seconds=rng.randint(0, 59))
    if ts.hour < 8:
        ts = ts.replace(hour=8, minute=rng.randint(0, 45), second=rng.randint(0, 59))
    if ts.hour > 23 or (ts.hour == 23 and ts.minute > 40):
        ts = (ts + timedelta(days=1)).replace(
            hour=rng.randint(8, 10),
            minute=rng.randint(0, 59),
            second=rng.randint(0, 59),
        )
    return ts


def make_user_times(user_count: int, rng: random.Random) -> dict[str, datetime]:
    base = datetime(2026, 6, 25, 8, 0, 0)
    times: dict[str, datetime] = {}
    for i in range(1, user_count + 1):
        times[f"u{i:03d}"] = base + timedelta(
            days=rng.randint(0, 18),
            hours=rng.randint(0, 12),
            minutes=rng.randint(0, 59),
            seconds=rng.randint(0, 59),
        )
    return times


def generate_rows(
    target_rows: int, user_count: int, seed: int
) -> tuple[list[dict[str, str]], Counter[str], Counter[str]]:
    rng = random.Random(seed)
    user_times = make_user_times(user_count, rng)
    users = list(user_times)
    scenes: list[tuple[str, list[str]]] = []
    rows: list[dict[str, str]] = []
    chain_counts: Counter[str] = Counter()
    chain_rows: Counter[str] = Counter()
    user_idx = 0

    for chain_name, percent in CHAIN_WEIGHTS.items():
        quota = round(target_rows * percent / 100)
        while chain_rows[chain_name] < quota:
            chain = clean_chain(CHAIN_BUILDERS[chain_name](rng))
            scenes.append((chain_name, chain))
            chain_counts[chain_name] += 1
            chain_rows[chain_name] += len(chain)

    rng.shuffle(scenes)
    for _chain_name, chain in scenes:
        user = users[user_idx % len(users)]
        user_idx += 1
        ts = next_session_start(user_times[user], rng)
        for op in chain:
            ts += timedelta(seconds=step_seconds(op, rng))
            rows.append(
                {
                    "user_id": user,
                    "timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
                    "app": APP,
                    "operation": op,
                    "user_group": GROUP,
                }
            )
        user_times[user] = ts

    rows.sort(key=lambda r: (r["user_id"], r["timestamp"]))
    return rows, chain_counts, chain_rows


def split_scenes(rows: list[dict[str, str]]) -> list[list[str]]:
    scenes: list[list[str]] = []
    current: list[str] = []
    for row in rows:
        op = row["operation"]
        if op == OPEN and current:
            scenes.append(current)
            current = []
        current.append(op)
    if current:
        scenes.append(current)
    return scenes


def max_run(values: list[str], target: str) -> int:
    best = run = 0
    for value in values:
        if value == target:
            run += 1
        else:
            run = 0
        best = max(best, run)
    return best


def validate(rows: list[dict[str, str]], vocab_ops: set[str]) -> None:
    errors: list[str] = []
    vocab_equiv = vocab_ops | {mojibake(op) for op in vocab_ops}

    for i, row in enumerate(rows, 1):
        op = row["operation"]
        if row["app"] != APP:
            errors.append(f"row {i}: invalid app")
        if row["user_group"] != GROUP:
            errors.append(f"row {i}: invalid user_group")
        if op not in ALL_OPS:
            errors.append(f"row {i}: unknown generated op {op}")
        if op not in vocab_equiv and mojibake(op) not in vocab_equiv:
            errors.append(f"row {i}: op not in Bilibili vocab {op}")

    by_user: defaultdict[str, list[datetime]] = defaultdict(list)
    for row in rows:
        by_user[row["user_id"]].append(datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S"))
    for user, times in by_user.items():
        if times != sorted(times):
            errors.append(f"{user}: timestamps are not sorted")

    operations = [row["operation"] for row in rows]
    for prev, cur in zip(operations, operations[1:]):
        if prev == cur and cur in NO_ADJACENT_REPEAT:
            errors.append(f"invalid adjacent repeat: {cur}")

    resize_ratio = operations.count(RESIZE) / len(operations)
    if resize_ratio > 0.05:
        errors.append(f"resize ratio too high: {resize_ratio:.3%}")
    if max_run(operations, RESIZE) > 3:
        errors.append("resize consecutive run > 3")
    if max_run(operations, SEEK) > 3:
        errors.append("seek consecutive run > 3")

    for scene in split_scenes(rows):
        state = {
            "opened": False,
            "source": False,
            "clicked": False,
            "playing": False,
            "paused": False,
            "fullscreen": False,
            "comments": False,
            "my_page": False,
            "publish": False,
            "upload": False,
            "go_publish": False,
        }
        if scene.count(RESIZE) > 3:
            errors.append("resize count > 3 in one scene")
        if scene.count(SEEK) > 3:
            errors.append("seek count > 3 in one scene")
        for op in scene:
            if op == OPEN:
                state["opened"] = True
            elif not state["opened"]:
                errors.append(f"operation before open: {op}")
            if op in {HOME, SEARCH, CATEGORIES, ENTER_CATEGORY, HISTORY, WATCH_LATER, MANUSCRIPT, DYNAMIC}:
                state["source"] = True
            if op == MY_PAGE:
                state["my_page"] = True
            if op in {HISTORY, WATCH_LATER, MANUSCRIPT, PUBLISH} and not state["my_page"]:
                errors.append(f"my-page operation without my page: {op}")
            if op == ENTER_CATEGORY and CATEGORIES not in scene[: scene.index(op)] and not state["playing"]:
                errors.append("enter category without category view")
            if op == CLICK_VIDEO and not state["source"]:
                errors.append("click video without content source")
            if op == CLICK_VIDEO:
                state["clicked"] = True
            if op == PLAY and not state["clicked"] and not state["paused"] and not state["fullscreen"]:
                errors.append("play without prior click/resume context")
            if op == PLAY:
                state["playing"] = True
                state["paused"] = False
            if op in {PAUSE, SEEK, SPEED, QUALITY, FULLSCREEN, DANMAKU, CLOSE_DANMAKU, LIKE, COIN, FAVORITE, SHARE, COMMENTS, CACHE} and not state["playing"]:
                errors.append(f"video control before play: {op}")
            if op == PAUSE:
                state["paused"] = True
                state["playing"] = False
            if op == RESUME and not state["paused"]:
                errors.append("resume without pause")
            if op == RESUME:
                state["playing"] = True
                state["paused"] = False
            if op == FULLSCREEN:
                state["fullscreen"] = True
            if op == EXIT_FULLSCREEN and not state["fullscreen"]:
                errors.append("exit fullscreen without fullscreen")
            if op == EXIT_FULLSCREEN:
                state["fullscreen"] = False
            if op == COMMENTS:
                state["comments"] = True
            if op in {POST_COMMENT, REPLY_COMMENT} and not state["comments"]:
                errors.append(f"comment action before comments: {op}")
            if op == PUBLISH:
                state["publish"] = True
            if op == UPLOAD and not state["publish"]:
                errors.append("upload before publish")
            if op == UPLOAD:
                state["upload"] = True
            if op == GO_PUBLISH and not state["upload"]:
                errors.append("go publish before upload")
            if op == GO_PUBLISH:
                state["go_publish"] = True
            if op == SELECT_TAG and not state["go_publish"]:
                errors.append("select tag before go publish")
            if op == CONFIRM and SELECT_TAG not in scene:
                errors.append("confirm before select tag")

    if errors:
        sample = "\n".join(errors[:20])
        raise ValueError(f"validation failed with {len(errors)} errors:\n{sample}")


def write_csv(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["user_id", "timestamp", "app", "operation", "user_group"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/raw/op_events_bilibili_fsm.csv")
    parser.add_argument("--vocab", default="data/vocab/op_vocab.json")
    parser.add_argument("--target-rows", type=int, default=15000)
    parser.add_argument("--users", type=int, default=80)
    parser.add_argument("--seed", type=int, default=20260624)
    args = parser.parse_args()

    output = Path(args.output)
    vocab = load_vocab_ops(Path(args.vocab))
    rows, chain_counts, chain_rows = generate_rows(args.target_rows, args.users, args.seed)
    validate(rows, vocab)
    write_csv(rows, output)

    op_counts = Counter(row["operation"] for row in rows)
    print(f"saved: {output}")
    print(f"rows: {len(rows)}")
    print(f"users: {len({row['user_id'] for row in rows})}")
    print(f"resize_ratio: {op_counts[RESIZE] / len(rows):.2%}")
    print("chain_rows:")
    for name in CHAIN_WEIGHTS:
        ratio = chain_rows[name] / len(rows)
        print(f"  {name}: {chain_rows[name]} ({ratio:.2%}), scenes={chain_counts[name]}")


if __name__ == "__main__":
    main()
