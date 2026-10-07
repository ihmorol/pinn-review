# Slice E: Biomedical, geoscience, civil/structural applications
(Scout E, 2026-10-06. Window 2021-2026; two flagged pre-window records retained because they are canonical for their subdomain.)

## Queries used
1. "physics-informed neural network hemodynamics blood flow Navier-Stokes"
2. "physics-informed neural networks seismic full waveform inversion Rasht-Behesht"
3. "Friha physics-informed neural networks healthcare use case"
4. "physics-informed neural networks tumor growth glioblastoma reaction-diffusion"
5. "physics-informed neural network cardiac digital twin clinical 2025 electrophysiology"
6. "physics-informed neural networks oil and gas industry application 2025"
(3 further queries were aborted by tool concurrency limits and re-issued within the above set; verification done via Semantic Scholar + Crossref APIs.)

## Screening summary
candidates screened: ~24; included: 14.
Dropped/notable: Friha et al. "PINNs... healthcare use case" — NOT FOUND in Crossref (author+bibliographic queries) nor Semantic Scholar; treated as unverified, excluded, replaced by E09 (verified 2025 biomedical PIML survey). Kadeethum "2021" attribution corrected: his verified PINN subsurface paper is PLOS ONE 2020 (E03); the CMAME 2022 mixed-formulation PINN-FEM paper is Rezaei et al. (not Kadeethum). Kamali, Sarabian & Laksari, "Elasticity imaging using PINNs", Acta Biomaterialia 2023, DOI 10.1016/j.actbio.2022.11.024 (91 cites, Crossref) verified but excluded for space. Sahli Costabal et al., "PINNs for cardiac activation mapping", Frontiers in Physics 2020, DOI 10.3389/fphy.2020.00042 (452 cites, S2) — pre-window canonical Eikonal activation-mapping reference, see takeaways.

## Paper records

### E01
- Title: A physics-informed deep learning framework for inversion and surrogate modeling in solid mechanics / Haghighat & Juanes / 2021 / Computer Methods in Applied Mechanics and Engineering / journal / DOI 10.1016/j.cma.2021.113741 / https://doi.org/10.1016/j.cma.2021.113741 / Citations 1253 (S2)
- Domain: solid mechanics (elasticity), geomechanics; industry: civil/energy
- Problem type: both (forward + inverse modulus identification; surrogate)
- Physics enforced: linear elasticity equilibrium ∇·σ+b=0 with σ=C:ε (heterogeneous E), incl. functional-Fourier variants
- Enforcement mechanism: autodiff PDE residual + data loss (SciANN)
- Architecture: MLP/SciANN with Fourier-feature input; Loss: PDE residual + displacement data; Sampling: collocation; Data: sparse synthetic/full-field displacement
- Key result: accurate inversion of heterogeneous Young's modulus from sparse displacement data; Relevance: template elasticity-inverse PINN for civil/solid mechanics section. Verification: verified via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.cma.2021.113741

### E02
- Title: Physics-Informed Neural Networks (PINNs) for Wave Propagation and Full Waveform Inversions / Rasht-Behesht, Huber, Shukla, Karniadakis / 2022 / Journal of Geophysical Research: Solid Earth / journal / DOI 10.1029/2021jb023120 / https://doi.org/10.1029/2021JB023120 / Citations 412 (Crossref)
- Domain: seismology/FWI; industry: oil&gas exploration, geoscience
- Problem type: both (wavefield simulation, source imaging, FWI velocity inversion)
- Physics enforced: acoustic + elastic wave equations (displacement-form elastic wave equation)
- Enforcement mechanism: autodiff wave-equation residual + seismogram data loss
- Architecture: continuous CNNs (cCNNs) with Fourier features; Loss: PDE residual + data misfit; Sampling: collocation; Data: synthetic seismograms (Marmousi etc.)
- Key result: FWI-quality velocity models without meshing; Relevance: flagship geoscience PINN application. Verification: verified via https://api.crossref.org/works/10.1029/2021jb023120 (note: venue is JGR Solid Earth, not GJI)

### E03
- Title: Physics-informed neural networks for solving nonlinear diffusivity and Biot's equations / Kadeethum, Jørgensen, Nick / 2020 / PLOS ONE / journal / DOI 10.1371/journal.pone.0232683 / https://doi.org/10.1371/journal.pone.0232683 / Citations 118 (Crossref)
- Domain: subsurface flow & poromechanics; industry: oil&gas, geological storage
- Problem type: both (forward + inverse heterogeneous coefficients)
- Physics enforced: nonlinear diffusivity equation + Biot's coupled poroelasticity (flow-deformation)
- Enforcement mechanism: autodiff PDE residual loss; accuracy benchmarked vs FEM
- Architecture: FCN; Loss: PDE residual (+BC/IC); Sampling: collocation; Data: synthetic heterogeneous media
- Key result: PINN competitive with FEM on smooth fields, degrades on sharp heterogeneity; Relevance: canonical subsurface-PINN benchmark and baseline for hydrology section. Verification: verified via https://api.crossref.org/works/10.1371/journal.pone.0232683 (year 2020, not 2021)

### E04
- Title: Physics-Informed Neural Networks With Monotonicity Constraints for Richardson-Richards Equation: Estimation of Constitutive Relationships and Soil Water Flux Density From Volumetric Water Content Measurements / Bandai & Ghezzehei / 2021 / Water Resources Research / journal / DOI 10.1029/2020wr027642 / https://doi.org/10.1029/2020WR027642 / Citations 126 (Crossref)
- Domain: vadose-zone hydrology / groundwater; industry: agriculture, environmental
- Problem type: inverse (constitutive relations + flux estimation)
- Physics enforced: 1D Richardson-Richards unsaturated-flow equation with monotone hydraulic constitutive laws (K(θ), h(θ))
- Enforcement mechanism: output-transformation imposing monotonicity + PDE residual loss
- Architecture: monotonicity-constrained MLP; Loss: PDE residual + soil-moisture data; Sampling: collocation; Data: θ(z,t) sensor time series
- Key result: recovers conductivity/retention curves and flux from moisture data alone; Relevance: exemplar of hard-constraint (monotonicity) enforcement in hydrology. Verification: verified via https://api.crossref.org/works/10.1029/2020wr027642

### E05
- Title: EP-PINNs: Cardiac Electrophysiology Characterisation Using Physics-Informed Neural Networks / Herrero Martin, Oved, Chowdhury, Ullmann, Peters, Bharath, Varela / 2022 / Frontiers in Cardiovascular Medicine / journal / DOI 10.3389/fcvm.2021.768419 / https://doi.org/10.3389/fcvm.2021.768419 / Citations 57 (Crossref)
- Domain: cardiac electrophysiology; industry: hospital cardiology
- Problem type: inverse (tissue excitability/conduction characterization)
- Physics enforced: Monodomain PDE + Aliev-Panfilov ionic model
- Enforcement mechanism: autodiff PDE residual + sparse transmembrane-potential data loss
- Architecture: MLP estimating heterogeneous parameter fields (a, b, D); Loss: PDE + Vm data; Sampling: collocation + data points; Data: sparse in-silico Vm + in-vitro optical mapping under drugs
- Key result: recovers heterogeneous conduction/excitability; drug effects characterized; Relevance: canonical "how EP physics is enforced" example. Verification: verified via https://api.crossref.org/works/10.3389/fcvm.2021.768419 + abstract

### E06
- Title: Personalising left-ventricular biophysical models of the heart using parametric physics-informed neural networks / Buoso, Joyce, Kozerke / 2021 / Medical Image Analysis / journal / DOI 10.1016/j.media.2021.102066 / https://doi.org/10.1016/j.media.2021.102066 / Citations 89 (Crossref)
- Domain: cardiac biomechanics / imaging; industry: hospital cardiology, MRI
- Problem type: inverse (personalization of LV active-mechanics parameters)
- Physics enforced: energy potential functional of hyperelastic, anisotropic, nearly-incompressible active LV material
- Enforcement mechanism: energy-functional loss + RBF output subspace (from FE solutions)
- Architecture: parametric PINN (pPINN) on radial-basis subspace; Loss: strain-energy functional + image/observational data; Data: imaging-derived LV deformation
- Key result: fast patient-specific LV biomechanics vs repeated FE solves; Relevance: energy-based (weak/variational) enforcement pattern for biomedical section. Verification: verified via https://api.crossref.org/works/10.1016/j.media.2021.102066 + abstract

### E07
- Title: Physics-Informed Neural Networks for Brain Hemodynamic Predictions Using Medical Imaging / Sarabian, Babaee, Laksari / 2022 / IEEE Transactions on Medical Imaging / journal / DOI 10.1109/tmi.2022.3161653 / https://doi.org/10.1109/TMI.2022.3161653 / Citations 126 (Crossref)
- Domain: cerebrovascular hemodynamics; industry: hospital neurology/imaging
- Problem type: inverse / imaging (assimilation of sparse clinical measurements)
- Physics enforced: 1D reduced-order blood-flow model (mass/momentum conservation in arterial network)
- Enforcement mechanism: ROM-constrained PINN hybrid + sparse TCD ultrasound data loss
- Architecture: PINN coupled with 1D ROM simulations; Loss: ROM consistency + TCD velocity data; Data: clinical TCD + imaging
- Key result: high-resolution physically consistent brain hemodynamics from sparse clinical data; Relevance: hospital-data assimilation pattern for hemodynamics subsection. Verification: verified via https://api.crossref.org/works/10.1109/tmi.2022.3161653 + abstract

### E08
- Title: Personalized predictions of Glioblastoma infiltration: Mathematical models, Physics-Informed Neural Networks and classifier / Zhang, Ezhov, Balcerak, Zhu, Wiestler, Menze / 2025 / Medical Image Analysis / journal / DOI 10.1016/j.media.2024.103423 / https://doi.org/10.1016/j.media.2024.103423 / Citations 33 (Crossref)
- Domain: oncology / tumor growth; industry: hospital oncology
- Problem type: inverse (patient-specific parameter inference) + prediction
- Physics enforced: reaction-diffusion PDE of glioblastoma cell-density invasion
- Enforcement mechanism: autodiff PDE residual + single 3D MRI snapshot data loss
- Architecture: PINN for cell density + parameter estimation; Loss: reaction-diffusion residual + MRI segmentation; Data: single 3D structural MRI per patient
- Key result: patient-specific proliferation/diffusion estimates predicting infiltration beyond enhancing core; Relevance: 2025 clinical-flagship tumor-growth PINN. Verification: verified via https://api.crossref.org/works/10.1016/j.media.2024.103423

### E09
- Title: Recent advancements and applications of physics-informed machine learning in biomedical research / Roquemen-Echeverri & Mosquera-Lopez / 2025 / Current Opinion in Biomedical Engineering / journal (review) / DOI 10.1016/j.cobme.2025.100612 / https://doi.org/10.1016/j.cobme.2025.100612 / Citations 10 (Crossref)
- Domain: biomedical/healthcare (survey: imaging, cardiology, oncology, digital twins)
- Problem type: survey (covers forward/inverse/imaging applications)
- Physics enforced: n/a (survey of embedded PDE/ODE constraints in biomedical models)
- Enforcement mechanism: n/a (categorizes residual-loss, hybrid, operator-learning approaches)
- Key result: maps 2023-2025 biomedical PIML trends and open clinical gaps; Relevance: dedicated healthcare survey anchor for the review (substitute for unverifiable Friha et al.). Verification: verified via https://api.crossref.org/works/10.1016/j.cobme.2025.100612

### E10
- Title: Meta-learning Physics-Informed Neural Networks for Personalized Cardiac Modeling / Toloubidokhti, Missel, Lian, Wang et al. / 2025 / MICCAI 2025 (LNCS) / conference / DOI 10.1007/978-3-032-04927-8_33 / https://doi.org/10.1007/978-3-032-04927-8_33 / Citations 1 (Crossref)
- Domain: cardiac digital twins; industry: hospital cardiology (pre-clinical)
- Problem type: operator / parametric (parameter-to-activation-map mapping)
- Physics enforced: Eikonal equation (activation-time physics)
- Enforcement mechanism: meta-trained PINN; per-patient CV fields from feedforward pass (no retraining)
- Architecture: meta-learned PINN over geometries/scars; Loss: Eikonal residual + sparse activation data; Data: 200 synthetic Eikonal cases (4 human MRI geometries) + real animal epicardial maps
- Key result: instant personalization to unseen subjects incl. experimental data; Relevance: 2025 clinical-workflow digital-twin trend. Verification: verified via https://api.crossref.org/works/10.1007/978-3-032-04927-8_33 + MICCAI page

### E11
- Title: Cardiovascular digital twins using a Windkessel physics informed neural network / Osman, Sel, Spatz, Jafari / 2026 / npj Digital Medicine / journal / DOI 10.1038/s41746-026-02610-9 / https://doi.org/10.1038/s41746-026-02610-9 / Citations 1 (Crossref)
- Domain: cardiovascular monitoring; industry: clinical/wearables (human pilot)
- Problem type: inverse (hemodynamic parameter estimation + BP prediction)
- Physics enforced: 2- and 3-element Windkessel ODEs (pressure-flow-resistance-compliance)
- Enforcement mechanism: ODE residual loss + wearable bioimpedance data loss
- Architecture: WPINN; Loss: Windkessel residual + Bio-Z signals; Data: wearable bioimpedance ring/wristband from N=6 healthy + N=23 hypertensive participants
- Key result: 12-25% RMSE improvement over data-driven baselines in a human pilot; Relevance: rare 2026 clinical-industrial pilot (hospital/wearables). Verification: verified via https://api.crossref.org/works/10.1038/s41746-026-02610-9 + PMC13254049

### E12
- Title: Physics-Informed Neural Networks with skip connections for modeling and control of gas-lifted oil wells / Kittelsen, Antonelo, Camponogara, Imsland / 2024 / Applied Soft Computing / journal / DOI 10.1016/j.asoc.2024.111603 / https://doi.org/10.1016/j.asoc.2024.111603 / Citations 27 (Crossref)
- Domain: production engineering / well control; industry: oil&gas (industrial deployment-oriented)
- Problem type: both (long-range prediction + model predictive control)
- Physics enforced: first-principles dynamic ODE model of gas-lifted oil wells (tubing/annulus flow dynamics)
- Enforcement mechanism: PINC framework — ODE residual loss, open-ended rollout, coupled with MPC
- Architecture: hierarchical PINC with skip connections; Loss: ODE residual + measurement fit (noise-robust); Data: noisy well simulations/measurements
- Key result: robust long-range prediction and bottom-hole-pressure MPC under noise; Relevance: documented oil&gas industrial PINN pilot. Verification: verified via https://api.crossref.org/works/10.1016/j.asoc.2024.111603 + abstract

### E13
- Title: Physics-informed neural network modelling of uplift behaviour of segmental linings during shield tunnelling / Shen, Wu, Zhou / 2025 / Journal of Rock Mechanics and Geotechnical Engineering / journal / DOI 10.1016/j.jrmge.2025.08.001 / https://doi.org/10.1016/j.jrmge.2025.08.001 / Citations 13 (Crossref)
- Domain: geotechnical / shield tunnel construction; industry: construction
- Problem type: both (lining uplift response modelling)
- Physics enforced: segmental-lining uplift mechanics (soil-structure interaction model) — exact governing PDE not in indexed abstract, needs-check
- Enforcement mechanism: PINN residual on lining-uplift model (needs-check detail)
- Architecture: needs-check; Data: shield-tunnelling case/engineering data
- Key result: PINN reproduces uplift behaviour of segmental linings during tunnelling; Relevance: 2025 construction-industry PINN instance (satisfies industrial-pilot quota). Verification: verified: partial (Crossref record + S2 title match; physics detail needs-check)

### E14
- Title: A Physics-Informed Neural Network for the Nonlinear Damage Identification in a Reinforced Concrete Beam / Yamaguchi & Mizutani / 2024 / Structural Control and Health Monitoring / journal / DOI 10.1155/2024/5532909 / https://doi.org/10.1155/2024/5532909 / Citations 37 (Crossref)
- Domain: structural health monitoring (RC bridge piers post-earthquake); industry: civil infrastructure
- Problem type: inverse (damage location/extent identification)
- Physics enforced: nonlinear multi-DOF equations of motion (all-nonlinear-spring MDOF structural model)
- Enforcement mechanism: EOM residual loss + measured vibration response data
- Architecture: DL-estimated large parameter set in nonlinear spring model; Loss: dynamics residual + responses; Data: measured structural responses (shake-table/field)
- Key result: identifies multiple nonlinear damage locations/extents beyond linear model updating; Relevance: nonlinear-physics enforcement example for SHM subsection. Verification: verified via https://api.crossref.org/works/10.1155/2024/5532909 + abstract

## Machine rows
E01|A physics-informed deep learning framework for inversion and surrogate modeling in solid mechanics|2021|Computer Methods in Applied Mechanics and Engineering|journal|10.1016/j.cma.2021.113741|1253 (S2)|Civil/solid mechanics (construction)|Linear elasticity equilibrium with heterogeneous modulus|autodiff PDE residual + data loss (SciANN)|both|1|Y
E02|Physics-Informed Neural Networks (PINNs) for Wave Propagation and Full Waveform Inversions|2022|Journal of Geophysical Research: Solid Earth|journal|10.1029/2021jb023120|412 (Crossref)|Geoscience/seismic (oil-gas exploration)|Acoustic + elastic wave equations|cCNN autodiff wave residual + seismogram data|both|1|Y
E03|Physics-informed neural networks for solving nonlinear diffusivity and Biot's equations|2020|PLOS ONE|journal|10.1371/journal.pone.0232683|118 (Crossref)|Geoscience/subsurface flow (oil-gas)|Nonlinear diffusivity + Biot poroelasticity|autodiff PDE residual vs FEM baseline|both|2|Y
E04|Physics-Informed Neural Networks With Monotonicity Constraints for Richardson-Richards Equation|2021|Water Resources Research|journal|10.1029/2020wr027642|126 (Crossref)|Hydrology/groundwater (agri-environmental)|Richardson-Richards unsaturated flow|monotonicity-constrained output + PDE residual|inverse|2|Y
E05|EP-PINNs: Cardiac Electrophysiology Characterisation Using Physics-Informed Neural Networks|2022|Frontiers in Cardiovascular Medicine|journal|10.3389/fcvm.2021.768419|57 (Crossref)|Biomedical/cardiac EP (hospital)|Monodomain + Aliev-Panfilov ionic model|autodiff PDE residual + sparse Vm data|inverse|1|Y
E06|Personalising left-ventricular biophysical models of the heart using parametric physics-informed neural networks|2021|Medical Image Analysis|journal|10.1016/j.media.2021.102066|89 (Crossref)|Biomedical/cardiac imaging (hospital MRI)|Hyperelastic anisotropic energy potential|energy-functional loss + RBF output subspace|inverse|2|Y
E07|Physics-Informed Neural Networks for Brain Hemodynamic Predictions Using Medical Imaging|2022|IEEE Transactions on Medical Imaging|journal|10.1109/tmi.2022.3161653|126 (Crossref)|Biomedical/cerebrovascular hemodynamics (hospital)|1D reduced-order blood-flow model|ROM-PINN hybrid + sparse TCD data|inverse|2|Y
E08|Personalized predictions of Glioblastoma infiltration: Mathematical models, Physics-Informed Neural Networks and classifier|2025|Medical Image Analysis|journal|10.1016/j.media.2024.103423|33 (Crossref)|Biomedical/oncology (hospital)|Reaction-diffusion tumor-invasion PDE|autodiff PDE residual + single-3D-MRI data|inverse|1|Y
E09|Recent advancements and applications of physics-informed machine learning in biomedical research|2025|Current Opinion in Biomedical Engineering|journal|10.1016/j.cobme.2025.100612|10 (Crossref)|Biomedical/healthcare survey|n/a survey of embedded PDE-ODE constraints|n/a categorizes residual-loss/hybrid/operator approaches|survey|2|Y
E10|Meta-learning Physics-Informed Neural Networks for Personalized Cardiac Modeling|2025|MICCAI 2025 (LNCS)|conference|10.1007/978-3-032-04927-8_33|1 (Crossref)|Biomedical/cardiac digital twins (pre-clinical)|Eikonal equation|meta-trained PINN fast CV-field inference|operator|2|Y
E11|Cardiovascular digital twins using a Windkessel physics informed neural network|2026|npj Digital Medicine|journal|10.1038/s41746-026-02610-9|1 (Crossref)|Biomedical/cardiovascular wearables (clinical pilot)|2- and 3-element Windkessel ODEs|ODE residual + wearable bioimpedance data|inverse|2|Y
E12|Physics-Informed Neural Networks with skip connections for modeling and control of gas-lifted oil wells|2024|Applied Soft Computing|journal|10.1016/j.asoc.2024.111603|27 (Crossref)|Oil-gas/production control (industrial)|Gas-lift well dynamic ODE model|PINC ODE residual + MPC coupling|both|3|Y
E13|Physics-informed neural network modelling of uplift behaviour of segmental linings during shield tunnelling|2025|Journal of Rock Mechanics and Geotechnical Engineering|journal|10.1016/j.jrmge.2025.08.001|13 (Crossref)|Construction/geotech tunneling|Segmental-lining uplift soil-structure mechanics|PDE residual on lining-uplift model|both|4|Y
E14|A Physics-Informed Neural Network for the Nonlinear Damage Identification in a Reinforced Concrete Beam|2024|Structural Control and Health Monitoring|journal|10.1155/2024/5532909|37 (Crossref)|Civil/SHM bridges|Nonlinear MDOF spring equations of motion|EOM residual + measured response data|inverse|3|Y

## Slice takeaways
- Physics palette is domain-striking: cardiology uses Monodomain+ionic models (EP-PINNs) and Eikonal activation equations (MICCAI 2025); geoscience uses acoustic/elastic wave equations for FWI and Biot/nonlinear-diffusivity/Richards equations for subsurface; civil uses linear-elasticity equilibrium and nonlinear MDOF structural dynamics; biomed mechanics uses variational energy functionals rather than strong-form residuals (Buoso).
- Enforcement is overwhelmingly soft residual losses via autodiff, but the slice shows a second wave: hard monotonicity constraints (Bandai WRR), output-subspace restriction with energy-based losses (Buoso), ROM-coupled hybrid constraints (Sarabian TMI), and meta-learning amortization for instant clinical personalization (MICCAI 2025).
- 2025-2026 momentum is clinical/industrial: glioblastoma personalization (MedIA 2025), biomedical PIML survey (COBE 2025), Eikonal meta-PINN cardiac twins (MICCAI 2025), Windkessel wearable pilot on N=29 humans (npj Digital Medicine 2026), shield-tunnelling lining PINN (JRMGE 2025) and gas-lift well MPC (Applied Soft Computing 2024) — usable as the review's "toward deployment" evidence.
- Verification corrections for the dossier: Rasht-Behesht et al. 2022 is in JGR Solid Earth (not Geophysical Journal International); Kadeethum et al.'s subsurface PINN paper is PLOS ONE 2020 (not 2021), and the CMAME 2022 PINN-vs-FEM mixed-formulation paper is Rezaei et al.; "Friha et al." healthcare PINN survey could not be verified in Crossref or Semantic Scholar (excluded; Roquemen-Echeverri & Mosquera-Lopez 2025 substitutes).
- Canonical pre-window anchor to cite in the survey's cardiac subsection: Sahli Costabal et al., "PINNs for cardiac activation mapping" (Frontiers in Physics 2020, DOI 10.3389/fphy.2020.00042, 452 cites per S2, Eikonal-based inverse activation mapping).
