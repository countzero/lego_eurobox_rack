# Web viewer

The web viewer shows the rack in 3D in the browser. It is one self-contained
file, `web/dist/index.html`, that opens by double-click and makes no network
request. The published copy is at
<https://countzero.github.io/lego_eurobox_rack/>.

## What it does

- Orbit, pan and zoom with mouse or touch (three.js `OrbitControls`).
- Buttons for the Front, Side, Top and Three-quarter views and Reset.
- A click or tap on one of the 15 boxes pulls it out; a second click pushes it
  back. The inserts and the ColorClip rings move with the box. "All out" pulls
  out every box, "All in" pushes every box back.
- "Top plate" hides or shows the planned top plate, which is shown by
  default. The rack has no panels, so the inside is always visible.
- On a pointer device, hovering a box highlights it and names it with its
  ColorClip colour, for example "L3 C2, 120 mm class, Purpur".
- The info line shows the rack's outer size from the model.
- "Colours" shows or hides the ColorClips panel (*ColorClips* below), open by
  default except on a narrow screen.

## ColorClips

The panel picks the ColorClip colour of each level; all three boxes of a level
take it, on both handles.

- One row per level, L5 at the top, each with the nine colours aidB sells as
  swatches (`rack.json` → `color_clips.colours`).
- "Current" sets the colours of `color_clips.levels`, the ones the model and
  the parts list use; the five buttons after it set `color_clips.presets`. The
  button whose colours match the choice is highlighted.
- Below the rows: the weakest step between two neighbouring levels of
  different colour (CIEDE2000, marked below 20, where two levels are hard to
  tell apart) and the packs to order per colour with their article numbers.
- The choice lives in the URL fragment, `#clips=<L1>,<L2>,<L3>,<L4>,<L5>` with
  the keys of `color_clips.colours`, for example
  `#clips=blue,lightgreen,lightgreen,purple,purple`. A pick rewrites the
  fragment without a history entry; a link with a fragment opens with that
  choice, and an edited fragment applies at once. A fragment that names an
  unknown colour or the wrong number of levels is ignored, and the panel
  starts at "Current". The fragment never leaves the browser, so the link
  works on GitHub Pages and offline alike.
- The picker only previews: it changes neither `rack.json` nor the model. The
  screen colours are read from aidB's photos (`UNVERIFIED`), so the real rings
  may differ.

## Building

```powershell
npm --prefix web ci
npm --prefix web run build   # writes web/dist/index.html
npm --prefix web run watch   # rebuilds on every change to web/src or the model
```

`web/build.mjs` bundles three.js, `web/src/main.js` and the model with esbuild
into `web/dist/index.html`. `web/src/clips.js` imports `color_clips`,
`levels`, `inserts` and `frame` from `design/rack.json`, which esbuild inlines,
so a change there needs a rebuild:

- The model is inlined deflated (`deflate-raw` from `node:zlib`); the browser
  unpacks it with `DecompressionStream` before `GLTFLoader.parse`.
- The favicon is inlined as a data URI.
- The licence of three.js goes into an HTML comment.
- A literal `</script` in the bundle is escaped.

The model is `web/rack.glb`, exported by `blender/build_rack.py` (step 0003).
The build stops with a message if it is missing. The environment variable
`RACK_GLB` points the build at another file, for example a stand-in model:

```powershell
$env:RACK_GLB = 'D:\path\to\standin.glb'
npm --prefix web run build
Remove-Item env:RACK_GLB
```

## The model contract

The viewer relies only on the node names and extras of `docs/design.md` →
*Contracts* → *Model objects and the web export*:

| Read from                  | Used for                                    |
| -------------------------- | ------------------------------------------- |
| `kind: "box"`              | the clickable boxes                         |
| `level`, `column`, `class` | the hover label                             |
| `travel`, `pull_axis`      | how far and in which direction a box moves  |
| `kind: "plate"`            | the "Top plate" toggle, shown at the start  |
| `kind: "clip"`             | the rings the ColorClips panel recolours    |
| scene extras `outer_mm`    | the info line                               |

The inserts and the ColorClip rings are children of their box node, so moving
the box node moves them too. The viewer clones the materials under every box,
so recolouring the rings of one level leaves the other levels alone. A change to these names or extras needs a change
to `web/src/main.js`.

## Publishing

`.github/workflows/pages.yml` runs on every push to `main`, which happens at
every release (`docs/releases.md`), and on demand. It runs `npm ci` and
`npm run build` in `web/` with the committed `web/rack.glb` (Blender does not
run in CI) and deploys `web/dist` to GitHub Pages through the `github-pages`
environment, which accepts only `main`.

## Browser requirement

The viewer needs WebGL and `DecompressionStream` with the `deflate-raw`
format: Chrome and Edge 103 or later, Firefox 113 or later, Safari 16.4 or
later.
