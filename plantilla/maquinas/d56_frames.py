# Dataset D80 Smith Front Squat Clean Grip: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def fs_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(90, -884); PAR = S(390, -640); STOP = S(390, -520)
    BAR = S(90, -626); BAR_D = S(90, -381)
    HIP = S(10, -462); HIP_D = S(-55, -262); HIP_H = S(-15, -368)
    KNEE = S(71, -230); KNEE_D = S(176, -198); BACK = S(30, -600)
    FOOT = S(60, 0); FOOT2 = S(-20, 0); HEAD_L = S(186, -442)
    return [
        hook("GIMNASIO · PIERNAS", ["SENTADILLA", "FRONTAL"], "Agarre de cargada",
             "Sentadilla frontal en la Smith: la barra delante de los hombros, los codos altos y el pecho arriba.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.4, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes: el recorrido es una vertical y los topes te marcan la salida.",
             [C("UP")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                         ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                         ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA", "ADELANTE"], "Sobre los hombros",
             "Sacá la barra de los ganchos y apoyala delante de los hombros, sobre el pecho alto, con los codos arriba.",
             [C("UP")], [ring(BAR, 62, 0.8), lab((60, 800), "BARRA ADELANTE", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES AL", "ANCHO"], "Puntas afuera",
             "Parate con los pies al ancho de la cadera y las puntas un poco hacia afuera, con las rodillas blandas.",
             [C("UP")], [ring(FOOT, 50, 0.8), ring(FOOT2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["CODOS", "ALTOS"], "Pecho arriba",
             "Arrancá con los codos bien altos, el pecho arriba y la mirada al frente: la barra no se mueve de ahí.",
             [C("UP")], [ring(BAR, 60, 0.8), lab((60, 800), "CODOS ALTOS", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "DERECHO"], "Torso vertical",
             "Paso uno. Bajá en la vertical con el torso lo más derecho posible, llevando la cola atrás y abajo.",
             [C("UP"), TO("DOWN", 0.4, 1.1)], [ring(HIP_D, 58, 0.8), lab((60, 800), "TORSO DERECHO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["RODILLAS", "BLANDAS"], "Hasta abajo",
             "Paso dos. Bajá hasta donde llegues sin perder la espalda: las rodillas blandas y alineadas con los pies.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(KNEE_D, 52, 0.8), lab((60, 800), "RODILLAS BLANDAS", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["SUBÍ CON", "EL PECHO"], "Empujá el piso",
             "Paso tres. Subí empujando el piso con todo el pie y subiendo el pecho primero, sin adelantarlo.",
             [C("DOWN"), TO("UP", 0.5, 1.2)], [ring(BAR, 58, 0.8), lab((60, 800), "SUBÍ EL PECHO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire arriba, aguantá mientras bajás y soltalo al subir. No pierdas el aire en el fondo.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.4, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "SENTADILLA"], "Hasta abajo",
             "Error: quedarte a mitad de camino. Bajá hasta donde puedas mantener la espalda recta.",
             [C("UP"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP_H, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["CAER", "ADELANTE"], "Codos altos",
             "Error: caer adelante con los codos abajo. Si los codos suben, la barra se queda sobre los hombros.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HEAD_L, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TALONES", "AFUERA"], "Pie entero",
             "Error: levantar los talones. El pie va entero en el piso, con el peso repartido de punta a talón.",
             [C("DOWN"), TO("HEEL_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(FOOT, 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra en el pecho", "Codos altos",
                                          "Torso derecho", "Pie entero"],
             "Tips: barra en el pecho alto, codos altos, torso derecho y el pie entero en el piso.",
             [C("UP"), seqloop("UP", "DOWN", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Codos arriba", "Pecho alto",
                                    "Rodillas afuera", "Subida controlada"],
             "Claves: codos arriba, pecho alto, rodillas afuera y subida controlada.",
             [{"cut": "DOWN", "at": 0.1}]),
        reps(["3 X 8–10"], "Cuádriceps y glúteo",
             "Tres series de ocho a diez repeticiones, con un minuto y medio de pausa. Peso moderado y bajada lenta.",
             ["1 · BAJÁ", "2 · RODILLAS", "3 · SUBÍ"], [C("UP"), seqloop("UP", "DOWN", 1.2, 1.2, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN LOS GANCHOS"], "Sin apuro",
             "Al terminar la serie, subí derecho y dejá la barra en los ganchos antes de soltar las manos.",
             [C("DOWN"), TO("UP", 0.9, 2.0)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT80 = {
    "titulo": "Smith Front Squat Clean Grip 🔥 Sentadilla frontal en la Smith | Piernas",
    "tags": ["smith front squat", "sentadilla frontal", "clean grip", "agarre de cargada", "smith machine",
             "multipower", "cuádriceps", "glúteo", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Smith Front Squat Clean Grip",
        "sentadilla frontal con barra guiada en la máquina Smith",
        "cuádriceps y glúteo",
        "La sentadilla frontal en la Smith pone la barra delante de los hombros, sobre el pecho alto, con los codos arriba en agarre de cargada. Como la barra va guiada en una sola vertical, el torso se mantiene más derecho y el trabajo se concentra en cuádriceps y glúteo. Si los codos caen, la barra se va adelante y la espalda se lleva la carga; si te quedás a media altura o levantás los talones, perdés el recorrido.",
        ["Sacá la barra de los ganchos y apoyala delante de los hombros.",
         "Pies al ancho de la cadera, puntas afuera y rodillas blandas."],
        ["Arrancá con los codos bien altos y el pecho arriba.",
         "Bajá en la vertical llevando la cola atrás y abajo.",
         "Mantené las rodillas alineadas con los pies.",
         "Subí empujando el piso y subiendo el pecho primero.",
         "Completá la serie y dejá la barra en los ganchos."],
        ["Media sentadilla → bajá hasta donde controlás.",
         "Caer adelante → codos altos y pecho arriba.",
         "Talones afuera → pie entero en el piso."],
        ["Barra en el pecho alto, no en la nuca.", "Codos altos y adelante.",
         "Torso lo más derecho posible.", "Subida controlada, sin rebotar."],
        "Piernas → Cuádriceps → Glúteo",
        "3 series de 8–10 repeticiones, con 1½ minuto de pausa. Nivel: intermedio.",
        "#Gimnasio #SentadillaFrontal #SmithMachine #Cuadriceps #Gluteo #Piernas #Entrenamiento #Fuerza")}

save("smith-front-squat-clean-grip", fs_scenes("smith-front-squat-clean-grip"),
     {"pose": "DOWN", "zoom": 1.02, "dy": 20}, YT80)
