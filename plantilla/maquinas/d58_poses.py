# Dataset D82 Smith Hack Squat: poses + props + rig.
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


# D82 - hack squat en la Smith: la barra va DETRÁS de las piernas y los brazos cuelgan hacia atrás sujetándola.
# El cuerpo se recuesta en la barra y baja con el torso casi vertical, rodillas viajando adelante.
# La cadera trabaja en el rango completo, con los talones apoyados.
st82 = dict(ankle=[60, 0], ankle2=[20, 0], ft=0, ft2=0, g=1, hx=70, ed=-1)
HACK = {
    "UP": {**st82, "hip": [0, -462], "b": -4, "hd": -2, "hy": -427},
    "DOWN": {**st82, "hip": [-50, -235], "b": -6, "hd": -4, "hy": -285},
    "HALF_BAD": {**st82, "hip": [-20, -360], "b": -4, "hd": -2, "hy": -362},
    "LEAN_BAD": {**st82, "hip": [-50, -235], "b": 26, "hd": 14, "hy": -300},
    "HEELS_BAD": {**st82, "hip": [-50, -235], "b": -6, "hd": -4, "hy": -285, "ft": -34},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-hack-squat", "Smith Hack Squat", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteo", "Aductor"], rig(540, 0.85),
         [{"type": "smith", "x": 70, "top": -860, "gap": 300, "stops": -300, "track": "hands",
           "torso": [-34, 18], "r": 64}],
         HACK, "UP",
         ("Hack squat en la Smith: la barra va detrás de las piernas, el cuerpo se recuesta en ella y bajás con "
          "el torso casi vertical llevando las rodillas adelante. Los talones quedan apoyados y la espalda viaja "
          "pegada a la barra. El recorrido completo carga cuádriceps con el torso más vertical que en la "
          "sentadilla normal."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
