---
name: captacion-whatsapp-prospeccion
description: Flujos de captación de Ceos aprendidos de @revolutia.ai - respuesta a leads por WhatsApp en segundos, ficha de lead, seguimiento de los que no contestan, reactivación de contactos antiguos y prospección de nuevos clientes para la agencia. Usar al diseñar o mejorar el seguimiento de leads, el WhatsApp de un cliente o la búsqueda de clientes para Ceos.
---

# Captación, WhatsApp y prospección

## 1. Lead de Meta → WhatsApp en segundos
El flujo que enseñan como "agente de ventas en WhatsApp":
1. Entra el lead (nombre, email, teléfono).
2. **Mensaje de bienvenida por WhatsApp en segundos**, no en horas.
3. El lead puede contestar con texto, audio o una captura.
4. Se clasifica la consulta: duda de atención o intención de compra.
5. Responde con la personalidad configurada para ese cliente.
6. Si hay intención de compra, cualifica (2–3 preguntas) y manda el enlace para agendar la llamada.
Su argumento: "La mayoría sigue perdiendo leads por tardar horas en responder".

Herramientas que muestran (decidir con Hugo antes de usar ninguna):
- **WhatsApp Business MCP oficial de Meta** (lanzado el 15-09-2026): Claude da de alta el número, lo conecta a la API oficial, prueba el webhook y crea las plantillas; si Meta rechaza una, la corrige y la reenvía. Es lo más seguro para clientes.
- n8n o Make con un proveedor oficial (YCloud).
- OpenWA (no oficial, autoalojado): **riesgo de bloqueo del número**. Solo para pruebas internas, nunca con números de clientes.

## 2. Ficha de lead en 4 campos
Para cada lead o prospecto: **perfil**, **dolor**, **oportunidad**, **ángulo de contacto**. Es el formato que usan para entregar "15 leads listos". Úsalo en el CRM y antes de cada llamada.

## 3. Seguimiento de los que no contestan
- Cada semana revisa las propuestas o leads sin respuesta y prepara un seguimiento personalizado para cada uno (no una plantilla genérica), listo para revisar y mandar.
- Si se automatiza, que reenvíe solo lo ignorado y con un límite de intentos.

## 4. Reactivar contactos antiguos
Exporta los contactos (CRM, WhatsApp o LinkedIn: ajustes, privacidad de datos, descargar copia) y pregunta a Claude: "¿Quién puede abrirme una puerta? ¿Quién ya respondió antes? ¿Con quién tengo más contexto para retomar?".

## 5. Prospección de clientes para Ceos
El flujo de "un solo prompt" que enseñan:
1. Elegir ubicación y tipo de negocio ("constructoras en Valencia").
2. Buscar negocios con ese filtro (Google Maps, directorios).
3. Elegir los que tienen buenas reseñas pero captación floja (sin anuncios activos, web mediocre, sin formulario).
4. Auditar su embudo con la skill `auditar-anuncio-landing`.
5. Preparar una demo concreta (un anuncio de ejemplo, una landing de muestra).
6. Mensaje con el problema, la oportunidad y la demo.
El ejemplo de prompt que usan: "Encuéntrame 5 agencias inmobiliarias en Valencia con menos de 20 empleados y el email directo del dueño".

**Límites legales en España**: los emails o mensajes comerciales en frío automatizados chocan con RGPD y LSSI. Úsalo para investigar y preparar; el primer contacto, personal y a empresas, con base legal clara. Nada de envíos masivos sin consentimiento.

## 6. Seguridad
Las automatizaciones con gasto (Meta Ads, generación de vídeo, envíos de WhatsApp) llevan límite de gasto y confirmación humana. Enseñan el caso de un agente que lanzó 500 generaciones en lugar de 59 (más de 5.000 $ en una hora).
