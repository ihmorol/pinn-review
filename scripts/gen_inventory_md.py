#!/usr/bin/env python
"""Generate docs/02-paper-inventory.md from data/paper-inventory.csv."""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "paper-inventory.csv"
OUT = ROOT / "docs" / "02-paper-inventory.md"


def load() -> list[dict]:
    with CSV.open(encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("title")]


def link(r: dict) -> str:
    ident = r.get("identifier", "")
    if ident.startswith("DOI:"):
        return f"[doi](https://doi.org/{ident[4:]})"
    if ident.startswith("arXiv:"):
        return f"[arXiv]({ident.replace('arXiv:', 'https://arxiv.org/abs/')})"
    return ident


def row_line(r: dict, cols: list[str]) -> str:
    cells = []
    for c in cols:
        v = r.get(c, "")
        if c == "title":
            v = f"**{v}**"
        elif c == "identifier":
            v = link(r)
        elif c == "citations":
            v = f"~{v}" if v not in ("", "n/a") else "n/a"
        cells.append(v.replace("|", "/"))
    return "| " + " | ".join(cells) + " |"


def table(rows: list[dict], cols: list[str], headers: list[str]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    out += [row_line(r, cols) for r in rows]
    return "\n".join(out)


METHOD_COLS = ["id", "title", "year", "venue", "type", "citations", "priority"]
METHOD_HEAD = ["ID", "Paper", "Year", "Venue", "Type", "Cites", "Read"]
DOMAIN_COLS = ["id", "domain", "physics", "mechanism", "problem_type", "citations", "priority"]
DOMAIN_HEAD = ["ID", "Domain", "Physics enforced", "Mechanism", "Problem", "Cites", "Read"]

PRIORITY_NAME = {"1": "must-read", "2": "careful", "3": "methods+results", "4": "skim", "5": "reference"}


def main() -> int:
    rows = load()
    for r in rows:
        r["priority_num"] = re.sub(r"\D", "", r.get("priority", "5")) or "5"
        r["priority"] = PRIORITY_NAME.get(r["priority_num"], r.get("priority"))
    by_id = {r["id"]: r for r in rows}

    def take(prefix: str) -> list[dict]:
        return sorted((r for r in rows if r["id"].startswith(f"PINN-{prefix}")),
                      key=lambda r: (int(r["priority_num"]), r["id"]))

    a, b, c, d, e, f, g = (take(x) for x in "ABCDEFG")
    years = Counter(r["year"] for r in rows)
    venues = Counter(r["venue"] for r in rows)
    n_journals = sum(1 for r in rows if r["type"] == "journal")
    n_conf = sum(1 for r in rows if r["type"] == "conference")
    n_pre = sum(1 for r in rows if r["type"] == "preprint")

    parts: list[str] = []
    parts.append("""# Master Paper Inventory

**Machine-generated** from `data/paper-inventory.csv` (run `python scripts/gen_inventory_md.py`
to refresh). Citation counts are approximate snapshots (Semantic Scholar / Google Scholar,
2026-10-06/07) and drift; "Read" gives the recommended reading depth (1=must-read ... 5=reference).
Every entry was verified against its publisher page or the Semantic Scholar API — see
`docs/01-search-protocol-and-log.md`.

## Corpus at a glance

| Metric | Value |
|---|---|
| Unique verified papers | {n} |
| Journal / conference / preprint | {j} / {c} / {p} |
| Year distribution | {yrs} |
| Distinct venues | {v} |
| Cross-slice papers (surfaced by 2+ scouts) | {dup} |
""".format(n=len(rows), j=n_journals, c=n_conf, p=n_pre, v=len(venues),
           yrs=", ".join(f"{y}: {n}" for y, n in sorted(years.items())),
           dup=sum(1 for r in rows if "+" in r.get("slices", ""))))

    parts.append("## 1. Foundations, theory & training methodology (slice A)\n")
    parts.append(table(a, METHOD_COLS, METHOD_HEAD))
    parts.append("\n## 2. Architectures, enforcement variants & operator learning (slice B)\n")
    parts.append(table(b, METHOD_COLS, METHOD_HEAD))
    parts.append("\n## 3. Fluid mechanics, aerospace & thermal applications (slice C)\n")
    parts.append(table(c, DOMAIN_COLS, DOMAIN_HEAD))
    parts.append("\n## 4. Energy, power systems, batteries & climate (slice D)\n")
    parts.append(table(d, DOMAIN_COLS, DOMAIN_HEAD))
    parts.append("\n## 5. Biomedical, geoscience & civil applications (slice E)\n")
    if e:
        parts.append(table(e, DOMAIN_COLS, DOMAIN_HEAD))
    else:
        parts.append("_Slice E pending._")
    parts.append("\n## 6. Materials, manufacturing, finance & industrial ecosystem (slice F)\n")
    if f:
        parts.append(table(f, DOMAIN_COLS, DOMAIN_HEAD))
    else:
        parts.append("_Slice F pending._")
    parts.append("\n## 7. Existing reviews & meta-landscape (slice G)\n")
    if g:
        parts.append(table(g, METHOD_COLS, METHOD_HEAD))
    else:
        parts.append("_Slice G pending._")

    parts.append("""

## Reading-depth legend

| Priority | Meaning |
|---|---|
| must-read | read in full, take notes; these anchor the manuscript |
| careful | read thoroughly; cite for component claims |
| methods+results | read method + evaluation sections; skim the rest |
| skim | abstract + figures; cite for breadth |
| reference | lookup citation only |

Full per-paper detail (architecture, loss weighting, sampling, data regime, key results,
verification URLs) lives in `research-notes/slice-*.md` and `data/paper-inventory.csv`.
""")
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"OK: {OUT.relative_to(ROOT)} ({len(rows)} papers; "
          f"A:{len(a)} B:{len(b)} C:{len(c)} D:{len(d)} E:{len(e)} F:{len(f)} G:{len(g)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
