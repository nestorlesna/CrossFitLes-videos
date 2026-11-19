# Dataset D68 Sled 45 Leg Wide Press: poses + props + rig.
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


# D68 - prensa a 45° con los pies bien separados: la misma máquina de D66/D67 pero el pie lejano se abre
# (ankle2 = ankle + (-84, 8)) para leer la postura ancha; el recorrido es el de la prensa normal.
st10 = dict(hip=[-320, -300], b=-45, hd=-12, g=1, hx=-280, hy=-310, ed=1, ft=-128, ft2=-128)


def wide(ankle, dx=-84, dy=8, **kw):
    return {**st10, **kw, "ankle": ankle, "ankle2": [ankle[0] + dx, ankle[1] + dy]}


LPW = {
    "TOP": wide([50.3, -559.3]),
    "MID": wide([3.6, -526.6]),
    "BOTTOM": wide([-45.6, -492.1]),
    "SHALLOW_BAD": wide([10.0, -532.0]),
    "HEELS_BAD": wide([-45.6, -492.1], ft=-100, ft2=-100),
    "NARROW_BAD": wide([-45.6, -492.1], dx=-10, dy=4),
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-45-leg-wide-press", "Sled 45 Leg Wide Press", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteos"], rig(610, 0.92),
         [{"type": "legpress", "hip": [-320, -300], "ang": 35, "lean": -45, "stops": 300}],
         LPW, "TOP",
         ("Prensa a 45 grados con los pies bien separados: apoyá la espalda, abrí los pies hacia los bordes de "
          "la plataforma y bajá el carro hasta donde llegues con la cadera apoyada. Empujá con toda la planta y "
          "las rodillas alineadas con las puntas."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
