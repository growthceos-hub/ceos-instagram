# -*- coding: utf-8 -*-
"""Contenido de los 6 recursos de la bóveda de Ceos Growth.

Reglas: español de España, sin cifras ni casos inventados. Cualquier número de
ejemplo va marcado como EJEMPLO. Los corchetes [así] son huecos para rellenar.
"""

import re
import sys

sys.path.insert(0, "/home/user/ceos-negocio-digital/web/lib")


def ganchos_de_seo():
    """Lee los 36 ganchos y la guía de grabación de seo.ts (fuente única)."""
    src = open("/home/user/ceos-negocio-digital/web/lib/seo.ts", encoding="utf-8").read()
    bloque = src.split("export const GANCHOS")[1].split("export const ECOSISTEMA")[0]
    cats = []
    for m in re.finditer(r'categoria: "([^"]+)",\s*uso: "([^"]+)",\s*items: \[(.*?)\],\s*\}', bloque, re.S):
        items = re.findall(r'"([^"]+)"', m.group(3))
        cats.append((m.group(1), m.group(2), items))
    guia_src = src.split("export const GUIA")[1].split("export const GANCHOS")[0]
    guia = re.findall(r'paso: "([^"]+)", detalle: "([^"]+)", error: "([^"]+)"', guia_src)
    return cats, guia


def ejemplo(txt="EJEMPLO"):
    return f'<span class="ej">{txt}</span>'


def say(txt):
    return f'<div class="say">«{txt}»</div>'


# ---------------------------------------------------------------- FORMULARIO

def tabla_preguntas(filas):
    out = ['<table class="t q"><thead><tr><th style="width:31%">Pregunta</th><th style="width:31%">Opciones</th><th>Qué hacer con la respuesta</th></tr></thead><tbody>']
    for preg, opciones, accion in filas:
        ops = "".join(f"<li>{o}</li>" for o in opciones)
        out.append(f"<tr><td><b>{preg}</b></td><td><ul class='ops'>{ops}</ul></td><td>{accion}</td></tr>")
    out.append("</tbody></table>")
    return "".join(out)


V, A, R = '<i class="dot v"></i>', '<i class="dot a"></i>', '<i class="dot r"></i>'

FORMULARIO = dict(
    palabra="FORMULARIO",
    titulo='El formulario de Meta que <em>filtra curiosos</em>',
    subtitulo="Las preguntas exactas para constructoras y casas modulares, software, formación online y negocio local. Y qué hacer con cada respuesta.",
    dentro=["Cómo configurar el formulario antes de escribir una sola pregunta",
            "El semáforo: a quién llamar ya, a quién hoy y a quién no",
            "Preguntas por nicho con sus opciones de respuesta",
            "Los fallos que llenan el CRM de gente que no compra"],
    paginas=[
        f'''
<div class="kicker">Antes de las preguntas</div>
<h2>Configúralo así o las preguntas no sirven</h2>
<p class="lead">Un buen formulario hace que el curioso se vaya solo y que el comprador llegue a la llamada con la mitad de la conversación hecha. Y para eso no hace falta pedir más datos.</p>
<div class="grid2">
  <div class="card"><div class="n">01</div><h3>Elige «Mayor intención»</h3><p>En el tipo de formulario de Meta, marca <b>Mayor intención</b> y no «Más volumen». Añade una pantalla en la que la persona revisa sus datos antes de enviar. Entran menos leads, pero son personas que saben lo que han pedido.</p></div>
  <div class="card"><div class="n">02</div><h3>Di el precio en la introducción</h3><p>Aunque sea «desde [tu precio de entrada]». Si tu servicio es caro, quien no puede pagarlo se va en la primera pantalla y no te hace perder una llamada.</p></div>
  <div class="card"><div class="n">03</div><h3>Opción múltiple, no texto libre</h3><p>Las preguntas abiertas se dejan en blanco o se contestan con un punto. Con opciones cerradas puedes ordenar los leads de un vistazo. Como mucho, una pregunta abierta.</p></div>
  <div class="card"><div class="n">04</div><h3>De 3 a 4 preguntas que filtran</h3><p>Más el nombre y el teléfono prellenados. Cada pregunta tiene que cambiar lo que haces después. Si una respuesta no cambia nada, la pregunta sobra.</p></div>
  <div class="card"><div class="n">05</div><h3>Incluye siempre una respuesta de salida</h3><p>Opciones como «Solo estoy mirando» o «Ahora mismo no puedo invertir». Si no existen, el curioso marca cualquier cosa y no lo distingues.</p></div>
  <div class="card"><div class="n">06</div><h3>Promete en la pantalla final lo que vas a cumplir</h3><p>«Te llamamos en los próximos minutos desde el [teléfono]» solo si de verdad vas a hacerlo. Si no, «hoy antes de las [hora]». Así coge el teléfono.</p></div>
</div>
<div class="kicker" style="margin-top:7mm">El semáforo</div>
<h2 class="sm">Cada lead sale del formulario con un color</h2>
<div class="sema">
  <div>{V}<b>Verde</b><p>Encaja en plazo, dinero y zona. Llamada en menos de 5 minutos con el guion completo.</p></div>
  <div>{A}<b>Ámbar</b><p>Le falta una pieza (terreno, financiación, decisión). Llamada hoy, más corta, para ver si esa pieza llega.</p></div>
  <div>{R}<b>Rojo</b><p>Solo mira o no puede ahora. Nada de llamada: WhatsApp con un recurso útil y recordatorio en el CRM a 30 o 60 días.</p></div>
</div>
''',
        f'''
<div class="kicker">Nicho 1</div>
<h2>Constructoras y casas modulares</h2>
<p class="lead">Aquí el filtro es el terreno, el plazo y cómo se paga. Sin esas tres cosas, la casa no se construye este año, por muchas ganas que tenga.</p>
{tabla_preguntas([
    ("¿Tienes ya terreno?", ["Sí, en propiedad", "Estoy cerrando la compra", "Todavía no", "Quiero reformar o ampliar mi casa"],
     f"{V} En propiedad: verde.<br>{A} Cerrando compra: pregunta en la llamada la fecha de firma.<br>{R} Sin terreno: manda tu guía para elegir parcela y apunta seguimiento a 60 días.<br>Reforma: deriva si no la haces."),
    ("¿Cuándo te gustaría empezar la obra?", ["En los próximos 3 meses", "Entre 3 y 6 meses", "Entre 6 y 12 meses", "Más adelante, estoy mirando"],
     f"{V} Hasta 6 meses: llamada ya.<br>{A} 6 a 12 meses: llamada hoy y visita cuando tenga licencia a la vista.<br>{R} «Estoy mirando»: contenido y recordatorio."),
    ("¿Cómo piensas pagarla?", ["Con fondos propios", "Hipoteca ya aprobada", "Necesito hipoteca, aún no la he pedido", "No lo sé todavía"],
     f"{V} Propios o aprobada: verde.<br>{A} Sin pedir: si trabajas con un intermediario hipotecario, ofrécelo en la llamada.<br>{R} «No lo sé» + sin terreno: rojo."),
    ("¿Qué presupuesto manejas?", ["Menos de [tu precio de entrada]", "Entre [entrada] y [precio medio]", "Más de [precio medio]", "Prefiero que me orientéis"],
     "Pon tus rangos reales. Por debajo de tu precio de entrada: rojo con educación (explica qué se puede hacer con ese dinero). «Orientadme» no es malo: suele ser alguien que aún no ha pedido presupuestos."),
])}
<div class="note"><b>Pregunta extra si construyes solo en ciertas zonas:</b> «¿En qué provincia está el terreno?» con tus provincias como opciones y una última «Otra». Fuera de zona: rojo, sin llamada.</div>
<div class="kicker" style="margin-top:7mm">Texto para la pantalla de introducción</div>
<div class="say">Construimos casas [modulares] en [zonas] desde [tu precio de entrada], llave en mano. Antes de llamarte te hacemos 4 preguntas rápidas para ver si tu proyecto encaja y no hacerte perder el tiempo.</div>
<p class="small">Precio, zona y un motivo honesto para las preguntas. Quien no encaja se va aquí, y quien sigue ya sabe de qué va la llamada.</p>
''',
        f'''
<div class="kicker">Nicho 2</div>
<h2>Software (B2B)</h2>
<p class="lead">El filtro es quién decide, cuántas personas lo usarían y qué tienen ahora. Quien compite con una hoja de Excel se vende distinto que quien viene de un competidor.</p>
{tabla_preguntas([
    ("¿Cuál es tu puesto?", ["Dueño o gerente", "Responsable de área", "Empleado", "Freelance o estudiante"],
     f"{V} Dueño o responsable: demo.<br>{A} Empleado: en la llamada pregunta quién decide y pide que esté en la demo.<br>{R} Estudiante: prueba gratis o contenido, sin comercial."),
    ("¿Cuántas personas lo usarían?", ["Solo yo", "De 2 a 10", "De 11 a 50", "Más de 50"],
     "Ajusta los tramos a tus planes de precio. El tramo te dice qué plan enseñar en la demo y quién la hace."),
    ("¿Cómo lo hacéis ahora?", ["Con Excel u hojas de cálculo", "Con otra herramienta", "A mano o en papel", "No lo hacemos todavía"],
     "Otra herramienta: prepara la comparación honesta antes de llamar.<br>Excel o papel: en la demo enseña el ahorro de tiempo con su caso.<br>«No lo hacemos»: hay que vender el problema antes que el producto."),
    ("¿Cuándo queréis tenerlo funcionando?", ["Este mes", "Este trimestre", "Este año", "Solo estoy investigando"],
     f"{V} Este mes o trimestre: demo esta semana.<br>{R} Investigando: prueba gratis y secuencia de emails."),
])}
<div class="kicker" style="margin-top:6mm">Nicho 3</div>
<h2 class="sm">Formación online</h2>
{tabla_preguntas([
    ("¿Qué te describe mejor ahora mismo?", ["[Situación de tu alumno ideal]", "[Situación 2]", "Estoy empezando de cero", "Solo quiero ver el contenido gratis"],
     "Escribe las situaciones con las palabras de tus alumnos. La última opción es la salida del curioso: mándale el contenido gratis y no lo llames."),
    ("Si el programa encaja contigo, ¿puedes invertir en él ahora?", ["Sí, tengo el dinero apartado", "Sí, si se puede pagar a plazos", "Ahora mismo no"],
     f"{V} Apartado: llamada ya.<br>{A} A plazos: llamada hoy, explica las cuotas.<br>{R} «Ahora no»: producto de entrada barato o lista de espera."),
    ("¿Cuántas horas a la semana puedes dedicarle?", ["Menos de 3", "Entre 3 y 6", "Más de 6"],
     "Ajusta a lo que exige tu programa. Si exige más de lo que tiene, díselo en la llamada: un alumno que abandona no recomienda."),
])}
''',
        f'''
<div class="kicker">Nicho 4</div>
<h2>Negocio local</h2>
<p class="lead">Clínicas, reformas, gimnasios, academias, talleres. Aquí el filtro es la zona y la urgencia. El precio suele importar menos que la distancia.</p>
{tabla_preguntas([
    ("¿Qué servicio te interesa?", ["[Servicio 1]", "[Servicio 2]", "[Servicio 3]", "Aún no lo sé"],
     "Manda cada servicio a la persona que lo lleva. «Aún no lo sé»: llamada corta de orientación, no de venta."),
    ("¿Estás en [zona que cubres]?", ["Sí, en [ciudad]", "En la provincia, cerca", "No, estoy más lejos"],
     f"{V} Ciudad o cerca: verde.<br>{R} Lejos: mensaje amable y fuera. No gastes una llamada en alguien que no va a venir."),
    ("¿Para cuándo lo necesitas?", ["Esta semana", "Este mes", "Solo quiero saber precios"],
     f"{V} Esta semana: llama y ofrece hueco concreto.<br>{A} Este mes: llamada hoy.<br>{R} Precios: mándalos por WhatsApp con un enlace para reservar."),
    ("¿Cómo prefieres que te contactemos?", ["Llamada", "WhatsApp", "Me da igual"],
     "Respétalo. Quien elige WhatsApp y recibe una llamada suele no cogerla. Usa los mensajes del recurso SEGUIMIENTO."),
])}
<div class="kicker" style="margin-top:7mm">Los fallos que llenan el CRM de gente que no compra</div>
<ul class="x">
  <li><b>Formulario de «Más volumen» en un servicio caro.</b> Entra mucha gente que rellena sin leer porque tiene los datos prellenados.</li>
  <li><b>Preguntas de sí o no fáciles de marcar.</b> «¿Te interesa ahorrar?» Todo el mundo dice que sí. Pregunta por hechos: terreno, puesto, plazo.</li>
  <li><b>Ninguna respuesta de salida.</b> Si no existe «Solo estoy mirando», el curioso miente sin querer.</li>
  <li><b>Ocultar el precio.</b> Ahorras un clic al curioso y te cuesta una llamada a ti.</li>
  <li><b>Tardar en llamar.</b> El mejor formulario del mundo no arregla un lead al que llamas al día siguiente. El guion está en el recurso LLAMADA.</li>
  <li><b>No mirar las respuestas antes de llamar.</b> Si ya sabes que tiene terreno, no se lo vuelvas a preguntar: pregúntale cuándo firmó.</li>
</ul>
''',
    ],
)

# ------------------------------------------------------------------- LLAMADA

LLAMADA = dict(
    palabra="LLAMADA",
    titulo='La primera llamada a un lead en <em>menos de 5 minutos</em>',
    subtitulo="Lo que se dice, palabra por palabra, desde que suena el teléfono hasta que queda fijado el siguiente paso.",
    dentro=["Los 30 segundos antes de marcar",
            "Apertura literal y qué hacer si no es buen momento",
            "Las 5 preguntas, en orden, con lo que tienes que escuchar",
            "Cómo cerrar el siguiente paso sin presionar",
            "Respuestas a las 7 objeciones que más se oyen"],
    paginas=[
        f'''
<div class="kicker">Antes de marcar · 30 segundos</div>
<h2>Llama mientras aún tiene tu anuncio en la cabeza</h2>
<p class="lead">El lead acaba de rellenar el formulario. Si le llamas ahora, recuerda qué pidió y por qué. Si le llamas mañana, eres un número desconocido más.</p>
<ul class="check">
  <li><b>Lee sus respuestas del formulario.</b> Plazo, presupuesto, situación. No vuelvas a preguntar lo que ya te ha dicho.</li>
  <li><b>Abre tu agenda</b> con dos huecos libres para la siguiente cita. Los vas a necesitar al final.</li>
  <li><b>Llama desde un móvil con WhatsApp</b> y con el nombre de la empresa en el perfil. Si no lo coge, verá quién eras.</li>
  <li><b>Ten a mano la ficha:</b> perfil, dolor, oportunidad y ángulo. Una línea de cada.</li>
</ul>
<div class="kicker" style="margin-top:7mm">Apertura</div>
<h2 class="sm">Los primeros 20 segundos</h2>
{say("Hola, ¿[nombre]? Soy [tu nombre], de [empresa]. Acabas de dejarnos tus datos en el anuncio de [tema] y te llamo para ver tu caso. ¿Te pillo bien dos minutos?")}
<div class="grid2 tight">
  <div class="card"><h3>Si dice que no es buen momento</h3>{say("Sin problema. ¿Te va mejor hoy a las [hora] o mañana a las [hora]?")}<p>Fija hora exacta y mándale un WhatsApp de confirmación mientras colgáis.</p></div>
  <div class="card"><h3>Si no se acuerda</h3>{say("Era un anuncio de [tema] en Instagram. Pusiste que [respuesta del formulario]. ¿Te suena?")}<p>Repetir su propia respuesta le devuelve al momento en que la escribió.</p></div>
</div>
<div class="kicker" style="margin-top:6mm">El marco</div>
{say("Te cuento cómo va: te hago cuatro o cinco preguntas para entender qué buscas. Si podemos ayudarte, te digo el siguiente paso. Y si no encaja, te lo digo también. ¿Te parece?")}
<p class="small">Esta frase baja la guardia. La persona sabe cuánto va a durar y que puede salir sin compromiso.</p>
''',
        f'''
<div class="kicker">Las 5 preguntas</div>
<h2>En este orden, y escuchando más que hablando</h2>
<ol class="steps">
  <li><h3>El motivo</h3>{say("¿Qué te ha hecho pedir información justo ahora?")}<p><b>Escucha:</b> el disparador. Un cambio de trabajo, un terreno comprado, una herramienta que ya no da más de sí. Sin disparador no hay urgencia.</p></li>
  <li><h3>Lo que ya ha probado</h3>{say("¿Qué has probado hasta ahora y qué no te ha funcionado?")}<p><b>Escucha:</b> con quién te compara y qué no quiere repetir. Eso es lo que no puedes prometer y lo que tienes que demostrar.</p></li>
  <li><h3>El objetivo</h3>{say("Si dentro de [plazo] esto estuviera resuelto, ¿cómo sería tu día a día?")}<p><b>Escucha:</b> sus palabras exactas. Las vas a usar en el resumen del final.</p></li>
  <li><h3>Plazo y quién decide</h3>{say("¿Para cuándo lo necesitas? ¿Lo decides tú o lo vas a ver con alguien más?")}<p><b>Escucha:</b> si hay pareja, socio o jefe. Esa persona tiene que estar en la siguiente reunión.</p></li>
  <li><h3>Presupuesto</h3>{say("Para orientarte bien: ¿tienes una cifra en mente o prefieres que te diga entre qué rangos nos movemos?")}<p><b>Escucha:</b> si se acerca a tu precio. Si está muy lejos, dilo ya con respeto y ahorrad tiempo los dos.</p></li>
</ol>
<div class="kicker" style="margin-top:5mm">Ajuste por nicho</div>
<table class="t">
<tr><td style="width:30%"><b>Constructora y casas modulares</b></td><td>En la 4, pregunta por el terreno y la licencia. En la 5, por la financiación: «¿Lo pagáis con fondos propios o con hipoteca?».</td></tr>
<tr><td><b>Software</b></td><td>En la 2, pregunta qué herramienta usan y qué les falla. En la 4, quién firma y si hay periodo de prueba interno.</td></tr>
<tr><td><b>Formación online</b></td><td>En la 3, el objetivo personal (trabajo, ingresos, tiempo). En la 5, si puede pagarlo de una vez o necesita plazos.</td></tr>
<tr><td><b>Negocio local</b></td><td>Más corta. Motivo, urgencia y hueco en agenda. Muchas veces la 5 sobra: da el precio tú.</td></tr>
</table>
''',
        f'''
<div class="kicker">Cerrar el siguiente paso</div>
<h2>Resumen, propuesta y confirmación por WhatsApp</h2>
<ol class="steps compact">
  <li><h3>Resume con sus palabras</h3>{say("Te resumo para ver si lo he entendido: quieres [objetivo] antes de [plazo], lo de [lo que ha probado] no te funcionó y lo vas a decidir con [persona]. ¿Es así?")}</li>
  <li><h3>Propón un paso concreto con dos horarios</h3>{say("El siguiente paso es [visita / demo / reunión] de [duración]. ¿Te viene mejor el [día] a las [hora] o el [día] a las [hora]?")}<p>Constructora: visita al terreno o reunión en oficina. Software: demo con su caso. Formación: llamada de admisión. Local: primera cita.</p></li>
  <li><h3>Confirma antes de colgar</h3>{say("Te acabo de mandar un WhatsApp con el día y la hora. ¿Te ha llegado?")}<p>Si decide con alguien más: «¿Puede estar [persona] en esa reunión?».</p></li>
</ol>
<div class="card warn"><h3>Si no encaja, dilo</h3>{say("Te soy sincero: ahora mismo no creo que seamos lo que buscas, porque [motivo]. Te mando por WhatsApp [recurso útil] y, si cambia algo, me escribes.")}</div>
<div class="kicker" style="margin-top:4mm">Objeciones</div>
<table class="t obj">
<tr><td style="width:30%"><b>«Solo estaba mirando»</b></td><td>«Perfecto, para eso es esta llamada. ¿Qué es lo que te gustaría tener claro antes de decidir nada?»</td></tr>
<tr><td><b>«Mándame la información por email»</b></td><td>«Te la mando. Para no enviarte veinte páginas que no te sirven: ¿qué es lo que más te importa, el precio, el plazo o cómo trabajamos?»</td></tr>
<tr><td><b>«¿Cuánto cuesta?»</b> (nada más empezar)</td><td>«Depende de [variable]. Con dos preguntas te doy un rango real. ¿[pregunta]?» Y luego dale el rango, sin rodeos.</td></tr>
<tr><td><b>«Lo tengo que hablar con mi pareja o socio»</b></td><td>«Normal. ¿Qué crees que te va a preguntar? Si te parece, lo vemos los tres juntos el [día] a las [hora].»</td></tr>
<tr><td><b>«Es caro»</b></td><td>«¿Caro comparado con qué?» Escucha. Si compara con algo que no hace lo mismo, explica la diferencia. Si de verdad no llega, no lo fuerces.</td></tr>
<tr><td><b>«Ahora no es buen momento»</b></td><td>«¿Qué tendría que pasar para que lo fuera?» Apunta la respuesta y la fecha en el CRM y llámale entonces.</td></tr>
<tr><td><b>«Ya estoy hablando con otra empresa»</b></td><td>«Bien hecho, compara. ¿Qué es lo que más te ha gustado de ellos? Así te digo en qué nos parecemos y en qué no.»</td></tr>
</table>
<p class="small">Si no coge el teléfono: vuelve a llamar a los dos minutos y, si tampoco, escríbele por WhatsApp. Los mensajes exactos están en el recurso SEGUIMIENTO.</p>
''',
    ],
)

# --------------------------------------------------------------- SEGUIMIENTO

def dia(n, nombre, cuando, base, variantes, nota=""):
    vs = "".join(f"<tr><td class='nk'>{k}</td><td>{v}</td></tr>" for k, v in variantes)
    nota_html = f"<p class='small'>{nota}</p>" if nota else ""
    return f'''
<div class="day">
  <div class="dh"><span class="dn">Día {n}</span><span class="dt">{nombre}</span><span class="dw">{cuando}</span></div>
  <div class="chat"><div class="bubble">{base}</div></div>
  <table class="t var">{vs}</table>
  {nota_html}
</div>'''

SEGUIMIENTO = dict(
    palabra="SEGUIMIENTO",
    titulo='5 WhatsApp para el lead que <em>no contesta</em>',
    subtitulo="Día 0, 1, 3, 5 y 7. Cada mensaje aporta algo nuevo y se contesta con una palabra. Con variantes para cada nicho.",
    dentro=["Las reglas para que el seguimiento no parezca acoso",
            "Los 5 mensajes listos para copiar",
            "Variantes para constructora, software, formación y negocio local",
            "Qué hacer cuando contesta y qué hacer después del día 7"],
    paginas=[
        f'''
<div class="kicker">Antes de escribir</div>
<h2>Seis reglas para el seguimiento</h2>
<div class="grid3">
  <div class="card"><div class="n">01</div><p><b>Un mensaje por día, nunca dos seguidos.</b> Si no contesta, el siguiente mensaje toca el día que marca la secuencia.</p></div>
  <div class="card"><div class="n">02</div><p><b>Nada de «¿has visto mi mensaje?».</b> Cada mensaje aporta algo: una pregunta útil, un vídeo, una salida fácil.</p></div>
  <div class="card"><div class="n">03</div><p><b>Que se conteste con una palabra.</b> Sí o no, 1 o 2, hoy o mañana. Cuanto menos cueste, más contestan.</p></div>
  <div class="card"><div class="n">04</div><p><b>Horario de persona.</b> Entre las 9:00 y las 21:00, y mejor no en domingo. Un mensaje a las 23:30 resta.</p></div>
  <div class="card"><div class="n">05</div><p><b>Si usas la API de WhatsApp,</b> pasadas 24 horas desde su último mensaje solo puedes escribir con plantillas aprobadas por Meta. Apruébalas antes de lanzar.</p></div>
  <div class="card"><div class="n">06</div><p><b>Si pide que no le escribas, se para.</b> Y se apunta en el CRM. Insistir con quien ya ha dicho que no quema tu número.</p></div>
</div>
<p class="small" style="margin-top:4mm">Los corchetes se rellenan con su nombre y lo que pidió en el formulario. Si el mensaje parece una plantilla, se trata como una plantilla.</p>
{dia(0, "Tras la llamada perdida", "a los 2 minutos de llamar",
     "Hola [nombre], soy [tu nombre] de [empresa]. Te acabo de llamar por la información que pediste sobre [tema]. ¿Te va mejor que hablemos por aquí o te llamo en otro momento?",
     [("Constructora", "«…sobre la casa que quieres construir. ¿Te va mejor por aquí o te llamo esta tarde?»"),
      ("Software", "«…sobre [producto] para tu equipo. Si te va mejor, te mando aquí un vídeo de 3 minutos en vez de llamarte.»"),
      ("Formación", "«…sobre el programa de [tema]. ¿Prefieres que te escriba por aquí?»"),
      ("Local", "«…sobre [servicio]. ¿Quieres que te diga por aquí los huecos que tengo esta semana?»")])}
''',
        f'''
{dia(1, "Una pregunta que filtra", "por la mañana",
     "Buenos días, [nombre]. Para no hacerte perder tiempo en una llamada, una sola pregunta: [pregunta clave]. Con eso ya te digo si te podemos ayudar.",
     [("Constructora", "«¿El terreno ya es tuyo o todavía lo estás buscando?»"),
      ("Software", "«¿Ahora mismo lo hacéis con Excel o con otra herramienta?»"),
      ("Formación", "«¿Lo quieres para cambiar de trabajo o para aplicarlo en lo que ya haces?»"),
      ("Local", "«¿Lo buscas para esta semana o más adelante?»")],
     "La respuesta te dice el color del semáforo (recurso FORMULARIO) aunque no haya llamada.")}
{dia(3, "Algo que pueda ver", "a media tarde",
     "[Nombre], te dejo [recurso] para que veas cómo trabajamos sin tener que hablar con nadie. Si después te encaja, me dices y buscamos un hueco.",
     [("Constructora", "un vídeo o las fotos de una casa terminada, con su plazo real de obra"),
      ("Software", "una demo grabada de 2 a 3 minutos con el caso que más se parece al suyo"),
      ("Formación", "una clase de muestra o el temario del programa"),
      ("Local", "fotos de antes y después reales, o la ubicación y el horario")])}
{dia(5, "La salida fácil", "por la mañana",
     "[Nombre], ¿sigues buscando [lo que pidió] o ya lo has resuelto? Con un «sí» o un «no» me vale, así no te escribo más si ya no te hace falta.",
     [("Constructora", "«¿Sigues con la idea de construir este año o lo has dejado para más adelante?»"),
      ("Software", "«¿Seguís mirando herramientas o ya lo habéis decidido?»"),
      ("Formación", "«¿Sigues pensando en formarte en [tema] o ahora no es el momento?»"),
      ("Local", "«¿Sigues necesitando [servicio] o ya lo has solucionado?»")],
     "Dar permiso para decir que no es lo que más respuestas saca. Un «no» también vale: limpia tu CRM.")}
''',
        f'''
{dia(7, "La despedida", "a media tarde",
     "Te escribo por última vez para no ser pesado, [nombre]. Cierro tu solicitud por ahora. Si más adelante quieres retomarlo, escríbeme por aquí y lo vemos. Mucha suerte con [su proyecto].",
     [("Constructora", "«…Mucha suerte con la casa. Si encuentras terreno, aquí estoy.»"),
      ("Software", "«…Si dentro de unos meses el Excel se os queda corto, aquí estoy.»"),
      ("Formación", "«…Cuando abramos la próxima convocatoria, ¿quieres que te avise?»"),
      ("Local", "«…Si te vuelve a hacer falta [servicio], tienes mi número.»")],
     "La despedida no es un truco. Cierra de verdad: si no contesta, pasa a reactivación.")}
<div class="kicker" style="margin-top:6mm">Cuando contesta</div>
<ul class="check">
  <li><b>Responde en minutos, no en horas.</b> Si te contesta y tardas, vuelves al principio.</li>
  <li><b>Pasa a llamada si puede.</b> «¿Te llamo ahora dos minutos y lo vemos?». Usa el guion del recurso LLAMADA.</li>
  <li><b>Si prefiere seguir por escrito, sigue por escrito.</b> Las 5 preguntas de la llamada funcionan igual en mensajes, de una en una.</li>
  <li><b>Apunta en el CRM</b> qué contestó y en qué día de la secuencia. En unas semanas sabrás qué mensaje funciona mejor con tus leads.</li>
</ul>
<div class="kicker" style="margin-top:6mm">Después del día 7</div>
<table class="t">
<tr><td style="width:24%"><b>A los 30 días</b></td><td>Un mensaje con una novedad real: obra terminada, función nueva, convocatoria abierta, hueco en agenda.</td></tr>
<tr><td><b>A los 60 o 90 días</b></td><td>«[Nombre], hace unos meses preguntaste por [tema]. ¿Sigue en tus planes?» Nada más.</td></tr>
<tr><td><b>Nunca</b></td><td>A quien pidió que no le escribieras. Ni aunque haya pasado un año.</td></tr>
</table>
<div class="kicker" style="margin-top:6mm">La secuencia de un vistazo</div>
<table class="t">
<thead><tr><th>Día</th><th>Qué aporta</th><th>Respuesta que buscas</th></tr></thead>
<tr><td style="width:14%"><b>0</b></td><td>Explica la llamada perdida</td><td>«Por aquí» o una hora para llamar</td></tr>
<tr><td><b>1</b></td><td>Una pregunta que filtra</td><td>Una palabra que te da el color del semáforo</td></tr>
<tr><td><b>3</b></td><td>Algo que puede ver sin hablar con nadie</td><td>«Me encaja» o una duda concreta</td></tr>
<tr><td><b>5</b></td><td>Permiso para decir que no</td><td>«Sí» o «no»</td></tr>
<tr><td><b>7</b></td><td>Cierre amable</td><td>Ninguna: la puerta queda abierta</td></tr>
</table>
''',
    ],
)

# ------------------------------------------------------------------- LANDING

def item(n, titulo, como):
    return f'<li><span class="box"></span><span class="num">{n:02d}</span><div><b>{titulo}</b><p>{como}</p></div></li>'

LANDING = dict(
    palabra="LANDING",
    titulo='La checklist de la landing <em>antes de lanzar</em> anuncios',
    subtitulo="20 puntos para revisar en una tarde. Cada uno con la forma de comprobarlo. Si falla uno, no enciendas la campaña todavía.",
    dentro=["Mensaje: lo que tiene que entenderse en 5 segundos",
            "Confianza: lo que hace que alguien deje su teléfono",
            "Formulario y conversión: que el lead llegue y se mida",
            "Técnica y legal: lo que nadie mira hasta que falla",
            "La prueba de 10 minutos antes de gastar un euro"],
    paginas=[
        f'''
<div class="kicker">Bloque A · Mensaje</div>
<h2 class="sm">Lo que se entiende sin hacer scroll</h2>
<ol class="cl">
{item(1, "El titular dice qué haces y para quién", "Enséñale la primera pantalla a alguien de fuera 5 segundos y pregúntale qué vendes. Si duda, reescribe.")}
{item(2, "La landing promete lo mismo que el anuncio", "Pon el anuncio y la landing lado a lado. Misma oferta, mismas palabras, misma imagen principal si se puede.")}
{item(3, "El botón se ve en el móvil sin bajar", "Abre la landing en tu móvil. El primer botón tiene que estar en la primera pantalla.")}
{item(4, "Hay una sola acción principal", "Todos los botones llevan al mismo sitio: formulario, WhatsApp o agenda. Nada de cinco caminos distintos.")}
{item(5, "Se habla de precio, aunque sea «desde»", "En servicios caros, un precio de partida o cómo se calcula filtra a quien no puede pagarlo antes de que te llame.")}
</ol>
<div class="kicker" style="margin-top:5mm">Bloque B · Confianza</div>
<h2 class="sm">Lo que hace que alguien deje su teléfono</h2>
<ol class="cl">
{item(6, "Pruebas reales, cerca del botón", "Reseñas de Google, obras o proyectos terminados, logos de clientes con su permiso. Nada inventado ni de banco de imágenes.")}
{item(7, "Se ve quién está detrás", "Una foto real del equipo o de quien atiende. La gente compra a personas.")}
{item(8, "Datos de empresa visibles", "Razón social, CIF, dirección y teléfono en el pie. Si no aparecen, parece que te escondes.")}
{item(9, "Responde a las objeciones de siempre", "Las 4 o 5 preguntas que te hacen en todas las llamadas, con su respuesta, en un bloque de preguntas frecuentes.")}
{item(10, "Explica qué pasa después de dejar los datos", "«Te llamamos hoy, vemos tu caso en 15 minutos y te mandamos [lo que sea]». Quita el miedo a que le persigan.")}
</ol>
''',
        f'''
<div class="kicker">Bloque C · Formulario y conversión</div>
<h2 class="sm">Que el lead llegue, llegue bien y se mida</h2>
<ol class="cl">
{item(11, "Formulario corto con una pregunta que filtra", "Nombre, teléfono con prefijo y de 1 a 3 preguntas de opción múltiple. Las preguntas por nicho están en el recurso FORMULARIO.")}
{item(12, "El botón de WhatsApp abre el chat correcto", "Púlsalo desde un móvil. Tiene que abrir tu número con un mensaje ya escrito, por ejemplo «Hola, vengo de la web y quiero información de [servicio]».")}
{item(13, "Página de gracias propia", "Con su propia URL, para medir conversiones, y diciendo cuándo vas a llamar y desde qué número.")}
{item(14, "El lead llega al instante a quien llama", "Rellena el formulario con tus datos. Tiene que entrar en el CRM y avisar al comercial en el momento, no en un email que se lee al día siguiente.")}
</ol>
<div class="kicker" style="margin-top:5mm">Bloque D · Técnica</div>
<h2 class="sm">Lo que nadie mira hasta que falla</h2>
<ol class="cl">
{item(15, "Carga rápida en el móvil", "Pasa la URL por PageSpeed Insights y ábrela con datos móviles, no con el wifi de la oficina. Comprime las imágenes y quita vídeos de fondo pesados.")}
{item(16, "Píxel y API de Conversiones funcionando", "En el Administrador de eventos de Meta, usa «Probar eventos». El evento Lead se dispara al enviar el formulario o en la página de gracias, no al cargar la landing.")}
{item(17, "Dominio verificado en Meta", "En la configuración del negocio, en Seguridad de la marca. Sin verificar, configurar eventos te dará problemas.")}
{item(18, "Se ve bien en un móvil pequeño", "Pruébala en un Android y en un iPhone. Sin textos cortados, sin ventanas emergentes que tapen el botón, sin scroll lateral.")}
</ol>
<div class="kicker" style="margin-top:5mm">Bloque E · Legal</div>
<ol class="cl">
{item(19, "Privacidad, cookies y aviso legal en regla", "Casilla de privacidad sin marcar por defecto y enlazada al texto legal. Analítica y píxel solo después de aceptar las cookies. Fuentes servidas desde tu propio dominio.")}
{item(20, "Nada que Meta rechace", "Sin promesas de resultados garantizados, sin antes y después en salud o estética, sin preguntas sobre atributos personales («¿tienes deudas?», «¿tienes sobrepeso?»).")}
</ol>
''',
        f'''
<div class="kicker">La prueba de los 10 minutos</div>
<h2>Antes de gastar el primer euro</h2>
<p class="lead">Hazla tú, con tu móvil, como si fueras un cliente. Si alguna falla, la campaña espera.</p>
<ol class="steps">
  <li><h3>Haz clic en tu propio anuncio</h3><p>Desde la vista previa del anuncio en el móvil. Comprueba que el enlace lleva a la landing correcta y que los parámetros UTM llegan.</p></li>
  <li><h3>Rellena el formulario como lo haría un cliente</h3><p>Con un teléfono real. Equivócate a propósito en un campo y mira que el error se entiende.</p></li>
  <li><h3>Comprueba que suena el aviso</h3><p>El lead aparece en el CRM y le llega al comercial en menos de un minuto. Si no llega, no hay campaña.</p></li>
  <li><h3>Mira el evento en Meta</h3><p>En «Probar eventos», el Lead aparece una vez, no dos. Si aparece dos veces, Meta aprende con datos falsos.</p></li>
  <li><h3>Llama al lead de prueba en menos de 5 minutos</h3><p>Cronométralo. Si el proceso real no consigue llamar en ese tiempo, arréglalo antes de lanzar.</p></li>
</ol>
<div class="card warn" style="margin-top:6mm"><h3>La regla</h3><p>Una landing preciosa con el formulario roto quema presupuesto igual que una fea. Primero que funcione todo el camino, de anuncio a llamada. Después, que sea bonita.</p></div>
<div class="kicker" style="margin-top:7mm">Si solo tienes una hora</div>
<h2 class="sm">Revisa primero estos cinco</h2>
<table class="t">
<tr><td style="width:12%"><b>03</b></td><td>El botón se ve en el móvil sin bajar. Si no lo ven, no hay lead.</td></tr>
<tr><td><b>11</b></td><td>Formulario corto con una pregunta que filtra. Sin filtro, llamas a curiosos.</td></tr>
<tr><td><b>14</b></td><td>El lead llega al instante a quien llama. Si llega tarde, se enfría.</td></tr>
<tr><td><b>16</b></td><td>El evento Lead funciona. Sin él, Meta no sabe a quién buscar.</td></tr>
<tr><td><b>19</b></td><td>Privacidad y cookies en regla. Es lo que te puede traer un disgusto que no se arregla con anuncios.</td></tr>
</table>
''',
    ],
)

# ------------------------------------------------------------------- GANCHOS

CATS, GUIA = ganchos_de_seo()

# Cuándo usar cada tipo (texto propio de Ceos; el de seo.ts habla de las versiones de Ads al Vuelo)
CUANDO = {
    "Pregunta que duele": ("Tráfico frío", "Gente que no te conoce. Se reconoce en la pregunta y se queda.", "¿Cuánto tiempo llevas diciendo que vas a construir tu casa?"),
    "Error y corrección": ("Cualquier público", "Funciona en todos los nichos y es de lo que más se guarda.", "El error que veo cada día en las demos de software."),
    "Resultado primero": ("Si tienes pruebas visuales", "Obras, antes y después, una demo. Enseña el final al principio.", "Así estaba esta parcela hace [tiempo real]. Mira cómo está hoy."),
    "Curiosidad": ("Orgánico y anuncios nativos", "Para que el anuncio parezca un vídeo normal de tu cuenta.", "Esto se lo digo a todos mis alumnos el primer día."),
    "Oferta clara": ("Retargeting", "Gente que ya ha visto tus vídeos o ha visitado tu web.", "Primera consulta sin compromiso. Te explico qué pasa."),
    "Identificación (POV)": ("Reels y TikTok", "El público lo comparte con quien le pasa lo mismo.", "Dueños de academias, esto os va a sonar."),
}


def bloque_cat(i, cat):
    nombre, _uso, items = cat
    publico, para, ej = CUANDO.get(nombre, ("", "", ""))
    lis = "".join(f"<li><span class='hn'>{i*6+k+1:02d}</span>{t}</li>" for k, t in enumerate(items))
    return f'''
<div class="cat">
  <div class="ch"><span class="ci">{i+1:02d}</span><h3>{nombre}</h3><span class="cu">{publico}</span></div>
  <ol class="hk">{lis}</ol>
  <p class="cej">{ejemplo()} {ej}</p>
</div>'''


filas_cuando = "".join(
    f"<tr><td style='width:28%'><b>{c[0]}</b></td><td style='width:22%'>{CUANDO[c[0]][0]}</td><td>{CUANDO[c[0]][1]}</td></tr>" for c in CATS)
guia_html = "".join(
    f"<li><h3>{p}</h3><p>{d}</p><p class='err'><b>Error típico:</b> {e}</p></li>" for p, d, e in GUIA)

GANCHOS = dict(
    palabra="GANCHOS",
    titulo='36 ganchos para tus <em>anuncios en vídeo</em>',
    subtitulo="Seis tipos de gancho, seis plantillas de cada uno y cuándo usar cada tipo. Más la guía para grabarlos bien con el móvil.",
    dentro=["Cuándo usar cada tipo de gancho",
            "Las 36 plantillas, listas para rellenar",
            "Un ejemplo de cada tipo para nuestros nichos",
            "Guía de grabación en 6 pasos"],
    paginas=[
        f'''
<div class="kicker">Cómo usar este PDF</div>
<h2>El gancho decide si alguien se queda</h2>
<p class="lead">Los primeros segundos del vídeo son los que deciden si la persona sigue mirando o pasa al siguiente. Aquí tienes 36 frases para esos segundos, agrupadas por tipo.</p>
<div class="grid3">
  <div class="card"><div class="n">01</div><p><b>Rellena los corchetes</b> con las palabras de tu cliente, no con las tuyas. «Construir tu casa», no «soluciones habitacionales».</p></div>
  <div class="card"><div class="n">02</div><p><b>Graba tres ganchos para el mismo vídeo.</b> El resto del anuncio igual. Súbelos como anuncios distintos y deja que Meta te diga cuál retiene más.</p></div>
  <div class="card"><div class="n">03</div><p><b>Nada inventado.</b> Si el gancho pide un resultado, un plazo o un precio, que sea real. Meta rechaza promesas y tu cliente también.</p></div>
</div>
<div class="kicker" style="margin-top:7mm">Cuándo usar cada tipo</div>
<table class="t">
<thead><tr><th>Tipo</th><th>Para quién</th><th>Por qué</th></tr></thead>
<tbody>{filas_cuando}</tbody>
</table>
<div class="note" style="margin-top:6mm"><b>Una combinación que suele dar juego:</b> abre la campaña de captación con «Pregunta que duele» y «Error y corrección», y guarda «Oferta clara» para quien ya ha visto tus vídeos. «Curiosidad» y «POV» te sirven también para el contenido orgánico.</div>
''',
        "".join(bloque_cat(i, c) for i, c in enumerate(CATS[:3])),
        "".join(bloque_cat(i + 3, c) for i, c in enumerate(CATS[3:])),
        f'''
<div class="kicker">Bonus</div>
<h2>Cómo grabarlos con el móvil</h2>
<p class="lead">Un buen gancho mal grabado se pierde. Seis pasos para que el vídeo aguante hasta el final.</p>
<ol class="steps guia">{guia_html}</ol>
''',
    ],
)

# ------------------------------------------------------------------- NUMEROS

NUMEROS = dict(
    palabra="NUMEROS",
    titulo='¿Cuánto puedes pagar <em>por un lead?</em>',
    subtitulo="Hoja de cálculo en papel: tu ticket, tu margen y tu tasa de cierre te dicen cuánto puedes pagar por un lead y por un cliente sin perder dinero.",
    dentro=["Los 4 datos que necesitas y dónde sacarlos",
            "Las fórmulas, una a una",
            "Una hoja para rellenar con tus números",
            "Un ejemplo resuelto (marcado EJEMPLO)",
            "Lo que cuesta montar el sistema por tu cuenta"],
    paginas=[
        f'''
<div class="kicker">Los datos de partida</div>
<h2>Cuatro números que tienes que saber</h2>
<p class="lead">Si no los tienes, sácalos de tus últimas ventas. Mejor un número aproximado tuyo que uno de internet.</p>
<div class="grid2">
  <div class="card"><div class="n">T</div><h3>Ticket medio</h3><p>Lo que paga de media un cliente en su primera compra. Si hay cuotas (software, formación por meses), mira la fórmula de recurrencia de la página siguiente.</p></div>
  <div class="card"><div class="n">M</div><h3>Margen</h3><p>Lo que te queda de cada venta después de pagar materiales, horas y comisiones, en porcentaje. No el precio: lo que te queda.</p></div>
  <div class="card"><div class="n">C</div><h3>Tasa de cierre</h3><p>De cada 100 leads, cuántos acaban comprando. Si llevas CRM, divide clientes entre leads de los últimos meses.</p></div>
  <div class="card"><div class="n">B</div><h3>Beneficio que quieres guardar</h3><p>Lo mínimo que quieres ganar por cliente después de pagar la captación. Esto lo decides tú.</p></div>
</div>
<div class="kicker" style="margin-top:7mm">Las fórmulas</div>
<div class="f"><span class="fl">1</span><div><b>Beneficio por venta</b><code>Ticket × Margen</code></div></div>
<div class="f"><span class="fl">2</span><div><b>Lo máximo que puedes pagar por un cliente</b><code>Beneficio por venta − Beneficio que quieres guardar</code></div></div>
<div class="f"><span class="fl">3</span><div><b>Lo máximo que puedes pagar por un lead</b><code>Máximo por cliente × Tasa de cierre</code></div></div>
<div class="f"><span class="fl">4</span><div><b>Leads que necesitas al mes</b><code>Clientes que quieres ÷ Tasa de cierre</code></div></div>
<div class="f"><span class="fl">5</span><div><b>Presupuesto de anuncios al mes</b><code>Leads que necesitas × Coste por lead real</code></div></div>
<div class="note"><b>Con cuotas o recompra:</b> cambia el ticket por el valor de un cliente durante su vida contigo: <code class="in">Cuota × Margen × Meses que se queda de media</code>. Si es tu primer año, usa un plazo prudente.</div>
''',
        f'''
<div class="kicker">Tu hoja</div>
<h2>Rellénala con lápiz</h2>
<table class="t sheet">
<tr><td>Ticket medio</td><td class="blank"></td><td class="u">€</td></tr>
<tr><td>Margen</td><td class="blank"></td><td class="u">%</td></tr>
<tr><td><b>1.</b> Beneficio por venta (ticket × margen)</td><td class="blank"></td><td class="u">€</td></tr>
<tr><td>Beneficio que quieres guardar por cliente</td><td class="blank"></td><td class="u">€</td></tr>
<tr><td><b>2.</b> Máximo por cliente (1 − lo que guardas)</td><td class="blank"></td><td class="u">€</td></tr>
<tr><td>Tasa de cierre (clientes ÷ leads)</td><td class="blank"></td><td class="u">%</td></tr>
<tr><td><b>3.</b> Máximo por lead (2 × tasa de cierre)</td><td class="blank hl"></td><td class="u">€</td></tr>
<tr><td>Clientes que quieres al mes</td><td class="blank"></td><td class="u"></td></tr>
<tr><td><b>4.</b> Leads necesarios al mes</td><td class="blank"></td><td class="u"></td></tr>
<tr><td><b>5.</b> Presupuesto al mes (4 × coste por lead real)</td><td class="blank"></td><td class="u">€</td></tr>
</table>
<div class="ejbox">
<div class="ejh">{ejemplo()} <span>Números inventados para enseñar la cuenta. No son datos de ningún cliente.</span></div>
<p><b>Una empresa de casas modulares.</b> Ticket medio 100.000 €. Margen 15 %. Quiere guardar al menos 10.000 € por casa. Cierra 2 de cada 100 leads.</p>
<table class="t mini">
<tr><td>1. Beneficio por venta</td><td>100.000 × 15 % = <b>15.000 €</b></td></tr>
<tr><td>2. Máximo por cliente</td><td>15.000 − 10.000 = <b>5.000 €</b></td></tr>
<tr><td>3. Máximo por lead</td><td>5.000 × 2 % = <b>100 €</b></td></tr>
<tr><td>4. Para 2 casas al mes</td><td>2 ÷ 2 % = <b>100 leads</b></td></tr>
</table>
<p class="small">Si con el mismo formulario y mejores llamadas cerrara 4 de cada 100, el máximo por lead pasaría a 200 €. Mejorar el cierre te deja pagar más por cada lead, y eso te permite pujar por gente que tu competencia no puede pagar.</p>
</div>
''',
        f'''
<div class="kicker">La otra cuenta</div>
<h2>Lo que cuesta montar el sistema <em>por tu cuenta</em></h2>
<p class="lead">Para captar clientes con Meta Ads de forma constante no basta con los anuncios. Hace falta todo esto, a la vez y coordinado.</p>
<table class="t sheet cost">
<thead><tr><th>Pieza</th><th>Tu coste al año</th></tr></thead>
<tr><td><b>Alguien que grabe y edite</b> los anuncios, cada mes, para que no se gasten</td><td class="blank"></td></tr>
<tr><td><b>Un sitio para grabar</b> con luz y sonido, y tiempo para sacar varios anuncios por sesión</td><td class="blank"></td></tr>
<tr><td><b>Alguien que lleve Meta Ads</b>: campañas, públicos, pruebas, presupuesto</td><td class="blank"></td></tr>
<tr><td><b>Alguien que siga cada lead</b>: llamada en minutos, WhatsApp, agenda</td><td class="blank"></td></tr>
<tr><td><b>Un CRM</b> montado y conectado a los anuncios</td><td class="blank"></td></tr>
<tr><td><b>Landing y formularios</b> que filtren y midan</td><td class="blank"></td></tr>
<tr class="tot"><td><b>Total</b></td><td class="blank hl"></td></tr>
</table>
<div class="big">
  <div class="bn">32.900 €<span>/año</span></div>
  <p>Es nuestra cuenta de lo que cuesta montarlo por tu cuenta. Y se paga antes de saber si funciona.</p>
</div>
<p class="small">Compara tu total con lo que te dejan las fórmulas de la página anterior. Si el sistema cuesta más de lo que te deja de beneficio el primer año, piensa también en quién asume el riesgo si no se vende.</p>
<div class="kicker" style="margin-top:6mm">Qué hacer con tu resultado</div>
<table class="t">
<tr><td style="width:36%"><b>Tu coste por lead real está por debajo del máximo</b></td><td>Hay margen para subir presupuesto. Hazlo poco a poco y vigila que la tasa de cierre no baje.</td></tr>
<tr><td><b>Está por encima del máximo</b></td><td>Antes de tocar los anuncios, mira el cierre: formulario que filtre, llamada en minutos y seguimiento. Subir el cierre sube lo que puedes pagar.</td></tr>
<tr><td><b>No sabes tu tasa de cierre</b></td><td>Empieza por ahí. Apunta en un CRM, o en una hoja, cada lead y si acabó comprando. Con unas semanas de datos ya puedes hacer la cuenta.</td></tr>
</table>
''',
    ],
)

RECURSOS = [FORMULARIO, LLAMADA, SEGUIMIENTO, LANDING, GANCHOS, NUMEROS]
