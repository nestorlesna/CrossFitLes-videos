// Registra un corto ya subido a YouTube: mueve <slug>.corto.mp4 y <slug>.corto.youtube.txt a salida/subidos/EnYoutube/,
// anota la fila en cortos-subidos.csv y regenera el CHECKLIST.
//   node plantilla/corto-subido.mjs <slug> <videoId> [--lista="Videos cortos de ejercicios"] [--vis=privado|publico]
//   node plantilla/corto-subido.mjs <slug> --vis=publico        (solo actualiza la visibilidad en el registro)
import { existsSync, mkdirSync, renameSync, readFileSync, writeFileSync, appendFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2);
const flag = (n, d) => (args.find((a) => a.startsWith(`--${n}=`)) || "").slice(n.length + 3) || d;
const [slug, videoId] = args.filter((a) => !a.startsWith("--"));
if (!slug) { console.error("uso: node plantilla/corto-subido.mjs <slug> <videoId> [--lista=...] [--vis=privado|publico]"); process.exit(1); }

const CSV = join(ROOT, "cortos-subidos.csv");
const HEAD = "slug;fecha;url;lista;visibilidad";
const filas = existsSync(CSV) ? readFileSync(CSV, "utf8").replace(/\r/g, "").split("\n").filter(Boolean).slice(1) : [];
const i = filas.findIndex((l) => l.startsWith(`${slug};`));
const hoy = new Date().toISOString().slice(0, 10);
const vis = flag("vis", "privado");

if (videoId) {
  const dest = join(ROOT, "salida", "subidos", "EnYoutube");
  mkdirSync(dest, { recursive: true });
  for (const ext of ["corto.mp4", "corto.youtube.txt"]) {
    const src = join(ROOT, "salida", `${slug}.${ext}`);
    if (existsSync(src)) renameSync(src, join(dest, `${slug}.${ext}`));
    else if (!existsSync(join(dest, `${slug}.${ext}`))) console.warn(`⚠ no encuentro ${slug}.${ext}`);
  }
  const fila = `${slug};${hoy};https://youtu.be/${videoId};${flag("lista", "Videos cortos de ejercicios")};${vis}`;
  if (i >= 0) filas[i] = fila; else filas.push(fila);
} else if (i >= 0) {
  const c = filas[i].split(";"); c[4] = vis; filas[i] = c.join(";");
} else { console.error(`${slug} no está en cortos-subidos.csv`); process.exit(1); }

writeFileSync(CSV, [HEAD, ...filas].join("\n") + "\n", "utf8");
console.log(`✓ ${slug} registrado (${vis})`);
spawnSync("node", [join(ROOT, "plantilla", "make-exercise.mjs"), "--checklist"], { stdio: "inherit", cwd: ROOT });
