# Dataset D130-D141 (poleas): poses + props + rig.
# De pie mirando a la derecha. La columna va a la derecha cuando el atleta mira la maquina
# (remo, press inclinado) y a la izquierda solo si la polea es BAJA (aduccion, extension inclinada).
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
# Inclinado (cabecera arriba a la izquierda, pies en el piso). Igual que D106-D117.
INCL = dict(hip=[0, -238], ankle=[230, 0], b=-60, hd=-62, ft=0, g=1, hx=-235, ed=1)
BENCH_INCL = {"type": "bench", "x0": -400, "x1": 20, "h": 240, "tilt": 30, "pivot": [20, -206]}


def pose(base, **k): return {**base, **k}


# D130 elevacion frontal a una mano: paso corto, polea baja al frente.
FR1 = dict(STAND, ankle=[105, 0], ankle2=[-70, 0], ft=0, ft2=14, ua2=2, fa2=8)
FR_P = {
    "ABAJO": pose(FR1, ua=4, fa=8),
    "MEDIO": pose(FR1, ua=48, fa=3),
    "ARRIBA": pose(FR1, ua=92, fa=-2),
    "CODO_BAD": pose(FR1, ua=52, fa=46),
    "IMPULSO_BAD": pose(FR1, ua=92, fa=-2, b=-12, hd=-6),
    "CRUZA_BAD": pose(FR1, ua=92, fa=-2, cv=-24),
}

# D131 elevacion frontal con las dos manos: poleas bajas al frente, suben juntas.
FR2 = dict(STAND, ua2=4, fa2=8)
FR2_P = {
    "ABAJO": pose(FR2, ua=5, fa=8),
    "MEDIO": pose(FR2, ua=50, fa=2, ua2=50, fa2=2),
    "ARRIBA": pose(FR2, ua=95, fa=-2, ua2=95, fa2=-2),
    "CODO_BAD": pose(FR2, ua=52, fa=44, ua2=52, fa2=44),
    "IMPULSO_BAD": pose(FR2, ua=95, fa=-2, ua2=95, fa2=-2, b=-14, hd=-6),
    "TORSION_BAD": pose(FR2, ua=95, fa=-2, ua2=95, fa2=-2, cv=20),
}

# D132 curl martillo con cuerda: palmas enfrentadas, codos fijos al costado.
HAM = dict(STAND, ua2=4, fa2=10)
HAM_P = {
    "ABAJO": pose(HAM, ua=4, fa=10),
    "MEDIO": pose(HAM, ua=5, fa=64),
    "ARRIBA": pose(HAM, ua=6, fa=122),
    "CODO_BAD": pose(HAM, ua=34, fa=98),
    "SWING_BAD": pose(HAM, ua=22, fa=106, b=-16, hd=-8),
    "MUNECA_BAD": pose(HAM, ua=6, fa=122, wr=42),
}

# D133 extension de triceps sobre la cabeza con cuerda: codos altos y quietos.
EXT = dict(STAND, ankle=[100, 0], ankle2=[-60, 0], ft=0, ft2=14, ua2=166, fa2=8)
EXT_P = {
    "ESTIRA": pose(EXT, ua=166, fa=8),
    "MEDIO": pose(EXT, ua=166, fa=62),
    "FLEX": pose(EXT, ua=166, fa=118),
    "CODO_BAD": pose(EXT, ua=122, fa=62),
    "ESPALDA_BAD": pose(EXT, ua=166, fa=8, b=-16, hd=-8),
    "GIRO_BAD": pose(EXT, ua=166, fa=8, cv=-22),
}

# D134 remo alto de rodillas: de rodillas frente a la maquina, la barra al pecho.
KROW = dict(hip=[-10, -235], ankle=[-190, -30], ankle2=[170, 0], ft=90, ft2=0,
            b=26, hd=22, g=0, knee="back", ua2=6, fa2=10)
KROW_P = {
    "LEJOS": pose(KROW, ua=80, fa=4),
    "MEDIO": pose(KROW, ua=50, fa=72),
    "CERCA": pose(KROW, ua=22, fa=120),
    "CODO_BAD": pose(KROW, ua=62, fa=58),
    "ESPALDA_BAD": pose(KROW, ua=22, fa=120, b=-10, hd=-4),
    "CUELLO_BAD": pose(KROW, ua=22, fa=120, hd=62),
}

# D135 aduccion de cadera: tobillera, la pierna cruza por delante de la de apoyo.
ADD = dict(hip=[-10, -450], ankle=[-170, -20], ankle2=[30, 0], ft=30, ft2=0,
           b=4, hd=2, g=0, knee="back", ua=4, fa=6, ua2=2, fa2=8)
ADD_P = {
    "AFUERA": pose(ADD, ankle=[-170, -20]),
    "MEDIO": pose(ADD, ankle=[-45, -12]),
    "CRUZA": pose(ADD, ankle=[70, -10]),
    "FUERA_BAD": pose(ADD, ankle=[-225, -20]),
    "TALON_BAD": pose(ADD, ankle=[-170, -20], ft=62),
    "TORSO_BAD": pose(ADD, ankle=[-170, -20], b=20, hd=16),
}

# D136 press en banco inclinado con poleas bajas a los costados.
INCLP_P = {
    "TOP": pose(INCL, hy=-640),
    "MID": pose(INCL, hy=-500),
    "BOTTOM": pose(INCL, hy=-330),
    "SHORT_BAD": pose(INCL, hy=-570),
    "NECK_BAD": pose(INCL, hip=[60, -238], hy=-312),
    "BUTT_BAD": pose(INCL, hip=[0, -204], b=-48, hy=-500, cv=-20),
}

# D137 remo en banco inclinado: pecho apoyado, una mano tira de polea baja.
IROW = dict(INCL, g=0, ua=4, fa=8, ua2=2, fa2=6)
IROW_P = {
    "ABAJO": pose(IROW, ua=4, fa=8),
    "MEDIO": pose(IROW, ua=6, fa=64),
    "ARRIBA": pose(IROW, ua=10, fa=122),
    "CODO_BAD": pose(IROW, ua=46, fa=96),
    "HOMBRO_BAD": pose(IROW, ua=10, fa=122, sh=28),
    "TIRON_BAD": pose(IROW, ua=10, fa=122, b=-34),
}

# D138 extension de triceps recostado en banco inclinado (poleas altas al frente).
IPD = dict(INCL, g=0, ua2=158, fa2=6)
IPD_P = {
    "ARRIBA": pose(IPD, ua=158, fa=6),
    "MEDIO": pose(IPD, ua=120, fa=4),
    "ABAJO": pose(IPD, ua=88, fa=2),
    "CODO_BAD": pose(IPD, ua=120, fa=62),
    "TROMPA_BAD": pose(IPD, ua=88, fa=2, b=-26),
    "MUNECA_BAD": pose(IPD, ua=88, fa=2, wr=-34),
}

# D139 extension de triceps en banco inclinado con polea baja atras de la cabeza.
ITE = dict(INCL, g=0, ua2=160, fa2=8)
ITE_P = {
    "ESTIRA": pose(ITE, ua=160, fa=8),
    "MEDIO": pose(ITE, ua=160, fa=44),
    "FLEX": pose(ITE, ua=160, fa=96),
    "CODO_BAD": pose(ITE, ua=118, fa=60),
    "CABEZA_BAD": pose(ITE, ua=160, fa=8, hd=-78),
    "ARCO_BAD": pose(ITE, ua=160, fa=8, b=-72),
}

# D140 judo flip: las dos manos arriba y bajan en diagonal con giro del torso.
JUDO = dict(STAND, ankle=[90, 0], ankle2=[-70, 0], ft=0, ft2=14, ua2=150, fa2=18)
JUDO_P = {
    "ARRIBA": pose(JUDO, ua=150, fa=18),
    "MEDIO": pose(JUDO, ua=108, fa=32),
    "ABAJO": pose(JUDO, ua=24, fa=26, cv=26),
    "CODO_BAD": pose(JUDO, ua=108, fa=78),
    "TORSO_BAD": pose(JUDO, ua=24, fa=26, b=24, hd=18, cv=0),
    "PLANO_BAD": pose(JUDO, ua=120, fa=8, cv=-26),
}

# D141 patada de triceps: inclinado al frente, codo alto y el antebrazo se estira atras.
KB = dict(STAND, hip=[-10, -450], ankle=[60, 0], ankle2=[-60, 0], ft=0, ft2=12,
          b=54, hd=48, ua2=2, fa2=8)
KB_P = {
    "FLEX": pose(KB, ua=10, fa=22),
    "MEDIO": pose(KB, ua=-28, fa=6),
    "EXT": pose(KB, ua=-62, fa=2),
    "CODO_BAD": pose(KB, ua=26, fa=-46),
    "IMPULSO_BAD": pose(KB, ua=-62, fa=2, b=26, hd=20),
    "ESPALDA_BAD": pose(KB, ua=-62, fa=2, b=78, hd=64),
}



# brazos simetricos: las dos manos copian el angulo del brazo cercano
for _p in HAM_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in EXT_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in KROW_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in IPD_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in ITE_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]
for _p in JUDO_P.values(): _p["ua2"], _p["fa2"] = _p["ua"], _p["fa"]

def cable_r(pulley, top=-1150, att="handle", stack=620, **k):
    d = {"type": "cable", "x": stack, "top": top, "pulley": pulley, "track": pulley[0], "att": att, "pin": 5}
    d.update(k)
    return d


for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("cable-front-raise", "Cable Front Raise", "GIMNASIO · HOMBROS",
         ["Deltoides anterior", "Pectorales superiores"], rig(540, 0.72),
         [cable_r([540, -130], stack=600)],
         FR_P, "ABAJO",
         ("Elevación frontal a una mano en polea baja: el brazo casi estirado sube al frente hasta la altura "
          "del hombro y baja controlado. Una mano trabaja por vez y el torso no se mueve.")),
        ("cable-front-shoulder-raise", "Cable Front Shoulder Raise", "GIMNASIO · HOMBROS",
         ["Deltoides anterior", "Deltoides lateral"], rig(560, 0.7),
         [{"type": "cablecrossover", "x": 560, "top": -700, "pulley": [500, -150], "pin": 5}],
         FR2_P, "ABAJO",
         ("Elevación frontal con las dos manos en poleas bajas: los brazos suben juntos y estirados hasta la "
          "altura del hombro. El abdomen firme evita el balanceo.")),
        ("cable-hammer-curl-with-rope", "Cable Hammer Curl (With Rope)", "GIMNASIO · BRAZOS",
         ["Bíceps", "Braquial", "Antebrazos"], rig(500, 0.72),
         [cable_r([500, -130], att="rope", stack=580)],
         HAM_P, "ABAJO",
         ("Curl martillo con cuerda en polea baja: las palmas enfrentadas y los codos pegados al costado. "
          "La cuerda sube al pecho sin que los codos se adelanten.")),
        ("cable-high-pulley-overhead-tricep-extension", "Cable High Pulley Overhead Tricep Extension",
         "GIMNASIO · BRAZOS", ["Tríceps"], rig(560, 0.7),
         [cable_r([500, -1150], top=-1320, att="rope", stack=620)],
         EXT_P, "FLEX",
         ("Extensión de tríceps sobre la cabeza con cuerda en polea alta: los codos apuntan arriba y quedan "
          "quietos mientras las manos bajan atrás de la cabeza. El torso se mantiene firme.")),
        ("cable-high-row-kneeling", "Cable High Row (Kneeling)", "GIMNASIO · ESPALDA",
         ["Dorsal ancho", "Romboides", "Bíceps"], rig(520, 0.72),
         [cable_r([520, -640], top=-1250, att="bar", stack=600)],
         KROW_P, "LEJOS",
         ("Remo alto de rodillas en polea: de rodillas frente a la máquina, la barra se tira al pecho con los "
          "codos abajo y atrás. La espalda queda recta y el torso no se levanta.")),
        ("cable-hip-adduction", "Cable Hip Adduction", "GIMNASIO · PIERNAS",
         ["Aductores", "Glúteo medio"], rig(560, 0.7),
         [cable_r([-440, -90], top=-860, att="strap", stack=-520, to="ankle")],
         ADD_P, "AFUERA",
         ("Aducción de cadera en polea: con la tobillera puesta, la pierna cruza por delante de la pierna de "
          "apoyo. El recorrido es corto y controlado, sin mover el torso.")),
        ("cable-incline-bench-press", "Cable Incline Bench Press", "GIMNASIO · PECHO",
         ["Pectorales", "Tríceps", "Deltoides anterior"], rig(600, 0.7),
         [BENCH_INCL, {"type": "cablecrossover", "x": -560, "top": -700, "pulley": [-430, -160], "pin": 5}],
         INCLP_P, "BOTTOM",
         ("Press de banca inclinado en poleas: recostado en el banco a unos cuarenta y cinco grados, las manos "
          "empujan desde el pecho hasta estirar los brazos. Los codos bajan a los costados.")),
        ("cable-incline-bench-row", "Cable Incline Bench Row", "GIMNASIO · ESPALDA",
         ["Dorsal ancho", "Romboides", "Bíceps"], rig(600, 0.68),
         [BENCH_INCL, cable_r([-520, -150], top=-880, stack=-560)],
         IROW_P, "ABAJO",
         ("Remo en banco inclinado con polea baja: el pecho apoyado en el banco y una mano tira la manija "
          "hasta el costado. El codo va atrás, pegado al cuerpo, sin levantar el hombro.")),
        ("cable-incline-pushdown", "Cable Incline Pushdown", "GIMNASIO · BRAZOS",
         ["Tríceps", "Pectorales"], rig(560, 0.7),
         [BENCH_INCL, cable_r([520, -1250], top=-1400, stack=640)],
         IPD_P, "ARRIBA",
         ("Extensión de tríceps recostado en banco inclinado: con las poleas altas, los brazos suben sobre la "
          "cabeza y bajan estirados al frente. El codo no se abre.")),
        ("cable-incline-triceps-extension", "Cable Incline Triceps Extension", "GIMNASIO · BRAZOS",
         ["Tríceps"], rig(560, 0.68),
         [BENCH_INCL, cable_r([-520, -140], top=-900, stack=-560)],
         ITE_P, "FLEX",
         ("Extensión de tríceps en banco inclinado con polea baja: la barra baja atrás de la cabeza con los "
          "codos altos y quietos, y sube hasta estirar los brazos.")),
        ("cable-judo-flip", "Cable Judo Flip", "GIMNASIO · CORE",
         ["Oblicuos", "Core", "Dorsal ancho"], rig(540, 0.7),
         [cable_r([520, -1180], top=-1340, att="rope", stack=620)],
         JUDO_P, "ARRIBA",
         ("Judo flip en polea: las dos manos agarran la cuerda arriba y la bajan en diagonal con un giro del "
          "torso, como un flip de judo. La cadera acompaña el giro y los brazos no se doblan.")),
        ("cable-kickback", "Cable Kickback", "GIMNASIO · BRAZOS",
         ["Tríceps"], rig(520, 0.72),
         [cable_r([520, -130], stack=580)],
         KB_P, "FLEX",
         ("Patada de tríceps en polea baja: inclinado al frente, el codo queda alto y quieto y el antebrazo se "
          "estira atrás. El torso no se levanta y el codo no se despega del costado.")),
]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
