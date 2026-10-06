# Physics-Informed Neural Networks (PINNs) — Literature Review Dossier

A research dossier supporting a survey paper on **Physics-Informed Neural Networks (PINNs)**,
formatted for Springer's **Artificial Intelligence Review** journal.

- **Owner:** Ikramul Hasan Morol (solo reviewer)
- **Started:** 2026-10-06
- **Time window surveyed:** 2021–2026 (plus seminal pre-2021 anchors)
- **Method:** deep-research protocol — 7 parallel scout agents, citation-verified
  inventory, MECE taxonomy synthesis, ranked reading roadmap

## Research questions

| # | Question |
|---|----------|
| RQ1 | Which industries/deployment settings use PINNs, and for which problem classes (forward / inverse / operator / control)? |
| RQ2 | What methodological components (architecture, enforcement mechanism, loss weighting, sampling, training, software) do recent works converge on? |
| RQ3 | What physics is enforced, and how (soft penalty / hard constraint / weak-variational / energy / operator / hybrid)? |
| RQ4 | What do existing reviews already cover — where is the gap for a new Artificial Intelligence Review submission? |

## Repository layout

```
pinn-review/
├── README.md                          <- this file
├── docs/
│   ├── 01-search-protocol-and-log.md  <- how the literature was searched (queries, criteria, counts)
│   ├── 02-paper-inventory.md          <- master tables of every verified paper
│   ├── 03-comparative-analysis.md     <- component-by-component comparison ("how they work")
│   ├── 04-findings-and-conclusions.md <- synthesis, trends, gaps, conclusions
│   ├── 05-reading-roadmap.md          <- ranked reading order for a solo reviewer
│   └── 06-manuscript-blueprint-AIR.md <- mapping to the Artificial Intelligence Review formula
├── research-notes/                    <- raw scout reports (provenance for every entry)
├── data/
│   └── paper-inventory.csv            <- machine-readable master inventory
├── figures/                           <- generated diagrams (PNG, 300 dpi)
├── scripts/
│   ├── consolidate.py                 <- scout reports -> CSV
│   └── make_figures.py                <- CSV -> figures
└── references/
    └── references.bib                 <- starter BibTeX for verified papers
```

## Status

| Step | Status |
|------|--------|
| Research brief frozen (RQ1–RQ4) | done |
| 7 scout slices dispatched (theory / architectures / fluids / energy / biomed+geo / materials+finance / meta-reviews) | done |
| Scout reports & verification | in progress |
| Consolidation, figures, dossier documents | pending |

> Working documents: citation counts are approximate (Semantic Scholar / Google Scholar
> snapshots, 2026-10-06) and every record carries a verification flag.
