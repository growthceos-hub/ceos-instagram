#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C3 2026-09-29 (captación: sesión de estudio) en src/."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
os.makedirs(OUT, exist_ok=True)
LOGO = '/_blob/70b4b68a06f5599a991cdf05ef629fec'

BASE_KF = """
body{margin:0;background:#0A0908}
@keyframes aLogo{0%,100%{filter:drop-shadow(0 0 6px rgba(255,106,26,.35))}50%{filter:drop-shadow(0 0 16px rgba(255,106,26,.75))}}
@keyframes aGlow{0%,100%{opacity:.8;transform:scale(1)}50%{opacity:1;transform:scale(1.07)}}
@keyframes aHeat{0%,100%{text-shadow:0 0 50px rgba(255,106,26,.3)}50%{text-shadow:0 0 110px rgba(255,106,26,.75)}}
@keyframes aShim{0%{transform:translateX(-140%) skewX(-20deg)}60%,100%{transform:translateX(620%) skewX(-20deg)}}
@keyframes aNudge{0%,100%{transform:translateX(0)}50%{transform:translateX(5px)}}
@keyframes aRec{0%,49%{opacity:1}50%,100%{opacity:.15}}
@keyframes aScan{0%{transform:translateY(-100%)}100%{transform:translateY(900%)}}
"""


def page(title, num, kf, body, foot_left, foot_right_html):
    bars = ''.join(
        f'<div style="height: 6px; border-radius: 99px; background: {"#FF6A1A" if i < num else "rgba(242,237,231,0.12)"}"></div>'
        for i in range(5))
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&amp;family=Instrument+Sans:wght@400;500;600;700&amp;family=Instrument+Serif:ital@0;1&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>{BASE_KF}{kf}
</style>
</helmet>
<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px; position: relative; overflow: hidden; background: #0A0908; color: #F2EDE7; font-family: 'Instrument Sans', sans-serif; display: flex; flex-direction: column; justify-content: space-between">
<div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(242,237,231,0.035) 1px, transparent 1px), linear-gradient(90deg, rgba(242,237,231,0.035) 1px, transparent 1px); background-size: 90px 90px"></div>
<div style="position: relative; display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; align-items: center; gap: 16px">
<img src="{LOGO}" alt="Ceos Productions" style="width: 56px; height: 56px; display: block; animation: aLogo 4s ease-in-out infinite">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 30px; letter-spacing: -0.02em">Ceos Productions</span>
</div>
<span style="font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.12em; color: #9C938B">0{num} / 05</span>
</div>
{body}
<div style="position: relative; display: flex; flex-direction: column; gap: 26px">
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px">{bars}</div>
<div style="display: flex; align-items: center; justify-content: space-between">
<span style="font-size: 25px; color: #B5ADA4">{foot_left}</span>
{foot_right_html}
</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
"""


DESLIZA_PILL = """<span style="display: inline-flex; align-items: center; gap: 10px; background: #FF6A1A; color: #0A0908; font-weight: 700; font-size: 24px; padding: 14px 26px; border-radius: 999px">Desliza<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="2.8" style="animation: aNudge 2s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></span>"""
DESLIZA_TXT = """<span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; letter-spacing: 0.12em; color: #FF6A1A">DESLIZA →</span>"""

# Silueta de persona (hombros + cabeza) en SVG, 420x420, ojos en y≈125
PERSON = """<svg width="420" height="420" viewBox="0 0 420 420" style="display:block">
<defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F2EDE7" stop-opacity=".95"/><stop offset="1" stop-color="#B5ADA4" stop-opacity=".55"/></linearGradient></defs>
<path d="M40 420 C40 300 110 250 210 250 C310 250 380 300 380 420 Z" fill="url(#pg)"/>
<rect x="178" y="200" width="64" height="70" rx="26" fill="url(#pg)"/>
<ellipse cx="210" cy="125" rx="78" ry="92" fill="url(#pg)"/>
<rect x="168" y="118" width="18" height="8" rx="4" fill="#0A0908" opacity=".55"/><rect x="234" y="118" width="18" height="8" rx="4" fill="#0A0908" opacity=".55"/>
</svg>"""

PERSON_TALL = PERSON.replace('height="420" viewBox="0 0 420 420"','height="520" viewBox="0 0 420 520"').replace('M40 420 C40 300 110 250 210 250 C310 250 380 300 380 420 Z','M40 520 C40 300 110 250 210 250 C310 250 380 300 380 520 Z').replace('id="pg"','id="pt"').replace('url(#pg)','url(#pt)')

MONO = "font-family: 'JetBrains Mono', monospace"
BRIC = "font-family: 'Bricolage Grotesque', sans-serif"
SERIF = "font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400"


def headline(tag, l1, l2, size=94):
    return f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 22px">
<span style="align-self: flex-start; padding: 10px 18px; border-radius: 999px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: 0.1em">{tag}</span>
<h1 style="margin: 0; {BRIC}; font-weight: 800; font-size: {size}px; line-height: 0.96; letter-spacing: -0.055em">{l1}<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">{l2}</span></h1>
</div>"""



# ============================================================ C3 captación: una sesión de estudio
def corners(c='#F2EDE7', s=34, w=4):
    return ''.join(
        f'<div style="position: absolute; {v}: 0; {h}: 0; width: {s}px; height: {s}px; border-{v}: {w}px solid {c}; border-{h}: {w}px solid {c}"></div>'
        for v in ('top', 'bottom') for h in ('left', 'right'))


def ejemplo(pos='right: 22px; top: 20px'):
    return f'<span style="position: absolute; {pos}; padding: 6px 12px; border-radius: 8px; border: 1.5px solid rgba(242,237,231,.28); {MONO}; font-size: 16px; letter-spacing: .14em; color: #9C938B; z-index: 7">EJEMPLO</span>'


COMMON_KF = """
@keyframes aPing{0%{transform:scale(.6);opacity:.9}100%{transform:scale(2.1);opacity:0}}
@keyframes aFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes aSweep{0%{transform:translateX(-120%)}100%{transform:translateX(320%)}}
"""

ICONS = {
    'ad': '<path d="M4 10v4h3l6 4V6L7 10H4z"/><path d="M16 9c1.3 1.6 1.3 4.4 0 6M18.5 7c2.4 2.8 2.4 7.2 0 10"/>',
    'reel': '<rect x="6" y="3" width="12" height="18" rx="2.5"/><path d="M10.5 9.5l4 2.5-4 2.5z" fill="currentColor"/>',
    'brand': '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.4 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
    'mic': '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0013 0M12 17.5V21M8.5 21h7"/>',
    'talk': '<path d="M4 5h11v8H9l-3.5 3V13H4z"/><path d="M15 9h5v8h-1.5v3L15 17h-4v-2"/>',
    'photo': '<rect x="3" y="6" width="18" height="14" rx="2.5"/><circle cx="12" cy="13" r="3.8"/><path d="M8.5 6l1.5-2.5h4L15.5 6"/>',
}


def icon(k, sz=34, col='#FF6A1A'):
    return f'<svg width="{sz}" height="{sz}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" style="color: {col}; display: block">{ICONS[k]}</svg>'


# ---------------------------------------------------------------- 01 GANCHO — calendario que se llena desde una sesión
cells = [  # (fila, col, etiqueta, icono)
    (0, 2, 'Reel', 'reel'), (0, 4, 'Anuncio', 'ad'),
    (1, 0, 'Reel', 'reel'), (1, 2, 'Entrevista', 'talk'), (1, 4, 'Anuncio', 'ad'),
    (2, 1, 'Podcast', 'mic'), (2, 3, 'Reel', 'reel'),
    (3, 0, 'Marca', 'brand'), (3, 2, 'Reel', 'reel'), (3, 4, 'Fotos', 'photo'),
]
kf1 = COMMON_KF + """
@keyframes aSes{0%,100%{box-shadow:0 0 0 0 rgba(255,106,26,.0),0 0 40px rgba(255,106,26,.45)}50%{box-shadow:0 0 0 10px rgba(255,106,26,.18),0 0 80px rgba(255,106,26,.8)}}
@keyframes aRecB{0%,49%{opacity:1}50%,100%{opacity:.2}}
@keyframes aWk{0%,10%{background:#FF6A1A}16%,100%{background:rgba(242,237,231,.12)}}
"""
n = len(cells)
pills = ''
for i, (r, c, lab, ic) in enumerate(cells):
    st = 22 + i * 6  # 22..76
    kf1 += (f"@keyframes aP{i}{{0%,9%{{opacity:1;transform:scale(1)}}15%,{st}%{{opacity:0;transform:scale(.3) translate(-60px,-60px)}}"
            f"{st+5}%{{opacity:1;transform:scale(1.14)}}{st+8}%,100%{{opacity:1;transform:scale(1)}}}}\n")
    pills += (f'<div style="grid-row: {r+2}; grid-column: {c+1}; position: relative; border-radius: 16px; background: linear-gradient(160deg, #FF6A1A, #FF8F45); color: #0A0908; '
              f'display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 16px 40px -14px rgba(255,106,26,.9); '
              f'animation: aP{i} 4s cubic-bezier(.3,1.4,.5,1) infinite">{icon(ic, 34, "#0A0908")}'
              f'<span style="{BRIC}; font-weight: 800; font-size: 21px; letter-spacing: -0.01em">{lab}</span></div>')
# semanas 2-4: indicadores que se encienden
for w in range(4):
    on = 30 + w * 14
    kf1 += f"@keyframes aW{w}{{0%,10%{{background:#FF6A1A;color:#0A0908}}16%,{on}%{{background:rgba(242,237,231,.08);color:#9C938B}}{on+4}%,100%{{background:#FF6A1A;color:#0A0908}}}}\n"
days = ''.join(f'<div style="grid-row: 1; grid-column: {k+1}; text-align: center; {MONO}; font-size: 19px; letter-spacing: .12em; color: #9C938B">{d}</div>' for k, d in enumerate(['LUN', 'MAR', 'MIÉ', 'JUE', 'VIE']))
empties = ''.join(f'<div style="grid-row: {r+2}; grid-column: {c+1}; border-radius: 16px; border: 2px dashed rgba(242,237,231,.13)"></div>' for r in range(4) for c in range(5) if not (r == 0 and c == 0))
weeks = ''.join(f'<div style="position: absolute; left: -2px; top: {99 + w * 126}px; width: 50px; height: 34px; border-radius: 10px; {MONO}; font-weight: 600; font-size: 17px; display: flex; align-items: center; justify-content: center; animation: aW{w} 4s steps(1) infinite">S{w+1}</div>' for w in range(4))
session = f'''<div style="grid-row: 2; grid-column: 1; position: relative; border-radius: 16px; background: #0A0908; border: 3px solid #FF6A1A; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; animation: aSes 1.6s ease-in-out infinite; z-index: 3">
<div style="display: flex; align-items: center; gap: 7px; {MONO}; font-weight: 600; font-size: 17px; letter-spacing: .1em; color: #F2EDE7"><span style="width: 12px; height: 12px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30; animation: aRecB 1s steps(1) infinite"></span>REC</div>
<span style="{BRIC}; font-weight: 800; font-size: 22px; color: #FF8F45">SESIÓN</span></div>'''
body1 = headline('ESTUDIO DE GRABACIÓN · BURGOS', 'Deja de grabar a ratos.', 'Graba semanas de vídeos<br>en una sola sesión.', 86) + f"""
<div style="position: relative; height: 640px; border-radius: 34px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.6)">
  <div style="position: absolute; inset: 0; background: radial-gradient(ellipse at 14% 24%, rgba(255,106,26,.22), rgba(10,9,8,0) 55%)"></div>
  <div style="position: absolute; left: 32px; top: 26px; {MONO}; font-size: 19px; letter-spacing: .14em; color: #B5ADA4">TU CALENDARIO DE CONTENIDO</div>
  {ejemplo()}
  <div style="position: absolute; left: 30px; top: 60px; bottom: 30px; width: 50px">{weeks}</div>
  <div style="position: absolute; left: 96px; right: 30px; top: 70px; bottom: 30px; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); grid-template-rows: 36px repeat(4, minmax(0, 1fr)); gap: 14px">
    {days}{empties}{session}{pills}
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Tu estudio de grabación en Burgos.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 PROBLEMA — tomas que se cortan en la oficina
reasons = [('SUENA EL TELÉFONO', 'ad'), ('ENTRA ALGUIEN', 'talk'), ('CAMBIA LA LUZ', 'brand'), ('TE QUEDAS EN BLANCO', 'mic')]
kf2 = COMMON_KF + """
@keyframes aStep{0%,24.9%{opacity:1}25%,100%{opacity:0}}
@keyframes aTake{0%{width:0%}18%{width:62%}20%,25%{width:62%}25.01%,100%{width:0%}}
@keyframes aStamp{0%,17%{opacity:0;transform:translate(-50%,-50%) rotate(-12deg) scale(1.9)}20%{opacity:1;transform:translate(-50%,-50%) rotate(-12deg) scale(.92)}22%,24.5%{opacity:1;transform:translate(-50%,-50%) rotate(-12deg) scale(1)}25%,100%{opacity:0}}
@keyframes aShake{0%,17%,24%,100%{transform:translateX(0)}18.5%{transform:translateX(-10px)}20%{transform:translateX(9px)}21.5%{transform:translateX(-5px)}}
@keyframes aBat{0%{width:46%}100%{width:6%}}
@keyframes aBatC{0%,70%{background:#F2EDE7}71%,100%{background:#FF3B30}}
@keyframes aRec{0%,49%{opacity:1}50%,100%{opacity:.15}}
@keyframes aRow{0%,17%{border-color:rgba(242,237,231,.12);background:#12100F;opacity:.55}19%,24.5%{border-color:#FF3B30;background:rgba(255,59,48,.14);opacity:1}25%,100%{border-color:rgba(242,237,231,.12);background:#12100F;opacity:.55}}
"""
take_labels = ''.join(f'<span style="position: absolute; left: 0; opacity: 0; animation: aStep 4s steps(1) {k-4}s infinite">TOMA 0{k+1}</span>' for k in range(4))
stamps = ''.join(f'<div style="position: absolute; left: 50%; top: 46%; padding: 12px 18px; border: 5px solid #FF3B30; border-radius: 14px; color: #FF3B30; background: rgba(10,9,8,.72); {BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.01em; white-space: nowrap; opacity: 0; z-index: 6; text-align: center; line-height: 1.05; animation: aStamp 4s linear {k-4}s infinite">CORTE<br><span style="{MONO}; font-size: 15px; letter-spacing: .1em; font-weight: 600">{reasons[k][0]}</span></div>' for k in range(4))
rows2 = ''.join(f'<div style="display: flex; align-items: center; gap: 16px; padding: 18px 20px; border-radius: 20px; border: 2px solid rgba(242,237,231,.12); background: #12100F; animation: aRow 4s linear {k-4}s infinite"><span style="flex: none; width: 46px; height: 46px; border-radius: 12px; background: rgba(255,59,48,.16); display: flex; align-items: center; justify-content: center">{icon(ic, 26, "#FF6B61")}</span><span style="{BRIC}; font-weight: 800; font-size: 25px; letter-spacing: -0.01em; line-height: 1.05">{t.capitalize()}</span></div>' for k, (t, ic) in enumerate(reasons))
phone = f'''<div style="position: relative; flex: none; width: 360px; height: 100%; border-radius: 46px; background: #1E1A17; border: 3px solid rgba(242,237,231,.2); padding: 14px; box-sizing: border-box; box-shadow: 0 40px 100px -30px rgba(255,106,26,.5)">
 <div style="position: relative; width: 100%; height: 100%; border-radius: 34px; overflow: hidden; background: linear-gradient(180deg, #2A150A, #0A0908 85%); animation: aShake 4s linear infinite">
  <div style="position: absolute; left: 8%; top: 18%; width: 30%; height: 28%; border-radius: 6px; background: linear-gradient(160deg, #FFFFFF, #B5ADA4); opacity: .55; box-shadow: 0 0 60px 20px rgba(242,237,231,.18)"></div>
  <div style="position: absolute; right: 8%; top: 22%; width: 26%; height: 36%; border-left: 5px solid #6B635C; border-right: 5px solid #6B635C; box-sizing: border-box; background: repeating-linear-gradient(180deg, transparent 0 40px, #6B635C 40px 45px)"></div>
  <svg width="300" height="300" viewBox="0 0 420 420" style="position: absolute; left: 50%; bottom: -40px; margin-left: -150px; display: block"><path d="M40 420 C40 300 110 250 210 250 C310 250 380 300 380 420 Z" fill="#B5ADA4" opacity=".75"/><rect x="178" y="200" width="64" height="70" rx="26" fill="#B5ADA4" opacity=".75"/><ellipse cx="210" cy="125" rx="78" ry="92" fill="#D9D1C8" opacity=".8"/></svg>
  <div style="position: absolute; left: 22px; top: 22px; display: flex; align-items: center; gap: 8px; {MONO}; font-size: 17px; letter-spacing: .1em; color: #F2EDE7"><span style="width: 12px; height: 12px; border-radius: 99px; background: #FF3B30; animation: aRec 1s steps(1) infinite"></span><span style="position: relative; width: 110px; height: 22px">{take_labels}</span></div>
  <div style="position: absolute; right: 20px; top: 22px; width: 44px; height: 20px; border: 2px solid #F2EDE7; border-radius: 5px; padding: 2px; box-sizing: border-box"><div style="height: 100%; border-radius: 2px; animation: aBat 4s linear infinite, aBatC 4s steps(1) infinite"></div></div>
  {stamps}
  <div style="position: absolute; left: 20px; right: 20px; bottom: 24px; height: 8px; border-radius: 99px; background: rgba(242,237,231,.18); overflow: hidden"><div style="height: 100%; background: #FF3B30; animation: aTake 1s linear infinite"></div></div>
 </div></div>'''
body2 = headline('EL PROBLEMA', 'Grabar en la oficina', 'te come la semana.', 94) + f"""
<div style="position: relative; height: 640px; display: flex; gap: 26px">
  {phone}
  <div style="flex: 1; display: flex; flex-direction: column; gap: 14px; justify-content: center">
    <span style="{MONO}; font-size: 19px; letter-spacing: .14em; color: #B5ADA4; margin-bottom: 6px">POR QUÉ SE CORTA</span>
    {rows2}
    <div style="margin-top: 10px; padding: 20px 22px; border-radius: 20px; background: rgba(255,106,26,.1); border: 2px solid rgba(255,106,26,.45); font-size: 24px; line-height: 1.25; color: #F2EDE7">Resultado: <b style="color: #FF8F45">el vídeo se queda para la semana que viene.</b></div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Problema', 2, kf2, body2,
    'Y la siguiente, igual.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 IDEA — qué puedes grabar (focos que recorren los formatos)
fmts = [('ad', 'Anuncios', 'para Meta Ads'), ('reel', 'Reels', 'y vídeos cortos'), ('brand', 'Vídeo de marca', 'para tu web'),
        ('talk', 'Entrevistas', 'y testimonios'), ('mic', 'Podcast', 'en vídeo'), ('photo', 'Fotos', 'de marca personal')]
kf3 = COMMON_KF + """
@keyframes aBeam{0%,100%{opacity:.55}50%{opacity:.9}}
"""
tiles = ''
for i, (ic, t, s) in enumerate(fmts):
    a, b = 4 + i * 15, 4 + i * 15 + 15
    kf3 += (f"@keyframes aT{i}{{0%,{a}%{{border-color:rgba(242,237,231,.12);background:#12100F;transform:scale(1)}}{a+2}%,{b-1}%{{border-color:#FF6A1A;background:#1C130D;transform:scale(1.035)}}{b+1}%,100%{{border-color:rgba(255,106,26,.4);background:#12100F;transform:scale(1)}}}}\n"
            f"@keyframes aF{i}{{0%,{a}%{{width:0%}}{b-1}%,100%{{width:100%}}}}\n"
            f"@keyframes aK{i}{{0%,{b-2}%{{opacity:0;transform:scale(.3)}}{b+1}%{{opacity:1;transform:scale(1.25)}}{b+3}%,100%{{opacity:1;transform:scale(1)}}}}\n"
            f"@keyframes aR{i}{{0%,{a}%{{opacity:0}}{a+1}%,{b-1}%{{opacity:1}}{b}%,100%{{opacity:0}}}}\n")
    tiles += f'''<div style="position: relative; border-radius: 24px; border: 2.5px solid rgba(242,237,231,.12); background: #12100F; padding: 24px 24px 22px; display: flex; flex-direction: column; justify-content: space-between; overflow: hidden; animation: aT{i} 4s ease-in-out infinite">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="width: 64px; height: 64px; border-radius: 18px; background: rgba(255,106,26,.13); display: flex; align-items: center; justify-content: center">{icon(ic, 36)}</span>
<span style="position: relative; width: 44px; height: 44px"><span style="position: absolute; inset: 0; border-radius: 99px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; opacity: 0; animation: aK{i} 4s ease-out infinite"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#0A0908" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
<span style="position: absolute; left: 12px; top: 12px; width: 20px; height: 20px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 16px #FF3B30; opacity: 0; animation: aR{i} 4s steps(1) infinite"></span></span></div>
<div><div style="{BRIC}; font-weight: 800; font-size: 36px; letter-spacing: -0.03em; line-height: 1">{t}</div><div style="margin-top: 6px; font-size: 22px; color: #B5ADA4">{s}</div></div>
<div style="height: 6px; border-radius: 99px; background: rgba(242,237,231,.1); overflow: hidden"><div style="height: 100%; background: #FF6A1A; width: 0%; animation: aF{i} 4s ease-in-out infinite"></div></div>
</div>'''
body3 = headline('QUÉ PUEDES GRABAR', 'Un solo set,', 'todos tus formatos.', 96) + f"""
<div style="position: relative; height: 640px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-rows: repeat(3, minmax(0, 1fr)); gap: 16px">
{tiles}
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Formatos', 3, kf3, body3,
    'Todo el mismo día, con la misma calidad.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 SOLUCIÓN — cómo es una sesión (stepper con punto viajero + timeline)
steps = [('Nos escribes', 'Cuéntanos qué quieres grabar y lo preparamos.'),
         ('Llegas y el set está listo', 'Luz, sonido y fondo montados antes de que entres.'),
         ('Grabas vídeo a vídeo', 'Sin llamadas, sin ruido, sin interrupciones.'),
         ('Te llevas el material', 'Las grabaciones de tus próximas semanas.')]
kf4 = COMMON_KF + """
@keyframes aDot{0%,4%{top:0%}22%,27%{top:33.3%}45%,50%{top:66.6%}68%,92%{top:100%}100%{top:0%}}
@keyframes aLine{0%,4%{height:0%}22%,27%{height:33.3%}45%,50%{height:66.6%}68%,92%{height:100%}100%{height:0%}}
@keyframes aHead{0%{left:0%}92%,100%{left:100%}}
@keyframes aClip{0%,100%{opacity:1}}
"""
st_html = ''
for i, (t, d) in enumerate(steps):
    on = [2, 22, 45, 68][i]
    kf4 += (f"@keyframes aS{i}{{0%,{max(on-1,0)}%{{opacity:.38;transform:translateX(0)}}{on+2}%,94%{{opacity:1;transform:translateX(8px)}}100%{{opacity:.38;transform:translateX(0)}}}}\n"
            f"@keyframes aN{i}{{0%,{max(on-1,0)}%{{background:#12100F;color:#9C938B;border-color:rgba(242,237,231,.2)}}{on+2}%,94%{{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A}}100%{{background:#12100F;color:#9C938B;border-color:rgba(242,237,231,.2)}}}}\n")
    st_html += f'''<div style="position: relative; display: flex; align-items: center; gap: 24px; animation: aS{i} 4s ease-out infinite">
<span style="flex: none; width: 66px; height: 66px; border-radius: 99px; border: 3px solid rgba(242,237,231,.2); display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 22px; z-index: 2; animation: aN{i} 4s ease-out infinite">0{i+1}</span>
<div style="flex: 1; padding: 18px 24px; border-radius: 20px; background: #12100F; border: 2px solid rgba(242,237,231,.12)"><div style="{BRIC}; font-weight: 800; font-size: 32px; letter-spacing: -0.02em; line-height: 1.05">{t}</div><div style="margin-top: 6px; font-size: 22px; color: #B5ADA4; line-height: 1.2">{d}</div></div></div>'''
clips = ''.join(f'<div style="position: absolute; top: 10px; bottom: 10px; left: {x}%; width: {w}%; border-radius: 8px; background: {c}; opacity: .9"></div>' for x, w, c in
                [(1, 14, '#FF6A1A'), (16, 10, '#FF8F45'), (27, 17, '#FF6A1A'), (45, 12, '#FFB27A'), (58, 15, '#FF6A1A'), (74, 11, '#FF8F45'), (86, 13, '#FF6A1A')])
body4 = headline('ASÍ ES UNA SESIÓN', 'Llegas con la idea.', 'Sales con semanas grabadas.', 86) + f"""
<div style="position: relative; height: 640px; display: flex; flex-direction: column; gap: 20px">
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: space-between; padding: 6px 12px 6px 0">
    <div style="position: absolute; left: 31px; top: 40px; bottom: 40px; width: 4px; background: rgba(242,237,231,.1); border-radius: 4px">
      <div style="position: absolute; left: 0; top: 0; width: 100%; background: #FF6A1A; border-radius: 4px; box-shadow: 0 0 16px rgba(255,106,26,.8); animation: aLine 4s cubic-bezier(.6,0,.3,1) infinite"></div>
      <div style="position: absolute; left: -9px; width: 22px; height: 22px; margin-top: -11px; border-radius: 99px; background: #F2EDE7; box-shadow: 0 0 22px 6px rgba(255,106,26,.9); z-index: 3; animation: aDot 4s cubic-bezier(.6,0,.3,1) infinite"></div>
    </div>
    {st_html}
  </div>
  <div style="position: relative; height: 96px; border-radius: 20px; background: #12100F; border: 2px solid rgba(242,237,231,.12); overflow: hidden">
    <span style="position: absolute; left: 18px; top: 8px; {MONO}; font-size: 15px; letter-spacing: .14em; color: #9C938B; z-index: 3">TIMELINE DE LA SESIÓN</span>
    <div style="position: absolute; left: 14px; right: 14px; top: 26px; bottom: 0">{clips}
      <div style="position: absolute; top: 0; bottom: 0; width: 4px; margin-left: -2px; background: #F2EDE7; box-shadow: 0 0 14px #F2EDE7; animation: aHead 4s linear infinite"></div></div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · La sesión', 4, kf4, body4,
    'Tú solo te preocupas de hablar.', DESLIZA_TXT))

# ---------------------------------------------------------------- 05 CTA — DM que escribe ESTUDIO
word = 'ESTUDIO'
kf5 = COMMON_KF + """
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
@keyframes aType{0%,6%{width:0ch}34%,100%{width:7.2ch}}
@keyframes aCaret{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes aInp{0%,37%{opacity:1}38%,100%{opacity:0}}
@keyframes aPh{0%,37%{opacity:0}38%,100%{opacity:1}}
@keyframes aSend{0%,34%{transform:scale(1);background:rgba(242,237,231,.15)}37%{transform:scale(1.25);background:#FF6A1A}40%,100%{transform:scale(1);background:#FF6A1A}}
@keyframes aMsg{0%,40%{opacity:0;transform:translateY(30px) scale(.9)}46%,100%{opacity:1;transform:translateY(0) scale(1)}}
@keyframes aDots{0%,50%{opacity:0}53%,66%{opacity:1}68%,100%{opacity:0}}
@keyframes aRep{0%,67%{opacity:0;transform:translateY(24px) scale(.9)}73%,100%{opacity:1;transform:translateY(0) scale(1)}}
@keyframes aBlink{0%,100%{opacity:.25}50%{opacity:1}}
@keyframes aSeen{0%,56%{opacity:0}60%,100%{opacity:1}}
"""
dots = ''.join(f'<span style="width: 12px; height: 12px; border-radius: 99px; background: #B5ADA4; animation: aBlink .9s ease-in-out {k*0.2}s infinite"></span>' for k in range(3))
chat = f'''<div style="position: relative; width: 920px; height: 520px; border-radius: 32px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6); text-align: left">
 <div style="display: flex; align-items: center; gap: 16px; padding: 22px 28px; border-bottom: 2px solid rgba(242,237,231,.08)">
  <span style="position: relative; width: 58px; height: 58px; border-radius: 99px; background: #0A0908; border: 2.5px solid #FF6A1A; display: flex; align-items: center; justify-content: center"><img src="{LOGO}" style="width: 36px; height: 36px"></span>
  <div><div style="{BRIC}; font-weight: 800; font-size: 28px; letter-spacing: -0.02em">ceos.productions</div><div style="font-size: 19px; color: #9C938B">Estudio de grabación · Burgos</div></div>
  {ejemplo('right: 26px; top: 34px')}
 </div>
 <div style="position: absolute; left: 28px; right: 28px; top: 124px; bottom: 104px; display: flex; flex-direction: column; justify-content: flex-end; gap: 16px">
  <div style="align-self: flex-end; display: flex; flex-direction: column; align-items: flex-end; gap: 6px; animation: aMsg 4s cubic-bezier(.3,1.3,.5,1) infinite">
   <div style="padding: 16px 28px; border-radius: 28px 28px 8px 28px; background: linear-gradient(135deg, #FF6A1A, #FF8F45); color: #0A0908; {BRIC}; font-weight: 800; font-size: 40px; letter-spacing: .02em">ESTUDIO</div>
   <span style="{MONO}; font-size: 15px; color: #9C938B; letter-spacing: .1em; animation: aSeen 4s steps(1) infinite">VISTO</span></div>
  <div style="position: relative; align-self: flex-start; height: 64px; width: 560px">
   <div style="position: absolute; left: 0; top: 0; display: flex; gap: 8px; padding: 22px 24px; border-radius: 26px; background: #1E1A17; animation: aDots 4s steps(1) infinite">{dots}</div>
   <div style="position: absolute; left: 0; top: 0; padding: 16px 24px; border-radius: 28px 28px 28px 8px; background: #1E1A17; font-size: 26px; line-height: 1.25; color: #F2EDE7; white-space: nowrap; animation: aRep 4s cubic-bezier(.3,1.3,.5,1) infinite">¡Hola! Te contamos cómo reservar tu sesión.</div>
  </div>
 </div>
 <div style="position: absolute; left: 24px; right: 24px; bottom: 22px; height: 64px; border-radius: 99px; border: 2px solid rgba(242,237,231,.16); display: flex; align-items: center; padding: 0 10px 0 28px; gap: 12px">
  <div style="flex: 1; position: relative; height: 40px; display: flex; align-items: center">
   <span style="position: absolute; left: 0; font-size: 24px; color: #6B635C; animation: aPh 4s steps(1) infinite">Mensaje…</span>
   <span style="position: relative; display: inline-flex; align-items: center; animation: aInp 4s steps(1) infinite"><span style="display: inline-block; overflow: hidden; white-space: nowrap; {MONO}; font-weight: 600; font-size: 26px; color: #F2EDE7; width: 0ch; animation: aType 4s steps(7) infinite">{word}</span><span style="width: 3px; height: 30px; margin-left: 3px; background: #FF6A1A; animation: aCaret .6s steps(1) infinite"></span></span>
  </div>
  <span style="width: 48px; height: 48px; border-radius: 99px; display: flex; align-items: center; justify-content: center; animation: aSend 4s ease-out infinite"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F2EDE7" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l16-8-6 16-3-6z"/></svg></span>
 </div>
</div>'''
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 84px; line-height: 0.98; letter-spacing: -0.05em">¿Grabamos lo tuyo?<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">Una palabra basta.</span></p>
<div style="margin-top: 38px">{chat}</div>
<div style="position: relative; overflow: hidden; margin-top: 40px; padding: 24px 46px; border-radius: 30px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 50px; line-height: 1.02; letter-spacing: -0.035em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Escríbenos ESTUDIO por DM<br><span style="font-size: 34px; font-weight: 700; letter-spacing: -0.02em">y reserva tu sesión en Burgos</span><div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.3), rgba(255,255,255,0)); animation: aShim 4s ease-in-out 0.6s infinite"></div></div>
</div>
"""
open(os.path.join(OUT, 'S5.dc.html'), 'w').write(page('05 · CTA', 5, kf5, body5,
    'Estudio de grabación propio en Burgos.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
