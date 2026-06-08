#!/usr/bin/env python3
"""
memcap 内存快照对比分析工具

对比多次 memcap 采集结果，找出跨快照持续驻留的"热"内存区域。

用法:
    python3 scripts/analysis/analyze_memory.py -i memcap_out/
    python3 scripts/analysis/analyze_memory.py -i memcap_out/ --mode fuzzy --threshold 0.8

    python3 scripts/analysis/analyze_memory.py -i memcap_out/ --mode fuzzy --threshold 0.8

匹配模式:
  exact - 按 (pid, vma_start, vma_end) 精确匹配（PID 不变时用）
  fuzzy - 按 (pathname, region_type, perms) 语义匹配（PID 变化 / ASLR 时用）
  auto  - 自动检测（默认）：PID 相同的快照用 exact，不同 PID 的用 fuzzy
"""

import argparse
import csv
import os
import sys
from collections import defaultdict, namedtuple
from statistics import mean, stdev
from typing import Dict, List, Optional, Tuple

# (file content preserved from original scripts/analyze_memory.py)

VmaRow = namedtuple('VmaRow', [
    'sample_id', 'pid', 'timestamp_ms', 'snapshot_index',
    'vma_id', 'vma_start', 'vma_end', 'vma_size_kb',
    'perms', 'offset', 'dev', 'inode', 'pathname', 'region_type',
    'rss_kb', 'pss_kb', 'referenced_kb', 'anonymous_kb', 'swap_kb', 'vm_flags',
])

PagemapRow = namedtuple('PagemapRow', [
    'sample_id', 'pid', 'vma_id', 'vma_start', 'vma_end',
    'page_count', 'present_pages', 'not_present_pages', 'swapped_pages',
    'file_or_shared_pages', 'exclusive_pages', 'soft_dirty_pages',
    'present_ratio', 'swapped_ratio', 'scan_status',
])

SnapshotMeta = namedtuple('SnapshotMeta', [
    'sample_id', 'operation_id', 'app_id', 'app_name', 'process_name',
    'pid', 'timestamp_ms', 'snapshot_index', 'foreground_state', 'collect_status',
])

MatchedVma = namedtuple('MatchedVma', [
    'vma_key',          # 匹配键 (exact: "start-end" / fuzzy: "pathname|type|perms")
    'pathname', 'region_type', 'perms', 'vma_size_kb',
    'snapshots',        # List[SnapshotMeta] 该 VMA 出现在哪些快照中
    'rss_per_snap',     # List[long] 每个快照的 RSS
    'present_per_snap', # List[int] 每个快照的 present_pages
    'ratio_per_snap',   # List[float] 每个快照的 present_ratio
    'persistence',      # float 0-1，多少比例的快照中该 VMA 有显著物理驻留
])


# 以下函数与原脚本等效，省略中间注释以保持文件完整性
def parse_snapshot_index(csv_dir: str) -> List[SnapshotMeta]:
    path = os.path.join(csv_dir, 'snapshot_index.csv')
    if not os.path.isfile(path):
        print(f"[错误] 找不到 {path}", file=sys.stderr)
        sys.exit(1)
    rows = []
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r.get('collect_status', '') != 'success':
                continue
            rows.append(SnapshotMeta(
                sample_id=r.get('sample_id', ''),
                operation_id=r.get('operation_id', ''),
                app_id=r.get('app_id', ''),
                app_name=r.get('app_name', ''),
                process_name=r.get('process_name', ''),
                pid=int(r.get('pid', 0)),
                timestamp_ms=int(r.get('timestamp_ms', 0)),
                snapshot_index=r.get('snapshot_index', ''),
                foreground_state=r.get('foreground_state', ''),
                collect_status=r.get('collect_status', ''),
            ))
    return rows


def parse_vma_csv(csv_dir: str) -> List[VmaRow]:
    path = os.path.join(csv_dir, 'vma_memory_snapshot.csv')
    if not os.path.isfile(path):
        print(f"[错误] 找不到 {path}", file=sys.stderr)
        sys.exit(1)
    rows = []
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                rows.append(VmaRow(
                    sample_id=r.get('sample_id', ''),
                    pid=int(r.get('pid', 0)),
                    timestamp_ms=int(r.get('timestamp_ms', 0)),
                    snapshot_index=r.get('snapshot_index', ''),
                    vma_id=r.get('vma_id', ''),
                    vma_start=int(r.get('vma_start', '0'), 16),
                    vma_end=int(r.get('vma_end', '0'), 16),
                    vma_size_kb=int(r.get('vma_size_kb', 0)),
                    perms=r.get('perms', ''),
                    offset=r.get('offset', ''),
                    dev=r.get('dev', ''),
                    inode=r.get('inode', '0'),
                    pathname=r.get('pathname', ''),
                    region_type=r.get('region_type', ''),
                    rss_kb=int(r.get('rss_kb', 0)),
                    pss_kb=int(r.get('pss_kb', 0)),
                    referenced_kb=int(r.get('referenced_kb', 0)),
                    anonymous_kb=int(r.get('anonymous_kb', 0)),
                    swap_kb=int(r.get('swap_kb', 0)),
                    vm_flags=r.get('vm_flags', ''),
                ))
            except (ValueError, KeyError) as e:
                print(f"[警告] 跳过解析失败的行: {e}", file=sys.stderr)
                continue
    return rows


def parse_pagemap_csv(csv_dir: str) -> List[PagemapRow]:
    path = os.path.join(csv_dir, 'pagemap_snapshot.csv')
    if not os.path.isfile(path):
        print(f"[错误] 找不到 {path}", file=sys.stderr)
        sys.exit(1)
    rows = []
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                rows.append(PagemapRow(
                    sample_id=r.get('sample_id', ''),
                    pid=int(r.get('pid', 0)),
                    vma_id=r.get('vma_id', ''),
                    vma_start=int(r.get('vma_start', '0'), 16),
                    vma_end=int(r.get('vma_end', '0'), 16),
                    page_count=int(r.get('page_count', 0)),
                    present_pages=int(r.get('present_pages', 0)),
                    not_present_pages=int(r.get('not_present_pages', 0)),
                    swapped_pages=int(r.get('swapped_pages', 0)),
                    file_or_shared_pages=int(r.get('file_or_shared_pages', 0)),
                    exclusive_pages=int(r.get('exclusive_pages', 0)),
                    soft_dirty_pages=int(r.get('soft_dirty_pages', 0)),
                    present_ratio=float(r.get('present_ratio', 0)),
                    swapped_ratio=float(r.get('swapped_ratio', 0)),
                    scan_status=r.get('scan_status', ''),
                ))
            except (ValueError, KeyError) as e:
                print(f"[警告] 跳过解析失败的行: {e}", file=sys.stderr)
                continue
    return rows


def make_exact_key(vma: VmaRow) -> str:
    return f"{vma.pid}:{vma.vma_start:x}-{vma.vma_end:x}"


def make_fuzzy_key(vma: VmaRow) -> str:
    pn = vma.pathname.strip()
    return f"{pn}|{vma.region_type}|{vma.perms}"


def build_vma_index(vma_rows: List[VmaRow], key_func) -> Dict[str, List[VmaRow]]:
    idx = defaultdict(list)
    for v in vma_rows:
        idx[key_func(v)].append(v)
    return idx


def build_pagemap_index(pm_rows: List[PagemapRow]) -> Dict[Tuple[str, str], PagemapRow]:
    idx = {}
    for p in pm_rows:
        idx[(p.sample_id, p.vma_id)] = p
    return idx


def detect_mode(snapshots: List[SnapshotMeta]) -> str:
    pids = set(s.pid for s in snapshots)
    if len(pids) == 1:
        return 'exact'
    return 'fuzzy'


def match_and_compare(
    snapshots: List[SnapshotMeta],
    vma_rows: List[VmaRow],
    pm_index: Dict[Tuple[str, str], PagemapRow],
    mode: str,
    threshold: float,
) -> List[MatchedVma]:
    sample_ids = set(s.sample_id for s in snapshots)
    n_total = len(sample_ids)
    target_vmas = [v for v in vma_rows if v.sample_id in sample_ids]
    key_func = make_exact_key if mode == 'exact' else make_fuzzy_key
    vma_index = build_vma_index(target_vmas, key_func)
    results = []
    for key, group in vma_index.items():
        per_sample = defaultdict(list)
        for v in group:
            per_sample[v.sample_id].append(v)
        rep = group[0]
        snap_list = []
        rss_list = []
        present_list = []
        ratio_list = []
        present_count = 0
        for sid in sorted(sample_ids):
            if sid not in per_sample:
                continue
            v = per_sample[sid][0]
            pm = pm_index.get((sid, v.vma_id))
            snap_meta = next((s for s in snapshots if s.sample_id == sid), None)
            if snap_meta:
                snap_list.append(snap_meta)
            rss_list.append(v.rss_kb)
            if pm and pm.page_count > 0:
                ratio = pm.present_ratio
                present_list.append(pm.present_pages)
                ratio_list.append(ratio)
                if ratio >= threshold:
                    present_count += 1
            else:
                present_list.append(0)
                ratio_list.append(0.0)
        actual_snaps = len(rss_list)
        persistence = present_count / actual_snaps if actual_snaps > 0 else 0.0
        results.append(MatchedVma(
            vma_key=key,
            pathname=rep.pathname,
            region_type=rep.region_type,
            perms=rep.perms,
            vma_size_kb=rep.vma_size_kb,
            snapshots=snap_list,
            rss_per_snap=rss_list,
            present_per_snap=present_list,
            ratio_per_snap=ratio_list,
            persistence=persistence,
        ))
    results.sort(key=lambda x: x.persistence, reverse=True)
    return results


def classify(persistence: float) -> Tuple[str, str]:
    if persistence >= 0.9:
        return "Hot", "🔴"
    elif persistence >= 0.3:
        return "Dynamic", "🟡"
    else:
        return "Cold", "🔵"


def print_report(results: List[MatchedVma], threshold: float, n_total: int, mode: str):
    hot_total = sum(1 for r in results if r.persistence >= 0.9)
    dynamic_total = sum(1 for r in results if 0.3 <= r.persistence < 0.9)
    cold_total = sum(1 for r in results if r.persistence < 0.3)
    matched_total = len(results)
    hot_rss = sum(r.rss_per_snap[-1] for r in results if r.persistence >= 0.9) if results else 0
    print(f"""
================================================================================
  memcap 内存快照对比分析报告
================================================================================
模式:        {mode}（{'PID 相同，按地址精确匹配' if mode == 'exact' else 'PID 不同，按路径+类型+权限语义匹配'}）
阈值:        连续 {threshold*100:.0f}% 以上快照 present_ratio ≥ {threshold} 视为"热"
快照数:      {n_total}
匹配 VMA:    {matched_total}
================================================================================

## 摘要

| 类别 | VMA 数 | 占比 | 当前 Hot RSS 合计 |
|------|:-----:|:----:|:-----------------:|
| Hot   (persistence ≥ 90%) | {hot_total} | {hot_total/matched_total*100:.1f}% | {hot_rss/1024:.1f} MB |
| Dynamic (30% ≤ p < 90%)   | {dynamic_total} | {dynamic_total/matched_total*100:.1f}% | — |
| Cold   (p < 30%)          | {cold_total} | {cold_total/matched_total*100:.1f}% | — |

---

## Hot 区域 — 持续驻留物理内存（persistence ≥ 90%）

""")
    hot_count = 0
    for r in results:
        if r.persistence < 0.9:
            break
        hot_count += 1
        if hot_count <= 50:
            rss_str = " → ".join(f"{x} KB" for x in r.rss_per_snap)
            print(f"| `{r.pathname[:80]}` | {r.region_type} | {r.vma_size_kb} KB | "
                  f"{r.rss_per_snap[-1]} KB | {r.present_per_snap[-1]} 页 | "
                  f"{r.persistence*100:.0f}% |")
        else:
            print(f"\n... 还有 {hot_total - 50} 个 Hot VMA，完整列表请加 --full 输出\n")
            break
    if hot_count == 0:
        print("（无）\n")
    print(f"""
---

## Dynamic 区域 — 间歇驻留（30% ≤ p < 90%）

共 {dynamic_total} 个 VMA。

""")
    dyn_show = 0
    for r in results:
        if 0.3 <= r.persistence < 0.9:
            dyn_show += 1
            if dyn_show <= 10:
                print(f"| `{r.pathname[:80]}` | {r.region_type} | "
                      f"{' → '.join(f'{x:.0%}' for x in r.ratio_per_snap)} | "
                      f"{r.persistence*100:.0f}% |")
    if dyn_show == 0:
        print("（无）\n")
    elif dyn_show > 10:
        print(f"\n... 还有 {dynamic_total - 10} 个 Dynamic VMA\n")
    print(f"""
---

## Cold 区域 — 极少驻留（p < 30%）

共 {cold_total} 个 VMA，主要包括预留虚拟地址空间、未使用的映射等。

---

*报告由 analyze_memory.py 自动生成 | 阈值={threshold} | 模式={mode}*
""")


def main():
    parser = argparse.ArgumentParser(
        description='memcap 内存快照对比分析工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s -i memcap_out/
  %(prog)s -i memcap_out/ --mode fuzzy --threshold 0.7
  %(prog)s -i memcap_out/ --pid 42820                # 只分析指定 PID
  %(prog)s -i memcap_out/ --sample sample_001 sample_002  # 只对比指定快照
        """)
    parser.add_argument('-i', '--input', default='memcap_out',
                        help='memcap 输出目录（包含 snapshot_index.csv 等）')
    parser.add_argument('--mode', choices=('auto', 'exact', 'fuzzy'), default='auto')
    parser.add_argument('--threshold', type=float, default=0.8)
    parser.add_argument('--pid', type=int, default=None)
    parser.add_argument('--sample', nargs='+', help='只对比指定的 sample_id 列表')
    args = parser.parse_args()

    snapshots = parse_snapshot_index(args.input)
    if args.sample:
        snapshots = [s for s in snapshots if s.sample_id in set(args.sample)]
    if args.pid is not None:
        snapshots = [s for s in snapshots if s.pid == args.pid]
    if not snapshots:
        print("没有可用的快照。请检查输入目录或过滤条件。", file=sys.stderr)
        sys.exit(2)

    mode = args.mode
    if mode == 'auto':
        mode = detect_mode(snapshots)

    vma_rows = parse_vma_csv(args.input)
    pm_rows = parse_pagemap_csv(args.input)
    pm_index = build_pagemap_index(pm_rows)

    results = match_and_compare(snapshots, vma_rows, pm_index, mode, args.threshold)
    print_report(results, args.threshold, len(set(s.sample_id for s in snapshots)), mode)


if __name__ == '__main__':
    main()
