# Independent reproduction — {{TITLE}}

**Repo:** {{REPO_URL}}  
**Freeze:** see `FREEZE.yaml`  
**Paper package:** this directory

## What “reproduced” means

| Layer | Pass criterion |
|-------|----------------|
| A. Publication / empirical | One-command exits 0; FREEZE metrics match |
| B. Parameter / honesty | Domain-specific audits if any |
| C. Formal (optional) | overall_ok / zero sorry as pinned |

## Tier 0 — quick path

```bash
git clone {{REPO_URL}}.git
cd REPO
git checkout TAG   # from FREEZE.yaml
pip install -r requirements.txt
# REPLACE one-command:
python scripts/REPLACE_BUNDLE.py
```

Then from this paper directory:

```bash
python verify_paper_claims.py --fsot-root /path/to/clone --strict-hash
```

## Tier 1+ 

Document Lean/multi-prover or domain-specific deeper checks here.

## What would falsify

1. Clean freeze checkout fails one-command hard.  
2. FREEZE metrics not recovered.  
3. Formal overall_ok false when toolchains present (if claimed).  

## What does not falsify

- Missing optional hardware  
- Narrative disagreement while ledger passes  
