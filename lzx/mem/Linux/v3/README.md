# mem_analyze v3

v3 keeps the v2 runtime view as the first-level classification:

- `text`
- `data`
- `bss`
- `heap`
- `stack`
- `file`
- `anon`
- `special`

For ELF-backed mappings, v3 adds a second-level section label from the ELF
section header `sh_name`, such as `libc.so.6:.text` or `libxul.so:.rodata`.

Build:

```bash
gcc -Wall -Wextra -std=c11 -o mem_analyze-v3 mem_analyze-v3.c
```

Analyze one process:

```bash
sudo ./mem_analyze-v3 <pid> -o report.md
```

Analyze all processes matching an app keyword:

```bash
sudo ./mem_analyze-v3 --app firefox -o firefox.md
sudo ./mem_analyze-v3 firefox -o firefox.md
```

Single-run output is split:

```text
mem_analyze_run_x/
├── report.md
└── details/
    └── pid_<pid>_<name>_details/
        ├── index.md
        ├── page_data.tsv
        ├── full_report.md
        ├── fields.md
        └── part_001.md ...
```

The main `report.md` uses a matrix overview: rows are grouped by `maps`,
`smaps`, and `pagemap`; columns are the whole process plus first-level
segments.

The split `part_*.md` files are for reading. `page_data.tsv` is the preferred
machine-readable per-page data for page code export. Delta images require two
snapshots, so use watch output or pass `--before` and `--after`.

Watch a process:

```bash
sudo ./mem_analyze-v3 --watch 30 --interval 1 <pid> -o watch.md
```

Watch all processes matching an app keyword:

```bash
sudo ./mem_analyze-v3 --watch-app firefox --duration 30 --interval 1 -o watch.md
```

Export page code text files:

```bash
python3 export_page_codes.py <pid_report.md-or-pid_dir> -o page_codes --with-pfn
```

For single-run split output, pass the PID detail directory directly; the script
will use `page_data.tsv` inside it and write a `snapshot/` output:

```bash
python3 export_page_codes.py mem_analyze_run_x/details/pid_<pid>_<name>_details -o page_codes --with-pfn
```

Draw a delta image:

```bash
python3 draw_pfn_delta.py <pid_report.md-or-pid_dir> -o pfn_delta.png --top 20
```

Single-run detail directories contain only one snapshot and are rejected by the
delta tool. Use a watch process directory with `first_snapshot.md` and
`last_snapshot.md`, or pass two explicit snapshots with `--before` and `--after`.

This writes two images by default:

- `pfn_delta.png`: top changed second-level sections
- `pfn_delta_segments.png`: first-level segment aggregation
