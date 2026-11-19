# Dataset D69 Sled Calf Press On Leg Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def soleo_scenes(slug):
    s, S, J = load(slug)
    PLATE = S(239, -564); RAIL = S(-72, -242); PLAT = S(70, -568)
    PAD = S(-450, -420); SEAT = S(-320, -268)
    KNEE_D = S(-257, -532); KNEE_U = S(-222, -519)
    ANK_D = S(-28, -504); ANK_U = S(8, -529); SOLEO = S(-150, -520)
    return [
        hook("GIMNASIO · PIERNAS", ["SÓLEO", "EN LA PRENSA 45"], "Rodilla semiflexionada",
             "Sóleo en la prensa a 45 grados: con la rodilla un poco doblada, el tobillo hace todo el recorrido y el trabajo se concentra abajo.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["CARRO Y", "RIEL 45°"], "Plataforma inclinada",
             "El carro con discos corre sobre un riel a 45 grados y la plataforma queda arriba, donde apoyás la planta.",
             [C("DOWN")], [ring(PLATE, 92, 0.8), lab((1040, 800), "DISCOS", "end", 0.8),
                          ring(RAIL, 44, 1.7), lab((560, 1200), "RIEL 45°", "start", 1.7),
                          ring(PLAT, 52, 2.6), lab((1040, 890), "PLATAFORMA", "end", 2.6)], 7.2),
        step("AJUSTE 1 / 2", ["ESPALDA", "Y CADERA"], "Bien apoyado",
             "Apoyá la espalda en el respaldo y la cadera en el asiento, sin despegar la zona lumbar en ningún momento.",
             [C("DOWN")], [ring(PAD, 60, 0.8), lab((60, 1010), "RESPALDO", "start", 0.8),
                          ring(SEAT, 56, 1.8), lab((60, 1470), "CADERA APOYADA", "start", 1.8)], 7.2),
        step("AJUSTE 2 / 2", ["RODILLA", "SEMIFLEXIONADA"], "Planta al borde",
             "Dejá las rodillas apenas flexionadas todo el ejercicio y apoyá la planta de los pies en la plataforma.",
             [C("DOWN")], [ring(KNEE_D, 50, 0.8), lab((60, 900), "RODILLA BLANDA", "start", 1.0),
                          ring(PLAT, 54, 1.9), lab((1040, 900), "PLANTA AL BORDE", "end", 1.9)], 7.8),
        step("POSICIÓN INICIAL", ["PUNTA", "ARRIBA"], "Estiramiento",
             "Arrancá con la punta de los pies hacia arriba y el talón bajo, sintiendo el estiramiento del sóleo.",
             [C("DOWN")], [ring(ANK_D, 48, 0.8), lab((60, 900), "PUNTA ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "EL TALÓN"], "Sin mover la rodilla",
             "Paso uno. Bajá el talón llevando la punta hacia arriba, sin doblar más la rodilla para ganar recorrido.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(ANK_D, 48, 0.8), lab((60, 900), "TALÓN ABAJO", "start", 1.0)], 7.0),
        step("PASO 2 / 3", ["ESTIRÁ", "EL TOBILLO"], "Empuje con la planta",
             "Paso dos. Empujá la plataforma estirando el tobillo y apretando el sóleo, sin estirar del todo la rodilla.",
             [C("DOWN"), TO("UP", 0.5, 1.0)], [ring(SOLEO, 46, 0.8), lab((60, 900), "APRETÁ EL SÓLEO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso tres. Quedate un segundo en la punta más alta, apretando el sóleo, y recién ahí bajá.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(ANK_U, 48, 0.8), lab((60, 900), "PAUSA ARRIBA", "start", 1.0)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al estirar",
             "Tomá aire al bajar el talón y soltalo al estirar el tobillo. No aguantes la respiración en la punta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["DOBLAR MÁS", "LA RODILLA"], "Rodilla fija",
             "Error: doblar la rodilla durante la repetición. La rodilla queda casi igual y solo se mueve el tobillo.",
             [C("DOWN"), TO("KNEE_BAD", 0.5, 0.9)],
             [NO(1.4, (150, 880)), ring(S(-288, -538), 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta el estiramiento y subí hasta la punta más alta.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(S(-50, -509), 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["LEVANTAR", "LA CADERA"], "Cadera apoyada",
             "Error: levantar la cadera del asiento para llegar más arriba. La cadera queda pegada todo el tiempo.",
             [C("DOWN"), TO("HIP_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(S(-296, -342), 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Rodilla semiflexionada", "Planta completa",
                                         "Recorrido completo", "Pausa en la punta"],
             "Tips: rodilla semiflexionada y quieta, planta completa, recorrido completo y pausa en la punta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda en el respaldo", "Rodilla sin moverse",
                                     "Sin rebotar", "Bajá hasta estirar"],
             "Claves: espalda en el respaldo, rodilla sin moverse, sin rebotar y bajá hasta sentir el estiramiento.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12–15"], "Sóleo",
             "Tres series de doce a quince repeticiones, con un minuto de pausa. Peso moderado y el recorrido completo, sin rebotar.",
             ["1 · BAJÁ", "2 · ESTIRÁ", "3 · PAUSA"], [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["SALÍ", "DESPACIO"], "Sin apurarse",
             "Al terminar la serie, trabá el seguro de la plataforma y salí de la máquina sin encorvarte.",
             [C("UP"), TO("DOWN", 0.9, 2.0)],
             [lab((60, 900), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT69 = {
    "titulo": "Sled Calf Press On Leg Press 🔥 Sóleo en la prensa 45 | Gimnasio",
    "tags": ["sled calf press on leg press", "sóleo en prensa", "gemelos", "sóleo",
             "prensa 45 grados", "pantorrilla", "piernas", "máquina de prensa",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Sled Calf Press On Leg Press",
        "extensión de tobillos en la prensa a 45 con la rodilla semiflexionada",
        "sóleo y gemelos",
        "Con la rodilla un poco flexionada, el gemelo queda acortado y el sóleo toma más protagonismo: es el mismo movimiento de la prensa a 45, pero con la rodilla fija en semiflexión. El recorrido sigue siendo largo y controlado. Si doblás más la rodilla en cada repetición, cortás el recorrido o levantás la cadera, el estímulo se pierde.",
        ["Apoyá la espalda en el respaldo y la cadera en el asiento.",
         "Dejá las rodillas apenas flexionadas y la planta en la plataforma."],
        ["Arrancá con la punta de los pies arriba y el talón bajo.",
         "Empujá la plataforma estirando el tobillo, con la rodilla fija.",
         "Quedate un segundo arriba apretando el sóleo.",
         "Bajá controlando hasta sentir el estiramiento.",
         "Completá la serie, trabá el seguro y salí despacio."],
        ["Doblar más la rodilla → la rodilla queda fija y solo se mueve el tobillo.",
         "Media repetición → bajá hasta el estiramiento y subí hasta la punta.",
         "Levantar la cadera → la cadera pegada al asiento."],
        ["Rodilla semiflexionada y quieta.", "Planta completa en la plataforma.",
         "Recorrido completo, sin rebotar.", "Pausa de un segundo en la punta."],
        "Piernas → Sóleo → Gemelos",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Soleo #Gemelos #Pantorrilla #Prensa45 #Piernas #Entrenamiento #Fuerza")}

save("sled-calf-press-on-leg-press", soleo_scenes("sled-calf-press-on-leg-press"),
     {"pose": "UP", "zoom": 1.06, "dy": 40}, YT69)
