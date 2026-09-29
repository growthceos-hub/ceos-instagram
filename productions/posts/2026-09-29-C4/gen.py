#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C4 2026-09-29 (posar en fotos) en src/."""
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


# ---------------------------------------------------------------- 01 GANCHO
kf1 = COMMON_KF + """
@keyframes aFlash{0%,47%{opacity:0}50%{opacity:.75}63%,100%{opacity:0}}
@keyframes aAF{0%,47%,100%{transform:scale(1);border-color:#F2EDE7}56%{transform:scale(1.12);border-color:#FF6A1A}70%{transform:scale(1);border-color:#F2EDE7}}
@keyframes aShot{0%,100%{border-color:rgba(242,237,231,.14);box-shadow:none}3%{border-color:#FFFFFF;box-shadow:0 0 30px rgba(255,255,255,.6)}20%{border-color:#FF3B30;box-shadow:0 0 24px rgba(255,59,48,.45)}24%,99%{border-color:rgba(242,237,231,.14);box-shadow:none}}
@keyframes aStamp{0%,100%{transform:rotate(-12deg) scale(1)}4%{transform:rotate(-12deg) scale(1.35)}12%{transform:rotate(-12deg) scale(.95)}18%{transform:rotate(-12deg) scale(1)}}
@keyframes aBlink{0%,55%{opacity:1}56%,100%{opacity:.35}}
"""


def thumb(i):
    anim = f'animation: aShot 4s linear {i-3.5}s infinite; '
    delay = i - 3.5
    return f'''<div style="position: relative; flex: 1; border-radius: 16px; overflow: hidden; background: #1C130D; border: 2px solid rgba(242,237,231,.14); {anim}">
  <div style="position: absolute; left: 50%; bottom: -8px; margin-left: -28px; width: 56px">{figure(56, f't{i}')}</div>
  <div style="position: absolute; left: 50%; top: 50%; margin: -19px 0 0 -62px; width: 124px; text-align: center; padding: 6px 0; border: 3px solid #FF3B30; border-radius: 8px; color: #FF3B30; background: rgba(10,9,8,.88); {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .1em; transform: rotate(-12deg); animation: aStamp 4s ease-out {delay}s infinite"><span>RÍGIDO</span></div>
  <div style="position: absolute; left: 8px; top: 6px; {MONO}; font-size: 15px; color: #9C938B">IMG_0{i+1}</div>
</div>'''


counter = ''.join(
    f'<span style="position: absolute; right: 0; opacity: 0; animation: aStep 4s steps(1) {k-4}s infinite">FOTO {k+1}/4</span>' for k in range(4))
body1 = headline('FOTOS DE MARCA PERSONAL', '¿Sales tieso en todas tus fotos?', 'No es tu cara: es tu pose.', 80) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 18px">
  <div style="position: relative; flex: 1; border-radius: 34px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
    {studio()}{softbox('l')}{softbox('r')}
    <div style="position: absolute; left: 50%; bottom: 14px; margin-left: -125px; width: 250px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%; z-index: 3">{figure(250, 'm1')}</div>
    <div style="position: absolute; left: 50%; top: 92px; width: 150px; height: 150px; margin-left: -75px; border: 3px solid #F2EDE7; border-radius: 10px; z-index: 5; animation: aAF 1s ease-out infinite"></div>
    <div style="position: absolute; inset: 20px; pointer-events: none; z-index: 5">{corners()}</div>
    <div style="position: absolute; left: 60px; top: 34px; display: flex; align-items: center; gap: 10px; {MONO}; font-size: 20px; letter-spacing: .1em; color: #F2EDE7; z-index: 6"><span style="width: 14px; height: 14px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30"></span>AF · RÁFAGA</div>
    <div style="position: absolute; right: 60px; top: 34px; width: 130px; height: 26px; {MONO}; font-size: 20px; letter-spacing: .08em; color: #F2EDE7; z-index: 6">{counter}</div>
    {pill('POSE "DE DNI" DETECTADA', extra='left: 50%; bottom: 40px; transform: translateX(-50%); animation: aBlink 1s steps(1) infinite')}
    <div style="position: absolute; inset: 0; background: #FFFFFF; opacity: 0; z-index: 7; animation: aFlash 1s linear infinite"></div>
  </div>
  <div style="flex: none; width: 190px; display: flex; flex-direction: column; gap: 12px">{''.join(thumb(i) for i in range(4))}</div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    '3 trucos de fotógrafo para salir natural.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 LA POSE DEL DNI
kf2 = COMMON_KF + """
@keyframes aHunt{0%,18%{left:434px;top:320px;width:300px;height:540px}26%,42%{left:434px;top:118px;width:130px;height:140px}50%,66%{left:434px;top:190px;width:200px;height:70px}74%,90%{left:382px;top:290px;width:80px;height:210px}100%{left:434px;top:320px;width:300px;height:540px}}
@keyframes aHuntC{0%,20%{border-color:#F2EDE7}24%,92%{border-color:#FF3B30}100%{border-color:#F2EDE7}}
@keyframes aL0{0%,18%{opacity:1}22%,96%{opacity:0}100%{opacity:1}}
@keyframes aL1{0%,24%{opacity:0;transform:translateX(-14px)}28%,42%{opacity:1;transform:none}46%,100%{opacity:0}}
@keyframes aL2{0%,48%{opacity:0;transform:translateX(-14px)}52%,66%{opacity:1;transform:none}70%,100%{opacity:0}}
@keyframes aL3{0%,72%{opacity:0;transform:translateX(14px)}76%,90%{opacity:1;transform:none}94%,100%{opacity:0}}
@keyframes aScanL{0%{top:0%}100%{top:100%}}
@keyframes aC1{0%,22%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}26%,42%{background:#FF3B30;color:#fff;border-color:#FF3B30}46%,100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
@keyframes aC2{0%,46%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}50%,66%{background:#FF3B30;color:#fff;border-color:#FF3B30}70%,100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
@keyframes aC3{0%,70%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}74%,90%{background:#FF3B30;color:#fff;border-color:#FF3B30}94%,100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
"""
chips2 = ''.join(
    f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px; padding: 16px 20px; border-radius: 20px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s ease-in-out infinite"><span style="{MONO}; font-weight: 600; font-size: 20px; opacity: .8">{n}</span><span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em; line-height: 1.02">{t}</span></div>'
    for n, t, a in (('ERROR 1', 'Barbilla hacia atrás', 'aC1'), ('ERROR 2', 'Hombros de frente', 'aC2'), ('ERROR 3', 'Brazos pegados', 'aC3')))
body2 = headline('LA POSE DEL DNI', 'De frente, recto y quieto:', 'la foto sale plana.', 86) + f"""
<div style="position: relative; height: 660px; display: flex; flex-direction: column; gap: 16px">
  <div style="position: relative; flex: 1; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.5); padding: 0">
   <div style="position: absolute; left: 26px; top: 26px; width: 868px; height: 454px; border-radius: 22px; overflow: hidden; background: #0A0908">
    <div style="position: absolute; left: 0; top: -60px; width: 868px; height: 640px">
      {studio(False)}
      <div style="position: absolute; left: 299px; top: 48px; width: 270px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{figure(270, 'm2')}</div>
      <div style="position: absolute; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, rgba(255,106,26,0), #FF6A1A, rgba(255,106,26,0)); box-shadow: 0 0 20px #FF6A1A; animation: aScanL 2s linear infinite; z-index: 4"></div>
      <div style="position: absolute; transform: translate(-50%,-50%); border: 3px solid #F2EDE7; border-radius: 10px; z-index: 5; left: 434px; top: 320px; width: 300px; height: 540px; animation: aHunt 4s cubic-bezier(.6,0,.3,1) infinite, aHuntC 4s steps(1) infinite"></div>
      {pill('ANALIZANDO POSE…', 'rgba(10,9,8,.85)', '#FF8F45', 'left: 606px; top: 150px; border: 2px solid #FF6A1A; animation: aL0 4s linear infinite')}
      {pill('BARBILLA HACIA ATRÁS', extra='left: 516px; top: 96px; opacity: 0; animation: aL1 4s ease-out infinite')}
      {pill('HOMBROS DE FRENTE', extra='left: 552px; top: 170px; opacity: 0; animation: aL2 4s ease-out infinite')}
      {pill('BRAZOS PEGADOS', extra='left: 90px; top: 268px; opacity: 0; animation: aL3 4s ease-out infinite')}
    </div>
    <div style="position: absolute; inset: 14px; pointer-events: none; z-index: 5">{corners()}</div>
   </div>
  </div>
  <div style="display: flex; gap: 14px">{chips2}</div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · La pose del DNI', 2, kf2, body2,
    'Es la pose por defecto… y la más rígida.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 GIRA 45°
kf3 = COMMON_KF + """
@keyframes aRot{0%,12%{transform:rotate(0deg)}44%,86%{transform:rotate(-40deg)}100%{transform:rotate(0deg)}}
@keyframes aArc{0%,12%{stroke-dashoffset:120}44%,86%{stroke-dashoffset:0}100%{stroke-dashoffset:120}}
@keyframes aDeg{0%,30%{opacity:0}44%,86%{opacity:1}96%,100%{opacity:0}}
@keyframes aFig3{0%,12%{transform:scaleX(1) rotate(0)}44%,86%{transform:scaleX(.8) rotate(-1.5deg)}100%{transform:scaleX(1) rotate(0)}}
@keyframes aSh3{0%,12%{opacity:0}44%,86%{opacity:.45}100%{opacity:0}}
@keyframes aLeg3{0%,12%{transform:rotate(0)}44%,86%{transform:rotate(-6deg)}100%{transform:rotate(0)}}
@keyframes aW{0%,12%{width:236px}44%,86%{width:180px}100%{width:236px}}
@keyframes aP1{0%,26%{opacity:1}34%,94%{opacity:0}100%{opacity:1}}
@keyframes aP2{0%,34%{opacity:0}44%,86%{opacity:1}94%,100%{opacity:0}}
@keyframes aBeam{0%,100%{opacity:.35}50%{opacity:.7}}
"""
body3 = headline('TRUCO 01 · GIRA EL CUERPO', 'Cuerpo a 45°,', 'la cara a cámara.', 90) + f"""
<div style="position: relative; height: 640px; display: flex; gap: 22px">
  <div style="position: relative; flex: none; width: 340px; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); overflow: hidden">
    <div style="position: absolute; left: 22px; top: 18px; {MONO}; font-size: 19px; letter-spacing: .1em; color: #9C938B">VISTA DESDE ARRIBA</div>
    <div style="position: absolute; left: 50%; top: 250px; width: 0; height: 0">
      <svg width="240" height="240" viewBox="-120 -120 240 240" style="position: absolute; left: -120px; top: -120px; overflow: visible">
        <line x1="0" y1="0" x2="0" y2="110" stroke="#6B635C" stroke-width="3" stroke-dasharray="6 6"/>
        <path d="M0 95 A95 95 0 0 1 61 73" fill="none" stroke="#FF6A1A" stroke-width="5" stroke-linecap="round" stroke-dasharray="120" style="animation: aArc 4s cubic-bezier(.6,0,.3,1) infinite"/>
        <g style="transform-box: view-box; transform-origin: 0 0; animation: aRot 4s cubic-bezier(.6,0,.3,1) infinite">
          <ellipse cx="0" cy="0" rx="92" ry="34" fill="#F2EDE7" opacity=".92"/>
          <line x1="-100" y1="0" x2="100" y2="0" stroke="#FF6A1A" stroke-width="3" opacity=".7"/>
        </g>
        <circle cx="0" cy="0" r="30" fill="#D9D1C8" stroke="#0A0908" stroke-width="3"/>
        <path d="M-9 26 L0 42 L9 26 Z" fill="#FF6A1A"/>
      </svg>
      <div style="position: absolute; left: 70px; top: 90px; {BRIC}; font-weight: 800; font-size: 44px; color: #FF6A1A; opacity: 0; animation: aDeg 4s linear infinite">45°</div>
    </div>
    <div style="position: absolute; left: 50%; bottom: 150px; width: 0; height: 0; border-left: 70px solid transparent; border-right: 70px solid transparent; border-bottom: 150px solid rgba(255,106,26,.16); margin-left: -70px; transform: rotate(180deg); transform-origin: 50% 100%; animation: aBeam 2s ease-in-out infinite"></div>
    <div style="position: absolute; left: 50%; bottom: 40px; width: 120px; height: 70px; margin-left: -60px; border-radius: 14px; background: #1E1A17; border: 3px solid #FF6A1A; display: flex; align-items: center; justify-content: center"><div style="width: 34px; height: 34px; border-radius: 99px; border: 5px solid #FF6A1A"></div></div>
    <div style="position: absolute; left: 0; right: 0; bottom: 12px; text-align: center; {MONO}; font-size: 17px; letter-spacing: .1em; color: #9C938B">CÁMARA</div>
  </div>
  <div style="position: relative; flex: 1; border-radius: 30px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.5)">
    {studio()}
    <div style="position: absolute; left: 50%; top: 118px; height: 40px; margin-left: 0; transform: translateX(-50%); z-index: 4; display: flex; align-items: center; animation: aW 4s cubic-bezier(.6,0,.3,1) infinite">
      <div style="position: absolute; left: 0; right: 0; top: 50%; height: 3px; background: #FF6A1A"></div>
      <div style="position: absolute; left: 0; top: 6px; width: 3px; height: 28px; background: #FF6A1A"></div><div style="position: absolute; right: 0; top: 6px; width: 3px; height: 28px; background: #FF6A1A"></div>
    </div>
    <div style="position: absolute; left: 50%; bottom: 14px; margin-left: -130px; width: 260px; z-index: 3">{figure(260, 'm3', {'fig': 'aFig3 4s cubic-bezier(.6,0,.3,1) infinite', 'shade': 'aSh3 4s cubic-bezier(.6,0,.3,1) infinite', 'legR': 'aLeg3 4s cubic-bezier(.6,0,.3,1) infinite'})}</div>
    <div style="position: absolute; inset: 16px; pointer-events: none; z-index: 5">{corners()}</div>
    {pill('DE FRENTE: ANCHO Y PLANO', extra='left: 50%; top: 40px; transform: translateX(-50%); animation: aP1 4s linear infinite')}
    {pill('A 45°: MÁS FORMA ✓', '#FF6A1A', '#0A0908', 'left: 50%; top: 40px; transform: translateX(-50%); opacity: 0; animation: aP2 4s linear infinite')}
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Gira 45°', 3, kf3, body3,
    'Menos ancho, más forma. La mirada, a cámara.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 LA POSE EN 3 PASOS
kf4 = COMMON_KF + """
@keyframes aF4{0%,8%{transform:scaleX(1) rotate(0)}20%,90%{transform:scaleX(.82) rotate(-1.5deg)}100%{transform:scaleX(1) rotate(0)}}
@keyframes aS4{0%,8%{opacity:0}20%,90%{opacity:.45}100%{opacity:0}}
@keyframes aLg4{0%,8%{transform:rotate(0)}20%,90%{transform:rotate(-6deg)}100%{transform:rotate(0)}}
@keyframes aA4{0%,30%{transform:rotate(0)}42%,90%{transform:rotate(28deg)}100%{transform:rotate(0)}}
@keyframes aFA4{0%,30%{transform:rotate(0)}42%,90%{transform:rotate(-108deg)}100%{transform:rotate(0)}}
@keyframes aG4{0%,42%{opacity:0}48%,90%{opacity:1}96%,100%{opacity:0}}
@keyframes aH4{0%,52%{transform:translate(0,0) rotate(0)}62%,90%{transform:translate(4px,6px) rotate(-4deg)}100%{transform:translate(0,0) rotate(0)}}
@keyframes aJ4{0%,60%{opacity:0}66%,90%{opacity:1}96%,100%{opacity:0}}
@keyframes aOk{0%,70%{opacity:0;transform:translateX(-50%) scale(.7)}76%,92%{opacity:1;transform:translateX(-50%) scale(1)}97%,100%{opacity:0;transform:translateX(-50%) scale(.7)}}
@keyframes aFl4{0%,74%{opacity:0}76%{opacity:.7}84%,100%{opacity:0}}
@keyframes aChk1{0%,10%{background:#12100F;border-color:rgba(242,237,231,.14)}18%,92%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aChk2{0%,34%{background:#12100F;border-color:rgba(242,237,231,.14)}42%,92%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aChk3{0%,54%{background:#12100F;border-color:rgba(242,237,231,.14)}62%,92%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aTk1{0%,12%{transform:scale(0)}18%{transform:scale(1.25)}22%,92%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aTk2{0%,36%{transform:scale(0)}42%{transform:scale(1.25)}46%,92%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aTk3{0%,56%{transform:scale(0)}62%{transform:scale(1.25)}66%,92%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aProg4{0%,8%{width:0%}20%{width:33%}42%{width:66%}62%,92%{width:100%}100%{width:0%}}
@keyframes aTagA{0%,24%{opacity:0;transform:translateY(10px)}30%,90%{opacity:1;transform:none}96%,100%{opacity:0}}
@keyframes aTagB{0%,46%{opacity:0;transform:translateY(10px)}50%,90%{opacity:1;transform:none}96%,100%{opacity:0}}
@keyframes aTagC{0%,64%{opacity:0;transform:translateY(10px)}68%,90%{opacity:1;transform:none}96%,100%{opacity:0}}
"""
E = 'cubic-bezier(.6,0,.3,1) infinite'
anims4 = {'fig': f'aF4 4s {E}', 'shade': f'aS4 4s {E}', 'legR': f'aLg4 4s {E}', 'armL': f'aA4 4s {E}',
          'foreL': f'aFA4 4s {E}', 'gap': 'aG4 4s ease-in-out infinite', 'head': f'aH4 4s {E}', 'jaw': 'aJ4 4s ease-in-out infinite'}
checks = [('Gira 45°', 'Y el peso, en la pierna de atrás', 'aChk1', 'aTk1'),
          ('Crea aire', 'Mano a la cintura o al bolsillo', 'aChk2', 'aTk2'),
          ('Barbilla', 'Un poco adelante y abajo', 'aChk3', 'aTk3')]
rows4 = ''.join(
    f'<div style="flex: 1; display: flex; flex-direction: column; gap: 8px; padding: 16px 18px; border-radius: 20px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s ease-in-out infinite"><div style="display: flex; align-items: center; gap: 12px"><span style="flex: none; width: 40px; height: 40px; border-radius: 99px; border: 2px solid #FF6A1A; display: flex; align-items: center; justify-content: center"><svg width="24" height="24" viewBox="0 0 24 24" style="animation: {tk} 4s ease-out infinite"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#FF6A1A" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="{MONO}; font-weight: 600; font-size: 20px; color: #FF8F45">0{i+1}</span></div><span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em; line-height: 1">{t}</span><span style="font-size: 21px; color: #B5ADA4; line-height: 1.2">{d}</span></div>'
    for i, (t, d, a, tk) in enumerate(checks))
body4 = headline('LA POSE EN 3 PASOS', 'De tieso a natural', 'en diez segundos.', 88) + f"""
<div style="position: relative; height: 660px; display: flex; flex-direction: column; gap: 16px">
  <div style="position: relative; flex: 1; border-radius: 30px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
    <div style="position: absolute; left: 0; right: 0; top: -40px; bottom: 0">
      {studio()}{softbox('l')}
      <div style="position: absolute; left: 50%; bottom: -170px; margin-left: -140px; width: 280px; z-index: 3">{figure(280, 'm4', anims4)}</div>
    </div>
    {pill('AIRE ✓', '#FF6A1A', '#0A0908', 'left: 230px; top: 250px; opacity: 0; animation: aTagB 4s ease-out infinite')}
    {pill('CUERPO A 45° ✓', '#FF6A1A', '#0A0908', 'right: 90px; top: 250px; opacity: 0; animation: aTagA 4s ease-out infinite')}
    {pill('MANDÍBULA MARCADA ✓', '#FF6A1A', '#0A0908', 'right: 70px; top: 130px; opacity: 0; animation: aTagC 4s ease-out infinite')}
    <div style="position: absolute; inset: 16px; pointer-events: none; z-index: 5">{corners()}</div>
    {pill('POSE NATURAL ✓', '#F2EDE7', '#0A0908', 'left: 50%; top: 40px; opacity: 0; font-size: 24px; animation: aOk 4s ease-out infinite')}
    <div style="position: absolute; inset: 0; background: #FFFFFF; opacity: 0; z-index: 7; animation: aFl4 4s linear infinite"></div>
    <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 8px; background: rgba(242,237,231,.1); z-index: 6"><div style="height: 100%; background: #FF6A1A; width: 0%; animation: aProg4 4s ease-in-out infinite"></div></div>
  </div>
  <div style="display: flex; gap: 12px">{rows4}</div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · La pose en 3 pasos', 4, kf4, body4,
    'Y entre foto y foto, muévete un poco.', DESLIZA_TXT))

# ---------------------------------------------------------------- 05 CTA
kf5 = COMMON_KF + """
@keyframes aWipe{0%,8%{width:92%}46%,54%{width:8%}92%,100%{width:92%}}
@keyframes aKnob{0%,8%{left:92%}46%,54%{left:8%}92%,100%{left:92%}}
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
"""
scene_before = studio(False) + f'<div style="position: absolute; left: 50%; bottom: -200px; margin-left: -125px; width: 250px; filter: saturate(.6)">{figure(250, "b5")}</div>'
scene_after = studio() + softbox('l') + f'<div style="position: absolute; left: 50%; bottom: -200px; margin-left: -125px; width: 250px">{figure(250, "a5", pose="relaxed")}</div>'
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 82px; line-height: 1; letter-spacing: -0.045em">Antes del clic,<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">recoloca tu cuerpo.</span></p>
<div style="position: relative; margin-top: 40px; width: 920px; height: 480px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">
  <div style="position: absolute; inset: 0">{scene_after}</div>
  <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 92%; overflow: hidden; animation: aWipe 4s cubic-bezier(.65,0,.35,1) infinite"><div style="position: absolute; left: 0; top: 0; width: 920px; height: 480px">{scene_before}</div></div>
  <div style="position: absolute; top: 0; bottom: 0; left: 92%; width: 0; z-index: 5; animation: aKnob 4s cubic-bezier(.65,0,.35,1) infinite">
    <div style="position: absolute; top: 0; bottom: 0; left: -3px; width: 6px; background: #F2EDE7; box-shadow: 0 0 24px rgba(255,106,26,.9)"></div>
    <div style="position: absolute; top: 50%; left: -36px; width: 72px; height: 72px; margin-top: -36px; border-radius: 99px; background: #F2EDE7; display: flex; align-items: center; justify-content: center; color: #0A0908; {BRIC}; font-weight: 800; font-size: 30px">⇆</div></div>
  <div style="position: absolute; left: 20px; top: 18px; padding: 8px 16px; border-radius: 10px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; z-index: 6">RÍGIDO</div>
  <div style="position: absolute; right: 20px; top: 18px; padding: 8px 16px; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; z-index: 6">NATURAL</div>
</div>
<div style="position: relative; overflow: hidden; margin-top: 44px; padding: 26px 54px; border-radius: 30px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 64px; line-height: 1; letter-spacing: -0.04em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.3), rgba(255,255,255,0)); animation: aShim 4s ease-in-out 0.6s infinite"></div></div>
</div>
"""
open(os.path.join(OUT, 'S5.dc.html'), 'w').write(page('05 · CTA', 5, kf5, body5,
    'Guárdalo para tu próxima sesión de fotos.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
