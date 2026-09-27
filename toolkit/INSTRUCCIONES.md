# Publicación diaria de Ceos Growth — instrucciones

Cada día a las 12:00 (Madrid) se crea y publica un carrusel animado de 5 slides.

## Plan semanal
- **Lunes a sábado → carrusel de VALOR** (plantilla `plantilla-valor/`). Enseña algo útil de captación, ventas, Meta Ads, CRM, seguimiento de leads, guiones o grabación. Sin vender. Slide 5 = CTA **"Síguenos para más tips"**.
- **Domingo → carrusel de MÉTODO** (plantilla `plantilla-metodo/`). Cuenta cómo trabaja Ceos Growth (sistema de 26 días, comisión sobre ventas, 10 perfiles, CRM, estudio propio). Slide 5 = "Comenta [PALABRA] y reserva tu llamada gratis".
- Estructura siempre: 01 gancho (el más llamativo, con movimiento) · 02 problema/idea · 03 contexto/idea · 04 solución/idea · 05 CTA.
- Temas ya publicados: ver `publicados.md`. No repetir tema.

## Estilo (no cambiar)
Fondo #0A0908, naranja #FF6A1A, crema #F2EDE7, grises #B5ADA4/#9C938B. Tipos: Bricolage Grotesque 800 (titulares), Instrument Serif cursiva (acentos), Instrument Sans (texto), JetBrains Mono (etiquetas). Logo caballo naranja con brillo arriba a la izquierda, "0X / 05" arriba a la derecha, barra de progreso de 5 abajo. Poco texto, una idea por slide. Animaciones suaves de 4 s: brillos lentos, números que cuentan desde cerca del valor final, reflejos.

**Estilo landing de Ceos (obligatorio, nivel top):** cada slide lleva una ANIMACIÓN VISUAL que explica la idea, distinta en cada slide y en cada carrusel, como en la landing y en las historias (`HISTORIAS.md`): mockups de CRM en directo (notificaciones que entran, cronómetros, embudos con un punto que viaja, fases que se iluminan), paneles de Meta Ads (barras que crecen, contadores), chat de WhatsApp que se escribe, móviles con notificaciones, checklists que se marcan, antes/después… Movimiento continuo y fluido durante los 4 s, que se vea premium, nunca una slide estática con solo texto. Si un mockup muestra datos de ejemplo, marca "EJEMPLO". Antes de publicar revisa que se vea al nivel de la landing; si no, mejóralo. Nunca inventar cifras: solo datos reales de Ceos Growth o consejos sin estadísticas.

Datos reales usables: +17 clientes activos, muchos más de 2 años con ellos; 10 perfiles; implantación en 26 días; 15–20 anuncios grabados en estudio propio; comisión sobre ventas; 12 meses de Meta Ads sin permanencia; coste de montarlo por tu cuenta 32.900 €/año.

## Pasos de cada ejecución
1. `cd toolkit && npm i --silent @fontsource/bricolage-grotesque @fontsource/instrument-sans @fontsource/instrument-serif @fontsource/jetbrains-mono && pip install --break-system-packages -q playwright && python3 -m playwright install chromium` (si falta).
2. Copiar la plantilla que toque a `posts/AAAA-MM-DD/src/` y reescribir el contenido de los 5 `.dc.html` (mismo diseño, texto e ilustraciones nuevas).
3. `python3 toolkit/render.py posts/AAAA-MM-DD/src posts/AAAA-MM-DD` → genera 01..05.mp4, 01..05.jpg y video-completo.mp4. Revisar los JPG antes de publicar.
   - **PORTADA (obligatorio):** Instagram usa el PRIMER fotograma del vídeo 01 como portada en la cuadrícula. Si la slide 01 arranca vacía (entrada animada), la portada sale en negro. Antes de publicar, extrae el primer fotograma (`ffmpeg -i 01.mp4 -frames:v 1 check.jpg`) y míralo: tiene que verse el titular completo. Si no, crea `01-portada.mp4` empezando en el momento en que ya se ve el titular y congelando el final para mantener 4 s: `ffmpeg -ss 1.0 -i 01.mp4 -vf "tpad=stop_mode=clone:stop_duration=1" -c:v libx264 -pix_fmt yuv420p -r 30 -movflags +faststart -an 01-portada.mp4`, y publica ese en lugar de 01.mp4.
4. `git add`, commit y `git push` a main. URLs públicas: `https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/main/posts/AAAA-MM-DD/NN.mp4`.
5. **Instagram (@ceos.growth, id 17841469551116816)** vía Zapier "Instagram for Business" → acción `_zap_raw_request` (connection_id 66508048):
   - Por cada vídeo: POST `https://graph.facebook.com/v21.0/17841469551116816/media` con querystring `media_type=VIDEO`, `is_carousel_item=true`, `video_url=<url>`.
   - Esperar hasta que GET `https://graph.facebook.com/v21.0/?ids=<ids>&fields=status_code` dé FINISHED en todos. Si uno se atasca más de 1 minuto, volver a crearlo.
   - POST `/17841469551116816/media` con `media_type=CAROUSEL`, `children=<ids en orden, separados por comas>`, `caption=<texto>`.
   - POST `/17841469551116816/media_publish` con `creation_id=<id del carrusel>`.
6. **Facebook (página Ceos Marketing, id 434829573050729)** vía Zapier "Facebook Pages" → `page_video` (connection_id 66508057) con `source=<url video-completo.mp4>`, `title` y `description` = el texto del post (sin hashtags).
7. **LinkedIn**: pendiente de que haya página de empresa con administrador. Cuando exista: Zapier "LinkedIn" → `create_company_update` con la imagen 01.jpg y el texto en tono profesional.
8. Añadir el tema a `publicados.md` y hacer push.

## Texto del post (descripción) — obligatorio en todas las redes
Siempre se publica con descripción: `caption` en Instagram, `description` en Facebook y texto en LinkedIn. Nunca publicar sin ella.
Primera línea = gancho (lo que se ve antes de "más"). Luego el contenido en líneas cortas con →. Cierre con el CTA de la slide 5. 6–8 hashtags en español (#marketingdigital #metaads #ventas #emprendedores #empresarios #captaciondeclientes #negociosespaña …).
