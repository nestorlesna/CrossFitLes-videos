/* Piezas propias de los videos largos (se suman al timeline "main" que arma plantilla/runtime.js).
 * window.__LARGO lo inyecta plantilla/largo/build-largo.mjs (tiempos absolutos, segundos):
 *   caps  [{ci, start, end}]            encabezado del capítulo: entra y sale con el capítulo
 *   holds [{id, t0, dur}]               cuenta regresiva: anillo que se vacía + segundos que faltan
 *   cards [{id, tipo, v0, segs}]        tarjeta "vista de frente / de arriba": figura dibujada según un valor v
 *                                       (segs [{t0, t1, a, b}] = v va de a → b, ease seno)
 * Todo se dibuja desde un reloj (propiedad-función, igual que el proxy del personaje): seek-safe, sin callbacks.
 */
(function () {
  const X = window.__LARGO;
  const tl = window.__timelines["main"];
  const NS = "http://www.w3.org/2000/svg";
  const $ = (id) => document.getElementById(id);
  const COL = { skin: "#E8B383", skinFar: "#D29A68", shirt: "#2FB3A6", pants: "#3F3F9A", pantsFar: "#31317E", hair: "#6B3B1F", floor: "#D9D2C5" };
  const rad = (d) => (d * Math.PI) / 180;
  const lerp = (p, q, k) => ({ x: p.x + (q.x - p.x) * k, y: p.y + (q.y - p.y) * k });
  const f2 = (n) => Math.round(n * 10) / 10;
  function el(tag, attrs, parent) {
    const n = document.createElementNS(NS, tag);
    for (const k in attrs) n.setAttribute(k, attrs[k]);
    parent.appendChild(n);
    return n;
  }
  const seg = (parent, color, w) => el("line", { stroke: color, "stroke-width": w, "stroke-linecap": "round" }, parent);
  const setL = (n, a, b) => { n.setAttribute("x1", f2(a.x)); n.setAttribute("y1", f2(a.y)); n.setAttribute("x2", f2(b.x)); n.setAttribute("y2", f2(b.y)); };
  const setC = (n, p) => { n.setAttribute("cx", f2(p.x)); n.setAttribute("cy", f2(p.y)); };
  const poly = (n, pts) => n.setAttribute("points", pts.map((p) => `${f2(p.x)},${f2(p.y)}`).join(" "));

  // ── Encabezado del capítulo ─────────────────────────────────────────────────
  const last = X.caps[X.caps.length - 1];
  X.caps.forEach((c) => {
    const n = `#cap-${c.ci} .inner`;
    tl.fromTo(n, { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.55, ease: "power3.out", immediateRender: false }, c.start + 0.05);
    if (c !== last) tl.to(n, { opacity: 0, duration: 0.3, ease: "power1.in" }, c.end - 0.32);
  });
  if (X.thumb) X.caps.forEach((c) => tl.set(`#cap-${c.ci} .inner`, { opacity: 1, x: 0 }, 0));

  // ── Tarjetas ────────────────────────────────────────────────────────────────
  // Figura sentada de frente: cadera en H, tronco inclinado th grados (+ = hacia la derecha de la tarjeta).
  function torsoParts(g) {
    return { torso: seg(g, COL.shirt, 54), hair: el("circle", { r: 24, fill: COL.hair }, g), face: el("circle", { r: 20, fill: COL.skin }, g) };
  }
  function placeTorso(p, H, th, len) {
    const d = { x: Math.sin(rad(th)), y: -Math.cos(rad(th)) }, n = { x: Math.cos(rad(th)), y: Math.sin(rad(th)) };
    const S = { x: H.x + d.x * len, y: H.y + d.y * len };
    setL(p.torso, { x: H.x + d.x * 18, y: H.y + d.y * 18 }, S);
    setC(p.hair, { x: S.x + d.x * 44, y: S.y + d.y * 44 });
    setC(p.face, { x: S.x + d.x * 41, y: S.y + d.y * 41 + 4 });
    return { S, d, n, SL: { x: S.x - n.x * 28, y: S.y - n.y * 28 }, SR: { x: S.x + n.x * 28, y: S.y + n.y * 28 } };
  }
  const floorLine = (g) => el("line", { x1: 10, y1: 302, x2: 290, y2: 302, stroke: COL.floor, "stroke-width": 6, "stroke-linecap": "round" }, g);

  const BUILD = {
    // Mariposa de frente: v 0 = rodillas arriba, 1 = rodillas cerca del piso. Manos en los pies.
    mariposa(g) {
      floorLine(g);
      const H = { x: 150, y: 262 }, legs = ["L", "R"].map((s) => ({ s: s === "L" ? -1 : 1, th: seg(g, COL.pants, 26), sh: seg(g, COL.pants, 22), ft: el("ellipse", { rx: 16, ry: 9, fill: COL.skin }, g) }));
      const p = torsoParts(g), arms = [seg(g, COL.skin, 13), seg(g, COL.skin, 13)];
      return (v) => {
        const sh = placeTorso(p, H, 0, 108);
        legs.forEach((L) => {
          const hip = { x: H.x + L.s * 24, y: H.y + 6 }, a = rad(-62 + v * 66);
          const K = { x: hip.x + L.s * Math.cos(a) * 112, y: hip.y + Math.sin(a) * 112 };
          const F = { x: H.x + L.s * 14, y: 290 };
          setL(L.th, hip, K); setL(L.sh, K, F); setC(L.ft, F);
        });
        setL(arms[0], sh.SL, { x: H.x - 14, y: 284 }); setL(arms[1], sh.SR, { x: H.x + 14, y: 284 });
      };
    },
    // Inclinación lateral sentado: pierna estirada a la izquierda de la tarjeta (lado −1 la espeja), la otra flexionada.
    // v −1 = inclinado hacia la pierna estirada (brazo de afuera por arriba), 0 = derecho, 1 = hacia el otro lado.
    lateral(g) {
      floorLine(g);
      const H = { x: 160, y: 262 };
      const ext = seg(g, COL.pants, 24), extF = el("ellipse", { rx: 9, ry: 15, fill: COL.skin }, g);
      const bt = seg(g, COL.pants, 26), bs = seg(g, COL.pantsFar, 22);
      const p = torsoParts(g), aL = el("polyline", { fill: "none", stroke: COL.skin, "stroke-width": 13, "stroke-linecap": "round", "stroke-linejoin": "round" }, g),
        aR = el("polyline", { fill: "none", stroke: COL.skin, "stroke-width": 13, "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
      return (v) => {
        setL(ext, { x: H.x - 24, y: H.y + 8 }, { x: 22, y: 288 }); setC(extF, { x: 16, y: 280 });
        setL(bt, { x: H.x + 24, y: H.y + 8 }, { x: 250, y: 284 }); setL(bs, { x: 250, y: 288 }, { x: 170, y: 292 });
        const sh = placeTorso(p, H, v * 40, 104), k = Math.abs(v);
        const over = (S, sgn) => { const a = rad(v * 40 + sgn * 34); return { x: S.x + Math.sin(a) * 120, y: S.y - Math.cos(a) * 120 }; };
        const elbow = (S, W) => lerp(S, W, 0.5);
        // v < 0: mano izquierda va hacia el pie, la derecha pasa por arriba; v > 0 al revés.
        const restL = { x: 100, y: 268 }, restR = { x: 222, y: 270 };
        const WL = v <= 0 ? lerp(restL, { x: 44, y: 276 }, k) : lerp(restL, over(sh.SL, 1), k);
        const WR = v <= 0 ? lerp(restR, over(sh.SR, -1), k) : lerp(restR, { x: 262, y: 292 }, k);
        poly(aL, [sh.SL, elbow(sh.SL, WL), WL]); poly(aR, [sh.SR, elbow(sh.SR, WR), WR]);
      };
    },
    // Sentado con piernas cruzadas, brazos cruzados al pecho; v −1…1 = el tronco se balancea hacia un lado y el otro.
    balanceo(g) {
      floorLine(g);
      const H = { x: 150, y: 262 };
      const tL = seg(g, COL.pants, 26), tR = seg(g, COL.pants, 26), sL = seg(g, COL.pantsFar, 22), sR = seg(g, COL.pants, 22);
      const p = torsoParts(g), a1 = el("polyline", { fill: "none", stroke: COL.skin, "stroke-width": 13, "stroke-linecap": "round", "stroke-linejoin": "round" }, g),
        a2 = el("polyline", { fill: "none", stroke: COL.skinFar, "stroke-width": 13, "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
      return (v) => {
        setL(tL, { x: H.x - 22, y: H.y + 8 }, { x: 52, y: 284 }); setL(tR, { x: H.x + 22, y: H.y + 8 }, { x: 248, y: 284 });
        setL(sL, { x: 52, y: 290 }, { x: 186, y: 294 }); setL(sR, { x: 248, y: 290 }, { x: 114, y: 296 });
        const sh = placeTorso(p, H, v * 26, 108), c = { x: sh.S.x - sh.d.x * 44, y: sh.S.y - sh.d.y * 44 };
        const e1 = { x: sh.SL.x - sh.d.x * 40 - sh.n.x * 4, y: sh.SL.y - sh.d.y * 40 - sh.n.y * 4 }, e2 = { x: sh.SR.x - sh.d.x * 40 + sh.n.x * 4, y: sh.SR.y - sh.d.y * 40 + sh.n.y * 4 };
        poly(a1, [sh.SL, e1, { x: c.x + sh.n.x * 30, y: c.y + sh.n.y * 30 }]);
        poly(a2, [sh.SR, e2, { x: c.x - sh.n.x * 30 + sh.d.x * 12, y: c.y - sh.n.y * 30 + sh.d.y * 12 }]);
      };
    },
    // Torsión sentado vista de arriba: piernas cruzadas fijas; hombros giran v·48°. v > 0 = gira a la derecha
    // (mano izquierda en la rodilla derecha, la derecha atrás); v < 0 al revés.
    torsion(g) {
      const C = { x: 150, y: 170 };
      [[-1, COL.pants], [1, COL.pants]].forEach(([s, col]) => {
        el("line", { x1: C.x + s * 20, y1: 196, x2: C.x + s * 104, y2: 246, stroke: col, "stroke-width": 30, "stroke-linecap": "round" }, g);
        el("line", { x1: C.x + s * 104, y1: 250, x2: C.x - s * 30, y2: 282, stroke: COL.pantsFar, "stroke-width": 24, "stroke-linecap": "round" }, g);
      });
      el("ellipse", { cx: C.x, cy: 196, rx: 46, ry: 30, fill: COL.pants }, g);
      const aL = el("polyline", { fill: "none", stroke: COL.skin, "stroke-width": 13, "stroke-linecap": "round", "stroke-linejoin": "round" }, g),
        aR = el("polyline", { fill: "none", stroke: COL.skin, "stroke-width": 13, "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
      const sh = seg(g, COL.shirt, 50), head = el("circle", { r: 27, fill: COL.hair }, g), nose = el("circle", { r: 7, fill: COL.skin }, g);
      return (v) => {
        const a = rad(v * 48), n = { x: Math.cos(a), y: Math.sin(a) }, f = { x: Math.sin(a), y: -Math.cos(a) };
        const L = { x: C.x - n.x * 62, y: C.y - n.y * 62 }, R = { x: C.x + n.x * 62, y: C.y + n.y * 62 };
        setL(sh, L, R); setC(head, C); setC(nose, { x: C.x + f.x * 28, y: C.y + f.y * 28 });
        const k = Math.abs(v), restL = { x: 66, y: 236 }, restR = { x: 234, y: 236 };
        const WL = v >= 0 ? lerp(restL, { x: 226, y: 240 }, k) : lerp(restL, { x: 76, y: 104 }, k);
        const WR = v >= 0 ? lerp(restR, { x: 224, y: 104 }, k) : lerp(restR, { x: 74, y: 240 }, k);
        poly(aL, [L, lerp(L, WL, 0.5), WL]); poly(aR, [R, lerp(R, WR, 0.5), WR]);
      };
    },
    // De pie de frente con las piernas bien abiertas; v 0 = tronco arriba (manos en los muslos), 1 = plegado hacia
    // adelante con las manos en el piso entre los pies. El tronco se acorta (escorzo) y la cabeza baja entre las piernas.
    pancake(g) {
      floorLine(g);
      const H = { x: 150, y: 148 };
      const legs = [-1, 1].map((s) => ({ s, l: seg(g, s < 0 ? COL.pantsFar : COL.pants, 28), f: el("ellipse", { rx: 17, ry: 9, fill: COL.skin }, g) }));
      const torso = seg(g, COL.shirt, 54), hair = el("circle", { r: 24, fill: COL.hair }, g), face = el("circle", { r: 20, fill: COL.skin }, g);
      const arm = () => el("polyline", { fill: "none", stroke: COL.skin, "stroke-width": 13, "stroke-linecap": "round", "stroke-linejoin": "round" }, g);
      const aL = arm(), aR = arm();
      return (v) => {
        legs.forEach((L) => {
          const F = { x: H.x + L.s * 112, y: 292 };
          setL(L.l, { x: H.x + L.s * 22, y: H.y + 6 }, F); setC(L.f, { x: F.x + L.s * 8, y: 296 });
        });
        const k = -Math.cos(rad(v * 128)); // −1 tronco vertical, +0,6 plegado (proyección hacia abajo)
        const S = { x: H.x, y: H.y + k * 108 }, d = k < 0 ? -1 : 1;
        setL(torso, { x: H.x, y: H.y + d * 10 }, S);
        setC(hair, { x: S.x, y: S.y + d * 44 });
        setC(face, { x: S.x, y: S.y + d * 41 + 4 });
        face.setAttribute("opacity", v < 0.5 ? 1 : 0); // plegado se ve la coronilla
        const SL = { x: S.x - 28, y: S.y }, SR = { x: S.x + 28, y: S.y };
        const m = Math.max(0, Math.min(1, (v - 0.25) / 0.6));
        const WL = lerp({ x: H.x - 52, y: H.y + 46 }, { x: H.x - 44, y: 294 }, m), WR = lerp({ x: H.x + 52, y: H.y + 46 }, { x: H.x + 44, y: 294 }, m);
        poly(aL, [SL, lerp(lerp(SL, WL, 0.5), { x: SL.x - 30, y: SL.y }, 0.3), WL]);
        poly(aR, [SR, lerp(lerp(SR, WR, 0.5), { x: SR.x + 30, y: SR.y }, 0.3), WR]);
      };
    },
  };

  const cards = X.cards.map((c) => {
    const g = $(`cg-${c.id}`);
    const draw = g && BUILD[c.tipo] ? BUILD[c.tipo](g) : null;
    return { c, draw };
  }).filter((x) => x.draw);
  const ease = (k) => 0.5 - Math.cos(Math.PI * k) / 2;
  const valueAt = (c, t) => {
    let v = c.v0;
    for (const s of c.segs) {
      if (t >= s.t1) v = s.b;
      else { if (t > s.t0) v = s.a + (s.b - s.a) * ease((t - s.t0) / (s.t1 - s.t0)); break; }
    }
    return v;
  };
  cards.forEach(({ c }) => {
    const n = $(`card-${c.id}`), t0 = n ? Number(n.dataset.start) : 0;
    tl.fromTo(`#card-${c.id} .inner`, { opacity: 0, x: 40 }, { opacity: 1, x: 0, duration: 0.5, ease: "power2.out", immediateRender: false }, t0 + 0.3);
  });

  // ── Cuenta regresiva ────────────────────────────────────────────────────────
  const holds = X.holds.map((h) => ({ h, ring: $(`ring-${h.id}`), num: $(`num-${h.id}`) })).filter((x) => x.ring);
  holds.forEach(({ h }) => {
    tl.fromTo(`#hold-${h.id} .inner`, { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)", immediateRender: false }, h.t0 - 0.3);
    tl.to(`#hold-${h.id} .inner`, { opacity: 0, duration: 0.3 }, h.t0 + h.dur + 0.15);
  });

  // ── Reloj ───────────────────────────────────────────────────────────────────
  let now = -1;
  function render(t) {
    cards.forEach(({ c, draw }) => draw(valueAt(c, t)));
    holds.forEach(({ h, ring, num }) => {
      const k = Math.max(0, Math.min(1, (t - h.t0) / h.dur));
      ring.setAttribute("stroke-dasharray", `${f2((1 - k) * 1000) / 1000} 1`);
      num.textContent = String(Math.max(0, Math.ceil(h.dur * (1 - k) - 1e-6)));
    });
  }
  const clock = { t: function (v) { if (arguments.length === 0) return now; now = v; render(v); } };
  tl.fromTo(clock, { t: 0 }, { t: X.total, duration: X.total, ease: "none", immediateRender: false }, 0);
  render(0);
  tl.seek(0);
})();
