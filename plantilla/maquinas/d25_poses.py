# Dataset D49 Lever Bent-over Row with V-Bar: poses + props + rig.
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


tb = dict(hip=[-80, -430], ankle=[0, 0], b=62, hd=0, g=1, ed=1, ft=0)
TB = {
    "HINGE": {**tb, "hx": 150, "hy": -300},
    "PULL": {**tb, "hx": 80, "hy": -420, "ed": -1},
    "ROUND_BAD": {**tb, "hx": 150, "hy": -300, "b": 66, "hd": 24, "cv": 30},
    "SHRUG_BAD": {**tb, "hx": 90, "hy": -390, "hd": 8, "ed": 1},
    "JERK_BAD": {**tb, "hip": [-80, -500], "ankle": [0, 0], "b": 45, "hx": 80, "hy": -420, "ed": -1},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-bent-over-row-with-v-bar", "Lever Bent-over Row with V-Bar", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Bíceps"], rig(700, 0.9),
         [{"type": "tbarrow", "pivot": [-420, 8], "radius": 88, "plateFrac": 0.84}],
         TB, "HINGE",
         ("Parate con los pies al ancho de los hombros y las rodillas apenas flexionadas. Tomá la barra en V con "
          "agarre prono, incliná el torso desde la cadera con la espalda recta y tirá del agarre hacia el abdomen. "
          "Apretá los omóplatos, hacé una pausa y volvé lento sin redondear la espalda."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
