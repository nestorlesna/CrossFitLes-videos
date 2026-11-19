# Dataset D76 Smith Bent Knee Good Morning: poses + props + rig.
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


# D76 - buenos días con rodillas semiflexionadas en la Smith: la barra va sobre los trapecios y el cuerpo hace
# la bisagra de cadera llevando la cola atrás, con las rodillas blandas y la espalda recta.
st76 = dict(ankle=[60, 0], ankle2=[-20, 0], ft=0, ft2=0, g=0, ua=-18, fa=178)
GM = {
    "UP": {**st76, "hip": [10, -462], "b": 6, "hd": 2},
    "DOWN": {**st76, "hip": [-20, -430], "b": 58, "hd": -8},
    "HALF_BAD": {**st76, "hip": [-6, -448], "b": 32, "hd": -3},
    "STIFF_BAD": {**st76, "hip": [-60, -470], "b": 58, "hd": -8},
    "ROUND_BAD": {**st76, "hip": [-20, -430], "b": 62, "hd": 30},
    "DEEP_BAD": {**st76, "hip": [-44, -404], "b": 80, "hd": 2},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-bent-knee-good-morning", "Smith Bent Knee Good Morning", "GIMNASIO · PIERNAS",
         ["Isquios", "Glúteo", "Espalda baja"], rig(540, 0.85),
         [{"type": "smith", "x": 0, "top": -860, "gap": 300, "stops": -560, "track": "back",
           "torso": [-34, 18], "r": 64}],
         GM, "UP",
         ("Buenos días con rodillas semiflexionadas en la Smith: la barra va sobre los trapecios y el cuerpo se "
          "dobla desde la cadera llevando la cola atrás, con las rodillas blandas y la espalda recta. Subí "
          "apretando los isquios sin arquear ni redondear la espalda."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
