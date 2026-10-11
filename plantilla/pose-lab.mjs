// Laboratorio de poses: dibuja TODAS las poses de una ficha en una sola hoja para ajustarlas rápido.
//   node plantilla/pose-lab.mjs <slug>          → videos/_poselab/snapshots/contact-sheet.jpg (una celda por pose)
//   node plantilla/pose-lab.mjs <slug> A,B,C    → solo esas poses
// Usa los mismos poses/props/rig de ejercicios/<slug>.json, sin voz ni música. El nombre de la pose sale como título.
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { buildIndex } from "./build-index.mjs";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const [slug, only] = process.argv.slice(2);
if (!slug) { console.error("uso: node plantilla/pose-lab.mjs <slug> [POSE,POSE]"); process.exit(1); }
const spec = JSON.parse(readFileSync(join(ROOT, "ejercicios", `${slug}.json`), "utf8"));
const names = only ? only.split(",") : Object.keys(spec.poses);
const LAB = join(ROOT, "videos", "_poselab");
mkdirSync(LAB, { recursive: true });
const ref = join(ROOT, "videos", "squat-to-stand");
for (const f of ["hyperframes.json", "meta.json", "package.json"]) writeFileSync(join(LAB, f), readFileSync(join(ref, f)));
rmSync(join(LAB, "audio_engine_meta.json"), { force: true });
const lab = {
  ...spec, slug: "_poselab", music: false, floorScroll: 0, initialPose: names[0],
  frames: names.map((n) => ({ kind: "step", min: 1.4, badge: "POSE", head: [n], vo: "", moves: [{ cut: n, at: 0 }] })),
};
writeFileSync(join(LAB, "exercise.json"), JSON.stringify(lab));
const b = buildIndex(LAB);
rmSync(join(LAB, "snapshots"), { recursive: true, force: true });
const at = b.frames.map((f) => (f.start + 1.2).toFixed(2)).join(",");
spawnSync(`npx hyperframes snapshot . --at ${at} --no-end --describe false`, { cwd: LAB, shell: true, stdio: "inherit" });
console.log(`· ${names.length} poses → videos/_poselab/snapshots/contact-sheet.jpg`);
