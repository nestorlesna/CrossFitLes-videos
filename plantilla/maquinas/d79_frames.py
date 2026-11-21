# Dataset D103 Smith Toe Raise: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def tr_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(120, -854); PAR = S(400, -560); STOP = S(400, -250)
    BAR = S(*J["DOWN"]["W"]); ANK = S(*J["UP"]["A"])
    KNEE = S(*J["UP"]["K"]); HIP = S(*J["DOWN"]["H"])
    return [
        hook("GIMNASIO · PANTORRILLAS", ["PUNTA", "DE PIE"], "Sentado en la Smith",
             "Elevación de punta de pie sentado en la Smith: la barra sobre los muslos y las puntas de los pies suben.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Solo el tobillo se mueve",
             "La barra de la Smith queda quieta sobre los muslos: el recorrido sale solo del tobillo.",
             [C("DOWN")], [ring(BEAM, 64, 0.8), lab((60, 860), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 54, 1.8), lab((60, 940), "PARANTE", "start", 1.8),
                           ring(STOP, 54, 2.8), lab((60, 1120), "TOPE", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["SENTATE", "DERECHO"], "Barra sobre los muslos",
             "Sentate en el banco con la espalda derecha y apoyá la barra sobre los muslos.",
             [C("DOWN")], [ring(BAR, 56, 0.8), lab((60, 900), "SOBRE LOS MUSLOS", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["PIES", "PLANOS"], "Toda la planta",
             "Apoyá los pies planos en el piso, con las puntas hacia adelante y el talón bien abajo.",
             [C("DOWN")], [ring(ANK, 46, 0.8), lab((60, 1250), "PIE PLANO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["PUNTA", "ABAJO"], "Tobillo relajado",
             "Arrancá con la punta del pie abajo y el tobillo relajado, sin levantar el talón.",
             [C("DOWN")], [ring(ANK, 46, 0.8), lab((60, 1250), "PUNTA ABAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ LA", "PUNTA"], "Lo más alto posible",
             "Paso uno. Subí la punta del pie lo más alto que puedas sin despegar el talón.",
             [C("DOWN"), TO("UP", 0.4, 0.9)], [ring(ANK, 46, 0.8), lab((1030, 1250), "PUNTA ARRIBA", "end", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRETÁ EL", "TIBIAL"], "Un segundo arriba",
             "Paso dos. Apretá el tibial arriba y quedate un segundo en el punto más alto.",
             [C("UP"), TO("UP", 0.2, 0.5)], [ring(ANK, 46, 0.8), lab((60, 1250), "TIBIAL ACTIVO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "DESPACIO"], "Sin rebotar",
             "Paso tres. Bajá la punta despacio hasta la posición inicial, sin dejar caer el pie.",
             [C("UP"), TO("DOWN", 0.4, 1.2)], [ring(ANK, 46, 0.8), lab((1030, 1250), "PUNTA ABAJO", "end", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Sin aguantar",
             "Subí soltando el aire y bajá tomando aire. No aguantes la respiración en ninguna parte.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: media repetición. Subí la punta hasta el tope y bajá hasta el final.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(ANK, 46, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TALÓN", "ARRIBA"], "Toda la planta",
             "Error: levantar el talón. El talón queda abajo y solo sube la punta del pie.",
             [C("UP"), TO("HEEL_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(ANK, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["ESPALDA", "ENCORVADA"], "Torso derecho",
             "Error: encorvar la espalda. La espalda queda derecha y el peso sobre los glúteos.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Tobillo completo", "Talón abajo",
                                          "Torso derecho", "Bajada lenta"],
             "Tips: tobillo completo, talón abajo, torso derecho y bajada lenta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Pies planos", "Solo el tobillo",
                                     "Tibial apretado", "Sin rebotar"],
             "Claves: pies planos, solo el tobillo, tibial apretado y sin rebotar.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15–20"], "Tibial anterior",
             "Tres series de quince a veinte repeticiones, con cuarenta segundos de pausa.",
             ["1 · SUBÍ", "2 · ARRIBA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["SOLTÁ LA", "BARRA"], "Sin apurarte",
             "Al terminar la serie, soltá la barra en el soporte y estirá los tobillos antes de seguir.",
             [C("DOWN"), TO("DOWN", 0.6, 0.8)],
             [lab((60, 900), "ESTIRÁ LOS TOBILLOS", "start", 1.0)], 6.5),
    ]


YT103 = {
    "titulo": "Smith Toe Raise 🔥 Elevación de punta de pie sentado | Tibial anterior",
    "tags": ["smith toe raise", "elevación de punta de pie", "toe raise", "tibial anterior",
             "smith machine", "multipower", "pantorrilla", "tobillo", "gimnasio",
             "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Smith Toe Raise",
        "elevación de punta de pie sentado en la Smith, con la barra apoyada sobre los muslos",
        "tibial anterior y gemelos",
        "La elevación de punta de pie sentado en la Smith se hace en un banco, con la barra apoyada sobre los muslos y las dos manos sujetándola. Los pies quedan planos, con el talón bien abajo, y solo suben las puntas lo más alto posible. Apretás el tibial un segundo arriba y bajás despacio, sin dejar caer el pie. El talón nunca se despega del piso. Los errores típicos son cortar el recorrido, levantar el talón y encorvar la espalda.",
        ["Sentate en el banco con la espalda derecha.",
         "Apoyá la barra sobre los muslos y sujetala con las dos manos."],
        ["Apoyá los pies planos, con las puntas hacia adelante.",
         "Subí la punta del pie sin despegar el talón.",
         "Apretá el tibial un segundo arriba.",
         "Bajá la punta despacio hasta la posición inicial.",
         "Completá la serie sin rebotar."],
        ["Media repetición → subí al tope y bajá hasta el final.",
         "Talón arriba → el talón queda abajo.",
         "Espalda encorvada → la espalda queda derecha."],
        ["Pies planos y talón abajo.", "Solo se mueve el tobillo.",
         "Tibial apretado arriba.", "Bajada lenta, sin rebotar."],
        "Pantorrillas → Tibial anterior → Gemelos",
        "3 series de 15–20 repeticiones, con 40 segundos de pausa. Nivel: principiante.",
        "#Gimnasio #Tibial #Pantorrillas #ToeRaise #SmithMachine #Multipower #Tobillo #Entrenamiento")}

save("smith-toe-raise", tr_scenes("smith-toe-raise"),
     {"pose": "UP", "zoom": 1.2, "dy": 40}, YT103)
