// Re-renderiza los videos ya hechos de salida/ (no los subidos) para que el nombre lo diga la voz en inglés.
// Toma los lotes del "Plan: nombre en inglés" de CHECKLIST.md, en orden, y conserva el nombre del archivo (OC_ sigue OC_).
//
//   node plantilla/revoz-en.mjs                 el próximo lote (10 videos)
//   node plantilla/revoz-en.mjs --lotes=3       los próximos 3 lotes
//   node plantilla/revoz-en.mjs --todos         todo lo pendiente
//   node plantilla/revoz-en.mjs --paralelo=2    cuántos make-exercise a la vez (default 3; más hace fallar el navegador)
//   node plantilla/revoz-en.mjs slug1 slug2     solo esos
//
// Cada video: voz nueva + index.html + check + miniatura + render, sin snapshots (la imagen no cambia).
// La salida de cada uno queda en videos/<slug>/revoz.log.
import { spawn, spawnSync } from "node:child_process";
import { createWriteStream, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "..");
const args = process.argv.slice(2);
const opt = (k, d) => Number((args.find((a) => a.startsWith(`--${k}=`)) || "").split("=")[1]) || d;
const MAKE = join(HERE, "make-exercise.mjs");

spawnSync("node", [MAKE, "--checklist"], { cwd: ROOT, stdio: "inherit" });
const md = readFileSync(join(ROOT, "CHECKLIST.md"), "utf8");
const lotes = [...md.matchAll(/^- \*\*Lote \d+:\*\* (.+)$/gm)].map((m) =>
  m[1].split(", ").map((s) => {
    const [, slug, archivo] = s.match(/^(\S+)(?: \((\S+)\))?$/);
    return { slug, archivo };
  }));
const pick = args.filter((a) => !a.startsWith("--"));
let cola = pick.length
  ? lotes.flat().filter((v) => pick.includes(v.slug))
  : (args.includes("--todos") ? lotes : lotes.slice(0, opt("lotes", 1))).flat();
if (!cola.length) {
  console.log("No hay videos pendientes de nombre en inglés.");
  process.exit(0);
}
console.log(`Re-render con nombre en inglés: ${cola.length} videos, de a ${opt("paralelo", 3)}`);

const run = ({ slug, archivo }) => new Promise((ok) => {
  // Prefijo del archivo actual: "OC_slug.mp4" → --prefijo=OC
  const pre = archivo?.endsWith(`_${slug}.mp4`) ? archivo.slice(0, -slug.length - 5) : "";
  const a = [MAKE, slug, "--render", "--no-snapshot", ...(pre ? [`--prefijo=${pre}`] : [])];
  const log = createWriteStream(join(ROOT, "videos", slug, "revoz.log"));
  const t0 = Date.now();
  const p = spawn("node", a, { cwd: ROOT, shell: false });
  p.stdout.pipe(log); p.stderr.pipe(log);
  p.on("close", (code) => {
    const min = ((Date.now() - t0) / 60000).toFixed(1);
    console.log(`${code === 0 ? "✓" : "✗"} ${archivo || slug + ".mp4"} (${min} min)${code === 0 ? "" : ` — ver videos/${slug}/revoz.log`}`);
    ok({ slug, ok: code === 0 });
  });
});

const res = [];
const worker = async () => { while (cola.length) res.push(await run(cola.shift())); };
await Promise.all(Array.from({ length: opt("paralelo", 3) }, worker));
spawnSync("node", [MAKE, "--checklist"], { cwd: ROOT, stdio: "inherit" });
const bad = res.filter((r) => !r.ok);
console.log(`Listo: ${res.length - bad.length} bien${bad.length ? `, fallaron: ${bad.map((r) => r.slug).join(", ")}` : ""}`);
