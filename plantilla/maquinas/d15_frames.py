# Dataset D01 · D29 Assisted Wide-grip Chest Dip (Kneeling) y D30 Lever Overhand Triceps Dip: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def dip_scenes(slug, v):
    s, S, J = load(slug)
    W = S(60, -750); PIN = S(471, -133); PILE = S(420, -110)
    H_T = S(*J["TOP"]["H"]); H_B = S(*J["BOTTOM"]["H"])
    S_B = S(*J["BOTTOM"]["S"])
    PAD = S(J["TOP"]["K"][0] - 30, J["TOP"]["K"][1] + 26)
    CH_BAD = S((J[v["bad_pose"]]["S"][0] + J[v["bad_pose"]]["H"][0]) / 2,
               (J[v["bad_pose"]]["S"][1] + J[v["bad_pose"]]["H"][1]) / 2)
    return [
        hook(v["cat"], ["ASSISTED", "DIP"], v["sub_hook"], v["vo_hook"],
             [C("TOP"), seqloop("BOTTOM", "TOP", 1.4, 1.6)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Contrapeso y paralelas",
             "La máquina asistida te ayuda con un contrapeso: cuanto más peso elegís, más ayuda y menos esfuerzo.",
             [C("TOP")], [ring(PAD, 44, 0.8), lab((60, 1180), "PLATAFORMA", "start", 0.8),
                          ring(W, 36, 1.8), lab((60, 1060), "MANIJAS", "start", 1.8),
                          ring(PILE, 60, 2.8), lab((886, 1370), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["LAS", "RODILLAS"], "Sobre la plataforma", v["vo_aj1"],
             [C("TOP")], [ring(PAD, 44, 0.8), lab((60, 1180), "RODILLAS ACÁ", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["EL CONTRA", "PESO"], "Más peso, más ayuda",
             "El pasador elige el contrapeso: más placas es más ayuda. Probá con uno que te deje hacer diez repeticiones.",
             [C("TOP")], [ring(PIN, 26, 0.8), lab((880, 1470), "PASADOR", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["BRAZOS", "ESTIRADOS"], v["sub_pos"], v["vo_pos"],
             [C("TOP")], [ring(W, 36, 0.8), lab((60, 1060), v["lab_grip"], "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "LENTO"], v["sub_1"], v["vo_1"],
             [C("TOP"), TO("BOTTOM", 0.6, 1.4)],
             [arrow((512, 958), (488, 1150), 0.9, 1.2), ring(H_B, 34, 1.6)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "ABAJO"], "Sin rebote",
             "Paso dos. Abajo, pausa un segundo sin rebotar y sin encoger los hombros.",
             [C("BOTTOM")], [ring(H_B, 34, 0.8), lab((60, 1100), "PAUSA", "start", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["EMPUJÁ", "ARRIBA"], "Sin trabar los codos",
             "Paso tres. Empujá hasta estirar casi del todo, sin trabar los codos.",
             [C("BOTTOM"), TO("TOP", 0.6, 1.2)],
             [arrow((488, 1150), (512, 958), 0.9, 1.2), ring(H_T, 34, 1.6)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
             "Soltá el aire mientras empujás y tomalo mientras bajás.",
             [C("TOP"), seqloop("BOTTOM", "TOP", 1.3, 2.0, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", v["bad1"], v["sub_bad1"], v["vo_bad1"],
             [C("TOP"), TO(v["bad_pose"], 0.5, 1.0)], [NO(pos=(540, 700)), ring(CH_BAD, 46, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["ENCOGER", "LOS HOMBROS"], "Hombros abajo",
             "Error: encoger los hombros hacia las orejas. Mantenelos abajo y lejos del cuello.",
             [C("BOTTOM"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(pos=(540, 700)), ring((S_B[0], S_B[1] + 46), 40, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], v["tips"], v["vo_tips"],
             [C("TOP"), seqloop("BOTTOM", "TOP")]),
        keys("CLAVES", ["TÉCNICA"], v["keys"], v["vo_keys"], [{"cut": "BOTTOM", "at": 0.1}]),
        reps([v["reps"]], "Un minuto de pausa", v["vo_reps"],
             ["1 · BAJÁ LENTO", "2 · PAUSA", "3 · EMPUJÁ ARRIBA"], [C("TOP"), seqloop("BOTTOM", "TOP")]),
        step("AL TERMINAR", ["SALÍ", "DESPACIO"], "Dejá el peso apoyado",
             "Al terminar, estirá los brazos, sacá las rodillas con cuidado y dejá el contrapeso apoyado.",
             [C("BOTTOM"), TO("TOP", 0.8, 2.0)],
             [lab((60, 1010), "SALÍ DESPACIO", "start", 1.0)], 6.5),
    ]


def sd_scenes(slug):
    s, S, J = load(slug)
    SEAT = S(-240, -184); PIN = S(-589, -155); PILE = S(-640, -120)
    W_T = S(*J["TOP"]["W"]); W_B = S(*J["BOTTOM"]["W"])
    E_B = S(*J["LOCK_BAD"]["E"]); N_L = S(*J["LEAN_BAD"]["N"])
    return [
        hook("GIMNASIO · BRAZOS", ["TRICEPS", "DIP"], "Fondos de tríceps en máquina",
             "Lever Overhand Triceps Dip: fondos de tríceps sentado en máquina de palanca, con agarre prono.",
             [C("TOP"), seqloop("BOTTOM", "TOP", 1.3, 1.7)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Manijas a los costados",
             "La máquina de fondos tiene manijas a los costados y un respaldo: el cuerpo queda fijo y el tríceps hace todo.",
             [C("TOP")], [ring(W_T, 34, 0.8), lab((985, 1230), "MANIJAS", "end", 0.8),
                          ring(SEAT, 40, 1.8), lab((985, 1390), "ASIENTO", "end", 1.8),
                          ring(PILE, 52, 2.8), lab((60, 1430), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["LA", "ALTURA"], "Manijas a las costillas",
             "Ajustá el asiento para que, al empezar, las manijas queden a la altura de las costillas.",
             [C("TOP")], [ring(W_T, 34, 0.8), lab((985, 1230), "A LAS COSTILLAS", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
             "Elegí el peso con el pasador: uno que puedas empujar doce veces sin mover los hombros.",
             [C("TOP")], [ring(PIN, 26, 0.8), lab((60, 1407), "PASADOR", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["MANOS", "PRONAS"], "Codos apuntando atrás",
             "Espalda pegada al respaldo, manos con las palmas hacia abajo y codos apuntando atrás.",
             [C("TOP")], [ring(W_T, 34, 0.8), lab((985, 1250), "PRONO", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "ABAJO"], "Sin mover los hombros",
             "Paso uno. Empujá hacia abajo hasta casi estirar los codos, sin encoger los hombros.",
             [C("TOP"), TO("BOTTOM", 0.6, 1.4)],
             [arrow((672, 1150), (660, 1315), 0.9, 1.2), ring(W_B, 34, 1.6)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "ABAJO"], "Sin trabar los codos",
             "Paso dos. Abajo, pausa breve sin trabar los codos.",
             [C("BOTTOM")], [ring(W_B, 34, 0.8), lab((985, 1400), "PAUSA", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["SUBÍ", "LENTO"], "Hasta noventa grados",
             "Paso tres. Subí lento hasta que los codos queden a unos noventa grados.",
             [C("BOTTOM"), TO("TOP", 0.6, 1.4)],
             [arrow((660, 1315), (672, 1150), 0.9, 1.2), ring(W_T, 34, 1.6)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
             "Soltá el aire mientras empujás y tomalo mientras subís.",
             [C("TOP"), seqloop("BOTTOM", "TOP", 1.3, 2.0, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", ["TIRAR", "EL TRONCO"], "Se despega la espalda",
             "Error: tirar el tronco adelante y despegar la espalda. Es un movimiento de tríceps, no de pecho.",
             [C("TOP"), TO("LEAN_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(N_L, 46, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["TRABAR", "LOS CODOS"], "Frená antes de estirar",
             "Error: trabar los codos de golpe abajo. Frená antes de estirar del todo.",
             [C("TOP"), TO("LOCK_BAD", 0.5, 1.0)], [NO(pos=(540, 700)), ring(E_B, 44, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Espalda pegada", "Manijas a las costillas", "Codos atrás", "Sin trabar los codos"],
             "Tips: espalda pegada al respaldo, manijas a la altura de las costillas, codos atrás y sin trabar los codos.",
             [C("TOP"), seqloop("BOTTOM", "TOP")]),
        keys("CLAVES", ["TÉCNICA"], ["Empujá en 1 segundo", "Subí en 3 segundos", "Sin mover los hombros", "Recorrido completo"],
             "Claves: empujá en un segundo, subí en tres, sin mover los hombros y con recorrido completo.",
             [{"cut": "BOTTOM", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Cuando las doce salen fáciles, subí una placa.",
             ["1 · EMPUJÁ ABAJO", "2 · PAUSA", "3 · SUBÍ LENTO"], [C("TOP"), seqloop("BOTTOM", "TOP")]),
        step("AL TERMINAR", ["ACOMPAÑÁ", "LAS MANIJAS"], "Sin soltar de golpe",
             "Al terminar, acompañá las manijas hasta arriba y dejá el peso apoyado. No lo sueltes de golpe.",
             [C("BOTTOM"), TO("TOP", 0.8, 2.2)],
             [lab((60, 1010), "ACOMPAÑÁ", "start", 1.0)], 6.5),
    ]


V29 = dict(cat="GIMNASIO · PECHO", sub_hook="Fondos de pecho, agarre ancho",
           vo_hook="Assisted Wide-grip Chest Dip: fondos de pecho asistidos con las manos bien separadas.",
           vo_aj1="Apoyá las rodillas en la plataforma y agarrá las paralelas bien abiertas, con los brazos estirados.",
           sub_pos="Manos bien abiertas", lab_grip="AGARRE ANCHO",
           vo_pos="Manos más separadas que los hombros, palmas hacia abajo y el pecho adelante.",
           sub_1="Codos abiertos", vo_1="Paso uno. Bajá doblando los codos hasta que los brazos queden paralelos al piso.",
           bad_pose="UPRIGHT_BAD", bad1=["TRONCO", "DERECHO"], sub_bad1="El pecho no trabaja",
           vo_bad1="Error: quedarte derecho y con los codos pegados. Con agarre ancho el pecho va adelante.",
           tips=["Rodillas en la plataforma", "Manos bien abiertas", "Pecho adelante", "Hombros abajo"],
           vo_tips="Tips: rodillas en la plataforma, manos bien abiertas, pecho adelante y hombros abajo.",
           keys=["Bajá en 2 segundos", "Agarre ancho", "Pausa abajo", "Subí sin trabar"],
           vo_keys="Claves: bajá en dos segundos, agarre ancho, pausa abajo y subí sin trabar los codos.",
           reps="3 X 10", vo_reps="Tres series de diez, con un minuto de pausa. Cuando las diez salen fáciles, bajá el contrapeso.")

YT29 = {
    "titulo": "Assisted Wide-grip Chest Dip 🔥 Fondos de pecho agarre ancho | Gimnasio",
    "tags": ["assisted wide grip chest dip", "fondos agarre ancho", "fondos asistidos", "chest dip", "máquina asistida",
             "pecho", "pectorales", "tríceps", "empuje", "fondos en máquina",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de pecho"],
    "descripcion": yt_desc("Assisted Wide-grip Chest Dip (Kneeling)", "fondos de pecho asistidos con agarre ancho",
        "pecho, sobre todo la porción externa, con tríceps como apoyo",
        "Con las manos más abiertas el pecho se estira más abajo. Mirá cómo hacerlo en la máquina asistida.",
        ["Apoyá las rodillas en la plataforma y agarrá las paralelas bien abiertas.", "Elegí un contrapeso que te deje hacer 10 repeticiones."],
        ["Apoyá las rodillas y agarrá las paralelas con un agarre ancho y las palmas hacia abajo.",
         "Con el pecho adelante, bajá doblando los codos hasta que los brazos queden paralelos al piso.",
         "Hacé una pausa abajo sin rebotar.",
         "Empujá hasta estirar casi del todo, sin trabar los codos."],
        ["Quedarte derecho con los codos pegados → pecho adelante y codos abiertos.",
         "Encoger los hombros → hombros abajo, lejos de las orejas.",
         "Recorrido corto → bajá hasta que los brazos queden paralelos."],
        ["Rodillas en la plataforma.", "Manos más separadas que los hombros.",
         "Pecho adelante y hombros abajo.", "Bajá en dos segundos y subí sin trabar."],
        "Pectorales · Tríceps · Hombros",
        "3 series de 10 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Fondos #Pecho #AgarreAncho #AssistedDip #Musculacion #Entrenamiento")}

YT30 = {
    "titulo": "Lever Overhand Triceps Dip 🔥 Fondos de tríceps en máquina | Gimnasio",
    "tags": ["lever overhand triceps dip", "fondos de tríceps", "triceps dip", "máquina de fondos", "fondos en máquina",
             "tríceps", "brazos", "agarre prono", "máquina de palanca", "empuje",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de brazos"],
    "descripcion": yt_desc("Lever Overhand Triceps Dip", "fondos de tríceps en máquina de palanca",
        "tríceps, con pecho y hombros como apoyo",
        "La máquina te fija el cuerpo y aísla el tríceps. Mirá cómo empujar sin mover los hombros.",
        ["Ajustá el asiento para que las manijas queden a la altura de las costillas.", "Elegí un peso que puedas empujar 12 veces."],
        ["Sentate con la espalda pegada al respaldo y agarrá las manijas con agarre prono.",
         "Empujá hacia abajo hasta casi estirar los codos, sin encoger los hombros.",
         "Hacé una pausa breve abajo, sin trabar los codos.",
         "Subí lento hasta que los codos queden a unos noventa grados."],
        ["Tirar el tronco adelante → espalda pegada al respaldo.",
         "Trabar los codos abajo → frená antes de estirar del todo.",
         "Encoger los hombros → hombros abajo y lejos de las orejas."],
        ["Espalda pegada al respaldo.", "Manijas a la altura de las costillas.",
         "Codos apuntando atrás.", "Empujá en uno y subí en tres segundos."],
        "Tríceps · Pecho · Hombros",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Fondos #Triceps #MaquinaDePalanca #Brazos #Musculacion #Entrenamiento")}

save("assisted-wide-grip-chest-dip-kneeling", dip_scenes("assisted-wide-grip-chest-dip-kneeling", V29),
     {"pose": "BOTTOM", "zoom": 1.05, "dy": 90}, YT29)

save("lever-overhand-triceps-dip", sd_scenes("lever-overhand-triceps-dip"),
     {"pose": "MID", "zoom": 1.1, "dy": 100}, YT30)
