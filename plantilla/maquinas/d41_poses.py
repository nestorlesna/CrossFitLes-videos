# Dataset D65 Sled Hack Squat: poses + props + rig.
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


# D65 - sentadilla hack con postura normal: mismo carro inclinado que D64 pero el pie lejano se separa
# (ankle2 a -30, punta abierta) para leer el ancho de hombros, y el fondo baja un poco más.
st7 = dict(hip=[-297.8, -394.7], ankle=[0, -60], ankle2=[-30, -60], b=-36, hd=-6, g=0, ua=16, fa=118,
           ft=-14, ft2=10, sh=0)
HACKS = {
    "TOP": {**st7},
    "HALF": {**st7, "hip": [-215.0, -285.0]},
    "BOTTOM": {**st7, "hip": [-172.0, -220.0]},
    "SHALLOW_BAD": {**st7, "hip": [-248.0, -330.0]},
    "HEELS_BAD": {**st7, "hip": [-172.0, -220.0], "ankle": [8, -96], "ankle2": [-22, -96], "ft": 22, "ft2": 26},
    "BACK_BAD": {**st7, "hip": [-112.0, -268.0], "b": 0, "hd": 14, "cv": 24},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-hack-squat", "Sled Hack Squat", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteos"], rig(800, 0.95),
         [{"type": "hacksquat", "hip": [-297.8, -394.7], "lean": -36, "foot": [0, -60], "plat": -14,
           "len": 300, "rail": [-470, 620], "stops": -330, "hand": [140.6, -99.6]}],
         HACKS, "TOP",
         ("Sentadilla hack clásica: apoyá la espalda y las hombreras, poné los pies al ancho de hombros en la "
          "plataforma y bajá el carro por los rieles con las rodillas en línea con las puntas. Subí empujando "
          "con los talones hasta estirar las piernas sin trabarlas."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
