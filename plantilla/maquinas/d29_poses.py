# Dataset D53 Lever Reverse Grip Vertical Row: poses + props + rig.
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


# D53 - remo vertical con agarre supino: sentado con el pecho apoyado, las dos manijas verticales se toman con
# las palmas hacia arriba y se tiran hasta el torso con los codos cerca del cuerpo.
rw = dict(hip=[-320, -270], ankle=[40, -30], b=-6, hd=-2, g=1, g2=1, ed=1, ed2=1, ft=0)
REV = {
    "START": {**rw, "hx": -55, "hy": -455, "hx2": -69, "hy2": -447},
    "PULL": {**rw, "hx": -215, "hy": -478, "ed": -1, "hx2": -229, "hy2": -470, "ed2": -1},
    "LEAN_BAD": {**rw, "hx": -215, "hy": -478, "ed": -1, "hx2": -229, "hy2": -470, "ed2": -1,
                 "b": -30, "hd": -10},
    "SHRUG_BAD": {**rw, "hx": -185, "hy": -560, "ed": 1, "hx2": -199, "hy2": -552, "ed2": 1, "hd": 8},
    "ROUND_BAD": {**rw, "hx": -55, "hy": -455, "hx2": -69, "hy2": -447, "b": 16, "hd": 20, "cv": 26},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-reverse-grip-vertical-row", "Lever Reverse Grip Vertical Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Bíceps"], rig(840, 0.86),
         [{"type": "leverrow", "pivot": [-380, -430], "seat": [-430, -190, -270], "back": [-460, -8, 360],
           "chest": [-280, -548, 288], "foot": [132, 18], "horn": [-500, -180], "radius": 112, "farOff": -16}],
         REV, "START",
         ("Sentate con el pecho apoyado en la almohadilla y los pies planos en la placa. Tomá las dos manijas "
          "verticales con agarre supino, las palmas hacia arriba. Tirá las manijas hacia el torso con los codos "
          "cerca del cuerpo, juntá los omóplatos, hacé una pausa y volvé lento sin despegar el pecho."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
