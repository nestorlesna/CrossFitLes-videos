# Lote 3 · tren superior sentado: poses + props + rig.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}
HIP, ANK = [-240, -230], [0, 0]
sit = dict(hip=HIP, ankle=ANK, ft=0, g=0)
def sh(b): return add(tuple(HIP), up(b, TORSO))
SEAT = [-390, -90, -184]

# ── MACHINE CHEST PRESS ──
b = -6; S = sh(b)
CP = {
    "BACK": {**sit, "b": b, "hd": 0, "ua": -18, "fa": 112},
    "MID": {**sit, "b": b, "hd": 0, "ua": 20, "fa": 72},
    "OUT": {**sit, "b": b, "hd": 0, "ua": 78, "fa": 8},
    "SEAT_BAD": {**sit, "b": b, "hd": 0, "ua": -60, "fa": 170},
    "BACK_BAD": {**sit, "b": 24, "hd": 22, "cv": 24, "ua": 70, "fa": 10},
    "LOCK_BAD": {**sit, "b": b, "hd": 0, "ua": 84, "fa": -8},
}
print("chest press", S); check(CP)
base_spec("machine-chest-press", "GIMNASIO · PECHO", ["Pectorales", "Tríceps"], rig(740, 0.66),
          [{"type": "chestpress", "pivot": [-30, -1010], "frameTop": -1070, "stack": -640, "seat": SEAT, "back": [-318, b, 470], "pin": 5}], CP, "BACK")

# ── MACHINE SHOULDER PRESS ──
b = -4; S = sh(b)
SP = {
    "DOWN": {**sit, "b": b, "hd": 0, "ua": 12, "fa": 166},
    "MID": {**sit, "b": b, "hd": 0, "ua": 92, "fa": 84},
    "UP": {**sit, "b": b, "hd": 0, "ua": 168, "fa": 8},
    "ARCH_BAD": {**sit, "b": -22, "hd": -12, "cv": -30, "ua": 172, "fa": 6, "hip": [-226, -236]},
    "LOW_BAD": {**sit, "b": b, "hd": 0, "ua": -22, "fa": 196},
    "LOCK_BAD": {**sit, "b": b, "hd": 0, "ua": 178, "fa": -6},
}
print("shoulder press", S); check(SP)
base_spec("machine-shoulder-press", "GIMNASIO · HOMBROS", ["Hombros", "Tríceps"], rig(720, 0.66),
          [{"type": "shoulderpress", "pivot": [-520, -620], "frameTop": -1080, "stack": -660, "seat": SEAT, "back": [-318, b, 470], "pin": 5}], SP, "DOWN")

# ── PEC DECK FLY ──
b = -4; S = sh(b)
PD = {
    "OPEN": {**sit, "b": b, "hd": 0, "ua": 84, "fa": -6, "al": 0.3},
    "MID": {**sit, "b": b, "hd": 0, "ua": 84, "fa": -4, "al": 0.72},
    "CLOSED": {**sit, "b": b, "hd": 0, "ua": 84, "fa": -2, "al": 1},
    "BACK_BAD": {**sit, "b": b, "hd": 0, "ua": 96, "fa": -10, "al": 0.12},
    "PRESS_BAD": {**sit, "b": b, "hd": 0, "ua": 40, "fa": 100, "al": 1},
    "SHRUG_BAD": {**sit, "b": 10, "hd": 18, "cv": 18, "ua": 90, "fa": -2, "al": 1},
}
print("pec deck", S); check(PD)
base_spec("pec-deck-fly", "GIMNASIO · PECHO", ["Pectorales"], rig(740, 0.66),
          [{"type": "pecdeck", "pivot": [round(S[0] + 30), round(S[1] - 330)], "frameTop": -1060, "stack": -640, "seat": SEAT, "back": [-318, b, 470], "pin": 4}], PD, "OPEN")

# ── MACHINE LATERAL RAISE ── sentado de frente al apoyo de pecho, eje en el hombro
b = 6; S = sh(b)
LR = {
    "DOWN": {**sit, "b": b, "hd": 4, "ua": 4, "fa": 14},
    "MID": {**sit, "b": b, "hd": 4, "ua": 50, "fa": 20, "al": 0.6},
    "UP": {**sit, "b": b, "hd": 4, "ua": 88, "fa": 20, "al": 0.24},
    "HIGH_BAD": {**sit, "b": b, "hd": 4, "ua": 150, "fa": 10, "al": 0.24},
    "SHRUG_BAD": {**sit, "b": b, "hd": 18, "cv": 10, "ua": 88, "fa": 20, "al": 0.24, "hip": [-240, -250]},
    "SWING_BAD": {**sit, "b": -18, "hd": -10, "ua": 90, "fa": 20, "al": 0.24},
}
print("lateral raise", S); check(LR)
base_spec("machine-lateral-raise", "GIMNASIO · HOMBROS", ["Hombros"], rig(720, 0.66),
          [{"type": "lateralraise", "pivot": [round(S[0]), round(S[1])], "frameTop": -1000, "stack": -660, "seat": SEAT,
            "chest": [round(S[0] + 92), round(S[1] + 150)], "pin": 4, "k": 1.4}], LR, "DOWN")

# ── MACHINE PREACHER CURL ── brazos sobre el apoyo inclinado, codo en el eje
b = 14; S = sh(b); UA = 42
E = add(S, down(UA, UPPER)); d = (math.sin(rad(UA)), math.cos(rad(UA))); n = (-d[1], d[0])
pad = [round(S[0] + d[0] * 20 + n[0] * 44), round(S[1] + d[1] * 20 + n[1] * 44), round(E[0] + d[0] * 16 + n[0] * 44), round(E[1] + d[1] * 16 + n[1] * 44)]
pc = dict(sit, b=b, hd=12, ua=UA)
PC = {
    "DOWN": {**pc, "fa": 22},
    "MID": {**pc, "fa": 80},
    "UP": {**pc, "fa": 132},
    "OFF_BAD": {**pc, "ua": 14, "fa": 120, "b": 2, "hd": 2},
    "DROP_BAD": {**pc, "fa": -4},
    "SWING_BAD": {**pc, "b": -10, "hd": -6, "fa": 128, "ua": 30},
}
print("preacher", S, E, pad); check(PC)
base_spec("machine-preacher-curl", "GIMNASIO · BRAZOS", ["Bíceps"], rig(720, 0.66),
          [{"type": "preachercurl", "pivot": [round(E[0]), round(E[1])], "frameTop": -1000, "stack": -660, "seat": SEAT, "pad": pad, "pin": 5}], PC, "DOWN")
