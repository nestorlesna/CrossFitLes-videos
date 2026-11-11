# Dataset D37 Lever Donkey Calf Raise y D38 Lever Rotary Calf: poses + props + rig.
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


# D37 - gemelos tipo donkey: tronco inclinado bajo la almohadilla, punta de los pies en el escalón
BALL = (70, 34)
STEP = (30, -74)


def dk_onstep(edge, ft, knee=470, **k):
    c, s_ = math.cos(rad(ft)), math.sin(rad(ft))
    rb = (BALL[0] * c - BALL[1] * s_, BALL[0] * s_ + BALL[1] * c)
    A = (round(edge[0] - rb[0], 1), round(edge[1] - rb[1], 1))
    p = {"hip": [A[0] - 10, A[1] - knee], "ankle": list(A), "ft": ft, "b": 58, "hd": 44,
         "g": 0, "ua": 2, "fa": 6}
    p.update(k); return p


def dk(ft, **k): return dk_onstep(STEP, ft, **k)


DONKEY = {
    "DOWN": dk(-26), "MID": dk(2), "UP": dk(34),
    "KNEES_BAD": dk(8, knee=392),
    "ROUND_BAD": {**dk(8), "cv": 34, "hd": 70},
    "SHORT_BAD": dk(14),
}

# D38 - gemelos rotatorio: sentado con las rodillas algo flexionadas, punta en la placa
STEP3 = (40, -30)
BALL3 = (70, 34)


def rc(ft, **k):
    c, s_ = math.cos(rad(ft)), math.sin(rad(ft))
    rb = (BALL3[0] * c - BALL3[1] * s_, BALL3[0] * s_ + BALL3[1] * c)
    A = (round(STEP3[0] - rb[0], 1), round(STEP3[1] - rb[1], 1))
    p = {"hip": [-240, -345], "ankle": list(A), "ft": ft, "b": 8, "hd": 6,
         "g": 1, "hx": -60, "hy": -480, "ed": -1}
    p.update(k); return p


ROTARY = {
    "DOWN": rc(-22), "MID": rc(2), "UP": rc(32),
    "PUSH_BAD": rc(28, b=34, hd=44, cv=22, hx=40, hy=-440),
    "SHORT_BAD": rc(10),
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-donkey-calf-raise", "Lever Donkey Calf Raise", "GIMNASIO · PIERNAS",
         ["Gemelos", "Sóleo"], rig(610, 0.62),
         [{"type": "standingcalf", "step": [-35, 190, -74], "stack": -560, "column": -220, "top": -1020,
           "padX": round(fk(DONKEY["MID"])["H"][0] - 30), "padAt": "hip", "pin": 6, "k": 1.6}],
         DONKEY, "DOWN",
         ("Apoyate inclinado bajo la almohadilla con la punta de los pies en el escalón y los talones en el aire. "
          "Levantá los talones lo más alto posible, pausá arriba y bajá lento hasta estirar la pantorrilla.")),
        ("lever-rotary-calf", "Lever Rotary Calf", "GIMNASIO · PIERNAS",
         ["Gemelos", "Sóleo"], rig(640, 0.78),
         [{"type": "seatedcalf", "step": [-40, 200, -30], "seat": [-360, -40, -320], "stack": -660, "top": -800,
           "pivot": [330, -150], "pin": 6, "k": 1.6}],
         ROTARY, "DOWN",
         ("Sentate con las rodillas algo flexionadas y la punta de los pies en la placa, con los talones fuera del "
          "borde. Empujá con la parte delantera del pie, pausá arriba y bajá lento dejando caer los talones."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
