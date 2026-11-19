# Dataset D63 Hack One Leg Calf Raise: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def hc1_scenes(slug):
    s, S, J = load(slug)
    ANK = S(2, -46); PLAT = S(30, -2); PLATE = S(-548, -416); RAIL = S(-387, -330)
    PAD = S(-497, -628); FREE = S(-85, -165); CALF = S(-53, -147)
    KNEE = S(-25, -274); LOW = S(5, -68); BACK = S(-330, -500)
    return [
        hook("GIMNASIO · PIERNAS", ["GEMELOS A", "UNA PIERNA"], "Pantorrillas en palanca",
             "Gemelos a una pierna en la sentadilla hack: un pie en la plataforma, la otra pierna colgada y el tobillo empuja el carro.",
             [C("START"), seqloop("START", "RAISE")]),
        step("LA MÁQUINA", ["CARRO Y", "RIELES"], "Palanca inclinada",
             "El carro con discos corre sobre dos rieles inclinados y la plataforma de los pies queda fija abajo.",
             [C("START")], [ring(PLATE, 58, 0.8), lab((60, 1050), "DISCOS", "start", 0.8),
                            ring(RAIL, 44, 1.7), lab((60, 1180), "RIELES", "start", 1.7),
                            ring(PLAT, 46, 2.6), lab((985, 1400), "PLATAFORMA", "end", 2.6)], 7.2),
        step("AJUSTE", ["HOMBROS", "EN EL APOYO"], "Bien sentado",
             "Apoyá la espalda en el respaldo y las hombreras sobre los hombros, sin despegar la cadera del carro.",
             [C("START")], [ring(PAD, 46, 0.8), lab((985, 720), "HOMBRERAS", "end", 1.0)], 7.0),
        step("UN PIE", ["PUNTA EN LA", "PLATAFORMA"], "Solo el pie que trabaja",
             "Apoyá la punta de un solo pie en el borde de la plataforma; la otra pierna queda colgada, sin tocar nada.",
             [C("START")], [ring(ANK, 44, 0.8), lab((985, 1330), "PUNTA AL BORDE", "end", 1.0),
                            ring(FREE, 44, 2.0), lab((60, 1300), "PIERNA LIBRE", "start", 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["TALÓN", "ABAJO"], "Rodilla trabada",
             "Dejá caer el talón hasta sentir el estiramiento, con la rodilla trabada y la cadera pegada al carro.",
             [C("START")], [ring(CALF, 50, 0.8), lab((60, 1180), "TALÓN BAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ CON", "EL TOBILLO"], "Solo el tobillo",
             "Paso uno. Empujá la plataforma con la punta del pie y subí el carro, sin mover la rodilla ni la cadera.",
             [C("START"), TO("RAISE", 0.6, 1.0)],
             [arrow((ANK[0], ANK[1] + 10), (ANK[0], ANK[1] - 70), 0.8, 1.0, [40, 0]),
              lab((985, 780), "EMPUJÁ CON EL TOBILLO", "end", 1.0)], 7.0),
        step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso dos. Sostené un segundo arriba, con el tobillo bien extendido y el gemelo apretado.",
             [C("RAISE"), TO("RAISE", 0.2, 0.4)], [ring(CALF, 50, 0.8), lab((60, 1240), "APRETÁ", "start", 1.0)], 6.8),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Sin rebotar",
             "Paso tres. Bajá lento hasta el estiramiento completo, sin rebotar abajo ni soltar el peso.",
             [C("RAISE"), TO("START", 0.5, 1.2)],
             [arrow((ANK[0], ANK[1] - 70), (ANK[0], ANK[1] + 10), 0.8, 1.0, [40, 0]),
              lab((985, 780), "BAJÁ LENTO", "end", 1.1)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al subir",
             "Soltá el aire cuando empujás y tomá aire cuando bajás. El abdomen queda firme y la espalda en el respaldo.",
             [C("START"), seqloop("START", "RAISE", 0.9, 1.7, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["DOBLAR LA", "RODILLA"], "Rodilla trabada",
             "Error: doblar la rodilla para empujar. La rodilla queda trabada y el recorrido lo hace el tobillo.",
             [C("START"), TO("KNEE_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(KNEE, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: subir apenas unos centímetros. Subí hasta el tope, hacé la pausa y bajá hasta el estiramiento.",
             [C("START"), TO("HALF_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(LOW, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["DESPEGAR", "LA ESPALDA"], "Espalda apoyada",
             "Error: despegar la espalda del respaldo y redondearla. La espalda queda apoyada y el pecho arriba.",
             [C("START"), TO("ARCH_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(BACK, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Un pie en la plataforma", "Rodilla trabada",
                                         "Pausa arriba", "Bajá lento"],
             "Tips: un pie en la plataforma, rodilla trabada, pausa arriba y bajada lenta.",
             [C("START"), seqloop("START", "RAISE")]),
        keys("CLAVES", ["TÉCNICA"], ["Empujá con el tobillo", "Sin doblar la rodilla",
                                     "Pierna libre colgada", "Mirada al frente"],
             "Claves: empujá con el tobillo, sin doblar la rodilla, pierna libre colgada y mirada al frente.",
             [{"cut": "RAISE", "at": 0.1}]),
        reps(["3 X 12–15 X LADO"], "Gemelos",
             "Tres series de doce a quince repeticiones por pierna, con un minuto de pausa. Elegí un peso que te deje llegar arriba sin rebotar.",
             ["1 · EMPUJÁ", "2 · PAUSA", "3 · BAJÁ"], [C("START"), seqloop("START", "RAISE")]),
        step("AL TERMINAR", ["CAMBIÁ", "DE PIE"], "Sin apurarse",
             "Al terminar la serie, bajá el carro despacio, apoyá los dos pies y cambiá de pierna sin encorvarte.",
             [C("RAISE"), TO("START", 0.9, 2.0)],
             [lab((60, 1000), "SIN REBOTAR", "start", 1.0)], 6.5),
    ]


YT63 = {
    "titulo": "Hack One Leg Calf Raise 🔥 Gemelos a una pierna en la hack | Gimnasio",
    "tags": ["hack one leg calf raise", "gemelos a una pierna", "sentadilla hack", "pantorrillas",
             "gemelos", "sóleo", "máquina hack", "unilateral",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Hack One Leg Calf Raise",
        "elevación de talones a una pierna en la sentadilla hack",
        "gemelos y sóleo",
        "La versión a una pierna carga todo el peso sobre un gemelo y deja la otra pierna colgada. La plataforma queda fija y el carro corre por los rieles: el tobillo hace el recorrido completo. Si doblás la rodilla, hacés media repetición o despegás la espalda, el trabajo se reparte y el gemelo queda a medias.",
        ["Apoyá la espalda en el respaldo y las hombreras sobre los hombros.",
         "Poné la punta de un solo pie en el borde de la plataforma; la otra pierna queda colgada."],
        ["Dejá caer el talón hasta sentir el estiramiento, con la rodilla trabada.",
         "Empujá la plataforma con el tobillo y subí el carro.",
         "Sostené un segundo arriba, con el gemelo apretado.",
         "Bajá lento hasta el estiramiento.",
         "Completá la serie y cambiá de pierna."],
        ["Doblar la rodilla → la rodilla queda trabada y el recorrido lo hace el tobillo.",
         "Media repetición → subí hasta el tope y hacé la pausa completa.",
         "Despegar la espalda → espalda apoyada en el respaldo y pecho arriba."],
        ["Un solo pie en la plataforma.", "Rodilla trabada durante todo el recorrido.",
         "Pierna libre colgada, sin apoyar.", "Bajada lenta, sin rebotar."],
        "Piernas → Gemelos → Sóleo",
        "3 series de 12–15 repeticiones por pierna, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Pantorrillas #SentadillaHack #Unilateral #Piernas #Entrenamiento #Fuerza")}

save("hack-one-leg-calf-raise", hc1_scenes("hack-one-leg-calf-raise"),
     {"pose": "RAISE", "zoom": 1.06, "dy": 40}, YT63)
