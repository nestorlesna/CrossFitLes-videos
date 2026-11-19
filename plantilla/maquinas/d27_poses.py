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


rw = dict(hip=[-320, -270], ankle=[40, -30], b=-6, hd=-2, g=1, g2=1, ed=1, ed2=1, ft=0)
NARROW = {
    "START": {**rw, "hx": -60, "hy": -470, "hx2": -74, "hy2": -462},
    "PULL": {**rw, "hx": -220, "hy": -480, "ed": -1, "hx2": -234, "hy2": -472, "ed2": -1},
    "LEAN_BAD": {**rw, "hx": -220, "hy": -480, "ed": -1, "hx2": -234, "hy2": -472, "ed2": -1,
                 "b": -30, "hd": -10},
    "SHRUG_BAD": {**rw, "hx": -180, "hy": -565, "ed": 1, "hx2": -194, "hy2": -557, "ed2": 1, "hd": 8},
    "ROUND_BAD": {**rw, "hx": -60, "hy": -470, "hx2": -74, "hy2": -462, "b": 16, "hd": 20, "cv": 26},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-narrow-grip-seated-row", "Lever Narrow Grip Seated Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Bíceps"], rig(840, 0.86),
         [{"type": "leverrow", "pivot": [-330, -160], "seat": [-430, -190, -270], "back": [-460, -8, 360],
           "chest": [-280, -548, 288], "foot": [132, 18], "horn": [-500, -180], "radius": 112, "farOff": -16}],
         NARROW, "START",
         ("Sentate con la espalda recta y el pecho apoyado en la almohadilla, los pies planos en la placa y las "
          "manijas con agarre estrecho, las palmas enfrentadas. Tirá de las dos manijas hacia el torso juntando los "
          "omóplatos, hacé una pausa y volvé lento sin perder el apoyo del pecho."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
