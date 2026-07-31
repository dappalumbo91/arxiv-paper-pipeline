# Submit this paper to arXiv

## 1. Before you click submit

| Step | Command / action | Done? |
|------|------------------|-------|
| Freeze tag on GitHub | `git tag -a v2.6-arxiv-paper01 81bc893 -m "arXiv paper 01 freeze"` then `git push origin v2.6-arxiv-paper01` | ☐ |
| Clean clone verify | See `SCIENTIST_REPRODUCE.md` Tier 0–1 | ☐ |
| Claim checker | `python verify_paper_claims.py --fsot-root <clone> --strict-hash` | ☐ |
| Build PDF | `pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper` | ☐ |
| Abstract length | `abstract.txt` ≤ 1920 chars | ☐ |
| Figures in PDF | H₀, contested, obligation map | ☐ |

## 2. arXiv metadata (copy-paste)

**Title** (no all-caps):

```
Formally Verified Parameter-Free Scalar Engine Resolving Cosmological Tensions: Lean 4 + Multi-Prover Certification of Fluid Spacetime Omni-Theory
```

**Authors:**

```
Damian Arthur Palumbo
```

**Abstract:** paste from `abstract.txt` (ASCII).

**Comments:** paste from `comments.txt`.

**Primary category:** `cs.LO`  
**Cross-lists:** `astro-ph.CO`, `math.LO` (optional but recommended)

**License:** arXiv non-exclusive distribution license (or match repo).

## 3. File package for upload

arXiv prefers a **flat** source directory (or a simple zip). Minimum:

```
paper.tex
references.bib
paper.bbl          # after bibtex; arXiv often wants .bbl not only .bib
figures/
  contested_fsot_vs_lcdm.png
  h0_landscape.png
  obligation_map_five_provers.png
  spine_walkthrough.png
```

Optional ancillary (`anc/`):

```
anc/FREEZE.yaml
anc/SCIENTIST_REPRODUCE.md
anc/verify_paper_claims.py
anc/EXPECTED_ARTIFACTS.md
anc/abstract.txt
anc/comments.txt
```

Do **not** upload the entire FSOT repo as the paper source—link it.

## 4. Build PDF locally (Windows)

```powershell
cd C:\Users\damia\Desktop\arxiv-papers\01-fsot-formal-contested-cosmology
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

If `bibtex` fails, ensure `references.bib` is next to `paper.tex`.

## 5. Reproducibility statement (for reviewers)

Independent scientists:

1. Clone freeze commit `81bc893` (or tag `v2.6-arxiv-paper01`).
2. Run `python scripts/run_publication_verification_bundle.py`.
3. Run `verify_paper_claims.py` from this package against that clone.
4. Optional: Lean build + `--full-cross-proof`.

Full contract: `SCIENTIST_REPRODUCE.md`.

## 6. Endorsement

First-time submitters in `cs.LO` may need endorsement.  
Use arXiv endorsement help if the submit button is blocked.
