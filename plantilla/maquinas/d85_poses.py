# Dataset D142-D152 + D154 (poleas). D153 (pelota) queda para cuando exista el prop.
# De pie / arrodillado mirando a la DERECHA. Columna a la derecha cuando el atleta mira la maquina
# y a la izquierda solo con polea BAJA (top >= -900) para no cruzar el bloque de titulo.
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


# --- bases -------------------------------------------------------------------------------------
STAND = dict(hip=[-10, -450], ankle=[70, 0], ankle2=[-60, 0], ft=0, ft2=12, b=4, hd=2, g=0)
KNEEL = dict(hip=[-10, -235], ankle=[-190, -30], ankle2=[170, 0], ft=90, ft2=0, b=0, hd=0, g=0, knee="back")
FLAT = dict(hip=[-20, -196], ankle=[230, 0], b=-90, hd=-92, ft=0, g=0, ed=1)
# Sentado en banco inclinado, torso recostado 45 grados, pies al frente.
INCL = dict(hip=[0, -238], ankle=[230, 0], b=-60, hd=-62, ft=0, g=0, ed=1)
BENCH_FLAT = {"type": "bench", "x0": -380, "x1": 120, "h": 200}
BENCH_INCL = {"type": "bench", "x0": -400, "x1": 20, "h": 240, "tilt": 30, "pivot": [20, -206]}


def pose(base, **k): return {**base, **k}


# D142 crunch de rodillas en polea alta: de espaldas a la maquina, la cuerda atras de la cabeza.
KNC1 = dict(KNEEL, ua2=166, fa2=118)
KNC_P = {
    "ERGUIDO": pose(KNC1, b=0, hd=0, ua=166, fa=118),
    "MEDIO": pose(KNC1, b=34, hd=34, ua=132, fa=118),
    "CRUNCH": pose(KNC1, b=64, hd=64, ua=102, fa=118),
    "SIN_FLEX": pose(KNC1, b=0, hd=0, ua=166, fa=64),
    "CADERA_ATRAS": pose(KNC1, b=16, hd=16, ua=166, fa=118, hip=[-95, -235]),
    "TIRON_BRAZOS": pose(KNC1, b=8, hd=6, ua=150, fa=60),
}

# D143 remo de deltoides posterior de rodillas: cuerda a la cara, codos altos.
KRD = dict(KNEEL, b=14, hd=12, ua2=98, fa2=8)
KRD_P = {
    "LEJOS": pose(KRD, ua=98, fa=8),
    "MEDIO": pose(KRD, ua=84, fa=66),
    "CERCA": pose(KRD, ua=78, fa=116),
    "CODO_BAD": pose(KRD, ua=44, fa=138),
    "ESPALDA_BAD": pose(KRD, ua=78, fa=116, b=-14, hd=-10),
    "HOMBRO_BAD": pose(KRD, ua=78, fa=116, sh=30),
}

# D144 extension de triceps de rodillas con cuerda: codos altos y quietos.
KTE = dict(KNEEL, ua2=166, fa2=8)
KTE_P = {
    "ESTIRA": pose(KTE, ua=166, fa=8),
    "MEDIO": pose(KTE, ua=166, fa=58),
    "FLEX": pose(KTE, ua=166, fa=112),
    "CODO_BAD": pose(KTE, ua=118, fa=62),
    "ESPALDA_BAD": pose(KTE, ua=166, fa=8, b=-22, hd=-10),
    "CUERPO_BAD": pose(KTE, ua=166, fa=8, b=20, hd=10),
}

# D145 elevacion lateral en polea baja: los brazos suben a los costados hasta el hombro.
CLR = dict(STAND, ankle=[105, 0], ankle2=[-70, 0], ft=0, ft2=14, ua2=4, fa2=10, al=0.8)
CLR_P = {
    "ABAJO": pose(CLR, ua=4, fa=10),
    "MEDIO": pose(CLR, ua=42, fa=4),
    "ARRIBA": pose(CLR, ua=74, fa=0),
    "CODO_BAD": pose(CLR, ua=46, fa=46),
    "ENCOGE_BAD": pose(CLR, ua=74, fa=0, sh=28),
    "IMPULSO_BAD": pose(CLR, ua=74, fa=0, b=-14, hd=-8),
}

# D146 curl de biceps acostado en banco plano: polea baja atras de la cabeza.
LBC = dict(FLAT, ua2=200, fa2=2)
LBC_P = {
    "ESTIRA": pose(LBC, ua=200, fa=2),
    "MEDIO": pose(LBC, ua=200, fa=-60),
    "ARRIBA": pose(LBC, ua=200, fa=-125),
    "CODO_BAD": pose(LBC, ua=150, fa=-40),
    "CADERA_BAD": pose(LBC, ua=200, fa=-125, hip=[-20, -176], b=-96, hd=-96),
    "HOMBRO_BAD": pose(LBC, ua=200, fa=-125, sh=26),
}

# D147 curl de biceps cerrado acostado en banco plano: barra al pecho.
LCG = dict(FLAT, ua2=205, fa2=2)
LCG_P = {
    "ESTIRA": pose(LCG, ua=205, fa=2),
    "MEDIO": pose(LCG, ua=205, fa=-55),
    "ARRIBA": pose(LCG, ua=205, fa=-108),
    "CODO_BAD": pose(LCG, ua=155, fa=-34),
    "CADERA_BAD": pose(LCG, ua=205, fa=-108, hip=[-20, -176], b=-96, hd=-96),
    "MUNECA_BAD": pose(LCG, ua=205, fa=-108, wr=36),
}

# D148 extension pullover acostado con cuerda: brazos largos bajan atras de la cabeza.
CEX = dict(FLAT, ua2=180, fa2=2)
CEX_P = {
    "ARRIBA": pose(CEX, ua=180, fa=2),
    "MEDIO": pose(CEX, ua=202, fa=2),
    "ATRAS": pose(CEX, ua=225, fa=6),
    "CODO_BAD": pose(CEX, ua=202, fa=52),
    "CADERA_BAD": pose(CEX, ua=225, fa=6, hip=[-20, -176], b=-96, hd=-96),
    "PASO_BAD": pose(CEX, ua=252, fa=2),
}

# D149 extension de triceps acostado: codos quietos, la cuerda baja a la frente.
LTE = dict(FLAT, ua2=180, fa2=2)
LTE_P = {
    "ARRIBA": pose(LTE, ua=180, fa=2),
    "MEDIO": pose(LTE, ua=180, fa=40),
    "FLEX": pose(LTE, ua=180, fa=78),
    "CODO_BAD": pose(LTE, ua=130, fa=96),
    "ARCO_BAD": pose(LTE, ua=180, fa=2, b=-84, hd=-86),
    "MUNECA_BAD": pose(LTE, ua=180, fa=78, wr=-34),
}

# D150 remo a una mano inclinado al frente: codo atras, pegado al costado.
BR1 = dict(STAND, ankle=[70, 0], ankle2=[-50, 0], ft=0, ft2=12, b=46, hd=40, ua2=2, fa2=8)
BR1_P = {
    "ESTIRA": pose(BR1, ua=8, fa=6),
    "MEDIO": pose(BR1, ua=-10, fa=62),
    "CERCA": pose(BR1, ua=-24, fa=118),
    "CODO_BAD": pose(BR1, ua=22, fa=96),
    "ESPALDA_BAD": pose(BR1, ua=-24, fa=118, b=72, hd=64),
    "HOMBRO_BAD": pose(BR1, ua=-24, fa=118, sh=28),
}

# D151 curl de biceps a una mano en polea baja.
OC1 = dict(STAND, ua2=2, fa2=8)
OC1_P = {
    "ABAJO": pose(OC1, ua=4, fa=12),
    "MEDIO": pose(OC1, ua=5, fa=64),
    "ARRIBA": pose(OC1, ua=6, fa=122),
    "CODO_BAD": pose(OC1, ua=32, fa=100),
    "SWING_BAD": pose(OC1, ua=6, fa=122, b=-16, hd=-8),
    "MUNECA_BAD": pose(OC1, ua=6, fa=122, wr=40),
}

# D152 press inclinado a una mano: recostado, polea baja atras de la cabeza.
IP1 = dict(INCL, ua2=2, fa2=8)
IP1_P = {
    "ABAJO": pose(IP1, ua=-30, fa=120),
    "MEDIO": pose(IP1, ua=28, fa=62),
    "ARRIBA": pose(IP1, ua=88, fa=4),
    "CODO_BAD": pose(IP1, ua=-58, fa=96),
    "TORSO_BAD": pose(IP1, ua=88, fa=4, b=-24, hd=-26),
    "HOMBRO_BAD": pose(IP1, ua=88, fa=4, sh=26),
}

# D154 elevacion lateral inclinado a una mano: brazo largo atras y al costado.
LB1 = dict(STAND, ankle=[80, 0], ankle2=[-60, 0], ft=0, ft2=12, b=48, hd=44,
           ua2=2, fa2=8, al=0.35)
LB1_P = {
    "ABAJO": pose(LB1, ua=8, fa=10, al=0.35),
    "MEDIO": pose(LB1, ua=-40, fa=6, al=0.55),
    "ARRIBA": pose(LB1, ua=-80, fa=2, al=0.8),
    "CODO_BAD": pose(LB1, ua=-70, fa=50, al=0.8),
    "TORSO_BAD": pose(LB1, ua=-80, fa=2, al=0.8, b=4, hd=2),
    "IMPULSO_BAD": pose(LB1, ua=-80, fa=2, al=0.8, b=6, hd=2),
}


# brazos simetricos: la mano lejana copia el angulo del brazo cercano
for _p in KNC_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in KRD_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in KTE_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in CLR_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in LBC_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in LCG_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in CEX_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in LTE_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]


def cable_r(pulley, top=-1150, att="handle", stack=620, **k):
    d = {"type": "cable", "x": stack, "top": top, "pulley": pulley, "track": pulley[0], "att": att, "pin": 5}
    d.update(k)
    return d


for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("cable-kneeling-crunch", "Cable Kneeling Crunch", "GIMNASIO · CORE",
         ["Abdominales", "Oblicuos"], rig(520, 0.72),
         [cable_r([520, -1180], top=-1340, att="rope", stack=620)],
         KNC_P, "ERGUIDO",
         ("Crunch de rodillas en polea alta: de espaldas a la máquina, la cuerda va atrás de la cabeza y el "
          "torso se encoge hacia los muslos sin mover la cadera.")),
        ("cable-kneeling-rear-delt-row-with-rope", "Cable Kneeling Rear Delt Row (With Rope)",
         "GIMNASIO · HOMBROS", ["Deltoides posterior", "Trapecios", "Romboides"], rig(520, 0.72),
         [cable_r([500, -940], top=-1120, att="rope", stack=600)],
         KRD_P, "LEJOS",
         ("Remo de deltoides posterior de rodillas: la cuerda se tira a la cara con los codos altos y los "
          "omóplatos juntos. La espalda queda recta y recta la cadera.")),
        ("cable-kneeling-triceps-extension", "Cable Kneeling Triceps Extension", "GIMNASIO · BRAZOS",
         ["Tríceps"], rig(520, 0.7),
         [cable_r([500, -1080], top=-1250, att="rope", stack=620)],
         KTE_P, "FLEX",
         ("Extensión de tríceps de rodillas: los codos apuntan arriba y quedan quietos mientras las manos "
          "bajan atrás de la cabeza. El torso queda erguido.")),
        ("cable-lateral-raise", "Cable Lateral Raise", "GIMNASIO · HOMBROS",
         ["Deltoides lateral", "Trapecios"], rig(560, 0.7),
         [{"type": "cablecrossover", "x": 560, "top": -700, "pulley": [490, -150], "pin": 5}],
         CLR_P, "ABAJO",
         ("Elevación lateral en polea baja: los brazos suben a los costados hasta la altura del hombro y "
          "bajan controlados. El codo casi estirado y el hombro lejos de la oreja.")),
        ("cable-lying-bicep-curl", "Cable Lying Bicep Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Antebrazos"], rig(600, 0.68),
         [BENCH_FLAT, cable_r([-620, -140], top=-880, stack=-700)],
         LBC_P, "ESTIRA",
         ("Curl de bíceps acostado en banco plano: la barra sube desde atrás de la cabeza hasta los hombros "
          "con los codos quietos y pegados al costado.")),
        ("cable-lying-close-grip-curl", "Cable Lying Close-grip Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Antebrazos"], rig(600, 0.68),
         [BENCH_FLAT, cable_r([-620, -140], top=-880, stack=-700, att="bar")],
         LCG_P, "ESTIRA",
         ("Curl de bíceps con agarre cerrado acostado en banco plano: las manos juntas curvan la barra al "
          "pecho sin despegar los codos del costado.")),
        ("cable-lying-extension-pullover-with-rope-attachment",
         "Cable Lying Extension Pullover (With Rope Attachment)", "GIMNASIO · ESPALDA",
         ["Dorsal ancho", "Tríceps"], rig(600, 0.68),
         [BENCH_FLAT, cable_r([-620, -700], top=-880, att="rope", stack=-700)],
         CEX_P, "ARRIBA",
         ("Pullover acostado con cuerda: los brazos largos bajan la cuerda atrás de la cabeza y vuelven "
          "sobre el pecho. El codo no se dobla y la cadera queda apoyada.")),
        ("cable-lying-triceps-extension-v-2", "Cable Lying Triceps Extension v. 2", "GIMNASIO · BRAZOS",
         ["Tríceps"], rig(600, 0.68),
         [BENCH_FLAT, cable_r([-620, -120], top=-880, att="rope", stack=-700)],
         LTE_P, "FLEX",
         ("Extensión de tríceps acostado en banco plano: la cuerda baja a la frente con los codos altos y "
          "quietos y sube hasta estirar los brazos.")),
        ("cable-one-arm-bent-over-row", "Cable One Arm Bent Over Row", "GIMNASIO · ESPALDA",
         ["Dorsal ancho", "Romboides", "Bíceps"], rig(540, 0.72),
         [cable_r([560, -130], stack=600)],
         BR1_P, "ESTIRA",
         ("Remo a una mano inclinado al frente: con la espalda recta, la manija se tira hasta el costado con "
          "el codo atrás y pegado al cuerpo.")),
        ("cable-one-arm-curl", "Cable One Arm Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Antebrazos"], rig(500, 0.72),
         [cable_r([500, -130], stack=580)],
         OC1_P, "ABAJO",
         ("Curl de bíceps a una mano en polea baja: el codo pegado al costado sube el antebrazo hasta el "
          "hombro y baja controlado. Una mano por vez.")),
        ("cable-one-arm-incline-press", "Cable One Arm Incline Press", "GIMNASIO · PECHO",
         ["Pectorales", "Deltoides anterior", "Tríceps"], rig(600, 0.7),
         [BENCH_INCL, cable_r([-520, -150], top=-880, stack=-560)],
         IP1_P, "ABAJO",
         ("Press inclinado a una mano en polea baja: sentado en el banco inclinado y de espaldas a la "
          "máquina, el brazo empuja arriba y adelante desde el hombro.")),
        ("cable-one-arm-lateral-bent-over", "Cable One Arm Lateral Bent Over", "GIMNASIO · HOMBROS",
         ["Deltoides posterior", "Trapecios", "Romboides"], rig(500, 0.72),
         [cable_r([-470, -240], top=-880, stack=-560)],
         LB1_P, "ABAJO",
         ("Elevación lateral inclinado a una mano: con el torso inclinado, el brazo casi estirado sube al "
          "costado hasta la altura del hombro. El torso no se levanta.")),
]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
