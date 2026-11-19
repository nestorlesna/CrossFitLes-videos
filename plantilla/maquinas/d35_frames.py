# Dataset D59 Lever Gripless Shrug: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def sh_scenes(slug):
    s, S, J = load(slug)
    PAD = S(-60, -763); GRIP = S(210, -700); STACK = S(450, -250)
    SH = S(0, -752); LOW = S(0, -766); LEAN = S(-30, -690); RND = S(70, -735)
    return [
        hook("GIMNASIO · ESPALDA", ["ENCOGIMIENTO", "SIN AGARRE"], "Trapecios en palanca",
             "Encogimiento de hombros en palanca: empujá la almohadilla con los trapecios, sin agarrar nada ni doblar los codos.",
             [C("START"), seqloop("START", "SHRUG")]),
        step("LA MÁQUINA", ["EL", "YUGO"], "Almohadilla y manijas",
             "La máquina tiene una almohadilla que apoya en los trapecios, manijas fijas al frente y una pila que sube por cable.",
             [C("START")], [ring(PAD, 46, 0.8), lab((60, PAD[1] - 60), "ALMOHADILLA", "start", 0.8),
                            ring(GRIP, 40, 1.7), lab((60, GRIP[1] - 10), "MANIJAS FIJAS", "start", 1.7),
                            ring(STACK, 42, 2.6), lab((60, 1150), "PILA", "start", 2.6)], 7.2),
        step("AJUSTE 1", ["ALTURA DEL", "YUGO"], "Sobre los trapecios",
             "Ajustá la altura para que la almohadilla apoye sobre los trapecios y las manijas queden a la altura del pecho.",
             [C("START")], [ring(PAD, 46, 0.8), lab((60, PAD[1] + 50), "SOBRE LOS TRAPECIOS", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["PIES Y", "MANOS"], "Sin agarrar fuerte",
             "Separá los pies al ancho de cadera y apoyá las manos en las manijas, sin apretar: el trabajo lo hacen los hombros.",
             [C("START")], [ring(S(70, -30), 40, 0.8),
                            ring(GRIP, 40, 1.8), lab((60, GRIP[1] + 60), "MANOS APOYADAS", "start", 1.8)], 7.0),
        step("POSICIÓN INICIAL", ["HOMBROS", "ABAJO"], "Pecho arriba",
             "Arrancá con los hombros abajo, el pecho arriba y los brazos apenas flexionados, sin colgar el peso de las manos.",
             [C("START")], [ring(SH, 50, 0.8), lab((60, SH[1]), "HOMBROS ABAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "ARRIBA"], "Con los trapecios",
             "Paso uno. Empujá la almohadilla hacia arriba con los trapecios, como si quisieras tocar las orejas con los hombros.",
             [C("START"), TO("SHRUG", 0.6, 1.0)],
             [arrow((PAD[0], PAD[1] + 40), (PAD[0], PAD[1] - 70), 0.8, 1.0, [-40, 0]),
              lab((60, PAD[1] - 80), "HOMBROS ARRIBA", "start", 1.0)], 7.0),
        step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso dos. Sostené un segundo arriba, con los codos quietos y la almohadilla bien alta.",
             [C("SHRUG"), TO("SHRUG", 0.2, 0.4)],
             [ring(S(-60, -787), 50, 0.8), lab((60, 900), "APRETÁ", "start", 1.0)], 6.8),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Sin soltar",
             "Paso tres. Bajá lento hasta sentir el estiramiento de los trapecios, sin soltar el peso de golpe.",
             [C("SHRUG"), TO("START", 0.5, 1.2)],
             [arrow((PAD[0], PAD[1] - 70), (PAD[0], PAD[1] + 40), 0.8, 1.0, [-40, 0]),
              lab((60, PAD[1] - 70), "BAJÁ LENTO", "start", 1.1)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al bajar",
             "Soltá el aire cuando encogés y tomá aire cuando bajás. El abdomen queda firme y las costillas abajo.",
             [C("START"), seqloop("START", "SHRUG", 0.9, 1.7, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ECHARSE", "ATRÁS"], "El tronco quieto",
             "Error: echarse atrás para empujar la almohadilla. El tronco queda vertical y los hombros hacen el recorrido.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(LEAN, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Encogé completo",
             "Error: encoger apenas unos centímetros. Subí la almohadilla hasta el tope y hacé la pausa completa.",
             [C("START"), TO("HALF_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(LOW, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda y bajar el pecho. El pecho se queda arriba y la espalda recta durante todo el recorrido.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(RND, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Almohadilla en los trapecios", "Codos quietos",
                                         "Pausa arriba", "Bajá lento"],
             "Tips: almohadilla sobre los trapecios, codos quietos, pausa arriba y bajada lenta.",
             [C("START"), seqloop("START", "SHRUG")]),
        keys("CLAVES", ["TÉCNICA"], ["Empujá con los hombros", "Sin agarrar fuerte",
                                     "Pecho arriba", "Mirada al frente"],
             "Claves: empujá con los hombros, sin agarrar fuerte las manijas, pecho arriba y mirada al frente.",
             [{"cut": "SHRUG", "at": 0.1}]),
        reps(["3 X 12–15"], "Trapecios",
             "Tres series de doce a quince repeticiones, con un minuto de pausa. Elegí un peso que te deje completar el recorrido.",
             ["1 · EMPUJÁ", "2 · PAUSA", "3 · BAJÁ"], [C("START"), seqloop("START", "SHRUG")]),
        step("AL TERMINAR", ["SOLTÁ Y", "BAJÁ"], "Sin apurarse",
             "Al terminar la serie, bajá la almohadilla despacio, soltá las manijas y salí de la máquina sin encorvarte.",
             [C("SHRUG"), TO("START", 0.9, 2.0)],
             [lab((60, 1000), "SIN SOLTAR", "start", 1.0)], 6.5),
    ]


YT59 = {
    "titulo": "Lever Gripless Shrug 🔥 Encogimiento de hombros sin agarre | Gimnasio",
    "tags": ["lever gripless shrug", "encogimiento de hombros", "shrug en máquina", "trapecios",
             "encogimiento sin agarre", "espalda alta", "máquina de palanca", "yugo para hombros",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Gripless Shrug",
        "encogimiento de hombros en máquina de palanca con yugo y manijas fijas",
        "trapecios y espalda alta",
        "El yugo deja empujar con los trapecios sin gastar fuerza en el agarre, así que el recorrido se siente completo. Si te echás atrás, hacés media repetición o redondeás la espalda, el peso se reparte y los trapecios trabajan menos. La clave es subir la almohadilla con los hombros, hacer la pausa y bajar lento.",
        ["Ajustá el yugo para que la almohadilla apoye sobre los trapecios y las manijas queden a la altura del pecho.",
         "Separá los pies al ancho de cadera y elegí un peso que te permita completar 12–15 repeticiones."],
        ["Parate bajo el yugo con la almohadilla sobre los trapecios y las manos apoyadas en las manijas.",
         "Con los hombros abajo y el pecho arriba, empujá la almohadilla hacia arriba con los trapecios.",
         "Sostené un segundo arriba, sin doblar los codos.",
         "Bajá lento hasta sentir el estiramiento.",
         "Completá la serie y salí de la máquina despacio."],
        ["Echarse atrás → el tronco queda vertical y los hombros hacen el recorrido.",
         "Media repetición → subí hasta el tope y hacé la pausa completa.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Almohadilla sobre los trapecios, no sobre el cuello.", "Los codos quedan quietos.",
         "Pausa de un segundo arriba.", "Bajada lenta, sin soltar el peso."],
        "Espalda → Trapecios → Espalda alta",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Trapecios #EspaldaAlta #EncogimientoDeHombros #MaquinaDePalanca #Shrug #Entrenamiento #Fuerza")}

save("lever-gripless-shrug", sh_scenes("lever-gripless-shrug"),
     {"pose": "SHRUG", "zoom": 1.06, "dy": 40}, YT59)
