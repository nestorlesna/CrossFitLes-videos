# Dataset D98 Smith Standing Back Wrist Curl: poses + props + rig.
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


# D98 - curl de muñeca "back" en la Smith: parado de frente a la barra, brazos rectos y la barra a la altura del
# muslo; solo las muñecas suben la barra (wr). El disco queda adelante, apenas tapando el muslo.
st98 = dict(b=2, hd=0, g=1, hx=170, hy=-468, ed=1, wr=0)


def WC(**kw): return {**st98, **kw, "hip": [0, -462], "ankle": [48, 0], "ankle2": [-20, 0]}


SQ = {
    "DOWN": WC(wr=0),
    "UP": WC(wr=58, hy=-505),
    "HALF_BAD": WC(wr=30, hy=-487),
    "ELBOW_BAD": WC(wr=58, hy=-565),
    "SHRUG_BAD": WC(wr=58, hy=-505, sh=30),
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-standing-back-wrist-curl", "Smith Standing Back Wrist Curl", "GIMNASIO · ANTEBRAZOS",
         ["Antebrazos", "Bíceps"], rig(480, 0.8),
         [{"type": "smith", "x": 170, "top": -880, "gap": 280, "stops": -520, "track": "hands", "r": 58}],
         SQ, "DOWN",
         ("Curl de muñeca con la barra guiada: parado de frente a la máquina, los brazos rectos y la barra a la "
          "altura del muslo con agarre prono. Solo las muñecas suben la barra hacia el cuerpo, sin mover los codos "
          "ni los hombros, y bajan despacio hasta el estiramiento completo. Trabaja los antebrazos con poco peso y "
          "muchas repeticiones."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
