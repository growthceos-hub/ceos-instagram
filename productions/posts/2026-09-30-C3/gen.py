#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C3 2026-09-30 (portadas de reels) en src/."""
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


def phone(w, h, inner, extra=''):
    return f'''<div style="position: relative; width: {w}px; height: {h}px; border-radius: 52px; background: #050505; padding: 14px; box-sizing: border-box; box-shadow: 0 0 0 3px rgba(242,237,231,.18), 0 50px 120px -30px rgba(255,106,26,.55); {extra}">
<div style="position: relative; width: 100%; height: 100%; border-radius: 40px; overflow: hidden; background: #0A0908">{inner}
<div style="position: absolute; left: 50%; top: 12px; width: 110px; height: 30px; margin-left: -55px; border-radius: 99px; background: #050505; z-index: 9"></div></div></div>'''



def scene(w, h, px, pw, extra='', tall=False):
    """Plano de estudio w x h con persona centrada en px (ancho pw)."""
    return f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #1C130D 0%, #12100F 70%, #0A0908 100%)"></div>
<div style="position: absolute; left: {px - pw*0.9}px; top: 4%; width: {pw*1.8}px; height: 90%; border-radius: 50%; background: radial-gradient(circle, rgba(255,106,26,.30), rgba(255,106,26,0) 70%); animation: aGlow 4s ease-in-out infinite"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 14%; background: linear-gradient(180deg, #171412, #0A0908); border-top: 2px solid rgba(242,237,231,.06)"></div>
{extra}
<div style="position: absolute; left: {px - pw/2}px; bottom: -{15 if tall else pw*0.06}px; width: {pw}px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{PERSON.replace('height="420" viewBox="0 0 420 420"', f'height="{pw*700/420:.0f}" viewBox="0 0 420 700"').replace('width="420"', f'width="{pw}"').replace('M40 420 C40 300 110 250 210 250 C310 250 380 300 380 420 Z', 'M8 700 L8 400 C8 300 96 262 210 262 C324 262 412 300 412 400 L412 700 Z').replace('id="pg"', 'id="px"').replace('url(#pg)', 'url(#px)') if tall else person(pw)}</div>'''


def ticklist(items, anims):
    return ''.join(
        f'<div style="display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 18px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s ease-in-out infinite">'
        f'<span style="flex: none; width: 40px; height: 40px; border-radius: 99px; border: 2px solid #FF6A1A; display: flex; align-items: center; justify-content: center"><svg width="24" height="24" viewBox="0 0 24 24" style="animation: {tk} 4s ease-out infinite"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#FF6A1A" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
        f'<span style="{BRIC}; font-weight: 800; font-size: 28px; letter-spacing: -0.02em; line-height: 1.05">{t}</span></div>'
        for t, (a, tk) in zip(items, anims))


def chk_kf(n, starts):
    out = ''
    for i, s in enumerate(starts, 1):
        out += f"@keyframes a{n}Row{i}{{0%,{s}%{{background:#12100F;border-color:rgba(242,237,231,.14)}}{s+6}%,94%{{background:#1E1A17;border-color:#FF6A1A}}100%{{background:#12100F;border-color:rgba(242,237,231,.14)}}}}\n"
        out += f"@keyframes a{n}Tk{i}{{0%,{s+2}%{{transform:scale(0)}}{s+7}%{{transform:scale(1.25)}}{s+11}%,94%{{transform:scale(1)}}100%{{transform:scale(0)}}}}\n"
    return out


def rec_badge(left=26, top=22, label='REC'):
    return f'<div style="position: absolute; left: {left}px; top: {top}px; display: flex; align-items: center; gap: 10px; {MONO}; font-size: 19px; letter-spacing: .1em; color: #F2EDE7; z-index: 6"><span style="width: 13px; height: 13px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30; animation: aRec 1s steps(1) infinite"></span>{label}</div>'



# ============================================================ helpers C3 (portadas de reels)
def person_svg(w, uid, col='#F2EDE7', smile=False):
    s = '<path d="M180 150 Q210 172 240 150" fill="none" stroke="#0A0908" stroke-width="7" stroke-linecap="round" opacity=".55"/>' if smile else ''
    return f'''<svg width="{w}" height="{w}" viewBox="0 0 420 420" style="display:block">
<defs><linearGradient id="p{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{col}" stop-opacity=".96"/><stop offset="1" stop-color="#B5ADA4" stop-opacity=".6"/></linearGradient></defs>
<path d="M40 420 C40 300 110 250 210 250 C310 250 380 300 380 420 Z" fill="url(#p{uid})"/>
<rect x="178" y="200" width="64" height="70" rx="26" fill="url(#p{uid})"/>
<ellipse cx="210" cy="125" rx="78" ry="92" fill="url(#p{uid})"/>
<rect x="168" y="112" width="18" height="10" rx="5" fill="#0A0908" opacity=".55"/><rect x="234" y="112" width="18" height="10" rx="5" fill="#0A0908" opacity=".55"/>{s}
</svg>'''


def clean_tile(title, accent, w, h, uid, glow=True):
    """Portada de marca: fondo azul, cara con expresión, título grande siempre en el mismo sitio."""
    fs = w * 0.165
    g = f'<div style="position: absolute; left: 10%; top: 18%; width: 80%; height: 70%; border-radius: 50%; background: radial-gradient(circle, rgba(255,106,26,.45), rgba(255,106,26,0) 70%)"></div>' if glow else ''
    return f'''<div style="position: absolute; inset: 0; overflow: hidden; background: linear-gradient(180deg, #2A150A 0%, #1C130D 55%, #0A0908 100%)">{g}
<div style="position: absolute; left: {w*0.15:.0f}px; bottom: -{w*0.2:.0f}px">{person_svg(int(w*0.7), uid, smile=True)}</div>
<div style="position: absolute; left: 0; right: 0; top: {h*0.12:.0f}px; text-align: center; {BRIC}; font-weight: 800; font-size: {fs:.0f}px; line-height: .92; letter-spacing: -0.04em; color: #F2EDE7; text-shadow: 0 {w*0.02:.0f}px {w*0.06:.0f}px rgba(0,0,0,.7)">{title}<br><span style="{SERIF}; color: #FF6A1A; font-size: {fs*1.05:.0f}px">{accent}</span></div>
</div>'''


MESSY = [('#3A3633', 0, 30, 'hola chicos hoy os traigo'), ('#6B635C', -40, 60, ''), ('#1E1A17', 30, -10, 'y bueno pues eso'),
         ('#9C938B', 60, 40, ''), ('#2B2724', -20, 80, 'parte 2 (ver la 1)'), ('#4A443F', 10, -30, ''),
         ('#171412', -50, 20, 'no sé qué poner aquí'), ('#7A716A', 40, 70, ''), ('#34302C', 0, 50, 'jajaja')]


def messy_tile(i, w, h, uid):
    bg, dx, dy, txt = MESSY[i % len(MESSY)]
    t = f'<div style="position: absolute; left: 8%; right: 8%; bottom: 10%; font-size: {max(9, w*0.075):.0f}px; line-height: 1.1; color: rgba(242,237,231,.7)">{txt}</div>' if txt else ''
    eyes = f'<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: linear-gradient(0deg, rgba(0,0,0,.35), rgba(0,0,0,0))"></div>'
    return f'''<div style="position: absolute; inset: 0; overflow: hidden; background: {bg}; filter: saturate(.3) blur({0.6 if i % 2 else 0}px)">
<div style="position: absolute; left: {w*0.1 + dx*w/135:.0f}px; top: {h*0.25 + dy*h/180:.0f}px; opacity: .55; transform: rotate({(i%3-1)*6}deg)">{person_svg(int(w*0.8), uid, '#B5ADA4')}</div>{eyes}{t}</div>'''


TITLES = [('LUZ', 'natural'), ('SONIDO', 'limpio'), ('GUION', 'en 3 pasos'), ('ENCUADRE', 'bien'), ('B-ROLL', 'que luce'),
          ('TU VOZ', 'a cámara'), ('FONDO', 'de estudio'), ('EDICIÓN', 'con ritmo'), ('GANCHO', '3 segundos')]


# ---------------------------------------------------------------- 01 GANCHO
TW, TH = 134, 179
def tile_kf():
    out = ''
    for k in range(9):
        s = 26 + (k % 3) * 4 + (k // 3) * 6
        out += f"@keyframes aC{k}{{0%,{s}%{{opacity:0;transform:scale(.6) rotateY(80deg)}}{s+7}%,90%{{opacity:1;transform:none}}97%,100%{{opacity:0;transform:scale(.9)}}}}\n"
    return out


kf1 = COMMON_KF + tile_kf() + """
@keyframes aBadC{0%,26%{opacity:1;transform:none}32%,94%{opacity:0;transform:translateY(-14px)}100%{opacity:1}}
@keyframes aGoodC{0%,40%{opacity:0;transform:translateY(14px)}48%,90%{opacity:1;transform:none}97%,100%{opacity:0}}
@keyframes aPhoneB{0%,26%{box-shadow:0 0 0 4px #FF3B30, 0 50px 120px -30px rgba(255,59,48,.55)}46%,90%{box-shadow:0 0 0 4px #FF6A1A, 0 50px 120px -30px rgba(255,106,26,.75)}100%{box-shadow:0 0 0 4px #FF3B30, 0 50px 120px -30px rgba(255,59,48,.55)}}
@keyframes aZoomBig{0%,100%{transform:scale(1)}50%{transform:scale(1.03)}}
@keyframes aLens{0%,100%{transform:translate(0,0)}50%{transform:translate(4px,-4px)}}
@keyframes aPlay{0%,100%{transform:scale(1);opacity:.9}50%{transform:scale(1.12);opacity:1}}
"""


def grid_tiles(tw, th, clean_anim=True, prefix='g'):
    cells = ''
    for k in range(9):
        r, c = divmod(k, 3)
        x, y = c * (tw + 3), r * (th + 3)
        t, a = TITLES[k]
        cl = f'animation: aC{k} 4s cubic-bezier(.6,0,.3,1) infinite; opacity: 0' if clean_anim else ''
        cells += f'''<div style="position: absolute; left: {x}px; top: {y}px; width: {tw}px; height: {th}px; overflow: hidden; perspective: 400px">
{messy_tile(k, tw, th, f'{prefix}m{k}')}
<div style="position: absolute; inset: 0; {cl}">{clean_tile(t, a, tw, th, f'{prefix}c{k}', glow=False)}</div></div>'''
    return cells


prof_head = f'''<div style="position: relative; height: 104px; padding: 46px 18px 0; box-sizing: border-box; display: flex; align-items: center; gap: 14px">
<div style="width: 50px; height: 50px; border-radius: 99px; background: linear-gradient(135deg, #FF6A1A, #FFB27A); padding: 3px; box-sizing: border-box"><div style="width: 100%; height: 100%; border-radius: 99px; background: #1E1A17"></div></div>
<div style="display: flex; flex-direction: column; gap: 6px"><span style="{BRIC}; font-weight: 800; font-size: 20px">@tu.marca</span>
<div style="display: flex; gap: 6px"><span style="width: 60px; height: 8px; border-radius: 9px; background: rgba(242,237,231,.2)"></span><span style="width: 90px; height: 8px; border-radius: 9px; background: rgba(242,237,231,.14)"></span></div></div>
<svg width="26" height="26" viewBox="0 0 24 24" style="margin-left: auto"><rect x="3" y="3" width="18" height="18" rx="2" fill="none" stroke="#F2EDE7" stroke-width="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18" stroke="#F2EDE7" stroke-width="1.6"/></svg></div>'''

inner1 = prof_head + f'<div style="position: relative; margin-top: 4px; width: {3*TW+6}px; height: {3*TH+6}px">{grid_tiles(TW, TH)}</div>'

big_tile = f'''<div style="position: relative; width: 330px; height: 440px; border-radius: 26px; overflow: hidden; border: 3px solid rgba(242,237,231,.18); animation: aZoomBig 4s ease-in-out infinite">
{messy_tile(0, 330, 440, 'bm')}
<div style="position: absolute; inset: 0; opacity: 0; animation: aC0 4s cubic-bezier(.6,0,.3,1) infinite">{clean_tile('LUZ', 'natural', 330, 440, 'bc')}</div>
<div style="position: absolute; right: 18px; bottom: 18px; width: 76px; height: 76px; border-radius: 99px; background: rgba(10,9,8,.55); border: 3px solid #F2EDE7; display: flex; align-items: center; justify-content: center; animation: aPlay 2s ease-in-out infinite; z-index: 4"><svg width="30" height="30" viewBox="0 0 24 24"><path d="M7 4l13 8-13 8z" fill="#F2EDE7"/></svg></div>
<div style="position: absolute; left: 16px; top: 14px; padding: 7px 12px; border-radius: 10px; background: rgba(10,9,8,.75); {MONO}; font-size: 16px; letter-spacing: .1em; color: #F2EDE7; z-index: 4">ZOOM · PORTADA</div>
</div>'''

body1 = headline('PORTADAS DE REELS', 'Si tu perfil es un caos,', 'nadie le da al play.', 88) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 40px; align-items: flex-start">
  <div style="position: relative; flex: none; width: 440px; height: 660px; border-radius: 52px; background: #050505; padding: 14px; box-sizing: border-box; animation: aPhoneB 4s ease-in-out infinite">
    <div style="position: relative; width: 100%; height: 100%; border-radius: 40px; overflow: hidden; background: #0A0908">{inner1}
    <div style="position: absolute; left: 50%; top: 12px; width: 110px; height: 30px; margin-left: -55px; border-radius: 99px; background: #050505; z-index: 9"></div></div>
  </div>
  <div style="position: relative; flex: 1; height: 660px; display: flex; flex-direction: column; gap: 20px">
    {big_tile}
    <div style="position: relative; flex: 1; border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); overflow: hidden">
      <div style="position: absolute; inset: 0; display: flex; align-items: center; gap: 16px; padding: 0 22px; animation: aBadC 4s ease-in-out infinite">
        <span style="flex: none; width: 54px; height: 54px; border-radius: 99px; background: #FF3B30; color: #fff; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 30px">✗</span>
        <span style="{BRIC}; font-weight: 800; font-size: 31px; line-height: 1.05; letter-spacing: -0.03em">Fotograma <span style="{SERIF}; color: #FF3B30; font-size: 38px">al azar</span></span>
      </div>
      <div style="position: absolute; inset: 0; display: flex; align-items: center; gap: 16px; padding: 0 22px; opacity: 0; animation: aGoodC 4s ease-in-out infinite">
        <span style="flex: none; width: 54px; height: 54px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 30px">✓</span>
        <span style="{BRIC}; font-weight: 800; font-size: 31px; line-height: 1.05; letter-spacing: -0.03em">Portada <span style="{SERIF}; color: #FF6A1A; font-size: 38px">de marca</span></span>
      </div>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    '3 reglas para portadas que dan ganas de ver.', DESLIZA_PILL))


# ---------------------------------------------------------------- 02 ZONA SEGURA (recorte del perfil)
CW, CH = 300, 533
CROP_T = (CH - 400) // 2  # 66
kf2 = COMMON_KF + """
@keyframes aTitle{0%,30%{top:14px}48%,90%{top:188px}100%{top:14px}}
@keyframes aBandKo{0%,32%{background:rgba(255,59,48,.38)}46%,90%{background:rgba(10,9,8,.72)}100%{background:rgba(255,59,48,.38)}}
@keyframes aCropB{0%,32%{border-color:#FF3B30}46%,90%{border-color:#FF6A1A}100%{border-color:#FF3B30}}
@keyframes aKo{0%,30%{opacity:1;transform:translate(-50%,0) scale(1)}38%,94%{opacity:0;transform:translate(-50%,0) scale(.85)}100%{opacity:1}}
@keyframes aOk{0%,46%{opacity:0;transform:translate(-50%,0) scale(.85)}54%,88%{opacity:1;transform:translate(-50%,0) scale(1)}96%,100%{opacity:0}}
@keyframes aArrow{0%,100%{transform:translateX(0)}50%{transform:translateX(10px)}}
@keyframes aDash2{to{stroke-dashoffset:-40}}
@keyframes aCardA{0%,40%{border-color:#FF3B30}50%,90%{border-color:#FF6A1A}100%{border-color:#FF3B30}}
"""


def cover2(uid):
    return f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #2A150A 0%, #1C130D 55%, #0A0908 100%)"></div>
<div style="position: absolute; left: 30px; top: 110px; width: 240px; height: 400px; border-radius: 50%; background: radial-gradient(circle, rgba(255,106,26,.4), rgba(255,106,26,0) 70%); animation: aGlow 4s ease-in-out infinite"></div>
<div style="position: absolute; left: 30px; bottom: -30px; animation: aBreath 3s ease-in-out infinite">{person_svg(240, uid, smile=True)}</div>
<div style="position: absolute; left: 0; right: 0; top: 14px; text-align: center; {BRIC}; font-weight: 800; font-size: 52px; line-height: .92; letter-spacing: -0.04em; color: #F2EDE7; text-shadow: 0 4px 20px rgba(0,0,0,.7); animation: aTitle 4s cubic-bezier(.7,0,.3,1) infinite">3 TRUCOS<br><span style="{SERIF}; color: #FF6A1A; font-size: 56px">de luz</span></div>'''


body2 = headline('REGLA 1 · ZONA SEGURA', 'Tu perfil la recorta:', 'pon el título en el centro.', 86) + f"""
<div style="position: relative; height: 680px; display: flex; flex-direction: column; gap: 22px">
  <div style="position: relative; height: 560px; border-radius: 28px; background: #12100F; border: 2px solid rgba(242,237,231,.14); overflow: hidden">
    <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(242,237,231,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(242,237,231,0.05) 1px, transparent 1px); background-size: 40px 40px"></div>
    <div style="position: absolute; left: 60px; top: 14px; width: {CW}px; height: {CH}px; margin-top: 0; border-radius: 18px; overflow: hidden; box-shadow: 0 30px 80px -30px rgba(0,0,0,.8); transform: translateY(0)">
      {cover2('a2')}
      <div style="position: absolute; left: 0; right: 0; top: 0; height: {CROP_T}px; z-index: 4; animation: aBandKo 4s ease-in-out infinite"></div>
      <div style="position: absolute; left: 0; right: 0; bottom: 0; height: {CROP_T}px; z-index: 4; animation: aBandKo 4s ease-in-out infinite"></div>
      <div style="position: absolute; left: 12px; bottom: 18px; padding: 6px 10px; border-radius: 8px; background: rgba(10,9,8,.8); {MONO}; font-weight: 600; font-size: 15px; letter-spacing: .1em; color: #F2EDE7; z-index: 6">REEL · 9:16</div>
      <div style="position: absolute; left: 0; right: 0; top: {CROP_T}px; height: 400px; border: 4px dashed #FF3B30; box-sizing: border-box; z-index: 5; animation: aCropB 4s ease-in-out infinite"></div>
    </div>
    <div style="position: absolute; left: 392px; top: 250px; animation: aArrow 1.4s ease-in-out infinite"><svg width="80" height="40" viewBox="0 0 80 40"><line x1="0" y1="20" x2="60" y2="20" stroke="#FF6A1A" stroke-width="5" stroke-dasharray="10 8" style="animation: aDash2 1s linear infinite"/><path d="M56 6 L80 20 L56 34 Z" fill="#FF6A1A"/></svg></div>
    <div style="position: absolute; left: 500px; top: 34px; {MONO}; font-weight: 600; font-size: 17px; letter-spacing: .1em; color: #FF6A1A; z-index: 3">ASÍ SE VE EN TU PERFIL</div>
    <div style="position: absolute; left: 500px; top: 80px; width: {CW}px; height: 400px; border-radius: 18px; overflow: hidden; border: 4px solid #FF3B30; box-sizing: border-box; animation: aCropB 4s ease-in-out infinite; box-shadow: 0 40px 100px -30px rgba(255,106,26,.6)">
      <div style="position: absolute; left: -4px; top: -{CROP_T + 4}px; width: {CW}px; height: {CH}px">{cover2('b2')}</div>
    </div>
    <div style="position: absolute; left: 650px; top: 494px; white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF3B30; color: #fff; {BRIC}; font-weight: 800; font-size: 26px; z-index: 7; animation: aKo 4s ease-in-out infinite">✗ Título cortado</div>
    <div style="position: absolute; left: 650px; top: 494px; white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 26px; z-index: 7; opacity: 0; animation: aOk 4s ease-in-out infinite">✓ Se lee entero</div>
  </div>
  <div style="position: relative; flex: 1; display: flex; align-items: center; gap: 20px; padding: 0 28px; border-radius: 24px; background: #12100F; border: 2px solid #FF3B30; animation: aCardA 4s ease-in-out infinite">
    <span style="flex: none; width: 58px; height: 58px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 30px">↕</span>
    <span style="{BRIC}; font-weight: 800; font-size: 30px; line-height: 1.1; letter-spacing: -0.02em">Deja libres arriba y abajo: <span style="{SERIF}; color: #FF6A1A; font-size: 36px">texto y cara, al centro</span></span>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Zona segura', 2, kf2, body2,
    'La cuadrícula solo enseña la parte central.', DESLIZA_TXT))


# ---------------------------------------------------------------- 03 SE LEE EN MINIATURA
kf3 = COMMON_KF + """
@keyframes aShrink{0%,22%{transform:scale(1)}40%,84%{transform:scale(.42)}100%{transform:scale(1)}}
@keyframes aMini{0%,34%{opacity:0}44%,82%{opacity:1}92%,100%{opacity:0}}
@keyframes aBadge{0%,42%{opacity:0;transform:translate(-50%,20px) scale(.8)}50%,82%{opacity:1;transform:translate(-50%,0) scale(1)}90%,100%{opacity:0}}
@keyframes aChip1{0%,8%{background:#12100F;border-color:rgba(242,237,231,.14);color:#B5ADA4}14%,94%{background:#FF6A1A;border-color:#FF6A1A;color:#0A0908}100%{background:#12100F}}
@keyframes aChip2{0%,30%{background:#12100F;border-color:rgba(242,237,231,.14);color:#B5ADA4}36%,94%{background:#FF6A1A;border-color:#FF6A1A;color:#0A0908}100%{background:#12100F}}
@keyframes aChip3{0%,52%{background:#12100F;border-color:rgba(242,237,231,.14);color:#B5ADA4}58%,94%{background:#FF6A1A;border-color:#FF6A1A;color:#0A0908}100%{background:#12100F}}
@keyframes aDashM{to{stroke-dashoffset:-30}}
"""
PW, PH = 360, 480


def cover3(kind, uid):
    base = f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #2A150A 0%, #1C130D 55%, #0A0908 100%)"></div>
<div style="position: absolute; left: 50px; bottom: -40px">{person_svg(260, uid, smile=(kind == 'ok'))}</div>'''
    if kind == 'ko':
        txt = f'<div style="position: absolute; left: 24px; right: 24px; top: 28px; font-size: 21px; line-height: 1.25; color: #D9D1C8; font-weight: 500">Hoy os traigo algunos consejos para mejorar la iluminación de vuestros vídeos en casa y que se vean un poquito mejor, espero que os sirvan</div>'
    else:
        txt = f'<div style="position: absolute; left: 0; right: 0; top: 118px; text-align: center; {BRIC}; font-weight: 800; font-size: 74px; line-height: .9; letter-spacing: -0.045em; color: #F2EDE7; text-shadow: 0 5px 24px rgba(0,0,0,.7)">LUZ QUE<br><span style="{SERIF}; color: #FF6A1A; font-size: 80px">favorece</span></div>'
    return base + txt


def panel3(kind, uid):
    col = '#FF3B30' if kind == 'ko' else '#FF6A1A'
    badge = ('✗ No se lee', '#FF3B30', '#fff') if kind == 'ko' else ('✓ Se lee al vuelo', '#FF6A1A', '#0A0908')
    return f'''<div style="position: relative; width: {PW}px; height: 560px">
  <div style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PH}px; transform-origin: 50% 50%; animation: aShrink 4s cubic-bezier(.7,0,.3,1) infinite">
    <div style="position: absolute; inset: 0; border-radius: 22px; overflow: hidden; border: 4px solid {col}; box-sizing: border-box; box-shadow: 0 40px 100px -30px {'rgba(255,59,48,.55)' if kind == 'ko' else 'rgba(255,106,26,.7)'}">{cover3(kind, uid)}</div>
  </div>
  <svg width="{PW}" height="{PH}" viewBox="0 0 {PW} {PH}" style="position: absolute; left: 0; top: 0; opacity: 0; animation: aMini 4s ease-in-out infinite; overflow: visible">
    <rect x="96" y="132" width="168" height="216" rx="14" fill="none" stroke="#F2EDE7" stroke-opacity=".5" stroke-width="3" stroke-dasharray="10 8" style="animation: aDashM 1s linear infinite"/>
  </svg>
  <div style="position: absolute; left: 50%; top: 364px; white-space: nowrap; {MONO}; font-size: 16px; letter-spacing: .1em; color: #9C938B; transform: translateX(-50%); opacity: 0; animation: aMini 4s ease-in-out infinite">TAMAÑO EN EL PERFIL</div>
  <div style="position: absolute; left: 50%; top: 486px; white-space: nowrap; padding: 12px 20px; border-radius: 14px; background: {badge[1]}; color: {badge[2]}; {BRIC}; font-weight: 800; font-size: 30px; opacity: 0; animation: aBadge 4s ease-in-out infinite">{badge[0]}</div>
</div>'''


chips3 = ''.join(
    f'<span style="flex: 1; text-align: center; padding: 18px 10px; border-radius: 18px; border: 2px solid rgba(242,237,231,.14); background: #12100F; {BRIC}; font-weight: 800; font-size: 29px; letter-spacing: -0.02em; animation: aChip{i} 4s ease-in-out infinite">{t}</span>'
    for i, t in ((1, 'Máx. 3–4 palabras'), (2, 'Letra gruesa'), (3, 'Contraste alto')))

body3 = headline('REGLA 2 · MINIATURA', '¿No se lee en pequeño?', 'Entonces no existe.', 84) + f"""
<div style="position: relative; height: 680px; display: flex; flex-direction: column; gap: 24px">
  <div style="position: relative; height: 570px; border-radius: 28px; background: #12100F; border: 2px solid rgba(242,237,231,.14); display: flex; justify-content: center; gap: 60px; padding-top: 4px; box-sizing: border-box; overflow: hidden">
    <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(242,237,231,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(242,237,231,0.05) 1px, transparent 1px); background-size: 40px 40px"></div>
    {panel3('ko', 'k3')}{panel3('ok', 'o3')}
  </div>
  <div style="position: relative; flex: 1; display: flex; gap: 14px; align-items: stretch">{chips3}</div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Miniatura', 3, kf3, body3,
    'Piensa en cómo se ve desde el perfil, no en grande.', DESLIZA_TXT))


# ---------------------------------------------------------------- 04 UNA PLANTILLA FIJA
kf4 = COMMON_KF + """
@keyframes aL1{0%,2%{opacity:0}12%,84%{opacity:1}92%,100%{opacity:0}}
@keyframes aL2{0%,20%{opacity:0;transform:translateY(80px)}32%,84%{opacity:1;transform:none}92%,100%{opacity:0}}
@keyframes aL3{0%,40%{opacity:0;transform:translateY(-60px) scale(1.2)}50%,84%{opacity:1;transform:none}92%,100%{opacity:0}}
@keyframes aFly{0%,58%{transform:translate(0,0) scale(1)}74%,86%{transform:translate(212px,440px) scale(.3333)}92%,100%{transform:translate(212px,440px) scale(.3333)}}
@keyframes aSlot{0%,70%{opacity:1}74%,100%{opacity:0}}
@keyframes aRowS1{0%,2%{background:#12100F;border-color:rgba(242,237,231,.14)}8%,20%{background:#1E1A17;border-color:#FF6A1A}26%,100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aRowS2{0%,20%{background:#12100F;border-color:rgba(242,237,231,.14)}26%,38%{background:#1E1A17;border-color:#FF6A1A}44%,100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aRowS3{0%,40%{background:#12100F;border-color:rgba(242,237,231,.14)}46%,58%{background:#1E1A17;border-color:#FF6A1A}64%,100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aRowS4{0%,62%{background:#12100F;border-color:rgba(242,237,231,.14)}68%,90%{background:#1E1A17;border-color:#FF6A1A}96%,100%{background:#12100F;border-color:rgba(242,237,231,.14)}}
@keyframes aNum{0%,100%{box-shadow:0 0 0 0 rgba(255,106,26,.5)}50%{box-shadow:0 0 0 10px rgba(255,106,26,0)}}
@keyframes aCur{0%,56%{opacity:0}62%,80%{opacity:1}86%,100%{opacity:0}}
"""


def step_row(n, title, sub, anim):
    return f'''<div style="position: relative; flex: 1; display: flex; align-items: center; gap: 18px; padding: 0 22px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {anim} 4s ease-in-out infinite">
<span style="flex: none; width: 56px; height: 56px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; {MONO}; font-weight: 600; font-size: 24px; animation: aNum 2s ease-out infinite">{n}</span>
<span style="display: flex; flex-direction: column; gap: 4px"><span style="{BRIC}; font-weight: 800; font-size: 31px; letter-spacing: -0.02em; line-height: 1.02">{title}</span><span style="font-size: 21px; color: #B5ADA4; line-height: 1.2">{sub}</span></span></div>'''


mini_row = ''.join(
    f'<div style="position: absolute; left: {68 + i*112}px; top: 440px; width: 100px; height: 133px; border-radius: 10px; overflow: hidden; border: 2px solid rgba(242,237,231,.18)">{clean_tile(t, a, 100, 133, f"mr{i}", glow=False)}</div>'
    for i, (t, a) in enumerate([TITLES[1], TITLES[2]]))
slot = f'<div style="position: absolute; left: 292px; top: 440px; width: 100px; height: 133px; border-radius: 10px; border: 3px dashed #FF6A1A; box-sizing: border-box; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 40px; color: #FF6A1A; animation: aSlot 4s steps(1) infinite">+</div>'

build = f'''<div style="position: absolute; left: 80px; top: 0; width: 300px; height: 400px; transform-origin: 0 0; animation: aFly 4s cubic-bezier(.7,0,.3,1) infinite; z-index: 5">
  <div style="position: absolute; inset: 0; border-radius: 22px; border: 3px dashed rgba(242,237,231,.25); box-sizing: border-box"></div>
  <div style="position: absolute; inset: 0; border-radius: 22px; overflow: hidden; box-shadow: 0 40px 100px -30px rgba(255,106,26,.7)">
    <div style="position: absolute; inset: 0; opacity: 0; animation: aL1 4s ease-in-out infinite; background: linear-gradient(180deg, #2A150A 0%, #1C130D 55%, #0A0908 100%)"><div style="position: absolute; left: 10%; top: 18%; width: 80%; height: 70%; border-radius: 50%; background: radial-gradient(circle, rgba(255,106,26,.45), rgba(255,106,26,0) 70%)"></div></div>
    <div style="position: absolute; left: 45px; bottom: -70px; opacity: 0; animation: aL2 4s cubic-bezier(.3,1.3,.5,1) infinite">{person_svg(210, 'b4', smile=True)}</div>
    <div style="position: absolute; left: 0; right: 0; top: 44px; text-align: center; {BRIC}; font-weight: 800; font-size: 56px; line-height: .92; letter-spacing: -0.04em; color: #F2EDE7; text-shadow: 0 4px 20px rgba(0,0,0,.7); opacity: 0; animation: aL3 4s cubic-bezier(.3,1.3,.5,1) infinite">LUZ<br><span style="{SERIF}; color: #FF6A1A; font-size: 53px">natural</span></div>
  </div>
</div>'''

body4 = headline('REGLA 3 · PLANTILLA', 'Misma plantilla,', 'cada vez.', 94) + f"""
<div style="position: relative; height: 640px; display: flex; gap: 30px">
  <div style="position: relative; width: 430px; display: flex; flex-direction: column; gap: 14px">
    {step_row(1, 'Fondo de marca', 'Siempre los mismos colores', 'aRowS1')}
    {step_row(2, 'Tu cara, expresiva', 'Mirando a cámara, que transmita', 'aRowS2')}
    {step_row(3, 'Título, mismo sitio', 'Misma letra y posición', 'aRowS3')}
    {step_row(4, 'A la cuadrícula', 'Y todo el perfil se ve de marca', 'aRowS4')}
  </div>
  <div style="position: relative; flex: 1; border-radius: 28px; background: #12100F; border: 2px solid rgba(242,237,231,.14); overflow: hidden; padding: 24px 0 0; box-sizing: border-box">
    <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(242,237,231,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(242,237,231,0.05) 1px, transparent 1px); background-size: 40px 40px"></div>
    <div style="position: relative; width: 460px; height: 600px; margin: 0 auto">
      {mini_row}{slot}{build}
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Plantilla', 4, kf4, body4,
    'Elígela en «Editar portada» antes de publicar.', DESLIZA_TXT))


# ---------------------------------------------------------------- 05 CTA
kf5 = COMMON_KF + chk_kf(5, [8, 30, 52]) + """
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
@keyframes aFol{0%,46%{opacity:1}50%,100%{opacity:0}}
@keyframes aFolD{0%,46%{opacity:0}50%,100%{opacity:1}}
@keyframes aFolBg{0%,46%{background:#FF6A1A;color:#0A0908}50%,100%{background:#1E1A17;color:#F2EDE7}}
@keyframes aTap{0%,36%{opacity:0;transform:scale(1.4)}42%{opacity:1;transform:scale(1)}48%{opacity:1;transform:scale(.85)}56%,100%{opacity:0;transform:scale(1)}}
"""
items5 = ['<span style="color:#FF6A1A">1 ·</span> Título y cara en el centro',
          '<span style="color:#FF6A1A">2 ·</span> 3–4 palabras que se lean en pequeño',
          '<span style="color:#FF6A1A">3 ·</span> Una plantilla fija para todas']
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 84px; line-height: 1; letter-spacing: -0.045em">Tu portada es<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">la puerta de tu reel.</span></p>
<div style="position: relative; margin-top: 40px; width: 920px; display: flex; flex-direction: column; gap: 14px; text-align: left">
{ticklist([f'<span style="font-size:34px">{t}</span>' for t in items5], [('a5Row1', 'a5Tk1'), ('a5Row2', 'a5Tk2'), ('a5Row3', 'a5Tk3')])}
</div>
<div style="position: relative; margin-top: 34px; display: flex; align-items: center; gap: 22px; padding: 18px 22px 18px 18px; border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14)">
  <img src="{LOGO}" style="width: 64px; height: 64px; border-radius: 99px; animation: aLogo 4s ease-in-out infinite">
  <span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em">@ceos.productions</span>
  <span style="position: relative; width: 190px; height: 58px; border-radius: 14px; {BRIC}; font-weight: 800; font-size: 28px; animation: aFolBg 4s steps(1) infinite; display: flex; align-items: center; justify-content: center">
    <span style="position: absolute; animation: aFol 4s steps(1) infinite">Seguir</span><span style="position: absolute; opacity: 0; animation: aFolD 4s steps(1) infinite">Siguiendo ✓</span>
    <span style="position: absolute; right: -14px; bottom: -22px; width: 56px; height: 56px; border-radius: 99px; background: rgba(242,237,231,.35); border: 3px solid #F2EDE7; opacity: 0; animation: aTap 4s ease-out infinite"></span>
  </span>
</div>
<div style="position: relative; overflow: hidden; margin-top: 34px; padding: 26px 54px; border-radius: 30px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 64px; line-height: 1; letter-spacing: -0.04em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.3), rgba(255,255,255,0)); animation: aShim 4s ease-in-out 0.6s infinite"></div></div>
</div>
"""
open(os.path.join(OUT, 'S5.dc.html'), 'w').write(page('05 · CTA', 5, kf5, body5,
    'Guárdalo para tu próxima portada.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
