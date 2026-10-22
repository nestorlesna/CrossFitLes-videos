# Lote 1 · piernas guiadas: poses + props + rig (frames vacíos hasta probar en pose-lab).
import sys, math
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}

# ── LEG EXTENSION ── rodilla en el eje (0,-345), cadera atrás, tibia que gira
HIP = [-240, -345]
seat = dict(t=-90, b=-12, hd=-4, g=1, hx=-180, hy=-330, ed=1, ft=8)
LE = {
    "DOWN": {**seat, "hip": HIP, "s": 6},
    "MID": {**seat, "hip": HIP, "s": -45, "ft": -20},
    "UP": {**seat, "hip": HIP, "s": -86, "ft": -60},
    "AXIS_BAD": {**seat, "hip": [-175, -345], "s": 6, "hx": -150},
    "KICK_BAD": {**seat, "hip": [-236, -392], "t": -82, "b": -26, "hd": -18, "s": -98, "ft": -70, "hx": -180},
    "LOCK_BAD": {**seat, "hip": HIP, "s": -99, "ft": -72},
}
print("leg-extension"); check(LE)
base_spec("leg-extension", "GIMNASIO · PIERNAS", ["Cuádriceps"], rig(700, 0.8),
          [{"type": "legextension", "pivot": [0, -345], "seat": [-330, -30, -300], "back": [-318, -12, 430],
            "stack": -600, "handle": [-180, -330], "roll": 205, "pin": 5}], LE, "DOWN")

# ── SEATED LEG CURL ── piernas estiradas al frente, rodillo atrás del tobillo, traba sobre los muslos
sc = dict(t=-90, b=-14, hd=-6, g=1, hx=-180, hy=-330, ed=1)
SL = {
    "EXT": {**sc, "hip": HIP, "s": -84, "ft": -70},
    "MID": {**sc, "hip": HIP, "s": -32, "ft": -20},
    "CURL": {**sc, "hip": HIP, "s": 26, "ft": 20},
    "THIGH_BAD": {**sc, "hip": [-240, -392], "t": -100, "b": -24, "hd": -16, "s": -10, "ft": 0, "bf": 1},
    "BACK_BAD": {**sc, "hip": HIP, "b": 18, "hd": 30, "cv": 26, "s": 20, "ft": 16, "hx": -150, "hy": -340},
    "SHORT_BAD": {**sc, "hip": HIP, "s": -55, "ft": -40},
}
print("seated-leg-curl"); check(SL)
base_spec("seated-leg-curl", "GIMNASIO · PIERNAS", ["Isquiotibiales", "Gemelos"], rig(700, 0.8),
          [{"type": "seatedlegcurl", "pivot": [0, -345], "seat": [-330, -30, -300], "back": [-322, -14, 430],
            "stack": -600, "handle": [-180, -330], "roll": 212, "thigh": [-70, -401], "pin": 5}], SL, "EXT")

# ── LYING LEG CURL ── boca abajo, cabeza a la derecha, rodilla en el eje (-240,-460)
pr = dict(t=90, b=92, hd=74, g=1, hx=372, hy=-362, ed=-1)
LL = {
    "EXT": {**pr, "hip": [0, -460], "s": 92, "ft": 92},
    "MID": {**pr, "hip": [0, -460], "s": 145, "ft": 145},
    "CURL": {**pr, "hip": [0, -460], "s": 200, "ft": 196},
    "HIP_BAD": {**pr, "hip": [8, -548], "t": 71, "b": 110, "hd": 92, "s": 196, "ft": 192},
    "POINT_BAD": {**pr, "hip": [0, -460], "s": 196, "ft": 260},
}
print("lying-leg-curl"); check(LL)
base_spec("lying-leg-curl", "GIMNASIO · PIERNAS", ["Isquiotibiales", "Gemelos"], rig(480, 0.74),
          [{"type": "lyinglegcurl", "pivot": [-240, -460], "top": -414, "x0": -200, "x1": 440, "stack": 610,
            "handle": [372, -362], "roll": 215, "pin": 5}], LL, "EXT")

# ── HACK SQUAT ── tronco apoyado a lean, cadera sobre la línea del riel, pies fijos en la plataforma
LEAN = -36
u = up(LEAN, 1); fr = (-u[1], u[0])  # fr: hacia el pecho (normal al tronco)
A = (0, -60)
Q = (A[0] - 120, A[1] - 90)  # punto de la línea de la cadera


def hipat(D):
    # cadera sobre la línea Q + u*m con |H - A| = D (raíz de arriba de la cuadrática)
    w = (Q[0] - A[0], Q[1] - A[1]); bb = 2 * (w[0] * u[0] + w[1] * u[1]); cc = w[0] ** 2 + w[1] ** 2 - D * D
    m = (-bb + math.sqrt(bb * bb - 4 * cc)) / 2
    return (round(Q[0] + u[0] * m, 1), round(Q[1] + u[1] * m, 1))


def hk(H, b=LEAN, extra=None):
    S = add(H, up(b, TORSO)); hand = (S[0] + fr[0] * 92 + u[0] * 6, S[1] + fr[1] * 92 + u[1] * 6)
    p = {"hip": list(H), "ankle": list(A), "b": b, "hd": b + 30, "ft": -14, "g": 0, "ua": b + 52, "fa": 118}
    if extra: p.update(extra)
    return p


HT, HM, HB = hipat(448), hipat(330), hipat(262)
HKP = {
    "TOP": hk(HT), "MID": hk(HM), "BOTTOM": hk(HB),
    "LOCK_BAD": hk(hipat(468)),
    "HEELS_BAD": {**hk(HB), "ankle": [8, -96], "ft": 22},
    "BACK_BAD": {**hk((HB[0] + 70, HB[1] - 30)), "b": LEAN + 34, "hd": LEAN + 50, "cv": 24},
}
# las manos van con el carro: en BACK_BAD el carro está en HB (la cadera se despegó), las manos siguen en la manija del carro
HKP["BACK_BAD"].update(ua=-10, fa=120)
print("hack-squat", HT, HM, HB); check(HKP)
def handpar(p, H0, b):
    j = fk(p); uu = up(b, 1); bk = (uu[1], -uu[0]); w = (j["W"][0] - H0[0], j["W"][1] - H0[1])
    return [round(w[0] * uu[0] + w[1] * uu[1], 1), round(w[0] * bk[0] + w[1] * bk[1], 1)]
base_spec("hack-squat", "GIMNASIO · PIERNAS", ["Cuádriceps", "Glúteos"], rig(700, 0.72),
          [{"type": "hacksquat", "hip": list(HT), "lean": LEAN, "foot": list(A), "plat": -14, "len": 300, "rail": [-470, 620], "stops": -330, "hand": handpar(HKP["TOP"], HT, LEAN)}], HKP, "TOP")

# ── PENDULUM SQUAT ── cadera en arco alrededor del eje PV; el tronco gira lo mismo
L0 = -26
A2 = (0, -60)
H0 = (-150, -470)
PV = (H0[0] - 520, H0[1] - 120)
r0 = dist(H0, PV); a0 = math.atan2(H0[1] - PV[1], H0[0] - PV[0])


def pend(da, extra=None):
    a = a0 + rad(da)
    H = (round(PV[0] + math.cos(a) * r0, 1), round(PV[1] + math.sin(a) * r0, 1))
    b = L0 + da
    uu = up(b, 1); ff = (-uu[1], uu[0])
    S = add(H, up(b, TORSO)); hand = (S[0] + ff[0] * 92 + uu[0] * 6, S[1] + ff[1] * 92 + uu[1] * 6)
    p = {"hip": list(H), "ankle": list(A2), "b": round(b, 1), "hd": round(b + 26, 1), "ft": -16, "g": 0, "ua": round(b + 52, 1), "fa": 118}
    if extra: p.update(extra)
    return p, dist(H, A2)


PD = {}
for k, da in [("TOP", 0), ("MID", 14), ("BOTTOM", 27), ("LOCK_BAD", -4)]:
    PD[k], d = pend(da); print(" ", k, round(d))
PD["BOUNCE_BAD"] = {**pend(33)[0]}
PD["HEELS_BAD"] = {**pend(27)[0], "ankle": [8, -96], "ft": 22}
print("pendulum-squat"); check(PD)
base_spec("pendulum-squat", "GIMNASIO · PIERNAS", ["Cuádriceps", "Glúteos"], rig(680, 0.72),
          [{"type": "pendulum", "hip": list(H0), "pivot": list(PV), "lean": L0, "foot": list(A2), "plat": -14, "len": 300, "hand": handpar(PD["TOP"], H0, L0)}], PD, "TOP")
