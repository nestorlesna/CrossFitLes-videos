# Dataset D01 · D14 Lever Front Pulldown y D15 Lever One Arm Lateral Wide Pulldown: poses + props + rig.
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


# ── D14 ── Lever Front Pulldown: sentado, rodillas bajo la almohadilla, jalón al pecho ──
front = dict(hip=[-240, -232], ankle=[0, 0], ft=0, g=1, ed=-1)
FRT = {
    "TOP": {**front, "b": 0, "hd": 2, "hx": -215, "hy": -830},
    "MID": {**front, "b": -8, "hd": -2, "hx": -196, "hy": -680},
    "PULL": {**front, "b": -12, "hd": -6, "hx": -228, "hy": -478},
    "NECK_BAD": {**front, "b": 16, "hd": 34, "hx": -228, "hy": -585},
    "LEAN_BAD": {**front, "b": -40, "hd": -22, "hx": -318, "hy": -440},
}
print("D14 lever front pulldown")
check(FRT)
base_dataset("lever-front-pulldown", "Lever Front Pulldown", "GIMNASIO · ESPALDA",
             ["Dorsales", "Bíceps"], rig(740, 0.66),
             [{"type": "latpulldown", "x": 300, "pulley": [-215, -1130], "seat": -186,
               "pad": [-75, -290], "pin": 5, "rest": 317}],
             FRT, "TOP",
             "Sentate con las rodillas bajo la almohadilla y los pies planos. Tirá de las asas al pecho juntando los omóplatos y soltá lento.")

# ── D15 ── Lever One Arm Lateral Wide Pulldown: pecho apoyado, un brazo, jalón cruzado a la cadera ──
one = dict(hip=[-240, -232], ankle=[0, 0], ft=0, g=1, ed=-1, g2=0, ua2=10, fa2=16, b=18, hd=-8)
ONE = {
    "TOP": {**one, "hx": -100, "hy": -810},
    "MID": {**one, "hx": -55, "hy": -560},
    "PULL": {**one, "hx": -150, "hy": -370},
    "TORSO_BAD": {**one, "b": 2, "hd": 0, "hx": -150, "hy": -500},
    "SHRUG_BAD": {**one, "hd": 18, "cv": 12, "hx": -110, "hy": -700},
}
print("D15 lever one arm lateral wide pulldown")
check(ONE)
base_dataset("lever-one-arm-lateral-wide-pulldown", "Lever One Arm Lateral Wide Pulldown", "GIMNASIO · ESPALDA",
             ["Dorsales", "Bíceps"], rig(740, 0.66),
             [{"type": "latpulldown", "x": 300, "pulley": [-100, -1150], "seat": -186,
               "pad": [-70, -292], "pin": 5, "rest": 347, "chest": [-100, -520]}],
             ONE, "TOP",
             "Apoyá el pecho en la almohadilla y sujetá el asa con un brazo. Tirá hacia abajo y cruzando al lado opuesto, apretá el dorsal y volvé lento.")
