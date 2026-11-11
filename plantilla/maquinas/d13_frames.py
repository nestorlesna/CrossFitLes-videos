# Dataset D01 · D25 Lever Reverse Grip Preacher Curl y D26 Lever Seated Calf Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def curl_scenes(slug, grip, sub_hook, vo_hook, vo_pos):
    s, S, J = load(slug)
    PAD_M = S(-135, -395); SEAT_K = S(-240, -94); PIN = S(-609, -155)
    HAND_D = S(*J["DOWN"]["W"]); HAND_U = S(*J["UP"]["W"])
    E_OFF = S(*J["OFF_BAD"]["E"]); HIP_SW = S(*J["SWING_BAD"]["H"])
    PILE = S(-660, -70)
    A1 = (HAND_D[0] + 23, HAND_D[1] - 1); B1 = (HAND_U[0] + 19, HAND_U[1] + 12)
    return [
        hook("GIMNASIO · BRAZOS", ["PREACHER", "CURL"], sub_hook, vo_hook,
             [C("DOWN"), seqloop("UP", "DOWN")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "También: Scott o predicador",
             "La máquina Scott o predicador aísla el bíceps. Con el brazo apoyado, el codo no se mueve y no hay trampa.",
             [C("DOWN")], [ring(PAD_M, 50, 0.8), lab((60, 1249), "APOYO", "start", 0.8),
                           ring(HAND_D, 34, 1.8), lab((985, 1370), "MANIJAS", "end", 1.8),
                           ring(PILE, 44, 2.6), lab((60, 1400), "PILA", "start", 2.6)], 7.0),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Axilas en el borde del apoyo",
             "Ajustá el asiento para que las axilas queden justo en el borde del apoyo y el codo al lado del eje rojo.",
             [C("DOWN")], [ring(SEAT_K, 40, 0.8), lab((985, 1430), "ASIENTO", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
             "Elegí el peso con el pasador: uno que puedas subir doce veces sin despegar los brazos del apoyo.",
             [C("DOWN")], [ring(PIN, 26, 0.8), lab((60, 1393), "PASADOR", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["BRAZOS", "APOYADOS"], "Tríceps pegados a la almohadilla",
             vo_pos,
             [C("DOWN")], [ring(HAND_D, 34, 0.8), lab((985, 1290), grip, "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ", "A LOS HOMBROS"], "Sin despegar los brazos",
             "Paso uno. Flexioná los codos llevando las manijas hacia los hombros, sin despegar los brazos del apoyo.",
             [C("DOWN"), TO("UP", 0.6, 1.0)],
             [arrow(A1, B1, 0.8, 1.2, [70, 0]), lab((60, 1010), "SUBÍ", "start", 1.2)], numeral="1"),
        step("PASO 2 / 3", ["APRETÁ", "ARRIBA"], "Un segundo",
             "Paso dos. Arriba, apretá el bíceps un segundo y no muevas los codos.",
             [C("UP")], [ring(HAND_U, 38, 0.8), lab((985, 1120), "APRETÁ 1 SEG", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Frená antes de estirar",
             "Paso tres. Bajá lento y frená antes de estirar del todo el codo. Así cuidás el tendón.",
             [C("UP"), TO("DOWN", 0.6, 3.0)],
             [arrow(B1, A1, 1.0, 1.2, [60, 0]), lab((60, 1010), "BAJÁ LENTO", "start", 1.4)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
             "Soltá el aire mientras subís y tomalo mientras bajás.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.1, 2.0, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", ["BRAZOS", "DESPEGADOS"], "Tríceps siempre apoyados",
             "Error: despegar los brazos del apoyo para subir. Deja de ser un curl aislado: tríceps pegados todo el tiempo.",
             [C("DOWN"), TO("OFF_BAD", 0.5, 1.0)], [NO(), ring(E_OFF, 44, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["BALANCEAR", "EL CUERPO"], "La cola no se despega",
             "Error: tirarte atrás y despegar la cola para ayudarte. Bajá el peso y subí solo con los brazos.",
             [C("DOWN"), TO("SWING_BAD", 0.5, 0.7)], [NO(), ring(HIP_SW, 46, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Axilas en el borde", "Codo alineado con el eje", "Tríceps pegados", "Frená antes de estirar"],
             "Tips de profe: axilas en el borde del apoyo, codo alineado con el eje, tríceps pegados y frená antes de estirar del todo.",
             [C("DOWN"), seqloop("UP", "DOWN")]),
        keys("CLAVES", ["TÉCNICA"], ["Subí en 1 segundo", "Bajá en 3 segundos", "Sin despegar la cola", "Muñecas firmes"],
             "Claves: subí en un segundo, bajá en tres, sin despegar la cola y con las muñecas firmes.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Cuando las doce salen fáciles, subí una placa.",
             ["1 · SUBÍ", "2 · APRETÁ", "3 · BAJÁ LENTO"], [C("DOWN"), seqloop("UP", "DOWN")]),
        step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
             "Al terminar, acompañá las manijas y dejá el peso apoyado. No lo sueltes de golpe.",
             [C("UP"), TO("DOWN", 0.8, 2.2)],
             [lab((60, 1010), "DEJÁ EL PESO", "start", 1.0)], 6.5),
    ]


def calf_scenes(slug):
    s, S, J = load(slug)
    PAD = S(-75, -300); STEP = S(100, -96)
    A_DN = S(*J["DOWN"]["A"]); A_UP = S(*J["UP"]["A"]); SH_B = S(*J["PUSH_BAD"]["S"])
    return [
        hook("GIMNASIO · PIERNAS", ["CALF", "PRESS"], "Gemelos sentado en prensa",
             "Lever Seated Calf Press: gemelos sentado en prensa de palanca. Con la rodilla doblada trabaja sobre todo el sóleo.",
             [C("DOWN"), seqloop("UP", "DOWN")]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Almohadilla sobre los muslos",
             "Tiene una almohadilla sobre los muslos y un escalón para la punta del pie. Trabaja el sóleo y los gemelos.",
             [C("DOWN")], [ring(PAD, 60, 0.8), lab((985, 1000), "ALMOHADILLA", "end", 0.8),
                           ring(STEP, 50, 1.8), lab((985, 1430), "ESCALÓN", "end", 1.8)], 7.0),
        step("AJUSTE 1", ["LA", "ALMOHADILLA"], "Cerca de la rodilla",
             "Ajustá la almohadilla sobre los muslos, cerca de la rodilla. Si queda lejos, el ejercicio pierde fuerza.",
             [C("DOWN")], [ring(PAD, 60, 0.8), lab((985, 1000), "CERCA DE LA RODILLA", "end", 1.0)], 7.0),
        step("AJUSTE 2", ["LOS", "PIES"], "La punta en el borde",
             "Apoyá la punta del pie en el borde del escalón, con el talón en el aire. Después destrabá la palanca.",
             [C("DOWN")], [ring(STEP, 50, 0.8), lab((985, 1440), "PUNTA", "end", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["SENTADO", "DERECHO"], "Las manos solo sostienen",
             "Sentado derecho, con las manos sobre la almohadilla. Las manos sostienen, no empujan.",
             [C("MID")], [], 6.5),
        step("PASO 1 / 3", ["BAJÁ EL", "TALÓN"], "Despacio",
             "Paso uno. Bajá el talón despacio hasta estirar bien la pantorrilla.",
             [C("MID"), TO("DOWN", 0.6, 1.8)],
              [ring(A_DN, 44, 1.6), lab((985, 1350), "ESTIRÁ ABAJO", "end", 1.6)], 6.5, numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "ABAJO"], "Sin rebote",
             "Paso dos. Abajo, pausa estirando. Nada de rebotar.",
             [C("DOWN")], [ring(A_DN, 44, 0.8), lab((985, 1440), "PAUSA", "end", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["SUBÍ", "Y APRETÁ"], "Lento, bien arriba",
             "Paso tres. Subí lento lo más alto que puedas y apretá arriba un segundo.",
             [C("DOWN"), TO("UP", 0.6, 1.4)],
             [ring(A_UP, 44, 1.6)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
             "Soltá el aire mientras subís y tomalo mientras bajás.",
             [C("DOWN"), seqloop("UP", "DOWN", 1.4, 2.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", ["REBOTAR", "ABAJO"], "Pausa, no resorte",
             "Error: rebotar abajo y hacer el recorrido corto. Bajá todo, pausá y subí todo.",
             [C("MID"), seqloop("DOWN", "MID", 0.3, 0.3, 0.5)],
             [NO(at=1.0), ring(A_DN, 44, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["EMPUJAR CON", "EL CUERPO"], "Las manos no empujan",
             "Error: empujar con las manos o tirar el tronco adelante. Si hace falta, el peso es mucho: bajalo.",
             [C("DOWN"), TO("PUSH_BAD", 0.5, 1.0)], [NO(), ring(SH_B, 56, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Talón abajo, estirá", "Pausa sin rebote", "Subí lento y apretá", "Las manos no empujan"],
             "Tips de profe: bajá el talón estirando la pantorrilla, pausá sin rebotar, subí lento apretando y no empujes con las manos.",
             [C("DOWN"), seqloop("UP", "DOWN")]),
        keys("CLAVES", ["TÉCNICA"], ["Almohadilla cerca de la rodilla", "Punta en el borde", "Rango completo", "Trabá al terminar"],
             "Claves: almohadilla cerca de la rodilla, la punta en el borde, rango completo y trabá la palanca al terminar.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15"], "Un minuto de pausa",
             "Tres series de quince, con un minuto de pausa. Cuando las quince salen fáciles, subí el peso.",
             ["1 · BAJÁ EL TALÓN", "2 · PAUSA", "3 · SUBÍ Y APRETÁ"], [C("DOWN"), seqloop("UP", "DOWN")]),
        step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
             "Al terminar, acompañá la almohadilla y dejá el peso apoyado antes de sacar las piernas.",
             [C("UP"), TO("DOWN", 0.8, 2.2)],
             [lab((60, 1010), "DEJÁ EL PESO", "start", 1.0)], 6.5),
    ]


YT25 = {
    "titulo": "Lever Reverse Grip Preacher Curl 🔥 Curl Scott con agarre prono | Gimnasio",
    "tags": ["lever reverse grip preacher curl", "curl scott", "preacher curl", "agarre prono", "curl inverso",
             "curl de bíceps en máquina", "predicador", "bíceps", "braquial", "antebrazos",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de brazos"],
    "descripcion": yt_desc("Lever Reverse Grip Preacher Curl", "curl Scott con agarre prono",
        "bíceps, con braquial y antebrazos como apoyo",
        "Con el agarre prono el antebrazo trabaja más y la muñeca sufre menos. Mirá cómo hacer el Scott invertido.",
        ["Ajustá el asiento para que las axilas queden en el borde del apoyo.", "Elegí un peso que puedas subir 12 veces."],
        ["Sentate con los tríceps pegados a la almohadilla y la cola en el asiento.",
         "Agarrá las manijas con agarre prono, las palmas hacia abajo.",
         "Flexioná los codos llevando las manijas a los hombros, sin despegar los brazos.",
         "Apretá arriba un segundo y bajá lento, frenando antes de estirar."],
        ["Despegar los brazos del apoyo → tríceps pegados todo el tiempo.",
         "Balancear el cuerpo → la cola no se despega del asiento.",
         "Extender de golpe abajo → frená antes de estirar del todo."],
        ["Axilas en el borde del apoyo.", "Codo alineado con el eje de la máquina.",
         "Tríceps pegados a la almohadilla.", "Muñecas firmes: no dejes que se doblen."],
        "Bíceps · Braquial · Antebrazos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #PreacherCurl #AgarreProno #Biceps #Brazos #Musculacion #Entrenamiento")}

YT26 = {
    "titulo": "Lever Seated Calf Press 🔥 Gemelos sentado en prensa de palanca | Gimnasio",
    "tags": ["lever seated calf press", "gemelos sentado", "calf press", "sóleo", "gemelos",
             "pantorrilla", "prensa de gemelos", "máquina de palanca", "piernas",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Lever Seated Calf Press", "gemelos sentado en prensa de palanca",
        "sóleo, con los gemelos como apoyo",
        "Con la rodilla doblada el sóleo trabaja a fondo. Mirá cómo usar la prensa de gemelos sentado.",
        ["Ajustá la almohadilla sobre los muslos, cerca de la rodilla.", "Apoyá la punta del pie en el borde del escalón."],
        ["Sentate derecho con las manos sobre la almohadilla, solo sosteniendo.",
         "Destrabá la palanca y bajá el talón despacio hasta estirar.",
         "Hacé una pausa abajo, sin rebotar.",
         "Subí lento lo más alto posible y apretá arriba un segundo."],
        ["Rebotar abajo → pausá estirando y subí todo el recorrido.",
         "Recorrido corto → bajá y subí completo.",
         "Empujar con las manos o el tronco → las manos solo sostienen."],
        ["Almohadilla cerca de la rodilla.", "Punta del pie en el borde del escalón.",
         "Pausa abajo sin rebote.", "Trabá la palanca al terminar."],
        "Sóleo · Gemelos",
        "3 series de 15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Soleo #CalfPress #Piernas #Musculacion #Entrenamiento")}

save("lever-reverse-grip-preacher-curl",
     curl_scenes("lever-reverse-grip-preacher-curl", "PRONO", "Curl Scott con agarre prono",
                 "Lever Reverse Grip Preacher Curl: curl en máquina Scott con agarre prono. Palmas hacia abajo y brazos apoyados.",
                 "Apoyá los brazos con los tríceps pegados a la almohadilla y agarrá las manijas con las palmas hacia abajo."),
     {"pose": "UP", "zoom": 1.15, "dy": 110}, YT25)

save("lever-seated-calf-press",
     calf_scenes("lever-seated-calf-press"),
     {"pose": "UP", "zoom": 1.1, "dy": 100}, YT26)
