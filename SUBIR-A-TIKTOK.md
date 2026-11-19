# Subir a TikTok — FitLeUY

**Reglas nuevas (13/11):** a TikTok van **solo los videos comunes (`<slug>.mp4`), nunca los `.corto`**. Si el archivo trae prefijo (`OC_`, `OC_2_`…), **se sube con el nombre limpio `<slug>.mp4`** (copia temporal sin prefijo en `salida/_tiktok-tmp/`). Ritmo: **4 videos por día** (08:00, 13:30, 18:30, 21:00). Plan completo en `salida/subidos/plan-tiktok-2026-11-14.json`; en el registro, las filas «Plan 4/día (sin subir)» pasan a «Programado» cuando se suben.

Por ahora la subida es **manual**. Después de 3 o 4 videos subidos (y de mirar sus números) se arma el plan automático con este documento como base.

Cuenta: **dinouy.XXI@gmail.com** (ya logueada en el Chrome). Los videos pendientes están en `salida/subidos/EnYoutube/`; **después de subirlos a TikTok se mueven a `salida/subidos/EnTikTok/`**. Por cada video:

| Archivo | Qué es |
|---|---|
| `<slug>.mp4` | El video (vertical 1080×1920, tal cual sale del render) |
| `<slug>.tiktok.txt` | Descripción para pegar, exacta |
| `<slug>.miniatura.tiktok.png` | Portada: la miniatura de YouTube al 50 %, centrada sobre el color de fondo |

La portada se genera desde la miniatura de YouTube (la original a tamaño completo queda muy grande y TikTok corta el cuerpo):

```sh
ffmpeg -y -i <slug>.miniatura.png \
  -vf "scale=540:960:flags=lanczos,pad=1080:1920:270:480:color=0xF5F0E8" \
  <slug>.miniatura.tiktok.png
```

## Checklist al subir (lo que se hizo con el primer video)

- [ ] Descripción: pegar `<slug>.tiktok.txt` exacta
- [ ] Portada: subir `<slug>.miniatura.tiktok.png`
- [ ] Sonido: elegir uno de los que ofrece TikTok (en tendencia, tranquilo) y llevar el volumen al **mínimo (slider todo a la izquierda)**. El video ya trae música suave + voz; el sonido sólo sirve para que el video aparezca en la página de ese audio
- [ ] Privacidad: **todo el mundo**
- [ ] Programación: activar «Programar video» y elegir fecha y hora (ver horarios en «Al publicar»)
- [ ] Configuración avanzada: marcar **contenido generado por IA** (la voz es TTS)
- [ ] Dejar habilitados Duo, Stitch y descargas
- [ ] Ubicación: Montevideo
- [ ] No pasar el video por otra app (sin marcas de agua de otras plataformas)

## Receta con Chrome (probada con barbell-good-morning, 2026-10-28)

Página: `https://www.tiktok.com/tiktokstudio/upload`. Antes de nada, **agrandar la ventana** (`resize_window` 1500×950): en la ventana angosta los botones «Guardar» de los editores quedan fuera de pantalla.

1. **Video**: `find` «input type=file» → `file_upload` con `salida/subidos/EnYoutube/<slug>.mp4`. Esperar ~10 s a que diga «Cargado». Cerrar el aviso «Entendido» si sale.
2. **Descripción**: clic en el campo, `ctrl+a`, `Delete`, y `type` con el contenido exacto del `.tiktok.txt` (acepta emojis y saltos de línea; los hashtags quedan bien si el texto termina en espacio).
3. **Portada**: «Editar portada» → `find` «Upload cover image» → `file_upload` del `.miniatura.tiktok.png` → botón **Guardar** del diálogo (si no responde: clic por JS sobre el botón con texto «Guardar»).
4. **Programación**: «Mostrar más» y radio «Programación» → el diálogo «¿Permitir que el vídeo se guarde…?» es parte de programar → «Permitir». Elegir fecha y hora (**los minutos van de 5 en 5**).
5. **IA**: toggle «Contenido generado por IA» → «Activar» en el diálogo. Todo el mundo, comentarios y reutilización ya vienen marcados.
6. **Sonido**: botón «Sonidos» (debajo de la vista previa; clic por JS si queda fuera) → «Entendido» al aviso «Phone mode» → pestaña «Para ti» → **+** en «Sway on the Water» (tranquilo, 2:07) → clic en la pista → panel Audio → arrastrar el slider de Volumen todo a la izquierda (queda en **-∞ dB**) → **Guardar** arriba a la derecha. La vista previa sigue diciendo «Sonido original», es normal: al reabrir el editor la pista está.
7. **Programar** (botón rosa abajo) → «Vídeo publicado» y aparece en Publicaciones como «Procesando…». No hay campo de ubicación en la web de TikTok Studio, se omite.
8. Mover `<slug>.*` de `EnYoutube/` a `EnTikTok/`.

### Tanda 2026-10-28 → 20/11 (71 videos, 1 pestaña, ~10-15 min por video)

- **Plan**: `plan.json` en el scratchpad de la sesión (slug, fecha, hora). Solo videos ≤ 10 MB (79 de 115; los 36 mayores quedan en `EnYoutube/` para comprimir). TikTok **solo deja programar hasta ~29 días** (el 26/11 el 28/10); se programa hasta el 20/11. Horas fijas 12:30 / 18:30 / 21:00; orden: populares primero.
- **Una sola pestaña**: con varias, las de fondo no responden («Couldn't determine which page»). `file_upload` suele dar timeout aunque sube bien: comprobar `document.body.innerText.includes('<slug>.mp4')`.
- **Pasos por video** (≈9 llamadas): navigate+find input → `file_upload` mp4 → batch (ctrl+a, Delete, `type` del `.tiktok.txt`; **cuidado con letras cirílicas**: comprobar con `/[Ѐ-ӿ]/`) + find «Editar portada» → clic ref + find «Upload cover image» → `file_upload` portada → batch (Guardar por JS, «Mostrar más», «Programación», scrollIntoView «Cuándo publicar», IA toggle en (505,514), fecha en (390,147), hora en (580,147)) → elegir día/hora/minuto → «Sonidos» por JS, **+** del primer sonido en (388,255), arrastrar volumen (1257,185)→(1130,185), Guardar (1419,34) → esperar la revisión («No se han detectado…», 1-15 min) → «Programar» por JS.
- **No pulsar «Publicar ahora»** del aviso «¿Seguir con la publicación?»: sale si se programa antes de terminar la revisión; hay que esperar.
- Selector de hora: la rueda desplaza 3 filas por paso; el de minutos queda centrado en el minuto actual (hay que subir/bajar con la rueda hasta ver el que se busca).
- Al terminar cada video: `mv EnYoutube/<slug>.* EnTikTok/`.

### Notas de la sesión 13/11 (Browser 1, ventana 1500×950, viewport 1568×726)

- Chrome: usar **Browser 1** (`86f93e42-…`); en Browser 2 TikTok Studio queda en blanco. Si `file_upload` falla con «offline»/«página no determinada», cerrar y reabrir Chrome; después del reinicio funcionó (subir con el `ref` del `file-input (hidden)`).
- Hora: el selector **no acepta texto**. Clic en un valor visible de la columna (hora o minutos) y la rueda mueve 1 fila cada 3 ticks (máx. 10 por llamada); tras elegir, la fila del centro es la elegida.
- «Programación» ya no muestra el diálogo de permitir; el toggle IA se activa directo. Sonidos: por JS `button` con texto «Sonidos» → **+** del primer tema (317,208) → arrastrar volumen (1382,151)→(1280,151) → Guardar (1515,28).
- Programar por JS (`button` «Programar»); redirige a Publicaciones y el video aparece «Procesando…». Después: `python mover-tt.py <slug>` (mueve archivos a `EnTikTok/`, marca `done` en el plan y el registro).

### Estado al corte (13/11, noche)

- **Programados con el plan 4/día (15/11, 21:30): 36 de 270** (30 programados a futuro del 16/11 08:00 al 23/11 13:30; `wall-thoracic-extensions` dio «Error al publicar» y se resolvió con «Reintentar»). Siguiente a subir: `spiderman-stretch-rotation` (2026-11-23 18:30). TikTok permite hasta 30 programados a la vez; ya hay 30 a futuro, así que hay que esperar a que se publiquen para seguir.
- `seated-quad-stretch` quedó programado el 15/11 a las 21:00 (el borrador roto del intento manual se descartó). Al abrir la página de subida puede salir «Descartar/Continuar» de un borrador viejo: al pulsar Descartar aparece un diálogo de confirmación que bloquea el teclado hasta pulsar su «Descartar» rojo (si la descripción no se escribe, es eso). Los videos pueden estar en `salida/` (no solo en `EnYoutube/`): usar el `dir` del plan. Notas: la herramienta `file_upload` admite 10 MB por llamada, pero TikTok Studio acepta hasta 30 GB; el viewport de esta ventana es 1150×722, así que las coordenadas de la receta cambian (el toggle de IA queda en ~(339,380) tras abrir «Mostrar más»; usar clic por coordenadas, no `.Switch__content` genérico, que activa «Avisar sobre el contenido»).
- **Pendiente sin subir:** el plan sigue en `salida/subidos/plan-tiktok-2026-11-14.json` (`done:false`). Las filas «Plan 4/día (sin subir)» de la tabla son las pendientes; las de «Programado» están hechas.
- **Receta rápida por JS** (probada): hora → clic en el input de hora y luego en `.tiktok-timepicker-option-text.tiktok-timepicker-left` (hh) y `…-right` (mm); fecha → clic con coordenadas en el input de fecha y luego JS sobre `span.day.valid` con el número del día; IA → `.Switch__content` junto a «Contenido generado por IA»; «Programar» solo si hay 2 «No se han detectado…» y fecha/hora correctas.
- Si `file_upload` falla (extensión desconectada): cerrar/reabrir Chrome, esperar a que `list_connected_browsers` muestre el navegador. Si TikTok restaura un borrador roto («Algo salió mal»), navegar con `force` para descartarlo.

## Cómo se arma la descripción

Más corta que la de YouTube. TikTok corta en la primera línea, así que esa línea es el gancho.

1. **Gancho**: pregunta o problema + promesa concreta (ej. «¿Terminás el WOD y te vas sin estirar? 😬 Estos 4 estiramientos en 5 minutos 🧘»)
2. **Pasos**: una línea por paso, con emoji numérico
3. **Claves** en una línea
4. **CTA de guardar y compartir**: «📌 Guardalo para… y mandáselo a tu compañero de box que…» (guardados y compartidos son lo que más empuja)
   Justo después, la **referencia al canal**: «▶️ Más técnica paso a paso en mi canal de YouTube: FitLesUY» + `https://www.youtube.com/channel/UCn5-2weRP2H5zfqb1OlYkHg`
5. **Aviso** corto: «⚠️ Contenido educativo, no reemplaza a un profesional. Si tenés una lesión, consultá antes.»
6. **Crédito de voz** (lo exige la licencia CC BY-SA): «🎙️ Voz: Daniela (Piper TTS), CC BY-SA 4.0.»
7. **8–12 hashtags**: mezcla de nicho (#estiramiento #crossfit #movilidad…), amplios (#gym #fitness #entrenamiento #fyp #parati) y local (#uruguay)

Repetir en el texto las palabras que la gente busca (nombre del ejercicio, músculo, «estiramiento», «técnica»…): TikTok funciona también como buscador.

## App FitLesUY en la descripción

Después de la referencia al canal (paso 4), agregar una línea con la app: **gratis, para Android, para monitorear las rutinas**.

```
📲 App gratis FitLesUY para Android: seguí las rutinas y registrá tus sesiones → https://nestorlesna.github.io/CrossFitLes/
```

TikTok no vuelve clicable el link dentro de la descripción: conviene tener el mismo link en la **bio** de la cuenta. En YouTube la descripción lleva el bloque completo (ver `SUBIR-A-YOUTUBE.md`, «App FitLesUY en TODAS las descripciones»).

## Al publicar

- **Ritmo**: 3 videos por día, programados en tres horarios fijos (hora Uruguay): **12:30** (almuerzo), **18:30** (vuelta del gym) y **21:00** (noche, pico de uso). Son estimaciones del sector, no datos propios: ajustar con Analytics → Actividad de los seguidores.
- Domingo de noche anda bien para contenido de «guardar para después».
- **Nunca borrar y volver a subir** un video que arranca lento: TikTok a veces lo levanta días después y los duplicados penalizan.

## Primera hora después de publicar

- **Comentario fijado** con una pregunta (ej. «¿Cuál de los 4 es el que más te cuesta? 👇»)
- **Responder todos los comentarios** rápido; a los mejores, con «Responder con video»
- **Compartir** por WhatsApp e Instagram Stories a grupos de box / gym

## Estrategia de cuenta

- **Constancia**: 1–2 videos por día. Lo que crece es la cuenta, no un video suelto.
- **Series**: «Movilidad para crossfiteros parte 1, 2, 3…» para que entren al perfil a buscar las otras.
- **A las 48 h** mirar estadísticas: si se van en los primeros 3 s, reforzar el gancho visual/textual del arranque en los próximos.

## Registro de subidas

Leyenda de la columna Notas (comprobado 15/11 contra los archivos): ✅ = subible (mp4 ≤ 10 MB + `.tiktok.txt` + portada `.miniatura.tiktok.png` presentes) · ⛔ = no subible todavía (>10 MB, comprimir) · «Programado» = ya hecho. Plan 4/día: 08:00, 13:30, 18:30, 21:00; plan reacomodado el 15/11 a las 19:51 (los horarios 13:30 y 18:30 de ese día ya habían pasado): seated-quad-stretch sale hoy 21:00 y el resto corre en orden, 4/día desde el 16/11; el límite de TikTok (~29 días) llega al 14/12 y hay tope de 30 programados a la vez, así que se sube por tandas siguiendo el orden de la tabla.

Completar a las 48 h con los números (vistas, % visto completo, guardados, compartidos, seguidores ganados) — son la base para decidir el plan automático.

| Fecha | Video | Sonido (a 0 %) | Vistas 48 h | % completo | Guardados | Compartidos | Seguidores | Notas |
|---|---|---|---|---|---|---|---|---|
| 2026-10-24 | general-stretching | uno de TikTok | | | | | | Primer video. Portada al 50 %, IA marcada, público |
| 2026-10-25 | air-squat | uno de TikTok | | | | | | Fecha según el `.tiktok.txt`. Portada al 50 % |
| 2026-10-26 | rowing | uno de TikTok | | | | | | Portada al 50 % |
| 2026-10-26 | barbell-hang-power-snatch | uno de TikTok | | | | | | Portada al 50 %. Crédito de voz doble (Daniela + Kokoro Heart) |
| 2026-10-28 | barbell-good-morning | Sway on the Water, -∞ dB | | | | | | PRUEBA programada 08:25 (+1 h). Primera con referencia al canal FitLesUY. Receta en «Receta con Chrome» |
| 2026-10-28 12:30 | 90-90-hip-rotation | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-28 18:30 | barbell-back-squat | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-29 12:30 | barbell-front-squat | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-29 18:30 | barbell-deadlift | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-29 21:00 | barbell-power-snatch | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-30 12:30 | barbell-hang-power-clean | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-30 18:30 | barbell-power-clean | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-30 21:00 | alternating-90-90-into-shin-box | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-31 12:30 | barbell-clean-and-jerk | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-31 18:30 | barbell-thruster | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-10-31 21:00 | alternating-single-arm-dumbbell-power-snatch | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-01 12:30 | bodyweight-burpee | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-01 18:30 | bar-pull-up | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-01 21:00 | arm-circles | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-02 12:30 | box-jump | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-02 18:30 | wall-ball-shot | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-02 21:00 | band-external-rotation | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-03 12:30 | kettlebell-swing | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-03 18:30 | hanging-toes-to-bar | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-03 21:00 | band-pass-through | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-04 12:30 | barbell-push-press | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-04 18:30 | barbell-overhead-squat | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-04 21:00 | band-pull-apart | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-05 12:30 | barbell-romanian-deadlift | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-05 18:30 | barbell-push-jerk | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-05 21:00 | band-triceps-pushdown | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-06 12:30 | barbell-squat-clean | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-06 18:30 | plank-hold | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-06 21:00 | barbell-bicep-curl | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-07 12:30 | hollow-hold | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-07 18:30 | dead-bug | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-07 21:00 | barbell-high-hang-power-clean | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-08 12:30 | cat-cow | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-08 18:30 | child-s-pose | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-08 21:00 | barbell-high-hang-squat-clean | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-09 12:30 | pigeon-pose | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-09 18:30 | couch-stretch | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-09 21:00 | barbell-muscle-snatch | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-10 12:30 | dynamic-warm-up | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-10 18:30 | barbell-sumo-deadlift-high-pull | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-10 21:00 | bent-over-dumbbell-lateral-raise | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-11 12:30 | snatch-high-pull | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-11 18:30 | hollow-rock | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-11 21:00 | box-jump-over | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-12 12:30 | russian-twist | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-12 18:30 | calf-raise | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-12 21:00 | burpee-broad-jump | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-13 12:30 | box-step-up | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-13 18:30 | burpee-over-the-bar | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-13 21:00 | cuban-press | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-14 12:30 | barbell-hang-clean | primer sonido, -∞ dB | | | | | | Programado (tanda 28/10) |
| 2026-11-14 08:00 | supine-spinal-twist | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-14 13:30 | half-kneeling-hip-flexor-stretch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-14 18:30 | cobra-pose | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-14 21:00 | overhead-triceps-stretch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-15 08:00 | seated-forward-fold | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-15 21:00 | seated-quad-stretch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-16 08:00 | standing-biceps-stretch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-16 13:30 | supine-abdominal-stretch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-16 18:30 | wrist-extensor-stretch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-16 21:00 | kettlebell-good-morning-to-squat | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-17 08:00 | kettlebell-farmer-carry | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-17 13:30 | shuttle-run | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-17 18:30 | yoga-push-up | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-17 21:00 | scapular-push-up | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-18 08:00 | sled-push-pull | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-18 13:30 | skierg | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-18 18:30 | kettlebell-good-morning | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-18 21:00 | squat-thoracic-rotation | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-19 08:00 | weighted-lunge | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-19 13:30 | push-press-behind-the-neck | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-19 18:30 | v-up | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-19 21:00 | sled-push | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-20 08:00 | wall-lat-stretch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-20 13:30 | wall-shoulder-stretch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-20 18:30 | dumbbell-push-press | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-20 21:00 | farmer-s-carry | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-21 08:00 | partner-wall-ball-sit-up | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-21 13:30 | wall-sit | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-21 18:30 | wall-thoracic-extensions | primer sonido, -∞ dB | | | | | | Programado (plan 4/día). Dio «Error al publicar»; el usuario pulsó «Reintentar» y quedó OK
| 2026-11-21 21:00 | march-in-place | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-22 08:00 | bird-dog-crunch | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-22 13:30 | cossack-squat | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-22 18:30 | descanso | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-22 21:00 | dynamic-hollow-hold | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-23 08:00 | goblet-squat-hold-press | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-23 13:30 | scapular-wall-slides | primer sonido, -∞ dB | | | | | | Programado (plan 4/día) |
| 2026-11-23 18:30 | spiderman-stretch-rotation | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-23 21:00 | dead-bug-with-band-resistance | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-24 08:00 | power-clean | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-24 13:30 | partner-wall-ball-over-bar | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-24 18:30 | barbell-front-rack-reverse-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-24 21:00 | wall-ball-box-over | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-25 08:00 | isometric-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-25 13:30 | kettlebell-ankle-mobility-drill | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-25 18:30 | doorway-chest-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-25 21:00 | supine-figure-4-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-26 08:00 | dumbbell-overhead-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-26 13:30 | single-leg-calf-raise | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-26 18:30 | tibialis-raise | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-26 21:00 | bodyweight-handstand-push-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-27 08:00 | superman-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-27 13:30 | 4-6-breathing | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-27 18:30 | dead-bug-hold-with-dumbbell | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-27 21:00 | banded-triceps-extensions | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-28 08:00 | hollow-to-superman-roll | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-28 13:30 | kettlebell-sumo-deadlift-high-pull | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-28 18:30 | snatch-grip-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-28 21:00 | squat-press-out | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-29 08:00 | strict-knees-to-elbows | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-29 13:30 | toe-touch-sit-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-29 18:30 | weighted-bird-dog | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-29 21:00 | weighted-plank | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-30 08:00 | kettlebell-windmill | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-30 13:30 | barbell-deadlift-to-knee-height | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-30 18:30 | deficit-banded-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-11-30 21:00 | single-leg-toes-to-bar | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-01 08:00 | rope-climb | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-01 13:30 | dumbbell-back-rack-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-01 18:30 | dumbbell-hang-clean-and-push-jerk | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-01 21:00 | squat-jump-to-plate | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-02 08:00 | weighted-sit-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-02 13:30 | standing-hamstring-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-02 18:30 | weighted-side-plank | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-02 21:00 | dumbbell-bench-press | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-03 08:00 | standing-quad-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-03 13:30 | ankle-mobility-rock | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-03 18:30 | calf-raise-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-03 21:00 | clamshell-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-04 08:00 | core-overhead-hold-with-side-bend | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-04 13:30 | half-kneeling-hip-flexor-hamstring-dynamic-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-04 18:30 | half-kneeling-ankle-dorsiflexion-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-04 21:00 | half-kneeling-windmill-rotation-and-side-bend | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-05 08:00 | overhead-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-05 13:30 | pigeon-rotation | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-05 18:30 | quadruped-thoracic-rotation | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-05 21:00 | single-leg-wall-sit | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-06 08:00 | towel-isometric-curl | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-06 13:30 | world-s-greatest-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-06 18:30 | bodyweight-push-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-06 21:00 | plank-shoulder-taps | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-07 08:00 | side-plank | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-07 13:30 | hanging-knees-to-elbows | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-07 18:30 | bodyweight-glute-bridge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-07 21:00 | mountain-climbers | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-08 08:00 | kettlebell-front-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-08 13:30 | barbell-bent-over-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-08 18:30 | bodyweight-hollow-body-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-08 21:00 | high-pull-external-rotation | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-09 08:00 | jumping-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-09 13:30 | pike-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-09 18:30 | single-arm-dumbbell-push-press | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-09 21:00 | single-leg-dumbbell-romanian-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-10 08:00 | toe-touch-crunch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-10 13:30 | ab-wheel-kneeling-rollout | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-10 18:30 | alternating-kettlebell-clean-and-press | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-10 21:00 | alternating-kettlebell-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-11 08:00 | american-kettlebell-swing | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-11 13:30 | band-alternating-pass-through | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-11 18:30 | band-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-11 21:00 | band-scapular-retraction-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-12 08:00 | banded-ankle-dorsiflexion-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-12 13:30 | banded-lat-pulldown | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-12 18:30 | banded-prone-leg-curl | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-12 21:00 | barbell-low-hang-power-clean | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-13 08:00 | barbell-shrug | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-13 13:30 | barbell-stiff-leg-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-13 18:30 | bear-crawl-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-13 21:00 | bird-dog-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-14 08:00 | bulgarian-split-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-14 13:30 | burpee-to-bar | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-14 18:30 | counterbalance-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-14 21:00 | cross-body-mountain-climbers | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-15 08:00 | db-lateral-step-over | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-15 13:30 | dual-dumbbell-snatch-with-burpee | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-15 18:30 | dumbbell-burpee-snatch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-15 21:00 | dumbbell-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-16 08:00 | dumbbell-front-raise | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-16 13:30 | dumbbell-hip-thrust | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-16 18:30 | dumbbell-reverse-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-16 21:00 | dumbbell-romanian-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-17 08:00 | dumbbell-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-17 13:30 | dumbbell-wall-sit | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-17 18:30 | goblet-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-17 21:00 | half-kneel-banded-lat-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-18 08:00 | half-kneeling-thoracic-rotation | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-18 13:30 | hanging-flutter-kicks | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-18 18:30 | hanging-leg-raise-with-rotation-over-box | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-18 21:00 | heel-elevated-goblet-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-19 08:00 | hip-rotations-in-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-19 13:30 | hollow-hold-pass | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-19 18:30 | i-y-t-raises | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-19 21:00 | inchworm | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-20 08:00 | isometric-push-up-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-20 13:30 | isometric-split-squat-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-20 18:30 | jump-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-20 21:00 | kb-dead-bug | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-21 08:00 | kettlebell-box-step-over | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-21 13:30 | kettlebell-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-21 18:30 | kettlebell-jumping-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-21 21:00 | kettlebell-pullover-on-wall-ball | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-22 08:00 | kettlebell-romanian-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-22 13:30 | kettlebell-single-leg-romanian-deadlift | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-22 18:30 | kettlebell-turkish-sit-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-22 21:00 | kettlebell-upright-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-23 08:00 | l-sit-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-23 13:30 | lateral-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-23 18:30 | lateral-raise-to-overhead | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-23 21:00 | lunge-with-open-rotation | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-24 08:00 | plank-to-opposite-toe-touch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-24 13:30 | plank-up-down | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-24 18:30 | plate-jump-over-and-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-24 21:00 | quadruped-rock-back | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-25 08:00 | reverse-snow-angels | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-25 13:30 | sally-up-sally-down | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-25 18:30 | sandbag-walking-lunges | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-25 21:00 | scapular-plank-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-26 08:00 | single-leg-pallof-press | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-26 13:30 | stability-ball-plate-crunch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-26 18:30 | tempo-push-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-26 21:00 | tempo-squat-3-1-3 | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-27 08:00 | towel-isometric-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-27 13:30 | wall-shoulder-car | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-27 18:30 | wall-sit-with-leg-extension | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-27 21:00 | wall-squat-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-28 08:00 | weighted-butterfly-sit-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-28 13:30 | weighted-hollow-rock | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-28 18:30 | y-raises | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-28 21:00 | bodyweight-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-29 08:00 | bodyweight-sit-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-29 13:30 | ring-strict-muscle-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-29 18:30 | double-under | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-29 21:00 | chest-to-bar-pull-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-30 08:00 | ring-dip | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-30 13:30 | ghd-sit-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-30 18:30 | bodyweight-walking-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-30 21:00 | double-dumbbell-overhead-walking-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-31 08:00 | barbell-bench-press | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-31 13:30 | ghd-back-extension | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-31 18:30 | negative-push-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2026-12-31 21:00 | walking-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-01 08:00 | barbell-upright-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-01 13:30 | bicycle-crunch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-01 18:30 | cool-down-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-01 21:00 | dumbbell-devil-s-press | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-02 08:00 | ring-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-02 13:30 | seated-leg-tucks | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-02 18:30 | superband-shoulder-dislocates | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-02 21:00 | barbell-inverted-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-03 08:00 | wall-walk | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-03 13:30 | dumbbell-split-clean | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-03 18:30 | kettlebell-snatch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-03 21:00 | knee-push-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-04 08:00 | med-ball-box-step-over | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-04 13:30 | oblique-crunch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-04 18:30 | ring-handstand-push-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-04 21:00 | side-lying-thoracic-opening | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-05 08:00 | band-hammer-curl-to-triceps-kickback | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-05 13:30 | band-rdl-to-bent-over-row | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-05 18:30 | band-shoulder-toss | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-05 21:00 | band-squat-to-front-raise | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-06 08:00 | band-woodchopper | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-06 13:30 | banded-glute-kickback | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-06 18:30 | bar-muscle-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-06 21:00 | barbell-hang-clean-and-jerk | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-07 08:00 | barbell-hang-muscle-clean-and-press | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-07 13:30 | barbell-hang-power-cluster | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-07 18:30 | barbell-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-07 21:00 | barbell-strict-press | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-08 08:00 | bodyweight-pistol-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-08 13:30 | bottom-half-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-08 18:30 | boxer-shuffle | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-08 21:00 | deep-squat-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-09 08:00 | dumbbell-bicep-curl | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-09 13:30 | dumbbell-farmer-hold | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-09 18:30 | dumbbell-one-arm-overhead-lunge | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-09 21:00 | dumbbell-thruster | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-10 08:00 | ground-pull-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-10 13:30 | high-knee-clap | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-10 18:30 | high-knees | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-10 21:00 | jumping-jack | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-11 08:00 | kettlebell-clean-and-jerk | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-11 13:30 | kettlebell-ground-to-overhead | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-11 18:30 | kettlebell-leg-overs | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-11 21:00 | kettlebell-push-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-12 08:00 | kneeling-squat | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-12 13:30 | lying-leg-raise | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-12 18:30 | pike-walk | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-12 21:00 | plank-knee-tap | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-13 08:00 | prone-around-the-world | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-13 13:30 | reach-up-crunch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-13 18:30 | seated-leg-compression | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-13 21:00 | shadow-boxing | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-14 08:00 | skater-jump | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-14 13:30 | sprint-in-place | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-14 18:30 | squat-to-toe-raise | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-14 21:00 | standing-cross-crunch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-15 08:00 | standing-knees-to-elbow | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-15 13:30 | step-jack | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-15 18:30 | upward-to-downward-dog | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-15 21:00 | weighted-box-step-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-16 08:00 | wide-negative-push-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-16 13:30 | open-the-gate | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-16 18:30 | candlestick-to-straddle-stretch | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-16 21:00 | barbell-cluster | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-17 08:00 | thoracic-wall-sweep | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-17 13:30 | clean-drop-drill | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-17 18:30 | leg-swing | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-17 21:00 | kneeling-weighted-shoulder-car | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-18 08:00 | dumbbell-around-the-world | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-18 13:30 | banded-pull-up | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-18 18:30 | dumbbell-standing-calf-raise | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-18 21:00 | plank-hip-dips | primer sonido, -∞ dB | | | | | | ✅ Plan 4/día (sin subir) |
| 2027-01-19 08:00 | running | primer sonido, -∞ dB | | | | | | ⛔ Plan 4/día (sin subir). >10 MB: lo sube el usuario a mano (ver «Para subir a mano») |
| 2027-01-19 13:30 | assault-bike | primer sonido, -∞ dB | | | | | | ⛔ Plan 4/día (sin subir). >10 MB: lo sube el usuario a mano (ver «Para subir a mano») |
| 2027-01-19 18:30 | jump-rope | primer sonido, -∞ dB | | | | | | ⛔ Plan 4/día (sin subir). >10 MB: lo sube el usuario a mano (ver «Para subir a mano») |
| 2027-01-19 21:00 | sled-pull | primer sonido, -∞ dB | | | | | | ⛔ Plan 4/día (sin subir). >10 MB: lo sube el usuario a mano (ver «Para subir a mano») |
| 2027-01-20 08:00 | walking | primer sonido, -∞ dB | | | | | | ⛔ Plan 4/día (sin subir). >10 MB: lo sube el usuario a mano (ver «Para subir a mano») |
| 2027-01-20 13:30 | wall-ball-run | primer sonido, -∞ dB | | | | | | ⛔ Plan 4/día (sin subir). >10 MB: lo sube el usuario a mano (ver «Para subir a mano») |
| 2027-01-20 18:30 | sandbag-carry | primer sonido, -∞ dB | | | | | | ⛔ Plan 4/día (sin subir). >10 MB: lo sube el usuario a mano (ver «Para subir a mano») |
| 2027-01-20 21:00 | lateral-shuffle | primer sonido, -∞ dB | | | | | | ⛔ Plan 4/día (sin subir). >10 MB: lo sube el usuario a mano (ver «Para subir a mano») |

## Para subir a mano (> 10 MB)

El usuario los sube a mano. Cada uno lleva su `<slug>.tiktok.txt` y `<slug>.miniatura.tiktok.png` en la misma carpeta; mover después con `python mover-tt.py <slug>`. **Antes de subir:** el tope de 10 MB fue un filtro puesto en la tanda del 28/10 (no consta como límite real de TikTok) y en `EnTikTok/` no hay ningún mp4 mayor a 9,3 MB, así que no se encontró registro de cuáles >10 MB se subieron; probar si TikTok Studio los acepta tal cual y, si no, comprimir.

| Fecha y hora | Video | MB | Archivo |
|---|---|---|---|
| 2027-01-19 08:00 | running | 13.6 | `salida/subidos/EnYoutube/running.mp4` |
| 2027-01-19 13:30 | assault-bike | 12.8 | `salida/subidos/EnYoutube/assault-bike.mp4` |
| 2027-01-19 18:30 | jump-rope | 11.9 | `salida/jump-rope.mp4` |
| 2027-01-19 21:00 | sled-pull | 10.2 | `salida/subidos/EnYoutube/sled-pull.mp4` |
| 2027-01-20 08:00 | walking | 10.1 | `salida/walking.mp4` |
| 2027-01-20 13:30 | wall-ball-run | 11.5 | `salida/subidos/EnYoutube/wall-ball-run.mp4` |
| 2027-01-20 18:30 | sandbag-carry | 10.1 | `salida/sandbag-carry.mp4` |
| 2027-01-20 21:00 | lateral-shuffle | 11.1 | `salida/lateral-shuffle.mp4` |

> Nota: al intentar programar el 53.º video (cobra-pose) TikTok respondió "Solo puedes programar hasta 30 publicaciones". Pendiente de aclarar el tope; el plan sigue en `salida/subidos/plan-tiktok-2026-11-20.json` desde cobra-pose.

## Pendiente para el plan automático (después de 3–4 videos)

- Generar `<slug>.tiktok.txt` y `<slug>.miniatura.tiktok.png` desde la ficha JSON, igual que el `.youtube.txt`
- Elegir qué videos van a TikTok (¿todos? ¿sólo los ≤ 60 s?) y calendario propio
- Ver si la subida se hace por la Content Posting API de TikTok o con Chrome en TikTok Studio (como la miniatura de YouTube)
