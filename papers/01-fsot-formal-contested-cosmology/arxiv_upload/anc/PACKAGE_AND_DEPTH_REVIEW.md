# Package + depth review (what the PDF has / still lacks)

## Checklist location (your question)

| Place | Correct? |
|-------|----------|
| End of **PDF / paper.tex** as Appendix | **No** — removed. Internal admin; not scholarly content. |
| Separate file **`PRE_SUBMISSION_CHECKLIST.md`** | **Yes** — use this only before you submit. |
| arXiv Comments field | **Yes** — paste `comments.txt` (not the checklist). |

---

## What the PDF currently contains (11 pages)

1. **Abstract + software box** — claim, numbers, clone path, tag  
2. **§1 Introduction** — problem, operational claim, scope, 5 contributions, claim taxonomy  
3. **§2 Scalar engine** — full seed constants, term1/2/3, Wave-1 $H_0,T_{\mathrm{CMB}},n_s,\Omega_b h^2,\alpha_s$  
4. **§3 Formal methods** — oracle hash, Lean theorems, five provers, error metric, non-claims  
5. **§4 Contested sector** — tables, bubble-bleed linked to equations, PRED-001/002/005, $H_0$ worked example, cautions on $\sigma$  
6. **§5 Core empirical** — tight high-precision domains + atlas context  
7. **§6 Falsifiability** — one-command, artifacts, freeze checker, reject criteria  
8. **§7 Discussion** — related work, strengths/limitations, **how to read the claim stack**  
9. **§8 Conclusion**  
10. **Acknowledgments + Data availability** (tag `v2.6-arxiv-paper01`)  
11. **References**  

Figures: $H_0$ landscape, contested vs baseline, five-prover obligation map.

**Admin checklist is no longer in the PDF** (verified by text extract).

---

## Depth: crucial vs optional

### Present and sufficient for a focused first paper

| Topic | Depth |
|-------|--------|
| Zero free-parameter statement | Clear + audit path |
| Full engine math | Present (not a sketch) |
| Formal vs empirical vs interpretation | Explicit taxonomy |
| Multi-prover story | Table + artifact paths |
| Contested $H_0$ with PRED | Worked numbers + discriminants |
| How to reproduce / falsify | Executable |
| Limitations | Honest list |

### Nice deeper, not required for v1

| Topic | Why optional |
|-------|----------------|
| Full 402-domain tables | Lives on GitHub by design |
| Full $\sigma$ cosmology MCMC | Separate paper |
| Line-by-line Lean proof scripts | Repo is the proof |
| Consciousness / fuels | Explicitly out of scope |
| Longer related-work survey | Can grow in v2 |

### Gaps we closed in this pass

- Bubble-bleed now **points at equation numbers** (not free-floating metaphor)  
- PRED-002 / PRED-005 table added  
- Discussion expanded with **claim-stack reading guide**  
- Data availability points at **tag v2.6-arxiv-paper01**  
- Checklist **out of the PDF**

### Remaining non-blocking gaps (aware, not blocking)

1. No full derivation appendix in PDF (GitHub `THESIS_APPENDIX_DERIVATIONS.md`) — pointer is enough.  
2. Contested “~15% baseline” is repository-scale, not a single published survey figure — already caveated.  
3. `spine_walkthrough.png` not in PDF (three figures already; optional fourth).  
4. ORCID not in author line (optional).

---

## Package map (what to open)

| File | Role |
|------|------|
| **`paper.pdf`** | Manuscript to read |
| **`PRE_SUBMISSION_CHECKLIST.md`** | Your admin checklist (this is what replaced the appendix) |
| **`ARXIV_UPLOAD_WALKTHROUGH.md`** | Chrome form field-by-field |
| **`arxiv_source_v1.zip`** | Upload to arXiv |
| **`title.txt` / `abstract.txt` / `comments.txt`** | Form paste |
| **`FREEZE.yaml`** | Number pins |
| **`SCIENTIST_REPRODUCE.md`** | Independent repro |
| **`logs/verify_paper_claims_clean.log`** | Latest freeze-check log |
| **`CLEAN_CLONE_REPRO_REPORT.md`** | Clean-clone evidence |

---

## Verdict on “missing crucial explanation?”

For a **focused** formal + contested-cosmology first arXiv paper: **no critical hole remains**.  
What was wrong was **putting the pre-submission checklist inside the paper** — that is fixed.

If a referee wants more physics depth, they will ask for likelihood-level $H_0$ analysis or a longer derivation appendix; those are **v2 / follow-on**, not blockers for this scope.
