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

## Pendientes / ideas

- Implementos a dibujar antes de los próximos de la lista: barra olímpica, mancuernas, kettlebell, cajón, wall ball,
  barra de dominadas, bandas (ver columna Implemento del CHECKLIST). Assault bike y SkiErg vienen pronto en la lista.
- Vista de frente no existe: elegir siempre la vista lateral que mejor muestre el movimiento (rotaciones y aperturas
  laterales —ej. estiramientos de tríceps, muñeca— se leen mal de costado: resolverlo con overlays y texto).
- Ejercicios con un brazo agarrando y el otro libre (estiramiento de cuádriceps de pie): falta `g2` (agarre independiente del lado lejano).
- Personajes en el piso se ven chicos (mucho espacio vacío arriba): se podría subir `scale` a ~0.95 con `x` centrado.
