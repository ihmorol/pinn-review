# Manuscript Blueprint — PINN Survey for *Artificial Intelligence Review*

**Status:** v1.0 (2026-10-07). Positioning below is grounded in slice G's verification of
the review landscape (13 reviews; `research-notes/slice-G-reviews-meta.md`).

## 1. The journal's formula

The target venue is Springer's **Artificial Intelligence Review** (s10462). The formula,
mirrored from our accepted-format BDA manuscript in the sibling repo (`bda/research/paper/manuscript.tex`):

| Element | Convention observed |
|---|---|
| Structure | Introduction → Literature Review (background → taxonomy → methods → platforms → applications → cross-cutting → future directions) → Tables & Figures → Conclusion |
| Review style | taxonomy-driven body, quantitative treatment of surveyed works, comparison tables, applications mapped per domain |
| References | large curated list (100–250 refs), recent-heavy, impact-factor venues |
| Abstract | one structured paragraph, ~200–300 words, ends with contribution list |
| Figures/tables | 10+ exhibits expected; tables carry the comparative weight |

## 2. Proposed title candidates

1. *Physics-Informed Neural Networks: A Component-Level Survey of Methods, Applications, and Industrial Deployment (2021–2026)*
2. *How Do PINNs Enforce Physics? A Cross-Industry Review of Architectures, Loss Design, and Training Practice*
3. *From Residual Penalties to Operator Learning: Mapping Five Years of Physics-Informed Neural Network Research*

## 3. Proposed section plan

| § | Content | Fed by |
|---|---|---|
| 1 | Introduction: PDEs everywhere vs cost of classical numerics; deep learning's data hunger; PINN promise; RQ1–RQ4; contribution list | 04-findings |
| 2 | Background & conceptual scope: PINN anatomy (network + autodiff + residual loss), problem classes (forward/inverse/operator), notation | 03-comparative |
| 3 | Taxonomy of the field: enforcement-mechanism axis (soft/hard/weak/energy/operator/hybrid) × problem-class axis × domain axis; PRISMA-style selection figure | 02-inventory, fig1 |
| 4 | Methodological components: architectures; loss composition & weighting; sampling & training schedules; UQ; operator learning; frameworks & benchmarks | slice A, B |
| 5 | Domain applications & industry adoption: fluids/aero, energy/power, climate, biomed, geoscience/civil, materials/mfg, finance; per-domain tables (physics enforced, mechanism, evidence level) | slices C–F |
| 6 | Cross-cutting analysis: reliability vs classical numerics; failure modes & mitigation maturity; reproducibility & benchmarks; adoption barriers | slices A–G |
| 7 | Future directions: gap-driven agenda (theory, scaling, industrialization) | 04-findings |
| 8 | Conclusion: answers to RQ1–RQ4 one by one | 04-findings |

## 4. Planned exhibits (draft numbering)

| # | Exhibit | Source |
|---|---|---|
| F1 | PRISMA-style literature selection flow | 01-search-log |
| F2 | Publication timeline by domain (2021–2026) | fig1_timeline |
| F3 | Enforcement mechanism × domain heatmap | fig2_domain_mechanism |
| F4 | PINN anatomy / pipeline diagram | 03-comparative (mermaid→redraw) |
| F5 | Taxonomy tree of the field | 03-comparative (mermaid) |
| F6 | Citations vs year bubble chart | fig4_citations |
| T1 | Master inventory excerpt: foundational & methodological works | 02-inventory |
| T2 | Loss-weighting & sampling methods comparison | 03-comparative |
| T3 | Domain applications master table (physics × mechanism × evidence) | 02-inventory |
| T4 | Software frameworks & benchmarks | 03-comparative |
| T5 | Existing reviews & their gaps (positioning) | slice G |

## 5. Reference strategy

- Target 150–220 references; ≥60% from 2021–2026; core venues: J. Comput. Phys., CMAME,
  SIAM, Nature Reviews Physics, Nature Machine Intelligence, Physics of Fluids, Applied
  Energy, IEEE Trans., Computers in Biology and Medicine, plus NeurIPS/ICLR/ICML.
- Starter BibTeX: `references/references.bib` (generated from verified inventory only).
- Every in-text claim must trace to an inventory row with a verification flag.

## 6. Solo-reviewer workflow

- Reading roadmap: `05-reading-roadmap.md` (tiered 4-week plan).
- Writing order: sections 4 and 5 first (evidence-dense, table-driven), then 2–3, then
  1, 6–8, abstract last.
- `data/paper-inventory.csv` is the single source of truth; regenerate derived docs with
  the `scripts/` pipeline rather than editing them by hand.

## 7. Positioning (verified against the review landscape, slice G)

The target journal already hosts **one** PINN review — Luo et al. 2025
(DOI:10.1007/s10462-025-11322-7), scoped to *PDE-problem methods* (forward/inverse) with a
problem×architecture×loss×training taxonomy, ~250+ citations. The 13 verified reviews
(Karniadakis 2021 NRP; Cuomo 2022 JSC; Willard 2022 ACM CSUR; 2025–2026 PIML and
operator-learning surveys) share one organizing axis — "how physics enters the model" —
and flag the same gaps (theory, benchmarks, UQ, training reliability). The only
bibliometric survey stops at 2022.

**Our differentiator (unoccupied as of 2026-10):** a **cross-industry, application-oriented
meta-survey** mapping *who uses PINNs → for which problem classes → enforcing which exact
physics → through which enforcement mechanism → with what evidence level*, integrating the
operator-learning branch and the benchmark/theory reality checks (Grossmann 2024;
risk-consistency 2025) into a single component-level synthesis with 2025–2026 currency.

Draft contribution list for the abstract:
1. An enforcement-mechanism taxonomy (soft / hard / weak-variational / energy / operator /
   hybrid) applied uniformly across 100+ verified works from 2021–2026.
2. Component-level comparison tables (architecture, loss weighting, sampling, training,
   software) — the manuscript's backbone.
3. A domain-by-domain adoption map (fluids, energy, climate, biomed, geoscience, materials,
   finance) with evidence tiers from research benchmark to clinical/industrial pilot.
4. A reliability synthesis: what benchmarks and theory actually license us to claim.
5. A gap-driven future-research agenda.

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Overlap with Luo 2025 (same venue) | cite and position explicitly in §1; differentiator is industry mapping + operator integration + evidence tiers |
| Citation counts drift | re-verify all counts at submission; inventory carries verification flags |
| Solo bandwidth | the corpus, tables, and reading roadmap are already solo-sized (4-week plan) |
