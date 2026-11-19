# Dataset D79 Smith Deadlift: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def dead_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(70, -884); PAR = S(370, -640); STOP = S(370, -560)
    BAR_L = S(70, -110); BAR_M = S(70, -250); BAR_T = S(70, -412)
    HIP_L = S(-110, -250); HIP_T = S(0, -455); BACK_L = S(0, -336)
    KNEE = S(128, -220); FOOT = S(60, 0); FOOT2 = S(-20, 0)
    BACK_R = S(64, -368); HIP_U = S(30, -420); LUMB_T = S(-10, -480)
    return [
        hook("GIMNASIO · PIERNAS", ["PESO MUERTO", "EN LA SMITH"], "Cadena posterior",
             "Peso muerto en la Smith: la barra sale del piso pegada a las tibias y subís con la espalda recta.",
             [C("START"), seqloop("START", "TOP", 1.3, 1.4, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada en una sola vertical pegada a las tibias, y los topes te dejan la salida segura.",
             [C("START")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                            ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                            ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA AL", "PISO"], "Tibias pegadas",
             "Bajá la barra hasta el piso sobre los topes y dejá que las tibias queden tocando la barra.",
             [C("START")], [ring(BAR_L, 62, 0.8), lab((60, 800), "BARRA AL PISO", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES AL", "ANCHO"], "Barra al medio pie",
             "Parate con los pies al ancho de la cadera y la barra justo sobre el medio pie, pegada a las tibias.",
             [C("START")], [ring(FOOT, 50, 0.8), ring(FOOT2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["AGARRE", "FIRME"], "Pecho arriba",
             "Agarrá la barra, bajá la cadera y subí el pecho: espalda recta, hombros justo sobre la barra.",
             [C("START")], [ring(BACK_L, 62, 0.8), lab((60, 800), "ESPALDA RECTA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["EMPUJÁ", "EL PISO"], "Con las piernas",
             "Paso uno. Empujá el piso con los pies y subí la barra pegada a las tibias, sin tirar con la espalda.",
             [C("START"), TO("MID", 0.4, 1.1)], [ring(FOOT, 54, 0.8), lab((60, 800), "EMPUJÁ EL PISO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["EXTENDÉ", "LA CADERA"], "Glúteo y isquios",
             "Paso dos. Extendé la cadera y apretá el glúteo hasta quedar derecho, con la barra pegada al cuerpo.",
             [C("MID"), TO("TOP", 0.4, 1.1)], [ring(HIP_T, 58, 0.8), lab((60, 800), "EXTENDÉ LA CADERA", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ", "CONTROLANDO"], "Mismo camino",
             "Paso tres. Bajá la barra por el mismo camino, con la cadera atrás y la espalda recta hasta el piso.",
             [C("TOP"), TO("START", 0.4, 1.3)], [ring(BAR_M, 60, 0.8), lab((60, 800), "BARRA PEGADA", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Tomá aire abajo",
             "Tomá aire arriba, aguantá mientras bajás y soltalo al terminar de subir. No sueltes la espalda.",
             [C("START"), seqloop("START", "TOP", 1.3, 1.4, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["REDONDEAR", "LA ESPALDA"], "Pecho arriba",
             "Error: redondear la espalda. El pecho va arriba y la espalda recta de la cadera a la nuca.",
             [C("START"), TO("ROUND_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BACK_R, 58, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["LEVANTAR", "LA COLA"], "Todo junto",
             "Error: levantar la cola primero. La cadera y los hombros suben juntos, no arranca la espalda.",
             [C("START"), TO("HIPUP_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP_U, 56, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["ARQUEAR", "ARRIBA"], "Cuerpo derecho",
             "Error: arquear la espalda al final. Terminá derecho, con el abdomen firme y el glúteo apretado.",
             [C("TOP"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(LUMB_T, 56, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra pegada", "Pecho arriba",
                                          "Empujá el piso", "Glúteo apretado"],
             "Tips: barra pegada a las tibias, pecho arriba, empujá el piso y terminá apretando el glúteo.",
             [C("START"), seqloop("START", "TOP", 1.3, 1.4, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda recta", "Hombros sobre la barra",
                                    "Cadera y hombros juntos", "Bajada controlada"],
             "Claves: espalda recta, hombros sobre la barra, cadera y hombros juntos y bajada controlada.",
             [{"cut": "TOP", "at": 0.1}]),
        reps(["3 X 6–8"], "Isquios y glúteo",
             "Tres series de seis a ocho repeticiones, con dos minutos de pausa. Peso moderado y técnica primero.",
             ["1 · EMPUJÁ", "2 · EXTENDÉ", "3 · BAJÁ"], [C("START"), seqloop("START", "TOP", 1.4, 1.5, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN EL PISO"], "Sin apuro",
             "Al terminar la serie, bajá la barra al piso por el mismo camino y soltala, sin redondear la espalda.",
             [C("TOP"), TO("START", 0.9, 2.0)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT79 = {
    "titulo": "Smith Deadlift 🔥 Peso muerto en la Smith | Cadena posterior",
    "tags": ["smith deadlift", "peso muerto", "peso muerto en smith", "smith machine", "multipower",
             "isquios", "glúteo", "espalda baja", "cadena posterior", "gimnasio", "principiantes",
             "rutina de piernas"],
    "descripcion": yt_desc("Smith Deadlift",
        "peso muerto con barra guiada en la máquina Smith",
        "isquiotibiales, glúteo y espalda baja",
        "El peso muerto en la Smith quita la variante del equilibrio: la barra corre guiada en una sola vertical, pegada a las tibias, y vos te concentrás en la bisagra de cadera. La barra arranca del piso, subís empujando con las piernas y extendiendo la cadera hasta quedar derecho, y bajás controlando el mismo camino con la espalda recta. Si redondeás la espalda, levantás la cola primero o arqueás al final, la zona lumbar se lleva la carga.",
        ["Apoyá la barra en el piso y parate con la barra sobre el medio pie.",
         "Agarrá la barra, bajá la cadera y subí el pecho."],
        ["Empujá el piso con los pies y subí la barra pegada a las tibias.",
         "Extendé la cadera y apretá el glúteo hasta quedar derecho.",
         "Mantené la espalda recta y los hombros sobre la barra.",
         "Bajá la barra por el mismo camino, con la cadera atrás.",
         "Dejá la barra en el piso al terminar la serie."],
        ["Redondear la espalda → pecho arriba y espalda recta.",
         "Levantar la cola primero → cadera y hombros suben juntos.",
         "Arquear al final → terminá derecho y con el abdomen firme."],
        ["Barra pegada a las tibias.", "Pecho arriba, mirada al frente.",
         "Empujá el piso, no tires con la espalda.", "Bajada controlada."],
        "Piernas → Isquios → Glúteo",
        "3 series de 6–8 repeticiones, con 2 minutos de pausa. Nivel: intermedio.",
        "#Gimnasio #PesoMuerto #SmithMachine #Gluteo #Isquios #EspaldaBaja #Entrenamiento #Fuerza")}

save("smith-deadlift", dead_scenes("smith-deadlift"),
     {"pose": "START", "zoom": 1.02, "dy": 30}, YT79)
