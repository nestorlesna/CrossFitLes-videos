// Bitácora de videos cortos vinculados con su video largo (el que explica Daniela).
//   node plantilla/vincular.mjs <slug> --buscar
//        → muestra el ID del largo si ya se conoce (CALENDARIO-YOUTUBE.md o vinculos.csv) y el del corto (cortos-subidos.csv)
//   node plantilla/vincular.mjs <slug> [--largo=<ID>] [--corto=<ID>] [--largo-en-corto=si|no|pendiente] [--corto-en-largo=si|no|pendiente] [--nota="…"]
//        → crea/actualiza la fila de vinculos.csv y regenera BITACORA-VINCULOS.md
//   node plantilla/vincular.mjs --md        → solo regenera BITACORA-VINCULOS.md
// "largo-en-corto" = el corto tiene el link al largo en la descripción Y el largo elegido en «Vídeo relacionado».
// "corto-en-largo" = lo mismo, al revés (el largo apunta al corto).
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const CSV = join(ROOT, "vinculos.csv");
const MD = join(ROOT, "BITACORA-VINCULOS.md");
const COLS = ["slug", "id_largo", "id_corto", "largo_en_corto", "corto_en_largo", "fecha", "nota"];

const read = (f) => (existsSync(f) ? readFileSync(f, "utf8").replace(/\r/g, "").split("\n").filter(Boolean).slice(1).map((l) => l.split(";")) : []);

export function leerVinculos() {
  const o = {};
  for (const c of read(CSV)) o[c[0]] = Object.fromEntries(COLS.map((k, i) => [k, c[i] || ""]));
  return o;
}
// ID del largo ya conocido: vinculos.csv primero, después el calendario de publicación.
export function idLargo(slug) {
  const v = leerVinculos()[slug];
  if (v?.id_largo) return v.id_largo;
  const f = join(ROOT, "CALENDARIO-YOUTUBE.md");
  if (existsSync(f)) {
    for (const l of readFileSync(f, "utf8").split("\n")) {
      const c = l.split("|").map((x) => x.trim());
      if (c[4] === slug && c[5]) return c[5];
    }
  }
  return "";
}
export function idCorto(slug) {
  const v = leerVinculos()[slug];
  if (v?.id_corto) return v.id_corto;
  for (const c of read(join(ROOT, "cortos-subidos.csv"))) if (c[0] === slug) return (c[2] || "").split("/").pop();
  return "";
}

function escribir(o) {
  const filas = Object.values(o).sort((a, b) => a.slug.localeCompare(b.slug));
  writeFileSync(CSV, [COLS.join(";"), ...filas.map((r) => COLS.map((k) => r[k] || "").join(";"))].join("\n") + "\n", "utf8");
  const lk = (id) => (id ? `[${id}](https://youtu.be/${id})` : "—");
  const ic = (v) => (v === "si" ? "✅" : v === "no" ? "⬜" : v || "⬜");
  const nCorto = filas.filter((r) => r.largo_en_corto === "si").length;
  const nLargo = filas.filter((r) => r.corto_en_largo === "si").length;
  const md = `# Bitácora de videos vinculados (corto ↔ largo)

Cada corto (\`<slug>.corto.mp4\`) se vincula con su video largo (el que explica Daniela) y al revés, de dos maneras:
el **link en la descripción** y el campo **Vídeo relacionado** de YouTube Studio. Procedimiento: \`SUBIR-A-YOUTUBE.md\` § 6 quinquies.
Datos en \`vinculos.csv\` (lo escribe \`node plantilla/vincular.mjs\`; no editar a mano).

**Corto → largo:** ${nCorto} · **Largo → corto:** ${nLargo} · Filas: ${filas.length}

| Ejercicio | Largo (Daniela) | Corto | Corto apunta al largo | Largo apunta al corto | Fecha | Nota |
|---|---|---|---|---|---|---|
${filas.map((r) => `| ${r.slug} | ${lk(r.id_largo)} | ${lk(r.id_corto)} | ${ic(r.largo_en_corto)} | ${ic(r.corto_en_largo)} | ${r.fecha || "—"} | ${r.nota || ""} |`).join("\n")}

✅ hecho (descripción + vídeo relacionado) · ⬜ no · pendiente = falta que el otro video esté en YouTube.
`;
  writeFileSync(MD, md, "utf8");
}

const isMain = process.argv[1] && process.argv[1].replace(/\\/g, "/").endsWith("plantilla/vincular.mjs");
if (isMain) {
  const args = process.argv.slice(2);
  const flag = (n) => { const a = args.find((x) => x.startsWith(`--${n}=`)); return a ? a.slice(n.length + 3) : undefined; };
  const slug = args.find((a) => !a.startsWith("--"));
  const o = leerVinculos();
  if (args.includes("--md") && !slug) { escribir(o); console.log("✓ BITACORA-VINCULOS.md"); }
  else if (!slug) { console.error("uso: node plantilla/vincular.mjs <slug> [--buscar | --largo=ID --corto=ID …]"); process.exit(1); }
  else if (args.includes("--buscar")) {
    console.log(JSON.stringify({ slug, id_largo: idLargo(slug) || null, id_corto: idCorto(slug) || null, fila: o[slug] || null }, null, 2));
  } else {
    const r = o[slug] || Object.fromEntries(COLS.map((k) => [k, ""]));
    r.slug = slug;
    r.id_largo = flag("largo") ?? r.id_largo ?? idLargo(slug);
    r.id_corto = flag("corto") ?? r.id_corto ?? idCorto(slug);
    if (!r.id_largo) r.id_largo = idLargo(slug);
    if (!r.id_corto) r.id_corto = idCorto(slug);
    r.largo_en_corto = flag("largo-en-corto") ?? r.largo_en_corto ?? "no";
    r.corto_en_largo = flag("corto-en-largo") ?? r.corto_en_largo ?? "no";
    r.nota = flag("nota") ?? r.nota ?? "";
    r.fecha = new Date().toISOString().slice(0, 10);
    o[slug] = r;
    escribir(o);
    console.log(`✓ ${slug}: largo ${r.id_largo || "—"} · corto ${r.id_corto || "—"} · corto→largo ${r.largo_en_corto} · largo→corto ${r.corto_en_largo}`);
  }
}
