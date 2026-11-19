# Dataset D76 Smith Bent Knee Good Morning: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def gm_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(0, -884); PAR = S(300, -640); STOP = S(300, -560)
    BAR = S(0, -726); BAR_D = S(0, -597); BACK = S(25, -600); BACK_R = S(150, -520)
    HIP = S(10, -462); HIP_D = S(-20, -430); KNEE = S(71, -230); KNEE_D = S(106, -225)
    KNEE_S = S(14, -225); HEAD = S(40, -772); HEAD_D = S(233, -485)
    FOOT = S(60, 0); FOOT2 = S(-20, 0)
    return [
        hook("GIMNASIO · PIERNAS", ["BUENOS DÍAS", "EN LA SMITH"], "Bisagra de cadera",
             "Buenos días con rodillas semiflexionadas en la Smith: la barra en la espalda, la cola atrás y el cuerpo se dobla desde la cadera.",
             [C("UP"), seqloop("UP", "DOWN", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes y los topes te dejan la salida de seguridad a la altura de la cadera.",
             [C("UP")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                         ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                         ring(STOP, 46, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA EN", "LA ESPALDA"], "Sobre los trapecios",
             "Apoyá la barra sobre los trapecios, agarrá con las manos a los costados y sacala de los ganchos.",
             [C("UP")], [ring(BAR, 66, 0.8), lab((60, 800), "BARRA EN LA ESPALDA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES AL", "ANCHO"], "Rodillas blandas",
             "Parate con los pies al ancho de la cadera, las puntas al frente y las rodillas apenas flexionadas.",
             [C("UP")], [ring(FOOT, 50, 0.8), ring(FOOT2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["DE PIE", "DERECHO"], "Espalda recta",
             "Arrancá de pie, con la espalda recta, el abdomen firme y la mirada al frente.",
             [C("UP")], [ring(BACK, 60, 0.8), lab((60, 800), "ESPALDA RECTA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["LLEVÁ LA", "COLA ATRÁS"], "Bisagra de cadera",
             "Paso uno. Llevá la cola hacia atrás doblando el cuerpo desde la cadera, con las rodillas blandas.",
             [C("UP"), TO("DOWN", 0.4, 1.0)], [ring(HIP_D, 56, 0.8), lab((60, 800), "COLA ATRÁS", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["RODILLAS", "BLANDAS"], "Sin trabarlas",
             "Paso dos. Mantené las rodillas semiflexionadas y la espalda recta en todo el recorrido.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(KNEE_D, 50, 0.8), lab((1030, 900), "RODILLAS BLANDAS", "end", 1.0)], 7.2),
        step("PASO 3 / 3", ["SUBÍ", "APRETANDO"], "Isquios y glúteo",
             "Paso tres. Subí empujando con los talones y apretando los isquios y el glúteo, sin arquear la espalda.",
             [C("DOWN"), TO("UP", 0.5, 1.1)], [ring(HIP, 56, 0.8), lab((60, 800), "SUBÍ APRETANDO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire cuando bajás y soltalo cuando subís. No aguantes el aire abajo.",
             [C("UP"), seqloop("UP", "DOWN", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["TRABAR", "LAS RODILLAS"], "Rodillas blandas",
             "Error: trabar las rodillas y doblar solo la cintura. Las rodillas quedan semiflexionadas y el movimiento sale de la cadera.",
             [C("UP"), TO("STIFF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(KNEE_S, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["REDONDEAR", "LA ESPALDA"], "Espalda recta",
             "Error: redondear la espalda y bajar la cabeza. La espalda queda recta y la mirada al frente.",
             [C("UP"), TO("ROUND_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BACK_R, 60, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["BAJAR", "DEMASIADO"], "Hasta donde llegás",
             "Error: bajar más allá de donde controlás. Bajá hasta sentir el estiramiento sin perder la espalda recta.",
             [C("UP"), TO("DEEP_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HEAD_D, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra sobre los trapecios", "Cola atrás",
                                         "Rodillas blandas", "Subí apretando"],
             "Tips: barra sobre los trapecios, cola atrás, rodillas blandas y subí apretando isquios y glúteo.",
             [C("UP"), seqloop("UP", "DOWN", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda recta", "Sin trabar las rodillas",
                                    "Mirada al frente", "Subida controlada"],
             "Claves: espalda recta, sin trabar las rodillas, mirada al frente y subida controlada.",
             [{"cut": "DOWN", "at": 0.1}]),
        reps(["3 X 10–12"], "Isquios y glúteo",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Peso moderado y el recorrido que controlás.",
             ["1 · COLA ATRÁS", "2 · RODILLAS", "3 · SUBÍ"], [C("UP"), seqloop("UP", "DOWN", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ", "LA BARRA"], "Sin apurarse",
             "Al terminar la serie, subí derecho, dejá la barra en los ganchos y salí de la máquina sin encorvarte.",
             [C("DOWN"), TO("UP", 0.9, 2.0)],
             [lab((60, 800), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT76 = {
    "titulo": "Smith Bent Knee Good Morning 🔥 Buenos días en la Smith | Gimnasio",
    "tags": ["smith bent knee good morning", "buenos días", "good morning", "smith machine", "multipower",
             "isquios", "isquiotibiales", "glúteo", "espalda baja", "gimnasio", "principiantes",
             "rutina de piernas"],
    "descripcion": yt_desc("Smith Bent Knee Good Morning",
        "buenos días con rodillas semiflexionadas en la máquina Smith",
        "isquiotibiales y glúteo",
        "En la Smith la barra va guiada sobre los trapecios y el cuerpo se dobla desde la cadera con las rodillas blandas: los isquios y el glúteo hacen el trabajo mientras la espalda se mantiene recta. Es un ejercicio de bisagra, no de sentadilla: la cola va atrás y el pecho baja. Si trabás las rodillas, redondeás la espalda o bajás de más, la zona lumbar se lleva la carga.",
        ["Apoyá la barra sobre los trapecios y sacala de los ganchos.",
         "Parate con los pies al ancho de la cadera y las rodillas blandas."],
        ["Llevá la cola hacia atrás doblando el cuerpo desde la cadera.",
         "Mantené las rodillas semiflexionadas y la espalda recta.",
         "Bajá hasta sentir el estiramiento de los isquios.",
         "Subí empujando con los talones y apretando glúteo.",
         "Completá la serie y dejá la barra en los ganchos."],
        ["Trabar las rodillas → rodillas semiflexionadas.",
         "Redondear la espalda → espalda recta y mirada al frente.",
         "Bajar demasiado → bajá hasta donde controlás."],
        ["Barra sobre los trapecios.", "Cola atrás, no sentadilla.",
         "Rodillas blandas todo el recorrido.", "Subida controlada."],
        "Piernas → Isquios → Glúteo",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Isquios #Gluteo #SmithMachine #BuenosDias #Piernas #Entrenamiento #Fuerza")}

save("smith-bent-knee-good-morning", gm_scenes("smith-bent-knee-good-morning"),
     {"pose": "DOWN", "zoom": 1.02, "dy": 20}, YT76)
