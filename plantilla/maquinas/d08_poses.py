# Dataset D01 · D16 Lever Reverse Grip Lateral Pulldown y D17 Reverse Grip Machine Lat Pulldown: poses + props + rig.
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


# ── D16 ── Lever Reverse Grip Lateral Pulldown: sentado, agarre prono ancho, tira al cuello alto ──
lat = dict(hip=[-240, -232], ankle=[0, 0], ft=0, g=1, ed=-1)
LAT = {
    "TOP": {**lat, "b": -2, "hd": 2, "hx": -205, "hy": -830},
    "MID": {**lat, "b": -8, "hd": -2, "hx": -200, "hy": -690},
    "PULL": {**lat, "b": -12, "hd": -6, "hx": -245, "hy": -500},
    "NECK_BAD": {**lat, "b": 14, "hd": 30, "hx": -226, "hy": -600},
    "LEAN_BAD": {**lat, "b": -40, "hd": -22, "hx": -318, "hy": -450},
}
print("D16 lever reverse grip lateral pulldown")
check(LAT)
base_dataset("lever-reverse-grip-lateral-pulldown", "Lever Reverse Grip Lateral Pulldown", "GIMNASIO · ESPALDA",
             ["Dorsales", "Bíceps"], rig(740, 0.66),
             [{"type": "latpulldown", "x": 300, "pulley": [-215, -1130], "seat": -186,
               "pad": [-75, -290], "pin": 6, "rest": 307}],
             LAT, "TOP",
             "Sentate con las rodillas bajo la almohadilla y el pecho alto. Tirá de las asas al pecho guiando con los codos y juntá los omóplatos.")

# ── D17 ── Reverse Grip Machine Lat Pulldown: sentado, agarre supino, jalón al pecho bajo ──
rev = dict(hip=[-240, -232], ankle=[0, 0], ft=0, g=1, ed=-1)
REV = {
    "TOP": {**rev, "b": 0, "hd": 2, "hx": -220, "hy": -790},
    "MID": {**rev, "b": -6, "hd": -2, "hx": -190, "hy": -650},
    "PULL": {**rev, "b": -8, "hd": -4, "hx": -240, "hy": -470},
    "NECK_BAD": {**rev, "b": 16, "hd": 32, "hx": -226, "hy": -575},
    "LEAN_BAD": {**rev, "b": -38, "hd": -20, "hx": -320, "hy": -430},
}
print("D17 reverse grip machine lat pulldown")
check(REV)
base_dataset("reverse-grip-machine-lat-pulldown", "Reverse Grip Machine Lat Pulldown", "GIMNASIO · ESPALDA",
             ["Dorsales", "Bíceps"], rig(740, 0.66),
             [{"type": "latpulldown", "x": 300, "pulley": [-215, -1090], "seat": -170,
               "pad": [-70, -270], "pin": 5, "rest": 307}],
             REV, "TOP",
             "Sentate con las rodillas bajo la almohadilla y el pecho alto. Con agarre supino, tirá de las asas al pecho juntando las escápulas y soltá lento.")
