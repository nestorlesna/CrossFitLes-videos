# Dataset D01 · D16 Lever Reverse Grip Lateral Pulldown y D17 Reverse Grip Machine Lat Pulldown: escenas + YouTube + miniatura.
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


# ═════════════ D16 · LEVER REVERSE GRIP LATERAL PULLDOWN ═════════════
s, S, J = load("lever-reverse-grip-lateral-pulldown"); pr = s["props"][0]
PINP = S(*PIN(pr["x"], pr["pin"])); ROLL = S(*pr["pad"])
WS, WP = S(*J["TOP"]["W"]), S(*J["PULL"]["W"])
SH = S(*J["PULL"]["S"]); NECKW = S(*J["NECK_BAD"]["W"]); LEANS = S(*J["LEAN_BAD"]["S"])
L = lambda: seqloop("PULL", "TOP", 1.0, 2.0)
F = [
    hook("GIMNASIO · ESPALDA", ["LATERAL", "PULLDOWN"], "Jalón lateral en máquina",
         "Lever Reverse Grip Lateral Pulldown: el jalón lateral en máquina de palanca, con agarre prono y los codos guiando.",
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
    step("POSICIÓN INICIAL", ["AGARRE", "PRONO"], "Más abierto que los hombros",
         "Sentate erguido con el pecho alto y los hombros atrás. Agarrá las asas con agarre prono, un poco más abiertas que los hombros.",
         [C("TOP")], [lab((60, 1120), "AGARRE PRONO", "start", 1.0), ring(WS, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["BAJÁ", "GUIANDO"], "Con los codos",
         "Paso uno. Tirá de las asas hacia el pecho guiando con los codos, no con las manos.",
         [C("TOP"), TO("MID", 0.6, 1.0), TO("PULL", 1.6, 1.0)],
         [arrow((WS[0] + 40, WS[1] - 24), (WP[0], WP[1] - 24), 0.8, 1.1), lab((985, 1240), "CON LOS CODOS", "end", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["JUNTÁ LOS", "OMÓPLATOS"], "Pausa abajo",
         "Paso dos. Juntá los omóplatos y hacé una pausa breve abajo, con las asas en el pecho.",
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
    keys("TIPS DEL PROFE", ["TIPS"], ["Asas al pecho", "Codos guían", "Omóplatos juntos", "Soltá sin apoyar"],
         "Tips de profe: asas al pecho, codos que guían, omóplatos juntos y soltá sin apoyar las placas.",
         [C("TOP"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Pecho alto", "Codos abajo", "Sin impulso", "Soltá lento"],
         "Claves: pecho alto, codos abajo, sin impulso y soltá lento.",
         [{"cut": "PULL", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce, con un minuto y medio de pausa. Cuando las doce salgan fáciles, subí una placa.",
         ["1 · BAJÁ GUIANDO", "2 · APRETÁ", "3 · SOLTÁ LENTO"], [C("TOP"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, soltá las asas despacio y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("TOP"), TO("MID", 1.0, 1.0), TO("TOP", 2.2, 1.2)], [lab((60, 1440), "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-reverse-grip-lateral-pulldown", F, {"pose": "PULL", "grip": 1, "zoom": 1.12, "dy": 130}, {
    "titulo": "Lever Reverse Grip Lateral Pulldown 🔥 Jalón lateral en máquina | Gimnasio",
    "tags": ["lever reverse grip lateral pulldown", "jalón lateral", "jalón al pecho", "dorsales", "espalda",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Reverse Grip Lateral Pulldown", "jalón lateral en máquina de palanca",
        "dorsales y bíceps guiando con los codos",
        "¿Querés una espalda más ancha? El jalón lateral en máquina te aísla los dorsales. Mirá cómo se usa.",
        ["Ajustá el asiento para que las rodillas queden bajo la almohadilla.", "Elegí un peso que puedas bajar 10 veces sin mover el cuerpo."],
        ["Sentate erguido con el pecho alto y los hombros atrás.", "Agarrá las asas con agarre prono, un poco más abiertas que los hombros.",
         "Tirá de las asas hacia el pecho guiando con los codos.", "Juntá los omóplatos y soltá lento, sin apoyar las placas."],
        ["Jalar al cuello → las asas van al pecho.", "Columpiar el cuerpo → sin impulso, erguido.",
         "Soltar de golpe → soltá lento y sin apoyar las placas."],
        ["Asas al pecho.", "Los codos guían el movimiento.", "Omóplatos juntos abajo.",
         "Pecho alto y hombros atrás.", "Soltá lento, sin que se apoye el peso."],
        "Dorsales · Bíceps · Romboides · Deltoides posterior",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #LeverReverseGripLateralPulldown #JalonLateral #Dorsales #Espalda #Musculacion #Entrenamiento")})

# ═════════════ D17 · REVERSE GRIP MACHINE LAT PULLDOWN ═════════════
s, S, J = load("reverse-grip-machine-lat-pulldown"); pr = s["props"][0]
PINP = S(*PIN(pr["x"], pr["pin"])); ROLL = S(*pr["pad"])
WS, WP = S(*J["TOP"]["W"]), S(*J["PULL"]["W"])
SH = S(*J["PULL"]["S"]); NECKW = S(*J["NECK_BAD"]["W"]); LEANS = S(*J["LEAN_BAD"]["S"])
L = lambda: seqloop("PULL", "TOP", 1.0, 2.0)
F = [
    hook("GIMNASIO · ESPALDA", ["SUPINO", "PULLDOWN"], "Jalón supino en máquina",
         "Reverse Grip Machine Lat Pulldown: el jalón al pecho con agarre supino, con las rodillas bajo la almohadilla.",
         [C("TOP"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Rodillas bajo la almohadilla",
         "Las asas bajan al pecho y las rodillas quedan bajo la almohadilla. Con agarre supino trabaja dorsales y bíceps.",
         [C("TOP")], [ring(WS, 36, 0.8), lab((985, 1010), "ASAS ARRIBA", "end", 0.8),
                      ring(ROLL, 40, 1.8), lab((60, 1330), "RODILLAS", "start", 1.8),
                      ring(PINP, 30, 2.6), lab((60, 1440), "PASADOR", "start", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Rodillas bajo la almohadilla",
         "Ajustá el asiento para que las rodillas queden justo bajo la almohadilla y los pies planos en el suelo.",
         [C("TOP")], [ring(ROLL, 40, 0.8), lab((60, 1330), "RODILLAS", "start", 1.0)], 7.0),
    step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
         "Elegí el peso con el pasador: uno que puedas bajar diez veces sin mover el cuerpo.",
         [C("TOP")], [ring(PINP, 30, 0.8), lab((60, 1440), "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["AGARRE", "SUPINO"], "Palmas hacia vos",
         "Sentate erguido con el pecho alto y los hombros atrás. Agarrá las asas con agarre supino, un poco más abiertas que los hombros.",
         [C("TOP")], [lab((60, 1120), "AGARRE SUPINO", "start", 1.0), ring(WS, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["LLEVÁ", "AL PECHO"], "Asas al esternón",
         "Paso uno. Tirá de las asas hacia el pecho, llevándolas al esternón, sin mover el torso.",
         [C("TOP"), TO("MID", 0.6, 1.0), TO("PULL", 1.6, 1.0)],
         [arrow((WS[0] + 40, WS[1] - 24), (WP[0], WP[1] - 24), 0.8, 1.1), lab((985, 1240), "AL ESTERNÓN", "end", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["JUNTÁ LAS", "ESCÁPULAS"], "Pausa abajo",
         "Paso dos. Juntá las escápulas y hacé una pausa breve abajo, con las asas en el pecho.",
         [C("PULL")], [ring(SH, 44, 0.8), lab((60, 1100), "ESCÁPULAS JUNTAS", "start", 1.0)], numeral="2"),
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
    keys("TIPS DEL PROFE", ["TIPS"], ["Agarre supino", "Asas al pecho", "Escápulas juntas", "Soltá sin apoyar"],
         "Tips de profe: agarre supino, asas al pecho, escápulas juntas y soltá sin apoyar las placas.",
         [C("TOP"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Agarre supino", "Pecho alto", "Sin impulso", "Soltá lento"],
         "Claves: agarre supino, pecho alto, sin impulso y soltá lento.",
         [{"cut": "PULL", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce, con un minuto y medio de pausa. Cuando las doce salgan fáciles, subí una placa.",
         ["1 · LLEVÁ AL PECHO", "2 · APRETÁ", "3 · SOLTÁ LENTO"], [C("TOP"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, soltá las asas despacio y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("TOP"), TO("MID", 1.0, 1.0), TO("TOP", 2.2, 1.2)], [lab((60, 1440), "PESO APOYADO", "start", 1.0)], 6.5),
]
save("reverse-grip-machine-lat-pulldown", F, {"pose": "PULL", "grip": 1, "zoom": 1.12, "dy": 130}, {
    "titulo": "Reverse Grip Machine Lat Pulldown 🔥 Jalón supino en máquina | Gimnasio",
    "tags": ["reverse grip machine lat pulldown", "jalón supino", "jalón al pecho", "agarre supino", "dorsales", "espalda",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Reverse Grip Machine Lat Pulldown", "jalón supino en máquina",
        "dorsales y bíceps con agarre supino",
        "¿Querés sentir más el dorsal? El jalón con agarre supino lo trabaja desde otro ángulo. Mirá cómo se usa.",
        ["Ajustá el asiento para que las rodillas queden bajo la almohadilla.", "Elegí un peso que puedas bajar 10 veces sin mover el cuerpo."],
        ["Sentate erguido con el pecho alto y los hombros atrás.", "Agarrá las asas con agarre supino, un poco más abiertas que la altura de los hombros.",
         "Tirá de las asas al pecho, llevándolas al esternón.", "Juntá las escápulas y soltá lento, sin apoyar las placas."],
        ["Jalar al cuello → las asas van al pecho.", "Columpiar el cuerpo → sin impulso, erguido.",
         "Soltar de golpe → soltá lento y sin apoyar las placas."],
        ["Agarre supino, palmas hacia vos.", "Asas al pecho, al esternón.", "Escápulas juntas abajo.",
         "Pecho alto y hombros atrás.", "Soltá lento, sin que se apoye el peso."],
        "Dorsales · Bíceps · Romboides · Deltoides posterior",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #ReverseGripMachineLatPulldown #JalonSupino #Dorsales #Espalda #Musculacion #Entrenamiento")})
