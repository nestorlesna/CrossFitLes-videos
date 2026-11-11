# Dataset D01 — D5 Assisted Standing Pull-up y D6 Lever Assisted Chin-up: poses + props + rig.
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


def st(S, b, ankle, grip, **k):
    H = (S[0] - up(b, TORSO)[0], S[1] - up(b, TORSO)[1])
    p = {"hip": [round(H[0], 1), round(H[1], 1)], "ankle": list(ankle), "b": b, "hd": b, "ft": 0, "g": 1,
         "hx": grip[0], "hy": grip[1], "ed": -1}
    p.update(k); return p


# — D5 — Assisted Standing Pull-up: de pie en la plataforma, agarre prono ancho, manijas altas —
GP5 = (70, -1300)
D5 = {
    "STAND": st((10, -976), 2, (40, -229), GP5),
    "MID": st((0, -1120), 2, (30, -373), GP5),
    "TOP": st((-10, -1230), 0, (20, -483), GP5),
    "SWING_BAD": st((30, -1000), -24, (180, -300), GP5),
    "HALF_BAD": st((15, -1030), 2, (45, -283), GP5),
}
print("D5 assisted standing pull-up")
check(D5)
ATOP5 = fk(D5["TOP"])["A"][1]
base_dataset("assisted-standing-pull-up", "Assisted Standing Pull-up", "GIMNASIO · ESPALDA",
             ["Dorsales", "Bíceps"], rig(560, 0.58),
             [{"type": "assisted", "stack": 420, "grip": list(GP5), "pivot": [300, -220], "pad": "feet",
               "rest": round(ATOP5), "pin": 6, "k": 1}],
             D5, "STAND",
             "Ponte de pie en la plataforma con agarre prono ancho. Tirá con los dorsales y los bíceps hasta pasar el mentón. Bajá lento.")

# — D6 — Lever Assisted Chin-up: manijas más bajas y adelantadas, de pie en la plataforma —
GP6 = (90, -1150)
D6 = {
    "STAND": st((40, -850), 2, (80, -104), GP6),
    "MID": st((30, -1000), 2, (70, -253), GP6),
    "TOP": st((20, -1110), 0, (60, -363), GP6),
    "SWING_BAD": st((70, -890), -26, (230, -200), GP6),
    "HALF_BAD": st((45, -910), 2, (85, -163), GP6),
}
print("D6 lever assisted chin-up")
check(D6)
ATOP6 = fk(D6["TOP"])["A"][1]
base_dataset("lever-assisted-chin-up", "Lever Assisted Chin-up", "GIMNASIO · ESPALDA",
             ["Dorsales", "Bíceps"], rig(560, 0.58),
             [{"type": "assisted", "stack": 420, "grip": list(GP6), "pivot": [300, -220], "pad": "feet",
               "rest": round(ATOP6), "pin": 6, "k": 1}],
             D6, "STAND",
             "De pie en la plataforma, agarrá las manijas con agarre prono y tirá del cuerpo hacia arriba liderando con el pecho.")
