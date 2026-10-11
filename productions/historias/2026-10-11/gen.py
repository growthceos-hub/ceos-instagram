#!/usr/bin/env python3
"""Genera H1..H5.dc.html (serie 2026-10-11: mito vs realidad, 3 mitos del móvil que estropean tus vídeos).
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





# ================= serie 2026-10-10: exposición con el móvil (3 pasos) =================
def bad_chip(text, top, delay, left=None, right=None):
    pos = f'top: {top}px; ' + (f'left: {left}px' if left is not None else f'right: {right}px')
    return (f'<div style="position: absolute; {pos}; z-index: 5; display: flex; align-items: center; gap: 12px; padding: 16px 26px; border-radius: 20px; '
            f"background: {BAD}; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 40px; letter-spacing: -0.02em; "
            f'white-space: nowrap; box-shadow: 0 24px 60px -12px rgba(0,0,0,0.8); animation: aPop .7s cubic-bezier(.2,.8,.2,1) {delay}s both, aBob 2.4s ease-in-out {delay+0.7:.1f}s infinite">✕ {text}</div>')


def fix_heading(n, html, size=108):
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both">
<span style="display: flex; align-items: center; gap: 14px; {MONO}; font-size: 28px; letter-spacing: 0.14em; color: #FF6A1A"><span style="width: 16px; height: 16px; border-radius: 99px; background: #FF6A1A; animation: aBlink 1.2s steps(1) infinite"></span>PASO {n} DE 3</span>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: {size}px; line-height: 0.95; letter-spacing: -0.055em">{html}</h2>
</div>"""


def label_swap(bad, good, style):
    return (f'<div style="position: absolute; {style}; z-index: 6; {MONO}; font-weight: 600; font-size: 28px; letter-spacing: 0.1em; white-space: nowrap">'
            f'<span style="position: absolute; left: 0; top: 0; color: {BAD}; animation: aSwap {CYCLE}s ease-in-out infinite">{bad}</span>'
            f'<span style="position: absolute; left: 0; top: 0; color: #FF6A1A; animation: aSwapB {CYCLE}s ease-in-out infinite">{good}</span></div>')


COMMON_CSS += """
@keyframes kHunt{0%{filter:brightness(1)}18%{filter:brightness(1.75) saturate(.6)}36%{filter:brightness(.42)}54%{filter:brightness(1.6) saturate(.6)}72%{filter:brightness(.5)}100%{filter:brightness(1)}}
@keyframes kEv{0%{transform:translateX(0)}18%{transform:translateX(150px)}36%{transform:translateX(-150px)}54%{transform:translateX(130px)}72%{transform:translateX(-120px)}100%{transform:translateX(0)}}
@keyframes kTap{0%,46%{opacity:0;transform:scale(1.6)}52%{opacity:1;transform:scale(.9)}58%,92%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(1)}}
@keyframes kRipple{0%,48%{opacity:0;transform:scale(.3)}52%{opacity:.9;transform:scale(.3)}70%,100%{opacity:0;transform:scale(2.4)}}
@keyframes kKnob{0%,42%{transform:translateY(0)}52%,92%{transform:translateY(120px)}100%{transform:translateY(0)}}
@keyframes kZebra{from{background-position:0 0}to{background-position:40px 0}}
@keyframes kRay{0%,100%{opacity:.35}50%{opacity:.9}}
@keyframes kHunt2{0%{filter:brightness(1)}18%{filter:brightness(2.2) saturate(.4)}36%{filter:brightness(.3)}54%{filter:brightness(2) saturate(.4)}72%{filter:brightness(.35)}100%{filter:brightness(1)}}
@keyframes kFlare{0%,100%{opacity:.85;transform:scale(1)}50%{opacity:1;transform:scale(1.05)}}"""

skin = 'background-color: #C9A58C'
SUN = lambda s, c='#FF6A1A': (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" aria-hidden="true">'
                              '<circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"></path></svg>')


def ev_meter(anim):
    ticks = ''.join(f'<span style="width: 4px; height: {34 if i % 5 == 0 else 18}px; background: rgba(242,237,231,{0.85 if i % 5 == 0 else 0.4})"></span>' for i in range(21))
    return (f'<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 10px">'
            f'<div style="position: relative; width: 420px; display: flex; justify-content: space-between; align-items: flex-end">{ticks}'
            f'<span style="position: absolute; left: 50%; bottom: -14px; width: 0; height: 0; margin-left: -14px; border: 14px solid transparent; border-bottom-color: #FF6A1A; animation: {anim}"></span></div>'
            f'<div style="width: 420px; display: flex; justify-content: space-between; {MONO}; font-size: 22px; color: #9C938B; margin-top: 14px"><span>-2</span><span>0</span><span>+2</span></div></div>')


# ================= serie 2026-10-11: mito vs realidad (3 mitos del móvil) =================
COMMON_CSS += """
@keyframes kStrike{0%,18%{transform:scaleX(0)}28%,100%{transform:scaleX(1)}}
@keyframes kZoomBad{0%,42%{transform:scale(1.7)}50%,92%{transform:scale(1.7)}100%{transform:scale(1.7)}}
@keyframes kPinch{0%,6%{transform:translate(0,0)}36%,100%{transform:translate(-70px,70px)}}
@keyframes kPinch2{0%,6%{transform:translate(0,0)}36%,100%{transform:translate(70px,-70px)}}
@keyframes kPhoneIn{0%,42%{transform:translateY(0) scale(1)}50%,92%{transform:translateY(-20px) scale(1.06)}100%{transform:translateY(0) scale(1)}}
@keyframes kFlip{0%,40%{transform:rotateY(0)}50%,90%{transform:rotateY(180deg)}100%{transform:rotateY(360deg)}}
@keyframes kWipe{0%,30%{transform:translateX(-800px) rotate(-8deg)}48%{transform:translateX(800px) rotate(8deg)}100%{transform:translateX(800px) rotate(8deg)}}
@keyframes kHaze{0%,36%{opacity:1}48%,100%{opacity:0}}
@keyframes kClear{0%,36%{opacity:0}48%,100%{opacity:1}}
@keyframes kSpin{from{transform:rotate(0)}to{transform:rotate(360deg)}}"""


def myth_heading(n, myth, size=104):
    lines = ''
    for i, ln in enumerate(myth.split('<br>')):
        lines += (f'<span style="position: relative; display: inline-block; align-self: flex-start">{ln}'
                  f'<span style="position: absolute; left: -8px; right: -8px; top: 54%; height: 11px; margin-top: -5px; border-radius: 9px; background: {BAD}; transform-origin: left; animation: kStrike 6s cubic-bezier(.6,0,.3,1) {0.4 + i*0.5:.1f}s both"></span></span>')
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both">
<span style="display: flex; align-items: center; gap: 14px; {MONO}; font-size: 28px; letter-spacing: 0.14em; color: {BAD}"><span style="width: 16px; height: 16px; border-radius: 99px; background: {BAD}; animation: aBlink 1.2s steps(1) infinite"></span>MITO {n} DE 3</span>
<h2 style="margin: 0; display: flex; flex-direction: column; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: {size}px; line-height: 0.95; letter-spacing: -0.055em; color: #D9D1C8">{lines}</h2>
</div>"""


def reality(text, nxt):
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 26px">
<span style="align-self: flex-start; padding: 10px 22px; border-radius: 12px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 28px; letter-spacing: 0.14em; animation: aPop .7s cubic-bezier(.2,.8,.2,1) 1.2s both">✓ REALIDAD</span>
<p style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 700; font-size: 60px; line-height: 1.04; letter-spacing: -0.03em; color: #F2EDE7; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 1.4s both">{text}</p>
<div style="display: flex; align-items: center; justify-content: flex-end; gap: 16px"><span style="{MONO}; font-size: 28px; letter-spacing: 0.1em; color: #FF6A1A">{nxt}</span>{ARROW}</div>
</div>"""


skin = 'background-color: #C9A58C'
PIX = ('<div style="position: absolute; inset: 0; z-index: 3; background-image: linear-gradient(rgba(10,9,8,0.35) 2px, transparent 2px), '
       'linear-gradient(90deg, rgba(10,9,8,0.35) 2px, transparent 2px); background-size: 34px 34px"></div>')
BG = 'radial-gradient(circle at 50% 35%, #22324D, #0A0908 75%)'

# ---------------- H1: gancho ----------------
h1_scene = (rec_bar('1080P · 30')
            + f'<div style="position: absolute; inset: 0; background: {BG}"></div>'
            + f'<div style="position: absolute; left: 50%; bottom: 60px; margin-left: -170px; z-index: 2; filter: blur(7px) brightness(1.1) saturate(.7); animation: aBreathe 3s ease-in-out infinite">{face(340, skin)}</div>'
            + PIX
            + bad_chip('Zoom digital', 110, 1.0, left=46)
            + bad_chip('Cámara de selfie', 200, 1.8, right=46)
            + bad_chip('Lente con huellas', 290, 2.6, left=60))
H1 = HEAD % ('Historia 1 · 3 mitos del móvil', COMMON_CSS, 1) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 46px">
<div style="display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both">
<span style="{MONO}; font-size: 28px; letter-spacing: 0.14em; color: #FF6A1A">MITO VS REALIDAD</span>
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 118px; line-height: 0.93; letter-spacing: -0.055em">3 mitos del móvil<br><span style="{SERIF}">que te roban calidad.</span></h1>
</div>
<div style="position: relative; {PANEL}; padding: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(h1_scene, 760)}
</div>
</div>

<div style="position: relative; display: flex; align-items: center; justify-content: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) 1.2s both">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 52px; letter-spacing: -0.03em">¿Cuántos te creías?</span>
<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; animation: aNudge 1.4s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
</div>
""" + TAIL

# ---------------- H2: zoom digital ----------------
fingers = (f'<div style="position: absolute; left: 50%; top: 330px; z-index: 6; animation: aSwap {CYCLE}s ease-in-out infinite">'
           f'<div style="position: absolute; left: -40px; top: -40px; width: 64px; height: 64px; border-radius: 99px; background: rgba(242,237,231,0.55); border: 3px solid #F2EDE7; animation: kPinch 2.5s ease-in-out infinite"></div>'
           f'<div style="position: absolute; left: -24px; top: -24px; width: 64px; height: 64px; border-radius: 99px; background: rgba(242,237,231,0.55); border: 3px solid #F2EDE7; animation: kPinch2 2.5s ease-in-out infinite"></div></div>')
zoom_pill = (f'<div style="position: absolute; left: 50%; bottom: 40px; transform: translateX(-50%); z-index: 6; display: flex; gap: 14px">'
             + ''.join(f'<span style="position: relative; width: 92px; height: 92px; border-radius: 99px; background: rgba(10,9,8,0.75); border: 2px solid rgba(242,237,231,0.3); display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 28px; color: #F2EDE7">'
                       f'<span style="position: absolute; inset: -2px; border-radius: 99px; border: 4px solid {c}; animation: {a} {CYCLE}s ease-in-out infinite"></span>{t}</span>'
                       for t, c, a in [('1x', '#FF6A1A', 'aSwapB'), ('5x', BAD, 'aSwap')]) + '</div>')
h2_scene = (f'<div style="position: absolute; inset: 0; background: {BG}"></div>'
            f'<div style="position: absolute; inset: 0; z-index: 2; animation: aSwap {CYCLE}s ease-in-out infinite">'
            f'<div style="position: absolute; left: 50%; bottom: -40px; margin-left: -170px; transform: scale(1.7); transform-origin: 50% 30%; filter: blur(8px) saturate(.75)">{face(340, skin)}</div>{PIX}</div>'
            f'<div style="position: absolute; inset: 0; z-index: 2; animation: aSwapB {CYCLE}s ease-in-out infinite">'
            f'<div style="position: absolute; left: 50%; bottom: -40px; margin-left: -170px; transform: scale(1.7); transform-origin: 50% 30%">{face(340, skin)}</div></div>'
            + fingers + zoom_pill
            + swap_tag('Zoom con los dedos', 'Móvil más cerca, en 1x', 34))
H2 = HEAD % ('Historia 2 · Mito del zoom', COMMON_CSS, 2) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 40px">
{myth_heading(1, '“Haz zoom<br>y listo.”', 112)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(h2_scene, 640)}
{ab_bar()}
</div>
</div>

{reality('El zoom digital solo recorta<br>y pierde nitidez. Acércate tú.', 'MITO 2')}
""" + TAIL

# ---------------- H3: cámara frontal vs trasera ----------------
def phone_back():
    lens = lambda x, y: (f'<span style="position: absolute; left: {x}px; top: {y}px; width: 56px; height: 56px; border-radius: 99px; background: radial-gradient(circle at 40% 40%, #3A4F75, #05080F 70%); border: 5px solid #2A2725"></span>')
    return (f'<div style="position: absolute; inset: 0; border-radius: 46px; background: linear-gradient(160deg, #2A2725, #12100F); border: 3px solid rgba(242,237,231,0.2); backface-visibility: hidden; transform: rotateY(180deg)">'
            f'<div style="position: absolute; left: 22px; top: 22px; width: 150px; height: 150px; border-radius: 34px; background: #1E1B19">{lens(14, 14)}{lens(80, 14)}{lens(14, 80)}</div>'
            f'<span style="position: absolute; left: 0; right: 0; bottom: 40px; text-align: center; {MONO}; font-weight: 600; font-size: 26px; letter-spacing: 0.12em; color: #FF6A1A">TRASERA ✓</span></div>')


def phone_front():
    return (f'<div style="position: absolute; inset: 0; border-radius: 46px; background: #0A0908; border: 3px solid rgba(242,237,231,0.2); overflow: hidden; backface-visibility: hidden">'
            f'<div style="position: absolute; left: 50%; top: 18px; width: 90px; height: 26px; margin-left: -45px; border-radius: 99px; background: #000; border: 2px solid #2A2725"></div>'
            f'<div style="position: absolute; left: 50%; top: 70px; margin-left: -80px; filter: blur(3px) saturate(.7)">{face(160, skin)}</div>'
            f'<span style="position: absolute; left: 0; right: 0; bottom: 40px; text-align: center; {MONO}; font-weight: 600; font-size: 26px; letter-spacing: 0.12em; color: {BAD}">SELFIE ✕</span></div>')


phone = (f'<div style="position: absolute; left: 50px; top: 120px; width: 260px; height: 480px; perspective: 1400px; z-index: 4">'
         f'<div style="position: relative; width: 100%; height: 100%; transform-style: preserve-3d; animation: kFlip {CYCLE}s cubic-bezier(.6,0,.3,1) infinite">'
         f'{phone_front()}{phone_back()}</div></div>')
h3_scene = (f'<div style="position: absolute; inset: 0; background: {BG}"></div>'
            + phone
            + f'<div style="position: absolute; right: 30px; bottom: 30px; z-index: 2; animation: aSwap {CYCLE}s ease-in-out infinite"><div style="filter: blur(5px) saturate(.6) brightness(.9)">{face(380, skin)}</div></div>'
            + f'<div style="position: absolute; right: 30px; bottom: 30px; z-index: 2; animation: aSwapB {CYCLE}s ease-in-out infinite">{face(380, skin)}</div>'
            + swap_tag('Grabas con la de selfie', 'Grabas con la trasera', 34))
H3 = HEAD % ('Historia 3 · Mito de la cámara de selfie', COMMON_CSS, 3) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 40px">
{myth_heading(2, '“La de selfie<br>graba igual.”', 112)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(h3_scene, 640)}
{ab_bar()}
</div>
</div>

{reality('En casi todos los móviles<br>la trasera es mejor. Usa esa.', 'MITO 3')}
""" + TAIL

# ---------------- H4: lente con huellas ----------------
print_svg = ('<svg width="300" height="360" viewBox="0 0 100 120" fill="none" stroke="rgba(242,237,231,0.55)" stroke-width="1.6" aria-hidden="true">'
             + ''.join(f'<ellipse cx="50" cy="62" rx="{8+i*6}" ry="{10+i*7.5}"></ellipse>' for i in range(7)) + '</svg>')
haze = (f'<div style="position: absolute; inset: 0; z-index: 3; animation: kHaze {CYCLE}s ease-in-out infinite">'
        f'<div style="position: absolute; inset: 0; background: radial-gradient(circle at 50% 45%, rgba(242,237,231,0.42), rgba(242,237,231,0.12) 60%)"></div>'
        f'<div style="position: absolute; left: 50%; top: 110px; margin-left: -150px">{print_svg}</div></div>')
cloth = (f'<div style="position: absolute; left: 50%; top: 80px; width: 260px; height: 480px; margin-left: -130px; z-index: 5; border-radius: 40px; '
         f'background: repeating-linear-gradient(45deg, #EEF2F8 0 14px, #D5DDEA 14px 28px); box-shadow: 0 30px 80px -10px rgba(0,0,0,0.8); animation: kWipe {CYCLE}s cubic-bezier(.6,0,.3,1) infinite"></div>')
h4_scene = (f'<div style="position: absolute; inset: 0; background: {BG}"></div>'
            f'<div style="position: absolute; left: 50%; bottom: 30px; margin-left: -190px; z-index: 2; animation: kHaze {CYCLE}s ease-in-out infinite"><div style="filter: blur(6px) brightness(1.15) contrast(.75)">{face(380, skin)}</div></div>'
            f'<div style="position: absolute; left: 50%; bottom: 30px; margin-left: -190px; z-index: 2; animation: kClear {CYCLE}s ease-in-out infinite">{face(380, skin)}</div>'
            + haze + cloth
            + label_swap('HUELLA EN LA LENTE', 'LENTE LIMPIA', 'left: 50px; top: 130px')
            + swap_tag('Imagen con velo', 'Imagen nítida', 34))
H4 = HEAD % ('Historia 4 · Mito de la lente', COMMON_CSS, 4) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 40px">
{myth_heading(3, '“Si sale borroso,<br>es el móvil.”', 104)}
<div style="position: relative; {PANEL}; padding: 26px 26px 30px; display: flex; flex-direction: column; gap: 26px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{screen(h4_scene, 640)}
{ab_bar()}
</div>
</div>

{reality('Casi siempre es una huella.<br>Limpia la lente antes de grabar.', 'EL RESUMEN')}
""" + TAIL

# ---------------- H5: resumen + CTA (domingo: tips) ----------------
steps = [('Nada de zoom digital', 'acerca el móvil, en 1x'), ('Graba con la trasera', 'la de selfie, solo para mirar'), ('Limpia la lente', 'antes de cada grabación')]
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
{heading('ANTES DE DARLE A REC', f'Más calidad con<br><span style="{SERIF}">el mismo móvil.</span>')}

<div style="border-radius: 44px; background: rgba(18,16,15,0.94); border: 1px solid rgba(242,237,231,0.12); padding: 34px 38px; display: flex; flex-direction: column; gap: 16px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both">
{rows}
<div style="height: 14px; border-radius: 99px; background: #171412; overflow: hidden; margin-top: 8px"><div style="height: 100%; border-radius: 99px; background: linear-gradient(90deg, #FF6A1A, #FFB27A); animation: aFill 3.2s ease-in-out 1.2s both"></div></div>
</div>
</div>

<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .9s both">
<span style="font-family: 'Instrument Serif', serif; font-style: italic; font-size: 50px; color: #D9D1C8">¿Cuál de los 3 te creías?</span>
<div style="position: relative; overflow: hidden; padding: 28px 60px; border-radius: 999px; background: #FF6A1A; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 60px; letter-spacing: -0.03em; white-space: nowrap; box-shadow: 0 30px 90px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.4), rgba(255,255,255,0)); animation: aShim 4s ease-in-out .6s infinite"></div></div>
<span style="{MONO}; font-size: 28px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>
</div>
""" + TAIL

for n, s in enumerate([H1, H2, H3, H4, H5], 1):
    open(os.path.join(HERE, f'H{n}.dc.html'), 'w').write(s)
print('ok')
