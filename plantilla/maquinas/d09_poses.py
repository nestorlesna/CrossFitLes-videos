# Dataset D01 · D18 Lever Alternate Leg Press y D19 Lever Horizontal One Leg Press: poses + props + rig.
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


def on_rail(hip, ang, d):
    a = rad(ang)
    return [round(hip[0] + math.cos(a) * d, 1), round(hip[1] - math.sin(a) * d, 1)]


HIP = [-320, -300]
REST = [-170, -30]  # pie de la pierna que descansa, apoyado en el piso

# ── D18 ── Lever Alternate Leg Press: prensa 45°, una pierna por vez, alternando ──
b18 = dict(hip=HIP, b=-45, hd=-12, ft=-128, g=1, hx=-280, hy=-310, ed=1, ankle2=REST)
alt = {
    "TOP": {**b18, "ankle": on_rail(HIP, 35, 452)},
    "MID": {**b18, "ankle": on_rail(HIP, 35, 395)},
    "BOTTOM": {**b18, "ankle": on_rail(HIP, 35, 333)},
    "LOCK_BAD": {**b18, "ankle": on_rail(HIP, 35, 466)},
    "HIP_BAD": {**b18, "hip": [-292, -258], "b": -36, "hd": -4, "ankle": on_rail(HIP, 35, 333)},
}
print("D18 lever alternate leg press")
check(alt)
base_dataset("lever-alternate-leg-press", "Lever Alternate Leg Press", "GIMNASIO · PIERNAS",
             ["Cuádriceps", "Isquiotibiales"], rig(640, 0.76),
             [{"type": "legpress", "hip": HIP, "ang": 35, "lean": -45, "stops": 300}],
             alt, "BOTTOM",
             "Sentate con la espalda bien apoyada y los pies en la plataforma. Empujá con una pierna hasta casi estirar, volvé lento y alterná con la otra.")

# ── D19 ── Lever Horizontal One Leg Press: prensa horizontal, una sola pierna ──
b19 = dict(hip=HIP, b=-30, hd=-10, ft=-120, g=1, hx=-280, hy=-310, ed=1, ankle2=REST)
hor = {
    "TOP": {**b19, "ankle": on_rail(HIP, 12, 452)},
    "MID": {**b19, "ankle": on_rail(HIP, 12, 392)},
    "BOTTOM": {**b19, "ankle": on_rail(HIP, 12, 332)},
    "LOCK_BAD": {**b19, "ankle": on_rail(HIP, 12, 466)},
    "HIP_BAD": {**b19, "hip": [-292, -258], "b": -22, "hd": -2, "ankle": on_rail(HIP, 12, 332)},
}
print("D19 lever horizontal one leg press")
check(hor)
base_dataset("lever-horizontal-one-leg-press", "Lever Horizontal One Leg Press", "GIMNASIO · PIERNAS",
             ["Glúteos", "Cuádriceps"], rig(640, 0.76),
             [{"type": "legpress", "hip": HIP, "ang": 12, "lean": -30, "stops": 320}],
             hor, "BOTTOM",
             "Sentate con la espalda apoyada y una sola pierna en la placa, con la rodilla a 90 grados. Empujá la placa hasta casi estirar y volvé lento.")
