# Per-Paper Full-Text Analysis — Agent Instructions

(Reference file for the sequential full-paper analysis loop. The orchestrator passes
PAPER_ID, PDF_PATH and inventory context per launch.)

You are analyzing ONE paper from a verified PINN literature dossier, for a survey targeting
Springer's "Artificial Intelligence Review". Your row will be merged into the master
literature-review table (`data/literature-review-master.csv`) — the single source of truth
from which the entire survey manuscript will be written. Depth matters more than speed.

## Procedure (mandatory)

1. Read the field schema: `E:\University\11th_trimester\pinn-review\scripts\row_schema.json`
   (56 fields; definitions are binding).
2. Read the ENTIRE PDF at the given PDF_PATH with the Read tool, in chunks of <=10 pages
   using the `pages` parameter (e.g. pages="1-10", then "11-20", ...) until the last page.
   Do not skip sections: introduction, methods, loss formulation, experiments, tables,
   conclusions all feed different fields. For PDFs >10 pages the `pages` parameter is
   REQUIRED. If a chunk fails, retry once; if a paper's PDF is missing/unopenable, fall
   back to the publisher landing page via WebFetch and set analysis_confidence=abstract-only.
3. Fill EVERY field. Rules:
   - Extract ONLY what the paper itself states. Empty string "" when not stated — never guess.
   - Numbers verbatim with units and case names (e.g. "rel. L2 = 3.1e-3 on Burgers (T=1)").
   - `quotable_finding`: one verbatim sentence <=30 words + page number, chosen because it
     captures the paper's core claim cleanly.
   - `cross_paper_links`: use inventory IDs (PINN-A01 style) when the paper cites/builds on
     papers that are in our dossier (the famous ones are: Raissi 2019=PINN-A01,
     DeepONet=PINN-B12, FNO=PINN-B13, XPINN=PINN-B07, self-adaptive=PINN-A07, NTK=PINN-A06...).
   - JSON must be valid: write it to the exact output path with UTF-8, no trailing commas,
     all 56 field names present.
4. FINAL MESSAGE: exactly two lines:
   `DONE <PAPER_ID> pages=<N> confidence=<full-paper|partial|abstract-only>`
   `KEY: <one line, the most important extracted fact>`

## Output path

`E:\University\11th_trimester\pinn-review\data\rows\<PAPER_ID>.json`

## Quality bar

A reader must be able to write the survey's paragraph about this paper — including its
exact physics, its enforcement mechanism, its loss design, its numbers, and its honest
limitations — from your row alone, without opening the PDF.
