# 20 reels meme diarios de Ceos Growth — instrucciones

Cada día se crean **20 reels meme nuevos** (formato POV, como `reels/meme-*`) y se publican **todos seguidos en una sola tanda** hacia las **20:00** (Madrid) en Instagram @ceos.growth. **Solo en la pestaña Reels**: siempre `share_to_feed=false`.

## Formato (no cambiar)
- Motor: `toolkit/reels/pov_reel.py` + `toolkit/reels/memes.py` (fondo negro, cabecera tipo tweet de Ceos Growth, texto POV, "pantalla" animada en caja redondeada, remate con zoom + temblor + gris, **solo efectos de sonido, sin música**; la música comercial la añade Hugo a mano en la app si quiere).
- Mira las clases de `memes.py` (`Visto`, `Cunado`, `Cuota`, `Socio`, `Sorteo`, `Informe`, `Torre`) y los vídeos `reels/meme-*/reel.mp4` como referencia de nivel.
- Cada meme es una clase con `POV`, `DUR` (6,5–8 s), `PUNCH` (segundo del remate), `FOCUS` (x,y del zoom, dentro de 960×1000), `SFX` (eventos `pop|tick|ding|boom|typing:dur|count:dur` con `@segundo`) y `draw(t)` → imagen 960×1000.

## Contenido
- Público: dueños de negocio (constructoras, SaaS, infoproductos, pymes) que invierten en marketing. Humor de situaciones reales: leads que no contestan, cuñados que "saben de Facebook", agencias que cobran sin resultados, informes con todo verde menos las ventas, socios que quieren resultados en 3 días, sorteos, formularios basura, llamadas que no se hacen, presupuestos, CRM vacío, el comercial que "ya le llamé", la web de 2014, el post de Canva con el logo gigante…
- **20 situaciones distintas cada día** y distintas de las publicadas: revisa `toolkit/reels-publicados.md` (filas "meme") y no repitas POV ni chiste.
- **Varía las pantallas**: WhatsApp, Administrador de anuncios, bandeja de correo, CRM, calendario, notificaciones del móvil, extracto bancario, reseñas de Google, Excel, Canva, llamada perdida, formulario, Stripe/pagos… Máximo 4 del mismo tipo de pantalla al día. Puedes heredar de una clase existente y cambiar textos/números, pero **cambia también los nombres y datos que dibuja** (no dejes "Laura (formulario)" en un meme de otra cosa).
- POV de 1–2 líneas (≤ 95 caracteres), en español de España, que se entienda en 1 segundo. El remate tiene que dar risa o "me ha pasado".
- Marca: todo como Ceos Growth / @ceos.growth. **Nunca nombres personales del equipo.** Nombres de clientes ficticios y genéricos. Nunca marcas reales de terceros en tono negativo. Nunca estadísticas presentadas como reales.

## Pasos
1. Dependencias: `pip install --break-system-packages -q numpy pillow` y ffmpeg (si faltan).
2. Carpeta del día: `reels/memes/AAAA-MM-DD/`. Si ya hay 20 filas meme con la fecha de hoy en `reels-publicados.md`, termina sin hacer nada. Si hay menos (una ejecución anterior se cortó), crea y publica solo los que falten.
3. Escribe `reels/memes/AAAA-MM-DD/memes_dia.py` con las 20 clases y al final `NEW = {'m01-<slug>': Clase, ... 'm20-<slug>': Clase}` (importa lo que necesites con `sys.path.insert(0, 'toolkit/reels')` y `from memes import *`).
4. Construye cada uno (en paralelo, 4 a la vez):
   `MEMES_FILE=reels/memes/AAAA-MM-DD/memes_dia.py python3 toolkit/reels/pov_reel.py reels/memes/AAAA-MM-DD/<nombre> <nombre>`
   Mira los 3 `_tmp/check*.jpg` de cada uno: nada cortado ni solapado, el texto se lee y el remate se entiende. Si alguno falla, corrígelo y reconstruye. Borra las carpetas `_tmp` antes del commit.
5. `git add reels/memes/AAAA-MM-DD` + commit (termina en "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>") + `git pull --rebase` + push a main. URLs fijadas al SHA: `https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/<SHA>/reels/memes/AAAA-MM-DD/<nombre>/reel.mp4` (comprueba que dan 200).
6. **Publicación en una sola tanda** — Zapier "Instagram for Business" → `_zap_raw_request`, cuenta @ceos.growth (id 17841469551116816):
   - Antes: GET `/17841469551116816/content_publishing_limit?fields=quota_usage,config`. Si no hay cupo para 20, publica los que quepan y dilo al final.
   - Crea los 20 contenedores: POST `/17841469551116816/media` con `media_type=REELS`, `share_to_feed=false`, `video_url=<url>`, `caption=<caption>`.
   - Espera a que todos den `status_code=FINISHED` (GET `/?ids=<ids>&fields=status_code`, cada ~30 s; si uno pasa de 4 min o da ERROR, recréalo).
   - Publica uno detrás de otro: POST `/17841469551116816/media_publish` con `creation_id`. **Una sola vez cada uno**; si falla, comprueba en `/17841469551116816/media?fields=caption,timestamp,permalink&limit=30` que no esté ya publicado antes de reintentar.
   - Caption: el POV como primera línea + 1 emoji, una frase corta que conecte con el problema ("Si te ha pasado, guárdalo 😅" / "Etiqueta a quien le pase"), y 5–6 hashtags en español con #ceosgrowth.
   - Facebook y LinkedIn: no.
7. **Verificación real**: GET `/17841469551116816/media?fields=permalink,caption,timestamp,media_type&limit=30` y cuenta cuántos de hoy están publicados. Solo cuentan los que aparecen ahí.
8. Añade una fila por meme a `toolkit/reels-publicados.md` (`| AAAA-MM-DD | meme | <POV corto> — solo pestaña Reels | <permalink> |`), commit y push.
9. Última línea: "Memes hoy: X/20 publicados" + motivo si faltan.
