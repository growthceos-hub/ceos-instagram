#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C4 (B-roll: planos recurso) en src/."""
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

import random
random.seed(28094)

BADGE_BAD = "position: absolute; left: 0; top: 0; white-space: nowrap; padding: 12px 22px; border-radius: 14px; background: rgba(10,9,8,.85); border: 2px solid #FF3B30; color: #FF6B61; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 22px; letter-spacing: 0.1em"
BADGE_GOOD = "position: absolute; left: 0; top: 0; white-space: nowrap; padding: 12px 22px; border-radius: 14px; background: #FF6A1A; color: #0A0908; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 22px; letter-spacing: 0.1em"
SWAP_KF = """
@keyframes aBad{0%,18%{opacity:1}28%,88%{opacity:0}96%,100%{opacity:1}}
@keyframes aGood{0%,24%{opacity:0}36%,84%{opacity:1}94%,100%{opacity:0}}
"""

def num_head(n, tag, h2, p):
    return f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 28px">
<div style="display: flex; align-items: flex-end; gap: 28px">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 170px; line-height: 0.78; letter-spacing: -0.07em; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">{n}</span>
<span style="margin-bottom: 8px; padding: 10px 18px; border-radius: 999px; border: 1px solid rgba(242,237,231,0.2); font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.1em; color: #B5ADA4">{tag}</span>
</div>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 88px; line-height: 0.95; letter-spacing: -0.05em">{h2}</h2>
<p style="margin: 0; font-size: 34px; line-height: 1.25; color: #D9D1C8">{p}</p>
</div>"""

IT = "font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A"
MONO = "font-family: 'JetBrains Mono', monospace"

# helpers de escena
PERSON = lambda w=300, op='.9': f'<svg width="{w}" height="{w}" viewBox="0 0 300 300" style="position: absolute; left: 50%; margin-left: -{w//2}px; bottom: -6px"><g fill="rgba(242,237,231,{op})"><ellipse cx="150" cy="112" rx="48" ry="57"/><path d="M52 310 C52 208 98 176 150 176 C202 176 248 208 248 310 Z"/></g></svg>'
def scene_detail():  # manos + taza / producto en macro
    return """<svg viewBox="0 0 400 240" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0"><defs><radialGradient id="gd" cx="50%" cy="40%" r="70%"><stop offset="0" stop-color="#3A2A20"/><stop offset="1" stop-color="#12100F"/></radialGradient></defs><rect width="400" height="240" fill="url(#gd)"/><rect x="150" y="70" width="100" height="120" rx="14" fill="#FF6A1A"/><rect x="250" y="95" width="34" height="60" rx="17" fill="none" stroke="#FF6A1A" stroke-width="12"/><path d="M170 50 q10 -20 0 -40 M200 50 q10 -20 0 -40 M230 50 q10 -20 0 -40" stroke="rgba(242,237,231,.5)" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 240 C60 190 110 180 150 170 L150 200 C120 210 100 230 100 240Z" fill="rgba(242,237,231,.85)"/><path d="M360 240 C340 190 300 185 262 176 L262 205 C290 212 310 230 310 240Z" fill="rgba(242,237,231,.85)"/></svg>"""
def scene_process():  # manos en portátil / pantalla
    return """<svg viewBox="0 0 400 240" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0"><rect width="400" height="240" fill="#171412"/><rect x="80" y="40" width="240" height="140" rx="10" fill="#0A0908" stroke="rgba(242,237,231,.35)" stroke-width="4"/><rect x="100" y="62" width="120" height="12" rx="6" fill="#FF6A1A"/><rect x="100" y="86" width="190" height="10" rx="5" fill="rgba(242,237,231,.35)"/><rect x="100" y="106" width="160" height="10" rx="5" fill="rgba(242,237,231,.25)"/><rect x="100" y="126" width="175" height="10" rx="5" fill="rgba(242,237,231,.25)"/><path d="M50 200 h300 l-20 20 h-260z" fill="rgba(242,237,231,.3)"/><ellipse cx="160" cy="206" rx="40" ry="16" fill="rgba(242,237,231,.9)"/><ellipse cx="250" cy="206" rx="40" ry="16" fill="rgba(242,237,231,.9)"/></svg>"""
def scene_ambient():  # espacio / fachada / sala
    return """<svg viewBox="0 0 400 240" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0"><defs><linearGradient id="ga" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A150A"/><stop offset="1" stop-color="#12100F"/></linearGradient></defs><rect width="400" height="240" fill="url(#ga)"/><rect x="0" y="180" width="400" height="60" fill="rgba(242,237,231,.08)"/><rect x="40" y="50" width="90" height="130" fill="rgba(242,237,231,.12)"/><rect x="150" y="30" width="110" height="150" fill="rgba(242,237,231,.18)"/><rect x="280" y="70" width="80" height="110" fill="rgba(242,237,231,.1)"/><circle cx="205" cy="80" r="26" fill="#FF6A1A" opacity=".9"/><path d="M205 106 L180 180 h50z" fill="rgba(255,106,26,.25)"/><rect x="60" y="70" width="20" height="20" fill="#FFB27A" opacity=".6"/><rect x="95" y="70" width="20" height="20" fill="#FFB27A" opacity=".4"/><rect x="300" y="90" width="18" height="18" fill="#FFB27A" opacity=".5"/></svg>"""
def scene_talk():
    return f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%, #3A2A20, #171412 75%)">{PERSON(260)}</div>'

VF = """<div style="position: absolute; inset: 18px; pointer-events: none">
<div style="position: absolute; left: 0; top: 0; width: 40px; height: 40px; border-left: 4px solid #F2EDE7; border-top: 4px solid #F2EDE7"></div>
<div style="position: absolute; right: 0; top: 0; width: 40px; height: 40px; border-right: 4px solid #F2EDE7; border-top: 4px solid #F2EDE7"></div>
<div style="position: absolute; left: 0; bottom: 0; width: 40px; height: 40px; border-left: 4px solid #F2EDE7; border-bottom: 4px solid #F2EDE7"></div>
<div style="position: absolute; right: 0; bottom: 0; width: 40px; height: 40px; border-right: 4px solid #F2EDE7; border-bottom: 4px solid #F2EDE7"></div>
<div style="position: absolute; left: 18px; top: 12px; display: flex; align-items: center; gap: 10px; font-family: 'JetBrains Mono', monospace; font-size: 18px; letter-spacing: .1em; color: #F2EDE7"><span style="width: 14px; height: 14px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30; animation: aRec 1s steps(1) infinite"></span>REC</div>
</div>"""

# ---------------------------------------------------------------- 01 GANCHO
kf1 = """
@keyframes aS1{0%,22%{opacity:1}25%,100%{opacity:0}}
@keyframes aS2{0%,22%{opacity:0}25%,47%{opacity:1}50%,100%{opacity:0}}
@keyframes aS3{0%,47%{opacity:0}50%,72%{opacity:1}75%,100%{opacity:0}}
@keyframes aS4{0%,72%{opacity:0}75%,97%{opacity:1}100%{opacity:0}}
@keyframes aKen{0%{transform:scale(1)}100%{transform:scale(1.12)}}
@keyframes aHead{0%{left:0%}100%{left:100%}}
@keyframes aDrop1{0%,18%{transform:translateY(-70px);opacity:0}24%,100%{transform:translateY(0);opacity:1}}
@keyframes aDrop2{0%,43%{transform:translateY(-70px);opacity:0}49%,100%{transform:translateY(0);opacity:1}}
@keyframes aDrop3{0%,68%{transform:translateY(-70px);opacity:0}74%,100%{transform:translateY(0);opacity:1}}
@keyframes aLab{0%,100%{opacity:1}50%{opacity:.6}}
@keyframes aWave{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}
"""
wave = ''.join(f'<div style="flex:1; height: 100%; border-radius: 3px; background: rgba(242,237,231,.55); transform-origin: 50% 50%; animation: aWave 1s ease-in-out {-(i*0.13)%1:.2f}s infinite"></div>' for i in range(46))
def clip(left, width, label, anim):
    return f'<div style="position: absolute; left: {left}%; width: {width}%; top: 0; height: 100%; border-radius: 10px; background: linear-gradient(135deg,#FF6A1A,#FFB27A); color: #0A0908; {MONO}; font-weight: 600; font-size: 15px; letter-spacing: .08em; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 24px rgba(255,106,26,.6); opacity: 0; animation: {anim} 4s cubic-bezier(.3,1.3,.5,1) infinite">{label}</div>'
body1 = f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 22px">
<span style="align-self: flex-start; padding: 10px 18px; border-radius: 999px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: 0.1em">EL TRUCO DE LAS PRODUCTORAS</span>
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 104px; line-height: 0.95; letter-spacing: -0.055em">Tu vídeo no aburre.<br><span style="{IT}; animation: aHeat 4s ease-in-out infinite">Le falta B-roll.</span></h1>
</div>

<div style="position: relative; height: 600px; border-radius: 34px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
  <div style="position: absolute; left: 40px; right: 40px; top: 32px; height: 340px; border-radius: 20px; overflow: hidden; background: #0A0908">
    <div style="position: absolute; inset: 0; animation: aS1 4s linear infinite">{scene_talk()}</div>
    <div style="position: absolute; inset: 0; opacity: 0; animation: aS2 4s linear infinite"><div style="position:absolute;inset:0;animation: aKen 4s linear infinite">{scene_detail()}</div></div>
    <div style="position: absolute; inset: 0; opacity: 0; animation: aS3 4s linear infinite"><div style="position:absolute;inset:0;animation: aKen 4s linear infinite">{scene_process()}</div></div>
    <div style="position: absolute; inset: 0; opacity: 0; animation: aS4 4s linear infinite"><div style="position:absolute;inset:0;animation: aKen 4s linear infinite">{scene_ambient()}</div></div>
    {VF}
    <div style="position: absolute; right: 80px; top: 30px; {MONO}; font-size: 18px; letter-spacing: .1em">
      <span style="position:absolute; right:0; white-space:nowrap; color:#B5ADA4; animation: aS1 4s linear infinite">A-ROLL · HABLANDO</span>
      <span style="position:absolute; right:0; white-space:nowrap; color:#FFB27A; opacity:0; animation: aS2 4s linear infinite">B-ROLL · DETALLE</span>
      <span style="position:absolute; right:0; white-space:nowrap; color:#FFB27A; opacity:0; animation: aS3 4s linear infinite">B-ROLL · PROCESO</span>
      <span style="position:absolute; right:0; white-space:nowrap; color:#FFB27A; opacity:0; animation: aS4 4s linear infinite">B-ROLL · AMBIENTE</span>
    </div>
  </div>
  <div style="position: absolute; left: 40px; right: 40px; top: 400px; height: 170px">
    <span style="position: absolute; left: 0; top: 14px; {MONO}; font-size: 16px; letter-spacing: .1em; color: #FFB27A">V2</span>
    <span style="position: absolute; left: 0; top: 76px; {MONO}; font-size: 16px; letter-spacing: .1em; color: #9C938B">V1</span>
    <span style="position: absolute; left: 0; top: 132px; {MONO}; font-size: 16px; letter-spacing: .1em; color: #9C938B">A1</span>
    <div style="position: absolute; left: 50px; right: 0; top: 0; height: 170px">
      <div style="position: absolute; left: 0; right: 0; top: 0; height: 46px; border-radius: 10px; background: rgba(242,237,231,.04); border: 1px dashed rgba(242,237,231,.14)">
        {clip(25, 22, 'DETALLE', 'aDrop1')}{clip(50, 22, 'PROCESO', 'aDrop2')}{clip(75, 24, 'AMBIENTE', 'aDrop3')}
      </div>
      <div style="position: absolute; left: 0; right: 0; top: 62px; height: 46px; border-radius: 10px; background: rgba(242,237,231,.12); border: 1px solid rgba(242,237,231,.2); display: flex; align-items: center; padding-left: 16px; {MONO}; font-size: 15px; letter-spacing: .08em; color: #B5ADA4">TÚ HABLANDO A CÁMARA</div>
      <div style="position: absolute; left: 0; right: 0; top: 124px; height: 40px; border-radius: 10px; background: rgba(242,237,231,.06); display: flex; gap: 4px; padding: 6px 12px; box-sizing: border-box">{wave}</div>
      <div style="position: absolute; top: -10px; bottom: -6px; width: 4px; border-radius: 4px; background: #F2EDE7; box-shadow: 0 0 18px rgba(242,237,231,.9); animation: aHead 4s linear infinite"></div>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Los planos que cambian un vídeo casero por uno pro.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 EL PROBLEMA
kf2 = SWAP_KF + """
@keyframes aAtt{0%{width:96%;background:#FFB27A}70%{width:14%;background:#FF3B30}78%{width:14%;background:#FF3B30}90%,100%{width:96%;background:#FFB27A}}
@keyframes aBlur{0%,60%{filter:none;opacity:1}70%,78%{filter:blur(3px) grayscale(.6);opacity:.55}88%,100%{filter:none;opacity:1}}
@keyframes aFlick{0%,70%{transform:translateY(0);opacity:0}74%{opacity:1}82%{transform:translateY(-120px);opacity:1}86%,100%{transform:translateY(-140px);opacity:0}}
@keyframes aT1{0%,24%{opacity:1}25%,100%{opacity:0}}
@keyframes aT2{0%,24%{opacity:0}25%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes aT3{0%,49%{opacity:0}50%,74%{opacity:1}75%,100%{opacity:0}}
@keyframes aT4{0%,74%{opacity:0}75%,100%{opacity:1}}
@keyframes aBreath{0%,100%{transform:scale(1)}50%{transform:scale(1.01)}}
"""
body2 = num_head('01', 'EL PROBLEMA',
    f'Un plano fijo<br><span style="{IT}">todo el vídeo.</span>',
    'La misma cara, el mismo fondo, sin un solo cambio. <b style="color: #F2EDE7">El ojo se cansa y hace scroll.</b>') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 44px; top: 34px; width: 520px; height: 300px; border-radius: 18px; overflow: hidden; background: #0A0908; animation: aBlur 4s ease-in-out infinite">
    <div style="position:absolute; inset:0; animation: aBreath 4s ease-in-out infinite">{scene_talk()}</div>
    {VF}
    <div style="position: absolute; right: 74px; top: 30px; {MONO}; font-size: 20px; letter-spacing: .08em; color: #F2EDE7; width: 70px; height: 24px">
      <span style="position:absolute; right:0; animation: aT1 4s steps(1) infinite">0:05</span><span style="position:absolute; right:0; opacity:0; animation: aT2 4s steps(1) infinite">0:15</span><span style="position:absolute; right:0; opacity:0; animation: aT3 4s steps(1) infinite">0:30</span><span style="position:absolute; right:0; opacity:0; animation: aT4 4s steps(1) infinite">0:45</span>
    </div>
  </div>
  <div style="position: absolute; left: 600px; top: 34px; right: 44px; height: 300px; display: flex; flex-direction: column; justify-content: center; gap: 18px">
    <span style="{MONO}; font-size: 18px; letter-spacing: .12em; color: #9C938B">ATENCIÓN DEL QUE MIRA</span>
    <div style="height: 34px; border-radius: 99px; background: rgba(242,237,231,.1); overflow: hidden"><div style="height: 100%; border-radius: 99px; animation: aAtt 4s cubic-bezier(.4,0,.6,1) infinite"></div></div>
    <span style="{MONO}; font-size: 16px; letter-spacing: .1em; color: #9C938B; line-height: 1.6">MISMO PLANO<br>MISMO FONDO<br>CERO CAMBIOS</span>
    <div style="position: relative; height: 70px">
      <div style="position: absolute; left: 40px; top: 10px; width: 56px; height: 56px; border-radius: 999px; background: rgba(242,237,231,.85); box-shadow: 0 10px 30px rgba(0,0,0,.6); opacity: 0; animation: aFlick 4s cubic-bezier(.4,0,.2,1) infinite"></div>
    </div>
  </div>
  <div style="position: absolute; left: 44px; bottom: 40px; height: 56px; width: 900px">
    <span style="{BADGE_BAD}; animation: aBad 4s ease-in-out infinite">✕ 1 PLANO = SCROLL</span>
    <span style="{BADGE_GOOD}; opacity: 0; animation: aGood 4s ease-in-out infinite">✓ LA SOLUCIÓN: PLANOS RECURSO →</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · El problema', 2, kf2, body2,
    'No es tu cara. Es que nunca cambia nada.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 LOS 3 PLANOS
kf3 = """
@keyframes aP1{0%,30%{opacity:1}33%,97%{opacity:0}100%{opacity:1}}
@keyframes aP2{0%,30%{opacity:0}33%,63%{opacity:1}66%,100%{opacity:0}}
@keyframes aP3{0%,63%{opacity:0}66%,97%{opacity:1}100%{opacity:0}}
@keyframes aZoomIn{0%{transform:scale(1.25)}100%{transform:scale(1)}}
@keyframes aPan{0%{transform:scale(1.15) translateX(-20px)}100%{transform:scale(1.15) translateX(20px)}}
@keyframes aC1{0%,2%{background:#171412;border-color:rgba(242,237,231,.12)}5%,30%{background:#2A150A;border-color:#FF6A1A}33%,100%{background:#171412;border-color:rgba(242,237,231,.12)}}
@keyframes aC2{0%,33%{background:#171412;border-color:rgba(242,237,231,.12)}36%,63%{background:#2A150A;border-color:#FF6A1A}66%,100%{background:#171412;border-color:rgba(242,237,231,.12)}}
@keyframes aC3{0%,66%{background:#171412;border-color:rgba(242,237,231,.12)}69%,96%{background:#2A150A;border-color:#FF6A1A}99%,100%{background:#171412;border-color:rgba(242,237,231,.12)}}
@keyframes aFoc{0%,100%{transform:scale(1);opacity:.9}50%{transform:scale(1.12);opacity:.5}}
"""
cards = [('DETALLE', 'Manos, producto, herramienta. Muy de cerca.', 'aC1'),
         ('PROCESO', 'Tú trabajando: escribir, preparar, montar.', 'aC2'),
         ('AMBIENTE', 'El lugar: entrada, sala, gente moviéndose.', 'aC3')]
ccards = ''.join(f'<div style="border-radius: 18px; border: 2px solid rgba(242,237,231,.12); padding: 16px 20px; animation: {a} 4s ease-in-out infinite"><span style="display:block; {MONO}; font-size: 16px; letter-spacing: .12em; color: #FFB27A; margin-bottom: 6px">PLANO {i+1} · {t}</span><span style="font-size: 25px; font-weight: 600; line-height: 1.15">{d}</span></div>' for i, (t, d, a) in enumerate(cards))
body3 = num_head('02', '3 PLANOS RECURSO',
    f'Graba estos 3<br><span style="{IT}">además de hablar.</span>',
    'Unos segundos de cada uno bastan para <b style="color: #F2EDE7">tapar cortes y dar ritmo</b>.') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden; display: flex; align-items: center; gap: 30px; padding: 0 36px; box-sizing: border-box">
  <div style="flex: none; position: relative; width: 470px; height: 400px; border-radius: 22px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,.2)">
    <div style="position: absolute; inset: 0; animation: aP1 4s linear infinite"><div style="position:absolute;inset:0;animation: aZoomIn 1.33s ease-out infinite">{scene_detail()}</div></div>
    <div style="position: absolute; inset: 0; opacity: 0; animation: aP2 4s linear infinite"><div style="position:absolute;inset:0;animation: aPan 1.33s linear infinite">{scene_process()}</div></div>
    <div style="position: absolute; inset: 0; opacity: 0; animation: aP3 4s linear infinite"><div style="position:absolute;inset:0;animation: aPan 1.33s linear infinite reverse">{scene_ambient()}</div></div>
    {VF}
    <div style="position: absolute; left: 50%; top: 50%; width: 90px; height: 90px; margin: -45px 0 0 -45px; border: 3px solid #FFB27A; border-radius: 12px; animation: aFoc 1.33s ease-in-out infinite"></div>
  </div>
  <div style="flex: 1; display: flex; flex-direction: column; gap: 14px">{ccards}</div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Los 3 planos', 3, kf3, body3,
    'Guárdalo como checklist para tu próxima grabación.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 CÓMO MONTARLO
kf4 = """
@keyframes aHead{0%{left:0%}100%{left:100%}}
@keyframes aW1{0%,14%{color:#9C938B;background:transparent}18%,38%{color:#0A0908;background:#FF6A1A}42%,100%{color:#9C938B;background:transparent}}
@keyframes aW2{0%,52%{color:#9C938B;background:transparent}56%,78%{color:#0A0908;background:#FF6A1A}82%,100%{color:#9C938B;background:transparent}}
@keyframes aV1{0%,15%{opacity:0;transform:translateY(-40px)}19%,100%{opacity:1;transform:translateY(0)}}
@keyframes aV2{0%,53%{opacity:0;transform:translateY(-40px)}57%,100%{opacity:1;transform:translateY(0)}}
@keyframes aM1{0%,17%{opacity:1}18%,39%{opacity:0}40%,55%{opacity:1}56%,79%{opacity:0}80%,100%{opacity:1}}
@keyframes aM2{0%,17%{opacity:0}18%,39%{opacity:1}40%,100%{opacity:0}}
@keyframes aM3{0%,55%{opacity:0}56%,79%{opacity:1}80%,100%{opacity:0}}
@keyframes aWave{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}
"""
wave4 = ''.join(f'<div style="flex:1; height: 100%; border-radius: 3px; background: rgba(242,237,231,.55); animation: aWave 1s ease-in-out {-(i*0.11)%1:.2f}s infinite"></div>' for i in range(50))
body4 = num_head('03', 'CÓMO MONTARLO',
    f'Tu voz sigue.<br><span style="{IT}">La imagen cambia.</span>',
    'Pon el B-roll <b style="color: #F2EDE7">justo cuando nombras algo</b>, encima de tu voz y tapando los cortes.') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 40px; top: 30px; width: 380px; height: 240px; border-radius: 16px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,.18)">
    <div style="position:absolute; inset:0; animation: aM1 4s steps(1) infinite">{scene_talk()}</div>
    <div style="position:absolute; inset:0; opacity:0; animation: aM2 4s steps(1) infinite">{scene_detail()}</div>
    <div style="position:absolute; inset:0; opacity:0; animation: aM3 4s steps(1) infinite">{scene_process()}</div>
  </div>
  <div style="position: absolute; left: 450px; right: 40px; top: 30px; height: 240px; display: flex; flex-direction: column; gap: 12px">
    <span style="{MONO}; font-size: 16px; letter-spacing: .12em; color: #9C938B">LO QUE DICES</span>
    <p style="margin: 0; font-size: 31px; line-height: 1.45; font-weight: 600; color: #9C938B">“Primero preparo <span style="padding: 2px 8px; border-radius: 8px; animation: aW1 4s ease-in-out infinite">el producto</span> y luego lo <span style="padding: 2px 8px; border-radius: 8px; animation: aW2 4s ease-in-out infinite">edito en el ordenador</span>.”</p>
  </div>
  <div style="position: absolute; left: 40px; right: 40px; top: 300px; height: 150px">
    <div style="position: absolute; left: 0; right: 0; top: 0; height: 40px; border-radius: 10px; background: rgba(242,237,231,.04); border: 1px dashed rgba(242,237,231,.14)">
      <div style="position: absolute; left: 18%; width: 22%; top: 0; height: 100%; border-radius: 10px; background: linear-gradient(135deg,#FF6A1A,#FFB27A); color: #0A0908; {MONO}; font-weight: 600; font-size: 15px; display: flex; align-items: center; justify-content: center; letter-spacing: .08em; opacity: 0; animation: aV1 4s cubic-bezier(.3,1.3,.5,1) infinite">B · DETALLE</div>
      <div style="position: absolute; left: 56%; width: 24%; top: 0; height: 100%; border-radius: 10px; background: linear-gradient(135deg,#FF6A1A,#FFB27A); color: #0A0908; {MONO}; font-weight: 600; font-size: 15px; display: flex; align-items: center; justify-content: center; letter-spacing: .08em; opacity: 0; animation: aV2 4s cubic-bezier(.3,1.3,.5,1) infinite">B · PROCESO</div>
    </div>
    <div style="position: absolute; left: 0; right: 0; top: 52px; height: 40px; border-radius: 10px; background: rgba(242,237,231,.12); display: flex; align-items: center; padding-left: 14px; {MONO}; font-size: 14px; letter-spacing: .08em; color: #B5ADA4">A · TÚ HABLANDO <span style="margin-left: auto; margin-right: 12px; display:flex; gap: 18%; width: 50%"><span style="margin-left:22%;color:#FF6B61;font-size:22px">✂</span><span style="margin-left:20%;color:#FF6B61;font-size:22px">✂</span></span></div>
    <div style="position: absolute; left: 0; right: 0; top: 104px; height: 40px; border-radius: 10px; background: rgba(242,237,231,.06); display: flex; gap: 4px; padding: 6px 12px; box-sizing: border-box">{wave4}</div>
    <div style="position: absolute; top: -8px; bottom: -4px; width: 4px; border-radius: 4px; background: #F2EDE7; box-shadow: 0 0 18px rgba(242,237,231,.9); animation: aHead 4s linear infinite"></div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Cómo montarlo', 4, kf4, body4,
    'Nombras algo → se ve. Así de simple.', DESLIZA_TXT))
# ---------------------------------------------------------------- 05 CTA
kf5 = """
@keyframes aBtn{0%,40%{background:#FF6A1A;color:#0A0908}48%,90%{background:#1E1A17;color:#F2EDE7}97%,100%{background:#FF6A1A;color:#0A0908}}
@keyframes aTxtA{0%,42%{opacity:1}46%,92%{opacity:0}97%,100%{opacity:1}}
@keyframes aTxtB{0%,42%{opacity:0}46%,92%{opacity:1}97%,100%{opacity:0}}
@keyframes aTap{0%,22%{transform:translate(120px,140px);opacity:0}32%{transform:translate(0,0);opacity:1}40%{transform:translate(0,0) scale(.85);opacity:1}48%{transform:translate(0,0) scale(1);opacity:1}62%,100%{transform:translate(90px,160px);opacity:0}}
@keyframes aRip{0%,39%{transform:scale(.2);opacity:0}42%{opacity:.9}60%,100%{transform:scale(2.4);opacity:0}}
@keyframes aTile{0%,100%{opacity:.55}50%{opacity:1}}
@keyframes aTB{0%,100%{transform:scaleY(.4)}50%{transform:scaleY(1)}}
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
"""
labels = ['B-ROLL', 'LUZ', 'SONIDO', 'ENCUADRE', 'GUION', 'EDICIÓN']
def tile(i):
    wb = ''.join(f'<div style="width: 6px; height: {h}px; border-radius: 3px; background: #F2EDE7; animation: aTB 1s ease-in-out {-(i+j)*0.17:.2f}s infinite"></div>' for j, h in enumerate([14, 30, 22, 38, 18]))
    return f'<div style="position: relative; aspect-ratio: 1/1; border-radius: 12px; background: linear-gradient(160deg, #2A150A, #171412); border: 1px solid rgba(242,237,231,.1); animation: aTile 4s ease-in-out {i*0.4:.1f}s infinite; display: flex; align-items: center; justify-content: center; gap: 5px"><span style="position: absolute; top: 10px; left: 12px; font-family: \'JetBrains Mono\', monospace; font-size: 14px; color: #FFB27A">{labels[i]}</span>{wb}</div>'
tiles = ''.join(tile(i) for i in range(6))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 76px; line-height: 1; letter-spacing: -0.045em">Graba <span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">más que tu cara</span>.<br>Y tu vídeo cambia.</p>
<div style="position: relative; margin-top: 40px; width: 600px; border-radius: 40px; background: #12100F; border: 2px solid rgba(242,237,231,0.12); padding: 34px 36px 30px; box-sizing: border-box; display: flex; flex-direction: column; gap: 24px; box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">
  <div style="display: flex; align-items: center; gap: 22px; text-align: left">
    <div style="flex: none; width: 104px; height: 104px; border-radius: 999px; padding: 4px; background: linear-gradient(135deg, #FF6A1A, #FFB27A); box-sizing: border-box"><div style="width: 100%; height: 100%; border-radius: 999px; background: #0A0908; display: flex; align-items: center; justify-content: center"><img src="{LOGO}" style="width: 62px; height: 62px"></div></div>
    <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 36px; letter-spacing: -0.02em">ceos.productions</span><span style="font-size: 24px; color: #9C938B">Estudio de grabación y foto · Burgos</span></div>
  </div>
  <div style="position: relative">
    <div style="position: relative; height: 72px; border-radius: 16px; font-weight: 700; font-size: 30px; animation: aBtn 4s ease-in-out infinite; background: #FF6A1A; color: #0A0908">
      <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; animation: aTxtA 4s ease-in-out infinite">Seguir</span>
      <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; opacity: 0; animation: aTxtB 4s ease-in-out infinite">Siguiendo ✓</span>
    </div>
    <div style="position: absolute; left: 50%; top: 50%; width: 90px; height: 90px; margin: -45px 0 0 -45px; border-radius: 999px; border: 3px solid #FFB27A; animation: aRip 4s ease-out infinite; opacity: 0"></div>
    <div style="position: absolute; left: 50%; top: 50%; width: 56px; height: 56px; margin: -10px 0 0 -10px; border-radius: 999px; background: rgba(242,237,231,.85); box-shadow: 0 10px 30px rgba(0,0,0,.5); animation: aTap 4s cubic-bezier(.4,0,.2,1) infinite; opacity: 0"></div>
  </div>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px">{tiles}</div>
</div>
<div style="position: relative; overflow: hidden; margin-top: 40px; padding: 26px 54px; border-radius: 30px; background: #FF6A1A; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 64px; line-height: 1; letter-spacing: -0.04em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.3), rgba(255,255,255,0)); animation: aShim 4s ease-in-out 0.6s infinite"></div></div>
</div>
"""
open(os.path.join(OUT, 'S5.dc.html'), 'w').write(page('05 · CTA', 5, kf5, body5,
    'Cada día, un tip para grabarte mejor.',
    """<span style="font-family: 'JetBrains Mono', monospace; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
