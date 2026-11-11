# Dataset D01 · D23 Lever Hammer Grip Preacher Curl y D24 Lever Preacher Curl v. 2: poses + props + rig.
import sys, os, json, math
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


# ── D23 / D24 ── curl en máquina Scott / predicador: brazos sobre el apoyo inclinado y codo en el eje ──
PIVOT = [-57, -374]
SEAT = [-390, -90, -184]
PAD = [-192, -457, -79, -333]
STACK = -660

pc = dict(hip=[-240, -230], ankle=[0, 0], ft=0, g=0, b=14, hd=12, ua=42)
curl = {
    "DOWN": {**pc, "fa": 22},
    "MID": {**pc, "fa": 80},
    "UP": {**pc, "fa": 132},
    "OFF_BAD": {"hip": [-240, -230], "ankle": [0, 0], "ft": 0, "g": 0, "b": 2, "hd": 2, "ua": 14, "fa": 120},
    "DROP_BAD": {**pc, "fa": -4},
    "SWING_BAD": {"hip": [-240, -230], "ankle": [0, 0], "ft": 0, "g": 0, "b": -10, "hd": -6, "ua": 30, "fa": 128},
}
hammer = {k: dict(v) for k, v in curl.items()}
for v in hammer.values(): v["wr"] = 90

for clave, nombre, poses in [
        ("lever-hammer-grip-preacher-curl", "Lever Hammer Grip Preacher Curl", hammer),
        ("lever-preacher-curl-v-2", "Lever Preacher Curl v. 2", curl)]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, "GIMNASIO · BRAZOS", ["Bíceps", "Antebrazos"],
                 rig(720, 0.66),
                 [{"type": "preachercurl", "pivot": PIVOT, "frameTop": -1000, "stack": STACK,
                   "seat": SEAT, "pad": PAD, "pin": 5}],
                 poses, "DOWN",
                 ("Sentate en la máquina de curl Scott con las axilas en el borde del apoyo y los brazos "
                  "sobre la almohadilla. Flexioná los codos llevando las manijas hacia los hombros y bajá lento, "
                  "sin despegar los brazos y sin estirar de golpe."))
