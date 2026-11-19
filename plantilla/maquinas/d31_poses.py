# Dataset D55 Lever Seated Row: poses + props + rig.
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


# D55 - remo sentado en palanca: sentado, el pecho apoyado en la almohadilla y los pies en la placa. Las dos manijas
# salen al frente a la altura del pecho con agarre prono y se tiran al torso juntando los omóplatos.
rw = dict(hip=[-330, -280], ankle=[30, -20], b=-4, hd=-2, g=1, g2=1, ed=-1, ed2=-1, ft=0)
SEAT = {
    "START": {**rw, "hx": -40, "hy": -460, "hx2": -54, "hy2": -452},
    "PULL": {**rw, "hx": -215, "hy": -478, "hx2": -229, "hy2": -470},
    "LEAN_BAD": {**rw, "hx": -215, "hy": -478, "hx2": -229, "hy2": -470,
                 "b": -26, "hd": -10},
    "SHRUG_BAD": {**rw, "hx": -200, "hy": -510, "hx2": -214, "hy2": -502, "hd": 7},
    "ROUND_BAD": {**rw, "hx": -40, "hy": -460, "hx2": -54, "hy2": -452, "b": 15, "hd": 20, "cv": 26},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-seated-row", "Lever Seated Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Bíceps"], rig(840, 0.86),
         [{"type": "leverrow", "pivot": [-420, -430], "seat": [-430, -190, -280], "back": [-460, -6, 360],
           "chest": [-276, -556, 288], "foot": [110, 12], "horn": [-540, -180], "radius": 112, "farOff": -16}],
         SEAT, "START",
         ("Sentate con el pecho apoyado en la almohadilla y los pies planos en la placa. Tomá las dos manijas "
          "con agarre prono, las manos a la altura de los hombros. Tirá las manijas hacia el torso juntando "
          "los omóplatos, hacé una pausa y volvé lento sin despegar el pecho."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
