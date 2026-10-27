# Subir a TikTok — FitLeUY

Por ahora la subida es **manual**. Después de 3 o 4 videos subidos (y de mirar sus números) se arma el plan automático con este documento como base.

Carpeta de trabajo: `salida/subidos/EnTikTok/`. Por cada video:

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
- [ ] Sonido: elegir uno de los que ofrece TikTok (en tendencia, tranquilo) y **bajarlo a 0 %**. El video ya trae música suave + voz; el sonido sólo sirve para que el video aparezca en la página de ese audio
- [ ] Privacidad: **todo el mundo**
- [ ] Configuración avanzada: marcar **contenido generado por IA** (la voz es TTS)
- [ ] Dejar habilitados Duo, Stitch y descargas
- [ ] Ubicación: Montevideo
- [ ] No pasar el video por otra app (sin marcas de agua de otras plataformas)

## Cómo se arma la descripción

Más corta que la de YouTube. TikTok corta en la primera línea, así que esa línea es el gancho.

1. **Gancho**: pregunta o problema + promesa concreta (ej. «¿Terminás el WOD y te vas sin estirar? 😬 Estos 4 estiramientos en 5 minutos 🧘»)
2. **Pasos**: una línea por paso, con emoji numérico
3. **Claves** en una línea
4. **CTA de guardar y compartir**: «📌 Guardalo para… y mandáselo a tu compañero de box que…» (guardados y compartidos son lo que más empuja)
5. **Aviso** corto: «⚠️ Contenido educativo, no reemplaza a un profesional. Si tenés una lesión, consultá antes.»
6. **Crédito de voz** (lo exige la licencia CC BY-SA): «🎙️ Voz: Daniela (Piper TTS), CC BY-SA 4.0.»
7. **8–12 hashtags**: mezcla de nicho (#estiramiento #crossfit #movilidad…), amplios (#gym #fitness #entrenamiento #fyp #parati) y local (#uruguay)

Repetir en el texto las palabras que la gente busca (nombre del ejercicio, músculo, «estiramiento», «técnica»…): TikTok funciona también como buscador.

## Al publicar

- **Horario (Uruguay)**: 18–21 h (vuelta del gym) o 12–13 h. Domingo de noche anda bien para contenido de «guardar para después».
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

## Pendiente para el plan automático (después de 3–4 videos)

- Generar `<slug>.tiktok.txt` y `<slug>.miniatura.tiktok.png` desde la ficha JSON, igual que el `.youtube.txt`
- Elegir qué videos van a TikTok (¿todos? ¿sólo los ≤ 60 s?) y calendario propio
- Ver si la subida se hace por la Content Posting API de TikTok o con Chrome en TikTok Studio (como la miniatura de YouTube)
