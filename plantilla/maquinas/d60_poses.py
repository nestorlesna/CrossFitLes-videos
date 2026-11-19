# Dataset D84 Smith Leg Press: poses + props + rig.
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


# D84 - prensa de piernas en la Smith: supino en el piso, la barra apoyada en las plantas de los pies y las piernas
# empujando en vertical por el carril. La cadera y los hombros quedan apoyados; el recorrido va de la rodilla al pecho
# (BENT) a la pierna casi estirada (EXT). track "feet": la barra sigue al tobillo (ver runtime).
st84 = dict(ankle=[230, -440], ankle2=[215, -424], ft=-64, ft2=-64, g=0, ua=86, fa=4)
PRESS = {
    "EXT": {**st84, "hip": [0, -40], "b": -92, "hd": -88},
    "BENT": {**st84, "hip": [0, -40], "b": -92, "hd": -88, "ankle": [190, -235], "ankle2": [175, -219]},
    "HALF_BAD": {**st84, "hip": [0, -40], "b": -92, "hd": -88, "ankle": [220, -350], "ankle2": [205, -334]},
    "TOES_BAD": {**st84, "hip": [0, -40], "b": -92, "hd": -88, "ft": 30, "ft2": 30},
    "HIP_BAD": {**st84, "hip": [0, -96], "b": -104, "hd": -80},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-leg-press", "Smith Leg Press", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteo", "Isquios"], rig(530, 0.85),
         [{"type": "smith", "x": 200, "top": -860, "gap": 300, "stops": -250, "track": "feet",
           "foot": 44, "torso": [-34, 18], "r": 64}],
         PRESS, "BENT",
         ("Prensa de piernas en la Smith: te acostás supino en el piso con la barra apoyada en las plantas de los "
          "pies y empujás en vertical por el carril. La cadera y los hombros no se despegan del piso. Es una "
          "prensa horizontal: cuádriceps y glúteo con la espalda baja protegida por el piso."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
