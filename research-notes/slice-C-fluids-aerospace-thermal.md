# Slice C: Fluid mechanics, aerospace, thermal applications

Scout C dossier for the PINN survey (target: Springer Artificial Intelligence Review). Time window primary 2021-2026; one pre-2021 anchor allowed and used (Hidden Fluid Mechanics, Science 2020). Papers verified 2026-10-06 via Crossref API, Semantic Scholar API, arXiv, and publisher pages.

## Queries used
1. physics-informed neural networks aerodynamics 2025
2. physics-informed neural networks fluid dynamics review Physics of Fluids
3. PINN RANS turbulence closure Eivazi CMAME physics-informed neural networks Reynolds stress
4. physics-informed neural networks heat transfer review journal
5. Cai Mao Wang Yin Karniadakis "physics-informed neural networks" fluid mechanics review Acta Mechanica Sinica 2021
6. physics-informed neural networks NASA aerodynamics transonic aircraft external flow
7. physics-informed neural networks airfoil inverse design shape optimization aerospace
8. physics-informed neural networks conjugate heat transfer electronics cooling Applied Thermal Engineering
9. physics-informed neural networks multiphase flow porous media subsurface 2023 2024
10. physics-informed neural networks aeroacoustics acoustics sound propagation journal 2022 2023
11. physics-informed neural networks digital twin flow automotive aerodynamics 2025 industrial deployment
12. physics-informed neural networks aircraft icing prediction journal 2024 2025
13. physics-informed neural networks gas turbine cooling film aeroengine heat transfer 2024
14. physics-informed neural networks nuclear reactor thermal hydraulics two-phase boiling flow
15. "physics-informed neural networks" jet noise OR "vortex sound" OR "Lighthill" aeroacoustic prediction

## Screening summary
- candidates screened: 28
- included: 18 (C01-C18)
- 2025-2026 papers included: 5 (C06, C08, C09, C13, C15) — requirement (>=4) met
- Exclusion reasons:
  - Not a PINN (no physics in training): Invertible Neural Networks for airfoil design (AIAA J 10.2514/1.J060866); NeuralFoil (data-only surrogate); classical NN icing-risk predictors.
  - Venue below quality bar: MDPI Applied Sciences PRISMA review of PINNs in aerospace (kept as backup lead only); WVU MSc thesis "PINN-AMF"; Frontiers in Physics 2026 nanofluid microchannel paper (marginal, cites 0).
  - Preprint-only or venue unverified: nuclear CHF gray-box PINN (SSRN); 2D street-canyon Reynolds-stress PINN (SSRN 2025); "Shear Flow Trap" SSRN 2026.
  - Duplicate of included work: Almajid SPE ATCE 2020 conference version (journal version JPSE 2022 included instead); Wassing ECCOMAS 2022 conference version (PoF 2025 journal version included).
  - Out of slice focus: RANS-CNN duct flows (Computers & Fluids 2026, CNN-family), GT2025 McNichols & Bons linear-cascade paper (kept as lead only).
- Citation-count sources: S2 = Semantic Scholar citationCount (API); CR = Crossref is-referenced-by-count. All counts fetched 2026-10-06; nothing estimated.

## Paper records

### C01
- Title: Hidden fluid mechanics: Learning velocity and pressure fields from flow visualizations
- Authors: Maziar Raissi et al. (Raissi, Yazdani, Karniadakis)
- Year: 2020 (anchor)
- Venue: Science
- Type: journal
- Identifier: DOI:10.1126/science.aaw4741
- URL: https://www.science.org/doi/10.1126/science.aaw4741 (verified via Crossref + S2)
- Citations: ~2198 (S2)
- Domain: fluid mechanics — incompressible flow field reconstruction from passive-scalar visualization (biomedical hemodynamics, environmental flows); foundational for any industry using imaging + CFD
- Problem type: inverse
- Physics enforced: incompressible Navier-Stokes (continuity + momentum) + passive-scalar advection
- Enforcement mechanism: divergence-free velocity ansatz (hard continuity) + soft momentum residuals
- Architecture: fully-connected MLPs; velocity split into network output + gradient of scalar potential
- Loss & weighting: PDE residual + data mismatch + BC terms; standard equal-weight summation (per paper)
- Sampling & training: collocation on imaging domain; Adam then L-BFGS (per paper)
- Data regime: experimental (flow visualization videos)
- Key result: reconstructs hidden velocity/pressure in 2-D and 3-D (e.g., vortex-street and cerebral-aneurysm flows) from dye/smoke videos only
- Relevance to review: canonical demonstration that physics constraints replace labeled CFD data — template cited by nearly every applied fluids PINN
- Verification: verified via Crossref https://api.crossref.org/works/10.1126/science.aaw4741

### C02
- Title: Physics-informed neural networks (PINNs) for fluid mechanics: a review
- Authors: Shengze Cai et al. (Cai, Mao, Wang, Yin, Karniadakis)
- Year: 2021
- Venue: Acta Mechanica Sinica
- Type: journal
- Identifier: DOI:10.1007/s10409-021-01148-1
- URL: https://link.springer.com/article/10.1007/s10409-021-01148-1
- Citations: ~2220 (S2)
- Domain: fluid mechanics review — incompressible, compressible, biomedical flows; inverse problems (3-D wake, supersonic flow)
- Problem type: review (covers forward/inverse)
- Physics enforced: incompressible NSE; compressible NSE/Euler (surveyed)
- Enforcement mechanism: soft residual (surveyed variants)
- Architecture: survey of MLP-based PINNs and variants
- Loss & weighting: survey
- Sampling & training: survey
- Data regime: survey (sparse to dense)
- Key result: establishes the standard taxonomy of flow-PINN uses: forward solver, data assimilation, and hidden-field/parameter inversion
- Relevance to review: dedicated fluid-mechanics PINN review (slice requirement g); Springer venue suits the target journal
- Verification: verified via Crossref + Springer landing page

### C03
- Title: Physics-Informed Neural Networks for Heat Transfer Problems
- Authors: Shengze Cai et al. (Cai, Wang, Wang, Perdikaris, Karniadakis)
- Year: 2021
- Venue: Journal of Heat Transfer (ASME), 143(6), 060801
- Type: journal
- Identifier: DOI:10.1115/1.4050542
- URL: https://asmedigitalcollection.asme.org/heattransfer/article/143/6/060801/1104439
- Citations: ~1393 (S2)
- Domain: thermal engineering review — conduction, convection, radiation, coupled multiphysics
- Problem type: review (covers forward/inverse)
- Physics enforced: heat equation, convection-diffusion, radiative transfer, coupled NSE+energy (surveyed)
- Enforcement mechanism: soft residual via automatic differentiation (surveyed)
- Architecture: survey of MLP PINNs
- Loss & weighting: survey (multi-task/balancing discussed)
- Sampling & training: survey
- Data regime: survey (none to sparse to dense)
- Key result: frames heat-transfer PINNs as multi-task learning; catalogs forward/inverse conduction-convection-radiation cases
- Relevance to review: anchor thermal review; defines the thermal subdomain vocabulary for the survey
- Verification: verified via Crossref https://api.crossref.org/works/10.1115/1.4050542 (author list corrected against Crossref)

### C04
- Title: Physics-informed neural networks for solving Reynolds-averaged Navier-Stokes equations
- Authors: Hamidreza Eivazi et al. (Eivazi, Tahani, Schlatter, Vinuesa)
- Year: 2022
- Venue: Physics of Fluids, 34(7), 075117
- Type: journal
- Identifier: DOI:10.1063/5.0095270
- URL: https://pubs.aip.org/aip/pof/article/34/7/075117 (verified via Crossref)
- Citations: ~469 (CR)
- Domain: turbulence modeling — wall-bounded turbulent flows (CFD/aerospace research)
- Problem type: forward (with field reconstruction)
- Physics enforced: incompressible RANS + continuity, without any turbulence model or assumption
- Enforcement mechanism: soft residual
- Architecture: fully-connected MLPs
- Loss & weighting: RANS residual + boundary data terms
- Sampling & training: boundary-only data; collocation interior
- Data regime: sparse (boundary data only)
- Key result: <1% error for laminar Falkner-Skan; good accuracy for ZPG/APG boundary layers, NACA4412 airfoil, periodic hill including Reynolds-stress components
- Relevance to review: flagship demonstration that PINNs can bypass turbulence closures given only boundary data — directly relevant to RANS-surrogate industry interest
- Verification: verified via Crossref https://api.crossref.org/works/10.1063/5.0095270

### C05
- Title: NSFnets (Navier-Stokes flow nets): Physics-informed neural networks for the incompressible Navier-Stokes equations
- Authors: Xiaowei Jin et al. (Jin, Cai, Li, Karniadakis)
- Year: 2021
- Venue: Journal of Computational Physics, 426, 109951
- Type: journal
- Identifier: DOI:10.1016/j.jcp.2020.109951
- URL: https://www.sciencedirect.com/science/article/pii/S0021999120307240 (verified via Crossref)
- Citations: ~1115 (CR)
- Domain: computational fluid dynamics — systematic forward solver for incompressible flows (methodological backbone for fluids industry use)
- Problem type: forward
- Physics enforced: incompressible NSE with periodic boundary conditions
- Enforcement mechanism: soft residual (direct and divergence-free formulations compared)
- Architecture: MLPs; systematic ablations of depth/width, activations, formulations
- Loss & weighting: residual + IC/BC; weighting ablations
- Sampling & training: uniform/random collocation; Adam + L-BFGS
- Data regime: none (validation against DNS data)
- Key result: systematic recipe establishing when vanilla PINNs solve unsteady incompressible NSE accurately (vortex-shedding, Kida flow benchmarks)
- Relevance to review: the reference "baseline" paper cited by most applied fluid-PINN works; defines methodological components
- Verification: verified via Crossref https://api.crossref.org/works/10.1016/j.jcp.2020.109951

### C06
- Title: Physics-informed neural networks for inviscid transonic flows around an airfoil
- Authors: Simon Wassing et al. (Wassing, Langer, Bekemeyer — DLR)
- Year: 2025 (preprint arXiv 2024)
- Venue: Physics of Fluids, 37(8)
- Type: journal
- Identifier: DOI:10.1063/5.0276518 (arXiv:2408.17364)
- URL: https://pubs.aip.org/aip/pof/article/37/8/ (via Crossref); preprint https://arxiv.org/abs/2408.17364
- Citations: ~9 (CR)
- Domain: aerospace external aerodynamics — transonic airfoil (DLR, German Aerospace Center)
- Problem type: forward (parametric)
- Physics enforced: compressible Euler equations (sub- and transonic regimes)
- Enforcement mechanism: soft residual + artificial dissipation added to stabilize shocks
- Architecture: MLP with angle-of-attack input (parametric single network)
- Loss & weighting: Euler residual with dissipation term + farfield/wall BCs
- Sampling & training: collocation sampling; training against finite-volume reference for validation
- Data regime: none (CFD validation)
- Key result: single network approximates flow across AoA range including shocks; matrix-valued artificial viscosity most stable
- Relevance to review: DLR-authored industrial-lab case for multi-query aerodynamic parametric studies replacing repeated CFD runs
- Verification: verified via arXiv https://arxiv.org/abs/2408.17364 + Crossref https://api.crossref.org/works/10.1063/5.0276518

### C07
- Title: Flow Reconstruction in a Transonic Turbine Cascade Using Physics-Informed Neural Networks (PINNs)
- Authors: M. McNichols et al. (NASA / Ohio State; incl. Juangphanich, Hawke, Shoemaker, Poulson, Brandt, Bons)
- Year: 2024
- Venue: ASME Turbo Expo (GT2024), Vol. 12C: Turbomachinery
- Type: conference
- Identifier: DOI:10.1115/GT2024-128885 (NASA NTRS 20240000093)
- URL: https://ntrs.nasa.gov/citations/20240000093
- Citations: ~3 (CR)
- Domain: aerospace/gas-turbine — transonic turbine cascade (NASA-affiliated turbomachinery)
- Problem type: both
- Physics enforced: governing flow equations of transonic cascade flow (compressible NSE/RANS-based, 2-D)
- Enforcement mechanism: soft residual; three modes — forward, data-assimilation, inverse
- Architecture: MLP PINN
- Loss & weighting: PDE residual + optional midspan pressure data term
- Sampling & training: trained with all/half/leading-edge-only/trailing-edge-only data subsets
- Data regime: sparse experimental (measured midspan pressure) + none (forward mode)
- Key result: good agreement with CFD for CMC7 blade when all data used; quantifies data-subset sensitivity
- Relevance to review: NASA-authored evidence of PINN use with real rig data in turbomachinery — direct industrial applicability signal
- Verification: verified via NASA NTRS https://ntrs.nasa.gov/citations/20240000093 + Crossref https://api.crossref.org/works/10.1115/GT2024-128885

### C08
- Title: Flight Dynamics Modeling Using Physics-Informed Neural Networks
- Authors: N. Michek et al. (Michek, Mehta, Huebsch — West Virginia University)
- Year: 2026 (AIAA Journal; print Jan 2026)
- Venue: AIAA Journal
- Type: journal
- Identifier: DOI:10.2514/1.J063991
- URL: https://arc.aiaa.org/doi/10.2514/1.J063991
- Citations: ~6 (CR)
- Domain: aerospace — flight dynamics/system identification from flight test data
- Problem type: inverse (parameter estimation / system ID)
- Physics enforced: six-DOF rigid-body equations of motion with aerodynamic model terms
- Enforcement mechanism: soft residual; trajectory network + parameter-estimation module
- Architecture: three variants — Determinant PINNs, Non-Determinant PINNs, Modified Non-Determinant PINNs
- Loss & weighting: trajectory residual vs measured flight data + physics consistency of parameter modules
- Sampling & training: trained on experimental flight-test time histories
- Data regime: experimental (flight data)
- Key result: estimates AoA-varying aerodynamic parameters within a framework designed for experimental flight testing
- Relevance to review: bridges PINNs to real flight-test pipelines — rare industrial aerospace deployment path (aircraft/simulation industry)
- Verification: verified via Crossref https://api.crossref.org/works/10.2514/1.J063991

### C09
- Title: A physics-informed neural network-based aerodynamic parameter identification method for aircraft
- Authors: H. Lin et al. (Lin, Chen, Yang, Jiang, Liu)
- Year: 2025
- Venue: Physics of Fluids, 37
- Type: journal
- Identifier: DOI:10.1063/5.0249130
- URL: https://pubs.aip.org/aip/pof/article/37/2/027200/3337533
- Citations: ~20 (CR)
- Domain: aerospace — aerodynamic parameter identification for ground/flight simulation
- Problem type: inverse
- Physics enforced: six-DOF motion equations as physical constraint (longitudinal-motion case study)
- Enforcement mechanism: soft residual; aerodynamic parameters as trainable variables
- Architecture: NN surrogate of aircraft model with physics-constrained training
- Loss & weighting: motion-equation residual + trajectory data mismatch
- Sampling & training: flight/measured trajectory data
- Data regime: sparse (simulation/measurement trajectories)
- Key result: outperforms genetic-algorithm and conventional NN identification; mitigates system and data errors
- Relevance to review: shows PINN system-ID entering aircraft-modeling practice (simulation & training industry)
- Verification: verified via Crossref https://api.crossref.org/works/10.1063/5.0249130

### C10
- Title: Physics-informed neural networks for transonic flow around a cylinder with high Reynolds number
- Authors: X. Ren et al. (Ren, Hu, Su, Zhang, Yu)
- Year: 2024
- Venue: Physics of Fluids, 36
- Type: journal
- Identifier: DOI:10.1063/5.0200384
- URL: https://pubs.aip.org/aip/pof/article/36/ (via Crossref)
- Citations: ~46 (CR)
- Domain: aerospace/external aerodynamics — high-Re transonic bluff body
- Problem type: both (learn from sparse data, predict global field)
- Physics enforced: RANS equations and Euler equations (PINN-RANS and PINN-Euler variants)
- Enforcement mechanism: hard boundary condition in output layer + sampling-distance function in input layer
- Architecture: MLP with distance-function input feature; gradient weight factor in loss
- Loss & weighting: PDE residuals with gradient weighting + local velocity data term
- Sampling & training: distance-aware sampling of thin boundary layers; local key-region data
- Data regime: sparse (velocity in local key regions)
- Key result: PINN-RANS accurately recovers global field incl. boundary layer and wake from local data; PINN-Euler fails in separated regions
- Relevance to review: explicit recipe (hard BC + distance features + gradient weighting) for industry-grade high-Re flows
- Verification: verified via Crossref https://api.crossref.org/works/10.1063/5.0200384

### C11
- Title: Physics-informed deep learning for simultaneous surrogate modeling and PDE-constrained optimization of an airfoil geometry
- Authors: Yubiao Sun et al. (Sun, Sengupta, Juniper — University of Cambridge)
- Year: 2023
- Venue: Computer Methods in Applied Mechanics and Engineering, 411, 116042
- Type: journal
- Identifier: DOI:10.1016/j.cma.2023.116042
- URL: https://www.sciencedirect.com/science/article/pii/S0045782523001664
- Citations: ~127 (CR; 134 S2)
- Domain: aerospace design — airfoil aerodynamic shape optimization
- Problem type: control (PDE-constrained design optimization)
- Physics enforced: Navier-Stokes equations, satisfied approximately across the whole shape-parameter design space
- Enforcement mechanism: soft residual; autodiff gradients for L-BFGS optimizer
- Architecture: PINN with geometry parameters as inputs (collocation over design space)
- Loss & weighting: NSE residual over design-space collocation points
- Sampling & training: adaptive sampling along optimization trajectory
- Data regime: none (validated vs conventional CFD)
- Key result: maximizes lift-to-drag for 1- and 11-parameter airfoils; avoids writing adjoint codes
- Relevance to review: demonstrates adjoint-free aerodynamic optimization — a core industrial use case (aircraft design)
- Verification: verified via Crossref + S2 (abstract fetched)

### C12
- Title: Physics-informed neural network simulation of conjugate heat transfer in manifold microchannel heat sinks for high-power IGBT cooling
- Authors: Xiangzhi Zhang et al. (Zhang, Tu, Yan)
- Year: 2024
- Venue: International Communications in Heat and Mass Transfer, 159, 108036
- Type: journal
- Identifier: DOI:10.1016/j.icheatmasstransfer.2024.108036
- URL: https://www.sciencedirect.com/science/article/pii/S073519332400798X
- Citations: ~39 (S2; 14 CR)
- Domain: thermal engineering — electronics cooling (power electronics / automotive IGBT industry)
- Problem type: forward
- Physics enforced: coupled fluid flow + heat transfer (conjugate heat transfer) in manifold microchannels
- Enforcement mechanism: soft residual (standard PINN formulation)
- Architecture: PINN for coupled flow/temperature fields
- Loss & weighting: flow + energy residuals incl. solid-fluid interface coupling
- Sampling & training: collocation; validated against CHT simulations
- Data regime: dense simulation (validation)
- Key result: PINN reproduces CHT fields for MMC heat sinks used in high-power IGBT thermal management
- Relevance to review: concrete electronics-cooling industry case (EV power modules) where mesh-free surrogates cut design cost
- Verification: verified via Crossref https://api.crossref.org/works/10.1016/j.icheatmasstransfer.2024.108036

### C13
- Title: Physics-informed neural networks for heat transfer: A mechanism-driven review of conduction, convection, radiation, and coupled multiphysics systems
- Authors: Yi-Fan Li et al. (Li, Lian, Yuan, Li, Han, Gu, Xie)
- Year: 2026
- Venue: Applied Thermal Engineering, 303, 132483
- Type: journal
- Identifier: DOI:10.1016/j.applthermaleng.2026.132483
- URL: https://www.sciencedirect.com/science/article/pii/S1359431126027912
- Citations: ~1 (S2/CR; published 2026)
- Domain: thermal engineering review — mechanism-by-mechanism (conduction/convection/radiation/multiphysics)
- Problem type: review
- Physics enforced: heat conduction, convective transport, radiation, coupled systems (surveyed)
- Enforcement mechanism: soft residual and constraint variants (surveyed)
- Architecture: survey
- Loss & weighting: survey
- Sampling & training: survey
- Data regime: survey
- Key result: organizes PINN-heat-transfer literature by physical mechanism rather than application sector; identifies sparse-data and strong-constraint trends
- Relevance to review: most recent (2026) dedicated thermal PINN review — anchors the survey's thermal section currency
- Verification: verified via Crossref + S2 https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.applthermaleng.2026.132483

### C14
- Title: A Physics-Informed Neural Network for Solving the Inverse Heat Transfer Problem in Gas Turbine Rotating Cavities
- Authors: M. Puttock-Brown et al. (Puttock-Brown, Bindhu, Ashby)
- Year: 2024
- Venue: Journal of Turbomachinery (ASME), 147
- Type: journal
- Identifier: DOI:10.1115/1.4067125
- URL: https://asmedigitalcollection.asme.org/turbomachinery/article/doi/10.1115/1.4067125 (also GT2024-128967)
- Citations: ~13 (CR)
- Domain: aerospace/thermal — aero-engine high-pressure compressor internal air system (gas-turbine cooling)
- Problem type: inverse
- Physics enforced: heat conduction equation in rotating-cavity walls (2-D)
- Enforcement mechanism: soft residual; NN maps measured temperature profiles to surface heat flux
- Architecture: PINN with experimental radial temperature profiles as inputs
- Loss & weighting: conduction residual; forward check via 2-D finite-element model
- Sampling & training: noise-free synthetic training set spanning radial temperature profiles; experimental data at inference
- Data regime: experimental (radial temperature profiles) + synthetic training
- Key result: predicted surface heat fluxes recover the original temperature profiles in FEM verification
- Relevance to review: industrial aero-engine thermal management — inverse problems where sensors are sparse and CFD is prohibitive
- Verification: verified via Crossref https://api.crossref.org/works/10.1115/1.4067125

### C15
- Title: Physics-informed neural network for predicting multi-row film cooling superposition using Fourier transform and attention mechanism
- Authors: H. Yan et al. (Yan, Ye, Zhou, Li, Ye, Zhang)
- Year: 2025
- Venue: Physics of Fluids, 37
- Type: journal
- Identifier: DOI:10.1063/5.0274462
- URL: https://pubs.aip.org/aip/pof/ (via Crossref 10.1063/5.0274462)
- Citations: ~18 (CR)
- Domain: aerospace/thermal — aero-engine nozzle/turbine film cooling (gas-turbine thermal protection)
- Problem type: forward (correction of engineering model)
- Physics enforced: Sellers superposition law for film-cooling effectiveness (engineering physics), correcting its flow/diffusion deviation
- Enforcement mechanism: hybrid (physics correlation + data-driven residual correction)
- Architecture: three branches — time-domain CNN, frequency-domain (DFT) branch with attention, residual MLP branch
- Loss & weighting: superposition-consistency + data fit
- Sampling & training: multi-row hole geometry and aerodynamic parameter datasets
- Data regime: dense simulation/experimental cooling-effectiveness data
- Key result: fixes Sellers superposition deviation for multi-row film cooling with attention-guided error-region focus
- Relevance to review: shows PINN-style hybrids entering gas-turbine cooling design practice (aero-engine industry)
- Verification: verified via Crossref https://api.crossref.org/works/10.1063/5.0274462

### C16
- Title: Prediction of porous media fluid flow using physics informed neural networks
- Authors: Mohammed M. Almajid et al. (Almajid, Abu-Al-Saud)
- Year: 2022
- Venue: Journal of Petroleum Science and Engineering, 208, 109205
- Type: journal
- Identifier: DOI:10.1016/j.petrol.2021.109205
- URL: https://www.sciencedirect.com/science/article/pii/S0920410521012505 (via Crossref)
- Citations: ~257 (S2; 269 CR)
- Domain: porous media flow — petroleum/reservoir engineering industry
- Problem type: forward (with sparse-data reconstruction)
- Physics enforced: mass conservation + Darcy's law (single-phase incompressible flow in porous media)
- Enforcement mechanism: soft residual + observation data assimilation
- Architecture: MLP PINN
- Loss & weighting: PDE residual + sparse pressure/velocity observation terms
- Sampling & training: collocation + sparse observation points
- Data regime: sparse
- Key result: PINN reproduces heterogeneous porous-media flow fields from sparse data, competitive with conventional simulators
- Relevance to review: largest-cited applied porous-flow PINN — evidences oil & gas industry uptake of physics-constrained surrogates
- Verification: verified via Crossref https://api.crossref.org/works/10.1016/j.petrol.2021.109205 + S2

### C17
- Title: Prediction of fluid flow in porous media by sparse observations and physics-informed PointNet
- Authors: Amir Kashefi et al. (Kashefi, Mukerji — Stanford)
- Year: 2023 (online 2022)
- Venue: Neural Networks, 167
- Type: journal
- Identifier: DOI:10.1016/j.neunet.2023.08.006 (arXiv:2208.13434)
- URL: https://www.sciencedirect.com/science/article/pii/S0893608023004270 (via Crossref); preprint https://arxiv.org/abs/2208.13434
- Citations: ~53 (S2)
- Domain: porous media / multiphase-adjacent — pore-scale flow (subsurface, petrophysics industry)
- Problem type: forward (geometry-to-field mapping)
- Physics enforced: steady-state Stokes flow (creeping flow) in pore spaces
- Enforcement mechanism: soft residual on point clouds (physics-informed PointNet)
- Architecture: PointNet — pore-space-only point-cloud input, smooth boundary representation, variable spatial resolution
- Loss & weighting: Stokes residual + sparse pressure-observation terms
- Sampling & training: sparse point observations; robustness tested to noisy sensor data
- Data regime: sparse
- Key result: predicts pore-scale velocity/pressure fields from sparse observations with memory-efficient irregular-geometry handling
- Relevance to review: geometry-generalizing physics-informed network — step toward reusable industrial surrogates across rock samples
- Verification: verified via Crossref + S2 (abstract fetched) https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.neunet.2023.08.006

### C18
- Title: Sound propagation in realistic interactive 3D scenes with parameterized sources using deep neural operators
- Authors: Nikola Borrel-Jensen et al. (Borrel-Jensen, Goswami, Engsig-Karup, Karniadakis, Jeong)
- Year: 2024
- Venue: Proceedings of the National Academy of Sciences (PNAS), 121
- Type: journal
- Identifier: DOI:10.1073/pnas.2312159120
- URL: https://www.pnas.org/doi/10.1073/pnas.2312159120
- Citations: ~37 (CR)
- Domain: acoustics/aeroacoustics-adjacent — room acoustics for VR/game audio and spatial computing industry
- Problem type: operator
- Physics enforced: linear acoustic wave equation (diffraction/interference fully captured)
- Enforcement mechanism: operator (DeepONet approximating wave-equation solution operator)
- Architecture: DeepONet with parametric source positions as inputs
- Loss & weighting: operator regression on wave-equation solutions
- Sampling & training: precomputed wave simulations for operator training
- Data regime: dense simulation
- Key result: millisecond-scale sound-propagation predictions in realistic 3D scenes, avoiding offline impulse-response storage
- Relevance to review: shows physics-based neural operators reaching commercial real-time markets (media/entertainment) — contrast to slow vanilla PINN solvers
- Verification: verified via Crossref https://api.crossref.org/works/10.1073/pnas.2312159120

## Machine rows

C01|Hidden fluid mechanics: Learning velocity and pressure fields from flow visualizations|2020|Science|journal|DOI:10.1126/science.aaw4741|2198|Fluid/incompressible flow reconstruction from imaging|Incompressible NSE + passive-scalar advection|Divergence-free velocity ansatz (hard) + soft momentum residuals|inverse|1|Y
C02|Physics-informed neural networks (PINNs) for fluid mechanics: a review|2021|Acta Mechanica Sinica|journal|DOI:10.1007/s10409-021-01148-1|2220|Fluid mechanics review (incompressible/compressible/biomedical)|Incompressible and compressible NSE (surveyed)|Soft residual (surveyed)|review|1|Y
C03|Physics-Informed Neural Networks for Heat Transfer Problems|2021|Journal of Heat Transfer|journal|DOI:10.1115/1.4050542|1393|Thermal engineering review (conduction/convection/radiation)|Heat equation + convection-diffusion + radiation + coupled NSE-energy|Soft residual via autodiff (surveyed)|review|1|Y
C04|Physics-informed neural networks for solving Reynolds-averaged Navier-Stokes equations|2022|Physics of Fluids|journal|DOI:10.1063/5.0095270|469|Turbulence/RANS closure-free reconstruction (CFD)|Incompressible RANS + continuity without turbulence model|Soft residual|forward|1|Y
C05|NSFnets (Navier-Stokes flow nets)|2021|Journal of Computational Physics|journal|DOI:10.1016/j.jcp.2020.109951|1115|CFD forward solver benchmark|Incompressible NSE with periodic BC|Soft residual (direct and divergence-free variants)|forward|2|Y
C06|Physics-informed neural networks for inviscid transonic flows around an airfoil|2025|Physics of Fluids|journal|DOI:10.1063/5.0276518|9|Aerospace external aerodynamics (DLR) transonic airfoil|Compressible Euler equations|Soft residual + artificial dissipation for shocks|forward|2|Y
C07|Flow Reconstruction in a Transonic Turbine Cascade Using PINNs|2024|ASME Turbo Expo (GT2024)|conference|DOI:10.1115/GT2024-128885|3|Gas turbine turbomachinery (NASA/Ohio State) transonic cascade|Transonic cascade flow governing equations (2-D compressible)|Soft residual in forward/data-assimilation/inverse modes|both|3|Y
C08|Flight Dynamics Modeling Using Physics-Informed Neural Networks|2026|AIAA Journal|journal|DOI:10.2514/1.J063991|6|Aerospace flight dynamics/system identification from flight test|Six-DOF equations of motion with aerodynamic model|Soft residual + trajectory/parameter networks|inverse|2|Y
C09|A physics-informed neural network-based aerodynamic parameter identification method for aircraft|2025|Physics of Fluids|journal|DOI:10.1063/5.0249130|20|Aerospace aerodynamic parameter ID for flight simulation|Six-DOF motion equations (longitudinal case)|Soft residual with parameters as trainable variables|inverse|3|Y
C10|Physics-informed neural networks for transonic flow around a cylinder with high Reynolds number|2024|Physics of Fluids|journal|DOI:10.1063/5.0200384|46|Aerospace high-Re transonic external flow|RANS and Euler equations|Hard BC output layer + distance-function inputs + gradient weighting|both|3|Y
C11|Physics-informed deep learning for simultaneous surrogate modeling and PDE-constrained optimization of an airfoil geometry|2023|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2023.116042|127|Aerospace airfoil shape optimization (adjoint-free)|Navier-Stokes equations across design space|Soft residual + autodiff L-BFGS optimization|control|2|Y
C12|Physics-informed neural network simulation of conjugate heat transfer in manifold microchannel heat sinks for high-power IGBT cooling|2024|International Communications in Heat and Mass Transfer|journal|DOI:10.1016/j.icheatmasstransfer.2024.108036|39|Electronics cooling (automotive power electronics IGBT)|Conjugate heat transfer: flow + energy with solid-fluid coupling|Soft residual|forward|2|Y
C13|Physics-informed neural networks for heat transfer: A mechanism-driven review|2026|Applied Thermal Engineering|journal|DOI:10.1016/j.applthermaleng.2026.132483|1|Thermal engineering review (2026 currency anchor)|Conduction + convection + radiation + coupled multiphysics|Soft residual and constraint variants (surveyed)|review|2|Y
C14|A Physics-Informed Neural Network for Solving the Inverse Heat Transfer Problem in Gas Turbine Rotating Cavities|2024|Journal of Turbomachinery|journal|DOI:10.1115/1.4067125|13|Aero-engine internal air system thermal (gas turbine industry)|Heat conduction equation in rotating cavity walls|Soft residual; experimental-input inverse mapping|inverse|3|Y
C15|Physics-informed neural network for predicting multi-row film cooling superposition using Fourier transform and attention mechanism|2025|Physics of Fluids|journal|DOI:10.1063/5.0274462|18|Aero-engine film cooling (nozzle/turbine thermal protection)|Sellers superposition law for film-cooling effectiveness|Hybrid physics-correlation + Fourier/attention residual branch|forward|3|Y
C16|Prediction of porous media fluid flow using physics informed neural networks|2022|Journal of Petroleum Science and Engineering|journal|DOI:10.1016/j.petrol.2021.109205|257|Porous media flow (oil and gas reservoir engineering)|Mass conservation + Darcy law (single-phase)|Soft residual + sparse observation assimilation|forward|3|Y
C17|Prediction of fluid flow in porous media by sparse observations and physics-informed PointNet|2023|Neural Networks|journal|DOI:10.1016/j.neunet.2023.08.006|53|Pore-scale porous flow (subsurface/petrophysics)|Steady Stokes flow in pore spaces|Soft residual on point clouds (physics-informed PointNet)|forward|3|Y
C18|Sound propagation in realistic interactive 3D scenes with parameterized sources using deep neural operators|2024|Proceedings of the National Academy of Sciences|journal|DOI:10.1073/pnas.2312159120|37|Acoustics for VR/game audio and spatial computing industry|Linear acoustic wave equation|Operator surrogate (DeepONet)|operator|4|Y

## Slice takeaways
- Dominant physics: incompressible NSE/RANS dominates fluids works (C04, C05, C07, C10); compressibility (Euler/transonic) arrives via stabilization tricks (C06, C10); thermal works enforce energy/conduction equations, increasingly conjugate (fluid+solid) formulations (C12, C13, C14); non-PDE "physics" such as Sellers film-cooling superposition (C15) shows engineering correlations being used as constraints too.
- Common fluids enforcement tricks beyond the vanilla soft residual: divergence-free velocity decompositions (hard continuity, C01/C05); hard BCs embedded in the output layer plus distance-function input features for thin boundary layers (C10); artificial dissipation injected into the PDE to stabilize shocks (C06); three-mode usage of the same network (forward, data assimilation, inverse) with sparse experimental data (C07).
- Industry adoption evidence is real but early: DLR (transonic parametric airfoils, C06), NASA turbomachinery with rig data (C07), flight-test system-ID heading to AIAA Journal (C08, C09), aero-engine inverse thermal and film cooling (C14, C15), EV power-electronics cooling (C12), oil & gas porous flow (C16, C17), and real-time acoustics reaching commercial VR markets via operators (C18). Pure-PINN digital twins for automotive aerodynamics were searched but no peer-reviewed deployment report was found — a documented gap.
- Gaps for the survey: PINN+icing, nuclear two-phase thermal-hydraulics, and aeroacoustic (Lighthill/jet-noise) PINNs remain niche with few peer-reviewed journal results; most 2025-2026 industrial-flavored work shifts from pure residual minimization to hybrid physics-correlation + attention/Fourier architectures (C15) and operator surrogates (C18) for speed.
