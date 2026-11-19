# Dataset D98 Smith Standing Back Wrist Curl: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def wc_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(170, -904); PAR = S(450, -700); STOP = S(450, -520); BAR_D = S(*J["DOWN"]["W"])
    BAR_U = S(*J["UP"]["W"]); SHO = S(*J["UP"]["S"]); ELBOW = S(*J["ELBOW_BAD"]["E"])
    HIP = S(*J["DOWN"]["H"]); KNEE = S(*J["DOWN"]["K"]); FOOT = S(48, 0)
    return [
        hook("GIMNASIO · ANTEBRAZOS", ["CURL DE", "MUÑECA"], "Barra a la cadera",
             "Curl de muñeca con barra guiada: brazos rectos, la barra a la altura del muslo y solo las muñecas la suben.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Topes abajo",
             "La Smith te deja la barra guiada a la altura del muslo, con topes para soltarla sin que caiga de golpe.",
             [C("DOWN")], [ring(BEAM, 64, 0.8), lab((60, 860), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 54, 1.8), lab((60, 940), "PARANTE", "start", 1.8),
                           ring(STOP, 54, 2.8), lab((60, 1120), "TOPE", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA AL", "MUSLO"], "Brazos estirados",
             "Ajustá la barra a la altura del muslo, con los brazos estirados y los hombros relajados.",
             [C("DOWN")], [ring(BAR_D, 58, 0.8), lab((60, 860), "BARRA AL MUSLO", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["AGARRE", "PRONO"], "Codos fijos",
             "Agarrá la barra con las palmas hacia atrás, agarre prono, y los codos pegados al cuerpo.",
             [C("DOWN")], [ring(BAR_D, 40, 0.8), lab((60, 860), "AGARRE PRONO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["ESPALDA", "DERECHA"], "Pies al ancho",
             "Arrancá con los pies al ancho de los hombros, la espalda derecha y la barra bien agarrada.",
             [C("DOWN")], [ring(KNEE, 50, 0.8), lab((60, 860), "RODILLA BLANDA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ LAS", "MUÑECAS"], "Estiramiento",
             "Paso uno. Bajá las muñecas hasta el estiramiento completo, sin soltar la barra.",
             [C("DOWN"), TO("DOWN", 0.3, 0.6)], [ring(BAR_D, 58, 0.8), lab((60, 860), "ESTIRÁ ABAJO", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["SUBÍ CON", "LAS MUÑECAS"], "Solo la muñeca",
             "Paso dos. Subí la barra solo con las muñecas, llevándola hacia el cuerpo.",
             [C("DOWN"), TO("UP", 0.5, 0.8)], [ring(BAR_U, 58, 0.8), lab((60, 860), "SOLO MUÑECA", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "DESPACIO"], "Sin soltar",
             "Paso tres. Bajá despacio, sin dejar caer la barra de golpe.",
             [C("UP"), TO("DOWN", 0.5, 1.2)], [ring(BAR_D, 58, 0.8), lab((60, 860), "BAJADA LENTA", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Normal",
             "Respirá normal: soltá el aire al subir y tomá aire al bajar. No aguantes la respiración.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.3, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: media repetición. Bajá hasta el estiramiento completo y subí hasta el tope.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR_U, 58, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["CODOS", "QUE SE MUEVEN"], "Codos fijos",
             "Error: mover los codos. Los codos quedan fijos y solo se mueven las muñecas.",
             [C("DOWN"), TO("ELBOW_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(ELBOW, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["HOMBROS", "ARRIBA"], "Hombros abajo",
             "Error: encoger los hombros. Los hombros quedan abajo y relajados todo el tiempo.",
             [C("DOWN"), TO("SHRUG_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(SHO, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Poco peso", "Codos fijos",
                                          "Recorrido completo", "Bajada lenta"],
             "Tips: poco peso, codos fijos, recorrido completo y bajada lenta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Codos fijos", "Hombros abajo",
                                     "Muñecas completas", "Bajada lenta"],
             "Claves: codos fijos, hombros abajo, muñecas completas y bajada lenta.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12–15"], "Antebrazos",
             "Tres series de doce a quince repeticiones, con un minuto de pausa. Peso liviano.",
             ["1 · BAJÁ", "2 · SUBÍ", "3 · BAJAR"], [C("DOWN"), seqloop("DOWN", "UP", 1.2, 1.2, 0.3)]),
        step("AL TERMINAR", ["SOLTÁ", "LA BARRA"], "Estirá",
             "Al terminar, colgá la barra en los topes y estirá los antebrazos antes de seguir.",
             [C("UP"), TO("DOWN", 0.8, 1.6)],
             [lab((60, 940), "ESTIRÁ EL ANTEBRAZO", "start", 1.0)], 6.5),
    ]


YT98 = {
    "titulo": "Smith Standing Back Wrist Curl 🔥 Curl de muñeca en la Smith | Antebrazos",
    "tags": ["smith standing back wrist curl", "curl de muñeca", "wrist curl", "smith machine",
             "multipower", "antebrazos", "bíceps", "agilidad de muñeca", "gimnasio",
             "principiantes", "rutina de antebrazos"],
    "descripcion": yt_desc("Smith Standing Back Wrist Curl",
        "curl de muñeca con la barra guiada a la altura del muslo y los brazos estirados",
        "antebrazos y bíceps",
        "El curl de muñeca en la Smith se hace parado de frente a la máquina, con la barra a la altura del muslo y agarre prono. Los brazos quedan estirados y los codos fijos: solo las muñecas suben la barra hacia el cuerpo y la bajan despacio hasta el estiramiento completo. Es un ejercicio de antebrazo, así que el peso va liviano y las repeticiones son altas. Los errores típicos son cortar el recorrido, mover los codos para ayudar y encoger los hombros.",
        ["Ajustá la barra a la altura del muslo.",
         "Agarrá la barra con agarre prono y los codos pegados al cuerpo."],
        ["Arrancá con los pies al ancho de los hombros y la espalda derecha.",
         "Bajá las muñecas hasta el estiramiento completo.",
         "Subí la barra solo con las muñecas, hacia el cuerpo.",
         "Bajá despacio, sin soltar la barra.",
         "Completá la serie con un peso liviano."],
        ["Media repetición → bajá hasta abajo y subí hasta el tope.",
         "Codos que se mueven → los codos quedan fijos.",
         "Hombros arriba → los hombros quedan abajo y relajados."],
        ["Poco peso y muchas repeticiones.", "Codos pegados al cuerpo.",
         "Recorrido completo de la muñeca.", "Bajada lenta y controlada."],
        "Antebrazos → Bíceps",
        "3 series de 12–15 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Antebrazos #Biceps #WristCurl #SmithMachine #Multipower #Fuerza #Entrenamiento")}

save("smith-standing-back-wrist-curl", wc_scenes("smith-standing-back-wrist-curl"),
     {"pose": "UP", "zoom": 1.0, "dy": 60}, YT98)
