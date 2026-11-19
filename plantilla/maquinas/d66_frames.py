# Dataset D90 Smith Rear Delt Row: escenas + YouTube + miniatura.
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
    BAR_L = S(200, -303); BAR_U = S(200, -515); BAR_S = S(200, -410)
    SHO = S(168, -632); LUMB = S(-5, -470); BACK = S(120, -520)
    SCAP = S(175, -600); WRIST = S(200, -303); ELBOW = S(*J["PULL"]["E"])
    return [
        hook("GIMNASIO · ESPALDA", ["REMO", "ABIERTO"], "Deltoide posterior",
             "Smith Rear Delt Row: remo abierto en la barra guiada para la parte de atrás del hombro.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.1, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Recorrido fijo",
             "La barra corre entre los parantes en una sola vertical: el torso se queda quieto y el recorrido es siempre el mismo.",
             [C("HINGE")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                            ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                            ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A", "LAS RODILLAS"], "Altura baja",
             "Dejá la barra a la altura de las rodillas y los topes justo debajo, para que puedas soltarla si hace falta.",
             [C("HINGE")], [ring(BAR_L, 62, 0.8), ring(STOP, 44, 2.0),
                            lab((60, 800), "BARRA Y TOPES", "start", 1.0),
                            lab((60, 880), "A LAS RODILLAS", "start", 2.2)], 7.2),
        step("AJUSTE 2 / 2", ["AGARRE", "ABIERTO"], "Manos anchas",
             "Agarrá la barra con las manos más anchas que los hombros, palmas hacia abajo y muñecas firmes.",
             [C("HINGE")], [ring(WRIST, 52, 0.8), lab((60, 800), "AGARRE ABIERTO", "start", 0.8)], 7.2),
        step("POSICIÓN INICIAL", ["INCLINADO", "ADELANTE"], "Espalda recta",
             "Inclinate desde la cadera con la espalda recta y las rodillas blandas. La barra cuelga de los brazos a la altura de las rodillas.",
             [C("HINGE")], [ring(BACK, 60, 0.8), lab((60, 800), "ESPALDA RECTA", "start", 1.0)], 7.2),
        step("PASO 1 / 3", ["TIRÁ AL", "PECHO ALTO"], "Codos afuera",
             "Paso uno. Tirá la barra al pecho alto abriendo los codos hacia afuera, a la altura de los hombros.",
             [C("HINGE"), TO("PULL", 0.4, 1.0)], [ring(BAR_U, 58, 0.8), lab((60, 800), "AL PECHO ALTO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRETÁ", "ATRÁS"], "Pausa arriba",
             "Paso dos. Hacé una pausa corta apretando la parte de atrás del hombro, sin encoger el cuello.",
             [C("PULL"), TO("PULL", 0.2, 0.4)], [ring(SCAP, 56, 0.8), lab((60, 800), "DELTOIDE POSTERIOR", "start", 1.0)], 7.2),
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
        step("ASÍ NO · 2 / 3", ["ENCOGER", "LOS HOMBROS"], "Cuello largo",
             "Error: encogerse de hombros. El cuello queda largo: el trabajo lo hace el deltoide posterior.",
             [C("HINGE"), TO("SHRUG_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(SHO, 58, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TIRAR CON", "EL CUERPO"], "Torso quieto",
             "Error: enderezar el torso para tirar. El torso queda firme y el peso lo mueve la espalda, no el balanceo.",
             [C("HINGE"), TO("SWING_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(LUMB, 56, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Agarre abierto", "Codos afuera",
                                          "Espalda recta", "Pecho alto"],
             "Tips: agarre abierto, codos afuera, espalda recta y la barra al pecho alto.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Manos anchas", "Bisagra de cadera",
                                     "Codos a la altura del hombro", "Bajada controlada"],
             "Claves: manos anchas, bisagra de cadera, codos a la altura del hombro y bajada controlada.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 12–15"], "Deltoide posterior y espalda alta",
             "Tres series de doce a quince repeticiones, con un minuto de pausa. Priorizá el recorrido corto y limpio.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · BAJÁ"], [C("HINGE"), seqloop("HINGE", "PULL", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN LOS TOPES"], "Sin apuro",
             "Al terminar, dejá la barra en los topes y enderezate despacio, sin soltar la espalda de golpe.",
             [C("PULL"), TO("HINGE", 0.9, 2.0)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT90 = {
    "titulo": "Smith Rear Delt Row 🔥 Remo abierto para hombro | Espalda",
    "tags": ["smith rear delt row", "remo abierto", "deltoide posterior", "hombro posterior", "remo en smith",
             "smith machine", "multipower", "espalda alta", "trapecio", "gimnasio", "principiantes",
             "rutina de espalda"],
    "descripcion": yt_desc("Smith Rear Delt Row",
        "remo abierto con la barra guiada para el deltoide posterior",
        "deltoide posterior y espalda alta",
        "El remo abierto en la Smith trabaja la parte de atrás del hombro. El torso queda más alto que en un remo común, el agarre es ancho y los codos salen hacia afuera a la altura de los hombros. La barra se tira al pecho alto con un recorrido corto, así el deltoide posterior y la espalda alta hacen el trabajo y el dorsal participa menos. Los errores típicos son redondear la espalda, encogerse de hombros y enderezar el torso para tirar.",
        ["Dejá la barra a la altura de las rodillas y los topes justo debajo.",
         "Pies al ancho de la cadera, rodillas blandas e inclinate desde la cadera."],
        ["Agarrá la barra más ancho que los hombros, palmas hacia abajo.",
         "Tirá la barra al pecho alto abriendo los codos hacia afuera.",
         "Hacé una pausa corta apretando la parte de atrás del hombro.",
         "Bajá controlando hasta estirar los brazos.",
         "Dejá la barra en los topes al terminar."],
        ["Redondear la espalda → espalda recta y mirada al frente.",
         "Encoger los hombros → cuello largo y hombros abajo.",
         "Tirar con el cuerpo → el torso queda firme."],
        ["Agarre abierto, más ancho que los hombros.", "Codos afuera, a la altura del hombro.",
         "La barra sube al pecho alto.", "Bajada controlada hasta estirar."],
        "Espalda → Deltoide posterior → Espalda alta → Trapecio",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Espalda #DeltoidePosterior #SmithMachine #Hombro #Remo #Entrenamiento #Fuerza")}

save("smith-rear-delt-row", row_scenes("smith-rear-delt-row"),
     {"pose": "PULL", "zoom": 1.02, "dy": 20}, YT90)
