# {{SLUG}} — {{TITLE}}

**Author:** {{AUTHOR}}  
**Started:** {{DATE}}  
**Status:** scaffold (fill FREEZE → verify → draft → package → submit)

## Manuscript naming (required)

| File | Role |
|------|------|
| **`{{MANUSCRIPT_BASENAME}}.tex`** | LaTeX source (topic-named) |
| **`{{MANUSCRIPT_BASENAME}}.pdf`** | Built PDF (topic-named — **never** bare `paper.pdf`) |
| `manuscript_basename.txt` | Records the basename for scripts |

Build:

```powershell
.\build-pdf.ps1
# equivalent:
# pdflatex {{MANUSCRIPT_BASENAME}}.tex
# bibtex {{MANUSCRIPT_BASENAME}}
# pdflatex {{MANUSCRIPT_BASENAME}}.tex
# pdflatex {{MANUSCRIPT_BASENAME}}.tex
```

## Source

- Repository: {{REPO_URL}}
- Primary arXiv category: {{PRIMARY_CATEGORY}}

## Pipeline (do in order)

See parent playbook: `../PLAYBOOK.md`

1. Fill `FREEZE.yaml` from the authority repo  
2. Clean-clone + `verify_paper_claims.py`  
3. Draft `{{MANUSCRIPT_BASENAME}}.tex`  
4. `SCIENTIST_REPRODUCE.md`  
5. Polish + `PRE_SUBMISSION_CHECKLIST.md` (not in PDF)  
6. Build zip + Chrome upload (`ARXIV_UPLOAD_WALKTHROUGH.md`)
