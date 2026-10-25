// The toolbar: its icons, the tooltips and the full-screen toggle.
import { icon, placeIcons } from "./icons.js";

const $ = (id) => document.getElementById(id);

// What a tooltip says; the buttons carry the same name and key for a screen
// reader, so the tooltip itself is hidden from it.
const TIPS = {
  reset: () => "Reset <kbd>Esc</kbd>",
  colours: () => "Colours <kbd>C</kbd>",
  explode: () => "Explode <kbd>E</kbd>",
  fullscreen: () => (document.fullscreenElement ? "Exit full screen" : "Full screen"),
};

let shownFor = null;
let dismissed = null;

function showTip(button) {
  if (button === dismissed) return;
  dismissed = null;
  const tip = $("tooltip");
  tip.innerHTML = TIPS[button.id]?.() ?? button.getAttribute("aria-label");
  tip.hidden = false;
  shownFor = button;
  // Below the button, kept inside the window.
  const r = button.getBoundingClientRect();
  const w = tip.offsetWidth, h = tip.offsetHeight;
  const gap = 6;
  const left = Math.min(Math.max(gap, r.left + r.width / 2 - w / 2), innerWidth - w - gap);
  let top = r.bottom + gap;
  if (top + h > innerHeight - gap) top = r.top - h - gap;
  tip.style.left = `${Math.max(gap, left)}px`;
  tip.style.top = `${Math.max(gap, top)}px`;
}

function hideTip() {
  $("tooltip").hidden = true;
  shownFor = null;
}

/** Hides a shown tooltip (Esc, WCAG 1.4.13); true if one was showing. It stays
 *  hidden until the pointer or the focus reaches another button. */
export function dismissTooltip() {
  if (!shownFor) return false;
  dismissed = shownFor;
  hideTip();
  return true;
}

export function initUi() {
  placeIcons();
  const tip = $("tooltip");
  const tools = document.querySelectorAll(".tool");
  // Hoverable: the pointer may move from the button onto the tooltip.
  const over = (el) => el.matches(":hover");
  const leave = () => {
    requestAnimationFrame(() => {
      if (!shownFor || over(shownFor) || over(tip) || shownFor.matches(":focus-visible")) return;
      hideTip();
    });
  };
  tools.forEach((b) => {
    b.addEventListener("pointerenter", () => showTip(b));
    b.addEventListener("pointerleave", leave);
    b.addEventListener("focus", () => { if (b.matches(":focus-visible")) showTip(b); });
    b.addEventListener("blur", () => {
      if (dismissed === b) dismissed = null;
      if (shownFor === b && !over(b) && !over(tip)) hideTip();
    });
    // A click by pointer hands the focus back to the view, whose keys then
    // work at once; a key press keeps it on the button.
    b.addEventListener("click", (e) => {
      if (e.detail > 0) $("view").focus({ preventScroll: true, focusVisible: false });
      if (shownFor === b) showTip(b);
    });
  });
  tip.addEventListener("pointerleave", leave);
  addEventListener("pointerleave", (e) => { if (!e.relatedTarget) hideTip(); });

  // Only on a touch screen whose browser grants full screen to the page:
  // iPhone Safari grants it to video only.
  const fs = $("fullscreen");
  if (document.fullscreenEnabled && matchMedia("(pointer: coarse)").matches) {
    fs.hidden = false;
    fs.addEventListener("click", () => {
      const p = document.fullscreenElement
        ? document.exitFullscreen()
        : document.documentElement.requestFullscreen({ navigationUI: "hide" });
      p.catch((err) => console.warn("[ui] full screen:", err));
    });
    document.addEventListener("fullscreenchange", () => {
      const on = Boolean(document.fullscreenElement);
      fs.setAttribute("aria-pressed", String(on));
      fs.querySelector("[data-icon]").innerHTML = icon(on ? "compress" : "expand");
      if (shownFor === fs) showTip(fs);
    });
  }
}
