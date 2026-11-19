# Dataset D80 Smith Front Squat Clean Grip: poses + props + rig.
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


# D80 - sentadilla frontal en la Smith con agarre de cargada: la barra va delante de los hombros, los codos
# altos y el pecho arriba mientras el cuerpo baja y sube en la vertical.
st80 = dict(ankle=[60, 0], ankle2=[-20, 0], ft=0, ft2=0, g=0, ua=70, fa=-140)
FRONT = {
    "UP": {**st80, "hip": [10, -462], "b": 8, "hd": 0},
    "DOWN": {**st80, "hip": [-55, -262], "b": 34, "hd": -2},
    "HALF_BAD": {**st80, "hip": [-15, -368], "b": 20, "hd": 0},
    "LEAN_BAD": {**st80, "hip": [-55, -262], "b": 58, "hd": 8},
    "HEEL_BAD": {**st80, "hip": [-55, -262], "b": 34, "hd": -2, "ft": -32},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-front-squat-clean-grip", "Smith Front Squat Clean Grip", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteo", "Espalda alta"], rig(540, 0.85),
         [{"type": "smith", "x": 90, "top": -860, "gap": 300, "stops": -520, "track": "hands",
           "torso": [-34, 18], "r": 58}],
         FRONT, "UP",
         ("Sentadilla frontal en la Smith con agarre de cargada: la barra va delante de los hombros, los codos "
          "bien altos y el pecho arriba. Bajás y subís en la vertical, con el torso lo más derecho posible y "
          "las rodillas blandas. Si los codos caen, la barra se va adelante y la espalda se lleva la carga."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
