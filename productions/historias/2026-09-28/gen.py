#!/usr/bin/env python3
"""Genera H1..H5.dc.html (serie 2026-09-28: errores de vestuario a cámara). Luego: boost_story.py."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = '#FF6A1A'  # acento (BRAND=productions lo pasa a azul)
BAD = '#FF5A64'

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&amp;family=Instrument+Sans:wght@400;500;600;700&amp;family=Instrument+Serif:ital@0;1&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;background:#0A0908}
@keyframes aLogo{0%%,100%%{filter:drop-shadow(0 0 8px rgba(255,106,26,.35))}50%%{filter:drop-shadow(0 0 22px rgba(255,106,26,.8))}}
@keyframes aGlow{0%%,100%%{opacity:.8;transform:scale(1)}50%%{opacity:1;transform:scale(1.06)}}
@keyframes aIn{from{opacity:0;transform:translateY(40px);filter:blur(10px)}to{opacity:1;transform:none;filter:blur(0)}}
@keyframes aNudge{0%%,100%%{transform:translateX(0)}50%%{transform:translateX(12px)}}
@keyframes aBob{0%%,100%%{transform:translateY(0)}50%%{transform:translateY(-10px)}}
@keyframes aBlink{0%%,49%%{opacity:1}50%%,100%%{opacity:.15}}
@keyframes aPop{0%%{opacity:0;transform:scale(.6) translateY(20px)}60%%{opacity:1;transform:scale(1.08)}100%%{opacity:1;transform:none}}
@keyframes aMoire{from{transform:translateX(0) rotate(3deg)}to{transform:translateX(-48px) rotate(3deg)}}
@keyframes aMoire2{from{background-position:0 0}to{background-position:28px 0}}
@keyframes aBracket{0%%,100%%{transform:scale(1);opacity:.9}50%%{transform:scale(1.04);opacity:1}}
@keyframes aShim{0%%{transform:translateX(-120%%)}60%%,100%%{transform:translateX(620%%)}}
@keyframes aBreathe{0%%,100%%{transform:scale(1)}50%%{transform:scale(1.04)}}
@property --s{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes aTc{from{--s:0}to{--s:15}}
.tc{counter-reset:s var(--s);animation:aTc 15s linear both}
.tc::after{content:"00:00:" counter(s, decimal-leading-zero)}
%s
@media (prefers-reduced-motion:reduce){*{animation-duration:.01s!important;animation-iteration-count:1!important}}
</style>
</helmet>
<div style="width: 1080px; height: 1920px; box-sizing: border-box; padding: 250px 80px 290px; position: relative; overflow: hidden; background: #0A0908; color: #F2EDE7; font-family: 'Instrument Sans', sans-serif; display: flex; flex-direction: column; justify-content: space-between">
<div style="position: absolute; top: 700px; left: 50%%; margin-left: -720px; width: 1440px; height: 1440px; border-radius: 999px; background: radial-gradient(circle, rgba(255,106,26,0.32), rgba(255,106,26,0) 60%%); animation: aGlow 5s ease-in-out infinite"></div>

<div style="position: relative; display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; align-items: center; gap: 18px"><img src="/_blob/70b4b68a06f5599a991cdf05ef629fec" alt="Ceos Productions" style="width: 68px; height: 68px; display: block; animation: aLogo 5s ease-in-out infinite"><span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 36px; letter-spacing: -0.02em">Ceos Productions</span></div>
<span style="padding: 12px 22px; border-radius: 999px; background: #FF6A1A; color: #0A0908; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 24px; letter-spacing: 0.1em">%02d / 05</span>
</div>
"""
TAIL = """</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1080,"height":1920}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
"""
MONO = "font-family: 'JetBrains Mono', monospace"
SERIF = "font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A"
ARROW = '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="animation: aNudge 1.4s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
STRIPES = "repeating-linear-gradient(90deg, #F2EDE7 0 7px, #12100F 7px 14px)"


def heading(label, html):
    return f"""<div style="display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both">
<span style="{MONO}; font-size: 28px; letter-spacing: 0.14em; color: #FF6A1A">{label}</span>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 112px; line-height: 0.95; letter-spacing: -0.055em">{html}</h2>
</div>"""


def footer(text, nxt):
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 30px">
<p style="margin: 0; font-family: 'Instrument Serif', serif; font-style: italic; font-size: 58px; line-height: 1.08; color: #D9D1C8; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 1s both">{text}</p>
<div style="display: flex; align-items: center; justify-content: flex-end; gap: 16px"><span style="{MONO}; font-size: 28px; letter-spacing: 0.1em; color: #FF6A1A">{nxt}</span>{ARROW}</div>
</div>"""


def person(w, shirt, extra='', head_extra=''):
    """Silueta estilizada: cabeza + hombros con camiseta (shirt = background CSS)."""
    hh = int(w * 0.42)
    return f"""<div style="position: relative; width: {w}px; height: {int(w*1.02)}px">
<div style="position: absolute; left: 50%; top: 0; width: {hh}px; height: {int(hh*1.15)}px; margin-left: -{hh//2}px; border-radius: 999px; background: linear-gradient(160deg, #B5ADA4, #6B635C); {head_extra}"></div>
<div style="position: absolute; left: 50%; top: {int(hh*1.05)}px; width: {int(hh*0.34)}px; height: {int(hh*0.3)}px; margin-left: -{int(hh*0.17)}px; background: #6B635C"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: {int(w*0.52)}px; border-radius: {int(w*0.4)}px {int(w*0.4)}px 30px 30px; overflow: hidden; background: {shirt}">{extra}</div>
</div>"""


def moire_layer():
    return ('<div style="position: absolute; inset: -40px -80px; background: repeating-linear-gradient(90deg, rgba(10,9,8,0.85) 0 6px, rgba(10,9,8,0) 6px 12px); '
            'animation: aMoire 1.1s linear infinite"></div>'
            '<div style="position: absolute; inset: 0; background: repeating-linear-gradient(0deg, rgba(242,237,231,0.35) 0 5px, rgba(242,237,231,0) 5px 10px); animation: aMoire2 .7s linear infinite"></div>')


def corners(color='#F2EDE7', inset=26, size=60):
    b = f'position: absolute; width: {size}px; height: {size}px; border-color: {color}; border-style: solid'
    return (f'<div style="{b}; left: {inset}px; top: {inset}px; border-width: 5px 0 0 5px; border-radius: 12px 0 0 0"></div>'
            f'<div style="{b}; right: {inset}px; top: {inset}px; border-width: 5px 5px 0 0; border-radius: 0 12px 0 0"></div>'
            f'<div style="{b}; left: {inset}px; bottom: {inset}px; border-width: 0 0 5px 5px; border-radius: 0 0 0 12px"></div>'
            f'<div style="{b}; right: {inset}px; bottom: {inset}px; border-width: 0 5px 5px 0; border-radius: 0 0 12px 0"></div>')


def rec_bar(right='4K · 25P'):
    return f"""<div style="position: absolute; left: 44px; right: 44px; top: 44px; display: flex; justify-content: space-between; align-items: center; {MONO}; font-size: 26px; letter-spacing: 0.08em; z-index: 3">
<span style="display: flex; align-items: center; gap: 12px"><span style="width: 20px; height: 20px; border-radius: 99px; background: {BAD}; animation: aBlink 1s steps(1) infinite"></span>REC <span class="tc"></span></span>
<span style="color: #B5ADA4">{right}</span></div>"""


def chip(text, top, left, delay, good=False, right=None):
    bg = '#FF6A1A' if good else BAD
    pos = f'top: {top}px; ' + (f'right: {right}px' if right is not None else f'left: {left}px')
    return (f'<div style="position: absolute; {pos}; z-index: 4; padding: 14px 24px; border-radius: 18px; background: {bg}; color: #0A0908; '
            f"font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 34px; letter-spacing: -0.02em; white-space: nowrap; "
            f'box-shadow: 0 20px 50px -10px rgba(0,0,0,0.7); animation: aPop .7s cubic-bezier(.2,.8,.2,1) {delay}s both">{text}</div>')


# ---------------- H1: gancho ----------------
h1_css = """@keyframes aScan{0%{top:12%}50%{top:82%}100%{top:12%}}"""
h1_shirt = person(430, STRIPES, moire_layer())
H1 = HEAD % ('Historia 1 · Tu ropa y la cámara', h1_css, 1) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 56px">
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 118px; line-height: 0.94; letter-spacing: -0.055em">Tu ropa<br>arruina el vídeo<br><span style="{SERIF}">antes de hablar.</span></h1>

<div style="position: relative; height: 720px; border-radius: 48px; background: #12100F; border: 2px solid rgba(242,237,231,0.12); box-shadow: 0 60px 140px -40px rgba(0,0,0,0.9); overflow: hidden; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="position: absolute; inset: 0; background: radial-gradient(circle at 50% 45%, rgba(255,106,26,0.18), rgba(10,9,8,0) 65%)"></div>
{rec_bar()}
<div style="position: absolute; inset: 0; animation: aBracket 2.4s ease-in-out infinite">{corners()}</div>
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -215px">{h1_shirt}</div>
<div style="position: absolute; left: 60px; right: 60px; height: 3px; background: linear-gradient(90deg, rgba(255,106,26,0), #FF6A1A, rgba(255,106,26,0)); box-shadow: 0 0 20px #FF6A1A; animation: aScan 4s ease-in-out infinite"></div>
{chip('✕ Rayas que bailan', 150, 50, 1.6)}
{chip('✕ Blanco quemado', 250, None, 3.0, right=50)}
{chip('✕ Logo gigante', 470, 50, 4.4)}
{chip('✕ Arrugas', 560, None, 5.8, right=50)}
</div>
</div>

<div style="position: relative; display: flex; align-items: center; justify-content: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 1.2s both">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 50px; letter-spacing: -0.03em">4 errores de vestuario a evitar</span>
<svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; animation: aNudge 1.4s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
</div>
""" + TAIL

# ---------------- H2: rayas finas ----------------
h2_css = """@keyframes aSwap{0%,42%{opacity:1}50%,92%{opacity:0}100%{opacity:1}}
@keyframes aSwapB{0%,42%{opacity:0}50%,92%{opacity:1}100%{opacity:0}}
@keyframes aLab{0%,42%{background:#FF5A64}50%,92%{background:#FF6A1A}100%{background:#FF5A64}}
@keyframes aWipe{0%,42%{left:-10%}50%{left:110%}92%{left:110%}100%{left:-10%}}"""
bad_p = person(420, STRIPES, moire_layer())
good_p = person(420, 'linear-gradient(160deg, #FF8F45, #FF6A1A)')
H2 = HEAD % ('Historia 2 · Rayas finas', h2_css, 2) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{heading('ERROR 1', f'Rayas finas<br>y <span style="{SERIF}">cuadritos.</span>')}

<div style="align-self: center; position: relative; width: 820px; height: 700px; border-radius: 48px; background: #12100F; border: 2px solid rgba(242,237,231,0.12); box-shadow: 0 60px 140px -40px rgba(0,0,0,0.9); overflow: hidden; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{rec_bar('VISOR')}
{corners('rgba(242,237,231,0.7)')}
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -210px; animation: aSwap 7.5s ease-in-out infinite">{bad_p}</div>
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -210px; animation: aSwapB 7.5s ease-in-out infinite">{good_p}</div>
<div style="position: absolute; top: 0; bottom: 0; width: 14px; margin-left: -7px; background: #F2EDE7; box-shadow: 0 0 40px #FF6A1A; animation: aWipe 7.5s ease-in-out infinite"></div>
<div style="position: absolute; left: 50%; top: 130px; transform: translateX(-50%); z-index: 4; padding: 14px 28px; border-radius: 18px; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 38px; width: 300px; white-space: nowrap; animation: aLab 7.5s ease-in-out infinite">
<span style="display: block; text-align: center; animation: aSwap 7.5s ease-in-out infinite">✕ Efecto moiré</span><span style="position: absolute; left: 0; right: 0; top: 14px; text-align: center; animation: aSwapB 7.5s ease-in-out infinite">✓ Tejido liso</span></div>
</div>
</div>

{footer('En cámara, las rayas finas parpadean.<br><span style="color: #F2EDE7">Mejor tejidos lisos.</span>', 'SIGUIENTE ERROR')}
""" + TAIL

# ---------------- H3: blanco puro / negro total ----------------
bars = ''
hs = [12, 18, 26, 34, 40, 46, 50, 52, 50, 46, 42, 38, 36, 38, 44, 56, 70, 88, 100]
for i, h in enumerate(hs):
    clip = i >= len(hs) - 3
    col = BAD if clip else 'rgba(242,237,231,0.75)'
    bars += (f'<div style="flex: 1; height: {h}%; border-radius: 8px 8px 0 0; background: {col}; transform-origin: bottom; '
             f'animation: aBar {1.6 + (i % 5) * 0.23:.2f}s ease-in-out {-(i * 0.17):.2f}s infinite"></div>')
sw = [('#2F4A7A', 'Azul'), ('#7A8699', 'Gris'), ('#5E7F6E', 'Verde'), ('#9A6B4F', 'Tierra'), ('#6E3B4A', 'Granate')]
swatches = ''
for i, (c, n) in enumerate(sw):
    d = 1.6 + i * 0.5
    swatches += (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 12px; animation: aPop .7s cubic-bezier(.2,.8,.2,1) {d:.1f}s both">'
                 f'<div style="position: relative; width: 112px; height: 112px; border-radius: 999px; background: {c}; border: 3px solid rgba(242,237,231,0.25); animation: aRing 3s ease-in-out {d+0.5:.1f}s infinite">'
                 f'<span style="position: absolute; right: -6px; bottom: -6px; width: 44px; height: 44px; border-radius: 99px; background: #FF6A1A; color: #0A0908; font-size: 28px; font-weight: 800; display: flex; align-items: center; justify-content: center">✓</span></div>'
                 f'<span style="font-size: 28px; font-weight: 600; color: #D9D1C8">{n}</span></div>')
h3_css = """@keyframes aBar{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.82)}}
@keyframes aZebra{from{background-position:0 0}to{background-position:56px 0}}
@keyframes aRing{0%,100%{box-shadow:0 0 0 0 rgba(255,106,26,.0)}50%{box-shadow:0 0 0 10px rgba(255,106,26,.35)}}
@keyframes aWarn{0%,100%{opacity:1}50%{opacity:.35}}"""
H3 = HEAD % ('Historia 3 · Blanco y negro', h3_css, 3) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{heading('ERROR 2', f'Blanco puro<br>o <span style="{SERIF}">negro total.</span>')}

<div style="border-radius: 44px; background: rgba(18,16,15,0.94); border: 1px solid rgba(242,237,231,0.12); padding: 40px 44px; display: flex; flex-direction: column; gap: 34px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="display: flex; justify-content: space-between; align-items: center; {MONO}; font-size: 26px; letter-spacing: 0.1em"><span style="color: #B5ADA4">HISTOGRAMA</span><span style="color: {BAD}; animation: aWarn 1s ease-in-out infinite">▲ SIN DETALLE</span></div>
<div style="position: relative; height: 250px; display: flex; align-items: flex-end; gap: 8px; border-bottom: 2px solid rgba(242,237,231,0.2)">{bars}
<div style="position: absolute; right: -8px; top: -10px; bottom: 0; width: 150px; border-radius: 12px; background: repeating-linear-gradient(135deg, rgba(255,90,100,0.35) 0 12px, rgba(255,90,100,0) 12px 28px); background-size: 56px 56px; animation: aZebra .8s linear infinite"></div></div>
<div style="height: 2px; background: rgba(242,237,231,0.1)"></div>
<div style="{MONO}; font-size: 26px; letter-spacing: 0.1em; color: #FF6A1A">MEJOR: TONOS MEDIOS</div>
<div style="display: flex; justify-content: space-between">{swatches}</div>
</div>
</div>

{footer('La cámara pierde el detalle.<br><span style="color: #F2EDE7">Elige tonos medios.</span>', 'SIGUIENTE ERROR')}
""" + TAIL

# ---------------- H4: logos y brillos ----------------
spark = ''
for (x, y, d, s) in [(90, 70, 0.0, 34), (300, 50, 0.6, 26), (180, 150, 1.1, 30), (340, 170, 0.3, 22), (60, 180, 0.9, 24), (250, 110, 1.5, 28)]:
    spark += (f'<span style="position: absolute; left: {x}px; top: {y}px; width: {s}px; height: {s}px; background: #F2EDE7; '
              f'clip-path: polygon(50% 0, 62% 38%, 100% 50%, 62% 62%, 50% 100%, 38% 62%, 0 50%, 38% 38%); animation: aTw 1.4s ease-in-out {d}s infinite"></span>')
logo = (f'<div style="position: absolute; left: 50%; top: 58px; transform: translateX(-50%); font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; '
        f'font-size: 64px; letter-spacing: -0.03em; color: #F2EDE7; border: 5px solid #F2EDE7; padding: 0 18px; border-radius: 14px">LOGO</div>')
h4_p = person(440, 'linear-gradient(160deg, #3A4A6B, #25324F)', logo + spark)
h4_css = """@keyframes aTw{0%,100%{transform:scale(.3) rotate(0);opacity:.2}50%{transform:scale(1.1) rotate(45deg);opacity:1}}
@keyframes aRet{0%,34%{transform:translate(0,300px) scale(1.1)}42%,58%{transform:translate(-100px,340px) scale(.9)}66%,100%{transform:translate(0,90px) scale(1)}}
@keyframes aRetC{0%,60%{border-color:#FF5A64}66%,100%{border-color:#FF6A1A}}
@keyframes aTagBad{0%,60%{opacity:1}64%,100%{opacity:0}}
@keyframes aTagGood{0%,62%{opacity:0;transform:scale(.8)}68%,100%{opacity:1;transform:none}}"""
H4 = HEAD % ('Historia 4 · Logos y brillos', h4_css, 4) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{heading('ERROR 3', f'Logos, frases<br>y <span style="{SERIF}">brillos.</span>')}

<div style="align-self: center; position: relative; width: 820px; height: 700px; border-radius: 48px; background: #12100F; border: 2px solid rgba(242,237,231,0.12); box-shadow: 0 60px 140px -40px rgba(0,0,0,0.9); overflow: hidden; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="position: absolute; inset: 0; background: radial-gradient(circle at 50% 40%, rgba(255,106,26,0.16), rgba(10,9,8,0) 65%)"></div>
{rec_bar('AF · SEGUIMIENTO')}
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -220px">{h4_p}</div>
<div style="position: absolute; left: 50%; top: 150px; width: 240px; height: 240px; margin-left: -120px; z-index: 3; animation: aRet 7.5s cubic-bezier(.6,0,.3,1) infinite">
<div style="position: absolute; inset: 0; border: 6px solid; border-radius: 22px; animation: aRetC 7.5s linear infinite"></div></div>
<div style="position: absolute; left: 50%; top: 110px; transform: translateX(-50%); z-index: 4; white-space: nowrap">
<div style="padding: 14px 28px; border-radius: 18px; background: {BAD}; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 38px; animation: aTagBad 7.5s linear infinite">✕ Miran la camiseta</div>
<div style="position: absolute; left: 0; top: 0; padding: 14px 28px; border-radius: 18px; background: #FF6A1A; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 38px; animation: aTagGood 7.5s linear infinite">✓ Miran tu cara</div></div>
</div>
</div>

{footer('Roban la mirada.<br><span style="color: #F2EDE7">Que miren tu cara, no tu ropa.</span>', 'ÚLTIMO ERROR')}
""" + TAIL

# ---------------- H5: arrugas + checklist + CTA ----------------
items = ['Tejidos lisos', 'Tonos medios', 'Sin logos ni brillos', '2–3 cambios planchados']
rows = ''
for i, t in enumerate(items):
    d = 1.3 + i * 0.9
    rows += (f'<div style="display: flex; align-items: center; gap: 26px; padding: 22px 28px; border-radius: 26px; background: #171412; border: 1px solid rgba(242,237,231,0.1); animation: aRow .6s ease-out {d:.1f}s both">'
             f'<span style="flex-shrink: 0; width: 60px; height: 60px; border-radius: 18px; border: 3px solid rgba(242,237,231,0.3); display: flex; align-items: center; justify-content: center; animation: aChk .5s ease-out {d+0.3:.1f}s both">'
             f'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5 9-10" style="stroke-dasharray: 30; stroke-dashoffset: 30; animation: aDash .5s ease-out {d+0.4:.1f}s both"></path></svg></span>'
             f'<span style="font-size: 44px; font-weight: 700; letter-spacing: -0.01em">{t}</span></div>')
h5_css = """@keyframes aRow{from{opacity:.35}to{opacity:1}}
@keyframes aChk{from{background:rgba(255,106,26,0);border-color:rgba(242,237,231,.3)}to{background:#FF6A1A;border-color:#FF6A1A}}
@keyframes aDash{to{stroke-dashoffset:0}}
@keyframes aFill{from{width:0}to{width:100%}}"""
H5 = HEAD % ('Historia 5 · Checklist de vestuario', h5_css, 5) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{heading('ERROR 4', f'Un solo look<br>y <span style="{SERIF}">arrugado.</span>')}

<div style="border-radius: 44px; background: rgba(18,16,15,0.94); border: 1px solid rgba(242,237,231,0.12); padding: 38px 40px; display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="display: flex; justify-content: space-between; {MONO}; font-size: 26px; letter-spacing: 0.1em; margin-bottom: 6px"><span style="color: #FF6A1A">CHECKLIST · ANTES DE GRABAR</span><span style="color: #9C938B">GUÁRDALA</span></div>
{rows}
<div style="height: 14px; border-radius: 99px; background: #171412; overflow: hidden; margin-top: 8px"><div style="height: 100%; border-radius: 99px; background: linear-gradient(90deg, #FF6A1A, #FFB27A); animation: aFill 4.2s ease-in-out 1.3s both"></div></div>
</div>
</div>

<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 20px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .9s both">
<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="animation: aBob 2s ease-in-out infinite"><path d="M6 15l6-6 6 6"></path></svg>
<div style="position: relative; overflow: hidden; padding: 26px 56px; border-radius: 999px; background: #FF6A1A; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 54px; letter-spacing: -0.03em; box-shadow: 0 30px 90px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.4), rgba(255,255,255,0)); animation: aShim 4s ease-in-out .6s infinite"></div></div>
<span style="{MONO}; font-size: 26px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>
</div>
""" + TAIL

for n, s in enumerate([H1, H2, H3, H4, H5], 1):
    open(os.path.join(HERE, f'H{n}.dc.html'), 'w').write(s)
print('ok')
