# Dataset D01 · D9 Lever Decline Chest Press y D10 Lever Incline Chest Press: poses + props + rig.
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


# ── D9 ── Lever Decline Chest Press: respaldo reclinado, manijas bajas, press hacia adelante ──
sit = dict(hip=[-240, -230], ankle=[0, 0], ft=0, g=0)
DEC = {
    "START": {**sit, "b": -32, "hd": -6, "ua": -22, "fa": 120},
    "MID": {**sit, "b": -32, "hd": -6, "ua": 34, "fa": 64},
    "OUT": {**sit, "b": -32, "hd": -6, "ua": 70, "fa": 6},
    "TORSO_BAD": {**sit, "b": 4, "hd": 8, "cv": -16, "ua": 30, "fa": 70},
    "LOCK_BAD": {**sit, "b": -32, "hd": -6, "ua": 76, "fa": -12},
}
print("D9 lever decline chest press")
check(DEC)
base_dataset("lever-decline-chest-press", "Lever Decline Chest Press", "GIMNASIO · PECHO",
             ["Pectorales", "Tríceps"], rig(740, 0.66),
             [{"type": "chestpress", "pivot": [-30, -1010], "frameTop": -1070, "stack": -640,
               "seat": [-390, -90, -184], "back": [-318, -32, 470], "pin": 5}],
             DEC, "START",
             "Sentate con la espalda apoyada en el respaldo reclinado y los pies planos. Empujá las manijas hacia adelante hasta estirar los brazos y volvé lento al pecho.")

# ── D10 ── Lever Incline Chest Press: respaldo casi vertical, manijas altas, press hacia arriba ──
INC = {
    "START": {**sit, "b": -2, "hd": 4, "ua": -5, "fa": 130},
    "MID": {**sit, "b": -2, "hd": 4, "ua": 48, "fa": 68},
    "OUT": {**sit, "b": -2, "hd": 4, "ua": 98, "fa": 8},
    "ARCH_BAD": {**sit, "b": 14, "hd": 16, "cv": 22, "ua": 60, "fa": 44},
    "LOCK_BAD": {**sit, "b": -2, "hd": 4, "ua": 104, "fa": -10},
}
print("D10 lever incline chest press")
check(INC)
base_dataset("lever-incline-chest-press", "Lever Incline Chest Press", "GIMNASIO · PECHO",
             ["Pectorales", "Hombros"], rig(740, 0.66),
             [{"type": "chestpress", "pivot": [-30, -1010], "frameTop": -1070, "stack": -640,
               "seat": [-390, -90, -184], "back": [-318, -2, 470], "pin": 5}],
             INC, "START",
             "Sentate con la espalda apoyada y los pies planos. Agarrá las manijas a la altura de la clavícula, empujá hacia adelante y arriba y volvé lento al pecho.")
