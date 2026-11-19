# Dataset D58 Lever Unilateral Row: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.2, tb=1.4, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def un_scenes(slug):
    s, S, J = load(slug)
    H0 = S(*J["START"]["W"]); H1 = S(*J["PULL"]["W"])
    PAD = S(-290, -470); CHEST = S(-292, -470); SEAT = S(-310, -258)
    PLATE = S(-520, -180); FOOT = S(120, -60); SH = S(-340, -520)
    LEAN = S(-250, -409); SHR = S(-340, -520); RND = S(-294, -416)
    REST = S(-370, -300)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO", "UNILATERAL"], "Un brazo a la vez",
             "Remo unilateral en palanca: tirá una manija al costado del torso con el codo atrás, sin rotar el tronco.",
             [C("START"), seqloop("START", "PULL")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Una manija por brazo",
             "La máquina tiene asiento, almohadilla para el pecho, placa de pies, dos manijas independientes y los discos atrás.",
             [C("START")], [ring(PAD, 44, 0.8), lab((60, PAD[1] - 40), "ALMOHADILLA", "start", 0.8),
                            ring(H0, 42, 1.7), lab((985, H0[1] - 40), "MANIJA", "end", 1.7),
                            ring(SEAT, 44, 2.6), lab((60, SEAT[1] - 20), "ASIENTO", "start", 2.6),
                            ring(PLATE, 36, 3.5), lab((60, PLATE[1] - 30), "DISCOS", "start", 3.5)], 7.2),
        step("AJUSTE 1", ["ALTURA DEL", "ASIENTO"], "Pecho en la almohadilla",
             "Ajustá el asiento para que el pecho quede apoyado y la manija a la altura del torso.",
             [C("START")], [ring(SEAT, 44, 0.8), lab((60, SEAT[1] + 40), "ALTURA DEL ASIENTO", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["PIES Y", "MANO LIBRE"], "La otra mano en la cadera",
             "Apoyá los pies en la placa y dejá la mano que no trabaja apoyada en la cadera o en el muslo.",
             [C("START")], [ring(FOOT, 42, 0.8), lab((985, FOOT[1] - 130), "PLACA DE PIES", "end", 0.9),
                            ring(REST, 34, 2.0), lab((60, REST[1] + 40), "MANO LIBRE", "start", 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["PECHO", "APOYADO"], "Un solo brazo",
             "Arrancá con el pecho apoyado, la espalda recta y el brazo de trabajo extendido hacia la manija.",
             [C("START")], [ring(CHEST, 54, 0.8), lab((60, CHEST[1] - 50), "PECHO APOYADO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["TIRÁ AL", "COSTADO"], "Codo hacia atrás",
             "Paso uno. Tirá la manija al costado del torso llevando el codo hacia atrás y afuera, sin rotar el tronco.",
             [C("START"), TO("PULL", 0.6, 1.0)],
             [arrow((H0[0] + 10, H0[1] - 20), (H1[0] + 10, H1[1] - 30), 0.8, 1.0, [34, -30]),
              lab((60, H0[1] - 40), "TIRÁ AL COSTADO", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["JUNTÁ EL", "OMÓPLATO"], "Pausa de un segundo",
             "Paso dos. Juntá el omóplato del lado que trabaja y hacé una pausa de un segundo.",
             [C("PULL"), TO("PULL", 0.2, 0.4)],
             [ring(SH, 50, 0.8), lab((985, SH[1] + 40), "JUNTÁ", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin rotar el tronco",
             "Paso tres. Volvé lento a la posición inicial, sin rotar el tronco y sin despegar el pecho.",
             [C("PULL"), TO("START", 0.5, 1.2)],
             [arrow((H1[0] + 10, H1[1] - 30), (H0[0] + 10, H0[1] - 20), 0.8, 1.0, [34, 30]),
              lab((60, H0[1] - 30), "VOLVÉ LENTO", "start", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando tirás y tomá aire cuando volvés. El abdomen queda firme y el tronco quieto.",
             [C("START"), seqloop("START", "PULL", 1.0, 1.8, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ECHARSE", "ATRÁS"], "El tronco queda quieto",
             "Error: echarse atrás para tirar con el peso del cuerpo. El tronco queda quieto y el pecho apoyado.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4), ring(LEAN, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["SUBIR EL", "HOMBRO"], "Hombro abajo",
             "Error: subir el hombro y tirar con el cuello. El hombro queda abajo y el omóplato hace el trabajo.",
             [C("START"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(1.4), ring(SHR, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda para llegar más lejos. El pecho se queda arriba y la espalda recta.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4), ring(RND, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pecho apoyado", "Codo atrás",
                                         "Sin rotar el tronco", "Cambiá de brazo"],
             "Tips: pecho apoyado, codo hacia atrás, sin rotar el tronco y cambiá de brazo al terminar la serie.",
             [C("START"), seqloop("START", "PULL")]),
        keys("CLAVES", ["TÉCNICA"], ["Manija a la altura del torso", "Mano libre apoyada",
                                     "Omóplato hacia atrás", "Mismo peso por lado"],
             "Claves: manija a la altura del torso, mano libre apoyada, omóplato hacia atrás y el mismo peso por lado.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Por brazo",
             "Tres series de diez a doce repeticiones por brazo, con un minuto de pausa. Empezá por el lado más débil.",
             ["1 · TIRÁ", "2 · JUNTÁ", "3 · VOLVÉ"], [C("START"), seqloop("START", "PULL")]),
        step("AL TERMINAR", ["CAMBIÁ", "DE BRAZO"], "Sin apurarse",
             "Al terminar la serie, soltá la manija despacio y cambiá de brazo. Descansá un minuto entre lados.",
             [C("PULL"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN SOLTAR", "end", 1.0)], 6.5),
    ]


YT58 = {
    "titulo": "Lever Unilateral Row 🔥 Remo unilateral en palanca | Gimnasio",
    "tags": ["lever unilateral row", "remo unilateral", "remo a una mano", "remo en máquina de palanca",
             "remo con pecho apoyado", "espalda alta", "dorsales", "bíceps",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Unilateral Row",
        "remo unilateral en máquina de palanca con el pecho apoyado",
        "dorsales, espalda alta y bíceps",
        "Trabajar un brazo por vez deja corregir diferencias de fuerza y sentir mejor el omóplato. Si te echás atrás, subís el hombro o redondeás la espalda, el peso se reparte y el dorsal no se activa. La clave es tirar con el codo atrás y volver lento, sin rotar el tronco.",
        ["Ajustá el asiento para que el pecho quede apoyado y la manija a la altura del torso.",
         "Apoyá los pies en la placa y elegí un peso que puedas mover 10–12 veces por brazo."],
        ["Sentate con el pecho apoyado en la almohadilla y los pies en la placa.",
         "Tomá una sola manija con agarre prono y dejá la otra mano apoyada en la cadera.",
         "Tirá la manija al costado del torso con el codo hacia atrás.",
         "Juntá el omóplato un segundo y volvé lento.",
         "Completá la serie y cambiá de brazo."],
        ["Echarse atrás para tirar → el tronco queda quieto y el pecho apoyado.",
         "Subir el hombro → hombro abajo y omóplato hacia atrás.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Pecho apoyado y mirada al frente.", "Mano libre apoyada en la cadera.",
         "Juntá el omóplato al final.", "Volvé lento, sin soltar el peso de golpe."],
        "Espalda → Dorsales → Espalda alta → Bíceps",
        "3 series de 10–12 repeticiones por brazo, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Espalda #Dorsales #RemoUnilateral #PechoApoyado #MaquinaDePalanca #Biceps #Entrenamiento")}

save("lever-unilateral-row", un_scenes("lever-unilateral-row"),
     {"pose": "PULL", "zoom": 1.08, "dy": 70}, YT58)
