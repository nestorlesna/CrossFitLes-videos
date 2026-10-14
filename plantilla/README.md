# Plantilla de videos de ejercicios

> Antes de empezar un ejercicio nuevo leé también **`plantilla/BITACORA.md`** (problemas ya resueltos y flujo recomendado).

Un ejercicio = una ficha JSON en `ejercicios/<slug>.json`. Todo lo demás se genera.

```
ejercicios/ejercicios.csv  ← lista maestra (export de la app del box); el orden de filas = orden de producción
ejercicios/<slug>.json     ← ficha (lo único que se escribe a mano), incluye la descripción de YouTube
videos/<slug>/             ← proyecto HyperFrames generado (index.html, voz, snapshots, render)
salida/<slug>.mp4          ← video final
salida/<slug>.youtube.txt  ← título + descripción + tags para pegar en YouTube Studio (autogenerado)
salida/<slug>.miniatura.png ← miniatura de YouTube 1080×1920: portada + personaje en la pose clave (autogenerada)
CHECKLIST.md               ← estado de todos los ejercicios de la lista (autogenerado)
salida/subidos/            ← los ya publicados en YouTube (el profe los mueve a mano; el CHECKLIST los marca como Subido)
plantilla/                 ← runtime del personaje, builder, estilos, música base, deslinde de YouTube
```

## Lista maestra (`ejercicios/ejercicios.csv`)

Separador `;`, UTF-8 con BOM. La `clave` es el slug del video. Las columnas que importan para la ficha:
`clave, nombre, categoria, implemento, posicion, zonas, dosis, descripcion, tecnica_coach, grupo_principal, dificultad, tags`
(el resto —`id`, `svg_local`, `video_corto/largo`, estadísticas de uso— es de la app y no se usa).

- Ver la fila de un ejercicio: `node plantilla/make-exercise.mjs <slug> --info`.
- El "próximo" a hacer es el primero de la lista sin ficha (lo muestra el CHECKLIST).
- Si un ejercicio tiene `implemento` distinto de "Ninguno", primero hay que dibujar ese implemento en `runtime.js`.
- Si falta `descripcion` o `tecnica_coach` (el CHECKLIST lo marca en Notas), completarlo en el CSV y anotar el cambio en
  `ejercicios/completados.csv` (`clave;campo;valor`, para que el profe lo revise e importe en su app). Ante una duda real
  sobre la técnica, preguntarle. `ejercicios.original.csv` es el export sin tocar.

## Pasos para un ejercicio nuevo

1. `--info <slug>` → leer descripción, técnica del coach, zonas, dosis, posición e implemento.
2. Copiar `ejercicios/squat-to-stand.json` como base y escribir `ejercicios/<slug>.json`:
   - `category` = `"CROSSFIT · " + categoría` en mayúsculas; `tags` = 2–3 zonas cortas (de `zonas`);
   - escenas: hook → posición inicial → pasos → claves (de `tecnica_coach`) → reps (de `dosis`).
3. Escribir el bloque **`youtube`** (ver abajo) y elegir la pose de la **`miniatura`**. Las dos son obligatorias:
   un video no está terminado sin descripción y miniatura (columnas YouTube y Miniatura del CHECKLIST).
4. `make-exercise <slug>` → contact sheet → ajustar → `--render`.

## Comandos (desde la raíz `VidesoEjercicios/`)

| Comando | Qué hace |
|---|---|
| `node plantilla/make-exercise.mjs <slug>` | crea/actualiza el proyecto, genera la voz (solo si cambió el texto), arma `index.html`, corre `check` y saca snapshots (`videos/<slug>/snapshots/contact-sheet.jpg`) |
| `node plantilla/make-exercise.mjs <slug> --render` | lo anterior + render y copia a `salida/<slug>.mp4` |
| `node plantilla/make-exercise.mjs --checklist` | regenera `CHECKLIST.md` (toda la lista del CSV) y los `salida/*.youtube.txt` |
| `node plantilla/make-exercise.mjs <slug> --miniatura` | solo regenera `salida/<slug>.miniatura.png` (rápido, sin voz ni render) |
| `node plantilla/pose-lab.mjs <slug> [A,B]` | dibuja todas (o algunas) poses de la ficha en `videos/_poselab/snapshots/contact-sheet.jpg` — **usarlo antes de escribir las escenas** |
| `node plantilla/make-exercise.mjs <slug> --info` | muestra la fila del CSV de ese ejercicio |
| `npx hyperframes preview` (dentro de `videos/<slug>`) | revisar en el Studio |

Flags: `--force-tts`, `--no-check`, `--no-snapshot`.

Flujo recomendado: escribir la ficha → `make-exercise <slug>` → mirar el contact sheet / preview → ajustar poses → `--render` → cuando el profe lo aprueba, `"revisado": true` y `--checklist`.

## Formato de la ficha

```jsonc
{
  "slug": "squat-to-stand",            // = nombre del archivo
  "name": "Squat to Stand",
  "category": "CROSSFIT · MOVILIDAD",  // barra superior
  "tags": ["Cadera", "Isquiotibiales"], // chips de la portada
  "descripcion": "texto original del ejercicio",
  // voz: Piper + Daniela (es_AR) por defecto, no hace falta ponerla. "voiceProvider": "kokoro" + "voice": "em_alex" = motor viejo
  "voiceSpeed": 1.0,
  "revisado": false, "notas": "",       // columnas del checklist
  "youtube": { "titulo": "...", "descripcion": "...", "tags": [...] },  // ver "Descripción de YouTube"
  "miniatura": { "pose": "CHEST", "grip": 1 },  // ver "Miniatura de YouTube"
  "music": true, "musicVolume": 0.18,
  "initialPose": "STAND", "initialGrip": 0,
  "poses": { "STAND": { ... }, ... },
  "frames": [ ... ]                     // escenas en orden
}
```

### Descripción de YouTube (`youtube`)

Cada ficha lleva el texto para publicar. `make-exercise` (y `--checklist`) lo exporta a `salida/<slug>.youtube.txt`.
Cambiar `youtube`, `notas` o `revisado` **no** marca el video como desactualizado (no hace falta re-renderizar).

- `titulo` (≤ 100 caracteres, ideal ~60): `<Nombre> 🔥 <beneficio> paso a paso | CrossFit`.
- `tags`: 8–15 búsquedas en español (nombre en inglés y en castellano, zona, "crossfit", momento de uso). Total ≤ 500 caracteres.
- `descripcion` (≤ 5000 caracteres, sin `<` ni `>`), tono **rioplatense, cercano, con emojis, nada formal**. Estructura fija:

```
🔥 <NOMBRE EN MAYÚSCULAS> — <para qué sirve en una línea>

<gancho de 1–2 frases: el problema que resuelve, "este ejercicio es para vos"> 💪

📋 PASO A PASO
1️⃣ ... (posición inicial + mismos pasos que la voz del video, en voseo)

✅ CLAVES DE TÉCNICA
• ... (las claves del video + tecnica_coach del CSV)

🎯 QUÉ TRABAJA
Zona · Zona · Zona

⏱️ CUÁNTO
<dosis> + cuándo usarlo (entrada en calor, WOD, vuelta a la calma)

🙌 Si te sirvió, dejá tu like, guardalo y compartilo con tu compañero de box.

<deslinde: copiar TAL CUAL plantilla/youtube-deslinde.txt>

#CrossFit #<Categoría> #<NombreSinEspacios> #<Zona> #Entrenamiento
```

Si el ejercicio tiene riesgos propios (carga en la espalda, cuelgue, saltos, impacto), sumar una línea específica antes del deslinde ("Si nunca hiciste ..., empezá con ... y con un coach al lado"). Ejemplo completo: `ejercicios/squat-to-stand.json`.

### Miniatura de YouTube (`miniatura`)

`make-exercise` genera `salida/<slug>.miniatura.png` (1080×1920, como el video): la escena **hook** quieta —categoría,
nombre en Bebas, tags— **sin subtítulo ni barra de progreso**, con el personaje agrandado en la pose más reconocible
del ejercicio (no la de pie). Se arma en `videos/<slug>/miniatura/` con `buildIndex(dir, { thumb: true })`.

- `pose`: nombre de una pose de la ficha (la que mejor "cuenta" el ejercicio: el fondo de la sentadilla, la barra arriba, etc.).
- `grip`: 0/1 (manos en el agarre o no). Opcionales: `zoom` (default 1.3) y `dy` (default 230 px hacia abajo) si el personaje
  se corta o queda chico. Revisar siempre la imagen: que no tape los tags y que se lea a tamaño chico.
- Cambiar `miniatura` no marca el video como desactualizado.

### Escenas (`frames[]`)

| Campo | Uso |
|---|---|
| `kind` | `"hook"` (portada con tags), `"step"` (default), `"keys"` (checklist de claves), `"reps"` (repetición con chips) |
| `badge`, `head[]`, `sub` | etiqueta negra, título Bebas (una línea por item, máx. ~14 caracteres) y bajada coral |
| `vo` | texto de la voz en off **y** del subtítulo |
| `min` | duración mínima (s). La real = máx(min, voz + 1 s, última acción + 0,45 s) |
| `numeral` | número gigante decorativo ("1".."4") |
| `stance: true` | tarjeta "vista de arriba" con los pies (`stanceLabel` cambia el texto) |
| `topview` | tarjeta "vista de arriba" acostado boca arriba, brazos en T, piernas que giran al costado: `{ "angle": -62, "at", "dur", "back"?, "label" }` (`back` = vuelve y cae al otro lado). Torsiones en el piso |
| `keys` | lista de claves (strings, o `{ "text", "at" }`) |
| `chips` | `[{ "label": "1 · FLEXIONÁ", "at": 2.6 }]` se iluminan a ese tiempo |
| `moves` | `[{ "to": "POSE", "at": s, "dur": s, "ease"? }]` y `[{ "grip": 0|1, "at", "dur" }]` (tiempos relativos a la escena) |
| `overlays` | marcas de técnica (abajo) |

### Movimientos avanzados (`moves`)

| Forma | Uso |
|---|---|
| `{ "to": "POSE", "at", "dur", "ease"? }` | transición normal (si la pose trae `"g"`, el agarre viaja con ella) |
| `{ "grip": 0/1, "at", "dur" }` | solo el agarre |
| `{ "loop": ["A","B"], "at", "step": 0.36, "until": "end" }` | alterna poses (correr). `until` en s o `"end"` = hasta el final de la escena; o `count` |
| `{ "seq": [["A",0.35],["B",0.2]], "at", "until": "end" }` | ciclo con tiempos propios (palada de remo: tirón rápido, vuelta lenta) |
| `{ "cut": "POSE", "at" }` | esconde al personaje ~0,45 s y aparece en otra posición (cambiar de estiramiento, del piso a de pie) |

### Opciones de la ficha (encuadre y escena)

- `"rig": { "x", "y", "scale" }` — mueve/achica al personaje (default 470, 1500, 0.9). Piso: `y + 34·scale ≈ 1532`.
  En el piso: `{ "x": 520, "y": 1504, "scale": 0.82 }`; remo: `{ "x": 720, "y": 1504, "scale": 0.78 }`.
- `"shadow": false` — oculta la sombra elíptica (cuando hay máquina).
- `"floorScroll": 260` — rayas bajo el piso que se desplazan (px/s): sensación de avance al correr/caminar en el lugar.
- `"props": [...]` — implementos dibujados (ver abajo).
- En una escena `kind: "keys"` el personaje se achica a 0,8 (la lista llega hasta y≈930). `"shrink": 1` lo desactiva.
- Texto/labels: nunca con y > 1580 (el subtítulo arranca en 1600).

### Implementos (`props`)

Se dibujan en `runtime.js` (bloque PROPS) en coordenadas del rig; las partes móviles siguen articulaciones en cada frame.

| type | parámetros | qué sigue a qué |
|---|---|---|
| `rower` | `foot [x,y]`, `fly [x,y]`, `seatY`, `railY`, `railFrom` | asiento → cadera; cadena y manija → manos |
| `kettlebell` | `off [dx,dy]` | manija en la mano cercana (+off), la pesa cuelga; se dibuja debajo del brazo cercano |
| `barbell` | `r` (radio del disco), `off` o `torso [fx, dy]` | disco de costado en la mano (+off) o, con `torso`, fijo al tronco (fx adelante, dy hacia abajo desde el hombro: barra en la espalda `[-34, 18]`); disco cercano encima del cuerpo |
| `wallball` | `off`, `r`, `wallX`, `target` | balón en las manos (+off); con `bf: 1` en la pose queda libre en `bx, by` (lanzado). Pared en `x = wallX` y marca en `y = target` (px del rig) |

Para agregar uno nuevo (barra, kettlebell, cajón…): sumar un `if (pr.type === "...")` en PROPS con las piezas fijas en
`propBack` y un `propUpdates.push((n, f) => …)` para lo que se mueve (n = articulaciones del lado cercano, f = lejano).
Documentarlo en esta tabla y en `BITACORA.md`.

### Overlays

Puntos: `{ "j": "POSE.J", "dx", "dy" }` (articulación de una pose: `A` tobillo, `K` rodilla, `H` cadera, `S` hombro, `N` cuello, `E` codo, `W` mano) o `[x, y]` en px del lienzo 1080×1920 (piso en y≈1535).

- `line` — `from`, `to`, `color: "ink"|coral`, `width`, `solid`
- `arrow` — `from`, `to`, `bend: [dx, dy]`, `dur` (se dibuja)
- `ring` — `pos`, `r`
- `bar` — `pos`, `w`, `h` (ej. marcador de talones)
- `label` — `pos`, `text`, `anchor: "start"|"end"|"middle"`

Todos llevan `at` (aparece) y opcional `out` (desaparece; default fin de escena).

### Poses — el personaje

Vista lateral mirando a la derecha. Ángulos en grados:

- `s` tibia, `t` muslo, `b` torso, `hd` cabeza: desde la **vertical hacia arriba**, `+` = inclinado hacia adelante (derecha).
- `ua` brazo, `fa` codo: desde la **vertical hacia abajo**, `+` = hacia adelante. `ua: 180` = brazo arriba.
- `s2 t2 ua2 fa2`: pierna/brazo del lado lejano (default = igual al cercano) → estocadas, carrera, etc.
- `lr`: las dos piernas caen al costado (grados, 0–90): escorzo de cadera→rodilla→tobillo (torsión acostado). `al`: largo del brazo libre (1 = normal, ~0,15 = brazo que apunta a la cámara, ej. brazos en T acostado).
- `ft ft2`: rotación de los pies. `rx ry`: desplaza todo el cuerpo (px del rig; el tobillo cercano está en 0,0, el piso en y=+34).
- Con `grip` = 1 las manos van al punto `hx, hy` (default la punta del pie: 70, -20). `"g": 0|1` dentro de la pose = agarre propio de esa pose.
- `hb: 1` — el punto de agarre `hx, hy` se mide desde el hombro en el marco del torso (hx adelante, hy hacia abajo por el torso): el agarre acompaña al tronco.
- Sostener un implemento contra el cuerpo (goblet, barra en la espalda, balón al pecho): mejor brazos libres `g 0` con ángulos relativos al torso:
  goblet `ua = -b + 12, fa = 142`; barra atrás `ua = -b - 12, fa = 178`; balón `ua = -b + 18, fa = 136` (ver `kettlebell-good-morning-to-squat`, `barbell-back-squat`, `wall-ball-shot`).
- `ed`: hacia dónde se dobla el codo cuando hay agarre (`1` adelante, `-1` atrás: remo, tirones, dominadas).
- **`hip: [x, y]`** — ubica la cadera ahí y calcula `rx/ry` (posiciones en el piso: el tobillo ya no manda).
- **`hip` + `ankle: [x, y]`** — pie fijo y cadera ubicada: calcula `s/t` solo (IK, rodilla arriba/adelante; `"knee": "back"` la invierte).
  Ideal para remo, sentadillas con pies fijos, estocadas con el pie de adelante quieto.

Poses de referencia (Squat to Stand, probadas):

| Pose | s | t | b | hd | brazos |
|---|---|---|---|---|---|
| De pie | 0 | 0 | 0 | 0 | ua 6, fa 6 |
| Bisagra piernas rectas | -5 | -5 | 128 | 150 | agarre a los pies |
| Cuclilla profunda | 38 | -112 | 48 | 62 | agarre |
| Cuclilla pecho arriba | 40 | -118 | 20 | 4 | agarre |

Poses probadas en el piso / máquina (copiar de la ficha indicada):

| Pose | Ficha | Claves |
|---|---|---|
| Correr (2 fases) | `running` | `hip [0,-415]`, piernas alternadas `s 12/t -62` y `s 52/t 28`, brazos `ua ±40` |
| Cuadrupedia | `pigeon-pose` `QUAD` | `hip [0,-231]`, `s 90, t 0` (tibia en el piso), `ft 172`, `b 72`, manos `g 1, hy 15` |
| Paloma / plegada | `pigeon-pose` | `hip [0,-120]`, `t -57 / t2 57`; plegada `b 82` con antebrazos `ua 25, fa 65` |
| Sentado piernas estiradas | `general-stretching` `SEATED` | `hip [-230,0]`, `s -90, t -90`, `ft -90` (punta arriba) |
| Rodilla al piso (flexor) | `general-stretching` `HALF_KNEEL` | `ankle [200,0] + hip [0,-230]`, pierna de atrás `s2 90, t2 5…24` |
| Postura del niño | `general-stretching` `CHILD` | `hip [-200,-110]`, `s 90, t -60`, `b 86`, brazos al piso |
| Boca arriba rodillas flexionadas / torsión | `supine-spinal-twist` | `hip [0,-20] + ankle [300,0]`, `b -90, hd -92`, brazos `ua 0, al 0.14`; torsión `lr 82`; rig `{520,1500,0.95}` |
| Media rodilla + brazo arriba | `half-kneeling-hip-flexor-stretch` `PUSH_ARM` | `g 0`, brazo lejano `ua2 172` |
| De rodillas / sentado en talones | `child-s-pose` | alto `hip [-200,-250], t 0`; talones `hip [-200,-72], t -70` |
| Remo (4 fases) | `rowing` | `ankle [0,-40]` + `hip [x,-190]`, `ed -1`, manos a la manija `hx/hy` |

Puntos de partida para otras (ajustar con snapshots): sentadilla paralela `s 30, t -75, b 35, hd 25`; brazos arriba `ua 175, fa 0`; brazos al frente `ua 90, fa 0`; estocada `s 25, t -60, s2 -60, t2 -10, b 0` con `rx` para centrar; plancha `s 78, t 78, b 78, hd 85, rx -300`, manos al piso con `grip 1, hx ≈ 430, hy 15`.

### Límites actuales

- Un solo personaje, vista lateral. Implementos: `rower`, `kettlebell`, `barbell`, `wallball`; el resto (mancuernas, cajón, barra de dominadas…) hay que agregarlo en PROPS de `plantilla/runtime.js`.
- Voz: ver sección **Voz** abajo.

## Voz

Desde 2026-10-12 la voz en off es **Piper** (local, gratis) con **Daniela, es_AR** (`plantilla/piper-tts.py`, llamado por `make-exercise`).
- Instalar en una PC nueva: `python -m pip install piper-tts` y bajar el modelo (no está en git, 114 MB):
  `https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_AR/daniela/high/es_AR-daniela-high.onnx` (+ `.onnx.json`) a `plantilla/voces-piper/`.
- Licencia CC BY-SA 4.0: el crédito ("🎙️ Voz: Daniela…") se agrega solo al exportar `salida/<slug>.youtube.txt`.
- `voiceSpeed` > 1 acelera. Por escena, `"voSpeed": 0.88` cambia solo la velocidad de esa línea.
- Nombres en inglés que Daniela lee mal: `"pronuncia": { "Burpee Broad Jump": "Burpii, brod champ", "burpee": "burpii" }`
  en la ficha. Reemplaza solo en el texto que se sintetiza; el subtítulo sigue mostrando el nombre real. Probar variantes
  antes con `python plantilla/piper-tts.py` en `videos/_pruebas-voz/<slug>/` (carpeta ignorada por git). Kokoro sigue disponible con `"voiceProvider": "kokoro"`.
- Edge TTS (voces es-AR Tomás/Elena) quedó descartado: Microsoft devuelve 403 desde oct-2026.
- `index.html` se regenera siempre: los cambios van en la ficha, no en el HTML.
