# Dataset D01 · D25 Lever Reverse Grip Preacher Curl y D26 Lever Seated Calf Press: poses + props + rig.
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


# ── D25 ── curl Scott con agarre prono (manos como martillo invertido) ──
pc = dict(hip=[-240, -230], ankle=[0, 0], ft=0, g=0, b=14, hd=12, ua=42)
rev = {
    "DOWN": {**pc, "fa": 22, "wr": -90},
    "MID": {**pc, "fa": 80, "wr": -90},
    "UP": {**pc, "fa": 132, "wr": -90},
    "OFF_BAD": {"hip": [-240, -230], "ankle": [0, 0], "ft": 0, "g": 0, "b": 2, "hd": 2, "ua": 14, "fa": 120, "wr": -90},
    "DROP_BAD": {**pc, "fa": -4, "wr": -90},
    "SWING_BAD": {"hip": [-240, -230], "ankle": [0, 0], "ft": 0, "g": 0, "b": -10, "hd": -6, "ua": 30, "fa": 128, "wr": -90},
}

# ── D26 ── prensa de gemelos sentado: almohadilla sobre los muslos y punta del pie en el escalón ──
cl = dict(hip=[-240, -345], b=4, hd=6, g=1, hx=-40, hy=-420, ed=1)
calf = {
    "DOWN": {**cl, "ankle": [-37.8, -98.6], "ft": -24},
    "MID": {**cl, "ankle": [-27.5, -134.8], "ft": 4},
    "UP": {**cl, "ankle": [1.0, -163.3], "ft": 34},
    "PUSH_BAD": {"hip": [-240, -345], "b": 34, "hd": 44, "g": 1, "hx": 20, "hy": -400, "ed": 1,
                 "ankle": [-3.6, -160.4], "ft": 30, "cv": 20},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-reverse-grip-preacher-curl", "Lever Reverse Grip Preacher Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Antebrazos"], rig(720, 0.66),
         [{"type": "preachercurl", "pivot": [-57, -374], "frameTop": -1000, "stack": -660,
           "seat": [-390, -90, -184], "pad": [-192, -457, -79, -333], "pin": 5}],
         rev, "DOWN",
         ("Sentate en la máquina de curl Scott con las axilas en el borde del apoyo. Con agarre prono "
          "(palmas hacia abajo), flexioná los codos llevando las manijas a los hombros y bajá lento, "
          "sin despegar los brazos y sin estirar de golpe.")),
        ("lever-seated-calf-press", "Lever Seated Calf Press", "GIMNASIO · PIERNAS",
         ["Sóleo", "Gemelos"], rig(680, 0.8),
         [{"type": "seatedcalf", "step": [20, 180, -96], "seat": [-380, -60, -300],
           "stack": -600, "pivot": [300, -200], "pin": 5, "k": 1.6}],
         calf, "DOWN",
         ("Ajustá el asiento para que las rodillas queden debajo de la almohadilla y la punta de los pies "
          "en el escalón, con el talón en el aire. Destrabá la palanca, bajá el talón despacio y subí "
          "lo más alto posible apretando el sóleo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
