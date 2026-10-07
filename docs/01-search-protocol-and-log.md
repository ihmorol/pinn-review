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

_Filled after consolidation: candidates screened → duplicates removed → verified → included._

## 4. Known limitations

- Single-pass web retrieval (no paid database access: no Web of Science/Scopus export);
  citation counts therefore approximate and slightly lag Google Scholar.
- Scout slices may overlap; cross-slice duplicates are merged in the master CSV.
- 2026 is only partially surveyed (year in progress at snapshot time).
