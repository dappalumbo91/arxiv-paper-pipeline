# arXiv Completeness Audit

**Paper:** Formally Verified Parameter-Free Scalar Engine Resolving Cosmological Tensions  
**Compared against:** arXiv format/moderation policies; peer Lean-in-science papers; cosmology H₀ papers  
**Date:** 2026-07-31

---

## What arXiv expects (scholarly contribution)

arXiv accepts **topical, refereeable scientific contributions** that follow scholarly communication norms:

| Requirement | Status | Notes |
|-------------|--------|-------|
| Title + non-anonymous authorship | ✅ | Damian Arthur Palumbo |
| Self-contained research article | ✅ / ⚠ | Main argument stands alone; atlas is out of scope by design |
| Complete references | ⚠ | Present but thin vs cosmology / formal-methods peers — expand |
| Public code/data links that resolve | ✅ | GitHub URL (must stay public at submission) |
| Machine-readable PDF (LaTeX preferred) | ❌ | Currently Markdown draft — **convert before submit** |
| Abstract ≤ 1920 characters | ⚠ | Previous draft ~1947 chars — **shortened in this pass** |
| No watermarks / ads / line numbers | ✅ | N/A for draft |
| Claim honesty / not pure marketing | ✅ | Claim taxonomy section is a strength |

Sources: [arXiv format requirements](https://info.arxiv.org/help/policies/format_requirements.html), [title/abstract prep](https://info.arxiv.org/help/prep.html), [content types](https://info.arxiv.org/help/policies/content-types.html).

---

## What a good arXiv paper *does* (function, not format)

| Function | Peer examples | Our paper |
|----------|---------------|-----------|
| States a sharp, falsifiable claim | HepLean: digitalise HEP defs/theorems; Bobbin: formalise Langmuir/BET | Formal engine + contested cosmology — sharp enough |
| Separates proved vs conjectured | Bobbin et al. (cs.LO) — premises explicit | ✅ Claim taxonomy (strong) |
| Gives full math definitions | HepLean, Bobbin, Cosmology H₀ papers | ✅ Expanded full formulas this pass |
| Names theorems / artifacts | Domain sign theorems; Wave-1 intervals | ✅ Inventory table this pass |
| Points to executable code | GitHub for Lean projects | ✅ Software box + Comments field |
| Cites prior art fairly | Related work sections | ⚠ Expanded; still needs DOI polish |
| Limits scope | HepLean: 3 HEP areas only | ✅ Deliberate 402-domain deferral |
| Reproducibility protocol | REPRODUCE / one-command | ✅ Strong |

**Closest peer positioning:**

1. **Bobbin et al., arXiv:2210.12150** (cs.LO) — *Formalizing Chemical Physics using the Lean Theorem Prover*  
   - Formalises classical scientific theories in Lean; explicit premises; Mathlib use.  
   - *We go further on multi-prover export + empirical contested sector; they are cleaner on pure formal narrative.*

2. **Tooby-Smith, arXiv:2405.08863** (hep-ph + cs.LO) — *HepLean*  
   - Open-source Lean 4 digitalisation of HEP; ~16 pages; clear benefits list.  
   - *Template for “Lean + physics domain” paper length and tone.*

3. **H₀ tension literature** (Riess, Planck, Poulin reviews)  
   - Careful uncertainty treatment (σ, not just % error).  
   - *We must not claim “solved the Hubble tension” in the community’s statistical sense; PRED-001 bridge + dual-anchor % error is the defensible claim.*

---

## Completeness scorecard (this draft after upgrades)

| Area | Score | Gap |
|------|------:|-----|
| Title / abstract / keywords | 9/10 | Abstract length fixed; good scope sentence |
| Introduction + contributions | 9/10 | Strong; taxonomy is rare and good |
| Full mathematics of engine | 9/10 | Full term1/2/3 + Wave-1 H₀ formulas |
| Formal methods methodology | 8/10 | Need more named proof templates / toolchain table |
| Contested cosmology results | 7/10 | Tables good; add σ-style caution on “tension resolved” |
| Related work | 7/10 | Bobbin, HepLean, Riess, Planck cited; expand BAO/DESI |
| Reproducibility + GitHub | 9/10 | Front-matter software box + comments metadata |
| Figures in manuscript body | 5/10 | Files exist in `figures/` — embed captions in LaTeX next |
| Bibliography quality | 6/10 | Need full bibliographic entries + arXiv IDs |
| LaTeX / PDF readiness | 2/10 | **Blocking for submission** |
| Tagged GitHub release matching freeze | 3/10 | **Blocking for scientific hygiene** |
| Author ORCID / affiliation detail | 4/10 | Independent researcher only — add ORCID if available |

**Overall readiness for arXiv upload:** ~65% (content draft strong; packaging incomplete).  
**Overall readiness as scientific claim structure:** ~80% (math + scope + falsification solid).

---

## Risks for moderators / hostile readers

1. **Overclaim language** — “resolving cosmological tensions” in the title is aspirational. Abstract/body correctly use dual-anchor bridge + % error; title may draw fire. Consider softer title if cross-listing astro-ph.CO.
2. **% error vs σ tension** — Cosmology community speaks in σ; our ledger uses relative % vs anchors. Both can coexist if clearly defined.
3. **ToE adjacency** — 402-domain pointer must stay secondary or moderators may treat as overreach.
4. **Independent researcher** — allowed; reproducibility must be airtight.
5. **Obligation count drift** (1863 vs 1873) — freeze before tag.

---

## Recommended next steps (priority order)

1. **P0 — Freeze tag** of FSOT-2.1-Lean matching `claims_freeze.yaml`.  
2. **P0 — Soften title option** for astro-ph.CO comfort (see paper front matter).  
3. **P1 — LaTeX conversion** (article class, equation numbers, figure includes).  
4. **P1 — Full BibTeX** with DOIs for Planck, Riess, DES, Bobbin, HepLean.  
5. **P2 — Figure captions** wired into paper body.  
6. **P2 — ORCID**.  
7. **P3 — arXiv submit** primary `cs.LO`, cross-list `astro-ph.CO` or `math.LO`.

---

## Suggested arXiv Comments field (ASCII, ready)

```
18 pages + references. Source code, Lean 4 formalization, five-prover
verification bundle, and contested-sector ledger:
https://github.com/dappalumbo91/FSOT-2.1-Lean
One-command verification: python scripts/run_publication_verification_bundle.py
Edition freeze 2026-07-16. Comments welcome.
```
