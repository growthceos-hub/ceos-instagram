#!/usr/bin/env python3
"""Genera H1..H5.dc.html (serie 2026-10-08: checklist antes de grabar tu podcast o entrevista).
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
<span style="display: flex; align-items: center; gap: 14px; {MONO}; font-size: 28px; letter-spacing: 0.14em; color: #FF6A1A"><span style="width: 16px; height: 16px; border-radius: 99px; background: #FF6A1A; animation: aBlink 1.2s steps(1) infinite"></span>CHECK {n} DE 3</span>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: {size}px; line-height: 0.95; letter-spacing: -0.055em">{html}</h2>
</div>"""


def screen(inner, h=560, bg='radial-gradient(circle at 50% 40%, #1C130D, #0A0908 70%)'):
    return (f'<div style="position: relative; height: {h}px; border-radius: 34px; overflow: hidden; background: {bg}">'
            f'{corners("rgba(242,237,231,0.7)", 22, 50)}{inner}</div>')




# ================= serie 2026-10-08: checklist antes de grabar tu podcast / entrevista =================
import random
COMMON_CSS += """
@keyframes aBar{0%{transform:scaleY(.25)}100%{transform:scaleY(1)}}
@keyframes kSpike{0%,100%{transform:scaleY(.4)}50%{transform:scaleY(1.15)}}
@keyframes kSlideN{0%{opacity:0;transform:translateY(-30px)}6%,40%{opacity:1;transform:none}46%,100%{opacity:0;transform:translateY(-30px)}}
@keyframes kFillG{0%,42%{height:6%}52%,92%{height:78%}100%{height:6%}}
@keyframes kScroll{from{transform:translateY(0)}to{transform:translateY(-50%)}}
@keyframes kDrop{0%{transform:translateY(-60px);opacity:0}20%{opacity:1}100%{transform:translateY(260px);opacity:0}}"""


def buzz_css():
    fr = []
    for i in range(0, 43, 3):
        x = 9 if (i // 3) % 2 == 0 else -9
        fr.append(f'{i}%{{transform:translateX({x}px) rotate({x/9:.0f}deg)}}')
    fr.append('45%,100%{transform:none}')
    return '@keyframes kBuzz{' + ''.join(fr) + '}'


COMMON_CSS += '\n' + buzz_css()


def wave(n=30, h=150, spikes=(), seed=1, spike_txt=None):
    """Onda de audio animada. spikes = índices de barras con pico rojo (solo en la fase ANTES)."""
    rnd = random.Random(seed)
    bars = ''
    for i in range(n):
        bh = rnd.randint(30, 85)
        dl = -rnd.uniform(0, 0.8)
        sp = ''
        if i in spikes:
            sp = (f'<span style="position: absolute; left: 0; right: 0; bottom: 50%; height: {h//2 - 4}px; transform-origin: bottom; animation: aSwap {CYCLE}s ease-in-out infinite">'
                  f'<span style="position: absolute; inset: 0; border-radius: 6px; background: {BAD}; box-shadow: 0 0 18px {BAD}; transform-origin: bottom; animation: kSpike .35s ease-in-out infinite"></span></span>'
                  f'<span style="position: absolute; left: 0; right: 0; top: 50%; height: {h//2 - 4}px; animation: aSwap {CYCLE}s ease-in-out infinite">'
                  f'<span style="position: absolute; inset: 0; border-radius: 6px; background: {BAD}; transform-origin: top; animation: kSpike .35s ease-in-out infinite"></span></span>')
        bars += (f'<span style="position: relative; flex: 1; height: {h}px; display: flex; align-items: center">'
                 f'<span style="width: 100%; height: {bh}%; border-radius: 6px; background: #FF6A1A; animation: aBar .8s ease-in-out {dl:.2f}s infinite alternate"></span>{sp}</span>')
    return f'<div style="position: relative; display: flex; gap: 8px; align-items: center; height: {h}px">{bars}</div>'


def mic(scale=1.0, delay=0):
    w = int(110 * scale)
    return (f'<div style="display: flex; flex-direction: column; align-items: center">'
            f'<div style="position: relative; width: {w}px; height: {int(w*1.5)}px; border-radius: {w}px; overflow: hidden; '
            f'background: repeating-linear-gradient(0deg, #B5ADA4 0 5px, #6B635C 5px 10px); border: 5px solid #F2EDE7; box-shadow: 0 0 60px rgba(255,106,26,0.35)">'
            f'<div style="position: absolute; left: 0; top: 0; bottom: 0; width: 30%; background: linear-gradient(90deg, rgba(255,255,255,0.35), rgba(255,255,255,0))"></div></div>'
            f'<div style="width: {int(w*0.14)}px; height: {int(w*0.9)}px; background: #6B635C"></div>'
            f'<div style="width: {int(w*1.1)}px; height: {int(w*0.14)}px; border-radius: 99px; background: #6B635C"></div></div>')


def bad_chip(text, top, delay, left=None, right=None):
    pos = f'top: {top}px; ' + (f'left: {left}px' if left is not None else f'right: {right}px')
    return (f'<div style="position: absolute; {pos}; z-index: 5; display: flex; align-items: center; gap: 12px; padding: 16px 26px; border-radius: 20px; '
            f"background: {BAD}; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 40px; letter-spacing: -0.02em; "
            f'white-space: nowrap; box-shadow: 0 24px 60px -12px rgba(0,0,0,0.8); animation: aPop .7s cubic-bezier(.2,.8,.2,1) {delay}s both, aBob 2.4s ease-in-out {delay+0.7:.1f}s infinite">✕ {text}</div>')


# ---------------- H1: gancho ----------------
H1 = HEAD % ('Historia 1 · Checklist podcast', COMMON_CSS, 1) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 50px">
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 122px; line-height: 0.93; letter-spacing: -0.055em">Tu podcast se arruina<br><span style="{SERIF}">antes del REC.</span></h1>

<div style="position: relative; {PANEL}; padding: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(rec_bar('PODCAST · 2 MICROS') + f'''
<div style="position: absolute; left: 80px; right: 80px; bottom: 60px; display: flex; justify-content: space-between; align-items: flex-end">{mic(1.15)}{mic(1.15)}</div>
<div style="position: absolute; left: 250px; right: 250px; bottom: 210px">{wave(16, 170, (3, 9, 13), 3)}</div>
{bad_chip('Móvil vibrando', 110, 1.2, left=50)}
{bad_chip('Boca seca', 215, 2.0, right=50)}
{bad_chip('Leyendo un folio', 320, 2.8, left=150)}''', 820)}
</div>
</div>

<div style="position: relative; display: flex; align-items: center; justify-content: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 1.2s both">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 52px; letter-spacing: -0.03em">La checklist de 3 pasos</span>
<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; animation: aNudge 1.4s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
</div>
""" + TAIL

# ---------------- H2: modo avión ----------------
plane = '<svg width="150" height="150" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"></path></svg>'
notif = ''.join(
    f'<div style="padding: 16px 18px; border-radius: 18px; background: rgba(242,237,231,0.12); display: flex; flex-direction: column; gap: 4px; animation: kSlideN {CYCLE}s ease-out {d}s infinite">'
    f'<span style="{MONO}; font-size: 17px; letter-spacing: 0.08em; color: #9C938B">{a}</span><span style="font-size: 24px; font-weight: 600">{b}</span></div>'
    for a, b, d in (('MENSAJES · AHORA', 'Nuevo mensaje', 0), ('LLAMADA', 'Llamada entrante', 0.6), ('CALENDARIO', 'Recordatorio', 1.2)))
phone = f"""<div style="position: absolute; left: 60px; top: 130px; width: 300px; height: 560px; z-index: 3">
<div style="position: absolute; inset: 0; animation: kBuzz {CYCLE}s linear infinite">
<div style="position: absolute; inset: 0; border-radius: 48px; background: #0A0908; border: 6px solid #B5ADA4; overflow: hidden; box-shadow: 0 40px 90px -20px rgba(0,0,0,0.9)">
<div style="position: absolute; left: 50%; top: 14px; width: 90px; height: 24px; margin-left: -45px; border-radius: 99px; background: #1E1A17"></div>
<div style="position: absolute; left: 16px; right: 16px; top: 60px; display: flex; flex-direction: column; gap: 12px; animation: aSwap {CYCLE}s ease-in-out infinite">{notif}</div>
<div style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 18px; animation: aSwapB {CYCLE}s ease-in-out infinite">{plane}<span style="{MONO}; font-size: 24px; letter-spacing: 0.12em; color: #FF6A1A">MODO AVIÓN</span></div>
</div></div>
<div style="position: absolute; left: 320px; top: 40px; {MONO}; font-size: 44px; font-weight: 600; color: {BAD}; transform: rotate(-12deg); animation: aSwap {CYCLE}s ease-in-out infinite"><span style="display: inline-block; animation: aBlink .3s steps(1) infinite">BZZ</span></div>
</div>"""
H2 = HEAD % ('Historia 2 · Modo avión', COMMON_CSS, 2) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(1, f'Todos los móviles<br><span style="{SERIF}">en modo avión.</span>', 108)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(swap_tag('Vibración en el audio', 'Audio limpio', 34) + phone + f'<div style="position: absolute; right: 70px; bottom: 120px; z-index: 2">{mic(1.25)}</div><div style="position: absolute; left: 50px; right: 50px; bottom: 30px; z-index: 4">{wave(30, 90, (4, 5, 11, 12, 19, 20, 26), 7)}</div>', 760)}
{ab_bar()}
</div>
</div>

{footer('Un móvil que vibra en la mesa<br>se cuela en el micro. También el tuyo.', 'SIGUIENTE CHECK')}
""" + TAIL

# ---------------- H3: agua a mano ----------------
glass = f"""<div style="position: absolute; left: 90px; top: 140px; width: 220px; height: 290px; z-index: 3">
<div style="position: absolute; left: 50%; top: -80px; width: 22px; height: 40px; margin-left: -11px; border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%; background: #8FC8FF; animation: aSwapB {CYCLE}s ease-in-out infinite"><span style="position: absolute; inset: 0; border-radius: inherit; background: inherit; animation: kDrop 1s ease-in infinite"></span></div>
<div style="position: absolute; inset: 0; border: 7px solid #F2EDE7; border-top: none; border-radius: 0 0 46px 46px; overflow: hidden; background: rgba(242,237,231,0.05)">
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 6%; background: linear-gradient(180deg, rgba(143,200,255,0.85), rgba(80,150,230,0.95)); animation: kFillG {CYCLE}s ease-in-out infinite">
<div style="position: absolute; left: 0; right: 0; top: 0; height: 10px; background: rgba(255,255,255,0.6)"></div></div>
<div style="position: absolute; left: 22px; top: 20px; bottom: 20px; width: 18px; border-radius: 99px; background: rgba(255,255,255,0.25)"></div></div>
<div style="position: absolute; left: -10px; right: -10px; bottom: -56px; text-align: center; {MONO}; font-size: 24px; letter-spacing: 0.12em; color: #B5ADA4">AGUA SIN GAS</div>
</div>"""
clicks = ''.join(
    f'<div style="position: absolute; left: {l}px; top: {t}px; z-index: 5; padding: 10px 18px; border-radius: 14px; background: {BAD}; color: #0A0908; {MONO}; font-weight: 600; font-size: 28px; '
    f'animation: aSwap {CYCLE}s ease-in-out infinite"><span style="display: inline-block; animation: aBlink {b}s steps(1) infinite">¡CLIC!</span></div>'
    for l, t, b in ((380, 170, .5), (480, 290, .7), (390, 410, .6)))
H3 = HEAD % ('Historia 3 · Agua a mano', COMMON_CSS, 3) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(2, f'Agua a mano.<br><span style="{SERIF}">Siempre.</span>', 120)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(glass + clicks + f'<div style="position: absolute; right: 80px; top: 140px; z-index: 2">{mic(1.4)}</div><div style="position: absolute; left: 50px; right: 50px; bottom: 34px; z-index: 4">{wave(30, 110, (3, 10, 17, 24), 11)}</div>' + swap_tag('Chasquidos en la voz', 'Voz limpia', 34), 700)}
{ab_bar()}
</div>
</div>

{footer('Con la boca seca, el micro capta<br>chasquidos. Un vaso cerca y listo.', 'SIGUIENTE CHECK')}
""" + TAIL

# ---------------- H4: temas en tarjetas ----------------
lines = ''.join(f'<div style="height: 14px; width: {w}%; border-radius: 99px; background: rgba(10,9,8,0.35)"></div>'
                for w in [92, 88, 95, 70, 90, 85, 93, 60, 88, 94, 79, 91, 86, 68, 95, 89, 72, 90] * 2)
paper = f"""<div style="position: absolute; left: 50%; top: 130px; width: 520px; height: 520px; margin-left: -260px; z-index: 3; animation: aSwap {CYCLE}s ease-in-out infinite">
<div style="position: absolute; inset: 0; border-radius: 18px; background: #F2EDE7; overflow: hidden; box-shadow: 0 40px 90px -20px rgba(0,0,0,0.9); transform: rotate(-3deg)">
<div style="position: absolute; left: 40px; right: 40px; top: 30px; display: flex; flex-direction: column; gap: 18px; animation: kScroll 6s linear infinite">{lines}</div></div>
<div style="position: absolute; right: -30px; bottom: -20px; padding: 10px 18px; border-radius: 14px; background: #0A0908; border: 2px solid {BAD}; {MONO}; font-size: 24px; color: {BAD}">PÁGINA 1 DE 4</div></div>"""
cards = ''.join(
    f'<div style="position: absolute; left: 50%; top: {t}px; width: 560px; margin-left: -280px; transform: rotate({r}deg); padding: 26px 32px; border-radius: 24px; background: #F2EDE7; color: #0A0908; '
    f'box-shadow: 0 30px 70px -20px rgba(0,0,0,0.9); display: flex; align-items: center; gap: 22px">'
    f'<span style="flex-shrink: 0; width: 64px; height: 64px; border-radius: 18px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; font-size: 38px">{i}</span>'
    f'<span style="font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; font-size: 44px; letter-spacing: -0.02em">{txt}</span></div>'
    for i, (t, r, txt) in enumerate(((150, -3, 'Cómo empezó todo'), (310, 2, 'El error que cometí'), (470, -2, 'Mi consejo')), 1))
cards = (f'<div style="position: absolute; inset: 0; z-index: 3; animation: aSwapB {CYCLE}s ease-in-out infinite">{cards}'
         f'<div style="position: absolute; right: 40px; bottom: 30px; {MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">EJEMPLO</div></div>')
H4 = HEAD % ('Historia 4 · Temas en tarjetas', COMMON_CSS, 4) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(3, f'Temas en tarjetas,<br><span style="{SERIF}">no un guion.</span>', 108)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(swap_tag('Leyendo un folio', 'Charla natural', 34) + paper + cards, 720)}
{ab_bar()}
</div>
</div>

{footer('Apunta 3 o 4 temas clave.<br>Leer palabra por palabra se nota.', 'LA CHECKLIST')}
""" + TAIL

# ---------------- H5: checklist + CTA (jueves: tips) ----------------
steps = [('Móviles en modo avión', 'ni vibraciones ni avisos'), ('Agua a mano', 'adiós a los chasquidos'), ('Temas en tarjetas', 'charla, no lectura')]
rows = ''
for i, (a, b) in enumerate(steps):
    d = 1.2 + i * 0.9
    rows += (f'<div style="display: flex; align-items: center; gap: 26px; padding: 24px 28px; border-radius: 26px; background: #171412; border: 1px solid rgba(242,237,231,0.1); animation: aRow .6s ease-out {d:.1f}s both">'
             f'<span style="flex-shrink: 0; width: 70px; height: 70px; border-radius: 18px; border: 3px solid rgba(242,237,231,0.3); display: flex; align-items: center; justify-content: center; animation: aChk .5s ease-out {d+0.3:.1f}s both">'
             f'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5 9-10" style="stroke-dasharray: 30; stroke-dashoffset: 30; animation: aDash .5s ease-out {d+0.4:.1f}s both"></path></svg></span>'
             f'<span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 48px; font-weight: 700; letter-spacing: -0.01em">{a}</span>'
             f'<span style="{MONO}; font-size: 22px; letter-spacing: 0.06em; color: #9C938B">{b.upper()}</span></span></div>')
recbtn = (f'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px">'
          f'<span style="{MONO}; font-size: 26px; letter-spacing: 0.12em; color: #9C938B">ANTES DE GRABAR</span>'
          f'<span style="display: flex; align-items: center; gap: 14px; padding: 14px 26px; border-radius: 999px; background: #1E1A17; {MONO}; font-weight: 600; font-size: 30px; letter-spacing: 0.1em; animation: kRecOn .5s ease-out 4.3s both">'
          f'<span style="width: 22px; height: 22px; border-radius: 99px; background: {BAD}; animation: aBlink 1s steps(1) 4.3s infinite"></span>LISTO PARA REC</span></div>')
h5_css = COMMON_CSS + """
@keyframes aRow{from{opacity:.35}to{opacity:1}}
@keyframes aChk{from{background:rgba(255,106,26,0);border-color:rgba(242,237,231,.3)}to{background:#FF6A1A;border-color:#FF6A1A}}
@keyframes aDash{to{stroke-dashoffset:0}}
@keyframes aFill{from{width:0}to{width:100%}}
@keyframes kRecOn{from{opacity:.35;transform:scale(.9)}to{opacity:1;transform:none;box-shadow:0 0 40px rgba(255,90,100,.5)}}"""
H5 = HEAD % ('Historia 5 · Checklist', h5_css, 5) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{heading('CHECKLIST · GUÁRDALA', f'Antes de darle<br><span style="{SERIF}">a REC.</span>')}

<div style="border-radius: 44px; background: rgba(18,16,15,0.94); border: 1px solid rgba(242,237,231,0.12); padding: 34px 38px; display: flex; flex-direction: column; gap: 16px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{recbtn}
{rows}
<div style="height: 14px; border-radius: 99px; background: #171412; overflow: hidden; margin-top: 8px"><div style="height: 100%; border-radius: 99px; background: linear-gradient(90deg, #FF6A1A, #FFB27A); animation: aFill 3.2s ease-in-out 1.2s both"></div></div>
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
