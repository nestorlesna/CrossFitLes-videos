# Dataset D71 Sled Lying Calf Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def lying_scenes(slug):
    s, S, J = load(slug)
    PLAT = S(154, -268); PAD = S(150, -300); RAIL = S(100, -78); STACK = S(234, -660)
    BENCH = S(-300, -150); BAL = S(131, -250); ANK_U = S(107, -200); SHIN = S(-93, -319)
    CALF = S(-20, -240); HIP = S(-300, -198)
    return [
        hook("GIMNASIO · PIERNAS", ["GEMELOS", "EN EL SLED"], "Tumbado y de frente",
             "Gemelos en el sled tumbado: la plataforma se empuja con la punta de los pies y el tobillo hace todo el recorrido.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BANCO", "Y PLATAFORMA"], "Carro con cable",
             "El banco queda horizontal, la plataforma se desliza sobre un riel y la pila del otro lado le da la carga.",
             [C("DOWN")], [ring(PAD, 66, 0.8), lab((470, 1090), "PLATAFORMA", "start", 0.8),
                           ring(STACK, 62, 1.8), lab((1000, 900), "PILA DE PESO", "end", 1.8),
                           ring(RAIL, 40, 2.8), lab((240, 1180), "RIEL", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["ESPALDA", "EN EL BANCO"], "Bien apoyado",
             "Acostate con la espalda y la cadera pegadas al banco, la cabeza en el apoyo y los brazos al costado.",
             [C("DOWN")], [ring(BENCH, 90, 0.8), lab((160, 1150), "ESPALDA APOYADA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PLANTA", "EN LA PLATAFORMA"], "Rodillas casi rectas",
             "Apoyá la planta completa en la plataforma con los tobillos a noventa grados y las rodillas casi extendidas.",
             [C("DOWN")], [ring(PLAT, 62, 0.8), lab((600, 1170), "PLANTA COMPLETA", "start", 0.8),
                           ring(SHIN, 46, 1.9), lab((240, 1060), "RODILLA BLANDA", "start", 1.9)], 7.8),
        step("POSICIÓN INICIAL", ["PUNTA", "ARRIBA"], "Talón abajo",
             "Arrancá con la punta de los pies hacia arriba y los talones bajos, sintiendo el estiramiento del gemelo.",
             [C("DOWN")], [ring(BAL, 46, 0.8), lab((520, 1150), "TALÓN ABAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "CON LA PUNTA"], "Solo el tobillo",
             "Paso uno. Empujá la plataforma con el metatarso estirando los tobillos, sin mover las rodillas.",
             [C("DOWN"), TO("UP", 0.4, 0.9)], [ring(CALF, 46, 0.8), lab((330, 1120), "APRETÁ EL GEMELO", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["PAUSA", "EN LA PUNTA"], "Un segundo",
             "Paso dos. Quedate un segundo en la punta más alta, con los tobillos estirados y el gemelo apretado.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(ANK_U, 46, 0.8), lab((560, 1150), "PAUSA ARRIBA", "start", 1.0)], 7.0),
        step("PASO 3 / 3", ["BAJÁ", "EL TALÓN"], "Controlá la vuelta",
             "Paso tres. Bajá los talones despacio hasta sentir el estiramiento, sin dejar que la plataforma gane velocidad.",
             [C("UP"), TO("DOWN", 0.5, 1.1)], [ring(BAL, 46, 0.8), lab((500, 1150), "BAJÁ CONTROLANDO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al empujar",
             "Tomá aire cuando bajás los talones y soltalo cuando empujás la plataforma. No aguantes el aire arriba.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["DOBLAR", "LAS RODILLAS"], "Rodillas quietas",
             "Error: doblar las rodillas para empujar la plataforma. Las rodillas quedan casi extendidas y quietas.",
             [C("DOWN"), TO("KNEE_BAD", 0.5, 0.9)],
             [NO(1.4, (150, 880)), ring(SHIN, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta estirar el gemelo y subí hasta la punta más alta.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(BAL, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["DESPEGAR", "LA CADERA"], "Cadera en el banco",
             "Error: levantar la cadera del banco para llegar más arriba. La cadera queda pegada todo el tiempo.",
             [C("DOWN"), TO("HIP_BAD", 0.5, 0.8)],
             [NO(1.4, (150, 880)), ring(HIP, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Talón abajo y punta arriba", "Empuje con el metatarso",
                                         "Rodillas casi rectas", "Pausa en la punta"],
             "Tips: arrancá con el talón bajo, empujá con el metatarso, rodillas casi rectas y pausa en la punta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Cadera pegada al banco", "Rodillas sin moverse",
                                     "Sin rebotar", "Recorrido completo"],
             "Claves: cadera pegada al banco, rodillas sin moverse, sin rebotar y recorrido completo.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15–20"], "Gemelos",
             "Tres series de quince a veinte repeticiones, con un minuto de pausa. Peso moderado y el recorrido completo, sin rebotar.",
             ["1 · EMPUJÁ", "2 · PAUSA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["SALÍ", "DESPACIO"], "Sin apurarse",
             "Al terminar la serie, volvé a apoyar la plataforma en el tope y recién ahí sentate y salí del banco.",
             [C("UP"), TO("DOWN", 0.9, 2.0)],
             [lab((520, 1150), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT71 = {
    "titulo": "Sled Lying Calf Press 🔥 Gemelos en el sled tumbado | Gimnasio",
    "tags": ["sled lying calf press", "gemelos en sled", "gemelos", "pantorrilla", "sled machine",
             "prensa tumbado", "piernas", "máquina de gimnasio", "gimnasio", "principiantes",
             "rutina de piernas", "entrenamiento de gemelos"],
    "descripcion": yt_desc("Sled Lying Calf Press",
        "extensión de tobillos en el sled tumbado",
        "gemelos",
        "En el sled tumbado la espalda y la cadera quedan en el banco y la plataforma corre sobre un riel: el movimiento es del tobillo, con las rodillas casi extendidas y quietas. Es la variante más directa para cargar los gemelos sin que la espalda tenga que sostener el peso. Si doblás las rodillas, cortás el recorrido o despegás la cadera, el estímulo se pierde.",
        ["Acostate con la espalda y la cadera pegadas al banco.",
         "Apoyá la planta completa con los tobillos a noventa grados."],
        ["Arrancá con la punta de los pies arriba y los talones bajos.",
         "Empujá la plataforma con el metatarso estirando los tobillos.",
         "Quedate un segundo arriba apretando el gemelo.",
         "Bajá controlando hasta sentir el estiramiento.",
         "Completá la serie y volvé la plataforma al tope."],
        ["Doblar las rodillas → las rodillas quedan casi rectas y quietas.",
         "Media repetición → bajá hasta el estiramiento y subí hasta la punta.",
         "Despegar la cadera → la cadera pegada al banco."],
        ["Talón abajo y punta arriba.", "Empuje con el metatarso.",
         "Rodillas casi rectas.", "Pausa de un segundo en la punta."],
        "Piernas → Gemelos → Pantorrilla",
        "3 series de 15–20 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Pantorrilla #SledMachine #Piernas #Entrenamiento #Fuerza")}

save("sled-lying-calf-press", lying_scenes("sled-lying-calf-press"),
     {"pose": "UP", "zoom": 1.06, "dy": 40}, YT71)
