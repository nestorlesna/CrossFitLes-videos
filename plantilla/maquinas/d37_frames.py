# Dataset D61 Lever Shrug: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def sh3_scenes(slug):
    s, S, J = load(slug)
    GRIP = S(70, -470); PLATE = S(170, -470); COL = S(300, -150); BAR = S(185, -470)
    SH = S(0, -752); LOW = S(0, -766); LEAN = S(-30, -690); RND = S(70, -735)
    return [
        hook("GIMNASIO · ESPALDA", ["ENCOGIMIENTO", "EN PALANCA"], "Trapecios en palanca",
             "Encogimiento de hombros en la palanca de barra al piso: agarrá los mangos y empujá con los trapecios sin doblar los codos.",
             [C("START"), seqloop("START", "SHRUG")]),
        step("LA MÁQUINA", ["BARRA", "Y DISCOS"], "Palanca al piso",
             "La palanca tiene una barra baja con discos grandes, un mango a cada lado y un pivote que gira apenas sobre la columna.",
             [C("START")], [ring(GRIP, 42, 0.8), lab((60, 1040), "MANGO", "start", 0.8),
                            ring(PLATE, 56, 1.6), lab((60, 1150), "DISCO", "start", 1.6),
                            ring(COL, 44, 2.5), lab((60, COL[1]), "COLUMNA", "start", 2.5)], 7.2),
        step("AJUSTE", ["BARRA A LA", "CADERA"], "Altura justa",
             "La barra queda a la altura de la cadera, con los brazos casi estirados y los pies al ancho de cadera.",
             [C("START")], [ring(BAR, 60, 0.8), lab((60, 1100), "A LA CADERA", "start", 1.0)], 7.0),
        step("AGARRE", ["MANOS", "FIRMES"], "Sin apretar de más",
             "Agarrá los mangos con las palmas hacia adentro y las muñecas rectas. El agarre solo sostiene: el trabajo lo hacen los hombros.",
             [C("START")], [ring(GRIP, 40, 0.8), lab((60, 1000), "AGARRE FIRME", "start", 1.0),
                            ring(S(70, -30), 40, 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["HOMBROS", "ABAJO"], "Pecho arriba",
             "Arrancá con los hombros abajo, el pecho arriba y la mirada al frente, sin colgar el peso de los brazos.",
             [C("START")], [ring(SH, 50, 0.8), lab((60, SH[1]), "HOMBROS ABAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "ARRIBA"], "Con los trapecios",
             "Paso uno. Encogé los hombros hacia las orejas, como si quisieras tocarlas, sin doblar los codos.",
             [C("START"), TO("SHRUG", 0.6, 1.0)],
             [arrow((SH[0] - 55, SH[1] + 40), (SH[0] - 55, SH[1] - 70), 0.8, 1.0, [-40, 0]),
              lab((60, 800), "HOMBROS ARRIBA", "start", 1.0)], 7.0),
        step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso dos. Sostené un segundo arriba con los codos quietos y la barra apenas levantada.",
             [C("SHRUG"), TO("SHRUG", 0.2, 0.4)], [ring(SH, 50, 0.8), lab((60, 900), "APRETÁ", "start", 1.0)], 6.8),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Sin soltar",
             "Paso tres. Bajá lento hasta sentir el estiramiento de los trapecios, sin dejar caer los hombros de golpe.",
             [C("SHRUG"), TO("START", 0.5, 1.2)],
             [arrow((SH[0] - 55, SH[1] - 70), (SH[0] - 55, SH[1] + 40), 0.8, 1.0, [-40, 0]),
              lab((60, 800), "BAJÁ LENTO", "start", 1.1)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al bajar",
             "Soltá el aire cuando encogés y tomá aire cuando bajás. El abdomen queda firme y las costillas abajo.",
             [C("START"), seqloop("START", "SHRUG", 0.9, 1.7, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ECHARSE", "ATRÁS"], "El tronco quieto",
             "Error: echarse atrás para empujar la barra. El tronco queda vertical y los hombros hacen el recorrido.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(LEAN, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Encogé completo",
             "Error: encoger apenas unos centímetros. Subí los hombros hasta el tope y hacé la pausa completa.",
             [C("START"), TO("HALF_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(LOW, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda y bajar el pecho. El pecho se queda arriba y la espalda recta durante todo el recorrido.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(RND, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Manos en los mangos", "Codos quietos",
                                         "Pausa arriba", "Bajá lento"],
             "Tips: manos en los mangos, codos quietos, pausa arriba y bajada lenta.",
             [C("START"), seqloop("START", "SHRUG")]),
        keys("CLAVES", ["TÉCNICA"], ["Empujá con los hombros", "Sin doblar los codos",
                                     "Pecho arriba", "Mirada al frente"],
             "Claves: empujá con los hombros, sin doblar los codos, pecho arriba y mirada al frente.",
             [{"cut": "SHRUG", "at": 0.1}]),
        reps(["3 X 12–15"], "Trapecios",
             "Tres series de doce a quince repeticiones, con un minuto de pausa. Elegí un peso que te deje completar el recorrido.",
             ["1 · EMPUJÁ", "2 · PAUSA", "3 · BAJÁ"], [C("START"), seqloop("START", "SHRUG")]),
        step("AL TERMINAR", ["SOLTÁ Y", "BAJÁ"], "Sin apurarse",
             "Al terminar la serie, bajá los hombros despacio, soltá los mangos y salí de la palanca sin encorvarte.",
             [C("SHRUG"), TO("START", 0.9, 2.0)],
             [lab((60, 1000), "SIN SOLTAR", "start", 1.0)], 6.5),
    ]


YT61 = {
    "titulo": "Lever Shrug 🔥 Encogimiento de hombros en palanca | Gimnasio",
    "tags": ["lever shrug", "encogimiento de hombros", "shrug en palanca", "trapecios",
             "encogimiento en máquina", "espalda alta", "máquina de palanca", "barra al piso",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Shrug",
        "encogimiento de hombros en la palanca de barra al piso con discos",
        "trapecios y espalda alta",
        "La palanca baja deja agarrar los mangos a la altura de la cadera y encoger los hombros con los brazos casi estirados. Como la barra no se levanta con las manos, el recorrido se siente en los trapecios. Si te echás atrás, hacés media repetición o redondeás la espalda, el peso se reparte y los trapecios trabajan menos.",
        ["Dejá la barra a la altura de la cadera y los pies al ancho de cadera.",
         "Agarrá los mangos con las palmas hacia adentro y elegí un peso para 12–15 repeticiones."],
        ["Parate frente a la palanca y agarrá los mangos con las palmas hacia adentro.",
         "Con los hombros abajo y el pecho arriba, encogé los hombros hacia las orejas sin doblar los codos.",
         "Sostené un segundo arriba, con los codos quietos.",
         "Bajá lento hasta sentir el estiramiento.",
         "Completá la serie y salí de la palanca despacio."],
        ["Echarse atrás → el tronco queda vertical y los hombros hacen el recorrido.",
         "Media repetición → subí hasta el tope y hacé la pausa completa.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Manos en los mangos, sin apretar de más.", "Los codos quedan quietos y apenas flexionados.",
         "Pausa de un segundo arriba.", "Bajada lenta, sin soltar la barra."],
        "Espalda → Trapecios → Espalda alta",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Trapecios #EspaldaAlta #EncogimientoDeHombros #MaquinaDePalanca #Shrug #Entrenamiento #Fuerza")}

save("lever-shrug", sh3_scenes("lever-shrug"),
     {"pose": "SHRUG", "zoom": 1.06, "dy": 40}, YT61)
