# Dataset D67 Sled 45 Calf Press: poses + props + rig.
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


# D67 - gemelos en la prensa a 45°: piernas estiradas (rodillas trabadas), planta en la plataforma y el tobillo
# hace todo el recorrido: la cadera corre un poco por el riel (d 402 -> 458) y el pie pasa de flexión a extensión.
st9 = dict(hip=[-320, -300], b=-45, hd=-12, g=1, hx=-280, hy=-310, ed=1)
C45 = {
    "DOWN": {**st9, "ankle": [3.5, -526.7], "ankle2": [-36.5, -518.7], "ft": -148, "ft2": -148},
    "UP": {**st9, "ankle": [63.3, -568.6], "ankle2": [23.3, -560.6], "ft": -100, "ft2": -100},
    "SHALLOW_BAD": {**st9, "ankle": [33, -548], "ankle2": [-7, -540], "ft": -124, "ft2": -124},
    "KNEE_BAD": {**st9, "ankle": [-30, -505], "ankle2": [-70, -497], "ft": -128, "ft2": -128},
    "HIP_BAD": {**st9, "hip": [-296, -334], "b": -38, "ankle": [-12, -528], "ankle2": [-52, -520],
                "ft": -148, "ft2": -148},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-45-calf-press", "Sled 45 Calf Press", "GIMNASIO · PIERNAS",
         ["Gemelos", "Sóleo"], rig(610, 0.92),
         [{"type": "legpress", "hip": [-320, -300], "ang": 35, "lean": -45, "stops": 320}],
         C45, "DOWN",
         ("Gemelos en la prensa a 45 grados: apoyá la espalda, las rodillas quedan trabadas y la planta de los "
          "pies en la plataforma. Empujá la plataforma extendiendo los tobillos y bajá hasta sentir el estiramiento "
          "del gemelo, sin doblar las rodillas."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
