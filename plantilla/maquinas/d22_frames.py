# Dataset D43 Lever Hip Extension v. 2 y D44 Lever Kneeling Twist: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}
KTW = lambda at=0.9, dur=2.6, ang=26, label="ROTÁ EL TORSO": {"mode": "ktw", "angle": ang, "at": at, "dur": dur, "label": label}


def pad(J, k):
    j = J[k]
    H, K = j["H"], j["K"]
    return (H[0] + (K[0] - H[0]) * 0.72, H[1] + (K[1] - H[1]) * 0.72, K)


def he_scenes(slug):
    s, S, J = load(slug)
    P_ST = pad(J, "START"); P_TOP = pad(J, "TOP")
    PAD_ST, PAD_TOP = S(*P_ST[:2]), S(*P_TOP[:2])
    K_ST, K_TOP = S(*P_ST[2]), S(*P_TOP[2])
    SEAT = S(-260, -520); BACK = S(-330, -700); HND = S(*J["START"]["W"])
    HIP = S(*J["START"]["H"]); HIP_B = S(*J["HIP_BAD"]["H"])
    SH_B = S(*J["LEAN_BAD"]["S"]); PIN = S(-569, -155)
    SW_PAD = S(*pad(J, "SWING_BAD")[:2])
    L_EM = (60, HIP[1] - 100); L_BAJ = (60, HIP[1] - 40)
    return [
        hook("GIMNASIO · GLÚTEOS", ["EXTENSIÓN", "DE CADERA"], "En máquina de palanca",
             "Lever Hip Extension: extensión de cadera en máquina. Empujás el muslo atrás y trabajás glúteos e isquios.",
             [C("START"), seqloop("TOP", "START", 1.0, 1.7, 0.4)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Almohadilla, asiento y pila",
             "La máquina tiene una almohadilla detrás del muslo, un asiento con respaldo y la pila de peso.",
             [C("START")], [ring(PAD_ST, 54, 0.8), lab((985, PAD_ST[1] + 40), "ALMOHADILLA", "end", 0.8),
                            ring(SEAT, 44, 1.8), lab((985, SEAT[1] - 90), "ASIENTO", "end", 1.8),
                            ring(PIN, 28, 2.8), lab((60, PIN[1] + 30), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Cadera a la altura del eje",
             "Ajustá el asiento para que la cadera quede a la altura del eje de la palanca.",
             [C("START")], [ring(HIP, 46, 0.8), lab((60, HIP[1] - 40), "EJE", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["LA", "ALMOHADILLA"], "Detrás del muslo",
             "La almohadilla va detrás del muslo, justo arriba de la rodilla. Que no te empuje el hueso.",
             [C("START")], [ring(PAD_ST, 54, 0.8), lab((985, PAD_ST[1] + 40), "ALMOHADILLA", "end", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "APOYADA"], "Manos en las manijas",
             "Sentate con la espalda apoyada y las manos en las manijas. Los pies quedan libres, sin empujar.",
             [C("START")], [ring(BACK, 60, 0.8), lab((60, BACK[1] + 80), "RESPALDO", "start", 1.0),
                            ring(HND, 30, 1.8), lab((985, HND[1] + 40), "MANIJAS", "end", 1.8)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "CON EL GLÚTEO"], "El muslo baja y atrás",
             "Paso uno. Empujá con el glúteo y el isquio: el muslo baja y atrás, la espalda no se mueve.",
             [C("START"), TO("MID", 0.6, 0.9)],
             [arrow((940, PAD_ST[1] - 20), (PAD_TOP[0] + 80, PAD_TOP[1] + 40), 0.8, 1.0, [50, 0]), lab(L_EM, "EMPUJÁ", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["LLEGÁ", "ARRIBA"], "Apretá el glúteo",
             "Paso dos. Llegá arriba sin arquear la espalda y apretá el glúteo un segundo.",
             [C("MID"), TO("TOP", 0.6, 0.9)],
             [ring(PAD_TOP, 54, 0.8), lab((60, PAD_TOP[1] - 30), "APRETÁ", "start", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLADO"], "Sin que pegue abajo",
             "Paso tres. Volvé bajando controlado, sin dejar que la pila pegue abajo.",
             [C("TOP"), TO("MID", 0.6, 1.0), TO("START", 0.5, 1.4)],
             [arrow((PAD_TOP[0] + 80, PAD_TOP[1] + 40), (940, PAD_ST[1] - 20), 1.0, 1.0, [50, 0]), lab(L_BAJ, "BAJÁ CONTROLADO", "start", 1.2)], 6.8, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al empujar",
             "Tomá aire al bajar y soltalo al empujar. El abdomen queda firme todo el tiempo.",
             [C("START"), seqloop("TOP", "START", 1.0, 1.8, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["TIRAR CON", "LA ESPALDA"], "Espalda en el respaldo",
             "Error: despegar la espalda del respaldo para empujar con la zona lumbar.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.8)], [NO(), ring(SH_B, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["LEVANTAR", "LA CADERA"], "Cadera pegada al asiento",
             "Error: levantar la cadera del asiento y buscar impulso con el tronco.",
             [C("START"), TO("HIP_BAD", 0.5, 0.8)], [NO(), ring(HIP_B, 44, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REBOTAR", "ABAJO"], "Bajada lenta",
             "Error: rebotar abajo y soltar el peso de golpe. Frená el retorno.",
             [C("START"), TO("SWING_BAD", 0.5, 0.8)], [NO(), ring(SW_PAD, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Cadera en el eje", "Espalda en el respaldo",
                                          "Empujá con el glúteo", "Bajada lenta"],
             "Tips: cadera a la altura del eje, espalda en el respaldo, empujá con el glúteo y bajá lento.",
             [C("START"), seqloop("TOP", "START", 1.0, 1.7, 0.4)]),
        keys("CLAVES", ["TÉCNICA"], ["Almohadilla arriba de la rodilla", "Solo la cadera se mueve",
                                     "Un segundo arriba", "Sin impulso"],
             "Claves: almohadilla arriba de la rodilla, solo la cadera se mueve, un segundo arriba y sin impulso.",
             [{"cut": "TOP", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · EMPUJÁ", "2 · LLEGÁ ARRIBA", "3 · BAJÁ"], [C("START"), seqloop("TOP", "START", 1.0, 1.7)]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, dejá que la pila baje sola y soltá la almohadilla despacio. No rebotes.",
             [C("TOP"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN REBOTAR", "end", 1.0)], 6.5),
    ]


def tk_scenes(slug):
    s, S, J = load(slug)
    HND = S(*J["CENTER"]["W"]); KNEE = S(-152, -90); PIN = S(-589, -155)
    CEN = S(-140, -520); SHO = S(*J["ROUND_BAD"]["S"]); SH_P = S(*J["PULL_BAD"]["S"])
    return [
        hook("GIMNASIO · CORE", ["TORSIÓN", "ARRODILLADO"], "En máquina de palanca",
             "Lever Kneeling Twist: torsión de torso arrodillado en máquina. Trabajás core y oblicuos con las caderas fijas.",
             [C("CENTER"), seqloop("TW_L", "TW_R", 1.0, 1.6, 0.4)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Almohadilla, manijas y pila",
             "La máquina tiene la almohadilla de rodillas, las manijas a la altura del pecho y la pila atrás.",
             [C("CENTER")], [ring(KNEE, 48, 0.8), lab((985, KNEE[1] + 40), "ALMOHADILLA", "end", 0.8),
                             ring(HND, 38, 1.8), lab((985, HND[1] - 20), "MANIJAS", "end", 1.8),
                             ring(PIN, 28, 2.8), lab((60, PIN[1] + 30), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["LAS", "RODILLAS"], "Centro de la almohadilla",
             "Apoyá las rodillas en el centro de la almohadilla, con las puntas de los pies atrás.",
             [C("CENTER")], [ring(KNEE, 48, 0.8), lab((985, KNEE[1] + 40), "ALMOHADILLA", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí un peso liviano: el giro lo hace el core, no los brazos.",
             [C("CENTER")], [ring(PIN, 28, 0.8), lab((60, PIN[1] + 30), "PILA", "start", 1.0)], 6.8),
        step("POSICIÓN INICIAL", ["ESPALDA", "RECTA"], "Codos flexionados",
             "Sentate sobre los talones, espalda recta y manos en las manijas con los codos flexionados.",
             [C("CENTER")], [ring(S(-140, -700), 70, 0.8), lab((60, S(-140, -700)[1] + 40), "ESPALDA RECTA", "start", 1.0)], 6.8),
        step("PASO 1 / 3", ["GIRÁ", "A UN LADO"], "Caderas quietas",
             "Paso uno. Girá el torso hacia un lado sin mover las caderas ni los brazos.",
             [C("TW_L")], topview=KTW(0.9, 2.8), mn=7.6, numeral="1"),
        step("PASO 2 / 3", ["VOLVÉ AL", "CENTRO"], "Controlá el peso",
             "Paso dos. Volvé al centro controlando el peso, sin dejarte llevar.",
             [C("CENTER"), TO("TW_L", 0.4, 0.8), TO("TW_R", 0.8, 1.2)], topview=KTW(0.8, 2.6, 20), mn=7.4, numeral="2"),
        step("PASO 3 / 3", ["GIRÁ AL", "OTRO LADO"], "Mismo rango",
             "Paso tres. Repetí para el otro lado, la misma cantidad de veces.",
             [C("TW_R")], topview=KTW(0.8, 2.8, -26), mn=7.4, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando girás y tomá aire al volver al centro.",
             [C("CENTER"), seqloop("TW_L", "TW_R", 1.1, 1.5, 0.3)], mn=6.2),
        step("ASÍ NO · 1 / 2", ["TIRAR CON", "LOS BRAZOS"], "El core hace el giro",
             "Error: tirar con los brazos y girar los hombros más que el torso.",
             [C("CENTER"), TO("PULL_BAD", 0.5, 0.8)], [NO(), ring(SH_P, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["REDONDEAR", "LA ESPALDA"], "Espalda recta",
             "Error: redondear la espalda y bajar la cabeza para llegar más lejos.",
             [C("CENTER"), TO("ROUND_BAD", 0.5, 0.8)], [NO(), ring(SHO, 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Rodillas en el centro", "Girá con el core",
                                          "Caderas quietas", "Volvé controlando"],
             "Tips: rodillas en el centro de la almohadilla, girá con el core, caderas quietas y volvé controlando.",
             [C("CENTER"), seqloop("TW_L", "TW_R", 1.0, 1.6, 0.4)]),
        keys("CLAVES", ["TÉCNICA"], ["Peso liviano", "Espalda recta",
                                     "Mismo rango cada lado", "Sin tirar con los brazos"],
             "Claves: peso liviano, espalda recta, el mismo rango para cada lado y sin tirar con los brazos.",
             [{"cut": "TW_L", "at": 0.1}]),
        reps(["3 X 10", "POR LADO"], "Un minuto de pausa",
             "Tres series de diez por lado, con un minuto de pausa. Alterná los lados sin soltar las manijas.",
             ["1 · GIRÁ", "2 · CENTRO", "3 · OTRO LADO"], [C("CENTER"), seqloop("TW_L", "TW_R", 1.0, 1.6)]),
        step("AL TERMINAR", ["SOLTÁ", "EL MANGO"], "Sin tirar",
             "Al terminar, volvé al centro, soltá las manijas y bajá el peso despacio.",
             [C("TW_R"), TO("CENTER", 0.7, 1.6)],
             [lab((985, 1040), "DESPACIO", "end", 1.0)], 6.5),
    ]


YT43 = {
    "titulo": "Lever Hip Extension 🔥 Extensión de cadera en máquina | Glúteos",
    "tags": ["lever hip extension", "extensión de cadera", "máquina de palanca", "glúteos", "isquiotibiales",
             "patada de glúteo", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de glúteos"],
    "descripcion": yt_desc("Lever Hip Extension", "extensión de cadera en máquina",
        "glúteos e isquiotibiales, sin cargar la espalda baja",
        "El glúteo trabaja cuando la cadera se extiende. En esta máquina el movimiento es corto: si buscás rango con la espalda, se lo llevás a la lumbar.",
        ["Ajustá el asiento para que la cadera quede a la altura del eje de la palanca.",
         "La almohadilla va detrás del muslo, justo arriba de la rodilla."],
        ["Sentate con la espalda apoyada en el respaldo y las manos en las manijas.",
         "Empujá con el glúteo y el isquio: el muslo baja y atrás, la espalda no se mueve.",
         "Arriba apretá el glúteo un segundo, sin arquear la espalda.",
         "Volvé bajando controlado, sin dejar que la pila pegue abajo."],
        ["Despegar la espalda del respaldo → espalda apoyada, menos peso.",
         "Levantar la cadera del asiento → cadera pegada y sin impulso.",
         "Rebotar abajo → frená el retorno y mantené la tensión."],
        ["Cadera a la altura del eje.", "Espalda apoyada en el respaldo.",
         "Empujá con el glúteo, no con la lumbar.", "Bajada lenta, sin rebote."],
        "Glúteos · Isquiotibiales",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gluteos #Isquios #Cadera #MaquinaDePalanca #Piernas #Entrenamiento")}

YT44 = {
    "titulo": "Lever Kneeling Twist 🔥 Torsión de torso arrodillado | Core",
    "tags": ["lever kneeling twist", "torsión de torso", "máquina de palanca", "core", "oblicuos",
             "rotación de torso", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de core"],
    "descripcion": yt_desc("Lever Kneeling Twist", "torsión de torso arrodillado",
        "core y oblicuos, con las caderas fijas",
        "El giro sale del torso, no de los brazos. Si tirás del mango, se mueven los hombros y el core no trabaja.",
        ["Apoyá las rodillas en el centro de la almohadilla, con las puntas de los pies atrás.",
         "Elegí un peso liviano: el giro lo hace el core, no los brazos."],
        ["Sentate sobre los talones, con la espalda recta y las manos en las manijas.",
         "Girá el torso hacia un lado sin mover las caderas ni los brazos.",
         "Volvé al centro controlando el peso, sin dejarte llevar.",
         "Repetí para el otro lado, la misma cantidad de veces."],
        ["Tirar con los brazos → girá con el core y dejá los brazos quietos.",
         "Redondear la espalda → espalda recta y menos rango.",
         "Girar la cadera con el torso → caderas fijas, solo gira el tronco."],
        ["Rodillas en el centro de la almohadilla.", "Girá con el core, no con los brazos.",
         "Caderas quietas durante todo el giro.", "Volvé al centro controlando el peso."],
        "Core · Oblicuos",
        "3 series de 10 por lado, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Core #Oblicuos #Torsion #MaquinaDePalanca #Abdomen #Entrenamiento")}

save("lever-hip-extension-v-2", he_scenes("lever-hip-extension-v-2"),
     {"pose": "START", "zoom": 1.15, "dy": 110}, YT43)

save("lever-kneeling-twist", tk_scenes("lever-kneeling-twist"),
     {"pose": "CENTER", "zoom": 1.12, "dy": 110}, YT44)
