---
name: sync-paper
description: >
  Use when paper submodule has uncommitted changes, after editing .tex files,
  or when user says 'sync paper', 'push to overleaf', 'update submodule',
  'paper同步'. Handles the full commit-submodule-push cycle.
---

# Sync Paper

One-command paper submodule synchronization. Commits paper changes, updates the parent repo pointer, and optionally pushes to Overleaf.

## When to Use

- After editing `.tex` files in the paper submodule
- When user says "sync", "push paper", "update submodule"
- Proactively when paper/ has uncommitted changes and main repo is about to commit

## Procedure

### Step 1: Detect paper directory

Look for paper submodule:
```bash
git submodule status | grep -i paper
```

If no submodule, check for `paper/` directory with `.git`.

Set `PAPER_DIR` to the paper path.

### Step 2: Check for changes

```bash
cd $PAPER_DIR && git status --short
```

If clean, report "Paper submodule is clean, nothing to sync." and exit.

### Step 3: Commit in paper submodule

```bash
cd $PAPER_DIR
git add -A
git commit -m "<type>: <description>"
```

Commit message rules:
- Infer type from changed files: `.tex` → content change, `.bib` → references, `gfx/` → figures
- Keep message concise: "§4 rewrite + new Fig.5" not "Updated section 4 with new content"

### Step 4: Update parent repo pointer

```bash
cd <parent_repo>
git add $PAPER_DIR
git commit -m "chore: update paper submodule (<summary>)"
```

### Step 5: Push to remotes (if configured)

Check available remotes in paper submodule:
```bash
cd $PAPER_DIR && git remote -v
```

- If `overleaf` remote exists: `git push overleaf HEAD:master`
- If `origin` remote exists: `git push origin`
- Report which remotes were pushed to

### Step 6: Verify

```bash
cd $PAPER_DIR && git status
cd <parent_repo> && git submodule status
```

## Output

```
## Paper Sync Complete

- Paper commit: <hash> "<message>"
- Parent commit: <hash> "chore: update paper submodule (<summary>)"
- Pushed to: [origin, overleaf] / [none — use git push manually]
```
