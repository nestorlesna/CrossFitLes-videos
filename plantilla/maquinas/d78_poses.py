# Dataset D102 Smith Sumo Squat: poses + props + rig.
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


# D102 - sentadilla sumo en la Smith: barra en la espalda alta (track "back", como D97/D100), pies bien
# separados y rodillas abiertas. En perfil la amplitud se lee como un apoyo ancho: pie de adelante a 60 y el de
# atrás a -55, con las rodillas siguiendo la línea de los pies.
st102 = dict(b=2, hd=0, g=1, hb=1, hx=-75, hy=22, ed=1, ft=0, ft2=0)


def SQ(**kw): return {**st102, **kw}


BASE = dict(ankle=[60, 0], ankle2=[-55, 0])

SQ = {
    "TOP": SQ(hip=[0, -430], **BASE),
    "BOTTOM": SQ(hip=[0, -300], **BASE),
    "HALF_BAD": SQ(hip=[0, -365], **BASE),
    "NARROW_BAD": SQ(hip=[0, -300], ankle=[20, 0], ankle2=[-20, 0]),
    "HEEL_BAD": SQ(hip=[0, -300], ankle=[60, -12], ankle2=[-55, -12], ft=20, ft2=18),
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-sumo-squat", "Smith Sumo Squat", "GIMNASIO · PIERNAS",
         ["Glúteos", "Cuádriceps", "Isquiotibiales"], rig(428, 0.8),
         [{"type": "smith", "x": -80, "top": -900, "gap": 300, "stops": -560, "track": "back",
           "torso": [-34, 18], "r": 56}],
         SQ, "TOP",
         ("Sentadilla sumo en la Smith: la barra apoyada en la espalda alta, los pies bien separados y las "
          "puntas hacia afuera. Bajá empujando las caderas hacia atrás y abriendo las rodillas, hasta que los "
          "muslos queden cerca de la paralela. Mantené el pecho arriba y la espalda derecha, y subí empujando "
          "con los talones. Trabaja glúteos y la cara interna del muslo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
