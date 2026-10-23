# -*- coding: utf-8 -*-
"""Genera el pack 01 de LinkedIn: carruseles PDF (1080×1350), portadas e imágenes.

Uso (desde la raíz del repo, con nice porque hay una cola de vídeo):
    nice -n 19 python3 linkedin/pack-01/src/build.py            # todo
    nice -n 19 python3 linkedin/pack-01/src/build.py carruseles  # solo PDF
    nice -n 19 python3 linkedin/pack-01/src/build.py imagenes    # solo PNG
    nice -n 19 python3 linkedin/pack-01/src/build.py <slug>      # una pieza

Reutiliza el sistema de boveda/src/build.py: mismas fuentes de toolkit/, misma
paleta, Playwright para PDF y capturas. El texto de cada post está en textos.py.
"""
import json
import os
import subprocess
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(HERE)  # linkedin/pack-01/
REPO = os.path.dirname(os.path.dirname(PACK))
sys.path.insert(0, HERE)
from carruseles import CARRUSELES  # noqa: E402
from imagenes import IMAGENES  # noqa: E402
from textos import ORDEN, TEXTOS, ENCUESTAS  # noqa: E402

FS = "../../../toolkit/node_modules/@fontsource"
LOGO = "../../../toolkit/logo.png"
PREV = os.path.join(HERE, "_prev")
SHEETS = os.environ.get("SHEETS", "/tmp/claude-0/-home-user/c60365fe-b5b6-5375-a77c-5447aa466621/scratchpad/sheets")
os.makedirs(SHEETS, exist_ok=True)

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

BASE = FONTS + """
:root{--ink:#0A0908;--or:#FF6A1A;--or2:#C9480A;--cr:#F2EDE7;--g1:#B5ADA4;--g2:#9C938B;--line:#DCD3C8;--card:#FBF8F4;}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--ink)}
body{font-family:'Sans';color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
em{font-family:'Serif';font-style:italic;font-weight:400;color:var(--or);letter-spacing:-.005em}
.glow{position:absolute;width:1200px;height:1200px;border-radius:50%;background:radial-gradient(circle,rgba(255,106,26,.30),rgba(255,106,26,0) 62%);left:-520px;top:-560px}
.glow.b{left:auto;top:auto;right:-560px;bottom:-640px;background:radial-gradient(circle,rgba(255,106,26,.20),rgba(255,106,26,0) 62%)}
.wm{position:absolute;right:-170px;top:430px;width:720px;opacity:.06}
.arrow{display:inline-block;margin-right:8px;width:34px;height:3px;background:currentColor;position:relative;vertical-align:middle;margin-left:14px}
.arrow:after{content:'';position:absolute;right:-1px;top:-7px;width:14px;height:14px;border-top:3px solid currentColor;border-right:3px solid currentColor;transform:rotate(45deg)}
"""

DECK = BASE + """
@page{size:1080px 1350px;margin:0}
.pg{width:1080px;height:1350px;position:relative;overflow:hidden;page-break-after:always;break-after:page;background:var(--cr)}
.pg:last-child{page-break-after:auto}
.pg.dark{background:var(--ink);color:var(--cr)}
.hd{position:absolute;top:0;left:0;right:0;height:120px;padding:0 80px;display:flex;align-items:center;justify-content:space-between}
.hd .l{display:flex;align-items:center;gap:18px;font:700 20px 'Mono';letter-spacing:.16em;text-transform:uppercase;color:var(--g2)}
.hd img{width:46px;height:46px}
.hd .r{font:700 22px 'Mono';letter-spacing:.14em;color:var(--or2)}
.dark .hd .l{color:var(--g1)}
.dark .hd img{filter:drop-shadow(0 0 18px rgba(255,106,26,.6))}
.dark .hd .r{color:var(--or)}
.bar{position:absolute;left:80px;right:80px;bottom:64px;height:6px;background:rgba(10,9,8,.10);border-radius:3px;overflow:hidden}
.dark .bar{background:rgba(242,237,231,.12)}
.bar i{display:block;height:100%;background:var(--or);border-radius:3px}
.ft{position:absolute;left:80px;right:80px;bottom:92px;display:flex;justify-content:space-between;font:500 19px 'Mono';letter-spacing:.1em;color:var(--g2)}
.ft b{color:var(--ink)}
.dark .ft b{color:var(--cr)}
.bd{position:absolute;top:150px;left:80px;right:80px;bottom:150px;overflow:hidden;display:flex;flex-direction:column;justify-content:center}
.kick{font:700 24px 'Mono';letter-spacing:.18em;text-transform:uppercase;color:var(--or2);margin-bottom:22px}
h2{font:800 96px/1.0 'Bricolage';letter-spacing:-.035em;margin-bottom:56px}
h2 em{color:var(--or2)}
.txt{font-size:46px;line-height:1.34;color:#2B2724;margin-bottom:34px}
.txt b{color:var(--ink)}
.say{font-family:'Serif';font-style:italic;font-size:56px;line-height:1.18;background:#fff;border-left:12px solid var(--or);padding:30px 38px;border-radius:0 18px 18px 0;margin:6px 0 32px}
.note{font:500 25px/1.5 'Mono';color:var(--g2);margin-top:20px;padding-top:20px;border-top:1.5px solid var(--line)}
.stats{display:grid;gap:22px;margin-bottom:40px}
.stat{background:var(--ink);color:var(--cr);border-radius:22px;padding:34px 34px 30px}
.stat .b{font:800 112px/1 'Bricolage';color:var(--or);letter-spacing:-.03em;white-space:nowrap}
.stats[style*="repeat(3"] .stat .b{font-size:76px}
.stat .l{font-size:32px;line-height:1.3;color:var(--g1);margin-top:14px}
.stat .l b{color:var(--cr)}
ul.arr{list-style:none}
ul.arr li{position:relative;padding:26px 0 26px 64px;font-size:42px;line-height:1.3;border-bottom:1.5px solid var(--line)}
ul.arr li:before{content:'';position:absolute;left:0;top:50px;width:30px;height:3px;background:var(--or)}
ul.arr li:after{content:'';position:absolute;left:18px;top:44px;width:12px;height:12px;border-top:3px solid var(--or);border-right:3px solid var(--or);transform:rotate(45deg)}
.q .qq{font:600 46px/1.22 'Bricolage';margin-bottom:30px}
ul.opts{list-style:none}
ul.opts li{background:#fff;border:1.5px solid var(--line);border-radius:18px;padding:30px 32px 30px 84px;font-size:40px;line-height:1.3;margin-bottom:18px;position:relative}
.dot{position:absolute;left:32px;top:42px;width:28px;height:28px;border-radius:50%;background:var(--g1)}
.dot.v{background:#2F8A57}.dot.a{background:#E0A100}.dot.r{background:#C8372D}
.chips{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:40px}
.chips span{background:var(--ink);color:var(--cr);border-radius:999px;padding:20px 34px;font:600 38px 'Sans'}
table.rows{width:100%;border-collapse:collapse;margin-bottom:36px}
table.rows td{padding:32px 10px 32px 0;border-bottom:1.5px solid var(--line);font-size:40px;line-height:1.3;vertical-align:top}
table.rows tr:first-child td{border-top:2.5px solid var(--ink)}
table.rows td:first-child{font-weight:600;padding-right:28px}
table.rows td:last-child{color:#3A342F}table.rows td b{white-space:nowrap}
table.rows td b{color:var(--or2);font:800 46px 'Bricolage'}
.ej{display:inline-block;font:700 22px 'Mono';letter-spacing:.16em;color:var(--or2);border:2.5px solid var(--or2);border-radius:8px;padding:6px 14px}
.ejrow{display:flex;align-items:center;gap:18px;font-size:30px;color:#5A524B;margin-bottom:26px}
.formula{background:var(--ink);color:var(--cr);border-radius:22px;padding:44px 44px;font:600 54px/1.25 'Bricolage';margin-bottom:40px}
.formula b{color:var(--or);font-weight:800}
.bignum{font:800 300px/0.9 'Bricolage';color:var(--or);letter-spacing:-.04em;margin:-10px 0 30px}
/* portada */
.cv{position:absolute;top:150px;left:80px;right:80px;bottom:150px;display:flex;flex-direction:column}
.cv .kick{color:var(--or);margin-top:auto}
.cv h1{font:800 HSIZEpx/0.98 'Bricolage';letter-spacing:-.035em;color:var(--cr)}
.cv h1 em{font-size:1.04em}
.cv .sub{font-size:42px;line-height:1.36;color:var(--g1);margin-top:44px;max-width:880px}
.cv .sw{margin-top:auto;margin-bottom:0;display:flex;align-items:center;justify-content:space-between;border-top:1.5px solid #2A2522;padding-top:30px}
.cv .sw span{font:700 22px 'Mono';letter-spacing:.18em;text-transform:uppercase;color:var(--g1)}
.cv .sw .go{color:var(--or)}
/* cierre */
.end h1{font:800 84px/1.0 'Bricolage';letter-spacing:-.03em;color:var(--cr);margin-top:40px}
.end .sub{font-size:38px;line-height:1.4;color:var(--g1);margin-top:40px;max-width:880px}
.end .cta{margin-top:50px;align-self:flex-start;background:var(--or);color:var(--ink);border-radius:999px;padding:30px 46px;font:800 40px 'Bricolage';letter-spacing:-.01em;box-shadow:0 20px 60px rgba(255,106,26,.35)}
.facts{margin-top:auto;display:grid;grid-template-columns:repeat(4,1fr);gap:20px;border-top:1.5px solid #2A2522;padding-top:30px}
.facts div{font-size:24px;line-height:1.3;color:var(--g1)}
.facts b{display:block;font:800 40px 'Bricolage';color:var(--cr);margin-bottom:6px}
"""


def hd(n, total, label="Ceos Growth"):
    return (f'<div class="hd"><div class="l"><img src="{LOGO}">{label}</div>'
            f'<div class="r">{n:02d} / {total:02d}</div></div>')


def bar(n, total):
    return f'<div class="bar"><i style="width:{100 * n / total:.1f}%"></i></div>'


def render_page(pg, n, total):
    if pg["kind"] == "cover":
        return f'''<section class="pg dark cover"><div class="glow"></div><div class="glow b"></div><img class="wm" src="{LOGO}">
{hd(n, total)}
<div class="cv"><div class="kick">{pg["kicker"]}</div><h1>{pg["title"]}</h1><p class="sub">{pg["sub"]}</p>
<div class="sw"><span>Ceos Growth · Burgos</span><span class="go">Desliza<i class="arrow"></i></span></div></div>
{bar(n, total)}</section>'''
    if pg["kind"] == "close":
        return f'''<section class="pg dark end"><div class="glow"></div><img class="wm" src="{LOGO}">
{hd(n, total)}
<div class="cv"><h1>{pg["title"]}</h1><p class="sub">{pg["sub"]}</p><div class="cta">{pg["cta"]}</div>
<div class="facts"><div><b>26 días</b>de implantación</div><div><b>15-20</b>anuncios grabados</div><div><b>10</b>perfiles</div><div><b>Comisión</b>sobre ventas</div></div></div>
{bar(n, total)}</section>'''
    return f'''<section class="pg {pg.get("cls", "")}">
{hd(n, total)}
<div class="bd"><div class="kick">{pg["kicker"]}</div><h2>{pg["title"]}</h2>{pg["body"]}</div>
{bar(n, total)}</section>'''


def deck_html(pages, hsize):
    total = len(pages)
    body = "".join(render_page(pg, i + 1, total) for i, pg in enumerate(pages))
    css = DECK.replace("HSIZE", str(hsize))
    body = body.replace(" €", "&nbsp;€").replace(" %", "&nbsp;%")
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


CHECK_JS = """() => [...document.querySelectorAll('.pg')].map((p,i)=>{
  const b=p.querySelector('.bd')||p.querySelector('.cv');
  return {page:i+1, over:b.scrollHeight-b.clientHeight, wide:b.scrollWidth-b.clientWidth};
})"""

COVER_FIT_JS = """() => { const c=document.querySelector('.cv'); return c.scrollHeight-c.clientHeight; }"""


def folder(slug):
    for nn, s, fmt in ORDEN:
        if s == slug:
            return os.path.join(PACK, f"{nn:02d}-{slug}")
    raise KeyError(slug)


def build_deck(br, slug, pages):
    d = folder(slug)
    os.makedirs(d, exist_ok=True)
    src = os.path.join(HERE, f"_{slug}.html")
    # tamaño de titular de portada: el mayor que quepa
    for hsize in (124, 116, 108, 100, 94, 88, 82):
        open(src, "w", encoding="utf-8").write(deck_html(pages, hsize))
        pg = br.new_page(viewport={"width": 1080, "height": 1350})
        pg.goto("file://" + src)
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        res = pg.evaluate(CHECK_JS)
        if res[0]["over"] <= 0:
            break
        pg.close()
    bad = [x for x in res if x["over"] > 0 or x["wide"] > 0]
    print(slug, "páginas:", len(res), "portada", hsize, "DESBORDA:" if bad else "ok", bad if bad else "")
    pdf = os.path.join(d, "carrusel.pdf")
    pg.pdf(path=pdf, width="1080px", height="1350px", print_background=True, prefer_css_page_size=True)
    pg.close()
    prev = os.path.join(PREV, slug)
    os.makedirs(prev, exist_ok=True)
    for f in os.listdir(prev):
        os.remove(os.path.join(prev, f))
    subprocess.run(["pdftoppm", "-png", "-r", "40", pdf, os.path.join(prev, "p")], check=True)
    subprocess.run("montage " + os.path.join(prev, 'p-*.png') + " -tile 5x2 -geometry +6+6 -background '#444' " + os.path.join(SHEETS, slug + '.png'), shell=True)
    # portada a 1080×1350 exactos (72 pt/in → 1080px = 810pt; -r 96 da 1080 px)
    subprocess.run(["pdftoppm", "-png", "-scale-to-x", "1080", "-scale-to-y", "1350", "-f", "1", "-l", "1", "-singlefile", pdf,
                    os.path.join(d, "portada")], check=True)
    return bad


def build_image(br, slug, html):
    d = folder(slug)
    os.makedirs(d, exist_ok=True)
    src = os.path.join(HERE, f"_{slug}.html")
    open(src, "w", encoding="utf-8").write(html.replace(" €", "&nbsp;€").replace(" %", "&nbsp;%"))
    pg = br.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto("file://" + src)
    pg.wait_for_load_state("networkidle")
    pg.evaluate("document.fonts.ready")
    over = pg.evaluate("""() => [...document.querySelectorAll('[data-fit]')].map(e=>({id:e.dataset.fit, over:e.scrollHeight-e.clientHeight}))""")
    bad = [o for o in over if o["over"] > 0]
    print(slug, "imagen", "DESBORDA:" if bad else "ok", bad if bad else "")
    pg.screenshot(path=os.path.join(d, "imagen.png"))
    pg.close()
    return bad


def write_texts():
    for nn, slug, fmt in ORDEN:
        d = folder(slug)
        os.makedirs(d, exist_ok=True)
        t = TEXTOS[slug].strip() + "\n"
        open(os.path.join(d, "post.txt"), "w", encoding="utf-8").write(t)
        if fmt == "encuesta":
            e = dict(ENCUESTAS[slug])
            e["texto"] = t.strip()
            json.dump(e, open(os.path.join(d, "encuesta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def main(args):
    write_texts()
    want = set(args)
    with sync_playwright() as p:
        br = p.chromium.launch()
        if not want or "carruseles" in want or want & set(CARRUSELES):
            for slug, pages in CARRUSELES.items():
                if want and "carruseles" not in want and slug not in want:
                    continue
                build_deck(br, slug, pages)
        if not want or "imagenes" in want or want & set(IMAGENES):
            for slug, fn in IMAGENES.items():
                if want and "imagenes" not in want and slug not in want:
                    continue
                build_image(br, slug, fn(BASE, LOGO))
        br.close()


if __name__ == "__main__":
    main(sys.argv[1:])
