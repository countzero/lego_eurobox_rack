// The rack viewer. It relies only on the node names and extras of
// docs/design.md → *Model objects and the web export*.
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import packed from "rack-model";
import { frame, levels, model_boxes, box_models } from "../../design/rack.json";
import { addClipMaterials, initClips } from "./clips.js";
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
let centre = new THREE.Vector3();
let radius = 1;
let tween = null;

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
  for (const box of boxes) {
    if (box.t >= 1) continue;
    box.t = Math.min(1, box.t + dt / 0.45);
    box.node.position.lerpVectors(box.from, box.to, ease(box.t));
    renderer.shadowMap.needsUpdate = true;
    busy = true;
  }
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
  redraw();
}

initClips();
load().catch((error) => {
  info.textContent = `The model could not be loaded: ${error.message}`;
  console.error(error);
});
