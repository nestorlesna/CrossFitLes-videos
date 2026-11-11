# Dataset D01 · D14 Lever Front Pulldown y D15 Lever One Arm Lateral Wide Pulldown: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.4, tb=1.2, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}
# pila del latpulldown: base 10, 14 placas de 22 → centro de la placa `pin` en -298 + (pin - 0.5) * 22
PIN = lambda cx, pin: (cx + 51, -298 + (pin - 0.5) * 22)


# ═════════════ D14 · LEVER FRONT PULLDOWN ═════════════
s, S, J = load("lever-front-pulldown"); pr = s["props"][0]
PINP = S(*PIN(pr["x"], pr["pin"])); ROLL = S(*pr["pad"])
WS, WP = S(*J["TOP"]["W"]), S(*J["PULL"]["W"])
SH = S(*J["PULL"]["S"]); NECKW = S(*J["NECK_BAD"]["W"]); LEANS = S(*J["LEAN_BAD"]["S"])
L = lambda: seqloop("PULL", "TOP", 1.0, 2.0)
F = [
    hook("GIMNASIO · ESPALDA", ["FRONT", "PULLDOWN"], "Jalón al pecho en máquina",
         "Lever Front Pulldown: el jalón al pecho en máquina de palanca, con las rodillas bajo la almohadilla.",
         [C("TOP"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Rodillas bajo la almohadilla",
         "Las asas bajan al pecho y las rodillas quedan bajo la almohadilla. Trabaja dorsales y bíceps.",
         [C("TOP")], [ring(WS, 36, 0.8), lab((985, 1010), "ASAS ARRIBA", "end", 0.8),
                      ring(ROLL, 40, 1.8), lab((60, 1330), "RODILLAS", "start", 1.8),
                      ring(PINP, 30, 2.6), lab((60, 1440), "PASADOR", "start", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Rodillas bajo la almohadilla",
         "Ajustá el asiento para que las rodillas queden justo bajo la almohadilla y los pies planos en el suelo.",
         [C("TOP")], [ring(ROLL, 40, 0.8), lab((60, 1330), "RODILLAS", "start", 1.0)], 7.0),
    step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
         "Elegí el peso con el pasador: uno que puedas bajar diez veces sin mover el cuerpo.",
         [C("TOP")], [ring(PINP, 30, 0.8), lab((60, 1440), "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["PECHO", "ALTO"], "Agarre ancho, erguido",
         "Sentate erguido con el pecho alto y los hombros atrás. Agarrá las asas con agarre prono, un poco más abiertas que los hombros.",
         [C("TOP")], [lab((60, 1120), "PECHO ALTO", "start", 1.0), ring(WS, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["BAJÁ", "AL PECHO"], "Sin mover el cuerpo",
         "Paso uno. Tirá de las asas hacia el pecho activando los dorsales, sin mover el torso.",
         [C("TOP"), TO("MID", 0.6, 1.0), TO("PULL", 1.6, 1.0)],
         [arrow((WS[0] + 40, WS[1] - 24), (WP[0], WP[1] - 24), 0.8, 1.1), lab((985, 1240), "AL PECHO", "end", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["JUNTÁ LOS", "OMÓPLATOS"], "Pausa abajo",
         "Paso dos. Apretá los omóplatos y hacé una pausa breve abajo, con las asas en el pecho.",
         [C("PULL")], [ring(SH, 44, 0.8), lab((60, 1100), "OMÓPLATOS JUNTOS", "start", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["SOLTÁ", "LENTO"], "Sin que se apoye",
         "Paso tres. Soltá las asas despacio hasta la posición inicial, sin dejar que las placas se apoyen.",
         [C("PULL"), TO("TOP", 0.6, 2.2)], [ring(PINP, 34, 1.8), lab((60, 1440), "SIN APOYAR", "start", 1.8)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al tirar",
         "Soltá el aire mientras tirás y tomalo mientras volvés. No aguantes el aire.",
         [C("TOP"), seqloop("PULL", "TOP", 1.0, 2.2, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["JALAR", "AL CUELLO"], "Asas al pecho",
         "Error: jalar las asas al cuello o por detrás de la nuca. Las asas van al pecho, nunca al cuello.",
         [C("TOP"), TO("NECK_BAD", 0.5, 0.9)], [NO(), ring(NECKW, 44, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["COLUMPIAR", "EL CUERPO"], "Sin impulso",
         "Error: columpiar el cuerpo hacia atrás para tirar. Quedate erguido y usá la espalda, no el impulso.",
         [C("TOP"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.0), ring(LEANS, 52, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Asas al pecho", "Pecho alto", "Omóplatos juntos", "Soltá sin apoyar"],
         "Tips de profe: asas al pecho, pecho alto, omóplatos juntos y soltá sin apoyar las placas.",
         [C("TOP"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Pecho alto", "Sin impulso", "Codos abajo", "Soltá lento"],
         "Claves: pecho alto, sin impulso, codos abajo y soltá lento.",
         [{"cut": "PULL", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce, con un minuto y medio de pausa. Cuando las doce salgan fáciles, subí una placa.",
         ["1 · BAJÁ AL PECHO", "2 · APRETÁ", "3 · SOLTÁ LENTO"], [C("TOP"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, soltá las asas despacio y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("TOP"), TO("MID", 1.0, 1.0), TO("TOP", 2.2, 1.2)], [lab((60, 1440), "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-front-pulldown", F, {"pose": "PULL", "grip": 1, "zoom": 1.12, "dy": 130}, {
    "titulo": "Lever Front Pulldown 🔥 Jalón al pecho en máquina | Gimnasio",
    "tags": ["lever front pulldown", "jalón al pecho", "jalón frontal", "lat pulldown", "dorsales", "espalda",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Front Pulldown", "jalón al pecho en máquina de palanca",
        "dorsales y bíceps con las rodillas bajo la almohadilla",
        "¿Querés una espalda más ancha? El jalón frontal en máquina te aísla los dorsales. Mirá cómo se usa.",
        ["Ajustá el asiento para que las rodillas queden bajo la almohadilla.", "Elegí un peso que puedas bajar 10 veces sin mover el cuerpo."],
        ["Sentate erguido con el pecho alto y los hombros atrás.", "Agarrá las asas con agarre prono, un poco más abiertas que los hombros.",
         "Tirá de las asas hacia el pecho activando los dorsales.", "Apretá los omóplatos y soltá lento, sin apoyar las placas."],
        ["Jalar al cuello → las asas van al pecho.", "Columpiar el cuerpo → sin impulso, erguido.",
         "Soltar de golpe → soltá lento y sin apoyar las placas."],
        ["Asas al pecho.", "Pecho alto y hombros atrás.", "Omóplatos juntos abajo.",
         "Codos abajo, no abiertos.", "Soltá lento, sin que se apoye el peso."],
        "Dorsales · Bíceps · Romboides · Deltoides posterior",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #LeverFrontPulldown #JalonAlPecho #Dorsales #Espalda #Musculacion #Entrenamiento")})

# ═════════════ D15 · LEVER ONE ARM LATERAL WIDE PULLDOWN ═════════════
s, S, J = load("lever-one-arm-lateral-wide-pulldown"); pr = s["props"][0]
PINP = S(*PIN(pr["x"], pr["pin"])); CHEST = S(*pr["chest"])
WS, WP = S(*J["TOP"]["W"]), S(*J["PULL"]["W"])
TORSO = S(*J["TORSO_BAD"]["S"]); SHRS = S(*J["SHRUG_BAD"]["S"])
L = lambda: seqloop("PULL", "TOP", 1.0, 2.0)
F = [
    hook("GIMNASIO · ESPALDA", ["LATERAL", "PULLDOWN"], "Jalón a una mano",
         "Lever One Arm Lateral Wide Pulldown: el jalón a una mano con el pecho apoyado, para trabajar el dorsal.",
         [C("TOP"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Pecho en la almohadilla",
         "El pecho va apoyado en la almohadilla y el asa baja cruzando el cuerpo. Trabaja el dorsal de un lado.",
         [C("TOP")], [ring(CHEST, 44, 0.8), lab((985, 1120), "PECHO APOYADO", "end", 0.8),
                      ring(WS, 36, 1.8), lab((985, 1000), "ASA ARRIBA", "end", 1.8),
                      ring(PINP, 30, 2.6), lab((60, 1440), "PASADOR", "start", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Pecho en la almohadilla",
         "Ajustá el asiento para que el pecho quede apoyado en la almohadilla y los pies planos en el suelo.",
         [C("TOP")], [ring(CHEST, 44, 0.8), lab((985, 1120), "PECHO APOYADO", "end", 1.0)], 7.0),
    step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
         "Elegí el peso con el pasador: uno que puedas bajar diez veces con un solo brazo.",
         [C("TOP")], [ring(PINP, 30, 0.8), lab((60, 1440), "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["BRAZO", "LARGO"], "Codo casi recto",
         "Apoyá el pecho y sujetá el asa con un brazo. Extendé el brazo por completo, con una leve flexión en el codo.",
         [C("TOP")], [lab((60, 1120), "BRAZO LARGO", "start", 1.0), ring(WS, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["TIRÁ", "CRUZANDO"], "Hacia la cadera opuesta",
         "Paso uno. Tirá del asa hacia abajo y cruzando el cuerpo, en dirección a la cadera opuesta.",
         [C("TOP"), TO("MID", 0.6, 1.0), TO("PULL", 1.6, 1.0)],
         [arrow((WS[0] + 40, WS[1] - 24), (WP[0], WP[1] - 24), 0.8, 1.1), lab((985, 1240), "CRUZANDO", "end", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["APRETÁ", "EL DORSAL"], "Pausa abajo",
         "Paso dos. Apretá el dorsal en la parte baja del movimiento y hacé una pausa breve.",
         [C("PULL")], [ring(WP, 44, 0.8), lab((60, 1260), "APRETÁ EL DORSAL", "start", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin que se apoye",
         "Paso tres. Devolvé el asa despacio y extendé el brazo por completo, sin apoyar las placas. Después cambiá de lado.",
         [C("PULL"), TO("TOP", 0.6, 2.2)], [ring(PINP, 34, 1.8), lab((60, 1440), "SIN APOYAR", "start", 1.8)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al tirar",
         "Soltá el aire mientras tirás y tomalo mientras volvés. No aguantes el aire.",
         [C("TOP"), seqloop("PULL", "TOP", 1.0, 2.2, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["PECHO", "SEPARADO"], "Pecho en la almohadilla",
         "Error: separar el pecho de la almohadilla para tirar. El pecho queda apoyado todo el movimiento.",
         [C("TOP"), TO("TORSO_BAD", 0.5, 0.9)], [NO(), ring(TORSO, 50, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["ENCOGER", "EL HOMBRO"], "Hombro abajo",
         "Error: encoger el hombro hacia la oreja. Mantené el hombro abajo y tirá con el dorsal.",
         [C("TOP"), TO("SHRUG_BAD", 0.5, 0.9)], [NO(1.0), ring(SHRS, 44, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Pecho apoyado", "Brazo largo", "Hombro abajo", "Soltá sin apoyar"],
         "Tips de profe: pecho apoyado, brazo largo, hombro abajo y soltá sin apoyar las placas.",
         [C("TOP"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Pecho apoyado", "Tirá cruzando", "Hombro abajo", "Volvé lento"],
         "Claves: pecho apoyado, tirá cruzando el cuerpo, hombro abajo y volvé lento.",
         [{"cut": "PULL", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce por lado, con un minuto y medio de pausa. Cuando salgan fáciles, subí una placa.",
         ["1 · TIRÁ CRUZANDO", "2 · APRETÁ", "3 · VOLVÉ LENTO"], [C("TOP"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, devolvé el asa despacio y dejá el peso apoyado. Cambiá de lado y repetí.",
         [C("TOP"), TO("MID", 1.0, 1.0), TO("TOP", 2.2, 1.2)], [lab((60, 1440), "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-one-arm-lateral-wide-pulldown", F, {"pose": "PULL", "grip": 1, "zoom": 1.12, "dy": 130}, {
    "titulo": "Lever One Arm Lateral Wide Pulldown 🔥 Jalón a una mano | Gimnasio",
    "tags": ["lever one arm lateral wide pulldown", "jalón a una mano", "jalón lateral", "dorsal", "dorsales", "espalda",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever One Arm Lateral Wide Pulldown", "jalón a una mano con el pecho apoyado",
        "dorsal de un lado, con el pecho apoyado",
        "¿Querés trabajar el dorsal de a un lado? Este jalón a una mano con el pecho apoyado es para vos. Mirá cómo se usa.",
        ["Ajustá el asiento para que el pecho quede apoyado en la almohadilla.", "Elegí un peso que puedas bajar 10 veces con un solo brazo."],
        ["Apoyá el pecho y sujetá el asa con un brazo.", "Extendé el brazo por completo, con una leve flexión en el codo.",
         "Tirá del asa hacia abajo y cruzando el cuerpo, hacia la cadera opuesta.", "Apretá el dorsal y volvé lento, sin apoyar las placas."],
        ["Separar el pecho de la almohadilla → pecho apoyado todo el movimiento.", "Encoger el hombro → hombro abajo, tirá con el dorsal.",
         "Soltar de golpe → volvé lento, sin que se apoye el peso."],
        ["Pecho apoyado en la almohadilla.", "Brazo largo, codo casi recto.", "Tirá cruzando hacia la cadera opuesta.",
         "Hombro abajo, no encogido.", "Volvé lento y cambiá de lado."],
        "Dorsales · Bíceps · Romboides · Deltoides posterior",
        "3 series de 10–12 repeticiones por lado, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #LeverOneArmPulldown #JalonUnaMano #Dorsales #Espalda #Musculacion #Entrenamiento")})
