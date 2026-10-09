# Fuentes reales de lo que recomienda @revolutia.ai (lote C)

Investigación del 2026-10-09. Cada repo se comprobó con `git ls-remote` y se clonó en superficial y sin checkout (`--filter=blob:none --no-checkout`) en `scratchpad/repos/`. Se leyeron el README, el árbol de archivos, los manifiestos de plugin y los hooks. **No se ejecutó nada de ningún repo.** Las estrellas no se han podido comprobar, porque la API de GitHub está bloqueada en esta sesión. Las cifras de estrellas que aparecen abajo salen del reel o de webs de terceros y están **sin verificar**.

Contexto para valorar la relevancia: agencia de captación con Meta Ads que hace reels, carruseles, historias y anuncios en vídeo con Claude, y que graba en estudio propio.

Leyenda de riesgos:
- **Hook**: un hook de Claude Code ejecuta código de forma automática en cada acción.
- **Red**: el elemento llama a servicios externos.
- **Telemetría**: el elemento envía datos de uso.

---

## 1. Hyperframes (HeyGen)
- **URL verificada:** https://github.com/heygen-com/hyperframes. El reel dice "Hyperframe(s)"; es casi seguro este repo.
- **Qué es:** framework open source que convierte HTML, CSS y GSAP en MP4 deterministas. Tiene CLI, una app de escritorio y Studio, y es a la vez un **plugin de Claude Code** con unas 22 skills. Entre ellas: `embedded-captions`, `talking-head-recut`, `motion-graphics`, `music-to-video`, `product-launch-video`, `faceless-explainer`, `media-use` (música de fondo, efectos de sonido, logos) y `hyperframes-registry`. Incluye un catálogo de bloques y plantillas de motion (`registry/blocks`, hyperframes.heygen.com/catalog) y plantillas de diseño. Encaja con lo que dice el reel: cortes, subtítulos, motion, efectos de sonido y biblioteca de plantillas.
- **Instalación (README):** `claude plugin marketplace add heygen-com/hyperframes` y luego `claude plugin install hyperframes@hyperframes`. Alternativa: `npx skills add heygen-com/hyperframes`. Requiere Node 22 o superior.
- **Licencia:** Apache-2.0.
- **Último commit:** 2026-10-09. Muy activo.
- **Riesgos:**
  - El plugin de Claude **no trae hooks** (solo hay `.codex/hooks.json`, que es para Codex).
  - La CLI tiene **telemetría anónima activada**. Se desactiva con `hyperframes telemetry disable` o con `HYPERFRAMES_NO_TELEMETRY=1` / `DO_NOT_TRACK=1`.
  - `media-use` consulta el catálogo de HeyGen, así que hay red.
  - Las skills piden ejecutar `npx hyperframes skills update`, que descarga código nuevo.
- **Relevancia: ALTA.** Sirve para montar reels y anuncios 9:16 con subtítulos y motion sobre lo que se graba en estudio (`talking-head-recut`, `embedded-captions`). Es lo más cercano al flujo de edición de la agencia.

## 2. Remotion skills
- **URL verificada:** https://github.com/remotion-dev/skills. Son las skills oficiales; el motor está en remotion-dev/remotion.
- **Qué es:** carpeta de 12 skills (SKILL.md), entre ellas `/remotion-best-practices`, `/remotion-create` y `/remotion-markup`. No es un plugin y no tiene hooks.
- **Instalación:** `npx skills add remotion-dev/skills`. También se ofrecen al crear un proyecto con `bun create video`.
- **Licencia:** el repo de skills no tiene archivo LICENSE. **Remotion usa una licencia propia: es gratis para particulares y empresas de hasta 3 personas, y a partir de ahí hace falta licencia de empresa.** Hay que revisarlo antes de usarlo en la agencia.
- **Último commit:** 2026-10-07.
- **Riesgos:** las skills son solo texto. Remotion necesita Node y Chromium para renderizar.
- **Relevancia: ALTA o MEDIA.** Es potente para plantillas de anuncio repetibles en código, pero se solapa con Hyperframes y la licencia puede costar dinero.

## 3. Skill que convierte una web en un vídeo de lanzamiento (música y subtítulos)
- **No estoy seguro de cuál enseña el reel.** Hay varios candidatos verificados:
  - **heygen-com/hyperframes → skill `product-launch-video`.** Toma una URL de producto y genera un MP4 con narración y música de fondo. Es el candidato más probable si el reel venía del ecosistema de Hyperframes. Apache-2.0, 2026-10-09.
  - **https://github.com/anudeepadi/launch-video-skills.** Es el que mejor encaja con "música y subtítulos": genera escenas HTML que se graban con Playwright y se montan con ffmpeg, con voz local (Kokoro TTS), sincronización palabra a palabra para los subtítulos (faster-whisper), y música y efectos generados con ffmpeg. Se instala con `npx launch-video-skills install` y `setup`, que copia la skill a **todos** los agentes que encuentre en tu carpeta personal. Para limitarlo hay que usar `--agents claude`. MIT, 2026-09-24.
  - **https://github.com/Anann99/launch-film-skill.** "Launch film" hecho con Remotion y banda sonora original. Es un plugin de Claude Code sin hooks. MIT, 2026-10-03.
  - **https://github.com/StanCosmin28/product-film-skill.** Película de 13 segundos hecha con Remotion a partir de la interfaz real, con música real y salida en 9:16 y 16:9. Necesita ffmpeg y Python con numpy. MIT, 2026-10-02.
  - **https://github.com/ouerf-man/product-launch-motion-skill.** Usa Hyperframes y GSAP, ofrece 12 tipos de vídeo y voz opcional con ElevenLabs (red y API de pago). MIT, 2026-10-02.
  - También existe "Brag" (greta.sh), que lee el código y la web y genera un vídeo con música y subtítulos usando Hyperframes. No he localizado su repo.
- **Riesgos:** ninguno trae hooks. Todos instalan dependencias (Chromium, ffmpeg, Python) y algunos descargan modelos.
- **Relevancia: MEDIA.** Sirve para vídeos de demo o de lanzamiento de una landing o de un cliente, no para anuncios con actriz.

## 4. MCP oficial de DaVinci Resolve
- **Oficial: no hay repo.** Blackmagic integró un **servidor MCP nativo dentro de DaVinci Resolve Studio 21.1** (publicado el 8 de septiembre de 2026, según CineD, Y.M.Cinema y pttl.gr). Se configura desde *File > Setup AI Assistants* y admite Claude, Claude Code y Codex. **Solo funciona en Studio (la versión de pago).** Además, en la 21.1 el scripting en Python pasó a ser exclusivo de Studio. Esto no lo he verificado en la web de Blackmagic, solo en prensa secundaria.
- **Alternativa comunitaria (no oficial):** https://github.com/samuelgursky/davinci-resolve-mcp. Es un servidor MCP en Python que usa la API oficial de scripting. Tiene un modo puente para la versión gratuita y un panel de control local.
  - Instalación: `npx davinci-resolve-mcp setup`, o clonar el repo y ejecutar `python install.py`.
  - Licencia MIT. Último commit 2026-10-09.
  - Riesgos: el instalador escribe la configuración de varios clientes y comprueba actualizaciones en GitHub (red). El repo incluye hooks en `.agents/hooks/`, que son para quien desarrolla el propio repo, no se instalan con el MCP. El modo puente instala un script dentro de Resolve.
- **Relevancia: MEDIA.** Solo si la agencia edita en DaVinci Studio. Si edita con Claude y código, aporta poco.

## 5. SupoClip
- **URL verificada:** https://github.com/FujiwaraChoki/supoclip.
- **Qué es:** app web open source alternativa a OpusClip. Corta vídeos largos en clips 9:16, puntúa cada clip según 4 criterios (gancho, engagement, valor y compartibilidad, que serían las "4 preguntas" del reel) y genera **subtítulos sincronizados palabra a palabra** con AssemblyAI. También trae un **MCP** (carpeta `mcp/`), API REST, versión alojada en supoclip.com y app de iOS.
- **Instalación:** con Docker Compose (`docker-compose up -d`). Necesita una clave de AssemblyAI y un proveedor de LLM (Google, OpenAI, Anthropic u Ollama). Hay un modo totalmente local con Whisper y Ollama.
- **Licencia:** **AGPL-3.0.** Usarlo internamente no supone problema; si se modifica y se ofrece como servicio, hay que publicar el código.
- **Último commit:** 2026-10-06.
- **Riesgos:** los vídeos se suben a AssemblyAI salvo en modo local, y el servicio alojado es de terceros. No tiene hooks. La telemetría no se pudo comprobar en el código.
- **Relevancia: MEDIA-ALTA.** Sirve para sacar shorts o reels de grabaciones largas del estudio (podcasts, formaciones). Para anuncios cortos con guion aporta menos.

## 6. Recordly
- **URL verificada:** https://github.com/webadderall/Recordly. Es un fork de OpenScreen.
- **Qué es:** app de escritorio (Electron, para macOS, Windows y Linux) que graba la pantalla con zooms automáticos, cursor suavizado y marcos. No es una skill ni un MCP.
- **Instalación:** desde las releases, AUR o compilando con `npm install`.
- **Licencia:** **AGPL-3.0.** Algunos listados dicen MIT, pero el LICENSE del repo es AGPL.
- **Último commit:** 2026-10-07.
- **Estrellas:** el reel dice 24k, sin verificar.
- **Riesgos:** pide permisos de grabación de pantalla y tiene un marketplace de extensiones de terceros. La telemetría no se pudo comprobar.
- **Relevancia: MEDIA.** Útil para tutoriales o demos de pantalla (por ejemplo, enseñar resultados de campañas), no para el contenido grabado en estudio.

## 7. MoneyPrinterTurbo
- **URL verificada:** https://github.com/harry0703/MoneyPrinterTurbo.
- **Qué es:** app en Python con WebUI y API que, a partir de un tema, genera guion, busca material de stock, pone voz, subtítulos y música, y produce vídeos faceless en lote. Incluye `docs/skill/SKILL.md` para que un agente la instale y la maneje.
- **Instalación:** con Docker o en local con Python 3.11 o superior. Necesita claves de LLM y de material de stock (Pexels o Pixabay).
- **Licencia:** MIT.
- **Último commit:** 2026-10-09.
- **Riesgos:** el README está lleno de enlaces de afiliado y patrocinios (Kimi, Volcengine, OfoxAI). Hace muchas llamadas a APIs de terceros. Su `SKILL.md` está pensada para que el agente **instale y ejecute** el proyecto de forma autónoma, así que habría que revisarla antes de usarla.
- **Relevancia: BAJA.** Produce vídeos faceless genéricos de stock, que no encajan con anuncios de captación grabados en estudio y pueden perjudicar el rendimiento y la confianza en Meta.

## 8. Instagram Skills (9) y YouTube Agent Skill (11)
- **Instagram, 9 skills.** URL verificada: https://github.com/sergebulaev/instagram-skills. Encaja con lo que dice el reel: exactamente 9 skills (`ig-caption-writer`, `ig-carousel-planner`, `ig-hook-extractor`, `ig-hashtag-strategist`, `ig-humanizer` para quitar la pinta de IA, `ig-audience-insights` para analizar lo que funciona, `ig-repurposer`, `ig-profile-optimizer`, `ig-content-planner`).
  - Es un plugin sin hooks.
  - Instalación: `/plugin install instagram-skills@instagram-skills` después de añadir el marketplace, o `npx skills add sergebulaev/instagram-skills`.
  - Licencia MIT. Último commit 2026-10-06.
  - Riesgos: `ig-audience-insights` usa **Apify** (red, de pago) y la publicación va por **Publora**, que es un servicio de terceros del propio autor y tiene sesgo comercial.
  - Alternativa: https://github.com/Jakeschincariol/instagram-agent-skill. Tiene **13** skills (`ig-reel` con 26 fórmulas de gancho, `ig-viral`, `ig-carousel`, `ig-story`, `ig-human` y otras). Es MIT, del 2026-09-13, sin API y sin red según su README. Su `hooks.json` es un archivo de datos de ganchos, **no un hook de Claude**.
- **YouTube, 11 skills.** URL verificada: https://github.com/Jakeschincariol/youtube-agent-skill. Es la versión original; hay varios clones idénticos de otros usuarios (basirkazi, synapzeai y otros). Trae 11 skills, entre ellas `yt-viral`, el "motor de viralidad".
  - Es un plugin sin hooks reales (`skills/yt-script/hooks.json` es un archivo de datos).
  - Instalación: `/plugin marketplace add Jakeschincariol/youtube-agent-skill` y `/plugin install youtube-agent`, o clonar el repo y copiar `skills/yt-*` a `~/.claude/skills/`.
  - Licencia MIT. Último commit 2026-09-16.
  - Riesgos: incluye scripts Python locales y `yt-viral` lee listados públicos.
- **Relevancia:** **ALTA para Instagram** (ganchos de reels, carruseles, historias, quitar pinta de IA), aunque se solapa con las skills propias de Ceos y conviene usarlo como fuente de ideas en vez de instalarlo a ciegas. **BAJA para YouTube**, salvo la skill de Shorts y la de ganchos.

## 9. Skill de LinkedIn (11 agentes, humanizador y 5 detectores)
- **URL verificada:** https://github.com/Jakeschincariol/linkedin-agent-skill. Encaja: 11 skills, y la skill `li-human` lleva `humanize.py` y `detect.py` con un "panel de detección" de **5 comprobaciones** (burstiness, especificidad, densidad de relleno, huella y voz).
- **Qué es:** plugin y carpeta de skills. `skills/li-post/hooks.json` es un archivo de datos de ganchos, **no un hook de Claude**.
- **Instalación:** `/plugin marketplace add Jakeschincariol/linkedin-agent-skill` y `/plugin install linkedin-agent`, o clonar el repo y copiar `skills/li-*`.
- **Licencia:** MIT.
- **Último commit:** 2026-09-07.
- **Riesgos:** scripts Python locales sin dependencias. Según el README no hay red.
- **Relevancia: BAJA.** La agencia no capta por LinkedIn. Lo aprovechable es el `detect.py` y el `slop.json`, que están en inglés.

## 10. Humanizer
- **blader/humanizer.** URL verificada: https://github.com/blader/humanizer. Es una skill que se distribuye como plugin, sin hooks, y está basada en la página de Wikipedia "Signs of AI writing".
  - Instalación: `/plugin marketplace add blader/humanizer` y `/plugin install humanizer@humanizer` (necesita Claude Code 2.1.142 o superior), o `npx skills add blader/humanizer --global --agent claude-code`.
  - Licencia MIT. Último commit 2026-09-27.
  - Riesgos: ninguno; es solo texto.
- **Skill `/human`.** El origen más probable es un **gist**, no un repo: https://gist.github.com/conradcaffier03/1d72e3ae9cbdde6d80456821392811ad (de @buildwith.conrad, publicado el 15 de julio de 2026). Es un único `SKILL.md` llamado `human` que se guarda en `.claude/skills/human/` y se basa en Wikipedia "Signs of AI writing". No tiene licencia declarada. **No estoy seguro** de que sea el que enseña el reel.
  - Alternativa con soporte de español: https://github.com/alandefreitas/humanize-claude-skill (verificado con ls-remote; contenido no revisado).
- **Relevancia: ALTA.** Todo copy de anuncio y caption pasa por un filtro anti-IA. Ojo: blader trabaja en inglés, y Ceos ya tiene la skill `texto-sin-tono-ia`. Lo más útil es tomar ideas de su lista de patrones.

## 11. Skills de diseño
| Elemento | URL verificada | Qué es | Instalación | Licencia | Último commit | Notas y riesgos |
|---|---|---|---|---|---|---|
| Taste Skill | https://github.com/Leonxlnx/taste-skill | Plugin con 13 skills (`taste-skill`, `minimalist`, `brutalist`, `soft`, `redesign`, `brandkit`, imagegen, etc.) | `npx skills add https://github.com/Leonxlnx/taste-skill` | MIT | 2026-10-08 | Sin hooks |
| Impeccable (/polish) | https://github.com/pbakaus/impeccable | Plugin con 1 skill y 24 comandos (`/impeccable polish`, `audit`, `critique`…) y 59 reglas de detección | `npx impeccable install` y después `/impeccable init` | Apache-2.0 | 2026-10-08 | El plugin de Claude no trae hooks (hay hooks para Codex, Cursor y GitHub). Cada skill trae un lanzador `scripts/impeccable` que ejecuta su motor. Hay iteración en navegador. |
| Motion de Emil Kowalski | https://github.com/emilkowalski/skill (`emilkowalski/skills` redirige aquí) | 14 skills: `animate`, `improve-animations`, `review-animations`, `emil-design-eng`, **`apple-design`**… | `npx skills@latest add emilkowalski/skills` | MIT | 2026-10-02 | Sin hooks. Es del propio autor. |
| UI UX Pro Max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Plugin con 7 skills (ui-ux-pro-max, design-system, brand, banner-design, slides…) y una CLI | `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` y `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`, o `npm i -g ui-ux-pro-max-cli` | MIT | 2026-10-09 | Sin hooks. Hay un `stack/.mcp.json` (no revisado). Las 116k estrellas están **sin verificar**. |
| Awesome Claude Design (68) | https://github.com/VoltAgent/awesome-claude-design | Lista README con 68 entradas (verificado), que enlazan a DESIGN.md de getdesign.md para Claude Design | Copiar el DESIGN.md elegido | MIT | 2026-06-20 | Solo enlaces |
| Design MD Chrome | https://github.com/bergside/design-md-chrome | Extensión de Chrome (TypeUI) que extrae DESIGN.md o SKILL.md de cualquier web | Cargar descomprimida en `chrome://extensions` | MIT | 2026-05-25 | Pide permisos sobre la pestaña activa. Hay copias en la Chrome Web Store de otros autores; usar la del repo. |
| Design Motion Principles | https://github.com/kylezantos/design-motion-principles | 1 skill de motion con modos "build" y "audit" (basada en Emil Kowalski, Jakub Krehel y Jhey Tompkins) | `npx skills add kylezantos/design-motion-principles` | MIT | 2026-05-30 | Sin hooks |
| Reglas de Vercel | https://github.com/vercel-labs/web-interface-guidelines | Documento README de directrices. La skill instalable está en `vercel-labs/agent-skills` (`web-design-guidelines`) | `npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines` | MIT | 2026-10-05 | Solo texto |
| Reglas de diseño de Apple | **No sé cuál enseña el reel.** Candidatos: la skill `apple-design` de emilkowalski/skill; https://github.com/ebuntario/apple-hig (1 skill con 68 referencias, MIT, 2026-04-21); https://github.com/raintree-technology/apple-hig-skills (14 skills con MCP `hig-doctor`, MIT, 2026-09-04) | Skills | `npx skills add …` o copiar a `~/.claude/skills/` | MIT | ver columna anterior | Solo texto. Raintree trae un MCP. |
| SkillUI | https://github.com/amaancoderx/npxskillui (paquete npm `skillui`) | CLI que rastrea una web y genera SKILL.md, DESIGN.md y tokens | `npm install -g skillui` y después `skillui --url <web>`. El modo "ultra" usa Playwright y Chromium. | MIT (según README y npm; el repo no tiene archivo LICENSE) | 2026-05-08 | Ejecuta código npm de un autor pequeño y hace red al rastrear la web |
| Awesome Design | https://github.com/VoltAgent/awesome-design-md | 74 carpetas DESIGN.md (Apple, Notion, Stripe…) en `design-md/` | Copiar el DESIGN.md elegido al proyecto | MIT | 2026-10-05 | Solo texto |

**Relevancia del bloque: MEDIA-ALTA para landings y carruseles.**
- Lo más útil para la agencia: Awesome Design o Awesome Claude Design, Design MD Chrome y SkillUI para clonar el estilo visual de un cliente; Impeccable y Taste Skill para landings; las skills de motion de Emil y kylezantos para las animaciones de los vídeos.
- Lo menos útil: las reglas de Apple HIG y las de Vercel, pensadas para crear apps, que aportan poco.

## 12. Plugins de desarrollo
- **Playwright CLI.** URL verificada: https://github.com/microsoft/playwright-cli. Es una CLI con skills (2 SKILL.md) y Microsoft la recomienda para agentes frente a Playwright MCP (https://github.com/microsoft/playwright-mcp, también verificado).
  - Instalación: `npm install -g @playwright/cli@latest`.
  - Licencia Apache-2.0. Último commit 2026-09-28.
  - Riesgos: maneja un navegador real.
  - Relevancia: MEDIA, para probar landings y formularios de captación y hacer capturas.
- **Context7.** URL verificada: https://github.com/upstash/context7. Es un plugin de Claude con un MCP remoto (`https://mcp.context7.com/mcp`) que trae documentación actualizada de librerías.
  - Instalación: `npx ctx7 setup`, que hace OAuth y genera una API key, o se configura el MCP a mano.
  - Licencia MIT. Último commit 2026-10-09.
  - Riesgos: envía tus consultas a Upstash.
  - Relevancia: BAJA o MEDIA; solo sirve al programar.
- **Plugin de Supabase.** URL verificada: https://github.com/supabase/agent-skills. Es el oficial de Supabase: un marketplace con 2 plugins (`supabase` y `postgres-best-practices`) y un `.mcp.json` que apunta a `https://mcp.supabase.com/mcp?features=docs`.
  - Instalación: `claude plugin marketplace add supabase/agent-skills` y `claude plugin install supabase@supabase-agent-skills`.
  - Licencia MIT. Último commit 2026-10-02.
  - Riesgos: no tiene hooks, pero hay red al MCP de Supabase. Si se amplía con permisos de escritura, puede tocar la base de datos.
  - Relevancia: BAJA, salvo que la agencia guarde leads en Supabase.

## 13. MarkItDown (Microsoft) y su MCP
- **URL verificada:** https://github.com/microsoft/markitdown. Es una librería y CLI en Python que convierte PDF, DOCX, PPTX, XLSX, HTML, imágenes, audio y otros formatos a Markdown. El MCP está en `packages/markitdown-mcp` y expone una sola herramienta, `convert_to_markdown(uri)`.
- **Instalación:** `pip install 'markitdown[all]'` y, para el MCP, `pip install markitdown-mcp` (funciona por STDIO, o por HTTP con `--http --host 127.0.0.1`).
- **Licencia:** MIT.
- **Último commit:** 2026-10-03.
- **Riesgos:** el propio README avisa de que accede a cualquier archivo o URL con los permisos del proceso y que el MCP es solo para uso local. Hay que tener cuidado con URIs que no sean de confianza.
- **Relevancia: MEDIA.** Sirve para pasar a Claude informes de Meta, briefs de clientes en PDF o DOCX y presentaciones.

## 14. Thinking Orbs
- **URL verificada:** https://github.com/Jakubantalik/thinking-orbs. Es un paquete npm con indicadores de carga en forma de esfera de puntos (9 estados animados en canvas 2D). No es una skill ni un MCP. Hay demo en orbs.jakubantalik.com.
- **Instalación:** `npm install thinking-orbs`.
- **Licencia:** MIT.
- **Último commit:** 2026-08-16.
- **Riesgos:** ninguno relevante.
- **Relevancia: BAJA.** Es un componente de interfaz web. Como mucho, un recurso visual para un vídeo o una landing con temática de IA.

## 15. Watermark Remover
- **URL verificada:** https://github.com/guillaumemeyer/watermarks-remover. Probablemente es el del reel: cubre PNG, PDF, SVG, HTML y muchos formatos más.
- **Qué es:** plugin de Claude Code con la skill `remove-ai-marks` (antes `remove-claude-marks`) y un servicio HTTP local en Python que se queda escuchando en `127.0.0.1:8765`. Quita metadatos C2PA, EXIF y XMP, caracteres Unicode invisibles y, "en lo posible", marcas de agua estadísticas de texto.
- **Instalación:** desde su marketplace de plugins, o con `python3 install_skill.py --skill remove-ai-marks --target claude-code`. Además hay que arrancar el servicio local.
- **Licencia:** MIT.
- **Último commit:** 2026-10-09.
- **Riesgos: ALTOS.**
  - **Trae un hook `PostToolUse`** (en `hooks/hooks.json`, ejecuta `node run_hook.js`) que se dispara en **cada Write, Edit, MultiEdit o NotebookEdit**. En modo `clean` modifica archivos sin preguntar.
  - Hay que mantener un servicio local corriendo.
  - La eliminación de marcas de agua de texto no se puede verificar.
  - Quitar marcas de procedencia de IA puede chocar con las políticas de Meta sobre contenido generado o modificado con IA (etiquetado "AI info") y con la transparencia hacia los clientes.
- **Relevancia: BAJA.** No compensa el riesgo. Si hace falta limpiar metadatos EXIF de una imagen concreta, basta con exportarla de nuevo.

---

## Resumen
- **Encontrados y verificados:** 15 de 15 elementos tienen fuente identificada.
- **Con dudas sobre cuál es exactamente el del reel:** el 3 (hay varios candidatos), el 4 (el oficial no tiene repo: es una función nativa de Resolve Studio 21.1), la skill `/human` del 10 (es un gist) y la skill de reglas de Apple del 11.
- **Ningún repo se ha ejecutado.**
- **Hooks reales de Claude Code:** solo `watermarks-remover`. Los `hooks.json` de Jakeschincariol son archivos de datos de ganchos de copy.
- **Telemetría encontrada:** la CLI de Hyperframes (se puede desactivar).
- **Licencias a vigilar:** AGPL en SupoClip y Recordly; licencia de empresa de Remotion para equipos de más de 3 personas.
