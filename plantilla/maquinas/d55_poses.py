# Dataset D79 Smith Deadlift: poses + props + rig.
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


# D79 - peso muerto en la Smith: la barra sale del piso pegada a las tibias, el cuerpo sube empujando con las
# piernas y extendiendo la cadera, con la espalda recta y los hombros sobre la barra.
st79 = dict(ankle=[60, 0], ankle2=[-20, 0], ft=0, ft2=0, g=1, hx=70)
DEAD = {
    "START": {**st79, "hip": [-110, -250], "b": 52, "hd": -4, "hy": -110},
    "MID": {**st79, "hip": [-80, -360], "b": 40, "hd": -2, "hy": -250},
    "TOP": {**st79, "hip": [0, -455], "b": 8, "hd": 0, "hy": -412},
    "ROUND_BAD": {**st79, "hip": [-110, -250], "b": 56, "hd": 38, "hy": -110},
    "HIPUP_BAD": {**st79, "hip": [-30, -420], "b": 28, "hd": 0, "hy": -350},
    "LEAN_BAD": {**st79, "hip": [0, -455], "b": -5, "hd": -8, "hy": -418},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-deadlift", "Smith Deadlift", "GIMNASIO · PIERNAS",
         ["Isquios", "Glúteo", "Espalda baja"], rig(540, 0.85),
         [{"type": "smith", "x": 70, "top": -860, "gap": 300, "stops": -560, "track": "hands",
           "torso": [-34, 18], "r": 72}],
         DEAD, "START",
         ("Peso muerto en la Smith: la barra arranca del piso pegada a las tibias, el pecho arriba y la espalda "
          "recta. Subís empujando el piso con las piernas y extendiendo la cadera hasta quedar derecho, y bajás "
          "controlando el mismo camino. La barra corre guiada en una sola vertical."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
