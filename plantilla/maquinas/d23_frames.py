# Dataset D45 Lever Pullover y D46 Lever Seated Good Morning: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def pl_scenes(slug):
    s, S, J = load(slug)
    SEAT = S(-260, -270); BACK = S(-330, -470); HIP = S(*J["START"]["H"])
    H0 = S(*J["START"]["W"]); H1 = S(*J["PULL"]["W"]); PIN = S(-569, -155)
    CH = S(-270, -515); LAT = S(*J["PULL"]["S"])
    SH_B = S(*J["LEAN_BAD"]["S"]); RND = S(*J["ROUND_BAD"]["S"]); LOW = S(*J["LOW_BAD"]["W"])
    return [
        hook("GIMNASIO · ESPALDA", ["LEVER", "PULLOVER"], "Manos al pecho",
             "Lever Pullover: jalón en máquina de palanca. Tirás las manijas al pecho con los codos bajos y trabajás dorsales.",
             [C("START"), seqloop("PULL", "START", 1.0, 1.7, 0.4)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Asiento, manijas y pila",
             "La máquina tiene asiento con respaldo, manijas al frente y la pila atrás.",
             [C("START")], [ring(H0, 44, 0.8), lab((985, H0[1] + 40), "MANIJAS", "end", 0.8),
                            ring(SEAT, 44, 1.8), lab((985, SEAT[1] - 90), "ASIENTO", "end", 1.8),
                            ring(PIN, 28, 2.8), lab((60, PIN[1] + 30), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Pecho a la altura de las manijas",
             "Ajustá el asiento para que las manijas queden a la altura del pecho.",
             [C("START")], [ring(H0, 44, 0.8), lab((60, H0[1] + 30), "ALTURA", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["EL", "AGARRE"], "Prono, pulgares adentro",
             "Agarre prono, con los pulgares para adentro, y los brazos apenas flexionados.",
             [C("START")], [ring(H0, 40, 0.8), lab((985, H0[1] + 50), "AGARRE PRONO", "end", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "APOYADA"], "Codos bajos",
             "Sentate con la espalda apoyada y los codos bajos, casi pegados al cuerpo. El core activo.",
             [C("START")], [ring(BACK, 60, 0.8), lab((60, BACK[1] + 80), "RESPALDO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["TIRÁ", "AL PECHO"], "Con los codos bajos",
             "Paso uno. Tirá las manijas al pecho con los codos bajos, sin encoger los hombros.",
             [C("START"), TO("PULL", 0.6, 1.0)],
             [arrow((H0[0] + 34, H0[1] - 6), (H1[0] + 26, H1[1] - 40), 0.8, 1.0, [40, -30]),
              lab((60, H0[1] - 40), "TIRÁ", "start", 1.0)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["APRETÁ", "EL DORSAL"], "Un segundo",
             "Paso dos. Apretá el dorsal un segundo, con el pecho arriba y los hombros abajo.",
             [C("PULL"), TO("PULL", 0.2, 0.4)],
             [ring(CH, 54, 0.8), lab((985, CH[1] - 40), "APRETÁ", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Sin soltar de golpe",
             "Paso tres. Volvé lento, estirando los brazos sin dejar que la pila pegue abajo.",
             [C("PULL"), TO("START", 0.6, 1.4)],
             [arrow((H1[0] + 26, H1[1] - 40), (H0[0] + 34, H0[1] - 6), 0.9, 1.0, [40, 30]),
              lab((60, H0[1] - 30), "VOLVÉ LENTO", "start", 1.1)], 6.8, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al volver",
             "Soltá el aire cuando tirás y tomá aire cuando volvés. El abdomen queda firme.",
             [C("START"), seqloop("PULL", "START", 1.0, 1.8, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["TIRAR CON", "LOS BRAZOS"], "Los dorsales hacen el trabajo",
             "Error: tirar solo con los brazos y encoger los hombros. Pensá en llevar el codo al bolsillo.",
             [C("START"), TO("PULL", 0.5, 0.8)], [NO(1.4, (540, 930)), ring(LAT, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["ECHCARTE", "ATRÁS"], "Espalda en el respaldo",
             "Error: echarse atrás para ayudar con el peso del cuerpo. La espalda queda en el respaldo.",
             [C("START"), TO("LEAN_BAD", 0.5, 0.8)], [NO(1.4, (540, 930)), ring(SH_B, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda y dejar caer los hombros hacia adelante.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4, (540, 930)), ring(RND, 56, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pecho arriba", "Codos bajos y cerca",
                                          "Un segundo al pecho", "Volvé lento"],
             "Tips: pecho arriba, codos bajos y cerca del cuerpo, un segundo al pecho y volvé lento.",
             [C("START"), seqloop("PULL", "START", 1.0, 1.7, 0.4)]),
        keys("CLAVES", ["TÉCNICA"], ["Manijas a la altura del pecho", "Agarre prono",
                                     "Sin encoger los hombros", "Sin impulso"],
             "Claves: manijas a la altura del pecho, agarre prono, sin encoger los hombros y sin impulso.",
             [{"cut": "PULL", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · TIRÁ", "2 · APRETÁ", "3 · VOLVÉ"], [C("START"), seqloop("PULL", "START", 1.0, 1.7)]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, dejá que la pila baje sola y soltá las manijas despacio. No rebotes.",
             [C("PULL"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN REBOTAR", "end", 1.0)], 6.5),
    ]


def gm_scenes(slug):
    s, S, J = load(slug)
    SEAT = S(-260, -350); HND = S(*J["UP"]["W"]); PIN = S(-569, -155)
    HIP = S(*J["UP"]["H"]); SH = S(*J["HINGE"]["S"]); SH_UP = S(*J["UP"]["S"]); HD_B = S(*J["HEAD_BAD"]["N"])
    RND = S(-240, -470); LOW = S(*J["LOW_BAD"]["S"])
    return [
        hook("GIMNASIO · ISQUIOS", ["LEVER SEATED", "GOOD MORNING"], "En máquina de palanca",
             "Lever Seated Good Morning: buenos días sentado en máquina. Bisagras desde la cadera y trabajás isquios y glúteos.",
             [C("UP"), seqloop("HINGE", "UP", 1.2, 1.8, 0.4)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Asiento, apoyapiés y pila",
             "La máquina tiene asiento con respaldo, manijas al costado y la pila atrás.",
             [C("UP")], [ring(SEAT, 44, 0.8), lab((985, SEAT[1] + 60), "ASIENTO", "end", 0.8),
                         ring(HND, 38, 1.8), lab((985, HND[1] - 30), "MANIJAS", "end", 1.8),
                         ring(PIN, 28, 2.8), lab((60, PIN[1] + 30), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE", ["CADERA", "ALTA"], "Un poco más que las rodillas",
             "Ajustá el asiento para que las caderas queden un poco más altas que las rodillas.",
             [C("UP")], [ring(HIP, 46, 0.8), lab((60, HIP[1] - 60), "CADERA", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "RECTA"], "Pies planos",
             "Sentate con la espalda recta, los pies planos y las manos en las manijas del asiento.",
             [C("UP")], [ring(SEAT, 46, 0.8), lab((60, SEAT[1] + 90), "PIES PLANOS", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["INCLINATE", "DESDE LA CADERA"], "Espalda recta",
             "Paso uno. Con la espalda recta, inclinate desde la cadera llevando el pecho hacia los muslos.",
             [C("UP"), TO("HINGE", 0.6, 1.2)],
             [arrow((SH[0] + 70, SH_UP[1] - 60), (SH[0] + 96, SH[1] + 10), 0.8, 1.2, [50, 0]),
              ring(HIP, 40, 0.8), lab((60, HIP[1] + 60), "BISAGRA", "start", 1.0)], 7.2, numeral="1"),
        step("PASO 2 / 3", ["PARALELO", "AL PISO"], "Pausa corta",
             "Paso dos. Bajá hasta que la espalda quede casi paralela al piso y hacé una pausa corta.",
             [C("HINGE"), TO("HINGE", 0.2, 0.4)],
             [ring(SH, 54, 0.8), lab((985, SH[1] - 40), "PARALELO", "end", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["VOLVÉ", "CON EL GLÚTEO"], "Sin tirar con la espalda",
             "Paso tres. Volvé empujando con los glúteos y los isquios, sin tirar con la espalda.",
             [C("HINGE"), TO("UP", 0.6, 1.4)],
             [arrow((SH[0] + 96, SH[1] + 10), (SH[0] + 70, SH_UP[1] - 60), 0.9, 1.2, [50, 0]),
              lab((60, SH_UP[1] - 40), "EMPUJÁ EL GLÚTEO", "start", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al subir",
             "Tomá aire al bajar y soltalo al subir. El abdomen queda firme para cuidar la espalda.",
             [C("UP"), seqloop("HINGE", "UP", 1.2, 1.8, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["REDONDEAR", "LA ESPALDA"], "Espalda recta",
             "Error: redondear la espalda para bajar más. Menos rango y espalda recta.",
             [C("UP"), TO("ROUND_BAD", 0.5, 0.8)], [NO(1.4, (540, 930)), ring(RND, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["PASAR", "EL PARALELO"], "Frená a la altura",
             "Error: bajar más allá del paralelo buscando rango. Frená cuando el torso queda paralelo.",
             [C("UP"), TO("LOW_BAD", 0.5, 0.8)], [NO(), ring(LOW, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["MIRAR", "ABAJO"], "Mirada al frente",
             "Error: bajar la cabeza y mirar al piso. La mirada va al frente, el cuello sigue la espalda.",
             [C("UP"), TO("HEAD_BAD", 0.5, 0.8)], [NO(), ring(HD_B, 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Cadera más alta que la rodilla", "Bisagra de cadera",
                                          "Espalda recta", "Volvé con el glúteo"],
             "Tips: cadera más alta que la rodilla, bisagra de cadera, espalda recta y volvé con el glúteo.",
             [C("UP"), seqloop("HINGE", "UP", 1.2, 1.8, 0.4)]),
        keys("CLAVES", ["TÉCNICA"], ["Pies planos y firmes", "Sin redondear la espalda",
                                     "Paralelo al piso", "Sin impulso"],
             "Claves: pies planos y firmes, sin redondear la espalda, bajá hasta el paralelo y sin impulso.",
             [{"cut": "HINGE", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · BAJÁ", "2 · PAUSA", "3 · SUBÍ"], [C("UP"), seqloop("HINGE", "UP", 1.2, 1.8)]),
        step("AL TERMINAR", ["VOLVÉ", "AL CENTRO"], "Sin rebotar",
             "Al terminar, volvé arriba sin rebotar y dejá que la pila baje despacio.",
             [C("HINGE"), TO("UP", 0.9, 2.0)],
             [lab((985, 1040), "SIN REBOTAR", "end", 1.0)], 6.5),
    ]


def te_scenes(slug):
    s, S, J = load(slug)
    SEAT = S(-260, -270); BACK = S(-330, -470); PIN = S(-569, -155)
    H0 = S(*J["START"]["W"]); H1 = S(*J["DOWN"]["W"]); PIV = S(*J["START"]["E"])
    HSHORT = S(*J["SHORT_BAD"]["W"]); HDROP = S(*J["DROP_BAD"]["W"]); SH_ARCH = S(*J["ARCH_BAD"]["S"])
    return [
        hook("GIMNASIO · BRAZOS", ["LEVER TRICEPS", "EXTENSION"], "En máquina de palanca",
             "Lever Triceps Extension: extensión de tríceps en máquina de palanca. Codos quietos y antebrazo que gira.",
             [C("START"), seqloop("DOWN", "START", 1.2, 1.8, 0.4)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Asiento, palanca y pila",
             "La máquina tiene asiento con respaldo, la palanca con la manija y la pila atrás.",
             [C("START")], [ring(H0, 44, 0.8), lab((985, H0[1] + 40), "MANIJAS", "end", 0.8),
                            ring(SEAT, 44, 1.8), lab((985, SEAT[1] - 90), "ASIENTO", "end", 1.8),
                            ring(PIN, 28, 2.8), lab((60, PIN[1] + 30), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["EL", "ASIENTO"], "Manija a la altura del hombro",
             "Ajustá el asiento para que la manija quede a la altura del hombro y el codo apoye en el eje.",
             [C("START")], [ring(H0, 40, 0.8), lab((60, H0[1] - 40), "ALTURA DEL HOMBRO", "start", 1.0),
                            ring(PIV, 34, 1.8), lab((985, PIV[1] + 40), "EJE DEL CODO", "end", 1.8)], 7.0),
        step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
             "Elegí el peso con el pasador: uno que puedas mover doce veces sin mover los codos.",
             [C("START")], [ring(PIN, 30, 0.8), lab((60, PIN[1] + 30), "PASADOR", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["ESPALDA", "APOYADA"], "Pies planos",
             "Sentate con la espalda apoyada en el respaldo, los pies planos y las manos en las manijas.",
             [C("START")], [ring(BACK, 60, 0.8), lab((60, BACK[1] + 80), "RESPALDO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "LENTO"], "Los codos no se mueven",
             "Paso uno. Con los codos quietos, bajá las manijas lento hacia la frente.",
             [C("START"), TO("DOWN", 0.6, 1.1)],
             [arrow((H0[0], H0[1] - 26), (H1[0] + 26, H1[1] - 20), 0.8, 1.1, [30, -40]),
              ring(PIV, 34, 1.2), lab((985, PIV[1] + 40), "CODO FIJO", "end", 1.2)], 7.0, numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "CORTA"], "Cerca de la frente",
             "Paso dos. Hacé una pausa con las manijas cerca de la frente, sin dejar caer el peso.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)],
             [ring(H1, 44, 0.8), lab((60, H1[1] - 40), "PAUSA", "start", 1.0)], 6.8, numeral="2"),
        step("PASO 3 / 3", ["EXTENDÉ", "ARRIBA"], "Apretá el tríceps",
             "Paso tres. Extendé los brazos hacia adelante y arriba, apretando el tríceps.",
             [C("DOWN"), TO("START", 0.6, 1.2)],
             [arrow((H1[0] + 26, H1[1] - 20), (H0[0], H0[1] - 26), 0.9, 1.1, [30, 40]),
              lab((985, H0[1] + 40), "EXTENDÉ", "end", 1.1)], 7.0, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al bajar",
             "Soltá el aire cuando extendés y tomá aire cuando bajás. No aguantes la respiración.",
             [C("START"), seqloop("DOWN", "START", 1.1, 1.8, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["ARQUEAR", "LA ESPALDA"], "Pegado al respaldo",
             "Error: echarse atrás y arquear la espalda para empujar. Espalda pegada al respaldo.",
             [C("START"), TO("ARCH_BAD", 0.5, 0.9)], [NO(1.4, (540, 930)), ring(SH_ARCH, 54, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["DEJAR CAER", "EL PESO"], "Bajá controlando",
             "Error: dejar caer el peso de golpe. Bajá y volvé controlando, sin rebotar.",
             [C("START"), {"seq": [["DOWN", 0.3], ["DROP_BAD", 0.3]], "at": 0.5, "until": 4.0},
              {"to": "DROP_BAD", "at": 4.0, "dur": 0.3}],
             [NO(1.4, (540, 930)), ring(HDROP, 44, 3.4), lab((985, HDROP[1] + 40), "DE GOLPE", "end", 3.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["EXTENDER", "A MEDIAS"], "Estirá el codo",
             "Error: extender a medias. Estirá casi por completo el codo y sentí el tríceps.",
             [C("START"), TO("SHORT_BAD", 0.5, 0.8)], [NO(1.4, (540, 930)), ring(HSHORT, 46, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Codos quietos", "Bajá hasta la frente",
                                          "Extendé completo", "Peso liviano"],
             "Tips: codos quietos, bajá hasta la frente, extendé completo y arrancá con poco peso.",
             [C("START"), seqloop("DOWN", "START", 1.2, 1.8, 0.4)]),
        keys("CLAVES", ["TÉCNICA"], ["Manija a la altura del hombro", "Codo en el eje",
                                     "Sin arquear la espalda", "Volvé controlando"],
             "Claves: manija a la altura del hombro, codo en el eje, sin arquear la espalda y volvé controlando.",
             [{"cut": "DOWN", "at": 0.1}]),
        reps(["3 X 12"], "Un minuto de pausa",
             "Tres series de diez a doce, con un minuto de pausa. Si las doce salen fáciles, subí peso.",
             ["1 · BAJÁ", "2 · PAUSA", "3 · EXTENDÉ"], [C("START"), seqloop("DOWN", "START", 1.2, 1.8)]),
        step("AL TERMINAR", ["SOLTÁ", "LENTO"], "Sin rebotar",
             "Al terminar, dejá que la pila baje despacio y soltá las manijas sin rebotar.",
             [C("DOWN"), TO("START", 0.9, 2.0)],
             [lab((985, 1040), "SIN REBOTAR", "end", 1.0)], 6.5),
    ]


YT45 = {
    "titulo": "Lever Pullover 🔥 Jalón al pecho en máquina | Dorsales",
    "tags": ["lever pullover", "jalón al pecho", "máquina de palanca", "dorsales", "espalda",
             "tirón vertical", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de espalda"],
    "descripcion": yt_desc("Lever Pullover", "jalón en máquina de palanca",
        "dorsales y espalda media, sin cargar la lumbar",
        "El dorsal trabaja cuando el codo baja y va atrás, no cuando el brazo tira solo. Si encogés los hombros, el trabajo se va al trapecio.",
        ["Ajustá el asiento para que las manijas queden a la altura del pecho.",
         "Agarre prono, con los pulgares para adentro."],
        ["Sentate con la espalda apoyada y los codos bajos.",
         "Tirá las manijas al pecho llevando el codo al bolsillo.",
         "Apretá el dorsal un segundo, con el pecho arriba.",
         "Volvé lento, sin dejar que la pila pegue abajo."],
        ["Echarse atrás para ayudar → espalda en el respaldo y menos peso.",
         "Encorvar los hombros → hombros abajo y pecho arriba.",
         "Redondear la espalda → espalda apoyada y core activo."],
        ["Pecho arriba y mirada al frente.", "Codos bajos y cerca del cuerpo.",
         "Un segundo al pecho en cada repetición.", "Volvé lento, sin rebote."],
        "Espalda · Dorsales",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Dorsales #Espalda #Jalon #MaquinaDePalanca #Tiron #Entrenamiento")}

YT46 = {
    "titulo": "Lever Seated Good Morning 🔥 Buenos días sentado | Isquios",
    "tags": ["lever seated good morning", "buenos días sentado", "máquina de palanca", "isquiotibiales",
             "glúteos", "bisagra de cadera", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Lever Seated Good Morning", "buenos días sentado en máquina",
        "isquiotibiales y glúteos, con la espalda recta",
        "El movimiento es una bisagra de cadera: la espalda se mantiene recta y el torso baja desde la cadera. Si redondeás la espalda, el peso se va a la lumbar.",
        ["Ajustá el asiento para que la cadera quede un poco más alta que las rodillas.",
         "Pies planos y firmes, separados al ancho de los hombros."],
        ["Sentate con la espalda recta y las manos en las manijas del asiento.",
         "Inclinate desde la cadera llevando el pecho hacia los muslos.",
         "Bajá hasta que el torso quede paralelo al piso y hacé una pausa.",
         "Volvé empujando con los glúteos y los isquios."],
        ["Redondear la espalda → menos rango y espalda recta.",
         "Pasar el paralelo → frená cuando el torso queda paralelo.",
         "Mirar al piso → mirada al frente y cuello alineado."],
        ["Cadera un poco más alta que las rodillas.", "Bisagra desde la cadera, no desde la espalda.",
         "Bajá hasta el paralelo, sin más.", "Volvé empujando con el glúteo."],
        "Isquiotibiales · Glúteos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Isquios #Gluteos #BuenosDias #MaquinaDePalanca #Piernas #Entrenamiento")}

YT47 = {
    "titulo": "Lever Triceps Extension 🔥 Extensión de tríceps en máquina | Brazos",
    "tags": ["lever triceps extension", "extensión de tríceps", "tríceps en máquina", "máquina de palanca",
             "tríceps", "brazos", "extensión sobre la cabeza", "máquinas de gimnasio", "gimnasio",
             "principiantes", "rutina de brazos"],
    "descripcion": yt_desc("Lever Triceps Extension", "extensión de tríceps en máquina de palanca",
        "tríceps fuertes, con el codo quieto y sin cargar el hombro",
        "El tríceps trabaja cuando el codo queda fijo y el antebrazo es lo único que se mueve. Si movés los codos o te echás atrás, el trabajo se reparte y el tríceps no se lleva nada. Este video es para vos. 💪",
        ["Ajustá el asiento para que la manija quede a la altura del hombro y el codo apoye en el eje de la palanca.",
         "Elegí el peso con el pasador: uno que puedas mover 12 veces sin despegar la espalda."],
        ["Sentate con la espalda apoyada y los pies planos.",
         "Con los codos quietos, bajá las manijas lento hacia la frente.",
         "Hacé una pausa corta, cerca de la frente.",
         "Extendé los brazos hacia adelante y arriba apretando el tríceps."],
        ["Echarse atrás y arquear la espalda → espalda pegada al respaldo.",
         "Dejar caer el peso de golpe → bajá y volvé controlando, sin rebotar.",
         "Extender a medias → estirá casi por completo el codo."],
        ["Codos quietos, pegados al eje de la máquina.", "Bajá hasta la frente, sin más.",
         "Extendé completo y apretá un segundo.", "Arrancá con poco peso: acá la técnica se rompe rápido."],
        "Tríceps · Hombros",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Triceps #Brazos #MaquinaDePalanca #ExtensionDeTriceps #Musculacion #Entrenamiento")}

save("lever-pullover", pl_scenes("lever-pullover"),
     {"pose": "START", "zoom": 1.12, "dy": 110}, YT45)

save("lever-seated-good-morning", gm_scenes("lever-seated-good-morning"),
     {"pose": "UP", "zoom": 1.12, "dy": 110}, YT46)

save("lever-triceps-extension", te_scenes("lever-triceps-extension"),
     {"pose": "START", "zoom": 1.12, "dy": 110}, YT47)
