// Bundles the viewer, three.js and rack.glb into one self-contained HTML file
// (docs/web_viewer.md → *Building*).
import * as esbuild from "esbuild";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { deflateRawSync } from "node:zlib";

const here = dirname(fileURLToPath(import.meta.url));
const out = join(here, "dist", "index.html");
const glb = process.env.RACK_GLB ? resolve(process.env.RACK_GLB) : join(here, "rack.glb");

if (!existsSync(glb)) {
  console.error(`[build] ${glb} is missing: export it with blender/build_rack.py or set RACK_GLB`);
  process.exit(1);
}

const licences = [["three", "LICENSE"], ["@awesome.me/webawesome", "LICENSE.md"], ["@fortawesome/fontawesome-free", "LICENSE.txt"]].map(([name, file]) => {
  const pkg = JSON.parse(readFileSync(join(here, "node_modules", name, "package.json"), "utf8"));
  const text = readFileSync(join(here, "node_modules", name, file), "utf8").trim();
  return `${name} ${pkg.version}\n\n${text}`;
});
// three ships meshoptimizer's decoder under meshoptimizer's own licence, which
// its first two lines name.
licences.push(readFileSync(join(here, "node_modules", "three", "examples", "jsm", "libs", "meshopt_decoder.module.js"), "utf8")
  .split("\n").slice(0, 2).map((l) => l.replace(/^\/\/ /, "")).join("\n"));

// docs/roadmap.md → 0021: the model, deflated as it goes into the page.
const MODEL_LIMIT_KB = 110;

function page(js, css) {
  const template = readFileSync(join(here, "src", "index.html"), "utf8");
  // A literal "</script" inside the bundle would end the script element early.
  const safeJs = js.replace(/<\/script/gi, "<\\/script");
  // Inline, since a file opened by double-click has no server to fetch it from.
  const favicon = encodeURIComponent(readFileSync(join(here, "src", "favicon.svg"), "utf8").trim());
  return template
    .replace("<!-- FAVICON -->", `<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,${favicon}">`)
    .replace("<!-- LICENCES -->", () => `<!--\nBundled third-party software:\n\n${licences.join("\n\n")}\n-->`)
    .replace("/* CSS */", () => css)
    .replace("/* JS */", () => safeJs);
}

// main.js imports "rack-model"; it resolves to the GLB, inlined deflated.
const model = {
  name: "rack-model",
  setup(b) {
    b.onResolve({ filter: /^rack-model$/ }, () => ({ path: glb }));
    b.onLoad({ filter: /\.glb$/ }, ({ path }) => {
      const raw = readFileSync(path);
      const contents = deflateRawSync(raw, { level: 6 });
      const kb = contents.length / 1e3;
      console.log(`[build] ${path}: ${(raw.length / 1e3).toFixed(0)} kB, deflated ${kb.toFixed(0)} kB`);
      if (!process.env.RACK_GLB && kb > MODEL_LIMIT_KB) {
        return { errors: [{ text: `rack.glb deflated is ${kb.toFixed(0)} kB, above the limit of ${MODEL_LIMIT_KB} kB` }] };
      }
      return { contents, loader: "binary", watchFiles: [path] };
    });
  },
};

const options = {
  entryPoints: [join(here, "src", "main.js")],
  plugins: [model],
  loader: { ".svg": "text" },
  bundle: true,
  minify: true,
  format: "iife",
  target: "es2020",
  write: false,
  outdir: join(here, "dist"),
  legalComments: "none",
  logLevel: "info",
};

function emit(result) {
  const js = result.outputFiles.find((f) => f.path.endsWith(".js")).text;
  const css = result.outputFiles.find((f) => f.path.endsWith(".css"))?.text ?? "";
  mkdirSync(dirname(out), { recursive: true });
  writeFileSync(out, page(js, css));
  console.log(`[build] wrote ${out} (${(readFileSync(out).length / 1e3).toFixed(0)} kB)`);
}

if (process.argv.includes("--watch")) {
  const ctx = await esbuild.context({
    ...options,
    plugins: [...options.plugins, { name: "emit", setup(b) { b.onEnd((r) => r.errors.length || emit(r)); } }],
  });
  await ctx.watch();
} else {
  emit(await esbuild.build(options));
}
