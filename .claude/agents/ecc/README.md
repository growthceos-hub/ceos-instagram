# Agentes de ECC (Everything Claude Code)

Copiados de https://github.com/affaan-m/ECC (commit 8384d60, licencia MIT en `LICENSE-ECC`). Son 71 (el README de ECC dice 68).
Solo los textos de los agentes: sin hooks, scripts ni MCP del plugin. `docs-lookup` y `gan-evaluator` nombran herramientas MCP (Context7, Playwright MCP) que no están instaladas; funcionan sin ellas con Bash o WebFetch.

## Quién vigila qué en la rama de negocio digital

Toda decisión pasa por el Consejo de 5 asesores (skill `consejo-5-asesores`) **y** por el panel de ECC que toque:

| Decisión | Agentes de ECC |
|---|---|
| Producto, oferta, precio, copy, anuncios, emails | `marketing-agent`, `agent-evaluator` |
| Plan de lanzamiento o de una web nueva | `planner`, `architect`, `gan-planner` |
| Web o landing (antes de publicar) | `seo-specialist`, `a11y-architect`, `performance-optimizer`, `security-reviewer`, `gan-evaluator`, `e2e-runner` |
| Código (Make, scripts, webhooks, JS) | `code-reviewer`, `typescript-reviewer`, `silent-failure-hunter`, `security-reviewer` |
| Datos y automatizaciones | `database-reviewer`, `rag-pipeline-reviewer`, `loop-operator` |
| Calidad de cualquier entregable | `agent-evaluator`, `comment-analyzer`, `doc-updater` |
| Producto de conocimiento por sector | `healthcare-reviewer` (salud) y los revisores de lenguaje si el producto enseña programación |

Los revisores de un lenguaje concreto (Go, Rust, Kotlin, Swift, C++, Java, PHP, Ruby, Dart, Flutter, Django, FastAPI, etc.) se convocan solo si un producto o una web usa ese lenguaje.
