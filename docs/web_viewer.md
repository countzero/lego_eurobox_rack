# Web viewer

The web viewer shows the rack in 3D in the browser. It is one self-contained
file, `web/dist/index.html`, that opens by double-click and makes no network
request. The published copy is at
<https://countzero.github.io/lego_eurobox_rack/>.

## What it does

- Orbit, pan and zoom with mouse or touch (three.js `OrbitControls`).
- Two buttons at the top right: "Reset" returns the view and sets the
  ColorClips back to the current colours of `design/rack.json`; "Colours"
  shows or hides the ColorClips panel (*ColorClips* below), which is hidden at
  the start on every screen.
- Hovering a box shows "Open" or "Close". A click or tap pulls the box out to
  the side that was clicked: on its front half to the front, on its back half
  to the back (the rack is open at the back). A second click pushes it back.
  The inserts and the ColorClip rings move with the box. A model without
  `sides` pulls to the front only.
- The top plate is always shown; there is no toggle. The rack has no
  panels, so the inside is always visible.
- The title line shows the storage volume, the sum of the boxes' nominal
  volumes from `rack.json` → `box_models` → `volume_l`: 12 × 11 l + 3 × 20 l
  = 192 l in 15 boxes.
- The shading is drawn to match Blender's material preview: AgX tone mapping
  and an environment map built in the page from three.js `RoomEnvironment`
  (no file, so it works offline). The plate's plywood is a procedural texture
  computed in the browser from the plate's glTF extras `plywood` (grain and
  ply colours), so it follows the Blender material without an image file.
- The look follows [Web Awesome](https://webawesome.com) (MIT): its default
  theme and native styles are bundled as CSS only, with native buttons and
  Web Awesome classes and tokens and no web components, fonts or icons
  fetched from the network.

## ColorClips

The panel picks the ColorClip colour of each level; all three boxes of a level
take it, on both handles.

- One row per level, L5 at the top, each with the nine colours aidB sells as
  swatches (`rack.json` → `color_clips.colours`), named in English by their
  `name` (for example "Light green"). The order list adds the article number.
- There are no presets; "Reset" sets the colours of `color_clips.levels`, the
  ones the model and the parts list use.
- Below the rows: the weakest step between two neighbouring levels of
  different colour (CIEDE2000, marked below 20, where two levels are hard to
  tell apart) and the packs to order per colour with their article numbers.
- The choice lives in the URL fragment as `#c=` and three base64url characters
  (`A`–`Z`, `a`–`z`, `0`–`9`, `-`, `_`). Each level is its index in
  `Object.keys(color_clips.colours)` (0 to 8); the five indices form one
  base-9 number with L1 as the lowest digit (9⁵ = 59049 < 64³), written
  big-endian in base64url. Example: blue, turquoise, turquoise, purple,
  purple (3, 4, 4, 2, 2) gives 3 + 4·9 + 4·81 + 2·729 + 2·6561 = 14943,
  that is `#c=Dpf`.
- The current colours of `rack.json` write no fragment at all, so a plain
  link and "Reset" show them. Any other pick rewrites the fragment without a
  history entry; a link with a fragment opens with that choice, and an edited
  fragment applies at once.
- The old form `#clips=<L1>,<L2>,<L3>,<L4>,<L5>` with the keys of
  `color_clips.colours`, for example
  `#clips=blue,lightgreen,lightgreen,purple,purple`, still opens and is
  rewritten to `#c=`. A fragment that does not decode to five known colours
  is ignored and the panel starts at the current colours. The fragment never
  leaves the browser, so the link works on GitHub Pages and offline alike.
- The picker only previews: it changes neither `rack.json` nor the model. The
  screen colours are read from aidB's photos (`UNVERIFIED`), so the real rings
  may differ.

## Building

```powershell
npm --prefix web ci
npm --prefix web run build   # writes web/dist/index.html
npm --prefix web run watch   # rebuilds on every change to web/src or the model
```

`web/build.mjs` bundles three.js, Web Awesome's CSS, `web/src/main.js` and the
model with esbuild into `web/dist/index.html`. `web/src/clips.js` imports
`color_clips`, `levels`, `inserts` and `frame` from `design/rack.json`, which
esbuild inlines, so a change there needs a rebuild:

- The model is inlined deflated (`deflate-raw` from `node:zlib`); the browser
  unpacks it with `DecompressionStream` before `GLTFLoader.parse`.
- `web/src/style.css` imports Web Awesome's `themes/default.css` and
  `native.css` from `node_modules`; esbuild inlines them. They reference no
  remote font or icon (their icons are inline SVG data URIs).
- The favicon is inlined as a data URI.
- The licences of three.js and Web Awesome go into an HTML comment.
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

| Read from                  | Used for                                                       |
| -------------------------- | -------------------------------------------------------------- |
| `kind: "box"`              | the clickable boxes                                            |
| `level`, `column`, `class` | the ColorClip level of a box                                   |
| `travel`                   | how far a box moves                                            |
| `pull_axis`                | the direction towards the front (`[0, 0, 1]`, glTF +z)         |
| `sides`                    | the sides a box pulls out to, `["front", "back"]` (schema 3)   |
| `kind: "plate"`, `plywood` | the top plate, always shown, and its procedural plywood        |
| `kind: "clip"`             | the rings the ColorClips panel recolours                       |
| scene extras `outer_mm`    | the scene framing                                              |

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
