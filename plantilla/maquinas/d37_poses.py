# Dataset D61 Lever Shrug: poses + props + rig.
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


# D61 - encogimiento en palanca de barra al piso: de pie, la barra a la altura de la cadera con discos grandes y las
# manos en los mangos. Se encogen los hombros (sh) y la barra gira apenas sobre el poste del bastidor.
st3 = dict(hip=[0, -470], ankle=[70, -4], ankle2=[-60, 0], b=0, hd=0, g=1, g2=1, ed=1, ed2=1, ft=0, sh=0)
LEVSH = {
    "START": {**st3, "hx": 70, "hy": -470, "hx2": 52, "hy2": -466},
    "SHRUG": {**st3, "sh": 24, "hx": 70, "hy": -452, "hx2": 52, "hy2": -449},
    "LEAN_BAD": {**st3, "b": -18, "hd": -4, "hx": 70, "hy": -470, "hx2": 52, "hy2": -466},
    "HALF_BAD": {**st3, "sh": 8, "hx": 70, "hy": -464, "hx2": 52, "hy2": -461},
    "ROUND_BAD": {**st3, "b": 16, "hd": 22, "cv": 24, "hx": 70, "hy": -470, "hx2": 52, "hy2": -466},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-shrug", "Lever Shrug", "GIMNASIO · ESPALDA",
         ["Espalda", "Trapecios", "Espalda alta"], rig(760, 0.78),
         [{"type": "shruglever", "pivot": [300, 6], "barY": -470, "tip": 30,
           "radius": 104, "plateX": 170, "gripX": 70}],
         LEVSH, "START",
         ("Parate de pie con las manos en los mangos de la barra, a la altura de la cadera. Sin doblar los codos, "
          "encogé los hombros hacia las orejas, sostené arriba y bajá lento. La barra acompaña el movimiento "
          "girando apenas sobre su poste."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
