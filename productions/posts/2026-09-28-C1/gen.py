#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C1 (encuadre a cámara) en src/."""
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
# ---------------------------------------------------------------- 01 GANCHO
kf1 = """
@keyframes aPerson{0%,14%{transform:translateX(-190px) scale(.6)}34%,82%{transform:translateX(0) scale(1.08)}96%,100%{transform:translateX(-190px) scale(.6)}}
@keyframes aBad{0%,16%{opacity:1;transform:scale(1)}26%,88%{opacity:0;transform:scale(.8)}96%,100%{opacity:1;transform:scale(1)}}
@keyframes aGood{0%,22%{opacity:0;transform:scale(.8)}32%,84%{opacity:1;transform:scale(1)}94%,100%{opacity:0;transform:scale(.8)}}
@keyframes aEye{0%,22%{opacity:.15}34%,82%{opacity:1}94%,100%{opacity:.15}}
@keyframes aFrame{0%,14%{inset:22px}34%,82%{inset:12px}96%,100%{inset:22px}}
@keyframes aFocus{0%,24%{border-color:rgba(242,237,231,.35)}34%,82%{border-color:#FF6A1A}94%,100%{border-color:rgba(242,237,231,.35)}}
"""
body1 = f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 22px">
<span style="align-self: flex-start; padding: 10px 18px; border-radius: 999px; background: #FF6A1A; color: #0A0908; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 20px; letter-spacing: 0.1em">GUÁRDALO ANTES DE GRABAR</span>
<h1 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 112px; line-height: 0.92; letter-spacing: -0.055em">No es tu cámara.<br><span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">Es tu encuadre.</span></h1>
</div>

<div style="position: relative; height: 520px; border-radius: 34px; overflow: hidden; background: radial-gradient(ellipse at 50% 30%, #2A150A, #12100F 70%); border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
  <div style="position: absolute; top: 0; left: 0; right: 0; height: 60px; background: linear-gradient(180deg, rgba(255,106,26,0), rgba(255,106,26,0.10), rgba(255,106,26,0)); animation: aScan 4s linear infinite"></div>
  <div style="position: absolute; left: 33.33%; top: 0; bottom: 0; width: 1px; background: rgba(242,237,231,0.16)"></div>
  <div style="position: absolute; left: 66.66%; top: 0; bottom: 0; width: 1px; background: rgba(242,237,231,0.16)"></div>
  <div style="position: absolute; top: 66.66%; left: 0; right: 0; height: 1px; background: rgba(242,237,231,0.16)"></div>
  <div style="position: absolute; top: 33.33%; left: 0; right: 0; height: 2px; background: #FF6A1A; box-shadow: 0 0 22px rgba(255,106,26,0.9); animation: aEye 4s ease-in-out infinite"></div>
  <span style="position: absolute; top: calc(33.33% - 40px); right: 30px; font-family: 'JetBrains Mono', monospace; font-size: 18px; letter-spacing: 0.12em; color: #FFB27A; animation: aEye 4s ease-in-out infinite">OJOS AQUÍ</span>
  <div style="position: absolute; left: 50%; bottom: -8px; margin-left: -210px; width: 420px; height: 420px; transform-origin: 50% 100%; animation: aPerson 4s cubic-bezier(.65,0,.35,1) infinite">{PERSON}
    <div style="position: absolute; left: 88px; top: 20px; width: 244px; height: 230px; border: 3px solid rgba(242,237,231,.35); border-radius: 18px; animation: aFocus 4s ease-in-out infinite"></div>
  </div>
  <div style="position: absolute; border-radius: 22px; animation: aFrame 4s cubic-bezier(.65,0,.35,1) infinite; inset: 22px">
    <div style="position:absolute;top:0;left:0;width:54px;height:54px;border-top:4px solid #F2EDE7;border-left:4px solid #F2EDE7;border-radius:18px 0 0 0"></div>
    <div style="position:absolute;top:0;right:0;width:54px;height:54px;border-top:4px solid #F2EDE7;border-right:4px solid #F2EDE7;border-radius:0 18px 0 0"></div>
    <div style="position:absolute;bottom:0;left:0;width:54px;height:54px;border-bottom:4px solid #F2EDE7;border-left:4px solid #F2EDE7;border-radius:0 0 0 18px"></div>
    <div style="position:absolute;bottom:0;right:0;width:54px;height:54px;border-bottom:4px solid #F2EDE7;border-right:4px solid #F2EDE7;border-radius:0 0 18px 0"></div>
  </div>
  <div style="position: absolute; top: 34px; left: 42px; display: flex; align-items: center; gap: 12px; font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.1em"><span style="width: 16px; height: 16px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 14px #FF3B30; animation: aRec 1s steps(1) infinite"></span>REC</div>
  <span style="position: absolute; top: 34px; right: 42px; font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.1em; color: #B5ADA4">16:9 · PLANO MEDIO</span>
  <div style="position: absolute; bottom: 34px; left: 42px; height: 58px">
    <span style="position: absolute; left: 0; bottom: 0; white-space: nowrap; padding: 12px 22px; border-radius: 14px; background: rgba(10,9,8,.85); border: 2px solid #FF3B30; color: #FF6B61; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 22px; letter-spacing: 0.1em; animation: aBad 4s ease-in-out infinite">✕ AMATEUR</span>
    <span style="position: absolute; left: 0; bottom: 0; white-space: nowrap; padding: 12px 22px; border-radius: 14px; background: #FF6A1A; color: #0A0908; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 22px; letter-spacing: 0.1em; animation: aGood 4s ease-in-out infinite">✓ PROFESIONAL</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Misma cámara, misma persona. Solo cambia el encuadre.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 AIRE SOBRE LA CABEZA
kf2 = """
@keyframes aArrow{0%,100%{height:250px}50%{height:268px}}
@keyframes aPush{0%{transform:scale(1.02)}50%{transform:scale(1.08)}100%{transform:scale(1.02)}}
@keyframes aLine{0%,100%{opacity:.55}50%{opacity:1}}
@keyframes aWarn{0%,100%{opacity:1}50%{opacity:.35}}
"""
PHONE = lambda label, lc, inner, border: f"""
<div style="display: flex; flex-direction: column; align-items: center; gap: 16px">
<span style="font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.14em; color: {lc}">{label}</span>
<div style="position: relative; width: 250px; height: 444px; border-radius: 36px; background: #171412; border: 3px solid {border}; padding: 10px; box-sizing: border-box">
<div style="position: relative; width: 100%; height: 100%; border-radius: 27px; overflow: hidden; background: radial-gradient(ellipse at 50% 40%, #2A150A, #12100F 75%)">{inner}</div>
</div></div>"""
bad_inner = f"""
<div style="position: absolute; left: 50%; bottom: -4px; margin-left: -210px; width: 420px; height: 420px; transform: scale(.42); transform-origin: 50% 100%">{PERSON}</div>
<div style="position: absolute; left: 50%; top: 14px; margin-left: -2px; width: 4px; background: #FF3B30; animation: aArrow 4s ease-in-out infinite; height: 250px">
  <div style="position:absolute;top:-2px;left:-10px;width:24px;height:4px;background:#FF3B30"></div>
  <div style="position:absolute;bottom:-2px;left:-10px;width:24px;height:4px;background:#FF3B30"></div>
</div>
<span style="position: absolute; top: 110px; left: 14px; padding: 6px 10px; border-radius: 8px; background: rgba(10,9,8,.85); color: #FF6B61; font-family: 'JetBrains Mono', monospace; font-size: 15px; letter-spacing: .08em; animation: aWarn 4s ease-in-out infinite">AIRE VACÍO</span>
"""
good_inner = f"""
<div style="position: absolute; inset: 0; animation: aPush 4s ease-in-out infinite; transform-origin: 50% 35%">
<div style="position: absolute; left: 50%; bottom: -29px; margin-left: -210px; width: 420px; height: 520px; transform: scale(.78); transform-origin: 50% 100%">{PERSON_TALL}</div>
</div>
<div style="position: absolute; top: 33.33%; left: 0; right: 0; height: 2px; background: #FF6A1A; box-shadow: 0 0 16px rgba(255,106,26,.9); animation: aLine 4s ease-in-out infinite"></div>
<span style="position: absolute; top: calc(33.33% - 32px); right: 12px; font-family: 'JetBrains Mono', monospace; font-size: 15px; letter-spacing: .08em; color: #FFB27A">1/3</span>
"""
body2 = f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 30px">
<div style="display: flex; align-items: flex-end; gap: 28px">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 170px; line-height: 0.78; letter-spacing: -0.07em; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">01</span>
<span style="margin-bottom: 8px; padding: 10px 18px; border-radius: 999px; border: 1px solid rgba(242,237,231,0.2); font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.1em; color: #B5ADA4">ERROR MÁS COMÚN</span>
</div>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 92px; line-height: 0.95; letter-spacing: -0.05em">Te sobra aire<br><span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">encima de la cabeza.</span></h2>
<p style="margin: 0; font-size: 36px; line-height: 1.25; color: #D9D1C8">Pon los <b style="color: #F2EDE7">ojos en el tercio superior</b> de la imagen. Lo de arriba, casi vacío.</p>
</div>
<div style="position: relative; display: flex; justify-content: center; align-items: center; gap: 70px">
{PHONE('✕ ASÍ NO', '#FF6B61', bad_inner, 'rgba(242,237,231,0.14)')}
<svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" style="margin-top: 40px; animation: aNudge 1.3333s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
{PHONE('✓ ASÍ SÍ', '#FFB27A', good_inner, '#FF6A1A')}
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Aire', 2, kf2, body2,
    'Vale para vertical y horizontal.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 ALTURA DE CÁMARA
kf3 = """
@keyframes aCam{0%,12%{transform:translateY(0)}40%,82%{transform:translateY(-94px)}96%,100%{transform:translateY(0)}}
@keyframes aPole{0%,12%{height:40px}40%,82%{height:134px}96%,100%{height:40px}}
@keyframes aSight{0%,12%{d:path('M312 300 L744 206')}40%,82%{d:path('M312 206 L744 206')}96%,100%{d:path('M312 300 L744 206')}}
@keyframes aDash{to{stroke-dashoffset:-48}}
@keyframes aBadT{0%,18%{opacity:1}30%,86%{opacity:0}96%,100%{opacity:1}}
@keyframes aGoodT{0%,26%{opacity:0}40%,84%{opacity:1}94%,100%{opacity:0}}
@keyframes aCone{0%,12%{transform:rotate(-20deg)}40%,82%{transform:rotate(0deg)}96%,100%{transform:rotate(-20deg)}}
"""
body3 = """
<div style="position: relative; display: flex; flex-direction: column; gap: 30px">
<div style="display: flex; align-items: flex-end; gap: 28px">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 170px; line-height: 0.78; letter-spacing: -0.07em; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">02</span>
<span style="margin-bottom: 8px; padding: 10px 18px; border-radius: 999px; border: 1px solid rgba(242,237,231,0.2); font-family: 'JetBrains Mono', monospace; font-size: 20px; letter-spacing: 0.1em; color: #B5ADA4">ALTURA DE CÁMARA</span>
</div>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 92px; line-height: 0.95; letter-spacing: -0.05em">La cámara,<br><span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">a la altura de tus ojos.</span></h2>
<p style="margin: 0; font-size: 36px; line-height: 1.25; color: #D9D1C8">Desde abajo: <b style="color: #F2EDE7">papada y techo</b>. Desde arriba: <b style="color: #F2EDE7">te hace pequeño</b>.</p>
</div>
<div style="position: relative; height: 500px; border-radius: 34px; background: #12100F; border: 1px solid rgba(242,237,231,0.1); overflow: hidden">
  <div style="position: absolute; left: 0; right: 0; bottom: 60px; height: 2px; background: rgba(242,237,231,0.18)"></div>
  <svg width="920" height="500" viewBox="0 0 920 500" style="position: absolute; inset: 0">
    <path d="M312 300 L744 206" stroke="#FF6A1A" stroke-width="4" stroke-dasharray="16 8" fill="none" style="animation: aSight 4s cubic-bezier(.65,0,.35,1) infinite, aDash 1s linear infinite; filter: drop-shadow(0 0 8px rgba(255,106,26,.9))"/>
    <!-- persona de perfil -->
    <g fill="#F2EDE7" opacity=".9">
      <ellipse cx="780" cy="205" rx="52" ry="62"/>
      <path d="M740 262 C700 280 690 330 690 440 L870 440 C870 330 860 280 820 262 Z"/>
      <rect x="760" y="250" width="40" height="30" rx="12"/>
    </g>
    <circle cx="752" cy="206" r="7" fill="#0A0908"/>
  </svg>
  <!-- trípode + cámara -->
  <div style="position: absolute; left: 150px; bottom: 60px; width: 160px; height: 400px">
    <div style="position: absolute; bottom: 0; left: 30px; width: 100px; height: 70px">
      <div style="position:absolute;bottom:0;left:48px;width:4px;height:78px;background:#9C938B;transform-origin:50% 0;transform:translateY(-8px) rotate(28deg)"></div>
      <div style="position:absolute;bottom:0;left:48px;width:4px;height:78px;background:#9C938B;transform-origin:50% 0;transform:translateY(-8px) rotate(-28deg)"></div>
    </div>
    <div style="position: absolute; bottom: 62px; left: 76px; width: 8px; background: #B5ADA4; border-radius: 4px; animation: aPole 4s cubic-bezier(.65,0,.35,1) infinite; height: 40px"></div>
    <div style="position: absolute; left: 0; bottom: 100px; width: 160px; height: 96px; animation: aCam 4s cubic-bezier(.65,0,.35,1) infinite">
      <div style="position: absolute; left: 20px; top: 20px; width: 110px; height: 72px; border-radius: 14px; background: #1E1A17; border: 2px solid #F2EDE7"></div>
      <div style="position: absolute; left: 44px; top: 6px; width: 40px; height: 18px; border-radius: 6px 6px 0 0; background: #F2EDE7"></div>
      <div style="position: absolute; left: 124px; top: 32px; width: 36px; height: 48px; border-radius: 6px; background: #FF6A1A; box-shadow: 0 0 20px rgba(255,106,26,.8)"></div>
      <span style="position: absolute; left: 34px; top: 38px; width: 12px; height: 12px; border-radius: 99px; background: #FF3B30; animation: aRec 1s steps(1) infinite"></span>
    </div>
  </div>
  <div style="position: absolute; top: 30px; left: 36px; height: 56px; width: 600px">
    <span style="position: absolute; left: 0; top: 0; white-space: nowrap; padding: 12px 22px; border-radius: 14px; background: rgba(10,9,8,.85); border: 2px solid #FF3B30; color: #FF6B61; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 22px; letter-spacing: 0.1em; animation: aBadT 4s ease-in-out infinite">✕ DESDE ABAJO</span>
    <span style="position: absolute; left: 0; top: 0; white-space: nowrap; padding: 12px 22px; border-radius: 14px; background: #FF6A1A; color: #0A0908; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 22px; letter-spacing: 0.1em; animation: aGoodT 4s ease-in-out infinite">✓ A LA ALTURA DE LOS OJOS</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Altura', 3, kf3, body3,
    'Sin trípode: sube el móvil sobre libros.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 CHECKLIST
items = [
    ('Ojos en el tercio superior', 'Poco aire encima'),
    ('Cámara a la altura de los ojos', 'Ni desde abajo ni desde arriba'),
    ('Plano medio: de pecho para arriba', 'Se ven gestos y expresión'),
    ('Separado de la pared', 'Da profundidad y evita sombras'),
    ('Vertical 9:16 si va a Reels', 'Sin bandas negras'),
]
kf4 = ''
rows = ''
for i, (t, s) in enumerate(items):
    a = 6 + i * 13  # % en que se marca
    kf4 += (f"@keyframes aT{i}{{0%,{a}%{{background:rgba(242,237,231,0);border-color:rgba(242,237,231,.3)}}{a+4}%,90%{{background:#FF6A1A;border-color:#FF6A1A}}97%,100%{{background:rgba(242,237,231,0);border-color:rgba(242,237,231,.3)}}}}\n"
            f"@keyframes aK{i}{{0%,{a}%{{stroke-dashoffset:30}}{a+5}%,90%{{stroke-dashoffset:0}}97%,100%{{stroke-dashoffset:30}}}}\n"
            f"@keyframes aR{i}{{0%,{a}%{{border-color:rgba(242,237,231,.1)}}{a+4}%,90%{{border-color:rgba(255,106,26,.45)}}97%,100%{{border-color:rgba(242,237,231,.1)}}}}\n")
    rows += f"""<div style="display: flex; align-items: center; gap: 26px; padding: 22px 28px; border-radius: 22px; background: #12100F; border: 1px solid rgba(242,237,231,.1); animation: aR{i} 4s ease-in-out infinite">
<div style="flex: none; width: 52px; height: 52px; border-radius: 14px; border: 3px solid rgba(242,237,231,.3); display: flex; align-items: center; justify-content: center; box-sizing: border-box; animation: aT{i} 4s ease-in-out infinite"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5" stroke-dasharray="30" style="animation: aK{i} 4s ease-in-out infinite"></path></svg></div>
<div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 36px; font-weight: 700; letter-spacing: -0.01em">{t}</span><span style="font-size: 25px; color: #9C938B">{s}</span></div>
</div>"""
kf4 += """
@keyframes aRecOn{0%,70%{background:#1E1A17;box-shadow:none;color:#6B635C}76%,90%{background:#FF3B30;box-shadow:0 0 60px rgba(255,59,48,.8);color:#F2EDE7}97%,100%{background:#1E1A17;box-shadow:none;color:#6B635C}}
"""
body4 = f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 34px">
<div style="display: flex; align-items: flex-end; justify-content: space-between">
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 92px; line-height: 0.95; letter-spacing: -0.05em">Antes de<br>darle a <span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">REC:</span></h2>
<div style="width: 150px; height: 150px; border-radius: 999px; border: 4px solid rgba(242,237,231,.25); display: flex; align-items: center; justify-content: center; box-sizing: border-box">
<div style="width: 112px; height: 112px; border-radius: 999px; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 26px; letter-spacing: .08em; animation: aRecOn 4s ease-in-out infinite; background: #1E1A17">REC</div>
</div>
</div>
<div style="display: flex; flex-direction: column; gap: 16px">{rows}</div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Checklist', 4, kf4, body4,
    'Haz captura y úsala en tu próxima grabación.', DESLIZA_TXT))

# ---------------------------------------------------------------- 05 CTA
kf5 = """
@keyframes aBtn{0%,40%{background:#FF6A1A;color:#0A0908}48%,90%{background:#1E1A17;color:#F2EDE7}97%,100%{background:#FF6A1A;color:#0A0908}}
@keyframes aTxtA{0%,42%{opacity:1}46%,92%{opacity:0}97%,100%{opacity:1}}
@keyframes aTxtB{0%,42%{opacity:0}46%,92%{opacity:1}97%,100%{opacity:0}}
@keyframes aTap{0%,22%{transform:translate(120px,140px);opacity:0}32%{transform:translate(0,0);opacity:1}40%{transform:translate(0,0) scale(.85);opacity:1}48%{transform:translate(0,0) scale(1);opacity:1}62%,100%{transform:translate(90px,160px);opacity:0}}
@keyframes aRip{0%,39%{transform:scale(.2);opacity:0}42%{opacity:.9}60%,100%{transform:scale(2.4);opacity:0}}
@keyframes aTile{0%,100%{opacity:.55}50%{opacity:1}}
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
"""
tiles = ''.join(
    f'<div style="position: relative; aspect-ratio: 1/1; border-radius: 12px; background: linear-gradient(160deg, #2A150A, #171412); border: 1px solid rgba(242,237,231,.1); animation: aTile 4s ease-in-out {i*0.4:.1f}s infinite; display: flex; align-items: center; justify-content: center"><span style="position: absolute; top: 10px; left: 12px; font-family: \'JetBrains Mono\', monospace; font-size: 15px; color: #FFB27A">TIP {6-i:02d}</span><svg width="44" height="44" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(242,237,231,.12)"/><path d="M10 8l6 4-6 4z" fill="#F2EDE7"/></svg></div>'
    for i in range(6))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 84px; line-height: 1; letter-spacing: -0.045em">¿Te ha servido? <span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">Guárdalo.</span></p>
<div style="position: relative; margin-top: 40px; width: 600px; border-radius: 40px; background: #12100F; border: 2px solid rgba(242,237,231,0.12); padding: 34px 36px 30px; box-sizing: border-box; display: flex; flex-direction: column; gap: 24px; box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">
  <div style="display: flex; align-items: center; gap: 22px; text-align: left">
    <div style="flex: none; width: 104px; height: 104px; border-radius: 999px; padding: 4px; background: linear-gradient(135deg, #FF6A1A, #FFB27A); box-sizing: border-box"><div style="width: 100%; height: 100%; border-radius: 999px; background: #0A0908; display: flex; align-items: center; justify-content: center"><img src="{LOGO}" style="width: 62px; height: 62px"></div></div>
    <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 36px; letter-spacing: -0.02em">ceos.productions</span><span style="font-size: 24px; color: #9C938B">Estudio de grabación y foto · Burgos</span></div>
  </div>
  <div style="position: relative">
    <div style="position: relative; height: 72px; border-radius: 16px; font-weight: 700; font-size: 30px; animation: aBtn 4s ease-in-out infinite; background: #FF6A1A; color: #0A0908">
      <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; animation: aTxtA 4s ease-in-out infinite">Seguir</span>
      <span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; animation: aTxtB 4s ease-in-out infinite">Siguiendo ✓</span>
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
