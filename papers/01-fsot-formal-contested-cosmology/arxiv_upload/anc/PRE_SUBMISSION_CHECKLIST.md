# Pre-submission checklist (NOT part of the paper PDF)

Keep this file in the paper package only. Do **not** paste it into `paper.tex` or upload it as manuscript body text. arXiv readers should see science, not your internal admin list.

---

## Status legend

- [x] done  
- [ ] still yours / optional  

---

## A. Repository freeze (code under test)

| # | Item | Status | Evidence |
|---|------|--------|----------|
| A1 | Tag `v2.6-arxiv-paper01` on GitHub | [x] | Points to `8a44947` (includes `matplotlib>=3.8`) |
| A2 | `requirements.txt` includes matplotlib | [x] | Pushed on main + tag |
| A3 | Skeptic intent `cosmology_cmb` (not broken `hubble_tension`) | [x] | README + SKEPTIC kit on tag |
| A4 | Oracle SHA-256 documented | [x] | `FREEZE.yaml` / paper software box |

---

## B. Independent reproduction

| # | Item | Status | Evidence |
|---|------|--------|----------|
| B1 | Clean GitHub clone (~0.5 GB) | [x] | `CLEAN_CLONE_REPRO_REPORT.md` |
| B2 | `run_publication_verification_bundle.py` exit 0 | [x] | ~25 s; contested 0.030% |
| B3 | `verify_paper_claims.py --strict-hash` PASS | [x] | Archive + clean clone |
| B4 | `audit_parameter_count.py` → ZERO_FREE | [x] | Clean clone |
| B5 | Re-run with `--require-cross-proof` and **archive log** | [ ] | Run before submit if you want belt-and-suspenders; shipped report already has `overall_ok` |
| B6 | Optional: full `lake build` on clean machine | [ ] | Tier 2; not required for empirical Tier 1 claim |

**Command for B5 (optional archive log):**

```powershell
cd C:\Users\damia\Desktop\arxiv-papers\_clean_clone\FSOT-2.1-Lean
git checkout v2.6-arxiv-paper01
python ..\..\01-fsot-formal-contested-cosmology\verify_paper_claims.py --fsot-root . --strict-hash --require-cross-proof *> ..\..\01-fsot-formal-contested-cosmology\logs\verify_paper_claims_clean.log
```

---

## C. Manuscript package

| # | Item | Status | Notes |
|---|------|--------|-------|
| C1 | Title finalized (no “Resolving”) | [x] | `title.txt` / `paper.tex` |
| C2 | Full scalar math + Wave-1 equations | [x] | §2 |
| C3 | Formal methodology + theorem names | [x] | §3 |
| C4 | Contested tables + PRED-001/002/005 | [x] | §4 |
| C5 | Falsifiability + clone commands | [x] | §6 |
| C6 | Discussion with claim-stack reading guide | [x] | §7 |
| C7 | Figures embedded (H₀, contested, obligation map) | [x] | `figures/` |
| C8 | **No admin checklist in PDF appendix** | [x] | Removed; this file only |
| C9 | Build `paper.pdf` from `paper.tex` | [x] | Rebuild after last edits |
| C10 | `arxiv_source_v1.zip` refreshed | [ ] | Rebuild zip after final PDF |
| C11 | Abstract ≤1920 chars | [x] | `abstract.txt` ~1552 |
| C12 | `comments.txt` ready | [x] | For arXiv Comments field only |

---

## D. arXiv form (you in Chrome)

| # | Item | Status |
|---|------|--------|
| D1 | Upload `arxiv_source_v1.zip` as TeX | [ ] |
| D2 | Preview PDF on arXiv looks good | [ ] |
| D3 | Title from `title.txt` | [ ] |
| D4 | Authors: Damian Arthur Palumbo | [ ] |
| D5 | Abstract from `abstract.txt` | [ ] |
| D6 | Comments from `comments.txt` | [ ] |
| D7 | Primary **cs.LO** | [ ] |
| D8 | Cross-list **astro-ph.CO** (and optional **math.LO**) | [ ] |
| D9 | License accepted | [ ] |
| D10 | Submit | [ ] |

Walkthrough: `ARXIV_UPLOAD_WALKTHROUGH.md`

---

## E. After public (post-submit)

| # | Item |
|---|------|
| E1 | Put arXiv ID on GitHub README |
| E2 | Optional GitHub Release notes pointing at abstract |
| E3 | Do not change claim numbers without new freeze |

---

## What is intentionally NOT on this checklist

- Expanding the PDF into a 402-domain monograph  
- Browser automation of arXiv login  
- ESP32 hardware  
- Claiming “Hubble tension solved at 5σ”  
