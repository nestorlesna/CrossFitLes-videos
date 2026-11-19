# Dataset D55 Lever Seated Row: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.2, tb=1.4, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def sr_scenes(slug):
    s, S, J = load(slug)
    H0 = S(*J["START"]["W"]); H1 = S(*J["PULL"]["W"])
    PAD = S(-276, -470); CHEST = S(*J["START"]["S"]); SEAT = S(-310, -258)
    PLATE = S(-540, -180); FOOT = S(140, -60); SH = S(*J["PULL"]["S"])
    LEAN = S(-420, -430); SHR = S(*J["SHRUG_BAD"]["S"]); RND = S(-300, -470)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO", "SENTADO"], "Pecho apoyado y tirón al torso",
             "Remo sentado en palanca: sentate con el pecho apoyado y tirá las manijas al torso juntando los omóplatos.",
             [C("START"), seqloop("START", "PULL")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Pecho apoyado y manijas al frente",
             "La máquina tiene asiento, almohadilla para el pecho, placa de pies, dos manijas y los discos atrás.",
             [C("START")], [ring(PAD, 44, 0.8), lab((60, PAD[1] - 40), "ALMOHADILLA", "start", 0.8),
                            ring(H0, 42, 1.7), lab((985, H0[1] - 50), "MANIJAS", "end", 1.7),
                            ring(SEAT, 44, 2.6), lab((60, SEAT[1] - 30), "ASIENTO", "start", 2.6),
                            ring(PLATE, 36, 3.5), lab((60, PLATE[1] - 30), "DISCOS", "start", 3.5)], 7.2),
        step("AJUSTE 1", ["ALTURA DEL", "ASIENTO"], "Pecho en la almohadilla",
             "Ajustá el asiento para que el pecho quede apoyado en la almohadilla y las manijas a la altura del pecho.",
             [C("START")], [ring(SEAT, 44, 0.8), lab((60, SEAT[1] + 40), "ALTURA DEL ASIENTO", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["PIES Y", "AGARRE"], "Agarre prono",
             "Apoyá los pies en la placa y tomá las manijas con agarre prono, las manos a la altura de los hombros.",
             [C("START")], [ring(FOOT, 42, 0.8), lab((985, FOOT[1] - 60), "PLACA DE PIES", "end", 0.9),
                            ring(H0, 40, 2.0), lab((60, H0[1] - 40), "AGARRE PRONO", "start", 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["PECHO", "ARRIBA"], "Hombros atrás",
             "Sentate con el pecho arriba, los hombros atrás y los brazos extendidos al frente.",
             [C("START")], [ring(CHEST, 54, 0.8), lab((60, CHEST[1] - 50), "PECHO ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["TIRÁ AL", "TORSO"], "Codos cerca del cuerpo",
             "Paso uno. Tirá las dos manijas hacia el torso llevando los codos cerca del cuerpo, sin mover el tronco.",
             [C("START"), TO("PULL", 0.6, 1.0)],
             [arrow((H0[0] + 20, H0[1] - 30), (H1[0] + 20, H1[1] - 30), 0.8, 1.0, [34, -34]),
              lab((60, H0[1] - 40), "TIRÁ AL TORSO", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ LOS", "OMÓPLATOS"], "Pausa de un segundo",
             "Paso dos. Apretá los omóplatos al final del movimiento y hacé una pausa de un segundo.",
             [C("PULL"), TO("PULL", 0.2, 0.4)],
             [ring(SH, 50, 0.8), lab((985, SH[1] - 40), "APRETÁ", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin soltar de golpe",
             "Paso tres. Volvé lento a la posición inicial, sin soltar el peso de golpe y sin despegar el pecho.",
             [C("PULL"), TO("START", 0.5, 1.2)],
             [arrow((H1[0] + 20, H1[1] - 30), (H0[0] + 20, H0[1] - 30), 0.8, 1.0, [34, 34]),
              lab((60, H0[1] - 30), "VOLVÉ LENTO", "start", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando tirás y tomá aire cuando volvés. El abdomen queda firme y el tronco quieto.",
             [C("START"), seqloop("START", "PULL", 1.0, 1.8, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ECHARSE", "ATRÁS"], "El tronco queda quieto",
             "Error: echarse atrás para tirar con el peso del cuerpo. El tronco queda quieto y el pecho apoyado.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4), ring(LEAN, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["SUBIR LOS", "HOMBROS"], "Hombros abajo",
             "Error: subir los hombros y tirar con el cuello. Los hombros quedan abajo y los omóplatos hacen el trabajo.",
             [C("START"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(1.4), ring(SHR, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda para llegar más lejos. El pecho se queda arriba y la espalda recta.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4), ring(RND, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pecho apoyado", "Agarre prono",
                                          "Codos cerca", "Volvé lento"],
             "Tips: pecho apoyado, agarre prono, codos cerca del cuerpo y volvé lento.",
             [C("START"), seqloop("START", "PULL")]),
        keys("CLAVES", ["TÉCNICA"], ["Asiento y placa ajustados", "Manos a la altura del pecho",
                                     "Sin impulso del tronco", "Pausa al final"],
             "Claves: asiento y placa ajustados, manos a la altura del pecho, sin impulso del tronco y pausa al final.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Un minuto de pausa",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · VOLVÉ"], [C("START"), seqloop("START", "PULL")]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, volvé a la posición inicial sin soltar las manijas de golpe y dejá que los discos bajen despacio.",
             [C("PULL"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN SOLTAR", "end", 1.0)], 6.5),
    ]


YT55 = {
    "titulo": "Lever Seated Row 🔥 Remo sentado en palanca | Gimnasio",
    "tags": ["lever seated row", "remo sentado", "remo en máquina de palanca", "remo sentado en palanca",
             "remo con pecho apoyado", "espalda alta", "dorsales", "bíceps",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Seated Row",
        "remo sentado en máquina de palanca con el pecho apoyado",
        "espalda alta, dorsales y bíceps",
        "El pecho apoyado saca el impulso del tronco y deja que los omóplatos hagan el trabajo. Si te echás atrás, subís los hombros o redondeás la espalda, el peso se reparte y el dorsal no se activa. La clave es tirar con los codos cerca y volver lento.",
        ["Ajustá el asiento para que el pecho quede apoyado en la almohadilla y las manijas a la altura del pecho.",
         "Apoyá los pies en la placa y elegí un peso que puedas mover 10–12 veces."],
        ["Sentate con el pecho apoyado en la almohadilla y los pies en la placa.",
         "Tomá las dos manijas con agarre prono, las manos a la altura de los hombros.",
         "Tirá las manijas hacia el torso llevando los codos cerca del cuerpo.",
         "Apretá los omóplatos un segundo y volvé lento.",
         "Mantené el pecho apoyado durante todo el recorrido."],
        ["Echarse atrás para tirar → el tronco queda quieto y el pecho apoyado.",
         "Subir los hombros → hombros abajo y omóplatos hacia atrás.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Pecho apoyado y mirada al frente.", "Agarre prono durante todo el recorrido.",
         "Apretá los omóplatos al final.", "Volvé lento, sin soltar el peso de golpe."],
        "Espalda → Espalda alta → Bíceps → Antebrazos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Espalda #EspaldaAlta #RemoSentado #PechoApoyado #MaquinaDePalanca #Biceps #Entrenamiento")}

save("lever-seated-row", sr_scenes("lever-seated-row"),
     {"pose": "PULL", "zoom": 1.08, "dy": 70}, YT55)
