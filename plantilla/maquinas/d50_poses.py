# Dataset D74 Smith Back Shrug: poses + props + rig.
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


# D74 - encogimientos de hombros con la barra guiada detrás de la espalda: el atleta queda parado dentro de la
# Smith, la barra a la altura de la cadera en las manos y solo suben los hombros (sh), sin doblar los codos.
st74 = dict(hip=[10, -462], ankle=[60, 0], ankle2=[-20, 0], ft=0, ft2=0, b=4, hd=2, g=1, ed=1)
SHR = {
    "DOWN": {**st74, "sh": 0, "hx": -60, "hy": -440},
    "UP": {**st74, "sh": 28, "hx": -60, "hy": -468},
    "HALF_BAD": {**st74, "sh": 13, "hx": -60, "hy": -453},
    "ARMS_BAD": {**st74, "sh": 3, "hx": -70, "hy": -545},
    "LEAN_BAD": {**st74, "b": 20, "hd": 16, "sh": 6, "hx": -10, "hy": -430},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-back-shrug", "Smith Back Shrug", "GIMNASIO · HOMBROS",
         ["Trapecio", "Hombros"], rig(540, 0.80),
         [{"type": "smith", "x": 0, "top": -1000, "gap": 300, "stops": -560, "track": "hands", "r": 70}],
         SHR, "DOWN",
         ("Encogimientos de hombros con la barra detrás de la espalda en la Smith: quedate parado, agarrá la barra "
          "a la altura de la cadera y subí los hombros hacia las orejas sin doblar los codos. Bajá controlando "
          "hasta estirar el trapecio."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
