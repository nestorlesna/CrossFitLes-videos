# Lote 7 · máquinas nuevas (multicadera de pie y press múltiple): poses + props + rig.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}

# ── MULTI HIP ── de pie, la pierna cercana trabaja y la lejana queda apoyada; eje de la palanca = cadera.
# bf = lado del rodillo (1 adelante, −1 atrás, 0 afuera, 2 adentro); cs = abrir (+) / cerrar (−) en la tarjeta de frente;
# by = cs de reposo (la pila sube con |cs − by|).
HIP = [0, -470]
st = dict(hip=HIP, s=0, t=0, s2=0, t2=0, ft=0, ft2=0, b=6, hd=4, g=1, hx=230, hy=-560, ed=1, cs=0, by=0)
MH = {
    # patada de glúteo hacia atrás (rodillo atrás del muslo)
    "KB_START": {**st, "bf": -1},
    "KB_MID": {**st, "bf": -1, "t": 16, "s": 40, "ft": 30},
    "KB_TOP": {**st, "bf": -1, "t": 32, "s": 62, "ft": 40, "b": 10, "hd": 8},
    "KB_BAD": {**st, "bf": -1, "t": 58, "s": 86, "ft": 46, "b": -12, "hd": -14, "cv": -26},
    # elevación de rodilla (rodillo arriba del muslo)
    "KR_START": {**st, "bf": 1},
    "KR_MID": {**st, "bf": 1, "t": -46, "s": -4, "ft": 10},
    "KR_TOP": {**st, "bf": 1, "t": -90, "s": 0, "ft": 22},
    "KR_BAD": {**st, "bf": 1, "t": -100, "s": 6, "ft": 22, "b": 24, "hd": 26, "cv": 24, "hx": 250, "hy": -540},
    # abducción (rodillo afuera de la pierna)
    "AB_START": {**st, "bf": 0},
    "AB_OUT": {**st, "bf": 0, "cs": 1},
    "AB_BAD": {**st, "bf": 0, "cs": 1.4, "b": 2},
    # aducción (rodillo adentro: arranca con la pierna abierta y cierra cruzando apenas)
    "AD_START": {**st, "bf": 2, "cs": 0.7, "by": 0.7},
    "AD_IN": {**st, "bf": 2, "cs": -0.25, "by": 0.7},
    # impulso / balanceo
    "SWING_BAD": {**st, "bf": -1, "t": 46, "s": 70, "ft": 40, "b": 30, "hd": 30, "cv": 10, "hx": 270, "hy": -520},
}
print("multi hip"); check(MH)
base_spec("multi-hip-machine", "GIMNASIO · GLÚTEOS", ["Glúteos", "Cadera"], rig(690, 0.66),
          [{"type": "multihip", "pivot": HIP, "stack": -520, "at": 210, "handle": [230, -560], "deck": [-240, 260], "pin": 5, "k": 2.2, "kc": 110}],
          MH, "KB_START")

# ── MULTI PRESS ── el asiento corre sobre el riel: hombros (casi derecho), inclinado y pecho (bien reclinado).
ANK = [0, 0]
def mp(H, b, W, **k):
    p = {"hip": list(H), "ankle": ANK, "ft": 0, "b": b, "hd": round(b * 0.85), "g": 1, "hx": round(W[0]), "hy": round(W[1]), "ed": 1}
    p.update(k); return p
def shp(H, b): return add(tuple(H), up(b, TORSO))
H_SH, H_IN, H_CH = (-240, -230), (-270, -250), (-300, -275)
B_SH, B_IN, B_CH = -8, -40, -72
S_SH, S_IN, S_CH = shp(H_SH, B_SH), shp(H_IN, B_IN), shp(H_CH, B_CH)
MP = {
    "SH_DOWN": mp(H_SH, B_SH, add(S_SH, (96, -24))),
    "SH_UP": mp(H_SH, B_SH, add(S_SH, up(-2, 314))),
    "IN_DOWN": mp(H_IN, B_IN, add(S_IN, (66, -34))),
    "IN_UP": mp(H_IN, B_IN, add(S_IN, up(22, 314))),
    "CH_DOWN": mp(H_CH, B_CH, add(S_CH, up(18, 72))),
    "CH_UP": mp(H_CH, B_CH, add(S_CH, up(18, 314))),
    "ARCH_BAD": mp((-226, -236), -22, add(shp((-226, -236), -22), up(4, 314)), cv=-30, hd=-14),
    "LOCK_BAD": mp(H_CH, B_CH, add(S_CH, up(18, 331))),
}
print("multi press", S_SH, S_IN, S_CH); check(MP)
base_spec("multi-press-machine", "GIMNASIO · PECHO", ["Pecho", "Hombros"], rig(660, 0.62),
          [{"type": "multipress", "pivot": [-120, -1100], "stack": 330, "frameTop": -1180, "rail": [H_SH[0], H_SH[1], H_CH[0], H_CH[1]], "pin": 5, "rest": 70, "k": 2.4}],
          MP, "CH_DOWN")
