# Plan de revisión YouTube — pendientes para mañana (8-11-2026)

Estado al 7-11-2026: 84 de 89 largos programados (23-11 → 10-12-2026, 5/día a las 08:00, 11:00, 14:00, 17:00, 20:00 Uruguay). Registro en `programacion-largos-subidos.csv`, plan en `plan-programacion-largos.json`, calendario actualizado en `CALENDARIO-YOUTUBE.md` («Plan 2»).

Usar el Chrome `a64d121a-d083-4bd7-bb7a-529d2c201274` (ver memoria) y el canal FitLesUY. Procedimiento general en `SUBIR-A-YOUTUBE.md`.

> **Límite de Studio:** hoy salió «no puedes subir más miniaturas hoy, esperá 24 horas». Mañana, antes de empezar, comprobar que ya deja subir miniaturas (probar con la primera tarea). Si vuelve a bloquear, dejar las miniaturas para el final y hacer primero todo lo que no las necesita.

---

## 1. `barbell-hang-power-snatch` duplicado (prioridad alta)

Buscando «hang power snatch» aparecen **dos videos**:
- uno **público** (el que ya existía de antes), y
- uno **programado** para 28-11 08:00, ID `aRTNIC7zuOM` (subido en esta tanda, sin miniatura propia).

Hacer:
1. Abrir ambos en Studio y confirmar cuál es cuál (ID, visibilidad, fecha de subida) **antes de borrar nada**.
2. En el **público**: dejar título, descripción (con bloque FitLesUY), etiquetas y miniatura correctos según `salida/barbell-hang-power-snatch.youtube.txt`. Si la miniatura no se puede cambiar (Short), anotarlo.
3. **Eliminar el programado** (`aRTNIC7zuOM`). Borrado permanente: el usuario ya lo pidió, pero mostrar igual título + ID + estado antes de confirmar.
4. Registro: quitar/marcar la fila 26 de `programacion-largos-subidos.csv` y la de `CALENDARIO-YOUTUBE.md` (28-11 08:00 queda libre, o reprogramar ahí otro video pendiente).
5. Verificar que no haya otros duplicados: buscar en Studio por cada título de las 84 filas del CSV (o comparar la lista de Shorts contra el CSV y contra los IDs ya existentes en `CALENDARIO-YOUTUBE.md`). Comprobar en especial los videos que ya estaban en el calendario anterior.

## 2. Los 5 archivos grandes (> 10 MB) que subió el usuario

Quedaron **privados, sin miniatura ni descripción**. Revisar y completar cada uno:

| Video | Hueco previsto | Archivo |
|---|---|---|
| jump-rope | 25-11 08:00 | `salida/jump-rope.mp4` |
| rowing-machine | 28-11 20:00 | `salida/rowing-machine.mp4` |
| stair-climber | 02-12 20:00 | `salida/stair-climber.mp4` |
| lateral-shuffle | 04-12 20:00 | `salida/lateral-shuffle.mp4` |
| smith-machine-bench-press | 06-12 20:00 | `salida/smith-machine-bench-press.mp4` |

Para cada uno:
1. Localizarlo en Studio (Contenido → Privados) y anotar su ID.
2. Título, descripción y etiquetas desde `salida/<slug>.youtube.txt` (con bloque de la app FitLesUY).
3. Miniatura `salida/<slug>.miniatura.png` (si el límite diario aún bloquea, dejarlo para el final).
4. Público para menores: «No, no es contenido para niños».
5. Programar en el hueco previsto (hora Uruguay) y verificar fecha/hora en el diálogo.
6. Anotar el ID en `programacion-largos-subidos.csv` y pasar la fila de `CALENDARIO-YOUTUBE.md` a «programado».
7. Comprobar que el archivo subido es el correcto (duración y audio) y que el video no tiene restricciones de copyright ni de procesamiento.

## 3. Verificaciones de los ya programados

- `stability-ball-plate-crunch` (ID `vdTmJgkRDxg`): se ve bien programado para 9-12 14:00. Confirmar solo que título, descripción y etiquetas estén completos (Studio se colgó al programar).
- `squat-jump-to-plate` (ID `ZHZrUGQbp-c`, 27-11 20:00): se rehízo desde el borrador. Comprobar título, descripción, etiquetas, miniatura propia y fecha.
- `wide-negative-push-up` (ID `sC4SP_E4hmM`, 26-11 14:00): la terminó el usuario a mano; comprobar que la fecha quedó en 26-11 14:00 y que tiene miniatura.
- Miniaturas: confirmar en Studio cuáles de los 84 salieron sin miniatura propia (solo se sabe de `barbell-hang-power-snatch`) y subirlas cuando el límite lo permita.

## 4. Vincular cortos y largos (ambos sentidos)

Reglas: `SUBIR-A-YOUTUBE.md` §6 quater / quinquies. En el **largo**, agregar en la descripción `▶️ Mirá cómo se hace en segundos: https://youtu.be/<corto>` y en «Vídeo relacionado» el corto. En el **corto**, descripción con el link al largo y «Vídeo relacionado» = largo. Registrar en `vinculos.csv` y `BITACORA-VINCULOS.md`.

### 4a. Largos nuevos que ya tienen corto subido (10)

| Largo (ID) | Corto (ID) |
|---|---|
| supine-abdominal-stretch (Q1Y4gTliGvg) | SL0AP7npMWE |
| standing-biceps-stretch (GxmlOiwUfN8) | 4ECz6yYNwMo |
| wrist-extensor-stretch (iumHB3XlWJc) | a3xiwSKng5E |
| scapular-push-up (8aTVRhRq-q0) | ePh7xz0Nlos |
| kettlebell-good-morning-to-squat (ud1nn-hbH6o) | XvFrzwLFDQ8 |
| squat-thoracic-rotation (2tCeGqVlN5E) | nZsFBvDky0M |
| skierg (u33JaYJDA04) | cM5Hi-Wf0C0 |
| shuttle-run (EXqchRL6ok4) | sKjlsoE2ETQ |
| yoga-push-up (bQIk_XIu3cQ) | IhGQBMmrN-Q |
| kettlebell-farmer-carry (yOhuajdpUbg) | G-OWtWukGBk |

Nota: los largos están **programados**, no públicos. «Vídeo relacionado» desde el corto hacia un largo programado puede no dejarse elegir hasta que sea público. Si Studio no lo permite, dejar el link en la descripción del corto y completar el «Vídeo relacionado» el día que el largo pase a público (ver 4b).

### 4b. Cortos ya públicos cuyo largo aún no es público

Pendientes del lado corto → largo («Vídeo relacionado»), cuando el largo se publique: cat-cow, sled-push-pull, russian-twist, kettlebell-good-morning, barbell-power-snatch, snatch-high-pull, barbell-thruster, y los que figuren como `pendiente` en `vinculos.csv`. Revisar `vinculos.csv` y filtrar `largo_en_corto` / `corto_en_largo` = `pendiente`.

### 4c. Cortos futuros

Para los demás largos nuevos (74 sin corto) no hay nada que vincular todavía; al subir cada corto nuevo se vincula en el momento.

## 5. Orden sugerido para mañana

1. Probar si ya deja subir miniaturas.
2. Duplicado `barbell-hang-power-snatch` (punto 1).
3. Los 5 grandes (punto 2).
4. Verificaciones (punto 3).
5. Vinculación (punto 4a; luego 4b según el estado).
6. Actualizar `CALENDARIO-YOUTUBE.md`, `programacion-largos-subidos.csv`, `vinculos.csv`, `BITACORA-VINCULOS.md` y commitear (solo cuando el usuario lo pida).
