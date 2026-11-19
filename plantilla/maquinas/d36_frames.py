# Dataset D60 Lever Gripless Shrug v.2: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def sh2_scenes(slug):
    s, S, J = load(slug)
    PAD = S(-60, -742); GRIP = S(190, -735); STACK = S(450, -250)
    SH = S(0, -752); LEAN = S(-30, -690); RND = S(70, -735)
    return [
        hook("GIMNASIO · ESPALDA", ["ENCOGIMIENTO", "MANOS ALTAS"], "Trapecios en palanca",
             "Variante dos del encogimiento sin agarre: las manos van altas, cerca del cuello, y las almohadillas empujan los hombros.",
             [C("START"), seqloop("START", "SHRUG")]),
        step("LA MÁQUINA", ["DOS", "ALMOHADILLAS"], "Agarre alto",
             "Esta versión tiene dos almohadillas que apoyan sobre los hombros y las manijas altas, cerca del cuello, para no perder el pecho.",
             [C("START")], [ring(PAD, 46, 0.8), lab((60, PAD[1] - 60), "ALMOHADILLAS", "start", 0.8),
                            ring(GRIP, 40, 1.7), lab((60, 900), "MANIJAS ALTAS", "start", 1.7),
                            ring(STACK, 42, 2.6), lab((60, 1150), "PILA", "start", 2.6)], 7.2),
        step("AJUSTE 1", ["ALTURA DE", "ALMOHADILLAS"], "Sobre los hombros",
             "Ajustá las almohadillas para que apoyen sobre los dos hombros, sin presionar el cuello ni dejar aire.",
             [C("START")], [ring(PAD, 46, 0.8), lab((60, PAD[1] + 50), "SOBRE LOS HOMBROS", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["MANOS", "ALTAS"], "Cerca del cuello",
             "Las manos van en las manijas altas, cerca del cuello, con los codos abajo y los pies al ancho de cadera.",
             [C("START")], [ring(GRIP, 40, 0.8), lab((60, 1010), "MANOS ARRIBA", "start", 1.0),
                            ring(S(76, -30), 40, 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["PECHO", "ARRIBA"], "Hombros abajo",
             "Arrancá con los hombros abajo, el pecho arriba y la mirada al frente. El agarre alto te ayuda a no encorvarte.",
             [C("START")], [ring(SH, 50, 0.8), lab((60, SH[1]), "HOMBROS ABAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "ARRIBA"], "Con los trapecios",
             "Paso uno. Empujá las almohadillas hacia arriba con los hombros, como si quisieras tocar las orejas con los trapecios.",
             [C("START"), TO("SHRUG", 0.6, 1.0)],
             [arrow((PAD[0], PAD[1] + 40), (PAD[0], PAD[1] - 70), 0.8, 1.0, [-40, 0]),
              lab((60, PAD[1] - 80), "HOMBROS ARRIBA", "start", 1.0)], 7.0),
        step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso dos. Sostené un segundo arriba con los codos quietos y el pecho alto, sin soltar el aire de golpe.",
             [C("SHRUG"), TO("SHRUG", 0.2, 0.4)], [ring(S(-60, -770), 50, 0.8)], 6.8),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Sin soltar",
             "Paso tres. Bajá lento hasta sentir el estiramiento de los trapecios, sin dejar que los hombros se vayan adelante.",
             [C("SHRUG"), TO("START", 0.5, 1.2)],
             [arrow((PAD[0], PAD[1] - 70), (PAD[0], PAD[1] + 40), 0.8, 1.0, [-40, 0]),
              lab((60, PAD[1] - 70), "BAJÁ LENTO", "start", 1.1)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al bajar",
             "Soltá el aire cuando encogés y tomá aire cuando bajás. El abdomen queda firme y las costillas abajo.",
             [C("START"), seqloop("START", "SHRUG", 0.9, 1.7, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ECHARSE", "ATRÁS"], "El tronco quieto",
             "Error: echarse atrás para empujar las almohadillas. El tronco queda vertical y los hombros hacen el recorrido.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(LEAN, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Encogé completo",
             "Error: encoger apenas unos centímetros. Subí las almohadillas hasta el tope y hacé la pausa completa.",
             [C("START"), TO("HALF_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(S(0, -766), 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda y bajar el pecho. El pecho se queda arriba y la espalda recta durante todo el recorrido.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(RND, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Manijas altas", "Codos abajo",
                                         "Pausa arriba", "Bajá lento"],
             "Tips: manijas altas cerca del cuello, codos abajo, pausa arriba y bajada lenta.",
             [C("START"), seqloop("START", "SHRUG")]),
        keys("CLAVES", ["TÉCNICA"], ["Empujá con los hombros", "Pecho arriba",
                                     "No tirés con los brazos", "Mirada al frente"],
             "Claves: empujá con los hombros, pecho arriba, no tirés con los brazos y mirada al frente.",
             [{"cut": "SHRUG", "at": 0.1}]),
        reps(["3 X 12–15"], "Trapecios",
             "Tres series de doce a quince repeticiones, con un minuto de pausa. Elegí un peso que te deje completar el recorrido.",
             ["1 · EMPUJÁ", "2 · PAUSA", "3 · BAJÁ"], [C("START"), seqloop("START", "SHRUG")]),
        step("AL TERMINAR", ["SOLTÁ Y", "BAJÁ"], "Sin apurarse",
             "Al terminar la serie, bajá las almohadillas despacio, soltá las manijas y salí de la máquina sin encorvarte.",
             [C("SHRUG"), TO("START", 0.9, 2.0)], [lab((60, 1000), "SIN SOLTAR", "start", 1.0)], 6.5),
    ]


YT60 = {
    "titulo": "Lever Gripless Shrug V2 🔥 Encogimiento de hombros sin agarre (manos altas) | Gimnasio",
    "tags": ["lever gripless shrug v2", "encogimiento de hombros", "shrug en máquina", "trapecios",
             "manijas altas", "encogimiento sin agarre", "espalda alta", "máquina de palanca",
             "gimnasio", "principiantes", "rutina de espalda", "trapecio superior"],
    "descripcion": yt_desc("Lever Gripless Shrug v. 2",
        "encogimiento de hombros en máquina de palanca con almohadillas en los hombros y manijas altas",
        "trapecios y espalda alta",
        "La variante dos sube el agarre a la altura del cuello, así el pecho se mantiene arriba y los hombros hacen todo el recorrido. Es la misma idea que la versión uno, pero con las manos más altas y dos almohadillas de apoyo. Si te echás atrás, hacés media repetición o redondeás la espalda, el peso se reparte y los trapecios trabajan menos.",
        ["Ajustá las almohadillas para que apoyen sobre los dos hombros, sin presionar el cuello.",
         "Poné las manos en las manijas altas, cerca del cuello, y elegí un peso para 12–15 repeticiones."],
        ["Parate con los pies al ancho de cadera y las manos en las manijas altas.",
         "Con los hombros abajo y el pecho arriba, empujá las almohadillas hacia arriba con los trapecios.",
         "Sostené un segundo arriba, con los codos quietos.",
         "Bajá lento hasta sentir el estiramiento.",
         "Completá la serie y salí de la máquina despacio."],
        ["Echarse atrás → el tronco queda vertical y los hombros hacen el recorrido.",
         "Media repetición → subí hasta el tope y hacé la pausa completa.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Manijas altas cerca del cuello.", "Los codos quedan abajo y quietos.",
         "Pausa de un segundo arriba.", "Bajada lenta, sin soltar el peso."],
        "Espalda → Trapecios → Espalda alta",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Trapecios #EspaldaAlta #EncogimientoDeHombros #MaquinaDePalanca #Shrug #Entrenamiento #Fuerza")}

save("lever-gripless-shrug-v-2", sh2_scenes("lever-gripless-shrug-v-2"),
     {"pose": "SHRUG", "zoom": 1.06, "dy": 40}, YT60)
