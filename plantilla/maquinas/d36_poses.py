# Dataset D60 Lever Gripless Shrug v.2: poses + props + rig.
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


# D60 - variante 2 del encogimiento sin agarre: misma máquina con las manijas altas, a la altura del cuello, y las
# almohadillas sobre los dos hombros. El recorrido sigue siendo empujar con los trapecios (sh) sin doblar los codos.
st2 = dict(hip=[0, -470], ankle=[76, -4], ankle2=[-64, 0], b=0, hd=0, g=1, g2=1, ed=-1, ed2=-1, ft=0, sh=0)
SHRUG2 = {
    "START": {**st2, "hx": 190, "hy": -735, "hx2": 186, "hy2": -729},
    "SHRUG": {**st2, "sh": 28, "hx": 190, "hy": -735, "hx2": 186, "hy2": -729},
    "LEAN_BAD": {**st2, "b": -20, "hd": -4, "hx": 190, "hy": -735, "hx2": 186, "hy2": -729},
    "HALF_BAD": {**st2, "sh": 9, "hd": 6, "hx": 190, "hy": -735, "hx2": 186, "hy2": -729},
    "ROUND_BAD": {**st2, "b": 16, "hd": 22, "cv": 26, "hx": 190, "hy": -735, "hx2": 186, "hy2": -729},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-gripless-shrug-v-2", "Lever Gripless Shrug v. 2", "GIMNASIO · ESPALDA",
         ["Espalda", "Trapecios", "Espalda alta"], rig(600, 0.78),
         [{"type": "levershrug", "column": 330, "top": -1000, "stack": 450,
           "grip": [190, -735], "padOff": 6, "pin": 7, "k": 6}],
         SHRUG2, "START",
         ("Parate bajo las almohadillas con las manos en las manijas altas, a la altura del cuello. Sin doblar "
          "los codos, empujá las almohadillas con los hombros hacia arriba, hacé una pausa y bajá lento. El "
          "agarre alto ayuda a mantener el pecho arriba durante todo el recorrido."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
