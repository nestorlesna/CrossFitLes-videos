# Dataset D99 Smith Standing Behind Head Military Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def mp_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(-95, -1144); PAR = S(185, -700); STOP = S(185, -300)
    BAR_D = S(*J["DOWN"]["W"]); BAR_T = S(*J["TOP"]["W"]); ELB = S(*J["DOWN"]["E"])
    BAR_H = S(*J["HALF_BAD"]["W"])
    SHO = S(*J["TOP"]["S"]); HIP = S(*J["DOWN"]["H"]); KNEE = S(*J["DOWN"]["K"])
    return [
        hook("GIMNASIO · HOMBROS", ["PRESS", "TRAS NUCA"], "Barra a la nuca",
             "Press militar por detrás de la nuca en la Smith: parado, la barra baja a la nuca y sube por el mismo carril.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.3, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Carril fijo",
             "La Smith te marca el carril: la barra sube y baja siempre por la misma línea, detrás de la cabeza.",
             [C("DOWN")], [ring(BEAM, 64, 0.8), lab((60, 860), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 54, 1.8), lab((60, 940), "PARANTE", "start", 1.8),
                           ring(STOP, 54, 2.8), lab((60, 1120), "TOPE", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA A", "LA NUCA"], "Altura de hombros",
             "Ajustá la barra a la altura de los hombros para arrancar con la barra apoyada en la nuca.",
             [C("DOWN")], [ring(BAR_D, 58, 0.8), lab((60, 860), "BARRA ATRÁS", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["AGARRE", "ANCHO"], "Codos atrás",
             "Agarrá la barra con las palmas al frente, un poco más ancho que los hombros, y los codos atrás.",
             [C("DOWN")], [ring(ELB, 54, 0.8), lab((60, 860), "CODOS ATRÁS", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["ABDOMEN", "FIRME"], "Pecho arriba",
             "Ponete firme: pies al ancho de los hombros, abdomen activo y el pecho arriba.",
             [C("DOWN")], [ring(KNEE, 50, 0.8), lab((60, 860), "ABDOMEN FIRME", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ POR", "EL CARRIL"], "Sin sacar la cabeza",
             "Paso uno. Empujá la barra hacia arriba por el carril, sin sacar la cabeza.",
             [C("DOWN"), TO("TOP", 0.4, 1.0)], [ring(BAR_T, 58, 0.8), lab((60, 860), "SUBÍ EL CARRIL", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["ARRIBA", "ESTIRADO"], "Codos firmes",
             "Paso dos. Estirá los brazos arriba, con los codos casi bloqueados y el torso quieto.",
             [C("TOP"), TO("TOP", 0.2, 0.5)], [ring(BAR_T, 58, 0.8), lab((60, 860), "BRAZOS ESTIRADOS", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ A", "LA NUCA"], "Hasta las orejas",
             "Paso tres. Bajá la barra a la nuca con control, hasta la altura de las orejas.",
             [C("TOP"), TO("DOWN", 0.4, 1.1)], [ring(BAR_D, 58, 0.8), lab((60, 860), "BAJÁ A LA NUCA", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al subir",
             "Tomá aire abajo y soltalo al subir. No aguantes la respiración en el esfuerzo.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.3, 1.2, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: media repetición. Bajá hasta la nuca y subí hasta estirar los brazos.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR_H, 58, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["ESPALDA", "ARQUEADA"], "Abdomen firme",
             "Error: arquear la espalda. El abdomen firme y las costillas abajo, sin tirar la cadera.",
             [C("DOWN"), TO("ARCH_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP, 54, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["HOMBROS", "ARRIBA"], "Hombros abajo",
             "Error: encoger los hombros. Los hombros quedan abajo y la barra sube con los brazos.",
             [C("DOWN"), TO("SHRUG_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(SHO, 54, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Carril fijo", "Abdomen firme",
                                          "Codos atrás", "Bajada controlada"],
             "Tips: carril fijo, abdomen firme, codos atrás y bajada controlada.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.2, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Barra a la nuca", "Torso derecho",
                                     "Codos atrás", "Recorrido completo"],
             "Claves: barra a la nuca, torso derecho, codos atrás y recorrido completo.",
             [{"cut": "TOP", "at": 0.1}]),
        reps(["3 X 8–12"], "Hombros y tríceps",
             "Tres series de ocho a doce repeticiones, con dos minutos de pausa. Peso moderado.",
             ["1 · SUBÍ", "2 · ARRIBA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.3, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA", "BARRA"], "Estirá",
             "Al terminar, dejá la barra en los topes y estirá los hombros antes de seguir.",
             [C("TOP"), TO("DOWN", 0.8, 1.6)],
             [lab((60, 1000), "ESTIRÁ LOS HOMBROS", "start", 1.0)], 6.5),
    ]


YT99 = {
    "titulo": "Smith Standing Behind Head Military Press 🔥 Press tras nuca en la Smith | Hombros",
    "tags": ["smith standing behind head military press", "press tras nuca", "press militar",
             "smith machine", "multipower", "hombros", "deltoides", "tríceps", "gimnasio",
             "intermedio", "rutina de hombros"],
    "descripcion": yt_desc("Smith Standing Behind Head Military Press",
        "press militar parado con la barra guiada bajando por detrás de la nuca",
        "deltoides y tríceps",
        "El press militar por detrás de la nuca en la Smith se hace parado, con la barra guiada bajando hasta la nuca y subiendo por el mismo carril hasta estirar los brazos. El abdomen va firme y el torso derecho para que la espalda no se arquee, y los codos empujan desde atrás. Es un movimiento estable porque la máquina fija la trayectoria, pero conviene empezar con poco peso y movilidad de hombros. Los errores típicos son cortar el recorrido, arquear la espalda y encoger los hombros.",
        ["Ajustá la barra a la altura de los hombros.",
         "Agarrá la barra con las palmas al frente y los codos atrás."],
        ["Ponete firme con el abdomen activo y el pecho arriba.",
         "Empujá la barra hacia arriba por el carril.",
         "Estirá los brazos arriba con el torso quieto.",
         "Bajá la barra a la nuca con control, hasta las orejas.",
         "Completá la serie y dejá la barra en los topes."],
        ["Media repetición → bajá hasta la nuca y subí hasta estirar.",
         "Espalda arqueada → abdomen firme y costillas abajo.",
         "Hombros arriba → los hombros quedan abajo y empujan los brazos."],
        ["Barra apoyada en la nuca, no en el cuello.", "Codos atrás y abajo.",
         "Abdomen firme todo el recorrido.", "Bajada controlada hasta las orejas."],
        "Hombros → Deltoides → Tríceps",
        "3 series de 8–12 repeticiones, con 2 minutos de pausa. Nivel: intermedio.",
        "#Gimnasio #Hombros #Deltoides #Triceps #SmithMachine #Multipower #PressMilitar #Entrenamiento")}

save("smith-standing-behind-head-military-press", mp_scenes("smith-standing-behind-head-military-press"),
     {"pose": "TOP", "zoom": 1.0, "dy": 40}, YT99)
