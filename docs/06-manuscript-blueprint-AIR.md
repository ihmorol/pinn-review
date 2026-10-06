# Manuscript Blueprint — PINN Survey for *Artificial Intelligence Review*

**Status:** working draft (v0.1, 2026-10-06). Positioning and gap claims are provisional
until scout G's survey-landscape analysis lands (`research-notes/slice-G-reviews-meta.md`).

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

- Reading roadmap: `05-reading-roadmap.md` (tiered, ~4 weeks part-time).
- Writing order: sections 4 and 5 first (evidence-dense, table-driven), then 2–3, then
  1, 6–8, abstract last.
- One person can hold the whole corpus if the master tables (T1–T3) stay canonical:
  update `data/paper-inventory.csv` as the single source of truth and regenerate docs.
