# Dataset D33 Lever One Arm Shoulder Press y D34 Lever Shoulder Press V2: poses + props + rig.
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


# D33 - press de hombro a un brazo: el brazo lejano cuelga libre (g2 0) y solo empuja el cercano
oa = dict(hip=[-240, -230], ankle=[0, 0], ft=0, g=0, b=-4, hd=0, g2=0, ua2=10, fa2=16)
one = {
    "DOWN": {**oa, "ua": 45, "fa": 135},
    "MID": {**oa, "ua": 94, "fa": 82},
    "UP": {**oa, "ua": 170, "fa": 6},
    "ARCH_BAD": {**oa, "hip": [-226, -236], "b": -24, "hd": -14, "cv": -30, "ua": 174, "fa": 4},
    "LOW_BAD": {**oa, "ua": -24, "fa": 196},
    "LOCK_BAD": {**oa, "ua": 190, "fa": -20},
}

# D34 - press de hombros bilateral, agarre prono: el empuje va arriba y un poco adelante
sp = dict(hip=[-240, -228], ankle=[0, 0], ft=0, g=0, b=-2, hd=2)
spress = {
    "DOWN": {**sp, "ua": 40, "fa": 140},
    "MID": {**sp, "ua": 88, "fa": 86},
    "UP": {**sp, "ua": 154, "fa": 16},
    "FWD_BAD": {**sp, "ua": 112, "fa": 34},
    "ARCH_BAD": {**sp, "hip": [-228, -234], "b": -22, "hd": -10, "cv": -28, "ua": 158, "fa": 12},
    "SEP_BAD": {**sp, "b": 16, "hd": 10, "cv": 14, "ua": 118, "fa": 58},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-one-arm-shoulder-press", "Lever One Arm Shoulder Press", "GIMNASIO · HOMBROS",
         ["Hombros", "Tríceps"], rig(700, 0.66),
         [{"type": "shoulderpress", "pivot": [-520, -620], "frameTop": -1080, "stack": -660,
           "seat": [-390, -90, -184], "back": [-318, -4, 470], "pin": 3}],
         one, "DOWN",
         ("Sentate con la espalda apoyada y agarrá la manija con una sola mano, a la altura del hombro. Empujá arriba "
          "hasta estirar el brazo, pausá y bajá lento. Al terminar la serie, cambiá de brazo.")),
        ("lever-shoulder-press-v-2", "Lever Shoulder Press V2", "GIMNASIO · HOMBROS",
         ["Hombros", "Tríceps"], rig(710, 0.65),
         [{"type": "shoulderpress", "pivot": [-540, -600], "frameTop": -1120, "stack": -700,
           "seat": [-400, -80, -190], "back": [-330, -2, 470], "pin": 5}],
         spress, "DOWN",
         ("Sentate con la espalda apoyada y agarrá las manijas con agarre prono, algo más abiertas que los hombros. "
          "Empujá arriba y un poco adelante hasta estirar casi del todo, pausá y bajá controlado."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
