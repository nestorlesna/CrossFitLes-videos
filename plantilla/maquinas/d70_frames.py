# Dataset D94 Smith Shoulder Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def sho_scenes(slug):
    s, S, J = load(slug)
    BAR = S(150, -620); BAR_T = S(150, -815); BEAM = S(150, -1047); PAR = S(430, -560)
    STOP = S(-130, -430); SEAT = S(-160, -240); BACK = S(-50, -330); FOOT = S(205, -46)
    SHO = S(10, -526); SHO_T = S(10, -540); HAND_H = S(150, -710); LUMB = S(-45, -380)
    return [
        hook("GIMNASIO · HOMBROS", ["PRESS DE", "HOMBROS"], "Sentado en la Smith",
             "Press de hombros en la Smith: sentado, la barra sube por delante de la cara hasta estirar los brazos sin arquear la espalda.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Banco con respaldo",
             "En la Smith la barra corre guiada entre los parantes y el banco con respaldo te deja sentado, firme y estable.",
             [C("DOWN")], [ring(BEAM, 66, 0.8), lab((60, 720), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 56, 1.8), lab((60, 800), "PARANTE", "start", 1.8),
                           ring(SEAT, 70, 2.8), lab((60, 1160), "BANCO", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["ASIENTO", "A TU ALTURA"], "Espalda al respaldo",
             "Ajustá el asiento para que la barra quede a la altura de los hombros y apoyá bien la espalda en el respaldo.",
             [C("DOWN")], [ring(SEAT, 70, 0.8), lab((60, 720), "ASIENTO A TU ALTURA", "start", 0.8),
                           ring(BACK, 62, 1.8), lab((60, 800), "ESPALDA APOYADA", "start", 1.8)], 7.4),
        step("AJUSTE 2 / 2", ["AGARRE", "PRONO"], "Manos abiertas",
             "Agarrá la barra con las palmas hacia delante y las manos un poco más abiertas que los hombros.",
             [C("DOWN")], [ring(BAR, 64, 0.8), lab((60, 720), "AGARRE PRONO", "start", 0.8),
                           ring(HAND_H, 52, 1.8), lab((1030, 800), "MANOS ABIERTAS", "end", 1.8)], 7.4),
        step("POSICIÓN INICIAL", ["BARRA AL", "MENTÓN"], "Codos abiertos",
             "Arrancá con la barra a la altura del mentón, los codos abiertos y los pies bien plantados en el piso.",
             [C("DOWN")], [ring(BAR, 64, 0.8), lab((60, 720), "BARRA AL MENTÓN", "start", 1.0),
                           ring(FOOT, 52, 1.8), lab((1030, 900), "PIES AL PISO", "end", 1.8)], 7.2),
        step("PASO 1 / 3", ["EMPUJÁ", "ARRIBA"], "Sin arquear",
             "Paso uno. Empujá la barra hacia arriba hasta estirar los brazos, sin arquear la espalda ni encogerte.",
             [C("DOWN"), TO("TOP", 0.4, 0.9)], [ring(SHO_T, 44, 0.8), lab((60, 720), "EMPUJÁ ARRIBA", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["ARRIBA", "CON TODO"], "Brazos extendidos",
             "Paso dos. Llegá arriba con los brazos bien extendidos y las costillas abajo: la espalda sigue en el respaldo.",
             [C("TOP"), TO("TOP", 0.2, 0.4)], [ring(BAR_T, 62, 0.8), lab((1030, 720), "BRAZOS EXTENDIDOS", "end", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "AL MENTÓN"], "Controlá la vuelta",
             "Paso tres. Bajá la barra despacio hasta el mentón, controlando el recorrido sin soltar el abdomen.",
             [C("TOP"), TO("DOWN", 0.5, 1.1)], [ring(BAR, 64, 0.8), lab((60, 720), "BAJÁ AL MENTÓN", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al empujar",
             "Tomá aire cuando bajás la barra y soltalo cuando empujás. No aguantes el aire arriba.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta el mentón y subí hasta estirar los brazos.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(HAND_H, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["ARQUEAR", "LA ESPALDA"], "Costillas abajo",
             "Error: arquear la espalda para empujar. La espalda queda apoyada en el respaldo y las costillas abajo.",
             [C("DOWN"), TO("ARCH_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(LUMB, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["ENCOGER", "LOS HOMBROS"], "Hombros abajo",
             "Error: encogerse de hombros al empujar. Los hombros quedan abajo y el trabajo lo hacen los brazos.",
             [C("DOWN"), TO("SHRUG_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(SHO, 46, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Espalda en el respaldo", "Barra al mentón",
                                          "Subí sin arquear", "Bajada controlada"],
             "Tips: espalda en el respaldo, barra al mentón, subí sin arquear y bajada controlada.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Codos abiertos", "Abdomen firme",
                                     "Pies plantados", "Recorrido completo"],
             "Claves: codos abiertos, abdomen firme, pies plantados y recorrido completo.",
             [{"cut": "TOP", "at": 0.1}]),
        reps(["3 X 8–12"], "Hombros",
             "Tres series de ocho a doce repeticiones, con un minuto y medio de pausa. Peso moderado y sin arquear la espalda.",
             ["1 · EMPUJÁ", "2 · ARRIBA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "TOP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ", "LA BARRA"], "Sin apurarse",
             "Al terminar la serie, dejá la barra en los topes, soltá las manos y recién ahí salí del banco.",
             [C("TOP"), TO("DOWN", 0.9, 2.0)],
             [lab((60, 720), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT94 = {
    "titulo": "Smith Shoulder Press 🔥 Press de hombros en la Smith | Gimnasio",
    "tags": ["smith shoulder press", "press de hombros", "press militar", "press sentado", "smith machine",
             "multipower", "hombros", "deltoides", "tríceps", "gimnasio", "principiantes", "rutina de hombros"],
    "descripcion": yt_desc("Smith Shoulder Press",
        "press de hombros sentado en la máquina Smith",
        "hombros, deltoides y tríceps",
        "La Smith guía la barra en línea recta y el banco con respaldo deja el torso estable, así que el press de hombros se puede hacer con un recorrido fijo y controlado. La barra arranca a la altura del mentón, por delante de la cara, y sube hasta estirar los brazos, con los codos abiertos y el abdomen firme. Si te arqueás, te encogés o cortás el recorrido, el hombro pierde tensión y la zona lumbar se lleva el trabajo.",
        ["Ajustá el asiento para que la barra quede a la altura de los hombros.",
         "Sentate con la espalda apoyada en el respaldo y los pies plantados."],
        ["Agarrá la barra con agarre prono, un poco más abierto que los hombros.",
         "Arrancá con la barra a la altura del mentón y los codos abiertos.",
         "Empujá la barra hacia arriba hasta estirar los brazos.",
         "Mantené las costillas abajo, sin arquear la espalda.",
         "Bajá controlando hasta el mentón y repetí."],
        ["Arquear la espalda → espalda apoyada y costillas abajo.",
         "Encogerse de hombros → los hombros quedan abajo.",
         "Media repetición → bajá hasta el mentón y subí hasta estirar."],
        ["Espalda en el respaldo.", "Barra al mentón, codos abiertos.",
         "Abdomen firme y costillas abajo.", "Bajada controlada."],
        "Hombros → Deltoides → Tríceps",
        "3 series de 8–12 repeticiones, con 1 minuto y medio de pausa. Nivel: principiante.",
        "#Gimnasio #Hombros #Deltoides #SmithMachine #Multipower #Press #Entrenamiento #Fuerza")}

save("smith-shoulder-press", sho_scenes("smith-shoulder-press"),
     {"pose": "TOP", "zoom": 1.0, "dy": 190}, YT94)
