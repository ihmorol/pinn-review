#!/usr/bin/env python
"""Generate references/references.bib from verified rows of data/paper-inventory.csv.

Only records carrying a DOI or arXiv identifier are exported (no identifiers -> skipped).
Fields are kept conservative (author/year/title/venue/identifier); enrich from the
publisher page when finalizing the manuscript.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "paper-inventory.csv"
OUT = ROOT / "references" / "references.bib"

VENUE_WORDS = {"of", "the", "for", "and", "in", "on", "a", "an", "de", "des"}


def key_for(r: dict) -> str:
    first = re.split(r"[,\s]+", r["title"].strip())
    w = re.sub(r"[^A-Za-z0-9]", "", first[0] if first else "paper").lower() or "paper"
    return f"{w}{r['year']}"


def title_case_venue(v: str) -> str:
    return " ".join(w if w in VENUE_WORDS else w[0].upper() + w[1:]
                    for w in v.split()) if v else "Unknown Venue"


def entry(r: dict) -> str:
    k = key_for(r)
    ident = r.get("identifier", "")
    lines = [f"@article{{{k},"]
    if r["type"] == "conference":
        lines[0] = f"@inproceedings{{{k},"
    lines.append(f"  title = {{{r['title']}}},")
    lines.append(f"  year = {{{r['year']}}},")
    if r["type"] == "conference":
        lines.append(f"  booktitle = {{{title_case_venue(r['venue'])}}},")
    else:
        lines.append(f"  journal = {{{title_case_venue(r['venue'])}}},")
    if ident.startswith("DOI:"):
        lines.append(f"  doi = {{{ident[4:]}}},")
    elif ident.startswith("arXiv:"):
        lines.append(f"  eprint = {{{ident[6:]}}},")
        lines.append("  archiveprefix = {arXiv},")
    lines.append(f"  note = {{verified snapshot 2026-10; dossier ID {r['id']}; "
                 f"authors to be completed from publisher page}}")
    lines.append("}")
    return "\n".join(lines)


def main() -> int:
    with CSV.open(encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f)
                if r.get("title") and (r.get("identifier", "").startswith("DOI:")
                                       or r.get("identifier", "").startswith("arXiv:"))]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    header = ("""% references.bib — STARTER set auto-generated from the verified paper inventory.
% Author lists are intentionally empty: complete them from the publisher page as each
% reference enters the manuscript. IDs (PINN-xxx) map to data/paper-inventory.csv.

""")
    OUT.write_text(header + "\n\n".join(entry(r) for r in rows) + "\n", encoding="utf-8")
    print(f"OK: {len(rows)} entries -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
