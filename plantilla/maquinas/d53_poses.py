# Dataset D77 Smith Bent Over Row: poses + props + rig.
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


# D77 - remo inclinado en la Smith: el cuerpo hace la bisagra, la barra cuelga de los brazos a la altura de las
# rodillas y se tira al abdomen juntando las escápulas; la barra corre guiada y no se separa de la vertical.
st77 = dict(ankle=[60, 0], ankle2=[-20, 0], ft=0, ft2=0)
HINGE = {**st77, "hip": [-50, -430], "b": 60, "hd": 0, "g": 1, "hx": 200, "hy": -255}
ROW = {
    "HINGE": HINGE,
    "PULL": {**HINGE, "hy": -470},
    "ROUND_BAD": {**HINGE, "hip": [-70, -400], "b": 68, "hd": 62, "hy": -275},
    "SWING_BAD": {**HINGE, "hip": [-10, -470], "b": 38, "hd": 4, "hy": -480},
    "SHORT_BAD": {**HINGE, "hy": -355},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-bent-over-row", "Smith Bent Over Row", "GIMNASIO · ESPALDA",
         ["Espalda alta", "Bíceps", "Antebrazos"], rig(370, 0.85),
         [{"type": "smith", "x": 200, "top": -860, "gap": 300, "stops": -240, "track": "hands",
           "torso": [-34, 18], "r": 60}],
         ROW, "HINGE",
         ("Remo inclinado en la Smith: el cuerpo se dobla desde la cadera con la espalda recta y las rodillas "
          "blandas, la barra cuelga a la altura de las rodillas y se tira al abdomen juntando las escápulas. "
          "La barra va guiada, así que el recorrido es siempre en la misma vertical."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
