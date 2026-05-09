# AI-Flavor Anti-Patterns Reference

Quick-lookup table for the writing-reviewer agent and /paper-writing-qa skill.

## Overclaiming Words → Replacements

| AI Pattern | Fix |
|------------|-----|
| systematic | (delete, or use "across N models") |
| comprehensive | thorough, detailed |
| extensive | (delete, let scope speak for itself) |
| novel | (delete — reviewer decides) |
| first | (delete unless provably true) |
| unique | distinctive, unusual |
| demonstrates | shows, finds |
| reveals | shows, finds, exposes |
| establishes | shows, supports |
| fundamental | (delete) |
| crucial | important, key |
| remarkable | notable, surprising |
| striking | clear, notable |
| pervasive | widespread, common |
| universal | (add "across X" qualifier) |
| paradigm shift | (delete) |
| groundbreaking | (delete) |

## Complex Vocabulary → Simple

| Avoid | Use |
|-------|-----|
| characterization | study, analysis |
| elucidate | explain, clarify |
| facilitate | help, enable |
| utilize | use |
| leverage | use, exploit |
| encompasses | covers, includes |
| delineate | describe, outline |
| substantiate | support, confirm |
| ameliorate | improve |
| aforementioned | this, the |
| endeavor | try, attempt |
| commence | start, begin |
| terminate | end, stop |
| subsequent | next, later |
| prior to | before |
| in order to | to |
| due to the fact that | because |

## Filler Transitions (delete entirely)

- Furthermore,
- Moreover,
- It is worth noting that
- In light of the above,
- Building upon these observations,
- Taken together,
- It should be noted that
- As previously mentioned,
- In this context,
- Along these lines,

## Em-dash Rules

- Max 1 per paragraph
- Never for parenthetical insertions (use commas or parens)
- OK for dramatic breaks in narrative: "The answer — surprisingly — was no."
- Not OK for lists or definitions: "The model — a 12B parameter DiT — uses..."

## Sentence-Start Patterns to Avoid

- "We observe that..." (just state the observation)
- "It can be seen that..." (delete, state the fact)
- "Interestingly,..." (let the reader decide what's interesting)
- "Notably,..." (same)
- "Importantly,..." (same)
- "To this end,..." (delete or rewrite)

## Section Intro Anti-Pattern

**Bad** (method-first):
> "We conduct a systematic empirical study of attention distributions across 12 diffusion transformer architectures."

**Good** (motivation-first):
> "Whether attention sinks exist outside of LLMs remains unknown. DiTs have a fundamentally different architecture: no causal mask, iterative denoising, and positional encoding instead of token order. We test this across 6 models."

## Abstract Anti-Pattern

**Bad** (vague + overclaiming):
> "We present a comprehensive study that reveals fundamental properties of attention in diffusion transformers, demonstrating striking phenomena..."

**Good** (specific + hedged):
> "We find that diffusion transformers allocate >30% of attention mass to the first text token regardless of content. This 'sink' pattern appears in 5 of 6 tested architectures and persists across all denoising steps."
