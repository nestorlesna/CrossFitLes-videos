# Dataset D74 Smith Back Shrug: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def shrug_scenes(slug):
    s, S, J = load(slug)
    BAR = S(0, -440); BAR_U = S(0, -468); BEAM = S(0, -1006); STOP = S(300, -560)
    PAR = S(300, -700); FOOT = S(40, 0); SHO = S(30, -741); SHO_U = S(30, -769)
    BACK = S(60, -700); HAND_B = S(-70, -545); HIP = S(10, -462)
    return [
        hook("GIMNASIO · HOMBROS", ["HOMBROS", "EN LA SMITH"], "Barra detrás",
             "Encogimientos con la barra detrás de la espalda en la Smith: parado, la barra a la altura de la cadera y solo suben los hombros.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "En la Smith la barra corre guiada entre dos parantes, así que el recorrido es en línea recta y solo hay que empujar.",
             [C("DOWN")], [ring(BEAM, 70, 0.8), lab((150, 660), "BARRA GUIADA", "start", 0.8),
                           ring(STOP, 46, 1.8), lab((60, 1120), "TOPES", "start", 1.8),
                           ring(PAR, 60, 2.8), lab((1030, 660), "PARANTES", "end", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A LA", "CADERA"], "Agarre atrás",
             "Poné la barra a la altura de la cadera y agarrá con las dos manos detrás de la espalda, los brazos extendidos.",
             [C("DOWN")], [ring(BAR, 70, 0.8), lab((150, 660), "BARRA A LA CADERA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES AL", "ANCHO"], "Bien parado",
             "Quedate parado con los pies al ancho de la cadera y el peso repartido en toda la planta.",
             [C("DOWN")], [ring(FOOT, 56, 0.8), lab((150, 660), "PIES AL ANCHO", "start", 0.8)], 7.0),
        step("POSICIÓN INICIAL", ["HOMBROS", "ABAJO"], "Brazos extendidos",
             "Arrancá con los hombros bajos, los brazos extendidos y la barra apoyada en las manos, sintiendo el trapecio estirado.",
             [C("DOWN")], [ring(SHO, 44, 0.8), lab((150, 660), "HOMBROS ABAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ", "LOS HOMBROS"], "Solo el trapecio",
             "Paso uno. Subí los hombros hacia las orejas, como si encogieras el cuello. Los codos quedan extendidos.",
             [C("DOWN"), TO("UP", 0.4, 0.9)], [ring(SHO_U, 44, 0.8), lab((150, 660), "SUBÍ LOS HOMBROS", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso dos. Quedate un segundo arriba con los hombros bien altos, apretando el trapecio.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(SHO_U, 44, 0.8), lab((1030, 660), "PAUSA ARRIBA", "end", 1.0)], 7.0),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLANDO"], "Estirá el trapecio",
             "Paso tres. Bajá los hombros despacio hasta estirar el trapecio, sin soltar la barra ni doblar los codos.",
             [C("UP"), TO("DOWN", 0.5, 1.1)], [ring(SHO, 44, 0.8), lab((150, 660), "BAJÁ CONTROLANDO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire cuando bajás los hombros y soltalo cuando encogés. No aguantes el aire arriba.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["TIRAR", "CON LOS BRAZOS"], "Codos quietos",
             "Error: doblar los codos para levantar la barra. Los brazos quedan extendidos y el trabajo es del hombro.",
             [C("DOWN"), TO("ARMS_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HAND_B, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Subí hasta el tope y bajá hasta estirar el trapecio.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(SHO_U, 44, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["INCLINARSE", "ADELANTE"], "Tronco derecho",
             "Error: inclinar el tronco para usar la espalda. El cuerpo queda derecho y el movimiento es solo del hombro.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(BACK, 56, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra a la altura de la cadera", "Codos extendidos",
                                          "Hombros hacia las orejas", "Bajada controlada"],
             "Tips: barra a la altura de la cadera, codos extendidos, hombros hacia las orejas y bajada controlada.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Sin doblar los codos", "Tronco derecho",
                                    "Pausa arriba", "Estirá abajo"],
             "Claves: sin doblar los codos, tronco derecho, pausa arriba y estirá abajo.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12–15"], "Trapecio",
             "Tres series de doce a quince repeticiones, con un minuto de pausa. Peso moderado y una pausa de un segundo arriba.",
             ["1 · SUBÍ", "2 · PAUSA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["SOLTÁ", "DESPACIO"], "Sin apurarse",
             "Al terminar la serie, dejá la barra en los topes, soltá las manos y salí de la máquina con cuidado.",
             [C("UP"), TO("DOWN", 0.9, 2.0)],
             [lab((150, 660), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT74 = {
    "titulo": "Smith Back Shrug 🔥 Encogimientos con barra detrás en la Smith | Gimnasio",
    "tags": ["smith back shrug", "encogimientos de hombros", "smith machine", "barra detrás de la espalda",
             "trapecio", "hombros", "multipower", "gimnasio", "principiantes", "rutina de hombros",
             "entrenamiento de hombros", "fuerza"],
    "descripcion": yt_desc("Smith Back Shrug",
        "encogimientos de hombros con la barra detrás de la espalda en la máquina Smith",
        "trapecio",
        "En la Smith la barra va guiada entre dos parantes, así que el recorrido es en línea recta y con la barra detrás de la espalda el trapecio trabaja con el tronco bien derecho. Es un ejercicio corto: suben solo los hombros, con los codos extendidos y una pausa arriba. Si tirás con los brazos, cortás el recorrido o te inclinás, el trabajo se reparte a otros músculos.",
        ["Poné la barra a la altura de la cadera y agarrá detrás de la espalda.",
         "Parate con los pies al ancho de la cadera y los brazos extendidos."],
        ["Arrancá con los hombros bajos y el trapecio estirado.",
         "Subí los hombros hacia las orejas sin doblar los codos.",
         "Quedate un segundo arriba apretando el trapecio.",
         "Bajá controlando hasta estirar de nuevo.",
         "Completá la serie y dejá la barra en los topes."],
        ["Doblar los codos → los brazos quedan extendidos.",
         "Media repetición → subí hasta el tope y bajá hasta estirar.",
         "Inclinar el tronco → el cuerpo queda derecho."],
        ["Barra a la altura de la cadera.", "Codos extendidos todo el tiempo.",
         "Pausa de un segundo arriba.", "Bajada controlada."],
        "Hombros → Trapecio",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Trapecio #Hombros #SmithMachine #Multipower #Entrenamiento #Fuerza")}

save("smith-back-shrug", shrug_scenes("smith-back-shrug"),
     {"pose": "UP", "zoom": 1.02, "dy": 18}, YT74)
