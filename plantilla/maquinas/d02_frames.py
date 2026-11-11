# Dataset D01 · D3 Assisted Parallel Close Grip Pull-up y D4 Assisted Standing Chin-up: escenas + YouTube + miniatura.
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


# ═════════════ D3 · ASSISTED PARALLEL CLOSE GRIP PULL-UP ═════════════
s, S, J = load("assisted-parallel-close-grip-pull-up"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); HANDLE = S(*pr["grip"])
PLAT = S(J["HANG"]["K"][0] - 10, J["HANG"]["K"][1] + 26); STEP = S(-245, -190)
KTOP = S(*J["TOP"]["K"]); HEAD = S(*J["TOP"]["N"]); KIP = S(*J["KIP_BAD"]["K"])
L = lambda: seqloop("MID", "TOP", 1.2, 1.8)
F = [
    hook("GIMNASIO · ESPALDA", ["DOMINADAS", "ASISTIDAS"], "Agarre paralelo cerrado",
         "Assisted Parallel Close Grip Pull-up: dominadas asistidas con agarre paralelo cerrado.",
         [C("HANG"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "Te ayuda a subir",
         "La máquina te empuja desde la plataforma de rodillas. Trabaja los dorsales y los bíceps.",
         [C("HANG")], [ring(HANDLE, 40, 0.8), lab(LT, "MANIJAS PARALELAS", "end", 0.8),
                       ring(PLAT, 56, 1.8), lab(LB, "PLATAFORMA", "start", 1.8),
                       ring(PINP, 30, 2.8), lab((130, 1250), "PASADOR", "start", 2.8)], 7.0),
    step("AJUSTE 1", ["EL", "CONTRAPESO"], "Más peso, más ayuda",
         "Elegí el contrapeso con el pasador. Acá es al revés: más peso es más ayuda.",
         [C("HANG")], [ring(PINP, 34, 0.8), lab(LT, "MÁS PESO = MÁS AYUDA", "end", 1.0)], 7.4),
    step("AJUSTE 2", ["SUBÍ CON", "CUIDADO"], "Por los escalones",
         "Subí por los escalones, agarrá las manijas y recién ahí apoyá las rodillas en la plataforma.",
         [C("HANG")], [ring(STEP, 60, 0.8), lab(LB, "ESCALONES", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["COLGADO", "FIRME"], "Hombros activos",
         "Colgate con los brazos estirados y los hombros activos: bajalos un poco, no quedes flojo.",
         [C("HANG")], [lab(LT, "HOMBROS ABAJO", "end", 1.0), ring(PLAT, 50, 1.6)], 7.0),
    step("PASO 1 / 3", ["PECHO A", "LAS MANOS"], "Tirá con la espalda",
         "Paso uno. Tirá llevando el pecho hacia las manos, con los codos hacia abajo y cerca del cuerpo.",
         [C("HANG"), TO("MID", 0.5, 0.9), TO("TOP", 1.4, 1.0)],
         [arrow((470, 1120), (470, 960), 0.8, 1.2), lab(LT, "PECHO ARRIBA", "end", 1.4)], numeral="1"),
    step("PASO 2 / 3", ["MENTÓN", "ARRIBA"], "Sobre las manos",
         "Paso dos. Subí hasta que el mentón pase por encima de las manos, sin estirar el cuello.",
         [C("TOP")], [ring(HEAD, 50, 0.8), lab(LT, "MENTÓN ARRIBA", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["BAJÁ", "EN 3"], "Hasta estirar los brazos",
         "Paso tres. Bajá en dos o tres segundos hasta estirar los brazos, sin soltarte de golpe.",
         [C("TOP"), TO("HANG", 0.6, 2.6)], [lab(LT, "2 A 3 SEGUNDOS", "end", 1.0)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
         "Soltá el aire mientras subís y tomá aire mientras bajás.",
         [C("HANG"), seqloop("TOP", "HANG", 1.4, 2.4, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 3", ["SUBIR CON", "IMPULSO"], "Sin balanceo",
         "Error: subir con impulso, balanceando las piernas. Si no sale, poné más ayuda.",
         [C("HANG"), TO("KIP_BAD", 0.5, 0.6)], [NO(), ring(KIP, 60, 1.4)], 7.2),
    step("ASÍ NO · 2 / 3", ["MEDIA", "REPETICIÓN"], "Bajá completo",
         "Error: quedarte a mitad de camino. Bajá hasta estirar los brazos del todo y recién ahí volvé.",
         [C("HANG"), TO("HALF_BAD", 0.5, 0.8)], [NO(), lab(LT, "ESTIRÁ DEL TODO", "end", 1.4)], 7.2),
    step("ASÍ NO · 3 / 3", ["SOLTARTE", "DE GOLPE"], "Bajada controlada",
         "Error: soltarte de golpe al bajar. El hombro recibe todo el tirón: controlá la bajada.",
         [C("TOP"), {"seq": [["HANG", 0.3], ["TOP", 0.3]], "at": 0.5, "until": 4.0}, TO("HANG", 4.1, 0.4)],
         [NO(1.0), lab(LT, "SIN CONTROL", "end", 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Hombros activos colgado", "Pecho a las manos", "Codos hacia abajo",
                                     "Cada semana, menos ayuda"],
         "Tips de profe: hombros activos, pecho a las manos, codos hacia abajo y cada semana un poco menos de ayuda.",
         [C("HANG"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Más peso = más ayuda", "Mentón sobre las manos", "Sin impulso",
                                "Bajada controlada"],
         "Claves: más peso es más ayuda, mentón sobre las manos, sin impulso y bajada controlada.",
         [{"cut": "TOP", "at": 0.1}]),
    reps(["3 X 6-10"], "Dos minutos de pausa",
         "Tres series de seis a diez, con dos minutos de pausa. Cuando las diez salen fáciles, sacá un poco de ayuda.",
         ["1 · PECHO ARRIBA", "2 · MENTÓN", "3 · BAJÁ LENTO"], [C("HANG"), L()]),
    step("AL TERMINAR", ["BAJATE", "CON CUIDADO"], "Pies al escalón",
         "Al terminar, apoyá los pies en los escalones y recién ahí soltá las manijas.",
         [C("HANG")], [ring(STEP, 60, 0.8), lab(LB, "PIES AL ESCALÓN", "start", 1.0)], 6.2),
]
save("assisted-parallel-close-grip-pull-up", F, {"pose": "HANG", "grip": 1, "zoom": 0.95, "dy": 160}, {
    "titulo": "Assisted Parallel Close Grip Pull-up 🔥 Dominadas asistidas agarre paralelo | Gimnasio",
    "tags": ["assisted parallel close grip pull up", "dominadas asistidas", "agarre paralelo", "máquina de dominadas",
             "dorsales", "bíceps", "espalda", "dominadas", "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Assisted Parallel Close Grip Pull-up", "dominadas asistidas con agarre paralelo cerrado",
        "el camino seguro a tus dominadas",
        "¿Todavía no te salen las dominadas y no sabés qué agarre usar? El agarre paralelo cerrado es el más amable con el hombro. Este video es para vos.",
        ["Elegí el contrapeso: acá más peso es más ayuda.", "Subí por los escalones y apoyá las rodillas en la plataforma."],
        ["Colgate con los brazos estirados y los hombros activos.", "Tirá llevando el pecho hacia las manos, con los codos abajo.",
         "Subí hasta pasar el mentón por encima de las manos.", "Bajá en 2–3 segundos hasta estirar los brazos."],
        ["Subir con impulso → subí lento, sin balanceo.", "Quedarte a media repetición → bajá hasta estirar del todo.",
         "Soltarte de golpe → bajada controlada de 2–3 segundos."],
        ["Colgate con los hombros activos, no flojos.", "Llevá el pecho a las manos.", "Los codos van hacia abajo, cerca del cuerpo.",
         "Cada semana sacá un poco de ayuda.", "Bajate con cuidado, pies al escalón."],
        "Dorsales · Bíceps · Romboides · Antebrazos",
        "3 series de 6–10 repeticiones, con 2 minutos de pausa. Nivel: principiante.",
        "#Gimnasio #AssistedPullUp #Dominadas #Espalda #Musculacion #Entrenamiento")})

# ═════════════ D4 · ASSISTED STANDING CHIN-UP ═════════════
s, S, J = load("assisted-standing-chin-up"); pr = s["props"][0]
PINP = S(*PIN(pr["stack"], pr["pin"])); HANDLE = S(*pr["grip"])
PLAT = S(J["STAND"]["A"][0], J["STAND"]["A"][1] + 36); STEP = S(-245, -190)
HEAD = S(*J["TOP"]["N"]); SWING = S(*J["SWING_BAD"]["K"])
L = lambda: seqloop("MID", "TOP", 1.2, 1.8)
F = [
    hook("GIMNASIO · ESPALDA", ["CHIN-UP", "ASISTIDO"], "De pie en la plataforma",
         "Assisted Standing Chin-up: la dominada asistida de pie, con plataforma para los pies.",
         [C("STAND"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "La plataforma te ayuda",
         "La plataforma de pies te empuja hacia arriba mientras tirás. Trabaja dorsales, bíceps y romboides.",
         [C("STAND")], [ring(PLAT, 56, 0.8), lab(LT, "PLATAFORMA", "end", 0.8),
                        ring(HANDLE, 40, 1.6), lab(LB, "MANIJAS ALTAS", "start", 1.6),
                        ring(PINP, 30, 2.8), lab((130, 1250), "PASADOR", "start", 2.8)], 7.0),
    step("AJUSTE 1", ["EL", "CONTRAPESO"], "Más peso, más ayuda",
         "Elegí el contrapeso con el pasador. Acá es al revés: más peso es más ayuda.",
         [C("STAND")], [ring(PINP, 34, 0.8), lab(LT, "MÁS PESO = MÁS AYUDA", "end", 1.0)], 7.4),
    step("AJUSTE 2", ["SUBÍ CON", "CUIDADO"], "Por los escalones",
         "Subí por los escalones y agarrá las manijas antes de apoyar los dos pies en la plataforma.",
         [C("STAND")], [ring(STEP, 60, 0.8), lab(LB, "ESCALONES", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["DE PIE", "FIRME"], "Hombros activos",
         "Quedate de pie en la plataforma con los brazos estirados y los hombros activos, sin encogerte.",
         [C("STAND")], [ring(PLAT, 50, 0.8), lab(LT, "HOMBROS ACTIVOS", "end", 1.0)], 7.0),
    step("PASO 1 / 3", ["PECHO A", "LAS MANOS"], "Tirá con la espalda",
         "Paso uno. Tirá con la espalda llevando el pecho a las manos, con los codos hacia abajo.",
         [C("STAND"), TO("MID", 0.5, 0.9), TO("TOP", 1.4, 1.0)],
         [arrow((470, 1120), (470, 960), 0.8, 1.2), lab(LT, "PECHO ARRIBA", "end", 1.4)], numeral="1"),
    step("PASO 2 / 3", ["MENTÓN", "ARRIBA"], "Sobre las manos",
         "Paso dos. Subí hasta que el mentón pase por encima de las manos, sin encoger los hombros.",
         [C("TOP")], [ring(HEAD, 50, 0.8), lab(LT, "MENTÓN ARRIBA", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["BAJÁ", "EN 3"], "Controlá la plataforma",
         "Paso tres. Bajá en dos o tres segundos, controlando la plataforma hasta estirar los brazos.",
         [C("TOP"), TO("STAND", 0.6, 2.6)], [lab(LT, "2 A 3 SEGUNDOS", "end", 1.0)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
         "Soltá el aire mientras subís y tomá aire mientras bajás.",
         [C("STAND"), seqloop("TOP", "STAND", 1.4, 2.4, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 2", ["IMPULSO DE", "CADERA"], "Sin hamacarte",
         "Error: usar impulso de cadera o piernas. Subí lento, sintiendo la espalda.",
         [C("STAND"), TO("SWING_BAD", 0.5, 0.7)], [NO(), ring(SWING, 60, 1.4)], 7.2),
    step("ASÍ NO · 2 / 2", ["MEDIA", "REPETICIÓN"], "Bajá completo",
         "Error: quedarte a mitad de camino. Bajá hasta estirar los brazos y recién ahí volvé a subir.",
         [C("STAND"), TO("HALF_BAD", 0.5, 0.8)], [NO(), lab(LT, "ESTIRÁ DEL TODO", "end", 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Pecho arriba, hombros atrás", "Rodillas apenas flexionadas",
                                     "Tirá con los codos abajo", "Cada semana, menos ayuda"],
         "Tips de profe: pecho arriba, hombros atrás, rodillas apenas flexionadas y cada semana menos ayuda.",
         [C("STAND"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Más peso = más ayuda", "Mentón sobre las manos", "Sin impulso de cadera",
                                "Bajada controlada"],
         "Claves: más peso es más ayuda, mentón sobre las manos, sin impulso de cadera y bajada controlada.",
         [{"cut": "TOP", "at": 0.1}]),
    reps(["3 X 6-10"], "Dos minutos de pausa",
         "Tres series de seis a diez, con dos minutos de pausa. Cuando las diez salen fáciles, sacá un poco de ayuda.",
         ["1 · PECHO ARRIBA", "2 · MENTÓN", "3 · BAJÁ LENTO"], [C("STAND"), L()]),
    step("AL TERMINAR", ["BAJATE", "CON CUIDADO"], "Un pie y después el otro",
         "Al terminar, apoyá un pie, después el otro, y soltá las manijas recién ahí.",
         [C("STAND")], [ring(PLAT, 56, 0.8), lab(LB, "PIES FIRMES", "start", 1.0)], 6.2),
]
save("assisted-standing-chin-up", F, {"pose": "STAND", "grip": 1, "zoom": 0.95, "dy": 160}, {
    "titulo": "Assisted Standing Chin-up 🔥 Dominadas asistidas de pie en máquina | Gimnasio",
    "tags": ["assisted standing chin up", "dominadas asistidas", "chin up", "máquina de dominadas asistidas",
             "dominadas de pie", "dorsales", "bíceps", "espalda", "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Assisted Standing Chin-up", "dominadas asistidas de pie",
        "la dominada con ayuda, sin colgarte de puntas",
        "¿No llegás a la barra ni con escalón? Esta máquina te empuja desde los pies y te deja entrenar la dominada sin miedo. Este video es para vos.",
        ["Elegí el contrapeso: acá más peso es más ayuda.", "Subí por los escalones y agarrá las manijas antes de apoyar los pies."],
        ["Quedate de pie en la plataforma, brazos estirados y hombros activos.", "Tirá con la espalda llevando el pecho a las manos.",
         "Subí hasta pasar el mentón por encima de las manos.", "Bajá en 2–3 segundos, controlando la plataforma."],
        ["Impulso de cadera → subí lento, sintiendo la espalda.", "Media repetición → bajá hasta estirar los brazos del todo.",
         "Soltarte de golpe → bajada controlada de 2–3 segundos."],
        ["Pecho arriba y hombros atrás.", "Rodillas apenas flexionadas sobre la plataforma.", "Tirá con los codos hacia abajo.",
         "Cada semana sacá un poco de ayuda.", "Bajate con cuidado, un pie y después el otro."],
        "Dorsales · Bíceps · Romboides · Antebrazos",
        "3 series de 6–10 repeticiones, con 2 minutos de pausa. Nivel: principiante.",
        "#Gimnasio #AssistedPullUp #ChinUp #Dominadas #Espalda #Entrenamiento")})
