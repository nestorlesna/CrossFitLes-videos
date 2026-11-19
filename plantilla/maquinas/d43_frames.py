# Dataset D67 Sled 45 Calf Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def calf_scenes(slug):
    s, S, J = load(slug)
    PLATE = S(239, -564); RAIL = S(-72, -242); PLAT = S(70, -568)
    PAD = S(-450, -420); SEAT = S(-320, -268)
    KNEE_D = S(-221, -518); KNEE_U = S(-159, -478)
    ANK_D = S(9, -531); ANK_U = S(55, -563)
    return [
        hook("GIMNASIO · PIERNAS", ["GEMELOS", "EN LA PRENSA 45"], "Solo el tobillo",
             "Gemelos en la prensa a 45 grados: las rodillas quedan trabadas y el recorrido lo hace únicamente el tobillo.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["CARRO Y", "RIEL 45°"], "Plataforma inclinada",
             "El carro con discos corre sobre un riel a 45 grados y la plataforma queda arriba, donde apoyás la planta.",
             [C("DOWN")], [ring(PLATE, 92, 0.8), lab((1040, 800), "DISCOS", "end", 0.8),
                          ring(RAIL, 44, 1.7), lab((560, 1200), "RIEL 45°", "start", 1.7),
                          ring(PLAT, 52, 2.6), lab((1040, 890), "PLATAFORMA", "end", 2.6)], 7.2),
        step("AJUSTE 1 / 2", ["ESPALDA", "Y CADERA"], "Bien apoyado",
             "Apoyá la espalda en el respaldo y la cadera en el asiento, con los hombros y la cabeza relajados.",
             [C("DOWN")], [ring(PAD, 60, 0.8), lab((60, 1010), "RESPALDO", "start", 0.8),
                          ring(SEAT, 56, 1.8), lab((60, 1470), "CADERA APOYADA", "start", 1.8)], 7.2),
        step("AJUSTE 2 / 2", ["PLANTA EN", "LA PLATAFORMA"], "Puntas afuera",
             "Apoyá la planta de los dos pies en la plataforma, con las puntas apenas abiertas y las rodillas trabadas.",
             [C("DOWN")], [ring(PLAT, 56, 0.8), lab((1040, 900), "PLANTA AL BORDE", "end", 0.8),
                          ring(KNEE_D, 50, 1.8), lab((60, 900), "RODILLAS TRABADAS", "start", 1.8)], 7.6),
        step("POSICIÓN INICIAL", ["PUNTA", "ARRIBA"], "Tobillo flexionado",
             "Arrancá con el tobillo flexionado y la punta de los pies hacia arriba, sintiendo el estiramiento del gemelo.",
             [C("DOWN")], [ring(ANK_D, 48, 0.8), lab((60, 900), "PUNTA ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "EL TALÓN"], "Estiramiento",
             "Paso uno. Bajá el talón y llevá la punta hacia arriba hasta sentir cómo se estira el gemelo.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(ANK_D, 48, 0.8), lab((60, 900), "TALÓN ABAJO", "start", 1.0)], 7.0),
        step("PASO 2 / 3", ["ESTIRÁ", "EL TOBILLO"], "Empuje con la planta",
             "Paso dos. Empujá la plataforma estirando el tobillo, como si te pararas de puntas, sin mover las rodillas.",
             [C("DOWN"), TO("UP", 0.5, 1.0)], [ring(ANK_U, 48, 0.8), lab((60, 900), "ESTIRÁ EL TOBILLO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso tres. Quedate un segundo en la punta más alta, apretando el gemelo, y recién ahí bajá.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(KNEE_U, 50, 0.8), lab((60, 900), "PAUSA ARRIBA", "start", 1.0)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al estirar",
             "Tomá aire al bajar el talón y soltalo al estirar el tobillo. No aguantes la respiración en la punta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["DOBLAR", "LAS RODILLAS"], "Rodillas trabadas",
             "Error: doblar las rodillas para empujar. Las rodillas quedan trabadas y solo se mueve el tobillo.",
             [C("DOWN"), TO("KNEE_BAD", 0.5, 0.9)],
             [NO(1.4, (150, 880)), ring(S(-258, -532), 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta el estiramiento y subí hasta la punta más alta.",
             [C("DOWN"), TO("SHALLOW_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(S(-6, -541), 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["LEVANTAR", "LA CADERA"], "Cadera apoyada",
             "Error: levantar la cadera del asiento para llegar más arriba. La cadera queda pegada al asiento.",
             [C("DOWN"), TO("HIP_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(S(-296, -342), 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Rodillas trabadas", "Planta completa",
                                         "Recorrido completo", "Pausa en la punta"],
             "Tips: rodillas trabadas, planta completa, recorrido completo y una pausa en la punta más alta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda en el respaldo", "Empujá con la planta",
                                     "Sin rebotar", "Bajá hasta estirar"],
             "Claves: espalda en el respaldo, empujá con la planta, sin rebotar y bajá hasta sentir el estiramiento.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15–20"], "Gemelos",
             "Tres series de quince a veinte repeticiones, con un minuto de pausa. Un peso liviano y el recorrido completo valen más que mucha carga.",
             ["1 · BAJÁ", "2 · ESTIRÁ", "3 · PAUSA"], [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["SALÍ", "DESPACIO"], "Sin apurarse",
             "Al terminar la serie, trabá el seguro de la plataforma y salí de la máquina sin encorvarte.",
             [C("UP"), TO("DOWN", 0.9, 2.0)],
             [lab((60, 900), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT67 = {
    "titulo": "Sled 45 Calf Press 🔥 Gemelos en la prensa 45 | Gimnasio",
    "tags": ["sled 45 calf press", "gemelos en prensa", "prensa 45 grados", "gemelos",
             "sóleo", "pantorrilla", "piernas", "máquina de prensa", "máquinas de gimnasio",
             "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Sled 45 Calf Press",
        "extensión de tobillos (gemelos) en la prensa a 45 grados",
        "gemelos y sóleo",
        "La prensa a 45 grados permite cargar los gemelos con la espalda apoyada y las rodillas trabadas: el tobillo hace todo el recorrido y el carro corre por el riel. Es un ejercicio de recorrido largo, así que conviene un peso moderado y una pausa arriba. Si doblás las rodillas, cortás el recorrido o levantás la cadera, el estímulo se pierde.",
        ["Apoyá la espalda en el respaldo y la cadera en el asiento.",
         "Poné la planta de los pies en la plataforma y trabá las rodillas."],
        ["Arrancá con la punta de los pies hacia arriba y el talón bajo.",
         "Empujá la plataforma estirando el tobillo hasta la punta más alta.",
         "Quedate un segundo arriba apretando el gemelo.",
         "Bajá controlando hasta sentir el estiramiento.",
         "Completá la serie, trabá el seguro y salí despacio."],
        ["Doblar las rodillas → rodillas trabadas, solo se mueve el tobillo.",
         "Media repetición → bajá hasta el estiramiento y subí hasta la punta.",
         "Levantar la cadera → la cadera queda pegada al asiento."],
        ["Rodillas trabadas durante todo el recorrido.", "Planta completa en la plataforma.",
         "Recorrido completo, sin rebotar.", "Pausa de un segundo en la punta."],
        "Piernas → Gemelos → Sóleo",
        "3 series de 15–20 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Pantorrilla #Soleo #Prensa45 #Piernas #Entrenamiento #Fuerza")}

save("sled-45-calf-press", calf_scenes("sled-45-calf-press"),
     {"pose": "UP", "zoom": 1.06, "dy": 40}, YT67)
