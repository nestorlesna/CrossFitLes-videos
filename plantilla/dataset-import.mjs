// Importa el dataset externo de ejercicios (exercises-dataset, 1324 ejercicios con GIF de referencia) y arma
// ejercicios/dataset.csv con los que TODAVÍA NO están en ejercicios.csv ni en maquinas.csv.
//
//   node plantilla/dataset-import.mjs [carpeta-del-dataset]
//
// Carpeta por defecto: C:\DATOS\DESARROLLOS\React\CrossFitLes\BKP\exercises-dataset-main (o env DATASET_DIR).
// Es re-ejecutable: regenera dataset.csv completo. Las equivalencias a mano (ejercicio del dataset que YA tenemos con
// otro nombre) van en ejercicios/dataset-equivalencias.csv (id;clave;motivo) y se excluyen de la lista.
// Las fichas/videos ya hechos no se tocan: la clave de cada fila se mantiene estable (slug del nombre del dataset).
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "..");
const DIR = resolve(process.argv[2] || process.env.DATASET_DIR || "C:/DATOS/DESARROLLOS/React/CrossFitLes/BKP/exercises-dataset-main");
const data = JSON.parse(readFileSync(join(DIR, "data", "exercises.json"), "utf8"));

// Mismo parser que make-exercise.mjs (no se importa: importar make-exercise.mjs ejecuta su main()).
function readCsv(name) {
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
  const [head, ...rest] = rows;
  return rest.filter((r) => r.length > 1 && r[0]).map((r) => Object.fromEntries(head.map((k, i) => [k, (r[i] || "").trim()])));
}

const csv = readCsv("ejercicios.csv"), maq = readCsv("maquinas.csv");
const equiv = new Map(readCsv("dataset-equivalencias.csv").map((r) => [r.id, r]));

// ---- nombres -------------------------------------------------------------------------------------------
// El dataset trae "°" roto ("в°") y variantes que son la misma animación desde otro ángulo o con otro modelo.
const fixName = (s) => s.replace(/в°/g, "°").replace(/\s+/g, " ").trim();
const baseName = (s) => fixName(s).toLowerCase()
  .replace(/\((back|side|front) pov\)/g, "").replace(/\(?\b(male|female)\b\)?/g, "").replace(/\s+/g, " ").trim();
const SMALL = new Set(["a", "and", "of", "on", "the", "to", "with", "in", "at", "for", "or", "v."]);
const title = (s) => fixName(s).split(" ").map((w, i) => (i && SMALL.has(w) ? w : w.replace(/^([("']?)(\p{L})/u, (_, p, c) => p + c.toUpperCase()))).join(" ")
  .replace(/\bEz\b/g, "EZ").replace(/\bJm\b/g, "JM").replace(/\bV-bar\b/gi, "V-Bar");
const slugify = (s) => fixName(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/°/g, "")
  .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

// Parecido con lo que ya existe (pista para el que hace la ficha: "variante de …"), Jaccard de palabras.
const SYN = { biceps: "bicep", lever: "machine", pullup: "pull up", pushup: "push up", situp: "sit up", raises: "raise", curls: "curl", rows: "row", lunges: "lunge", squats: "squat", extensions: "extension", climbers: "climber", dips: "dip", triceps: "tricep", flyes: "fly", flys: "fly" };
const STOP = new Set(["the", "with", "to", "on", "a", "of", "and", "v", "version", "male", "female", "pov"]);
const toks = (s) => fixName(s).toLowerCase().replace(/['’`]/g, "").replace(/[^a-z0-9]+/g, " ").trim().split(" ")
  .map((w) => SYN[w] || w).join(" ").split(" ").filter((w) => w && !STOP.has(w));
const known = [...csv.map((r) => ({ k: r.clave, n: r.nombre })), ...maq.map((r) => ({ k: r.clave, n: r.nombre }))].map((x) => ({ ...x, t: toks(x.n) }));
const jac = (a, b) => { const A = new Set(a), B = new Set(b); let i = 0; A.forEach((w) => B.has(w) && i++); return i / (A.size + B.size - i); };
const similar = (name) => {
  const t = toks(name);
  let best = null, s = 0;
  for (const x of known) { const v = jac(t, x.t); if (v > s) { s = v; best = x; } }
  return s >= 0.5 ? best.k : "";
};

// ---- castellano ----------------------------------------------------------------------------------------
const ZONA = { waist: "Core", "upper legs": "Piernas", back: "Espalda", "lower legs": "Pantorrillas", chest: "Pecho", "upper arms": "Brazos", cardio: "Cardio", shoulders: "Hombros", "lower arms": "Antebrazos", neck: "Cuello" };
const MUSC = {
  abs: "Abdominales", quads: "Cuádriceps", lats: "Dorsales", calves: "Gemelos", pectorals: "Pectorales", glutes: "Glúteos", hamstrings: "Isquiotibiales", adductors: "Aductores", triceps: "Tríceps", "cardiovascular system": "Sistema cardiovascular", spine: "Erectores espinales", "upper back": "Espalda alta", biceps: "Bíceps", delts: "Deltoides", forearms: "Antebrazos", traps: "Trapecios", "serratus anterior": "Serrato anterior", abductors: "Abductores", "levator scapulae": "Elevador de la escápula",
  "hip flexors": "Flexores de cadera", "lower back": "Zona lumbar", obliques: "Oblicuos", rhomboids: "Romboides", "ankle stabilizers": "Estabilizadores del tobillo", shoulders: "Hombros", core: "Core", back: "Espalda", quadriceps: "Cuádriceps", chest: "Pecho", "rear deltoids": "Deltoides posteriores", trapezius: "Trapecios", ankles: "Tobillos", feet: "Pies", deltoids: "Deltoides", brachialis: "Braquial", groin: "Ingle", wrists: "Muñecas", "rotator cuff": "Manguito rotador", "upper chest": "Pecho superior", "latissimus dorsi": "Dorsales", "wrist flexors": "Flexores de muñeca", "wrist extensors": "Extensores de muñeca", abdominals: "Abdominales", "grip muscles": "Agarre", "lower abs": "Abdominales inferiores", "inner thighs": "Aductores", soleus: "Sóleo", sternocleidomastoid: "Esternocleidomastoideo", hands: "Manos", shins: "Tibiales",
};
const musc = (m) => MUSC[m] || m;

// ---- familia (orden de producción), implemento y prop de runtime.js -------------------------------------
// formato: "maquina" → GENERAR_VIDEOS_MAQUINAS.md (90–150 s) · "corto" → GENERAR_VIDEOS.md (40–52 s).
const FAMILIAS = [
  { id: "palanca", nombre: "Máquinas de palanca", eq: ["leverage machine"], impl: "Máquina de palanca", formato: "maquina" },
  { id: "trineo", nombre: "Prensa / hack (trineo)", eq: ["sled machine"], impl: "Prensa de trineo", formato: "maquina" },
  { id: "smith", nombre: "Máquina Smith", eq: ["smith machine"], impl: "Máquina Smith", formato: "maquina" },
  { id: "polea", nombre: "Poleas", eq: ["cable"], impl: "Polea", formato: "maquina" },
  { id: "cardio", nombre: "Máquinas de cardio", eq: ["upper body ergometer", "skierg machine", "stationary bike", "elliptical machine", "stepmill machine"], impl: "Máquina de cardio", formato: "maquina" },
  { id: "barra", nombre: "Barra", eq: ["barbell", "olympic barbell", "trap bar"], impl: "Barra olímpica", formato: "corto" },
  { id: "barraz", nombre: "Barra Z", eq: ["ez barbell"], impl: "Barra Z", formato: "corto" },
  { id: "mancuernas", nombre: "Mancuernas", eq: ["dumbbell"], impl: "Mancuernas", formato: "corto" },
  { id: "kettlebell", nombre: "Kettlebell", eq: ["kettlebell"], impl: "Kettlebell", formato: "corto" },
  { id: "banda", nombre: "Bandas elásticas", eq: ["band", "resistance band"], impl: "Banda elástica", formato: "corto" },
  { id: "lastre", nombre: "Con lastre", eq: ["weighted"], impl: "Disco / lastre", formato: "corto" },
  { id: "pelotas", nombre: "Balón medicinal, fitball y bosu", eq: ["medicine ball", "stability ball", "bosu ball"], impl: "", formato: "corto" },
  { id: "accesorios", nombre: "Rodillo, rueda, soga, maza y cubierta", eq: ["roller", "wheel roller", "rope", "hammer", "tire"], impl: "", formato: "corto" },
  { id: "asistido", nombre: "Estiramientos y ejercicios asistidos", eq: ["assisted"], impl: "Ninguno", formato: "corto" },
  { id: "corporal", nombre: "Peso corporal", eq: ["body weight"], impl: "Ninguno", formato: "corto" },
];
const IMPL = { "trap bar": "Barra hexagonal", "upper body ergometer": "Ergómetro de brazos", "skierg machine": "SkiErg", "stationary bike": "Bicicleta fija", "elliptical machine": "Elíptico", "stepmill machine": "Escaladora", "medicine ball": "Balón medicinal", "stability ball": "Fitball", "bosu ball": "Bosu", roller: "Rodillo de espuma", "wheel roller": "Rueda abdominal", rope: "Soga", hammer: "Maza", tire: "Cubierta de tractor" };
const famOf = (eq) => FAMILIAS.find((f) => f.eq.includes(eq)) || FAMILIAS.at(-1);

// Prop(s) sugeridos para runtime.js. Los que no existen todavía figuran como "(falta dibujar)" en el CHECKLIST.
const first = (n, rules, def) => (rules.find(([re]) => re.test(n)) || [, def])[1];
const conBanco = (n) => /bench|incline|decline|lying|seated|preacher|pullover|fly|skull/.test(n) && !/floor/.test(n);
function props(e) {
  const n = fixName(e.name).toLowerCase();
  const plus = (p) => (conBanco(n) ? `${p} + bench` : p);
  switch (e.equipment) {
    case "leverage machine": return first(n, [
      [/leg press/, "legpress"], [/hack/, "hacksquat"], [/pendulum/, "pendulum"], [/leg extension/, "legextension"],
      [/lying .*curl|leg curl.*lying/, "lyinglegcurl"], [/leg curl/, "seatedlegcurl"], [/calf/, /seated/.test(n) ? "seatedcalf" : "standingcalf"],
      [/preacher/, "preachercurl"], [/lateral raise/, "lateralraise"], [/fly|pec deck/, "pecdeck"], [/crunch/, "abcrunch"],
      [/abduction/, "hipabduction"], [/adduction/, "hipadduction"], [/hip thrust|glute/, "hipthrust"], [/pulldown/, "latpulldown"],
      [/chest press|bench press|incline .*press|decline .*press/, "chestpress"], [/shoulder press|military/, "shoulderpress"],
      [/dip/, "seateddip"], [/back extension|hyperextension/, "backext45"], [/chin-up|pull-up/, "assisted"],
      [/row/, "leverrow"], [/shrug/, "levershrug"]], "lever");
    case "sled machine": return first(n, [[/hack/, "hacksquat"]], "legpress");
    case "smith machine": return plus("smith");
    case "cable": return first(n, [[/cross-?over|fly/, "cablecrossover"], [/seated .*row|low .*row/, "cablerow"], [/pulldown/, "latpulldown"]], "cable");
    case "upper body ergometer": return "handbike";
    case "skierg machine": return "skierg";
    case "stationary bike": return "stationarybike";
    case "elliptical machine": return "elliptical";
    case "stepmill machine": return "stairclimber";
    case "barbell": case "olympic barbell": return plus("barbell");
    case "trap bar": return "trapbar";
    case "ez barbell": return plus("ezbar");
    case "dumbbell": return plus("dumbbell");
    case "kettlebell": return "kettlebell";
    case "band": case "resistance band": return "band";
    case "weighted": return first(n, [[/pull-up|chin-up|muscle up|hanging/, "pullupbar + plate"], [/dip/, "dipbars + plate"]], plus("plate"));
    case "medicine ball": return "wallball";
    case "stability ball": return "stabilityball";
    case "bosu ball": return "bosu";
    case "roller": return "foamroller";
    case "wheel roller": return "abwheel";
    case "rope": return first(n, [[/battling/, "battlerope"], [/rope climb/, "rope"], [/jump rope/, "jumprope"]], "strap");
    case "hammer": return "sledgehammer + tire";
    case "tire": return "tire";
    default: return first(n, [[/pull-up|chin-up|muscle.?up|hanging|toes to bar|skin the cat/, "pullupbar"], [/parallel bars|dip cage|straight bar dip|chest dip|^dips?\b|korean dip|impossible dip/, "dipbars"],
      [/bench dip|three bench|on bench|bench/, "bench"], [/wall/, "wall"], [/box|step-up/, "box"]], "");
  }
}

// ---- armar la lista -------------------------------------------------------------------------------------
const csvClaves = new Set([...csv, ...maq].map((r) => r.clave));
const vistos = new Map(); // nombre base → id (la primera animación de cada ejercicio)
const filas = [], excluidos = { equivalentes: 0, duplicados: 0 };
for (const e of data) {
  if (equiv.has(e.id)) { excluidos.equivalentes++; continue; }
  const base = baseName(e.name);
  if (vistos.has(base)) { excluidos.duplicados++; continue; }
  vistos.set(base, e.id);
  const fam = famOf(e.equipment);
  let clave = slugify(base);
  if (csvClaves.has(clave)) clave = `${clave}-ds`; // mismo nombre que algo que ya existe pero con otro ejercicio
  for (let n = 2; filas.some((f) => f.clave === clave); n++) clave = `${slugify(base)}-${n}`; // "push-up (wall)" / "push-up wall"
  const pasos = (l) => (e.instruction_steps?.[l] || []).map((s) => s.trim()).join(" · ");
  filas.push({
    clave,
    id_dataset: e.id,
    lote: "",
    familia: fam.nombre,
    formato: fam.formato,
    nombre: title(base),
    nombre_es: "",
    equipo_dataset: e.equipment,
    implemento: IMPL[e.equipment] || fam.impl,
    props: props(e),
    zona: ZONA[e.body_part] || e.body_part,
    musculo_objetivo: musc(e.target),
    grupo_muscular: musc(e.muscle_group),
    musculos_secundarios: (e.secondary_muscles || []).map(musc).join(", "),
    similar_a: similar(e.name),
    descripcion_es: (e.instructions?.es || "").trim(),
    pasos_es: pasos("es"),
    pasos_en: pasos("en"),
    gif: join(DIR, e.gif_url).replace(/\\/g, "/"),
    imagen: join(DIR, e.image).replace(/\\/g, "/"),
    atribucion: e.attribution || "",
  });
}

// Orden de producción: por familia; dentro de la familia primero los que ya tienen el prop dibujado
// (se pueden hacer ya), después por prop (así un dibujo nuevo sirve para varios seguidos) y por nombre.
const runtime = readFileSync(join(HERE, "runtime.js"), "utf8");
const dibujado = (p) => p.split(" + ").every((x) => !x || runtime.includes(`pr.type === "${x}"`));
const famIdx = (f) => FAMILIAS.findIndex((x) => x.nombre === f);
filas.sort((a, b) => famIdx(a.familia) - famIdx(b.familia) || dibujado(b.props) - dibujado(a.props) || a.props.localeCompare(b.props) || a.nombre.localeCompare(b.nombre));
// Lotes de 10 dentro de cada familia: D01, D02… (numeración corrida).
let lote = 0, prevFam = null, enLote = 0;
for (const f of filas) {
  if (f.familia !== prevFam || enLote === 10) { lote++; enLote = 0; prevFam = f.familia; }
  enLote++;
  f.lote = `D${String(lote).padStart(2, "0")} · ${f.familia}`;
}

const cols = Object.keys(filas[0]);
const q = (v) => `"${String(v ?? "").replace(/"/g, '""').replace(/\r?\n/g, " ")}"`;
writeFileSync(join(ROOT, "ejercicios", "dataset.csv"), "﻿" + [cols.map(q).join(";"), ...filas.map((f) => cols.map((c) => q(f[c])).join(";"))].join("\r\n") + "\r\n");

const sinProp = [...new Set(filas.flatMap((f) => f.props.split(" + ")).filter((p) => p && !dibujado(p)))];
console.log(`✓ ejercicios/dataset.csv — ${filas.length} ejercicios nuevos en ${lote} lotes`);
console.log(`  dataset: ${data.length} · ya los tenemos (dataset-equivalencias.csv): ${excluidos.equivalentes} · misma animación repetida (pov/male/female): ${excluidos.duplicados}`);
console.log(`  props a dibujar en runtime.js: ${sinProp.join(", ") || "ninguno"}`);
for (const fam of FAMILIAS) {
  const n = filas.filter((f) => f.familia === fam.nombre);
  if (n.length) console.log(`  ${fam.nombre}: ${n.length} (${n.filter((f) => dibujado(f.props)).length} con el prop ya dibujado)`);
}
