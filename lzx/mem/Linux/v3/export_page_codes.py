#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export per-page numeric code sequences from mem_analyze-v3 snapshots.

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
from typing import DefaultDict, Dict, Iterable, List, Optional, Tuple


SNAPSHOT_START_RE = re.compile(r"^### 开始快照", re.MULTILINE)
SNAPSHOT_END_RE = re.compile(r"^### 结束快照", re.MULTILINE)
CODE_SECTION_RE = re.compile(r"^## 逻辑区间 PFN 序列\s*$", re.MULTILINE)
NEXT_H2_RE = re.compile(r"^## ", re.MULTILINE)
REGION_HEADER_RE = re.compile(r"^### `([0-9a-fA-F]+)-([0-9a-fA-F]+)` ([^\n]+)$", re.MULTILINE)
CODE_BLOCK_RE = re.compile(r"- page_code_sequence：\s*```text\s*(.*?)\s*```", re.S)
PFN_BLOCK_RE = re.compile(r"- pfn_sequence：\s*```text\s*(.*?)\s*```", re.S)
PRIMARY_SEGMENT_RE = re.compile(r"- 一级段：(.+)")
SECONDARY_SECTION_RE = re.compile(r"- 二级 section：`([^`]*)`")


SEGMENT_ORDER = ["text", "data", "bss", "heap", "stack", "file", "anon", "special", "unknown"]


def normalize_segment(raw: str) -> str:
    token = raw.strip().split("/", 1)[0].strip()
    if token in SEGMENT_ORDER:
        return token
    for seg in SEGMENT_ORDER:
        if raw.startswith(seg + "/"):
            return seg
    return token or "unknown"


def sanitize(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("_") or "unknown"


def split_snapshots(report_path: Path) -> Tuple[str, Optional[str]]:
    if report_path.is_dir():
        page_data = report_path / "page_data.tsv"
        if page_data.exists():
            return page_data.read_text(encoding="utf-8", errors="ignore"), None
        before_path = report_path / "first_snapshot.md"
        after_path = report_path / "last_snapshot.md"
        full_path = report_path / "full_report.md"
        if full_path.exists():
            text = full_path.read_text(encoding="utf-8", errors="ignore")
            return text, None
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


def pfn_section(text: str) -> str:
    match = CODE_SECTION_RE.search(text)
    if not match:
        raise ValueError("快照中没有 `## 逻辑区间 PFN 序列`，请用 mem_analyze-v3 重新采样")
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


def parse_snapshot(text: str) -> Tuple[Dict[Tuple[str, str], List[str]], Dict[Tuple[str, str], List[str]]]:
    section = pfn_section(text)
    headers = list(REGION_HEADER_RE.finditer(section))
    codes: DefaultDict[Tuple[str, str], List[str]] = defaultdict(list)
    pfns: DefaultDict[Tuple[str, str], List[str]] = defaultdict(list)

    for idx, header in enumerate(headers):
        block_start = header.end()
        block_end = headers[idx + 1].start() if idx + 1 < len(headers) else len(section)
        block = section[block_start:block_end]
        key = parse_region_identity(header.group(3), block)
        codes[key].extend(parse_numeric_block(block, CODE_BLOCK_RE))
        pfns[key].extend(parse_numeric_block(block, PFN_BLOCK_RE))

    return dict(codes), dict(pfns)


def parse_snapshot_or_tsv(text: str) -> Tuple[Dict[Tuple[str, str], List[str]], Dict[Tuple[str, str], List[str]]]:
    if text.startswith("addr\tsegment\tsection\tstatus\tcode\tpfn"):
        codes: DefaultDict[Tuple[str, str], List[str]] = defaultdict(list)
        pfns: DefaultDict[Tuple[str, str], List[str]] = defaultdict(list)
        for line_no, line in enumerate(text.splitlines()):
            if line_no == 0 or not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 6:
                continue
            _addr, segment, section, _status, code, pfn = parts[:6]
            key = (normalize_segment(segment), section)
            codes[key].append(code)
            pfns[key].append(pfn)
        return dict(codes), dict(pfns)
    return parse_snapshot(text)


def sorted_keys(values: Dict[Tuple[str, str], List[str]]) -> List[Tuple[str, str]]:
    return sorted(values, key=lambda k: (SEGMENT_ORDER.index(k[0]) if k[0] in SEGMENT_ORDER else len(SEGMENT_ORDER), k[1]))


def write_numeric_files(out_dir: Path, label: str, values_by_section: Dict[Tuple[str, str], List[str]], suffix: str) -> List[Tuple[str, str, Path, int]]:
    written = []
    phase_dir = out_dir / label
    phase_dir.mkdir(parents=True, exist_ok=True)
    for segment, section in sorted_keys(values_by_section):
        values = values_by_section.get((segment, section), [])
        if not values:
            continue
        path = phase_dir / f"{sanitize(segment)}__{sanitize(section)}_{suffix}.txt"
        path.write_text(" ".join(values) + "\n", encoding="ascii")
        written.append((segment, section, path, len(values)))
    return written


def write_manifest(path: Path, rows: Iterable[Tuple[str, str, str, Path, int]]) -> None:
    lines = ["phase\tsegment\tsection\tpages\tpath"]
    for phase, segment, section, file_path, count in rows:
        lines.append(f"{phase}\t{segment}\t{section}\t{count}\t{file_path}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="导出 mem_analyze-v3 快照中的逐页数字状态 txt")
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

    before_codes, before_pfns = parse_snapshot_or_tsv(before_text)
    after_codes: Dict[Tuple[str, str], List[str]] = {}
    after_pfns: Dict[Tuple[str, str], List[str]] = {}
    if after_text is not None:
        after_codes, after_pfns = parse_snapshot_or_tsv(after_text)

    rows: List[Tuple[str, str, str, Path, int]] = []
    if after_text is None:
        for segment, section, path, count in write_numeric_files(args.out_dir, "snapshot", before_codes, "codes"):
            rows.append(("snapshot", segment, section, path, count))
    else:
        for segment, section, path, count in write_numeric_files(args.out_dir, "before", before_codes, "codes"):
            rows.append(("before", segment, section, path, count))
        for segment, section, path, count in write_numeric_files(args.out_dir, "after", after_codes, "codes"):
            rows.append(("after", segment, section, path, count))

    if args.with_pfn:
        if after_text is None:
            for segment, section, path, count in write_numeric_files(args.out_dir, "snapshot", before_pfns, "pfns"):
                rows.append(("snapshot_pfn", segment, section, path, count))
        else:
            for segment, section, path, count in write_numeric_files(args.out_dir, "before", before_pfns, "pfns"):
                rows.append(("before_pfn", segment, section, path, count))
            for segment, section, path, count in write_numeric_files(args.out_dir, "after", after_pfns, "pfns"):
                rows.append(("after_pfn", segment, section, path, count))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_manifest(args.out_dir / "manifest.tsv", rows)
    print(f"wrote {args.out_dir}")


if __name__ == "__main__":
    main()
