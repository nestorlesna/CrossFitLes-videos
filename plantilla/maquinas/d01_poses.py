# Dataset D01 · D1 Lever Seated Crunch (Chest Pad) y D2 Lever Seated Leg Raise Crunch: poses + props + rig.
# (D2 del dataset original, "Lever Seated Crunch v. 2", quedó como equivalente de ab-crunch-machine.)
import sys, os, json, csv
sys.path.insert(0, os.path.dirname(__file__))
from common import *


def rig(x, scale): return {"x": x, "y": round(1532 - 34 * scale, 1), "scale": scale}


def dsrow(clave):
    p = os.path.join(R, "ejercicios", "dataset.csv")
    for r in csv.DictReader(open(p, encoding="utf-8-sig"), delimiter=";"):
        if r["clave"] == clave:
            return r


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


# ── D1 · Lever Seated Crunch (Chest Pad): sentado, almohadilla al pecho, el torso va atrás ──
sit = dict(hip=[-240, -230], ankle=[60, -20], ft=0, g=0)
D1 = {
    "UP": {**sit, "b": 2, "hd": 0, "ua": 24, "fa": 150},
    "LEAN": {**sit, "b": -20, "hd": -24, "ua": 20, "fa": 150},
    "DEEP": {**sit, "b": -30, "hd": -34, "ua": 16, "fa": 150},
    "ARMS_BAD": {**sit, "b": -6, "hd": 0, "ua": 70, "fa": 40},
    "NECK_BAD": {**sit, "b": -24, "hd": 60, "ua": 20, "fa": 150},
    "SWING_BAD": {**sit, "ankle": [90, -20], "ft": -14, "b": -34, "hd": -54, "ua": 8, "fa": 170},
}
print("D1 lever seated crunch (chest pad)")
check(D1)
base_dataset("lever-seated-crunch-chest-pad", "Lever Seated Crunch (Chest Pad)", "GIMNASIO · CORE",
             ["Abdominales", "Oblicuos"], rig(720, 0.66),
             [{"type": "abcrunch", "seat": [-390, -90, -184], "pivot": [-300, -820], "stack": -640, "feet": [60, -20], "pin": 5}],
             D1, "UP",
             "Sentate con el pecho contra la almohadilla, trabá los pies y llevá el torso atrás con el abdomen. Volvé lento.")

# ── D2 · Lever Seated Leg Raise Crunch: elevar las piernas + crunch, la palanca sigue la rodilla ──
base = dict(hip=[-240, -230], ft=0, g=0)
D2 = {
    "DOWN": {**base, "ankle": [60, -20], "b": 8, "hd": 8, "ua": 15, "fa": 10},
    "MID": {**base, "ankle": [80, -160], "b": 14, "hd": 18, "ua": 8, "fa": 14},
    "LIFT": {**base, "ankle": [-20, -300], "b": 24, "hd": 34, "ua": -14, "fa": 36},
    "SWING_BAD": {**base, "ankle": [170, -120], "b": 10, "hd": 6, "ua": 10, "fa": 12},
    "CURL_BAD": {**base, "ankle": [-20, -300], "b": 8, "hd": 4, "ua": 15, "fa": 10},
}
print("D2 lever seated leg raise crunch")
check(D2)
base_dataset("lever-seated-leg-raise-crunch", "Lever Seated Leg Raise Crunch", "GIMNASIO · CORE",
             ["Abdominales", "Flexores de cadera"], rig(720, 0.66),
             [{"type": "abcrunch", "seat": [-390, -90, -184], "pivot": [-300, -820], "stack": -640, "feet": [60, -20],
               "pin": 5, "leg": True, "legPivot": [-320, -260]}],
             D2, "DOWN",
             "Sentate con la espalda apoyada y las manos en el asiento. Subí las rodillas al pecho y, arriba, enrollá el torso con el abdomen.")
