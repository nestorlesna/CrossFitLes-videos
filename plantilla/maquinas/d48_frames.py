# Dataset D72 Sled Lying Squat: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def squat_scenes(slug):
    s, S, J = load(slug)
    PLAT = S(59, -88); RAIL = S(0, -78); STACK = S(234, -660); BENCH = S(-300, -150)
    FOOT = S(36, -140); KNEE = S(-100, -331); KNEE_E = S(-62, -231); ANK_E = S(196, -172)
    HIP = S(-300, -198); HEEL = S(120, -110)
    return [
        hook("GIMNASIO · PIERNAS", ["SENTADILLA", "EN EL SLED"], "Tumbado y de frente",
             "Sentadilla en el sled tumbado: la plataforma se empuja con la planta completa y las piernas hacen todo el recorrido.",
             [C("BENT"), seqloop("BENT", "EXT", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BANCO", "Y PLATAFORMA"], "Carro sobre riel",
             "El banco queda horizontal, la plataforma corre sobre un riel y la pila del otro lado le da la carga.",
             [C("BENT")], [ring(PLAT, 66, 0.8), lab((470, 1120), "PLATAFORMA", "start", 0.8),
                           ring(STACK, 62, 1.8), lab((1000, 900), "PILA DE PESO", "end", 1.8),
                           ring(RAIL, 44, 2.8), lab((240, 1210), "RIEL", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["ESPALDA", "Y CADERA"], "Bien apoyado",
             "Acostate con la espalda y la cadera pegadas al banco y la cabeza en el apoyo. La cadera no se despega en ningún momento.",
             [C("BENT")], [ring(BENCH, 90, 0.8), lab((150, 1140), "CADERA PEGADA", "start", 0.8)], 7.4),
        step("AJUSTE 2 / 2", ["PLANTA", "COMPLETA"], "Pies bien apoyados",
             "Apoyá la planta completa en la plataforma, con los pies al ancho de la cadera y los tobillos a noventa grados.",
             [C("BENT")], [ring(FOOT, 52, 0.8), lab((520, 1140), "PLANTA COMPLETA", "start", 0.8),
                           ring(KNEE, 50, 1.9), lab((230, 1000), "RODILLAS ALINEADAS", "start", 1.9)], 7.6),
        step("POSICIÓN INICIAL", ["RODILLAS", "DOBLADAS"], "Pies en la plataforma",
             "Arrancá con las rodillas dobladas y los pies apoyados, sintiendo la plataforma pegada a la planta.",
             [C("BENT")], [ring(KNEE, 50, 0.8), lab((300, 1100), "RODILLAS DOBLADAS", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "CON LAS PIERNAS"], "Planta completa",
             "Paso uno. Empujá la plataforma extendiendo las piernas, con la planta completa y la cadera pegada al banco.",
             [C("BENT"), TO("EXT", 0.4, 1.0)], [ring(KNEE_E, 50, 0.8), lab((330, 1080), "EXTENDÉ LAS PIERNAS", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["ARRIBA", "SIN TRABAR"], "Piernas casi rectas",
             "Paso dos. Llegá arriba con las piernas casi extendidas, sin trabar la rodilla ni despegar la cadera.",
             [C("EXT"), TO("EXT", 0.2, 0.4)], [ring(ANK_E, 46, 0.8), lab((560, 1140), "SIN TRABAR", "start", 1.0)], 7.0),
        step("PASO 3 / 3", ["VOLVÉ", "CONTROLANDO"], "Sin soltar la plataforma",
             "Paso tres. Volvé doblando las rodillas despacio, sin dejar que la plataforma gane velocidad.",
             [C("EXT"), TO("BENT", 0.5, 1.1)], [ring(PLAT, 50, 0.8), lab((470, 1120), "VOLVÉ DESPACIO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al empujar",
             "Tomá aire cuando bajás y soltalo cuando empujás la plataforma. No aguantes el aire arriba.",
             [C("BENT"), seqloop("BENT", "EXT", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta las rodillas bien dobladas y subí hasta extender las piernas.",
             [C("BENT"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(KNEE_E, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["DESPEGAR", "LA CADERA"], "Cadera en el banco",
             "Error: levantar la cadera del banco para empujar más. La cadera y la espalda quedan apoyadas todo el tiempo.",
             [C("BENT"), TO("HIP_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(HIP, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TALONES", "ARRIBA"], "Planta completa",
             "Error: empujar con la punta de los pies. Los talones quedan apoyados y la planta completa empuja la plataforma.",
             [C("BENT"), TO("HEEL_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(HEEL, 46, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Planta completa en la plataforma", "Cadera pegada al banco",
                                         "Rodillas alineadas con los pies", "Bajá controlando"],
             "Tips: planta completa en la plataforma, cadera pegada al banco, rodillas alineadas con los pies y bajada controlada.",
             [C("BENT"), seqloop("BENT", "EXT", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Empujá con los talones", "Sin despegar la cadera",
                                    "Extendé sin trabar", "Recorrido completo"],
             "Claves: empujá con los talones, no despegues la cadera, extendé sin trabar y completá el recorrido.",
             [{"cut": "EXT", "at": 0.1}]),
        reps(["3 X 10–15"], "Cuádriceps y glúteo",
             "Tres series de diez a quince repeticiones, con un minuto de pausa. Peso moderado y el recorrido completo, sin rebotar.",
             ["1 · EMPUJÁ", "2 · ARRIBA", "3 · VOLVÉ"], [C("BENT"), seqloop("BENT", "EXT", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["VOLVÉ", "DESPACIO"], "Sin apurarse",
             "Al terminar la serie, volvé la plataforma al tope con las rodillas dobladas y recién ahí sentate y salí del banco.",
             [C("EXT"), TO("BENT", 0.9, 2.0)],
             [lab((470, 1140), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT72 = {
    "titulo": "Sled Lying Squat 🔥 Sentadilla en el sled tumbado | Gimnasio",
    "tags": ["sled lying squat", "sentadilla en sled", "prensa de piernas tumbado", "cuádriceps", "glúteo",
             "piernas", "máquina de gimnasio", "gimnasio", "principiantes", "rutina de piernas",
             "entrenamiento de piernas", "fuerza"],
    "descripcion": yt_desc("Sled Lying Squat",
        "sentadilla acostado en el sled horizontal",
        "cuádriceps y glúteo",
        "En el sled tumbado la espalda y la cadera quedan apoyadas en el banco y la plataforma corre sobre un riel: el empuje sale de las piernas, con la planta completa y la cadera pegada. Es una prensa horizontal muy estable para cargar cuádriceps y glúteo. Si despegás la cadera, empujás con la punta o cortás el recorrido, la espalda se lleva parte del trabajo.",
        ["Acostate con la espalda y la cadera pegadas al banco.",
         "Apoyá la planta completa con los pies al ancho de la cadera."],
        ["Arrancá con las rodillas dobladas y los pies en la plataforma.",
         "Empujá la plataforma extendiendo las piernas.",
         "Llegá arriba sin trabar la rodilla.",
         "Volvé doblando despacio hasta la posición inicial.",
         "Completá la serie y volvé la plataforma al tope."],
        ["Despegar la cadera → la cadera queda pegada al banco.",
         "Empujar con la punta → la planta completa empuja.",
         "Media repetición → bajá hasta el final y extendé arriba."],
        ["Planta completa en la plataforma.", "Cadera pegada al banco.",
         "Rodillas alineadas con los pies.", "Bajada controlada."],
        "Piernas → Cuádriceps → Glúteo",
        "3 series de 10–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Cuádriceps #Glúteo #SledMachine #Piernas #Entrenamiento #Fuerza")}

save("sled-lying-squat", squat_scenes("sled-lying-squat"),
     {"pose": "EXT", "zoom": 1.04, "dy": 45}, YT72)
