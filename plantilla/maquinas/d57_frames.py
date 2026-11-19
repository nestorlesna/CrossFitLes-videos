# Dataset D81 Smith Full Squat: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def fq_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(0, -884); PAR = S(300, -640); STOP = S(300, -520)
    BAR = S(0, -726); BAR_D = S(0, -447)
    HIP = S(10, -462); HIP_D = S(-55, -215); HIP_H = S(0, -350)
    KNEE = S(71, -230); KNEE_D = S(184, -194); BACK = S(30, -600)
    FOOT = S(60, 0); FOOT2 = S(-20, 0); HEAD_L = S(193, -387)
    return [
        hook("GIMNASIO · PIERNAS", ["SENTADILLA", "COMPLETA"], "Hasta el fondo",
             "Sentadilla completa en la Smith: bajás hasta el fondo con los talones apoyados y el torso derecho.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.5, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes y los topes te dejan una salida de seguridad a la altura justa.",
             [C("UP")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                         ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                         ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA", "ALTA"], "Sobre los trapecios",
             "Apoyá la barra bien alta sobre los trapecios, no en la nuca, y sacala de los ganchos.",
             [C("UP")], [ring(BAR, 62, 0.8), lab((60, 800), "BARRA ALTA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES AL", "ANCHO"], "Puntas afuera",
             "Pies al ancho de la cadera con las puntas afuera: las rodillas van a seguir esa misma línea.",
             [C("UP")], [ring(FOOT, 50, 0.8), ring(FOOT2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["DE PIE", "DERECHO"], "Pecho arriba",
             "Arrancá de pie, con el pecho arriba, el abdomen firme y el peso repartido en todo el pie.",
             [C("UP")], [ring(BACK, 62, 0.8), lab((60, 800), "PECHO ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "AL FONDO"], "Rodillas afuera",
             "Paso uno. Bajá controlado hasta el fondo, abriendo las rodillas y llevando la cola abajo y atrás.",
             [C("UP"), TO("DOWN", 0.4, 1.3)], [ring(KNEE_D, 54, 0.8), lab((60, 800), "RODILLAS AFUERA", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["TALONES", "ABAJO"], "Pie entero",
             "Paso dos. En el fondo, los talones siguen abajo y el torso lo más derecho que puedas.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(FOOT, 52, 0.8), lab((60, 800), "TALONES ABAJO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["SUBÍ", "EMPUJANDO"], "Todo el pie",
             "Paso tres. Subí empujando el piso con todo el pie y apretando el glúteo arriba, sin rebotar.",
             [C("DOWN"), TO("UP", 0.5, 1.3)], [ring(HIP, 56, 0.8), lab((60, 800), "EMPUJÁ EL PISO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire arriba, aguantá mientras bajás y soltalo al subir. No sueltes el aire en el fondo.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.5, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "SENTADILLA"], "Hasta el fondo",
             "Error: quedarte a mitad de camino. Bajá hasta el fondo manteniendo la espalda recta.",
             [C("UP"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP_H, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["CAER", "ADELANTE"], "Pecho arriba",
             "Error: caer con el pecho adelante. El torso sube y baja lo más derecho posible, con el abdomen firme.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HEAD_L, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TALONES", "AFUERA"], "Pie entero",
             "Error: despegar los talones en el fondo. Si no llegás con los talones abajo, no bajes tanto.",
             [C("DOWN"), TO("HEEL_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(FOOT, 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra alta", "Rodillas afuera",
                                          "Talones abajo", "Subí apretando"],
             "Tips: barra alta, rodillas afuera, talones abajo y subí apretando el glúteo.",
             [C("UP"), seqloop("UP", "DOWN", 1.2, 1.3, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Recorrido completo", "Torso derecho",
                                    "Rodillas alineadas", "Subida controlada"],
             "Claves: recorrido completo, torso derecho, rodillas alineadas y subida controlada.",
             [{"cut": "DOWN", "at": 0.1}]),
        reps(["3 X 8–10"], "Cuádriceps y glúteo",
             "Tres series de ocho a diez repeticiones, con un minuto y medio de pausa. Bajada lenta y sin rebote.",
             ["1 · BAJÁ", "2 · AFUERA", "3 · SUBÍ"], [C("UP"), seqloop("UP", "DOWN", 1.3, 1.4, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN EL GANCHO"], "Sin apuro",
             "Al terminar la serie, subí derecho, acomodá la barra en los ganchos y salí de la máquina.",
             [C("DOWN"), TO("UP", 0.9, 2.2)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT81 = {
    "titulo": "Smith Full Squat 🔥 Sentadilla completa en la Smith | Piernas",
    "tags": ["smith full squat", "sentadilla completa", "sentadilla profunda", "smith machine", "multipower",
             "cuádriceps", "glúteo", "isquios", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Smith Full Squat",
        "sentadilla profunda con barra guiada en la máquina Smith",
        "cuádriceps y glúteo",
        "La sentadilla completa en la Smith lleva el recorrido hasta el fondo: la barra va alta sobre los trapecios, las rodillas se abren hacia afuera y los talones no se despegan del piso. Al bajar más, el cuádriceps y el glúteo trabajan en todo su rango. Como la barra corre guiada, podés concentrarte en la profundidad y en no perder la espalda. Si te quedás a media altura, caés con el pecho adelante o levantás los talones, el fondo no se trabaja y la zona lumbar se carga de más.",
        ["Apoyá la barra alta sobre los trapecios y sacala de los ganchos.",
         "Pies al ancho de la cadera con las puntas afuera."],
        ["Bajá controlado hasta el fondo abriendo las rodillas.",
         "Mantené los talones apoyados y el torso derecho.",
         "Llevá la cola abajo y atrás, sin redondear la espalda.",
         "Subí empujando el piso con todo el pie.",
         "Completá la serie y dejá la barra en los ganchos."],
        ["Media sentadilla → bajá hasta el fondo.", "Caer adelante → pecho arriba y abdomen firme.",
         "Talones afuera → si no llegás, no bajes tanto."],
        ["Barra alta, sobre los trapecios.", "Rodillas afuera, alineadas con los pies.",
         "Talones pegados al piso.", "Sin rebote en el fondo."],
        "Piernas → Cuádriceps → Glúteo",
        "3 series de 8–10 repeticiones, con 1½ minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Sentadilla #SmithMachine #Cuadriceps #Gluteo #Piernas #Entrenamiento #Fuerza")}

save("smith-full-squat", fq_scenes("smith-full-squat"),
     {"pose": "DOWN", "zoom": 1.02, "dy": 20}, YT81)
