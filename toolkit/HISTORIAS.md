# Historias diarias de Ceos Growth — instrucciones

Cada día a las 9:00 (Madrid) se publica UNA historia animada de valor (1080×1920, 5 s) en Instagram @ceos.growth.

## Contenido
- Un tip práctico de marketing distinto cada día (captación, Meta Ads, creatividades, guiones, CRM, seguimiento de leads, ventas por teléfono, embudos, remarketing, métricas, contenido orgánico, landing pages, formularios, WhatsApp, email…). Nunca repetir tema: ver `historias-publicadas.md`.
- Estructura: etiqueta "TIP DEL DÍA" + titular grande (una idea, con la palabra clave en naranja y `white-space: nowrap`) + una ANIMACIÓN VISUAL que explique el tip + una frase de cierre en Instagram Serif cursiva + "Síguenos para más tips / @CEOS.GROWTH" abajo.
- La animación visual debe ser rica y distinta cada día, estilo landing de Ceos: mockups de CRM en directo (notificaciones que entran, cronómetros, embudos con un punto que viaja, tarjetas de lead que cambian de fase), paneles de Meta Ads (barras que crecen, CPL que baja, contador), chat de WhatsApp que se escribe, checklist que se marca, comparativa antes/después, etc. Si el mockup muestra datos inventados, marca "EJEMPLO". Nunca presentes estadísticas inventadas como reales.
- Deja libres ~250 px arriba y ~290 px abajo (zona de la interfaz de Instagram).

## Estilo
Igual que `plantilla-historia/Historia.dc.html` (úsala como base y cambia contenido y animación): fondo #0A0908, naranja #FF6A1A, crema #F2EDE7, grises #B5ADA4/#9C938B, Bricolage Grotesque 800, Instrument Serif cursiva, Instrument Sans, JetBrains Mono, logo caballo con brillo arriba a la izquierda. Animaciones que funcionen en bucle de 5 s (CSS keyframes; contadores con @property).

## Pasos
1. Dependencias como en INSTRUCCIONES.md (npm fontsource + playwright + ffmpeg).
2. Crear `historias/AAAA-MM-DD/Historia.dc.html` y renderizar: `python3 toolkit/render_story.py historias/AAAA-MM-DD/Historia.dc.html historias/AAAA-MM-DD`. Revisar `historia.jpg` (nada cortado ni solapado; si hace falta, render con KEEP=1 y mirar varios fotogramas).
3. Commit + push a main. URL: `https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/main/historias/AAAA-MM-DD/historia.mp4`.
4. Instagram vía Zapier "Instagram for Business" `_zap_raw_request` (connection_id 66508048): POST `https://graph.facebook.com/v21.0/17841469551116816/media` con `media_type=STORIES`, `video_url=<url>`; esperar a `status_code=FINISHED` (GET `/<id>?fields=status_code`); POST `/17841469551116816/media_publish` con `creation_id=<id>`. Publicar UNA sola vez.
5. Cuando @hugo.ceos y @victor.ceos aparezcan en GET `https://graph.facebook.com/v21.0/me/accounts?fields=name,instagram_business_account{username}`, publica la misma historia también en esas cuentas con su id.
6. Añadir el tema a `historias-publicadas.md`, commit y push.
