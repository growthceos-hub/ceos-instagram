#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel C1 2026-10-09 (captación: cómo es una sesión en el estudio) en src/."""
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





# ============================================================ C1 2026-10-09 · Captación: cómo es una sesión en el estudio
def wave(n, anim_prefix, h=90, w=10, gap=6, col='#FF6A1A'):
    return ''.join(
        f'<span style="width: {w}px; height: {h}px; border-radius: 99px; background: {col}; transform-origin: 50% 50%; animation: {anim_prefix} {0.9 + (i % 5) * 0.13:.2f}s ease-in-out {-(i * 0.17):.2f}s infinite"></span>'
        for i in range(n))


def gperson(w, uid, c1='#C9CCC2', c2='#7C8077'):
    return (PERSON.replace('width="420" height="420"', f'width="{w}" height="{w}"')
            .replace('id="pg"', f'id="{uid}"').replace('url(#pg)', f'url(#{uid})')
            .replace('stop-color="#F2EDE7" stop-opacity=".95"', f'stop-color="{c1}" stop-opacity="1"')
            .replace('stop-color="#B5ADA4" stop-opacity=".55"', f'stop-color="{c2}" stop-opacity=".9"'))


# ---------------------------------------------------------------- 01 GANCHO · antes/después oficina vs estudio
kf1 = COMMON_KF + """
@keyframes aWipe{0%,8%{clip-path:inset(0 0 0 58%)}46%,58%{clip-path:inset(0 0 0 22%)}96%,100%{clip-path:inset(0 0 0 58%)}}
@keyframes aDiv{0%,8%{left:58%}46%,58%{left:22%}96%,100%{left:58%}}
@keyframes aFlick{0%,100%{opacity:1}7%{opacity:.35}9%{opacity:1}31%{opacity:.5}33%{opacity:1}64%{opacity:.25}66%{opacity:.9}68%{opacity:.4}70%{opacity:1}}
@keyframes aShake{0%,100%{transform:translate(0,0) rotate(-2.2deg)}20%{transform:translate(-7px,4px) rotate(-1deg)}40%{transform:translate(5px,-3px) rotate(-3deg)}60%{transform:translate(-4px,-5px) rotate(-1.6deg)}80%{transform:translate(6px,3px) rotate(-2.8deg)}}
@keyframes aNoise{0%,100%{transform:scaleY(.25)}30%{transform:scaleY(1)}55%{transform:scaleY(.45)}75%{transform:scaleY(.9)}}
@keyframes aClean{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(.8)}}
@keyframes aBat{0%,49%{opacity:1}50%,100%{opacity:.25}}
@keyframes aTagO{0%,40%{opacity:1;transform:none}48%,90%{opacity:.0;transform:translateY(-8px)}98%,100%{opacity:1;transform:none}}
@keyframes aKnob{0%,100%{box-shadow:0 0 0 0 rgba(255,106,26,.6)}50%{box-shadow:0 0 0 18px rgba(255,106,26,0)}}
"""
office = f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #3B3D38 0%, #2B2D29 70%, #20211E 100%)"></div>
<div style="position: absolute; left: 60px; right: 60px; top: 0; height: 14px; border-radius: 0 0 8px 8px; background: #E9F2CF; box-shadow: 0 0 60px 14px rgba(233,242,207,.35); animation: aFlick 2.2s steps(1) infinite"></div>
<div style="position: absolute; left: 36px; top: 70px; width: 170px; height: 230px; border: 6px solid #55574F; background: linear-gradient(160deg, #6E7366, #4A4D45)"></div>
<div style="position: absolute; left: 36px; top: 180px; width: 170px; height: 6px; background: #55574F"></div>
<div style="position: absolute; right: 30px; top: 110px; width: 120px; height: 340px; background: #34362F; border: 3px solid #44463F"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 15%; background: #1A1B18; border-top: 3px solid #44463F"></div>
<div style="position: absolute; left: 50%; bottom: -10px; width: 380px; margin-left: -190px; animation: aShake 0.9s ease-in-out infinite; transform-origin: 50% 100%">{gperson(380, 'go')}</div>
<div style="position: absolute; left: 22px; bottom: 26px; display: flex; align-items: center; gap: 5px; height: 70px; z-index: 4">{wave(14, 'aNoise', 64, 8, 5, '#C9CCC2')}</div>
<div style="position: absolute; left: 24px; top: 22px; display: flex; align-items: center; gap: 10px; {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .1em; color: #C9CCC2; z-index: 4">
  <span style="display: inline-block; width: 40px; height: 20px; border: 2px solid #C9CCC2; border-radius: 5px; position: relative"><span style="position: absolute; left: 2px; top: 2px; bottom: 2px; width: 5px; background: #FF3B30; animation: aBat 1s steps(1) infinite"></span></span>3% · MÓVIL</div>
<div style="position: absolute; left: 24px; top: 330px; display: flex; flex-direction: column; gap: 10px; z-index: 5; animation: aTagO 4s ease-in-out infinite">
  {''.join(f'<span style="align-self: flex-start; white-space: nowrap; padding: 8px 14px; border-radius: 10px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .08em">{t}</span>' for t in ('✕ LUZ DEL TECHO', '✕ ECO', '✕ PULSO'))}
</div>
'''
studio1 = f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #1C130D 0%, #12100F 70%, #0A0908 100%)"></div>
<div style="position: absolute; left: 50%; top: 4%; width: 620px; height: 90%; margin-left: -310px; border-radius: 50%; background: radial-gradient(circle, rgba(255,106,26,.34), rgba(255,106,26,0) 70%); animation: aGlow 4s ease-in-out infinite"></div>
{softbox('l')}{softbox('r')}
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 15%; background: linear-gradient(180deg, #171412, #0A0908); border-top: 2px solid rgba(242,237,231,.06)"></div>
<div style="position: absolute; left: 50%; bottom: -10px; width: 380px; margin-left: -190px; animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{person(380)}</div>
<div style="position: absolute; right: 22px; bottom: 26px; display: flex; align-items: center; gap: 5px; height: 70px; z-index: 4">{wave(14, 'aClean', 56, 8, 5)}</div>
{rec_timer()}
<div style="position: absolute; right: 24px; top: 330px; display: flex; flex-direction: column; align-items: flex-end; gap: 10px; z-index: 5">
  {''.join(f'<span style="white-space: nowrap; padding: 8px 14px; border-radius: 10px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .08em">{t}</span>' for t in ('✓ LUZ QUE FAVORECE', '✓ SONIDO LIMPIO', '✓ PLANO FIJO'))}
</div>
<div style="position: absolute; inset: 0; pointer-events: none">{corners()}</div>
'''
panel1 = f'''<div style="position: relative; height: 640px; border-radius: 28px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">
<div style="position: absolute; inset: 0">{office}</div>
<div style="position: absolute; inset: 0; animation: aWipe 4s {E} infinite">{studio1}</div>
<div style="position: absolute; top: 0; bottom: 0; left: 58%; width: 0; z-index: 8; animation: aDiv 4s {E} infinite">
  <div style="position: absolute; top: 0; bottom: 0; left: -3px; width: 6px; background: #F2EDE7; box-shadow: 0 0 30px rgba(255,106,26,.8)"></div>
  <div style="position: absolute; top: 50%; left: -34px; width: 68px; height: 68px; margin-top: -34px; border-radius: 99px; background: #F2EDE7; display: flex; align-items: center; justify-content: center; animation: aKnob 1.4s ease-out infinite">
    <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l-6 6 6 6M15 6l6 6-6 6"/></svg></div>
  <div style="position: absolute; bottom: 120px; right: 16px; white-space: nowrap; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .14em; color: #F2EDE7; background: rgba(0,0,0,.55); padding: 6px 10px; border-radius: 8px">OFICINA</div>
  <div style="position: absolute; bottom: 120px; left: 16px; white-space: nowrap; {MONO}; font-weight: 600; font-size: 18px; letter-spacing: .14em; color: #0A0908; background: #FF6A1A; padding: 6px 10px; border-radius: 8px">ESTUDIO</div>
</div>
</div>'''
body1 = headline('ESTUDIO EN BURGOS', '¿Tus vídeos parecen<br>hechos en la oficina?', 'Es que lo están.', 84) + panel1
open(os.path.join(OUT, 'Main.dc.html'), 'w').write(page('01 · Gancho', 1, kf1, body1,
    'Así es grabar en un estudio de verdad.', DESLIZA_PILL))

# ---------------------------------------------------------------- 02 PROBLEMA · interrupciones en la oficina
kf2 = COMMON_KF + """
@keyframes aI{0%,100%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}
@keyframes aCut{0%,4%{opacity:0;transform:scale(1.6) rotate(-14deg)}9%,22%{opacity:1;transform:scale(1) rotate(-14deg)}25%,100%{opacity:0;transform:scale(1) rotate(-14deg)}}
@keyframes aRecDot{0%,4%{opacity:1}5%,24%{opacity:.15}25%,100%{opacity:1}}
@keyframes aTilt{0%,100%{transform:rotate(0)}50%{transform:rotate(-1.5deg) translateX(-6px)}}
@keyframes aBarP{0%{width:0%}100%{width:100%}}
"""
# 4 interrupciones, una por segundo: cada tarjeta se ilumina en su segundo y la cámara marca CORTE
for i in range(4):
    s = i * 25
    kf2 += (f"@keyframes aIn{i}{{0%,{max(s-0.1,0)}%{{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}"
            f"{s+3}%,{s+21}%{{background:#1E1A17;border-color:#FF3B30;transform:translateX(-12px)}}"
            f"{s+25}%,100%{{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}}}}\n")
    kf2 += (f"@keyframes aIc{i}{{0%,{max(s-0.1,0)}%{{transform:scale(1)}}{s+5}%{{transform:scale(1.3)}}{s+10}%,100%{{transform:scale(1)}}}}\n")
if True:
    # el primer segmento empieza en 0: forzamos que la tarjeta 0 arranque iluminada
    kf2 = kf2.replace('@keyframes aIn0{0%,0%{background:#12100F;border-color:rgba(242,237,231,.14);transform:none}3%,21%',
                      '@keyframes aIn0{0%,21%')
ints = (('📞', 'Te llaman', 'justo en la mejor toma'),
        ('🔊', 'Ruido de fondo', 'la calle, la impresora, el pasillo'),
        ('🙋', '"¿Tienes un minuto?"', 'y se corta el ritmo'),
        ('🌥️', 'Cambia la luz', 'y la toma anterior ya no casa'))
cards2 = ''.join(
    f'''<div style="display: flex; align-items: center; gap: 18px; padding: 18px 20px; border-radius: 22px; border: 2px solid rgba(242,237,231,.14); background: #12100F; animation: aIn{i} 4s {E} infinite">
<span style="flex: none; width: 62px; height: 62px; border-radius: 16px; background: #0A0908; border: 2px solid rgba(242,237,231,.14); display: flex; align-items: center; justify-content: center; font-size: 32px; animation: aIc{i} 4s ease-out infinite">{ic}</span>
<span style="display: flex; flex-direction: column; gap: 4px"><span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em; line-height: 1.05">{t}</span><span style="font-size: 21px; color: #B5ADA4">{d}</span></span></div>'''
    for i, (ic, t, d) in enumerate(ints))
cam2 = f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #3B3D38 0%, #2B2D29 70%, #20211E 100%)"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 15%; background: #1A1B18; border-top: 3px solid #44463F"></div>
<div style="position: absolute; left: 50%; bottom: -10px; width: 300px; margin-left: -150px; animation: aTilt 2s ease-in-out infinite; transform-origin: 50% 100%">{gperson(300, 'g2')}</div>
<div style="position: absolute; inset: 18px; pointer-events: none">{corners()}</div>
<div style="position: absolute; left: 34px; top: 34px; display: flex; align-items: center; gap: 10px; {MONO}; font-size: 20px; letter-spacing: .1em; color: #F2EDE7; z-index: 5"><span style="width: 14px; height: 14px; border-radius: 99px; background: #FF3B30; box-shadow: 0 0 12px #FF3B30; animation: aRecDot 1s steps(1) infinite"></span>REC</div>
<div style="position: absolute; right: 34px; top: 30px; width: 150px; height: 30px; {MONO}; font-weight: 600; font-size: 22px; letter-spacing: .08em; color: #F2EDE7; text-align: right; z-index: 5">{cycle(['TOMA 11', 'TOMA 12', 'TOMA 13', 'TOMA 14'], 'text-align: right')}</div>
<div style="position: absolute; left: 50%; top: 42%; margin-left: -130px; width: 260px; padding: 14px 0; text-align: center; border: 6px solid #FF3B30; border-radius: 14px; color: #FF3B30; {BRIC}; font-weight: 800; font-size: 54px; letter-spacing: .02em; background: rgba(10,9,8,.55); z-index: 6; animation: aCut 1s ease-out infinite">¡CORTA!</div>
<div style="position: absolute; left: 34px; right: 34px; bottom: 30px; height: 8px; border-radius: 99px; background: rgba(242,237,231,.18); overflow: hidden; z-index: 5"><div style="height: 100%; background: #FF3B30; animation: aBarP 1s linear infinite"></div></div>
'''
body2 = headline('EL PROBLEMA', 'Grabar en la oficina:', 'toma 14 y sigue sin salir.', 76) + f"""
<div style="position: relative; height: 650px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: 420px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,59,48,.35)">{cam2}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 14px">{cards2}
    <div style="margin-top: 6px; padding: 20px 22px; border-radius: 22px; background: #0A0908; border: 2px dashed #FF6A1A">
      <span style="{BRIC}; font-weight: 800; font-size: 27px; letter-spacing: -0.02em; line-height: 1.12">No eres tú. Es que la oficina <span style="{SERIF}; color: #FF6A1A; font-size: 33px">no es un set.</span></span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S2.dc.html'), 'w').write(page('02 · El problema', 2, kf2, body2,
    'Una tarde entera para un vídeo que no te convence.', DESLIZA_TXT))

# ---------------------------------------------------------------- 03 LA SESIÓN · el set ya está montado
kf3 = COMMON_KF + chk_kf(3, [4, 26, 48, 70]) + """
@keyframes aOnK{0%,4%{opacity:.08;filter:none}10%,94%{opacity:1}100%{opacity:.08}}
@keyframes aOnF{0%,26%{opacity:.08}32%,94%{opacity:1}100%{opacity:.08}}
@keyframes aOnB{0%,48%{opacity:.0}54%,94%{opacity:1}100%{opacity:0}}
@keyframes aOnR{0%,70%{opacity:0}76%,94%{opacity:1}100%{opacity:0}}
@keyframes aOnP{0%,4%{filter:brightness(.35)}12%,26%{filter:brightness(.75)}34%,94%{filter:brightness(1)}100%{filter:brightness(.35)}}
@keyframes aMic{0%,26%{transform:scaleY(.08)}32%,94%{transform:scaleY(1)}100%{transform:scaleY(.08)}}
@keyframes aLvl{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
"""
SB = lambda side, anim: f'''<div style="position: absolute; {side}; top: 70px; width: 104px; z-index: 3">
<div style="width: 104px; height: 140px; border-radius: 12px; background: linear-gradient(180deg, #FFFFFF, #D9D1C8); transform: perspective(300px) rotateY({'14deg' if 'left' in side else '-14deg'}); box-shadow: 0 0 80px 22px rgba(255,178,122,.45); animation: {anim} 4s {E} infinite"></div>
<div style="margin: 0 auto; width: 6px; height: 170px; background: #6B635C"></div></div>'''
set3 = f'''<div style="position: absolute; inset: 0; background: linear-gradient(180deg, #1C130D 0%, #12100F 70%, #0A0908 100%)"></div>
<div style="position: absolute; left: 50%; top: 6%; width: 520px; height: 86%; margin-left: -260px; border-radius: 50%; background: radial-gradient(circle, rgba(255,106,26,.36), rgba(255,106,26,0) 70%); animation: aOnB 4s {E} infinite"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 15%; background: linear-gradient(180deg, #171412, #0A0908); border-top: 2px solid rgba(242,237,231,.06)"></div>
{SB('left: 22px', 'aOnK')}{SB('right: 22px', 'aOnF')}
<div style="position: absolute; left: 50%; bottom: -10px; width: 300px; margin-left: -150px; animation: aOnP 4s {E} infinite"><div style="animation: aBreath 3s ease-in-out infinite; transform-origin: 50% 100%">{person(300)}</div></div>
<div style="position: absolute; left: 50%; top: 0; margin-left: -96px; width: 5px; height: 300px; background: linear-gradient(180deg, #1E1A17, #6B635C); z-index: 4"></div>
<div style="position: absolute; left: 50%; top: 290px; margin-left: -112px; width: 38px; height: 62px; border-radius: 19px; background: linear-gradient(180deg, #D9D1C8, #6B635C); transform: rotate(-24deg); z-index: 4; box-shadow: 0 0 0 4px rgba(10,9,8,.5)"></div>
<div style="position: absolute; left: 22px; right: 22px; bottom: 22px; height: 60px; border-radius: 14px; background: rgba(10,9,8,.75); border: 2px solid rgba(242,237,231,.14); display: flex; align-items: center; gap: 14px; padding: 0 16px; z-index: 6">
  <span style="{MONO}; font-weight: 600; font-size: 16px; letter-spacing: .1em; color: #9C938B">AUDIO</span>
  <div style="flex: 1; height: 36px; display: flex; align-items: center; gap: 4px; transform-origin: 50% 50%; animation: aMic 4s {E} infinite">{wave(22, 'aLvl', 32, 6, 4)}</div>
</div>
<div style="position: absolute; left: 22px; top: 20px; display: flex; align-items: center; gap: 10px; padding: 8px 14px; border-radius: 10px; background: #FF3B30; color: #fff; {MONO}; font-weight: 600; font-size: 19px; letter-spacing: .1em; z-index: 6; animation: aOnR 4s {E} infinite"><span style="width: 12px; height: 12px; border-radius: 99px; background: #fff; animation: aRec 1s steps(1) infinite"></span>REC</div>
'''
body3 = headline('LA SESIÓN', 'Llegas y el set<br>ya está montado.', 'Tú solo hablas.', 88) + f"""
<div style="position: relative; height: 640px; display: flex; gap: 24px">
  <div style="position: relative; flex: none; width: 470px; border-radius: 30px; overflow: hidden; border: 2px solid rgba(242,237,231,.16); box-shadow: 0 50px 120px -40px rgba(255,106,26,.55)">{set3}</div>
  <div style="position: relative; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 16px">
    <div style="border-radius: 24px; background: #12100F; border: 2px solid rgba(242,237,231,.14); padding: 20px 18px; display: flex; flex-direction: column; gap: 12px">
      <span style="{MONO}; font-size: 18px; letter-spacing: .12em; color: #9C938B; padding-left: 4px">CUANDO LLEGAS YA ESTÁ</span>
      {ticklist(['La luz colocada', 'El sonido preparado', 'Cámara y encuadre', 'Grabando'], [('a3Row1', 'a3Tk1'), ('a3Row2', 'a3Tk2'), ('a3Row3', 'a3Tk3'), ('a3Row4', 'a3Tk4')])}
    </div>
    <div style="padding: 20px 22px; border-radius: 22px; background: #0A0908; border: 2px dashed #FF6A1A">
      <span style="font-size: 23px; color: #D9D1C8; line-height: 1.3">Sin montar nada, sin pelearte con el móvil: <b style="color: #F2EDE7">te sientas y grabas.</b></span>
    </div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S3.dc.html'), 'w').write(page('03 · El set', 3, kf3, body3,
    'Tu energía, en lo que dices. No en el trípode.', DESLIZA_TXT))

# ---------------------------------------------------------------- 04 QUÉ GRABAS + CÓMO RESERVAR
kf4 = COMMON_KF + """
@keyframes aDot{0%,6%{left:0%}30%,40%{left:50%}64%,94%{left:100%}100%{left:0%}}
@keyframes aFill{0%,6%{width:0%}30%,40%{width:50%}64%,94%{width:100%}100%{width:0%}}
@keyframes aSt1{0%,94%{background:#FF6A1A;color:#0A0908}100%{background:#12100F;color:#F2EDE7}}
@keyframes aSt2{0%,28%{background:#12100F;color:#F2EDE7}32%,94%{background:#FF6A1A;color:#0A0908}100%{background:#12100F;color:#F2EDE7}}
@keyframes aSt3{0%,62%{background:#12100F;color:#F2EDE7}66%,94%{background:#FF6A1A;color:#0A0908}100%{background:#12100F;color:#F2EDE7}}
@keyframes aSpin{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}
@keyframes aPlay{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
@keyframes aFlash{0%,80%{opacity:0}84%{opacity:1}100%{opacity:0}}
@keyframes aTalk{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
@keyframes aProg{0%{width:8%}100%{width:100%}}
@keyframes aTile{0%,100%{border-color:rgba(242,237,231,.14);box-shadow:none}}
"""
for i in range(6):
    s = round(i * 100 / 6, 2); e = round(s + 100 / 6, 2)
    kf4 += (f"@keyframes aT{i}{{0%,{s}%{{border-color:rgba(242,237,231,.14);box-shadow:none;transform:none}}"
            f"{s + 2}%,{e - 2}%{{border-color:#FF6A1A;box-shadow:0 0 44px rgba(255,106,26,.45);transform:translateY(-8px)}}"
            f"{e}%,100%{{border-color:rgba(242,237,231,.14);box-shadow:none;transform:none}}}}\n")
kf4 = kf4.replace('@keyframes aT0{0%,0%{border-color:rgba(242,237,231,.14);box-shadow:none;transform:none}2%,14.67%', '@keyframes aT0{0%,14.67%')
ICONS = {
    'ad': f'<div style="position: relative; width: 70px; height: 70px; border-radius: 16px; border: 3px solid #F2EDE7; display: flex; align-items: center; justify-content: center"><span style="{MONO}; font-weight: 600; font-size: 18px; color: #FF6A1A; letter-spacing: .06em">AD</span><div style="position: absolute; left: 6px; right: 6px; bottom: 6px; height: 5px; border-radius: 9px; background: rgba(242,237,231,.2); overflow: hidden"><div style="height: 100%; background: #FF6A1A; animation: aProg 2s linear infinite"></div></div></div>',
    'reel': '<div style="width: 44px; height: 74px; border-radius: 10px; border: 3px solid #F2EDE7; display: flex; align-items: center; justify-content: center"><svg width="24" height="24" viewBox="0 0 24 24" style="animation: aPlay 1.4s ease-in-out infinite"><path d="M8 5v14l11-7z" fill="#FF6A1A"/></svg></div>',
    'marca': '<svg width="72" height="72" viewBox="0 0 72 72" style="animation: aSpin 6s linear infinite"><circle cx="36" cy="36" r="30" fill="none" stroke="#F2EDE7" stroke-width="3"/><circle cx="36" cy="36" r="10" fill="#FF6A1A"/>' + ''.join(f'<circle cx="{36 + 20 * __import__("math").cos(k * 1.2566):.1f}" cy="{36 + 20 * __import__("math").sin(k * 1.2566):.1f}" r="5" fill="#F2EDE7"/>' for k in range(5)) + '</svg>',
    'entrevista': f'<div style="display: flex; align-items: flex-end; gap: 10px; height: 70px"><div style="width: 26px; height: 26px; border-radius: 99px; background: #F2EDE7; margin-bottom: 30px"></div><div style="display: flex; align-items: center; gap: 4px; height: 40px">{wave(5, "aTalk", 34, 5, 3)}</div><div style="width: 26px; height: 26px; border-radius: 99px; background: #F2EDE7; margin-bottom: 30px"></div></div>',
    'podcast': f'<div style="position: relative; width: 44px; height: 72px"><div style="position: absolute; left: 6px; top: 0; width: 32px; height: 46px; border-radius: 16px; background: linear-gradient(180deg, #F2EDE7, #9C938B)"></div><div style="position: absolute; left: 0; top: 24px; width: 44px; height: 30px; border: 3px solid #F2EDE7; border-top: none; border-radius: 0 0 22px 22px; box-sizing: border-box"></div><div style="position: absolute; left: 20px; top: 54px; width: 4px; height: 18px; background: #F2EDE7"></div><div style="position: absolute; left: -10px; top: 8px; width: 64px; height: 30px; border-radius: 50%; border: 3px solid #FF6A1A; opacity: .0; animation: aPing 1.6s ease-out infinite"></div></div>',
    'foto': '<div style="position: relative; width: 78px; height: 58px; border-radius: 12px; border: 3px solid #F2EDE7"><div style="position: absolute; left: 50%; top: 50%; width: 26px; height: 26px; margin: -13px; border-radius: 99px; border: 3px solid #FF6A1A"></div><div style="position: absolute; left: 10px; top: -10px; width: 20px; height: 8px; border-radius: 3px 3px 0 0; background: #F2EDE7"></div><div style="position: absolute; inset: -14px; border-radius: 18px; background: #FFFFFF; animation: aFlash 1.3s ease-out infinite"></div></div>',
}
tiles = (('ad', 'Anuncios'), ('reel', 'Reels'), ('marca', 'Vídeo de marca'), ('entrevista', 'Entrevistas'), ('podcast', 'Podcast'), ('foto', 'Fotos de marca'))
grid4 = ''.join(
    f'''<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; height: 186px; border-radius: 24px; background: #12100F; border: 3px solid rgba(242,237,231,.14); animation: aT{i} 4s {E} infinite">
<div style="height: 76px; display: flex; align-items: center; justify-content: center">{ICONS[k]}</div>
<span style="{BRIC}; font-weight: 800; font-size: 30px; letter-spacing: -0.02em">{t}</span></div>'''
    for i, (k, t) in enumerate(tiles))
steps4 = ''.join(
    f'<div style="position: absolute; left: {x}%; top: 50%; transform: translate(-50%,-50%); white-space: nowrap; padding: 12px 18px; border-radius: 16px; {BRIC}; font-weight: 800; font-size: 23px; letter-spacing: -0.01em; border: 2px solid #FF6A1A; animation: {a} 4s {E} infinite">{t}</div>'
    for x, t, a in ((17, '01 · Nos escribes', 'aSt1'), (50, '02 · Vienes y grabas', 'aSt2'), (83, '03 · Te llevas tu material', 'aSt3')))
body4 = headline('QUÉ PUEDES GRABAR', 'Lo que tu marca necesite,', 'en vídeo y en foto.', 80) + f"""
<div style="position: relative; display: flex; flex-direction: column; gap: 26px">
  <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px">{grid4}</div>
  <div style="position: relative; height: 150px; border-radius: 26px; background: #0A0908; border: 2px dashed rgba(242,237,231,.18)">
    <span style="position: absolute; left: 24px; top: 14px; {MONO}; font-size: 17px; letter-spacing: .12em; color: #9C938B">ASÍ DE FÁCIL</span>
    <div style="position: absolute; left: 17%; right: 17%; top: 57%; height: 4px; border-radius: 9px; background: rgba(242,237,231,.14)">
      <div style="height: 100%; border-radius: 9px; background: #FF6A1A; animation: aFill 4s {E} infinite"></div>
      <div style="position: absolute; top: 50%; width: 22px; height: 22px; margin: -11px 0 0 -11px; border-radius: 99px; background: #F2EDE7; box-shadow: 0 0 22px #FF6A1A; animation: aDot 4s {E} infinite"></div>
    </div>
    <div style="position: absolute; left: 0; right: 0; top: 57%; height: 0">{steps4}</div>
  </div>
</div>
"""
open(os.path.join(OUT, 'S4.dc.html'), 'w').write(page('04 · Qué grabas', 4, kf4, body4,
    'Empresas, marcas personales y creadores.', DESLIZA_TXT))

# ---------------------------------------------------------------- 05 CTA · DM "ESTUDIO"
kf5 = COMMON_KF + """
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
@keyframes aType{0%,8%{width:0ch}44%,100%{width:7ch}}
@keyframes aCaret{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes aInput{0%,50%{opacity:1}54%,100%{opacity:0}}
@keyframes aSent{0%,52%{opacity:0;transform:translateY(30px) scale(.9)}58%,96%{opacity:1;transform:none}100%{opacity:0}}
@keyframes aSeen{0%,70%{opacity:0}76%,96%{opacity:1}100%{opacity:0}}
@keyframes aTyping{0%,78%{opacity:0}82%,96%{opacity:1}100%{opacity:0}}
@keyframes aDots{0%,100%{transform:translateY(0);opacity:.4}50%{transform:translateY(-6px);opacity:1}}
@keyframes aSend{0%,48%{transform:scale(1)}51%{transform:scale(.8)}55%,100%{transform:scale(1)}}
@keyframes aPin{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
"""
dm5 = f'''<div style="position: relative; width: 600px; border-radius: 30px; background: #12100F; border: 2px solid rgba(242,237,231,.16); overflow: hidden; box-shadow: 0 50px 120px -40px rgba(255,106,26,.6)">
  <div style="display: flex; align-items: center; gap: 16px; padding: 18px 22px; border-bottom: 2px solid rgba(242,237,231,.08)">
    <img src="{LOGO}" style="width: 52px; height: 52px; border-radius: 99px; background: #0A0908">
    <span style="display: flex; flex-direction: column; gap: 2px"><span style="{BRIC}; font-weight: 800; font-size: 26px">ceos.productions</span><span style="font-size: 18px; color: #9C938B">Estudio de grabación · Burgos</span></span>
  </div>
  <div style="position: relative; height: 190px; padding: 22px">
    <div style="position: absolute; right: 22px; top: 24px; padding: 16px 26px; border-radius: 26px 26px 6px 26px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 34px; letter-spacing: .04em; animation: aSent 4s {E} infinite">ESTUDIO</div>
    <div style="position: absolute; right: 26px; top: 100px; {MONO}; font-size: 16px; letter-spacing: .08em; color: #9C938B; animation: aSeen 4s ease-out infinite">Visto</div>
    <div style="position: absolute; left: 22px; top: 120px; display: flex; gap: 8px; padding: 18px 22px; border-radius: 22px 22px 22px 6px; background: #1E1A17; animation: aTyping 4s ease-out infinite">{''.join(f'<span style="width: 12px; height: 12px; border-radius: 99px; background: #F2EDE7; animation: aDots .9s ease-in-out {k * .15:.2f}s infinite"></span>' for k in range(3))}</div>
  </div>
  <div style="display: flex; align-items: center; gap: 14px; margin: 0 18px 18px; padding: 12px 12px 12px 24px; border-radius: 99px; border: 2px solid rgba(242,237,231,.16)">
    <span style="flex: 1; position: relative; height: 40px; text-align: left; animation: aInput 4s steps(1) infinite">
      <span style="display: inline-block; vertical-align: top; overflow: hidden; white-space: nowrap; {MONO}; font-weight: 600; font-size: 30px; line-height: 40px; color: #F2EDE7; animation: aType 4s steps(7) infinite">ESTUDIO</span><span style="display: inline-block; vertical-align: top; width: 3px; height: 34px; margin-top: 3px; background: #FF6A1A; animation: aCaret .8s steps(1) infinite"></span>
    </span>
    <span style="flex: none; width: 52px; height: 52px; border-radius: 99px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; animation: aSend 4s ease-out infinite"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
  </div>
</div>'''
body5 = f"""
<div style="position: relative; display: flex; flex-direction: column; align-items: center; text-align: center">
<p style="margin: 0; {BRIC}; font-weight: 800; font-size: 88px; line-height: .98; letter-spacing: -0.05em">Tu próximo vídeo,<br><span style="{SERIF}; color: #FF6A1A; animation: aHeat 4s ease-in-out infinite">grabado en estudio.</span></p>
<div style="position: relative; margin-top: 40px">{dm5}
  <div style="position: absolute; right: -96px; top: -30px; display: flex; align-items: center; gap: 10px; padding: 12px 20px; border-radius: 99px; background: #F2EDE7; color: #0A0908; {MONO}; font-weight: 600; font-size: 20px; letter-spacing: .1em; transform: rotate(6deg); box-shadow: 0 20px 50px -10px rgba(0,0,0,.6)">
    <svg width="22" height="22" viewBox="0 0 24 24" style="animation: aPin 1.6s ease-in-out infinite"><path d="M12 2C8 2 5 5 5 9c0 5 7 13 7 13s7-8 7-13c0-4-3-7-7-7z" fill="#FF6A1A"/><circle cx="12" cy="9" r="2.6" fill="#0A0908"/></svg>BURGOS</div>
</div>
<div style="position: relative; overflow: hidden; margin-top: 40px; padding: 26px 48px; border-radius: 30px; background: #FF6A1A; color: #0A0908; {BRIC}; font-weight: 800; font-size: 56px; line-height: 1.02; letter-spacing: -0.04em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 4s ease-in-out infinite">Escríbenos ESTUDIO por DM<br><span style="font-size: 38px; letter-spacing: -0.02em">y reserva tu sesión en Burgos</span><div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.3), rgba(255,255,255,0)); animation: aShim 4s ease-in-out 0.6s infinite"></div></div>
</div>
"""
open(os.path.join(OUT, 'S5.dc.html'), 'w').write(page('05 · CTA', 5, kf5, body5,
    'Estudio de grabación y fotografía en Burgos.',
    f"""<span style="{MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.PRODUCTIONS</span>"""))
print('ok')
