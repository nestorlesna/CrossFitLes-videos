# Dataset D99 Smith Standing Behind Head Military Press: poses + props + rig.
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


# D99 - press militar por detrás de la cabeza, PARADO en la Smith (D75 lo hacía sentado). Las manos van en el
# sistema del torso (`hb`) y la barra sube y baja por el mismo carril, detrás de la nuca.
st99 = dict(b=2, hd=0, g=1, hb=1, hx=-100, hy=45, ed=1)


def MP(**kw): return {**st99, **kw, "hip": [0, -450], "ankle": [42, 0], "ankle2": [-20, 0]}


SQ = {
    "DOWN": MP(hy=45),
    "TOP": MP(hy=-290),
    "HALF_BAD": MP(hy=-120),
    "ARCH_BAD": MP(b=-16, hy=-270),
    "SHRUG_BAD": MP(hy=-290, sh=24),
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-standing-behind-head-military-press", "Smith Standing Behind Head Military Press",
         "GIMNASIO · HOMBROS", ["Deltoides", "Tríceps"], rig(500, 0.72),
         [{"type": "smith", "x": -95, "top": -1040, "gap": 280, "stops": -300, "track": "hands", "r": 56}],
         SQ, "DOWN",
         ("Press militar por detrás de la cabeza en la Smith, parado: la barra baja hasta la nuca y sube por el "
          "mismo carril hasta estirar los brazos arriba. Mantené el abdomen firme y el torso derecho, sin arquear la "
          "espalda ni encoger los hombros. Bajá con control hasta la altura de las orejas y no dejes que la barra "
          "caiga de golpe."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
