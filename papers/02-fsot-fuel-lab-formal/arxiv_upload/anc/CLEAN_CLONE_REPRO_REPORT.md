# Clean-clone reproduction report — Paper 02

**Date:** 2026-07-31  
**Clone:** `Desktop/arxiv-papers/_clean_clone/FSOT-2.1-Lean`  
**Pin:** `v2.6-arxiv-paper01` / `8a44947`

## Commands run

| Command | Result |
|---------|--------|
| `build_verified_desktop_cross_proof_closure.py` | **OK** — Fuel Lab oracle OK, 5 obligations; verdict READY |
| `build_verified_desktop_fuel_figure.py` | **OK** — 366 records, pooled 0.039349% |
| `audit_parameter_count.py` | **ZERO_FREE** |
| `query_fsot_domain_navigator.py --intent fuel_lab_engine` | **OK** |
| `verify_paper_claims.py --strict-hash --require-cross-proof` | **PASS** |
| `reproduce_domain_panel.py --panel Fuel_Lab_Live_Panel --deep` | **FAIL** (missing external arXiv primitives cache) — documented as non-portable |

## Freeze metrics recovered

- Fuel records: **366**  
- Pooled median: **0.039349%**  
- Oracle hash: **D1D38A…**  
- Atomic obligations: **≥1863**, `overall_ok: true`  

## Verdict

Portable Paper 02 claims are **reproducible** from the public tag without the physical archive.  
Deep re-ingest is optional and environment-dependent.
