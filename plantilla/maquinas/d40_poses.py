# Dataset D64 Sled Closer Hack Squat: poses + props + rig.
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


# D64 - sentadilla hack con los pies juntos (sled closer): mismo carro inclinado, el recorrido baja y sube por el
# riel y el pie lejano queda casi pegado al cercano (ankle2 a -8) para marcar la postura cerrada.
st6 = dict(hip=[-297.8, -394.7], ankle=[0, -60], ankle2=[-8, -60], b=-36, hd=-6, g=0, ua=16, fa=118,
           ft=-14, ft2=-14, sh=0)
HACKC = {
    "TOP": {**st6},
    "HALF": {**st6, "hip": [-228.0, -298.6]},
    "BOTTOM": {**st6, "hip": [-187.5, -243.0]},
    "SHALLOW_BAD": {**st6, "hip": [-252.0, -333.0]},
    "HEELS_BAD": {**st6, "hip": [-187.5, -243.0], "ankle": [8, -96], "ankle2": [0, -96], "ft": 22, "ft2": 22},
    "BACK_BAD": {**st6, "hip": [-117.5, -273.0], "b": -2, "hd": 14, "cv": 24},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-closer-hack-squat", "Sled Closer Hack Squat", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteos"], rig(800, 0.95),
         [{"type": "hacksquat", "hip": [-297.8, -394.7], "lean": -36, "foot": [0, -60], "plat": -14,
           "len": 300, "rail": [-470, 620], "stops": -330, "hand": [140.6, -99.6]}],
         HACKC, "TOP",
         ("Sentadilla hack con los pies juntos: apoyá la espalda y las hombreras, juntá los pies en la "
          "plataforma y bajá el carro por los rieles hasta donde llegues con la espalda apoyada. Subí empujando "
          "con los talones y las rodillas alineadas con los pies."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
