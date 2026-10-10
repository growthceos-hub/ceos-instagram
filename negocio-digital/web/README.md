# Web de venta del Kit Primera Campaña

HTML + CSS puro, sin frameworks ni CDNs de JS. Un solo `styles.css`, `cookies.js` (banner, consentimiento de 12 meses y carga del Pixel tras aceptar), `gracias.js` (evento Purchase) y `media.js` (marcadores de medios que faltan). Sin scripts ni estilos en línea, para poder activar la CSP. Tipografías: pila del sistema (no se llama a Google Fonts, por RGPD); si se quiere Bricolage Grotesque + Instrument Sans, descargar los woff2, ponerlos en `media/` y declarar `@font-face` con `font-display:swap` y `<link rel="preload">`.

## Placeholders a sustituir (buscar `{{` en todo el directorio)
| Placeholder | Qué poner |
|---|---|
| `{{STRIPE_LINK}}` | URL del Payment Link de Stripe (todos los botones de compra) |
| `{{AUDITORIA_LINK}}` | Enlace a la página o formulario de la auditoría de 97 € |
| `{{NIF}}` | CIF de CEOS GROWTH, S.L. (aparece en el pie de todas las páginas) |
| `{{EMAIL_SOPORTE}}` | Email único de soporte |
| `{{REGISTRO_MERCANTIL}}` | Datos de inscripción en el Registro Mercantil (aviso-legal.html) |
| `{{DOMINIO}}` | Dominio final sin `https://` (canonical, Open Graph, schema) |
| `{{PIXEL_ID}}` | ID del Pixel nuevo de Meta, solo en `cookies.js` |

Con sed: `grep -rl '{{NIF}}' . | xargs sed -i 's/{{NIF}}/B12345678/g'`. Ojo: en `mailto:` el placeholder funciona igual.

## Archivos de medios que faltan (los pone Hugo o Claude)
- `media/hugo-30s.mp4` y `media/hugo-poster.jpg` (vídeo 9:16 de 30 s). Si el mp4 falta, se ve el aviso de vídeo no cargado. `media/hugo-30s.es.vtt` y la transcripción ya están: si Hugo cambia el guion, actualizar ambos.
- `media/kit-1.jpg`, `kit-2.jpg`, `kit-3.jpg` (4:3, capturas reales). Sin ellas se ve "Imagen del kit (pendiente)"; no publicar mientras exista ese texto.
- `media/og.jpg` (1200x630) ya generada; `media/logo.png` también.

## Antes de publicar
1. `grep -rn '{{' .` no debe devolver nada (salvo `PIXEL_ID` si aún no hay Pixel, que mantiene el Pixel apagado).
2. `grep -rn 'pendiente' index.html` solo debe mostrar los alt/clases, y en el navegador no debe verse "Imagen del kit (pendiente)".
3. Cabeceras: `_headers` lleva la CSP en modo `Content-Security-Policy-Report-Only`. Tras comprobar en la consola que no bloquea nada, renombrar a `Content-Security-Policy`.
4. `robots.txt` y `sitemap.xml` (solo la portada) usan `{{DOMINIO}}`. Las páginas legales van con `noindex,follow` y `gracias.html` con `noindex,nofollow`.

## Pixel de Meta
- `cookies.js` carga el Pixel solo tras pulsar "Aceptar" y no hace nada mientras `PIXEL_ID` siga siendo el placeholder.
- `gracias.js` valida `session_id` (`^cs_(test|live)_[A-Za-z0-9]{10,200}$`) y manda `Purchase` con `eventID` = session_id, sin importe: el valor lo envía solo el servidor (Conversions API desde Make) y Meta deduplica por `event_id`. Make debe enviar ese mismo `session_id` como `event_id` con `value` y `currency`.
- El consentimiento se guarda con fecha y caduca a los 12 meses.
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
