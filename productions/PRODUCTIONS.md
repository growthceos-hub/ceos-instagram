# Publicación diaria de Ceos Productions (@ceos.productions) — instrucciones

Ceos Productions es el **estudio de grabación y fotografía en Burgos** (empresa distinta de Ceos Growth). Público: **cualquiera que necesite grabarse o fotografiarse** — empresas, marcas personales, creadores, profesionales, emprendedores.

## Nivel exigido (decisión de Hugo, 27-09): SÚPER PROFESIONAL
Todo tiene que verse al nivel de las mejores cuentas del sector: animado, fluido, premium, con el mismo nivel visual que Ceos Growth pero con la marca de Ceos Productions (azul y blanco, su logo). Si al revisar los fotogramas algo parece amateur, estático, cortado, con poco contraste o con texto de relleno, **se corrige y se vuelve a renderizar antes de publicar**. Nunca se publica "lo que ha salido".

## Parrilla diaria (hora de Madrid, decisión de Hugo 28-09) — cada ejecución programada hace UNA pieza
Total al día: **5 carruseles + 5 historias de valor + 5 reels TIP (valor) + 5 reels MEME** = 20 publicaciones (el límite de la API de Instagram es 50 cada 24 h).

| Hora | Pieza | Dónde |
|---|---|---|
| 09:00 · 11:00 · 13:00 · 17:00 · 20:00 | **5 carruseles** animados de 5 slides (huecos C1–C5) | Cuadrícula |
| ~10:30 | **5 historias** de valor (una serie) | Historias |
| 12:30 · 13:30 · 14:30 · 15:30 · 16:30 · 17:30 · 18:30 · 19:30 · 20:30 · 21:30 | **10 reels** (huecos 1–10): **5 TIP + 5 MEME** alternados | Solo pestaña Reels (`share_to_feed=false`) |

**Evitar temas repetidos entre piezas del mismo día (se ejecutan en paralelo):** nada más elegir el tema, haz `git pull --rebase`, comprueba en `productions/publicados.md` que nadie lo ha cogido hoy y añade una fila de reserva `| fecha | <pieza> | tema | en curso |`; commit + push. Al terminar, sustituye `en curso` por el permalink (o por `NO PUBLICADO: motivo`). Las filas `en curso` de otra pieza cuentan como tema ocupado. Si `git pull --rebase` da conflicto en `publicados.md`, conserva las filas de los dos lados.

Todo se hace con el mismo motor que Ceos Growth y la marca Productions: **`BRAND=productions`** (render.py, render_story.py, build_reel.py y pov_reel.py cambian nombre, @, logo `toolkit/brands/productions/logo.png` y paleta azul/blanco). Nunca pongas naranja a mano.

## Paso 0 — comprobar que la cuenta está conectada (siempre primero)
Zapier "Instagram for Business" → `_zap_raw_request` GET `https://graph.facebook.com/v21.0/me/accounts` con `fields=name,id,instagram_business_account{id,username}` y `limit=100`.
- Busca la cuenta con `username` = `ceos.productions`. Su `instagram_business_account.id` es el **IG_ID** para todos los pasos.
- **Si no aparece: no construyas nada.** Termina con la línea: "⚠️ @ceos.productions todavía no está conectada: vincúlala a una página de Facebook y vuelve a conectar Instagram for Business en Zapier dando permiso a esa página." (Una vez aparezca, apunta el IG_ID aquí abajo en "IDs".)

## IDs
- Instagram @ceos.productions: **IG_ID = 17841447505872534** (conectada el 27-09-2026 vía Zapier "Instagram for Business"). Aun así haz el Paso 0 cada vez.
- Facebook: página **Ceos Productions, id 1276641715541348**. Publica ahí el vídeo (carrusel → video-completo.mp4; reel → reel.mp4) vía Zapier "Facebook Pages" → `page_video` con `page=1276641715541348`, solo si esa página aparece en el desplegable `page` de la acción; si no aparece, sáltalo sin error. **Nunca** publicar en "Ceos Marketing", "Ceos Growth Hugo" ni ninguna otra página.

## Contenido
El tema de la cuenta es **nuestro estudio de grabación en Burgos**.

### Plan del carrusel (día de la semana en Madrid)
- Los 5 carruseles del día son de **TIPS/valor**, salvo **martes y viernes el carrusel C3 (13:00), que es de CAPTACIÓN**. Los 5 del día con temas y formatos distintos entre sí (no 5 variaciones del mismo tema).
- **Carrusel de CAPTACIÓN**: presenta el estudio de grabación en Burgos para atraer clientes (empresas, marcas personales, creadores que necesitan grabar vídeo). Qué pueden grabar (anuncios, reels, vídeos de marca, entrevistas, podcasts…), por qué grabar en un estudio en vez de con el móvil en la oficina, cómo es una sesión, qué se llevan. Slide 5 = CTA **"Escríbenos ESTUDIO por DM y reserva tu sesión en Burgos"**; en el caption, lo mismo. Varía el ángulo cada vez (tipo de cliente, tipo de vídeo, dolor distinto).
- **Carrusel de TIPS** para ganar seguidores: consejos de grabación y vídeo (cómo hablar a cámara, luz, sonido, encuadre, ganchos de los 3 primeros segundos, guiones, B-roll, edición, subtítulos, formatos para Reels/Meta Ads, cómo preparar una sesión de grabación…). Sin vender. Slide 5 = CTA **"Síguenos para más tips"**.
- **Reels y historias**: de VALOR para ganar seguidores (ver sus secciones). Solo los martes y viernes la última historia invita a reservar sesión.

### Reglas
- Tema nuevo cada vez: mira `productions/publicados.md` y no repitas (el carrusel y el reel del mismo día, de temas distintos).
- **Nunca inventes datos del estudio**: ni precios, ni equipos concretos, ni metros, ni clientes, ni estadísticas. Lo único cierto: es un estudio de grabación propio en Burgos. Los mockups con datos llevan "EJEMPLO".
- Marca: todo como **Ceos Productions** y **@ceos.productions**. Nunca nombres personales del equipo. Nunca mencionar Ceos Growth.
- **Colores: azul y blanco** (lo aplica `BRAND=productions` automáticamente; no pongas naranja a mano). Logo en `toolkit/brands/productions/logo.png`.
- Caption: primera línea = pregunta-gancho + 1 emoji; 1 frase de contexto; los pasos con "→"; cierre: en tips "Guárdalo y síguenos para más tips 🎬", en captación "Escríbenos ESTUDIO por DM 📩"; 6–7 hashtags en español con #ceosproductions y, en captación, #burgos #estudiodegrabacion.

## Dependencias (si faltan)
`cd toolkit && npm i --silent && pip install --break-system-packages -q playwright scipy numpy && python3 -m playwright install chromium` (y ffmpeg).

## Carruseles (5 al día, huecos C1–C5 → 09:00, 11:00, 13:00, 17:00, 20:00)
**Animado como los de Ceos Growth** (INSTRUCCIONES.md, "Estilo landing de Ceos"): cada slide con su propia animación visual continua (mockups de cámara/visor con encuadre que se ajusta, esquema de luces que se encienden, onda de audio que se limpia, timeline de edición, guion que se escribe, móvil con reel en reproducción, checklist que se marca, antes/después móvil vs estudio…). Slide 01 = gancho brutal y la portada tiene que enganchar en la cuadrícula.
1. Carpeta `productions/posts/AAAA-MM-DD-CN/` (N = hueco 1–5). Si en `productions/publicados.md` ya hay una fila de hoy `carrusel CN` con permalink, termina sin hacer nada.
2. Copia `toolkit/plantilla-valor/` a `productions/posts/AAAA-MM-DD-CN/src/` y reescribe los 5 `.dc.html` (mismo diseño, texto y animaciones nuevas del tema). Estructura: 01 gancho · 02 problema/idea · 03 idea · 04 solución · 05 CTA (el que toque según el plan semanal: captación o tips). Mismo estilo y reglas visuales que `toolkit/INSTRUCCIONES.md` (animación visual distinta en cada slide, nada estático).
3. `BRAND=productions python3 toolkit/render.py productions/posts/AAAA-MM-DD-CN/src productions/posts/AAAA-MM-DD-CN`. Revisa los JPG y la **portada** (primer fotograma de 01.mp4) como dice INSTRUCCIONES.md; crea `01-portada.mp4` si hace falta.
4. Commit + `git pull --rebase` + push a main. URLs: `https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/<SHA>/productions/posts/AAAA-MM-DD-CN/NN.mp4` (comprueba que dan 200).
5. Instagram (Zapier "Instagram for Business" → `_zap_raw_request`):
   - Por vídeo: POST `https://graph.facebook.com/v21.0/<IG_ID>/media` con `media_type=VIDEO`, `is_carousel_item=true`, `video_url=<url>`.
   - GET `https://graph.facebook.com/v21.0/?ids=<ids>&fields=status_code` hasta FINISHED en todos (si uno se atasca >1 min, recréalo).
   - POST `/<IG_ID>/media` con `media_type=CAROUSEL`, `children=<ids en orden>`, `caption=<texto>`.
   - POST `/<IG_ID>/media_publish` con `creation_id`. **Una sola vez**; si falla, mira `GET /<IG_ID>/media?fields=caption,timestamp,permalink&limit=5` antes de reintentar.
6. Facebook solo si existe la página "Ceos Productions" (ver IDs).

## Reels (10 al día, huecos 1–10 → 12:30, 13:30 … 21:30)
Cada ejecución hace y publica **UN** reel: el de su hueco N. Carpeta `productions/reels/AAAA-MM-DD-N/`. Si en `productions/publicados.md` ya hay una fila de hoy `reel N` con permalink, termina sin hacer nada.

**Tipo según el día** (día del año en Madrid): día PAR → huecos impares (1, 3, 5, 7, 9) = MEME y pares (2, 4, 6, 8, 10) = TIP. Día IMPAR → al revés. Siempre 5 TIP + 5 MEME, alternados, y cada día cambia cuál abre.

**Reglas de retención (obligatorias en los dos tipos):**
- **Gancho en el primer segundo**: el texto del gancho se ve completo desde el fotograma 0 (nada de pantalla vacía o fundido de entrada), máx. ~8 palabras, que genere curiosidad, "me ha pasado" o polémica suave ("Deja de grabarte con la luz del techo", "POV: el cliente trae su guion en 14 folios").
- Movimiento constante: cambio visual cada 1–2 s, nada estático más de 2 s. Poco texto, grande, legible en móvil.
- Caption: primera línea = el gancho + 1 emoji; 1 frase; en TIP los pasos con "→"; cierre "Guárdalo y síguenos para más 🎬" (TIP) o "Etiqueta a quien le pase 😅" (MEME); 5–7 hashtags en español con #ceosproductions.

**MEME (formato POV, estilo cuentas de memes de nicho):**
- Motor `toolkit/reels/pov_reel.py` + `toolkit/reels/memes.py` con **`BRAND=productions`** (cabecera Ceos Productions / @ceos.productions). Lee `toolkit/MEMES.md` para el formato de las clases (`POV`, `DUR` 6,5–8 s, `PUNCH`, `FOCUS`, `SFX`, `draw(t)`), pero el contenido es del mundo de **grabarse y fotografiarse**: el cliente que llega sin guion, "solo son 5 minutos de grabación", repetir la toma 47 veces, el móvil con 1 % de batería, el micro sin encender, la ring light del cuñado, "¿me puedes quitar 10 kilos en edición?", el reel con 12 visitas, la foto de perfil de 2012, el primer "hola a todos" a cámara, las notas del móvil como teleprompter…
- Escribe `productions/reels/AAAA-MM-DD-N/meme.py` con UNA clase y `NEW = {'p-<slug>': Clase}`; construye con `BRAND=productions MEMES_FILE=... python3 toolkit/reels/pov_reel.py productions/reels/AAAA-MM-DD-N p-<slug>`. Pantallas variadas (visor de cámara, WhatsApp, calendario, notificaciones, galería, estadísticas de Instagram, teleprompter…), azules/blancos, remate que dé risa. Nunca repitas un POV ya publicado (mira `publicados.md`).

**TIP (reel de valor animado):**
- `spec.json` como `toolkit/REELS.md` (hook · 3 step · cta; mockups `checklist`, `compare`, `timeline`, `script`, `timer`, `bars`, `chat`… variados entre escenas y entre reels). Temas: hablar a cámara, luz, sonido, encuadre, ganchos, guiones, B-roll, edición, subtítulos, fotos de perfil/marca personal, cómo prepararse para una sesión, qué ropa llevar, formatos para Reels/anuncios… El hook con `size` 130–140, 2 líneas cortas.
- `BRAND=productions python3 toolkit/reels/build_reel.py productions/reels/AAAA-MM-DD-N/spec.json productions/reels/AAAA-MM-DD-N <N + día del año>`.

**Revisión antes de publicar**: mira los `_tmp/check*.jpg` y extrae el fotograma 0 (`ffmpeg -i reel.mp4 -frames:v 1 f0.jpg`): el gancho se lee entero. Si no, corrige y reconstruye. Borra `_tmp` antes del commit.

**Publicar**: commit + `git pull --rebase` + push; URL fijada al SHA con `reel.mp4` (200; si da 404 usa la de `main`). POST `/<IG_ID>/media` con `media_type=REELS`, `share_to_feed=false`, `video_url`, `caption` → espera FINISHED (~30 s entre consultas; >4 min o ERROR, recrea) → `media_publish` **una sola vez** (si falla, mira `/media` antes de reintentar). Facebook: solo si existe la página Ceos Productions (ver IDs), con `reel.mp4`.

## Historias (5 al día, ~10:30)
**Siempre 5** historias de valor (T = 5).
- Carpeta `productions/historias/AAAA-MM-DD/`. Antes: GET `/<IG_ID>/stories?fields=id,timestamp`; si ya hay historias de hoy (Madrid) no publiques más.
- Serie animada 1080×1920, 15 s cada una, en orden (se tocan como un carrusel), **mismo nivel y motor que las de Ceos Growth** (`toolkit/HISTORIAS.md`: referencia de diseño `historias/2026-09-26-serie/`, `toolkit/boost_story.py` para la capa de efectos) renderizadas con **`BRAND=productions DUR=15 NAME=0N python3 toolkit/render_story.py ...`**. Pastilla "0X / 0T" (T = total de hoy).
- **Alto valor**: un tema útil distinto cada día y distinto del carrusel y los reels de hoy. Rota el FORMATO de la serie: tips en pasos · mito vs realidad · error común + cómo arreglarlo · antes/después (móvil vs estudio) · checklist antes de grabar/fotografiarse · mini-guion listo para copiar · "haz esto hoy". Estructura: 01 = gancho muy potente con "→"; las del medio = una idea por historia con su animación; la última = remate + CTA. CTA: martes y viernes "Escríbenos ESTUDIO por DM y reserva tu sesión en Burgos"; resto "Síguenos para más tips". (La API no permite encuestas ni stickers: todo va en el vídeo.)
- Revisa los JPG (nada cortado, texto grande, zona libre ~250 px arriba y ~290 px abajo). Commit + push; URLs con 200.
- Publica EN ORDEN con `media_type=STORIES`, `video_url`; espera FINISHED en todas antes de publicar; cada una **una sola vez**.
- **Verifica** en GET `/<IG_ID>/stories` que hay exactamente las de hoy. Fila en `publicados.md`: `| fecha | historias ×T | tema | — |`.

## Siempre al final
- **Verifica que se publicó de verdad**: GET `/<IG_ID>/media?fields=permalink,caption,timestamp,media_type&limit=3` y confirma que el post de hoy está ahí. Solo entonces cuenta como hecho.
- En `productions/publicados.md` sustituye `en curso` de tu fila de reserva por el permalink (formato: fecha | carrusel CN / reel N (meme o tip) / historias ×5 | tema | permalink), commit + `git pull --rebase` + push.
- Si al final NO se publicó, envía un correo a growthceos@gmail.com con asunto "⚠️ Ceos Productions: <pieza> no publicada · <fecha>" con el paso y el error exacto.
- Última línea: tipo + tema + permalink, o el motivo exacto si no se publicó.
