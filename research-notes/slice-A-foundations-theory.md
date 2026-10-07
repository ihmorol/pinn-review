# Slice A: Foundations, theory, and training methodology

Scout A of 7 — verified paper dossier for the PINN survey targeting Springer *Artificial Intelligence Review*.
Verification date: 2026-10-06. Verification tools: Semantic Scholar API (rate-limited; 2 records verified), Crossref API (9 records), arXiv abs pages (10 records), plus web-search cross-checks.

## Queries used

1. Physics-informed neural networks Raissi Perdikaris Karniadakis 2019 Journal of Computational Physics
2. Mishra Molinaro estimates on the generalization error of physics-informed neural networks solving PDEs
3. Krishnapriyan characterizing possible failure modes in physics-informed neural networks NeurIPS 2021 curriculum
4. Wang Teng Perdikaris "Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks" SIAM
5. Wang Wang Perdikaris "On the eigenvector bias of Fourier feature networks" computer methods applied mechanics engineering
6. "When and why PINNs fail to train" Journal of Computational Physics 2022 spectral bias stiffness
7. McClenny Braga-Neto self-adaptive physics-informed neural networks soft attention weights
8. Nabian Gladisch "Radar" adaptive sampling physics-informed neural networks residual-based adaptive refinement
9. Lu Menghini Karniadakis DeepXDE deep learning library differential equations SIAM Review 2021
10. "An expert's guide to training physics-informed neural networks" 2023 arXiv
11. PINNacle comprehensive benchmark physics-informed neural networks NeurIPS 2023 datasets
12. PDEBench extensive benchmark scientific machine learning NeurIPS 2022 Takamoto
13. Grossmann Komorowska Latz "Can physics-informed neural networks beat the finite element method" IMA Journal Applied Mathematics
14. De Ryck Mishra generic bounds on the robustness certification physics-informed neural networks inverse problems
15. De Ryck Mishra "Numerical analysis of physics-informed neural networks and related models" Acta Numerica 2024
16. "Respecting causality" training physics-informed neural networks Wang Sankaran Perdikaris ICML 2024
17. physics-informed neural networks survey review 2025 training loss balancing advances
18. NVIDIA Modulus PhysicsNeMo framework physics-ML open source 2025
19. SciANN Keras wrapper scientific computations physics-informed Haghighat Juanes paper journal
20. PDEArena neural PDE solvers benchmark ICLR 2022 Gupta Brandstetter
21. physics-informed neural networks convergence theory 2026 generalization error bounds recent advances
22. PINN training challenges 2025 adaptive sampling loss weighting empirical study benchmark evaluation arXiv
23. Luo "Physics-informed neural networks for PDE problems" National Science Open 2025 review
24. physics-informed neural networks loss weighting training 2025 CMAME "Journal of Computational Physics" adaptive NTK new method
25. Nabian Gladisch "RADAR" "Residual-based Adaptive Refinement" arXiv Siemens PINN sampling
26. Wu "A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks" CMAME volume DOI
27. "Generic bounds on the approximation error for physics-informed" De Ryck Mishra proceedings NeurIPS 2022 hash
28. "Numerical analysis of physics-informed neural networks and related models in physics-informed machine learning" De Ryck Mishra Acta Numerica doi cambridge
29. Luo "Physics-informed neural networks for PDE problems: a comprehensive review" "Artificial Intelligence Review" volume 58 doi 10.1007

## Screening summary

candidates screened: 26; included: 19; exclusion reasons: scope (PDEArena — operator-learning benchmark, overlaps scout B; kept as a note only), unverified (RADAR/Nabian-Gladisch — no verifiable record found; dropped, never fabricated), marginal (ASW-PINN 2025; "Self-adaptive weighting and sampling" arXiv Nov-2025 — overlapping scope, weaker venues), irrelevant (2 mis-guessed arXiv/DOI hits rejected during verification).

Note on NVIDIA Modulus/PhysicsNeMo and jaxpi: no canonical peer-reviewed paper found for either (PhysicsNeMo is NVIDIA's renamed Modulus framework, GitHub NVIDIA/physicsnemo, active through 2026; jaxpi is the JAX library accompanying A10). Cite as software, not as papers.

## Paper records

### A01
- Title: Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations
- Authors: Maziar Raissi, Paris Perdikaris, George Em Karniadakis
- Year: 2019 (ANCHOR — pre-2021, 1 of max 3)
- Venue: Journal of Computational Physics, Vol. 378, pp. 686-707
- Type: journal
- Identifier: DOI:10.1016/j.jcp.2018.10.045
- URL: https://www.sciencedirect.com/science/article/pii/S0021999118307125 (Semantic Scholar record verified)
- Citations: ~20,971 (source: Semantic Scholar 2026-10-06; GS snippet ~30,564)
- Domain: framework
- Problem type: framework
- Physics enforced: generic nonlinear PDE u_t + N[u; lambda] = 0 (Burgers, Schrodinger, Navier-Stokes exemplars)
- Enforcement mechanism: soft-penalty — PDE residual added to loss via automatic differentiation (collocation MSE)
- Architecture: fully connected MLP (tanh), e.g. 9 layers x 20 neurons (Burgers)
- Loss & weighting: MSE(data fit) + MSE(PDE residual), fixed manual weights
- Sampling & training: fixed Latin-hypercube collocation points; L-BFGS(-B) full-batch
- Data regime: sparse (forward Burgers ~256 snapshots; inverse Navier-Stokes ~0.25% density)
- Key result: launched the field; accurate forward and inverse solutions from sparse data; the field's reference implementation of the soft-constraint recipe
- Relevance to review: anchor citation defining the PINN formulation all later methodology modifies
- Verification: verified via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.jcp.2018.10.045

### A02
- Title: Estimates on the generalization error of physics-informed neural networks for approximating PDEs
- Authors: Siddhartha Mishra, Roberto Molinaro
- Year: 2022 (online 2022-01-14; issue Vol. 43(1) 2023)
- Venue: IMA Journal of Numerical Analysis, Vol. 43, No. 1, pp. 1-43
- Type: journal
- Identifier: DOI:10.1093/imanum/drab093
- URL: https://academic.oup.com/imajna (Crossref record verified)
- Citations: n/a
- Domain: theory
- Problem type: theory
- Physics enforced: generic class of PDEs (elliptic/parabolic forward problems)
- Enforcement mechanism: soft-penalty (analysis of the standard PINN empirical risk)
- Architecture: agnostic (MLP with ReLU-type activations analyzed)
- Loss & weighting: PINN loss decomposed; bound scales with training residual and squared training loss
- Sampling & training: theoretical — quadrature/collocation error enters the bound
- Data regime: none
- Key result: first a posteriori generalization estimates: total error = approximation + generalization + quadrature error; small training loss implies small generalization gap
- Relevance to review: theoretical backbone for "why the soft-constraint loss works" claims
- Verification: verified via https://api.crossref.org/works/10.1093/imanum/drab093

### A03
- Title: Characterizing possible failure modes in physics-informed neural networks
- Authors: Aditi S. Krishnapriyan, Amir Gholami, Shandian Zhe, Robert M. Kirby, Michael W. Mahoney
- Year: 2021
- Venue: Advances in Neural Information Processing Systems 34 (NeurIPS 2021)
- Type: conference
- Identifier: arXiv:2109.01050
- URL: https://arxiv.org/abs/2109.01050
- Citations: ~2,114 (source: GS-snippet estimate)
- Domain: training
- Problem type: training-methodology
- Physics enforced: parameterized convection, reaction, diffusion (linear prototypes); Burgers; wave equation
- Enforcement mechanism: soft-penalty (shown to fail); curriculum regularization and sequence-to-sequence time-marching proposed
- Architecture: MLP
- Loss & weighting: unweighted sum of MSE terms; curriculum splits time horizon into sequential sub-problems
- Sampling & training: fixed collocation; per-step training on time intervals (curriculum / seq2seq)
- Data regime: none
- Key result: soft-constraint PINNs fail even on slightly parameterized PDEs (errors grow orders of magnitude with convection speed); curriculum/seq2seq recover 1-2 orders of magnitude lower error
- Relevance to review: canonical citation that PINN failure is systematic, motivating all loss-balancing and scheduling work
- Verification: verified via https://arxiv.org/abs/2109.01050 (NeurIPS 2021 journal-ref listed on page)

### A04
- Title: Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks
- Authors: Sifan Wang, Yujun Teng, Paris Perdikaris
- Year: 2021
- Venue: SIAM Journal on Scientific Computing, Vol. 43, No. 5, pp. A3055-A3081
- Type: journal
- Identifier: DOI:10.1137/20M1318043
- URL: https://epubs.siam.org/doi/10.1137/20M1318043 (Crossref record verified)
- Citations: ~425 (source: GS-snippet estimate, likely outdated)
- Domain: training
- Problem type: training-methodology
- Physics enforced: generic PDE residual (Helmholtz, Burgers, Allen-Cahn exemplars)
- Enforcement mechanism: soft-penalty with adaptive loss weights
- Architecture: MLP
- Loss & weighting: competing loss-term gradient magnitudes imbalance; learning-rate annealing — per-term weights proportional to inverse L2 norm of each loss term's gradient
- Sampling & training: fixed collocation; Adam with annealed weights (alternative: SGA/Adam tuning)
- Data regime: none / sparse (forward and inverse)
- Key result: names and measures the gradient-conflict pathology; learning-rate annealing restores balanced gradients and materially improves accuracy
- Relevance to review: foundational entry of the gradient-norm loss-balancing family used across industries
- Verification: verified via https://api.crossref.org/works/10.1137/20M1318043

### A05
- Title: On the eigenvector bias of Fourier feature networks: From regression to solving multi-scale PDEs with physics-informed neural networks
- Authors: Sifan Wang, Hanwen Wang, Paris Perdikaris
- Year: 2021
- Venue: Computer Methods in Applied Mechanics and Engineering, Vol. 384, Article 113938
- Type: journal
- Identifier: DOI:10.1016/j.cma.2021.113938
- URL: https://www.sciencedirect.com/science/article/pii/S0045782521006200 (arXiv abs page verified; Crossref DOI cross-checked)
- Citations: n/a
- Domain: theory
- Problem type: theory
- Physics enforced: multi-scale / high-wavenumber PDEs (Helmholtz, Navier-Stokes-type benchmarks)
- Enforcement mechanism: soft-penalty with Fourier-feature input embedding
- Architecture: Fourier feature MLP; modified Fourier feature distribution with scaled spectral bandwidth
- Loss & weighting: standard weighted MSE loss; reweighting via learning-rate annealing
- Sampling & training: fixed collocation; Adam + L-BFGS
- Data regime: none
- Key result: NTK eigenvector bias explains slow convergence to high-frequency modes; scaled Fourier features (beta > 1) mitigate spectral bias and enable multi-scale PDE solutions
- Relevance to review: theory-driven fix for high-frequency failure; connects architecture choice to kernel spectrum
- Verification: verified via https://arxiv.org/abs/2012.10047 + https://api.crossref.org/works/10.1016/j.cma.2021.113938

### A06
- Title: When and why PINNs fail to train: A neural tangent kernel perspective
- Authors: Sifan Wang, Xinling Yu, Paris Perdikaris
- Year: 2022
- Venue: Journal of Computational Physics, Vol. 449, Article 110768
- Type: journal
- Identifier: DOI:10.1016/j.jcp.2021.110768
- URL: https://www.sciencedirect.com/science/article/pii/S0021999121006771 (Semantic Scholar record verified)
- Citations: ~1,880 (source: Semantic Scholar 2026-10-06; GS snippet ~2,483)
- Domain: theory
- Problem type: theory
- Physics enforced: stiff high-wavenumber diffusion-advection-reaction; Helmholtz; irregular-domain Poisson-type problems
- Enforcement mechanism: soft-penalty analyzed through NTK eigenspectra
- Architecture: MLP (spectral-bias analysis of NTK at initialization and during training)
- Loss & weighting: loss-term interdependence via NTK; learning-rate annealing to balance eigenvalue condition numbers
- Sampling & training: fixed collocation; annealing schedule over training
- Data regime: none
- Key result: identifies spectral bias and stiffness (large NTK condition number) as the two causes of training failure; annealing and modified losses resolve failures on stiff problems
- Relevance to review: the standard theoretical explanation of PINN training failure cited by later methodological papers
- Verification: verified via https://api.semanticscholar.org/graph/v1/paper/arXiv:2007.14527

### A07
- Title: Self-adaptive physics-informed neural networks
- Authors: Levi D. McClenny, Ulisses M. Braga-Neto
- Year: 2023 (arXiv 2020)
- Venue: Journal of Computational Physics, Vol. 474, Article 111722
- Type: journal
- Identifier: DOI:10.1016/j.jcp.2022.111722
- URL: https://www.sciencedirect.com/science/article/pii/S0021999122008088 (arXiv abs page verified; Crossref DOI cross-checked)
- Citations: ~1,300 (source: GS-snippet estimate)
- Domain: training
- Problem type: training-methodology
- Physics enforced: generic PDE residual (Burgers, Helmholtz high-frequency, irregular domains, Allen-Cahn-type exemplars)
- Enforcement mechanism: soft-penalty with trainable pointwise self-adaptive weights sigma(x; eta) — soft attention mask multiplying residual terms, incentivized to exceed 1 where residual is violated
- Architecture: MLP + trainable weight mask eta over collocation points
- Loss & weighting: weighted MSE where pointwise weights are learned jointly with network parameters
- Sampling & training: fixed collocation; Adam then L-BFGS
- Data regime: none
- Key result: learned pointwise weights concentrate on high-residual regions and solve instances (e.g., high-frequency Helmholtz) where standard PINNs fail
- Relevance to review: representative of the self-adaptive weighting family; frequently copied in applied PINN papers
- Verification: verified via https://arxiv.org/abs/2009.04544 + https://api.crossref.org/works/10.1016/j.jcp.2022.111722

### A08
- Title: A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks
- Authors: Chenxi Wu, Min Zhu, Qinyang Tan, Yadhu Kartha, Lu Lu
- Year: 2023
- Venue: Computer Methods in Applied Mechanics and Engineering, Vol. 403, Article 115671
- Type: journal
- Identifier: DOI:10.1016/j.cma.2022.115671
- URL: https://www.sciencedirect.com/science/article/pii/S0045782522007162 (Crossref record verified)
- Citations: ~1,142 (source: GS-snippet estimate)
- Domain: training
- Problem type: training-methodology
- Physics enforced: generic PDE residual (Burgers, Helmholtz, Klein-Gordon, and other benchmarks; forward and inverse)
- Enforcement mechanism: soft-penalty; collocation distribution is the control variable (RAD = residual-based adaptive distribution; RAR = residual-based adaptive refinement incl. RAR-D)
- Architecture: MLP
- Loss & weighting: standard weighted MSE loss
- Sampling & training: systematic comparison of fixed uniform/LHS sampling vs RAD/RAR refinement across thousands of configurations; Adam-style training with periodic resampling
- Data regime: none
- Key result: residual-based adaptive sampling (esp. RAR-D) improves accuracy with fewer residual points; large-scale empirical evidence
- Relevance to review: the reference quantitative study of the collocation-sampling axis of PINN methodology
- Verification: verified via https://api.crossref.org/works/10.1016/j.cma.2022.115671

### A09
- Title: DeepXDE: A deep learning library for solving differential equations
- Authors: Lu Lu, Xuhui Meng, Zhiping Mao, George Em Karniadakis
- Year: 2021
- Venue: SIAM Review, Vol. 63, No. 1, pp. 208-228
- Type: journal
- Identifier: DOI:10.1137/19M1274067
- URL: https://epubs.siam.org/doi/10.1137/19M1274067 (arXiv abs page verified; Crossref DOI cross-checked)
- Citations: ~3,835 (source: GS-snippet estimate on arXiv version)
- Domain: framework
- Problem type: framework
- Physics enforced: generic ODE/PDE systems, forward and inverse (user-declared geometry and equations)
- Enforcement mechanism: soft-penalty; supports hard constraints, RAR (residual-based adaptive refinement) sampling, coupled PDEs, and operator learning
- Architecture: MLP and variants (Platypus-style user stack: activations, initialization, dropout)
- Loss & weighting: configurable loss weights per term
- Sampling & training: built-in uniform/LHS/adaptive sampling; Adam then L-BFGS
- Data regime: none / sparse / dense (user-defined)
- Key result: the most widely adopted open-source PINN library (TensorFlow/PyTorch/JAX/Paddle backends); introduced RAR sampling in practice
- Relevance to review: the enabling framework most used in industrial and academic reproductions
- Verification: verified via https://arxiv.org/abs/1907.04502 + https://api.crossref.org/works/10.1137/19M1274067

### A10
- Title: An Expert's Guide to Training Physics-informed Neural Networks
- Authors: Sifan Wang, Shyam Sankaran, Hanwen Wang, Paris Perdikaris
- Year: 2023
- Venue: arXiv (preprint; accompanying jaxpi JAX library)
- Type: preprint
- Identifier: arXiv:2308.08468
- URL: https://arxiv.org/abs/2308.08468
- Citations: n/a
- Domain: training
- Problem type: training-methodology
- Physics enforced: generic PDE residual (challenging benchmark suite incl. fluid and wave problems)
- Enforcement mechanism: soft-penalty with the authors' full best-practice stack (architectures, activations, weighting, sampling)
- Architecture: MLP variants (incl. modified MLP with residual connections)
- Loss & weighting: systematic ablation of weighting schemes and training stages
- Sampling & training: best practices: training stages, collocation strategies, optimizer schedules; fully reproducible ablations
- Data regime: none / sparse
- Key result: a curated set of training choices that achieves state-of-the-art accuracy and strong baselines; jaxpi reference code
- Relevance to review: de facto training guide; the source of the Adam-then-L-BFGS and two-stage training conventions many applied papers follow
- Verification: verified via https://arxiv.org/abs/2308.08468

### A11
- Title: PINNacle: A Comprehensive Benchmark of Physics-Informed Neural Networks for Solving PDEs
- Authors: Zhongkai Hao, Jiachen Yao, Chang Su, Hang Su, Ziao Wang, Fanzhi Lu, Zeyu Xia, Yichi Zhang, Songming Liu, Lu Lu, Jun Zhu
- Year: 2023 (accepted NeurIPS 2024 Datasets and Benchmarks track)
- Venue: arXiv preprint / NeurIPS 2024 Datasets and Benchmarks
- Type: conference
- Identifier: arXiv:2306.08827
- URL: https://arxiv.org/abs/2306.08827
- Citations: n/a
- Domain: benchmark
- Problem type: benchmark
- Physics enforced: 20+ PDEs across heat conduction, fluid dynamics, biology, electromagnetics (complex geometry, multi-scale, nonlinearity, high-dimensionality challenges)
- Enforcement mechanism: soft-penalty (compares ~10 state-of-the-art PINN methods incl. loss reweighting and domain decomposition)
- Architecture: multiple (MLP, modified MLP, PINNsacle variants)
- Loss & weighting: benchmarked variants (fixed, annealed, NTK-based)
- Sampling & training: standardized training protocol across methods
- Data regime: none
- Key result: largest PINN benchmark to date; finds no single method dominates and that robustness varies by challenge type
- Relevance to review: benchmark for substantiating methodological comparison claims in the survey
- Verification: verified via https://arxiv.org/abs/2306.08827 + OpenReview NeurIPS 2024 D&B record (search cross-check)

### A12
- Title: PDEBENCH: An Extensive Benchmark for Scientific Machine Learning
- Authors: Makoto Takamoto, Timothy Praditia, Raphael Leiteritz, Dan MacKinlay, Francesco Alesiani, Dirk Pflueger, Mathias Niepert
- Year: 2022
- Venue: Advances in Neural Information Processing Systems 35 (NeurIPS 2022 Datasets and Benchmarks Track)
- Type: conference
- Identifier: arXiv:2210.07182
- URL: https://arxiv.org/abs/2210.07182
- Citations: n/a
- Domain: benchmark
- Problem type: benchmark
- Physics enforced: broad time-dependent PDE families in 1D/2D/3D (advection, diffusion-reaction, incompressible/compressible Navier-Stokes, shallow water, etc.), forward and inverse tasks
- Enforcement mechanism: data-driven simulation benchmarks incl. a PINN baseline (soft-penalty among FNO, U-Net baselines)
- Architecture: PINN, FNO, U-Net baselines provided
- Loss & weighting: standard per-model setups
- Sampling & training: standardized dataset splits and metrics
- Data regime: dense simulation (reference numerical solvers)
- Key result: large ready-to-use dataset + classical-solver baselines + metrics; identifies tasks still unsolved by ML surrogates
- Relevance to review: community benchmark that situates PINN accuracy against data-driven surrogates and classical solvers
- Verification: verified via https://arxiv.org/abs/2210.07182 (NeurIPS 2022 D&B acceptance stated on page)

### A13
- Title: Can physics-informed neural networks beat the finite element method?
- Authors: Tamara G. Grossmann, Urszula Julia Komorowska, Jonas Latz, Carola-Bibiane Schoenlieb
- Year: 2024
- Venue: IMA Journal of Applied Mathematics, Vol. 89, No. 1, pp. 143-174
- Type: journal
- Identifier: DOI:10.1093/imamat/hxae011
- URL: https://academic.oup.com/imamat (arXiv abs page verified; Crossref record verified)
- Citations: n/a
- Domain: theory
- Problem type: theory
- Physics enforced: Poisson in 1D/2D/3D, Allen-Cahn in 1D, semilinear Schrodinger in 1D/2D
- Enforcement mechanism: soft-penalty, compared to FEM discretization
- Architecture: MLP
- Loss & weighting: standard PINN loss with tuned hyperparameters
- Sampling & training: tuned collocation and optimizer settings for fair comparison
- Data regime: none
- Key result: in solution time and accuracy, PINNs did not outperform FEM on the tested problems; PINNs faster only at evaluating an already-trained model (inference)
- Relevance to review: the key honest-comparison citation tempering PINN claims vs classical numerics
- Verification: verified via https://arxiv.org/abs/2302.04107 + https://api.crossref.org/works/10.1093/imamat/hxae011

### A14
- Title: Generic bounds on the approximation error for physics-informed (and) operator learning
- Authors: Tim De Ryck, Siddhartha Mishra
- Year: 2022
- Venue: Advances in Neural Information Processing Systems 35 (NeurIPS 2022)
- Type: conference
- Identifier: arXiv:2205.11393
- URL: https://arxiv.org/abs/2205.11393
- Citations: ~132 (source: GS-snippet estimate)
- Domain: theory
- Problem type: theory
- Physics enforced: general classes of PDEs incl. nonlinear parabolic PDEs (Kolmogorov-type)
- Enforcement mechanism: soft-penalty (analysis of physics-informed neural/operator architectures)
- Architecture: agnostic (PINNs, physics-informed DeepONets/FNOs)
- Loss & weighting: theoretical
- Sampling & training: theoretical (quadrature effects bounded)
- Data regime: none
- Key result: generic, distribution-independent approximation-error bounds; curse of dimensionality avoided for nonlinear parabolic PDEs; first rigorous bounds for physics-informed operator learning
- Relevance to review: connects PINN approximation theory to operator learning in one framework
- Verification: verified via https://arxiv.org/abs/2205.11393 (NeurIPS 35 venue from proceedings citation cross-check)

### A15
- Title: Numerical analysis of physics-informed neural networks and related models in physics-informed machine learning
- Authors: Tim De Ryck, Siddhartha Mishra
- Year: 2024
- Venue: Acta Numerica, Vol. 33, pp. 633-713 (Cambridge University Press)
- Type: journal
- Identifier: DOI:10.1017/S0962492923000089
- URL: https://www.cambridge.org/core/journals/acta-numerica (Crossref record verified)
- Citations: ~167 (source: GS-snippet estimate)
- Domain: theory
- Problem type: survey
- Physics enforced: generic PDEs (approximation, generalization, robustness across model classes)
- Enforcement mechanism: covers soft-penalty PINNs and related physics-informed models (Deep Ritz, DGM, VPINN etc.)
- Architecture: survey across architectures
- Loss & weighting: survey across loss formulations
- Sampling & training: survey incl. training/optimization analysis
- Data regime: n/a
- Key result: authoritative synthesis of the numerical-analysis view of PINNs: error decomposition, a priori/a posteriori bounds, robustness and training behavior
- Relevance to review: the single best theory survey to cite for the methodology section's theoretical claims
- Verification: verified via https://api.crossref.org/works/10.1017/S0962492923000089

### A16
- Title: Respecting causality for training physics-informed neural networks
- Authors: Sifan Wang, Shyam Sankaran, Paris Perdikaris
- Year: 2024 (arXiv 2022 as "Respecting causality is all you need...")
- Venue: Computer Methods in Applied Mechanics and Engineering, Vol. 421, Article 116813
- Type: journal
- Identifier: DOI:10.1016/j.cma.2024.116813
- URL: https://www.sciencedirect.com/science/article/pii/S0045782524000815 (arXiv abs page verified; Crossref record verified)
- Citations: n/a
- Domain: training
- Problem type: training-methodology
- Physics enforced: time-dependent chaotic/dynamic systems: Lorenz system, Kuramoto-Sivashinsky (chaotic regime), Navier-Stokes (turbulent regime)
- Enforcement mechanism: soft-penalty with causal weighting — residual weights penalize the residual at time t only after earlier times converge (temporal causality annealing)
- Architecture: MLP
- Loss & weighting: residual MSE with time-marching-inspired causal weights derived from residual decay rates
- Sampling & training: causal annealing schedule over time; provides a practical convergence criterion
- Data regime: none
- Key result: first reported PINN success on such chaotic/turbulent benchmarks; significant accuracy gains over standard training
- Relevance to review: flagship of the scheduling/curriculum branch of PINN training methodology
- Verification: verified via https://api.crossref.org/works/10.1016/j.cma.2024.116813 + https://arxiv.org/abs/2203.07404

### A17
- Title: Physics-informed neural networks for PDE problems: a comprehensive review
- Authors: Kuang Luo, Jingshang Zhao, Yingping Wang, Jiayao Li, Junjie Wen, Jiong Liang, Henry Soekmadji, Shaolin Liao
- Year: 2025
- Venue: Artificial Intelligence Review, Vol. 58, Issue 10, Article 323 (Springer, open access)
- Type: journal
- Identifier: DOI:10.1007/s10462-025-11322-7
- URL: https://link.springer.com/article/10.1007/s10462-025-11322-7
- Citations: ~358 (source: GS-snippet estimate)
- Domain: survey
- Problem type: survey
- Physics enforced: generic PDE problems (forward and inverse) across domains
- Enforcement mechanism: taxonomy of soft/hard/weak constraint enforcement, sampling, loss and activation design, feature embedding
- Architecture: survey of architectures incl. modified MLPs
- Loss & weighting: survey of adaptive weighting approaches
- Sampling & training: survey of collocation strategies and software (DeepXDE, IDRLnet, NeuroDiffEq, SciANN, TensorDiffEq)
- Data regime: n/a
- Key result: comprehensive 2025 taxonomy of PINN methods and open challenges (published in the target journal of the survey)
- Relevance to review: most recent comprehensive review in Artificial Intelligence Review itself — must be positioned/differentiated against
- Verification: verified via https://api.crossref.org/works/10.1007/s10462-025-11322-7 + Springer issue page

### A18
- Title: On the convergence of PINNs
- Authors: Nathan Doumeche, Gerard Biau, Claire Boyer
- Year: 2025 (arXiv 2023)
- Venue: Bernoulli, Vol. 31, No. 3, pp. 2127-2151
- Type: journal
- Identifier: DOI:10.3150/24-BEJ1799
- URL: https://projecteuclid.org/journals/bernoulli (arXiv abs page verified; Crossref record verified)
- Citations: n/a
- Domain: theory
- Problem type: theory
- Physics enforced: linear and nonlinear PDE systems (hybrid/physics + data estimation)
- Enforcement mechanism: soft-penalty; theoretical analysis of the empirical risk
- Architecture: agnostic (statistical learning analysis)
- Loss & weighting: shows plain PINN training overfits systematically; ridge-regularized empirical risk gives risk-consistent estimators
- Sampling & training: theoretical; Sobolev-type regularization for physically consistent solutions
- Data regime: sparse (data + physics setting)
- Key result: plain PINN training is not statistically consistent without regularization; an additional ridge term fixes it
- Relevance to review: recent statistical-learning critique of the default PINN loss — sharpens the loss-design discussion
- Verification: verified via https://arxiv.org/abs/2305.01240 + https://api.crossref.org/works/10.3150/24-BEJ1799

### A19
- Title: Self-adaptive weights based on balanced residual decay rate for physics-informed neural networks and deep operator networks
- Authors: Wenqian Chen, Amanda A. Howard, Panos Stinis
- Year: 2025 (arXiv 2024)
- Venue: Journal of Computational Physics, Vol. 542, Article 114226
- Type: journal
- Identifier: DOI:10.1016/j.jcp.2025.114226
- URL: https://www.sciencedirect.com/science/article/pii/S0021999125002171 (arXiv abs page verified; journal DOI listed on arXiv page)
- Citations: n/a
- Domain: training
- Problem type: training-methodology
- Physics enforced: generic PDE residual (PINN benchmarks) and DeepONet operator-learning settings
- Enforcement mechanism: soft-penalty with pointwise adaptive weights balancing residual decay rates across training points
- Architecture: MLP (and DeepONet variant)
- Loss & weighting: pointwise self-adaptive weights, bounded by construction, updated from residual decay-rate statistics
- Sampling & training: standard collocation with weight updates during training; low computational overhead
- Data regime: none
- Key result: argues plain PINN failure stems from large discrepancy in residual convergence rates across points; balancing them yields bounded weights, faster convergence, and accuracy competitive with or better than prior weighting schemes
- Relevance to review: 2025 state-of-the-art entry for the loss-weighting axis; bridges PINN and operator-learning training
- Verification: verified via https://arxiv.org/abs/2407.01613 (journal DOI on page)

### A20
- Title: Physics-Informed Neural Networks in Computational Mechanics: A Critical Review of Stability, Generalization, and Multi-Scale Applications
- Authors: Yazan Sanjalawe, Nashat Al-E'mari, Nabeil Makhadmeh (family names from Crossref)
- Year: 2026
- Venue: Archives of Computational Methods in Engineering (Springer)
- Type: journal
- Identifier: DOI:10.1007/s11831-026-10747-9
- URL: https://link.springer.com/article/10.1007/s11831-026-10747-9 (Crossref record verified)
- Citations: n/a
- Domain: theory
- Problem type: survey
- Physics enforced: PDEs of computational mechanics (multi-scale problems)
- Enforcement mechanism: reviews the composite residual functional and training in the language of numerical analysis
- Architecture: survey
- Loss & weighting: analyzes training dynamics via NTK and reviews weighting schemes
- Sampling & training: derives Sobolev-norm stability bounds linking minimized residual to true error
- Data regime: n/a
- Key result: 2026 review formalizing PINN training theory for computational mechanics: NTK training dynamics, Sobolev-norm stability, multi-scale application analysis
- Relevance to review: freshest theory-oriented review to cite for 2026 currency of the methodology section
- Verification: verified via https://api.crossref.org/works/10.1007/s11831-026-10747-9

## Machine rows

A01|Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations|2019|Journal of Computational Physics|journal|DOI:10.1016/j.jcp.2018.10.045|~20971 (S2 2026-10-06)|framework|generic nonlinear PDE residual (Burgers/ Schrodinger/ Navier-Stokes)|soft-penalty|framework|1|Y
A02|Estimates on the generalization error of physics-informed neural networks for approximating PDEs|2022|IMA Journal of Numerical Analysis|journal|DOI:10.1093/imanum/drab093|n/a|theory|generic PDE class|soft-penalty|theory|2|Y
A03|Characterizing possible failure modes in physics-informed neural networks|2021|NeurIPS 2021|conference|arXiv:2109.01050|~2114 (GS-snippet)|training|convection/ reaction/ diffusion/ Burgers/ wave|soft-penalty|training-methodology|1|Y
A04|Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks|2021|SIAM Journal on Scientific Computing|journal|DOI:10.1137/20M1318043|~425 (GS-snippet estimate)|training|generic PDE residual|soft-penalty|training-methodology|1|Y
A05|On the eigenvector bias of Fourier feature networks: From regression to solving multi-scale PDEs with physics-informed neural networks|2021|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2021.113938|n/a|theory|multi-scale high-wavenumber PDEs|soft-penalty|theory|2|Y
A06|When and why PINNs fail to train: A neural tangent kernel perspective|2022|Journal of Computational Physics|journal|DOI:10.1016/j.jcp.2021.110768|~1880 (S2 2026-10-06)|theory|stiff diffusion-advection-reaction/ Helmholtz|soft-penalty|theory|1|Y
A07|Self-adaptive physics-informed neural networks|2023|Journal of Computational Physics|journal|DOI:10.1016/j.jcp.2022.111722|~1300 (GS-snippet estimate)|training|generic PDE residual|soft-penalty|training-methodology|1|Y
A08|A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks|2023|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2022.115671|~1142 (GS-snippet)|training|generic PDE residual (forward and inverse)|soft-penalty|training-methodology|2|Y
A09|DeepXDE: A Deep Learning Library for Solving Differential Equations|2021|SIAM Review|journal|DOI:10.1137/19M1274067|~3835 (GS-snippet)|framework|generic ODE/PDE systems|soft-penalty|framework|2|Y
A10|An Expert's Guide to Training Physics-informed Neural Networks|2023|arXiv (jaxpi library)|preprint|arXiv:2308.08468|n/a|training|generic PDE residual benchmark suite|soft-penalty|training-methodology|1|Y
A11|PINNacle: A Comprehensive Benchmark of Physics-Informed Neural Networks for Solving PDEs|2023|NeurIPS 2024 Datasets and Benchmarks (arXiv 2023)|conference|arXiv:2306.08827|n/a|benchmark|20+ PDEs: heat/ fluids/ biology/ electromagnetics|soft-penalty|benchmark|2|Y
A12|PDEBENCH: An Extensive Benchmark for Scientific Machine Learning|2022|NeurIPS 2022 Datasets and Benchmarks|conference|arXiv:2210.07182|n/a|benchmark|1D/2D/3D time-dependent PDE families incl. Navier-Stokes/ shallow water|soft-penalty|benchmark|3|Y
A13|Can physics-informed neural networks beat the finite element method?|2024|IMA Journal of Applied Mathematics|journal|DOI:10.1093/imamat/hxae011|n/a|theory|Poisson 1D/2D/3D/ Allen-Cahn/ semilinear Schrodinger|soft-penalty|theory|2|Y
A14|Generic bounds on the approximation error for physics-informed (and) operator learning|2022|NeurIPS 2022|conference|arXiv:2205.11393|~132 (GS-snippet)|theory|nonlinear parabolic PDEs (Kolmogorov-type)|soft-penalty|theory|3|Y
A15|Numerical analysis of physics-informed neural networks and related models in physics-informed machine learning|2024|Acta Numerica|journal|DOI:10.1017/S0962492923000089|~167 (GS-snippet)|theory|generic PDEs (PINNs and related models)|soft-penalty|survey|1|Y
A16|Respecting causality for training physics-informed neural networks|2024|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2024.116813|n/a|training|Lorenz/ Kuramoto-Sivashinsky (chaotic)/ Navier-Stokes (turbulent)|soft-penalty|training-methodology|2|Y
A17|Physics-informed neural networks for PDE problems: a comprehensive review|2025|Artificial Intelligence Review|journal|DOI:10.1007/s10462-025-11322-7|~358 (GS-snippet)|survey|generic PDE problems (forward and inverse)|soft-penalty|survey|1|Y
A18|On the convergence of PINNs|2025|Bernoulli|journal|DOI:10.3150/24-BEJ1799|n/a|theory|linear and nonlinear PDE systems|soft-penalty|theory|3|Y
A19|Self-adaptive weights based on balanced residual decay rate for physics-informed neural networks and deep operator networks|2025|Journal of Computational Physics|journal|DOI:10.1016/j.jcp.2025.114226|n/a|training|generic PDE residual and DeepONet setting|soft-penalty|training-methodology|2|Y
A20|Physics-Informed Neural Networks in Computational Mechanics: A Critical Review of Stability, Generalization, and Multi-Scale Applications|2026|Archives of Computational Methods in Engineering|journal|DOI:10.1007/s11831-026-10747-9|n/a|theory|PDEs of computational mechanics (multi-scale)|soft-penalty|survey|4|Y

## Slice takeaways

- The field's canonical formulation is remarkably uniform: essentially every foundational paper uses a soft-penalty PDE-residual MSE added to data losses via automatic differentiation on an MLP; the "hard-constraint / weak-form / energy-form" branches are handled by scout B/other slices, but within this slice A01-A20 all use the soft-penalty mechanism with variations only in weighting, sampling, scheduling, and architecture.
- Training failure is the unifying methodological theme: competing-loss gradient imbalance (A04), spectral bias and stiffness via NTK eigenspectra (A05, A06), and non-convergence on parameterized/chaotic PDEs (A03, A16) motivated three remedy families that dominate applied PINN papers: adaptive/annealed loss weighting (A04, A07, A19), residual-based adaptive sampling (A08, also built into A09), and curriculum/causal time-scheduling (A03, A16) — often combined with Adam-then-L-BFGS two-stage training (A10's best practices; DeepXDE default).
- Theory matured from universal approximation to quantitative error decomposition: a posteriori generalization bounds (A02), distribution-independent approximation bounds with no curse of dimensionality for parabolic PDEs (A14), the Acta Numerica synthesis (A15), and — importantly — a 2025 statistical result that the plain PINN loss is not risk-consistent without ridge regularization (A18), an open challenge worth flagging in the survey.
- Benchmarks now exist but are sobering: PINNacle (A11) and PDEBench (A12) show no single PINN method dominates across challenge types, and Grossmann et al. (A13) found FEM strictly better in time+accuracy on standard 2D problems (PINN advantage limited to inference speed on trained models).
- Recency anchors for the survey: the target journal itself published a comprehensive PINN review in July 2025 (A17, Luo et al., open access, ~358 citations) — the survey must differentiate from it — plus 2025 JCP loss-weighting state-of-the-art (A19), 2025 Bernoulli theory (A18), and a 2026 ACM E review (A20).
- Quantitative anchors available for the survey text: Raissi et al. ~21k S2 citations (30.5k GS); "When and why PINNs fail to train" ~1.9k S2; DeepXDE ~3.8k; Krishnapriyan ~2.1k — indicating training methodology is the most-cited subfield after the anchor.
- Frameworks: DeepXDE (A09) is the dominant open-source library (multi-backend); SciANN (CMAME 2021, DOI:10.1016/j.cma.2020.113552, ~576 GS citations) is the lighter-weight alternative; NVIDIA Modulus was renamed PhysicsNeMo (GitHub NVIDIA/physicsnemo, releases through 2026) and jaxpi (JAX) accompanies A10 — no canonical papers exist for the latter two, cite as software.
- Gaps/open problems for the survey: no consensus weighting scheme (A11 found none dominates; A19 is the 2025 state of the art); theory-practice gap remains (A18's regularization requirement is rarely applied in practice); chaos/turbulence only became reachable with causal training (A16); RADAR-style importance sampling (Nabian/Gladisch) could not be verified and was excluded — do not cite without checking.
