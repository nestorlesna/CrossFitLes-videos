# Lote 2 · poleas: poses + props + rig.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}

# ── CABLE TRICEPS PUSHDOWN ── polea alta adelante, barra
st = dict(b=8, hd=6, g=0, ft=0)
TP = {
    "UP": {**st, "ua": 10, "fa": 82},
    "MID": {**st, "ua": 8, "fa": 42},
    "DOWN": {**st, "ua": 4, "fa": 2},
    "ELBOWS_BAD": {**st, "ua": 48, "fa": 52},
    "LEAN_BAD": {**st, "b": 34, "hd": 38, "ua": 30, "fa": 20},
    "HIGH_BAD": {**st, "ua": 6, "fa": 150},
}
print("pushdown"); check(TP)
base_spec("cable-triceps-pushdown", "GIMNASIO · BRAZOS", ["Tríceps"], rig(420, 0.62),
          [{"type": "cable", "x": 400, "top": -1220, "pulley": [230, -1110], "track": 268, "att": "bar", "pin": 5}], TP, "UP")

# ── CABLE BICEP CURL ── polea baja adelante, barra
st = dict(b=2, hd=2, g=0, ft=0)
BC = {
    "DOWN": {**st, "ua": 3, "fa": 8},
    "MID": {**st, "ua": 4, "fa": 80},
    "UP": {**st, "ua": 6, "fa": 140},
    "ELBOWS_BAD": {**st, "ua": 50, "fa": 112},
    "SWING_BAD": {**st, "b": -18, "hd": -10, "ua": 12, "fa": 132, "rx": -12},
    "FAR_BAD": {**st, "b": 10, "hd": 8, "ua": 26, "fa": 30, "rx": -230},
}
print("bicep curl"); check(BC)
base_spec("cable-bicep-curl", "GIMNASIO · BRAZOS", ["Bíceps"], rig(420, 0.66),
          [{"type": "cable", "x": 400, "top": -1100, "pulley": [230, -70], "track": 268, "att": "bar", "pin": 6}], BC, "DOWN")

# ── CABLE FACE PULL ── polea a la altura de la cara, soga, un paso atrás
st = dict(b=-4, hd=0, g=0, ft=0, rx=-60)
FP = {
    "EXT": {**st, "ua": 82, "fa": 4},
    "MID": {**st, "ua": 86, "fa": 56, "ul": 0.65},
    "PULL": {**st, "ua": 90, "fa": 112, "ul": 0.28},
    "LEAN_BAD": {**st, "b": -26, "hd": -16, "ua": 70, "fa": 70, "ul": 0.6},
    "LOW_BAD": {**st, "ua": 18, "fa": 88},
    "ARCH_BAD": {**st, "b": -14, "hd": -8, "cv": -34, "ua": 90, "fa": 112, "ul": 0.28},
}
print("face pull"); check(FP)
base_spec("cable-face-pull", "GIMNASIO · HOMBROS", ["Hombros", "Espalda alta"], rig(400, 0.66),
          [{"type": "cable", "x": 440, "top": -1100, "pulley": [270, -800], "track": 308, "att": "rope", "pin": 4}], FP, "EXT")

# ── SEATED CABLE ROW ── banco bajo, pies en el apoyo, polea baja
H = [-300, -216]; A = [110, -130]
sr = dict(hip=H, ankle=A, ft=-62, g=1, ed=-1)
def rowp(b, hand, **k):
    S = add(tuple(H), up(b, TORSO)); return {**sr, "b": b, "hd": b + 4, "hx": round(S[0] + hand[0], 1), "hy": round(S[1] + hand[1], 1), **k}
SR = {
    "EXT": rowp(16, (318, 70)),
    "MID": rowp(4, (210, 150)),
    "PULL": rowp(-4, (96, 196)),
    "SWING_BAD": rowp(-30, (90, 170), hd=-26),
    "ROUND_BAD": rowp(44, (300, 70), hd=64, cv=34),
    "SHRUG_BAD": rowp(-4, (110, 70), hd=-8, ed=1),
}
print("cable row"); check(SR)
base_spec("seated-cable-row", "GIMNASIO · ESPALDA", ["Dorsales", "Romboides"], rig(560, 0.72),
          [{"type": "cablerow", "x": 470, "top": -900, "pulley": [306, -236], "track": 340, "att": "handle", "pin": 6,
            "seat": [-500, -150, -170], "foot": [112, -116], "ang": -24}], SR, "EXT")

# ── CABLE CROSSOVER ── pies escalonados, poleas altas detrás
cs = dict(hip=[0, -455], ankle=[80, 0], ankle2=[-110, 0], ft=0, ft2=20, b=16, hd=12, g=0)
CX = {
    "OPEN": {**cs, "ua": 72, "fa": -4, "al": 0.32},
    "MID": {**cs, "ua": 62, "fa": 2, "al": 0.72},
    "CLOSED": {**cs, "ua": 36, "fa": 14, "al": 1},
    "BACK_BAD": {**cs, "ua": 112, "fa": -24, "al": 0.22, "hd": 6},
    "PRESS_BAD": {**cs, "ua": 30, "fa": 118, "al": 1},
    "BODY_BAD": {**cs, "b": 44, "hd": 48, "ua": 40, "fa": 10, "al": 1, "hip": [20, -440]},
}
print("crossover"); check(CX)
base_spec("cable-crossover", "GIMNASIO · PECHO", ["Pectorales"], rig(600, 0.6),
          [{"type": "cablecrossover", "x": -300, "top": -1300, "pulley": [-196, -1200], "pin": 4}], CX, "OPEN")
