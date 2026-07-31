# Next steps (post completeness audit)

## Status snapshot

| Item | Status |
|------|--------|
| Manuscript draft with full math | Done (`paper.md` v2) |
| GitHub linked in body + Comments metadata | Done |
| arXiv completeness audit | Done (`ARXIV_COMPLETENESS_AUDIT.md`) |
| Figures copied locally | Done (`figures/`) |
| Frozen claim numbers | Done (`claims_freeze.yaml`) |
| Git tag matching freeze | **Todo** |
| LaTeX / PDF for arXiv | **Todo** |
| Full DOI bibliography | **Todo** |

## Immediate priorities

### 1. Content review (you + Grok)

Read `paper.md` and flag:

- Any claim that feels too strong (especially title “Resolving”)
- Any number that doesn’t match your preferred freeze
- Sections to cut for page budget

### 2. Tag the repository (P0)

On the FSOT-2.1-Lean tree that matches the freeze:

```bash
# after clean verification
git tag -a v2.6-arxiv-paper01 -m "Edition freeze for arXiv paper 01 formal+contested"
git push origin v2.6-arxiv-paper01
```

Update paper Comments / abstract to cite that tag.

### 3. LaTeX conversion (P1)

Convert `paper.md` → `paper.tex` with:

- `article` or `revtex` / `amsart` style as preferred
- Numbered equations matching §2
- `\includegraphics` for the five figures
- `.bbl` for arXiv (not only `.bib`)

### 4. Bibliography polish (P1)

Replace thin references with full BibTeX from:

- Planck 2018 (A&A)
- Riess SH0ES ApJL 2022
- Bobbin arXiv:2210.12150
- HepLean arXiv:2405.08863
- DES Y3, PDG 2024

### 5. Soften title? (decision)

If cross-listing `astro-ph.CO`, consider the alternate title already noted in the YAML front matter (less “resolving,” more “machine-checked engine for contested cosmology”).

### 6. Submit

- Primary: `cs.LO`
- Cross-list: `astro-ph.CO` and/or `math.LO`
- Comments field: use the ASCII block already in `paper.md`
- Abstract: verify ≤1920 characters in the arXiv form (ASCII)

## What not to do yet

- Expand main body into 402-domain atlas
- Claim community-consensus “Hubble tension solved” in σ units without a dedicated cosmology analysis paper
- Change oracle constants without re-freezing
