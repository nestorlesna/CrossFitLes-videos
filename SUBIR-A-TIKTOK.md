# Subir a TikTok — FitLeUY

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

> Nota: al intentar programar el 53.º video (cobra-pose) TikTok respondió "Solo puedes programar hasta 30 publicaciones". Pendiente de aclarar el tope; el plan sigue en `salida/subidos/plan-tiktok-2026-11-20.json` desde cobra-pose.

## Pendiente para el plan automático (después de 3–4 videos)

- Generar `<slug>.tiktok.txt` y `<slug>.miniatura.tiktok.png` desde la ficha JSON, igual que el `.youtube.txt`
- Elegir qué videos van a TikTok (¿todos? ¿sólo los ≤ 60 s?) y calendario propio
- Ver si la subida se hace por la Content Posting API de TikTok o con Chrome en TikTok Studio (como la miniatura de YouTube)
