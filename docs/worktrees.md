# Git Worktree Reference

Read before creating, using or removing a git worktree. The short rule is
`AGENTS.md` → *Multi-Agent Working Tree Discipline*, rule 3.

## Which tree holds what

The main working tree holds `develop` and the work no step owns. Each step
lives in `.worktrees/<NNNN>/` on `feature/<NNNN>`, from its first commit to its
merge, so the main tree never leaves `develop`. A task that writes to a step
moves there without asking:

1. If `.worktrees/NNNN/` exists, use it.
2. Otherwise create it (*Creating the worktree*).
3. Enter it (*Entering it*).

Read-only work stays in the main tree. The user's word on which tree to use
overrides this.

## Location and naming

`.worktrees/<NNNN>/`, one level below the repository root, so absolute paths
stay under the Windows 260-character `MAX_PATH` limit. `.worktrees/` is
gitignored, and `core.longpaths` is set in the untracked `.git/config`.

The worktrees are created with `git worktree add`, not with OpenCode's
`worktree_create` tool, which places them in OpenCode's own data folder outside
the repository.

## Creating the worktree

On a fresh step branch, from a freshly fetched `origin/develop`:

```powershell
git fetch origin
git worktree add --no-track -b feature/NNNN .worktrees/NNNN origin/develop
```

An existing step branch is checked out by name:

```powershell
git worktree add .worktrees/NNNN feature/NNNN
```

The start point is `origin/develop`, so the main tree is never pulled under
another agent. `--no-track` keeps the new branch from tracking
`origin/develop`: a bare `git push` would otherwise be refused, and the
refusal's first suggestion, `git push origin HEAD:develop`, writes the step to
`develop`. The first push is therefore explicit:

```powershell
git push --set-upstream origin feature/NNNN
```

Before it, `git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'` must
not print `origin/develop`.

## Entering it

OpenCode 2 moves a session with its `session_move` tool, which takes the
target directory. The move happens at the next safe boundary, so no tool call
that depends on the new directory runs in the same turn. A session moved into a
worktree reads the branch and runs the preflight again before it writes.
Uncommitted changes never travel with a move. A subagent is given the
worktree's absolute path and passes it as the working directory of every shell
call and as the base of every file path.

## Scratch artifacts

Scratch files go to `.tmp/sessions/<session-id>/` of the tree the session
works in (`AGENTS.md` → *Scratch Files*). Inside a worktree that folder is
deleted with the worktree, so anything worth keeping is committed or moved to
the main tree's `.tmp/` before the cleanup.

## Generated files

`web/node_modules/` and `web/dist/` are per worktree; run
`npm --prefix web ci` in a new one before building the viewer. Blender runs
headless in every worktree at once (`AGENTS.md` → *Tools*), each on its own
files.

## Cleanup

Run `git worktree remove <path>` from the main working tree. It refuses while
the worktree holds uncommitted or untracked changes, which is the point:
commit, or ask the user what is to become of them. Never reach for `--force`
or `git worktree prune`; surface a refusal to the user instead.
