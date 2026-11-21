# Dataset D101 Smith Standing Military Press: poses + props + rig.
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


# D101 - press militar parado en la Smith: misma mecánica que D94 pero de pie (hip -455, hombros -735).
# La barra arranca a la altura de la clavícula por delante de la cara y sube hasta estirar los brazos.
st101 = dict(hip=[0, -455], ankle=[30, 0], ankle2=[-25, 0], b=1, hd=0,
             ft=0, ft2=0, g=1, hx=140, ed=1)
PR = {
    "DOWN": {**st101, "hy": -748},
    "TOP": {**st101, "hy": -1010},
    "HALF_BAD": {**st101, "hy": -880},
    "ARCH_BAD": {**st101, "b": -18, "hd": -12, "hy": -750},
    "SHRUG_BAD": {**st101, "sh": 26, "hy": -1000},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-standing-military-press", "Smith Standing Military Press", "GIMNASIO · HOMBROS",
         ["Deltoides", "Tríceps", "Espalda alta"], rig(500, 0.66),
         [{"type": "smith", "x": 140, "top": -1120, "gap": 280, "stops": -560, "track": "hands", "r": 56}],
         PR, "DOWN",
         ("Press militar parado en la Smith: la barra arranca a la altura de la clavícula, por delante de la cara, "
          "y sube hasta estirar los brazos. Los codos quedan abajo y adelante, el abdomen firme y el torso derecho: "
          "si te arqueás o encogés los hombros, el trabajo se va a la lumbar y al cuello."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
