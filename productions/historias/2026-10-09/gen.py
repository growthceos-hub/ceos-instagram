#!/usr/bin/env python3
"""Genera H1..H5.dc.html (serie 2026-10-09: error común de sonido (voz que suena a lata) y 3 arreglos).
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




def fix_heading(n, html, size=108):
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both">
<span style="display: flex; align-items: center; gap: 14px; {MONO}; font-size: 28px; letter-spacing: 0.14em; color: #FF6A1A"><span style="width: 16px; height: 16px; border-radius: 99px; background: #FF6A1A; animation: aBlink 1.2s steps(1) infinite"></span>ARREGLO {n} DE 3</span>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: {size}px; line-height: 0.95; letter-spacing: -0.055em">{html}</h2>
</div>"""


COMMON_CSS += """
@keyframes kMic{0%,42%{transform:translateX(0)}50%,92%{transform:translateX(-300px)}100%{transform:translateX(0)}}
@keyframes kDist{0%,42%{width:420px}50%,92%{width:120px}100%{width:420px}}
@keyframes kAmp{0%,42%{transform:scaleY(.32)}50%,92%{transform:scaleY(1)}100%{transform:scaleY(.32)}}
@keyframes kRing{0%{transform:scale(.2);opacity:1}100%{transform:scale(2.6);opacity:0}}
@keyframes kRingS{0%{transform:scale(.2);opacity:1}100%{transform:scale(1.1);opacity:0}}
@keyframes kHum{0%,42%{height:92%}50%,92%{height:10%}100%{height:92%}}
@keyframes kHp{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
@keyframes kArc{0%,100%{opacity:.2}50%{opacity:1}}"""


def label_swap(bad, good, style):
    return (f'<div style="position: absolute; {style}; z-index: 6; {MONO}; font-weight: 600; font-size: 28px; letter-spacing: 0.1em; white-space: nowrap">'
            f'<span style="position: absolute; left: 0; top: 0; color: {BAD}; animation: aSwap {CYCLE}s ease-in-out infinite">{bad}</span>'
            f'<span style="position: absolute; left: 0; top: 0; color: #FF6A1A; animation: aSwapB {CYCLE}s ease-in-out infinite">{good}</span></div>')


skin = 'background-color: #C9A58C'

# ---------------- H1: gancho ----------------
H1 = HEAD % ('Historia 1 · Tu voz suena a lata', COMMON_CSS, 1) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 50px">
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 124px; line-height: 0.93; letter-spacing: -0.055em">Se ve genial.<br><span style="{SERIF}">Suena a lata.</span></h1>

<div style="position: relative; {PANEL}; padding: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(rec_bar('AUDIO · -38 dB') + f'''
<div style="position: absolute; left: 50%; bottom: 170px; margin-left: -140px">{face(280, skin)}</div>
<div style="position: absolute; left: 50px; right: 50px; bottom: 40px">{wave(30, 130, (2, 6, 11, 15, 20, 24, 28), 5)}</div>
{bad_chip('Eco de sala', 100, 1.2, left=50)}
{bad_chip('Micro lejos', 190, 2.0, right=50)}
{bad_chip('Ruido de fondo', 280, 2.8, left=90)}''', 820)}
</div>
</div>

<div style="position: relative; display: flex; align-items: center; justify-content: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 1.2s both">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 52px; letter-spacing: -0.03em">El error y 3 arreglos</span>
<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; animation: aNudge 1.4s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
</div>
""" + TAIL

# ---------------- H2: micro cerca ----------------
h2_scene = (f'<div style="position: absolute; left: 50px; bottom: 200px; z-index: 2">{face(300, skin)}</div>'
            f'<div style="position: absolute; left: 650px; bottom: 200px; z-index: 3; animation: kMic {CYCLE}s cubic-bezier(.6,0,.3,1) infinite">{mic(1.0)}</div>'
            f'<div style="position: absolute; left: 300px; top: 532px; height: 4px; z-index: 4; border-radius: 9px; background: repeating-linear-gradient(90deg, #F2EDE7 0 14px, rgba(0,0,0,0) 14px 24px); animation: kDist {CYCLE}s cubic-bezier(.6,0,.3,1) infinite"></div>'
            + label_swap('LEJOS', 'A UN PALMO', 'left: 320px; top: 548px')
            + f'<div style="position: absolute; left: 50px; right: 50px; bottom: 20px; z-index: 4; transform-origin: center; animation: kAmp {CYCLE}s ease-in-out infinite">{wave(30, 100, (), 9)}</div>'
            + swap_tag('Voz lejana y hueca', 'Voz cercana y clara', 34))
H2 = HEAD % ('Historia 2 · Micro cerca', COMMON_CSS, 2) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(1, f'El micro cerca,<br><span style="{SERIF}">no en la mesa.</span>', 108)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(h2_scene, 720)}
{ab_bar()}
</div>
</div>

{footer('Cuanto más lejos está el micro,<br>más sala y menos voz graba.', 'SIGUIENTE ARREGLO')}
""" + TAIL

# ---------------- H3: sala sin eco ----------------
rings_bad = ''.join(f'<div style="position: absolute; left: 50%; top: 50%; width: 240px; height: 240px; margin: -120px 0 0 -120px; border-radius: 999px; border: 5px solid {BAD}; animation: kRing 2s ease-out {-d:.1f}s infinite"></div>' for d in (0, .5, 1.0, 1.5))
rings_good = ''.join(f'<div style="position: absolute; left: 50%; top: 50%; width: 240px; height: 240px; margin: -120px 0 0 -120px; border-radius: 999px; border: 5px solid #FF6A1A; animation: kRingS 1.6s ease-out {-d:.1f}s infinite"></div>' for d in (0, .55, 1.1))
echo = ''.join(f'<div style="position: absolute; {side}: 40px; top: {t}px; {MONO}; font-weight: 600; font-size: 40px; color: {BAD}"><span style="display: inline-block; animation: aBlink {b}s steps(1) infinite">ECO</span></div>' for side, t, b in (('left', 200, .6), ('right', 330, .8), ('left', 470, .7)))
curtain = lambda side: (f'<div style="position: absolute; {side}: 22px; top: 100px; bottom: 120px; width: 110px; border-radius: 16px; '
                        f'background: repeating-linear-gradient(90deg, #1F3550 0 18px, #2D4C73 18px 36px); box-shadow: inset 0 0 30px rgba(0,0,0,0.6)"></div>')
rug = '<div style="position: absolute; left: 200px; right: 200px; bottom: 60px; height: 70px; border-radius: 50%; background: repeating-linear-gradient(90deg, #2D4C73 0 22px, #1F3550 22px 44px)"></div>'
h3_scene = (f'<div style="position: absolute; inset: 0; z-index: 2; animation: aSwap {CYCLE}s ease-in-out infinite">{rings_bad}{echo}</div>'
            f'<div style="position: absolute; inset: 0; z-index: 2; animation: aSwapB {CYCLE}s ease-in-out infinite">{curtain("left")}{curtain("right")}{rug}{rings_good}'
            f'<div style="position: absolute; left: 160px; top: 120px; {MONO}; font-size: 24px; letter-spacing: 0.12em; color: #B5ADA4">CORTINA</div>'
            f'<div style="position: absolute; left: 50%; bottom: 150px; transform: translateX(-50%); {MONO}; font-size: 24px; letter-spacing: 0.12em; color: #B5ADA4">ALFOMBRA</div></div>'
            f'<div style="position: absolute; left: 50%; top: 50%; margin: -95px 0 0 -95px; z-index: 3">{face(190, skin)}</div>'
            + swap_tag('Sala vacía: rebota', 'Sala vestida: voz seca', 34))
H3 = HEAD % ('Historia 3 · Sala sin eco', COMMON_CSS, 3) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(2, f'Mata el eco<br><span style="{SERIF}">de la sala.</span>', 116)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(h3_scene, 720)}
{ab_bar()}
</div>
</div>

{footer('Paredes desnudas rebotan la voz.<br>Cortinas, alfombra, sofá: todo suma.', 'SIGUIENTE ARREGLO')}
""" + TAIL

# ---------------- H4: auriculares ----------------
hp = ('<svg width="300" height="300" viewBox="0 0 24 24" fill="none" stroke="#F2EDE7" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
      '<path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3z" fill="#FF6A1A" stroke="#FF6A1A"></path>'
      '<path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z" fill="#FF6A1A" stroke="#FF6A1A"></path></svg>')
arcs = ''.join(f'<div style="position: absolute; left: {335 + i*28}px; top: {210 - i*30}px; width: {60 + i*40}px; height: {120 + i*60}px; border-radius: 0 999px 999px 0; border: 5px solid #FF6A1A; border-left: none; animation: kArc 1.2s ease-in-out {i*0.25:.2f}s infinite"></div>' for i in range(3))
rnd = random.Random(4)
spec = ''
for i in range(14):
    if i < 2:
        inner = (f'<span style="position: absolute; left: 0; right: 0; bottom: 0; border-radius: 8px; background: {BAD}; box-shadow: 0 0 18px {BAD}; animation: kHum {CYCLE}s ease-in-out infinite"></span>')
    else:
        inner = (f'<span style="position: absolute; left: 0; right: 0; bottom: 0; height: {rnd.randint(25, 70)}%; border-radius: 8px; background: #FF6A1A; transform-origin: bottom; animation: aBar .7s ease-in-out {-rnd.uniform(0, .7):.2f}s infinite alternate"></span>')
    spec += f'<span style="position: relative; flex: 1; height: 100%">{inner}</span>'
spec = (f'<div style="position: absolute; left: 50px; right: 50px; bottom: 60px; height: 170px; display: flex; gap: 10px; z-index: 3">{spec}</div>'
        f'<div style="position: absolute; left: 50px; bottom: 22px; {MONO}; font-size: 20px; letter-spacing: 0.12em; color: #9C938B">GRAVES</div>'
        f'<div style="position: absolute; right: 50px; bottom: 22px; {MONO}; font-size: 20px; letter-spacing: 0.12em; color: #9C938B">AGUDOS</div>')
h4_scene = (f'<div style="position: absolute; left: 50px; top: 130px; z-index: 3; transform-origin: center; animation: kHp 3s ease-in-out infinite">{hp}</div>{arcs}'
            f'<div style="position: absolute; right: 60px; top: 150px; z-index: 5; display: flex; flex-direction: column; gap: 16px; align-items: flex-end; animation: aSwap {CYCLE}s ease-in-out infinite">'
            f'{bad_chip("Zumbido", 0, .8, right=0).replace("position: absolute; top: 0px; right: 0px;", "position: relative;")}'
            f'{bad_chip("Ventilador", 0, 1.4, right=0).replace("position: absolute; top: 0px; right: 0px;", "position: relative;")}</div>'
            f'<div style="position: absolute; right: 60px; top: 200px; z-index: 5; padding: 18px 28px; border-radius: 20px; background: #FF6A1A; color: #0A0908; font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; font-size: 40px; animation: aSwapB {CYCLE}s ease-in-out infinite">✓ Fondo limpio</div>'
            + spec + swap_tag('Lo oyes al editar', 'Lo oyes antes de grabar', 34))
H4 = HEAD % ('Historia 4 · Auriculares', COMMON_CSS, 4) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{fix_heading(3, f'Escucha con<br><span style="{SERIF}">auriculares.</span>', 116)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(h4_scene, 720)}
{ab_bar()}
</div>
</div>

{footer('Lo que no oyes al grabar,<br>lo vas a oír al editar.', 'EL RESUMEN')}
""" + TAIL

# ---------------- H5: resumen + CTA (viernes: captación) ----------------
steps = [('Micro cerca de la boca', 'más voz, menos sala'), ('Sala sin eco', 'cortinas, alfombra, sofá'), ('Escucha con auriculares', 'pilla el ruido antes')]
rows = ''
for i, (a, b) in enumerate(steps):
    d = 1.2 + i * 0.9
    rows += (f'<div style="display: flex; align-items: center; gap: 26px; padding: 24px 28px; border-radius: 26px; background: #171412; border: 1px solid rgba(242,237,231,0.1); animation: aRow .6s ease-out {d:.1f}s both">'
             f'<span style="flex-shrink: 0; width: 70px; height: 70px; border-radius: 18px; border: 3px solid rgba(242,237,231,0.3); display: flex; align-items: center; justify-content: center; animation: aChk .5s ease-out {d+0.3:.1f}s both">'
             f'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5 9-10" style="stroke-dasharray: 30; stroke-dashoffset: 30; animation: aDash .5s ease-out {d+0.4:.1f}s both"></path></svg></span>'
             f'<span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 46px; font-weight: 700; letter-spacing: -0.01em">{a}</span>'
             f'<span style="{MONO}; font-size: 22px; letter-spacing: 0.06em; color: #9C938B">{b.upper()}</span></span></div>')
h5_css = COMMON_CSS + """
@keyframes aRow{from{opacity:.35}to{opacity:1}}
@keyframes aChk{from{background:rgba(255,106,26,0);border-color:rgba(242,237,231,.3)}to{background:#FF6A1A;border-color:#FF6A1A}}
@keyframes aDash{to{stroke-dashoffset:0}}
@keyframes aFill{from{width:0}to{width:100%}}"""
H5 = HEAD % ('Historia 5 · Resumen', h5_css, 5) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 40px">
{heading('RESUMEN · GUÁRDALO', f'Que se te oiga<br><span style="{SERIF}">tan bien como se te ve.</span>')}

<div style="border-radius: 44px; background: rgba(18,16,15,0.94); border: 1px solid rgba(242,237,231,0.12); padding: 34px 38px; display: flex; flex-direction: column; gap: 16px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{rows}
<div style="height: 14px; border-radius: 99px; background: #171412; overflow: hidden; margin-top: 8px"><div style="height: 100%; border-radius: 99px; background: linear-gradient(90deg, #FF6A1A, #FFB27A); animation: aFill 3.2s ease-in-out 1.2s both"></div></div>
</div>
</div>

<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .9s both">
<span style="font-family: 'Instrument Serif', serif; font-style: italic; font-size: 46px; color: #D9D1C8">¿Prefieres un set con el sonido ya resuelto?</span>
<div style="position: relative; overflow: hidden; padding: 28px 56px; border-radius: 999px; background: #FF6A1A; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 56px; letter-spacing: -0.03em; white-space: nowrap; box-shadow: 0 30px 90px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Escríbenos ESTUDIO por DM<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.4), rgba(255,255,255,0)); animation: aShim 4s ease-in-out .6s infinite"></div></div>
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 700; font-size: 40px; letter-spacing: -0.02em">y reserva tu sesión en Burgos</span>
<span style="{MONO}; font-size: 28px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>
</div>
""" + TAIL

for n, s in enumerate([H1, H2, H3, H4, H5], 1):
    open(os.path.join(HERE, f'H{n}.dc.html'), 'w').write(s)
print('ok')
