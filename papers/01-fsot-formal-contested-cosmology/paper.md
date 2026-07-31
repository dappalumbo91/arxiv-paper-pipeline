---
title: "Formally Verified Parameter-Free Scalar Engine for Contested Cosmology: Lean 4 and Multi-Prover Certification of Fluid Spacetime Omni-Theory"
# Softer alternate (if astro-ph.CO moderators prefer less claim-forward wording):
# "Machine-Checked Zero Free-Parameter Scalar Engine for Contested Cosmology: Lean 4 Formalization of Fluid Spacetime Omni-Theory with Five-Prover Triangulation"
author: "Damian Arthur Palumbo"
date: "2026-07-31"
edition_freeze: "2026-07-16"
arxiv_primary: "cs.LO"
arxiv_secondary: ["astro-ph.CO", "math.LO"]
repository: "https://github.com/dappalumbo91/FSOT-2.1-Lean"
status: "draft"
---

# Formally Verified Parameter-Free Scalar Engine for Contested Cosmology: Lean 4 and Multi-Prover Certification of Fluid Spacetime Omni-Theory

**Damian Arthur Palumbo**  
Independent researcher  

**Code and formalization (canonical):**  
[https://github.com/dappalumbo91/FSOT-2.1-Lean](https://github.com/dappalumbo91/FSOT-2.1-Lean)

**Edition freeze:** 2026-07-16 claim numbers; recommended code tip **`8a44947`** (includes `matplotlib>=3.8` in `requirements.txt`).  
All numerical headline claims are intended to reproduce from the public repository.

> **Software availability.**  
> Lean 4 formalization (`FSOT/Formal/`), five-prover obligation export, Python decimal oracle (`vendor/fsot_compute.py`), contested-sector ledger, preregistered predictions **PRED-001â€“041**, and the one-command verification entry point:
>
> **[https://github.com/dappalumbo91/FSOT-2.1-Lean](https://github.com/dappalumbo91/FSOT-2.1-Lean)**
>
> ```bash
> git clone https://github.com/dappalumbo91/FSOT-2.1-Lean.git
> cd FSOT-2.1-Lean
> pip install -r requirements.txt
> python scripts/run_publication_verification_bundle.py
> ```
>
> Full cross-proof (when local Lean/Coq/Isabelle/F\*/Rust toolchains are installed):  
> `python scripts/run_publication_verification_bundle.py --full-cross-proof`
>
> Cosmology navigation: `python scripts/query_fsot_domain_navigator.py --intent cosmology_cmb`  
> Freeze checker (paper package): `python verify_paper_claims.py --fsot-root . --strict-hash`
>
> **arXiv Comments:** paste from `comments.txt` in this package.

---

## Abstract

Modern physics is accurate in fragments and fragmented in architecture: sector models accumulate free parameters, and contested observablesâ€”especially the Hubble constant $H_0$ dual-anchor tensionâ€”expose the cost. We present a machine-checked, zero free-parameter scalar engine for Fluid Spacetime Omni-Theory (FSOT): a seed-derived vitality scalar $\mathrm{raw}\_S=\mathrm{term}_1+\mathrm{term}_2+\mathrm{term}_3$ built only from $\pi$, $e$, $\varphi$, $\gamma$ (Eulerâ€“Mascheroni), and Catalanâ€™s $G$, with domain routes as preregistered folds rather than per-observable least-squares knobs.

Formally, Lean 4 is primary authority; atomic obligations are exported to Coq/Rocq, Isabelle/HOL, F\*, and Rust executable replayâ€”**1,863** obligations in the edition freeze with `overall_ok: true`, bound to a SHA-256-pinned Python oracle. Empirically, contested-sector pooled median error is **0.030%** across 13 monitored observables (dual-anchor $H_0$, $\sigma_8$, BBN lithium proxy, hierarchy, $w_a$), versus a ~15% typical baseline tension scale for open $\Lambda$CDM/SM panels. Dual-anchor $H_0$ uses a bubble-bleed route ($\mathrm{term}_3$ turbulence with $\mathrm{perceived\_adjust}$ on $\mathrm{term}_1$); preregistered PRED-001 places the FSOT bridge scalar strictly between Planck 2018 CMB and Riess et al. local anchors.

We scope this paper to the formal spine and contested cosmologyâ€”not a 400-domain monograph. The full 402-domain atlas (536,740 records; 394/394 domains under a $\le 0.5\%$ green gate) is the living GitHub thesis. Readers can accept or reject claims by running the published verification bundle.

**Keywords:** formal methods; Lean 4; multi-prover verification; parameter-free models; Hubble tension; Fluid Spacetime Omni-Theory; reproducible science

---

## 1. Introduction

### 1.1 The fragmentation problem

Twentieth-century physics delivered extraordinary local theoriesâ€”general relativity, quantum mechanics, the Standard Model, and $\Lambda$CDM cosmologyâ€”each optimized inside institutional and mathematical boundaries. The empirical cost of that success is visible where the boundaries meet:

| Symptom | Example |
|---------|---------|
| Parameter proliferation | Dark-sector densities, Yukawa couplings, inflation potentials |
| Cross-sector tension | Local $H_0$ (Riess et al.) vs CMB inference (Planck Collaboration 2018) |
| Siloed success | Cosmology papers do not certify molecular chemistry; chemistry papers do not certify $H_0$ |
| Unfalsifiable breadth | â€œTheories of everythingâ€ without executable kill criteria |

$\Lambda$CDM explains CMB and large-scale structure with excellent *internal* consistency, yet the $H_0$ tension (local distance ladder vs early-universe inference) and $\sigma_8$ tensions remain open scientific problems [1,2,3]. The Standard Model similarly succeeds sector-by-sector while leaving hierarchy and dark-sector couplings as free or lightly constrained structure.

FSOT does not reject the *data* those theories explain. It rejects the **architecture**: many knobs, many silos, no single engine that must survive formal and empirical gates at once.

### 1.2 What FSOT claims (operational statement)

> Reality is modeled as a **25-dimensional fluid condensate**. Observed regimes of space, time, matter, and measurement are folds of a single scalar field $\mathrm{raw}\_S$, computed from seed geometry with **no per-observable least-squares tuning**.

This is a **falsifiable engineering specification**, not a prose-only ontology. Routing coordinates $(D_{\mathrm{eff}}, \delta\psi, \mathrm{recent\_hits}, \mathrm{observed})$ are declared in domain manifests before comparison; failed green gates are ledger events, not opportunities for silent parameter rescue.

### 1.3 Why formal methods as scientific instruments

Proof assistants (Lean, Coq, Isabelle, F\*) are standard in software verification. Their use as **scientific instruments**â€”exporting atomic physical obligations, triangulating across independent kernels, and binding formal terms to a decimal oracleâ€”is still uncommon, though growing (e.g. formal chemical theory [4], HepLean for high-energy physics [5]). Numeric agreement alone is not a machine-checked guarantee: floating-point scripts can drift; caches can be overwritten; â€œpassedâ€ benchmarks can silently change meaning. FSOTâ€™s response is a **cross-gauntlet**:

1. **Lean 4** primary formalization of the scalar engine and domain certificates.  
2. **Coq/Rocq, Isabelle/HOL, F\*, Rust** independent replay of exported obligations.  
3. **Python oracle** `vendor/fsot_compute.py` hash-locked as decimal authority.  
4. **Preregistered predictions** PRED-001â€“041 and per-domain kill criteria.

### 1.4 Scope of this paper

A monolithic 400-domain Theory-of-Everything paper is nearly impossible to place cleanly and invites the critique that no single definitive claim is tested. Following the scope discipline of HepLean (three HEP areas [5]) and Bobbin et al. (selected classical theories [4]), this manuscript is **focused**:

| In scope | Out of main body (GitHub living thesis) |
|----------|------------------------------------------|
| Scalar engine definition and zero free-parameter statement | Full 402-domain atlas narrative |
| Five-prover formal methodology and obligation counts | Engineering fuels, wet-lab longevity stacks |
| Contested-sector cosmology ($H_0$, bubble-bleed, $\sigma_8$, BBN proxies) | Linguistics, consciousness philosophy deep-dives |
| Tight core high-precision physics domains | Propulsion / transporter simulation volumes |
| Falsifiability registry and one-command reproduction | Optional ESP32 hardware observer |

### 1.5 Contributions

1. **Unified scalar architecture.** A single seed-derived engine $\mathrm{raw}\_S = \mathrm{term}_1 + \mathrm{term}_2 + \mathrm{term}_3$ evaluated across **402 routed scientific domains** (35 core + 367 extension panels) and **536,740** empirical records, with **no per-observable least-squares tuning**. *Category: architecture + numerical pipeline (not a single Lean theorem of physical truth).*

2. **Cross-domain empirical closure (context).** **394/394** public benchmark domains pass a $\le 0.5\%$ pooled median error gate; cross-domain pooled median is **0.013%** (Planck 2018, PDG 2024, NIST/CODATA targets per row). *Category: empirical / numerically verified.* Used here only as context.

3. **Contested-sector readouts.** Unified FSOT predictions on $H_0$, $\sigma_8$, BBN, hierarchy, and dark-energy proxies achieve **0.030%** pooled median across 13 actively monitored observables vs ~15% typical $\Lambda$CDM/SM sector baseline tension scale. *Category: empirical comparison under preregistered discriminants.*

4. **Five-prover formal triangulation.** **1,863** atomic obligations (edition freeze) exported to Lean 4, Coq/Rocq, Isabelle/HOL, F\*, and Rust with `overall_ok: true`. *Category: proved / certified obligations at exported statements.*

5. **Executable falsification registry.** Preregistered predictions **PRED-001â€“041**, per-domain kill criteria, and a one-command verification bundle. *Category: methodological contribution.*

### 1.6 Claim taxonomy (required for fair reading)

| Category | Definition | Examples in this work |
|----------|------------|------------------------|
| **Proved** | Machine-checked in proof assistants / executable replay; no `sorry` on formal spine | Domain sign certificates; exported atomic obligations; `overall_ok: true` |
| **Numerically verified** | Oracle/hash gate match; reproducible cache | Wave-1 cosmology caches; domain oracle rows |
| **Empirical** | Agreement with external measured authorities | $H_0$ vs Planck 2018; contested-sector table |
| **Interpretation** | Physics narrative, not machine-checked truth | Bubble-bleed as fluid phase bleeding; 25D ontology |
| **Inventory** | Counts of assets, not per-row proofs | Module counts; panel registries |

**This paper does not claim that Lean proves FSOT is fundamental physics.** Lean proves internal certificates at declared parameters. Empirical tables test external agreement. Interpretation remains interpretation. In particular, â€œtension resolutionâ€ in the FSOT ledger means *unified dual-anchor routing with preregistered discriminants and low relative error under the repository metric*â€”not a claim that the observational astrophysics community has adopted a new consensus $H_0$ posterior.

---

## 2. The Scalar Engine (Full Mathematics)

Formal authority: `FSOT/Formal/Scalar.lean` (Mathlib `Real`). Float mirror: `FSOT/Scalar.lean`. Decimal oracle: `vendor/fsot_compute.py`.  
Repository: [https://github.com/dappalumbo91/FSOT-2.1-Lean](https://github.com/dappalumbo91/FSOT-2.1-Lean).

### 2.1 Seeds

| Seed | Symbol | Definition (Lean) |
|------|--------|-------------------|
| Pi | $\pi$ | `Real.pi` |
| Eulerâ€™s number | $e$ | $\exp(1)$ |
| Golden ratio | $\varphi$ | $(1+\sqrt{5})/2$ |
| Eulerâ€“Mascheroni | $\gamma$ | fixed numeric constant (edition pin) |
| Catalan | $G$ | fixed numeric constant (edition pin) |

### 2.2 Intrinsic seed-derived constants

All of the following are **definitions** in Lean (not fitted coefficients):

\begin{align}
\alpha &= \frac{\log \pi}{e\,\varphi^{13}}, \\
\psi_{\mathrm{con}} &= 1 - e^{-1}, \\
\eta_{\mathrm{eff}} &= \frac{1}{\pi - 1}, \\
\beta &= \frac{1}{\exp\!\bigl(\pi^{\pi} + (e-1)\bigr)}, \\
\gamma_{\mathrm{fold}} &= -\frac{\log 2}{\varphi}, \\
\omega &= \sin(\pi/e)\cdot\sqrt{2}, \\
\theta_s &= \sin(\psi_{\mathrm{con}}\cdot\eta_{\mathrm{eff}}), \\
\mathrm{poof} &= \exp\!\Bigl(-\frac{\log\pi / e}{\eta_{\mathrm{eff}}\log\varphi}\Bigr), \\
\mathrm{acoustic\_bleed} &= \sin(\pi/e)\cdot\varphi/\sqrt{2}, \\
\sigma_\phi &= -\cos(\theta_s + \pi), \\
\mathrm{coherence} &= (1 - \mathrm{poof}\cdot\sin\theta_s)\,
  \bigl(1 + 0.01\cdot G/(\pi\varphi)\bigr), \\
\mathrm{bleed\_in} &= \mathrm{coherence}\cdot\bigl(1 - \sin\theta_s/\varphi\bigr), \\
\mathrm{acoustic\_inflow} &= \mathrm{acoustic\_bleed}\cdot\bigl(1 + \cos\theta_s/\varphi\bigr), \\
\mathrm{suction} &= \mathrm{poof}\cdot\bigl(-\cos(\theta_s - \pi)\bigr), \\
\mathrm{chaos} &= \gamma_{\mathrm{fold}} / \omega, \\
p_{\mathrm{new}} &= (\gamma/e)\cdot\sqrt{2}, \\
c_f &= \mathrm{coherence}\cdot p_{\mathrm{new}}, \\
k &= \varphi\cdot(\gamma/e)\cdot\sqrt{2}/\log\pi \cdot (99/100).
\end{align}

### 2.3 Parameter structure

A domain evaluation uses a parameter record $p$:

$$
p = (N, P, D_{\mathrm{eff}}, \mathrm{recent\_hits}, \delta\psi, \delta\theta, \rho, \mathrm{scale}, \mathrm{amplitude}, \mathrm{trend\_bias}, \mathrm{observed}).
$$

Default cosmology-style base uses $N=P=1$, $D_{\mathrm{eff}}=25$, $\mathrm{observed}=\mathrm{false}$. Domain folds are **preregistered** via `get_domain_params` (e.g. cosmological: $D_{\mathrm{eff}}=25$, $\delta\psi=1$, unobserved; quantum: $D_{\mathrm{eff}}=6$, $\delta\psi=1$, observed).

### 2.4 Term definitions (Eqs. 1â€“3 expanded)

**(Eq. 1)** Vitality scalar:

$$
\mathrm{raw}\_S(p) := \mathrm{term}_1(p) + \mathrm{term}_2(p) + \mathrm{term}_3(p),\qquad
\mathrm{scaled}\_S(p) := k\cdot\mathrm{raw}\_S(p).
$$

**(Eq. 2a)** Growth and base wave:

\begin{align}
\mathrm{growth}(p) &= \exp\!\Bigl(\alpha\cdot\bigl(1 - \tfrac{\mathrm{recent\_hits}}{N}\bigr)\cdot\gamma/\varphi\Bigr), \\
\mathrm{term}_{1,\mathrm{base}}(p) &=
  \frac{N\cdot P}{\sqrt{D_{\mathrm{eff}}}}
  \cdot\cos\!\Bigl(\frac{\psi_{\mathrm{con}}+\delta\psi}{\eta_{\mathrm{eff}}}\Bigr)
  \cdot\exp\!\bigl(-\alpha\cdot\mathrm{recent\_hits}/N + \rho + \mathrm{bleed\_in}\cdot\delta\psi\bigr)
  \cdot\bigl(1 + \mathrm{growth}(p)\cdot\mathrm{coherence}\bigr).
\end{align}

**(Eq. 2b)** Observer coupling and perceived adjustment:

\begin{align}
\mathrm{quirkMod}(p) &=
\begin{cases}
\exp(c_f\cdot\sigma_\phi)\cdot\cos(\delta\psi + \sigma_\phi) & \text{if }\mathrm{observed}, \\
1 & \text{otherwise},
\end{cases} \\
\mathrm{perceived\_adjust}(D_{\mathrm{eff}}) &= 1 + p_{\mathrm{new}}\cdot\log(D_{\mathrm{eff}}/25), \\
\mathrm{term}_1(p) &= \mathrm{term}_{1,\mathrm{base}}(p)\cdot\mathrm{perceived\_adjust}(D_{\mathrm{eff}})\cdot\mathrm{quirkMod}(p).
\end{align}

**(Eq. 3)** Environment baseline and chaotic bleed:

\begin{align}
\mathrm{term}_2(p) &= \mathrm{scale}\cdot\mathrm{amplitude} + \mathrm{trend\_bias}, \\
\mathrm{term}_3(p) &=
  \beta\cdot\cos(\delta\psi)\cdot\frac{N\cdot P}{\sqrt{D_{\mathrm{eff}}}}
  \cdot\Bigl(1 + \mathrm{chaos}\cdot\frac{D_{\mathrm{eff}}-25}{25}\Bigr) \\
  &\quad\cdot\bigl(1 + \mathrm{poof}\cdot\cos(\theta_s+\pi) + \mathrm{suction}\cdot\sin\theta_s\bigr) \\
  &\quad\cdot\Bigl(1 + \mathrm{acoustic\_bleed}\cdot\frac{\sin^2\delta\theta}{\varphi}
         + \mathrm{acoustic\_inflow}\cdot\frac{\cos^2\delta\theta}{\varphi}\Bigr) \\
  &\quad\cdot\bigl(1 + \mathrm{bleed\_in}\cdot\sigma_\phi\bigr).
\end{align}

**Zero free parameters (operational).** Seeds and intrinsic constants are fixed mathematical definitions. Domain routing slots are preregistered folds. The verification pipeline performs **no per-record least-squares** when a measurement is tested (`scripts/audit_parameter_count.py` â†’ `ZERO_FREE`; `data/honest_claims_manifest.yaml`).

**Sign interpretation (interpretation tier).** Positive $\mathrm{raw}\_S$ tends toward emergence; negative toward dispersal. Lean proves **sign certificates** at canonical domain parametersâ€”proved statements about the formal object, not proofs of ontology.

### 2.5 Wave-1 cosmological observables (formal definitions)

From `FSOT/Formal/Cosmology.lean` (bound to cached cosmology scalar $S_{\mathrm{cosm}}$ from the oracle):

\begin{align}
c_{\mathrm{cosm}} &= 1/(\varphi\cdot 10), \\
H_0^{\mathrm{FSOT}}(S_{\mathrm{cosm}}) &= 100\cdot\Bigl(1 + S_{\mathrm{cosm}}\cdot\frac{\mathrm{acoustic\_bleed}}{\mathrm{acoustic\_inflow}}\Bigr), \\
T_{\mathrm{CMB}}^{\mathrm{FSOT}}(S_{\mathrm{cosm}}) &= \varphi^2 + (\gamma/e)\cdot|S_{\mathrm{cosm}}|, \\
n_s^{\mathrm{FSOT}}(S_{\mathrm{cosm}}) &= 1 + S_{\mathrm{cosm}}\cdot c_{\mathrm{cosm}}\cdot\varphi^{1/\pi}, \\
\Omega_b h^2{}^{\mathrm{FSOT}}(S_{\mathrm{cosm}},S_{\mathrm{quant}}) &= |S_{\mathrm{cosm}}|\cdot(1 - S_{\mathrm{quant}}), \\
\alpha_s(M_Z) &= 1/(e\pi).
\end{align}

Interval certificates in Lean establish **internal consistency** of these formulas at cached inputs (e.g. $|H_0^{\mathrm{FSOT}}(S_{\mathrm{cosm}}^{\mathrm{cached}}) - H_0^{\mathrm{canonical}}| < 0.11$). External agreement with Planck/SH0ES is **empirical** (Â§4), not a theorem of observational cosmology.

### 2.6 Domain routing

- **35 core** NeuroLab domains with manifest-declared folds.  
- **367 extension** panels with Lean priors modules.  
- **402 routed domains** in `data/publication/domain_atlas.csv`.

Cosmology and atomic physics **share seeds**; they differ only in route.

---

## 3. Formal Verification Methodology

### 3.1 Three layers

1. **Formal object** â€” definitions and theorems in Lean (and multi-prover exports).  
2. **Numeric oracle** â€” high-precision Python, SHA-256 pinned.  
3. **Empirical ledger** â€” measured authorities vs seed-derived predictions.

If Lean and Python disagree, the pipeline **fails**.

### 3.2 Oracle gate

Authority module: `vendor/fsot_compute.py`.  
Edition freeze SHA-256:

```
D1D38A185487B452E470AC68ECE2EB45AEB1CA9CE25FC9BF9564C19633FFBE70
```

### 3.3 Lean 4 primary formalization

| Component | Role |
|-----------|------|
| `FSOT/Formal/Scalar.lean` | Real seeds, $\mathrm{term}_i$, $\mathrm{raw}\_S$ |
| `FSOT/Formal/Domains.lean` | Per-domain sign / bound theorems |
| `FSOT/Formal/Cosmology.lean` | Wave-1 observables + interval certificates |
| `FSOT/Formal/*Priors.lean` | Extension panel prior modules |
| Toolchain | Lean 4.31.0 + Mathlib v4.31.0 |

**Representative proved theorems** (`FSOT/Formal/Domains.lean`):

| Theorem | Statement (informal) |
|---------|----------------------|
| `cosmological_raw_S_negative` | $\mathrm{raw}\_S(p_{\mathrm{cosm}}) < 0$ |
| `dark_energy_raw_S_negative` | $\mathrm{raw}\_S(p_{\mathrm{DE}}) < 0$ |
| `cmb_raw_S_negative` | $\mathrm{raw}\_S(p_{\mathrm{cmb}}) < 0$ |
| `medical_raw_S_positive` | $\mathrm{raw}\_S(p_{\mathrm{med}}) > 0$ |
| `chemical_raw_S_positive` | $\mathrm{raw}\_S(p_{\mathrm{chem}}) > 0$ |
| `electron_raw_S_positive` | $\mathrm{raw}\_S(p_{\mathrm{e}}) > 0$ |
| `neural_raw_S_positive` | $\mathrm{raw}\_S(p_{\mathrm{neural}}) > 0$ |
| `quantum_raw_S_positive` | $\mathrm{raw}\_S(p_{\mathrm{q}}) > 0$ |
| `h0_fsot_cached_approx_value` | $|H_0^{\mathrm{FSOT}}(S_{\mathrm{cached}}) - H_0^{\mathrm{can}}| < 0.11$ |

Proof templates include dominance lemmas of the form: if $\mathrm{term}_2=1$ and $|\mathrm{term}_1| > 1+|\mathrm{term}_3|$ with $\mathrm{term}_1<0$, then $\mathrm{raw}\_S<0$ (`raw_S_negative_when_term1_overcomes_defaults`).

### 3.4 Five-prover triangulation

| Framework | Role | Edition status |
|-----------|------|----------------|
| Lean 4 | Primary formal authority | PASS |
| Coq / Rocq | Independent reproof of exported obligations | PASS |
| Isabelle/HOL | Independent reproof | PASS |
| F\* | Boot scalar kernel specification | PASS |
| Rust | Executable obligation replay | PASS |

**Authoritative artifact:** `data/cross_proof_verification_report.json` â†’ `overall_ok: true`, edition freeze **1,863 atomic obligations** (Appendix XI). Full formal spine counts are larger (bundle conjunctions); the **atomic** count is the headline triangulation surface.  
Optional: QEMU bare-metal harness; ESP32 hardware observer (not required for main claims).

### 3.5 Empirical error definitions

For records $(m_i,c_i)$ (measured, computed):

$$
\varepsilon_i = 100 \times \frac{|c_i - m_i|}{\max(|m_i|, \epsilon_{\mathrm{floor}})},\qquad
\tilde{\varepsilon} = \mathrm{median}(\varepsilon_1,\ldots,\varepsilon_n).
$$

**GREEN gate:** $\tilde{\varepsilon}\le 0.5\%$ (and classifier $\ge 99.5\%$ where applicable).  
**Cross-domain headline:** median of per-domain $\tilde{\varepsilon}$â€”not a global re-fit across 536,740 rows.

### 3.6 What formalization does *not* prove

- Not a proof that FSOT is the true ontology of the universe.  
- Sign certificates are at **canonical domain parameters**, not universal quantification over all physical sweeps.  
- Wave-1 intervals certify **internal** formula consistency at caches.  
- F\* covers the boot scalar kernel shell; full spine is Lean+Coq+Isabelle+Rust+Python.

---

## 4. Contested-Sector Results

### 4.1 Motivation

Cross-domain medians can look strong while missing the observables that drive theory change. We foreground **13 contested observables** where open $\Lambda$CDM/SM panels typically sit near a **~15%** tension scale in the repositoryâ€™s contested watch definition.

| Metric | FSOT (edition) | Typical baseline |
|--------|---------------:|-----------------:|
| Pooled median error | **0.030%** | ~15% |
| Observables monitored | 13 | â€” |

*Source: `data/publication/CONTESTED_SECTOR_WATCH.md` (raw 0.029749%). Category: empirical under repository metric.*

### 4.2 Contested observable table

| Observable | FSOT err % | Reference / note |
|------------|----------:|------------------|
| $H_0$ tension SH0ES vs Planck | 0.027 | Riess vs Planck 2018 |
| $H_0$ tension Carnegie vs Planck | 0.227 | Freedman 2019 |
| $S_8$ tension Planck vs DES Y3 | 0.195 | DES Y3 |
| Lithium problem factor | 0.316 | BBN obs vs theory |
| FRB DM excess vs IGM | 0.043 | CHIME high DM |
| $N_{\mathrm{eff}}$ | 0.009 | open panel |
| $\Omega_\Lambda$ | 0.002 | open panel |
| $\sigma_8$ | 0.003 | open panel |
| $\tau_{\mathrm{reion}}$ | 0.006 | open panel |
| D/H ratio | 0.091 | open panel |
| $r_c$ (cusp-core) | 0.341 | Fornax dwarf |
| $m_H$ (hierarchy proxy) | 0.040 | ATLAS/CMS |
| $H_0$ FSOT local anchor | 0.829 | dual-anchor bubble-bleed |
| $H_0$ Planck CMB | 0.193 | Planck 2018 |
| $H_0$ SH0ES local | 0.662 | Riess local ladder |
| $w_a$ | 0.0006 | DESI DR2 |

Living status labels mark **FSOT ledger** resolution; they are not claims of external community adoption.

### 4.3 Bubble-bleed mechanism

**Interpretation tier** with formal hooks: small-scale fluid turbulence on $\mathrm{term}_3$ couples to $\mathrm{perceived\_adjust}$ on $\mathrm{term}_1$ at preregistered cosmology folds (Lean family `bubble_bleed_*`). Dual anchors are not separately least-squares fitted; they emerge from the same seed engine at different routes.

### 4.4 Worked $H_0$ example

| Quantity | Value |
|----------|------:|
| Measured (Planck 2018) | $67.36 \pm 0.54$ km s$^{-1}$ Mpc$^{-1}$ |
| FSOT computed (worked CMB route) | $67.270$ km s$^{-1}$ Mpc$^{-1}$ |
| Relative error | **0.13%** |
| PRED-001 bridge scalar | **70.75** km s$^{-1}$ Mpc$^{-1}$ |
| Local ladder anchor (Riess series) | $73.04$ km s$^{-1}$ Mpc$^{-1}$ |
| PRED-001 discriminant | strictly between Planck and SH0ES |

Preregistration file: `data/preregistered_predictions_manifest.yaml`.  
**Cosmology-community caution:** the observational $H_0$ tension is typically quoted in $\sigma$ units under $\Lambda$CDM; our primary reported metric is **relative percent error** on dual-anchor routes and a **preregistered between-anchors** discriminant. Both should be stated when comparing to reviews of the tension [1,2,3].

### 4.5 Figures (repository / local paper folder)

| Figure | File |
|--------|------|
| Contested FSOT vs $\Lambda$CDM | `figures/contested_fsot_vs_lcdm.png` |
| $H_0$ landscape | `figures/h0_landscape.png` |
| Five-prover obligation map | `figures/obligation_map_five_provers.png` |
| Verification spine | `figures/spine_walkthrough.png` |

(Regenerate from the GitHub repo scripts so figures stay bit-aligned with the freeze tag.)

---

## 5. Selected Core-Domain Empirical Closure

| Domain | Records | Median error % | Tier |
|--------|--------:|---------------:|------|
| Cosmology | 347 | 0.0007 | A_strong |
| Astrophysics | 305 | 0.0006 | A_strong |
| High-energy physics | 151 | 0.0036 | A_strong |
| Atomic physics | 116 | 0.0010 | A_strong |
| Electromagnetism | 271,912 | 0.0 | A_strong |

**Headline context:** 402 domains; 536,740 records; 394/394 green under $\le 0.5\%$ gate; cross-domain pooled median 0.013%. Full atlas: GitHub `data/publication/domain_atlas.csv`.

---

## 6. Falsifiability and Reproduction

### 6.1 One-command bundle

```bash
git clone https://github.com/dappalumbo91/FSOT-2.1-Lean.git
cd FSOT-2.1-Lean
pip install -r requirements.txt
python scripts/run_publication_verification_bundle.py
```

### 6.2 Kill criteria and preregistration

- Predictions: `data/preregistered_predictions_manifest.yaml` (PRED-001â€“041).  
- Domain kill criteria: `data/fsot_domain_navigator.json`.  
- Near-miss ledger: `data/publication/BENCHMARK_NEAR_MISS_LEDGER.md`.  
- Honest claims: `data/honest_claims_manifest.yaml`.

### 6.3 Machine-readable artifacts

| Artifact | Path in repository |
|----------|--------------------|
| Cross-proof report | `data/cross_proof_verification_report.json` |
| Publication claims | `data/publication_claims_manifest.json` |
| Domain atlas | `data/publication/domain_atlas.csv` |
| Contested watch | `data/publication/CONTESTED_SECTOR_WATCH.md` |
| Certificate export | `data/certificate.json` |
| Skeptic kit | `docs/SKEPTIC_REPLICATION_KIT.md` |

### 6.4 How to reject this paper

1. Clone the **tagged release** matching this freeze.  
2. Run the verification bundle.  
3. Show either: formal obligations fail / `overall_ok` is false; or contested-sector recomputation fails preregistered discriminants under the **same** oracle hash; or parameter audit no longer reports zero free per-row fits.

Narrative disagreement without running the ledger is outside the falsification contract.

---

## 7. Discussion

### 7.1 Strengths

- Rare combination: parameter-free seed engine + multi-prover triangulation + contested cosmology with preregistered discriminants.  
- Explicit claim taxonomy (proved / numerical / empirical / interpretation).  
- Executable falsification path via public GitHub.

### 7.2 Limitations

1. Formal certificates do not imply physical necessity.  
2. Single decimal oracle is a specification risk mitigatedâ€”not eliminatedâ€”by multi-prover export.  
3. Contested â€œ~15% baselineâ€ is a sector-scale repository characterization; individual observables have detailed observational uncertainties in the primary literature.  
4. Hardware observer deferred.  
5. 402-domain breadth is deliberately not defended in full in this paper.

### 7.3 Related work

- **Formal methods in science:** Bobbin et al. formalize Langmuir/BET and thermodynamic structures in Lean [4]; HepLean digitalises HEP definitions and theorems in Lean 4 [5]; related work includes physics index notation and dimensional analysis formalizations in Lean. FSOT adds multi-prover obligation export, a hash-locked physical oracle, and a contested empirical ledger.  
- **$\Lambda$CDM and $H_0$ tension:** Planck 2018 parameters [1]; local distance ladder (Riess et al.) [2]; Carnegie program [6]; reviews and early-dark-energy proposals (e.g. Poulin et al.) attack the tension with extended cosmological dynamics [3]. FSOT competes as a **single seed engine with dual-anchor routing**, not as a one-parameter $\Lambda$CDM patch.  
- **Certified numerics / interval methods:** Wave-1 interval certificates sit in this tradition, bound to cosmology caches.  
- **ML + Lean:** automated proving systems differ from FSOTâ€™s engineered domain certificates tied to a physical oracle.

### 7.4 Open work

| Priority | Item |
|----------|------|
| P0 | Git tag + Zenodo archive matching this freeze |
| P1 | LaTeX typesetting; full DOI bibliography |
| P2 | Tighten interval certificates; optional pure formal short paper |
| P3 | Follow-on engineering / molecular papers after core is public |

Living multi-domain thesis: [https://github.com/dappalumbo91/FSOT-2.1-Lean](https://github.com/dappalumbo91/FSOT-2.1-Lean).

---

## 8. Conclusion

We presented a focused claim:

> A **machine-checked, zero free-parameter** scalar engineâ€”formalized primarily in Lean 4 and triangulated across five independent proof frameworksâ€”supplies unified, preregistered readouts on the contested cosmological sector, including dual-anchor $H_0$ via bubble-bleed routing, at **0.030%** pooled median error across 13 monitored observables, with **1,863** atomic obligations closed under `overall_ok: true` in the edition freeze.

The full 402-domain atlas and engineering stacks remain the **living GitHub thesis**. The invitation to the reader is executable: clone the repository, run the bundle, and accept or reject the ledger on its own terms.

---

## Acknowledgments

Grok and Cursor assisted manuscript assembly and repository orchestration. Generative AI tools are not co-authors; the author retains full scientific responsibility for interpretation and for the freeze edition of the claims (consistent with arXiv AI-language-tool policy). All numerical claims are intended to reproduce independently from the public repository.

---

## Data and code availability

- **Primary repository:** [https://github.com/dappalumbo91/FSOT-2.1-Lean](https://github.com/dappalumbo91/FSOT-2.1-Lean)  
- **One-command verification:** `python scripts/run_publication_verification_bundle.py`  
- **License:** see repository `LICENSE` (Apache-2.0 for formal sources as declared there)  
- **This manuscript workspace:** `Desktop/arxiv-papers/01-fsot-formal-contested-cosmology/`  
- **Physical archive (author):** `I:\FSOT-Physical-Archive\02_FSOT-2.1-Lean-Full`

---

## References

1. Planck Collaboration. *Planck 2018 results. VI. Cosmological parameters.* Astron. Astrophys. **641**, A6 (2020). arXiv:1807.06209.  
2. Riess, A. G., et al. *A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km s$^{-1}$ Mpc$^{-1}$ Uncertainty from the Hubble Space Telescope and the SH0ES Team.* Astrophys. J. Lett. **934**, L7 (2022). (and subsequent SH0ES updates as cited in repository anchors.)  
3. Poulin, V., et al. Reviews and models addressing the Hubble tension (e.g. early dark energy); see community reviews of the $H_0$ crisis for $\sigma$-scale status.  
4. Bobbin, M. P., et al. *Formalizing Chemical Physics using the Lean Theorem Prover.* arXiv:2210.12150 [cs.LO] (2022; revised 2023). Digital Discovery **3**, 264â€“280 (2024).  
5. Tooby-Smith, J. *HepLean: Digitalising high energy physics.* arXiv:2405.08863 [hep-ph] (2024).  
6. Freedman, W. L., et al. Carnegieâ€“Chicago Hubble Program / TRGB distance ladder results (2019â€“2024 series).  
7. DES Collaboration. DES Y3 cosmic shear / $S_8$ constraints (2022).  
8. Particle Data Group. *Review of Particle Physics* (2024).  
9. NIST / CODATA. Fundamental physical constants (as cited per benchmark row).  
10. de Moura, L., Ullrich, S., et al. *The Lean 4 Theorem Prover and Programming Language.* (Lean 4 + Mathlib documentation.)  
11. The Coq Development Team. *The Coq Proof Assistant* / Rocq.  
12. Nipkow, T., Paulson, L. C., Wenzel, M. *Isabelle/HOL â€” A Proof Assistant for Higher-Order Logic.*  
13. Swamy, N., et al. *Dependent Types and Multi-Monadic Effects in F\*.*  
14. Palumbo, D. A. *Fluid Spacetime Omni-Theory (FSOT) 2.1 Lean â€” Living thesis.* GitHub (2026). https://github.com/dappalumbo91/FSOT-2.1-Lean  

*Domain-specific bibliography export from the repo:* `python scripts/export_domain_citations.py`.

---

## Appendix A â€” Supplementary pointers

| Volume | Location in repository |
|--------|------------------------|
| Appendix XI â€” full verification record | `docs/THESIS_APPENDIX_XI.md` |
| Appendix XII â€” domain coverage | `docs/THESIS_APPENDIX_XII.md` |
| Seed-to-formula derivations | `docs/THESIS_APPENDIX_DERIVATIONS.md` |
| Skeptic replication kit | `docs/SKEPTIC_REPLICATION_KIT.md` |
| Near-miss ledger | `data/publication/BENCHMARK_NEAR_MISS_LEDGER.md` |
| Contested sector watch | `data/publication/CONTESTED_SECTOR_WATCH.md` |
| REPRODUCE.md | repository root |
| Completeness audit (this paper project) | `ARXIV_COMPLETENESS_AUDIT.md` (local) |

*Pre-submission admin checklist lives in PRE_SUBMISSION_CHECKLIST.md (not part of the manuscript).*
