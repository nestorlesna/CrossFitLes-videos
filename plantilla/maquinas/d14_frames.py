# Dataset D01 · D27 Assisted Chest Dip (Kneeling) y D28 Assisted Triceps Dip (Kneeling): escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.1, tb=1.9, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def dip_scenes(slug, v):
    s, S, J = load(slug)
    W = S(60, -750); PIN = S(471, -133); PILE = S(420, -110)
    H_T = S(*J["TOP"]["H"]); H_B = S(*J["BOTTOM"]["H"])
    S_T = S(*J["TOP"]["S"]); S_B = S(*J["BOTTOM"]["S"])
    PAD = S(J["TOP"]["K"][0] - 30, J["TOP"]["K"][1] + 26)
    CH_BAD = S((J[v["bad_pose"]]["S"][0] + J[v["bad_pose"]]["H"][0]) / 2,
               (J[v["bad_pose"]]["S"][1] + J[v["bad_pose"]]["H"][1]) / 2)
    return [
        hook(v["cat"], ["ASSISTED", "DIP"], v["sub_hook"], v["vo_hook"],
             [C("TOP"), seqloop("BOTTOM", "TOP", 1.4, 1.6)]),
        step("LA MÁQUINA", ["LA", "MÁQUINA"], "Contrapeso y paralelas",
             "La máquina asistida te ayuda con un contrapeso: cuanto más peso elegís, más ayuda y menos esfuerzo.",
             [C("TOP")], [ring(PAD, 44, 0.8), lab((60, 1180), "PLATAFORMA", "start", 0.8),
                          ring(W, 36, 1.8), lab((60, 1060), "MANIJAS", "start", 1.8),
                          ring(PILE, 60, 2.8), lab((886, 1370), "PILA", "start", 2.8)], 7.2),
        step("AJUSTE 1", ["LAS", "RODILLAS"], "Sobre la plataforma",
             v["vo_aj1"],
             [C("TOP")], [ring(PAD, 44, 0.8), lab((60, 1180), "RODILLAS ACÁ", "start", 1.0)], 7.0),
        step("AJUSTE 2", ["EL CONTRA", "PESO"], "Más peso, más ayuda",
             "El pasador elige el contrapeso: más placas es más ayuda. Probá con uno que te deje hacer diez repeticiones.",
             [C("TOP")], [ring(PIN, 26, 0.8), lab((880, 1470), "PASADOR", "start", 1.0)], 7.0),
        step("POSICIÓN INICIAL", ["BRAZOS", "ESTIRADOS"], v["sub_pos"], v["vo_pos"],
             [C("TOP")], [ring(W, 36, 0.8), lab((60, 1060), v["lab_grip"], "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "LENTO"], v["sub_1"], v["vo_1"],
             [C("TOP"), TO("BOTTOM", 0.6, 1.4)],
             [arrow((512, 958), (488, 1150), 0.9, 1.2), ring(H_B, 34, 1.6)], 6.8, numeral="1"),
        step("PASO 2 / 3", ["PAUSA", "ABAJO"], "Sin rebote",
             "Paso dos. Abajo, pausa un segundo sin rebotar y sin encoger los hombros.",
             [C("BOTTOM")], [ring(H_B, 34, 0.8), lab((60, 1100), "PAUSA", "start", 1.0)], 6.5, numeral="2"),
        step("PASO 3 / 3", ["EMPUJÁ", "ARRIBA"], "Sin trabar los codos",
             "Paso tres. Empujá hasta estirar casi del todo, sin trabar los codos.",
             [C("BOTTOM"), TO("TOP", 0.6, 1.2)],
             [arrow((488, 1150), (512, 958), 0.9, 1.2), ring(H_T, 34, 1.6)], 6.5, numeral="3"),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al subir",
             "Soltá el aire mientras empujás y tomalo mientras bajás.",
             [C("TOP"), seqloop("BOTTOM", "TOP", 1.3, 2.0, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 2", v["bad1"], v["sub_bad1"], v["vo_bad1"],
             [C("TOP"), TO(v["bad_pose"], 0.5, 1.0)], [NO(pos=(540, 700)), ring(CH_BAD, 46, 1.4)], 7.2),
        step("ASÍ NO · 2 / 2", ["ENCOGER", "LOS HOMBROS"], "Hombros abajo",
             "Error: encoger los hombros hacia las orejas. Mantenelos abajo y lejos del cuello.",
             [C("BOTTOM"), TO("SHRUG_BAD", 0.5, 0.8)], [NO(pos=(540, 700)), ring((S_B[0], S_B[1] + 46), 40, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], v["tips"], v["vo_tips"],
             [C("TOP"), seqloop("BOTTOM", "TOP")]),
        keys("CLAVES", ["TÉCNICA"], v["keys"], v["vo_keys"],
             [{"cut": "BOTTOM", "at": 0.1}]),
        reps([v["reps"]], "Un minuto de pausa", v["vo_reps"],
             ["1 · BAJÁ LENTO", "2 · PAUSA", "3 · EMPUJÁ ARRIBA"], [C("TOP"), seqloop("BOTTOM", "TOP")]),
        step("AL TERMINAR", ["SALÍ", "DESPACIO"], "Dejá el peso apoyado",
             "Al terminar, estirá los brazos, sacá las rodillas con cuidado y dejá el contrapeso apoyado.",
             [C("BOTTOM"), TO("TOP", 0.8, 2.0)],
             [lab((60, 1010), "SALÍ DESPACIO", "start", 1.0)], 6.5),
    ]


V27 = dict(cat="GIMNASIO · PECHO", sub_hook="Fondos de pecho con ayuda",
           vo_hook="Assisted Chest Dip: fondos de pecho asistidos de rodillas. El contrapeso te ayuda a completar el recorrido.",
           vo_aj1="Apoyá las rodillas sobre la plataforma, con los brazos estirados y las manos en las paralelas.",
           sub_pos="Palmas hacia abajo", lab_grip="PALMAS ABAJO",
           vo_pos="Brazos estirados, palmas hacia abajo y el pecho adelante. Desde ahí arranca el movimiento.",
           sub_1="Codos hacia atrás", vo_1="Paso uno. Bajá doblando los codos hasta que los brazos queden paralelos al piso.",
           bad_pose="UPRIGHT_BAD", bad1=["TRONCO", "DERECHO"], sub_bad1="El pecho no trabaja",
           vo_bad1="Error: quedarte derecho como en un fondo de tríceps. Acá va el pecho adelante y los codos algo abiertos.",
           tips=["Rodillas en la plataforma", "Pecho adelante", "Hombros abajo", "Sin trabar los codos"],
           vo_tips="Tips: rodillas en la plataforma, pecho adelante, hombros abajo y sin trabar los codos.",
           keys=["Bajá en 2 segundos", "Codos algo abiertos", "Pausa abajo", "Subí sin trabar"],
           vo_keys="Claves: bajá en dos segundos, codos algo abiertos, pausa abajo y subí sin trabar los codos.",
           reps="3 X 10", vo_reps="Tres series de diez, con un minuto de pausa. Cuando las diez salen fáciles, bajá el contrapeso.")

V28 = dict(cat="GIMNASIO · BRAZOS", sub_hook="Fondos de tríceps con ayuda",
           vo_hook="Assisted Triceps Dip: fondos de tríceps asistidos de rodillas. El contrapeso te ayuda a completar el recorrido.",
           vo_aj1="Apoyá las rodillas sobre la plataforma, con los brazos estirados y las manos en las paralelas.",
           sub_pos="Tronco casi derecho", lab_grip="CODOS PEGADOS",
           vo_pos="Tronco casi derecho y los brazos pegados al cuerpo. Así el trabajo se va al tríceps.",
           sub_1="Brazos pegados", vo_1="Paso uno. Bajá doblando los codos con los brazos pegados al cuerpo.",
           bad_pose="FORWARD_BAD", bad1=["TIRARTE", "ADELANTE"], sub_bad1="Se vuelve de pecho",
           vo_bad1="Error: tirar el tronco adelante. Se convierte en fondo de pecho y el tríceps deja de trabajar.",
           tips=["Rodillas en la plataforma", "Tronco casi derecho", "Codos pegados", "Sin trabar los codos"],
           vo_tips="Tips: rodillas en la plataforma, tronco casi derecho, codos pegados y sin trabar los codos.",
           keys=["Bajá en 2 segundos", "Codos pegados al cuerpo", "Pausa abajo", "Subí sin trabar"],
           vo_keys="Claves: bajá en dos segundos, codos pegados al cuerpo, pausa abajo y subí sin trabar.",
           reps="3 X 12", vo_reps="Tres series de doce, con un minuto de pausa. Trabajá el tríceps hasta que queme.")

YT27 = {
    "titulo": "Assisted Chest Dip 🔥 Fondos de pecho asistidos de rodillas | Gimnasio",
    "tags": ["assisted chest dip", "fondos asistidos", "fondos de pecho", "chest dip", "máquina asistida",
             "fondos en máquina", "pecho", "pectorales", "tríceps", "empuje",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de pecho"],
    "descripcion": yt_desc("Assisted Chest Dip (Kneeling)", "fondos de pecho asistidos de rodillas",
        "pecho, con tríceps y hombros como apoyo",
        "El contrapeso te ayuda a hacer fondos completos aunque todavía no tengas fuerza. Mirá cómo usarlo.",
        ["Apoyá las rodillas en la plataforma con los brazos estirados.", "Elegí un contrapeso que te deje hacer 10 repeticiones."],
        ["Apoyá las rodillas y agarrá las paralelas con las palmas hacia abajo.",
         "Con el pecho adelante, bajá doblando los codos hasta que los brazos queden paralelos al piso.",
         "Hacé una pausa abajo sin rebotar.",
         "Empujá hasta estirar casi del todo, sin trabar los codos."],
        ["Quedarte con el tronco derecho → pecho adelante y codos algo abiertos.",
         "Encoger los hombros → hombros abajo, lejos de las orejas.",
         "Trabar los codos arriba → estirá casi del todo y frená."],
        ["Rodillas en la plataforma.", "Pecho adelante en todo el recorrido.",
         "Hombros abajo y atrás.", "Bajá en dos segundos y subí sin trabar."],
        "Pectorales · Tríceps · Hombros",
        "3 series de 10 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Fondos #Pecho #AssistedDip #Pectorales #Musculacion #Entrenamiento")}

YT28 = {
    "titulo": "Assisted Triceps Dip 🔥 Fondos de tríceps asistidos de rodillas | Gimnasio",
    "tags": ["assisted triceps dip", "fondos asistidos", "fondos de tríceps", "triceps dip", "máquina asistida",
             "fondos en máquina", "tríceps", "brazos", "pecho", "empuje",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de brazos"],
    "descripcion": yt_desc("Assisted Triceps Dip (Kneeling)", "fondos de tríceps asistidos de rodillas",
        "tríceps, con pecho y hombros como apoyo",
        "Con el tronco casi derecho el tríceps se lleva casi todo el trabajo. Mirá cómo hacerlo en la máquina asistida.",
        ["Apoyá las rodillas en la plataforma con los brazos estirados.", "Elegí un contrapeso que te deje hacer 12 repeticiones."],
        ["Apoyá las rodillas y agarrá las paralelas.",
         "Con el tronco casi derecho, bajá doblando los codos con los brazos pegados al cuerpo.",
         "Hacé una pausa abajo sintiendo el tríceps.",
         "Empujá hasta estirar casi del todo, sin trabar los codos."],
        ["Tirar el tronco adelante → se vuelve un fondo de pecho.",
         "Encoger los hombros → hombros abajo y lejos del cuello.",
         "Trabar los codos arriba → estirá casi del todo y frená."],
        ["Rodillas en la plataforma.", "Tronco casi derecho.",
         "Codos pegados al cuerpo.", "Bajá en dos segundos y subí sin trabar."],
        "Tríceps · Pecho · Hombros",
        "3 series de 12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Fondos #Triceps #AssistedDip #Brazos #Musculacion #Entrenamiento")}

save("assisted-chest-dip-kneeling", dip_scenes("assisted-chest-dip-kneeling", V27),
     {"pose": "BOTTOM", "zoom": 1.05, "dy": 90}, YT27)

save("assisted-triceps-dip-kneeling", dip_scenes("assisted-triceps-dip-kneeling", V28),
     {"pose": "BOTTOM", "zoom": 1.05, "dy": 90}, YT28)
