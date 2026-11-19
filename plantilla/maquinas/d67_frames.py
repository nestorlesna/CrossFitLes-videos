# Dataset D91 Smith Reverse Calf Raises: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def calf_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(210, -968); PAR = S(370, -620); STOP = S(370, -500)
    BAR = S(70, -780); STEP = S(40, -74); TOE = S(-30, -58); HEEL = S(95, -20)
    KNEE = S(70, -284); SHIN = S(58, -170); LUMB = S(25, -560)
    return [
        hook("GIMNASIO · PIERNAS", ["GEMELO", "INVERTIDO"], "Tibial anterior",
             "Smith Reverse Calf Raises: elevación de las puntas de los pies con la barra en la espalda.",
             [C("STAND"), seqloop("STAND", "UP", 1.2, 1.3, 0.4)]),
        step("LA MÁQUINA", ["BARRA Y", "CAJÓN"], "Talón en el cajón",
             "La barra corre entre los parantes y apoya en la espalda alta. El cajón levanta los talones para que las puntas queden libres.",
             [C("STAND")], [ring(BEAM, 64, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                            ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                            ring(STEP, 54, 2.8), lab((60, 960), "CAJÓN", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A", "LA ESPALDA"], "Trapecios",
             "Ajustá la barra a la altura de los trapecios, con los topes altos para poder soltarla sin agacharte.",
             [C("STAND")], [ring(BAR, 60, 0.8), lab((60, 800), "BARRA A LA ESPALDA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["TALÓN EN", "EL CAJÓN"], "Puntas afuera",
             "Apoyá los talones en el cajón y dejá las puntas afuera, colgando en el aire.",
             [C("STAND")], [ring(HEEL, 46, 0.8), ring(TOE, 48, 1.8),
                            lab((60, 800), "TALÓN ARRIBA DEL CAJÓN", "start", 1.0),
                            lab((60, 880), "PUNTAS AFUERA", "start", 2.2)], 7.2),
        step("POSICIÓN INICIAL", ["DE PIE", "DERECHO"], "Torso alto",
             "Quedate derecho, con el abdomen firme y la mirada al frente. Los talones apoyan en el cajón y las rodillas quedan casi estiradas.",
             [C("STAND")], [ring(KNEE, 54, 0.8), lab((60, 800), "RODILLAS ESTIRADAS", "start", 1.0)], 7.2),
        step("PASO 1 / 3", ["SUBÍ LAS", "PUNTAS"], "Lo más alto",
             "Paso uno. Levantá las puntas de los pies lo más alto que puedas, como si quisieras llevarlas hacia la espinilla.",
             [C("STAND"), TO("UP", 0.4, 1.0)], [ring(TOE, 48, 0.8), lab((60, 800), "PUNTAS ARRIBA", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRETÁ", "ARRIBA"], "Pausa arriba",
             "Paso dos. Hacé una pausa de un segundo arriba, apretando la parte de adelante de la pierna sin mover las rodillas.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(SHIN, 50, 0.8), lab((60, 800), "TIBIAL ANTERIOR", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Hasta el piso",
             "Paso tres. Bajá las puntas despacio hasta que el pie quede plano, sin dejarlo caer.",
             [C("UP"), TO("STAND", 0.5, 1.2)], [ring(TOE, 48, 0.8), lab((60, 800), "CONTROLÁ LA BAJADA", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire abajo y soltalo mientras subís las puntas. No aguantes el aire ni pierdas el equilibrio.",
             [C("STAND"), seqloop("STAND", "UP", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIO", "RECORRIDO"], "Puntas completas",
             "Error: quedarte a mitad de camino. Subí las puntas hasta arriba y bajá hasta el pie plano en cada repetición.",
             [C("STAND"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(TOE, 48, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["DOBLAR", "LAS RODILLAS"], "Rodillas quietas",
             "Error: doblar las rodillas. La rodilla queda casi estirada: el movimiento sale del tobillo, no de la pierna.",
             [C("STAND"), TO("KNEES_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(KNEE, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["INCLINAR", "EL TORSO"], "Torso alto",
             "Error: inclinarte hacia adelante. El torso queda alto y la barra quieta sobre la espalda durante todo el recorrido.",
             [C("STAND"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(LUMB, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Puntas completas", "Rodillas quietas",
                                          "Torso alto", "Bajada lenta"],
             "Tips: subí las puntas completas, rodillas quietas, torso alto y bajada lenta.",
             [C("STAND"), seqloop("STAND", "UP", 1.2, 1.1, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Talón en el cajón", "Puntas afuera",
                                     "Pausa arriba", "Sin rebote"],
             "Claves: talón en el cajón, puntas afuera, pausa arriba y sin rebote.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 15–20"], "Tibial anterior",
             "Tres series de quince a veinte repeticiones, con un minuto de pausa. Es un músculo chico: priorizá el recorrido.",
             ["1 · SUBÍ", "2 · APRETÁ", "3 · BAJÁ"], [C("STAND"), seqloop("STAND", "UP", 1.0, 1.0, 0.3)]),
        step("AL TERMINAR", ["APOYÁ LOS", "PIES"], "Sin apuro",
             "Al terminar, apoyá los pies completos en el piso y dejá la barra en los topes antes de salir de la máquina.",
             [C("UP"), TO("STAND", 0.8, 1.4)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT91 = {
    "titulo": "Smith Reverse Calf Raises 🔥 Tibial anterior | Piernas",
    "tags": ["smith reverse calf raises", "gemelo invertido", "tibial anterior", "espinilla", "gemelos",
             "smith machine", "multipower", "tobillo", "pantorrillas", "gimnasio", "principiantes",
             "rutina de piernas"],
    "descripcion": yt_desc("Smith Reverse Calf Raises",
        "elevación de las puntas de los pies en la máquina Smith",
        "tibial anterior y estabilidad del tobillo",        "El gemelo invertido en la Smith trabaja el tibial anterior, la parte de adelante de la pierna. Los talones apoyan en un cajón y las puntas quedan afuera, colgando: desde ahí se levantan las puntas lo más alto posible, con la barra apoyada en la espalda alta. Es un músculo chico, así que se usan más repeticiones y poco peso. Sirve para equilibrar el trabajo del gemelo y estabilizar el tobillo. Los errores típicos son hacer medio recorrido, doblar las rodillas e inclinar el torso.",
        ["Ajustá la barra a la altura de los trapecios, con los topes altos.",
         "Apoyá los talones en el cajón y dejá las puntas afuera."],
        ["Quedate derecho, con el abdomen firme y las rodillas casi estiradas.",
         "Levantá las puntas de los pies lo más alto posible.",
         "Hacé una pausa de un segundo arriba.",
         "Bajá despacio hasta que el pie quede plano.",
         "Al terminar, apoyá los pies y dejá la barra en los topes."],
        ["Medio recorrido → puntas completas arriba y bajada entera.",
         "Doblar las rodillas → la rodilla queda casi estirada.",
         "Inclinar el torso → torso alto y barra quieta."],
        ["Talón en el cajón y puntas afuera.", "Rodillas casi estiradas.",
         "Pausa arriba, sin rebote.", "Bajada lenta hasta el pie plano."],
        "Piernas → Tibial anterior → Tobillo",
        "3 series de 15–20 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Piernas #TibialAnterior #SmithMachine #Gemelos #Tobillo #Entrenamiento #Fuerza")}

save("smith-reverse-calf-raises", calf_scenes("smith-reverse-calf-raises"),
     {"pose": "UP", "zoom": 1.02, "dy": 70}, YT91)
