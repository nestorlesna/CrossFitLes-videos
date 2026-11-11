# Dataset D01 · D9 Lever Decline Chest Press y D10 Lever Incline Chest Press: escenas + YouTube + miniatura.
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
LT, RT = (60, 1100), (1010, 1120)   # labels: izquierda (arriba de la pila) / derecha (arriba del hombro)


# ═════════════ D9 · LEVER DECLINE CHEST PRESS ═════════════
s, S, J = load("lever-decline-chest-press"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); SEAT = S(pr["back"][0] - 10, pr["seat"][2] + 61)
WS, WO = S(*J["START"]["W"]), S(*J["OUT"]["W"])
EB, EO = S(*J["START"]["E"]), S(*J["OUT"]["E"])
BACKTOP = S(pr["back"][0] + math.sin(rad(pr["back"][1])) * pr["back"][2], pr["seat"][2] + 6 - math.cos(rad(pr["back"][1])) * pr["back"][2])
BADSH = S(*J["TORSO_BAD"]["S"]); LOCKE = S(*J["LOCK_BAD"]["E"])
L = lambda: seqloop("OUT", "START", 1.0, 2.0)
F = [
    hook("GIMNASIO · PECHO", ["DECLINE", "PRESS"], "Pecho inferior en máquina",
         "Lever Decline Chest Press: el press declinado en máquina, para el pecho inferior, con la espalda bien apoyada.",
         [C("START"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Respaldo reclinado",
         "El respaldo va reclinado y las manijas salen a la altura del pecho bajo. Trabaja el pecho y suma tríceps.",
         [C("START")], [ring(SEAT, 44, 0.8), lab(LT, "RESPALDO RECLINADO", "start", 0.8),
                        ring(WS, 36, 1.6), lab(RT, "MANIJAS BAJAS", "end", 1.6),
                        ring(PINP, 30, 2.6), lab((60, 1290), "PASADOR", "start", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Pecho bajo a la altura",
         "Ajustá el asiento para que las manijas queden a la altura del pecho bajo, sin forzar el hombro.",
         [C("START")], [ring(SEAT, 40, 0.8), ring(WS, 36, 1.6), lab(RT, "ALTURA DEL PECHO", "end", 1.4)], 7.0),
    step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
         "Elegí el peso con el pasador: uno que puedas empujar diez veces sin despegar la espalda del respaldo.",
         [C("START")], [ring(PINP, 30, 0.8), lab((60, 1290), "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["ESPALDA", "APOYADA"], "Pies planos",
         "Sentate con la espalda pegada al respaldo y los pies planos. Agarrá las manijas y sacá pecho.",
         [C("START")], [lab(LT, "PIES PLANOS", "start", 1.0), ring(WS, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["EMPUJÁ", "ADELANTE"], "Sin despegar la espalda",
         "Paso uno. Empujá las manijas hacia adelante y un poco abajo, sin despegar la espalda del respaldo.",
         [C("START"), TO("MID", 0.6, 1.0), TO("OUT", 1.6, 1.0)],
         [arrow((WS[0] + 40, WS[1] - 30), (WO[0], WO[1] - 30), 0.8, 1.1), lab(RT, "HACIA ADELANTE", "end", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["SIN", "TRABAR"], "Brazos casi estirados",
         "Paso dos. Llegá hasta casi estirar los brazos, sin trabar los codos de golpe.",
         [C("OUT")], [ring(EO, 36, 0.8), lab(RT, "CODOS SIN TRABAR", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Hasta sentir el pecho",
         "Paso tres. Volvé lento hasta sentir que estira el pecho, sin dejar que las placas se apoyen.",
         [C("OUT"), TO("START", 0.6, 2.2)], [ring(PINP, 34, 1.8), lab((60, 1290), "SIN APOYAR", "start", 1.8)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
         "Soltá el aire mientras empujás y tomalo mientras volvés. No aguantes el aire.",
         [C("START"), seqloop("OUT", "START", 1.0, 2.2, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["DESPEGAR", "LA ESPALDA"], "Quedate apoyado",
         "Error: despegar la espalda del respaldo para empujar. El pecho queda alto y la espalda pegada.",
         [C("START"), TO("TORSO_BAD", 0.5, 0.9)], [NO(), ring(BADSH, 56, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["TRABAR", "LOS CODOS"], "Casi estirado, nunca trabado",
         "Error: trabar los codos de golpe al final. Llegá casi estirado y empez\u00e1 a volver.",
         [C("START"), TO("LOCK_BAD", 0.5, 0.7)], [NO(1.0), ring(LOCKE, 36, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Manijas al pecho bajo", "Espalda pegada", "Codos a 45°", "Volvé sin apoyar"],
         "Tips de profe: manijas al pecho bajo, espalda pegada, codos a cuarenta y cinco grados y volvé sin apoyar las placas.",
         [C("START"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Espalda pegada", "Pecho alto", "Sin trabar los codos", "Volvé lento"],
         "Claves: espalda pegada, pecho alto, sin trabar los codos y volvé lento.",
         [{"cut": "OUT", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce, con un minuto y medio de pausa. Cuando las doce salgan fáciles, subí una placa.",
         ["1 · EMPUJÁ", "2 · SIN TRABAR", "3 · VOLVÉ LENTO"], [C("START"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, volvé despacio, soltá las manijas y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("START"), TO("MID", 1.0, 1.0), TO("START", 2.2, 1.2)], [lab((60, 1290), "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-decline-chest-press", F, {"pose": "OUT", "grip": 0, "zoom": 1.1, "dy": 110}, {
    "titulo": "Lever Decline Chest Press 🔥 Press declinado en máquina | Pecho inferior",
    "tags": ["lever decline chest press", "press declinado en máquina", "pecho inferior", "pectorales", "tríceps",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de pecho"],
    "descripcion": yt_desc("Lever Decline Chest Press", "press declinado en máquina de palanca",
        "pecho inferior fuerte y seguro",
        "¿Querés trabajar la parte baja del pecho sin cargar el hombro? El press declinado en máquina es para vos. Mirá cómo se usa.",
        ["Ajustá el asiento para que las manijas queden a la altura del pecho bajo.", "Elegí un peso que puedas empujar 10 veces sin despegar la espalda."],
        ["Sentate con la espalda pegada al respaldo y los pies planos.", "Empujá las manijas hacia adelante y un poco abajo.",
         "Llegá hasta casi estirar, sin trabar los codos.", "Volvé lento hasta sentir que estira el pecho, sin apoyar las placas."],
        ["Despegar la espalda → pecho alto y espalda pegada.", "Trabar los codos → casi estirado, nunca trabado.",
         "Asiento mal regulado → manijas a la altura del pecho bajo."],
        ["Manijas a la altura del pecho bajo.", "Espalda pegada y pecho alto.", "Codos a unos 45° del cuerpo.",
         "Empujá sin trabar codos.", "Volvé hasta sentir estirar el pecho."],
        "Pectorales · Tríceps · Hombros anteriores",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #LeverDeclineChestPress #Pecho #Pectorales #Musculacion #Entrenamiento")})

# ═════════════ D10 · LEVER INCLINE CHEST PRESS ═════════════
s, S, J = load("lever-incline-chest-press"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); SEAT = S(pr["back"][0] - 10, pr["seat"][2] + 61)
WS, WO = S(*J["START"]["W"]), S(*J["OUT"]["W"])
EO = S(*J["OUT"]["E"]); ARCHSH = S(*J["ARCH_BAD"]["S"]); LOCKE = S(*J["LOCK_BAD"]["E"])
L = lambda: seqloop("OUT", "START", 1.0, 2.0)
F = [
    hook("GIMNASIO · PECHO", ["INCLINE", "PRESS"], "Pecho superior en máquina",
         "Lever Incline Chest Press: el press inclinado en máquina, para el pecho superior, con la espalda bien apoyada.",
         [C("START"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Manijas a la altura de la clavícula",
         "El respaldo va casi vertical y las manijas salen altas, a la altura de la clavícula. Trabaja el pecho y el hombro.",
         [C("START")], [ring(SEAT, 44, 0.8), lab(LT, "RESPALDO ALTO", "start", 0.8),
                        ring(WS, 36, 1.6), lab(RT, "MANIJAS ALTAS", "end", 1.6),
                        ring(PINP, 30, 2.6), lab((60, 1290), "PASADOR", "start", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Manijas a la clavícula",
         "Ajustá el asiento para que las manijas queden a la altura de la clavícula, no a la altura del cuello.",
         [C("START")], [ring(SEAT, 40, 0.8), ring(WS, 36, 1.6), lab(RT, "ALTURA DE LA CLAVÍCULA", "end", 1.4)], 7.0),
    step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
         "Elegí el peso con el pasador: uno que puedas empujar diez veces sin despegar la espalda del respaldo.",
         [C("START")], [ring(PINP, 30, 0.8), lab((60, 1290), "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["ESPALDA", "APOYADA"], "Pecho alto",
         "Sentate con la espalda pegada al respaldo, los pies planos y el pecho alto. Agarrá las manijas.",
         [C("START")], [lab(LT, "PIES PLANOS", "start", 1.0), ring(WS, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["EMPUJÁ", "ARRIBA"], "Siguiendo la inclinación",
         "Paso uno. Empujá las manijas hacia adelante y arriba, siguiendo la inclinación de la máquina.",
         [C("START"), TO("MID", 0.6, 1.0), TO("OUT", 1.6, 1.0)],
         [arrow((WS[0] + 40, WS[1] - 30), (WO[0], WO[1] - 30), 0.8, 1.1), lab(RT, "HACIA ARRIBA", "end", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["SIN", "TRABAR"], "Brazos casi estirados",
         "Paso dos. Llegá hasta casi estirar los brazos, sin trabar los codos de golpe.",
         [C("OUT")], [ring(EO, 36, 0.8), lab(RT, "CODOS SIN TRABAR", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Hasta sentir el pecho",
         "Paso tres. Volvé lento hasta sentir que estira el pecho, sin dejar que las placas se apoyen.",
         [C("OUT"), TO("START", 0.6, 2.2)], [ring(PINP, 34, 1.8), lab((60, 1290), "SIN APOYAR", "start", 1.8)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
         "Soltá el aire mientras empujás y tomalo mientras volvés. No aguantes el aire.",
         [C("START"), seqloop("OUT", "START", 1.0, 2.2, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["ARQUEAR", "LA ESPALDA"], "Costillas abajo",
         "Error: arquear la espalda para empujar más. Las costillas quedan abajo y la espalda pegada al respaldo.",
         [C("START"), TO("ARCH_BAD", 0.5, 0.9)], [NO(), ring(ARCHSH, 56, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["TRABAR", "LOS CODOS"], "Casi estirado, nunca trabado",
         "Error: trabar los codos de golpe al final. Llegá casi estirado y empezá a volver.",
         [C("START"), TO("LOCK_BAD", 0.5, 0.7)], [NO(1.0), ring(LOCKE, 36, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Manijas a la clavícula", "Espalda pegada", "Empujá hacia arriba", "Volvé sin apoyar"],
         "Tips de profe: manijas a la clavícula, espalda pegada, empujá hacia arriba y volvé sin apoyar las placas.",
         [C("START"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Espalda pegada", "Pecho alto", "Empujá hacia arriba", "Volvé lento"],
         "Claves: espalda pegada, pecho alto, empujá hacia arriba y volvé lento.",
         [{"cut": "OUT", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce, con un minuto y medio de pausa. Cuando las doce salgan fáciles, subí una placa.",
         ["1 · EMPUJÁ ARRIBA", "2 · SIN TRABAR", "3 · VOLVÉ LENTO"], [C("START"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, volvé despacio, soltá las manijas y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("START"), TO("MID", 1.0, 1.0), TO("START", 2.2, 1.2)], [lab((60, 1290), "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-incline-chest-press", F, {"pose": "OUT", "grip": 0, "zoom": 1.05, "dy": 120}, {
    "titulo": "Lever Incline Chest Press 🔥 Press inclinado en máquina | Pecho superior",
    "tags": ["lever incline chest press", "press inclinado en máquina", "pecho superior", "pectorales", "hombros",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de pecho"],
    "descripcion": yt_desc("Lever Incline Chest Press", "press inclinado en máquina de palanca",
        "pecho superior y hombro fuerte",
        "¿Querés llenar la parte de arriba del pecho? El press inclinado en máquina apunta justo ahí. Mirá cómo se usa.",
        ["Ajustá el asiento para que las manijas queden a la altura de la clavícula.", "Elegí un peso que puedas empujar 10 veces sin despegar la espalda."],
        ["Sentate con la espalda pegada y los pies planos.", "Agarrá las manijas a la altura de la clavícula.",
         "Empujá hacia adelante y arriba, sin trabar los codos.", "Volvé lento hasta sentir que estira el pecho, sin apoyar las placas."],
        ["Arquear la espalda → costillas abajo y espalda pegada.", "Trabar los codos → casi estirado, nunca trabado.",
         "Manijas a la altura del cuello → subí o bajá el asiento."],
        ["Manijas a la altura de la clavícula.", "Espalda pegada y pecho alto.", "Empujá hacia adelante y arriba.",
         "Casi estirado, nunca trabado.", "Volvé hasta sentir estirar el pecho."],
        "Pectorales superiores · Hombros · Tríceps",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #LeverInclineChestPress #Pecho #PechoSuperior #Musculacion #Entrenamiento")})
