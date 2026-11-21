# Dataset D105 Smith Close Grip Bench Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def press_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(-235, -1030); PAR = S(-105, -700); STOP = S(-105, -300)
    BENCH = S(-200, -180); W_TOP = S(*J["TOP"]["W"]); W_BOT = S(*J["BOTTOM"]["W"])
    W_MID = S(*J["MID"]["W"]); HEAD = S(*J["TOP"]["N"]); ELB = S(*J["BOTTOM"]["E"])
    HIP = S(*J["BUTT_BAD"]["H"])
    return [
        hook("GIMNASIO · BRAZOS", ["PRESS", "CERRADO"], "Manos al centro",
             "Smith Close Grip Bench Press: press de banca con agarre cerrado y la barra guiada del Smith.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 1.2, 1.4, 0.4)]),
        step("LA MÁQUINA", ["BARRA Y", "BANCO"], "Banco plano",
             "La barra corre entre los parantes y el banco se ubica debajo, a la altura del pecho bajo. Los topes te dejan una salida segura.",
             [C("TOP")], [ring(BEAM, 64, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                          ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                          ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BANCO BAJO", "LA BARRA"], "Pecho bajo",
             "Corré el banco hasta que la barra baje al pecho bajo, no al cuello. Los pies quedan firmes en el piso.",
             [C("TOP")], [ring(BENCH, 60, 0.8), lab((60, 800), "BANCO A LA ALTURA", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["AGARRE", "CERRADO"], "Manos al centro",
             "Agarrá la barra con las manos al centro, a un palmo de distancia entre sí, y las muñecas rectas.",
             [C("TOP")], [ring(W_TOP, 58, 0.8), lab((60, 800), "MANOS AL CENTRO", "start", 0.8)], 7.2),
        step("POSICIÓN INICIAL", ["ACOSTADO", "FIRME"], "Ojos bajo la barra",
             "Apoyá los glúteos y la espalda alta en el banco, los ojos debajo de la barra y los pies firmes en el piso.",
             [C("TOP")], [ring(HEAD, 54, 0.8), lab((60, 800), "OJOS BAJO LA BARRA", "start", 1.0)], 7.2),
        step("PASO 1 / 3", ["BAJÁ AL", "PECHO BAJO"], "Codos pegados",
             "Paso uno. Bajá la barra al pecho bajo con los codos pegados al torso y las muñecas rectas.",
             [C("TOP"), TO("BOTTOM", 0.4, 1.2)], [ring(W_BOT, 54, 0.8), lab((60, 800), "AL PECHO BAJO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["TOCÁ", "SUAVE"], "Sin rebote",
             "Paso dos. Tocá el pecho sin rebotar y hacé una pausa corta. Los codos siguen pegados al torso.",
             [C("BOTTOM"), TO("BOTTOM", 0.2, 0.5)], [ring(ELB, 52, 0.8), lab((60, 800), "CODO PEGADO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["EMPUJÁ", "ARRIBA"], "Hasta estirar",
             "Paso tres. Empujá la barra hasta estirar los brazos, sin trabar los codos ni mover los pies del piso.",
             [C("BOTTOM"), TO("TOP", 0.4, 1.1)], [ring(W_TOP, 56, 0.8), lab((60, 800), "BRAZOS ESTIRADOS", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire arriba, aguantalo en la bajada y soltalo al empujar. No aguantes el aire en todo el recorrido.",
             [C("TOP"), seqloop("TOP", "MID", 1.2, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["AL CUELLO", "O A LA CARA"], "Pecho bajo",
             "Error: bajar la barra al cuello o a la cara. La barra baja al pecho bajo, con el agarre cerrado bien firme.",
             [C("TOP"), TO("NECK_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(S(*J["NECK_BAD"]["W"]), 52, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["DESPEGAR", "LA COLA"], "Glúteos abajo",
             "Error: despegar los glúteos del banco. La cola y la espalda alta quedan apoyadas, y el pecho es el que trabaja.",
             [C("TOP"), TO("BUTT_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["MEDIO", "RECORRIDO"], "Tocá y estirá",
             "Error: cortar el recorrido. La barra toca el pecho bajo en cada repetición y sube hasta estirar los brazos.",
             [C("TOP"), TO("SHORT_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(S(*J["SHORT_BAD"]["W"]), 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Manos al centro", "Codos pegados", "Muñecas firmes", "Sin rebote"],
             "Tips: manos al centro, codos pegados, muñecas firmes y sin rebote.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Agarre cerrado", "Codos al torso", "Tocá suave", "Empujá parejo"],
             "Claves: agarre cerrado, codos al torso, tocá suave y empujá parejo.",
             [{"cut": "BOTTOM", "at": 0.1}]),
        reps(["3 X 8–12"], "Tríceps y pecho",
             "Tres series de ocho a doce repeticiones, con un minuto y medio de pausa. El agarre cerrado pide menos peso.",
             ["1 · BAJÁ", "2 · TOCÁ", "3 · EMPUJÁ"], [C("TOP"), seqloop("TOP", "BOTTOM", 1.2, 1.2, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN LOS TOPES"], "Salí de costado",
             "Al terminar, dejá la barra en los topes, sacá las manos y salí del banco de costado, sin apurarte.",
             [C("BOTTOM"), TO("MID", 0.8, 1.4)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT105 = {
    "titulo": "Smith Close Grip Press 🔥 Press agarre cerrado | Tríceps",
    "tags": ["smith close grip press", "press agarre cerrado", "press de banca cerrado", "press de banca",
             "smith machine", "multipower", "tríceps", "pectorales", "pecho bajo", "gimnasio", "principiantes",
             "rutina de tríceps"],
    "descripcion": yt_desc("Smith Close Grip Bench Press",
        "press de banca con agarre cerrado en la máquina Smith",
        "tríceps, pectorales y deltoides anterior",
        "El press con agarre cerrado en la Smith se hace acostado en un banco plano, con las manos juntas sobre el esternón y la barra guiada bajando al pecho bajo. Los codos se quedan pegados al torso, el recorrido es corto y controlado, y el tríceps hace más fuerza que en un press normal. Por eso el peso baja bastante. Los errores típicos son abrir los codos, despegar los glúteos y cortar el recorrido.",
        ["Ubicá el banco para que la barra baje al pecho bajo y dejá los topes altos.",
         "Acostate con los ojos debajo de la barra y los pies firmes en el piso."],
        ["Agarrá la barra con las manos al centro, a un palmo de distancia entre sí.",
         "Bajá la barra al pecho bajo con los codos pegados al torso.",
         "Tocá el pecho sin rebotar y hacé una pausa corta.",
         "Empujá hasta estirar los brazos sin trabar los codos.",
         "Al terminar, dejá la barra en los topes y salí de costado."],
        ["Abrir los codos → codos pegados al torso todo el recorrido.",
         "Despegar los glúteos → cola y espalda alta apoyadas.",
         "Cortar el recorrido → tocá el pecho y estirá los brazos."],
        ["Manos al centro y muñecas rectas.", "Codos pegados al torso.",
         "La barra toca el pecho bajo.", "Empuje parejo, sin rebote."],
        "Brazos → Tríceps → Pectorales → Deltoides anterior",
        "3 series de 8–12 repeticiones, con 1 minuto y medio de pausa. Nivel: intermedio.",
        "#Gimnasio #Brazos #PressAgarreCerrado #SmithMachine #Triceps #Pectorales #Entrenamiento #Fuerza")}

save("smith-close-grip-bench-press", press_scenes("smith-close-grip-bench-press"),
     {"pose": "TOP", "grip": 1, "zoom": 1.0, "dy": 40}, YT105)
