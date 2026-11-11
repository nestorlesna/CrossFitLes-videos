# Dataset D01 · D5 Assisted Standing Pull-up y D6 Lever Assisted Chin-up: escenas + YouTube + miniatura.
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
LB, LT = (130, 700), (1000, 700)


# ═════════════ D5 · ASSISTED STANDING PULL-UP ═════════════
s, S, J = load("assisted-standing-pull-up"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); HANDLE = S(*pr["grip"])
PLAT = S(J["STAND"]["A"][0], J["STAND"]["A"][1] + 36); STEP = S(-245, -190)
HEAD = S(*J["TOP"]["N"]); SWING = S(*J["SWING_BAD"]["K"])
L = lambda: seqloop("MID", "TOP", 1.2, 1.8)
F = [
    hook("GIMNASIO · ESPALDA", ["DOMINADAS", "DE PIE"], "Agarre prono ancho",
         "Assisted Standing Pull-up: dominadas asistidas de pie, con agarre prono y plataforma para los pies.",
         [C("STAND"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Plataforma que empuja",
         "La plataforma de pies te empuja hacia arriba. Trabaja dorsales, bíceps y romboides.",
         [C("STAND")], [ring(PLAT, 56, 0.8), lab(LT, "PLATAFORMA", "end", 0.8),
                        ring(HANDLE, 40, 1.6), lab(LB, "MANIJAS ALTAS", "start", 1.6),
                        ring(PINP, 30, 2.8), lab((130, 1250), "PASADOR", "start", 2.8)], 7.0),
    step("AJUSTE 1", ["EL", "CONTRAPESO"], "Más peso, más ayuda",
         "Elegí el contrapeso con el pasador. Acá es al revés: más peso es más ayuda.",
         [C("STAND")], [ring(PINP, 34, 0.8), lab(LT, "MÁS PESO = MÁS AYUDA", "end", 1.0)], 7.4),
    step("AJUSTE 2", ["SUBÍ CON", "CUIDADO"], "Por los escalones",
         "Subí por los escalones y agarrá las manijas antes de apoyar los dos pies en la plataforma.",
         [C("STAND")], [ring(STEP, 60, 0.8), lab(LB, "ESCALONES", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["DE PIE", "FIRME"], "Pies al ancho de hombros",
         "Quedate de pie con los pies al ancho de hombros, los brazos estirados y los hombros activos.",
         [C("STAND")], [ring(PLAT, 50, 0.8), lab(LT, "PIES AL ANCHO", "end", 1.0)], 7.0),
    step("PASO 1 / 3", ["PECHO A", "LAS MANOS"], "Tirá con la espalda",
         "Paso uno. Activá los dorsales y tirá llevando el pecho hacia las manos, con los codos abajo.",
         [C("STAND"), TO("MID", 0.5, 0.9), TO("TOP", 1.4, 1.0)],
         [arrow((490, 1120), (490, 960), 0.8, 1.2), lab(LT, "PECHO ARRIBA", "end", 1.4)], numeral="1"),
    step("PASO 2 / 3", ["MENTÓN", "ARRIBA"], "Sobre las manos",
         "Paso dos. Subí hasta que el mentón pase por encima de las manos y apretá la espalda un segundo.",
         [C("TOP")], [ring(HEAD, 50, 0.8), lab(LT, "MENTÓN ARRIBA", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["BAJÁ", "EN 3"], "Controlá la plataforma",
         "Paso tres. Bajá en dos o tres segundos, controlando la plataforma hasta estirar los brazos.",
         [C("TOP"), TO("STAND", 0.6, 2.6)], [lab(LT, "2 A 3 SEGUNDOS", "end", 1.0)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
         "Soltá el aire mientras subís y tomá aire mientras bajás.",
         [C("STAND"), seqloop("TOP", "STAND", 1.4, 2.4, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 3", ["IMPULSO DE", "CADERA"], "Sin hamacarte",
         "Error: usar impulso de cadera o piernas. Subí lento, sintiendo la espalda.",
         [C("STAND"), TO("SWING_BAD", 0.5, 0.7)], [NO(), ring(SWING, 60, 1.4)], 7.2),
    step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Bajá completo",
         "Error: quedarte a mitad de camino. Bajá hasta estirar los brazos del todo y recién ahí volvé.",
         [C("STAND"), TO("HALF_BAD", 0.5, 0.8)], [NO(), lab(LT, "ESTIRÁ DEL TODO", "end", 1.4)], 7.2),
    step("ASÍ NO · 3 / 3", ["SOLTARTE", "DE GOLPE"], "Bajada controlada",
         "Error: soltarte de golpe al bajar. Controlá la plataforma hasta el final, sin dejar caer el peso.",
         [C("TOP"), {"seq": [["STAND", 0.3], ["TOP", 0.3]], "at": 0.5, "until": 4.0}, TO("STAND", 4.1, 0.4)],
         [NO(1.0), lab(LT, "SIN CONTROL", "end", 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Pies al ancho de hombros", "Pecho arriba, hombros atrás", "Tirá con los codos abajo",
                                     "Cada semana, menos ayuda"],
         "Tips de profe: pies al ancho de hombros, pecho arriba, codos hacia abajo y cada semana un poco menos de ayuda.",
         [C("STAND"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Más peso = más ayuda", "Mentón sobre las manos", "Cuerpo recto, sin impulso",
                                "Bajada controlada"],
         "Claves: más peso es más ayuda, mentón sobre las manos, cuerpo recto sin impulso y bajada controlada.",
         [{"cut": "TOP", "at": 0.1}]),
    reps(["3 X 6-10"], "Dos minutos de pausa",
         "Tres series de seis a diez, con dos minutos de pausa. Cuando las diez salen fáciles, sacá un poco de ayuda.",
         ["1 · PECHO ARRIBA", "2 · MENTÓN", "3 · BAJÁ LENTO"], [C("STAND"), L()]),
    step("AL TERMINAR", ["BAJATE", "CON CUIDADO"], "Un pie y después el otro",
         "Al terminar, apoyá un pie, después el otro, y soltá las manijas recién ahí.",
         [C("STAND")], [ring(PLAT, 56, 0.8), lab(LB, "PIES FIRMES", "start", 1.0)], 6.2),
]
save("assisted-standing-pull-up", F, {"pose": "STAND", "grip": 1, "zoom": 0.95, "dy": 160}, {
    "titulo": "Assisted Standing Pull-up 🔥 Dominadas asistidas de pie agarre prono | Gimnasio",
    "tags": ["assisted standing pull up", "dominadas asistidas", "pull up asistida", "máquina de dominadas",
             "agarre prono", "dominadas de pie", "dorsales", "bíceps", "espalda", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Assisted Standing Pull-up", "dominadas asistidas de pie con agarre prono",
        "la dominada clásica, con ayuda",
        "¿Querés aprender la dominada con agarre prono sin quedarte colgado? La máquina asistida te da la ayuda justa. Este video es para vos.",
        ["Elegí el contrapeso: acá más peso es más ayuda.", "Subí por los escalones y agarrá las manijas antes de apoyar los pies."],
        ["De pie, pies al ancho de hombros, brazos estirados y hombros activos.", "Tirá con los dorsales llevando el pecho a las manos.",
         "Subí hasta pasar el mentón por encima de las manos.", "Bajá en 2–3 segundos controlando la plataforma."],
        ["Impulso de cadera → subí lento, sintiendo la espalda.", "Media repetición → bajá hasta estirar los brazos del todo.",
         "Soltarte de golpe → bajada controlada de 2–3 segundos."],
        ["Pies al ancho de hombros sobre la plataforma.", "Pecho arriba y hombros atrás.", "Tirá con los codos hacia abajo.",
         "Cada semana sacá un poco de ayuda.", "Bajate con cuidado, un pie y después el otro."],
        "Dorsales · Bíceps · Romboides · Antebrazos",
        "3 series de 6–10 repeticiones, con 2 minutos de pausa. Nivel: principiante.",
        "#Gimnasio #AssistedPullUp #Dominadas #AgarreProno #Espalda #Entrenamiento")})

# ═════════════ D6 · LEVER ASSISTED CHIN-UP ═════════════
s, S, J = load("lever-assisted-chin-up"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); HANDLE = S(*pr["grip"])
PLAT = S(J["STAND"]["A"][0], J["STAND"]["A"][1] + 36); STEP = S(-245, -190)
HEAD = S(*J["TOP"]["N"]); SWING = S(*J["SWING_BAD"]["K"])
L = lambda: seqloop("MID", "TOP", 1.2, 1.8)
F = [
    hook("GIMNASIO · ESPALDA", ["CHIN-UP", "EN PALANCA"], "Manijas bajas, cuerpo recto",
         "Lever Assisted Chin-up: la dominada asistida en máquina de palanca, de pie en la plataforma.",
         [C("STAND"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Palanca y contrapeso",
         "La palanca mueve la pila y la plataforma te ayuda a subir. Trabaja dorsales, bíceps y romboides.",
         [C("STAND")], [ring(PLAT, 56, 0.8), lab(LT, "PLATAFORMA", "end", 0.8),
                        ring(HANDLE, 44, 1.6), lab(LB, "MANIJAS", "start", 1.6),
                        ring(PINP, 30, 2.8), lab((130, 1250), "PASADOR", "start", 2.8)], 7.0),
    step("AJUSTE 1", ["EL", "CONTRAPESO"], "Más peso, más ayuda",
         "Elegí el contrapeso con el pasador. Acá es al revés: más peso es más ayuda.",
         [C("STAND")], [ring(PINP, 34, 0.8), lab(LT, "MÁS PESO = MÁS AYUDA", "end", 1.0)], 7.4),
    step("AJUSTE 2", ["SUBÍ CON", "CUIDADO"], "Por los escalones",
         "Subí por los escalones y agarrá las manijas con agarre prono antes de apoyar los pies.",
         [C("STAND")], [ring(STEP, 60, 0.8), lab(LB, "ESCALONES", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["CUERPO", "RECTO"], "Brazos extendidos",
         "Quedate con el cuerpo recto, los brazos extendidos y los hombros activos, sin quedar flojo.",
         [C("STAND")], [lab(LT, "CUERPO RECTO", "end", 1.0), ring(PLAT, 50, 1.6)], 7.0),
    step("PASO 1 / 3", ["PECHO A", "LAS MANOS"], "Liderá con el pecho",
         "Paso uno. Activá la espalda y tirá del cuerpo hacia arriba liderando con el pecho.",
         [C("STAND"), TO("MID", 0.5, 0.9), TO("TOP", 1.4, 1.0)],
         [arrow((500, 1100), (500, 940), 0.8, 1.2), lab(LT, "PECHO ADELANTE", "end", 1.4)], numeral="1"),
    step("PASO 2 / 3", ["MENTÓN", "ARRIBA"], "Sobre las manijas",
         "Paso dos. Subí hasta que el mentón quede por encima de las manijas y apretá un segundo.",
         [C("TOP")], [ring(HEAD, 46, 0.8), lab(LT, "MENTÓN ARRIBA", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["BAJÁ", "EN 3"], "Hasta estirar los brazos",
         "Paso tres. Bajá lento, en dos o tres segundos, hasta estirar los brazos del todo.",
         [C("TOP"), TO("STAND", 0.6, 2.6)], [lab(LT, "2 A 3 SEGUNDOS", "end", 1.0)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
         "Soltá el aire mientras subís y tomá aire mientras bajás.",
         [C("STAND"), seqloop("TOP", "STAND", 1.4, 2.4, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["IMPULSO DE", "CADERA"], "Cuerpo recto",
         "Error: usar impulso de cadera. Mantené el cuerpo recto y tirá solo con la espalda.",
         [C("STAND"), TO("SWING_BAD", 0.5, 0.7)], [NO(), ring(SWING, 60, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["MEDIA", "REPETICIÓN"], "Bajá completo",
         "Error: quedarte a mitad de camino. Bajá hasta estirar los brazos y recién ahí volvé a subir.",
         [C("STAND"), TO("HALF_BAD", 0.5, 0.8)], [NO(), lab(LT, "ESTIRÁ DEL TODO", "end", 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Agarre prono, un poco ancho", "Cuerpo recto colgado", "Liderá con el pecho",
                                     "Cada semana, menos ayuda"],
         "Tips de profe: agarre prono un poco ancho, cuerpo recto, liderá con el pecho y cada semana menos ayuda.",
         [C("STAND"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Más peso = más ayuda", "Mentón sobre las manijas", "Cuerpo recto, sin impulso",
                                "Bajada controlada"],
         "Claves: más peso es más ayuda, mentón sobre las manijas, cuerpo recto sin impulso y bajada controlada.",
         [{"cut": "TOP", "at": 0.1}]),
    reps(["3 X 6-10"], "Dos minutos de pausa",
         "Tres series de seis a diez, con dos minutos de pausa. Cuando las diez salen fáciles, sacá un poco de ayuda.",
         ["1 · PECHO ARRIBA", "2 · MENTÓN", "3 · BAJÁ LENTO"], [C("STAND"), L()]),
    step("AL TERMINAR", ["BAJATE", "CON CUIDADO"], "Pies al escalón",
         "Al terminar, apoyá los pies en los escalones y recién ahí soltá las manijas.",
         [C("STAND")], [ring(STEP, 60, 0.8), lab(LB, "PIES AL ESCALÓN", "start", 1.0)], 6.2),
]
save("lever-assisted-chin-up", F, {"pose": "STAND", "grip": 1, "zoom": 0.95, "dy": 160}, {
    "titulo": "Lever Assisted Chin-up 🔥 Dominada asistida en máquina de palanca | Gimnasio",
    "tags": ["lever assisted chin up", "dominada asistida", "chin up en máquina", "máquina de palanca",
             "dominadas asistidas", "dorsales", "bíceps", "espalda", "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Lever Assisted Chin-up", "dominada asistida en máquina de palanca",
        "subí con la espalda, no con impulso",
        "¿Usás la máquina de palanca pero volvés con impulso? Con estos ajustes, cada repetición la hace la espalda. Este video es para vos.",
        ["Elegí el contrapeso: acá más peso es más ayuda.", "Subí por los escalones y agarrá las manijas con agarre prono."],
        ["Cuerpo recto, brazos extendidos y hombros activos.", "Tirá del cuerpo hacia arriba liderando con el pecho.",
         "Subí hasta pasar el mentón por encima de las manijas.", "Bajá en 2–3 segundos hasta estirar los brazos."],
        ["Usar impulso de cadera → cuerpo recto, tirá con la espalda.", "Media repetición → bajá hasta estirar del todo.",
         "Soltarte de golpe → bajada controlada de 2–3 segundos."],
        ["Agarre prono un poco más ancho que los hombros.", "Cuerpo recto mientras colgás.", "Liderá con el pecho, no con el mentón.",
         "Cada semana sacá un poco de ayuda.", "Bajate con cuidado, pies al escalón."],
        "Dorsales · Bíceps · Romboides · Antebrazos",
        "3 series de 6–10 repeticiones, con 2 minutos de pausa. Nivel: principiante.",
        "#Gimnasio #LeverAssistedChinUp #Dominadas #Espalda #Musculacion #Entrenamiento")})
