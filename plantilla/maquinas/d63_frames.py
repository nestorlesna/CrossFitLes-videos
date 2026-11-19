# Dataset D87 Smith Narrow Row: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def row_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(200, -884); PAR = S(500, -620); STOP = S(500, -260)
    BAR_L = S(200, -295); BAR_U = S(200, -500); BAR_S = S(200, -380)
    SHO = S(174, -625); LUMB = S(0, -470); BACK = S(120, -520)
    SCAP = S(180, -600); WRIST = S(200, -295); ELBOW = S(*J["PULL"]["E"])
    return [
        hook("GIMNASIO · ESPALDA", ["REMO", "ESTRECHO"], "Manos juntas",
             "Smith Narrow Row: remo estrecho en la barra guiada, con las manos juntas y los codos pegados al cuerpo.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.1, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Recorrido fijo",
             "La barra corre entre los parantes en una sola vertical: no peleás con el equilibrio y el recorrido es siempre el mismo.",
             [C("HINGE")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                            ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                            ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A", "LAS RODILLAS"], "Altura baja",
             "Dejá la barra a la altura de las rodillas y los topes justo debajo, para que puedas soltarla si hace falta.",
             [C("HINGE")], [ring(BAR_L, 62, 0.8), ring(STOP, 44, 2.0),
                            lab((60, 800), "BARRA Y TOPES", "start", 1.0),
                            lab((60, 880), "A LAS RODILLAS", "start", 2.2)], 7.2),
        step("AJUSTE 2 / 2", ["AGARRE", "ESTRECHO"], "Manos juntas",
             "Agarrá la barra con las manos juntas, a menos de un palmo entre una y otra, y las palmas hacia abajo.",
             [C("HINGE")], [ring(WRIST, 52, 0.8), lab((60, 800), "AGARRE ESTRECHO", "start", 0.8)], 7.2),
        step("POSICIÓN INICIAL", ["INCLINADO", "ADELANTE"], "Espalda recta",
             "Inclinate desde la cadera con la espalda recta y las rodillas blandas. La barra cuelga de los brazos a la altura de las rodillas.",
             [C("HINGE")], [ring(BACK, 60, 0.8), lab((60, 800), "ESPALDA RECTA", "start", 1.0)], 7.2),
        step("PASO 1 / 3", ["TIRÁ AL", "ESTERNÓN"], "Codos al cuerpo",
             "Paso uno. Tirá la barra al esternón con los codos pegados al cuerpo, sin despegar los brazos del torso.",
             [C("HINGE"), TO("PULL", 0.4, 1.0)], [ring(BAR_U, 58, 0.8), lab((60, 800), "AL ESTERNÓN", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRETÁ LA", "ESPALDA"], "Pausa arriba",
             "Paso dos. Juntá las escápulas arriba y hacé una pausa corta apretando la espalda alta, sin subir los hombros.",
             [C("PULL"), TO("PULL", 0.2, 0.4)], [ring(SCAP, 56, 0.8), lab((60, 800), "ESCÁPULAS", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLANDO"], "Brazos estirados",
             "Paso tres. Bajá la barra controlando el recorrido hasta estirar los brazos, sin dejarla caer ni perder la espalda recta.",
             [C("PULL"), TO("HINGE", 0.5, 1.1)], [ring(BAR_L, 58, 0.8), lab((60, 800), "CONTROLÁ LA BAJADA", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al tirar",
             "Tomá aire cuando la barra baja y soltalo al tirar. No aguantes el aire ni pierdas la posición del torso.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["REDONDEAR", "LA ESPALDA"], "Espalda recta",
             "Error: redondear la espalda. Mantenela recta de la cadera a la nuca y la mirada al frente, sin bajar la cabeza.",
             [C("HINGE"), TO("ROUND_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BACK, 58, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TIRAR CON", "EL CUERPO"], "Torso quieto",
             "Error: enderezar el torso para tirar. El torso queda firme y el peso lo mueve la espalda, no el balanceo.",
             [C("HINGE"), TO("SWING_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(LUMB, 56, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["MEDIO", "RECORRIDO"], "Hasta el esternón",
             "Error: cortar el recorrido. La barra llega al esternón en cada repetición y baja hasta estirar los brazos.",
             [C("HINGE"), TO("SHORT_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR_S, 58, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Manos juntas", "Codos al cuerpo",
                                          "Espalda recta", "Al esternón"],
             "Tips: manos juntas, codos al cuerpo, espalda recta y la barra al esternón.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Agarre estrecho", "Bisagra de cadera",
                                    "Escápulas juntas", "Bajada controlada"],
             "Claves: agarre estrecho, bisagra de cadera, escápulas juntas y bajada controlada.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Espalda alta y dorsal",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Empezá liviano y priorizá la técnica.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · BAJÁ"], [C("HINGE"), seqloop("HINGE", "PULL", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN LOS TOPES"], "Sin apuro",
             "Al terminar, dejá la barra en los topes y enderezate despacio, sin soltar la espalda de golpe.",
             [C("PULL"), TO("HINGE", 0.9, 2.0)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT87 = {
    "titulo": "Smith Narrow Row 🔥 Remo estrecho en la Smith | Espalda",
    "tags": ["smith narrow row", "remo estrecho", "remo en smith", "remo con barra", "smith machine",
             "multipower", "espalda alta", "dorsales", "bíceps", "gimnasio", "principiantes",
             "rutina de espalda"],
    "descripcion": yt_desc("Smith Narrow Row",
        "remo estrecho con la barra guiada de la máquina Smith",
        "espalda alta y dorsal",
        "El remo estrecho en la Smith es un remo inclinado con las manos juntas y los codos pegados al cuerpo. La barra guiada corre en una sola vertical, así que el torso puede quedarse más alto y quieto mientras la espalda alta y el dorsal hacen el trabajo. La barra sube al esternón, no al abdomen, y el recorrido corto y pegado hace que los hombros ayuden menos. Los errores típicos son redondear la espalda, enderezar el torso para tirar y cortar el recorrido.",
        ["Dejá la barra a la altura de las rodillas y los topes justo debajo.",
         "Pies al ancho de la cadera, rodillas blandas e inclinate desde la cadera."],
        ["Agarrá la barra con las manos juntas, palmas hacia abajo.",
         "Tirá la barra al esternón con los codos pegados al cuerpo.",
         "Juntá las escápulas arriba y hacé una pausa corta.",
         "Bajá controlando hasta estirar los brazos.",
         "Dejá la barra en los topes al terminar."],
        ["Redondear la espalda → espalda recta y mirada al frente.",
         "Enderezar el torso para tirar → el torso queda firme.",
         "Cortar el recorrido → la barra llega al esternón."],
        ["Manos juntas, a menos de un palmo.", "Codos pegados al cuerpo.",
         "La barra sube al esternón.", "Bajada controlada hasta estirar."],
        "Espalda → Espalda alta → Dorsal → Bíceps",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Espalda #RemoEstrecho #SmithMachine #Dorsales #Biceps #Entrenamiento #Fuerza")}

save("smith-narrow-row", row_scenes("smith-narrow-row"),
     {"pose": "PULL", "zoom": 1.02, "dy": 20}, YT87)
