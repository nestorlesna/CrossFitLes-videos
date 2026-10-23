# GENERAR_VIDEOS_DATASET — videos de los ejercicios del dataset externo

> **Para el modelo / agente que lee esto:** este archivo es la orden de trabajo para los videos de la sección
> **📚 Dataset de ejercicios** del `CHECKLIST.md` (`#` D1, D2…). No es un formato nuevo: cada fila se hace con
> `GENERAR_VIDEOS.md` (formato **corto**) o con `GENERAR_VIDEOS_MAQUINAS.md` (formato **máquina**), según la columna
> `formato`. Todo lo de esos archivos vale igual **salvo lo que este archivo cambia**. Sirve para cualquier herramienta
> (Claude Code, opencode, Codex, Cursor, Aider…) y cualquier modelo.

**Lectura obligatoria antes de empezar** (en este orden): `GENERAR_VIDEOS.md` → `GENERAR_VIDEOS_MAQUINAS.md` (si hay
filas de formato máquina) → **este archivo** → `plantilla/README.md` → `plantilla/BITACORA.md`.

---

## Cómo usarlo (para el usuario): prompts de ejemplo

```
Seguí GENERAR_VIDEOS_DATASET.md. LOTE: D01.
```
```
Seguí GENERAR_VIDEOS_DATASET.md. CANTIDAD: 5. PREFIJO: OC
```
```
Seguí GENERAR_VIDEOS_DATASET.md. EJERCICIOS: lever-seated-crunch-chest-pad, smith-shrug. SOLO_FICHAS: sí
```
```
Seguí GENERAR_VIDEOS_DATASET.md. PROPS: ezbar, stabilityball.   ← solo dibujar implementos nuevos, sin videos
```

Parámetros: los de `GENERAR_VIDEOS.md` §0 (`CANTIDAD`, `PREFIJO`, `EJERCICIOS`, `SOLO_FICHAS`) más `LOTE` (código
`Dxx` de la columna `lote`: hacé todo ese lote) y `PROPS` (dibujar esos implementos en `runtime.js`, §5). Si no hay
`CANTIDAD`, `LOTE`, `EJERCICIOS` ni `PROPS`, preguntá. Sin `CANTIDAD` explícita, nunca hagas más de un lote.

---

## 1. De dónde salen los datos

| Archivo | Qué es | ¿Se edita? |
|---|---|---|
| `C:\DATOS\DESARROLLOS\React\CrossFitLes\BKP\exercises-dataset-main` | dataset externo: `data/exercises.json` (1324 ejercicios), `videos/<id>-<media>.gif` (animación), `images/` (miniatura 180×180) | **no** |
| `ejercicios/dataset.csv` | los ejercicios del dataset que **faltan** (1230), en orden de producción | **no a mano**: lo regenera el script |
| `ejercicios/dataset-equivalencias.csv` | ejercicios del dataset que **ya tenemos** con otro nombre (`id;clave;motivo`) | sí, a mano |
| `plantilla/dataset-import.mjs` | arma `dataset.csv` (compara con `ejercicios.csv` y `maquinas.csv`, saca repetidos pov/male/female) | — |

- Regenerar la lista: `node plantilla/dataset-import.mjs` y después `node plantilla/make-exercise.mjs --checklist`.
  Las claves no cambian al regenerar (son el slug del nombre del dataset), así que las fichas hechas no se pierden.
- **Si al hacer una ficha descubrís que el ejercicio ya existe** con otro nombre (la columna Notas dice «parecido a
  …» como pista): no hagas el video; agregá la línea `"<id_dataset>";"<clave existente>";"<motivo>"` a
  `dataset-equivalencias.csv`, regenerá y anotalo en el reporte.
- Ver una fila: `node plantilla/make-exercise.mjs <clave> --info` (busca en los tres CSV).

Columnas de `dataset.csv`:

| Columna | Qué es | Dónde se usa |
|---|---|---|
| `clave` | slug del video (`ejercicios/<clave>.json`) | todo |
| `id_dataset` | id del ejercicio en `exercises.json` | trazabilidad, equivalencias |
| `lote` | `Dxx · <familia>` (lotes de 10 dentro de cada familia de implemento) | orden de trabajo |
| `familia` | familia de implemento (palanca, Smith, poleas, barra, mancuernas, …) | orden de trabajo |
| `formato` | `maquina` → `GENERAR_VIDEOS_MAQUINAS.md` · `corto` → `GENERAR_VIDEOS.md` | qué instructivo seguir |
| `nombre` | nombre en **inglés** = `name` de la ficha (lo dice la voz inglesa) | portada |
| `nombre_es` | **vacío**: lo completás vos (ver §3) | `sub` de la portada, YouTube |
| `equipo_dataset`, `implemento` | implemento original (inglés) y en castellano | escena del implemento / máquina |
| `props` | prop(s) **sugeridos** de `runtime.js`, separados por ` + ` (ej. `dumbbell + bench`) | `props[].type` de la ficha |
| `zona`, `musculo_objetivo`, `grupo_muscular`, `musculos_secundarios` | ya en castellano | `category`, `tags`, 🎯 QUÉ TRABAJA |
| `similar_a` | clave nuestra más parecida (pista; ficha base para copiar poses) | §2 |
| `descripcion_es` | instrucciones del dataset en castellano neutro (tuteo) | base de `descripcion`; **pasar a voseo** |
| `pasos_es`, `pasos_en` | los mismos pasos separados por ` · ` | pasos de la voz / escenas |
| `gif`, `imagen` | ruta absoluta de la animación y la miniatura del dataset | **solo referencia visual** (§4) |
| `atribucion` | © Gym visual | — (no va en el video, ver §4) |

---

## 2. Qué cambia respecto de los otros instructivos

| Tema | Formato `corto` (`GENERAR_VIDEOS.md`) | Formato `maquina` (`GENERAR_VIDEOS_MAQUINAS.md`) |
|---|---|---|
| Elegir ejercicios | sección 📚 del CHECKLIST, primeros con Ficha ⬜ (o el `LOTE`) | ídem |
| `category` | **`GIMNASIO · <ZONA>`** (no `CROSSFIT`; son ejercicios de gimnasio) | `GIMNASIO · <ZONA>` |
| `maquina` | no va | `"maquina": true` |
| `descripcion` | `descripcion_es` pasada a **voseo rioplatense** y resumida (1–2 frases) | `descripcion_es` en voseo |
| `tecnica_coach` / claves | no hay columna: sacalas de `pasos_es` + tu criterio de profe | `que_no_hacer` y `tips_profe` no existen: escribilos vos (3 errores, 4–5 tips) |
| `dosis` | no hay columna: elegí una razonable (fuerza 3 × 8–12, core 3 × 30 s, estiramiento 2 × 30 s por lado, cardio minutos) | ídem |
| YouTube | estructura de `GENERAR_VIDEOS.md` §6.8, pero título `… | Gimnasio`, cierre «compartilo con tu compañero de entrenamiento» y hashtags `#Gimnasio #<NombreSinEspacios> #<Zona> #Musculacion #Entrenamiento` | estructura de `GENERAR_VIDEOS_MAQUINAS.md` §9 |
| Ficha base para copiar | la de `similar_a` si existe; si no, la del prop (tabla de `GENERAR_VIDEOS.md` §4) | la de la máquina del mismo prop (`plantilla/maquinas/`) |

Todo lo demás no cambia: 1080×1920, castellano rioplatense con voseo, voz Daniela + nombre en inglés con Kokoro,
personaje de perfil mirando a la derecha, música base, `revisado: false`, no tocar `salida/subidos/`, no commitear
sin pedido.

**Variantes (`v. 2`, `v. 3`, «with rope attachment», «on stability ball», etc.)**: son ejercicios distintos en el
dataset. Mirá el GIF para ver qué cambia (agarre, ángulo, accesorio) y dejalo claro en la voz y en `nombre_es`
(ej. «Remo en polea con soga»). Si dos filas quedan iguales en la práctica, marcá la segunda como equivalente (§1).

---

## 3. Nombre en castellano

`nombre_es` está vacío en el CSV (el dataset solo trae el nombre en inglés). Al hacer la ficha decidí el nombre en
castellano como lo diría un profe de gimnasio en Uruguay/Argentina («Press inclinado con mancuernas», «Jalón con agarre
cerrado», «Encogimientos en Smith») y usalo en el `sub` de la portada y en YouTube. **No edites `dataset.csv`**: el
nombre queda en la ficha (`ejercicios/<clave>.json`). `name` sigue siendo el inglés de la columna `nombre`, en Title
Case, sin `(male)` ni `pov`. Revisá la pronunciación del nombre inglés (`GENERAR_VIDEOS.md` §6.7): nombres como
«Lever», «Smith», «Sled», «EZ» van en `pronuncia` si Kokoro los dice mal.

---

## 4. El GIF del dataset: referencia, nunca material del video

Las animaciones e imágenes del dataset son **© Gym visual** (ver `NOTICE.md` del dataset): se pueden mirar para
entender el movimiento, **pero no se copian al proyecto, no se incrustan en el video, no se usan de miniatura ni se
calcan**. El personaje y el implemento se dibujan con el sistema de siempre (`runtime.js`).

Para mirar el movimiento cuadro a cuadro (en la carpeta temporal, no en el proyecto):

```bash
mkdir -p "$TMP/gif-<clave>" && ffmpeg -v error -i "<ruta de la columna gif>" -vf "select=not(mod(n\,4)),scale=360:-1,tile=4x2" -frames:v 1 "$TMP/gif-<clave>/hoja.png"
```

Con la hoja definí (como en `GENERAR_VIDEOS.md` §5.1): posición inicial, fases, rango de movimiento, dónde está el
implemento respecto del cuerpo y si se ve bien de perfil o necesita tarjeta `topview`. Si el GIF y `pasos_es` no
coinciden, manda el GIF (los textos del dataset a veces son genéricos).

---

## 5. Implementos (props) que faltan dibujar

La columna Implemento del CHECKLIST dice «(falta dibujar …)» cuando un prop sugerido no está en `runtime.js`. Antes de
hacer esos videos hay que dibujarlo (reglas: `GENERAR_VIDEOS_MAQUINAS.md` §4 y `GENERAR_VIDEOS.md` §4 punto 4).
Hacé **un prop por pasada** con `PROPS:`, probalo con `node plantilla/pose-lab.mjs <clave>` en 2–3 ejercicios de esa
familia, documentalo en la tabla de Implementos de `plantilla/README.md` y en la BITÁCORA, y regenerá el CHECKLIST.

| Prop sugerido | Qué es | Familias que lo usan |
|---|---|---|
| `lever` | máquina de palanca genérica (cuando el nombre no dice cuál): mirá el GIF y, si coincide con una máquina ya dibujada, usá esa | Máquinas de palanca |
| `leverrow` | remo en máquina de palanca (pecho apoyado, manijas) | Máquinas de palanca |
| `levershrug` | encogimientos en máquina | Máquinas de palanca |
| `handbike` | ergómetro de brazos | Cardio |
| `trapbar` | barra hexagonal | Barra |
| `ezbar` | barra Z (puede salir de `barbell` con la parte central quebrada) | Barra Z |
| `dipbars` | paralelas para fondos | Peso corporal, Con lastre |
| `bosu`, `stabilityball` | media esfera y fitball | Pelotas |
| `abwheel` | rueda abdominal | Accesorios |
| `battlerope`, `strap` | sogas de batalla; correa / soga de estirar | Accesorios |
| `foamroller` | rodillo de espuma | Accesorios |
| `sledgehammer`, `tire` | maza y cubierta de tractor | Accesorios |

Los props sugeridos son una primera aproximación por palabras del nombre (`plantilla/dataset-import.mjs`, función
`props`). **Si el GIF muestra otro implemento** (ej. un banco que no figura, una barra de dominadas), usá el correcto en
la ficha; si el error se repite en muchas filas, corregí la regla en `props()` y regenerá.

Ejercicios con prop ya dibujado: se pueden hacer ya. El orden del CSV pone primero, dentro de cada familia, los que
tienen el prop dibujado.

---

## 6. Plan por lotes

El orden de `dataset.csv` es por familia de implemento (así el dibujo de una sirve para las siguientes):
máquinas de palanca → prensa/hack de trineo → Smith → poleas → cardio → barra → barra Z → mancuernas → kettlebell →
bandas → con lastre → pelotas → accesorios → asistidos/estiramientos → peso corporal. Cada familia está partida en
lotes de 10 (`D01`, `D02`, …); el número de lotes y la cantidad por familia los imprime `dataset-import.mjs`.

Sugerencia de arranque (lo decide el usuario): un **piloto** con 2 filas de formato máquina (D01) y 2 de formato corto
(primer lote de Mancuernas), revisión del usuario, y recién después lotes completos.

---

## 7. Generar, revisar, renderizar y cerrar

Igual que `GENERAR_VIDEOS.md` §5.5–5.7 (o `GENERAR_VIDEOS_MAQUINAS.md` §10 para formato máquina):
`node plantilla/make-exercise.mjs <clave>` → contact sheet → `--render` → `--checklist`. La fila pasa sola de ⬜ a ✅
en la sección 📚 del CHECKLIST.

Reporte final: lo de `GENERAR_VIDEOS.md` §9 más
- `nombre_es` elegido para cada ejercicio,
- props dibujados o cambiados respecto del sugerido,
- filas marcadas como equivalentes (agregadas a `dataset-equivalencias.csv`).
