# Dataset D41 Lever Deadlift y D42 Lever Gripper Hands: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def dl_scenes(slug):
    s, S, J = load(slug)
    A_B = S(*J["BOTTOM"]["A"]); A_T = S(*J["TOP"]["A"])
    SEAT = S(-320, -246); BACK = S(-325, -466); HND = S(-270, -320)
    HIP_B = S(*J["BACK_BAD"]["H"]); FT_B = S(*J["HEELS_BAD"]["A"])
    PL0 = (A_B[0] - 70, A_B[1] + 30); PL1 = (A_T[0] + 30, A_T[1] + 46)
    return [
        hook("GIMNASIO · PIERNAS", ["LEVER", "DEADLIFT"], "Peso muerto en máquina",
             "Lever Deadlift: peso muerto sentado en máquina. Empujás con los talones y extendés las caderas.",
             [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Asiento, plataforma y manijas",
             "La máquina tiene un asiento con respaldo, una plataforma para los pies y manijas a los costados.",
             [C("BOTTOM")], [ring(A_B, 62, 0.8), lab((985, 1400), "PLATAFORMA", "end", 0.8),
                             ring(SEAT, 44, 1.8), lab((985, 1310), "ASIENTO", "end", 1.8),
                             ring(HND, 30, 2.8), lab((60, 1290), "MANIJAS", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Espalda apoyada",
             "Ajustá el asiento para que la espalda quede apoyada en el respaldo y los pies lleguen cómodos.",
             [C("BOTTOM")], [ring(BACK, 46, 0.8), lab((985, 1150), "RESPALDO", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["LA", "PLATAFORMA"], "Pies planos y completos",
             "Regular la plataforma: apoyá los pies completos y planos, con el talón bien asentado.",
             [C("BOTTOM")], [ring(A_B, 62, 0.8), lab((60, 1400), "PIE COMPLETO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["RODILLAS", "FLEXIONADAS"], "Manos en las manijas",
             "Empezá con las rodillas flexionadas y las manos en las manijas. Activá glúteos e isquios antes de empujar.",
             [C("BOTTOM")], [ring(HND, 30, 0.8), lab((60, 1290), "MANIJAS", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "CON LOS TALONES"], "El peso sale con las piernas",
             "Paso uno. Empujá la plataforma con los talones, no con la punta del pie.",
             [C("BOTTOM"), TO("MID", 0.6, 0.9), TO("TOP", 0.6, 0.9)],
             [arrow(PL0, PL1, 0.8, 1.2, [0, -60]), lab((60, 1040), "EMPUJÁ", "start", 1.2)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["EXTENDÉ", "LAS CADERAS"], "Apretá los glúteos arriba",
             "Paso dos. Arriba extendé las caderas del todo y apretá los glúteos. La espalda no se despega.",
             [C("TOP")], [ring(S(*J["TOP"]["H"]), 48, 0.8), lab((60, 1180), "CADERA", "start", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLADO"], "Sin soltar el peso",
             "Paso tres. Volvé bajando controlado, manteniendo la tensión en glúteos e isquios.",
             [C("TOP"), TO("MID", 0.6, 0.9), TO("BOTTOM", 0.6, 1.6)],
             [arrow(PL1, PL0, 1.0, 1.2, [0, -50]), lab((60, 1040), "BAJÁ CONTROLADO", "start", 1.4)], 6.8, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
             "Tomá aire antes de empujar y soltalo mientras extendés las caderas.",
             [C("BOTTOM"), seqloop("TOP", "BOTTOM", 1.1, 2.0, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["TRABAR", "LAS RODILLAS"], "Nunca estires del todo",
             "Error: extender las rodillas hasta trabarlas. Frená un poco antes y mantené la tensión.",
             [C("MID"), TO("LOCK_BAD", 0.5, 0.8)], [NO(), ring(S(*J["LOCK_BAD"]["K"]), 44, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["REDONDEAR", "LA ESPALDA"], "Espalda apoyada y recta",
             "Error: redondear la espalda o despegarla del respaldo para empujar más. Bajá el peso.",
             [C("MID"), TO("BACK_BAD", 0.5, 0.8)], [NO(), ring(S(*J["BACK_BAD"]["S"]), 52, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TALONES", "ARRIBA"], "Todo el pie apoyado",
             "Error: empujar en punta de pie. Se pierde fuerza y se cargan los gemelos: apoyá el talón.",
             [C("MID"), TO("HEELS_BAD", 0.5, 0.8)], [NO(), ring(FT_B, 44, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Espalda en el respaldo", "Empujá con los talones",
                                          "Apretá los glúteos", "No trabes las rodillas"],
             "Tips: espalda en el respaldo, empujá con los talones, apretá los glúteos arriba y no trabes las rodillas.",
             [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
        keys("CLAVES", ["TÉCNICA"], ["Pies completos", "Rodillas sin trabar",
                                     "Caderas extendidas", "Bajada controlada"],
             "Claves: pies completos en la plataforma, rodillas sin trabar, caderas extendidas y bajada controlada.",
             [{"cut": "TOP", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · EMPUJÁ", "2 · EXTENDÉ", "3 · BAJÁ"], [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
        step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Con las rodillas flexionadas",
             "Al terminar, dejá el peso con las rodillas flexionadas. No sueltes la plataforma de golpe.",
             [C("TOP"), TO("BOTTOM", 0.8, 2.2)],
             [lab((985, 1040), "SIN SOLTAR", "end", 1.0)], 6.5),
    ]


def gh_scenes(slug):
    s, S, J = load(slug)
    W = S(*J["GRIP"]["W"]); SEAT = S(-245, -196); PIN = S(-589, -155); SH = S(*J["BACK_BAD"]["S"])
    return [
        hook("GIMNASIO · ANTEBRAZOS", ["GRIPPER", "HANDS"], "Máquina de agarre",
             "Lever Gripper Hands: máquina de agarre. Apretás el mango y trabajás antebrazos y mano.",
             [C("OPEN"), seqloop("GRIP", "OPEN", 0.7, 1.3)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Mango, asiento y pila",
             "Tiene un mango fijo, un asiento y la pila con el pasador. El mango no se mueve: lo que hacés es fuerza.",
             [C("OPEN")], [ring(W, 36, 0.8), lab((985, 1230), "MANGO", "end", 0.8),
                           ring(SEAT, 44, 1.8), lab((985, 1380), "ASIENTO", "end", 1.8),
                           ring(PIN, 28, 2.8), lab((60, 1400), "PESO", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Manos a la altura del mango",
             "Ajustá el asiento para que el mango quede a la altura del pecho y los codos flexionados.",
             [C("OPEN")], [ring(SEAT, 44, 0.8), lab((985, 1380), "ASIENTO", "end", 1.0),
                           ring(W, 36, 1.8), lab((985, 1230), "MANGO", "end", 1.8)], 7.2),
        step("AJUSTE 2", ["EL", "PESO"], "Empezá liviano",
             "Elegí el peso con el pasador: uno que te deje cerrar las doce veces sin perder la postura.",
             [C("OPEN")], [ring(PIN, 28, 0.8), lab((60, 1400), "PESO", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "RECTA"], "Pies planos en el suelo",
             "Sentate derecho, con la espalda recta y los pies planos. Agarrá el mango con la mano completa.",
             [C("OPEN")], [lab((60, 1000), "ESPALDA RECTA", "start", 1.0)], 6.8),
        step("PASO 1 / 3", ["APRETÁ", "EL MANGO"], "Toda la mano",
             "Paso uno. Apretá el mango con toda la mano, contrayendo el antebrazo. No muevas el brazo.",
             [C("OPEN"), TO("GRIP", 0.6, 0.8)],
             [ring(W, 36, 0.8), lab((985, 1180), "APRETÁ", "end", 1.0)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["SOSTENÉ", "UN SEGUNDO"], "Sin soltar",
             "Paso dos. Sostené la contracción un segundo, con la muñeca firme y el codo quieto.",
             [C("GRIP")], [ring(W, 36, 0.8), lab((985, 1180), "1 SEGUNDO", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["SOLTÁ", "LENTO"], "Sin abrir del todo",
             "Paso tres. Soltá lento hasta abrir la mano casi del todo y volvé a apretar.",
             [C("GRIP"), TO("OPEN", 0.8, 1.6)],
             [ring(W, 36, 0.8), lab((985, 1180), "SOLTÁ LENTO", "end", 1.2)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al apretar",
             "Soltá el aire mientras apretás y tomalo mientras soltás.",
             [C("OPEN"), seqloop("GRIP", "OPEN", 0.7, 1.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", ["REDONDEAR", "LA ESPALDA"], "Espalda recta",
             "Error: encorvarte para hacer fuerza. La espalda va recta y el trabajo lo hacen el antebrazo y la mano.",
             [C("GRIP"), TO("BACK_BAD", 0.5, 0.8)], [NO(), ring(SH, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["SOLTAR", "DE GOLPE"], "Abrí la mano sin tirar",
             "Error: soltar el mango de golpe y abrir la mano del todo. Soltá lento y controlá el peso.",
             [C("GRIP"), TO("DROP_BAD", 0.6, 0.7)], [NO(), ring(W, 36, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Mango a la altura del pecho", "Apretá toda la mano",
                                          "Codo quieto", "Soltá lento"],
             "Tips: mango a la altura del pecho, apretá con toda la mano, codo quieto y soltá lento.",
             [C("OPEN"), seqloop("GRIP", "OPEN", 0.7, 1.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda recta", "Pies planos",
                                     "1 segundo arriba", "Sin soltar de golpe"],
             "Claves: espalda recta, pies planos, un segundo de contracción y sin soltar de golpe.",
             [{"cut": "GRIP", "at": 0.1}]),
        reps(["3 X 12 POR MANO"], "Un minuto de pausa",
             "Tres series de diez a doce por mano, con un minuto de pausa. Empezá con poco peso.",
             ["1 · APRETÁ", "2 · SOSTENÉ", "3 · SOLTÁ"], [C("OPEN"), seqloop("GRIP", "OPEN", 0.7, 1.3)]),
        step("AL TERMINAR", ["ABRÍ LA", "MANO"], "Sin tirar el peso",
             "Al terminar, abrí la mano despacio y sacá el brazo. Si te tironea el codo, bajá el peso.",
             [C("DROP_BAD")], [lab((985, 1180), "DESPACIO", "end", 1.0)], 6.5),
    ]


YT41 = {
    "titulo": "Lever Deadlift 🔥 Peso muerto en máquina | Gimnasio",
    "tags": ["lever deadlift", "peso muerto en máquina", "peso muerto sentado", "máquina de palanca",
             "glúteos", "isquiotibiales", "empuje de cadera", "máquinas de gimnasio",
             "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Lever Deadlift", "peso muerto en máquina",
        "glúteos e isquiotibiales, con la espalda apoyada",
        "El peso muerto sentado en máquina: empujás con los talones y extendés las caderas sin cargar la espalda baja.",
        ["Ajustá el asiento para que la espalda quede apoyada en el respaldo.",
         "Apoyá los pies completos y planos en la plataforma."],
        ["Empezá con las rodillas flexionadas y las manos en las manijas.",
         "Activá glúteos e isquios y empujá la plataforma con los talones.",
         "Arriba extendé las caderas y apretá los glúteos, sin despegar la espalda.",
         "Volvé bajando controlado, manteniendo la tensión."],
        ["Trabar las rodillas → frená antes de estirar del todo.",
         "Redondear la espalda → espalda apoyada y recta, menos peso.",
         "Empujar en punta de pie → todo el pie apoyado, el talón manda."],
        ["Espalda apoyada en el respaldo.", "Empujá con los talones, no con la punta.",
         "Apretá los glúteos arriba.", "No trabes las rodillas al extender."],
        "Glúteos · Isquiotibiales · Cuádriceps",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #PesoMuerto #Gluteos #Isquios #MaquinaDePalanca #Piernas #Entrenamiento")}

YT42 = {
    "titulo": "Lever Gripper Hands 🔥 Máquina de agarre para antebrazos | Gimnasio",
    "tags": ["lever gripper hands", "máquina de agarre", "grip machine", "antebrazos", "agarre",
             "fuerza de mano", "máquina de palanca", "máquinas de gimnasio",
             "gimnasio", "principiantes", "rutina de antebrazos"],
    "descripcion": yt_desc("Lever Gripper Hands", "máquina de agarre",
        "antebrazos y fuerza de agarre",
        "¿Soltás el mango de golpe? Así se pierde la mitad del trabajo y se castiga el codo. Mirá cómo se hace.",
        ["Ajustá el asiento para que el mango quede a la altura del pecho.",
         "Elegí un peso que puedas cerrar doce veces sin perder la postura."],
        ["Sentate derecho, espalda recta y pies planos en el suelo.",
         "Agarrá el mango con toda la mano y el codo flexionado.",
         "Apretá el mango contrayendo el antebrazo y sostené un segundo.",
         "Soltá lento hasta abrir la mano casi del todo y repetí."],
        ["Encorvar la espalda → espalda recta y menos peso.",
         "Soltar el mango de golpe → soltá lento y controlá el peso.",
         "Mover el brazo para ayudar → el codo queda quieto."],
        ["Mango a la altura del pecho.", "Apretá con toda la mano, no solo con los dedos.",
         "Un segundo de contracción arriba.", "Soltá lento para no castigar el codo."],
        "Antebrazos · Mano · Agarre",
        "3 series de 10–12 por mano, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Antebrazos #Agarre #FuerzaDeMano #MaquinaDePalanca #Grip #Entrenamiento")}

save("lever-deadlift", dl_scenes("lever-deadlift"),
     {"pose": "BOTTOM", "zoom": 1.06, "dy": 110}, YT41)

save("lever-gripper-hands", gh_scenes("lever-gripper-hands"),
     {"pose": "GRIP", "zoom": 1.08, "dy": 110}, YT42)
