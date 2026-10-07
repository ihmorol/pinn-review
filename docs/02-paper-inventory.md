# Master Paper Inventory

**Machine-generated** from `data/paper-inventory.csv` (run `python scripts/gen_inventory_md.py`
to refresh). Citation counts are approximate snapshots (Semantic Scholar / Google Scholar,
2026-10-06/07) and drift; "Read" gives the recommended reading depth (1=must-read ... 5=reference).
Every entry was verified against its publisher page or the Semantic Scholar API — see
`docs/01-search-protocol-and-log.md`.

## Corpus at a glance

| Metric | Value |
|---|---|
| Unique verified papers | 92 |
| Journal / conference / preprint | 73 / 14 / 5 |
| Year distribution | 2018: 1, 2019: 1, 2020: 7, 2021: 16, 2022: 12, 2023: 11, 2024: 18, 2025: 18, 2026: 8 |
| Distinct venues | 64 |
| Cross-slice papers (surfaced by 2+ scouts) | 2 |

## 1. Foundations, theory & training methodology (slice A)

| ID | Paper | Year | Venue | Type | Cites | Read |
|---|---|---|---|---|---|---|
| PINN-A01 | **Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations** | 2019 | Journal of Computational Physics | journal | ~20971 (S2 2026-10-06) | must-read |
| PINN-A03 | **Characterizing possible failure modes in physics-informed neural networks** | 2021 | NeurIPS 2021 | conference | ~2114 (GS-snippet) | must-read |
| PINN-A04 | **Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks** | 2021 | SIAM Journal on Scientific Computing | journal | ~425 (GS-snippet estimate) | must-read |
| PINN-A06 | **When and why PINNs fail to train: A neural tangent kernel perspective** | 2022 | Journal of Computational Physics | journal | ~1880 (S2 2026-10-06) | must-read |
| PINN-A07 | **Self-adaptive physics-informed neural networks** | 2023 | Journal of Computational Physics | journal | ~1300 (GS-snippet estimate) | must-read |
| PINN-A10 | **An Expert's Guide to Training Physics-informed Neural Networks** | 2023 | arXiv (jaxpi library) | preprint | n/a | must-read |
| PINN-A15 | **Numerical analysis of physics-informed neural networks and related models in physics-informed machine learning** | 2024 | Acta Numerica | journal | ~167 (GS-snippet) | must-read |
| PINN-A17 | **Physics-informed neural networks for PDE problems: a comprehensive review** | 2025 | Artificial Intelligence Review | journal | ~358 (GS-snippet) | must-read |
| PINN-A02 | **Estimates on the generalization error of physics-informed neural networks for approximating PDEs** | 2022 | IMA Journal of Numerical Analysis | journal | n/a | careful |
| PINN-A05 | **On the eigenvector bias of Fourier feature networks: From regression to solving multi-scale PDEs with physics-informed neural networks** | 2021 | Computer Methods in Applied Mechanics and Engineering | journal | ~864 (S2) | careful |
| PINN-A08 | **A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks** | 2023 | Computer Methods in Applied Mechanics and Engineering | journal | ~1142 (GS-snippet) | careful |
| PINN-A09 | **DeepXDE: A Deep Learning Library for Solving Differential Equations** | 2021 | SIAM Review | journal | ~3835 (GS-snippet) | careful |
| PINN-A11 | **PINNacle: A Comprehensive Benchmark of Physics-Informed Neural Networks for Solving PDEs** | 2023 | NeurIPS 2024 Datasets and Benchmarks (arXiv 2023) | conference | n/a | careful |
| PINN-A13 | **Can physics-informed neural networks beat the finite element method?** | 2024 | IMA Journal of Applied Mathematics | journal | n/a | careful |
| PINN-A16 | **Respecting causality for training physics-informed neural networks** | 2024 | Computer Methods in Applied Mechanics and Engineering | journal | n/a | careful |
| PINN-A19 | **Self-adaptive weights based on balanced residual decay rate for physics-informed neural networks and deep operator networks** | 2025 | Journal of Computational Physics | journal | n/a | careful |
| PINN-A12 | **PDEBENCH: An Extensive Benchmark for Scientific Machine Learning** | 2022 | NeurIPS 2022 Datasets and Benchmarks | conference | n/a | methods+results |
| PINN-A14 | **Generic bounds on the approximation error for physics-informed (and) operator learning** | 2022 | NeurIPS 2022 | conference | ~132 (GS-snippet) | methods+results |
| PINN-A18 | **On the convergence of PINNs** | 2025 | Bernoulli | journal | n/a | methods+results |
| PINN-A20 | **Physics-Informed Neural Networks in Computational Mechanics: A Critical Review of Stability, Generalization, and Multi-Scale Applications** | 2026 | Archives of Computational Methods in Engineering | journal | n/a | skim |

## 2. Architectures, enforcement variants & operator learning (slice B)

| ID | Paper | Year | Venue | Type | Cites | Read |
|---|---|---|---|---|---|---|
| PINN-B12 | **Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators** | 2021 | Nature Machine Intelligence | journal | ~4708 (S2) | must-read |
| PINN-B13 | **Fourier Neural Operator for Parametric Partial Differential Equations** | 2021 | International Conference on Learning Representations | conference | ~5063 (S2) | must-read |
| PINN-B14 | **Learning the solution operator of parametric partial differential equations with physics-informed DeepONets** | 2021 | Science Advances | journal | ~1246 (S2) | must-read |
| PINN-B15 | **Physics-Informed Neural Operator for Learning Partial Differential Equations (PINO)** | 2024 | ACM/IMS Journal of Data Science | journal | ~194 (Crossref) | must-read |
| PINN-B05 | **Self-Adaptive Physics-Informed Neural Networks using a Soft Attention Mechanism** | 2023 | Journal of Computational Physics | journal | ~866 (S2) | careful |
| PINN-B06 | **Conservative physics-informed neural networks on discrete domains for conservation laws (cPINN)** | 2020 | Computer Methods in Applied Mechanics and Engineering | journal | ~1277 (S2) | careful |
| PINN-B09 | **Finite basis physics-informed neural networks (FBPINNs): a scalable domain decomposition approach for solving differential equations** | 2023 | Advances in Computational Mathematics | journal | ~321 (Crossref) | careful |
| PINN-B17 | **Transolver: A Fast Transformer Solver for PDEs on General Geometries** | 2024 | International Conference on Machine Learning | conference | ~408 (S2) | careful |
| PINN-B18 | **Poseidon: Efficient Foundation Models for PDEs** | 2024 | NeurIPS | conference | ~232 (S2) | careful |
| PINN-B19 | **B-PINNs: Bayesian Physics-Informed Neural Networks for Forward and Inverse PDE Problems with Noisy Data** | 2021 | Journal of Computational Physics | journal | ~1259 (S2) | careful |
| PINN-B01 | **Implicit Neural Representations with Periodic Activation Functions (SIREN)** | 2020 | NeurIPS | conference | ~3998 (S2) | methods+results |
| PINN-B02 | **The Deep Ritz Method: A Deep Learning-Based Numerical Algorithm for Solving Variational Problems** | 2018 | Communications in Mathematics and Statistics | journal | ~2018 (S2) | methods+results |
| PINN-B07 | **Extended Physics-Informed Neural Networks (XPINNs): A Generalized Space-Time Domain Decomposition based Deep Learning Framework for Nonlinear PDEs** | 2020 | Communications in Computational Physics | journal | ~1215 (S2) | methods+results |
| PINN-B08 | **hp-VPINNs: Variational Physics-Informed Neural Networks With Domain Decomposition** | 2021 | Computer Methods in Applied Mechanics and Engineering | journal | ~917 (S2) | methods+results |
| PINN-B10 | **Multilevel domain decomposition-based architectures for physics-informed neural networks** | 2024 | Computer Methods in Applied Mechanics and Engineering | journal | ~120 (S2) | methods+results |
| PINN-B11 | **Weak Adversarial Networks for High-dimensional Partial Differential Equations** | 2020 | Journal of Computational Physics | journal | ~570 (S2) | methods+results |
| PINN-B16 | **GNOT: A General Neural Operator Transformer for Operator Learning** | 2023 | International Conference on Machine Learning | conference | ~496 (S2) | methods+results |
| PINN-B20 | **Transolver++: An Accurate Neural Solver for PDEs on Million-Scale Geometries** | 2025 | International Conference on Machine Learning | conference | n/a | methods+results |
| PINN-B21 | **Physics-Informed Diffusion Models** | 2025 | International Conference on Learning Representations | conference | n/a | methods+results |
| PINN-B22 | **From Theory to Application: A Practical Introduction to Neural Operators in Scientific Computing** | 2025 | arXiv preprint | preprint | ~15 (search snippet) | skim |
| PINN-B23 | **Large language models for partial differential equation workflows** | 2026 | arXiv preprint | preprint | n/a | skim |

## 3. Fluid mechanics, aerospace & thermal applications (slice C)

| ID | Domain | Physics enforced | Mechanism | Problem | Cites | Read |
|---|---|---|---|---|---|---|
| PINN-C01 | Fluid/incompressible flow reconstruction from imaging | Incompressible NSE + passive-scalar advection | Divergence-free velocity ansatz (hard) + soft momentum residuals | inverse | ~2198 | must-read |
| PINN-C02 | Fluid mechanics review (incompressible/compressible/biomedical) | Incompressible and compressible NSE (surveyed) | Soft residual (surveyed) | review | ~2220 | must-read |
| PINN-C03 | Thermal engineering review (conduction/convection/radiation) | Heat equation + convection-diffusion + radiation + coupled NSE-energy | Soft residual via autodiff (surveyed) | review | ~1393 | must-read |
| PINN-C04 | Turbulence/RANS closure-free reconstruction (CFD) | Incompressible RANS + continuity without turbulence model | Soft residual | forward | ~469 | must-read |
| PINN-C05 | CFD forward solver benchmark | Incompressible NSE with periodic BC | Soft residual (direct and divergence-free variants) | forward | ~1115 | careful |
| PINN-C06 | Aerospace external aerodynamics (DLR) transonic airfoil | Compressible Euler equations | Soft residual + artificial dissipation for shocks | forward | ~9 | careful |
| PINN-C08 | Aerospace flight dynamics/system identification from flight test | Six-DOF equations of motion with aerodynamic model | Soft residual + trajectory/parameter networks | inverse | ~6 | careful |
| PINN-C11 | Aerospace airfoil shape optimization (adjoint-free) | Navier-Stokes equations across design space | Soft residual + autodiff L-BFGS optimization | control | ~127 | careful |
| PINN-C12 | Electronics cooling (automotive power electronics IGBT) | Conjugate heat transfer: flow + energy with solid-fluid coupling | Soft residual | forward | ~39 | careful |
| PINN-C13 | Thermal engineering review (2026 currency anchor) | Conduction + convection + radiation + coupled multiphysics | Soft residual and constraint variants (surveyed) | review | ~1 | careful |
| PINN-C07 | Gas turbine turbomachinery (NASA/Ohio State) transonic cascade | Transonic cascade flow governing equations (2-D compressible) | Soft residual in forward/data-assimilation/inverse modes | both | ~3 | methods+results |
| PINN-C09 | Aerospace aerodynamic parameter ID for flight simulation | Six-DOF motion equations (longitudinal case) | Soft residual with parameters as trainable variables | inverse | ~20 | methods+results |
| PINN-C10 | Aerospace high-Re transonic external flow | RANS and Euler equations | Hard BC output layer + distance-function inputs + gradient weighting | both | ~46 | methods+results |
| PINN-C14 | Aero-engine internal air system thermal (gas turbine industry) | Heat conduction equation in rotating cavity walls | Soft residual; experimental-input inverse mapping | inverse | ~13 | methods+results |
| PINN-C15 | Aero-engine film cooling (nozzle/turbine thermal protection) | Sellers superposition law for film-cooling effectiveness | Hybrid physics-correlation + Fourier/attention residual branch | forward | ~18 | methods+results |
| PINN-C16 | Porous media flow (oil and gas reservoir engineering) | Mass conservation + Darcy law (single-phase) | Soft residual + sparse observation assimilation | forward | ~257 | methods+results |
| PINN-C17 | Pore-scale porous flow (subsurface/petrophysics) | Steady Stokes flow in pore spaces | Soft residual on point clouds (physics-informed PointNet) | forward | ~53 | methods+results |
| PINN-C18 | Acoustics for VR/game audio and spatial computing industry | Linear acoustic wave equation | Operator surrogate (DeepONet) | operator | ~37 | skim |

## 4. Energy, power systems, batteries & climate (slice D)

| ID | Domain | Physics enforced | Mechanism | Problem | Cites | Read |
|---|---|---|---|---|---|---|
| PINN-D01 | energy/power - grid dynamics | swing equation (rotor angle/frequency dynamics) and steady-state power-system models | soft-penalty | both | ~570 (GS)/243 Crossref | must-read |
| PINN-D05 | energy/power - dedicated survey | power-flow equations; swing dynamics; transients (reviewed) | mixed (survey) | both | ~7 | must-read |
| PINN-D06 | battery - BMS/SOH prognosis | empirical degradation model plus state-space dynamics; monotonic capacity fade | hybrid (physics model integrated with NN loss) | forecasting | ~897 | must-read |
| PINN-D16 | climate - parameterization emulation | mass (water) and radiative energy conservation laws | hard-constraint (conservative layers) compared to soft-penalty | operator | ~400 (S2)/~600 GS | must-read |
| PINN-D17 | climate/weather - hybrid emulator | atmospheric dynamics solved by differentiable physics core; learned subgrid closures | hybrid (physics solver plus learned components; NOT classic PINN) | operator | ~605 | must-read |
| PINN-D18 | renewables/energy - sector survey | grid; wind; PV radiative; storage physics (reviewed) | mixed (survey) | both | ~46 | must-read |
| PINN-D02 | energy/power - AC-OPF | AC power-flow equations (Kirchhoff/power balance) | soft-penalty | control | ~163 | careful |
| PINN-D07 | battery - SOH estimation | P2D Doyle-Fuller-Newman PDEs (concentration/potential transport) | soft-penalty | inverse | ~104 | careful |
| PINN-D08 | battery - electrochemistry | full P2D PDEs incl. Butler-Volmer kinetics | soft-penalty (PDE collocation) | both | ~13 | careful |
| PINN-D10 | buildings/HVAC - demand response | building heat-balance dynamics (RC thermal-network ODEs) | soft-penalty | control | ~196 | careful |
| PINN-D11 | buildings/HVAC - survey | heat transfer; HVAC component physics; thermodynamics (reviewed) | mixed (survey) | both | ~96 | careful |
| PINN-D19 | energy sector - cross-sector survey | power-flow; electrochemical; thermodynamic laws (reviewed) | mixed (survey) | both | ~3 | careful |
| PINN-D03 | energy/power - state estimation | power-flow and network admittance physics | hybrid (physics-informed loss plus measurement model) | inverse | n/a | methods+results |
| PINN-D04 | energy/power - power flow | Kirchhoff's Current Law at every bus | hard-constraint (hyperplane projection in GNN) | forward | n/a | methods+results |
| PINN-D09 | battery - parameter inference | SPM/P2D electrochemical PDEs | soft-penalty | inverse | ~20 | methods+results |
| PINN-D12 | nuclear - reactor dynamics | point kinetics ODEs (neutron density plus 6 delayed precursor groups) | soft-penalty (ELM-based) | forward | ~57 | methods+results |
| PINN-D13 | nuclear - reactor dynamics/digital twin | point kinetics reactor-transfer ODE dynamics | soft-penalty plus transfer learning | forward | ~92 | methods+results |
| PINN-D14 | renewables - wind speed forecasting | wind-speed physical constraints (bounds and evolution regularities) | hybrid (KAN backbone plus constraint loss) | forecasting | ~3 | skim |
| PINN-D15 | renewables - 3D wind fields | physical consistency of wind evolution (advection-type) | hybrid (physics-guided loss with uncertainty) | forecasting | ~0 | skim |

## 5. Biomedical, geoscience & civil applications (slice E)

| ID | Domain | Physics enforced | Mechanism | Problem | Cites | Read |
|---|---|---|---|---|---|---|
| PINN-E01 | Civil/solid mechanics (construction) | Linear elasticity equilibrium with heterogeneous modulus | autodiff PDE residual + data loss (SciANN) | both | ~1253 (S2) | must-read |
| PINN-E02 | Geoscience/seismic (oil-gas exploration) | Acoustic + elastic wave equations | cCNN autodiff wave residual + seismogram data | both | ~412 (Crossref) | must-read |
| PINN-E05 | Biomedical/cardiac EP (hospital) | Monodomain + Aliev-Panfilov ionic model | autodiff PDE residual + sparse Vm data | inverse | ~57 (Crossref) | must-read |
| PINN-E08 | Biomedical/oncology (hospital) | Reaction-diffusion tumor-invasion PDE | autodiff PDE residual + single-3D-MRI data | inverse | ~33 (Crossref) | must-read |
| PINN-E03 | Geoscience/subsurface flow (oil-gas) | Nonlinear diffusivity + Biot poroelasticity | autodiff PDE residual vs FEM baseline | both | ~118 (Crossref) | careful |
| PINN-E04 | Hydrology/groundwater (agri-environmental) | Richardson-Richards unsaturated flow | monotonicity-constrained output + PDE residual | inverse | ~126 (Crossref) | careful |
| PINN-E06 | Biomedical/cardiac imaging (hospital MRI) | Hyperelastic anisotropic energy potential | energy-functional loss + RBF output subspace | inverse | ~89 (Crossref) | careful |
| PINN-E07 | Biomedical/cerebrovascular hemodynamics (hospital) | 1D reduced-order blood-flow model | ROM-PINN hybrid + sparse TCD data | inverse | ~126 (Crossref) | careful |
| PINN-E09 | Biomedical/healthcare survey | n/a survey of embedded PDE-ODE constraints | n/a categorizes residual-loss/hybrid/operator approaches | survey | ~10 (Crossref) | careful |
| PINN-E10 | Biomedical/cardiac digital twins (pre-clinical) | Eikonal equation | meta-trained PINN fast CV-field inference | operator | ~1 (Crossref) | careful |
| PINN-E11 | Biomedical/cardiovascular wearables (clinical pilot) | 2- and 3-element Windkessel ODEs | ODE residual + wearable bioimpedance data | inverse | ~1 (Crossref) | careful |
| PINN-E12 | Oil-gas/production control (industrial) | Gas-lift well dynamic ODE model | PINC ODE residual + MPC coupling | both | ~27 (Crossref) | methods+results |
| PINN-E14 | Civil/SHM bridges | Nonlinear MDOF spring equations of motion | EOM residual + measured response data | inverse | ~37 (Crossref) | methods+results |
| PINN-E13 | Construction/geotech tunneling | Segmental-lining uplift soil-structure mechanics | PDE residual on lining-uplift model | both | ~13 (Crossref) | skim |

## 6. Materials, manufacturing, finance & industrial ecosystem (slice F)

_Slice F pending._

## 7. Existing reviews & meta-landscape (slice G)

_Slice G pending._


## Reading-depth legend

| Priority | Meaning |
|---|---|
| must-read | read in full, take notes; these anchor the manuscript |
| careful | read thoroughly; cite for component claims |
| methods+results | read method + evaluation sections; skim the rest |
| skim | abstract + figures; cite for breadth |
| reference | lookup citation only |

Full per-paper detail (architecture, loss weighting, sampling, data regime, key results,
verification URLs) lives in `research-notes/slice-*.md` and `data/paper-inventory.csv`.
