# Dataset D92 Smith Reverse Grip Bent Over Row: poses + props + rig.
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


# D92 - remo inclinado con agarre supino (palmas arriba) en la Smith: torso casi horizontal, codos pegados
# y la barra al abdomen bajo; el agarre supino suma biceps y espalda alta.
st92 = dict(ankle=[55, 0], ankle2=[-25, 0], ft=0, ft2=0)
HINGE = {**st92, "hip": [-50, -430], "b": 60, "hd": 0, "g": 1, "hx": 200, "hy": -255}
ROW = {
    "HINGE": HINGE,
    "PULL": {**HINGE, "hy": -460},
    "ROUND_BAD": {**HINGE, "hip": [-70, -400], "b": 68, "hd": 62, "hy": -280},
    "SWING_BAD": {**HINGE, "hip": [-10, -470], "b": 38, "hd": 4, "hy": -470},
    "SHORT_BAD": {**HINGE, "hy": -370},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-reverse-grip-bent-over-row", "Smith Reverse Grip Bent Over Row", "GIMNASIO · ESPALDA",
         ["Dorsales", "Bíceps", "Espalda alta"], rig(370, 0.85),
         [{"type": "smith", "x": 200, "top": -860, "gap": 300, "stops": -260, "track": "hands",
           "torso": [-34, 18], "r": 60}],
         ROW, "HINGE",
         ("Remo inclinado con agarre supino en la Smith: las palmas miran hacia arriba y la barra se tira al "
          "abdomen bajo con los codos pegados al cuerpo. El agarre supino mete más bíceps y espalda alta, y el "
          "torso casi horizontal hace que el dorsal trabaje de punta a punta."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
