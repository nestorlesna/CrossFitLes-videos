# Dataset D93 Smith Reverse Grip Press: poses + props + rig.
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


# D93 - press de banca con agarre supino en la Smith: acostado, palmas hacia la cara, la barra baja al pecho
# bajo y sube con los codos cerca del torso. Mismo bench + rig que smith-machine-bench-press (M24).
st93 = dict(hip=[-20, -196], ankle=[230, 0], b=-90, hd=-92, ft=0, g=1, hx=-200, ed=1)
PRESS = {
    "TOP": {**st93, "hy": -508},
    "MID": {**st93, "hy": -390},
    "BOTTOM": {**st93, "hy": -270},
    "NECK_BAD": {**st93, "hip": [70, -196], "ankle": [320, 0], "hy": -292},
    "BUTT_BAD": {**st93, "hip": [-20, -262], "b": -104, "hd": -100, "hy": -320, "cv": -20},
    "SHORT_BAD": {**st93, "hy": -380},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-reverse-grip-press", "Smith Reverse Grip Press", "GIMNASIO · PECHO",
         ["Pectorales", "Tríceps", "Espalda alta"], rig(600, 0.7),
         [{"type": "bench", "x0": -560, "x1": 120, "h": 200},
          {"type": "smith", "x": -200, "top": -1180, "stops": -300, "track": "hands", "r": 70}],
         PRESS, "TOP",
         ("Press de banca con agarre supino en la Smith: acostado, las palmas miran hacia la cara y la barra baja "
          "al pecho bajo con los codos cerca del torso. El agarre supino cambia el ángulo de empuje, suma "
          "tríceps y espalda alta y obliga a bajar el peso para controlar la barra."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
