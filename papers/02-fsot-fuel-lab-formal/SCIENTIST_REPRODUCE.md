# Independent reproduction — Paper 02 Fuel Lab

**Repo:** https://github.com/dappalumbo91/FSOT-2.1-Lean  
**Tag:** `v2.6-arxiv-paper01` (commit `8a44947`)  
**Freeze:** `FREEZE.yaml`

## Portable path (validated on clean clone)

```bash
git clone https://github.com/dappalumbo91/FSOT-2.1-Lean.git
cd FSOT-2.1-Lean
git checkout v2.6-arxiv-paper01
pip install -r requirements.txt
python scripts/build_verified_desktop_cross_proof_closure.py
python scripts/build_verified_desktop_fuel_figure.py
python scripts/audit_parameter_count.py
python scripts/query_fsot_domain_navigator.py --intent fuel_lab_engine
```

**Expect:**

| Check | Value |
|-------|------:|
| Fuel records | 366 |
| Pooled median | 0.039349% |
| Desktop verdict | VERIFIED_DESKTOP_CROSS_PROOF_READY |
| Parameter audit | ZERO_FREE |
| Figure | `data/figures/verified_desktop_fuels.png` |

## Automated checker

```bash
python verify_paper_claims.py --fsot-root /path/to/FSOT-2.1-Lean --strict-hash --require-cross-proof
```

Author clean-clone result: **PASS** (`logs/verify_paper_claims_clean.log`).

## Optional broader bundle

```bash
python scripts/run_publication_verification_bundle.py
```

## Avoid on bare clones

```bash
python scripts/reproduce_domain_panel.py --panel Fuel_Lab_Live_Panel --deep
```

May require external desktop/archive caches (`FileNotFoundError: arXiv primitives root`). Portable claims do **not** need `--deep`.

## Falsify

1. Median far from 0.039349% on freeze tag benchmarks.  
2. Closure verdict fails / oracle replay Δ ≠ 0 under pinned oracle.  
3. ZERO_FREE lost.  
