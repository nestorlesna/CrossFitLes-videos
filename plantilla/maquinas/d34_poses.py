# Dataset D58 Lever Unilateral Row: poses + props + rig.
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


# D58 - remo unilateral en palanca: sentado con el pecho apoyado, una sola mano tira la manija al costado del
# torso con el codo atrás, mientras la otra queda apoyada en la cadera (la manija lejana la sigue y queda quieta).
rw = dict(hip=[-330, -270], ankle=[35, -28], b=-4, hd=-2, g=1, g2=1, ed=1, ed2=1, ft=0)
UNI = {
    "START": {**rw, "hx": -45, "hy": -455, "hx2": -370, "hy2": -300},
    "PULL": {**rw, "hx": -225, "hy": -500, "ed": -1, "hx2": -370, "hy2": -300},
    "LEAN_BAD": {**rw, "hx": -225, "hy": -500, "ed": -1, "hx2": -370, "hy2": -300,
                 "b": -30, "hd": -10},
    "SHRUG_BAD": {**rw, "hx": -180, "hy": -545, "ed": -1, "hx2": -370, "hy2": -300, "hd": 10},
    "ROUND_BAD": {**rw, "hx": -45, "hy": -455, "hx2": -370, "hy2": -300, "b": 14, "hd": 20, "cv": 26,
                  "ed": -1},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-unilateral-row", "Lever Unilateral Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Dorsales", "Bíceps"], rig(820, 0.87),
         [{"type": "leverrow", "pivot": [-400, -430], "seat": [-430, -190, -280], "back": [-460, -6, 360],
           "chest": [-290, -556, 288], "foot": [120, 12], "horn": [-520, -180], "radius": 112, "farOff": -10}],
         UNI, "START",
         ("Sentate con el pecho apoyado en la almohadilla y los pies en la placa. Tomá una sola manija con "
          "agarre prono y dejá la otra mano apoyada en la cadera. Tirá la manija al costado del torso con el "
          "codo hacia atrás, juntá el omóplato y volvé lento sin rotar el tronco. Cambiá de brazo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
