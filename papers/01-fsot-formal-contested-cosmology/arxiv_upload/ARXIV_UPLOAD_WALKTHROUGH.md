# arXiv upload walkthrough (you do this in Chrome)

**You are correct:** Grok cannot log into your Google/Chrome arXiv session or click Submit for you.  
arXiv requires *you* to authenticate and accept the license. What follows is every field, ready to copy-paste.

**Package on disk:**  
`C:\Users\damia\Desktop\arxiv-papers\01-fsot-formal-contested-cosmology\`

| File | Use |
|------|-----|
| `arxiv_source_v1.zip` | Upload this (or the `arxiv_upload\` folder contents) |
| `paper.pdf` | Local preview only (arXiv will rebuild PDF from TeX) |
| `abstract.txt` | Abstract field |
| `comments.txt` | Comments field |
| `title_options.txt` | Title decision |

---

## Before you start (2 minutes)

1. Open Chrome (signed into the Google account you use for arXiv).
2. Open a second window/tab with this folder so you can copy files.
3. Have GitHub open: https://github.com/dappalumbo91/FSOT-2.1-Lean (tag `v2.6-arxiv-paper01`).
4. Optional: skim local `paper.pdf` once more.

Start here: **https://arxiv.org/submit**  
(If prompted: log in / register with the same email you want as author contact.)

---

## Step-by-step form fields

### A. Start submission

| UI item | What to do |
|---------|------------|
| **New submission** | Click to start |
| **Agreement / license** | Accept arXiv’s non-exclusive distribution license (default is fine; do not add a conflicting copyright line in the paper) |
| **Endorse?** | If arXiv says you need endorsement for `cs.LO`, pause and request endorsement *before* finishing. First-time category submitters often hit this. |

---

### B. File upload

| UI item | What to enter |
|---------|----------------|
| **Process / type** | Prefer **TeX** / process with TeX (not “PDF only” if both offered) |
| **Upload** | Upload **`arxiv_source_v1.zip`** from the paper folder |

**What is inside the zip (so you can check arXiv’s file list):**

```
paper.tex
paper.bbl
references.bib
figures/… (pngs)
anc/… (optional: FREEZE.yaml, SCIENTIST_REPRODUCE.md, verify_paper_claims.py, …)
```

| After upload | What you want |
|--------------|----------------|
| **Process / Compile** | arXiv runs LaTeX |
| **Preview PDF** | Open it. Check: title, abstract, figures (H₀, contested, obligation map), references |

**If compile fails:** usually missing `.bbl` or figure path. Re-upload zip; `paper.bbl` is already included.

**If preview looks fine:** continue to Metadata.

---

### C. Metadata (most important copy-paste block)

#### 1. Title

**Recommended (also now in `paper.tex`):**

```
Formally Verified Parameter-Free Scalar Engine for Contested Cosmology: Lean 4 and Multi-Prover Certification of Fluid Spacetime Omni-Theory
```

Rules: no ALL CAPS; plain ASCII/TeX-safe; match the PDF title as closely as possible.

#### 2. Authors

```
Damian Arthur Palumbo
```

If affiliation is asked on a separate line / parentheses style:

```
Damian Arthur Palumbo (Independent researcher)
```

No “et al.” No AI tools as co-authors.

#### 3. Abstract

Open `abstract.txt` and paste **the entire file** into the Abstract box.  
(Length is under arXiv’s 1920-character limit.)

Do **not** put the word “Abstract” at the top of the box.

#### 4. Comments (recommended)

Open `comments.txt` and paste:

```
11 pages + references. Source code, Lean 4 formalization, five-prover verification bundle, and contested-sector ledger: https://github.com/dappalumbo91/FSOT-2.1-Lean Public clone is about 0.5 GB. One-command: pip install -r requirements.txt; python scripts/run_publication_verification_bundle.py (matplotlib>=3.8 in requirements as of commit 8a44947). Author clean-clone reproduction: exit 0. Independent claim checker: verify_paper_claims.py. Comments welcome.
```

Tip: leave a **space before the period** after a URL if arXiv glues punctuation into the link.

#### 5. Report-no

Leave **blank** (unless your institution assigns a number — you don’t have one).

#### 6. Category — Primary (required)

```
cs.LO
```

Full name: **Computer Science → Logic in Computer Science**

This matches Lean formalization + multi-prover verification as the spine.

#### 7. Category — Cross-lists (recommended)

Add if the UI allows:

| Cross-list | Why |
|------------|-----|
| **astro-ph.CO** | Contested cosmology / H₀ readouts |
| **math.LO** (optional) | Formal methods adjacent |

You can ship **cs.LO only** if endorsement for astro is hard; the paper still stands.

#### 8. Journal-ref / DOI

Leave **blank** (preprint not yet journal-published).

#### 9. ACM-class (cs archive, optional)

If the form offers ACM class, a reasonable entry:

```
F.3.1; F.4.1
```

(F.3.1 Specifying and Verifying and Reasoning about Programs; F.4.1 Mathematical Logic)

Optional — skip if unsure.

#### 10. MSC-class

Skip (not a pure math archive primary).

---

### D. Final review page

Check this list on the confirmation screen:

- [ ] Title matches recommended wording  
- [ ] Author name correct  
- [ ] Abstract complete (3 paragraphs)  
- [ ] Comments include GitHub URL  
- [ ] Primary = **cs.LO**  
- [ ] Preview PDF has figures and bibliography  
- [ ] License accepted  
- [ ] You are listed as author/owner  

Then click **Submit** / **Submit and freeze** (wording varies).

---

### E. After submission

| When | What happens |
|------|----------------|
| Same day | Submission held for moderation |
| Next announcement slot | Appears on arXiv if accepted (often next business day depending on deadline) |
| If rejected / delayed | Read moderator email; common fixes: category, title claim, incomplete refs |

**After it is public:**

1. Put the arXiv ID in the GitHub README (e.g. `arXiv:XXXX.XXXXX`).  
2. Optionally create a GitHub Release notes pointing at the arXiv abstract.  
3. Do **not** rewrite claim numbers without a new freeze.

---

## Title decision (last pass)

| Option | Tone | Use when |
|--------|------|----------|
| **Recommended** “…for Contested Cosmology…” | Confident, not overclaiming | Default for first paper |
| Safer Lean-first | cs.LO pure | If you want to de-emphasize cosmology in the title |
| Original “…Resolving…” | Aggressive | Only if you accept more pushback |

**Recommendation:** use the **Recommended** title (already applied in `paper.tex`).  
The abstract still says contested 0.030% and PRED-001 between anchors — that is the scientific claim, without the title saying the tension is “resolved.”

---

## What I will not do

- Log into arXiv as you  
- Drive Chrome to click through CAPTCHA / Google OAuth  
- Submit on your behalf  

Those steps must be yours so the license and authorship are valid.

---

## Quick “day of” checklist

1. [ ] Rebuild/preview local `paper.pdf` if you changed title (optional)  
2. [ ] Upload `arxiv_source_v1.zip`  
3. [ ] Paste title (recommended)  
4. [ ] Paste abstract from `abstract.txt`  
5. [ ] Paste comments from `comments.txt`  
6. [ ] Primary `cs.LO` + optional `astro-ph.CO`  
7. [ ] Preview PDF on arXiv  
8. [ ] Submit  
