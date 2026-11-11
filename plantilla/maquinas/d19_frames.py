# Dataset D37 Lever Donkey Calf Raise y D38 Lever Rotary Calf: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.5, tb=2.0, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def dk_scenes(slug):
    s, S, J = load(slug)
    PAD = S(J["MID"]["H"][0] - 30, J["MID"]["H"][1] - 34); STEP = S(62, -52)
    PIN = S(-509, -133)
    A_DN = S(*J["DOWN"]["A"]); A_UP = S(*J["UP"]["A"])
    KNEES = S(*J["KNEES_BAD"]["K"]); ROUND = S((J["ROUND_BAD"]["S"][0] + J["ROUND_BAD"]["H"][0]) / 2,
                                               (J["ROUND_BAD"]["S"][1] + J["ROUND_BAD"]["H"][1]) / 2)
    A_SHORT = S(*J["SHORT_BAD"]["A"])
    ARX = round(A_DN[0] + 46)
    return [
        hook("GIMNASIO · PIERNAS", ["DONKEY", "CALF"], "Gemelos inclinado en máquina",
             "Lever Donkey Calf Raise: gemelos inclinado en máquina de palanca. Punta de los pies en el escalón y subí los talones.",
             [C("MID"), seqloop("UP", "DOWN")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Almohadilla, escalón y pila",
             "La máquina tiene una almohadilla para la cadera, un escalón para la punta de los pies y la pila con el pasador.",
             [C("MID")], [ring(PAD, 52, 0.8), lab((60, 1140), "ALMOHADILLA", "start", 0.8),
                          ring(STEP, 56, 1.8), lab((985, 1420), "ESCALÓN", "end", 1.8),
                          ring(PIN, 26, 2.8), lab((60, 1430), "PESO", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["LA", "ALMOHADILLA"], "A la altura de la cadera",
             "Ajustá la almohadilla para que apoye en la cadera cuando te inclinás. Si queda alta, no trabaja.",
             [C("MID")], [ring(PAD, 52, 0.8), lab((60, 1140), "EN LA CADERA", "start", 1.0)], 7.2),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí el peso con el pasador: uno que te deje subir quince veces sin rebotar.",
             [C("MID")], [ring(PIN, 26, 0.8), lab((60, 1430), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["INCLINADO", "Y FIRME"], "Talones en el aire",
             "Inclinate con la espalda apoyada en la almohadilla, las rodillas casi rectas y los talones en el aire.",
             [C("MID")], [ring(A_DN, 44, 1.6), lab((985, 1390), "TALÓN AFUERA", "end", 1.6)], 7.0),
        step("PASO 1 / 3", ["BAJÁ EL", "TALÓN"], "Despacio, hasta estirar",
             "Paso uno. Bajá el talón despacio por debajo del escalón hasta estirar bien la pantorrilla.",
             [C("MID"), TO("DOWN", 0.6, 1.8)],
             [ring(A_DN, 44, 1.6), arrow((ARX, A_UP[1] - 42), (ARX, A_DN[1] - 16), 0.9, 1.2)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "ABAJO"], "Uno o dos segundos",
             "Paso dos. Abajo, pausá uno o dos segundos. Nada de rebotar como un resorte.",
             [C("DOWN")], [ring(A_DN, 44, 0.8), lab((985, 1400), "PAUSA", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["SUBÍ", "BIEN ALTO"], "Sobre el dedo gordo",
             "Paso tres. Subí lo más alto posible sobre el dedo gordo y apretá arriba un segundo.",
             [C("DOWN"), TO("UP", 0.6, 1.4)],
             [ring(A_UP, 44, 1.6), arrow((ARX, A_DN[1] + 4), (ARX, A_UP[1] - 20), 0.9, 1.4)], 6.8, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
             "Soltá el aire mientras subís y tomalo mientras bajás. Ritmo lento.",
             [C("MID"), seqloop("UP", "DOWN", 1.6, 2.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["RODILLAS", "FLEXIONADAS"], "No te ayudes con las piernas",
             "Error: flexionar las rodillas para ayudarte a subir. Rodillas casi rectas y quietas: solo se mueve el tobillo.",
             [C("MID"), TO("KNEES_BAD", 0.5, 0.9)], [NO(pos=(860, 880)), ring(KNEES, 46, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["ESPALDA", "REDONDA"], "Pecho abierto",
             "Error: redondear la espalda y esconder el pecho. Abrí el pecho y mantené la espalda firme bajo la almohadilla.",
             [C("MID"), TO("ROUND_BAD", 0.5, 1.0)], [NO(pos=(860, 880)), ring(ROUND, 56, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["RECORRIDO", "CORTO"], "Bajá y subí todo",
             "Error: hacer medio recorrido. Bajá el talón hasta estirar y subí hasta lo más alto.",
             [C("MID"), TO("SHORT_BAD", 0.5, 1.0)], [NO(pos=(860, 880)), ring(A_SHORT, 44, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Rodillas casi rectas", "Pausa abajo estirando",
                                          "Subí sobre el dedo gordo", "Espalda firme, pecho abierto"],
             "Tips: rodillas casi rectas, pausa abajo estirando, subí sobre el dedo gordo y espalda firme con el pecho abierto.",
             [C("MID"), seqloop("UP", "DOWN")]),
        keys("CLAVES", ["TÉCNICA"], ["Punta en el borde", "Pies paralelos",
                                     "Rango completo", "Apretá arriba"],
             "Claves: punta en el borde, pies paralelos, rango completo y apretá arriba.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15"], "Un minuto de pausa",
             "Tres series de doce a quince, con un minuto de pausa. Cuando las quince salen fáciles, subí el peso.",
             ["1 · BAJÁ EL TALÓN", "2 · PAUSA ABAJO", "3 · SUBÍ ALTO"],
             [C("DOWN"), seqloop("UP", "DOWN")]),
        step("AL TERMINAR", ["BAJÁ EL", "PESO"], "Sin soltar de golpe",
             "Al terminar, bajá el peso despacio y recién después salí de la máquina.",
             [C("UP"), TO("DOWN", 0.8, 2.2)], [lab((60, 1010), "DEJÁ EL PESO", "start", 1.0)], 6.5),
    ]


def rc_scenes(slug):
    s, S, J = load(slug)
    PAD = S(J["MID"]["K"][0] - 50, J["MID"]["K"][1] - 52); STEP = S(80, -44)
    PIN = S(-609, -133); SEAT = S(-200, -300)
    A_DN = S(*J["DOWN"]["A"]); A_UP = S(*J["UP"]["A"])
    BACK = S((J["PUSH_BAD"]["S"][0] + J["PUSH_BAD"]["H"][0]) / 2,
             (J["PUSH_BAD"]["S"][1] + J["PUSH_BAD"]["H"][1]) / 2)
    A_SHORT = S(*J["SHORT_BAD"]["A"])
    ARX = round(A_DN[0] + 48)
    return [
        hook("GIMNASIO · PIERNAS", ["ROTARY", "CALF"], "Gemelos en máquina rotatoria",
             "Lever Rotary Calf: gemelos sentado en máquina rotatoria. Empujá la punta del pie y subí los talones.",
             [C("MID"), seqloop("UP", "DOWN")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Placa, almohadilla y pila",
             "La máquina tiene una placa para la punta de los pies, una almohadilla sobre los muslos y la pila con el pasador.",
             [C("MID")], [ring(PAD, 52, 0.8), lab((985, 1180), "ALMOHADILLA", "end", 0.8),
                          ring(STEP, 56, 1.8), lab((985, 1400), "PLACA", "end", 1.8),
                          ring(PIN, 26, 2.8), lab((60, 1380), "PESO", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Rodillas algo flexionadas",
             "Ajustá el asiento para que las rodillas queden algo flexionadas y los pies apoyados en la placa.",
             [C("MID")], [ring(SEAT, 44, 0.8), lab((985, 1240), "ASIENTO", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí el peso con el pasador. Si el talón no baja del todo, es mucho peso.",
             [C("MID")], [ring(PIN, 26, 0.8), lab((60, 1380), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["SENTADO", "DERECHO"], "Punta en la placa",
             "Sentado derecho, con la punta de los pies en la placa, los talones fuera del borde y las manos en las asas.",
             [C("MID")], [ring(STEP, 56, 1.6), lab((985, 1400), "TALONES AFUERA", "end", 1.6)], 7.0),
        step("PASO 1 / 3", ["BAJÁ EL", "TALÓN"], "Despacio",
             "Paso uno. Bajá el talón despacio por debajo de la placa hasta estirar la pantorrilla.",
             [C("MID"), TO("DOWN", 0.6, 1.8)],
             [ring(A_DN, 44, 1.6), arrow((ARX, A_UP[1] - 44), (ARX, A_DN[1] - 16), 0.9, 1.2)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "ABAJO"], "Sin rebote",
             "Paso dos. Abajo, pausá estirando la pantorrilla. Nada de rebotar.",
             [C("DOWN")], [ring(A_DN, 44, 0.8), lab((985, 1420), "PAUSA", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["EMPUJÁ", "Y APRETÁ"], "Bien arriba",
             "Paso tres. Empujá con la parte delantera del pie, subí bien alto y apretá un segundo.",
             [C("DOWN"), TO("UP", 0.6, 1.4)],
             [ring(A_UP, 44, 1.6), arrow((ARX, A_DN[1] + 4), (ARX, A_UP[1] - 22), 0.9, 1.4)], 6.8, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
             "Soltá el aire mientras empujás con el pie y tomalo mientras bajás los talones.",
             [C("MID"), seqloop("UP", "DOWN", 1.5, 2.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", ["EMPUJAR CON", "EL CUERPO"], "Las manos no empujan",
             "Error: empujar con las manos o tirar el tronco adelante. Si pasa, el peso es mucho: bajalo.",
             [C("MID"), TO("PUSH_BAD", 0.5, 1.0)], [NO(), ring(BACK, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["RECORRIDO", "CORTO"], "Bajá y subí todo",
             "Error: rebotar abajo y hacer medio recorrido. Bajá todo, pausá y subí todo.",
             [C("MID"), TO("SHORT_BAD", 0.5, 1.0)], [NO(), ring(A_SHORT, 44, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Rodillas algo flexionadas", "Talón bien abajo",
                                          "Pausa sin rebote", "Empujá con la punta"],
             "Tips: rodillas algo flexionadas, talón bien abajo, pausa sin rebote y empujá con la punta del pie.",
             [C("MID"), seqloop("UP", "DOWN")]),
        keys("CLAVES", ["TÉCNICA"], ["Punta en la placa", "Talones afuera",
                                     "Rango completo", "Apretá arriba"],
             "Claves: punta en la placa, talones afuera, rango completo y apretá arriba.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15"], "Un minuto de pausa",
             "Tres series de quince, con un minuto de pausa. Cuando las quince salen fáciles, subí el peso.",
             ["1 · BAJÁ EL TALÓN", "2 · PAUSA ABAJO", "3 · SUBÍ Y APRETÁ"],
             [C("DOWN"), seqloop("UP", "DOWN")]),
        step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
             "Al terminar, acompañá la placa y dejá el peso apoyado antes de sacar los pies.",
             [C("UP"), TO("DOWN", 0.8, 2.2)], [lab((60, 1010), "DEJÁ EL PESO", "start", 1.0)], 6.5),
    ]


YT37 = {
    "titulo": "Lever Donkey Calf Raise 🔥 Gemelos inclinado en máquina | Gimnasio",
    "tags": ["lever donkey calf raise", "donkey calf raise", "gemelos inclinado", "máquina de gemelos",
             "calf raise", "gemelos", "pantorrilla", "sóleo", "piernas", "máquina de palanca",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Lever Donkey Calf Raise", "gemelos inclinado en máquina de palanca",
        "gemelos y sóleo, con el tobillo como único motor",
        "¿Subís los talones ayudándote con las rodillas? Así el gemelo casi no trabaja. Mirá cómo se hace bien.",
        ["Ajustá la almohadilla para que apoye en la cadera cuando te inclinás.",
         "Apoyá solo la punta de los pies en el escalón, con los talones en el aire.",
         "Elegí un peso que te deje subir quince veces sin rebotar."],
        ["Inclinate con la espalda apoyada en la almohadilla y las rodillas casi rectas.",
         "Bajá el talón despacio por debajo del escalón hasta estirar.",
         "Pausá uno o dos segundos abajo, sin rebotar.",
         "Subí lo más alto posible sobre el dedo gordo y apretá un segundo."],
        ["Flexionar las rodillas para ayudarte → rodillas casi rectas y quietas.",
         "Redondear la espalda → pecho abierto y espalda firme.",
         "Hacer medio recorrido → bajá hasta estirar y subí hasta lo más alto."],
        ["Rodillas casi rectas, sin trabarlas.", "Pausa abajo estirando la pantorrilla.",
         "Subí sobre el dedo gordo, no con el pie plano.", "Espalda firme y pecho abierto bajo la almohadilla.",
         "Pies paralelos en el escalón."],
        "Gemelos · Sóleo",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Pantorrilla #DonkeyCalfRaise #Piernas #Musculacion #Entrenamiento")}

YT38 = {
    "titulo": "Lever Rotary Calf 🔥 Gemelos sentado en máquina rotatoria | Gimnasio",
    "tags": ["lever rotary calf", "rotary calf", "gemelos rotatorio", "gemelos sentado",
             "máquina de gemelos", "gemelos", "pantorrilla", "sóleo", "piernas", "máquina de palanca",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Lever Rotary Calf", "gemelos sentado en máquina rotatoria",
        "sóleo y gemelos, con la punta del pie como único motor",
        "¿Bajás apenas el talón y rebotás? Ese es el atajo que deja los gemelos iguales. Mirá cómo se hace bien.",
        ["Ajustá el asiento para que las rodillas queden algo flexionadas y los pies apoyados en la placa.",
         "Apoyá la punta de los pies en la placa, con los talones fuera del borde.",
         "Elegí el peso con el pasador: si el talón no baja del todo, es mucho peso."],
        ["Sentado derecho, con las manos en las asas para estabilizarte.",
         "Bajá el talón despacio hasta estirar la pantorrilla.",
         "Pausá abajo, sin rebotar.",
         "Empujá con la parte delantera del pie, subí bien alto y apretá un segundo."],
        ["Empujar con las manos o tirar el tronco adelante → si pasa, el peso es mucho.",
         "Rebotar abajo y hacer medio recorrido → bajá todo, pausá y subí todo."],
        ["Rodillas algo flexionadas, sin moverlas.", "Talón bien abajo, pantorrilla estirada.",
         "Pausa abajo sin rebote.", "Empujá con la punta del pie, no con la rodilla.",
         "Las manos solo estabilizan."],
        "Sóleo · Gemelos",
        "3 series de 15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Pantorrilla #RotaryCalf #Piernas #Musculacion #Entrenamiento")}

save("lever-donkey-calf-raise", dk_scenes("lever-donkey-calf-raise"),
     {"pose": "UP", "zoom": 1.06, "dy": 150}, YT37)

save("lever-rotary-calf", rc_scenes("lever-rotary-calf"),
     {"pose": "UP", "zoom": 1.05, "dy": 110}, YT38)
