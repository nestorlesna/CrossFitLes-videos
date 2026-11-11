# Dataset D39 Cycle Cross Trainer y D40 Lever Bicep Curl: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def cyc(prefix, n=6, t=0.18, at=0.3, until="end"): return {"seq": [[f"{prefix}{i}", t] for i in range(n)], "at": at, "until": until, "ease": "none"}


def cct_scenes(slug):
    s, S, J = load(slug)
    FLY = S(*s["props"][0]["fly"]); GRIP = S(*J["E0"]["W"])
    PED = S(J["E0"]["A"][0] + 26, J["E0"]["A"][1] + 40)
    LB, LT = (60, 820), (985, 820)
    L = lambda at=0.3: cyc("E", t=0.22, at=at)
    return [
        hook("GIMNASIO · CARDIO", ["CROSS", "TRAINER"], "Elíptica de cuerpo completo",
             "Cycle Cross Trainer: la elíptica. Cardio de cuerpo completo, sin impacto en las rodillas.",
             [C("E0"), L()]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Pedales y manijas móviles",
             "Tiene pedales grandes y manijas móviles. Trabajás piernas, glúteos y, si usás las manijas, también brazos.",
             [C("E0")], [ring(PED, 60, 0.8), lab(LB, "PEDALES", "start", 0.8),
                         ring(GRIP, 40, 1.8), lab(LT, "MANIJAS MÓVILES", "end", 1.8),
                         ring(FLY, 90, 2.8)], 7.0),
        step("AJUSTE 1", ["LA", "RESISTENCIA"], "Que no vayas por inercia",
             "Elegí una resistencia que te haga empujar. Sin resistencia, las piernas van solas por inercia.",
             [C("E0")], [ring(FLY, 90, 0.8), lab(LT, "RESISTENCIA", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["PIES", "COMPLETOS"], "Bien apoyados en los pedales",
             "Subite con la máquina quieta y apoyá los pies completos en el centro de los pedales.",
             [C("E0")], [ring(PED, 60, 0.8), lab((60, 1360), "PIE COMPLETO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["TRONCO", "ERGUIDO"], "Mirada al frente",
             "Tronco erguido, mirada al frente y las manos en las manijas móviles.",
             [C("E0")], [lab(LT, "MIRADA AL FRENTE", "end", 1.0)], 6.5),
        step("PASO 1 / 3", ["PEDALEÁ"], "Movimiento continuo",
             "Paso uno. Pedaleá con un movimiento continuo y controlado, empujando con todo el pie.",
             [C("E0"), L()], (), 6.8, numeral="1"),
        step("PASO 2 / 3", ["EMPUJÁ", "Y TIRÁ"], "Las manijas trabajan los brazos",
             "Paso dos. Empujá y tirá de las manijas alternando con las piernas: así trabajan también los brazos.",
             [C("E0"), L()], [lab(LT, "EMPUJÁ Y TIRÁ", "end", 1.0)], numeral="2"),
        step("PASO 3 / 3", ["CAMBIÁ EL", "SENTIDO"], "Hacia atrás también vale",
             "Paso tres. Podés pedalear hacia atrás un rato para cambiar el estímulo.",
             [C("E5"), {"seq": [[f"E{i}", 0.22] for i in (5, 4, 3, 2, 1, 0)], "at": 0.3, "until": "end", "ease": "none"}],
             [lab(LT, "HACIA ATRÁS", "end", 1.0)], numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Parejo",
             "Respirá parejo. A ritmo moderado tenés que poder hablar con frases cortas.",
             [C("E0"), L()], mn=6.0),
        step("ASÍ NO · 1 / 2", ["COLGARTE DE", "LAS MANIJAS"], "El peso va en las piernas",
             "Error: inclinarte y apoyar todo el peso en las manijas. Tronco erguido: el peso va en las piernas.",
             [C("E0"), TO("LEAN_BAD", 0.5, 0.8)], [NO(), ring(S(*J["LEAN_BAD"]["S"]), 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["TALONES", "ARRIBA"], "Todo el pie apoyado",
             "Error: levantar los talones y pedalear en punta de pie. Se cargan los gemelos y los pies: apoyá todo el pie.",
             [C("E0"), TO("TOES_BAD", 0.5, 0.8)], [NO(), ring(S(*J["TOES_BAD"]["A"]), 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Talón siempre apoyado", "Empujá y tirá las manijas",
                                          "Tronco erguido", "Probá hacia atrás"],
             "Tips: el talón no se despega, empujá y tirá de las manijas, tronco erguido y probá pedalear hacia atrás.",
             [C("E0"), L()]),
        keys("CLAVES", ["TÉCNICA"], ["Pies completos", "Mirada al frente",
                                     "Resistencia que se sienta", "Ritmo parejo"],
             "Claves: pies completos en los pedales, mirada al frente, una resistencia que se sienta y ritmo parejo.",
             [C("E0"), L()]),
        reps(["20 MIN"], "3 suave · 14 a ritmo · 3 suave",
             "De quince a treinta minutos. Por ejemplo: tres minutos suave, catorce a ritmo y tres minutos suave.",
             ["3 MIN SUAVE", "14 MIN RITMO", "3 MIN SUAVE"], [C("E0"), L()]),
        step("AL TERMINAR", ["FRENÁ Y", "BAJÁ"], "Con la máquina quieta",
             "Al terminar, bajá el ritmo, esperá que los pedales se detengan y recién ahí bajate.",
             [C("E0"), L()], mn=6.5),
    ]


def lcurl_scenes(slug):
    s, S, J = load(slug)
    W_D = S(*J["DOWN"]["W"]); W_M = S(*J["MID"]["W"]); W_U = S(*J["UP"]["W"])
    PIV = S(*J["DOWN"]["E"]); SEAT = S(-245, -196); PIN = S(-609, -155); BACK = S(-333, -424)
    E_BAD = S(*J["ELBOW_BAD"]["E"]); S_SW = S(*J["SWING_BAD"]["S"]); W_DR = S(*J["DROP_BAD"]["W"])
    A1 = (W_D[0] + 23, W_D[1] - 1); B1 = (W_U[0] + 19, W_U[1] + 12)
    return [
        hook("GIMNASIO · BRAZOS", ["BICEP", "CURL"], "Curl de bíceps en máquina",
             "Lever Bicep Curl: curl de bíceps sentado en máquina de palanca. Codos fijos en el eje y agarre supino.",
             [C("DOWN"), seqloop("UP", "DOWN")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Manijas, respaldo y pila",
             "La máquina tiene dos manijas, un respaldo para la espalda y la pila con el pasador.",
             [C("DOWN")], [ring(W_D, 34, 0.8), lab((985, 1370), "MANIJAS", "end", 0.8),
                           ring(BACK, 44, 1.8), lab((985, 1240), "RESPALDO", "end", 1.8),
                           ring(PIN, 26, 2.8), lab((60, 1400), "PESO", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Codos a la altura del eje",
             "Ajustá el asiento para que los codos queden justo a la altura del eje rojo de la máquina.",
             [C("DOWN")], [ring(PIV, 32, 0.8), lab((985, 1250), "EJE", "end", 1.0),
                           ring(SEAT, 40, 1.8), lab((985, 1430), "ASIENTO", "end", 1.8)], 7.2),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí el peso con el pasador: uno que te deje hacer las doce repeticiones sin mover los codos.",
             [C("DOWN")], [ring(PIN, 26, 0.8), lab((60, 1400), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "APOYADA"], "Palmas hacia arriba",
             "Espalda apoyada en el respaldo, codos pegados al eje y las palmas hacia arriba agarrando las manijas.",
             [C("DOWN")], [ring(W_D, 34, 0.8), lab((985, 1360), "AGARRE SUPINO", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ", "A LOS HOMBROS"], "Sin mover los codos",
             "Paso uno. Flexioná los codos llevando las manijas hacia los hombros, sin mover los codos del eje.",
             [C("DOWN"), TO("MID", 0.6, 0.9), TO("UP", 0.6, 0.9)],
             [arrow(A1, B1, 0.8, 1.2, [70, 0]), lab((60, 946), "SUBÍ", "start", 1.2)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ", "ARRIBA"], "Un segundo",
             "Paso dos. Arriba, apretá el bíceps un segundo sin despegar la espalda del respaldo.",
             [C("UP")], [ring(W_U, 38, 0.8), lab((985, 1130), "APRETÁ 1 SEG", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Frená antes de estirar",
             "Paso tres. Bajá lento y frená antes de estirar del todo el codo. Así cuidás el tendón.",
             [C("UP"), TO("MID", 0.6, 0.9), TO("DOWN", 0.6, 1.6)],
             [arrow(B1, A1, 1.0, 1.2, [60, 0]), lab((60, 946), "BAJÁ LENTO", "start", 1.4)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
             "Soltá el aire mientras subís y tomalo mientras bajás.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.1, 2.0, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["CODOS", "ADELANTE"], "El codo no se mueve",
             "Error: adelantar los codos para subir el peso. El codo queda fijo en el eje: si se mueve, es mucho peso.",
             [C("DOWN"), TO("ELBOW_BAD", 0.5, 1.0)], [NO(), ring(E_BAD, 44, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TIRARTE", "ATRÁS"], "La espalda en el respaldo",
             "Error: tirarte atrás y despegar la espalda para ayudarte. Espalda apoyada y menos peso.",
             [C("DOWN"), TO("SWING_BAD", 0.5, 0.7)], [NO(), ring(S_SW, 56, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["ESTIRAR", "DE GOLPE"], "Bajá en tres segundos",
             "Error: bajar de golpe y estirar del todo el codo. Bajá en tres segundos y frená antes de estirar.",
             [C("UP"), TO("DROP_BAD", 0.4, 0.5)], [NO(), ring(W_DR, 34, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Codos fijos en el eje", "Espalda en el respaldo",
                                          "Apretá arriba", "Bajá en 3 segundos"],
             "Tips: codos fijos en el eje, espalda en el respaldo, apretá arriba y bajá en tres segundos.",
             [C("DOWN"), seqloop("UP", "DOWN")]),
        keys("CLAVES", ["TÉCNICA"], ["Agarre supino", "Muñecas firmes",
                                     "Sin mover los codos", "Frená antes de estirar"],
             "Claves: agarre supino, muñecas firmes, sin mover los codos y frená antes de estirar del todo.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Cuando las doce salen fáciles, subí una placa.",
             ["1 · SUBÍ", "2 · APRETÁ", "3 · BAJÁ LENTO"], [C("DOWN"), seqloop("UP", "DOWN")]),
        step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
             "Al terminar, acompañá las manijas y dejá el peso apoyado. No lo sueltes de golpe.",
             [C("UP"), TO("DOWN", 0.8, 2.2)],
             [lab((60, 946), "DEJÁ EL PESO", "start", 1.0)], 6.5),
    ]


YT39 = {
    "titulo": "Cycle Cross Trainer 🔥 Cómo usar la elíptica bien | Gimnasio",
    "tags": ["cycle cross trainer", "elíptica", "cross trainer", "elíptico", "cómo usar la elíptica",
             "cardio sin impacto", "cardio", "cuerpo completo", "máquinas de gimnasio",
             "gimnasio", "principiantes", "rutina de cardio"],
    "descripcion": yt_desc("Cycle Cross Trainer", "elíptica o cross trainer",
        "cardio de cuerpo completo sin impacto en las rodillas",
        "¿Vas en la elíptica colgado de las manijas o en punta de pie? Así se pierde gran parte del trabajo. Este video es para vos.",
        ["Subite con la máquina quieta y apoyá los pies completos en los pedales.",
         "Elegí una resistencia que te haga empujar y no te deje ir por inercia."],
        ["Tronco erguido, mirada al frente y manos en las manijas móviles.",
         "Pedaleá con un movimiento continuo y controlado, empujando con todo el pie.",
         "Empujá y tirá de las manijas alternando con las piernas.",
         "Probá pedalear hacia atrás un rato para cambiar el estímulo.",
         "Al terminar, frená y bajate con los pedales quietos."],
        ["Colgarte de las manijas → el peso va en las piernas y el tronco erguido.",
         "Levantar los talones → todo el pie apoyado en el pedal.",
         "Ir sin resistencia → subí la resistencia y controlá el ritmo."],
        ["El talón no se despega del pedal.", "Empujá y tirá de las manijas: trabajan los brazos.",
         "Tronco erguido, mirada al frente.", "Probá pedalear hacia atrás para cambiar el estímulo.",
         "Subí la resistencia para no ir solo por inercia."],
        "Cuádriceps · Glúteos · Isquiotibiales · Pecho · Espalda · Brazos",
        "15 a 30 minutos a ritmo moderado. Nivel: principiante.",
        "#Gimnasio #Eliptica #Cardio #CrossTrainer #Entrenamiento #CardioSinImpacto")}

YT40 = {
    "titulo": "Lever Bicep Curl 🔥 Curl de bíceps en máquina de palanca | Gimnasio",
    "tags": ["lever bicep curl", "curl de bíceps en máquina", "bicep curl machine", "curl en máquina",
             "bíceps", "braquial", "antebrazos", "máquina de palanca", "máquinas de gimnasio",
             "gimnasio", "principiantes", "rutina de brazos"],
    "descripcion": yt_desc("Lever Bicep Curl", "curl de bíceps en máquina de palanca",
        "bíceps, con braquial y antebrazos como apoyo",
        "¿Subís el peso adelantando los codos? Ahí el bíceps deja de trabajar. Mirá cómo se hace bien.",
        ["Ajustá el asiento para que los codos queden a la altura del eje.",
         "Elegí un peso que puedas subir doce veces sin mover los codos."],
        ["Sentate con la espalda apoyada y las palmas hacia arriba.",
         "Agarrá las manijas con agarre supino, con los codos pegados al eje.",
         "Flexioná los codos llevando las manijas hacia los hombros, sin mover los codos.",
         "Apretá arriba un segundo y bajá lento, frenando antes de estirar."],
        ["Adelantar los codos para subir → el codo queda fijo en el eje.",
         "Tirarte atrás despegando la espalda → espalda apoyada y menos peso.",
         "Estirar de golpe abajo → bajá en tres segundos."],
        ["Codos fijos a la altura del eje.", "Espalda apoyada en el respaldo.",
         "Apretá arriba un segundo.", "Bajá en tres segundos, sin soltar el peso."],
        "Bíceps · Braquial · Antebrazos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Biceps #CurlDeBiceps #MaquinaDePalanca #Brazos #Musculacion #Entrenamiento")}

save("cycle-cross-trainer", cct_scenes("cycle-cross-trainer"),
     {"pose": "E0", "grip": 1, "zoom": 1.05, "dy": 120}, YT39)

save("lever-bicep-curl", lcurl_scenes("lever-bicep-curl"),
     {"pose": "UP", "zoom": 1.15, "dy": 110}, YT40)
