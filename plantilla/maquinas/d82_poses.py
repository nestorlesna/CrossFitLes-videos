# Dataset D106-D117 (Smith + banco: declinado, inclinado, agarres y variantes): poses + props + rig.
# Banco con `tilt` (grados, + = cabecera arriba) y `pivot`; runtime dibuja las patas verticales hasta el piso
# para que el banco no quede flotando.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}


def base_dataset(clave, name, category, tags, rig_, props, poses, initial, descripcion):
    p = os.path.join(R, "ejercicios", clave + ".json")
    s = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
    s.update({"slug": clave, "name": name, "maquina": True, "category": category, "tags": tags,
              "descripcion": descripcion, "revisado": s.get("revisado", False), "notas": s.get("notas", ""),
              "music": True, "musicVolume": 0.18, "rig": rig_, "shadow": False, "initialPose": initial,
              "props": props, "poses": poses})
    s.setdefault("frames", [])
    json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return s


# --- geometria comun -------------------------------------------------------------------------------------
# Declinado: cabecera abajo a la izquierda, pies en el piso a la derecha. Torso b = -90 - 15 = -105.
DECL = dict(hip=[0, -272], ankle=[235, 0], b=-105, hd=-107, ft=0, g=1, hx=-235, ed=1)
# Inclinado: cabecera arriba a la izquierda, pies en el piso. Torso b = -90 + 30 = -60.
INCL = dict(hip=[0, -238], ankle=[230, 0], b=-60, hd=-62, ft=0, g=1, hx=-160, ed=1)
# Plano (agarre ancho): mismo banco que D105.
FLAT = dict(hip=[-20, -196], ankle=[230, 0], b=-90, hd=-92, ft=0, g=1, hx=-235, ed=1)

BENCH_DECL = {"type": "bench", "x0": -380, "x1": 80, "h": 300, "tilt": -15, "pivot": [80, -266]}
BENCH_INCL = {"type": "bench", "x0": -400, "x1": 20, "h": 240, "tilt": 30, "pivot": [20, -206]}
BENCH_FLAT = {"type": "bench", "x0": -560, "x1": 120, "h": 200}


def press(base, hx, top, mid, bot):
    st = dict(base, hx=hx)
    return {
        "TOP": {**st, "hy": top},
        "MID": {**st, "hy": mid},
        "BOTTOM": {**st, "hy": bot},
        "SHORT_BAD": {**st, "hy": round((top + bot) / 2 + (top - bot) * 0.18)},
        "NECK_BAD": {**st, "hip": [base["hip"][0] + 70, base["hip"][1]], "hy": bot - 18},
        "BUTT_BAD": {**st, "hip": [base["hip"][0], base["hip"][1] - 34], "b": base["b"] - 12, "hy": mid, "cv": -20},
    }


# D106 declinado: barra al pecho bajo. Hombro ~(-270,-199); TOP -430 / MID -320 / BOTTOM -220.
DECL_P = press(DECL, -235, -510, -360, -220)
# D108 inclinado: barra al pecho alto. Hombro ~(-242,-378); TOP -600 / MID -470 / BOTTOM -340.
INCL_P = press(INCL, -160, -680, -510, -340)
# D110 elevacion de hombros: brazos estirados, recorrido corto arriba de la cabeza.
SHOULDER_P = press(INCL, -160, -690, -660, -630)
# D112 extension de triceps: barra a la frente, codos altos y quietos (ed -1 = codo atras).
TRICEPS_P = {k: {**v, "ed": -1} for k, v in press(INCL, -270, -700, -585, -470).items()}
# D111/D113 declinado agarre cerrado: mismas poses que D106.
# D116 ancho plano: mismas poses que D105 (TOP -505 / MID -390 / BOTTOM -272).
FLAT_P = press(FLAT, -235, -505, -390, -272)
# D117 ancho declinado: mismas poses que D106.
# D114 sentado, una pierna: barra sobre los muslos.
CALF = dict(hip=[-30, -250], ankle=[215, 0], ankle2=[205, 0], ft=0, ft2=0, b=2, hd=0, g=1, hx=100, ed=1)
CALF_P = {
    "DOWN": {**CALF, "hy": -238},
    "UP": {**CALF, "ankle": [210, -30], "ft": 30, "hy": -238},
    "HALF_BAD": {**CALF, "ankle": [213, -14], "ft": 14, "hy": -238},
    "KNEE_BAD": {**CALF, "hip": [-30, -270], "b": 8, "hd": 4, "ankle": [215, -6], "ft": 6, "hy": -238},
    "LEAN_BAD": {**CALF, "b": 16, "hd": 10, "hy": -238},
}
# D115 curl de muneca sentado: antebrazos en los muslos, barra a la altura de las rodillas.
WRIST = dict(hip=[-30, -250], ankle=[215, 0], ankle2=[205, 0], ft=0, ft2=0, b=16, hd=8, g=1, hx=160, ed=1)
WRIST_P = {
    "DOWN": {**WRIST, "hy": -250, "wr": 0},
    "UP": {**WRIST, "hy": -300, "wr": 46},
    "HALF_BAD": {**WRIST, "hy": -275, "wr": 22},
    "FOREARM_BAD": {**WRIST, "hy": -318, "wr": 20, "b": 24, "hd": 12},
    "SWING_BAD": {**WRIST, "hy": -292, "wr": 40, "b": 28, "hd": 16},
}


for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-decline-bench-press", "Smith Decline Bench Press", "GIMNASIO · PECHO",
         ["Pectorales", "Tríceps", "Deltoides anterior"], rig(563, 0.7),
         [BENCH_DECL, {"type": "smith", "x": -235, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         DECL_P, "TOP",
         ("Press de banca declinado en la Smith: el banco baja la cabecera y los pies quedan en el piso. La barra "
          "baja al pecho bajo y sube hasta estirar los brazos, con el énfasis en el pecho inferior.")),
        ("smith-decline-reverse-grip-press", "Smith Decline Reverse-grip Press", "GIMNASIO · PECHO",
         ["Pectorales superiores", "Tríceps", "Deltoides anterior"], rig(563, 0.7),
         [BENCH_DECL, {"type": "smith", "x": -235, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         DECL_P, "TOP",
         ("Press declinado con agarre supino en la Smith: las palmas miran hacia la cara y la barra baja al pecho "
          "bajo. Los codos quedan pegados al torso y el recorrido es corto y controlado.")),
        ("smith-incline-bench-press", "Smith Incline Bench Press", "GIMNASIO · PECHO",
         ["Pectorales superiores", "Deltoides anterior", "Tríceps"], rig(554, 0.7),
         [BENCH_INCL, {"type": "smith", "x": -160, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         INCL_P, "TOP",
         ("Press de banca inclinado en la Smith: el banco queda a unos treinta grados, la espalda apoyada y los "
          "pies en el piso. La barra baja al pecho alto y sube hasta estirar los brazos, cargando el pecho superior.")),
        ("smith-incline-reverse-grip-press", "Smith Incline Reverse-grip Press", "GIMNASIO · PECHO",
         ["Pectorales superiores", "Tríceps", "Deltoides anterior"], rig(554, 0.7),
         [BENCH_INCL, {"type": "smith", "x": -160, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         INCL_P, "TOP",
         ("Press inclinado con agarre supino en la Smith: el banco inclinado y las palmas hacia la cara. La barra "
          "baja al pecho alto con los codos cerca del torso y sube hasta estirar los brazos.")),
        ("smith-incline-shoulder-raises", "Smith Incline Shoulder Raises", "GIMNASIO · PECHO",
         ["Deltoides anterior", "Serrato anterior", "Pectorales superiores"], rig(554, 0.7),
         [BENCH_INCL, {"type": "smith", "x": -160, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         SHOULDER_P, "TOP",
         ("Elevación de hombros en banco inclinado: sentado con la espalda en el respaldo y los brazos estirados, "
          "la barra sube desde atrás de la cabeza hasta arriba. El recorrido es corto y los codos no se doblan.")),
        ("smith-machine-decline-close-grip-bench-press", "Smith Machine Decline Close Grip Bench Press", "GIMNASIO · BRAZOS",
         ["Tríceps", "Pectorales", "Deltoides anterior"], rig(563, 0.7),
         [BENCH_DECL, {"type": "smith", "x": -235, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         DECL_P, "TOP",
         ("Press declinado con agarre cerrado en la Smith: manos al centro sobre el pecho bajo y codos pegados al "
          "torso. El tríceps hace más fuerza y el peso baja bastante.")),
        ("smith-machine-incline-tricep-extension", "Smith Machine Incline Tricep Extension", "GIMNASIO · BRAZOS",
         ["Tríceps", "Deltoides anterior"], rig(554, 0.7),
         [BENCH_INCL, {"type": "smith", "x": -270, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         TRICEPS_P, "TOP",
         ("Extensión de tríceps en banco inclinado: la barra baja a la frente con los codos altos y quietos, y "
          "sube hasta estirar los brazos. Los codos apuntan arriba y no se abren.")),
        ("smith-machine-reverse-decline-close-grip-bench-press", "Smith Machine Reverse Decline Close Grip Bench Press", "GIMNASIO · BRAZOS",
         ["Tríceps", "Pectorales", "Deltoides anterior"], rig(563, 0.7),
         [BENCH_DECL, {"type": "smith", "x": -235, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         DECL_P, "TOP",
         ("Press declinado con agarre cerrado y supino en la Smith: palmas hacia la cara, manos al centro y codos "
          "pegados. La barra baja al pecho bajo y el tríceps trabaja fuerte.")),
        ("smith-seated-one-leg-calf-raise", "Smith Seated One Leg Calf Raise", "GIMNASIO · PANTORRILLAS",
         ["Gemelos", "Sóleo"], rig(480, 0.8),
         [{"type": "bench", "x0": -260, "x1": 180, "h": 284},
          {"type": "smith", "x": 100, "top": -830, "gap": 280, "stops": -250, "track": "hands", "r": 56}],
         CALF_P, "DOWN",
         ("Elevación de talón sentado con una pierna en la Smith: la barra apoya sobre los muslos y el talón del "
          "pie apoyado sube todo lo posible. La otra pierna queda afuera, sin empujar.")),
        ("smith-seated-wrist-curl", "Smith Seated Wrist Curl", "GIMNASIO · ANTEBRAZOS",
         ["Antebrazos", "Flexores de muñeca"], rig(480, 0.8),
         [{"type": "bench", "x0": -260, "x1": 180, "h": 284},
          {"type": "smith", "x": 160, "top": -830, "gap": 280, "stops": -250, "track": "hands", "r": 56}],
         WRIST_P, "DOWN",
         ("Curl de muñeca sentado en la Smith: los antebrazos apoyados en los muslos y las palmas hacia arriba. "
          "Las muñecas suben la barra y bajan despacio, sin mover los antebrazos.")),
        ("smith-wide-grip-bench-press", "Smith Wide Grip Bench Press", "GIMNASIO · PECHO",
         ["Pectorales", "Tríceps", "Deltoides anterior"], rig(600, 0.7),
         [BENCH_FLAT, {"type": "smith", "x": -235, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         FLAT_P, "TOP",
         ("Press de banca con agarre amplio en la Smith: las manos bien abiertas y los codos hacia afuera. La "
          "barra baja al pecho y sube hasta estirar los brazos, con más trabajo del pecho.")),
        ("smith-wide-grip-decline-bench-press", "Smith Wide Grip Decline Bench Press", "GIMNASIO · PECHO",
         ["Pectorales", "Tríceps", "Deltoides anterior"], rig(563, 0.7),
         [BENCH_DECL, {"type": "smith", "x": -235, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         DECL_P, "TOP",
         ("Press declinado con agarre amplio en la Smith: manos bien abiertas, codos hacia afuera y la barra al "
          "pecho bajo. El pecho inferior hace la mayor parte del trabajo.")),
]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
