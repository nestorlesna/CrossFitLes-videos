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
  "voice": "em_alex",                   // Kokoro español: em_alex, em_santa (hombre), ef_dora (mujer)
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
- `ft ft2`: rotación de los pies. `rx ry`: desplaza todo el cuerpo (px del rig; el tobillo cercano está en 0,0, el piso en y=+34).
- Con `grip` = 1 las manos van al punto `hx, hy` (default la punta del pie: 70, -20). `"g": 0|1` dentro de la pose = agarre propio de esa pose.
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
| Remo (4 fases) | `rowing` | `ankle [0,-40]` + `hip [x,-190]`, `ed -1`, manos a la manija `hx/hy` |

Puntos de partida para otras (ajustar con snapshots): sentadilla paralela `s 30, t -75, b 35, hd 25`; brazos arriba `ua 175, fa 0`; brazos al frente `ua 90, fa 0`; estocada `s 25, t -60, s2 -60, t2 -10, b 0` con `rx` para centrar; plancha `s 78, t 78, b 78, hd 85, rx -300`, manos al piso con `grip 1, hx ≈ 430, hy 15`.

### Límites actuales

- Un solo personaje, vista lateral. Implementos: solo `rower` por ahora; el resto (barra, pesas, cajón…) hay que agregarlo en PROPS de `plantilla/runtime.js`.
- La voz es Kokoro local (algo robótica). Con sesión HeyGen (`npx hyperframes auth login`) se puede pasar a una voz mejor cambiando `provider` en `make-exercise.mjs`.
- `index.html` se regenera siempre: los cambios van en la ficha, no en el HTML.
