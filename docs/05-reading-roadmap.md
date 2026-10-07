# Reading Roadmap — Ranked Order for a Solo Reviewer

**Basis:** priority scores from the verified inventory (92+ papers); citation mass;
component coverage; domain exemplarity; recency. Refresh after slices F/G land.

## How papers were ranked

| Criterion | Weight | Question it answers |
|---|---|---|
| Foundationalness | 40% | Do later works build on it? (field-citation mass) |
| Component coverage | 25% | Does it define a loss/architecture/enforcement component in our taxonomy? |
| Domain exemplarity | 20% | Is it the cleanest industry example of its pattern? |
| Recency | 10% | Does it carry the 2025–2026 frontier? |
| Accessibility | 5% | Can a solo reader absorb it without a supervisor? |

## The 4-week plan (part-time, ~2–3 h/day)

### Week 1 — The spine: what a PINN is and why it fails

Read **in this order**, in full, with notes:

| # | ID | Paper | Why now | Est. |
|---|---|---|---|---|
| 1 | PINN-A01 | Raissi et al. 2019, *J. Comput. Phys.* (the original, ~21k cites) | the definition of everything | 2.5 h |
| 2 | PINN-G01 | Karniadakis et al. 2021, *Nature Reviews Physics* "Physics-informed machine learning" (slice G) | the field's own framing | 2 h |
| 3 | PINN-A03 | Krishnapriyan et al., NeurIPS 2021 — failure modes | why vanilla training breaks | 2 h |
| 4 | PINN-A04 | Wang et al., SIAM JSC 2021 — gradient pathologies (= slice B record) | the weighting problem, stated | 2 h |
| 5 | PINN-A06 | Wang et al. 2022, *JCP* — NTK perspective on training failure | the diagnosis tool | 2.5 h |
| 6 | PINN-A07 | McClenny & Braga-Neto 2023, *JCP* — self-adaptive PINNs | the standard fix | 2 h |
| 7 | PINN-C02 | PINNs for fluid mechanics review, *Acta Mech. Sin.* 2021 | first domain synthesis + reading map | 1.5 h |

### Week 2 — Architectures and the operator-learning branch

| # | ID | Paper | Depth |
|---|---|---|---|
| 8 | PINN-B12 | DeepONet, *Nature MI* 2021 | must-read |
| 9 | PINN-B13 | FNO, ICLR 2021 | must-read |
| 10 | PINN-B14 | Physics-informed DeepONet, *Science Advances* 2021 | must-read |
| 11 | PINN-B15 | PINO 2024 | careful |
| 12 | PINN-B01 | SIREN, NeurIPS 2020 | careful (architectures) |
| 13 | PINN-B09 | FBPINNs 2023 | careful |
| 14 | PINN-B07 (+B06) | XPINN 2020 (cPINN alongside) | methods+results |
| 15 | PINN-B19 | B-PINNs (UQ), *JCP* 2021 | careful |

### Week 3 — Domain exemplars (methods + results)

| # | ID | Paper | Domain signal |
|---|---|---|---|
| 16 | PINN-C01 | Hidden fluid mechanics, *Science* 2020 | fluids from video data |
| 17 | PINN-C04 | RANS PINNs, *Phys. Fluids* 2022 | turbulence without a model |
| 18 | PINN-C11 | Airfoil PDE-constrained optimization, CMAME 2023 | design loops |
| 19 | PINN-C12 | Conjugate heat transfer, ICHMT 2024 | electronics cooling (industry) |
| 20 | PINN-D01 | PINNs for power systems (IEEE PES) | grid dynamics entry point |
| 21 | PINN-D02 | AC-OPF PINNs, EPSR 2022 | optimization class |
| 22 | PINN-D06 | PINN4SOH, *Nature Comms* 2024 | battery industry benchmark |
| 23 | PINN-D16 | Beucler et al., *PRL* 2021 — analytic constraints | hard constraints done right |
| 24 | PINN-D17 | NeuralGCM, *Nature* 2024 | hybrid beyond classic PINN (read critically) |
| 25 | PINN-E01 | SciANN solid mechanics, CMAME 2021 | elasticity + framework |
| 26 | PINN-E02 | Seismic FWI PINNs, *JGR* 2022 | geoscience inverse |
| 27 | PINN-E05 | EP-PINNs cardiac, *Front. Cardiovasc. Med.* 2022 | clinical inverse pattern |
| 28 | PINN-E08 | Glioblastoma infiltration, *MedIA* 2025 | single-patient personalization |

### Week 4 — Positioning, reliability, frontier

| # | ID | Paper | Purpose |
|---|---|---|---|
| 29 | PINN-A17 | Luo et al. 2025, *Artificial Intelligence Review* — comprehensive PINN review | **the review to differentiate from** — read its taxonomy and gaps |
| 30 | PINN-A15 | Acta Numerica 2024 numerical analysis of PIML | theory synthesis |
| 31 | PINN-A13 | "Can PINNs beat FEM?", IMA JAM 2024 | the honest reliability claim |
| 32 | PINN-A11 | PINNacle benchmark | evaluation practice |
| 33 | PINN-A10 | Expert's guide to training PINNs | practical defaults |
| 34 | PINN-B18 | Poseidon, NeurIPS 2024 | PDE foundation models |
| 35 | PINN-B17/B20 | Transolver / Transolver++ | million-scale industrial meshes |
| 36 | PINN-B21 | Physics-informed diffusion models, ICLR 2025 | frontier |
| 37 | slice G reviews (Karniadakis aside) + slice F picks | positioning pass | skim protocol |

## The 15-minute skim protocol (weeks 3–4)

For every non-must-read paper: abstract → figures 1–2 → find the loss equation → check
the evaluation table → last paragraph. Record one line in the inventory CSV. If a paper
fails to yield its physics equations and enforcement mechanism in 15 minutes, its entry
stays at "reference" priority.

## If you only read 10 papers

1. PINN-A01 (Raissi 2019) — the definition
2. PINN-A03 (failure modes) — the training reality
3. PINN-A06 (NTK diagnosis) — why, not just what
4. PINN-B12 (DeepONet) — the operator turn
5. PINN-B13 (FNO) — the operator turn, spectral
6. PINN-B14 (PI-DeepONet) — physics meets operators
7. PINN-C01 (Hidden fluid mechanics) — the showcase inverse result
8. PINN-D16 (Beucler PRL) — hard constraints done properly
9. PINN-D06 (PINN4SOH) — what industrial traction looks like
10. PINN-A17 (Luo 2025 AIR review) — the conversation we are joining
