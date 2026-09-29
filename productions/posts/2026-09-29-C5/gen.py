#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C5 2026-09-29 (cómo cerrar tu vídeo) en src/."""
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



# ============================================================ helpers C2 (fondo a cámara)
def corners(c='#F2EDE7'):
    return ''.join(
        f'<div style="position: absolute; {v}: 0; {h}: 0; width: 40px; height: 40px; border-{v}: 4px solid {c}; border-{h}: 4px solid {c}"></div>'
        for v in ('top', 'bottom') for h in ('left', 'right'))


def rec_timer():
    t = ''.join(
        f'<span style="position: absolute; right: 0; opacity: 0; animation: aStep 4s steps(1) {k-4}s infinite">00:00:0{k+1}</span>'
        for k in range(4))
    return (f'<div style="position: absolute; left: 70px; top: 34px; display: flex; align-items: center; gap: 10px; {MONO}; font-size: 20px; letter-spacing: .1em; color: #F2EDE7; z-index: 5"><span style="width: 14px; height: 14px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30; animation: aRec 1s steps(1) infinite"></span>REC</div>'
            f'<div style="position: absolute; right: 70px; top: 34px; width: 150px; height: 26px; {MONO}; font-size: 20px; letter-spacing: .08em; color: #F2EDE7; z-index: 5">{t}</div>')


def person(w):
    return PERSON.replace('width="420" height="420"', f'width="{w}" height="{w}"')



# ============================================================ figura de cuerpo entero (300x600) con articulaciones animables
ORIG = {'fig': '150px 330px', 'head': '150px 128px', 'armL': '96px 160px', 'foreL': '53px 241px',
        'armR': '204px 160px', 'foreR': '247px 241px', 'legL': '125px 300px', 'legR': '175px 300px',
        'shade': '150px 220px', 'gap': '90px 215px', 'jaw': '150px 120px'}


def figure(w, uid, a=None, pose='stiff', col='#F2EDE7'):
    a = a or {}
    relaxed = pose == 'relaxed'
    static = {'fig': 'scaleX(.82) rotate(-1.5deg)', 'armL': 'rotate(28deg)', 'foreL': 'rotate(-108deg)',
              'head': 'translate(4px,6px) rotate(-4deg)', 'legR': 'rotate(-6deg)'} if relaxed else {}

    def st(k, extra=''):
        s = f'transform-box: view-box; transform-origin: {ORIG[k]}'
        if k in a:
            s += f'; animation: {a[k]}'
        elif k in static:
            s += f'; transform: {static[k]}'
        return f'style="{s}{extra}"'
    shade_op = '.0' if not relaxed else '.45'
    gap_op = '0' if not relaxed else '1'
    return f'''<svg width="{w}" height="{w*2}" viewBox="0 0 300 600" style="display:block; overflow: visible">
<defs><linearGradient id="g{uid}" gradientUnits="userSpaceOnUse" x1="0" y1="20" x2="0" y2="580"><stop offset="0" stop-color="{col}" stop-opacity=".97"/><stop offset="1" stop-color="#B5ADA4" stop-opacity=".62"/></linearGradient>
<linearGradient id="h{uid}" gradientUnits="userSpaceOnUse" x1="0" y1="20" x2="0" y2="580"><stop offset="0" stop-color="#D9D1C8"/><stop offset="1" stop-color="#9C938B" stop-opacity=".7"/></linearGradient></defs>
<ellipse cx="150" cy="578" rx="92" ry="12" fill="#000" opacity=".45"/>
<g {st('fig')}>
 <g {st('legL')}><path d="M106 292 L148 292 L142 566 Q128 574 112 566 Z" fill="url(#h{uid})"/></g>
 <g {st('legR')}><path d="M152 292 L194 292 L188 566 Q172 574 158 566 Z" fill="url(#h{uid})"/></g>
 <rect x="136" y="112" width="28" height="44" rx="12" fill="url(#g{uid})"/>
 <path d="M84 156 Q150 132 216 156 L204 304 Q150 318 96 304 Z" fill="url(#g{uid})"/>
 <path d="M150 140 Q185 142 216 156 L204 304 Q178 312 150 312 Z" fill="#0A0908" {st('shade', f'; opacity: {shade_op}')} opacity=".0"/>
 <path d="M92 178 L62 236 L112 250 Z" fill="rgba(255,106,26,.22)" stroke="#FF6A1A" stroke-width="3" stroke-dasharray="7 6" {st('gap', f'; opacity: {gap_op}')}/>
 <g {st('armR')}><line x1="204" y1="160" x2="247" y2="241" stroke="url(#g{uid})" stroke-width="0"/>
  <line x1="206" y1="162" x2="212" y2="250" stroke="url(#g{uid})" stroke-width="26" stroke-linecap="round"/>
  <g {st('foreR')}><line x1="212" y1="250" x2="210" y2="334" stroke="url(#g{uid})" stroke-width="22" stroke-linecap="round"/><circle cx="210" cy="342" r="13" fill="url(#g{uid})"/></g></g>
 <g {st('armL')}>
  <line x1="94" y1="162" x2="53" y2="241" stroke="url(#g{uid})" stroke-width="0"/>
  <line x1="94" y1="162" x2="88" y2="250" stroke="url(#g{uid})" stroke-width="26" stroke-linecap="round"/>
  <g style="transform-box: view-box; transform-origin: 88px 250px{'; animation: ' + a['foreL'] if 'foreL' in a else ('; transform: rotate(-108deg)' if relaxed else '')}"><line x1="88" y1="250" x2="90" y2="334" stroke="url(#g{uid})" stroke-width="22" stroke-linecap="round"/><circle cx="90" cy="342" r="13" fill="url(#g{uid})"/></g></g>
 <g {st('head')}>
  <ellipse cx="150" cy="76" rx="40" ry="48" fill="url(#g{uid})"/>
  <rect x="129" y="72" width="12" height="6" rx="3" fill="#0A0908" opacity=".55"/><rect x="159" y="72" width="12" height="6" rx="3" fill="#0A0908" opacity=".55"/>
  <path d="M120 104 Q150 134 180 104" fill="none" stroke="#FF6A1A" stroke-width="4" stroke-linecap="round" {st('jaw', '; opacity: ' + ('1' if relaxed else '0'))}/>
 </g>
</g></svg>'''


def studio(glow=True):
    g = '<div style="position: absolute; left: 50%; top: 8%; width: 70%; height: 80%; margin-left: -35%; border-radius: 50%; background: radial-gradient(circle, rgba(255,106,26,.28), rgba(255,106,26,0) 70%); animation: aGlow 4s ease-in-out infinite"></div>' if glow else ''
    return f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #1C130D 0%, #12100F 70%, #0A0908 100%)"></div>{g}
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 16%; background: linear-gradient(180deg, #171412, #0A0908); border-top: 2px solid rgba(242,237,231,.06)"></div>'''


def softbox(side, anim='aSoft'):
    pos = 'left: 4%' if side == 'l' else 'right: 4%'
    rot = '14deg' if side == 'l' else '-14deg'
    return f'''<div style="position: absolute; {pos}; top: 12%; width: 110px; height: 300px; z-index: 2">
<div style="width: 110px; height: 150px; border-radius: 12px; background: linear-gradient(180deg, #FFFFFF, #D9D1C8); transform: perspective(300px) rotateY({rot}); box-shadow: 0 0 70px 18px rgba(255,178,122,.35); animation: {anim} 4s ease-in-out infinite"></div>
<div style="margin: 0 auto; width: 6px; height: 150px; background: #6B635C"></div></div>'''


COMMON_KF = """
@keyframes aStep{0%,24.9%{opacity:1}25%,100%{opacity:0}}
@keyframes aBreath{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-5px) scale(1.01)}}
@keyframes aPing{0%{transform:scale(.6);opacity:.9}100%{transform:scale(1.9);opacity:0}}
@keyframes aSoft{0%,100%{filter:brightness(1)}50%{filter:brightness(1.12)}}
"""


def pill(txt, bg='#FF3B30', fg='#fff', extra=''):
    return f'<div style="position: absolute; white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: {bg}; color: {fg}; {MONO}; font-weight: 600; font-size: 21px; letter-spacing: .08em; z-index: 6; {extra}">{txt}</div>'


E = 'cubic-bezier(.6,0,.3,1)'


def cycle(items, style=''):
    """4 textos que se alternan cada segundo (usa aStep)."""
    return ''.join(
        f'<span style="position: absolute; left: 0; right: 0; opacity: 0; animation: aStep 4s steps(1) {k-4}s infinite; {style}">{t}</span>'
        for k, t in enumerate(items))


# ---------------------------------------------------------------- 01 GANCHO
kf1 = COMMON_KF + """
@keyframes aProg{0%{width:0%}76%,100%{width:100%}}
@keyframes aSwipe{0%,78%{transform:translateY(0)}90%,99%{transform:translateY(-100%)}100%{transform:translateY(0)}}
@keyframes aNext{0%,78%{transform:translateY(100%)}90%,99%{transform:translateY(0)}100%{transform:translateY(100%)}}
@keyframes aFinger{0%,68%{opacity:0;transform:translateY(0) scale(.8)}72%{opacity:1;transform:translateY(0) scale(1)}88%{opacity:1;transform:translateY(-300px) scale(1)}94%,100%{opacity:0;transform:translateY(-320px) scale(.8)}}
@keyframes aX1{0%,76%{transform:scale(0);opacity:0}80%{transform:scale(1.3);opacity:1}84%,99%{transform:scale(1);opacity:1}100%{transform:scale(0);opacity:0}}
@keyframes aX2{0%,82%{transform:scale(0);opacity:0}86%{transform:scale(1.3);opacity:1}90%,99%{transform:scale(1);opacity:1}100%{transform:scale(0);opacity:0}}
@keyframes aX3{0%,88%{transform:scale(0);opacity:0}92%{transform:scale(1.3);opacity:1}95%,99%{transform:scale(1);opacity:1}100%{transform:scale(0);opacity:0}}
@keyframes aR1{0%,76%{border-color:rgba(242,237,231,.14);background:#12100F}80%,99%{border-color:#FF3B30;background:rgba(255,59,48,.12)}100%{border-color:rgba(242,237,231,.14);background:#12100F}}
@keyframes aR2{0%,82%{border-color:rgba(242,237,231,.14);background:#12100F}86%,99%{border-color:#FF3B30;background:rgba(255,59,48,.12)}100%{border-color:rgba(242,237,231,.14);background:#12100F}}
@keyframes aR3{0%,88%{border-color:rgba(242,237,231,.14);background:#12100F}92%,99%{border-color:#FF3B30;background:rgba(255,59,48,.12)}100%{border-color:rgba(242,237,231,.14);background:#12100F}}
@keyframes aSpin{to{transform:rotate(360deg)}}
@keyframes aWait{0%,74%{opacity:1}78%,100%{opacity:0}}
@keyframes aGone{0%,90%{opacity:0;transform:translateX(-50%) scale(.8)}93%,99%{opacity:1;transform:translateX(-50%) scale(1)}100%{opacity:0}}
@keyframes aEq{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
"""


def phone(w, h, inner, extra=''):
    return f'''<div style="position: relative; width: {w}px; height: {h}px; border-radius: 52px; background: #050505; padding: 14px; box-sizing: border-box; box-shadow: 0 0 0 3px rgba(242,237,231,.18), 0 50px 120px -30px rgba(255,106,26,.55); {extra}">
<div style="position: relative; width: 100%; height: 100%; border-radius: 40px; overflow: hidden; background: #0A0908">{inner}
<div style="position: absolute; left: 50%; top: 12px; width: 110px; height: 30px; margin-left: -55px; border-radius: 99px; background: #050505; z-index: 9"></div></div></div>'''


caps1 = cycle(['“…y ese es el truco”', '“…para grabar mejor.”', '“Bueno… pues eso.”', '“¡Chao!”'],
              f'{BRIC}; font-weight: 800; font-size: 32px; letter-spacing: -0.02em; text-align: center; color: #F2EDE7; text-shadow: 0 2px 12px #000, 0 0 4px #000')
reel1 = f'''
<div style="position: absolute; inset: 0; animation: aSwipe 4s {E} infinite">
  {studio()}
  <div style="position: absolute; left: 50%; bottom: -40px; margin-left: -210px; width: 420px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{person(420)}</div>
  <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 260px; background: linear-gradient(180deg, rgba(10,9,8,0), rgba(10,9,8,.85))"></div>
  <div style="position: absolute; left: 20px; right: 20px; top: 54px; height: 6px; border-radius: 99px; background: rgba(242,237,231,.25); z-index: 5"><div style="height: 100%; border-radius: 99px; background: #F2EDE7; animation: aProg 4s linear infinite"></div></div>
  <div style="position: absolute; left: 22px; top: 76px; {MONO}; font-size: 17px; letter-spacing: .1em; color: #F2EDE7; z-index: 5">TU REEL</div>
  <div style="position: absolute; left: 24px; right: 24px; bottom: 120px; height: 44px; z-index: 5">{caps1}</div>
  <div style="position: absolute; right: 16px; bottom: 200px; display: flex; flex-direction: column; gap: 26px; z-index: 5">
    <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#F2EDE7" stroke-width="2"><path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/></svg>
    <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#F2EDE7" stroke-width="2"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>
    <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#F2EDE7" stroke-width="2"><path d="M6 3h12v18l-6-4-6 4z"/></svg>
  </div>
  <div style="position: absolute; left: 22px; bottom: 60px; display: flex; align-items: flex-end; gap: 4px; height: 26px; z-index: 5">{''.join(f'<span style="width: 5px; height: 26px; background: #F2EDE7; transform-origin: 50% 100%; animation: aEq .8s ease-in-out {-k*0.13}s infinite"></span>' for k in range(6))}<span style="margin-left: 10px; {MONO}; font-size: 16px; color: #F2EDE7">@ceos.productions</span></div>
</div>
<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #1E1A17, #0A0908); transform: translateY(100%); animation: aNext 4s {E} infinite; display: flex; align-items: center; justify-content: center">
  <span style="{MONO}; font-size: 20px; letter-spacing: .12em; color: #9C938B">SIGUIENTE VÍDEO →</span></div>
<div style="position: absolute; left: 50%; bottom: 60px; width: 74px; height: 74px; margin-left: -37px; border-radius: 99px; background: rgba(242,237,231,.35); border: 3px solid #F2EDE7; opacity: 0; z-index: 8; animation: aFinger 4s ease-in-out infinite"></div>
'''
rows1 = ''.join(f'''<div style="position: relative; display: flex; align-items: center; justify-content: space-between; padding: 22px 24px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {r} 4s linear infinite">
  <span style="{BRIC}; font-weight: 800; font-size: 34px; letter-spacing: -0.02em">{t}</span>
  <span style="position: relative; width: 50px; height: 50px">
    <span style="position: absolute; inset: 6px; border-radius: 99px; border: 4px solid rgba(242,237,231,.2); border-top-color: #FF6A1A; animation: aSpin 1s linear infinite, aWait 4s steps(1) infinite"></span>
    <span style="position: absolute; inset: 0; border-radius: 99px; background: #FF3B30; display: flex; align-items: center; justify-content: center; color: #fff; {BRIC}; font-weight: 800; font-size: 30px; opacity: 0; animation: {x} 4s ease-out infinite">✕</span>
  </span></div>''' for t, r, x in (('¿Te sigue?', 'aR1', 'aX1'), ('¿Lo guarda?', 'aR2', 'aX2'), ('¿Te escribe?', 'aR3', 'aX3')))
body1 = headline('EL FINAL DE TU VÍDEO', 'Lo ven hasta el final…', 'y se van sin hacer nada.', 84) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 26px; align-items: stretch">
  {phone(370, 660, reel1, 'flex: none')}
  <div style="position: relative; flex: 1; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); padding: 30px 26px; box-sizing: border-box; display: flex; flex-direction: column; gap: 18px">
    <div style="display: flex; justify-content: space-between; {MONO}; font-size: 19px; letter-spacing: .1em; color: #9C938B"><span>AL ACABAR EL VÍDEO…</span><span style="color: #FF8F45">EJEMPLO</span></div>
    {rows1}
    <div style="flex: 1; position: relative; border-radius: 22px; border: 2px dashed rgba(242,237,231,.16); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; text-align: center; padding: 0 20px">
      <span style="{MONO}; font-size: 18px; letter-spacing: .1em; color: #9C938B">EL PROBLEMA NO ES EL GANCHO</span>
      <span style="{BRIC}; font-weight: 800; font-size: 40px; line-height: 1.02; letter-spacing: -0.03em">Es que tu final <span style="{SERIF}; color: #FF6A1A">no pide nada.</span></span>
    </div>
    {pill('SE FUE SIN ACTUAR', extra='left: 50%; bottom: -22px; opacity: 0; font-size: 22px; animation: aGone 4s ease-out infinite')}
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    '3 formas de cerrar para que actúen.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 EL FINAL FLOJO
kf2 = COMMON_KF + """
@keyframes aHead{0%{left:2%}100%{left:98%}}
@keyframes aDraw{0%{stroke-dashoffset:1000}80%,100%{stroke-dashoffset:0}}
@keyframes aDot{0%{offset-distance:0%}80%,100%{offset-distance:100%}}
@keyframes aZone{0%,55%{opacity:.25}62%,100%{opacity:1}}
@keyframes aC1{0%,24%{background:#FF3B30;color:#fff;border-color:#FF3B30}33%,100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
@keyframes aC2{0%,33%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}37%,58%{background:#FF3B30;color:#fff;border-color:#FF3B30}66%,100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
@keyframes aC3{0%,66%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}70%,94%{background:#FF3B30;color:#fff;border-color:#FF3B30}100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
@keyframes aT1{0%,28%{opacity:1;transform:none}33%,96%{opacity:0;transform:translateY(-10px)}100%{opacity:1}}
@keyframes aT2{0%,33%{opacity:0;transform:translateY(10px)}37%,62%{opacity:1;transform:none}66%,100%{opacity:0}}
@keyframes aT3{0%,66%{opacity:0;transform:translateY(10px)}70%,96%{opacity:1;transform:none}100%{opacity:0}}
"""
mon_txt = [('“Bueno… pues eso.<br>Nada más, ¡chao!”', 'aT1'),
           ('“Dale like, comenta, comparte,<br>sígueme y mira el link…”', 'aT2'),
           ('<span style="' + MONO + '; font-size: 30px; letter-spacing: .1em; color: #9C938B">[ LOGO + MÚSICA · SILENCIO ]</span>', 'aT3')]
mon = ''.join(f'<div style="position: absolute; left: 0; right: 0; top: 50%; transform: translateY(-50%); text-align: center; {BRIC}; font-weight: 800; font-size: 44px; line-height: 1.05; letter-spacing: -0.03em; opacity: 0; animation: {a} 4s ease-out infinite"><div style="animation: none">{t}</div></div>' for t, a in mon_txt)
chips2 = ''.join(
    f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px; padding: 16px 20px; border-radius: 20px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s ease-in-out infinite"><span style="{MONO}; font-weight: 600; font-size: 20px; opacity: .8">{n}</span><span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em; line-height: 1.02">{t}</span></div>'
    for n, t, a in (('ERROR 1', 'Despedida eterna', 'aC1'), ('ERROR 2', 'Pedir cinco cosas', 'aC2'), ('ERROR 3', 'Silencio con logo', 'aC3')))
curve = 'M0 40 C120 44 260 52 420 60 C520 66 580 72 640 82 C690 100 720 150 760 200 C790 225 820 232 868 236'
body2 = headline('EL FINAL FLOJO', 'Tu vídeo no termina:', 'se va apagando.', 86) + f"""
<div style="position: relative; height: 660px; display: flex; flex-direction: column; gap: 16px">
  <div style="position: relative; flex: 1; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.5); padding: 22px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 16px">
    <div style="position: relative; height: 210px; border-radius: 20px; overflow: hidden; background: linear-gradient(180deg, #1C130D, #0A0908); border: 2px solid rgba(242,237,231,.1)">
      {mon}
      <div style="position: absolute; left: 18px; top: 14px; display: flex; align-items: center; gap: 8px; {MONO}; font-size: 17px; letter-spacing: .1em; color: #F2EDE7"><span style="width: 12px; height: 12px; border-radius: 99px; background: #FF3B30; animation: aRec 1s steps(1) infinite"></span>ÚLTIMOS SEGUNDOS</div>
      <div style="position: absolute; inset: 10px; pointer-events: none">{corners('rgba(242,237,231,.5)')}</div>
    </div>
    <div style="position: relative; flex: 1">
      <div style="position: absolute; left: 0; right: 0; top: 0; display: flex; justify-content: space-between; {MONO}; font-size: 17px; letter-spacing: .1em; color: #9C938B"><span>GENTE QUE SIGUE VIENDO</span><span style="color: #FF8F45">EJEMPLO</span></div>
      <svg width="868" height="150" viewBox="0 0 868 240" preserveAspectRatio="none" style="position: absolute; left: 0; top: 30px">
        <defs><linearGradient id="fa" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A1A" stop-opacity=".35"/><stop offset="1" stop-color="#FF6A1A" stop-opacity="0"/></linearGradient></defs>
        <rect x="640" y="0" width="228" height="240" fill="rgba(255,59,48,.14)" style="animation: aZone 4s linear infinite"/>
        <path d="{curve} L868 240 L0 240 Z" fill="url(#fa)"/>
        <path d="{curve}" fill="none" stroke="#FF6A1A" stroke-width="6" stroke-linecap="round" stroke-dasharray="1000" style="animation: aDraw 4s linear infinite"/>
      </svg>
      <div style="position: absolute; left: 650px; top: 38px; {MONO}; font-weight: 600; font-size: 17px; letter-spacing: .08em; color: #FF3B30; animation: aZone 4s linear infinite">AQUÍ SE VAN ↓</div>
      <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 46px; display: flex; gap: 6px">
        <div style="flex: 2; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 17px; display: flex; align-items: center; padding-left: 12px">GANCHO</div>
        <div style="flex: 9; border-radius: 10px; background: #1E1A17; border: 2px solid rgba(242,237,231,.2); {MONO}; font-size: 17px; color: #B5ADA4; display: flex; align-items: center; padding-left: 12px">CONTENIDO</div>
        <div style="flex: 4; border-radius: 10px; background: repeating-linear-gradient(45deg, rgba(255,59,48,.55) 0 12px, rgba(255,59,48,.25) 12px 24px); {MONO}; font-weight: 600; font-size: 17px; color: #fff; display: flex; align-items: center; padding-left: 12px">FINAL FLOJO</div>
      </div>
      <div style="position: absolute; top: 24px; bottom: -6px; width: 4px; margin-left: -2px; background: #F2EDE7; box-shadow: 0 0 14px rgba(242,237,231,.8); animation: aHead 4s linear infinite; z-index: 3"><div style="position: absolute; left: -9px; top: -6px; width: 22px; height: 14px; border-radius: 4px; background: #F2EDE7"></div></div>
    </div>
  </div>
  <div style="display: flex; gap: 14px">{chips2}</div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · El final flojo', 2, kf2, body2,
    'Los últimos segundos deciden qué hacen.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 UNA SOLA PETICIÓN
kf3 = COMMON_KF + """
@keyframes aShake{0%,100%{transform:translateX(0)}20%{transform:translateX(-4px)}40%{transform:translateX(4px)}60%{transform:translateX(-3px)}80%{transform:translateX(3px)}}
@keyframes aOut{0%,30%{opacity:1;max-height:70px;margin-bottom:0}42%,92%{opacity:0;max-height:0;margin-bottom:-12px}100%{opacity:1;max-height:70px;margin-bottom:0}}
@keyframes aStrike{0%,22%{width:0}30%,92%{width:100%}100%{width:0}}
@keyframes aWin{0%,34%{transform:scale(1);background:#1E1A17;color:#F2EDE7;box-shadow:none}46%,92%{transform:scale(1.1);background:#FF6A1A;color:#0A0908;box-shadow:0 0 60px rgba(255,106,26,.7)}100%{transform:scale(1);background:#1E1A17;color:#F2EDE7;box-shadow:none}}
@keyframes aTy1{0%,4%{width:0}24%,95%{width:100%}100%{width:0}}
@keyframes aTy2{0%,24%{width:0}40%,95%{width:100%}100%{width:0}}
@keyframes aTy3{0%,40%{width:0}54%,95%{width:100%}100%{width:0}}
@keyframes aCaret{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes aTagIn{0%,40%{opacity:0;transform:translateY(12px)}48%,92%{opacity:1;transform:none}100%{opacity:0}}
@keyframes aMsg1{0%,36%{opacity:1;transform:none}42%,96%{opacity:0;transform:translateY(-12px)}100%{opacity:1}}
@keyframes aMsg2{0%,42%{opacity:0;transform:translateY(12px)}48%,94%{opacity:1;transform:none}98%,100%{opacity:0}}
"""
ctas = [('Dale like', True), ('Comenta', True), ('Sígueme', False), ('Comparte', True), ('Link en la bio', True)]
cta_list = ''.join(
    (f'<div style="position: relative; align-self: center; overflow: hidden; padding: 14px 26px; border-radius: 16px; background: #1E1A17; border: 2px solid rgba(242,237,231,.2); {BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em; animation: aOut 4s {E} infinite"><span style="animation: aShake .4s linear infinite; display: inline-block">{t}</span><div style="position: absolute; left: 8%; top: 50%; height: 4px; background: #FF3B30; animation: aStrike 4s {E} infinite"></div></div>'
     if lose else
     f'<div style="align-self: center; padding: 14px 30px; border-radius: 16px; border: 2px solid #FF6A1A; {BRIC}; font-weight: 800; font-size: 30px; line-height: 1.05; text-align: center; letter-spacing: -0.02em; animation: aWin 4s {E} infinite; position: relative; z-index: 2">Sígueme para la parte 2</div>')
    for t, lose in ctas)
screen3 = f'''{studio(False)}
<div style="position: absolute; inset: 0; background: rgba(10,9,8,.55)"></div>
<div style="position: absolute; left: 0; right: 0; top: 70px; text-align: center; {MONO}; font-size: 17px; letter-spacing: .12em; color: #9C938B">FINAL DEL VÍDEO</div>
<div style="position: absolute; left: 20px; right: 20px; top: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center; gap: 12px">{cta_list}</div>
'''
body3 = headline('TRUCO 01 · UNA SOLA PETICIÓN', 'Pide una cosa,', 'no cinco.', 96) + f"""
<div style="position: relative; height: 640px; display: flex; gap: 24px">
  {phone(360, 640, screen3, 'flex: none')}
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 18px">
    <div style="position: relative; flex: 1; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); padding: 28px; box-sizing: border-box; box-shadow: 0 50px 120px -40px rgba(255,106,26,0.45)">
      <div style="display: flex; justify-content: space-between; {MONO}; font-size: 18px; letter-spacing: .1em; color: #9C938B"><span>GUION · ÚLTIMA FRASE</span><span style="color: #FF8F45">■ 00:28</span></div>
      <div style="margin-top: 30px; {BRIC}; font-weight: 800; font-size: 50px; line-height: 1.08; letter-spacing: -0.03em; position: relative">
        <div style="position: relative; overflow: hidden; white-space: nowrap; width: 0; animation: aTy1 4s steps(14) infinite">“Si te ha servido,</div>
        <div style="position: relative; overflow: hidden; white-space: nowrap; width: 0; animation: aTy2 4s steps(12) infinite"><span style="color: #FF6A1A">sígueme</span> para</div>
        <div style="position: relative; overflow: hidden; white-space: nowrap; width: 0; animation: aTy3 4s steps(10) infinite">la parte 2.”<span style="display: inline-block; width: 5px; height: 42px; margin-left: 6px; background: #FF6A1A; vertical-align: -4px; animation: aCaret .8s steps(1) infinite"></span></div>
      </div>
      <div style="position: absolute; left: 28px; right: 28px; bottom: 26px; display: flex; flex-direction: column; gap: 10px">
        <div style="display: flex; align-items: center; gap: 12px; opacity: 0; animation: aTagIn 4s ease-out infinite"><span style="width: 36px; height: 36px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; font-weight: 800">✓</span><span style="font-size: 25px; color: #F2EDE7">Una acción concreta</span></div>
        <div style="display: flex; align-items: center; gap: 12px; opacity: 0; animation: aTagIn 4s ease-out .25s infinite"><span style="width: 36px; height: 36px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; font-weight: 800">✓</span><span style="font-size: 25px; color: #F2EDE7">Con un motivo para hacerla</span></div>
      </div>
    </div>
    <div style="position: relative; height: 120px; border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); display: flex; align-items: center; padding: 0 26px; box-sizing: border-box">
      <div style="position: absolute; left: 26px; right: 26px; {BRIC}; font-weight: 800; font-size: 32px; letter-spacing: -0.02em; line-height: 1.05; animation: aMsg1 4s linear infinite">Cinco opciones <span style="{SERIF}; color: #FF3B30">= ninguna.</span></div>
      <div style="position: absolute; left: 26px; right: 26px; {BRIC}; font-weight: 800; font-size: 32px; letter-spacing: -0.02em; line-height: 1.05; opacity: 0; animation: aMsg2 4s linear infinite">Una orden clara <span style="{SERIF}; color: #FF6A1A">= la hacen.</span></div>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Una sola petición', 3, kf3, body3,
    'Elige: seguir, guardar o escribir. Solo una.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 CIERRE EN 3 PASOS
kf4 = COMMON_KF + """
@keyframes aScis{0%,8%{left:96%;opacity:0}14%{opacity:1}30%{left:66%;opacity:1}36%{left:66%;opacity:1}40%,100%{left:66%;opacity:0}}
@keyframes aTail{0%,34%{transform:none;opacity:1}46%,92%{transform:translateY(90px) rotate(6deg);opacity:0}100%{transform:none;opacity:1}}
@keyframes aCutLine{0%,30%{opacity:0}33%{opacity:1}40%,100%{opacity:0}}
@keyframes aLoop{0%,46%{stroke-dashoffset:1000}78%,92%{stroke-dashoffset:0}100%{stroke-dashoffset:1000}}
@keyframes aLoopDot{0%,46%{offset-distance:0%;opacity:0}48%{opacity:1}78%{offset-distance:100%;opacity:1}84%,100%{offset-distance:100%;opacity:0}}
@keyframes aHookHit{0%,76%{box-shadow:none;transform:scale(1)}80%{box-shadow:0 0 60px rgba(255,106,26,.9);transform:scale(1.08)}88%,100%{box-shadow:none;transform:scale(1)}}
@keyframes aLoopTag{0%,76%{opacity:0;transform:translateX(-50%) translateY(8px)}80%,94%{opacity:1;transform:translateX(-50%)}100%{opacity:0}}
@keyframes aChk1{0%,10%{background:#12100F;border-color:rgba(242,237,231,.14)}18%,94%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aChk2{0%,30%{background:#12100F;border-color:rgba(242,237,231,.14)}38%,94%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aChk3{0%,60%{background:#12100F;border-color:rgba(242,237,231,.14)}68%,94%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aTk1{0%,12%{transform:scale(0)}18%{transform:scale(1.25)}22%,94%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aTk2{0%,32%{transform:scale(0)}38%{transform:scale(1.25)}42%,94%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aTk3{0%,62%{transform:scale(0)}68%{transform:scale(1.25)}72%,94%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aPH{0%{left:0%}100%{left:100%}}
@keyframes aEqW{0%,100%{transform:scaleY(.55)}50%{transform:scaleY(1)}}
@keyframes aTailW{0%,34%{opacity:1}46%,92%{opacity:.08}100%{opacity:1}}
"""
WAVE = '<span style="flex: 1; height: 20%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out 0.00s infinite"></span><span style="flex: 1; height: 64%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.07s infinite"></span><span style="flex: 1; height: 67%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.14s infinite"></span><span style="flex: 1; height: 35%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.21s infinite"></span><span style="flex: 1; height: 28%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.28s infinite"></span><span style="flex: 1; height: 21%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.35s infinite"></span><span style="flex: 1; height: 33%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.42s infinite"></span><span style="flex: 1; height: 20%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.49s infinite"></span><span style="flex: 1; height: 57%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.56s infinite"></span><span style="flex: 1; height: 74%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.63s infinite"></span><span style="flex: 1; height: 44%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.70s infinite"></span><span style="flex: 1; height: 46%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.77s infinite"></span><span style="flex: 1; height: 69%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.84s infinite"></span><span style="flex: 1; height: 48%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.91s infinite"></span><span style="flex: 1; height: 20%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -0.98s infinite"></span><span style="flex: 1; height: 23%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.05s infinite"></span><span style="flex: 1; height: 34%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.12s infinite"></span><span style="flex: 1; height: 32%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.19s infinite"></span><span style="flex: 1; height: 41%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.26s infinite"></span><span style="flex: 1; height: 74%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.33s infinite"></span><span style="flex: 1; height: 64%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.40s infinite"></span><span style="flex: 1; height: 22%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.47s infinite"></span><span style="flex: 1; height: 61%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.54s infinite"></span><span style="flex: 1; height: 58%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.61s infinite"></span><span style="flex: 1; height: 29%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.68s infinite"></span><span style="flex: 1; height: 23%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.75s infinite"></span><span style="flex: 1; height: 32%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.82s infinite"></span><span style="flex: 1; height: 41%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.89s infinite"></span><span style="flex: 1; height: 22%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -1.96s infinite"></span><span style="flex: 1; height: 64%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.03s infinite"></span><span style="flex: 1; height: 76%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.10s infinite"></span><span style="flex: 1; height: 41%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.17s infinite"></span><span style="flex: 1; height: 46%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.24s infinite"></span><span style="flex: 1; height: 61%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.31s infinite"></span><span style="flex: 1; height: 39%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.38s infinite"></span><span style="flex: 1; height: 20%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.45s infinite"></span><span style="flex: 1; height: 28%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.52s infinite"></span><span style="flex: 1; height: 46%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.59s infinite"></span><span style="flex: 1; height: 34%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.66s infinite"></span><span style="flex: 1; height: 47%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.73s infinite"></span><span style="flex: 1; height: 78%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.80s infinite"></span><span style="flex: 1; height: 62%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.87s infinite"></span><span style="flex: 1; height: 25%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -2.94s infinite"></span><span style="flex: 1; height: 56%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.01s infinite"></span><span style="flex: 1; height: 47%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.08s infinite"></span><span style="flex: 1; height: 23%; border-radius: 3px; background: #6B635C; transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.15s infinite"></span><span style="flex: 1; height: 23%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.22s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 45%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.29s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 48%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.36s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 26%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.43s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 69%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.50s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 76%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.57s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 37%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.64s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 44%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.71s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 50%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.78s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 29%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.85s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 20%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.92s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 39%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -3.99s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 56%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.06s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 35%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.13s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 52%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.20s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 79%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.27s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 58%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.34s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 27%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.41s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 48%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.48s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 34%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.55s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 20%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.62s infinite, aTailW 4s linear infinite"></span><span style="flex: 1; height: 31%; border-radius: 3px; background: rgba(255,59,48,.7); transform-origin: 50% 50%; animation: aEqW 1.2s ease-in-out -4.69s infinite, aTailW 4s linear infinite"></span>'
loop_path = 'M800 150 C860 150 868 20 700 20 L170 20 C40 20 40 150 90 150'
checks = [('Una sola petición', 'Seguir, guardar o escribir', 'aChk1', 'aTk1'),
          ('Dila sobre la última idea', 'No después, cuando ya se van', 'aChk2', 'aTk2'),
          ('Corta en seco', 'Y que enlace con el gancho', 'aChk3', 'aTk3')]
rows4 = ''.join(
    f'<div style="flex: 1; display: flex; flex-direction: column; gap: 8px; padding: 16px 18px; border-radius: 20px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s ease-in-out infinite"><div style="display: flex; align-items: center; gap: 12px"><span style="flex: none; width: 40px; height: 40px; border-radius: 99px; border: 2px solid #FF6A1A; display: flex; align-items: center; justify-content: center"><svg width="24" height="24" viewBox="0 0 24 24" style="animation: {tk} 4s ease-out infinite"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#FF6A1A" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="{MONO}; font-weight: 600; font-size: 20px; color: #FF8F45">0{i+1}</span></div><span style="{BRIC}; font-weight: 800; font-size: 29px; letter-spacing: -0.02em; line-height: 1">{t}</span><span style="font-size: 21px; color: #B5ADA4; line-height: 1.2">{d}</span></div>'
    for i, (t, d, a, tk) in enumerate(checks))
body4 = headline('EL CIERRE EN 3 PASOS', 'Pide, remata', 'y corta en seco.', 92) + f"""
<div style="position: relative; height: 660px; display: flex; flex-direction: column; gap: 16px">
  <div style="position: relative; flex: 1; border-radius: 30px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55); padding: 26px; box-sizing: border-box">
    <div style="display: flex; justify-content: space-between; {MONO}; font-size: 18px; letter-spacing: .1em; color: #9C938B"><span>EDICIÓN · LÍNEA DE TIEMPO</span><span style="color: #FF8F45">✂ CORTE FINAL</span></div>
    <svg width="868" height="170" viewBox="0 0 868 170" style="position: absolute; left: 26px; top: 64px; z-index: 2; overflow: visible">
      <path d="{loop_path}" fill="none" stroke="rgba(242,237,231,.12)" stroke-width="4" stroke-dasharray="8 10"/>
      <path d="{loop_path}" fill="none" pathLength="1000" stroke="#FF6A1A" stroke-width="6" stroke-linecap="round" stroke-dasharray="1000" stroke-dashoffset="1000" style="animation: aLoop 4s {E} infinite"/>
    </svg>
    <div style="position: absolute; left: 26px; top: 64px; width: 20px; height: 20px; margin: -10px 0 0 -10px; border-radius: 99px; background: #FF6A1A; box-shadow: 0 0 20px #FF6A1A; offset-path: path('{loop_path}'); animation: aLoopDot 4s {E} infinite"></div>
    <div style="position: absolute; left: 50%; top: 98px; padding: 8px 16px; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .08em; opacity: 0; animation: aLoopTag 4s ease-out infinite">↺ VUELVE AL GANCHO</div>
    <div style="position: absolute; left: 26px; right: 26px; top: 214px; height: 110px">
      <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 20%; border-radius: 14px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 19px; display: flex; align-items: center; justify-content: center; animation: aHookHit 4s ease-out infinite">GANCHO</div>
      <div style="position: absolute; left: 21%; top: 0; bottom: 0; width: 32%; border-radius: 14px; background: #1E1A17; border: 2px solid rgba(242,237,231,.2); {MONO}; font-size: 19px; color: #B5ADA4; display: flex; align-items: center; justify-content: center">IDEA</div>
      <div style="position: absolute; left: 54%; top: 0; bottom: 0; width: 12%; border-radius: 14px; background: #1E1A17; border: 2px solid #FF6A1A; {MONO}; font-weight: 600; font-size: 19px; color: #FF8F45; display: flex; align-items: center; justify-content: center">CTA</div>
      <div style="position: absolute; left: 67%; right: 0; top: 0; bottom: 0; border-radius: 14px; background: repeating-linear-gradient(45deg, rgba(255,59,48,.5) 0 12px, rgba(255,59,48,.2) 12px 24px); {MONO}; font-weight: 600; font-size: 17px; color: #fff; display: flex; align-items: center; justify-content: center; text-align: center; line-height: 1.2; animation: aTail 4s {E} infinite">“BUENO… PUES ESO”<br>+ LOGO</div>
      <div style="position: absolute; left: 66.5%; top: -18px; bottom: -18px; width: 4px; background: #FF3B30; box-shadow: 0 0 18px #FF3B30; opacity: 0; animation: aCutLine 4s linear infinite"></div>
      <div style="position: absolute; top: -64px; width: 56px; height: 56px; margin-left: -28px; border-radius: 99px; background: #F2EDE7; color: #0A0908; display: flex; align-items: center; justify-content: center; font-size: 32px; opacity: 0; animation: aScis 4s {E} infinite; z-index: 4">✂</div>
    </div>
    <div style="position: absolute; left: 26px; right: 26px; top: 356px; height: 64px; display: flex; align-items: center; gap: 4px">
      <div style="position: absolute; left: 0; top: -14px; {MONO}; font-size: 14px; letter-spacing: .1em; color: #9C938B">AUDIO</div>
      <div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; display: flex; align-items: center; gap: 4px">{WAVE}</div>
    </div>
    <div style="position: absolute; left: 26px; right: 26px; top: 196px; height: 234px; z-index: 3; pointer-events: none"><div style="position: absolute; top: 0; bottom: 0; width: 4px; margin-left: -2px; background: #F2EDE7; box-shadow: 0 0 14px rgba(242,237,231,.8); animation: aPH 4s linear infinite"><div style="position: absolute; left: -9px; top: -6px; width: 22px; height: 14px; border-radius: 4px; background: #F2EDE7"></div></div></div>
  </div>
  <div style="display: flex; gap: 12px">{rows4}</div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · El cierre en 3 pasos', 4, kf4, body4,
    'Si el final enlaza con el inicio, se repite.', DESLIZA_TXT))

# ---------------------------------------------------------------- 05 CTA
kf5 = COMMON_KF + """
@keyframes aWipe{0%,8%{width:92%}46%,54%{width:8%}92%,100%{width:92%}}
@keyframes aKnob{0%,8%{left:92%}46%,54%{left:8%}92%,100%{left:92%}}
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
"""


def endscene(txt, tag, tagbg, tagfg, dim):
    op = '.55' if dim else '1'
    return f'''{studio(not dim)}{'' if dim else softbox('l')}
<div style="position: absolute; left: 50%; bottom: -30px; margin-left: -160px; width: 320px; opacity: {op}">{person(320)}</div>
<div style="position: absolute; left: 60px; right: 60px; bottom: 44px; text-align: center; {BRIC}; font-weight: 800; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em; color: #F2EDE7; text-shadow: 0 3px 14px #000; opacity: {op}">{txt}</div>
<div style="position: absolute; {'left' if dim else 'right'}: 20px; top: 18px; padding: 8px 16px; border-radius: 10px; background: {tagbg}; color: {tagfg}; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; z-index: 6">{tag}</div>'''


scene_before = endscene('“Bueno… pues eso. ¡Chao!”', 'FINAL FLOJO', '#FF3B30', '#fff', True)
scene_after = endscene('“Guárdalo para tu próxima grabación.”', 'FINAL QUE ACTÚA', '#FF6A1A', '#0A0908', False)
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 82px; line-height: 1; letter-spacing: -0.045em">El final también<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">se escribe en el guion.</span></p>
<div style="position: relative; margin-top: 40px; width: 920px; height: 480px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">
  <div style="position: absolute; inset: 0">{scene_after}</div>
  <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 92%; overflow: hidden; animation: aWipe 4s cubic-bezier(.65,0,.35,1) infinite"><div style="position: absolute; left: 0; top: 0; width: 920px; height: 480px">{scene_before}</div></div>
  <div style="position: absolute; top: 0; bottom: 0; left: 92%; width: 0; z-index: 7; animation: aKnob 4s cubic-bezier(.65,0,.35,1) infinite">
    <div style="position: absolute; top: 0; bottom: 0; left: -3px; width: 6px; background: #F2EDE7; box-shadow: 0 0 24px rgba(255,106,26,.9)"></div>
    <div style="position: absolute; top: 50%; left: -36px; width: 72px; height: 72px; margin-top: -36px; border-radius: 99px; background: #F2EDE7; display: flex; align-items: center; justify-content: center; color: #0A0908; {BRIC}; font-weight: 800; font-size: 30px">⇆</div></div>
</div>
<div style="position: relative; overflow: hidden; margin-top: 44px; padding: 26px 54px; border-radius: 30px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 64px; line-height: 1; letter-spacing: -0.04em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.3), rgba(255,255,255,0)); animation: aShim 4s ease-in-out 0.6s infinite"></div></div>
</div>
"""
open(os.path.join(OUT, 'S5.dc.html'), 'w').write(page('05 · CTA', 5, kf5, body5,
    'Guárdalo para tu próximo vídeo.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
