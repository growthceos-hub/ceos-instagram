# -*- coding: utf-8 -*-
"""Los 10 carruseles PDF del pack 01 de LinkedIn.

Datos reales permitidos: casas modulares 140 contactos a 6,64 € y 33 a 20,13 €;
software 1,92 € y 3,36 €; formación online 28 contactos a 2,09 €; 26 días;
15-20 anuncios; 10 perfiles; puesta en marcha + comisión; sin permanencia;
+17 clientes activos; 32.900 €/año. Todo lo demás va marcado como EJEMPLO.
"""
from h import (arr, big, card, chips, close, cover, ej, note, opts, p, page,
               pair, rows, say, stat, stats)

CIERRE_FACTS = True

CARRUSELES = {}

# ------------------------------------------------------------------ C1
CARRUSELES["casas-modulares-6-64-vs-20-13"] = [
    cover("Caso real · Casas modulares",
          'Mismo sector. Un contacto a <em>6,64 €</em>. Otro a <em>20,13 €</em>.',
          "Dos campañas nuestras de casas modulares. Antes de decidir cuál va mejor, hay cuatro preguntas."),
    page("Los datos", "Dos campañas, el mismo producto",
         stats(stat("6,64 €", "por contacto<br><b>140 contactos</b>"),
               stat("20,13 €", "por contacto<br><b>33 contactos</b>"))
         + p("Una invirtió unos 930 €. La otra, unos 664 €. Las dos venden casas modulares.")
         + note("Datos reales de dos campañas de Ceos Growth en Meta Ads.")),
    page("La tentación", "Apagar la cara y doblar la barata",
         p("Sobre el papel, la segunda es tres veces más cara.")
         + p("Pero el coste por contacto mide una sola cosa: cuánto cuesta que alguien rellene un formulario.")
         + say("No dice si tiene terreno, si quiere empezar este año ni si puede pagarlo.")),
    page("Pregunta 1", "¿Cuántos tienen terreno?",
         p("En casas modulares, sin terreno no hay obra. Al menos este año.")
         + p("Un contacto con parcela y otro sin ella cuestan lo mismo en Meta. No valen lo mismo.")
         + note("Por eso es la primera pregunta de nuestros formularios en este sector.")),
    page("Pregunta 2", "¿Qué preguntaba cada formulario?",
         p("Cada pregunta que añades quita volumen y sube el precio por contacto.")
         + p("A cambio, el que llega ya ha dicho su plazo, su terreno y cómo piensa pagar.")
         + say("Un formulario más exigente casi siempre sale más caro por contacto. Es lo que buscas.")),
    page("Pregunta 3", "¿A cuántos se llamó en 5 minutos?",
         p("Un contacto de 20 € al que llamas mañana vale menos que uno de 6 € al que llamas ahora.")
         + p("En 5 minutos aún tiene tu anuncio en la cabeza. Al día siguiente eres un número desconocido.")),
    page("Pregunta 4", "¿Cuánto te cuesta cada <em>cliente?</em>",
         f'<div class="ejrow">{ej()} Tasas de cierre inventadas, solo para ver la cuenta.</div>'
         + rows([("6,64 € × 50 contactos por venta", "<b>332 €</b> por cliente"),
                 ("20,13 € × 15 contactos por venta", "<b>302 €</b> por cliente")])
         + p("Si el formulario caro cierra más, el contacto caro sale más barato. Y puede pasar lo contrario: lo dicen las ventas.")),
    close('El coste por contacto se mira. Se decide con el coste por <em>cliente.</em>',
          "Si quieres que miremos tus campañas con esta cuenta, escríbeme por privado."),
]

# ------------------------------------------------------------------ C2
CARRUSELES["140-contactos-y-ahora-que"] = [
    cover("Caso real · Casas modulares",
          '140 contactos a 6,64 €. <em>Ahora hay que llamarlos.</em>',
          "Lo que tiene que pasar entre que entra un contacto y la visita a la obra."),
    page("El dato", "Un buen número. Y la parte fácil.",
         stats(stat("140", "contactos"), stat("6,64 €", "cada uno"), stat("≈930 €", "en anuncios"))
         + p("Una campaña nuestra de casas modulares. Desde aquí, el anuncio ya no vende nada. Vende lo que haga tu equipo.")),
    page("El riesgo", "140 contactos son 140 llamadas",
         p("Entran a cualquier hora, también en fin de semana. A veces varios seguidos.")
         + p("Si nadie está pendiente, el último espera horas. Y el que espera se enfría.")
         + say("Un contacto barato al que nadie llama sale carísimo.")),
    page("Paso 1", "El aviso llega al momento",
         p("El contacto entra en el CRM y el comercial recibe el aviso en el móvil. No en un email que se lee mañana.")
         + p("Con sus respuestas del formulario a la vista: terreno, plazo, cómo paga.")),
    page("Paso 2", "Cada contacto, un color",
         opts("¿A quién llamas primero?", [
             ("v", "<b>Verde.</b> Terreno, plazo y forma de pago. Llamada en 5 minutos."),
             ("a", "<b>Ámbar.</b> Le falta una pieza: firma del terreno, hipoteca. Llamada hoy."),
             ("r", "<b>Rojo.</b> Solo está mirando. WhatsApp con algo útil y recordatorio a 60 días.")])),
    page("Paso 3", "La primera llamada",
         p("Cinco preguntas, en orden. La primera:")
         + say("¿Qué te ha hecho pedir información justo ahora?")
         + p("Luego terreno y licencia, plazo, quién decide y si lo paga con fondos propios o con hipoteca.")),
    page("Paso 4", "Y el que no contesta",
         p("Cinco WhatsApp en siete días. Ninguno dice «¿has visto mi mensaje?».")
         + say("¿El terreno ya es tuyo o lo estás buscando?")
         + p("Una pregunta que se contesta con una palabra y te dice su color sin llamar.")),
    close('El anuncio trae el contacto. <em>La venta</em> la trae lo de después.',
          "¿Quieres que revisemos qué pasa con tus contactos desde que entran? Escríbeme por privado."),
]

# ------------------------------------------------------------------ C3
CARRUSELES["software-1-92-por-contacto"] = [
    cover("Caso real · Software",
          '1,92 € por contacto. <em>Y aun así puede salir caro.</em>',
          "Dos campañas de software, a 1,92 € y 3,36 €. Qué hay que filtrar cuando el contacto es barato."),
    page("Los datos", "Dos campañas de software",
         stats(stat("1,92 €", "por contacto<br>campaña 1"), stat("3,36 €", "por contacto<br>campaña 2"))
         + note("Datos reales de campañas de Ceos Growth en Meta Ads.")),
    page("El problema", "Barato atrae a todo el mundo",
         p("Cuando rellenar no cuesta nada, entra el gerente que lleva meses buscando una herramienta.")
         + p("Y también el empleado curioso, el estudiante que hace un trabajo y el que solo quiere la prueba gratis.")
         + say("Con contactos baratos, el cuello de botella pasa a ser el comercial.")),
    page("Filtro 1", "¿Cuál es tu puesto?",
         opts("Opciones de respuesta", [
             ("v", "Dueño o gerente → demo."),
             ("v", "Responsable de área → demo."),
             ("a", "Empleado → en la llamada, pregunta quién decide."),
             ("r", "Freelance o estudiante → prueba gratis, sin comercial.")])),
    page("Filtro 2", "¿Cuántas personas lo usarían?",
         chips(["Solo yo", "De 2 a 10", "De 11 a 50", "Más de 50"])
         + p("Ajusta los tramos a tus planes de precio.")
         + p("El tramo te dice qué plan enseñar en la demo y quién la hace.")),
    page("Filtro 3", "¿Cómo lo hacéis ahora?",
         rows([("Con Excel", "enseña el tiempo que ahorra con su caso"),
               ("Con otra herramienta", "prepara una comparación honesta"),
               ("A mano o en papel", "empieza por el problema, no por las funciones"),
               ("No lo hacemos", "primero hay que vender el problema")])),
    page("Filtro 4", "¿Cuándo lo queréis funcionando?",
         opts("Opciones de respuesta", [
             ("v", "Este mes → demo esta semana."),
             ("v", "Este trimestre → demo esta semana."),
             ("a", "Este año → llamada corta y seguimiento."),
             ("r", "Solo estoy investigando → emails, sin llamada.")])),
    page("La demo", "Su caso, no tu lista de funciones",
         p("Con las cuatro respuestas, llegas a la demo sabiendo con quién compite tu software y para cuándo lo necesita.")
         + say("Si el que decide no está en la demo, la demo se repite.")),
    close('Un contacto barato está bien. Llamar a todos <em>por igual</em>, no tanto.',
          "Si vendes software y quieres revisar tu formulario, escríbeme por privado."),
]

# ------------------------------------------------------------------ C4
CARRUSELES["formacion-online-un-mes-normal"] = [
    cover("Caso real · Formación online",
          'Un mes normal: <em>28 contactos</em> a 2,09 €.',
          "Sin récords. El mes que más se parece a lo que puedes esperar."),
    page("El dato", "Lo que da un mes cualquiera",
         stats(stat("28", "contactos"), stat("2,09 €", "cada uno"), stat("58,52 €", "en anuncios"))
         + note("Datos reales de una campaña de formación online gestionada por Ceos Growth.")),
    page("Por qué este mes", "Los récords venden. Los meses normales pagan.",
         p("Un pico queda bien en una captura. Pero no puedes planificar con él.")
         + p("Para saber cuántos alumnos esperar, cuánto invertir y a quién contratar, necesitas el mes de siempre.")),
    page("La cuenta", "Casi uno al día",
         big("≈1")
         + p("28 contactos al mes es casi un contacto al día. Con ese ritmo no hay excusa para no llamar a todos en 5 minutos.")
         + say("Con pocos contactos, cada uno cuenta. No se puede perder ni uno por llamar tarde.")),
    page("La pregunta clave", "¿Puede invertir ahora?",
         opts("Si el programa encaja contigo, ¿puedes invertir en él ahora?", [
             ("v", "Sí, tengo el dinero apartado → llamada ya."),
             ("a", "Sí, si se puede pagar a plazos → llamada hoy, explica las cuotas."),
             ("r", "Ahora mismo no → producto de entrada o lista de espera.")])),
    page("La llamada", "Llamada de admisión, no de venta",
         p("Pregunta por el objetivo: cambiar de trabajo, ganar más, tener tiempo.")
         + p("Y por las horas que puede dedicarle a la semana. Si tu programa exige más de lo que tiene, díselo.")
         + say("Un alumno que abandona no recomienda.")),
    page("El «ahora no»", "No es un contacto perdido",
         p("Quien no puede pagar hoy puede estar listo en la próxima convocatoria.")
         + say("Cuando abramos la próxima convocatoria, ¿quieres que te avise?")
         + p("Apúntalo en el CRM con la fecha. Ese contacto ya lo pagaste.")),
    close('Un mes normal, repetido, <em>da para planificar.</em>',
          "Si vendes formación online y quieres ver tus números con calma, escríbeme por privado."),
]

# ------------------------------------------------------------------ C5
CARRUSELES["7-errores-que-traen-curiosos"] = [
    cover("Meta Ads · Formularios",
          '7 errores que llenan tu CRM de <em>curiosos</em>',
          "Gente que rellena, no coge el teléfono y, si lo coge, dice «solo estaba mirando»."),
    page("Error 1", "Formulario de «Más volumen» en un servicio caro",
         p("Con los datos prellenados, rellenar cuesta dos toques. Muchos lo hacen sin leer.")
         + say("Si vendes algo caro, elige «Mayor intención».")),
    page("Error 2", "Esconder el precio",
         p("Le ahorras un clic al curioso y te cuesta una llamada a ti.")
         + p("Pon un «desde» en la pantalla de introducción. Quien no puede pagarlo se va solo.")),
    page("Error 3", "Preguntas que todo el mundo contesta que sí",
         say("¿Te interesa ahorrar?")
         + p("Pregunta por hechos: si tiene terreno, qué puesto ocupa, para cuándo lo necesita.")),
    page("Error 4", "No dejar una salida",
         p("Si no existe «Solo estoy mirando», el curioso marca cualquier opción y no lo distingues.")
         + p("Con la salida, se identifica él solo. Y no le llamas.")),
    page("Error 5", "Regalar algo sin decir qué viene después",
         p("«Descarga gratis» trae a quien busca cosas gratis.")
         + p("Si el regalo lleva a una llamada, dilo en el anuncio. Menos contactos, más conversaciones.")),
    page("Error 6", "Un anuncio que habla a todo el mundo",
         p("Si no dices para quién no es, no se va nadie.")
         + say("Si todavía no tienes terreno, este vídeo no es para ti.")
         + p("Una frase así filtra más que cualquier segmentación.")),
    page("Error 7", "Llamar al día siguiente",
         p("El contacto bueno también parece curioso cuando ya no se acuerda de ti.")
         + p("Llama en 5 minutos. Si no lo coge, a los dos minutos otra vez, y luego un WhatsApp.")),
    close('Los curiosos entran <em>por el formulario.</em>',
          "¿Quieres que le echemos un ojo a tu formulario? Escríbeme por privado."),
]

# ------------------------------------------------------------------ C6
CARRUSELES["sistema-26-dias"] = [
    cover("Cómo trabajamos",
          'Lo que dejamos montado <em>en 26 días</em>',
          "De nada a una campaña que trae contactos y un equipo que sabe qué hacer con ellos."),
    page("Antes", "Cada pieza por su lado",
         rows([("Anuncios", "entran contactos"), ("CRM", "sin configurar"), ("Comercial", "sin avisos")])
         + say("Si las piezas no están unidas, el contacto se pierde por el camino.")),
    page("Pieza 1", "Entre 15 y 20 anuncios grabados en nuestro estudio",
         p("Con guion, luz y edición. Ganchos distintos, objeciones distintas.")
         + p("Así se comparan mensajes, no calidades de vídeo.")),
    page("Pieza 2", "Campañas de Meta y un formulario que filtra",
         p("Preguntas cerradas según tu sector: terreno, puesto, plazo, zona.")
         + p("Cada respuesta dice a quién llamar ya, a quién hoy y a quién no.")),
    page("Pieza 3", "Nuestro CRM, con IA",
         p("Cada contacto entra con sus respuestas y tu equipo recibe el aviso al momento.")
         + p("Del anuncio a la venta, en el mismo sitio.")),
    page("Pieza 4", "Un responsable de cuenta",
         p("Una persona que conoce tu negocio y a la que escribes cuando algo no cuadra.")
         + stats(stat("10", "perfiles detrás de tu cuenta"), stat("26", "días de implantación"))),
    page("Cómo cobramos", "Puesta en marcha y comisión sobre ventas",
         p("Cobramos la puesta en marcha y, desde ahí, una comisión sobre lo que vendes.")
         + say("Sin permanencia. Si no vendes, no tiene sentido que sigas.")),
    close('Anuncios, CRM y comercial, <em>conectados.</em>',
          "Si quieres saber si tu negocio encaja, escríbeme por privado y lo vemos en una llamada."),
]

# ------------------------------------------------------------------ C7
CARRUSELES["cuanto-pagar-por-un-cliente"] = [
    cover("Números",
          '¿Cuánto puedes pagar <em>por un cliente?</em>',
          "Tres datos y una cuenta. Hazla antes de apagar una campaña que te parece cara."),
    page("Dato 1", "Lo que ganas con cada venta",
         '<div class="formula">Ticket medio × margen = <b>beneficio por venta</b></div>'
         + p("Lo que te queda de cada venta después de materiales, horas y comisiones.")),
    page("Dato 2", "Lo que quieres guardar",
         '<div class="formula">Beneficio − lo que guardas = <b>máximo por cliente</b></div>'
         + p("Es lo máximo que puedes gastar en conseguir un cliente sin perder dinero. Esa línea la decides tú.")),
    page("Dato 3", "Tu tasa de cierre",
         '<div class="formula">Máximo por cliente × tasa de cierre = <b>máximo por contacto</b></div>'
         + p("Si de cada 100 contactos cierras 2, tu tasa es el 2 %.")),
    page("La cuenta", "Una empresa de casas modulares",
         f'<div class="ejrow">{ej()} Números inventados para enseñar la cuenta.</div>'
         + rows([("Ticket 100.000 € × margen 15 %", "<b>15.000 €</b>"),
                 ("15.000 € − 10.000 € que guarda", "<b>5.000 €</b> por cliente"),
                 ("5.000 € × 2 % de cierre", "<b>100 €</b> por contacto")])),
    page("Con datos reales", "Y lo que de verdad hemos pagado",
         stats(stat("6,64 €", "por contacto<br>casas modulares"), stat("20,13 €", "por contacto<br>casas modulares"))
         + p("Con la cuenta del ejemplo, los dos precios caben de sobra. Lo que decide si hay negocio es cuántos cierras.")),
    page("La palanca", "Si cierras el doble, puedes pagar el doble",
         p("Mejorar la llamada sube lo que puedes pagar por cada contacto.")
         + say("A veces el problema está en la llamada y no en el anuncio.")
         + p("Y te deja pujar por gente que tu competencia no puede pagar.")),
    close('Sin este número, cualquier precio <em>te parecerá caro.</em>',
          "Si quieres hacer la cuenta con tus datos, escríbeme por privado y la hacemos juntos."),
]

# ------------------------------------------------------------------ C8
CARRUSELES["guion-anuncio-alto-ticket"] = [
    cover("Guiones",
          'El guion de un anuncio para vender <em>algo caro</em>',
          "Seis bloques en menos de un minuto. Con ejemplos para una empresa de casas modulares."),
    page("Bloque 1 · Gancho", "Habla a quien ya tiene el problema",
         p("Los primeros segundos deciden si se queda. Nada de logos ni de «somos una empresa con experiencia».")
         + f'<div class="ejrow">{ej()}</div>'
         + say("¿Tienes terreno y no sabes cuánto costaría construir en él?")),
    page("Bloque 2 · Problema", "Con sus palabras, no con las tuyas",
         p("Cuenta lo que le pasa como lo contaría él en una cena.")
         + f'<div class="ejrow">{ej()}</div>'
         + say("Pides tres presupuestos y cada uno te da un precio y un plazo distintos.")),
    page("Bloque 3 · Prueba", "Algo que se pueda ver",
         p("Una obra terminada. Una demo de la pantalla. Una clase de muestra. Un cliente real, con su permiso.")
         + p("Nada de banco de imágenes. En alto ticket, la gente quiere ver que existes.")),
    page("Bloque 4 · Cómo funciona", "Tres pasos, no veinte",
         f'<div class="ejrow">{ej()}</div>'
         + rows([("1", "Nos cuentas tu terreno y tu idea"),
                 ("2", "Te damos precio y plazo cerrados"),
                 ("3", "Construimos y te entregamos la llave")])
         + p("Quien entiende el proceso, se imagina dentro.")),
    page("Bloque 5 · Para quién no es", "La frase que más filtra",
         f'<div class="ejrow">{ej()}</div>'
         + say("Si todavía no tienes terreno, guarda este vídeo para cuando lo tengas.")
         + p("Se va quien no encaja. Y quien sigue, se siente elegido.")),
    page("Bloque 6 · Siguiente paso", "Concreto y con precio",
         f'<div class="ejrow">{ej()}</div>'
         + say("Desde [precio]. Contesta cuatro preguntas y te llamamos hoy.")
         + p("Qué tiene que hacer, cuánto tarda y qué pasa después.")),
    page("Al grabar", "Tres ganchos para el mismo vídeo",
         p("Graba el cuerpo una vez y tres ganchos distintos: una pregunta, un error, un resultado.")
         + p("Deja que Meta te diga cuál retiene más. Luego graba más de ese tipo.")),
    close('En alto ticket, el anuncio <em>abre la llamada.</em> La venta viene después.',
          "Si quieres que revisemos el guion de tu próximo anuncio, escríbeme por privado."),
]

# ------------------------------------------------------------------ C9
CARRUSELES["preguntas-formulario-por-sector"] = [
    cover("Formularios de Meta",
          'Qué preguntar en el formulario <em>según lo que vendes</em>',
          "Constructoras y casas modulares, software, formación online y negocio local."),
    page("Las reglas", "Antes de escribir una pregunta",
         arr(["Opción múltiple, no texto libre.",
              "De 3 a 4 preguntas, más nombre y teléfono.",
              "Siempre una salida: «Solo estoy mirando».",
              "Si una respuesta no cambia lo que haces después, la pregunta sobra."])),
    page("Constructoras y casas modulares", "Terreno, plazo y cómo paga",
         arr(["¿Tienes ya terreno?",
              "¿Cuándo te gustaría empezar la obra?",
              "¿Cómo piensas pagarla? Fondos propios, hipoteca aprobada, sin pedir.",
              "¿Qué presupuesto manejas? Con tus rangos reales."])
         + note("Si solo construyes en ciertas zonas, añade la provincia.")),
    page("Software", "Quién decide y qué usa hoy",
         arr(["¿Cuál es tu puesto?",
              "¿Cuántas personas lo usarían?",
              "¿Cómo lo hacéis ahora? Excel, otra herramienta, papel.",
              "¿Cuándo queréis tenerlo funcionando?"])),
    page("Formación online", "Situación, dinero y tiempo",
         arr(["¿Qué te describe mejor ahora mismo? Con las palabras de tus alumnos.",
              "Si encaja contigo, ¿puedes invertir ahora? Sí / A plazos / Ahora no.",
              "¿Cuántas horas a la semana puedes dedicarle?"])),
    page("Negocio local", "Zona y urgencia",
         arr(["¿Qué servicio te interesa?",
              "¿Estás en [tu zona]? Sí / Cerca / Más lejos.",
              "¿Para cuándo lo necesitas? Esta semana / Este mes / Solo precios.",
              "¿Cómo prefieres que te contactemos? Llamada / WhatsApp."])),
    page("Después", "Cada respuesta, un color",
         opts("El semáforo", [
             ("v", "<b>Verde:</b> encaja en plazo, dinero y zona. Llamada en 5 minutos."),
             ("a", "<b>Ámbar:</b> le falta una pieza. Llamada hoy, más corta."),
             ("r", "<b>Rojo:</b> solo mira. WhatsApp con algo útil y recordatorio.")])),
    close('Las preguntas del formulario deciden <em>a quién llamas mañana.</em>',
          "¿Quieres que te digamos qué pregunta añadiríamos en tu caso? Escríbeme por privado."),
]

# ------------------------------------------------------------------ C10
CARRUSELES["por-que-15-20-anuncios"] = [
    cover("Anuncios en vídeo",
          'Por qué grabamos <em>entre 15 y 20 anuncios</em> y no uno muy bueno',
          "Lo que pasa cuando una campaña depende de un solo vídeo."),
    page("La verdad incómoda", "Nadie sabe qué gancho va a funcionar",
         p("Ni tú, ni tu agencia, ni nosotros.")
         + p("Se sabe probando. Y para probar hace falta tener con qué.")),
    page("Motivo 1", "El mismo mensaje, ganchos distintos",
         chips(["Pregunta que duele", "Error y corrección", "Resultado primero", "Oferta clara"])
         + p("Cuatro formas de empezar el mismo vídeo. Una retiene más que las otras. No sabes cuál hasta que la ves.")),
    page("Motivo 2", "No todos están en el mismo punto",
         p("Al que no te conoce le habla una pregunta que duele.")
         + p("Al que ya ha visto tres vídeos tuyos le basta una oferta clara.")),
    page("Motivo 3", "Cada objeción, su anuncio",
         rows([("Precio", "qué incluye y desde cuánto"),
               ("Plazo", "cuánto se tarda de verdad"),
               ("Confianza", "quién está detrás y qué ha hecho")])),
    page("Motivo 4", "Los anuncios se cansan",
         p("La misma gente ve el mismo vídeo una y otra vez. Deja de mirarlo.")
         + p("Con recambio grabado, cambias el anuncio en un día y no en un mes.")),
    page("Por qué en estudio", "Misma luz, mismo sonido",
         p("Si todos los vídeos tienen la misma calidad, comparas lo que dicen.")
         + say("Cuando un anuncio gana, sabes que es por el mensaje y no porque el otro se oyera mal.")),
    close('Un anuncio bueno es suerte. Quince <em>son un método.</em>',
          "¿Quieres saber qué ganchos probaríamos en tu sector? Escríbeme por privado."),
]
