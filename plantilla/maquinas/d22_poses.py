# Dataset D43 Lever Hip Extension v. 2 y D44 Lever Kneeling Twist: poses + props + rig.
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


# D43 - extensión de cadera en palanca: sentado, la almohadilla va detrás del muslo y el muslo empuja atrás/abajo
he = dict(hip=[-300, -520], b=-6, hd=6, g=1, hx=-190, hy=-610, ed=1, ft=-20)
HE = {
    "START": {**he, "ankle": [-60, -290]},
    "MID": {**he, "ankle": [-70, -230]},
    "TOP": {**he, "ankle": [-84, -170]},
    "LEAN_BAD": {**he, "ankle": [-70, -230], "b": 16, "hd": 14, "cv": 18},
    "HIP_BAD": {**he, "ankle": [-70, -230], "hip": [-296, -590], "b": 4},
    "SWING_BAD": {**he, "ankle": [-92, -140], "b": 22, "hd": 20, "hip": [-288, -526]},
}

# D44 - torsión arrodillado: rodillas en la almohadilla, manos en el brazo de la máquina y el giro se cuenta arriba
tk = dict(hip=[-140, -330], ankle=[-380, -60], ft=54, knee="back", b=0, hd=0, g=1, hx=-40, hy=-540, ed=-1, cs=0)
TK = {
    "CENTER": {**tk},
    "TW_L": {**tk, "cs": 1, "b": -7, "hd": -7, "hx": -24},
    "TW_R": {**tk, "cs": -1, "b": 7, "hd": 7, "hx": -56},
    "PULL_BAD": {**tk, "cs": 1.3, "b": -18, "hd": -16, "hx": -8, "hy": -512},
    "ROUND_BAD": {**tk, "cs": 0.6, "cv": 24, "hd": 30, "b": 6},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-hip-extension-v-2", "Lever Hip Extension v. 2", "GIMNASIO · GLÚTEOS",
         ["Glúteos", "Isquiotibiales"], rig(880, 0.84),
         [{"type": "lever", "pivot": [-300, -520], "seat": [-380, -150, -520], "back": [-352, -6, 440],
           "stack": -620, "frameTop": -980, "handle": [-190, -610], "at": 0.72, "off": 58, "side": -1, "pin": 5}],
         HE, "START",
         ("Sentate con la espalda apoyada en el respaldo y las manos en las manijas. La almohadilla va detrás del muslo: "
          "empujá con los glúteos y los isquios para llevar el muslo atrás, sostené arriba y volvé lento.")),
        ("lever-kneeling-twist", "Lever Kneeling Twist", "GIMNASIO · CORE",
         ["Core", "Oblicuos"], rig(700, 0.9),
         [{"type": "kneeltwist", "pivot": [-30, -673], "knee": [-300, 30, -90], "stack": -640,
           "frameTop": -820, "pin": 5}],
         TK, "CENTER",
         ("Arrodillate con las rodillas en la almohadilla y sujetá las manijas a la altura del pecho. "
          "Con el core activado, girá el torso hacia un lado, volvé al centro y repetí para el otro lado."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
