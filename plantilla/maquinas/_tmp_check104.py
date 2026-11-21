import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import fk

base = dict(hip=[0, -455], ankle=[40, 0], ankle2=[-22, 0], b=2, hd=0, g=1, hx=130, ed=1)
for hy in (-468, -560, -640, -680):
    for ed in (1, -1):
        r = fk({**base, "hy": hy, "ed": ed})
        print(hy, ed, "S", tuple(round(v) for v in r["S"]), "E", tuple(round(v) for v in r["E"]),
              "W", tuple(round(v) for v in r["W"]), "reach", round(r["reach"]))
