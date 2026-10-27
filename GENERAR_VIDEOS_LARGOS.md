# GENERAR_VIDEOS_LARGOS — videos largos 16:9 a partir de un video de YouTube

> **Para el modelo / agente que lee esto:** orden de trabajo completa para convertir un video de YouTube (rutina,
> clase, explicación de un ejercicio) en un **video largo animado 16:9** con nuestro personaje, la voz de Daniela y
> consejos de técnica propios. Seguilo en orden. Leé también `plantilla/README.md` (poses, moves, overlays: **es la
> misma especificación**) y `plantilla/BITACORA.md`. Primer video hecho así: `estiramientos-flexibilidad` (2026-10-25).

## Cómo usarlo (para el usuario)

```
Seguí GENERAR_VIDEOS_LARGOS.md con este video: https://www.youtube.com/watch?v=XXXX
```

Opcional: `SLUG: <nombre-corto>`, `DURACIÓN: ~8 min`, `SOLO_FICHA: sí` (todo menos el render).

---

## 1. Qué es y dónde queda cada cosa

- Video **horizontal 1920×1080**, 8–12 min, dividido en **capítulos** (uno por ejercicio o lado). Español
  rioplatense con voseo. Columna izquierda = textos; derecha = el personaje (`plantilla/runtime.js`, el mismo de los
  shorts); abajo = subtítulo y barra de progreso con una marca por capítulo.
- Piezas propias del formato largo: **encabezado de capítulo** ("EJERCICIO 3 DE 14"), **cuenta regresiva** de las
  esperas (anillo + segundos), **tarjeta CONSEJO**, **tarjetas "vista de frente / de arriba"** para lo que no se ve de
  perfil, y **capítulos de YouTube** calculados solos.
- No reemplaza al pipeline de shorts: es un builder aparte que reutiliza el personaje, la voz y la música.

```
videos-largos/
  fichas/<slug>.json        ficha del video (lo único que se escribe a mano)
  fuentes/<slug>/           análisis del original: transcripcion.txt, info.json, analisis.md
    _frames/                hojas de fotogramas + video bajado (NO van a git)
  proyectos/<slug>/         proyecto HyperFrames generado (index.html se regenera siempre)
  proyectos/_poselab/<slug>/ laboratorio de poses
  salida/<slug>.mp4         video final (no va a git)
  salida/<slug>.miniatura.png  miniatura 1280×720
  salida/<slug>.youtube.txt    título + descripción con capítulos + tags
  LISTA.md                  estado de todos los videos largos (autogenerado)
plantilla/largo/
  fuente.mjs                baja subtítulos + fotogramas del video original
  make-largo.mjs            voz → composición → check → snapshots → miniatura → youtube.txt → render
  build-largo.mjs           arma index.html (1920×1080) desde la ficha
  largo-runtime.js          capítulos, cuenta regresiva y tarjetas (se suma al timeline del personaje)
  styles-largo.css          layout 16:9 (preset Coral, igual que los shorts)
```

## 2. Reglas fijas

1. **Nunca se usa audio ni imagen del original.** El video bajado es solo para mirar las posturas. Se replica la
   secuencia de ejercicios; el guion se escribe de cero, con nuestras palabras, y se le suman consejos propios.
2. Idioma: rioplatense con voseo en voz, textos y descripción. **Sin adjetivos con género** referidos a quien mira
   ("quedate del lado de…", no "quedate inclinada").
3. Voz Daniela (Piper), música `plantilla/musica/bgm-base.wav` en loop a 0,12. No cambiar voz ni estilo visual.
4. No editar `proyectos/<slug>/index.html` ni `LISTA.md` a mano. Los cambios van en la ficha.
5. Ficha nueva con `"revisado": false`. Solo el usuario aprueba. No hacer commit salvo pedido.
6. Un video no está terminado sin: ficha + voz + check + render + miniatura + youtube.txt.
7. Cambios en `plantilla/largo/` → documentarlos acá y una fila en `plantilla/BITACORA.md`.

## 3. Procedimiento

### 3.1 Bajar y analizar el original

```bash
node plantilla/largo/fuente.mjs <slug> "<url>"          # --en si el video está en inglés, --cada=3 para más fotogramas
```

Deja `fuentes/<slug>/transcripcion.txt` (con minuto:segundo) e `info.json`, y hojas de fotogramas en `_frames/`
(cada 5 s, el tiempo impreso en cada cuadro). **Mirá todas las hojas** y leé la transcripción. Después escribí
`fuentes/<slug>/analisis.md` con una tabla: tiempo del original → ejercicio → qué dice la persona → cómo lo
mostramos (pose de perfil, tarjeta de frente) → consejos que sumamos. Ver `fuentes/estiramientos-flexibilidad/analisis.md`.

Preguntate para cada ejercicio: **¿se ve de perfil?** Flexión hacia adelante, estocadas, cuadrupedia, perro, paloma,
cobra: sí. Inclinaciones laterales, aperturas de rodillas, balanceos y torsiones: no → **tarjeta** (§4.4).

### 3.2 Poses

Escribí la ficha con `poses` y probalas antes de escribir escenas:

```bash
node plantilla/largo/make-largo.mjs <slug> --poses            # todas
node plantilla/largo/make-largo.mjs <slug> --poses A,B        # algunas
```

→ `videos-largos/proyectos/_poselab/<slug>/snapshots/contact-sheet-N.jpg`. Copiá poses probadas de
`videos-largos/fichas/*.json` y de `ejercicios/*.json` (tabla de poses de `GENERAR_VIDEOS.md` §6.3). Las coordenadas
del rig son las mismas que en los shorts; el encuadre por defecto es `rig { x: 1400, y: 838, scale: 0.95 }`
(piso en y ≈ 870). **Centrá cada pose alrededor de x ≈ 0** del rig: el escenario va de x ≈ 880 a 1880 en pantalla
(rig −540 … +500). Ej.: el perro boca abajo de `yoga-push-up` va corrido 330 px (`rx -330`, manos `hx 345`).

Tip: armá la ficha con un script Python (lee `plantilla/youtube-deslinde.txt` y hace `json.dump(..., ensure_ascii=False, indent=2)`).

### 3.3 Escenas, consejos, miniatura y YouTube → §4

### 3.4 Generar y revisar

```bash
node plantilla/largo/make-largo.mjs <slug>
```

Genera la voz (solo lo que cambió), `index.html`, `capitulos.json`, `salida/<slug>.youtube.txt`, corre
`hyperframes check`, saca un cuadro por escena (`proyectos/<slug>/snapshots/contact-sheet-N.jpg`, 9 por hoja) y la
miniatura. ~6–8 min. Revisá todas las hojas: textos que se pisan, labels sobre el cuerpo, tarjetas que no se entienden.

### 3.5 Renderizar

```bash
node plantilla/largo/make-largo.mjs <slug> --render --no-snapshot
```

→ `videos-largos/salida/<slug>.mp4`. Correlo en segundo plano: el render de 10 min tarda bastante más que un short.
Al terminar, mirá algunos cuadros del mp4 (`ffmpeg -ss <s> -i salida/<slug>.mp4 -frames:v 1 x.png`) y la duración en `LISTA.md`.

Otros: `--miniatura` (solo la miniatura), `--youtube` (solo el .txt), `--force-tts`, `--no-check`,
`node plantilla/largo/make-largo.mjs --lista` (regenera `LISTA.md`).

## 4. La ficha (`videos-largos/fichas/<slug>.json`)

```jsonc
{
  "slug": "estiramientos-flexibilidad",
  "name": "Estiramientos para ganar flexibilidad",       // barra superior
  "category": "RUTINA GUIADA · ESTIRAMIENTOS",            // barra superior (derecha)
  "tags": ["Cadera", "Piernas", "Espalda"],               // chips de la portada (escena con "tags": true)
  "fuente": { "url", "canal", "titulo", "duracion", "nota" },   // de dónde sale (no se exporta a YouTube)
  "revisado": false, "notas": "",
  "voiceSpeed": 1.0, "pronuncia": { },                    // igual que en los shorts
  "music": true, "musicVolume": 0.12,
  "rig": { "x": 1400, "y": 838, "scale": 0.95 },
  "initialPose": "CROSS", "props": [], "poses": { },
  "capitulos": [ … ],
  "miniatura": { … },
  "youtube": { "titulo", "descripcion", "tags" }
}
```

### 4.1 Capítulos

```jsonc
{ "titulo": "Mariposa (aductores)",     // capítulo de YouTube (descripción) — corto y buscable
  "head": ["MARIPOSA", "ADUCTORES"],    // encabezado Bebas: 2 líneas, ≤ 12 caracteres c/u (la 2.ª en coral)
  "badge": "…",                         // opcional; por defecto "EJERCICIO n DE N"
  "numero": false,                      // intro y cierre: no cuentan como ejercicio
  "hero": true,                         // solo la intro: encabezado más grande
  "escenas": [ … ] }
```

Estructura que funcionó (16 capítulos, 43 escenas, 10:01):
- **Intro** (`numero: false`, `hero: true`): qué es + para qué (`"tags": true`), y "Antes de empezar" con `keys`
  (reglas generales: material, tensión sí / dolor no, no rebotar, respirar).
- **Un capítulo por ejercicio y por lado** cuando cada lado tiene su espera (los capítulos de YouTube quedan útiles).
  Si los dos lados son cortos, un solo capítulo con dos escenas con `hold`.
- Cada capítulo: 1. **POSICIÓN** (cómo entrar) → 2. **el movimiento** (dinámico, con `seq … until: "end"`) →
  3. **ASÍ NO** cuando hay un error típico (pose `_BAD` + label) → 4. **AGUANTÁ** con `tip` y `hold`.
- **Cierre** (`numero: false`): vuelta a la calma + `keys` de cuándo hacer la rutina.

### 4.2 Escenas

| Campo | Uso |
|---|---|
| `vo` | voz + subtítulo. **≤ ~170 caracteres** (2 líneas de subtítulo en 16:9). Voseo |
| `step` | etiqueta del paso ("POSICIÓN", "AGUANTÁ", "PIERNA DERECHA") — mayúsculas, corta |
| `sub` | bajada coral (≤ ~32 caracteres) |
| `tip` | tarjeta **CONSEJO** (≤ ~120 caracteres). El consejo es nuestro: postura, alternativa más fácil, error común |
| `keys` | lista con ticks (`{ "text", "cue" }`: aparece cuando la voz dice la palabra `cue`, sin tildes) |
| `tags: true` | chips de `spec.tags` (solo la portada) |
| `hold` | segundos de espera con cuenta regresiva. Arranca cuando termina la voz (o en `holdAt`). `holdLabel` (default "AGUANTÁ") |
| `min` | duración mínima. Real = máx(`min`, voz + 1 s, última acción + 0,45 s, fin del hold + 0,7 s) |
| `moves` | igual que en los shorts (`to`, `cut`, `seq`, `loop`, `grip`). Extra: `{ "to": "X", "hold": true }` = arranca con la espera y dura 60 % de ella (bajar un poco más mientras aguanta) |
| `overlays` | igual que en los shorts, en px del lienzo **1920×1080**. Labels: zona libre arriba a la derecha (≈ x 1500–1700, y 520–620) o a la izquierda del cuerpo (x ≤ 1060, `anchor: "end"`) |
| `card` | tarjeta "vista de frente / de arriba" (§4.4) |

Zonas: columna de texto x 80–840 (encabezado y 96–400, escena y 404–870); cuenta regresiva x 870–1080, y 96–346;
tarjeta x 1500–1840, y 96–496; subtítulo y 906–1046. Nada de texto con y > 880.

### 4.3 Voz y ritmo

- Seguí el orden y las indicaciones del original, pero **reescritas** y más claras; sumá lo que falta (por qué, qué se
  siente, cómo hacerlo más fácil o más intenso).
- Esperas: 15–20 s por lado alcanzan para un video de YouTube (el original suele tener 30 s+). La cuenta regresiva
  reemplaza al "cuatro, tres, dos, uno" hablado.
- Escribí números con letras en la voz ("veinte segundos", "cuatro apoyos"): Daniela lee mejor.

### 4.4 Tarjetas (`card`)

`{ "tipo", "lado": 1 | -1, "label", "desde": v0, "anim": [[v, at, dur], …], "vaiven": { "de", "a", "dur", "at" } }`.
El valor `v` mueve la figura; `at` puede ser `"hold"` (inicio de la espera). Escenas seguidas con la misma tarjeta
(tipo + lado + label) comparten un clip y la animación sigue sin cortes. `lado: -1` la espeja (otra pierna).

| tipo | vista | v |
|---|---|---|
| `mariposa` | de frente, sentado plantas juntas | 0 rodillas arriba → 1 rodillas al piso |
| `lateral` | de frente, una pierna estirada al costado y la otra flexionada | −1 inclinado hacia la pierna estirada (brazo por arriba) · 0 derecho · 1 hacia el otro lado |
| `balanceo` | de frente, piernas y brazos cruzados | −1 … 1 el tronco se balancea |
| `torsion` | de arriba, piernas cruzadas | 1 gira a la derecha (mano a la rodilla) · −1 a la izquierda |
| `pancake` | de frente, de pie con las piernas bien abiertas | 0 tronco arriba (manos en los muslos) → 1 plegado, manos al piso entre los pies |

Para una tarjeta nueva: agregar el dibujo en `BUILD` de `plantilla/largo/largo-runtime.js` (función que recibe el
grupo SVG `viewBox 0 0 300 330`, piso en y 302, y devuelve `draw(v)`) y documentarla en esta tabla.

### 4.5 Miniatura (`miniatura`)

`{ "pose", "grip", "badge", "head": ["GANÁ", "FLEXIBILIDAD"], "chip": "10 MIN EN EL PISO", "size": 170, "zoom": 1.3, "dx": 0, "dy": 40 }`
→ título enorme a la izquierda + personaje agrandado en la pose más reconocible. Sale 1280×720.
Revisala en chico: que el título se lea y el personaje no se corte.

### 4.6 YouTube (`youtube`)

- `titulo` ≤ 100 caracteres: `<Qué> para <beneficio> 🧘 Rutina guiada de <N> min …`.
- `descripcion`: misma estructura y tono que los shorts (`GENERAR_VIDEOS.md` §6.8) más una sección
  `⏱️ CAPÍTULOS` con el marcador **`{{CAPITULOS}}`** (se reemplaza por `0:00 Intro…` con los tiempos reales), lista
  `📋 QUÉ VAS A HACER`, deslinde de `plantilla/youtube-deslinde.txt` tal cual y la **última línea con hashtags**
  (el crédito de la voz se inserta solo antes). ≤ 5000 caracteres, sin `<` ni `>`.
- `tags`: 10–15 búsquedas en castellano.
- Subida → §4.7.

### 4.7 Subir a YouTube

Mismo skill que los shorts (`SUBIR-A-YOUTUBE.md`), con estas diferencias:

1. **Antes:** `"revisado": true` en la ficha (lo aprueba el usuario) y `--lista`.
2. **Carpeta:** `videos-largos/salida` (no `salida/`). Siempre `--dry-run` primero:
   ```powershell
   & $PY $SK --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\videos-largos\salida" --privacy private --dry-run
   & $PY $SK --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\videos-largos\salida" --privacy private
   ```
3. **Miniatura por la API (sin `--no-thumbnail`):** en 16:9 YouTube no lo toma como Short y la miniatura **sí queda**
   (comprobado 2026-10-26 con los dos primeros). Igual mirala en Studio (`/video/<ID>/edit`, panel izquierdo) y si no
   está, cargala como en `SUBIR-A-YOUTUBE.md` §6 bis.
4. **Público:** en Studio, *Visibilidad* → Público → Hecho → Guardar (o programar, si va al calendario). Después cambiar
   `private` → `public` en `uploads_log.csv` del skill.
5. **`--lista`** otra vez: el uploader mueve mp4 + miniatura + txt a `videos-largos/salida/subidos/`; la LISTA los busca
   ahí también (y en `subidos/EnYoutube/`, donde se archivan a mano) y la columna *YouTube* pasa a mostrar el link con el estado del log.
6. Si hay que re-renderizar uno ya subido, el mp4 nuevo sale en `videos-largos/salida/`: borrá o mové el viejo de
   `subidos/` para no tener dos.

Otras diferencias: ≤ 15 min no necesita canal verificado (más largo sí); cada video pesa 60–70 MB y tarda ~1 min en
subir; los capítulos de la descripción (`0:00 …`, ≥ 3, de ≥ 10 s) los toma YouTube solos al procesar.

## 5. Problemas conocidos

| Síntoma | Solución |
|---|---|
| El título de la intro pisa la etiqueta del paso | `hero` a 124 px; título de 2 líneas cortas |
| Label de overlay sobre la cara | posición absoluta a un costado (ver §4.2), no `{ j, dy }` grande |
| `yt-dlp` falla con 429 en subtítulos en inglés | `fuente.mjs` baja solo `es.*` (o `en.*` con `--en`) y sigue aunque falle |
| Movimiento lateral / torsión no se entiende de perfil | tarjeta (§4.4); el personaje hace un gesto chico (ej. `b ±6`) para que no quede quieto |
| Pierna cruzada (figura 4) | pierna cercana con `s/t` a mano + `ll 0.6` (escorzo) y la lejana con `s2/t2` del IK; ver `FIG4_*` |
| De pie se corta la cabeza arriba (con el rig por defecto) | no usar poses de pie derechas: entrar a las posturas de pie desde el piso o ya inclinado (`PIKE_HALF`, `WIDE_UP` en `flexibilidad-cuerpo-completo`) |
| Acostado con los brazos estirados atrás, las manos entran en la columna de texto | cerrar sentado (`CROSS` / `ARMS_UP`) o con `ua` corto |
| Video original sin voz ("No Talking") | `fuente.mjs` avisa que no hay subtítulos: el nombre del ejercicio está en pantalla en las hojas; el guion es todo propio |
