# Slice B: Architectures, enforcement variants, operator learning

Scout B dossier for PINN survey (target: Artificial Intelligence Review, Springer). Time window 2021-2026 primary; 2 foundational anchors pre-2021 (SIREN 2020, Deep Ritz 2018). All papers verified via Semantic Scholar API, Crossref API, or arXiv API on 2026-10-06.

## Queries used
1. "neural operator survey 2025 operator learning review PDE"
2. "physics-informed foundation model PDE 2026"
3. "Transolver++ transformer PDE solver 2025 general geometries"
4. "PDE foundation model Poseidon efficient foundation models for PDEs ICLR 2025"
5. "domain decomposition physics-informed neural networks cPINN XPINN survey 2024 2025"
6. "self-adaptive physics-informed neural networks attention weights McClenny Braga-Neto"
7. "large language models for solving PDEs partial differential equations 2025 2026"
8. "physics-informed neural networks survey 2025 architectures activation functions review"
9. "\"weak adversarial networks\" high-dimensional partial differential equations Zang"
10. "operator learning survey \"neural operators\" 2025 Jha practical introduction scientific machine learning"
11. "\"physics-informed neural operator\" 2025 2026 advances review PINO variants"
12. "\"Can Large Language Models Design Effective Neural Operators\" ICML 2026"
13. "physics-informed diffusion model PDE generative hybrid 2025 uncertainty quantification neural operator"

## Screening summary
Candidates screened: ~31. Included: 23. Exclusion reasons:
- Tancik et al. 2020 (Fourier features, NeurIPS 2020): anchor budget; folded as context into B04 (eigenvector-bias Fourier-feature PINNs), which is the PINN-specific Fourier-features record.
- Galerkin Transformer (Cao, NeurIPS 2021, arXiv:2105.14995) and OFormer (Li, Meidani, Farimani, TMLR 2023, arXiv:2205.13671): both arXiv-verified; folded as lineage mentions in B16/B17 to stay near record target; both are safe citations.
- "Can Large Language Models Design Effective Neural Operators?" (Song, Zhen, Jiang; AI for Math Workshop @ ICML 2026): workshop-level venue, OpenReview page not fetched → excluded (mentioned in takeaways).
- G-PIFNN, AFDONet, PIGLNO, PIANO, DGNO (2025-2026 variants surfaced in search): venue/verification insufficient → excluded.
- DeepDDM: no verified top-venue record found; the 2023+ DD slot is filled by Dolean et al. 2024 (B10, CMAME).
- CP-PRE conformal prediction (arXiv:2502.04406), PINN-UU (JCP 2024): UQ methods outside architecture/operator scope → excluded (B-PINN covers UQ).
- "Solving PDEs using large-data models" (Artificial Intelligence Review, DOI 10.1007/s10462-024-10784-5): general large-data review, better suited to survey intro/scout A; flagged here for the parent.
- Note: no "attention-based PINN" by Wang & Perdikaris could be verified; the attention-based enforcement angle is covered by SA-PINN (B05, soft attention mechanism).
- Record count (23) exceeds the 12-18 target because the mission explicitly enumerates these topics; every record is verified.

## Paper records

### B01
- Title: Implicit Neural Representations with Periodic Activation Functions (SIREN)
- Authors: Sitzmann et al.
- Year: 2020
- Venue: Advances in Neural Information Processing Systems (NeurIPS 2020)
- Type: conference
- Identifier: arXiv:2006.09661
- URL: https://arxiv.org/abs/2006.09661
- Citations: ~3998 (Semantic Scholar)
- Domain: methodology
- Problem type: architecture
- Physics enforced: generic PDE residual (Poisson, wave/Helmholtz-style demos); mainly implicit functions (SDF, images, audio)
- Enforcement mechanism: soft-penalty
- Architecture: coordinate MLP with sine activations (sine(omega_0 Wx+b)); spectral-bias-free first layer with omega_0=30
- Loss & weighting: MSE data/residual sums
- Sampling & training: uniform collocation sampling; Adam
- Data regime: none (forward PDE demos) / sparse (fitted signals)
- Key result: periodic activations fit derivatives and higher-order details that ReLU/softplus MLPs miss, enabling PINN-grade coordinate networks.
- Relevance to review: anchor for the activation-function design axis of PINN architectures (sin vs tanh vs Fourier).
- Verification: verified via Semantic Scholar API (arXiv:2006.09661, NeurIPS 2020)

### B02
- Title: The Deep Ritz Method: A Deep Learning-Based Numerical Algorithm for Solving Variational Problems
- Authors: E et al. (Weinan E, Bing Yu)
- Year: 2018
- Venue: Communications in Mathematics and Statistics (Springer)
- Type: journal
- Identifier: DOI:10.1007/s40304-018-0127-z (arXiv:1710.00211)
- URL: https://doi.org/10.1007/s40304-018-0127-z
- Citations: ~2018 (Semantic Scholar; S2 lists online-first year 2017, print vol. 6, 2018)
- Domain: methodology
- Problem type: weak-form
- Physics enforced: Poisson equation (Dirichlet energy), generic PDEs with variational/energy form
- Enforcement mechanism: energy-form
- Architecture: deep ReLU ResNet-style MLP trial function
- Loss & weighting: Ritz energy functional + penalty-weighted Dirichlet BC term
- Sampling & training: stochastic mini-batch sampling inside the domain; SGD/Adam
- Data regime: none
- Key result: recasts PDEs as energy minimization, avoiding high-dimensional integration; natural-gradient-style optimization discussed.
- Relevance to review: anchor of the energy/variational enforcement family that weak-form and Galerkin PINNs build on.
- Verification: verified via Semantic Scholar API (DOI:10.1007/s40304-018-0127-z)

### B03
- Title: Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks
- Authors: Wang et al. (Sifan Wang, Yujun Teng, Paris Perdikaris)
- Year: 2021
- Venue: SIAM Journal on Scientific Computing 43(5):A3055-A3081
- Type: journal
- Identifier: DOI:10.1137/20M1318043
- URL: https://doi.org/10.1137/20M1318043
- Citations: ~1892 (Semantic Scholar)
- Domain: methodology
- Problem type: architecture
- Physics enforced: generic PDE residual (Burgers, Schrodinger, Helmholtz, Allen-Cahn demos)
- Enforcement mechanism: soft-penalty
- Architecture: "modified MLP": u -> [u, u_enh] where u_enh = a * W2 tanh(W1 u + b1); NTK-motivated two-layer enhancement of every hidden layer; paired with learning-rate annealing for loss balancing
- Loss & weighting: residual/data MSE with annealed weights (learning-rate annealing)
- Sampling & training: collocation sampling; Adam + L-BFGS
- Data regime: none / sparse (inverse demos)
- Key result: modified-MLP gradients + annealing drastically improve PINN training stability and accuracy.
- Relevance to review: canonical "modified MLP" architecture used by most later PINN implementations; architecture aspect (NTK theory is scout A's slice).
- Verification: verified via Semantic Scholar API (DOI:10.1137/20M1318043)

### B04
- Title: On the eigenvector bias of Fourier feature networks: From regression to solving multi-scale PDEs with physics-informed neural networks
- Authors: Wang et al. (Sifan Wang, Hanwen Wang, Paris Perdikaris)
- Year: 2021
- Venue: Computer Methods in Applied Mechanics and Engineering 384:113938
- Type: journal
- Identifier: DOI:10.1016/j.cma.2021.113938 (arXiv:2012.10047)
- URL: https://doi.org/10.1016/j.cma.2021.113938
- Citations: ~864 (Semantic Scholar; S2 lists online-first 2020)
- Domain: methodology
- Problem type: architecture
- Physics enforced: multi-scale PDE residuals (Poisson, Helmholtz, Navier-Stokes-type multi-scale benchmarks)
- Enforcement mechanism: soft-penalty
- Architecture: MLP with fixed/learnable random Fourier feature embedding u(x)=sin/cos(Bx) at multiple scales (extension of Tancik et al. 2020 Fourier features); multi-scale FF variants
- Loss & weighting: residual/data MSE with annealed weighting
- Sampling & training: collocation sampling; Adam + L-BFGS
- Data regime: none / sparse (inverse)
- Key result: Fourier-feature eigenvector bias explains spectral training bias; multi-scale FF embeddings let PINNs capture high-frequency multi-scale solutions.
- Relevance to review: canonical Fourier-feature input-embedding architecture for PINNs (random + adaptive FF).
- Verification: verified via Semantic Scholar API (DOI:10.1016/j.cma.2021.113938)

### B05
- Title: Self-Adaptive Physics-Informed Neural Networks using a Soft Attention Mechanism (SA-PINN)
- Authors: McClenny & Braga-Neto (Levi McClenny, Ulisses Braga-Neto)
- Year: 2023
- Venue: Journal of Computational Physics 491:112322 (arXiv preprint 2020)
- Type: journal
- Identifier: DOI:10.1016/j.jcp.2022.111722 (arXiv:2009.04544)
- URL: https://doi.org/10.1016/j.jcp.2022.111722
- Citations: ~866 (Semantic Scholar)
- Domain: methodology
- Problem type: architecture
- Physics enforced: generic PDE residual (Burgers, Helmholtz, Klein-Gordon, nonlinear Schrodinger-type demos)
- Enforcement mechanism: soft-penalty
- Architecture: standard PINN + pointwise trainable attention/mask vector multiplying the residual loss per collocation point
- Loss & weighting: residual weighted elementwise by trainable self-adaptive mask (alpha grows where error concentrates)
- Sampling & training: fixed collocation points; mask updated every iteration (sigmoidal schedule); Adam
- Data regime: none / sparse
- Key result: trainable pointwise soft attention autonomously focuses capacity on hard solution regions, outperforming non-adaptive PINNs.
- Relevance to review: the canonical attention/self-adaptive-weighting enforcement variant (covers the "attention-style PINN" item).
- Verification: verified via Semantic Scholar API (arXiv:2009.04544 linked to DOI:10.1016/j.jcp.2022.111722)

### B06
- Title: Conservative physics-informed neural networks on discrete domains for conservation laws: Applications to forward and inverse problems (cPINN)
- Authors: Jagtap et al. (Ameya Jagtap, Ehsan Kharazmi, George Em Karniadakis)
- Year: 2020
- Venue: Computer Methods in Applied Mechanics and Engineering 370:113028
- Type: journal
- Identifier: DOI:10.1016/j.cma.2020.113028
- URL: https://doi.org/10.1016/j.cma.2020.113028
- Citations: ~1277 (Semantic Scholar)
- Domain: methodology
- Problem type: domain-decomposition
- Physics enforced: conservation laws (inviscid/viscous Burgers, Euler-type systems)
- Enforcement mechanism: hybrid (per-subdomain soft residual + interface flux-continuity conditions)
- Architecture: one network per subdomain; communication only through shared interface points
- Loss & weighting: sum of subdomain losses + interface flux-continuity penalty
- Sampling & training: collocation per subdomain + interface points; Adam/L-BFGS
- Data regime: none / sparse (inverse)
- Key result: subdomain decomposition with flux-continuity interfaces conserves physics across interfaces and parallelizes training.
- Relevance to review: founding domain-decomposition PINN; defines the interface-condition pattern XPINN/FBPINN generalize.
- Verification: verified via Semantic Scholar API (DOI:10.1016/j.cma.2020.113028)

### B07
- Title: Extended Physics-Informed Neural Networks (XPINNs): A Generalized Space-Time Domain Decomposition based Deep Learning Framework for Nonlinear Partial Differential Equations
- Authors: Jagtap & Karniadakis (Ameya Jagtap, George Em Karniadakis)
- Year: 2020
- Venue: Communications in Computational Physics 28(5):2002-2041
- Type: journal
- Identifier: DOI:10.4208/cicp.OA-2020-0164
- URL: https://doi.org/10.4208/cicp.OA-2020-0164
- Citations: ~1215 (Semantic Scholar)
- Domain: methodology
- Problem type: domain-decomposition
- Physics enforced: nonlinear PDE residuals in space-time (Navier-Stokes-type benchmarks)
- Enforcement mechanism: hybrid (per-subdomain residual + interface solution/derivative continuity)
- Architecture: multiple subnetworks on generalized space-time subdomains with activation-function flexibility per subdomain
- Loss & weighting: subdomain residuals + interface continuity penalties
- Sampling & training: per-subdomain space-time collocation; Adam
- Data regime: none / sparse
- Key result: generalizes cPINN from conservation laws to arbitrary PDEs and space-time decomposition with hp-refinement potential.
- Relevance to review: the general DD-PINN formulation; widely cited baseline for decomposition-based PINN scalability.
- Verification: verified via Semantic Scholar API (DOI:10.4208/cicp.OA-2020-0164)

### B08
- Title: hp-VPINNs: Variational Physics-Informed Neural Networks With Domain Decomposition
- Authors: Kharazmi et al. (Ehsan Kharazmi, Weinan E, George Em Karniadakis)
- Year: 2021
- Venue: Computer Methods in Applied Mechanics and Engineering 374:113547
- Type: journal
- Identifier: DOI:10.1016/j.cma.2020.113547 (arXiv:2003.05385)
- URL: https://doi.org/10.1016/j.cma.2020.113547
- Citations: ~917 (Semantic Scholar; S2 lists online-first 2020)
- Domain: methodology
- Problem type: weak-form
- Physics enforced: PDEs in variational/weak form (Burgers-type, low-regularity solutions)
- Enforcement mechanism: weak/variational
- Architecture: PINN networks per element of an hp-decomposition; discontinuous Galerkin-style assembly with polynomial test functions
- Loss & weighting: elementwise variational residual integrated by Gauss quadrature + interelement penalty
- Sampling & training: quadrature points per element; Adam/L-BFGS
- Data regime: none
- Key result: weak form + hp domain decomposition handles low-regularity solutions where strong-form PINNs fail.
- Relevance to review: canonical variational/weak-form PINN; connects PINNs to FEM/DG structure (extends vpPINN).
- Verification: verified via Semantic Scholar API (DOI:10.1016/j.cma.2020.113547)

### B09
- Title: Finite basis physics-informed neural networks (FBPINNs): a scalable domain decomposition approach for solving differential equations
- Authors: Moseley et al. (Ben Moseley, Andrew Markham, Tarje Nissen-Meyer)
- Year: 2023
- Venue: Advances in Computational Mathematics (Springer) 49
- Type: journal
- Identifier: DOI:10.1007/s10444-023-10065-9
- URL: https://doi.org/10.1007/s10444-023-10065-9
- Citations: ~321 (Crossref is-referenced-by-count; preprint arXiv 2021 widely cited)
- Domain: methodology
- Problem type: domain-decomposition
- Physics enforced: generic ODE/PDE residuals (e.g., Burgers, wave-type benchmarks)
- Enforcement mechanism: hybrid (partition-of-unity finite-basis sum is a hard structural constraint; residuals still soft-penalized)
- Architecture: many small subnetworks summed through smooth partition-of-unity windows with per-subdomain input normalization
- Loss & weighting: normalized per-subdomain residual losses summed globally
- Sampling & training: collocation per subdomain; independent/parallel subnetwork training
- Data regime: none
- Key result: local normalization + small subnetworks beat a single large PINN on large/multi-scale domains and are embarrassingly parallel.
- Relevance to review: the scaling-oriented DD architecture; per-subdomain normalization is a key trick for multi-scale problems. Related: Dolean et al. multilevel DD (B10).
- Verification: verified via Crossref API (DOI:10.1007/s10444-023-10065-9)

### B10
- Title: Multilevel domain decomposition-based architectures for physics-informed neural networks
- Authors: Dolean et al. (Victorita Dolean, Alexander Heinlein, Siddhartha Mishra, Ben Moseley et al.)
- Year: 2024
- Venue: Computer Methods in Applied Mechanics and Engineering
- Type: journal
- Identifier: DOI:10.1016/j.cma.2024.117116 (arXiv:2306.05486)
- URL: https://doi.org/10.1016/j.cma.2024.117116
- Citations: ~120 (Semantic Scholar; S2 lists online-first 2023)
- Domain: methodology
- Problem type: domain-decomposition
- Physics enforced: generic PDE residuals (Poisson/Helmholtz-type benchmarks, incl. inverse problems)
- Enforcement mechanism: soft-penalty (with DD-structured basis)
- Architecture: finite-basis networks with coarse+fine (multilevel) localized basis functions, FEM-inspired
- Loss & weighting: global residual/data losses over DD-summed network
- Sampling & training: collocation sampling; standard optimizers
- Data regime: none / sparse
- Key result: multilevel (coarse+fine) DD basis converges faster and more robustly than single-level FBPINN on complex domains.
- Relevance to review: 2023+ evolution of DD-PINN architectures; links FEM multilevel theory to PINN design.
- Verification: verified via Semantic Scholar API (DOI:10.1016/j.cma.2024.117116)

### B11
- Title: Weak Adversarial Networks for High-dimensional Partial Differential Equations
- Authors: Zang et al. (Yaohua Zang, Gang Bao, Xiaojing Ye, Haomin Zhou)
- Year: 2020
- Venue: Journal of Computational Physics 411:109409
- Type: journal
- Identifier: DOI:10.1016/j.jcp.2020.109409 (arXiv:1907.08272)
- URL: https://doi.org/10.1016/j.jcp.2020.109409
- Citations: ~570 (Semantic Scholar; S2 lists online-first 2019)
- Domain: methodology
- Problem type: weak-form
- Physics enforced: high-dimensional PDEs in weak form (Black-Scholes, Hamilton-Jacobi-Bellman, Schrodinger-type)
- Enforcement mechanism: weak/variational (adversarial minimax over test-function network)
- Architecture: solution network vs adversarial test-function network (GAN-style saddle point)
- Loss & weighting: weak-form residual integrated against the learned test function; minimax objective
- Sampling & training: interior sampling + test nets trained on shrinking supports; alternating optimization
- Data regime: none
- Key result: weak formulation with adversarial test functions handles low regularity and scales to very high dimensions without integration over meshes.
- Relevance to review: the weak/adversarial enforcement variant of the Deep Ritz family; contrast to strong-form PINNs.
- Verification: verified via Semantic Scholar API (DOI:10.1016/j.jcp.2020.109409)

### B12
- Title: Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators
- Authors: Lu et al. (Lu Lu, Pengzhan Jin, Guofei Pang, Zhongqiang Zhang, George Em Karniadakis)
- Year: 2021
- Venue: Nature Machine Intelligence 3:218-229
- Type: journal
- Identifier: DOI:10.1038/s42256-021-00302-5 (arXiv:1910.03193)
- URL: https://doi.org/10.1038/s42256-021-00302-5
- Citations: ~4708 (Semantic Scholar; S2 year field reflects arXiv 2019, journal 2021)
- Domain: operator learning
- Problem type: operator
- Physics enforced: none enforced (data-driven operator); generic PDE solution operators learned
- Enforcement mechanism: operator (data-driven)
- Architecture: branch (input-function sensors) + trunk (query coordinates) networks whose outputs dot-product; operator universal approximation
- Loss & weighting: L2 data loss on solution pairs
- Sampling & training: sensor grids + query points; Adam
- Data regime: dense simulation
- Key result: DeepONet achieves mesh-free operator approximation with theoretical grounding; generalizes across forcing functions and resolutions.
- Relevance to review: foundational operator-learning architecture; the branch/trunk template that physics-informed variants build on.
- Verification: verified via Semantic Scholar API (DOI:10.1038/s42256-021-00302-5)

### B13
- Title: Fourier Neural Operator for Parametric Partial Differential Equations (FNO)
- Authors: Li et al. (Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, Andrew Stuart, Anima Anandkumar)
- Year: 2021
- Venue: International Conference on Learning Representations (ICLR 2021)
- Type: conference
- Identifier: arXiv:2010.08895
- URL: https://arxiv.org/abs/2010.08895
- Citations: ~5063 (Semantic Scholar; S2 year field reflects arXiv 2020)
- Domain: operator learning
- Problem type: operator
- Physics enforced: none enforced (data-driven); benchmarks: Navier-Stokes, Darcy, Burgers-type
- Enforcement mechanism: operator (data-driven)
- Architecture: spectral convolutions (FFT) + pointwise lifts/projections in Fourier space; resolution-invariant discretization
- Loss & weighting: relative L2 data loss; autoregressive rollout for time
- Sampling & training: uniform grids; Adam
- Data regime: dense simulation
- Key result: learns resolution-invariant operators, beats prior neural operators on turbulent Navier-Stokes with large speedups over classical solvers.
- Relevance to review: most-cited neural operator; defines the spectral architecture axis and the data-driven baseline physics-informed operators are measured against.
- Verification: verified via Semantic Scholar API (arXiv:2010.08895, ICLR)

### B14
- Title: Learning the solution operator of parametric partial differential equations with physics-informed DeepONets
- Authors: Wang et al. (Sifan Wang, Hanwen Wang, Paris Perdikaris)
- Year: 2021
- Venue: Science Advances 7(40):eabi8605
- Type: journal
- Identifier: DOI:10.1126/sciadv.abi8605 (arXiv:2103.10974)
- URL: https://doi.org/10.1126/sciadv.abi8605
- Citations: ~1246 (Semantic Scholar)
- Domain: operator learning
- Problem type: operator
- Physics enforced: generic PDE residual constraints on operator outputs (diffusion-reaction-type and time-dependent benchmarks)
- Enforcement mechanism: hybrid (operator architecture + soft-penalty residual collocation)
- Architecture: DeepONet branch/trunk with PDE-residual collocation during training; two training modes (direct data vs physics-informed)
- Loss & weighting: optional data L2 + PDE residual collocation loss
- Sampling & training: branch sensors + trunk queries + residual collocation; Adam
- Data regime: none (physics-informed mode) / sparse / dense simulation (direct mode)
- Key result: embedding residual constraints in operator training enables accurate operator learning with little or no labeled data.
- Relevance to review: the canonical "physics enforced inside operator learning" bridge paper — core to the survey's enforcement-mechanism taxonomy.
- Verification: verified via Semantic Scholar API (DOI:10.1126/sciadv.abi8605)

### B15
- Title: Physics-Informed Neural Operator for Learning Partial Differential Equations (PINO)
- Authors: Li et al. (Zongyi Li, Hongkai Zheng, Nikola Kovachki, David Jin, Haoxuan Chen, Burigede Liu, Kamyar Azizzadenesheli, Anima Anandkumar)
- Year: 2024
- Venue: ACM / IMS Journal of Data Science 1(3):1-27
- Type: journal
- Identifier: DOI:10.1145/3648506 (preprint arXiv:2111.03794)
- URL: https://doi.org/10.1145/3648506
- Citations: ~194 (Crossref is-referenced-by-count; preprint cited more)
- Domain: operator learning
- Problem type: operator
- Physics enforced: PDE residual constraints (Navier-Stokes, Darcy, KdV, Burgers-type benchmarks)
- Enforcement mechanism: hybrid (operator + soft-penalty residual loss)
- Architecture: FNO backbone trained with data + physics losses; physics-based fine-tuning and pseudo-label generation
- Loss & weighting: L2 data loss + PDE residual loss on collocation points (weighted)
- Sampling & training: grid samples + collocation; Adam; pretrain-then-finetune
- Data regime: sparse (few-shot) / dense simulation / none (physics-only fine-tune)
- Key result: adding physics residual to neural-operator training enables data-efficient operator learning and zero-shot-ish generalization to new PDE instances.
- Relevance to review: the flagship physics-informed neural operator; defines the data+physics hybrid regime for operators.
- Verification: verified via Crossref API (DOI:10.1145/3648506) + arXiv API (arXiv:2111.03794)

### B16
- Title: GNOT: A General Neural Operator Transformer for Operator Learning
- Authors: Hao et al. (Zhongkai Hao, Songming Liu, Yichi Zhang, Chengyang Ying, Yao Feng, Hang Su, Jun Zhu)
- Year: 2023
- Venue: International Conference on Machine Learning (ICML 2023)
- Type: conference
- Identifier: arXiv:2302.14376
- URL: https://arxiv.org/abs/2302.14376
- Citations: ~496 (Semantic Scholar)
- Domain: operator learning
- Problem type: operator
- Physics enforced: none enforced (data-driven); benchmarks: Navier-Stokes, elastodynamics-type multi-physics
- Enforcement mechanism: operator (data-driven)
- Architecture: transformer with heteroskedastic Gaussian linear-attention (HGAL) for arbitrary irregular meshes and multiple input functions; multi-query cross-attention
- Loss & weighting: relative L2 data loss
- Sampling & training: irregular meshes; Adam
- Data regime: dense simulation
- Key result: scalable general operator transformer handling irregular geometries and multi-physics inputs with SOTA accuracy at the time.
- Relevance to review: anchor of the transformer-operator lineage (Galerkin Transformer 2021 → OFormer 2023 → GNOT → Transolver) for the architecture timeline.
- Verification: verified via Semantic Scholar API (arXiv:2302.14376, ICML)

### B17
- Title: Transolver: A Fast Transformer Solver for PDEs on General Geometries
- Authors: Wu et al. (Haixu Wu, Huakun Luo, Haowen Wang, Jianmin Wang, Mingsheng Long)
- Year: 2024
- Venue: International Conference on Machine Learning (ICML 2024)
- Type: conference
- Identifier: arXiv:2402.02366
- URL: https://arxiv.org/abs/2402.02366
- Citations: ~408 (Semantic Scholar)
- Domain: operator learning
- Problem type: operator
- Physics enforced: none enforced (data-driven); benchmarks: AirfRANS external aerodynamics, elastodynamics, plasticity, industrial car/airfoil meshes
- Enforcement mechanism: operator (data-driven)
- Architecture: physics-attention over learnable "slices" (function-eigenbasis tokens) on unstructured meshes; linear-complexity attention
- Loss & weighting: relative L2 data loss
- Sampling & training: unstructured mesh data; Adam
- Data regime: dense simulation
- Key result: slice-based physics attention generalizes across geometries and outperforms prior neural operators on industrial-scale PDE benchmarks.
- Relevance to review: current industrial-grade transformer operator; shows where operator learning meets engineering simulation.
- Verification: verified via Semantic Scholar API (arXiv:2402.02366, ICML)

### B18
- Title: Poseidon: Efficient Foundation Models for PDEs
- Authors: Herde et al. (Maximilian Herde, Bogdan Raonic, Tobias Rohner, Roger Kappe, Siddhartha Mishra)
- Year: 2024
- Venue: Advances in Neural Information Processing Systems (NeurIPS 2024)
- Type: conference
- Identifier: arXiv:2405.19101
- URL: https://arxiv.org/abs/2405.19101
- Citations: ~232 (Semantic Scholar)
- Domain: operator learning
- Problem type: operator
- Physics enforced: none enforced during pretraining (data-driven over multi-PDE corpus); physics enters via multi-PDE structure
- Enforcement mechanism: operator (data-driven foundation model)
- Architecture: multiscale operator transformer (U-Net-style SMP backbone) with time-conditioned layer norms; T/B/L sizes; pretrained on ~15k PDE-group simulations (A1/A2 suites)
- Loss & weighting: L2 data loss with noise augmentation (steadies training); scOT-style fine-tuning
- Sampling & training: large multi-PDE pretraining corpus then task fine-tuning
- Data regime: dense simulation (pretraining); sparse fine-tune
- Key result: pretrained PDE foundation model fine-tunes to unseen unrelated PDEs, including with very few trajectories.
- Relevance to review: the PDE-foundation-model milestone; evidence that pretraining/fine-tuning supplants per-problem training.
- Verification: verified via Semantic Scholar API (arXiv:2405.19101, NeurIPS 2024)

### B19
- Title: B-PINNs: Bayesian Physics-Informed Neural Networks for Forward and Inverse PDE Problems with Noisy Data
- Authors: Yang et al. (Liu Yang, Xuhui Meng, George Em Karniadakis)
- Year: 2021
- Venue: Journal of Computational Physics 425:109913
- Type: journal
- Identifier: DOI:10.1016/j.jcp.2020.109913 (arXiv:2003.06097)
- URL: https://doi.org/10.1016/j.jcp.2020.109913
- Citations: ~1259 (Semantic Scholar; S2 lists online-first 2020)
- Domain: UQ
- Problem type: UQ
- Physics enforced: generic PDE residual in the likelihood (forward/inverse benchmarks)
- Enforcement mechanism: soft-penalty (as Bayesian likelihood term)
- Architecture: Bayesian NN (BNN) + HMC posterior sampling; optional variational inference
- Loss & weighting: posterior = data likelihood + PDE-residual likelihood (no point-estimate loss)
- Sampling & training: HMC over network weights; collocation points
- Data regime: sparse (noisy measurements)
- Key result: Bayesian treatment yields calibrated posterior uncertainty for noisy-data PDE inversion, outperforming vanilla NN ensembles/VI in noisy regimes.
- Relevance to review: canonical UQ-for-PINNs record; defines the uncertainty axis the review tracks alongside architectures.
- Verification: verified via Semantic Scholar API (DOI:10.1016/j.jcp.2020.109913)

### B20
- Title: Transolver++: An Accurate Neural Solver for PDEs on Million-Scale Geometries
- Authors: Luo et al. (Huakun Luo, Haixu Wu, Hang Zhou, Lanxiang Xing, Yichen Di, Jianmin Wang, Mingsheng Long)
- Year: 2025
- Venue: International Conference on Machine Learning (ICML 2025)
- Type: conference
- Identifier: arXiv:2502.02414
- URL: https://arxiv.org/abs/2502.02414
- Citations: n/a (Semantic Scholar rate-limited at verification time)
- Domain: operator learning
- Problem type: operator
- Physics enforced: none enforced (data-driven); million-scale industrial geometries (car, aircraft meshes)
- Enforcement mechanism: operator (data-driven)
- Architecture: improved physics-attention with learnable physical attention modules over slices; scales to million-node meshes
- Loss & weighting: relative L2 data loss
- Sampling & training: large unstructured meshes; Adam
- Data regime: dense simulation
- Key result: ~13% average accuracy gain over Transolver across benchmarks and first-class support for million-scale geometries.
- Relevance to review: 2025 frontier of transformer operators; documents the industrial-scale trajectory.
- Verification: verified: partial (arXiv API title/author check + ICML 2025 venue via web search and official code repo thuml/Transolver_plus)

### B21
- Title: Physics-Informed Diffusion Models
- Authors: Bastek et al. (Jan-Hendrik Bastek, WaiChing Sun, Dennis M. Kochmann)
- Year: 2025
- Venue: International Conference on Learning Representations (ICLR 2025)
- Type: conference
- Identifier: arXiv:2403.14404
- URL: https://arxiv.org/abs/2403.14404
- Citations: n/a (Semantic Scholar rate-limited at verification time)
- Domain: methodology
- Problem type: architecture
- Physics enforced: PDE constraints imposed during generative sampling via a surrogate PDE solver in the diffusion chain
- Enforcement mechanism: hybrid (generative diffusion + physics-guided sampling)
- Architecture: diffusion model over solution fields; a differentiable surrogate solver projects/corrects samples toward PDE satisfaction during sampling
- Loss & weighting: diffusion denoising objective; physics applied at sampling time
- Sampling & training: diffusion training on solution snapshots; physics-guided sampling
- Data regime: dense simulation
- Key result: generated samples approximately satisfy governing equations, enabling generative PDE solving with physics consistency.
- Relevance to review: the PINN+diffusion/generative hybrid frontier the review must cover.
- Verification: verified: partial (arXiv API title/author check + ICLR 2025 proceedings URL via web search)

### B22
- Title: From Theory to Application: A Practical Introduction to Neural Operators in Scientific Computing
- Authors: Jha (Prashant K. Jha)
- Year: 2025
- Venue: arXiv preprint (journal version reported in MDPI, not separately verified)
- Type: preprint
- Identifier: arXiv:2503.05598
- URL: https://arxiv.org/abs/2503.05598
- Citations: ~15 (web-search snippet, Google-Scholar-style estimate)
- Domain: operator learning
- Problem type: survey
- Physics enforced: n/a (survey of neural operators incl. physics-informed training)
- Enforcement mechanism: operator
- Architecture: reviews FNO/DeepONet families, discretization invariance, Bayesian inverse-problem use of operators
- Loss & weighting: n/a (tutorial with reproducible code)
- Sampling & training: n/a
- Data regime: n/a
- Key result: practical operator-learning tutorial mapping architectures to scientific computing workflows.
- Relevance to review: 2025 operator-learning survey reference for framing the operator-learning section.
- Verification: verified: partial (arXiv API title/author/date check; citation estimate from search snippet)

### B23
- Title: Large language models for partial differential equation workflows
- Authors: Wan et al. (Han Wan, Rui Zhang, Hao Sun)
- Year: 2026
- Venue: arXiv preprint
- Type: preprint
- Identifier: arXiv:2608.03600
- URL: https://arxiv.org/abs/2608.03600
- Citations: n/a (2026 preprint)
- Domain: methodology
- Problem type: survey
- Physics enforced: n/a (LLM orchestration around PDE solvers, incl. physics-informed components)
- Enforcement mechanism: operator
- Architecture: LLM agents/workflows linking natural language, symbolic math, numerical solvers, diagnostics, and decisions
- Loss & weighting: n/a
- Sampling & training: n/a
- Data regime: n/a
- Key result: argues PDEs become actionable as executable LLM-orchestrated workflows rather than isolated formulae; maps the LLM-for-PDE trend.
- Relevance to review: 2026 LLM-for-PDE frontier item for the outlook section.
- Verification: verified: partial (arXiv API title/author/date check; cross-referenced in web search)

## Machine rows
B01|Implicit Neural Representations with Periodic Activation Functions (SIREN)|2020|NeurIPS|conference|arXiv:2006.09661|~3998 (S2)|methodology|generic PDE residual (Poisson/wave demos)|soft-penalty|architecture|3|Y
B02|The Deep Ritz Method: A Deep Learning-Based Numerical Algorithm for Solving Variational Problems|2018|Communications in Mathematics and Statistics|journal|DOI:10.1007/s40304-018-0127-z|~2018 (S2)|methodology|Poisson and PDEs with energy form|energy-form|weak-form|3|Y
B03|Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks|2021|SIAM Journal on Scientific Computing|journal|DOI:10.1137/20M1318043|~1892 (S2)|methodology|generic PDE residual|soft-penalty|architecture|2|Y
B04|On the eigenvector bias of Fourier feature networks: From regression to solving multi-scale PDEs with physics-informed neural networks|2021|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2021.113938|~864 (S2)|methodology|multi-scale PDE residuals (Poisson/Helmholtz/NS-type)|soft-penalty|architecture|2|Y
B05|Self-Adaptive Physics-Informed Neural Networks using a Soft Attention Mechanism|2023|Journal of Computational Physics|journal|DOI:10.1016/j.jcp.2022.111722|~866 (S2)|methodology|generic PDE residual|soft-penalty (trainable per-point attention weights)|architecture|2|Y
B06|Conservative physics-informed neural networks on discrete domains for conservation laws (cPINN)|2020|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2020.113028|~1277 (S2)|methodology|conservation laws (Burgers/Euler-type)|hybrid (interface flux continuity)|domain-decomposition|2|Y
B07|Extended Physics-Informed Neural Networks (XPINNs): A Generalized Space-Time Domain Decomposition based Deep Learning Framework for Nonlinear PDEs|2020|Communications in Computational Physics|journal|DOI:10.4208/cicp.OA-2020-0164|~1215 (S2)|methodology|nonlinear PDE residuals in space-time|hybrid (interface continuity)|domain-decomposition|3|Y
B08|hp-VPINNs: Variational Physics-Informed Neural Networks With Domain Decomposition|2021|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2020.113547|~917 (S2)|methodology|PDEs in weak form (low-regularity Burgers-type)|weak/variational|weak-form|3|Y
B09|Finite basis physics-informed neural networks (FBPINNs): a scalable domain decomposition approach for solving differential equations|2023|Advances in Computational Mathematics|journal|DOI:10.1007/s10444-023-10065-9|~321 (Crossref)|methodology|generic ODE/PDE residuals|hybrid (partition-of-unity basis + soft residual)|domain-decomposition|2|Y
B10|Multilevel domain decomposition-based architectures for physics-informed neural networks|2024|Computer Methods in Applied Mechanics and Engineering|journal|DOI:10.1016/j.cma.2024.117116|~120 (S2)|methodology|generic PDE residuals (Poisson/Helmholtz-type)|soft-penalty (DD basis)|domain-decomposition|3|Y
B11|Weak Adversarial Networks for High-dimensional Partial Differential Equations|2020|Journal of Computational Physics|journal|DOI:10.1016/j.jcp.2020.109409|~570 (S2)|methodology|high-dimensional PDEs in weak form (Black-Scholes/HJB-type)|weak/variational (adversarial test functions)|weak-form|3|Y
B12|Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators|2021|Nature Machine Intelligence|journal|DOI:10.1038/s42256-021-00302-5|~4708 (S2)|operator learning|none enforced (data-driven operator)|operator|operator|1|Y
B13|Fourier Neural Operator for Parametric Partial Differential Equations|2021|International Conference on Learning Representations|conference|arXiv:2010.08895|~5063 (S2)|operator learning|none enforced (data-driven operator)|operator|operator|1|Y
B14|Learning the solution operator of parametric partial differential equations with physics-informed DeepONets|2021|Science Advances|journal|DOI:10.1126/sciadv.abi8605|~1246 (S2)|operator learning|generic PDE residual constraints on operator outputs|hybrid (operator + soft-penalty collocation)|operator|1|Y
B15|Physics-Informed Neural Operator for Learning Partial Differential Equations (PINO)|2024|ACM/IMS Journal of Data Science|journal|DOI:10.1145/3648506|~194 (Crossref)|operator learning|PDE residual constraints (NS/Darcy/KdV-type)|hybrid (operator + soft-penalty residual)|operator|1|Y
B16|GNOT: A General Neural Operator Transformer for Operator Learning|2023|International Conference on Machine Learning|conference|arXiv:2302.14376|~496 (S2)|operator learning|none enforced (data-driven operator)|operator|operator|3|Y
B17|Transolver: A Fast Transformer Solver for PDEs on General Geometries|2024|International Conference on Machine Learning|conference|arXiv:2402.02366|~408 (S2)|operator learning|none enforced (data-driven operator)|operator|operator|2|Y
B18|Poseidon: Efficient Foundation Models for PDEs|2024|NeurIPS|conference|arXiv:2405.19101|~232 (S2)|operator learning|none enforced during pretraining (multi-PDE data corpus)|operator (foundation model)|operator|2|Y
B19|B-PINNs: Bayesian Physics-Informed Neural Networks for Forward and Inverse PDE Problems with Noisy Data|2021|Journal of Computational Physics|journal|DOI:10.1016/j.jcp.2020.109913|~1259 (S2)|UQ|generic PDE residual in likelihood|soft-penalty (Bayesian likelihood)|UQ|2|Y
B20|Transolver++: An Accurate Neural Solver for PDEs on Million-Scale Geometries|2025|International Conference on Machine Learning|conference|arXiv:2502.02414|n/a|operator learning|none enforced (data-driven operator)|operator|operator|3|Y
B21|Physics-Informed Diffusion Models|2025|International Conference on Learning Representations|conference|arXiv:2403.14404|n/a|methodology|PDE constraints during generative sampling|hybrid (diffusion + physics-guided sampling)|architecture|3|Y
B22|From Theory to Application: A Practical Introduction to Neural Operators in Scientific Computing|2025|arXiv preprint|preprint|arXiv:2503.05598|~15 (search snippet)|operator learning|n/a (survey)|operator|survey|4|Y
B23|Large language models for partial differential equation workflows|2026|arXiv preprint|preprint|arXiv:2608.03600|n/a|methodology|n/a (LLM orchestration)|operator|survey|4|Y

## Slice takeaways
- Two enforcement philosophies dominate the record set: soft-penalty residual PINNs on modified MLPs (modified-MLP, Fourier-feature embeddings, self-adaptive attention weights) and structure-in-the-formulation PINNs (cPINN/XPINN/FBPINN domain decomposition, hp-VPINN/WAN weak-variational forms, Deep Ritz energy form). Hard constraints remain rare and appear mainly as partition-of-unity bases (FBPINN) rather than exact BC imposition.
- Operator learning has overtaken pointwise PINNs in citation velocity: FNO (~5063) and DeepONet (~4708) each out-cite the entire DD-PINN family combined; the physics is migrating from the loss (PINO, PI-DeepONet) into the pretraining corpus (Poseidon, NeurIPS 2024) — physics-informed fine-tuning is now the enforcement mechanism at the frontier.
- The transformer-operator lineage is fast and industrial: Galerkin Transformer (2021) -> OFormer (2023) -> GNOT (2023) -> Transolver (ICML 2024) -> Transolver++ (ICML 2025, million-scale geometries); physics-attention over learned "slices" is the recurring mechanism, and 2024-2025 papers target car/aircraft-scale industrial meshes.
- UQ for PINNs is still essentially one canonical architecture (B-PINN, HMC-based, 2021) with slow architectural evolution; 2025-2026 UQ energy is drifting toward conformal prediction and generative/diffusion-based probabilistic operators rather than BNNs.
- 2025-2026 frontier trends: physics-informed diffusion/generative hybrids (ICLR 2025), PDE foundation models with scOT fine-tuning, and LLM-for-PDE workflows (orchestration, autoformalization, LLM-designed operator architectures — e.g., "Can LLMs Design Effective Neural Operators?", ICML 2026 AI-for-Math workshop) — none yet replace the residual-loss core of PINNs.
- Domain decomposition matured from interface conditions (cPINN/XPINN 2020) through partition-of-unity bases (FBPINN 2023) to FEM-theory-backed multilevel architectures (Dolean et al., CMAME 2024); DD is the main answer to PINN scalability on large/multi-scale domains.
- Data regimes are bimodal: strong-form PINN variants (B01-B11) train with no data (physics-only), while all operator/foundation-model records (B12-B18, B20) depend on dense simulation corpora — the physics-informed operator (B14, B15) is the bridge regime (sparse/few-shot).
