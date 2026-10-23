# -*- coding: utf-8 -*-
"""Genera la bóveda: boveda/<palabra>/recurso.pdf y post.png.

Uso: python3 boveda/src/build.py [PALABRA ...]
"""
import os
import subprocess
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # boveda/
sys.path.insert(0, HERE)
from contenido import RECURSOS  # noqa: E402

FS = "../../toolkit/node_modules/@fontsource"
LOGO = "../../toolkit/logo.png"

FONTS = f"""
@font-face{{font-family:'Bricolage';font-weight:800;src:url({FS}/bricolage-grotesque/files/bricolage-grotesque-latin-800-normal.woff2) format('woff2');}}
@font-face{{font-family:'Bricolage';font-weight:600;src:url({FS}/bricolage-grotesque/files/bricolage-grotesque-latin-600-normal.woff2) format('woff2');}}
@font-face{{font-family:'Serif';font-style:italic;font-weight:400;src:url({FS}/instrument-serif/files/instrument-serif-latin-400-italic.woff2) format('woff2');}}
@font-face{{font-family:'Sans';font-weight:400;src:url({FS}/instrument-sans/files/instrument-sans-latin-400-normal.woff2) format('woff2');}}
@font-face{{font-family:'Sans';font-weight:600;src:url({FS}/instrument-sans/files/instrument-sans-latin-600-normal.woff2) format('woff2');}}
@font-face{{font-family:'Sans';font-weight:700;src:url({FS}/instrument-sans/files/instrument-sans-latin-700-normal.woff2) format('woff2');}}
@font-face{{font-family:'Mono';font-weight:500;src:url({FS}/jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2) format('woff2');}}
@font-face{{font-family:'Mono';font-weight:700;src:url({FS}/jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2) format('woff2');}}
"""

CSS = FONTS + """
:root{--ink:#0A0908;--or:#FF6A1A;--or2:#C9480A;--cr:#F2EDE7;--g1:#B5ADA4;--g2:#9C938B;--line:#DCD3C8;--card:#FBF8F4;}
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--ink)}
body{font-family:'Sans';color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;break-after:page;background:var(--cr)}
.page:last-child{page-break-after:auto}
.hdr{position:absolute;top:0;left:0;right:0;height:16mm;padding:0 16mm;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line)}
.hdr .l{display:flex;align-items:center;gap:3mm;font:500 7.5pt 'Mono';letter-spacing:.12em;text-transform:uppercase;color:var(--g2)}
.hdr img{width:6mm;height:6mm}
.hdr .r{font:700 7.5pt 'Mono';letter-spacing:.14em;color:var(--or2)}
.ftr{position:absolute;bottom:0;left:0;right:0;height:13mm;padding:0 16mm;display:flex;align-items:center;justify-content:space-between;font:500 7.5pt 'Mono';letter-spacing:.08em;color:var(--g2);border-top:1px solid var(--line)}
.ftr b{color:var(--ink);font-weight:700}
.body{position:absolute;top:22mm;bottom:19mm;left:16mm;right:16mm;overflow:hidden}
.kicker{font:700 7.5pt 'Mono';letter-spacing:.16em;text-transform:uppercase;color:var(--or2);margin-bottom:2mm}
h2{font:800 21pt/1.05 'Bricolage';letter-spacing:-.02em;margin-bottom:3.5mm}
h2.sm{font-size:15pt;margin-bottom:3mm}
h2 em,h1 em{font-family:'Serif';font-style:italic;font-weight:400;color:var(--or2);letter-spacing:0}
h3{font:600 10.5pt/1.2 'Bricolage';margin-bottom:1.2mm}
p{font-size:9.4pt;line-height:1.45}
.lead{font-size:10.6pt;line-height:1.45;color:#2B2724;margin-bottom:5mm;max-width:165mm}
.small{font-size:8.4pt;color:#5A524B;margin-top:2.5mm;line-height:1.45}
b{font-weight:700}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3mm}
.grid2.tight{margin-top:3mm}
.card{background:var(--card);border:1px solid var(--line);border-radius:3mm;padding:4mm 4.5mm}
.card p{font-size:8.9pt}
.card .n{font:800 13pt 'Bricolage';color:var(--or);margin-bottom:1.5mm}
.card.warn{border-left:2.2mm solid var(--or);margin-top:3mm}
table.obj td{padding:1.6mm 2.4mm}
.note{background:#fff;border-left:1.6mm solid var(--or);padding:3mm 4mm;font-size:9pt;line-height:1.45;margin-top:4mm;border-radius:0 2mm 2mm 0}
.say{font-family:'Serif';font-style:italic;font-size:12.5pt;line-height:1.3;color:var(--ink);background:#fff;border-left:1.6mm solid var(--or);padding:2.6mm 4mm;margin:1.8mm 0;border-radius:0 2mm 2mm 0}
.card .say{font-size:11pt}
.sema{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3mm}
.sema>div{background:var(--card);border:1px solid var(--line);border-radius:3mm;padding:3.5mm 4mm;font-size:10pt}
.sema p{font-size:8.7pt;margin-top:1.2mm}
.dot{display:inline-block;width:2.6mm;height:2.6mm;border-radius:50%;margin-right:1.5mm;vertical-align:-.2mm}
.dot.v{background:#2F8A57}.dot.a{background:#E0A100}.dot.r{background:#C8372D}
table.t{width:100%;border-collapse:collapse;font-size:8.6pt;line-height:1.4}
table.t th{font:700 7pt 'Mono';letter-spacing:.12em;text-transform:uppercase;color:var(--g2);text-align:left;padding:1.6mm 2.4mm;border-bottom:1.5px solid var(--ink)}
table.t td{padding:2mm 2.4mm;border-bottom:1px solid var(--line);vertical-align:top}
table.q td{font-size:8.4pt}
ul.ops{list-style:none}
ul.ops li{padding-left:3.4mm;position:relative;margin-bottom:.6mm}
ul.ops li:before{content:'';position:absolute;left:0;top:1.1mm;width:1.6mm;height:1.6mm;border:1px solid var(--g2);border-radius:50%}
ul.x,ul.check{list-style:none}
ul.x li,ul.check li{position:relative;padding-left:7mm;font-size:9.2pt;line-height:1.45;margin-bottom:2.4mm}
ul.x li:before{content:'×';position:absolute;left:0;top:-.6mm;font:800 12pt 'Bricolage';color:var(--or2)}
ul.check li:before{content:'';position:absolute;left:0;top:.6mm;width:3.6mm;height:3.6mm;border:1.4px solid var(--ink);border-radius:.8mm}
ol.steps{list-style:none;counter-reset:s}
ol.steps>li{counter-increment:s;position:relative;padding-left:11mm;margin-bottom:3.4mm}
ol.steps>li:before{content:counter(s);position:absolute;left:0;top:-.5mm;width:7.5mm;height:7.5mm;border-radius:50%;background:var(--ink);color:var(--or);font:800 11pt/7.5mm 'Bricolage';text-align:center}
ol.steps.compact>li{margin-bottom:2.6mm}
ol.steps li p{font-size:8.9pt}
ol.steps.guia li{margin-bottom:4.2mm}
.err{color:#7A3A1A;margin-top:1mm}
/* seguimiento */
.day{margin-top:5mm}
.dh{display:flex;align-items:baseline;gap:3mm;margin-bottom:2mm}
.dn{font:800 15pt 'Bricolage';color:var(--or2)}
.dt{font:600 12pt 'Bricolage'}
.dw{margin-left:auto;font:500 7.5pt 'Mono';letter-spacing:.1em;text-transform:uppercase;color:var(--g2)}
.chat{background:#E7DED3;border-radius:3mm;padding:3mm 4mm}
.bubble{background:#fff;border-radius:2.5mm 2.5mm 2.5mm .6mm;padding:2.6mm 3.6mm;font-size:9.6pt;line-height:1.45;max-width:150mm;box-shadow:0 .3mm .6mm rgba(0,0,0,.08)}
table.var{margin-top:1.5mm}
table.var td{padding:1.4mm 2.4mm;font-size:8.5pt}
td.nk{width:24mm;font:700 7pt 'Mono';letter-spacing:.08em;text-transform:uppercase;color:var(--or2);padding-top:2mm!important}
/* landing */
ol.cl{list-style:none}
ol.cl li{display:grid;grid-template-columns:6mm 9mm 1fr;align-items:start;padding:2.2mm 0;border-bottom:1px solid var(--line)}
ol.cl .box{width:4.2mm;height:4.2mm;border:1.5px solid var(--ink);border-radius:.8mm;margin-top:.4mm}
ol.cl .num{font:800 11pt 'Bricolage';color:var(--or2)}
ol.cl b{font-size:10pt}
ol.cl p{font-size:8.7pt;color:#3A342F;margin-top:.5mm}
/* ganchos */
.cat{margin-bottom:6mm}
.ch{display:flex;align-items:baseline;gap:3mm;border-bottom:1.5px solid var(--ink);padding-bottom:1.6mm;margin-bottom:2mm}
.ci{font:800 18pt 'Bricolage';color:var(--or)}
.ch h3{font:800 15pt 'Bricolage';margin:0}
.cu{margin-left:auto;font:700 7pt 'Mono';letter-spacing:.12em;text-transform:uppercase;color:var(--g2)}
ol.hk{list-style:none}
ol.hk li{font-size:10pt;line-height:1.35;padding:1.5mm 0 1.5mm 10mm;position:relative;border-bottom:1px dashed var(--line)}
.hn{position:absolute;left:0;top:1.9mm;font:700 7.5pt 'Mono';color:var(--or2)}
.cej{font-family:'Serif';font-style:italic;font-size:11pt;margin-top:2mm;color:#3A342F}
.ej{display:inline-block;font:700 6.8pt 'Mono';font-style:normal;letter-spacing:.14em;color:var(--or2);border:1.2px solid var(--or2);border-radius:1mm;padding:.5mm 1.4mm;vertical-align:1px}
/* numeros */
.f{display:flex;gap:3.5mm;align-items:center;background:#fff;border:1px solid var(--line);border-radius:2.5mm;padding:2.6mm 4mm;margin-bottom:2mm}
.fl{font:800 14pt 'Bricolage';color:var(--or);width:6mm}
.f b{display:block;font-size:9.4pt}
code{font:500 9pt 'Mono';color:#3A342F}
code.in{font-size:8.4pt}
table.sheet td{font-size:9.6pt;padding:3mm 2.4mm}
td.blank{width:42mm;border-bottom:1.5px solid var(--ink)!important}
td.blank.hl{background:#FFE5D6}
td.u{width:8mm;font:500 9pt 'Mono';color:var(--g2)}
table.cost td.blank{width:45mm}
tr.tot td{border-bottom:none;font-size:10.5pt}
.ejbox{margin-top:6mm;border:1.5px dashed var(--or2);border-radius:3mm;padding:4mm 5mm;background:#fff}
.ejh{display:flex;gap:2.5mm;align-items:center;margin-bottom:2.4mm;font-size:8.4pt;color:#5A524B}
.ejbox .ej{font-size:9pt;padding:.8mm 2mm}
table.mini td{font-size:9.2pt;padding:1.8mm 2.4mm}
.big{margin-top:6mm;background:var(--ink);color:var(--cr);border-radius:3mm;padding:6mm 7mm;display:flex;gap:7mm;align-items:center}
.bn{font:800 32pt 'Bricolage';color:var(--or);white-space:nowrap;letter-spacing:-.02em}
.bn span{font:400 14pt 'Serif';font-style:italic;color:var(--g1);margin-left:1mm}
.big p{color:var(--cr);font-size:10pt}
/* portada y cierre */
.dark{background:var(--ink);color:var(--cr)}
.glow{position:absolute;width:150mm;height:150mm;border-radius:50%;background:radial-gradient(circle,rgba(255,106,26,.28),rgba(255,106,26,0) 65%);top:-55mm;left:-45mm}
.glow.b{top:auto;bottom:-80mm;left:auto;right:-60mm;background:radial-gradient(circle,rgba(255,106,26,.16),rgba(255,106,26,0) 65%)}
.cv{position:absolute;inset:0;padding:18mm 18mm 16mm;display:flex;flex-direction:column}
.cv .top{display:flex;align-items:center;justify-content:space-between}
.cv .logo{width:16mm;height:16mm;filter:drop-shadow(0 0 6mm rgba(255,106,26,.55))}
.cv .lbl{font:700 7.5pt 'Mono';letter-spacing:.18em;text-transform:uppercase;color:var(--g1)}
.cv .word{margin-top:34mm;font:700 9pt 'Mono';letter-spacing:.3em;color:var(--or)}
.cv h1{font:800 52pt/0.98 'Bricolage';letter-spacing:-.03em;margin-top:5mm;color:var(--cr)}
.cv h1 em{color:var(--or);font-size:1.04em}
.cv .sub{font-size:12pt;line-height:1.45;color:var(--g1);margin-top:7mm;max-width:150mm}
.cv .in{margin-top:auto;border-top:1px solid #2A2522;padding-top:6mm}
.cv .in .k{font:700 7.5pt 'Mono';letter-spacing:.18em;text-transform:uppercase;color:var(--g2);margin-bottom:3mm}
.cv .in ol{list-style:none;counter-reset:i;columns:2;column-gap:10mm}
.cv .in li{counter-increment:i;font-size:9.6pt;line-height:1.4;color:var(--cr);padding:1.4mm 0 1.4mm 8mm;position:relative;break-inside:avoid}
.cv .in li:before{content:counter(i,decimal-leading-zero);position:absolute;left:0;top:1.9mm;font:700 7.5pt 'Mono';color:var(--or)}
.cv .foot{margin-top:7mm;display:flex;justify-content:space-between;font:500 7.5pt 'Mono';letter-spacing:.1em;color:var(--g2)}
.cv .foot b{color:var(--cr)}
.end h1{font-size:46pt;margin-top:40mm}
.wm{position:absolute;right:-30mm;top:95mm;width:130mm;opacity:.06}
.end .sub{font-size:13pt}
.end .cta{margin-top:12mm;display:inline-flex;align-items:center;gap:4mm;background:var(--or);color:var(--ink);border-radius:30mm;padding:5mm 9mm;font:800 15pt 'Bricolage';align-self:flex-start}
.end .facts{margin-top:auto;display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;border-top:1px solid #2A2522;padding-top:6mm}
.end .facts div{font-size:9pt;line-height:1.4;color:var(--g1)}
.end .facts b{display:block;font:800 15pt 'Bricolage';color:var(--cr);margin-bottom:1mm}
"""


def cover(r, total):
    lis = "".join(f"<li>{x}</li>" for x in r["dentro"])
    return f'''
<section class="page dark"><div class="glow"></div><div class="glow b"></div><img class="wm" src="{LOGO}">
<div class="cv">
  <div class="top"><img class="logo" src="{LOGO}"><span class="lbl">Bóveda Ceos Growth · Recurso gratuito</span></div>
  <div class="word">{r["palabra"]}</div>
  <h1>{r["titulo"]}</h1>
  <p class="sub">{r["subtitulo"]}</p>
  <div class="in"><div class="k">Qué hay dentro</div><ol>{lis}</ol></div>
  <div class="foot"><span><b>Ceos Growth</b> · ceosgrowth.com</span><span>1 / {total}</span></div>
</div></section>'''


def closing(total):
    return f'''
<section class="page dark end"><div class="glow"></div>
<div class="cv">
  <div class="top"><img class="logo" src="{LOGO}"><span class="lbl">Ceos Growth · Burgos</span></div>
  <h1>¿Quieres que lo montemos <em>contigo?</em></h1>
  <p class="sub">Somos una agencia de Meta Ads que trabaja con constructoras, casas modulares, software, formación online y negocio local. Montamos el sistema completo: anuncios, formulario, CRM y seguimiento.</p>
  <div class="cta">Solo cobramos si vendes</div>
  <p class="sub" style="margin-top:6mm;color:var(--cr)">Reserva una llamada en <b style="color:var(--or)">ceosgrowth.com/#agendar</b></p>
  <div class="facts">
    <div><b>+17</b>clientes activos</div>
    <div><b>26 días</b>de implantación</div>
    <div><b>10</b>perfiles en el equipo</div>
    <div><b>Comisión</b>sobre ventas</div>
  </div>
  <div class="foot"><span><b>Ceos Growth</b> · ceosgrowth.com</span><span>{total} / {total}</span></div>
</div></section>'''


def content_page(r, body, n, total):
    return f'''
<section class="page">
<div class="hdr"><div class="l"><img src="{LOGO}">Bóveda Ceos Growth</div><div class="r">{r["palabra"]}</div></div>
<div class="body">{body}</div>
<div class="ftr"><span><b>Ceos Growth</b> · ceosgrowth.com</span><span>{n} / {total}</span></div>
</section>'''


def html_for(r):
    total = len(r["paginas"]) + 2
    pages = [cover(r, total)]
    for i, b in enumerate(r["paginas"]):
        pages.append(content_page(r, b, i + 2, total))
    pages.append(closing(total))
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{r["palabra"]}</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'


CHECK_JS = """() => [...document.querySelectorAll('.page')].map((p,i)=>{
  const b=p.querySelector('.body')||p.querySelector('.cv');
  return {page:i+1, over:b.scrollHeight-b.clientHeight};
})"""

POST_CSS = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;background:#0A0908;overflow:hidden}
.p{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Sans';color:#F2EDE7}
.glow{position:absolute;width:1100px;height:1100px;border-radius:50%;background:radial-gradient(circle,rgba(255,106,26,.30),rgba(255,106,26,0) 62%);right:-420px;top:380px}
.glow2{position:absolute;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(255,106,26,.18),rgba(255,106,26,0) 65%);left:-300px;top:-300px}
.top{position:absolute;top:64px;left:72px;right:72px;display:flex;align-items:center;justify-content:space-between}
.top img{width:64px;height:64px;filter:drop-shadow(0 0 22px rgba(255,106,26,.6))}
.top span{font:700 20px 'Mono';letter-spacing:.2em;text-transform:uppercase;color:#B5ADA4}
.h{position:absolute;top:170px;left:72px;right:72px}
.tag{display:inline-block;font:700 20px 'Mono';letter-spacing:.22em;color:#FF6A1A;border:2px solid #FF6A1A;border-radius:8px;padding:8px 16px;margin-bottom:26px}
h1{font:800 HSIZEpx/0.98 'Bricolage';letter-spacing:-.035em}
h1 em{font-family:'Serif';font-style:italic;font-weight:400;color:#FF6A1A;letter-spacing:-.01em}
.mock{position:absolute;left:300px;top:MTOPpx;width:620px;transform:rotate(-5deg);transform-origin:top left}
.mock img{width:100%;display:block;border-radius:10px;box-shadow:0 40px 90px rgba(0,0,0,.7),0 0 0 1.5px rgba(255,106,26,.45),0 0 80px rgba(255,106,26,.18)}
.mock.back{left:600px;top:MBACKpx;transform:rotate(2deg);opacity:1}
.fade{position:absolute;left:0;right:0;bottom:0;height:360px;background:linear-gradient(180deg,rgba(10,9,8,0) 0%,rgba(10,9,8,.92) 45%,#0A0908 70%)}
.mock.back img{filter:brightness(.9)}
.cta{position:absolute;left:72px;bottom:72px;right:72px;display:flex;align-items:center;gap:26px}
.pill{background:#FF6A1A;color:#0A0908;border-radius:999px;padding:26px 40px;font:800 44px 'Bricolage';letter-spacing:-.02em;box-shadow:0 20px 60px rgba(255,106,26,.35);white-space:nowrap}
.cta p{font-size:26px;line-height:1.3;color:#F2EDE7}
.cta p span{color:#B5ADA4}
.side{position:absolute;left:72px;top:SIDETOPpx;width:230px}
.side div{font:700 17px 'Mono';letter-spacing:.12em;text-transform:uppercase;color:#9C938B;padding:16px 0;border-top:1px solid #2A2522}
.side div b{display:block;font:800 30px 'Bricolage';letter-spacing:-.01em;text-transform:none;color:#F2EDE7;margin-bottom:4px}
"""

POSTS = {
    "FORMULARIO": dict(h='El formulario que <em>filtra curiosos</em>', size=104, side=[("4 nichos", "preguntas exactas"), ("Semáforo", "a quién llamar"), ("PDF", "6 páginas")]),
    "LLAMADA": dict(h='Qué decir en la <em>primera llamada</em> a un lead', size=96, side=[("5 preguntas", "en orden"), ("7 objeciones", "respondidas"), ("Guion", "palabra por palabra")]),
    "SEGUIMIENTO": dict(h='5 WhatsApp para el lead que <em>no contesta</em>', size=98, side=[("Día 0 a 7", "listos para copiar"), ("4 nichos", "con variantes"), ("PDF", "5 páginas")]),
    "LANDING": dict(h='20 cosas que revisar <em>antes de lanzar</em> anuncios', size=94, side=[("20 puntos", "con cómo comprobarlo"), ("Legal", "y técnica"), ("Prueba", "de 10 minutos")]),
    "GANCHOS": dict(h='36 ganchos para tus <em>anuncios en vídeo</em>', size=104, side=[("6 tipos", "cuándo usar cada uno"), ("36", "plantillas"), ("Bonus", "guía de grabación")]),
    "NUMEROS": dict(h='¿Cuánto puedes pagar <em>por un lead?</em>', size=106, side=[("5 fórmulas", "paso a paso"), ("Hoja", "para rellenar"), ("Ejemplo", "resuelto")]),
}


def post_html(palabra, cfg, d):
    css = (POST_CSS.replace("HSIZE", str(cfg["size"])).replace("MTOP", str(cfg.get("mtop", 560)))
           .replace("MBACK", str(cfg.get("mtop", 560) + 10)).replace("SIDETOP", str(cfg.get("mtop", 560) + 40)))
    side = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in cfg["side"])
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="p"><div class="glow2"></div><div class="glow"></div>
<div class="top"><img src="../../toolkit/logo.png"><span>Recurso gratis · PDF</span></div>
<div class="h"><div class="tag">BÓVEDA CEOS</div><h1>{cfg["h"]}</h1></div>
<div class="side">{side}</div>
<div class="mock back"><img src="{d}/_p2.png"></div>
<div class="mock"><img src="{d}/_p1.png"></div>
<div class="fade"></div><div class="cta"><div class="pill">Comenta {palabra}</div><p>y te lo mando<br><span>por privado 👇</span></p></div>
</div></body></html>'''


def main(only):
    with sync_playwright() as p:
        br = p.chromium.launch()
        for r in RECURSOS:
            pal = r["palabra"]
            if only and pal not in only:
                continue
            d = os.path.join(ROOT, pal.lower())
            os.makedirs(d, exist_ok=True)
            src = os.path.join(HERE, f"{pal.lower()}.html")
            open(src, "w", encoding="utf-8").write(html_for(r))
            page = br.new_page()
            page.goto("file://" + src)
            page.wait_for_load_state("networkidle")
            page.evaluate("document.fonts.ready")
            res = page.evaluate(CHECK_JS)
            bad = [x for x in res if x["over"] > 0]
            print(pal, "páginas:", len(res), "DESBORDA:" if bad else "ok", bad if bad else "")
            pdf = os.path.join(d, "recurso.pdf")
            page.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True)
            page.close()
            # miniaturas para revisar y para el mockup
            prev = os.path.join(HERE, "_prev", pal.lower())
            os.makedirs(prev, exist_ok=True)
            subprocess.run(["pdftoppm", "-png", "-r", "70", pdf, os.path.join(prev, "p")], check=True)
            subprocess.run(["pdftoppm", "-png", "-r", "110", "-f", "1", "-l", "2", pdf, os.path.join(prev, "m")], check=True)
            ms = sorted(f for f in os.listdir(prev) if f.startswith("m-"))
            os.replace(os.path.join(prev, ms[0]), os.path.join(prev, "_p1.png"))
            os.replace(os.path.join(prev, ms[1]), os.path.join(prev, "_p2.png"))
            # post
            ph = os.path.join(HERE, f"post-{pal.lower()}.html")
            open(ph, "w", encoding="utf-8").write(post_html(pal, POSTS[pal], f"_prev/{pal.lower()}"))
            pg = br.new_page(viewport={"width": 1080, "height": 1350})
            pg.goto("file://" + ph)
            pg.wait_for_load_state("networkidle")
            pg.evaluate("document.fonts.ready")
            pg.screenshot(path=os.path.join(d, "post.png"))
            pg.close()
        br.close()


if __name__ == "__main__":
    main(set(a.upper() for a in sys.argv[1:]))
