# Escenario de Make "Venta kit"

Diseño para montar en Make. No está creado todavía: nada de este documento se ha ejecutado contra Make, Stripe ni Meta.

## Datos fijos

| Dato | Valor |
|---|---|
| Organización Make | zona **eu2**, team **922922** |
| Conexión Gmail | "Gmail Ceos (Claude)", id **14652169** (growthceos@gmail.com). Envía entregas, avisos y alertas |
| Conexión Google Sheets | "Sheets Ceos (Claude)", id **14652170**. Registro de ventas |
| Conexión Stripe | **No existe.** Ver "Disparador" (Hugo decide entre crearla o usar webhook propio) |
| Moneda | EUR |
| Variables del escenario (Make > Scenario > Custom variables, o un módulo "Set multiple variables" al principio) | `STRIPE_WHSEC`, `STRIPE_RK` (clave restringida de solo lectura), `PRICE_KIT`, `PRICE_EXTRA`, `PRICE_AUDITORIA`, `PIXEL_ID`, `CAPI_TOKEN`, `CAPI_TEST_CODE` (vacío en producción), `URL_KIT`, `URL_EXTRA`, `URL_FORM_AUDITORIA`, `SHEET_ID` |

Las claves se guardan solo en Make. Nunca en el repositorio ni en este documento.

### Cambio de stack respecto al PLAN (10-10-2026)

Para arrancar sin cuentas nuevas, los emails salen por **Gmail** (conexión ya creada) y el registro va a **Google Sheets**, en vez de Brevo y un data store.

- **Límite de Gmail.** Una cuenta @gmail.com puede enviar unos **500 emails al día** (cifra publicada por Google para cuentas personales; puede ser menor en cuentas nuevas o si hay rebotes). Cada venta gasta 1 email de entrega y luego 2 de seguimiento (día 2 y día 5). Con la campaña de 24 €/día no se llega ni de lejos.
- **Cuándo pasar a Brevo:** si se superan **150 envíos/día** de forma sostenida (30 % del límite, margen para soporte), o si las entregas empiezan a caer en spam. Brevo gratis da 300/día y permite enviar desde el dominio .es con SPF/DKIM. El cambio es sustituir los módulos "Gmail > Send an email" por "Brevo > Send a transactional email" con los mismos textos.
- **Remitente:** `Hugo · Ceos Growth <growthceos@gmail.com>`. Cuando exista el dominio, conviene un buzón `soporte@dominio.es`; no se pueden enviar emails "desde" un dominio propio por la conexión de Gmail gratuita sin configurar alias, así que hasta entonces todo sale y se responde desde growthceos@gmail.com.

## Esquema

```
[1 Webhook Stripe] → [2 Comprobar firma] → [3 Parse JSON] → [4 Filtro: checkout.session.completed y paid]
 → [5 Sheets: ¿ya procesada?] → [6 Filtro: no existe] → [7 HTTP: leer sesión de Stripe con line_items]
 → [8 Variables calculadas] → [9 Router]
      ├─ Ruta A "kit"        → [A1 Gmail entrega kit]
      ├─ Ruta B "kit+extra"  → [B1 Gmail entrega kit+extra]
      └─ Ruta C "auditoría"  → [C1 Sheets: auditorías esta semana] → [C2 Gmail confirmación o lista de espera]
 → (las tres rutas siguen, cada una con su copia de) 
   [S1 Sheets: añadir fila de venta] → [S2 HubSpot: crear/actualizar contacto] → [S3 HTTP: Meta Conversions API]
```

En Make un router no "vuelve a juntar" las rutas. Para no triplicar módulos: las rutas A, B y C solo contienen el email distinto; el resto (S1-S3) va **antes** del router, ordenado así: 5 → 6 → 7 → 8 → S1 → 9 (router con emails) y, en una segunda rama del mismo router con filtro "siempre", S2 → S3. Orden exacto en "Módulos" abajo. Lo importante: **la entrega del producto nunca espera a HubSpot ni a Meta**, y un fallo de esos dos no bloquea la entrega.

## Disparador (módulo 1) y verificación de firma

No hay conexión de Stripe en Make. Dos opciones; **recomendada la B** porque no exige dar a Make una clave de escritura de Stripe:

**A. Conexión de Stripe en Make (la crea Hugo).** Módulo "Stripe > Watch events" instantáneo, evento `checkout.session.completed`. Make registra el webhook en Stripe y lo autentica. Necesita una clave de API de Stripe con permiso de escritura en webhooks. Si se elige esta, se saltan los módulos 2 y 3.

**B. Webhook personalizado con verificación de firma (recomendado).**

1. **Webhooks > Custom webhook** "stripe-venta-kit".
   - Opciones avanzadas: **Get request headers = Sí**, **JSON pass-through = Sí** (hace falta el cuerpo exacto, sin reformatear, para calcular la firma).
   - En Stripe (Hugo): Developers > Webhooks > Add endpoint con la URL del webhook de Make, eventos: `checkout.session.completed`, `charge.refunded`, `charge.dispute.created`. Copiar el "Signing secret" (`whsec_...`) a `STRIPE_WHSEC`.
2. **Tools > Set multiple variables** "firma":
   - `sig_header` = valor de la cabecera `stripe-signature` (en Make sale en el array `headers`; `get(map(1.headers; "value"; "name"; "stripe-signature"); 1)`)
   - `t` = el número tras `t=` (`replace(sig_header; /^.*t=(\d+).*$/; $1)`)
   - `v1` = la firma tras `v1=` (`replace(sig_header; /^.*v1=([a-f0-9]+).*$/; $1)`)
   - `esperada` = `sha256(t + "." + 1.value; "hex"; STRIPE_WHSEC)` (HMAC-SHA256 con el secreto completo, incluido `whsec_`)
   - **Filtro de salida:** `esperada` = `v1` **y** `timestamp - t` ≤ 300 (5 min de tolerancia, como recomienda Stripe). Si no se cumple, la ejecución se para sin hacer nada (Make ya ha respondido 200 a quien llamó, así que un atacante no aprende nada).
   - Si Stripe envía varias `v1` (al rotar el secreto), la expresión coge la última; durante una rotación, comparar con las dos.
3. **JSON > Parse JSON** sobre `1.value` (estructura de datos "evento Stripe": `id`, `type`, `created`, `data.object`).
4. **Filtro:** `type` = `checkout.session.completed` **y** `data.object.payment_status` = `paid`. Los eventos `charge.refunded` y `charge.dispute.created` van por otra ruta (ver "Escenarios hermanos").

La verificación tiene un segundo cerrojo: el módulo 7 vuelve a leer la sesión desde la API de Stripe con nuestra clave. Aunque alguien falsificara una firma, sin una sesión real y pagada en nuestra cuenta no pasa.

## Módulos

### 5. Google Sheets > Search rows (idempotencia)
Hoja `ventas-negocio-digital`, pestaña `ventas`, buscar `session_id` = `3.data.object.id`. Stripe reintenta webhooks si no recibe 2xx a tiempo; sin esto se mandaría el kit dos veces.

### 6. Filtro: total de filas encontradas = 0
Si ya existe, la ejecución termina sin hacer nada.

### 7. HTTP > Make a request (leer la sesión)
- GET `https://api.stripe.com/v1/checkout/sessions/{{3.data.object.id}}?expand[]=line_items&expand[]=payment_intent.latest_charge.balance_transaction`
- Cabecera `Authorization: Bearer {{STRIPE_RK}}`. Clave restringida con lectura de Checkout Sessions, Payment Intents, Charges y Balance transactions. Nada de escritura.
- Parse response = Sí.
- Si devuelve error o `payment_status` ≠ `paid`, se para (y avisa, ver Errores).

### 8. Tools > Set multiple variables (cálculos)
| Variable | Fórmula | Nota |
|---|---|---|
| `tiene_kit` | `contains(map(7.data.line_items.data; "price.id"); PRICE_KIT)` | |
| `tiene_extra` | `contains(map(...); PRICE_EXTRA)` | |
| `tiene_auditoria` | `contains(map(...); PRICE_AUDITORIA)` | |
| `producto` | `auditoria` si `tiene_auditoria`; si no, `kit+extra` si `tiene_extra`; si no, `kit` | Valor para el router, la hoja y HubSpot |
| `total` | `7.data.amount_total / 100` | Con IVA, en euros |
| `base` | `round(total / 1,21; 2)` | Sin IVA. Si se activa Stripe Tax, usar `(amount_total - total_details.amount_tax)/100` |
| `iva` | `total - base` | |
| `comision_stripe` | `7.data.payment_intent.latest_charge.balance_transaction.fee / 100` | Comisión real, no la estimada del PLAN |
| `email` | `lower(trim(7.data.customer_details.email))` | |
| `telefono` | `7.data.customer_details.phone` | Solo si el Payment Link pide teléfono (recomendado: opcional) |
| `ph_norm` | `replace(telefono; /[^0-9]/g; "")`; si tiene 9 cifras, anteponer `34` | Formato Meta: solo dígitos con prefijo de país |
| `ref` | `7.data.client_reference_id` | Lo pone la landing (ver "UTM") |
| `utm_*`, `fbc`, `fbp`, `ip`, `ua` | Buscar `ref` en la pestaña `visitas` de la misma hoja | Ver "UTM y datos del navegador" |
| `event_time` | `3.created` | Momento del pago, en segundos Unix |

Si `map()` con clave anidada no funciona en la versión de Make, usar un Iterator sobre `line_items.data` + Array aggregator. Comprobar al montarlo.

### S1. Google Sheets > Add a row (registro de ventas)
Hoja `ventas-negocio-digital` (en Drive de growthceos@gmail.com), pestaña `ventas`:

| Columna | Valor |
|---|---|
| fecha | `formatDate(event_time; "YYYY-MM-DD HH:mm"; "Europe/Madrid")` |
| session_id | id de la sesión |
| producto | `kit` / `kit+extra` / `auditoria` |
| extra | `sí` / `no` |
| importe_total | `total` |
| base | `base` |
| iva | `iva` |
| comision_stripe | `comision_stripe` |
| neto | `base - comision_stripe` |
| utm_source, utm_medium, utm_campaign, utm_content | de `visitas`; vacío si no hay |
| estado | `pagada` (el escenario de reembolsos lo cambia a `reembolsada`) |
| entrega | `pendiente` → el módulo de email lo actualiza a `enviada` |

No se guarda el email del comprador en la hoja: está en Stripe y HubSpot. Así la hoja se puede compartir con el gestor sin datos personales.

Pestaña `resumen` (fórmulas, la monta Claude):
- **Facturado acumulado de la rama** = `SUMA(base)` de filas `pagada`. Umbral de revisión de sociedad: **20.000 €** (el PLAN dice "facturados"; se cuenta base imponible, sin IVA, que es lo que suma en la contabilidad. Confirmar el criterio con el gestor). Celda en rojo al pasar de 18.000 €.
- **Ventas por día y por `utm_campaign`**, % de compradores con extra, % de auditorías, % de reembolsos.
- **Coste por venta** = gasto de Meta del día (lo copia Claude desde Windsor en la pestaña `gasto`, ver `soporte-diario.md`) / ventas del día.

### 9. Router (emails de entrega)
| Ruta | Filtro | Módulo |
|---|---|---|
| A kit | `producto` = `kit` | Gmail > Send an email: texto "Entrega del kit" de `emails.md`, con `URL_KIT` |
| B kit+extra | `producto` = `kit+extra` | Gmail > Send an email: texto "Entrega kit + extra", con `URL_KIT` y `URL_EXTRA` |
| C auditoría | `producto` = `auditoria` | C1: Sheets > Search rows en `ventas` con producto `auditoria` y fecha en la semana actual (lunes a domingo). C2: Gmail > Send an email con "Confirmación de auditoría" (enlace `URL_FORM_AUDITORIA?ref={{session_id}}`) si van **≤5**; si van más, la variante "lista de espera" del mismo texto y aviso a Hugo |
| D seguimiento | sin filtro (siempre) | S2 y S3 |

Tras cada Gmail: Sheets > Update a row `entrega` = `enviada`.

Los emails del día 2 y día 5 los manda un escenario aparte (ver "Escenarios hermanos").

**Enlaces de descarga:** carpetas de Google Drive en "cualquiera con el enlace puede ver" o una ruta con nombre largo e imposible de adivinar en Cloudflare Pages (`/k/8f3c...`, sin enlazar desde ningún sitio y con `noindex`). Es un producto de 27 €: no merece enlaces firmados que caducan. Si se ve el enlace compartido en algún foro, se cambia la ruta y se reenvía a los compradores.

### S2. HubSpot > Create/Update a contact (por email)
Conexión: la crea Hugo (no existe en Make todavía). Propiedades personalizadas a crear antes en HubSpot:

| Propiedad | Tipo | Valor |
|---|---|---|
| `origen` | Desplegable | `negocio-digital` |
| `producto_comprado` | Casillas múltiples (kit, extra, auditoria) | se **añade** al valor existente (`;` como separador), no se pisa |
| `fecha_ultima_compra` | Fecha | `event_time` |
| `importe_total_compras` | Número | suma al valor anterior (requiere leer antes el contacto: módulo "Search for contacts") |
| `utm_campaign_compra` | Texto | `utm_campaign` |
| lifecyclestage | Estándar | `customer` |
| email, firstname, phone | Estándar | de Stripe (`customer_details.name` partido por el primer espacio) |

Si un contacto ya viene de la agencia con otro `origen`, **no se cambia** el `origen`: se añade solo `producto_comprado`. Así no se mezclan los 17 clientes de la agencia con los compradores del kit.

### S3. HTTP > Make a request (Meta Conversions API)
- POST `https://graph.facebook.com/v21.0/{{PIXEL_ID}}/events`
- Body type: Raw, `application/json`. Payload abajo.
- `PIXEL_ID` y `CAPI_TOKEN` son del **Pixel nuevo** del Business Manager de esta rama, nunca del de la agencia.
- Respuesta esperada: `{"events_received":1,"messages":[],"fbtrace_id":"..."}`. Si `events_received` ≠ 1, se trata como error (ver Errores).

#### Qué valor se envía: **base sin IVA**
`custom_data.value` = `base` (22,31 kit; 36,36 kit+extra; 80,17 auditoría).

Motivo: Meta compara ese valor con el gasto en anuncios, y el gasto que factura Meta a una S.L. española con NIF-IVA va sin IVA (inversión del sujeto pasivo). Si mandáramos 27 €, el retorno que enseña Meta saldría inflado un 21 %, y el IVA no es dinero nuestro. Se descarta enviar el neto tras Stripe porque esa comisión no se conoce en la página de gracias y el Pixel y la API deben mandar lo mismo para deduplicar bien. Las decisiones de corte se toman con la hoja, no con el valor que enseña Meta.

#### Normalización de `em` y `ph`
- `em` = `sha256(lower(trim(email)))` en hex minúsculas.
- `ph` = `sha256(ph_norm)`: solo dígitos, con `34` delante, sin `+` ni espacios. Si no hay teléfono, se omite la clave (no se manda un hash de texto vacío).
- `external_id` = el mismo hash del email, para unir compras repetidas de la misma persona.
- `country` = `sha256("es")`.
- `fn` / `ln` = `sha256(lower(trim(nombre)))` y apellido, solo si Stripe trae nombre.
- `fbc`, `fbp`, `client_ip_address`, `client_user_agent` **van sin hash**.

#### `client_ip_address` y `client_user_agent`
**Stripe no los da** en la Checkout Session. Se recogen en la landing, antes de ir a Stripe (ver abajo). Si no llegan, se omiten; Meta acepta el evento igual, solo baja la calidad de coincidencia.

#### Payload de ejemplo
```json
{
  "data": [
    {
      "event_name": "Purchase",
      "event_time": 1760104800,
      "event_id": "cs_live_a1B2c3D4e5F6g7H8i9J0",
      "action_source": "website",
      "event_source_url": "https://DOMINIO.es/gracias",
      "user_data": {
        "em": ["7b17fb0bd173f625b58636fb796407c22b3d16fc78302d79f0fd30c2fc2fc068"],
        "ph": ["a1f3c8a3d0c4b9a1e5f7d2c6b8e0f4a2c9d1e3f5a7b9c0d2e4f6a8b1c3d5e7f9"],
        "external_id": ["7b17fb0bd173f625b58636fb796407c22b3d16fc78302d79f0fd30c2fc2fc068"],
        "country": ["c0bc1e08f9743b2d50d5f1607503bf4e849af0e729fca896515bea955d70a33e"],
        "client_ip_address": "88.12.34.56",
        "client_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 350.0",
        "fbc": "fb.1.1760104512000.IwAR2xYzEjEmPlO",
        "fbp": "fb.1.1760104500000.1234567890"
      },
      "custom_data": {
        "value": 36.36,
        "currency": "EUR",
        "content_ids": ["kit-primera-campana", "extra-temporada-whatsapp"],
        "content_type": "product",
        "num_items": 2,
        "order_id": "cs_live_a1B2c3D4e5F6g7H8i9J0"
      }
    }
  ],
  "access_token": "{{CAPI_TOKEN}}",
  "test_event_code": "{{CAPI_TEST_CODE}}"
}
```
Los hashes de `em`, `ph` y `external_id` son ilustrativos; el de `country` sí es el SHA-256 real de `es`. En producción se quita `test_event_code` (o se manda vacío solo si la API lo acepta; más seguro quitar la clave con un filtro de dos módulos HTTP o un `if` que construya el JSON sin ella).

#### Deduplicación con el Pixel
- El Payment Link redirige tras pagar a `https://DOMINIO.es/gracias?sid={CHECKOUT_SESSION_ID}` (Stripe sustituye esa etiqueta).
- La página de gracias lanza `fbq('track', 'Purchase', {value: 22.31, currency: 'EUR'}, {eventID: sid})`.
- Mismo `event_name` y mismo `event_id` → Meta cuenta una compra.
- La página de gracias no sabe si se cogió el extra, así que manda el valor del kit. Si Meta se queda con el evento del navegador, el valor del extra se pierde en Meta. Aceptado: el valor real está en la hoja.

## UTM y datos del navegador

Un Payment Link no deja meter metadata distinta por visita. Solución:

1. Los anuncios llevan en "Parámetros de URL": `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`.
2. La landing, al pulsar "Comprar", genera `ref` (16 caracteres aleatorios, letras y números), y:
   - abre el Payment Link con `?client_reference_id={ref}` (Stripe solo admite letras, números, `-` y `_`, máx. 200);
   - hace `navigator.sendBeacon` a un segundo webhook de Make, "visita-checkout", con `{ref, utm_source, utm_medium, utm_campaign, utm_content, fbc, fbp, user_agent}`. Ese escenario (2 módulos) añade una fila en la pestaña `visitas` con la IP que llegue en la cabecera `x-forwarded-for` (si Make la expone; comprobar al montar, si no, se omite).
3. El módulo 8 busca `ref` en `visitas`. Las filas de `visitas` sin compra se borran a los 7 días (escenario semanal), porque contienen IP.
4. Si Stripe ya guarda en la sesión las UTM del enlace (algunas cuentas lo muestran en el panel), leerlas de ahí y dejar `visitas` solo para IP, user agent, `fbc` y `fbp`.

Esto se declara en la política de privacidad y en el banner de cookies (las cookies `_fbp`/`_fbc` y el beacon solo se activan si el visitante acepta cookies de marketing).

## Gestión de errores

| Módulo | Si falla | Manejo en Make |
|---|---|---|
| 7 Stripe API | No se sabe qué entregar | **Break** con 3 reintentos cada 10 min. Ejecuciones incompletas activadas. |
| Gmail de entrega (A1, B1, C2) | El cliente pagó y no tiene el producto: lo más grave | **Break** con 3 reintentos cada 15 min. Si se agotan: ruta de error con Gmail a Hugo, asunto `[URGENTE] Entrega fallida {{session_id}}`, y fila con `entrega` = `fallida`. Hugo reenvía a mano con la plantilla. |
| S1 Sheets | Se pierde el control de cifras, no la entrega | **Break** con 3 reintentos; la entrega ya salió. |
| S2 HubSpot | Sin daño al cliente | **Resume** (sigue) + fila en pestaña `errores` de la hoja |
| S3 Conversions API | Meta pierde una compra (el Pixel la puede tener) | 1 reintento con **Break**; luego **Ignore** + fila en `errores` |

- Si falla el propio Gmail (conexión caída, límite diario alcanzado), el aviso a Hugo tampoco saldría por Gmail. Por eso: **activar en Make la notificación por email de errores y ejecuciones incompletas** (Make la manda desde sus servidores a la dirección del usuario de Make) y que Claude revise `errores` y la columna `entrega` cada día (`soporte-diario.md`).
- Configuración del escenario: "Allow storing of incomplete executions" = Sí; "Sequential processing" = Sí (evita dos ejecuciones con la misma sesión a la vez).
- Respuesta a Stripe: el webhook de Make responde 200 en cuanto encola la petición (no se usa módulo Webhook response). Por eso los reintentos los hace Make, no Stripe, y el módulo 5 cubre los reenvíos manuales desde el panel de Stripe.

## Escenarios hermanos (mismo webhook o pequeños aparte)

1. **Reembolsos** (`charge.refunded`): buscar la fila por `payment_intent`, `estado` = `reembolsada`; Conversions API no tiene evento de reembolso útil, no se manda nada a Meta.
2. **Disputas** (`charge.dispute.created`): Gmail a Hugo inmediato, asunto `[DISPUTA] {{importe}} €`, y fila en pestaña `disputas`. Claude prepara las pruebas al día siguiente.
3. **Seguimiento día 2 y día 5**: programado cada día a las 10:00 (Europe/Madrid). Busca en `ventas` filas `pagada`, producto kit o kit+extra, con fecha = hoy-2 o hoy-5, y columna `seg_d2`/`seg_d5` vacía. Lee el email del comprador en Stripe (GET sesión), envía el texto correspondiente de `emails.md` y marca la columna. No se manda si la venta está reembolsada o si el comprador respondió pidiendo no recibir más (Claude añade su email a la pestaña `bajas`).
4. **Formulario de auditoría**: ver `formulario-auditoria.md`.
5. **Visita-checkout**: el beacon de la landing.

## Consumo de operaciones

Plan gratis de Make: 1.000 operaciones al mes. Una venta usa unas 12-14 (webhook, firma, parse, búsqueda, Stripe, variables, hoja ×2, router, Gmail, HubSpot ×2, Meta) más 2 de la visita y unas 4 de seguimiento. Con unas 20 operaciones por venta, el plan gratis aguanta **unas 45 ventas al mes** contando visitas sin compra. Al pasar de 30 ventas en un mes, pasar al plan Core (no incluido en los 200 €; avisar a Hugo antes).
