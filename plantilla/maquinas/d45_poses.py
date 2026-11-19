# Dataset D69 Sled Calf Press On Leg Press: poses + props + rig.
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


# D69 - gemelos (sóleo) en la prensa a 45° con las rodillas semiflexionadas: al quedar la rodilla un poco
# doblada (cadera-tobillo 384-428, nunca estirada) trabaja más el sóleo y el recorrido es corto y controlado.
st11 = dict(hip=[-320, -300], b=-45, hd=-12, g=1, hx=-280, hy=-310, ed=1)
CSO = {
    "DOWN": {**st11, "ankle": [-28.4, -504.3], "ankle2": [-68.4, -496.3], "ft": -150, "ft2": -150},
    "UP": {**st11, "ankle": [7.6, -529.4], "ankle2": [-32.4, -521.4], "ft": -104, "ft2": -104},
    "HALF_BAD": {**st11, "ankle": [-10.4, -516.8], "ankle2": [-50.4, -508.8], "ft": -128, "ft2": -128},
    "KNEE_BAD": {**st11, "ankle": [-66.1, -477.8], "ankle2": [-106.1, -469.8], "ft": -150, "ft2": -150},
    "HIP_BAD": {**st11, "hip": [-296, -334], "b": -38, "ankle": [-4.4, -538.3], "ankle2": [-44.4, -530.3],
                "ft": -150, "ft2": -150},
}

for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("sled-calf-press-on-leg-press", "Sled Calf Press On Leg Press", "GIMNASIO · PIERNAS",
         ["Sóleo", "Gemelos"], rig(610, 0.92),
         [{"type": "legpress", "hip": [-320, -300], "ang": 35, "lean": -45, "stops": 330}],
         CSO, "DOWN",
         ("Sóleo en la prensa a 45 grados: apoyá la espalda, dejá las rodillas apenas flexionadas y la planta de los "
          "pies en la plataforma. Empujá con los tobillos sin estirar del todo las rodillas y bajá hasta sentir "
          "el estiramiento."))]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
