# Dataset D71 Sled Lying Calf Press: poses + props + rig.
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


# D71 - gemelos en el sled tumbado: el banco queda horizontal, las rodillas casi extendidas y la plataforma
# vertical se lleva con el metatarso; solo el tobillo hace el recorrido (talón abajo ↔ punta adelante).
st11 = dict(hip=[-300, -198], b=-90, hd=-90, g=1, hx=-400, hy=-186, ed=1)
CSO = {
    "DOWN": {**st11, "ankle": [95, -186], "ankle2": [67, -192], "ft": -106, "ft2": -106},
    "UP": {**st11, "ankle": [107, -200], "ankle2": [79, -206], "ft": -72, "ft2": -72},
    "HALF_BAD": {**st11, "ankle": [101, -193], "ankle2": [73, -199], "ft": -89, "ft2": -89},
    "KNEE_BAD": {**st11, "ankle": [40, -150], "ankle2": [12, -156], "ft": -104, "ft2": -104},
    "HIP_BAD": {**st11, "hip": [-300, -228], "b": -80, "ankle": [95, -186], "ankle2": [67, -192],
                "ft": -106, "ft2": -106},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-lying-calf-press", "Sled Lying Calf Press", "GIMNASIO · PIERNAS",
         ["Gemelos", "Pantorrilla"], rig(700, 0.92),
         [{"type": "legpresslie", "bench": [-660, -195, -150], "ankle": [95, -186], "cx": 230, "stops": -290}],
         CSO, "DOWN",
         ("Gemelos en el sled tumbado: acostate en el banco con las rodillas casi extendidas y la planta de los pies "
          "en la plataforma. Empujá la plataforma con el metatarso moviendo solo los tobillos y volvé hasta sentir "
          "el estiramiento."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
