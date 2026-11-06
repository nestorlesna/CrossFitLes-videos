// Genera salida/<slug>.corto.youtube.txt (título + descripción + tags) del video corto, a partir del
// <slug>.youtube.txt del largo (en salida/ o en salida/subidos/**).
//   node plantilla/corto-youtube.mjs <slug> [<slug> …]      uno o varios
//   node plantilla/corto-youtube.mjs --todos                 todos los cortos que no tienen su txt
import { existsSync, readFileSync, writeFileSync, readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { idLargo } from "./vincular.mjs";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const SALIDA = join(ROOT, "salida");

function walk(d) {
  return readdirSync(d, { withFileTypes: true }).flatMap((e) => (e.isDirectory() ? walk(join(d, e.name)) : [join(d, e.name)]));
}
const findFile = (name) => {
  const p = join(SALIDA, name);
  if (existsSync(p)) return p;
  return walk(join(SALIDA, "subidos")).find((f) => f.endsWith(`/${name}`) || f.endsWith(`\\${name}`)) || null;
};

function section(txt, head, next) {
  const m = txt.match(new RegExp(`^${head}\\s*\\n([\\s\\S]*?)(?=\\n${next}\\s*\\n|(?![\\s\\S]))`, "m"));
  return m ? m[1].trim() : "";
}

export function cortoYoutube(slug) {
  const src = findFile(`${slug}.youtube.txt`);
  if (!src) throw new Error(`no hay ${slug}.youtube.txt del largo`);
  const t = readFileSync(src, "utf8").replace(/\r/g, "");
  const titulo = section(t, "TÍTULO", "DESCRIPCIÓN").split("\n")[0];
  const desc = section(t, "DESCRIPCIÓN", "TAGS");
  const tags = section(t, "TAGS", "\\0");
  // nombre = lo que está antes del primer emoji / «·»; categoría = lo que sigue al último « | »
  const specP = join(ROOT, "ejercicios", `${slug}.json`);
  const nombreFicha = existsSync(specP) ? JSON.parse(readFileSync(specP, "utf8")).name : "";
  const nombre = nombreFicha || titulo.split(/\s+(?=[^\p{L}\p{N}\s\-'’()/&,.+]| · | \| )/u)[0].replace(/\s*[·|].*$/, "").trim();
  const cat = (titulo.match(/\|\s*([^|]+)$/) || [])[1]?.trim() || "";
  const trabaja = (desc.match(/QUÉ TRABAJA\s*\n(.+)/) || [])[1]?.trim() || "";
  const hashtags = (desc.match(/^(#\S+(?:\s+#\S+)*)\s*$/m) || [])[1] || "";
  const largoId = idLargo(slug); // del calendario o de vinculos.csv; si no se conoce, línea genérica (se completa al vincular)
  const linkLargo = largoId ? `▶️ Explicación paso a paso con Daniela: https://youtu.be/${largoId}` : "📺 La explicación paso a paso, con la voz de Daniela, está en el video completo de este ejercicio en el canal.";
  let titleOut = `${nombre} 🎬 Así se hace en segundos${cat ? ` | ${cat}` : ""} #Shorts`;
  if (titleOut.length > 100) titleOut = `${nombre} 🎬 Así se hace #Shorts`.slice(0, 100);
  const out = `TÍTULO
${titleOut}

DESCRIPCIÓN
🎬 ${nombre.toUpperCase()} — mirá cómo se hace, en pocos segundos.
${trabaja ? `\n🎯 QUÉ TRABAJA\n${trabaja}\n` : ""}
${linkLargo}

🙌 Si te sirvió, dejá tu like, guardalo y compartilo con tu compañero de box.

⚠️ Este video es educativo y no reemplaza la indicación de un profesional. Si tenés una lesión o dolor, consultá primero con tu médico o kinesiólogo. Entrenás bajo tu propia responsabilidad.

${hashtags ? `${hashtags} #Shorts` : "#CrossFit #Shorts"}

TAGS
${tags}
`;
  writeFileSync(join(SALIDA, `${slug}.corto.youtube.txt`), out, "utf8");
  return titleOut;
}

const args = process.argv.slice(2);
let slugs = args.filter((a) => !a.startsWith("--"));
if (args.includes("--todos")) {
  slugs = walk(SALIDA).map((f) => f.replace(/\\/g, "/").split("/").pop()).filter((n) => n.endsWith(".corto.mp4")).map((n) => n.slice(0, -10));
  slugs = [...new Set(slugs)].filter((s) => !existsSync(join(SALIDA, `${s}.corto.youtube.txt`)));
}
for (const s of slugs) {
  try { console.log(`${s}: ${cortoYoutube(s)}`); } catch (e) { console.log(`${s}: ✗ ${e.message}`); }
}
