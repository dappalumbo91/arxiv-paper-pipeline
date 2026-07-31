---
name: arxiv-paper-pipeline
description: >
  End-to-end reproducible arXiv paper pipeline used for FSOT and future work:
  focused claim selection, FREEZE pins, clean-clone verification, LaTeX manuscript,
  scientist reproduction kit, pre-submit checklist (not in PDF), and Chrome upload
  field walkthrough. Use when the user wants a new arXiv paper, "write a paper from
  this repo", "reproduce the paper process", "arxiv pipeline", "scaffold paper",
  /arxiv-paper, or /new-paper.
---

# arXiv paper pipeline (standardized)

This skill codifies the **Paper 01** process so every future paper is produced the same way: top to bottom, reproducible, no admin checklist inside the PDF.

**Canonical human playbook (Desktop):**  
`C:\Users\damia\Desktop\arxiv-papers\PLAYBOOK.md`

**Scaffold template:**  
`C:\Users\damia\Desktop\arxiv-papers\_template\`

**Scaffold command:**  
```powershell
C:\Users\damia\Desktop\arxiv-papers\new-paper.ps1 -Slug "02-short-topic-name" -Title "Working Title Here"
```

**Reference paper (worked example):**  
`C:\Users\damia\Desktop\arxiv-papers\01-fsot-formal-contested-cosmology\`

---

## When invoked

1. Read `PLAYBOOK.md` if any step is unclear.
2. Ask only for missing essentials: **topic/source repo**, **primary claim**, **arxiv categories**, **title direction**.
3. Run the pipeline phases in order. Do not skip freeze + clean-clone verification for claim-heavy papers.
4. Never put pre-submission checklists inside `paper.tex` / PDF.
5. Do not automate arXiv login/submit; prepare paste fields + zip only.

---

## Phase 0 — Scope lock (do first)

Choose a **sharp claim** that can be placed cleanly:

| Good | Bad |
|------|-----|
| Formal methods + one empirical payoff | Monolithic “400-domain ToE” |
| One engine + contested sector | Unrelated multi-topic monograph |
| Executable kill criteria | Pure narrative |

Write 5 contributions max. Define claim taxonomy early:

- **Proved** — machine-checked
- **Numerically verified** — oracle/hash
- **Empirical** — external measured agreement
- **Interpretation** — narrative, not proof

Pick categories (example): primary `cs.LO`; cross-list as needed (`astro-ph.CO`, `math.LO`, …).

Create folder:

```text
Desktop/arxiv-papers/NN-short-slug/
```

Use `new-paper.ps1` or copy `_template`.

---

## Phase 1 — Source inventory

From the **authority repo/archive**:

1. README / thesis headline claims  
2. Formal modules (Lean/Coq/…)  
3. Verification reports / JSON ledgers  
4. Preregistered predictions / kill criteria  
5. One-command reproduction path  
6. Figures worth shipping  

Extract **exact numbers** into `FREEZE.yaml` (never hand-wave).

---

## Phase 2 — Freeze contract

Create `FREEZE.yaml` with:

- `edition_id`, dates, author  
- `repository.url`, `commit`, `recommended_tag`  
- oracle hashes if any  
- toolchains  
- formal counts / overall_ok  
- empirical headline metrics  
- reproduction commands  
- `artifacts_required_after_bundle`  

Rules:

- Freeze **before** heavy prose freezes numbers.  
- If code changes for repro (e.g. missing dependency), commit **on top** of freeze lineage and document both claim-freeze and repro-tip commits.  
- Tag: `vX.Y-arxiv-paperNN` when ready.

---

## Phase 3 — Scientist reproduction (before PDF polish)

1. **Clean clone** of the public repo (not only author archive).  
2. Install deps from `requirements.txt` (fix missing deps **in the repo**, not only paper docs).  
3. Run one-command verification bundle.  
4. Run `verify_paper_claims.py --strict-hash` (and optionally `--require-cross-proof`).  
5. Fix broken docs (wrong CLI intents, missing packages).  
6. Write `CLEAN_CLONE_REPRO_REPORT.md`.  
7. Archive log under `logs/`.

If clean clone fails, **fix the repo**, then continue the paper.

---

## Phase 4 — Manuscript skeleton

Write in this order:

1. Title options (`title_options.txt`) → pick non-overclaiming title  
2. Abstract (`abstract.txt`, ≤1920 chars for arXiv form)  
3. `paper.tex` (primary) + optional `paper.md` working draft  
4. Software availability box + GitHub URL  
5. Intro + contributions + claim taxonomy  
6. Math / methods (full definitions, not sketches)  
7. Results tables + figures with **regenerate one-liners** in captions  
8. Falsifiability / one-command repro  
9. Discussion (related work, limitations, how to read claim stack)  
10. Conclusion + data availability (tag/commit)  
11. `references.bib` with DOIs where possible  

**Do not** put admin checklists in the PDF appendix.

Depth rule: main body 12–20 pages focused; bulk atlas → GitHub / anc.

---

## Phase 5 — Package files (every paper)

Required in the paper directory:

| File | Role |
|------|------|
| `paper.tex` / `paper.pdf` | Manuscript |
| `references.bib` / `paper.bbl` | Bibliography |
| `abstract.txt` | arXiv abstract field |
| `comments.txt` | arXiv comments field |
| `title.txt` | Chosen title |
| `FREEZE.yaml` | Immutable pins |
| `SCIENTIST_REPRODUCE.md` | Independent repro contract |
| `verify_paper_claims.py` | Automated freeze checker |
| `PRE_SUBMISSION_CHECKLIST.md` | Admin only (not in PDF) |
| `ARXIV_UPLOAD_WALKTHROUGH.md` | Chrome field-by-field |
| `figures/` | Embedded figures |
| `arxiv_upload/` + `arxiv_source_v1.zip` | Upload package |
| `logs/` | Verification logs |

Optional but recommended:

- `CLEAN_CLONE_REPRO_REPORT.md`  
- `PACKAGE_AND_DEPTH_REVIEW.md`  
- `READY_TO_SUBMIT.md`  
- `create_github_freeze_tag.ps1`  

---

## Phase 6 — Polish pass (standard)

Run a fixed review pass:

1. Abstract readability (short first sentences)  
2. Equation spacing for dense blocks  
3. Figure captions: path + regenerate command  
4. Tables: explain pooled vs single-row outliers  
5. Align bib commit/tag with software box  
6. Intermediate symbols for long products if needed  
7. Confirm no admin appendix in PDF  

---

## Phase 7 — Pre-submit (separate checklist)

Use `PRE_SUBMISSION_CHECKLIST.md` only:

- Tag pushed  
- Clean-clone PASS  
- PDF builds; figures embedded  
- Abstract ≤1920 chars  
- Categories chosen  
- Comments paste ready  
- Zip refreshed  

User submits in Chrome. Agent prepares paste blocks only.

---

## Phase 8 — After public

1. Put arXiv ID on GitHub README.  
2. Optional GitHub Release pointing at abstract.  
3. Do not change claim numbers without new freeze + paper revision.

---

## Agent behaviors (non-negotiable)

1. **Numbers only from freeze / live JSON** — no invented percentages.  
2. **Clean clone required** for claim-heavy papers.  
3. **Fix repo deps** when bare install fails (e.g. matplotlib).  
4. **No checklist in PDF.**  
5. **No arXiv login automation.**  
6. Prefer LaTeX `article` + `plain` bib for first pass; keep sources flat-friendly for arXiv.  
7. Keep scope tight; push breadth to GitHub living thesis.  
8. Title: avoid “resolving / solved” unless empirically and statistically justified in community terms.

---

## Quick start prompt (user can paste)

```text
/arxiv-paper
Source: <repo or archive path>
Claim: <one sentence>
Categories: primary <cs.LO>, cross-list <...>
Scaffold paper NN-<slug> and run the full pipeline through READY_TO_SUBMIT.
```

---

## Lessons learned from Paper 01 (carry forward)

- Public GitHub clone was ~0.5 GB — size anxiety often overstated; still verify.  
- Publication bundle may dirty working tree (timestamps) — compare values, not git clean.  
- Wrong CLI intents in docs (`hubble_tension`) break skeptic path — test real commands.  
- Commit drift (1863 vs 1873) — freeze acceptance rule `>=` + document tip commit.  
- Admin checklist in PDF looks unprofessional — always separate file.  
- Pooled medians need one sentence when single rows are larger.  
