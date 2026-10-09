# Repos recomendados por @revolutia.ai: verificación (lote A)

Fecha de la comprobación: 2026-10-09. Cada repo se ha comprobado con `git ls-remote` y un `git clone --depth 1` en `scratchpad/repos/`. No se ha ejecutado nada de los repos. Las cifras de estrellas no se han comprobado; los recuentos de skills salen de contar archivos SKILL.md o de los manifiestos.

Contexto para la relevancia: Ceos es una agencia de captación con Meta Ads que crea contenido de Instagram con Claude. **Relevancia alta** = ayuda directamente con copy, anuncios, landings, contenido o el uso diario de Claude. **Baja** = está pensado para equipos de desarrollo de software.

---

## 1. Everything Claude Code (ECC), de Affaan Mustafa
- **URL:** https://github.com/affaan-m/ECC. Antes se llamaba `affaan-m/everything-claude-code`, que redirige a la misma rama: el mismo commit `ef648e0`. **Coincidencia segura.**
- **Qué es:** un plugin de Claude Code muy grande (v2.2.3) que incluye **hooks**, agentes, skills, comandos y reglas. También trae `.mcp.json`, que arranca `chrome-devtools-mcp` con npx, y una CLI de npm (`ecc-universal`).
- **Cifras actuales:** 68 agentes, 293 skills, 94 "legacy command shims", según `plugin.json` y lo que hay en las carpetas. El reel dice 292 skills: cuadra con una versión anterior.
- **Instalación (README):** `/plugin marketplace add https://github.com/affaan-m/ECC` y luego `/plugin install ecc@ecc`. El reel dice "/plugin install ECC", pero el identificador actual es `ecc@ecc`. Otras vías: `npx ecc-universal@2.2.3 setup` o `./install.sh --profile minimal|core|full`.
- **Licencia:** MIT. **Último commit:** 2026-10-01.
- **Hackathon:** el README dice "Won the Anthropic x Forum Ventures hackathon in Sep 2025" y "Built at the Claude Code Hackathon (Cerebral Valley x Anthropic, Feb 2026)".
- **Riesgos:** hooks activados por defecto (`hooks_enabled: true`) en casi todos los eventos: 9 PreToolUse, 7 Stop, además de SessionStart, PostToolUse, PreCompact y SessionEnd. Son unos 976 scripts js/sh/py. Hay "telemetría" de skills (`skill-run-tracker.js`), pero escribe en un archivo local (`~/.claude/state/skill-runs.jsonl`); no he visto envío a la red en ese hook. El servidor MCP se descarga con npx. Es mucho contexto y mucha automatización en una sola instalación.
- **Relevancia: baja-media.** Está orientado a ingeniería: TDD, revisión de código y seguridad. Hay alguna skill de contenido o marketing suelta, pero instalarlo entero es excesivo para Ceos. Si interesa algo, mejor copiar a mano la skill concreta, sin los hooks.

## 2. "63 agentes de IA, 249 skills" (sep 2026)
- **URL:** https://github.com/affaan-m/ECC. **Es ECC.** La traducción al español del README del propio repo (`docs/es/README.md` y `docs/es/AGENTS.md`) dice literalmente "63 agentes, 249 skills y 79 shims de comandos". Es una versión anterior de las cifras del punto 1.
- Licencia, instalación, riesgos y relevancia: los mismos que en el punto 1.

## 3. Arena Skill (100 subagentes que compiten)
- **URL:** https://github.com/Jakeschincariol/arena-skill. **Coincidencia segura:** el README dice "make 100 versions of it fight to the death… 100 becomes 50, 25, 13, 7, 4, 2, 1". Existe un fork en español, `akiotanaka847/arena-skill`, que no he verificado.
- **Qué es:** una sola skill (`skills/arena/SKILL.md`, con `strategies.json` y `rubric.md`) y un `bracket.py` en Python con solo la librería estándar. Se puede instalar también como plugin de Claude Code, sin hooks ni MCP.
- **Instalación:** pegar la URL en Claude, copiar la carpeta, o `/plugin marketplace add Jakeschincariol/arena-skill` y luego `/plugin install arena-skill@arena-skill`.
- **Licencia:** MIT. **Último commit:** 2026-09-26.
- **Riesgos:** Claude ejecuta `bracket.py` con `python3`. Sus importaciones (argparse, json, os, random…) no tocan la red, y todo se escribe en `.arena/`. **El riesgo real es el coste:** una ronda completa son unas 595 llamadas a subagentes (el modo `--quick` usa 16), y eso consume mucho uso de Claude.
- **Relevancia: media.** Puede servir para elegir el mejor gancho, ángulo de anuncio o titular de landing cuando Claude se atasca, con `--quick` o pocos agentes. No es para el día a día por el consumo.

## 4. Find Skills (buscador de skills de Vercel)
- **URL:** https://github.com/vercel-labs/skills, skill `skills/find-skills/SKILL.md`. **Coincidencia probable.** Es la CLI `npx skills` y el directorio skills.sh de Vercel Labs. Agregadores externos dan unos 3 millones de instalaciones para find-skills, lo que cuadra con el reel. No he podido confirmar el "ingeniero de Vercel" ni las "~700.000 skills".
- **Qué es:** una skill suelta (find-skills) que usa la CLI de npm `skills` (`npx skills find` / `npx skills add`) para buscar en skills.sh.
- **Instalación:** `npx skills add vercel-labs/skills --skill find-skills` (se puede añadir `--agent claude-code`).
- **Licencia:** MIT. **Último commit:** 2026-10-09.
- **Riesgos:** la CLI hace peticiones de red a skills.sh y GitHub y tiene **telemetría anónima activada por defecto**; se desactiva con `DISABLE_TELEMETRY` o `DO_NOT_TRACK`. Además, la skill invita a instalar skills de terceros sin revisarlas, y ese es el riesgo principal.
- **Relevancia: media.** Es útil para descubrir skills de marketing, pero cada skill que encuentre hay que revisarla antes de instalarla.

## 5. "Prompt audit" del equipo de Claude (auditar CLAUDE.md)
- **URL:** no es un repo. Es un **comando integrado de Claude Code**, confirmado en el CHANGELOG oficial (`anthropics/claude-code`, versión 2.1.283): "Added `/doctor prompt-audit` (also `/checkup prompt-audit`) to audit your CLAUDE.md files, skills, agents and commands for prompting patterns written for older models". Desde la 2.1.221 existe además `/claude-api prompt-audit`, que audita prompts de aplicaciones con el SDK y no CLAUDE.md.
- **Instalación:** ninguna; basta con Claude Code 2.1.283 o posterior.
- **Licencia y fecha:** no aplican (es parte de Claude Code).
- **Riesgos:** ninguno especial. Según fuentes externas solo propone cambios (diffs) y no modifica archivos si no se le pide.
- **Relevancia: alta.** Ceos tiene CLAUDE.md y varias skills propias, y este comando sirve para limpiarlos.

## 6a. Superpowers (obliga a planear y testear)
- **URL:** https://github.com/obra/superpowers, de Jesse Vincent. **Coincidencia segura.**
- **Qué es:** un plugin de Claude Code con 14 skills de flujo de trabajo (brainstorming, writing-plans, test-driven-development, systematic-debugging, subagent-driven-development, etc.) y **1 hook SessionStart**, que inyecta "using-superpowers" al arrancar, limpiar y compactar.
- **Instalación:** `/plugin install superpowers@claude-plugins-official` (ya está en el marketplace oficial), o `/plugin marketplace add obra/superpowers-marketplace` y luego `/plugin install superpowers@superpowers-marketplace`.
- **Licencia:** MIT. **Último commit:** 2026-09-25.
- **Riesgos:** un único hook que ejecuta un script local al iniciar la sesión; no he visto llamadas de red en él. Cambia el comportamiento por defecto: obliga a planificar, hacer TDD y usar worktrees.
- **Relevancia: baja-media.** Está pensado para desarrollo de software. Las skills de brainstorming y de planificación sí pueden servir en tareas largas.

## 6b. gstack de Garry Tan
- **URL:** https://github.com/garrytan/gstack. **Coincidencia segura** (Garry Tan, CEO de Y Combinator). Hoy tiene unas 56 carpetas de skills, no 23 como dice el reel.
- **Qué es:** un pack de skills con roles (/office-hours, /plan-ceo-review, /review, /qa, /cso, design…) y además binarios propios: un navegador headless (`/browse`) que necesita Bun y descarga Chromium.
- **Instalación:** `git clone --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`.
- **Licencia:** MIT. **Último commit:** 2026-10-09.
- **Riesgos:** **`./setup` compila binarios y descarga Chromium**; son unos 1.970 scripts. Tiene **telemetría opt-in** que envía a Supabase (se desactiva con `gstack-config set telemetry off`). El README también propone modificar CLAUDE.md.
- **Relevancia: baja-media.** Es una "fábrica de software". La /qa con navegador real podría servir para revisar landings, pero la instalación es pesada.

## 6c. Plugin oficial "Claude Code Setup" de Anthropic
- **URL:** https://github.com/anthropics/claude-plugins-official, en `plugins/claude-code-setup`. **Coincidencia segura.**
- **Qué es:** un plugin con una sola skill (`claude-automation-recommender`) que analiza el proyecto y recomienda MCPs, skills, hooks, subagentes y comandos. Según su README es de solo lectura y no tiene hooks.
- **Instalación:** desde el marketplace oficial con `/plugin install claude-code-setup@claude-plugins-official`. Ese nombre lo deduzco de la estructura del marketplace; no figura en el README del plugin.
- **Licencia:** Apache 2.0. **Último commit del repo:** 2026-10-09.
- **Riesgos:** mínimos.
- **Relevancia: media.** Puede proponer automatizaciones para el repo de Ceos. Del mismo marketplace, `claude-md-management` también encaja con el punto 5.

## 6d. Repositorio oficial de skills de Anthropic
- **URL:** https://github.com/anthropics/skills. **Coincidencia segura.**
- **Qué es:** 19 skills (docx, pdf, pptx, xlsx, frontend-design, canvas-design, brand-guidelines, skill-creator, mcp-builder, theme-factory…) y un marketplace de plugins.
- **Instalación:** `/plugin marketplace add anthropics/skills` y luego `/plugin install document-skills@anthropic-agent-skills` o `example-skills@anthropic-agent-skills`.
- **Licencia:** mixta. Las skills de ejemplo son Apache 2.0; las de documentos (docx, pdf, pptx, xlsx) son source-available con restricciones. Último commit: 2026-10-09.
- **Riesgos:** scripts de Python para manipular documentos; sin hooks.
- **Relevancia: media-alta.** Muchas ya están disponibles en esta sesión (`anthropic-skills:*`). Para contenido visual pueden ayudar `canvas-design`, `brand-guidelines` y `frontend-design`.

## 7. Ruflo (antes Claude Flow)
- **URL:** https://github.com/ruvnet/ruflo. `ruvnet/claude-flow` apunta al mismo commit (`a1f9050`), así que es el mismo repo renombrado. **Coincidencia segura.**
- **Qué es:** un "meta-harness" para Claude Code y Codex. Incluye CLI de npm (`ruflo`), **servidor MCP** (unas 314 herramientas), **daemon**, memoria vectorial, "federation" entre máquinas, 48 plugins, unos 98 agentes y **hooks** (PreToolUse, PostToolUse, PreCompact, Stop).
- **Instalación:** `/plugin marketplace add ruvnet/ruflo` y luego `/plugin install ruflo-core@ruflo` (más ruflo-console y ruflo-mods). La versión completa se instala con `npx ruflo@latest init wizard`.
- **Licencia:** MIT. **Último commit:** 2026-10-09.
- **Riesgos: altos.** Los hooks llaman a `npx --prefer-offline --yes ruflo@latest hooks …` en cada edición o comando, así que se descarga y ejecuta la última versión de npm sin fijar. Hay daemon, federación en red y unos 4.000 scripts. Es mucha superficie y mucho consumo.
- **Relevancia: baja.** Está pensado para orquestar enjambres de agentes de código, no para una agencia de contenido.

## 8. The Agency (agencia de agentes open source)
- **URL:** https://github.com/msitarzewski/agency-agents. **Coincidencia segura:** el README dice "From frontend wizards to Reddit community ninjas…".
- **Qué es:** unos 300 archivos .md de **subagentes** (no SKILL.md) organizados por divisiones: engineering, design, marketing (37 agentes, entre ellos `instagram-curator`, `carousel-growth-engine`, `social-media-strategist`, `reddit-community-builder`), **paid-media** (7, entre ellos `paid-social-strategist`, `creative-strategist`, `tracking-specialist`, `auditor`), sales, etc. Hay también una app de escritorio aparte.
- **Instalación:** `./scripts/install.sh --tool claude-code` o copiar a mano: `cp marketing/*.md ~/.claude/agents/`. También con la app o `brew install --cask msitarzewski/agency-agents/agency-agents`.
- **Licencia:** MIT. **Último commit:** 2026-10-07.
- **Riesgos:** bajos si se copian a mano solo los .md que interesen. Los scripts de instalación solo copian o convierten archivos, y no hay hooks.
- **Relevancia: alta.** Los agentes de paid-media y los de Instagram o carruseles encajan directamente con Ceos. Conviene revisarlos y adaptarlos al estilo de la casa.

## 9. Agent Skills del "exdirector de ingeniería de IA de Google"
- **URL:** https://github.com/addyosmani/agent-skills, de Addy Osmani. **Coincidencia probable.** Hay 25 skills (el README dice "install all 25 skills"; el reel dice 24, que sería una versión anterior). Addy Osmani fue director de ingeniería en Google (Chrome); no he verificado el cargo exacto que cita el reel.
- **Qué es:** un plugin de Claude Code con skills de todo el ciclo de desarrollo (spec, plan, build, test, review, ship) y comandos. Tiene una carpeta `hooks/` con scripts sh, pero `plugin.json` no declara hooks.
- **Instalación:** `npx skills add addyosmani/agent-skills`, o `/plugin marketplace add addyosmani/agent-skills` y luego `/plugin install agent-skills@addy-agent-skills`.
- **Licencia:** MIT. **Último commit:** 2026-10-03.
- **Riesgos:** bajos.
- **Relevancia: baja.** Es ingeniería de software; quizá aproveche la skill "interview-me" para sacar requisitos.

## 10. Auto-Research (testea y optimiza tus skills en bucle)
- **Candidato A, coincide con la descripción:** https://github.com/zircote/autoresearch. Dice "Autonomous skill improvement for Claude Code plugins… modify the skill, evaluate it against fixed evals, keep improvements, discard regressions". Es un plugin con una skill (`/autoresearch path/to/skill`, `--eval-doctor`) y sin hooks. Instalación: `claude plugins add ./` tras clonar. Licencia MIT. **Último commit: 2026-03-27**, poco mantenido. Usa Python (pyproject).
- **Candidato B, el más popular:** https://github.com/uditgoenka/autoresearch (v2.2.2). Es un bucle "modificar → verificar → conservar o descartar" para cualquier métrica (código, contenido, marketing), **no específico de skills**. Plugin con **muchos hooks** (PreToolUse, UserPromptSubmit, SubagentStart, SessionStart, SessionEnd) que ejecutan scripts de Node, todos activados por defecto. Envía un webhook solo si se define `AR_NOTIFY_WEBHOOK`. Instalación: `npx skills add uditgoenka/autoresearch` o `/plugin marketplace add uditgoenka/autoresearch` y luego `/plugin install autoresearch@autoresearch`. Licencia MIT. Último commit: 2026-08-13.
- **No sé seguro cuál es el del reel.** Por la descripción ("optimiza tus skills") encaja más zircote; por popularidad, uditgoenka.
- **Relevancia: media.** Puede servir para mejorar las skills propias de Ceos con evaluaciones (copy-ads-ceos, carruseles…). Para eso también sirve `skill-creator`, que ya está disponible en esta sesión.

## 11. Prompt Master
- **URL:** https://github.com/nidhinjs/prompt-master. **Coincidencia segura:** el README habla de "35 credit killing patterns" y de "Zero tokens or credits wasted".
- **Qué es:** una sola skill (SKILL.md y `references/` con patterns y templates). No tiene scripts ni hooks.
- **Instalación:** descargar el ZIP y subirlo en claude.ai (Customize → Skills → Upload), o `git clone … ~/.claude/skills/prompt-master`.
- **Licencia:** MIT. **Último commit:** 2026-08-24.
- **Riesgos:** ninguno técnico.
- **Relevancia: media.** Útil para pasar de una idea desordenada a un prompt para herramientas de vídeo o imagen (Midjourney, etc.). El valor real depende del contenido de la skill.

## 12. LLM Council de Andrej Karpathy
- **URL:** https://github.com/karpathy/llm-council. **Coincidencia segura.**
- **Qué es:** **no es una skill**. Es una app web local (backend FastAPI y frontend en npm) que manda la pregunta a varios modelos vía **OpenRouter**; los modelos se evalúan entre ellos de forma anónima y un "Chairman" da la respuesta final. Karpathy avisa: "99% vibe coded… I'm not going to support it".
- **Instalación:** `uv sync`, `npm install` en `frontend/`, un `.env` con `OPENROUTER_API_KEY` y `./start.sh`.
- **Licencia:** no hay archivo LICENSE. **Último commit:** 2025-11-22.
- **Riesgos:** requiere una API key de pago de OpenRouter y envía las consultas a terceros.
- **Relevancia: baja como app.** La idea ya está aplicada en la skill `consejo-5-asesores` de esta sesión.

## 13. GitHub Spec Kit
- **URL:** https://github.com/github/spec-kit. **Coincidencia segura.**
- **Qué es:** una CLI en Python (`specify`) que prepara un proyecto para "spec-driven development" con comandos (/specify, /plan, /tasks…) y scripts que se copian al proyecto.
- **Instalación:** `uv tool install specify-cli` y luego `specify init <proyecto> --integration <agente>`.
- **Licencia:** MIT. **Último commit:** 2026-10-09.
- **Riesgos:** instala una CLI y añade scripts bash o PowerShell al proyecto.
- **Relevancia: baja.** Está pensado para desarrollo de software.

## 14. "Departamento de marketing" con 29 skills
- **URL más probable:** https://github.com/coreyhaines31/marketingskills, de Corey Haines. **No es seguro.** Una guía en español (tododeia, "29 habilidades de marketing") lo describe como un pack de "29+ skills". Hoy tiene **50 skills**: content-strategy, copywriting, ads, ad-creative, competitors, competitor-profiling, cro, lead-magnets, social, marketing-plan, marketing-psychology, etc. Otra alternativa es `alirezarezvani/claude-skills` (carpeta `marketing-skill`, 49 skills), pero no cuadra con el número 29.
- **Qué es:** un plugin o colección de skills, sin hooks. La carpeta `tools/` trae guías e integraciones (CLIs, Composio) para conectar cuentas de marketing.
- **Instalación:** `npx skills add coreyhaines31/marketingskills` (se puede añadir `--skill cro copywriting` o `-a claude-code`), o `/plugin marketplace add coreyhaines31/marketingskills`.
- **Licencia:** MIT. **Último commit:** 2026-10-08.
- **Riesgos:** bajos para las skills. Las integraciones de `tools/` piden credenciales de terceros, y el README incluye partners patrocinados (por ejemplo Converly).
- **Relevancia: alta.** Es el pack más alineado con Ceos: copywriting, anuncios, CRO de landings, lead magnets y estrategia de contenido.

## 15a. Pack de 12 skills (director de contenido, landing pages, planificador de campañas, consultor de crecimiento…)
- **No encontrado en GitHub.** Lo más parecido es un ZIP descargable de una newsletter ("12 AI employees for Claude", theaileverage.beehiiv.com), con "Chief Content Officer", "Marketing Campaign Planner", "Landing Page CRO Expert", "CEO Advisor"… No está en un repo verificable y no lo he descargado.
- **Relevancia:** no evaluable. Si se consigue, hay que revisarlo antes de usarlo, porque viene de una fuente no auditable.

## 15b. 42 skills de diseño en 6 capas (refactoring-ui, web-typography, page-cro, copywriting, qa)
- **No es un único repo.** Parece una **lista recopilada** ("42 Claude Design Skills That Kill AI Slop", de Artem Novitckii, novitckii.com: "6 layers · 42 skills"). No he podido abrir la página: el dominio no resuelve desde aquí. **Sin verificar.**
- Los nombres que cita el reel salen de repos distintos, que sí he verificado:
  - `refactoring-ui` y `web-typography`: https://github.com/wondelai/skills. Son 65 skills basadas en libros, empaquetadas en plugins (`/plugin marketplace add wondelai/skills` y luego `/plugin install ux-design@wondelai-skills`, `marketing-cro@wondelai-skills`…). MIT; último commit 2026-09-10; sin hooks. **Relevancia media-alta** para landings (diseño, tipografía, CRO, StoryBrand, $100M Offers).
  - `page-cro` y `copywriting`: coreyhaines31/marketingskills (punto 14). `page-cro` es el **nombre antiguo** de la skill, renombrada a `cro` en la v2.0.
  - `qa`: probablemente la /qa de gstack (punto 6b).
- Otra colección distinta de 42 skills de diseño es `Owl-Listener/ai-design-skills`, sobre diseño de productos de IA; no la he verificado y no parece la del reel.

---

## Resumen
| # | Elemento | Repo | ¿Seguro? | Hooks/código | Relevancia para Ceos |
|---|---|---|---|---|---|
| 1-2 | ECC | affaan-m/ECC | Sí | Muchos hooks, MCP, npm | Baja-media |
| 3 | Arena | Jakeschincariol/arena-skill | Sí | Script Python local, coste alto | Media |
| 4 | Find Skills | vercel-labs/skills | Probable | CLI npx con telemetría | Media |
| 5 | prompt-audit | Integrado en Claude Code 2.1.283 | Sí | No | Alta |
| 6a | Superpowers | obra/superpowers | Sí | 1 hook SessionStart | Baja-media |
| 6b | gstack | garrytan/gstack | Sí | setup compila y descarga Chromium; telemetría opt-in | Baja-media |
| 6c | Claude Code Setup | anthropics/claude-plugins-official | Sí | No | Media |
| 6d | Skills oficiales | anthropics/skills | Sí | Scripts Python | Media-alta |
| 7 | Ruflo | ruvnet/ruflo | Sí | Hooks con npx @latest, MCP, daemon | Baja |
| 8 | The Agency | msitarzewski/agency-agents | Sí | No (solo .md) | Alta |
| 9 | Agent Skills | addyosmani/agent-skills | Probable | Mínimo | Baja |
| 10 | Autoresearch | zircote/autoresearch o uditgoenka/autoresearch | Dudoso | uditgoenka: muchos hooks | Media |
| 11 | Prompt Master | nidhinjs/prompt-master | Sí | No | Media |
| 12 | LLM Council | karpathy/llm-council | Sí | App web + OpenRouter | Baja |
| 13 | Spec Kit | github/spec-kit | Sí | CLI Python | Baja |
| 14 | Marketing 29 skills | coreyhaines31/marketingskills | Probable | No | Alta |
| 15a | Pack 12 skills | No encontrado (ZIP de newsletter) | – | – | – |
| 15b | 42 skills de diseño | Lista recopilada; piezas en wondelai/skills, coreyhaines31, gstack | Parcial | No | Media-alta |
