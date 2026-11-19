# Dataset D85 Smith Low Bar Squat: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def lb_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(0, -884); PAR = S(300, -640); STOP = S(300, -520)
    BAR = S(0, -689); BAR_D = S(0, -428)
    HIP = S(10, -462); HIP_D = S(-65, -240); HIP_H = S(-5, -350)
    KNEE = S(71, -230); KNEE_D = S(172, -201); BACK = S(30, -600)
    FOOT = S(60, 0); FOOT2 = S(20, 0); HEAD_L = S(189, -403)
    return [
        hook("GIMNASIO · PIERNAS", ["BARRA", "BAJA"], "Más cadera",
             "Sentadilla con barra baja en la Smith: la barra apoya abajo, sobre los deltoides, y la cadera viaja atrás.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.5, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Multipower",
             "La barra corre guiada entre los parantes y los topes te dejan una salida de seguridad a la altura justa.",
             [C("UP")], [ring(BEAM, 66, 0.8), lab((60, 800), "BARRA GUIADA", "start", 0.8),
                         ring(PAR, 56, 1.8), lab((60, 880), "PARANTES", "start", 1.8),
                         ring(STOP, 48, 2.8), lab((60, 960), "TOPES", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA", "ABAJO"], "Sobre los deltoides",
             "Apoyá la barra más abajo que en la sentadilla alta, sobre los deltoides posteriores, nunca en la nuca.",
             [C("UP")], [ring(BAR, 62, 0.8), lab((60, 800), "BARRA BAJA", "start", 0.8)], 7.2),
        step("AJUSTE 2 / 2", ["PIES AL", "ANCHO"], "Puntas afuera",
             "Pies al ancho de los hombros con las puntas afuera: la cadera va a viajar más atrás que en la alta.",
             [C("UP")], [ring(FOOT, 50, 0.8), ring(FOOT2, 50, 1.4), lab((60, 800), "PIES AL ANCHO", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["PECHO", "ARRIBA"], "Torso inclinado",
             "Arrancá de pie con el pecho arriba y el torso un poco más inclinado, el abdomen firme y el peso en el pie.",
             [C("UP")], [ring(BACK, 62, 0.8), lab((60, 800), "PECHO ARRIBA", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["CADERA", "ATRÁS"], "Con control",
             "Paso uno. Llevá la cadera atrás y bajá controlado, con las rodillas siguiendo la línea de los pies.",
             [C("UP"), TO("DOWN", 0.4, 1.3)], [ring(HIP_D, 56, 0.8), lab((60, 800), "CADERA ATRÁS", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["TALONES", "ABAJO"], "Pasá la paralela",
             "Paso dos. En el fondo los talones siguen abajo y el torso mantiene su inclinación, sin redondear.",
             [C("DOWN"), TO("DOWN", 0.2, 0.4)], [ring(FOOT, 52, 0.8), lab((60, 800), "TALONES ABAJO", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["SUBÍ", "CON LA CADERA"], "Empujá el piso",
             "Paso tres. Subí empujando el piso y llevando la cadera adelante, sin adelantar los hombros.",
             [C("DOWN"), TO("UP", 0.5, 1.3)], [ring(HIP, 56, 0.8), lab((60, 800), "CADERA ADELANTE", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire arriba, aguantá mientras bajás y soltalo al subir. No sueltes el aire en el fondo.",
             [C("UP"), seqloop("UP", "DOWN", 1.3, 1.5, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "SENTADILLA"], "Pasá la paralela",
             "Error: quedarte a mitad de camino. Bajá hasta pasar la paralela con la espalda recta.",
             [C("UP"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP_H, 56, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["CAER", "ADELANTE"], "Torso estable",
             "Error: caer con el pecho adelante. El torso mantiene su inclinación y la barra queda sobre el pie.",
             [C("DOWN"), TO("LEAN_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HEAD_L, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["TALONES", "AFUERA"], "Pie entero",
             "Error: despegar los talones en el fondo. Si no llegás con los talones abajo, no bajes tanto.",
             [C("DOWN"), TO("HEEL_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(FOOT, 50, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Barra en los deltoides", "Cadera atrás",
                                          "Talones abajo", "Rodillas alineadas"],
             "Tips: barra sobre los deltoides, cadera atrás, talones abajo y rodillas alineadas con los pies.",
             [C("UP"), seqloop("UP", "DOWN", 1.2, 1.3, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Barra baja y firme", "Cadera atrás",
                                    "Torso inclinado", "Subida controlada"],
             "Claves: barra baja y firme, cadera atrás, torso inclinado constante y subida controlada.",
             [{"cut": "DOWN", "at": 0.1}]),
        reps(["3 X 6–8"], "Glúteo e isquios",
             "Tres series de seis a ocho repeticiones, con dos minutos de pausa. Es un básico pesado, sin rebote.",
             ["1 · CADERA", "2 · FONDO", "3 · SUBÍ"], [C("UP"), seqloop("UP", "DOWN", 1.3, 1.4, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA BARRA", "EN EL GANCHO"], "Sin apuro",
             "Al terminar la serie, subí derecho, acomodá la barra en los ganchos y salí de la máquina.",
             [C("DOWN"), TO("UP", 0.9, 2.2)],
             [lab((60, 800), "SIN APURO", "start", 1.0)], 6.5),
    ]


YT85 = {
    "titulo": "Smith Low Bar Squat 🔥 Sentadilla con barra baja | Glúteo",
    "tags": ["smith low bar squat", "sentadilla barra baja", "low bar squat", "smith machine", "multipower",
             "glúteo", "isquios", "cuádriceps", "piernas", "gimnasio", "intermedio"],
    "descripcion": yt_desc("Smith Low Bar Squat",
        "sentadilla con barra baja sobre los deltoides en la máquina Smith",
        "glúteo e isquios",
        "En la sentadilla con barra baja la barra apoya más abajo, sobre los deltoides posteriores, y el torso se inclina un poco más que en la sentadilla alta. Eso hace que la cadera viaje más atrás y que el glúteo y los isquios hagan más trabajo, con un recorrido profundo y los talones apoyados. La barra guiada de la Smith te deja concentrarte en la posición. Los errores típicos son quedarse a media altura, caer con el pecho adelante y despegar los talones.",
        ["Apoyá la barra sobre los deltoides, más abajo que en la alta.",
         "Pies al ancho de los hombros con las puntas afuera."],
        ["Llevá la cadera atrás y bajá controlado.",
         "Mantené el torso inclinado y los talones abajo.",
         "Pasá la paralela sin redondear la espalda.",
         "Subí empujando el piso con todo el pie.",
         "Completá la serie y dejá la barra en los ganchos."],
        ["Media sentadilla → pasá la paralela.", "Caer adelante → torso estable y pecho arriba.",
         "Talones afuera → si no llegás, no bajes tanto."],
        ["Barra baja, sobre los deltoides.", "Cadera atrás, rodillas en línea con los pies.",
         "Talones pegados al piso.", "Sin rebote en el fondo."],
        "Piernas → Glúteo → Isquios",
        "3 series de 6–8 repeticiones, con 2 minutos de pausa. Nivel: intermedio.",
        "#Gimnasio #Sentadilla #LowBarSquat #SmithMachine #Gluteo #Isquios #Piernas #Fuerza")}

save("smith-low-bar-squat", lb_scenes("smith-low-bar-squat"),
     {"pose": "DOWN", "zoom": 1.02, "dy": 20}, YT85)
