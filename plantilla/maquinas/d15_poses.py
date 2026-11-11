# Dataset D01 · D29 Assisted Wide-grip Chest Dip (Kneeling) y D30 Lever Overhand Triceps Dip: poses + props + rig.
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


PROP_A = [{"type": "assisted", "stack": 420, "grip": [60, -1240], "dip": [60, -760],
           "pivot": [300, -260], "rest": -567, "pin": 6, "k": 1}]
cm = dict(s=92, t=4, ft=80, g=1, hx=60, hy=-750, ed=-1)

# ── D29 ── fondos de pecho asistidos con agarre ancho: algo más de recorrido y pecho bien alto ──
wide = {
    "TOP": {**cm, "hip": [-18.6, -804.0], "b": 16, "hd": 12},
    "MID": {**cm, "hip": [-40.0, -714.0], "b": 19, "hd": 16},
    "BOTTOM": {**cm, "hip": [-58.0, -646.0], "b": 22, "hd": 20},
    "UPRIGHT_BAD": {**cm, "hip": [-40.0, -714.0], "b": 0, "hd": 2},
    "SHRUG_BAD": {**cm, "hip": [-58.0, -646.0], "b": 22, "hd": 20, "cv": 26},
}

# ── D30 ── fondos de tríceps en máquina de palanca (manijas al costado que bajan) ──
sd = dict(hip=[-240, -230], ankle=[0, 0], ft=0, b=4, hd=2, g=1, ed=-1)
dip30 = {
    "TOP": {**sd, "hx": -185, "hy": -390},
    "MID": {**sd, "hx": -195, "hy": -290},
    "BOTTOM": {**sd, "hx": -206, "hy": -186},
    "LEAN_BAD": {**sd, "b": 26, "hd": 30, "hx": -150, "hy": -200, "cv": 22},
    "LOCK_BAD": {**sd, "hx": -210, "hy": -182},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("assisted-wide-grip-chest-dip-kneeling", "Assisted Wide-grip Chest Dip", "GIMNASIO · PECHO",
         ["Pecho", "Tríceps"], rig(560, 0.58), PROP_A, wide, "TOP",
         ("Con las manos más separadas en las paralelas, el pecho se estira más abajo. Apoyá las rodillas, "
          "elegí el contrapeso, bajá hasta que los brazos queden paralelos y empujá con el pecho adelante, "
          "sin encoger los hombros.")),
        ("lever-overhand-triceps-dip", "Lever Overhand Triceps Dip", "GIMNASIO · BRAZOS",
         ["Tríceps", "Pecho"], rig(720, 0.66),
         [{"type": "seateddip", "pivot": [-430, -560], "frameTop": -1000, "stack": -640,
           "seat": [-390, -90, -184], "back": [-318, 4, 470], "pin": 5}],
         dip30, "TOP",
         ("Sentate con la espalda pegada al respaldo y agarrá las manijas con agarre prono. Empujá hacia "
          "abajo hasta casi estirar los codos, sin encoger los hombros, y subí lento hasta que los codos "
          "queden a unos noventa grados."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
