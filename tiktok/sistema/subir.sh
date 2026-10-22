#!/bin/bash
# Copia los reels renderizados a ceos-instagram/tiktok/<id>/ y hace push. Imprime id SHA.
set -e
cd ${REPO:-/home/user/ceos-instagram}
git pull -q --rebase origin main
n=0
for o in ${FABRICA:-/home/user/fabrica}/out/*/; do
  id=$(basename "$o"); [ -e "$o/tiktok.mp4" ] || continue
  [ -e "tiktok/$id/reel.mp4" ] && continue
  mkdir -p "tiktok/$id"; cp "$o/tiktok.mp4" "tiktok/$id/reel.mp4"; cp "$o/portada.jpg" "tiktok/$id/portada.jpg"; cp "$o/spec.json" "tiktok/$id/spec.json"
  git add "tiktok/$id"; n=$((n+1))
done
[ $n -gt 0 ] && git commit -qm "TikTok: $n reels nuevos para programar en Metricool

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" && git push -q origin HEAD:main
echo "subidos $n · $(git rev-parse HEAD)"
