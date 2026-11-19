# Dataset D73 Sled One Leg Calf Press On Leg Press: poses + props + rig.
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


# D73 - gemelos a una pierna en la prensa a 45°: solo la pierna cercana empuja con el metatarso; la lejana
# queda flexionada colgando al costado, sin tocar la plataforma.
st9 = dict(hip=[-320, -300], b=-45, hd=-12, g=1, hx=-280, hy=-310, ed=1)
FREE = dict(ankle2=[-190, -90], ft2=20)
ONE = {
    "DOWN": {**st9, **FREE, "ankle": [3.5, -526.7], "ft": -148},
    "UP": {**st9, **FREE, "ankle": [63.3, -568.6], "ft": -100},
    "HALF_BAD": {**st9, **FREE, "ankle": [33, -548], "ft": -124},
    "KNEE_BAD": {**st9, **FREE, "ankle": [-30, -505], "ft": -128},
    "HIP_BAD": {**st9, **FREE, "hip": [-296, -334], "b": -38, "ankle": [-12, -528], "ft": -148},
    "BOTH_BAD": {**st9, "ankle": [3.5, -526.7], "ft": -148, "ankle2": [-36.5, -518.7], "ft2": -148},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-one-leg-calf-press-on-leg-press", "Sled One Leg Calf Press On Leg Press", "GIMNASIO · PIERNAS",
         ["Gemelos", "Pantorrilla", "Unilateral"], rig(610, 0.92),
         [{"type": "legpress", "hip": [-320, -300], "ang": 35, "lean": -45, "stops": 320}],
         ONE, "DOWN",
         ("Gemelos a una pierna en la prensa a 45 grados: apoyá la espalda y la cadera en el respaldo, poné solo "
          "un pie en la plataforma con la rodilla casi extendida y empujá con el metatarso. La otra pierna queda "
          "flexionada colgando al costado. Subí hasta estirar el tobillo y bajá hasta sentir el estiramiento."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
