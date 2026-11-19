# Dataset D62 Hack Calf Raise: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def hc_scenes(slug):
    s, S, J = load(slug)
    ANK = S(2, -46); PLAT = S(30, -2); PLATE = S(-548, -416); RAIL = S(-387, -330)
    PAD = S(-497, -628); SH = S(-462, -621); CALF = S(-53, -147)
    KNEE = S(-25, -274); LOW = S(5, -68); BACK = S(-330, -500)
    return [
        hook("GIMNASIO · PIERNAS", ["GEMELOS EN", "LA HACK"], "Pantorrillas en palanca",
             "Gemelos en la sentadilla hack: la punta de los pies en la plataforma y los tobillos empujan el carro hacia arriba.",
             [C("START"), seqloop("START", "RAISE")]),
        step("LA MÁQUINA", ["CARRO Y", "RIELES"], "Palanca inclinada",
             "El carro con discos corre sobre dos rieles inclinados y la plataforma de los pies queda fija abajo.",
             [C("START")], [ring(PLATE, 58, 0.8), lab((60, 1050), "DISCOS", "start", 0.8),
                            ring(RAIL, 44, 1.7), lab((60, 1180), "RIELES", "start", 1.7),
                            ring(PLAT, 46, 2.6), lab((985, 1400), "PLATAFORMA", "end", 2.6)], 7.2),
        step("AJUSTE 1", ["HOMBROS", "EN EL APOYO"], "Bien sentado",
             "Apoyá la espalda en el respaldo y las hombreras sobre los hombros, sin despegar la cadera del carro.",
             [C("START")], [ring(PAD, 46, 0.8), lab((985, 720), "HOMBRERAS", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["PUNTA DE", "LOS PIES"], "Al borde",
             "Apoyá solo la punta de los pies en el borde de la plataforma, con los talones afuera y libres.",
             [C("START")], [ring(ANK, 44, 0.8), lab((985, 1330), "PUNTA AL BORDE", "end", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["TALONES", "ABAJO"], "Rodillas trabadas",
             "Dejá caer los talones hasta sentir el estiramiento y quedate con las rodillas trabadas, sin doblarlas.",
             [C("START")], [ring(CALF, 50, 0.8), lab((60, 1300), "TALÓN BAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ CON", "EL TOBILLO"], "Solo el tobillo",
             "Paso uno. Empujá la plataforma con la punta de los pies y subí el carro, sin mover las rodillas.",
             [C("START"), TO("RAISE", 0.6, 1.0)],
             [arrow((ANK[0], ANK[1] + 10), (ANK[0], ANK[1] - 70), 0.8, 1.0, [40, 0]),
              lab((985, 780), "EMPUJÁ CON EL TOBILLO", "end", 1.0)], 7.0),
        step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso dos. Sostené un segundo arriba, con los tobillos bien extendidos y los gemelos apretados.",
             [C("RAISE"), TO("RAISE", 0.2, 0.4)], [ring(CALF, 50, 0.8), lab((60, 1240), "APRETÁ", "start", 1.0)], 6.8),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Sin rebotar",
             "Paso tres. Bajá lento hasta el estiramiento completo, sin rebotar abajo ni soltar el peso.",
             [C("RAISE"), TO("START", 0.5, 1.2)],
             [arrow((ANK[0], ANK[1] - 70), (ANK[0], ANK[1] + 10), 0.8, 1.0, [40, 0]),
              lab((985, 780), "BAJÁ LENTO", "end", 1.1)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al subir",
             "Soltá el aire cuando empujás y tomá aire cuando bajás. El abdomen queda firme y la espalda en el respaldo.",
             [C("START"), seqloop("START", "RAISE", 0.9, 1.7, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["DOBLAR LAS", "RODILLAS"], "Rodillas trabadas",
             "Error: doblar las rodillas para empujar. Las rodillas quedan trabadas y el recorrido lo hacen los tobillos.",
             [C("START"), TO("KNEE_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(KNEE, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: subir apenas unos centímetros. Subí hasta el tope, hacé la pausa y bajá hasta el estiramiento.",
             [C("START"), TO("HALF_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(LOW, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["DESPEGAR", "LA ESPALDA"], "Espalda apoyada",
             "Error: despegar la espalda del respaldo y redondearla. La espalda queda apoyada y el pecho arriba.",
             [C("START"), TO("ARCH_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(BACK, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Punta de los pies", "Rodillas trabadas",
                                         "Pausa arriba", "Bajá lento"],
             "Tips: punta de los pies en la plataforma, rodillas trabadas, pausa arriba y bajada lenta.",
             [C("START"), seqloop("START", "RAISE")]),
        keys("CLAVES", ["TÉCNICA"], ["Empujá con el tobillo", "Sin mover las rodillas",
                                     "Talones afuera", "Mirada al frente"],
             "Claves: empujá con el tobillo, sin mover las rodillas, talones afuera y mirada al frente.",
             [{"cut": "RAISE", "at": 0.1}]),
        reps(["3 X 15–20"], "Gemelos",
             "Tres series de quince a veinte repeticiones, con un minuto de pausa. Elegí un peso que te deje llegar arriba sin rebotar.",
             ["1 · EMPUJÁ", "2 · PAUSA", "3 · BAJÁ"], [C("START"), seqloop("START", "RAISE")]),
        step("AL TERMINAR", ["SALÍ", "DESPACIO"], "Sin apurarse",
             "Al terminar la serie, bajá el carro despacio, apoyá los talones y salí de la máquina sin encorvarte.",
             [C("RAISE"), TO("START", 0.9, 2.0)],
             [lab((60, 1000), "SIN REBOTAR", "start", 1.0)], 6.5),
    ]


YT62 = {
    "titulo": "Hack Calf Raise 🔥 Gemelos en la sentadilla hack | Gimnasio",
    "tags": ["hack calf raise", "gemelos en hack", "sentadilla hack", "pantorrillas",
             "gemelos", "sóleo", "máquina hack", "ejercicio de pantorrillas",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Hack Calf Raise",
        "elevación de talones en la sentadilla hack con el carro inclinado",
        "gemelos y sóleo",
        "En la hack la plataforma queda fija y el carro corre por los rieles: con la punta de los pies apoyada y las rodillas trabadas, los tobillos empujan el carro hacia arriba. El recorrido es corto pero completo. Si doblás las rodillas, hacés media repetición o despegás la espalda, el trabajo se reparte y los gemelos quedan a medias.",
        ["Apoyá la espalda en el respaldo y las hombreras sobre los hombros.",
         "Poné solo la punta de los pies en el borde de la plataforma, con los talones afuera."],
        ["Dejá caer los talones hasta sentir el estiramiento, con las rodillas trabadas.",
         "Empujá la plataforma con los tobillos y subí el carro.",
         "Sostené un segundo arriba, con los gemelos apretados.",
         "Bajá lento hasta el estiramiento.",
         "Completá la serie y bajá el carro despacio."],
        ["Doblar las rodillas → las rodillas quedan trabadas y el recorrido lo hacen los tobillos.",
         "Media repetición → subí hasta el tope y hacé la pausa completa.",
         "Despegar la espalda → espalda apoyada en el respaldo y pecho arriba."],
        ["Punta de los pies en la plataforma.", "Rodillas trabadas durante todo el recorrido.",
         "Pausa de un segundo arriba.", "Bajada lenta, sin rebotar."],
        "Piernas → Gemelos → Sóleo",
        "3 series de 15–20 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Pantorrillas #SentadillaHack #HackSquat #Piernas #Entrenamiento #Fuerza")}

save("hack-calf-raise", hc_scenes("hack-calf-raise"),
     {"pose": "RAISE", "zoom": 1.06, "dy": 40}, YT62)
