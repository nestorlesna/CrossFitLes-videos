# Dataset D66 Sled 45 Degrees One Leg Press: poses + props + rig.
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


# D66 - prensa a 45° a una pierna: la misma de `leg-press` pero la pierna lejana queda flexionada colgando
# (ankle2 abajo, junto al asiento) y solo la cercana empuja la plataforma por el riel de 35°.
st8 = dict(hip=[-320, -300], b=-45, hd=-12, ft=-128, g=1, hx=-280, hy=-310, ed=1,
           ankle2=[-190, -90], ft2=20)
LP1 = {
    "TOP": {**st8, "ankle": [50.3, -559.3]},
    "MID": {**st8, "ankle": [3.6, -526.6]},
    "BOTTOM": {**st8, "ankle": [-45.6, -492.1]},
    "SHALLOW_BAD": {**st8, "ankle": [10.0, -532.0]},
    "HEELS_BAD": {**st8, "ankle": [-45.6, -492.1], "ft": -88},
    "FREELEG_BAD": {**st8, "ankle": [-45.6, -492.1], "ankle2": [-120, -455], "ft2": -128},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-45-degrees-one-leg-press", "Sled 45 Degrees One Leg Press", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteos"], rig(610, 0.92),
         [{"type": "legpress", "hip": [-320, -300], "ang": 35, "lean": -45, "stops": 300}],
         LP1, "TOP",
         ("Prensa a 45 grados a una pierna: apoyá la espalda en el respaldo, poné un pie en el centro de la "
          "plataforma y dejá la otra pierna flexionada sin apoyar. Empujá la plataforma por los rieles y bajá "
          "controlando hasta donde llegues con la cadera apoyada."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
