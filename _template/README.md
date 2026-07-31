# {{SLUG}} — {{TITLE}}

**Author:** {{AUTHOR}}  
**Started:** {{DATE}}  
**Status:** scaffold (fill FREEZE → verify → draft → package → submit)

## Source

- Repository: {{REPO_URL}}
- Primary arXiv category: {{PRIMARY_CATEGORY}}

## Pipeline (do in order)

See parent playbook: `../PLAYBOOK.md`

1. Fill `FREEZE.yaml` from the authority repo  
2. Clean-clone + `verify_paper_claims.py`  
3. Draft `paper.tex`  
4. `SCIENTIST_REPRODUCE.md`  
5. Polish + `PRE_SUBMISSION_CHECKLIST.md` (not in PDF)  
6. Build zip + Chrome upload (`ARXIV_UPLOAD_WALKTHROUGH.md`)

## One-command rebuild (after LaTeX is real)

```powershell
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```
