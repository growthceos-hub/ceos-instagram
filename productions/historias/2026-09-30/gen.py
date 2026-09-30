#!/usr/bin/env python3
"""Genera H1..H5.dc.html (serie 2026-09-30: antes/después de color — por qué sales amarillo o azul).
Uso: python3 gen.py && python3 toolkit/boost_story.py H*.dc.html && python3 gen.py fx
("fx" pasa a tonos de marca los brillos cálidos que añade boost_story.py)."""
import os, re, sys

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





def fix_fx():
    """Tras boost_story.py: partículas, barrido y flash cálidos -> acento de marca (render los pasa a azul)."""
    for n in range(1, 6):
        p = os.path.join(HERE, f'H{n}.dc.html')
        s = open(p).read()
        s = re.sub(r'rgba\(255,(?:140|178),(?:26|60|74|122),', 'rgba(255,106,26,', s)
        s = s.replace('rgba(255,106,74,', 'rgba(255,106,26,').replace('rgba(255,106,122,', 'rgba(255,106,26,')
        s = s.replace('rgba(255,200,160,', 'rgba(242,237,231,').replace('rgba(255,150,80,', 'rgba(255,106,26,')
        open(p, 'w').write(s)
    print('fx ok')


if len(sys.argv) > 1 and sys.argv[1] == 'fx':
    fix_fx()
    sys.exit()

# ---------- piezas comunes: antes / después de color de piel ----------
# Colores de contenido (no son de marca y render.py no los toca): tonos de piel teñida.
WARM = '#E2AA52'   # piel amarilla (bombilla cálida)
COOL = '#8CA6D4'   # piel azulada (ventana / sombra)
NAT = '#D39D80'    # piel natural
GREEN = '#58A86C'  # pared verde
PANEL = ("border-radius: 48px; background: #12100F; border: 2px solid rgba(242,237,231,0.12); "
         "box-shadow: 0 60px 140px -40px rgba(0,0,0,0.9); overflow: hidden")
CYCLE = 7.5

COMMON_CSS = """@keyframes aEye{0%,93%,100%{transform:scaleY(1)}96%{transform:scaleY(.1)}}
@keyframes aSwap{0%,42%{opacity:1}50%,92%{opacity:0}100%{opacity:1}}
@keyframes aSwapB{0%,42%{opacity:0}50%,92%{opacity:1}100%{opacity:0}}
@keyframes aWipe{0%,42%{transform:scaleX(0)}50%,92%{transform:scaleX(1)}100%{transform:scaleX(0)}}
@keyframes aTick{0%,44%{opacity:0;transform:scale(.4)}52%,92%{opacity:1;transform:none}100%{opacity:0;transform:scale(.4)}}
@keyframes aX{0%,40%{opacity:1;transform:none}48%,96%{opacity:0;transform:scale(.4)}100%{opacity:1;transform:none}}"""


def face(w, skin, overlays='', shirt='#1E1A17'):
    """Retrato estilizado: pelo, cara con sombreado, ojos que parpadean, cuello y hombros.
    skin = estilo CSS de la piel (background-color + animation)."""
    hw = int(w * 0.44)
    hh = int(hw * 1.22)
    left = (w - hw) // 2
    eye = int(hw * 0.075)
    return f"""<div style="position: relative; width: {w}px; height: {int(w*1.08)}px">
<div style="position: absolute; left: 50%; bottom: 0; width: {w}px; height: {int(w*0.46)}px; margin-left: -{w//2}px; border-radius: {int(w*0.42)}px {int(w*0.42)}px 24px 24px; background: linear-gradient(170deg, {shirt}, #0A0908)"></div>
<div style="position: absolute; left: 50%; bottom: {int(w*0.40)}px; width: {int(hw*0.36)}px; height: {int(hh*0.3)}px; margin-left: -{int(hw*0.18)}px; border-radius: 0 0 30px 30px; {skin}"><div style="position: absolute; inset: 0; background: rgba(0,0,0,0.28); border-radius: inherit"></div>{overlays}</div>
<div style="position: absolute; left: {left}px; top: {int(w*0.04)}px; width: {hw}px; height: {hh}px; border-radius: 46% 46% 44% 44% / 40% 40% 60% 60%; overflow: hidden; {skin}">
<div style="position: absolute; inset: 0; background: radial-gradient(ellipse at 38% 30%, rgba(255,255,255,0.32), rgba(255,255,255,0) 55%), linear-gradient(180deg, rgba(0,0,0,0) 55%, rgba(0,0,0,0.22))"></div>
{overlays}
<div style="position: absolute; left: 27%; top: 47%; width: {eye}px; height: {eye}px; border-radius: 99px; background: #0A0908; animation: aEye 4s ease-in-out infinite"></div>
<div style="position: absolute; right: 27%; top: 47%; width: {eye}px; height: {eye}px; border-radius: 99px; background: #0A0908; animation: aEye 4s ease-in-out infinite"></div>
<div style="position: absolute; left: 50%; top: 70%; width: {int(hw*0.26)}px; height: {int(hw*0.07)}px; margin-left: -{int(hw*0.13)}px; border-radius: 0 0 99px 99px; background: rgba(10,9,8,0.55)"></div>
</div>
<div style="position: absolute; left: {left - int(hw*0.03)}px; top: {int(w*0.015)}px; width: {int(hw*1.06)}px; height: {int(hh*0.34)}px; border-radius: 50% 50% 18% 42% / 88% 88% 12% 30%; background: linear-gradient(160deg, #3A2E27, #120D0A)"></div>
</div>"""


def swap_tag(bad, good, top=34):
    base = ("position: absolute; left: 50%; top: 0; transform: translateX(-50%); white-space: nowrap; padding: 14px 28px; border-radius: 18px; "
            "color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 36px; letter-spacing: -0.02em; "
            "box-shadow: 0 20px 50px -10px rgba(0,0,0,0.7)")
    return (f'<div style="position: absolute; left: 50%; top: {top}px; z-index: 6; width: 0; height: 70px">'
            f'<div style="{base}; background: {BAD}; animation: aSwap {CYCLE}s ease-in-out infinite">✕ {bad}</div>'
            f'<div style="{base}; background: #FF6A1A; animation: aSwapB {CYCLE}s ease-in-out infinite">✓ {good}</div></div>')


def ab_bar():
    """Barra ANTES / DESPUÉS que se llena en cada ciclo."""
    return (f'<div style="position: relative; display: flex; justify-content: space-between; align-items: center; {MONO}; font-size: 24px; letter-spacing: 0.14em; color: #9C938B; padding: 0 6px">'
            f'<span style="color: {BAD}; animation: aSwap {CYCLE}s ease-in-out infinite">● ANTES</span>'
            f'<span style="position: absolute; left: 190px; right: 230px; top: 50%; height: 6px; margin-top: -3px; border-radius: 9px; background: #1E1A17; overflow: hidden">'
            f'<span style="position: absolute; inset: 0; border-radius: 9px; background: linear-gradient(90deg, {BAD}, #FF6A1A); transform-origin: left; animation: aWipe {CYCLE}s cubic-bezier(.6,0,.3,1) infinite"></span></span>'
            f'<span style="color: #FF6A1A; animation: aSwapB {CYCLE}s ease-in-out infinite">DESPUÉS ●</span></div>')


def fix_heading(n, html, size=108):
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both">
<span style="display: flex; align-items: center; gap: 14px; {MONO}; font-size: 28px; letter-spacing: 0.14em; color: #FF6A1A"><span style="width: 16px; height: 16px; border-radius: 99px; background: #FF6A1A; animation: aBlink 1.2s steps(1) infinite"></span>ARREGLO {n} · ANTES / DESPUÉS</span>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: {size}px; line-height: 0.95; letter-spacing: -0.055em">{html}</h2>
</div>"""


def screen(inner, h=560, bg='radial-gradient(circle at 50% 40%, #1C130D, #0A0908 70%)'):
    return (f'<div style="position: relative; height: {h}px; border-radius: 34px; overflow: hidden; background: {bg}">'
            f'{corners("rgba(242,237,231,0.7)", 22, 50)}{inner}</div>')


# ---------------- H1: gancho ----------------
h1_css = COMMON_CSS + f"""
@keyframes kTone{{0%,27%{{background-color:{WARM}}}33%,60%{{background-color:{COOL}}}66%,94%{{background-color:{NAT}}}100%{{background-color:{WARM}}}}}
@keyframes kCast{{0%,27%{{background-color:rgba(226,170,82,.34)}}33%,60%{{background-color:rgba(140,166,212,.32)}}66%,94%{{background-color:rgba(211,157,128,0)}}100%{{background-color:rgba(226,170,82,.34)}}}}
@keyframes kL1{{0%,27%{{opacity:1;transform:translate(-50%,0)}}31%,97%{{opacity:0;transform:translate(-50%,-14px)}}100%{{opacity:1;transform:translate(-50%,0)}}}}
@keyframes kL2{{0%,29%{{opacity:0;transform:translate(-50%,14px)}}33%,60%{{opacity:1;transform:translate(-50%,0)}}64%,100%{{opacity:0;transform:translate(-50%,-14px)}}}}
@keyframes kL3{{0%,62%{{opacity:0;transform:translate(-50%,14px)}}66%,94%{{opacity:1;transform:translate(-50%,0)}}98%,100%{{opacity:0;transform:translate(-50%,-14px)}}}}
@keyframes aScan{{0%{{top:8%}}50%{{top:88%}}100%{{top:8%}}}}"""
tagb = ("position: absolute; left: 50%; top: 0; transform: translateX(-50%); white-space: nowrap; padding: 14px 30px; border-radius: 18px; color: #0A0908; "
        "font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 40px; letter-spacing: -0.02em; box-shadow: 0 20px 50px -10px rgba(0,0,0,0.7)")
labels = (f'<div style="position: absolute; left: 50%; bottom: 44px; z-index: 6; width: 0; height: 76px">'
          f'<div style="{tagb}; background: {BAD}"><span style="display: block; animation: kL1 {CYCLE}s ease-in-out infinite">✕ AMARILLO</span></div>'
          f'<div style="{tagb}; background: {BAD}; animation: kL2 {CYCLE}s ease-in-out infinite">✕ AZUL</div>'
          f'<div style="{tagb}; background: #FF6A1A; animation: kL3 {CYCLE}s ease-in-out infinite">✓ NATURAL</div></div>')
# la primera etiqueta: se anima el contenedor completo (fondo incluido)
labels = labels.replace(f'<div style="{tagb}; background: {BAD}"><span style="display: block; animation: kL1 {CYCLE}s ease-in-out infinite">✕ AMARILLO</span></div>',
                        f'<div style="{tagb}; background: {BAD}; animation: kL1 {CYCLE}s ease-in-out infinite">✕ AMARILLO</div>')
skin1 = f'background-color: {WARM}; animation: kTone {CYCLE}s ease-in-out infinite'
H1 = HEAD % ('Historia 1 · Color de piel', h1_css, 1) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 52px">
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 128px; line-height: 0.93; letter-spacing: -0.055em">Tu piel no es<br><span style="{SERIF}">de ese color.</span></h1>

<div style="position: relative; {PANEL}; padding: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(rec_bar('WB · AUTO') + f'''<div style="position: absolute; inset: 0; animation: kCast {CYCLE}s ease-in-out infinite"></div>
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -270px">{face(540, skin1)}</div>
<div style="position: absolute; left: 50px; right: 50px; height: 3px; background: linear-gradient(90deg, rgba(255,106,26,0), #FF6A1A, rgba(255,106,26,0)); box-shadow: 0 0 20px #FF6A1A; animation: aScan 5s ease-in-out infinite"></div>
{labels}''', 800)}
</div>
</div>

<div style="position: relative; display: flex; align-items: center; justify-content: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 1.2s both">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 50px; letter-spacing: -0.03em">3 arreglos · antes / después</span>
<svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; animation: aNudge 1.4s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
</div>
""" + TAIL

# ---------------- H2: no mezcles luces ----------------
h2_css = COMMON_CSS + f"""
@keyframes kLamp{{0%,42%{{opacity:1}}50%,92%{{opacity:.08}}100%{{opacity:1}}}}
@keyframes kHalf{{0%,42%{{opacity:.85}}50%,92%{{opacity:0}}100%{{opacity:.85}}}}
@keyframes kRay{{from{{background-position:0 0}}to{{background-position:60px 0}}}}"""
half_warm = f'<div style="position: absolute; inset: 0; background: linear-gradient(90deg, {WARM} 0%, {WARM} 42%, rgba(226,170,82,0) 58%); mix-blend-mode: normal; animation: kHalf {CYCLE}s ease-in-out infinite"></div>'
half_cool = f'<div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(140,166,212,0) 42%, {COOL} 58%, {COOL} 100%); animation: kHalf {CYCLE}s ease-in-out infinite"></div>'
skin2 = f'background-color: {NAT}'
lamp = f"""<div style="position: absolute; left: 44px; top: 150px; display: flex; flex-direction: column; align-items: center; gap: 14px; z-index: 3">
<div style="position: relative; width: 120px; height: 120px">
<div style="position: absolute; inset: -70px; border-radius: 999px; background: radial-gradient(circle, rgba(226,170,82,0.75), rgba(226,170,82,0) 65%); animation: kLamp {CYCLE}s ease-in-out infinite"></div>
<svg width="120" height="120" viewBox="0 0 24 24" fill="none" stroke="#F2EDE7" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="position: relative"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"></path></svg>
</div>
<span style="{MONO}; font-size: 22px; letter-spacing: 0.1em; color: #B5ADA4">BOMBILLA</span></div>"""
window = f"""<div style="position: absolute; right: 44px; top: 150px; display: flex; flex-direction: column; align-items: center; gap: 14px; z-index: 3">
<div style="position: relative; width: 120px; height: 120px; border-radius: 12px; border: 4px solid #F2EDE7; background: linear-gradient(160deg, rgba(140,166,212,0.9), rgba(140,166,212,0.35)); box-shadow: 0 0 80px 10px rgba(140,166,212,0.55)">
<div style="position: absolute; left: 50%; top: 0; bottom: 0; width: 4px; margin-left: -2px; background: #F2EDE7"></div><div style="position: absolute; top: 50%; left: 0; right: 0; height: 4px; margin-top: -2px; background: #F2EDE7"></div></div>
<span style="{MONO}; font-size: 22px; letter-spacing: 0.1em; color: #B5ADA4">VENTANA</span></div>"""
rays = (f'<div style="position: absolute; left: 170px; top: 205px; width: 210px; height: 6px; transform: rotate(18deg); transform-origin: left; background: repeating-linear-gradient(90deg, {WARM} 0 24px, rgba(0,0,0,0) 24px 36px); animation: kRay 1s linear infinite, kLamp {CYCLE}s ease-in-out infinite; z-index: 2"></div>'
        f'<div style="position: absolute; right: 170px; top: 205px; width: 210px; height: 6px; transform: rotate(-18deg); transform-origin: right; background: repeating-linear-gradient(90deg, {COOL} 0 24px, rgba(0,0,0,0) 24px 36px); animation: kRay 1s linear infinite reverse; z-index: 2"></div>')
H2 = HEAD % ('Historia 2 · No mezcles luces', h2_css, 2) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(1, f'No mezcles<br><span style="{SERIF}">luces.</span>', 120)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(swap_tag('Media cara amarilla', 'Una sola luz', 34) + lamp + window + rays + f'<div style="position: absolute; left: 50%; bottom: 0; margin-left: -200px; z-index: 1">{face(400, skin2, half_warm + half_cool)}</div>', 610)}
{ab_bar()}
</div>
</div>

{footer('Apaga la bombilla o cierra la ventana:<br>elige un solo tipo de luz.', 'SIGUIENTE ARREGLO')}
""" + TAIL

# ---------------- H3: balance de blancos fijo ----------------
h3_css = COMMON_CSS + f"""
@keyframes kThumb{{0%{{left:18%}}9%{{left:74%}}18%{{left:34%}}27%{{left:82%}}36%{{left:26%}}42%{{left:58%}}50%,92%{{left:62%}}100%{{left:18%}}}}
@keyframes kDrift{{0%{{background-color:{WARM}}}9%{{background-color:{COOL}}}18%{{background-color:#DDA66A}}27%{{background-color:#84A0D8}}36%{{background-color:{WARM}}}42%{{background-color:#B7A2A8}}50%,92%{{background-color:{NAT}}}100%{{background-color:{WARM}}}}}
@keyframes kVal{{0%{{--s:0}}100%{{--s:0}}}}"""
skin3 = f'background-color: {WARM}; animation: kDrift {CYCLE}s ease-in-out infinite'
lock = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"></rect><path d="M8 11V7a4 4 0 0 1 8 0v4"></path></svg>'
pillb = ("position: absolute; left: 0; top: 0; display: flex; align-items: center; gap: 12px; white-space: nowrap; padding: 12px 24px; border-radius: 16px; "
         "font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 34px; letter-spacing: 0.06em; color: #0A0908")
wb_pill = (f'<div style="position: relative; height: 64px; width: 330px">'
           f'<div style="{pillb}; background: {BAD}; animation: aSwap {CYCLE}s ease-in-out infinite"><span style="animation: aBlink .8s steps(1) infinite">●</span> WB AUTO</div>'
           f'<div style="{pillb}; background: #FF6A1A; animation: aSwapB {CYCLE}s ease-in-out infinite">{lock} WB FIJO</div></div>')
kelvin = f"""<div style="display: flex; flex-direction: column; gap: 16px; padding: 0 8px">
<div style="display: flex; justify-content: space-between; align-items: center">{wb_pill}<span style="{MONO}; font-size: 24px; letter-spacing: 0.1em; color: #9C938B">EJEMPLO</span></div>
<div style="position: relative; height: 26px; border-radius: 99px; background: linear-gradient(90deg, {WARM}, #F2EDE7 55%, {COOL})">
<span style="position: absolute; top: 50%; width: 52px; height: 52px; margin: -26px 0 0 -26px; border-radius: 99px; background: #F2EDE7; border: 6px solid #0A0908; box-shadow: 0 0 0 3px #FF6A1A, 0 0 30px rgba(255,106,26,0.8); animation: kThumb {CYCLE}s cubic-bezier(.6,0,.3,1) infinite"></span></div>
<div style="display: flex; justify-content: space-between; {MONO}; font-size: 22px; letter-spacing: 0.12em; color: #B5ADA4"><span>CÁLIDO</span><span>NEUTRO</span><span>FRÍO</span></div>
</div>"""
H3 = HEAD % ('Historia 3 · Balance de blancos', h3_css, 3) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(2, f'Saca el balance<br><span style="{SERIF}">de AUTO.</span>', 104)}
<div style="position: relative; {PANEL}; padding: 26px 26px 34px; display: flex; flex-direction: column; gap: 28px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(rec_bar('BALANCE DE BLANCOS') + swap_tag('Cambia en cada plano', 'Igual toda la toma', 80) + f'<div style="position: absolute; left: 50%; bottom: 0; margin-left: -180px">{face(360, skin3)}</div>', 530)}
{kelvin}
</div>
</div>

{footer('Fíjalo según tu luz al empezar<br>y no lo toques en toda la grabación.', 'SIGUIENTE ARREGLO')}
""" + TAIL

# ---------------- H4: paredes que tiñen ----------------
h4_css = COMMON_CSS + f"""
@keyframes kWall{{0%,42%{{background-color:{GREEN}}}50%,92%{{background-color:#EEF2F7}}100%{{background-color:{GREEN}}}}}
@keyframes kTint{{0%,42%{{opacity:.62}}50%,92%{{opacity:0}}100%{{opacity:.62}}}}
@keyframes kBounce{{from{{background-position:0 0}}to{{background-position:-60px 0}}}}
@keyframes kRayC{{0%,42%{{filter:none}}50%,92%{{filter:saturate(0) brightness(2.2)}}100%{{filter:none}}}}"""
tint = f'<div style="position: absolute; inset: 0; background: linear-gradient(90deg, {GREEN} 0%, rgba(88,168,108,0.35) 70%, rgba(88,168,108,0.15)); animation: kTint {CYCLE}s ease-in-out infinite"></div>'
skin4 = f'background-color: {NAT}'
wall_lbl_b = f"position: absolute; left: 0; top: 0; white-space: nowrap; {MONO}; font-size: 22px; letter-spacing: 0.1em; color: #0A0908; font-weight: 600"
wall = f"""<div style="position: absolute; left: 0; top: 0; bottom: 0; width: 150px; animation: kWall {CYCLE}s ease-in-out infinite; z-index: 2">
<div style="position: absolute; left: 36px; top: 50%; transform: rotate(-90deg) translateX(-50%); transform-origin: left top; width: 0; height: 30px">
<span style="{wall_lbl_b}; animation: aSwap {CYCLE}s ease-in-out infinite">PARED VERDE</span>
<span style="{wall_lbl_b}; animation: aSwapB {CYCLE}s ease-in-out infinite">PANEL BLANCO</span></div></div>"""
bounce = ''.join(
    f'<div style="position: absolute; left: 150px; top: {t}px; width: 260px; height: 6px; transform: rotate({r}deg); transform-origin: left; '
    f'background: repeating-linear-gradient(90deg, {GREEN} 0 24px, rgba(0,0,0,0) 24px 36px); animation: kBounce .9s linear infinite, kRayC {CYCLE}s ease-in-out infinite; z-index: 2"></div>'
    for t, r in ((200, 10), (290, 0), (380, -10)))
key = f"""<div style="position: absolute; right: 50px; top: 130px; display: flex; flex-direction: column; align-items: center; gap: 12px; z-index: 3">
<div style="width: 110px; height: 150px; border-radius: 14px; background: linear-gradient(180deg, #F2EDE7, #B5ADA4); box-shadow: 0 0 90px 16px rgba(242,237,231,0.35)"></div>
<span style="{MONO}; font-size: 22px; letter-spacing: 0.1em; color: #B5ADA4">LUZ</span></div>"""
H4 = HEAD % ('Historia 4 · Paredes que tiñen', h4_css, 4) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(3, f'Las paredes<br><span style="{SERIF}">tiñen tu cara.</span>', 112)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(wall + bounce + key + swap_tag('Piel verdosa', 'Piel natural', 34) + f'<div style="position: absolute; left: 50%; bottom: 0; margin-left: -170px; z-index: 1">{face(400, skin4, tint)}</div>', 600)}
{ab_bar()}
</div>
</div>

{footer('Pared de color cerca = piel de ese color.<br>Aléjate o pon algo blanco al lado.', 'EL RESUMEN')}
""" + TAIL

# ---------------- H5: remate + CTA (miércoles: tips) ----------------
steps = [('Una sola luz', 'nada de mezclar bombilla y ventana'), ('Balance fijo', 'fuera el modo AUTO'), ('Nada que rebote', 'lejos de paredes de color')]
rows = ''
for i, (a, b) in enumerate(steps):
    d = 1.2 + i * 0.9
    rows += (f'<div style="display: flex; align-items: center; gap: 26px; padding: 22px 28px; border-radius: 26px; background: #171412; border: 1px solid rgba(242,237,231,0.1); animation: aRow .6s ease-out {d:.1f}s both">'
             f'<span style="flex-shrink: 0; width: 64px; height: 64px; border-radius: 18px; border: 3px solid rgba(242,237,231,0.3); display: flex; align-items: center; justify-content: center; animation: aChk .5s ease-out {d+0.3:.1f}s both">'
             f'<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5 9-10" style="stroke-dasharray: 30; stroke-dashoffset: 30; animation: aDash .5s ease-out {d+0.4:.1f}s both"></path></svg></span>'
             f'<span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 46px; font-weight: 700; letter-spacing: -0.01em">{a}</span>'
             f'<span style="{MONO}; font-size: 22px; letter-spacing: 0.06em; color: #9C938B">{b.upper()}</span></span></div>')
swatch = ''.join(
    f'<span style="flex: 1; height: 44px; border-radius: 12px; background: {c}; animation: aPop .6s cubic-bezier(.2,.8,.2,1) {0.6 + i*0.15:.2f}s both"></span>'
    for i, c in enumerate([WARM, COOL, '#8FB08F']))
h5_css = COMMON_CSS + """
@keyframes aRow{from{opacity:.35}to{opacity:1}}
@keyframes aChk{from{background:rgba(255,106,26,0);border-color:rgba(242,237,231,.3)}to{background:#FF6A1A;border-color:#FF6A1A}}
@keyframes aDash{to{stroke-dashoffset:0}}
@keyframes aFill{from{width:0}to{width:100%}}
@keyframes kNat{0%,100%{box-shadow:0 0 0 0 rgba(255,106,26,.6)}50%{box-shadow:0 0 0 14px rgba(255,106,26,0)}}"""
H5 = HEAD % ('Historia 5 · Resumen', h5_css, 5) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{heading('RESUMEN · GUÁRDALA', f'Piel natural<br><span style="{SERIF}">en 3 pasos.</span>')}

<div style="border-radius: 44px; background: rgba(18,16,15,0.94); border: 1px solid rgba(242,237,231,0.12); padding: 34px 38px; display: flex; flex-direction: column; gap: 16px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="display: flex; align-items: center; gap: 14px; margin-bottom: 6px">{swatch}<span style="{MONO}; font-size: 30px; color: #9C938B">→</span><span style="flex: 1.3; height: 44px; border-radius: 12px; background: {NAT}; animation: aPop .6s cubic-bezier(.2,.8,.2,1) 1.1s both, kNat 2s ease-out 1.8s infinite"></span></div>
{rows}
<div style="height: 14px; border-radius: 99px; background: #171412; overflow: hidden; margin-top: 8px"><div style="height: 100%; border-radius: 99px; background: linear-gradient(90deg, #FF6A1A, #FFB27A); animation: aFill 3.4s ease-in-out 1.2s both"></div></div>
</div>
</div>

<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .9s both">
<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="animation: aBob 2s ease-in-out infinite"><path d="M6 15l6-6 6 6"></path></svg>
<div style="position: relative; overflow: hidden; padding: 28px 60px; border-radius: 999px; background: #FF6A1A; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 58px; letter-spacing: -0.03em; white-space: nowrap; box-shadow: 0 30px 90px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.4), rgba(255,255,255,0)); animation: aShim 4s ease-in-out .6s infinite"></div></div>
<span style="{MONO}; font-size: 28px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>
</div>
""" + TAIL

for n, s in enumerate([H1, H2, H3, H4, H5], 1):
    open(os.path.join(HERE, f'H{n}.dc.html'), 'w').write(s)
print('ok')
