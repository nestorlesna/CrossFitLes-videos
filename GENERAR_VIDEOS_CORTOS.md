# GENERAR_VIDEOS_CORTOS — videos cortos sin voz (2–3 repeticiones)

> **Para el modelo / agente que lee esto:** orden de trabajo para generar el **video corto** de un ejercicio que ya
> tiene ficha (`ejercicios/<slug>.json`). No hay que escribir nada nuevo: el corto se arma solo desde la ficha.
> Sirve para cualquier herramienta (Claude Code, opencode, Codex, Cursor…) y cualquier modelo.

## Qué es

Un video vertical 1080×1920 de ~8–16 s que **solo muestra cómo se hace el ejercicio**:

- Es la **portada** del video largo: categoría, nombre (en pantalla), tags, el personaje con el implemento y la barra de progreso.
- **Sin voz** (ni Daniela ni el nombre en inglés) y **sin subtítulos**. **Con la música** de siempre (`bgm-base.wav`, con fundido).
- El movimiento sale de los `moves` de la escena `hook` de la ficha, repetido varias veces.

## Cómo se genera

```bash
export HF_PKG=hyperframes@0.9.8          # si npx no baja la última versión (ver BITACORA)
node plantilla/make-exercise.mjs <slug> --corto
```

Tarda ~1–2 min (no hay voz ni snapshots). Sale en **`salida/<slug>.corto.mp4`** — **siempre sin prefijo** (nunca `OC_`, `OC_2_`, etc., aunque el largo lo tenga):

| Largo hoy | Corto |
|---|---|
| `salida/dumbbell-overhead-hold.mp4` | `salida/dumbbell-overhead-hold.corto.mp4` |
| `salida/OC_2_air-squat.mp4` (con prefijo) | `salida/air-squat.corto.mp4` (sin prefijo) |
| todavía sin video largo | `salida/<slug>.corto.mp4` |

- El nombre es el slug del ejercicio; el prefijo del largo no se usa. **No renombres a mano.**
- Si el largo está en `salida/subidos/`, el corto igual sale en `salida/` (no toques `subidos/`).
- Flags: `--check` corre `hyperframes check` sobre el corto (por defecto no, ya pasó en el largo).
- El proyecto del corto vive en `videos/<slug>/corto/` (se regenera siempre; no editar a mano).

## Cuántas repeticiones (regla automática, `plantilla/build-index.mjs`)

1. Si la portada tiene un ciclo (`seq` / `loop` con `until: "end"`): se repite ese ciclo **3 veces**.
2. Si son solo transiciones (`to` / `cut`): se repite **toda la cadena** 3 veces (sin corte entre repeticiones si termina en la pose inicial).
3. Si 3 repeticiones pasarían de **16 s** → **2** repeticiones.
4. Si 3 repeticiones dan menos de **8 s** (ejercicios rápidos: correr, saltos, pedalear) → se suman repeticiones hasta llegar a 8 s.
5. Queda una cola de 0,8 s al final. Las constantes están arriba en `build-index.mjs` (`CORTO_MIN`, `CORTO_MAX`).

Si el movimiento de la portada no se ve bien como demostración (se ve una sola fase, o corta feo), **no cambies el
runtime**: ajustá los `moves` del `hook` en la ficha (eso también mejora el largo) y volvé a generar.

## Registro (CHECKLIST.md)

La columna **Corto** del `CHECKLIST.md` (autogenerada con `node plantilla/make-exercise.mjs --checklist`) muestra:
`[✅ <duración>](ruta)` si existe el corto · `⬜` si falta · `⚠️ desactualizado` si la ficha cambió después.
El estado se guarda en `videos/<slug>/.pipeline.json` (`corto`, `cortoHash`, `cortoFecha`, `cortoReps`).
El encabezado de cada tabla dice **Cortos: N**.

## Procedimiento por tanda

1. Elegí los ejercicios (los que pida el usuario, o los primeros con **Corto ⬜** de la tabla, en orden).
2. Para cada uno: `node plantilla/make-exercise.mjs <slug> --corto` (2–3 a la vez como máximo; es liviano).
3. Mirá el resultado: `ffmpeg -i salida/<archivo>.corto.mp4 -vf "fps=1/2,scale=300:-1,tile=7x1" -frames:v 1 hoja.png` y revisá que el título no se pise, que se vean las repeticiones completas y que el implemento acompañe.
4. Regenerá el CHECKLIST y reportá en castellano rioplatense: lista de cortos (nombre, repeticiones, duración) y cualquier duda.

## Reglas fijas

- No cambies la música, el estilo visual ni el tamaño. Sin voz y sin subtítulos.
- No hagas `git commit` ni `git push` salvo pedido explícito.
- Los videos de máquinas (`M*`) y del dataset (`D*`) se hacen igual **después** de tener su ficha (`GENERAR_VIDEOS_MAQUINAS.md` / `GENERAR_VIDEOS_DATASET.md`); la ficha ya trae el `hook` que usa el corto.

## Subirlos a YouTube

Por grupos que pide el profe, desde Studio con Chrome, a la lista **«Videos cortos de ejercicios»**: ver `SUBIR-A-YOUTUBE.md` § 6 quater. Título/descripción/tags: `node plantilla/corto-youtube.mjs <slug>` → `salida/<slug>.corto.youtube.txt`. Registro: `cortos-subidos.csv` + columna **Corto subido** del CHECKLIST.

Vinculación corto ↔ largo (link en la descripción + Vídeo relacionado) y su bitácora `BITACORA-VINCULOS.md`: `SUBIR-A-YOUTUBE.md` § 6 quinquies.
