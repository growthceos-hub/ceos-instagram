#!/usr/bin/env python3
"""Genera H1..H5.dc.html (serie 2026-09-29: mito vs realidad al grabarte). Luego: boost_story.py."""
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




# ---------- piezas comunes de la serie mito vs realidad ----------
STAMP_CSS = """@keyframes aStamp{0%{opacity:0;transform:rotate(-12deg) scale(2.4)}60%{opacity:1;transform:rotate(-12deg) scale(.92)}100%{opacity:1;transform:rotate(-12deg) scale(1)}}
@keyframes aThump{0%,100%{transform:translateX(0)}20%{transform:translateX(-6px)}40%{transform:translateX(6px)}60%{transform:translateX(-3px)}}
@keyframes aPulseR{0%,100%{box-shadow:0 0 0 0 rgba(255,90,100,.0)}50%{box-shadow:0 0 0 14px rgba(255,90,100,.18)}}"""
PANEL = ("border-radius: 48px; background: #12100F; border: 2px solid rgba(242,237,231,0.12); "
         "box-shadow: 0 60px 140px -40px rgba(0,0,0,0.9); overflow: hidden")


def stamp(text='FALSO', delay=2.0, size=54, extra=''):
    return (f'<span style="display: inline-block; padding: 8px 22px; border: 6px solid {BAD}; border-radius: 16px; color: {BAD}; '
            f"font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: {size}px; letter-spacing: 0.06em; line-height: 1; "
            f'background: rgba(10,9,8,0.55); animation: aStamp .55s cubic-bezier(.3,1.4,.5,1) {delay}s both; {extra}">{text}</span>')


def myth_heading(n, html, size=112):
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both">
<span style="display: flex; align-items: center; gap: 14px; {MONO}; font-size: 28px; letter-spacing: 0.14em; color: {BAD}"><span style="width: 16px; height: 16px; border-radius: 99px; background: {BAD}; animation: aBlink 1.2s steps(1) infinite"></span>MITO {n}</span>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: {size}px; line-height: 0.95; letter-spacing: -0.055em">{html}</h2>
<div style="position: absolute; right: 0; bottom: 4px">{stamp()}</div>
</div>"""


def real_footer(text, nxt):
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 22px">
<span style="{MONO}; font-size: 28px; letter-spacing: 0.14em; color: #FF6A1A; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 2.4s both">✓ REALIDAD</span>
<p style="margin: 0; font-family: 'Instrument Serif', serif; font-style: italic; font-size: 60px; line-height: 1.06; color: #D9D1C8; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 2.7s both">{text}</p>
<div style="display: flex; align-items: center; justify-content: flex-end; gap: 16px; margin-top: 6px"><span style="{MONO}; font-size: 28px; letter-spacing: 0.1em; color: #FF6A1A">{nxt}</span>{ARROW}</div>
</div>"""


def swap_label(bad, good, dur=7.5, top=120):
    return (f'<div style="position: absolute; left: 50%; top: {top}px; transform: translateX(-50%); z-index: 5; white-space: nowrap">'
            f'<div style="padding: 14px 28px; border-radius: 18px; background: {BAD}; color: #0A0908; font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; font-size: 36px; animation: aSwap {dur}s ease-in-out infinite">{bad}</div>'
            f'<div style="position: absolute; left: 50%; top: 0; transform: translateX(-50%); padding: 14px 28px; border-radius: 18px; background: #FF6A1A; color: #0A0908; font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; font-size: 36px; animation: aSwapB {dur}s ease-in-out infinite">{good}</div></div>')


SWAP_CSS = """@keyframes aSwap{0%,42%{opacity:1}50%,92%{opacity:0}100%{opacity:1}}
@keyframes aSwapB{0%,42%{opacity:0}50%,92%{opacity:1}100%{opacity:0}}"""

# ---------------- H1: gancho ----------------
myths = ['Necesito equipo caro', 'No soy fotogénico', 'Todo a la primera']
cards = ''
for i, m in enumerate(myths):
    d = 1.8 + i * 1.5
    cards += (f'<div style="position: relative; display: flex; align-items: center; justify-content: space-between; gap: 20px; padding: 36px 36px; border-radius: 30px; '
              f'background: #171412; border: 2px solid rgba(255,90,100,0.35); animation: aPop .7s cubic-bezier(.2,.8,.2,1) {0.9 + i*0.3:.1f}s both, aBob 4s ease-in-out {-i*1.3:.1f}s infinite">'
              f'<div style="display: flex; flex-direction: column; gap: 8px"><span style="{MONO}; font-size: 24px; letter-spacing: 0.14em; color: {BAD}">MITO 0{i+1}</span>'
              f'<span style="position: relative; display: inline-block; font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; font-size: 50px; letter-spacing: -0.03em">“{m}”<span style="position: absolute; left: -6px; right: -6px; top: 54%; height: 5px; border-radius: 9px; background: rgba(255,90,100,0.9); transform-origin: left; animation: aStrike .5s ease-out {d+0.2:.1f}s both"></span></span></div>'
              f'<div style="position: absolute; right: 26px; top: 50%; margin-top: -40px; animation: aThump .4s ease-out {d+0.35:.1f}s both">{stamp("FALSO", d, 44)}</div>'
              f'</div>')
h1_css = STAMP_CSS + """
@keyframes aStrike{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes aScan{0%{top:6%}50%{top:90%}100%{top:6%}}"""
H1 = HEAD % ('Historia 1 · Mitos al grabarte', h1_css, 1) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 56px">
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 124px; line-height: 0.93; letter-spacing: -0.055em">Lo que crees<br>de la cámara<br><span style="{SERIF}">es mentira.</span></h1>

<div style="position: relative; {PANEL}; padding: 112px 40px 44px; display: flex; flex-direction: column; gap: 28px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="position: absolute; inset: 0; background: radial-gradient(circle at 50% 30%, rgba(255,106,26,0.14), rgba(10,9,8,0) 65%)"></div>
{rec_bar('MITO vs REALIDAD')}
{cards}
<div style="position: absolute; left: 40px; right: 40px; height: 3px; background: linear-gradient(90deg, rgba(255,106,26,0), #FF6A1A, rgba(255,106,26,0)); box-shadow: 0 0 20px #FF6A1A; animation: aScan 5s ease-in-out infinite"></div>
</div>
</div>

<div style="position: relative; display: flex; align-items: center; justify-content: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 1.2s both">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 50px; letter-spacing: -0.03em">3 mitos que te frenan a grabarte</span>
<svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; animation: aNudge 1.4s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
</div>
""" + TAIL

# ---------------- H2: equipo caro ----------------
def slider(name, kf, delay=0):
    return (f'<div style="display: grid; grid-template-columns: 190px 1fr; align-items: center; gap: 24px">'
            f'<span style="{MONO}; font-size: 26px; letter-spacing: 0.1em; color: #B5ADA4">{name}</span>'
            f'<div style="position: relative; height: 18px; border-radius: 99px; background: #1E1A17">'
            f'<div style="position: absolute; left: 0; top: 0; bottom: 0; border-radius: 99px; background: linear-gradient(90deg, #FF8F45, #FF6A1A); animation: {kf} 7.5s cubic-bezier(.6,0,.3,1) infinite">'
            f'<span style="position: absolute; right: -19px; top: 50%; width: 38px; height: 38px; margin-top: -19px; border-radius: 99px; background: #F2EDE7; box-shadow: 0 0 22px rgba(255,106,26,0.8)"></span></div></div></div>')

wave = ''
for i in range(34):
    h = 20 + (i * 37) % 60
    wave += (f'<span style="flex: 1; height: {h}%; border-radius: 6px; background: #F2EDE7; transform-origin: center; '
             f'animation: aWv {0.5 + (i % 6) * 0.11:.2f}s ease-in-out {-(i * 0.07):.2f}s infinite alternate"></span>')
h2_p = person(250, 'linear-gradient(160deg, #3A4A6B, #25324F)')
h2_css = STAMP_CSS + '\n' + SWAP_CSS + """
@keyframes kCam{0%,42%{width:96%}50%,92%{width:42%}100%{width:96%}}
@keyframes kLuz{0%,42%{width:14%}50%,92%{width:90%}100%{width:14%}}
@keyframes kSon{0%,42%{width:18%}50%,92%{width:88%}100%{width:18%}}
@keyframes kMeter{0%,42%{width:24%;background:#FF5A64}50%,92%{width:94%;background:#FF6A1A}100%{width:24%;background:#FF5A64}}
@keyframes kDark{0%,42%{opacity:.78}50%,92%{opacity:0}100%{opacity:.78}}
@keyframes kNoise{from{background-position:0 0,0 0}to{background-position:40px 26px,-30px 40px}}
@keyframes kWvCol{0%,42%{opacity:.35;filter:blur(1.5px)}50%,92%{opacity:1;filter:none}100%{opacity:.35;filter:blur(1.5px)}}
@keyframes aWv{from{transform:scaleY(.35)}to{transform:scaleY(1)}}"""
H2 = HEAD % ('Historia 2 · Equipo caro', h2_css, 2) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{myth_heading(1, f'“Necesito<br>una cámara<br><span style="{SERIF}">carísima.”</span>', 100)}

<div style="position: relative; {PANEL}; padding: 40px 44px 44px; display: flex; flex-direction: column; gap: 30px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="position: relative; height: 300px; border-radius: 30px; overflow: hidden; background: radial-gradient(circle at 50% 40%, #2A3550, #0B1224 75%)">
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -125px">{h2_p}</div>
<div style="position: absolute; inset: 0; background: #000; animation: kDark 7.5s ease-in-out infinite"></div>
<div style="position: absolute; inset: 0; background-image: radial-gradient(rgba(242,237,231,0.35) 1px, transparent 1.5px), radial-gradient(rgba(242,237,231,0.2) 1px, transparent 1.5px); background-size: 7px 7px, 11px 11px; animation: kNoise .25s steps(3) infinite, kDark 7.5s ease-in-out infinite"></div>
<div style="position: absolute; left: 24px; right: 24px; bottom: 18px; height: 56px; display: flex; align-items: center; gap: 5px; animation: kWvCol 7.5s ease-in-out infinite">{wave}</div>
{swap_label('✕ Cámara top · se ve mal', '✓ Buena luz y sonido', top=22)}
</div>
{slider('CÁMARA', 'kCam')}
{slider('LUZ', 'kLuz')}
{slider('SONIDO', 'kSon')}
<div style="display: flex; flex-direction: column; gap: 14px; padding-top: 6px; border-top: 2px solid rgba(242,237,231,0.08)">
<div style="display: flex; justify-content: space-between; {MONO}; font-size: 24px; letter-spacing: 0.1em; color: #9C938B; padding-top: 16px"><span>CÓMO SE VE Y SE OYE</span><span>EJEMPLO</span></div>
<div style="height: 22px; border-radius: 99px; background: #1E1A17; overflow: hidden"><div style="height: 100%; border-radius: 99px; animation: kMeter 7.5s cubic-bezier(.6,0,.3,1) infinite"></div></div>
</div>
</div>
</div>

{real_footer('La luz y el sonido<br><span style="color: #F2EDE7">pesan más que la cámara.</span>', 'SIGUIENTE MITO')}
""" + TAIL

# ---------------- H3: no soy fotogénico ----------------
def lit_person(w):
    hh = int(w * 0.42)
    return f"""<div style="position: relative; width: {w}px; height: {int(w*1.02)}px; transform-origin: 50% 100%; animation: kSway 7.5s ease-in-out infinite">
<div style="position: absolute; left: 50%; top: 0; width: {hh}px; height: {int(hh*1.15)}px; margin-left: -{hh//2}px; border-radius: 999px; overflow: hidden; background: #6B635C">
<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #F2EDE7 0%, #9C938B 30%, #1E1A17 78%); animation: aSwap 7.5s ease-in-out infinite"></div>
<div style="position: absolute; inset: 0; background: linear-gradient(100deg, #F2EDE7 0%, #D9D1C8 40%, #9C938B 85%); animation: aSwapB 7.5s ease-in-out infinite"></div>
<div style="position: absolute; left: 22%; right: 22%; top: 62%; height: 26%; border-radius: 50%; background: rgba(10,9,8,0.75); filter: blur(10px); animation: aSwap 7.5s ease-in-out infinite"></div>
<div style="position: absolute; left: 30%; right: 30%; top: 64%; height: 10px; border-radius: 0 0 40px 40px; border-bottom: 5px solid rgba(10,9,8,0.6); animation: aSwapB 7.5s ease-in-out infinite"></div>
</div>
<div style="position: absolute; left: 50%; top: {int(hh*1.05)}px; width: {int(hh*0.34)}px; height: {int(hh*0.3)}px; margin-left: -{int(hh*0.17)}px; background: #6B635C"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: {int(w*0.52)}px; border-radius: {int(w*0.4)}px {int(w*0.4)}px 30px 30px; background: linear-gradient(160deg, #3A4A6B, #25324F)"></div>
</div>"""

h3_css = STAMP_CSS + '\n' + SWAP_CSS + """
@keyframes kSway{0%,42%{transform:rotate(0)}55%{transform:rotate(-2.5deg)}68%{transform:rotate(2deg)}80%{transform:rotate(-1.5deg)}92%{transform:rotate(0)}100%{transform:rotate(0)}}
@keyframes kFlick{0%,100%{opacity:1}47%{opacity:.6}49%{opacity:1}}"""
H3 = HEAD % ('Historia 3 · No soy fotogénico', h3_css, 3) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{myth_heading(2, f'“No soy<br><span style="{SERIF}">fotogénico.”</span>')}

<div style="align-self: stretch; position: relative; height: 700px; {PANEL}; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{rec_bar('VISOR')}
{corners('rgba(242,237,231,0.6)')}
<div style="position: absolute; inset: 0; animation: aSwap 7.5s ease-in-out infinite">
<div style="position: absolute; left: 50%; top: 96px; width: 200px; height: 26px; margin-left: -100px; border-radius: 10px; background: #F2EDE7; box-shadow: 0 0 60px 10px rgba(242,237,231,0.6); animation: kFlick 1.3s linear infinite"></div>
<div style="position: absolute; left: 50%; top: 122px; width: 560px; height: 560px; margin-left: -280px; background: linear-gradient(180deg, rgba(242,237,231,0.22), rgba(242,237,231,0)); clip-path: polygon(40% 0, 60% 0, 100% 100%, 0 100%)"></div>
</div>
<div style="position: absolute; inset: 0; animation: aSwapB 7.5s ease-in-out infinite">
<div style="position: absolute; left: 44px; top: 210px; width: 120px; height: 190px; border-radius: 22px; background: linear-gradient(180deg, #FFFFFF, #D9D1C8); box-shadow: 0 0 90px 24px rgba(255,106,26,0.55); transform: rotate(-8deg)"></div>
<div style="position: absolute; left: 130px; top: 150px; width: 640px; height: 420px; background: linear-gradient(90deg, rgba(255,178,122,0.28), rgba(255,178,122,0)); clip-path: polygon(0 30%, 100% 0, 100% 100%, 0 70%)"></div>
</div>
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -210px">{lit_person(420)}</div>
{swap_label('✕ Luz de techo · rígido', '✓ Luz suave · natural', top=110)}
</div>
</div>

{real_footer('No es tu cara, es la luz.<br><span style="color: #F2EDE7">Y hablar como hablas.</span>', 'SIGUIENTE MITO')}
""" + TAIL

# ---------------- H4: a la primera ----------------
TK = 2.3
good_idx = {1, 4, 5}
takes = ''
final = ''
for i in range(6):
    d = 0.9 + i * TK
    col = '#FF6A1A' if i in good_idx else BAD
    mark = '✓' if i in good_idx else '✕'
    anim = f'aPop .5s cubic-bezier(.2,.8,.2,1) {d:.1f}s both' + ('' if i in good_idx else f', aCut .6s ease-in {d+1.2:.1f}s forwards')
    takes += (f'<div style="flex: 1; height: 86px; border-radius: 16px; background: {col}; color: #0A0908; display: flex; align-items: center; justify-content: center; '
              f"font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 34px; animation: {anim}\">{mark} {i+1}</div>")
for j, i in enumerate(sorted(good_idx)):
    d = 0.9 + i * TK + 1.0
    final += (f'<div style="flex: 1; height: 86px; border-radius: 16px; background: linear-gradient(135deg, #FF8F45, #FF6A1A); color: #0A0908; display: flex; align-items: center; justify-content: center; '
              f"font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 32px; animation: aDrop .6s cubic-bezier(.2,.8,.2,1) {d:.1f}s both\">TOMA {i+1}</div>")
h4_css = STAMP_CSS + """
@property --t{syntax:'<integer>';inherits:false;initial-value:1}
@keyframes aTk{from{--t:1}to{--t:6}}
.tk{counter-reset:t var(--t);animation:aTk 11.5s steps(5,jump-none) .9s both}
.tk::after{content:counter(t)}
@keyframes aClap{0%{transform:rotate(-24deg)}18%{transform:rotate(0)}100%{transform:rotate(0)}}
@keyframes aCut{to{opacity:.42;transform:scale(.9);filter:saturate(.4)}}
@keyframes aDrop{from{opacity:0;transform:translateY(-110px) scale(.8)}to{opacity:1;transform:none}}
@keyframes aHead{from{left:0}to{left:100%}}"""
CLAP_STRIPES = 'repeating-linear-gradient(135deg, #F2EDE7 0 34px, #0A0908 34px 68px)'
H4 = HEAD % ('Historia 4 · A la primera', h4_css, 4) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 40px">
{myth_heading(3, f'“Tiene que<br>salir a la<br><span style="{SERIF}">primera.”</span>', 100)}

<div style="position: relative; {PANEL}; padding: 40px 44px 44px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="display: flex; align-items: center; gap: 34px">
<div style="position: relative; width: 300px; flex-shrink: 0; padding-top: 50px">
<div style="position: absolute; left: 0; top: 0; width: 300px; height: 44px; border-radius: 10px; background: {CLAP_STRIPES}; transform-origin: 6px 40px; animation: aClap {TK}s cubic-bezier(.5,0,.3,1.4) .9s infinite"></div>
<div style="height: 170px; border-radius: 16px; background: #0A0908; border: 3px solid rgba(242,237,231,0.2); display: flex; flex-direction: column; justify-content: center; padding: 0 26px; gap: 4px">
<span style="{MONO}; font-size: 24px; letter-spacing: 0.14em; color: #9C938B">TOMA</span>
<span class="tk" style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 96px; line-height: 1; color: #F2EDE7"></span></div>
</div>
<p style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 46px; line-height: 1.05; letter-spacing: -0.03em">Repetir es <span style="{SERIF}">parte</span><br>del trabajo.</p>
</div>
<div style="display: flex; flex-direction: column; gap: 14px">
<span style="{MONO}; font-size: 24px; letter-spacing: 0.12em; color: #9C938B">TOMAS GRABADAS</span>
<div style="position: relative; display: flex; gap: 12px">{takes}</div>
<span style="{MONO}; font-size: 24px; letter-spacing: 0.12em; color: #FF6A1A; margin-top: 8px">MONTAJE FINAL</span>
<div style="position: relative; display: flex; gap: 12px; padding: 12px; border-radius: 22px; background: #171412; border: 2px dashed rgba(255,106,26,0.35)">{final}
<div style="position: absolute; top: -6px; bottom: -6px; width: 5px; margin-left: -2px; border-radius: 9px; background: #F2EDE7; box-shadow: 0 0 18px #FF6A1A; animation: aHead 5s linear infinite"></div></div>
</div>
</div>
</div>

{real_footer('Todos repiten tomas.<br><span style="color: #F2EDE7">Lo bueno se queda en edición.</span>', 'ÚLTIMO PASO')}
""" + TAIL

# ---------------- H5: remate + CTA (martes: reserva) ----------------
reals = [('Equipo caro', 'Luz y sonido primero'), ('No soy fotogénico', 'Buena luz y naturalidad'), ('A la primera', 'Repetir es normal')]
rows = ''
for i, (m, r) in enumerate(reals):
    d = 1.2 + i * 0.9
    rows += (f'<div style="display: flex; align-items: center; gap: 26px; padding: 20px 28px; border-radius: 26px; background: #171412; border: 1px solid rgba(242,237,231,0.1); animation: aRow .6s ease-out {d:.1f}s both">'
             f'<span style="flex-shrink: 0; width: 60px; height: 60px; border-radius: 18px; border: 3px solid rgba(242,237,231,0.3); display: flex; align-items: center; justify-content: center; animation: aChk .5s ease-out {d+0.3:.1f}s both">'
             f'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5 9-10" style="stroke-dasharray: 30; stroke-dashoffset: 30; animation: aDash .5s ease-out {d+0.4:.1f}s both"></path></svg></span>'
             f'<span style="display: flex; flex-direction: column; gap: 4px"><span style="{MONO}; font-size: 22px; letter-spacing: 0.08em; color: {BAD}; text-decoration: line-through">{m.upper()}</span>'
             f'<span style="font-size: 42px; font-weight: 700; letter-spacing: -0.01em">{r}</span></span></div>')
h5_css = """@keyframes aRow{from{opacity:.35}to{opacity:1}}
@keyframes aChk{from{background:rgba(255,106,26,0);border-color:rgba(242,237,231,.3)}to{background:#FF6A1A;border-color:#FF6A1A}}
@keyframes aDash{to{stroke-dashoffset:0}}
@keyframes aFill{from{width:0}to{width:100%}}"""
H5 = HEAD % ('Historia 5 · Reserva tu sesión', h5_css, 5) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 44px">
{heading('<span style="display: inline-flex; align-items: center; gap: 14px"><span style="width: 18px; height: 18px; border-radius: 99px; background: ' + BAD + '; animation: aBlink 1s steps(1) infinite"></span>REC</span>', f'Solo te falta<br><span style="{SERIF}">darle a REC.</span>')}

<div style="border-radius: 44px; background: rgba(18,16,15,0.94); border: 1px solid rgba(242,237,231,0.12); padding: 36px 40px; display: flex; flex-direction: column; gap: 16px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
<div style="display: flex; justify-content: space-between; {MONO}; font-size: 26px; letter-spacing: 0.1em; margin-bottom: 6px"><span style="color: #FF6A1A">MITO → REALIDAD</span><span style="color: #9C938B">GUÁRDALA</span></div>
{rows}
<div style="height: 14px; border-radius: 99px; background: #171412; overflow: hidden; margin-top: 8px"><div style="height: 100%; border-radius: 99px; background: linear-gradient(90deg, #FF6A1A, #FFB27A); animation: aFill 3.4s ease-in-out 1.2s both"></div></div>
</div>
</div>

<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .9s both">
<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="animation: aBob 2s ease-in-out infinite"><path d="M6 15l6-6 6 6"></path></svg>
<div style="position: relative; overflow: hidden; padding: 26px 50px; border-radius: 999px; background: #FF6A1A; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 52px; letter-spacing: -0.03em; white-space: nowrap; box-shadow: 0 30px 90px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Escríbenos ESTUDIO por DM<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.4), rgba(255,255,255,0)); animation: aShim 4s ease-in-out .6s infinite"></div></div>
<span style="font-family: 'Instrument Serif', serif; font-style: italic; font-size: 48px; color: #F2EDE7">y reserva tu sesión en Burgos</span>
<span style="{MONO}; font-size: 26px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>
</div>
""" + TAIL

for n, s in enumerate([H1, H2, H3, H4, H5], 1):
    open(os.path.join(HERE, f'H{n}.dc.html'), 'w').write(s)
print('ok')
