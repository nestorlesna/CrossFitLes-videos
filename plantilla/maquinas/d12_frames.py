# Dataset D01 · D23 Lever Hammer Grip Preacher Curl y D24 Lever Preacher Curl v. 2: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def scenes(slug, grip, sub_hook, vo_hook):
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
             "Apoyá los brazos con los tríceps pegados a la almohadilla y agarrá las manijas. La cola, en el asiento.",
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


YT23 = {
    "titulo": "Lever Hammer Grip Preacher Curl 🔥 Curl Scott con agarre martillo | Gimnasio",
    "tags": ["lever hammer grip preacher curl", "curl scott", "preacher curl", "agarre martillo", "agarre neutro",
             "curl de bíceps en máquina", "predicador", "bíceps", "braquial", "antebrazos",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de brazos"],
    "descripcion": yt_desc("Lever Hammer Grip Preacher Curl", "curl Scott con agarre martillo",
        "bíceps, con braquial y antebrazos como apoyo",
        "El agarre martillo en el Scott suma braquial y antebrazo sin castigar la muñeca. Mirá cómo se hace.",
        ["Ajustá el asiento para que las axilas queden en el borde del apoyo.", "Elegí un peso que puedas subir 12 veces."],
        ["Sentate con los tríceps pegados a la almohadilla y la cola en el asiento.",
         "Agarrá las manijas con las palmas enfrentadas (agarre martillo).",
         "Flexioná los codos llevando las manijas a los hombros, sin despegar los brazos.",
         "Apretá arriba un segundo y bajá lento, frenando antes de estirar."],
        ["Despegar los brazos del apoyo → tríceps pegados todo el tiempo.",
         "Balancear el cuerpo → la cola no se despega del asiento.",
         "Extender de golpe abajo → frená antes de estirar del todo."],
        ["Axilas en el borde del apoyo.", "Codo alineado con el eje de la máquina.",
         "Tríceps pegados a la almohadilla.", "Muñecas firmes y bajada controlada."],
        "Bíceps · Braquial · Antebrazos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #PreacherCurl #AgarreMartillo #Biceps #Brazos #Musculacion #Entrenamiento")}

YT24 = {
    "titulo": "Lever Preacher Curl v. 2 🔥 Curl Scott en máquina de palanca | Gimnasio",
    "tags": ["lever preacher curl", "curl scott", "preacher curl", "curl de bíceps en máquina", "predicador",
             "máquina de palanca", "bíceps", "braquial", "antebrazos",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de brazos"],
    "descripcion": yt_desc("Lever Preacher Curl v. 2", "curl Scott en máquina de palanca",
        "bíceps, con braquial y antebrazos como apoyo",
        "El curl Scott de siempre en máquina de palanca: brazos apoyados y cero trampa para aislar el bíceps.",
        ["Ajustá el asiento para que las axilas queden en el borde del apoyo.", "Elegí un peso que puedas subir 12 veces."],
        ["Sentate con los tríceps pegados a la almohadilla y la cola en el asiento.",
         "Agarrá las manijas con agarre supino, las palmas hacia arriba.",
         "Flexioná los codos llevando las manijas a los hombros, sin despegar los brazos.",
         "Apretá arriba un segundo y bajá lento, frenando antes de estirar."],
        ["Despegar los brazos del apoyo → tríceps pegados todo el tiempo.",
         "Balancear el cuerpo → la cola no se despega del asiento.",
         "Extender de golpe abajo → frená antes de estirar del todo."],
        ["Axilas en el borde del apoyo.", "Codo alineado con el eje de la máquina.",
         "Tríceps pegados a la almohadilla.", "Bajá en tres segundos, sin soltar el peso."],
        "Bíceps · Braquial · Antebrazos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #PreacherCurl #CurlScott #Biceps #Brazos #Musculacion #Entrenamiento")}

save("lever-hammer-grip-preacher-curl",
     scenes("lever-hammer-grip-preacher-curl", "MARTILLO", "Curl Scott con agarre martillo",
            "Lever Hammer Grip Preacher Curl: curl en máquina Scott con agarre martillo. Palmas enfrentadas y brazos apoyados."),
     {"pose": "UP", "zoom": 1.15, "dy": 110}, YT23)

save("lever-preacher-curl-v-2",
     scenes("lever-preacher-curl-v-2", "SUPINO", "Curl Scott clásico",
            "Lever Preacher Curl versión dos: el curl Scott de siempre en máquina de palanca. Brazos apoyados y cero trampa."),
     {"pose": "UP", "zoom": 1.15, "dy": 110}, YT24)
