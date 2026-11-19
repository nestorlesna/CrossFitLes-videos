# Dataset D91 Smith Reverse Calf Raises: poses + props + rig.
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


# D91 - gemelo invertido (tibial anterior) en la Smith: los talones sobre un cajon, las puntas afuera y
# se levantan las puntas de los pies; la barra apoya en la espalda alta (track "back").
st91 = dict(ankle=[55, -54], ankle2=[-25, -54], ft=0, ft2=0, g=0, ua=-16, fa=8)
BASE = {**st91, "hip": [10, -516], "b": 8, "hd": 2}
CALF = {
    "STAND": BASE,
    "UP": {**BASE, "ft": -34},
    "HALF_BAD": {**BASE, "ft": -16},
    "KNEES_BAD": {**BASE, "hip": [10, -486], "b": 10},
    "LEAN_BAD": {**BASE, "hip": [40, -512], "b": 24, "hd": 10},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-reverse-calf-raises", "Smith Reverse Calf Raises", "GIMNASIO · PIERNAS",
         ["Tibial anterior", "Gemelos", "Espinilla"], rig(540, 0.85),
         [{"type": "smith", "x": 70, "top": -1000, "gap": 300, "stops": -520, "track": "back",
           "torso": [-34, 18], "r": 64},
          {"type": "step", "x": 40, "y": 0, "w": 220, "h": 54}],
         CALF, "STAND",
         ("Gemelo invertido en la Smith: con los talones apoyados en un cajón y las puntas afuera, se "
          "levantan las puntas de los pies contra la barra. Trabaja el tibial anterior, la parte de adelante de la "
          "pierna, que casi nunca se entrena y ayuda a estabilizar el tobillo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
