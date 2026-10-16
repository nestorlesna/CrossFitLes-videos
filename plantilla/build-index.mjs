// Builds <project>/index.html from <project>/exercise.json + audio_engine_meta.json + plantilla/runtime.js.
// Usage: node plantilla/build-index.mjs videos/<slug>
// buildIndex(dir, { thumb: true }) arma en cambio <project>/miniatura/index.html: la portada (escena hook) quieta,
// con el personaje en la pose de spec.miniatura, sin subtítulo, barra de progreso ni audio → miniatura de YouTube.
import { spawnSync } from "node:child_process";
import { copyFileSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
export const VO_LEAD = 0.25; // voice starts this long after its frame opens
const TAIL = 0.75; // breathing room after the line ends
const RIG = { x: 470, y: 1500, scale: 0.9 }; // spec.rig overrides (e.g. rowing: machine needs more room)
const POSE_KEYS = ["s", "t", "b", "hd", "ua", "fa", "s2", "t2", "ua2", "fa2", "rx", "ry", "ft", "ft2", "hx", "hy", "ed", "lr", "al", "hb", "bf", "bx", "by", "g2", "hx2", "hy2", "ed2", "wr", "wr2", "cv", "fx", "dh", "pz", "rp", "ul"];
const SHIN = 230, THIGH = 240; // = runtime.js L.shin / L.thigh
const deg = (r) => (r * 180) / Math.PI, rad = (d) => (d * Math.PI) / 180;

// Pose helpers (rig px, near ankle of the standing pose at 0,0, floor y = +34):
//   hip: [x, y]             → keeps s/t and computes rx/ry so the hip lands there (floor / kneeling poses).
//   hip + ankle: [x, y]     → solves s/t (2-bone IK, knee bows forward/up; knee: "back" flips it) — feet fixed + hip placed
//                             (rowing, squats on a box…). rx/ry = ankle.
//   + ankle2: [x, y]        → also solves the far leg (s2/t2) from the same hip (pedaling: each foot on its own pedal).
function legIK([hx, hy], [ax, ay], back) {
  const dx = hx - ax, dy = hy - ay, d = Math.min(Math.hypot(dx, dy), SHIN + THIGH - 0.5);
  const base = Math.atan2(dy, dx);
  const a = Math.acos((SHIN * SHIN + d * d - THIGH * THIGH) / (2 * SHIN * d));
  const k1 = { x: ax + Math.cos(base + a) * SHIN, y: ay + Math.sin(base + a) * SHIN };
  const k2 = { x: ax + Math.cos(base - a) * SHIN, y: ay + Math.sin(base - a) * SHIN };
  const fwd = k1.y < k2.y ? k1 : k2; // knee up (seated / squatting): the higher solution
  const K = back ? (fwd === k1 ? k2 : k1) : fwd;
  const H = { x: ax + Math.cos(base) * d, y: ay + Math.sin(base) * d };
  return { s: +deg(Math.atan2(K.x - ax, -(K.y - ay))).toFixed(2), t: +deg(Math.atan2(H.x - K.x, -(H.y - K.y))).toFixed(2) };
}
export function normalizePose(p) {
  const q = { s: 0, t: 0, b: 0, hd: 0, ua: 6, fa: 6, rx: 0, ry: 0, ft: 0, hx: 70, hy: -20, ed: 1, lr: 0, al: 1, hb: 0, bf: 0, bx: 0, by: 0, cv: 0, fx: 1, dh: 0, pz: 0, rp: 0, ul: 1, ...p };
  if (p.hip && p.ankle) {
    Object.assign(q, legIK(p.hip, p.ankle, p.knee === "back"));
    q.rx = p.ankle[0]; q.ry = p.ankle[1];
    if (p.ankle2) { const f = legIK(p.hip, p.ankle2, p.knee === "back"); q.s2 = f.s; q.t2 = f.t; }
  } else if (p.hip) {
    q.rx = +(p.hip[0] - Math.sin(rad(q.s)) * SHIN - Math.sin(rad(q.t)) * THIGH).toFixed(2);
    q.ry = +(p.hip[1] + Math.cos(rad(q.s)) * SHIN + Math.cos(rad(q.t)) * THIGH).toFixed(2);
  }
  delete q.hip; delete q.ankle; delete q.ankle2; delete q.knee;
  q.s2 ??= q.s; q.t2 ??= q.t; q.ua2 ??= q.ua; q.fa2 ??= q.fa; q.ft2 ??= q.ft;
  q.g2 ??= -1; q.hx2 ??= q.hx; q.hy2 ??= q.hy; q.ed2 ??= q.ed; q.wr ??= 0; q.wr2 ??= q.wr;
  return q;
}

// Move sugar → plain moves (times relative to the frame):
//   { loop: ["A","B"], at, step, count | until }  alternates poses every `step` s (running, rowing strokes…)
//                                                  until: "end" = hasta el final de la escena (se expande ya con la duración real)
//   { seq: [["A", dur], ["B", dur], …], at, count | until }  repeats a sequence of poses with their own durations
//   { cut: "POSE", at }                            hides the athlete ~0.45 s and jumps to POSE (unrelated positions)
function expandMoves(f, frameDur) {
  const out = [], cuts = [];
  for (const m of f.moves || []) {
    if ((m.loop || m.seq) && m.until === "end" && frameDur == null) continue; // still unknown: no extiende la escena
    if (m.loop || m.seq) {
      const seq = m.seq || m.loop.map((k) => [k, m.step || 0.4]);
      let t = m.at, i = 0, n = 0;
      const end = m.until === "end" ? frameDur - 0.15 : m.until ?? Infinity, count = m.count ?? Infinity;
      while (n < count) {
        const [to, dur] = seq[i % seq.length];
        if (t + dur > end + 1e-6) break;
        out.push({ to, at: +t.toFixed(3), dur, ease: m.ease || "sine.inOut" });
        t += dur; i++;
        if (i % seq.length === 0) n++;
      }
    } else if (m.cut) {
      cuts.push(m.at);
      out.push({ to: m.cut, at: +(m.at + 0.2).toFixed(3), dur: 0.04, ease: "none" });
      if (m.grip != null) out.push({ grip: m.grip, at: +(m.at + 0.2).toFixed(3), dur: 0.04 });
    } else out.push(m);
  }
  return { moves: out, cuts };
}

// hyperframes ≥ 0.8 guarda los snapshots en .hyperframes/artifacts/snapshots/<id>/ (antes: snapshots/).
// collectShots copia la tanda más nueva a <dir>/snapshots/ para que las rutas de siempre sigan funcionando.
export function collectShots(dir) {
  const base = join(dir, ".hyperframes", "artifacts", "snapshots");
  const out = join(dir, "snapshots");
  if (!existsSync(base)) return out;
  const runs = readdirSync(base).map((d) => join(base, d)).filter((d) => statSync(d).isDirectory());
  if (!runs.length) return out;
  const last = runs.sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs)[0];
  if (existsSync(out) && statSync(out).mtimeMs > statSync(last).mtimeMs) return out;
  rmSync(out, { recursive: true, force: true });
  mkdirSync(out, { recursive: true });
  for (const f of readdirSync(last)) copyFileSync(join(last, f), join(out, f));
  return out;
}

export const THUMB_AT = 2.6; // instante de la miniatura: entradas de texto, tags y personaje ya completas

export function buildIndex(projectDir, { thumb = false } = {}) {
  const P = resolve(projectDir);
  const spec = JSON.parse(readFileSync(join(P, "exercise.json"), "utf8"));
  const metaPath = join(P, "audio_engine_meta.json");
  const meta = existsSync(metaPath) ? JSON.parse(readFileSync(metaPath, "utf8")) : { voices: [] };
  const voice = Object.fromEntries((meta.voices || []).map((v) => [v.id, v]));
  const warnings = [];

  const poses = Object.fromEntries(Object.entries(spec.poses).map(([k, v]) => [k, normalizePose(v)]));
  const RIGX = { ...RIG, ...(spec.rig || {}) };
  const cutTimes = [];
  let frames = spec.frames.map((f, i) => {
    const e = expandMoves(f);
    return { ...f, rawMoves: f.moves, moves: e.moves, cutsRel: e.cuts, id: f.id || String(i + 1).padStart(2, "0") };
  });
  if (thumb) {
    const hook = frames.find((f) => f.kind === "hook") || frames[0];
    frames = [{ ...hook, moves: [], rawMoves: null, cutsRel: [], overlays: [], chips: null, numeral: null, min: THUMB_AT + 0.4 }];
    voice[hook.id] = undefined;
  }

  // Durations: voice-driven, never shorter than the frame's last scheduled action.
  let t = 0;
  for (const f of frames) {
    const v = voice[f.id];
    const acts = [...(f.moves || []).map((m) => m.at + m.dur), ...(f.overlays || []).map((o) => o.at + 0.6), ...(f.chips || []).map((c) => c.at + 0.5)];
    const need = Math.max(f.min || 4, v ? VO_LEAD + v.duration_s + TAIL : 0, acts.length ? Math.max(...acts) + 0.45 : 0);
    if (!v && !thumb) warnings.push(`frame ${f.id}: sin voz generada`);
    f.start = +t.toFixed(3);
    f.dur = +need.toFixed(3);
    t += f.dur;
  }
  const total = +t.toFixed(3);
  frames.forEach((f) => { if (f.rawMoves) f.moves = expandMoves({ moves: f.rawMoves }, f.dur).moves; });
  frames.forEach((f) => f.cutsRel.forEach((c) => cutTimes.push(+(f.start + c).toFixed(3))));

  // Moves → absolute fromTo tweens with explicit from-state (seek-safe).
  const mini = spec.miniatura || {};
  const initialPose = thumb ? mini.pose || spec.initialPose || Object.keys(poses)[0] : spec.initialPose || Object.keys(poses)[0];
  if (!poses[initialPose]) throw new Error(`miniatura: pose desconocida "${initialPose}"`);
  const cur = { ...poses[initialPose], g: thumb ? mini.grip ?? poses[initialPose].g ?? 0 : spec.initialGrip ?? poses[initialPose].g ?? 0 };
  const initialState = { ...cur };
  const all = [];
  frames.forEach((f) => (f.moves || []).forEach((m) => all.push({ ...m, t: f.start + m.at, frame: f.id })));
  all.sort((a, b) => a.t - b.t);
  const moves = all.map((m) => {
    if (m.grip != null) {
      const mv = { keys: ["g"], from: { g: cur.g }, to: { g: m.grip }, t: +m.t.toFixed(3), dur: m.dur, ease: m.ease };
      cur.g = m.grip;
      return mv;
    }
    if (!poses[m.to]) throw new Error(`frame ${m.frame}: pose desconocida "${m.to}"`);
    const from = {}, to = {};
    // Una pose puede traer su agarre ("g": 0/1): se mezcla junto con el resto de la pose.
    const keys = poses[m.to].g != null ? [...POSE_KEYS, "g"] : POSE_KEYS;
    keys.forEach((k) => { from[k] = cur[k]; to[k] = poses[m.to][k]; cur[k] = poses[m.to][k]; });
    return { keys, from, to, t: +m.t.toFixed(3), dur: m.dur, ease: m.ease };
  });

  const overlays = [];
  frames.forEach((f) =>
    (f.overlays || []).forEach((o) => {
      const end = o.out != null ? f.start + o.out : f.start + f.dur - 0.35;
      overlays.push({ ...o, t: +(f.start + o.at).toFixed(3), end: +end.toFixed(3) });
    }),
  );

  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
  const clip = (id, f, cls, inner, track, innerAttrs = "") =>
    `<div id="${id}" class="clip ${cls}" data-start="${f.start}" data-duration="${f.dur}" data-track-index="${track}"><div class="inner"${innerAttrs}>${inner}</div></div>`;

  const runtimeFrames = frames.map((f) => {
    const rf = { id: f.id, start: f.start, dur: f.dur, kind: f.kind || "step", numeral: f.numeral || null, stance: !!f.stance, shrink: f.shrink, scroll: thumb ? 0 : f.scroll ?? null };
    if (f.topview) rf.topview = { angle: f.topview.angle ?? -62, at: f.topview.at === null ? null : f.topview.at ?? 1.0, dur: f.topview.dur ?? 1.6, back: f.topview.back ?? null, mode: f.topview.mode || null, from: f.topview.from ?? 1, plates: !!f.topview.plates };
    if (f.keys) {
      const v = voice[f.id];
      rf.keyTimes = f.keys.map((k, i) => {
        const cue = (typeof k === "object" && k.cue) || null;
        const w = cue && (v?.words || []).find((w) => w.text.toLowerCase().normalize("NFD").replace(/[^a-z]/g, "").startsWith(cue));
        const rel = w ? VO_LEAD + w.start - 0.1 : (typeof k === "object" && k.at) ?? 1.0 + i * 1.3;
        return +(f.start + rel).toFixed(3);
      });
    }
    if (f.chips) rf.chips = f.chips.map((c) => +(f.start + c.at).toFixed(3));
    return rf;
  });

  const textBlocks = frames.map((f) => {
    const head = f.head.map((h) => `<span class="hl">${esc(h)}</span>`).join("");
    const hero = f.kind === "hook";
    let inner = `<div class="badge">${esc(f.badge || "")}</div><h1 class="headline${hero ? " hero" : ""}">${head}</h1>`;
    if (f.sub) inner += `<p class="subline">${esc(f.sub)}</p>`;
    if (hero && spec.tags?.length) inner += `<div class="tags">${spec.tags.map((x) => `<span class="chip-tag">${esc(x)}</span>`).join("")}</div>`;
    if (f.keys)
      inner += `<ul id="keys-${f.id}" class="keys">${f.keys
        .map((k, i) => `<li id="key-${f.id}-${i}"><span class="tick"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span>${esc(typeof k === "object" ? k.text : k)}</span></li>`)
        .join("")}</ul>`;
    return clip(`txt-${f.id}`, f, "scene-text", inner, 3);
  });
  const numerals = frames.filter((f) => f.numeral).map((f) => clip(`num-${f.id}`, f, "numeral", esc(f.numeral), 1, ' data-layout-ignore aria-hidden="true"'));
  const subs = thumb ? [] : frames.map((f) => clip(`sub-${f.id}`, f, "subtitle", `<p>${esc(f.vo)}</p>`, 5));
  const extras = [];
  frames.forEach((f) => {
    if (f.stance)
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="feetcard-${f.id}" class="feetcard"><div class="lbl">VISTA DE ARRIBA</div>
          <svg viewBox="0 0 252 300">
            <rect x="52" y="70" width="52" height="130" rx="26" fill="#3B3FA3"/>
            <rect x="148" y="70" width="52" height="130" rx="26" fill="#3B3FA3"/>
            <line x1="78" y1="20" x2="78" y2="250" stroke="#E85D5D" stroke-width="4" stroke-dasharray="10 8"/>
            <line x1="174" y1="20" x2="174" y2="250" stroke="#E85D5D" stroke-width="4" stroke-dasharray="10 8"/>
            <g id="hipwidth-${f.id}" class="hipwidth"><line x1="84" y1="235" x2="168" y2="235" stroke="#1A1A1A" stroke-width="5"/>
              <path d="M84 235 l14 -10 v20 z M168 235 l-14 -10 v20 z" fill="#1A1A1A"/></g>
            <text x="126" y="290" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="#1A1A1A">${esc(f.stanceLabel || "ANCHO DE CADERA")}</text>
          </svg>
        </div>
      </div>`);
    if (f.topview?.mode === "front")
      // Vista de frente con brazos que siguen la pose de perfil (runtime: frontCards). plates: discos en las manos.
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="topcard-${f.id}" class="feetcard topcard"><div class="lbl">VISTA DE FRENTE</div>
          <svg viewBox="0 0 252 300">
            <line x1="114" y1="180" x2="110" y2="262" stroke="#3F3F9A" stroke-width="18" stroke-linecap="round"/>
            <line x1="138" y1="180" x2="142" y2="262" stroke="#3F3F9A" stroke-width="18" stroke-linecap="round"/>
            <rect x="100" y="88" width="52" height="94" rx="18" fill="#2FB3A6"/>
            <circle cx="126" cy="64" r="20" fill="#E8B383"/>
            <path d="M106 60 C 106 36 146 36 146 60 C 138 50 114 50 106 60 Z" fill="#6B3B1F"/>
            ${["L", "R"].map((sd) => `<line id="fcu${sd}-${f.id}" stroke="#E8B383" stroke-width="13" stroke-linecap="round"/>
            <line id="fcf${sd}-${f.id}" stroke="#E8B383" stroke-width="12" stroke-linecap="round"/>
            <circle id="fch${sd}-${f.id}" r="7" fill="#E8B383"/>${f.topview.plates ? `<circle id="fcp${sd}-${f.id}" r="13" fill="#7C7F86" stroke="#5E6168" stroke-width="3"/>` : ""}`).join("")}
            <text x="126" y="294" text-anchor="middle" font-family="Inter" font-weight="800" font-size="20" fill="#1A1A1A">${esc(f.topview.label || "HOMBROS")}</text>
          </svg>
        </div>
      </div>`);
    else if (f.topview?.mode === "lean")
      // Vista de frente (lat stretch en la pared): pared a la izquierda; tronco + brazo arriba se inclinan hacia ella.
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="topcard-${f.id}" class="feetcard topcard"><div class="lbl">VISTA DE FRENTE</div>
          <svg viewBox="0 0 252 300">
            <rect x="18" y="10" width="14" height="262" fill="#D9D2C5"/>
            <line x1="114" y1="180" x2="106" y2="262" stroke="#3F3F9A" stroke-width="18" stroke-linecap="round"/>
            <line x1="138" y1="180" x2="146" y2="262" stroke="#3F3F9A" stroke-width="18" stroke-linecap="round"/>
            <g id="tvlegs-${f.id}">
              <rect x="102" y="96" width="48" height="86" rx="18" fill="#2FB3A6"/>
              <line x1="108" y1="104" x2="42" y2="24" stroke="#E8B383" stroke-width="14" stroke-linecap="round"/>
              <line x1="146" y1="106" x2="160" y2="170" stroke="#D29A68" stroke-width="13" stroke-linecap="round"/>
              <circle cx="126" cy="76" r="20" fill="#6B3B1F"/>
            </g>
            <text x="126" y="294" text-anchor="middle" font-family="Inter" font-weight="800" font-size="20" fill="#1A1A1A">${esc(f.topview.label || "CADERA AFUERA")}</text>
          </svg>
        </div>
      </div>`);
    else if (f.topview?.mode === "rot")
      // Vista de arriba (hombro en la pared): pared arriba, mano apoyada; los hombros rotan alejándose.
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="topcard-${f.id}" class="feetcard topcard"><div class="lbl">VISTA DE ARRIBA</div>
          <svg viewBox="0 0 252 300">
            <rect x="10" y="22" width="232" height="14" fill="#D9D2C5"/>
            <circle cx="196" cy="44" r="10" fill="#E8B383"/>
            <g id="tvlegs-${f.id}">
              <line x1="190" y1="150" x2="196" y2="50" stroke="#E8B383" stroke-width="14" stroke-linecap="round"/>
              <rect x="96" y="128" width="108" height="44" rx="20" fill="#2FB3A6"/>
              <circle cx="150" cy="150" r="22" fill="#6B3B1F"/>
            </g>
            <text x="126" y="292" text-anchor="middle" font-family="Inter" font-weight="800" font-size="20" fill="#1A1A1A">${esc(f.topview.label || "ROTÁ EL TORSO")}</text>
          </svg>
        </div>
      </div>`);
    else if (f.topview?.mode === "twist")
      // Vista de arriba del russian twist: piernas fijas; hombros, brazos y balón giran (tvlegs = grupo que rota).
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="topcard-${f.id}" class="feetcard topcard"><div class="lbl">VISTA DE ARRIBA</div>
          <svg viewBox="0 0 252 300">
            <rect x="98" y="150" width="22" height="96" rx="11" fill="#3F3F9A"/>
            <rect x="132" y="150" width="22" height="96" rx="11" fill="#3F3F9A"/>
            <rect x="96" y="128" width="60" height="48" rx="20" fill="#3F3F9A"/>
            <g id="tvlegs-${f.id}">
              <rect x="80" y="104" width="92" height="44" rx="20" fill="#2FB3A6"/>
              <line x1="92" y1="118" x2="122" y2="56" stroke="#E8B383" stroke-width="16" stroke-linecap="round"/>
              <line x1="160" y1="118" x2="130" y2="56" stroke="#D29A68" stroke-width="16" stroke-linecap="round"/>
              <circle cx="126" cy="42" r="22" fill="#2E2E33"/>
              <circle cx="126" cy="126" r="22" fill="#6B3B1F"/>
            </g>
            <text x="126" y="292" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="#1A1A1A">${esc(f.topview.label || "ROTÁ EL TORSO")}</text>
          </svg>
        </div>
      </div>`);
    else if (f.topview?.mode === "bar")
      // Vista de arriba del burpee lateral: barra vertical con discos; el atleta acostado al lado salta al otro lado.
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="topcard-${f.id}" class="feetcard topcard"><div class="lbl">VISTA DE ARRIBA</div>
          <svg viewBox="0 0 252 300">
            <rect x="120" y="14" width="12" height="250" rx="6" fill="#A4A8B0"/>
            <rect x="104" y="30" width="44" height="18" rx="6" fill="#7C7F86"/>
            <rect x="104" y="230" width="44" height="18" rx="6" fill="#7C7F86"/>
            <g id="tvlegs-${f.id}">
              <circle cx="126" cy="70" r="20" fill="#6B3B1F"/>
              <rect x="104" y="92" width="44" height="88" rx="18" fill="#2FB3A6"/>
              <rect x="106" y="176" width="16" height="72" rx="8" fill="#3F3F9A"/>
              <rect x="130" y="176" width="16" height="72" rx="8" fill="#3F3F9A"/>
            </g>
            <text x="126" y="292" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="#1A1A1A">${esc(f.topview.label || "SALTO LATERAL")}</text>
          </svg>
        </div>
      </div>`);
    else if (f.topview?.mode === "9090")
      // Vista de arriba sentado en 90/90: pierna de adelante y de atrás en L; el grupo se espeja (scaleX) = cambio de lado.
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="topcard-${f.id}" class="feetcard topcard"><div class="lbl">VISTA DE ARRIBA</div>
          <svg viewBox="0 0 252 300">
            <g id="tvlegs-${f.id}">
              <line x1="136" y1="160" x2="150" y2="236" stroke="#3F3F9A" stroke-width="30" stroke-linecap="round"/>
              <line x1="150" y1="236" x2="58" y2="250" stroke="#E8B383" stroke-width="20" stroke-linecap="round"/>
              <line x1="146" y1="150" x2="222" y2="166" stroke="#31317E" stroke-width="30" stroke-linecap="round"/>
              <line x1="222" y1="166" x2="232" y2="78" stroke="#D29A68" stroke-width="20" stroke-linecap="round"/>
            </g>
            <line x1="62" y1="104" x2="190" y2="104" stroke="#E8B383" stroke-width="20" stroke-linecap="round"/>
            <rect x="92" y="88" width="68" height="78" rx="26" fill="#2FB3A6"/>
            <circle cx="126" cy="106" r="25" fill="#6B3B1F"/>
            <text x="126" y="292" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="#1A1A1A">${esc(f.topview.label || "RODILLAS A 90°")}</text>
          </svg>
        </div>
      </div>`);
    else if (f.topview)
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="topcard-${f.id}" class="feetcard topcard"><div class="lbl">VISTA DE ARRIBA</div>
          <svg viewBox="0 0 252 300">
            <line x1="22" y1="86" x2="230" y2="86" stroke="#E8B383" stroke-width="20" stroke-linecap="round"/>
            <g id="tvlegs-${f.id}">
              <rect x="100" y="166" width="22" height="104" rx="11" fill="#3F3F9A"/>
              <rect x="130" y="166" width="22" height="104" rx="11" fill="#3F3F9A"/>
              <rect x="101" y="246" width="20" height="30" rx="10" fill="#3B3FA3"/>
              <rect x="131" y="246" width="20" height="30" rx="10" fill="#3B3FA3"/>
            </g>
            <rect x="96" y="70" width="60" height="112" rx="22" fill="#2FB3A6"/>
            <circle cx="126" cy="44" r="24" fill="#6B3B1F"/>
            <line x1="14" y1="62" x2="238" y2="62" stroke="#E85D5D" stroke-width="4" stroke-dasharray="10 8"/>
            <text x="126" y="296" text-anchor="middle" font-family="Inter" font-weight="800" font-size="20" fill="#1A1A1A">${esc(f.topview.label || "HOMBROS EN EL PISO")}</text>
          </svg>
        </div>
      </div>`);
    if (f.chips)
      extras.push(`<div id="fx-${f.id}" class="clip" data-start="${f.start}" data-duration="${f.dur}" data-track-index="4">
        <div id="chips-${f.id}" class="chips">${f.chips.map((c, i) => `<div id="chip-${f.id}-${i}">${esc(c.label)}</div>`).join("")}</div>
      </div>`);
  });

  const audio = frames
    .filter((f) => voice[f.id] && !thumb)
    .map((f) => `<audio id="vo-${f.id}" src="${voice[f.id].path}" data-start="${+(f.start + VO_LEAD).toFixed(3)}" data-duration="${voice[f.id].duration_s}" data-track-index="10" data-volume="1"></audio>`);

  // Shared music bed (plantilla/musica/bgm-base.wav, ~177s, pre-looped with crossfades) trimmed to length.
  let bgm = "";
  const bed = join(HERE, "musica", "bgm-base.wav");
  if (!thumb && spec.music !== false && existsSync(bed)) {
    mkdirSync(join(P, "assets", "bgm"), { recursive: true });
    const out = join(P, "assets", "bgm", "track-long.wav");
    const r = spawnSync("ffmpeg", ["-y", "-loglevel", "error", "-i", bed, "-t", String(total + 1), out]);
    if (r.status === 0) {
      const vol = spec.musicVolume ?? 0.18;
      bgm = `<audio id="bgm" src="assets/bgm/track-long.wav" data-start="0" data-duration="${total}" data-track-index="11" data-volume="${vol}" data-automation='{"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0},{"t":1.2,"v":${vol}},{"t":${+(total - 2).toFixed(2)},"v":${vol}},{"t":${total},"v":0}]}]}'></audio>`;
    } else warnings.push("ffmpeg falló al preparar la música");
  }

  const f2 = frames[1] || frames[0];
  const config = { total, rig: RIGX, props: spec.props || [], cuts: cutTimes, floorScroll: thumb ? 0 : spec.floorScroll || 0, poses, initialState, initialPose, moves, overlays, frames: runtimeFrames, colors: spec.colors || null, fingers: !!spec.fingers };
  const runtime = readFileSync(join(HERE, "runtime.js"), "utf8");
  const css = readFileSync(join(HERE, "styles.css"), "utf8");

  const html = `<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
${css}${thumb ? `
      /* miniatura: personaje más grande y más abajo (spec.miniatura.zoom / dy) */
      #stage { transform: translateY(${mini.dy ?? 230}px) scale(${mini.zoom ?? 1.3}); transform-origin: 540px 1532px; }
      #hatch { transform: translateY(${(mini.dy ?? 230) / 2}px); }` : ""}
    </style>
  </head>
  <body>
    <!-- GENERADO por plantilla/build-index.mjs desde exercise.json — no editar a mano -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="${total}" data-width="1080" data-height="1920">
      <div id="bg" class="clip" data-start="0" data-duration="${total}" data-track-index="0"><div id="hatch"></div></div>
      ${numerals.join("\n      ")}
      <div id="stage" class="clip" data-start="0" data-duration="${total}" data-track-index="2">
        <div id="floor-shadow"${spec.shadow === false ? ' style="display:none"' : RIGX.x !== RIG.x ? ` style="left:${RIGX.x - 140}px"` : ""}></div>
        <div id="floor"></div>
        <svg viewBox="0 0 1080 1920">
          <g id="athlete"><g id="rig" transform="translate(${RIGX.x},${RIGX.y}) scale(${RIGX.scale})"></g></g>
          <g id="overlays"></g>
        </svg>
      </div>
      ${thumb ? "" : `<div id="topbar" class="clip" data-start="${f2.start}" data-duration="${+(total - f2.start).toFixed(3)}" data-track-index="4"><div class="inner"><span><b>${esc(spec.name.toUpperCase())}</b></span><span>${esc(spec.category || "CROSSFIT")}</span></div></div>`}
      ${textBlocks.join("\n      ")}
      ${extras.join("\n      ")}
      ${subs.join("\n      ")}
      ${thumb ? "" : `<div id="progress" class="clip" data-start="0" data-duration="${total}" data-track-index="6"><div id="progress-fill"></div></div>`}
      ${audio.join("\n      ")}
      ${bgm}
    </div>
    <script>
      window.__EX_CONFIG = ${JSON.stringify(config)};
${runtime}
    </script>
  </body>
</html>
`;
  if (thumb) {
    const T = join(P, "miniatura");
    mkdirSync(T, { recursive: true });
    for (const f of ["hyperframes.json", "meta.json", "package.json"]) if (existsSync(join(P, f))) writeFileSync(join(T, f), readFileSync(join(P, f)));
    writeFileSync(join(T, "index.html"), html);
    return { dir: T, at: THUMB_AT, pose: initialPose };
  }
  writeFileSync(join(P, "index.html"), html);
  return { total, frames: frames.map((f) => ({ id: f.id, start: f.start, dur: f.dur })), warnings, voices: Object.keys(voice).length, music: !!bgm };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const dir = process.argv[2];
  if (!dir) {
    console.error("uso: node plantilla/build-index.mjs videos/<slug>");
    process.exit(1);
  }
  const r = buildIndex(dir);
  console.log(`✓ index.html — ${r.frames.length} escenas, ${r.total}s, voces ${r.voices}, música ${r.music ? "sí" : "no"}`);
  r.warnings.forEach((w) => console.log(`  ⚠ ${w}`));
}
