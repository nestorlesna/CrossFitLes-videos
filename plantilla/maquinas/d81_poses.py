# Dataset D105 Smith Close Grip Bench Press: poses + props + rig.
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


# D105 - press de banca con agarre cerrado en la Smith: mismo banco plano que D93 (smith-reverse-grip-press),
# pero con las manos juntas sobre el esternÃ³n y los codos pegados al torso. La barra baja al pecho bajo.
st105 = dict(hip=[-20, -196], ankle=[230, 0], b=-90, hd=-92, ft=0, g=1, hx=-235, ed=1)

CG = {
    "TOP": {**st105, "hy": -505},
    "MID": {**st105, "hy": -390},
    "BOTTOM": {**st105, "hy": -272},
    "SHORT_BAD": {**st105, "hy": -380},
    "NECK_BAD": {**st105, "hip": [70, -196], "ankle": [320, 0], "hy": -292},
    "BUTT_BAD": {**st105, "hip": [-20, -262], "b": -104, "hd": -100, "hy": -330, "cv": -20},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-close-grip-bench-press", "Smith Close Grip Bench Press", "GIMNASIO Â· BRAZOS",
         ["TrÃ­ceps", "Pectorales", "Deltoides anterior"], rig(600, 0.7),
         [{"type": "bench", "x0": -560, "x1": 120, "h": 200},
          {"type": "smith", "x": -235, "top": -1040, "stops": -300, "track": "hands", "r": 70}],
         CG, "TOP",
         ("Press de banca con agarre cerrado en la Smith: acostado en el banco plano, las manos juntas sobre "
          "el esternÃ³n y los codos pegados al torso. La barra baja al pecho bajo y sube hasta estirar los "
          "brazos. El agarre cerrado carga mÃ¡s el trÃ­ceps y exige bajar el peso para controlar la barra."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)

