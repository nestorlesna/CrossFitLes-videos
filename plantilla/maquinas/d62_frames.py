# Dataset D86 Smith Machine Bicep Curl: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def curl_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(-75, -860); PAR = S(-375, -500); STOP = S(-375, -330)
    BAR_D = S(-75, -424); BAR_U = S(-75, -640)
    SHO = S(49, -739); WRIST_D = S(-45, -424); WRIST_H = S(-95, -540)
    ELBOW_BAD = S(*J["ELBOW_BAD"]["E"]); SHO_SWING = S(133, -714)
    return [
        hook("GIMNASIO \u00b7 BRAZOS", ["CURL EN", "LA SMITH"], "Aisl\u00e1 el b\u00edceps",
             "Smith Machine Bicep Curl: el curl de b\u00edceps en la barra guiada de la Smith, para aislar el b\u00edceps sin balanceo.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.4)]),
        step("LA M\u00c1QUINA", ["BARRA", "GUIADA"], "Barra fija en el carril",
             "La Smith te gu\u00eda la barra en l\u00ednea recta entre los parantes: no pele\u00e1s con el equilibrio, solo con la subida.",
             [C("DOWN")], [ring(BEAM, 62, 0.8), lab((60, 748), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 52, 1.8), lab((60, 840), "PARANTES", "start", 1.8),
                           ring(STOP, 46, 2.8), lab((60, 932), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A", "LA CADERA"], "Altura justa",
             "Ajust\u00e1 la barra a la altura de la cadera: con los brazos estirados las manos llegan c\u00f3modas y sin encogerte.",
             [C("DOWN")], [ring(BAR_D, 58, 0.8), lab((60, 800), "BARRA A LA CADERA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["AGARRE", "SUPINO"], "Manos al ancho",
             "Agarr\u00e1 la barra con las palmas hacia arriba, un poco m\u00e1s abiertas que los hombros, y eleg\u00ed un peso que puedas controlar.",
             [C("DOWN")], [ring(WRIST_D, 44, 0.8), lab((60, 800), "AGARRE SUPINO", "start", 0.8)], 7.4),
        step("POSICI\u00d3N INICIAL", ["CODO", "PEGADO"], "Codos al costado",
             "De pie, pies al ancho de los hombros, codos pegados al torso y abdomen firme. La espalda no se mueve.",
             [C("DOWN")], [ring(SHO, 44, 0.8), lab((60, 800), "CODO PEGADO", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUB\u00cd", "AL PECHO"], "Sin mover el codo",
             "Paso uno. Sub\u00ed la barra hacia el pecho contrayendo el b\u00edceps, sin mover los codos ni el torso.",
             [C("DOWN"), TO("UP", 0.4, 0.9)], [ring(BAR_U, 52, 0.8), lab((60, 800), "BARRA AL PECHO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["APRET\u00c1", "ARRIBA"], "Pausa corta",
             "Paso dos. Arriba hac\u00e9 una pausa breve y apret\u00e1 el b\u00edceps: no hace falta subir m\u00e1s all\u00e1 del pecho.",
             [C("UP"), TO("UP", 0.2, 0.4)], [ring(BAR_U, 52, 0.8), lab((1020, 800), "APRET\u00c1 ARRIBA", "end", 1.0)], 7.0),
        step("PASO 3 / 3", ["BAJ\u00c1", "CONTROLADO"], "Dos segundos",
             "Paso tres. Baj\u00e1 la barra en dos segundos hasta estirar el brazo, sin soltar la tensi\u00f3n ni rebotar.",
             [C("UP"), TO("DOWN", 0.5, 1.2)], [ring(WRIST_D, 44, 0.8), lab((60, 800), "BAJADA LENTA", "start", 1.0)], 7.4),
        step("RESPIRACI\u00d3N", ["RESPIR\u00c1"], "Solt\u00e1 al subir",
             "Tom\u00e1 aire abajo y soltalo mientras sub\u00eds. No aguantes el aire arriba ni te quedes sin aire en la serie.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.1, 1.1, 0.3)], mn=6.0),
        step("AS\u00cd NO \u00b7 1 / 3", ["MEDIA", "REPETICI\u00d3N"], "Recorrido completo",
             "Error: quedarte a mitad de camino. Baj\u00e1 hasta estirar el brazo y sub\u00ed hasta el pecho en cada repetici\u00f3n.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(WRIST_H, 44, 1.4)], 7.4),
        step("AS\u00cd NO \u00b7 2 / 3", ["BALANCEO", "DEL TORSO"], "Torso quieto",
             "Error: balancear el torso para subir. La espalda queda quieta y el codo sigue pegado al costado.",
             [C("DOWN"), TO("SWING_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(SHO_SWING, 48, 1.4)], 7.4),
        step("AS\u00cd NO \u00b7 3 / 3", ["CODO", "ADELANTE"], "Codo en su lugar",
             "Error: llevar los codos adelante o atr\u00e1s. Quedan pegados al torso y la barra sube en l\u00ednea recta.",
             [C("DOWN"), TO("ELBOW_BAD", 0.5, 0.8)],
             [NO(1.4, (940, 660)), ring(ELBOW_BAD, 46, 1.4)], 7.4),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra a la cadera", "Codo pegado",
                                          "Sin balanceo", "Bajada de dos segundos"],
             "Tips: barra a la altura de la cadera, codo pegado, sin balanceo y bajada de dos segundos.",
             [C("DOWN"), seqloop("DOWN", "UP", 1.0, 1.1, 0.3)]),
        keys("CLAVES", ["T\u00c9CNICA"], ["Agarre supino", "Codos fijos",
                                        "Mu\u00f1eca firme", "Recorrido completo"],
             "Claves: agarre supino, codos fijos, mu\u00f1eca firme y recorrido completo.",
             [{"cut": "UP", "at": 0.1}]),
        reps(["3 X 10\u201312"], "B\u00edceps",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Sub\u00ed el peso cuando las doce salgan f\u00e1ciles.",
             ["1 \u00b7 SUB\u00cd", "2 \u00b7 APRET\u00c1", "3 \u00b7 BAJ\u00c1"],
             [C("DOWN"), seqloop("DOWN", "UP", 1.0, 1.1, 0.3)]),
        step("AL TERMINAR", ["SOLT\u00c1", "LA BARRA"], "Sin apuro",
             "Al terminar, dej\u00e1 la barra en el soporte de la Smith y sal\u00ed de la m\u00e1quina sin apurarte.",
             [C("DOWN")], [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT86 = {
    "titulo": "Smith Machine Bicep Curl \U0001f525 Curl de b\u00edceps en la Smith | Gimnasio",
    "tags": ["smith machine bicep curl", "curl de b\u00edceps en smith", "curl b\u00edceps", "smith machine",
             "multipower", "b\u00edceps", "antebrazo", "brazos", "gimnasio", "principiantes",
             "rutina de brazos", "aislar b\u00edceps"],
    "descripcion": yt_desc("Smith Machine Bicep Curl",
        "curl de b\u00edceps con la barra guiada de la m\u00e1quina Smith",
        "b\u00edceps y antebrazo",
        "La Smith gu\u00eda la barra en l\u00ednea recta, as\u00ed que el curl de b\u00edceps se puede hacer de pie con un recorrido parejo y sin pelear con el equilibrio. La barra arranca a la altura de la cadera y sube hasta el pecho, con los codos pegados al torso y la espalda quieta. Es un ejercicio ideal para aislar el b\u00edceps y sentir la contracci\u00f3n, sobre todo si te cuesta no balancear el cuerpo con mancuernas. Los errores t\u00edpicos son cortar el recorrido, balancear el torso para subir y despegar los codos del costado.",
        ["Ajust\u00e1 la barra a la altura de la cadera.",
         "Agarr\u00e1 con las palmas hacia arriba, un poco m\u00e1s abiertas que los hombros."],
        ["De pie, pies al ancho de los hombros y codos pegados al torso.",
         "Sub\u00ed la barra hacia el pecho contrayendo el b\u00edceps.",
         "Hac\u00e9 una pausa breve arriba, sin subir m\u00e1s all\u00e1 del pecho.",
         "Baj\u00e1 en dos segundos hasta estirar el brazo.",
         "Dej\u00e1 la barra en el soporte al terminar la serie."],
        ["Media repetici\u00f3n \u2192 baj\u00e1 hasta estirar y sub\u00ed hasta el pecho.",
         "Balancear el torso \u2192 espalda quieta y codo pegado.",
         "Codos adelante o atr\u00e1s \u2192 quedan fijos al costado."],
        ["Barra a la altura de la cadera.", "Codo pegado al torso.",
         "Sin balanceo: el peso lo mueve el b\u00edceps.", "Bajada lenta de dos segundos."],
        "B\u00edceps \u2192 Antebrazo",
        "3 series de 10\u201312 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Biceps #Curl #SmithMachine #Multipower #Brazos #Entrenamiento #Fuerza")}

save("smith-machine-bicep-curl", curl_scenes("smith-machine-bicep-curl"),
     {"pose": "UP", "zoom": 1.0, "dy": 20}, YT86)
