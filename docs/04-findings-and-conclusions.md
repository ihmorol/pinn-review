# Findings & Conclusions

**Status:** synthesized from slices A–E (92 verified papers, snapshot 2026-10-06/07);
slice F (materials/manufacturing/finance) and slice G (survey landscape) slots are marked
*pending* where their data is load-bearing. Companion: `figures/fig1..fig6`.

## 1. Answering the research questions

### RQ1 — Who uses PINNs, and for which problem classes?

Five adoption tiers emerged from the corpus:

| Tier | Sectors (evidence in corpus) | Dominant problem class |
|---|---|---|
| Research-grade, broad | fluid mechanics, heat transfer (Physics of Fluids, JCP, J. Heat Transfer) | forward + inverse benchmarks |
| Strong applied traction | oil & gas (seismic FWI, porous flow, gas-lift wells), energy/batteries (BMS, SOH), aerospace (DLR transonic airfoils, turbine-cascade rig data, flight-test system ID) | inverse & parameter identification |
| Emerging industrial pilots | clinical (npj Digital Medicine Windkessel wearables, N=29 humans; glioblastoma infiltration), construction (shield tunnelling), electronics cooling (IGBT modules), nuclear reactor twins | inverse, digital-twin framing |
| Real-time / deployment-oriented | acoustics (DeepONet, PNAS), power grids (AC-OPF), million-scale meshes (Transolver++, ICML 2025) | operator learning, control |
| Aspirational | "digital twin" framing across sectors; automotive aerodynamics | — (no peer-reviewed deployment report found) |

**Inversion is the industrial sweet spot.** Across all domain slices, the single most
common industrial pattern is: sparse/experimental sensors + PDE residual → recover hidden
fields or parameters (cardiac activation maps, battery degradation states, seismic
velocity, aerodynamic coefficients, turbine heat loads). Pure forward simulation against
mature numerical solvers remains mostly academic — consistent with the benchmark finding
that FEM still wins on standard 2D problems in both accuracy and wall-clock time.

### RQ2 — What components do recent works converge on?

- **Architecture:** vanilla MLP → *modified MLP* (per-layer input transforms), *random/
  learned Fourier features* and *SIREN* activations to defeat spectral bias; the
  fastest-cited branch is operator networks (DeepONet ~4.7k cites, FNO ~5.1k) with a
  transformer-operator lineage (Galerkin Transformer → OFormer → GNOT → Transolver →
  Transolver++) now targeting million-scale industrial geometries.
- **Loss weighting:** fixed weights → adaptive schemes: learning-rate annealing, NTK-based
  weighting, gradient-norm balancing, per-point *self-adaptive attention*, and balanced
  residual-decRate weights (JCP 2025). Adaptive weighting is now standard practice in
  2023+ methodology papers.
- **Sampling:** uniform collocation → residual-based adaptive refinement (RAD/RAR family);
  a 2023 CMAME comparative study is the reference point.
- **Training schedule:** Adam-then-L-BFGS two-stage is the community backbone ("Expert's
  guide", jaxpi); curriculum and *causal training* address stiff/chaotic dynamics.
- **Software:** DeepXDE (SIAM Review), jaxpi, NVIDIA Modulus/PhysicsNeMo, SciANN;
  benchmarks PINNacle, PDEBench, PDEArena.

### RQ3 — What physics is enforced, and how?

| Domain group | Physics typically enforced | Enforcement seen |
|---|---|---|
| Fluids & aero | incompressible/compressible NSE, RANS, Euler, energy eq. | soft residual; hard BCs + distance-function inputs at high Re; artificial dissipation for shocks; divergence-free variants |
| Thermal | conduction/convection/radiation, conjugate HT | soft residual; engineering correlations as enforced laws (film-cooling superposition) |
| Power & energy | power-flow/Kirchhoff, swing equations, AC-OPF constraints | soft penalty → **hard constraints via projection layers (KCLNet, 2025)** |
| Batteries | P2D/Doyle–Fuller–Newman PDEs, Butler–Volmer, degradation state-space laws | soft residual; hybrid empirical+physics (PINN4SOH, Nature Comms) |
| Nuclear | point-kinetics ODEs (reactor dynamics) | soft penalty + transfer learning |
| Climate | conservation laws (mass/energy), parameterization constraints | **hard conservative layers (Beucler, PRL)**; hybrid physics-core + learned closure (NeuralGCM, Nature — beyond classic PINN) |
| Biomed | Monodomain + ionic models, Eikonal, reduced-order hemodynamics, reaction–diffusion tumor, Windkessel ODEs | soft residual; ROM-PINN hybrids; energy-functional loss; meta-learning |
| Geoscience | acoustic/elastic wave equations, Biot poroelasticity, Richards equation | soft residual; **monotonicity-constrained outputs** |
| Civil | linear elasticity, nonlinear MDOF dynamics, soil–structure models | soft residual, autodiff |
| Finance | Black–Scholes, HJB | weak/variational & deep Galerkin line (pending slice F refresh) |
| Materials/mfg | phase-field fracture, Allen–Cahn/Cahn–Hilliard, melt-pool transport (pending slice F refresh) | transfer-learning-enhanced soft residual |

Mechanism distribution across the corpus is plotted in `fig3_mechanism_bar.png` and
cross-tabulated against domains in `fig2_domain_mechanism.png`. Soft residual penalties
remain the universal default; **hard constraints are the clearest 2024–2026 trend**;
weak/variational forms persist for low-regularity and high-dimensional PDEs; operator-side
enforcement grows with operator learning's citation dominance.

### RQ4 — What do the existing reviews cover, and what's our gap?

*Pending slice G final numbers.* Load-bearing fact already verified: **the target journal
itself published a comprehensive PINN review in July 2025** — Luo et al., "Physics-informed
neural networks for PDE problems: a comprehensive review", *Artificial Intelligence Review*
(DOI:10.1007/s10462-025-11322-7, ~358 cites). A 2026 critical review of PINNs in
computational mechanics also exists (Arch. Comput. Methods Eng.). Our positioning must
therefore be: (i) **cross-industry comparative** (their scope is generic PDE problems),
(ii) **component-level methodology tables** (physics × mechanism × problem-class × evidence),
(iii) **adoption/reliability synthesis** including the sobering theory results, and
(iv) 2025–2026 currency (foundation-model operators, hard-constraint trend, physics-informed
diffusion).

## 2. Cross-cutting synthesis

1. **Two research programs, one label.** "Physics-informed" now covers (a) pointwise
   PDE-solving PINNs (Raissi lineage) and (b) operator learning with physics constraints
   (DeepONet/FNO lineage). Citation mass is shifting decisively to (b); industrial
   real-time use cases cluster there too. Surveys that blend them blur the field's most
   important distinction — we keep it explicit.
2. **The training problem is the field's central technical story.** Failure modes
   (Krishnapriyan 2021), gradient pathologies (Wang et al. 2021), NTK diagnosis (Wang et
   al. 2022), self-adaptive attention (2023), causality (2024), balanced decay (2025):
   five years of steady, cumulative work — mostly on soft-penalty training. A reader
   should come away knowing *why* vanilla PINNs fail and which fixes are standard.
3. **Theory is honest but sobering.** A posteriori error bounds exist (Mishra & Molinaro;
   De Ryck et al.; Acta Numerica 2024); a 2025 Bernoulli result shows the plain PINN loss
   is not risk-consistent without ridge regularization; benchmark studies find no universal
   winner and FEM ahead on standard problems. The honest industry claim is *inverse
   problems and hybrid data assimilation*, not "replaces FEM".
4. **Hard constraints are moving from trick to trend.** Divergence-free constructions and
   output transforms (2021–22) → conservative climate layers (2021) → KCL projections for
   power flow (2025) → monotonicity constraints in hydrology. Architectural enforcement
   trades flexibility for guaranteed physical consistency — a structural shift worth a
   dedicated manuscript section.
5. **Domain transfer happens through physics, not code.** The same soft-penalty loop is
   re-instantiated per sector with sector-specific equations and data regimes; what
   transfers between sectors is the *training methodology* (weighting, sampling,
   scheduling) — which argues for organizing a survey by components, not by domain. We do
   both (taxonomy axis + domain tables).

## 3. Open problems worth stating in the manuscript

- Convergence/risk-consistency of the practical loss (post-Bernoulli-2025 agenda).
- Stiff, multi-scale, and chaotic systems at scale (causal training, spectral methods).
- Hard-constraint design theory (when do projections hurt accuracy?).
- UQ beyond B-PINN-style posteriors for industrial certification.
- Standardized industrial reporting: almost no peer-reviewed deployment studies with
  ablations against production numerics.
- Physics-informed foundation models: residual fine-tuning as the new enforcement site.

## 4. Limitations of this dossier

- Citation counts are approximate (S2/GS snapshots, 2026-10-06/07) — fine for ranking
  reading order, not for quoting in the manuscript (re-verify at submission).
- Retrieval was web-only (no Scopus/WoS bibliometrics); selection favors English-language,
  high-visibility venues.
- 2026 corpus is partial (year in progress).
- Slice E verification notes: one widely-repeated attribution ("Friha et al." healthcare
  PINN survey) could not be verified and was excluded — do not cite it from memory.
