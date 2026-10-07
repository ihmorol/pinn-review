# Slice F: Materials, manufacturing, finance, and industrial ecosystem

## Queries used
1. physics-informed neural networks additive manufacturing melt pool review
2. Goswami transfer learning enhanced physics-informed neural networks phase field modeling fracture CMAME
3. physics-informed neural networks option pricing Black-Scholes 2023 2024
4. physics-informed neural networks manufacturing survey 2024 2025 Vidyarthi
5. Goswami physics-informed neural networks phase field modeling fracture transfer learning CMAME 2020
6. Montes de Oca Zapiain Stewart Dingreville physics-informed neural networks microstructure evolution npj Computational Materials
7. NVIDIA Modulus PhysicsNeMo physics-ML industrial deployment case study
8. physics-informed neural networks elastoplasticity path-dependent constitutive solid mechanics journal
9. Vidyarthi physics-informed machine learning manufacturing review survey
10. physics-informed deep learning Hamilton-Jacobi-Bellman option pricing local volatility Quantitative Finance
11. Faegh "physics-informed machine learning" additive manufacturing process monitoring review Journal of Intelligent Manufacturing 2025

## Screening summary
candidates screened: ~25; included: 15 (13 papers + 2 vendor webpages, allowed only for slice d)
Notes: no dedicated "Vidyarthi et al." manufacturing survey could be verified (dropped). The Goswami phase-field fracture paper is in Theoretical and Applied Fracture Mechanics (not CMAME as commonly miscited). Montes de Oca Zapiain et al. is a data-driven CNN surrogate of Cahn-Hilliard phase-field, not a residual-based PINN (kept with caveat). A dedicated 2021-2026 journal PINN option-pricing paper could not be verified under rate limits; finance covered by DGM (2018) + HJB (2021) + MathWorks example (marked). Crystal plasticity PINN and dedicated welding PINN papers were not verified in time — gap flagged.

## Paper records

### F01
- Title: Transfer learning enhanced physics informed neural network for phase-field modeling of fracture / Goswami, Anitescu, Chakraborty, Rabczuk / 2020 / Theoretical and Applied Fracture Mechanics / journal / DOI 10.1016/j.tafmec.2019.102447 / https://doi.org/10.1016/j.tafmec.2019.102447 / Citations 888 (Semantic Scholar)
- Domain: brittle fracture phase-field modeling (materials/solid mechanics; civil-mechanical engineering)
- Problem type: forward (initial/boundary value, crack propagation)
- Physics enforced: coupled phase-field evolution PDE + quasi-static brittle fracture energy balance (elastic energy release driving crack phase-field)
- Enforcement mechanism: PDE residual in loss; transfer learning from intact-material solution
- Architecture: fully connected MLP / Loss: phase-field + elasticity residuals / Sampling: collocation on cracked-domain subdomains / Data: physics-only, transfer-pretrained
- Key result: transfer learning cuts training cost vs training from scratch on fracture configs. / Relevance: canonical materials PINN, anchor for fracture/phase-field section. / Verification: verified via Semantic Scholar (paperId d14055cee)

### F02
- Title: Accelerating phase-field-based microstructure evolution predictions via surrogate models trained by machine learning methods / Montes de Oca Zapiain, Stewart, Dingreville / 2021 / npj Computational Materials / journal / DOI 10.1038/s41524-020-00471-8 / https://www.nature.com/articles/s41524-020-00471-8 / Citations 233 (Semantic Scholar)
- Domain: microstructure evolution (spinodal decomposition) — materials/metallurgy industry
- Problem type: operator-like surrogate (forward evolution emulation)
- Physics enforced: Cahn-Hilliard phase-field equations — via data only (CAVEAT: data-driven CNN surrogate, NOT a residual-based PINN)
- Enforcement mechanism: supervised learning on phase-field simulation snapshots (no PDE residual)
- Architecture: CNN (U-Net style) / Loss: snapshot MSE / Sampling: curated training trajectories / Data: simulation-generated labeled microstructure sequences
- Key result: predicts two-phase microstructure evolution in seconds, bypassing on-the-fly Cahn-Hilliard solves. / Relevance: defines the PIML-adjacent baseline that residual-based PINN microstructure works claim to improve. / Verification: verified via Semantic Scholar API

### F03
- Title: Machine learning for metal additive manufacturing: predicting temperature and melt pool fluid dynamics using physics-informed neural networks / Zhu, Liu, Yan / 2020 / Computational Mechanics / journal / DOI 10.1007/s00466-020-01952-9 / https://doi.org/10.1007/s00466-020-01952-9 / Citations 465 (Semantic Scholar)
- Domain: metal additive manufacturing melt pool (manufacturing/3D-printing industry)
- Problem type: forward + transfer to new process parameters
- Physics enforced: melt-pool heat transport (conduction/advection) + incompressible Navier-Stokes for melt flow
- Enforcement mechanism: PDE residual loss; transfer learning to new operating points
- Architecture: fully connected MLP / Loss: PDE + data residuals / Sampling: spatio-temporal collocation / Data: small labeled CFD/experimental melt-pool data
- Key result: accurate melt pool geometry and temperature fields with far less data than purely data-driven CNNs. / Relevance: foundational AM melt-pool PINN, benchmark for all later AM-PIML work. / Verification: verified via Semantic Scholar (paperId 68f691a4)

### F04
- Title: A physics-informed deep neural network for surrogate modeling in classical elasto-plasticity / Eghbalian, Pouragha, Wan / 2022 (journal version Computers and Geotechnics 2023) / Computers and Geotechnics / journal / arXiv 2204.12088 / https://arxiv.org/abs/2204.12088 / Citations 103 (Semantic Scholar)
- Domain: soil/rock and solid elasto-plasticity (geomechanics, civil engineering)
- Problem type: forward surrogate (stress prediction from strain paths)
- Physics enforced: incremental elasticity + additive strain decomposition + plastic-flow admissibility (classical J2-type elastoplasticity)
- Enforcement mechanism: physics-constrained loss (EPNN): elasticity residual + yield/consistency terms
- Architecture: recurrent-style DNN over strain increments / Loss: constitutive residual + soft constraints / Sampling: strain-path batches / Data: synthetic elasto-plastic response data
- Key result: EPNN generalizes to unseen complex strain paths while respecting yield behavior. / Relevance: representative elastoplasticity PINN with constitutive-law embedding. / Verification: verified via arXiv page + Semantic Scholar (paperId 9edc6311)

### F05
- Title: Physics-informed neural network frameworks in strong and weak forms for elastoplastic analysis / (authors n/a — S2 rate-limited) / 2026 / Applied Mathematical Modelling / journal / DOI 10.1016/j.apm.2026.116968 / https://www.sciencedirect.com/science/article/pii/S0307904X26002295 / Citations 6 (Semantic Scholar)
- Domain: small-strain von Mises elastoplasticity (mechanical/civil engineering)
- Problem type: forward (boundary value problem with material nonlinearity)
- Physics enforced: equilibrium PDE + von Mises (J2) elastoplastic flow theory (yield surface, flow rule)
- Enforcement mechanism: two frameworks — strong-form PDE residual and weak-form (virtual work) loss
- Architecture: MLP / Loss: strong/weak residual + constitutive terms / Sampling: collocation vs weak-form quadrature / Data: physics-only
- Key result: weak-form PINN handles material nonlinearity more stably than strong form for elastoplasticity. / Relevance: current (2026) statement of how elastoplastic physics is enforced in PINNs. / Verification: verified via Semantic Scholar (paperId cfbf8e86)

### F06
- Title: Plasolver: Physics-Informed Neural Operators for Elastoplasticity / (authors n/a) / 2026 / arXiv / preprint / arXiv 2608.15157 / https://arxiv.org/abs/2608.15157 / Citations n/a
- Domain: elastoplastic analysis (mechanical engineering / materials)
- Problem type: operator (parametric path-dependent constitutive behavior)
- Physics enforced: elastoplastic equilibrium with nonlinear path-dependent constitutive relations
- Enforcement mechanism: physics-informed neural operator (residual + operator learning)
- Architecture: neural operator / Loss: PDE + constitutive residuals / Sampling: n/a (preprint details) / Data: physics + solver reference
- Key result: combines operator-learning speed with classical solver robustness for plasticity. / Relevance: signals 2026 shift from PINN to physics-informed operators in solid mechanics. / Verification: verified: partial (arXiv listing from search results)

### F07
- Title: A review on physics-informed machine learning for monitoring metal additive manufacturing process / Yang, Shoulan et al. / 2024 / Advanced Manufacturing / journal / DOI 10.55092/am2024008 / https://doi.org/10.55092/am2024008 / Citations 27 (Semantic Scholar)
- Domain: metal AM process monitoring (manufacturing industry)
- Problem type: review (forward/inverse monitoring applications)
- Physics enforced: surveyed thermal/heat-transfer and melt-pool physics embedded in PIML monitors
- Enforcement mechanism: taxonomy of PDE-residual, hybrid, and physics-constrained losses (survey)
- Architecture: n/a (survey) / Loss: n/a / Sampling: n/a / Data: n/a
- Key result: maps PIML methods onto in-situ monitoring tasks for metal AM. / Relevance: manufacturing-survey anchor for the AM industry section. / Verification: verified via Semantic Scholar search

### F08
- Title: A review on physics-informed machine learning for process-structure-property modeling in additive manufacturing / Faegh, Ghungrad, et al. / 2025 / venue needs-check (institutional record: NOVA Lisbon repository) / journal / Identifier n/a / https://run.unl.pt / Citations ~135 (search snippet estimate)
- Domain: metal AM process-structure-property chain (manufacturing industry)
- Problem type: review
- Physics enforced: surveyed thermomechanical (heat transfer, stress) principles embedded in AM PIML
- Enforcement mechanism: survey of residual, hybrid, and architecture-embedded physics (reports 15-40% gains from physics embedding)
- Architecture: n/a / Loss: n/a / Sampling: n/a / Data: n/a
- Key result: quantifies benefit of embedding physics in AM process-structure-property models. / Relevance: highest-visibility recent AM PIML review; must-read for manufacturing section. / Verification: verified: partial (2 independent search hits; venue unconfirmed)

### F09
- Title: Review of physics-informed machine learning in laser metal additive manufacturing: a process-lifecycle perspective / Yeo, Taegyeong et al. / 2026 / Virtual and Physical Prototyping / journal / DOI 10.1080/17452759.2026.2724699 / https://doi.org/10.1080/17452759.2026.2724699 / Citations 0 (Semantic Scholar, very new)
- Domain: laser metal AM, full process lifecycle (manufacturing industry)
- Problem type: review
- Physics enforced: surveyed melt-pool thermal/fluid physics across lifecycle stages (design-to-inspection)
- Enforcement mechanism: lifecycle taxonomy of PIML approaches (survey)
- Architecture: n/a / Loss: n/a / Sampling: n/a / Data: n/a
- Key result: organizes PIML for laser AM by process lifecycle rather than by method. / Relevance: freshest (2026) manufacturing review; shows survey framing conventions. / Verification: verified via Semantic Scholar search

### F10
- Title: DGM: A deep learning algorithm for solving partial differential equations / Sirignano, Spiliopoulos / 2018 / Journal of Computational Physics / journal / DOI 10.1016/j.jcp.2018.08.029 / https://doi.org/10.1016/j.jcp.2018.08.029 / Citations 2673 (Semantic Scholar)
- Domain: general nonlinear PDEs; foundation for finance PDE solvers (quantitative finance)
- Problem type: forward
- Physics enforced: governing PDE residual (diffusion-reaction type: Burgers, Allen-Cahn, elliptic); template used for Black-Scholes-type extensions
- Enforcement mechanism: deep Galerkin — network ansatz plugged into PDE residual, optimized by SGD
- Architecture: DGM layer architecture / Loss: PDE residual + boundary/initial data / Sampling: collocation points from domain / Data: physics-only
- Key result: demonstrated scalable PDE solving via DGM architecture; basis of most finance PINN variants. / Relevance: foundational enforcement-mechanism reference for the finance section. / Verification: verified via Semantic Scholar API

### F11
- Title: Adaptive Deep Learning for High Dimensional Hamilton-Jacobi-Bellman Equations / Nakamura-Zimmerer, Gong, Kang / 2021 / SIAM Journal on Scientific Computing / journal / DOI 10.1137/19M1288802 / https://doi.org/10.1137/19M1288802 / Citations 169 (Semantic Scholar)
- Domain: HJB optimal control / stochastic control (finance, robotics)
- Problem type: forward (semiglobal value-function solve)
- Physics enforced: high-dimensional Hamilton-Jacobi-Bellman PDE (value-function dynamics)
- Enforcement mechanism: HJB residual + terminal data loss with adaptive collocation sampling
- Architecture: feedforward NN per time slice / Loss: HJB residual / Sampling: adaptive sampling concentrated on solution features / Data: physics-only
- Key result: semiglobal solutions of HJB in up to hundreds of dimensions. / Relevance: bridges PINN enforcement to optimal execution/portfolio-control finance problems. / Verification: verified via Semantic Scholar (paperId af857259)

### F12
- Title: DeepXDE: A Deep Learning Library for Solving Differential Equations / Lu, Lu; Pestourie, Yao, Wang, Verdugo, Johnson / 2021 / SIAM Review / journal / DOI 10.1137/19M1274067 / https://doi.org/10.1137/19M1274067 / Citations 2498 (Semantic Scholar, merged record incl. 2019 preprint)
- Domain: general PINN software (cross-industry)
- Problem type: deployment (library: forward/inverse, hard-constraint)
- Physics enforced: user-specified PDE residuals (heat, wave, elasticity, etc.)
- Enforcement mechanism: automatic-differentiation residuals with hard/soft BC constraints, collocation sampling
- Architecture: pluggable PyTorch/TensorFlow backends / Loss: PDE + BC + data residuals / Sampling: built-in collocation / Data: sparse-data inverse supported
- Key result: de-facto standard open PINN library used across industry and academia. / Relevance: core ecosystem entry for the software section. / Verification: verified via Semantic Scholar API

### F13
- Title: SciANN: A Keras/TensorFlow wrapper for scientific computations and physics-informed deep learning using artificial neural networks / Haghighat, Juanes / 2020 (CMAME issue 2021) / Computer Methods in Applied Mechanics and Engineering / journal / DOI 10.1016/j.cma.2020.113552 / https://doi.org/10.1016/j.cma.2020.113552 / Citations 394 (Semantic Scholar)
- Domain: PINN software; used for solid mechanics (elastoplasticity, phase-field) studies (cross-industry)
- Problem type: deployment (library: functional PINN composition)
- Physics enforced: user-defined governing equations via functional API
- Enforcement mechanism: functional composition of NN and PDE residuals in Keras/TensorFlow
- Architecture: Keras functional MLPs / Loss: assembled residual terms / Sampling: collocation / Data: physics or data-driven
- Key result: widely used wrapper behind several landmark solid-mechanics PINN papers. / Relevance: second core ecosystem entry alongside DeepXDE. / Verification: verified via Semantic Scholar API

### F14
- Title: NVIDIA PhysicsNeMo (successor to NVIDIA Modulus) / NVIDIA / 2024-2026 / NVIDIA developer site + GitHub / webpage / https://github.com/NVIDIA/physicsnemo / Citations n/a
- Domain: physics-ML framework for industrial engineering simulation (energy, aerospace, manufacturing)
- Problem type: deployment
- Physics enforced: configurable PDE residuals (PINN, FNO, and hybrid physics-ML architectures)
- Enforcement mechanism: framework support — residual losses, hard constraints, operators at GPU scale
- Architecture: PyTorch framework / Loss: configurable / Sampling: configurable / Data: industrial simulation + sensor data
- Key result: industrial case study — Siemens Energy digital twins for the power industry using PhysicsNeMo + Omniverse (GTC talk). / Relevance: what industry actually deploys; anchor of ecosystem section. / Verification: verified: partial (developer.nvidia.com + GitHub via search)

### F15
- Title: Physics-Informed Neural Networks for Option Pricing (MATLAB example) / MathWorks / 2024 / MathWorks documentation / webpage / https://uk.mathworks.com (Deep Learning Toolbox examples) / Citations n/a
- Domain: option pricing (finance industry)
- Problem type: pricing (forward Black-Scholes solve)
- Physics enforced: Black-Scholes PDE residual
- Enforcement mechanism: PDE residual + boundary/terminal condition losses in MATLAB
- Architecture: MLP (Deep Learning Toolbox) / Loss: residual + data / Sampling: collocation / Data: physics-only
- Key result: vendor-tutorial evidence that PINN pricing is now mainstreamed into industrial toolchains. / Relevance: ecosystem indicator for finance adoption. / Verification: verified: partial (MathWorks listing via search)

## Machine rows
F01|Transfer learning enhanced physics informed neural network for phase-field modeling of fracture|2020|Theoretical and Applied Fracture Mechanics|journal|10.1016/j.tafmec.2019.102447|888|Fracture-phase-field materials|Phase-field evolution PDE + quasi-static brittle fracture energy balance|PDE residual loss with transfer learning from intact material|forward|1|Y
F02|Accelerating phase-field-based microstructure evolution predictions via surrogate models trained by machine learning methods|2021|npj Computational Materials|journal|10.1038/s41524-020-00471-8|233|Microstructure evolution materials|Cahn-Hilliard spinodal decomposition (data-driven surrogate not residual PINN)|Supervised CNN on phase-field snapshots (no residual)|operator|2|Y
F03|Machine learning for metal additive manufacturing: predicting temperature and melt pool fluid dynamics using physics-informed neural networks|2020|Computational Mechanics|journal|10.1007/s00466-020-01952-9|465|Melt pool additive manufacturing|Heat transport + incompressible Navier-Stokes for melt pool|PDE residual loss plus transfer learning to new parameters|forward|1|Y
F04|A physics-informed deep neural network for surrogate modeling in classical elasto-plasticity|2022|Computers and Geotechnics|journal|arXiv:2204.12088|103|Elastoplasticity geomechanics|Incremental elasticity + additive strain decomposition + plastic admissibility|Physics-constrained loss (EPNN) on constitutive residuals|forward|2|Y
F05|Physics-informed neural network frameworks in strong and weak forms for elastoplastic analysis|2026|Applied Mathematical Modelling|journal|10.1016/j.apm.2026.116968|6|von Mises elastoplasticity|Equilibrium PDE + von Mises J2 flow theory|Strong-form residual and weak-form virtual-work losses|forward|2|Y
F06|Plasolver: Physics-Informed Neural Operators for Elastoplasticity|2026|arXiv|preprint|arXiv:2608.15157|n/a|Elastoplasticity|Elastoplastic equilibrium with path-dependent constitutive laws|Physics-informed neural operator residuals|operator|3|N
F07|A review on physics-informed machine learning for monitoring metal additive manufacturing process|2024|Advanced Manufacturing|journal|10.55092/am2024008|27|AM process monitoring|Surveyed thermal and melt-pool physics in PIML monitors|Survey of residual and hybrid enforcement|deployment|3|Y
F08|A review on physics-informed machine learning for process-structure-property modeling in additive manufacturing|2025|venue needs-check|journal|n/a|~135|AM process-structure-property|Surveyed thermomechanical heat transfer and stress physics|Survey of residual and architecture-embedded physics|deployment|1|N
F09|Review of physics-informed machine learning in laser metal additive manufacturing: a process-lifecycle perspective|2026|Virtual and Physical Prototyping|journal|10.1080/17452759.2026.2724699|0|Laser AM lifecycle|Surveyed melt-pool thermal-fluid physics across lifecycle|Lifecycle taxonomy of PIML enforcement|deployment|4|Y
F10|DGM: A deep learning algorithm for solving partial differential equations|2018|Journal of Computational Physics|journal|10.1016/j.jcp.2018.08.029|2673|Finance/general PDEs|PDE residual (diffusion-reaction: Burgers Allen-Cahn elliptic)|Deep Galerkin residual minimization by SGD|forward|2|Y
F11|Adaptive Deep Learning for High Dimensional Hamilton-Jacobi-Bellman Equations|2021|SIAM Journal on Scientific Computing|journal|10.1137/19M1288802|169|Optimal control finance|Hamilton-Jacobi-Bellman PDE for value function|HJB residual loss with adaptive collocation sampling|forward|2|Y
F12|DeepXDE: A Deep Learning Library for Solving Differential Equations|2021|SIAM Review|journal|10.1137/19M1274067|2498|PINN software ecosystem|User-specified PDE residuals (heat wave elasticity)|Autodiff residuals with hard and soft BC constraints|deployment|1|Y
F13|SciANN: A Keras/TensorFlow wrapper for scientific computations and physics-informed deep learning using artificial neural networks|2020|Computer Methods in Applied Mechanics and Engineering|journal|10.1016/j.cma.2020.113552|394|PINN software ecosystem|User-defined governing equations via functional API|Functional composition of NN and PDE residuals in Keras|deployment|3|Y
F14|NVIDIA PhysicsNeMo (successor to Modulus)|2024|NVIDIA developer site + GitHub|webpage|https://github.com/NVIDIA/physicsnemo|n/a|Industrial physics-ML framework|Configurable PDE residuals (PINN FNO hybrid)|Framework support for residual and operator losses at GPU scale|deployment|3|N
F15|Physics-Informed Neural Networks for Option Pricing|2024|MathWorks documentation|webpage|https://uk.mathworks.com|n/a|Option pricing finance|Black-Scholes PDE residual|Residual plus boundary and terminal condition losses|pricing|5|N

## Slice takeaways
- Materials/manufacturing is dominated by residual-based PINNs for melt-pool thermal-fluid physics (Zhu 2020) and phase-field fracture (Goswami 2020, actually in Theoretical and Applied Fracture Mechanics, not CMAME), with transfer learning the recurring enabler for parametric reuse.
- Elastoplasticity enforcement has matured from data-supervised constitutive surrogates (EPNN 2022) toward explicit J2 flow-theory residuals in strong AND weak (virtual-work) forms by 2026, and from PINNs toward physics-informed neural operators (Plasolver 2026).
- Additive manufacturing now has its own PIML review layer (Yang 2024, Faegh 2025 ~135 cites, Yeo 2026 lifecycle review) — use these to frame the manufacturing industry section rather than re-surveying primary papers.
- Finance enforcement is equation-driven: DGM residual minimization (2018) and adaptive-sampling HJB residuals (SIAM J. Sci. Comput. 2021) remain the verified core; no dedicated 2021-2026 journal option-pricing PINN survived verification (gap to re-run).
- The industrial ecosystem is anchored by DeepXDE (SIAM Review, 2498 cites) and SciANN (CMAME, 394 cites) as method libraries and NVIDIA Modulus→PhysicsNeMo as the deployment vehicle, with Siemens Energy power-industry digital twins as the flagship industrial case study; vendor evidence (PhysicsNeMo, MathWorks Black-Scholes example) is webpage-type and marked as such.
