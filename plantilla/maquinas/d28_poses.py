# Dataset D52 Lever One Arm Lateral High Row: poses + props + rig.
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


# D52 - remo alto a un brazo: el brazo de trabajo arranca extendido arriba-adelante y baja la manija hasta el
# costado del torso con el codo hacia atrás y afuera. La otra mano queda apoyada en la cadera, sobre la manija baja:
# el brazo lejano la sigue (g2 1) para que el asa quede quieta junto al cuerpo.
rw = dict(hip=[-320, -270], ankle=[40, -30], b=-4, hd=-2, g=1, g2=1, ed=1, ed2=1, ft=0)
ONE = {
    "START": {**rw, "hx": -45, "hy": -690, "hx2": -370, "hy2": -300},
    "PULL": {**rw, "hx": -180, "hy": -510, "ed": -1, "hx2": -370, "hy2": -300},
    "LEAN_BAD": {**rw, "hx": -180, "hy": -510, "ed": -1, "hx2": -370, "hy2": -300,
                 "b": -30, "hd": -10},
    "SHRUG_BAD": {**rw, "hx": -195, "hy": -565, "ed": 1, "hx2": -370, "hy2": -300, "hd": 10},
    "ROUND_BAD": {**rw, "hx": -45, "hy": -690, "hx2": -370, "hy2": -300, "b": 14, "hd": 20, "cv": 26},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-one-arm-lateral-high-row", "Lever One Arm Lateral High Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Bíceps"], rig(820, 0.87),
         [{"type": "leverrow", "pivot": [-380, -760], "seat": [-430, -190, -270], "back": [-460, -6, 360],
           "chest": [-300, -560, 300], "foot": [132, 18], "horn": [-520, -180], "radius": 112, "farOff": -10}],
         ONE, "START",
         ("Sentate frente a la máquina con la espalda recta, los pies en la placa y el pecho cerca de la "
          "almohadilla. Tomá una manija alta con una sola mano y dejá la otra apoyada en la cadera. Tirá la manija "
          "hacia el costado del torso llevando el codo hacia atrás y afuera, juntá el omóplato y volvé lento sin "
          "rotar el tronco."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
