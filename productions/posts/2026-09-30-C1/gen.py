#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C1 2026-09-30 (formatos de vídeo) en src/."""
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


# ---------------------------------------------------------------- 01 GANCHO
kf1 = COMMON_KF + """
@keyframes aCrop{0%,42%{left:314px;width:291px}58%,76%{left:0px;width:920px}92%,100%{left:314px;width:291px}}
@keyframes aCutOn{0%,40%{opacity:1;transform:translateX(-50%) scale(1)}46%,88%{opacity:0;transform:translateX(-50%) scale(.85)}94%,100%{opacity:1;transform:translateX(-50%) scale(1)}}
@keyframes aFullOn{0%,52%{opacity:0}60%,76%{opacity:1}84%,100%{opacity:0}}
@keyframes aDash{to{stroke-dashoffset:-40}}
@keyframes aLose{0%,42%{left:34.2%;width:31.6%}58%,76%{left:0%;width:100%}92%,100%{left:34.2%;width:31.6%}}
@keyframes aLblOn{0%,40%{opacity:1}46%,88%{opacity:0}94%,100%{opacity:1}}
@keyframes aSlash{0%,100%{transform:translateX(-50%) rotate(-8deg) scale(1)}50%{transform:translateX(-50%) rotate(-8deg) scale(1.06)}}
"""
mon1 = scene(920, 518, 307, 330, softbox('r')) + rec_timer() + f'''
<div style="position: absolute; top: 0; bottom: 0; left: 314px; width: 291px; box-shadow: 0 0 0 1400px rgba(6,5,5,.74); border: 4px solid #FF6A1A; box-sizing: border-box; z-index: 4; animation: aCrop 4s {E} infinite">
  <div style="position: absolute; left: 0; right: 0; top: 70px; text-align: center; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; color: #FF6A1A; animation: aLblOn 4s ease-in-out infinite">9:16 · REELS</div>
  <div style="position: absolute; left: 50%; bottom: 26px; {BRIC}; font-weight: 800; font-size: 26px; color: #fff; background: #FF3B30; padding: 10px 16px; border-radius: 12px; white-space: nowrap; animation: aCutOn 4s ease-in-out infinite">✂ CARA CORTADA</div>
</div>
<div style="position: absolute; right: 26px; bottom: 24px; padding: 10px 18px; border-radius: 12px; background: rgba(242,237,231,.92); color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; z-index: 5; opacity: 0; animation: aFullOn 4s ease-in-out infinite">16:9 · LO QUE GRABASTE</div>
'''
body1 = headline('FORMATO DE VÍDEO', 'Grabaste en horizontal…', 'y en Reels te cortó la cara.', 82) + f"""
<div style="position: relative; height: 660px; display: flex; flex-direction: column; gap: 20px">
  <div style="position: relative; height: 518px; border-radius: 26px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">{mon1}</div>
  <div style="position: relative; flex: 1; border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 0 28px; display: flex; align-items: center; gap: 26px">
    <div style="flex: none; {BRIC}; font-weight: 800; font-size: 36px; letter-spacing: -0.03em; line-height: 1">Pierdes <span style="{SERIF}; color: #FF6A1A; font-size: 44px">2/3</span> del plano</div>
    <div style="position: relative; flex: 1; height: 22px; border-radius: 99px; background: rgba(255,59,48,.25); overflow: hidden"><div style="position: absolute; left: 34.2%; top: 0; bottom: 0; height: 100%; border-radius: 99px; background: #FF6A1A; animation: aLose 4s {E} infinite"></div></div>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Cómo grabar una vez y que sirva en todas partes.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 CADA RED, UN FORMATO
kf2 = COMMON_KF + """
@keyframes aMorph{0%,26%{width:330px;height:586px}36%,59%{width:440px;height:550px}69%,92%{width:480px;height:270px}100%{width:330px;height:586px}}
@keyframes aF1{0%,28%{background:#1E1A17;border-color:#FF6A1A;transform:translateX(-8px)}34%,100%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}
@keyframes aF2{0%,32%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}37%,61%{background:#1E1A17;border-color:#FF6A1A;transform:translateX(-8px)}67%,100%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}
@keyframes aF3{0%,65%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}70%,94%{background:#1E1A17;border-color:#FF6A1A;transform:translateX(-8px)}100%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}
@keyframes aL1{0%,30%{opacity:1}33%,97%{opacity:0}100%{opacity:1}}
@keyframes aL2{0%,33%{opacity:0}36%,63%{opacity:1}66%,100%{opacity:0}}
@keyframes aL3{0%,66%{opacity:0}69%,96%{opacity:1}99%,100%{opacity:0}}
"""
labels2 = ''.join(f'<span style="position: absolute; left: 0; right: 0; text-align: center; opacity: 0; animation: {a} 4s linear infinite">{t}</span>' for t, a in (('9:16', 'aL1'), ('4:5', 'aL2'), ('16:9', 'aL3')))
rows2 = ''.join(
    f'<div style="display: flex; flex-direction: column; gap: 6px; padding: 20px 22px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s {E} infinite">'
    f'<span style="{MONO}; font-weight: 600; font-size: 24px; letter-spacing: .06em; color: #FF6A1A">{r}</span>'
    f'<span style="{BRIC}; font-weight: 800; font-size: 32px; letter-spacing: -0.02em; line-height: 1.02">{t}</span>'
    f'<span style="font-size: 22px; color: #B5ADA4">{d}</span></div>'
    for r, t, d, a in (('9:16 · VERTICAL', 'Reels, historias y TikTok', 'Pantalla completa en el móvil', 'aF1'),
                       ('4:5 · RETRATO', 'Publicación y anuncios del feed', 'Ocupa más feed que el cuadrado', 'aF2'),
                       ('16:9 · HORIZONTAL', 'YouTube y tu web', 'El de toda la vida', 'aF3')))
body2 = headline('EL PROBLEMA', 'Cada sitio pide', 'su propio formato.', 92) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: 500px; border-radius: 30px; background: #0A0908; border: 2px dashed rgba(242,237,231,.14); display: flex; flex-direction: column; align-items: center; justify-content: center">
    <div style="position: relative; width: 330px; height: 586px; border-radius: 20px; overflow: hidden; border: 4px solid #FF6A1A; box-shadow: 0 0 80px -10px rgba(255,106,26,.6); animation: aMorph 4s {E} infinite">
      <div style="position: absolute; left: 50%; top: 50%; width: 900px; height: 620px; margin-left: -450px; margin-top: -310px">{scene(900, 620, 450, 380)}</div>
      <div style="position: absolute; left: 0; right: 0; top: 14px; height: 60px; {BRIC}; font-weight: 800; font-size: 50px; letter-spacing: -0.03em; color: #fff; text-shadow: 0 3px 14px #000; z-index: 3">{labels2}</div>
    </div>
  </div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 18px">{rows2}</div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · El problema', 2, kf2, body2,
    'Si grabas sin pensarlo, recortas a ciegas.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 GRABA PARA EL RECORTE
kf3 = COMMON_KF + chk_kf(3, [8, 38, 68]) + """
@keyframes aBox{0%,20%{top:0;height:100%;border-color:rgba(242,237,231,.0)}30%,52%{top:15.7%;height:70%;border-color:#FF6A1A}62%,86%{top:20.4%;height:56%;border-color:#FF6A1A}96%,100%{top:0;height:100%;border-color:rgba(242,237,231,0)}}
@keyframes aB1{0%,22%{opacity:1}28%,94%{opacity:0}100%{opacity:1}}
@keyframes aB2{0%,26%{opacity:0}32%,54%{opacity:1}60%,100%{opacity:0}}
@keyframes aB3{0%,58%{opacity:0}64%,88%{opacity:1}94%,100%{opacity:0}}
@keyframes aAir{0%,100%{opacity:.55}50%{opacity:1}}
"""
vf_labels = ''.join(f'<div style="position: absolute; left: 50%; transform: translateX(-50%); bottom: 12px; white-space: nowrap; padding: 8px 14px; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .06em; opacity: 0; animation: {a} 4s linear infinite">✓ {t}</div>' for t, a in (('9:16 · REELS', 'aB1'), ('4:5 · FEED', 'aB2'), ('1:1 · CUADRADO', 'aB3')))
vf3 = scene(356, 636, 178, 300, tall=True) + f'''
<div style="position: absolute; left: 0; right: 0; top: 0; height: 21%; border-bottom: 3px dashed rgba(255,106,26,.7); background: rgba(255,106,26,.08); animation: aAir 2s ease-in-out infinite; display: flex; align-items: flex-end; padding-bottom: 12px; box-sizing: border-box; justify-content: center; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; color: #FF8F45">↕ AIRE</div>
<div style="position: absolute; left: 33.3%; top: 0; bottom: 0; border-left: 1px solid rgba(242,237,231,.25)"></div><div style="position: absolute; left: 66.6%; top: 0; bottom: 0; border-left: 1px solid rgba(242,237,231,.25)"></div>
<div style="position: absolute; top: 33.3%; left: 0; right: 0; border-top: 1px solid rgba(242,237,231,.25)"></div><div style="position: absolute; top: 66.6%; left: 0; right: 0; border-top: 1px solid rgba(242,237,231,.25)"></div>
<div style="position: absolute; left: 0; right: 0; top: 0; height: 100%; border: 4px solid transparent; box-sizing: border-box; box-shadow: 0 0 0 900px rgba(6,5,5,.62); z-index: 4; animation: aBox 4s {E} infinite">{vf_labels}</div>
{rec_timer().replace('left: 70px', 'left: 22px').replace('right: 70px', 'right: 22px')}
<div style="position: absolute; inset: 12px; z-index: 5">{corners('rgba(242,237,231,.6)')}</div>
'''
body3 = headline('TRUCO 01 · GRABA PARA EL RECORTE', 'Vertical y con aire:', 'de ahí salen todos.', 88) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 26px">
  <div style="position: relative; flex: none; width: 380px; height: 660px; border-radius: 30px; overflow: hidden; background: #050505; padding: 12px; box-sizing: border-box; box-shadow: 0 0 0 3px rgba(242,237,231,.18), 0 50px 120px -30px rgba(255,106,26,.55)">
    <div style="position: relative; width: 356px; height: 636px; border-radius: 20px; overflow: hidden">{vf3}</div>
  </div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 16px">
    <div style="border-radius: 26px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 24px; display: flex; flex-direction: column; gap: 12px">
      <span style="{MONO}; font-size: 19px; letter-spacing: .1em; color: #9C938B">ANTES DE DARLE A REC</span>
      {ticklist(['Cara en el centro, no a un lado', 'Aire por encima de la cabeza', 'Nada importante en los bordes'], [('a3Row1', 'a3Tk1'), ('a3Row2', 'a3Tk2'), ('a3Row3', 'a3Tk3')])}
    </div>
    <div style="flex: 1; border-radius: 26px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 26px; display: flex; flex-direction: column; justify-content: center; gap: 12px">
      <span style="{MONO}; font-size: 19px; letter-spacing: .1em; color: #9C938B">POR QUÉ FUNCIONA</span>
      <span style="{BRIC}; font-weight: 800; font-size: 38px; line-height: 1.06; letter-spacing: -0.03em">Recortar un vertical <span style="{SERIF}; color: #FF6A1A">no te corta la cara.</span></span>
      <span style="font-size: 24px; line-height: 1.3; color: #B5ADA4">El 4:5 y el cuadrado caben dentro sin tocar lo importante.</span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Graba para el recorte', 3, kf3, body3,
    'Un encuadre bien pensado = varios formatos.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 EXPORTA UNA VERSIÓN POR FORMATO
kf4 = COMMON_KF + """
@keyframes aP1{0%,4%{width:0%}26%,94%{width:100%}100%{width:0%}}
@keyframes aP2{0%,28%{width:0%}50%,94%{width:100%}100%{width:0%}}
@keyframes aP3{0%,52%{width:0%}74%,94%{width:100%}100%{width:0%}}
@keyframes aD1{0%,25%{transform:scale(0)}29%{transform:scale(1.3)}32%,94%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aD2{0%,49%{transform:scale(0)}53%{transform:scale(1.3)}56%,94%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aD3{0%,73%{transform:scale(0)}77%{transform:scale(1.3)}80%,94%{transform:scale(1)}100%{transform:scale(0)}}
@keyframes aFit{0%,40%{height:170px}56%,92%{height:100%}100%{height:170px}}
@keyframes aZoom{0%,40%{transform:scale(.336)}56%,92%{transform:scale(1.25)}100%{transform:scale(.336)}}
@keyframes aBad{0%,38%{opacity:1}46%,94%{opacity:0}100%{opacity:1}}
@keyframes aGood{0%,50%{opacity:0}58%,92%{opacity:1}100%{opacity:0}}
@keyframes aSub{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
"""
exp_rows = ''.join(
    f'''<div style="display: flex; flex-direction: column; gap: 10px">
  <div style="display: flex; align-items: center; justify-content: space-between">
    <span style="display: flex; align-items: baseline; gap: 14px"><span style="{BRIC}; font-weight: 800; font-size: 34px; letter-spacing: -0.02em">{r}</span><span style="font-size: 22px; color: #B5ADA4">{d}</span></span>
    <span style="width: 38px; height: 38px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 22px; transform: scale(0); animation: {dk} 4s ease-out infinite">✓</span>
  </div>
  <div style="position: relative; height: 16px; border-radius: 99px; background: rgba(242,237,231,.1); overflow: hidden"><div style="position: absolute; left: 0; top: 0; bottom: 0; width: 0; border-radius: 99px; background: linear-gradient(90deg, #FF6A1A, #FFB27A); animation: {pk} 4s {E} infinite"></div></div>
</div>''' for r, d, pk, dk in (('9:16', 'Reels &nbsp;·&nbsp; historias', 'aP1', 'aD1'), ('4:5', 'Feed &nbsp;·&nbsp; anuncios', 'aP2', 'aD2'), ('16:9', 'YouTube &nbsp;·&nbsp; web', 'aP3', 'aD3')))
ph4 = f'''<div style="position: absolute; inset: 0; background: #000"></div>
<div style="position: absolute; left: 0; right: 0; top: 50%; transform: translateY(-50%); height: 170px; overflow: hidden; animation: aFit 4s {E} infinite">
  <div style="position: absolute; left: 50%; top: 50%; width: 900px; height: 506px; margin-left: -450px; margin-top: -253px; transform: scale(.336); animation: aZoom 4s {E} infinite">{scene(900, 506, 450, 300)}</div>
</div>
<div style="position: absolute; left: 16px; right: 16px; top: 72%; text-align: center; z-index: 5"><span style="display: inline-block; padding: 8px 14px; border-radius: 10px; background: rgba(6,5,5,.72); {BRIC}; font-weight: 800; font-size: 26px; color: #fff; animation: aSub 2s ease-in-out infinite">Subtítulos al centro</span></div>
<div style="position: absolute; left: 50%; top: 70px; transform: translateX(-50%); white-space: nowrap; padding: 9px 16px; border-radius: 12px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .06em; z-index: 6; animation: aBad 4s linear infinite">✕ FRANJAS NEGRAS</div>
<div style="position: absolute; left: 50%; top: 70px; transform: translateX(-50%); white-space: nowrap; padding: 9px 16px; border-radius: 12px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .06em; z-index: 6; opacity: 0; animation: aGood 4s linear infinite">✓ PANTALLA COMPLETA</div>'''
body4 = headline('TRUCO 02 · UNA VERSIÓN POR FORMATO', 'Exporta cada formato,', 'no lo metas a presión.', 84) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 26px">
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 18px">
    <div style="position: relative; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,0.14); box-shadow: 0 50px 120px -40px rgba(255,106,26,0.5); padding: 28px; display: flex; flex-direction: column; gap: 26px">
      <div style="display: flex; justify-content: space-between; {MONO}; font-size: 19px; letter-spacing: .1em; color: #9C938B"><span>EXPORTAR · MISMO VÍDEO</span><span style="display: flex; align-items: center; gap: 8px; color: #FF8F45"><span style="width: 18px; height: 18px; border-radius: 99px; border: 3px solid rgba(242,237,231,.2); border-top-color: #FF6A1A; animation: aSpin 1s linear infinite"></span>EN COLA</span></div>
      {exp_rows}
    </div>
    <div style="flex: 1; border-radius: 26px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 24px 26px; display: flex; flex-direction: column; justify-content: center; gap: 10px">
      <span style="{MONO}; font-size: 19px; letter-spacing: .1em; color: #9C938B">Y EN CADA VERSIÓN</span>
      <span style="{BRIC}; font-weight: 800; font-size: 40px; line-height: 1.08; letter-spacing: -0.03em">Reencuadra y deja textos y subtítulos <span style="{SERIF}; color: #FF6A1A">en el centro.</span></span>
    </div>
  </div>
  {phone(330, 660, ph4, 'flex: none')}
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Exporta cada formato', 4, kf4.replace('@keyframes aSub', '@keyframes aSpin{to{transform:rotate(360deg)}}\n@keyframes aSub'), body4,
    'Nada de estirar ni de franjas negras.', DESLIZA_TXT))

# ---------------------------------------------------------------- 05 CTA
kf5 = COMMON_KF + """
@keyframes aHi1{0%,30%{border-color:#FF6A1A;box-shadow:0 0 50px rgba(255,106,26,.6);transform:translateY(-10px)}36%,100%{border-color:rgba(242,237,231,.2);box-shadow:none;transform:none}}
@keyframes aHi2{0%,33%{border-color:rgba(242,237,231,.2);box-shadow:none;transform:none}39%,63%{border-color:#FF6A1A;box-shadow:0 0 50px rgba(255,106,26,.6);transform:translateY(-10px)}69%,100%{border-color:rgba(242,237,231,.2);box-shadow:none;transform:none}}
@keyframes aHi3{0%,66%{border-color:rgba(242,237,231,.2);box-shadow:none;transform:none}72%,94%{border-color:#FF6A1A;box-shadow:0 0 50px rgba(255,106,26,.6);transform:translateY(-10px)}100%{border-color:rgba(242,237,231,.2);box-shadow:none;transform:none}}
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
@keyframes aFol{0%,46%{opacity:1}50%,100%{opacity:0}}
@keyframes aFolD{0%,46%{opacity:0}50%,100%{opacity:1}}
@keyframes aFolBg{0%,46%{background:#FF6A1A;color:#0A0908}50%,100%{background:#1E1A17;color:#F2EDE7}}
@keyframes aTap{0%,36%{opacity:0;transform:scale(1.4)}42%{opacity:1;transform:scale(1)}48%{opacity:1;transform:scale(.85)}56%,100%{opacity:0;transform:scale(1)}}
"""
frames5 = ''.join(
    f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 14px">
  <div style="position: relative; width: {w}px; height: {h}px; border-radius: 18px; overflow: hidden; border: 4px solid rgba(242,237,231,.2); animation: {a} 4s {E} infinite">
    <div style="position: absolute; left: 50%; top: 50%; width: 900px; height: 620px; margin-left: -450px; margin-top: -310px; transform: scale({sc}); transform-origin: 50% 50%">{scene(900, 620, 450, 380)}</div>
  </div>
  <span style="{MONO}; font-weight: 600; font-size: 24px; letter-spacing: .08em; color: #F2EDE7">{r}</span>
</div>''' for w, h, sc, r, a in ((190, 338, .56, '9:16', 'aHi1'), (256, 320, .55, '4:5', 'aHi2'), (360, 203, .42, '16:9', 'aHi3')))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 86px; line-height: 1; letter-spacing: -0.045em">Graba pensando<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">dónde se va a ver.</span></p>
<div style="position: relative; margin-top: 40px; width: 920px; height: 470px; border-radius: 30px; background: #0A0908; border: 2px dashed rgba(242,237,231,.14); display: flex; align-items: flex-end; justify-content: center; gap: 34px; padding-bottom: 34px; box-sizing: border-box">{frames5}</div>
<div style="position: relative; margin-top: 30px; display: flex; align-items: center; gap: 22px; padding: 18px 22px 18px 18px; border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14)">
  <img src="{LOGO}" style="width: 64px; height: 64px; border-radius: 99px; animation: aLogo 4s ease-in-out infinite">
  <span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em">@ceos.productions</span>
  <span style="position: relative; width: 190px; height: 58px; border-radius: 14px; {BRIC}; font-weight: 800; font-size: 28px; animation: aFolBg 4s steps(1) infinite; display: flex; align-items: center; justify-content: center">
    <span style="position: absolute; animation: aFol 4s steps(1) infinite">Seguir</span><span style="position: absolute; opacity: 0; animation: aFolD 4s steps(1) infinite">Siguiendo ✓</span>
    <span style="position: absolute; right: -14px; bottom: -22px; width: 56px; height: 56px; border-radius: 99px; background: rgba(242,237,231,.35); border: 3px solid #F2EDE7; opacity: 0; animation: aTap 4s ease-out infinite"></span>
  </span>
</div>
<div style="position: relative; overflow: hidden; margin-top: 30px; padding: 26px 54px; border-radius: 30px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 64px; line-height: 1; letter-spacing: -0.04em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Síguenos para más tips<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.3), rgba(255,255,255,0)); animation: aShim 4s ease-in-out 0.6s infinite"></div></div>
</div>
"""
open(os.path.join(OUT, 'S5.dc.html'), 'w').write(page('05 · CTA', 5, kf5, body5,
    'Guárdalo para tu próxima grabación.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
