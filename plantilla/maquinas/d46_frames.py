# Dataset D70 Sled Forward Angled Calf Raise: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def ang_scenes(slug):
    s, S, J = load(slug)
    ANK = S(0, -60); ANK_U = S(6, -24); PAD = S(140, -640)
    HIP = S(0, -470); SHO = S(180, -684); KNEE = S(115, -259)
    PLAT = S(35, -26); CALF = S(70, -400)
    return [
        hook("GIMNASIO · PIERNAS", ["GEMELOS", "INCLINADO AL FRENTE"], "Pecho en la almohadilla",
             "Gemelos inclinado al frente: el pecho va apoyado en la almohadilla y los talones suben y bajan desde la plataforma.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.3, 0.4)]),
        step("LA MÁQUINA", ["PLATAFORMA", "Y ALMOHADILLA"], "Banco a 45°",
             "La plataforma de los pies queda abajo y la almohadilla inclinada a 45 grados sostiene el pecho durante todo el ejercicio.",
             [C("DOWN")], [ring(PLAT, 56, 0.8), lab((1040, 1300), "PLATAFORMA", "end", 0.8),
                          ring(PAD, 62, 1.8), lab((1040, 1000), "ALMOHADILLA", "end", 1.8)], 7.4),
        step("AJUSTE 1 / 2", ["PIES EN", "LA PLATAFORMA"], "Puntas afuera",
             "Parate con la planta de los pies en la plataforma y la punta de los pies apenas hacia afuera.",
             [C("DOWN")], [ring(ANK, 50, 0.8), lab((1040, 1300), "PIES ADENTRO", "end", 1.0),
                          ring(KNEE, 50, 2.0), lab((1040, 1150), "RODILLAS BLANDAS", "end", 2.0)], 7.4),
        step("AJUSTE 2 / 2", ["PECHO EN", "LA ALMOHADILLA"], "Bien apoyado",
             "Apoyá el pecho en la almohadilla y tomate de la parte de arriba, con la espalda derecha.",
             [C("DOWN")], [ring(PAD, 62, 0.8), lab((1040, 1000), "PECHO APOYADO", "end", 1.0)], 7.4),
        step("POSICIÓN INICIAL", ["TALONES", "ABAJO"], "Estiramiento",
             "Arrancá con los talones abajo, sintiendo el estiramiento del gemelo y la planta bien apoyada.",
             [C("DOWN")], [ring(ANK, 50, 0.8), lab((1040, 1300), "TALÓN ABAJO", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ", "LOS TALONES"], "Como pararte de puntas",
             "Paso uno. Subí los talones como si te pararas de puntas, empujando la plataforma con la parte de adelante del pie.",
             [C("DOWN"), TO("UP", 0.6, 1.1)],
             [arrow((900, 1330), (900, 1180), 0.8, 1.1, [40, 0]),
              lab((1040, 1300), "SUBÍ", "end", 1.0)], 7.2),
        step("PASO 2 / 3", ["PAUSA", "ARRIBA"], "Un segundo",
             "Paso dos. Quedate un segundo en la punta más alta, apretando el gemelo antes de bajar.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(CALF, 48, 0.8), lab((1040, 1150), "APRETÁ EL GEMELO", "end", 1.0)], 7.0),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLANDO"], "Hasta estirar",
             "Paso tres. Bajá los talones despacio hasta sentir el estiramiento completo, sin rebotar abajo.",
             [C("UP"), TO("DOWN", 0.5, 1.3)],
             [arrow((1000, 1180), (1000, 1330), 0.8, 1.1, [40, 0]),
              lab((1040, 1420), "BAJÁ LENTO", "end", 1.0)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire al bajar los talones y soltalo al subir. El pecho queda apoyado y no aguantás el aire.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.3, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: subir apenas un poco. Subí hasta la punta más alta y bajá hasta el estiramiento completo.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(S(3, -42), 48, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["DOBLAR", "LAS RODILLAS"], "Rodillas blandas",
             "Error: doblar las rodillas para subir. Las rodillas quedan apenas blandas y no cambian de ángulo.",
             [C("DOWN"), TO("KNEE_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(S(156, -229), 50, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["DESPEGAR", "EL PECHO"], "Pecho apoyado",
             "Error: despegar el pecho de la almohadilla. El pecho queda apoyado de principio a fin.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(S(60, -300), 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pecho apoyado", "Rodillas blandas",
                                         "Recorrido completo", "Pausa en la punta"],
             "Tips: pecho apoyado, rodillas apenas blandas, recorrido completo y una pausa en la punta.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.3, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Pies bien apoyados", "Subí de puntas",
                                     "Sin rebotar", "Bajá hasta estirar"],
             "Claves: pies bien apoyados, subí de puntas, sin rebotar y bajá hasta sentir el estiramiento.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15–20"], "Gemelos",
             "Tres series de quince a veinte repeticiones, con un minuto de pausa. Peso moderado y el recorrido completo.",
             ["1 · SUBÍ", "2 · PAUSA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["BAJÁ", "Y SALÍ"], "Sin apurarse",
             "Al terminar la serie, bajá el peso, soltá las manos y salí del banco despacio, sin encorvarte.",
             [C("UP"), TO("DOWN", 0.9, 2.0)],
             [lab((1040, 1300), "SIN APURARSE", "end", 1.0)], 6.5),
    ]


YT70 = {
    "titulo": "Sled Forward Angled Calf Raise 🔥 Gemelos inclinado al frente | Gimnasio",
    "tags": ["sled forward angled calf raise", "gemelos inclinado", "gemelos", "sóleo",
             "pantorrilla", "banco 45 grados", "piernas", "gemelos en máquina",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Sled Forward Angled Calf Raise",
        "extensión de tobillos inclinado al frente, con el pecho en la almohadilla a 45 grados",
        "gemelos y sóleo",
        "Inclinado al frente con el pecho apoyado, el gemelo trabaja en un ángulo distinto al de la prensa: el cuerpo va adelante y los talones suben desde la plataforma. Es un ejercicio de recorrido largo y controlado. Si cortás el recorrido, doblás las rodillas para empujar o despegás el pecho, la postura se desarma.",
        ["Parate con la planta de los pies en la plataforma, puntas apenas afuera.",
         "Apoyá el pecho en la almohadilla y tomate de la parte de arriba."],
        ["Arrancá con los talones abajo, sintiendo el estiramiento.",
         "Subí los talones como si te pararas de puntas.",
         "Quedate un segundo arriba apretando el gemelo.",
         "Bajá controlando hasta el estiramiento completo.",
         "Terminá la serie, bajá el peso y salí despacio."],
        ["Media repetición → subí hasta la punta y bajá hasta el estiramiento.",
         "Doblar las rodillas → rodillas apenas blandas, sin cambiar de ángulo.",
         "Despegar el pecho → pecho apoyado de principio a fin."],
        ["Pecho apoyado en la almohadilla.", "Rodillas apenas blandas y quietas.",
         "Recorrido completo, sin rebotar.", "Pausa de un segundo en la punta."],
        "Piernas → Gemelos → Sóleo",
        "3 series de 15–20 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Gemelos #Pantorrilla #Soleo #Piernas #Entrenamiento #Fuerza #RutinaDePiernas")}

save("sled-forward-angled-calf-raise", ang_scenes("sled-forward-angled-calf-raise"),
     {"pose": "UP", "zoom": 1.06, "dy": 40}, YT70)
