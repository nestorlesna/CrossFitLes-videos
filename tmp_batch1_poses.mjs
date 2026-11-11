import fs from "fs";

const base = (slug, name, category, tags, descripcion, notas, rig, props, initialPose, poses, pronuncia) => ({
  slug, name, category, tags, descripcion, notas,
  music: true, musicVolume: 0.18, rig, props,
  initialPose, poses, pronuncia, revisado: false, frames: []
});

const data = [
  base(
    "heel-elevated-goblet-squat",
    "Heel-Elevated Goblet Squat",
    "ACTIVACIÓN · FUERZA",
    ["Sentadilla", "Goblet", "Talones elevados", "Cuádriceps", "Glúteos", "Movilidad", "CrossFit"],
    "Sentadilla goblet con los talones elevados sobre una cuña o discos. La elevación permite más profundidad manteniendo el torso erguido.",
    "Talones y planta apoyados en la cuña; codos dentro de las rodillas en el fondo; cadera por debajo de las rodillas.",
    { x: 500, y: 1500, scale: 0.9 },
    [
      { type: "box", x0: -130, x1: -15, h: 30 },
      { type: "dumbbell", hand: "near", side: true, r: 42 }
    ],
    "STAND",
    {
      STAND: { hip: [0, -490], ankle: [0, -20], ft: 14, b: 0, hd: 0, g: 0, ua: 12, fa: 142, ua2: 8, fa2: 146 },
      HALF: { hip: [-80, -365], ankle: [0, -20], ft: 14, b: 20, hd: 10, g: 0, ua: -6, fa: 142, ua2: -10, fa2: 146 },
      BOTTOM: { hip: [-145, -215], ankle: [0, -20], ft: 14, b: 34, hd: 22, g: 0, ua: -22, fa: 142, ua2: -26, fa2: 146 },
      FWD_BAD: { hip: [-120, -235], ankle: [0, -20], ft: 14, b: 60, hd: 46, g: 0, ua: -18, fa: 142, ua2: -22, fa2: 146 }
    },
    {
      "Heel-Elevated Goblet Squat": "Jil elevéited góublet skuat",
      "goblet squat": "góublet skuat",
      "heel-elevated": "jil elevéited",
      "squat": "skuat"
    }
  ),
  base(
    "kettlebell-turkish-sit-up",
    "Kettlebell Turkish Sit-Up",
    "ACTIVACIÓN · CORE",
    ["Kettlebell", "Core", "Abdomen", "Turkish sit-up", "Estabilidad", "CrossFit"],
    "Acostado boca arriba con una kettlebell sostenida con el brazo extendido hacia el techo. Sentarse hasta quedar con el torso erguido manteniendo la kettlebell arriba y volver a acostarse con control.",
    "Brazo con la kettlebell vertical y bloqueado; mirada en la kettlebell; pies apoyados y rodillas dobladas; no empujar con la mano libre.",
    { x: 560, y: 1470, scale: 0.86 },
    [{ type: "kettlebell", off: [0, -12], swing: true }],
    "FLAT",
    {
      FLAT: { hip: [0, -12], s: -28.6, t: -147.3, s2: -31, t2: -145, ft: 0, ft2: 0, b: -90, hd: -70, g: 0, ua: 180, fa: 0, ua2: 80, fa2: 0 },
      HALF: { hip: [0, -12], s: -28.6, t: -147.3, s2: -31, t2: -145, ft: 0, ft2: 0, b: -38, hd: -28, g: 0, ua: 180, fa: 0, ua2: 70, fa2: 12 },
      UP: { hip: [0, -12], s: -28.6, t: -147.3, s2: -31, t2: -145, ft: 0, ft2: 0, b: 58, hd: 50, g: 0, ua: 180, fa: 0, ua2: 45, fa2: 60 },
      ARM_BAD: { hip: [0, -12], s: -28.6, t: -147.3, s2: -31, t2: -145, ft: 0, ft2: 0, b: 58, hd: 50, g: 0, ua: 142, fa: 42, ua2: 40, fa2: 60 }
    },
    {
      "Kettlebell Turkish Sit-Up": "Kételbel túrkish sit ap",
      "Turkish Sit-Up": "túrkish sit ap",
      "kettlebell": "kételbel",
      "sit-up": "sit ap"
    }
  ),
  base(
    "lateral-raise-to-overhead",
    "Lateral Raise to Overhead",
    "ACTIVACIÓN · HOMBRO",
    ["Hombros", "Deltoides", "Elevación lateral", "Overhead", "Disco", "Activación", "CrossFit"],
    "De pie con discos muy livianos, elevar los brazos lateralmente hasta la horizontal y continuar el arco hasta overhead. Bajar por el mismo camino.",
    "Pesos muy livianos; movimiento continuo y fluido, sin pausa; core activo; no encogerse de hombros.",
    { x: 520, y: 1500, scale: 0.9 },
    [
      { type: "plate", hand: "near", off: [0, -12], r: 40 },
      { type: "plate", hand: "far", off: [0, -12], r: 40 }
    ],
    "DOWN",
    {
      DOWN: { s: 0, t: 0, b: 0, hd: 0, g: 0, ua: 4, fa: 4, ua2: 2, fa2: 2, al: 1 },
      SIDE: { s: 0, t: 0, b: 0, hd: 0, g: 0, ua: 90, fa: 0, ua2: 88, fa2: 0, al: 0.34 },
      OH: { s: 0, t: 0, b: 0, hd: 0, g: 0, ua: 176, fa: 0, ua2: 174, fa2: 0, al: 0.34 },
      SHRUG_BAD: { s: 0, t: 0, b: 8, hd: 2, g: 0, ua: 82, fa: 38, ua2: 86, fa2: 34, al: 0.4 }
    },
    {
      "Lateral Raise to Overhead": "Láteral réis tu óverjed",
      "lateral raise": "láteral réis",
      "overhead": "óverjed"
    }
  ),
  base(
    "plank-to-opposite-toe-touch",
    "Plank to Opposite Toe Touch",
    "ENTRADA EN CALOR · CORE",
    ["Core", "Plancha", "Pike", "Coordinación cruzada", "Entrada en calor", "Activación", "CrossFit"],
    "Desde plancha alta, elevar la cadera tipo pike y llevar una mano al pie contrario. Volver a plancha y alternar lados.",
    "Combina estabilidad de core, flexión de cadera y coordinación cruzada; también se llama Alternating o Crossbody Plank Toe Touch.",
    { x: 460, y: 1504, scale: 0.8 },
    [],
    "PLANK",
    {
      PLANK: { hip: [141.6, -222.8], ankle: [-300, -62], ft: 55, b: 70, hd: 74, g: 1, hx: 405, hy: 15, ed: 1 },
      PIKE: { s: 0, t: 0, b: 130, hd: 104, g: 1, hx: 320, hy: 15, ed: 1 },
      TOE: { s: 0, t: 0, b: 132, hd: 108, g: 1, hx: 55, hy: 10, ed: 1, g2: 1, hx2: 255, hy2: 10, ed2: 1 },
      KNEE_BAD: { hip: [0, -320], ankle: [0, 0], b: 118, hd: 96, g: 1, hx: 90, hy: 15, ed: 1 }
    },
    {
      "Plank to Opposite Toe Touch": "Planc tu ópousit tou toch",
      "plank": "planc",
      "opposite toe touch": "ópousit tou toch",
      "toe touch": "tou toch"
    }
  ),
  base(
    "plank-up-down",
    "Plank Up-Down",
    "ACTIVACIÓN · CORE",
    ["Core", "Plancha", "Antebrazos", "Tríceps", "Estabilidad", "Activación", "CrossFit"],
    "Desde plancha alta, descender a plancha baja sobre los antebrazos y volver a subir, manteniendo las caderas estables. Alternar el brazo que lidera.",
    "Caderas estables, sin rotar; core siempre activo; alternar el brazo de inicio.",
    { x: 460, y: 1504, scale: 0.8 },
    [],
    "PLANK",
    {
      PLANK: { hip: [141.6, -222.8], ankle: [-300, -62], ft: 55, b: 70, hd: 74, g: 1, hx: 405, hy: 15, ed: 1 },
      FOREARM: { hip: [141, -122], ankle: [-300, -62], ft: 55, b: 80, hd: 84, g: 0, ua: 0, fa: 90, ua2: 0, fa2: 90 },
      SAG_BAD: { hip: [141, -60], ankle: [-300, -62], ft: 55, b: 86, hd: 88, g: 0, ua: 0, fa: 90, ua2: 0, fa2: 90 }
    },
    {
      "Plank Up-Down": "Planc ap dáun",
      "plank": "planc",
      "up-down": "ap dáun",
      "forearm plank": "fóraram planc"
    }
  )
];

for (const d of data) {
  const p = `ejercicios/${d.slug}.json`;
  fs.writeFileSync(p, JSON.stringify(d, null, 2) + "\n", "utf8");
  console.log("wrote", p);
}
