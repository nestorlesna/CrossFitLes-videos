# Dataset D86 Smith Machine Bicep Curl: poses + props + rig.
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


# D86 - curl de bíceps en la Smith: de pie frente a la barra baja, agarre supino y la barra sube desde el muslo
# hasta el pecho sin mover los codos ni el torso.
st86 = dict(ankle=[60, 0], ankle2=[20, 0], ft=0, ft2=0, g=1, hx=-45, ed=1)
CURL = {
    "DOWN": {**st86, "hip": [10, -462], "b": 8, "hd": 2, "hy": -424},
    "UP": {**st86, "hip": [10, -462], "b": 8, "hd": 2, "hx": -120, "hy": -640},
    "HALF_BAD": {**st86, "hip": [10, -462], "b": 8, "hd": 2, "hx": -95, "hy": -540},
    "SWING_BAD": {**st86, "hip": [10, -462], "b": 26, "hd": 8, "hx": -120, "hy": -640},
    "ELBOW_BAD": {**st86, "hip": [10, -462], "b": 8, "hd": 2, "hx": -200, "hy": -560},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-machine-bicep-curl", "Smith Machine Bicep Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Antebrazo"], rig(540, 0.85),
         [{"type": "smith", "x": -75, "top": -860, "gap": 300, "stops": -330, "track": "hands",
           "torso": [-34, 18], "r": 56}],
         CURL, "DOWN",
         ("Curl de bíceps en la Smith: de pie frente a la barra baja, con agarre supino, la barra sube desde el "
          "muslo hasta el pecho sin mover los codos ni el torso. La barra guiada te obliga a un recorrido recto "
          "y parejo, ideal para aislar el bíceps sin balanceo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
