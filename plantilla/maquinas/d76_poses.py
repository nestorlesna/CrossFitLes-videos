# Dataset D100 Smith Standing Leg Calf Raise: poses + props + rig.
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


# D100 - elevación de talón a una pierna en la Smith: barra en la espalda alta (track "back", como D97), la pierna
# de apoyo sube al metatarso (ft) mientras la otra se despega doblada atrás (ankle2 arriba y atrás).
st100 = dict(b=3, hd=0, g=1, hb=1, hx=-75, hy=22, ed=1, ft=0)


def CR(**kw): return {**st100, **kw}


SQ = {
    "DOWN": CR(hip=[0, -455], ankle=[30, 0], ankle2=[-30, 0]),
    "UP": CR(hip=[0, -495], ankle=[30, -40], ankle2=[-120, -215], ft=38, ft2=40),
    "HALF_BAD": CR(hip=[0, -470], ankle=[30, -18], ankle2=[-90, -120], ft=18, ft2=20),
    "KNEE_BAD": CR(hip=[0, -455], ankle=[30, -40], ankle2=[-120, -215], ft=38, ft2=40),
    "LEAN_BAD": CR(hip=[35, -495], ankle=[30, -40], ankle2=[-120, -215], ft=38, ft2=40, b=16, hd=10),
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-standing-leg-calf-raise", "Smith Standing Leg Calf Raise", "GIMNASIO · PANTORRILLAS",
         ["Gemelos", "Isquiotibiales"], rig(428, 0.8),
         [{"type": "smith", "x": -80, "top": -900, "gap": 300, "stops": -560, "track": "back",
           "torso": [-34, 18], "r": 56}],
         SQ, "DOWN",
         ("Elevación de talón a una pierna en la Smith: la barra apoyada en la espalda alta, una pierna de apoyo "
          "y la otra despegada del piso. Subí el talón hasta quedar sobre la punta del pie, apretá el gemelo "
          "arriba y bajá despacio hasta el estiramiento completo. Mantené la rodilla casi estirada y el torso "
          "derecho: el movimiento sale solo del tobillo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
