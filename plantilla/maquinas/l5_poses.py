# Lote 5 · Smith, asistidas y core: poses + props + rig.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}

# ── SMITH SQUAT ── la barra (en la espalda) baja en línea recta en x = 0; pies apenas adelante
FX, DY = -34, 18
def sq(hy, b, ankle=(70, 0), **k):
    # cadera ubicada para que el punto de la barra quede en x = 0
    off = up(b, TORSO)[0] + math.cos(rad(b)) * FX - math.sin(rad(b)) * DY
    p = {"hip": [round(-off, 1), hy], "ankle": list(ankle), "b": b, "hd": round(b * 0.4, 1), "ft": 0, "g": 0, "ua": round(-b - 12, 1), "fa": 178}
    p.update(k); return p
SQ = {"TOP": sq(-462, 6), "MID": sq(-360, 18), "BOTTOM": sq(-262, 30),
      "FWD_BAD": sq(-300, 2, ankle=(250, 0)), "BACK_BAD": sq(-280, 44, ankle=(-40, 0)),
      "HEELS_BAD": sq(-262, 30, ankle=(80, -40), ft=28)}
print("smith squat"); check(SQ)
base_spec("smith-machine-squat", "GIMNASIO · PIERNAS", ["Cuádriceps", "Glúteos"], rig(560, 0.68),
          [{"type": "smith", "x": 0, "top": -1100, "stops": -440, "track": "back", "torso": [FX, DY], "r": 70}], SQ, "TOP")

# ── SMITH BENCH ── acostado en el banco, la barra baja en x = -200 (mitad del pecho)
BX = -200
def bp(hand_y, hip=(0, -196), **k):
    p = {"hip": list(hip), "ankle": [hip[0] + 250, 0], "b": -90, "hd": -92, "ft": 0, "g": 1, "hx": BX, "hy": hand_y, "ed": 1}
    p.update(k); return p
BP = {"TOP": bp(-516), "MID": bp(-400), "BOTTOM": bp(-292),
      "NECK_BAD": bp(-292, hip=(90, -196)), "BUTT_BAD": bp(-330, hip=(0, -262), b=-104, hd=-100, cv=-20)}
print("smith bench"); check(BP)
base_spec("smith-machine-bench-press", "GIMNASIO · PECHO", ["Pectorales", "Tríceps"], rig(600, 0.7),
          [{"type": "bench", "x0": -560, "x1": 120, "h": 200},
           {"type": "smith", "x": BX, "top": -1180, "stops": -300, "track": "hands", "r": 70}], BP, "TOP")

# ── ASSISTED PULL-UP ── arrodillado en la plataforma, manijas altas en GP
GP = (60, -1240)
def pu(S, b, **k):
    H = (S[0] - up(b, TORSO)[0], S[1] - up(b, TORSO)[1])
    p = {"hip": [round(H[0], 1), round(H[1], 1)], "s": 92, "t": 4, "b": b, "hd": b, "ft": 80, "g": 1, "hx": GP[0], "hy": GP[1], "ed": -1}
    p.update(k); return p
APU = {"HANG": pu((GP[0] - 50, GP[1] + 318), -6), "MID": pu((GP[0] - 80, GP[1] + 200), -10), "TOP": pu((GP[0] - 90, GP[1] + 70), -12),
       "KIP_BAD": pu((GP[0] - 40, GP[1] + 200), -26, t=40, s=120)}
for k, v in APU.items(): v["K"] = None
print("assisted pull-up"); APU = {k: {kk: vv for kk, vv in v.items() if kk != "K"} for k, v in APU.items()}; check(APU)
KTOP = fk(APU["TOP"])["K"][1]
base_spec("assisted-pull-up-machine", "GIMNASIO · ESPALDA", ["Dorsales", "Bíceps"], rig(560, 0.58),
          [{"type": "assisted", "stack": 420, "grip": list(GP), "dip": [60, -760], "pivot": [300, -260], "rest": round(KTOP), "pin": 6, "k": 1}], APU, "HANG")

# ── ASSISTED DIP ── manos en las paralelas DP, rodillas en la plataforma
DP = (60, -760)
def dp(drop, b=10, **k):
    S = (DP[0] - 30, DP[1] - 322 + drop)
    H = (S[0] - up(b, TORSO)[0], S[1] - up(b, TORSO)[1])
    p = {"hip": [round(H[0], 1), round(H[1], 1)], "s": 92, "t": 4, "b": b, "hd": b, "ft": 80, "g": 1, "hx": DP[0], "hy": DP[1] + 10, "ed": -1}
    p.update(k); return p
ADP = {"TOP": dp(0), "MID": dp(90), "BOTTOM": dp(160, b=18), "DEEP_BAD": dp(250, b=22), "SHRUG_BAD": dp(160, b=18, hd=50, cv=26)}
print("assisted dip"); check(ADP)
KTOP = fk(ADP["TOP"])["K"][1]
base_spec("assisted-dip-machine", "GIMNASIO · PECHO", ["Pecho", "Tríceps"], rig(560, 0.58),
          [{"type": "assisted", "stack": 420, "grip": list(GP), "dip": list(DP), "pivot": [300, -260], "rest": round(KTOP), "pin": 6, "k": 1}], ADP, "TOP")

# ── AB CRUNCH ── sentado, pies trabados, el tronco se enrolla
sit = dict(hip=[-240, -230], ankle=[60, -20], ft=0, g=0)
AC = {"UP": {**sit, "b": -6, "hd": -2, "ua": 24, "fa": 150}, "MID": {**sit, "b": 14, "hd": 24, "cv": 14, "ua": 44, "fa": 150},
      "CRUNCH": {**sit, "b": 32, "hd": 52, "cv": 30, "ua": 62, "fa": 150},
      "ARMS_BAD": {**sit, "b": 14, "hd": 14, "ua": 70, "fa": 40}, "NECK_BAD": {**sit, "b": 8, "hd": 80, "ua": 38, "fa": 150}}
print("ab crunch"); check(AC)
base_spec("ab-crunch-machine", "GIMNASIO · CORE", ["Abdominales"], rig(720, 0.66),
          [{"type": "abcrunch", "seat": [-390, -90, -184], "pivot": [-300, -820], "stack": -640, "feet": [60, -20], "pin": 5}], AC, "UP")

# ── 45° BACK EXTENSION ── piernas a 45°, cadera sobre la almohadilla
A = (0, -60); U = (math.sin(rad(45)), -math.cos(rad(45)))
H = (round(A[0] + U[0] * 466, 1), round(A[1] + U[1] * 466, 1))
be = dict(hip=list(H), ankle=list(A), ft=45, g=0)
def arms(b): return {"ua": round(-b + 26, 1), "fa": 140}
BE = {"TOP": {**be, "b": 45, "hd": 50, **arms(45)}, "MID": {**be, "b": 100, "hd": 110, **arms(100)}, "BOTTOM": {**be, "b": 140, "hd": 155, **arms(140)},
      "HYPER_BAD": {**be, "b": 12, "hd": 0, "cv": -20, **arms(12)}, "ROUND_BAD": {**be, "b": 140, "hd": 170, "cv": 44, **arms(140)}}
print("back ext", H); check(BE)
PAD = (round(H[0] + 0.707 * 62 - U[0] * 20), round(H[1] + 0.707 * 62 - U[1] * 20))
ROLL = (round(A[0] + U[0] * 150 - 0.707 * 52), round(A[1] + U[1] * 150 - 0.707 * 52))
base_spec("back-extension-45", "GIMNASIO · ESPALDA BAJA", ["Lumbares", "Glúteos"], rig(470, 0.74),
          [{"type": "backext45", "foot": list(A), "pad": list(PAD), "roll": list(ROLL), "ang": 45}], BE, "TOP",
          extra={"nombreEnVoz": "Forty five degree back extension"})
