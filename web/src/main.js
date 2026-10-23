// The rack viewer. It relies only on the node names and extras of
// docs/design.md → *Model objects and the web export*.
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import packed from "rack-model";
import { frame, levels, model_boxes, box_models } from "../../design/rack.json";
import { addClipMaterials, initClips } from "./clips.js";
import { applyPlywood } from "./plywood.js";
import "./style.css";

const canvas = document.getElementById("view");
const info = document.getElementById("info");
const label = document.getElementById("label");

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.toneMapping = THREE.AgXToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x8c8c8c);
// The aluminium is a full metal and only shows what it reflects; a procedural
// room gives it something to reflect without loading a file.
const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
scene.environmentIntensity = 0.25;
pmrem.dispose();
scene.add(new THREE.HemisphereLight(0xffffff, 0x5a5a5a, 0.15));
const sun = new THREE.DirectionalLight(0xffffff, 2.6);
sun.position.set(-1.5, 4, 3);
sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048);
sun.shadow.bias = -0.0005;
sun.shadow.normalBias = 0.01;
scene.add(sun, sun.target);

const camera = new THREE.PerspectiveCamera(35, 1, 0.01, 100);
const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;

const boxes = [];
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

// side is +1 (front, along pull_axis) or -1 (back, against it).
function setOut(box, out, side = 1) {
  box.out = out;
  box.from = box.node.position.clone();
  box.to = box.home.clone().addScaledVector(box.axis, out ? side * box.travel : 0);
  box.t = 0;
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
      if (box) return { box, side: sideOf(box, hit.point) };
    }
    return null;
  }
  return null;
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
  label.hidden = !box;
  if (box) {
    label.textContent = box.out ? "Close" : "Open";
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
  const { box, side } = pick(event) ?? {};
  if (box) {
    setOut(box, !box.out, side);
  }
});

for (const button of document.querySelectorAll("[data-view]")) {
  button.addEventListener("click", () => {
    view(button.dataset.view);
    if (button.dataset.view === "reset") for (const box of boxes) if (box.out) setOut(box, false);
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
        axis: new THREE.Vector3(...(x.pull_axis ?? [0, 0, 1])).normalize(),
        travel: x.travel ?? 0.4,
        back: (x.sides ?? ["front"]).includes("back"),
        home: o.position.clone(),
        materials,
        out: false,
        t: 1,
      });
    }
  });
  root.updateMatrixWorld(true);
  for (const box of boxes) {
    const world = new THREE.Box3().setFromObject(box.node).getCenter(new THREE.Vector3());
    box.centre = box.node.parent.worldToLocal(world);
  }

  const bounds = new THREE.Box3().setFromObject(root);
  const sphere = bounds.getBoundingSphere(new THREE.Sphere());
  centre = sphere.center;
  radius = sphere.radius;

  const floorY = bounds.min.y;
  const ground = new THREE.Mesh(
    new THREE.CircleGeometry(radius * 4, 64).rotateX(-Math.PI / 2),
    new THREE.MeshStandardMaterial({ color: 0x737373, roughness: 0.85 }),
  );
  ground.position.set(centre.x, floorY, centre.z);
  ground.receiveShadow = true;
  scene.add(ground);
  sun.target.position.copy(centre);
  sun.position.copy(centre).add(new THREE.Vector3(-1.5, 4, 3));
  const cam = sun.shadow.camera;
  cam.left = cam.bottom = -radius * 1.5;
  cam.right = cam.top = radius * 1.5;
  cam.near = 0.1;
  cam.far = 10;
  cam.updateProjectionMatrix();

  const litres = levels.reduce((sum, l) => sum + frame.columns * box_models[model_boxes[l.class]].volume_l, 0);
  const count = levels.length * frame.columns;
  info.textContent = `Storage volume ${litres} l in ${count} boxes`;
  resize();
  view("three");
  tween.step(1);
  tween = null;
}

initClips();
load().catch((error) => {
  info.textContent = `The model could not be loaded: ${error.message}`;
  console.error(error);
});
