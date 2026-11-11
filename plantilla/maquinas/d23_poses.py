# Dataset D45 Lever Pullover y D46 Lever Seated Good Morning: poses + props + rig.
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


# D45 - jalón en palanca: sentado, espalda en el respaldo y las manijas al frente; se tiran al pecho con los codos abajo
pl = dict(hip=[-320, -270], b=-10, hd=-2, g=1, ankle=[-60, -20], ed=1, ft=4)
PL = {
    "START": {**pl, "hx": -70, "hy": -560},
    "PULL": {**pl, "hx": -178, "hy": -470, "ed": -1},
    "LEAN_BAD": {**pl, "hx": -178, "hy": -470, "b": -30, "hd": -6, "ed": -1},
    "LOW_BAD": {**pl, "hx": -236, "hy": -330, "ed": -1},
    "ROUND_BAD": {**pl, "hx": -70, "hy": -560, "cv": 26, "hd": 16},
}

# D46 - buenos días sentado: cadera un poco más alta que la rodilla, pies planos y el tronco baja desde la cadera
gm = dict(hip=[-330, -350], ankle=[-110, -20], b=-6, hd=-2, g=1, hx=-160, hy=-385, ed=1, ft=0)
GM = {
    "UP": {**gm},
    "HINGE": {**gm, "b": 72, "hd": 72},
    "ROUND_BAD": {**gm, "b": 72, "hd": 72, "cv": 26},
    "LOW_BAD": {**gm, "b": 100, "hd": 100},
    "HEAD_BAD": {**gm, "b": 72, "hd": 96},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-pullover", "Lever Pullover", "GIMNASIO · ESPALDA",
         ["Espalda", "Dorsales"], rig(880, 0.84),
         [{"type": "lever", "pivot": [-190, -330], "seat": [-380, -150, -270], "back": [-352, -10, 440],
           "stack": -620, "frameTop": -980, "at": 0.72, "off": 56, "side": -1, "pin": 5,
           "grip": "hand", "k": 3.0}],
         PL, "START",
         ("Sentate con la espalda apoyada en el respaldo y las manijas al frente, con agarre prono. "
          "Con los codos bajos, tirá las manijas al pecho apretando los dorsales, hacé una pausa y volvé lento.")),
        ("lever-seated-good-morning", "Lever Seated Good Morning", "GIMNASIO · ISQUIOS",
         ["Isquiotibiales", "Glúteos"], rig(880, 0.84),
         [{"type": "lever", "pivot": [-380, -350], "seat": [-380, -150, -350], "back": [-430, -6, 440],
           "stack": -620, "frameTop": -980, "handle": [-160, -385], "pin": 5,
           "padOn": "torso", "at": 0.55, "off": 30, "side": -1, "k": 2.0}],
         GM, "UP",
         ("Sentate con la cadera un poco más alta que las rodillas y los pies planos en el piso. "
          "Con la espalda recta, inclinate desde la cadera hasta quedar paralelo al piso y volvé empujando con los glúteos."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
