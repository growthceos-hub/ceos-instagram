#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C3 (los 3 primeros segundos: ganchos) en src/."""
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
random.seed(28093)

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

# ---------------------------------------------------------------- 01 GANCHO
kf1 = """
@keyframes aN3{0%,24%{opacity:1;transform:scale(1)}25.5%,100%{opacity:0;transform:scale(.6)}}
@keyframes aN2{0%,25%{opacity:0;transform:scale(1.4)}26.5%,48%{opacity:1;transform:scale(1)}49.5%,100%{opacity:0;transform:scale(.6)}}
@keyframes aN1{0%,49%{opacity:0;transform:scale(1.4)}50.5%,70%{opacity:1;transform:scale(1)}73%,100%{opacity:0;transform:scale(.6)}}
@keyframes aNS{0%,70%{opacity:0;transform:translateY(30px)}75%,94%{opacity:1;transform:translateY(0)}100%{opacity:0}}
@keyframes aRing{0%{stroke-dashoffset:0}72%,100%{stroke-dashoffset:-603}}
@keyframes aRingC{0%,48%{stroke:#FF6A1A}52%,100%{stroke:#FF3B30}}
@keyframes aFeed{0%,72%{transform:translateY(0)}84%,95%{transform:translateY(-50%)}100%{transform:translateY(-50%)}}
@keyframes aFade{0%,4%{opacity:0}8%,94%{opacity:1}100%{opacity:0}}
@keyframes aThumb{0%,64%{transform:translate(0,120px);opacity:0}70%{transform:translate(0,40px);opacity:1}84%{transform:translate(0,-190px);opacity:1}90%,100%{transform:translate(0,-220px);opacity:0}}
@keyframes aSub{0%{clip-path:inset(0 100% 0 0)}40%,100%{clip-path:inset(0 0 0 0)}}
@keyframes aBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes aProg{0%{width:0}72%,100%{width:100%}}
"""
def reel(bg, sub, subanim):
    return f"""<div style="position: relative; height: 50%; background: {bg}; overflow: hidden">
  <svg width="300" height="300" viewBox="0 0 300 300" style="position: absolute; left: 0; bottom: 60px; animation: aBob 2s ease-in-out infinite"><g fill="rgba(242,237,231,.88)"><ellipse cx="150" cy="120" rx="46" ry="54"/><path d="M60 300 C60 210 100 180 150 180 C200 180 240 210 240 300 Z"/></g></svg>
  <div style="position: absolute; left: 18px; right: 18px; bottom: 34px; padding: 10px 12px; border-radius: 10px; background: rgba(10,9,8,.78); font-size: 20px; font-weight: 600; line-height: 1.2; color: #F2EDE7; text-align: center; {subanim}">{sub}</div>
</div>"""
body1 = f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 22px">
<span style="align-self: flex-start; padding: 10px 18px; border-radius: 999px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: 0.1em">¿TE HACEN SCROLL?</span>
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 100px; line-height: 0.95; letter-spacing: -0.055em; white-space: nowrap">Tienes 3 segundos.<br><span style="{IT}; animation: aHeat 4s ease-in-out infinite">Luego, scroll.</span></h1>
</div>

<div style="position: relative; height: 560px; border-radius: 34px; overflow: hidden; background: radial-gradient(ellipse at 70% 45%, #2A150A, #12100F 70%); border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
  <div style="position: absolute; left: 70px; top: 34px; width: 300px; height: 492px; border-radius: 40px; background: #0A0908; border: 3px solid rgba(242,237,231,.3); overflow: hidden; box-shadow: 0 30px 70px -20px rgba(0,0,0,.8)">
    <div style="position: absolute; left: 0; right: 0; top: 0; height: 200%; animation: aFeed 4s cubic-bezier(.65,0,.35,1) infinite">
      {reel('linear-gradient(180deg,#3A2A20,#1E1A17)', '“Hola a todos, hoy os quiero hablar de…”', 'animation: aSub 4s steps(24) infinite')}
      {reel('linear-gradient(180deg,#2A150A,#12100F)', 'Siguiente vídeo →', '')}
    </div>
    <div style="position: absolute; left: 16px; right: 16px; top: 18px; height: 5px; border-radius: 9px; background: rgba(242,237,231,.2)"><div style="height: 100%; border-radius: 9px; background: #F2EDE7; animation: aProg 4s linear infinite"></div></div>
    <div style="position: absolute; left: 50%; bottom: 30px; width: 64px; height: 64px; margin-left: -32px; border-radius: 999px; background: rgba(242,237,231,.85); box-shadow: 0 10px 30px rgba(0,0,0,.6); opacity: 0; animation: aThumb 4s cubic-bezier(.4,0,.2,1) infinite"></div>
  </div>
  <div style="position: absolute; left: 430px; top: 70px; width: 420px; display: flex; flex-direction: column; align-items: center; gap: 26px">
    <div style="position: relative; width: 240px; height: 240px">
      <svg width="240" height="240" viewBox="0 0 220 220" style="position: absolute; inset: 0"><circle cx="110" cy="110" r="96" stroke="rgba(242,237,231,.1)" stroke-width="14" fill="none"/><circle cx="110" cy="110" r="96" stroke="#FF6A1A" stroke-width="14" fill="none" stroke-linecap="round" stroke-dasharray="603" transform="rotate(-90 110 110)" style="animation: aRing 4s linear infinite, aRingC 4s linear infinite; filter: drop-shadow(0 0 10px rgba(255,106,26,.8))"/></svg>
      <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 150px; letter-spacing: -0.06em; animation: aN3 4s ease-in-out infinite">3</span>
      <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 150px; letter-spacing: -0.06em; opacity: 0; animation: aN2 4s ease-in-out infinite">2</span>
      <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 150px; letter-spacing: -0.06em; color: #FF6B61; opacity: 0; animation: aN1 4s ease-in-out infinite">1</span>
      <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 40px; letter-spacing: .08em; color: #FF6B61; opacity: 0; animation: aNS 4s ease-in-out infinite">SCROLL ↑</span>
    </div>
    <span style="{MONO}; font-size: 22px; letter-spacing: .12em; color: #B5ADA4; text-align: center; line-height: 1.5">SEGUNDOS PARA<br>ENGANCHAR</span>
    <span style="padding: 12px 22px; border-radius: 14px; background: rgba(10,9,8,.85); border: 2px solid #FF3B30; color: #FF6B61; {MONO}; font-weight: 600; font-size: 21px; letter-spacing: 0.08em; white-space: nowrap; animation: aGlow 2s ease-in-out infinite">✕ EMPEZAR SALUDANDO</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Si no enganchas al principio, el resto no se ve.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 EMPIEZA POR EL FINAL
kf2 = SWAP_KF + """
@keyframes aRes{0%,18%{left:66%}42%,86%{left:0%}98%,100%{left:66%}}
@keyframes aA{0%,18%{left:0%}42%,86%{left:34%}98%,100%{left:0%}}
@keyframes aB{0%,18%{left:33%}42%,86%{left:67%}98%,100%{left:33%}}
@keyframes aHead{0%{left:0%}100%{left:100%}}
@keyframes aLift{0%,18%{transform:translateY(0)}24%,36%{transform:translateY(-34px)}42%,100%{transform:translateY(0)}}
@keyframes aQ1{0%,20%{opacity:1}30%,86%{opacity:0}96%,100%{opacity:1}}
@keyframes aQ2{0%,28%{opacity:0;transform:translateY(14px)}40%,84%{opacity:1;transform:translateY(0)}94%,100%{opacity:0}}
"""
blk = "position: absolute; top: 0; width: 32%; height: 100%; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 20px; letter-spacing: .08em; box-sizing: border-box"
ticks = ''.join(f'<div style="position: absolute; left: {i*10}%; top: 0; height: {16 if i%5==0 else 9}px; width: 2px; background: rgba(242,237,231,.25)"></div>' for i in range(11))
body2 = num_head('01', 'EMPIEZA POR EL FINAL',
    f'Lo mejor,<br><span style="{IT}">en el segundo 1.</span>',
    'Nada de saludos ni presentaciones: abre con <b style="color: #F2EDE7">el resultado, el error o la promesa</b>.') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 44px; right: 44px; top: 36px; height: 132px; border-radius: 20px; background: linear-gradient(135deg,#2A150A,#171412); border: 1px solid rgba(242,237,231,.12)">
    <span style="position: absolute; left: 24px; top: 16px; {MONO}; font-size: 16px; letter-spacing: .12em; color: #9C938B">LO PRIMERO QUE SE OYE</span>
    <span style="position: absolute; left: 24px; right: 24px; top: 50px; font-size: 34px; font-weight: 600; color: #B5ADA4; animation: aQ1 4s ease-in-out infinite">“Hola, soy… y hoy os quiero contar…”</span>
    <span style="position: absolute; left: 24px; right: 24px; top: 50px; font-size: 34px; font-weight: 700; color: #F2EDE7; opacity: 0; animation: aQ2 4s ease-in-out infinite">“Este error arruina tus <span style="color:#FFB27A">fotos de perfil</span>.”</span>
  </div>
  <div style="position: absolute; left: 44px; right: 44px; top: 214px; height: 18px">{ticks}</div>
  <div style="position: absolute; left: 44px; top: 240px; {MONO}; font-size: 16px; letter-spacing: .1em; color: #9C938B">SEG. 0</div>
  <div style="position: absolute; left: 44px; right: 44px; top: 272px; height: 96px">
    <div style="{blk}; background: rgba(242,237,231,.08); border: 2px solid rgba(242,237,231,.18); color: #B5ADA4; animation: aA 4s cubic-bezier(.65,0,.35,1) infinite">SALUDO</div>
    <div style="{blk}; left: 33%; background: rgba(242,237,231,.08); border: 2px solid rgba(242,237,231,.18); color: #B5ADA4; animation: aB 4s cubic-bezier(.65,0,.35,1) infinite">CONTEXTO</div>
    <div style="{blk}; left: 66%; background: linear-gradient(135deg,#FF6A1A,#FFB27A); color: #0A0908; box-shadow: 0 0 40px rgba(255,106,26,.7); z-index: 2; animation: aRes 4s cubic-bezier(.65,0,.35,1) infinite"><span style="animation: aLift 4s ease-in-out infinite; display:block">★ RESULTADO</span></div>
    <div style="position: absolute; top: -20px; bottom: -20px; width: 4px; border-radius: 4px; background: #F2EDE7; box-shadow: 0 0 18px rgba(242,237,231,.9); z-index: 3; animation: aHead 4s linear infinite"></div>
  </div>
  <div style="position: absolute; left: 44px; bottom: 30px; height: 56px; width: 700px">
    <span style="{BADGE_BAD}; animation: aBad 4s ease-in-out infinite">✕ LO BUENO, AL FINAL</span>
    <span style="{BADGE_GOOD}; opacity: 0; animation: aGood 4s ease-in-out infinite">✓ LO BUENO, PRIMERO</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · El final primero', 2, kf2, body2,
    'Tu mejor frase va la primera. No la última.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 MOVIMIENTO
kf3 = """
@keyframes aShot{0%,8%{transform:scale(1) translateX(0)}14%,34%{transform:scale(1.35) translateX(0)}40%,64%{transform:scale(1.35) translateX(0)}68%,94%{transform:scale(1.1) translateX(-120px)}100%{transform:scale(1) translateX(0)}}
@keyframes aObj{0%,36%{transform:translate(260px,120px) rotate(18deg);opacity:0}44%,64%{transform:translate(0,0) rotate(-6deg);opacity:1}68%,100%{transform:translate(0,0) rotate(-6deg);opacity:0}}
@keyframes aFlash{0%,65%{opacity:0}67%{opacity:.85}72%,100%{opacity:0}}
@keyframes aC1{0%,6%{background:rgba(242,237,231,.06);color:#9C938B;border-color:rgba(242,237,231,.18)}10%,34%{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A}38%,100%{background:rgba(242,237,231,.06);color:#9C938B;border-color:rgba(242,237,231,.18)}}
@keyframes aC2{0%,36%{background:rgba(242,237,231,.06);color:#9C938B;border-color:rgba(242,237,231,.18)}42%,64%{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A}68%,100%{background:rgba(242,237,231,.06);color:#9C938B;border-color:rgba(242,237,231,.18)}}
@keyframes aC3{0%,64%{background:rgba(242,237,231,.06);color:#9C938B;border-color:rgba(242,237,231,.18)}68%,94%{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A}100%{background:rgba(242,237,231,.06);color:#9C938B;border-color:rgba(242,237,231,.18)}}
@keyframes aTL{0%{width:0}100%{width:100%}}
@keyframes aFoc{0%,100%{transform:scale(1);opacity:.9}50%{transform:scale(1.08);opacity:.6}}
"""
corner = lambda pos: f'<div style="position: absolute; {pos}; width: 46px; height: 46px; border-color: #F2EDE7; border-style: solid; border-width: 0"></div>'
chip = lambda t, a: f'<span style="flex: 1; text-align: center; padding: 14px 8px; border-radius: 14px; border: 2px solid rgba(242,237,231,.18); {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .06em; animation: {a} 4s ease-in-out infinite">{t}</span>'
body3 = num_head('02', 'MOVIMIENTO AL SEGUNDO 1',
    f'Que algo cambie<br><span style="{IT}">nada más empezar.</span>',
    'Un zoom, un objeto a cámara, un cambio de plano. <b style="color: #F2EDE7">Lo quieto se pasa.</b>') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 44px; right: 44px; top: 30px; height: 310px; border-radius: 18px; overflow: hidden; background: radial-gradient(ellipse at 50% 30%, #3A2A20, #171412 75%)">
    <div style="position: absolute; inset: 0; transform-origin: 50% 35%; animation: aShot 4s cubic-bezier(.65,0,.35,1) infinite">
      <svg width="360" height="300" viewBox="0 0 360 300" style="position: absolute; left: 50%; margin-left: -180px; bottom: -10px"><g fill="rgba(242,237,231,.9)"><ellipse cx="180" cy="110" rx="52" ry="62"/><path d="M70 310 C70 210 120 180 180 180 C240 180 290 210 290 310 Z"/></g><circle cx="200" cy="100" r="6" fill="#0A0908"/><circle cx="162" cy="100" r="6" fill="#0A0908"/></svg>
    </div>
    <div style="position: absolute; left: 520px; top: 110px; width: 150px; height: 150px; border-radius: 22px; background: linear-gradient(135deg,#FF6A1A,#FFB27A); box-shadow: 0 20px 50px rgba(0,0,0,.6), 0 0 40px rgba(255,106,26,.6); display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 18px; color: #0A0908; text-align: center; opacity: 0; animation: aObj 4s cubic-bezier(.3,1.4,.5,1) infinite">TU<br>PRODUCTO</div>
    <div style="position: absolute; inset: 0; background: #F2EDE7; opacity: 0; animation: aFlash 4s linear infinite"></div>
    <div style="position: absolute; inset: 22px">
      <div style="position: absolute; left: 0; top: 0; width: 46px; height: 46px; border-left: 4px solid #F2EDE7; border-top: 4px solid #F2EDE7"></div>
      <div style="position: absolute; right: 0; top: 0; width: 46px; height: 46px; border-right: 4px solid #F2EDE7; border-top: 4px solid #F2EDE7"></div>
      <div style="position: absolute; left: 0; bottom: 0; width: 46px; height: 46px; border-left: 4px solid #F2EDE7; border-bottom: 4px solid #F2EDE7"></div>
      <div style="position: absolute; right: 0; bottom: 0; width: 46px; height: 46px; border-right: 4px solid #F2EDE7; border-bottom: 4px solid #F2EDE7"></div>
      
      <div style="position: absolute; left: 20px; top: 14px; display: flex; align-items: center; gap: 10px; {MONO}; font-size: 18px; letter-spacing: .1em"><span style="width: 14px; height: 14px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30; animation: aRec 1s steps(1) infinite"></span>REC</div>
      <div style="position: absolute; right: 20px; top: 14px; {MONO}; font-size: 18px; letter-spacing: .1em; color: #B5ADA4">4K · 25P</div>
    </div>
    <div style="position: absolute; left: 0; bottom: 0; height: 6px; background: #FF6A1A; box-shadow: 0 0 14px rgba(255,106,26,.9); animation: aTL 4s linear infinite"></div>
  </div>
  <div style="position: absolute; left: 44px; right: 44px; bottom: 34px; display: flex; gap: 14px">
    {chip('ZOOM', 'aC1')}{chip('OBJETO A CÁMARA', 'aC2')}{chip('CAMBIO DE PLANO', 'aC3')}
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Movimiento', 3, kf3, body3,
    'Lo quieto se pasa. Lo que se mueve, se mira.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 GANCHO EN TEXTO
kf4 = """
@keyframes aL1{0%,4%{clip-path:inset(0 100% 0 0)}22%,92%{clip-path:inset(0 0 0 0)}100%{clip-path:inset(0 100% 0 0)}}
@keyframes aL2{0%,22%{clip-path:inset(0 100% 0 0)}40%,92%{clip-path:inset(0 0 0 0)}100%{clip-path:inset(0 100% 0 0)}}
@keyframes aMute{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
@keyframes aF1{0%,2%{border-color:rgba(242,237,231,.12);background:#171412}6%,30%{border-color:#FF6A1A;background:#2A150A}34%,100%{border-color:rgba(242,237,231,.12);background:#171412}}
@keyframes aF2{0%,34%{border-color:rgba(242,237,231,.12);background:#171412}38%,62%{border-color:#FF6A1A;background:#2A150A}66%,100%{border-color:rgba(242,237,231,.12);background:#171412}}
@keyframes aF3{0%,66%{border-color:rgba(242,237,231,.12);background:#171412}70%,96%{border-color:#FF6A1A;background:#2A150A}100%{border-color:rgba(242,237,231,.12);background:#171412}}
@keyframes aCaret{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes aBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
"""
forms = [('Deja de ___ si quieres ___', 'aF1'), ('El error que todos cometen al ___', 'aF2'), ('Nadie te cuenta esto de ___', 'aF3')]
fcards = ''.join(f'<div style="border-radius: 18px; border: 2px solid rgba(242,237,231,.12); padding: 20px 22px; animation: {a} 4s ease-in-out infinite"><span style="display:block; {MONO}; font-size: 15px; letter-spacing: .12em; color: #FFB27A; margin-bottom: 8px">FÓRMULA {i+1}</span><span style="font-size: 26px; font-weight: 600; line-height: 1.15">{t}</span></div>' for i, (t, a) in enumerate(forms))
body4 = num_head('03', 'GANCHO TAMBIÉN EN TEXTO',
    f'Escríbelo en pantalla.<br><span style="{IT}">Muchos lo ven sin sonido.</span>',
    'La primera frase, en <b style="color: #F2EDE7">texto grande</b> desde el primer fotograma.') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden; display: flex; align-items: center; gap: 36px; padding: 0 40px; box-sizing: border-box">
  <div style="flex: none; position: relative; width: 320px; height: 420px; border-radius: 36px; background: linear-gradient(180deg,#3A2A20,#171412); border: 3px solid rgba(242,237,231,.3); overflow: hidden">
    <svg width="280" height="280" viewBox="0 0 300 300" style="position: absolute; left: 20px; bottom: 0; animation: aBob 2s ease-in-out infinite"><g fill="rgba(242,237,231,.85)"><ellipse cx="150" cy="120" rx="46" ry="54"/><path d="M60 310 C60 210 100 180 150 180 C200 180 240 210 240 310 Z"/></g></svg>
    <div style="position: absolute; left: 10px; right: 10px; top: 64px; display: flex; flex-direction: column; align-items: center; gap: 8px">
      <span style="padding: 6px 12px; border-radius: 10px; background: #F2EDE7; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 25px; letter-spacing: -0.02em; white-space: nowrap; animation: aL1 4s steps(12) infinite">DEJA DE GRABARTE</span>
      <span style="padding: 6px 12px; border-radius: 10px; background: #FF6A1A; color: #0A0908; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 25px; letter-spacing: -0.02em; white-space: nowrap; animation: aL2 4s steps(12) infinite">CON LA LUZ DEL TECHO</span>
    </div>
    <div style="position: absolute; right: 16px; bottom: 16px; width: 48px; height: 48px; border-radius: 999px; background: rgba(10,9,8,.75); display: flex; align-items: center; justify-content: center; animation: aMute 1.4s ease-in-out infinite"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#F2EDE7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M23 9l-6 6M17 9l6 6"/></svg></div>
  </div>
  <div style="flex: 1; display: flex; flex-direction: column; gap: 16px">{fcards}</div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Gancho en texto', 4, kf4, body4,
    'Guárdalo y usa estas fórmulas en tu próximo vídeo.', DESLIZA_TXT))

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
labels = ['GANCHOS', 'LUZ', 'SONIDO', 'ENCUADRE', 'GUION', 'EDICIÓN']
def tile(i):
    wb = ''.join(f'<div style="width: 6px; height: {h}px; border-radius: 3px; background: #F2EDE7; animation: aTB 1s ease-in-out {-(i+j)*0.17:.2f}s infinite"></div>' for j, h in enumerate([14, 30, 22, 38, 18]))
    return f'<div style="position: relative; aspect-ratio: 1/1; border-radius: 12px; background: linear-gradient(160deg, #2A150A, #171412); border: 1px solid rgba(242,237,231,.1); animation: aTile 4s ease-in-out {i*0.4:.1f}s infinite; display: flex; align-items: center; justify-content: center; gap: 5px"><span style="position: absolute; top: 10px; left: 12px; font-family: \'JetBrains Mono\', monospace; font-size: 14px; color: #FFB27A">{labels[i]}</span>{wb}</div>'
tiles = ''.join(tile(i) for i in range(6))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 76px; line-height: 1; letter-spacing: -0.045em">Engancha en el <span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">segundo 1</span>.<br>Lo demás viene solo.</p>
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
