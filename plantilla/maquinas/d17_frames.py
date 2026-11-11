# Dataset D33 Lever One Arm Shoulder Press y D34 Lever Shoulder Press V2: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def oa_scenes(slug):
    s, S, J = load(slug)
    SEAT = S(-240, -184); PIN = S(-609, -199); BACK = S(-333, -484)
    W_D = S(*J["DOWN"]["W"]); W_M = S(*J["MID"]["W"]); W_U = S(*J["UP"]["W"])
    E_D = S(*J["DOWN"]["E"])
    CH_BAD = S((J["ARCH_BAD"]["S"][0] + J["ARCH_BAD"]["H"][0]) / 2,
               (J["ARCH_BAD"]["S"][1] + J["ARCH_BAD"]["H"][1]) / 2)
    W_LOW = S(*J["LOW_BAD"]["W"]); W_LOCK = S(*J["LOCK_BAD"]["W"])
    return [
        hook("GIMNASIO · HOMBROS", ["ONE ARM", "PRESS"], "Press a un brazo",
             "Lever One Arm Shoulder Press: press de hombro con un brazo en máquina de palanca. Un lado por vez.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.0)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Una manija por brazo",
             "La máquina tiene una manija por brazo, un respaldo para pegar la espalda y la pila con el pasador.",
             [C("DOWN")], [ring(W_D, 36, 0.8), lab((985, 1180), "MANIJA", "end", 0.8),
                           ring(BACK, 40, 1.8), lab((985, 1240), "RESPALDO", "end", 1.8),
                           ring(PIN, 26, 2.8), lab((60, 1378), "PESO", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Manija a la altura del hombro",
             "Ajustá el asiento para que la manija quede a la altura del hombro, ni más alta ni más baja.",
             [C("DOWN")], [ring(SEAT, 40, 0.8), lab((985, 1440), "ASIENTO", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["MENOS", "PESO"], "Un brazo mueve menos",
             "Con un brazo movés menos peso: bajá dos o tres placas respecto del press a dos brazos.",
             [C("DOWN")], [ring(PIN, 26, 0.8), lab((60, 1378), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["UN BRAZO", "FIRME"], "Codo flexionado, mano arriba",
             "Espalda pegada, pies firmes y el codo flexionado, con la mano arriba del codo.",
             [C("DOWN")], [ring(E_D, 40, 0.9), lab((985, 1253), "CODO", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "ARRIBA"], "Sin girar el tronco",
             "Paso uno. Empujá la manija hacia arriba sin girar ni inclinar el tronco de costado.",
             [C("DOWN"), TO("MID", 0.6, 0.9), TO("UP", 0.6, 0.9)],
             [arrow((W_D[0] + 26, W_D[1] - 34), (W_U[0] - 4, W_U[1] + 12), 0.9, 1.2)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["PAUSÁ", "ARRIBA"], "Casi estirado",
             "Paso dos. Arriba, pausá un segundo con el brazo casi estirado, sin trabar el codo.",
             [C("UP")], [ring(W_U, 36, 0.8)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Hasta el hombro",
             "Paso tres. Bajá lento hasta la altura del hombro, sin dejar caer el peso.",
             [C("UP"), TO("MID", 0.6, 0.9), TO("DOWN", 0.6, 1.4)],
             [arrow((W_U[0] + 20, W_U[1] - 10), (W_D[0] + 26, W_D[1] - 26), 0.9, 2.0)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
             "Soltá el aire mientras empujás hacia arriba y tomalo mientras bajás.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ESPALDA", "ARQUEADA"], "La lumbar pegada",
             "Error: arquear la espalda para empujar con un solo brazo. Apretá el abdomen y bajá el peso.",
             [C("DOWN"), TO("ARCH_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(CH_BAD, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["BAJAR", "DE MÁS"], "Frená en el hombro",
             "Error: bajar la manija mucho más abajo que el hombro. Frená a la altura del hombro.",
             [C("DOWN"), TO("LOW_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(W_LOW, 36, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["CODO", "TRABADO"], "Casi estirado, nunca trabado",
             "Error: trabar el codo arriba y empujar de más. Llegá casi estirado y empezá a bajar.",
             [C("DOWN"), TO("LOCK_BAD", 0.5, 0.8)], [NO(pos=(540, 700)), ring(W_LOCK, 36, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Un brazo por vez", "Manija a la altura del hombro",
                                          "Tronco quieto", "Pausá arriba"],
             "Tips: un brazo por vez, manija a la altura del hombro, tronco quieto y pausá arriba.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.0)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda pegada", "Codo flexionado",
                                     "Bajá en 3 segundos", "Cambiá de brazo"],
             "Claves: espalda pegada, codo flexionado, bajá en tres segundos y cambiá de brazo.",
             [{"cut": "MID", "at": 0.1}]),
        reps(["3 X 10"], "Por brazo: cambiá al terminar",
             "Tres series de ocho a diez por brazo, con un minuto y medio de pausa. Terminá un lado y pasá al otro.",
             ["1 · EMPUJÁ ARRIBA", "2 · PAUSÁ ARRIBA", "3 · BAJÁ LENTO"],
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.0)]),
        step("AL TERMINAR", ["CAMBIÁ", "DE BRAZO"], "Sin apuro",
             "Al terminar, apoyá la manija, soltá el peso y pasá al otro brazo con el mismo ajuste.",
             [C("UP"), TO("DOWN", 0.8, 2.2)],
             [lab((60, 1010), "OTRO BRAZO", "start", 1.0)], 6.5),
    ]


def sp_scenes(slug):
    s, S, J = load(slug)
    SEAT = S(-240, -190); PIN = S(-649, -155); BACK = S(-333, -484)
    W_D = S(*J["DOWN"]["W"]); W_M = S(*J["MID"]["W"]); W_U = S(*J["UP"]["W"])
    W_FWD = S(*J["FWD_BAD"]["W"])
    CH_BAD = S((J["ARCH_BAD"]["S"][0] + J["ARCH_BAD"]["H"][0]) / 2,
               (J["ARCH_BAD"]["S"][1] + J["ARCH_BAD"]["H"][1]) / 2)
    CH_SEP = S((J["SEP_BAD"]["S"][0] + J["SEP_BAD"]["H"][0]) / 2,
               (J["SEP_BAD"]["S"][1] + J["SEP_BAD"]["H"][1]) / 2)
    return [
        hook("GIMNASIO · HOMBROS", ["SHOULDER", "PRESS"], "Press de hombros en máquina",
             "Lever Shoulder Press: press de hombros en máquina de palanca, con el empuje arriba y un poco adelante.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.1, 2.0)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Agarre prono y respaldo",
             "La máquina tiene manijas con agarre prono y un respaldo que te deja la espalda bien apoyada.",
             [C("DOWN")], [ring(W_D, 36, 0.8), lab((985, 1160), "MANIJAS", "end", 0.8),
                           ring(BACK, 40, 1.8), lab((985, 1240), "RESPALDO", "end", 1.8),
                           ring(PIN, 26, 2.8), lab((60, 1409), "PESO", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Manijas a la altura del hombro",
             "Ajustá el asiento para que las manijas arranquen a la altura de los hombros.",
             [C("DOWN")], [ring(SEAT, 40, 0.8), lab((985, 1440), "ASIENTO", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí un peso liviano con el pasador: el hombro es una articulación delicada.",
             [C("DOWN")], [ring(PIN, 26, 0.8), lab((60, 1409), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["AGARRE", "PRONO"], "Algo más abiertas que los hombros",
             "Espalda pegada al respaldo y agarre prono, con las manos algo más abiertas que los hombros.",
             [C("DOWN")], [ring(W_D, 36, 0.8), lab((985, 1160), "AGARRE PRONO", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["ARRIBA", "Y ADELANTE"], "Sin despegar la espalda",
             "Paso uno. Empujá las manijas arriba y un poco adelante, sin despegar la espalda del respaldo.",
             [C("DOWN"), TO("MID", 0.6, 0.9), TO("UP", 0.6, 0.9)],
             [arrow((W_D[0] + 26, W_D[1] - 34), (W_U[0] + 16, W_U[1] + 10), 0.9, 1.2)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["PAUSÁ", "ARRIBA"], "Casi estirado",
             "Paso dos. Arriba, pausá un segundo con los brazos casi estirados, sin trabar los codos.",
             [C("UP")], [ring(W_U, 36, 0.8)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLADO"], "Hasta el hombro",
             "Paso tres. Bajá controlado hasta la altura del hombro, sin dejar caer el peso.",
             [C("UP"), TO("MID", 0.6, 0.9), TO("DOWN", 0.6, 1.4)],
             [arrow((W_U[0] + 16, W_U[1] - 10), (W_D[0] + 26, W_D[1] - 26), 0.9, 2.2)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
             "Soltá el aire mientras empujás hacia arriba y tomalo mientras bajás.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.1, 2.1, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["SE VA", "ADELANTE"], "El empuje se va de largo",
             "Error: empujar tanto adelante que el hombro se va de su lugar. Arriba, no adelante.",
             [C("DOWN"), TO("FWD_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(W_FWD, 36, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["ESPALDA", "ARQUEADA"], "La lumbar pegada",
             "Error: arquear la espalda para empujar. Apretá el abdomen y bajá el peso.",
             [C("DOWN"), TO("ARCH_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(CH_BAD, 56, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["ESPALDA", "DESPEGADA"], "El respaldo queda lejos",
             "Error: separar la espalda del respaldo para empujar. Quedate pegado de principio a fin.",
             [C("DOWN"), TO("SEP_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(CH_SEP, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Agarre prono, algo abierto", "Manijas a la altura del hombro",
                                          "Arriba y un poco adelante", "Espalda en el respaldo"],
             "Tips: agarre prono algo abierto, manijas a la altura del hombro, arriba y un poco adelante.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.1, 2.0)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda pegada", "Pies firmes",
                                     "Arriba sin trabar", "Bajá controlado"],
             "Claves: espalda pegada, pies firmes, arriba sin trabar y bajá controlado.",
             [{"cut": "MID", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto y medio de pausa",
             "Tres series de diez a doce, con un minuto y medio de pausa. Cuando salen fáciles, subí una placa.",
             ["1 · ARRIBA Y ADELANTE", "2 · PAUSÁ ARRIBA", "3 · BAJÁ AL HOMBRO"],
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.0)]),
        step("AL TERMINAR", ["ACOMPAÑÁ", "LAS MANIJAS"], "Sin soltar de golpe",
             "Al terminar, acompañá las manijas hasta la altura del hombro y dejá el peso apoyado.",
             [C("UP"), TO("DOWN", 0.8, 2.2)],
             [lab((60, 1010), "ACOMPAÑÁ", "start", 1.0)], 6.5),
    ]


YT33 = {
    "titulo": "Lever One Arm Shoulder Press 🔥 Press de hombro a un brazo | Gimnasio",
    "tags": ["lever one arm shoulder press", "press a un brazo", "one arm shoulder press",
             "press de hombros a una mano", "hombros", "deltoides", "tríceps", "unilateral",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de hombros"],
    "descripcion": yt_desc("Lever One Arm Shoulder Press", "press de hombro a un brazo en máquina de palanca",
        "deltoides, sobre todo la parte de adelante, con tríceps y trapecio",
        "¿Un hombro tira más que el otro? El press a un brazo te muestra la diferencia en la primera serie.",
        ["Ajustá el asiento para que la manija quede a la altura del hombro.",
         "Bajá dos o tres placas respecto del press a dos brazos."],
        ["Sentate con la espalda pegada al respaldo y los pies firmes.",
         "Agarrá una manija con una mano, con el codo flexionado y la mano arriba del codo.",
         "Empujá la manija hacia arriba sin girar el tronco.",
         "Pausá un segundo arriba, con el brazo casi estirado.",
         "Bajá lento hasta el hombro y cambiá de brazo al terminar la serie."],
        ["Arquear la espalda → abdomen firme y menos peso.",
         "Bajar más abajo que el hombro → frená a la altura del hombro.",
         "Trabar el codo → casi estirado, nunca trabado."],
        ["Una manija a la altura del hombro al empezar.",
         "Tronco quieto: no gires para empujar.", "Codo flexionado, mano arriba del codo.",
         "Bajá en tres segundos y cambiá de brazo."],
        "Deltoides · Tríceps · Trapecio",
        "3 series de 8–10 por brazo, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #Hombros #UnBrazo #Deltoides #MaquinaDePalanca #Musculacion #Entrenamiento")}

YT34 = {
    "titulo": "Lever Shoulder Press V2 🔥 Press de hombros en máquina | Gimnasio",
    "tags": ["lever shoulder press", "press de hombros en máquina", "shoulder press machine",
             "press de hombros", "hombros", "deltoides", "tríceps", "agarre prono",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de hombros"],
    "descripcion": yt_desc("Lever Shoulder Press V2", "press de hombros en máquina de palanca",
        "deltoides, sobre todo la parte de adelante, con tríceps y trapecio",
        "¿Empujás para adelante en vez de para arriba? Ese es el error que te deja el hombro cargado.",
        ["Ajustá el asiento para que las manijas arranquen a la altura de los hombros.",
         "Elegí un peso liviano con el pasador para empezar."],
        ["Sentate con la espalda apoyada y los pies planos en el suelo.",
         "Agarrá las manijas con agarre prono, algo más abiertas que los hombros.",
         "Empujá arriba y un poco adelante, sin despegar la espalda.",
         "Pausá arriba, con los brazos casi estirados.",
         "Bajá controlado hasta la altura del hombro."],
        ["Empujar demasiado adelante → arriba y apenas adelante.",
         "Arquear la espalda → abdomen firme y menos peso.",
         "Despegar la espalda del respaldo → quedate pegado de principio a fin."],
        ["Agarre prono, algo más abierto que los hombros.",
         "Manijas a la altura del hombro al empezar.", "Espalda pegada al respaldo.",
         "Bajá controlado, sin impulso."],
        "Deltoides · Tríceps · Trapecio",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #PressDeHombros #Hombros #Deltoides #MaquinaDePalanca #Musculacion #Entrenamiento")}

save("lever-one-arm-shoulder-press", oa_scenes("lever-one-arm-shoulder-press"),
     {"pose": "MID", "grip": 0, "zoom": 1.05, "dy": 120}, YT33)

save("lever-shoulder-press-v-2", sp_scenes("lever-shoulder-press-v-2"),
     {"pose": "UP", "grip": 0, "zoom": 1.05, "dy": 130}, YT34)
