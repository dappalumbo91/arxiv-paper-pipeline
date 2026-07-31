# First arXiv paper — thorough readiness review

**Manuscript:** Formally Verified Parameter-Free Scalar Engine Resolving Cosmological Tensions  
**Review date:** 2026-07-31  
**Clean-clone empirical path:** **PASS** (see `CLEAN_CLONE_REPRO_REPORT.md`)

---

## Executive verdict

| Dimension | Grade | Notes |
|-----------|:-----:|-------|
| Reproducibility (Tier 1 empirical) | **A** | Clean GitHub clone + bundle exit 0, freeze checker PASS |
| Math completeness | **A−** | Full term1/2/3 + Wave-1 formulas; Lean module paths cited |
| Claim honesty / taxonomy | **A** | Proved vs empirical vs interpretation — essential for first paper |
| GitHub linkage | **A** | Front box, abstract, Comments, Data availability |
| Bibliography | **B+** | DOIs for core refs; could add DESI DR2 primary paper |
| Cosmology community caution | **B+** | % vs σ noted; title still claim-forward |
| Formal re-execution (Tier 2–3) | **B** | Shipped certificates pass; full lake/multi-prover not re-run on clean clone |
| Packaging for arXiv upload | **A−** | PDF builds (11 pp); add `matplotlib` note; tag not pushed yet |
| First-author polish | **B+** | Ready for submission after tag + optional title softener |

**Overall:** Strong enough for a first arXiv preprint in **cs.LO** with optional **astro-ph.CO** cross-list, provided you (1) push freeze tag, (2) keep claim language careful, (3) treat clean-clone report as the reproducibility evidence.

---

## What arXiv moderators / readers will look for

| Expectation | Status |
|-------------|--------|
| Self-contained scientific claim | Yes — formal engine + contested cosmology |
| Not pure marketing / empty ToE | Yes — scoped; atlas deferred |
| Public code that resolves | Yes — GitHub HEAD = freeze commit |
| Runnable reproduction | **Verified clean clone** |
| Math present | Yes |
| References | Adequate |
| Honest limitations | Yes |
| Anonymous? | N/A — named author required |

---

## Clean-clone findings that improve the paper

1. **Repo size is fine** (~0.5 GB) — address size anxiety in abstract/comments if needed.  
2. **Bundle is fast** (~25 s) — good for reviewers.  
3. **matplotlib gap** — document until upstream `requirements.txt` updated.  
4. **Wrong intent name** — fixed to `cosmology_cmb`.  
5. **Atomic count on GitHub = 1863** — aligns with paper; archive 1873 was a red herring.

---

## Remaining before submit (ordered)

### Must do

1. **Push freeze tag** `v2.6-arxiv-paper01` → `81bc893`  
   `.\create_github_freeze_tag.ps1 -Push`  
2. Rebuild PDF after last tex edits: `pdflatex` + `bibtex` cycle  
3. Upload flat sources + `paper.bbl` + figures  

### Strongly recommended

4. Soften title if cross-listing `astro-ph.CO` (optional alternate in YAML front matter)  
5. Upstream PR: add `matplotlib>=3.8` to repo `requirements.txt`  
6. Upstream PR: fix skeptic kit `hubble_tension` → `cosmology_cmb`  
7. ORCID in author line if you have one  

### Nice to have

8. DESI primary citation for $w_a$  
9. Page budget closer to 15–18 with slightly expanded related work  
10. Zenodo DOI for freeze tarball  

---

## Risk register (first-paper specific)

| Risk | Severity | Mitigation |
|------|----------|------------|
| Title “Resolving…Tensions” read as overclaim | Medium | Body language careful; optional softer title |
| Independent researcher without affiliation | Low | Code-first verification is the answer |
| cs.LO endorsement needed | Medium | Request endorsement early if new to category |
| Reviewer asks for full 402-domain proof | Low | Scope section + GitHub pointer |
| Reviewer rejects % error as cosmology metric | Medium | Already caveat σ vs % |
| matplotlib missing for bare venv | Medium | Documented; upstream fix |

---

## Do not do before v1

- Expand paper into full ToE monograph  
- Claim “Hubble tension solved at 5σ”  
- Require ESP32 for acceptance  
- Hand-edit claim JSON to “look better”

---

## Final recommendation

**Submit-ready after freeze tag + PDF rebuild.**  
Your clean-clone test is the strongest asset for a first arXiv paper: you can honestly write that an independent clone reproduces the publication bundle and freeze checker without the author’s archive.
