#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel 2026-09-29 (valor: qué medir cada semana en tus campañas)."""
import os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SRC = os.path.join(HERE, 'src')
os.makedirs(SRC, exist_ok=True)
for f in os.listdir(os.path.join(ROOT, 'toolkit/plantilla-valor')):
    shutil.copy(os.path.join(ROOT, 'toolkit/plantilla-valor', f), SRC)

base = open(os.path.join(ROOT, 'posts/2026-09-27/src/Main.dc.html')).read()
HEAD = base.split('</style>\n</helmet>')[0]
BG = re.search(r'(<div aria-hidden="true".*?</div></div>)\n<div style="position: relative; display: flex; align-items: center; justify-content: space-between">', base, re.S).group(1)
LOGO = re.search(r'/_blob/[0-9a-f]{32}', base).group(0)
TAIL = '''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1080,"height":1350}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
'''

EXTRA = '''
@keyframes ring{0%{transform:scale(1);opacity:.8}100%{transform:scale(1.9);opacity:0}}
@keyframes rowIn{from{opacity:0;transform:translateX(-30px)}to{opacity:1;transform:none}}
@keyframes drop{0%{opacity:0;transform:translateY(-60px) scale(.9)}60%{opacity:1;transform:translateY(6px) scale(1.02)}100%{opacity:1;transform:none}}
@keyframes fadeOut{to{opacity:0}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes shake{0%,100%{transform:rotate(0)}20%{transform:rotate(-14deg)}40%{transform:rotate(12deg)}60%{transform:rotate(-8deg)}80%{transform:rotate(6deg)}}
@keyframes rowOn{from{border-color:rgba(242,237,231,0.1);background:rgba(242,237,231,0.03)}to{border-color:rgba(255,106,26,0.75);background:rgba(255,106,26,0.1)}}
@keyframes icoOn{from{background:rgba(242,237,231,0.08)}to{background:#FF6A1A;box-shadow:0 0 26px rgba(255,106,26,.8)}}
@keyframes cool{0%{width:100%;background:linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A)}100%{width:14%;background:linear-gradient(90deg,#4A4540,#6B635C,#9C938B)}}
@keyframes dayOff{from{background:#FF6A1A;box-shadow:0 0 14px rgba(255,106,26,.5)}to{background:rgba(242,237,231,0.1);box-shadow:none}}
@keyframes greyOut{to{filter:grayscale(1);opacity:.45}}
@keyframes stamp{0%{opacity:0;transform:rotate(-12deg) scale(2.2)}60%{opacity:1;transform:rotate(-12deg) scale(.92)}100%{opacity:1;transform:rotate(-12deg) scale(1)}}
@property --d{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes dcnt{from{--d:0}to{--d:7}}
.dc{counter-reset:d var(--d);animation:dcnt 2.4s steps(7,end) .5s both}
.dc::after{content:counter(d)}
@keyframes travel{from{top:47px}to{top:455px}}
@keyframes type{from{width:0}to{width:100%}}
@keyframes caret{0%,100%{opacity:1}50%{opacity:0}}
@keyframes bounce{0%,100%{transform:translateY(0);opacity:.4}50%{transform:translateY(-8px);opacity:1}}
@keyframes tick{from{color:#6B635C}to{color:#FF6A1A}}
@keyframes check{0%{background:transparent;border-color:rgba(242,237,231,0.25);transform:scale(.8)}60%{transform:scale(1.2)}100%{background:#FF6A1A;border-color:#FF6A1A;transform:scale(1)}}
@keyframes draw{from{stroke-dashoffset:30}to{stroke-dashoffset:0}}
@keyframes txtOn{from{color:#9C938B}to{color:#F2EDE7}}
@keyframes aBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035)}}
@keyframes aShim{0%{transform:translateX(-120%)}60%,100%{transform:translateX(620%)}}
@keyframes wob{0%,100%{transform:rotate(-2deg)}50%{transform:rotate(-1deg) translateY(-6px)}}
'''

CARD = "background: linear-gradient(160deg, rgba(34,30,27,0.96), rgba(18,16,15,0.96)); border: 1px solid rgba(242,237,231,0.12); box-shadow: 0 50px 120px -40px rgba(0,0,0,0.9), inset 0 1px 0 rgba(242,237,231,0.06); border-radius: 34px"
MONO = "font-family: 'JetBrains Mono', monospace"
BRIC = "font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800"
EJ = f'<span style="{MONO}; font-size: 16px; letter-spacing: 0.14em; color: #FFB27A; padding: 6px 12px; border-radius: 99px; border: 1px solid rgba(255,106,26,0.45)">EJEMPLO</span>'
TILT = "animation: fxTilt 1.1s cubic-bezier(.2,.8,.2,1) .35s both, fxFloat 4s ease-in-out 1.45s infinite"

ICON = {
    'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    'chat': '<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/>',
    'mic': '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v3"/>',
    'x': '<path d="M6 6l12 12M18 6L6 18"/>',
    'ok': '<path d="M5 12l5 5L20 7"/>',
    'cal': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    'flame': '<path d="M12 2c1 4 5 6 5 11a5 5 0 0 1-10 0c0-2 1-3.5 2-4.5 0 2 1 3 2 3 0-3-1-6 1-9.5z"/>',
}


def ic(name, size=28, color='#F2EDE7', sw=2.4, extra=''):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="{extra}">{ICON[name]}</svg>'


def words(txt, t0, step=0.07):
    out, t = [], t0
    for w in txt.split(' '):
        out.append(f'<span class="fx-w" style="animation-delay: {t:.2f}s">{w}</span>')
        t += step
    return ' '.join(out), t


def headline(l1, accent, size=104, t0=0.15):
    a, t = words(l1, t0)
    b, _ = words(accent, t)
    return (f'<h2 style="margin: 0; {BRIC}; font-size: {size}px; line-height: 0.95; letter-spacing: -0.05em">{a}<br>'
            f'<span style="font-family: \'Instrument Serif\', serif; font-style: italic; font-weight: 400; letter-spacing: -0.015em; color: #FF6A1A">{b}</span></h2>')


def sub(txt):
    return f'<p style="margin: -18px 0 0; font-size: 34px; line-height: 1.25; color: #B5ADA4; max-width: 880px; animation: aIn .9s cubic-bezier(.2,.8,.2,1) .5s both">{txt}</p>'


def header(n):
    return f'''<div style="position: relative; display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; align-items: center; gap: 16px">
<img src="{LOGO}" alt="Ceos Growth" style="width: 56px; height: 56px; display: block; animation: aLogo 4s ease-in-out infinite">
<span style="{BRIC}; font-size: 30px; letter-spacing: -0.02em">Ceos Growth</span>
</div>
<span style="{MONO}; font-size: 20px; letter-spacing: 0.12em; color: #9C938B">0{n} / 05</span>
</div>'''


def footer(n):
    bars = ''.join(f'<div style="height: 6px; border-radius: 99px; background: {"#FF6A1A" if i < n else "rgba(242,237,231,0.12)"}"></div>' for i in range(5))
    if n < 5:
        tail = f'<span style="align-self: flex-end; display: inline-flex; align-items: center; gap: 10px; background: #FF6A1A; color: #0A0908; font-weight: 700; font-size: 24px; padding: 14px 26px; border-radius: 999px">Desliza<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="2.8" aria-hidden="true" style="animation: aNudge 2s ease-in-out infinite"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></span>'
    else:
        tail = f'<span style="align-self: center; {MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.GROWTH · GUÁRDALO PARA TU REVISIÓN DEL LUNES</span>'
    return f'''<div style="position: relative; display: flex; flex-direction: column; gap: 26px">
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px">{bars}</div>
{tail}
</div>'''


def page(n, middle, title):
    return (HEAD.replace('<title>01</title>', f'<title>{title}</title>') + EXTRA + '</style>\n</helmet>\n'
            + '<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px; position: relative; overflow: hidden; background: #0A0908; color: #F2EDE7; font-family: \'Instrument Sans\', sans-serif; display: flex; flex-direction: column; justify-content: space-between">\n'
            + BG + '\n' + header(n) + '\n'
            + '<div style="position: relative; display: flex; flex-direction: column; gap: 46px">\n' + middle + '\n</div>\n'
            + footer(n) + '\n</div>\n' + TAIL)




EXTRA += '''
@keyframes barGrow{from{transform:scaleY(.06)}to{transform:scaleY(1)}}
@keyframes heartUp{0%{transform:translate(0,0) scale(.5);opacity:0}15%{opacity:1}100%{transform:translate(var(--dx),-260px) scale(1.15);opacity:0}}
@keyframes spark{from{stroke-dashoffset:900}to{stroke-dashoffset:0}}
@keyframes strike{from{width:0}to{width:108%}}
@keyframes chipOn{0%{border-color:rgba(242,237,231,0.1);background:rgba(242,237,231,0.03);transform:scale(1)}50%{transform:scale(1.06)}100%{border-color:rgba(255,106,26,0.8);background:rgba(255,106,26,0.14);transform:scale(1);box-shadow:0 0 36px -8px rgba(255,106,26,.8)}}
@keyframes pulseDot{0%,100%{transform:scale(1);box-shadow:0 0 0 0 rgba(255,106,26,.7)}50%{transform:scale(1.25);box-shadow:0 0 0 14px rgba(255,106,26,0)}}
@property --lk{syntax:'<integer>';inherits:false;initial-value:180}
@keyframes lkc{from{--lk:180}to{--lk:2480}}
.lk{counter-reset:lk var(--lk);animation:lkc 1.9s cubic-bezier(.3,.7,.4,1) 0s both}
.lk::after{content:counter(lk)}
@keyframes notif{0%{opacity:0;transform:translateY(-40px) scale(.94)}12%{opacity:1;transform:none}80%{opacity:1;transform:none}100%{opacity:0;transform:translateY(10px)}}
@keyframes qPulse{0%,100%{transform:scale(1);box-shadow:0 0 0 0 rgba(255,106,26,.6)}50%{transform:scale(1.12);box-shadow:0 0 0 18px rgba(255,106,26,0)}}
@keyframes lens{0%{transform:translate(0,0)}25%{transform:translate(260px,30px)}50%{transform:translate(200px,190px)}75%{transform:translate(30px,160px)}100%{transform:translate(0,0)}}
@keyframes flow{0%{top:34px;opacity:0}8%{opacity:1}92%{opacity:1}100%{top:526px;opacity:0}}
@keyframes leak{0%{top:34px;left:0;opacity:0}8%{opacity:1}45%{top:190px;left:0;opacity:1}75%{top:230px;left:-70px;opacity:0}100%{top:230px;left:-70px;opacity:0}}
@keyframes nodeOn{0%{background:#FF6A1A;box-shadow:0 0 0 10px rgba(255,106,26,.25),0 0 40px rgba(255,106,26,.9);transform:scale(1.18)}40%,100%{background:#2A2420;box-shadow:0 0 0 0 rgba(255,106,26,0);transform:scale(1)}}
@keyframes rowGlow{0%{border-color:rgba(255,106,26,0.75);background:rgba(255,106,26,0.12)}45%,100%{border-color:rgba(242,237,231,0.08);background:rgba(242,237,231,0.025)}}
@keyframes euro{0%,70%{opacity:0;transform:scale(.4) translateY(10px)}80%{opacity:1;transform:scale(1.15)}100%{opacity:0;transform:scale(1) translateY(-30px)}}
@keyframes fillW{from{width:0}}
@keyframes toggleOff{from{left:34px;background:#FF6A1A}to{left:4px;background:#6B635C}}
@keyframes trackOff{from{background:rgba(255,106,26,0.35)}to{background:rgba(242,237,231,0.12)}}
@keyframes upBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes cardWin{0%,100%{box-shadow:0 0 0 2px rgba(255,106,26,.6),0 30px 90px -20px rgba(255,106,26,.55)}50%{box-shadow:0 0 0 2px rgba(255,106,26,1),0 30px 110px -10px rgba(255,106,26,.9)}}
@keyframes cursorGo{0%{transform:translate(240px,170px)}100%{transform:translate(0,0)}}
@keyframes press{0%,100%{transform:scale(1)}50%{transform:scale(.9)}}
@keyframes ripple{0%{opacity:.9;transform:scale(.3)}100%{opacity:0;transform:scale(2.6)}}
@keyframes swapOut{to{opacity:0;transform:translateY(-16px)}}
@keyframes swapIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes btnDone{to{background:rgba(242,237,231,0.1);color:#F2EDE7;box-shadow:inset 0 0 0 2px rgba(242,237,231,0.25)}}
'''

ICON.update({
    'heart': '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/>',
    'euro': '<path d="M18 6.5A7 7 0 1 0 18 17.5"/><path d="M4 10h9M4 14h9"/>',
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    'megaphone': '<path d="M3 11v2a1 1 0 0 0 1 1h3l6 5V5L7 10H4a1 1 0 0 0-1 1z"/><path d="M17 8a5 5 0 0 1 0 8"/>',
    'up': '<path d="M7 17L17 7M9 7h8v8"/>',
    'pause': '<path d="M9 5v14M15 5v14"/>',
    'search': '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    'bell': '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>',
    'play': '<path d="M7 4l13 8-13 8z"/>',
})

LBL = f"{MONO}; font-size: 18px; letter-spacing: 0.14em; color: #9C938B"


def hearts(n, area_w, dur=1.8, size=30):
    out = []
    for i in range(n):
        left = 20 + (i * 67) % (area_w - 60)
        dx = [-40, 30, -20, 50, -60, 20, 40, -30][i % 8]
        delay = -(i * dur / n)
        out.append(f'<span style="position: absolute; left: {left}px; bottom: 10px; --dx: {dx}px; animation: heartUp {dur}s ease-out {delay:.2f}s infinite">{ic("heart", size, "#FF6A1A", 2.2, "fill: rgba(255,106,26,0.85)")}</span>')
    return ''.join(out)


# ---------- 01 GANCHO: panel de Meta Ads — los likes suben, pero no son la métrica ----------
def h_static(l1, accent, size):
    # Titular visible desde el primer fotograma (portada de Instagram), con brillo que lo recorre
    return (f'<h2 style="position: relative; margin: 0; {BRIC}; font-size: {size}px; line-height: 0.95; letter-spacing: -0.05em">{l1}<br>'
            f'<span style="font-family: \'Instrument Serif\', serif; font-style: italic; font-weight: 400; letter-spacing: -0.015em; color: #FF6A1A; text-shadow: 0 0 40px rgba(255,106,26,.45)">{accent}</span></h2>')


bars = [34, 48, 42, 60, 72, 66, 88]
barhtml = ''.join(
    f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 10px"><div style="width: 100%; height: 210px; display: flex; align-items: flex-end"><div style="width: 100%; height: {h}%; border-radius: 10px 10px 4px 4px; background: linear-gradient(180deg, #FFB27A, #FF6A1A 45%, #C84A0C); transform-origin: bottom; box-shadow: 0 0 22px -4px rgba(255,106,26,.7); animation: barGrow .9s cubic-bezier(.2,.8,.2,1) {0.3 + i * 0.12:.2f}s both"></div></div><span style="{MONO}; font-size: 15px; color: #6B635C">{d}</span></div>'
    for i, (h, d) in enumerate(zip(bars, 'LMXJVSD')))
pts = ' '.join(f'{20 + i * 57},{150 - h * 1.5:.0f}' for i, h in enumerate(bars))

chips = ''
for i, (icn, t) in enumerate([('euro', 'Coste por lead'), ('cal', 'Citas'), ('ok', 'Ventas')]):
    d = 2.1 + i * 0.4
    chips += (f'<div style="display: flex; align-items: center; gap: 12px; padding: 16px 16px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); animation: chipOn .6s cubic-bezier(.2,.8,.2,1) {d:.2f}s both">'
              f'<span style="flex: none; width: 44px; height: 44px; border-radius: 12px; background: rgba(242,237,231,0.08); display: flex; align-items: center; justify-content: center; animation: icoOn .5s ease-out {d:.2f}s both">{ic(icn, 24, "#F2EDE7", 2.4)}</span>'
              f'<span style="font-size: 25px; font-weight: 700; white-space: nowrap">{t}</span></div>')

S1 = f'''{h_static("¿Tus anuncios funcionan?", "Los likes no te lo dicen.", 104)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; flex-direction: column; gap: 22px; animation: fxFloat 4s ease-in-out infinite">
<div style="position: absolute; inset: 0; border-radius: 34px; overflow: hidden; pointer-events: none"><div style="position: absolute; top: -10%; bottom: -10%; left: 0; width: 22%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,210,170,0.07), rgba(255,255,255,0)); animation: shim 2.6s ease-in-out infinite"></div></div>
<div style="display: flex; align-items: center; justify-content: space-between"><span style="{LBL}">META ADS · ESTA SEMANA</span>{EJ}</div>
<div style="display: flex; gap: 22px">
<div style="position: relative; width: 380px; height: 330px; flex: none">
<div style="position: absolute; inset: 0; box-sizing: border-box; padding: 24px; border-radius: 24px; background: rgba(255,106,26,0.07); border: 1px solid rgba(255,106,26,0.3); overflow: hidden; display: flex; flex-direction: column; gap: 6px; animation: greyOut .6s ease-out 1.9s both">
<div style="display: flex; align-items: center; gap: 10px">{ic("heart", 26, "#FF6A1A", 2.2, "fill: rgba(255,106,26,0.9)")}<span style="{LBL}; color: #B5ADA4">ME GUSTA</span></div>
<div style="position: relative; align-self: flex-start"><span class="lk" style="{BRIC}; font-size: 124px; letter-spacing: -0.05em; line-height: 1"></span><span style="position: absolute; left: -4%; top: 52%; height: 8px; border-radius: 99px; background: #F2EDE7; animation: strike .45s cubic-bezier(.2,.8,.2,1) 2.0s both"></span></div>
<span style="font-size: 22px; color: #B5ADA4">y subiendo…</span>
{hearts(8, 380)}
</div>
<div style="position: absolute; left: 50%; top: 50%; margin: -40px 0 0 -150px; width: 300px; box-sizing: border-box; padding: 16px 0; text-align: center; border-radius: 16px; border: 4px solid #FF6A1A; color: #FF6A1A; background: rgba(10,9,8,0.82); {BRIC}; font-size: 34px; letter-spacing: -0.02em; box-shadow: 0 0 40px rgba(255,106,26,.5); animation: stamp .55s cubic-bezier(.2,.8,.2,1) 2.1s both">NO PAGA FACTURAS</div>
</div>
<div style="position: relative; flex: 1; box-sizing: border-box; padding: 22px 22px 16px; border-radius: 24px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); display: flex; flex-direction: column; gap: 10px; animation: rowOn .6s ease-out 2.1s both">
<span style="{LBL}">LO QUE SÍ CUENTA</span>
<div style="position: relative; display: flex; gap: 12px">{barhtml}
<svg width="100%" height="210" viewBox="0 0 382 170" preserveAspectRatio="none" style="position: absolute; left: 0; top: 0; overflow: visible" aria-hidden="true"><polyline points="{pts}" fill="none" stroke="#F2EDE7" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" style="stroke-dasharray: 900; animation: spark 2.4s ease-in-out .4s both; filter: drop-shadow(0 0 8px rgba(242,237,231,.6))"/></svg>
<span style="position: absolute; right: 8px; top: 8px; width: 18px; height: 18px; border-radius: 99px; background: #F2EDE7; animation: pulseDot 1.2s ease-in-out infinite, fadeIn .3s ease-out 2.7s both"></span>
</div>
</div>
</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">{chips}</div>
</div>'''


# ---------- 02 PROBLEMA: móvil lleno de likes vs CRM sin saber de dónde viene la venta ----------
notifs = ''
for i, (who, txt) in enumerate([('L', 'A Laura le gusta tu anuncio'), ('J', 'A Jorge le gusta tu anuncio'), ('M', 'A Marta le gusta tu anuncio')]):
    notifs += (f'<div style="position: absolute; left: 12px; right: 12px; top: {92 + i * 78}px; display: flex; align-items: center; gap: 10px; padding: 12px 12px; border-radius: 16px; background: rgba(242,237,231,0.95); color: #0A0908; box-shadow: 0 16px 30px -10px rgba(0,0,0,.8); animation: drop .7s cubic-bezier(.2,.8,.2,1) {0.6 + i * 0.6:.2f}s both">'
               f'<span style="flex: none; width: 34px; height: 34px; border-radius: 99px; background: linear-gradient(160deg, #FF8F45, #C84A0C); display: flex; align-items: center; justify-content: center; {BRIC}; font-size: 18px; color: #0A0908">{who}</span>'
               f'<span style="font-size: 17px; font-weight: 600; line-height: 1.2">{txt}</span></div>')

sales = ''
for i, name in enumerate(['Venta · Carlos R.', 'Venta · Ana P.', 'Venta · Luis M.']):
    d = 0.7 + i * 0.4
    sales += (f'<div style="display: flex; align-items: center; gap: 14px; padding: 16px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); animation: rowIn .6s cubic-bezier(.2,.8,.2,1) {d:.2f}s both">'
              f'<span style="flex: none; width: 46px; height: 46px; border-radius: 12px; background: rgba(242,237,231,0.08); display: flex; align-items: center; justify-content: center">{ic("euro", 24)}</span>'
              f'<div style="flex: 1; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 24px; font-weight: 600">{name}</span><span style="{MONO}; font-size: 15px; letter-spacing: 0.08em; color: #9C938B">ORIGEN: <span style="color: #FFB27A; animation: aBlink 1.2s ease-in-out {i * 0.3:.1f}s infinite">SIN MEDIR</span></span></div>'
              f'<span style="flex: none; width: 44px; height: 44px; border-radius: 99px; border: 2px solid #FF6A1A; color: #FF6A1A; display: flex; align-items: center; justify-content: center; {BRIC}; font-size: 26px; animation: qPulse 1.4s ease-in-out {i * 0.35:.2f}s infinite">?</span></div>')

S2 = f'''{headline("Mides lo que se ve.", "No lo que vende.", 104)}
{sub("Los likes no te dicen de qué anuncio sale el dinero.")}
<div style="display: flex; gap: 26px; align-items: center; {TILT}">
<div style="position: relative; flex: none; width: 310px; height: 590px; border-radius: 44px; background: #0A0908; border: 3px solid rgba(242,237,231,0.16); box-shadow: inset 0 0 0 8px #12100F, 0 40px 100px -30px rgba(0,0,0,.9); overflow: hidden; box-sizing: border-box; padding: 60px 18px 18px">
<div style="position: absolute; top: 14px; left: 50%; margin-left: -45px; width: 90px; height: 24px; border-radius: 99px; background: #1E1A17"></div>
<div style="display: flex; align-items: center; gap: 10px"><span style="width: 34px; height: 34px; border-radius: 99px; background: linear-gradient(160deg, #FF8F45, #C84A0C)"></span><span style="font-size: 18px; font-weight: 700">tu_negocio</span><span style="{MONO}; font-size: 12px; color: #9C938B">PUBLICIDAD</span></div>
<div style="position: relative; margin-top: 14px; height: 340px; border-radius: 18px; background: radial-gradient(circle at 30% 30%, #3A2518, #171412 70%); overflow: hidden; display: flex; align-items: center; justify-content: center">
<span style="width: 74px; height: 74px; border-radius: 99px; background: rgba(242,237,231,0.14); display: flex; align-items: center; justify-content: center; animation: aBreathe 1.6s ease-in-out infinite">{ic("play", 32, "#F2EDE7", 2, "fill: #F2EDE7")}</span>
{hearts(7, 264, 1.6, 34)}
</div>
<div style="margin-top: 16px; display: flex; align-items: center; gap: 12px">{ic("heart", 34, "#FF6A1A", 2.2, "fill: #FF6A1A; animation: aBreathe .8s ease-in-out infinite")}<span style="font-size: 20px; font-weight: 700">Muchos me gusta</span></div>
{notifs}
</div>
<div style="flex: 1; box-sizing: border-box; padding: 26px; {CARD}; display: flex; flex-direction: column; gap: 14px; position: relative; overflow: hidden">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="{LBL}">CRM · VENTAS</span>{EJ}</div>
{sales}
<div style="margin-top: 6px; display: flex; align-items: center; gap: 12px; padding: 16px 18px; border-radius: 18px; border: 1px dashed rgba(255,106,26,0.6); animation: fadeIn .6s ease-out 2.2s both">{ic("search", 28, "#FF6A1A", 2.6, "animation: aNudge 1s ease-in-out infinite")}<span style="font-family: 'Instrument Serif', serif; font-style: italic; font-size: 30px; line-height: 1.1">¿Qué anuncio las trajo?</span></div>
</div>
</div>'''


# ---------- 03 IDEA: el camino completo con un punto que viaja por las 4 fases ----------
STEP = 132
stages = [('megaphone', 'Anuncio', '¿Cuánto te cuesta cada lead?'),
          ('user', 'Lead', '¿Contesta cuando le llamas?'),
          ('cal', 'Cita', '¿Se presenta?'),
          ('euro', 'Venta', '¿De qué anuncio viene?')]
rows = ''
for i, (icn, name, q) in enumerate(stages):
    delay = (((i * STEP + 52) - 43) / 246.0) % 1.0
    rows += (f'<div style="position: relative; height: {STEP - 14}px; margin-bottom: 14px; display: flex; align-items: center; gap: 22px; padding: 0 24px 0 96px; border-radius: 22px; border: 1px solid rgba(242,237,231,0.08); background: rgba(242,237,231,0.025); animation: rowGlow 1s ease-out {delay:.2f}s infinite, rowIn .6s cubic-bezier(.2,.8,.2,1) {0.3 + i * 0.15:.2f}s backwards">'
             f'<span style="position: absolute; left: 22px; top: 50%; margin-top: -26px; width: 52px; height: 52px; border-radius: 99px; background: #2A2420; display: flex; align-items: center; justify-content: center; animation: nodeOn 1s ease-out {delay:.2f}s infinite">{ic(icn, 26, "#F2EDE7", 2.4)}</span>'
             f'<span style="width: 170px; flex: none; {BRIC}; font-size: 40px; letter-spacing: -0.03em">{name}</span>'
             f'<span style="font-family: \'Instrument Serif\', serif; font-style: italic; font-size: 34px; line-height: 1.05; color: #D9D1C8">{q}</span></div>')

S3 = f'''{headline("Mídelo todo:", "del anuncio a la venta.", 104)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 28px 28px 14px; {CARD}; {TILT}">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px"><span style="{LBL}">TU EMBUDO · 4 PREGUNTAS</span><span style="display: inline-flex; align-items: center; gap: 8px; {MONO}; font-size: 16px; letter-spacing: 0.12em; color: #FFB27A"><span style="width: 10px; height: 10px; border-radius: 99px; background: #FF6A1A; animation: aBlink 1s ease-in-out infinite"></span>EN DIRECTO</span></div>
<div style="position: relative">
<div style="position: absolute; left: 48px; top: 34px; width: 3px; height: {STEP * 3}px; margin-left: -1px; background: linear-gradient(180deg, rgba(255,106,26,.7), rgba(255,106,26,.15))"></div>
{rows}
<span style="position: absolute; z-index: 2; left: 40px; width: 18px; height: 18px; border-radius: 99px; background: #FFE2CC; box-shadow: 0 0 20px 6px rgba(255,106,26,.95), 0 -30px 24px -6px rgba(255,106,26,.5); animation: flow 2s linear 0s infinite"></span>
<span style="position: absolute; z-index: 2; left: 40px; width: 18px; height: 18px; border-radius: 99px; background: #FFE2CC; box-shadow: 0 0 20px 6px rgba(255,106,26,.95), 0 -30px 24px -6px rgba(255,106,26,.5); animation: flow 2s linear -1s infinite"></span>
<span style="position: absolute; z-index: 1; left: 44px; width: 12px; height: 12px; border-radius: 99px; background: #9C938B; animation: leak 2s ease-in -0.5s infinite"></span>
<span style="position: absolute; z-index: 3; right: 30px; top: {STEP * 3 + 18}px; display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; border-radius: 99px; background: #FF6A1A; color: #0A0908; font-weight: 700; font-size: 22px; box-shadow: 0 0 40px rgba(255,106,26,.8); animation: euro 1s ease-out .87s infinite">{ic("ok", 20, "#0A0908", 3)}Venta</span>
</div>
</div>
{sub("Si solo miras el anuncio, no sabes dónde se pierden.")}'''


# ---------- 04 SOLUCIÓN: comparar dos anuncios → pausar uno y escalar otro ----------
def metric(name, pct, d, hot=True):
    col = 'linear-gradient(90deg, #C84A0C, #FF6A1A, #FFB27A)' if hot else 'linear-gradient(90deg, #6B635C, #9C938B)'
    return (f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="display: flex; justify-content: space-between"><span style="font-size: 22px; font-weight: 600; color: #D9D1C8">{name}</span></div>'
            f'<div style="height: 14px; border-radius: 99px; background: rgba(242,237,231,0.08); overflow: hidden"><div style="height: 100%; width: {pct}%; border-radius: 99px; background: {col}; animation: fillW 1s cubic-bezier(.2,.8,.2,1) {d:.2f}s both"></div></div></div>')


def adcard(letter, vals, win):
    d0 = 0.5
    ms = ''.join(metric(n, v, d0 + i * 0.3, win or i == 0) for i, (n, v) in enumerate(zip(['Leads', 'Citas', 'Ventas'], vals)))
    anim = 'animation: cardWin 1.6s ease-in-out 2.4s infinite' if win else 'animation: greyOut .6s ease-out 2.4s both'
    toggle = (f'<span style="position: relative; width: 66px; height: 36px; border-radius: 99px; background: rgba(255,106,26,0.35); {"" if win else "animation: trackOff .4s ease-out 2.3s both"}">'
              f'<span style="position: absolute; top: 4px; left: 34px; width: 28px; height: 28px; border-radius: 99px; background: #FF6A1A; {"" if win else "animation: toggleOff .4s ease-out 2.3s both"}"></span></span>')
    return (f'<div style="position: relative; flex: 1; box-sizing: border-box; padding: 22px; border-radius: 26px; background: rgba(242,237,231,0.03); border: 1px solid rgba(242,237,231,0.1); display: flex; flex-direction: column; gap: 18px; {anim}">'
            f'<div style="display: flex; align-items: center; justify-content: space-between"><span style="{BRIC}; font-size: 32px; letter-spacing: -0.02em">Anuncio {letter}</span>{toggle}</div>'
            f'<div style="height: 170px; border-radius: 18px; background: radial-gradient(circle at {"30% 30%, #4A2A14" if win else "70% 40%, #2E2A26"}, #171412 70%); display: flex; align-items: center; justify-content: center"><span style="width: 58px; height: 58px; border-radius: 99px; background: rgba(242,237,231,0.14); display: flex; align-items: center; justify-content: center">{ic("play", 26, "#F2EDE7", 2, "fill: #F2EDE7")}</span></div>'
            f'{ms}</div>')


S4 = f'''{headline("Cada lunes, decide:", "qué pausar y qué escalar.", 100)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 28px; {CARD}; display: flex; flex-direction: column; gap: 20px; {TILT}">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="{LBL}">COMPARATIVA · META ADS</span>{EJ}</div>
<div style="position: relative; display: flex; gap: 22px">
{adcard("A", [55, 62, 58], True)}
{adcard("B", [88, 22, 6], False)}
<div style="position: absolute; right: 40px; top: 118px; padding: 12px 22px; border-radius: 14px; border: 4px solid #9C938B; color: #F2EDE7; background: rgba(10,9,8,0.85); {BRIC}; font-size: 34px; display: flex; align-items: center; gap: 10px; animation: stamp .55s cubic-bezier(.2,.8,.2,1) 2.5s both">{ic("pause", 28, "#F2EDE7", 3)}PAUSAR</div>
<div style="position: absolute; left: 40px; top: 118px; padding: 12px 22px; border-radius: 14px; background: #FF6A1A; color: #0A0908; {BRIC}; font-size: 34px; display: flex; align-items: center; gap: 10px; box-shadow: 0 0 50px rgba(255,106,26,.8); animation: pop .6s cubic-bezier(.2,.8,.2,1) 2.8s both">ESCALAR<span style="display: inline-flex; animation: upBob .8s ease-in-out infinite">{ic("up", 30, "#0A0908", 3.2)}</span></div>
</div>
</div>
{sub("El que trae más leads no siempre es el que más vende.")}'''


# ---------- 05 CTA: perfil de @ceos.growth, cursor que pulsa Seguir ----------
S5 = f'''<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0 0 100px; {BRIC}; font-size: 84px; line-height: 1; letter-spacing: -0.045em; animation: aIn .8s cubic-bezier(.2,.8,.2,1) .1s both">¿Te ha servido?</p>
<div style="position: relative; width: 900px; box-sizing: border-box; padding: 40px 36px; {CARD}; display: flex; align-items: center; gap: 26px; text-align: left; {TILT}">
<div style="position: relative; flex: none; width: 120px; height: 120px; border-radius: 99px; padding: 4px; background: conic-gradient(from 0deg, #FF6A1A, #FFB27A, #C84A0C, #FF6A1A); animation: aGlow 2s ease-in-out infinite"><div style="width: 100%; height: 100%; border-radius: 99px; background: #0A0908; display: flex; align-items: center; justify-content: center"><img src="{LOGO}" alt="" style="width: 70px; height: 70px"></div></div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 6px"><span style="{BRIC}; font-size: 40px; letter-spacing: -0.03em">@ceos.growth</span><span style="font-size: 23px; color: #B5ADA4; line-height: 1.25">Captación y ventas para negocios.<br>Tips cada semana.</span></div>
<div style="position: relative; flex: none">
<div style="position: relative; width: 190px; height: 68px; border-radius: 18px; background: #FF6A1A; color: #0A0908; font-weight: 700; font-size: 27px; overflow: hidden; animation: press .25s ease-in-out 1.85s both, btnDone .3s ease-out 2.05s both">
<span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; animation: swapOut .25s ease-in 2.0s both">Seguir</span>
<span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; gap: 8px; animation: swapIn .3s ease-out 2.1s both">Siguiendo{ic("ok", 22, "#FF6A1A", 3.2)}</span>
</div>
<span style="position: absolute; left: 50%; top: 50%; width: 120px; height: 120px; margin: -60px 0 0 -60px; border-radius: 99px; border: 3px solid #FF6A1A; animation: ripple .8s ease-out 1.9s both"></span>
<span style="position: absolute; left: 110px; top: 40px; animation: cursorGo 1.2s cubic-bezier(.4,0,.2,1) .5s both"><svg width="44" height="44" viewBox="0 0 24 24" aria-hidden="true" style="filter: drop-shadow(0 6px 10px rgba(0,0,0,.7))"><path d="M4 2l16 9-7 2-3 7z" fill="#F2EDE7" stroke="#0A0908" stroke-width="1.4" stroke-linejoin="round"/></svg></span>
</div>
<div style="position: absolute; left: 34px; right: 34px; top: -80px; display: flex; align-items: center; gap: 12px; padding: 14px 18px; border-radius: 18px; background: rgba(242,237,231,0.96); color: #0A0908; box-shadow: 0 20px 40px -10px rgba(0,0,0,.8); animation: drop .6s cubic-bezier(.2,.8,.2,1) 2.35s both">{ic("bell", 24, "#C84A0C", 2.4, "animation: shake .8s ease-in-out infinite")}<span style="font-size: 22px; font-weight: 600">Ahora sigues a @ceos.growth</span></div>
</div>
<div style="position: relative; margin-top: 80px; animation: pop .7s cubic-bezier(.2,.8,.2,1) 1.0s both"><div style="animation: wob 4s ease-in-out infinite">
<div style="position: relative; overflow: hidden; padding: 30px 60px; border-radius: 34px; background: #FF6A1A; color: #0A0908; {BRIC}; font-size: 100px; line-height: 0.9; letter-spacing: -0.05em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 2s ease-in-out infinite">Síguenos<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.35), rgba(255,255,255,0)); animation: aShim 2s ease-in-out infinite"></div></div>
</div></div>
<p style="margin: 40px 0 0; font-family: 'Instrument Serif', serif; font-style: italic; font-size: 56px; line-height: 1.05; animation: aIn .8s cubic-bezier(.2,.8,.2,1) 1.3s both">para más tips de captación y ventas.</p>
</div>'''

for n, name, mid, title in [(1, 'Main', S1, '01'), (2, 'S2', S2, '02'), (3, 'S3', S3, '03'), (4, 'S4', S4, '04'), (5, 'S5', S5, '05')]:
    open(os.path.join(SRC, f'{name}.dc.html'), 'w').write(page(n, mid, title))
print('ok')
