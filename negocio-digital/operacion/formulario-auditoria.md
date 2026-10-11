# Formulario e informe de la auditoría de 97 €

## Herramienta

Tally (plan gratis: subida de archivos de hasta 10 MB por archivo) o Google Forms con subida a Drive (exige que el cliente tenga cuenta de Google; peor). Recomendado Tally. Al enviar, webhook de Tally → Make:
1. Comprueba que `ref` (session_id de Stripe) existe en la hoja `ventas` con producto `auditoria` y estado `pagada`. Si no, Gmail a Hugo.
2. Copia los archivos a Drive de growthceos@gmail.com, carpeta `auditorias/AAAA-MM-DD_ref/`.
3. Añade fila en la pestaña `auditorias` de la hoja `ventas-negocio-digital`: `ref`, fecha de recepción, fecha límite (recepción + 72 h laborables, sin contar sábados, domingos ni festivos nacionales), fecha de entrega, fecha de borrado, estado.
4. Gmail a Hugo: "Nueva auditoría {{ref}}, límite {{fecha_limite}}".

La URL del formulario lleva `?ref={{session_id}}` y Tally lo guarda en un campo oculto.

**Nunca se pide acceso a la cuenta publicitaria, contraseñas ni que nos añadan como socio en el Business Manager.** Si alguien lo ofrece, se responde que no hace falta.

## Campos

Aviso arriba del formulario:
> Tardas unos 15 minutos. No te pedimos acceso a tu cuenta: solo capturas o un exporte. Antes de subir capturas, tapa nombres, teléfonos o emails de tus clientes si aparecen.

| # | Campo | Tipo | Obligatorio |
|---|---|---|---|
| 0 | ref | Oculto (de la URL) | Sí |
| 1 | Nombre | Texto | Sí |
| 2 | Email con el que pagaste | Email | Sí |
| 3 | Nombre del negocio | Texto | Sí |
| 4 | Sector | Desplegable: peluquería/barbería, fisioterapia, estética, restaurante, gimnasio, taller, reformas, academia, inmobiliaria, otro | Sí |
| 5 | Ciudad o zona donde trabajas | Texto | Sí |
| 6 | Web o Instagram del negocio | URL | No |
| 7 | ¿Qué quieres conseguir con los anuncios? | Opción: citas/reservas, presupuestos, llamadas, mensajes de WhatsApp, otro | Sí |
| 8 | ¿Qué ofreces en el anuncio? (cópialo tal cual) | Texto largo | Sí |
| 9 | ¿Cuánto gastas al mes en anuncios? | Número (€) | Sí |
| 10 | ¿Cuánto te deja de media un cliente nuevo en su primer año? (aproximado vale) | Número (€) | Sí |
| 11 | ¿A dónde llegan los contactos? | Opción: formulario de Meta, tu web, WhatsApp, Messenger/Instagram, llamada | Sí |
| 12 | ¿Quién contesta a los contactos y cuánto se tarda de media? | Texto corto | Sí |
| 13 | De cada 10 contactos, ¿cuántos acaban viniendo o comprando? | Número 0-10 | No |
| 14 | ¿Qué has probado ya y qué pasó? | Texto largo | No |
| 15 | Captura del Administrador de anuncios, nivel campaña, últimos 30 días, con columnas: entrega, presupuesto, importe gastado, resultados, coste por resultado, alcance, frecuencia, impresiones, CTR (todos), CPM | Archivo (imagen/PDF) | Sí, o el 16 |
| 16 | Exporte de los últimos 30 días a nivel anuncio (Informes > Exportar > .csv o .xlsx) con esas mismas columnas | Archivo (.csv/.xlsx) | Sí, o el 15 |
| 17 | Capturas de los anuncios activos (imagen o primer fotograma + texto) o enlace a la Biblioteca de anuncios de tu página | Archivos / URL | Sí |
| 18 | Captura de la segmentación del conjunto de anuncios (ubicación, edad, públicos) | Archivo | Sí |
| 19 | Captura del formulario instantáneo o de la página a la que lleva el anuncio | Archivo / URL | Sí |
| 20 | ¿Algo más que debamos saber? | Texto largo | No |
| 21 | Casilla RGPD | Casilla | Sí |

Al lado de los campos 15-19 va un enlace "Cómo hacer esta captura" con una imagen de EJEMPLO de la cuenta propia de @ceos.growth (nunca de un cliente de la agencia).

## Casilla RGPD (texto completo)

> ☐ He leído y acepto el tratamiento de mis datos para hacer la auditoría.
>
> **Responsable:** CEOS GROWTH, S.L., NIF [NIF], [dirección], Burgos. Contacto: growthceos@gmail.com.
> **Finalidad:** analizar los datos y capturas que envías para preparar tu auditoría de anuncios, entregártela y atender tus consultas sobre ella.
> **Base legal:** la ejecución del contrato de la auditoría que has comprado.
> **Qué datos:** los que escribes en este formulario y los que aparezcan en tus capturas y exportes. Te pedimos que tapes los datos de tus propios clientes; si aparece alguno, no lo usamos y se borra con el resto.
> **Quién más los trata:** proveedores que nos prestan el servicio y actúan por cuenta nuestra: Tally (formulario), Google (correo y almacenamiento), Make (automatización) y Anthropic (el modelo de IA con el que preparamos el análisis, que luego revisa y firma una persona). Algunos están en EE. UU.; las transferencias se amparan en el Marco de Privacidad de Datos UE-EE. UU. o en cláusulas contractuales tipo. No cedemos tus datos a nadie más ni los usamos para entrenar modelos.
> **Decisiones automatizadas:** ninguna. La IA prepara un borrador; el informe lo revisa y firma una persona.
> **Cuánto tiempo:** las capturas, exportes y respuestas de este formulario se borran **30 días después de entregarte la auditoría**. El informe se conserva el mismo plazo. Tu nombre, email y la factura se guardan lo que exige la ley fiscal y mercantil (hasta 6 años).
> **Tus derechos:** acceso, rectificación, supresión, oposición, limitación y portabilidad, escribiendo a growthceos@gmail.com. Si crees que no los respetamos, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).
> Más información en la política de privacidad: [URL_PRIVACIDAD].

[Revisar con el gestor o asesor legal antes de publicar: dirección, NIF y que la política de privacidad general dice lo mismo. Comprobar en la configuración de la cuenta de Anthropic/Claude que los datos no se usan para entrenar.]

## Borrado a 30 días

- La pestaña `auditorias` tiene `fecha_borrado` = fecha de entrega + 30 días.
- Escenario de Make "Borrado auditorías", diario a las 03:00: para cada fila con `fecha_borrado` ≤ hoy y estado ≠ `borrada`, mueve la carpeta de Drive a la papelera y la vacía (Drive API: delete permanente), borra el envío en Tally (API de Tally) y pone `estado` = `borrada` con la fecha.
- Los adjuntos que lleguen por Gmail de soporte relacionados con una auditoría se borran a mano el mismo día (Claude lo apunta en el registro diario; Hugo lo confirma).
- Claude no guarda copias en el repositorio. Si trabaja con los archivos en local, lo hace en el scratchpad de la sesión y lo borra al terminar.
- Si no llega el formulario en 30 días desde el pago, Claude redacta un recordatorio; a los 60 días, se ofrece reembolso.

## Plantilla del informe (PDF, 5 páginas)

Cabecera de todas las páginas: "Auditoría de anuncios · {{negocio}} · {{fecha}}". Pie: "Análisis preparado con IA, revisado y firmado por Hugo, Ceos Growth".

### Página 1. Tu nota y lo esencial
- Nota sobre 10, grande, con la tabla de los 7 criterios y su puntuación.
- Tres frases: qué está bien, qué está frenando más, qué cambiar primero.
- Fecha de los datos analizados ("últimos 30 días hasta el {{fecha}}, según tus capturas").

### Página 2. Tus cifras
- Tabla con sus datos tal cual: gasto, resultados, coste por resultado, CTR, CPM, frecuencia, alcance.
- Su cálculo: valor de un cliente (campo 10) × tasa de cierre (campo 13) = cuánto puede pagar como máximo por un contacto. Comparado con lo que paga.
- Sin comparaciones con "la media del sector" salvo que haya fuente pública citada. Nunca datos de clientes de la agencia.
- Si falta un dato, se dice "no lo tenemos" y se explica qué supone.

### Página 3. Los 3 cambios, por impacto
Para cada uno:
- Qué cambiar, en una frase que se pueda hacer sin ayuda.
- Por qué, señalando la cifra o captura en la que se ve.
- Cómo comprobar en 7 días si ha funcionado (qué número mirar).
- Esfuerzo: 10 min / 1 h / medio día.

Orden: primero el que más puede mover el coste por contacto o la conversión a cliente, con el esfuerzo como desempate. Garantía: si no hay 3 cambios aplicables, se devuelve el dinero; si Claude no encuentra 3 de verdad, se dice a Hugo antes de inventar uno de relleno.

### Página 4. 2 anuncios reescritos
- Sus 2 anuncios con más gasto: original a la izquierda, reescrito a la derecha (gancho de los 3 primeros segundos, texto principal, titular, llamada a la acción).
- Si son vídeos: guion nuevo de 20-30 s para grabar con el móvil, con el formato de los guiones del kit.
- Pasada de `texto-sin-tono-ia` y de `auditar-anuncio-landing` sobre los reescritos.

### Página 5. Plan de 7 días y siguiente paso
- Día a día qué hacer con los 3 cambios y cuándo mirar las cifras.
- Reglas de corte sencillas para su caso (cuánto gastar sin resultados antes de cambiar el gancho).
- "¿Te lo hacemos?": un párrafo sobre la agencia, sin presión, con enlace para una llamada. Solo si su presupuesto encaja con lo que acepta la agencia; si no, se omite y se le remite al kit.
- Firma de Hugo y fecha.

### Vídeo de 3 minutos
Grabación de pantalla sobre sus capturas, sin voz, con anotaciones (flechas, recuadros y textos) en el orden del informe: nota, cifras, cambio 1, 2 y 3, anuncios reescritos. Se monta con `render.py`.

### Criterios de la nota sobre 10

| Criterio | Peso | 0 | Mitad | Máximo |
|---|---|---|---|---|
| 1. Oferta | 2 | Genérica ("conócenos", "pide información") | Concreta pero sin precio o condición clara | Concreta, con precio o condición y un motivo para pedirla ya (las 3 comprobaciones de la guía 1.1) |
| 2. Gancho y creativos | 2 | Sin gancho en los 3 primeros segundos, o imagen de banco | Gancho presente pero genérico, una sola variante | Gancho que nombra al cliente o su problema, ≥2 variantes distintas en prueba |
| 3. Destino del clic | 1,5 | Lleva a la portada de una web o a un perfil | Formulario o página correctos con fricción (muchos campos, carga lenta) | Formulario instantáneo o página con una sola acción, coherente con el anuncio |
| 4. Respuesta a los contactos | 1,5 | Más de 24 h o sin sistema | En el día | En menos de 5 min con mensaje preparado y seguimiento si no contesta |
| 5. Estructura y segmentación | 1 | Muchos conjuntos con poco presupuesto cada uno, públicos muy cerrados | Estructura razonable con algún solapamiento | Una campaña, un conjunto, zona bien puesta, presupuesto que deja salir de aprendizaje |
| 6. Números de negocio | 1 | No sabe cuánto puede pagar por un contacto | Lo sabe a ojo | Lo calcula y el coste actual está por debajo |
| 7. Medición | 1 | No sabe cuántos contactos acaban en cliente | Lo apunta a veces | Apunta cada contacto y su resultado |
| **Total** | **10** | | | |

Puntuación por criterio en pasos de 0,5. Se redondea el total a una cifra decimal. La justificación de cada puntuación va en una línea en la tabla de la página 1, siempre señalando una captura o un dato del formulario. Si no hay datos para un criterio, se puntúa con la mitad y se marca "sin datos".
