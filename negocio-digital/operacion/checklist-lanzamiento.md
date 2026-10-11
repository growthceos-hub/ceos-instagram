# Checklist antes de gastar 1 € en anuncios

En orden. No se pasa a la siguiente fase con algo pendiente de la anterior, salvo lo marcado como "en paralelo". **[H]** lo hace Hugo (cuentas, claves, firmas, grabación). **[C]** lo hace Claude. **[H+C]** juntos.

Tiempo de Hugo estimado: unas 3 h repartidas, más la grabación de 30 min del PLAN.

## Fase 1. Legal y fiscal
- [ ] [H] Preguntar al gestor: epígrafe de venta de contenidos digitales en CEOS GROWTH, S.L., factura simplificada por venta, criterio para contar los 20.000 € (base o total) y etiqueta contable propia de la rama.
- [ ] [C] Redactar aviso legal (con NIF), condiciones de venta (con art. 103 m y garantía voluntaria de 14 días), privacidad (incluido el texto del formulario de auditoría y el beacon de la landing) y cookies.
- [ ] [H] Revisar y aprobar esos textos (o pasarlos al gestor).
- [ ] [H] Firmar la cesión de imagen propia para los anuncios de esta rama (la redacta Claude).

## Fase 2. Cuentas (todas nuevas, separadas de la agencia)
- [ ] [H] Comprar el dominio .es en DonDominio.
- [ ] [H] Crear Business Manager nuevo, cuenta publicitaria nueva y Pixel nuevo. Método de pago. Verificar el dominio en el Business Manager. Darle a Claude el ID del Pixel.
- [ ] [H] Generar el token de Conversions API del Pixel nuevo (Administrador de eventos > Configuración) y pegarlo solo en Make como `CAPI_TOKEN`.
- [ ] [H] Cuenta de HubSpot: crear o reutilizar la de Ceos; conectar HubSpot en Make.
- [ ] [C] Crear en HubSpot (con aprobación) las propiedades `origen`, `producto_comprado`, `fecha_ultima_compra`, `importe_total_compras`, `utm_campaign_compra`.
- [ ] [H] Conectar en Windsor la cuenta publicitaria nueva (y, si quiere, Stripe) para que Claude lea gasto y compras.
- [ ] [H] Cuenta de Tally para el formulario de auditoría.

## Fase 3. Stripe
- [ ] [H] Etiqueta propia de la rama: cuenta de Stripe separada o, como mínimo, productos con metadata `rama=negocio-digital` y descriptor del extracto reconocible ("CEOS GROWTH KIT").
- [ ] [H] Crear los 3 productos y precios (27 €, 17 €, 97 €, IVA incluido) y darle a Claude los `price_id`.
- [ ] [H] Payment Link del kit con el extra como venta cruzada; Payment Link de la auditoría. En ambos: factura activada, teléfono opcional, casilla obligatoria personalizada con el texto del art. 103 m, redirección tras el pago a `https://DOMINIO.es/gracias?sid={CHECKOUT_SESSION_ID}`.
- [ ] [H] **Conexión de Stripe en Make: no existe todavía.** Elegir:
  - Opción recomendada: webhook personalizado de Make con verificación de firma. Hugo crea el endpoint en Stripe (eventos `checkout.session.completed`, `charge.refunded`, `charge.dispute.created`), pega el `whsec_...` en Make, y crea una **clave restringida de solo lectura** (Checkout Sessions, Payment Intents, Charges, Balance transactions) para `STRIPE_RK`.
  - Alternativa: crear la conexión de Stripe en Make (necesita clave con permiso de escritura en webhooks).
- [ ] [H] Activar notificaciones de disputas de Stripe al email de Hugo.

## Fase 4. Producto y textos (en paralelo con fases 1-3)
- [ ] [C] Cerrar el kit: guía, 30 guiones, 10 plantillas de Canva (comprobar que abren con cuenta gratuita), y el extra.
- [ ] [C] Subir el kit y el extra a sus enlaces de descarga (Drive "cualquiera con el enlace" o ruta oculta en Cloudflare Pages con `noindex`). Probar los enlaces desde una ventana privada y desde el móvil.
- [ ] [C] Emails de `emails.md` revisados con `texto-sin-tono-ia`.
- [ ] [H] Leer los emails y aprobarlos.
- [ ] [C] Formulario de auditoría en Tally según `formulario-auditoria.md` (lo monta Hugo si Tally no tiene acceso para Claude; Claude le da el contenido campo a campo).
- [ ] [C] Plantilla del informe de auditoría en Canva o HTML → PDF, con un informe de EJEMPLO completo hecho sobre la cuenta propia de @ceos.growth.

## Fase 5. Web
- [ ] [C] Landing en Cloudflare Pages (no GitHub Pages): qué se compra enseñado de verdad, quién responde (Hugo, NIF, Burgos), garantía, enlaces legales, banner de cookies que bloquea el Pixel y el beacon hasta aceptar.
- [ ] [C] Script de la landing: captura de UTM, `fbc`/`fbp`, `ref` aleatorio, `client_reference_id` en el Payment Link y beacon al webhook "visita-checkout".
- [ ] [C] Página de gracias con `fbq('track','Purchase', {value:22.31, currency:'EUR'}, {eventID: sid})`.
- [ ] [H] Apuntar el dominio a Cloudflare Pages.
- [ ] [C] Pasar `auditar-anuncio-landing` a la landing y corregir lo que salga.

## Fase 6. Make
Organización en zona eu2, team 922922. Conexiones ya existentes: "Gmail Ceos (Claude)" (id 14652169) para enviar emails y "Sheets Ceos (Claude)" (id 14652170) para el registro.
- [ ] [C] Crear la hoja `ventas-negocio-digital` en el Drive de growthceos@gmail.com con las pestañas `ventas`, `visitas`, `resumen`, `gasto`, `errores`, `disputas`, `auditorias`, `bajas`, y las fórmulas del resumen.
- [ ] [H] Pegar en Make las claves (`STRIPE_WHSEC`, `STRIPE_RK`, `CAPI_TOKEN`). Claude nunca las ve.
- [ ] [C] Montar el escenario "Venta kit" según `make-escenario.md`, **desactivado**, y los hermanos: reembolsos, disputas, seguimiento día 2/5, formulario de auditoría, visita-checkout, borrado de auditorías, limpieza de `visitas`.
- [ ] [C] Gmail como remitente: tener presente el límite de unos 500 envíos al día de una cuenta @gmail.com. Pasar a Brevo (con dominio propio, SPF y DKIM) si se superan 150 envíos al día o las entregas caen en spam.
- [ ] [H] Activar en Make el aviso por email de errores y ejecuciones incompletas.
- [ ] [H] Crear en Gmail la etiqueta `soporte-kit`, el filtro que la pone y la respuesta automática (texto 7 de `emails.md`).

## Fase 7. Compra de prueba (dinero real)
Con `CAPI_TEST_CODE` puesto (Administrador de eventos > Probar eventos) y el escenario activado.
- [ ] [H] Abrir la landing desde el móvil con una URL que imite la de un anuncio:
  `https://DOMINIO.es/?utm_source=meta&utm_medium=paid&utm_campaign=PRUEBA&utm_content=prueba-1&fbclid=PRUEBA123`
- [ ] [H] Aceptar cookies, comprar el **kit + extra** (44 €) con su tarjeta, marcando la casilla del art. 103 m.
- [ ] [C] Comprobar, en este orden:
  1. Email de entrega recibido en menos de 2 min, con los dos enlaces y que abren.
  2. Factura de Stripe recibida.
  3. Fila en `ventas`: producto `kit+extra`, total 44, base 36,36, comisión real de Stripe, `utm_campaign` = `PRUEBA`, `entrega` = `enviada`.
  4. Contacto en HubSpot con `origen` = `negocio-digital` y `producto_comprado` = kit; extra.
  5. En "Probar eventos" de Meta: un evento Purchase del navegador y uno del servidor con el mismo `event_id`, marcados como deduplicados; valor y moneda correctos.
  6. Calidad de coincidencia del evento del servidor (Meta la muestra pasadas unas horas): anotar el valor.
- [ ] [H] Reenviar el mismo evento desde Stripe (Webhooks > Reenviar): comprobar que **no** llega un segundo email (idempotencia).
- [ ] [C] Enviar al webhook una petición con firma falsa: comprobar que se para en el módulo 2.
- [ ] [H] Comprar la **auditoría** (97 €): email de confirmación con el enlace al formulario; rellenar el formulario con capturas de @ceos.growth; aviso a Hugo y fila en `auditorias`.
- [ ] [H] Reembolsar las dos compras en Stripe. [C] Comprobar `estado` = `reembolsada` en la hoja.
- [ ] [C] Forzar un fallo de Gmail (desconectar el módulo en una copia del escenario) y comprobar que llega el aviso de Make a Hugo.
- [ ] [C] Comprobar el seguimiento día 2 adelantando la fecha de la fila de prueba (y que no sale porque está reembolsada; repetir con una fila sin reembolsar a un email de Hugo).
- [ ] [C] Quitar `CAPI_TEST_CODE` y poner el escenario en producción.

## Fase 8. Verificación de atribución Stripe → anuncio
- [ ] [C] En la cuenta publicitaria nueva, plantilla de "Parámetros de URL" de todos los anuncios: `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`. Nombres de campaña y anuncio sin espacios raros (ej. `kit-c1-recorrido`).
- [ ] [C] Configuración de atribución de la campaña: 7 días clic, 1 día visualización; evento de optimización Purchase del Pixel nuevo.
- [ ] [H] Aprobar la campaña antes de activarla.
- [ ] [C] Con la primera venta real que llegue de anuncios: comprobar que la fila tiene `utm_campaign` y `utm_content` del anuncio, y que Meta cuenta la compra el mismo día o el siguiente. Si la venta llega sin UTM o Meta no la ve, **pausar** y revisar antes de seguir gastando. El PLAN exige esta verificación antes de gastar; como no se puede generar un clic de anuncio sin gastar, la prueba de la fase 7 cubre la tubería y esta comprobación se hace con los primeros euros (tope: si a los 24 € no ha habido ninguna venta, se prueba el clic desde la vista previa del anuncio).

## Fase 9. Creativos
- [ ] [H] Grabar el creativo 5 (30 s, móvil) y hacer la captura del 4 (Ads Manager de @ceos.growth). Es lo único que Claude no puede hacer.
- [ ] [C] Producir los creativos 1-5 y pasar `copy-ads-ceos`, `texto-sin-tono-ia` y `auditar-anuncio-landing`. Nada de personas o voces de IA, ni testimonios inventados, ni resultados de clientes de la agencia. Declarar IA si Meta lo pide.
- [ ] [H] Aprobar los creativos.

## Fase 10. Arranque
- [ ] [C] Días 1-2: solo orgánico en @ceos.growth (historias y reel).
- [ ] [C] Primera ejecución de la rutina de `soporte-diario.md` el día 1 y crear `negocio-digital/registro/`.
- [ ] [H] Día 3: activar la campaña (≈24 €/día, 7 días, 170 € en total).
- [ ] [C] Reglas de corte vigiladas cada día desde la rutina.
