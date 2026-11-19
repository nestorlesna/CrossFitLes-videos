# Dataset D94 Smith Shoulder Press: poses + props + rig.
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


# D94 - press de hombros en la Smith: sentado en el banco con respaldo, la barra arranca a la altura de los
# hombros por delante de la cara y sube hasta estirar los brazos sin arquear la espalda ni encogerse.
st94 = dict(hip=[10, -246], ankle=[235, -16], ankle2=[160, -16], b=0, hd=0,
            ft=0, ft2=0, g=1, hx=150, ed=1)
SHO = {
    "DOWN": {**st94, "hy": -620},
    "TOP": {**st94, "hy": -815},
    "HALF_BAD": {**st94, "hy": -710},
    "ARCH_BAD": {**st94, "b": -22, "hd": -14, "hy": -600},
    "SHRUG_BAD": {**st94, "sh": 26, "hy": -808},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-shoulder-press", "Smith Shoulder Press", "GIMNASIO · HOMBROS",
         ["Deltoides", "Tríceps", "Espalda alta"], rig(520, 0.9),
         [{"type": "smith", "x": 150, "top": -1040, "gap": 280, "stops": -430, "track": "hands", "r": 56,
           "seat": [-300, 60, -240, -40, -6, 460]}],
         SHO, "DOWN",
         ("Press de hombros en la Smith: sentado con la espalda apoyada en el respaldo, la barra arranca a la "
          "altura de los hombros por delante de la cara y sube hasta estirar los brazos. Los codos quedan abiertos, "
          "el abdomen firme y la espalda pegada al respaldo: si te arqueás o te encogés, el trabajo se va a la "
          "lumbar y al cuello."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
