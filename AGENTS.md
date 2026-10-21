# AGENTS.md

Canonical agent-instruction file for this repository. It carries the always-on
rules; the documents under `docs/` hold the details and are read on demand
through *Reference* at the end.

## Project Overview

A rolling rack of 30 × 30 aluminium profiles for 15 Euroboxes 400 × 300
(NextGen 2.0 Cycle), used as drawers for LEGO: 3 columns, 5 levels, the short
side of each box with its handle at the front, one long bar front and back on
4 castors. The repository holds the specification, the Blender model and its
renders, a web viewer, the parts and cut list, the price comparison and the
assembly guide. Nothing here is built into software; the rack is built by hand.

## Single Source of Truth

- **Every dimension lives in `design/rack.json`.** The Blender script, the parts
  and cut list and the web viewer read it; no other file states a dimension of
  its own. A changed dimension is changed there and everything is generated
  again.
- **Every fact has a status and a source.** A dimension, a price or a product
  property names its status (`VERIFIED`, `MEASURED`, `SECONDARY`, `DERIVED`,
  `UNVERIFIED`) and its URL in `docs/sources.md`
  (`docs/conventions.md` → *Sources*). An unverified value is never presented
  as a fact.
- **The rack accepts NextGen and regular Euroboxes 400 × 300.** A design change that
  narrows the box envelope of `docs/design.md` is refused unless the user
  agrees.

## Privacy

No machine names, local user names, IP addresses, home addresses or paths to a
home folder in any file, commit message or render.

## Scratch Files

Every ad-hoc artifact of an agent session (anything not meant to be committed)
goes under `.tmp/sessions/<session-id>/` in the working tree the session works
in; `.tmp/` is gitignored. `<session-id>` is `$env:OPENCODE_SESSION_ID`, which
OpenCode 2 sets in every shell; run `Write-Output $env:OPENCODE_SESSION_ID`
once when a Write or Edit path needs the literal value. Without it, mint
`YYYYMMDD-HHMMSS-<random6>` once per session. Never write scratch files to the
repository root or the operating system's temp directory.

## Multi-Agent Working Tree Discipline

Several agents may work in this repository at once. Any uncommitted change or
untracked file you did not create in this session belongs to another agent.

1. **Foreign changes are untouchable.** Never run `git checkout --`,
   `git restore --`, `git reset --hard`, `git clean`, `git stash` without a
   pathspec, `rm` or `mv` on a path another agent modified or created.
2. **Preflight.** Run `git status --porcelain -u` at task start and again
   before `git commit`.
3. **Worktrees.** The main working tree holds `develop` and the work no roadmap
   step owns. A step is worked in `.worktrees/<NNNN>/` on `feature/<NNNN>`;
   read `docs/worktrees.md` before creating, using or removing one.
   `git worktree remove --force` and `git worktree prune` are forbidden.
4. **Edit tool and shell writes are mutually exclusive per file.** If an edit
   fails with "oldString not found", re-read the file and tell the user.

When your changes overlap foreign work in the same file, stop and ask.

## Tools

- **Blender runs headless from the command line**, never through a running
  Blender instance, so parallel sessions never share one:

  ```powershell
  $blender = Join-Path (Get-ChildItem "C:\Program Files\Blender Foundation" -Directory |
      Select-Object -Last 1).FullName 'blender.exe'
  & $blender --background --factory-startup --python-exit-code 1 --python blender/build_rack.py
  ```

  The Blender MCP server may inspect a scene but never writes a committed file.
- **The user's Blender window is never closed or relaunched.** It runs
  `blender/live_reload.py`, which reloads `rack.blend` by itself whenever the
  headless build rewrites the file; an agent only rebuilds. If no window is
  open, or the open one does not run the script, the agent asks the user
  instead of starting or killing Blender.
- **The web viewer** builds with `npm --prefix web ci` and
  `npm --prefix web run build` (`docs/web_viewer.md` once 0009 exists).
- **One browser.** Only one session at a time drives the browser.

## Version Control

- Gitflow: `main` holds what is released and changes only through a release pull
  request from `develop`; `develop` holds every finished step; a step is worked
  on `feature/NNNN`, branched from `origin/develop`, and its pull request
  targets `develop`. Pull requests merge with a merge commit, never squashed or
  rebased.
- Commits of a step are prefixed `[NNNN]`; work no step owns carries no prefix.
  The subject is one imperative line; the body says why. No `Co-Authored-By`
  trailer. All text files use LF (`.gitattributes`).
- Commit and push only when the user asks; "commit" does not imply "push".
- Semantic Versioning; `CHANGELOG.md` follows Common Changelog and is written
  only in a release's own commit (`docs/releases.md`).

## Default Change Workflow

Work of more than one step keeps the todo list current, one item in progress
and each ticked off as it finishes.

## Output Formatting

Pad every cell of a markdown table so all cells of a column share one width.
The em dash is reserved for interrupted dialogue and a genuine break in
thought; everywhere else use the specific mark (`docs/conventions.md` →
*Punctuation*).

## Reference

| Document              | When to read                                                                    |
| --------------------- | ------------------------------------------------------------------------------- |
| `docs/roadmap.md`     | Read before starting a step, to see its spec, its status and what blocks it     |
| `docs/conventions.md` | Read when naming anything, writing a commit or a pull request, or citing a fact |
| `docs/sources.md`     | Read when stating a dimension, a price or a product property                    |
| `docs/design.md`      | Read when changing the rack, once 0002 exists                                   |
| `docs/releases.md`    | Read when cutting, publishing or verifying a release                            |
| `docs/worktrees.md`   | Read before creating, using or removing a git worktree                          |
