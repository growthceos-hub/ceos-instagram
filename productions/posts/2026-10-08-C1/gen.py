#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C1 2026-10-08 (luz dura vs luz suave) en src/."""
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



# ============================================================ C1 2026-10-08 · Luz dura vs luz suave
import urllib.parse

HEAD_SHAPES = ('<path d="M18 520 C18 405 96 338 200 338 C304 338 382 405 382 520 Z"/>'
               '<rect x="166" y="240" width="68" height="110" rx="28"/>'
               '<ellipse cx="200" cy="168" rx="94" ry="112"/>')
MASK = "url('data:image/svg+xml," + urllib.parse.quote(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 520" preserveAspectRatio="none"><g fill="black">{HEAD_SHAPES}</g></svg>', safe='') + "')"


def litface(w, uid, sh='aShad', dur='4s'):
    """Busto iluminado desde la izquierda; la sombra del lado derecho cambia de borde duro a suave."""
    h = round(w * 1.3)
    return f'''<div style="position: relative; width: {w}px; height: {h}px">
<svg width="{w}" height="{h}" viewBox="0 0 400 520" preserveAspectRatio="none" style="position: absolute; inset: 0; display: block">
<defs><linearGradient id="lf{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#F2EDE7"/><stop offset="1" stop-color="#D9D1C8"/></linearGradient></defs>
<g fill="url(#lf{uid})">{HEAD_SHAPES}</g>
<rect x="150" y="160" width="22" height="9" rx="4.5" fill="#0A0908" opacity=".6"/><rect x="228" y="160" width="22" height="9" rx="4.5" fill="#0A0908" opacity=".6"/>
<path d="M200 178 L190 214 L206 214" fill="none" stroke="#9C938B" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" opacity=".7"/>
<path d="M172 238 Q200 254 228 238" fill="none" stroke="#9C938B" stroke-width="6" stroke-linecap="round" opacity=".8"/>
</svg>
<div style="position: absolute; inset: 0; -webkit-mask-image: {MASK}; mask-image: {MASK}; -webkit-mask-size: 100% 100%; mask-size: 100% 100%; overflow: hidden">
  <div style="position: absolute; left: 50%; top: -15%; width: 90%; height: 130%; background: #0A0908; opacity: .86; animation: {sh} {dur} cubic-bezier(.6,0,.3,1) infinite"></div>
</div>
</div>'''


SHADOW_KF = """
@keyframes aShad{0%,36%{filter:blur(0px);left:50%;opacity:.88}50%,86%{filter:blur(38px);left:60%;opacity:.42}100%{filter:blur(0px);left:50%;opacity:.88}}
@keyframes aSrc{0%,36%{width:46px;height:46px;border-radius:50%;box-shadow:0 0 26px 10px rgba(255,178,122,.95),0 0 4px 2px #fff}50%,86%{width:150px;height:250px;border-radius:18px;box-shadow:0 0 130px 46px rgba(255,178,122,.42),0 0 4px 2px #fff}100%{width:46px;height:46px;border-radius:50%;box-shadow:0 0 26px 10px rgba(255,178,122,.95),0 0 4px 2px #fff}}
@keyframes aDura{0%,38%{opacity:1;transform:scale(1)}44%,90%{opacity:0;transform:scale(.8)}96%,100%{opacity:1;transform:scale(1)}}
@keyframes aSuave{0%,42%{opacity:0;transform:scale(.8)}50%,86%{opacity:1;transform:scale(1)}92%,100%{opacity:0;transform:scale(.8)}}
"""


def cone(x1, y1a, y1b, x2, y2a, y2b, anim=None, extra=''):
    a = f'; animation: {anim} 4s cubic-bezier(.6,0,.3,1) infinite' if anim else ''
    return (f'<div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(255,178,122,.30), rgba(255,178,122,.06)); '
            f'clip-path: polygon({x1}% {y1a}%, {x2}% {y2a}%, {x2}% {y2b}%, {x1}% {y1b}%){a}; z-index: 1; {extra}"></div>')


def dark_bg(glow_x='70%'):
    return f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #1C130D 0%, #12100F 70%, #0A0908 100%)"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 14%; background: linear-gradient(180deg, #171412, #0A0908); border-top: 2px solid rgba(242,237,231,.06)"></div>'''


def tag_pair(dura, suave, extra):
    return (f'<div style="position: absolute; {extra}; z-index: 6">'
            f'<div style="position: absolute; right: 0; top: 0; white-space: nowrap; padding: 12px 20px; border-radius: 14px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 22px; letter-spacing: .08em; animation: aDura 4s ease-in-out infinite; transform-origin: 100% 0">{dura}</div>'
            f'<div style="position: absolute; right: 0; top: 0; white-space: nowrap; padding: 12px 20px; border-radius: 14px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 22px; letter-spacing: .08em; opacity: 0; animation: aSuave 4s ease-in-out infinite; transform-origin: 100% 0">{suave}</div></div>')


def stand(x, top, h):
    return f'<div style="position: absolute; left: {x - 3}px; top: {top}px; width: 6px; height: {h}px; background: linear-gradient(180deg, #6B635C, #1E1A17); z-index: 1"></div>'


def source(x, y, anim='aSrc'):
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: 46px; height: 46px; transform: translate(-50%,-50%); '
            f'background: radial-gradient(circle, #FFFFFF 0%, #FFFFFF 45%, #FFB27A 100%); border-radius: 50%; z-index: 3; animation: {anim} 4s cubic-bezier(.6,0,.3,1) infinite"></div>')


# ---------------------------------------------------------------- 01 GANCHO
kf1 = COMMON_KF + SHADOW_KF + """
@keyframes aCone1{0%,36%{clip-path:polygon(16% 38%,60% 14%,60% 92%,16% 46%)}50%,86%{clip-path:polygon(16% 16%,60% 14%,60% 92%,16% 66%)}100%{clip-path:polygon(16% 38%,60% 14%,60% 92%,16% 46%)}}
@keyframes aEdge{0%,36%{filter:blur(0px)}50%,86%{filter:blur(16px)}100%{filter:blur(0px)}}
@keyframes aEdgeL1{0%,38%{opacity:1}44%,90%{opacity:0}96%,100%{opacity:1}}
@keyframes aEdgeL2{0%,42%{opacity:0}50%,86%{opacity:1}92%,100%{opacity:0}}
"""
mon1 = dark_bg() + cone(16, 38, 46, 60, 14, 92, 'aCone1') + stand(150, 210, 300) + source(150, 210) + rec_timer() + f'''
<div style="position: absolute; left: 330px; bottom: -6px; width: 400px; z-index: 2; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{litface(400, 'm1')}</div>
{tag_pair('✕ LUZ DURA', '✓ LUZ SUAVE', 'right: 30px; top: 80px')}
'''
body1 = headline('LUZ A CÁMARA', '¿Sombras duras<br>en la cara?', 'No es tu cara: es tu luz.', 88) + f"""
<div style="position: relative; height: 600px; display: flex; flex-direction: column; gap: 18px">
  <div style="position: relative; height: 486px; border-radius: 26px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">{mon1}</div>
  <div style="position: relative; flex: 1; border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 0 28px; display: flex; align-items: center; gap: 24px">
    <div style="position: relative; flex: none; width: 420px; height: 40px; {BRIC}; font-weight: 800; font-size: 34px; letter-spacing: -0.03em; line-height: 40px">
      <span style="position: absolute; left: 0; animation: aEdgeL1 4s ease-in-out infinite">Borde de sombra: <span style="color: #FF3B30">duro</span></span>
      <span style="position: absolute; left: 0; opacity: 0; animation: aEdgeL2 4s ease-in-out infinite">Borde de sombra: <span style="{SERIF}; color: #FF6A1A; font-size: 40px">suave</span></span>
    </div>
    <div style="position: relative; flex: 1; height: 34px; border-radius: 99px; overflow: hidden; background: #F2EDE7">
      <div style="position: absolute; left: 50%; top: -20px; bottom: -20px; right: -40px; background: #0A0908; animation: aEdge 4s cubic-bezier(.6,0,.3,1) infinite"></div>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    '3 trucos para una luz que te favorece.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 EL PORQUÉ
kf2 = COMMON_KF + SHADOW_KF + """
@keyframes aBar{0%,36%{height:34px}50%,86%{height:330px}100%{height:34px}}
@keyframes aCone2{0%,36%{clip-path:polygon(16% 47%,50% 39%,50% 59%,16% 50%)}50%,86%{clip-path:polygon(16% 24%,50% 39%,50% 59%,16% 74%)}100%{clip-path:polygon(16% 47%,50% 39%,50% 59%,16% 50%)}}
@keyframes aWallSh{0%,36%{filter:blur(0px);transform:scale(1.08)}50%,86%{filter:blur(22px);transform:scale(.92)}100%{filter:blur(0px);transform:scale(1.08)}}
@keyframes aR1{0%,40%{background:#1E1A17;border-color:#FF6A1A;transform:translateX(-8px)}46%,100%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}
@keyframes aR2{0%,44%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}50%,88%{background:#1E1A17;border-color:#FF6A1A;transform:translateX(-8px)}94%,100%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}
@keyframes aKey{0%,100%{box-shadow:0 0 0 rgba(255,106,26,0)}50%{box-shadow:0 0 60px -6px rgba(255,106,26,.55)}}
"""
diag2 = f'''<div style="position: absolute; inset: 0; background: radial-gradient(circle at 30% 45%, #1C130D, #0A0908 75%)"></div>
{cone(16, 47, 50, 50, 39, 59, 'aCone2')}
<div style="position: absolute; left: 80px; top: 48.5%; width: 30px; height: 34px; transform: translate(-50%,-50%); border-radius: 10px; background: linear-gradient(90deg, #FFB27A, #FFFFFF); box-shadow: 0 0 60px 16px rgba(255,178,122,.55); z-index: 3; animation: aBar 4s cubic-bezier(.6,0,.3,1) infinite"></div>
<div style="position: absolute; left: 196px; top: 48.5%; width: 110px; height: 110px; margin-top: -55px; border-radius: 50%; background: radial-gradient(circle at 28% 40%, #FFFFFF, #D9D1C8 45%, #3A3530 100%); z-index: 3"></div>
<div style="position: absolute; right: 0; top: 0; bottom: 0; width: 90px; background: linear-gradient(90deg, #1E1A17, #2A2622); border-left: 2px solid rgba(242,237,231,.2)"></div>
<div style="position: absolute; right: 0; top: 0; bottom: 0; width: 90px; overflow: hidden">
  <div style="position: absolute; left: 6px; top: 48.5%; width: 70px; height: 150px; margin-top: -75px; border-radius: 50%; background: #050403; animation: aWallSh 4s cubic-bezier(.6,0,.3,1) infinite"></div>
</div>
<div style="position: absolute; left: 22px; top: 22px; {MONO}; font-size: 18px; letter-spacing: .12em; color: #9C938B">LUZ · CARA · PARED</div>
{tag_pair('FUENTE PEQUEÑA', 'FUENTE GRANDE', 'left: 22px; right: 22px; bottom: 74px; height: 50px')}
'''
rows2 = ''.join(
    f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 22px 24px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s {E} infinite">'
    f'<span style="{MONO}; font-weight: 600; font-size: 22px; letter-spacing: .08em; color: {c}">{r}</span>'
    f'<span style="{BRIC}; font-weight: 800; font-size: 31px; letter-spacing: -0.02em; line-height: 1.04">{t}</span>'
    f'<span style="font-size: 22px; color: #B5ADA4; line-height: 1.25">{d}</span></div>'
    for r, c, t, d, a in (('✕ SOMBRA DURA', '#FF3B30', 'Bombilla desnuda o sol directo', 'Borde marcado: se notan ojeras, arrugas y granitos', 'aR1'),
                          ('✓ SOMBRA SUAVE', '#FF6A1A', 'Ventana nublada o luz difuminada', 'La sombra se funde poco a poco: piel más uniforme', 'aR2')))
body2 = headline('EL PORQUÉ', 'Luz pequeña, sombra dura.', 'Luz grande, sombra suave.', 72) + f"""
<div style="position: relative; height: 640px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: 440px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.5)">{diag2}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 18px">{rows2}
    <div style="padding: 20px 24px; border-radius: 22px; background: #0A0908; border: 2px dashed #FF6A1A; animation: aKey 4s ease-in-out infinite">
      <span style="{BRIC}; font-weight: 800; font-size: 28px; letter-spacing: -0.02em; line-height: 1.1">La clave: lo <span style="{SERIF}; color: #FF6A1A; font-size: 34px">grande</span> que es la luz comparada contigo.</span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · El porqué', 2, kf2, body2,
    'No necesitas más luz: necesitas una luz más grande.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 TRUCO 01 · DIFUMINA
kf3 = COMMON_KF + chk_kf(3, [8, 38, 68]) + SHADOW_KF + """
@keyframes aDif{0%,10%{transform:translateY(-560px)}30%,84%{transform:translateY(0)}98%,100%{transform:translateY(-560px)}}
@keyframes aDifGlow{0%,26%{box-shadow:0 0 0 rgba(255,178,122,0);background:rgba(242,237,231,.10)}38%,82%{box-shadow:0 0 120px 30px rgba(255,178,122,.45);background:rgba(255,255,255,.88)}94%,100%{box-shadow:0 0 0 rgba(255,178,122,0);background:rgba(242,237,231,.10)}}
@keyframes aShad3{0%,26%{filter:blur(0px);left:50%;opacity:.88}40%,82%{filter:blur(34px);left:60%;opacity:.42}96%,100%{filter:blur(0px);left:50%;opacity:.88}}
@keyframes aCone3{0%,26%{clip-path:polygon(26% 27%,62% 46%,62% 96%,26% 33%)}40%,82%{clip-path:polygon(40% 10%,62% 46%,62% 96%,40% 58%)}96%,100%{clip-path:polygon(26% 27%,62% 46%,62% 96%,26% 33%)}}
@keyframes aBulb{0%,100%{box-shadow:0 0 30px 12px rgba(255,178,122,.95)}50%{box-shadow:0 0 40px 16px rgba(255,178,122,1)}}
@keyframes aD1{0%,30%{opacity:1}36%,90%{opacity:0}96%,100%{opacity:1}}
@keyframes aD2{0%,32%{opacity:0}40%,84%{opacity:1}92%,100%{opacity:0}}
@keyframes aWarm{0%,100%{opacity:.6}50%{opacity:1}}
"""
panel3 = dark_bg() + cone(26, 27, 33, 62, 46, 96, 'aCone3') + stand(130, 180, 460) + f'''
<div style="position: absolute; left: 130px; top: 170px; width: 50px; height: 50px; transform: translate(-50%,-50%); border-radius: 50%; background: radial-gradient(circle, #FFFFFF 45%, #FFB27A); z-index: 2; animation: aBulb 2s ease-in-out infinite"></div>
<div style="position: absolute; left: 180px; top: 40px; width: 34px; height: 290px; z-index: 4; animation: aDif 4s cubic-bezier(.6,0,.3,1) infinite">
  <div style="position: absolute; inset: 0; border-radius: 8px; border: 3px solid #F2EDE7; animation: aDifGlow 4s cubic-bezier(.6,0,.3,1) infinite"></div>
  <div style="position: absolute; left: 50%; top: 304px; transform: translateX(-50%); white-space: nowrap; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .1em; color: #F2EDE7; background: rgba(10,9,8,.7); padding: 4px 8px; border-radius: 6px">DIFUSOR</div>
</div>
<div style="position: absolute; left: 236px; bottom: -6px; width: 250px; z-index: 2">{litface(250, 'm3', 'aShad3')}</div>
<div style="position: absolute; left: 22px; right: 22px; top: 22px; height: 44px; z-index: 6">
  <div style="position: absolute; right: 0; white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; animation: aD1 4s ease-in-out infinite">✕ SIN DIFUSOR</div>
  <div style="position: absolute; right: 0; white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; opacity: 0; animation: aD2 4s ease-in-out infinite">✓ CON DIFUSOR</div>
</div>
'''
body3 = headline('TRUCO 01 · DIFUMINA', 'Pon algo delante de la luz:', 'se reparte y se suaviza.', 80) + f"""
<div style="position: relative; height: 640px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: 480px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.55)">{panel3}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 16px">
    <div style="border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 20px 18px; display: flex; flex-direction: column; gap: 12px">
      <span style="{MONO}; font-size: 18px; letter-spacing: .12em; color: #9C938B; padding-left: 4px">SIRVE CUALQUIERA</span>
      {ticklist(['Tela o papel blanco fino', 'Softbox o paraguas translúcido', 'Cortina blanca en la ventana'], [('a3Row1', 'a3Tk1'), ('a3Row2', 'a3Tk2'), ('a3Row3', 'a3Tk3')])}
    </div>
    <div style="border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 22px 24px; display: flex; gap: 16px; align-items: flex-start">
      <span style="flex: none; width: 44px; height: 44px; border-radius: 12px; background: rgba(255,106,26,.16); border: 2px solid #FF6A1A; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 26px; color: #FF6A1A; animation: aWarm 2s ease-in-out infinite">!</span>
      <span style="font-size: 23px; color: #D9D1C8; line-height: 1.3">Déjalo a un palmo del foco: que <b style="color: #F2EDE7">no toque la bombilla</b> ni se caliente.</span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Difumina', 3, kf3, body3,
    'Más superficie de luz = sombra que se funde.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 TRUCOS 02 + 03 · REBOTA Y ACERCA
kf4 = COMMON_KF + """
@keyframes aRay{0%{left:70px;top:470px;opacity:0}6%{opacity:1}40%{left:210px;top:92px;opacity:1}78%{left:340px;top:410px;opacity:1}86%,100%{left:340px;top:410px;opacity:0}}
@keyframes aRay2{0%,10%{left:70px;top:470px;opacity:0}16%{opacity:1}50%{left:210px;top:92px;opacity:1}88%{left:340px;top:410px;opacity:1}96%,100%{left:340px;top:410px;opacity:0}}
@keyframes aWall{0%,30%{box-shadow:0 0 0 rgba(255,178,122,0);background:#D9D1C8}42%,90%{box-shadow:0 0 90px 26px rgba(255,178,122,.55);background:#FFFFFF}100%{box-shadow:0 0 0 rgba(255,178,122,0);background:#D9D1C8}}
@keyframes aHeadLit{0%,64%{box-shadow:0 0 0 rgba(255,178,122,0)}78%,92%{box-shadow:0 0 70px 14px rgba(255,178,122,.55)}100%{box-shadow:0 0 0 rgba(255,178,122,0)}}
@keyframes aDash{to{stroke-dashoffset:-44}}
@keyframes aMove{0%,14%{left:24px}46%,84%{left:150px}100%{left:24px}}
@keyframes aCone4{0%,14%{clip-path:polygon(11% 44%,58% 30%,58% 86%,11% 66%)}46%,84%{clip-path:polygon(40% 24%,58% 30%,58% 86%,40% 70%)}100%{clip-path:polygon(11% 44%,58% 30%,58% 86%,11% 66%)}}
@keyframes aShad4{0%,14%{filter:blur(0px);left:50%;opacity:.88}46%,84%{filter:blur(36px);left:60%;opacity:.4}100%{filter:blur(0px);left:50%;opacity:.88}}
@keyframes aFar{0%,24%{opacity:1}32%,90%{opacity:0}98%,100%{opacity:1}}
@keyframes aNear{0%,30%{opacity:0}40%,84%{opacity:1}92%,100%{opacity:0}}
@keyframes aArrow{0%,14%{opacity:0;transform:translateX(-20px)}26%,40%{opacity:1;transform:translateX(0)}50%,100%{opacity:0;transform:translateX(20px)}}
"""
panelA = f'''<div style="position: absolute; inset: 0; background: radial-gradient(circle at 50% 60%, #1C130D, #0A0908 80%)"></div>
<div style="position: absolute; left: 40px; right: 40px; top: 66px; height: 26px; border-radius: 8px; z-index: 2; animation: aWall 4s ease-in-out infinite"></div>
<div style="position: absolute; left: 40px; top: 100px; {MONO}; font-size: 16px; letter-spacing: .12em; color: #9C938B">PARED O CARTULINA BLANCA</div>
<svg width="448" height="560" viewBox="0 0 448 560" style="position: absolute; left: 0; top: 0; z-index: 1">
  <path d="M70 470 L210 92 L340 410" fill="none" stroke="#FF6A1A" stroke-width="4" stroke-dasharray="14 8" stroke-linecap="round" opacity=".75" style="animation: aDash 1s linear infinite"/>
</svg>
<div style="position: absolute; left: 70px; top: 470px; width: 64px; height: 64px; transform: translate(-50%,-50%) rotate(-20deg); border-radius: 14px; background: linear-gradient(0deg, #FFB27A, #FFFFFF); box-shadow: 0 0 40px 12px rgba(255,178,122,.6); z-index: 3"></div>
<div style="position: absolute; left: 340px; top: 410px; width: 110px; height: 110px; transform: translate(-50%,-50%); border-radius: 50%; background: radial-gradient(circle at 50% 22%, #FFFFFF, #D9D1C8 55%, #6B635C); z-index: 3; animation: aHeadLit 4s ease-in-out infinite"></div>
<div style="position: absolute; left: 340px; top: 482px; transform: translateX(-50%); {MONO}; font-size: 16px; letter-spacing: .12em; color: #9C938B; z-index: 3">TÚ</div>
<div style="position: absolute; width: 22px; height: 22px; margin: -11px 0 0 -11px; border-radius: 50%; background: #FFFFFF; box-shadow: 0 0 22px 8px rgba(255,178,122,.9); z-index: 4; animation: aRay 2s linear infinite"></div>
<div style="position: absolute; width: 22px; height: 22px; margin: -11px 0 0 -11px; border-radius: 50%; background: #FFFFFF; box-shadow: 0 0 22px 8px rgba(255,178,122,.9); z-index: 4; animation: aRay2 2s linear 1s infinite"></div>
'''
panelB = f'''{dark_bg()}
{cone(11, 44, 66, 58, 30, 86, 'aCone4')}
<div style="position: absolute; left: 24px; top: 210px; width: 60px; height: 120px; z-index: 3; animation: aMove 4s cubic-bezier(.6,0,.3,1) infinite">
  <div style="width: 60px; height: 120px; border-radius: 12px; background: linear-gradient(90deg, #FFB27A, #FFFFFF); box-shadow: 0 0 70px 18px rgba(255,178,122,.5)"></div>
  <div style="margin: 0 auto; width: 6px; height: 260px; background: linear-gradient(180deg, #6B635C, #1E1A17)"></div>
</div>
<div style="position: absolute; left: 220px; bottom: -6px; width: 240px; z-index: 2">{litface(240, 'm4', 'aShad4')}</div>
<div style="position: absolute; left: 22px; right: 22px; top: 22px; height: 44px; z-index: 6">
  <div style="position: absolute; left: 0; white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; animation: aFar 4s ease-in-out infinite">✕ LEJOS</div>
  <div style="position: absolute; left: 0; white-space: nowrap; padding: 10px 18px; border-radius: 12px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .08em; opacity: 0; animation: aNear 4s ease-in-out infinite">✓ CERCA</div>
</div>
<div style="position: absolute; left: 100px; top: 150px; {BRIC}; font-weight: 800; font-size: 44px; color: #FF6A1A; z-index: 6; animation: aArrow 4s ease-in-out infinite">→</div>
'''


def card4(num, title, sub, panel):
    return f'''<div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 14px">
  <div style="position: relative; height: 560px; border-radius: 28px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.5)">{panel}</div>
  <div style="display: flex; align-items: baseline; gap: 12px"><span style="{MONO}; font-weight: 600; font-size: 22px; letter-spacing: .08em; color: #FF6A1A">{num}</span><span style="{BRIC}; font-weight: 800; font-size: 32px; letter-spacing: -0.02em">{title}</span></div>
  <span style="margin-top: -8px; font-size: 22px; color: #B5ADA4; line-height: 1.25">{sub}</span>
</div>'''


body4 = headline('TRUCOS 02 + 03', 'Rebótala y acércala:', 'más grande, más suave.', 84) + f"""
<div style="position: relative; height: 680px; display: flex; gap: 24px">
{card4('02', 'Rebota', 'Apúntala a una pared blanca: te llega grande y suave.', panelA)}
{card4('03', 'Acerca', 'Cuanto más cerca de ti, más suave cae la sombra.', panelB)}
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Rebota y acerca', 4, kf4, body4,
    'Sin comprar nada: solo mover lo que ya tienes.', DESLIZA_TXT))

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
@keyframes aI1{0%,100%{box-shadow:0 0 20px 6px rgba(255,178,122,.4)}50%{box-shadow:0 0 50px 18px rgba(255,178,122,.75)}}
@keyframes aI2{0%{left:18px;top:96px}50%{left:62px;top:18px}100%{left:106px;top:96px}}
@keyframes aI3{0%,100%{transform:translateX(0)}50%{transform:translateX(40px)}}
"""
icon1 = f'''<div style="position: relative; width: 130px; height: 120px">
<div style="position: absolute; left: 14px; top: 44px; width: 32px; height: 32px; border-radius: 50%; background: #FFFFFF; box-shadow: 0 0 22px 8px rgba(255,178,122,.9)"></div>
<div style="position: absolute; left: 66px; top: 6px; width: 46px; height: 108px; border-radius: 10px; background: rgba(255,255,255,.9); border: 3px solid #F2EDE7; animation: aI1 2s ease-in-out infinite"></div></div>'''
icon2 = f'''<div style="position: relative; width: 130px; height: 120px">
<div style="position: absolute; left: 4px; right: 4px; top: 0; height: 12px; border-radius: 6px; background: #F2EDE7"></div>
<div style="position: absolute; width: 20px; height: 20px; margin: -10px 0 0 -10px; border-radius: 50%; background: #FFFFFF; box-shadow: 0 0 18px 6px rgba(255,178,122,.9); animation: aI2 1.6s linear infinite"></div></div>'''
icon3 = f'''<div style="position: relative; width: 130px; height: 120px">
<div style="position: absolute; left: 4px; top: 30px; width: 34px; height: 64px; border-radius: 8px; background: linear-gradient(90deg, #FFB27A, #FFFFFF); box-shadow: 0 0 30px 8px rgba(255,178,122,.55); animation: aI3 2s ease-in-out infinite"></div>
<div style="position: absolute; right: 6px; top: 22px; width: 44px; height: 54px; border-radius: 50%; background: #F2EDE7"></div>
<div style="position: absolute; right: -4px; top: 76px; width: 64px; height: 40px; border-radius: 30px 30px 0 0; background: #D9D1C8"></div></div>'''
cards5 = ''.join(
    f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 14px; width: 270px; padding: 26px 0 24px; border-radius: 26px; background: #12100F; border: 3px solid rgba(242,237,231,.2); animation: {a} 4s {E} infinite">
  {ic}
  <span style="{MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; color: #FF6A1A">{n}</span>
  <span style="{BRIC}; font-weight: 800; font-size: 38px; letter-spacing: -0.03em; line-height: 1">{t}</span>
</div>''' for n, t, ic, a in (('01', 'Difumina', icon1, 'aHi1'), ('02', 'Rebota', icon2, 'aHi2'), ('03', 'Acerca', icon3, 'aHi3')))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 86px; line-height: 1; letter-spacing: -0.045em">Luz grande y cerca<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">= cara de estudio.</span></p>
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
    'Guárdalo para tu próxima grabación.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
