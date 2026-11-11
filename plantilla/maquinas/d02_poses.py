# Dataset D01 — D3 Assisted Parallel Close Grip Pull-up y D4 Assisted Standing Chin-up: poses + props + rig.
import sys, os, json, csv
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


# — D3 — Assisted Parallel Close Grip Pull-up: arrodillado en la plataforma, agarre paralelo cerrado —
GP3 = (60, -1000)


def kn(S, b, **k):
    H = (S[0] - up(b, TORSO)[0], S[1] - up(b, TORSO)[1])
    p = {"hip": [round(H[0], 1), round(H[1], 1)], "s": 92, "t": 4, "b": b, "hd": b, "ft": 80, "g": 1,
         "hx": GP3[0], "hy": GP3[1], "ed": -1}
    p.update(k); return p


D3 = {
    "HANG": kn((10, -682), -6),
    "MID": kn((-20, -800), -10),
    "TOP": kn((-30, -930), -12),
    "KIP_BAD": kn((20, -800), -26, t=40, s=120),
    "HALF_BAD": kn((-10, -750), -8, hd=6),
}
print("D3 assisted parallel close grip pull-up")
check(D3)
KTOP3 = fk(D3["TOP"])["K"][1]
base_dataset("assisted-parallel-close-grip-pull-up", "Assisted Parallel Close Grip Pull-up", "GIMNASIO · ESPALDA",
             ["Dorsales", "Bíceps"], rig(560, 0.58),
             [{"type": "assisted", "stack": 420, "grip": list(GP3), "pivot": [300, -260], "rest": round(KTOP3), "pin": 6, "k": 1}],
             D3, "HANG",
             "Arrodillate en la plataforma y agarrá las barras paralelas con agarre cerrado. Tirá del cuerpo hacia arriba con la espalda y bajá lento.")

# — D4 — Assisted Standing Chin-up: de pie sobre la plataforma, manijas altas —
GP4 = (60, -1240)


def st(S, b, ankle, **k):
    H = (S[0] - up(b, TORSO)[0], S[1] - up(b, TORSO)[1])
    p = {"hip": [round(H[0], 1), round(H[1], 1)], "ankle": list(ankle), "b": b, "hd": b, "ft": 0, "g": 1,
         "hx": GP4[0], "hy": GP4[1], "ed": -1}
    p.update(k); return p


D4 = {
    "STAND": st((10, -915), 0, (46, -168)),
    "MID": st((0, -1055), 0, (36, -308)),
    "TOP": st((-10, -1160), 0, (26, -413)),
    "SWING_BAD": st((30, -950), -26, (160, -240)),
    "HALF_BAD": st((15, -962), 2, (51, -213)),
}
print("D4 assisted standing chin-up")
check(D4)
ATOP4 = fk(D4["TOP"])["A"][1]
base_dataset("assisted-standing-chin-up", "Assisted Standing Chin-up", "GIMNASIO · ESPALDA",
             ["Dorsales", "Bíceps"], rig(560, 0.58),
             [{"type": "assisted", "stack": 420, "grip": list(GP4), "pivot": [300, -220], "pad": "feet",
               "rest": round(ATOP4), "pin": 6, "k": 1}],
             D4, "STAND",
             "Subí a la plataforma, agarrá las manijas con agarre prono y tirá con la espalda hasta pasar el mentón. Bajá lento.")
