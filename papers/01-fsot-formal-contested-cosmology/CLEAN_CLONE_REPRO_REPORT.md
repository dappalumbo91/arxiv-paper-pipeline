# Clean-clone reproduction report

**Date:** 2026-07-31  
**Machine:** author Windows workstation, **fresh GitHub clone** (not `I:\` archive)  
**Clone path:** `Desktop/arxiv-papers/_clean_clone/FSOT-2.1-Lean`  
**Purpose:** prove a scientist can reproduce paper claims from GitHub alone.

---

## Setup

| Step | Result |
|------|--------|
| `git clone https://github.com/dappalumbo91/FSOT-2.1-Lean.git` | **OK** (~38 s, ~58 MB pack, **483 MB** working tree) |
| HEAD | `81bc893` — **matches freeze** |
| `pip install -r requirements.txt` | **OK** (numpy, mpmath, sympy, pytest, PyYAML, pypdf) |
| Oracle SHA-256 | **D1D38A…FFBE70** — **matches freeze** |

**Size note:** The public repo is **not** multi-GB for a normal clone. ~0.5 GB working tree is fine for typical academic machines. The multi-GB costs are **optional** Lean Mathlib (Tier 2) and the author’s offline archive (not required).

---

## Tier 1 — publication bundle

```text
python scripts/run_publication_verification_bundle.py
```

| Result | Value |
|--------|--------|
| Exit code | **0** |
| Wall time | **~25 s** |
| Contested pooled median | **0.029749%** |
| Claims green | **394/394** |
| Margin audit (this run) | **407/407** GREEN (includes all active benchmark files; claims ledger still quotes 394/394 public set) |
| H₀ Planck walkthrough error | **0.133%** |
| Figures regenerated | yes (`h0_landscape`, `contested_fsot_vs_lcdm`, `spine_walkthrough`, …) |
| Advisory only | `build_tier_scalar_precision_closure.py` exit 1 (documented non-blocking) |

Console closed with:

```text
=== Publication verification bundle complete ===
```

---

## Automated freeze checker

```text
python verify_paper_claims.py --fsot-root <clean_clone> --strict-hash
```

**RESULT: PASS** — all hard checks, including:

- oracle hash  
- contested 0.030% / 13 observables  
- atomic obligations **1863**  
- `overall_ok: true`  
- `sorry_count_formal: 0`  
- key figures present  

On clean GitHub tree, cross-proof report reports **atomic_provable_count: 1863** (archive had 1873; paper freeze uses ≥1863 acceptance).

---

## Parameter honesty

```text
python scripts/audit_parameter_count.py
```

**Verdict: ZERO_FREE** — seed-derived constants and preregistered domain routes.

---

## Contested / cosmology navigation (corrected)

| Command | Result |
|---------|--------|
| `--intent hubble_tension` | **FAIL** — intent does not exist (docs were wrong) |
| `--intent cosmology_cmb` | **OK** → Cosmology, keywords include hubble |
| `--query hubble` | **OK** → Hubble panels + cosmology_cmb |
| `--core Cosmology` | **OK** — 347 records, median ~0.0007% |

**Action taken:** paper package docs updated to use working commands (see below).

---

## Gaps found (and fixes)

### 1. Matplotlib not in `requirements.txt` (medium)

Figure scripts import `matplotlib.pyplot`.  
On this machine it worked because the environment already had matplotlib 3.10.9.

**Scientist risk:** fresh venv with *only* `requirements.txt` may fail figure steps.

**Mitigation in paper package:**

```bash
pip install -r requirements.txt
pip install matplotlib   # needed to regenerate figures
```

Recommended upstream fix (on GitHub, separate PR): add `matplotlib>=3.8` to `requirements.txt`.

### 2. Wrong navigator intent in skeptic docs (low, fixed here)

Replace `hubble_tension` with `cosmology_cmb` or `--query hubble`.

### 3. Bundle dirties the working tree (expected)

Regeneration updates timestamps/JSON; **not a failure**.  
Scientists should compare **values**, not expect a clean `git status`.

### 4. Green count 394 vs 407 (documentation, not failure)

- Claims manifest: **394/394** (publication headline set)  
- Full margin audit this run: **407/407** active files  

Paper correctly cites **394/394** from the claims ledger. Optional footnote: margin audit may list additional domain files that also pass.

### 5. Tier 2 Lean / Tier 3 five-prover not re-run on clean clone (optional)

Shipped `certificate.json` and `cross_proof_verification_report.json` already satisfy freeze checks.  
Full `lake build` / multi-prover re-execution needs local toolchains (~3 GB Mathlib) — still optional for empirical Tier 1 claims.

---

## Verdict

| Paper claim layer | Clean-clone status |
|-------------------|--------------------|
| Clone + oracle pin | **PASS** |
| One-command publication bundle | **PASS** (~25 s) |
| Contested sector numbers | **PASS** |
| Parameter ZERO_FREE | **PASS** |
| Freeze checker | **PASS** |
| Docs accuracy (hubble intent) | **Fixed in package** |
| Figure deps (matplotlib) | **Documented; recommend upstream pin** |

**Bottom line:** A scientist with Python 3.11+, pip, git, and matplotlib can reproduce the **headline empirical and claims-ledger results** from GitHub in under a minute after clone. The repo is ~0.5 GB, not prohibitive.

---

## Commands that worked (copy for paper)

```bash
git clone https://github.com/dappalumbo91/FSOT-2.1-Lean.git
cd FSOT-2.1-Lean
git checkout 81bc893   # optional; currently HEAD
pip install -r requirements.txt
pip install matplotlib
python scripts/run_publication_verification_bundle.py
python scripts/audit_parameter_count.py
python scripts/query_fsot_domain_navigator.py --intent cosmology_cmb
python scripts/query_fsot_domain_navigator.py --query hubble
# from paper package:
python path/to/verify_paper_claims.py --fsot-root . --strict-hash
```
