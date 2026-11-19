# Dataset D59 Lever Gripless Shrug: poses + props + rig.
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


# D59 - encogimiento sin agarre: de pie bajo el yugo (de cara a la máquina), la almohadilla apoyada en los trapecios y
# las manos en las manijas fijas delante del pecho. Se encogen los hombros empujando la almohadilla hacia arriba (sh),
# sin doblar los codos ni inclinar el tronco.
st = dict(hip=[0, -470], ankle=[70, -4], ankle2=[-60, 0], b=0, hd=0, g=1, g2=1, ed=-1, ed2=-1, ft=0, sh=0)
SHRUG = {
    "START": {**st, "hx": 210, "hy": -700, "hx2": 214, "hy2": -696},
    "SHRUG": {**st, "sh": 26, "hx": 210, "hy": -700, "hx2": 214, "hy2": -696},
    "LEAN_BAD": {**st, "b": -18, "hd": -6, "hx": 210, "hy": -700, "hx2": 214, "hy2": -696},
    "HALF_BAD": {**st, "sh": 8, "hd": 8, "hx": 210, "hy": -700, "hx2": 214, "hy2": -696},
    "ROUND_BAD": {**st, "b": 14, "hd": 20, "cv": 24, "hx": 210, "hy": -700, "hx2": 214, "hy2": -696},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-gripless-shrug", "Lever Gripless Shrug", "GIMNASIO · ESPALDA",
         ["Espalda", "Trapecios", "Espalda alta"], rig(600, 0.78),
         [{"type": "levershrug", "column": 330, "top": -1000, "stack": 450, "padX": -60,
           "grip": [210, -700], "pin": 6, "k": 5, "padOff": -15}],
         SHRUG, "START",
         ("Parate bajo el yugo con la almohadilla apoyada en los trapecios y las manos en las manijas, delante "
          "del pecho. Sin doblar los codos, empujá la almohadilla hacia arriba con los hombros, hacé una pausa "
          "arriba y bajá lento hasta sentir el estiramiento."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)