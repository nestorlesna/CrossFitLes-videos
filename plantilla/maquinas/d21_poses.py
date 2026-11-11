# Dataset D41 Lever Deadlift y D42 Lever Gripper Hands: poses + props + rig.
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


# D41 - prensa baja ("peso muerto" en máquina): riel casi horizontal, el carro sale con los talones
ANG = -18
DIR = (math.cos(rad(ANG)), -math.sin(rad(ANG)))
HIP = (-320, -290)


def on_rail(d): return [round(HIP[0] + DIR[0] * d, 1), round(HIP[1] + DIR[1] * d, 1)]


ld = dict(hip=list(HIP), b=-22, hd=16, g=1, hx=-270, hy=-320, ed=1, ft=-72)
DL = {
    "BOTTOM": {**ld, "ankle": on_rail(338)},
    "MID": {**ld, "ankle": on_rail(392)},
    "TOP": {**ld, "ankle": on_rail(446)},
    "LOCK_BAD": {**ld, "ankle": on_rail(466)},
    "BACK_BAD": {**ld, "ankle": on_rail(392), "hip": [-300, -298], "b": -14, "hd": 26, "cv": 24},
    "HEELS_BAD": {**ld, "ankle": on_rail(392), "ft": -40},
}

# D42 - máquina de agarre: manos al frente a la altura del pecho, el apretón se ve en la muñeca y la pila
gr = dict(hip=[-240, -232], ankle=[0, 0], ft=0, g=1, b=2, hd=0, ed=-1, hx=-55, hy=-410)
GR = {
    "OPEN": {**gr, "wr": -18},
    "GRIP": {**gr, "wr": 26},
    "BACK_BAD": {**gr, "wr": 20, "b": 16, "hd": 14, "cv": 22, "hip": [-230, -238]},
    "DROP_BAD": {**gr, "wr": -34, "hx": -66, "hy": -398},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-deadlift", "Lever Deadlift", "GIMNASIO · PIERNAS",
         ["Glúteos", "Isquiotibiales"], rig(640, 0.76),
         [{"type": "legpress", "hip": list(HIP), "ang": ANG, "lean": -22, "stops": 340}],
         DL, "BOTTOM",
         ("Sentate con la espalda apoyada, los pies planos en la plataforma y las manos en las manijas. "
          "Empujá con los talones hasta extender las caderas, apretá los glúteos arriba y bajá controlado.")),
        ("lever-gripper-hands", "Lever Gripper Hands", "GIMNASIO · ANTEBRAZOS",
         ["Antebrazos", "Agarre"], rig(700, 0.66),
         [{"type": "gripper", "hub": [-55, -410], "stack": -640, "frameTop": -1030,
           "seat": [-380, -110, -196], "pin": 5}],
         GR, "OPEN",
         ("Sentate derecho con los pies planos y las manos en el mango de la máquina de agarre. "
          "Apretá el mango contrayendo los antebrazos, sostené un segundo y soltá lento sin abrir del todo la mano."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
