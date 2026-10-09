---
name: comenta-palabra-boveda
description: Diseñar y montar la mecánica "Comenta PALABRA y te lo mando por privado" con una bóveda de recursos, el motor de comentarios y leads de @revolutia.ai. Usar cuando Hugo quiera activarla, al preparar un recurso descargable o al montar la respuesta automática por mensaje privado en Make.
---

# "Comenta PALABRA" + bóveda de recursos

**Estado: propuesta. No se usa en las piezas de valor de Ceos hasta que Hugo lo apruebe y la entrega automática funcione.** Prometer un envío que no llega quema la cuenta.

## Por qué
En 460 publicaciones de @revolutia.ai:
- Reels con "Comenta PALABRA": mediana de 12.293 views y **124 comentarios**.
- Reels con "Síguenos": mediana de 5.465 views y **1 comentario**.
- Picos: 15.366, 10.970 y 8.550 comentarios en reels con palabra.
Cada comentario es una persona que pide algo: es un formulario de Meta Ads, pero orgánico y gratis.

## Reglas que salen de sus datos
1. **La palabra = el nombre de lo que regalas**, ligada al tema: CRM 561, GODMODE 1.874, EMPLEO 727. Una palabra en mayúsculas. Nunca números (caída de 5–6 veces).
2. **Regalo concreto y tangible**: "el enlace y los dos comandos", "la checklist completa", "el guion". El cierre corto con entregable concreto supera al largo de "comunidad todas las semanas": 35 mil views y 270 comentarios de mediana frente a 22 mil y 225.
3. **Formato del cierre**: "Comenta FORMULARIO y te mando la plantilla de las 3 preguntas por privado 👇". Una línea.
4. **Pregunta + palabra** dio su récord de comentarios de agosto a octubre: "¿Tú te fiarías…? Comenta FORECAST…" → 5.129.
5. Los comentarios de las republicaciones casi no cuentan: se concentran en la primera publicación.

## La bóveda de Ceos (qué meter)
Recursos reales, hechos por Ceos, sin cifras inventadas. Uno por pieza:
- Plantilla de formulario de Meta que filtra curiosos.
- Guion de la primera llamada a un lead en menos de 5 minutos.
- Checklist de la landing antes de lanzar anuncios.
- Mensajes de WhatsApp de bienvenida y de seguimiento para leads que no contestan.
- Calculadora de lo que cuesta montar el sistema por tu cuenta (32.900 €/año).
Se guardan en el repo (`boveda/<palabra>.pdf` o una página) con URL pública.

## Montaje técnico (en Make, cuando Hugo lo apruebe)
1. Escenario nuevo con el disparador de comentarios de Instagram: módulo `instagram-business` → `NewComment` ("Watch events"), conexión 14651824, cuenta 17841469551116816. Comprobar antes con `app-module_get` qué campos devuelve.
2. Filtro: el texto del comentario contiene la palabra activa (tabla palabra → URL del recurso en un data store).
3. Respuesta pública corta al comentario (`CreateComment`): "¡Te lo mando por privado!".
4. Mensaje privado con el enlace. Comprobar si la conexión tiene permiso de mensajes (`instagram_manage_messages`); si no, hace falta reconectar o usar una herramienta de DM como ManyChat.
5. Guardar cada persona en el CRM como lead orgánico (nombre de usuario, palabra, fecha).
6. Probar con una cuenta propia antes de usarlo en una pieza.

Hasta que los pasos 1–6 funcionen, las piezas de valor siguen con su cierre actual + una pregunta concreta.
