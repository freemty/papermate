# PaperMate

Version 0.2.0. Six portable paper-writing skills and one Claude named reviewer.
The same role can run in an ordinary subagent or the main thread.

Skills: compile-check, figure-qa, paper-writing-qa, section-guard, sync-paper and
pre-submit-challenge. Invoke through the host's skill selector. Claude plugin
syntax is `/papermate:<skill>`; Codex plugin syntax is `$papermate:<skill>`.

Only one default hook remains: current compiler-output diagnostics after a
recognized compilation command. It reports actual undefined references, missing
assets and overfull boxes; it does not read an unrelated stale log or recommend
other skills after ordinary edits. This is feedback, not a permission gate.

Paper synchronization requires the matching commit/push intent and exact nested
repository/remotes. Read-only review does not authorize edits or publication.
Inspect figures/layout when those properties matter; model role counts, reviewer
scores and full QA suites are not universal completion requirements.

`python3 tests/test_compile_feedback.py` covers Claude/Codex payloads, unrelated
events, clean output and failures. Real host hook invocation is a separate check.
