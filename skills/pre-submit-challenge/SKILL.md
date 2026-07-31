---
name: pre-submit-challenge
description: Use when a paper is at its final pre-submission gate and needs an adversarial code-evidence consistency review.
---

# Pre-Submit Challenge

Adversarial final-pass before submission. Tries to break the paper's claims by finding code-paper mismatches, unreported failure cases, and logical gaps.

## When to Use

- Right before submitting to a venue (NeurIPS, ICML, ICLR, etc.)
- When user says "ready to submit?", "pre-submit check", "challenge this"
- After all other QA skills have passed

## Procedure

### Phase 1: Code-Paper Alignment

Verify that paper claims match what the code actually does:

1. **Metric definitions**: Does the code compute exactly what the paper equation says?
2. **Experiment configs**: Do reported hyperparameters match config files?
3. **Model list**: Are all models claimed in the paper actually tested?
4. **Numbers**: Do reported numbers match output logs? (spot-check 3-5 key results)

### Phase 2: Adversarial Review

Think like a hostile reviewer:

1. **Missing baselines**: What obvious comparison is missing?
2. **Cherry-picking**: Are results selectively shown? What does the worst case look like?
3. **Overclaiming**: Does the conclusion overstate what the evidence supports?
4. **Reproducibility**: Can someone replicate this with the information given?
5. **Statistical significance**: Are differences meaningful or within noise?

### Phase 3: Structural Completeness

1. **Abstract**: Does it match the actual content? (not stale from earlier draft)
2. **Contributions**: Are claimed contributions actually delivered in the paper?
3. **Figures**: Does every figure serve the narrative? Any redundant ones?
4. **Supplementary**: Is anything promised in main text but missing from appendix?
5. **References**: Any placeholder citations? Any self-citations that should be anonymized?

### Phase 4: Independent Challenge (Optional)

When the host supports an independent read-only reviewer, ask it to find three
concrete code-paper contradictions or unsupported claims with line-level
evidence. The main thread verifies every finding before merging it into the
report. If independent review is unavailable, perform the same pass directly.

## Output Format

```
## Pre-Submit Challenge Report

### Code-Paper Mismatches
- [severity]: [paper claim at line X] vs [code reality at file:line]

### Adversarial Findings
- [severity]: [potential reviewer attack] — [evidence/mitigation]

### Structural Issues
- [severity]: [issue] → [fix]

### Verdict
- Submission-ready: [Yes / No — fix N critical issues first]
- Estimated reviewer score if submitted now: [X/10]
- Top risk: [what's most likely to get the paper rejected]
```
