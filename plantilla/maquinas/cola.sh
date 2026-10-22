#!/usr/bin/env bash
# Cola de trabajo para muchos videos de máquinas (GENERAR_VIDEOS_MAQUINAS.md §10):
#   bash plantilla/maquinas/cola.sh render clave1 clave2 ...   → --render de a 2 en paralelo
#   bash plantilla/maquinas/cola.sh build  clave1 clave2 ...   → make-exercise (voz + check + snapshots) de a 1
# Logs en videos/_logs/<clave>.log (build) y <clave>.r.log (render). Al final imprime duración y check de cada uno.
cd "$(dirname "$0")/../.."
mkdir -p videos/_logs
mode=$1; shift
claves=("$@")
if [ "$mode" = render ]; then
  sfx=.r
  for ((i = 0; i < ${#claves[@]}; i += 2)); do
    for c in "${claves[@]:i:2}"; do node plantilla/make-exercise.mjs "$c" --render > "videos/_logs/$c$sfx.log" 2>&1 & done
    wait
  done
else
  sfx=
  for c in "${claves[@]}"; do node plantilla/make-exercise.mjs "$c" > "videos/_logs/$c.log" 2>&1; done
fi
for c in "${claves[@]}"; do
  echo "$c: $(grep -o '✓ index.html — [^,]*, [0-9.]*s' "videos/_logs/$c$sfx.log") check=$(grep -c 'Check passed' "videos/_logs/$c$sfx.log") $(grep -o 'salida/[^ ]*\.mp4' "videos/_logs/$c$sfx.log" | head -1)"
done
