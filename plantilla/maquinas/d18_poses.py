# Dataset D35 Lever Shoulder Press V3 y D36 Lever Calf Press: poses + props + rig.
import sys, os, json, math
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


# D35 - press de hombros bilateral, empuje casi vertical: espalda apoyada, codos abajo
sp = dict(hip=[-240, -232], ankle=[0, 0], ft=0, g=0, b=-3, hd=3)
spress = {
    "DOWN": {**sp, "ua": 42, "fa": 138},
    "MID": {**sp, "ua": 90, "fa": 84},
    "UP": {**sp, "ua": 168, "fa": 8},
    "ARCH_BAD": {**sp, "hip": [-228, -238], "b": -23, "hd": -12, "cv": -30, "ua": 172, "fa": 6},
    "LOW_BAD": {**sp, "ua": -26, "fa": 198},
    "LOCK_BAD": {**sp, "ua": 186, "fa": -12},
}

# D36 - prensa de gemelos: punta de los pies en la almohadilla y empuje hacia abajo
cp = dict(hip=[-240, -345], b=4, hd=6, g=1, hx=-40, hy=-420, ed=1)
calf = {
    "DOWN": {**cp, "ankle": [-37.8, -98.6], "ft": -24},
    "MID": {**cp, "ankle": [-27.5, -134.8], "ft": 4},
    "UP": {**cp, "ankle": [1.0, -163.3], "ft": 34},
    "PUSH_BAD": {**cp, "b": 34, "hd": 44, "hx": 20, "hy": -400, "ankle": [-3.6, -160.4], "ft": 30, "cv": 20},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-shoulder-press-v-3", "Lever Shoulder Press V3", "GIMNASIO · HOMBROS",
         ["Hombros", "Tríceps"], rig(700, 0.64),
         [{"type": "shoulderpress", "pivot": [-560, -580], "frameTop": -1150, "stack": -640,
           "seat": [-380, -100, -196], "back": [-340, 4, 440], "pin": 6}],
         spress, "DOWN",
         ("Sentate con la espalda apoyada y las manos en las manijas, a la altura del hombro. Empujá casi vertical, "
          "sin sacar la espalda del respaldo, pausá arriba y bajá controlado.")),
        ("lever-calf-press", "Lever Calf Press", "GIMNASIO · PIERNAS",
         ["Gemelos", "Sóleo"], rig(660, 0.8),
         [{"type": "seatedcalf", "step": [20, 180, -96], "seat": [-380, -60, -300], "stack": -620,
           "pivot": [300, -200], "pin": 6, "k": 1.6}],
         calf, "MID",
         ("Sentate con las puntas de los pies en la almohadilla y los talones en el aire. Empujá la almohadilla "
          "hacia abajo estirando los tobillos, pausá abajo y volvé lento dejando subir los talones."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
