# Dataset D73 Sled One Leg Calf Press On Leg Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def one_scenes(slug):
    s, S, J = load(slug)
    PLATE = S(239, -564); RAIL = S(-72, -242); PLAT = S(70, -568)
    PAD = S(-450, -420); SEAT = S(-320, -268)
    KNEE_D = S(-226, -521); KNEE_U = S(-137, -455)
    ANK_D = S(4, -527); ANK_U = S(63, -569)
    FREE = S(-190, -90); FREE2 = S(-36, -519); HIP = S(-296, -338)
    return [
        hook("GIMNASIO · PIERNAS", ["GEMELOS", "A UNA PIERNA"], "Unilateral",
             "Gemelos a una pierna en la prensa a 45 grados: un solo pie empuja la plataforma y el tobillo hace todo el recorrido.",
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
        step("AJUSTE 2 / 2", ["UN PIE EN", "LA PLATAFORMA"], "La otra afuera",
             "Apoyá un solo pie en la plataforma, con la punta apenas abierta y la rodilla trabada. La otra pierna queda flexionada al costado.",
             [C("DOWN")], [ring(PLAT, 56, 0.8), lab((1040, 900), "UN PIE AL BORDE", "end", 0.8),
                           ring(FREE, 52, 1.8), lab((60, 900), "LA OTRA AFUERA", "start", 1.8)], 7.8),
        step("POSICIÓN INICIAL", ["PUNTA", "ARRIBA"], "Tobillo flexionado",
             "Arrancá con el tobillo flexionado y la punta del pie hacia arriba, sintiendo el estiramiento del gemelo.",
             [C("DOWN")], [ring(ANK_D, 48, 0.8), lab((60, 900), "PUNTA ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "EL TALÓN"], "Estiramiento",
             "Paso uno. Bajá el talón y llevá la punta hacia arriba hasta sentir cómo se estira el gemelo.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(ANK_D, 48, 0.8), lab((60, 900), "TALÓN ABAJO", "start", 1.0)], 7.0),
        step("PASO 2 / 3", ["ESTIRÁ", "EL TOBILLO"], "Empuje con el metatarso",
             "Paso dos. Empujá la plataforma estirando el tobillo, como si te pararas de puntas, sin mover la rodilla.",
             [C("DOWN"), TO("UP", 0.5, 1.0)], [ring(ANK_U, 48, 0.8), lab((60, 900), "ESTIRÁ EL TOBILLO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso tres. Quedate un segundo en la punta más alta, apretando el gemelo, y recién ahí bajá.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(KNEE_U, 50, 0.8), lab((60, 900), "PAUSA ARRIBA", "start", 1.0)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al estirar",
             "Tomá aire al bajar el talón y soltalo al estirar el tobillo. No aguantes la respiración en la punta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["DOBLAR", "LA RODILLA"], "Rodilla trabada",
             "Error: doblar la rodilla para empujar. La rodilla queda trabada y solo se mueve el tobillo.",
             [C("DOWN"), TO("KNEE_BAD", 0.5, 0.9)],
             [NO(1.4, (150, 880)), ring(S(-258, -532), 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta el estiramiento y subí hasta la punta más alta.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(S(33, -548), 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["EMPUJAR", "CON LAS DOS"], "Una sola pierna",
             "Error: apoyar la otra pierna y empujar con las dos. La pierna libre queda flexionada y afuera de la plataforma.",
             [C("DOWN"), TO("BOTH_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(FREE2, 48, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Una sola pierna empuja", "Rodilla trabada",
                                         "Planta completa", "Pausa en la punta"],
             "Tips: empujá con una sola pierna, rodilla trabada, planta completa en la plataforma y una pausa arriba.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda en el respaldo", "La otra pierna afuera",
                                    "Sin rebotar", "Bajá hasta estirar"],
             "Claves: espalda en el respaldo, la otra pierna afuera, sin rebotar y bajá hasta sentir el estiramiento.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12–15"], "Por pierna",
             "Tres series de doce a quince repeticiones por pierna, con un minuto de pausa. Peso liviano y recorrido completo.",
             ["1 · BAJÁ", "2 · ESTIRÁ", "3 · PAUSA"], [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["CAMBIÁ", "DE PIERNA"], "Sin apurarse",
             "Al terminar la serie, trabá el seguro de la plataforma, cambiá de pierna y repetí. Salí de la máquina sin encorvarte.",
             [C("UP"), TO("DOWN", 0.9, 2.0)],
             [lab((60, 900), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT73 = {
    "titulo": "Sled One Leg Calf Press 🔥 Gemelos a una pierna en la prensa 45 | Gimnasio",
    "tags": ["sled one leg calf press", "gemelos a una pierna", "gemelos en prensa", "prensa 45 grados",
             "gemelos", "pantorrilla", "unilateral", "sóleo", "piernas", "máquina de prensa",
             "gimnasio", "principiantes"],
    "descripcion": yt_desc("Sled One Leg Calf Press",
        "extensión de tobillos a una pierna en la prensa a 45 grados",
        "gemelos y pantorrilla",
        "La prensa a 45 grados permite cargar los gemelos con la espalda apoyada y las rodillas trabadas. A una pierna, el recorrido del tobillo es el mismo pero cada gemelo trabaja solo, así que se corrige la diferencia entre lados: conviene un peso moderado, pausa arriba y bajar hasta sentir el estiramiento. Si doblás la rodilla, cortás el recorrido o empujás con las dos piernas, el estímulo se pierde.",
        ["Apoyá la espalda en el respaldo y la cadera en el asiento.",
         "Poné un solo pie en la plataforma, con la rodilla trabada, y dejá la otra pierna flexionada al costado."],
        ["Arrancá con la punta del pie hacia arriba y el talón bajo.",
         "Empujá la plataforma estirando el tobillo hasta la punta más alta.",
         "Quedate un segundo arriba apretando el gemelo.",
         "Bajá controlando hasta sentir el estiramiento.",
         "Completá la serie, trabá el seguro y cambiá de pierna."],
        ["Doblar la rodilla → la rodilla queda trabada y solo se mueve el tobillo.",
         "Media repetición → bajá hasta el estiramiento y subí hasta la punta.",
         "Empujar con las dos piernas → la otra pierna queda afuera."],
        ["Una sola pierna empuja la plataforma.", "Rodilla trabada durante todo el recorrido.",
         "Planta completa en la plataforma.", "Pausa de un segundo en la punta."],
        "Piernas → Gemelos → Pantorrilla",
        "3 series de 12–15 repeticiones por pierna, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #Gemelos #Pantorrilla #Unilateral #Prensa45 #Piernas #Entrenamiento #Fuerza")}

save("sled-one-leg-calf-press-on-leg-press", one_scenes("sled-one-leg-calf-press-on-leg-press"),
     {"pose": "UP", "zoom": 1.06, "dy": 40}, YT73)
