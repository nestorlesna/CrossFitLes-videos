# Dataset D01 · D12 Lever Standing Chest Press y D13 Machine Inner Chest Press: poses + props + rig.
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


# ── D12 ── Lever Standing Chest Press: de pie frente a la palanca, empuje al pecho ──
stand = dict(hip=[0, -455], ankle=[15, 0], ft=0, g=0)
STD = {
    "START": {**stand, "b": 3, "hd": 0, "ua": -2, "fa": 116},
    "MID": {**stand, "b": 3, "hd": 0, "ua": 46, "fa": 66},
    "OUT": {**stand, "b": 3, "hd": 0, "ua": 86, "fa": 8},
    "LEAN_BAD": {**stand, "b": 22, "hd": 14, "cv": -14, "ua": 40, "fa": 72},
    "LOCK_BAD": {**stand, "b": 3, "hd": 0, "ua": 94, "fa": -10},
}
print("D12 lever standing chest press")
check(STD)
base_dataset("lever-standing-chest-press", "Lever Standing Chest Press", "GIMNASIO · PECHO",
             ["Pectorales", "Hombros"], rig(740, 0.62),
             [{"type": "chestpress", "pivot": [-30, -1010], "frameTop": -1070, "stack": -640,
               "seat": [-260, -40, -40], "stand": True, "pin": 5}],
             STD, "START",
             "Parate frente a la máquina con los pies planos y las manijas a la altura del pecho. Empujá hacia adelante hasta estirar los brazos y volvé lento al pecho.")

# ── D13 ── Machine Inner Chest Press: sentado, codos cerca del cuerpo, pecho interno ──
sit = dict(hip=[-240, -230], ankle=[0, 0], ft=0, g=0)
INN = {
    "START": {**sit, "b": -4, "hd": 2, "ua": -2, "fa": 118},
    "MID": {**sit, "b": -4, "hd": 2, "ua": 40, "fa": 70},
    "OUT": {**sit, "b": -4, "hd": 2, "ua": 80, "fa": 10},
    "ELBOW_BAD": {**sit, "b": -4, "hd": 2, "ua": 30, "fa": 150},
    "LOCK_BAD": {**sit, "b": -4, "hd": 2, "ua": 88, "fa": -12},
}
print("D13 machine inner chest press")
check(INN)
base_dataset("machine-inner-chest-press", "Machine Inner Chest Press", "GIMNASIO · PECHO",
             ["Pectorales", "Tríceps"], rig(740, 0.66),
             [{"type": "chestpress", "pivot": [-30, -1010], "frameTop": -1070, "stack": -640,
               "seat": [-390, -90, -184], "back": [-318, -4, 470], "pin": 5}],
             INN, "START",
             "Sentate con la espalda apoyada y los codos cerca del cuerpo. Empujá las manijas hacia adelante juntando el pecho y volvé lento, sin trabar los codos.")
