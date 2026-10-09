# Fuentes reales de lo que recomienda @revolutia.ai (bloque B)

Fecha de la investigación: 9 de octubre de 2026. No se ha instalado ni ejecutado nada.

**Cómo se ha verificado:**
- Los repos de GitHub se han comprobado con `git ls-remote` y con un clon superficial sin checkout en `scratchpad/repos/`.
- De cada repo se han leído el README, el LICENSE y la fecha del último commit.
- Las estrellas no se han podido leer en GitHub, porque la API no está habilitada en esta sesión. Las cifras salen de agregadores (Star History, OSS Insight, appsecsanta, Skillselion) y son aproximadas.
- Desde este entorno no se han podido abrir las páginas de developers.facebook.com, thenewstack.io ni Manus (el proxy las bloquea). Lo que se dice de ellas sale de los resultados de búsqueda.

**Contexto de uso:** agencia española que capta leads con Meta Ads, los atiende por WhatsApp y los lleva a un CRM.

---

## 1. WhatsApp Business MCP de Meta (lanzado el 15/09/2026)

- **Coincide con el reel:** sí. Varias fuentes confirman que se lanzó el 15 de septiembre de 2026. Meta lo llama **"WhatsApp Business Tools MCP"**.
- **URL:**
  - Documentación oficial de los MCP de Meta: https://developers.facebook.com/documentation/mcp. Según el buscador, esta página "ofrece servidores MCP remotos oficiales para Facebook, Instagram, WhatsApp y Meta Ads", con OAuth y permisos de lectura y de gestión, y cita Claude Desktop y Claude Code como clientes validados.
  - Noticia de referencia: https://thenewstack.io/meta-mcp-whatsapp-business-claude/
  - Otras coberturas: marketing4ecommerce.net, ciol.com y opentools.ai.
  - **No he podido verificar la URL exacta del endpoint MCP.** El dominio está bloqueado desde aquí y ninguna fuente la publica. Hay que sacarla de esa página de documentación.
- **Qué es:** un MCP remoto oficial de Meta.
- **Qué hace:** crea la cuenta de WhatsApp Business, añade, verifica y registra el número en la Cloud API, y avisa de requisitos que falten (método de pago, verificación de la empresa). También configura el webhook (URL de retorno y campos), envía mensajes de prueba y crea o edita plantillas consultando si están aprobadas. Coincide con lo que dice el reel. Lo de "reenviar la plantilla si la rechazan" equivale a editarla y volver a mandarla; no es un reintento automático confirmado.
- **Cómo se conecta a Claude:** como conector remoto con inicio de sesión de Facebook Login for Business. Un administrador tiene que verificarlo antes de que se pueda usar. Funciona con Claude, Codex, Cursor y ChatGPT.
- **Limitaciones según la prensa:**
  - Meta lo está abriendo poco a poco.
  - Está pensado para desarrollo y pruebas, no para enviar mensajes a escala en producción.
  - El token de producción (usuario de sistema y token de larga duración) se sigue sacando aparte, fuera del MCP.
  - El agente no tiene identidad propia: actúa con los permisos del usuario.
- **Coste:** el MCP no tiene precio publicado. Los mensajes se pagan con la tarifa normal de la WhatsApp Cloud API, por conversación o mensaje de plantilla.
- **Licencia:** servicio propietario de Meta. No es un repo.
- **Riesgos:**
  - Es la API oficial, así que no hay riesgo de bloqueo por usar un cliente no oficial.
  - Claude actúa con permisos de administrador sobre el Business Manager: un error puede tocar números o plantillas de clientes.
  - RGPD: los mensajes y los números de los leads pasan por Meta, igual que con la Cloud API. Si Claude lee conversaciones, el contenido también pasa por Anthropic.
- **Relevancia: ALTA.** Es la vía oficial para montar el WhatsApp de cada cliente: alta del número, plantillas de seguimiento de leads y webhook hacia el CRM o n8n. Merece la pena probarlo en un cliente piloto.

---

## 2. OpenWA (API de WhatsApp open source autoalojada)

- **URL verificada:** https://github.com/rmyndharis/OpenWA. Es el repo original; existen copias como Hyd3r1/OpenWA, bsuap o jurby que conviene no usar.
- **Último commit:** 2026-10-09.
- **Coincide con el reel:** sí. Tiene panel en React, varias sesiones a la vez, Docker, webhooks, claves de API y Swagger. También trae nodos comunitarios para n8n, plugins para Chatwoot y Typebot, y un endpoint MCP propio.
- **Qué es:** una pasarela de WhatsApp que se aloja en tu servidor (NestJS y TypeScript), con base de datos SQLite o PostgreSQL y almacenamiento local o en S3.
- **Cómo se conecta a Claude:** por su endpoint MCP o por la API REST. Se pueden crear claves limitadas a ciertos chats.
- **Coste:** gratis. Solo se paga el servidor.
- **Licencia:** MIT.
- **Riesgos (muy altos):**
  - El propio README dice que es **no oficial**: usa clientes de ingeniería inversa (whatsapp-web.js y Baileys), no la Cloud API.
  - Siempre hay riesgo de que WhatsApp **restrinja o bloquee el número**. Baileys tiene más riesgo que whatsapp-web.js.
  - Algunos números ya no pueden vincular dispositivos (piden una passkey).
  - El README dice textualmente que, en entornos UE/RGPD o de mensajería comercial, se trate como **"no aprobado"** y se use la Cloud API oficial.
- **Relevancia: BAJA** para el WhatsApp de clientes. Pone en riesgo el número del cliente y va contra los términos de WhatsApp. Como mucho sirve para pruebas internas con un número desechable.

---

## 3. n8n + YCloud + n8n-MCP + plantillas

- **YCloud:** https://www.ycloud.com/blog/integrate-ycloud-with-n8n (marzo de 2026).
  - Qué es: un BSP de WhatsApp, es decir, un proveedor oficial de la Cloud API. Es un SaaS de pago (cuota y coste por mensaje). Permite "coexistencia": usar el mismo número en la app de WhatsApp Business y en la API.
  - Cómo se conecta: con n8n por webhooks y API. **No he encontrado un nodo comunitario oficial de YCloud.**
  - El reel no enlaza ningún flujo concreto de "chatbot con YCloud", así que no puedo confirmar qué plantilla usa.
- **n8n-MCP:** https://github.com/czlonkowski/n8n-mcp, verificado.
  - Último commit: 2026-10-06. Licencia MIT.
  - Qué es: un servidor MCP local (npx o Docker) o alojado (dashboard.n8n-mcp.com, gratis hasta 100 llamadas al día).
  - Qué da: documentación de unos 2.950 nodos de n8n y 2.352 plantillas. Con `N8N_API_URL` y `N8N_API_KEY`, crea y valida flujos en tu propia instancia de n8n.
  - Cómo se conecta a Claude: guía propia para Claude Code (`docs/CLAUDE_CODE_SETUP.md`) y skills opcionales.
- **Repositorios de plantillas de n8n** (se verificaron 2 conocidos; no consta que sean los del reel):
  - https://github.com/Zie619/n8n-workflows (último commit 2026-06-24).
  - https://github.com/enescingoz/awesome-n8n-templates (último commit 2026-09-12).
- **Riesgos:**
  - La clave de API de n8n da a Claude permiso para crear y modificar flujos de producción.
  - Las plantillas de terceros pueden traer nodos de código o webhooks: hay que revisarlas antes de importarlas.
  - RGPD: los datos de los leads viajan por YCloud, que debe tener un contrato de encargado de tratamiento (DPA).
- **Relevancia: ALTA.** n8n-MCP acelera montar flujos de "lead de Meta → WhatsApp → CRM". YCloud es una opción oficial (BSP) para el WhatsApp de clientes; hay que compararla con un BSP que ya se use o con la Cloud API directa.

---

## 4. Apify MCP

- **URL verificada:** https://github.com/apify/apify-mcp-server
  - Servidor alojado: https://mcp.apify.com
  - Último commit: 2026-10-09. Licencia MIT (en el fichero LICENSE.md).
- **Qué es:** un MCP remoto (Streamable HTTP con OAuth) o local (`npx @apify/actors-mcp-server` con `APIFY_TOKEN`). Da acceso a miles de "Actors" de Apify Store, entre ellos scrapers de Google Maps, Instagram y LinkedIn.
- **Cómo se conecta a Claude:** en Claude.ai o Claude Desktop, añadiendo `https://mcp.apify.com` como conector personalizado (OAuth). En Claude Code, como servidor HTTP.
- **Coste:** SaaS de pago por uso, con un plan gratuito que da crédito mensual. Cada Actor cobra por ejecución o por resultado. También admite pagos "agénticos" (x402 y Skyfire).
- **Riesgos:**
  - Scrapear LinkedIn o Instagram va contra los términos de esas plataformas.
  - RGPD: los datos personales extraídos (nombres, teléfonos, emails de personas) necesitan base legal (interés legítimo documentado) y hay que informar a los afectados. En España, las comunicaciones comerciales no solicitadas también están limitadas por la LSSI.
  - Los datos de empresas de Google Maps son menos problemáticos.
- **Relevancia: MEDIA-ALTA.** Sirve para prospectar clientes de la agencia (negocios locales en Google Maps por nicho y ciudad). No sirve para los leads de clientes, que ya llegan por Meta.

---

## 5. ScrapeGraphAI y "Scrape Graph API"

- **URL verificada:** https://github.com/ScrapeGraphAI/Scrapegraph-ai. Último commit: 2026-10-06. Licencia MIT.
- **Qué es:** una librería de Python (`pip install scrapegraphai`) que convierte instrucciones en lenguaje natural en un proceso de scraping. Funciona con OpenAI, Gemini o con modelos locales a través de Ollama.
- **Cómo se conecta a Claude:** tiene un servidor MCP (`ScrapeGraphAI/scrapegraph-mcp`, listado en Smithery) que usa su API de pago.
- **"Scrape Graph API" de 29k estrellas que corre en local:** casi seguro es **el mismo repo**. Las fuentes le dan entre 27.000 y 30.700 estrellas, y la versión local es la librería con Ollama. Su API en la nube (scrapegraphai.com) es de pago: el SDK es MIT y el servicio se cobra. No he encontrado otro repo distinto con ese nombre.
- **Coste:** la librería es gratis; el LLM y la API se pagan aparte.
- **Riesgos:** RGPD si se extraen datos personales. Es una librería que ejecuta código local, así que hay que instalarla en un entorno aislado.
- **Relevancia: MEDIA-BAJA.** Para la agencia, Apify ya cubre los casos útiles con menos montaje.

---

## 6. Scrapling MCP y Agent Reach

### Scrapling
- **URL verificada:** https://github.com/D4Vinci/Scrapling
  - Último commit: 2026-10-08. Licencia BSD-3-Clause.
  - Unas 71.500 estrellas según agregadores, lo que encaja con los "70k" del reel.
- **Qué es:** una librería de scraping en Python con servidor MCP integrado (documentación: https://scrapling.readthedocs.io/en/latest/ai/mcp-server.html). Es un MCP local.
- **Cómo se conecta a Claude:** como MCP local con el comando `scrapling mcp`, tras instalarlo con pip.
- **Coste:** gratis.
- **Riesgos:** está diseñado para **saltarse sistemas antibots** (Cloudflare Turnstile, falsificación de la huella del navegador). Eso choca con los términos de muchas webs y tiene riesgo legal. Aplica RGPD a los datos personales.

### Agent Reach
- **URL verificada:** https://github.com/Panniantong/Agent-Reach
  - Último commit: 2026-10-08. Licencia MIT.
  - Entre 20.000 y 53.000 estrellas según la fuente.
- **Qué es:** una skill para agentes (`agent_reach/skill/SKILL.md`) más una herramienta de línea de comandos en Python. Instala y comprueba programas de terceros como yt-dlp, Jina Reader, clientes de Twitter y Reddit, y mcporter.
- **Matiz importante frente al reel:** **no todo funciona "sin API key"**.
  - Sin configurar: YouTube, webs y perfiles públicos de LinkedIn (vía Jina).
  - **Twitter/X y Reddit necesitan las cookies de tu sesión.**
  - Los perfiles completos de LinkedIn también requieren configuración.
- **Cómo se conecta a Claude:** el agente instala la skill y ejecuta comandos de shell (`pip install`, etc.).
- **Coste:** gratis.
- **Riesgos:**
  - El agente instala y ejecuta paquetes de terceros con permisos amplios.
  - Usar cookies de tus cuentas personales arriesga el bloqueo de esas cuentas.
  - El README está casi todo en chino y tiene banners patrocinados.
- **Relevancia (ambos): BAJA-MEDIA.** Puede ayudar a investigar el mercado (Reddit, YouTube, ver qué dice la competencia), no a gestionar leads.

---

## 7. Vibe Prospecting y Explorium MCP

- **URLs verificadas:**
  - Plugin para Claude Code: https://github.com/explorium-ai/vibeprospecting-plugin (último commit 2026-10-04, MIT, sin hooks).
  - MCP: https://github.com/explorium-ai/vibeprospecting-mcp, endpoint `https://vibeprospecting.explorium.ai/mcp`.
  - MCP genérico de Explorium: https://github.com/explorium-ai/mcp-explorium, endpoint `https://mcp.explorium.ai/mcp` (último commit 2026-01-22, MIT).
  - Documentación: https://docs.vibeprospecting.ai/plugin y /connector.
- **Qué es:** un MCP remoto con OAuth y un plugin para Claude Code. Está en el marketplace comunitario de Anthropic: `claude plugin marketplace add anthropics/claude-plugins-community` y luego `claude plugin install vibe-prospecting@claude-community`. En Claude.ai o Desktop se añade como conector.
- **Datos que dice tener:** más de 150 millones de empresas y 800 millones de profesionales. El reel dice 100M; las cifras son del propio fabricante.
- **Coste:** SaaS por créditos, con un nivel gratuito limitado. No he verificado los precios.
- **Riesgos:** enriquece contactos de personas (emails y teléfonos), así que aplica RGPD: base legal, deber de informar y LSSI para emails comerciales. La cobertura de pymes españolas no está verificada y probablemente sea floja.
- **Relevancia: MEDIA.** Sirve para prospectar empresas a las que vender la agencia. Para negocios locales españoles, Google Maps vía Apify probablemente rinde más.

---

## 8. CRM open source clon de Salesforce

- **Confirmado: Twenty.** https://github.com/twentyhq/twenty
  - Último commit: 2026-10-09.
  - Unas 49.700 estrellas según un listado de 2026; el reel dice 51k, que es verosímil hoy.
- **Licencia:** **AGPL-3.0**, con algunos ficheros marcados `@license Enterprise` bajo licencia comercial.
- **Qué es:** un CRM que se puede usar en la nube (twenty.com, de pago) o alojar en tu servidor con Docker Compose (gratis).
- **Cómo se conecta a Claude:** trae un **MCP integrado en cada espacio de trabajo** (`https://<workspace>/mcp`, con OAuth) y skills oficiales en `packages/twenty-agent-skills` (`use-twenty-mcp`). También tiene API y una integración con Zapier.
- **Riesgos:**
  - Si se aloja en tu servidor, la agencia es responsable de la seguridad y las copias de seguridad de los datos de los leads (RGPD).
  - La AGPL obliga a publicar el código si se modifica y se ofrece como servicio.
  - Conectarlo con WhatsApp requiere montarlo aparte (n8n).
- **Relevancia: MEDIA-ALTA.** Es un CRM serio sin coste por usuario y se integra con Claude por MCP. Habría que compararlo con lo que la agencia ya use (por ejemplo HubSpot o GoHighLevel).

---

## 9. Skill de scraping de leads "alternativa a Apollo"

- **NO ENCONTRADO** con seguridad. No hay ningún repo que encaje claramente con la descripción del reel.
- **Candidatos aproximados (sin verificar que sean el del reel):**
  - El plugin de Firecrawl para Claude Code (github.com/firecrawl/firecrawl-claude-plugin; plan gratuito de 500 créditos).
  - La skill "email-finder" de shipshitdev (24 estrellas).
  - La skill "apollo-outreach" de openclaudia (usa la API de Apollo, de pago).
- **Riesgos:** RGPD y LSSI al extraer emails de personas. Scrapear Apollo va contra sus términos.
- **Relevancia: BAJA** mientras no se identifique el repo.

---

## 10. Composio

- **URL verificada:** https://github.com/ComposioHQ/composio (último commit 2026-10-09, MIT). Web: https://composio.dev
- **Qué es:** un SaaS con SDK que da más de 1.000 integraciones con la autenticación ya resuelta, entre ellas Canva.
- **Cómo se conecta a Claude:** cada sesión genera una URL MCP alojada que se añade en Claude Code con `/mcp`, o como conector personalizado en Claude.ai. También tiene una herramienta de línea de comandos y adaptadores para el Claude Agent SDK.
- **Coste:** plan gratuito de unas 20.000 llamadas al mes según su propio blog; los planes de pago no están verificados. El código del SDK es MIT; el servicio es propietario.
- **Riesgos:** Composio guarda los tokens OAuth de todas las apps que conectes (Gmail, CRM, WhatsApp…): es un tercero con acceso a todo. RGPD: hace falta un contrato de encargado de tratamiento.
- **Relevancia: MEDIA.** Ya existen conectores de Canva, Zapier y Make que cubren lo mismo. Composio solo aporta si falta una app concreta.

---

## 11. SEO: stack de 4 skills y plugin de 18 agentes y 25 skills

### Stack de 4 skills (Auditor con Search Console y 180 comprobaciones, AI Search Spy, Diagnoser, Fixer)
- **NO ENCONTRADO.** No hay ningún repo con esos nombres ni con 180 comprobaciones.
- **Lo más parecido:**
  - https://github.com/houtini-ai/seo-audit: MCP que cruza Search Console con un rastreo de la web. Tiene **99 comprobaciones**, no 180. Apache-2.0, último commit 2026-10-06.
  - https://github.com/Hainrixz/claude-seo-ai: plugin con auditoría para Google y para buscadores de IA, más un "fixer" que hay que activar. Tiene 25 comprobaciones y 151 tipos de hallazgo. MIT, último commit 2026-09-06.
  - Ninguno es con seguridad el del reel.

### Plugin de 18 agentes y 25 skills
- **Casi seguro:** https://github.com/AgriciDaniel/claude-seo (MIT, último commit 2026-10-05, unas 9.400 estrellas).
- La versión de "25 sub-skills y 18 subagentes" es la que describe su copia (fork) sritinsightanalyst/claude-seo. **Hoy el original anuncia 26 skills y 19 agentes**; en el repo hay 35 ficheros SKILL.md y 19 agentes.
- **Qué es:** un plugin de Claude Code. Usa Search Console con credenciales propias y extensiones opcionales de pago (DataForSEO, Firecrawl).
- **Riesgos:** **trae un hook `PostToolUse`** que ejecuta `node` y un script de Python (`validate-schema.py`) en cada Edit/Write. Es decir, ejecuta código automáticamente en tu máquina. Hay que revisarlo antes de instalar. Las extensiones de pago generan costes.
- **Relevancia: BAJA-MEDIA.** La agencia capta con Meta Ads, no con SEO. Solo sirve para la web propia o si se vende SEO.

---

## 12. Google Agent Skills oficiales

- **URL verificada:** https://github.com/google/skills (último commit 2026-10-09, Apache-2.0).
  - Anuncio: https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository/
- **Qué es:** un repositorio de skills con formato estándar (agentskills.io). Se instala con `npx skills add google/skills`.
- **Contenido:** el repo tiene **161 ficheros SKILL.md**, lo que encaja con las "100+" del reel. Hay skills de:
  - Ads: Google Ads API, configuración del MCP de Google Ads, Data Manager API (audiencias y eventos).
  - Analytics: Admin API y Data API de GA4.
  - Gemini API, Firebase, y Cloud (BigQuery, Cloud Run, GKE…).
- **Coste:** gratis. Las APIs de Google se pagan aparte.
- **Riesgos:** bajos. Son instrucciones, aunque algunas incluyen scripts.
- **Relevancia: MEDIA-BAJA.** Útil si la agencia lleva también Google Ads o GA4. No aporta nada para Meta Ads ni WhatsApp.

---

## 13. Strix y el plugin de seguridad de Anthropic

### Strix
- **URL verificada:** https://github.com/usestrix/strix
  - Último commit: 2026-10-08. Licencia Apache-2.0.
  - Unas 46.000 estrellas en julio de 2026, lo que encaja con los "45k" del reel.
- **Qué es:** una herramienta de línea de comandos que hace pruebas de intrusión (pentest) con agentes. Funciona en local con Docker y con tu propia clave de un LLM (Anthropic, OpenAI…). Tiene versión empresarial de pago e incluye skills para Claude Code.
- **Riesgos:** **lanza exploits reales.** Solo se puede usar contra sistemas propios o con autorización. Usarlo contra webs ajenas es delito. Consume muchos tokens.

### Plugin de seguridad de Anthropic
- **Identificado:** **"claude-security"**, en el marketplace oficial https://github.com/anthropics/claude-plugins-official, ruta `plugins/claude-security`. Último commit del repo: 2026-10-09.
  - Se instala con `/plugin install claude-security@claude-plugins-official` y se usa con `/claude-security`.
  - Es la versión para usar dentro de una sesión del producto Claude Security. Salió en beta, con fecha de lanzamiento del 22/07/2026 según una fuente.
- **Qué hace:** un equipo de agentes mapea la arquitectura del código, construye un modelo de amenazas y busca fallos. Cada hallazgo lo revisan **verificadores independientes** que intentan refutarlo, lo que encaja con los "jueces" del reel.
- **Qué entrega:** un informe en Markdown, JSONL y SARIF. El formato SARIF lleva fichero y línea de cada fallo. También puede proponer parches.
- **Lo que no está confirmado:** las cifras de "100 agentes" y "3 jueces" no aparecen en la documentación. El número de agentes depende del alcance y del nivel de esfuerzo elegidos.
- **Riesgos:** **trae hooks** (`hooks/hooks.json`) que ejecutan `hooks.sh` al abrir el menú, después de algunos comandos Bash y tras `git push`. Son del propio Anthropic. El escaneo trabaja con tus permisos, sin aislamiento, y el README recomienda no usarlo en repos que no sean de confianza. Gasta muchos tokens.
- No hay que confundirlo con el plugin "security-guidance", que también es de Anthropic pero solo revisa en la misma sesión el código que Claude va escribiendo.

- **Relevancia (ambos): BAJA.** La agencia no desarrolla software. Solo tendría sentido para revisar landings o automatizaciones propias con código.

---

## 14. Manus Cloud Computer

- **Coincide con el reel:** sí. Se lanzó el 30/04/2026.
  - Fuentes: https://www.testingcatalog.com/manus-launches-cloud-computer-with-service-hosting-capabilities/ y idlen.io. Web del producto: manus.im (no verificada desde aquí).
- **Qué es:** un SaaS de pago que da una máquina virtual Ubuntu en la nube siempre encendida. Sirve para tener bots, scrapers y tareas programadas funcionando 24/7. Se accede por SSH o terminal web.
- **Relación con Claude:** **no es una herramienta de Claude**; es la competencia (Manus). En una VM así se podría ejecutar Claude Code con una API key, pero eso no forma parte del producto.
- **Coste:** por niveles según computación y almacenamiento. Los precios no están verificados.
- **Riesgos:** datos de clientes en una infraestructura de terceros (RGPD, transferencias internacionales). Si se usa para bots de WhatsApp no oficiales, aplican los mismos riesgos de bloqueo que con OpenWA.
- **Relevancia: BAJA.** Para tener automatizaciones 24/7 ya existen Make, n8n en la nube o las tareas programadas de Claude.

---

## Resumen

| # | Elemento | Fuente verificada | Relevancia |
|---|---|---|---|
| 1 | MCP de WhatsApp Business de Meta | Sí (docs de Meta y prensa); URL del endpoint sin verificar | ALTA |
| 2 | OpenWA | rmyndharis/OpenWA | BAJA (no oficial, riesgo de bloqueo) |
| 3 | n8n-MCP, YCloud, plantillas | czlonkowski/n8n-mcp, blog de YCloud, 2 repos de plantillas | ALTA |
| 4 | Apify MCP | apify/apify-mcp-server, mcp.apify.com | MEDIA-ALTA |
| 5 | ScrapeGraphAI | ScrapeGraphAI/Scrapegraph-ai (la "API de 29k" probablemente es el mismo repo) | MEDIA-BAJA |
| 6 | Scrapling y Agent Reach | D4Vinci/Scrapling, Panniantong/Agent-Reach | BAJA-MEDIA |
| 7 | Vibe Prospecting y Explorium | repos de explorium-ai (plugin y mcp) | MEDIA |
| 8 | CRM clon de Salesforce | twentyhq/twenty (confirmado) | MEDIA-ALTA |
| 9 | Skill "alternativa a Apollo" | NO ENCONTRADO | — |
| 10 | Composio | ComposioHQ/composio | MEDIA |
| 11 | Stack de 4 skills de SEO | NO ENCONTRADO (aproximados: houtini-ai/seo-audit, Hainrixz/claude-seo-ai) | — |
| 11 | Plugin SEO de 18 agentes y 25 skills | AgriciDaniel/claude-seo (hoy 26 skills y 19 agentes, con hook) | BAJA-MEDIA |
| 12 | Google Agent Skills | google/skills (161 skills) | MEDIA-BAJA |
| 13 | Strix y claude-security | usestrix/strix, anthropics/claude-plugins-official/plugins/claude-security | BAJA |
| 14 | Manus Cloud Computer | Sí (prensa) | BAJA |
