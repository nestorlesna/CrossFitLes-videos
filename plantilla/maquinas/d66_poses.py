# Dataset D90 Smith Rear Delt Row: poses + props + rig.
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


# D90 - remo abierto para deltoide posterior en la Smith: torso mas alto que en D87, agarre ancho, codos
# hacia afuera y la barra al pecho alto; el recorrido es corto y el torso no se mueve.
st90 = dict(ankle=[55, 0], ankle2=[-25, 0], ft=0, ft2=0)
HINGE = {**st90, "hip": [-40, -445], "b": 48, "hd": 6, "g": 1, "hx": 200, "hy": -303}
ROW = {
    "HINGE": HINGE,
    "PULL": {**HINGE, "hy": -515},
    "ROUND_BAD": {**HINGE, "hip": [-55, -425], "b": 54, "hd": 50, "hy": -300},
    "SHRUG_BAD": {**HINGE, "hy": -515, "sh": 28},
    "SWING_BAD": {**HINGE, "hip": [0, -482], "b": 30, "hd": 0, "hy": -520},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-rear-delt-row", "Smith Rear Delt Row", "GIMNASIO · ESPALDA",
         ["Deltoide posterior", "Espalda alta", "Trapecio"], rig(370, 0.85),
         [{"type": "smith", "x": 200, "top": -860, "gap": 300, "stops": -260, "track": "hands",
           "torso": [-34, 18], "r": 60}],
         ROW, "HINGE",
         ("Remo abierto para deltoide posterior en la Smith: el torso queda más alto que en un remo común, el "
          "agarre es ancho y los codos salen hacia afuera. La barra se tira al pecho alto con un recorrido corto, "
          "así trabaja la parte de atrás del hombro y la espalda alta, no el dorsal."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
