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

## 7. Problemas comunes

| Mensaje | Qué hacer |
|---|---|
| `El token … venció o fue revocado` | `& $PY $SK --auth fitlesuy`. Mientras la app esté en modo prueba, pasa cada 7 días. |
| El video quedó **privado** aunque pediste público | El proyecto de Google todavía no tiene la auditoría. Cambialo a mano con el link de YouTube Studio que imprime el script. |
| No se pudo poner la miniatura (403) | Verificá el canal por teléfono en <https://www.youtube.com/verify>. |
| `quotaExceeded` / `uploadLimitExceeded` | Esperá al otro día. La cuota se renueva alrededor de las 4 o 5 de la mañana (hora de Uruguay/Argentina). |
| `{{marcador}}` sin reemplazar | Hay que corregir el `.youtube.txt`. Ese video no se sube. |
| "Ya figura en el log" | Ya lo subiste. Si querés resubirlo, usá `--force`. |
