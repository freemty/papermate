---
name: paper-writing-qa
description: >
  Use when drafting, revising, or polishing paper sections. Also use proactively
  after generating any LaTeX text, when user says 'check writing', 'polish',
  'review the text', 'AI味', or when overclaiming/filler/missing-citations suspected.
---

# Paper Writing QA

Audit a paper section for writing quality. Focuses on **how** things are written (language, flow, citations, formalization), not scientific correctness.

## When to Use

- After drafting or revising any section
- When user says "review the writing", "check this section", "polish", "去AI味"
- Proactively after generating paper text (>200 words of prose)

## Audit Procedure

Read the target section(s), then check against all criteria below. Report findings as a structured list with severity (Critical / Important / Minor) and specific line-level fixes.

---

## 1. Language Quality (AI-Flavor Detection)

### 1.1 Overclaiming

Flag any of these patterns:
- "systematic/comprehensive/extensive" + noun (let data speak for itself)
- "novel/first/unique" (reviewer decides novelty)
- "demonstrates/reveals/establishes" (use "shows/finds/suggests")
- "fundamental/crucial/remarkable/striking" (empty intensifiers)
- "pervasive/universal" without qualifying exceptions
- "a unified theory/framework" (unless truly unified)

**Fix**: replace with concrete, hedged alternatives. "We study X across Y models" > "systematic empirical characterization".

### 1.2 Complex Vocabulary

Flag words that have simpler equivalents:
- characterization → study/analysis
- elucidate → explain
- facilitate → help/enable
- utilize → use
- leverage → use/exploit
- encompasses → covers/includes
- delineate → describe
- substantiate → support

**Rule**: if you wouldn't use the word in a talk, don't use it in the paper.

### 1.3 Em-dash Abuse

- Flag any paragraph with 2+ em-dashes (`---`)
- Flag em-dashes used for parenthetical insertions (use commas or parentheses instead)
- Em-dashes are a high-frequency AI writing marker

### 1.4 Filler Transitions

Flag and suggest removal:
- "Furthermore" / "Moreover" → just start the sentence
- "It is worth noting that..." → delete, state the fact
- "In light of the above..." → delete
- "Building upon these observations..." → delete
- "Taken together..." → delete or rewrite as a concrete conclusion

---

## 2. Flow and Self-Containedness

### 2.1 Section Intros

Every section/subsection should open with **motivation before method**:
- Why are we asking this question?
- What is different about our setting vs. prior work?
- Then: how we answer it

**Bad**: "We begin with a systematic empirical characterization..."
**Good**: "Unlike LLMs, DiTs have iterative denoising. Whether sinks exist in this setting is not obvious."

### 2.2 Reader Readiness

Check: after reading Section N, is the reader equipped to understand Section N+1?
- All symbols used in Section N+1 should be defined by end of Section N
- Forward references to undefined terms are disallowed
- If a concept is used before its definition section, inline a one-sentence explanation

### 2.3 Self-Invented Terminology

- Any new term MUST have a one-sentence in-place explanation on first use
- Do NOT introduce a term and forward-ref to a later section as the only explanation
- Prefer existing terminology from the field; only coin new terms when necessary

### 2.4 Paragraph Coherence

Each paragraph should:
- Have ONE point
- Start with a topic sentence stating that point
- End with a takeaway or transition
- NOT start with meta-commentary ("In this paragraph we discuss...")

---

## 3. Citation Completeness

### 3.1 Mandatory Citation Points

Flag missing citations at:
- First mention of any named model (DiT, FLUX.1, PixArt, etc.)
- First mention of any technique (RoPE, QK-Norm, attention sink, etc.)
- Any claim about prior work ("In LLMs, certain tokens absorb..." needs cite)
- Any quantitative claim from another paper

### 3.2 "Many/Several/Various" Without Specifics

Flag vague quantifiers:
- "many models show..." → which models? cite them or say "X of Y models"
- "several prior works..." → cite them
- "various architectures..." → list them

### 3.3 First-Occurrence Rule

The first time a key concept appears in the paper body (not abstract), it needs:
- A brief definition or description (1 sentence)
- A citation to the originating work

---

## 4. Formalization Quality

### 4.1 Key Concepts Need Equations

Flag important concepts defined only in prose:
- If a metric is used throughout the paper, it needs a numbered equation
- Definitions should include all relevant dimensions (layer $l$, head $h$, step $t$)

### 4.2 Equation Hygiene

- Every equation should be followed by a one-sentence intuition
- Notation must be consistent across sections
- Superscripts/subscripts should cover all axes the concept varies over

### 4.3 Symbol Introduction

- Symbols must be defined before or immediately at first use
- Don't drop a symbol in an equation and explain it 3 lines later
- Format: "Let $X$ be [definition]." then equation.

---

## 5. Structural Checks

### 5.1 Subsection-Figure Alignment

- Each subsection should have at most one primary figure
- Text should appear before the figure it references
- If two paragraphs both cite the same figure, they likely belong in the same subsection

### 5.2 Paragraph Naming

- Descriptive titles: "Across denoising steps" not "Temporal Invariance Across Denoising Steps"
- Don't put conclusions in titles (overclaiming)
- Titles should tell what axis/dimension is being analyzed

---

## Output Format

```
## Writing QA Report: [Section Name]

### Critical
- [Line X]: [issue description] → [specific fix]

### Important
- [Line X]: [issue description] → [specific fix]

### Minor
- [Line X]: [issue description] → [specific fix]

### Summary
- AI-flavor score: X/10 (0 = no issues, 10 = pure AI slop)
- Flow score: X/10 (0 = perfect, 10 = unreadable)
- Citation completeness: X/10 (0 = all cited, 10 = many missing)
- Overall: [Pass / Needs revision / Major rewrite needed]
```
