# Dataset D01 · D22 Lever Seated Reverse Fly y D23 Lever Seated Reverse Fly (Parallel Grip): escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def scenes(slug, grip, sub_hook, vo_hook):
    s, S, J = load(slug)
    PIV = S(-230, -839); SEAT = S(-240, -184); PAD = S(-185, -340)
    HAND_F = S(*J["FRONT"]["W"]); HAND_B = S(*J["BACK"]["W"])
    ELB = S(*J["ELBOW_BAD"]["E"]); SH_B = S(*J["LEAN_BAD"]["S"])
    PILE = S(-640, -70); PIN = S(-589, -177)
    AX = (HAND_F[0] - 10, HAND_F[1] - 40); BX = (HAND_B[0] + 18, HAND_B[1] - 40)
    return [
        hook("GIMNASIO · HOMBROS", ["REVERSE", "FLY"], sub_hook, vo_hook,
             [C("FRONT"), seqloop("BACK", "FRONT")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Aperturas inversas",
             "La máquina de aperturas inversas: apoyo de pecho, manijas adelante y pila de peso atrás.",
             [C("FRONT")], [ring(PAD, 44, 0.8), lab((60, 1285), "APOYO", "start", 0.8),
                            ring(HAND_F, 34, 1.8), lab((985, 1120), "MANIJAS", "end", 1.8),
                            ring(PILE, 44, 2.6), lab((60, 1430), "PILA", "start", 2.6)], 7.0),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Manijas a la altura del pecho",
             "Ajustá el asiento para que las manijas queden a la altura del pecho, con los brazos casi horizontales.",
             [C("FRONT")], [ring(SEAT, 40, 0.8), lab((985, 1430), "ASIENTO", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Liviano para empezar",
             "Elegí el peso con el pasador. Empezá liviano: en la apertura el hombro queda expuesto.",
             [C("FRONT")], [ring(PIN, 26, 0.8), lab((60, 1393), "PASADOR", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["BRAZOS", "ADELANTE"], "Codos apenas flexionados",
             "Apoyá el pecho, agarrá las manijas adelante y dejá los codos apenas flexionados y fijos.",
             [C("FRONT")], [ring(HAND_F, 34, 0.8), lab((985, 1290), grip, "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["ABRÍ", "LOS BRAZOS"], "Atrás y afuera",
             "Paso uno. Abrí los brazos hacia atrás y afuera, juntando las escápulas, sin mover los codos.",
             [C("FRONT"), TO("MID", 0.6, 0.9), TO("BACK", 1.5, 1.0)],
             [arrow(AX, BX, 0.8, 1.2, [0, -50]), lab((60, 1010), "ABRÍ", "start", 1.2)], numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "ATRÁS"], "Escápulas juntas",
             "Paso dos. Hacé una pausa atrás, con las escápulas bien juntas y el pecho en el apoyo.",
             [C("BACK")], [ring(HAND_B, 36, 0.8), lab((60, 1010), "APRETÁ", "start", 1.0)], numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin soltar el peso",
             "Paso tres. Volvé lento a la posición inicial, controlando el peso en todo el recorrido.",
             [C("BACK"), TO("MID", 0.6, 0.9), TO("FRONT", 1.5, 1.1)],
             [arrow(BX, AX, 0.8, 1.2, [0, -50]), lab((60, 1010), "VOLVÉ LENTO", "start", 1.2)], numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al abrir",
             "Soltá el aire al abrir y tomalo al volver. No aguantes el aire.",
             [C("FRONT"), seqloop("BACK", "FRONT", 1.1, 1.9, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", ["DOBLAR", "LOS CODOS"], "Se vuelve un remo",
             "Error: doblar los codos para tirar. Los codos quedan apenas flexionados y fijos.",
             [C("FRONT"), TO("ELBOW_BAD", 0.5, 0.9)], [NO(), ring(ELB, 46, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["DESPEGAR", "EL PECHO"], "Pecho en el apoyo",
             "Error: despegar el pecho del apoyo y usar el torso. Quedate bien apoyado.",
             [C("FRONT"), TO("LEAN_BAD", 0.5, 0.9)], [NO(), ring(SH_B, 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pecho apoyado", "Codos casi fijos", "Abrí a la línea", "Sin encoger"],
             "Tips de profe: pecho apoyado, codos casi fijos, abrí hasta la línea del hombro y no encojas los hombros.",
             [C("FRONT"), seqloop("BACK", "FRONT")]),
        keys("CLAVES", ["TÉCNICA"], ["Pecho en el apoyo", "Codos fijos", "Pausa atrás", "Volvé lento"],
             "Claves: pecho en el apoyo, codos fijos, pausa atrás y volvé lento.",
             [{"cut": "BACK", "at": 0.1}]),
        reps(["3 X 12-15"], "Cuarenta y cinco segundos",
             "Tres series de doce a quince, con cuarenta y cinco segundos de pausa. Subí cuando salgan fáciles.",
             ["1 · ABRÍ", "2 · APRETÁ", "3 · VOLVÉ LENTO"], [C("FRONT"), seqloop("BACK", "FRONT")]),
        step("AL TERMINAR", ["DEJÁ LAS", "MANIJAS"], "Sin soltar de golpe",
             "Al terminar, acompañá las manijas y dejá el peso apoyado. No lo sueltes de golpe.",
             [C("BACK"), TO("MID", 0.8, 0.9), TO("FRONT", 2.0, 1.1)],
             [lab((60, 1010), "DEJÁ LAS MANIJAS", "start", 1.0)], 6.5),
    ]


YT22 = {
    "titulo": "Lever Seated Reverse Fly 🔥 Aperturas inversas en máquina | Gimnasio",
    "tags": ["lever seated reverse fly", "aperturas inversas", "reverse fly", "deltoides posterior",
             "hombro posterior", "pec deck inverso", "máquina de palanca", "máquinas de gimnasio", "gimnasio",
             "principiantes", "rutina de hombros", "hombros"],
    "descripcion": yt_desc("Lever Seated Reverse Fly", "aperturas inversas en máquina",
        "deltoides posterior, con trapecios y romboides como apoyo",
        "¿Querés hombros más completos? Las aperturas inversas atacan la parte de atrás del hombro. Mirá cómo se usan.",
        ["Ajustá el asiento para que las manijas queden a la altura del pecho.", "Elegí un peso liviano para empezar."],
        ["Sentate con el pecho contra la almohadilla y los pies planos.",
         "Agarrá las manijas adelante, con los codos apenas flexionados.",
         "Abrí los brazos hacia atrás y afuera, juntando las escápulas.",
         "Hacé una pausa atrás y volvé lento a la posición inicial."],
        ["Doblar los codos → se vuelve un remo.", "Despegar el pecho del apoyo → quedate apoyado.",
         "Abrir más allá de la línea del hombro → frená ahí."],
        ["Pecho apoyado en la almohadilla.", "Codos apenas flexionados y fijos.", "Abrí hasta la línea del hombro.",
         "Pausa atrás y volvé lento."],
        "Deltoides posterior · Trapecios · Romboides",
        "3 series de 12–15 repeticiones, con 45 segundos de pausa. Nivel: principiante.",
        "#Gimnasio #ReverseFly #Hombros #DeltoidesPosterior #Espalda #Musculacion #Entrenamiento")}

YT23 = {
    "titulo": "Lever Seated Reverse Fly (Parallel Grip) 🔥 Aperturas inversas agarre paralelo | Gimnasio",
    "tags": ["lever seated reverse fly parallel grip", "aperturas inversas", "reverse fly", "agarre paralelo",
             "deltoides posterior", "hombro posterior", "pec deck inverso", "máquina de palanca",
             "máquinas de gimnasio", "gimnasio", "principiantes", "hombros"],
    "descripcion": yt_desc("Lever Seated Reverse Fly (Parallel Grip)", "aperturas inversas con agarre paralelo",
        "deltoides posterior, con trapecios y romboides como apoyo",
        "Con las palmas enfrentadas el hombro queda más cómodo. Mirá cómo hacer las aperturas inversas con agarre paralelo.",
        ["Ajustá el asiento para que las manijas queden a la altura del pecho.", "Elegí un peso liviano para empezar."],
        ["Sentate con el pecho contra la almohadilla y los pies planos.",
         "Agarrá las manijas con las palmas enfrentadas y los codos apenas flexionados.",
         "Abrí los brazos hacia atrás y afuera, juntando las escápulas.",
         "Hacé una pausa atrás y volvé lento a la posición inicial."],
        ["Doblar los codos → se vuelve un remo.", "Despegar el pecho del apoyo → quedate apoyado.",
         "Abrir más allá de la línea del hombro → frená ahí."],
        ["Pecho apoyado en la almohadilla.", "Palmas enfrentadas y codos casi fijos.",
         "Abrí hasta la línea del hombro.", "Pausa atrás y volvé lento."],
        "Deltoides posterior · Trapecios · Romboides",
        "3 series de 12–15 repeticiones, con 45 segundos de pausa. Nivel: principiante.",
        "#Gimnasio #ReverseFly #Hombros #DeltoidesPosterior #AgarreParalelo #Musculacion #Entrenamiento")}

save("lever-seated-reverse-fly",
     scenes("lever-seated-reverse-fly", "AGARRE PRONO", "Aperturas inversas",
            "Lever Seated Reverse Fly: aperturas inversas en máquina para la parte de atrás del hombro. Pecho apoyado y codos casi fijos."),
     {"pose": "BACK", "zoom": 1.05, "dy": 100}, YT22)

save("lever-seated-reverse-fly-parallel-grip",
     scenes("lever-seated-reverse-fly-parallel-grip", "AGARRE PARALELO", "Agarre paralelo",
            "Lever Seated Reverse Fly con agarre paralelo: palmas enfrentadas y el mismo movimiento para la parte de atrás del hombro."),
     {"pose": "BACK", "zoom": 1.05, "dy": 100}, YT23)
