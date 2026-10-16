# Bitácora de producción

Problemas encontrados al generar videos, cómo se resolvieron y qué conviene hacer la próxima vez.
**Leer antes de arrancar un ejercicio nuevo y sumar una entrada cada vez que algo falle o se mejore.**

## Flujo que funciona (2026-10-11, después de 5 videos)

1. `node plantilla/make-exercise.mjs <slug> --info` → datos del CSV.
2. Escribir `ejercicios/<slug>.json` **solo con `poses`** (frames vacío) y correr `node plantilla/pose-lab.mjs <slug>`.
   Iterar las poses mirando `videos/_poselab/snapshots/contact-sheet.jpg` (2–3 vueltas suelen alcanzar).
3. Recién ahí escribir `frames`, `youtube` y `miniatura`. Conviene armarlos con un script Python que lea el deslinde
   de `plantilla/youtube-deslinde.txt` (así no hay que escapar saltos de línea a mano). Ojo: en Git Bash de Windows
   dos heredocs seguidos en un mismo comando pueden romperse → un heredoc por comando, o escribir el script a un archivo.
4. `make-exercise <slug>` → mirar `videos/<slug>/snapshots/contact-sheet.jpg`: casi siempre hay 1–2 labels que pisan
   el cuerpo o el subtítulo. Corregir y `--render` en segundo plano (~1,5 min por video).
5. Mientras renderiza, avanzar con las poses del siguiente ejercicio (el pose-lab usa otra carpeta: `videos/_poselab`).

## Problemas y soluciones

| Fecha | Ejercicio | Problema | Solución / regla |
|---|---|---|---|
| 10-11 | squat-to-stand | `at` en overlays era tiempo y posición a la vez | posición = `pos`, tiempo = `at` |
| 10-11 | squat-to-stand | El estado inicial no tenía agarre `g` | el builder arma `initialState` con `g` (también desde `pose.g`) |
| 10-11 | squat-to-stand | Kokoro: la transcripción por palabra no funciona (0 words) | tiempos de las claves por `at` o `1.0 + i·1.3` s |
| 10-11 | (todos) | Cambiar la descripción de YouTube marcaba el video como desactualizado | la huella (`contentHash`) ignora `youtube`, `miniatura`, `notas`, `revisado` |
| 10-11 | (CSV) | El CSV desapareció de `ejercicios/` (el profe lo movió a su app) | trabajar sobre una copia en `ejercicios/`; cambios en `completados.csv` |
| 10-11 | running | El rig nace del tobillo cercano: al levantar ese pie se movía todo el cuerpo | pose con `hip: [x,y]` → el builder calcula `rx/ry` |
| 10-11 | running | Correr = decenas de moves a mano y la duración de la escena depende de la voz | `{ "loop": [...], "until": "end" }` se expande **después** de medir la voz |
| 10-11 | running | Corriendo en el lugar no parece que avance | `"floorScroll": 260` (rayas bajo el piso) |
| 10-11 | (de pie) | En la escena de claves la lista tapa la cabeza de un personaje parado | el runtime achica al personaje a 0,8 en `kind: "keys"` (`shrink`) |
| 10-11 | running/rowing | Labels entre el piso (y 1532) y el subtítulo (y 1600) pisan el subtítulo | no poner texto con y > 1580; usar y≈1500 o arriba del cuerpo |
| 10-11 | pigeon-pose | Posiciones en el piso salen del cuadro por la izquierda | `"rig": { "x": 520, "y": 1504, "scale": 0.82 }` |
| 10-11 | pigeon-pose | Con agarre IK los antebrazos no se apoyan en el piso | sin agarre: `g 0` con `ua`/`fa` a mano (`ua 25, fa 65`) |
| 10-11 | rowing | El IK siempre doblaba el codo hacia adelante | clave `ed: -1` (codo atrás) |
| 10-11 | rowing | Pie fijo en la plataforma + cadera en el asiento = calcular ángulos a mano | pose `ankle` + `hip` → IK de pierna en el builder |
| 10-11 | rowing | Primer implemento | prop `rower` en runtime.js (asiento sigue a la cadera, cadena/manija a las manos) |
| 10-11 | general-stretching | "Serie libre de estiramientos" no es un movimiento | circuito de 4 estiramientos, uno por zona del CSV, con `cut` entre posiciones |
| 10-11 | general-stretching | Flexión sentado / postura del niño: brazos muy doblados o cabeza en el piso | target de manos casi a largo de brazo (≈300 px del hombro) → brazos casi rectos |
| 10-11 | (labels) | Labels pegados a una articulación suelen caer sobre la cabeza/torso | offset grande hacia arriba (`dy -250…-330`) o posición absoluta a un costado |
| 10-12 | supine-spinal-twist | Torsión acostado: de costado las rodillas "al costado" van hacia la cámara | clave `lr` (escorzo de piernas por cos) + tarjeta `topview` animada con la vista de arriba |
| 10-12 | supine-spinal-twist | Brazos en T acostado apuntan a la cámara (de costado no se ven) | clave `al` (largo del brazo ~0,14) + label "BRAZOS EN T" |
| 10-12 | supine-spinal-twist | Miniatura con zoom 1,3 corta la cabeza de un personaje acostado | `miniatura.zoom: 1.0` en posiciones horizontales |
| 10-12 | child-s-pose | Sentado en talones con `t -84` dejaba las piernas flotando | la rodilla debe quedar en y≈+10: `hip [-200,-72], t -70` |
| 10-12 | child-s-pose | Voz de claves de 4 líneas desborda el subtítulo | máx. ~3 líneas (~130 caracteres) por `vo` |
| 10-12 | half-kneeling | Label en [60,1440] pisaba la pierna de atrás arrodillada | en media rodilla usar y≈1330 y texto corto |
| 10-12 | (voz) | Kokoro sonaba robótico; Edge TTS (es-AR) da 403 aunque se actualice | Piper + Daniela es_AR (local, CC BY-SA → crédito automático en la descripción). El profe la aprobó |
| 10-13 | (todos) | `npx hyperframes` tardaba ~5 min en arrancar (consulta el registro de npm cada vez) | `npx --prefer-offline hyperframes` en make-exercise y pose-lab (3 s) |
| 10-13 | (todos) | hyperframes 0.8 guarda los snapshots en `.hyperframes/artifacts/snapshots/<id>/`: no salían contact sheet ni miniatura | `collectShots(dir)` (build-index) copia la última tanda a `<dir>/snapshots/` |
| 10-13 | cobra-pose | Boca abajo: con `hd 100` la cabeza atraviesa el piso | prono `hip [-30,-8]`, `s/t 90`, `ft 175`, `b 92`, `hd 72`; cobra `b 46, hd 22`, manos bajo hombros `g 1, ed -1` |
| 10-13 | overhead-triceps | El brazo cercano doblado detrás de la cabeza tapa la cara (se dibuja encima) | el brazo que se estira es el **lejano** (`ua2 172, fa2 158`); el cercano guía el codo (`ua 125, fa 117`) |
| 10-13 | seated-quad-stretch | `hip + ankle` con el pie junto a la cadera pone la rodilla arriba, no adelante | pierna en "héroe" con ángulos: `hip [-100,-30], s 86, t -84, ft 178`; de sentado a héroe con `cut` |
| 10-13 | seated-forward-fold | Manos con target cerca del hombro → brazos doblados raros | target de manos lejos, más allá de los pies (`hx 360`), así el IK los deja rectos |
| 10-13 | standing-biceps | Overlay con `{ "j": "POSE.W" }` en una pose sin agarre cae en otro lado (el overlay calcula las manos con `g 1`) | con brazos libres (`g 0`), poner la posición absoluta `[x, y]` |
| 10-14 | kb-good-morning / back-squat / wall-ball | Primeros implementos sostenidos (kettlebell, barra, balón) | props `kettlebell`, `barbell` (disco de costado, gris, encima del cuerpo como en la imagen de referencia), `wallball` (pared + marca; balón libre con `bf/bx/by`) |
| 10-14 | kb-good-morning | Con agarre IK (`g 1`) el codo del goblet subía hacia adelante | brazos libres relativos al torso: `ua = -b + 12, fa = 142` (el agarre sigue al tronco en la bisagra) |
| 10-14 | barbell-back-squat | Con IK la mano asomaba por detrás del disco y el codo quedaba arriba en el fondo | barra fija al torso (`torso [-34, 18]`) y brazos libres `ua = -b - 12, fa = 178` (mano escondida detrás del disco) |
| 10-14 | (overlays) | `{ "j": "POSE.W/E" }` con brazos libres cae en otro lado (el overlay calcula manos con `g 1`) | ring/label de codos o pesa con posición absoluta (calcular con los ángulos) |
| 10-14 | burpee-broad-jump | Burpee + salto: el cuerpo ocupa ~1400 px de rig de punta a punta y se salía del cuadro | rig `{580, 1511, 0.62}`, plancha en `hip [-290,-240]`, aterrizaje en `hip [290,-330]`; entre reps `cut` a STAND (si no, "camina para atrás") |
| 10-14 | burpee-broad-jump | Pecho al piso con agarre: los brazos atravesaban el piso | brazos libres `ua -120, fa 168` (codos arriba, manos al lado del pecho) |
| 10-14 | (todos) | 4 `make-exercise` en paralelo con una versión nueva de hyperframes → `npm ECOMPROMISED` (lock de npx) | correr uno solo primero (descarga la versión), después los demás en paralelo |
| 10-14 | wall-ball-shot | La pared (prop) cruzaba la lista de la escena de claves | las piezas de escenografía llevan `class="prop-scenery"` y el runtime las desvanece en `kind: "keys"` |
| 10-14 | burpee-broad-jump | Daniela no pronuncia claro "Burpee Broad Jump" | `pronuncia` (reemplazo solo para la voz) + `voSpeed: 0.88` en la portada; el profe eligió "Burpii, brod champ" entre 13 pruebas |
| 10-15 | (todos) | El pose-lab usaba una sola carpeta: no se podían probar poses de varios ejercicios a la vez | `videos/_poselab/<slug>/`: correr uno solo primero y después el resto en paralelo |
| 10-15 | assault-bike | Pedalear = las dos piernas con pies en pedales opuestos y las dos manos en manijas que van y vienen | prop `airbike` + `ankle2` (IK pierna lejana) + `g2/hx2/hy2` (mano lejana propia); 6 poses generadas por script (cada 60° de biela), `seq` con `ease: "none"` |
| 10-15 | wrist-extensor | El personaje no tenía muñeca | `"fingers": true` + `wr/wr2`; el brazo que se estira es el **lejano** y la mano cercana empuja (`g 1, hb 1`, `g2 0`) para que se vea encima |
| 10-15 | 90-90-hip-rotation | De costado, la pierna de adelante en 90/90 se veía estirada | pre-escorzo con el tobillo casi debajo de la rodilla (`ankle [110,95]`) + `lr 80`; el cambio de lado se cuenta con la tarjeta `topview mode 9090` |
| 10-15 | barbell-deadlift | Arranque con cadera baja parecía sentadilla y los brazos no llegaban a la barra (disco r 96 → barra a y −62) | `hip [-150,-285] + ankle [0,0]`, `b 72`: hombros apenas delante de la barra a ≤ 330 px |
| 10-15 | barbell-front-squat | Rack frontal | barra `torso [60, 30]` (r 72, no tapa la cara), brazos `ua = 90 − b`, `fa 176` → codos altos adelante |
| 10-15 | hanging-toes-to-bar | Colgado: con piernas a la barra el hombro quedaba lejos de la barra | geometría resuelta (hombro a ≤ 330 de la barra, puntas en la barra, pike ~45°) con la intersección de círculos en el script; claves con `shrink: 0.62` |

## Pendientes / ideas

- Implementos a dibujar antes de los próximos de la lista: mancuernas, cajón, bandas, SkiErg, trineo
  (ya están: remo, kettlebell, barra, wall ball, assault bike y barra de dominadas, 10-15) (ver columna Implemento del CHECKLIST).
- Vista de frente no existe: elegir siempre la vista lateral que mejor muestre el movimiento (rotaciones y aperturas
  laterales —ej. estiramientos de tríceps, muñeca— se leen mal de costado: resolverlo con overlays y texto).
- ~~Agarre independiente del lado lejano~~: hecho con `g2` (10-15).
- Personajes en el piso se ven chicos (mucho espacio vacío arriba): se podría subir `scale` a ~0.95 con `x` centrado.
