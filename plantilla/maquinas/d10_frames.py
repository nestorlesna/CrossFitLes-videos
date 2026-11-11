# Dataset D01 · D20 Lever Seated Squat Calf Raise on Leg Press Machine y D21 Lever Lying Two-one Leg Curl: escenas + YouTube + miniatura.
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
    A = J["MID"]["A"]
    return dict(back=S(sb[0] + u[0] * 150, sb[1] + u[1] * 150),
                plates=S(A[0] + d[0] * 158 + n[0] * 105, A[1] + d[1] * 158 + n[1] * 105),
                stop=S(*at(pr["stops"], 160)))


def seqloop(a, b, ta=1.2, tb=1.6, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


# ═════════════ D20 · LEVER SEATED SQUAT CALF RAISE ON LEG PRESS MACHINE ═════════════
s, S, J = load("lever-seated-squat-calf-raise-on-leg-press-machine"); M = mpts(s, J)
HIP = S(*J["MID"]["H"]); KNEE = S(*J["MID"]["K"]); ANK = S(*J["MID"]["A"])
CALF = S((J["MID"]["K"][0] + J["MID"]["A"][0]) / 2, (J["MID"]["K"][1] + J["MID"]["A"][1]) / 2)
KNEE_B = S(*J["KNEE_BAD"]["K"]); HIP_B = S(*J["HIP_BAD"]["H"])
ANH = S(*J["HEELS"]["A"]); ANP = S(*J["PRESS"]["A"])
F = [
    hook("GIMNASIO · PIERNAS", ["CALF", "RAISE"], "En la prensa de piernas",
         "Lever Seated Squat Calf Raise on Leg Press Machine: elevación de talones en la prensa. Trabaja los gemelos.",
         [C("HEELS"), seqloop("PRESS", "HEELS")]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Puntas de pie en la placa",
         "La prensa de piernas con las puntas de los pies en la plataforma. Las rodillas quedan casi estiradas.",
         [C("MID")], [ring(M["back"], 44, 0.8), lab((60, 1164), "RESPALDO", "start", 0.8),
                      ring(ANK, 42, 1.8), lab((985, 1000), "PLATAFORMA", "end", 1.8),
                      ring(M["plates"], 46, 2.6), lab((985, 1210), "DISCOS", "end", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Rodillas casi estiradas",
         "Ajustá el asiento para que las rodillas queden casi estiradas con los pies en la plataforma.",
         [C("MID")], [ring(KNEE, 44, 0.8), lab((60, 1010), "CASI ESTIRADAS", "start", 1.0)], 7.0),
    step("AJUSTE 2", ["LOS", "PIES"], "Puntas en la plataforma",
         "Apoyá las puntas y la planta en la plataforma, con los talones al borde y los pies al ancho de los hombros.",
         [C("MID")], [ring(ANK, 42, 0.8), lab((60, 1010), "PUNTAS EN LA PLACA", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["TALONES", "LIBRES"], "Al borde de la placa",
         "Con las rodillas casi estiradas, dejá los talones libres en el borde de la plataforma.",
         [C("HEELS")], [ring(ANH, 42, 0.8), lab((60, 1010), "TALONES LIBRES", "start", 1.0)], 7.0),
    step("PASO 1 / 3", ["SUBÍ", "LOS TALONES"], "Sin mover las rodillas",
         "Paso uno. Empujá la plataforma subiendo los talones, sin cambiar el ángulo de las rodillas.",
         [C("HEELS"), TO("MID", 0.6, 0.8), TO("PRESS", 1.4, 0.8)],
         [arrow((ANH[0] - 46, ANH[1] + 34), (ANP[0] - 16, ANP[1] - 28), 0.8, 1.1),
          lab((60, 1010), "SUBÍ", "start", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Apretá el gemelo",
         "Paso dos. Hacé una pausa arriba, con los talones bien altos y el gemelo contraído.",
         [C("PRESS")], [ring(CALF, 46, 0.8), lab((60, 1010), "GEMELO", "start", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Estirá el gemelo",
         "Paso tres. Bajá los talones despacio hasta sentirlos estirar, sin dejar caer la plataforma.",
         [C("PRESS"), TO("MID", 0.6, 0.8), TO("HEELS", 1.4, 1.0)],
         [arrow((ANP[0] - 16, ANP[1] - 24), (ANH[0] - 46, ANH[1] + 38), 0.8, 1.1),
          lab((60, 1010), "ESTIRÁ", "start", 1.2)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
         "Soltá el aire al subir y tomalo al bajar. Respirá parejo, sin rebotar.",
         [C("HEELS"), seqloop("PRESS", "HEELS", 1.2, 1.6, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["DOBLAR", "LAS RODILLAS"], "Rodillas fijas",
         "Error: doblar las rodillas para empujar. Las rodillas quedan casi estiradas y el trabajo es del gemelo.",
         [C("MID"), TO("KNEE_BAD", 0.5, 0.9)], [NO(), ring(KNEE_B, 50, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["DESPEGAR", "LA CADERA"], "Espalda apoyada",
         "Error: despegar la cadera y la espalda del respaldo. Quedá bien apoyado.",
         [C("MID"), TO("HIP_BAD", 0.5, 0.9)], [NO(), ring(HIP_B, 52, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Talones libres", "Rodillas fijas", "Pausa arriba", "Bajá lento"],
         "Tips de profe: talones libres, rodillas fijas, pausa arriba y bajá lento.",
         [C("HEELS"), seqloop("PRESS", "HEELS")]),
    keys("CLAVES", ["TÉCNICA"], ["Puntas al borde", "Rodillas casi rectas", "Sin rebote", "Rango completo"],
         "Claves: puntas al borde, rodillas casi estiradas, sin rebote y rango completo.",
         [{"cut": "PRESS", "at": 0.1}]),
    reps(["3 X 12-15"], "Cuarenta y cinco segundos",
         "Tres series de doce a quince, con cuarenta y cinco segundos de pausa. Subí cuando salgan fáciles.",
         ["1 · SUBÍ", "2 · APRETÁ", "3 · BAJÁ LENTO"], [C("HEELS"), seqloop("PRESS", "HEELS")]),
    step("AL TERMINAR", ["DEJÁ LA", "PLATAFORMA"], "Sin soltar de golpe",
         "Al terminar, volvé la plataforma despacio y soltá las trabas. No dejes caer el peso.",
         [C("MID"), TO("HEELS", 1.0, 1.0)],
         [lab((60, 1010), "DEJÁ LA PLATAFORMA", "start", 1.0)], 6.5),
]
save("lever-seated-squat-calf-raise-on-leg-press-machine", F,
     {"pose": "PRESS", "zoom": 1.15, "dy": 120}, {
    "titulo": "Lever Seated Squat Calf Raise 🔥 Elevación de talones en prensa | Gimnasio",
    "tags": ["lever seated squat calf raise", "elevación de talones", "calf raise", "gemelos", "pantorrillas",
             "prensa de piernas", "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes",
             "rutina de piernas", "piernas"],
    "descripcion": yt_desc("Lever Seated Squat Calf Raise on Leg Press Machine", "elevación de talones en la prensa",
        "gemelos, con cuádriceps como apoyo",
        "¿Querés gemelos más fuertes? La prensa de piernas también sirve para elevación de talones. Mirá cómo se usa.",
        ["Ajustá el asiento para que las rodillas queden casi estiradas.",
         "Apoyá las puntas en la plataforma, con los talones al borde."],
        ["Sentate con la espalda apoyada y las puntas de los pies en la plataforma.",
         "Dejá los talones libres en el borde y las rodillas casi estiradas.",
         "Empujá la plataforma subiendo los talones, sin mover las rodillas.",
         "Hacé una pausa arriba y bajá los talones lento hasta estirar el gemelo."],
        ["Doblar las rodillas → quedan casi estiradas.",
         "Despegar la cadera → espalda bien apoyada.",
         "Rebotar abajo → pausa y bajada controlada."],
        ["Puntas y planta en la plataforma.", "Rodillas casi estiradas y fijas.",
         "Pausa arriba con el gemelo contraído.", "Bajá lento hasta estirar."],
        "Gemelos · Cuádriceps · Isquiotibiales",
        "3 series de 12–15 repeticiones, con 45 segundos de pausa. Nivel: principiante.",
        "#Gimnasio #CalfRaise #Gemelos #PrensaDePiernas #Pantorrillas #Musculacion #Entrenamiento")})

# ═════════════ D21 · LEVER LYING TWO-ONE LEG CURL ═════════════
s, S, J = load("lever-lying-two-one-leg-curl"); pr = s["props"][0]
PINP = S(pr["stack"] + 51, -254 + (pr["pin"] - 0.5) * 22)
BACK = S(pr["back"][0] - 52, -502)
HANDLE = S(*pr["handle"]); _PAD = S(*pr["thigh"]); PAD = (_PAD[0] + 44, _PAD[1] - 22)
A_EXT = S(*J["EXT"]["A"]); A_CUR = S(*J["CURL"]["A"]); KNEEP = S(*pr["pivot"])
CALF_C = S((J["CURL"]["K"][0] + J["CURL"]["A"][0]) / 2, (J["CURL"]["K"][1] + J["CURL"]["A"][1]) / 2)
HIP_B = S(*J["HIP_BAD"]["H"]); PAD_UP = (PAD[0], PAD[1] - 72)
F = [
    hook("GIMNASIO · PIERNAS", ["LEG", "CURL"], "Femoral en máquina",
         "Lever Lying Two-one Leg Curl: el curl femoral en máquina. Con la espalda apoyada, flexioná las piernas hacia los glúteos.",
         [C("EXT"), seqloop("CURL", "EXT", 1.1, 1.9)]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Rodillo detrás del tobillo",
         "La máquina de femoral: asiento con respaldo, rodillo detrás de los tobillos y traba sobre los muslos.",
         [C("EXT")], [ring(BACK, 44, 0.8), lab((60, 1100), "RESPALDO", "start", 0.8),
                      ring(A_EXT, 40, 1.8), lab((985, 1110), "RODILLO", "end", 1.8),
                      ring(PAD, 42, 2.6), lab((60, 1184), "TRABA", "start", 2.6),
                      ring(PINP, 30, 3.4), lab((60, 1450), "PASADOR", "start", 3.4)], 7.0),
    step("AJUSTE 1", ["EL", "EJE"], "Rodilla alineada",
         "Alineá la rodilla con el eje de la máquina y ajustá el respaldo para que la espalda quede apoyada.",
         [C("EXT")], [ring(KNEEP, 40, 0.8), lab((60, 1000), "RODILLA AL EJE", "start", 1.0)], 7.0),
    step("AJUSTE 2", ["LA", "TRABA"], "Sobre los muslos",
         "Bajá la traba sobre los muslos: tiene que quedar firme, sin apretar de más.",
         [C("EXT")], [ring(PAD, 42, 0.8), lab((60, 1000), "TRABA FIRME", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["TOBILLOS", "ENGANCHADOS"], "Manos en las manijas",
         "Apoyá el rodillo detrás de los tobillos y agarrá las manijas a los costados.",
         [C("EXT")], [ring(A_EXT, 40, 0.8), lab((60, 1000), "DETRÁS DEL TOBILLO", "start", 1.0),
                      ring(HANDLE, 34, 1.8), lab((985, 1360), "MANIJAS", "end", 1.8)], 7.0),
    step("PASO 1 / 3", ["FLEXIONÁ"], "Sin mover el torso",
         "Paso uno. Flexioná las piernas hacia los glúteos, manteniendo el torso quieto y la espalda apoyada.",
         [C("EXT"), TO("MID", 0.6, 1.0), TO("CURL", 1.6, 1.0)],
         [arrow((A_EXT[0] - 10, A_EXT[1] + 10), (A_CUR[0] + 40, A_CUR[1] - 30), 0.8, 1.2, [40, 90]),
          lab((60, 1000), "FLEXIONÁ", "start", 1.2)], numeral="1"),
    step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Talones al glúteo",
         "Paso dos. Hacé una pausa breve arriba, con los talones cerca de los glúteos.",
         [C("CURL")], [ring(CALF_C, 44, 0.8), lab((60, 1000), "APRETÁ", "start", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["VOLVÉ", "LENTO"], "Controlá la vuelta",
         "Paso tres. Volvé lento a la posición inicial, controlando el peso en todo el recorrido.",
         [C("CURL"), TO("MID", 0.6, 1.0), TO("EXT", 1.6, 1.2)],
         [arrow((A_CUR[0] + 40, A_CUR[1] - 30), (A_EXT[0] - 10, A_EXT[1] + 10), 0.8, 1.2, [40, 90]),
          lab((60, 1000), "VOLVÉ LENTO", "start", 1.2)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al flexionar",
         "Soltá el aire al flexionar y tomalo al volver. No aguantes el aire.",
         [C("EXT"), seqloop("CURL", "EXT", 1.1, 1.9, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["DESPEGAR", "LA CADERA"], "Espalda apoyada",
         "Error: despegar la cadera y la espalda para ayudar. Quedá bien apoyado en el respaldo.",
         [C("EXT"), TO("HIP_BAD", 0.5, 0.9)], [NO(), ring(HIP_B, 52, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["SOLTAR", "LA TRABA"], "Traba firme",
         "Error: dejar la traba de muslos abierta. Bajala firme antes de empezar.",
         [C("EXT"), TO("PAD_BAD", 0.5, 0.9)], [NO(), ring(PAD_UP, 50, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Rodilla al eje", "Traba firme", "Torso quieto", "Volvé lento"],
         "Tips de profe: rodilla al eje, traba firme, torso quieto y volvé lento.",
         [C("EXT"), seqloop("CURL", "EXT", 1.1, 1.9)]),
    keys("CLAVES", ["TÉCNICA"], ["Eje alineado", "Traba firme", "Pausa arriba", "Bajada controlada"],
         "Claves: eje alineado, traba firme, pausa arriba y bajada controlada.",
         [{"cut": "CURL", "at": 0.1}]),
    reps(["3 X 10-12"], "Un minuto de pausa",
         "Tres series de diez a doce, con un minuto de pausa. Subí una placa cuando salgan fáciles.",
         ["1 · FLEXIONÁ", "2 · APRETÁ", "3 · VOLVÉ LENTO"], [C("EXT"), seqloop("CURL", "EXT", 1.1, 1.9)]),
    step("AL TERMINAR", ["DEJÁ EL", "PESO"], "Sin soltar de golpe",
         "Al terminar, volvé las piernas despacio y dejá el peso apoyado. No lo sueltes de golpe.",
         [C("EXT"), TO("MID", 1.0, 1.0), TO("EXT", 2.2, 1.2)],
         [lab((60, 1000), "PESO APOYADO", "start", 1.0)], 6.5),
]
save("lever-lying-two-one-leg-curl", F, {"pose": "CURL", "zoom": 1.1, "dy": 110}, {
    "titulo": "Lever Lying Two-one Leg Curl 🔥 Curl femoral en máquina | Gimnasio",
    "tags": ["lever lying two-one leg curl", "curl femoral", "leg curl", "isquiotibiales", "glúteos",
             "máquina de palanca", "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas",
             "femoral", "piernas"],
    "descripcion": yt_desc("Lever Lying Two-one Leg Curl", "curl femoral en máquina",
        "isquiotibiales y glúteos",
        "¿Querés femorales más fuertes? El curl en máquina los aísla con la espalda apoyada. Mirá cómo se usa.",
        ["Alineá la rodilla con el eje de la máquina.",
         "Bajá la traba de muslos y elegí un peso que puedas mover 10 veces."],
        ["Sentate con la espalda apoyada y la rodilla alineada al eje.",
         "Bajá la traba sobre los muslos y enganchá los tobillos en el rodillo.",
         "Flexioná las piernas hacia los glúteos, sin mover el torso.",
         "Hacé una pausa arriba y volvé lento a la posición inicial."],
        ["Despegar la cadera → quedate bien apoyado.",
         "Soltar la traba → bajala firme sobre los muslos.",
         "Usar impulso → movimiento controlado."],
        ["Rodilla alineada con el eje.", "Traba firme sobre los muslos.", "Torso quieto y espalda apoyada.",
         "Pausa arriba y volvé lento."],
        "Isquiotibiales · Glúteos",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #LegCurl #CurlFemoral #Isquiotibiales #Femoral #Musculacion #Entrenamiento")})
