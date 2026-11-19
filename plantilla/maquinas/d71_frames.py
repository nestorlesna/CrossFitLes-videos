# Dataset D95 Smith Shrug: escenas + YouTube + miniatura.
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
    BAR = S(25, -415); BAR_UP = S(25, -455); BEAM = S(25, -888); PAR = S(305, -560)
    STOP = S(-255, -300); SHO = S(-15, -740); HAND_H = S(25, -437); ELBOW = S(*J["ELBOW_BAD"]["E"])
    TRUNK = S(-54, -598)
    return [
        hook("GIMNASIO · ESPALDA", ["ENCOGER", "LOS HOMBROS"], "Barra a la cadera",
             "Encogimientos de hombros en la Smith: parado, brazos rectos y solo suben los hombros hacia las orejas.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.4, 1.0, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "De frente a la barra",
             "En la Smith la barra corre guiada en línea recta y los topes frenan la bajada, así que el encogimiento queda fijo.",
             [C("DOWN")], [ring(BEAM, 66, 0.8), lab((60, 760), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 56, 1.8), lab((60, 840), "PARANTE", "start", 1.8),
                           ring(STOP, 52, 2.8), lab((60, 920), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A", "LA CADERA"], "Brazos estirados",
             "Bajá la barra hasta la altura de la cadera, con los brazos estirados y los discos al lado de las piernas.",
             [C("DOWN")], [ring(BAR, 58, 0.8), lab((60, 760), "BARRA A LA CADERA", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["AGARRE", "PRONO"], "Manos cómodas",
             "Agarrá la barra con las palmas hacia delante, las manos un poco más abiertas que los hombros y los brazos rectos.",
             [C("DOWN")], [ring(HAND_H, 52, 0.8), lab((60, 760), "AGARRE PRONO", "start", 0.8),
                           ring(SHO, 44, 1.8), lab((1030, 840), "BRAZOS RECTOS", "end", 1.8)], 7.2),
        step("POSICIÓN INICIAL", ["HOMBROS", "RELAJADOS"], "Pies al ancho",
             "Arrancá con los pies al ancho de los hombros, las rodillas blandas y los hombros relajados, sin subirlos.",
             [C("DOWN")], [ring(SHO, 44, 0.8), lab((60, 760), "HOMBROS RELAJADOS", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ LOS", "HOMBROS"], "Hacia las orejas",
             "Paso uno. Subí los hombros hacia las orejas como si quisieras tocar el techo con la punta de arriba.",
             [C("DOWN"), TO("UP", 0.4, 0.9)], [ring(BAR_UP, 58, 0.8), lab((60, 760), "SUBÍ LOS HOMBROS", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["ARRIBA", "APRETÁ"], "Codos quietos",
             "Paso dos. Arriba, apretá los trapecios y quedate un instante: los codos no se doblan, los brazos quedan rectos.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(SHO, 44, 0.8), lab((1030, 760), "CODO QUIETO", "end", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "DESPACIO"], "Controlá la vuelta",
             "Paso tres. Bajá los hombros despacio hasta la posición inicial, sin soltarlos de golpe ni dejar caer la barra.",
             [C("UP"), TO("DOWN", 0.5, 1.1)], [ring(BAR, 58, 0.8), lab((60, 760), "BAJÁ DESPACIO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá arriba",
             "Tomá aire abajo y soltalo cuando suben los hombros. No aguantes el aire en todo el movimiento.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.3, 1.0, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Subí hasta arriba",
             "Error: quedarse a mitad de camino. Los hombros suben hasta arriba y los trapecios se aprietan de verdad.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(HAND_H, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["DOBLAR", "LOS CODOS"], "Brazos rectos",
             "Error: doblar los codos y tirar con los brazos. Los brazos quedan rectos y el trabajo lo hace el trapecio.",
             [C("DOWN"), TO("ELBOW_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(ELBOW, 52, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["BALANCEAR", "EL CUERPO"], "Sin impulso",
             "Error: tirar el cuerpo atrás para empujar con la barra. Las piernas quedan firmes y el tronco quieto.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(TRUNK, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Brazos bien rectos", "Barra a la cadera",
                                          "Subí sin impulso", "Bajá despacio"],
             "Tips: brazos bien rectos, barra a la cadera, subí sin impulso y bajá despacio.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.3, 1.0, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Hombros a las orejas", "Codos quietos",
                                     "Pies al ancho", "Recorrido corto"],
             "Claves: hombros a las orejas, codos quietos, pies al ancho y recorrido corto.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12–15"], "Trapecios",
             "Tres series de doce a quince repeticiones, con un minuto de pausa. Peso cómodo y sin balancear el cuerpo.",
             ["1 · SUBÍ", "2 · APRETÁ", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.0, 0.3)]),
        step("AL TERMINAR", ["DEJÁ", "LA BARRA"], "Sin apurarse",
             "Al terminar la serie, dejá la barra en los topes, soltá las manos y recién ahí salí de la máquina.",
             [C("UP"), TO("DOWN", 0.9, 2.0)],
             [lab((60, 760), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT95 = {
    "titulo": "Smith Shrug 🔥 Encogimientos de hombros en la Smith | Trapecios",
    "tags": ["smith shrug", "encogimientos de hombros", "shrug en smith", "smith machine", "multipower",
             "trapecios", "espalda alta", "hombros", "gimnasio", "principiantes", "rutina de espalda", "trapecio"],
    "descripcion": yt_desc("Smith Shrug",
        "encogimientos de hombros con la barra guiada en la Smith",
        "trapecios y espalda alta",
        "En la Smith la barra corre guiada en línea recta y los topes frenan la bajada, así que el encogimiento queda fijo y controlado. Se hace parado, de frente a la barra, con los brazos rectos y las manos un poco más abiertas que los hombros. Los hombros suben hacia las orejas y bajan despacio; los codos no se doblan y el tronco no se balancea. Si tirás con los brazos, cortás el recorrido o te colgás del impulso, el trapecio pierde el trabajo.",
        ["Bajá la barra hasta la altura de la cadera y ajustá los topes.",
         "Parate de frente a la barra con los pies al ancho de los hombros."],
        ["Agarrá la barra con agarre prono, un poco más abierto que los hombros.",
         "Arrancá con los hombros relajados y los brazos bien rectos.",
         "Subí los hombros hacia las orejas y apretá los trapecios.",
         "Mantené el tronco quieto, sin balancear el cuerpo.",
         "Bajá los hombros despacio hasta la posición inicial."],
        ["Doblar los codos → los brazos quedan rectos.",
         "Balancear el cuerpo → piernas firmes y tronco quieto.",
         "Media repetición → los hombros suben hasta arriba."],
        ["Brazos bien rectos.", "Barra a la altura de la cadera.",
         "Subí sin impulso de piernas.", "Bajada controlada."],
        "Espalda → Trapecios → Espalda alta",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Trapecios #Espalda #SmithMachine #Multipower #Shrug #Entrenamiento #Fuerza")}

save("smith-shrug", shrug_scenes("smith-shrug"),
     {"pose": "UP", "zoom": 1.0, "dy": 120}, YT95)
