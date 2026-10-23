# GENERAR_VIDEOS — instructivo para generar videos de ejercicios

> **Para el modelo / agente que lee esto:** este archivo es una orden de trabajo completa. Seguilo paso a paso, en orden,
> sin saltear verificaciones. Está escrito para que lo pueda ejecutar cualquier herramienta (Claude Code, opencode,
> ChatGPT/Codex, Cursor, Aider…) y cualquier modelo. No asumas nada que no esté acá o en los archivos que se indican.
>
> **Videos de máquinas de gimnasio** (lista `ejercicios/maquinas.csv`, sección 🏋️ del CHECKLIST, `#` M1, M2…):
> seguí además **`GENERAR_VIDEOS_MAQUINAS.md`**, que cambia la lista, la duración (90–150 s), las escenas y YouTube.

---

## Cómo usarlo (para el usuario): prompts de ejemplo

Abrí la herramienta (opencode, Claude Code, ChatGPT/Codex, Cursor…) en la carpeta `VidesoEjercicios/` y pegá uno de estos:

**Con prefijo (ej. opencode):**
```
Leé y seguí GENERAR_VIDEOS.md al pie de la letra.
CANTIDAD: 5
PREFIJO: OC
```

**Sin prefijo (como siempre):**
```
Seguí GENERAR_VIDEOS.md. Generá 10 videos.
```

**Ejercicios elegidos a mano:**
```
Seguí GENERAR_VIDEOS.md. CANTIDAD: 3. PREFIJO: GPT.
EJERCICIOS: goblet-squat-hold-press, burpee, push-up
```

**Solo fichas, para revisar antes de renderizar (útil con modelos baratos):**
```
Seguí GENERAR_VIDEOS.md. CANTIDAD: 4. SOLO_FICHAS: sí.
No renderices; avisame cuando estén los contact sheets.
```

Consejos: con modelos chicos pedí pocos videos por vez (3–5). Si la herramienta no puede ver imágenes, va a usar poses
de fichas ya probadas y te va a avisar que no revisó los contact sheets.

---

## 0. Parámetros que da el usuario

El usuario te llama con algo como *"Seguí GENERAR_VIDEOS.md. Cantidad: 5. Prefijo: OC"*. Leé estos parámetros del mensaje:

| Parámetro | Obligatorio | Default | Qué hace |
|---|---|---|---|
| `CANTIDAD` | sí | — | Cuántos videos nuevos generar. |
| `PREFIJO` | no | *(vacío)* | Si el usuario lo dice (ej. `OC`), el video final sale como `salida/OC_<slug>.mp4`. **Si el usuario no dice nada, NO uses prefijo**: el archivo sale `salida/<slug>.mp4`, como siempre. Nunca inventes un prefijo según la herramienta o el modelo que sos. |
| `EJERCICIOS` | no | los próximos de la lista | Lista de slugs o números del CHECKLIST si el usuario quiere unos en particular (puede elegir fuera de orden). |
| `SOLO_FICHAS` | no | no | Si el usuario pide "sin renderizar", hacé todo menos el `--render`. |

El prefijo solo se aplica con el flag `--prefijo=<PREFIJO>` del paso 5.6 (sin espacios, sin guion bajo final: `--prefijo=OC`,
no `--prefijo=OC_`). El script agrega el `_`, guarda el nombre en `videos/<slug>/.pipeline.json` (`archivo`) y el
CHECKLIST lo encuentra solo. **No renombres archivos a mano.**

Si falta `CANTIDAD`, preguntala. Ante cualquier otra duda de técnica de un ejercicio, decidí vos con criterio de coach
de CrossFit y anotalo en el reporte final; solo preguntá si es una duda real que cambia el movimiento.

---

## 1. Qué es este proyecto (contexto mínimo)

- Videos instructivos de ejercicios de CrossFit para alumnos de un box. Verticales **1080×1920**, ~40–52 s, en
  **español rioplatense con voseo** ("flexioná", "tomá", "bajá", "parate"), voz en off + subtítulo + música de fondo.
- El personaje es un atleta SVG plano dibujado por `plantilla/runtime.js`, en **vista lateral mirando a la derecha**.
- Motor de video: **HyperFrames** (CLI vía `npx --prefer-offline hyperframes`). Voz: **Piper** local con la voz
  **Daniela es_AR** (`plantilla/piper-tts.py`), salvo el **nombre del ejercicio en la portada, que lo dice en inglés
  la voz Kokoro "Heart"** (`af_heart`) y después sigue Daniela en castellano (ver 6.7). Música: `plantilla/musica/bgm-base.wav`.
  Todo es local y gratis.
- **Un ejercicio = un archivo** `ejercicios/<slug>.json` (la "ficha"). Es lo único que se escribe a mano.
  Todo lo demás lo genera `node plantilla/make-exercise.mjs`.

```
ejercicios/ejercicios.csv   lista maestra (separador ";", UTF-8 con BOM). Orden de filas = orden de producción
ejercicios/<slug>.json      ficha del ejercicio (la escribís vos)
ejercicios/completados.csv  huecos del CSV que completaste vos (clave;campo;valor)
ejercicios/maquinas.csv     lista de videos de máquinas de gimnasio (ver GENERAR_VIDEOS_MAQUINAS.md)
maquinas_gimnasio.xlsx      planilla de máquinas del usuario (no editar: de ahí sale maquinas.csv)
ejercicios/dataset.csv      ejercicios del dataset externo que faltan (ver GENERAR_VIDEOS_DATASET.md; lo arma plantilla/dataset-import.mjs)
videos/<slug>/              proyecto HyperFrames generado (no editar a mano: index.html se regenera siempre)
videos/_poselab/<slug>/     laboratorio de poses
salida/[PREFIJO_]<slug>.mp4 video final
salida/<slug>.youtube.txt   título + descripción + tags (autogenerado desde la ficha)
salida/<slug>.miniatura.png miniatura 1080×1920 (autogenerada)
salida/subidos/             videos ya publicados: los mueve el usuario a mano. NUNCA muevas nada de/para ahí
CHECKLIST.md                estado de todos los ejercicios (autogenerado, no editar a mano)
plantilla/README.md         REFERENCIA COMPLETA del formato de la ficha (poses, escenas, props, overlays)
plantilla/BITACORA.md       problemas ya resueltos (leer antes de arrancar)
```

**Lectura obligatoria antes de empezar** (en este orden): este archivo → `plantilla/README.md` → `plantilla/BITACORA.md`.
El README es la especificación exacta de cada campo; este archivo es el procedimiento y las reglas aprendidas.

---

## 2. Reglas fijas (no negociables)

1. Idioma: español rioplatense con voseo en voz, subtítulos, textos en pantalla y descripción de YouTube. Nada formal.
2. No cambies la voz (Daniela + nombre en inglés con Kokoro `af_heart`), la música, el tamaño ni el estilo visual.
   No propongas otras voces.
3. No edites `videos/<slug>/index.html` ni `CHECKLIST.md` a mano: se regeneran. Los cambios van en la ficha JSON.
4. No toques `salida/subidos/` ni muevas archivos de salida.
5. **No hagas `git commit` ni `git push`** salvo que el usuario lo pida explícitamente.
6. No modifiques fichas de videos ya hechos salvo que el usuario lo pida.
7. Si cambiás algo de `plantilla/` (runtime, builder), documentalo en `plantilla/README.md` y en `plantilla/BITACORA.md`.
8. Toda ficha nueva lleva `"revisado": false`. Solo el usuario aprueba videos.
9. Un video **no está terminado** sin: ficha + voz + check + render + `youtube` + miniatura.
10. Al terminar cada problema nuevo que resuelvas, agregá una fila a la tabla de `plantilla/BITACORA.md`
    (`| MM-DD | slug | Problema | Solución / regla |`).

---

## 3. Verificar el entorno (una vez, al principio)

Corré desde la raíz del proyecto (`VidesoEjercicios/`):

```bash
node -v                                   # Node 20+ (probado con 24)
python -c "import piper; print('ok')"     # si falla: python -m pip install piper-tts
ffprobe -version                          # FFmpeg instalado (para duraciones)
ls plantilla/voces-piper                  # deben estar es_AR-daniela-high.onnx y .onnx.json
python -c "import kokoro_onnx; print('ok')"   # voz del nombre en inglés; si falla: python -m pip install kokoro-onnx
ls ~/.cache/hyperframes/tts/models/kokoro-v1.0.onnx   # o plantilla/voces-kokoro/kokoro-v1.0.onnx (ver abajo)
ls plantilla/musica/bgm-base.wav
ls .claude/skills/hyperframes             # skills de HyperFrames (si faltan: npx skills add heygen-com/hyperframes)
```

Si falta el modelo de voz, bajalo (114 MB, no está en git) a `plantilla/voces-piper/`:
`https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_AR/daniela/high/es_AR-daniela-high.onnx` y el mismo con `.onnx.json`.

Si falta Kokoro (voz del nombre en inglés, 325 MB + 28 MB, no está en git), bajá a `plantilla/voces-kokoro/`:
`https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx` y
`https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin`.
`piper-tts.py` lo busca ahí y, si no está, en `~/.cache/hyperframes/tts/` (donde lo deja HyperFrames).

Si algo de esto falla y no lo podés arreglar, frená y avisale al usuario qué falta.

---

## 4. Elegir los ejercicios

1. Corré `node plantilla/make-exercise.mjs --checklist` y abrí `CHECKLIST.md`. Los videos de este archivo son los de
   la tabla principal; **no tomes filas de la sección 🏋️ Máquinas** salvo que el usuario lo pida (esas van con
   `GENERAR_VIDEOS_MAQUINAS.md`).
2. Si el usuario dio `EJERCICIOS`, usá esos. Si no, tomá los **primeros `CANTIDAD` de la tabla que tengan Ficha ⬜**,
   en el orden de la tabla (= orden del CSV). La línea "**Próximo:**" arriba de la tabla dice cuál es el primero.
3. Para cada uno mirá la columna **Implemento**. Implementos que ya están dibujados en `runtime.js` (prop → ficha ejemplo):

| Implemento del CSV | `props[].type` | Copiar de la ficha |
|---|---|---|
| Ninguno | — | `air-squat`, `squat-to-stand`, `cat-cow`, `v-up` |
| Remo (Rower) | `rower` | `rowing` |
| Kettlebell | `kettlebell` (`hand: "far"`, `swing: true`) | `kettlebell-good-morning-to-squat`, `kettlebell-farmer-carry`, `kettlebell-swing` |
| Barra olímpica | `barbell` (`torso`, `blend`) | `barbell-back-squat`, `barbell-front-squat`, `barbell-thruster`, `barbell-clean-and-jerk` |
| Barra en el piso | `floorbar` | `burpee-over-the-bar` |
| Wall ball / Balón medicinal | `wallball` (`wall:false`, `depth`, `mirror`) | `wall-ball-shot`, `russian-twist`, `partner-wall-ball-sit-up` |
| Disco (chico) | `barbell` con `r: 40` | `cuban-press` |
| Mancuernas | `dumbbell` (`hand`, `side`) | `alternating-single-arm-dumbbell-power-snatch`, `weighted-lunge`, `dumbbell-push-press` |
| Assault bike | `airbike` | `assault-bike` |
| Barra de dominadas | `pullupbar` | `hanging-toes-to-bar` |
| Trineo (Sled) | `sled` | `sled-push-pull`, `sled-push` |
| SkiErg | `skierg` | `skierg` |
| Cajón (Box) | `box` | `box-jump`, `box-jump-over`, `box-step-up` |
| Cuerda para saltar | `jumprope` | `jump-rope` |
| Pared | `wall` | `wall-sit`, `wall-lat-stretch`, `wall-thoracic-extensions` |
| Banda elástica | `band` | `band-triceps-pushdown`, `band-external-rotation` |
| Compañero | `partner` | `partner-wall-ball-sit-up` |
| 🏋️ Prensa 45° (máquina) | `legpress` | `leg-press` (ver `GENERAR_VIDEOS_MAQUINAS.md`) |
| 🏋️ Jalón al pecho (máquina, pila de peso) | `latpulldown` | `lat-pulldown` (ver `GENERAR_VIDEOS_MAQUINAS.md`) |
| 🏋️ Resto de las máquinas de gimnasio (35) | ver la tabla de Implementos de `plantilla/README.md` | la ficha de esa máquina (`GENERAR_VIDEOS_MAQUINAS.md`) |

4. **Si el implemento NO está en la tabla** (ej. anillas, cuerda de trepar, GHD, paralelas): hay que programarlo en
   `plantilla/runtime.js` (bloque PROPS). Si no te sentís seguro de hacerlo bien, **salteá ese ejercicio**, tomá el
   siguiente de la lista para completar la cantidad y anotá en el reporte final cuáles salteaste y por qué.
   Si lo programás: piezas fijas en `propBack`, partes móviles con `propUpdates.push((n, f) => …)`, escenario fijo
   (que no se espeja) con `propStatic`; documentalo en la tabla de Implementos del README y en la BITÁCORA.
5. Para cada ejercicio corré `node plantilla/make-exercise.mjs <slug> --info` y leé: `nombre, categoria, implemento,
   posicion, zonas, dosis, descripcion, tecnica_coach, errores, dificultad`.
   - Si falta `descripcion` o `tecnica_coach`: completala vos en `ejercicios/ejercicios.csv` y agregá una línea en
     `ejercicios/completados.csv` con el formato `clave;campo;valor`. No toques `ejercicios.original.csv`.

---

## 5. Procedimiento por ejercicio

### 5.1 Pensar el movimiento (antes de escribir nada)

Escribí (para vos) en 5–8 líneas: posición inicial, 3–4 fases del movimiento, la pose más reconocible (para la
miniatura), 3–4 claves de técnica (de `tecnica_coach`) y 1–2 errores típicos que se puedan mostrar.
Preguntate: **¿se ve bien de perfil?** Si el movimiento es lateral, rotación o apertura de brazos, se necesita una
tarjeta `topview` (ver 6.6) o claves de escorzo (`lr`, `al`, `ul`, `fl`, `ll`).

### 5.2 Escribir la ficha SOLO con poses

Copiá como base la ficha más parecida de la tabla del punto 4 y creá `ejercicios/<slug>.json` con `frames: []`
(vacío) y todas las poses que vas a necesitar (4–8 suele alcanzar, más los "errores" con sufijo `_BAD`).

> Tip que funcionó muy bien: generar la ficha con un **script Python** guardado como archivo (no heredocs largos en
> bash: se rompen con comillas y backticks). Leé el deslinde con `open('plantilla/youtube-deslinde.txt', encoding='utf-8')`,
> armá el dict y `json.dump(..., ensure_ascii=False, indent=2)` a `ejercicios/<slug>.json` con `encoding='utf-8'`.
> Calculá las poses difíciles con geometría (ver 6.3: largos de segmentos).

### 5.3 Probar las poses

```bash
node plantilla/pose-lab.mjs <slug>              # todas las poses
node plantilla/pose-lab.mjs <slug> BOTTOM,TOP   # solo algunas
```

Mirá `videos/_poselab/<slug>/snapshots/contact-sheet.jpg` (una celda por pose). Revisá: pies en el piso (no flotan ni
atraviesan), manos donde corresponde, implemento en su lugar, cabeza no atraviesa el piso, el personaje entra en el cuadro.
Iterá 2–3 veces. Si la hoja sale **vacía** (sin personaje), casi seguro hay un error de JavaScript en `runtime.js`
o una pose con un valor inválido.

> Si tu herramienta **no puede ver imágenes**, igual corré el pose-lab y el check, usá solo poses copiadas de fichas
> probadas (ajustando poco) y avisá en el reporte que el contact sheet no se revisó visualmente.

### 5.4 Escribir las escenas, la descripción de YouTube y la miniatura

Ver la sección 6 (estructura exacta). Completá `frames`, `youtube`, `miniatura`, `pronuncia` (si el nombre es en inglés)
y `notas` (una línea si hiciste algo nuevo; si no, `""`).

### 5.5 Generar y revisar

```bash
node plantilla/make-exercise.mjs <slug>
```

Tarda ~5–6 min (voz + index.html + `hyperframes check` + snapshots + miniatura). Después:

1. Leé la salida: `✓ index.html — N escenas, Xs` y las advertencias `⚠`. Duración total esperable: **40–52 s**.
2. `hyperframes check` debe pasar. Si marca errores de **contenido** (texto cortado en el borde, texto que pisa el
   subtítulo, elementos superpuestos), corregí la ficha y volvé a correr. Si el error es
   `Browser process did not exit` o un timeout del navegador, **no es de contenido**: volvé a correr con menos procesos
   en paralelo.
3. Mirá `videos/<slug>/snapshots/contact-sheet.jpg` (un cuadro por escena) y `salida/<slug>.miniatura.png`.
   Lo más común: 1–2 labels que pisan el cuerpo o el subtítulo → movelos (ver 6.5).

La voz solo se regenera si cambió el texto (`--force-tts` la fuerza). Para rehacer solo la miniatura:
`node plantilla/make-exercise.mjs <slug> --miniatura` (rápido).

### 5.6 Renderizar

Sin prefijo (el usuario no dijo nada):
```bash
node plantilla/make-exercise.mjs <slug> --render
```
Con prefijo (el usuario dijo, por ejemplo, "prefijo OC"):
```bash
node plantilla/make-exercise.mjs <slug> --render --prefijo=OC
```
Resultado: `salida/<slug>.mp4` o `salida/OC_<slug>.mp4`. El render vuelve a hacer el check y los snapshots (~6–8 min
en total). Corrélo en segundo plano si tu herramienta lo permite y mientras tanto avanzá con las poses del siguiente.

### 5.7 Cerrar el ejercicio

- Confirmá que existe el `.mp4` en `salida/` (con o sin prefijo) y que el CHECKLIST lo muestra con Render ✅.
- Si resolviste algo nuevo, fila en `plantilla/BITACORA.md`.

---

## 6. Cómo escribir la ficha (lo aprendido en 70 videos)

### 6.1 Esqueleto completo

```jsonc
{
  "slug": "air-squat",                          // = nombre del archivo, = clave del CSV
  "name": "Air Squat",                          // nombre del CSV
  "category": "CROSSFIT · ENTRADA EN CALOR",    // "CROSSFIT · " + categoría en MAYÚSCULAS. Máx. 2 partes (si el CSV trae
                                                //  "Entrada en calor, WOD" usá una sola) o se pisa con el nombre
  "tags": ["Piernas", "Glúteos", "Core"],       // 2–3 zonas cortas para los chips de la portada
  "descripcion": "texto de descripcion del CSV",
  "revisado": false,
  "notas": "",
  "music": true, "musicVolume": 0.18,
  "rig": { "x": 500, "y": 1500, "scale": 0.9 }, // encuadre del personaje (ver 6.4)
  "pronuncia": { "Air Squat": "Er scuat" },     // solo para la voz (ver 6.7)
  "initialPose": "STAND",
  "props": [],                                  // implementos (ver tabla del punto 4 y README)
  "poses": { "STAND": { "s": 0, "t": 0, "b": 0, "hd": 0, "g": 0, "ua": 4, "fa": 6 } },
  "frames": [ /* escenas, ver 6.2 */ ],
  "miniatura": { "pose": "BOTTOM", "grip": 0 },
  "youtube": { "titulo": "...", "descripcion": "...", "tags": [] }
}
```

Ejemplo real completo y simple para copiar: **`ejercicios/air-squat.json`**.

### 6.2 Escenas (`frames`) — estructura estándar de 7 escenas

| # | `kind` | badge | head (Bebas, 1–2 líneas, **máx. ~14 caracteres c/u**) | vo | `min` |
|---|---|---|---|---|---|
| 1 | `hook` | categoría | nombre en 2 líneas | "<Nombre>: <qué es en una frase>. <para qué>." (empieza con el `name` **exacto**, ver 6.7) | 4.5–5 |
| 2 | (step) | `POSICIÓN INICIAL` | ej. "PIES / AL ANCHO" | cómo pararse/ubicarse | 5–5.5 |
| 3–5 | (step) con `numeral` "1".."3/4" | `PASO 1 / 4` … | acción corta | "Paso uno. …" | 5–6 |
| 6 | `keys` | `CLAVES` | `TÉCNICA` | "Claves: a, b, c y d." | 7–8 |
| 7 | `reps` | `A ENTRENAR` | dosis ("12 REPS", "30 SEG", "400 M") | dosis + ritmo | 6–7 |

Reglas de las escenas:
- `vo`: **máx. ~130 caracteres (3 líneas de subtítulo)**. Más largo desborda el subtítulo. Voseo siempre.
- `sub`: bajada corta (≤ ~32 caracteres).
- La duración real de cada escena = máx(`min`, voz + 1 s, última acción + 0,45 s). Total ideal 40–52 s.
- El `hook` muestra el movimiento completo en loop (`seq` … `"until": "end"`) para enganchar.
- Cada escena de paso empieza con `{ "cut": "POSE", "at": 0 }` o con un `to` desde la pose en la que terminó la anterior.
- `keys`: 3–4 strings cortos (≤ ~30 caracteres). El personaje se achica a 0,8 automáticamente; si queda debajo de la
  lista usá `"shrink": 0.62`. Las piezas de escenario (pared, parante) se atenúan solas.
- `reps`: 3 `chips` `{ "label": "1 · BAJÁ", "at": 0.6 }` con `at` 0.6 / 1.1 / 1.6, y el movimiento en loop.
  **No pongas `topview` en la escena de reps** (los chips ocupan ese lugar).
- Mostrar un error: pose `_BAD` con un label "… NO" y volver a la pose correcta (ver paso 3 de `air-squat`).

Movimientos (`moves`, tiempos relativos a la escena, en segundos):
- `{ "to": "POSE", "at": 0.5, "dur": 0.8 }` transición. `"ease": "none"` para ciclos continuos (pedalear, correr).
- `{ "cut": "POSE", "at": 0 }` aparece directo en otra pose (cambio de posición, ej. del piso a de pie).
- `{ "seq": [["A",0.45],["B",0.45]], "at": 0.8, "until": "end" }` ciclo con tiempos propios.
- `{ "loop": ["A","B"], "at": 0, "step": 0.36, "until": "end" }` alternar dos poses (correr, caminar).
- `{ "grip": 1, "at": 1, "dur": 0.5 }` solo el agarre.

### 6.3 Poses — sistema de coordenadas y valores probados

- Vista lateral mirando a la derecha. Ángulos en grados.
- `s` tibia, `t` muslo, `b` torso, `hd` cabeza: desde la **vertical hacia arriba**, `+` = inclinado hacia adelante.
- `ua` brazo, `fa` antebrazo: desde la **vertical hacia abajo**, `+` = hacia adelante. `ua 180` = brazo arriba.
- Lado lejano: `s2 t2 ua2 fa2` (default = igual al cercano).
- Coordenadas del rig: el tobillo cercano está en (0,0); **el piso es y = +34**; y negativa = arriba.
- Largos aproximados: pierna completa cadera→tobillo ≈ **470 px**; hombro→mano con brazo recto ≈ **330 px**
  (si el agarre está más lejos de 330 del hombro, el brazo no llega).
- `hip: [x,y]` ubica la cadera (el builder calcula el resto). `hip` + `ankle: [x,y]` = pie fijo, IK de la pierna
  (`"knee": "back"` invierte). `ankle2` = IK de la pierna lejana. Ideal para sentadillas, estocadas, remo, cajón.
- Agarre: `g 1` lleva las manos a `hx, hy` (IK); `ed -1` dobla el codo hacia atrás (tirones, remo).
  `g2 / hx2 / hy2` agarre propio de la mano lejana (`g2 -1` = sigue a `g`). `hb 1` = agarre medido desde el hombro
  en el marco del torso.
- Para **sostener algo contra el cuerpo** usá brazos libres `g 0` con ángulos relativos al torso (el IK queda raro):
  goblet `ua = -b + 12, fa = 142`; barra en la espalda `ua = -b - 12, fa = 178`; balón al pecho `ua = -b + 18, fa = 136`;
  rack frontal `ua = 90 - b, fa = 176`.
- Otras claves: `cv` curva de espalda (+ redondea, − hunde); `fx` hacia dónde mira (1 / −1; pasar por 0 = giro);
  `lr` piernas al costado acostado (escorzo); `al` largo del brazo (0.14 = apunta a la cámara); `ul` brazo superior,
  `fl` antebrazo, `ll/ll2` largo de pierna (escorzo); `ft/ft2` rotación del pie; `wr` muñeca con `"fingers": true`.

Poses de partida probadas:

| Pose | Valores |
|---|---|
| De pie | `s 0, t 0, b 0, hd 0, g 0, ua 4, fa 6` |
| Brazos al frente / arriba | `ua 88, fa 0` / `ua 175, fa 0` |
| Media sentadilla | `hip [-80,-380], ankle [0,0], b 22, hd 12` |
| Sentadilla profunda | `hip [-150,-205], ankle [0,0], b 40, hd 24` |
| Talones levantados (error) | `ankle [30,-30], ft -30, ft2 -30` |
| Bisagra piernas rectas | `s -5, t -5, b 128, hd 150` + agarre a los pies |
| Estocada | `s 25, t -60, s2 -60, t2 -10, b 0` + `rx` para centrar |
| Plancha | `s 78, t 78, b 78, hd 85, rx -300`, manos `g 1, hx ≈ 430, hy 15` |
| Cuadrupedia | `hip [0,-231], s 90, t 0, ft 172, b 72`, manos `g 1, hy 15` |
| Sentado piernas estiradas | `hip [-230,0], s -90, t -90, ft -90` |
| Boca arriba rodillas flexionadas | `hip [0,-20] + ankle [300,0], b -90, hd -92` |
| Boca abajo | `hip [-30,-8], s 90, t 90, ft 175, b 92, hd 72` |
| De rodillas / sentado en talones | `hip [-200,-250], t 0` / `hip [-200,-72], t -70` |
| Correr (2 fases) | `hip [0,-415]`, piernas `s 12, t -62` y `s 52, t 28`, brazos `ua ±40` |

Para cualquier otra, buscá en `ejercicios/*.json` una pose parecida y copiala (hay 70 fichas probadas).

### 6.4 Encuadre (`rig`)

- Default de pie: `{ "x": 470–500, "y": 1500, "scale": 0.9 }`. Piso en pantalla ≈ y 1532 (`y + 34·scale`).
- En el piso (acostado, cuadrupedia): `{ "x": 520, "y": 1504, "scale": 0.82 }`.
- Movimientos largos (burpee + salto): `scale ~0.62`. Barra arriba de la cabeza: `scale ~0.66` (si no, la barra tapa los tags).
- `"shadow": false` cuando hay máquina o compañero. `"floorScroll": 150–260` para caminar/correr en el lugar;
  `"scroll"` por escena para cambiar la velocidad del piso (negativo = hacia atrás).

### 6.5 Overlays (marcas de técnica)

Tipos: `line`, `arrow` (`from`, `to`, `bend`, `dur`), `ring` (`pos`, `r`), `bar` (`pos`, `w`, `h`), `label` (`pos`, `text`,
`anchor`). Todos con `at` y opcional `out`. Posiciones en **px del lienzo 1080×1920**: `[x, y]`.

Reglas aprendidas (las que más fallan en el check):
- **Ningún texto con y > 1580** (el subtítulo empieza en 1600). Labels cerca de y≈1500 o por arriba del cuerpo.
- Labels largos cerca de un borde: `anchor` hacia el centro (`"end"` si está a la derecha, `"start"` a la izquierda);
  dejá ≥ 60 px de margen con los bordes (0 y 1080).
- Labels pegados a una articulación caen sobre el cuerpo: usá un offset grande hacia arriba (`dy -250…-330`) o una
  posición absoluta a un costado.
- `{ "j": "POSE.W" }` (posición de una articulación) solo es confiable con agarre `g 1`; con brazos libres poné `[x, y]`
  absoluto. Con `fx -1` también usá posiciones absolutas.
- Texto de labels en MAYÚSCULAS y corto (≤ ~18 caracteres).

### 6.6 Movimientos que no se ven de perfil → tarjeta `topview`

| Movimiento | Solución | Ficha ejemplo |
|---|---|---|
| Ancho de pies | `"stance": true` + `stanceLabel` | `air-squat` |
| Torsión acostado | `topview { angle, at, dur, back, label }` + clave `lr` | `supine-spinal-twist` |
| Rotación sentado con balón | `topview mode twist` + balón `depth`/`pz` | `russian-twist` |
| Hombros / brazos (de frente) | `topview mode front` (`plates: true` con discos) | `cuban-press`, `arm-circles` |
| Inclinación lateral / rotación en pared | `topview mode lean` / `rot` | `wall-lat-stretch`, `wall-shoulder-stretch` |
| Rotación externa con banda | `topview mode er` + clave `fl` | `band-external-rotation` |
| Sentadilla lateral | `topview mode cossack` + claves `ll`, `cs` | `cossack-squat` |
| Salto lateral sobre barra | `topview mode bar` + `floorbar` con `pz` | `burpee-over-the-bar` |
| 90/90 | `topview mode 9090` | `90-90-hip-rotation` |

### 6.7 Nombre en inglés y pronunciación

**Desde 2026-10-21 el nombre del ejercicio lo dice una voz en inglés** (Kokoro `af_heart`, aprobada por el usuario) y
el resto sigue con Daniela, con una pausa corta y un fundido en el medio. Es automático, no hay que configurar nada:
- Si el `vo` del `hook` **empieza con el `name` exacto** (`"Air Squat: la sentadilla…"`), el nombre lo dice la voz
  inglesa y Daniela sigue desde lo que viene después de los dos puntos. **Escribí siempre el hook así.**
- Si el `vo` del hook no empieza con el nombre (ej. `"Elevación de gemelos: …"`), la voz inglesa dice el nombre
  antes y Daniela lee el `vo` completo. Sirve cuando el `vo` arranca con la traducción. No arranques con el nombre
  en inglés recortado (`"Hang Clean:"` en `Barbell Hang Clean`): Daniela lo repetiría mal en inglés.
- Nombres con números o símbolos: `"nombreEnVoz": "Four six breathing"` (cómo lo dice la voz inglesa; el subtítulo
  sigue mostrando el `vo`). Ej.: `4-6 Breathing`, `Sled Push & Pull`, `SkiErg` → `"Ski erg"`, `DB Hang Clean + Jerk`.
- Nombre en castellano (ej. `Descanso`): `"nombreEn": false` y lo dice Daniela, como antes.
- En el hook ya **no hace falta** `"voSpeed": 0.88` ni poner el nombre en `pronuncia` (se ignoran para el nombre).

`"pronuncia"` sigue sirviendo para palabras en inglés que lee Daniela en el **resto** de las escenas
(`"pronuncia": { "kettlebell": "kételbel" }`; solo cambia la voz, el subtítulo queda con el texto real).

**Re-render de videos viejos:** los videos de `salida/` hechos antes del cambio (no los de `salida/subidos/`) se
re-renderizan por lotes con `node plantilla/revoz-en.mjs` (próximo lote de 10; `--lotes=N`, `--todos`, o slugs).
Conserva el nombre del archivo (`OC_` sigue `OC_`). El plan y el avance están al final de `CHECKLIST.md`
(columna **Nombre EN**).

### 6.8 Bloque `youtube` (obligatorio)

- `titulo` (≤ 100 caracteres, ideal ~60): `<Nombre> 🔥 <beneficio> paso a paso | CrossFit`.
- `tags`: 8–15 búsquedas en español (nombre en inglés y en castellano, zona, "crossfit", momento de uso). Total ≤ 500 caracteres.
- `descripcion` (≤ 5000 caracteres, **sin `<` ni `>`**), rioplatense, cercana, con emojis. Estructura fija exacta:

```
🔥 <NOMBRE EN MAYÚSCULAS> — <para qué sirve en una línea>

<gancho de 1–2 frases: el problema que resuelve, "Este ejercicio es para vos."> 💪

📋 PASO A PASO
1️⃣ <posición inicial>
2️⃣ … (los mismos pasos que la voz, en voseo; usá 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣)

✅ CLAVES DE TÉCNICA
• … (las claves del video + tecnica_coach del CSV)

🎯 QUÉ TRABAJA
<zonas del CSV separadas por " · ">

⏱️ CUÁNTO
<dosis> + cuándo usarlo (entrada en calor, WOD, vuelta a la calma)

🙌 Si te sirvió, dejá tu like, guardalo y compartilo con tu compañero de box.

<contenido de plantilla/youtube-deslinde.txt copiado TAL CUAL>

#CrossFit #<Categoría> #<NombreSinEspacios> #<Zona> #Entrenamiento
```

- Si el ejercicio tiene riesgos propios (carga en la espalda, cuelgue, saltos, impacto, olímpicos), sumá una línea antes
  del deslinde: "Si nunca hiciste …, empezá con … y con un coach al lado."
- **La última línea deben ser los hashtags** (el script inserta el crédito de la voz justo antes).
- No hace falta poner el crédito de la voz: se agrega solo al exportar `salida/<slug>.youtube.txt` (Daniela, y
  también Kokoro "Heart" cuando el render dice el nombre en inglés).

### 6.9 Miniatura (obligatoria)

`"miniatura": { "pose": "<la pose más reconocible, no la de pie>", "grip": 0|1 }`. Opcionales `zoom` (default 1.3) y
`dy` (default 230). Acostado o muy horizontal: `zoom: 1.0`. Revisá que no tape los tags y que se lea en chico.

---

## 7. Errores conocidos y su solución (resumen de la BITÁCORA)

| Síntoma | Solución |
|---|---|
| Pie flota o atraviesa el piso | Rodilla/tobillo en y≈+10…+34; usar `hip` + `ankle` y recalcular |
| Brazo no llega al agarre / codo raro | Hombro a ≤ 330 px del agarre; target de manos lejos para que el brazo quede recto; `ed -1` para codo atrás |
| Brazos atraviesan el piso al interpolar | Los ángulos van por el camino corto: usar `ua 270` en vez de `-90` |
| El brazo/mano "salta" | No interpolar `g2` de −1 a 1: poner `g2` igual en las dos poses (`0` o `1`) |
| Brazo cercano tapa la cara | Que el brazo que hace el movimiento sea el **lejano** (`ua2`, `fa2`) |
| Barra en el rack tapa la cara | `barbell` `r 74` con `torso [64, 36]` |
| Barra arriba tapa los tags | `rig.scale ~0.66` |
| Personaje se sale del cuadro | Bajar `scale`, mover `rig.x`, revisar `hip` |
| Entre reps "camina para atrás" | `cut` a la pose inicial en vez de `to` |
| Texto pisa el subtítulo | y ≤ 1580; `vo` ≤ 130 caracteres |
| Nombre + categoría se pisan arriba | categoría de 2 partes como máximo |
| Lista de claves tapa al personaje | `"shrink": 0.62` en la escena `keys`; `wall` con `h` más baja |
| Contact sheet / pose-lab vacío | Error de JS en `runtime.js` o pose inválida |
| `npx hyperframes` tarda minutos | Ya se usa `--prefer-offline`; la primera vez correr uno solo (descarga) |
| `npm ECOMPROMISED` | Correr un solo `make-exercise` primero, después en paralelo |
| `npm error notarget No matching version found for hyperframes@x.y.z` | El `latest` del registro todavía no se baja: `export HF_PKG=hyperframes@<versión en caché>` (ej. `0.8.171`) y repetir |
| `Browser process did not exit` / timeout | No es de contenido: menos procesos en paralelo y repetir |
| Heredoc de bash se corta | Escribir el script en un archivo y ejecutarlo |
| Cajón alto: la pierna no llega | Cajón `h 220` (cadera–tobillo ≤ 470) |

---

## 8. Paralelismo y tiempos

- `pose-lab`: hasta **5** a la vez. `make-exercise` (check/snapshots): **2–3** a la vez. Renders: **2–3** a la vez.
  No corras `make-exercise` mientras hay muchos renders (falla el navegador).
- Tiempos aprox.: pose-lab ~1 min, `make-exercise` ~6 min, `--render` ~7–8 min por video.
- Flujo eficiente con varios videos: poses de todos (pose-lab en paralelo) → escenas → `make-exercise` de a 2–3 →
  `--render` en segundo plano de a 2–3, mientras avanzás con el siguiente.

---

## 9. Al terminar todos

1. `node plantilla/make-exercise.mjs --checklist`
2. Verificá en `CHECKLIST.md` que cada video nuevo tiene: Ficha, Voz, Composición, Check, Render, YouTube, Miniatura y Nombre EN en ✅
   y que la columna Archivo muestra el nombre correcto (`OC_<slug>.mp4` si hubo prefijo).
3. Si aprendiste algo nuevo: filas en `plantilla/BITACORA.md` (y README si cambiaste `plantilla/`).
4. **No hagas commit** (salvo pedido explícito).
5. Reportale al usuario, en castellano rioplatense y corto:

```
Videos generados (N):
- #<n> <Nombre> → salida/<archivo>.mp4 (<duración> s) — <nota si hay algo para revisar>
Salteados: <slug> (falta dibujar <implemento>)   ← solo si hubo
Datos del CSV completados: <clave: campo>        ← solo si hubo
Para revisar: <dudas de técnica que decidiste vos, checks que fallaron, contact sheets no revisados>
```
