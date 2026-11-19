# Dataset D66 Sled 45 Degrees One Leg Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def lp1_scenes(slug):
    s, S, J = load(slug)
    PLATE = S(239, -564); RAIL = S(-72, -242); PLAT = S(57, -564)
    HIP = S(-320, -300); SHO = S(-518, -498); PAD = S(-450, -420); SEAT = S(-320, -268)
    ANKT = S(50, -559); ANKB = S(-46, -492); FREE = S(-190, -90); KNEEB = S(-272, -535)
    return [
        hook("GIMNASIO · PIERNAS", ["UNA PIERNA", "EN LA PRENSA 45"], "Fuerza unilateral",
             "Prensa a 45 grados a una pierna: el carro corre por el riel y cada pierna empuja por su cuenta.",
             [C("TOP"), seqloop("TOP", "BOTTOM")]),
        step("LA MÁQUINA", ["CARRO Y", "RIEL 45°"], "Plataforma inclinada",
             "El carro con discos corre sobre un riel a 45 grados y la plataforma queda arriba, donde apoyás el pie.",
             [C("TOP")], [ring(PLATE, 92, 0.8), lab((1040, 800), "DISCOS", "end", 0.8),
                          ring(RAIL, 44, 1.7), lab((560, 1200), "RIEL 45°", "start", 1.7),
                          ring(PLAT, 52, 2.6), lab((1040, 890), "PLATAFORMA", "end", 2.6)], 7.2),
        step("AJUSTE 1 / 2", ["ESPALDA", "Y CADERA"], "Bien apoyado",
             "Apoyá la espalda en el respaldo y la cadera en el asiento, con la cabeza y los hombros relajados.",
             [C("TOP")], [ring(PAD, 60, 0.8), lab((60, 1010), "RESPALDO", "start", 0.8),
                          ring(SEAT, 56, 1.8), lab((60, 1470), "CADERA APOYADA", "start", 1.8)], 7.2),
        step("AJUSTE 2 / 2", ["UNA PIERNA", "AL CENTRO"], "La otra cuelga",
             "Poné un solo pie en el centro de la plataforma y dejá la otra pierna flexionada, sin apoyarla en ningún lado.",
             [C("TOP")], [ring(PLAT, 52, 0.8), lab((1040, 900), "PIE AL CENTRO", "end", 0.8),
                          ring(FREE, 50, 1.8), lab((60, 1450), "PIERNA LIBRE", "start", 1.8)], 7.6),
        step("POSICIÓN INICIAL", ["PIERNA", "ESTIRADA"], "Sin trabar",
             "Arrancá con la pierna casi estirada, la rodilla blanda y el pie bien apoyado en la plataforma.",
             [C("TOP")], [ring(ANKT, 48, 0.8), lab((1040, 900), "SIN TRABAR", "end", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ", "CONTROLANDO"], "Rodilla al pecho",
             "Paso uno. Bajá la plataforma doblando la rodilla hacia el pecho, sin que la cadera se despegue del asiento.",
             [C("TOP"), TO("BOTTOM", 0.6, 1.2)],
             [arrow((739, 894), (647, 985), 0.8, 1.2, [40, 0]),
              lab((60, 900), "BAJÁ LENTO", "start", 1.0)], 7.2),
        step("PASO 2 / 3", ["FONDO", "DEL RECORRIDO"], "Rodilla flexionada",
             "Paso dos. Llegá hasta donde llegues con la cadera apoyada y la rodilla bien flexionada, sin rebotar.",
             [C("BOTTOM"), TO("BOTTOM", 0.2, 0.4)],
             [ring(KNEEB, 52, 0.8), lab((60, 900), "RODILLA AL PECHO", "start", 1.0)], 7.0),
        step("PASO 3 / 3", ["EMPUJÁ", "PAREJO"], "Con toda la planta",
             "Paso tres. Empujá la plataforma con toda la planta del pie, estirando la rodilla sin trabarla de golpe.",
             [C("BOTTOM"), TO("TOP", 0.5, 1.2)],
             [arrow((647, 985), (739, 894), 0.8, 1.2, [40, 0]),
              lab((60, 900), "SUBÍ PAREJO", "start", 1.1)], 7.0),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Aire al bajar",
             "Tomá aire al bajar la plataforma y soltalo al empujar. El abdomen queda firme y la cadera apoyada.",
             [C("TOP"), seqloop("TOP", "BOTTOM", 0.9, 1.7, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: quedarse a mitad de camino. Bajá hasta donde llegues con la cadera apoyada y sin rebotar.",
             [C("TOP"), TO("SHALLOW_BAD", 0.5, 0.9)], [NO(1.4, (150, 880)), ring(S(10, -532), 50, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TALÓN", "DESPEGADO"], "Planta completa",
             "Error: empujar con la punta y despegar el talón. Todo el pie queda apoyado y empuja parejo.",
             [C("TOP"), TO("HEELS_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(ANKB, 46, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["APOYAR", "LA OTRA"], "Pierna libre",
             "Error: subir los dos pies a la plataforma. La pierna libre queda flexionada y sin apoyar en ningún lado.",
             [C("TOP"), TO("FREELEG_BAD", 0.5, 0.8)], [NO(1.4, (150, 880)), ring(S(-120, -455), 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Cadera apoyada", "Una sola pierna",
                                         "Rodilla con el pie", "Bajá controlando"],
             "Tips: cadera apoyada, una sola pierna en la plataforma, rodilla alineada con el pie y bajada controlada.",
             [C("TOP"), seqloop("TOP", "BOTTOM")]),
        keys("CLAVES", ["TÉCNICA"], ["Espalda en el respaldo", "Empujá con toda la planta",
                                     "Sin trabar la rodilla", "Cambiá de pierna"],
             "Claves: espalda en el respaldo, empujá con toda la planta, sin trabar la rodilla y cambiá de pierna.",
             [{"cut": "BOTTOM", "at": 0.1}]),
        reps(["3 X 10–12"], "Cuádriceps",
             "Tres series de diez a doce por pierna, con dos minutos de pausa. Elegí un peso que te deje llegar al fondo sin despegar la cadera.",
             ["1 · BAJÁ", "2 · FONDO", "3 · SUBÍ"], [C("TOP"), seqloop("TOP", "BOTTOM")]),
        step("AL TERMINAR", ["CAMBIÁ", "DE PIERNA"], "Sin apurarse",
             "Al terminar la serie, dejá la plataforma arriba, trabá el seguro y cambiá de pierna con calma.",
             [C("BOTTOM"), TO("TOP", 0.9, 2.0)],
             [lab((60, 900), "SIN APURARSE", "start", 1.0)], 6.5),
    ]


YT66 = {
    "titulo": "Sled 45 Degrees One Leg Press 🔥 Prensa a una pierna | Gimnasio",
    "tags": ["sled 45 degrees one leg press", "prensa a una pierna", "prensa 45 grados",
             "prensa unilateral", "cuádriceps", "glúteos", "piernas", "máquina de prensa",
             "máquinas de gimnasio", "gimnasio", "principiantes", "rutina de piernas"],
    "descripcion": yt_desc("Sled 45 Degrees One Leg Press",
        "prensa a 45 grados con una sola pierna en la plataforma",
        "cuádriceps y glúteos",
        "La prensa a 45 grados a una pierna trabaja cada lado por separado: el carro corre por el riel y la plataforma se mueve solo con la fuerza de esa pierna. Sirve para corregir diferencias entre lados y mejorar el control. Si cortás el recorrido, despegás el talón o apoyás las dos piernas, el trabajo se reparte y se pierde el objetivo.",
        ["Apoyá la espalda en el respaldo y la cadera en el asiento.",
         "Poné un pie en el centro de la plataforma y dejá la otra pierna colgando."],
        ["Arrancá con la pierna casi estirada y la rodilla blanda.",
         "Bajá la plataforma doblando la rodilla hacia el pecho.",
         "Llegá al fondo sin despegar la cadera ni rebotar.",
         "Empujá con toda la planta hasta estirar la rodilla.",
         "Terminá la serie, trabá el seguro y cambiá de pierna."],
        ["Media repetición → bajá hasta donde llegues con la cadera apoyada.",
         "Talón despegado → planta completa y empuje parejo.",
         "Apoyar las dos piernas → la pierna libre queda flexionada sin apoyar."],
        ["Cadera y espalda apoyadas.", "Una sola pierna en la plataforma.",
         "Rodilla alineada con el pie.", "Bajada controlada, sin rebotar."],
        "Piernas → Cuádriceps → Glúteos",
        "3 series de 10–12 repeticiones por pierna, con 2 minutos de pausa. Nivel: intermedio.",
        "#Gimnasio #Cuadriceps #Prensa45 #PrensaUnilateral #Piernas #Gluteos #Entrenamiento #Fuerza")}

save("sled-45-degrees-one-leg-press", lp1_scenes("sled-45-degrees-one-leg-press"),
     {"pose": "BOTTOM", "zoom": 1.06, "dy": 40}, YT66)
