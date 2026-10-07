# Search Protocol & Log

**Snapshot date:** 2026-10-06. **Corpus:** verified papers on physics-informed neural
networks, primary window 2021–2026, seminal pre-2021 anchors capped at 3 per slice.

## 1. Protocol

The deep-research method: freeze the brief (RQ1–RQ4 in `README.md`), run independent
scout perspectives, verify every candidate before inclusion, synthesize into a MECE
taxonomy, and calibrate every claim to the evidence.

### Scout slices (perspectives)

| Slice | Perspective | File |
|---|---|---|
| A | Foundations, theory, training methodology | `research-notes/slice-A-foundations-theory.md` |
| B | Architectures, enforcement variants, operator learning | `research-notes/slice-B-architectures-operator.md` |
| C | Fluid mechanics, aerospace, thermal applications | `research-notes/slice-C-fluids-aerospace-thermal.md` |
| D | Energy, power systems, batteries, climate/weather | `research-notes/slice-D-energy-power-climate.md` |
| E | Biomedical, geoscience, civil/structural | `research-notes/slice-E-biomed-geo-civil.md` |
| F | Materials, manufacturing, finance, industrial ecosystem | `research-notes/slice-F-materials-mfg-finance.md` |
| G | Survey-of-surveys, meta-landscape, venue metrics | `research-notes/slice-G-reviews-meta.md` |

### Inclusion criteria

1. Peer-reviewed journal/conference paper, or influential arXiv preprint (flagged `preprint`).
2. Venue quality bar: recognized high-impact journals or top AI/ML conferences.
3. Relevance to at least one research question (RQ1–RQ4).
4. Existence verified against the publisher landing page or the Semantic Scholar API.
5. Domain slices target 12–18 papers each with breadth across subtopics; the
   survey-of-surveys slice targets all major published reviews 2021–2026.

### Exclusion criteria

Predatory or unverifiable venues; near-duplicate method papers by the same team; works
that could not be verified (marked `needs-check` are quarantined, never cited).

### Verification & citation policy

- Every record was checked against a publisher page (Springer/Elsevier/IEEE/AIP/Nature/
  SIAM/arXiv/OpenReview) or `api.semanticscholar.org` (title, year, venue, citationCount).
- Citation counts are **approximate snapshots as of 2026-10-06** (Semantic Scholar preferred,
  Google Scholar snippets as fallback, marked `~`). They drift and are not authoritative.
- Records keep a per-paper `Verification` field; the master CSV carries `verified Y/N`.

## 2. Query log

Machine-compiled verbatim query strings per slice: [`data/queries-log.md`](../data/queries-log.md).
(Web search + Semantic Scholar API + publisher-page fetches were the only retrieval channels.)

## 3. Selection counts (PRISMA-style, coarse)

| Slice | Screened | Included | Notable exclusions (verification-driven) |
|---|---|---|---|
| A foundations/theory | 26 | 19 (+1 anchor) | RADAR & Nabian–Gladisch unverifiable → dropped; PDEArena out-of-scope |
| B architectures/operators | ~31 | 23 | Tancik 2020 folded into B04 (anchor budget) |
| C fluids/aero/thermal | 28 | 18 | — |
| D energy/power/climate | 24 | 19 | — |
| E biomed/geo/civil | ~24 | 14 | "Friha et al." healthcare survey NOT FOUND in Crossref/S2 → excluded; Kadeethum attribution corrected (PLOS ONE 2020) |
| F materials/mfg/finance/ecosystem | ~25 | 15 (13 + 2 vendor webpages) | "Vidyarthi et al." manufacturing survey unverifiable → dropped; Goswami venue corrected (TAFMEC, not CMAME) |
| G reviews/meta | 17 | 13 | Luo 2025 (G01) merged into A17; Grossmann 2024 (G08) merged into A13 — cross-slice duplicates |
| **Total (unique after cross-slice merge)** | **~175** | **117** | 109 fully verified / 8 flagged `verified: N` (quarantined) |

Cross-slice duplicates (e.g., Wang et al. SIAM JSC gradient-pathologies paper surfaced by
both A and B) are merged into single inventory rows with `slices = A+B`.


## 4. Known limitations

- Single-pass web retrieval (no paid database access: no Web of Science/Scopus export);
  citation counts therefore approximate and slightly lag Google Scholar.
- Scout slices may overlap; cross-slice duplicates are merged in the master CSV.
- 2026 is only partially surveyed (year in progress at snapshot time).
