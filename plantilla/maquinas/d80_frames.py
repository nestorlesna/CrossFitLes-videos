# Dataset D104 Smith Upright Row: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def ur_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(130, -904); PAR = S(410, -600); STOP = S(410, -520)
    BAR_D = S(*J["DOWN"]["W"]); BAR_U = S(*J["UP"]["W"])
    SHO = S(75, -705); TRAP = S(-20, -772); CHIN = S(40, -760)
    ELBOW = S(*J["UP"]["E"]); BAR_F = S(*J["FAR_BAD"]["W"])
    return [
        hook("GIMNASIO · HOMBROS", ["REMO AL", "MENTÓN"], "Barra pegada al cuerpo",
             "Remo al mentón en la Smith: la barra sube pegada al cuerpo desde los muslos hasta el mentón.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.0, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "El carril no se mueve",
             "En la Smith la barra corre por el carril: no se te va ni adelante ni atrás, sube derecha.",
             [C("DOWN")], [ring(BEAM, 64, 0.8), lab((60, 860), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 54, 1.8), lab((60, 940), "PARANTE", "start", 1.8),
                           ring(STOP, 54, 2.8), lab((60, 1120), "TOPE", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["AGARRE", "ANGOSTO"], "Manos cerca",
             "Agarrá la barra con las manos más juntas que el ancho de los hombros y los pulgares cerrados.",
             [C("DOWN")], [ring(BAR_D, 56, 0.8), lab((60, 1120), "AGARRE CERRADO", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["BARRA AL", "CUERPO"], "Pegada al torso",
             "Dejá la barra pegada al cuerpo, a la altura de los muslos, y el torso bien derecho.",
             [C("DOWN")], [ring(BAR_D, 56, 0.8), lab((60, 1060), "BARRA PEGADA", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["BRAZOS", "LARGOS"], "Sin encogerte",
             "Arrancá con los brazos largos, los hombros abajo y el abdomen firme.",
             [C("DOWN")], [ring(SHO, 52, 0.8), lab((60, 840), "HOMBROS ABAJO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ CON", "LOS CODOS"], "Los codos guían",
             "Paso uno. Subí la barra guiando con los codos, que van arriba y afuera, no con las manos.",
             [C("DOWN"), TO("UP", 0.4, 1.1)], [ring(ELBOW, 48, 0.8), lab((1030, 900), "CODO ARRIBA", "end", 1.0)], 7.6),
        step("PASO 2 / 3", ["HASTA EL", "MENTÓN"], "Altura justa",
             "Paso dos. Llegá hasta el mentón, sin pasar más arriba ni encogerte de hombros.",
             [C("UP"), TO("UP", 0.2, 0.5)], [ring(CHIN, 50, 0.8), lab((1030, 760), "AL MENTÓN", "end", 1.0)], 7.4),
        step("PASO 3 / 3", ["BAJÁ", "DESPACIO"], "Control total",
             "Paso tres. Bajá la barra despacio hasta los muslos, sin dejarla caer.",
             [C("UP"), TO("DOWN", 0.4, 1.2)], [ring(BAR_D, 56, 0.8), lab((60, 1060), "HASTA LOS MUSLOS", "start", 1.0)], 7.4),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Soltá el aire al subir la barra y tomá aire al bajarla. El abdomen queda firme.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.0, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Hasta el mentón",
             "Error: media repetición. Subí la barra hasta el mentón, no hasta la panza.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(SHO, 52, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["BARRA", "LEJOS"], "Pegada al cuerpo",
             "Error: alejar la barra. La barra sube pegada al cuerpo, los codos bien cerca.",
             [C("UP"), TO("FAR_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR_F, 56, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["HOMBROS", "ARRIBA"], "Cuello libre",
             "Error: encogerse. Los hombros quedan abajo y el cuello libre durante todo el movimiento.",
             [C("UP"), TO("SHRUG_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(TRAP, 48, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra pegada", "Codos arriba",
                                          "Hasta el mentón", "Bajada lenta"],
             "Tips: barra pegada, codos arriba, hasta el mentón y bajada lenta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.0, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Agarre angosto", "Codos guían",
                                     "Sin encogerse", "Torso firme"],
             "Claves: agarre angosto, los codos guían, sin encogerse y torso firme.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 10–12"], "Hombros y trapecio",
             "Tres series de diez a doce repeticiones, con un minuto de pausa.",
             ["1 · SUBÍ", "2 · MENTÓN", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "UP", 1.0, 1.2, 0.3)]),
        step("AL TERMINAR", ["SOLTÁ LA", "BARRA"], "Sin soltar el torso",
             "Al terminar la serie, apoyá la barra en los topes y aflojá los hombros. Respirá antes de seguir.",
             [C("DOWN"), TO("DOWN", 0.6, 0.8)],
             [lab((60, 1060), "APOYÁ LA BARRA", "start", 1.0)], 6.5),
    ]


YT104 = {
    "titulo": "Smith Upright Row 🔥 Remo al mentón en la máquina | Hombros y trapecio",
    "tags": ["smith upright row", "remo al mentón", "upright row", "hombros", "trapecio",
             "smith machine", "multipower", "deltoides", "gimnasio",
             "principiantes", "rutina de hombros"],
    "descripcion": yt_desc("Smith Upright Row",
        "remo al mentón con la barra guiada pegada al cuerpo, desde los muslos hasta el mentón",
        "deltoides, trapecio y bíceps",
        "El remo al mentón en la Smith se hace parado, con un agarre angosto y la barra pegada al cuerpo. La barra sube desde los muslos hasta el mentón guiando con los codos, que van arriba y afuera, y baja despacio. El torso queda derecho y los hombros abajo, sin encogerse. Los errores típicos son cortar el recorrido, alejar la barra del cuerpo y encogerse de hombros.",
        ["Agarrá la barra con las manos más juntas que el ancho de los hombros.",
         "Dejá la barra pegada al cuerpo, a la altura de los muslos."],
        ["Arrancá con los brazos largos y los hombros abajo.",
         "Subí la barra guiando con los codos arriba.",
         "Llegá hasta el mentón, sin pasarte.",
         "Bajá la barra despacio hasta los muslos.",
         "Completá la serie sin encogerte."],
        ["Media repetición → subí hasta el mentón.",
         "Barra lejos → la barra sube pegada al cuerpo.",
         "Hombros arriba → los hombros quedan abajo."],
        ["Barra pegada al cuerpo.", "Los codos guían el movimiento.",
         "Altura justa: hasta el mentón.", "Bajada lenta y controlada."],
        "Hombros → Deltoides → Trapecio",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Hombros #Trapecio #UprightRow #SmithMachine #Multipower #Deltoides #Entrenamiento")}

save("smith-upright-row", ur_scenes("smith-upright-row"),
     {"pose": "UP", "zoom": 1.0, "dy": 60}, YT104)
