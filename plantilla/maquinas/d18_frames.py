# Dataset D35 Lever Shoulder Press V3 y D36 Lever Calf Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def sp3_scenes(slug):
    s, S, J = load(slug)
    SEAT = S(-240, -196); PIN = S(-589, -133); BACK = S(-338, -470)
    W_D = S(*J["DOWN"]["W"]); W_M = S(*J["MID"]["W"]); W_U = S(*J["UP"]["W"])
    CH_BAD = S((J["ARCH_BAD"]["S"][0] + J["ARCH_BAD"]["H"][0]) / 2,
               (J["ARCH_BAD"]["S"][1] + J["ARCH_BAD"]["H"][1]) / 2)
    W_LOW = S(*J["LOW_BAD"]["W"]); W_LOCK = S(*J["LOCK_BAD"]["W"])
    return [
        hook("GIMNASIO · HOMBROS", ["SHOULDER", "PRESS"], "Press de hombros en máquina",
             "Lever Shoulder Press V3: press de hombros en máquina de palanca, con empuje casi vertical.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.1, 2.0)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Manijas, respaldo y pila",
             "La máquina tiene dos manijas, un respaldo alto para la espalda y la pila con el pasador.",
             [C("DOWN")], [ring(W_D, 36, 0.8), lab((985, 1150), "MANIJAS", "end", 0.8),
                           ring(BACK, 40, 1.8), lab((985, 1260), "RESPALDO", "end", 1.8),
                           ring(PIN, 26, 2.8), lab((60, 1425), "PESO", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Manijas a la altura del hombro",
             "Ajustá el asiento para que las manijas arranquen a la altura de los hombros.",
             [C("DOWN")], [ring(SEAT, 40, 0.8), lab((985, 1436), "ASIENTO", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí un peso que te deje hacer las doce repeticiones sin mover el tronco.",
             [C("DOWN")], [ring(PIN, 26, 0.8), lab((60, 1425), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "APOYADA"], "Manos a la altura del hombro",
             "Espalda apoyada en el respaldo y manos a la altura del hombro, con los codos abajo.",
             [C("DOWN")], [ring(W_D, 36, 0.8), lab((985, 1150), "MANOS AL HOMBRO", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "CASI VERTICAL"], "Sin sacar la espalda",
             "Paso uno. Empujá las manijas casi vertical, sin sacar la espalda del respaldo.",
             [C("DOWN"), TO("MID", 0.6, 0.9), TO("UP", 0.6, 0.9)],
             [arrow((W_D[0] + 26, W_D[1] - 34), (W_U[0] + 16, W_U[1] + 10), 0.9, 1.2)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["PAUSÁ", "ARRIBA"], "Sin trabar los codos",
             "Paso dos. Arriba, pausá un segundo con los codos casi estirados, sin trabarlos.",
             [C("UP")], [ring(W_U, 36, 0.8)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLADO"], "Hasta el hombro",
             "Paso tres. Bajá controlado hasta la altura del hombro, sin soltar el peso de golpe.",
             [C("UP"), TO("MID", 0.6, 0.9), TO("DOWN", 0.6, 1.4)],
             [arrow((W_U[0] + 16, W_U[1] - 10), (W_D[0] + 26, W_D[1] - 26), 0.9, 2.2)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
             "Soltá el aire mientras empujás y tomalo mientras bajás.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.1, 2.1, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ESPALDA", "ARQUEADA"], "La lumbar pegada",
             "Error: arquear la lumbar para empujar. Apretá el abdomen y bajá el peso.",
             [C("DOWN"), TO("ARCH_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(CH_BAD, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["BAJAR", "DE MÁS"], "Frená en el hombro",
             "Error: bajar las manijas más abajo que el hombro. Frená a la altura del hombro.",
             [C("DOWN"), TO("LOW_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(W_LOW, 36, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["CODOS", "TRABADOS"], "Casi estirado, nunca trabado",
             "Error: trabar los codos arriba y empujar de más. Llegá casi estirado y empezá a bajar.",
             [C("DOWN"), TO("LOCK_BAD", 0.5, 0.8)], [NO(pos=(540, 700)), ring(W_LOCK, 36, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Manijas a la altura del hombro", "Empuje casi vertical",
                                          "Espalda en el respaldo", "Codos sin trabar"],
             "Tips: manijas a la altura del hombro, empuje casi vertical, espalda en el respaldo y codos sin trabar.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.1, 2.0)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda apoyada", "Pies firmes",
                                     "Pausá arriba", "Bajá controlado"],
             "Claves: espalda apoyada, pies firmes, pausá arriba y bajá controlado.",
             [{"cut": "MID", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto y medio de pausa",
             "Tres series de diez a doce, con un minuto y medio de pausa. Si no llegás a las diez, bajá una placa.",
             ["1 · EMPUJÁ VERTICAL", "2 · PAUSÁ ARRIBA", "3 · BAJÁ AL HOMBRO"],
             [C("DOWN"), seqloop("UP", "DOWN", 1.0, 2.0)]),
        step("AL TERMINAR", ["ACOMPAÑÁ", "LAS MANIJAS"], "Sin soltar de golpe",
             "Al terminar, acompañá las manijas hasta la altura del hombro y dejá el peso apoyado.",
             [C("UP"), TO("DOWN", 0.8, 2.2)],
             [lab((60, 1010), "ACOMPAÑÁ", "start", 1.0)], 6.5),
    ]


def cf_scenes(slug):
    s, S, J = load(slug)
    PAD = S(J["MID"]["K"][0] - 50, J["MID"]["K"][1] - 52); STEP = S(100, -96); PIN = S(-569, -155)
    A_DN = S(*J["DOWN"]["A"]); A_UP = S(*J["UP"]["A"]); SH_B = S(*J["PUSH_BAD"]["S"])
    return [
        hook("GIMNASIO · PIERNAS", ["CALF", "PRESS"], "Gemelos en prensa de palanca",
             "Lever Calf Press: gemelos en prensa de palanca. Empujá la almohadilla hacia abajo con la punta del pie.",
             [C("MID"), seqloop("UP", "DOWN")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Almohadilla y respaldo",
             "La máquina tiene una almohadilla para la punta de los pies, un respaldo y la pila con el pasador.",
             [C("MID")], [ring(PAD, 60, 0.8), lab((985, 1180), "ALMOHADILLA", "end", 0.8),
                          ring(STEP, 50, 1.8), lab((985, 1430), "PUNTA", "end", 1.8),
                          ring(PIN, 26, 2.8), lab((60, 1400), "PESO", "start", 2.8)], 7.0),
        step("AJUSTE 1", ["LA", "ALMOHADILLA"], "Punta en el borde",
             "Apoyá la punta de los pies en el borde de la almohadilla, con los talones en el aire.",
             [C("MID")], [ring(STEP, 50, 0.8), lab((985, 1430), "PUNTA", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí el peso con el pasador. Si el talón no baja del todo, es mucho peso.",
             [C("MID")], [ring(PIN, 26, 0.8), lab((60, 1400), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["SENTADO", "DERECHO"], "Talones en el aire",
             "Sentado derecho, con las manos sosteniendo el cuerpo y los talones flotando.",
             [C("MID")], [ring(A_DN, 44, 1.6)], 6.5),
        step("PASO 1 / 3", ["BAJÁ EL", "TALÓN"], "Despacio",
             "Paso uno. Bajá el talón despacio hasta estirar bien la pantorrilla.",
             [C("MID"), TO("DOWN", 0.6, 1.8)],
             [ring(A_DN, 44, 1.6)], 6.5, numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "ABAJO"], "Sin rebote",
             "Paso dos. Abajo, pausá estirando la pantorrilla. Nada de rebotar.",
             [C("DOWN")], [ring(A_DN, 44, 0.8), lab((985, 1440), "PAUSA", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["EMPUJÁ", "ABAJO"], "Lento, bien arriba",
             "Paso tres. Empujá la almohadilla hacia abajo estirando los tobillos y apretá un segundo.",
             [C("DOWN"), TO("UP", 0.6, 1.4)],
             [ring(A_UP, 44, 1.6), lab((985, 1225), "APRETÁ ARRIBA", "end", 1.6)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
             "Soltá el aire mientras empujás hacia abajo y tomalo mientras subís los talones.",
             [C("MID"), seqloop("UP", "DOWN", 1.4, 2.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", ["RECORRIDO", "CORTO"], "Bajá todo, sin rebote",
             "Error: rebotar abajo y hacer medio recorrido. Bajá todo, pausá y subí todo.",
             [C("MID"), seqloop("DOWN", "MID", 0.3, 0.3, 0.5)],
             [NO(at=1.0), ring(A_DN, 44, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["EMPUJAR CON", "EL CUERPO"], "Las manos no empujan",
             "Error: empujar con las manos o tirar el tronco adelante. Si pasa, el peso es mucho: bajalo.",
             [C("MID"), TO("PUSH_BAD", 0.5, 1.0)], [NO(), ring(SH_B, 56, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Punta en el borde", "Talón bien abajo",
                                          "Pausa sin rebote", "Empujá con el tobillo"],
             "Tips: punta en el borde, talón bien abajo, pausa sin rebote y empujá con el tobillo.",
             [C("MID"), seqloop("UP", "DOWN")]),
        keys("CLAVES", ["TÉCNICA"], ["Talones afuera", "Rango completo",
                                     "Apretá abajo", "Volvé lento"],
             "Claves: talones afuera, rango completo, apretá abajo y volvé lento.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15"], "Un minuto de pausa",
             "Tres series de quince, con un minuto de pausa. Cuando las quince salen fáciles, subí el peso.",
             ["1 · BAJÁ EL TALÓN", "2 · PAUSA ABAJO", "3 · EMPUJÁ ABAJO"],
             [C("MID"), seqloop("UP", "DOWN")]),
        step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
             "Al terminar, acompañá la almohadilla y dejá el peso apoyado antes de sacar los pies.",
             [C("UP"), TO("DOWN", 0.8, 2.2)],
             [lab((60, 1010), "DEJÁ EL PESO", "start", 1.0)], 6.5),
    ]


YT35 = {
    "titulo": "Lever Shoulder Press V3 🔥 Press de hombros en máquina | Gimnasio",
    "tags": ["lever shoulder press", "press de hombros en máquina", "shoulder press machine",
             "press de hombros", "hombros", "deltoides", "tríceps", "empuje vertical",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de hombros"],
    "descripcion": yt_desc("Lever Shoulder Press V3", "press de hombros en máquina de palanca",
        "deltoides, sobre todo la parte de adelante, con tríceps y trapecio",
        "¿Empujás y se te despega la espalda del respaldo? Ahí es donde el hombro empieza a quejarse.",
        ["Ajustá el asiento para que las manijas arranquen a la altura de los hombros.",
         "Elegí un peso que te deje hacer las doce repeticiones sin mover el tronco."],
        ["Sentate con la espalda apoyada y los pies firmes en el suelo.",
         "Agarrá las manijas con las manos a la altura del hombro.",
         "Empujá casi vertical, sin sacar la espalda del respaldo.",
         "Pausá arriba un segundo, con los codos casi estirados.",
         "Bajá controlado hasta el hombro."],
        ["Arquear la lumbar → abdomen firme y menos peso.",
         "Bajar más abajo que el hombro → frená a la altura del hombro.",
         "Trabar los codos arriba → casi estirado, nunca trabado."],
        ["Manijas a la altura del hombro al empezar.",
         "Empuje casi vertical, no hacia adelante.", "Espalda apoyada en el respaldo.",
         "Bajá controlado, sin soltar el peso."],
        "Deltoides · Tríceps · Trapecio",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #PressDeHombros #Hombros #Deltoides #MaquinaDePalanca #Musculacion #Entrenamiento")}

YT36 = {
    "titulo": "Lever Calf Press 🔥 Gemelos en prensa de palanca | Gimnasio",
    "tags": ["lever calf press", "prensa de gemelos", "calf press", "gemelos en máquina",
             "gemelos", "pantorrilla", "sóleo", "piernas", "máquina de palanca",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Lever Calf Press", "gemelos en prensa de palanca",
        "gemelos y sóleo, con el tobillo como único motor",
        "¿Hacés rebotar el talón? Ese es el atajo que te deja los gemelos igual. Mirá cómo se hace bien.",
        ["Apoyá la punta de los pies en el borde de la almohadilla, con los talones en el aire.",
         "Elegí el peso con el pasador: si el talón no baja del todo, es mucho peso."],
        ["Sentate derecho, con las manos sosteniendo el cuerpo.",
         "Bajá el talón despacio hasta estirar la pantorrilla.",
         "Pausá abajo, sin rebotar.",
         "Empujá la almohadilla hacia abajo estirando los tobillos.",
         "Apretá arriba un segundo y volvé lento."],
        ["Rebotar abajo y hacer medio recorrido → bajá todo, pausá y subí todo.",
         "Empujar con las manos o tirar el tronco adelante → si pasa, el peso es mucho."],
        ["Punta en el borde de la almohadilla, talones en el aire.",
         "Talón bien abajo, pantorrilla estirada.", "Pausa abajo sin rebote.",
         "Empujá con el tobillo, no con la rodilla."],
        "Gemelos · Sóleo",
        "3 series de 15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Pantorrilla #Piernas #PrensaDeGemelos #MaquinaDePalanca #Entrenamiento")}

save("lever-shoulder-press-v-3", sp3_scenes("lever-shoulder-press-v-3"),
     {"pose": "MID", "grip": 0, "zoom": 1.05, "dy": 120}, YT35)

save("lever-calf-press", cf_scenes("lever-calf-press"),
     {"pose": "UP", "zoom": 1.1, "dy": 100}, YT36)
