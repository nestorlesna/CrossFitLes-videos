# Dataset D01 - D31 Lever Kneeling Leg Curl y D32 Lever Military Press: poses + props + rig.
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


# D31 - femoral arrodillado: rodillas en la almohadilla baja, pecho en el apoyo inclinado y talones que suben
kn = dict(t=-22, b=35, hd=15, ft=-40, g=1, hx=95, hy=-590)
kneel = {
    "KNEEL": {**kn, "hip": [-230, -552], "s": 78},
    "MID": {**kn, "hip": [-230, -552], "s": 112},
    "CURL": {**kn, "hip": [-230, -552], "s": 145},
    "HIP_BAD": {**kn, "hip": [-250, -500], "t": -8, "b": 30, "hd": 24, "s": 145},
    "DIP_BAD": {**kn, "hip": [-230, -552], "b": 55, "hd": 40, "s": 145},
    "SHORT_BAD": {**kn, "hip": [-230, -552], "s": 105},
}

# D32 - press militar en maquina de palanca: agarre prono, manos algo mas abiertas que los hombros
mp = dict(hip=[-240, -230], ankle=[0, 0], ft=0, g=0, b=-4, hd=0)
press = {
    "DOWN": {**mp, "ua": 45, "fa": 135},
    "MID": {**mp, "ua": 94, "fa": 82},
    "UP": {**mp, "ua": 170, "fa": 6},
    "ARCH_BAD": {**mp, "hip": [-226, -236], "b": -24, "hd": -14, "cv": -30, "ua": 174, "fa": 4},
    "LOW_BAD": {**mp, "ua": -24, "fa": 196},
    "LOCK_BAD": {**mp, "ua": 180, "fa": -8},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-kneeling-leg-curl", "Lever Kneeling Leg Curl", "GIMNASIO · PIERNAS",
         ["Isquiotibiales", "Glúteos"], rig(720, 0.66),
         [{"type": "kneelingcurl", "pivot": [-140, -330], "stack": -740, "knee": [-300, -100],
           "handle": [95, -590], "roll": 236, "pin": 5, "k": 3.0}],
         kneel, "KNEEL",
         ("Arrodillate con las rodillas en la almohadilla y el pecho sobre el apoyo inclinado. Con la cadera quieta, "
          "llevá los talones hacia los glúteos, apretá un segundo arriba y volvé lento hasta casi estirar.")),
        ("lever-military-press", "Lever Military Press", "GIMNASIO · HOMBROS",
         ["Hombros", "Tríceps"], rig(700, 0.66),
         [{"type": "shoulderpress", "pivot": [-520, -620], "frameTop": -1080, "stack": -660,
           "seat": [-390, -90, -184], "back": [-318, -4, 470], "pin": 4}],
         press, "DOWN",
         ("Sentate con la espalda apoyada y agarrá las manijas con las palmas hacia abajo, un poco más abiertas que "
          "los hombros. Empujá hacia arriba sin arquear la lumbar y bajá controlado hasta la altura del hombro."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
