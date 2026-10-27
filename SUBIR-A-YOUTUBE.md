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
