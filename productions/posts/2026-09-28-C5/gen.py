#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C5 (edición con ritmo: 3 cortes) en src/."""
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


GRAD = "background: linear-gradient(135deg,#FF6A1A,#FFB27A)"
STRIPE = "background: repeating-linear-gradient(135deg, rgba(255,59,48,.55) 0 10px, rgba(255,59,48,.25) 10px 20px); border: 2px solid #FF3B30"

# ---------------------------------------------------------------- 01 GANCHO
kf1 = """
@keyframes aHead{0%{left:0%}100%{left:100%}}
@keyframes aWave{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}
@keyframes aGapFlash{0%,26%{box-shadow:none}30%,40%{box-shadow:0 0 30px rgba(255,59,48,.9)}}
@keyframes aSnip{0%,27%{opacity:0;transform:scale(.4) rotate(-30deg)}32%,42%{opacity:1;transform:scale(1.15) rotate(0)}48%,100%{opacity:0;transform:scale(.6)}}
@keyframes aTagA{0%,44%{opacity:1}50%,94%{opacity:0}100%{opacity:1}}
@keyframes aTagB{0%,44%{opacity:0}50%,94%{opacity:1}100%{opacity:0}}
@keyframes aDur{0%,42%{width:100%}58%,90%{width:66%}98%,100%{width:100%}}
@keyframes aSpeak{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
@keyframes aSub{0%,14%{opacity:1}15%,29%{opacity:0}30%,100%{opacity:1}}
@keyframes aSub2{0%,14%{opacity:0}15%,29%{opacity:1}30%,100%{opacity:0}}
"""
segs = [('H', 84), ('SILENCIO', 72), ('H', 96), ('EHHH', 56), ('H', 104), ('REPITO', 70), ('H', 88), ('PAUSA', 58), ('H', 84)]
def seg1(i, lab, w):
    if lab == 'H':
        return f'<div style="flex: none; width: {w}px; height: 100%; border-radius: 10px; {GRAD}; box-shadow: 0 0 20px rgba(255,106,26,.45)"></div>'
    kfn = f'aG{i}'
    return f'<div style="flex: none; width: {w}px; height: 100%; border-radius: 10px; {STRIPE}; box-sizing: border-box; overflow: hidden; display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 13px; letter-spacing: .06em; color: #FFD2CE; animation: {kfn} 4s cubic-bezier(.6,0,.3,1) infinite, aGapFlash 4s linear infinite">{lab}</div>'
kf1 += ''.join(f'@keyframes aG{i}{{0%,44%{{width:{w}px;opacity:1;margin:0}}58%,90%{{width:0px;opacity:0;margin:0 -3px}}98%,100%{{width:{w}px;opacity:1;margin:0}}}}\n' for i, (l, w) in enumerate(segs) if l != 'H')
track1 = ''.join(seg1(i, l, w) for i, (l, w) in enumerate(segs))
snips = ''.join(f'<div style="position:absolute; top: -48px; left: {x}px; color: #FF6B61; font-size: 34px; opacity: 0; animation: aSnip 4s ease-out {d}s infinite">✂</div>' for x, d in [(109, 0), (281, .05), (460, .1), (624, .15)])
wave1 = ''.join(f'<div style="flex:1; height: 100%; border-radius: 3px; background: rgba(242,237,231,.55); animation: aWave 1s ease-in-out {-(i*0.13)%1:.2f}s infinite"></div>' for i, in [(k,) for k in range(40)])
body1 = f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 22px">
<span style="align-self: flex-start; padding: 10px 18px; border-radius: 999px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: 0.1em">EL SECRETO DEL RITMO</span>
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 96px; line-height: 0.95; letter-spacing: -0.055em">Tu vídeo no es largo.<br><span style="{IT}; animation: aHeat 4s ease-in-out infinite">Tiene huecos.</span></h1>
</div>

<div style="position: relative; height: 600px; border-radius: 34px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
  <div style="position: absolute; left: 40px; right: 40px; top: 32px; height: 300px; border-radius: 20px; overflow: hidden; background: #0A0908">
    <div style="position:absolute; inset:0; animation: aSpeak 1s ease-in-out infinite">{scene_talk()}</div>
    {VF}
    <div style="position: absolute; left: 0; right: 0; bottom: 26px; display: flex; justify-content: center">
      <span style="position: absolute; bottom: 0; padding: 10px 22px; border-radius: 12px; background: rgba(10,9,8,.85); font-weight: 700; font-size: 28px; animation: aSub 4s steps(1) infinite">“Hoy te enseño…”</span>
      <span style="position: absolute; bottom: 0; padding: 10px 22px; border-radius: 12px; background: rgba(10,9,8,.85); font-weight: 700; font-size: 28px; color: #FF6B61; opacity: 0; animation: aSub2 4s steps(1) infinite">“eeeh…”</span>
    </div>
    <div style="position: absolute; right: 70px; top: 30px; {MONO}; font-size: 18px; letter-spacing: .1em; width: 400px; height: 24px">
      <span style="position:absolute; right:0; white-space:nowrap; color:#FF6B61; animation: aTagA 4s linear infinite">ANTES · CON HUECOS</span>
      <span style="position:absolute; right:0; white-space:nowrap; color:#FFB27A; opacity:0; animation: aTagB 4s linear infinite">DESPUÉS · SOLO LO QUE APORTA</span>
    </div>
  </div>
  <div style="position: absolute; left: 40px; right: 40px; top: 382px; height: 190px">
    <span style="position: absolute; left: 0; top: 18px; {MONO}; font-size: 16px; letter-spacing: .1em; color: #FFB27A">V1</span>
    <span style="position: absolute; left: 0; top: 90px; {MONO}; font-size: 16px; letter-spacing: .1em; color: #9C938B">A1</span>
    <span style="position: absolute; left: 0; top: 150px; {MONO}; font-size: 14px; letter-spacing: .1em; color: #9C938B">DUR.</span>
    <div style="position: absolute; left: 60px; right: 0; top: 0; height: 190px">
      <div style="position: absolute; left: 0; right: 0; top: 0; height: 56px; display: flex; gap: 6px">{track1}</div>
      {snips}
      <div style="position: absolute; left: 0; right: 0; top: 74px; height: 46px; border-radius: 10px; background: rgba(242,237,231,.06); display: flex; gap: 4px; padding: 6px 12px; box-sizing: border-box">{wave1}</div>
      <div style="position: absolute; left: 0; right: 0; top: 146px; height: 22px; border-radius: 99px; background: rgba(242,237,231,.08); overflow: hidden"><div style="height: 100%; border-radius: 99px; {GRAD}; animation: aDur 4s cubic-bezier(.6,0,.3,1) infinite"></div></div>
      <div style="position: absolute; top: -10px; height: 136px; width: 4px; border-radius: 4px; background: #F2EDE7; box-shadow: 0 0 18px rgba(242,237,231,.9); animation: aHead 4s linear infinite"></div>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    '3 cortes para que no se vayan a mitad.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 CORTE 1: MULETILLAS
kf2 = SWAP_KF + """
@keyframes aCaret{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes aLab{0%,100%{opacity:.7}50%{opacity:1}}
"""
words = [('Eeeh…', 1), ('hola.', 1), ('Bueno,', 1), ('pues', 1), ('hoy…', 1), ('hoy', 0), ('te', 0), ('enseño', 0), ('tres', 0), ('trucos', 0), ('para,', 0), ('eh,', 1), ('grabarte', 0), ('mejor.', 0)]
toks = []
k = 0
for w, bad in words:
    if bad:
        t0 = 14 + k * 6; k += 1
        kf2 += f'@keyframes aK{k}{{0%,{t0}%{{max-width:220px;color:#F2EDE7;background:transparent;text-decoration-color:transparent;margin-right:14px;padding:0 6px}}{t0+4}%,56%{{max-width:220px;opacity:1;color:#FF6B61;background:rgba(255,59,48,.16);text-decoration-color:#FF3B30;margin-right:14px;padding:0 6px}}66%,90%{{max-width:0;opacity:0;color:#FF6B61;background:rgba(255,59,48,0);margin-right:0;padding:0}}97%,100%{{max-width:220px;color:#F2EDE7;background:transparent;text-decoration-color:transparent;margin-right:14px;padding:0 6px}}}}\n'
        toks.append(f'<span style="display: inline-block; vertical-align: top; overflow: hidden; white-space: nowrap; max-width: 220px; margin-right: 14px; padding: 0 6px; border-radius: 8px; text-decoration: line-through; text-decoration-thickness: 5px; text-decoration-color: transparent; animation: aK{k} 4s cubic-bezier(.6,0,.3,1) infinite">{w}</span>')
    else:
        toks.append(f'<span style="display: inline-block; vertical-align: top; margin-right: 14px; padding: 0 6px; color: #F2EDE7">{w}</span>')
body2 = num_head('01', 'CORTE 1 · MULETILLAS',
    f'Corta cada<br><span style="{IT}">“eeeh…”</span>',
    'Silencios, muletillas y frases repetidas. <b style="color: #F2EDE7">Fuera todo lo que no aporta.</b>') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 44px; right: 44px; top: 34px; display: flex; align-items: center; justify-content: space-between">
    <span style="{MONO}; font-size: 18px; letter-spacing: .12em; color: #9C938B">TRANSCRIPCIÓN · EDITOR</span>
    <span style="{MONO}; font-size: 16px; letter-spacing: .1em; color: #FFB27A; padding: 6px 14px; border: 1px solid rgba(255,178,122,.4); border-radius: 99px; animation: aLab 2s ease-in-out infinite">EJEMPLO</span>
  </div>
  <div style="position: absolute; left: 44px; right: 44px; top: 90px; height: 250px; border-radius: 20px; background: #0A0908; border: 1px solid rgba(242,237,231,.12); padding: 30px 30px; box-sizing: border-box; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 700; font-size: 46px; line-height: 1.35; letter-spacing: -0.02em">{''.join(toks)}<span style="display: inline-block; width: 4px; height: 48px; background: #FF6A1A; vertical-align: middle; animation: aCaret 1s steps(1) infinite"></span></div>
  <div style="position: absolute; left: 44px; bottom: 40px; height: 56px; width: 900px">
    <span style="{BADGE_BAD}; animation: aBad 4s ease-in-out infinite">✕ 5 HUECOS ANTES DE LA IDEA</span>
    <span style="{BADGE_GOOD}; opacity: 0; animation: aGood 4s ease-in-out infinite">✓ DIRECTO AL GRANO</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Corte 1', 2, kf2, body2,
    'Cada pausa es una excusa para hacer scroll.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 CORTE 2: ENTRA TARDE, SAL PRONTO
kf3 = """
@keyframes aHL{0%,20%{left:0%}42%,88%{left:30%}96%,100%{left:0%}}
@keyframes aHR{0%,20%{right:0%}42%,88%{right:22%}96%,100%{right:0%}}
@keyframes aDimL{0%,24%{opacity:1;filter:none}40%,88%{opacity:.35;filter:grayscale(1)}96%,100%{opacity:1;filter:none}}
@keyframes aXo{0%,30%{opacity:0;transform:scale(.5)}40%,88%{opacity:1;transform:scale(1)}96%,100%{opacity:0}}
@keyframes aFA{0%,44%{opacity:1}50%,92%{opacity:0}98%,100%{opacity:1}}
@keyframes aFB{0%,44%{opacity:0}50%,92%{opacity:1}98%,100%{opacity:0}}
@keyframes aGlowK{0%,40%{box-shadow:none}50%,88%{box-shadow:0 0 40px rgba(255,106,26,.7)}}
@keyframes aHead{0%{left:0%}100%{left:100%}}
"""
HANDLE = "position: absolute; top: -14px; bottom: -14px; width: 20px; border-radius: 8px; background: #F2EDE7; box-shadow: 0 0 22px rgba(242,237,231,.8)"
body3 = num_head('02', 'CORTE 2 · ENTRA TARDE',
    f'Empieza en la<br><span style="{IT}">primera frase útil.</span>',
    'Fuera el “hola, ¿qué tal?” y el “bueno, pues eso”. <b style="color: #F2EDE7">Entra tarde y sal pronto.</b>') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 44px; right: 44px; top: 34px; height: 170px; display: flex; gap: 26px; align-items: center">
    <div style="flex: none; position: relative; width: 300px; height: 170px; border-radius: 16px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,.18)">{scene_talk()}
      <span style="position: absolute; left: 12px; top: 10px; {MONO}; font-size: 14px; letter-spacing: .1em; color: #F2EDE7; background: rgba(10,9,8,.7); padding: 4px 8px; border-radius: 6px">SEGUNDO 0</span>
    </div>
    <div style="flex: 1; position: relative; height: 170px">
      <span style="{MONO}; font-size: 16px; letter-spacing: .12em; color: #9C938B">LO PRIMERO QUE OYEN</span>
      <p style="position: absolute; left: 0; right: 0; top: 36px; margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 44px; line-height: 1.05; letter-spacing: -0.03em; color: #FF6B61; animation: aFA 4s ease-in-out infinite">“Hola, ¿qué tal? Bueno, pues…”</p>
      <p style="position: absolute; left: 0; right: 0; top: 36px; margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 44px; line-height: 1.05; letter-spacing: -0.03em; color: #FFB27A; opacity: 0; animation: aFB 4s ease-in-out infinite">“El error que arruina tus vídeos.”</p>
    </div>
  </div>
  <div style="position: absolute; left: 44px; right: 44px; top: 250px; height: 110px">
    <div style="position: absolute; inset: 0; display: flex; border-radius: 14px; overflow: hidden; {MONO}; font-weight: 600; font-size: 15px; letter-spacing: .06em">
      <div style="width: 30%; {STRIPE}; box-sizing: border-box; display: flex; align-items: center; justify-content: center; text-align: center; color: #FFD2CE; animation: aDimL 4s ease-in-out infinite">HOLA, ¿QUÉ TAL?<br>BUENO, PUES…</div>
      <div style="width: 48%; {GRAD}; color: #0A0908; display: flex; align-items: center; justify-content: center; animation: aGlowK 4s ease-in-out infinite">LA IDEA</div>
      <div style="width: 22%; {STRIPE}; box-sizing: border-box; display: flex; align-items: center; justify-content: center; text-align: center; color: #FFD2CE; animation: aDimL 4s ease-in-out infinite">Y NADA,<br>ESO. ¡CHAO!</div>
    </div>
    <div style="{HANDLE}; animation: aHL 4s cubic-bezier(.6,0,.3,1) infinite"></div>
    <div style="{HANDLE}; animation: aHR 4s cubic-bezier(.6,0,.3,1) infinite"></div>
    <div style="position: absolute; left: 12%; top: 26px; font-size: 54px; color: #FF3B30; opacity: 0; animation: aXo 4s ease-out infinite">✕</div>
    <div style="position: absolute; right: 8%; top: 26px; font-size: 54px; color: #FF3B30; opacity: 0; animation: aXo 4s ease-out .1s infinite">✕</div>
  </div>
  <div style="position: absolute; left: 44px; right: 44px; bottom: 40px; display: flex; justify-content: space-between; {MONO}; font-size: 18px; letter-spacing: .1em; color: #9C938B">
    <span>✂ CORTA EL SALUDO</span><span style="color: #FFB27A">CONSERVA LA IDEA</span><span>✂ CORTA LA DESPEDIDA</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Corte 2', 3, kf3, body3,
    'Tu primera frase tiene que ser ya el tema.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 CORTE 3: ZOOM / CAMBIO DE PLANO
kf4 = """
@keyframes aPunch{0%,24.9%{transform:scale(1) translateY(0)}25%,49.9%{transform:scale(1.5) translateY(26px)}50%,74.9%{transform:scale(1) translateY(0)}75%,100%{transform:scale(1.5) translateY(26px)}}
@keyframes aFlash{0%,24%,26%,49%,51%,74%,76%,99%{opacity:0}25%,50%,75%,100%{opacity:.5}}
@keyframes aLA{0%,24.9%{opacity:1}25%,49.9%{opacity:0}50%,74.9%{opacity:1}75%,100%{opacity:0}}
@keyframes aLB{0%,24.9%{opacity:0}25%,49.9%{opacity:1}50%,74.9%{opacity:0}75%,100%{opacity:1}}
@keyframes aHead{0%{left:0%}100%{left:100%}}
@keyframes aB1{0%,24.9%{filter:brightness(1.35);transform:translateY(-4px)}25%,100%{filter:brightness(.55);transform:none}}
@keyframes aB2{0%,24.9%{filter:brightness(.55);transform:none}25%,49.9%{filter:brightness(1.35);transform:translateY(-4px)}50%,100%{filter:brightness(.55);transform:none}}
@keyframes aB3{0%,49.9%{filter:brightness(.55);transform:none}50%,74.9%{filter:brightness(1.35);transform:translateY(-4px)}75%,100%{filter:brightness(.55);transform:none}}
@keyframes aB4{0%,74.9%{filter:brightness(.55);transform:none}75%,100%{filter:brightness(1.35);transform:translateY(-4px)}}
@keyframes aFrame{0%,24.9%{inset:18px}25%,49.9%{inset:70px 120px}50%,74.9%{inset:18px}75%,100%{inset:70px 120px}}
"""
blocks = [('ABIERTO', 'aB1', 'rgba(242,237,231,.22)', '#F2EDE7'), ('ZOOM', 'aB2', '', '#0A0908'), ('ABIERTO', 'aB3', 'rgba(242,237,231,.22)', '#F2EDE7'), ('ZOOM', 'aB4', '', '#0A0908')]
blk = ''.join(f'<div style="flex: 1; height: 100%; border-radius: 10px; {("background:" + bg) if bg else GRAD}; color: {c}; display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 16px; letter-spacing: .08em; animation: {a} 4s steps(1) infinite">{t}</div>' for t, a, bg, c in blocks)
body4 = num_head('03', 'CORTE 3 · CAMBIA EL PLANO',
    f'Zoom en cada<br><span style="{IT}">cambio de frase.</span>',
    'Alterna plano abierto y cerrado sobre la misma toma. <b style="color: #F2EDE7">Parece que grabaste con dos cámaras.</b>') + f"""
<div style="position: relative; height: 470px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 44px; right: 44px; top: 30px; height: 300px; border-radius: 18px; overflow: hidden; background: #0A0908; border: 2px solid rgba(242,237,231,.18)">
    <div style="position: absolute; inset: 0; animation: aPunch 4s steps(1) infinite; transform-origin: 50% 40%">{scene_talk()}</div>
    <div style="position: absolute; inset: 0; background: #F2EDE7; opacity: 0; animation: aFlash 4s linear infinite"></div>
    {VF}
    <div style="position: absolute; right: 70px; top: 30px; {MONO}; font-size: 18px; letter-spacing: .1em; width: 400px; height: 24px">
      <span style="position:absolute; right:0; white-space:nowrap; color:#F2EDE7; animation: aLA 4s steps(1) infinite">PLANO ABIERTO</span>
      <span style="position:absolute; right:0; white-space:nowrap; color:#FFB27A; opacity:0; animation: aLB 4s steps(1) infinite">ZOOM · MISMA TOMA</span>
    </div>
  </div>
  <div style="position: absolute; left: 44px; right: 44px; top: 356px; height: 70px">
    <div style="position: absolute; inset: 0; display: flex; gap: 8px">{blk}</div>
    <div style="position: absolute; top: -10px; bottom: -10px; width: 4px; border-radius: 4px; background: #F2EDE7; box-shadow: 0 0 18px rgba(242,237,231,.9); animation: aHead 4s linear infinite"></div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Corte 3', 4, kf4, body4,
    'Una cámara, dos planos. Cero cortes feos.', DESLIZA_TXT))
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
labels = ['EDICIÓN', 'LUZ', 'SONIDO', 'ENCUADRE', 'GUION', 'B-ROLL']
def tile(i):
    wb = ''.join(f'<div style="width: 6px; height: {h}px; border-radius: 3px; background: #F2EDE7; animation: aTB 1s ease-in-out {-(i+j)*0.17:.2f}s infinite"></div>' for j, h in enumerate([14, 30, 22, 38, 18]))
    return f'<div style="position: relative; aspect-ratio: 1/1; border-radius: 12px; background: linear-gradient(160deg, #2A150A, #171412); border: 1px solid rgba(242,237,231,.1); animation: aTile 4s ease-in-out {i*0.4:.1f}s infinite; display: flex; align-items: center; justify-content: center; gap: 5px"><span style="position: absolute; top: 10px; left: 12px; font-family: \'JetBrains Mono\', monospace; font-size: 14px; color: #FFB27A">{labels[i]}</span>{wb}</div>'
tiles = ''.join(tile(i) for i in range(6))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 76px; line-height: 1; letter-spacing: -0.045em">Corta <span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">sin miedo</span>.<br>Y tu vídeo vuela.</p>
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
