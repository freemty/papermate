---
name: figure-qa
description: >
  Use after generating or modifying paper figures. Also use when user says
  'check the figure', 'figure QA', 'is this plot ok', or proactively after
  any matplotlib/plot script completes successfully.
---

# Figure QA

Audit a generated figure against publication standards. Catches issues that cause reviewer complaints or post-acceptance embarrassment.

## When to Use

- After running a plot script that generates PDF/PNG for the paper
- When user asks "is this figure ok", "check the plot"
- Proactively when a figure is about to be committed to the paper

## Checklist

### 1. Resolution & Format
- [ ] DPI ≥ 300 (for raster); vector PDF preferred
- [ ] No JPEG artifacts (use PNG for raster, PDF for vector)
- [ ] File size reasonable (<5MB per figure)

### 2. Text Readability
- [ ] Font size ≥ 8pt at final print size (single-column ~3.25in, double ~6.5in)
- [ ] Axis labels present and readable
- [ ] Title/caption not cut off by tight_layout
- [ ] No overlapping tick labels (rotate or subsample if needed)
- [ ] Legend doesn't obscure data

### 3. Color & Style
- [ ] Colorblind-safe palette (no red-green only distinction)
- [ ] Consistent with paper's color scheme (check project palette if defined)
- [ ] White background (no gray matplotlib default)
- [ ] Grid lines subtle or absent (not distracting)

### 4. Data Integrity
- [ ] Axis ranges appropriate (no misleading truncation)
- [ ] Units labeled on axes
- [ ] Error bars / confidence intervals where applicable
- [ ] No data accidentally clipped by axis limits

### 5. Layout
- [ ] Subfigures aligned (same height, consistent spacing)
- [ ] Panel labels (a), (b), (c) present and consistent style
- [ ] Caption describes what to observe, not just what the plot shows
- [ ] Figure width matches target column width

### 6. LaTeX Integration
- [ ] `\includegraphics` path matches actual file location
- [ ] Figure placement won't cause float issues (check if [H] or FloatBarrier needed)
- [ ] `\label{fig:xxx}` present and matches `\ref{fig:xxx}` in text

## Output Format

```
## Figure QA: [filename]

### Issues
- [severity]: [issue] → [fix]

### Pass/Fail
- Resolution: ✓/✗
- Readability: ✓/✗
- Color: ✓/✗
- Data: ✓/✗
- Layout: ✓/✗
- LaTeX: ✓/✗

### Verdict: [Ready / Needs fixes]
```
