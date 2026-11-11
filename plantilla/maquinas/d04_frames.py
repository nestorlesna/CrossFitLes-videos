# Dataset D01 · D7 Lever Back Extension y D8 Lever Reverse Hyperextension: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.4, tb=1.2, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}
PIN = lambda cx, pin: (cx + 51, -254 + (pin - 0.5) * 22)


# ═════════════ D7 · LEVER BACK EXTENSION ═════════════
s, S, J = load("lever-back-extension"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); SEAT = S(pr["seat"][0] + 110, pr["seat"][2])
PADP = S(J["UP"]["S"][0] - 30, J["UP"]["S"][1] + 30); FEET = S(*pr["feet"])
HEAD = S(*J["DEEP"]["N"]); BADBACK = S(*J["ROUND_BAD"]["N"]); LB, LT = (130, 880), (1000, 900)
L = lambda: seqloop("DEEP", "UP", 1.2, 2.0)
F = [
    hook("GIMNASIO · ESPALDA BAJA", ["EXTENSIÓN", "LUMBAR"], "En máquina de palanca",
         "Lever Back Extension: la extensión lumbar en máquina de palanca, sentado y con la espalda apoyada.",
         [C("UP"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Almohadilla y pila",
         "La almohadilla apoya en la espalda alta y la palanca mueve la pila. Trabaja la zona lumbar y los glúteos.",
         [C("UP")], [ring(PADP, 50, 0.8), lab(LT, "ALMOHADILLA", "end", 0.8),
                     ring(SEAT, 44, 1.8), lab(LB, "ASIENTO", "start", 1.8),
                     ring(PINP, 30, 2.8), lab((130, 1250), "PASADOR", "start", 2.8)], 7.0),
    step("AJUSTE 1", ["ALTURA", "DEL ASIENTO"], "Espalda cómoda",
         "Ajustá el asiento para que la almohadilla quede en la espalda alta, cómoda y sin apretar el cuello.",
         [C("UP")], [ring(SEAT, 44, 0.8), ring(PADP, 50, 1.8), lab(LT, "ALMOHADILLA ALTA", "end", 1.4)], 7.0),
    step("AJUSTE 2", ["PESO", "MODERADO"], "Con el pasador",
         "Elegí un peso moderado con el pasador. Si necesitás impulso para volver, es demasiado.",
         [C("UP")], [ring(PINP, 30, 0.8), lab(LB, "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["SENTADO", "FIRME"], "Pies fijos",
         "Sentate con la espalda en la almohadilla y los pies firmes en el piso. Tomá las asas con las manos.",
         [C("UP")], [ring(FEET, 36, 0.8), lab(LT, "PIES FIRMES", "end", 1.0)], 7.0),
    step("PASO 1 / 3", ["INCLINATE", "DESPACIO"], "Adelante, sin rebotar",
         "Paso uno. Activá el core e inclinate despacio hacia adelante, dejando que la espalda se redondee apenas.",
         [C("UP"), TO("FWD", 0.6, 1.1), TO("DEEP", 1.7, 0.9)],
         [lab(LT, "LLEVÁ EL PECHO ABAJO", "end", 1.4)], numeral="1"),
    step("PASO 2 / 3", ["PAUSA", "ABAJO"], "Un segundo",
         "Paso dos. Hacé una pausa breve abajo y sentí el estiramiento en la zona lumbar, sin rebotar.",
         [C("DEEP")], [ring(HEAD, 46, 0.8), lab(LT, "ESTIRÁ SIN REBOTAR", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ CON", "LA ESPALDA"], "Sin tirar con brazos",
         "Paso tres. Volvé subiendo el torso con los músculos de la espalda, sin tirar con los brazos.",
         [C("DEEP"), TO("UP", 0.6, 2.2)], [lab(LB, "SIN TIRAR CON BRAZOS", "start", 1.0)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al volver",
         "Tomá aire al inclinarte y soltalo al volver. No aguantes el aire abajo.",
         [C("UP"), seqloop("DEEP", "UP", 1.2, 2.2, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["REDONDEAR", "LA ESPALDA"], "Curva suave",
         "Error: redondear mucho la espalda. Es una curva suave, no una joroba: el pecho queda abierto.",
         [C("UP"), TO("ROUND_BAD", 0.5, 0.9)], [NO(), ring(BADBACK, 46, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["PASARTE", "DE LARGO"], "Sin arquear",
         "Error: volver demasiado y arquear la lumbar. Volvé hasta quedar derecho, no más allá.",
         [C("UP"), TO("HYPER_BAD", 0.5, 0.9)], [NO(1.0), lab(LT, "SIN ARQUEAR", "end", 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Almohadilla en la espalda alta", "Pies firmes en el piso", "Curva suave al bajar",
                                     "Volvé con la espalda"],
         "Tips de profe: almohadilla en la espalda alta, pies firmes, curva suave al bajar y volvé con la espalda.",
         [C("UP"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Asiento a tu altura", "Bajá despacio", "Curva suave, sin joroba",
                                "No arquees de más"],
         "Claves: asiento a tu altura, bajá despacio, curva suave sin joroba y no arquees de más.",
         [{"cut": "DEEP", "at": 0.1}]),
    reps(["3 X 12-15"], "Un minuto de pausa",
         "Tres series de doce a quince, con un minuto de pausa. Subí una placa cuando las quince salgan fáciles.",
         ["1 · INCLINATE", "2 · PAUSÁ", "3 · VOLVÉ LENTO"], [C("UP"), L()]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, volvé despacio, soltá las asas y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("UP"), TO("DEEP", 1.0, 1.2), TO("UP", 2.4, 1.4)], [lab(LB, "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-back-extension", F, {"pose": "DEEP", "grip": 0, "zoom": 1.15, "dy": 110}, {
    "titulo": "Lever Back Extension 🔥 Extensión lumbar en máquina de palanca | Gimnasio",
    "tags": ["lever back extension", "extensión lumbar en máquina", "extensión de espalda", "máquina de palanca",
             "lumbares", "espalda baja", "glúteos", "core", "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Lever Back Extension", "extensión lumbar en máquina de palanca",
        "espalda baja fuerte sin cargar la columna",
        "¿Sentís la lumbar cansada y no sabés cómo entrenarla? Esta máquina te deja trabajar la espalda baja con control. Este video es para vos.",
        ["Ajustá el asiento para que la almohadilla quede en la espalda alta.", "Elegí un peso moderado con el pasador."],
        ["Sentate con la espalda en la almohadilla y los pies firmes.", "Activá el core e inclinate despacio hacia adelante.",
         "Pausá abajo un segundo, sintiendo el estiramiento lumbar.", "Volvé subiendo el torso con la espalda, sin tirar con los brazos."],
        ["Redondear mucho la espalda → curva suave, pecho abierto.", "Arquear la lumbar al volver → volvé hasta quedar derecho.",
         "Tirar con los brazos → volvé con la espalda."],
        ["Almohadilla en la espalda alta, no en el cuello.", "Pies firmes en el piso.", "Bajá despacio y pausá abajo.",
         "Volvé con la espalda, no con los brazos.", "Peso moderado: si necesitás impulso, es mucho."],
        "Lumbares · Glúteos · Isquiotibiales",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #LeverBackExtension #EspaldaBaja #Lumbares #Musculacion #Entrenamiento")})

# ═════════════ D8 · LEVER REVERSE HYPEREXTENSION ═════════════
s, S, J = load("lever-reverse-hyperextension"); pr = s["props"][0]
PADP = S(*pr["pad"]); FOOTP = S(*pr["foot"])
HIPT = S(*J["TOP"]["H"]); KNEET = S(*J["TOP"]["K"]); ANKT = S(*J["TOP"]["A"])
BADSH = S(*J["HIP_BAD"]["S"]); ARCHSH = S(*J["ARCH_BAD"]["S"])
LB, LT = (130, 760), (1000, 760)
L = lambda: seqloop("REST", "TOP", 1.0, 1.8)
F = [
    hook("GIMNASIO · GLÚTEOS", ["REVERSE", "HYPER"], "Piernas hacia arriba",
         "Lever Reverse Hyperextension: la extensión inversa, boca abajo, para glúteos e isquiotibiales.",
         [C("REST"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Almohadilla en la cadera",
         "La cadera va en el borde de la almohadilla y las piernas cuelgan libres. Trabaja glúteos e isquiotibiales.",
         [C("REST")], [ring(PADP, 50, 0.8), lab(LT, "ALMOHADILLA", "end", 0.8),
                       ring(FOOTP, 40, 1.6), lab(LB, "APOYO DE PIES", "start", 1.6)], 7.0),
    step("AJUSTE 1", ["ALTURA", "DE LA CADERA"], "En el borde",
         "Ajustá la máquina para que la cadera quede en el borde de la almohadilla y las piernas cuelguen libres.",
         [C("REST")], [ring(PADP, 50, 0.8), lab(LT, "CADERA EN EL BORDE", "end", 1.2)], 7.0),
    step("AJUSTE 2", ["PESO", "MODERADO"], "Brazos cruzados",
         "Cruzate los brazos sobre el pecho o tomá las asas. Elegí un peso moderado para empezar.",
         [C("REST")], [lab(LB, "BRAZOS CRUZADOS", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["BOCA", "ABAJO"], "Cuerpo en línea",
         "Apoyá la cadera en la almohadilla, el torso firme y las piernas colgando, sin arquear la lumbar.",
         [C("REST")], [lab(LT, "SIN ARQUEAR", "end", 1.0)], 7.0),
    step("PASO 1 / 3", ["SUBÍ LAS", "PIERNAS"], "Con los glúteos",
         "Paso uno. Activá los glúteos y subí las piernas hasta quedar en línea con el torso.",
         [C("REST"), TO("MID", 0.5, 0.9), TO("TOP", 1.4, 1.2)],
         [ring(ANKT, 44, 1.6), lab(LT, "PIERNAS EN LÍNEA", "end", 1.4)], numeral="1"),
    step("PASO 2 / 3", ["APRETÁ", "ARRIBA"], "Un segundo",
         "Paso dos. Arriba, apretá los glúteos un segundo sin arquear la lumbar.",
         [C("TOP")], [ring(HIPT, 56, 0.8), lab(LT, "APRETÁ LOS GLÚTEOS", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Sin hamacarte",
         "Paso tres. Bajá las piernas lento, sin dejarlas caer de golpe.",
         [C("TOP"), TO("REST", 0.6, 2.2)], [lab(LB, "SIN DEJAR CAER", "start", 1.0)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
         "Soltá el aire al subir las piernas y tomá aire al bajarlas.",
         [C("REST"), seqloop("TOP", "REST", 1.4, 2.0, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["IMPULSO DE", "CADERA"], "Sin hamacarte",
         "Error: hamacarte y usar impulso. Subí con los glúteos, sin mover el torso.",
         [C("REST"), TO("HIP_BAD", 0.5, 0.9)], [NO(), ring(BADSH, 50, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["ARQUEAR", "LA LUMBAR"], "Costillas abajo",
         "Error: arquear la lumbar para subir más. Las costillas quedan abajo y el movimiento sale de la cadera.",
         [C("REST"), TO("ARCH_BAD", 0.5, 0.9)], [NO(1.0), ring(ARCHSH, 50, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Cadera en el borde", "Costillas abajo", "Subí con los glúteos", "Bajá sin soltar"],
         "Tips de profe: cadera en el borde, costillas abajo, subí con los glúteos y bajá sin soltar.",
         [C("REST"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Cadera en el borde", "Piernas en línea", "Sin arquear la lumbar", "Bajada lenta"],
         "Claves: cadera en el borde, piernas en línea, sin arquear la lumbar y bajada lenta.",
         [{"cut": "TOP", "at": 0.1}]),
    reps(["3 X 12-15"], "Un minuto de pausa",
         "Tres series de doce a quince, con un minuto de pausa. Subí una placa cuando las quince salgan fáciles.",
         ["1 · SUBÍ", "2 · APRETÁ", "3 · BAJÁ LENTO"], [C("REST"), L()]),
    step("AL TERMINAR", ["BAJÁ CON", "CONTROL"], "Y salí despacio",
         "Al terminar, bajá las piernas despacio y salí de la máquina apoyando las manos.",
         [C("REST"), TO("MID", 0.8, 0.9), TO("REST", 1.8, 0.9)], [lab(LB, "SALÍ DESPACIO", "start", 1.0)], 6.5),
]
save("lever-reverse-hyperextension", F, {"pose": "TOP", "grip": 0, "zoom": 1.0, "dy": 140}, {
    "titulo": "Lever Reverse Hyperextension 🔥 Extensión inversa para glúteos | Gimnasio",
    "tags": ["lever reverse hyperextension", "reverse hyperextension", "extensión inversa", "glúteos en máquina",
             "isquiotibiales", "glúteos", "espalda baja", "máquina de palanca", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Lever Reverse Hyperextension", "extensión inversa de piernas en máquina",
        "glúteos e isquiotibiales sin cargar la lumbar",
        "¿Buscás glúteos fuertes sin que la lumbar pague el precio? La extensión inversa es la respuesta. Este video es para vos.",
        ["Ajustá la cadera en el borde de la almohadilla.", "Cruzate los brazos y elegí un peso moderado."],
        ["Boca abajo, cadera en la almohadilla y piernas colgando.", "Activá los glúteos y subí las piernas en línea con el torso.",
         "Apretá un segundo arriba, sin arquear la lumbar.", "Bajá las piernas lento, sin dejarlas caer."],
        ["Hamacarte con impulso → subí con los glúteos, torso quieto.", "Arquear la lumbar → costillas abajo, movimiento de cadera.",
         "Dejar caer las piernas → bajada lenta y controlada."],
        ["Cadera en el borde de la almohadilla.", "Costillas abajo y core activo.", "Las piernas llegan en línea con el torso.",
         "Apretá los glúteos arriba.", "Bajá sin soltar el peso."],
        "Glúteos · Isquiotibiales · Lumbares",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #ReverseHyperextension #Gluteos #Isquiotibiales #Musculacion #Entrenamiento")})
