# Dataset D95 Smith Shrug: poses + props + rig.
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


# D95 - encogimientos de hombros en la Smith: parado de frente a la barra, brazos rectos y solo suben los
# hombros hacia las orejas. La barra queda a la altura de la cadera y los topes frenan la bajada.
st95 = dict(hip=[-30, -460], ankle=[45, 0], ankle2=[-25, 0], b=3, hd=0,
            ft=0, ft2=0, g=1, hx=25, ed=1)
SH = {
    "DOWN": {**st95, "hy": -415},
    "UP": {**st95, "sh": 40, "hy": -455},
    "HALF_BAD": {**st95, "sh": 20, "hy": -437},
    "ELBOW_BAD": {**st95, "sh": 24, "hx": 110, "hy": -510},
    "LEAN_BAD": {**st95, "b": -16, "sh": 32, "hy": -480},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-shrug", "Smith Shrug", "GIMNASIO · ESPALDA",
         ["Trapecios", "Hombros", "Espalda alta"], rig(540, 0.8),
         [{"type": "smith", "x": 25, "top": -920, "gap": 280, "stops": -300, "track": "hands", "r": 60}],
         SH, "DOWN",
         ("Encogimientos de hombros en la Smith: parado de frente a la barra, con los brazos rectos y las manos "
          "un poco más abiertas que los hombros, subí los hombros hacia las orejas y bajalos despacio. La barra "
          "queda a la altura de la cadera y solo se mueven los hombros: los codos no se doblan."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
