# Dataset D48 Lever Alternating Narrow Grip Seated Row: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def alt_loop(at=0.4):
    return {"seq": [["PULL_N", 0.95], ["START", 0.65], ["PULL_F", 0.95], ["START", 0.65]], "at": at, "until": "end"}


def seqloop(a, b, ta=1.1, tb=1.8, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def rw_scenes(slug):
    s, S, J = load(slug)
    H0 = S(*J["START"]["W"]); H1 = S(*J["PULL_N"]["W"])
    SEAT = S(-310, -250); CHEST = S(-280, -430); FOOT = S(160, -80); PLATE = S(-500, -180)
    SH = S(*J["PULL_N"]["S"]); LAT = S(-340, -470); LEAN = S(*J["LEAN_BAD"]["S"])
    SHR = S(-380, -490); RND = S(-340, -480)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO SENTADO", "ALTERNADO"], "Agarre estrecho en palanca",
             "Remo sentado alternado en máquina de palanca: tirá una manija por vez, con agarre estrecho y el pecho apoyado.",
             [C("START"), alt_loop()]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Pecho, manijas y discos",
             "La máquina tiene asiento, almohadilla para el pecho, placa de pies, dos manijas y los discos atrás.",
             [C("START")], [ring(CHEST, 44, 0.8), lab((60, 1080), "PECHO APOYADO", "start", 0.8),
                            ring(H0, 42, 1.7), lab((985, 1010), "MANIJAS", "end", 1.7),
                            ring(SEAT, 44, 2.6), lab((60, 1340), "ASIENTO", "start", 2.6),
                            ring(PLATE, 36, 3.5), lab((60, 1430), "DISCOS", "start", 3.5)], 7.2),
        step("AJUSTE 1", ["LA", "ALTURA"], "Pecho en la almohadilla",
             "Ajustá el asiento para que el pecho quede apoyado en la almohadilla y las manijas a la altura del pecho.",
             [C("START")], [ring(CHEST, 46, 0.8), lab((60, CHEST[1] + 40), "ALTURA DEL PECHO", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["PIES Y", "AGARRE"], "Agarre estrecho",
             "Poné los pies planos en la placa y tomá las manijas con un agarre estrecho, las palmas enfrentadas.",
             [C("START")], [ring(FOOT, 42, 0.8), lab((985, 1360), "PLACA DE PIES", "end", 0.9),
                            ring(H0, 40, 2.0), lab((60, 1050), "AGARRE ESTRECHO", "start", 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["PECHO", "ARRIBA"], "Hombros atrás",
             "Sentate con la espalda recta, el pecho elevado y los hombros hacia atrás. Los brazos quedan extendidos.",
             [C("START")], [ring(LAT, 54, 0.8), lab((60, LAT[1] - 50), "PECHO ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["TIRÁ UNA", "MANIJA"], "La otra queda quieta",
             "Paso uno. Tirá de una manija hacia el torso mientras la otra queda inmóvil, sin girar el tronco.",
             [C("START"), TO("PULL_N", 0.6, 1.0)],
             [arrow((H0[0] + 10, H0[1] - 20), (H1[0] + 10, H1[1] - 30), 0.8, 1.0, [30, -30]),
              lab((60, H0[1] - 40), "TIRÁ UN LADO", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ LOS", "OMÓPLATOS"], "Pausa de un segundo",
             "Paso dos. Apretá los omóplatos al final del movimiento y hacé una pausa de un segundo.",
             [C("PULL_N"), TO("PULL_N", 0.2, 0.4)],
             [ring(LAT, 50, 0.8), lab((985, 1120), "APRETÁ", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ Y", "CAMBIÁ"], "Sin soltar de golpe",
             "Paso tres. Volvé lento a la posición inicial y repetí con la otra mano. Alterná los lados.",
             [C("PULL_N"), TO("START", 0.5, 0.5), TO("PULL_F", 1.0, 0.8)],
             [arrow((H1[0] + 10, H1[1] - 30), (H0[0] + 10, H0[1] - 20), 0.8, 0.8, [30, 30]),
              lab((60, H0[1] - 30), "VOLVÉ Y CAMBIÁ", "start", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando tirás y tomá aire cuando volvés. El abdomen queda firme y el tronco quieto.",
             [C("START"), seqloop("PULL_N", "START", 1.0, 1.8, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ECHARSE", "ATRÁS"], "El tronco queda quieto",
             "Error: echarse atrás para tirar con el peso del cuerpo. El tronco queda quieto y el pecho apoyado.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4, (540, 930)), ring(LEAN, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["SUBIR LOS", "HOMBROS"], "Hombros abajo",
             "Error: subir los hombros y tirar con el cuello. Los hombros quedan abajo y los omóplatos hacen el trabajo.",
             [C("START"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(1.4, (540, 930)), ring(SHR, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda para llegar más lejos. El pecho se queda arriba y la espalda recta.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4, (540, 930)), ring(RND, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pecho apoyado", "Una manija por vez",
                                          "Omóplatos juntos", "Volvé lento"],
             "Tips: pecho apoyado, una manija por vez, omóplatos juntos al final y volvé lento.",
             [C("START"), alt_loop()]),
        keys("CLAVES", ["TÉCNICA"], ["Asiento y placa ajustados", "Agarre estrecho",
                                     "Sin impulso del tronco", "Pausa al final"],
             "Claves: asiento y placa ajustados, agarre estrecho, sin impulso del tronco y pausa al final.",
             [{"cut": "PULL_N", "at": 0.1}]),
        reps(["3 X 10–12"], "Por lado, un minuto de pausa",
             "Tres series de diez a doce repeticiones por lado, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · VOLVÉ"], [C("START"), alt_loop()]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, volvé a la posición inicial sin soltar las manijas de golpe y dejá que los discos bajen despacio.",
             [C("PULL_N"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN SOLTAR", "end", 1.0)], 6.5),
    ]


YT48 = {
    "titulo": "Lever Alternating Narrow Grip Seated Row 🔥 Remo alternado en palanca | Espalda",
    "tags": ["lever alternating narrow grip seated row", "remo sentado alternado", "remo en máquina de palanca",
             "agarre estrecho", "espalda alta", "dorsales", "máquinas de gimnasio", "gimnasio",
             "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Alternating Narrow Grip Seated Row",
        "remo sentado alternado con agarre estrecho en máquina de palanca",
        "espalda alta y bíceps, con el pecho apoyado",
        "El remo alternado trabaja una mitad de la espalda por vez: si girás el tronco o usás impulso, el trabajo se reparte y los omóplatos no se juntan. La clave es tirar de una manija, dejar la otra quieta y volver lento.",
        ["Ajustá el asiento para que el pecho quede apoyado en la almohadilla y las manijas a la altura del pecho.",
         "Poné los pies planos en la placa y elegí un peso que puedas mover 10–12 veces por lado."],
        ["Sentate con la espalda recta y el pecho apoyado en la almohadilla.",
         "Tomá las dos manijas con agarre estrecho, las palmas enfrentadas.",
         "Tirá de una manija hacia el torso mientras la otra queda quieta.",
         "Apretá los omóplatos un segundo y volvé lento.",
         "Alterná los lados en cada repetición."],
        ["Echarse atrás para tirar → el tronco queda quieto y el pecho apoyado.",
         "Subir los hombros → hombros abajo y omóplatos hacia atrás.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Pecho apoyado y mirada al frente.", "Una manija por vez: la otra no se mueve.",
         "Apretá los omóplatos al final del recorrido.", "Volvé lento, sin soltar el peso de golpe."],
        "Espalda · Espalda alta · Bíceps",
        "3 series de 10–12 repeticiones por lado, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Espalda #EspaldaAlta #RemoSentado #MaquinaDePalanca #Biceps #Entrenamiento")}

save("lever-alternating-narrow-grip-seated-row", rw_scenes("lever-alternating-narrow-grip-seated-row"),
     {"pose": "PULL_N", "zoom": 1.1, "dy": 100}, YT48)
