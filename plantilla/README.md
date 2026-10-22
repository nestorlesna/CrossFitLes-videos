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

## Máquinas de gimnasio (`ejercicios/maquinas.csv`)

Segunda lista, para videos de máquinas (no CrossFit), armada desde `maquinas_gimnasio.xlsx` (planilla del usuario, no
se edita): una fila por video (las máquinas multiuso se parten en un video por ejercicio), mismo formato `;` + BOM.
Columnas: `clave, lote, nombre` (inglés)`, nombre_es, otros_nombres, maquina_excel, fila_excel, tipo, zona,
musculos_principales, musculos_secundarios, como_se_usa, que_no_hacer, tips_profe, nivel, nivel_texto, dosis, prop, vista`.

- El CHECKLIST las muestra en la sección **🏋️ Máquinas de gimnasio** (al final), numeradas `M1, M2…`; la columna
  Implemento dice 🏋️ + la máquina + el prop de `runtime.js`, con «(falta dibujar)» si `runtime.js` no tiene
  `pr.type === "<prop>"`.
- La ficha lleva `"maquina": true` (el BRIEF/STORYBOARD dicen "alumnos de gimnasio"). `--info` busca en las dos listas.
- Procedimiento, estructura de 14–18 escenas (90–150 s), escenas ASÍ NO, tips del profe y YouTube:
  **`GENERAR_VIDEOS_MAQUINAS.md`**.

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
| `node plantilla/pose-lab.mjs <slug> [A,B]` | dibuja todas (o algunas) poses de la ficha en `videos/_poselab/<slug>/snapshots/contact-sheet.jpg` (se pueden correr varios a la vez) — **usarlo antes de escribir las escenas** |
| `node plantilla/make-exercise.mjs <slug> --info` | muestra la fila del CSV de ese ejercicio |
| `npx hyperframes preview` (dentro de `videos/<slug>`) | revisar en el Studio |

Flags: `--force-tts`, `--no-check`, `--no-snapshot`, `--prefijo=OC` (con `--render`: el video sale como `salida/OC_<slug>.mp4`; el nombre queda en `.pipeline.json` → `archivo` y el CHECKLIST lo encuentra).

Para generar varios videos con otra herramienta o modelo: seguir **`GENERAR_VIDEOS.md`** (raíz del proyecto).

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
  "maquina": true,                      // solo videos de máquinas de gimnasio (lista ejercicios/maquinas.csv)
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
| `topview` con `"mode": "twist"` | tarjeta "vista de arriba" sentado: hombros, brazos y balón giran de lado a lado (`angle`, `dur` por ida, `at`); russian twist |
| `topview` con `"mode": "lean"` / `"rot"` | "vista de frente": el tronco con el brazo arriba se inclina hacia una pared (lat stretch); "vista de arriba": el cuerpo gira alrededor de la mano apoyada en la pared (hombro). `angle`, `at`, `dur`, `back` |
| `topview` con `"mode": "front"` | tarjeta "vista de frente" cuyos brazos siguen solos la pose de perfil (altura de codo y mano de la vista lateral, el resto del largo hacia afuera). `plates: true` agrega discos en las manos. Para ejercicios de hombro (ver `cuban-press`) |
| `topview` con `"mode": "fly"` | "vista de arriba" de aperturas: los brazos van del costado (abiertos) al frente (juntos) según la clave `al` de la pose (ángulo = acos(al)). `cable: true` dibuja los cables a las poleas. Ver `cable-crossover`, `pec-deck-fly` |
| `topview` con `"mode": "abd"` | "vista de arriba" sentado: los muslos se abren según la clave `cs` (0 juntas, 1 ≈ 43°); `pads: "out"` almohadillas afuera (abductores) / `"in"` adentro (aductores). Ver `hip-abduction-machine` |
| `topview` con `"mode": "er"` | "vista de arriba" de la rotación externa: el antebrazo gira hacia afuera según la clave `fl` y la banda se estira hasta el ancla. Solo `label` |
| `topview` con `"mode": "cossack"` | "vista de frente" con los pies abiertos: la cadera baja hacia un lado según la clave `cs` de la pose (1 / −1) y la otra pierna queda estirada. Movimientos laterales (ver `cossack-squat`). Solo `label` |
| `scroll` | velocidad del piso que se desplaza en esa escena (px/s; negativa = camina para atrás, 0 = quieto). Pisa a `floorScroll` |
| `topview` con `"mode": "bar"` | tarjeta "vista de arriba" con la barra y el atleta al costado; `at` = salta al otro lado, `at: null` = quieta (burpee lateral) |
| `topview` con `"mode": "9090"` | tarjeta "vista de arriba" sentado en 90/90; `at` = momento en que las piernas cambian de lado (espejo), `from: -1` arranca espejado, `at: null` = quieta |
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
| `legpress` 🏋️ | `hip [x,y]`, `ang` (35), `lean` (-45), `stops`, `handle [x,y]`, `gap` | prensa 45°: asiento + respaldo reclinado + manijas/trabas fijos; riel a `ang` grados que pasa por `hip`; el carro (plataforma + discos) sigue al tobillo cercano proyectado sobre el riel. Poses: `hip` fijo + `ankle` sobre la línea del riel, `ft -128` (suela contra la plataforma). Ver `leg-press` |
| `latpulldown` 🏋️ | `x` (columna), `pulley [x,y]`, `seat`, `pad [x,y]`, `pin`, `rest` | jalón al pecho: columna con pila de peso, viga y polea arriba, asiento y rodillo de muslos; barra de punta en las manos y cable a la polea. La pila sube lo que se alarga el cable respecto de la primera pose dibujada (`initialPose` = pila apoyada; `rest` lo fija a mano). Ver `lat-pulldown` |

| `legextension` / `seatedlegcurl` 🏋️ | `pivot [x,y]` (eje = rodilla), `seat [x0,x1,y]`, `back [x,lean,len]`, `stack`, `handle [x,y]`, `roll`, `thigh [x,y]` (curl), `pin`, `k` | sillón de cuádriceps / femoral sentado: pila atrás, asiento + respaldo regulable, palanca con rodillo que sigue a la tibia (adelante de la tibia en el sillón, atrás del tobillo en el curl). Curl: traba de muslos; **`bf 1` en la pose = traba abierta** (error "sin trabar"). Ver `leg-extension`, `seated-leg-curl` |
| `lyinglegcurl` 🏋️ | `pivot`, `top`, `x0`, `x1`, `stack`, `handle`, `roll` | camilla boca abajo (cabeza a la derecha), rodillo atrás del tobillo. Prono: `t 90, b 92, hd 74`, tibia `s 92 → 200`, `ft = s`. Ver `lying-leg-curl` |
| `hacksquat` 🏋️ | `hip`, `lean`, `foot`, `plat`, `len`, `rail [d0,d1]`, `stops`, `hand [d,k]` | rieles paralelos al tronco (`b = lean` en todas las poses); el carro (respaldo, hombrera, manijas, discos) sigue a la cadera proyectada sobre el riel. Cadera sobre la línea del riel (`hipat()` en el generador) y brazos libres `ua = b + 52, fa 118`. Ver `hack-squat` |
| `pendulum` 🏋️ | `hip`, `pivot`, `lean`, `foot`, `plat`, `len`, `hand` | el carro cuelga de un brazo que gira en `pivot`: la cadera hace un arco y `b = lean + giro`. Ver `pendulum-squat` |
| `cable` / `cablerow` 🏋️ | `x` (pila), `top`, `pulley [x,y]`, `track`, `att` (`bar`/`rope`/`handle`), `pin`, `ratio`; cablerow + `seat`, `foot`, `ang` | columna de polea regulable; cable de la polea a las manos y accesorio en las manos. La pila sube lo que se alarga el cable. Pushdown/curl/face pull con brazos libres (`ua`/`fa`, face pull con `ul 0.28`). Ver `cable-triceps-pushdown`, `cable-bicep-curl`, `cable-face-pull`, `seated-cable-row` |
| `cablecrossover` 🏋️ | `x`, `top`, `pulley`, `pin` | dos columnas (de perfil, detrás del atleta); un cable y una manija por mano. Brazos libres con `al` (0,32 abiertos → 1 juntos) + tarjeta `topview mode fly`. Ver `cable-crossover` |
| `chestpress` / `shoulderpress` / `pecdeck` / `lateralraise` / `preachercurl` 🏋️ | `pivot`, `frameTop`, `stack`, `seat`, `back` (sin `back` = sin respaldo), `pad` (preacher), `chest` (lateral), `pin`, `k`, `rest` | tren superior sentado: palanca del eje a la mano (pecdeck en L; lateralraise = almohadilla sobre el brazo con eje en el hombro). La pila sube k × lo que se mueve la mano. Ver las fichas del lote 3 |
| `hipthrust` 🏋️ | `back [x,y]`, `pivot`, `stack`, `seat`, `pin`, `k` | respaldo bajo para los omóplatos (hombro fijo: la cadera gira alrededor de él), almohadilla sobre la cadera colgada de una palanca. Ver `hip-thrust-machine` |
| `hipabduction` / `hipadduction` 🏋️ | `seat`, `back`, `stack`, `rest [x,y]` (pie), `pin`, `k`, `open` | sentado reclinado con almohadilla en la rodilla (afuera / adentro). **De perfil no se ve abrir**: la clave **`cs`** (0 juntas, 1 abiertas) mueve la pila y la tarjeta `topview mode abd`. Ver `hip-abduction-machine`, `hip-adduction-machine` |
| `standingcalf` / `seatedcalf` 🏋️ | `step [x0,x1,y]`, `stack`, `column` + `padX` (de pie), `seat` + `pivot` (sentado), `pin`, `k` | escalón bajo la punta del pie; hombreras (de pie) o almohadilla de rodillas (sentado) que siguen al cuerpo. Poses con la punta fija en el borde: `onstep()` del generador calcula el tobillo para cada `ft`. Ver las fichas de gemelos |
| `smith` 🏋️ | `x` (riel), `top`, `gap`, `stops`, `track` (`back`/`hands`), `torso`, `r` | multipower: la barra (de punta, con disco) sube y baja en x fija; `back` = punto del tronco (como `barbell.torso`), `hands` = mano. Sentadilla: la cadera se ubica para que el punto de la barra quede en x = riel. Banca: con `bench`. Ver `smith-machine-squat`, `smith-machine-bench-press` |
| `assisted` 🏋️ | `stack`, `grip [x,y]`, `dip [x,y]`, `pivot`, `rest`, `pin`, `k` | dominadas / fondos asistidos: plataforma de rodillas que sigue a la rodilla; la pila (contrapeso) sube cuando el cuerpo baja (`rest` = altura de la rodilla arriba). Arrodillado: `s 92, t 4, ft 80`. Ver `assisted-pull-up-machine`, `assisted-dip-machine` |
| `abcrunch` 🏋️ | `seat`, `pivot`, `stack`, `feet`, `pin`, `k` | crunch en máquina: almohadilla/manija que sigue al hombro, rodillo sobre el empeine. Ver `ab-crunch-machine` |
| `backext45` 🏋️ | `foot`, `pad`, `roll`, `ang` | banco romano 45° (fijo): piernas a `ang`° con `ft = ang`, almohadilla bajo la cadera, rodillo detrás de las pantorrillas. Ver `back-extension-45` |
| `treadmill` 🏋️ | `deck [x0,x1,y]`, `console`, `rail`, `clip` | cinta: con `floorScroll`/`scroll` las rayas se mueven **sobre la cinta**; poses de `running` subidas 74 px; `clip: true` = cuerda roja del clip de seguridad a la cadera. Ver `treadmill` |
| `stationarybike` 🏋️ | `crank`, `seat`, `bar`, `fly` | bici fija: pedales en la biela (radio 72, poses `bike(θ)` del generador), manos fijas en el manubrio. Ver `stationary-bike` |
| `elliptical` 🏋️ | `fly`, `pivot`, `x0` | elíptico: pedales siguen a cada tobillo (elipse en las poses), manijas largas del `pivot` a cada mano (`g2 1`). Ver `elliptical-trainer` |
| `stairclimber` 🏋️ | `base`, `x`, `rail`, `rise`, `run`, `steps` | escaladora: escalera de fondo fija + un escalón bajo cada pie que sigue al tobillo. Ver `stair-climber` |

**Generador de fichas de máquinas** (`plantilla/maquinas/`): `common.py` (FK igual a `runtime.js` para calcular
articulaciones y ubicar overlays, `check()` de alcance, helpers de escenas, `yt_desc()` y `save()` con validaciones de
`vo` y labels) + un `lN_poses.py` y un `lN_frames.py` por lote. Ver `GENERAR_VIDEOS_MAQUINAS.md` §4.4.

Helper de máquinas en `runtime.js`: **`weightStack(parent, x, y, {n, ph, w, pin, guide, max})`** dibuja la pila de placas
con guías, varilla y pasador (ACCENT) y devuelve `{ top, lift(px) }`: `lift` sube las placas de arriba del pasador y
devuelve cuánto subió. Usarlo en toda máquina con pila (ver `GENERAR_VIDEOS_MAQUINAS.md` §4.2).
| `kettlebell` | `off [dx,dy]` | manija en la mano cercana (+off), la pesa cuelga; se dibuja debajo del brazo cercano |
| `barbell` | `r` (radio del disco), `off` o `torso [fx, dy]` | disco de costado en la mano (+off) o, con `torso`, fijo al tronco (fx adelante, dy hacia abajo desde el hombro: barra en la espalda `[-34, 18]`); disco cercano encima del cuerpo |
| `wallball` | `off`, `r`, `wallX`, `target` | balón en las manos (+off); con `bf: 1` en la pose queda libre en `bx, by` (lanzado). Pared en `x = wallX` y marca en `y = target` (px del rig) |
| `airbike` | `crank`, `fan`, `fanR`, `pivot`, `seat` | cuadro y ventilador fijos; bielas del centro `crank` a cada tobillo (pedal bajo la zapatilla), manijas de `pivot` a cada mano; el ventilador gira con la biela cercana. Poses con `hip` + `ankle` + `ankle2` y `g2` (ver `assault-bike`) |
| `pullupbar` | `bar [x,y]`, `postX` | barra vista de punta en `bar` (encima de las manos) + viga y parante atrás. Colgado: manos `g 1` en la barra, cadera calculada para que el hombro quede a ≤ 330 px (ver `hanging-toes-to-bar`) |
| `kettlebell` + `hand: "far"` | igual que `kettlebell` | segunda pesa en la mano lejana, detrás del cuerpo (farmer carry: dos props, ver `kettlebell-farmer-carry`) |
| `dumbbell` | `off`, `r` | mancuerna vista de punta en la mano que diga la pose: `dh 0` cercana (bajo el brazo cercano), `dh 1` lejana (atrás). Con `bf 1` queda suelta en el piso en `bx, by`. Cambio de mano: las dos manos en la mancuerna (`g 1` + `g2 1`) y recién ahí `dh` (ver `alternating-single-arm-dumbbell-power-snatch`) |
| `dumbbell` + `hand` + `side` | `hand: "near"/"far"`, `side: true` | mancuerna fija en una mano (ignora `dh`) y vista de costado (manija hacia adelante): dos props para una en cada mano (ver `weighted-lunge`) |
| `wallball` + `wall: false` + `depth: true` | | balón medicinal sin pared; con `depth` pasa por delante (`pz 1`) o por detrás (`pz 0`) del cuerpo (ver `russian-twist`) |
| `barbell` + `blend: true` | con `torso` | `bf 1` = barra en el rack (fija al tronco), `bf 0` = en las manos: del rack frontal a arriba de la cabeza (ver `barbell-thruster`) |
| `sled` | `len`, `post` | trineo en `x = bx` de la pose (cerca para empujar, lejos para tirar); `rp 1` muestra la soga del gancho a la mano cercana (ver `sled-push-pull`) |
| `skierg` | `x`, `top` | torre con volante y polea; cuerdas a cada mano y manijas en las manos (ver `skierg`) |
| `box` | `x0`, `x1`, `h` | cajón de madera fijo. Va fuera del rig (escenario fijo): no se espeja con `fx` ni desaparece en los `cut` (ver `box-jump-over`) |
| `kettlebell` + `swing: true` | | la pesa sigue la línea hombro→mano (swing: atrás entre las piernas, al frente, arriba de la cabeza). Ver `kettlebell-swing` |
| `jumprope` | `c [dx,dy]`, `rx`, `ry` | cuerda que gira alrededor de la cadera (+c) en una elipse; fase `rp` (0 = bajo los pies, 0.5 = arriba). Ciclo: `seq [[AIR(rp 0), 0.01], [LAND(rp .5), t], [AIR2(rp 1), t]]` (el salto de 1 a 0 no se ve). Ver `jump-rope` |
| `wall` | `x`, `h` | pared fija (escenario, fuera del rig). Ojo con `h`: si es muy alta cruza la portada y la lista de claves (≈ 880). Ver `wall-shoulder-stretch` |
| `band` | `anchor [x,y]`, `hand` (`near`/`both`), `post [x,h]`, `layer` (`mid`/`back`), `color` | banda elástica del ancla a la(s) mano(s); `post` dibuja el parante (escenario, se atenúa en claves). Ancla alta adelante = pushdown; ancla a la altura de la mano con `layer: "mid"` = rotación externa. Ver `band-triceps-pushdown`, `band-external-rotation` |
| `partner` | `x` | compañero frente a frente: copia espejada del atleta (`<use>`) alrededor de x (rig px); hace el mismo movimiento a la vez. Con `shadow: false`. Ver `partner-wall-ball-sit-up` |
| `wallball` + `mirror: x` | `arc` | balón que se pasan con el `partner`: bf 0 = mis manos, 1 = las del compañero (con arco al cruzar); se dibuja encima de los dos |
| `floorbar` | `x0`, `x1`, `r` | barra en el piso paralela al cuerpo (larga, discos de canto). `pz 0` = detrás del atleta, `pz 1` = delante: el salto lateral por encima se lee con el cambio de profundidad (ver `burpee-over-the-bar`) |

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
- **`g2`** (≥ 0): agarre propio del brazo lejano hacia `hx2, hy2` (codo `ed2`); `-1` (default) = sigue a `g`. Una mano agarra y la otra queda libre, o cada mano en su manija (assault bike).
- **`cv`**: curva de la espalda en px (`+` redondea hacia el techo: gato, protracción escapular; `−` la hunde: vaca). Ver `cat-cow`, `scapular-push-up`.
- **`ul`**: largo del brazo superior (1 normal; ~0,3 = codo abierto al costado, que de perfil apunta a la cámara: upright row, rotación externa). Ver `cuban-press`.
- Ángulos de brazo que se interpolan: pasan por el camino corto entre los dos valores. Acostado con brazos atrás de la cabeza usar `ua 270` (no −90) para que al subir pasen por arriba y no atraviesen el piso (ver `v-up`).
- **`fl`**: largo del antebrazo cercano (1 normal; ~0,26 = rotado ~75° hacia la cámara). Ver `band-external-rotation`.
- **`ll` / `ll2`**: largo dibujado de la pierna cercana / lejana (1 normal). Una pierna estirada hacia el costado (se aleja de la cámara) se ve corta: ubicar la pose con `hip`, la pierna con `s = t` y `ll` = distancia cadera→pie / 470 (ver `cossack-squat`). La cadera sigue saliendo de la cadena completa.
- **`cs`**: corrimiento de peso para la tarjeta `topview mode cossack` (−1 … 1).
- **`fx`**: hacia dónde mira (1 derecha, −1 izquierda). Interpolarlo pasa por 0 = giro sobre la cadera. Con `fx −1` el cuerpo se espeja alrededor de la cadera: escribir la pose "hacia la derecha" con la cadera en su x (ver `shuttle-run`). Los overlays `{ "j": ... }` ignoran `fx` (usar posiciones absolutas) y los props del rig también se espejan (salvo `box`, que es escenario fijo). Para volver por el mismo camino mirando a la izquierda: la misma pose con todas las x corridas −2·(x de la cadera) y `fx −1` (ver `mirror()` en `box-jump-over`).
- **`ankle2`** (con `hip` + `ankle`): IK de la pierna lejana desde la misma cadera (cada pie en su pedal).
- **`wr` / `wr2`** + `"fingers": true` en la ficha: dedos dibujados y ángulo de muñeca (−80 = dedos al piso con el brazo al frente). Ver `wrist-extensor-stretch`.
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

- Un solo personaje, vista lateral. Implementos: `rower`, `kettlebell`, `barbell`, `wallball`, `airbike`, `pullupbar`, `dumbbell`, `floorbar`, `sled`, `skierg`, `box`, `jumprope`, `wall`, `band`, `partner` (discos chicos: `barbell` con `r` 40); el resto (anillas, cuerda de trepar…) hay que agregarlo en PROPS de `plantilla/runtime.js`.
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
- **Nombre en inglés (desde 2026-10-21):** en el `hook`, el nombre lo dice **Kokoro `af_heart`** (inglés, Apache 2.0) y
  sigue Daniela. `make-exercise` manda la línea como `{ en, text }` + `enVoice` y `piper-tts.py` la arma (pausa de
  0,35 s, fundido y volumen igualado). Regla: el `vo` del hook empieza con `name` exacto → Daniela sigue después de
  los dos puntos; si no, el nombre se dice antes del `vo` completo. Ficha: `"nombreEnVoz"` (cómo leer nombres con
  símbolos) y `"nombreEn": false` (nombre en castellano). Requiere `python -m pip install kokoro-onnx` y el modelo
  (`kokoro-v1.0.onnx` + `voices-v1.0.bin`) en `plantilla/voces-kokoro/` o `~/.cache/hyperframes/tts/` (ver GENERAR_VIDEOS §3).
  El crédito de Kokoro se suma a la descripción solo si el render lo usó (`.pipeline.json` → `renderVozEn`).
  Videos viejos: `node plantilla/revoz-en.mjs` re-renderiza por lotes (plan al final de `CHECKLIST.md`).
- Edge TTS (voces es-AR Tomás/Elena) quedó descartado: Microsoft devuelve 403 desde oct-2026.
- `index.html` se regenera siempre: los cambios van en la ficha, no en el HTML.
