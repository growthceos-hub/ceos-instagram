# Reels diarios de Ceos Growth — instrucciones

Cada día se publican **5 reels de valor**, uno cada media hora: **16:00, 16:30, 17:00, 17:30 y 18:00** (hora de Madrid). Cada ejecución programada hace y publica **UN** reel (su "hueco" 1–5).

## Contenido
- Reel de VALOR (no vender): captación, Meta Ads, formularios, creatividades, guiones, grabación, CRM, seguimiento de leads, llamadas de venta, métricas, landing pages, WhatsApp, email…
- Tema nuevo cada vez: mira `reels-publicados.md`, `publicados.md` e `historias-publicadas.md` y no repitas. Los 5 reels del día, de temas distintos entre sí.
- Estructura fija de 5 escenas (≈28 s):
  1. **hook** (5 s): pregunta-gancho sobre un dolor del empresario, 2–3 líneas, con un mockup y un pie tipo "3 pasos para…".
  2–4. **step** (6–6,5 s cada una): `label` "PASO 1/2/3" (o "ERROR 1", "NÚMERO 1", "MIN 0–2"…), título corto de 2 líneas con la parte clave en `<em>`, un mockup distinto en cada escena y una `note` corta con la parte fuerte en `<b>`.
  5. **cta** (6 s): título de 2 líneas + 3 `items` de resumen + botón "Síguenos para más tips".
- Mockups disponibles (`toolkit/reels/gen_reel.py`, funciones `m_*`): `chat`, `timer`, `timeline`, `checklist`, `ad`, `form`, `compare`, `bars`, `script`. Varía los tipos entre escenas y entre reels.
- Poco texto: títulos de 2 líneas (máx. ~17 caracteres por línea a 112 px; en el hook usa `size` 122–140), ítems de ≤ 30 caracteres, líneas de chat de ≤ 26 caracteres.
- **Nunca inventes estadísticas** presentadas como reales. Los mockups con datos llevan "EJEMPLO" (ya lo pone el generador). Sin emojis dentro del vídeo (no se renderizan).
- **Marca**: todo como Ceos Growth y @ceos.growth. **Nunca** nombres personales del equipo en vídeo, caption o hashtags.
- Referencias: `reels/2026-09-26*/spec.json`.

## Pasos
1. Dependencias como en INSTRUCCIONES.md (`cd toolkit && npm i --silent` + playwright + ffmpeg; `pip install --break-system-packages -q scipy numpy` si faltan).
2. Crea `reels/AAAA-MM-DD-N/spec.json` (N = hueco 1–5) con `topic`, `scenes` y `caption`.
   - Caption: primera línea = pregunta-gancho + 1 emoji; 1 frase de contexto; los pasos con "→"; cierre "Guárdalo y síguenos para más tips 🧡"; 6–7 hashtags en español con #ceosgrowth.
3. `python3 toolkit/reels/build_reel.py reels/AAAA-MM-DD-N/spec.json reels/AAAA-MM-DD-N <N + día del año>`. La semilla elige el estilo de música (épica/trap, house, cinemática, synthwave o phonk) y la progresión de acordes: con N + día del año, los 5 reels del día llevan 5 estilos distintos y cambian de un día a otro. No uses otra semilla. Mira `reels/AAAA-MM-DD-N/_tmp/check1..5.jpg`: nada cortado, solapado ni fuera de marco. Si algo falla, corrige el spec y vuelve a construir.
4. `git add reels/AAAA-MM-DD-N` + commit (mensaje terminado en "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>") + `git pull --rebase` + push a main. URL fijada al commit: `https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/<SHA>/reels/AAAA-MM-DD-N/reel.mp4` (comprueba que da 200).
5. **Instagram** (@ceos.growth, id 17841469551116816) vía Zapier "Instagram for Business" → `_zap_raw_request` (Make API Mutating Request):
   - POST `https://graph.facebook.com/v21.0/17841469551116816/media` con querystring `media_type=REELS`, `share_to_feed=true`, `video_url=<url>`, `caption=<caption>`.
   - GET `https://graph.facebook.com/v21.0/<id>?fields=status_code` hasta `FINISHED` (espera ~30 s entre consultas; si pasa de 4 min, crea el contenedor de nuevo).
   - POST `https://graph.facebook.com/v21.0/17841469551116816/media_publish` con `creation_id=<id>`. **Una sola vez.** Si falla, comprueba en `GET /17841469551116816/media?fields=caption,timestamp&limit=5` que no esté ya publicado antes de reintentar.
6. **Facebook** (página **Ceos Marketing**, id 434829573050729) vía Zapier "Facebook Pages" → `page_video` (connection_id 66508057) con `page=434829573050729`, `source=<url>`, `title=<gancho>`, `description=<caption sin hashtags ni emojis>`. **Nunca** en la página "Ceos Growth Hugo" ni en otras páginas.
7. **LinkedIn**: solo si Zapier "LinkedIn" tiene una acción que publique vídeo en la página de empresa de Ceos Growth; si no, sáltalo sin error.
8. Añade una fila a `reels-publicados.md` (fecha, hueco, tema, enlace de Instagram) y haz push.
