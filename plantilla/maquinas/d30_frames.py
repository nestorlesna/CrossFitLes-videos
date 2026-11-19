# Dataset D54 Lever Reverse T-bar Row: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.2, tb=1.4, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def tb_scenes(slug):
    s, S, J = load(slug)
    H0 = S(*J["START"]["W"]); H1 = S(*J["PULL"]["W"])
    PAD = S(-186, -470); CHEST = S(*J["START"]["S"]); HEAD = S(*J["START"]["N"])
    PLATE = S(114, -238); PIVOT = S(-120, 8); ANK = S(60, -6)
    LCHEST = S(-30, -519); SHR = S(*J["SHRUG_BAD"]["S"]); RND = S(25, -446)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO T", "INVERTIDO"], "Pecho apoyado, tirón al abdomen",
             "Remo T invertido con pecho apoyado: tirá la manija hacia el abdomen juntando los omóplatos.",
             [C("START"), seqloop("START", "PULL")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Pecho apoyado y palanca al piso",
             "La máquina tiene una almohadilla para el pecho, una manija en V, los discos sobre la palanca y una base firme en el piso.",
             [C("START")], [ring(PAD, 44, 0.8), lab((60, PAD[1] - 40), "ALMOHADILLA", "start", 0.8),
                            ring(H0, 42, 1.7), lab((60, 1170), "MANIJA EN V", "start", 1.7),
                            ring(PLATE, 40, 2.6), lab((60, 1310), "DISCOS", "start", 2.6),
                            ring(PIVOT, 34, 3.5), lab((60, PIVOT[1] - 40), "PALANCA", "start", 3.5)], 7.2),
        step("AJUSTE 1", ["ALTURA DE", "LA ALMOHADILLA"], "A la altura del esternón",
             "Ajustá la almohadilla a la altura del esternón: el pecho se apoya sin arquear la espalda.",
             [C("START")], [ring(PAD, 46, 0.8), lab((60, PAD[1] + 40), "ALTURA DEL PECHO", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["PIES Y", "AGARRE"], "Agarre neutro",
             "Apoyá los pies firmes y tomá la manija con las dos manos, las palmas enfrentadas y los brazos extendidos.",
             [C("START")], [ring(ANK, 40, 0.8), lab((985, ANK[1] - 80), "PIES FIRMES", "end", 0.9),
                            ring(H0, 40, 2.0), lab((60, H0[1] + 60), "AGARRE NEUTRO", "start", 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["PECHO", "APOYADO"], "Espalda recta",
             "Arrancá con el pecho apoyado, la espalda recta y los brazos extendidos hacia la manija.",
             [C("START")], [ring(CHEST, 54, 0.8), lab((60, CHEST[1] - 50), "PECHO APOYADO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["TIRÁ AL", "ABDOMEN"], "Codos cerca del cuerpo",
             "Paso uno. Tirá la manija hacia el abdomen llevando los codos cerca del cuerpo, sin despegar el pecho.",
             [C("START"), TO("PULL", 0.6, 1.0)],
             [arrow((H0[0] + 8, H0[1] - 12), (H1[0] + 8, H1[1] - 24), 0.8, 1.0, [34, -26]),
              lab((60, H0[1] - 30), "TIRÁ AL ABDOMEN", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ LOS", "OMÓPLATOS"], "Pausa de un segundo",
             "Paso dos. Apretá los omóplatos al final del movimiento y hacé una pausa de un segundo.",
             [C("PULL"), TO("PULL", 0.2, 0.4)],
             [ring(SHR, 50, 0.8), lab((985, SHR[1] + 40), "APRETÁ", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin soltar de golpe",
             "Paso tres. Volvé lento a la posición inicial, sin soltar el peso de golpe y sin despegar el pecho.",
             [C("PULL"), TO("START", 0.5, 1.2)],
             [arrow((H1[0] + 8, H1[1] - 24), (H0[0] + 8, H0[1] - 12), 0.8, 1.0, [34, 26]),
              lab((60, H0[1] - 20), "VOLVÉ LENTO", "start", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando tirás y tomá aire cuando volvés. El abdomen queda firme y el pecho apoyado.",
             [C("START"), seqloop("START", "PULL", 1.0, 1.8, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["LEVANTAR", "EL PECHO"], "El pecho no se despega",
             "Error: levantarse y despegar el pecho de la almohadilla. El pecho queda apoyado y el tronco quieto.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4), ring(LCHEST, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["SUBIR LOS", "HOMBROS"], "Hombros abajo",
             "Error: subir los hombros y tirar con el cuello. Los hombros quedan abajo y los omóplatos hacen el trabajo.",
             [C("START"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(1.4), ring(SHR, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda para llegar más lejos. El pecho se queda arriba y la espalda recta.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4), ring(RND, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pecho apoyado", "Agarre neutro",
                                          "Codos cerca", "Volvé lento"],
             "Tips: pecho apoyado, agarre neutro, codos cerca del cuerpo y volvé lento.",
             [C("START"), seqloop("START", "PULL")]),
        keys("CLAVES", ["TÉCNICA"], ["Almohadilla al esternón", "Pies firmes",
                                     "Sin impulso del tronco", "Pausa al final"],
             "Claves: almohadilla a la altura del esternón, pies firmes, sin impulso del tronco y pausa al final.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Un minuto de pausa",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · VOLVÉ"], [C("START"), seqloop("START", "PULL")]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, volvé a la posición inicial sin soltar la manija de golpe y dejá que los discos bajen despacio.",
             [C("PULL"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN SOLTAR", "end", 1.0)], 6.5),
    ]


YT54 = {
    "titulo": "Lever Reverse T-bar Row 🔥 Remo T invertido con pecho apoyado | Gimnasio",
    "tags": ["lever reverse t bar row", "remo t invertido", "remo t con pecho apoyado",
             "remo en máquina de palanca", "remo con pecho apoyado", "espalda alta", "dorsales", "bíceps",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Reverse T-bar Row",
        "remo T invertido en máquina de palanca con el pecho apoyado",
        "espalda alta, dorsales y bíceps",
        "El pecho apoyado saca el impulso del tronco y deja que los omóplatos hagan el trabajo. Si te levantás, subís los hombros o redondeás la espalda, el peso se reparte y el dorsal no se activa. La clave es tirar con los codos cerca y volver lento.",
        ["Ajustá la almohadilla a la altura del esternón, con el pecho apoyado sin arquear la espalda.",
         "Apoyá los pies firmes y elegí un peso que puedas mover 10–12 veces."],
        ["Parate inclinado sobre la máquina con el pecho apoyado en la almohadilla.",
         "Tomá la manija con las dos manos y agarre neutro, las palmas enfrentadas.",
         "Tirá la manija hacia el abdomen llevando los codos cerca del cuerpo.",
         "Apretá los omóplatos un segundo y volvé lento.",
         "Mantené el pecho apoyado durante todo el recorrido."],
        ["Levantar el pecho de la almohadilla → el tronco queda quieto y el pecho apoyado.",
         "Subir los hombros → hombros abajo y omóplatos hacia atrás.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Pecho apoyado y mirada al frente.", "Agarre neutro durante todo el recorrido.",
         "Apretá los omóplatos al final.", "Volvé lento, sin soltar el peso de golpe."],
        "Espalda → Espalda alta → Bíceps → Antebrazos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Espalda #EspaldaAlta #RemoT #PechoApoyado #MaquinaDePalanca #Biceps #Entrenamiento")}

save("lever-reverse-t-bar-row", tb_scenes("lever-reverse-t-bar-row"),
     {"pose": "PULL", "zoom": 1.08, "dy": 70}, YT54)
