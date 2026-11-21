# Dataset D100 Smith Standing Leg Calf Raise: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def cr_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(-80, -924); PAR = S(220, -650); STOP = S(220, -560)
    BAR = S(*J["DOWN"]["W"]); SHO = S(*J["UP"]["S"])
    ANK_D = S(30, 0); ANK_U = S(30, -40); KNEE_U = S(*J["UP"]["K"]); KNEE_B = S(*J["KNEE_BAD"]["K"])
    HIP = S(*J["UP"]["H"]); HEAD = S(*J["UP"]["N"])
    return [
        hook("GIMNASIO · PANTORRILLAS", ["ELEVACIÓN", "DE TALÓN"], "A una pierna",
             "Elevación de talón a una pierna en la Smith: barra en la espalda, una pierna de apoyo y la otra despegada.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Barra a la espalda",
             "La Smith te sostiene la barra en la espalda mientras hacés el trabajo de pantorrilla sobre una sola pierna.",
             [C("DOWN")], [ring(BEAM, 64, 0.8), lab((60, 860), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 54, 1.8), lab((60, 940), "PARANTE", "start", 1.8),
                           ring(STOP, 54, 2.8), lab((60, 1120), "TOPE", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A LA", "ESPALDA"], "Omóplatos juntos",
             "Apoyá la barra en la espalda alta, con los omóplatos juntos y las manos bien agarradas.",
             [C("DOWN")], [ring(BAR, 56, 0.8), lab((60, 860), "ESPALDA ALTA", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["PIE DE", "APOYO"], "Una sola pierna",
             "Elegí la pierna de apoyo, dejá la otra despegada atrás y pasá el peso a la punta del pie.",
             [C("DOWN")], [ring(ANK_D, 46, 0.8), lab((60, 1250), "PIE DE APOYO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["TALÓN", "ABAJO"], "Rodilla estirada",
             "Arrancá con la rodilla casi estirada, el torso derecho y el talón bien abajo, en el piso.",
             [C("DOWN")], [ring(ANK_D, 46, 0.8), lab((60, 1250), "TALÓN AL PISO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ EL", "TALÓN"], "Hasta la punta",
             "Paso uno. Subí el talón hasta quedar lo más alto posible sobre la punta del pie.",
             [C("DOWN"), TO("UP", 0.4, 0.9)], [ring(ANK_U, 46, 0.8), lab((1030, 1250), "PUNTA DEL PIE", "end", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRETÁ EL", "GEMELO"], "Un segundo arriba",
             "Paso dos. Apretá el gemelo arriba y quedate un segundo en el punto más alto.",
             [C("UP"), TO("UP", 0.2, 0.5)], [ring(KNEE_U, 48, 0.8), lab((60, 860), "RODILLA ESTIRADA", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "DESPACIO"], "Estiramiento",
             "Paso tres. Bajá el talón despacio hasta el estiramiento completo, sin rebotar.",
             [C("UP"), TO("DOWN", 0.4, 1.2)], [ring(ANK_D, 46, 0.8), lab((1030, 1250), "TALÓN AL PISO", "end", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Subí soltando el aire y bajá tomando aire. No aguantes la respiración.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: media repetición. Subí hasta el tope y bajá hasta el estiramiento completo.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(ANK_U, 46, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["RODILLA", "DOBLADA"], "Rodilla estirada",
             "Error: doblar la rodilla. La rodilla queda casi estirada y el movimiento sale del tobillo.",
             [C("UP"), TO("KNEE_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(KNEE_B, 50, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TORSO", "INCLINADO"], "Torso derecho",
             "Error: inclinar el torso. El torso queda derecho y el peso sobre la punta del pie.",
             [C("UP"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Rodilla estirada", "Torso derecho",
                                          "Recorrido completo", "Bajada lenta"],
             "Tips: rodilla estirada, torso derecho, recorrido completo y bajada lenta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Una pierna firme", "Tobillo completo",
                                     "Gemelo apretado", "Bajada lenta"],
             "Claves: una pierna firme, tobillo completo, gemelo apretado y bajada lenta.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12–15"], "Pantorrillas",
             "Tres series de doce a quince repeticiones por pierna, con un minuto de pausa.",
             ["1 · SUBÍ", "2 · ARRIBA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        step("AL TERMINAR", ["CAMBIÁ", "DE PIERNA"], "Sin apurarte",
             "Al terminar la serie, apoyá el pie y cambiá de pierna. Descansá antes de seguir.",
             [C("UP"), TO("DOWN", 0.8, 1.5)],
             [lab((60, 1000), "CAMBIÁ DE PIERNA", "start", 1.0)], 6.5),
    ]


YT100 = {
    "titulo": "Smith Standing Leg Calf Raise 🔥 Elevación de talón a una pierna | Pantorrillas",
    "tags": ["smith standing leg calf raise", "elevación de talón", "calf raise", "pantorrilla",
             "smith machine", "multipower", "gemelos", "una pierna", "gimnasio",
             "principiantes", "rutina de pantorrillas"],
    "descripcion": yt_desc("Smith Standing Leg Calf Raise",
        "elevación de talón sobre una pierna con la barra guiada apoyada en la espalda",
        "gemelos e isquiotibiales",
        "La elevación de talón a una pierna en la Smith se hace con la barra apoyada en la espalda alta y una sola pierna de apoyo, mientras la otra queda despegada del piso. Subís el talón hasta quedar sobre la punta del pie, apretás el gemelo arriba y bajás despacio hasta el estiramiento completo. La rodilla queda casi estirada y el torso derecho: el recorrido sale solo del tobillo. Los errores típicos son cortar el movimiento, doblar la rodilla y inclinar el torso.",
        ["Apoyá la barra en la espalda alta, con los omóplatos juntos.",
         "Elegí la pierna de apoyo y dejá la otra despegada atrás."],
        ["Arrancá con la rodilla casi estirada y el talón en el piso.",
         "Subí el talón hasta quedar sobre la punta del pie.",
         "Apretá el gemelo arriba y quedate un segundo.",
         "Bajá el talón despacio hasta el estiramiento.",
         "Completá la serie y cambiá de pierna."],
        ["Media repetición → subí al tope y bajá hasta el estiramiento.",
         "Rodilla doblada → la rodilla queda casi estirada.",
         "Torso inclinado → el torso queda derecho."],
        ["Una sola pierna, bien firme.", "Rodilla casi estirada.",
         "Recorrido completo del tobillo.", "Bajada lenta y controlada."],
        "Pantorrillas → Gemelos → Isquiotibiales",
        "3 series de 12–15 repeticiones por pierna, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Pantorrillas #Gemelos #CalfRaise #SmithMachine #Multipower #Piernas #Entrenamiento")}

save("smith-standing-leg-calf-raise", cr_scenes("smith-standing-leg-calf-raise"),
     {"pose": "UP", "zoom": 1.0, "dy": 60}, YT100)
