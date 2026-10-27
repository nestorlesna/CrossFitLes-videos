// Analizar un video de YouTube que se va a replicar como video largo animado.
//   node plantilla/largo/fuente.mjs <slug> <url-de-youtube> [--cada=5] [--en]   (--en: subtítulos en inglés)
// Deja en videos-largos/fuentes/<slug>/:
//   transcripcion.txt   subtítulos (manuales o automáticos) con minuto:segundo, una línea por frase
//   info.json           título, canal, duración, url (sin la descripción del canal)
//   _frames/hoja-N.jpg  hojas de fotogramas cada --cada segundos (default 5) con el tiempo impreso — NO van a git
// Requiere yt-dlp y ffmpeg. El video bajado (baja resolución) queda en _frames/ y tampoco va a git: solo sirve para
// mirar las posturas; nunca se usa su audio ni su imagen en nuestro video.
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
const [slug, url] = process.argv.slice(2).filter((a) => !a.startsWith("--"));
const cada = Number((process.argv.find((a) => a.startsWith("--cada=")) || "--cada=5").slice(7));
if (!slug || !url) { console.error("uso: node plantilla/largo/fuente.mjs <slug> <url> [--cada=5]"); process.exit(1); }
const OUT = join(ROOT, "videos-largos", "fuentes", slug), FR = join(OUT, "_frames");
mkdirSync(FR, { recursive: true });
const run = (cmd, a, cwd) => { const r = spawnSync(cmd, a, { cwd, encoding: "utf8" }); if (r.status !== 0) console.error(r.stderr?.slice(-800)); return r.status === 0; };

// 1. Subtítulos + info (preferencia: subtítulo original en castellano, después el automático)
run("yt-dlp", ["--ignore-errors", "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", process.argv.includes("--en") ? "en.*" : "es.*", "--sub-format", "vtt", "--write-info-json", "-o", "src", url], FR);
const vtts = readdirSync(FR).filter((f) => f.endsWith(".vtt"));
const vtt = ["src.es-orig.vtt", "src.es.vtt", ...vtts].find((f) => vtts.includes(f));
if (vtt) {
  const res = [];
  let t = null, last = "";
  for (const l of readFileSync(join(FR, vtt), "utf8").split(/\r?\n/)) {
    const m = l.match(/^(\d+):(\d+):(\d+)\.\d+ -->/);
    if (m) { t = +m[1] * 3600 + +m[2] * 60 + +m[3]; continue; }
    const txt = l.replace(/<[^>]+>/g, "").trim();
    if (t == null || !txt || /^(WEBVTT|Kind:|Language:)/.test(l) || txt === last) continue;
    res.push(`[${String(Math.floor(t / 60)).padStart(2, "0")}:${String(t % 60).padStart(2, "0")}] ${txt}`);
    last = txt;
  }
  writeFileSync(join(OUT, "transcripcion.txt"), `# ${url} — subtítulo ${vtt.replace("src.", "")}\n${res.join("\n")}\n`);
  console.log(`✓ transcripcion.txt (${res.length} líneas, ${vtt})`);
} else console.log("⚠ el video no tiene subtítulos: hay que guiarse solo por los fotogramas");
if (existsSync(join(FR, "src.info.json"))) {
  const d = JSON.parse(readFileSync(join(FR, "src.info.json"), "utf8"));
  writeFileSync(join(OUT, "info.json"), JSON.stringify({ url, titulo: d.title, canal: d.channel, duracion: d.duration, idioma: d.language, capitulos: d.chapters || null }, null, 2));
  console.log(`✓ info.json — "${d.title}" (${d.channel}, ${Math.floor(d.duration / 60)}:${String(d.duration % 60).padStart(2, "0")})`);
}

// 2. Video en baja resolución → un fotograma cada `cada` s con el tiempo → hojas de 8×5 (200 s por hoja con cada=5)
if (run("yt-dlp", ["-f", "worst[height>=240]/worst", "-o", "video.%(ext)s", url], FR)) {
  const vid = readdirSync(FR).find((f) => f.startsWith("video."));
  const tmp = join(FR, "f");
  rmSync(tmp, { recursive: true, force: true });
  mkdirSync(tmp);
  run("ffmpeg", ["-loglevel", "error", "-i", vid, "-vf", `fps=1/${cada},scale=320:-1,drawtext=text='%{pts\\:hms}':x=5:y=5:fontcolor=yellow:fontsize=18:box=1:boxcolor=black`, "f/%04d.jpg"], FR);
  const n = readdirSync(tmp).length;
  for (let i = 0; i * 40 < n; i++) run("ffmpeg", ["-loglevel", "error", "-y", "-start_number", String(i * 40 + 1), "-i", "f/%04d.jpg", "-frames:v", "1", "-vf", "tile=8x5", `hoja-${i + 1}.jpg`], FR);
  rmSync(tmp, { recursive: true, force: true });
  console.log(`✓ ${Math.ceil(n / 40)} hojas de fotogramas en videos-largos/fuentes/${slug}/_frames/ (cada ${cada} s)`);
}
console.log("Siguiente: escribir videos-largos/fuentes/" + slug + "/analisis.md (ver GENERAR_VIDEOS_LARGOS.md §2)");
