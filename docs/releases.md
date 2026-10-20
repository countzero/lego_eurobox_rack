# Releases

Read when cutting, publishing or verifying a release.

## Order of operations

| Step | What                                                              | Where                                               |
| ---- | ----------------------------------------------------------------- | --------------------------------------------------- |
| 1    | On `develop`, commit `Release vX.Y.Z`: the `CHANGELOG.md` section | *Version*, *Changelog*                              |
| 2    | Open the pull request `Release vX.Y.Z` from `develop` into `main` | `docs/conventions.md` → *Pull request descriptions* |
| 3    | Merge it with a merge commit                                      | `docs/conventions.md` → *Steps and version control* |
| 4    | Publish from the merge commit                                     | *Publishing*                                        |
| 5    | Bring `main` back into `develop` and push it                      | *Back into develop*                                 |
| 6    | Verify                                                            | *Verify*                                            |

Release commits and pull requests carry no `[NNNN]` prefix: no step owns them.

## Version

What a builder relies on is the version's interface: the dimensions in
`design/rack.json`, the part IDs and the files of the parts list. Before 1.0.0,
a change to a dimension or a part raises the minor version, a fix to a
document or a render alone the patch. 1.0.0 is the first release whose box
dimensions are measured (roadmap 0004). From 1.0.0 on, a change that makes
already bought parts or an already built rack incompatible raises the major
version.

## Changelog

`CHANGELOG.md` follows [Common Changelog](https://common-changelog.org). The
choices it leaves open:

- **Written only in the release commit.** No *Unreleased* section: a step's
  pull request does not touch it.
- **One line per merged step** since the previous tag. The merges are listed by
  `git log --merges --first-parent --format='%s' v<previous>..develop`; for the
  first release, `develop` alone.
- **References:** the pull request as a link. No author names.
- **Left out:** what reaches no builder: agent rules, conventions, the
  roadmap.
- **A notice** when a builder has to act, such as a dimension that changes an
  already cut part.

## Publishing

The tag names the merge commit of the release pull request. Pass its SHA to
`--target`, not `main`, which can move before the publish. The release is named
`vX.Y.Z`, and its body is two links:

```markdown
- [Changelog](https://github.com/countzero/lego_eurobox_rack/blob/main/CHANGELOG.md#<anchor>)
- [Code Changes](https://github.com/countzero/lego_eurobox_rack/compare/v<previous>...vX.Y.Z)
```

The anchor is GitHub's slug of the heading: `## [0.1.0] - 2026-10-20` becomes
`#010---2026-10-20`. The first release has no compare link.

```powershell
git fetch origin
git log --max-count=1 --format='%h %s' origin/main   # the release pull request's merge commit
gh release create vX.Y.Z --target (git rev-parse origin/main) --title vX.Y.Z --notes-file <file>
```

The notes file goes under `.tmp/sessions/<session-id>/`. Publish neither a
draft, which creates no tag, nor a prerelease, which `/releases/latest` skips.

The push to `main` also starts the Pages workflow (roadmap 0009), which
publishes the web viewer of the released state.

## Back into develop

The merge commit exists only on `main`. In the main working tree, on
`develop`: `git merge --ff-only origin/main`, or `git merge origin/main` when
`develop` has moved on, then `git push origin develop`.

## Verify

| Check                                     | Command                                                           |
| ----------------------------------------- | ----------------------------------------------------------------- |
| The tag is on the merge commit            | `git fetch --tags; git log --max-count=1 --format='%h %s' vX.Y.Z` |
| Neither a draft nor a prerelease          | `gh release view vX.Y.Z --json isDraft,isPrerelease`              |
| It is what `/releases/latest` serves      | `gh release view --json tagName`                                  |
| The changelog anchor lands on the heading | Open the release's Changelog link                                 |
| The web viewer is deployed                | `gh run list --workflow pages.yml --branch main --limit 1`        |
| The website opens the viewer              | Open `https://countzero.github.io/lego_eurobox_rack/`             |
| `develop` contains every commit of `main` | `git rev-list --count origin/develop..origin/main` answers `0`    |
