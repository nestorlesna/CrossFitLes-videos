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
| 10-15 | (runtime) | `const f2` se usa en PROPS antes de declararse: un prop que lo llama al construirse (no en el update) deja la pantalla sin personaje y sin error visible | en la parte que se arma una sola vez usar `toFixed` directo; si el pose-lab sale vacío, sospechar de un error de JS en runtime.js |
| 10-15 | db-power-snatch | Mancuerna en una mano que alterna, y que arranca en el piso | prop `dumbbell` + clave `dh` (mano) + `bf/bx/by` (suelta en el piso). Cambio de mano con las dos manos en la mancuerna (`g 1`, `g2 1`) y recién ahí `dh` 0→1; poses libres del brazo lejano con `g2 0` (no −1: interpolar 1→−1 salta) |
| 10-15 | db-power-snatch | Tirón con codo alto: el antebrazo tapaba la cara (`ua 122, fa −128`) | `ua 100, fa −106`; arriba `ua 190` (brazo apenas detrás de la cabeza) |
| 10-15 | farmer-carry | Dos pesas, una por mano | dos props `kettlebell`, uno con `hand: "far"`; `off [0,16]` (manija en la mano); caminata `loop` WALK_A/B + `floorScroll 150` |
| 10-15 | burpee-over-the-bar | Salto lateral = en profundidad, de costado no se ve | prop `floorbar` con `pz` (barra detrás/delante; la de adelante un poco más abajo) + tarjeta `topview mode bar`; `pz 0.5` en el punto alto del salto |
| 10-15 | cat-cow / scapular | El torso era una línea recta | torso como curva cuadrática: clave `cv` (gato +40, vaca −30; protracción +34, retracción −22) |
| 10-15 | shuttle-run | Ir y volver: el personaje solo miraba a la derecha | clave `fx` (espejo alrededor de la cadera; 1→−1 = giro). Poses de carrera generadas por script con la cadera avanzando (`ease: none`), líneas como overlays absolutos, `shadow: false` |
| 10-15 | yoga-push-up | Plancha / chaturanga / perro arriba con las manos fijas | geometría por script: hombro sobre la mano a ≤ 330 px, cuerpo recto de 750 px desde el tobillo; rig `x 290` para que entren pies y cabeza |
| 10-15 | sled-push-pull | Empujar de ida y tirar de vuelta: el piso tenía una sola velocidad para todo el video | campo `scroll` por escena (negativo = hacia atrás). Trineo con `bx` en la pose (cerca/lejos) y `rp` para la soga |
| 10-15 | russian-twist | La rotación de tronco no se ve de costado | balón con `depth` (delante/detrás con `pz`) + tarjeta `topview mode twist` |
| 10-15 | thruster | La barra va en el rack (fija al tronco) y después en las manos | `barbell` con `blend: true`: `bf` mezcla entre los dos puntos |
| 10-15 | box-jump-over | Con `fx` el cajón se espejaba y se corría de lugar | escenario fijo (`propStatic`) fuera del rig; la vuelta con poses espejadas (`mirror`: x − 2·cadera, `fx −1`) |
| 10-15 | snatch / high pull | Barra en la cadera con agarre IK: codos doblados raros | brazos libres colgando (`ua 2, fa 0`); tirón alto con codos arriba `ua 95…118, fa −100…−124` |
| 10-15 | (topbar) | Nombre largo + categoría larga se pisan en la barra superior | categoría corta (máx. 2 partes: "CROSSFIT · FUERZA") |
| 10-15 | (bash) | Heredocs largos con comillas/backticks se cortan ("unexpected EOF") | scripts y parches como archivo (Write) y `python archivo.py` |
| 10-16 | kettlebell-swing | La pesa siempre colgaba hacia abajo, aun arriba de la cabeza | `kettlebell` con `swing: true` (rota con la línea del brazo) |
| 10-16 | jump-rope | Cuerda que gira sin "volver para atrás" al interpolar la fase | fase `rp` con salto invisible 1→0 en un paso de 0,01 s dentro del `seq` |
| 10-16 | v-up | De acostado (brazos `ua −90`) a sentado (`ua 125`) los brazos atravesaban el piso | `ua 270` en la pose acostada: la interpolación pasa por arriba |
| 10-16 | cuban-press | Codos abiertos al costado: de perfil el brazo se veía adelante | clave `ul` (brazo superior acortado) |
| 10-16 | wall-lat / wall-shoulder | Inclinación lateral y rotación no se ven de perfil | tarjetas `topview` `lean` (de frente) y `rot` (de arriba, gira alrededor de la mano) + prop `wall` |
| 10-16 | (varios) | El check marcó labels cortados en el borde o pisando el subtítulo, y tarjetas encima de los chips de reps | labels largos con anchor hacia el centro; no usar `topview` en la escena de reps (los chips ocupan ese lugar) |
| 10-16 | cuban-press | El profe pidió ver el movimiento de los hombros de frente | tarjeta `topview mode front`: los brazos se calculan en cada cuadro desde la pose lateral (sirve para cualquier ejercicio de hombros) |
| 10-16 | clean-and-jerk / hang-power-clean | Con disco r 90 la barra en el rack tapaba toda la cara | `barbell` r 74 con `torso [64, 36]`; en el SETUP bajar las manos (hy −40) para que el disco toque el piso |
| 10-16 | clean-and-jerk | Tijera del jerk: el pie de atrás atravesaba el piso al ponerlo en puntas | pie de atrás levantado (`ankle2 y −40`) y `ft2` positivo (horario = punta abajo) |
| 10-16 | (varios) | `pose-lab` con 10 ejercicios en paralelo: uno falló por timeout del navegador | correr de a 5, o repetir el que falló |
| 10-16 | box-step-up | Con el cajón de 300 la pierna de abajo no llegaba al piso al bajar | cajón de 220 para que `ankle`/`ankle2` lleguen (cadera–tobillo ≤ 470) |
| 10-16 | partner-wall-ball-sit-up | Dos personas | prop `partner` (copia espejada con `<use>`) + `wallball` `mirror` (balón fuera del rig para que no se duplique) |
| 10-16 | band-external-rotation | La rotación externa (antebrazo hacia la cámara) no se ve de perfil | clave `fl` (antebrazo acortado) + tarjeta `topview` `er` (vista de arriba con la banda) |
| 10-16 | cossack-squat | Sentadilla lateral: la pierna estirada va hacia el costado y de perfil no se ve | claves `ll`/`ll2` (pierna corta por escorzo, el pie cae bajo la cadera) + tarjeta `topview mode cossack` (vista de frente que sigue a `cs`) |
| 10-16 | arm-circles | Brazos en cruz haciendo círculos | `al 0.34` + `ua` 0/90/180/270 en un `seq` con `ease: none` (adelante = ua decreciente); tarjeta `topview mode front` |
| 10-16 | wall-sit / wall-thoracic | Pared detrás o adelante | prop `wall` (rect de `x` a `x+60`): detrás = `x` = espalda − 60; adelante con manos `g 1` a la pared y el hombro a ≤ 330 px |
| 10-16 | bird-dog-crunch | Brazo libre y el otro apoyado, pasando de cuadrupedia | poner `g2 1, hx2, hy2` también en la pose de cuadrupedia (si no, `g2` va de −1 a 1 y el brazo salta); codo y rodilla se tocan en la intersección de círculos calculada en el script |
| 10-17 | (overlays) | Dos labels en el mismo lugar se veían juntos y el check marcaba `content_overlap ... unreadable` | la clave de fin es `out` (relativo al frame), NO `end`: `build-index.mjs` calcula `end = o.out != null ? f.start + o.out : f.start + f.dur - 0.35` |
| 10-17 | barbell-romanian-deadlift | Bisagra de cadera con la barra colgando de las manos | `hip`+`ankle` (IK de pierna, rodillas casi fijas) y brazos por `ua`/`fa` con `g 0` (absolutos desde abajo: la barra sigue la mano pegada a la pierna); la barra a media tibia sale de hip −220, b 60 |
| 10-17 | (miniatura) | La miniatura por defecto (`dy 230`, `zoom 1.3`) corta al personaje en poses bajas (bisagras, piso) | `spec.miniatura.dy` negativo y `zoom` ≤ 1.2 (ej. bisagra: `zoom 1.2, dy 60`) |
| 10-17 | partner-wall-ball-over-bar | Barra en el piso entre los dos sin que el espejo la duplique corrida | `floorbar` centrada en el eje del espejo (`x0 165, x1 365` con `partner`/`wallball` en `x`/`mirror 265`): la copia espejada de `propFront` cae exactamente encima |
| 10-17 | partner-wall-ball-over-bar | El balón tapaba la cara del atleta | `wallball.off` (34, 30) baja el balón al esternón; el `off` se espeja igual para el compañero, así que sirve para los dos |
| 10-17 | barbell-sumo-deadlift-high-pull | Marcar el stance ancho (sumo) de perfil | frame con `stance: true` + `stanceLabel` (tarjeta "VISTA DE ARRIBA" de pies); no usar `ll` para esto |
| 10-17 | barbell-sumo-deadlift-high-pull | El tirón alto a la barbilla es difícil de armar con `ua`/`fa` a mano | grip IK `g: 1` con `hy` a la altura de la barbilla (`-800`) y `ed: 1`: el codo se abre solo hacia adelante (codos altos) y la barra llega al mentón |
| 10-17 | barbell-front-rack-reverse-lunge | Zancada hacia atrás: el pie de adelante queda fijo y el de atrás se mueve | el pie delantero es la pierna cercana con `rx` fijo (290) y solo cambia el `hip` (s/t); la pierna de atrás es la lejana (`s2`/`t2`), derivada de la cadera. La geometría final reusa la de una zancada hacia adelante (s/t `1.95/-82.31`, s2/t2 `89.94/10.81`) |
| 10-17 | (etiquetas) | Un label con `anchor: "end"` en `x < 360` se corta igual si el texto es largo (`BARRA EN LOS HOMBROS`) | acortar el texto o pasarlo al lado derecho (`x > 660`); el check de layout no siempre lo marca |
| 10-18 | wall-ball-box-over | Saltar por encima de un cajón con el atleta fijo se lee mal | el prop `box` ({x0,x1,h}) va en `propStatic` y el atleta cruza moviendo la cadera con `hip` (de `[-250,-470]` a `[560,-470]`), pico en el aire con `hip:[170,-690]` y piernas recogidas (`s 44`,`t -62`): los pies quedan por encima del cajón |
| 10-18 | wall-ball-box-over | Sostener la pelota al pecho con las manos | grip IK `g: 1` + `hb: 1` con `hx 70`/`hy 150` (objetivo relativo al torso) y prop `wallball {wall:false, off:[34,-34]}`; el agarre sigue al torso cuando cambian `b`/`hd` (cargá, salto, aterrizaje) |
| 10-18 | barbell-push-press | La barra pasa del rack frontal (hombros) a las manos (arriba de la cabeza) | prop `barbell` con `blend: true`: `bf 1` en las poses de rack/dip y `bf 0` cuando la levantan los brazos (PRESS/LOCK), la barra interpola sola entre torso y manos |
| 10-18 | (miniaturas) | La barra/disco arriba de la cabeza choca con la fila de tags | en pose de bloqueo (LOCK) bajar con `zoom ≤ 0.95` y `dy` ~220: la barra queda en y stage ≈ 826 y los chips terminan en ≈ 670 |
| 10-18 | couch-stretch | Rodilla trasera en el piso con la canilla vertical contra la pared | la pierna de atrás va como lejana con `s2: 180` (la canilla sube del tobillo a la rodilla) y `t2` recalculado por pose (`acos((16 - hipY)/240)`) para que la rodilla no se hunda bajo el piso; la de adelante se resuelve con `{hip, ankle}` (IK, pie fijo) |
| 10-18 | (moves) | Un `seq`/`loop` sin `until` ni `count` no corta nunca y el move list crece sin fin (Node se queda sin memoria) | pasar siempre `until: "end"` o `count`; sin los dos, el `while` corre infinito y el build muere con heap OOM |
| 10-18 | (etiquetas) | Un label con `y > ~1579` queda tapado por la barra de subtítulos (`#sub-XX` arranca ahí) | mantener las etiquetas por encima de ~1560 o subirlas a una zona segura |
| 10-18 | (poses de piso) | Se ve raro cuando un pie queda fijo y la cadera se mueve | usar `{hip, ankle}` (IK) en la pierna de apoyo y dejar la otra con ángulos explícitos o derivados de la cadera |

## Pendientes / ideas

- Implementos a dibujar antes de los próximos de la lista: bandas, cuerda para saltar, disco (cajón, SkiErg, trineo, balón medicinal, mancuernas y barra en el piso: 10-15)
  (ya están: remo, kettlebell, barra, wall ball, assault bike y barra de dominadas, 10-15) (ver columna Implemento del CHECKLIST).
- Vista de frente no existe: elegir siempre la vista lateral que mejor muestre el movimiento (rotaciones y aperturas
  laterales —ej. estiramientos de tríceps, muñeca— se leen mal de costado: resolverlo con overlays y texto).
- ~~Agarre independiente del lado lejano~~: hecho con `g2` (10-15).
- Personajes en el piso se ven chicos (mucho espacio vacío arriba): se podría subir `scale` a ~0.95 con `x` centrado.
