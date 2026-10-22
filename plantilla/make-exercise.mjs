// One command per exercise: ejercicios/<slug>.json → videos/<slug>/ → salida/<slug>.mp4 + CHECKLIST.md
//
//   node plantilla/make-exercise.mjs <slug>            crea/actualiza proyecto, voz, index.html, check y snapshots
//   node plantilla/make-exercise.mjs <slug> --render   además renderiza y copia a salida/<slug>.mp4
//   node plantilla/make-exercise.mjs --checklist       solo regenera CHECKLIST.md (+ salida/<slug>.youtube.txt)
//   node plantilla/make-exercise.mjs <slug> --miniatura  solo regenera salida/<slug>.miniatura.png (miniatura de YouTube)
//   node plantilla/make-exercise.mjs <slug> --info     muestra la fila de ejercicios/ejercicios.csv o maquinas.csv (datos para la ficha)
//
// Flags: --force-tts (regenera la voz aunque el texto no cambió) · --no-check · --no-snapshot
//        --prefijo=OC (con --render: el video sale como salida/OC_<slug>.mp4; sin prefijo, salida/<slug>.mp4)
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { copyFileSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { buildIndex, collectShots } from "./build-index.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "..");
const ENGINE = join(ROOT, ".claude", "skills", "media-use", "audio", "scripts", "audio.mjs");
const args = process.argv.slice(2);
const has = (f) => args.includes(f);
const slug = args.find((a) => !a.startsWith("--"));
// Prefijo opcional del .mp4 (lo pide el usuario según la herramienta que genera: OC_ = opencode, etc.).
const PREFIJO = (args.find((a) => a.startsWith("--prefijo=")) || "").slice(10).replace(/[^A-Za-z0-9-]/g, "");
const mp4Name = (s) => `${PREFIJO ? `${PREFIJO}_` : ""}${s}.mp4`;

const sh = (cmd, cwd, inherit = true) => {
  console.log(`$ ${cmd}`);
  const r = spawnSync(cmd, { cwd, shell: true, stdio: inherit ? "inherit" : "pipe", encoding: "utf8" });
  return r;
};
const statusPath = (dir) => join(dir, ".pipeline.json");
const readStatus = (dir) => (existsSync(statusPath(dir)) ? JSON.parse(readFileSync(statusPath(dir), "utf8")) : {});
const writeStatus = (dir, patch) => writeFileSync(statusPath(dir), JSON.stringify({ ...readStatus(dir), ...patch }, null, 2));
const today = () => new Date().toISOString().slice(0, 10);

// Lista maestra de ejercicios (export de la app del box): ejercicios/ejercicios.csv, ";" con comillas, UTF-8 con BOM.
// El orden de las filas es el orden en que se van a hacer los videos.
// readCsv("maquinas.csv"): lista de videos de máquinas de gimnasio (sale de maquinas_gimnasio.xlsx, una fila por video).
export function readCsv(name = "ejercicios.csv") {
  const file = join(ROOT, "ejercicios", name);
  if (!existsSync(file)) return [];
  const t = readFileSync(file, "utf8").replace(/^﻿/, "");
  const rows = [];
  let row = [], f = "", q = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (q) {
      if (c === '"') { if (t[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += c;
    } else if (c === '"') q = true;
    else if (c === ";") { row.push(f); f = ""; }
    else if (c === "\n") { row.push(f.replace(/\r$/, "")); rows.push(row); row = []; f = ""; }
    else f += c;
  }
  if (f || row.length) { row.push(f); rows.push(row); }
  const [head, ...data] = rows;
  return data.filter((r) => r.length > 1 && r[0]).map((r) => Object.fromEntries(head.map((k, i) => [k, (r[i] || "").trim()])));
}

// Huella de lo que se ve/escucha en el video: cambiar youtube, miniatura, notas o revisado no obliga a re-renderizar.
export function contentHash(spec) {
  const { youtube, miniatura, notas, revisado, ...rest } = spec;
  return createHash("sha1").update(JSON.stringify(rest)).digest("hex").slice(0, 12);
}

// Los videos ya publicados el profe los mueve a mano a salida/subidos/ (o subidos/ en la raíz).
// outPath busca cada archivo de salida ahí también, para no perderlo del CHECKLIST ni duplicarlo al regenerarlo.
// También cuentan sus subcarpetas (ej. salida/subidos/viejos/).
const SUBIDOS = [join(ROOT, "salida", "subidos"), join(ROOT, "subidos")];
const subidosDirs = () => SUBIDOS.filter((d) => existsSync(d)).flatMap((d) => [d,
  ...readdirSync(d, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => join(d, e.name))]);
const subidoPath = (file) => subidosDirs().map((d) => join(d, file)).find((f) => existsSync(f)) || null;
const outPath = (file) => subidoPath(file) || join(ROOT, "salida", file);
const rel = (f) => f.slice(ROOT.length + 1).replace(/\\/g, "/");

const VOICE_CREDIT = "🎙️ Voz: Daniela (Piper TTS, rhasspy/piper-voices), datos de Google OpenSLR 61, licencia CC BY-SA 4.0.";
const VOICE_CREDIT_EN = "🎙️ Nombre del ejercicio: voz Heart (Kokoro TTS, hexgrad/Kokoro-82M), licencia Apache 2.0.";
// salida/<slug>.youtube.txt — título, descripción y tags listos para copiar en YouTube Studio.
// conEn = el último render dice el nombre en inglés con Kokoro (.pipeline.json → renderVozEn): suma ese crédito.
function exportYoutube(spec, conEn = false) {
  const yt = spec.youtube;
  if (!yt?.descripcion) return false;
  mkdirSync(join(ROOT, "salida"), { recursive: true });
  // La voz Daniela (Piper) es CC BY-SA 4.0: el crédito va antes de los hashtags (última línea de la descripción).
  let desc = yt.descripcion;
  if ((spec.voiceProvider || "piper") === "piper" && !desc.includes("Voz:")) {
    const lines = desc.split("\n"), tags = lines.pop();
    desc = [...lines, VOICE_CREDIT, ...(conEn ? [VOICE_CREDIT_EN] : []), "", tags].join("\n");
  }
  const txt = ["TÍTULO", yt.titulo, "", "DESCRIPCIÓN", desc, "", "TAGS", (yt.tags || []).join(", "), ""].join("\n");
  writeFileSync(outPath(`${spec.slug}.youtube.txt`), txt);
  return true;
}

function writeDocs(dir, spec) {
  const frames = spec.frames.map((f, i) => ({ ...f, id: f.id || String(i + 1).padStart(2, "0") }));
  const audience = spec.maquina ? "alumnos de gimnasio (máquinas)" : "alumnos de CrossFit";
  writeFileSync(join(dir, "BRIEF.md"), `---
workflow: faceless-explainer
flow: automation
storyboard: no
message: "Cómo ejecutar ${spec.name} paso a paso"
destination: reels
aspect: 1080x1920
language: es
audience: ${audience}
angle: how-to
---

## Intent

Video instructivo vertical del ejercicio "${spec.name}" para que un alumno sepa cómo ejecutarlo.
Descripción (verbatim): "${spec.descripcion}"

## Notes

- Generado con plantilla/make-exercise.mjs desde ejercicios/${spec.slug}.json (no editar a mano).
`);
  writeFileSync(join(dir, "STORYBOARD.md"), `---
format: 1080x1920
message: "Cómo ejecutar ${spec.name} paso a paso"
audience: ${audience}
mode: autonomous
music: plantilla/musica/bgm-base.wav
---
${frames.map((f, i) => `
## Frame ${i + 1} — ${f.badge || ""} ${f.head.join(" ")}

- status: animated
- min: ${f.min || 4}s
- voiceover: "${f.vo}"
- poses: ${(f.moves || []).filter((m) => m.to).map((m) => m.to).join(" → ") || "—"}
`).join("")}`);
  writeFileSync(join(dir, "SCRIPT.md"), `# SCRIPT — ${spec.slug}

**Voice:** ${spec.voice || "es_AR-daniela-high"} (${spec.voiceProvider || "piper"}, español rioplatense)
**Voice direction:** Coach claro y motivador.

---
${frames.map((f, i) => `
## Line ${i + 1} — ${f.badge || ""} (Frame ${i + 1})

    ${f.vo}
`).join("")}`);
  return frames;
}

// Voz: Piper local con Daniela (es_AR) por defecto. "voiceProvider": "kokoro" en la ficha vuelve al motor anterior
// (voces em_alex, em_santa, ef_dora).
const PIPER_VOICE = "es_AR-daniela-high";
// Nombre en inglés (desde 2026-10-21): en la portada el nombre lo dice Kokoro "Heart" en inglés y el resto, Daniela.
const EN_VOICE = "kokoro:af_heart";

// Parte el vo de la portada en { en, es }. Si el vo empieza con el nombre ("Air Squat: la sentadilla…"), el nombre se
// saca del texto de Daniela; si no, el nombre en inglés se dice antes del vo completo. "nombreEnVoz" (ficha) = cómo lo
// dice la voz inglesa ("4-6 Breathing" → "Four six breathing"); "nombreEn": false lo apaga (nombres en castellano).
function nombreEn(spec, vo) {
  if (spec.nombreEn === false || (spec.voiceProvider || "piper") !== "piper") return null;
  const en = spec.nombreEnVoz || spec.name;
  if (!vo.toLowerCase().startsWith(spec.name.toLowerCase())) return { en, es: vo };
  const es = vo.slice(spec.name.length).replace(/^[\s:,.;—-]+/, "");
  return { en, es: es.charAt(0).toUpperCase() + es.slice(1) };
}

function tts(dir, spec, frames) {
  const provider = spec.voiceProvider || "piper";
  const hook = Math.max(0, frames.findIndex((f) => f.kind === "hook"));
  let conEn = false;
  const request = {
    provider,
    lang: "es",
    speed: spec.voiceSpeed ?? 1.0,
    voice: spec.voice || (provider === "piper" ? PIPER_VOICE : "em_alex"),
    lines: frames.map((f, i) => {
      // "pronuncia" (ficha): reemplazos solo para la voz, el subtítulo queda con el texto real ("Burpee" → "Burpii").
      // "voSpeed" (escena): velocidad propia de esa línea (ej. 0.88 para que el nombre en inglés se entienda).
      const sp = i === hook ? nombreEn(spec, f.vo) : null;
      let text = sp ? sp.es : f.vo;
      for (const [from, to] of Object.entries(spec.pronuncia || {})) text = text.split(from).join(to);
      // Con el nombre en inglés, el voSpeed de la portada (que era para el nombre) ya no se usa.
      if (sp) { conEn = true; return { id: f.id, en: sp.en, text }; }
      return f.voSpeed ? { id: f.id, text, speed: f.voSpeed } : { id: f.id, text };
    }),
    bgm: { mode: "none" },
  };
  if (conEn) request.enVoice = EN_VOICE;
  writeStatus(dir, { vozEn: conEn ? EN_VOICE : null });
  const reqPath = join(dir, "audio_request.json");
  const prev = existsSync(reqPath) ? readFileSync(reqPath, "utf8") : "";
  const next = JSON.stringify(request, null, 2);
  const metaOk = existsSync(join(dir, "audio_engine_meta.json"));
  if (prev === next && metaOk && !has("--force-tts")) {
    console.log("· voz: sin cambios, se reutiliza");
    return true;
  }
  writeFileSync(reqPath, next);
  const r = provider === "piper"
    ? sh(`python "${join(HERE, "piper-tts.py")}" audio_request.json audio_engine_meta.json`, dir)
    : sh(`node "${ENGINE}" --request ./audio_request.json --hyperframes . --out ./audio_engine_meta.json --only tts`, dir);
  return r.status === 0;
}

// Miniatura de YouTube: la portada del video quieta, con el personaje en la pose de spec.miniatura.
function miniatura(dir, slug) {
  const t = buildIndex(dir, { thumb: true });
  const shots = join(t.dir, "snapshots");
  rmSync(shots, { recursive: true, force: true });
  const r = sh(`npx --prefer-offline hyperframes snapshot . --at ${t.at} --no-end --describe false`, t.dir);
  collectShots(t.dir);
  const png = existsSync(shots) && readdirSync(shots).find((f) => f.endsWith(".png"));
  if (r.status !== 0 || !png) return false;
  mkdirSync(join(ROOT, "salida"), { recursive: true });
  copyFileSync(join(shots, png), outPath(`${slug}.miniatura.png`));
  console.log(`✓ salida/${slug}.miniatura.png (pose ${t.pose})`);
  return true;
}

function mp4Duration(file) {
  const r = spawnSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", file], { encoding: "utf8" });
  return r.status === 0 ? Number(r.stdout.trim()) : null;
}

export function checklist() {
  const csv = readCsv();
  const specs = Object.fromEntries(
    readdirSync(join(ROOT, "ejercicios")).filter((f) => f.endsWith(".json")).map((f) => {
      const spec = JSON.parse(readFileSync(join(ROOT, "ejercicios", f), "utf8"));
      return [spec.slug, { spec, file: join(ROOT, "ejercicios", f) }];
    }),
  );
  // Máquinas de gimnasio: lista aparte (ejercicios/maquinas.csv), tabla aparte y numeración M1, M2…
  const maq = readCsv("maquinas.csv");
  const runtime = readFileSync(join(HERE, "runtime.js"), "utf8");
  const dibujada = (prop) => runtime.includes(`pr.type === "${prop}"`);
  // Primero las fichas que no están en ninguna lista (p. ej. squat-to-stand), después la lista en su orden.
  const inCsv = new Set([...csv, ...maq].map((r) => r.clave));
  const items = [
    ...Object.keys(specs).filter((k) => !inCsv.has(k)).sort().map((k) => ({ slug: k, n: "—" })),
    ...csv.map((r, i) => ({ slug: r.clave, n: String(i + 1), row: r })),
  ];
  const ok = (b) => (b ? "✅" : "⬜");
  let done = 0, fichas = 0, yts = 0, subidos = 0, next = null;
  const conEn = [], sinEn = []; // videos en salida/ (no subidos) ya re-renderizados / pendientes con el nombre en inglés
  const fila = ({ slug, n, row }) => {
    const s = specs[slug];
    const st = readStatus(join(ROOT, "videos", slug));
    const mp4 = st.archivo || `${slug}.mp4`; // archivo = nombre con prefijo del último render (--prefijo)
    // Subido = está en salida/subidos/ con su nombre o sin prefijo (un OC_ que se subió como <slug>.mp4).
    const out = outPath(mp4), subido = !!(subidoPath(mp4) || subidoPath(`${slug}.mp4`));
    const rendered = existsSync(out);
    const name = s?.spec.name || row?.nombre || slug;
    // Máquina: 🏋️ + nombre en castellano + prop de runtime.js (y si todavía hay que dibujarla).
    const impl = row?.prop
      ? `🏋️ ${row.nombre_es} · \`${row.prop}\`${dibujada(row.prop) ? "" : " (falta dibujar)"}`
      : row?.implemento || (s ? "Ninguno" : "");
    if (!s) {
      next ??= `${n} · ${name}`;
      const faltan = row?.prop ? [] : [!row?.descripcion && "descripción", !row?.tecnica_coach && "técnica"].filter(Boolean);
      const nota = faltan.length ? `falta ${faltan.join(" y ")} en el CSV` : row?.prop ? `Lote ${row.lote} · Nivel ${row.nivel} · ${row.dosis}` : "";
      return `| ${n} | ${name} | ${impl} | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | — | ⬜ | ⬜ | — | ${nota} |`;
    }
    fichas++;
    const { spec, file } = s;
    const stale = rendered && (st.renderHash ? st.renderHash !== contentHash(spec) : statSync(file).mtimeMs > statSync(out).mtimeMs);
    const yt = exportYoutube(spec, !!st.renderVozEn);
    if (rendered) done++;
    if (subido) subidos++;
    if (yt) yts++;
    const dur = rendered ? `${mp4Duration(out)?.toFixed(1)} s` : "—";
    // Nombre EN: ✅ el render dice el nombre en inglés · ⬜ falta re-renderizar · — no aplica (subido, sin render, nombreEn false)
    let en = "—";
    if (rendered && st.renderVozEn) { en = "✅"; if (!subido) conEn.push(slug); }
    else if (rendered && !subido && spec.nombreEn !== false) { en = "⬜"; sinEn.push(`${slug}${mp4 !== `${slug}.mp4` ? ` (${mp4})` : ""}`); }
    return `| ${n} | ${name} | ${impl} | ✅ | ${ok(st.voz)} | ${ok(st.composicion)} | ${st.check == null ? "⬜" : st.check ? "✅" : "❌"} | ${rendered ? (stale ? "⚠️ desactualizado" : "✅") : "⬜"} | ${yt ? `[✅](${rel(outPath(`${slug}.youtube.txt`))})` : "⬜"} | ${existsSync(outPath(`${slug}.miniatura.png`)) ? `[✅](${rel(outPath(`${slug}.miniatura.png`))})` : "⬜"} | ${dur} | ${rendered ? `[${mp4}](${rel(out)})` : "—"} | ${en} | ${ok(spec.revisado)} | ${ok(subido)} | ${st.renderizado || "—"} | ${spec.notas || ""} |`;
  };
  const rows = items.map(fila);
  const cf = { done, fichas, yts, subidos, next, total: items.length };
  done = fichas = yts = subidos = 0; next = null;
  const rowsMaq = maq.map((r, i) => fila({ slug: r.clave, n: `M${i + 1}`, row: r }));
  const mq = { done, fichas, yts, subidos, next, total: maq.length };
  const head = `| # | Ejercicio | Implemento | Ficha | Voz | Composición | Check | Render | YouTube | Miniatura | Duración | Archivo | Nombre EN | Revisado | Subido | Fecha render | Notas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|`;
  const resumen = (c) => `**Renderizados:** ${c.done} / ${c.total} · **Fichas:** ${c.fichas} · **Descripción YouTube:** ${c.yts} · **Subidos:** ${c.subidos}${c.next ? ` · **Próximo:** ${c.next}` : ""}`;
  const faltaDibujar = [...new Set(maq.filter((r) => !dibujada(r.prop)).map((r) => r.prop))];
  const tablaMaq = maq.length
    ? `\n## 🏋️ Máquinas de gimnasio\n
Videos de máquinas (no CrossFit): se hacen con \`GENERAR_VIDEOS_MAQUINAS.md\`. La lista y su orden salen de
\`ejercicios/maquinas.csv\` (armada desde \`maquinas_gimnasio.xlsx\`, un video por ejercicio). Duran 90–150 s.
La columna Implemento dice la máquina y el prop de \`plantilla/runtime.js\` que la dibuja.\n
${resumen(mq)}${faltaDibujar.length ? ` · **Máquinas sin dibujar:** ${faltaDibujar.length}` : ""}\n
${head}
${rowsMaq.join("\n")}\n`
    : "";
  // Plan de re-render con el nombre en inglés: lotes de 10 en el orden de la tabla (plantilla/revoz-en.mjs toma el primero).
  const lotes = [];
  for (let i = 0; i < sinEn.length; i += 10) lotes.push(sinEn.slice(i, i + 10));
  const plan = sinEn.length
    ? `\n## Plan: nombre en inglés en los videos ya renderizados\n
Los videos de \`salida/\` (no los subidos) se re-renderizan para que el nombre lo diga la voz en inglés.
Hechos: **${conEn.length}** · Pendientes: **${sinEn.length}** en ${lotes.length} lotes. Próximo lote: \`node plantilla/revoz-en.mjs --lotes=1\`.
El archivo conserva su nombre (los \`OC_\` siguen siendo \`OC_\`).\n
${lotes.map((l, i) => `- **Lote ${i + 1}:** ${l.join(", ")}`).join("\n")}\n`
    : "";
  const md = `# Checklist de videos de ejercicios

Generado automáticamente por \`node plantilla/make-exercise.mjs --checklist\` (no editar a mano).
La lista y su orden salen de \`ejercicios/ejercicios.csv\`; el estado, de \`ejercicios/<clave>.json\`,
\`videos/<clave>/.pipeline.json\` y \`salida/\`. Para aprobar un video: \`"revisado": true\` en su JSON; las notas salen de \`"notas"\`.
Subido = el .mp4 está en \`salida/subidos/\` (se mueve a mano después de publicarlo en YouTube).

${resumen(cf)}

${head}
${rows.join("\n")}

Leyenda: ✅ listo · ⬜ pendiente · ❌ falló · ⚠️ lo que se ve/escucha en la ficha cambió después del último render (volver a renderizar).
Nombre EN: ✅ el nombre lo dice la voz en inglés · ⬜ falta re-renderizar · — no aplica (subido a YouTube, sin render o nombre en castellano).
Implemento distinto de "Ninguno": el personaje todavía no lo tiene; hay que agregarlo a \`plantilla/runtime.js\` antes de hacer ese video.
🏋️ = ejercicio de máquina de gimnasio (tabla aparte, al final).
${plan}${tablaMaq}`;
  writeFileSync(join(ROOT, "CHECKLIST.md"), md);
  console.log(`✓ CHECKLIST.md (${cf.done}/${cf.total} renderizados, ${cf.fichas} fichas, ${cf.yts} con descripción YouTube · máquinas ${mq.done}/${mq.total})`);
}

function main() {
  if (has("--checklist") && !slug) return checklist();
  if (has("--info")) {
    const row = [...readCsv(), ...readCsv("maquinas.csv")].find((r) => r.clave === slug);
    if (!row) throw new Error(`${slug} no está en ejercicios/ejercicios.csv ni en ejercicios/maquinas.csv`);
    return console.log(JSON.stringify(row, null, 2));
  }
  if (has("--miniatura")) {
    const specPath = join(ROOT, "ejercicios", `${slug}.json`);
    copyFileSync(specPath, join(ROOT, "videos", slug, "exercise.json"));
    writeStatus(join(ROOT, "videos", slug), { miniatura: miniatura(join(ROOT, "videos", slug), slug) });
    return checklist();
  }
  if (!slug) {
    console.error("uso: node plantilla/make-exercise.mjs <slug> [--render] | --checklist");
    process.exit(1);
  }
  const specPath = join(ROOT, "ejercicios", `${slug}.json`);
  if (!existsSync(specPath)) throw new Error(`no existe ${specPath}`);
  const spec = JSON.parse(readFileSync(specPath, "utf8"));
  const dir = join(ROOT, "videos", slug);

  if (!existsSync(join(dir, "hyperframes.json"))) {
    const r = sh(`npx --prefer-offline hyperframes init "videos/${slug}" --non-interactive --example=blank --skill=faceless-explainer`, ROOT);
    if (r.status !== 0) throw new Error("hyperframes init falló");
  }
  copyFileSync(specPath, join(dir, "exercise.json"));
  copyFileSync(join(HERE, "frame.md"), join(dir, "frame.md"));
  const frames = writeDocs(dir, spec);

  const vozOk = tts(dir, spec, frames);
  writeStatus(dir, { voz: vozOk });
  if (!vozOk) throw new Error("la generación de voz falló");

  const b = buildIndex(dir);
  console.log(`✓ index.html — ${b.frames.length} escenas, ${b.total}s, voces ${b.voices}, música ${b.music ? "sí" : "no"}`);
  b.warnings.forEach((w) => console.log(`  ⚠ ${w}`));
  writeStatus(dir, { composicion: true, duracion: b.total });

  if (!has("--no-check")) {
    const r = sh("npx --prefer-offline hyperframes check", dir);
    writeStatus(dir, { check: r.status === 0 });
  }
  if (!has("--no-snapshot")) {
    const mids = b.frames.map((f) => (f.start + f.dur * 0.7).toFixed(2)).join(",");
    sh(`npx --prefer-offline hyperframes snapshot --at ${mids}`, dir);
    collectShots(dir);
    console.log(`· contact sheet: videos/${slug}/snapshots/contact-sheet.jpg`);
  }
  writeStatus(dir, { miniatura: miniatura(dir, slug) });
  if (has("--render")) {
    const r = sh("npx --prefer-offline hyperframes render --skill=faceless-explainer --quality high --output renders/video.mp4", dir);
    if (r.status !== 0) throw new Error("render falló");
    mkdirSync(join(ROOT, "salida"), { recursive: true });
    copyFileSync(join(dir, "renders", "video.mp4"), join(ROOT, "salida", mp4Name(slug)));
    writeStatus(dir, { renderizado: today(), renderHash: contentHash(spec), archivo: mp4Name(slug), renderVozEn: readStatus(dir).vozEn || null });
    console.log(`✓ salida/${mp4Name(slug)}`);
  }
  checklist();
}

main();
