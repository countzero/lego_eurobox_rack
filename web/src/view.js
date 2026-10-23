// Renderer, lights, camera, controls and the two render paths
// (docs/web_viewer.md → *Performance*).
import {
  Color, DirectionalLight, HalfFloatType, HemisphereLight, MOUSE, PCFShadowMap, PMREMGenerator, PerspectiveCamera, Scene,
  WebGLRenderer, WebGLRenderTarget,
} from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { TAARenderPass } from "three/addons/postprocessing/TAARenderPass.js";
import { BlenderAgXToneMapping } from "./agx.js";

/** Jittered samples a still frame gathers: TAARenderPass's fixed pattern, one
 *  per animation frame. */
export const TAA_SAMPLES = 32;

/** MSAA samples of a frame in motion. */
export const MOVING_SAMPLES = 4;

/** Pixels per CSS pixel: a still frame at the screen's own, a frame in motion at
 *  most 1, since pixel count dominates on an integrated GPU; the samples per
 *  pixel are kept instead. On a touch screen the still frame is at most 1 too,
 *  to spare a phone's GPU. */
export const pixelRatio = (still) => (still && !matchMedia("(pointer: coarse)").matches
  ? window.devicePixelRatio : Math.min(window.devicePixelRatio, 1));

export function createView(canvas) {
  // The canvas stays at the screen's resolution and only receives finished
  // frames, so it is never resized between a moving and a still frame. Hence
  // no MSAA of its own either.
  const renderer = new WebGLRenderer({ canvas, antialias: false, powerPreference: "high-performance" });
  renderer.setPixelRatio(pixelRatio(true));
  renderer.toneMapping = BlenderAgXToneMapping;
  renderer.toneMappingExposure = 1.0;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = PCFShadowMap;
  // Redrawn only when something that casts a shadow has moved (needsUpdate).
  renderer.shadowMap.autoUpdate = false;

  const scene = new Scene();
  // OutputPass tone-maps the background too: AgX Punchy shows #b6b6b6 as the
  // #8c8c8c the contrast ratios of docs/accessibility.md are measured against.
  scene.background = new Color(0xb6b6b6);
  // The aluminium is a full metal and only shows what it reflects; a procedural
  // room gives it something to reflect without loading a file.
  const pmrem = new PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.25;
  pmrem.dispose();
  scene.add(new HemisphereLight(0xffffff, 0x5a5a5a, 0.15));
  const sun = new DirectionalLight(0xffffff, 2.6);
  sun.position.set(-1.5, 4, 3);
  sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048);
  sun.shadow.bias = -0.0005;
  sun.shadow.normalBias = 0.01;
  scene.add(sun, sun.target);

  const camera = new PerspectiveCamera(35, 1, 0.01, 100);
  const controls = new OrbitControls(camera, canvas);
  // No damping: the view stops with the hand, nothing glides on after it.
  controls.enableDamping = false;
  // The wheel already zooms, so the middle button pans as in CAD tools rather
  // than zooming a second time.
  controls.mouseButtons.MIDDLE = MOUSE.PAN;

  // Half float, so the tone mapping in OutputPass gets the light unclipped.
  // A frame in motion: MSAA at the lower ratio, stretched onto the canvas.
  const moving = new EffectComposer(renderer,
    new WebGLRenderTarget(1, 1, { type: HalfFloatType, samples: MOVING_SAMPLES }));
  moving.addPass(new RenderPass(scene, camera));
  moving.addPass(new OutputPass());
  // A still frame: jittered samples gathered over frames, which smooth the
  // edges in place of MSAA.
  const composer = new EffectComposer(renderer,
    new WebGLRenderTarget(1, 1, { type: HalfFloatType }));
  const taa = new TAARenderPass(scene, camera);
  taa.accumulate = true;
  // The pass leaves the first frame it blends the samples over at its old size.
  const taaSetSize = taa.setSize.bind(taa);
  taa.setSize = (w, h) => {
    taaSetSize(w, h);
    taa._holdRenderTarget?.setSize(w, h);
  };
  composer.addPass(taa);
  composer.addPass(new OutputPass());

  function resize() {
    const { clientWidth: w, clientHeight: h } = canvas;
    renderer.setPixelRatio(pixelRatio(true));
    renderer.setSize(w, h, false);
    for (const [c, still] of [[moving, false], [composer, true]]) {
      c.setPixelRatio(pixelRatio(still));
      c.setSize(w, h);
    }
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }

  return { renderer, scene, camera, controls, sun, moving, composer, taa, resize };
}
