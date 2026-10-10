# Web de venta del Kit Primera Campaña

HTML + CSS puro, sin frameworks ni CDNs de JS. Un solo `styles.css` y un `cookies.js` de 1 KB (banner y carga del Pixel tras aceptar). Tipografías: pila del sistema (no se llama a Google Fonts, por RGPD); si se quiere Bricolage Grotesque + Instrument Sans, descargar los woff2, ponerlos en `media/` y declarar `@font-face` con `font-display:swap` y `<link rel="preload">`.

## Placeholders a sustituir (buscar `{{` en todo el directorio)
| Placeholder | Qué poner |
|---|---|
| `{{STRIPE_LINK}}` | URL del Payment Link de Stripe (todos los botones de compra) |
| `{{AUDITORIA_LINK}}` | Enlace a la página o formulario de la auditoría de 97 € |
| `{{NIF}}` | CIF de CEOS GROWTH, S.L. (aparece en el pie de todas las páginas) |
| `{{EMAIL_SOPORTE}}` | Email único de soporte |
| `{{REGISTRO_MERCANTIL}}` | Datos de inscripción en el Registro Mercantil (aviso-legal.html) |
| `{{DOMINIO}}` | Dominio final sin `https://` (canonical, Open Graph, schema) |
| `{{PIXEL_ID}}` | ID del Pixel nuevo de Meta, en `cookies.js` y en el bloque comentado de `gracias.html` |

Con sed: `grep -rl '{{NIF}}' . | xargs sed -i 's/{{NIF}}/B12345678/g'`. Ojo: en `mailto:` el placeholder funciona igual.

## Archivos de medios que faltan (los pone Hugo o Claude)
- `media/hugo-30s.mp4` y `media/hugo-poster.jpg` (vídeo vertical 9:16 de 30 s y su fotograma). Mientras no existan se ve un texto de aviso.
- `media/kit-1.jpg`, `kit-2.jpg`, `kit-3.jpg` (4:3, capturas reales del kit: un guion, una plantilla, una página de la guía). Sin ellas se ve un hueco punteado.
- `media/og.jpg` (1200x630) para Open Graph.
- `media/logo.png` ya está (256 px, copiado de `toolkit/logo.png`; sirve de favicon).

## Pixel de Meta
- `cookies.js` carga el Pixel solo tras pulsar "Aceptar" y no hace nada mientras `PIXEL_ID` siga siendo el placeholder.
- `gracias.html` tiene un bloque `<script>` comentado con `fbq('init')` y `Purchase` con `eventID` = parámetro `session_id` de la URL. Descomentarlo al tener ID. Make debe enviar a la Conversions API ese mismo `session_id` como `event_id` para deduplicar.
- Pendiente de revisar con el gestor/DPO: la API de conversiones envía el email con hash; la política de privacidad la declara bajo consentimiento, así que Make solo debería enviarla si hubo consentimiento (o cambiar el texto).

## Desplegar en Cloudflare Pages
1. Subir el repo a GitHub.
2. Cloudflare Pages > Create project > conectar el repo.
3. Framework preset: None. Build command: vacío. **Build output directory: `negocio-digital/web`**.
4. Custom domain: el .es de DonDominio, y comprobar que `{{DOMINIO}}` coincide.

## Configurar en Stripe (Payment Link del kit de 27 €)
- **Casilla de términos obligatoria**: Payment Link > Opciones > "Recopilar el consentimiento de los clientes" > Términos de servicio, y usar un texto propio en "Texto personalizado" o en el campo de consentimiento: "Acepto la entrega inmediata del contenido digital y reconozco que pierdo mi derecho de desistimiento (art. 103.m TRLGDCU). Conozco la garantía de 14 días." Enlazar `condiciones.html` como URL de términos. Guardar esta evidencia para posibles contracargos.
- **Venta cruzada de 17 €**: crear el producto "Extra: 10 guiones de temporada + 15 mensajes de WhatsApp" a 17 € (IVA incluido) y añadirlo en "Añadir venta cruzada" (order bump) del Payment Link.
- **URL de éxito**: tras el pago, redirigir a `https://{{DOMINIO}}/gracias.html?session_id={CHECKOUT_SESSION_ID}` (Payment Link > Después del pago > Redirigir a tu sitio web).
- **Factura automática**: activar "Crear factura" en el Payment Link, con datos de CEOS GROWTH, S.L. y NIF. Impuestos: IVA 21 % incluido en el precio. Etiqueta/metadatos propios para separar esta rama contablemente.
- Recoger dirección de facturación y activar el recibo por email.

## Pendientes legales
Los textos legales son una base razonable, no asesoramiento. Revisarlos con el gestor: epígrafe de venta de contenidos digitales, plazos de conservación y condiciones de la auditoría, que tendrá sus propias condiciones.
