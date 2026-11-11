# Dataset D01 · D27 Assisted Chest Dip (Kneeling) y D28 Assisted Triceps Dip (Kneeling): poses + props + rig.
import sys, os, json, math
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


PROP = [{"type": "assisted", "stack": 420, "grip": [60, -1240], "dip": [60, -760],
         "pivot": [300, -260], "rest": -567, "pin": 6, "k": 1}]
cm = dict(s=92, t=4, ft=80, g=1, hx=60, hy=-750, ed=-1)

# ── D27 ── fondos de pecho asistidos: tronco inclinado adelante, codos algo abiertos ──
chest = {
    "TOP": {**cm, "hip": [-18.6, -806.3], "b": 20, "hd": 16},
    "MID": {**cm, "hip": [-40.0, -720.0], "b": 23, "hd": 20},
    "BOTTOM": {**cm, "hip": [-58.0, -652.0], "b": 26, "hd": 24},
    "UPRIGHT_BAD": {**cm, "hip": [-40.0, -720.0], "b": 2, "hd": 4},
    "SHRUG_BAD": {**cm, "hip": [-58.0, -652.0], "b": 26, "hd": 24, "cv": 26},
}

# ── D28 ── fondos de tríceps asistidos: tronco más derecho y recorrido más corto ──
triceps = {
    "TOP": {**cm, "hip": [-18.6, -800.0], "b": 8, "hd": 8},
    "MID": {**cm, "hip": [-40.0, -736.0], "b": 10, "hd": 10},
    "BOTTOM": {**cm, "hip": [-56.0, -676.0], "b": 12, "hd": 12},
    "FORWARD_BAD": {**cm, "hip": [-40.0, -736.0], "b": 34, "hd": 30},
    "SHRUG_BAD": {**cm, "hip": [-56.0, -676.0], "b": 12, "hd": 12, "cv": 26},
}

for clave, nombre, category, tags, poses, initial, descripcion in [
        ("assisted-chest-dip-kneeling", "Assisted Chest Dip (Kneeling)", "GIMNASIO · PECHO",
         ["Pecho", "Tríceps"], chest, "TOP",
         ("Apoyá las rodillas en la plataforma y agarrá las paralelas con las palmas hacia abajo. "
          "Con el pecho adelante, bajá doblando los codos hasta que los brazos queden paralelos al piso "
          "y empujá para volver arriba sin encoger los hombros.")),
        ("assisted-triceps-dip-kneeling", "Assisted Triceps Dip (Kneeling)", "GIMNASIO · BRAZOS",
         ["Tríceps", "Pecho"], triceps, "TOP",
         ("Apoyá las rodillas en la plataforma y agarrá las paralelas. Con el tronco casi derecho, "
          "bajá doblando los codos con los brazos pegados al cuerpo y empujá hasta estirar sin trabar. "
          "El contrapeso te ayuda a completar las repeticiones."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig(560, 0.58), PROP, poses, initial, descripcion)
