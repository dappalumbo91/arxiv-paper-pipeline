# Expected artifacts after independent reproduction

## After `python scripts/run_publication_verification_bundle.py`

Must exist under the FSOT-2.1-Lean clone:

```
data/publication_claims_manifest.json
data/contested_observables_closure.json
data/benchmark_margin_audit.json
data/publication_spine_walkthrough.json
data/fsot_domain_navigator.json
data/figures/contested_fsot_vs_lcdm.png
data/figures/h0_landscape.png
data/figures/spine_walkthrough.png
data/figures/empirical_headline_summary.png
```

Often also present / regenerable:

```
data/publication/CONTESTED_SECTOR_WATCH.md
data/publication/domain_atlas.csv
data/figures/obligation_map_five_provers.png
data/domain_citations/verified_desktop.bib
```

## After Lean certificate export

```
data/certificate.json
```

Fields: `lean_build_ok`, `sorry_count_formal`, `authority.sha256`, `proved_claims`.

## After full cross-proof

```
data/cross_proof_verification_report.json
```

Fields: `overall_ok`, `github_ready`, `full_formal_spine.atomic_provable_count`.

## Paper-local freeze checker

```
python verify_paper_claims.py --fsot-root /path/to/FSOT-2.1-Lean
```
