# Dataset D88 Smith One Arm Row: poses + props + rig.
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


# D88 - remo a una mano en la Smith: pies escalonados, bisagra de cadera, la mano libre cuelga y el brazo que
# trabaja tira la barra hacia la cadera sin girar el torso.
st88 = dict(ankle=[85, 0], ankle2=[-40, 0], ft=0, ft2=0, g2=0, ua2=12, fa2=30)
HINGE = {**st88, "hip": [-45, -440], "b": 58, "hd": 12, "g": 1, "hx": 200, "hy": -300}
ROW = {
    "HINGE": HINGE,
    "PULL": {**HINGE, "hy": -465},
    "ROUND_BAD": {**HINGE, "hip": [-65, -415], "b": 66, "hd": 60, "hy": -315},
    "SWING_BAD": {**HINGE, "hip": [-5, -470], "b": 36, "hd": 4, "hy": -470},
    "SHORT_BAD": {**HINGE, "hy": -385},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-one-arm-row", "Smith One Arm Row", "GIMNASIO · ESPALDA",
         ["Dorsal", "Espalda alta", "Bíceps"], rig(370, 0.85),
         [{"type": "smith", "x": 200, "top": -860, "gap": 300, "stops": -250, "track": "hands",
           "torso": [-34, 18], "r": 60}],
         ROW, "HINGE",
         ("Remo a una mano en la Smith: con los pies escalonados y el torso inclinado, una sola mano tira de la "
          "barra hacia la cadera mientras la otra cuelga libre. Al ser un brazo por vez, el recorrido es más largo "
          "y el dorsal trabaja sin que el torso gire ni se enderece."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
