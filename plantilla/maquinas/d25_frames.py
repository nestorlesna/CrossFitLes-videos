# Dataset D49 Lever Bent-over Row with V-Bar: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.6, at=0.4): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def tb_scenes(slug):
    s, S, J = load(slug)
    H0 = S(*J["HINGE"]["W"]); H1 = S(*J["PULL"]["W"])
    BASE = S(-420, 8); PLATE = S(58, -250); FOOT = S(0, 0); HIP = S(-80, -430)
    BACK = S(40, -500); TRAP = S(160, -555); MOM = S(50, -470)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO", "INCLINADO"], "Barra en V y bisagra de cadera",
             "Remo inclinado con barra en V: hacé la bisagra desde la cadera, mantené la espalda recta y tirá del agarre hacia el abdomen.",
             [C("HINGE"), seqloop("PULL", "HINGE", 1.0, 1.6, 0.3)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Barra en V y discos",
             "La máquina tiene una barra en V, discos cerca del agarre y un pivote en el piso. No tiene asiento: el torso trabaja.",
             [C("HINGE")], [ring(BASE, 42, 0.8), lab((60, 1480), "PIVOTE", "start", 0.8),
                            ring(FOOT, 38, 1.6), lab((985, 1480), "PIES", "end", 1.6),
                            ring(H0, 40, 2.4), lab((60, 1180), "AGARRE EN V", "start", 2.4),
                            ring(PLATE, 44, 3.2), lab((60, 1320), "DISCOS", "start", 3.2)], 7.4),
        step("AJUSTE 1", ["PIES Y", "CADERA"], "Bisagra desde la cadera",
             "Parate con los pies al ancho de los hombros, las rodillas apenas flexionadas y llevá la cadera atrás.",
             [C("HINGE")], [ring(HIP, 50, 0.8), lab((60, 1100), "CADERA ATRÁS", "start", 1.0),
                            ring(FOOT, 40, 2.2), lab((985, 1460), "PIES FIRMES", "end", 2.2)], 7.0),
        step("AJUSTE 2", ["AGARRE", "EN V"], "Agarre prono",
             "Tomá la barra en V con agarre prono y los brazos extendidos. El agarre queda debajo del pecho.",
             [C("HINGE")], [ring(H0, 44, 0.8), lab((60, 1280), "AGARRE PRONO", "start", 1.0),
                            ring(PLATE, 40, 2.2), lab((985, 1300), "BARRA EN V", "end", 2.2)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "RECTA"], "Pecho arriba",
             "Incliná el torso desde la cadera con la espalda recta y el pecho arriba. La mirada va al piso, adelante.",
             [C("HINGE")], [ring(BACK, 52, 0.8), lab((60, 1000), "ESPALDA RECTA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["TIRÁ DEL", "AGARRE"], "Hacia el abdomen",
             "Paso uno. Tirá del agarre hacia el abdomen sin cambiar el ángulo del torso.",
             [C("HINGE"), TO("PULL", 0.6, 1.0)],
             [arrow((H0[0] + 10, H0[1] - 20), (H1[0] + 10, H1[1] - 30), 0.8, 1.0, [30, -30]),
              lab((60, H0[1] - 40), "TIRÁ", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ LOS", "OMÓPLATOS"], "Pausa de un segundo",
             "Paso dos. Apretá los omóplatos al final del movimiento y hacé una pausa breve. El codo pasa cerca del torso.",
             [C("PULL"), TO("PULL", 0.2, 0.4)],
             [ring(BACK, 50, 0.8), lab((985, 1080), "APRETÁ", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin redondear",
             "Paso tres. Volvé lento a la posición inicial con los brazos extendidos y la espalda recta.",
             [C("PULL"), TO("HINGE", 0.5, 0.8)],
             [arrow((H1[0] + 10, H1[1] - 30), (H0[0] + 10, H0[1] - 20), 0.8, 0.8, [30, 30]),
              lab((60, H0[1] - 30), "VOLVÉ", "start", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando tirás y tomá aire cuando volvés. El abdomen queda firme y el tronco quieto.",
             [C("HINGE"), seqloop("PULL", "HINGE", 1.0, 1.6, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda para llegar más lejos. El pecho se queda arriba y la espalda recta.",
             [C("HINGE"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4, (540, 780)), ring(BACK, 52, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["SUBIR LOS", "HOMBROS"], "Hombros abajo",
             "Error: subir los hombros y tirar con el cuello. Los hombros quedan abajo y los omóplatos trabajan.",
             [C("HINGE"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(1.4, (540, 780)), ring(TRAP, 44, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["USAR", "IMPULSO"], "Torso quieto",
             "Error: pararte y usar el impulso del cuerpo. El ángulo del torso se mantiene y la espalda no rebota.",
             [C("HINGE"), TO("JERK_BAD", 0.5, 0.8)], [NO(1.4, (540, 780)), ring(MOM, 52, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Bisagra de cadera", "Espalda recta",
                                          "Codos cerca", "Volvé lento"],
             "Tips: bisagra de cadera, espalda recta, codos cerca del torso y volvé lento.",
             [C("HINGE"), seqloop("PULL", "HINGE", 1.0, 1.6, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Pies firmes", "Agarre prono",
                                     "Sin impulso", "Pausa arriba"],
             "Claves: pies firmes, agarre prono, sin impulso del torso y pausa arriba.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Un minuto de pausa",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · VOLVÉ"], [C("HINGE"), seqloop("PULL", "HINGE", 1.0, 1.6, 0.3)]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, dejá la barra bajar despacio y volvé a la posición inicial sin soltar el agarre de golpe.",
             [C("PULL"), TO("HINGE", 0.9, 1.8)],
             [lab((985, 1120), "SIN SOLTAR", "end", 1.0)], 6.5),
    ]


YT49 = {
    "titulo": "Lever Bent-over Row with V-Bar 🔥 Remo inclinado en palanca | Espalda",
    "tags": ["lever bent over row with v bar", "remo inclinado con barra en v", "remo en palanca",
             "remo inclinado", "t bar row", "espalda alta", "dorsales", "bíceps",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Bent-over Row with V-Bar",
        "remo inclinado con barra en V en máquina de palanca",
        "espalda alta y bíceps, con la bisagra de cadera",
        "El remo inclinado con barra en V trabaja la espalda desde una bisagra de cadera. Si redondeás la espalda, usás impulso o subís los hombros, el trabajo se reparte y los omóplatos no se juntan. La clave es mantener el ángulo del torso y tirar con los codos cerca.",
        ["Parate con los pies al ancho de los hombros y las rodillas apenas flexionadas.",
         "Llevá la cadera atrás y tomá la barra en V con agarre prono."],
        ["Hacé la bisagra desde la cadera con la espalda recta y el pecho arriba.",
         "Tomá la barra en V con agarre prono y los brazos extendidos.",
         "Tirá del agarre hacia el abdomen sin cambiar el ángulo del torso.",
         "Apretá los omóplatos un segundo y volvé lento.",
         "Mantené los pies firmes durante todo el recorrido."],
        ["Redondear la espalda → pecho arriba y espalda recta.",
         "Subir los hombros → hombros abajo y omóplatos hacia atrás.",
         "Usar impulso → el ángulo del torso se mantiene y la espalda no rebota."],
        ["Bisagra de cadera, no sentadilla.", "Codos cerca del torso.",
         "Apretá los omóplatos arriba.", "Volvé lento, sin soltar el peso de golpe."],
        "Espalda · Espalda alta · Bíceps",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Espalda #EspaldaAlta #RemoInclinado #TBarRow #BarraV #Biceps #Entrenamiento")}

save("lever-bent-over-row-with-v-bar", tb_scenes("lever-bent-over-row-with-v-bar"),
     {"pose": "PULL", "zoom": 1.05, "dy": 40}, YT49)
