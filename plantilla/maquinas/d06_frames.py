# Dataset D01 · D12 Lever Standing Chest Press y D13 Machine Inner Chest Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.4, tb=1.2, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}
PIN = lambda cx, pin: (cx + 51, -254 + (pin - 0.5) * 22)


# ═════════════ D12 · LEVER STANDING CHEST PRESS ═════════════
s, S, J = load("lever-standing-chest-press"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"]))
WS, WO = S(*J["START"]["W"]), S(*J["OUT"]["W"])
EO = S(*J["OUT"]["E"]); LEANSH = S(*J["LEAN_BAD"]["S"]); LOCKE = S(*J["LOCK_BAD"]["E"])
FEET = S(*J["START"]["A"])
L = lambda: seqloop("OUT", "START", 1.0, 2.0)
F = [
    hook("GIMNASIO · PECHO", ["STANDING", "PRESS"], "Pecho de pie en máquina",
         "Lever Standing Chest Press: el press de pecho de pie en máquina de palanca, con los pies firmes.",
         [C("START"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Palanca a la altura del pecho",
         "La palanca sale de arriba y las manijas quedan a la altura del pecho. Trabaja pectorales, hombros y tríceps.",
         [C("START")], [ring(WS, 36, 0.8), lab((1010, 1040), "MANIJAS AL PECHO", "end", 0.8),
                        ring(PINP, 30, 1.8), lab((1010, 1400), "PASADOR", "end", 1.8),
                        ring(FEET, 36, 2.6), lab((1010, 1470), "PIES FIRMES", "end", 2.6)], 7.0),
    step("AJUSTE 1", ["ALTURA DE", "LAS MANIJAS"], "A la mitad del pecho",
         "Ajustá la máquina para que las manijas queden a la altura de la mitad del pecho, no del cuello.",
         [C("START")], [ring(WS, 36, 0.8), lab((1010, 1040), "MITAD DEL PECHO", "end", 1.4)], 7.0),
    step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
         "Elegí el peso con el pasador: uno que puedas empujar diez veces sin mover los pies.",
         [C("START")], [ring(PINP, 30, 0.8), lab((1010, 1400), "PASADOR", "end", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["PIES", "FIRMES"], "De pie, cuerpo derecho",
         "Parate frente a la máquina con los pies planos y separados. Agarrá las manijas y mantené el cuerpo derecho.",
         [C("START")], [lab((60, 1100), "CUERPO DERECHO", "start", 1.0), ring(FEET, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["EMPUJÁ", "ADELANTE"], "Sin mover los pies",
         "Paso uno. Empujá las manijas hacia adelante hasta estirar los brazos, sin mover los pies.",
         [C("START"), TO("MID", 0.6, 1.0), TO("OUT", 1.6, 1.0)],
         [arrow((WS[0] + 40, WS[1] - 24), (WO[0], WO[1] - 24), 0.8, 1.1), lab((1010, 1250), "HACIA ADELANTE", "end", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["SIN", "TRABAR"], "Codos casi estirados",
         "Paso dos. Llegá hasta casi estirar los codos, sin trabarlos de golpe.",
         [C("OUT")], [ring(EO, 36, 0.8), lab((1010, 1130), "CODOS SIN TRABAR", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Hasta el pecho",
         "Paso tres. Volvé lento hasta el pecho, sin dejar que las placas se apoyen.",
         [C("OUT"), TO("START", 0.6, 2.2)], [ring(PINP, 34, 1.8), lab((1010, 1400), "SIN APOYAR", "end", 1.8)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
         "Soltá el aire mientras empujás y tomalo mientras volvés. No aguantes el aire.",
         [C("START"), seqloop("OUT", "START", 1.0, 2.2, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["INCLINAR", "EL CUERPO"], "Cuerpo derecho",
         "Error: inclinar todo el cuerpo hacia adelante para empujar. Usá el pecho, no el peso del cuerpo.",
         [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(), ring(LEANSH, 56, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["TRABAR", "LOS CODOS"], "Casi estirado, nunca trabado",
         "Error: trabar los codos de golpe al final. Llegá casi estirado y empezá a volver.",
         [C("START"), TO("LOCK_BAD", 0.5, 0.7)], [NO(1.0), ring(LOCKE, 36, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Manijas al pecho", "Pies firmes", "Codos a 45°", "Volvé sin apoyar"],
         "Tips de profe: manijas a la mitad del pecho, pies firmes, codos a cuarenta y cinco grados y volvé sin apoyar.",
         [C("START"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Cuerpo derecho", "Pies firmes", "Sin trabar los codos", "Volvé lento"],
         "Claves: cuerpo derecho, pies firmes, sin trabar los codos y volvé lento.",
         [{"cut": "OUT", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce, con un minuto y medio de pausa. Cuando las doce salgan fáciles, subí una placa.",
         ["1 · EMPUJÁ", "2 · SIN TRABAR", "3 · VOLVÉ LENTO"], [C("START"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, volvé despacio, soltá las manijas y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("START"), TO("MID", 1.0, 1.0), TO("START", 2.2, 1.2)], [lab((1010, 1400), "PESO APOYADO", "end", 1.0)], 6.5),
]
save("lever-standing-chest-press", F, {"pose": "OUT", "grip": 0, "zoom": 1.12, "dy": 150}, {
    "titulo": "Lever Standing Chest Press 🔥 Press de pecho de pie | Gimnasio",
    "tags": ["lever standing chest press", "press de pecho de pie", "pecho de pie en máquina", "pectorales", "hombros",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de pecho"],
    "descripcion": yt_desc("Lever Standing Chest Press", "press de pecho de pie en máquina de palanca",
        "pecho y hombro sin sentarte",
        "¿La máquina de press de pecho está ocupada? Esta versión se hace de pie y trabaja igual. Mirá cómo se usa.",
        ["Ajustá la máquina para que las manijas queden a la mitad del pecho.", "Elegí un peso que puedas empujar 10 veces sin mover los pies."],
        ["Parate frente a la máquina con los pies planos y separados.", "Agarrá las manijas y mantené el cuerpo derecho.",
         "Empujá hacia adelante hasta casi estirar los brazos.", "Volvé lento hasta el pecho, sin apoyar las placas."],
        ["Inclinar todo el cuerpo → usá el pecho, no el peso del cuerpo.", "Trabar los codos → casi estirado, nunca trabado.",
         "Pies juntos o en puntas → pies planos y firmes."],
        ["Manijas a la mitad del pecho.", "Pies planos y firmes.", "Codos a unos 45° del cuerpo.",
         "Empujá sin trabar codos.", "Volvé sin apoyar las placas."],
        "Pectorales · Hombros anteriores · Tríceps",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #LeverStandingChestPress #Pecho #Pectorales #Musculacion #Entrenamiento")})

# ═════════════ D13 · MACHINE INNER CHEST PRESS ═════════════
s, S, J = load("machine-inner-chest-press"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); SEAT = S(pr["back"][0] - 10, pr["seat"][2] + 61)
WS, WO = S(*J["START"]["W"]), S(*J["OUT"]["W"])
EO = S(*J["OUT"]["E"]); BADE = S(*J["ELBOW_BAD"]["W"]); LOCKE = S(*J["LOCK_BAD"]["E"])
FEET = S(*J["START"]["A"])
L = lambda: seqloop("OUT", "START", 1.0, 2.0)
F = [
    hook("GIMNASIO · PECHO", ["INNER", "PRESS"], "Pecho interno en máquina",
         "Machine Inner Chest Press: el press de pecho interno en máquina, con los codos cerca del cuerpo.",
         [C("START"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Manijas al centro del pecho",
         "Las manijas salen al centro del pecho y los codos van cerca del cuerpo. Trabaja el pecho interno y los tríceps.",
         [C("START")], [ring(SEAT, 44, 0.8), lab((60, 1100), "RESPALDO", "start", 0.8),
                        ring(WS, 36, 1.6), lab((1010, 1120), "MANIJAS AL CENTRO", "end", 1.6),
                        ring(PINP, 30, 2.6), lab((60, 1290), "PASADOR", "start", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Manijas a la altura del pecho",
         "Ajustá el asiento para que las manijas queden a la altura del pecho, con los codos cómodos.",
         [C("START")], [ring(SEAT, 40, 0.8), ring(WS, 36, 1.6), lab((1010, 1120), "ALTURA DEL PECHO", "end", 1.4)], 7.0),
    step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
         "Elegí el peso con el pasador: uno que puedas empujar diez veces pegando bien los codos.",
         [C("START")], [ring(PINP, 30, 0.8), lab((60, 1290), "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["CODOS", "CERCA"], "Espalda pegada",
         "Sentate con la espalda pegada al respaldo y los codos cerca del cuerpo. Agarrá las manijas al centro del pecho.",
         [C("START")], [lab((60, 1180), "CODOS CERCA", "start", 1.0), ring(WS, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["EMPUJÁ", "JUNTANDO"], "Manijas al centro",
         "Paso uno. Empujá las manijas hacia adelante juntándolas al centro, con los codos cerca del cuerpo.",
         [C("START"), TO("MID", 0.6, 1.0), TO("OUT", 1.6, 1.0)],
         [arrow((WS[0] + 40, WS[1] - 24), (WO[0], WO[1] - 24), 0.8, 1.1), lab((1010, 1240), "AL CENTRO", "end", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["SIN", "TRABAR"], "Codos casi estirados",
         "Paso dos. Llegá hasta casi estirar los codos, sin trabarlos de golpe.",
         [C("OUT")], [ring(EO, 36, 0.8), lab((1010, 1130), "CODOS SIN TRABAR", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Hasta sentir el pecho",
         "Paso tres. Volvé lento hasta sentir que estira el pecho, sin dejar que las placas se apoyen.",
         [C("OUT"), TO("START", 0.6, 2.2)], [ring(PINP, 34, 1.8), lab((60, 1290), "SIN APOYAR", "start", 1.8)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
         "Soltá el aire mientras empujás y tomalo mientras volvés. No aguantes el aire.",
         [C("START"), seqloop("OUT", "START", 1.0, 2.2, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["CODOS", "MUY ABIERTOS"], "Manijas a la cara",
         "Error: abrir mucho los codos, con las manijas a la cara. Los codos van cerca del cuerpo.",
         [C("START"), TO("ELBOW_BAD", 0.5, 0.9)], [NO(), ring(BADE, 44, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["TRABAR", "LOS CODOS"], "Casi estirado, nunca trabado",
         "Error: trabar los codos de golpe al final. Llegá casi estirado y empezá a volver.",
         [C("START"), TO("LOCK_BAD", 0.5, 0.7)], [NO(1.0), ring(LOCKE, 36, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Manijas al centro", "Codos cerca", "Espalda pegada", "Volvé sin apoyar"],
         "Tips de profe: manijas al centro del pecho, codos cerca, espalda pegada y volvé sin apoyar las placas.",
         [C("START"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Espalda pegada", "Codos cerca", "Sin trabar los codos", "Volvé lento"],
         "Claves: espalda pegada, codos cerca, sin trabar los codos y volvé lento.",
         [{"cut": "OUT", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce, con un minuto y medio de pausa. Cuando las doce salgan fáciles, subí una placa.",
         ["1 · EMPUJÁ AL CENTRO", "2 · SIN TRABAR", "3 · VOLVÉ LENTO"], [C("START"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, volvé despacio, soltá las manijas y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("START"), TO("MID", 1.0, 1.0), TO("START", 2.2, 1.2)], [lab((60, 1290), "PESO APOYADO", "start", 1.0)], 6.5),
]
save("machine-inner-chest-press", F, {"pose": "OUT", "grip": 0, "zoom": 1.1, "dy": 110}, {
    "titulo": "Machine Inner Chest Press 🔥 Press de pecho interno | Gimnasio",
    "tags": ["machine inner chest press", "press de pecho interno", "pecho interno", "pectorales", "tríceps",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de pecho"],
    "descripcion": yt_desc("Machine Inner Chest Press", "press de pecho interno en máquina",
        "pecho interno y tríceps con los codos cerca",
        "¿Querés apuntar al centro del pecho? Este press con los codos cerca del cuerpo es para vos. Mirá cómo se usa.",
        ["Ajustá el asiento para que las manijas queden a la altura del pecho.", "Elegí un peso que puedas empujar 10 veces con los codos cerca."],
        ["Sentate con la espalda pegada y los codos cerca del cuerpo.", "Empujá las manijas hacia adelante juntándolas al centro.",
         "Llegá hasta casi estirar, sin trabar los codos.", "Volvé lento hasta sentir que estira el pecho, sin apoyar las placas."],
        ["Codos muy abiertos, manijas a la cara → codos cerca del cuerpo.", "Trabar los codos → casi estirado, nunca trabado.",
         "Despegar la espalda → espalda pegada y pecho alto."],
        ["Manijas al centro del pecho.", "Codos cerca del cuerpo, no abiertos.", "Espalda pegada al respaldo.",
         "Empujá sin trabar codos.", "Volvé hasta sentir estirar el pecho."],
        "Pectorales internos · Tríceps · Hombros anteriores",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #MachineInnerChestPress #Pecho #Pectorales #Musculacion #Entrenamiento")})
