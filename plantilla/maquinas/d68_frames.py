# Dataset D92 Smith Reverse Grip Bent Over Row: escenas + YouTube + miniatura.
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
    BEAM = S(200, -868); PAR = S(500, -620); STOP = S(500, -260)
    BAR_L = S(200, -255); BAR_U = S(200, -460); BAR_S = S(200, -370)
    LUMB = S(20, -460); BACK = S(90, -520); SCAP = S(180, -545)
    WRIST = S(200, -255); ELBOW = S(*J["PULL"]["E"])
    return [
        hook("GIMNASIO · ESPALDA", ["REMO", "SUPINO"], "Palmas arriba",
             "Smith Reverse Grip Bent Over Row: remo inclinado con agarre supino en la barra guiada.",
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
        step("AJUSTE 2 / 2", ["AGARRE", "SUPINO"], "Palmas arriba",
             "Agarrá la barra con las palmas hacia arriba y las manos al ancho de los hombros, con las muñecas firmes.",
             [C("HINGE")], [ring(WRIST, 52, 0.8), lab((60, 800), "PALMAS ARRIBA", "start", 0.8)], 7.2),
        step("POSICIÓN INICIAL", ["INCLINADO", "ADELANTE"], "Espalda recta",
             "Inclinate desde la cadera con la espalda recta y las rodillas blandas. La barra cuelga de los brazos a la altura de las rodillas.",
             [C("HINGE")], [ring(BACK, 60, 0.8), lab((60, 800), "ESPALDA RECTA", "start", 1.0)], 7.2),
        step("PASO 1 / 3", ["TIRÁ AL", "ABDOMEN"], "Codos pegados",
             "Paso uno. Tirá la barra al abdomen bajo con los codos pegados al cuerpo, sin separarla del torso.",
             [C("HINGE"), TO("PULL", 0.4, 1.0)], [ring(BAR_U, 58, 0.8), lab((60, 800), "AL ABDOMEN BAJO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRETÁ", "ARRIBA"], "Pausa corta",
             "Paso dos. Apretá la espalda y el bíceps arriba con una pausa corta, sin subir los hombros ni mover el torso.",
             [C("PULL"), TO("PULL", 0.2, 0.4)], [ring(SCAP, 56, 0.8), lab((60, 800), "APRETÁ LA ESPALDA", "start", 1.0)], 7.2),
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
        step("ASÍ NO · 3 / 3", ["MEDIO", "RECORRIDO"], "Hasta el abdomen",
             "Error: cortar el recorrido. La barra llega al abdomen bajo en cada repetición y baja hasta estirar los brazos.",
             [C("HINGE"), TO("SHORT_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR_S, 58, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Palmas arriba", "Codos pegados",
                                          "Espalda recta", "Al abdomen"],
             "Tips: palmas arriba, codos pegados, espalda recta y la barra al abdomen bajo.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Agarre supino", "Bisagra de cadera",
                                     "Codos al cuerpo", "Bajada controlada"],
             "Claves: agarre supino, bisagra de cadera, codos al cuerpo y bajada controlada.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 8–12"], "Dorsal, espalda alta y bíceps",
             "Tres series de ocho a doce repeticiones, con un minuto de pausa. Empezá liviano y priorizá la técnica.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · BAJÁ"], [C("HINGE"), seqloop("HINGE", "PULL", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN LOS TOPES"], "Sin apuro",
             "Al terminar, dejá la barra en los topes y enderezate despacio, sin soltar la espalda de golpe.",
             [C("PULL"), TO("HINGE", 0.9, 2.0)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT92 = {
    "titulo": "Smith Reverse Grip Bent Over Row 🔥 Remo supino | Espalda",
    "tags": ["smith reverse grip bent over row", "remo supino", "remo agarre invertido", "remo inclinado",
             "smith machine", "multipower", "dorsales", "bíceps", "espalda alta", "gimnasio", "principiantes",
             "rutina de espalda"],
    "descripcion": yt_desc("Smith Reverse Grip Bent Over Row",
        "remo inclinado con agarre supino en la máquina Smith",
        "dorsal, espalda alta y bíceps",
        "El remo con agarre supino en la Smith se hace inclinado, con las palmas hacia arriba y los codos pegados al cuerpo. La barra se tira al abdomen bajo con un recorrido corto y pegado: el agarre supino suma trabajo de bíceps y espalda alta, y el torso casi horizontal hace que el dorsal se estire y se contraiga de punta a punta. Los errores típicos son redondear la espalda, enderezar el torso para tirar y cortar el recorrido.",
        ["Dejá la barra a la altura de las rodillas y los topes justo debajo.",
         "Pies al ancho de la cadera, rodillas blandas e inclinate desde la cadera."],
        ["Agarrá la barra con las palmas hacia arriba, manos al ancho de los hombros.",
         "Tirá la barra al abdomen bajo con los codos pegados.",
         "Apretá la espalda y el bíceps arriba con una pausa corta.",
         "Bajá controlando hasta estirar los brazos.",
         "Dejá la barra en los topes al terminar."],
        ["Redondear la espalda → espalda recta y mirada al frente.",
         "Enderezar el torso para tirar → el torso queda firme.",
         "Cortar el recorrido → la barra llega al abdomen bajo."],
        ["Palmas arriba, manos al ancho de los hombros.", "Codos pegados al cuerpo.",
         "La barra sube al abdomen bajo.", "Bajada controlada hasta estirar."],
        "Espalda → Dorsal → Espalda alta → Bíceps",
        "3 series de 8–12 repeticiones, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Espalda #RemoSupino #SmithMachine #Dorsales #Biceps #Entrenamiento #Fuerza")}

save("smith-reverse-grip-bent-over-row", row_scenes("smith-reverse-grip-bent-over-row"),
     {"pose": "PULL", "zoom": 1.02, "dy": 20}, YT92)
