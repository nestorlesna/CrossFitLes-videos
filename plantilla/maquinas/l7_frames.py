# Lote 7 · máquinas nuevas: escenas + YouTube + miniatura (multicadera de pie y press múltiple).
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

# ═════════════ MULTI HIP MACHINE ═════════════
s, S, J = load("multi-hip-machine"); pr = s["props"][0]
pv = pr["pivot"]
PV, KNOB, DISCPIN = S(*pv), S(pv[0] - 150, pv[1] + 100), S(pv[0], pv[1] + 44)
ROLL_B, ROLL_S = S(pv[0] - 52, pv[1] + pr["at"]), S(pv[0], pv[1] + pr["at"])
HANDLE, PINP = S(*pr["handle"]), S(*PIN(pr["stack"], pr["pin"]))
LT, LR1, LR2 = (130, 760), (1000, 860), (1000, 920)   # izquierda arriba de la máquina / derecha a la altura de la cabeza
TVA = lambda: {"mode": "hip", "pads": "out", "label": "ABRÍ LA PIERNA"}
TVD = lambda: {"mode": "hip", "pads": "in", "label": "CERRÁ LA PIERNA"}
TVB = lambda: {"mode": "hip", "pads": "out", "label": "ABRÍ DE MÁS"}
KB = lambda at=0.5: seqloop("KB_TOP", "KB_START", 1.4, 1.4, at)
F = [
    hook("GIMNASIO · GLÚTEOS", ["MULTI HIP", "MACHINE"], "Máquina multicadera de pie",
         "Multi Hip Machine: la multicadera de pie. Una sola máquina para cuatro ejercicios de cadera y glúteos.",
         [C("KB_START"), KB()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "También: multi-hip",
         "También le dicen multi-hip. Sirve para patada atrás, abrir la pierna, cerrarla y subir la rodilla.",
         [C("KB_START")], [lab(LT, "PILA DE PESO", "start", 0.8), ring(PV, 70, 1.6), lab(LR1, "EJE Y DISCO", "end", 1.6),
                           ring(ROLL_B, 46, 2.6), lab(LR2, "RODILLO", "end", 2.6)], 7.4),
    step("AJUSTE 1", ["ALTURA", "DEL EJE"], "A la altura de tu cadera",
         "Subí o bajá el eje hasta que quede justo a la altura de tu cadera. Es el ajuste más importante.",
         [C("KB_START")], [ring(KNOB, 26, 0.8), ring(PV, 70, 1.6), lab(LR1, "EJE = CADERA", "end", 1.6)], 7.0),
    step("AJUSTE 2", ["EL", "RODILLO"], "Arriba de la rodilla",
         "El rodillo va a la altura de la pierna, justo arriba de la rodilla. Nunca sobre el tobillo.",
         [C("KB_START")], [ring(ROLL_B, 50, 0.8), lab(LR1, "ARRIBA DE LA RODILLA", "end", 1.2)], 7.0),
    step("AJUSTE 3", ["EL", "DISCO"], "Regula el ángulo",
         "El disco con agujeros regula el ángulo: elegí desde dónde arranca la palanca y trabá el pasador.",
         [C("KB_START")], [ring(PV, 74, 0.8), ring(DISCPIN, 18, 1.6), lab(LR1, "PASADOR DEL ÁNGULO", "end", 1.6)], 7.0),
    step("AJUSTE 4", ["EL", "PESO"], "Empezá liviano",
         "Elegí el peso con el pasador de la pila. Empezá liviano: son músculos chicos que se cansan rápido.",
         [C("KB_START")], [ring(PINP, 30, 0.8), lab(LT, "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["DE", "COSTADO"], "Agarrado de la manija",
         "Parate de costado a la máquina, agarrate de la manija y dejá la pierna de apoyo apenas flexionada.",
         [C("KB_START")], [ring(HANDLE, 40, 1.0), lab(LR1, "MANIJA", "end", 1.0), lab(LR2, "TRONCO QUIETO", "end", 2.2)]),
    step("USO 1 / 4", ["PATADA", "ATRÁS"], "Rodillo atrás del muslo",
         "Uno: patada de glúteo. Con el rodillo atrás del muslo, llevá la pierna hacia atrás y volvé lento.",
         [C("KB_START"), KB(0.4)], [lab(LR1, "APRETÁ EL GLÚTEO", "end", 1.0)], 7.6, numeral="1"),
    step("USO 2 / 4", ["ABRÍ"], "Abducción: rodillo afuera",
         "Dos: abducción. Con el rodillo del lado de afuera, abrí la pierna al costado y volvé sin golpe.",
         [C("AB_START"), seqloop("AB_OUT", "AB_START", 1.4, 1.4, 0.4)], [lab(LT, "RODILLO AFUERA", "start", 1.0)], 7.6,
         numeral="2", topview=TVA()),
    step("USO 3 / 4", ["CERRÁ"], "Aducción: rodillo adentro",
         "Tres: aducción. Con el rodillo del lado de adentro, arrancá abierto y cerrá la pierna cruzando apenas.",
         [C("AD_START"), seqloop("AD_IN", "AD_START", 1.4, 1.4, 0.4)], [lab(LT, "RODILLO ADENTRO", "start", 1.0)], 7.6,
         numeral="3", topview=TVD()),
    step("USO 4 / 4", ["SUBÍ LA", "RODILLA"], "Rodillo arriba del muslo",
         "Cuatro: elevación de rodilla. Con el rodillo arriba del muslo, subí la rodilla hasta la altura de la cadera.",
         [C("KR_START"), seqloop("KR_TOP", "KR_START", 1.4, 1.4, 0.4)], [lab(LR1, "HASTA LA CADERA", "end", 1.0)], 7.6, numeral="4"),
    step("ASÍ NO · 1 / 4", ["LUMBAR", "ARQUEADA"], "La patada sale del glúteo",
         "Error: llevar la pierna tan atrás que se arquea la lumbar. Recorrido corto: la patada sale del glúteo.",
         [C("KB_START"), TO("KB_BAD", 0.5, 1.0)], [NO(), ring(S(*J["KB_BAD"]["H"]), 64, 1.4)], 7.4),
    step("ASÍ NO · 2 / 4", ["TRONCO", "ENCORVADO"], "Subí solo la rodilla",
         "Error: encorvar el tronco para subir más la rodilla. Pecho alto y la rodilla solo hasta la cadera.",
         [C("KR_START"), TO("KR_BAD", 0.5, 1.0)], [NO(), ring(S(*J["KR_BAD"]["S"]), 64, 1.4)], 7.4),
    step("ASÍ NO · 3 / 4", ["CON", "IMPULSO"], "Lento y controlado",
         "Error: balancear el cuerpo para mover la pierna con impulso. Bajá el peso y hacelo lento.",
         [C("KB_START"), {"seq": [["SWING_BAD", 0.35], ["KB_START", 0.35]], "at": 0.4, "until": 3.6}, TO("SWING_BAD", 3.7, 0.4)],
         [NO(), lab(LR1, "SIN CONTROL", "end", 1.0)], 7.4),
    step("ASÍ NO · 4 / 4", ["ABRIR", "DE MÁS"], "Un rango cómodo",
         "Error: abrir la pierna más de lo que da tu cadera, inclinando el tronco. Abrí hasta donde llegás derecho.",
         [C("AB_START"), TO("AB_BAD", 0.5, 1.0)], [NO(pos=(300, 760))], 7.4, topview=TVB()),
    keys("TIPS DEL PROFE", ["TIPS"], ["Eje a la altura de la cadera", "Rodillo arriba de la rodilla", "Solo se mueve la pierna", "Todas las reps y cambiá"],
         "Tips de profe: eje a la altura de la cadera, rodillo arriba de la rodilla, y hacé todas las reps de una pierna antes de cambiar.",
         [C("KB_START"), KB()]),
    keys("CLAVES", ["TÉCNICA"], ["Agarrado de la manija", "Tronco quieto", "Recorrido corto", "Sin que choque la pila"],
         "Claves: agarrado de la manija, tronco quieto, recorrido corto y sin que la pila choque.",
         [{"cut": "KB_TOP", "at": 0.1}]),
    reps(["3 X 15"], "Por pierna, en cada ejercicio",
         "Tres series de doce a quince por pierna, con un minuto de pausa. Cuando salen fáciles, subí una placa.",
         ["1 · AJUSTÁ EL EJE", "2 · MOVÉ LA PIERNA", "3 · VOLVÉ LENTO"], [C("KB_START"), KB()]),
]
save("multi-hip-machine", F, {"pose": "KB_TOP", "grip": 1, "zoom": 1.0, "dy": 150}, {
    "titulo": "Multi Hip Machine 🔥 Multicadera: 4 ejercicios de glúteos y cadera | Gimnasio",
    "tags": ["multi hip", "máquina multicadera", "multicadera", "patada de glúteo en máquina", "abducción de cadera de pie", "aducción de cadera",
             "elevación de rodilla", "glúteos", "glúteo medio", "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Multi Hip Machine", "máquina multicadera de pie", "cuatro ejercicios de cadera en una sola máquina",
        "¿Viste esa máquina con un disco con agujeros y un rodillo, y no sabés cómo se usa? Sirve para cuatro ejercicios. Este video es para vos.",
        ["Subí o bajá el eje hasta que quede a la altura de tu cadera.", "Poné el rodillo justo arriba de la rodilla, nunca en el tobillo.",
         "Con el disco con agujeros elegí el ángulo de arranque y trabá el pasador.", "Elegí un peso liviano con el pasador de la pila."],
        ["Parate de costado a la máquina, agarrado de la manija, con la pierna de apoyo apenas flexionada.",
         "Patada de glúteo: rodillo atrás del muslo, llevá la pierna hacia atrás y volvé lento.",
         "Abducción: rodillo del lado de afuera, abrí la pierna al costado y volvé sin golpe.",
         "Aducción: rodillo del lado de adentro, arrancá abierto y cerrá la pierna cruzando apenas.",
         "Elevación de rodilla: rodillo arriba del muslo, subí la rodilla hasta la altura de la cadera."],
        ["Eje más alto o más bajo que la cadera → alinealo con la cadera antes de empezar.",
         "Arquear la lumbar en la patada atrás → recorrido corto, la patada sale del glúteo.",
         "Encorvar o inclinar el tronco para subir más la pierna → tronco quieto y rango cómodo.",
         "Balancear y usar impulso → menos peso y movimiento lento.", "Dejar que la pila choque entre repeticiones → volvé controlado."],
        ["Eje de la máquina a la altura de la cadera.", "Rodillo justo arriba de la rodilla, no en el tobillo.",
         "Agarrate de la manija y tronco quieto: solo se mueve la pierna.", "Recorrido corto y controlado: el glúteo trabaja, no la lumbar.",
         "Hacé todas las reps de una pierna y después cambiá."],
        "Glúteo mayor · Glúteo medio · Aductores · Flexores de cadera · Core",
        "3 series de 12–15 repeticiones por pierna en cada ejercicio, con 1 minuto de pausa. Cuando salen fáciles, subí una placa. Nivel: principiante.",
        "#Gimnasio #MultiHip #Gluteos #Musculacion #Entrenamiento")})

# ═════════════ MULTI PRESS MACHINE ═════════════
s, S, J = load("multi-press-machine"); pr = s["props"][0]
rx0, ry0, rx1, ry1 = pr["rail"]
r0, r1 = (rx0 + 10, ry0 + 130), (rx1 - 40, ry1 + 150); mid = ((r0[0] + r1[0]) / 2 + 40, (r0[1] + r1[1]) / 2 + 60)
def railp(hx):
    t = (hx - rx0) / (rx1 - rx0); q = 1 - t
    return (q * q * r0[0] + 2 * q * t * mid[0] + t * t * r1[0], q * q * r0[1] + 2 * q * t * mid[1] + t * t * r1[1])
KN = {k: S(*railp(J[k]["H"][0])) for k in ("SH_DOWN", "IN_DOWN", "CH_DOWN")}
PINP = S(*PIN(pr["stack"], pr["pin"]))
W = lambda k: S(*J[k]["W"])
L1, L2, L3 = (130, 820), (130, 890), (130, 960)   # margen izquierdo, arriba del respaldo
CH = lambda at=0.5: seqloop("CH_UP", "CH_DOWN", 1.0, 2.0, at)
F = [
    hook("GIMNASIO · PECHO", ["MULTI", "PRESS"], "Press múltiple",
         "Multi Press Machine: el press múltiple. Una máquina, tres ejercicios: pecho, inclinado y hombros.",
         [C("CH_DOWN"), CH()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Asiento que corre en el riel",
         "Es una máquina de press con el asiento sobre un riel. Trabaja pectorales y hombros, y suma tríceps.",
         [C("CH_DOWN")], [ring(KN["CH_DOWN"], 30, 0.8), lab(L1, "RIEL DEL ASIENTO", "start", 0.8), ring(W("CH_DOWN"), 36, 1.8),
                          lab(L2, "MANIJAS", "start", 1.8), ring(PINP, 30, 2.8), lab(L3, "PILA A LA DERECHA", "start", 2.8)], 7.4),
    step("AJUSTE 1", ["EL", "ÁNGULO"], "Pecho · inclinado · hombros",
         "Corré el asiento: bien reclinado es press de pecho, en el medio inclinado y casi derecho, hombros.",
         [C("CH_DOWN"), TO("IN_DOWN", 1.8, 1.2), TO("SH_DOWN", 4.0, 1.2)],
         [lab(L1, "1 · PECHO", "start", 0.6), lab(L2, "2 · INCLINADO", "start", 2.2), lab(L3, "3 · HOMBROS", "start", 4.4)], 7.6),
    step("AJUSTE 2", ["EL", "PASADOR"], "Mirá los dibujos de la placa",
         "Los tres dibujos de la placa te muestran cada posición. Elegí una y trabá el pasador del riel.",
         [C("SH_DOWN")], [ring(KN["SH_DOWN"], 30, 0.8), lab(L1, "TRABÁ EL PASADOR", "start", 1.0)], 7.0),
    step("AJUSTE 3", ["EL", "PESO"], "Con el pasador de la pila",
         "Elegí el peso con el pasador de la pila: uno que puedas empujar doce veces sin despegar la espalda.",
         [C("CH_DOWN")], [ring(PINP, 30, 0.8), lab(L1, "PASADOR DE LA PILA", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["ESPALDA", "PEGADA"], "Escápulas juntas, pecho alto",
         "Sentate con la espalda pegada al respaldo, juntá las escápulas y agarrá las manijas.",
         [C("CH_DOWN")], [lab(L1, "ESCÁPULAS JUNTAS", "start", 1.0), ring(W("CH_DOWN"), 36, 2.0)]),
    step("PECHO · 1 / 2", ["EMPUJÁ"], "Respaldo bien reclinado",
         "Press de pecho, con el respaldo bien reclinado. Empujá las manijas hacia arriba sin trabar los codos.",
         [C("CH_DOWN"), TO("CH_UP", 0.6, 1.2)], [arrow((W("CH_DOWN")[0] + 40, W("CH_DOWN")[1] - 20), (W("CH_UP")[0] + 40, W("CH_UP")[1]), 0.8, 1.0)], numeral="1"),
    step("PECHO · 2 / 2", ["VOLVÉ", "LENTO"], "Sin apoyar el peso",
         "Volvé lento hasta sentir que estira el pecho, sin que las placas se apoyen.",
         [C("CH_UP"), TO("CH_DOWN", 0.6, 2.4)], [ring(PINP, 34, 2.0), lab(L1, "SIN APOYAR", "start", 2.0)], numeral="1"),
    step("INCLINADO · 1 / 2", ["EMPUJÁ"], "Asiento en el medio",
         "Press inclinado, con el asiento en el medio. Empujá hacia arriba y adelante, con los codos bajo las manos.",
         [C("IN_DOWN"), TO("IN_UP", 0.6, 1.2)], [arrow((W("IN_DOWN")[0] + 40, W("IN_DOWN")[1] - 20), (W("IN_UP")[0] + 40, W("IN_UP")[1]), 0.8, 1.0)], numeral="2"),
    step("INCLINADO · 2 / 2", ["BAJÁ", "AL PECHO"], "Parte alta del pecho",
         "Bajá controlado hasta que las manijas lleguen a la parte alta del pecho y volvé a empujar.",
         [C("IN_UP"), TO("IN_DOWN", 0.6, 2.4)], [ring(W("IN_DOWN"), 40, 2.2), lab(L1, "PARTE ALTA DEL PECHO", "start", 2.2)], numeral="2"),
    step("HOMBROS · 1 / 2", ["EMPUJÁ", "ARRIBA"], "Respaldo casi derecho",
         "Press de hombros, con el respaldo casi derecho. Empujá hacia arriba sin arquear la espalda.",
         [C("SH_DOWN"), TO("SH_UP", 0.6, 1.2)], [arrow((W("SH_DOWN")[0] + 50, W("SH_DOWN")[1]), (W("SH_UP")[0] + 50, W("SH_UP")[1] + 40), 0.8, 1.0)], numeral="3"),
    step("HOMBROS · 2 / 2", ["BAJÁ", "AL HOMBRO"], "No más abajo",
         "Bajá controlado hasta que las manijas lleguen a la altura de los hombros, no más abajo.",
         [C("SH_UP"), TO("SH_DOWN", 0.6, 2.4)], [ring(W("SH_DOWN"), 40, 2.2), lab(L1, "HASTA EL HOMBRO", "start", 2.2)], numeral="3"),
    step("ASÍ NO · 1 / 3", ["ESPALDA", "ARQUEADA"], "La lumbar pegada",
         "Error: arquear la espalda para empujar más. La zona lumbar sufre: apretá el abdomen y bajá el peso.",
         [C("SH_DOWN"), TO("ARCH_BAD", 0.5, 1.0)], [NO(pos=(300, 780)), ring(S(*J["ARCH_BAD"]["H"]), 60, 1.4)], 7.2),
    step("ASÍ NO · 2 / 3", ["CODOS", "TRABADOS"], "Casi estirado, nunca trabado",
         "Error: trabar los codos de golpe arriba. Llegá casi estirado y empezá a volver.",
         [C("CH_DOWN"), TO("LOCK_BAD", 0.5, 0.5)], [NO(pos=(300, 780)), ring(S(*J["LOCK_BAD"]["E"]), 40, 1.4)], 7.2),
    step("ASÍ NO · 3 / 3", ["DE", "GOLPE"], "Que la pila no choque",
         "Error: bajar de golpe y dejar que la pila choque. Volvé en dos o tres segundos, con control.",
         [C("CH_UP"), {"seq": [["CH_DOWN", 0.3], ["CH_UP", 0.3]], "at": 0.4, "until": 3.6}, TO("CH_DOWN", 3.7, 0.3)],
         [NO(pos=(300, 780)), ring(PINP, 34, 1.4), lab(L2, "SIN CONTROL", "start", 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Elegí la posición en la placa", "Trabá el pasador del riel", "Escápulas juntas", "Volvé sin tocar la pila"],
         "Tips de profe: elegí la posición mirando la placa, trabá el pasador, escápulas juntas y volvé sin tocar la pila.",
         [C("CH_DOWN"), CH()]),
    keys("CLAVES", ["TÉCNICA"], ["Espalda pegada", "Pies firmes en el piso", "Sin trabar los codos", "Volvé lento"],
         "Claves: espalda pegada, pies firmes en el piso, sin trabar los codos y volvé lento.",
         [{"cut": "IN_UP", "at": 0.1}]),
    reps(["3 X 12"], "Un minuto y medio de pausa",
         "Tres series de diez a doce, con un minuto y medio de pausa. Cuando las doce salen fáciles, subí una placa.",
         ["1 · ELEGÍ EL ÁNGULO", "2 · EMPUJÁ", "3 · VOLVÉ LENTO"], [C("CH_DOWN"), CH()]),
]
save("multi-press-machine", F, {"pose": "IN_UP", "grip": 1, "zoom": 1.05, "dy": 120}, {
    "titulo": "Multi Press Machine 🔥 Press de pecho, inclinado y hombros en una máquina | Gimnasio",
    "tags": ["multi press", "press múltiple", "paramount multi press", "press de pecho en máquina", "press inclinado en máquina",
             "press de hombros en máquina", "pecho", "hombros", "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Multi Press Machine", "press múltiple", "pecho, inclinado y hombros en una sola máquina",
        "¿El asiento se mueve y no sabés en qué posición ponerlo? Cada posición es un ejercicio distinto. Este video es para vos.",
        ["Corré el asiento sobre el riel: bien reclinado = press de pecho, en el medio = press inclinado, casi derecho = press de hombros (son los tres dibujos de la placa).",
         "Trabá el pasador del riel en la posición elegida.", "Elegí con el pasador de la pila un peso que puedas empujar 12 veces sin despegar la espalda."],
        ["Espalda pegada al respaldo, escápulas juntas y manijas en las manos.",
         "Press de pecho: empujá hacia arriba sin trabar los codos y volvé lento hasta sentir estirar el pecho.",
         "Press inclinado: empujá hacia arriba y adelante, con los codos debajo de las manos, y bajá a la parte alta del pecho.",
         "Press de hombros: empujá hacia arriba sin arquear la espalda y bajá hasta la altura de los hombros."],
        ["No trabar bien el pasador del riel → trabalo siempre antes de cargar.", "Despegar la espalda o arquear la lumbar → abdomen firme y menos peso.",
         "Trabar los codos arriba → casi estirado, nunca trabado.", "Bajar de golpe hasta que la pila choque → volvé en 2–3 segundos."],
        ["Elegí la posición mirando la placa: pecho, inclinado u hombros.", "Trabá el pasador del asiento antes de cargar.",
         "Espalda pegada al respaldo, escápulas juntas.", "Empujá sin trabar los codos.", "Volvé en 2–3 segundos sin apoyar el peso."],
        "Pectorales · Deltoides · Tríceps · Hombros anteriores",
        "3 series de 10–12 repeticiones, con 1 minuto y medio de pausa. Cuando las 12 salen fáciles, subí una placa. Nivel: principiante.",
        "#Gimnasio #MultiPress #Pecho #Musculacion #Entrenamiento")},
    extra={"pronuncia": {"press": "pres", "Press": "Pres"}})
