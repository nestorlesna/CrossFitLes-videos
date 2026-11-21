# Dataset D103 Smith Toe Raise: poses + props + rig.
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


# D103 - elevaciÃ³n de punta de pie sentado en la Smith: la barra apoya sobre los muslos y las manos la sujetan.
# El pie queda plano y solo las puntas suben (ft negativo = dorsiflexiÃ³n). Banco plano como D93.
st103 = dict(hip=[-30, -250], ankle=[215, 0], ankle2=[215, 0], b=2, hd=0, ft=0, ft2=0, g=1, hx=100, hy=-238, ed=1)

TR = {
    "DOWN": dict(st103),
    "UP": {**st103, "ft": -26, "ft2": -26},
    "HALF_BAD": {**st103, "ft": -12, "ft2": -12},
    "HEEL_BAD": {**st103, "ft": 24, "ft2": 24},
    "LEAN_BAD": {**st103, "b": 14, "hd": 8},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("smith-toe-raise", "Smith Toe Raise", "GIMNASIO Â· PANTORRILLAS",
         ["Tibial anterior", "Gemelos"], rig(480, 0.8),
         [{"type": "bench", "x0": -260, "x1": 180, "h": 284},
          {"type": "smith", "x": 120, "top": -830, "gap": 280, "stops": -250, "track": "hands", "r": 56}],
         TR, "DOWN",
         ("ElevaciÃ³n de punta de pie sentado en la Smith: sentate en el banco, apoyÃ¡ la barra sobre los muslos y "
          "sujetala con las dos manos. Con el pie plano, subÃ­ las puntas de los pies lo mÃ¡s alto posible, "
          "apretÃ¡ el tibial y bajÃ¡ despacio. El talÃ³n no se despega del piso: el recorrido sale solo del tobillo."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)




