// Font Awesome icons inlined at build time: the page opens offline, with no
// CDN to load them from (docs/web_viewer.md).
import bomb from "@fortawesome/fontawesome-free/svgs/solid/bomb.svg";
import compress from "@fortawesome/fontawesome-free/svgs/solid/compress.svg";
import expand from "@fortawesome/fontawesome-free/svgs/solid/expand.svg";
import palette from "@fortawesome/fontawesome-free/svgs/solid/palette.svg";
import reset from "@fortawesome/fontawesome-free/svgs/solid/rotate-left.svg";

const SVG = { bomb, compress, expand, palette, reset };

// Font Awesome 7 boxes its icons unevenly: rotate-left and palette fill their
// 512 x 512 box, expand and compress only 448 x 448 of a 448 x 512 one (their
// curves' control points reach past the box, the drawing does not). A square
// box round each true drawing, with a sixteenth of it as margin, draws all
// four equally large and centred. The bomb draws from x 32 to 560 and from
// y -16 (the spark) to 512 of a 576 x 512 box: 528 square, 33 margin.
const VIEW = {
  bomb: ["0 0 576 512", "-1 -49 594 594"],
  compress: ["0 0 448 512", "-28 4 504 504"],
  expand: ["0 0 448 512", "-28 4 504 504"],
  palette: ["0 0 512 512", "-32 -32 576 576"],
  reset: ["0 0 512 512", "-32 -32 576 576"],
};

/** Markup of an icon; decorative, so the control round it carries the name.
 *  The licence comment goes; the page's head carries the licences. */
export function icon(name) {
  const [from, to] = VIEW[name];
  return SVG[name]
    .replace(/<!--[\s\S]*?-->/, "")
    .replace("<svg", '<svg aria-hidden="true" class="icon" focusable="false"')
    .replace(`viewBox="${from}"`, `viewBox="${to}"`);
}

/** Fills every `<span data-icon="…">` in the page. */
export function placeIcons(root = document) {
  root.querySelectorAll("[data-icon]").forEach((el) => { el.innerHTML = icon(el.dataset.icon); });
}
