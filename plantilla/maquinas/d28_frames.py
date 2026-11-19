# Dataset D52 Lever One Arm Lateral High Row: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.2, tb=1.4, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def oa_scenes(slug):
    s, S, J = load(slug)
    H0 = S(*J["START"]["W"]); H1 = S(*J["PULL"]["W"])
    SEAT = S(-310, -250); CHEST = S(-300, -420); FOOT = S(145, -80); PLATE = S(-520, -180)
    SH = S(*J["PULL"]["S"]); LAT = S(-340, -470); LEAN = S(*J["LEAN_BAD"]["S"])
    SHR = S(-350, -560); RND = S(-300, -500)
    return [
        hook("GIMNASIO · ESPALDA", ["REMO ALTO", "A UNA MANO"], "Un brazo por vez",
             "Remo alto a un brazo en palanca: tirá una manija desde arriba hasta el costado del torso, con el codo afuera.",
             [C("START"), seqloop("START", "PULL")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Manijas altas y pecho apoyado",
             "La máquina tiene asiento, almohadilla para el pecho, placa de pies, una manija alta por brazo y los discos atrás.",
             [C("START")], [ring(CHEST, 44, 0.8), lab((60, 1200), "PECHO APOYADO", "start", 0.8),
                            ring(H0, 42, 1.7), lab((985, 930), "MANIJA ALTA", "end", 1.7),
                            ring(SEAT, 44, 2.6), lab((60, 1320), "ASIENTO", "start", 2.6),
                            ring(PLATE, 36, 3.5), lab((60, 1410), "DISCOS", "start", 3.5)], 7.2),
        step("AJUSTE 1", ["ALTURA", "DEL ASIENTO"], "Pecho en la almohadilla",
             "Ajustá el asiento para que el pecho quede cerca de la almohadilla y la manija arranque a la altura de la cabeza.",
             [C("START")], [ring(CHEST, 46, 0.8), lab((60, CHEST[1] + 40), "ALTURA DEL PECHO", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["PIES Y", "AGARRE"], "Una mano por vez",
             "Poné los pies planos en la placa, elegí el peso y tomá la manija con una mano. La otra queda apoyada en la cadera.",
             [C("START")], [ring(FOOT, 42, 0.8), lab((985, 1280), "PLACA DE PIES", "end", 0.9),
                            ring(H0, 40, 2.0), lab((60, 900), "AGARRE A UNA MANO", "start", 2.0)], 7.0),
        step("POSICIÓN INICIAL", ["PECHO", "ARRIBA"], "Brazo extendido",
             "Sentate con la espalda recta y el pecho arriba. El brazo de trabajo arranca extendido y la otra mano descansa.",
             [C("START")], [ring(LAT, 54, 0.8), lab((60, LAT[1] - 50), "PECHO ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["TIRÁ AL", "COSTADO"], "Codo hacia atrás y afuera",
             "Paso uno. Tirá la manija hacia el costado del torso llevando el codo hacia atrás y afuera, sin rotar el tronco.",
             [C("START"), TO("PULL", 0.6, 1.0)],
             [arrow((H0[0] - 10, H0[1] + 10), (H1[0] - 10, H1[1] - 10), 0.8, 1.0, [-40, 30]),
              lab((60, H0[1] - 35), "TIRÁ AL COSTADO", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ", "EL OMÓPLATO"], "Pausa de un segundo",
             "Paso dos. Apretá el omóplato al final y hacé una pausa de un segundo con la manija al lado del torso.",
             [C("PULL"), TO("PULL", 0.2, 0.4)],
             [ring(SH, 50, 0.8), lab((985, 1080), "APRETÁ", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin soltar de golpe",
             "Paso tres. Volvé lento a la posición inicial con el brazo extendido, sin soltar el peso de golpe.",
             [C("PULL"), TO("START", 0.5, 1.2)],
             [arrow((H1[0] - 10, H1[1] - 10), (H0[0] - 10, H0[1] + 10), 0.8, 1.0, [40, -30]),
              lab((60, H0[1] - 25), "VOLVÉ LENTO", "start", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando tirás y tomá aire cuando volvés. El abdomen queda firme y la espalda quieta.",
             [C("START"), seqloop("START", "PULL", 1.0, 1.6, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ECHARSE", "ATRÁS"], "El tronco queda quieto",
             "Error: echarse atrás para tirar con el peso del cuerpo. El tronco queda quieto y la espalda apoyada.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.9)], [NO(1.4), ring(LEAN, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["SUBIR EL", "HOMBRO"], "Hombro abajo",
             "Error: subir el hombro y tirar con el cuello. El hombro queda abajo y el omóplato hace el trabajo.",
             [C("START"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(1.4), ring(SHR, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda para llegar más lejos. El pecho se queda arriba y la espalda recta.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4), ring(RND, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Una mano por vez", "Codo hacia atrás",
                                          "Omóplato junto", "Tronco quieto"],
             "Tips: una mano por vez, codo hacia atrás y afuera, omóplato junto y el tronco quieto.",
             [C("START"), seqloop("START", "PULL")]),
        keys("CLAVES", ["TÉCNICA"], ["Asiento y placa ajustados", "Una sola mano",
                                     "Sin rotar el tronco", "Pausa al final"],
             "Claves: asiento y placa ajustados, una sola mano, sin rotar el tronco y pausa al final.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 10–12"], "Un minuto de pausa",
             "Tres series de diez a doce por brazo, con un minuto de pausa. Subí peso cuando las doce salgan fáciles.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · VOLVÉ"], [C("START"), seqloop("START", "PULL")]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, volvé a la posición inicial sin soltar la manija de golpe y dejá que los discos bajen despacio.",
             [C("PULL"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN SOLTAR", "end", 1.0)], 6.5),
    ]


YT52 = {
    "titulo": "Lever One Arm Lateral High Row 🔥 Remo alto a una mano en palanca | Gimnasio",
    "tags": ["lever one arm lateral high row", "remo alto a una mano", "remo unilateral en palanca",
             "remo alto en máquina", "remo sentado a un brazo", "espalda alta", "dorsales",
             "deltoides posteriores", "máquinas de gimnasio", "gimnasio", "principiantes",
             "rutina de espalda"],
    "descripcion": yt_desc("Lever One Arm Lateral High Row",
        "remo alto a una mano en máquina de palanca",
        "espalda alta, dorsales y deltoides posteriores",
        "El remo alto a una mano te deja corregir diferencias entre lados: si tirás con impulso, subís el hombro o rotás el tronco, el trabajo se va al cuello y la espalda no se activa. La clave es llevar el codo atrás y afuera, con el tronco quieto.",
        ["Ajustá el asiento para que el pecho quede cerca de la almohadilla y la manija arranque a la altura de la cabeza.",
         "Poné los pies planos en la placa, elegí el peso y tomá la manija con una sola mano."],
        ["Sentate con la espalda recta y el pecho arriba, la otra mano apoyada en la cadera.",
         "Tomá la manija alta con una mano y arrancá con el brazo extendido.",
         "Tirá la manija hacia el costado del torso llevando el codo hacia atrás y afuera.",
         "Apretá el omóplato un segundo y volvé lento.",
         "Hacé todas las repeticiones de un lado y después cambiá de brazo."],
        ["Echarse atrás para tirar → el tronco queda quieto y la espalda apoyada.",
         "Subir el hombro → hombro abajo y omóplato haciendo el trabajo.",
         "Redondear la espalda → pecho arriba y espalda recta."],
        ["Una mano por vez, sin apurar el cambio de lado.", "Codo hacia atrás y afuera, no pegado al cuerpo.",
         "Apretá el omóplato al final del recorrido.", "Volvé lento, sin soltar el peso de golpe."],
        "Espalda · Espalda alta · Bíceps · Hombros",
        "3 series de 10–12 por brazo, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Espalda #EspaldaAlta #RemoAlto #MaquinaDePalanca #Dorsales #Entrenamiento")}

save("lever-one-arm-lateral-high-row", oa_scenes("lever-one-arm-lateral-high-row"),
     {"pose": "PULL", "zoom": 1.08, "dy": 70}, YT52)
