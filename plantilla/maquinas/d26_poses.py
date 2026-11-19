# Dataset D50 Lever High Row: poses + props + rig.
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


# D50 - remo alto sentado: el pecho va contra la almohadilla, los pies en la placa y las dos manijas arrancan
# altas y anchas para bajar juntas hasta el pecho, con los codos hacia atrás.
hr = dict(hip=[-320, -270], ankle=[40, -30], b=-4, hd=-2, g=1, ed=1, ft=0)
HR = {
    "START": {**hr, "hx": -55, "hy": -690},
    "PULL": {**hr, "hx": -180, "hy": -510, "ed": -1},
    "LEAN_BAD": {**hr, "hx": -180, "hy": -510, "ed": -1, "b": -30, "hd": -10},
    "SHRUG_BAD": {**hr, "hx": -195, "hy": -565, "ed": 1, "hd": 10},
    "ROUND_BAD": {**hr, "hx": -55, "hy": -690, "b": 14, "hd": 20, "cv": 26},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-high-row", "Lever High Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Deltoides posteriores"], rig(820, 0.87),
         [{"type": "leverrow", "pivot": [-380, -760], "seat": [-430, -190, -270], "back": [-460, -6, 360],
           "chest": [-300, -560, 300], "foot": [132, 18], "horn": [-520, -180], "radius": 112, "farOff": -10}],
         HR, "START",
         ("Sentate con el pecho apoyado en la almohadilla y los pies planos en la placa. Tomá las manijas altas "
          "con agarre prono, un poco más separadas que los hombros. Tirá de las manijas hacia el pecho llevando "
          "los codos atrás, juntá los omóplatos y volvé lento sin perder el apoyo del pecho."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
