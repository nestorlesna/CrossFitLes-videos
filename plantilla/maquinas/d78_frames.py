# Dataset D102 Smith Sumo Squat: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def sumo_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(-80, -924); PAR = S(220, -650); STOP = S(220, -560)
    BAR = S(*J["BOTTOM"]["W"]); ANK = S(*J["BOTTOM"]["A"])
    HIP_B = S(*J["BOTTOM"]["H"]); KNEE_B = S(*J["BOTTOM"]["K"])
    NECK = S(*J["TOP"]["N"])
    return [
        hook("GIMNASIO · PIERNAS", ["SENTADILLA", "SUMO"], "Pies bien abiertos",
             "Sentadilla sumo en la Smith: barra en la espalda alta, pies bien separados y puntas hacia afuera.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "El recorrido es vertical",
             "La barra de la Smith corre por los parantes: el recorrido es vertical y no se te va hacia adelante.",
             [C("TOP")], [ring(BEAM, 64, 0.8), lab((60, 860), "BARRA GUIADA", "start", 0.8),
                          ring(PAR, 54, 1.8), lab((60, 940), "PARANTE", "start", 1.8),
                          ring(STOP, 54, 2.8), lab((60, 1120), "TOPE", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["PIES", "ABIERTOS"], "Puntas hacia afuera",
             "Poné los pies más abiertos que el ancho de los hombros, con las puntas bien hacia afuera.",
             [C("BOTTOM")], [ring(ANK, 46, 0.8), lab((60, 1250), "PIES ABIERTOS", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["BARRA A LA", "ESPALDA"], "Sobre los omóplatos",
             "Apoyá la barra en la espalda alta, sobre los omóplatos, y agarrala firme a los costados.",
             [C("TOP")], [ring(BAR, 56, 0.8), lab((60, 860), "ESPALDA ALTA", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["PECHO", "ARRIBA"], "Rodillas abiertas",
             "Arrancá con el pecho arriba, la espalda derecha y las rodillas apuntando hacia afuera.",
             [C("TOP")], [ring(NECK, 48, 0.8), lab((60, 830), "PECHO ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ Y", "ABRÍ"], "Cadera atrás",
             "Paso uno. Bajá llevando la cadera hacia atrás y abriendo las rodillas hacia afuera.",
             [C("TOP"), TO("BOTTOM", 0.4, 1.1)], [ring(HIP_B, 52, 0.8), lab((1030, 1180), "CADERA ATRÁS", "end", 1.0)], 7.6),
        step("PASO 2 / 3", ["HASTA", "ABAJO"], "Muslos cerca de la paralela",
             "Paso dos. Bajá hasta que los muslos queden cerca de la paralela, con el torso derecho.",
             [C("BOTTOM"), TO("BOTTOM", 0.2, 0.5)], [ring(KNEE_B, 50, 0.8), lab((60, 1120), "RODILLAS AFUERA", "start", 1.0)], 7.4),
        step("PASO 3 / 3", ["EMPUJÁ", "CON LOS TALONES"], "Subida firme",
             "Paso tres. Subí empujando con los talones y apretando los glúteos, sin juntar las rodillas.",
             [C("BOTTOM"), TO("TOP", 0.4, 1.2)], [ring(ANK, 46, 0.8), lab((1030, 1250), "TALONES", "end", 1.0)], 7.4),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al bajar",
             "Tomá aire arriba, aguantá mientras bajás y soltá al subir. El abdomen queda firme.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Bajá completo",
             "Error: media repetición. Bajá hasta abajo y subí completo: el recorrido se hace entero.",
             [C("TOP"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(S(*J["HALF_BAD"]["H"]), 52, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["PIES", "JUNTOS"], "Base bien abierta",
             "Error: juntar los pies. La base queda bien abierta y las rodillas siguen la línea de los pies.",
             [C("BOTTOM"), TO("NARROW_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(ANK, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TALONES", "DESPEGADOS"], "Pies planos",
             "Error: levantar los talones. Los pies quedan planos y el empuje sale de todo el pie.",
             [C("BOTTOM"), TO("HEEL_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(S(60, -12), 46, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pies bien abiertos", "Rodillas afuera",
                                          "Pecho arriba", "Empujá con los talones"],
             "Tips: pies bien abiertos, rodillas afuera, pecho arriba y empuje con los talones.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Base amplia", "Cadera atrás",
                                     "Torso derecho", "Subida completa"],
             "Claves: base amplia, cadera atrás, torso derecho y subida completa.",
             [{"cut": "BOTTOM", "at": 0.1}]),
        reps(["3 X 12–15"], "Glúteos y cuádriceps",
             "Tres series de doce a quince repeticiones, con un minuto de pausa.",
             ["1 · BAJÁ", "2 · ABRÍ", "3 · EMPUJÁ"], [C("TOP"), seqloop("TOP", "BOTTOM", 1.2, 1.2, 0.3)]),
        step("AL TERMINAR", ["SOLTÁ LA", "BARRA"], "Sin apurarte",
             "Al terminar la serie, subí derecho y enganchá la barra en los topes. Respirá antes de seguir.",
             [C("TOP"), TO("TOP", 0.6, 0.8)],
             [lab((60, 900), "ENGANCHÁ LA BARRA", "start", 1.0)], 6.5),
    ]


YT102 = {
    "titulo": "Smith Sumo Squat 🔥 Sentadilla sumo en la máquina | Glúteos y piernas",
    "tags": ["smith sumo squat", "sentadilla sumo", "sumo squat", "glúteos", "piernas",
             "smith machine", "multipower", "sentadilla", "cuádriceps", "gimnasio",
             "principiantes", "rutina de glúteos"],
    "descripcion": yt_desc("Smith Sumo Squat",
        "sentadilla sumo con la barra guiada apoyada en la espalda alta y una base bien amplia",
        "glúteos y cuádriceps",
        "La sentadilla sumo en la Smith se hace con la barra apoyada en la espalda alta, los pies más abiertos que el ancho de los hombros y las puntas hacia afuera. Bajás llevando la cadera atrás y abriendo las rodillas, hasta que los muslos queden cerca de la paralela, y subís empujando con los talones. El pecho queda arriba y los pies planos todo el tiempo. Los errores típicos son cortar el recorrido, juntar los pies y levantar los talones.",
        ["Poné los pies bien abiertos, con las puntas hacia afuera.",
         "Apoyá la barra en la espalda alta, sobre los omóplatos."],
        ["Arrancá con el pecho arriba y las rodillas apuntando afuera.",
         "Bajá llevando la cadera atrás y abriendo las rodillas.",
         "Llegá hasta que los muslos queden cerca de la paralela.",
         "Subí empujando con los talones y apretando los glúteos.",
         "Volvé a la posición inicial y repetí."],
        ["Media repetición → bajá hasta abajo y subí completo.",
         "Pies juntos → la base queda bien abierta.",
         "Talones despegados → los pies quedan planos."],
        ["Base bien amplia y firme.", "Cadera atrás, rodillas afuera.",
         "Pecho arriba, pies planos.", "Empuje con los talones."],
        "Piernas → Glúteos → Cuádriceps",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Glúteos #Piernas #Sentadilla #SumoSquat #SmithMachine #Multipower #Entrenamiento")}

save("smith-sumo-squat", sumo_scenes("smith-sumo-squat"),
     {"pose": "BOTTOM", "zoom": 1.0, "dy": 60}, YT102)
