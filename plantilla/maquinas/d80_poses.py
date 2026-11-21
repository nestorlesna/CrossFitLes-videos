# Dataset D104 Smith Upright Row: poses + props + rig.
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


# D104 - remo al mentÃ³n en la Smith: agarre angosto, la barra sube pegada al cuerpo desde los muslos hasta el
# mentÃ³n y los codos guÃ­an el movimiento. Manos en `hx` fijo (la barra no se aleja) y `hy` de los muslos al mentÃ³n.
st104 = dict(hip=[0, -455], ankle=[40, 0], ankle2=[-22, 0], b=2, hd=0, g=1, hx=145, ed=-1, ft=0, ft2=0)

UR = {
    "DOWN": {**st104, "hy": -470},
    "UP": {**st104, "hy": -690},
    "HALF_BAD": {**st104, "hy": -595},
    "FAR_BAD": {**st104, "hy": -690, "hx": 230},
    "SHRUG_BAD": {**st104, "hy": -690, "sh": 24},
    "LEAN_BAD": {**st104, "hy": -690, "b": -12, "hd": -6},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-upright-row", "Smith Upright Row", "GIMNASIO Â· HOMBROS",
         ["Deltoides", "Trapecio", "BÃ­ceps"], rig(480, 0.8),
         [{"type": "smith", "x": 130, "top": -880, "gap": 280, "stops": -520, "track": "hands", "r": 56}],
         UR, "DOWN",
         ("Remo al mentÃ³n en la Smith: parado, agarre angosto sobre la barra y la barra pegada al cuerpo. "
          "Subila desde los muslos hasta el mentÃ³n guiando con los codos bien altos, sin encogerte ni tirar "
          "con la espalda, y bajala despacio. Trabaja hombros, trapecio y bÃ­ceps."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)

