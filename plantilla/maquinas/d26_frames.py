# Dataset D50 Lever High Row: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.2, tb=1.4, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def hr_scenes(slug):
    s, S, J = load(slug)
    H0 = S(*J["START"]["W"]); H1 = S(*J["PULL"]["W"])
    SEAT = S(-310, -250); CHEST = S(-300, -420); FOOT = S(145, -80); PLATE = S(-520, -180)
    SH = S(*J["PULL"]["S"]); LAT = S(-340, -470); LEAN = S(*J["LEAN_BAD"]["S"])
    SHR = S(-350, -560); RND = S(-300, -500)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO", "ALTO"], "Manijas altas y anchas",
             "Remo alto sentado en máquina de palanca: tirá las dos manijas desde arriba hasta el pecho, con el pecho apoyado.",
             [C("START"), seqloop("START", "PULL")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Manijas altas y pecho apoyado",
             "La máquina tiene asiento, almohadilla para el pecho, placa de pies, dos manijas altas y los discos atrás.",
             [C("START")], [ring(CHEST, 44, 0.8), lab((60, 1200), "PECHO APOYADO", "start", 0.8),
                            ring(H0, 42, 1.7), lab((985, 930), "MANIJAS ALTAS", "end", 1.7),
                            ring(SEAT, 44, 2.6), lab((60, 1320), "ASIENTO", "start", 2.6),
                            ring(PLATE, 36, 3.5), lab((60, 1410), "DISCOS", "start", 3.5)], 7.2),
        step("AJUSTE 1", ["ALTURA", "DEL ASIENTO"], "Pecho en la almohadilla",
             "Ajustá el asiento para que el pecho quede apoyado en la almohadilla y las manijas arranquen a la altura de la cabeza.",
             [C("START")], [ring(CHEST, 46, 0.8), lab((60, CHEST[1] + 40), "ALTURA DEL PECHO", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["PIES Y", "AGARRE"], "Agarre prono ancho",
             "Poné los pies planos en la placa y tomá las manijas con agarre prono, un poco más separadas que los hombros.",
             [C("START")], [ring(FOOT, 42, 0.8), lab((985, 1280), "PLACA DE PIES", "end", 0.9),
                            ring(H0, 40, 2.0), lab((60, 900), "AGARRE ANCHO", "start", 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["PECHO", "ARRIBA"], "Brazos altos",
             "Sentate con la espalda recta, el pecho elevado y los hombros abajo. Las manijas arrancan altas y los brazos extendidos.",
             [C("START")], [ring(LAT, 54, 0.8), lab((60, LAT[1] - 50), "PECHO ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["TIRÁ", "HACIA EL PECHO"], "Codos hacia atrás",
             "Paso uno. Tirá las dos manijas hacia el pecho llevando los codos hacia atrás, sin mover el tronco.",
             [C("START"), TO("PULL", 0.6, 1.0)],
             [arrow((H0[0] - 10, H0[1] + 10), (H1[0] - 10, H1[1] - 10), 0.8, 1.0, [-40, 30]),
              lab((60, H0[1] - 35), "TIRÁ HACIA EL PECHO", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ LOS", "OMÓPLATOS"], "Pausa de un segundo",
             "Paso dos. Apretá los omóplatos al final del movimiento y hacé una pausa de un segundo.",
             [C("PULL"), TO("PULL", 0.2, 0.4)],
             [ring(SH, 50, 0.8), lab((985, 1080), "APRETÁ", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin perder el apoyo",
             "Paso tres. Volvé lento a la posición inicial, sin soltar el peso de golpe y sin despegar el pecho.",
             [C("PULL"), TO("START", 0.5, 1.2)],
             [arrow((H1[0] - 10, H1[1] - 10), (H0[0] - 10, H0[1] + 10), 0.8, 1.0, [40, -30]),
              lab((60, H0[1] - 25), "VOLVÉ LENTO", "start", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando tirás y tomá aire cuando volvés. El abdomen queda firme y el pecho apoyado.",
             [C("START"), seqloop("START", "PULL", 1.0, 1.6, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ECHARSE", "ATRÁS"], "El tronco queda quieto",
             "Error: echarse atrás para tirar con el peso del cuerpo. El tronco queda quieto y el pecho apoyado.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4, (540, 900)), ring(LEAN, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["SUBIR LOS", "HOMBROS"], "Hombros abajo",
             "Error: subir los hombros y tirar con el cuello. Los hombros quedan abajo y los omóplatos hacen el trabajo.",
             [C("START"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(1.4, (540, 900)), ring(SHR, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda para llegar más lejos. El pecho se queda arriba y la espalda recta.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4, (540, 900)), ring(RND, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pecho apoyado", "Codos hacia atrás",
                                          "Omóplatos juntos", "Volvé lento"],
             "Tips: pecho apoyado, codos hacia atrás, omóplatos juntos al final y volvé lento.",
             [C("START"), seqloop("START", "PULL")]),
        keys("CLAVES", ["TÉCNICA"], ["Asiento y placa ajustados", "Agarre prono ancho",
                                     "Sin impulso del tronco", "Pausa al final"],
             "Claves: asiento y placa ajustados, agarre prono ancho, sin impulso del tronco y pausa al final.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Un minuto de pausa",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · VOLVÉ"], [C("START"), seqloop("START", "PULL")]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, volvé a la posición inicial sin soltar las manijas de golpe y dejá que los discos bajen despacio.",
             [C("PULL"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN SOLTAR", "end", 1.0)], 6.5),
    ]


YT50 = {
    "titulo": "Lever High Row 🔥 Remo alto en palanca | Espalda alta",
    "tags": ["lever high row", "remo alto en máquina", "remo alto en palanca", "remo sentado",
             "espalda alta", "dorsales", "deltoides posteriores", "máquinas de gimnasio", "gimnasio",
             "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever High Row",
        "remo alto sentado en máquina de palanca",
        "espalda alta, dorsales y deltoides posteriores",
        "El remo alto arranca con las manijas arriba y anchas: si tirás con impulso o subís los hombros, el trabajo se va al cuello y los omóplatos no se juntan. La clave es llevar los codos atrás y bajar las manijas hasta el pecho.",
        ["Ajustá el asiento para que el pecho quede apoyado en la almohadilla y las manijas arranquen a la altura de la cabeza.",
         "Poné los pies planos en la placa y elegí un peso que puedas mover 10–12 veces."],
        ["Sentate con la espalda recta y el pecho apoyado en la almohadilla.",
         "Tomá las dos manijas altas con agarre prono, un poco más separadas que los hombros.",
         "Tirá las manijas hacia el pecho llevando los codos hacia atrás.",
         "Apretá los omóplatos un segundo y volvé lento.",
         "Mantené el pecho apoyado durante todo el recorrido."],
        ["Echarse atrás para tirar → el tronco queda quieto y el pecho apoyado.",
         "Subir los hombros → hombros abajo y omóplatos hacia atrás.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Pecho apoyado y mirada al frente.", "Codos hacia atrás, no hacia los costados.",
         "Apretá los omóplatos al final del recorrido.", "Volvé lento, sin soltar el peso de golpe."],
        "Espalda · Espalda alta · Deltoides posteriores",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Espalda #EspaldaAlta #RemoAlto #MaquinaDePalanca #Dorsales #Entrenamiento")}

save("lever-high-row", hr_scenes("lever-high-row"),
     {"pose": "PULL", "zoom": 1.08, "dy": 70}, YT50)
