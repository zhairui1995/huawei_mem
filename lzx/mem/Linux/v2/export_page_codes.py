#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export per-page numeric code sequences from mem_analyze-v2 snapshots.

The exported segment files contain numbers only. Each number is one virtual page
position in address order.

Code bitmask:
  0  no flag / not present
  1  present
  2  soft-dirty
  4  swapped
  8  exclusive
  16 file/shared
  32 PFN visible
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Tuple


SNAPSHOT_START_RE = re.compile(r"^### 开始快照", re.MULTILINE)
SNAPSHOT_END_RE = re.compile(r"^### 结束快照", re.MULTILINE)
CODE_SECTION_RE = re.compile(r"^## 逻辑区间 PFN 序列\s*$", re.MULTILINE)
NEXT_H2_RE = re.compile(r"^## ", re.MULTILINE)
REGION_HEADER_RE = re.compile(r"^### `([0-9a-fA-F]+)-([0-9a-fA-F]+)` ([^\n]+)$", re.MULTILINE)
CODE_BLOCK_RE = re.compile(r"- page_code_sequence：\s*```text\s*(.*?)\s*```", re.S)
PFN_BLOCK_RE = re.compile(r"- pfn_sequence：\s*```text\s*(.*?)\s*```", re.S)


SEGMENT_ORDER = ["text", "data", "bss", "heap", "stack", "file", "anon", "special", "unknown"]


def normalize_segment(raw: str) -> str:
    token = raw.strip().split("/", 1)[0].strip()
    return token if token in SEGMENT_ORDER else "unknown"


def sanitize(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("_") or "unknown"


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


def pfn_section(text: str) -> str:
    match = CODE_SECTION_RE.search(text)
    if not match:
        raise ValueError("快照中没有 `## 逻辑区间 PFN 序列`，请用新版 mem_analyze-v2 重新采样")
    next_h2 = NEXT_H2_RE.search(text, match.end())
    return text[match.end() : next_h2.start() if next_h2 else len(text)]


def parse_numeric_block(block_text: str, regex: re.Pattern[str]) -> List[str]:
    match = regex.search(block_text)
    if not match:
        return []
    text = match.group(1).strip()
    if text == "unavailable":
        return []
    return text.split()


def parse_snapshot(text: str) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    section = pfn_section(text)
    headers = list(REGION_HEADER_RE.finditer(section))
    codes: DefaultDict[str, List[str]] = defaultdict(list)
    pfns: DefaultDict[str, List[str]] = defaultdict(list)

    for idx, header in enumerate(headers):
        segment = normalize_segment(header.group(3))
        block_start = header.end()
        block_end = headers[idx + 1].start() if idx + 1 < len(headers) else len(section)
        block = section[block_start:block_end]
        codes[segment].extend(parse_numeric_block(block, CODE_BLOCK_RE))
        pfns[segment].extend(parse_numeric_block(block, PFN_BLOCK_RE))

    return dict(codes), dict(pfns)


def write_numeric_files(out_dir: Path, label: str, values_by_segment: Dict[str, List[str]], suffix: str) -> List[Tuple[str, Path, int]]:
    written = []
    phase_dir = out_dir / label
    phase_dir.mkdir(parents=True, exist_ok=True)
    for segment in SEGMENT_ORDER:
        values = values_by_segment.get(segment, [])
        if not values:
            continue
        path = phase_dir / f"{sanitize(segment)}_{suffix}.txt"
        path.write_text(" ".join(values) + "\n", encoding="ascii")
        written.append((segment, path, len(values)))
    return written


def write_manifest(path: Path, rows: Iterable[Tuple[str, str, Path, int]]) -> None:
    lines = ["phase\tsegment\tpages\tpath"]
    for phase, segment, file_path, count in rows:
        lines.append(f"{phase}\t{segment}\t{count}\t{file_path}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="导出 mem_analyze-v2 快照中的逐页数字状态 txt")
    parser.add_argument("report", nargs="?", type=Path, help="包含开始/结束快照的 PID 监控详情 Markdown，或含 first_snapshot.md/last_snapshot.md 的目录")
    parser.add_argument("--before", type=Path, help="操作前快照 Markdown")
    parser.add_argument("--after", type=Path, help="操作后快照 Markdown")
    parser.add_argument("-o", "--out-dir", type=Path, default=Path("page_codes"), help="输出目录")
    parser.add_argument("--with-pfn", action="store_true", help="同时导出 PFN 纯数字序列")
    args = parser.parse_args()

    if args.before and args.after:
        before_text = args.before.read_text(encoding="utf-8", errors="ignore")
        after_text = args.after.read_text(encoding="utf-8", errors="ignore")
    elif args.report:
        before_text, after_text = split_snapshots(args.report)
    else:
        parser.error("需要传入 report，或同时传入 --before 和 --after")

    before_codes, before_pfns = parse_snapshot(before_text)
    after_codes, after_pfns = parse_snapshot(after_text)

    rows: List[Tuple[str, str, Path, int]] = []
    for segment, path, count in write_numeric_files(args.out_dir, "before", before_codes, "codes"):
        rows.append(("before", segment, path, count))
    for segment, path, count in write_numeric_files(args.out_dir, "after", after_codes, "codes"):
        rows.append(("after", segment, path, count))

    if args.with_pfn:
        for segment, path, count in write_numeric_files(args.out_dir, "before", before_pfns, "pfns"):
            rows.append(("before_pfn", segment, path, count))
        for segment, path, count in write_numeric_files(args.out_dir, "after", after_pfns, "pfns"):
            rows.append(("after_pfn", segment, path, count))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_manifest(args.out_dir / "manifest.tsv", rows)
    print(f"wrote {args.out_dir}")


if __name__ == "__main__":
    main()
