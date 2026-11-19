# Dataset D82 Smith Hack Squat: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def hk_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(0, -884); PAR = S(300, -640); STOP = S(300, -300)
    BAR = S(0, -427); BAR_D = S(0, -285)
    HIP = S(0, -462); HIP_D = S(-50, -235); HIP_H = S(-20, -360)
    KNEE = S(61, -230); KNEE_D = S(186, -192); BACK = S(25, -600)
    FOOT = S(60, 0); FOOT2 = S(20, 0); HEAD_L = S(80, -518)
    return [
        hook("GIMNASIO · PIERNAS", ["HACK", "SQUAT"], "Barra detrás",
             "Hack squat en la Smith: la barra va detrás de las piernas y el cuerpo se recuesta en ella al bajar.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.5, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes y los topes te dejan una salida de seguridad a la altura justa.",
             [C("UP")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                         ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                         ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA", "DETRÁS"], "Pegada a las piernas",
             "La barra va detrás de las piernas, a la altura de la cadera, y la espalda se recuesta en ella.",
             [C("UP")], [ring(BAR, 62, 0.8), lab((60, 800), "BARRA DETRÁS", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES", "ADELANTE"], "Base firme",
             "Pies al ancho de la cadera y un poco adelante de la barra, con las puntas afuera.",
             [C("UP")], [ring(FOOT, 50, 0.8), ring(FOOT2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["RECOSTADO", "EN LA BARRA"], "Pecho arriba",
             "Arrancá de pie, recostado en la barra y con el pecho arriba, el abdomen firme y los brazos relajados.",
             [C("UP")], [ring(BACK, 62, 0.8), lab((60, 800), "PECHO ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "CON LA ESPALDA"], "Pegado a la barra",
             "Paso uno. Bajá controlado con la espalda pegada a la barra y las rodillas viajando adelante.",
             [C("UP"), TO("DOWN", 0.4, 1.3)], [ring(KNEE_D, 54, 0.8), lab((60, 800), "RODILLAS ADELANTE", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["TALONES", "ABAJO"], "Pie entero",
             "Paso dos. En el fondo los talones siguen abajo y el torso queda casi vertical, recostado en la barra.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(FOOT, 52, 0.8), lab((60, 800), "TALONES ABAJO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["SUBÍ", "EMPUJANDO"], "Todo el pie",
             "Paso tres. Subí empujando el piso con todo el pie y extendiendo las rodillas, sin despegar la espalda.",
             [C("DOWN"), TO("UP", 0.5, 1.3)], [ring(HIP, 56, 0.8), lab((60, 800), "EMPUJÁ EL PISO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire arriba, aguantá mientras bajás y soltalo al subir. No sueltes el aire en el fondo.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.5, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "SENTADILLA"], "Hasta el fondo",
             "Error: quedarte a mitad de camino. Bajá hasta el fondo manteniendo la espalda pegada a la barra.",
             [C("UP"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP_H, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["SACAR", "EL PECHO"], "Torso vertical",
             "Error: despegar la espalda y sacar el pecho. La espalda viaja pegada a la barra todo el recorrido.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HEAD_L, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TALONES", "AFUERA"], "Pie entero",
             "Error: despegar los talones en el fondo. Si no llegás con los talones abajo, no bajes tanto.",
             [C("DOWN"), TO("HEELS_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(FOOT, 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Espalda en la barra", "Rodillas adelante",
                                          "Talones abajo", "Subí empujando"],
             "Tips: espalda pegada a la barra, rodillas adelante, talones abajo y subí empujando el piso.",
             [C("UP"), seqloop("UP", "DOWN", 1.2, 1.3, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Recorrido completo", "Torso vertical",
                                    "Rodillas alineadas", "Subida controlada"],
             "Claves: recorrido completo, torso vertical, rodillas alineadas y subida controlada.",
             [{"cut": "DOWN", "at": 0.1}]),
        reps(["3 X 8–10"], "Cuádriceps y glúteo",
             "Tres series de ocho a diez repeticiones, con un minuto y medio de pausa. Bajada lenta y sin rebote.",
             ["1 · BAJÁ", "2 · RODILLAS", "3 · SUBÍ"], [C("UP"), seqloop("UP", "DOWN", 1.3, 1.4, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN EL TOPE"], "Sin apuro",
             "Al terminar la serie, subí derecho, apoyá la barra en los topes y salí de la máquina.",
             [C("DOWN"), TO("UP", 0.9, 2.2)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT82 = {
    "titulo": "Smith Hack Squat 🔥 Barra detrás de las piernas | Cuádriceps",
    "tags": ["smith hack squat", "hack squat", "smith machine", "multipower", "cuádriceps", "glúteo", "aductor",
             "piernas", "gimnasio", "intermedio", "rutina de piernas"],
    "descripcion": yt_desc("Smith Hack Squat",
        "hack squat con barra guiada en la máquina Smith",
        "cuádriceps y glúteo",
        "El hack squat en la Smith se hace con la barra detrás de las piernas: el cuerpo se recuesta en ella, la espalda viaja pegada a la barra y las rodillas van adelante mientras bajás con el torso casi vertical. Esa posición deja el cuádriceps con más recorrido y menos carga en la espalda baja que una sentadilla normal. Los errores clásicos son quedarse a media altura, despegar la espalda de la barra sacando el pecho y levantar los talones en el fondo.",
        ["Apoyá la barra detrás de las piernas y recostate en ella.",
         "Pies al ancho de la cadera, un poco adelante de la barra."],
        ["Bajá controlado con la espalda pegada a la barra.",
         "Dejá que las rodillas viajen adelante.",
         "Mantené los talones apoyados en el fondo.",
         "Subí empujando el piso con todo el pie.",
         "Completá la serie y dejá la barra en los topes."],
        ["Media sentadilla → bajá hasta el fondo.", "Sacar el pecho → espalda pegada a la barra.",
         "Talones afuera → si no llegás, no bajes tanto."],
        ["Espalda siempre en la barra.", "Rodillas adelante, alineadas con los pies.",
         "Talones pegados al piso.", "Sin rebote en el fondo."],
        "Piernas → Cuádriceps → Glúteo",
        "3 series de 8–10 repeticiones, con 1½ minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #HackSquat #SmithMachine #Cuadriceps #Gluteo #Piernas #Entrenamiento #Fuerza")}

save("smith-hack-squat", hk_scenes("smith-hack-squat"),
     {"pose": "DOWN", "zoom": 1.02, "dy": 20}, YT82)
