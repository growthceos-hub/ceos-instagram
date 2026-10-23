# Encargo para la sesión de LinkedIn del PC (LinkedIn + Facebook)

Pégalo tal cual en la sesión «LinkedIn organic content strategy» del PC.

Material en el repo growthceos-hub/ceos-instagram (git pull): `linkedin/ALGORITMO-2026.md` (léelo primero), `linkedin/pack-01/` (30 posts: 10 carruseles PDF, 8 texto, 6 imagen, 3 encuestas, 3 «Comenta PALABRA», con `CALENDARIO.md`) y `boveda/` (6 PDF de «Comenta PALABRA»).

## LinkedIn
1. Programa el pack-01 en el orden de `CALENDARIO.md`, de lunes a viernes a las 13:00, del 26/10 al 4/12 (los 40 que ya hay siguen a las 8:30). Mejor desde el perfil personal de Hugo (≈6 veces más alcance que la página). Carruseles como documento PDF, imágenes con su PNG, encuestas con `encuesta.json`. Sin enlaces en el cuerpo.
2. 60-90 min después de publicar, responde a todos los comentarios con algo que aporte; vuelve a las 24 h.
3. Cada día laborable, 3-5 comentarios con sustancia (2-4 frases, experiencia propia) en posts recientes de dueños o directivos de constructoras/casas modulares, software y formación online de España, mejor en sus primeros 30 min. Lista de 30-50 cuentas objetivo, rotando.
4. «Comenta PALABRA» (posts 08, 18, 28 y los 6 de la bóveda): rondas a las 10:07 y 18:07. Respuesta pública distinta cada vez, privado con el PDF (`boveda/README.md`). Límites: máx. 10 invitaciones y 30 privados al día (~70 invitaciones/semana), con nota personal.

## Facebook (página Ceos Marketing, id 434829573050729)
5. Mismos contenidos adaptados (carrusel → post de varias imágenes, imagen con su PNG, encuestas como pregunta), uno al día a las 12:30, del 26/10 al 4/12. Vía Make (conexión id 14651824, modelo: escenario 9941497) con las URL raw del repo; programar con Graph API `published=false` + `scheduled_publish_time`.
6. Escenario de Make cada 15 min: comentarios nuevos de la página que contengan una palabra de la bóveda → respuesta pública «¡Te lo mando por privado!» + private reply por Messenger con el mensaje y el PDF de `boveda/README.md` (`POST /{page-id}/messages` con `recipient.comment_id`, permiso `pages_messaging`). Si falta permiso, avisa de qué reconectar. Probar con un comentario de prueba antes de activar.

No tocar Instagram. Al acabar, informar de lo programado en cada red y del estado de las dos automatizaciones.
