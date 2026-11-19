# Dataset D83 Smith Hip Raise: poses + props + rig.
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


# D83 - elevación de cadera en la Smith (puente de glúteo con barra): el atleta queda supino en el piso, con la
# cabeza a la izquierda y los pies apoyados a la derecha agarrando la barra sobre la pelvis.
# La cadera sube hasta alinear hombros-cadera-rodillas sin arquear la lumbar. `b -90` = torso horizontal con la
# cabeza hacia -x; al subir la cadera el torso queda a `b -120` con el hombro todavía en el piso.
st83 = dict(ankle=[225, 0], ankle2=[205, 0], ft=0, ft2=0, g=1, hx=0, ed=1)
HIP = {
    "DOWN": {**st83, "hip": [0, -40], "b": -92, "hd": -90, "hy": -65},
    "UP": {**st83, "hip": [0, -172], "b": -120, "hd": -92, "hy": -197},
    "HALF_BAD": {**st83, "hip": [0, -110], "b": -106, "hd": -91, "hy": -135},
    "HEELS_BAD": {**st83, "hip": [0, -172], "b": -120, "hd": -92, "hy": -197, "ft": -30, "ft2": -30},
    "ARCH_BAD": {**st83, "hip": [0, -205], "b": -132, "hd": -104, "hy": -230},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-hip-raise", "Smith Hip Raise", "GIMNASIO · GLÚTEO",
         ["Glúteo", "Isquios", "Core"], rig(540, 0.85),
         [{"type": "smith", "x": 0, "top": -860, "gap": 300, "stops": -300, "track": "hands",
           "torso": [-34, 18], "r": 64}],
         HIP, "DOWN",
         ("Elevación de cadera en la Smith: te acostás supino con la barra sobre la pelvis, los pies apoyados y "
          "los brazos firmes. Subís la cadera apretando el glúteo hasta alinear hombros, cadera y rodillas, sin "
          "arquear la lumbar. Es la versión con barra del puente de glúteo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
