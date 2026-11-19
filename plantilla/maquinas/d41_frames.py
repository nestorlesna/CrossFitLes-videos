# Dataset D65 Sled Hack Squat: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def hs_scenes(slug):
    s, S, J = load(slug)
    ANK = S(0, -60); ANK2 = S(-30, -60); PLAT = S(28, -16); PLATE = S(-548, -416)
    RAIL = S(-387, -330); PAD = S(-497, -628); HIP = S(-298, -395)
    HIPB = S(-172, -220); KNEEB = S(60, -282)
    return [
        hook("GIMNASIO · PIERNAS", ["AL ANCHO", "DE HOMBROS"], "La hack clásica",
             "Sentadilla hack con los pies al ancho de hombros: el carro inclinado baja por los rieles y las piernas empujan.",
             [C("TOP"), seqloop("TOP", "BOTTOM")]),
        step("LA MÁQUINA", ["CARRO Y", "RIELES"], "Palanca inclinada",
             "El carro con discos corre sobre dos rieles inclinados y la plataforma de los pies queda fija abajo.",
             [C("TOP")], [ring(PLATE, 58, 0.8), lab((60, 1030), "DISCOS", "start", 0.8),
                          ring(RAIL, 44, 1.7), lab((60, 1215), "RIELES", "start", 1.7),
                          ring(PLAT, 46, 2.6), lab((985, 1400), "PLATAFORMA", "end", 2.6)], 7.2),
        step("AJUSTE 1 / 2", ["PIES AL ANCHO", "DE HOMBROS"], "Base estable",
             "Apoyá la espalda en el respaldo y poné los pies al ancho de hombros, uno a cada lado del centro.",
             [C("TOP")], [ring(((ANK[0] + ANK2[0]) / 2, (ANK[1] + ANK2[1]) / 2), 68, 0.8),
                          lab((985, 1250), "AL ANCHO DE HOMBROS", "end", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["RODILLAS", "ALINEADAS"], "Puntas abiertas",
             "Girá un poco las puntas hacia afuera y llevá las rodillas en línea con los pies durante todo el recorrido.",
             [C("TOP")], [ring(PAD, 46, 0.8), lab((985, 760), "HOMBRERAS", "end", 1.0),
                          ring(HIP, 50, 2.0), lab((985, 980), "CADERA", "end", 2.0)], 7.2),
        step("POSICIÓN INICIAL", ["DE PIE", "ARRIBA"], "Rodillas blandas",
             "Arrancá arriba, con las rodillas blandas, la espalda apoyada y el pecho arriba, mirando al frente.",
             [C("TOP")], [ring(HIP, 50, 0.8), lab((985, 980), "CADERA ARRIBA", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "EL CARRO"], "Rodillas al frente",
             "Paso uno. Bajá el carro por los rieles y dejá que las rodillas vayan hacia adelante, en línea con las puntas.",
             [C("TOP"), TO("BOTTOM", 0.6, 1.2)],
             [arrow((1010, 1000), (1010, 1200), 0.8, 1.2, [40, 0]),
              lab((1010, 900), "BAJÁ LENTO", "end", 1.0)], 7.2),
        step("PASO 2 / 3", ["FONDO", "COMPLETO"], "Sin despegar",
             "Paso dos. Llegá hasta donde puedas con la espalda apoyada y la cadera abajo, sin levantar los talones.",
             [C("BOTTOM"), TO("BOTTOM", 0.2, 0.4)],
             [ring(KNEEB, 50, 0.8), lab((1000, 1080), "RODILLAS ALINEADAS", "end", 1.0)], 7.0),
        step("PASO 3 / 3", ["SUBÍ", "EMPUJANDO"], "Con los talones",
             "Paso tres. Empujá con los talones y subí el carro, estirando las piernas sin trabar las rodillas de golpe.",
             [C("BOTTOM"), TO("TOP", 0.5, 1.2)],
             [arrow((1010, 1200), (1010, 1000), 0.8, 1.2, [40, 0]),
              lab((1010, 900), "SUBÍ", "end", 1.1)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al subir",
             "Tomá aire al bajar y soltalo al subir. El abdomen queda firme y las costillas abajo durante todo el recorrido.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 0.9, 1.7, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "SENTADILLA"], "Fondo completo",
             "Error: bajar apenas un poco. Bajá hasta donde llegues con la espalda apoyada y los talones en la plataforma.",
             [C("TOP"), TO("SHALLOW_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(HIP, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["LEVANTAR", "LOS TALONES"], "Pies planos",
             "Error: levantar los talones para bajar más. Los pies quedan planos y el peso repartido en toda la planta.",
             [C("TOP"), TO("HEELS_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(ANK, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Espalda apoyada",
             "Error: redondear la espalda y despegarse del respaldo. La espalda queda apoyada y el pecho arriba.",
             [C("TOP"), TO("BACK_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(S(-127, -553), 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pies al ancho de hombros", "Rodillas con las puntas",
                                         "Talones abajo", "Subí parejo"],
             "Tips: pies al ancho de hombros, rodillas con las puntas, talones abajo y subida pareja.",
             [C("TOP"), seqloop("TOP", "BOTTOM")]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda en el respaldo", "Empujá con los talones",
                                     "Sin trabar las rodillas", "Mirada al frente"],
             "Claves: espalda en el respaldo, empujá con los talones, sin trabar las rodillas y mirada al frente.",
             [{"cut": "BOTTOM", "at": 0.1}]),
        reps(["3 X 8–12"], "Cuádriceps",
             "Tres series de ocho a doce repeticiones, con dos minutos de pausa. Un peso que te deje llegar al fondo sin despegar la espalda.",
             ["1 · BAJÁ", "2 · FONDO", "3 · SUBÍ"], [C("TOP"), seqloop("TOP", "BOTTOM")]),
        step("AL TERMINAR", ["SALÍ", "DESPACIO"], "Sin apurarse",
             "Al terminar la serie, subí el carro, trabá las manijas y salí de la máquina sin encorvarte.",
             [C("BOTTOM"), TO("TOP", 0.9, 2.0)],
             [lab((60, 1000), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT65 = {
    "titulo": "Sled Hack Squat 🔥 Sentadilla hack al ancho de hombros | Gimnasio",
    "tags": ["sled hack squat", "hack squat", "sentadilla hack", "sentadilla en máquina",
             "cuádriceps", "glúteos", "máquina hack", "piernas", "prensa inclinada",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Sled Hack Squat",
        "sentadilla hack con los pies al ancho de hombros en la plataforma",
        "cuádriceps y glúteos",
        "La sentadilla hack es una prensa inclinada con la espalda apoyada: el carro corre por los rieles y el peso se distribuye entre cuádriceps y glúteos. Con los pies al ancho de hombros y las rodillas alineadas con las puntas, el recorrido es estable y profundo. Si cortás el fondo, levantás los talones o redondeás la espalda, la sentadilla pierde tensión.",
        ["Apoyá la espalda en el respaldo y las hombreras sobre los hombros.",
         "Poné los pies al ancho de hombros, uno a cada lado del centro de la plataforma."],
        ["Arrancá arriba con las rodillas blandas y la espalda apoyada.",
         "Bajá el carro por los rieles con las rodillas en línea con las puntas.",
         "Llegá al fondo sin levantar los talones ni despegar la espalda.",
         "Subí empujando con los talones hasta estirar las piernas.",
         "Completá la serie y salí de la máquina despacio."],
        ["Media sentadilla → bajá hasta donde llegues con la espalda apoyada.",
         "Levantar los talones → pies planos y peso en toda la planta.",
         "Redondear la espalda → espalda apoyada y pecho arriba."],
        ["Pies al ancho de hombros.", "Rodillas alineadas con las puntas.",
         "Talones abajo durante todo el recorrido.", "Subida pareja, sin trabar las rodillas."],
        "Piernas → Cuádriceps → Glúteos",
        "3 series de 8–12 repeticiones, con 2 minutos de pausa. Nivel: principiante.",
        "#Gimnasio #Cuadriceps #SentadillaHack #HackSquat #Piernas #Gluteos #Entrenamiento #Fuerza")}

save("sled-hack-squat", hs_scenes("sled-hack-squat"),
     {"pose": "BOTTOM", "zoom": 1.06, "dy": 40}, YT65)
