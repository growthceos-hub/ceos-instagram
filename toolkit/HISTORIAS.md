# Historias diarias de Ceos Growth — instrucciones

Cada día a las 9:00 (Madrid) se publica una SERIE DE 5 HISTORIAS animadas (1080×1920, 15 s cada una) en Instagram @ceos.growth, en orden, como un carrusel: la gente tiene que tocar para ver la siguiente.

## Contenido de la serie
- Un tema de marketing distinto cada día (captación, Meta Ads, creatividades, guiones, CRM, seguimiento de leads, ventas por teléfono, embudos, remarketing, métricas, contenido orgánico, landing pages, formularios, WhatsApp, email…). Nunca repetir: ver `historias-publicadas.md`.
- 01 = gancho muy potente que cree curiosidad ("4 pasos para…", "El error que…") y termine con una flecha "→".
- 02, 03, 04 = un paso/idea por historia ("PASO 1", "PASO 2"…), cada uno con su propia animación visual, y abajo "SIGUIENTE PASO →" (o "ÚLTIMO PASO →" en la 04).
- 05 = último paso + botón grande "Síguenos para más tips" + @CEOS.GROWTH.
- Pastilla "0X / 05" arriba a la derecha en todas.
- Cada historia tiene una ANIMACIÓN VISUAL que explica la idea, distinta cada vez, estilo landing de Ceos: mockups de CRM en directo (notificaciones, cronómetros, embudos con un punto que viaja, fases que se iluminan), paneles de Meta Ads (barras que crecen, contadores), chat de WhatsApp que se escribe, móviles con notificaciones, checklists que se marcan, antes/después… Todo con movimiento continuo durante los 15 s. Si un mockup muestra datos de ejemplo, marca "EJEMPLO". Nunca inventes estadísticas presentadas como reales.
- Poco texto y grande. Deja libres ~250 px arriba y ~290 px abajo.

## Estilo y archivos base
- Base de diseño: `historias/2026-09-26-serie/H1..H5.dc.html` (la serie de referencia). Copia su estructura y estilo y cambia contenido y animaciones.
- Colores y tipos: fondo #0A0908, naranja #FF6A1A, crema #F2EDE7, grises #B5ADA4/#9C938B; Bricolage Grotesque 800, Instrument Serif cursiva, Instrument Sans, JetBrains Mono; logo caballo con brillo.
- Escribe cada archivo SIN la capa de efectos y luego pásale `python3 toolkit/boost_story.py <archivos>`: añade partículas, anillo de luz giratorio, orbes, barrido de luz, titular palabra a palabra, entrada 3D + flotación de los mockups. Para que la entrada 3D funcione, el mockup principal debe llevar `animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both` y el contenedor del titular `gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both` (como en la serie de referencia).

## Pasos
1. Dependencias como en INSTRUCCIONES.md (npm fontsource + playwright + ffmpeg).
2. Crear `historias/AAAA-MM-DD/H1..H5.dc.html`, aplicar boost_story.py y renderizar cada una: `DUR=15 NAME=0N python3 toolkit/render_story.py historias/AAAA-MM-DD/HN.dc.html historias/AAAA-MM-DD` (se pueden lanzar las 5 en paralelo, cada una a su carpeta temporal). Revisar los JPG (y con KEEP=1 varios fotogramas): nada cortado ni solapado.
3. Commit + push a main. URLs: `https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/<SHA>/historias/AAAA-MM-DD/0N.mp4`. **Antes de crear los contenedores comprueba con curl que las 5 URLs dan 200.** Si la URL fijada al commit da 404 (pasa a veces justo después del push), usa la de `main` (`.../ceos-instagram/main/historias/...`): son archivos nuevos y no tienen caché. Nunca crees contenedores con una URL que no dé 200.
4. Instagram vía Zapier "Instagram for Business" `_zap_raw_request` (connection_id 66508048):
   - Crea los 5 contenedores: POST `https://graph.facebook.com/v21.0/17841469551116816/media` con `media_type=STORIES`, `video_url=<url>`.
   - Espera a que los 5 den `status_code=FINISHED` (GET `https://graph.facebook.com/v21.0/?ids=<ids>&fields=status_code`). Si uno se atasca más de 3 min, créalo de nuevo.
   - Publica EN ORDEN 01→05, uno detrás de otro: POST `/17841469551116816/media_publish` con `creation_id=<id>`. Cada historia UNA sola vez.
5. Cuando @hugo.ceos y @victor.ceos aparezcan en GET `https://graph.facebook.com/v21.0/me/accounts?fields=name,instagram_business_account{username}`, publica la misma serie también en esas cuentas.
6. Añadir el tema a `historias-publicadas.md`, commit y push.
