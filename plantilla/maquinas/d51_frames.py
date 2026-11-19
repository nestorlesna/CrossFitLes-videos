# Dataset D75 Smith Behind Neck Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def bnp_scenes(slug):
    s, S, J = load(slug)
    BAR = S(-30, -590); BAR_T = S(0, -846); BEAM = S(-30, -912); PAR = S(250, -500)
    SEAT = S(-110, -230); BACK = S(-250, -470); SHO = S(10, -516); SHO_T = S(10, -534)
    LOW = S(-60, -380); HAND_H = S(-25, -720); FOOT = S(180, -36)
    return [
        hook("GIMNASIO · HOMBROS", ["DETRÁS", "DE LA NUCA"], "En la Smith",
             "Press por detrás de la nuca en la Smith: sentado, la barra baja a la nuca y se empuja hasta arriba sin arquear la espalda.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Banco con respaldo",
             "En la Smith la barra corre guiada entre los parantes y el banco con respaldo te deja sentado y estable.",
             [C("DOWN")], [ring(BEAM, 66, 0.8), lab((60, 720), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 56, 1.8), lab((60, 800), "PARANTE", "start", 1.8),
                           ring(SEAT, 70, 2.8), lab((60, 1160), "BANCO", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["ESPALDA", "AL RESPALDO"], "Bien sentado",
             "Sentate con la espalda apoyada en el respaldo y los pies bien plantados en el piso.",
             [C("DOWN")], [ring(BACK, 62, 0.8), lab((60, 720), "ESPALDA APOYADA", "start", 0.8),
                           ring(FOOT, 52, 1.8), lab((1030, 900), "PIES AL PISO", "end", 1.8)], 7.2),
        step("AJUSTE 2 / 2", ["BARRA A", "LA NUCA"], "Agarre abierto",
             "Agarrá la barra con las manos bien abiertas y llevala detrás de la cabeza, a la altura de la nuca.",
             [C("DOWN")], [ring(BAR, 64, 0.8), lab((60, 720), "BARRA A LA NUCA", "start", 0.8)], 7.4),
        step("POSICIÓN INICIAL", ["CODO", "ABIERTO"], "Barra en la nuca",
             "Arrancá con la barra en la nuca, los codos abiertos y el abdomen firme, sin sacar el pecho.",
             [C("DOWN")], [ring(BAR, 64, 0.8), lab((60, 720), "CODO ABIERTO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "ARRIBA"], "Sin arquear",
             "Paso uno. Empujá la barra hacia arriba hasta estirar los brazos, sin arquear la espalda ni encogerte.",
             [C("DOWN"), TO("TOP", 0.4, 0.9)], [ring(SHO_T, 44, 0.8), lab((60, 720), "EMPUJÁ ARRIBA", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["ARRIBA", "CON TODO"], "Brazos extendidos",
             "Paso dos. Llegá arriba con los brazos bien extendidos y las costillas abajo: el cuerpo queda derecho.",
             [C("TOP"), TO("TOP", 0.2, 0.4)], [ring(BAR_T, 62, 0.8), lab((1030, 720), "BRAZOS EXTENDIDOS", "end", 1.0)], 7.0),
        step("PASO 3 / 3", ["BAJÁ", "A LA NUCA"], "Controlá la vuelta",
             "Paso tres. Bajá la barra despacio hasta la nuca, controlando el recorrido sin soltar el abdomen.",
             [C("TOP"), TO("DOWN", 0.5, 1.1)], [ring(BAR, 64, 0.8), lab((60, 720), "BAJÁ A LA NUCA", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al empujar",
             "Tomá aire cuando bajás la barra y soltalo cuando empujás. No aguantes el aire arriba.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta la nuca y subí hasta estirar los brazos.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(HAND_H, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["ARQUEAR", "LA ESPALDA"], "Costillas abajo",
             "Error: arquear la espalda para empujar. La espalda queda apoyada en el respaldo y las costillas abajo.",
             [C("DOWN"), TO("ARCH_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(LOW, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["ENCOGER", "LOS HOMBROS"], "Hombros abajo",
             "Error: encogerse de hombros al empujar. Los hombros quedan abajo y el trabajo lo hacen los brazos.",
             [C("DOWN"), TO("SHRUG_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(SHO_T, 44, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Espalda en el respaldo", "Barra a la nuca",
                                          "Subí sin arquear", "Bajada controlada"],
             "Tips: espalda en el respaldo, barra a la nuca, subí sin arquear y bajada controlada.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Codos abiertos", "Abdomen firme",
                                    "Sin encogerse", "Recorrido completo"],
             "Claves: codos abiertos, abdomen firme, sin encogerse y recorrido completo.",
             [{"cut": "TOP", "at": 0.1}]),
        reps(["3 X 8–12"], "Hombros",
             "Tres series de ocho a doce repeticiones, con un minuto y medio de pausa. Peso moderado y sin arquear la espalda.",
             ["1 · EMPUJÁ", "2 · ARRIBA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "TOP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ", "LA BARRA"], "Sin apurarse",
             "Al terminar la serie, dejá la barra en los topes, soltá las manos y recién ahí salí del banco.",
             [C("TOP"), TO("DOWN", 0.9, 2.0)],
             [lab((60, 720), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT75 = {
    "titulo": "Smith Behind Neck Press 🔥 Press detrás de la nuca en la Smith | Gimnasio",
    "tags": ["smith behind neck press", "press detrás de la nuca", "press militar", "smith machine",
             "hombros", "deltoides", "multipower", "press sentado", "gimnasio", "principiantes",
             "rutina de hombros", "fuerza"],
    "descripcion": yt_desc("Smith Behind Neck Press",
        "press de hombros por detrás de la nuca guiado en la Smith",
        "hombros y deltoides",
        "La Smith guía la barra en línea recta y el banco con respaldo deja el torso estable, así que el press por detrás de la nuca se puede hacer con un recorrido fijo y controlado. La barra baja hasta la nuca y sube hasta estirar los brazos, con los codos abiertos y el abdomen firme. Si arqueás la espalda, te encogés o cortás el recorrido, el hombro pierde tensión y la zona lumbar se lleva el trabajo.",
        ["Sentate con la espalda apoyada en el respaldo y los pies plantados.",
         "Agarrá la barra con las manos bien abiertas y llevala detrás de la cabeza."],
        ["Arrancá con la barra en la nuca y los codos abiertos.",
         "Empujá la barra hacia arriba hasta estirar los brazos.",
         "Mantené las costillas abajo, sin arquear la espalda.",
         "Bajá controlando hasta la nuca.",
         "Completá la serie y dejá la barra en los topes."],
        ["Arquear la espalda → espalda apoyada y costillas abajo.",
         "Encogerse de hombros → los hombros quedan abajo.",
         "Media repetición → bajá hasta la nuca y subí hasta estirar."],
        ["Espalda en el respaldo.", "Barra a la nuca, codos abiertos.",
         "Abdomen firme y costillas abajo.", "Bajada controlada."],
        "Hombros → Deltoides",
        "3 series de 8–12 repeticiones, con 1 minuto y medio de pausa. Nivel: intermedio.",
        "#Gimnasio #Hombros #Deltoides #SmithMachine #Multipower #Press #Entrenamiento #Fuerza")}

save("smith-behind-neck-press", bnp_scenes("smith-behind-neck-press"),
     {"pose": "TOP", "zoom": 1.0, "dy": 30}, YT75)
