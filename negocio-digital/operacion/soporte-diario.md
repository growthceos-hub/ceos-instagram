# Rutina diaria de soporte y control (Claude)

Cada día laborable a las **08:45** (Europe/Madrid), como tarea programada. Duración objetivo: menos de 20 min de Claude y **unos 10 min de Hugo**. Resultado: un archivo `negocio-digital/registro/AAAA-MM-DD.md` y borradores en Gmail listos para que Hugo los envíe.

Claude **no envía** emails a compradores, **no reembolsa** y **no toca** campañas sin aprobación de Hugo. Lee, redacta y propone.

## Herramientas

| Qué | Cómo | Si no está conectado |
|---|---|---|
| Buzón de soporte | Gmail MCP sobre growthceos@gmail.com | Parar y avisar en el registro |
| Ventas, entregas, errores, disputas | Hoja `ventas-negocio-digital` (pestañas `ventas`, `errores`, `disputas`, `auditorias`, `bajas`) por Google Drive MCP | Leerlas por la API de Make (data store no aplica) |
| Disputas y reembolsos en Stripe | Pestaña `disputas` (la alimenta el webhook `charge.dispute.created`) y, como segunda fuente, el conector `stripe` de Windsor si Hugo lo conecta | Pedir a Hugo una captura de Stripe > Disputas |
| Gasto y compras de Meta | Windsor, conector `facebook`, cuenta publicitaria **nueva** de esta rama | Pedir a Hugo una captura del Administrador de anuncios |

## Pasos

### 1. Leer el buzón
- Búsqueda: `label:soporte-kit newer_than:3d -label:soporte-respondido` (la etiqueta `soporte-kit` la pone un filtro de Gmail a todo lo que llega a growthceos@gmail.com con "kit", "descarga", "factura", "reembolso", "auditoría" o desde un remitente que esté en Stripe; lo que no encaje, Claude lo revisa igualmente en `in:inbox newer_than:1d`).
- Leer el hilo completo de cada uno, no solo el último mensaje.
- Clasificar: `descarga`, `factura`, `reembolso`, `no-funciona`, `duda-uso`, `auditoria`, `baja`, `queja`, `disputa`, `otro`.
- Prioridad alta (va arriba en la lista de Hugo): `reembolso`, `queja`, `disputa`, cualquier mención de banco o contracargo, y lo que lleve más de 16 h laborables sin respuesta (el plazo es 24 h).

### 2. Redactar borradores
- Con `create_draft` como respuesta en el mismo hilo, usando las plantillas de `emails.md` (8 reembolso, 9 diagnóstico) y la guía del kit para dudas de uso.
- Pasada de `texto-sin-tono-ia` a cada borrador.
- Nunca prometer resultados, plazos de leads ni cifras. Nunca citar datos de clientes de la agencia.
- `baja`: añadir el email a la pestaña `bajas` (Claude lo propone, Hugo lo aprueba con el lote) y borrador de confirmación de una línea.
- `descarga`: comprobar en `ventas` que la sesión existe y su columna `entrega`; si fue `fallida`, el borrador lleva los enlaces.
- Si un caso no encaja en ninguna plantilla o es delicado (amenaza, datos de salud, menores, algo legal), no se redacta respuesta: se marca "Hugo decide".

### 3. Lista para Hugo (aprobar en bloque)
En el registro del día, una tabla numerada:

| # | Prioridad | Remitente | Tipo | Resumen (1 línea) | Acción propuesta | Borrador |
|---|---|---|---|---|---|---|

Hugo contesta en el chat con "ok todo", "ok menos 3 y 5", o cambios por número. Con su ok:
- Claude envía los borradores aprobados (o Hugo los envía desde Gmail, según prefiera; por defecto, Hugo pulsa enviar, que son 10 clics).
- Hugo hace los reembolsos aprobados en Stripe.
- Claude pone la etiqueta `soporte-respondido`.

### 4. Comprobaciones del sistema
- `ventas`: filas de ayer con `entrega` ≠ `enviada` → prioridad alta en la lista.
- `errores`: filas nuevas de Conversions API o HubSpot → anotar; si hay más de 2 seguidas del mismo módulo, revisar la conexión.
- Make: ejecuciones incompletas del escenario "Venta kit" (si Hugo da acceso de lectura a Make; si no, lo mira él en 1 min).
- `auditorias`: las que vencen hoy o mañana, y las pendientes de borrado.
- Seguimiento día 2/día 5: que se enviaron los de ayer.

### 5. Disputas en Stripe
- Leer `disputas` y, si está conectado, Windsor `stripe`.
- Tasa = disputas abiertas en los últimos 30 días / ventas de los últimos 30 días.
- Por cada disputa nueva, preparar en `negocio-digital/registro/disputas/{{id}}.md` (sin datos de tarjeta): factura, email de entrega con fecha y hora (de Gmail "Enviados"), captura de la casilla del art. 103 m del checkout, IP o fecha de descarga si existe, y la conversación de soporte si la hubo. Hugo la envía desde Stripe.

### 6. Coste por compra (Windsor)
- `get_data` con conector `facebook`, cuenta de esta rama, fecha ayer y acumulado desde el inicio, campos: `date`, `campaign`, `ad_name`, `spend`, compras (`actions_purchase` u `offsite_conversion.fb_pixel_purchase`; comprobar el nombre exacto con `get_fields` la primera vez y apuntarlo aquí).
- Copiar el gasto por día a la pestaña `gasto` de la hoja.
- Calcular dos costes por venta y anotar los dos:
  - **Según Meta** = gasto / compras atribuidas por Meta.
  - **Según Stripe** = gasto / ventas reales de la hoja con `utm_source=meta` (más ventas sin UTM aparte, que pueden venir de orgánico).
  - Si se separan más de un 30 %, avisar: la atribución está fallando o hay mucha venta orgánica.
- Para las reglas de corte se usa el **coste por venta según Stripe** (dinero real). Meta sirve para comparar anuncios entre sí.

### 7. Reglas de corte (del PLAN)
Comprobar cada día y escribir el resultado en el registro, con una de estas tres palabras: **SEGUIR**, **CAMBIAR** o **PARAR**.

| Regla | Condición | Acción propuesta |
|---|---|---|
| Antes de gastar | Compra de prueba y atribución verificadas (`checklist-lanzamiento.md`) | Si no, PARAR: no se lanza |
| Gancho | 60 € gastados en total (o desde el último cambio de gancho) sin ninguna venta | CAMBIAR el gancho: proponer 3 ganchos nuevos de los creativos del PLAN |
| Día 7 | < 5 ventas o coste por venta > 24 € | CAMBIAR la oferta (no el nicho) y recalcular con los porcentajes reales de extra, auditoría y reembolso |
| Ofertas | Dos ofertas fallidas | PARAR y guardar el resto del presupuesto |
| Disputas | > 0,5 % | PARAR anuncios ese mismo día (Hugo los pausa) |
| Bola de nieve | ≥ 10 ventas y coste por venta ≤ 18 € | Proponer +20 % de presupuesto (máximo cada 3 días), recordando que Stripe puede retener 7-14 días el dinero |
| Umbral fiscal | Facturado acumulado (base) ≥ 18.000 € | Avisar a Hugo para hablar con el gestor antes de los 20.000 € |

Con pocas ventas, una disputa ya supera el 0,5 %: con 1 disputa y menos de 200 ventas, se aplica la regla igual y se avisa a Hugo para que decida con contexto.

Claude **propone**; Hugo aprueba cualquier cambio de anuncios o presupuesto.

### 8. Registro del día
Crear `negocio-digital/registro/AAAA-MM-DD.md` con esta plantilla y no tocar los de días anteriores:

```markdown
# Registro AAAA-MM-DD

## Decisión de hoy: SEGUIR / CAMBIAR / PARAR
Motivo en una línea.

## Cifras
| | Ayer | Acumulado |
|---|---|---|
| Ventas (Stripe) | | |
| De ellas con extra | | |
| Auditorías | | |
| Reembolsos | | |
| Gasto Meta | | |
| Coste por venta (Stripe) | | |
| Coste por venta (Meta) | | |
| Facturado rama (base) | | / 20.000 € |
| Disputas (30 días) | | % |

## Para Hugo (aprobar en bloque)
| # | Prioridad | Remitente | Tipo | Resumen | Acción propuesta | Borrador |

## Sistema
- Entregas fallidas:
- Errores Make / CAPI / HubSpot:
- Auditorías que vencen:
- Borrados pendientes:

## Notas
Lo que haya que recordar mañana.
```

Al terminar, una línea a Hugo (en el chat de la tarea) con la decisión del día y el número de cosas que tiene que aprobar.
