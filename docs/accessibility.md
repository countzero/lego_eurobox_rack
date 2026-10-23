# Accessibility

Read when changing the web viewer's controls, keys, texts or layout: how it
meets WCAG 2.2 Level AA.

## Target and scope

The viewer, `web/dist/index.html`, is to meet WCAG 2.2 Level AA as one full
page, in every state: loading, boxes open or closed, the ColorClips panel
shown or hidden, full screen. No conformance claim is published; the
requirement binds every change. AAA criteria are not pursued. The controls
themselves are described in `docs/web_viewer.md` → *Controls*.

## The view as one component

The canvas is one keyboard component: `tabindex="0"`, `role="application"`,
`aria-roledescription="3D view"`, named *The rack* and described by a hidden
paragraph that lists its keys. It takes the focus once the model is loaded and
on every click into it. Focused, it shows an inset frame round the view; the
toolbar buttons show a focus ring with a dark halo.

- **Keys:** the arrow keys move a box cursor, the hover highlight, over levels
  and columns (Left and Right follow the screen, also from behind); Enter or
  Space pulls the box out to the front or pushes it back, Shift+Enter pulls it
  out to the back; Shift with the arrows turns the view by 15°; `+` and `−`
  zoom by 1.25.
- **Esc** is no character key and stays global: it first hides a shown tooltip
  or box hint (1.4.13), else, with the focus in the ColorClips panel, closes
  the panel and returns the focus to Colours, else resets view, boxes and
  colours. In full screen the browser takes the first Esc to leave full
  screen.
- **C** shows or hides the ColorClips panel only while the view or a toolbar
  button has the focus (2.1.4, *Active only on focus*).
- **Focus back to the view:** a toolbar button clicked with a pointer hands
  the focus back to the view, so its keys go on working; one pressed from the
  keyboard keeps it.

## Without dragging

Keys do not meet 2.5.1 and 2.5.7: a pointer user who cannot drag or pinch
needs clicks (Understanding SC 2.5.7 → *Relationship to keyboard*).

| Drag or pinch          | Single click or tap                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------- |
| Turn the view          | A click off the boxes in the left or right third turns the view 45° to that side       |
| Pinch or wheel to zoom | A double click off the boxes centres the view on that point and zooms in               |
| Zoom back out          | Reset                                                                                  |
| Open or close a box    | A click on the box, at once, as before                                                 |

The single click waits 300 ms so that it is not the first half of a double
tap.

## Announcements and names

- **Live region** (polite): each step of the box cursor and each box opened
  or closed by key ("Level 3, column 2, closed").
- **The weakest-step line** of the ColorClips panel is a polite live region,
  so a changed colour announces the new weakest step.
- **`#info`**, the storage volume, is a status (`role="status"`).
- **Icon buttons** are native `<button>` elements named by `aria-label`:
  Reset, Colours with `aria-expanded` and `aria-controls` pointing at the
  panel, Full screen with `aria-pressed` and a constant name. The icons are
  `aria-hidden`.
- **Tooltips** show on hover and on keyboard focus with the name and key
  ("Reset Esc", "Colours C"); they can be hovered, stay until the pointer or
  the focus leaves, and Esc hides them (1.4.13).
- **Swatches** are named by the colour's English name.

## Contrast and layout

| Mark                               | Against              | Ratio  |
| ---------------------------------- | -------------------- | ------ |
| Title text `text-normal` (gray-10) | White panel          | 16.8:1 |
| Quiet text `#info` (gray-40)       | White panel          | 7.1:1  |
| Quiet text before 0019 (gray-40)   | Scene `#8c8c8c`      | 2.1:1  |
| Icon `text-normal` (gray-10)       | White button         | 16.8:1 |
| White button                       | Scene `#8c8c8c`      | 3.4:1  |
| Focus ring `focus` (blue-60)       | White                | 3.0:1  |
| Focus ring `focus` (blue-60)       | Scene `#8c8c8c`      | 1.1:1  |
| Focus ring `focus` (blue-60)       | Dark halo (gray-10)  | 5.6:1  |
| Dark halo (gray-10)                | Scene `#8c8c8c`      | 5.0:1  |

Computed with the WCAG relative-luminance formula from the hex values of Web
Awesome's tokens (`themes/default.css` and `color/palettes/default.css`:
`--wa-color-text-normal` → `neutral-10` → `gray-10` `#1b1d26`,
`--wa-color-text-quiet` → `neutral-40` → `gray-40` `#545868`,
`--wa-color-focus` → `brand-60` → `blue-60` `#3e96ff`). The title and the
volume sit on a white panel, so their contrast never depends on the scene;
before, the quiet text stood on the scene at 2.1:1. The ring alone fails
against the scene, which is why it carries the dark halo. Recheck the table
when `web/src/style.css` changes a token.

Buttons are 2.75rem (about 44 px); swatches are at least 28 × 24 px (2.5.8).
At 320 × 256 CSS pixels and at 390 × 844 the toolbar, the title panel and the
ColorClips panel stay within the window and overlap nothing; the panel
scrolls. The text-spacing overrides of 1.4.12 clip nothing.

## Judgement calls

- **2.5.1 and 2.5.7:** 45° steps and a double click to zoom in stand in for
  free dragging and pinching; zooming out by pointer is Reset.
- **4.1.2:** the boxes are parts of one named view, not controls of their own;
  the keyboard reaches each through the box cursor.
- **`role="application"`** puts screen readers into focus mode, so the view's
  keys reach the page; the hidden description lists them.
- **Full screen** is offered only on touch screens whose browser grants it to
  the page; iPhone Safari grants it only to video, and a desktop has F11.

## Checking

After a change to `web/src/`, in Chromium:

- Lighthouse's accessibility audit at 100 and axe with no violations. Neither
  finds the failures above by itself, so the rest are checked by hand.
- Every function by keyboard alone: Tab order view, Reset, Colours, Full
  screen when shown, the swatches when the panel is open; the view's keys;
  Esc in each of its three cases; C from the view and from a button.
- Emulated at 320 × 256 and at 390 × 844 with touch: no control overlaps
  another or leaves the window; the single and double tap work.
- The text-spacing bookmarklet's values (line height 1.5, paragraph spacing 2,
  letter spacing 0.12, word spacing 0.16): nothing clipped (1.4.12).
- The contrast ratios of the table above, against the final CSS.
