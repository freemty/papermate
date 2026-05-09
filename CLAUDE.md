# PaperMate

> Paper writing harness for Claude Code — from figures to submission-ready manuscripts.

Companion to [labmate](https://github.com/freemty/labmate). Labmate handles research (experiments, analysis, literature); PaperMate handles writing (text quality, figures, compilation, sync, submission).

## Quick commands

| Command | Purpose |
|---------|---------|
| `/paper-writing-qa` | Audit text for AI flavor, flow, citations |
| `/figure-qa` | Check figure publication readiness |
| `/compile-check` | Post-compilation warning audit |
| `/sync-paper` | One-command paper submodule sync |
| `/section-guard` | Detect broken refs after restructuring |
| `/pre-submit-challenge` | Adversarial final-pass before submission |

## Plugin architecture

| Component | Location | Auto-loaded |
|-----------|----------|-------------|
| Agents (1) | agents/ | Yes (plugin.json) |
| Skills (6) | skills/ | Yes (plugin.json) |
| Hooks (5) | hooks/ | Yes (hooks.json) |

## Hooks (auto-triggers)

| Hook | Trigger | Action |
|------|---------|--------|
| post-plot-figure-qa | Python plot script succeeds | Remind `/figure-qa` |
| post-compile-check | latexmk/pdflatex completes | Report undefined refs, missing figs |
| post-tex-edit-sync-remind | 5+ uncommitted paper changes | Remind `/sync-paper` |
| post-section-change-guard | `\section`/`\label` edits | Remind `/section-guard` |
| post-writing-qa-remind | 100+ words of prose written | Remind `/paper-writing-qa` |

## Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| writing-reviewer | opus | Deep writing quality review — AI flavor, flow, citations |

## Relationship to labmate

```
labmate (upstream)          papermate (downstream)
─────────────────           ────────────────────
/new-experiment      →      /figure-qa (results → figures)
/analyze-experiment  →      /compile-check (figures → paper)
/monitor             →      /sync-paper (paper → overleaf)
/read-paper          →      /paper-writing-qa (text quality)
/update-knowhow     →      /section-guard (structure integrity)
                            /pre-submit-challenge (final gate)
```
