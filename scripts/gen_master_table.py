#!/usr/bin/env python
"""Merge data/paper-inventory.csv + data/rows/<ID>.json -> data/literature-review-master.csv
(the single source of truth), plus a browsable digest and an xlsx when openpyxl exists."""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = ROOT / "data" / "paper-inventory.csv"
ROWS = ROOT / "data" / "rows"
SCHEMA = json.loads((ROOT / "scripts" / "row_schema.json").read_text(encoding="utf-8"))
FIELD_ORDER = [f["name"] for f in SCHEMA["fields"]]
OUT = ROOT / "data" / "literature-review-master.csv"
OUT_MD = ROOT / "docs" / "07-full-analysis-table.md"
OUT_XLSX = ROOT / "data" / "literature-review-master.xlsx"


def main() -> int:
    with INV.open(encoding="utf-8") as f:
        papers = {r["id"]: dict(r) for r in csv.DictReader(f) if r.get("title")}

    analyzed = {}
    for jf in sorted(ROWS.glob("PINN-*.json")):
        try:
            r = json.loads(jf.read_text(encoding="utf-8"))
            analyzed[r.get("paper_id", jf.stem)] = r
        except Exception as e:
            print(f"warn: bad json {jf.name}: {e}", file=sys.stderr)

    all_fields = list(papers[next(iter(papers))].keys()) + [f for f in FIELD_ORDER]
    seen, columns = set(), []
    for c in all_fields:
        if c not in seen:
            seen.add(c)
            columns.append(c)

    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columns)
        w.writeheader()
        for pid in sorted(papers):
            row = {c: "" for c in columns}
            row.update(papers[pid])
            if pid in analyzed:
                for k, v in analyzed[pid].items():
                    if isinstance(v, list):
                        v = " | ".join(str(x) for x in v)
                    row[k] = str(v)
            w.writerow(row)

    n = len(papers)
    n_an = len(analyzed & papers.keys())
    n_full = sum(1 for r in analyzed.values() if r.get("analysis_confidence") == "full-paper")
    lines = ["""# Full-Text Analysis Table (digest)

**The single source of truth is [`data/literature-review-master.csv`](../data/literature-review-master.csv)**
(one row per paper, 56 analysis fields + inventory fields — enough to write the manuscript
from this table alone). This digest renders the same data in readable column-bands.

## Coverage

| Metric | Value |
|---|---|
| Papers in inventory | {n} |
| Full-text analyzed (PDF read) | {full} |
| Partial / abstract-only | {part} |
| Pending analysis | {pend} |

_Col definitions: `scripts/row_schema.json`. Regenerate with `python scripts/gen_master_table.py`._
""".format(n=n, full=n_full, part=n_an - n_full, pend=n - n_an)]

    bands = [
        ("Identity & context", ["paper_id", "title", "authors_full", "year", "venue",
                                "primary_category", "domain_group", "subdomain",
                                "industry_context", "problem_class", "trl_evidence_level",
                                "citations_approx"]),
        ("Physics & enforcement", ["paper_id", "physics_enforced_exact", "pde_type",
                                   "dimensionality", "nonlinearity", "bcs_ic_handled",
                                   "enforcement_mechanism", "enforcement_details"]),
        ("Methodology", ["paper_id", "network_architecture", "activation_function",
                         "input_representation", "output_representation", "loss_terms",
                         "loss_weighting", "sampling_strategy", "optimizer_schedule",
                         "training_compute", "domain_decomposition",
                         "transfer_or_pretraining", "uq_method"]),
        ("Data, results & evaluation", ["paper_id", "data_regime", "datasets_used",
                                        "baselines_compared", "evaluation_metrics",
                                        "key_quantitative_results", "errors_reported",
                                        "speedup_claims", "ablations"]),
        ("Limitations & synthesis", ["paper_id", "stated_limitations", "failure_modes",
                                     "reproducibility", "quotable_finding", "relevance_rqs",
                                     "manuscript_section", "cross_paper_links",
                                     "notes_caveats", "analysis_confidence"]),
    ]

    for band, cols in bands:
        lines.append(f"\n## {band}\n")
        lines.append("| " + " | ".join(cols) + " |")
        lines.append("|" + "|".join(["---"] * len(cols)) + "|")
        for pid in sorted(papers):
            a = analyzed.get(pid, {})
            cells = []
            for c in cols:
                v = a.get(c, "") if c not in papers[pid] else papers[pid].get(c, "")
                v = str(v).replace("|", "/").replace("\n", " ").strip()
                cells.append(v if v else "—")
            lines.append("| " + " | ".join(cells) + " |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    try:
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "master"
        with OUT.open(encoding="utf-8") as f:
            for row in csv.reader(f):
                ws.append(row)
        wb.save(OUT_XLSX)
        xlsx = str(OUT_XLSX.name)
    except ImportError:
        xlsx = None

    print(f"OK: {OUT.name} ({n} rows, {len(columns)} cols); analyzed={n_an} "
          f"(full-paper {n_full}); digest -> {OUT_MD.name}; xlsx={xlsx}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
