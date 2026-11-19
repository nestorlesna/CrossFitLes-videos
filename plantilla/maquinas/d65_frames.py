# Dataset D89 Smith One Leg Floor Calf Raise: escenas + YouTube + miniatura.
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
    BEAM = S(210, -900); PAR = S(370, -620); BAR = S(70, -726); BAR_UP = S(70, -770)
    FOOT = S(60, 0); KNEE = S(71, -230); KNEE_B = S(137, -217)
    BACK = S(45, -690); LUMB = S(35, -560); FREE = S(130, -280)
    return [
        hook("GIMNASIO · PIERNAS", ["GEMELO A", "UNA PIERNA"], "Desde el piso",
             "Smith One Leg Floor Calf Raise: elevación de talón a una pierna con la barra en la espalda.",
             [C("STAND"), seqloop("STAND", "UP", 1.3, 1.2, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Barra en la espalda",
             "La barra corre entre los parantes y apoya en la espalda alta. Los topes altos te dejan una salida si te falta fuerza.",
             [C("STAND")], [ring(BEAM, 64, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                            ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                            ring(S(370, -500), 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A", "LA ESPALDA"], "Trapecios",
             "Ajustá la barra a la altura de los trapecios, con los topes altos para poder soltarla sin agacharte.",
             [C("STAND")], [ring(BAR, 60, 0.8), lab((60, 800), "BARRA A LA ESPALDA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["UNA PIERNA", "EN EL PISO"], "Pie de apoyo",
             "Apoyá todo el pie de la pierna que trabaja y flexioná la otra detrás, con la punta del pie apuntando al piso.",
             [C("STAND")], [ring(FOOT, 50, 0.8), ring(FREE, 46, 1.8),
                            lab((60, 800), "PIE DE APOYO", "start", 1.0),
                            lab((60, 880), "PIERNA LIBRE", "start", 2.2)], 7.2),
        step("POSICIÓN INICIAL", ["DE PIE", "DERECHO"], "Torso alto",
             "Quedate derecho, con el abdomen firme y la mirada al frente. La rodilla de apoyo arranca casi estirada.",
             [C("STAND")], [ring(KNEE, 54, 0.8), lab((60, 800), "RODILLA ESTIRADA", "start", 1.0)], 7.2),
        step("PASO 1 / 3", ["SUBÍ EL", "TALÓN"], "Lo más alto",
             "Paso uno. Empujá con la punta del pie y subí el talón lo más alto posible, sin doblar la rodilla de apoyo.",
             [C("STAND"), TO("UP", 0.4, 1.0)], [ring(FOOT, 50, 0.8), lab((60, 800), "TALÓN ARRIBA", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRETÁ", "ARRIBA"], "Pausa arriba",
             "Paso dos. Arriba hacé una pausa de un segundo y apretá el gemelo sin perder el equilibrio.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(S(60, -44), 46, 0.8), lab((60, 800), "APRETÁ ARRIBA", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "LENTO"], "Hasta el estiramiento",
             "Paso tres. Bajá el talón despacio hasta el piso y seguí un poco más para estirar el gemelo, sin rebotar.",
             [C("UP"), TO("STAND", 0.5, 1.2)], [ring(FOOT, 50, 0.8), lab((60, 800), "BAJADA LENTA", "start", 1.0)], 7.4),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire abajo y soltalo mientras subís el talón. No aguantes el aire ni pierdas el equilibrio.",
             [C("STAND"), seqloop("STAND", "UP", 1.2, 1.1, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIO", "RECORRIDO"], "Talón completo",
             "Error: quedarte a mitad de camino. Subí el talón hasta arriba y bajá hasta el estiramiento en cada repetición.",
             [C("STAND"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(FOOT, 48, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["DOBLAR LA", "RODILLA"], "Rodilla estirada",
             "Error: doblar la rodilla de apoyo. La rodilla queda casi estirada: el movimiento sale del tobillo, no de la pierna.",
             [C("STAND"), TO("KNEES_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(KNEE_B, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["INCLINAR", "EL TORSO"], "Torso alto",
             "Error: inclinarte hacia adelante. El torso queda alto y la barra quieta sobre la espalda durante todo el recorrido.",
             [C("STAND"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(LUMB, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Talón completo", "Rodilla estirada",
                                          "Torso alto", "Bajada lenta"],
             "Tips: subí el talón completo, rodilla estirada, torso alto y bajada lenta.",
             [C("STAND"), seqloop("STAND", "UP", 1.2, 1.1, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Punta del pie", "Pausa arriba",
                                    "Sin rebote", "Estiramiento abajo"],
             "Claves: empujá con la punta del pie, pausa arriba, sin rebote y estirá abajo.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 12–15"], "Gemelos y sóleo",
             "Tres series de doce a quince repeticiones por pierna, con un minuto de pausa. Cambiá de pierna al terminar.",
             ["1 · SUBÍ", "2 · APRETÁ", "3 · BAJÁ"], [C("STAND"), seqloop("STAND", "UP", 1.1, 1.0, 0.3)]),
        step("AL TERMINAR", ["SOLTÁ LA BARRA", "CON CUIDADO"], "Sin apuro",
             "Al terminar, apoyá los dos pies y dejá la barra en los topes antes de salir de la máquina, sin apurarte.",
             [C("UP"), TO("STAND", 0.8, 1.4)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT89 = {
    "titulo": "Smith One Leg Floor Calf Raise 🔥 Gemelo a una pierna | Piernas",
    "tags": ["smith one leg floor calf raise", "gemelo a una pierna", "elevación de talón", "gemelos",
             "sóleo", "smith machine", "multipower", "pantorrillas", "gimnasio", "principiantes",
             "rutina de piernas", "calf raise"],
    "descripcion": yt_desc("Smith One Leg Floor Calf Raise",
        "elevación de talón a una pierna en la máquina Smith, desde el piso",
        "gemelos y sóleo",
        "El gemelo a una pierna en la Smith se hace desde el piso, con la barra apoyada en la espalda alta y la otra pierna flexionada detrás. Al trabajar con una sola pierna, cada gemelo recibe toda la carga y el recorrido es más exigente. Se sube el talón lo más alto posible, se sostiene arriba y se baja lento hasta el estiramiento. La rodilla de apoyo queda casi estirada: el movimiento sale del tobillo. Los errores típicos son hacer medio recorrido, doblar la rodilla y inclinar el torso.",
        ["Ajustá la barra a la altura de los trapecios, con los topes altos.",
         "Apoyá un pie completo y flexioná la otra pierna detrás."],
        ["Quedate derecho, con el abdomen firme y la rodilla de apoyo casi estirada.",
         "Empujá con la punta del pie y subí el talón lo más alto posible.",
         "Hacé una pausa de un segundo arriba, apretando el gemelo.",
         "Bajá el talón despacio hasta el piso y estirá.",
         "Cambiá de pierna al terminar la serie."],
        ["Medio recorrido → subí hasta arriba y bajá hasta el estiramiento.",
         "Doblar la rodilla → la rodilla queda casi estirada.",
         "Inclinar el torso → torso alto y barra quieta."],
        ["Talón completo, sin rebote.", "Rodilla de apoyo estirada.",
         "Torso alto y mirada al frente.", "Bajada lenta hasta estirar."],
        "Piernas → Gemelos → Sóleo",
        "3 series de 12–15 repeticiones por pierna, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Piernas #Gemelos #CalfRaise #SmithMachine #Pantorrillas #Entrenamiento #Fuerza")}

save("smith-one-leg-floor-calf-raise", calf_scenes("smith-one-leg-floor-calf-raise"),
     {"pose": "UP", "zoom": 1.08, "dy": 60}, YT89)
