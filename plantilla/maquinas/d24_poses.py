# Dataset D48 Lever Alternating Narrow Grip Seated Row: poses + props + rig.
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


# D48 - remo sentado en palanca, agarre estrecho y alternado: el pecho queda apoyado, los pies en la placa y
# cada mano tira de su manija mientras la otra queda extendida.
rw = dict(hip=[-320, -270], ankle=[40, -30], b=-8, hd=-2, g=1, ed=1, ft=0)
RW = {
    "START": {**rw, "hx": -40, "hy": -470, "g2": 1, "hx2": -40, "hy2": -470, "ed2": 1},
    "PULL_N": {**rw, "hx": -225, "hy": -480, "ed": -1, "g2": 1, "hx2": -40, "hy2": -470, "ed2": 1},
    "PULL_F": {**rw, "hx": -40, "hy": -470, "g2": 1, "hx2": -225, "hy2": -480, "ed2": -1},
    "LEAN_BAD": {**rw, "hx": -225, "hy": -480, "ed": -1, "b": -30, "hd": -10,
                 "g2": 1, "hx2": -40, "hy2": -470, "ed2": 1},
    "SHRUG_BAD": {**rw, "hx": -180, "hy": -565, "ed": 1, "hd": 8,
                  "g2": 1, "hx2": -40, "hy2": -470, "ed2": 1},
    "ROUND_BAD": {**rw, "hx": -40, "hy": -470, "b": 16, "hd": 20, "cv": 26,
                  "g2": 1, "hx2": -40, "hy2": -470, "ed2": 1},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-alternating-narrow-grip-seated-row", "Lever Alternating Narrow Grip Seated Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Bíceps"], rig(840, 0.86),
         [{"type": "leverrow", "pivot": [-330, -160], "seat": [-430, -190, -270], "back": [-460, -8, 360],
           "chest": [-280, -548, 288], "foot": [132, 18], "horn": [-500, -180], "radius": 112, "farOff": -16}],
         RW, "START",
         ("Sentate con la espalda recta y el pecho apoyado en la almohadilla, los pies planos en la placa y las "
          "manijas con agarre estrecho. Tirá de una manija hacia el torso mientras la otra queda quieta, apretá los "
          "omóplatos y volvé lento. Alterná los lados."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
