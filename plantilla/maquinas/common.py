# Helpers comunes para generar fichas de máquinas (GENERAR_VIDEOS_MAQUINAS.md §4.4). FK = misma geometría que runtime.js.
# Uso: python plantilla/maquinas/lN_poses.py (poses + props) → pose-lab → python plantilla/maquinas/lN_frames.py (escenas + YouTube).
import json, os, math, csv

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # raíz del proyecto
DESL = open(os.path.join(R, "plantilla", "youtube-deslinde.txt"), encoding="utf-8").read().strip()
SHIN, THIGH, TORSO, NECK, UPPER, FORE = 230, 240, 280, 32, 172, 160
rad = math.radians
deg = math.degrees


def up(a, l): return (math.sin(rad(a)) * l, -math.cos(rad(a)) * l)
def down(a, l): return (math.sin(rad(a)) * l, math.cos(rad(a)) * l)
def add(p, q): return (p[0] + q[0], p[1] + q[1])
def dist(p, q): return math.hypot(p[0] - q[0], p[1] - q[1])


def legIK(H, A, back=False):
    hx, hy = H; ax, ay = A
    dx, dy = hx - ax, hy - ay
    d = min(math.hypot(dx, dy), SHIN + THIGH - 0.5)
    base = math.atan2(dy, dx)
    a = math.acos((SHIN * SHIN + d * d - THIGH * THIGH) / (2 * SHIN * d))
    k1 = (ax + math.cos(base + a) * SHIN, ay + math.sin(base + a) * SHIN)
    k2 = (ax + math.cos(base - a) * SHIN, ay + math.sin(base - a) * SHIN)
    fwd = k1 if k1[1] < k2[1] else k2
    K = (k2 if fwd is k1 else k1) if back else fwd
    Hh = (ax + math.cos(base) * d, ay + math.sin(base) * d)
    return round(deg(math.atan2(K[0] - ax, -(K[1] - ay))), 2), round(deg(math.atan2(Hh[0] - K[0], -(Hh[1] - K[1]))), 2)


def norm(p):
    q = dict(s=0, t=0, b=0, hd=0, ua=6, fa=6, rx=0, ry=0, ft=0, hx=70, hy=-20, ed=1, g=0, ll=1, ll2=1, ul=1, fl=1, al=1)
    q.update(p)
    if "hip" in p and "ankle" in p:
        q["s"], q["t"] = legIK(p["hip"], p["ankle"], p.get("knee") == "back")
        q["rx"], q["ry"] = p["ankle"]
        if "ankle2" in p: q["s2"], q["t2"] = legIK(p["hip"], p["ankle2"], p.get("knee") == "back")
    elif "hip" in p:
        q["rx"] = p["hip"][0] - math.sin(rad(q["s"])) * SHIN - math.sin(rad(q["t"])) * THIGH
        q["ry"] = p["hip"][1] + math.cos(rad(q["s"])) * SHIN + math.cos(rad(q["t"])) * THIGH
    for k in ("s", "t", "ua", "fa", "ft"): q.setdefault(k + "2", q[k])
    return q


def ik(S, T, l1, l2, side):
    dx, dy = T[0] - S[0], T[1] - S[1]
    d = max(1, min(math.hypot(dx, dy), l1 + l2 - 0.5))
    base = math.atan2(dy, dx)
    a = math.acos(max(-1, min(1, (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d))))
    e1 = (S[0] + math.cos(base + a) * l1, S[1] + math.sin(base + a) * l1)
    e2 = (S[0] + math.cos(base - a) * l1, S[1] + math.sin(base - a) * l1)
    E = e1 if (e1[0] > e2[0]) == (side >= 0) else e2
    return E, (S[0] + math.cos(base) * d, S[1] + math.sin(base) * d)


def fk(p):
    """Articulaciones del lado cercano (rig px) de una pose de ficha."""
    st = norm(p)
    A = (st["rx"], st["ry"])
    K = add(A, up(st["s"], SHIN)); H = add(K, up(st["t"], THIGH))
    S = add(H, up(st["b"], TORSO)); N = add(S, up(st["hd"], NECK))
    al = st["al"]; fE = add(S, down(st["ua"], UPPER * al * st["ul"])); fW = add(fE, down(st["ua"] + st["fa"], FORE * al * st["fl"]))
    g = st["g"]
    if g:
        E, W = ik(S, (st["hx"], st["hy"]), UPPER, FORE, st["ed"])
        E = (fE[0] + (E[0] - fE[0]) * g, fE[1] + (E[1] - fE[1]) * g); W = (fW[0] + (W[0] - fW[0]) * g, fW[1] + (W[1] - fW[1]) * g)
    else:
        E, W = fE, fW
    reach = dist(S, (st["hx"], st["hy"])) if g else 0
    return dict(A=A, K=K, H=H, S=S, N=N, E=E, W=W, reach=reach, st=st)


def check(poses, maxreach=331):
    for k, p in poses.items():
        j = fk(p)
        flag = " <<< NO LLEGA" if j["reach"] > maxreach else ""
        print(f"  {k:12s} A({j['A'][0]:.0f},{j['A'][1]:.0f}) K({j['K'][0]:.0f},{j['K'][1]:.0f}) H({j['H'][0]:.0f},{j['H'][1]:.0f}) "
              f"S({j['S'][0]:.0f},{j['S'][1]:.0f}) N({j['N'][0]:.0f},{j['N'][1]:.0f}) W({j['W'][0]:.0f},{j['W'][1]:.0f}) reach {j['reach']:.0f}{flag}")


class Stage:
    def __init__(self, rig): self.r = rig
    def __call__(self, x, y=None):
        if y is None: x, y = x
        return (self.r["x"] + self.r["scale"] * x, self.r["y"] + self.r["scale"] * y)


def row(clave):
    for r in csv.DictReader(open(os.path.join(R, "ejercicios", "maquinas.csv"), encoding="utf-8-sig"), delimiter=";"):
        if r["clave"] == clave: return r


def ring(p, r, at=1.0, **k): return {"type": "ring", "pos": [round(p[0]), round(p[1])], "r": r, "at": at, **k}
def lab(p, t, a="middle", at=1.2, **k): return {"type": "label", "pos": [round(p[0]), round(p[1])], "text": t, "anchor": a, "at": at, **k}
def arrow(a, b, at=1.0, dur=0.8, bend=None):
    o = {"type": "arrow", "from": [round(a[0]), round(a[1])], "to": [round(b[0]), round(b[1])], "at": at, "dur": dur}
    if bend: o["bend"] = bend
    return o
def NO(at=1.4, pos=(540, 780)): return lab(pos, "ASÍ NO", at=at)


def step(badge, head, sub, vo, moves, ov=(), mn=6.5, **k):
    f = {"min": mn, "badge": badge, "head": head, "sub": sub, "vo": vo, "moves": moves, **k}
    if ov: f["overlays"] = list(ov)
    return f


def hook(cat, head, sub, vo, moves, mn=5.6): return {"kind": "hook", "min": mn, "badge": cat, "head": head, "sub": sub, "vo": vo, "moves": moves}
def keys(badge, head, ks, vo, moves, mn=8.6, shrink=0.78): return {"kind": "keys", "min": mn, "badge": badge, "head": head, "shrink": shrink, "keys": ks, "vo": vo, "moves": moves}
def reps(head, sub, vo, chips, moves, mn=7.6):
    return {"kind": "reps", "min": mn, "badge": "A ENTRENAR", "head": head, "sub": sub, "vo": vo,
            "chips": [{"label": c, "at": a} for c, a in zip(chips, (0.6, 1.1, 1.6))], "moves": moves}


def yt_desc(name, es, linea, gancho, ajuste, pasos, errores, tips, musc, cuanto, hashtags, nivel=1, extra=None):
    n = lambda xs: "\n".join(f"{e} {x}" for e, x in zip(["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"], xs))
    b = lambda xs: "\n".join("• " + x for x in xs)
    aviso = ""
    if nivel >= 3:
        aviso = "\n\nSi es tu primera vez en esta máquina, pedile al profe del gimnasio que te ajuste la máquina y te mire las primeras series."
    if extra: aviso += "\n\n" + extra
    return f"""🔥 {name.upper()} ({es}) — {linea}

{gancho} 💪

🛠️ AJUSTE DE LA MÁQUINA
{n(ajuste)}

📋 PASO A PASO
{n(pasos)}

❌ ERRORES COMUNES
{b(errores)}

💡 TIPS DEL PROFE
{b(tips)}

🎯 QUÉ TRABAJA
{musc}

⏱️ CUÁNTO
{cuanto}

🙌 Si te sirvió, dejá tu like, guardalo y compartilo con quien entrena con vos.{aviso}

{DESL}

{hashtags}"""


def base_spec(clave, category, tags, rig, props, poses, initial, extra=None):
    r = row(clave)
    p = os.path.join(R, "ejercicios", clave + ".json")
    s = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
    s.update({"slug": clave, "name": r["nombre"], "maquina": True, "category": category, "tags": tags,
              "descripcion": r["como_se_usa"], "revisado": s.get("revisado", False), "notas": s.get("notas", ""),
              "music": True, "musicVolume": 0.18, "rig": rig, "shadow": False, "initialPose": initial,
              "props": props, "poses": poses})
    s.setdefault("frames", [])
    if extra: s.update(extra)
    json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return s


def save(slug, frames, mini, yt, extra=None):
    p = os.path.join(R, "ejercicios", slug + ".json")
    s = json.load(open(p, encoding="utf-8"))
    names = set(s["poses"])
    for i, f in enumerate(frames, 1):
        assert len(f["vo"]) <= 135, (slug, i, len(f["vo"]), f["vo"])
        for m in f["moves"]:
            for k in ("to", "cut"):
                if k in m: assert m[k] in names, (slug, i, m)
            if "seq" in m:
                for a, _ in m["seq"]: assert a in names, (slug, i, a)
                assert "until" in m or "count" in m
        for o in f.get("overlays", []):
            if o["type"] == "label":
                assert o["pos"][1] <= 1570 and len(o["text"]) <= 22, (slug, i, o)
                w = len(o["text"]) * 21; x = o["pos"][0]
                lo = x - w if o["anchor"] == "end" else x - w / 2 if o["anchor"] == "middle" else x
                assert lo >= 40 and lo + w <= 1040, ("label fuera", slug, i, o)
    assert len(yt["titulo"]) <= 100 and "<" not in yt["descripcion"] and ">" not in yt["descripcion"]
    assert len(", ".join(yt["tags"])) <= 500
    s.update({"frames": frames, "miniatura": mini, "youtube": yt})
    if extra: s.update(extra)
    json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(slug, len(frames), "escenas OK")
