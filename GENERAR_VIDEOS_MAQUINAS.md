# GENERAR_VIDEOS_MAQUINAS — videos de máquinas de gimnasio

> **Para el modelo / agente que lee esto:** este archivo es una orden de trabajo completa para los videos de
> **máquinas de gimnasio** (no CrossFit). Es un **complemento** de `GENERAR_VIDEOS.md`: todo lo de ese archivo vale
> igual (entorno, reglas fijas, poses, overlays, check, render, reporte) **salvo lo que este archivo cambia**.
> Está escrito para cualquier herramienta (Claude Code, opencode, ChatGPT/Codex, Cursor, Aider…) y cualquier modelo.
> No asumas nada que no esté acá, en `GENERAR_VIDEOS.md` o en los archivos que se indican.

**Lectura obligatoria antes de empezar** (en este orden): `GENERAR_VIDEOS.md` → **este archivo** →
`plantilla/README.md` → `plantilla/BITACORA.md`.

---

## Cómo usarlo (para el usuario): prompts de ejemplo

```
Seguí GENERAR_VIDEOS_MAQUINAS.md. LOTE: 0 (piloto).
```
```
Seguí GENERAR_VIDEOS_MAQUINAS.md. CANTIDAD: 3. PREFIJO: OC
```
```
Seguí GENERAR_VIDEOS_MAQUINAS.md. EJERCICIOS: leg-extension, seated-leg-curl. SOLO_FICHAS: sí
```

Parámetros: los mismos de `GENERAR_VIDEOS.md` §0 (`CANTIDAD`, `PREFIJO`, `EJERCICIOS`, `SOLO_FICHAS`) más
`LOTE` (número de lote de la §3: hacé todos los ejercicios de ese lote). Si no hay `CANTIDAD` ni `LOTE` ni
`EJERCICIOS`, preguntá. Sin `PREFIJO` → sin prefijo (regla de siempre).

---

## 1. Qué cambia respecto de los videos de CrossFit

| Tema | CrossFit (`GENERAR_VIDEOS.md`) | Máquinas (este archivo) |
|---|---|---|
| Lista maestra | `ejercicios/ejercicios.csv` | **`ejercicios/maquinas.csv`** (una fila = un video) |
| CHECKLIST | tabla principal, `#` 1, 2, 3… | sección **🏋️ Máquinas de gimnasio** al final, `#` **M1, M2…** |
| Duración | 40–52 s, 7 escenas | **90–150 s, 14–18 escenas** (ver §5) |
| Enfoque | cómo se hace | cómo se **ajusta** la máquina, cómo se hace, **cómo NO se hace** (con corrección) y **tips del profe** |
| Implemento | casi siempre ya dibujado | **cada máquina hay que dibujarla** en `plantilla/runtime.js` (ver §4) |
| Ficha | — | `"maquina": true` (obligatorio) |
| `category` | `CROSSFIT · …` | `GIMNASIO · <ZONA>` (ej. `GIMNASIO · PIERNAS`, `GIMNASIO · CARDIO`) |
| Voz | nombre en inglés (Kokoro `af_heart`) + Daniela | **igual**: el nombre de la máquina en inglés y el resto Daniela, con detalle |
| YouTube | estructura de §6.8 | estructura propia (ver §8) |
| Público | alumnos de un box | alumnos de gimnasio, sobre todo principiantes |

Todo lo demás no cambia: 1080×1920, español rioplatense con voseo, personaje de perfil mirando a la derecha,
música base, `revisado: false`, no tocar `salida/subidos/`, no commitear sin pedido.

---

## 2. De dónde salen los datos

- **`maquinas_gimnasio.xlsx`** (raíz): planilla del usuario (hoja «Máquinas»). **No la edites**: tiene columnas que
  completa él (`Mi puntaje`, `Mi ranking`, `Mis notas`).
- **`ejercicios/maquinas.csv`**: lista de producción armada desde la planilla (separador `;`, todo entre comillas,
  UTF-8 con BOM). **Orden de filas = orden de producción.** Las máquinas multiuso se partieron en un video por
  ejercicio (Smith → sentadilla y press de banca; Polea → crossover, face pull, curl, tríceps; abductores y aductores;
  gemelos de pie y sentado; dominadas y fondos asistidos). Columnas:

| Columna | Qué es | Dónde se usa |
|---|---|---|
| `clave` | slug del video (`ejercicios/<clave>.json`) | todo |
| `lote` | lote de producción (§3) | orden de trabajo |
| `nombre` | nombre en **inglés** = `name` de la ficha | portada (lo dice la voz inglesa) |
| `nombre_es` | nombre en castellano | `sub` de la portada, escena «LA MÁQUINA», YouTube |
| `otros_nombres` | alias de la planilla | escena «LA MÁQUINA», tags de YouTube |
| `maquina_excel`, `fila_excel` | fila de origen en el xlsx | trazabilidad |
| `tipo`, `zona` | Cardio/Fuerza, zona | `category`, `tags` |
| `musculos_principales`, `musculos_secundarios` | músculos | escena «LA MÁQUINA», 🎯 QUÉ TRABAJA |
| `como_se_usa` | ajuste + ejecución | escenas de ajuste, posición y pasos |
| `que_no_hacer` | errores típicos (separados por `;`) | escenas **ASÍ NO** (§6) |
| `tips_profe` | tips de profe (separados por ` · `) | escenas **TIPS DEL PROFE** y claves (§7) |
| `nivel`, `nivel_texto` | 1–5 | descripción de YouTube, advertencias |
| `dosis` | series × reps o minutos | escena **A ENTRENAR** |
| `prop` | nombre del implemento en `runtime.js` | `props[].type` de la ficha (§4) |
| `vista` | `lateral` o `lateral + topview …` | si hace falta tarjeta `topview` (ver `GENERAR_VIDEOS.md` §6.6) |

- Ver una fila: `node plantilla/make-exercise.mjs <clave> --info` (busca en los dos CSV).
- Si el usuario agrega máquinas a la planilla: agregá la(s) fila(s) a `maquinas.csv` a mano (un video por ejercicio)
  y corré `node plantilla/make-exercise.mjs --checklist`.
- Podés mejorar `tips_profe` o `que_no_hacer` en el CSV con criterio de profe de musculación; anotalo en el reporte.
- **Ojo con las filas partidas de una máquina multiuso** (polea, Smith, asistida, abductores/aductores, gemelos): al
  armar el CSV quedaron con los datos genéricos de la máquina (`musculos_principales` "Depende del ejercicio…",
  `zona` "Cuerpo completo", `otros_nombres` de otro ejercicio). Antes de escribir la ficha, revisá que esas columnas
  hablen de **ese** ejercicio (el 2026-10-22 se corrigieron las 11 filas de los lotes 2, 4 y 5).

---

## 3. Plan por lotes

Las máquinas de un lote comparten dibujo o familia de dibujo (asiento + respaldo, pila de peso, polea…), así lo que
se programa para una sirve para las siguientes.

| Lote | Ejercicios (`clave`) | Qué hay que dibujar |
|---|---|---|
| **0 · piloto** | `leg-press`, `lat-pulldown` | `legpress` (prensa 45°: carro sobre rieles + plataforma), `latpulldown` (columna, polea alta, barra, rodillo de muslos). **Incluye el helper de pila de peso** (§4.2) |
| 1 · piernas guiadas | `leg-extension`, `seated-leg-curl`, `lying-leg-curl`, `hack-squat`, `pendulum-squat` | sillón con rodillo y eje; camilla; hack (respaldo sobre rieles); péndulo (respaldo en arco) |
| 2 · poleas | `seated-cable-row`, `cable-triceps-pushdown`, `cable-bicep-curl`, `cable-face-pull`, `cable-crossover` | `cable` (columna + polea regulable + cable + accesorio: barra o soga), `cablerow`, `cablecrossover` (doble columna) |
| 3 · tren superior sentado | `machine-chest-press`, `machine-shoulder-press`, `pec-deck-fly`, `machine-lateral-raise`, `machine-preacher-curl` | asiento + respaldo + brazos de palanca con eje |
| 4 · cadera y gemelos | `hip-thrust-machine`, `hip-abduction-machine`, `hip-adduction-machine`, `standing-calf-raise-machine`, `seated-calf-raise-machine` | aductor/abductor (necesitan `topview`), gemelos (escalón + almohadillas) |
| 5 · Smith, asistidas y core | `smith-machine-squat`, `smith-machine-bench-press`, `assisted-pull-up-machine`, `assisted-dip-machine`, `ab-crunch-machine`, `back-extension-45` | `smith` (rieles + barra guiada + topes), `assisted` (plataforma de rodillas + manijas), crunch, banco 45° |
| 6 · cardio | `treadmill`, `stationary-bike`, `elliptical-trainer`, `rowing-machine`, `stair-climber` | cinta (con `floorScroll`), bici, elíptico, escaladora. `rowing-machine` usa el `rower` que ya existe |

**Estado (2026-10-22):** el piloto se aprobó el 2026-10-21 y los 31 videos restantes (lotes 1–6) ya tienen la máquina
dibujada en `runtime.js` y ficha. Si se suman máquinas nuevas, seguí este mismo plan por familias.

**Regla del piloto:** hasta que el usuario apruebe el lote 0 (`"revisado": true` en `leg-press` y `lat-pulldown`),
**no arranques el lote 1**. Si el usuario pide cambios de estilo/duración/estructura en el piloto, actualizá este
archivo con lo que decidió antes de seguir.

---

## 4. Dibujar la máquina (implemento nuevo)

Seguí `GENERAR_VIDEOS.md` §4.4 y mirá en `runtime.js` cómo están hechos `rower`, `airbike`, `sled` o `bench`.

### 4.1 Reglas de dibujo

- Un `if (pr.type === "<prop>") { … }` por máquina dentro del bloque `PROPS` de `runtime.js`, con el comentario de
  parámetros arriba (como los demás). El nombre del prop es la columna `prop` del CSV: el CHECKLIST muestra
  «(falta dibujar)» hasta que encuentra `pr.type === "<prop>"` en `runtime.js`.
- Vista lateral, mismo estilo plano: colores `METAL`, `METAL_D`, `PLATE*`, tapizado `#1A1A1A`, detalle `ACCENT`
  (pasador de la pila, ejes, perillas de regulación). Sin texto dentro del dibujo.
- Piezas fijas (estructura, asiento, respaldo) en `propBack` o `propStatic`; piezas que se mueven con el cuerpo
  (rodillo, brazo de palanca, barra, carro de la prensa) con `propUpdates.push((n, f) => …)` siguiendo la
  articulación que corresponde (`n.A` tobillo, `n.K` rodilla, `n.W` mano, `n.H` cadera…). Lo que va en las manos,
  delante del brazo cercano (`propFront` o `handleNode`, como el `rower`).
- **La máquina tiene que verse completa y reconocible** en la escena «LA MÁQUINA»: usá `rig.scale` ~0.66–0.80 y
  `"shadow": false`. Piso: `rig.y = 1532 - 34 * scale` (BITÁCORA 10-21). **La parte más alta de la máquina tiene que
  quedar en y ≥ ~760 de pantalla**: más arriba pisa los chips de la portada (piloto: jalón con `scale 0.66`).
- Labels: en el margen izquierdo (`[130, y]`, `anchor: "start"`) o a la derecha de la columna (`[870, y]`, `start`);
  en el medio caen sobre las guías de la pila. Escenas `keys` con `"shrink": 0.78` (0.62 deja la máquina diminuta).
- **Antes de poner un label, calculá dónde termina la máquina en pantalla** (`y = rig.y + scale × y_rig` de la parte
  más alta del lado del label). Si la pila está a la izquierda, un label `[130, 1000]` cae justo sobre el techo de la
  pila (pasó en todo el lote 1): subilo por encima de la máquina (`y ≈ 760–900`) o pasalo al lado libre
  (`[1000, y]`, `anchor: "end"`). Regla rápida: **lado de la pila → labels arriba de la máquina; lado libre → a la
  altura de la cabeza**.
- En escenas con tarjeta `topview` la tarjeta ocupa `x 720–1020, y 820–1240`: ahí no va ningún label (usá
  `[130, 760]` o `[130, 900]`).
- Cuando el error **no se ve de perfil** (abrir/cerrar piernas, aperturas, codos altos), sumá la tarjeta `topview`
  correspondiente en los pasos y en el ASÍ NO: `fly` (aperturas, clave `al`), `abd` (abductores/aductores, clave `cs`),
  `front` (hombros, `face pull`, elevaciones laterales).
- Fichas de referencia ya hechas: **`leg-press`** (máquina de discos con carro sobre riel) y **`lat-pulldown`**
  (máquina de pila con polea). Copiá la más parecida.
- Las regulaciones que se explican en el video (altura del asiento, respaldo, rodillo, topes) tienen que existir
  en el dibujo como piezas separadas, para poder marcarlas con `ring` / `label`.
- Documentá el prop en la tabla de Implementos de `plantilla/README.md`, en la tabla del §4.3 de
  `GENERAR_VIDEOS.md` y con una fila en `plantilla/BITACORA.md`.

### 4.2 Pila de peso (helper compartido, se hace en el piloto)

Casi todas las máquinas de fuerza tienen una **pila de placas con pasador**. Programala una sola vez como función
reutilizable dentro de `runtime.js` (ej. `weightStack(parent, x, y, { placas, alto })` que devuelve
`lift(px)`): las placas de arriba del pasador suben cuando la palanca/cable se mueve y bajan al volver.
Así se ve el error «dejar caer el peso / que la pila choque» (escena ASÍ NO) y la elección de peso (escena de ajuste).
La subida se calcula en el `propUpdates` a partir del desplazamiento de la articulación respecto de la pose inicial.

### 4.3 Antes de escribir escenas

`node plantilla/pose-lab.mjs <clave>` con la máquina y todas las poses: el cuerpo no atraviesa el asiento ni la
almohadilla, las manos llegan a las manijas, el eje de la máquina coincide con la rodilla/codo/hombro cuando
corresponde, y la pila de peso sube y baja.

---

### 4.4 Generador de fichas (lo que mejor funcionó, 31 máquinas en una sesión)

Las fichas de máquinas se arman con Python, no a mano. En `plantilla/maquinas/` quedan:

- `common.py` — **FK idéntica a `runtime.js`** (`fk(pose)` devuelve A K H S N E W en px del rig, respeta `hip`/`ankle`
  IK, `al`, `ul`, `fl`), `check(poses)` (avisa si la mano no llega: > 331 px), `Stage(rig)` (rig → pantalla para los
  overlays), helpers `hook/step/keys/reps/ring/lab/arrow/NO`, `yt_desc()` con la estructura del §9, `base_spec()`
  (escribe props/poses/rig desde el CSV) y `save()` (valida `vo` ≤ 135, labels ≤ 22 caracteres dentro del lienzo,
  poses existentes en los moves, `seq` con `until`, título y tags de YouTube).
- `lN_poses.py` / `lN_frames.py` — uno por lote: primero poses + props (correr, pose-lab, mirar, ajustar), después
  escenas + YouTube + miniatura.

Flujo por lote: `python plantilla/maquinas/lN_poses.py` → `node plantilla/pose-lab.mjs <clave>` de cada una (de a
una si hay renders corriendo) → mirar las hojas → `python plantilla/maquinas/lN_frames.py` → `make-exercise` de a 3
→ contact sheets → `--render` de a 2. Para muchos videos, `plantilla/maquinas/cola.sh`:
`bash plantilla/maquinas/cola.sh render <claves…>` (renders de a 2) y, a la vez, `bash plantilla/maquinas/cola.sh build
<claves…>` (make-exercise de a 1); al final imprime duración, check y archivo de cada video. Con 2 renders + 1 build
en paralelo no falla el navegador. Los overlays se ubican con las articulaciones de `fk()` pasadas por `Stage`,
nunca a ojo. Ring del pasador de una pila `weightStack(…, x, 10, {n: 12, pin})`: `(x + 51, -254 + (pin − 0,5) × 22)`.

## 5. Estructura de escenas (14–18 escenas, 90–150 s)

Las mismas reglas de `GENERAR_VIDEOS.md` §6.2 por escena (**`vo` ≤ ~130 caracteres**, head ≤ ~14 caracteres, labels
≤ ~18, nada con y > 1580). Para explicar con detalle se usan **más escenas**, no `vo` más largos.

| # | `kind` / badge | Qué muestra | vo (ejemplo `leg-press`) | `min` |
|---|---|---|---|---|
| 1 | `hook` · categoría | movimiento completo en loop; head = nombre en inglés; `sub` = `nombre_es` | "Leg Press: la prensa de piernas a 45 grados, para cuádriceps y glúteos." (empieza con el `name` exacto) | 5–6 |
| 2 | `LA MÁQUINA` | la máquina entera; labels de las partes (asiento, respaldo, plataforma, pila/discos) | "También le dicen prensa 45. Trabaja cuádriceps y glúteos, y suma isquios y aductores." | 6–7 |
| 3 | `AJUSTE 1` | regulación principal (asiento, respaldo, eje, rodillo) con `ring` | "Antes de cargar, ajustá el respaldo: la cadera y la espalda tienen que quedar bien apoyadas." | 6–7 |
| 4 | `AJUSTE 2` | segunda regulación / topes de seguridad / elegir el peso (pasador) | "Elegí un peso que puedas mover doce veces con control, sin que la técnica se rompa." | 6–7 |
| 5 | `POSICIÓN INICIAL` | cómo ubicarse: apoyos, agarre, pies | "Pies al ancho de hombros, en el centro de la plataforma. Agarrate de las manijas." | 6–7 |
| 6–9 | `PASO 1 / 4` … `PASO 4 / 4` (con `numeral`) | fases: destrabar / bajar / punto más bajo / subir | "Paso dos. Bajá en dos o tres segundos hasta que la rodilla quede cerca de noventa grados." | 6–8 |
| 10 | `RESPIRACIÓN` | el movimiento lento | "Tomá aire al bajar y soltalo mientras empujás." | 5–6 |
| 11–13 | `ASÍ NO · 1/3` … | un error por escena (de `que_no_hacer`), pose `_BAD` + label `ASÍ NO` (§6) | "Error: bloquear las rodillas arriba. Dejalas apenas flexionadas: la carga queda en el músculo." | 6–8 |
| 14 | `kind: "keys"` · `TIPS DEL PROFE` | 3–4 tips cortos (de `tips_profe`) | "Tip de profe: las manos en las manijas, nunca empujando las rodillas." | 8–9 |
| 15 | `kind: "keys"` · `CLAVES` | 3–4 claves de técnica | "Claves: espalda apoyada, rodillas en la línea de los pies, bajada lenta y sin trabar." | 8 |
| 16 | `kind: "reps"` · `A ENTRENAR` | dosis + descanso + cómo progresar | "Tres series de diez a doce, con un minuto y medio de pausa. Subí el peso cuando las doce salgan fáciles." | 7–8 |
| 17 *(opcional)* | `AL TERMINAR` | trabar la máquina, descargar, dejarla lista | "Al terminar, trabá la máquina antes de sacar los pies y descargá los discos." | 5–6 |

- Con `vo` de ~110–130 caracteres cada escena dura ~7 s: **14 escenas ≈ 95–100 s, 15–17 ≈ 105–120 s**. Máquinas
  simples: 14 (2 ASÍ NO, sin AL TERMINAR) alcanza para pasar los 90 s.
- Total esperable: **90–150 s**. Menos de 90 s → faltan errores, ajustes o tips; más de 150 s → recortá escenas,
  no texto. La música base dura 177 s: no pases de ~170 s.
- Máquinas simples (gemelos, abductor) pueden tener 2 escenas ASÍ NO y una sola de ajuste; las complejas (Smith,
  hack, remo, prensa) 3–4 ASÍ NO.
- Cardio: los «pasos» son técnica (postura, pisada/pedaleo, ritmo) y la escena A ENTRENAR es tiempo/intensidad
  (ej. «10 MIN» + «2 MIN SUAVE · 6 MIN RITMO · 2 MIN SUAVE»).
- Con más de 9 escenas el contact sheet sale en varias hojas (`contact-sheet-1.jpg`, `-2.jpg`, …): **revisalas todas**.
- `hook` con nombres con números: `"nombreEnVoz"` (ej. `45 Degree Back Extension` → `"Forty five degree back extension"`).
- `pronuncia` sirve igual para palabras en inglés que lea Daniela en el resto (`"Smith": "Esmit"`, `"press": "pres"`).

---

## 6. Escenas «ASÍ NO» (cómo NO hacerlo)

Es la parte más importante para el usuario: mostrar el error y su corrección.

- Una escena por error, tomado de `que_no_hacer` (los más peligrosos primero: rodillas, lumbar, hombros, golpes de la pila).
- Pose de error con sufijo `_BAD` (ej. `KNEES_LOCKED_BAD`, `HIPS_UP_BAD`), label **`ASÍ NO`** arriba del cuerpo y, si
  ayuda, un `ring` en la articulación que falla.
- `vo` con la estructura **"Error: <qué pasa>. <Corrección en voseo>."** (≤ 130 caracteres).
- Terminá la escena **en la pose mala** (`{cut: BUENA, at: 0}`, `{to: MALA, at: 0.5}`) y arrancá la siguiente con
  `cut` a la buena (BITÁCORA 10-21: si vuelve a la buena, el contact sheet no muestra el error).
- Errores de **ritmo** (rebotar, impulso, dejar caer el peso, recorrido corto): un `seq` rápido entre las dos poses
  (`[["MALA", 0.3], ["BUENA", 0.3]]` con `until: 4.0`) y un `to` final a la pose mala, con un label ("SIN CONTROL",
  "DE GOLPE") — el contact sheet así muestra la pose mala.
- Errores de **ubicación** (banco corrido, pies muy adelante, rodilla fuera del eje): moviendo `hip`/`ankle` de la pose,
  la máquina queda fija y se ve la diferencia (ring en la articulación y en el eje/tope).
- Si el error no se ve de perfil (rodillas hacia adentro, codos abiertos), usá `topview` (`GENERAR_VIDEOS.md` §6.6) o
  un overlay explícito (flechas + label), nunca solo la voz.

## 7. Tips del profe

- Salen de `tips_profe` (separados por ` · `). Elegí los 3–4 que más ayudan a un principiante y que se puedan
  mostrar o señalar en pantalla.
- Van en la escena `keys` «TIPS DEL PROFE» (textos de ≤ ~30 caracteres) y los demás en la descripción de YouTube.
- Tono de profe en el salón: corto, concreto, en voseo ("Pensá en llevar los codos al bolsillo").

---

## 8. Ficha: diferencias con §6.1 de `GENERAR_VIDEOS.md`

```jsonc
{
  "slug": "leg-press",
  "name": "Leg Press",                         // columna nombre (inglés)
  "maquina": true,                             // obligatorio en videos de máquina
  "category": "GIMNASIO · PIERNAS",            // "GIMNASIO · " + zona en MAYÚSCULAS (máx. 2 partes)
  "tags": ["Cuádriceps", "Glúteos"],
  "descripcion": "<como_se_usa del CSV>",
  "revisado": false, "notas": "",
  "rig": { "x": 470, "y": 1506, "scale": 0.76 },
  "shadow": false,
  "props": [{ "type": "legpress" /* parámetros del prop */ }],
  "poses": { "...": {} },
  "frames": [ /* §5 */ ],
  "miniatura": { "pose": "<la más reconocible con la máquina>", "zoom": 1.0 },
  "youtube": { /* §9 */ }
}
```

## 9. Bloque `youtube` para máquinas

- `titulo` (≤ 100): `<Name> 🔥 Cómo usar la <nombre_es> bien | Gimnasio` (ej. `Leg Press 🔥 Cómo usar la prensa de piernas sin lastimarte | Gimnasio`).
- `tags` (8–15, ≤ 500 caracteres): nombre en inglés, `nombre_es`, `otros_nombres`, "cómo usar <máquina>", zona,
  músculos, "gimnasio", "máquinas de gimnasio", "principiantes".
- `descripcion` (≤ 5000, sin `<` ni `>`), estructura fija:

```
🔥 <NAME EN MAYÚSCULAS> (<nombre_es>) — <para qué sirve en una línea>

<gancho: el problema que resuelve / el error más común. "Este video es para vos."> 💪

🛠️ AJUSTE DE LA MÁQUINA
1️⃣ … (las regulaciones del video)

📋 PASO A PASO
1️⃣ … (los mismos pasos que la voz)

❌ ERRORES COMUNES
• <error> → <corrección>   (todos los de que_no_hacer)

💡 TIPS DEL PROFE
• … (todos los de tips_profe)

🎯 QUÉ TRABAJA
<musculos_principales> · <musculos_secundarios>

⏱️ CUÁNTO
<dosis> + descanso + cómo progresar. Nivel: <nivel_texto>.

🙌 Si te sirvió, dejá tu like, guardalo y compartilo con quien entrena con vos.

<si nivel ≥ 3: "Si es tu primera vez en esta máquina, pedile al profe del gimnasio que te ajuste la máquina y te mire las primeras series.">

<contenido de plantilla/youtube-deslinde.txt TAL CUAL>

#Gimnasio #<NameSinEspacios> #<Zona> #Musculacion #Entrenamiento
```

La última línea son los hashtags (el script inserta antes el crédito de las voces).

## 10. Generar, revisar, renderizar y cerrar

Igual que `GENERAR_VIDEOS.md` §5.5–5.7, §8 y §9, con estos agregados:

1. `node plantilla/make-exercise.mjs <clave>` → revisá **todas** las hojas del contact sheet y la miniatura.
   Duración esperable 90–150 s (el builder la imprime: `✓ index.html — N escenas, Xs`).
2. Render: con estas duraciones tarda ~10–13 min por par: de a **2** en paralelo como máximo. Mientras renderiza se
   puede correr el pose-lab del lote siguiente **de a uno** (no falla); `make-exercise` de a 3 cuando no hay renders.
3. `node plantilla/make-exercise.mjs --checklist` → en la sección **🏋️ Máquinas de gimnasio** cada video tiene que
   tener Ficha, Voz, Composición, Check, Render, YouTube, Miniatura y Nombre EN en ✅, y la columna Implemento sin
   «(falta dibujar)».
4. Reporte al usuario (formato de `GENERAR_VIDEOS.md` §9) usando el número `M<n>`, y sumando: máquinas dibujadas,
   errores mostrados por video y tips que agregaste o cambiaste en el CSV.
