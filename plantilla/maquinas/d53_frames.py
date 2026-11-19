# Dataset D77 Smith Bent Over Row: escenas + YouTube + miniatura.
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
    BEAM = S(200, -884); PAR = S(500, -640); STOP = S(500, -240)
    BAR_L = S(200, -255); BAR_U = S(200, -470); BAR_S = S(200, -355)
    SHO = S(192, -570); HIP = S(-50, -430); KNEE = S(81, -229)
    FOOT = S(60, 0); FOOT2 = S(-20, 0); BACK = S(70, -500)
    SCAP = S(150, -555); BACK_R = S(110, -480); LUMB = S(25, -508)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO EN", "LA SMITH"], "Espalda alta",
             "Remo inclinado en la Smith: la barra cuelga de los brazos y se tira al abdomen con la espalda recta.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes: el recorrido es siempre la misma vertical y los topes te marcan abajo.",
             [C("HINGE")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                            ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                            ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA", "BAJA"], "A las rodillas",
             "Bajá los topes y dejá la barra a la altura de las rodillas, con los ganchos libres por si tenés que soltarla.",
             [C("HINGE")], [ring(BAR_L, 62, 0.8), ring(STOP, 44, 2.0),
                            lab((60, 800), "BARRA Y TOPES", "start", 1.0),
                            lab((60, 880), "A LAS RODILLAS", "start", 2.2)], 7.2),
        step("AJUSTE 2 / 2", ["PIES AL", "ANCHO"], "Rodillas blandas",
             "Pies al ancho de la cadera, rodillas blandas y el peso repartido en todo el pie, sin levantar los talones.",
             [C("HINGE")], [ring(FOOT, 50, 0.8), ring(FOOT2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["INCLINADO", "ADELANTE"], "Espalda recta",
             "Inclinate desde la cadera con la espalda recta y el abdomen firme: la barra cuelga de los brazos a las rodillas.",
             [C("HINGE")], [ring(BACK, 62, 0.8), lab((60, 800), "ESPALDA RECTA", "start", 1.0)], 7.2),
        step("PASO 1 / 3", ["TIRÁ AL", "ABDOMEN"], "Codos atrás",
             "Paso uno. Tirá de la barra hacia el abdomen bajo llevando los codos hacia atrás, sin mover el torso.",
             [C("HINGE"), TO("PULL", 0.4, 1.0)], [ring(BAR_U, 60, 0.8), lab((60, 800), "AL ABDOMEN", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["JUNTÁ LAS", "ESCÁPULAS"], "Espalda alta",
             "Paso dos. Juntá las escápulas arriba y hacé una pausa de un segundo apretando la espalda alta.",
             [C("PULL"), TO("PULL", 0.2, 0.4)], [ring(SCAP, 58, 0.8), lab((60, 800), "ESCÁPULAS", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLANDO"], "Brazos estirados",
             "Paso tres. Bajá la barra controlando el recorrido hasta estirar los brazos, sin dejarla caer.",
             [C("PULL"), TO("HINGE", 0.5, 1.1)], [ring(BAR_L, 60, 0.8), lab((60, 800), "CONTROLÁ LA BAJADA", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al tirar",
             "Tomá aire al bajar la barra y soltalo al tirar. No aguantes la respiración en el esfuerzo.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["REDONDEAR", "LA ESPALDA"], "Espalda recta",
             "Error: redondear la espalda. La espalda queda recta de la cadera a la nuca y la mirada al frente.",
             [C("HINGE"), TO("ROUND_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BACK_R, 58, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TIRAR CON", "LA ESPALDA"], "Torso firme",
             "Error: usar la espalda baja y el balanceo. El torso no sube y baja: queda firme mientras tiran los brazos.",
             [C("HINGE"), TO("SWING_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(LUMB, 56, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["MEDIO", "RECORRIDO"], "Hasta el abdomen",
             "Error: medio recorrido. La barra llega al abdomen en cada repetición, sin quedarse a mitad de camino.",
             [C("HINGE"), TO("SHORT_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR_S, 58, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Espalda recta", "Barra al abdomen",
                                          "Escápulas juntas", "Bajada controlada"],
             "Tips: espalda recta, barra al abdomen, escápulas juntas y bajada controlada.",
             [C("HINGE"), seqloop("HINGE", "PULL", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Bisagra de cadera", "Torso firme",
                                    "Codos cerca del cuerpo", "Recorrido completo"],
             "Claves: bisagra de cadera, torso firme, codos cerca del cuerpo y recorrido completo.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Espalda alta y bíceps",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Peso moderado y técnica primero.",
             ["1 · TIRÁ", "2 · ESCÁPULAS", "3 · BAJÁ"], [C("HINGE"), seqloop("HINGE", "PULL", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN LOS TOPES"], "Sin apurarte",
             "Al terminar, dejá la barra en los topes y salí de la máquina enderezando el cuerpo sin apuro.",
             [C("PULL"), TO("HINGE", 0.9, 2.0)],
             [lab((60, 800), "SIN APURARTE", "start", 1.0)], 6.5),
    ]


YT77 = {
    "titulo": "Smith Bent Over Row 🔥 Remo inclinado en la Smith | Espalda",
    "tags": ["smith bent over row", "remo inclinado", "remo con barra", "smith machine", "multipower",
             "espalda alta", "dorsales", "bíceps", "gimnasio", "principiantes", "rutina de espalda",
             "remo en smith"],
    "descripcion": yt_desc("Smith Bent Over Row",
        "remo inclinado con barra guiada en la máquina Smith",
        "espalda alta y bíceps",
        "En la Smith la barra corre guiada en una sola vertical, así que el remo inclinado se vuelve más estable: el cuerpo hace la bisagra de cadera con la espalda recta y las rodillas blandas, la barra cuelga de los brazos a la altura de las rodillas y se tira al abdomen juntando las escápulas. El torso no se mueve: el trabajo lo hacen la espalda alta y los bíceps. Si redondeás la espalda, usás el balanceo o hacés medio recorrido, la zona lumbar y los codos se llevan la carga.",
        ["Ajustá la barra baja, a la altura de las rodillas, y los topes justo debajo.",
         "Pies al ancho de la cadera, rodillas blandas e inclinate desde la cadera."],
        ["Sujetá la barra con las manos un poco más abiertas que los hombros.",
         "Tirá de la barra hacia el abdomen bajo llevando los codos atrás.",
         "Juntá las escápulas arriba y hacé una pausa.",
         "Bajá la barra controlando el recorrido hasta estirar los brazos.",
         "Completá la serie y dejá la barra en los topes."],
        ["Redondear la espalda → espalda recta y mirada al frente.",
         "Tirar con la espalda baja → el torso queda firme.",
         "Medio recorrido → la barra llega al abdomen."],
        ["Espalda recta de la cadera a la nuca.", "Barra al abdomen, codos atrás.",
         "Escápulas juntas en cada repetición.", "Bajada controlada, sin soltar."],
        "Espalda → Espalda alta → Bíceps",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Espalda #Remo #SmithMachine #Dorsales #Biceps #Entrenamiento #Fuerza")}

save("smith-bent-over-row", row_scenes("smith-bent-over-row"),
     {"pose": "PULL", "zoom": 1.02, "dy": 20}, YT77)
