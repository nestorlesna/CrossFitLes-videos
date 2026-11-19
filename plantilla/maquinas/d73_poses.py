# Dataset D97 Smith Sprint Lunge: poses + props + rig.
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


# D97 - zancada "sprint" en la Smith: la barra apoya en la espalda alta (track "back"), el pie de adelante en el
# piso y el empeine del de atrás sobre el soporte bajo de la máquina. Misma rama doble de IK que D96.
FRONT = (130, 0)
REAR = (-345, -86)
st97 = dict(b=4, hd=0, g=1, hb=1, hx=-75, hy=22, ed=1, ft=0, ft2=24)


def LUNGE(hip, front=FRONT, **kw):
    fs, ft = legIK(hip, front, False)
    rs, rt = legIK(hip, REAR, True)
    return {**st97, **kw, "hip": list(hip), "ankle": list(front), "s": fs, "t": ft, "s2": rs, "t2": rt}


SQ = {
    "TOP": LUNGE((-20, -430)),
    "BOTTOM": LUNGE((-20, -320)),
    "HALF_BAD": LUNGE((-20, -375)),
    "HEEL_BAD": LUNGE((-20, -330), ft=26),
    "SHORT_BAD": LUNGE((-20, -330), front=(30, 0)),
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-sprint-lunge", "Smith Sprint Lunge", "GIMNASIO · PIERNAS",
         ["Glúteos", "Cuádriceps", "Isquiotibiales"], rig(428, 0.8),
         [{"type": "smith", "x": -80, "top": -900, "gap": 300, "stops": -560, "track": "back",
           "torso": [-34, 18], "r": 56},
          {"type": "step", "x": -350, "y": 0, "w": 280, "h": 86}],
         SQ, "TOP",
         ("Zancada sprint en la Smith: la barra apoyada en la espalda alta, un pie adelante en el piso y el "
          "empeine del otro sobre el soporte bajo de la máquina. Bajá doblando la rodilla de adelante, mantené el "
          "torso derecho y subí rápido empujando con el talón de adelante. Alterná las piernas en cada "
          "repetición, como si fueras a arrancar a correr."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
