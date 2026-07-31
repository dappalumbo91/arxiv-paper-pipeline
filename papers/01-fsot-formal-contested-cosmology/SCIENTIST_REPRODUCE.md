# Independent reproduction guide (for scientists)

This document is the **paper’s reproducibility contract**.  
Manuscript: *Formally Verified Parameter-Free Scalar Engine Resolving Cosmological Tensions*  
Code: **https://github.com/dappalumbo91/FSOT-2.1-Lean**  
Freeze: see `FREEZE.yaml` (commit pin, oracle SHA-256, expected numbers).

You do **not** need the author’s desktop or physical archive. A public clone is enough for the publication bundle. Full five-prover triangulation needs optional local proof assistants.

---

## What “reproduced” means

| Layer | You verify | Pass criterion |
|-------|------------|----------------|
| **A. Empirical / publication** | One-command bundle | Completes without hard failure; claims JSON matches freeze within tolerances |
| **B. Parameter honesty** | `audit_parameter_count.py` | Reports `ZERO_FREE` (no per-row least-squares) |
| **C. Contested sector** | Contested closure / watch | Pooled median ≈ **0.030%** (freeze 0.029749%); 13 observables |
| **D. Formal Lean** | `lake build` / verification runner | `lean_build_ok: true`, `sorry_count_formal: 0` |
| **E. Five-prover** | Cross-proof (optional) | `overall_ok: true`, atomic obligations ≥ **1863** |

Failing any of A–C after a clean clone of the **pinned commit** is a successful falsification of the paper’s executable claims.

---

## Hardware / time budget

| Path | Time (typical) | Disk | Needs |
|------|----------------:|------|-------|
| **Tier 0 — 15 min skeptic** | ~15 min | ~0.5–2 GB clone | Python 3.11+, pip |
| **Tier 1 — publication bundle** | ~10–30 min | same | Python deps |
| **Tier 2 — Lean formal** | +30–90 min first build | +~3 GB Mathlib | elan + Lean 4.31.0 |
| **Tier 3 — five-prover** | +10–40 min | toolchains | Coq/Rocq, Isabelle, F\*, Rust (as available) |

ESP32 hardware observer is **optional** and not required for paper claims.

---

## Pin the exact code (mandatory)

```bash
git clone https://github.com/dappalumbo91/FSOT-2.1-Lean.git
cd FSOT-2.1-Lean
# Prefer the paper freeze tag when published:
# git checkout v2.6-arxiv-paper01
# Or pin the freeze commit from FREEZE.yaml:
git checkout 81bc89364d206aca6da4c65f3faa875ad168cc8e
```

Confirm oracle hash (must match freeze):

```bash
# Windows PowerShell
Get-FileHash vendor\fsot_compute.py -Algorithm SHA256
# Linux/macOS
shasum -a 256 vendor/fsot_compute.py
```

Expected:

```
D1D38A185487B452E470AC68ECE2EB45AEB1CA9CE25FC9BF9564C19633FFBE70
```

---

## Tier 0 — 15-minute skeptic path

```bash
pip install -r requirements.txt
# matplotlib is included in requirements.txt (fix: matplotlib>=3.8 for publication figures).
# On an older checkout before that commit, also run: pip install matplotlib
python scripts/run_publication_verification_bundle.py
python scripts/audit_parameter_count.py
python scripts/query_fsot_domain_navigator.py --intent cosmology_cmb
python scripts/query_fsot_domain_navigator.py --query hubble
```

**Expect:**

1. Console ends with `=== Publication verification bundle complete ===` (exit 0)
2. Parameter audit: **ZERO_FREE**
3. Cosmology / Hubble panels appear under `--intent cosmology_cmb` or `--query hubble`
   - Note: `--intent hubble_tension` is **not** a registered intent (common doc typo)

Also open (after run):

- `data/publication_claims_manifest.json`
- `data/contested_observables_closure.json`
- `data/figures/h0_landscape.png`

**Author clean-clone result (2026-07-31):** PASS in ~25 s after clone; see `CLEAN_CLONE_REPRO_REPORT.md`.

Repository mirror: `docs/SKEPTIC_REPLICATION_KIT.md` (if it still lists `hubble_tension`, use `cosmology_cmb` instead).

---

## Tier 1 — Publication verification bundle (paper default)

```bash
pip install -r requirements.txt
pip install matplotlib
python scripts/run_publication_verification_bundle.py
```

This **does not** re-ingest live APIs; it uses on-disk benchmarks shipped in the repo (portable scientific claim).

**Clean-clone size:** ~0.5 GB working tree (GitHub public repo). Not the multi-GB physical archive.

### Required output artifacts

| Artifact | Role |
|----------|------|
| `data/publication_claims_manifest.json` | Peer-review claim ledger |
| `data/contested_observables_closure.json` | Contested sector numbers |
| `data/benchmark_margin_audit.json` | Green-gate audit |
| `data/figures/contested_fsot_vs_lcdm.png` | Figure |
| `data/figures/h0_landscape.png` | Figure |
| `data/figures/obligation_map_five_provers.png` | Figure |
| `data/figures/spine_walkthrough.png` | Figure |

### Expected numbers (edition freeze)

| Quantity | Expected |
|----------|----------|
| Contested pooled median | **0.029749%** (paper rounds to **0.030%**) |
| Contested observables | **13** |
| Cross-domain pooled median | **≈0.013%** |
| Benchmark green (claims) | **394/394** under ≤0.5% gate |
| Formal (claims manifest) | `overall_ok: true`, atomic obligations **1863** |

### Automated check from this paper folder

From the paper project directory (after clone):

```bash
# Set path to your clone
set FSOT_ROOT=C:\path\to\FSOT-2.1-Lean
python verify_paper_claims.py
```

```bash
export FSOT_ROOT=/path/to/FSOT-2.1-Lean
python verify_paper_claims.py
```

Exit code `0` = freeze checks passed; nonzero = mismatch (print details).

---

## Tier 2 — Lean formalization

Prerequisites: [elan](https://github.com/leanprover/elan), toolchain from `lean-toolchain`:

```
leanprover/lean4:v4.31.0
```

```bash
lake exe cache get
lake build
# or repository runner:
python scripts/fsot_verification_runner.py --portable
python scripts/export_certificate.py --lean-ok
```

**Expect** in `data/certificate.json`:

- `lean_build_ok: true`
- `sorry_count_formal: 0`
- `lean_toolchain: leanprover/lean4:v4.31.0`
- `authority.sha256` matches freeze oracle

Key formal modules:

- `FSOT/Formal/Scalar.lean` — $\mathrm{raw}\_S$ definitions  
- `FSOT/Formal/Domains.lean` — sign certificates  
- `FSOT/Formal/Cosmology.lean` — Wave-1 $H_0$ etc.

---

## Tier 3 — Five-prover cross-proof (optional but recommended)

```bash
python scripts/run_publication_verification_bundle.py --full-cross-proof
# or
python scripts/run_cross_proof_verification.py
```

**Expect** in `data/cross_proof_verification_report.json`:

- `overall_ok: true`
- `github_ready: true`
- atomic provable count ≥ **1863** (archive freeze report: **1873**)

Frameworks (as installed on the machine):

| Framework | Role |
|-----------|------|
| Lean 4 | Primary authority |
| Coq / Rocq | Independent export replay |
| Isabelle/HOL | Independent export replay |
| F\* | Boot scalar kernel |
| Rust | Executable obligation replay |

If a toolchain is missing, the report documents skip/fail status—do not treat a partial local install as a paper falsification unless the **portable GitHub-ready** path fails.

---

## Contested cosmology spot-checks

```bash
python scripts/build_contested_observables_closure.py
python scripts/build_contested_sector_watch.py
python scripts/query_fsot_domain_navigator.py --intent cosmology_cmb
python scripts/query_fsot_domain_navigator.py --query hubble
```

**PRED-001** (preregistered): FSOT $H_0$ bridge scalar strictly between Planck CMB and SH0ES local anchors — see `data/preregistered_predictions_manifest.yaml`.

Worked CMB example (paper): Planck $67.36\pm0.54$ vs FSOT $67.270$ km s$^{-1}$ Mpc$^{-1}$ (~0.13% relative error).

---

## What would falsify the paper

1. Clean checkout of freeze commit fails publication bundle with hard error.  
2. `publication_claims_manifest.json` contested pooled median far from 0.030% after regeneration.  
3. `audit_parameter_count.py` no longer reports zero free per-observable fits.  
4. `certificate.json` has `sorry_count_formal > 0` or Lean build fails on freeze toolchain.  
5. `cross_proof_verification_report.json` has `overall_ok: false` when toolchains matching the repo docs are installed.  
6. Oracle `vendor/fsot_compute.py` SHA-256 differs from freeze without a documented authority repin.

---

## What does *not* falsify the paper

- Missing ESP32 hardware.  
- Missing one of five optional provers if the report marks that path skipped and GitHub-ready portable path still passes.  
- Disagreement with FSOT *ontology* while the executable ledger still passes.  
- Wanting a full $\sigma$-level Bayesian re-analysis of Planck likelihoods (out of scope; separate cosmology paper).

---

## Offline / archive note

Author’s physical archive (`FSOT-Physical-Archive`) includes larger caches and portable toolchains. **It is not required.** GitHub portable vendor snapshots are the public contract. If you use an archive copy, still pin the same commit and oracle hash.

---

## Cite the software

```bibtex
@software{fsot21lean2026,
  author = {Palumbo, Damian Arthur},
  title  = {FSOT-2.1-Lean: Fluid Spacetime Omni-Theory formalization and verification},
  year   = {2026},
  url    = {https://github.com/dappalumbo91/FSOT-2.1-Lean},
  note   = {Commit 81bc893; edition freeze arxiv-paper01-2026-07-16}
}
```

---

## Support files in this paper directory

| File | Purpose |
|------|---------|
| `FREEZE.yaml` | Immutable pins |
| `verify_paper_claims.py` | Automated freeze checker |
| `EXPECTED_ARTIFACTS.md` | Artifact checklist |
| `paper.tex` / `references.bib` | arXiv LaTeX sources |
| `abstract.txt` / `comments.txt` | arXiv metadata fields |
| `figures/` | Manuscript figures (also regenerated in repo) |
