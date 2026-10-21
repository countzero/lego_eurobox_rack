// The rack viewer. It relies only on the node names and extras of
// docs/design.md → *Model objects and the web export*.
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import packed from "rack-model";
import "./style.css";

const canvas = document.getElementById("view");
const info = document.getElementById("info");
const label = document.getElementById("label");

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xf4f5f7);
scene.add(new THREE.HemisphereLight(0xffffff, 0xb8bcc4, 2.2));
const sun = new THREE.DirectionalLight(0xffffff, 2.2);
sun.position.set(2, 4, 3);
scene.add(sun);

const camera = new THREE.PerspectiveCamera(35, 1, 0.01, 100);
const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;

const boxes = [];
let plate = null;
let centre = new THREE.Vector3();
let radius = 1;
let tween = null;

async function unpack(bytes) {
  const stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("deflate-raw"));
  return new Response(stream).arrayBuffer();
}

function resize() {
  const { clientWidth: w, clientHeight: h } = canvas;
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
}

window.addEventListener("resize", resize);

const directions = {
  front: [0, 0, 1],
  side: [-1, 0, 0],
  top: [0, 1, 0.0001],
  three: [-0.8, 0.55, 1],
};

function view(name) {
  const dir = new THREE.Vector3(...directions[name === "reset" ? "three" : name]).normalize();
  const fit = radius / Math.sin(THREE.MathUtils.degToRad(camera.fov / 2)) / Math.min(1, camera.aspect);
  const to = centre.clone().addScaledVector(dir, fit * 1.05);
  const from = camera.position.clone();
  const fromTarget = controls.target.clone();
  tween = { t: 0, step: (k) => {
    camera.position.lerpVectors(from, to, k);
    controls.target.lerpVectors(fromTarget, centre, k);
  } };
}

const ease = (t) => (t < 0.5 ? 2 * t * t : 1 - (-2 * t + 2) ** 2 / 2);

function setOut(box, out) {
  box.out = out;
  box.from = box.node.position.clone();
  box.to = box.home.clone().addScaledVector(box.axis, out ? box.travel : 0);
  box.t = 0;
}

function updateAllButton() {
  const any = boxes.some((b) => b.out);
  const button = document.getElementById("all");
  button.textContent = any ? "All in" : "All out";
}

function highlight(box, on) {
  for (const m of box.materials) m.emissive?.setHex(on ? 0x2a4d7a : 0x000000);
}

const pointer = new THREE.Vector2();
const raycaster = new THREE.Raycaster();
let hovered = null;

function pick(event) {
  const r = canvas.getBoundingClientRect();
  pointer.set(((event.clientX - r.left) / r.width) * 2 - 1, -((event.clientY - r.top) / r.height) * 2 + 1);
  raycaster.setFromCamera(pointer, camera);
  for (const hit of raycaster.intersectObjects(scene.children, true)) {
    if (!hit.object.visible) continue;
    for (let o = hit.object; o; o = o.parent) {
      const box = boxes.find((b) => b.node === o);
      if (box) return box;
    }
    return null;
  }
  return null;
}

canvas.addEventListener("pointermove", (event) => {
  if (event.pointerType !== "mouse") return;
  const box = pick(event);
  if (box !== hovered) {
    if (hovered) highlight(hovered, false);
    if (box) highlight(box, true);
    hovered = box;
  }
  canvas.style.cursor = box ? "pointer" : "";
  label.hidden = !box;
  if (box) {
    label.textContent = box.name;
    label.style.left = `${event.clientX + 14}px`;
    label.style.top = `${event.clientY + 14}px`;
  }
});

canvas.addEventListener("pointerleave", () => {
  if (hovered) highlight(hovered, false);
  hovered = null;
  label.hidden = true;
});

// A click is a press and release without dragging, so orbiting never toggles a box.
let down = null;
canvas.addEventListener("pointerdown", (e) => { down = [e.clientX, e.clientY]; });
canvas.addEventListener("pointerup", (event) => {
  if (!down || Math.hypot(event.clientX - down[0], event.clientY - down[1]) > 5) return;
  down = null;
  const box = pick(event);
  if (box) {
    setOut(box, !box.out);
    updateAllButton();
  }
});

for (const button of document.querySelectorAll("[data-view]")) {
  button.addEventListener("click", () => view(button.dataset.view));
}

document.getElementById("all").addEventListener("click", () => {
  const out = !boxes.some((b) => b.out);
  for (const box of boxes) setOut(box, out);
  updateAllButton();
});

function toggle(id, objects) {
  const button = document.getElementById(id);
  button.addEventListener("click", () => {
    const on = button.getAttribute("aria-pressed") !== "true";
    button.setAttribute("aria-pressed", String(on));
    for (const o of objects) o.visible = on;
  });
}

let last = performance.now();
renderer.setAnimationLoop((now) => {
  const dt = Math.min((now - last) / 1000, 0.1);
  last = now;
  for (const box of boxes) {
    if (box.t >= 1) continue;
    box.t = Math.min(1, box.t + dt / 0.45);
    box.node.position.lerpVectors(box.from, box.to, ease(box.t));
  }
  if (tween) {
    tween.t = Math.min(1, tween.t + dt / 0.6);
    tween.step(ease(tween.t));
    if (tween.t >= 1) tween = null;
  }
  controls.update();
  renderer.render(scene, camera);
});

async function load() {
  const gltf = await new GLTFLoader().parseAsync(await unpack(packed), "");
  const root = gltf.scene;
  scene.add(root);
  root.traverse((o) => {
    const x = o.userData;
    if (x.kind === "plate") plate = o;
    if (x.kind === "box") {
      const materials = [];
      o.traverse((m) => {
        if (!m.isMesh) return;
        m.material = Array.isArray(m.material) ? m.material.map((c) => c.clone()) : m.material.clone();
        materials.push(...[m.material].flat());
      });
      boxes.push({
        node: o,
        name: `L${x.level} C${x.column}, ${x.class} mm class`,
        axis: new THREE.Vector3(...(x.pull_axis ?? [0, 0, 1])).normalize(),
        travel: x.travel ?? 0.4,
        home: o.position.clone(),
        materials,
        out: false,
        t: 1,
      });
    }
  });
  toggle("plate", plate ? [plate] : []);

  const bounds = new THREE.Box3().setFromObject(root);
  const sphere = bounds.getBoundingSphere(new THREE.Sphere());
  centre = sphere.center;
  radius = sphere.radius;

  const mm = root.userData.outer_mm;
  info.textContent = mm ? `Outer size ${mm[0]} × ${mm[1]} × ${mm[2]} mm (W × D × H), ${boxes.length} boxes` : `${boxes.length} boxes`;
  resize();
  view("three");
  tween.step(1);
  tween = null;
}

load().catch((error) => {
  info.textContent = `The model could not be loaded: ${error.message}`;
  console.error(error);
});
