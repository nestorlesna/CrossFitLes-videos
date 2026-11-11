# Dataset D01 · D18 Lever Alternate Leg Press y D19 Lever Horizontal One Leg Press: escenas + YouTube + miniatura.
import sys, os, json, math
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def mpts(s, J):
    pr = s["props"][0]; S = Stage(s["rig"]); hip = pr["hip"]
    ang = rad(pr["ang"]); d = (math.cos(ang), -math.sin(ang)); n = (math.sin(ang), math.cos(ang))
    u = up(pr["lean"], 1); back = (-u[1], u[0]); sb = (hip[0] + back[0] * 62, hip[1] + back[1] * 62)
    at = lambda dd, kk: (hip[0] + d[0] * dd + n[0] * kk, hip[1] + d[1] * dd + n[1] * kk)
    A = J["BOTTOM"]["A"]
    return dict(back=S(sb[0] + u[0] * 150, sb[1] + u[1] * 150),
                plates=S(A[0] + d[0] * 158 + n[0] * 105, A[1] + d[1] * 158 + n[1] * 105),
                stop=S(*at(pr["stops"], 160)))


def seqloop(a, b, ta=1.1, tb=1.7, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


# ═════════════ D18 · LEVER ALTERNATE LEG PRESS ═════════════
s, S, J = load("lever-alternate-leg-press"); M = mpts(s, J)
HIP = S(*J["BOTTOM"]["H"]); KNEEB = S(*J["BOTTOM"]["K"]); KNEET = S(*J["TOP"]["K"])
ANKB = S(*J["BOTTOM"]["A"]); ANKT = S(*J["TOP"]["A"]); FAR = S(*s["poses"]["TOP"]["ankle2"])
KNEE_L = S(*J["LOCK_BAD"]["K"]); HIP_B = S(*J["HIP_BAD"]["H"])
F = [
    hook("GIMNASIO · PIERNAS", ["LEG", "PRESS"], "Prensa a una pierna",
         "Lever Alternate Leg Press: la prensa de palanca con una pierna por vez. Cuádriceps, isquiotibiales y glúteos.",
         [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Una pierna por vez",
         "La prensa de palanca: respaldo, plataforma para el pie y discos. Una pierna trabaja por vez.",
         [C("BOTTOM")], [ring(M["back"], 44, 0.8), lab((60, 1164), "RESPALDO", "start", 0.8),
                         ring(M["plates"], 46, 1.8), lab((985, 1195), "DISCOS", "end", 1.8),
                         ring(M["stop"], 30, 2.6), lab((60, 1370), "TOPE", "start", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "RESPALDO"], "Espalda bien apoyada",
         "Ajustá el respaldo para que la cadera y toda la espalda queden apoyadas. No dejes aire atrás.",
         [C("BOTTOM")], [ring(HIP, 44, 0.8), lab((60, 1300), "BIEN APOYADO", "start", 1.0)], 7.0),
    step("AJUSTE 2", ["EL", "ASIENTO"], "Rodilla a 90 grados",
         "Sentate y ajustá el asiento: al empezar, la rodilla tiene que quedar cerca de los noventa grados.",
         [C("BOTTOM")], [ring(KNEEB, 44, 0.8), lab((60, 1010), "RODILLA A 90°", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["UN PIE", "CENTRADO"], "La otra pierna afuera",
         "Apoyá un pie centrado en la plataforma y dejá la otra pierna en el piso. Agarrá las manijas.",
         [C("BOTTOM")], [ring(ANKB, 40, 0.8), lab((60, 1040), "UN PIE CENTRADO", "start", 1.0),
                         ring(FAR, 34, 1.8), lab((60, 1430), "OTRA PIERNA", "start", 1.8)], 7.0),
    step("PASO 1 / 3", ["EMPUJÁ"], "Sin apurar",
         "Paso uno. Empujá la plataforma con una pierna, extendiendo la rodilla sin apurarte.",
         [C("BOTTOM"), TO("MID", 0.6, 1.0), TO("TOP", 1.6, 1.0)],
         [arrow((ANKB[0] + 16, ANKB[1] - 16), (ANKT[0] - 6, ANKT[1] - 16), 0.8, 1.1),
          lab((60, 1010), "EMPUJÁ", "start", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["CASI", "ESTIRADA"], "Sin trabar la rodilla",
         "Paso dos. Llegá casi a estirar la pierna y hacé una pausa breve, sin trabar la rodilla.",
         [C("TOP")], [ring(KNEET, 46, 0.8), lab((60, 1010), "SIN TRABAR", "start", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Controlá la vuelta",
         "Paso tres. Flexioná la rodilla y volvé lento hasta la posición inicial, controlando el peso.",
         [C("TOP"), TO("BOTTOM", 0.6, 2.2)],
         [arrow((ANKT[0] - 6, ANKT[1] - 16), (ANKB[0] + 16, ANKB[1] - 16), 0.8, 1.1),
          lab((985, 1370), "CONTROLÁ", "end", 1.2)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al empujar",
         "Soltá el aire mientras empujás y tomalo cuando volvés. No aguantes el aire.",
         [C("BOTTOM"), seqloop("TOP", "BOTTOM", 1.1, 1.9, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["TRABAR", "LA RODILLA"], "Casi estirada",
         "Error: trabar o hiperextender la rodilla arriba. Llegá casi a estirar, sin bloquear la articulación.",
         [C("BOTTOM"), TO("LOCK_BAD", 0.5, 0.9)], [NO(), ring(KNEE_L, 50, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["DESPEGAR", "LA CADERA"], "Espalda apoyada",
         "Error: despegar la cadera y la espalda del respaldo para empujar. Quedá bien apoyado.",
         [C("BOTTOM"), TO("HIP_BAD", 0.5, 0.9)], [NO(), ring(HIP_B, 52, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Una pierna", "Espalda apoyada", "Sin trabar", "Volvé lento"],
         "Tips de profe: una pierna por vez, espalda apoyada, sin trabar la rodilla y volvé lento.",
         [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
    keys("CLAVES", ["TÉCNICA"], ["Pie centrado", "Rodilla alineada", "Sin impulso", "Bajá controlado"],
         "Claves: pie centrado, rodilla alineada con el pie, sin impulso y bajada controlada.",
         [{"cut": "TOP", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto de pausa",
         "Tres series de diez a doce por pierna, con un minuto de pausa. Alterná las piernas en cada serie.",
         ["1 · EMPUJÁ", "2 · PAUSÁ", "3 · VOLVÉ LENTO"], [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
    step("AL TERMINAR", ["CAMBIÁ", "DE PIERNA"], "Sin soltar de golpe",
         "Al terminar, volvé la plataforma despacio y cambiá de pierna. No dejes caer el peso.",
         [C("BOTTOM"), TO("MID", 1.0, 1.0), TO("BOTTOM", 2.2, 1.2)],
         [lab((60, 1010), "CAMBIÁ DE PIERNA", "start", 1.0)], 6.5),
]
save("lever-alternate-leg-press", F, {"pose": "TOP", "zoom": 1.15, "dy": 120}, {
    "titulo": "Lever Alternate Leg Press 🔥 Prensa a una pierna | Gimnasio",
    "tags": ["lever alternate leg press", "prensa a una pierna", "prensa de piernas", "leg press", "cuádriceps",
             "glúteos", "isquiotibiales", "máquina de palanca", "máquinas de gimnasio", "gimnasio",
             "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Lever Alternate Leg Press", "prensa de palanca a una pierna",
        "cuádriceps, isquiotibiales y glúteos",
        "¿Querés corregir diferencias entre piernas? La prensa a una pierna te ayuda. Mirá cómo se usa.",
        ["Ajustá el respaldo para que la espalda quede bien apoyada.",
         "Elegí un peso que puedas mover 10 veces con una pierna."],
        ["Sentate con la espalda apoyada y un pie centrado en la plataforma.",
         "Dejá la otra pierna apoyada en el piso y agarrá las manijas.",
         "Empujá la plataforma hasta casi estirar la rodilla.",
         "Volvé lento y alterná con la otra pierna."],
        ["Trabar la rodilla → llegá casi a estirar.",
         "Despegar la cadera → espalda bien apoyada.",
         "Empujar con impulso → movimiento controlado."],
        ["Una pierna por vez.", "Espalda y cadera bien apoyadas.", "Sin trabar la rodilla arriba.",
         "Volvé lento y controlá el peso."],
        "Cuádriceps · Isquiotibiales · Glúteos",
        "3 series de 10–12 repeticiones por pierna, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #LeverAlternateLegPress #PrensaDePiernas #Cuadriceps #Gluteos #Musculacion #Entrenamiento")})

# ═════════════ D19 · LEVER HORIZONTAL ONE LEG PRESS ═════════════
s, S, J = load("lever-horizontal-one-leg-press"); M = mpts(s, J)
HIP = S(*J["BOTTOM"]["H"]); KNEEB = S(*J["BOTTOM"]["K"]); KNEET = S(*J["TOP"]["K"])
ANKB = S(*J["BOTTOM"]["A"]); ANKT = S(*J["TOP"]["A"]); FAR = S(*s["poses"]["TOP"]["ankle2"])
KNEE_L = S(*J["LOCK_BAD"]["K"]); HIP_B = S(*J["HIP_BAD"]["H"])
F = [
    hook("GIMNASIO · PIERNAS", ["ONE LEG", "PRESS"], "Prensa horizontal",
         "Lever Horizontal One Leg Press: la prensa horizontal con una sola pierna. Glúteos, cuádriceps e isquiotibiales.",
         [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Horizontal y a una pierna",
         "La prensa horizontal: espalda apoyada, una placa que empujás con el pie y discos al costado.",
         [C("BOTTOM")], [ring(M["back"], 44, 0.8), lab((60, 1156), "RESPALDO", "start", 0.8),
                         ring(M["plates"], 46, 1.8), lab((985, 1303), "DISCOS", "end", 1.8),
                         ring(M["stop"], 30, 2.6), lab((60, 1390), "TOPE", "start", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Rodilla a 90 grados",
         "Ajustá el asiento para que, al empezar, la rodilla quede en un ángulo de noventa grados.",
         [C("BOTTOM")], [ring(KNEEB, 44, 0.8), lab((60, 1010), "RODILLA A 90°", "start", 1.0)], 7.0),
    step("AJUSTE 2", ["EL", "PIE"], "Centrado en la placa",
         "Apoyá el pie centrado en la placa, con toda la planta. Agarralo de las manijas del asiento.",
         [C("BOTTOM")], [ring(ANKB, 40, 0.8), lab((985, 1160), "PIE CENTRADO", "end", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["UNA", "PIERNA"], "La otra descansa",
         "Sentate con la espalda apoyada y una sola pierna en la placa. La otra queda relajada.",
         [C("BOTTOM")], [ring(ANKB, 40, 0.8), lab((60, 1000), "PIERNA ACTIVA", "start", 1.0),
                         ring(FAR, 34, 1.8), lab((60, 1430), "LA OTRA", "start", 1.8)], 7.0),
    step("PASO 1 / 3", ["EMPUJÁ", "LA PLACA"], "Sin apurar",
         "Paso uno. Empujá la placa alejándola del cuerpo, extendiendo la rodilla sin apurarte.",
         [C("BOTTOM"), TO("MID", 0.6, 1.0), TO("TOP", 1.6, 1.0)],
         [arrow((ANKB[0] + 16, ANKB[1] - 12), (ANKT[0] - 6, ANKT[1] - 12), 0.8, 1.1),
          lab((60, 1010), "EMPUJÁ", "start", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["CASI", "ESTIRADA"], "Sin trabar la rodilla",
         "Paso dos. Llegá casi a estirar la pierna y hacé una pausa breve, sin trabar la rodilla.",
         [C("TOP")], [ring(KNEET, 46, 0.8), lab((60, 1010), "SIN TRABAR", "start", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Controlá la vuelta",
         "Paso tres. Flexioná la rodilla y volvé lento hasta la posición inicial, controlando el peso.",
         [C("TOP"), TO("BOTTOM", 0.6, 2.2)],
         [arrow((ANKT[0] - 6, ANKT[1] - 12), (ANKB[0] + 16, ANKB[1] - 12), 0.8, 1.1),
          lab((60, 1010), "VOLVÉ LENTO", "start", 1.2)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al empujar",
         "Soltá el aire mientras empujás y tomalo cuando volvés. No aguantes el aire.",
         [C("BOTTOM"), seqloop("TOP", "BOTTOM", 1.1, 1.9, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["TRABAR", "LA RODILLA"], "Casi estirada",
         "Error: trabar o hiperextender la rodilla arriba. Llegá casi a estirar, sin bloquear la articulación.",
         [C("BOTTOM"), TO("LOCK_BAD", 0.5, 0.9)], [NO(), ring(KNEE_L, 50, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["DESPEGAR", "LA ESPALDA"], "Bien apoyado",
         "Error: despegar la espalda del respaldo para empujar. Mantené la espalda bien apoyada.",
         [C("BOTTOM"), TO("HIP_BAD", 0.5, 0.9)], [NO(), ring(HIP_B, 52, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Una pierna", "Espalda apoyada", "Sin trabar", "Volvé lento"],
         "Tips de profe: una pierna por vez, espalda apoyada, sin trabar la rodilla y volvé lento.",
         [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
    keys("CLAVES", ["TÉCNICA"], ["Pie centrado", "Rodilla alineada", "Sin impulso", "Bajá controlado"],
         "Claves: pie centrado, rodilla alineada con el pie, sin impulso y bajada controlada.",
         [{"cut": "TOP", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto de pausa",
         "Tres series de diez a doce por pierna, con un minuto de pausa. Cambiá de pierna entre series.",
         ["1 · EMPUJÁ", "2 · PAUSÁ", "3 · VOLVÉ LENTO"], [C("BOTTOM"), seqloop("TOP", "BOTTOM")]),
    step("AL TERMINAR", ["CAMBIÁ", "DE PIERNA"], "Sin soltar de golpe",
         "Al terminar, volvé la placa despacio y cambiá de pierna. No dejes caer el peso.",
         [C("BOTTOM"), TO("MID", 1.0, 1.0), TO("BOTTOM", 2.2, 1.2)],
         [lab((60, 1010), "CAMBIÁ DE PIERNA", "start", 1.0)], 6.5),
]
save("lever-horizontal-one-leg-press", F, {"pose": "TOP", "zoom": 1.15, "dy": 120}, {
    "titulo": "Lever Horizontal One Leg Press 🔥 Prensa a una pierna | Gimnasio",
    "tags": ["lever horizontal one leg press", "prensa horizontal", "prensa a una pierna", "leg press", "glúteos",
             "cuádriceps", "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes",
             "rutina de piernas", "piernas"],
    "descripcion": yt_desc("Lever Horizontal One Leg Press", "prensa horizontal a una pierna",
        "glúteos, cuádriceps e isquiotibiales",
        "¿Querés trabajar una pierna a la vez? La prensa horizontal a una pierna lo hace simple. Mirá cómo se usa.",
        ["Ajustá el asiento para que la rodilla quede a 90 grados al empezar.",
         "Elegí un peso que puedas mover 10 veces con una pierna."],
        ["Sentate con la espalda apoyada y una sola pierna en la placa.",
         "Apoyá el pie centrado y agarrá las manijas.",
         "Empujá la placa hasta casi estirar la rodilla.",
         "Volvé lento y cambiá de pierna."],
        ["Trabar la rodilla → llegá casi a estirar.",
         "Despegar la espalda → quedate bien apoyado."],
        ["Rodilla a 90 grados para empezar.", "Pie centrado en la placa.", "Sin trabar la rodilla.",
         "Volvé lento y controlá."],
        "Glúteos · Cuádriceps · Isquiotibiales · Gemelos",
        "3 series de 10–12 repeticiones por pierna, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #LeverHorizontalOneLegPress #PrensaDePiernas #Gluteos #Cuadriceps #Musculacion #Entrenamiento")})
