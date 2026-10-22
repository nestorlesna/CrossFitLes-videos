# Lote 4 · cadera y gemelos: poses + props + rig.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}

# ── HIP THRUST MACHINE ── omóplatos fijos en el respaldo, la cadera gira alrededor del hombro
SH = (-330, -300)
def ht(deg_below, ankle=(200, 0), **k):
    a = rad(deg_below); H = (round(SH[0] + math.cos(a) * 280, 1), round(SH[1] + math.sin(a) * 280, 1))
    b = round(deg(math.atan2(SH[0] - H[0], -(SH[1] - H[1]))), 1)
    p = {"hip": list(H), "ankle": list(ankle), "b": b, "hd": b - 10, "ft": 0, "g": 0, "ua": round(-b - 8, 1), "fa": 26}
    p.update(k); return p
HT = {
    "DOWN": ht(44), "MID": ht(22), "UP": ht(0),
    "ARCH_BAD": {**ht(-12), "cv": -34, "hd": -130},
    "TOES_BAD": ht(0, ankle=(200, -40), ft=40),
    "FAR_BAD": ht(0, ankle=(300, 0)),
}
print("hip thrust"); check(HT)
base_spec("hip-thrust-machine", "GIMNASIO · GLÚTEOS", ["Glúteos", "Isquiotibiales"], rig(640, 0.72),
          [{"type": "hipthrust", "back": [-320, -246], "pivot": [330, -560], "stack": -700, "seat": [-250, -40, -56], "pin": 6}], HT, "DOWN")

# ── ABDUCTORES / ADUCTORES ── sentado reclinado, pies en los apoyos; ll = escorzo de las piernas que se abren
sit = dict(hip=[-240, -345], ankle=[20, -120], b=-18, hd=-8, ft=0, g=1, hx=-170, hy=-330, ed=1)
AB = {
    "CLOSED": {**sit, "cs": 0}, "MID": {**sit, "cs": 0.5}, "OPEN": {**sit, "cs": 1},
    "BOUNCE_BAD": {**sit, "cs": 1.15},
    "BACK_BAD": {**sit, "cs": 1, "b": 14, "hd": 24, "cv": 22, "hx": -150},
}
print("abduction"); check(AB)
base_spec("hip-abduction-machine", "GIMNASIO · GLÚTEOS", ["Glúteo medio"], rig(700, 0.8),
          [{"type": "hipabduction", "seat": [-380, -60, -300], "back": [-326, -18, 450], "stack": -620, "rest": [20, -120], "pin": 5, "k": 160}], AB, "CLOSED")
AD = {
    "OPEN": {**sit, "cs": 1}, "MID": {**sit, "cs": 0.5}, "CLOSED": {**sit, "cs": 0},
    "WIDE_BAD": {**sit, "cs": 1.35},
    "BACK_BAD": {**sit, "cs": 0, "b": 14, "hd": 24, "cv": 22, "hx": -150},
}
base_spec("hip-adduction-machine", "GIMNASIO · PIERNAS", ["Aductores"], rig(700, 0.8),
          [{"type": "hipadduction", "seat": [-380, -60, -300], "back": [-326, -18, 450], "stack": -620, "rest": [20, -120], "pin": 5, "k": 160, "open": 1}], AD, "OPEN")

# ── GEMELOS DE PIE ── la punta del pie fija en el borde del escalón, el tobillo sube y baja
BALL = (70, 34)  # punta (base del dedo) en coordenadas del pie
def onstep(edge, ft, knee=466, **k):
    c, s_ = math.cos(rad(ft)), math.sin(rad(ft))
    rb = (BALL[0] * c - BALL[1] * s_, BALL[0] * s_ + BALL[1] * c)
    A = (round(edge[0] - rb[0], 1), round(edge[1] - rb[1], 1))
    p = {"hip": [A[0] - 8, A[1] - knee], "ankle": list(A), "ft": ft, "b": 0, "hd": 2, "g": 0, "ua": 4, "fa": 12}
    p.update(k); return p
STEP = (30, -70)
def sc(ft, **k):
    p = onstep(STEP, ft, **k); S = add(tuple(p["hip"]), up(p.get("b", 0), TORSO))
    return p
CS = {"DOWN": sc(-22), "MID": sc(4), "UP": sc(34),
      "KNEES_BAD": {**sc(10, knee=400)}, "ARCH_BAD": onstep((130, -70), 0), "SHORT_BAD": sc(12)}
print("standing calf"); check(CS)
base_spec("standing-calf-raise-machine", "GIMNASIO · PIERNAS", ["Gemelos", "Sóleo"], rig(600, 0.62),
          [{"type": "standingcalf", "step": [-35, 190, -70], "stack": -560, "column": -220, "padX": round(CS["MID"]["hip"][0] + 8), "pin": 6, "k": 1.6}], CS, "DOWN")

# ── GEMELOS SENTADO ── cadera fija, la punta en el escalón; la rodilla sube con el talón
STEP2 = (40, -96)
def ss(ft, **k):
    c, s_ = math.cos(rad(ft)), math.sin(rad(ft))
    rb = (BALL[0] * c - BALL[1] * s_, BALL[0] * s_ + BALL[1] * c)
    A = (round(STEP2[0] - rb[0], 1), round(STEP2[1] - rb[1], 1))
    p = {"hip": [-240, -345], "ankle": list(A), "ft": ft, "b": 4, "hd": 6, "g": 1, "hx": -40, "hy": -420, "ed": 1}
    p.update(k); return p
SC = {"DOWN": ss(-24), "MID": ss(4), "UP": ss(34), "PUSH_BAD": ss(30, b=34, hd=44, cv=20, hx=20, hy=-400)}
print("seated calf"); check(SC)
base_spec("seated-calf-raise-machine", "GIMNASIO · PIERNAS", ["Sóleo", "Gemelos"], rig(680, 0.8),
          [{"type": "seatedcalf", "step": [20, 180, -96], "seat": [-380, -60, -300], "stack": -600, "pivot": [300, -200], "pin": 5, "k": 1.6}], SC, "DOWN")
