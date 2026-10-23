// The ColorClips panel: one colour per level from rack.json → color_clips, kept
// in the URL fragment as #c=<3 base64url chars> (docs/web_viewer.md → *ColorClips*).
import { color_clips as clips, levels, inserts, frame } from "../../design/rack.json";
import { deltaE2000 } from "./colour.js";

const keys = Object.keys(clips.colours);
const levelNumbers = levels.map((l) => l.level);
const layoutNames = { half: "set 1/2", quarter: "set 1/4" };
const current = levelNumbers.map((n) => clips.levels[String(n)]);
const B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_";
const width = Math.ceil(Math.log(keys.length ** levelNumbers.length) / Math.log(64));

const materials = new Map(levelNumbers.map((n) => [n, []]));
let choice = [...current];

const name = (key) => clips.colours[key].name;
const same = (a, b) => a.every((k, i) => k === b[i]);

export function colourOf(level) {
  return name(choice[levelNumbers.indexOf(level)]);
}

export function addClipMaterials(level, list) {
  materials.get(level)?.push(...list);
  paint();
}

// L1 is the least significant base-9 digit; the number is written big-endian in base64url.
function encode(list) {
  let n = list.reduceRight((acc, key) => acc * keys.length + keys.indexOf(key), 0);
  let s = "";
  for (let i = 0; i < width; i++, n = Math.floor(n / 64)) s = B64[n % 64] + s;
  return s;
}

function decode(s) {
  if (s.length !== width || [...s].some((c) => !B64.includes(c))) return null;
  let n = [...s].reduce((acc, c) => acc * 64 + B64.indexOf(c), 0);
  if (n >= keys.length ** levelNumbers.length) return null;
  return levelNumbers.map(() => {
    const key = keys[n % keys.length];
    n = Math.floor(n / keys.length);
    return key;
  });
}

function parse(hash) {
  const compact = /(?:^#|&)c=([^&]*)/.exec(hash);
  if (compact) return decode(compact[1]);
  const legacy = /(?:^#|&)clips=([^&]*)/.exec(hash);
  if (!legacy) return null;
  const list = decodeURIComponent(legacy[1]).split(",");
  return list.length === levelNumbers.length && list.every((k) => keys.includes(k)) ? list : null;
}

function paint() {
  levelNumbers.forEach((n, i) => {
    for (const m of materials.get(n)) m.color.set(clips.colours[choice[i]].srgb);
  });
}

function levelName(lv) {
  const layout = inserts.boxes[`L${lv.level}.C1`];
  return `L${lv.level} · ${lv.class}, ${layout ? layoutNames[layout] : "no inserts"}`;
}

function render() {
  for (const button of document.querySelectorAll("#levels button")) {
    const i = levelNumbers.indexOf(Number(button.dataset.level));
    button.setAttribute("aria-pressed", String(choice[i] === button.dataset.colour));
  }
  for (const el of document.querySelectorAll("#levels [data-name]")) {
    el.textContent = name(choice[levelNumbers.indexOf(Number(el.dataset.name))]);
  }

  const counts = new Map();
  for (const key of choice) counts.set(key, (counts.get(key) ?? 0) + frame.columns);
  document.getElementById("order").innerHTML = [...counts]
    .map(([key, n]) => `<li><i style="background:${clips.colours[key].srgb}"></i>${n} × ${name(key)} <code>${clips.colours[key].article}</code></li>`)
    .join("");

  let weakest = null;
  for (let i = 1; i < choice.length; i++) {
    if (choice[i] === choice[i - 1]) continue;
    const d = deltaE2000(clips.colours[choice[i - 1]].srgb, clips.colours[choice[i]].srgb);
    if (!weakest || d < weakest.d) weakest = { d, lower: levelNumbers[i - 1], upper: levelNumbers[i] };
  }
  const step = document.getElementById("step");
  step.classList.toggle("weak", Boolean(weakest && weakest.d < 20));
  step.textContent = weakest
    ? `Weakest neighbour step: L${weakest.lower} / L${weakest.upper}, ΔE ${weakest.d.toFixed(0)}${weakest.d < 20 ? ", hard to tell apart" : ""}`
    : "All levels share one colour";
}

// The current colours of rack.json write no fragment, so a plain link shows them.
const link = () => location.href.split("#")[0] + (same(choice, current) ? "" : `#c=${encode(choice)}`);

function set(list, write = true) {
  choice = [...list];
  paint();
  render();
  if (write && location.href !== link()) history.replaceState(null, "", link());
}

function build() {
  document.getElementById("levels").innerHTML = [...levels].reverse()
    .map((lv) => `<div class="level"><span class="level-name">${levelName(lv)}: <b data-name="${lv.level}"></b></span>`
      + `<div class="swatches" role="group" aria-label="L${lv.level} colour">`
      + keys.map((k) => `<button class="swatch" data-level="${lv.level}" data-colour="${k}" style="background:${clips.colours[k].srgb}"`
        + ` title="${name(k)}" aria-label="${name(k)}"></button>`).join("")
      + "</div></div>")
    .join("");

  document.getElementById("levels").addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (!button) return;
    const next = [...choice];
    next[levelNumbers.indexOf(Number(button.dataset.level))] = button.dataset.colour;
    set(next);
  });
  document.querySelector('[data-view="reset"]')?.addEventListener("click", () => set(current));

  const panel = document.getElementById("clips");
  const toggle = document.getElementById("colours");
  const show = (on) => {
    panel.hidden = !on;
    toggle.setAttribute("aria-pressed", String(on));
  };
  show(false);
  toggle.addEventListener("click", () => show(panel.hidden));

  window.addEventListener("hashchange", () => {
    const list = parse(location.hash) ?? current;
    if (!same(list, choice)) set(list, false);
  });
}

export function initClips() {
  build();
  const list = parse(location.hash);
  // Rewrites an old #clips= link into the compact form.
  set(list ?? current, Boolean(list));
}
