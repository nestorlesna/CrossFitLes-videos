# Dataset D85 Smith Low Bar Squat: poses + props + rig.
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


# D85 - sentadilla con barra baja en la Smith: la barra apoya más abajo, sobre los deltoides posteriores
# (torso [-20,52] en el prop en vez de [-34,18]) y el torso se inclina un poco más, con la cadera viajando atrás.
st85 = dict(ankle=[60, 0], ankle2=[20, 0], ft=0, ft2=0, g=0, ua=-20, fa=10)
LOW = {
    "UP": {**st85, "hip": [10, -462], "b": 12, "hd": 2},
    "DOWN": {**st85, "hip": [-65, -240], "b": 40, "hd": 0},
    "HALF_BAD": {**st85, "hip": [-5, -350], "b": 20, "hd": 0},
    "LEAN_BAD": {**st85, "hip": [-65, -240], "b": 62, "hd": 12},
    "HEEL_BAD": {**st85, "hip": [-65, -240], "b": 40, "hd": 0, "ft": -34},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-low-bar-squat", "Smith Low Bar Squat", "GIMNASIO · PIERNAS",
         ["Glúteo", "Isquios", "Cuádriceps"], rig(540, 0.85),
         [{"type": "smith", "x": 0, "top": -860, "gap": 300, "stops": -520, "track": "back",
           "torso": [-20, 52], "r": 64}],
         LOW, "UP",
         ("Sentadilla con barra baja en la Smith: la barra apoya más abajo, sobre los deltoides posteriores, y "
          "el torso se inclina un poco más que en la sentadilla alta. La cadera viaja atrás y el recorrido llega "
          "hasta pasar la paralela con los talones apoyados. Más glúteo e isquios."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
