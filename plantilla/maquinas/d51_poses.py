# Dataset D75 Smith Behind Neck Press: poses + props + rig.
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


# D75 - press militar por detrás de la nuca en la Smith: sentado en el banco con respaldo, la barra arranca
# detrás de la cabeza a la altura del hombro y se empuja hasta arriba sin arquear la espalda ni encogerse.
st75 = dict(hip=[0, -236], ankle=[215, -36], ankle2=[145, -36], ft=0, ft2=0, b=2, hd=0, g=1, ed=1)
BNP = {
    "DOWN": {**st75, "sh": 0, "hx": -50, "hy": -590},
    "TOP": {**st75, "sh": 0, "hx": 0, "hy": -846},
    "HALF_BAD": {**st75, "sh": 0, "hx": -25, "hy": -720},
    "ARCH_BAD": {**st75, "sh": 0, "b": -18, "hd": -10, "hx": -50, "hy": -600},
    "SHRUG_BAD": {**st75, "sh": 18, "hx": 0, "hy": -860},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-behind-neck-press", "Smith Behind Neck Press", "GIMNASIO · HOMBROS",
         ["Hombros", "Deltoides", "Press"], rig(540, 0.95),
         [{"type": "smith", "x": -30, "top": -900, "gap": 280, "stops": -380, "track": "hands", "r": 64,
           "seat": [-290, 70, -230, -250, -8, 470]}],
         BNP, "DOWN",
         ("Press por detrás de la nuca en la Smith: sentate en el banco con la espalda apoyada, agarrá la barra "
          "detrás de la cabeza a la altura de los hombros y empujá hasta arriba sin arquear la espalda. Bajá "
          "controlando hasta la nuca."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
