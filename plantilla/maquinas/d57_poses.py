# Dataset D81 Smith Full Squat: poses + props + rig.
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


# D81 - sentadilla completa en la Smith: barra alta sobre los trapecios, bajada hasta el fondo con los talones
# apoyados y el torso lo más derecho posible, y subida empujando con los pies.
st81 = dict(ankle=[60, 0], ankle2=[20, 0], ft=0, ft2=0, g=0, ua=-16, fa=8)
FULL = {
    "UP": {**st81, "hip": [10, -462], "b": 8, "hd": 2},
    "DOWN": {**st81, "hip": [-55, -215], "b": 36, "hd": -4},
    "HALF_BAD": {**st81, "hip": [0, -350], "b": 18, "hd": 0},
    "HEEL_BAD": {**st81, "hip": [-55, -215], "b": 36, "hd": -4, "ft": -34},
    "LEAN_BAD": {**st81, "hip": [-55, -215], "b": 60, "hd": 10},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-full-squat", "Smith Full Squat", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteo", "Isquios"], rig(540, 0.85),
         [{"type": "smith", "x": 0, "top": -860, "gap": 300, "stops": -520, "track": "back",
           "torso": [-34, 18], "r": 64}],
         FULL, "UP",
         ("Sentadilla completa en la Smith: la barra va alta sobre los trapecios y el cuerpo baja hasta el fondo "
          "con los talones apoyados, las rodillas hacia afuera y el torso lo más derecho posible. Subís empujando "
          "el piso con todo el pie. El recorrido completo es el que más trabaja cuádriceps y glúteo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
