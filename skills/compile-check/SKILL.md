---
name: compile-check
description: >
  Use after LaTeX compilation to check for warnings and errors. Also use when
  user says 'compile', 'check build', 'any warnings', or proactively after
  latexmk/pdflatex completes.
---

# Compile Check

Post-compilation audit of LaTeX build. Catches undefined references, float issues, and overfull boxes before they become submission problems.

## When to Use

- After any `latexmk` / `pdflatex` / `xelatex` run
- When user says "compile the paper", "any build warnings"
- Proactively after paper edits that might break references

## Procedure

### Step 1: Run compilation (if not already done)

```bash
cd <paper_dir> && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tee /tmp/latex-build.log
```

### Step 2: Parse log for issues

Check `main.log` (or build output) for:

#### Critical (blocks submission)
- `Undefined control sequence`
- `Missing $ inserted`
- `File not found` / `cannot find image file`
- `Fatal error occurred`

#### Important (reviewers will notice)
- `Reference .* undefined` — broken `\ref{}`
- `Citation .* undefined` — missing bib entry
- `Float too large for page` — figure overflows
- `Label .* multiply defined` — duplicate labels

#### Minor (polish)
- `Overfull \\hbox` > 10pt — text overflows margin
- `Underfull \\hbox` with badness > 5000 — ugly spacing
- Float warnings (figure too far from reference point)
- `Package hyperref Warning` — broken hyperlinks

### Step 3: Cross-check references

```bash
grep -n '\\ref{' main.tex | sed 's/.*\\ref{\([^}]*\)}.*/\1/' | sort -u > /tmp/refs-used.txt
grep -n '\\label{' main.tex | sed 's/.*\\label{\([^}]*\)}.*/\1/' | sort -u > /tmp/labels-defined.txt
comm -23 /tmp/refs-used.txt /tmp/labels-defined.txt  # orphan refs
```

### Step 4: Check figure files exist

```bash
grep -h '\\includegraphics' *.tex | sed 's/.*{\([^}]*\)}.*/\1/' | while read f; do
  [ -f "$f" ] || [ -f "${f}.pdf" ] || [ -f "${f}.png" ] || echo "MISSING: $f"
done
```

## Output Format

```
## Compile Check Report

### Critical
- [issue]: [file:line] → [fix]

### Important
- [issue]: [file:line] → [fix]

### Minor
- [count] overfull hboxes (worst: Xpt at line Y)
- [count] underfull hboxes

### Reference Integrity
- Labels defined: N
- Refs used: M
- Orphan refs: [list]
- Missing figures: [list]

### Verdict: [Clean build / Has issues]
```
