# Dataset D101 Smith Standing Military Press: escenas + YouTube + miniatura.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def load(slug):
    s = json.load(open(os.path.join(R, "ejercicios", slug + ".json"), encoding="utf-8"))
    return s, Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}


def seqloop(a, b, ta=1.0, tb=1.5, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}


def sp_scenes(slug):
    s, S, J = load(slug)
    BEAM = S(140, -1144); PAR = S(420, -800); STOP = S(420, -560)
    BAR_D = S(*J["DOWN"]["W"]); BAR_T = S(*J["TOP"]["W"]); ELB = S(*J["DOWN"]["E"])
    HIP = S(*J["DOWN"]["H"]); KNEE = S(*J["DOWN"]["K"])
    SH2 = S(70, -706)
    return [
        hook("GIMNASIO · HOMBROS", ["PRESS", "MILITAR"], "Barra al mentón",
             "Press militar parado en la Smith: la barra arranca a la altura de la clavícula y sube hasta estirar los brazos.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.3, 0.4)]),
        step("LA MÁQUINA", ["BARRA", "GUIADA"], "Carril fijo",
             "La Smith fija el carril de la barra: sube y baja siempre por la misma línea, frente a la cara.",
             [C("DOWN")], [ring(BEAM, 64, 0.8), lab((60, 860), "BARRA GUIADA", "start", 0.8),
                           ring(PAR, 54, 1.8), lab((60, 940), "PARANTE", "start", 1.8),
                           ring(STOP, 54, 2.8), lab((60, 1120), "TOPE", "start", 2.8)], 7.2),
        step("AJUSTE 1 / 2", ["BARRA AL", "MENTÓN"], "Clavícula",
             "Ajustá la barra a la altura de la clavícula, con los topes un poco más abajo para poder soltarla.",
             [C("DOWN")], [ring(BAR_D, 58, 0.8), lab((60, 860), "BARRA AL MENTÓN", "start", 1.0)], 7.2),
        step("AJUSTE 2 / 2", ["AGARRE", "FIRME"], "Palmas al frente",
             "Agarrá la barra un poco más ancho que los hombros, con las palmas al frente y las muñecas firmes.",
             [C("DOWN")], [ring(BAR_D, 58, 0.8), lab((60, 860), "AGARRE FIRME", "start", 1.0)], 7.2),
        step("POSICIÓN INICIAL", ["ABDOMEN", "FIRME"], "Pecho arriba",
             "Ponete firme: pies al ancho de los hombros, abdomen activo y el pecho arriba.",
             [C("DOWN")], [ring(KNEE, 50, 0.8), lab((60, 860), "ABDOMEN FIRME", "start", 1.0)], 7.0),
        step("PASO 1 / 3", ["SUBÍ LA", "BARRA"], "Por el carril",
             "Paso uno. Empujá la barra hacia arriba por el carril, sin mover el torso.",
             [C("DOWN"), TO("HALF_BAD", 0.4, 0.8)], [ring(ELB, 54, 0.8), lab((60, 860), "CODOS ABAJO", "start", 1.0)], 7.4),
        step("PASO 2 / 3", ["ESTIRÁ LOS", "BRAZOS"], "Arriba",
             "Paso dos. Estirá los brazos arriba, con el torso quieto y el abdomen firme.",
             [C("HALF_BAD"), TO("TOP", 0.2, 0.7)], [ring(BAR_T, 58, 0.8), lab((60, 860), "BRAZOS ESTIRADOS", "start", 1.0)], 7.2),
        step("PASO 3 / 3", ["BAJÁ AL", "MENTÓN"], "Con control",
             "Paso tres. Bajá la barra al mentón con control, sin dejarla caer.",
             [C("TOP"), TO("DOWN", 0.4, 1.2)], [ring(BAR_D, 58, 0.8), lab((60, 860), "BARRA AL MENTÓN", "start", 1.0)], 7.2),
        step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá al empujar",
             "Tomá aire al bajar y soltalo al empujar. No aguantes la respiración.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.3, 0.3)], mn=6.0),
        step("ASÍ NO · 1 / 3", ["MEDIA", "REPETICIÓN"], "Recorrido completo",
             "Error: media repetición. Subí hasta estirar y bajá hasta el mentón.",
             [C("DOWN"), TO("HALF_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(BAR_D, 58, 1.4)], 7.2),
        step("ASÍ NO · 2 / 3", ["ESPALDA", "ARQUEADA"], "Costillas abajo",
             "Error: arquear la espalda. El abdomen va firme y las costillas abajo.",
             [C("DOWN"), TO("ARCH_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(HIP, 52, 1.4)], 7.2),
        step("ASÍ NO · 3 / 3", ["HOMBROS", "ARRIBA"], "Hombros abajo",
             "Error: encoger los hombros. Los hombros quedan abajo y empujan los brazos.",
             [C("DOWN"), TO("SHRUG_BAD", 0.5, 0.9)],
             [NO(1.4, (940, 660)), ring(SH2, 46, 1.4)], 7.2),
        keys("TIPS DEL PROFE", ["TIPS"], ["Carril fijo", "Abdomen firme",
                                          "Codos abajo", "Recorrido completo"],
             "Tips: carril fijo, abdomen firme, codos abajo y recorrido completo.",
             [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.3, 0.3)]),
        keys("CLAVES", ["TÉCNICA"], ["Barra al mentón", "Torso derecho",
                                     "Codos abajo", "Recorrido completo"],
             "Claves: barra al mentón, torso derecho, codos abajo y recorrido completo.",
             [{"cut": "TOP", "at": 0.1}]),
        reps(["3 X 8–12"], "Hombros y tríceps",
             "Tres series de ocho a doce repeticiones, con dos minutos de pausa.",
             ["1 · SUBÍ", "2 · ARRIBA", "3 · BAJÁ"], [C("DOWN"), seqloop("DOWN", "TOP", 1.2, 1.3, 0.3)]),
        step("AL TERMINAR", ["DEJÁ LA", "BARRA"], "Estirá",
             "Al terminar, dejá la barra en los topes y estirá los hombros y los tríceps.",
             [C("TOP"), TO("DOWN", 0.8, 1.6)],
             [lab((60, 1000), "ESTIRÁ LOS HOMBROS", "start", 1.0)], 6.5),
    ]


YT101 = {
    "titulo": "Smith Standing Military Press 🔥 Press militar parado en la Smith | Hombros",
    "tags": ["smith standing military press", "press militar parado", "press de hombros",
             "smith machine", "multipower", "hombros", "deltoides", "tríceps", "gimnasio",
             "principiantes", "rutina de hombros"],
    "descripcion": yt_desc("Smith Standing Military Press",
        "press militar parado con la barra guiada subiendo frente a la cara",
        "deltoides y tríceps",
        "El press militar parado en la Smith se hace de pie, con la barra guiada arrancando a la altura de la clavícula, por delante de la cara, y subiendo por el mismo carril hasta estirar los brazos. El abdomen va firme, los glúteos activos y el torso derecho para que la espalda no se arquee, y los codos quedan abajo y adelante. La máquina fija la trayectoria, así que el trabajo se concentra en empujar bien. Los errores típicos son cortar el recorrido, arquear la espalda y encoger los hombros.",
        ["Ajustá la barra a la altura de la clavícula y los topes un poco más abajo.",
         "Agarrá la barra un poco más ancho que los hombros."],
        ["Ponete firme con el abdomen activo y el pecho arriba.",
         "Empujá la barra hacia arriba por el carril.",
         "Estirá los brazos arriba con el torso quieto.",
         "Bajá la barra al mentón con control.",
         "Completá la serie y dejá la barra en los topes."],
        ["Media repetición → subí hasta estirar y bajá hasta el mentón.",
         "Espalda arqueada → abdomen firme y costillas abajo.",
         "Hombros arriba → los hombros quedan abajo y empujan los brazos."],
        ["Barra a la altura de la clavícula, no del cuello.", "Codos abajo y adelante.",
         "Abdomen firme todo el recorrido.", "Bajada controlada hasta el mentón."],
        "Hombros → Deltoides → Tríceps",
        "3 series de 8–12 repeticiones, con 2 minutos de pausa. Nivel: principiante.",
        "#Gimnasio #Hombros #Deltoides #Triceps #SmithMachine #Multipower #PressMilitar #Entrenamiento")}

save("smith-standing-military-press", sp_scenes("smith-standing-military-press"),
     {"pose": "TOP", "zoom": 1.0, "dy": 40}, YT101)
