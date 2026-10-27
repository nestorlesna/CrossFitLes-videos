// Videos largos 16:9 (rutinas guiadas, explicaciones largas): videos-largos/fichas/<slug>.json → videos-largos/salida/
//
//   node plantilla/largo/make-largo.mjs <slug>              voz + index.html + check + snapshots + miniatura + youtube.txt
//   node plantilla/largo/make-largo.mjs <slug> --render     además renderiza → videos-largos/salida/<slug>.mp4
//   node plantilla/largo/make-largo.mjs <slug> --poses [A,B]  laboratorio de poses (una celda por pose, sin voz)
//   node plantilla/largo/make-largo.mjs <slug> --miniatura  solo la miniatura (1280×720)
//   node plantilla/largo/make-largo.mjs <slug> --youtube    solo el .youtube.txt (usa los capítulos del último build)
//   node plantilla/largo/make-largo.mjs --lista             regenera videos-largos/LISTA.md
//
// Flags: --force-tts · --no-check · --no-snapshot. Procedimiento completo: GENERAR_VIDEOS_LARGOS.md.
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { copyFileSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { basename, dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { collectShots } from "../build-index.mjs";
import { buildLargo, chaptersText, flatScenes } from "./build-largo.mjs";

const HF = process.env.HF_PKG || "hyperframes";
const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "..", "..");
const BASE = join(ROOT, "videos-largos");
const SALIDA = join(BASE, "salida");
const args = process.argv.slice(2);
const has = (f) => args.includes(f);
const slug = args.find((a) => !a.startsWith("--"));

const sh = (cmd, cwd) => {
  console.log(`$ ${cmd}`);
  return spawnSync(cmd, { cwd, shell: true, stdio: "inherit", encoding: "utf8" });
};
const statusPath = (dir) => join(dir, ".pipeline.json");
const readStatus = (dir) => (existsSync(statusPath(dir)) ? JSON.parse(readFileSync(statusPath(dir), "utf8")) : {});
const writeStatus = (dir, patch) => writeFileSync(statusPath(dir), JSON.stringify({ ...readStatus(dir), ...patch }, null, 2));
const today = () => new Date().toISOString().slice(0, 10);
const readSpec = (s) => JSON.parse(readFileSync(join(BASE, "fichas", `${s}.json`), "utf8"));
export function contentHash(spec) {
  const { youtube, miniatura, notas, revisado, fuente, ...rest } = spec;
  return createHash("sha1").update(JSON.stringify(rest)).digest("hex").slice(0, 12);
}

function initProject(dir) {
  if (existsSync(join(dir, "hyperframes.json"))) return;
  const rel = dir.slice(ROOT.length + 1).replace(/\\/g, "/");
  const r = sh(`npx --prefer-offline ${HF} init "${rel}" --non-interactive --example=blank --skill=faceless-explainer`, ROOT);
  if (r.status !== 0) throw new Error("hyperframes init falló");
}

// Voz: Piper + Daniela (es_AR), una línea por escena (id CCSS). Solo se regenera si cambió el texto.
function tts(dir, spec) {
  const { scenes } = flatScenes(spec);
  const request = {
    provider: "piper", lang: "es", speed: spec.voiceSpeed ?? 1.0, voice: spec.voice || "es_AR-daniela-high",
    lines: scenes.filter((f) => f.vo).map((f) => {
      let text = f.vo;
      for (const [from, to] of Object.entries(spec.pronuncia || {})) text = text.split(from).join(to);
      return f.voSpeed ? { id: f.id, text, speed: f.voSpeed } : { id: f.id, text };
    }),
    bgm: { mode: "none" },
  };
  const reqPath = join(dir, "audio_request.json");
  const next = JSON.stringify(request, null, 2);
  if (existsSync(reqPath) && readFileSync(reqPath, "utf8") === next && existsSync(join(dir, "audio_engine_meta.json")) && !has("--force-tts")) {
    console.log("· voz: sin cambios, se reutiliza");
    return true;
  }
  writeFileSync(reqPath, next);
  return sh(`python "${join(HERE, "..", "piper-tts.py")}" audio_request.json audio_engine_meta.json`, dir).status === 0;
}

// Miniatura de YouTube 1280×720: título grande + personaje en la pose de spec.miniatura.
function miniatura(dir, slug) {
  const t = buildLargo(dir, { thumb: true });
  const shots = join(t.dir, "snapshots");
  rmSync(shots, { recursive: true, force: true });
  const r = sh(`npx --prefer-offline ${HF} snapshot . --at ${t.at} --no-end --describe false`, t.dir);
  collectShots(t.dir);
  const png = existsSync(shots) && readdirSync(shots).find((f) => f.endsWith(".png"));
  if (r.status !== 0 || !png) return false;
  mkdirSync(SALIDA, { recursive: true });
  const out = join(SALIDA, `${slug}.miniatura.png`);
  const s = spawnSync("ffmpeg", ["-y", "-loglevel", "error", "-i", join(shots, png), "-vf", "scale=1280:720:flags=lanczos", out]);
  if (s.status !== 0) return false;
  console.log(`✓ videos-largos/salida/${slug}.miniatura.png`);
  return true;
}

const VOICE_CREDIT = "🎙️ Voz: Daniela (Piper TTS, rhasspy/piper-voices), datos de Google OpenSLR 61, licencia CC BY-SA 4.0.";
// videos-largos/salida/<slug>.youtube.txt: título, descripción con capítulos ({{CAPITULOS}}) y crédito de la voz, tags.
function exportYoutube(dir, spec) {
  const yt = spec.youtube;
  const capPath = join(dir, "capitulos.json");
  if (!yt?.descripcion || !existsSync(capPath)) return false;
  const caps = chaptersText(JSON.parse(readFileSync(capPath, "utf8")));
  const lines = yt.descripcion.replace("{{CAPITULOS}}", caps).split("\n"), tags = lines.pop();
  const desc = [...lines, VOICE_CREDIT, "", tags].join("\n");
  mkdirSync(SALIDA, { recursive: true });
  writeFileSync(join(SALIDA, `${spec.slug}.youtube.txt`), ["TÍTULO", yt.titulo, "", "DESCRIPCIÓN", desc, "", "TAGS", (yt.tags || []).join(", "), ""].join("\n"));
  if (desc.length > 5000 || /[<>]/.test(desc)) console.log(`  ⚠ descripción: ${desc.length} caracteres${/[<>]/.test(desc) ? " y tiene < o >" : ""} (YouTube: ≤ 5000, sin < >)`);
  console.log(`✓ videos-largos/salida/${spec.slug}.youtube.txt`);
  return true;
}

// Laboratorio de poses: una escena de 1,4 s por pose, sin voz → proyectos/_poselab/<slug>/snapshots/contact-sheet.jpg
function poseLab(spec, only) {
  const names = only ? only.split(",") : Object.keys(spec.poses);
  const LAB = join(BASE, "proyectos", "_poselab", spec.slug);
  mkdirSync(LAB, { recursive: true });
  const ref = join(ROOT, "videos", "squat-to-stand");
  for (const f of ["hyperframes.json", "meta.json", "package.json"]) writeFileSync(join(LAB, f), readFileSync(join(ref, f)));
  rmSync(join(LAB, "audio_engine_meta.json"), { force: true });
  const lab = { ...spec, music: false, initialPose: names[0], capitulos: [{ titulo: "", head: ["POSES"], numero: false, escenas: names.map((n) => ({ min: 1.4, step: n, moves: [{ cut: n, at: 0 }] })) }] };
  writeFileSync(join(LAB, "guion.json"), JSON.stringify(lab));
  const b = buildLargo(LAB, { lab: true });
  rmSync(join(LAB, "snapshots"), { recursive: true, force: true });
  sh(`npx --prefer-offline ${HF} snapshot . --at ${b.scenes.map((f) => (f.start + 1.2).toFixed(2)).join(",")} --no-end --describe false`, LAB);
  collectShots(LAB);
  console.log(`· ${names.length} poses → videos-largos/proyectos/_poselab/${spec.slug}/snapshots/`);
}

function mp4Duration(file) {
  const r = spawnSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", file], { encoding: "utf8" });
  return r.status === 0 ? Number(r.stdout.trim()) : null;
}

// Última subida de ese mp4 según el log del skill youtube-upload (busca por nombre de archivo): { id, estado } o null.
const UPLOADS_LOG = join(process.env.USERPROFILE || process.env.HOME || "", ".claude", "skills", "youtube-upload", "uploads_log.csv");
function subido(mp4) {
  if (!mp4 || !existsSync(UPLOADS_LOG)) return null;
  const name = basename(mp4).toLowerCase();
  const rows = readFileSync(UPLOADS_LOG, "utf8").split("\n").map((l) => l.trim())
    .filter((l) => l.toLowerCase().includes("videos-largos") && l.toLowerCase().includes(`\\${name},`));
  if (!rows.length) return null;
  const c = rows.at(-1).split(",");
  return { id: c.at(-2), estado: c.at(-1) };
}

// videos-largos/LISTA.md: estado de todos los videos largos (autogenerado).
function lista() {
  const dir = join(BASE, "fichas");
  const fichas = existsSync(dir) ? readdirSync(dir).filter((f) => f.endsWith(".json")) : [];
  const ok = (b) => (b ? "✅" : "⬜");
  const rows = fichas.map((f) => {
    const spec = JSON.parse(readFileSync(join(dir, f), "utf8")), p = join(BASE, "proyectos", spec.slug), st = readStatus(p);
    // después de subir, youtube-upload mueve mp4 + miniatura + txt a salida/subidos/ (y a mano van a subidos/EnYoutube/)
    const sal = (ext) => [SALIDA, join(SALIDA, "subidos"), join(SALIDA, "subidos", "EnYoutube")].map((d) => join(d, `${spec.slug}${ext}`)).find(existsSync);
    const mp4 = sal(".mp4"), rendered = !!mp4, yt = subido(mp4);
    const stale = rendered && st.renderHash && st.renderHash !== contentHash(spec);
    const dur = rendered ? mp4Duration(mp4) : st.duracion;
    const fuente = spec.fuente?.url ? `[${spec.fuente.canal || "original"}](${spec.fuente.url})` : "—";
    return `| ${spec.name} | \`${spec.slug}\` | ${fuente} | ${spec.capitulos.length} | ${ok(st.voz)} | ${st.check == null ? "⬜" : st.check ? "✅" : "❌"} | ${rendered ? (stale ? "⚠️ desactualizado" : "✅") : "⬜"} | ${ok(sal(".miniatura.png"))} | ${yt ? `[${yt.estado}](https://youtu.be/${yt.id})` : ok(sal(".youtube.txt"))} | ${dur ? `${Math.floor(dur / 60)}:${String(Math.round(dur % 60)).padStart(2, "0")}` : "—"} | ${ok(spec.revisado)} | ${st.renderizado || "—"} | ${spec.notas || ""} |`;
  });
  writeFileSync(join(BASE, "LISTA.md"), `# Videos largos (16:9)

Generado por \`node plantilla/largo/make-largo.mjs --lista\` (no editar a mano). Procedimiento: \`GENERAR_VIDEOS_LARGOS.md\`.
Para aprobar un video: \`"revisado": true\` en su ficha (\`videos-largos/fichas/<slug>.json\`).

| Video | Slug | Original | Capítulos | Voz | Check | Render | Miniatura | YouTube | Duración | Revisado | Fecha render | Notas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
${rows.join("\n")}
`);
  console.log(`✓ videos-largos/LISTA.md (${fichas.length} videos)`);
}

function main() {
  if (has("--lista") && !slug) return lista();
  if (!slug) { console.error("uso: node plantilla/largo/make-largo.mjs <slug> [--render | --poses | --miniatura | --youtube] | --lista"); process.exit(1); }
  const spec = readSpec(slug);
  if (has("--poses")) return poseLab(spec, args[args.indexOf("--poses") + 1]?.startsWith("--") ? null : args[args.indexOf("--poses") + 1]);
  const dir = join(BASE, "proyectos", slug);
  initProject(dir);
  copyFileSync(join(BASE, "fichas", `${slug}.json`), join(dir, "guion.json"));
  if (has("--miniatura")) { writeStatus(dir, { miniatura: miniatura(dir, slug) }); return lista(); }
  if (has("--youtube")) { exportYoutube(dir, spec); return lista(); }

  const vozOk = tts(dir, spec);
  writeStatus(dir, { voz: vozOk });
  if (!vozOk) throw new Error("la generación de voz falló");
  const b = buildLargo(dir);
  console.log(`✓ index.html — ${b.chapters.length} capítulos, ${b.scenes.length} escenas, ${Math.floor(b.total / 60)}:${String(Math.round(b.total % 60)).padStart(2, "0")} (${b.total}s), voces ${b.voices}, música ${b.music ? "sí" : "no"}`);
  b.warnings.forEach((w) => console.log(`  ⚠ ${w}`));
  writeStatus(dir, { composicion: true, duracion: b.total });
  exportYoutube(dir, spec);

  if (!has("--no-check")) writeStatus(dir, { check: sh(`npx --prefer-offline ${HF} check`, dir).status === 0 });
  if (!has("--no-snapshot")) {
    sh(`npx --prefer-offline ${HF} snapshot --at ${b.scenes.map((f) => (f.start + f.dur * 0.7).toFixed(2)).join(",")} --describe false`, dir);
    collectShots(dir);
    console.log(`· contact sheets: videos-largos/proyectos/${slug}/snapshots/`);
  }
  writeStatus(dir, { miniatura: miniatura(dir, slug) });
  if (has("--render")) {
    const r = sh(`npx --prefer-offline ${HF} render --skill=faceless-explainer --quality high --output renders/video.mp4`, dir);
    if (r.status !== 0) throw new Error("render falló");
    mkdirSync(SALIDA, { recursive: true });
    copyFileSync(join(dir, "renders", "video.mp4"), join(SALIDA, `${slug}.mp4`));
    writeStatus(dir, { renderizado: today(), renderHash: contentHash(spec) });
    console.log(`✓ videos-largos/salida/${slug}.mp4`);
  }
  lista();
}

main();
