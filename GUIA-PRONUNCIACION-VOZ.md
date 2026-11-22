# Guía: que la voz en off pronuncie bien (R, doble L, inglés)

Lo que aprendimos en este proyecto con **Piper + Daniela (es_AR)**. Sirve para cualquier proyecto idéntico
(HyperFrames + `make-exercise.mjs` + `piper-tts.py`).

> Idea central: **el motor de voz es español**. Todo lo que está en inglés (o cualquier palabra rara) lo lee con
> reglas del castellano y sale mal. La solución NO es cambiar el motor: es **escribir la palabra como se
> pronunciaría en castellano** (ortografía fonética) y que ese reemplazo valga **solo para el audio**; el
> subtítulo y la descripción siguen con el texto real.

---

## 1. Cómo funciona el mecanismo

En la ficha del ejercicio (`ejercicios/<slug>.json`):

```json
"pronuncia": {
  "Kettlebell": "Ketelbel",
  "kettlebell": "ketelbel",
  "Romanian": "Rrouméinian",
  "wall ball": "uál bol"
}
```

`make-exercise.mjs` (función `tts`) recorre el diccionario **en el orden en que está escrito** y hace
`text.split(from).join(to)` sobre el texto de cada escena **antes** de mandarlo a Piper. Por eso:

1. **Distingue mayúsculas/minúsculas.** `Kettlebell` y `kettlebell` son dos entradas distintas: poné las dos.
2. **El orden importa.** Poné primero la frase larga y después la palabra suelta
   (`"Barbell Hang Clean"` antes que `"Clean"`); si no, la palabra suelta ya reemplazó y la frase larga no
   coincide más.
3. **Un reemplazo puede pisar a otro.** Si el resultado de una entrada contiene el texto que busca otra
   entrada posterior, se vuelve a reemplazar. Elegí salidas que no contengan claves del diccionario.
4. Solo cambia la voz. Subtítulo, `youtube.txt` y miniatura quedan con el texto real.
5. Si cambia el texto, hay que regenerar la voz (`--force-tts` si el diccionario cambió y el texto no).
   `make-exercise` reutiliza el audio cuando el `audio_request.json` es idéntico.

---

## 2. Problema: la **R** no suena bien

**Síntoma:** al principio de palabra (o tras consonante) Daniela dice una R suave, casi una "d" o "l"
(`Romanian` → "Omanian", `Reverse` → "Evemerse", `row` → "ow").

**Solución:** la R inicial en castellano es vibrante múltiple solo si se escribe **`rr`**. Duplicar la R:

| Original | Se escribe para la voz |
|---|---|
| Romanian | `Rrouméinian` |
| Reverse Lunge | `Rrivérs lanch` |
| Russian Twist | `Rashan tuist` (R inicial + `sh`→"sh" ya vibra bien con la A tónica) |

Reglas prácticas:
- **R inicial → `rr`.** (`Rr…`). Es el arreglo principal.
- **R al final de sílaba en palabras en inglés** (`row`, `rack`, `rock`, `raise`): reescribir sin la R
  problemática o con el sonido inglés aproximado: `row → rou`, `rack → rac / rak`, `rock → rok`, `raise → reis`.
  Si queda débil, probar `rr` (`rrou`).
- **Evitar `-er` / `-or` final con R muda.** `Farmer → Fármers`, `Powers → páuer`: la R final queda flojita
  pero audible si la vocal anterior es tónica; si desaparece, agregar una vocal de apoyo (`kerl` en vez de `curl`).
- **No usar letras R sueltas dobles en el medio** salvo que quieras la vibrante ("carro"): `carri`
  (carry) está bien con una sola `r` porque es la R simple de "caro".

---

## 3. Problema: la **doble L** (`ll`) no se escucha

**Síntoma:** en inglés `ll` suena como "l" simple. Piper en castellano la lee como **"y"/"sh"**
(`ball` → "bay"/"basha", `wall` → "uay", `bell` → "bey") o se la come.

**Solución:** nunca dejar `ll` en la palabra que va a la voz. Reemplazar por **`l` simple** y, si la palabra
termina en `ll`, **separar la sílaba** o cerrar con vocal/consonante para que la L se oiga:

| Original | Para la voz | Qué se corrige |
|---|---|---|
| wall ball | `uál bol` / `uol bol` | `wall` → `uál`, `ball` → `bol` (sin `ll`) |
| Wall Walk | `Uol uók` | idem |
| Kettlebell | `Ketelbel` / `kételbel` | `bell` → `bel` (una sola L) |
| Kettlebell (nombre en voz) | `Kétol bel` | separado en dos palabras: la L cae al final de sílaba y suena |
| Dumbbell | `dambel` / `dámbel` | idem |
| Barbell | `bárbel` | idem |
| Ab Wheel | `ab güil` | `wh` → `gu`, y `ee` → `i` |
| Wall Ball Run | `uol bol ron` | |

Reglas prácticas:
- **Prohibido `ll` en el texto de la voz** para palabras inglesas. Siempre `l`.
- Palabra que termina en `l` y se pierde (`bel`, `bol`): probar una **L doble separada** (`bel bel`) o
  dividir en dos palabras (`Kétol bel`). La pausa del espacio ayuda a que la L final suene.
- Para castellano real (`rodillas`, `pantorrillas`): la `ll` rioplatense ("sh") está bien en Daniela; no tocar
  salvo que se pierda, y en ese caso escribir `rodishas`.

---

## 4. Otros patrones fonéticos que ya resolvimos

Escribir cómo suena, con ortografía castellana:

| Sonido inglés | Se escribe | Ejemplos |
|---|---|---|
| `w` inicial | `u` / `ú` / `gu` | wall → `uol`, walking → `uóquin`, weighted → `uéited`, Wheel → `güil` |
| `h` aspirada | `j` | hang → `jang`, hollow → `jólou`, hold → `jold`, high → `jái`, hip → `jip`, handstand → `jandstand` |
| `-ing` | `-in` / `-ing` sin g marcada | walking → `uóquin`, swing → `suing` |
| `ee` / `ea` (larga) | `i` | clean → `clin`, squat clean → `scuat clin`, burpee → `burpii`, knees → `nis` |
| `ai` / `ay` / `ei` | `ei`, `ai` | raise → `reis`, plate → `pleit`, bike → `baik` |
| `th` | `z`, `d`, `t` | thruster → `thráster`/`traster`, through → `zru`, the → `de` |
| `sh` | `sh` (funciona) o `ch` | push → `push`/`puch`, snatch → `snach` |
| `j` inicial inglesa | `y` / `ch` | jerk → `yerk`, jump → `champ`, jack → `yak` |
| `c` / `k` final | `c` | rack → `rac`, plank → `planc`, crunch → `cranch` |
| `s` inicial + consonante | agregar `e` | squat → `escuat`, scapular → `escápular`, spiderman → `espáiderman` |
| `u` corta inglesa | `a` | clean… curl → `kerl`, cluster → `claster`, muscle → `masel`, cranch |
| `oo` | `u` | good morning → `gud mórnin` |
| Números | en letras | `90/90` → `noventa noventa`, `4-6` → `cuatro seis` |
| Siglas | letra por letra fonética | `GHD` → `Yi eich di`, `DB` → `Di bi` |

---

## 5. Nombre del ejercicio en inglés (portada)

Para que el nombre en inglés **se entienda de verdad** se usan **dos voces**:

- Portada (`kind: "hook"`): el nombre lo dice **Kokoro `af_heart`** (inglés) y después sigue **Daniela** en español.
- `piper-tts.py` arma la línea con `{ en, text }` + `enVoice`: pausa de 0,35 s, fundido de 30 ms y volumen del
  inglés igualado al de Daniela (RMS).
- El `vo` del hook **debe empezar con el `name` exacto**: `"Hang Clean: ..."`. Lo que sigue a los dos puntos va a Daniela.
- Nombre con símbolos: `"nombreEnVoz": "Four six breathing"`. Nombre en castellano: `"nombreEn": false`.
- Con esto, en el hook **no** hace falta `pronuncia` ni `voSpeed 0.88` para el nombre (se ignoran). `pronuncia`
  sigue valiendo para las palabras en inglés que Daniela dice en el **resto** de las escenas.

---

## 6. Velocidad y claridad

- `"voiceSpeed": 1.0` en la ficha (global). Acelerar >1, bajar <1.
- Por escena: `"voSpeed": 0.88` baja solo esa línea (útil para frases con muchas palabras técnicas).
- Frases cortas (≤ ~130 caracteres por `vo`, unas 3 líneas de subtítulo): las largas se atropellan y desbordan el subtítulo.
- Una palabra difícil por frase como máximo: si hay dos, separarlas con coma.
- Puntuación = pausa. Una coma después de la palabra inglesa ayuda a que se oiga entera (`Kettlebell, swing`).

---

## 7. Procedimiento para encontrar la grafía correcta (probar, no adivinar)

1. Crear `videos/_pruebas-voz/<slug>/` (carpeta ignorada por git).
2. Escribir un `audio_request.json` con **varias variantes** de la misma palabra, una por línea:
   ```json
   { "voice": "es_AR-daniela-high", "speed": 1.0, "lines": [
     { "id": "a", "text": "Ketelbel" },
     { "id": "b", "text": "Kétol bel" },
     { "id": "c", "text": "Kételbel" }
   ] }
   ```
3. `python plantilla/piper-tts.py audio_request.json meta.json` → escuchar los `assets/voice/*.wav`.
4. Elegir la que suene clara (en este proyecto se llegaron a hacer 10–13 variantes por palabra difícil, p. ej. `burpee-broad-jump`).
5. Guardarla en `pronuncia` de la ficha. Probar **siempre con la frase completa**, no con la palabra aislada: en contexto cambia la entonación.
6. Si la misma palabra aparece en muchas fichas (kettlebell, dumbbell, clean, press, row, rack, wall ball…),
   **copiar el mismo diccionario a todas** para que el canal suene consistente. Mantener un diccionario maestro.

---

## 8. Diccionario base listo para copiar

```json
"pronuncia": {
  "Barbell Hang Clean": "Bárbel jang clin",
  "Kettlebell": "Ketelbel",   "kettlebell": "ketelbel",
  "Dumbbell": "Dámbel",       "dumbbell": "dámbel",
  "Barbell": "Bárbel",        "barbell": "bárbel",
  "Romanian": "Rrouméinian",
  "Reverse": "Rrivérs",
  "Ab Wheel": "ab güil",
  "rollout": "rolaut",
  "wall ball": "uál bol",
  "Deadlift": "Dedlift",      "deadlift": "dedlift",
  "Clean": "Clin",            "clean": "clin",
  "press": "pres",
  "row": "rou",
  "rack": "rac",
  "crunch": "cranch",
  "hollow": "jólou",
  "hang": "jang",
  "Hold": "Jold",             "hold": "jold",
  "squat": "escuat",
  "burpee": "burpii",
  "plank": "planc",
  "jerk": "yerk",
  "snatch": "snach",
  "Calf Raise": "kalf reis",
  "Weighted": "Uéited",       "weighted": "uéited",
  "Walking": "Uóquin",
  "Single-Leg": "Sínguel leg",
  "superman": "súperman",
  "Smith": "Esmit",
  "Sit-Up": "sit ap"
}
```

(Probar siempre en contexto: las entradas son las que usamos y aprobamos en este proyecto; ajustar según el oído.)

---

## 9. Checklist rápido antes de renderizar

- [ ] ¿Alguna palabra inglesa lleva `ll`? → pasarla a `l` o separarla.
- [ ] ¿Alguna palabra empieza con R? → `rr`.
- [ ] ¿Hay `wh`, `w`, `h`, `th`, `j`, `ee`? → ver tabla de la sección 4.
- [ ] ¿Está en `pronuncia` tanto la versión con mayúscula como con minúscula?
- [ ] ¿Las claves largas van antes que las cortas?
- [ ] ¿El hook empieza con el `name` exacto (para que entre Kokoro)?
- [ ] ¿Escuché el audio completo (no solo la palabra aislada)?
- [ ] ¿Subtítulo y descripción conservan el texto real (el reemplazo es solo de voz)?

---

## 10. Tecnología / instalación (por si el otro proyecto empieza de cero)

- `python -m pip install piper-tts kokoro-onnx`
- Modelo Daniela (114 MB, no va en git): `https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_AR/daniela/high/es_AR-daniela-high.onnx` (+ `.onnx.json`) → `plantilla/voces-piper/`
- Kokoro: `kokoro-v1.0.onnx` + `voices-v1.0.bin` en `plantilla/voces-kokoro/` o `~/.cache/hyperframes/tts/`
- Daniela es CC BY-SA 4.0 → hay que acreditarla en la descripción de YouTube; Kokoro es Apache 2.0.
- Edge TTS (Tomás/Elena es-AR) se descartó: Microsoft devuelve 403.
- Kokoro en español sonaba robótico; por eso Piper/Daniela para el castellano y Kokoro solo para el nombre inglés.
