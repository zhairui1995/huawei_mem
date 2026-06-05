#!/usr/bin/env python3
"""Host-side HarmonyOS smaps collector driven by hdc.

This is the Python equivalent of the v6 Referenced workflow:
clear_refs -> user operation -> read smaps -> generate a Markdown report.
It does not build or push any device-side binary.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SEGMENTS = [
    "ark ts heap",
    "native heap",
    "AnonPage other",
    "FilePage other",
    "stack",
    ".so",
    ".hap",
    ".ttf",
    "dev",
    "GL",
    "Graph",
    "guard",
    "unknown",
]

MAP_HEADER_RE = re.compile(
    r"^([0-9a-fA-F]+)-([0-9a-fA-F]+)\s+"
    r"(\S+)\s+([0-9a-fA-F]+)\s+(\S+)\s+(\d+)\s*(.*)$"
)


@dataclass
class Vma:
    start: int
    end: int
    perms: str
    offset: int
    dev: str
    inode: int
    path: str
    segment: str = "unknown"
    size_kb: int = 0
    rss_kb: int = 0
    pss_kb: int = 0
    referenced_kb: int = 0
    swap_kb: int = 0

    @property
    def label(self) -> str:
        return f"{self.start:012x}-{self.end:012x}"


def run_cmd(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        args,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and proc.returncode != 0:
        cmd = " ".join(shlex.quote(a) for a in args)
        detail = proc.stderr.strip() or proc.stdout.strip()
        raise RuntimeError(f"command failed ({proc.returncode}): {cmd}\n{detail}")
    return proc


def hdc_shell(command: str, *, check: bool = True) -> str:
    return run_cmd(["hdc", "shell", command], check=check).stdout


def shell_quote(text: str) -> str:
    return "'" + text.replace("'", "'\"'\"'") + "'"


def read_proc_file(pid: int, name: str, *, check: bool = True) -> str:
    return hdc_shell(f"cat /proc/{pid}/{name}", check=check)


def read_exe_path(pid: int) -> str:
    out = hdc_shell(f"readlink /proc/{pid}/exe 2>/dev/null", check=False).strip()
    return out or "(cannot read /proc/<pid>/exe)"


def normalize_nul_text(text: str) -> str:
    return text.replace("\x00", " ").strip()


def contains_ci(haystack: str, needle: str) -> bool:
    return needle.lower() in haystack.lower()


def clean_deleted_suffix(path: str) -> str:
    suffix = " (deleted)"
    return path[: -len(suffix)] if path.endswith(suffix) else path


def has_suffix(path: str, suffix: str) -> bool:
    return clean_deleted_suffix(path).endswith(suffix)


def is_dev_path(path: str) -> bool:
    return path.startswith("/dev/") or path.startswith("anon_inode:")


def is_guard(path: str, perms: str) -> bool:
    return (
        contains_ci(path, "guard")
        or path == "[anon:thread signal stack guard page]"
        or perms.startswith("---")
    )


def is_graph(path: str) -> bool:
    keywords = ["graph", "graphic", "gralloc", "surface", "framebuffer", "frame_buffer", "bufferqueue", "sharedbuffer"]
    return any(contains_ci(path, key) for key in keywords)


def is_gl(path: str) -> bool:
    keywords = ["gl", "egl", "gles", "gpu", "mali", "vulkan", "render"]
    return any(contains_ci(path, key) for key in keywords)


def is_ark_ts_heap(path: str) -> bool:
    return (
        contains_ci(path, "ark ts heap")
        or contains_ci(path, "arkts heap")
        or contains_ci(path, "ark heap")
        or contains_ci(path, "ets heap")
        or contains_ci(path, "js heap")
        or (contains_ci(path, "ark") and contains_ci(path, "heap"))
    )


def is_native_heap(path: str) -> bool:
    if path == "[heap]":
        return True
    keywords = ["native heap", "malloc", "jemalloc", "scudo", "libc_malloc", "heap"]
    return any(contains_ci(path, key) for key in keywords)


def classify_vma(vma: Vma) -> str:
    path = vma.path
    is_anon = vma.inode == 0 and not path
    if is_guard(path, vma.perms):
        return "guard"
    if is_ark_ts_heap(path):
        return "ark ts heap"
    if is_native_heap(path):
        return "native heap"
    if path.startswith("[stack"):
        return "stack"
    if is_dev_path(path):
        return "dev"
    if is_gl(path):
        return "GL"
    if is_graph(path):
        return "Graph"
    if has_suffix(path, ".so"):
        return ".so"
    if has_suffix(path, ".hap"):
        return ".hap"
    if has_suffix(path, ".ttf") or has_suffix(path, ".otf"):
        return ".ttf"
    if is_anon:
        return "AnonPage other"
    if path:
        return "FilePage other"
    return "unknown"


def parse_kb_line(line: str) -> tuple[str, int] | None:
    if ":" not in line:
        return None
    key, rest = line.split(":", 1)
    match = re.search(r"(-?\d+)", rest)
    if not match:
        return None
    return key.strip(), int(match.group(1))


def parse_smaps(text: str) -> list[Vma]:
    vmas: list[Vma] = []
    current: Vma | None = None

    for raw in text.splitlines():
        line = raw.rstrip("\r\n")
        match = MAP_HEADER_RE.match(line)
        if match:
            if current is not None:
                current.segment = classify_vma(current)
                vmas.append(current)
            start, end, perms, offset, dev, inode, path = match.groups()
            current = Vma(
                start=int(start, 16),
                end=int(end, 16),
                perms=perms,
                offset=int(offset, 16),
                dev=dev,
                inode=int(inode),
                path=path.strip(),
            )
            continue

        if current is None:
            continue
        item = parse_kb_line(line)
        if item is None:
            continue
        key, kb = item
        if key == "Size":
            current.size_kb = kb
        elif key == "Rss":
            current.rss_kb = kb
        elif key == "Pss":
            current.pss_kb = kb
        elif key == "Referenced":
            current.referenced_kb = kb
        elif key == "Swap":
            current.swap_kb = kb

    if current is not None:
        current.segment = classify_vma(current)
        vmas.append(current)
    return vmas


def discover_pids(keyword: str) -> list[int]:
    ps_out = hdc_shell("ps -A -o PID,ARGS", check=False)
    candidates: set[int] = set()
    for line in ps_out.splitlines()[1:]:
        parts = line.strip().split(maxsplit=1)
        if not parts or not parts[0].isdigit():
            continue
        pid = int(parts[0])
        args = parts[1] if len(parts) > 1 else ""
        if contains_ci(args, keyword):
            candidates.add(pid)

    proc_listing = hdc_shell("ls /proc 2>/dev/null", check=False)
    for token in proc_listing.split():
        if not token.isdigit():
            continue
        pid = int(token)
        comm = read_proc_file(pid, "comm", check=False).strip()
        cmdline = normalize_nul_text(read_proc_file(pid, "cmdline", check=False))
        if contains_ci(comm, keyword) or contains_ci(cmdline, keyword):
            candidates.add(pid)

    return sorted(candidates)


def clear_refs(pid: int) -> None:
    cmd = f"echo 1 > /proc/{pid}/clear_refs"
    out = hdc_shell(cmd, check=False)
    # hdc sometimes reports shell redirection failures in stdout.
    if "Permission denied" in out or "No such file" in out or "not found" in out:
        raise RuntimeError(f"failed to clear /proc/{pid}/clear_refs:\n{out.strip()}")


def kb_pages(kb: int, page_size: int) -> int:
    if kb <= 0 or page_size <= 0:
        return 0
    return (kb * 1024 + page_size - 1) // page_size


def pct(numerator: int, denominator: int) -> float:
    return 100.0 * numerator / denominator if denominator > 0 else 0.0


def make_pid_output_path(base: Path, pid: int, total_count: int) -> Path:
    if total_count <= 1:
        return base
    if base.suffix:
        return base.with_name(f"{base.stem}_pid_{pid}{base.suffix}")
    return base.with_name(f"{base.name}_pid_{pid}.md")


def segment_summary(vmas: Iterable[Vma]) -> dict[str, dict[str, int]]:
    summary = {
        seg: {"vma_count": 0, "size": 0, "rss": 0, "pss": 0, "referenced": 0, "swap": 0}
        for seg in SEGMENTS
    }
    for vma in vmas:
        row = summary.setdefault(vma.segment, {"vma_count": 0, "size": 0, "rss": 0, "pss": 0, "referenced": 0, "swap": 0})
        row["vma_count"] += 1
        row["size"] += vma.size_kb
        row["rss"] += vma.rss_kb
        row["pss"] += vma.pss_kb
        row["referenced"] += vma.referenced_kb
        row["swap"] += vma.swap_kb
    return summary


def write_report(path: Path, pid: int, comm: str, cmdline: str, exe_path: str, vmas: list[Vma], include_vma: bool) -> None:
    page_size = 4096
    summary = segment_summary(vmas)
    total_size = sum(row["size"] for row in summary.values())
    total_rss = sum(row["rss"] for row in summary.values())
    total_pss = sum(row["pss"] for row in summary.values())
    total_ref = sum(row["referenced"] for row in summary.values())
    total_swap = sum(row["swap"] for row in summary.values())
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = [
        "# Referenced 操作后访问定位报告",
        "",
        "| 项目 | 值 |",
        "| --- | --- |",
        f"| PID | `{pid}` |",
        f"| 进程名 | `{comm or 'unknown'}` |",
        f"| 命令行 | `{cmdline or 'unknown'}` |",
        f"| 可执行文件 | `{exe_path}` |",
        f"| 采样时间 | `{now}` |",
        f"| VMA 数 | `{len(vmas)}` |",
        f"| Size | `{total_size} KiB` |",
        f"| Rss | `{total_rss} KiB` |",
        f"| Pss | `{total_pss} KiB` |",
        f"| Referenced | `{total_ref} KiB / {kb_pages(total_ref, page_size)} 页` |",
        f"| Swap | `{total_swap} KiB` |",
        "",
        "> 使用方法：先清空 `clear_refs`，再执行用户操作，然后立即采样。本报告中的 `Referenced` 表示观察窗口内被访问过的驻留页规模。",
        "",
        "## Referenced 段汇总",
        "",
        "| 一级段 | VMA 数 | Size(KiB) | Rss(KiB) | Pss(KiB) | Referenced(KiB) | Swap(KiB) | Referenced/Size | Referenced/Rss |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for seg in SEGMENTS:
        row = summary.get(seg)
        if not row or row["vma_count"] == 0:
            continue
        lines.append(
            f"| {seg} | {row['vma_count']} | {row['size']} | {row['rss']} | {row['pss']} | "
            f"{row['referenced']} | {row['swap']} | {pct(row['referenced'], row['size']):.2f}% | "
            f"{pct(row['referenced'], row['rss']):.2f}% |"
        )

    if include_vma:
        lines.extend(
            [
                "",
                "## Referenced VMA 定位",
                "",
                "| VMA | 一级段 | 权限 | Size(KiB) | Rss(KiB) | Pss(KiB) | Referenced(KiB) | Referenced页 | Referenced/Size | 路径 |",
                "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
            ]
        )
        for vma in sorted(vmas, key=lambda item: item.referenced_kb, reverse=True):
            path_text = vma.path or "(anonymous)"
            lines.append(
                f"| `{vma.label}` | {vma.segment} | `{vma.perms}` | {vma.size_kb} | {vma.rss_kb} | "
                f"{vma.pss_kb} | {vma.referenced_kb} | {kb_pages(vma.referenced_kb, page_size)} | "
                f"{pct(vma.referenced_kb, vma.size_kb):.2f}% | `{path_text}` |"
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def save_raw_files(raw_dir: Path, pid: int, files: dict[str, str]) -> None:
    pid_dir = raw_dir / f"pid_{pid}"
    pid_dir.mkdir(parents=True, exist_ok=True)
    for name, text in files.items():
        (pid_dir / f"{name}.txt").write_text(text, encoding="utf-8", errors="replace")


def collect_one(pid: int, output_path: Path, include_vma: bool, save_raw: bool, raw_dir: Path) -> None:
    smaps = read_proc_file(pid, "smaps")
    maps = read_proc_file(pid, "maps", check=False)
    comm = read_proc_file(pid, "comm", check=False).strip()
    cmdline = normalize_nul_text(read_proc_file(pid, "cmdline", check=False))
    exe_path = read_exe_path(pid)

    if save_raw:
        save_raw_files(raw_dir, pid, {"maps": maps, "smaps": smaps, "comm": comm, "cmdline": cmdline, "exe": exe_path})

    vmas = parse_smaps(smaps)
    if not vmas:
        raise RuntimeError(f"no VMA entries parsed from /proc/{pid}/smaps")
    write_report(output_path, pid, comm, cmdline, exe_path, vmas, include_vma)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Host-side HarmonyOS v6 Referenced collector over hdc.")
    parser.add_argument("target_pos", nargs="?", help="PID or app/package keyword.")
    parser.add_argument("--target", "-t", help="PID or app/package keyword. Overrides positional target.")
    parser.add_argument("--out", "-o", type=Path, default=Path(__file__).resolve().parent / "hdc_out", help="Output directory.")
    parser.add_argument("--operation-cmd", help="Host command to run between clear_refs and smaps sampling.")
    parser.add_argument("--with-vma", action="store_true", help="Include VMA-level details in the Markdown report.")
    parser.add_argument("--save-raw", action="store_true", help="Save raw maps/smaps/comm/cmdline/exe text.")
    parser.add_argument("--skip-clear-refs", action="store_true", help="Skip writing /proc/<pid>/clear_refs.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    target = args.target or args.target_pos
    if not target:
        print("missing target: pass --target <pid|app_keyword>", file=sys.stderr)
        return 1

    try:
        run_cmd(["hdc", "list", "targets"])
        if target.isdigit():
            pids = [int(target)]
        else:
            pids = discover_pids(target)
        if not pids:
            raise RuntimeError(f"no process matched target: {target}")

        print(f"matched PID(s): {', '.join(str(pid) for pid in pids)}")
        if not args.skip_clear_refs:
            for pid in pids:
                print(f"clearing referenced bits for PID {pid}")
                clear_refs(pid)

        if args.operation_cmd:
            print(f"running operation command: {args.operation_cmd}")
            subprocess.run(args.operation_cmd, shell=True, check=True)
        else:
            input("Referenced bits are cleared. Perform the target operation on the device, then press Enter...")

        timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        out_dir: Path = args.out
        raw_dir = out_dir / f"raw_{timestamp}"
        base_report = out_dir / f"referenced_{timestamp}.md"
        for pid in pids:
            report_path = make_pid_output_path(base_report, pid, len(pids))
            print(f"sampling PID {pid} -> {report_path}")
            collect_one(pid, report_path, args.with_vma, args.save_raw, raw_dir)
        print(f"done. output: {out_dir}")
        return 0
    except (RuntimeError, subprocess.CalledProcessError, KeyboardInterrupt) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
