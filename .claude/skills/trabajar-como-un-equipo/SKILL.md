---
name: trabajar-como-un-equipo
description: Cómo trabaja Claude en las tareas de Ceos para no repetir errores y mejorar cada día - corregir el manual y no el chat, lista de terminado, traspaso entre sesiones, plan antes de construir, diagnóstico con nivel de confianza y revisión por otro agente. Usar en cualquier tarea larga, al crear o corregir una skill o tarea programada, o cuando algo ha salido mal.
---

# Trabajar como un equipo (lo que @revolutia.ai enseña sobre usar Claude, aplicado a mí)

## 1. Cuando algo sale mal, se corrige el manual, no el chat
Su "bucle de delegación" tiene tres piezas por tarea:
- **Manual**: el paso a paso exacto de la tarea (aquí: `toolkit/*.md` y las skills de `.claude/skills/`).
- **Caja de herramientas**: cada plantilla, guion aprobado o archivo bueno se guarda y se enlaza desde el manual, para no construir dos veces lo mismo (aquí: `reels/2026-09-26*/spec.json`, `historias/2026-09-26-serie/`, plantillas).
- **Lista de terminado**: qué tiene que cumplir un trabajo para darlo por bueno, dentro del manual.
Regla: si una tarea falla o Hugo corrige algo, el arreglo va al .md o a la skill correspondiente (con fecha), no solo a la respuesta de ese día. Así la siguiente ejecución ya lo sabe.

## 2. Plan antes de construir
Antes de montar un embudo, una automatización o un escenario de Make: requisitos, piezas, plan y tareas ("primero el mapa, luego la construcción"). Los campos del formulario, las etapas del CRM y los disparadores de WhatsApp, por escrito antes de tocar nada.

## 3. Diagnóstico con nivel de confianza
En análisis de campañas, leads o contenido, marca cada afirmación como:
- **Seguro**: lo dicen los datos.
- **Probable**: es una inferencia.
- **Suposición**: falta información.
La verdad incómoda va en la primera línea, sin "buena pregunta" ni dar la razón por defecto. Para decisiones importantes, la skill `consejo-5-asesores` (es el mismo diseño de "LLM Council" que enseñan con 889 comentarios).

## 4. Que revise otro
"Los modelos son malísimos revisando su propio trabajo". Para piezas importantes (un anuncio, una landing, un cambio en una tarea programada), un subagente distinto revisa contra la lista de terminado antes de publicar.

## 5. Sesiones largas: traspaso limpio
- Si llevas 3 intentos con la misma solución que no funciona, o la sesión es muy larga: escribe `handoff.md` con objetivo, estado actual, archivos, qué ha cambiado, qué se probó y falló, y siguiente paso. Sesión nueva: "Lee el handoff y continúa".
- Si un paso salió mal, vuelve atrás al punto anterior al error y replantea, en lugar de corregir encima: "si solo corriges sobre el error, ese error se queda en el contexto".

## 6. Instrucciones limpias para modelos nuevos ("prompt audit")
Al revisar los .md de instrucciones o una skill, buscar tres cosas que con modelos nuevos empeoran el resultado: instrucciones de doble comprobación, frases en MAYÚSCULAS para dar énfasis y pasos explicados uno a uno que el modelo ya sabe hacer. Proponer los cambios y enseñarlos antes de aplicarlos; las reglas de negocio de Hugo no se tocan sin su OK.

## 7. Criterios en vez de adjetivos
Pedir y escribir siempre con criterio medible, cliente concreto y formato ("que lo entienda en 5 segundos", "3 versiones distintas", "en 3 frases"). Ver `texto-sin-tono-ia`.

## 8. Aprender cada día
La rutina "Estudio diario @revolutia.ai" (08:12) lee lo nuevo de la cuenta y actualiza `toolkit/APRENDIZAJES.md` y estas skills. Cuando una técnica nueva sirva a Ceos, va a la skill que le toca; si cambia el negocio o promete algo al público, va a la sección B de APRENDIZAJES para Hugo.
