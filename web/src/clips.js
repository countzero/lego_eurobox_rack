// The ColorClips panel: one colour per level from rack.json → color_clips, kept
// in the URL fragment as #clips=<L1>,…,<L5> (docs/web_viewer.md → *ColorClips*).
import { color_clips as clips, levels, inserts, frame } from "../../design/rack.json";
import { deltaE2000 } from "./colour.js";

const keys = Object.keys(clips.colours);
const levelNumbers = levels.map((l) => l.level);
const layoutNames = { half: "set 1/2", quarter: "set 1/4" };
const current = levelNumbers.map((n) => clips.levels[String(n)]);
const presets = [
  { name: "Current", why: "the colours in design/rack.json", colours: current },
  ...clips.presets.map((p) => ({ ...p, colours: levelNumbers.map((n) => p.levels[String(n)]) })),
];

const materials = new Map(levelNumbers.map((n) => [n, []]));
let choice = [...current];

const label = (key) => clips.colours[key].label;
const same = (a, b) => a.every((k, i) => k === b[i]);

export function colourOf(level) {
  return label(choice[levelNumbers.indexOf(level)]);
}

export function addClipMaterials(level, list) {
  materials.get(level)?.push(...list);
  paint();
}

function parse(hash) {
  const match = /(?:^#|&)clips=([^&]*)/.exec(hash);
  if (!match) return null;
  const list = decodeURIComponent(match[1]).split(",");
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
  for (const button of document.querySelectorAll("#presets button")) {
    button.setAttribute("aria-pressed", String(same(presets[button.dataset.preset].colours, choice)));
  }
  for (const button of document.querySelectorAll("#levels button")) {
    const i = levelNumbers.indexOf(Number(button.dataset.level));
    button.setAttribute("aria-pressed", String(choice[i] === button.dataset.colour));
  }
  for (const name of document.querySelectorAll("#levels [data-name]")) {
    name.textContent = label(choice[levelNumbers.indexOf(Number(name.dataset.name))]);
  }

  const counts = new Map();
  for (const key of choice) counts.set(key, (counts.get(key) ?? 0) + frame.columns);
  document.getElementById("order").innerHTML = [...counts]
    .map(([key, n]) => `<li><i style="background:${clips.colours[key].srgb}"></i>${n} × ${label(key)} <code>${clips.colours[key].article}</code></li>`)
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

const link = () => `${location.href.split("#")[0]}#clips=${choice.join(",")}`;

function set(list, write = true) {
  choice = [...list];
  paint();
  render();
  if (write && location.href !== link()) history.replaceState(null, "", link());
}

function build() {
  document.getElementById("presets").innerHTML = presets
    .map((p, i) => `<button data-preset="${i}" title="${p.why}">${p.name}</button>`)
    .join("");
  document.getElementById("levels").innerHTML = [...levels].reverse()
    .map((lv) => `<div class="level"><span class="level-name">${levelName(lv)}: <b data-name="${lv.level}"></b></span>`
      + `<div class="swatches" role="group" aria-label="L${lv.level} colour">`
      + keys.map((k) => `<button class="swatch" data-level="${lv.level}" data-colour="${k}" style="background:${clips.colours[k].srgb}"`
        + ` title="${label(k)} (${clips.colours[k].article})" aria-label="${label(k)}"></button>`).join("")
      + "</div></div>")
    .join("");

  document.getElementById("presets").addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (button) set(presets[button.dataset.preset].colours);
  });
  document.getElementById("levels").addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (!button) return;
    const next = [...choice];
    next[levelNumbers.indexOf(Number(button.dataset.level))] = button.dataset.colour;
    set(next);
  });

  const panel = document.getElementById("clips");
  const toggle = document.getElementById("colours");
  const show = (on) => {
    panel.hidden = !on;
    toggle.setAttribute("aria-pressed", String(on));
  };
  show(!window.matchMedia("(max-width: 600px)").matches);
  toggle.addEventListener("click", () => show(panel.hidden));

  window.addEventListener("hashchange", () => {
    const list = parse(location.hash);
    if (list && !same(list, choice)) set(list, false);
  });
}

export function initClips() {
  build();
  set(parse(location.hash) ?? current, false);
}
