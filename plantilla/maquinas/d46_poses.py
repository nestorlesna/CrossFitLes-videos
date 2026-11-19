# Dataset D70 Sled Forward Angled Calf Raise: poses + props + rig.
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


# D70 - gemelos inclinado al frente: el atleta se para en la plataforma del banco a 45°, apoya el pecho en la
# almohadilla y sube talones; la cadera sube con el cuerpo y la almohadilla queda fija (el pecho se desliza).
st12 = dict(ankle=[0, -60], ankle2=[-26, -64], b=40, hd=10, g=1, hx=150, hy=-560, ed=1, ft=45, ft2=45, sh=0,
            knee="back")
LEAN = {
    "DOWN": {**st12, "hip": [0, -470]},
    "UP": {**st12, "hip": [6, -434], "ankle": [6, -24], "ankle2": [-20, -28], "ft": 15, "ft2": 15},
    "HALF_BAD": {**st12, "hip": [3, -452], "ankle": [3, -42], "ankle2": [-23, -46], "ft": 30, "ft2": 30},
    "KNEE_BAD": {**st12, "hip": [10, -420], "b": 46},
    "LEAN_BAD": {**st12, "hip": [0, -470], "b": 22, "hd": -6},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-forward-angled-calf-raise", "Sled Forward Angled Calf Raise", "GIMNASIO · PIERNAS",
         ["Gemelos", "Sóleo"], rig(520, 0.95),
         [{"type": "backext45", "foot": [0, -60], "pad": [140, -640], "roll": False, "ang": 45}],
         LEAN, "DOWN",
         ("Gemelos inclinado al frente: parate en la plataforma del banco a 45 grados, apoyá el pecho en la "
          "almohadilla y subí los talones estirando los tobillos. Bajá controlando hasta sentir el estiramiento, "
          "sin doblar las rodillas."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
