# Subir videos a YouTube — machete

Resumen práctico del skill `youtube-upload`. La guía completa (configuración de Google Cloud, auditoría y errores) está en
`C:\Users\nesto\.claude\skills\youtube-upload\README.md`.

> También podés pedírselo a Claude: *"subí arm-circles a YouTube"*. Claude corre el `--dry-run`, te muestra los datos y sube cuando confirmes.

---

## 0. Preparar la terminal (PowerShell)

Pegá esto una vez por sesión de terminal para no escribir las rutas largas cada vez:

```powershell
$PY  = "C:\Users\nesto\.claude\skills\youtube-upload\.venv\Scripts\python.exe"
$SK  = "C:\Users\nesto\.claude\skills\youtube-upload\upload.py"
$OUT = "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\salida"
```

Todos los ejemplos de abajo usan `& $PY $SK ...`.

---

## 1. Qué tiene que haber en la carpeta

Por cada video, con el **mismo nombre base**:

| Archivo | ¿Obligatorio? | Para qué |
|---|---|---|
| `arm-circles.mp4` | Sí | El video. |
| `arm-circles.youtube.txt` (o `.txt`) | Sí | Título, descripción y tags. Sin este archivo el video **no se sube**. |
| `arm-circles.miniatura.png` (o `.png`, `.jpg`, `.miniatura.jpg`) | No | Miniatura. Pesa 2 MB como máximo, y el canal tiene que estar verificado por teléfono. |

El `.youtube.txt` que arma el pipeline ya trae las secciones `TÍTULO` / `DESCRIPCIÓN` / `TAGS`. Si el txt es texto plano, todo se usa como descripción y el título sale del nombre del archivo.

---

## 2. Subir UN video

```powershell
# 1) Probar (no sube nada, muestra título, canal y avisos)
& $PY $SK --channel fitlesuy "$OUT\arm-circles.mp4" --dry-run

# 2) Subir de verdad
& $PY $SK --channel fitlesuy "$OUT\arm-circles.mp4"
```

> **Después de subir un video largo (Daniela): vincularlo con su corto** (§ 6 quinquies): link en la descripción + *Vídeo relacionado*, y registrar en `BITACORA-VINCULOS.md`. Si el corto todavía no está subido, queda «pendiente» y se completa cuando se suba el corto.

## 3. Subir una CARPETA entera

Toma todos los `.mp4` de la carpeta. Las subcarpetas no entran, así que `subidos/` queda afuera.

```powershell
& $PY $SK --channel fitlesuy $OUT --dry-run
& $PY $SK --channel fitlesuy $OUT
```

> **Cuota:** alcanza para unos **6 videos por día** (10.000 unidades, y cada subida usa unas 1600). Si se acaba, el script frena y lista los pendientes. Al otro día corrés el mismo comando y saltea los que ya subió.

---

## 4. Parámetros

| Parámetro | Qué hace | Por defecto |
|---|---|---|
| `<ruta>` | Un `.mp4` o una carpeta. | — |
| `--channel <alias>` | Canal destino: `cripto`, `fitlesuy` o `kia`. | — (obligatorio para subir) |
| `--dry-run` | Muestra lo que subiría, **sin subir**. Usalo siempre primero. | apagado |
| `--privacy private\|unlisted\|public` | Visibilidad del video. | `public` |
| `--thumbnail <imagen>` | Fuerza una miniatura puntual. Solo sirve si subís **un** video. | busca `<video>.miniatura.png` |
| `--no-thumbnail` | No manda la miniatura por la API, porque igual no queda. Se carga en Studio (ver 6 bis). El archivo se mueve igual. | apagado |
| `--category <id>` | Categoría de YouTube (27 = Educación, 17 = Deportes, 15 = Mascotas, 22 = Personas y blogs). | la del canal (fitlesuy = 17) |
| `--force` | Sube aunque el video ya figure en `uploads_log.csv`. Sirve para resubir. | apagado |
| `--no-move` | No mueve los archivos a `subidos/` después de subir. | los mueve |
| `--channels` | Lista los canales configurados. | — |
| `--auth <alias>` | Autoriza o re-autoriza un canal. Abre el navegador. | — |

---

## 5. Ejemplos útiles

```powershell
# Ver qué canales hay y cuál está autorizado
& $PY $SK --channels

# Subir como "no listado" para revisarlo antes de hacerlo público
& $PY $SK --channel fitlesuy "$OUT\air-squat.mp4" --privacy unlisted

# Subir privado
& $PY $SK --channel fitlesuy "$OUT\air-squat.mp4" --privacy private

# Usar otra miniatura
& $PY $SK --channel fitlesuy "$OUT\arm-circles.mp4" --thumbnail "C:\ruta\otra-miniatura.png"

# Resubir un video que ya está en el log (por ejemplo, después de corregirlo)
& $PY $SK --channel fitlesuy "$OUT\subidos\arm-circles.mp4" --force

# Subir y dejar los archivos donde están
& $PY $SK --channel fitlesuy "$OUT\arm-circles.mp4" --no-move

# Probar toda la carpeta como no listados
& $PY $SK --channel fitlesuy $OUT --privacy unlisted --dry-run
```

### Los mismos ejemplos, con las rutas completas (sin variables)

Sirven para copiar y pegar directo en PowerShell, sin preparar nada antes:

```powershell
# Ver qué canales hay y cuál está autorizado
& "C:\Users\nesto\.claude\skills\youtube-upload\.venv\Scripts\python.exe" "C:\Users\nesto\.claude\skills\youtube-upload\upload.py" --channels

# Subir como "no listado" para revisarlo antes de hacerlo público
& "C:\Users\nesto\.claude\skills\youtube-upload\.venv\Scripts\python.exe" "C:\Users\nesto\.claude\skills\youtube-upload\upload.py" --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\salida\air-squat.mp4" --privacy unlisted

# Subir privado
& "C:\Users\nesto\.claude\skills\youtube-upload\.venv\Scripts\python.exe" "C:\Users\nesto\.claude\skills\youtube-upload\upload.py" --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\salida\air-squat.mp4" --privacy private

# Usar otra miniatura
& "C:\Users\nesto\.claude\skills\youtube-upload\.venv\Scripts\python.exe" "C:\Users\nesto\.claude\skills\youtube-upload\upload.py" --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\salida\arm-circles.mp4" --thumbnail "C:\ruta\otra-miniatura.png"

# Resubir un video que ya está en el log (por ejemplo, después de corregirlo)
& "C:\Users\nesto\.claude\skills\youtube-upload\.venv\Scripts\python.exe" "C:\Users\nesto\.claude\skills\youtube-upload\upload.py" --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\salida\subidos\arm-circles.mp4" --force

# Subir y dejar los archivos donde están
& "C:\Users\nesto\.claude\skills\youtube-upload\.venv\Scripts\python.exe" "C:\Users\nesto\.claude\skills\youtube-upload\upload.py" --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\salida\arm-circles.mp4" --no-move

# Probar toda la carpeta como no listados
& "C:\Users\nesto\.claude\skills\youtube-upload\.venv\Scripts\python.exe" "C:\Users\nesto\.claude\skills\youtube-upload\upload.py" --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\salida" --privacy unlisted --dry-run
```

---

## 6. Qué pasa después de subir

- Imprime el link `https://youtu.be/<ID>`.
- Lo anota en `C:\Users\nesto\.claude\skills\youtube-upload\uploads_log.csv`.
- Mueve el `.mp4`, el `.txt` y la miniatura a `salida\subidos\`, salvo que uses `--no-move`.
- Siempre marca el video como "no es para niños".
- **Falta un paso: vincular con el corto** (§ 6 quinquies), tanto en videos de `salida` como en los largos 16:9 (6 ter).

---

## 6 bis. Flujo recomendado: privado → miniatura en Studio → público

La miniatura **no queda puesta por la API**: el script dice `✓ Miniatura`, pero en Studio el recuadro sigue vacío. Pasa sobre todo con videos verticales (YouTube los toma como Shorts). Por eso conviene hacerlo así (comprobado con `lat-pulldown` el 2026-10-22 → <https://youtu.be/M1nW1T1S_Ks>):

1. **Subir privado y sin miniatura:**
   ```powershell
   & $PY $SK --channel fitlesuy "$OUT\lat-pulldown.mp4" --privacy private --no-thumbnail
   ```
   La miniatura igual se mueve a `salida\subidos\`.
2. **Abrir el video en Studio:** `https://studio.youtube.com/video/<ID>/edit`. No hace falta esperar a que termine de procesar.
3. **Miniatura:** en *Detalles* → *Miniatura* → **Subir archivo** → elegir `salida\subidos\<video>.miniatura.png` → **Guardar**. Se tiene que ver en el panel de la izquierda.
4. **Visibilidad:** en el panel derecho, *Visibilidad* → **Público** → **Hecho** → **Guardar**. Queda bien cuando dice *Público* y el botón Guardar queda gris.
5. En `uploads_log.csv`, cambiar el estado de esa fila de `private` a `public`.

> Probado también con `multi-hip-machine` y `multi-press-machine` (2026-10-22): con `--no-thumbnail` y la miniatura
> cargada en Studio, las dos quedaron bien. Para varios videos, subí todos en privado primero y después hacé los pasos
> 2 a 4 de cada uno en la misma pestaña. Si el menú de *Visibilidad* no se abre al primer clic (pasa justo después de
> guardar la miniatura), volvé a hacer clic.

> Pedíselo a Claude así: *"subí lat-pulldown privado, ponele la miniatura con Chrome y pasalo a público"*. Claude hace los pasos 2 a 4 con la extensión Claude in Chrome. Para cargar el archivo usa `file_upload` sobre el input oculto `#file-loader`, sin hacer clic en el botón, porque así no se abre el selector de Windows.

## 6 ter. Videos largos (16:9)

Están en `videos-largos\salida` (no en `salida`) y la miniatura **sí queda puesta por la API** (no van como Shorts), así
que no hace falta `--no-thumbnail`. Probado el 2026-10-26 con `estiramientos-flexibilidad` (<https://youtu.be/wpKXHIQ3hCM>)
y `flexibilidad-cuerpo-completo` (<https://youtu.be/KlVTaJ-CIho>).

```powershell
& $PY $SK --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\videos-largos\salida" --privacy private --dry-run
& $PY $SK --channel fitlesuy "C:\DATOS\DESARROLLOS\Hyperframes\VidesoEjercicios\videos-largos\salida" --privacy private
```

Después: mirar la miniatura en Studio, pasar a **Público** (pasos 4 y 5 de 6 bis) y correr
`node plantilla/largo/make-largo.mjs --lista`. Detalle completo en `GENERAR_VIDEOS_LARGOS.md` §4.7.

> Si `--auth` abre otro navegador (Brave) en vez de Chrome: antes de correrlo, en la misma terminal,
> `$env:BROWSER = '"C:/Program Files/Google/Chrome/Application/chrome.exe" %s'`.

---

## 6 quater. Videos cortos (`<slug>.corto.mp4`) — por YouTube Studio con Chrome

Los cortos (ver `GENERAR_VIDEOS_CORTOS.md`) se suben **por grupos que pide el profe** (5, 10…), **sin el skill `youtube-upload`**: Claude los sube desde YouTube Studio con la extensión Claude in Chrome (sin API ni cuota). Probado el 2026-11-05 con `air-squat` (<https://youtu.be/qi2uWme2JYY>).

**Reglas fijas**

- Canal **FitLesUY**. Cada corto va a la lista de reproducción **«Videos cortos de ejercicios»** (ya existe; en Studio es `PLaxjIdaCJSz8`).
- Archivos (todos con el nombre del slug, sin prefijo):
  - `salida/<slug>.corto.mp4` — el video.
  - `salida/<slug>.corto.youtube.txt` — título, descripción y tags. Se generan con `node plantilla/corto-youtube.mjs <slug> …` (o `--todos`; ya están los 364).
  - Miniatura: **la misma del largo**, `<slug>.miniatura.png` (en `salida/` o en `salida/subidos/EnYoutube/`). No se mueve (es del largo).
- Título: `<Nombre> 🎬 Así se hace en segundos | <Categoría> #Shorts`.
- Visibilidad: se sube **privado**; pasa a público solo cuando el profe lo confirma.
- Siempre «No, no está creado para niños».

**Pasos por cada video (Claude los hace)**

1. Elegir el navegador (`select_browser`), abrir `https://studio.youtube.com` → **Crear → Subir vídeos**.
2. `file_upload` del `.corto.mp4` sobre el input de archivo (no se hace clic en «Seleccionar archivos»).
3. Título y descripción con JavaScript (los textbox son `contenteditable`; `form_input` no sirve):
   `#title-textarea #textbox` y `#description-textarea #textbox` → `focus()`, `execCommand('selectAll')`, `execCommand('insertText', false, texto)`.
4. Miniatura: `file_upload` de `<slug>.miniatura.png` sobre el input de la sección *Miniatura*.
5. *Listas* → **Seleccionar** → tildar «Videos cortos de ejercicios» → **Hecho**.
6. *Audiencia* → «No, no está creado para niños». *Mostrar más* → *Etiquetas*: escribir los tags separados por coma (con coma al final).
7. **Siguiente** ×3 → *Visibilidad* → **Privado** → **Guardar**.
8. Sacar el ID del video (en la lista `https://studio.youtube.com/playlist/PLaxjIdaCJSz8/videos` el link `/video/<ID>/edit`) y comprobar que figura en la lista y con la miniatura.
9. **Vincular con el largo** (§ 6 quinquies): si el largo está en el calendario, o se lo encuentra en Studio por título, la descripción ya sale con su link y se elige en *Vídeo relacionado*; si no, queda «pendiente».
10. **Registrar y mover** (mueve el `.corto.mp4` y el `.corto.youtube.txt` a `salida\subidos\EnYoutube\`, anota la fila en `cortos-subidos.csv` y regenera el CHECKLIST, columna **Corto subido**):

   ```powershell
   node plantilla/corto-subido.mjs <slug> <videoId> --vis=privado
   ```

Cuando el profe lo pasa a público: `node plantilla/corto-subido.mjs <slug> --vis=publico`.

**Trucos comprobados el 2026-11-05 (tanda de 5)**

- El diálogo de subida se abre directo con `https://studio.youtube.com/channel/UCn5-2weRP2H5zfqb1OlYkHg/videos/upload?d=ud` (esperar ~4 s antes de buscar el input de archivo).
- **Hashtags:** terminar la descripción con `#Shorts ` + salto de línea (con espacio y `
` al final). Si queda `#Shorts` pegado al final del texto, Studio abre las sugerencias y al hacer clic afuera lo cambia por `#shortsvideo`. No hacer clic en el diálogo mientras el popup está abierto.
- Tras marcar la lista y tocar *Hecho*, **esperar/mirar** que el diálogo no cambie de posición antes del próximo clic (un clic fuera de lugar abrió el reproductor en pantalla completa y cerró el diálogo: el video quedó como **borrador**). Un borrador se termina con *Editar borrador* → *Siguiente* ×3 → Privado → *Guardar*.
- Después de *Guardar* del diálogo, navegar a `/video/<ID>/edit` para el «Vídeo relacionado». En esa página el botón guardar se acciona por JS: `document.querySelector('#save').click()`; si aparece el aviso «Leave site?», es que falta guardar.
- En el selector de *Vídeo relacionado*, hacer **dos** clics en el buscador antes de escribir (si no, el texto no entra) y recién ahí buscar por título; el resultado se elige haciendo clic en la tarjeta.
- El selector solo ofrece videos **públicos o programados**: un corto **privado** no aparece en la lista, así que el **largo → corto no se puede hacer hasta que el corto sea público** (en el largo tampoco se agrega el link en la descripción antes, para no dejar un link muerto). Queda «pendiente» en la bitácora.

**Actualización 2026-11-06 (segunda tanda, ya en público)**

- Navegador de Studio: `select_browser` con el deviceId `a64d121a-d083-4bd7-bb7a-529d2c201274` (el otro Chrome; ambos entran al mismo canal).
- Los cortos se suben **directo en Público** (no privados). Después de *Siguiente* ×3 y elegir Público, **esperar ~25 s** a que terminen las comprobaciones y recién ahí *Publicar*; si sale «Aún estamos comprobando…», usar *Atrás*, esperar y repetir (no «Publicar de todas formas»).
- Etiquetas del corto: las mismas del largo (12, o las que tenga).
- **Largos con el texto pegado** (título plano «Running» y la descripción con los encabezados `TÍTULO / DESCRIPCIÓN / TAGS`, de subidas viejas): se arreglan solos desde su página de edición. Un script JS lee la descripción actual con `match(/TÍTULO\s*
(.+)
\s*DESCRIPCIÓN\s*
([\s\S]*?)
\s*TAGS\s*
(.+)/)`, pone como título la primera captura, como descripción `▶️ Mirá cómo se hace en segundos: https://youtu.be/<corto>` + la segunda (terminada en espacio + salto de línea), y las etiquetas se cargan a mano con `type` (separadas por coma). Antes de re-tipearlas hay que vaciar las que hubiera (botón *clear* del campo). **No** cargar las etiquetas con `execCommand`: parte las palabras.
- **Relacionado:** el selector del «Vídeo relacionado» solo ofrece videos públicos. Un largo **programado** (p. ej. Child's Pose, 22-11-2026) no aparece: se hace largo → corto ya, y corto → largo cuando el largo sea público (queda «pendiente» en `BITACORA-VINCULOS.md`).
- Búsqueda en ese selector: títulos con apóstrofe no matchean (buscar «Child», no «Child's Pose»); el corto y el largo se distinguen porque el corto lleva 🎬.

> Si el diálogo se cierra a medias, el video queda guardado como privado/borrador; se retoma desde Studio.

---

## 6 quinquies. Vincular el corto con el largo (y el largo con el corto)

Aplica **siempre**: al subir un corto y también al subir un video largo (el que explica Daniela; secciones 2, 3, 6 bis y 6 ter). Cada video apunta al otro de **dos maneras**:

1. **Link en la descripción:** `▶️ Explicación paso a paso con Daniela: https://youtu.be/<ID del largo>` (en el corto) y `▶️ Mirá cómo se hace en segundos: https://youtu.be/<ID del corto>` (en el largo).
2. **Vídeo relacionado:** en Studio → el video → *Detalles* → **Vídeo relacionado** → elegir el otro video (en el Short se muestra como enlace en el reproductor).

**Cómo se busca el otro video**

1. `node plantilla/vincular.mjs <slug> --buscar` → muestra el ID del largo si ya se conoce (`CALENDARIO-YOUTUBE.md` o `vinculos.csv`) y el del corto (`cortos-subidos.csv`).
2. Si no está: buscarlo en Studio (*Contenido*, filtro por título del ejercicio) y tomar el ID del link `/video/<ID>/edit`. Si no aparece, el otro video **todavía no está subido**: no se vincula, se registra «pendiente».
3. Si el otro video existe → editar el que se está subiendo (descripción con el link + *Vídeo relacionado*) **y también el otro** (agregarle el link en la descripción y su *Vídeo relacionado*). Así queda en los dos sentidos aunque se hayan subido en días distintos.
   **Excepción:** si el corto está **privado**, Studio no lo ofrece en el *Vídeo relacionado* del largo y el link en la descripción del largo quedaría muerto: se hace **corto → largo** ahora y **largo → corto** recién cuando el corto pase a público (queda «pendiente» en la bitácora).

**Registro:** cada vez, `node plantilla/vincular.mjs <slug> --largo=<ID> --corto=<ID> --largo-en-corto=si|pendiente --corto-en-largo=si|pendiente`. Escribe `vinculos.csv` y regenera **`BITACORA-VINCULOS.md`** (bitácora de videos vinculados). Los «pendiente» se retoman cuando se sube el que faltaba: buscar en la bitácora las filas con «pendiente».

> Los cortos generan su descripción con `node plantilla/corto-youtube.mjs <slug>`; si el largo ya se conoce, la línea del link sale sola (hoy 92 de 364 cortos tienen el ID del calendario). Si el largo se sube después, se agrega el link al editar el corto.

---

## 7. Problemas comunes

| Mensaje | Qué hacer |
|---|---|
| `El token … venció o fue revocado` | `& $PY $SK --auth fitlesuy`. Mientras la app esté en modo prueba, pasa cada 7 días. |
| El video quedó **privado** aunque pediste público | El proyecto de Google todavía no tiene la auditoría. Cambialo a mano con el link de YouTube Studio que imprime el script. |
| No se pudo poner la miniatura (403) | Verificá el canal por teléfono en <https://www.youtube.com/verify>. |
| Dice `✓ Miniatura` pero en Studio no aparece | La API no la deja puesta. Cargala a mano en Studio (sección 6 bis). |
| `quotaExceeded` / `uploadLimitExceeded` | Esperá al otro día. La cuota se renueva alrededor de las 4 o 5 de la mañana (hora de Uruguay/Argentina). |
| `{{marcador}}` sin reemplazar | Hay que corregir el `.youtube.txt`. Ese video no se sube. |
| "Ya figura en el log" | Ya lo subiste. Si querés resubirlo, usá `--force`. |
