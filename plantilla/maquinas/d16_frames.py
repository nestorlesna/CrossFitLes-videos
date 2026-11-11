# Dataset D01 - D31 Lever Kneeling Leg Curl y D32 Lever Military Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def kc_scenes(slug):
    s, S, J = load(slug)
    PAD = S(-200, -300); HD = S(95, -590); PILE = S(-600, -300); PIN = S(-549, -155)
    A_K = S(*J["KNEEL"]["A"]); A_M = S(*J["MID"]["A"]); A_C = S(*J["CURL"]["A"])
    K_BAD = S(*J["HIP_BAD"]["K"]); N_BAD = S(*J["DIP_BAD"]["N"])
    A_S = S(*J["SHORT_BAD"]["A"])
    return [
        hook("GIMNASIO · PIERNAS", ["KNEELING", "LEG CURL"], "Femoral arrodillado",
             "Lever Kneeling Leg Curl: femoral arrodillado en máquina de palanca. Isquiotibiales fuertes con el tronco quieto.",
             [C("KNEEL"), seqloop("CURL", "KNEEL", 1.2, 1.8)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Almohadilla, manijas y rodillo",
             "La máquina tiene una almohadilla para las rodillas, manijas adelante y un rodillo que va detrás del tobillo.",
             [C("KNEEL")], [ring(PAD, 56, 0.8), lab((985, 1310), "RODILLA", "end", 0.8),
                            ring(HD, 34, 1.8), lab((985, 1120), "MANIJAS", "end", 1.8),
                            ring(PILE, 52, 2.8), lab((60, 1300), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["LAS", "RODILLAS"], "En la almohadilla",
             "Apoyá las rodillas en la almohadilla, con el eje rojo justo al costado de la rodilla.",
             [C("KNEEL")], [ring(PAD, 56, 0.8), lab((985, 1310), "RODILLA", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Rodillo y pasador",
             "Elegí el peso con el pasador y ajustá el rodillo detrás del tobillo, no sobre el talón.",
             [C("KNEEL")], [ring(PIN, 26, 0.8), lab((60, 1440), "PASADOR", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "RECTA"], "Manos firmes en las manijas",
             "Arrodillate, agarrá las manijas con los brazos firmes y dejá el tronco quieto, mirando abajo.",
             [C("KNEEL")], [lab((60, 1010), "ESPALDA RECTA", "start", 1.0),
                            ring(A_K, 40, 1.6), lab((60, 1240), "TALONES", "start", 1.6)], 7.0),
        step("PASO 1 / 3", ["TALONES", "ARRIBA"], "Cadera quieta",
             "Paso uno. Llevá los talones hacia los glúteos, doblando las rodillas sin mover la cadera.",
             [C("KNEEL"), TO("MID", 0.6, 1.2)],
             [arrow((437, 1308), (498, 1152), 0.9, 1.2)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ", "ARRIBA"], "Un segundo",
             "Paso dos. Arriba, apretá los isquiotibiales un segundo, sin subir la cadera.",
             [C("CURL")], [ring(A_C, 34, 0.8), lab((985, 1180), "APRETÁ", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Tres segundos",
             "Paso tres. Volvé lento, en tres segundos, hasta casi estirar las rodillas.",
             [C("CURL"), TO("KNEEL", 0.6, 2.4)],
             [arrow((498, 1152), (437, 1308), 0.9, 2.0)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
             "Soltá el aire cuando subís los talones y tomalo cuando bajás.",
             [C("KNEEL"), seqloop("CURL", "KNEEL", 1.3, 2.0, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["CADERA", "ARRIBA"], "La cadera se despega",
             "Error: subir la cadera para ayudarte. La cadera queda quieta y las rodillas no se despegan.",
             [C("KNEEL"), TO("HIP_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(K_BAD, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TIRAR", "EL TRONCO"], "El pecho se va adelante",
             "Error: tirar el tronco adelante para empujar. El tronco queda firme y solo se mueven las rodillas.",
             [C("CURL"), TO("DIP_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(N_BAD, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["MEDIO", "RECORRIDO"], "Rápido y corto",
             "Error: medio recorrido, rápido. Llevá los talones bien arriba y volvé lento.",
             [C("KNEEL"), TO("SHORT_BAD", 0.5, 0.8)], [NO(pos=(540, 700)), ring(A_S, 40, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Rodillas en la almohadilla", "Cadera quieta", "Talones a los glúteos", "Vuelta lenta"],
             "Tips: rodillas en la almohadilla, cadera quieta, talones a los glúteos y vuelta lenta.",
             [C("KNEEL"), seqloop("CURL", "KNEEL")]),
        keys("CLAVES", ["TÉCNICA"], ["Rodillo detrás del tobillo", "Tronco firme", "Apretá arriba", "Volvé en 3 segundos"],
             "Claves: rodillo detrás del tobillo, tronco firme, apretá arriba y volvé en tres segundos.",
             [{"cut": "CURL", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Cuando las doce salen fáciles, subí una placa.",
             ["1 · TALONES ARRIBA", "2 · APRETÁ", "3 · VOLVÉ LENTO"],
             [C("KNEEL"), seqloop("CURL", "KNEEL")]),
        step("AL TERMINAR", ["BAJÁ", "DESPACIO"], "Sin soltar la pila",
             "Al terminar, bajá los talones despacio y soltá las manijas sin dejar caer la pila.",
             [C("CURL"), TO("KNEEL", 0.8, 2.2)],
             [lab((60, 1010), "BAJÁ DESPACIO", "start", 1.0)], 6.5),
    ]


def mp_scenes(slug):
    s, S, J = load(slug)
    SEAT = S(-240, -184); PIN = S(-609, -155); BACK = S(-318, -300)
    W_D = S(*J["DOWN"]["W"]); W_U = S(*J["UP"]["W"])
    CH_BAD = S((J["ARCH_BAD"]["S"][0] + J["ARCH_BAD"]["H"][0]) / 2,
               (J["ARCH_BAD"]["S"][1] + J["ARCH_BAD"]["H"][1]) / 2)
    W_LOW = S(*J["LOW_BAD"]["W"]); W_LOCK = S(*J["LOCK_BAD"]["W"])
    return [
        hook("GIMNASIO · HOMBROS", ["MILITARY", "PRESS"], "Press militar en máquina",
             "Lever Military Press: press militar en máquina de palanca. Hombros fuertes con la espalda apoyada.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.0)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Agarre prono y respaldo",
             "La máquina tiene manijas con agarre prono y un respaldo que te deja la espalda pegada.",
             [C("DOWN")], [ring(W_D, 36, 0.8), lab((985, 1180), "MANIJAS", "end", 0.8),
                           ring(BACK, 40, 1.8), lab((985, 1310), "RESPALDO", "end", 1.8),
                           ring(PIN, 26, 2.8), lab((60, 1407), "PESO", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Manijas a la altura del hombro",
             "Ajustá el asiento para que las manijas arranquen a la altura de los hombros.",
             [C("DOWN")], [ring(SEAT, 40, 0.8), lab((985, 1440), "ASIENTO", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí un peso liviano con el pasador: el hombro es una articulación delicada.",
             [C("DOWN")], [ring(PIN, 26, 0.8), lab((60, 1407), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "PEGADA"], "Muñecas sobre los codos",
             "Espalda pegada al respaldo, pies firmes y las muñecas justo arriba de los codos.",
             [C("DOWN")], [ring(W_D, 36, 0.8), lab((985, 1140), "MUÑECA SOBRE CODO", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "ARRIBA"], "Sin arquear la lumbar",
             "Paso uno. Empujá las manijas hacia arriba, sin arquear la zona lumbar.",
             [C("DOWN"), TO("UP", 0.6, 1.2)],
             [arrow(W_D, (W_U[0] + 4, W_U[1] + 10), 0.9, 1.2)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["SIN", "TRABAR"], "Casi estirado arriba",
             "Paso dos. Arriba, estirá casi del todo, pero sin trabar los codos.",
             [C("UP")], [ring(W_U, 36, 0.8), lab((985, 960), "SIN TRABAR", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLADO"], "Hasta el hombro",
             "Paso tres. Bajá controlado hasta la altura del hombro, no más abajo.",
             [C("UP"), TO("DOWN", 0.6, 2.4)],
             [arrow((W_U[0] + 4, W_U[1] + 10), W_D, 0.9, 2.0)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
             "Soltá el aire mientras empujás hacia arriba y tomalo mientras bajás.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ESPALDA", "ARQUEADA"], "La lumbar pegada",
             "Error: arquear la espalda para empujar. Apretá el abdomen y bajá el peso.",
             [C("DOWN"), TO("ARCH_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(CH_BAD, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["BAJAR", "DE MÁS"], "Frená en el hombro",
             "Error: bajar las manijas mucho más abajo que los hombros. Frená a la altura del hombro.",
             [C("DOWN"), TO("LOW_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(W_LOW, 36, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["CODOS", "TRABADOS"], "Casi estirado, nunca trabado",
             "Error: trabar los codos arriba. Llegá casi estirado y empezá a bajar.",
             [C("DOWN"), TO("LOCK_BAD", 0.5, 0.8)], [NO(pos=(540, 700)), ring(W_LOCK, 36, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Manijas a la altura del hombro", "Lumbar pegada", "Arriba sin trabar", "Muñecas firmes"],
             "Tips: manijas a la altura del hombro, lumbar pegada, arriba sin trabar y muñecas firmes.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.0)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda pegada", "Pies firmes", "Bajá controlado", "Sin impulso"],
             "Claves: espalda pegada, pies firmes, bajá controlado y sin impulso.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto y medio de pausa",
             "Tres series de diez a doce, con un minuto y medio de pausa. Cuando salen fáciles, subí una placa.",
             ["1 · EMPUJÁ ARRIBA", "2 · SIN TRABAR", "3 · BAJÁ AL HOMBRO"],
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.0)]),
        step("AL TERMINAR", ["ACOMPAÑÁ", "LAS MANIJAS"], "Sin soltar de golpe",
             "Al terminar, acompañá las manijas hasta la altura del hombro y dejá el peso apoyado.",
             [C("UP"), TO("DOWN", 0.8, 2.2)],
             [lab((60, 1010), "ACOMPAÑÁ", "start", 1.0)], 6.5),
    ]


YT31 = {
    "titulo": "Lever Kneeling Leg Curl 🔥 Femoral arrodillado en máquina | Gimnasio",
    "tags": ["lever kneeling leg curl", "femoral arrodillado", "kneeling leg curl", "curl femoral",
             "isquiotibiales", "femorales", "piernas", "glúteos", "máquina de palanca",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Lever Kneeling Leg Curl", "femoral arrodillado en máquina de palanca",
        "isquiotibiales, con glúteos como apoyo",
        "¿Sentís que el femoral no trabaja? Casi siempre es la cadera que sube. Mirá cómo dejarla quieta.",
        ["Apoyá las rodillas en la almohadilla y ajustá el rodillo detrás del tobillo.",
         "Elegí el peso con el pasador: uno que te deje hacer 10 repeticiones limpias."],
        ["Arrodillate con las rodillas en la almohadilla y el tronco quieto, mirando abajo.",
         "Agarrá las manijas con los brazos firmes.",
         "Llevá los talones hacia los glúteos doblando las rodillas.",
         "Apretá un segundo arriba, sin subir la cadera.",
         "Volvé lento, en tres segundos, hasta casi estirar."],
        ["Subir la cadera → cadera quieta, rodillas pegadas a la almohadilla.",
         "Tirar el tronco adelante → tronco firme, solo se mueven las rodillas.",
         "Medio recorrido y rápido → talones bien arriba y vuelta lenta."],
        ["Rodillas en la almohadilla y el eje al costado de la rodilla.",
         "Rodillo detrás del tobillo, no sobre el talón.",
         "Cadera quieta toda la serie.", "Apretá arriba y volvé en tres segundos."],
        "Isquiotibiales · Glúteos · Gemelos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Femoral #Isquiotibiales #Piernas #MaquinaDePalanca #Musculacion #Entrenamiento")}

YT32 = {
    "titulo": "Lever Military Press 🔥 Press militar en máquina | Gimnasio",
    "tags": ["lever military press", "press militar", "military press", "press de hombros en máquina",
             "hombros", "deltoides", "tríceps", "máquina de palanca", "empuje",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de hombros"],
    "descripcion": yt_desc("Lever Military Press", "press militar en máquina de palanca",
        "deltoides, sobre todo la parte de adelante, con tríceps y trapecio",
        "¿Arqueás la espalda cuando empujás? Es la forma más rápida de lastimarte la lumbar. Mirá cómo evitarlo.",
        ["Ajustá el asiento para que las manijas arranquen a la altura de los hombros.",
         "Elegí un peso liviano con el pasador para empezar."],
        ["Sentate con la espalda pegada al respaldo y los pies firmes.",
         "Agarrá las manijas con agarre prono, un poco más abiertas que los hombros.",
         "Empujá hacia arriba sin arquear la lumbar.",
         "Llegá casi a estirar, sin trabar los codos.",
         "Bajá controlado hasta la altura del hombro."],
        ["Arquear la espalda → abdomen firme y menos peso.",
         "Bajar más abajo que el hombro con dolor → frená a la altura del hombro.",
         "Trabar los codos → casi estirado, nunca trabado."],
        ["Manijas a la altura de los hombros al empezar.",
         "Espalda pegada al respaldo.", "Muñecas firmes sobre los codos.",
         "Bajá controlado, sin impulso."],
        "Deltoides · Tríceps · Trapecio",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #PressMilitar #Hombros #Deltoides #MaquinaDePalanca #Musculacion #Entrenamiento")}

save("lever-kneeling-leg-curl", kc_scenes("lever-kneeling-leg-curl"),
     {"pose": "CURL", "grip": 1, "zoom": 1.05, "dy": 100}, YT31)

save("lever-military-press", mp_scenes("lever-military-press"),
     {"pose": "MID", "grip": 0, "zoom": 1.05, "dy": 120}, YT32)
