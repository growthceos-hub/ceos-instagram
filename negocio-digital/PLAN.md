# Rama de negocio digital de Ceos Growth — plan de arranque

Decidido el 10-10-2026 por el Consejo de 5 asesores (dos sesiones, cada una con 5 revisiones anónimas), con el `marketing-agent` de ECC y una investigación de costes. Debates completos en `consejo/`. Los 71 agentes de ECC vigilan cada decisión según `.claude/agents/ecc/README.md`.

## Reglas de la casa
- **Sin trabajadores.** Claude hace ideas, producto, webs, creativos, anuncios, análisis y posventa. Hugo y su socio son los dueños: dan la cara y aprueban.
- **No se abre una segunda web** hasta que la primera demuestre que un desconocido que llega por anuncio deja más dinero del que cuesta traerlo. El millón al mes sale de repetir ese proceso.
- **La confianza sale de enseñar lo que se compra**, de que el comprador se reconozca en un caso como el suyo y de saber quién responde. Nunca de algo inventado.

## Primer producto
- **"Kit Primera Campaña"**: 30 guiones, 10 plantillas de Canva y una guía para lanzar una campaña de captación con menos de 300 €/mes. Lo escribe Claude en `kit-primera-campana/`.
- **Precio**: 27 € IVA incluido. **Extra al pagar**: 17 € (10 guiones de temporada + 15 mensajes de WhatsApp para responder a los leads). **Siguiente escalón**: auditoría de 97 €.
- **Público**: negocios locales con menos de 300 €/mes de presupuesto, que la agencia no acepta a comisión. No compite con la agencia: la alimenta.
- **Material 100 % propio.** Ningún anuncio, resultado ni dato de clientes de la agencia.

## Creativos (los hace Claude)
| # | Formato | 0-3 s | Prueba | Producción |
|---|---|---|---|---|
| 1 | Vídeo 9:16, 20 s: recorrido del kit | Carpeta abierta + "Esto te llevas por 27 €" | El material real | Exportes de Canva + `render.py` |
| 2 | Vídeo: plantilla rellenada en 60 s | "Tu primer anuncio sin grabarte" | Peluquería marcada EJEMPLO | Canva + time-lapse con `render.py` |
| 3 | Carrusel "Tu anuncio de 5 €/día, corregido en 4 cambios" | Anuncio con tachones rojos, EJEMPLO | El antes y después | Canva |
| 4 | Captura sin pulir del Ads Manager de @ceos.growth (cuenta propia) | Coste por lead real con fecha | Dato real propio | Captura de Hugo (1 min) + anotaciones con `render.py` |
| 5 | Hugo da la cara, 30 s | "Soy Hugo, Ceos Growth, Burgos" | Persona real, NIF, garantía, @ceos.growth | Hugo graba con el móvil; Claude edita con subtítulos |

Se prueba diseño animado frente a capturas sin pulir; no se da por hecho que gana lo "premium".

**Prohibido:** personas o voces generadas con IA, testimonios o reseñas inventados, resultados de clientes de la agencia, promesas de ingresos, usar "lo hizo la IA" como gancho y jerga que el comprador no entiende (bump, CPL, píxel). Si Meta pide declarar contenido generado con IA, se declara.

## Papel de Hugo (mínimo)
- 30 min una sola vez: grabar el creativo 5 y hacer la captura del 4.
- ~10 min al día: aprobar en bloque las respuestas de soporte que redacta Claude.
- 10 min por auditoría: revisarla y firmarla. **Tope: 5 auditorías por semana**; si se pasa, lista de espera.

## Auditoría de 97 €
- Formulario con capturas o exporte de su cuenta. **Nunca se pide acceso a la cuenta del cliente.**
- Casilla de consentimiento RGPD; los datos se borran a los 30 días.
- Claude prepara un PDF de 5 páginas (nota sobre 10, sus cifras, 3 cambios por impacto, 2 anuncios reescritos) y un vídeo de 3 min con anotaciones, sin voz.
- Hugo revisa y firma. Entrega en 72 h laborables. Aviso visible: "Análisis preparado con IA, revisado y firmado por Hugo".
- Garantía: si no hay 3 cambios aplicables, se devuelve el dinero.
- Al final, "¿Te lo hacemos?" → agencia.

## Posventa sin trabajadores
- Un único correo de soporte con respuesta automática y preguntas frecuentes.
- Claude redacta las respuestas una vez al día y Hugo las aprueba. Plazo: 24 h laborables.
- Reembolso sin preguntas durante 14 días. Ante una queja, se devuelve el dinero antes de que abra una disputa.
- Contracargo: Claude prepara las pruebas (factura, email de entrega, casilla del art. 103 m) y Hugo las envía. Si las disputas superan el 0,5 %, se paran los anuncios.
- Si el kit no le funciona al comprador: plantilla de diagnóstico y, después, oferta de auditoría.

## Stack
| Pieza | Herramienta | Coste |
|---|---|---|
| Landing | Cloudflare Pages (GitHub Pages prohíbe tiendas en sus condiciones) | 0 € |
| Dominio | .es en DonDominio | ≈6 €/año |
| Cobro | Stripe Payment Link con venta cruzada + factura | 1,5 % + 0,25 € por venta |
| Entrega | Webhook de Stripe → Make → email con Brevo | 0 € (planes gratis) |
| CRM | HubSpot | 0 € |
| Medición | Make → Conversions API (Purchase con `event_id`, deduplicado con el Pixel de la página de gracias); Windsor lee el coste por compra a diario | 0 € |

## Legal y fiscal
- **Decisión de Hugo (10-10-2026):** es una rama de Ceos Growth y factura CEOS GROWTH, S.L. con la estructura fiscal actual. Al llegar a **20.000 € facturados** en esta rama se revisa si pasa a una sociedad propia. Hasta entonces, sus ingresos y gastos van separados (etiqueta propia en Stripe y en la contabilidad) para medir su rentabilidad y saber cuándo se cruza el umbral.
- Añadir el epígrafe de venta de contenidos digitales si la S.L. no lo tiene, y emitir factura simplificada por venta (confirmar con el gestor).
- Aviso legal con NIF visible, condiciones, privacidad y cookies.
- Casilla obligatoria de entrega inmediata y pérdida del desistimiento (art. 103 m TRLGDCU), más la garantía voluntaria de 14 días.
- Solo España al principio (IVA 21 % en el 303; sin OSS mientras las ventas a particulares del resto de la UE no pasen de 10.000 €/año).
- **Business Manager, cuenta publicitaria y Pixel nuevos**, separados de la agencia, para que un problema aquí no toque a los 17 clientes.
- Cesión de imagen de Hugo para los anuncios de esta rama (firma propia).

## Dinero: 200 €
| Concepto | € |
|---|---|
| Dominio | 6 |
| Herramientas | 0 |
| Meta Ads (≈24 €/día durante 7 días, desde el día 3) | 170 |
| Reserva (reembolsos, cambio de gancho) | 24 |

Días 1-2: solo orgánico (historias y reel en @ceos.growth).

## Economía por venta (IVA y Stripe descontados)
| | Precio | Base | Stripe | Neto |
|---|---|---|---|---|
| Kit | 27 € | 22,31 € | 0,66 € | 21,65 € |
| Extra al pagar | 17 € | 14,05 € | 0,51 € | 13,54 € |
| Auditoría | 97 € | 80,17 € | 1,71 € | 78,46 € |

Supuesto conservador: 15 % coge el extra y 2 % la auditoría → 25,25 € por comprador; con un 5 % de reembolsos, **≈24 €. Coste por venta máximo: 24 €. Objetivo: ≤18 €.** El día 7 se recalcula con los porcentajes reales. Cifras de comisiones e IVA de fuentes de terceros: confirmarlas en Stripe y con el gestor.

## Reglas de corte
- Antes de gastar: compra real de prueba y atribución Stripe → anuncio verificada.
- 60 € gastados sin venta → cambiar el gancho.
- Día 7 con menos de 5 ventas o coste por venta > 24 € → cambiar la oferta, no el nicho.
- Dos ofertas fallidas → parar y guardar el resto.
- Disputas > 0,5 % → parar anuncios.

## Bola de nieve
- ≥10 ventas y coste por venta ≤18 € → el 100 % del neto vuelve a ads; +20 % de presupuesto cada 3 días mientras aguante (Stripe retiene 7-14 días el dinero de cuentas nuevas).
- Segunda web solo con ≥30 ventas/mes y 2 semanas seguidas rentables, clonando el mismo proceso. Desde ahí, el 50 % del beneficio financia el siguiente producto.
- Más adelante (no antes de validar): suscripción mensual de anuncios hechos por Claude, que el Expansionista propuso como el producto de más techo.

## Primer paso
Hugo graba con el móvil sus 30 s: "Soy Hugo, Ceos Growth, Burgos…". Es lo único que Claude no puede producir.
