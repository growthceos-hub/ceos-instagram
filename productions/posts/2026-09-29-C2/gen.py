#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C2 2026-09-29 (fondo a cámara) en src/."""
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


def window_el(anim=''):
    return f'''<div style="position: absolute; left: 6%; top: 9%; width: 19%; height: 50%; border-radius: 6px; border: 7px solid #6B635C; background: linear-gradient(160deg, #FFFFFF, #D9D1C8 70%, #B5ADA4); box-shadow: 0 0 90px 26px rgba(242,237,231,.28); animation: aGlare 2s ease-in-out infinite{anim}; box-sizing: border-box">
  <div style="position: absolute; left: 50%; top: 0; bottom: 0; width: 6px; margin-left: -3px; background: #6B635C"></div>
  <div style="position: absolute; top: 48%; left: 0; right: 0; height: 6px; background: #6B635C"></div></div>'''


def shelf_el(anim=''):
    items_top = [(14, 34, '#B5ADA4', -4), (10, 48, '#9C938B', 0), (18, 26, '#FF8A4A', 8), (12, 40, '#D9D1C8', -10), (16, 30, '#6B635C', 0)]
    items_bot = [(20, 22, '#9C938B', 0), (12, 44, '#B5ADA4', 6), (22, 30, '#FFB27A', -6), (14, 36, '#6B635C', 0)]
    def row(items):
        return ''.join(f'<div style="flex: none; width: {w}%; height: {h}px; background: {c}; border-radius: 3px; transform: rotate({r}deg); transform-origin: 50% 100%"></div>' for w, h, c, r in items)
    return f'''<div style="position: absolute; right: 5%; top: 16%; width: 27%; height: 52%{anim}">
  <div style="position: absolute; left: 0; right: 0; top: 0; height: 40%; display: flex; align-items: flex-end; gap: 3%; padding: 0 4%">{row(items_top)}</div>
  <div style="position: absolute; left: 0; right: 0; top: 40%; height: 9px; background: #6B635C; border-radius: 3px"></div>
  <div style="position: absolute; left: 0; right: 0; top: 46%; height: 40%; display: flex; align-items: flex-end; gap: 4%; padding: 0 5%">{row(items_bot)}</div>
  <div style="position: absolute; left: 0; right: 0; top: 86%; height: 9px; background: #6B635C; border-radius: 3px"></div></div>'''


def pile_el(anim=''):
    return f'''<div style="position: absolute; left: 2%; bottom: 8%; width: 24%; height: 26%{anim}">
  <div style="position: absolute; left: 8%; bottom: 0; width: 70%; height: 48%; border-radius: 40% 50% 12% 12%; background: #9C938B"></div>
  <div style="position: absolute; left: 30%; bottom: 36%; width: 64%; height: 42%; border-radius: 50% 44% 18% 18%; background: #FF8A4A; opacity: .8"></div>
  <div style="position: absolute; left: 0; bottom: 30%; width: 44%; height: 34%; border-radius: 50%; background: #D9D1C8; opacity: .85"></div></div>'''


def wall():
    return '''<div style="position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 38%, #2A150A, #0A0908 80%)"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 12%; background: #12100F; border-top: 2px solid rgba(242,237,231,.08)"></div>'''


def messy_room(pw=340, extra_person_style=''):
    return wall() + window_el() + shelf_el() + pile_el() + f'''
<div style="position: absolute; left: 50%; bottom: -50px; margin-left: -{pw//2}px; width: {pw}px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%{extra_person_style}">{person(pw)}</div>'''


COMMON_KF = """
@keyframes aStep{0%,24.9%{opacity:1}25%,100%{opacity:0}}
@keyframes aBreath{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-6px) scale(1.012)}}
@keyframes aGlare{0%,100%{filter:brightness(1)}50%{filter:brightness(1.18)}}
@keyframes aPing{0%{transform:scale(.6);opacity:.9}100%{transform:scale(1.9);opacity:0}}
"""

# ---------------------------------------------------------------- 01 GANCHO
kf1 = COMMON_KF + """
@keyframes aHunt{0%,18%{left:50%;top:62%;width:150px;height:120px}26%,42%{left:15.5%;top:34%;width:190px;height:290px}50%,66%{left:81.5%;top:42%;width:270px;height:250px}74%,90%{left:14%;top:78%;width:220px;height:150px}100%{left:50%;top:62%;width:150px;height:120px}}
@keyframes aHuntC{0%,18%{border-color:#F2EDE7}26%,90%{border-color:#FF3B30}100%{border-color:#F2EDE7}}
@keyframes aLbl1{0%,24%{opacity:0}28%,42%{opacity:1}46%,100%{opacity:0}}
@keyframes aLbl2{0%,48%{opacity:0}52%,66%{opacity:1}70%,100%{opacity:0}}
@keyframes aLbl3{0%,72%{opacity:0}76%,90%{opacity:1}94%,100%{opacity:0}}
@keyframes aTag0{0%,20%{opacity:1}24%,94%{opacity:.0}98%,100%{opacity:1}}
"""
def ping(left, top, delay):
    return f'''<div style="position: absolute; left: {left}; top: {top}; width: 0; height: 0; z-index: 4">
  <div style="position: absolute; left: -22px; top: -22px; width: 44px; height: 44px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 22px rgba(255,59,48,.8); display: flex; align-items: center; justify-content: center; color: #fff; {BRIC}; font-weight: 800; font-size: 28px">!</div>
  <div style="position: absolute; left: -22px; top: -22px; width: 44px; height: 44px; border-radius: 99px; border: 3px solid #FF3B30; animation: aPing 1.6s ease-out {delay}s infinite"></div></div>'''

def lbl(txt, left, top, anim):
    return f'<div style="position: absolute; left: {left}; top: {top}; transform: translateX(-50%); white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 21px; letter-spacing: .08em; opacity: 0; z-index: 6; animation: {anim} 4s linear infinite">{txt}</div>'

body1 = headline('EL FONDO DE TU VÍDEO', 'Lo que hay detrás de ti', 'habla antes que tú.', 88) + f"""
<div style="position: relative; height: 650px; border-radius: 34px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
  <div style="position: absolute; inset: 26px; border-radius: 22px; overflow: hidden; background: #0A0908">
    {messy_room(360)}
    {ping('25%', '20%', 0)}{ping('88%', '30%', -0.5)}{ping('24%', '72%', -1.0)}
    <div style="position: absolute; transform: translate(-50%,-50%); border: 3px solid #F2EDE7; border-radius: 8px; z-index: 5; animation: aHunt 4s cubic-bezier(.6,0,.3,1) infinite, aHuntC 4s steps(1) infinite; left: 50%; top: 62%; width: 150px; height: 120px"></div>
    {lbl('VENTANA QUE QUEMA', '44%', '30%', 'aLbl1')}{lbl('ESTANTERÍA CAÓTICA', '76%', '72%', 'aLbl2')}{lbl('ROPA EN LA SILLA', '25%', '59%', 'aLbl3')}
    <div style="position: absolute; left: 50%; top: 40%; transform: translateX(-50%); white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: rgba(10,9,8,.85); border: 2px solid #FF6A1A; color: #FF8F45; {MONO}; font-weight: 600; font-size: 21px; letter-spacing: .08em; z-index: 6; animation: aTag0 4s linear infinite">¿A QUIÉN ENFOCO?</div>
    <div style="position: absolute; inset: 16px; pointer-events: none; z-index: 5">{corners()}</div>
    {rec_timer()}
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Y casi nunca dice lo que quieres.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 DÓNDE MIRAN
kf2 = COMMON_KF + """
@keyframes aGaze{0%,6%{left:16%;top:34%}30%,38%{left:16%;top:34%}46%,64%{left:81%;top:30%}72%,94%{left:50%;top:60%}100%{left:16%;top:34%}}
@keyframes aHeat1{0%,38%{opacity:1;transform:scale(1)}46%,100%{opacity:.35;transform:scale(.8)}}
@keyframes aHeat2{0%,40%{opacity:0;transform:scale(.6)}48%,64%{opacity:1;transform:scale(1)}72%,100%{opacity:.35;transform:scale(.8)}}
@keyframes aHeat3{0%,66%{opacity:0;transform:scale(.6)}74%,94%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(.6)}}
@keyframes aC1{0%,38%{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A}44%,100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
@keyframes aC2{0%,42%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}46%,64%{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A}70%,100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
@keyframes aC3{0%,68%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}72%,96%{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A}100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.14)}}
"""
def heat(left, top, size, anim):
    return f'<div style="position: absolute; left: {left}; top: {top}; width: {size}px; height: {size}px; margin: -{size//2}px 0 0 -{size//2}px; border-radius: 50%; background: radial-gradient(circle, rgba(255,59,48,.85), rgba(255,106,26,.55) 35%, rgba(255,178,122,.2) 60%, rgba(255,178,122,0) 72%); mix-blend-mode: screen; z-index: 4; animation: {anim} 4s ease-in-out infinite"></div>'

chips2 = ''.join(
    f'<div style="flex: 1; display: flex; flex-direction: column; gap: 6px; padding: 18px 20px; border-radius: 20px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s ease-in-out infinite"><span style="{MONO}; font-weight: 600; font-size: 20px; opacity: .8">{n}</span><span style="{BRIC}; font-weight: 800; font-size: 31px; letter-spacing: -0.02em; line-height: 1.02">{t}</span></div>'
    for n, t, a in (('1º MIRAN', 'Lo que más brilla', 'aC1'), ('2º MIRAN', 'Lo que desentona', 'aC2'), ('3º MIRAN', 'Tu cara (por fin)', 'aC3')))
body2 = headline('DÓNDE MIRA LA GENTE', 'El ojo se va', 'a lo que más brilla.', 90) + f"""
<div style="position: relative; height: 640px; display: flex; flex-direction: column; gap: 18px">
  <div style="position: relative; flex: 1; border-radius: 30px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.5)">
    <div style="position: absolute; inset: 0; filter: saturate(.55) brightness(.8)">{messy_room(330)}</div>
    {heat('16%', '34%', 300, 'aHeat1')}{heat('81%', '30%', 260, 'aHeat2')}{heat('50%', '60%', 240, 'aHeat3')}
    <div style="position: absolute; left: 16%; top: 34%; width: 0; height: 0; z-index: 6; animation: aGaze 4s cubic-bezier(.65,0,.3,1) infinite">
      <div style="position: absolute; left: -46px; top: -46px; width: 92px; height: 92px; border-radius: 99px; border: 3px solid #F2EDE7; animation: aPing 1s ease-out infinite"></div>
      <div style="position: absolute; left: -30px; top: -30px; width: 60px; height: 60px; border-radius: 99px; background: rgba(242,237,231,.18); border: 3px solid #F2EDE7; display: flex; align-items: center; justify-content: center"><svg width="36" height="20" viewBox="0 0 46 24"><ellipse cx="23" cy="12" rx="21" ry="10" fill="none" stroke="#F2EDE7" stroke-width="3.5"/><circle cx="23" cy="12" r="5.5" fill="#F2EDE7"/></svg></div>
    </div>
    <div style="position: absolute; left: 22px; top: 18px; padding: 8px 14px; border-radius: 10px; background: rgba(10,9,8,.8); {MONO}; font-size: 19px; letter-spacing: .1em; color: #FFB27A; z-index: 6">RECORRIDO DE LA MIRADA · EJEMPLO</div>
  </div>
  <div style="display: flex; gap: 14px">{chips2}</div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Dónde miran', 2, kf2, body2,
    'Si algo brilla más que tú, te roba el vídeo.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 SEPÁRATE
kf3 = COMMON_KF + """
@keyframes aMove{0%,10%{top:22%}50%,86%{top:58%}100%{top:22%}}
@keyframes aDist{0%,10%{height:6%}50%,86%{height:42%}100%{height:6%}}
@keyframes aDistT{0%,10%{opacity:.4}50%,86%{opacity:1}100%{opacity:.4}}
@keyframes aBlur{0%,10%{filter:blur(0px) brightness(1.35)}50%,86%{filter:blur(9px) brightness(.8)}100%{filter:blur(0px) brightness(1.35)}}
@keyframes aShadow{0%,10%{opacity:1;transform:translate(60px,-10px) scale(1.12)}50%,86%{opacity:0;transform:translate(60px,-10px) scale(1.3)}100%{opacity:1;transform:translate(60px,-10px) scale(1.12)}}
@keyframes aPill1{0%,30%{opacity:1}40%,92%{opacity:0}100%{opacity:1}}
@keyframes aPill2{0%,40%{opacity:0}50%,86%{opacity:1}96%,100%{opacity:0}}
@keyframes aBeam{0%,100%{opacity:.35}50%{opacity:.7}}
"""
body3 = headline('EL TRUCO QUE NADIE USA', 'Sepárate de la pared:', 'el fondo se suaviza.', 84) + f"""
<div style="position: relative; height: 640px; display: flex; gap: 22px">
  <div style="position: relative; flex: none; width: 330px; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); overflow: hidden">
    <div style="position: absolute; left: 20px; top: 16px; {MONO}; font-size: 19px; letter-spacing: .1em; color: #9C938B">VISTA DESDE ARRIBA</div>
    <div style="position: absolute; left: 24px; right: 24px; top: 58px; height: 20px; border-radius: 6px; background: repeating-linear-gradient(45deg, #6B635C 0 10px, #1E1A17 10px 20px)"></div>
    <div style="position: absolute; left: 30px; top: 86px; {MONO}; font-size: 18px; letter-spacing: .1em; color: #B5ADA4">PARED</div>
    <div style="position: absolute; left: 50%; top: 80px; width: 4px; margin-left: -2px; background: #FF6A1A; border-radius: 4px; animation: aDist 4s cubic-bezier(.6,0,.3,1) infinite"></div>
    <div style="position: absolute; left: 50%; top: 22%; width: 86px; height: 86px; margin: -43px 0 0 -43px; border-radius: 99px; background: #F2EDE7; box-shadow: 0 0 40px rgba(255,106,26,.55); display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 30px; color: #0A0908; animation: aMove 4s cubic-bezier(.6,0,.3,1) infinite">TÚ</div>
    <div style="position: absolute; left: 50%; bottom: 60px; width: 0; height: 0; border-left: 60px solid transparent; border-right: 60px solid transparent; border-bottom: 170px solid rgba(255,106,26,.18); margin-left: -60px; animation: aBeam 2s ease-in-out infinite"></div>
    <div style="position: absolute; left: 50%; bottom: 26px; width: 110px; height: 60px; margin-left: -55px; border-radius: 12px; background: #1E1A17; border: 3px solid #FF6A1A; display: flex; align-items: center; justify-content: center"><div style="width: 30px; height: 30px; border-radius: 99px; border: 4px solid #FF6A1A"></div></div>
    <div style="position: absolute; right: 14px; top: 30%; padding: 8px 12px; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .06em; animation: aDistT 4s cubic-bezier(.6,0,.3,1) infinite">+ DISTANCIA</div>
  </div>
  <div style="position: relative; flex: 1; border-radius: 30px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.5)">
    <div style="position: absolute; inset: -20px; animation: aBlur 4s cubic-bezier(.6,0,.3,1) infinite">{wall()}{window_el()}{shelf_el()}</div>
    <div style="position: absolute; left: 50%; bottom: -40px; margin-left: -175px; width: 350px; opacity: 1; filter: blur(5px) brightness(0); animation: aShadow 4s cubic-bezier(.6,0,.3,1) infinite">{person(350)}</div>
    <div style="position: absolute; left: 50%; bottom: -40px; margin-left: -175px; width: 350px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{person(350)}</div>
    <div style="position: absolute; inset: 16px; pointer-events: none">{corners()}</div>
    <div style="position: absolute; left: 50%; top: 40px; transform: translateX(-50%); white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 21px; letter-spacing: .08em; animation: aPill1 4s linear infinite">PEGADO: SOMBRA Y FONDO NÍTIDO</div>
    <div style="position: absolute; left: 50%; top: 40px; transform: translateX(-50%); white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 21px; letter-spacing: .08em; opacity: 0; animation: aPill2 4s linear infinite">SEPARADO: TÚ DESTACAS ✓</div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Sepárate', 3, kf3, body3,
    'Da unos pasos al frente y la sombra desaparece.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 SET EN 3 CAPAS
kf4 = COMMON_KF + """
@keyframes aOut{0%,12%{opacity:1;transform:scale(1)}26%,92%{opacity:0;transform:scale(.9)}100%{opacity:1;transform:scale(1)}}
@keyframes aWin{0%,12%{opacity:1}26%,92%{opacity:.0}100%{opacity:1}}
@keyframes aLight{0%,36%{opacity:0}48%,92%{opacity:1}100%{opacity:0}}
@keyframes aLamp{0%,36%{opacity:.15;box-shadow:none}48%,92%{opacity:1;box-shadow:0 0 50px 16px rgba(255,178,122,.75)}100%{opacity:.15;box-shadow:none}}
@keyframes aBrand{0%,58%{opacity:0;transform:translateY(24px)}68%,92%{opacity:1;transform:translateY(0)}100%{opacity:0;transform:translateY(24px)}}
@keyframes aChk1{0%,14%{background:#12100F;border-color:rgba(242,237,231,.14)}22%,92%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aChk2{0%,38%{background:#12100F;border-color:rgba(242,237,231,.14)}46%,92%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aChk3{0%,60%{background:#12100F;border-color:rgba(242,237,231,.14)}68%,92%{background:#1E1A17;border-color:#FF6A1A}100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aTk1{0%,14%{transform:scale(0)}20%{transform:scale(1.25)}24%,92%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aTk2{0%,38%{transform:scale(0)}44%{transform:scale(1.25)}48%,92%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aTk3{0%,60%{transform:scale(0)}66%{transform:scale(1.25)}70%,92%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aProg4{0%,10%{width:0%}24%{width:33%}48%{width:66%}70%,92%{width:100%}100%{width:0%}}
"""
anim_out = '; animation: aOut 4s cubic-bezier(.6,0,.3,1) infinite'
room4 = wall() + f'''
<div style="position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 42%, rgba(255,138,74,.55), rgba(255,106,26,.12) 45%, rgba(10,9,8,0) 70%); animation: aLight 4s ease-in-out infinite"></div>
<div style="position: absolute; left: 0; top: 0; right: 0; bottom: 0; animation: aWin 4s cubic-bezier(.6,0,.3,1) infinite">{window_el()}</div>
{shelf_el(anim_out)}{pile_el(anim_out)}
<div style="position: absolute; left: 11%; bottom: 12%; width: 60px; height: 220px; display: flex; flex-direction: column; align-items: center">
  <div style="width: 70px; height: 50px; border-radius: 40px 40px 6px 6px; background: #FFB27A; animation: aLamp 4s ease-in-out infinite"></div>
  <div style="width: 6px; flex: 1; background: #6B635C"></div><div style="width: 50px; height: 8px; border-radius: 4px; background: #6B635C"></div></div>
<div style="position: absolute; right: 9%; bottom: 12%; width: 140px; height: 260px; animation: aBrand 4s cubic-bezier(.3,0,.2,1) infinite">
  <div style="position: absolute; left: 10px; right: 10px; top: 0; height: 120px; border-radius: 10px; border: 4px solid #F2EDE7; background: #1E1A17; display: flex; align-items: center; justify-content: center"><img src="{LOGO}" style="width: 70px; height: 70px"></div>
  <div style="position: absolute; left: 30px; bottom: 0; width: 80px; height: 64px; border-radius: 8px 8px 16px 16px; background: #6B635C"></div>
  <div style="position: absolute; left: 20px; bottom: 56px; width: 100px; height: 70px; border-radius: 50% 50% 20% 20%; background: radial-gradient(circle at 50% 70%, #4E8A5A, #2E5A3A)"></div></div>
<div style="position: absolute; left: 50%; bottom: -50px; margin-left: -170px; width: 340px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{person(340)}</div>'''
checks = [('Despeja', 'Fuera lo que no cuenta nada', 'aChk1', 'aTk1'),
          ('Ilumina el fondo', 'Una luz suave detrás, cálida', 'aChk2', 'aTk2'),
          ('Fírmalo', 'Un solo detalle de tu marca', 'aChk3', 'aTk3')]
rows4 = ''.join(
    f'<div style="flex: 1; display: flex; flex-direction: column; gap: 8px; padding: 16px 18px; border-radius: 20px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s ease-in-out infinite"><div style="display: flex; align-items: center; gap: 12px"><span style="flex: none; width: 40px; height: 40px; border-radius: 99px; border: 2px solid #FF6A1A; display: flex; align-items: center; justify-content: center"><svg width="24" height="24" viewBox="0 0 24 24" style="animation: {tk} 4s ease-out infinite"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#FF6A1A" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="{MONO}; font-weight: 600; font-size: 20px; color: #FF8F45">0{i+1}</span></div><span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em; line-height: 1">{t}</span><span style="font-size: 21px; color: #B5ADA4; line-height: 1.2">{d}</span></div>'
    for i, (t, d, a, tk) in enumerate(checks))
body4 = headline('MONTA TU SET EN 3 PASOS', 'Despeja, ilumina', 'y firma tu fondo.', 88) + f"""
<div style="position: relative; height: 650px; display: flex; flex-direction: column; gap: 16px">
  <div style="position: relative; flex: 1; border-radius: 30px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
    {room4}
    <div style="position: absolute; inset: 16px; pointer-events: none; z-index: 5">{corners()}</div>
    {rec_timer()}
    <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 8px; background: rgba(242,237,231,.1); z-index: 6"><div style="height: 100%; background: #FF6A1A; width: 0%; animation: aProg4 4s ease-in-out infinite"></div></div>
  </div>
  <div style="display: flex; gap: 12px">{rows4}</div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Set en 3 pasos', 4, kf4, body4,
    'Sin obras: con lo que ya tienes en casa.', DESLIZA_TXT))

# ---------------------------------------------------------------- 05 CTA
kf5 = COMMON_KF + """
@keyframes aWipe{0%,8%{width:92%}46%,54%{width:8%}92%,100%{width:92%}}
@keyframes aKnob{0%,8%{left:92%}46%,54%{left:8%}92%,100%{left:92%}}
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
"""
clean_room = wall() + f'''<div style="position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 42%, rgba(255,138,74,.5), rgba(255,106,26,.1) 45%, rgba(10,9,8,0) 70%)"></div>
<div style="position: absolute; left: 12%; bottom: 12%; width: 60px; height: 190px; display: flex; flex-direction: column; align-items: center"><div style="width: 64px; height: 46px; border-radius: 40px 40px 6px 6px; background: #FFB27A; box-shadow: 0 0 50px 16px rgba(255,178,122,.7)"></div><div style="width: 6px; flex: 1; background: #6B635C"></div></div>
<div style="position: absolute; right: 10%; bottom: 12%; width: 120px; height: 230px"><div style="position: absolute; left: 8px; right: 8px; top: 0; height: 104px; border-radius: 10px; border: 4px solid #F2EDE7; background: #1E1A17; display: flex; align-items: center; justify-content: center"><img src="{LOGO}" style="width: 60px; height: 60px"></div><div style="position: absolute; left: 26px; bottom: 0; width: 68px; height: 56px; border-radius: 8px 8px 14px 14px; background: #6B635C"></div><div style="position: absolute; left: 16px; bottom: 48px; width: 88px; height: 62px; border-radius: 50% 50% 20% 20%; background: radial-gradient(circle at 50% 70%, #4E8A5A, #2E5A3A)"></div></div>
<div style="position: absolute; left: 50%; bottom: -50px; margin-left: -150px; width: 300px">{person(300)}</div>'''
messy5 = wall() + window_el() + shelf_el() + pile_el() + f'<div style="position: absolute; left: 50%; bottom: -50px; margin-left: -150px; width: 300px">{person(300)}</div>'
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 82px; line-height: 1; letter-spacing: -0.045em">Antes de darle a REC,<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">mira detrás de ti.</span></p>
<div style="position: relative; margin-top: 40px; width: 920px; height: 470px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">
  <div style="position: absolute; inset: 0">{clean_room}</div>
  <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 92%; overflow: hidden; animation: aWipe 4s cubic-bezier(.65,0,.35,1) infinite"><div style="position: absolute; left: 0; top: 0; width: 920px; height: 470px; filter: saturate(.7)">{messy5}</div></div>
  <div style="position: absolute; top: 0; bottom: 0; left: 92%; width: 0; z-index: 5; animation: aKnob 4s cubic-bezier(.65,0,.35,1) infinite">
    <div style="position: absolute; top: 0; bottom: 0; left: -3px; width: 6px; background: #F2EDE7; box-shadow: 0 0 24px rgba(255,106,26,.9)"></div>
    <div style="position: absolute; top: 50%; left: -36px; width: 72px; height: 72px; margin-top: -36px; border-radius: 99px; background: #F2EDE7; display: flex; align-items: center; justify-content: center; color: #0A0908; {BRIC}; font-weight: 800; font-size: 30px">⇆</div></div>
  <div style="position: absolute; left: 20px; top: 18px; padding: 8px 16px; border-radius: 10px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; z-index: 6">ANTES</div>
  <div style="position: absolute; right: 20px; top: 18px; padding: 8px 16px; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; z-index: 6">DESPUÉS</div>
</div>
<div style="position: relative; overflow: hidden; margin-top: 44px; padding: 26px 54px; border-radius: 30px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 64px; line-height: 1; letter-spacing: -0.04em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.3), rgba(255,255,255,0)); animation: aShim 4s ease-in-out 0.6s infinite"></div></div>
</div>
"""
open(os.path.join(OUT, 'S5.dc.html'), 'w').write(page('05 · CTA', 5, kf5, body5,
    'Guárdalo para tu próxima grabación.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
