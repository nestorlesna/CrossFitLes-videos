// Videos largos 16:9: arma <proyecto>/index.html desde <proyecto>/guion.json + audio_engine_meta.json.
// Reutiliza el personaje (plantilla/runtime.js) y los helpers de poses/moves de plantilla/build-index.mjs; agrega
// capítulos, cuenta regresiva de las esperas ("hold"), tarjeta de consejo y tarjetas "vista de frente / de arriba".
// buildLargo(dir, { thumb: true }) arma <proyecto>/miniatura/index.html (miniatura de YouTube, sin audio).
// buildLargo(dir, { lab: true }) no exige voz (pose-lab). Formato de la ficha: GENERAR_VIDEOS_LARGOS.md.
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { expandMoves, normalizePose, VO_LEAD } from "../build-index.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const PLANTILLA = resolve(HERE, "..");
const TAIL = 0.75; // aire después de cada línea de voz
const RIG = { x: 1400, y: 838, scale: 0.95 }; // piso en y ≈ 870 (y + 34·scale)
const POSE_KEYS = ["s", "t", "b", "hd", "ua", "fa", "s2", "t2", "ua2", "fa2", "rx", "ry", "ft", "ft2", "hx", "hy", "ed", "lr", "al", "hb", "bf", "bx", "by", "g2", "hx2", "hy2", "ed2", "wr", "wr2", "cv", "fx", "dh", "pz", "rp", "ul", "fl", "ll", "ll2", "cs"];
export const THUMB_AT = 1.9;

// Escenas planas con su capítulo: ids "CCSS" (capítulo, escena) = nombre del .wav de la voz.
export function flatScenes(spec) {
  const out = [];
  let n = 0;
  spec.capitulos.forEach((c, ci) => {
    const num = c.numero === false ? null : ++n;
    c.escenas.forEach((e, si) => out.push({ ...e, cap: ci, capNum: num, id: `${String(ci + 1).padStart(2, "0")}${String(si + 1).padStart(2, "0")}` }));
  });
  return { scenes: out, numerados: n };
}

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
const fmt = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, "0")}`;

export function buildLargo(projectDir, { thumb = false, lab = false } = {}) {
  const P = resolve(projectDir);
  const spec = JSON.parse(readFileSync(join(P, "guion.json"), "utf8"));
  const metaPath = join(P, "audio_engine_meta.json");
  const meta = !thumb && existsSync(metaPath) ? JSON.parse(readFileSync(metaPath, "utf8")) : { voices: [] };
  const voice = Object.fromEntries((meta.voices || []).map((v) => [v.id, v]));
  const warnings = [];
  const poses = Object.fromEntries(Object.entries(spec.poses).map(([k, v]) => [k, normalizePose(v)]));
  const RIGX = { ...RIG, ...(spec.rig || {}) };
  let { scenes, numerados } = flatScenes(spec);

  if (thumb) {
    const m = spec.miniatura || {};
    scenes = [{ id: "thumb", cap: 0, capNum: null, vo: "", min: THUMB_AT + 0.5, moves: [] }];
    spec.capitulos = [{ titulo: "", head: m.head || [spec.name], hero: true, numero: false, badge: m.badge || spec.category }];
  }

  // Duraciones: la voz manda; nunca menos que la última acción ni que la espera (hold) completa.
  let t = 0;
  for (const f of scenes) {
    const v = voice[f.id];
    if (!v && !thumb && !lab && f.vo) warnings.push(`escena ${f.id}: sin voz generada`);
    f.holdStart = f.hold ? +(f.holdAt ?? (v ? VO_LEAD + v.duration_s + 0.3 : 0.6)).toFixed(3) : null;
    // { to, hold: true } = el movimiento arranca con la espera (ej. bajar un poco más mientras se aguanta).
    f.rawMoves = (f.moves || []).map((m) => (m.hold ? { ...m, at: +(f.holdStart + (m.holdOff ?? 0.4)).toFixed(3), dur: m.dur ?? Math.max(1.2, f.hold * 0.6) } : m));
    const e = expandMoves({ moves: f.rawMoves });
    const acts = [...e.moves.map((m) => m.at + m.dur), ...(f.overlays || []).map((o) => o.at + 0.6)];
    const need = Math.max(f.min || 3, v ? VO_LEAD + v.duration_s + TAIL : 0, acts.length ? Math.max(...acts) + 0.45 : 0, f.hold ? f.holdStart + f.hold + 0.7 : 0);
    f.start = +t.toFixed(3);
    f.dur = +need.toFixed(3);
    t += f.dur;
  }
  const total = +t.toFixed(3);
  const cutTimes = [];
  scenes.forEach((f) => {
    const e = expandMoves({ moves: f.rawMoves }, f.dur);
    f.moves = e.moves;
    e.cuts.forEach((c) => cutTimes.push(+(f.start + c).toFixed(3)));
  });

  // Capítulos: inicio/fin (para el encabezado, las marcas de la barra y los capítulos de YouTube).
  const caps = spec.capitulos.map((c, ci) => {
    const sc = scenes.filter((s) => s.cap === ci);
    return { ...c, ci, num: sc[0]?.capNum ?? null, start: sc[0]?.start ?? 0, end: sc.length ? sc.at(-1).start + sc.at(-1).dur : 0 };
  }).filter((c) => c.end > c.start);

  // Moves → tweens absolutos con estado de partida explícito (igual que build-index).
  const mini = spec.miniatura || {};
  const initialPose = thumb ? mini.pose || spec.initialPose : spec.initialPose || Object.keys(poses)[0];
  if (!poses[initialPose]) throw new Error(`pose desconocida "${initialPose}"`);
  const cur = { ...poses[initialPose], g: thumb ? mini.grip ?? poses[initialPose].g ?? 0 : spec.initialGrip ?? poses[initialPose].g ?? 0 };
  const initialState = { ...cur };
  const all = [];
  scenes.forEach((f) => f.moves.forEach((m) => all.push({ ...m, t: f.start + m.at, frame: f.id })));
  all.sort((a, b) => a.t - b.t);
  const moves = all.map((m) => {
    if (m.grip != null) {
      const mv = { keys: ["g"], from: { g: cur.g }, to: { g: m.grip }, t: +m.t.toFixed(3), dur: m.dur, ease: m.ease };
      cur.g = m.grip;
      return mv;
    }
    if (!poses[m.to]) throw new Error(`escena ${m.frame}: pose desconocida "${m.to}"`);
    const from = {}, to = {};
    const keys = poses[m.to].g != null ? [...POSE_KEYS, "g"] : POSE_KEYS;
    keys.forEach((k) => { from[k] = cur[k]; to[k] = poses[m.to][k]; cur[k] = poses[m.to][k]; });
    return { keys, from, to, t: +m.t.toFixed(3), dur: m.dur, ease: m.ease };
  });

  const overlays = [];
  scenes.forEach((f) => (f.overlays || []).forEach((o) => {
    const end = o.out != null ? f.start + o.out : f.start + f.dur - 0.35;
    overlays.push({ ...o, t: +(f.start + o.at).toFixed(3), end: +end.toFixed(3) });
  }));

  // Esperas: cuenta regresiva (anillo + segundos que faltan).
  const holds = scenes.filter((f) => f.hold).map((f) => ({ id: f.id, t0: +(f.start + f.holdStart).toFixed(3), dur: f.hold, label: f.holdLabel || "AGUANTÁ" }));

  // Tarjetas: escenas seguidas con la misma tarjeta (tipo + lado + label) comparten un solo clip (no parpadea).
  // Valor animado v: anim [[valor, at, dur]] (at numérico o "hold"), vaiven { de, a, at, dur } hasta el final de la escena.
  const cards = [];
  scenes.forEach((f) => {
    if (!f.card) return;
    const c = f.card, key = `${c.tipo}|${c.lado ?? 1}|${c.label || ""}`;
    let g = cards.at(-1);
    if (!g || g.key !== key || Math.abs(g.end - f.start) > 0.01) {
      g = { key, id: f.id, tipo: c.tipo, lado: c.lado ?? 1, label: c.label || "", start: f.start, end: f.start, v0: c.desde ?? 0, segs: [] };
      cards.push(g);
    }
    g.end = +(f.start + f.dur).toFixed(3);
    let v = g.segs.length ? g.segs.at(-1).b : g.v0;
    const rel = (at) => (at === "hold" ? f.holdStart ?? 0.6 : at);
    for (const [val, at, dur] of c.anim || []) {
      g.segs.push({ t0: +(f.start + rel(at)).toFixed(3), t1: +(f.start + rel(at) + dur).toFixed(3), a: v, b: val });
      v = val;
    }
    if (c.vaiven) {
      const { de, a, dur } = c.vaiven;
      let tt = f.start + rel(c.vaiven.at ?? 0.4), i = 0;
      if (v !== de) { g.segs.push({ t0: +tt.toFixed(3), t1: +(tt + dur / 2).toFixed(3), a: v, b: de }); tt += dur / 2; v = de; }
      while (tt + dur <= f.start + f.dur - 0.2) {
        const b = i % 2 ? de : a;
        g.segs.push({ t0: +tt.toFixed(3), t1: +(tt + dur).toFixed(3), a: v, b });
        v = b; tt += dur; i++;
      }
    }
  });

  const clip = (id, start, dur, cls, inner, track, attrs = "") =>
    `<div id="${id}" class="clip ${cls}" data-start="${start}" data-duration="${+dur.toFixed(3)}" data-track-index="${track}"><div class="inner"${attrs}>${inner}</div></div>`;

  const capBlocks = caps.map((c) => {
    const badge = c.badge || (c.num ? `EJERCICIO ${c.num} DE ${numerados}` : spec.category || "");
    const head = (c.head || [c.titulo]).map((h) => `<span class="hl">${esc(h)}</span>`).join("");
    return clip(`cap-${c.ci}`, c.start, c.end - c.start, `cap${c.hero ? " hero" : ""}`, `<div class="badge">${esc(badge)}</div><h1 class="headline">${head}</h1>`, 7);
  });

  const textBlocks = scenes.map((f) => {
    let inner = "";
    if (f.step) inner += `<div class="step">${esc(f.step)}</div>`;
    if (f.sub) inner += `<p class="subline">${esc(f.sub)}</p>`;
    if (f.tags && spec.tags?.length) inner += `<div class="tags">${spec.tags.map((x) => `<span class="chip-tag">${esc(x)}</span>`).join("")}</div>`;
    if (thumb && mini.chip) inner += `<div class="tags"><span class="chip-tag">${esc(mini.chip)}</span></div>`;
    if (f.tip) inner += `<div class="tip"><div class="lbl">CONSEJO</div><p>${esc(f.tip)}</p></div>`;
    if (f.keys) inner += `<ul id="keys-${f.id}" class="keys">${f.keys.map((k, i) => `<li id="key-${f.id}-${i}"><span class="tick"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span>${esc(typeof k === "object" ? k.text : k)}</span></li>`).join("")}</ul>`;
    return clip(`txt-${f.id}`, f.start, f.dur, "scene-text", inner, 3);
  });
  const subs = thumb ? [] : scenes.map((f) => clip(`sub-${f.id}`, f.start, f.dur, "subtitle", `<p>${esc(f.vo || "")}</p>`, 5));
  const holdBlocks = holds.map((h) => clip(`hold-${h.id}`, +(h.t0 - 0.3).toFixed(3), h.dur + 0.8, "hold",
    `<svg viewBox="0 0 210 210"><circle cx="105" cy="105" r="88" fill="#fff" stroke="#E8E0D4" stroke-width="16"/>
      <circle id="ring-${h.id}" cx="105" cy="105" r="88" fill="none" stroke="#E85D5D" stroke-width="16" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1" transform="rotate(-90 105 105)"/>
      <text id="num-${h.id}" class="num" x="105" y="138" text-anchor="middle">${h.dur}</text></svg><div class="lbl">${esc(h.label)}</div>`, 8));
  const cardBlocks = cards.map((c) => clip(`card-${c.id}`, c.start, c.end - c.start, "card",
    `<div class="lbl">${c.tipo === "torsion" ? "VISTA DE ARRIBA" : "VISTA DE FRENTE"}</div><svg viewBox="0 0 300 330"><g id="cg-${c.id}"${c.lado === -1 ? ' transform="translate(300,0) scale(-1,1)"' : ""}></g>
      <text x="150" y="324" text-anchor="middle" font-family="Inter" font-weight="800" font-size="20" fill="#1A1A1A">${esc(c.label)}</text></svg>`, 4));

  const runtimeFrames = scenes.map((f) => {
    const rf = { id: f.id, start: f.start, dur: f.dur, kind: f.tags ? "hook" : "step", numeral: null, stance: false, scroll: 0 };
    if (f.keys) {
      const v = voice[f.id];
      rf.keyTimes = f.keys.map((k, i) => {
        const cue = (typeof k === "object" && k.cue) || null;
        const w = cue && (v?.words || []).find((w) => w.text.toLowerCase().normalize("NFD").replace(/[^a-z]/g, "").startsWith(cue));
        const rel = w ? VO_LEAD + w.start - 0.1 : (typeof k === "object" && k.at) ?? 1.0 + i * 1.3;
        return +(f.start + rel).toFixed(3);
      });
    }
    return rf;
  });

  const audio = thumb ? [] : scenes.filter((f) => voice[f.id]).map((f) =>
    `<audio id="vo-${f.id}" src="${voice[f.id].path}" data-start="${+(f.start + VO_LEAD).toFixed(3)}" data-duration="${voice[f.id].duration_s}" data-track-index="10" data-volume="1"></audio>`);

  // Música: plantilla/musica/bgm-base.wav (~177 s) en loop hasta el largo del video, más baja que en los shorts.
  let bgm = "";
  const bed = join(PLANTILLA, "musica", "bgm-base.wav");
  if (!thumb && !lab && spec.music !== false && existsSync(bed)) {
    mkdirSync(join(P, "assets", "bgm"), { recursive: true });
    const r = spawnSync("ffmpeg", ["-y", "-loglevel", "error", "-stream_loop", "-1", "-i", bed, "-t", String(total + 1), join(P, "assets", "bgm", "track-long.wav")]);
    if (r.status === 0) {
      const vol = spec.musicVolume ?? 0.12;
      bgm = `<audio id="bgm" src="assets/bgm/track-long.wav" data-start="0" data-duration="${total}" data-track-index="11" data-volume="${vol}" data-automation='{"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0},{"t":1.5,"v":${vol}},{"t":${+(total - 3).toFixed(2)},"v":${vol}},{"t":${total},"v":0}]}]}'></audio>`;
    } else warnings.push("ffmpeg falló al preparar la música");
  }

  const config = { total, rig: RIGX, props: spec.props || [], cuts: cutTimes, floorScroll: 0, poses, initialState, initialPose, moves, overlays, frames: runtimeFrames, colors: spec.colors || null, fingers: !!spec.fingers };
  const extra = { total, caps: caps.map((c) => ({ ci: c.ci, start: c.start, end: c.end })), holds, cards: cards.map(({ id, tipo, v0, segs }) => ({ id, tipo, v0, segs })), thumb };
  const runtime = readFileSync(join(PLANTILLA, "runtime.js"), "utf8");
  const css = readFileSync(join(HERE, "styles-largo.css"), "utf8");
  const z = mini.zoom ?? 1.35, dx = mini.dx ?? 0, dy = mini.dy ?? 60;
  const ticks = caps.slice(1).map((c) => `<div class="tick-cap" style="left:${((c.start / total) * 1760).toFixed(1)}px"></div>`).join("");

  const html = `<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
${css}${thumb ? `
      /* miniatura: personaje más grande (spec.miniatura.zoom / dx / dy), título enorme */
      #stage { transform: translate(${dx}px, ${dy}px) scale(${z}); transform-origin: 1400px 870px; }
      .cap { top: 110px; width: 900px; height: 560px; }
      .cap .badge { font-size: 34px; padding: 14px 26px; }
      .cap.hero .headline { font-size: ${mini.size ?? 190}px; }
      .scene-text { top: 640px; }
      .chip-tag { font-size: 44px; padding: 12px 28px; border-width: 6px; }` : ""}
    </style>
  </head>
  <body>
    <!-- GENERADO por plantilla/largo/build-largo.mjs desde guion.json — no editar a mano -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="${total}" data-width="1920" data-height="1080">
      <div id="bg" class="clip" data-start="0" data-duration="${total}" data-track-index="0"><div id="hatch"></div></div>
      <div id="stage" class="clip" data-start="0" data-duration="${total}" data-track-index="2">
        <div id="floor-shadow"${spec.shadow === false ? ' style="display:none"' : ""}></div>
        <div id="floor"></div>
        <svg viewBox="0 0 1920 1080">
          <g id="athlete"><g id="rig" transform="translate(${RIGX.x},${RIGX.y}) scale(${RIGX.scale})"></g></g>
          <g id="overlays"></g>
        </svg>
      </div>
      ${thumb ? "" : `<div id="topbar" class="clip" data-start="0" data-duration="${total}" data-track-index="6"><div class="inner"><span><b>${esc(spec.name.toUpperCase())}</b></span><span>${esc(spec.category || "")}</span></div></div>`}
      ${capBlocks.join("\n      ")}
      ${textBlocks.join("\n      ")}
      ${cardBlocks.join("\n      ")}
      ${holdBlocks.join("\n      ")}
      ${subs.join("\n      ")}
      ${thumb ? "" : `<div id="progress" class="clip" data-start="0" data-duration="${total}" data-track-index="9"><div id="progress-fill"></div>${ticks}</div>`}
      ${audio.join("\n      ")}
      ${bgm}
    </div>
    <script>
      window.__EX_CONFIG = ${JSON.stringify(config)};
${runtime}
    </script>
    <script>
      window.__LARGO = ${JSON.stringify(extra)};
${readFileSync(join(HERE, "largo-runtime.js"), "utf8")}
    </script>
  </body>
</html>
`;
  const chapters = caps.map((c) => ({ t: c.start, titulo: c.titulo }));
  if (thumb) {
    const T = join(P, "miniatura");
    mkdirSync(T, { recursive: true });
    for (const f of ["hyperframes.json", "meta.json", "package.json"]) if (existsSync(join(P, f))) writeFileSync(join(T, f), readFileSync(join(P, f)));
    writeFileSync(join(T, "index.html"), html);
    return { dir: T, at: THUMB_AT };
  }
  writeFileSync(join(P, "index.html"), html);
  if (!lab) writeFileSync(join(P, "capitulos.json"), JSON.stringify(chapters, null, 2));
  return { total, scenes: scenes.map((f) => ({ id: f.id, start: f.start, dur: f.dur })), chapters, warnings, voices: Object.keys(voice).length, music: !!bgm };
}

// Capítulos de YouTube ("0:00 Intro"): el primero en 0:00, cada uno de 10 s o más.
export function chaptersText(chapters) {
  return chapters.filter((c) => c.titulo).map((c, i) => `${i === 0 ? "0:00" : fmt(c.t)} ${c.titulo}`).join("\n");
}
