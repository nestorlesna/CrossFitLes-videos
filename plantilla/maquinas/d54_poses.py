# Dataset D78 Smith Chair Squat: poses + props + rig.
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


# D78 - sentadilla al banco en la Smith: barra sobre los trapecios y el cuerpo baja hasta tocar el banco con la
# cola, sin dejar caer el peso, y sube empujando con los pies enteros.
st78 = dict(ankle=[60, 0], ankle2=[-20, 0], ft=0, ft2=0, g=0, ua=-14, fa=6)
CHAIR = {
    "UP": {**st78, "hip": [10, -462], "b": 6, "hd": 2},
    "DOWN": {**st78, "hip": [-90, -250], "b": 42, "hd": -4},
    "HALF_BAD": {**st78, "hip": [-40, -370], "b": 22, "hd": 0},
    "HEEL_BAD": {**st78, "hip": [-90, -250], "b": 42, "hd": -4, "ft": -32},
    "LEAN_BAD": {**st78, "hip": [-90, -250], "b": 64, "hd": 8},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-chair-squat", "Smith Chair Squat", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteo", "Isquios"], rig(540, 0.85),
         [{"type": "smith", "x": 0, "top": -860, "gap": 300, "stops": -520, "track": "back",
           "torso": [-34, 18], "r": 64, "seat": [-460, -60, -250, -480, -6, 260]}],
         CHAIR, "UP",
         ("Sentadilla al banco en la Smith: la barra va sobre los trapecios y el cuerpo baja controlado hasta "
          "tocar el banco con la cola, sin desplomarse. Las rodillas van blandas y hacia afuera, y la subida sale "
          "empujando con todo el pie y apretando el glúteo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
