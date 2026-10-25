// The rack viewer. It relies only on the node names and extras of
// docs/design.md → *Model objects and the web export*.
import * as THREE from "three";
import { MeshoptDecoder } from "three/addons/libs/meshopt_decoder.module.js";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import packed from "rack-model";
import { addClipMaterials, initClips, isPanelOpen, openPanel } from "./clips.js";
import { announce, createHint, inViewer } from "./a11y.js";
import { initUi, dismissTooltip } from "./ui.js";
import { applyPlywood } from "./plywood.js";
import { redraw, take } from "./redraw.js";
import { TAA_SAMPLES, createView } from "./view.js";
import "./style.css";

const canvas = document.getElementById("view");
const info = document.getElementById("info");
const label = document.getElementById("label");

const { renderer, scene, camera, controls, sun, moving, composer, taa, resize: resizeView } = createView(canvas);
// Read live, so a change in the system settings applies at once.
const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
const boxes = [];
// Every node with an `explode` extra: where it is assembled and its moves in
// the exploded view, one offset per step in its parent's space; the steps run
// one after the other, the boxes out first (docs/design.md → *Contracts*).
const parts = [];
let centre = new THREE.Vector3();
let radius = 1;
let tween = null;
// The exploded view: k runs from 0 (assembled) to 1 (exploded).
const explosion = { k: 0, from: 0, to: 0, t: 1, centre: new THREE.Vector3(), radius: 1 };
const exploded = () => explosion.to === 1;
const EXPLODE_SECONDS = 1.8; // three steps of 0.6 s
const steps = (list) => (list ?? []).map((v) => new THREE.Vector3(...v));
const explodeButton = document.getElementById("explode");

async function unpack(bytes) {
  const stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("deflate-raw"));
  return new Response(stream).arrayBuffer();
}

let resized = false;

function resize() {
  resizeView();
  resized = true;
}

window.addEventListener("resize", resize);

const directions = {
  front: [0, 0, 1],
  side: [-1, 0, 0],
  top: [0, 1, 0.0001],
  three: [-0.8, 0.55, 1],
};

// The camera fits the rack as it is, or as it will be once the exploded view
// has moved; dir keeps the current direction when not given.
function fit(dir) {
  const r = exploded() ? explosion.radius : radius;
  const target = exploded() ? explosion.centre : centre;
  dir ??= camera.position.clone().sub(controls.target).normalize();
  const d = r / Math.sin(THREE.MathUtils.degToRad(camera.fov / 2)) / Math.min(1, camera.aspect);
  const to = target.clone().addScaledVector(dir, d * 1.05);
  const from = camera.position.clone();
  const fromTarget = controls.target.clone();
  tween = { t: 0, step: (k) => {
    camera.position.lerpVectors(from, to, k);
    controls.target.lerpVectors(fromTarget, target, k);
  } };
}

function view(name) {
  fit(new THREE.Vector3(...directions[name === "reset" ? "three" : name]).normalize());
}

const ease = (t) => (t < 0.5 ? 2 * t * t : 1 - (-2 * t + 2) ** 2 / 2);

// side is +1 (front, along pull_axis) or -1 (back, against it). A box's pull
// is apart from the exploded view's move, so the two add up.
function setOut(box, out, side = 1) {
  box.out = out;
  box.from = box.pull.clone();
  box.to = new THREE.Vector3().addScaledVector(box.axis, out ? side * box.travel : 0);
  box.t = 0;
}

// Adds the exploded move at k (0 to 1) to v: each step takes its share of k in turn.
function addMove(v, steps, k) {
  steps.forEach((s, i) => v.addScaledVector(s, THREE.MathUtils.clamp(k * steps.length - i, 0, 1)));
  return v;
}

function placeBox(box) {
  addMove(box.node.position.copy(box.home).add(box.pull), box.explode, explosion.k);
}

// Draws the rack apart or puts it together; open boxes close first.
function setExploded(on) {
  if (on === exploded()) return;
  if (on) for (const box of boxes) if (box.out) setOut(box, false);
  explosion.from = explosion.k;
  explosion.to = on ? 1 : 0;
  explosion.t = 0;
  explodeButton.setAttribute("aria-pressed", String(on));
  fit();
  redraw();
}

function highlight(box, on) {
  for (const m of box.materials) m.emissive?.setHex(on ? 0x2a4d7a : 0x000000);
  redraw();
}

const pointer = new THREE.Vector2();
const raycaster = new THREE.Raycaster();
let hovered = null;

function pick(event) {
  const r = canvas.getBoundingClientRect();
  pointer.set(((event.clientX - r.left) / r.width) * 2 - 1, -((event.clientY - r.top) / r.height) * 2 + 1);
  raycaster.setFromCamera(pointer, camera);
  for (const hit of raycaster.intersectObjects(scene.children, true)) {
    if (!solid(hit)) continue;
    for (let o = hit.object; o; o = o.parent) {
      const box = boxes.find((b) => b.node === o);
      if (box) return { box, side: sideOf(box, hit.point) };
    }
    return null;
  }
  return null;
}

// Screws, nuts, washers and end caps let a click through to what lies behind.
const passThrough = new Set(["fastener", "cap"]);
function solid(hit) {
  if (!hit.object.visible) return false;
  for (let o = hit.object; o; o = o.parent) if (passThrough.has(o.userData.kind)) return false;
  return true;
}

// The side of the box's current centre the hit lies on, in the box's parent space.
function sideOf(box, point) {
  if (!box.back) return 1;
  const local = box.node.parent.worldToLocal(point.clone());
  const centre = box.centre.clone().add(box.node.position).sub(box.home);
  return local.sub(centre).dot(box.axis) >= 0 ? 1 : -1;
}

canvas.addEventListener("pointermove", (event) => {
  if (event.pointerType !== "mouse") return;
  const { box } = pick(event) ?? {};
  if (box !== hovered) {
    if (hovered) highlight(hovered, false);
    if (box) highlight(box, true);
    hovered = box ?? null;
  }
  canvas.style.cursor = box ? "pointer" : "";
  if (box) {
    clearCursor();
    hint.show(box, exploded() ? "Assemble" : box.out ? "Close" : "Open", event.clientX, event.clientY);
  } else hint.hide();
});

canvas.addEventListener("pointerleave", () => {
  if (hovered) highlight(hovered, false);
  hovered = null;
  hint.hide();
});

// A click is a press and release without dragging, so orbiting never toggles a box.
// A click beside the boxes turns the view; a double click there zooms to the point.
let down = null;
let single = null;
canvas.addEventListener("pointerdown", (e) => {
  down = [e.clientX, e.clientY];
  canvas.focus({ preventScroll: true, focusVisible: false });
});
canvas.addEventListener("pointerup", (event) => {
  if (!down || Math.hypot(event.clientX - down[0], event.clientY - down[1]) > 5) return;
  down = null;
  const { box, side } = pick(event) ?? {};
  if (box) {
    clearTimeout(single?.timer);
    single = null;
    if (exploded()) {
      setExploded(false);
      hint.hide();
      announce("Assembled");
    } else setOut(box, !box.out, side);
    return;
  }
  if (single) {
    clearTimeout(single.timer);
    single = null;
    zoomTo(event);
    return;
  }
  const r = canvas.getBoundingClientRect();
  const third = Math.floor(((event.clientX - r.left) / r.width) * 3);
  single = { timer: setTimeout(() => {
    single = null;
    if (third !== 1) turn(third < 1 ? 1 : -1);
  }, 300) };
});

const hint = createHint(label);

// The model's root is the scene child that holds the boxes.
function model() {
  let o = boxes[0]?.node;
  while (o?.parent && o.parent !== scene) o = o.parent;
  return o;
}

function zoomTo(event) {
  const r = canvas.getBoundingClientRect();
  pointer.set(((event.clientX - r.left) / r.width) * 2 - 1, -((event.clientY - r.top) / r.height) * 2 + 1);
  raycaster.setFromCamera(pointer, camera);
  const root = model();
  const hit = root && raycaster.intersectObject(root, true).find(solid);
  const target = hit ? hit.point.clone() : controls.target.clone();
  const fromTarget = controls.target.clone();
  const from = camera.position.clone();
  const to = target.clone().addScaledVector(from.clone().sub(fromTarget), 1 / 1.5);
  tween = { t: 0, step: (k) => {
    camera.position.lerpVectors(from, to, k);
    controls.target.lerpVectors(fromTarget, target, k);
  } };
  redraw();
}

// dir +1 turns the view to the left, like rotateLeft.
function turn(dir) {
  const target = controls.target.clone();
  const offset = camera.position.clone().sub(target);
  const up = new THREE.Vector3(0, 1, 0);
  const angle = -dir * Math.PI / 4;
  tween = { t: 0, step: (k) => {
    camera.position.copy(target).add(offset.clone().applyAxisAngle(up, angle * k));
  } };
  redraw();
}

// The keyboard cursor over the boxes.
let cursor = null;

function clearCursor() {
  if (!cursor) return;
  if (cursor !== hovered) highlight(cursor, false);
  cursor = null;
  redraw();
}

function setCursor(box) {
  if (cursor && cursor !== box) highlight(cursor, false);
  cursor = box;
  highlight(box, true);
  redraw();
}

const levelList = () => [...new Set(boxes.map((b) => b.level))].sort((a, b) => a - b);
const screenX = (box) => new THREE.Box3().setFromObject(box.node).getCenter(new THREE.Vector3()).project(camera).x;
const stateOf = (box) => {
  if (!box.out) return "closed";
  const d = box.to.dot(box.axis);
  return d < 0 ? "out to the back" : "out to the front";
};
const where = (box) => `Level ${box.level}, column ${box.column}`;

function moveCursor(key) {
  const lv = levelList();
  if (!lv.length) return;
  if (!cursor) {
    const row = boxes.filter((b) => b.level === lv[Math.floor((lv.length - 1) / 2)]).sort((a, b) => screenX(a) - screenX(b));
    setCursor(row[Math.floor((row.length - 1) / 2)]);
  } else if (key === "ArrowUp" || key === "ArrowDown") {
    const i = lv.indexOf(cursor.level) + (key === "ArrowUp" ? 1 : -1);
    if (i < 0 || i >= lv.length) return announce(`${where(cursor)}, ${stateOf(cursor)}`);
    const next = boxes.find((b) => b.level === lv[i] && b.column === cursor.column)
      ?? boxes.find((b) => b.level === lv[i]);
    setCursor(next);
  } else {
    // Left and right follow the screen, so they flip when the rack is seen from behind.
    const row = boxes.filter((b) => b.level === cursor.level).sort((a, b) => screenX(a) - screenX(b));
    const i = row.indexOf(cursor) + (key === "ArrowRight" ? 1 : -1);
    if (i >= 0 && i < row.length) setCursor(row[i]);
  }
  announce(`${where(cursor)}, ${stateOf(cursor)}`);
}

canvas.addEventListener("blur", clearCursor);

canvas.addEventListener("keydown", (ev) => {
  if (ev.ctrlKey || ev.altKey || ev.metaKey) return;
  const step = THREE.MathUtils.degToRad(15);
  const arrows = ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"];
  if (arrows.includes(ev.key) && ev.shiftKey) {
    if (ev.key === "ArrowLeft") controls.rotateLeft(step);
    if (ev.key === "ArrowRight") controls.rotateLeft(-step);
    if (ev.key === "ArrowUp") controls.rotateUp(step);
    if (ev.key === "ArrowDown") controls.rotateUp(-step);
  } else if (arrows.includes(ev.key)) {
    moveCursor(ev.key);
  } else if (["+", "="].includes(ev.key) || ev.code === "NumpadAdd") {
    controls.dollyIn(1.25);
  } else if (ev.key === "-" || ev.code === "NumpadSubtract") {
    controls.dollyOut(1.25);
  } else if ((ev.key === "Enter" || ev.key === " ") && cursor) {
    if (ev.repeat) return ev.preventDefault();
    const back = ev.key === "Enter" && ev.shiftKey;
    if (back && !cursor.back) return;
    if (ev.shiftKey && !back) return;
    if (exploded()) {
      setExploded(false);
      announce("Assembled");
      ev.preventDefault();
      return;
    }
    if (cursor.out) setOut(cursor, false);
    else setOut(cursor, true, back ? -1 : 1);
    announce(`${where(cursor)}, ${cursor.out ? stateOf(cursor) : "pushed in"}`);
  } else return;
  ev.preventDefault();
  redraw();
});

window.addEventListener("keydown", (ev) => {
  if (ev.defaultPrevented || ev.ctrlKey || ev.altKey || ev.metaKey) return;
  if (ev.key === "Escape") {
    ev.preventDefault();
    if (dismissTooltip() || hint.dismiss()) return;
    const panel = document.getElementById("clips");
    if (isPanelOpen() && panel.contains(document.activeElement)) {
      openPanel(false);
      document.getElementById("colours").focus();
      return;
    }
    document.getElementById("reset").click();
    announce("View reset");
    return;
  }
  if ((ev.key === "c" || ev.key === "C") && inViewer(ev) && !ev.repeat) {
    ev.preventDefault();
    document.getElementById("colours").click();
    announce(isPanelOpen() ? "Colours shown" : "Colours hidden");
  }
  if ((ev.key === "e" || ev.key === "E") && inViewer(ev) && !ev.repeat) {
    ev.preventDefault();
    explodeButton.click();
  }
});

explodeButton.addEventListener("click", () => {
  setExploded(!exploded());
  announce(exploded() ? "Exploded" : "Assembled");
});

for (const button of document.querySelectorAll("[data-view]")) {
  button.addEventListener("click", () => {
    if (button.dataset.view === "reset") {
      setExploded(false);
      for (const box of boxes) if (box.out) setOut(box, false);
    }
    view(button.dataset.view);
  });
}

// Without damping the controls move the camera inside their own pointer and
// wheel handlers, so the loop's controls.update() sees nothing left to do:
// the change event is what marks the frame as one in motion.
let cameraMoved = false;
controls.addEventListener("change", () => { cameraMoved = true; });

// While anything moves, one MSAA frame at the lower ratio; once it stops,
// one jittered sample a frame at the screen's own until the still frame has
// them all; then nothing is drawn (docs/web_viewer.md → *Performance*).
let last = performance.now();
let settle = false;
renderer.setAnimationLoop((now) => {
  // Reduced motion: every tween ends in the frame it starts.
  const dt = reducedMotion.matches ? Infinity : Math.min((now - last) / 1000, 0.1);
  last = now;
  let busy = resized;
  resized = false;
  const exploding = explosion.t < 1;
  if (exploding) {
    explosion.t = Math.min(1, explosion.t + dt / EXPLODE_SECONDS);
    explosion.k = explosion.from + (explosion.to - explosion.from) * ease(explosion.t);
    for (const p of parts) addMove(p.node.position.copy(p.home), p.steps, explosion.k);
    busy = true;
  }
  for (const box of boxes) {
    const pulling = box.t < 1;
    if (!pulling && !exploding) continue;
    if (pulling) {
      box.t = Math.min(1, box.t + dt / 0.45);
      box.pull.lerpVectors(box.from, box.to, ease(box.t));
    }
    placeBox(box);
    busy = true;
  }
  if (busy) renderer.shadowMap.needsUpdate = true;
  if (tween) {
    tween.t = Math.min(1, tween.t + dt / 0.6);
    tween.step(ease(tween.t));
    if (tween.t >= 1) tween = null;
    busy = true;
  }
  controls.update();
  busy ||= cameraMoved;
  cameraMoved = false;
  // A requested frame (the model loaded, a highlight, new ring colours): its
  // shadows are redrawn too, which costs little next to how rarely it comes.
  let dirty = take();
  if (dirty) renderer.shadowMap.needsUpdate = true;
  if (busy) {
    moving.render();
    settle = true;
    return;
  }
  // Whatever changed, the samples gathered so far show the old picture.
  if (settle || dirty) {
    taa.accumulateIndex = -1;
    settle = false;
    dirty = true;
  } else if (taa.accumulateIndex >= 0 && taa.accumulateIndex < TAA_SAMPLES) {
    dirty = true;
  }
  if (dirty) composer.render();
});

async function load() {
  const [bytes] = await Promise.all([unpack(packed), MeshoptDecoder.ready]);
  const gltf = await new GLTFLoader().setMeshoptDecoder(MeshoptDecoder).parseAsync(bytes, "");
  const root = gltf.scene;
  scene.add(root);
  root.traverse((o) => {
    const x = o.userData;
    if (o.isMesh) {
      o.castShadow = true;
      o.receiveShadow = true;
    }
    if (x.kind === "plate" && x.plywood) o.traverse((m) => { if (m.isMesh) applyPlywood(m, x.plywood); });
    if (x.kind === "box") {
      const materials = [];
      o.traverse((m) => {
        if (!m.isMesh) return;
        m.material = Array.isArray(m.material) ? m.material.map((c) => c.clone()) : m.material.clone();
        materials.push(...[m.material].flat());
      });
      o.traverse((c) => {
        if (c.userData.kind !== "clip") return;
        c.traverse((m) => { if (m.isMesh) addClipMaterials(x.level, [m.material].flat()); });
      });
      boxes.push({
        node: o,
        level: x.level,
        column: x.column,
        axis: new THREE.Vector3(...(x.pull_axis ?? [0, 0, 1])).normalize(),
        travel: x.travel ?? 0.4,
        back: (x.sides ?? ["front"]).includes("back"),
        home: o.position.clone(),
        pull: new THREE.Vector3(),
        explode: steps(x.explode),
        materials,
        out: false,
        t: 1,
      });
    } else if (x.explode) {
      parts.push({ node: o, home: o.position.clone(), steps: steps(x.explode) });
    }
  });
  root.updateMatrixWorld(true);
  for (const box of boxes) {
    const world = new THREE.Box3().setFromObject(box.node).getCenter(new THREE.Vector3());
    box.centre = box.node.parent.worldToLocal(world);
  }

  const bounds = new THREE.Box3().setFromObject(root);
  radius = bounds.getBoundingSphere(new THREE.Sphere()).radius;
  // The view turns about the middle of the rack: the frame from the floor to
  // the top of the plate, whatever else the model holds.
  const rack = new THREE.Box3();
  root.traverse((o) => { if (["frame", "plate"].includes(o.userData.kind)) rack.expandByObject(o); });
  centre = (rack.isEmpty() ? bounds : rack).getCenter(new THREE.Vector3());

  // The exploded rack's size, measured once with every part moved out.
  for (const p of parts) addMove(p.node.position.copy(p.home), p.steps, 1);
  for (const box of boxes) addMove(box.node.position.copy(box.home), box.explode, 1);
  root.updateMatrixWorld(true);
  const apart = new THREE.Box3().setFromObject(root);
  explosion.radius = apart.getBoundingSphere(new THREE.Sphere()).radius;
  explosion.centre = apart.getCenter(new THREE.Vector3());
  for (const p of parts) p.node.position.copy(p.home);
  for (const box of boxes) box.node.position.copy(box.home);
  root.updateMatrixWorld(true);
  const reach = Math.max(radius, explosion.radius + explosion.centre.distanceTo(centre));

  const floorY = bounds.min.y;
  const ground = new THREE.Mesh(
    new THREE.CircleGeometry(reach * 4, 64).rotateX(-Math.PI / 2),
    new THREE.MeshStandardMaterial({ color: 0x737373, roughness: 0.85 }),
  );
  ground.position.set(centre.x, floorY, centre.z);
  ground.receiveShadow = true;
  scene.add(ground);
  sun.target.position.copy(centre);
  sun.position.copy(centre).add(new THREE.Vector3(-1.5, 4, 3));
  const cam = sun.shadow.camera;
  cam.left = cam.bottom = -reach * 1.5;
  cam.right = cam.top = reach * 1.5;
  cam.near = 0.1;
  cam.far = 10;
  cam.updateProjectionMatrix();

  info.textContent = "";
  info.hidden = true;
  resize();
  view("three");
  tween.step(1);
  tween = null;
  redraw();
}

initClips();
initUi();
load().then(() => {
  canvas.focus({ preventScroll: true, focusVisible: false });
}).catch((error) => {
  info.hidden = false;
  info.textContent = `The model could not be loaded: ${error.message}`;
  console.error(error);
});
