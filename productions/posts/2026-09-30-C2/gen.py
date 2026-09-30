#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C2 2026-09-30 (entrevistas a dos) en src/."""
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


# ============================================================ helpers C2 (entrevista a dos)
def profile(w, uid, col='#F2EDE7'):
    """Persona de perfil mirando a la DERECHA (viewBox 300x300)."""
    return f'''<svg width="{w}" height="{w}" viewBox="0 0 300 300" style="display:block; overflow: visible">
<defs><linearGradient id="q{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{col}" stop-opacity=".97"/><stop offset="1" stop-color="#B5ADA4" stop-opacity=".55"/></linearGradient></defs>
<path d="M36 300 C36 222 92 190 150 190 C208 190 262 222 262 300 Z" fill="url(#q{uid})"/>
<rect x="128" y="148" width="44" height="58" rx="18" fill="url(#q{uid})"/>
<ellipse cx="150" cy="98" rx="62" ry="72" fill="url(#q{uid})"/>
<path d="M204 86 L234 116 L206 124 Z" fill="url(#q{uid})"/>
<path d="M92 70 Q110 22 160 26 Q206 30 212 72 Q170 50 120 64 Z" fill="#0A0908" opacity=".35"/>
<ellipse cx="124" cy="104" rx="10" ry="16" fill="#0A0908" opacity=".22"/>
<rect x="182" y="88" width="16" height="7" rx="3.5" fill="#0A0908" opacity=".6"/>
</svg>'''


def gaze(len_=150, top=0, left=0, col='#FF6A1A'):
    return f'''<svg width="{len_}" height="30" viewBox="0 0 {len_} 30" style="position: absolute; left: {left}px; top: {top}px; overflow: visible">
<line x1="0" y1="15" x2="{len_-18}" y2="15" stroke="{col}" stroke-width="4" stroke-dasharray="10 8" style="animation: aDash 1s linear infinite"/>
<path d="M{len_-22} 3 L{len_} 15 L{len_-22} 27 Z" fill="{col}"/></svg>'''


def bg_set(glow_x='50%'):
    return f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #1C130D 0%, #12100F 70%, #0A0908 100%)"></div>
<div style="position: absolute; left: {glow_x}; top: 6%; width: 360px; height: 86%; margin-left: -180px; border-radius: 50%; background: radial-gradient(circle, rgba(255,106,26,.30), rgba(255,106,26,0) 70%); animation: aGlow 4s ease-in-out infinite"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 14%; background: linear-gradient(180deg, #171412, #0A0908); border-top: 2px solid rgba(242,237,231,.06)"></div>'''


def cam_icon(w=86):
    return f'''<svg width="{w}" height="{w*0.6:.0f}" viewBox="0 0 86 52" style="display:block; overflow: visible">
<path d="M86 26 L270 -40 L270 92 Z" fill="url(#fov)" opacity=".9"/>
<rect x="2" y="8" width="58" height="36" rx="8" fill="#F2EDE7"/>
<rect x="12" y="2" width="20" height="8" rx="3" fill="#F2EDE7"/>
<path d="M60 16 L82 8 L82 44 L60 36 Z" fill="#D9D1C8"/>
<circle cx="72" cy="26" r="7" fill="#0A0908"/><circle cx="72" cy="26" r="3" fill="#FF6A1A"/>
<circle cx="14" cy="18" r="4" fill="#FF3B30" style="animation: aRec 1s steps(1) infinite"/>
</svg>'''

FOV_DEFS = '''<svg width="0" height="0" style="position:absolute"><defs><linearGradient id="fov" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF6A1A" stop-opacity=".38"/><stop offset="1" stop-color="#FF6A1A" stop-opacity="0"/></linearGradient></defs></svg>'''


def rec_badge(left=26, top=22, label='REC'):
    return f'<div style="position: absolute; left: {left}px; top: {top}px; display: flex; align-items: center; gap: 10px; {MONO}; font-size: 19px; letter-spacing: .1em; color: #F2EDE7; z-index: 6"><span style="width: 13px; height: 13px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30; animation: aRec 1s steps(1) infinite"></span>{label}</div>'


# ---------------------------------------------------------------- 01 GANCHO
kf1 = COMMON_KF + """
@keyframes aDash{to{stroke-dashoffset:-36}}
@keyframes aTurn{0%,44%{transform:scaleX(1)}56%,90%{transform:scaleX(-1)}100%{transform:scaleX(1)}}
@keyframes aBad{0%,44%{opacity:1}52%,92%{opacity:0}100%{opacity:1}}
@keyframes aGood{0%,48%{opacity:0}56%,90%{opacity:1}98%,100%{opacity:0}}
@keyframes aBorder{0%,44%{border-color:#FF3B30;box-shadow:0 0 0 0 rgba(255,59,48,0), 0 40px 100px -40px rgba(255,59,48,.7)}56%,90%{border-color:#FF6A1A;box-shadow:0 0 0 0 rgba(255,106,26,0), 0 40px 100px -40px rgba(255,106,26,.8)}100%{border-color:#FF3B30}}
@keyframes aTalkA{0%,100%{transform:scaleY(.3)}25%{transform:scaleY(1)}50%{transform:scaleY(.5)}75%{transform:scaleY(.9)}}
@keyframes aWave{0%,100%{height:10px}50%{height:40px}}
"""


def panel1(side):
    left = side == 'A'
    px = 70 if left else 60
    turn = '' if left else 'animation: aTurn 4s cubic-bezier(.7,0,.3,1) infinite;'
    waves = ''.join(f'<span style="width: 6px; border-radius: 9px; background: #FF6A1A; animation: aWave {0.5+0.13*k:.2f}s ease-in-out {-0.1*k:.1f}s infinite"></span>' for k in range(6))
    return f'''<div style="position: relative; flex: 1; border-radius: 22px; overflow: hidden; border: 3px solid rgba(242,237,231,.16)">
{bg_set('38%' if left else '62%')}
{rec_badge(22, 20, 'CÁM ' + side)}
<div style="position: absolute; right: 22px; top: 18px; display: flex; align-items: center; gap: 5px; height: 40px; z-index: 6">{waves}</div>
<div style="position: absolute; left: {px}px; bottom: -8px; width: 330px; height: 330px; transform-origin: 50% 50%; {turn}">
  <div style="position: absolute; inset: 0; animation: aBreath 3s ease-in-out {'-1.2s' if left else '0s'} infinite; transform-origin: 50% 100%">{profile(250 if False else 250, 'h1' + side)}</div>
  {gaze(120, 88, 238)}
</div>
</div>'''


body1 = headline('PODCAST · ENTREVISTA', 'Grabaste la entrevista…', 'y parece que no se hablan.', 84) + f"""
<div style="position: relative; height: 640px; display: flex; flex-direction: column; gap: 20px">
  <div style="position: relative; height: 470px; border-radius: 28px; padding: 14px; box-sizing: border-box; display: flex; gap: 14px; background: #0A0908; border: 4px solid #FF3B30; animation: aBorder 4s ease-in-out infinite">
    {panel1('A')}{panel1('B')}
    <div style="position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); width: 70px; height: 70px; border-radius: 99px; background: #0A0908; border: 3px solid rgba(242,237,231,.2); display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 26px; z-index: 8">VS</div>
  </div>
  <div style="position: relative; flex: 1; border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); overflow: hidden">
    <div style="position: absolute; inset: 0; display: flex; align-items: center; gap: 20px; padding: 0 30px; animation: aBad 4s ease-in-out infinite">
      <span style="flex: none; width: 60px; height: 60px; border-radius: 99px; background: #FF3B30; color: #fff; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 34px">✗</span>
      <span style="{BRIC}; font-weight: 800; font-size: 38px; letter-spacing: -0.03em; line-height: 1.05">Los dos miran <span style="{SERIF}; color: #FF3B30; font-size: 46px">al mismo lado</span></span>
    </div>
    <div style="position: absolute; inset: 0; display: flex; align-items: center; gap: 20px; padding: 0 30px; opacity: 0; animation: aGood 4s ease-in-out infinite">
      <span style="flex: none; width: 60px; height: 60px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 34px">✓</span>
      <span style="{BRIC}; font-weight: 800; font-size: 38px; letter-spacing: -0.03em; line-height: 1.05">Ahora sí <span style="{SERIF}; color: #FF6A1A; font-size: 46px">se miran</span> (y conversan)</span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    '3 reglas de cámara para grabar a dos.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 EL EJE DE 180°
# persona A (300,210) mira →, persona B (620,210) mira ←. Cámaras: A en (140,56), B en (780,56) / cruzada (780,364)
kf2 = COMMON_KF + """
@keyframes aDash{to{stroke-dashoffset:-36}}
@keyframes aCamPos{0%,34%{left:737px;top:30px}52%,84%{left:737px;top:330px}100%{left:737px;top:30px}}
@keyframes aCamRot{0%,34%{transform:rotate(161.6deg)}52%,84%{transform:rotate(198.4deg)}100%{transform:rotate(161.6deg)}}
@keyframes aRedZone{0%,40%{opacity:0}52%,84%{opacity:1}94%,100%{opacity:0}}
@keyframes aBadOn{0%,44%{opacity:0;transform:translate(-50%,-50%) scale(.8)}52%,84%{opacity:1;transform:translate(-50%,-50%) scale(1)}92%,100%{opacity:0;transform:translate(-50%,-50%) scale(.8)}}
@keyframes aMonB{0%,44%{border-color:rgba(242,237,231,.18)}52%,84%{border-color:#FF3B30}92%,100%{border-color:rgba(242,237,231,.18)}}
@keyframes aFlipB{0%,44%{transform:scaleX(-1)}54%,84%{transform:scaleX(1)}94%,100%{transform:scaleX(-1)}}
@keyframes aTagOk{0%,44%{opacity:1}50%,86%{opacity:0}94%,100%{opacity:1}}
@keyframes aTagKo{0%,44%{opacity:0}50%,86%{opacity:1}94%,100%{opacity:0}}
@keyframes aAxis{0%,100%{opacity:.75}50%{opacity:1}}
"""


def head_top(x, y, facing, uid):
    rot = 0 if facing == 'r' else 180
    return f'''<div style="position: absolute; left: {x-60}px; top: {y-60}px; width: 120px; height: 120px; transform: rotate({rot}deg); z-index: 3">
<svg width="120" height="120" viewBox="0 0 120 120"><ellipse cx="60" cy="60" rx="54" ry="40" fill="#B5ADA4" opacity=".5"/><circle cx="60" cy="60" r="32" fill="#F2EDE7"/><path d="M88 50 L106 60 L88 70 Z" fill="#F2EDE7"/></svg>
<div style="position: absolute; left: 110px; top: 46px; width: 0; height: 0"></div></div>'''


def mon(label, facing, flip_anim=None, border_anim=None, uid='m'):
    px = 70 if facing == 'r' else 150
    fl = f'animation: {flip_anim} 4s cubic-bezier(.7,0,.3,1) infinite;' if flip_anim else ('transform: scaleX(-1);' if facing == 'l' else '')
    ba = f'animation: {border_anim} 4s ease-in-out infinite;' if border_anim else ''
    return f'''<div style="position: relative; flex: 1; border-radius: 18px; overflow: hidden; border: 4px solid rgba(242,237,231,.18); {ba}">
{bg_set('50%')}{rec_badge(18, 14, label)}
<div style="position: absolute; left: {110 if facing == 'r' else 190}px; bottom: -4px; width: 190px; height: 190px; {fl}"><div style="position: absolute; inset: 0; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{profile(150, uid)}</div>{gaze(70, 50, 146)}</div>
</div>'''


body2 = headline('REGLA 1 · EL EJE', 'Hay una línea invisible', 'que no puedes cruzar.', 84) + f"""
<div style="position: relative; height: 680px; display: flex; flex-direction: column; gap: 16px">
  <div style="position: relative; height: 420px; border-radius: 28px; overflow: hidden; background: #12100F; border: 2px solid rgba(242,237,231,.14)">
    {FOV_DEFS}
    <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(242,237,231,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(242,237,231,0.05) 1px, transparent 1px); background-size: 40px 40px"></div>
    <div style="position: absolute; left: 0; right: 0; top: 0; height: 210px; background: linear-gradient(180deg, rgba(255,106,26,.13), rgba(255,106,26,.03))"></div>
    <div style="position: absolute; left: 0; right: 0; top: 210px; bottom: 0; background: linear-gradient(0deg, rgba(255,59,48,.30), rgba(255,59,48,.06)); opacity: 0; animation: aRedZone 4s ease-in-out infinite"></div>
    <div style="position: absolute; left: 22px; top: 176px; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .1em; color: #FF6A1A">LADO BUENO ↑</div>
    <div style="position: absolute; left: 0; right: 0; top: 207px; height: 0; border-top: 5px dashed #FF6A1A; animation: aAxis 2s ease-in-out infinite"></div>
    <div style="position: absolute; right: 22px; top: 222px; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .1em; color: #F2EDE7; background: #0A0908; padding: 6px 12px; border-radius: 8px">EJE 180°</div>
    <div style="position: absolute; left: 350px; top: 160px; width: 220px; height: 100px; border-radius: 50%; background: #1E1A17; border: 3px solid rgba(242,237,231,.18)"></div>
    {head_top(300, 210, 'r', 'a')}{head_top(620, 210, 'l', 'b')}
    <div style="position: absolute; left: 97px; top: 30px; width: 86px; height: 52px; transform: rotate(18.4deg); z-index: 4">{cam_icon()}</div>
    <div style="position: absolute; left: 737px; top: 30px; width: 86px; height: 52px; z-index: 5; animation: aCamPos 4s cubic-bezier(.7,0,.3,1) infinite"><div style="width: 86px; height: 52px; animation: aCamRot 4s cubic-bezier(.7,0,.3,1) infinite">{cam_icon()}</div></div>
    <div style="position: absolute; left: 110px; top: 92px; {MONO}; font-weight: 600; font-size: 18px; color: #F2EDE7; z-index: 6">A</div>
    <div style="position: absolute; left: 50%; top: 330px; white-space: nowrap; padding: 12px 20px; border-radius: 14px; background: #FF3B30; color: #fff; {BRIC}; font-weight: 800; font-size: 30px; z-index: 7; opacity: 0; animation: aBadOn 4s ease-in-out infinite">✗ CÁM B cruzó el eje</div>
  </div>
  <div style="position: relative; flex: 1; display: flex; gap: 16px">
    {mon('CÁM A', 'r', uid='ma')}
    {mon('CÁM B', 'l', 'aFlipB', 'aMonB', uid='mb')}
  </div>
  <div style="position: relative; height: 50px">
    <div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 32px; letter-spacing: -0.02em; animation: aTagOk 4s steps(1) infinite">Cámaras del mismo lado → <span style="{SERIF}; color: #FF6A1A; font-size: 40px; margin-left: 10px">se miran</span></div>
    <div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 32px; letter-spacing: -0.02em; opacity: 0; animation: aTagKo 4s steps(1) infinite">Cruzas la línea → <span style="{SERIF}; color: #FF3B30; font-size: 40px; margin-left: 10px">se dan la espalda</span></div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · El eje', 2, kf2, body2,
    'Todas las cámaras, a un solo lado.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 AIRE HACIA LA MIRADA
kf3 = COMMON_KF + """
@keyframes aDash{to{stroke-dashoffset:-36}}
@keyframes aSlide{0%,30%{left:520px}50%,88%{left:120px}100%{left:520px}}
@keyframes aAir{0%,38%{opacity:0;transform:scaleX(.2)}54%,86%{opacity:1;transform:scaleX(1)}96%,100%{opacity:0;transform:scaleX(.2)}}
@keyframes aNoAir{0%,30%{opacity:1}40%,92%{opacity:0}100%{opacity:1}}
@keyframes aKoTag{0%,32%{opacity:1;transform:scale(1)}40%,92%{opacity:0;transform:scale(.85)}100%{opacity:1}}
@keyframes aOkTag{0%,48%{opacity:0;transform:scale(.85)}56%,86%{opacity:1;transform:scale(1)}94%,100%{opacity:0}}
@keyframes aFr{0%,34%{border-color:#FF3B30}50%,88%{border-color:#FF6A1A}100%{border-color:#FF3B30}}
@keyframes aCard1{0%,45%{border-color:#FF6A1A;background:#1E1A17;transform:translateY(-6px)}55%,100%{border-color:rgba(242,237,231,.14);background:#12100F;transform:none}}
@keyframes aCard2{0%,45%{border-color:rgba(242,237,231,.14);background:#12100F;transform:none}55%,95%{border-color:#FF6A1A;background:#1E1A17;transform:translateY(-6px)}100%{border-color:rgba(242,237,231,.14);background:#12100F}}
@keyframes aEye{0%,100%{transform:translateX(0)}50%{transform:translateX(6px)}}
"""
grid3 = ''.join(f'<div style="position: absolute; {p}: {v}; {"top: 0; bottom: 0; width: 2px" if p == "left" else "left: 0; right: 0; height: 2px"}; background: rgba(242,237,231,.18); z-index: 4"></div>' for p, v in (('left', '33.33%'), ('left', '66.66%'), ('top', '33.33%'), ('top', '66.66%')))
body3 = headline('REGLA 2 · LA MIRADA', 'Deja aire', 'hacia donde mira.', 94) + f"""
<div style="position: relative; height: 650px; display: flex; flex-direction: column; gap: 18px">
  <div style="position: relative; height: 450px; border-radius: 26px; overflow: hidden; border: 4px solid #FF3B30; animation: aFr 4s ease-in-out infinite">
    {bg_set('50%')}{grid3}
    <div style="position: absolute; inset: 22px; z-index: 5">{corners()}</div>
    {rec_badge(50, 42, 'REC · CÁM A')}
    <div style="position: absolute; left: 470px; top: 60px; width: 400px; height: 330px; border-radius: 22px; background: repeating-linear-gradient(135deg, rgba(255,106,26,.22) 0 14px, rgba(255,106,26,.08) 14px 28px); border: 3px dashed #FF6A1A; transform-origin: 0 50%; z-index: 3; opacity: 0; animation: aAir 4s cubic-bezier(.7,0,.3,1) infinite; display: flex; align-items: center; justify-content: center"><span style="{BRIC}; font-weight: 800; font-size: 42px; color: #FF6A1A; letter-spacing: -0.02em">AIRE →</span></div>
    <div style="position: absolute; left: 520px; bottom: -14px; width: 330px; height: 330px; z-index: 4; animation: aSlide 4s cubic-bezier(.7,0,.3,1) infinite">
      <div style="position: absolute; inset: 0; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{profile(310, 'c3')}</div>
    </div>
    <div style="position: absolute; right: 26px; top: 0; bottom: 0; width: 60px; background: linear-gradient(90deg, rgba(255,59,48,0), rgba(255,59,48,.45)); z-index: 3; animation: aNoAir 4s ease-in-out infinite"></div>
    <div style="position: absolute; right: 44px; bottom: 34px; padding: 12px 20px; border-radius: 14px; background: #FF3B30; color: #fff; {BRIC}; font-weight: 800; font-size: 30px; z-index: 7; animation: aKoTag 4s ease-in-out infinite">✗ Nariz contra el borde</div>
    <div style="position: absolute; right: 44px; bottom: 34px; padding: 12px 20px; border-radius: 14px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 30px; z-index: 7; opacity: 0; animation: aOkTag 4s ease-in-out infinite">✓ En el tercio, con aire</div>
  </div>
  <div style="position: relative; flex: 1; display: flex; gap: 18px">
    <div style="flex: 1; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); padding: 22px 24px; display: flex; gap: 18px; align-items: center; animation: aCard1 4s ease-in-out infinite">
      <span style="flex: none; width: 58px; height: 58px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 30px">👀</span>
      <span style="{BRIC}; font-weight: 800; font-size: 30px; line-height: 1.08; letter-spacing: -0.02em">Mira a quien pregunta, <span style="{SERIF}; color: #FF6A1A; font-size: 36px">no a la cámara</span></span>
    </div>
    <div style="flex: 1; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); padding: 22px 24px; display: flex; gap: 18px; align-items: center; animation: aCard2 4s ease-in-out infinite">
      <span style="flex: none; width: 58px; height: 58px; border-radius: 99px; background: #FF6A1A; color: #0A0908; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 30px">🎥</span>
      <span style="{BRIC}; font-weight: 800; font-size: 30px; line-height: 1.08; letter-spacing: -0.02em">Cámara junto al hombro <span style="{SERIF}; color: #FF6A1A; font-size: 36px">de quien pregunta</span></span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · La mirada', 3, kf3, body3,
    'Así la mirada queda casi a cámara, natural.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 PLANO · CONTRAPLANO · GENERAL
kf4 = COMMON_KF + """
@keyframes aDash{to{stroke-dashoffset:-36}}
@keyframes aS1{0%,32%{opacity:1}33.4%,100%{opacity:0}}
@keyframes aS2{0%,32%{opacity:0}33.4%,65.9%{opacity:1}66.7%,100%{opacity:0}}
@keyframes aS3{0%,65.9%{opacity:0}66.7%,100%{opacity:1}}
@keyframes aZoom{0%{transform:scale(1)}100%{transform:scale(1.06)}}
@keyframes aHead{0%{left:0%}100%{left:100%}}
@keyframes aC1{0%,32%{background:#FF6A1A;color:#0A0908;box-shadow:0 0 30px rgba(255,106,26,.7)}33.4%,100%{background:#1E1A17;color:#9C938B;box-shadow:none}}
@keyframes aC2{0%,32%{background:#1E1A17;color:#9C938B;box-shadow:none}33.4%,65.9%{background:#FF6A1A;color:#0A0908;box-shadow:0 0 30px rgba(255,106,26,.7)}66.7%,100%{background:#1E1A17;color:#9C938B;box-shadow:none}}
@keyframes aC3{0%,65.9%{background:#1E1A17;color:#9C938B;box-shadow:none}66.7%,100%{background:#FF6A1A;color:#0A0908;box-shadow:0 0 30px rgba(255,106,26,.7)}}
@keyframes aFlash{0%{opacity:.28}8%,100%{opacity:0}}
"""


def shot(inner, anim, label):
    return f'''<div style="position: absolute; inset: 0; opacity: 0; animation: {anim} 4s steps(1) infinite">
<div style="position: absolute; inset: 0; animation: aZoom 1.333s linear infinite">{inner}</div>
<div style="position: absolute; left: 24px; bottom: 22px; padding: 10px 16px; border-radius: 12px; background: rgba(10,9,8,.8); border: 2px solid #FF6A1A; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; color: #FF6A1A; z-index: 6">{label}</div></div>'''


shotA = bg_set('35%') + f'<div style="position: absolute; left: 110px; bottom: -14px; width: 340px; height: 340px"><div style="position: absolute; inset: 0; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{profile(320, "sa")}</div>{gaze(150, 104, 300)}</div>'
shotB = bg_set('65%') + f'<div style="position: absolute; right: 150px; bottom: -14px; width: 340px; height: 340px; transform: scaleX(-1)"><div style="position: absolute; inset: 0; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{profile(320, "sb", "#D9D1C8")}</div>{gaze(150, 104, 300)}</div>'
shotG = bg_set('50%') + f'''<div style="position: absolute; left: 50%; bottom: 30px; width: 420px; height: 70px; margin-left: -210px; border-radius: 16px; background: #1E1A17; border: 3px solid rgba(242,237,231,.2); z-index: 3"></div>
<div style="position: absolute; left: 190px; bottom: 40px; width: 230px; height: 230px">{profile(210, "ga")}</div>
<div style="position: absolute; right: 190px; bottom: 40px; width: 230px; height: 230px; transform: scaleX(-1)">{profile(210, "gb", "#D9D1C8")}</div>'''


def track(name, blocks, anim):
    bl = ''.join(f'<div style="position: absolute; left: {a}%; width: {b-a}%; top: 6px; bottom: 6px; border-radius: 10px; animation: {anim} 4s steps(1) infinite; display: flex; align-items: center; padding-left: 14px; box-sizing: border-box; {MONO}; font-weight: 600; font-size: 17px; letter-spacing: .08em">{name}</div>' for a, b in blocks)
    return f'<div style="position: relative; height: 62px; border-radius: 12px; background: #0A0908; border: 2px solid rgba(242,237,231,.08)">{bl}</div>'


body4 = headline('REGLA 3 · EL MONTAJE', 'Plano, contraplano', 'y un general para respirar.', 80) + f"""
<div style="position: relative; height: 660px; display: flex; flex-direction: column; gap: 18px">
  <div style="position: relative; height: 420px; border-radius: 26px; overflow: hidden; border: 3px solid rgba(242,237,231,.18); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">
    {shot(shotA, 'aS1', 'PLANO · HABLA A')}{shot(shotB, 'aS2', 'CONTRAPLANO · RESPONDE B')}{shot(shotG, 'aS3', 'GENERAL · LOS DOS')}
    <div style="position: absolute; inset: 0; background: #F2EDE7; z-index: 8; pointer-events: none; animation: aFlash 1.333s linear infinite"></div>
    {rec_badge(26, 22, 'MONTAJE')}
  </div>
  <div style="position: relative; flex: 1; border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 20px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">
    <div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 10px">
      {track('CÁM A', [(0, 33.3)], 'aC1')}
      {track('CÁM B', [(33.3, 66.6)], 'aC2')}
      {track('GENERAL', [(66.6, 100)], 'aC3')}
      <div style="position: absolute; top: -8px; bottom: -8px; left: 0; width: 0; z-index: 5; animation: aHead 4s linear infinite"><div style="position: absolute; left: -2px; top: 0; bottom: 0; width: 4px; background: #F2EDE7; box-shadow: 0 0 14px #F2EDE7"></div><div style="position: absolute; left: -10px; top: -6px; width: 20px; height: 14px; border-radius: 4px; background: #F2EDE7"></div></div>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · El montaje', 4, kf4, body4,
    'Corta cuando cambia quien habla.', DESLIZA_TXT))

# ---------------------------------------------------------------- 05 CTA
kf5 = COMMON_KF + chk_kf(5, [8, 30, 52]) + """
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
@keyframes aFol{0%,46%{opacity:1}50%,100%{opacity:0}}
@keyframes aFolD{0%,46%{opacity:0}50%,100%{opacity:1}}
@keyframes aFolBg{0%,46%{background:#FF6A1A;color:#0A0908}50%,100%{background:#1E1A17;color:#F2EDE7}}
@keyframes aTap{0%,36%{opacity:0;transform:scale(1.4)}42%{opacity:1;transform:scale(1)}48%{opacity:1;transform:scale(.85)}56%,100%{opacity:0;transform:scale(1)}}
"""
items5 = ['<span style="color:#FF6A1A">1 ·</span> Todas las cámaras a un lado del eje',
          '<span style="color:#FF6A1A">2 ·</span> Aire hacia donde mira cada uno',
          '<span style="color:#FF6A1A">3 ·</span> Plano, contraplano y general']
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 84px; line-height: 1; letter-spacing: -0.045em">Una buena charla<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">también se graba bien.</span></p>
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
    'Guárdalo para tu próximo podcast.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
