import fs from 'fs';
import path from 'path';

function copyAndModify(srcSlug, dstSlug, name, category, tags, desc, notas, props, extra={}) {
  const srcPath = path.join('ejercicios', srcSlug + '.json');
  const dstPath = path.join('ejercicios', dstSlug + '.json');
  const src = JSON.parse(fs.readFileSync(srcPath, 'utf8'));
  const dst = JSON.parse(JSON.stringify(src));
  dst.slug = dstSlug;
  dst.name = name;
  if(category) dst.category = category;
  if(tags) dst.tags = tags;
  if(desc) dst.descripcion = desc;
  if(notas !== undefined) dst.notas = notas;
  if(props !== undefined) dst.props = props;
  if(extra.pronuncia) dst.pronuncia = extra.pronuncia;
  if(extra.rig) dst.rig = extra.rig;
  if(extra.initialPose) dst.initialPose = extra.initialPose;
  if(extra.youtube) dst.youtube = extra.youtube;
  if(extra.miniatura) dst.miniatura = extra.miniatura;
  if(extra.frames) dst.frames = extra.frames;
  dst.revisado = false;
  if(dst.music === undefined) { dst.music = true; dst.musicVolume = 0.18; }
  fs.writeFileSync(dstPath, JSON.stringify(dst, null, 2), 'utf8');
  console.log('wrote', dstSlug);
}

// 1
copyAndModify('band-external-rotation', 'banded-ankle-dorsiflexion-stretch', 
  'Banded Ankle Dorsiflexion Stretch',
  'CROSSFIT · ENTRADA EN CALOR',
  ['Tobillos', 'Gemelos', 'Movilidad'],
  'Con una banda elástica anclada al suelo alrededor del tobillo, empujar la rodilla hacia adelante sobre los dedos del pie para abrir el rango de dorsiflexión del tobillo. Mantener el talón apoyado en el suelo.',
  'Con banda baja anclada al suelo alrededor del tobillo; talón siempre apoyado y rodilla que va hacia adelante sobre los dedos.',
  [{ type: 'band', anchor: [200, 100], post: [200, 650], hand: 'near', layer: 'mid' }],
  { pronuncia: {"Banded Ankle Dorsiflexion Stretch": "Bánded ánkel dorsifléxion stréch"}, rig: {x: 460, y: 1510, scale: 0.82} }
);

// 2
copyAndModify('band-triceps-pushdown', 'banded-prone-leg-curl',
  'Banded Prone Leg Curl',
  'CROSSFIT · ENTRADA EN CALOR',
  ['Isquiotibiales', 'Piernas', 'Activación'],
  'Acostado boca abajo con una banda elástica anclada a los tobillos o con la banda bajo el pie, flexionar la rodilla llevando el talón hacia los glúteos contra la resistencia y volver controlado.',
  'Boca abajo con banda elástica para trabajar la flexión de rodilla; movimiento controlado sin tirar con impulso.',
  [{ type: 'band', anchor: [400, 900], post: [420, 1300], hand: 'both' }],
  { pronuncia: {"Banded Prone Leg Curl": "Bánded prón leg córl"}, rig: {x: 500, y: 1508, scale: 0.8} }
);

// 3
copyAndModify('burpee-over-the-bar', 'burpee-to-bar',
  'Burpee to Bar',
  'CROSSFIT · WOD',
  ['Pecho', 'Core', 'Tracción'],
  'Burpee hasta plancha, bajar al pecho, empujar y saltar para agarrar la barra de dominadas con salto, bajando controlado.',
  'Transición burpee → salto a barra; coordinación y tracción.',
  [{ type: "pullupbar", x: 700, y: 1200, h: 900 }],
  { pronuncia: {"Burpee to Bar": "Burpii tú bar"}, rig: {x: 620, y: 1508, scale: 0.68} }
);

// 4
copyAndModify('mountain-climbers', 'cross-body-mountain-climbers',
  'Cross Body Mountain Climbers',
  'CROSSFIT · WOD',
  ['Core', 'Oblicuos', 'Cardio'],
  'En plancha alta, llevar la rodilla hacia el codo contrario cruzando el cuerpo, alternando lados a ritmo controlado.',
  'Enfoque en oblicuos con cruce; mantener cadera baja y estable.',
  null,
  { pronuncia: {"Cross Body Mountain Climbers": "Cross bódi máuntin kláimars"}, rig: {x: 230, y: 1504, scale: 0.85} }
);

// 5
copyAndModify('box-step-up', 'db-lateral-step-over',
  'DB Lateral Step-Over',
  'CROSSFIT · WOD',
  ['Piernas', 'Glúteos', 'Estabilidad'],
  'Con una mancuerna en cada mano, dar un paso lateral sobre un obstáculo o caja, cruzando la pierna y colocando el pie al otro lado con control, alternando o en recorrido.',
  'Paso lateral controlado sobre obstáculo; mantener estable con mancuernas.',
  [
    { type: "box", x: 500, y: 1360, w: 200, h: 180 },
    { type: "dumbbell", hand: "near", side: 1 },
    { type: "dumbbell", hand: "far", side: 1 }
  ],
  { pronuncia: {"DB Lateral Step-Over": "Di bíi láteral stép óuver"}, rig: {x: 520, y: 1510, scale: 0.78} }
);
