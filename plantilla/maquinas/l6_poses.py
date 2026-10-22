# Lote 6 · cardio: poses + props + rig.
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from common import *

def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}

# ── TREADMILL ── cinta en y -40: todas las poses suben 74 px (la suela apoya sobre la cinta)
UPY = -74
def lift(p): q = dict(p); q["hip"] = [p["hip"][0], p["hip"][1] + UPY]; return q
run = json.load(open(os.path.join(R, "ejercicios", "running.json"), encoding="utf-8"))["poses"]
TM = {
    "STAND": {"hip": [0, -470 + UPY], "s": 0, "t": 0, "b": 0, "hd": 0, "ua": 6, "fa": 6},
    "WALK_A": lift({"hip": [0, -462], "s": 6, "t": -22, "s2": -14, "t2": 16, "b": 2, "hd": 2, "ua": -20, "fa": 20, "ua2": 20, "fa2": 24, "ft": 0, "ft2": 10}),
    "WALK_B": lift({"hip": [0, -462], "s": -14, "t": 16, "s2": 6, "t2": -22, "b": 2, "hd": 2, "ua": 20, "fa": 24, "ua2": -20, "fa2": 20, "ft": 10, "ft2": 0}),
    "RUN_A": lift(run["RUN_A"]), "RUN_B": lift(run["RUN_B"]),
    "HOLD_BAD": lift({"hip": [0, -440], "s": 10, "t": -20, "s2": -10, "t2": 18, "b": 24, "hd": 18, "g": 1, "hx": 190, "hy": -760 - UPY * 0 + 0, "ed": -1}),
    "LOOK_BAD": lift({**run["RUN_A"], "hd": 48, "b": 18}),
    "STRIDE_BAD": lift({"hip": [0, -440], "s": -30, "t": -48, "s2": 40, "t2": 30, "b": 0, "hd": 0, "ua": -40, "fa": 90, "ua2": 40, "fa2": 80, "ft": -30, "ft2": 30}),
    "SIDE": {"hip": [0, -470 + UPY - 16], "s": 0, "t": 0, "b": 0, "hd": 0, "ua": 6, "fa": 6},
}
TM["HOLD_BAD"]["hy"] = -760
print("treadmill"); check(TM)
base_spec("treadmill", "GIMNASIO · CARDIO", ["Cardio", "Piernas"], rig(500, 0.7),
          [{"type": "treadmill", "deck": [-520, 380, -40], "console": [330, -1000], "rail": -760, "clip": True}], TM, "STAND",
          extra={"floorScroll": 0})

# ── STATIONARY BIKE ── la biela gira alrededor de CR con radio 72; las manos fijas en el manubrio
CR = (60, -112); RR = 72
def bike(th, hip=(-170, -484), **k):
    a = rad(th); p1 = (CR[0] + RR * math.cos(a) - 30, CR[1] + RR * math.sin(a) - 36); p2 = (CR[0] - RR * math.cos(a) - 30, CR[1] - RR * math.sin(a) - 36)
    p = {"hip": list(hip), "ankle": [round(p1[0], 1), round(p1[1], 1)], "ankle2": [round(p2[0], 1), round(p2[1], 1)], "ft": 0, "ft2": 0,
         "b": 22, "hd": 2, "g": 1, "hx": 150, "hy": -640, "ed": -1}
    p.update(k); return p
BK = {f"P{i}": bike(i * 60) for i in range(6)}
BK["LOW_BAD0"] = bike(0, hip=(-150, -400)); BK["LOW_BAD3"] = bike(180, hip=(-150, -400))
BK["HIGH_BAD0"] = bike(90, hip=(-185, -530))
BK["HUNCH_BAD"] = bike(0, b=48, hd=30, cv=30, hx=150, hy=-640)
print("bike"); check(BK)
base_spec("stationary-bike", "GIMNASIO · CARDIO", ["Cardio", "Piernas"], rig(470, 0.86),
          [{"type": "stationarybike", "crank": list(CR), "seat": [-170, -450], "bar": [150, -640], "fly": [320, -280]}], BK, "P0")

# ── ELLIPTICAL ── el pie recorre una elipse; las manos van y vienen en las manijas
EC, ERX, ERY = (40, -186), 100, 40
def ell(th, **k):
    a = rad(th)
    A1 = (EC[0] + ERX * math.cos(a), EC[1] + ERY * math.sin(a)); A2 = (EC[0] - ERX * math.cos(a), EC[1] - ERY * math.sin(a))
    sw = math.cos(a)  # pierna cercana adelante → mano cercana atrás
    p = {"hip": [0, -624 + 8 * math.sin(2 * a)], "ankle": [round(A1[0], 1), round(A1[1], 1)], "ankle2": [round(A2[0], 1), round(A2[1], 1)],
         "ft": round(-8 * sw, 1), "ft2": round(8 * sw, 1), "b": 4, "hd": 2, "g": 1, "g2": 1, "ed": -1, "ed2": -1,
         "hx": round(150 - 70 * sw, 1), "hy": -820, "hx2": round(150 + 70 * sw, 1), "hy2": -820}
    p["hip"] = [p["hip"][0], round(p["hip"][1], 1)]
    p.update(k); return p
EL = {f"E{i}": ell(i * 60) for i in range(6)}
EL["LEAN_BAD"] = ell(0, b=34, hd=24, hip=[20, -600])
EL["TOES_BAD"] = ell(180, ft=30, ft2=30)
print("elliptical"); check(EL)
base_spec("elliptical-trainer", "GIMNASIO · CARDIO", ["Cardio", "Cuerpo completo"], rig(470, 0.78),
          [{"type": "elliptical", "fly": [360, -170], "pivot": [330, -430], "x0": -380}], EL, "E0")

# ── ROWING MACHINE ── se reusan las poses de la ficha rowing (CrossFit) + errores
rw = json.load(open(os.path.join(R, "ejercicios", "rowing.json"), encoding="utf-8"))
RW = dict(rw["poses"])
RW["ARMS_BAD"] = {**RW["CATCH"], "hx": -60, "hy": -300, "b": 18}
RW["ROUND_BAD"] = {**RW["CATCH"], "b": 44, "hd": 40, "cv": 40, "hx": 60, "hy": -210}
RW["HIGH_BAD"] = {**RW["FINISH"], "hy": -460}
RW["KNEES_BAD"] = {**RW["CATCH"], "hip": [-300, -190], "b": -10, "hd": -6, "hx": -200, "hy": -300}
print("rowing"); check(RW)
base_spec("rowing-machine", "GIMNASIO · CARDIO", ["Espalda", "Piernas"], rw["rig"], rw["props"], RW, "CATCH")

# ── STAIR CLIMBER ── un pie arriba, el otro abajo; la cadera sube y baja apenas
def stp(up_near, **k):
    hi, lo = (80, -150), (-30, -40)
    A1, A2 = (hi, lo) if up_near else (lo, hi)
    p = {"hip": [-10, -496], "ankle": list(A1), "ankle2": list(A2), "ft": 0, "ft2": 0, "b": 10, "hd": 4, "g": 1, "hx": 200, "hy": -700, "ed": -1}
    p.update(k); return p
SC = {"STEP_A": stp(True), "STEP_B": stp(False), "MID": stp(True, ankle=[50, -95], ankle2=[0, -95], hip=[-10, -520]),
      "HANG_BAD": stp(True, b=42, hd=30, hip=[-40, -450], hx=150, hy=-640), "TOES_BAD": stp(True, ft=36, ft2=36)}
print("stair"); check(SC)
base_spec("stair-climber", "GIMNASIO · CARDIO", ["Glúteos", "Cardio"], rig(540, 0.76),
          [{"type": "stairclimber", "base": [-460, 34], "x": 340, "rail": -700}], SC, "STEP_A")
