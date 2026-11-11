# Dataset D39 Cycle Cross Trainer y D40 Lever Bicep Curl: poses + props + rig.
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


# D39 - elíptico: el pie recorre una elipse y las manos van y vienen en las manijas
EC, ERX, ERY = (46, -190), 104, 42


def ell(th, **k):
    a = rad(th)
    A1 = (EC[0] + ERX * math.cos(a), EC[1] + ERY * math.sin(a))
    A2 = (EC[0] - ERX * math.cos(a), EC[1] - ERY * math.sin(a))
    sw = math.cos(a)
    p = {"hip": [0, round(-628 + 8 * math.sin(2 * a), 1)],
         "ankle": [round(A1[0], 1), round(A1[1], 1)], "ankle2": [round(A2[0], 1), round(A2[1], 1)],
         "ft": round(-8 * sw, 1), "ft2": round(8 * sw, 1), "b": 4, "hd": 2, "g": 1, "g2": 1, "ed": -1, "ed2": -1,
         "hx": round(150 - 70 * sw, 1), "hy": -824, "hx2": round(150 + 70 * sw, 1), "hy2": -824}
    p.update(k); return p


EL = {f"E{i}": ell(i * 60) for i in range(6)}
EL["LEAN_BAD"] = ell(0, b=34, hd=24, hip=[20, -604])
EL["TOES_BAD"] = ell(180, ft=30, ft2=30)

# D40 - curl sentado en máquina de palanca: codo fijo en el eje, el antebrazo sube con las manijas
pc = dict(hip=[-240, -232], ankle=[0, 0], ft=0, g=0, b=-5, hd=8, ua=38)
CURL = {
    "DOWN": {**pc, "fa": -22},
    "MID": {**pc, "fa": 48},
    "UP": {**pc, "fa": 100},
    "ELBOW_BAD": {**pc, "ua": 62, "fa": -2},
    "SWING_BAD": {**pc, "b": -20, "hd": -12, "fa": 96},
    "DROP_BAD": {**pc, "fa": -52},
}
PIVOT = [round(fk(CURL["DOWN"])["E"][0]), round(fk(CURL["DOWN"])["E"][1])]

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("cycle-cross-trainer", "Cycle Cross Trainer", "GIMNASIO · CARDIO",
         ["Cardio", "Cuerpo completo"], rig(486, 0.77),
         [{"type": "elliptical", "fly": [372, -182], "pivot": [342, -440], "x0": -392}],
         EL, "E0",
         ("Subite con la máquina quieta, con los pies completos en los pedales y las manos en las manijas. "
          "Pedaleá con un movimiento continuo empujando y tirando de las manijas, con el tronco erguido.")),
        ("lever-bicep-curl", "Lever Bicep Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Antebrazos"], rig(700, 0.66),
         [{"type": "preachercurl", "pivot": PIVOT, "frameTop": -780, "stack": -660,
           "seat": [-390, -100, -196], "back": [-330, 2, 420], "pin": 5}],
         CURL, "DOWN",
         ("Sentate con la espalda apoyada y los codos pegados al eje de la máquina, con las palmas hacia arriba. "
          "Flexioná los codos llevando las manijas hacia los hombros y bajá lento hasta estirar sin soltar de golpe."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
