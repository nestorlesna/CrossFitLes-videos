# Dataset D83 Smith Hip Raise: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def hr_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(0, -884); PAR = S(300, -640); STOP = S(300, -300)
    BAR = S(0, -65); BAR_U = S(0, -197)
    HIP = S(0, -40); HIP_U = S(0, -172); HIP_H = S(0, -110)
    SHO = S(-280, -30); KNEE = S(159, -220); KNEE_U = S(233, -230)
    ANK = S(225, 0); ANK2 = S(205, 0); HEAD = S(-312, -30); HEAD_A = S(-239, -10)
    return [
        hook("GIMNASIO · GLÚTEO", ["ELEVACIÓN", "DE CADERA"], "Puente con barra",
             "Elevación de cadera en la Smith: supino, la barra sobre la pelvis y subís el glúteo hasta alinear el cuerpo.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.3, 1.4, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes y los topes te dejan una salida de seguridad.",
             [C("DOWN")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                           ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA EN LA", "PELVIS"], "Cómoda",
             "Apoyá la barra sobre la pelvis, no sobre el abdomen, y sujetala con las manos a los costados.",
             [C("DOWN")], [ring(BAR, 62, 0.8), lab((60, 800), "SOBRE LA PELVIS", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES", "APOYADOS"], "Al ancho",
             "Pies al ancho de la cadera, apoyados a unos pasos, con las puntas apenas afuera.",
             [C("DOWN")], [ring(ANK, 50, 0.8), ring(ANK2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["HOMBROS", "EN EL PISO"], "Todo apoyado",
             "Arrancá supino, con los hombros, la cabeza y los pies bien apoyados y el abdomen firme.",
             [C("DOWN")], [ring(SHO, 62, 0.8), lab((60, 800), "HOMBROS AL PISO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ LA", "CADERA"], "Apretá el glúteo",
             "Paso uno. Empujá el piso con los talones y subí la cadera apretando el glúteo.",
             [C("DOWN"), TO("UP", 0.4, 1.3)], [ring(HIP_U, 56, 0.8), lab((60, 800), "GLÚTEO ARRIBA", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["ALINEÁ", "EL CUERPO"], "Sin arquear",
             "Paso dos. Arriba, hombros, cadera y rodillas quedan en línea, sin arquear la lumbar.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(KNEE_U, 54, 0.8), ring(HIP_U, 56, 1.2),
                                             lab((60, 800), "TODO ALINEADO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLADO"], "Sin soltar",
             "Paso tres. Bajá controlado hasta apoyar la pelvis, sin dejarte caer y sin soltar el abdomen.",
             [C("UP"), TO("DOWN", 0.5, 1.3)], [ring(HIP, 56, 0.8), lab((60, 800), "BAJÁ CONTROLADO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá arriba",
             "Tomá aire abajo, subí soltando el aire y apretá el glúteo arriba. No aguantes la respiración.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.3, 1.4, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "ELEVACIÓN"], "Llegá arriba",
             "Error: quedarte a mitad de camino. Subí hasta alinear hombros, cadera y rodillas.",
             [C("UP"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP_H, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["ARQUEAR", "LA LUMBAR"], "Costillas abajo",
             "Error: subir de más y arquear la lumbar. Las costillas bajan y el glúteo hace el trabajo.",
             [C("UP"), TO("ARCH_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HEAD_A, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["PUNTAS", "DEL PIE"], "Empujá con el talón",
             "Error: empujar con las puntas. El empuje sale del talón y del pie entero, no de los dedos.",
             [C("UP"), TO("HEELS_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(ANK, 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra en la pelvis", "Empujá con el talón",
                                          "Apretá el glúteo", "No arquees"],
             "Tips: barra sobre la pelvis, empujá con el talón, apretá el glúteo arriba y no arquees la lumbar.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.3, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Recorrido completo", "Costillas abajo",
                                    "Empuje del talón", "Bajada controlada"],
             "Claves: recorrido completo, costillas abajo, empuje del talón y bajada controlada.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 10–12"], "Glúteo e isquios",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Apretá un segundo arriba.",
             ["1 · SUBÍ", "2 · APRETÁ", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "UP", 1.3, 1.4, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN EL GANCHO"], "Con cuidado",
             "Al terminar la serie, bajá la cadera, acomodá la barra en los ganchos y salí de la máquina.",
             [C("UP"), TO("DOWN", 0.9, 1.8)],
             [lab((60, 800), "CON CUIDADO", "start", 1.0)], 6.5),
    ]


YT83 = {
    "titulo": "Smith Hip Raise 🔥 Elevación de cadera con barra | Glúteo",
    "tags": ["smith hip raise", "elevación de cadera", "puente de glúteo", "hip thrust", "smith machine",
             "glúteo", "isquios", "core", "gimnasio", "principiantes", "rutina de glúteo"],
    "descripcion": yt_desc("Smith Hip Raise",
        "elevación de cadera supino con barra guiada en la máquina Smith",
        "glúteo e isquios",
        "La elevación de cadera en la Smith es un puente de glúteo con barra: te acostás supino con la barra sobre la pelvis, los pies apoyados y los hombros firmes en el piso. Empujás con los talones y subís la cadera apretando el glúteo hasta alinear hombros, cadera y rodillas. La barra guiada te permite cargar sin pelear con el equilibrio. Los errores típicos son quedarse a media elevación, arquear la lumbar para subir de más y empujar con las puntas de los pies.",
        ["Apoyá la barra sobre la pelvis y sujetala a los costados.",
         "Pies al ancho de la cadera, apoyados a unos pasos."],
        ["Empujá el piso con los talones y subí la cadera.",
         "Apretá el glúteo arriba, con las costillas abajo.",
         "Quedá en línea hombros, cadera y rodillas.",
         "Bajá controlado hasta apoyar la pelvis.",
         "Completá la serie y dejá la barra en los ganchos."],
        ["Media elevación → subí hasta alinear el cuerpo.",
         "Arquear la lumbar → costillas abajo y glúteo apretado.",
         "Empujar con las puntas → empuje del talón."],
        ["Barra sobre la pelvis, no sobre el abdomen.", "Costillas abajo, sin arquear.",
         "Empuje del talón y del pie entero.", "Pausa de un segundo arriba."],
        "Glúteo → Isquios → Core",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gluteo #HipRaise #SmithMachine #PuenteDeGluteo #Isquios #Entrenamiento #Fuerza")}

save("smith-hip-raise", hr_scenes("smith-hip-raise"),
     {"pose": "UP", "zoom": 1.06, "dy": 60}, YT83)
