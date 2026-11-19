# Dataset D88 Smith One Arm Row: escenas + YouTube + miniatura.
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
    BEAM = S(200, -884); PAR = S(500, -620); STOP = S(500, -250)
    BAR_L = S(200, -300); BAR_U = S(200, -465); BAR_S = S(200, -385)
    SHO = S(192, -588); LUMB = S(0, -470); BACK = S(130, -500)
    SCAP = S(195, -560); HIP = S(-45, -440); WRIST = S(200, -300)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO A", "UNA MANO"], "Un brazo por vez",
             "Smith One Arm Row: remo a una mano en la barra guiada, con el torso inclinado y el dorsal trabajando solo.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.1, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Recorrido fijo",
             "La barra corre entre los parantes en una sola vertical: el recorrido es siempre el mismo y no tenés que pelear con el equilibrio.",
             [C("HINGE")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                            ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                            ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A", "LAS RODILLAS"], "Altura baja",
             "Dejá la barra a la altura de las rodillas y los topes debajo, para que puedas soltarla si te falta fuerza.",
             [C("HINGE")], [ring(BAR_L, 62, 0.8), ring(STOP, 44, 2.0),
                            lab((60, 800), "BARRA Y TOPES", "start", 1.0),
                            lab((60, 880), "A LAS RODILLAS", "start", 2.2)], 7.2),
        step("AJUSTE 2 / 2", ["PIES", "ESCALONADOS"], "Un pie adelante",
             "Poné un pie adelante y otro atrás, con las rodillas blandas y el peso repartido. Así el torso queda estable.",
             [C("HINGE")], [ring(S(85, 0), 50, 0.8), lab((60, 800), "UN PIE ADELANTE", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["INCLINADO", "ADELANTE"], "Una mano en la barra",
             "Inclinate desde la cadera con la espalda recta. Una mano toma la barra y la otra queda libre, colgando.",
             [C("HINGE")], [ring(SHO, 52, 0.8), lab((60, 800), "ESPALDA RECTA", "start", 1.0),
                            lab((60, 880), "MANO LIBRE", "start", 2.2)], 7.4),
        step("PASO 1 / 3", ["TIRÁ A", "LA CADERA"], "Codo atrás",
             "Paso uno. Tirá la barra hacia la cadera llevando el codo hacia atrás, sin girar ni enderezar el torso.",
             [C("HINGE"), TO("PULL", 0.4, 1.0)], [ring(BAR_U, 58, 0.8), lab((60, 800), "A LA CADERA", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRETÁ EL", "DORSAL"], "Pausa arriba",
             "Paso dos. Apretá el dorsal arriba y hacé una pausa corta, sin subir el hombro ni abrir el codo.",
             [C("PULL"), TO("PULL", 0.2, 0.4)], [ring(SCAP, 54, 0.8), lab((60, 800), "APRETÁ EL DORSAL", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLANDO"], "Brazo estirado",
             "Paso tres. Bajá la barra controlando hasta estirar el brazo, sin dejarla caer ni perder la espalda recta.",
             [C("PULL"), TO("HINGE", 0.5, 1.1)], [ring(BAR_L, 58, 0.8), lab((60, 800), "CONTROLÁ LA BAJADA", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al tirar",
             "Tomá aire abajo y soltalo al tirar. No aguantes el aire ni pierdas la posición inclinada del torso.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["REDONDEAR", "LA ESPALDA"], "Espalda recta",
             "Error: redondear la espalda. Mantenela recta de la cadera a la nuca y la mirada al frente, sin bajar la cabeza.",
             [C("HINGE"), TO("ROUND_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BACK, 58, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TIRAR CON", "EL CUERPO"], "Torso quieto",
             "Error: enderezar el torso para tirar. El torso queda quieto y el peso lo mueve el dorsal, no el balanceo.",
             [C("HINGE"), TO("SWING_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(LUMB, 56, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["MEDIO", "RECORRIDO"], "Hasta la cadera",
             "Error: cortar el recorrido. La barra llega a la cadera en cada repetición y baja hasta estirar el brazo.",
             [C("HINGE"), TO("SHORT_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR_S, 58, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pies escalonados", "Codo atrás",
                                          "Sin girar el torso", "Hasta la cadera"],
             "Tips: pies escalonados, codo atrás, sin girar el torso y la barra hasta la cadera.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Bisagra de cadera", "Un brazo por vez",
                                    "Dorsal apretado", "Bajada controlada"],
             "Claves: bisagra de cadera, un brazo por vez, dorsal apretado y bajada controlada.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Dorsal y espalda alta",
             "Tres series de diez a doce repeticiones por brazo, con un minuto de pausa. Cambiá de lado al terminar la serie.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · BAJÁ"], [C("HINGE"), seqloop("HINGE", "PULL", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN LOS TOPES"], "Sin apuro",
             "Al terminar, dejá la barra en los topes y enderezate despacio, sin soltar la espalda de golpe.",
             [C("PULL"), TO("HINGE", 0.9, 2.0)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT88 = {
    "titulo": "Smith One Arm Row 🔥 Remo a una mano en la Smith | Espalda",
    "tags": ["smith one arm row", "remo a una mano", "remo unilateral", "remo en smith", "smith machine",
             "multipower", "dorsal", "espalda alta", "bíceps", "gimnasio", "principiantes",
             "rutina de espalda"],
    "descripcion": yt_desc("Smith One Arm Row",
        "remo a una mano con la barra guiada de la máquina Smith",
        "dorsal y espalda alta",
        "El remo a una mano en la Smith permite trabajar un lado por vez con la barra guiada, así que el torso queda más quieto y el recorrido no se desvía. Con los pies escalonados y la cadera hacia atrás, una sola mano tira de la barra hacia la cadera mientras la otra cuelga libre. El dorsal y la espalda alta trabajan con más recorrido y el bíceps ayuda al final. Los errores típicos son redondear la espalda, enderezar el torso para tirar y cortar el recorrido.",
        ["Dejá la barra a la altura de las rodillas y los topes justo debajo.",
         "Poné un pie adelante y otro atrás, con las rodillas blandas."],
        ["Inclinate desde la cadera con la espalda recta.",
         "Agarrá la barra con una mano y dejá la otra libre.",
         "Tirá la barra hacia la cadera llevando el codo atrás.",
         "Apretá el dorsal arriba y hacé una pausa corta.",
         "Bajá controlando hasta estirar el brazo y cambiá de lado."],
        ["Redondear la espalda → espalda recta y mirada al frente.",
         "Enderezar el torso para tirar → el torso queda quieto.",
         "Cortar el recorrido → la barra llega a la cadera."],
        ["Pies escalonados para mayor estabilidad.", "Codo hacia atrás, pegado al cuerpo.",
         "No gires el torso: un lado por vez.", "Bajada controlada hasta estirar."],
        "Espalda → Dorsal → Espalda alta → Bíceps",
        "3 series de 10–12 repeticiones por brazo, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Espalda #RemoUnaMano #SmithMachine #Dorsal #Biceps #Entrenamiento #Fuerza")}

save("smith-one-arm-row", row_scenes("smith-one-arm-row"),
     {"pose": "PULL", "zoom": 1.02, "dy": 20}, YT88)
