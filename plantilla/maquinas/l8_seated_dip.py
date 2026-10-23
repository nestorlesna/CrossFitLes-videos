# Lote 7 (cont.) · Seated Dip Machine: poses + props (python ... poses) y escenas + YouTube (python ... frames).
# Usa el prop de la familia de tren superior sentado (seateddip = chestpress con el eje atrás y las manijas a los costados).
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *

SLUG = "seated-dip-machine"
def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}
HIP, ANK = [-240, -230], [0, 0]
SEAT = [-390, -90, -184]
def dip(W, b=4, **k):
    p = {"hip": HIP, "ankle": ANK, "ft": 0, "b": b, "hd": 2, "g": 1, "hx": W[0], "hy": W[1], "ed": -1}
    p.update(k); return p

if sys.argv[1:] == ["poses"]:
    P = {
        "TOP": dip((-185, -390)),
        "MID": dip((-195, -290)),
        "BOTTOM": dip((-206, -186)),
        "LEAN_BAD": dip((-150, -200), b=26, hd=30, cv=22),
        "HIGH_BAD": dip((-175, -480)),
        "LOCK_BAD": dip((-210, -176)),
    }
    check(P)
    base_spec(SLUG, "GIMNASIO · BRAZOS", ["Tríceps"], rig(720, 0.66),
              [{"type": "seateddip", "pivot": [-430, -560], "frameTop": -1000, "stack": -640, "seat": SEAT, "back": [-318, 4, 470], "pin": 5}], P, "TOP")
    sys.exit()

s = json.load(open(os.path.join(R, "ejercicios", SLUG + ".json"), encoding="utf-8"))
S, J, pr = Stage(s["rig"]), {k: fk(v) for k, v in s["poses"].items()}, s["props"][0]
def seqloop(a, b, ta=1.4, tb=1.2, at=0.5): return {"seq": [[a, ta], [b, tb]], "at": at, "until": "end"}
C = lambda p: {"cut": p, "at": 0}
TO = lambda p, at=0.6, dur=1.0: {"to": p, "at": at, "dur": dur}
PINP = S(pr["stack"] + 51, -254 + (pr["pin"] - 0.5) * 22)
SEATK = S(pr["back"][0] - 10, pr["seat"][2] + 61)
W = lambda k: S(*J[k]["W"]); E = lambda k: S(*J[k]["E"])
R1, R2, R3 = (1000, 780), (1000, 730), (130, 760)
L = lambda: seqloop("BOTTOM", "TOP", 1.0, 2.0)
F = [
    hook("GIMNASIO · BRAZOS", ["SEATED DIP", "MACHINE"], "Fondos de tríceps sentado",
         "Seated Dip Machine: los fondos de tríceps sentado en máquina. Tríceps fuertes sin colgarte de las paralelas.",
         [C("TOP"), L()]),
    step("LA MÁQUINA", ["LA", "MÁQUINA"], "También: fondos sentado",
         "También le dicen fondos sentado o dip machine. Trabaja los tríceps y suma pecho y hombros.",
         [C("TOP")], [lab(R3, "PILA DE PESO", "start", 0.8), ring(W("TOP"), 36, 1.6), lab(R1, "MANIJAS AL COSTADO", "end", 1.6),
                      ring(SEATK, 26, 2.6), lab(R2, "ALTURA DEL ASIENTO", "end", 2.6)], 7.0),
    step("AJUSTE 1", ["EL", "ASIENTO"], "Manijas a la altura de las costillas",
         "Ajustá el asiento para que, al empezar, las manijas queden a la altura de las costillas.",
         [C("TOP")], [ring(SEATK, 28, 0.8), ring(W("TOP"), 36, 1.6), lab(R1, "ALTURA DE COSTILLAS", "end", 1.6)], 7.0),
    step("AJUSTE 2", ["EL", "PESO"], "Con el pasador",
         "Elegí el peso con el pasador: uno que puedas empujar doce veces sin inclinar el tronco.",
         [C("TOP")], [ring(PINP, 30, 0.8), lab(R3, "PASADOR", "start", 1.0)], 7.0),
    step("POSICIÓN INICIAL", ["ESPALDA", "PEGADA"], "Codos apuntando atrás",
         "Espalda pegada al respaldo, pecho alto, y agarrá las manijas de los costados con los codos apuntando atrás.",
         [C("TOP")], [ring(E("TOP"), 36, 1.0), lab(R1, "CODOS ATRÁS", "end", 1.2)]),
    step("PASO 1 / 3", ["EMPUJÁ", "ABAJO"], "Solo se mueven los antebrazos",
         "Paso uno. Empujá las manijas hacia abajo, con los codos pegados al cuerpo y el tronco quieto.",
         [C("TOP"), TO("BOTTOM", 0.6, 1.2)], [arrow((W("TOP")[0] + 60, W("TOP")[1]), (W("BOTTOM")[0] + 60, W("BOTTOM")[1]), 0.8, 1.0)], numeral="1"),
    step("PASO 2 / 3", ["SIN", "TRABAR"], "Casi estirado abajo",
         "Paso dos. Abajo, llegá casi a estirar los brazos y apretá el tríceps un segundo, sin trabar los codos.",
         [C("BOTTOM")], [ring(E("BOTTOM"), 36, 0.8), lab(R1, "CODOS SIN TRABAR", "end", 1.0)], numeral="2"),
    step("PASO 3 / 3", ["SUBÍ", "LENTO"], "Hasta 90° de codo",
         "Paso tres. Subí lento hasta que los codos queden a unos noventa grados, sin que las placas se apoyen.",
         [C("BOTTOM"), TO("TOP", 0.6, 2.4)], [ring(PINP, 34, 2.0), lab(R3, "SIN APOYAR", "start", 2.0)], numeral="3"),
    step("RESPIRACIÓN", ["RESPIRÁ"], "Soltá el aire al empujar",
         "Soltá el aire mientras empujás hacia abajo y tomalo mientras subís.",
         [C("TOP"), seqloop("BOTTOM", "TOP", 1.0, 2.2, 0.3)], mn=6.0),
    step("ASÍ NO · 1 / 3", ["TRONCO", "ADELANTE"], "Espalda pegada al respaldo",
         "Error: inclinar el tronco adelante y despegar la espalda. Ahí empuja el pecho: espalda pegada y pecho alto.",
         [C("TOP"), TO("LEAN_BAD", 0.5, 1.0)], [NO(), ring(S(*J["LEAN_BAD"]["S"]), 60, 1.4)], 7.2),
    step("ASÍ NO · 2 / 3", ["SUBIR", "DE MÁS"], "Frená en 90°",
         "Error: subir las manijas más arriba del pecho. El hombro se va adelante y sufre: frená con el codo en noventa.",
         [C("TOP"), TO("HIGH_BAD", 0.5, 1.0)], [NO(), ring(S(*J["HIGH_BAD"]["S"]), 50, 1.4)], 7.2),
    step("ASÍ NO · 3 / 3", ["CODOS", "TRABADOS"], "Casi estirado, nunca trabado",
         "Error: trabar los codos de golpe abajo. Llegá casi estirado y empezá a subir.",
         [C("TOP"), TO("LOCK_BAD", 0.5, 0.5)], [NO(), ring(E("LOCK_BAD"), 40, 1.4)], 7.2),
    keys("TIPS DEL PROFE", ["TIPS"], ["Codos atrás y pegados", "Hombros lejos de las orejas", "Abajo sin trabar", "Subí hasta 90°, no más"],
         "Tips de profe: codos atrás y pegados, hombros lejos de las orejas, abajo sin trabar y subí hasta noventa grados.",
         [C("TOP"), L()]),
    keys("CLAVES", ["TÉCNICA"], ["Espalda pegada", "Pecho alto", "Tronco quieto", "Subí lento"],
         "Claves: espalda pegada, pecho alto, tronco quieto y subí lento.",
         [{"cut": "BOTTOM", "at": 0.1}]),
    reps(["3 X 12"], "Un minuto de pausa",
         "Tres series de diez a doce, con un minuto de pausa. Cuando las doce salen fáciles, subí una placa.",
         ["1 · EMPUJÁ ABAJO", "2 · SIN TRABAR", "3 · SUBÍ LENTO"], [C("TOP"), L()]),
]
save(SLUG, F, {"pose": "BOTTOM", "grip": 1, "zoom": 1.1, "dy": 110}, {
    "titulo": "Seated Dip Machine 🔥 Fondos de tríceps sentado en máquina | Gimnasio",
    "tags": ["seated dip", "fondos de tríceps sentado", "dip machine", "máquina de fondos", "fondos en máquina", "tríceps", "tríceps en máquina",
             "brazos", "máquinas de gimnasio", "gimnasio", "principiantes"],
    "descripcion": yt_desc("Seated Dip Machine", "fondos de tríceps sentado en máquina", "tríceps fuertes sin colgarte de las paralelas",
        "¿Todavía no te salen los fondos en paralelas? Esta máquina te da el mismo trabajo de tríceps, sentado y con el peso que elegís. Este video es para vos.",
        ["Ajustá el asiento para que, al empezar, las manijas queden a la altura de las costillas.", "Elegí un peso que puedas empujar 12 veces sin inclinar el tronco."],
        ["Espalda pegada al respaldo, pecho alto y las manijas de los costados con los codos apuntando atrás.",
         "Empujá las manijas hacia abajo con los codos pegados y el tronco quieto.",
         "Abajo, llegá casi a estirar los brazos y apretá el tríceps un segundo, sin trabar.",
         "Subí lento hasta que los codos queden a unos 90°, sin apoyar las placas."],
        ["Inclinar el tronco adelante o despegar la espalda → espalda pegada y pecho alto.",
         "Subir las manijas más arriba del pecho → frená con el codo a 90°: el hombro lo agradece.",
         "Trabar los codos de golpe abajo → casi estirado, nunca trabado.", "Abrir los codos hacia afuera → codos atrás y pegados al cuerpo.",
         "Encoger los hombros → hombros abajo, lejos de las orejas."],
        ["Codos atrás y pegados al cuerpo, no abiertos.", "Espalda pegada al respaldo y pecho alto.", "Hombros abajo, lejos de las orejas.",
         "Abajo casi estirado, sin trabar.", "Subí lento hasta 90° de codo, no más."],
        "Tríceps · Pectoral inferior · Hombros anteriores",
        "3 series de 10–12 repeticiones, con 1 minuto de pausa. Cuando las 12 salen fáciles, subí una placa. Nivel: principiante.",
        "#Gimnasio #SeatedDip #Triceps #Musculacion #Entrenamiento")})
