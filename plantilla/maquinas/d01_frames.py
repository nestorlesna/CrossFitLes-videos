# Dataset D01 · D1 Lever Seated Crunch (Chest Pad) y D2 Lever Seated Leg Raise Crunch: escenas + YouTube + miniatura.
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
LB, LT = (130, 880), (1000, 900)


# ═════════════ D1 · LEVER SEATED CRUNCH (CHEST PAD) ═════════════
s, S, J = load("lever-seated-crunch-chest-pad"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); SEAT = S(pr["seat"][0] + 110, pr["seat"][2])
PADP = S(J["UP"]["S"][0] + 30, J["UP"]["S"][1] + 30); FEET = S(pr["feet"][0] + 58, pr["feet"][1] - 54)
L = lambda: seqloop("DEEP", "UP", 1.2, 2.2)
F = [
    hook("GIMNASIO · CORE", ["LEVER SEATED", "CRUNCH"], "Crunch con almohadilla al pecho",
         "Lever Seated Crunch: el crunch abdominal en máquina de palanca, con la almohadilla apoyada al pecho.",
         [C("UP"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Palanca con pila de peso",
         "La almohadilla va contra el pecho y la palanca mueve la pila. Trabaja el recto abdominal y suma los oblicuos.",
         [C("UP")], [ring(PADP, 50, 0.8), lab(LT, "ALMOHADILLA", "end", 0.8),
                     ring(SEAT, 44, 1.8), lab(LB, "ASIENTO", "start", 1.8),
                     ring(PINP, 30, 2.8), lab((130, 1250), "PASADOR", "start", 2.8)], 7.0),
    step("AJUSTE 1", ["ALTURA", "DEL ASIENTO"], "Pecho y cadera cómodos",
         "Ajustá el asiento y la altura de la almohadilla para que quede cómoda contra el pecho, sin apretar el cuello.",
         [C("UP")], [ring(SEAT, 44, 0.8), ring(PADP, 50, 1.8), lab(LT, "ALMOHADILLA AL PECHO", "end", 1.4)], 7.0),
    step("AJUSTE 2", ["PESO", "MODERADO"], "Con el pasador",
         "Elegí un peso moderado con el pasador. Si necesitás impulso para moverlo, es demasiado.",
         [C("UP")], [ring(PINP, 30, 0.8), lab(LB, "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["PECHO", "APOYADO"], "Pies firmes",
         "Sentate con el pecho contra la almohadilla, la espalda apoyada y los pies firmes en el piso. Tomá las manijas.",
         [C("UP")], [lab(LT, "PECHO BIEN APOYADO", "end", 1.0), ring(FEET, 36, 1.8)], 7.0),
    step("PASO 1 / 3", ["RECLINATE", "LENTO"], "El abdomen frena",
         "Paso uno. Activá el abdomen y reclinate despacio hacia atrás, dejando que la almohadilla te acompañe.",
         [C("UP"), TO("DEEP", 0.6, 1.6)], [lab(LT, "LLEVÁ EL TORSO ATRÁS", "end", 1.0)], numeral="1"),
    step("PASO 2 / 3", ["APRETÁ", "ARRIBA"], "Un segundo",
         "Paso dos. En la máxima contracción, apretá el abdomen un segundo y soltá todo el aire.",
         [C("DEEP")], [ring(S(*J["DEEP"]["H"]), 64, 0.8), lab(LT, "APRETÁ UN SEGUNDO", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin tocar la pila",
         "Paso tres. Volvé a la posición inicial contrayendo el abdomen, sin que las placas toquen la pila.",
         [C("DEEP"), TO("UP", 0.6, 2.4)], [ring(PINP, 34, 1.8), lab(LB, "SIN TOCAR LA PILA", "start", 1.8)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver, soltalo al ir",
         "Tomá aire mientras volvés y soltalo mientras te reclinás. Nunca aguantes el aire arriba.",
         [C("UP"), seqloop("DEEP", "UP", 1.2, 2.4, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 3", ["TIRAR CON", "LOS BRAZOS"], "El abdomen hace el trabajo",
         "Error: tirar con los brazos y usar mucho peso. Los brazos solo sostienen: el que mueve es el abdomen.",
         [C("UP"), TO("ARMS_BAD", 0.5, 0.9)], [NO(), ring(S(*J["ARMS_BAD"]["W"]), 44, 1.4)], 7.2),
    step("ASÍ NO · 2 / 3", ["TIRAR DEL", "CUELLO"], "Cuello largo",
         "Error: empujar con el cuello y la cabeza. El cuello sufre y el abdomen no trabaja: cuello largo y mirada al frente.",
         [C("UP"), TO("NECK_BAD", 0.5, 0.9)], [NO(), ring(S(*J["NECK_BAD"]["N"]), 50, 1.4)], 7.2),
    step("ASÍ NO · 3 / 3", ["SOLTAR", "DE GOLPE"], "Bajada controlada",
         "Error: dejar caer el peso de golpe y rebotar. Volvé en dos o tres segundos, sin que la pila choque.",
         [C("UP"), {"seq": [["SWING_BAD", 0.3], ["UP", 0.3]], "at": 0.5, "until": 4.0}, TO("SWING_BAD", 4.1, 0.4)],
         [NO(1.0), lab(LT, "SIN CONTROL", "end", 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Almohadilla cómoda al pecho", "Los brazos solo sostienen", "Exhalá al reclinar",
                                     "Volvé sin tocar la pila"],
         "Tips de profe: almohadilla cómoda al pecho, los brazos solo sostienen, exhalá al reclinar y volvé sin tocar la pila.",
         [C("UP"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Pecho contra la almohadilla", "Pies firmes", "Cuello largo", "Movimiento lento"],
         "Claves: pecho contra la almohadilla, pies firmes, cuello largo y movimiento lento.",
         [{"cut": "DEEP", "at": 0.1}]),
    reps(["3 X 12-15"], "Un minuto de pausa",
         "Tres series de doce a quince, con un minuto de pausa. Cuando las quince salen fáciles, subí una placa.",
         ["1 · RECLINATE", "2 · APRETÁ", "3 · VOLVÉ LENTO"], [C("UP"), L()]),
    step("AL TERMINAR", ["DEJALA", "LISTA"], "Peso descargado",
         "Al terminar, volvé despacio, soltá las manijas y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("UP"), TO("DEEP", 1.0, 1.2), TO("UP", 2.4, 1.4)], [lab(LB, "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-seated-crunch-chest-pad", F, {"pose": "DEEP", "grip": 0, "zoom": 1.15, "dy": 110}, {
    "titulo": "Lever Seated Crunch (Chest Pad) 🔥 Crunch abdominal en máquina de palanca | Gimnasio",
    "tags": ["lever seated crunch", "crunch con almohadilla", "crunch en máquina de palanca", "abdominales en máquina",
             "crunch abdominal", "abdomen", "core", "recto abdominal", "oblicuos", "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Lever Seated Crunch (Chest Pad)", "crunch abdominal con almohadilla al pecho",
        "abdominales con carga sin tirar del cuello",
        "¿Terminás las abdominales con dolor de cuello o tirando con los brazos? En esta máquina se evita, si ajustás bien. Este video es para vos.",
        ["Ajustá el asiento y la altura de la almohadilla, cómoda contra el pecho.", "Elegí un peso moderado con el pasador."],
        ["Sentate con el pecho contra la almohadilla y los pies firmes en el piso.", "Activá el abdomen y reclinate lento hacia atrás.",
         "Apretá un segundo en la máxima contracción y soltá el aire.", "Volvé lento, sin que las placas toquen la pila."],
        ["Tirar con los brazos → los brazos solo sostienen.", "Empujar con el cuello → cuello largo, mirada al frente.",
         "Dejar caer el peso de golpe → bajada controlada de dos o tres segundos."],
        ["Pensá en acercar las costillas a la cadera.", "Los brazos solo sostienen: no tires.", "Exhalá todo el aire al reclinar.",
         "Volvé lento sin que el peso toque la pila.", "Peso moderado: si necesitás impulso, es mucho."],
        "Recto abdominal · Oblicuos",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #LeverSeatedCrunch #Core #Musculacion #Entrenamiento")})

# ═════════════ D2 · LEVER SEATED LEG RAISE CRUNCH ═════════════
s, S, J = load("lever-seated-leg-raise-crunch"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); SEAT = S(pr["seat"][0] + 110, pr["seat"][2])
BACK = S(pr["seat"][0] + 12, pr["seat"][2] - 130)
KD = J["DOWN"]["K"]; AD = J["DOWN"]["A"]; ROLL = S(KD[0] + (AD[0] - KD[0]) * 0.32, KD[1] + (AD[1] - KD[1]) * 0.32)
KL = S(*J["LIFT"]["K"]); WDOWN = S(*J["DOWN"]["W"])
L = lambda: seqloop("DOWN", "LIFT", 1.0, 1.4)
F = [
    hook("GIMNASIO · CORE", ["LEVER SEATED", "LEG RAISE CRUNCH"], "Elevación de piernas con crunch",
         "Lever Seated Leg Raise Crunch: subí las rodillas al pecho en la máquina de palanca y enrollá el torso arriba.",
         [C("DOWN"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Palanca con rodillo",
         "El rodillo empuja la palanca desde las piernas. Trabaja el abdomen y los flexores de cadera.",
         [C("DOWN")], [ring(BACK, 48, 0.8), lab(LT, "RESPALDO", "end", 0.8),
                       ring(ROLL, 40, 1.8), lab(LB, "RODILLO", "start", 1.8),
                       ring(PINP, 30, 2.8), lab((130, 1250), "PASADOR", "start", 2.8)], 7.0),
    step("AJUSTE 1", ["ALTURA", "DEL ASIENTO"], "Espalda apoyada",
         "Ajustá el asiento para que la espalda quede apoyada en el respaldo y los pies lleguen cómodos al apoyo.",
         [C("DOWN")], [ring(SEAT, 44, 0.8), ring(BACK, 48, 1.6), lab(LT, "ESPALDA APOYADA", "end", 1.4)], 7.0),
    step("AJUSTE 2", ["PESO", "MODERADO"], "Con el pasador",
         "Elegí un peso moderado con el pasador. Si las piernas se sueltan de golpe, bajá la carga.",
         [C("DOWN")], [ring(PINP, 30, 0.8), lab(LB, "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["MANOS", "AL ASIENTO"], "Piernas abajo",
         "Sentate con la espalda apoyada y las manos en el asiento. Las piernas empiezan abajo, sin impulso.",
         [C("DOWN")], [ring(WDOWN, 44, 0.8), lab(LT, "MANOS EN EL ASIENTO", "end", 1.0)], 7.0),
    step("PASO 1 / 3", ["SUBÍ LAS", "RODILLAS"], "Al pecho",
         "Paso uno. Activá el abdomen y subí las rodillas hacia el pecho, sin balancear el cuerpo.",
         [C("DOWN"), TO("MID", 0.5, 0.9), TO("LIFT", 1.4, 1.0)],
         [ring(KL, 50, 1.6), lab(LT, "RODILLAS AL PECHO", "end", 1.4)], numeral="1"),
    step("PASO 2 / 3", ["ENROLLÁ", "ARRIBA"], "Costillas a la cadera",
         "Paso dos. Arriba, enrollá el torso acercando las costillas a la cadera y apretá un segundo.",
         [C("LIFT")], [ring(S(*J["LIFT"]["H"]), 64, 0.8), lab(LT, "ENROLLÁ EL TORSO", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Sin soltar",
         "Paso tres. Bajá las piernas y el torso lento, controlando el peso hasta abajo.",
         [C("LIFT"), TO("DOWN", 0.6, 2.4)], [ring(PINP, 34, 1.8), lab(LB, "SIN SOLTAR", "start", 1.8)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
         "Soltá el aire mientras subís las rodillas y tomá aire mientras bajás.",
         [C("DOWN"), seqloop("LIFT", "DOWN", 1.4, 1.8, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["BALANCEAR", "LAS PIERNAS"], "Sin impulso",
         "Error: usar impulso y balancear las piernas. Subí con el abdomen, sin hamacarte.",
         [C("DOWN"), {"seq": [["SWING_BAD", 0.3], ["DOWN", 0.3]], "at": 0.5, "until": 4.0}, TO("SWING_BAD", 4.1, 0.4)],
         [NO(1.0), lab(LT, "SIN CONTROL", "end", 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["SUBIR SIN", "ENROLLAR"], "El crunch es arriba",
         "Error: subir las piernas sin enrollar el torso. Arriba pensá en juntar las costillas con la cadera.",
         [C("DOWN"), TO("CURL_BAD", 0.5, 1.0)], [NO(), ring(S(*J["CURL_BAD"]["K"]), 50, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Espalda apoyada al respaldo", "Rodillas al pecho sin impulso",
                                     "Arriba, enrollá el torso", "Bajá lento, sin soltar"],
         "Tips de profe: espalda apoyada, rodillas al pecho sin impulso, enrollá el torso arriba y bajá lento sin soltar.",
         [C("DOWN"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Espalda apoyada", "Rodillas al pecho", "Enrollá arriba", "Bajada lenta"],
         "Claves: espalda apoyada, rodillas al pecho, enrollá arriba y bajada lenta.",
         [{"cut": "LIFT", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto de pausa",
         "Tres series de diez a doce, con un minuto de pausa. Sumá peso cuando las doce salgan sin impulso.",
         ["1 · SUBÍ", "2 · ENROLLÁ", "3 · BAJÁ LENTO"], [C("DOWN"), L()]),
    step("AL TERMINAR", ["DEJALA", "LISTA"], "Piernas abajo",
         "Al terminar, bajá las piernas despacio, soltá el rodillo y dejá el peso apoyado.",
         [C("DOWN"), TO("MID", 0.8, 0.9), TO("DOWN", 1.9, 1.0)], [lab(LB, "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-seated-leg-raise-crunch", F, {"pose": "LIFT", "grip": 0, "zoom": 1.15, "dy": 110}, {
    "titulo": "Lever Seated Leg Raise Crunch 🔥 Elevación de piernas con crunch en máquina | Gimnasio",
    "tags": ["lever seated leg raise crunch", "elevación de piernas en máquina", "crunch en máquina de palanca",
             "rodillas al pecho", "abdominales en máquina", "abdomen", "core", "flexores de cadera",
             "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Lever Seated Leg Raise Crunch", "elevación de piernas con crunch",
        "abdomen y flexores de cadera sin balancearte",
        "¿Subís las piernas con impulso y el abdomen no trabaja? Con este ajuste y este orden, la máquina te obliga a usar el core. Este video es para vos.",
        ["Ajustá el asiento para que la espalda quede apoyada en el respaldo.", "Elegí un peso moderado con el pasador."],
        ["Sentate con las manos en el asiento y las piernas abajo.", "Subí las rodillas al pecho sin balancear el cuerpo.",
         "Arriba, enrollá el torso y apretá un segundo.", "Bajá las piernas y el torso lento, sin soltar el peso."],
        ["Balancear las piernas → subí con el abdomen, sin impulso.", "Subir sin enrollar el torso → juntá costillas y cadera arriba.",
         "Soltar el peso de golpe → bajada lenta y controlada."],
        ["Espalda apoyada en el respaldo todo el tiempo.", "Las rodillas van al pecho, no los pies al techo.", "Arriba, pensá en enrollar el torso.",
         "Bajá lento, sin soltar la pila.", "Manos en el asiento: no tires con los brazos."],
        "Recto abdominal · Flexores de cadera",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #LeverSeatedLegRaiseCrunch #Core #Musculacion #Entrenamiento")})
