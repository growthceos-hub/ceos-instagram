#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C1 2026-10-11 (vídeo que tiembla: 3 trucos) en src/."""
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


# ============================================================ C1 2026-10-11 · Vídeo que tiembla: 3 trucos
import random
random.seed(1011)


def shake_kf(name, n=48, amp=9, rot=1.6, calm=None):
    """Temblor a mano: n saltos en 4 s. calm=(a,b) -> tramo en % sin temblor."""
    out = []
    for i in range(n + 1):
        p = i * 100 / n
        if calm and calm[0] <= p <= calm[1]:
            x = y = r = 0
        elif i in (0, n):
            x, y, r = 0, 0, 0
        else:
            x, y, r = random.uniform(-amp, amp), random.uniform(-amp, amp), random.uniform(-rot, rot)
        out.append(f'{p:.2f}%{{transform:translate({x:.1f}px,{y:.1f}px) rotate({r:.2f}deg)}}')
    return f'@keyframes {name}{{' + ''.join(out) + '}\n'


def trace(w, h, amp, n, col, sw=4):
    """Traza periódica (ancho w, repetida 2 veces) para desplazarla en bucle."""
    pts = [(0, h / 2)]
    for i in range(1, n):
        pts.append((i * w / n, h / 2 + random.uniform(-amp, amp)))
    pts.append((w, h / 2))
    full = pts + [(x + w, y) for x, y in pts[1:]]
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in full)
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>'


# ---------------------------------------------------------------- 01 GANCHO · a pulso vs estable
VW1, VH1 = 448, 470
kf1 = COMMON_KF + shake_kf('aShake', 56, 11, 2.2) + """
@keyframes aBlur{0%,100%{filter:blur(0)}20%{filter:blur(1.6px)}40%{filter:blur(.4px)}60%{filter:blur(2px)}80%{filter:blur(.8px)}}
@keyframes aScroll{0%{transform:translateX(0)}100%{transform:translateX(-916px)}}
@keyframes aBub{0%,100%{transform:translateX(-50%)}50%{transform:translateX(-50%) scale(1.15)}}
@keyframes aBubBad{0%{left:20%}13%{left:78%}27%{left:30%}41%{left:70%}55%{left:18%}69%{left:82%}84%{left:35%}100%{left:20%}}
@keyframes aHL{0%,100%{border-color:#FF3B30;box-shadow:0 0 40px -6px rgba(255,59,48,.6)}50%{border-color:rgba(255,59,48,.4);box-shadow:none}}
@keyframes aHR{0%,100%{border-color:rgba(255,106,26,.4);box-shadow:none}50%{border-color:#FF6A1A;box-shadow:0 0 40px -6px rgba(255,106,26,.7)}}
"""
wp1 = 330


def vf1(bad):
    person_anim = 'aShake 4s linear infinite' if bad else 'aBreath 3s ease-in-out infinite'
    blur = '; animation: aBlur .5s linear infinite' if bad else ''
    bub = ('aBubBad 4s ease-in-out infinite', '#FF3B30') if bad else ('aBub 2s ease-in-out infinite', '#FF6A1A')
    lvl_pos = 'left: 20%' if bad else 'left: 50%; transform: translateX(-50%)'
    return f'''<div style="position: relative; width: {VW1}px; height: {VH1}px; border-radius: 26px; overflow: hidden; border: 3px solid {'#FF3B30' if bad else '#FF6A1A'}; animation: {'aHL' if bad else 'aHR'} 2s ease-in-out infinite">
<div style="position: absolute; inset: -30px{blur}">
 <div style="position: absolute; inset: 0; animation: {person_anim}">
  {studio_bg(not bad)}
  <div style="position: absolute; left: 0; right: 0; top: 66%; height: 2px; background: rgba(242,237,231,.25)"></div>
  <div style="position: absolute; left: {(VW1 + 60 - wp1)/2:.0f}px; top: 120px; width: {wp1}px">{tall_person(wp1, 'h' + ('b' if bad else 'g'))}</div>
 </div>
</div>
{grid(VW1, VH1, '.12')}
<div style="position: absolute; left: 50%; top: 22px; width: 190px; height: 34px; margin-left: -95px; border-radius: 99px; background: rgba(10,9,8,.8); border: 2px solid rgba(242,237,231,.3); z-index: 6">
  <div style="position: absolute; left: 50%; top: 4px; bottom: 4px; width: 2px; background: rgba(242,237,231,.5)"></div>
  <div style="position: absolute; top: 5px; width: 22px; height: 22px; margin-left: -11px; border-radius: 99px; background: {bub[1]}; box-shadow: 0 0 14px {bub[1]}; {lvl_pos}; animation: {bub[0]}"></div>
</div>
{tag('✕ A PULSO', 'left: 18px; bottom: 18px') if bad else tag('✓ ESTABLE', 'right: 18px; bottom: 18px', '#FF6A1A', '#0A0908')}
<div style="position: absolute; left: 18px; top: 26px; display: flex; align-items: center; gap: 8px; {MONO}; font-size: 17px; letter-spacing: .1em; color: #F2EDE7; z-index: 6"><span style="width: 12px; height: 12px; border-radius: 99px; background: #FF3B30; animation: aRec 1s steps(1) infinite"></span>REC</div>
</div>'''


graph1 = f'''<div style="position: relative; width: 916px; height: 132px; border-radius: 22px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,.14)">
<div style="position: absolute; left: 20px; top: 12px; {MONO}; font-weight: 600; font-size: 17px; letter-spacing: .1em; color: #9C938B; z-index: 3">MOVIMIENTO DE LA IMAGEN</div>
<div style="position: absolute; left: 0; right: 0; top: 66px; height: 1px; background: rgba(242,237,231,.12)"></div>
<svg width="1832" height="132" viewBox="0 0 1832 132" style="position: absolute; left: 0; top: 0; animation: aScroll 4s linear infinite">
 <g transform="translate(0,4)">{trace(916, 124, 36, 70, '#FF3B30', 4)}</g>
 <g transform="translate(0,10)">{trace(916, 124, 2.5, 18, '#FF6A1A', 5)}</g>
</svg>
<div style="position: absolute; right: 18px; top: 12px; display: flex; gap: 18px; {MONO}; font-weight: 600; font-size: 17px; letter-spacing: .08em; z-index: 3"><span style="color: #FF3B30">━ A PULSO</span><span style="color: #FF6A1A">━ CON LOS 3 TRUCOS</span></div>
</div>'''
body1 = headline('VÍDEO ESTABLE SIN GIMBAL', 'Tu vídeo tiembla.', 'Y el móvil no tiene la culpa.', 88) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 20px">
  <div style="display: flex; gap: 20px">{vf1(True)}{vf1(False)}</div>
  {graph1}
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Mismo móvil, misma persona: 3 trucos.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 TRUCO 01 · APOYO FIJO
PW2, PH2 = 470, 650
kf2 = COMMON_KF + chk_kf(2, [8, 38, 68]) + """
@keyframes aBub2{0%{left:22%}10%{left:74%}20%{left:38%}30%{left:58%}40%,100%{left:50%}}
@keyframes aBubC{0%,36%{background:#FF3B30;box-shadow:0 0 12px #FF3B30}42%,100%{background:#FF6A1A;box-shadow:0 0 16px #FF6A1A}}
@keyframes aTilt{0%{transform:rotate(-5deg)}10%{transform:rotate(4deg)}20%{transform:rotate(-2.5deg)}30%{transform:rotate(1.2deg)}40%,100%{transform:rotate(0)}}
@keyframes aOk{0%,40%{opacity:0;transform:scale(.6)}48%{opacity:1;transform:scale(1.15)}54%,100%{opacity:1;transform:scale(1)}}
@keyframes aTimer{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}
@keyframes aKey{0%,100%{box-shadow:0 0 0 rgba(255,106,26,0)}50%{box-shadow:0 0 60px -6px rgba(255,106,26,.55)}}
@keyframes aCnt{0%,24.9%{opacity:1;transform:scale(1)}20%{transform:scale(1.1)}25%,100%{opacity:0}}
"""
# soportes que se alternan cada segundo
sup_tri = '''<svg width="300" height="230" viewBox="0 0 300 230"><g stroke="#B5ADA4" stroke-width="10" stroke-linecap="round"><line x1="150" y1="10" x2="40" y2="220"/><line x1="150" y1="10" x2="260" y2="220"/><line x1="150" y1="10" x2="150" y2="225"/></g><rect x="120" y="0" width="60" height="26" rx="8" fill="#6B635C"/></svg>'''
sup_books = ''.join(
    f'<div style="width: {w}px; height: 52px; margin: 0 auto 4px; border-radius: 6px; background: {c}; border-left: 10px solid rgba(0,0,0,.25)"></div>'
    for w, c in ((250, '#6B635C'), (290, '#9C938B'), (270, '#6B635C'), (300, '#B5ADA4')))
sup_shelf = '<div style="width: 360px; height: 30px; margin: 0 auto; border-radius: 6px; background: #9C938B"></div><div style="display: flex; justify-content: space-between; width: 300px; margin: 0 auto"><span style="width: 18px; height: 196px; background: #6B635C"></span><span style="width: 18px; height: 196px; background: #6B635C"></span></div>'
sup_table = '<div style="width: 400px; height: 34px; margin: 0 auto; border-radius: 8px; background: #B5ADA4"></div><div style="display: flex; justify-content: space-between; width: 340px; margin: 0 auto"><span style="width: 22px; height: 192px; background: #6B635C"></span><span style="width: 22px; height: 192px; background: #6B635C"></span></div>'
sups = [('TRÍPODE', sup_tri), ('PILA DE LIBROS', sup_books), ('ESTANTERÍA', sup_shelf), ('MESA', sup_table)]
sup_layers = ''.join(
    f'<div style="position: absolute; left: 0; right: 0; bottom: 70px; height: 230px; display: flex; flex-direction: column; justify-content: flex-end; opacity: 0; animation: aStep 4s steps(1) {k-4}s infinite">{s}</div>'
    for k, (_, s) in enumerate(sups))
sup_names = cycle([f'<span style="background: #FF6A1A; color: #0A0908; padding: 8px 16px; border-radius: 10px">APOYO: {n}</span>' for n, _ in sups],
                  f'{MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; text-align: center')
mini = studio_bg(True) + f'<div style="position: absolute; left: 50%; top: 26px; width: 150px; margin-left: -75px">{tall_person(150, "m2")}</div>'
panel2 = studio_bg(False) + f'''
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 70px; background: linear-gradient(180deg, #171412, #0A0908); border-top: 2px solid rgba(242,237,231,.08)"></div>
{sup_layers}
<div style="position: absolute; left: 50%; bottom: 296px; width: 216px; height: 260px; margin-left: -108px; transform-origin: 50% 100%; animation: aTilt 4s ease-out infinite; z-index: 3">
  <div style="position: absolute; inset: 0; border-radius: 30px; background: #050505; padding: 10px; box-sizing: border-box; box-shadow: 0 0 0 3px rgba(242,237,231,.2), 0 30px 80px -20px rgba(255,106,26,.6)">
    <div style="position: relative; width: 100%; height: 100%; border-radius: 22px; overflow: hidden">{mini}
      <div style="position: absolute; left: 10px; top: 10px; display: flex; align-items: center; gap: 6px; {MONO}; font-size: 13px; letter-spacing: .1em; color: #F2EDE7"><span style="width: 9px; height: 9px; border-radius: 99px; background: #FF3B30; animation: aRec 1s steps(1) infinite"></span>REC</div>
    </div>
  </div>
  <div style="position: absolute; left: 50%; top: -48px; width: 170px; height: 30px; margin-left: -85px; border-radius: 99px; background: rgba(10,9,8,.85); border: 2px solid rgba(242,237,231,.35)">
    <div style="position: absolute; left: 50%; top: 3px; bottom: 3px; width: 2px; background: rgba(242,237,231,.5)"></div>
    <div style="position: absolute; top: 4px; width: 20px; height: 20px; margin-left: -10px; border-radius: 99px; animation: aBub2 4s ease-out infinite, aBubC 4s steps(1) infinite"></div>
  </div>
</div>
<div style="position: absolute; left: 20px; right: 20px; bottom: 16px; height: 44px; z-index: 6">{sup_names}</div>
<div style="position: absolute; right: 20px; top: 84px; z-index: 6; animation: aOk 4s ease-out infinite">{tag('✓ QUIETO', 'right: 0; top: 0', '#FF6A1A', '#0A0908')}</div>
{corners()}'''
timer2 = ''.join(
    f'<span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; opacity: 0; animation: aStep 4s steps(1) {k-4}s infinite">{t}</span>'
    for k, t in enumerate(['3', '2', '1', '●']))
body2 = headline('TRUCO 01 · APOYO FIJO', 'Si tú no te mueves,', 'el móvil tampoco.', 84) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: {PW2}px; height: {PH2}px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.55)">{panel2}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 18px">
    <div style="border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 20px 18px; display: flex; flex-direction: column; gap: 12px">
      <span style="{MONO}; font-size: 18px; letter-spacing: .12em; color: #9C938B; padding-left: 4px">SI HABLAS SIN MOVERTE</span>
      {ticklist(['Saca el móvil de la mano', 'Apóyalo a la altura de tus ojos', 'Pon el temporizador de 3 s'], [('a2Row1', 'a2Tk1'), ('a2Row2', 'a2Tk2'), ('a2Row3', 'a2Tk3')])}
    </div>
    <div style="padding: 20px 22px; border-radius: 22px; background: #0A0908; border: 2px dashed #FF6A1A; display: flex; gap: 18px; align-items: center; animation: aKey 4s ease-in-out infinite">
      <span style="position: relative; flex: none; width: 74px; height: 74px; border-radius: 99px; border: 3px solid #FF6A1A; {BRIC}; font-weight: 800; font-size: 38px; color: #FF6A1A; animation: aTimer 1s ease-in-out infinite">{timer2}</span>
      <span style="{BRIC}; font-weight: 800; font-size: 26px; letter-spacing: -0.02em; line-height: 1.15">Al tocar el botón de grabar también lo mueves. <span style="{SERIF}; color: #FF6A1A; font-size: 31px">El temporizador lo evita.</span></span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · Apoyo fijo', 2, kf2, body2,
    'Sin trípode vale una estantería o unos libros.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 TRUCO 02 · CODOS PEGADOS
VW3, VH3 = 470, 650
WIDE_L = 'M150 196 L52 300 L196 330'
TUCK_L = 'M150 196 L146 330 L196 330'
WIDE_R = 'M290 196 L388 300 L244 330'
TUCK_R = 'M290 196 L294 330 L244 330'
kf3 = COMMON_KF + shake_kf('aPhJ', 40, 7, 3, calm=(36, 88)) + f"""
@keyframes aArmL{{0%,26%{{d:path("{WIDE_L}")}}40%,84%{{d:path("{TUCK_L}")}}98%,100%{{d:path("{WIDE_L}")}}}}
@keyframes aArmR{{0%,26%{{d:path("{WIDE_R}")}}40%,84%{{d:path("{TUCK_R}")}}98%,100%{{d:path("{WIDE_R}")}}}}
@keyframes aMeter{{0%,26%{{width:24%;background:#FF3B30}}42%,84%{{width:94%;background:#FF6A1A}}98%,100%{{width:24%;background:#FF3B30}}}}
@keyframes aBad{{0%,30%{{opacity:1}}36%,90%{{opacity:0}}97%,100%{{opacity:1}}}}
@keyframes aGood{{0%,34%{{opacity:0}}42%,84%{{opacity:1}}90%,100%{{opacity:0}}}}
@keyframes aR1{{0%,28%{{background:#1E1A17;border-color:#FF3B30;transform:translateX(-8px)}}36%,88%{{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}96%,100%{{background:#1E1A17;border-color:#FF3B30;transform:translateX(-8px)}}}}
@keyframes aR2{{0%,34%{{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}42%,84%{{background:#1E1A17;border-color:#FF6A1A;transform:translateX(-8px)}}92%,100%{{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}}}
@keyframes aElb{{0%,30%{{opacity:0}}40%,84%{{opacity:1}}92%,100%{{opacity:0}}}}
@keyframes aWarm{{0%,100%{{opacity:.6}}50%{{opacity:1}}}}
"""
body_svg = f'''<svg width="440" height="470" viewBox="0 0 440 470" style="display:block; overflow: visible">
<defs><linearGradient id="bd3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F2EDE7" stop-opacity=".97"/><stop offset="1" stop-color="#B5ADA4" stop-opacity=".6"/></linearGradient></defs>
<path d="M120 470 L128 220 Q132 186 170 182 L270 182 Q308 186 312 220 L320 470 Z" fill="url(#bd3)"/>
<rect x="200" y="140" width="40" height="50" rx="16" fill="url(#bd3)"/>
<ellipse cx="220" cy="90" rx="56" ry="66" fill="url(#bd3)"/>
<rect x="190" y="84" width="14" height="7" rx="3" fill="#0A0908" opacity=".55"/><rect x="236" y="84" width="14" height="7" rx="3" fill="#0A0908" opacity=".55"/>
<path d="{WIDE_L}" fill="none" stroke="#D9D1C8" stroke-width="30" stroke-linecap="round" stroke-linejoin="round" style="animation: aArmL 4s cubic-bezier(.65,0,.35,1) infinite"/>
<path d="{WIDE_R}" fill="none" stroke="#D9D1C8" stroke-width="30" stroke-linecap="round" stroke-linejoin="round" style="animation: aArmR 4s cubic-bezier(.65,0,.35,1) infinite"/>
<g style="animation: aElb 4s ease-in-out infinite"><circle cx="146" cy="330" r="24" fill="none" stroke="#FF6A1A" stroke-width="4" stroke-dasharray="6 5"/><circle cx="294" cy="330" r="24" fill="none" stroke="#FF6A1A" stroke-width="4" stroke-dasharray="6 5"/></g>
</svg>'''
panel3 = studio_bg(True) + f'''
<div style="position: absolute; left: 15px; top: 100px; z-index: 2">{body_svg}</div>
<div style="position: absolute; left: 179px; top: 300px; width: 112px; height: 76px; z-index: 4; animation: aPhJ 4s linear infinite">
  <div style="width: 100%; height: 100%; border-radius: 14px; background: #050505; border: 3px solid rgba(242,237,231,.35); box-shadow: 0 0 30px rgba(255,106,26,.45); display: flex; align-items: center; justify-content: center"><span style="width: 14px; height: 14px; border-radius: 99px; background: #FF3B30; animation: aRec 1s steps(1) infinite"></span></div>
</div>
<div style="position: absolute; left: 22px; right: 22px; bottom: 22px; z-index: 6; padding: 16px 18px; border-radius: 18px; background: rgba(10,9,8,.85); border: 2px solid rgba(242,237,231,.16)">
  <div style="position: relative; height: 26px; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .1em">
    <span style="position: absolute; left: 0; color: #9C938B">ESTABILIDAD</span>
    <span style="position: absolute; right: 0; color: #FF3B30; animation: aBad 4s ease-in-out infinite">TIEMBLA</span>
    <span style="position: absolute; right: 0; color: #FF6A1A; opacity: 0; animation: aGood 4s ease-in-out infinite">FIRME</span>
  </div>
  <div style="margin-top: 10px; height: 16px; border-radius: 99px; background: #1E1A17; overflow: hidden"><div style="height: 100%; border-radius: 99px; animation: aMeter 4s cubic-bezier(.65,0,.35,1) infinite"></div></div>
</div>
{tag('✕ BRAZOS ABIERTOS', 'left: 22px; top: 22px', anim='aBad 4s ease-in-out infinite')}
{tag('✓ CODOS PEGADOS', 'left: 22px; top: 22px; opacity: 0', '#FF6A1A', '#0A0908', 'aGood 4s ease-in-out infinite')}
{corners()}'''
rows3 = ''.join(
    f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 22px 24px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: {a} 4s {E} infinite">'
    f'<span style="{MONO}; font-weight: 600; font-size: 21px; letter-spacing: .08em; color: {c}">{r}</span>'
    f'<span style="{BRIC}; font-weight: 800; font-size: 31px; letter-spacing: -0.02em; line-height: 1.04">{t}</span>'
    f'<span style="font-size: 22px; color: #B5ADA4; line-height: 1.25">{d}</span></div>'
    for r, c, t, d, a in (('✕ BRAZOS ABIERTOS', '#FF3B30', 'El móvil va por libre', 'Cada respiración se nota en la imagen', 'aR1'),
                          ('✓ CODOS PEGADOS', '#FF6A1A', 'Tu cuerpo hace de trípode', 'Móvil con las dos manos y cerca del pecho', 'aR2')))
body3 = headline('TRUCO 02 · CODOS PEGADOS', '¿Grabas a pulso?', 'Pega los codos al cuerpo.', 84) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: {VW3}px; height: {VH3}px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.55)">{panel3}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 16px">{rows3}
    <div style="border-radius: 22px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 20px 22px; display: flex; gap: 14px; align-items: flex-start">
      <span style="flex: none; width: 42px; height: 42px; border-radius: 12px; background: rgba(255,106,26,.16); border: 2px solid #FF6A1A; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 25px; color: #FF6A1A; animation: aWarm 2s ease-in-out infinite">!</span>
      <span style="font-size: 22px; color: #D9D1C8; line-height: 1.3">Truco extra: suelta el aire despacio mientras grabas. <b style="color: #F2EDE7">Con los pulmones llenos</b> el pulso tiembla más.</span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · Codos pegados', 3, kf3, body3,
    'Dos manos, codos dentro y móvil cerca.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 TRUCO 03 · PASO NINJA
VW4, VH4 = 470, 650
bounce_big = ''.join(f'{p}%{{transform:translateY({y}px) rotate({r}deg)}}' for p, y, r in
                     ((0, 0, 0), (6, -26, -1.8), (12, 6, 1.2), (18, -26, 1.8), (24, 6, -1.2), (30, -26, -1.8), (36, 6, 1.2), (44, 0, 0), (100, 0, 0)))
bounce_small = ''.join(f'{p}%{{transform:translateY({y}px)}}' for p, y in
                       ((0, 0), (44, 0), (50, -3), (56, 1), (62, -3), (68, 1), (74, -3), (80, 1), (86, -3), (92, 0), (100, 0)))
kf4 = COMMON_KF + chk_kf(4, [8, 38, 68]) + f"""
@keyframes aBounce{{{bounce_big}}}
@keyframes aBounceS{{{bounce_small}}}
@keyframes aBad{{0%,40%{{opacity:1}}46%,96%{{opacity:0}}100%{{opacity:1}}}}
@keyframes aGood{{0%,42%{{opacity:0}}48%,94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes aKey{{0%,100%{{box-shadow:0 0 0 rgba(255,106,26,0)}}50%{{box-shadow:0 0 60px -6px rgba(255,106,26,.55)}}}}
"""
# huellas: 3 pasos largos (rojo, 0-44%) y 6 pasos cortos (azul, 48-94%)
steps_kf = ''
foot_html = ''
foot = '<svg width="30" height="52" viewBox="0 0 30 52"><ellipse cx="15" cy="16" rx="12" ry="15" fill="{c}"/><ellipse cx="15" cy="42" rx="9" ry="9" fill="{c}"/></svg>'
for i in range(3):
    p0 = 4 + i * 12
    steps_kf += f'@keyframes aFb{i}{{0%,{p0}%{{opacity:0;transform:scale(.4)}}{p0+3}%{{opacity:1;transform:scale(1)}}44%{{opacity:1}}48%,100%{{opacity:0}}}}\n'
    x = 60 + (i % 2) * 54
    foot_html += f'<div style="position: absolute; left: {x}px; bottom: {20 + i*86}px; opacity: 0; animation: aFb{i} 4s ease-out infinite">{foot.format(c="#FF3B30")}</div>'
for i in range(6):
    p0 = 50 + i * 7
    steps_kf += f'@keyframes aFs{i}{{0%,{p0}%{{opacity:0;transform:scale(.4)}}{p0+3}%{{opacity:1;transform:scale(1)}}94%{{opacity:1}}98%,100%{{opacity:0}}}}\n'
    x = 286 + (i % 2) * 44
    foot_html += f'<div style="position: absolute; left: {x}px; bottom: {20 + i*42}px; opacity: 0; animation: aFs{i} 4s ease-out infinite">{foot.format(c="#FF6A1A")}</div>'
kf4 += steps_kf
wp4 = 230
vf4 = f'''<div style="position: absolute; left: 22px; right: 22px; top: 22px; height: 300px; border-radius: 22px; overflow: hidden; border: 2px solid rgba(242,237,231,.18)">
 <div style="position: absolute; inset: -40px; animation: aBounce 4s ease-in-out infinite">
  <div style="position: absolute; inset: 0; animation: aBounceS 4s ease-in-out infinite">
   {studio_bg(True)}
   <div style="position: absolute; left: 0; right: 0; top: 62%; height: 2px; background: rgba(242,237,231,.3)"></div>
   <div style="position: absolute; left: {(426 + 80 - wp4)/2:.0f}px; top: 70px; width: {wp4}px">{tall_person(wp4, 'w4')}</div>
  </div>
 </div>
 {grid(426, 300, '.12')}
 <div style="position: absolute; left: 14px; top: 14px; display: flex; align-items: center; gap: 8px; {MONO}; font-size: 16px; letter-spacing: .1em; color: #F2EDE7"><span style="width: 11px; height: 11px; border-radius: 99px; background: #FF3B30; animation: aRec 1s steps(1) infinite"></span>REC</div>
</div>'''
panel4 = studio_bg(False) + vf4 + f'''
<div style="position: absolute; left: 22px; right: 22px; top: 340px; bottom: 22px; border-radius: 22px; background: #12100F; border: 2px solid rgba(242,237,231,.14); overflow: hidden">
  <div style="position: absolute; left: 50%; top: 14px; bottom: 14px; width: 2px; background: rgba(242,237,231,.12)"></div>
  <div style="position: absolute; left: 0; width: 50%; top: 12px; text-align: center; {MONO}; font-weight: 600; font-size: 16px; letter-spacing: .1em; color: #FF3B30">PASO NORMAL</div>
  <div style="position: absolute; right: 0; width: 50%; top: 12px; text-align: center; {MONO}; font-weight: 600; font-size: 16px; letter-spacing: .1em; color: #FF6A1A">PASO NINJA</div>
  {foot_html}
</div>
{tag('✕ BOTA A CADA PASO', 'right: 36px; top: 266px', anim='aBad 4s ease-in-out infinite')}
{tag('✓ SE DESLIZA', 'right: 36px; top: 266px; opacity: 0', '#FF6A1A', '#0A0908', 'aGood 4s ease-in-out infinite')}'''
body4 = headline('TRUCO 03 · PASO NINJA', '¿Grabas caminando?', 'Pasos cortos y lentos.', 84) + f"""
<div style="position: relative; height: 660px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: {VW4}px; height: {VH4}px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.55)">{panel4}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 18px">
    <div style="border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 20px 18px; display: flex; flex-direction: column; gap: 12px">
      <span style="{MONO}; font-size: 18px; letter-spacing: .12em; color: #9C938B; padding-left: 4px">ASÍ SE CAMINA</span>
      {ticklist(['Rodillas un poco flexionadas', 'Apoya el talón y luego la punta', 'Gira con la cintura, no con las muñecas'], [('a4Row1', 'a4Tk1'), ('a4Row2', 'a4Tk2'), ('a4Row3', 'a4Tk3')])}
    </div>
    <div style="padding: 20px 24px; border-radius: 22px; background: #0A0908; border: 2px dashed #FF6A1A; animation: aKey 4s ease-in-out infinite">
      <span style="{BRIC}; font-weight: 800; font-size: 26px; letter-spacing: -0.02em; line-height: 1.15">Y activa la <span style="{SERIF}; color: #FF6A1A; font-size: 32px">estabilización de vídeo</span> en los ajustes de la cámara.</span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Paso ninja', 4, kf4, body4,
    'Tus piernas hacen de amortiguador.', DESLIZA_TXT))

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
@keyframes aI1{0%{left:20%}15%{left:75%}30%{left:35%}45%,100%{left:50%}}
@keyframes aI2L{0%,20%{d:path("M40 40 L14 84 L54 96")}50%,80%{d:path("M40 40 L38 96 L54 96")}100%{d:path("M40 40 L14 84 L54 96")}}
@keyframes aI2R{0%,20%{d:path("M80 40 L106 84 L66 96")}50%,80%{d:path("M80 40 L82 96 L66 96")}100%{d:path("M80 40 L106 84 L66 96")}}
@keyframes aI3a{0%,10%{opacity:0}20%,90%{opacity:1}100%{opacity:0}}
@keyframes aI3b{0%,35%{opacity:0}45%,90%{opacity:1}100%{opacity:0}}
@keyframes aI3c{0%,60%{opacity:0}70%,90%{opacity:1}100%{opacity:0}}
"""
icon1 = f'''<div style="position: relative; width: 120px; height: 120px; border-radius: 12px; border: 2px solid rgba(242,237,231,.4); overflow: hidden">
<svg width="120" height="120" viewBox="0 0 120 120" style="position: absolute; inset: 0"><g stroke="#B5ADA4" stroke-width="5" stroke-linecap="round"><line x1="60" y1="66" x2="28" y2="112"/><line x1="60" y1="66" x2="92" y2="112"/><line x1="60" y1="66" x2="60" y2="112"/></g><rect x="36" y="38" width="48" height="30" rx="6" fill="#F2EDE7"/></svg>
<div style="position: absolute; left: 22px; right: 22px; top: 12px; height: 16px; border-radius: 99px; border: 2px solid rgba(242,237,231,.5)"><span style="position: absolute; top: 1px; width: 10px; height: 10px; margin-left: -5px; border-radius: 99px; background: #FF6A1A; animation: aI1 2s ease-out infinite"></span></div></div>'''
icon2 = f'''<div style="position: relative; width: 120px; height: 120px; border-radius: 12px; border: 2px solid rgba(242,237,231,.4); overflow: hidden">
<svg width="120" height="120" viewBox="0 0 120 120" style="position: absolute; inset: 0"><circle cx="60" cy="18" r="13" fill="#F2EDE7"/><path d="M36 120 L38 46 Q40 34 52 34 L68 34 Q80 34 82 46 L84 120 Z" fill="#D9D1C8"/>
<path d="M40 40 L14 84 L54 96" fill="none" stroke="#F2EDE7" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" style="animation: aI2L 2s cubic-bezier(.65,0,.35,1) infinite"/>
<path d="M80 40 L106 84 L66 96" fill="none" stroke="#F2EDE7" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" style="animation: aI2R 2s cubic-bezier(.65,0,.35,1) infinite"/>
<rect x="48" y="88" width="24" height="16" rx="3" fill="#FF6A1A"/></svg></div>'''
fp = '<svg width="18" height="30" viewBox="0 0 30 52"><ellipse cx="15" cy="16" rx="12" ry="15" fill="#FF6A1A"/><ellipse cx="15" cy="42" rx="9" ry="9" fill="#FF6A1A"/></svg>'
icon3 = f'''<div style="position: relative; width: 120px; height: 120px; border-radius: 12px; border: 2px solid rgba(242,237,231,.4); overflow: hidden">
<div style="position: absolute; left: 38px; bottom: 10px; animation: aI3a 2s ease-out infinite">{fp}</div>
<div style="position: absolute; left: 64px; bottom: 44px; animation: aI3b 2s ease-out infinite">{fp}</div>
<div style="position: absolute; left: 38px; bottom: 78px; animation: aI3c 2s ease-out infinite">{fp}</div></div>'''
cards5 = ''.join(
    f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 14px; width: 270px; padding: 26px 0 24px; border-radius: 26px; background: #12100F; border: 3px solid rgba(242,237,231,.2); animation: {a} 4s {E} infinite">
  {ic}
  <span style="{MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; color: #FF6A1A">{n}</span>
  <span style="{BRIC}; font-weight: 800; font-size: 36px; letter-spacing: -0.03em; line-height: 1">{t}</span>
</div>''' for n, t, ic, a in (('01', 'Apoyo fijo', icon1, 'aHi1'), ('02', 'Codos pegados', icon2, 'aHi2'), ('03', 'Paso ninja', icon3, 'aHi3')))
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 80px; line-height: 1; letter-spacing: -0.045em">Antes de darle a REC,<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">decide dónde va el móvil.</span></p>
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
    '¿Cuál vas a probar en tu próximo vídeo?',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
