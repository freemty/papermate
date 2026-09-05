---
name: sync-paper
description: >
  Use when paper submodule has uncommitted changes, after editing .tex files,
  or when user says 'sync paper', 'push to overleaf', 'update submodule',
  'paper同步'. Handles the full commit-submodule-push cycle.
---

# Sync Paper

Resolve the paper repository, requested remotes and parent gitlink. Inspect both
worktrees and recent commits; preserve unrelated edits. A .tex edit alone does
not authorize committing or publishing.

For a requested sync, review the relevant paper diff, verify the changed artifact,
stage explicit files and commit inside the paper repository first. Then stage only
its gitlink and relevant requested parent changes. If the paper is clean, check
whether the parent pointer or requested remote still needs synchronization.

Push only to destinations included in the user's request. Existing origin/Overleaf
remotes are not automatic publication permission; verify the destination branch
rather than assuming master. Report inner and outer hashes, actual pushed remotes
or local-only state, and remaining differences. Do not use blanket staging.
