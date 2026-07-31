# Paper 01 — Formally Verified Parameter-Free Scalar Engine

**Status:** **Ready to submit** — see `READY_TO_SUBMIT.md`  
**PDF:** `paper.pdf` (11 pages)  
**GitHub:** https://github.com/dappalumbo91/FSOT-2.1-Lean  
**Freeze tag (public):** `v2.6-arxiv-paper01` → commit `8a44947` (matplotlib in requirements)  
**Upload package:** `arxiv_source_v1.zip`

---

## For scientists (reproduce the paper)

1. Read **`SCIENTIST_REPRODUCE.md`** (tiered 15 min → full five-prover).  
2. Clone freeze commit and run the publication bundle.  
3. Run the automated checker:

```powershell
$env:FSOT_ROOT = "C:\path\to\FSOT-2.1-Lean"
python verify_paper_claims.py --strict-hash
```

**Verified twice:**

| Environment | Result |
|-------------|--------|
| Author physical archive (`I:\…`) | PASS |
| **Clean GitHub clone** (`_clean_clone/FSOT-2.1-Lean`, commit `81bc893`) | **PASS** (~25 s bundle; see `CLEAN_CLONE_REPRO_REPORT.md`) |

Oracle hash, 394/394 green, contested 0.030%, `overall_ok`, 1863 obligations, `sorry=0`, `ZERO_FREE`.

---

## Package contents

| File | Purpose |
|------|---------|
| `paper.pdf` | Compiled manuscript |
| `paper.tex` | LaTeX source (arXiv upload) |
| `paper.md` | Markdown working draft |
| `references.bib` | Bibliography with DOIs |
| `abstract.txt` | arXiv abstract field (≤1920 chars) |
| `comments.txt` | arXiv comments field |
| `FREEZE.yaml` | Immutable pins (commit, hashes, numbers) |
| `verify_paper_claims.py` | Independent freeze checker |
| `SCIENTIST_REPRODUCE.md` | Full reproducibility contract |
| `EXPECTED_ARTIFACTS.md` | Post-run file checklist |
| `SUBMIT_ARXIV.md` | Submission checklist |
| `create_github_freeze_tag.ps1` | Tag helper (use `-Push` carefully) |
| `figures/` | Manuscript figures |
| `ARXIV_COMPLETENESS_AUDIT.md` | Standards audit |

---

## Build PDF

```powershell
cd C:\Users\damia\Desktop\arxiv-papers\01-fsot-formal-contested-cosmology
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

---

## Author remaining steps

1. **Push freeze tag** (when ready):  
   `.\create_github_freeze_tag.ps1 -Push`  
   (pushes `v2.6-arxiv-paper01` → commit `81bc893` on GitHub)
2. Optional: clean-machine clone test (not only I:\ archive).  
3. Submit via arXiv using `SUBMIT_ARXIV.md`.

---

## Scope (locked)

Formal verification of the zero free-parameter scalar engine + contested cosmological readouts.  
Full 402-domain atlas stays on GitHub as the living thesis—not the main paper body.
