# Ready to submit — status board

**Last updated:** 2026-07-31  
**Paper package:** `Desktop/arxiv-papers/01-fsot-formal-contested-cosmology/`

**Admin checklist (not in the PDF):** [`PRE_SUBMISSION_CHECKLIST.md`](PRE_SUBMISSION_CHECKLIST.md)  
**Depth/package review:** [`PACKAGE_AND_DEPTH_REVIEW.md`](PACKAGE_AND_DEPTH_REVIEW.md)

---

## Completed

| Item | Status |
|------|--------|
| Full math + formal + contested sections | Done (`paper.tex` / `paper.pdf`) |
| Claim taxonomy (proved / empirical / interpretation) | Done |
| GitHub software box + Comments metadata | Done |
| Bibliography with DOIs | Done (`references.bib`) |
| `matplotlib>=3.8` in repo `requirements.txt` | **Pushed** (`8a44947`) |
| Skeptic/README hubble intent fix | **Pushed** |
| Clean GitHub clone reproduction | **PASS** (~25 s, ~0.5 GB) |
| Freeze tag `v2.6-arxiv-paper01` | **Pushed** → `8a44947` |
| Claim checker `verify_paper_claims.py` | PASS on archive + clean clone |
| arXiv source zip | `arxiv_source_v1.zip` |
| PDF build | `paper.pdf` (11 pages) |

---

## How a scientist reproduces (final)

```bash
git clone https://github.com/dappalumbo91/FSOT-2.1-Lean.git
cd FSOT-2.1-Lean
git checkout v2.6-arxiv-paper01
pip install -r requirements.txt
python scripts/run_publication_verification_bundle.py
python scripts/audit_parameter_count.py
python scripts/query_fsot_domain_navigator.py --intent cosmology_cmb
```

Expect: bundle complete, contested ~0.030%, **ZERO_FREE**.

---

## Your arXiv upload steps

1. Go to https://arxiv.org/submit  
2. **Primary category:** `cs.LO`  
3. **Cross-list (recommended):** `astro-ph.CO`, optionally `math.LO`  
4. **Title / authors / abstract:** from `abstract.txt` (or paper PDF)  
5. **Comments:** paste `comments.txt`  
6. **Upload:** either  
   - `arxiv_source_v1.zip`, or  
   - files under `arxiv_upload/` (`paper.tex`, `paper.bbl`, `references.bib`, `figures/`)  
7. Preview PDF on arXiv; confirm figures and citations render  
8. Submit  

### Endorsement

If arXiv asks for endorsement in `cs.LO` (common for first-time submitters in a category), request it early. Your public Lean repo + clean reproduction helps.

### License

Choose arXiv’s non-exclusive distribution license (or the option that matches your repo Apache-2.0 intent). Do **not** add a conflicting copyright statement in the PDF.

---

## Optional polish (not blocking)

| Item | Why |
|------|-----|
| Soften title for `astro-ph.CO` | Reduces moderator/reviewer heat on “Resolving” |
| ORCID | Nice on author line |
| Upstream: ensure archive desktop trees pull latest main | Local consistency only |
| DESI primary citation for $w_a$ | Bibliography depth |

---

## Key URLs

- Code: https://github.com/dappalumbo91/FSOT-2.1-Lean  
- Tag: https://github.com/dappalumbo91/FSOT-2.1-Lean/releases/tag/v2.6-arxiv-paper01  
  (or tree at tag if no GitHub “Release” object—tag is on remote)  
- Paper PDF: `paper.pdf` in this folder  
- Upload zip: `arxiv_source_v1.zip`  

---

## Honest readiness

**You can submit.** Empirical reproducibility is demonstrated on a clean clone; the freeze tag is public; deps for figures are fixed; the PDF builds.

What remains is **you** on arXiv.org: account, endorsement if needed, and the upload click.
