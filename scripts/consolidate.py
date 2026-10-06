#!/usr/bin/env python
"""Consolidate scout reports (research-notes/slice-*.md) into data/paper-inventory.csv.

Each slice file must contain a '## Machine rows' section with pipe-delimited lines:
    <ID>|<Title>|<Year>|<Venue>|<Type>|<Identifier>|<Cites>|<Domain>|<Physics>|<Mechanism>|<Problem>|<Priority>|<Verified>

Also collects '## Queries used' lists into data/queries-log.md for the search log.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "research-notes"
OUT_CSV = ROOT / "data" / "paper-inventory.csv"
OUT_Q = ROOT / "data" / "queries-log.md"

COLUMNS = [
    "id", "title", "year", "venue", "type", "identifier", "citations",
    "domain", "physics", "mechanism", "problem_type", "priority", "verified",
    "slices",
]

ROW_RE = re.compile(r"^[A-G]\d{2}\|")


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", t.lower())[:60]


def parse_slice(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    rows, queries, warnings = [], [], []

    m = re.search(r"^## Machine rows\s*$(.*?)^(?=## |\Z)", text, re.M | re.S)
    if not m:
        warnings.append(f"{path.name}: no '## Machine rows' section found")
        return rows, queries, warnings

    for raw in m.group(1).splitlines():
        line = raw.strip()
        if not line or not ROW_RE.match(line):
            continue
        fields = [f.strip() for f in line.split("|")]
        if len(fields) > 13:  # stray pipe inside a middle field: merge into physics
            extra = fields[8:len(fields) - 4]
            fields = fields[:8] + [", ".join(extra)] + fields[len(fields) - 4:]
            warnings.append(f"{path.name}: merged {len(extra)} stray pipes in: {fields[0]}")
        if len(fields) < 13:
            warnings.append(f"{path.name}: skipped short row ({len(fields)} fields): {line[:80]}")
            continue
        rec = dict(zip(COLUMNS[:-1], fields))
        rec["priority"] = re.sub(r"\D", "", rec["priority"]) or "5"
        rec["citations"] = rec["citations"].lstrip("~").strip()
        rows.append(rec)

    q = re.search(r"^## Queries used\s*$(.*?)^## ", text, re.M | re.S)
    if q:
        for line in q.group(1).splitlines():
            line = line.strip().lstrip("-*0123456789. ").strip()
            if line and not line.startswith("#"):
                queries.append(line)
    return rows, queries, warnings


def main() -> int:
    all_rows: dict[str, dict] = {}
    all_queries: list[tuple[str, str]] = []
    all_warnings: list[str] = []

    files = sorted(NOTES.glob("slice-*.md"))
    if not files:
        print("No slice-*.md files found in research-notes/ yet.", file=sys.stderr)
        return 1

    for path in files:
        slice_name = re.sub(r"^slice-([A-G])-.+$", r"\1", path.name)
        rows, queries, warnings = parse_slice(path)
        for w in warnings:
            all_warnings.append(w)
        for q in queries:
            all_queries.append((slice_name, q))
        for rec in rows:
            rec["id"] = f"PINN-{rec['id']}"
            key = norm_title(rec["title"])
            if key in all_rows:
                all_rows[key]["slices"] += f"+{slice_name}"
                if rec["citations"] not in ("", "n/a") and all_rows[key]["citations"] in ("", "n/a"):
                    all_rows[key]["citations"] = rec["citations"]
            else:
                rec["slices"] = slice_name
                all_rows[key] = rec

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(all_rows.values())

    with OUT_Q.open("w", encoding="utf-8") as f:
        f.write("# Search queries used by scout agents\n\n")
        f.write("_Compiled from scout reports; verbatim query strings._\n\n")
        cur = None
        for s, q in all_queries:
            if s != cur:
                f.write(f"\n## Slice {s}\n\n")
                cur = s
            f.write(f"- {q}\n")
        if not all_queries:
            f.write("\n_(no queries recorded)_\n")

    n = len(all_rows)
    verified = sum(1 for r in all_rows.values() if r["verified"].upper().startswith("Y"))
    print(f"OK: {n} unique papers -> {OUT_CSV.relative_to(ROOT)}")
    print(f"    verified Y: {verified}/{n}")
    print(f"    queries logged: {len(all_queries)}")
    for w in all_warnings:
        print(f"    warn: {w}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
