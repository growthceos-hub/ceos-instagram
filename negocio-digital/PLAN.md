# Rama de negocio digital de Ceos — plan de arranque

Decidido el 10-10-2026 por el Consejo de 5 asesores, con 5 revisiones anónimas, el agente `marketing-agent` de ECC y una investigación de costes. Debate completo en `consejo/2026-10-10-primer-producto.md`.

## Regla de oro
No se abre una segunda web hasta que la primera demuestre que **un desconocido que llega por anuncio deja más dinero del que cuesta traerlo**. El millón al mes sale de repetir ese proceso, no de lanzar muchas webs a la vez.

## Primer producto
- **"Kit Primera Campaña"**: 30 guiones, 10 plantillas de Canva y una guía para lanzar una campaña de captación con menos de 300 €/mes.
- **Precio**: 27 € IVA incluido. **Order bump**: 17 € (10 guiones extra + mensajes de WhatsApp para responder a los leads). **Siguiente escalón**: auditoría grabada de la cuenta, 97 €.
- **Público**: negocios locales con menos de 300 €/mes de presupuesto, que la agencia no acepta a comisión. No compite con la agencia: la alimenta (los que piden "házmelo" y encajan pasan a la agencia).
- **Material**: 100 % propio, grabado con la actriz. Ningún anuncio ni dato de clientes. Testimonios solo con permiso escrito.

## Confianza (lo que vende)
Cara de la actriz y firma de Hugo, "+17 clientes activos, agencia en Burgos" con enlace a @ceos.growth, pruebas solo con permiso, garantía voluntaria de 14 días, aviso legal con NIF visible.

Landing en 8 bloques: portada con vídeo de 30 s y botón · problema · quiénes somos (estudio, equipo) · qué incluye · cómo se usa en 3 pasos · pruebas · garantía y FAQ (factura, entrega, IVA) · cierre con el order bump.

## Stack
| Pieza | Herramienta | Coste |
|---|---|---|
| Landing | Cloudflare Pages (GitHub Pages prohíbe tiendas en sus condiciones) | 0 € |
| Dominio | .es en DonDominio | ≈6 €/año |
| Cobro | Stripe Payment Link con cross-sell + factura | 1,5 % + 0,25 € por venta |
| Entrega | Webhook de Stripe → Make → email con Brevo (Drive o Notion) | 0 € (planes gratis) |
| CRM | HubSpot | 0 € |
| Medición | Make → Conversions API (Purchase con `event_id`, deduplicado con el Pixel en la página de gracias); Windsor lee el coste por compra a diario | 0 € |

## Legal mínimo
- Factura la S.L. actual, con el epígrafe de venta de contenidos digitales y factura simplificada por venta (confirmar con el gestor).
- Aviso legal, condiciones, privacidad y cookies.
- Casilla obligatoria de entrega inmediata y pérdida del desistimiento (art. 103 m TRLGDCU).
- Solo España al principio (IVA 21 % en el 303; sin OSS mientras las ventas a particulares del resto de la UE no pasen de 10.000 €/año).
- **Business Manager y cuenta publicitaria nuevos**, separados de los 17 clientes.
- Cesión de imagen de la actriz para este producto, firmada antes de publicar.

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
| Order bump | 17 € | 14,05 € | 0,51 € | 13,54 € |
| Auditoría | 97 € | 80,17 € | 1,71 € | 78,46 € |

Con un 30 % de bump y un 5 % de auditorías, cada comprador deja ≈29,60 €; con un 5 % de reembolsos, ≈28 €. **Coste por venta máximo: 28 €. Objetivo: ≤22 €.** En frío lo normal al empezar son 25-50 €, por eso el bump y la auditoría son obligatorios.

Cifras de comisiones e IVA sacadas de fuentes de terceros: confirmarlas en Stripe y con el gestor.

## Reglas de corte
- 60 € gastados sin venta → cambiar el gancho.
- Día 7 con menos de 5 ventas o coste por venta > 28 € → cambiar la oferta, no el nicho.
- Dos ofertas fallidas → parar y guardar el resto.

## Bola de nieve
- ≥10 ventas y coste por venta ≤22 € → el 100 % del neto vuelve a ads; +20 % de presupuesto cada 3 días mientras aguante (Stripe retiene 7-14 días el dinero de cuentas nuevas).
- Segunda web solo con ≥30 ventas/mes y 2 semanas seguidas rentables, clonando el mismo proceso. Desde ahí, el 50 % del beneficio financia el siguiente producto.

## Primer paso
Compra real de 27 € + bump y comprobar 4 cosas: llega la factura, llega el email de entrega, el contacto entra en HubSpot y el Purchase aparece deduplicado en Meta. Hasta entonces, 0 € en ads.
