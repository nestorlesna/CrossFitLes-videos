# Dataset D72 Sled Lying Squat: poses + props + rig.
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


# D72 - sentadilla en el sled tumbado: misma máquina que D71 pero acá las rodillas se doblan y extienden
# empujando la plataforma lejos, con la planta completa y la cadera pegada al banco.
st72 = dict(hip=[-300, -198], b=-90, hd=-90, g=1, hx=-400, hy=-186, ed=1)
SQT = {
    "BENT": {**st72, "ankle": [0, -124], "ankle2": [-24, -130], "ft": -90, "ft2": -86},
    "EXT": {**st72, "ankle": [160, -172], "ankle2": [136, -178], "ft": -88, "ft2": -84},
    "HALF_BAD": {**st72, "ankle": [86, -150], "ankle2": [62, -156], "ft": -89, "ft2": -85},
    "HIP_BAD": {**st72, "hip": [-300, -232], "b": -80, "ankle": [40, -140], "ankle2": [16, -146],
                "ft": -90, "ft2": -86},
    "HEEL_BAD": {**st72, "ankle": [86, -150], "ankle2": [62, -156], "ft": -58, "ft2": -54},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-lying-squat", "Sled Lying Squat", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteo", "Piernas"], rig(700, 0.92),
         [{"type": "legpresslie", "bench": [-660, -195, -150], "ankle": [0, -124], "cx": 230, "stops": -290}],
         SQT, "BENT",
         ("Sentadilla en el sled tumbado: acostate en el banco con la planta completa en la plataforma y las "
          "rodillas dobladas. Empujá la plataforma extendiendo las piernas sin despegar la cadera y volvé "
          "controlando hasta la posición inicial."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
