#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C1 2026-10-10 (encuadre a cámara: 3 reglas) en src/."""
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




# ============================================================ C1 2026-10-10 · Encuadre a cámara: 3 reglas
def tall_person(w, uid):
    """Busto de estudio (viewBox 420x700): cabeza arriba en y=33, ojos en y=122, cuerpo hasta abajo."""
    h = round(w * 700 / 420)
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 420 700" style="display:block">
<defs><linearGradient id="tp{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F2EDE7" stop-opacity=".97"/><stop offset="1" stop-color="#B5ADA4" stop-opacity=".6"/></linearGradient></defs>
<path d="M8 700 L8 400 C8 300 96 262 210 262 C324 262 412 300 412 400 L412 700 Z" fill="url(#tp{uid})"/>
<rect x="178" y="196" width="64" height="80" rx="26" fill="url(#tp{uid})"/>
<ellipse cx="210" cy="125" rx="78" ry="92" fill="url(#tp{uid})"/>
<rect x="168" y="118" width="18" height="8" rx="4" fill="#0A0908" opacity=".55"/><rect x="234" y="118" width="18" height="8" rx="4" fill="#0A0908" opacity=".55"/>
<path d="M190 172 Q210 184 230 172" fill="none" stroke="#0A0908" stroke-width="5" stroke-linecap="round" opacity=".35"/>
</svg>'''


def grid(w, h, op='.16'):
    c = f'rgba(242,237,231,{op})'
    return (f'<div style="position: absolute; left: 0; right: 0; top: {h/3:.1f}px; height: 2px; background: {c}; z-index: 4"></div>'
            f'<div style="position: absolute; left: 0; right: 0; top: {2*h/3:.1f}px; height: 2px; background: {c}; z-index: 4"></div>'
            f'<div style="position: absolute; top: 0; bottom: 0; left: {w/3:.1f}px; width: 2px; background: {c}; z-index: 4"></div>'
            f'<div style="position: absolute; top: 0; bottom: 0; left: {2*w/3:.1f}px; width: 2px; background: {c}; z-index: 4"></div>')


def studio_bg(glow=True, gx='50%'):
    g = (f'<div style="position: absolute; left: {gx}; top: 2%; width: 74%; height: 96%; margin-left: -37%; border-radius: 50%; '
         f'background: radial-gradient(circle, rgba(255,106,26,.32), rgba(255,106,26,0) 70%); animation: aGlow 4s ease-in-out infinite"></div>') if glow else ''
    return f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #1C130D 0%, #12100F 70%, #0A0908 100%)"></div>{g}'''


def tag(txt, pos, bg='#FF3B30', fg='#fff', anim=''):
    a = f'; animation: {anim}' if anim else ''
    return (f'<div style="position: absolute; {pos}; white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: {bg}; color: {fg}; '
            f'{MONO}; font-weight: 600; font-size: 21px; letter-spacing: .08em; z-index: 8{a}">{txt}</div>')


# ---------------------------------------------------------------- 01 GANCHO · antes/después con cortinilla
FW, FH = 916, 500
kf1 = COMMON_KF + """
@keyframes aWipe{0%{clip-path:inset(0 0 0 84%)}45%,55%{clip-path:inset(0 0 0 16%)}100%{clip-path:inset(0 0 0 84%)}}
@keyframes aDiv{0%{left:84%}45%,55%{left:16%}100%{left:84%}}
@keyframes aHL{0%,14%,86%,100%{background:#1E1A17;border-color:#FF3B30;transform:translateY(-4px)}34%,66%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}
@keyframes aHR{0%,14%,86%,100%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}34%,66%{background:#1E1A17;border-color:#FF6A1A;transform:translateY(-4px)}}
@keyframes aEyeGlow{0%,100%{box-shadow:0 0 10px 1px rgba(255,106,26,.6)}50%{box-shadow:0 0 26px 5px rgba(255,106,26,1)}}
@keyframes aHandle{0%,100%{transform:translate(-50%,-50%) scale(1)}50%{transform:translate(-50%,-50%) scale(1.12)}}
"""
wa, wb = 300, 470
topA, topB = 163, 30
layerA = studio_bg(False) + f'''
<div style="position: absolute; left: {FW/2 - wa/2:.0f}px; top: {topA}px; width: {wa}px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{tall_person(wa, 'a1')}</div>
<div style="position: absolute; left: 0; right: 0; top: 250px; border-top: 3px dashed #FF3B30; z-index: 5"></div>
<div style="position: absolute; left: 24px; top: 262px; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .1em; color: #FF3B30; z-index: 5">OJOS · CENTRO</div>
<div style="position: absolute; left: {FW/2 - 4}px; top: 196px; width: 8px; height: 0; z-index: 5"></div>
'''
layerB = studio_bg(True) + f'''
<div style="position: absolute; left: {FW/2 - wb/2:.0f}px; top: {topB}px; width: {wb}px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{tall_person(wb, 'b1')}</div>
<div style="position: absolute; left: 0; right: 0; top: {FH/3 - 1.5:.1f}px; height: 3px; background: #FF6A1A; z-index: 5; animation: aEyeGlow 2s ease-in-out infinite"></div>
<div style="position: absolute; right: 24px; top: {FH/3 + 12:.0f}px; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .1em; color: #FF6A1A; z-index: 5">OJOS · LÍNEA DE ARRIBA</div>
'''
frame1 = f'''<div style="position: absolute; inset: 0; z-index: 1">{layerA}</div>
<div style="position: absolute; inset: 0; animation: aWipe 4s cubic-bezier(.65,0,.35,1) infinite; z-index: 3">{layerB}</div>
{grid(FW, FH)}
<div style="position: absolute; top: 0; bottom: 0; width: 4px; margin-left: -2px; background: #F2EDE7; box-shadow: 0 0 24px rgba(242,237,231,.7); z-index: 7; animation: aDiv 4s cubic-bezier(.65,0,.35,1) infinite">
  <div style="position: absolute; left: 50%; top: 50%; width: 64px; height: 64px; border-radius: 99px; background: #F2EDE7; display: flex; align-items: center; justify-content: center; gap: 4px; box-shadow: 0 10px 30px rgba(0,0,0,.5); animation: aHandle 2s ease-in-out infinite">
    <svg width="34" height="20" viewBox="0 0 34 20"><path d="M10 3 L3 10 L10 17 M24 3 L31 10 L24 17" fill="none" stroke="#0A0908" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
</div>
{tag('✕ CASERO', 'left: 24px; bottom: 24px')}
{tag('✓ DE ESTUDIO', 'right: 24px; bottom: 24px', '#FF6A1A', '#0A0908')}
{rec_timer()}'''
body1 = headline('ENCUADRE A CÁMARA', '¿Tu vídeo parece casero?', 'Mira dónde están tus ojos.', 84) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 18px">
  <div style="position: relative; width: {FW}px; height: {FH}px; border-radius: 26px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">{frame1}</div>
  <div style="display: flex; gap: 18px">
    <div style="flex: 1; padding: 20px 24px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: aHL 4s cubic-bezier(.65,0,.35,1) infinite">
      <span style="{MONO}; font-weight: 600; font-size: 19px; letter-spacing: .08em; color: #FF3B30">✕ LO HABITUAL</span><br>
      <span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em">Ojos en el centro</span></div>
    <div style="flex: 1; padding: 20px 24px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: aHR 4s cubic-bezier(.65,0,.35,1) infinite">
      <span style="{MONO}; font-weight: 600; font-size: 19px; letter-spacing: .08em; color: #FF6A1A">✓ LO QUE HACEMOS</span><br>
      <span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em">Ojos en la línea de arriba</span></div>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Misma cámara, mismo sitio: 3 reglas de encuadre.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 REGLA 01 · OJOS ARRIBA (móvil con cuadrícula)
PW, PH = 372, 612
kf2 = COMMON_KF + chk_kf(2, [8, 38, 68]) + """
@keyframes aGh1{0%,4%{transform:scaleX(0)}14%,92%{transform:scaleX(1)}100%{transform:scaleX(0)}}
@keyframes aGh2{0%,8%{transform:scaleX(0)}18%,92%{transform:scaleX(1)}100%{transform:scaleX(0)}}
@keyframes aGv1{0%,12%{transform:scaleY(0)}22%,92%{transform:scaleY(1)}100%{transform:scaleY(0)}}
@keyframes aGv2{0%,16%{transform:scaleY(0)}26%,92%{transform:scaleY(1)}100%{transform:scaleY(0)}}
@keyframes aRise{0%,28%{transform:translateY(96px)}46%,90%{transform:translateY(0)}100%{transform:translateY(96px)}}
@keyframes aTop{0%,42%{background:rgba(242,237,231,.6);box-shadow:none}50%,90%{background:#FF6A1A;box-shadow:0 0 22px 2px #FF6A1A}100%{background:rgba(242,237,231,.6);box-shadow:none}}
@keyframes aDot{0%,44%{transform:translate(-50%,-50%) scale(0)}50%{transform:translate(-50%,-50%) scale(1.4)}56%,90%{transform:translate(-50%,-50%) scale(1)}100%{transform:translate(-50%,-50%) scale(0)}}
@keyframes aOjos{0%,46%{opacity:0;transform:translateX(16px)}54%,90%{opacity:1;transform:none}100%{opacity:0}}
@keyframes aKnob{0%,3%{left:4px}9%,94%{left:30px}100%{left:4px}}
@keyframes aSw{0%,3%{background:#3A3530}9%,94%{background:#FF6A1A}100%{background:#3A3530}}
@keyframes aKey{0%,100%{box-shadow:0 0 0 rgba(255,106,26,0)}50%{box-shadow:0 0 60px -6px rgba(255,106,26,.55)}}
"""
wp = 360
inner2 = studio_bg(True) + f'''
<div style="position: absolute; left: {(PW - wp)/2:.0f}px; top: {PH/3 - 122*wp/420:.0f}px; width: {wp}px; z-index: 2; animation: aRise 4s cubic-bezier(.65,0,.35,1) infinite">{tall_person(wp, 'p2')}</div>
<div style="position: absolute; left: 0; right: 0; top: {PH/3 - 1.5:.1f}px; height: 3px; transform-origin: 0 50%; z-index: 5; animation: aGh1 4s {E} infinite, aTop 4s ease-in-out infinite"></div>
<div style="position: absolute; left: 0; right: 0; top: {2*PH/3:.1f}px; height: 2px; background: rgba(242,237,231,.6); transform-origin: 0 50%; z-index: 5; animation: aGh2 4s {E} infinite"></div>
<div style="position: absolute; top: 0; bottom: 0; left: {PW/3:.1f}px; width: 2px; background: rgba(242,237,231,.6); transform-origin: 50% 0; z-index: 5; animation: aGv1 4s {E} infinite"></div>
<div style="position: absolute; top: 0; bottom: 0; left: {2*PW/3:.1f}px; width: 2px; background: rgba(242,237,231,.6); transform-origin: 50% 0; z-index: 5; animation: aGv2 4s {E} infinite"></div>
<div style="position: absolute; left: {PW/3:.1f}px; top: {PH/3:.1f}px; width: 22px; height: 22px; border-radius: 99px; background: #FF6A1A; border: 3px solid #F2EDE7; z-index: 6; animation: aDot 4s ease-out infinite"></div>
<div style="position: absolute; left: {2*PW/3:.1f}px; top: {PH/3:.1f}px; width: 22px; height: 22px; border-radius: 99px; background: #FF6A1A; border: 3px solid #F2EDE7; z-index: 6; animation: aDot 4s ease-out infinite"></div>
<div style="position: absolute; right: 12px; top: {PH/3 - 52:.0f}px; padding: 6px 12px; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 17px; letter-spacing: .08em; z-index: 7; animation: aOjos 4s ease-out infinite">OJOS AQUÍ</div>
<div style="position: absolute; left: 16px; right: 16px; top: 54px; height: 50px; border-radius: 14px; background: rgba(10,9,8,.78); border: 1px solid rgba(242,237,231,.16); display: flex; align-items: center; justify-content: space-between; padding: 0 14px; z-index: 8">
  <span style="{MONO}; font-weight: 600; font-size: 17px; letter-spacing: .1em; color: #F2EDE7">CUADRÍCULA</span>
  <span style="position: relative; width: 58px; height: 32px; border-radius: 99px; animation: aSw 4s ease-in-out infinite"><span style="position: absolute; top: 4px; width: 24px; height: 24px; border-radius: 99px; background: #F2EDE7; animation: aKnob 4s ease-in-out infinite"></span></span>
</div>
'''
body2 = headline('REGLA 01 · OJOS ARRIBA', 'Divide la pantalla en 3.', 'Tus ojos, en la línea de arriba.', 72) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 30px; align-items: center">
  <div style="flex: none">{phone(400, 640, inner2)}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 18px">
    <div style="border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 20px 18px; display: flex; flex-direction: column; gap: 12px">
      <span style="{MONO}; font-size: 18px; letter-spacing: .12em; color: #9C938B; padding-left: 4px">PASO A PASO</span>
      {ticklist(['Activa la cuadrícula de la cámara', 'Sube o baja el móvil hasta que tus ojos toquen la línea de arriba', 'Cara en el centro si hablas a cámara'], [('a2Row1', 'a2Tk1'), ('a2Row2', 'a2Tk2'), ('a2Row3', 'a2Tk3')])}
    </div>
    <div style="padding: 20px 24px; border-radius: 22px; background: #0A0908; border: 2px dashed #FF6A1A; animation: aKey 4s ease-in-out infinite">
      <span style="{BRIC}; font-weight: 800; font-size: 27px; letter-spacing: -0.02em; line-height: 1.15">Está en los ajustes de la cámara de cualquier móvil: busca <span style="{SERIF}; color: #FF6A1A; font-size: 33px">«Cuadrícula»</span>.</span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Ojos arriba', 2, kf2, body2,
    'Vale igual en vertical que en horizontal.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 REGLA 02 · POCO AIRE (zoom y medidor de aire)
VW, VH = 470, 640
kf3 = COMMON_KF + """
@keyframes aZoom{0%,26%{transform:translateY(200px) scale(1)}44%,84%{transform:translateY(3px) scale(1.9)}100%{transform:translateY(200px) scale(1)}}
@keyframes aBr{0%,26%{height:230px}44%,84%{height:60px}100%{height:230px}}
@keyframes aBrC{0%,30%{border-color:#FF3B30}40%,84%{border-color:#FF6A1A}96%,100%{border-color:#FF3B30}}
@keyframes aA1{0%,30%{opacity:1}36%,88%{opacity:0}96%,100%{opacity:1}}
@keyframes aA2{0%,34%{opacity:0}42%,84%{opacity:1}90%,100%{opacity:0}}
@keyframes aR1{0%,26%{background:#1E1A17;border-color:#FF3B30;transform:translateX(-8px)}34%,88%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}96%,100%{background:#1E1A17;border-color:#FF3B30;transform:translateX(-8px)}}
@keyframes aR2{0%,36%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}44%,84%{background:#1E1A17;border-color:#FF6A1A;transform:translateX(-8px)}92%,100%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}
@keyframes aWarm{0%,100%{opacity:.6}50%{opacity:1}}
"""
wz = 380
panel3 = studio_bg(True) + f'''
<div style="position: absolute; left: {VW/2 - wz/2:.0f}px; top: 0; width: {wz}px; transform-origin: 50% 0; z-index: 2; animation: aZoom 4s cubic-bezier(.65,0,.35,1) infinite">{tall_person(wz, 'z3')}</div>
{grid(VW, VH, '.14')}
<div style="position: absolute; left: 34px; top: 0; width: 26px; z-index: 6; animation: aBr 4s cubic-bezier(.65,0,.35,1) infinite">
  <div style="position: absolute; left: 11px; top: 0; bottom: 0; width: 4px; background: #F2EDE7"></div>
  <div style="position: absolute; left: 0; right: 0; bottom: -4px; height: 4px; background: #F2EDE7"></div>
  <div style="position: absolute; left: 40px; bottom: -22px; white-space: nowrap; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .1em; color: #F2EDE7; background: rgba(10,9,8,.7); padding: 4px 8px; border-radius: 6px">AIRE</div>
</div>
{tag('✕ MUCHO AIRE', 'right: 22px; bottom: 22px', anim='aA1 4s ease-in-out infinite')}
{tag('✓ UN DEDO DE AIRE', 'right: 22px; bottom: 22px; opacity: 0', '#FF6A1A', '#0A0908', 'aA2 4s ease-in-out infinite')}
{corners()}'''
rows3 = ''.join(
    f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 22px 24px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s {E} infinite">'
    f'<span style="{MONO}; font-weight: 600; font-size: 21px; letter-spacing: .08em; color: {c}">{r}</span>'
    f'<span style="{BRIC}; font-weight: 800; font-size: 31px; letter-spacing: -0.02em; line-height: 1.04">{t}</span>'
    f'<span style="font-size: 22px; color: #B5ADA4; line-height: 1.25">{d}</span></div>'
    for r, c, t, d, a in (('✕ MUCHO AIRE', '#FF3B30', 'Pareces pequeño y lejos', 'La pantalla se llena de pared y techo', 'aR1'),
                          ('✓ UN DEDO DE AIRE', '#FF6A1A', 'Llenas la pantalla', 'Se ven mejor tu cara y tus gestos', 'aR2')))
body3 = headline('REGLA 02 · POCO AIRE', 'Deja muy poco espacio', 'sobre tu cabeza.', 78) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: {VW}px; height: {VH}px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.55)">{panel3}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 16px">{rows3}
    <div style="border-radius: 22px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 20px 22px; display: flex; gap: 14px; align-items: flex-start">
      <span style="flex: none; width: 42px; height: 42px; border-radius: 12px; background: rgba(255,106,26,.16); border: 2px solid #FF6A1A; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 25px; color: #FF6A1A; animation: aWarm 2s ease-in-out infinite">!</span>
      <span style="font-size: 22px; color: #D9D1C8; line-height: 1.3">Acerca el móvil en vez de hacer zoom: el <b style="color: #F2EDE7">zoom digital</b> (ampliar con los dedos) pierde calidad.</span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Poco aire', 3, kf3, body3,
    'Más cerca = más presencia en pantalla.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 REGLA 03 · CORTA BIEN (línea de corte que recorre el cuerpo)
kf4 = COMMON_KF + """
@keyframes aCut{0%,21%{top:170px}25%,46%{top:240px}50%,71%{top:460px}75%,96%{top:390px}100%{top:170px}}
@keyframes aLc{0%,24.9%{border-color:#FF3B30}25%,49.9%{border-color:#FF6A1A}50%,74.9%{border-color:#FF3B30}75%,100%{border-color:#FF6A1A}}
@keyframes aChip{0%,100%{transform:scale(1)}8%{transform:scale(1.12)}16%{transform:scale(1)}}
@keyframes aKey{0%,100%{box-shadow:0 0 0 rgba(255,106,26,0)}50%{box-shadow:0 0 60px -6px rgba(255,106,26,.55)}}
@keyframes aJ{0%,100%{transform:translate(-50%,-50%) scale(.8);opacity:.5}50%{transform:translate(-50%,-50%) scale(1.25);opacity:1}}
"""
cut_labels = cycle([
    '<span style="background: #FF3B30; color: #fff; padding: 8px 14px; border-radius: 10px">✕ CUELLO</span>',
    '<span style="background: #FF6A1A; color: #0A0908; padding: 8px 14px; border-radius: 10px">✓ PECHO</span>',
    '<span style="background: #FF3B30; color: #fff; padding: 8px 14px; border-radius: 10px">✕ RODILLAS</span>',
    '<span style="background: #FF6A1A; color: #0A0908; padding: 8px 14px; border-radius: 10px">✓ MITAD DEL MUSLO</span>'],
    f'{MONO}; font-weight: 600; font-size: 19px; letter-spacing: .08em; white-space: nowrap; text-align: right')
joints = ''.join(
    f'<div style="position: absolute; left: {x}px; top: {y}px; width: 18px; height: 18px; border-radius: 99px; border: 3px solid #FF3B30; z-index: 4; animation: aJ 2s ease-in-out {d}s infinite"></div>'
    for x, y, d in ((150 + 40, 160, 0), (88 + 40, 280, .3), (212 + 40, 280, .3), (90 + 40, 372, .6), (210 + 40, 372, .6), (127 + 40, 460, .9), (173 + 40, 460, .9)))
panel4 = studio_bg(True) + f'''
<div style="position: absolute; left: 40px; top: 30px; z-index: 2">{figure(300, 'f4')}</div>
{joints}
<div style="position: absolute; left: 0; right: 0; top: 170px; bottom: -10px; z-index: 5; animation: aCut 4s cubic-bezier(.65,0,.35,1) infinite">
  <div style="position: absolute; inset: 0; background: rgba(10,9,8,.74); border-top: 5px dashed #FF3B30; animation: aLc 4s steps(1) infinite"></div>
  <div style="position: absolute; right: 18px; top: -50px; left: 18px; height: 40px">{cut_labels}</div>
</div>
<div style="position: absolute; left: 18px; top: 18px; {MONO}; font-size: 17px; letter-spacing: .12em; color: #9C938B; z-index: 6">BORDE INFERIOR DEL PLANO</div>
'''


def chips(items, col, fg, delay0):
    return ''.join(
        f'<span style="display: inline-block; padding: 10px 16px; border-radius: 12px; border: 2px solid {col}; color: {fg}; {BRIC}; font-weight: 700; font-size: 25px; '
        f'animation: aChip 4s ease-in-out {delay0 + i*0.5:.1f}s infinite">{t}</span>' for i, t in enumerate(items))


body4 = headline('REGLA 03 · CORTA BIEN', 'Nunca cortes el plano', 'justo en una articulación.', 74) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: 420px; height: 650px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.55)">{panel4}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 18px">
    <div style="padding: 22px 22px; border-radius: 22px; background: #12100F; border: 2px solid rgba(242,237,231,.14); display: flex; flex-direction: column; gap: 14px">
      <span style="{MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; color: #FF3B30">✕ NO CORTES EN</span>
      <div style="display: flex; flex-wrap: wrap; gap: 10px">{chips(['Cuello', 'Codos', 'Muñecas', 'Rodillas', 'Tobillos'], '#FF3B30', '#F2EDE7', 0)}</div>
    </div>
    <div style="padding: 22px 22px; border-radius: 22px; background: #12100F; border: 2px solid rgba(242,237,231,.14); display: flex; flex-direction: column; gap: 14px">
      <span style="{MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; color: #FF6A1A">✓ CORTA EN</span>
      <div style="display: flex; flex-wrap: wrap; gap: 10px">{chips(['Pecho', 'Cintura', 'Mitad del muslo'], '#FF6A1A', '#F2EDE7', 2.5)}</div>
    </div>
    <div style="padding: 20px 24px; border-radius: 22px; background: #0A0908; border: 2px dashed #FF6A1A; animation: aKey 4s ease-in-out infinite">
      <span style="{BRIC}; font-weight: 800; font-size: 26px; letter-spacing: -0.02em; line-height: 1.15">Si cortas encima de una articulación, parece que <span style="{SERIF}; color: #FF6A1A; font-size: 32px">te falta un trozo.</span></span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Corta bien', 4, kf4, body4,
    'Corta entre articulaciones, nunca encima.', DESLIZA_TXT))

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
@keyframes aI1{0%,20%{transform:translateY(22px)}50%,80%{transform:translateY(0)}100%{transform:translateY(22px)}}
@keyframes aI2{0%,20%{transform:scale(.62)}50%,80%{transform:scale(1)}100%{transform:scale(.62)}}
@keyframes aI3{0%,100%{top:22px}50%{top:70px}}
"""
icon1 = f'''<div style="position: relative; width: 120px; height: 120px; border-radius: 12px; border: 2px solid rgba(242,237,231,.4); overflow: hidden">
<div style="position: absolute; left: 0; right: 0; top: 40px; height: 3px; background: #FF6A1A"></div>
<div style="position: absolute; left: 0; right: 0; top: 80px; height: 2px; background: rgba(242,237,231,.35)"></div>
<div style="position: absolute; top: 0; bottom: 0; left: 40px; width: 2px; background: rgba(242,237,231,.35)"></div>
<div style="position: absolute; top: 0; bottom: 0; left: 80px; width: 2px; background: rgba(242,237,231,.35)"></div>
<div style="position: absolute; left: 36px; top: 30px; width: 48px; height: 20px; display: flex; justify-content: space-between; animation: aI1 2s cubic-bezier(.65,0,.35,1) infinite"><span style="width: 14px; height: 14px; margin-top: 3px; border-radius: 99px; background: #F2EDE7"></span><span style="width: 14px; height: 14px; margin-top: 3px; border-radius: 99px; background: #F2EDE7"></span></div></div>'''
icon2 = f'''<div style="position: relative; width: 120px; height: 120px; border-radius: 12px; border: 2px solid rgba(242,237,231,.4); overflow: hidden">
<div style="position: absolute; left: 10px; right: 10px; top: 14px; bottom: -40px; transform-origin: 50% 100%; animation: aI2 2s cubic-bezier(.65,0,.35,1) infinite">
<div style="margin: 0 auto; width: 56px; height: 66px; border-radius: 50%; background: #F2EDE7"></div>
<div style="margin: -4px auto 0; width: 100px; height: 60px; border-radius: 40px 40px 0 0; background: #D9D1C8"></div></div></div>'''
icon3 = f'''<div style="position: relative; width: 120px; height: 120px; border-radius: 12px; border: 2px solid rgba(242,237,231,.4); overflow: hidden">
<div style="position: absolute; left: 44px; top: 8px; width: 32px; height: 36px; border-radius: 50%; background: #F2EDE7"></div>
<div style="position: absolute; left: 30px; top: 46px; width: 60px; height: 80px; border-radius: 20px 20px 0 0; background: #D9D1C8"></div>
<div style="position: absolute; left: 0; right: 0; top: 22px; border-top: 4px dashed #FF6A1A; animation: aI3 2s cubic-bezier(.65,0,.35,1) infinite"></div></div>'''
cards5 = ''.join(
    f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 14px; width: 270px; padding: 26px 0 24px; border-radius: 26px; background: #12100F; border: 3px solid rgba(242,237,231,.2); animation: {a} 4s {E} infinite">
  {ic}
  <span style="{MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; color: #FF6A1A">{n}</span>
  <span style="{BRIC}; font-weight: 800; font-size: 36px; letter-spacing: -0.03em; line-height: 1">{t}</span>
</div>''' for n, t, ic, a in (('01', 'Ojos arriba', icon1, 'aHi1'), ('02', 'Poco aire', icon2, 'aHi2'), ('03', 'Corta bien', icon3, 'aHi3')))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 80px; line-height: 1; letter-spacing: -0.045em">Antes de darle a REC,<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">mira el encuadre.</span></p>
<div style="position: relative; margin-top: 44px; width: 920px; padding: 34px 0; border-radius: 30px; background: #0A0908; border: 2px dashed rgba(242,237,231,.14); display: flex; justify-content: center; gap: 26px">{cards5}</div>
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
    '¿Cuál de las 3 se te escapa más?',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
