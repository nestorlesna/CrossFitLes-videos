# Dataset D87 Smith Narrow Row: poses + props + rig.
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


# D87 - remo estrecho en la Smith: mismo remo inclinado pero con las manos juntas, el torso un poco más alto y
# los codos pegados al cuerpo; la barra sube al esternón, no al abdomen bajo.
st87 = dict(ankle=[55, 0], ankle2=[-25, 0], ft=0, ft2=0)
HINGE = {**st87, "hip": [-40, -445], "b": 50, "hd": 8, "g": 1, "hx": 200, "hy": -295}
ROW = {
    "HINGE": HINGE,
    "PULL": {**HINGE, "hy": -500},
    "ROUND_BAD": {**HINGE, "hip": [-60, -420], "b": 58, "hd": 56, "hy": -300},
    "SWING_BAD": {**HINGE, "hip": [0, -478], "b": 32, "hd": 0, "hy": -505},
    "SHORT_BAD": {**HINGE, "hy": -380},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-narrow-row", "Smith Narrow Row", "GIMNASIO · ESPALDA",
         ["Espalda alta", "Dorsales", "Bíceps"], rig(370, 0.85),
         [{"type": "smith", "x": 200, "top": -860, "gap": 300, "stops": -260, "track": "hands",
           "torso": [-34, 18], "r": 60}],
         ROW, "HINGE",
         ("Remo estrecho en la Smith: la barra guiada se agarra con las manos juntas y se tira al esternón con los "
          "codos pegados al cuerpo. El torso queda más alto que en el remo abierto y no se mueve: el recorrido "
          "corto y pegado trabaja la espalda alta y el dorsal con menos ayuda de los hombros."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
