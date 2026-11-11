# Dataset D01 · D20 Lever Seated Squat Calf Raise on Leg Press Machine y D21 Lever Lying Two-one Leg Curl: poses + props + rig.
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

# ── D20 ── Lever Seated Squat Calf Raise on Leg Press Machine: rodillas casi estiradas, sube y baja los talones ──
c20 = dict(hip=HIP, b=-45, hd=-12, g=1, hx=-280, hy=-310, ed=1)
calf = {
    "PRESS": {**c20, "ankle": on_rail(HIP, 35, 444), "ft": -96},
    "MID": {**c20, "ankle": on_rail(HIP, 35, 438), "ft": -128},
    "HEELS": {**c20, "ankle": on_rail(HIP, 35, 432), "ft": -165},
    "KNEE_BAD": {**c20, "ankle": on_rail(HIP, 35, 370), "ft": -128},
    "HIP_BAD": {**c20, "hip": [-292, -258], "b": -36, "hd": -4, "ankle": on_rail(HIP, 35, 438), "ft": -128},
}
print("D20 lever seated squat calf raise on leg press machine")
check(calf)
base_dataset("lever-seated-squat-calf-raise-on-leg-press-machine",
             "Lever Seated Squat Calf Raise on Leg Press Machine", "GIMNASIO · PIERNAS",
             ["Gemelos", "Cuádriceps"], rig(640, 0.76),
             [{"type": "legpress", "hip": HIP, "ang": 35, "lean": -45, "stops": 300}],
             calf, "MID",
             "Sentate con la espalda apoyada y las puntas de los pies en la plataforma. Con las rodillas casi estiradas, bajá los talones y empujá de nuevo subiéndolos.")

# ── D21 ── Lever Lying Two-one Leg Curl: sentado, rodillo detrás del tobillo, flexiona hacia los glúteos ──
sc = dict(t=-90, b=-14, hd=-6, g=1, hx=-180, hy=-330, ed=1, hip=[-240, -345])
curl21 = {
    "EXT": {**sc, "s": -84, "ft": -70},
    "MID": {**sc, "s": -32, "ft": -20},
    "CURL": {**sc, "s": 26, "ft": 20},
    "HIP_BAD": {**sc, "hip": [-240, -384], "b": -6, "hd": 4, "cv": 24, "s": 20, "ft": 16, "hx": -192, "hy": -356},
    "PAD_BAD": {**sc, "hip": [-240, -360], "s": 20, "ft": 16, "bf": 1},
}
print("D21 lever lying two-one leg curl")
check(curl21)
base_dataset("lever-lying-two-one-leg-curl", "Lever Lying Two-one Leg Curl", "GIMNASIO · PIERNAS",
             ["Isquiotibiales", "Glúteos"], rig(700, 0.8),
             [{"type": "seatedlegcurl", "pivot": [0, -345], "seat": [-330, -30, -300], "back": [-322, -14, 430],
               "stack": -600, "handle": [-180, -330], "roll": 212, "thigh": [-70, -401], "pin": 5}],
             curl21, "EXT",
             "Sentate con la espalda apoyada y la rodilla alineada al eje. Bajá la traba sobre los muslos, enganchá los tobillos y flexioná las piernas hacia los glúteos.")
