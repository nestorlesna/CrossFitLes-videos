# VidesoEjercicios — fábrica de videos de ejercicios (FitLesUY)

> **Leé esto primero, sea cual sea la herramienta que seas** (Claude Code, Claude Chat, Claude Cowork, OpenCode,
> Hermes Agent u otra). Acá está el panorama completo: qué se produce, en qué estado está, qué archivo manda para cada
> cosa y qué reglas hay que respetar porque **varias herramientas trabajan en paralelo sobre esta misma carpeta**.
> Los detalles de cada paso están en los documentos que se enlazan; este README es el mapa, no los reemplaza.

Idioma de trabajo: **español rioplatense (voseo)** en textos, voz y respuestas. Nombres de archivos y slugs en inglés.

---

## 1. Qué hacemos acá

Producimos **videos animados de ejercicios** (un personaje dibujado en HTML que hace cada movimiento, con voz en off
sintética) y los publicamos en **YouTube** (canal **FitLesUY**) y **TikTok**. Los videos alimentan la app **FitLesUY**
(gratis, código abierto, Android: <https://nestorlesna.github.io/CrossFitLes/>), que usa el dueño del proyecto para
sus rutinas; por eso la lista de ejercicios crece cuando él agrega sesiones con ejercicios nuevos.

Todo el contenido (voz TTS, imagen generada) se marca en YouTube como **«contenido alterado por IA = Sí»**.

### Los dos formatos por ejercicio

| Formato | Archivo | Qué es |
|---|---|---|
| **Largo** (el de siempre) | `salida/<slug>.mp4` | Vertical 1080×1920, ~40–150 s. **Explica el ejercicio** con voz (Daniela, español) y tarjetas de técnica. Título tipo `Nombre 🔥 … paso a paso | CrossFit`. |
| **Corto** | `salida/<slug>.corto.mp4` | Vertical 1080×1920, 8–16 s, **sin voz**, solo muestra 2–3 repeticiones. Va como YouTube Short, título `Nombre 🎬 Así se hace en segundos | Categoría #Shorts`. Siempre **sin prefijo** en el nombre. |

> No confundir con la carpeta `videos-largos/`: ahí viven unos **videos horizontales 16:9 de 8–12 min** (rutinas de
> estiramiento/flexibilidad armadas a partir de un video de YouTube). Es un tercer producto, aparte
> (`GENERAR_VIDEOS_LARGOS.md`, `videos-largos/README.md`, estado en `videos-largos/LISTA.md`). Cuando en este README o
> en los registros se dice «largo» sin más, es el `<slug>.mp4` que explica el ejercicio.

### Los tres grandes grupos de ejercicios

| Grupo | Qué es | Lista maestra | Cómo se hace | Estado (2026-11-23, según `CHECKLIST.md`) |
|---|---|---|---|---|
| **Normales** | Ejercicios de la app FitLesUY (CrossFit, movilidad, cardio…). | `ejercicios/ejercicios.csv` | `GENERAR_VIDEOS.md` | 339 fichas; **327 con largo renderizado** (auditoría 2026-11-23: ver §9 para los 12 que faltan, los cortos pendientes y desactualizados). Pueden aparecer nuevos. |
| **Máquinas** | Ejercicios de máquinas de gimnasio más usadas. Una fila por video. | `ejercicios/maquinas.csv` (`M1, M2…`) | `GENERAR_VIDEOS_MAQUINAS.md` | **36/36 completos.** |
| **Dataset** | Ejercicios de un proyecto externo público con miles de ejercicios, pasados a video. | `ejercicios/dataset.csv` (`D1, D2…`, lotes `Dxx`) | `GENERAR_VIDEOS_DATASET.md` (usa los dos anteriores según la columna `formato`) | **153/1227 (~12 %)**, sigue por `D153`. Hay props (implementos) sin dibujar que se listan en el CHECKLIST. |

Cada ejercicio es un **slug** (ej. `air-squat`, `barbell-bench-press`); es la clave que une todos los archivos y
registros. Una ficha JSON por ejercicio en `ejercicios/<slug>.json` es lo único que se escribe a mano; el resto se genera.

---

## 2. Quién hace qué (herramientas)

| Herramienta | Uso habitual |
|---|---|
| **OpenCode** | **Genera los videos** (largos y cortos, sobre todo del Dataset) con las herramientas locales, gratis en la PC del usuario. Los archivos salen con prefijo si se pide (`OC_`, `OC_2_`). |
| **Claude Code** | Genera algunos videos (siempre sobre las mismas herramientas locales) y, sobre todo, **sube a YouTube y TikTok** usando la extensión **Claude in Chrome** ya levantada, y registra todo. |
| **Claude Chat / Cowork / Hermes Agent / otras** | Consulta, planificación, revisión, tareas puntuales. Mismas reglas. |
| **HyperFrames** (`npx hyperframes …`) | Motor local que renderiza HTML a video. Skills `hyperframes*` en Claude Code. |

Todas deben poder arrancar leyendo solo este README y los documentos que enlaza. **Es normal y esperado** que, por
ejemplo, OpenCode esté generando videos del Dataset mientras Claude Code sube otros a YouTube: ver §7.

---

## 3. Flujo natural (no siempre lineal)

```
1. Largo ─► 2. Corto ─► 3. Alta en YouTube ─► 4. Programar/publicar en tandas ─► 5. Vincular corto↔largo ─► 6. Miniaturas pendientes
                                      └──► (con los ya publicados en YouTube) ─► 7. Alta en TikTok (en cualquier orden)
```

1. **Generar el largo** (`make-exercise.mjs <slug>`): ficha → voz → composición → check → render → miniatura + texto de YouTube.
2. **Generar el corto** (`make-exercise.mjs <slug> --corto`): se arma solo desde la ficha, sin voz.
3. **Subir a YouTube**, corto y largo. YouTube deja subir pocos videos por día, así que se **planifica varios días
   hacia adelante** y se programa en **tandas de 3–5 por día** (el último plan de largos: 5/día a las 08:00, 11:00,
   14:00, 17:00 y 20:00 hora de Uruguay; 23-11 → 10-12-2026).
4. **Vincular** corto↔largo en YouTube (link en la descripción + «Vídeo relacionado»). **Solo se referencia lo que
   ya está publicado**: Studio no ofrece como relacionado un video privado o programado. Por eso la vinculación queda
   «pendiente» y se completa más tarde, cuando el otro video pasa a público.
5. **Miniaturas**: la API de YouTube no deja la miniatura puesta en videos verticales (los toma como Shorts) y Studio
   limita las miniaturas personalizadas por día. Se sube primero el video y **las miniaturas se cargan en otra pasada**.
6. **TikTok**: solo se suben videos **que ya están en YouTube** (publicados o programados; primero YouTube, después TikTok), pero **el orden
   puede ser distinto**: el alta en TikTok no sigue el orden del alta en YouTube. A TikTok van **solo los largos
   (`<slug>.mp4`), nunca los `.corto`**, ~4 por día. **Borradores:** como subir por el flujo normal tarda más de 30 min por video, a veces se suben a TikTok **como borrador** (sin publicar ni programar) para adelantar el trámite; más adelante se programan. Se anotan en el «Registro de subidas» de `SUBIR-A-TIKTOK.md` con la nota «BORRADOR en TikTok» (el CHECKLIST los muestra como 📝 en la columna TikTok). Mientras sean borrador, el archivo **no** se mueve a `EnTikTok/`; se mueve al programarlos. Más borradores nuevos son esperables.

Las etapas se hacen en pasadas distintas y a ritmos distintos, así que **un video puede estar «subido» pero sin
miniatura, sin vincular o sin TikTok**. Por eso todo se registra (§5): el estado real está en los registros, no en la
memoria de la herramienta.

---

## 4. Mapa de carpetas y documentos

```
VidesoEjercicios/
├─ README.md                  ← este mapa
├─ CHECKLIST.md               ← estado de TODOS los ejercicios (autogenerado; no editar a mano)
├─ ejercicios/                ← listas maestras (*.csv) + una ficha <slug>.json por ejercicio
├─ videos/<slug>/             ← proyecto HyperFrames generado (no editar a mano); .pipeline.json = estado de ese video
├─ salida/                    ← resultados: <slug>.mp4, .corto.mp4, .miniatura.png, .youtube.txt, .tiktok.txt
│  └─ subidos/EnYoutube|EnTikTok  ← archivos ya publicados (EnTikTok/viejos = lotes anteriores)
├─ videos-largos/             ← el formato 16:9 de 8–12 min (fichas, fuentes, proyectos, salida, LISTA.md)
├─ plantilla/                 ← motor: runtime del personaje (runtime.js), scripts .mjs, voces, música, BITACORA.md
├─ imagenes/, LogoBanner/     ← recursos gráficos
└─ BKP/                       ← respaldos
```

### Documentos de «cómo hacer»

| Documento | Para qué |
|---|---|
| `GENERAR_VIDEOS.md` | **Orden de trabajo para generar videos** (parámetros `CANTIDAD`, `PREFIJO`, `EJERCICIOS`, `SOLO_FICHAS`). |
| `GENERAR_VIDEOS_MAQUINAS.md` | Complemento para máquinas (lotes, 90–150 s, escenas). |
| `GENERAR_VIDEOS_DATASET.md` | Complemento para el Dataset (`LOTE`, `PROPS`). |
| `GENERAR_VIDEOS_CORTOS.md` | Cómo se genera el corto y cuántas repeticiones lleva. |
| `GENERAR_VIDEOS_LARGOS.md` | Los videos 16:9 de 8–12 min desde un video de YouTube. |
| `plantilla/README.md` | Especificación técnica de fichas, poses, moves, overlays y comandos. |
| `plantilla/BITACORA.md` | **Problemas ya resueltos** al generar videos; leer antes de empezar uno. |
| `GUIA-PRONUNCIACION-VOZ.md` | Pronunciación de la voz TTS. |
| `SUBIR-A-YOUTUBE.md` | **Todo lo de YouTube**: skill de subida por API, flujo por Studio con Chrome, cortos, miniaturas (§6 septies), vinculación (§6 quinquies), cuotas y errores. |
| `SUBIR-A-TIKTOK.md` | Todo lo de TikTok: reglas, receta con Chrome, descripción, portada, registro de subidas. |

### Registros (estado y aprendizajes)

| Archivo | Qué registra | Quién lo escribe |
|---|---|---|
| `CHECKLIST.md` | Una fila por ejercicio con ficha, voz, render, YouTube, miniatura, subido, corto, corto subido, corto miniatura, corto vinculado. | **Se regenera**: `node plantilla/make-exercise.mjs --checklist` (también lo hacen los otros scripts). |
| `videos/<slug>/.pipeline.json` | Estado de generación de ese video (hash, fechas, prefijo del archivo, reps del corto). | Los scripts. |
| `cortos-subidos.csv` | Cortos publicados: slug, fecha, URL, lista, visibilidad, **miniatura (`si|no`)**. | `node plantilla/corto-subido.mjs` |
| `vinculos.csv` + `BITACORA-VINCULOS.md` | Por slug: ID del largo, ID del corto, si cada uno apunta al otro (`si|pendiente`), nota. | `node plantilla/vincular.mjs` (la bitácora se regenera sola). |
| `programacion-largos-subidos.csv`, `plan-programacion-largos.json` | Largos subidos y programados (fecha, hora, ID). | Claude Code al programar. |
| `CALENDARIO-YOUTUBE.md` | Calendario de publicación (fecha, hora, tema, video, ID, estado). | A mano/Claude al programar. |
| `PLAN-REVISION-YOUTUBE.md` | Pendientes de revisión en YouTube con su estado. | A mano/Claude. |
| `videos-youtube-para-app.csv` | Para cada ejercicio, URL del corto y del largo para cargar en la app FitLesUY. | Script que cruza `ejercicios.csv` + `cortos-subidos.csv` + `vinculos.csv` (hoy hay que regenerarlo a mano: el script original se perdió). |
| `SUBIR-A-TIKTOK.md` → «Registro de subidas» + `salida/subidos/plan-tiktok-*.json` | Qué se subió a TikTok, cuándo, y el plan por día. | Claude Code al subir. |
| `videos-largos/LISTA.md` | Estado de los videos 16:9. | `node plantilla/largo/make-largo.mjs --lista` |
| `ejercicios/completados.csv` | Datos que se completaron en la lista maestra (para que el dueño los importe en la app). | A mano/agente. |
| `plantilla/BITACORA.md` y las secciones de aprendizajes de `SUBIR-A-*.md` | **Limitaciones y trampas de cada herramienta**. | Quien las descubra: **documentarlas** ahí. |

---

## 5. Cómo registrar (regla de oro: registrá lo que hiciste, con el script, en el momento)

- **Usá los scripts, no edites a mano los CSV/CHECKLIST/bitácora.**
  - Subiste un corto: `node plantilla/corto-subido.mjs <slug> <videoId> --vis=publico|privado --mini=si|no`.
    Para cambiar solo un dato en un corto ya registrado (ej. cargaste la miniatura después):
    `node plantilla/corto-subido.mjs <slug> --vis=publico --mini=si`. **Pasá siempre `--vis`**: sin ella, la
    visibilidad se pisa con «privado».
  - Vinculaste: `node plantilla/vincular.mjs <slug> --largo=<ID> --corto=<ID> --largo-en-corto=si|pendiente --corto-en-largo=si|pendiente --nota="…"`.
    Consultar: `node plantilla/vincular.mjs <slug> --buscar`.
  - Con muchos en fila, poné `NOCHK=1` delante para no regenerar el CHECKLIST en cada uno y regeneralo al final sin esa variable.
- Al terminar una tanda, dejá una nota de **qué quedó pendiente y por dónde seguir** (en `SUBIR-A-*.md`, en el
  registro correspondiente o en la memoria de tu herramienta) y de **cualquier límite o trampa nueva**.
- Lo que no está registrado, no pasó: un compañero (otra herramienta) va a repetirlo o a pisarlo.

---

## 6. Restricciones conocidas de las plataformas

**YouTube**
- **Cuota de la API**: ~6 subidas/día por el skill `youtube-upload` (cada una ≈1600 de 10.000 unidades).
- **Límite diario de subidas en Studio**: ~87 cortos/día; aparece «Límite diario de subida alcanzado», se retoma a las ~24 h. No se esquiva.
- **Miniaturas**: tope diario de miniaturas personalizadas (hay que parar al ver «Límite de miniaturas personalizadas diarias superado»; se alcanzó con ~25). En videos verticales la API dice `✓ Miniatura` pero **no queda**: se carga en Studio. Por eso los cortos masivos se subieron **sin miniatura** y se completan después (`cortos-subidos.csv`, columna `miniatura`).
- **Vídeo relacionado**: solo ofrece videos **públicos** (a veces programados no aparecen). Largo programado → solo se puede hacer largo→corto; corto→largo queda `pendiente` hasta que el largo sea público.
- Siempre: «No, no está creado para niños», **Uso de IA = Sí**, lista «Videos cortos de ejercicios» para los cortos, y el bloque de la app FitLesUY en toda descripción (antes del aviso de salud ⚠️).
- Studio con la extensión: el navegador correcto es el **deviceId `a64d121a-d083-4bd7-bb7a-529d2c201274`**. A veces Studio se cuelga (los `screenshot` dan timeout): cerrar la pestaña y abrir otra. Trusted Types impide inyectar scripts; los campos de título/descripción son `contenteditable` y se llenan con `execCommand('insertText')`. Detalle en `SUBIR-A-YOUTUBE.md` §6 quater–septies.

**TikTok**
- Solo largos (`<slug>.mp4`), nunca `.corto`; ~4 por día (08:00, 13:30, 18:30, 21:00); archivo ≤ 10 MB para la subida con Chrome; portada propia generada desde la miniatura. Detalle en `SUBIR-A-TIKTOK.md`.

**Reglas fijas del proyecto**
- No cambiar música, estilo visual ni tamaño de los videos. Los cortos no llevan voz ni subtítulos.
- No renombrar a mano archivos de salida ni tocar `salida/subidos/`. **Los videos finales van sin prefijo** (`<slug>.mp4`): el 2026-11-23 se quitaron `OC_` y `OC_2_` de los 148 largos de normales/máquinas (queda el prefijo `O_D2_` en los del Dataset en curso). Si una herramienta renderiza con `PREFIJO`, que lo quite al terminar o no lo use.
- No hacer `git commit`/`git push` salvo que el dueño lo pida.
- **Avisar siempre antes** de acciones irreversibles hacia afuera (publicar, borrar en YouTube, enviar mensajes); el borrado de un video se muestra (título + ID + estado) antes de confirmarlo.
- Cuidado con rutas: en algunos documentos aparecen `C:\Users\nesto\…` y `…\DESARROLLOS\…` (typos); la real es `C:\DATOS\DESARROLLO\Hyperframes\VidesoEjercicios` y el usuario de Windows es `nestor`.

---

## 7. Trabajo en paralelo (varias herramientas a la vez)

Es lo esperado. Para no pisarse:

1. **Cada una trabaja sobre slugs distintos.** Antes de tomar un ejercicio mirá el `CHECKLIST.md`/`.pipeline.json`
   (¿ya tiene ficha o render?) y el registro de lo que vas a tocar (¿ya subido, vinculado, con miniatura?). Si te
   dieron una lista de slugs (`EJERCICIOS:`), respetala.
2. **Generar vs. subir no chocan**: generar escribe en `ejercicios/`, `videos/<slug>/` y `salida/`; subir escribe en
   los CSV de registro y mueve archivos a `salida/subidos/`. Si vas a subir un video que otra herramienta podría estar
   regenerando, verificá primero que su render esté terminado (`.pipeline.json`).
3. **Antes de escribir un registro, volvé a leerlo** (otro agente pudo cambiarlo) y escribí con los scripts, que
   actualizan solo la fila del slug. No reescribas un CSV entero.
4. **El CHECKLIST es derivado**: si dos herramientas lo regeneran a la vez no pasa nada grave (se recalcula de las
   fuentes); no lo edites a mano ni lo uses como fuente de verdad de la subida (la verdad está en los CSV).
5. **Un solo agente a la vez en Studio/TikTok con la misma cuenta** (la sesión del navegador es única y los topes
   diarios son compartidos): coordiná por mensaje con el dueño si hay duda.
6. **Los topes diarios son globales**: lo que sube una herramienta consume la cuota de todas.

---

## 8. Cómo empezar según la tarea

| Quiero… | Leé | Pedí algo así |
|---|---|---|
| Generar videos nuevos | `GENERAR_VIDEOS.md` (+ `_MAQUINAS` / `_DATASET`), `plantilla/README.md`, `plantilla/BITACORA.md` | `Seguí GENERAR_VIDEOS_DATASET.md. CANTIDAD: 5. PREFIJO: OC` |
| Generar solo los cortos | `GENERAR_VIDEOS_CORTOS.md` | `node plantilla/make-exercise.mjs <slug> --corto` |
| Subir a YouTube | `SUBIR-A-YOUTUBE.md` | «subí `<slug>` a YouTube» (primero `--dry-run`) |
| Poner miniaturas a cortos ya subidos | `SUBIR-A-YOUTUBE.md` §6 septies | `grep ";no$" cortos-subidos.csv` para ver los pendientes |
| Vincular corto ↔ largo | `SUBIR-A-YOUTUBE.md` §6 quinquies, `BITACORA-VINCULOS.md` | `node plantilla/vincular.mjs <slug> --buscar` |
| Subir a TikTok | `SUBIR-A-TIKTOK.md` | solo largos ya publicados en YouTube |
| Ver el estado general | `CHECKLIST.md`, `videos-largos/LISTA.md` | — |
| Agregar un ejercicio nuevo de la app | `plantilla/README.md` («Pasos para un ejercicio nuevo») | completar `ejercicios.csv` y seguir `GENERAR_VIDEOS.md` |

### Comandos útiles (desde la raíz)

```bash
node plantilla/make-exercise.mjs <slug> --info        # ver la fila de un ejercicio (busca en las tres listas)
node plantilla/make-exercise.mjs <slug>               # ficha → voz → composición → check → snapshots
node plantilla/make-exercise.mjs <slug> --render      # render final
node plantilla/make-exercise.mjs <slug> --corto       # video corto
node plantilla/make-exercise.mjs --checklist          # regenerar CHECKLIST.md
node plantilla/corto-youtube.mjs <slug>               # título/descripción/tags del corto
node plantilla/largo/make-largo.mjs --lista           # regenerar videos-largos/LISTA.md
```

---

## 9. Estado de un vistazo (2026-11-23) y pendientes principales

> Instantánea: los números reales salen de `CHECKLIST.md` y los CSV; actualizá esta sección al cerrar etapas grandes.

**Auditoría de archivos (2026-11-23, contra los `.mp4` reales con `ffprobe`: todos 1080×1920, con audio; largos 39–134 s, cortos 7,7–15,6 s):**

- **Normales — largos:** 327/339 renderizados. **Faltan 12** (tienen ficha pero no hay largo válido): `supinated-band-pull-apart`, `alternating-heel-touches`, `90-90-hip-internal-rotation-lift-off` (solo existe un render viejo de ~6,8 s, no sirve), y `wall-shoulder-external-rotation`, `alternating-spiderman-stretch`, `shoulder-press`, `single-leg-v-up`, `snatch`, `snatch-with-pause-at-knee`, `split-squat-calf-raise`, `dumbbell-front-rack-lunge`, `nordic-hamstring-curl` (nunca se renderizó el largo; su corto sí está subido). Además `descanso`: largo desactualizado respecto de la ficha (render del 16-10).
- **Normales — cortos:** 328 existen. **Faltan 11** (los ejercicios 328–338, que sí tienen largo): `open-the-gate`, `candlestick-to-straddle-stretch`, `barbell-cluster`, `thoracic-wall-sweep`, `clean-drop-drill`, `leg-swing`, `kneeling-weighted-shoulder-car`, `dumbbell-around-the-world`, `banded-pull-up`, `dumbbell-standing-calf-raise`, `plank-hip-dips`. **25 cortos «desactualizados»**: el corto es del 5-11 y el largo se volvió a renderizar el 6–7-11 con cambios en la ficha; esos cortos **ya están publicados** en YouTube con la versión anterior.
- **Máquinas:** 36/36 largos y 36/36 cortos, sin diferencias.
- **Dataset:** 153/1227 renderizados (próximo `D153`).
- **Duplicados (resueltos 2026-11-23):** de los 12 dobles renders se quedó el `OC_2_` (voz con el nombre en inglés) **renombrado sin prefijo** (`<slug>.mp4`, y el `archivo` de su `.pipeline.json`); las copias viejas (`OC_`, `EnTikTok/viejos/`) están en `salida/repetidos/REPETIDO_*`. 10 quedaron **desmarcados para subir otra vez** (volvieron a `salida/`; marcados «↻ RE-SUBIR» en `SUBIR-A-TIKTOK.md`): `general-stretching`, `rowing`, `air-squat`, `kettlebell-windmill`, `weighted-side-plank`, `clamshell-hold`, `core-overhead-hold-with-side-bend`, `half-kneeling-ankle-dorsiflexion-stretch`, `half-kneeling-windmill-rotation-and-side-bend`, `overhead-squat`. Sus versiones anteriores siguen publicadas en YouTube/TikTok (hay que reemplazarlas o borrarlas a mano). `barbell-bicep-curl` era una copia idéntica (la sobrante pasó a `repetidos/`). `barbell-hang-power-snatch` sigue con dos versiones: pendiente de decidir.
- **Dónde está cada largo:** `salida/` (raíz) = generado, aún no movido; **los largos programados en YouTube siguen en la raíz hasta publicarse** (por eso «Subido» del CHECKLIST no equivale a «está en YouTube»); `subidos/EnYoutube/` = ya en YouTube (solo largos de máquinas/viejos y todos los cortos: 354); `subidos/EnTikTok/` = ya en YouTube **y** TikTok (129 largos). Los 30 borradores de TikTok del plan 12-2026 y 87 videos «Plan 4/día (sin subir)» **no se movieron** de la raíz.
- **Cortos en YouTube:** 354 en `cortos-subidos.csv` = 354 archivos en `subidos/EnYoutube/`. ~221 sin miniatura (se cargan por tandas).
- **Largos en YouTube (verificado en Studio el 2026-11-23):** los 192 IDs de largo registrados existen: 106 públicos y 85 programados (hasta el 10-12-2026, 5/día; hoy salieron 08:00, 11:00 y 14:00, faltan 17:00 y 20:00). `CALENDARIO-YOUTUBE.md` quedó con 95 «publicado» y 85 «programado». Las 36 máquinas tienen ID de largo; 33 son públicas (archivos en `subidos/EnYoutube/`) y 3 están programadas (`rowing-machine` 28-11, `stair-climber` 2-12, `smith-machine-bench-press` 6-12; archivos en la raíz). Un largo programado en YouTube cuya versión ya subió a TikTok está en `subidos/EnTikTok/` (45 casos).
- **Vinculación:** 354 filas en `vinculos.csv` (una por corto subido); 115 con corto→largo y 147 con largo→corto. Con el largo ya público no queda ningún enlace pendiente; 82 tienen el largo programado (solo largo→corto) y 157 todavía no tienen largo conocido.
- **TikTok:** ~124 programados/publicados, 25 borradores (📝), 10 para re-subir (↻) y 87 en plan sin subir; ver `SUBIR-A-TIKTOK.md`. Más borradores se sumarán.
- **Pendientes sueltos:** `alternating-spiderman-stretch` y `wall-shoulder-external-rotation` no tienen archivo de miniatura; `videos-youtube-para-app.csv` hay que regenerarlo.
