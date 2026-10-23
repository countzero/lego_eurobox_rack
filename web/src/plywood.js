// Oiled birch plywood for the top plate, a GLSL port of add_plywood in
// blender/build_rack.py. Coordinates are the plate's local ones in metres
// (y up from the plate's bottom, grain along x), from userData.plywood.
import * as THREE from "three";

const linear = (hex) => new THREE.Color(hex);

const NOISE = /* glsl */ `
varying vec3 vPlyPos;
varying vec3 vPlyNormal;
uniform vec3 plyFaceDark, plyFaceLight, plyGrain, plyLong, plyCross, plyGlue;
uniform float plyT, plyGrainFreq, plyGlueWidth;
float plyHash(vec3 p) {
  p = fract(p * 0.3183099 + 0.1);
  p *= 17.0;
  return fract(p.x * p.y * p.z * (p.x + p.y + p.z));
}
float plyNoise(vec3 x) {
  vec3 i = floor(x), f = fract(x);
  f = f * f * (3.0 - 2.0 * f);
  return mix(mix(mix(plyHash(i), plyHash(i + vec3(1, 0, 0)), f.x),
                 mix(plyHash(i + vec3(0, 1, 0)), plyHash(i + vec3(1, 1, 0)), f.x), f.y),
             mix(mix(plyHash(i + vec3(0, 0, 1)), plyHash(i + vec3(1, 0, 1)), f.x),
                 mix(plyHash(i + vec3(0, 1, 1)), plyHash(i + vec3(1, 1, 1)), f.x), f.y), f.z);
}
float plyFbm(vec3 x) {
  return 0.5 * plyNoise(x) + 0.3 * plyNoise(x * 2.03) + 0.2 * plyNoise(x * 4.01);
}
// Detail finer than about a pixel fades to its mean, so the plate does not
// shimmer when seen from afar; fwidth gives the pattern's change per pixel.
float plyFade(float perPixel) {
  return 1.0 - smoothstep(0.25, 0.6, perPixel);
}
vec3 plyColour() {
  vec3 p = vPlyPos;
  if (abs(vPlyNormal.y) > 0.9) {
    float figure = smoothstep(0.3, 0.7, plyFbm(vec3(p.x * 1.5, p.y * 25.0, p.z * 25.0)));
    vec3 c = mix(plyFaceDark, plyFaceLight, figure);
    vec3 f = vec3(p.x * 25.0, p.y * 2500.0, p.z * 2500.0);
    float fibre = smoothstep(0.35, 0.7, plyNoise(f)) * plyFade(fwidth(f.z));
    c = mix(c, plyFaceLight, fibre * 0.18);
    float wobble = (plyFbm(vec3(p.x * 4.0, 0.0, p.z * 40.0)) - 0.5) * 2.5;
    float arg = p.z * plyGrainFreq + wobble * 6.2832;
    float wave = 0.5 + 0.5 * sin(arg);
    float line = mix(0.05, smoothstep(0.9, 0.99, wave), plyFade(fwidth(arg) / 6.2832));
    return mix(c, plyGrain, line * 0.35);
  }
  float w = plyNoise(vec3(p.x * 40.0, 0.0, p.z * 40.0)) - 0.5;
  float ply = (p.y + w * 0.3 * plyT) / plyT;
  float index = floor(ply);
  float parity = mod(index, 2.0);
  vec3 c = mix(plyLong, plyCross, parity);
  c = mix(c, plyCross, plyHash(vec3(index, 3.1, 7.7)) * 0.35);
  float half_ = plyNoise(vec3(p.x * 80.0, 1.0, p.z * 80.0)) * plyGlueWidth + plyGlueWidth * 0.25;
  float dist = abs(fract(ply) - 0.5);
  float glue = smoothstep(-0.03, 0.03, dist - (0.5 - half_));
  c = mix(c, plyGlue, glue);
  vec3 mean = mix(mix(plyLong, plyCross, 0.6), plyGlue, plyGlueWidth * 1.25);
  return mix(mean, c, plyFade(fwidth(ply)));
}
`;

export function applyPlywood(mesh, spec) {
  const material = mesh.material.clone();
  material.color.set(0xffffff);
  material.map = null;
  material.roughness = 0.55;
  material.metalness = 0;
  const uniforms = {
    plyFaceDark: { value: linear(spec.face_dark) },
    plyFaceLight: { value: linear(spec.face_light) },
    plyGrain: { value: linear(spec.grain) },
    plyLong: { value: linear(spec.ply_long) },
    plyCross: { value: linear(spec.ply_cross) },
    plyGlue: { value: linear(spec.glue) },
    plyT: { value: spec.thickness / 1000 / spec.plies },
    plyGrainFreq: { value: (2 * Math.PI) / ((spec.grain_spacing_mm ?? 5) / 1000) },
    plyGlueWidth: { value: spec.glue_width ?? 0.15 },
  };
  material.onBeforeCompile = (shader) => {
    Object.assign(shader.uniforms, uniforms);
    shader.vertexShader = shader.vertexShader
      .replace("#include <common>", "#include <common>\nvarying vec3 vPlyPos;\nvarying vec3 vPlyNormal;")
      .replace("#include <begin_vertex>", "#include <begin_vertex>\nvPlyPos = position;\nvPlyNormal = normal;");
    shader.fragmentShader = shader.fragmentShader
      .replace("#include <common>", `#include <common>\n${NOISE}`)
      .replace("#include <color_fragment>", "#include <color_fragment>\ndiffuseColor.rgb *= plyColour();");
  };
  material.customProgramCacheKey = () => "plywood";
  mesh.material = material;
}
