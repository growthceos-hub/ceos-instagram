#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C1 2026-09-29 (guion para vídeo corto) en src/."""
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


# ---------------------------------------------------------------- 01 GANCHO
kf1 = """
@keyframes aStep{0%,24.9%{opacity:1}25%,100%{opacity:0}}
@keyframes aS1{0%,34%{opacity:1}35%,100%{opacity:0}}
@keyframes aS2{0%,34%{opacity:0}35%,69%{opacity:1}70%,100%{opacity:0}}
@keyframes aS3{0%,69%{opacity:0}70%,100%{opacity:1}}
@keyframes aBreath{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-6px) scale(1.012)}}
@keyframes aShake{0%,70%,100%{transform:translateX(0)}74%{transform:translateX(-5px)}78%{transform:translateX(5px)}82%{transform:translateX(-3px)}86%{transform:translateX(0)}}
@keyframes aCur{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes aAlert{0%,100%{box-shadow:0 0 0 0 rgba(255,59,48,.0);opacity:.75}50%{box-shadow:0 0 26px 2px rgba(255,59,48,.65);opacity:1}}
@keyframes aDot{0%,100%{opacity:.2;transform:translateY(0)}50%{opacity:1;transform:translateY(-8px)}}
@keyframes aLine{0%,100%{opacity:.35}50%{opacity:.6}}
@keyframes aFocus{0%,100%{transform:scale(1);opacity:.9}50%{transform:scale(1.04);opacity:.5}}
"""
timer = ''.join(
    f'<span style="position: absolute; right: 0; opacity: 0; animation: aStep 4s steps(1) {k-4}s infinite">00:00:0{k+1}</span>'
    for k in range(4))
lines1 = ''.join(
    f'<div style="height: 18px; width: {w}%; border-radius: 6px; border: 2px dashed rgba(242,237,231,.28); animation: aLine 2s ease-in-out {i*0.3:.1f}s infinite"></div>'
    for i, w in enumerate((88, 72, 80)))
body1 = headline('GUION PARA VÍDEO CORTO', 'Te quedas en blanco', 'porque grabas sin guion.', 90) + f"""
<div style="position: relative; height: 620px; border-radius: 34px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.55)">
  <div style="position: absolute; left: 36px; right: 36px; top: 32px; height: 352px; border-radius: 22px; overflow: hidden; background: #0A0908; animation: aShake 4s linear infinite">
    <div style="position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 35%, #2A150A, #0A0908 75%)"></div>
    <div style="position: absolute; left: 50%; bottom: -70px; margin-left: -190px; width: 380px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{PERSON.replace('width="420" height="420"', 'width="380" height="380"')}</div>
    <div style="position: absolute; left: 50%; top: 58px; margin-left: 110px; display: flex; gap: 10px">
      <span style="width: 16px; height: 16px; border-radius: 99px; background: #F2EDE7; animation: aDot 1.2s ease-in-out 0s infinite"></span>
      <span style="width: 16px; height: 16px; border-radius: 99px; background: #F2EDE7; animation: aDot 1.2s ease-in-out .2s infinite"></span>
      <span style="width: 16px; height: 16px; border-radius: 99px; background: #F2EDE7; animation: aDot 1.2s ease-in-out .4s infinite"></span>
    </div>
    <div style="position: absolute; inset: 18px; pointer-events: none">
      <div style="position: absolute; left: 0; top: 0; width: 40px; height: 40px; border-left: 4px solid #F2EDE7; border-top: 4px solid #F2EDE7"></div>
      <div style="position: absolute; right: 0; top: 0; width: 40px; height: 40px; border-right: 4px solid #F2EDE7; border-top: 4px solid #F2EDE7"></div>
      <div style="position: absolute; left: 0; bottom: 0; width: 40px; height: 40px; border-left: 4px solid #F2EDE7; border-bottom: 4px solid #F2EDE7"></div>
      <div style="position: absolute; right: 0; bottom: 0; width: 40px; height: 40px; border-right: 4px solid #F2EDE7; border-bottom: 4px solid #F2EDE7"></div>
      <div style="position: absolute; left: 50%; top: 50%; width: 110px; height: 80px; margin: -40px 0 0 -55px; border: 2px solid rgba(242,237,231,.5); border-radius: 6px; animation: aFocus 2s ease-in-out infinite"></div>
      <div style="position: absolute; left: 18px; top: 12px; display: flex; align-items: center; gap: 10px; {MONO}; font-size: 20px; letter-spacing: .1em; color: #F2EDE7"><span style="width: 14px; height: 14px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30; animation: aRec 1s steps(1) infinite"></span>REC</div>
      <div style="position: absolute; right: 18px; top: 12px; width: 150px; height: 26px; {MONO}; font-size: 20px; letter-spacing: .08em; color: #F2EDE7">{timer}</div>
    </div>
    <div style="position: absolute; left: 0; right: 0; bottom: 30px; display: flex; justify-content: center">
      <span style="position: absolute; bottom: 0; white-space: nowrap; padding: 12px 24px; border-radius: 14px; background: rgba(10,9,8,.88); font-weight: 700; font-size: 32px; animation: aS1 4s steps(1) infinite">“Hola, hoy os cuento…”</span>
      <span style="position: absolute; bottom: 0; white-space: nowrap; padding: 12px 24px; border-radius: 14px; background: rgba(10,9,8,.88); font-weight: 700; font-size: 32px; color: #FF6B61; opacity: 0; animation: aS2 4s steps(1) infinite">“eeeh…”</span>
      <span style="position: absolute; bottom: 0; white-space: nowrap; padding: 12px 24px; border-radius: 14px; background: rgba(10,9,8,.88); font-weight: 700; font-size: 32px; color: #FF6B61; opacity: 0; animation: aS3 4s steps(1) infinite">“¿por dónde iba?”</span>
    </div>
  </div>
  <div style="position: absolute; left: 36px; right: 36px; top: 408px; bottom: 30px; border-radius: 20px; background: #171412; border: 1px solid rgba(242,237,231,.1); padding: 22px 28px; box-sizing: border-box; display: flex; flex-direction: column; gap: 16px">
    <div style="display: flex; align-items: center; justify-content: space-between">
      <span style="{MONO}; font-size: 20px; letter-spacing: .08em; color: #B5ADA4">GUION_VIDEO.TXT</span>
      <span style="padding: 6px 14px; border-radius: 99px; border: 2px solid #FF3B30; color: #FF6B61; {MONO}; font-weight: 600; font-size: 17px; letter-spacing: .1em; animation: aAlert 1.6s ease-in-out infinite">0 PALABRAS</span>
    </div>
    <div style="display: flex; align-items: center; gap: 6px; height: 24px"><span style="width: 3px; height: 28px; background: #FF6A1A; animation: aCur 1s steps(1) infinite"></span></div>
    {lines1}
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'La estructura para no improvisar nunca más.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 FOLIO vs BLOQUES
kf2 = """
@keyframes aScroll{0%{transform:translateY(0)}100%{transform:translateY(-50%)}}
@keyframes aFolio{0%,38%{transform:scale(1);opacity:1;filter:none}52%,88%{transform:scale(.82);opacity:.28;filter:grayscale(1)}100%{transform:scale(1);opacity:1;filter:none}}
@keyframes aStamp{0%,40%{opacity:0;transform:rotate(-12deg) scale(1.6)}48%,88%{opacity:1;transform:rotate(-12deg) scale(1)}96%,100%{opacity:0;transform:rotate(-12deg) scale(1)}}
@keyframes aReadA{0%,38%{opacity:1}46%,100%{opacity:0}}
@keyframes aEye{0%,100%{transform:translateX(-10px)}50%{transform:translateX(10px)}}
@keyframes aArrow{0%,100%{transform:translateX(0);opacity:.6}50%{transform:translateX(10px);opacity:1}}
@keyframes aChip{0%,8%{opacity:.18;transform:translateX(24px) scale(.96)}16%,90%{opacity:1;transform:translateX(0) scale(1)}100%{opacity:.18;transform:translateX(24px) scale(.96)}}
@keyframes aChipGlow{0%,100%{box-shadow:0 0 0 rgba(255,106,26,0)}50%{box-shadow:0 0 34px rgba(255,106,26,.55)}}
"""
fl = ''.join(
    f'<div style="flex: none; height: 12px; width: {w}%; border-radius: 6px; background: rgba(242,237,231,.32)"></div>'
    for w in (96, 88, 92, 70, 94, 84, 90, 62, 95, 86, 91, 74, 89, 93, 68, 90) * 2)
chips = ''.join(
    f'<div style="display: flex; align-items: center; gap: 16px; height: 86px; padding: 0 22px; border-radius: 18px; background: {"#FF6A1A" if i == 0 else "#1E1A17"}; color: {"#0A0908" if i == 0 else "#F2EDE7"}; border: 2px solid {"#FF6A1A" if i == 0 else "rgba(255,106,26,.5)"}; opacity: .18; animation: aChip 4s cubic-bezier(.3,0,.2,1) {0.35*i:.2f}s infinite, aChipGlow 2s ease-in-out {0.25*i:.2f}s infinite"><span style="{MONO}; font-weight: 600; font-size: 20px; opacity: .8">0{i+1}</span><span style="{BRIC}; font-weight: 800; font-size: 34px; letter-spacing: -0.02em">{t}</span></div>'
    for i, t in enumerate(('GANCHO', 'PROBLEMA', 'SOLUCIÓN', 'CIERRE')))
body2 = headline('EL ERROR MÁS COMÚN', 'Un guion no es un folio.', 'Son 4 bloques.', 82) + f"""
<div style="position: relative; height: 600px; display: flex; align-items: center; gap: 26px">
  <div style="position: relative; flex: none; width: 420px; height: 600px; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); overflow: hidden; animation: aFolio 4s cubic-bezier(.6,0,.3,1) infinite">
    <div style="position: absolute; left: 0; right: 0; top: 0; height: 64px; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; background: #1E1A17; z-index: 2">
      <span style="{MONO}; font-size: 17px; letter-spacing: .08em; color: #B5ADA4">TEXTO_ENTERO.DOC</span>
      <svg width="46" height="24" viewBox="0 0 46 24" style="animation: aEye 1.2s ease-in-out infinite"><ellipse cx="23" cy="12" rx="21" ry="10" fill="none" stroke="#FF6B61" stroke-width="3"/><circle cx="23" cy="12" r="5" fill="#FF6B61"/></svg>
    </div>
    <div style="position: absolute; left: 28px; right: 28px; top: 90px; bottom: 0; overflow: hidden">
      <div style="display: flex; flex-direction: column; gap: 18px; animation: aScroll 4s linear infinite">{fl}</div>
    </div>
    <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 120px; background: linear-gradient(0deg, #12100F, rgba(18,16,15,0))"></div>
    <div style="position: absolute; left: 24px; bottom: 24px; padding: 8px 14px; border-radius: 10px; background: rgba(255,59,48,.18); color: #FF6B61; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .08em; animation: aReadA 4s linear infinite">SE NOTA QUE LEES</div>
  </div>
  <div style="position: absolute; left: 60px; top: 230px; padding: 16px 26px; border: 5px solid #FF3B30; border-radius: 14px; color: #FF3B30; {BRIC}; font-weight: 800; font-size: 56px; letter-spacing: -0.02em; opacity: 0; animation: aStamp 4s cubic-bezier(.3,0,.2,1) infinite">DESCARTADO</div>
  <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" style="flex: none; animation: aArrow 1.4s ease-in-out infinite"><path d="M4 12h15M13 6l6 6-6 6"/></svg>
  <div style="flex: 1; display: flex; flex-direction: column; gap: 18px">{chips}</div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Folio vs bloques', 2, kf2, body2,
    'Bloques cortos = hablas natural, no lees.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 LA ESTRUCTURA
kf3 = """
@keyframes aQ{0%,24.9%{opacity:1}25%,100%{opacity:0}}
@keyframes aRow{0%,24.9%{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A;transform:scale(1.02)}25%,100%{background:#12100F;color:#F2EDE7;border-color:rgba(242,237,231,.12);transform:scale(1)}}
@keyframes aRowTxt{0%,24.9%{color:#0A0908;opacity:.85}25%,100%{color:#9C938B;opacity:1}}
@keyframes aProg{0%{width:0%}100%{width:100%}}
@keyframes aBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
"""
steps3 = [('GANCHO', 'La frase que frena el scroll', '“¿Te quedas en blanco a cámara?”'),
          ('PROBLEMA', 'Lo que le pasa a quien te ve', '“Es porque improvisas.”'),
          ('SOLUCIÓN', 'Tu consejo, en pasos cortos', '“Divide tu guion en 4 bloques.”'),
          ('CIERRE', 'Qué quieres que haga', '“Guárdalo para tu próximo vídeo.”')]
rows3 = ''.join(
    f'<div style="display: flex; align-items: center; gap: 20px; padding: 20px 24px; border-radius: 20px; border: 2px solid rgba(242,237,231,.12); background: #12100F; animation: aRow 4s steps(1) {k-4}s infinite"><span style="flex: none; width: 58px; height: 58px; border-radius: 99px; border: 2px solid currentColor; display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 22px">0{k+1}</span><div style="display: flex; flex-direction: column; gap: 4px"><span style="{BRIC}; font-weight: 800; font-size: 36px; letter-spacing: -0.02em; line-height: 1">{t}</span><span style="font-size: 23px; font-weight: 500; animation: aRowTxt 4s steps(1) {k-4}s infinite">{d}</span></div></div>'
    for k, (t, d, _) in enumerate(steps3))
subs3 = ''.join(
    f'<div style="position: absolute; left: 14px; right: 14px; bottom: 70px; padding: 12px 14px; border-radius: 12px; background: rgba(10,9,8,.86); text-align: center; font-weight: 700; font-size: 23px; line-height: 1.2; opacity: 0; animation: aQ 4s steps(1) {k-4}s infinite">{s}</div>'
    for k, (_, _, s) in enumerate(steps3))
segs3 = ''.join(
    f'<div style="flex: 1; height: 6px; border-radius: 99px; background: rgba(242,237,231,.25); overflow: hidden"><div style="height: 100%; background: #F2EDE7; width: 0%; animation: aProg 1s linear {k}s 1 both"></div></div>'
    for k in range(4))
body3 = headline('LA ESTRUCTURA', 'Cuatro bloques,', 'en este orden.') + f"""
<div style="position: relative; height: 600px; display: flex; gap: 30px; align-items: center">
  <div style="position: relative; flex: none; width: 320px; height: 600px; border-radius: 44px; background: #0A0908; border: 8px solid #1E1A17; box-shadow: 0 40px 100px -30px rgba(255,106,26,.55); overflow: hidden; animation: aBob 3s ease-in-out infinite">
    <div style="position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 30%, #2A150A, #0A0908 75%)"></div>
    <div style="position: absolute; left: 50%; bottom: -40px; margin-left: -160px; width: 320px">{PERSON.replace('width="420" height="420"', 'width="320" height="320"')}</div>
    <div style="position: absolute; left: 16px; right: 16px; top: 18px; display: flex; gap: 6px">{segs3}</div>
    {subs3}
  </div>
  <div style="flex: 1; display: flex; flex-direction: column; gap: 14px">{rows3}</div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Estructura', 3, kf3, body3,
    'Sirve para un reel, un anuncio o una historia.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 PLANTILLA
kf4 = """
@keyframes aType{0%{max-width:0}100%{max-width:640px}}
@keyframes aTick{0%{transform:scale(0);opacity:0}60%{transform:scale(1.25);opacity:1}100%{transform:scale(1);opacity:1}}
@keyframes aBox{0%{background:transparent;border-color:rgba(242,237,231,.35)}100%{background:#FF6A1A;border-color:#FF6A1A}}
@keyframes aCur{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes aTipGlow{0%,100%{box-shadow:0 0 0 rgba(255,106,26,0)}50%{box-shadow:0 0 40px rgba(255,106,26,.45)}}
@keyframes aRecOn{0%,86%{background:#1E1A17;color:#9C938B;box-shadow:none}90%,100%{background:#FF3B30;color:#F2EDE7;box-shadow:0 0 40px rgba(255,59,48,.8)}}
"""
tpl = [('GANCHO', '¿Te pasa [problema]?'),
       ('PROBLEMA', 'Es por [la causa].'),
       ('SOLUCIÓN', 'Haz [paso 1], [2] y [3].'),
       ('CIERRE', 'Guárdalo y síguenos.')]
rows4 = ''.join(
    f'<div style="display: flex; align-items: center; gap: 22px; height: 86px; padding: 0 24px; border-radius: 18px; background: #171412; border: 1px solid rgba(242,237,231,.08)">'
    f'<div style="flex: none; width: 44px; height: 44px; border-radius: 12px; border: 3px solid rgba(242,237,231,.35); box-sizing: border-box; display: flex; align-items: center; justify-content: center; animation: aBox .2s ease-out {0.7+0.75*k:.2f}s 1 both"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.4" style="animation: aTick .3s ease-out {0.7+0.75*k:.2f}s 1 both"><path d="M4 12l5 5 11-11"/></svg></div>'
    f'<span style="flex: none; width: 170px; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; color: #FFB27A">{t}</span>'
    f'<span style="display: inline-block; overflow: hidden; white-space: nowrap; max-width: 0; {BRIC}; font-weight: 700; font-size: 34px; letter-spacing: -0.02em; animation: aType .7s steps(22) {0.75*k:.2f}s 1 both">{x}</span>'
    f'</div>'
    for k, (t, x) in enumerate(tpl))
body4 = headline('PLANTILLA PARA COPIAR', 'Rellena los huecos', 'y dale a REC.') + f"""
<div style="position: relative; height: 600px; border-radius: 34px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.5); padding: 30px 32px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">
  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px">
    <span style="{MONO}; font-size: 20px; letter-spacing: .08em; color: #B5ADA4">MI_GUION.TXT</span>
    <div style="width: 96px; height: 44px; border-radius: 99px; display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; animation: aRecOn 4s ease-in-out infinite">● REC</div>
  </div>
  {rows4}
  <div style="margin-top: 6px; display: flex; align-items: center; gap: 16px; padding: 20px 24px; border-radius: 18px; border: 2px solid rgba(255,106,26,.55); animation: aTipGlow 2.4s ease-in-out infinite">
    <span style="flex: none; padding: 6px 12px; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .08em">TRUCO</span>
    <span style="font-size: 26px; font-weight: 600; line-height: 1.25">Apunta palabras clave, no frases: así hablas, no lees.</span>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Plantilla', 4, kf4, body4,
    'Haz captura y úsala en tu próximo vídeo.', DESLIZA_TXT))

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
    f'<div style="position: relative; aspect-ratio: 1/1; border-radius: 12px; background: linear-gradient(160deg, #2A150A, #171412); border: 1px solid rgba(242,237,231,.1); animation: aTile 4s ease-in-out {i*0.4:.1f}s infinite; display: flex; align-items: center; justify-content: center"><span style="position: absolute; top: 10px; left: 12px; font-family: \'JetBrains Mono\', monospace; font-size: 15px; color: #FFB27A">{["GUION","LUZ","SONIDO","ENCUADRE","EDICIÓN","GANCHO"][i]}</span><svg width="44" height="44" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(242,237,231,.12)"/><path d="M10 8l6 4-6 4z" fill="#F2EDE7"/></svg></div>'
    for i in range(6))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 80px; line-height: 1; letter-spacing: -0.045em">Tu próximo vídeo, <br><span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">sin quedarte en blanco.</span></p>
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
