# Dataset D118-D129 (poleas): poses + props + rig.
# De pie mirando a la derecha; la columna va del lado del que tira el cable (derecha = frente,
# izquierda = espalda). `cable` acepta to:"ankle" para la tobillera (curl femoral).
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
SEAT = dict(hip=[-230, -215], ankle=[60, 0], ankle2=[-60, 0], ft=0, ft2=10, b=34, hd=40, g=0)
SEAT_EXT = dict(hip=[-230, -215], ankle=[60, 0], ankle2=[-60, 0], ft=0, ft2=10, b=50, hd=56, g=0)
STAND_ONE = dict(hip=[-10, -450], ankle=[-160, -40], ankle2=[40, 0], ft=60, ft2=0, b=6, hd=2, g=0, knee="back", ua=2, fa=8)
KNEEL = dict(hip=[-10, -235], ankle=[-190, -30], ankle2=[170, 0], ft=90, ft2=0, b=62, hd=68, g=0, knee="back", ua=-12)
FLAT = dict(hip=[-20, -196], ankle=[230, 0], b=-90, hd=-92, ft=0, g=1, hx=-235, ed=1)
DECL = dict(hip=[0, -272], ankle=[235, 0], b=-105, hd=-107, ft=0, g=1, hx=-235, ed=1)


def pose(base, **k): return {**base, **k}


# D118 press alterno de hombros: poleas altas, una mano arriba y la otra al hombro.
ALT_P = {
    "ARRIBA": pose(STAND, ua=162, fa=8, ua2=22, fa2=120),
    "MEDIO": pose(STAND, ua=95, fa=70, ua2=22, fa2=120),
    "ABAJO": pose(STAND, ua=22, fa=120, ua2=22, fa2=120),
    "ARRIBA2": pose(STAND, ua=22, fa=120, ua2=162, fa2=8),
    "CODO_BAD": pose(STAND, ua=112, fa=96, ua2=22, fa2=120),
    "TORSION_BAD": pose(STAND, ua=162, fa=8, ua2=22, fa2=120, b=-16, hd=-8, cv=-24),
}

# D119 extension de triceps alterna: codo alto y quieto; la otra mano cruza al triceps.
TRI = dict(STAND, ua2=70, fa2=-150)
TRI_P = {
    "TOP": pose(TRI, ua=165, fa=7),
    "MID": pose(TRI, ua=165, fa=45),
    "START": pose(TRI, ua=165, fa=85),
    "CODO_BAD": pose(TRI, ua=45, fa=150),
    "ARCH_BAD": pose(TRI, ua=165, fa=7, b=-14, hd=-6),
    "FRENTE_BAD": pose(TRI, ua=165, fa=-30),
}

# D120 curl femoral asistido de pie: una punta de pie atras con la tobillera en la polea alta.
LEGCURL_P = {
    "ABAJO": pose(STAND_ONE, ankle=[-160, -40], ft=60),
    "MEDIO": pose(STAND_ONE, ankle=[-165, -180], ft=30),
    "ARRIBA": pose(STAND_ONE, ankle=[-170, -280], ft=-10),
    "RODILLA_BAD": pose(STAND_ONE, ankle=[-160, -40], ft=60, hip=[-10, -430], b=14, hd=8),
    "CADERA_BAD": pose(STAND_ONE, ankle=[-165, -180], ft=30, b=32, hd=36),
    "IMPULSO_BAD": pose(STAND_ONE, ankle=[-120, -230], ft=0, b=-14, hd=-6),
}

# D121 press de banca en polea: acostado en banco plano, poleas bajas atras de la cabeza.
BENCHP_P = {
    "ARRIBA": pose(FLAT, hy=-505),
    "MEDIO": pose(FLAT, hy=-390),
    "ABAJO": pose(FLAT, hy=-272),
    "CORTO_BAD": pose(FLAT, hy=-450),
    "CUELLO_BAD": pose(FLAT, hip=[-90, -196], hy=-252),
    "CADERA_BAD": pose(FLAT, hip=[-20, -168], b=-102, hy=-390),
}

# D122 curl cerrado en polea baja: codos fijos al costado, la barra sube al pecho.
CURL_P = {
    "ABAJO": pose(STAND, ua=4, fa=10),
    "MEDIO": pose(STAND, ua=5, fa=62, b=3, hd=1),
    "ARRIBA": pose(STAND, ua=6, fa=118, b=2, hd=0),
    "CODO_BAD": pose(STAND, ua=34, fa=96, b=2, hd=0),
    "SWING_BAD": pose(STAND, ua=22, fa=104, b=-18, hd=-10, rx=-14),
    "HOMBRO_BAD": pose(STAND, ua=6, fa=118, b=2, hd=0, sh=30),
}

# D123 curl concentrado sentado: el codo apoyado en la cara interna del muslo.
CONC_P = {
    "ABAJO": pose(SEAT, ua=22, fa=-22),
    "MEDIO": pose(SEAT, ua=22, fa=80),
    "ARRIBA": pose(SEAT, ua=22, fa=150),
    "CODO_BAD": pose(SEAT, ua=48, fa=120),
    "ESPALDA_BAD": pose(SEAT, ua=22, fa=150, b=56, hd=64),
    "BALANCE_BAD": pose(SEAT, ua=30, fa=-30, b=12),
}

# D124 extension concentrada sobre la rodilla: en cuclillas sobre una rodilla, codo en la rodilla de adelante.
CONC_EXT_P = {
    "ABAJO": pose(KNEEL, fa=150),
    "MEDIO": pose(KNEEL, fa=95),
    "ARRIBA": pose(KNEEL, fa=20),
    "CODO_BAD": pose(KNEEL, fa=95, ua=24),
    "TORSO_BAD": pose(KNEEL, fa=20, b=34, hd=40),
    "HOMBRO_BAD": pose(KNEEL, fa=20, sh=36),
}

# D125 peso muerto en polea: cadera atras, espalda recta, tira con piernas y gluteos.
DEAD = dict(STAND, hip=[-10, -430], g=1, ed=1, ua2=6, fa2=10)
DEADLIFT_P = {
    "ABAJO": pose(DEAD, b=62, hd=68, hx=185, hy=-245),
    "MEDIO": pose(DEAD, b=30, hd=34, hx=160, hy=-368),
    "ARRIBA": pose(DEAD, b=6, hd=4, hx=60, hy=-420),
    "ESPALDA_BAD": pose(DEAD, b=78, hd=60, hx=185, hy=-245, cv=26),
    "PIERNA_BAD": pose(DEAD, hip=[-10, -400], b=22, hd=28, hx=110, hy=-350),
    "TIRON_BAD": pose(DEAD, b=16, hd=8, hx=40, hy=-460, rx=-10),
}

# D126 press declinado a una mano: polea baja atras de la cabeza.
DECL1_P = {
    "ARRIBA": pose(DECL, hy=-510, ua2=26, fa2=104),
    "MEDIO": pose(DECL, hy=-360, ua2=26, fa2=104),
    "ABAJO": pose(DECL, hy=-220, ua2=26, fa2=104),
    "CORTO_BAD": pose(DECL, hy=-450, ua2=26, fa2=104),
    "CUELLO_BAD": pose(DECL, hip=[-70, -272], hy=-202, ua2=26, fa2=104),
    "CADERA_BAD": pose(DECL, hip=[0, -238], b=-117, hy=-360, ua2=26, fa2=104),
}
# D127 press declinado con las dos manos.
DECL2_P = {
    "ARRIBA": pose(DECL, hy=-510),
    "MEDIO": pose(DECL, hy=-360),
    "ABAJO": pose(DECL, hy=-220),
    "CORTO_BAD": pose(DECL, hy=-450),
    "CUELLO_BAD": pose(DECL, hip=[-70, -272], hy=-202),
    "CADERA_BAD": pose(DECL, hip=[0, -238], b=-117, hy=-360),
}

# D128 curl arrastre: codos atras, la barra roza el torso y sube por el pecho.
DRAG_P = {
    "ABAJO": pose(STAND, ua=10, fa=14),
    "MEDIO": pose(STAND, ua=-8, fa=95),
    "ARRIBA": pose(STAND, ua=-18, fa=150),
    "CODO_BAD": pose(STAND, ua=26, fa=110),
    "SWING_BAD": pose(STAND, ua=-10, fa=140, b=-16, hd=-8),
    "CUELLO_BAD": pose(STAND, ua=-18, fa=150, b=18, hd=24),
}

# D129 elevacion frontal: brazo casi estirado hasta la altura del hombro.
FRONT_P = {
    "ABAJO": pose(STAND, ua=6, fa=6),
    "MEDIO": pose(STAND, ua=46, fa=2),
    "ARRIBA": pose(STAND, ua=88, fa=-2),
    "CODO_BAD": pose(STAND, ua=40, fa=40),
    "IMPULSO_BAD": pose(STAND, ua=88, fa=-2, b=-12, hd=-4),
    "HOMBRO_BAD": pose(STAND, ua=88, fa=-2, sh=36),
}

BENCH_FLAT = {"type": "bench", "x0": -380, "x1": 120, "h": 200}
BENCH_SEAT = {"type": "bench", "x0": -480, "x1": -140, "h": 200}
BENCH_DECL = {"type": "bench", "x0": -380, "x1": 80, "h": 300, "tilt": -15, "pivot": [80, -266]}


def cable_r(pulley, top=-1150, att="handle", stack=620, **k):
    d = {"type": "cable", "x": stack, "top": top, "pulley": pulley, "track": pulley[0], "att": att, "pin": 5}
    d.update(k)
    return d


for clave, nombre, category, tags, rig_, props, poses, initial, descripcion in [
        ("cable-alternate-shoulder-press", "Cable Alternate Shoulder Press", "GIMNASIO · HOMBROS",
         ["Deltoides anterior", "Deltoides lateral", "Tríceps"], rig(470, 0.78),
         [{"type": "cablecrossover", "x": -420, "top": -1340, "pulley": [-300, -1250], "pin": 4}],
         ALT_P, "ABAJO",
         ("Press de hombros alterno en poleas: de pie, una mano sube por encima de la cabeza mientras la otra "
          "queda a la altura del hombro. El cable mantiene la tensión y el cambio de mano es lento y controlado.")),
        ("cable-alternate-triceps-extension", "Cable Alternate Triceps Extension", "GIMNASIO · BRAZOS",
         ["Tríceps", "Deltoides posterior"], rig(600, 0.72),
         [cable_r([-260, -1250], top=-1400, stack=-400)],
         TRI_P, "START",
         ("Extensión de tríceps alterna en polea: el codo queda alto y quieto y el antebrazo sale de atrás de la "
          "cabeza hasta estirar el brazo. La otra mano cruza y sujeta el tríceps que trabaja.")),
        ("cable-assisted-inverse-leg-curl", "Cable Assisted Inverse Leg Curl", "GIMNASIO · PIERNAS",
         ["Isquiotibiales", "Glúteos", "Gemelos"], rig(560, 0.7),
         [cable_r([-400, -80], top=-900, att="strap", stack=-560, to="ankle")],
         LEGCURL_P, "ABAJO",
         ("Curl femoral de pie en polea alta: una punta de pie atrás con la tobillera puesta y el talón sube "
          "hacia el glúteo. La pierna de apoyo queda firme y el torso no se mueve.")),
        ("cable-bench-press", "Cable Bench Press", "GIMNASIO · PECHO",
         ["Pectorales", "Tríceps", "Deltoides anterior"], rig(600, 0.7),
         [BENCH_FLAT, {"type": "cablecrossover", "x": -560, "top": -700, "pulley": [-420, -150], "pin": 5}],
         BENCHP_P, "ABAJO",
         ("Press de banca en poleas: acostado en el banco plano con las poleas bajas atrás de la cabeza. Las dos "
          "manos suben desde el pecho hasta estirar los brazos, con los codos cerca del torso.")),
        ("cable-close-grip-curl", "Cable Close Grip Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Braquial", "Antebrazos"], rig(480, 0.74),
         [cable_r([500, -120], att="bar")],
         CURL_P, "ABAJO",
         ("Curl de bíceps con agarre cerrado en polea baja: las manos juntas a la barra y los codos pegados al "
          "costado. La barra sube al pecho sin que los codos se adelanten.")),
        ("cable-concentration-curl", "Cable Concentration Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Braquial"], rig(480, 0.72),
         [BENCH_SEAT, cable_r([470, -140], stack=600)],
         CONC_P, "ABAJO",
         ("Curl concentrado sentado en polea baja: el codo apoyado en la cara interna del muslo y la mano sube "
          "hasta el hombro. Aísla el bíceps y no deja balancear el torso.")),
        ("cable-concentration-extension-on-knee", "Cable Concentration Extension (On Knee)", "GIMNASIO · BRAZOS",
         ["Tríceps", "Antebrazos"], rig(540, 0.7),
         [cable_r([500, -1150], top=-1300, stack=640)],
         CONC_EXT_P, "ABAJO",
         ("Extensión de tríceps sobre la rodilla: en cuclillas sobre una rodilla, el codo apoyado en la rodilla "
          "de adelante y el antebrazo se estira hacia el piso. El codo no se despega de la rodilla.")),
        ("cable-deadlift", "Cable Deadlift", "GIMNASIO · PIERNAS",
         ["Glúteos", "Isquiotibiales", "Cuádriceps", "Zona lumbar"], rig(520, 0.7),
         [cable_r([500, -120], att="bar", stack=600)],
         DEADLIFT_P, "ABAJO",
         ("Peso muerto en polea baja: la cadera va atrás, la espalda queda recta y el peso sube pegado a las "
          "piernas. Empuja con los talones y termina parado, sin tirar con la espalda.")),
        ("cable-decline-one-arm-press", "Cable Decline One Arm Press", "GIMNASIO · PECHO",
         ["Pectorales", "Tríceps", "Deltoides anterior"], rig(560, 0.72),
         [BENCH_DECL, cable_r([-400, -140], top=-900, stack=-520)],
         DECL1_P, "ARRIBA",
         ("Press declinado a una mano en polea: la polea baja queda atrás de la cabeza y el brazo empuja hacia "
          "arriba, con el codo cerca del torso. Una mano trabaja y la otra descansa en el pecho.")),
        ("cable-decline-press", "Cable Decline Press", "GIMNASIO · PECHO",
         ["Pectorales", "Tríceps", "Deltoides anterior"], rig(560, 0.72),
         [BENCH_DECL, {"type": "cablecrossover", "x": -520, "top": -700, "pulley": [-400, -140], "pin": 5}],
         DECL2_P, "ARRIBA",
         ("Press declinado en poleas: tumbado en el banco declinado con las poleas bajas atrás de la cabeza. "
          "Las dos manos empujan hacia arriba hasta estirar los brazos y bajan controladas.")),
        ("cable-drag-curl", "Cable Drag Curl", "GIMNASIO · BRAZOS",
         ["Bíceps", "Braquial"], rig(480, 0.74),
         [cable_r([500, -140], att="bar")],
         DRAG_P, "ABAJO",
         ("Curl arrastre en polea baja: los codos van atrás y la barra sube pegada al torso hasta el pecho. "
          "El codo no se adelanta y el peso nunca se despega del cuerpo.")),
        ("cable-forward-raise", "Cable Forward Raise", "GIMNASIO · HOMBROS",
         ["Deltoides anterior", "Pectorales superiores"], rig(480, 0.74),
         [cable_r([500, -140])],
         FRONT_P, "ABAJO",
         ("Elevación frontal en polea baja: el brazo casi estirado sube al frente hasta la altura del hombro y "
          "baja despacio. El torso no se balancea y el codo no se dobla.")),
]:
    print(nombre)
    check(poses)
    base_dataset(clave, nombre, category, tags, rig_, props, poses, initial, descripcion)
