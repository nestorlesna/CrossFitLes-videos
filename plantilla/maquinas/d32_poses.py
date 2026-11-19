# Dataset D56 Lever T Bar Row: poses + props + rig.
import sys, os, json
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


# D56 - remo T en palanca con pecho apoyado: de pie e inclinado sobre la máquina, el pecho en la almohadilla y las
# manos en la barra en T con agarre prono ancho. Se tira la barra al esternón abriendo los codos.
rw = dict(hip=[-130, -390], ankle=[70, -6], b=56, hd=14, g=1, g2=1, ed=1, ed2=1, ft=0)
TBAR = {
    "START": {**rw, "hx": 190, "hy": -330, "hx2": 204, "hy2": -322},
    "PULL": {**rw, "hx": 60, "hy": -420, "hx2": 74, "hy2": -412},
    "LEAN_BAD": {**rw, "hx": 60, "hy": -420, "hx2": 74, "hy2": -412, "b": 34, "hd": 6},
    "SHRUG_BAD": {**rw, "hx": 70, "hy": -500, "hx2": 84, "hy2": -492, "hd": 2},
    "ROUND_BAD": {**rw, "hx": 190, "hy": -330, "hx2": 204, "hy2": -322, "b": 68, "hd": 38, "cv": 26},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-t-bar-row", "Lever T Bar Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Dorsales"], rig(820, 0.88),
         [{"type": "tbarrow", "pivot": [-140, 8], "radius": 82, "plateFrac": 0.78,
           "pad": [-250, -505, 360, 48, -5]}],
         TBAR, "START",
         ("Parate inclinado sobre la máquina con el pecho apoyado en la almohadilla y los pies firmes. "
          "Tomá la barra en T con agarre prono, un poco más abierto que los hombros. Tirá la barra al "
          "esternón abriendo los codos, apretá los omóplatos y volvé lento sin despegar el pecho."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)

# D57 - remo T con agarre invertido: misma máquina, las palmas hacia arriba y los codos más cerca del cuerpo.
rw2 = dict(hip=[-120, -400], ankle=[80, -6], b=58, hd=12, g=1, g2=1, ed=-1, ed2=-1, ft=0)
TBARV = {
    "START": {**rw2, "hx": 180, "hy": -345, "hx2": 194, "hy2": -337},
    "PULL": {**rw2, "hx": 50, "hy": -430, "hx2": 64, "hy2": -422},
    "LEAN_BAD": {**rw2, "hx": 50, "hy": -430, "hx2": 64, "hy2": -422, "b": 34, "hd": 4},
    "SHRUG_BAD": {**rw2, "hx": 60, "hy": -505, "hx2": 74, "hy2": -497, "hd": 0},
    "ROUND_BAD": {**rw2, "hx": 180, "hy": -345, "hx2": 194, "hy2": -337, "b": 70, "hd": 36, "cv": 26},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("lever-t-bar-reverse-grip-row", "Lever T-bar Reverse Grip Row", "GIMNASIO · ESPALDA",
         ["Espalda", "Espalda alta", "Bíceps"], rig(820, 0.88),
         [{"type": "tbarrow", "pivot": [-150, 8], "radius": 84, "plateFrac": 0.8,
           "pad": [-245, -515, 355, 48, -6]}],
         TBARV, "START",
         ("Parate inclinado sobre la máquina con el pecho apoyado en la almohadilla y los pies firmes. "
          "Tomá la barra en T con agarre invertido, las palmas hacia arriba. Tirá la barra al abdomen con "
          "los codos cerca del cuerpo, apretá los omóplatos y volvé lento sin despegar el pecho."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
