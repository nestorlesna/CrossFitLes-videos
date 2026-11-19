# Dataset D68 Sled 45 Leg Wide Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def wide_scenes(slug):
    s, S, J = load(slug)
    PLATE = S(239, -564); RAIL = S(-72, -242); PLAT = S(57, -564)
    PAD = S(-450, -420); SEAT = S(-320, -268)
    ANKT = S(50, -559); ANKB = S(-46, -492); KNEEB = S(-272, -535)
    FAR_T = S(-34, -551); FAR_B = S(-130, -484)
    return [
        hook("GIMNASIO · PIERNAS", ["PIES BIEN", "SEPARADOS"], "Postura ancha",
             "Prensa a 45 grados con los pies bien abiertos: el carro corre por el riel y las piernas empujan desde una base ancha.",
             [C("TOP"), seqloop("TOP", "BOTTOM")]),
        step("LA MÁQUINA", ["CARRO Y", "RIEL 45°"], "Plataforma inclinada",
             "El carro con discos corre sobre un riel a 45 grados y la plataforma queda arriba, donde apoyás los pies.",
             [C("TOP")], [ring(PLATE, 92, 0.8), lab((1040, 800), "DISCOS", "end", 0.8),
                          ring(RAIL, 44, 1.7), lab((560, 1200), "RIEL 45°", "start", 1.7),
                          ring(PLAT, 52, 2.6), lab((1040, 890), "PLATAFORMA", "end", 2.6)], 7.2),
        step("AJUSTE 1 / 2", ["ESPALDA", "Y CADERA"], "Bien apoyado",
             "Apoyá la espalda en el respaldo y la cadera en el asiento, con la cabeza y los hombros relajados.",
             [C("TOP")], [ring(PAD, 60, 0.8), lab((60, 1010), "RESPALDO", "start", 0.8),
                          ring(SEAT, 56, 1.8), lab((60, 1470), "CADERA APOYADA", "start", 1.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES A LOS", "BORDES"], "Base ancha",
             "Abrí los pies hacia los bordes de la plataforma, con las puntas un poco hacia afuera y las rodillas alineadas.",
             [C("TOP")], [ring(ANKT, 56, 0.8), ring(FAR_T, 56, 0.8), lab((1040, 900), "PIES ANCHOS", "end", 1.0)], 7.6),
        step("POSICIÓN INICIAL", ["PIERNAS", "CASI ESTIRADAS"], "Sin trabar",
             "Arrancá con las piernas casi estiradas, las rodillas blandas y los pies bien apoyados en la plataforma.",
             [C("TOP")], [ring(ANKT, 48, 0.8), lab((60, 900), "SIN TRABAR", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "CONTROLANDO"], "Rodillas afuera",
             "Paso uno. Bajá el carro llevando las rodillas hacia afuera, en línea con las puntas de los pies.",
             [C("TOP"), TO("BOTTOM", 0.6, 1.2)],
             [arrow((739, 894), (647, 985), 0.8, 1.2, [40, 0]),
              lab((60, 900), "BAJÁ LENTO", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["FONDO", "DEL RECORRIDO"], "Cadera apoyada",
             "Paso dos. Llegá hasta donde llegues con la cadera apoyada en el asiento y la espalda pegada al respaldo.",
             [C("BOTTOM"), TO("BOTTOM", 0.2, 0.4)],
             [ring(KNEEB, 52, 0.8), lab((60, 900), "SIN DESPEGAR", "start", 1.0)], 7.0),
        step("PASO 3 / 3", ["EMPUJÁ", "PAREJO"], "Toda la planta",
             "Paso tres. Empujá con toda la planta de los dos pies, estirando las rodillas sin trabarlas de golpe.",
             [C("BOTTOM"), TO("TOP", 0.5, 1.2)],
             [arrow((647, 985), (739, 894), 0.8, 1.2, [40, 0]),
              lab((60, 900), "SUBÍ PAREJO", "start", 1.1)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al bajar",
             "Tomá aire al bajar el carro y soltalo al empujar. El abdomen queda firme y la cadera apoyada.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 0.9, 1.7, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta donde llegues con la cadera apoyada y sin rebotar.",
             [C("TOP"), TO("SHALLOW_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(S(10, -532), 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TALÓN", "DESPEGADO"], "Planta completa",
             "Error: empujar con la punta y despegar los talones. Toda la planta queda apoyada y empuja parejo.",
             [C("TOP"), TO("HEELS_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(ANKB, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["JUNTAR", "LOS PIES"], "Base ancha",
             "Error: juntar los pies para empujar más fácil. Los pies quedan abiertos hacia los bordes de la plataforma.",
             [C("TOP"), TO("NARROW_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(S(-56, -488), 56, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Pies a los bordes", "Rodillas afuera",
                                         "Talones abajo", "Bajá controlando"],
             "Tips: pies a los bordes, rodillas hacia afuera, talones abajo y bajada controlada.",
             [C("TOP"), seqloop("TOP", "BOTTOM")]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda en el respaldo", "Empujá con la planta",
                                     "Sin trabar las rodillas", "Puntas hacia afuera"],
             "Claves: espalda en el respaldo, empujá con la planta, sin trabar las rodillas y puntas hacia afuera.",
             [{"cut": "BOTTOM", "at": 0.1}]),
        reps(["3 X 10–12"], "Cuádriceps",
             "Tres series de diez a doce repeticiones, con dos minutos de pausa. Elegí un peso que te deje llegar al fondo sin despegar la cadera.",
             ["1 · BAJÁ", "2 · FONDO", "3 · SUBÍ"], [C("TOP"), seqloop("TOP", "BOTTOM")]),
        step("AL TERMINAR", ["SALÍ", "DESPACIO"], "Sin apurarse",
             "Al terminar la serie, subí el carro, trabá el seguro y salí de la máquina sin encorvarte.",
             [C("BOTTOM"), TO("TOP", 0.9, 2.0)],
             [lab((60, 900), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT68 = {
    "titulo": "Sled 45 Leg Wide Press 🔥 Prensa 45 con pies bien separados | Gimnasio",
    "tags": ["sled 45 leg wide press", "prensa pies separados", "prensa 45 grados",
             "prensa ancha", "cuádriceps", "glúteos", "aductores", "piernas",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Sled 45 Leg Wide Press",
        "prensa a 45 grados con los pies abiertos hacia los bordes de la plataforma",
        "cuádriceps, glúteos y aductores",
        "Con los pies bien separados en la plataforma de la prensa a 45 grados, el recorrido involucra más glúteo y aductor, y las rodillas tienen más lugar para viajar hacia afuera. Es una postura cómoda para empujar fuerte sin que la cadera se despegue. Si cortás el recorrido, despegás los talones o juntás los pies, el trabajo cambia y se pierde la base ancha.",
        ["Apoyá la espalda en el respaldo y la cadera en el asiento.",
         "Abrí los pies hacia los bordes de la plataforma con las puntas afuera."],
        ["Arrancá con las piernas casi estiradas y las rodillas blandas.",
         "Bajá el carro llevando las rodillas hacia afuera.",
         "Llegá al fondo con la cadera apoyada y sin rebotar.",
         "Empujá con toda la planta hasta estirar las piernas.",
         "Subí el carro, trabá el seguro y salí despacio."],
        ["Media repetición → bajá hasta donde llegues con la cadera apoyada.",
         "Talones despegados → planta completa y empuje parejo.",
         "Juntar los pies → pies abiertos hacia los bordes."],
        ["Pies a los bordes de la plataforma.", "Rodillas hacia afuera, con las puntas.",
         "Talones abajo durante todo el recorrido.", "Bajada controlada, sin rebotar."],
        "Piernas → Cuádriceps → Glúteos",
        "3 series de 10–12 repeticiones, con 2 minutos de pausa. Nivel: principiante.",
        "#Gimnasio #Cuadriceps #Prensa45 #Gluteos #Piernas #Aductores #Entrenamiento #Fuerza")}

save("sled-45-leg-wide-press", wide_scenes("sled-45-leg-wide-press"),
     {"pose": "BOTTOM", "zoom": 1.06, "dy": 40}, YT68)
