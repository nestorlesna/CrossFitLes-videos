# Dataset D89 Smith One Leg Floor Calf Raise: poses + props + rig.
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


# D89 - gemelo a una pierna en el piso: barra en la espalda, una pierna trabaja sobre la punta del pie y la otra
# queda flexionada detrás. Se sube el talón lo más alto posible y se baja lento hasta el estiramiento.
st89 = dict(ankle=[60, 0], ft=0, ankle2=[130, -280], ft2=30, g=0, ua=-16, fa=8)
CALF = {
    "STAND": {**st89, "hip": [10, -462], "b": 8, "hd": 2, "hy": -726, "hy2": -726},
    "UP": {**st89, "hip": [10, -506], "ankle": [60, -44], "ft": 32, "ankle2": [130, -324],
           "b": 8, "hd": 2, "hy": -770, "hy2": -770},
    "HALF_BAD": {**st89, "hip": [10, -484], "ankle": [60, -22], "ft": 16, "ankle2": [130, -302],
                 "b": 8, "hd": 4, "hy": -748, "hy2": -748},
    "KNEES_BAD": {**st89, "hip": [10, -420], "b": 8, "hd": 4, "hy": -684, "hy2": -684},
    "LEAN_BAD": {**st89, "hip": [10, -462], "b": 24, "hd": 8, "hy": -715, "hy2": -715},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-one-leg-floor-calf-raise", "Smith One Leg Floor Calf Raise", "GIMNASIO · PIERNAS",
         ["Gemelos", "Sóleo", "Tobillo"], rig(540, 0.85),
         [{"type": "smith", "x": 70, "top": -900, "gap": 300, "stops": -520, "track": "back",
           "torso": [-34, 18], "r": 64}],
         CALF, "STAND",
         ("Gemelo a una pierna en la Smith, desde el piso: la barra apoya en la espalda, una pierna queda "
          "flexionada detrás y la otra sube el talón lo más alto posible. Se sostiene arriba y se baja lento "
          "hasta sentir el estiramiento del gemelo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
