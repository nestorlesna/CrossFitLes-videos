# Dataset D01 — D7 Lever Back Extension y D8 Lever Reverse Hyperextension: poses + props + rig.
import sys, os, json, csv
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


# — D7 — Lever Back Extension: sentado, almohadilla en la espalda alta, extensión lumbar —
sit = dict(hip=[-240, -230], ankle=[70, -20], ft=0, g=0)
D7 = {
    "UP": {**sit, "b": 6, "hd": 2, "ua": 22, "fa": 150},
    "FWD": {**sit, "b": 34, "hd": 30, "ua": 16, "fa": 150},
    "DEEP": {**sit, "b": 48, "hd": 44, "ua": 12, "fa": 150},
    "ROUND_BAD": {**sit, "b": 48, "hd": 76, "cv": 30, "ua": 12, "fa": 150},
    "HYPER_BAD": {**sit, "b": -10, "hd": -18, "ua": 24, "fa": 150},
}
print("D7 lever back extension")
check(D7)
base_dataset("lever-back-extension", "Lever Back Extension", "GIMNASIO · ESPALDA BAJA",
             ["Lumbares", "Glúteos"], rig(720, 0.66),
             [{"type": "abcrunch", "seat": [-380, -90, -230], "pivot": [-420, -520], "stack": -640, "feet": [70, -20],
               "pin": 5, "padBack": True}],
             D7, "UP",
             "Sentate con la espalda apoyada en la almohadilla y los pies fijos. Inclinate adelante y volvé extendiendo la espalda baja.")

# — D8 — Lever Reverse Hyperextension: boca abajo, cadera en la almohadilla, piernas suben —
A = (0, -60); U = (math.sin(rad(45)), -math.cos(rad(45)))
H = (round(A[0] + U[0] * 466, 1), round(A[1] + U[1] * 466, 1))
PAD = (round(H[0] + 0.707 * 62 - U[0] * 20), round(H[1] + 0.707 * 62 - U[1] * 20))


def arms(b): return {"ua": round(-b + 26, 1), "fa": 140}
D8 = {
    "REST": {"hip": list(H), "ankle": list(A), "b": 45, "hd": 50, "ft": 45, "g": 0, **arms(45)},
    "MID": {"hip": list(H), "ankle": [-110, -229], "b": 45, "hd": 50, "ft": 45, "g": 0, **arms(45)},
    "TOP": {"hip": list(H), "ankle": [-137, -430], "b": 45, "hd": 45, "ft": 45, "g": 0, **arms(45)},
    "HIP_BAD": {"hip": list(H), "ankle": [-137, -430], "b": 26, "hd": 30, "ft": 45, "g": 0, **arms(26)},
    "ARCH_BAD": {"hip": list(H), "ankle": [-110, -550], "b": 62, "hd": 72, "ft": 45, "g": 0, "cv": -20, **arms(62)},
}
print("D8 lever reverse hyperextension")
check(D8)
base_dataset("lever-reverse-hyperextension", "Lever Reverse Hyperextension", "GIMNASIO · GLÚTEOS",
             ["Glúteos", "Isquiotibiales"], rig(470, 0.74),
             [{"type": "backext45", "foot": list(A), "pad": list(PAD), "roll": False, "ang": 45}],
             D8, "REST",
             "Boca abajo con la cadera en la almohadilla y las piernas colgando. Subí las piernas con los glúteos y bajá lento.")
