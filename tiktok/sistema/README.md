# Sistema TikTok de Ceos · guion → reel → Metricool

Cadena para producir y programar reels de TikTok en volumen (cuenta @ceos.growth, marca Metricool `7288052`). Instagram NO: allí publica otra automatización.

## Piezas
| Archivo | Qué hace |
|---|---|
| `specs/<oferta>-NN.json` (en la carpeta de trabajo) | Guion del reel en el formato de `toolkit/REELS.md` + campo `tiktok: {title, text}` (título SEO ≤ 90 car. y caption). |
| `cola.sh` | Renderiza las specs una a una con `toolkit/reels/build_reel.py`, en el orden de `orden.txt` (fecha de publicación), y comprime para TikTok (crf 24). Sale tras ~110 min o cuando no queda nada. |
| `subir.sh` | Copia cada reel renderizado a `tiktok/<id>/` de este repo y hace push (URL pública raw para Metricool). |
| `lote.py` | Lista los reels subidos y aún no programados, con su fecha según el calendario y el JSON listo para `createScheduledPost`. |
| `programados.txt` | Ids ya programados (para no duplicar). |

## Calendario (7 al día, desde el 26/10/2026)
09:00 agencia (valor) · 11:00 webs · 13:30 ads · 15:00 agencia · 17:30 webs · 19:30 reels · 21:30 método. El número del id marca el día (`lote.py`, `SLOT`). Para otra oferta, añade su fila a `SLOT`.

## Programar en Metricool
`createScheduledPost` con `blogId "7288052"`, `date` = la del lote y `info` = la línea JSON tal cual: `providers [{"network":"tiktok"}]`, media = URL raw fijada al commit, `tiktokData {privacyOption PUBLIC_TO_EVERYONE, commercialContentOwnBrand true, title, isAigc true}`. Metricool copia el vídeo a su servidor (`static.metricool.com`). Si da 502 al normalizar, reintenta una vez. Después apunta el id en `programados.txt`.

## Reglas de contenido
Solo datos reales de cada oferta (Web al Vuelo 79 € pago único, 2 días, se rehace gratis · Reels al Vuelo 1,99 € el primero, 10 por 59 €, 24 h · Ads al Vuelo desde 49 € por 12 versiones · agencia: datos de `toolkit/INSTRUCCIONES.md`). Nada de casos, testimonios ni cifras inventadas. Sin emojis dentro del vídeo. Pasada final con `.claude/skills/texto-sin-tono-ia`.

## Avisos
- En la nube, el contenedor se suspende si la sesión se queda quieta: lanza `cola.sh` como tarea en segundo plano de Claude (no con nohup) y vuelve a lanzarla al terminar.
- Un render tarda ~2,5 min y usa toda la CPU: un solo render a la vez.
- `tiktok/_pc/` = specs repartidas para renderizar en el PC.
