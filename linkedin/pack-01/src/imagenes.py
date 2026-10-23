# -*- coding: utf-8 -*-
"""Imágenes 1080×1350 del pack 01: 6 posts de dato/contraste/checklist y 3 de «Comenta PALABRA»."""

IMG = """
html,body{width:1080px;height:1350px;overflow:hidden}
.p{position:relative;width:1080px;height:1350px;overflow:hidden;background:var(--ink);color:var(--cr)}
.top{position:absolute;top:64px;left:72px;right:72px;display:flex;align-items:center;justify-content:space-between}
.top img{width:60px;height:60px;filter:drop-shadow(0 0 22px rgba(255,106,26,.6))}
.top span{font:700 20px 'Mono';letter-spacing:.2em;text-transform:uppercase;color:var(--g1)}
.main{position:absolute;top:170px;left:72px;right:72px;bottom:150px;display:flex;flex-direction:column;overflow:hidden}
.tag{align-self:flex-start;font:700 20px 'Mono';letter-spacing:.22em;color:var(--or);border:2px solid var(--or);border-radius:8px;padding:8px 16px;margin-bottom:28px;text-transform:uppercase}
h1{font:800 HSIZEpx/1.0 'Bricolage';letter-spacing:-.035em}
h1 em{font-size:1.04em}
.sub{font-size:32px;line-height:1.38;color:var(--g1);margin-top:26px}
.foot{position:absolute;left:72px;right:72px;bottom:64px;display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid #2A2522;padding-top:24px;font:500 19px 'Mono';letter-spacing:.08em;color:var(--g2)}
.foot b{color:var(--cr)}
.ej{display:inline-block;font:700 18px 'Mono';letter-spacing:.16em;color:var(--or);border:2px solid var(--or);border-radius:6px;padding:4px 10px}
/* barras */
.bars{margin-top:auto}
.br{display:grid;grid-template-columns:280px 1fr;align-items:center;gap:24px;padding:20px 0;border-bottom:1.5px solid #2A2522}
.br .lb{font:600 28px/1.2 'Sans';color:var(--cr)}
.br .lb small{display:block;font:500 18px 'Mono';letter-spacing:.1em;color:var(--g2);text-transform:uppercase;margin-top:6px}
.br .tr{position:relative;height:58px;display:flex;align-items:center;gap:18px}
.br .fill{height:58px;background:var(--or);border-radius:0 6px 6px 0}
.br .v{font:800 44px 'Bricolage';letter-spacing:-.02em;color:var(--cr);white-space:nowrap}
.br.max .fill{background:var(--or)}
.br:not(.max) .fill{background:#C9480A}
/* checklist */
ul.ck{list-style:none;margin-top:24px;margin-bottom:24px}
ul.ck li{position:relative;padding:13px 0 13px 78px;font-size:33px;line-height:1.28;border-bottom:1.5px solid #2A2522}
ul.ck li:before{content:'';position:absolute;left:0;top:15px;width:44px;height:44px;border:3px solid var(--or);border-radius:10px}
ul.ck li:after{content:'';position:absolute;left:12px;top:21px;width:20px;height:11px;border-left:4px solid var(--or);border-bottom:4px solid var(--or);transform:rotate(-45deg)}
ul.ck li small{display:block;font-size:23px;color:var(--g2);margin-top:6px}
.verdict{margin-top:auto;background:var(--or);color:var(--ink);border-radius:20px;padding:28px 34px;font:800 38px/1.15 'Bricolage';letter-spacing:-.01em}
/* contraste */
.vs{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:auto}
.col{border-radius:24px;padding:36px 34px;background:#16130F;border:1.5px solid #2A2522}
.col.hot{background:var(--cr);color:var(--ink);border-color:var(--cr)}
.col h3{font:700 20px 'Mono';letter-spacing:.16em;text-transform:uppercase;color:var(--g2);margin-bottom:18px}
.col.hot h3{color:var(--or2)}
.col .big{font:800 50px/1.05 'Bricolage';letter-spacing:-.02em;margin-bottom:26px}
.col dl dt{font:700 18px 'Mono';letter-spacing:.14em;text-transform:uppercase;color:var(--g2);margin-top:22px}
.col dl dd{font-size:33px;line-height:1.3;margin-top:6px}
.col.hot dl dd{color:#2B2724}
/* timeline */
.tl{margin-top:auto}
.st{display:grid;grid-template-columns:230px 1fr;gap:30px;padding:30px 0;border-bottom:1.5px solid #2A2522;align-items:start}
.st .t{font:800 54px/1 'Bricolage';letter-spacing:-.02em}
.st .d{font-size:32px;line-height:1.35;color:var(--cr)}
.st .d small{display:block;font-family:'Serif';font-style:italic;font-size:38px;color:var(--or);margin-top:8px}
.st.s1 .t{color:var(--or)}.st.s2 .t{color:#D98A5A}.st.s3 .t{color:var(--g2)}
/* stats */
.sg{display:grid;grid-template-columns:1fr;gap:20px;margin-top:auto}
.sc{display:flex;align-items:baseline;gap:30px;border-bottom:1.5px solid #2A2522;padding:18px 0}
.sc b{font:800 150px/0.95 'Bricolage';letter-spacing:-.04em;color:var(--or);white-space:nowrap}
.sc span{font-size:34px;color:var(--g1);line-height:1.2}
/* coste */
.roles{margin-top:40px}
.roles div{display:flex;align-items:center;gap:22px;font-size:38px;padding:26px 0;border-bottom:1.5px solid #2A2522}
.roles div i{width:16px;height:16px;border-radius:50%;background:var(--g2);flex:none}
.box{margin-top:auto;background:var(--cr);color:var(--ink);border-radius:24px;padding:34px 38px}
.box .k{font:700 20px 'Mono';letter-spacing:.16em;text-transform:uppercase;color:var(--or2);margin-bottom:12px}
.box p{font:800 42px/1.12 'Bricolage';letter-spacing:-.02em}
.box p span{display:block;font:400 28px/1.35 'Sans';letter-spacing:0;color:#3A342F;margin-top:12px}
"""

GLOW = '<div class="glow"></div><div class="glow b"></div>'


def frame(base, logo, label, inner, hsize=96, foot_l="<b>Ceos Growth</b> · Burgos", foot_r=""):
    css = base + IMG.replace("HSIZE", str(hsize))
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="p">{GLOW}
<div class="top"><img src="{logo}"><span>{label}</span></div>
<div class="main" data-fit="main">{inner}</div>
<div class="foot"><span>{foot_l}</span><span>{foot_r}</span></div>
</div></body></html>'''


# ------------------------------------------------------------------ I1
def cinco_campanas(base, logo):
    data = [("Software", "Campaña 1", 1.92), ("Formación online", "Un mes normal", 2.09),
            ("Software", "Campaña 2", 3.36), ("Casas modulares", "Campaña 1", 6.64),
            ("Casas modulares", "Campaña 2", 20.13)]
    mx = max(v for *_, v in data)
    rows = ""
    for s, c, v in data:
        w = max(8, 380 * v / mx)
        val = f"{v:.2f}".replace(".", ",") + " €"
        cls = "br max" if v == mx else "br"
        rows += f'<div class="{cls}"><div class="lb">{s}<small>{c}</small></div><div class="tr"><div class="fill" style="width:{w:.0f}px"></div><div class="v">{val}</div></div></div>'
    inner = f'''<div class="tag">Datos reales</div>
<h1>De <em>1,92 €</em> a <em>20,13 €</em> por contacto</h1>
<p class="sub">Cinco campañas de Meta Ads que llevamos en Ceos Growth. Mismo equipo, sectores distintos.</p>
<div class="bars">{rows}</div>'''
    return frame(base, logo, "Coste por contacto", inner, hsize=96, foot_r="¿Cuánto pagas tú?")


# ------------------------------------------------------------------ I2
def checklist_formulario(base, logo):
    items = [("Tipo «Mayor intención»", "no «Más volumen», si vendes algo caro"),
             ("Un precio «desde» en la introducción", "quien no puede pagarlo se va solo"),
             ("Opción múltiple, no texto libre", "para ordenar contactos de un vistazo"),
             ("De 3 a 4 preguntas que filtran", "cada una cambia lo que haces después"),
             ("Una salida: «Solo estoy mirando»", "el curioso se identifica sin mentir"),
             ("Una promesa final que vas a cumplir", "«te llamamos hoy antes de las [hora]»")]
    lis = "".join(f"<li>{a}<small>{b}</small></li>" for a, b in items)
    inner = f'''<div class="tag">Checklist</div>
<h1>¿Tu formulario de Meta <em>filtra?</em></h1>
<ul class="ck">{lis}</ul>
<div class="verdict">Si te fallan dos, mañana llamarás a curiosos.</div>'''
    return frame(base, logo, "Formularios de Meta", inner, hsize=84, foot_r="Guárdalo para tu próxima campaña")


# ------------------------------------------------------------------ I3
def cuota_vs_comision(base, logo):
    inner = '''<div class="tag">Contraste</div>
<h1>Dime cómo cobra tu agencia y te diré <em>qué mira</em></h1>
<div class="vs">
 <div class="col"><h3>Cobra por contacto</h3><div class="big">Le sirve el contacto barato</div>
  <dl><dt>Te enseña</dt><dd>El coste por contacto y cuántos han entrado.</dd>
  <dt>No le toca</dt><dd>Si alguien los llama o si compran.</dd></dl></div>
 <div class="col hot"><h3>Cobra comisión</h3><div class="big">Le sirve el contacto que compra</div>
  <dl><dt>Te pregunta</dt><dd>Cuánto tardas en llamar y cuántos pasan a visita.</dd>
  <dt>Le toca</dt><dd>Todo el camino, del anuncio a la venta.</dd></dl></div>
</div>'''
    return frame(base, logo, "Opinión", inner, hsize=88, foot_r="Nosotros: puesta en marcha + comisión")


# ------------------------------------------------------------------ I4
def coste_por_tu_cuenta(base, logo):
    roles = ["Quien grabe y edite los anuncios", "Quien lleve las campañas de Meta Ads",
             "Quien siga cada contacto", "El CRM y las herramientas"]
    rs = "".join(f"<div><i></i>{r}</div>" for r in roles)
    inner = f'''<div class="tag">El coste que no se ve</div>
<h1>Montarlo por tu cuenta: <em>32.900 €</em> al año</h1>
<div class="roles">{rs}</div>
<div class="box"><div class="k">Con Ceos Growth</div><p>Puesta en marcha y comisión sobre ventas.<span>Sin permanencia. Implantación en 26 días, 15-20 anuncios grabados en estudio y 10 perfiles en tu cuenta.</span></p></div>'''
    return frame(base, logo, "Números", inner, hsize=96, foot_r="Cálculo de Ceos Growth")


# ------------------------------------------------------------------ I5
def cinco_minutos(base, logo):
    inner = '''<div class="tag">Tiempo de respuesta</div>
<h1>Lo que piensa un lead <em>mientras esperas</em></h1>
<div class="tl">
 <div class="st s1"><div class="t">5 min</div><div class="d">Aún tiene el móvil en la mano. Sabe qué pidió y por qué.<small>«Sí, sí, era yo.»</small></div></div>
 <div class="st s2"><div class="t">1 hora</div><div class="d">Está con otra cosa. Se acuerda si le recuerdas el anuncio.<small>«Ah, lo de la casa…»</small></div></div>
 <div class="st s3"><div class="t">Mañana</div><div class="d">Número desconocido en mitad de una reunión.<small>«¿Quién eres?»</small></div></div>
</div>'''
    return frame(base, logo, "Primera llamada", inner, hsize=96, foot_r="El anuncio ya hizo su parte")


# ------------------------------------------------------------------ I6
def formacion_mes_normal(base, logo):
    inner = '''<div class="tag">Caso real · Formación online</div>
<h1>Un mes <em>normal</em></h1>
<p class="sub">Sin récords. Una campaña de formación online gestionada por Ceos Growth.</p>
<div class="sg">
 <div class="sc"><b>28</b><span>contactos<br>en el mes</span></div>
 <div class="sc"><b>2,09 €</b><span>por<br>contacto</span></div>
 <div class="sc"><b>58,52 €</b><span>en<br>anuncios</span></div>
</div>'''
    return frame(base, logo, "Datos reales", inner, hsize=120, foot_r="Casi un contacto al día")


# ------------------------------------------------------------------ Comenta PALABRA
COMENTA_CSS = """
.h{position:absolute;top:170px;left:72px;right:72px}.h .tag{display:inline-block}
.mock{position:absolute;left:300px;top:MTOPpx;width:620px;transform:rotate(-5deg);transform-origin:top left}
.mock img{width:100%;display:block;border-radius:10px;box-shadow:0 40px 90px rgba(0,0,0,.7),0 0 0 1.5px rgba(255,106,26,.45),0 0 80px rgba(255,106,26,.18)}
.mock.back{left:600px;top:MBACKpx;transform:rotate(2deg)}
.mock.back img{filter:brightness(.9)}
.fade{position:absolute;left:0;right:0;bottom:0;height:360px;background:linear-gradient(180deg,rgba(10,9,8,0) 0%,rgba(10,9,8,.92) 45%,#0A0908 70%)}
.cta{position:absolute;left:72px;bottom:72px;right:72px;display:flex;align-items:center;gap:26px}
.pill{background:#FF6A1A;color:#0A0908;border-radius:999px;padding:26px 40px;font:800 44px 'Bricolage';letter-spacing:-.02em;box-shadow:0 20px 60px rgba(255,106,26,.35);white-space:nowrap}
.cta p{font-size:26px;line-height:1.3;color:#F2EDE7}
.cta p span{color:#B5ADA4}
.side{position:absolute;left:72px;top:SIDETOPpx;width:230px}
.side div{font:700 17px 'Mono';letter-spacing:.12em;text-transform:uppercase;color:#9C938B;padding:16px 0;border-top:1px solid #2A2522}
.side div b{display:block;font:800 30px 'Bricolage';letter-spacing:-.01em;text-transform:none;color:#F2EDE7;margin-bottom:4px}
"""


def comenta(palabra, h, side, hsize, mtop=600, mocks=("_p1", "_p2")):
    def fn(base, logo):
        prev = f"../../../boveda/src/_prev/{palabra.lower()}"
        css = (base + IMG.replace("HSIZE", str(hsize)) + COMENTA_CSS.replace("MTOP", str(mtop))
               .replace("MBACK", str(mtop + 10)).replace("SIDETOP", str(mtop + 40)))
        sd = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in side)
        return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="p"><div class="glow"></div><div class="glow b"></div>
<div class="top"><img src="{logo}"><span>Recurso gratis · PDF</span></div>
<div class="h" data-fit="h"><div class="tag">Bóveda Ceos</div><h1>{h}</h1></div>
<div class="side">{sd}</div>
<div class="mock back"><img src="{prev}/{mocks[1]}.png"></div>
<div class="mock"><img src="{prev}/{mocks[0]}.png"></div>
<div class="fade"></div><div class="cta"><div class="pill">Comenta {palabra}</div><p>y te lo mando<br><span>por privado</span></p></div>
</div></body></html>'''
    return fn


IMAGENES = {
    "cinco-campanas-cinco-precios": cinco_campanas,
    "checklist-formulario-que-filtra": checklist_formulario,
    "cuota-fija-o-comision": cuota_vs_comision,
    "32900-euros-por-tu-cuenta": coste_por_tu_cuenta,
    "5-minutos-1-hora-manana": cinco_minutos,
    "formacion-un-mes-normal-dato": formacion_mes_normal,
    "comenta-llamada-objeciones": comenta(
        "LLAMADA", '«Mándame la info <em>por email</em>»', [("7 objeciones", "respondidas"), ("5 preguntas", "en orden"), ("Guion", "palabra por palabra")], 100),
    "comenta-seguimiento-reactivar": comenta(
        "SEGUIMIENTO", 'El lead que no contestó <em>hace 3 meses</em>', [("Día 0 a 7", "5 mensajes"), ("30 y 90 días", "cómo reactivar"), ("4 nichos", "con variantes")], 96),
    "comenta-landing-prueba-10-minutos": comenta(
        "LANDING", 'La prueba de <em>10 minutos</em> antes de lanzar', [("20 puntos", "con cómo comprobarlo"), ("La prueba", "con tu móvil"), ("Si tienes 1 hora", "mira estos 5")], 90, mtop=650),
}
