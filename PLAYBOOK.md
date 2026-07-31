# arXiv paper pipeline — start-to-finish playbook

**Purpose:** Reproduce exactly the process used for  
`01-fsot-formal-contested-cosmology` for any future paper.

**Skill (Grok Build):** `/arxiv-paper` or `/new-paper` → skill `arxiv-paper-pipeline`  
**Scaffold:** `.\new-paper.ps1 -Slug "02-topic" -Title "..."`  
**Template:** `_template\`  
**Worked example:** `01-fsot-formal-contested-cosmology\`

---

## Overview (one page)

```text
0 Scope lock
1 Inventory source repo / archive
2 FREEZE.yaml (numbers + commit pins)
3 Clean-clone verification + fix repo gaps
4 Draft {slug}.tex → build {slug}.pdf (topic-named, never bare paper.pdf)
5 Scientist kit + claim checker
6 Polish (title, abstract, eqs, captions, bib)
7 PRE_SUBMISSION_CHECKLIST (admin only — not in PDF)
8 Build arxiv_source_v1.zip + Chrome upload fields
9 After public: arXiv ID → GitHub README
```

---

## Phase 0 — Scope lock

**Goal:** one placeable claim.

Write:

1. Working title (and a softer alternate)  
2. Primary arXiv category + optional cross-lists  
3. Five contributions max  
4. In-scope / out-of-scope table  
5. Claim taxonomy (proved / numerical / empirical / interpretation)

**Anti-pattern:** full multi-domain monograph as the first paper.

Scaffold:

```powershell
cd $env:USERPROFILE\Desktop\arxiv-papers
.\new-paper.ps1 -Slug "02-my-topic" -Title "Working Title" -Number 2
```

---

## Phase 1 — Source inventory

From the authority tree (GitHub and/or physical archive):

| Pull | Examples |
|------|----------|
| Headline claims | README abstract |
| Formal spine | Lean/Coq modules, obligation counts |
| Verification reports | `*_report.json`, certificates |
| Empirical ledgers | contested watch, domain atlas |
| Prereg / kill criteria | manifests, navigator |
| Repro command | one-command bundle |
| Figures | paths under `data/figures` |

Record paths in `outline.md` or paper README.

---

## Phase 2 — FREEZE.yaml

Create immutable pins **before** finalizing prose numbers.

Minimum keys: see `_template/FREEZE.yaml`.

Rules:

- Prefer live JSON over memory.  
- Document oracle hashes.  
- If live count drifts slightly, use acceptance `>= freeze_min`.  
- Recommended scientist checkout = tagged tip (may include deps fix on top of claim freeze).

Tag when ready:

```powershell
git tag -a vX.Y-arxiv-paperNN <commit> -m "arXiv paper NN freeze"
git push origin vX.Y-arxiv-paperNN
```

---

## Phase 3 — Clean-clone verification

**Do not skip** for claim-heavy papers.

```powershell
git clone <repo-url> ...\_clean_clone\<repo>
cd ...\_clean_clone\<repo>
git checkout <freeze-or-tag>
pip install -r requirements.txt
# run paper's one-command
python scripts\...
python <paper>\verify_paper_claims.py --fsot-root . --strict-hash
```

Then:

1. Write `CLEAN_CLONE_REPRO_REPORT.md`  
2. Save log to `logs/`  
3. **If bare install fails** (missing matplotlib, wrong CLI): fix **upstream repo**, push, retag if needed  

---

## Phase 4 — Manuscript

Preferred order of writing:

1. Title + abstract + contributions  
2. Software box (clone + one-command)  
3. Math / definitions (full, not sketch)  
4. Methods / formal verification  
5. Results + tables + figures  
6. Falsifiability  
7. Discussion + limitations + claim-stack reading guide  
8. Conclusion + data availability  
9. Bibliography  

**Hard rule:** no pre-submit checklist in the PDF.

Captions must include:

- artifact path  
- one-line regenerate command  

Tables with pooled medians must note outliers if individual rows are larger.

---

## Phase 5 — Scientist package

Always ship:

- `SCIENTIST_REPRODUCE.md` (tiered: 15 min → full formal)  
- `verify_paper_claims.py` driven by `FREEZE.yaml`  
- `EXPECTED_ARTIFACTS.md`  

---

## Phase 6 — Polish checklist

- [ ] Abstract short first sentences  
- [ ] `\mbox{...}` or reflow for critical monospaced tokens  
- [ ] Equation spacing for dense blocks  
- [ ] Intermediate symbols for long products if needed  
- [ ] Bib commit/tag matches software box  
- [ ] PDF text extract: no “Pre-submission checklist”  

---

## Phase 7 — Pre-submit (admin file only)

Use `PRE_SUBMISSION_CHECKLIST.md` — **never** paste into the manuscript `.tex`.

### Manuscript file naming (required)

The PDF and TeX **must** be named for the topic/slug, not `paper.pdf`:

| Wrong | Right |
|-------|--------|
| `paper.pdf` | `02-fsot-fuel-lab-formal.pdf` |
| `paper.tex` | `02-fsot-fuel-lab-formal.tex` |

`new-paper.ps1` sets `manuscript_basename.txt` to the folder slug. Build with:

```powershell
.\build-pdf.ps1
```

Build upload package:

```powershell
# from paper dir
.\build-pdf.ps1
# copy {basename}.tex, {basename}.bbl, references.bib, figures/ into arxiv_upload/
Compress-Archive -Path arxiv_upload\* -DestinationPath arxiv_source_v1.zip -Force
```

---

## Phase 8 — arXiv upload (human in Chrome)

1. https://arxiv.org/submit  
2. Upload `arxiv_source_v1.zip` as TeX  
3. Paste `title.txt`, `abstract.txt`, `comments.txt`  
4. Primary category + cross-lists  
5. Preview PDF → Submit  

Walkthrough template: `ARXIV_UPLOAD_WALKTHROUGH.md`  
**No browser automation** (license/authorship).

---

## Phase 9 — After public

- arXiv ID → GitHub README  
- Optional Release notes  
- New freeze for any number changes  

---

## Directory layout (standard)

```text
Desktop/arxiv-papers/
  PLAYBOOK.md                 ← this file
  new-paper.ps1
  _template/                  ← copy source
  01-.../                     ← paper 1
  02-.../                     ← paper 2
  _clean_clone/               ← disposable clean clones
```

Each paper:

```text
NN-slug/
  {slug}.tex {slug}.pdf references.bib {slug}.bbl
  manuscript_basename.txt build-pdf.ps1
  abstract.txt comments.txt title.txt title_options.txt
  FREEZE.yaml
  SCIENTIST_REPRODUCE.md
  verify_paper_claims.py
  PRE_SUBMISSION_CHECKLIST.md
  ARXIV_UPLOAD_WALKTHROUGH.md
  CLEAN_CLONE_REPRO_REPORT.md
  figures/
  logs/
  arxiv_upload/
  arxiv_source_v1.zip
  README.md
```

---

## Timing expectations (rough)

| Phase | Time |
|-------|------|
| Scope + inventory | 1–3 h |
| Freeze + clean clone | 1–4 h (deps on repo) |
| First full draft | 1–3 days |
| Polish + package | 0.5–1 day |
| Upload | 30–60 min |

Paper 01 clean-clone verification was ~minutes once clone finished; formal Lean rebuild is optional and slower.

---

## Definition of done

A paper package is **done** when:

1. Clean-clone verification **PASS** (or documented Tier-1 PASS)  
2. FREEZE + tag published  
3. PDF builds without admin appendix  
4. Zip + paste fields ready  
5. READY_TO_SUBMIT / checklist all green except human Chrome steps  
