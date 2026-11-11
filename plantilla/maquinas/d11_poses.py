# Dataset D01 · D22 Lever Seated Reverse Fly y D23 Lever Seated Reverse Fly (Parallel Grip): poses + props + rig.
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


PIVOT = [-230, -839]
SEAT = [-390, -90, -184]
CHEST = [-185, -340]
STACK = -640

# ── D22 / D23 ── reverse pec deck: pecho contra el apoyo, brazos adelante y apertura hacia atrás ──
pc = dict(hip=[-240, -230], ankle=[0, 0], ft=0, g=0, b=-4, hd=0)
fly = {
    "FRONT": {**pc, "ua": 88, "fa": -14, "al": 0.95},
    "MID": {**pc, "ua": 88, "fa": -14, "al": 0.65},
    "BACK": {**pc, "ua": 86, "fa": -22, "al": 0.34},
    "ELBOW_BAD": {**pc, "ua": 20, "fa": 90, "al": 0.95},
    "LEAN_BAD": {**pc, "b": -22, "hd": -10, "ua": 88, "fa": -14, "al": 0.6},
    "SHRUG_BAD": {**pc, "b": 4, "hd": 10, "cv": 24, "ua": 88, "fa": -14, "al": 0.8},
}
flyp = {k: dict(v) for k, v in fly.items()}
for v in flyp.values(): v["wr"] = 90

for clave, nombre, poses, amp in [
        ("lever-seated-reverse-fly", "Lever Seated Reverse Fly", fly, False),
        ("lever-seated-reverse-fly-parallel-grip", "Lever Seated Reverse Fly (Parallel Grip)", flyp, True)]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, "GIMNASIO · HOMBROS", ["Deltoides", "Trapecios", "Romboides"],
                 rig(720, 0.66),
                 [{"type": "pecdeck", "pivot": PIVOT, "frameTop": -1060, "stack": STACK,
                   "seat": SEAT, "chest": CHEST, "pin": 4}],
                 poses, "FRONT",
                 ("Sentate con el pecho contra la almohadilla y los pies planos en el suelo. "
                  "Con los codos apenas flexionados, abrí los brazos hacia atrás y afuera juntando las escápulas, "
                  "y volvé lento a la posición inicial."))
