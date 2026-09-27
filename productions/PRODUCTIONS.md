# Publicación diaria de Ceos Productions (@ceos.productions) — instrucciones

Ceos Productions es el **estudio de producción audiovisual** (empresa distinta de Ceos Growth). Cada día se publica en Instagram:
- **13:00 → 1 carrusel** animado de 5 slides (normal, en la cuadrícula).
- **19:00 → 1 reel** de valor animado (~28 s), **solo en la pestaña Reels** (`share_to_feed=false`, misma regla que en Ceos Growth).

Se usa el mismo motor y el mismo nivel visual que Ceos Growth, cambiando la marca con la variable de entorno **`BRAND=productions`** (pone "Ceos Productions", "@ceos.productions" y el logo de `toolkit/brands/productions/logo.png` si existe; si no, el caballo naranja).

## Paso 0 — comprobar que la cuenta está conectada (siempre primero)
Zapier "Instagram for Business" → `_zap_raw_request` GET `https://graph.facebook.com/v21.0/me/accounts` con `fields=name,id,instagram_business_account{id,username}` y `limit=100`.
- Busca la cuenta con `username` = `ceos.productions`. Su `instagram_business_account.id` es el **IG_ID** para todos los pasos.
- **Si no aparece: no construyas nada.** Termina con la línea: "⚠️ @ceos.productions todavía no está conectada: vincúlala a una página de Facebook y vuelve a conectar Instagram for Business en Zapier dando permiso a esa página." (Una vez aparezca, apunta el IG_ID aquí abajo en "IDs".)

## IDs
- Instagram @ceos.productions: IG_ID = _pendiente (se rellena al conectarla)_
- Facebook: solo si en `me/accounts` hay una página llamada "Ceos Productions" con esa cuenta de Instagram. **Nunca** publicar en "Ceos Marketing", "Ceos Growth Hugo" ni ninguna otra página.

## Contenido
Tema: **producción audiovisual para negocios** — dar valor, no vender. Ideas: cómo grabar anuncios con el móvil, iluminación barata que funciona, sonido (micros, sala), encuadre y planos, guiones y ganchos de los 3 primeros segundos, cómo hablar a cámara, B-roll, edición y ritmo, subtítulos, formatos que funcionan en Reels/Meta Ads, cómo preparar un rodaje, errores típicos, qué grabar en un día de estudio, contenido de marca personal, antes/después de un plano…
- Tema nuevo cada vez: mira `productions/publicados.md` y no repitas (el carrusel y el reel del mismo día, de temas distintos).
- **Nunca inventes estadísticas, clientes, precios ni datos del estudio.** Solo consejos. Los mockups con datos llevan "EJEMPLO".
- Marca: todo como **Ceos Productions** y **@ceos.productions**. Nunca nombres personales del equipo. Nunca mencionar Ceos Growth.
- Caption: primera línea = pregunta-gancho + 1 emoji; 1 frase de contexto; los pasos con "→"; cierre "Guárdalo y síguenos para más tips 🎬"; 6–7 hashtags en español con #ceosproductions (p. ej. #produccionaudiovisual #videomarketing #grabacion #contenidoparaempresas #reels).

## Dependencias (si faltan)
`cd toolkit && npm i --silent && pip install --break-system-packages -q playwright scipy numpy && python3 -m playwright install chromium` (y ffmpeg).

## Carrusel (13:00)
1. Carpeta `productions/posts/AAAA-MM-DD/`. Si ya está en `productions/publicados.md` con fecha de hoy y tipo carrusel, termina sin hacer nada.
2. Copia `toolkit/plantilla-valor/` a `productions/posts/AAAA-MM-DD/src/` y reescribe los 5 `.dc.html` (mismo diseño, texto y animaciones nuevas del tema). Estructura: 01 gancho · 02 problema/idea · 03 idea · 04 solución · 05 CTA "Síguenos para más tips". Mismo estilo y reglas visuales que `toolkit/INSTRUCCIONES.md` (animación visual distinta en cada slide, nada estático).
3. `BRAND=productions python3 toolkit/render.py productions/posts/AAAA-MM-DD/src productions/posts/AAAA-MM-DD`. Revisa los JPG y la **portada** (primer fotograma de 01.mp4) como dice INSTRUCCIONES.md; crea `01-portada.mp4` si hace falta.
4. Commit + `git pull --rebase` + push a main. URLs: `https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/<SHA>/productions/posts/AAAA-MM-DD/NN.mp4` (comprueba que dan 200).
5. Instagram (Zapier "Instagram for Business" → `_zap_raw_request`):
   - Por vídeo: POST `https://graph.facebook.com/v21.0/<IG_ID>/media` con `media_type=VIDEO`, `is_carousel_item=true`, `video_url=<url>`.
   - GET `https://graph.facebook.com/v21.0/?ids=<ids>&fields=status_code` hasta FINISHED en todos (si uno se atasca >1 min, recréalo).
   - POST `/<IG_ID>/media` con `media_type=CAROUSEL`, `children=<ids en orden>`, `caption=<texto>`.
   - POST `/<IG_ID>/media_publish` con `creation_id`. **Una sola vez**; si falla, mira `GET /<IG_ID>/media?fields=caption,timestamp,permalink&limit=5` antes de reintentar.
6. Facebook solo si existe la página "Ceos Productions" (ver IDs).

## Reel (19:00)
1. Carpeta `productions/reels/AAAA-MM-DD/`. Si ya está publicado hoy en `productions/publicados.md`, termina.
2. `spec.json` con `topic`, 5 `scenes` (hook · 3 step · cta) y `caption`, igual que `toolkit/REELS.md` (mockups `checklist`, `compare`, `timeline`, `script`, `timer`, `bars`… variados; poco texto). Referencia: `reels/2026-09-26*/spec.json`.
3. `BRAND=productions python3 toolkit/reels/build_reel.py productions/reels/AAAA-MM-DD/spec.json productions/reels/AAAA-MM-DD <día del año>`. Revisa `_tmp/check1..5.jpg`.
4. Commit + pull --rebase + push; URL fijada al SHA con `reel.mp4` (200).
5. Instagram: POST `/<IG_ID>/media` con `media_type=REELS`, `share_to_feed=false`, `video_url`, `caption` → espera FINISHED (~30 s entre consultas; >4 min recrea) → `media_publish` **una sola vez**.

## Siempre al final
- **Verifica que se publicó de verdad**: GET `/<IG_ID>/media?fields=permalink,caption,timestamp,media_type&limit=3` y confirma que el post de hoy está ahí. Solo entonces cuenta como hecho.
- Añade fila a `productions/publicados.md` (fecha | carrusel/reel | tema | permalink), commit y push.
- Última línea: tipo + tema + permalink, o el motivo exacto si no se publicó.
