# Dataset D62 Hack Calf Raise: poses + props + rig.
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


# D62 - gemelos en la sentadilla hack: el carro reclinado lleva el cuerpo; con las rodillas trabadas se empuja con
# los tobillos (ft) y el carro sube por el riel. Misma máquina que la sentadilla hack (mismo prop y misma geometría).
st4 = dict(hip=[-297.8, -394.7], ankle=[2, -46], b=-36, hd=-6, g=0, ua=16, fa=118, ft=-14, sh=0)
HACK = {
    "START": {**st4, "ft": -14, "ankle": [2, -46]},
    "RAISE": {"hip": [-317.7, -422.1], "ankle": [8, -86], "b": -36, "hd": -6, "g": 0, "ua": 16, "fa": 118,
              "ft": 26, "sh": 0},
    "KNEE_BAD": {"hip": [-252.0, -352.0], "ankle": [2, -46], "b": -36, "hd": -6, "g": 0, "ua": 16, "fa": 118,
                 "ft": -14, "sh": 0},
    "HALF_BAD": {"hip": [-307.8, -408.5], "ankle": [5, -68], "b": -36, "hd": -6, "g": 0, "ua": 16, "fa": 118,
                 "ft": 4, "sh": 0},
    "ARCH_BAD": {"hip": [-297.8, -394.7], "ankle": [2, -46], "b": -26, "hd": 6, "cv": 20, "g": 0, "ua": 16,
                 "fa": 118, "ft": -14, "sh": 0},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("hack-calf-raise", "Hack Calf Raise", "GIMNASIO · PIERNAS",
         ["Gemelos", "Sóleo"], rig(800, 0.95),
         [{"type": "hacksquat", "hip": [-297.8, -394.7], "lean": -36, "foot": [2, -46], "plat": -14,
           "len": 300, "rail": [-470, 620], "stops": -330, "hand": [140.6, -99.6]}],
         HACK, "START",
         ("En la sentadilla hack, apoyá la punta de los pies en la plataforma y dejá caer los talones. Con las "
          "rodillas trabadas, empujá con los tobillos para subir el carro, hacé una pausa arriba y bajá lento "
          "hasta sentir el estiramiento de los gemelos."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
