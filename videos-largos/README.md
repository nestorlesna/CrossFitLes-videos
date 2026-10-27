# Videos largos (16:9)

Videos horizontales de 8–12 min con capítulos, hechos a partir de un video de YouTube: se replica la secuencia con
nuestro personaje animado, la voz de Daniela y consejos de técnica propios.

- **Cómo hacer uno nuevo:** `GENERAR_VIDEOS_LARGOS.md` (raíz del proyecto).
- **Estado de todos:** `LISTA.md` (autogenerado con `node plantilla/largo/make-largo.mjs --lista`).
- **Para subir a YouTube:** `salida/<slug>.mp4` + `salida/<slug>.miniatura.png` + `salida/<slug>.youtube.txt`.

| Carpeta | Qué hay |
|---|---|
| `fichas/` | una ficha JSON por video (lo único que se escribe a mano) |
| `fuentes/<slug>/` | transcripción e info del original + `analisis.md` (qué se tomó y qué se sumó) |
| `proyectos/<slug>/` | proyecto HyperFrames generado (no editar a mano) |
| `salida/` | video final, miniatura 1280×720 y texto para YouTube |
