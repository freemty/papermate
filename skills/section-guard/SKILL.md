---
name: section-guard
description: >
  Use after restructuring paper sections (renaming, merging, splitting, reordering).
  Also use when user says 'check refs', 'any broken references', 'section变了检查一下',
  or proactively after detecting \section or \label changes in .tex files.
---

# Section Guard

Detect broken cross-references after paper restructuring. Catches orphan `\ref{}`, stale `\label{}`, and documentation drift.

## When to Use

- After renaming, merging, or splitting sections
- After moving figures between main paper and supplementary
- When user says "check refs", "did I break anything"
- Proactively after detecting `\section` or `\label` edits

## Procedure

### Step 1: Collect all labels and refs

```bash
# All labels defined
grep -rn '\\label{' *.tex supplementary.tex appendix.tex 2>/dev/null | \
  sed 's/.*\\label{\([^}]*\)}.*/\1/' | sort -u > /tmp/labels.txt

# All refs used
grep -rn '\\ref{' *.tex supplementary.tex appendix.tex 2>/dev/null | \
  sed 's/.*\\ref{\([^}]*\)}.*/\1/' | sort -u > /tmp/refs.txt

# Also check \cref, \autoref, \eqref
grep -rn '\\[a-z]*ref{' *.tex 2>/dev/null | \
  sed 's/.*\\[a-z]*ref{\([^}]*\)}.*/\1/' | sort -u >> /tmp/refs.txt
sort -u -o /tmp/refs.txt /tmp/refs.txt
```

### Step 2: Find orphans

```bash
# Refs that have no matching label
comm -23 /tmp/refs.txt /tmp/labels.txt

# Labels that are never referenced (potential dead labels)
comm -23 /tmp/labels.txt /tmp/refs.txt
```

### Step 3: Check figure references

```bash
# All \includegraphics paths
grep -rhn '\\includegraphics' *.tex 2>/dev/null | \
  sed 's/.*{\([^}]*\)}.*/\1/' | while read f; do
    [ -f "$f" ] || [ -f "${f}.pdf" ] || [ -f "${f}.png" ] || echo "MISSING: $f"
  done
```

### Step 4: Check section ordering consistency

- Read `\section` order from main.tex
- Verify that forward references don't point to later-defined labels (anti-pattern)
- Check if CLAUDE.md figure inventory is stale compared to actual `\label{fig:}`

### Step 5: Report

```
## Section Guard Report

### Broken References (refs without labels)
- \ref{fig:xxx} at main.tex:42 — label not found

### Dead Labels (labels never referenced)
- \label{sec:old_name} at main.tex:88 — consider removing

### Missing Figures
- gfx/old_figure.pdf — referenced but file not found

### Documentation Drift
- CLAUDE.md lists fig:xxx but paper no longer has it

### Verdict: [Clean / N issues found]
```
