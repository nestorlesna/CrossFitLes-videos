# Dataset D78 Smith Chair Squat: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def chair_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(0, -884); PAR = S(300, -640); STOP = S(300, -520)
    SEAT = S(-200, -250); BAR_UP = S(0, -726); BAR_D = S(0, -467)
    BACK = S(28, -629); HIP_D = S(-90, -250); HIP_H = S(-40, -370)
    KNEE = S(71, -230); FOOT = S(60, 0); FOOT2 = S(-20, 0); HEAD_L = S(166, -404)
    return [
        hook("GIMNASIO · PIERNAS", ["SENTADILLA", "AL BANCO"], "En la Smith",
             "Sentadilla al banco en la Smith: la barra en la espalda, bajás hasta tocar el banco y subís sin desplomarte.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.4, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes y el banco te marca la profundidad: bajás hasta tocarlo suave.",
             [C("UP")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                         ring(SEAT, 62, 1.8), lab((60, 880), "BANCO", "start", 1.8),
                         ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA EN", "LA ESPALDA"], "Sobre los trapecios",
             "Apoyá la barra sobre los trapecios y sacala de los ganchos con las manos a los costados.",
             [C("UP")], [ring(BAR_UP, 66, 0.8), lab((60, 800), "BARRA EN LA ESPALDA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES AL", "ANCHO"], "Puntas afuera",
             "Parate con los pies al ancho de la cadera y las puntas un poco hacia afuera, el banco justo detrás.",
             [C("UP")], [ring(FOOT, 50, 0.8), ring(FOOT2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["DE PIE", "DERECHO"], "Espalda recta",
             "Arrancá de pie, con la espalda recta, el abdomen firme y la mirada al frente.",
             [C("UP")], [ring(BACK, 62, 0.8), lab((60, 800), "ESPALDA RECTA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["BAJÁ AL", "BANCO"], "Controlá la bajada",
             "Paso uno. Bajá llevando la cola hacia atrás hasta tocar el banco, sin dejar caer el peso.",
             [C("UP"), TO("DOWN", 0.4, 1.1)], [ring(SEAT, 60, 0.8), lab((60, 800), "AL BANCO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["TOCÁ", "SIN CAER"], "Toque suave",
             "Paso dos. Tocá el banco sin sentarte ni dejarte caer: el peso queda en los pies, listo para subir.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(SEAT, 60, 0.8), lab((60, 800), "SIN SENTARTE", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["SUBÍ CON", "TODO EL PIE"], "Empujá el piso",
             "Paso tres. Subí empujando el piso con todo el pie y apretando el glúteo, sin adelantar las rodillas.",
             [C("DOWN"), TO("UP", 0.5, 1.2)], [ring(FOOT, 54, 0.8), lab((60, 800), "PIE ENTERO", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire cuando bajás y soltalo cuando subís. No aguantes el aire abajo.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.4, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "SENTADILLA"], "Hasta el banco",
             "Error: quedarte a mitad de camino. Bajá hasta tocar el banco en cada repetición.",
             [C("UP"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP_H, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["TALONES", "AFUERA"], "Pie entero",
             "Error: levantar los talones. El pie va entero en el piso, con el peso repartido de punta a talón.",
             [C("DOWN"), TO("HEEL_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(FOOT, 50, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TIRARSE", "ADELANTE"], "Torso firme",
             "Error: tirarte adelante con la espalda. El pecho sube junto con la cadera, sin doblar la cintura.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HEAD_L, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra en los trapecios", "Cola al banco",
                                          "Talones abajo", "Subí apretando"],
             "Tips: barra en los trapecios, cola al banco, talones abajo y subí apretando el glúteo.",
             [C("UP"), seqloop("UP", "DOWN", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Tocá el banco", "Sin sentarte",
                                    "Rodillas afuera", "Subida controlada"],
             "Claves: tocá el banco, sin sentarte, rodillas afuera y subida controlada.",
             [{"cut": "DOWN", "at": 0.1}]),
        reps(["3 X 10–12"], "Cuádriceps y glúteo",
             "Tres series de diez a doce repeticiones, con un minuto de pausa. Peso moderado y bajada lenta.",
             ["1 · BAJÁ", "2 · TOCÁ", "3 · SUBÍ"], [C("UP"), seqloop("UP", "DOWN", 1.1, 1.1, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN LOS GANCHOS"], "Sin apuro",
             "Al terminar la serie, subí derecho, dejá la barra en los ganchos y salí de la máquina sin encorvarte.",
             [C("DOWN"), TO("UP", 0.9, 2.0)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT78 = {
    "titulo": "Smith Chair Squat 🔥 Sentadilla al banco en la Smith | Piernas",
    "tags": ["smith chair squat", "sentadilla al banco", "box squat", "smith machine", "multipower",
             "cuádriceps", "glúteo", "sentadilla", "gimnasio", "principiantes", "rutina de piernas",
             "sentadilla en smith"],
    "descripcion": yt_desc("Smith Chair Squat",
        "sentadilla al banco con barra guiada en la máquina Smith",
        "cuádriceps y glúteo",
        "La sentadilla al banco en la Smith usa el banco como referencia de profundidad: bajás controlado hasta tocar el asiento con la cola y subís sin sentarte del todo. La barra va sobre los trapecios y corre guiada, así que podés concentrarte en el recorrido. Con los pies enteros, las rodillas blandas y el pecho arriba, el trabajo se reparte entre cuádriceps y glúteo. Si te quedás a media altura, levantás los talones o te tirás adelante, la zona lumbar y las rodillas se llevan la carga.",
        ["Apoyá la barra sobre los trapecios y sacala de los ganchos.",
         "Pies al ancho de la cadera, puntas afuera y el banco justo detrás."],
        ["Bajá llevando la cola hacia atrás hasta tocar el banco.",
         "Tocá el asiento sin sentarte ni dejarte caer.",
         "Mantené las rodillas alineadas con los pies.",
         "Subí empujando el piso con todo el pie.",
         "Completá la serie y dejá la barra en los ganchos."],
        ["Media sentadilla → bajá hasta tocar el banco.",
         "Talones afuera → pie entero en el piso.",
         "Tirarse adelante → el pecho sube con la cadera."],
        ["Barra en los trapecios, no en la nuca.", "Cola atrás, pecho arriba.",
         "Tocá el banco sin sentarte.", "Subida controlada, sin rebotar."],
        "Piernas → Cuádriceps → Glúteo",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Nivel: principiante.",
        "#Gimnasio #Piernas #Sentadilla #SmithMachine #Gluteo #Cuadriceps #Entrenamiento #Fuerza")}

save("smith-chair-squat", chair_scenes("smith-chair-squat"),
     {"pose": "DOWN", "zoom": 1.02, "dy": 20}, YT78)
