# Dataset D97 Smith Sprint Lunge: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def split_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(-60, -924); BAR = S(*J["TOP"]["W"]); PAR = S(240, -620); STOP = S(-360, -560)
    STEP = S(-350, -86); KNEE_T = S(*J["TOP"]["K"]); KNEE_B = S(*J["BOTTOM"]["K"])
    HIP = S(*J["BOTTOM"]["H"]); FOOT = S(130, 0); SHORT = S(30, 0)
    return [
        hook("GIMNASIO · PIERNAS", ["ZANCADA", "SPRINT"], "Barra en la espalda",
             "Zancada sprint en la Smith: barra en la espalda, un pie adelante y el empeine del otro sobre el soporte bajo.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 1.3, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Soporte bajo atrás",
             "La Smith te da la barra guiada para apoyarla en la espalda alta y un soporte bajo atrás para el pie que queda elevado.",
             [C("TOP")], [ring(BEAM, 64, 0.8), lab((60, 860), "BARRA GUIADA", "start", 0.8),
                          ring(PAR, 54, 1.8), lab((60, 940), "PARANTE", "start", 1.8),
                          ring(STEP, 60, 2.8), lab((60, 1180), "SOPORTE", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A LA", "ESPALDA"], "Omóplatos juntos",
             "Apoyá la barra en la espalda alta, con los omóplatos bien juntos y las manos agarradas a la barra.",
             [C("TOP")], [ring(BAR, 58, 0.8), lab((60, 860), "ESPALDA ALTA", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["PIE ATRÁS", "AL SOPORTE"], "Punta hacia abajo",
             "Adelantá un pie y apoyá el empeine del otro sobre el soporte bajo de la máquina, con la punta hacia abajo.",
             [C("TOP")], [ring(STEP, 60, 0.8), lab((60, 1120), "PIE ATRÁS", "start", 1.0),
                          ring(FOOT, 50, 1.8), lab((1030, 1240), "PIE ADELANTE", "end", 1.8)], 7.4),
        step("POSICIÓN INICIAL", ["TORSO", "DERECHO"], "Rodilla blanda",
             "Arrancá con el torso derecho, la rodilla de adelante blanda y el peso repartido sobre el pie de adelante.",
             [C("TOP")], [ring(KNEE_T, 50, 0.8), lab((60, 860), "RODILLA BLANDA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "DOBLANDO"], "Rodilla adelante",
             "Paso uno. Bajá doblando la rodilla de adelante, con el torso derecho y la rodilla siguiendo la punta del pie.",
             [C("TOP"), TO("BOTTOM", 0.4, 1.1)], [ring(KNEE_B, 50, 0.8), lab((60, 860), "RODILLA ADELANTE", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["ABAJO", "FIRME"], "Sin rebotar",
             "Paso dos. Llegá abajo con control, sin rebotar y sin que la rodilla se meta para adentro.",
             [C("BOTTOM"), TO("BOTTOM", 0.2, 0.5)], [ring(HIP, 50, 0.8), lab((60, 860), "CONTROLÁ ABAJO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["SUBÍ CON", "EL TALÓN"], "Rápido y firme",
             "Paso tres. Subí rápido empujando con el talón de adelante, como si arrancaras a correr.",
             [C("BOTTOM"), TO("TOP", 0.4, 1.0)], [ring(FOOT, 50, 0.8), lab((1030, 1240), "TALÓN AL PISO", "end", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire cuando bajás y soltalo cuando subís. Mantené el abdomen firme en todo el recorrido.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 1.3, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Bajá hasta abajo",
             "Error: media repetición. Bajá hasta abajo con control y subí hasta estirar la pierna.",
             [C("TOP"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP, 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TALÓN", "DESPEGADO"], "Pie completo",
             "Error: levantar el talón de adelante. El pie va completo en el piso y empujás con el talón.",
             [C("TOP"), TO("HEEL_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(FOOT, 50, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["PASO", "MUY CORTO"], "Paso cómodo",
             "Error: paso muy corto. La rodilla se va muy adelante y el peso se escapa; adelantá más el pie.",
             [C("TOP"), TO("SHORT_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(SHORT, 48, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra a la espalda", "Paso cómodo",
                                          "Rodilla a la punta", "Subí con el talón"],
             "Tips: barra en la espalda alta, paso cómodo, torso derecho y subí con el talón.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 1.3, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Torso derecho", "Rodilla estable",
                                     "Pie completo", "Sin impulso atrás"],
             "Claves: torso derecho, rodilla estable, pie completo y sin impulso de la pierna de atrás.",
             [{"cut": "BOTTOM", "at": 0.1}]),
        reps(["3 X 8–10"], "Cuádriceps y glúteo",
             "Tres series de ocho a diez repeticiones por pierna, con un minuto y medio de pausa. Peso liviano.",
             ["1 · BAJÁ", "2 · ABAJO", "3 · SUBÍ"], [C("TOP"), seqloop("TOP", "BOTTOM", 1.3, 1.2, 0.3)]),
        step("AL TERMINAR", ["CAMBIÁ", "DE PIERNA"], "Sin apurarte",
             "Al terminar la serie, soltá la barra, bajá el pie del soporte y cambiá de pierna. Descansá antes de seguir.",
             [C("TOP"), TO("BOTTOM", 0.8, 1.6)],
             [lab((60, 860), "CAMBIÁ DE PIERNA", "start", 1.0)], 6.5),
    ]


YT97 = {
    "titulo": "Smith Sprint Lunge 🔥 Zancada sprint en la Smith | Piernas",
    "tags": ["smith sprint lunge", "zancada sprint", "zancadas en smith", "smith machine",
             "multipower", "cuádriceps", "glúteos", "isquiotibiales", "piernas", "gimnasio",
             "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Smith Sprint Lunge",
        "zancada con la barra en la espalda alta y el pie de atrás sobre el soporte bajo de la máquina",
        "cuádriceps, glúteos e isquiotibiales",
        "La zancada sprint en la Smith se hace con la barra apoyada en la espalda alta, un pie adelante en el piso y el empeine del otro sobre el soporte bajo de la máquina. Bajás doblando la rodilla de adelante, con el torso derecho y la rodilla siguiendo la punta del pie; subís rápido empujando con el talón de adelante, como si arrancaras a correr. Es un trabajo de una sola pierna, así que el peso va liviano y la serie se completa de cada lado. Los errores típicos son cortar el recorrido, despegar el talón y dar un paso demasiado corto.",
        ["Apoyá la barra en la espalda alta, con los omóplatos juntos.",
         "Adelantá un pie y apoyá el empeine del otro sobre el soporte bajo."],
        ["Arrancá con el torso derecho y la rodilla de adelante blanda.",
         "Bajá doblando la rodilla de adelante, con la rodilla hacia la punta del pie.",
         "Llegá abajo con control, sin rebotar.",
         "Subí rápido empujando con el talón de adelante.",
         "Completá la serie y cambiá de pierna."],
        ["Media repetición → bajá hasta abajo y subí hasta estirar.",
         "Talón despegado → el pie queda completo en el piso.",
         "Paso muy corto → adelantá más el pie para que la rodilla no se vaya."],
        ["Barra en la espalda alta.", "Paso cómodo, ni corto ni largo.",
         "Rodilla siguiendo la punta del pie.", "Subí empujando con el talón."],
        "Piernas → Cuádriceps → Glúteos → Isquiotibiales",
        "3 series de 8–10 repeticiones por pierna, con 1 minuto y medio de pausa. Nivel: intermedio.",
        "#Gimnasio #Piernas #Cuadriceps #Gluteos #SmithMachine #Multipower #Zancadas #Entrenamiento")}

save("smith-sprint-lunge", split_scenes("smith-sprint-lunge"),
     {"pose": "BOTTOM", "zoom": 1.0, "dy": 60}, YT97)
