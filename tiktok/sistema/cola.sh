#!/bin/bash
# Cola de render: coge cada spec nueva de specs/, la construye y la deja comprimida en out/<id>/.
cd ${FABRICA:-/home/user/fabrica} && cd ${REPO:-/home/user/ceos-instagram}
FIN=$(( $(date +%s) + 6600 ))
while [ $(date +%s) -lt $FIN ]; do
  for s in $(sed "s|.*|${FABRICA:-/home/user/fabrica}/specs/&.json|" ${FABRICA:-/home/user/fabrica}/orden.txt); do
    [ -e "$s" ] || continue; [ $(date +%s) -lt $FIN ] || exit 0
    id=$(basename "$s" .json); o=${FABRICA:-/home/user/fabrica}/out/$id
    [ -e "$o/tiktok.mp4" ] || [ -e "$o/FALLO" ] && continue
    mkdir -p "$o"; cp "$s" "$o/spec.json"
    seed=$(( $(echo -n "$id" | cksum | cut -d' ' -f1) % 97 ))
    if python3 toolkit/reels/build_reel.py "$o/spec.json" "$o" $seed > ${FABRICA:-/home/user/fabrica}/logs/$id.log 2>&1; then
      ffmpeg -y -loglevel error -i "$o/reel.mp4" -c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -crf 24 -preset medium -c:a aac -b:a 160k -movflags +faststart "$o/tiktok.mp4" && rm -f "$o/reel.mp4"
      echo "$(date +%H:%M) ok $id" >> ${FABRICA:-/home/user/fabrica}/logs/cola.log
    else
      touch "$o/FALLO"; echo "$(date +%H:%M) FALLO $id" >> ${FABRICA:-/home/user/fabrica}/logs/cola.log
    fi
  done
  pend=0; for s in $(sed "s|.*|${FABRICA:-/home/user/fabrica}/specs/&.json|" ${FABRICA:-/home/user/fabrica}/orden.txt); do i=$(basename $s .json); [ -e ${FABRICA:-/home/user/fabrica}/out/$i/tiktok.mp4 ] || [ -e ${FABRICA:-/home/user/fabrica}/out/$i/FALLO ] || pend=1; done; [ $pend = 0 ] && exit 0; sleep 20
done
