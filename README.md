# arXiv Paper Pipeline

Reproducible **start-to-finish process** for writing arXiv papers, plus a living archive of manuscripts produced with it.

**Author:** Damian Arthur Palumbo  
**Repo:** https://github.com/dappalumbo91/arxiv-paper-pipeline

Born from FSOT research:

| Paper | Folder | Focus |
|-------|--------|--------|
| 01 | [`papers/01-fsot-formal-contested-cosmology/`](papers/01-fsot-formal-contested-cosmology/) | Formal scalar engine + contested cosmology (Lean 4 / multi-prover) |
| 02 | [`papers/02-fsot-fuel-lab-formal/`](papers/02-fsot-fuel-lab-formal/) | Same engine applied to Fuel Lab thermochemistry (PRED-034) |

Code under test for both papers: [FSOT-2.1-Lean](https://github.com/dappalumbo91/FSOT-2.1-Lean) tag `v2.6-arxiv-paper01`.

---

## Quick start (new paper)

```powershell
git clone https://github.com/dappalumbo91/arxiv-paper-pipeline.git
cd arxiv-paper-pipeline
.\new-paper.ps1 -Slug "my-topic" -Title "Working Title" -RepoUrl "https://github.com/you/repo"
```

Then follow **[PLAYBOOK.md](PLAYBOOK.md)** end to end:

1. Scope lock  
2. FREEZE.yaml pins  
3. Clean-clone verification  
4. Draft `paper.tex`  
5. Scientist kit + claim checker  
6. Polish  
7. `PRE_SUBMISSION_CHECKLIST.md` (never inside the PDF)  
8. Build zip → upload on arXiv.org in your browser  

### Grok Build skill (optional)

Copy the skill into your user skills directory:

```powershell
Copy-Item -Recurse .\grok-skill\arxiv-paper-pipeline $env:USERPROFILE\.grok\skills\
```

Triggers: `/arxiv-paper`, `/new-paper`, “write an arXiv paper from this repo”.

---

## Repository layout

```text
PLAYBOOK.md              # human process
new-paper.ps1            # scaffold next paper
_template/               # empty paper package
grok-skill/              # Grok skill sources
papers/
  01-.../                # full package (tex, pdf, freeze, repro)
  02-.../
```

---

## Manuscript naming

PDFs and TeX sources are **topic-named** after the paper slug (folder name):

- `papers/01-fsot-formal-contested-cosmology/01-fsot-formal-contested-cosmology.pdf`
- `papers/02-fsot-fuel-lab-formal/02-fsot-fuel-lab-formal.pdf`

Never leave the deliverable as bare `paper.pdf`. Scaffold sets `manuscript_basename.txt`; build with `.\build-pdf.ps1`.

## Design rules (non-negotiable)

- Numbers come from **FREEZE.yaml** / live JSON — not memory.  
- **Clean-clone** verify claim-heavy papers before final prose.  
- Fix missing deps **in the science repo**, not only in paper docs.  
- **No admin checklist inside the PDF.**  
- **No arXiv login automation** — prepare paste fields + zip only.  
- Keep scope tight; breadth lives on GitHub living theses.

---

## License

Apache-2.0 for pipeline tooling unless a paper folder states otherwise.  
Manuscripts remain the author's scientific work; cite the relevant paper folder and the FSOT-2.1-Lean tag when reproducing numerical claims.

