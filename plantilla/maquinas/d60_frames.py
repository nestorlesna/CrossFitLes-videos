# Dataset D84 Smith Leg Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def lp_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(200, -884); PAR = S(500, -640); STOP = S(500, -250)
    BAR = S(200, -484); BAR_B = S(200, -279)
    HIP = S(0, -40); HIP_B = S(0, -96); KNEE_E = S(79, -267); KNEE_B = S(-36, -277)
    SHO = S(-280, -30); ANK = S(230, -440); ANK2 = S(215, -424)
    return [
        hook("GIMNASIO · PIERNAS", ["PRENSA", "EN LA SMITH"], "Empuje vertical",
             "Prensa de piernas en la Smith: supino en el piso, la barra en las plantas y empujás en vertical.",
             [C("BENT"), seqloop("BENT", "EXT", 1.3, 1.4, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes y los topes te dejan una salida de seguridad.",
             [C("BENT")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                           ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA EN LAS", "PLANTAS"], "Pies firmes",
             "Apoyá la barra en las plantas de los pies, con los pies al ancho de la cadera y las puntas arriba.",
             [C("BENT")], [ring(BAR_B, 62, 0.8), lab((60, 800), "EN LAS PLANTAS", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["CADERA Y", "HOMBROS"], "Todo apoyado",
             "La cadera y los hombros quedan apoyados en el piso durante todo el recorrido, sin despegarse.",
             [C("BENT")], [ring(SHO, 60, 0.8), ring(HIP, 56, 1.4),
                           lab((60, 800), "TODO APOYADO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["RODILLAS", "AL PECHO"], "Cargá el aire",
             "Arrancá con las rodillas al pecho y la barra apoyada, el abdomen firme y la espalda baja en el piso.",
             [C("BENT")], [ring(KNEE_B, 56, 0.8), lab((60, 800), "RODILLAS AL PECHO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "EL PISO"], "Con todo el pie",
             "Paso uno. Empujá la barra hacia arriba con las plantas de los pies, sin apurar el movimiento.",
             [C("BENT"), TO("HALF_BAD", 0.4, 0.9)], [ring(ANK, 50, 0.8), lab((60, 800), "PIE ENTERO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["EXTENDÉ", "LAS PIERNAS"], "Sin trabar",
             "Paso dos. Extendé las piernas casi del todo, sin trabar las rodillas ni despegar la cadera.",
             [C("HALF_BAD"), TO("EXT", 0.5, 1.2)], [ring(KNEE_E, 54, 0.8), lab((60, 800), "SIN TRABAR", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["VOLVÉ", "CONTROLADO"], "Rodillas al pecho",
             "Paso tres. Volvé flexionando las rodillas hacia el pecho con la barra siempre apoyada en los pies.",
             [C("EXT"), TO("BENT", 0.5, 1.3)], [ring(BAR_B, 60, 0.8), lab((60, 800), "VOLVÉ CONTROLADO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al empujar",
             "Tomá aire con las rodillas al pecho y soltalo al empujar la barra. No aguantes la respiración.",
             [C("BENT"), seqloop("BENT", "EXT", 1.3, 1.4, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "PRENSA"], "Casi estirado",
             "Error: quedarte a mitad de recorrido. Extendé casi del todo antes de volver a bajar.",
             [C("EXT"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR, 60, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["PUNTAS", "DEL PIE"], "Planta entera",
             "Error: empujar con las puntas. La barra va en las plantas de los pies, no en los dedos.",
             [C("EXT"), TO("TOES_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(ANK2, 50, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["DESPEGAR", "LA CADERA"], "Pegado al piso",
             "Error: despegar la cadera o los hombros. La espalda baja queda en el piso todo el movimiento.",
             [C("EXT"), TO("HIP_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP_B, 56, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Planta del pie", "Cadera al piso",
                                          "Sin trabar", "Bajada controlada"],
             "Tips: barra en las plantas, cadera al piso, no trabes las rodillas y bajá controlando.",
             [C("BENT"), seqloop("BENT", "EXT", 1.2, 1.3, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Recorrido completo", "Espalda al piso",
                                    "Empuje simétrico", "Rodillas alineadas"],
             "Claves: recorrido completo, espalda al piso, empuje con las dos piernas y rodillas alineadas.",
             [{"cut": "EXT", "at": 0.1}]),
        reps(["3 X 10–12"], "Cuádriceps y glúteo",
             "Tres series de diez a doce repeticiones, con un minuto y medio de pausa. Bajada lenta, sin rebote.",
             ["1 · EMPUJÁ", "2 · EXTENDÉ", "3 · VOLVÉ"], [C("BENT"), seqloop("BENT", "EXT", 1.3, 1.4, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN EL TOPE"], "Sin apuro",
             "Al terminar la serie, dejá la barra en los topes, flexioná las rodillas y salí de la máquina.",
             [C("EXT"), TO("BENT", 0.9, 1.8)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT84 = {
    "titulo": "Smith Leg Press 🔥 Prensa de piernas en la Smith | Piernas",
    "tags": ["smith leg press", "prensa de piernas", "smith machine", "multipower", "cuádriceps", "glúteo",
             "isquios", "piernas", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Smith Leg Press",
        "prensa de piernas supino con barra guiada en la máquina Smith",
        "cuádriceps y glúteo",
        "La prensa de piernas en la Smith se hace acostado supino en el piso, con la barra apoyada en las plantas de los pies: empujás en vertical por el carril y la barra sube guiada. La cadera y los hombros no se despegan del piso, así la espalda baja queda protegida. Es un empuje simétrico y controlado, bueno para sumar volumen de piernas sin cargar la columna. Los errores típicos son quedarse a mitad del recorrido, empujar con las puntas y despegar la cadera.",
        ["Apoyá la barra en las plantas de los pies, al ancho de la cadera.",
         "Cadera y hombros apoyados en el piso."],
        ["Empujá la barra hacia arriba con todo el pie.",
         "Extendé las piernas sin trabar las rodillas.",
         "Volvé flexionando las rodillas hacia el pecho.",
         "Mantené la espalda baja en el piso.",
         "Completá la serie y dejá la barra en los topes."],
        ["Media prensa → extendé casi del todo.", "Puntas del pie → la barra va en las plantas.",
         "Despegar la cadera → espalda baja pegada al piso."],
        ["Barra en las plantas, pies al ancho.", "Cadera y hombros pegados al piso.",
         "Sin trabar las rodillas arriba.", "Bajada lenta y controlada."],
        "Piernas → Cuádriceps → Glúteo",
        "3 series de 10–12 repeticiones, con 1½ minuto de pausa. Nivel: principiante.",
        "#Gimnasio #PrensaDePiernas #SmithMachine #Cuadriceps #Gluteo #Piernas #Entrenamiento #Fuerza")}

save("smith-leg-press", lp_scenes("smith-leg-press"),
     {"pose": "EXT", "zoom": 1.03, "dy": 40}, YT84)
