---
name: pre-submit-challenge
description: >
  Use before paper submission as a final adversarial review. Triggers on
  'pre-submit', 'challenge', 'submission check', 'ready to submit?',
  '提交前检查'. Runs Codex adversarial + internal consistency audit.
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

### Phase 4: Codex Challenge (Optional)

If Codex CLI is available, dispatch adversarial review:

```bash
codex --model o3 --approval-mode full-auto \
  "You are an adversarial reviewer. Read the paper at paper/main.tex and the code at src/. \
   Find 3 concrete issues where the code contradicts the paper, or where claims lack evidence. \
   Be specific — cite line numbers in both code and paper."
```

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
