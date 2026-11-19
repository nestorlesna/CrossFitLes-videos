# Dataset D54 Lever Reverse T-bar Row: poses + props + rig.
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


# D54 - remo T invertido con pecho apoyado: de pie e inclinado sobre la máquina, el pecho apoyado en la almohadilla,
# los pies firmes y las dos manos en la manija en V. Se tira la manija al abdomen juntando los omóplatos.
rw = dict(hip=[-110, -380], ankle=[60, -6], b=52, hd=18, g=1, g2=1, ed=1, ed2=1, ft=0)
REV = {
    "START": {**rw, "hx": 180, "hy": -320, "hx2": 194, "hy2": -312},
    "PULL": {**rw, "hx": 60, "hy": -400, "ed": 1, "hx2": 74, "hy2": -392, "ed2": 1},
    "LEAN_BAD": {**rw, "hx": 60, "hy": -400, "ed": 1, "hx2": 74, "hy2": -392, "ed2": 1,
                 "b": 30, "hd": 8},
    "SHRUG_BAD": {**rw, "hx": 50, "hy": -505, "hx2": 64, "hy2": -497, "hd": 4},
    "ROUND_BAD": {**rw, "hx": 180, "hy": -320, "hx2": 194, "hy2": -312, "b": 64, "hd": 40, "cv": 26},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-reverse-t-bar-row", "Lever Reverse T-bar Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Bíceps"], rig(840, 0.86),
         [{"type": "tbarrow", "pivot": [-120, 8], "radius": 78, "plateFrac": 0.8,
           "pad": [-240, -500, 350, 46]}],
         REV, "START",
         ("Parate inclinado sobre la máquina con el pecho apoyado en la almohadilla y los pies firmes. "
          "Tomá las manijas con agarre neutro, las palmas enfrentadas. Tirá la manija hacia el abdomen "
          "juntando los omóplatos, hacé una pausa y volvé lento sin despegar el pecho."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
