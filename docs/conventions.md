# Conventions

Read when naming anything, writing a commit or a pull request, or citing a
fact.

## Steps and version control

A roadmap step is the unit of work. Its ID ties the branch, the worktree, the
commits and the pull request together.

| Where             | Format                        | Example                                 |
| ----------------- | ----------------------------- | --------------------------------------- |
| Branch            | `feature/NNNN`                | `feature/0003`                          |
| Worktree          | `.worktrees/NNNN/`            | `.worktrees/0003/`                      |
| Commit and PR     | `[NNNN] <imperative subject>` | `[0003] Build the frame from rack.json` |
| Work with no step | No prefix                     | `Fix a typo in the README`              |

- **Numbering.** A step takes the ID of its row in the roadmap. Work the
  roadmap does not list yet first gets a row there with the next free ID.
- **One purpose.** A step is statable in one sentence and writes only the files
  its *Delivers* names. A step that finds a needed change elsewhere says so in
  its pull request instead of making it.
- **Branches.**

  | Branch         | What it holds          | How it changes                                           |
  | -------------- | ---------------------- | -------------------------------------------------------- |
  | `feature/NNNN` | One step               | Commits `[NNNN] …`; deleted after its merge              |
  | `develop`      | Every finished step    | A step's pull request, or a direct commit no step owns   |
  | `main`         | What has been released | Only a release pull request from `develop`; never a push |

- **Merge commits only.** The repository allows nothing else, so `main` and
  `develop` never drift apart. Automatic deletion of head branches stays off,
  because it would delete `develop` after a release.
- **After the merge** remove the worktree (`docs/worktrees.md` → *Cleanup*),
  then `git push origin --delete feature/NNNN` and `git branch -d feature/NNNN`.
  Never force a deletion with `-D`.

## Commit messages

- The subject is imperative, starts with a capital letter, has no trailing
  period, and follows the `[NNNN] ` prefix where a step owns the work.
- A body, after a blank line, says **why**, the measurement behind a changed
  dimension, and what was left undone.
- No `Co-Authored-By` trailer.
- Commit and push only on the user's explicit request.

## Pull request descriptions

The title carries the `[NNNN]` prefix. The body answers, all of them
mandatory:

- **What** changed, specifically enough to skim.
- **Why**, including the decisions the diff cannot show.
- **The shortcomings** of the approach.
- **Which feedback** you want, and on what.
- **What is not done**: an unrun check, a deferred step, a follow-up.

## Sources

Every dimension, price and product property cites an entry in
`docs/sources.md`, which gives its status and URL:

| Status       | Meaning                                                            |
| ------------ | ------------------------------------------------------------------ |
| `VERIFIED`   | Read on the maker's or the seller's own page, datasheet or drawing |
| `MEASURED`   | Measured on a real part, by us or in a named public source         |
| `SECONDARY`  | Only in a search snippet, a reseller listing or a forum post       |
| `DERIVED`    | Calculated from verified values; the calculation is stated         |
| `UNVERIFIED` | An estimate or an inference; never presented as a fact             |

A price states whether it includes VAT and the date it was read. A net price
is converted with 19 % VAT and marked `DERIVED`.

## Units and numbers

Millimetres throughout, without a unit in `design/rack.json` and with `mm` in
prose. Euro prices with two decimals and a comma-free point, such as
`12.55 €`. A range uses an en dash: `396–405 mm`.

## Naming and language

Everything is English: folders, files, identifiers, JSON keys, documents. A
German product or shop name stays as the maker writes it, such as
„Hammermutter“ or „Einsatzkasten“, with the English term in brackets at its
first use in a document. Files and folders are lowercase with underscores;
part IDs are lowercase and dotted (`profile.upright`).

## Punctuation

The em dash is reserved for interrupted dialogue and a genuine break in the
flow of thought. Everywhere else, use the specific mark: paired commas for a
short aside, parentheses for a tangential one, a colon to introduce an
explanation or list, a semicolon or a full stop between related clauses, an
en dash for a range, and a hyphen for a compound modifier.
