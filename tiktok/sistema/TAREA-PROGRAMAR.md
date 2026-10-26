# Tarea programada: programar en Metricool los reels pendientes de TikTok

Crear en claude.ai → Tareas programadas (Routines) → Nueva, con el conector **Metricool** activado, repositorio `growthceos-hub/ceos-instagram`, cada día a las 07:41 (o una sola vez). Instrucciones (pegar tal cual):

---
Programa en Metricool los reels de TikTok pendientes. Sin preguntas, sin subagentes. Solo TikTok, nunca Instagram.
1. En la raíz del repo ceos-instagram: `FABRICA=tiktok/sistema REPO=. python3 tiktok/sistema/lote.py > /tmp/pendientes.txt`. El archivo alterna líneas "### <id> <fecha>" y una línea JSON.
2. Por cada bloque cuya fecha sea futura: llama a `createScheduledPost` con blogId "7288052", date = la fecha del encabezado e info = la línea JSON EXACTA. Si va bien (la media pasa a static.metricool.com), añade el id a `tiktok/sistema/programados.txt`. Si da error, reintenta una vez; si vuelve a fallar, apúntalo y sigue.
3. Al terminar: git add tiktok/sistema/programados.txt, commit "TikTok: programados N reels" (con "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"), git pull --rebase y push a main.
4. Termina con una línea: cuántos programados, rango de fechas y fallos.
---

## Además: LinkedIn (cuando LinkedIn esté conectado en Metricool)
Añadir a las instrucciones de la tarea:
5. `python3 linkedin/lote_linkedin.py 2026-10-27 > /tmp/linkedin.txt` (los 30 posts del pack-01, de lunes a viernes a las 13:00). Por cada bloque con fecha futura: `createScheduledPost` con blogId "7288052", date del encabezado e info = la línea JSON exacta. Si va bien, añade el id (nombre de carpeta) a `linkedin/programados.txt`. Los carruseles salen como documento PDF (publishImagesAsPDF) a partir de las páginas PNG; las encuestas, como encuesta nativa de 7 días.
