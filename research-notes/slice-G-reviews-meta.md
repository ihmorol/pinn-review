# Slice G: Reviews, meta-landscape, venue metrics

## Queries used
1. physics-informed neural networks survey 2025 review
2. scientific machine learning review 2026 physics-informed
3. physics-informed neural networks bibliometric analysis CiteSpace
4. neural operator learning survey 2025 scientific computing
5. site:link.springer.com s10462 physics-informed
6. Faroughi physics-guided physics-informed physics-encoded neural networks operators survey venue
7. "Artificial Intelligence Review" "physics-informed" neural networks review s10462 2025 2026
8. Willard "Integrating physics-based modeling with machine learning" ACM Computing Surveys DOI
9. Grossmann "Can physics-informed neural networks beat the finite element method" IMA Journal
10. "Nature Reviews Physics" "Journal of Scientific Computing" "Nature Machine Intelligence" impact factor 2024
11. "Journal of Computational Physics" "Physics of Fluids" "Applied Energy" impact factor 2024 CiteScore
(+ Semantic Scholar API DOI lookups; Crossref API bibliographic queries; S2 hit persistent HTTP 429 for title searches)

## Screening summary
candidates screened: 17; included: 13
Excluded (domain-scout territory, one line): Ra et al. 2026 PIML in manufacturing (J. Manuf. Syst., ~29 cites); Valentim 2026 "From Data to Physics" (MDPI); Wang 2021 bibliometric (unrelated HMR topic); Neurocomputing 2026 "PINNs for differential equation solving" (methods consolidation, S0925231226007149); "Adaptive PINNs: A Survey" arXiv:2503.18181 (narrow training-adaptation scope); PINE neuro-evolution survey arXiv:2501.06572 (narrow).

## Review records

### G01
- Title / Authors (First et al.) / Year / Venue / Type / Identifier (DOI or arXiv) / URL / Citations (~N, source)
- Luo et al. (Luo, Gong, Ma, Xiang, Liu) / 2025 / Artificial Intelligence Review / comprehensive review / DOI 10.1007/s10462-025-11322-7 / https://link.springer.com/article/10.1007/s10462-025-11322-7 / ~250 (Semantic Scholar)
- Scope: PINNs for forward and inverse PDE problems across application areas; architecture, loss, training methods.
- Taxonomy: by PDE problem type (forward/inverse), network architecture, loss formulation, training strategy.
- Stated gaps/future directions: theory of convergence/generalization, benchmarks, uncertainty quantification, scaling to complex geometry/multiphysics.
- Not covered (our judgment): industry adoption mapping; operator learning; non-PDE physics constraints; cost/benefit vs classical solvers.
- Verification: verified via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s10462-025-11322-7 (AIR 58(10):323 confirmed via citing snippets)

### G02
- Karniadakis et al. (Karniadakis, Kevrekidis, Lu, Perdikaris, Wang, Yang) / 2021 / Nature Reviews Physics / position review / DOI 10.1038/s42254-021-00314-5 / https://www.nature.com/articles/s42254-021-00314-5 / ~8842 (Semantic Scholar)
- Scope: cross-domain physics-informed ML: fluids, mechanics, climate, engineering systems; data assimilation and discovery.
- Taxonomy: three paradigms — observational bias, inductive bias (PINNs), learning with physical constraints/hybrid models.
- Stated gaps/future directions: training difficulties, noise handling, theory; calls for hybrid physics-ML frameworks and software.
- Not covered (our judgment): pre-2021 field only; no bibliometrics; no application-industry depth; operator learning nascent.
- Verification: verified via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/s42254-021-00314-5

### G03
- Cuomo et al. (Cuomo, Schiano di Cola, Giampaolo, Rozza, Raissi, Piccialli) / 2022 / Journal of Scientific Computing / comprehensive review / DOI 10.1007/s10915-022-01939-z / https://link.springer.com/article/10.1007/s10915-022-01939-z / ~2857 (Semantic Scholar)
- Scope: scientific computing at large: forward/inverse problems, PDE solving, fluid dynamics, biomedical, engineering.
- Taxonomy: classification of PINN literature by problem type, methodological variant, application domain; challenge analysis.
- Stated gaps/future directions: missing benchmarks, weak software ecosystem, training pathologies, uncertainty quantification, theory.
- Not covered (our judgment): 2023-2026 advances (operator networks, adaptive training, LLM-era trends); industry survey angle.
- Verification: verified via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s10915-022-01939-z

### G04
- Willard et al. (Willard, Jia, Xu, Steinbach, Kumar) / 2022 / ACM Computing Surveys (55, article 160) / survey / DOI 10.1145/3514223 / https://dl.acm.org/doi/10.1145/3514223 / ~1352 (ACM DL "cited by", search snippet)
- Scope: physical, geospatial, and dynamical systems; theory-guided data science for engineering/earth science.
- Taxonomy: where physics enters ML pipeline — loss functions, hybrid model components, model design/architecture constraints.
- Stated gaps/future directions: generalization, scalability, integration of imperfect physics with sparse noisy data.
- Not covered (our judgment): predates most 2022-2026 PINN variants; light on operator learning and software; no metrics.
- Verification: verified: partial (ACM DL snippet + arXiv:2003.04919 cross-checked)

### G05
- Meng et al. (Meng, Guo, Li, Tan, Su, Li, Zhang, Shi, Xin) / 2025 / Machine Learning for Computational Science and Engineering (Springer) / survey / DOI 10.1007/s44379-025-00016-0 / https://link.springer.com/article/10.1007/s44379-025-00016-0 / ~309 (Semantic Scholar; 236 Crossref)
- Scope: broad PIML: forecasting, PDE solving, model predictive control, engineering applications.
- Taxonomy: fusion mode — physics-guided / physics-informed / physics-encoded; plus application-type organization.
- Stated gaps/future directions: unifying frameworks, large-scale/real-time use, hybridization with foundation models.
- Not covered (our judgment): thin on per-industry detail and failure-mode analysis; newer operator surveys postdate it.
- Verification: verified via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s44379-025-00016-0

### G06
- Faroughi et al. (Faroughi, Pawar, Fernandes, Raissi, Das, Kalantari, Mahjour) / 2024 / J. Computing and Information Science in Engineering (ASME) 24(4) / survey / DOI 10.1115/ (JCISE 24(4), exact suffix needs-check) / https://asmedigitalcollection.asme.org/computinginformationscience / n/a (S2 rate-limited)
- Scope: fluid and solid mechanics scientific computing.
- Taxonomy: physics-guided vs physics-informed vs physics-encoded neural networks AND neural operators.
- Stated gaps/future directions: accuracy/efficiency trade-offs, standardized datasets, hybrid operator-PINN methods.
- Not covered (our judgment): mechanics-centric; other physics domains and industries out of scope.
- Verification: verified: partial (Google Scholar profile + 2 search results confirm venue/year; DOI suffix unresolved)

### G07
- Hao et al. (Hao, Liu, Zhang, Ying, Feng, Su, Zhu) / 2022 / arXiv (preprint) / survey / arXiv 2211.09651 / https://arxiv.org/abs/2211.09651 / n/a
- Scope: broad PIML: problems, methods, applications (forecasting, PDEs, control).
- Taxonomy: problem-centric organization (tasks) x method families x applications.
- Stated gaps/future directions: unifying theory, benchmarking, coupling with foundation models.
- Not covered (our judgment): never journal-published to our knowledge; pre-2023 literature only.
- Verification: needs-check (S2/crossref 429; not re-confirmed this session)

### G08
- Grossmann et al. (Grossmann, Komorowska, Latz, Schoenlieb) / 2024 / IMA Journal of Applied Mathematics 89(1) / position/benchmark study / DOI 10.1093/imamat/hxae011 / https://academic.oup.com/imamat / ~197 (Crossref; ~411 per search snippet)
- Scope: PINNs vs finite element method on classical forward PDE benchmark problems (Poisson etc.).
- Taxonomy: empirical comparison protocol across problem difficulty, run time, accuracy.
- Stated gaps/future directions: PINNs not beating FEM for standard forward problems; potential in inverse/higher-dim/settings without solvers.
- Not covered (our judgment): no applications review; limited problem set; inverse-problem comparisons left open.
- Verification: verified via Crossref https://api.crossref.org/works (DOI 10.1093/imamat/hxae011)

### G09
- Kovachki et al. (Kovachki, Li, Azizzadenesheli, Burigede, Bhattacharya, Stuart, Anandkumar) / 2023 / J. Machine Learning Research 24(397) / comprehensive framework/survey / no DOI (JMLR; arXiv 2108.08481) / https://jmlr.org/papers/v24/21-1524.html / n/a
- Scope: neural operators as function-space mappings; theory, discretization convergence, applications across PDEs.
- Taxonomy: operator-learning architecture families (FNO, DeepONet, graph/attention operators) with approximation theory.
- Stated gaps/future directions: generalization guarantees, discretization invariance, data requirements.
- Not covered (our judgment): not PINN-loss centric; minimal industry/application mapping.
- Verification: verified: partial (AlphaXiv/search hit; JMLR metadata from prior knowledge, volume number needs-check)

### G10
- Liu et al. (Liu, Yang, Zhou, Lin, Liu, Meng et al.) / 2025 / Neurocomputing / comparative review / DOI 10.1016/j.neucom.2025.130518 / https://www.sciencedirect.com/science/article/pii/ (S2 record) / ~24 (Semantic Scholar)
- Scope: neural operator architectures for PDE/scientific computing tasks.
- Taxonomy: architecture families x variants x reported performance comparison.
- Stated gaps/future directions: lack of standardized benchmarks and fair comparisons across operators.
- Not covered (our judgment): operator learning only; no physics-loss PINN coverage.
- Verification: verified via https://api.semanticscholar.org/graph/v1/paper/search (DOI 10.1016/j.neucom.2025.130518)

### G11
- Subedi et al. (Subedi, et al.) / 2026 / Annual Review of Statistics and Its Application / review / DOI 10.1146/annurev-statistics-042424-070908 / https://www.annualreviews.org / ~3 (Crossref; ~26 per search snippet)
- Scope: operator learning from a statistical perspective: approximating infinite-dimensional mappings.
- Taxonomy: statistical estimation framework for operator learning; theory-first organization.
- Stated gaps/future directions: generalization theory, statistical guarantees for scientific ML.
- Not covered (our judgment): little applied/industry content; PINN training practice untouched.
- Verification: verified via Crossref https://api.crossref.org/works (DOI confirmed, year 2026)

### G12
- (First author not resolved) "Physics-Informed Neural Network (PINN) Evolution and Beyond: A Systematic Literature Review and Bibliometric Analysis" / 2022 / Big Data and Cognitive Computing 6(4):140 (MDPI) / systematic review + bibliometrics / DOI 10.3390/bdcc6040140 / https://www.mdpi.com/2504-2289/6/4/140 / ~271 (Crossref)
- Scope: whole PINN field meta-analysis: publication trends, top journals, authors, countries.
- Taxonomy: PRISMA-style systematic review + bibliometric clusters (evolution stages, hot topics).
- Stated gaps/future directions: fragmentation, need for theory and benchmarks; tracks growth trajectory.
- Not covered (our judgment): shallow on technical taxonomy; only 2019-2022 corpus.
- Verification: verified via Crossref https://api.crossref.org/works (DOI 10.3390/bdcc6040140)

### G13
- Ahmadi et al. (N. Ahmadi, et al.) / 2026 / Annual Review of Biomedical Engineering / review / DOI 10.1146/annurev-bioeng-110824-124907 / https://www.annualreviews.org/content/journals/10.1146/annurev-bioeng-110824-124907 / ~43 (search snippet)
- Scope: physics-informed ML in biomedical science (cross-cutting for health domain).
- Taxonomy: PIML paradigm applied to biomedical modeling, imaging, physiology.
- Stated gaps/future directions: data scarcity, validation, regulatory/clinical adoption barriers.
- Not covered (our judgment): biomedical only; included for positioning against domain scouts.
- Verification: verified: partial (annualreviews.org page + search snippet, "cited by 43")

## Venue metrics table
| Venue | Publisher | Metric | Value | Year | Source URL |
|---|---|---|---|---|---|
| Nature Reviews Physics | Springer Nature | Impact Factor | 44.8 | 2024 | https://icmab.es (secondary; partial) |
| Nature Machine Intelligence | Springer Nature | Impact Factor | 23.9 | 2024 | https://wos-journal.info (secondary; partial) |
| Journal of Computational Physics | Elsevier | Impact Factor | 3.8 | 2024 | studylib.net JCR-2024 ranking list (secondary; partial) |
| CMAME | Elsevier | n/a | n/a | n/a | publisher/Scimago bot-blocked (HTTP 403) |
| SIAM Review | SIAM | n/a | n/a | n/a | epubs.siam.org bot-blocked (HTTP 403) |
| Journal of Scientific Computing | Springer | n/a | n/a (aggregator conflict: ~1.3-3.3) | n/a | portalcientifico.upm.es (ambiguous columns) |
| Physics of Fluids | AIP | n/a | n/a (secondary conflict 4.1/4.3) | n/a | n/a |
| Applied Energy | Elsevier | n/a | n/a (secondary conflict 11.2/12.2) | n/a | n/a |
| ACM Computing Surveys | ACM | n/a | n/a | n/a | dl.acm.org bot-blocked |
| Artificial Intelligence Review | Springer | Impact Factor 13.9; 5-yr 14.9 | 13.9 / 14.9 | 2024 | https://www.springer.com/journal/10462 (verified) |

## Machine rows
G01|Physics-informed neural networks for PDE problems: a comprehensive review|2025|Artificial Intelligence Review|journal-review|10.1007/s10462-025-11322-7|250|meta/review|PINN forward/inverse PDE problems cross-domain|problem type x architecture x loss x training|survey|1|Y
G02|Physics-informed machine learning|2021|Nature Reviews Physics|position-review|10.1038/s42254-021-00314-5|8842|meta/review|cross-domain PIML fluids mechanics climate|observational bias / inductive bias / hybrid constraints|survey|2|Y
G03|Scientific Machine Learning Through Physics-Informed Neural Networks: Where we are and What's Next|2022|Journal of Scientific Computing|journal-review|10.1007/s10915-022-01939-z|2857|meta/review|SciML/PINNs in scientific computing broad|problem type x method variant x application|survey|1|Y
G04|Integrating Scientific Knowledge with Machine Learning for Engineering and Physical Systems|2022|ACM Computing Surveys|journal-review|10.1145/3514223|~1352|meta/review|physical geospatial dynamical systems|physics in loss / hybrid components / model design|survey|2|Y
G05|When physics meets machine learning: a survey of physics-informed machine learning|2025|Machine Learning for Computational Science and Engineering|journal-review|10.1007/s44379-025-00016-0|~309|meta/review|broad PIML forecasting control engineering|physics-guided / -informed / -encoded|survey|2|Y
G06|Physics-Guided, Physics-Informed, and Physics-Encoded Neural Networks and Operators in Scientific Computing: Fluid and Solid Mechanics|2024|J. Computing and Information Science in Engineering|journal-review|JCISE 24(4) DOI needs-check|n/a|meta/review|fluid and solid mechanics|guided / informed / encoded NNs and operators|survey|3|N
G07|Physics-Informed Machine Learning: A Survey on Problems, Methods and Applications|2022|arXiv|preprint-survey|arXiv 2211.09651|n/a|meta/review|broad PIML tasks and applications|problems x methods x applications|survey|3|N
G08|Can physics-informed neural networks beat the finite element method?|2024|IMA Journal of Applied Mathematics|position/benchmark|10.1093/imamat/hxae011|~197|meta/review|PINN vs FEM forward PDE benchmarks|empirical comparison protocol|survey|2|Y
G09|Neural Operator: Learning Maps Between Function Spaces|2023|J. Machine Learning Research|framework-survey|arXiv 2108.08481 JMLR 24(397)|n/a|meta/review|neural operators across PDEs|operator architecture families + theory|survey|3|N
G10|Architectures, variants, and performance of neural operators: A comparative review|2025|Neurocomputing|journal-review|10.1016/j.neucom.2025.130518|24|meta/review|neural operator architectures|architectures x variants x performance|survey|3|Y
G11|Operator Learning: A Statistical Perspective|2026|Annual Review of Statistics and Its Application|journal-review|10.1146/annurev-statistics-042424-070908|~3|meta/review|operator learning statistical theory|statistical estimation framework|survey|4|Y
G12|Physics-Informed Neural Network (PINN) Evolution and Beyond: A Systematic Literature Review and Bibliometric Analysis|2022|Big Data and Cognitive Computing|systematic-review/bibliometric|10.3390/bdcc6040140|271|meta/review|whole PINN field publication trends|PRISMA + bibliometric clusters|survey|4|Y
G13|Physics-Informed Machine Learning in Biomedical Science|2026|Annual Review of Biomedical Engineering|journal-review|10.1146/annurev-bioeng-110824-124907|~43|meta/review|biomedical PIML cross-cutting|PIML applied to biomedical modeling|survey|4|N

## Slice takeaways
- AIR (s10462) DOES have physics-informed coverage beyond Luo 2025: a 2026 methods paper "Physics-Informed Symbolic Regression Ensemble (PISRE)" (Vilas Boas Pappi Maciel et al., 2026, verified: partial); but Luo 2025 remains the ONLY AIR review, and its scope is PDE-problem methods, not industry applications.
- Field is saturated with method-centric reviews (Karniadakis 2021, Cuomo 2022, Willard 2022, Meng 2025, Luo 2025) all organized around HOW physics enters the model (observational/inductive bias; guided/informed/encoded) and all flagging the same gaps: theory, benchmarks, UQ, training reliability.
- Clearest gap for a new AIR submission: a cross-industry, application-oriented meta-survey mapping WHO uses PINNs/PIML, WHICH physics they enforce, and WHICH components/architectures (incl. operator learning + benchmark reality checks like Grossmann 2024) — none of the 13 verified reviews does the industry/component mapping; operator learning is covered only in separate non-PINN surveys (Kovachki 2023, Liu 2025, Subedi 2026) never integrated with PINN reviews.
- Bibliometric grounding exists (MDCC 2022, only 2019-2022 corpus) but is stale — a 2026 bibliometric + review-synthesis chapter is open space.
- Venue-metric caveat: only AIR (IF 13.9/5yr 14.9, 2024) was publisher-verified; NRP/NMI/JCP values are secondary-source (partial); CMAME/SIAM Review/Physics of Fluids/Applied Energy/ACM CSUR/JSC marked n/a due to bot-walls (Scimago, ACM, SIAM, Elsevier all returned 403) — do not cite the partial numbers without re-checking JCR.
