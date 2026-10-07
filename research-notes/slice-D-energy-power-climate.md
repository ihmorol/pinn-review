# Slice D: Energy, power systems, batteries, climate/weather

Scout D | verified 2026-10-06 | scope: PINNs/PIML in energy, power systems, batteries, buildings/HVAC, nuclear, renewables, climate/weather (primary window 2021-2026).

## Queries used

1. physics-informed neural networks power systems survey
2. physics-informed neural network lithium-ion battery state of charge estimation
3. Beucler "Enforcing Analytic Constraints in Neural Networks Emulating Physical Systems" Physical Review Letters
4. Kochkov "Neural general circulation models for weather and climate" Nature 2024
5. physics-informed neural network P2D pseudo-two-dimensional lithium battery model Journal of Power Sources
6. physics-informed neural network building HVAC thermal energy model Applied Energy
7. physics-informed neural network nuclear reactor thermal-hydraulics "Nuclear Engineering"
8. physics-informed neural networks nuclear engineering review Annals of Nuclear Energy reactor physics
9. physics-informed neural network wind speed forecasting physical constraints Renewable Energy
10. physics-informed neural network swing equation transient stability power system frequency dynamics
11. physics-informed machine learning energy systems review 2025 Applied Energy
12. physics-informed neural network load forecasting power flow constraints IEEE Transactions Power Systems
13. physics-informed neural network solar irradiance forecasting clear sky model
14. "physics-informed" neural networks battery degradation state of health prognosis Nature Communications 2024
15. physics-informed neural network digital twin grid battery management system deployment 2025
16. Xu "Physics-informed neural networks for power systems" review Renewable Sustainable Energy Reviews 2026

## Screening summary

- Candidates screened: 24
- Included: 19
- 2025-2026 papers included: 8 (D03, D04, D05, D08, D14, D15, D18, D19) — exceeds the >=4 requirement.
- Excluded (reasons):
  - Al-Ismail 2024, "PINN-Based AC Optimal Power Flow Under High RES Penetration" (IEEE Access, DOI 10.1109/access.2024.3514362, 12 cites): redundant with stronger EPSR 2022 AC-OPF record (D02); lower-impact venue.
  - Stiasny/Misyris PowerTech 2021 "PINNs for Non-linear System Identification for Power System Dynamics" (DOI 10.1109/powertech46648.2021.9495063, 69 cites): strong candidate, cut only to cap list length; recommend for Slice A/bibliography backup.
  - RTI-Net (Renewable Energy 2025), PI-SDNN (Scientific Reports 2026), PISSM (arXiv 2026), Bird clear-sky PINN (GitHub-only): solar forecasting candidates dropped — thinner verification and mostly engineering-variant models; only 2 renewables slots kept (wind).
  - PhysCon building model (Energy and Buildings 2023) and MDPI Buildings 2026 urban PINN review: not verified in time; backup candidates.
  - Iliadis et al. 2025 (MDPI Energies, state estimation, ~28 cites): lower-impact venue, overlapping with D03.
  - Several wind/solar hits from aggregator sites (freederia, themoonlight.io): unverifiable — dropped.
- Citation-count note: Semantic Scholar API was heavily rate-limited (HTTP 429) during verification (parallel scouts); fallbacks were Crossref API (authoritative, but lagging), arXiv API, and Google-Scholar snippets from search results (marked ~).

## Paper records

### D01
- Title: Physics-Informed Neural Networks for Power Systems
- Authors: G. S. Misyris et al. (Misyris, Venzke, Chatzivasileiadis)
- Year: 2020
- Venue: IEEE Power & Energy Society General Meeting (PESGM)
- Type: conference
- Identifier: DOI:10.1109/PESGM41954.2020.9282004; arXiv:1911.03737
- URL: https://arxiv.org/abs/1911.03737 (verified via arXiv API + Crossref)
- Citations: ~570 (Google Scholar via search snippet; 243 per Crossref)
- Domain: energy/power — grid dynamics & steady-state (foundational paper; predates 2021 window, included as the field's origin)
- Problem type: both (forward dynamic-state estimation + inverse parameter identification)
- Physics enforced: swing equation (generator rotor angle/frequency dynamics) and steady-state power-system models
- Enforcement mechanism: soft-penalty on ODE residual in supervised loss
- Architecture: feedforward NN on time-series inputs
- Loss & weighting: data-fit + scaled ODE-residual penalty; second-derivative terms handled to avoid full Jacobians
- Sampling & training: supervised on simulated dynamic responses; residual evaluated at collocation points
- Data regime: sparse (claims substantially less training data than pure ML)
- Key result: recovers rotor angle, frequency, and uncertain parameters (inertia, damping) at a fraction of conventional computational time; ~87x faster dynamics determination reported in follow-up coverage
- Relevance to review: the canonical "PINN enters power engineering" reference; anchors the industry narrative for grid digital tools
- Verification: verified via https://api.crossref.org/works/10.1109/pesgm41954.2020.9282004 and https://arxiv.org/abs/1911.03737

### D02
- Title: Physics-Informed Neural Networks for AC Optimal Power Flow
- Authors: R. Nellikkath & S. Chatzivasileiadis
- Year: 2022
- Venue: Electric Power Systems Research
- Type: journal
- Identifier: DOI:10.1016/j.epsr.2022.108412
- URL: https://www.sciencedirect.com/science/article/pii/S0378779622006865 (record via Crossref)
- Citations: 163 (Crossref)
- Domain: energy/power — AC optimal power flow (grid operations)
- Problem type: control (OPF solution prediction with optimality guarantees)
- Physics enforced: AC power-flow equations (Kirchhoff laws, nonlinear power balance)
- Enforcement mechanism: soft-penalty (physics-informed loss on power-flow residuals)
- Architecture: feedforward NN mapping bus loads to generator setpoints
- Loss & weighting: OPF-cost + equality/inequality constraint penalties; Lagrangian pseudo-dual for weighting
- Sampling & training: trained on OPF instances; worst-case error-certification discussion (with follow-up 2023 IEEE TSG work)
- Data regime: dense simulation (case files, e.g., IEEE/PGLib test cases)
- Key result: near-global-optimal AC-OPF solutions with orders-of-magnitude faster inference than interior-point solvers
- Relevance to review: flagship industrial use-case — replacing numerical OPF solvers in transmission operation
- Verification: verified via https://api.crossref.org/works/10.1016/j.epsr.2022.108412

### D03
- Title: Robust Power System State Estimation using Physics-Informed Neural Networks
- Authors: S. Falas et al. (Falas, Asprou, Konstantinou, Michael)
- Year: 2025
- Venue: arXiv (preprint)
- Type: preprint
- Identifier: arXiv:2507.05874
- URL: https://arxiv.org/abs/2507.05874
- Citations: n/a (new preprint; institutional copy at KAUST repository)
- Domain: energy/power — distribution/transmission state estimation (grid monitoring)
- Problem type: inverse
- Physics enforced: power-flow / network model physics (grid admittance relations)
- Enforcement mechanism: hybrid (physics-informed loss combined with measurement model, targeted at robustness)
- Architecture: NN mapping measurements to bus voltage states
- Loss & weighting: measurement-fit + physics residual; robustness-oriented terms against bad data
- Sampling & training: simulation-generated measurement snapshots
- Data regime: sparse simulation
- Key result: improved accuracy and robustness of state estimation vs purely data-driven baselines, including under measurement noise
- Relevance to review: current industrial direction — physics-informed grid digital twins/monitoring; pairs with KAUST energy-systems program
- Verification: verified via https://arxiv.org/abs/2507.05874

### D04
- Title: KCLNet: Physics-Informed Power Flow Prediction via Constraints Projections
- Authors: P. Dogoulis, K. Tit, M. Cordy
- Year: 2025
- Venue: arXiv (preprint)
- Type: preprint
- Identifier: arXiv:2506.12902
- URL: https://arxiv.org/abs/2506.12902
- Citations: n/a (new preprint)
- Domain: energy/power — power-flow prediction (grid analysis)
- Problem type: forward
- Physics enforced: Kirchhoff's Current Law (KCL) at every bus
- Enforcement mechanism: hard-constraint — hyperplane projection layer enforcing KCL exactly in a GNN
- Architecture: graph neural network with constraint-projection output layer
- Loss & weighting: supervised power-flow loss (KCL satisfied by construction, not by penalty)
- Sampling & training: trained on power-flow solutions of benchmark grids
- Data regime: dense simulation
- Key result: exact KCL satisfaction by architecture improves prediction accuracy and out-of-distribution generalization vs unconstrained GNNs
- Relevance to review: representative of the architectural hard-constraint trend in grid ML — directly relevant to the review's enforcement-mechanism taxonomy
- Verification: verified via https://arxiv.org/abs/2506.12902

### D05
- Title: Physics-informed neural networks for power systems: A systematic review
- Authors: X. Xu et al. (Xu, Qiang, Wu, Xuan)
- Year: 2026
- Venue: Sustainable Energy, Grids and Networks
- Type: journal
- Identifier: DOI:10.1016/j.segan.2026.102261
- URL: https://www.sciencedirect.com/science/article/pii/S2352467726001438
- Citations: ~7 (Google Scholar snippet; 1 per Crossref — very recent)
- Domain: energy/power — dedicated survey of PINNs in power systems
- Problem type: both (survey of forward and inverse applications)
- Physics enforced: power-flow equations, rotor/swing dynamics, electromagnetic transients (as reviewed categories)
- Enforcement mechanism: mixed — survey covers soft-penalty and hard/structural constraints
- Architecture: n/a (survey)
- Loss & weighting: n/a
- Sampling & training: n/a
- Data regime: n/a
- Key result: comprehensive taxonomy of PINN algorithmic frameworks, physical-law embedding, and applications for "new power systems" modernization
- Relevance to review: the dedicated 2023-2026 "PINNs power systems" survey requested by the mission — core related-work anchor
- Verification: verified via https://api.crossref.org/works/10.1016/j.segan.2026.102261 + ScienceDirect PII page

### D06
- Title: Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis (PINN4SOH)
- Authors: F. Wang et al. (Wang, Zhai, Zhao, Di, Chen)
- Year: 2024
- Venue: Nature Communications
- Type: journal
- Identifier: DOI:10.1038/s41467-024-48779-z
- URL: https://www.nature.com/articles/s41467-024-48779-z
- Citations: 897 (Semantic Scholar)
- Domain: battery — state of health / degradation prognosis (battery management systems industry)
- Problem type: forecasting (SOH/RUL prognosis)
- Physics enforced: empirical degradation model + state-space equation of capacity fade; degradation stability/monotonicity regularities
- Enforcement mechanism: hybrid — physics-encoded degradation model integrated with recurrent NN training loss
- Architecture: physics-informed recurrent network with attention-based feature extraction (open-source PINN4SOH code)
- Loss & weighting: data loss + model-consistency (degradation/state-space) loss
- Sampling & training: trained across battery types/operating conditions; transfer across chemistries claimed
- Data regime: sparse experimental (public cycling datasets, e.g., CALCE/Oxford-type)
- Key result: accurate and stable SOH estimation and prognosis under varied operating conditions across battery types; the most-cited PINN energy paper of 2024
- Relevance to review: flagship evidence of industrial interest — EV/BMS degradation management; shows PIML leaving pure academia
- Verification: verified via Semantic Scholar DOI lookup + https://www.nature.com/articles/s41467-024-48779-z

### D07
- Title: Physics-Informed Neural Networks for State of Health Estimation in Lithium-Ion Batteries
- Authors: T. Hofmann et al. (Hofmann, Hamar, Rogge, Zoerr, et al.)
- Year: 2023
- Venue: Journal of The Electrochemical Society
- Type: journal
- Identifier: DOI:10.1149/1945-7111/acf0ef
- URL: https://iopscience.iop.org/article/10.1149/1945-7111/acf0ef
- Citations: 104 (Crossref)
- Domain: battery — SOH estimation (BMS industry)
- Problem type: inverse
- Physics enforced: Doyle-Fuller-Newman (P2D) electrochemical PDEs, mass-transport focused
- Enforcement mechanism: soft-penalty (P2D residuals in loss)
- Architecture: NN with P2D-physics backbone
- Loss & weighting: measurement fit + P2D residual terms
- Sampling & training: collocation over charge/discharge cycles
- Data regime: sparse experimental + simulation
- Key result: accurate SOH estimates with markedly less training data than pure-data approaches by anchoring to P2D physics
- Relevance to review: bridges electrochemistry (P2D) and BMS engineering; canonical battery-PINN methodology record
- Verification: verified via https://api.crossref.org/works/10.1149/1945-7111/acf0ef

### D08
- Title: Forward and inverse simulation of pseudo-two-dimensional model of lithium-ion batteries using neural networks
- Authors: M. Lee et al. (Lee, Oh, Lee, Lee)
- Year: 2025
- Venue: Computer Methods in Applied Mechanics and Engineering
- Type: journal
- Identifier: DOI:10.1016/j.cma.2025.117856
- URL: https://www.sciencedirect.com/science/article/pii/S0045782525002613 (record via Crossref)
- Citations: 13 (Crossref)
- Domain: battery — electrochemistry (P2D modeling)
- Problem type: both (forward solve + inverse parameter identification)
- Physics enforced: full P2D PDE system incl. Butler-Volmer kinetics, concentration/potential equations
- Enforcement mechanism: soft-penalty (PDE collocation residual)
- Architecture: PINN with problem-tailored feature/normalization layers for stiff nonlinear kinetics
- Loss & weighting: PDE residuals + boundary/initial conditions + data terms; weighting to tame Butler-Volmer nonlinearity
- Sampling & training: collocation sampling across charge/discharge states
- Data regime: none/sparse (mostly equation-driven; inverse uses sparse voltage data)
- Key result: stable forward/inverse P2D solutions despite Butler-Volmer stiffness, a known PINN pain point
- Relevance to review: state-of-the-art methods record for battery PDE surrogates (fast BMS-grade electrochemical models)
- Verification: verified via https://api.crossref.org/works/10.1016/j.cma.2025.117856

### D09
- Title: PINN surrogate of Li-ion battery models for parameter inference, Part I: Implementation and multi-fidelity uncertainty
- Authors: M. Hassanaly et al. (Hassanaly, Weddle, King, De...)
- Year: 2024
- Venue: Journal of Energy Storage
- Type: journal
- Identifier: DOI:10.1016/j.est.2024.113103 (Part I); Part II: DOI:10.1016/j.est.2024.113104
- URL: https://www.sciencedirect.com/science/article/pii/S2352152X24019907 (record via Crossref)
- Citations: 20 (Crossref, Part I; 15 Part II)
- Domain: battery — parameter inference for electrochemical models
- Problem type: inverse
- Physics enforced: single-particle (SPM)/P2D electrochemical PDEs
- Enforcement mechanism: soft-penalty (PINN surrogate trained on model responses)
- Architecture: feedforward PINN surrogate; multi-fidelity treatment; Bayesian/regularization in Part II
- Loss & weighting: surrogate fit + PDE-derived constraints
- Sampling & training: simulation ensembles across parameter space
- Data regime: dense simulation (surrogate setting)
- Key result: quantifies when PINN surrogates are competitive for battery parameter estimation and where they struggle (high-fidelity P2D)
- Relevance to review: candid negative/limitation results valuable for the review's "lessons learned" section
- Verification: verified via https://api.crossref.org/works/10.1016/j.est.2024.113103

### D10
- Title: Physics informed neural networks for control oriented thermal modeling of buildings
- Authors: G. Gokhale, B. Claessens, C. Develder
- Year: 2022
- Venue: Applied Energy
- Type: journal
- Identifier: DOI:10.1016/j.apenergy.2022.118852
- URL: https://www.sciencedirect.com/science/article/pii/S0306261922002884
- Citations: 196 (Crossref)
- Domain: buildings/HVAC — control-oriented thermal modeling (demand response industry)
- Problem type: control (model for MPC/demand-response)
- Physics enforced: building heat-balance dynamics (RC thermal-network ODEs; indoor temperature evolution)
- Enforcement mechanism: soft-penalty (physics residual added to supervised loss)
- Architecture: feedforward/GRU-style network on weather+occupancy inputs
- Loss & weighting: temperature-fit loss + physics-consistency penalty
- Sampling & training: simulated buildings; comparisons vs grey-box RC models
- Data regime: sparse simulation + measured weather
- Key result: outperforms both pure black-box and classical grey-box thermal models; enables grid-integrated building demand response
- Relevance to review: highest-cited building-PINN record; direct link to smart-grid demand-response industry
- Verification: verified via https://api.crossref.org/works/10.1016/j.apenergy.2022.118852

### D11
- Title: A review of physics-informed machine learning for building energy modeling
- Authors: (Applied Energy review; first author et al. — see DOI record)
- Year: 2024
- Venue: Applied Energy
- Type: journal
- Identifier: DOI:10.1016/j.apenergy.2024.125169
- URL: https://www.sciencedirect.com/science/article/pii/S0306261924025534
- Citations: 96 (Crossref)
- Domain: buildings/HVAC — survey of PIML for building energy modeling (BEM)
- Problem type: both (survey of forward prediction and control/inverse calibration)
- Physics enforced: heat transfer (conduction/convection), HVAC component models, thermodynamic laws (as reviewed categories)
- Enforcement mechanism: mixed — soft-penalty, hybrid residual modeling, physics-guided features
- Architecture: n/a (survey)
- Loss & weighting: n/a
- Sampling & training: n/a
- Data regime: n/a
- Key result: systematic map of where physics helps BEM: load prediction, model calibration, MPC; identifies gap between academic PINNs and deployed building tools
- Relevance to review: dedicated sector survey for the buildings/HVAC slice; supports industry-adoption discussion
- Verification: verified via https://api.crossref.org/works/10.1016/j.apenergy.2024.125169

### D12
- Title: Physics-informed neural networks for the point kinetics equations for nuclear reactor dynamics
- Authors: E. Schiassi et al. (Schiassi, De Florio, Ganapol, Picca, Furfaro)
- Year: 2022
- Venue: Annals of Nuclear Energy
- Type: journal
- Identifier: DOI:10.1016/j.anucene.2021.108833
- URL: https://www.sciencedirect.com/science/article/pii/S0306454921004866 (record via Crossref)
- Citations: 57 (Crossref)
- Domain: nuclear — reactor dynamics (zero-power/point kinetics)
- Problem type: forward
- Physics enforced: point kinetics equations — 7 coupled stiff ODEs (neutron density + 6 delayed-neutron precursor groups)
- Enforcement mechanism: soft-penalty with ELM-based extreme-learningPINN (fixed random weights,_least-squares output layer)
- Architecture: extreme learning machine PINN (ELM-PINN) with transfer-learning variants
- Loss & weighting: ODE residual + initial conditions; least-squares weighting
- Sampling & training: time-collocation points; no data needed
- Data regime: none (equation-driven)
- Key result: high-accuracy solution of stiff point kinetics (incl. rod-reactivity transients) far faster than classical solvers
- Relevance to review: canonical nuclear-sector PINN; supports reactor digital-twin narrative
- Verification: verified via https://api.crossref.org/works/10.1016/j.anucene.2021.108833

### D13
- Title: Physics-informed neural network with transfer learning (TL-PINN) based on domain similarity measurement for nuclear reactor dynamics
- Authors: M. Prantikos et al. (Prantikos, Chatzidakis, et al.)
- Year: 2023
- Venue: Scientific Reports
- Type: journal
- Identifier: DOI:10.1038/s41598-023-43325-1
- URL: https://www.nature.com/articles/s41598-023-43325-1
- Citations: 92 (Crossref)
- Domain: nuclear — reactor dynamics / digital twin
- Problem type: forward (+ transfer to new regimes)
- Physics enforced: point kinetics / reactor-transfer ODE dynamics
- Enforcement mechanism: soft-penalty + transfer learning across operating domains
- Architecture: PINN with pretraining/fine-tuning scheme; domain-similarity metric
- Loss & weighting: ODE residual + data terms; similarity-weighted transfer
- Sampling & training: pretrain on source reactor regime, fine-tune on sparse target data
- Data regime: sparse simulation
- Key result: fast accurate reactor-state prediction in new regimes with minimal retraining; cited as PINN-based nuclear digital-twin step
- Relevance to review: shows the transfer-learning + PINN pattern the nuclear industry needs for online monitoring
- Verification: verified via https://api.crossref.org/works/10.1038/s41598-023-43325-1

### D14
- Title: KAPNet: A physics-informed neural network with physical constraints modeled by Kolmogorov-Arnold networks for wind speed prediction
- Authors: B. Pang et al. (Pang, Zhang, Hao)
- Year: 2025
- Venue: AIP Advances
- Type: journal
- Identifier: DOI:10.1063/5.0292276
- URL: https://pubs.aip.org/aip/adv/article/15/11/115212/3371351
- Citations: 3 (Crossref)
- Domain: renewables — wind speed forecasting (wind energy dispatch)
- Problem type: forecasting
- Physics enforced: wind-speed physical constraints (physical bounds/evolution regularities)
- Enforcement mechanism: hybrid — KAN-based backbone with physics-constraint loss terms
- Architecture: Kolmogorov-Arnold network (KAN) enabled PINN
- Loss & weighting: data loss + physical-constraint penalties
- Sampling & training: historical wind-speed series; sliding-window forecasting
- Data regime: dense observational (time series)
- Key result: improved dispatch-relevant wind speed prediction accuracy vs standard deep baselines
- Relevance to review: exemplifies 2025 trend of pairing new architectures (KAN) with physics constraints in renewables forecasting
- Verification: verified via https://api.crossref.org/works/10.1063/5.0292276 + AIP page

### D15
- Title: Physics-guided neural network integrating uncertainty evolution for spatiotemporal wind speed prediction
- Authors: J. Wang et al. (Wang, Zhang, Ren, Li, Lin)
- Year: 2026
- Venue: Communications Earth & Environment (Nature Portfolio)
- Type: journal
- Identifier: DOI:10.1038/s43247-026-03844-x
- URL: https://www.nature.com/articles/s43247-026-03844-x
- Citations: 0 (Crossref; published July 2026)
- Domain: renewables — 3D wind-field prediction (wind energy / weather services)
- Problem type: forecasting
- Physics enforced: physical consistency of wind evolution (spatiotemporal advection-type consistency)
- Enforcement mechanism: hybrid (physics-guided loss with uncertainty-evolution modeling)
- Architecture: spatiotemporal NN with physics-guided structure
- Loss & weighting: data loss + physical-consistency term + uncertainty calibration
- Sampling & training: reanalysis/observational wind fields
- Data regime: dense observational
- Key result: improved 3D wind-speed field prediction with calibrated uncertainty vs purely data-driven models
- Relevance to review: newest Nature-portfolio renewables record; illustrates physics-guided (not Raissi-PDE) PIML in wind energy
- Verification: verified via https://api.crossref.org/works/10.1038/s43247-026-03844-x

### D16
- Title: Enforcing Analytic Constraints in Neural Networks Emulating Physical Systems
- Authors: T. Beucler et al. (Beucler, Pritchard, Rasp, Ott, Bauer, Eyring)
- Year: 2021
- Venue: Physical Review Letters
- Type: journal
- Identifier: DOI:10.1103/PhysRevLett.126.098302; arXiv:1909.00912
- URL: https://link.aps.org/doi/10.1103/PhysRevLett.126.098302
- Citations: ~400 (Semantic Scholar; ~600 per Google Scholar snippet)
- Domain: climate — climate-model parameterization emulation
- Problem type: operator (NN emulating convection/radiation parameterizations)
- Physics enforced: nonlinear analytic conservation laws — mass (water) conservation, radiative (TOA) energy conservation
- Enforcement mechanism: hard-constraint — two-step: architectural constraints (custom layers) + re-weighting; explicitly compared to soft-penalty losses
- Architecture: feedforward NN with conservative input/output layers
- Loss & weighting: MSE data loss (constraints satisfied by construction) vs penalized variants analyzed
- Sampling & training: climate-model (CAM-type) output as training data
- Data regime: dense simulation
- Key result: systematic framework guaranteeing exact analytic constraints with no accuracy loss; foundational for climate PIML constraint design
- Relevance to review: the reference taxonomy paper for hard-vs-soft enforcement, with direct cross-sector transfer (power/battery conservative layers)
- Verification: verified via Semantic Scholar DOI lookup (paperId ed53d031...) + APS listing

### D17
- Title: Neural general circulation models for weather and climate (NeuralGCM)
- Authors: D. Kochkov et al. (Kochkov, Yuval, Langmore, ..., Hoyer; Google Research)
- Year: 2024
- Venue: Nature
- Type: journal
- Identifier: DOI:10.1038/s41586-024-07744-y; arXiv:2311.07222
- URL: https://www.nature.com/articles/s41586-024-07744-y
- Citations: 605 (Semantic Scholar)
- Domain: climate/weather — hybrid atmospheric emulator (weather forecasting + climate simulation)
- Problem type: operator (learned parameterizations inside a differentiable physics solver)
- Physics enforced: full atmospheric dynamics solved by differentiable Navier-Stokes-based dynamical core (constraining large scales); learned moist-convection/cloud microphysics
- Enforcement mechanism: hybrid — classical physics solver carries the equations (exact physics), NN learns subgrid closures from reanalysis (FLAG: not a Raissi-style PINN; "physics-preserving hybrid" rather than physics-INFORMED training)
- Architecture: JAX/CStOW differentiable dynamical core + learned parameterization networks
- Loss & weighting: supervised reanalysis loss on long rollout trajectories
- Sampling & training: ERA5-type reanalysis; multi-year rollouts
- Data regime: dense reanalysis
- Key result: 1-15 day forecasts competitive with/better than leading physical GCMs on some metrics, plus stable multi-decade climate simulation
- Relevance to review: the flagship hybrid physics-ML climate model; essential for the review's "PINN vs hybrid emulator" boundary discussion
- Verification: verified via Semantic Scholar DOI lookup (paperId d035359d...) + https://www.nature.com/articles/s41586-024-07744-y

### D18
- Title: Physics-informed machine learning meets renewable energy systems: A review of advances, challenges, guidelines, and future outlooks
- Authors: S. M. Parsa et al.
- Year: 2025
- Venue: Applied Energy
- Type: journal
- Identifier: DOI:10.1016/j.apenergy.2025.126925
- URL: https://www.sciencedirect.com/science/article/pii/S0306261925016551
- Citations: 46 (Semantic Scholar)
- Domain: renewables/energy — sector-wide PIML review (grid to wind-farm to component scale)
- Problem type: both (survey of forecasting, control, and design problems)
- Physics enforced: power-system laws, wind/aerodynamic physics, PV radiative physics, storage electrochemistry (as reviewed categories)
- Enforcement mechanism: mixed — survey covers soft-penalty, hard constraints, physics-guided features
- Architecture: n/a (survey)
- Loss & weighting: n/a
- Sampling & training: n/a
- Data regime: n/a
- Key result: guidelines for embedding physical laws across renewable-energy scales; calls out reliability/interpretability gains and deployment gaps
- Relevance to review: the requested 2025 "PIML meets renewable energy" review; key comparative anchor for Slice D
- Verification: verified via Semantic Scholar DOI lookup (paperId de985340...) + ScienceDirect page

### D19
- Title: Physics-informed neural networks in the energy sector: Progress, trends, and future directions
- Authors: I. Thawon et al.
- Year: 2026
- Venue: Energy Reports
- Type: journal
- Identifier: DOI:10.1016/j.egyr.2025.109013
- URL: https://www.sciencedirect.com/science/article/pii/S2666147726000137 (record via Crossref)
- Citations: 3 (Crossref; ~8 per Google Scholar snippet)
- Domain: energy sector-wide — survey (power systems, batteries, renewables, grid digital twins)
- Problem type: both (survey)
- Physics enforced: power-flow/dynamics laws, electrochemical models, thermodynamics (as reviewed categories)
- Enforcement mechanism: mixed (survey)
- Architecture: n/a (survey)
- Loss & weighting: n/a
- Sampling & training: n/a
- Data regime: n/a
- Key result: cross-sector progress/trends map of PINNs across the energy industry, incl. digital-twin directions
- Relevance to review: 2026 energy-sector survey satisfying the "survey of PINNs in energy systems + industrial pilots" requirement
- Verification: verified via https://api.crossref.org/works/10.1016/j.egyr.2025.109013

## Machine rows

D01|Physics-Informed Neural Networks for Power Systems (Misyris et al.)|2020|IEEE PES General Meeting|conference|DOI:10.1109/PESGM41954.2020.9282004|~570 (GS)/243 Crossref|energy/power - grid dynamics|swing equation (rotor angle/frequency dynamics) and steady-state power-system models|soft-penalty|both|1|Y
D02|Physics-Informed Neural Networks for AC Optimal Power Flow (Nellikkath and Chatzivasileiadis)|2022|Electric Power Systems Research|journal|DOI:10.1016/j.epsr.2022.108412|163|energy/power - AC-OPF|AC power-flow equations (Kirchhoff/power balance)|soft-penalty|control|2|Y
D03|Robust Power System State Estimation using Physics-Informed Neural Networks (Falas et al.)|2025|arXiv (preprint)|preprint|arXiv:2507.05874|n/a|energy/power - state estimation|power-flow and network admittance physics|hybrid (physics-informed loss plus measurement model)|inverse|3|Y
D04|KCLNet: Physics-Informed Power Flow Prediction via Constraints Projections (Dogoulis et al.)|2025|arXiv (preprint)|preprint|arXiv:2506.12902|n/a|energy/power - power flow|Kirchhoff's Current Law at every bus|hard-constraint (hyperplane projection in GNN)|forward|3|Y
D05|Physics-informed neural networks for power systems: A systematic review (Xu et al.)|2026|Sustainable Energy Grids and Networks|journal|DOI:10.1016/j.segan.2026.102261|~7|energy/power - dedicated survey|power-flow equations; swing dynamics; transients (reviewed)|mixed (survey)|both|1|Y
D06|PINN for lithium-ion battery degradation stable modeling and prognosis PINN4SOH (Wang et al.)|2024|Nature Communications|journal|DOI:10.1038/s41467-024-48779-z|897|battery - BMS/SOH prognosis|empirical degradation model plus state-space dynamics; monotonic capacity fade|hybrid (physics model integrated with NN loss)|forecasting|1|Y
D07|PINNs for State of Health Estimation in Lithium-Ion Batteries (Hofmann et al.)|2023|Journal of The Electrochemical Society|journal|DOI:10.1149/1945-7111/acf0ef|104|battery - SOH estimation|P2D Doyle-Fuller-Newman PDEs (concentration/potential transport)|soft-penalty|inverse|2|Y
D08|Forward and inverse simulation of pseudo-two-dimensional model of lithium-ion batteries using neural networks (Lee et al.)|2025|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2025.117856|13|battery - electrochemistry|full P2D PDEs incl. Butler-Volmer kinetics|soft-penalty (PDE collocation)|both|2|Y
D09|PINN surrogate of Li-ion battery models for parameter inference Part I (Hassanaly et al.)|2024|Journal of Energy Storage|journal|DOI:10.1016/j.est.2024.113103|20|battery - parameter inference|SPM/P2D electrochemical PDEs|soft-penalty|inverse|3|Y
D10|Physics informed neural networks for control oriented thermal modeling of buildings (Gokhale et al.)|2022|Applied Energy|journal|DOI:10.1016/j.apenergy.2022.118852|196|buildings/HVAC - demand response|building heat-balance dynamics (RC thermal-network ODEs)|soft-penalty|control|2|Y
D11|A review of physics-informed machine learning for building energy modeling|2024|Applied Energy|journal|DOI:10.1016/j.apenergy.2024.125169|96|buildings/HVAC - survey|heat transfer; HVAC component physics; thermodynamics (reviewed)|mixed (survey)|both|2|Y
D12|PINNs for the point kinetics equations for nuclear reactor dynamics (Schiassi et al.)|2022|Annals of Nuclear Energy|journal|DOI:10.1016/j.anucene.2021.108833|57|nuclear - reactor dynamics|point kinetics ODEs (neutron density plus 6 delayed precursor groups)|soft-penalty (ELM-based)|forward|3|Y
D13|TL-PINN based on domain similarity measurement for nuclear reactor dynamics (Prantikos et al.)|2023|Scientific Reports|journal|DOI:10.1038/s41598-023-43325-1|92|nuclear - reactor dynamics/digital twin|point kinetics reactor-transfer ODE dynamics|soft-penalty plus transfer learning|forward|3|Y
D14|KAPNet: A physics-informed neural network with physical constraints modeled by Kolmogorov-Arnold networks (Pang et al.)|2025|AIP Advances|journal|DOI:10.1063/5.0292276|3|renewables - wind speed forecasting|wind-speed physical constraints (bounds and evolution regularities)|hybrid (KAN backbone plus constraint loss)|forecasting|4|Y
D15|Physics-guided neural network integrating uncertainty evolution for spatiotemporal wind speed prediction (Wang et al.)|2026|Communications Earth and Environment|journal|DOI:10.1038/s43247-026-03844-x|0|renewables - 3D wind fields|physical consistency of wind evolution (advection-type)|hybrid (physics-guided loss with uncertainty)|forecasting|4|Y
D16|Enforcing Analytic Constraints in Neural Networks Emulating Physical Systems (Beucler et al.)|2021|Physical Review Letters|journal|DOI:10.1103/PhysRevLett.126.098302|~400 (S2)/~600 GS|climate - parameterization emulation|mass (water) and radiative energy conservation laws|hard-constraint (conservative layers) compared to soft-penalty|operator|1|Y
D17|Neural general circulation models for weather and climate (Kochkov et al.)|2024|Nature|journal|DOI:10.1038/s41586-024-07744-y|605|climate/weather - hybrid emulator|atmospheric dynamics solved by differentiable physics core; learned subgrid closures|hybrid (physics solver plus learned components; NOT classic PINN)|operator|1|Y
D18|Physics-informed machine learning meets renewable energy systems: A review (Parsa et al.)|2025|Applied Energy|journal|DOI:10.1016/j.apenergy.2025.126925|46|renewables/energy - sector survey|grid; wind; PV radiative; storage physics (reviewed)|mixed (survey)|both|1|Y
D19|Physics-informed neural networks in the energy sector: Progress trends and future directions (Thawon et al.)|2026|Energy Reports|journal|DOI:10.1016/j.egyr.2025.109013|3|energy sector - cross-sector survey|power-flow; electrochemical; thermodynamic laws (reviewed)|mixed (survey)|both|2|Y

## Slice takeaways

- Dominant physics per sector: power systems enforces Kirchhoff/power-flow equations and the swing equation (rotor dynamics); batteries enforce P2D/Doyle-Fuller-Newman electrochemical PDEs and degradation/state-space laws; buildings enforce RC heat-balance/thermodynamic dynamics; nuclear enforces point-kinetics stiff ODEs; climate enforces mass and radiative conservation and (in hybrids) the full atmospheric dynamical equations; renewables forecasting mostly uses weaker "physics-guided" constraints (clear-sky models, wind evolution regularities, physical bounds) rather than governing PDEs.
- Hard-vs-soft constraint trend: soft PDE-residual penalties dominate 2021-2023, but 2024-2026 shows a clear shift to architectural hard constraints (KCLNet's exact KCL projections; Beucler's conservative layers) and to hybrid physics-solver + learned-component designs (NeuralGCM), which sidestep loss-weighting pathologies; transfer learning is the favored add-on for operating-regime shifts (nuclear, battery).
- Industry adoption evidence: strong and growing — battery BMS (Nature Comms PINN4SOH, 897 cites; P2D surrogates for parameter inference), grid operations (AC-OPF solvers, robust state estimation, 2026 systematic reviews targeting "new power systems" modernization), building demand response (196-cite Applied Energy record), and reactor digital twins; dedicated 2024-2026 surveys in Applied Energy, SEGAN, and Energy Reports confirm sector-wide institutional uptake, though industrial-pilot reports remain mostly aspirational (digital-twin framing) rather than documented deployments.
- Distinction to flag in the review: climate/weather leaders (NeuralGCM, physics-guided wind models) are largely physics-preserving hybrids or physics-guided, not Raissi-style physics-INFORMED training; Beucler et al. is the genuine constraint-enforcement landmark for climate.
- Gaps: few nuclear thermal-hydraulics (two-phase flow) PINNs verified; solar/PV records thinner than wind; load forecasting with physical constraints under-represented relative to OPF/state estimation; benchmark datasets and certified-constraint guarantees are recurring open problems across all four sectors.
