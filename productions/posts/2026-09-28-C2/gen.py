#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C2 (sonido: que tu vídeo no suene a lata) en src/."""
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
random.seed(28092)

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

# ---------------------------------------------------------------- 01 GANCHO
kf1 = SWAP_KF + """
@keyframes aBarN{0%,100%{transform:scaleY(.45)}25%{transform:scaleY(1)}50%{transform:scaleY(.7)}75%{transform:scaleY(.95)}}
@keyframes aBarC{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}
@keyframes aPlay{0%{transform:translateX(0)}100%{transform:translateX(860px)}}
@keyframes aNoiseL{0%,20%{opacity:1}30%,88%{opacity:0}96%,100%{opacity:1}}
@keyframes aCleanL{0%,24%{opacity:0}36%,84%{opacity:1}94%,100%{opacity:0}}
@keyframes aMeter{0%,20%{height:92%;background:#FF3B30}32%,86%{height:62%;background:#FF6A1A}96%,100%{height:92%;background:#FF3B30}}
@keyframes aWig{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.86)}}
"""
N = 44
noisy, clean = [], []
env = [0.15,0.55,0.9,0.75,0.95,0.6,0.2,0.05,0.4,0.85,1,0.7,0.9,0.5,0.1,0.05,0.3,0.7,0.95,0.8,0.55,0.2,
       0.05,0.45,0.8,1,0.85,0.6,0.9,0.7,0.3,0.06,0.2,0.65,0.9,0.75,0.95,0.5,0.15,0.05,0.35,0.75,0.6,0.2]
for i in range(N):
    hn = 0.45 + random.random() * 0.55
    d = -random.random()
    noisy.append(f'<div style="flex: 1; height: {hn*100:.0f}%; border-radius: 4px; background: linear-gradient(180deg,#FF6B61,#B5ADA4); opacity: .85; transform-origin: 50% 50%; animation: aBarN {0.5 if i%2 else 1}s ease-in-out {d:.2f}s infinite"></div>')
    hc = max(0.04, env[i])
    clean.append(f'<div style="flex: 1; height: {hc*100:.0f}%; border-radius: 6px; background: linear-gradient(180deg,#FFB27A,#FF6A1A); box-shadow: 0 0 14px rgba(255,106,26,.55); transform-origin: 50% 50%; animation: aBarC 1s ease-in-out {d:.2f}s infinite"></div>')
body1 = f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 22px">
<span style="align-self: flex-start; padding: 10px 18px; border-radius: 999px; background: #FF6A1A; color: #0A0908; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 20px; letter-spacing: 0.1em">¿TU VÍDEO SUENA A LATA?</span>
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 112px; line-height: 0.92; letter-spacing: -0.055em">No se ve mal.<br><span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">Se oye mal.</span></h1>
</div>

<div style="position: relative; height: 560px; border-radius: 34px; overflow: hidden; background: radial-gradient(ellipse at 50% 40%, #2A150A, #12100F 70%); border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
  <div style="position: absolute; top: 34px; left: 42px; display: flex; align-items: center; gap: 12px; font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.1em"><span style="width: 16px; height: 16px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 14px #FF3B30; animation: aRec 1s steps(1) infinite"></span>AUDIO · PISTA 1</div>
  <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#F2EDE7" stroke-width="1.8" style="position: absolute; top: 22px; right: 40px; opacity: .9"><path d="M3 14v-2a9 9 0 0 1 18 0v2"/><rect x="2.5" y="13.5" width="5" height="7" rx="2" fill="#FF6A1A" stroke="none"/><rect x="16.5" y="13.5" width="5" height="7" rx="2" fill="#FF6A1A" stroke="none"/></svg>
  <div style="position: absolute; left: 42px; right: 42px; top: 50%; height: 1px; background: rgba(242,237,231,.14)"></div>
  <div style="position: absolute; left: 42px; right: 112px; top: 120px; height: 300px; display: flex; align-items: center; gap: 7px; animation: aNoiseL 4s ease-in-out infinite">{''.join(noisy)}</div>
  <div style="position: absolute; left: 42px; right: 112px; top: 120px; height: 300px; display: flex; align-items: center; gap: 7px; opacity: 0; animation: aCleanL 4s ease-in-out infinite">{''.join(clean)}</div>
  <div style="position: absolute; left: 42px; top: 100px; width: 4px; height: 340px; border-radius: 4px; background: #F2EDE7; box-shadow: 0 0 18px rgba(242,237,231,.9); animation: aPlay 4s linear infinite"></div>
  <div style="position: absolute; right: 42px; top: 120px; width: 34px; height: 300px; border-radius: 10px; background: rgba(242,237,231,.08); overflow: hidden">
    <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 92%; background: #FF3B30; animation: aMeter 4s ease-in-out infinite"><div style="position:absolute;inset:0;background:repeating-linear-gradient(180deg,transparent 0 10px,rgba(10,9,8,.7) 10px 13px);animation: aWig .5s ease-in-out infinite;transform-origin:50% 100%"></div></div>
  </div>
  <div style="position: absolute; bottom: 34px; left: 42px; height: 58px; width: 700px">
    <span style="{BADGE_BAD}; animation: aBad 4s ease-in-out infinite">✕ ECO + RUIDO DE FONDO</span>
    <span style="{BADGE_GOOD}; opacity: 0; animation: aGood 4s ease-in-out infinite">✓ VOZ LIMPIA Y CERCANA</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'La gente perdona una imagen normal. Un mal audio, no.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 DISTANCIA
kf2 = SWAP_KF + """
@keyframes aMic{0%,16%{transform:translateX(0)}40%,82%{transform:translateX(-470px)}96%,100%{transform:translateX(0)}}
@keyframes aRing{0%{transform:scale(.2);opacity:.9}100%{transform:scale(3.2);opacity:0}}
@keyframes aVoz{0%,16%{width:24%}40%,82%{width:92%}96%,100%{width:24%}}
@keyframes aSala{0%,16%{width:88%}40%,82%{width:14%}96%,100%{width:88%}}
@keyframes aDist{0%,16%{opacity:1}26%,88%{opacity:0}96%,100%{opacity:1}}
@keyframes aDist2{0%,26%{opacity:0}40%,82%{opacity:1}92%,100%{opacity:0}}
"""
rings = ''.join(f'<div style="position: absolute; left: 236px; top: 118px; width: 80px; height: 80px; margin: -40px 0 0 -40px; border-radius: 999px; border: 3px solid rgba(255,106,26,.8); animation: aRing 2s ease-out {-i*0.5:.1f}s infinite"></div>' for i in range(4))
body2 = num_head('01', 'DISTANCIA DEL MICRO',
    'Micro cerca<br>de tu boca.<br><span style="font-family: \'Instrument Serif\', serif; font-style: italic; font-weight: 400; color: #FF6A1A">No en la cámara.</span>',
    'Lejos graba <b style="color: #F2EDE7">la habitación</b>. A un palmo, <b style="color: #F2EDE7">tu voz</b>.') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 0; right: 0; bottom: 110px; height: 2px; background: rgba(242,237,231,0.14)"></div>
  <svg width="420" height="360" viewBox="0 0 420 360" style="position: absolute; left: 40px; top: 0">
    <g fill="#F2EDE7" opacity=".92">
      <ellipse cx="190" cy="120" rx="58" ry="68"/>
      <path d="M100 360 C100 250 140 210 190 210 C240 210 280 250 280 360 Z"/>
      <rect x="168" y="170" width="44" height="50" rx="16"/>
    </g>
    <circle cx="222" cy="108" r="7" fill="#0A0908"/>
  </svg>
  {rings}
  <div style="position: absolute; left: 790px; top: 120px; width: 90px; height: 170px; animation: aMic 4s cubic-bezier(.65,0,.35,1) infinite">
    <div style="position: absolute; left: 20px; top: 0; width: 56px; height: 104px; border-radius: 12px; background: #1E1A17; border: 3px solid #F2EDE7"><div style="position:absolute;left:18px;top:8px;width:14px;height:4px;border-radius:4px;background:#9C938B"></div><div style="position:absolute;left:14px;top:40px;width:22px;height:22px;border-radius:99px;background:#FF6A1A;box-shadow:0 0 18px rgba(255,106,26,.9)"></div></div>
    <div style="position: absolute; left: 44px; top: 104px; width: 6px; height: 64px; background: #9C938B"></div>
  </div>
  <div style="position: absolute; right: 40px; top: 30px; height: 56px; width: 360px">
    <span style="position: absolute; right: 0; top: 0; white-space: nowrap; font-family: 'JetBrains Mono', monospace; font-size: 22px; letter-spacing: .1em; color: #FF6B61; animation: aDist 4s ease-in-out infinite">↔ LEJOS DE TI</span>
    <span style="position: absolute; right: 0; top: 0; white-space: nowrap; font-family: 'JetBrains Mono', monospace; font-size: 22px; letter-spacing: .1em; color: #FFB27A; opacity: 0; animation: aDist2 4s ease-in-out infinite">↔ A UN PALMO</span>
  </div>
  <div style="position: absolute; left: 40px; right: 40px; bottom: 26px; display: grid; grid-template-columns: 110px 1fr; row-gap: 16px; align-items: center; font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: .1em; color: #B5ADA4">
    <span>TU VOZ</span><div style="height: 22px; border-radius: 99px; background: rgba(242,237,231,.08)"><div style="height: 100%; border-radius: 99px; background: linear-gradient(90deg,#FF6A1A,#FFB27A); box-shadow: 0 0 16px rgba(255,106,26,.7); width: 24%; animation: aVoz 4s cubic-bezier(.65,0,.35,1) infinite"></div></div>
    <span>SALA</span><div style="height: 22px; border-radius: 99px; background: rgba(242,237,231,.08)"><div style="height: 100%; border-radius: 99px; background: linear-gradient(90deg,#9C938B,#FF6B61); width: 88%; animation: aSala 4s cubic-bezier(.65,0,.35,1) infinite"></div></div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Distancia', 2, kf2, body2,
    'Sin micro: graba el audio con otro móvil cerca de ti.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 ECO
kf3 = SWAP_KF + """
@keyframes aRay{to{stroke-dashoffset:-120}}
@keyframes aRaysBad{0%,18%{opacity:1}30%,88%{opacity:0}96%,100%{opacity:1}}
@keyframes aRaysGood{0%,26%{opacity:0}40%,84%{opacity:1}94%,100%{opacity:0}}
@keyframes aSoft{0%,20%{opacity:0;transform:scale(.7)}36%,86%{opacity:1;transform:scale(1)}96%,100%{opacity:0;transform:scale(.7)}}
@keyframes aPulse{0%,100%{r:14}50%{r:19}}
"""
cx, cy = 460, 230
bad_rays = [
    "M460 230 L60 90 L300 30 L860 170",
    "M460 230 L860 60 L640 430 L60 300",
    "M460 230 L220 430 L60 180 L520 30",
    "M460 230 L860 330 L420 430 L60 60",
    "M460 230 L700 30 L860 250 L300 430",
]
good_rays = ["M460 230 L150 230", "M460 230 L770 230", "M460 230 L530 110", "M460 230 L300 350", "M460 230 L620 350", "M460 230 L200 170", "M460 230 L640 110"]
bad_svg = ''.join(f'<path d="{d}" stroke="#FF6B61" stroke-width="3" fill="none" stroke-dasharray="14 10" stroke-linejoin="round" style="animation: aRay 1s linear infinite; opacity:.85"/>' for d in bad_rays)
good_svg = ''.join(f'<path d="{d}" stroke="#FF6A1A" stroke-width="4" fill="none" stroke-dasharray="14 10" stroke-linecap="round" style="animation: aRay 1s linear infinite; filter: drop-shadow(0 0 6px rgba(255,106,26,.9))"/>' for d in good_rays)
def soft(x, y, w, h, label, delay):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; border-radius: 14px; background: repeating-linear-gradient(90deg, rgba(255,178,122,.28) 0 10px, rgba(255,106,26,.16) 10px 20px); border: 2px solid rgba(255,178,122,.7); display: flex; align-items: center; justify-content: center; font-family: \'JetBrains Mono\', monospace; font-size: 17px; letter-spacing: .1em; color: #F2EDE7; opacity: 0; animation: aSoft 4s ease-in-out {delay}s infinite">{label}</div>'
body3 = num_head('02', 'ECO DE LA SALA',
    'Si la sala suena,<br><span style="font-family: \'Instrument Serif\', serif; font-style: italic; font-weight: 400; color: #FF6A1A">tu voz también.</span>',
    'Paredes desnudas rebotan la voz. <b style="color: #F2EDE7">Cortinas, alfombra y sofá</b> se la comen.') + f"""
<div style="position: relative; height: 480px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 40px; top: 20px; width: 840px; height: 440px; border: 6px solid #B5ADA4; border-radius: 10px; box-sizing: border-box"></div>
  <svg width="920" height="480" viewBox="0 0 920 480" style="position: absolute; inset: 0">
    <g style="animation: aRaysBad 4s ease-in-out infinite">{bad_svg}</g>
    <g style="opacity: 0; animation: aRaysGood 4s ease-in-out infinite">{good_svg}</g>
    <circle cx="{cx}" cy="{cy}" r="16" fill="#F2EDE7" style="animation: aPulse 1s ease-in-out infinite"/>
  </svg>
  {soft(52, 150, 90, 170, 'CORTINA', 0)}
  {soft(778, 150, 90, 170, 'CORTINA', 0.1)}
  {soft(250, 350, 420, 90, 'ALFOMBRA', 0.2)}
  {soft(380, 32, 300, 70, 'SOFÁ · ESTANTERÍA', 0.3)}
  <div style="position: absolute; left: 70px; top: 50px; height: 56px; width: 300px">
    <span style="{BADGE_BAD}; font-size: 20px; animation: aBad 4s ease-in-out infinite">✕ RETUMBA</span>
    <span style="{BADGE_GOOD}; font-size: 20px; opacity: 0; animation: aGood 4s ease-in-out infinite">✓ SECO Y CLARO</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Eco', 3, kf3, body3,
    'Test rápido: da una palmada. Si retumba, hay eco.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 PRUEBA
kf4 = """
@keyframes aChk1{0%,8%{background:transparent;border-color:rgba(242,237,231,.3)}14%,94%{background:#FF6A1A;border-color:#FF6A1A}100%{background:transparent;border-color:rgba(242,237,231,.3)}}
@keyframes aTick{0%,8%{opacity:0;transform:scale(.4)}14%,94%{opacity:1;transform:scale(1)}100%{opacity:0}}
@keyframes aRow{0%,8%{opacity:.45}14%,94%{opacity:1}100%{opacity:.45}}
@keyframes aLvl{0%{height:38%}12%{height:62%}24%{height:48%}36%{height:70%}48%{height:55%}60%{height:66%}72%{height:44%}84%{height:68%}100%{height:38%}}
@keyframes aPeak{0%,100%{bottom:62%}36%{bottom:72%}84%{bottom:70%}}
@keyframes aTimer{0%{stroke-dashoffset:0}100%{stroke-dashoffset:-277}}
"""
items = ['Aire y ventiladores apagados', 'Móvil en modo avión', 'Micro a un palmo de la boca', 'Graba 10 s y escúchalo con cascos']
rows = ''
for i, t in enumerate(items):
    d = i * 0.7
    rows += f"""<div style="display: flex; align-items: center; gap: 22px; animation: aRow 4s ease-in-out {d}s infinite; animation-fill-mode: both">
<div style="flex: none; position: relative; width: 46px; height: 46px; border-radius: 12px; border: 3px solid rgba(242,237,231,.3); box-sizing: border-box; animation: aChk1 4s ease-in-out {d}s infinite; animation-fill-mode: both"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" style="position: absolute; left: 5px; top: 5px; animation: aTick 4s ease-in-out {d}s infinite; animation-fill-mode: both"><path d="M5 12l5 5L20 7"/></svg></div>
<span style="font-size: 32px; font-weight: 600; line-height: 1.15">{t}</span></div>"""
bars4 = ''.join(f'<div style="position: absolute; left: {i*30}px; bottom: 0; width: 22px; border-radius: 6px 6px 2px 2px; background: linear-gradient(0deg,#FF6A1A,#FFB27A); box-shadow: 0 0 12px rgba(255,106,26,.6); animation: aLvl {1 if i%2 else 2}s ease-in-out {-i*0.23:.2f}s infinite; height: 50%"></div>' for i in range(6))
body4 = num_head('03', 'PRUEBA ANTES DE GRABAR',
    'Antes de darle a REC,<br><span style="font-family: \'Instrument Serif\', serif; font-style: italic; font-weight: 400; color: #FF6A1A">escúchate 10 segundos.</span>',
    'Lo que no oyes ahora, lo oirá <b style="color: #F2EDE7">todo el que vea el vídeo</b>.') + f"""
<div style="position: relative; height: 460px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden; display: flex; align-items: center; padding: 0 44px; box-sizing: border-box; gap: 40px">
  <div style="flex: 1; display: flex; flex-direction: column; gap: 30px">{rows}</div>
  <div style="flex: none; position: relative; width: 190px; height: 380px; border-radius: 24px; background: #0A0908; border: 2px solid rgba(242,237,231,.14)">
    <svg width="110" height="110" viewBox="0 0 100 100" style="position: absolute; left: 40px; top: 18px"><circle cx="50" cy="50" r="44" stroke="rgba(242,237,231,.12)" stroke-width="8" fill="none"/><circle cx="50" cy="50" r="44" stroke="#FF6A1A" stroke-width="8" fill="none" stroke-dasharray="277" stroke-linecap="round" transform="rotate(-90 50 50)" style="animation: aTimer 4s linear infinite"/><text x="50" y="58" text-anchor="middle" font-family="JetBrains Mono" font-size="24" fill="#F2EDE7">10s</text></svg>
    <div style="position: absolute; left: 12px; right: 12px; top: 138px; text-align: center; font-family: 'JetBrains Mono', monospace; font-size: 15px; letter-spacing: .1em; color: #9C938B">NIVEL</div>
    <div style="position: absolute; left: 12px; right: 12px; bottom: 24px; height: 190px">
      <div style="position: absolute; left: 0; right: 0; top: 0; height: 22%; background: rgba(255,59,48,.18); border-radius: 6px"></div>
      <div style="position: absolute; left: 14px; bottom: 0; width: 172px; height: 190px">{bars4}</div>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Prueba', 4, kf4, body4,
    'Haz captura y úsala antes de tu próxima grabación.', DESLIZA_TXT))

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
labels = ['SONIDO', 'LUZ', 'ENCUADRE', 'GUION', 'EDICIÓN', 'GANCHO']
def tile(i):
    wb = ''.join(f'<div style="width: 6px; height: {h}px; border-radius: 3px; background: #F2EDE7; animation: aTB 1s ease-in-out {-(i+j)*0.17:.2f}s infinite"></div>' for j, h in enumerate([14, 30, 22, 38, 18]))
    return f'<div style="position: relative; aspect-ratio: 1/1; border-radius: 12px; background: linear-gradient(160deg, #2A150A, #171412); border: 1px solid rgba(242,237,231,.1); animation: aTile 4s ease-in-out {i*0.4:.1f}s infinite; display: flex; align-items: center; justify-content: center; gap: 5px"><span style="position: absolute; top: 10px; left: 12px; font-family: \'JetBrains Mono\', monospace; font-size: 14px; color: #FFB27A">{labels[i]}</span>{wb}</div>'
tiles = ''.join(tile(i) for i in range(6))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 80px; line-height: 1; letter-spacing: -0.045em">Que se te <span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">oiga</span><br>como se te ve.</p>
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
