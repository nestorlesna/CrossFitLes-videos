# Dataset D96 Smith Single Leg Split Squat: poses + props + rig.
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


# D96 - sentadilla búlgara en la Smith: pie de adelante en el piso, pie de atrás arriba del banco y las manos
# agarradas a la barra para estabilidad. Las dos piernas usan ramas distintas del IK (la de atrás dobla la rodilla
# hacia abajo), así que las poses guardan s/t y s2/t2 calculados a mano.
FRONT = (150, 0)
REAR = (-386, -166)
st96 = dict(b=6, hd=0, hx=120, hy=-540, g=1, ed=-1, ft=0, ft2=0)


def SPLIT(hip, front=FRONT, **kw):
    fs, ft = legIK(hip, front, False)
    rs, rt = legIK(hip, REAR, True)
    return {**st96, **kw, "hip": list(hip), "ankle": list(front), "s": fs, "t": ft, "s2": rs, "t2": rt}


SQ = {
    "TOP": SPLIT((-20, -430)),
    "BOTTOM": SPLIT((-20, -320)),
    "HALF_BAD": SPLIT((-20, -380)),
    "HEEL_BAD": SPLIT((-20, -330), ft=26),
    "SHORT_BAD": SPLIT((-20, -330), front=(30, 0)),
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-single-leg-split-squat", "Smith Single Leg Split Squat", "GIMNASIO · PIERNAS",
         ["Cuádriceps", "Glúteos", "Isquiotibiales"], rig(428, 0.8),
         [{"type": "smith", "x": 120, "top": -900, "gap": 280, "stops": -560, "track": "hands", "r": 60},
          {"type": "bench", "x0": -520, "x1": -250, "h": 200}],
         SQ, "TOP",
         ("Sentadilla búlgara en la Smith: un pie adelante en el piso y el otro arriba del banco, con las manos "
          "agarradas a la barra para estabilizarte. Bajá doblando la rodilla de adelante, con el torso derecho y "
          "la rodilla siguiendo la punta del pie; subí empujando con el talón de adelante. Cambiá de pierna al "
          "terminar la serie."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
