#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel 2026-10-12 (valor: las 5 fases del lead en el CRM)."""
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
        tail = f'<span style="align-self: center; {MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.GROWTH · GUÁRDALO PARA TUS PRÓXIMAS CITAS</span>'
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


def h_static(l1, accent, size):
    # Titular visible desde el primer fotograma (portada de Instagram), con brillo que lo recorre
    return (f'<h2 style="position: relative; margin: 0; {BRIC}; font-size: {size}px; line-height: 0.95; letter-spacing: -0.05em">{l1}<br>'
            f'<span style="font-family: \'Instrument Serif\', serif; font-style: italic; font-weight: 400; letter-spacing: -0.015em; color: #FF6A1A; text-shadow: 0 0 40px rgba(255,106,26,.45)">{accent}</span></h2>')



EXTRA += '''
@keyframes wave{0%,100%{transform:scaleY(.22)}50%{transform:scaleY(1)}}
@keyframes sweep{from{stroke-dashoffset:754}to{stroke-dashoffset:0}}
@keyframes orbit{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@property --mn{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes mnc{from{--mn:0}to{--mn:15}}
.mn{counter-reset:mn var(--mn);animation:mnc 3.4s linear .3s both}
.mn::after{content:counter(mn)}
@property --sc{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes scc{from{--sc:0}to{--sc:59}}
.sc{counter-reset:sc var(--sc);animation:scc 2.4s linear 1.6s both}
.sc::after{content:counter(sc, decimal-leading-zero)}
@keyframes callOut{to{opacity:0;transform:scale(.96)}}
@keyframes callIn{from{opacity:0;transform:scale(1.04)}to{opacity:1;transform:none}}
@keyframes accept{0%,100%{transform:scale(1);box-shadow:0 0 0 0 rgba(255,106,26,.7)}50%{transform:scale(1.1);box-shadow:0 0 0 16px rgba(255,106,26,0)}}
@keyframes bubble{0%{opacity:0;transform:translateY(20px) scale(.9)}100%{opacity:1;transform:none}}
@keyframes typ{0%,47%{opacity:0;transform:translateY(12px)}50%,62%{opacity:1;transform:none}65%,100%{opacity:0}}
@keyframes growH{from{height:0}}
@keyframes scan{0%{top:-8%}100%{top:104%}}
@keyframes head{from{left:0%}to{left:100%}}
@keyframes segOn{from{background:rgba(242,237,231,0.1);box-shadow:none}to{background:linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A);box-shadow:0 0 22px -2px rgba(255,106,26,.8)}}
@keyframes rowAct{0%{border-color:rgba(242,237,231,0.08);background:rgba(242,237,231,0.025)}30%,70%{border-color:rgba(255,106,26,0.8);background:rgba(255,106,26,0.12)}100%{border-color:rgba(255,106,26,0.35);background:rgba(255,106,26,0.05)}}
@keyframes numOn{to{background:#FF6A1A;color:#0A0908;box-shadow:0 0 22px rgba(255,106,26,.8)}}
'''
ICON.update({
    'phoneoff': '<path d="M10.7 13.3a16 16 0 0 0 3.4 2.6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.4 19.4 0 0 1-3.3-2.6M5.2 13.4A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8"/><path d="M22 2L2 22"/>',
    'list': '<path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/>',
})


def wavebars(n, h, w=8, gap=6, color='#FF6A1A', dur=0.9):
    out = []
    for i in range(n):
        d = -((i * 0.37) % dur)
        hh = [0.5, 0.9, 0.7, 1.0, 0.6, 0.8, 0.45, 0.95, 0.65, 0.75][i % 10]
        out.append(f'<span style="width: {w}px; height: {int(h * hh)}px; border-radius: 99px; background: {color}; transform-origin: center; animation: wave {dur}s ease-in-out {d:.2f}s infinite"></span>')
    return f'<div style="display: flex; align-items: center; gap: {gap}px; height: {h}px">' + ''.join(out) + '</div>'


EXTRA += '''
@keyframes coolV{0%{height:96%;background:#FF6A1A;box-shadow:0 0 40px rgba(255,106,26,.9)}100%{height:16%;background:#6B635C;box-shadow:0 0 0 rgba(0,0,0,0)}}
@property --mw{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes mwc{from{--mw:0}to{--mw:60}}
.mw{counter-reset:mw var(--mw);animation:mwc 3.6s linear .2s both}
.mw::after{content:counter(mw)}
@keyframes lit{0%{background:#FF6A1A;box-shadow:0 0 0 10px rgba(255,106,26,.22),0 0 46px rgba(255,106,26,.9);transform:scale(1.12)}30%,100%{background:#2A2420;box-shadow:0 0 0 0 rgba(255,106,26,0);transform:scale(1)}}
@keyframes runX{from{left:0%}to{left:100%}}
@keyframes glowPulse{0%,100%{box-shadow:0 0 0 1px rgba(255,106,26,.5),0 20px 60px -20px rgba(255,106,26,.5)}50%{box-shadow:0 0 0 2px rgba(255,106,26,1),0 20px 80px -10px rgba(255,106,26,.9)}}
@keyframes snowIn{0%{opacity:0;transform:scale(.3) rotate(-90deg)}100%{opacity:1;transform:scale(1) rotate(0)}}
@keyframes spinSlow{from{transform:rotate(0)}to{transform:rotate(360deg)}}
@keyframes typeC{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
'''
ICON.update({
    'snow': '<path d="M12 2v20M4.9 4.9l14.2 14.2M2 12h20M4.9 19.1L19.1 4.9"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'form': '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
    'checks': '<path d="M2 12l5 5L17 7M12 16l1 1L23 7"/>',
})


def fade_seq(spans):
    """spans = [(texto, inicio, fin, color)] -> etiquetas que se van sustituyendo en el mismo sitio."""
    out = ''
    for txt, a, b, col in spans:
        anim = f'fadeIn .25s ease-out {a:.2f}s both' + (f', fadeOut .25s ease-in {b:.2f}s forwards' if b else '')
        if a == 0:
            anim = (f'fadeOut .25s ease-in {b:.2f}s forwards' if b else 'none')
        out += f'<span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; {BRIC}; font-size: 40px; letter-spacing: -0.03em; color: {col}; animation: {anim}">{txt}</span>'
    return out


EXTRA += '''
@keyframes leadDrop{0%{opacity:0;transform:translateY(-70px) scale(.94)}100%{opacity:1;transform:none}}
@keyframes tagGrey{0%{opacity:0;transform:scale(1.6) rotate(-6deg)}100%{opacity:1;transform:scale(1) rotate(-6deg)}}
@keyframes tapLoop{0%,30%,100%{transform:scale(1)}15%{transform:scale(.92)}}
@keyframes rippleLoop{0%{opacity:.9;transform:scale(.3)}40%,100%{opacity:0;transform:scale(2.4)}}
@keyframes fingerTap{0%,100%{transform:translate(0,0)}15%{transform:translate(-6px,8px) scale(.94)}30%{transform:translate(0,0)}}
@keyframes autofill{0%{background:rgba(242,237,231,0.04)}50%{background:rgba(255,178,122,0.22)}100%{background:rgba(242,237,231,0.04)}}
@keyframes selDot{from{transform:scale(0)}to{transform:scale(1)}}
@keyframes optOn{to{border-color:rgba(255,106,26,0.85);background:rgba(255,106,26,0.13);box-shadow:0 0 36px -10px rgba(255,106,26,.9)}}
@keyframes optDim{to{opacity:.38}}
@keyframes cur1{0%{transform:translate(380px,240px)}100%{transform:translate(0,0)}}
@keyframes cur2{0%{transform:translate(0,0)}100%{transform:translate(0,210px)}}
@keyframes cardOff{to{border-color:rgba(242,237,231,0.08);background:rgba(242,237,231,0.02);box-shadow:none}}
@keyframes radioOff{to{background:transparent;border-color:rgba(242,237,231,0.3);box-shadow:none}}
@keyframes radioOn{to{background:#FF6A1A;border-color:#FF6A1A;box-shadow:0 0 0 6px rgba(255,106,26,.25)}}
@keyframes leadFall{0%{top:-70px;opacity:0}12%{opacity:1}100%{top:330px;opacity:1}}
@keyframes sieveOut{0%{top:-70px;left:0;opacity:0}12%{opacity:1}55%{top:150px;left:0;opacity:1}100%{top:200px;left:-260px;opacity:0}}
'''
ICON.update({
    'tap': '<path d="M9 11V5a2 2 0 0 1 4 0v6"/><path d="M13 10a2 2 0 0 1 4 0v2"/><path d="M17 11a2 2 0 0 1 4 0v4a7 7 0 0 1-7 7h-1a7 7 0 0 1-6-3l-3-5a2 2 0 0 1 3.4-2L9 14"/>',
    'filter': '<path d="M3 4h18l-7 8.5V19l-4 2v-8.5z"/>',
    'help': '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 0 1 5 .5c0 1.5-2.5 2-2.5 3.5M12 17h.01"/>',
    'shield': '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
})

def field(label, val, d):
    return (f'<div style="display: flex; flex-direction: column; gap: 6px">'
            f'<span style="{MONO}; font-size: 13px; letter-spacing: 0.12em; color: #9C938B">{label}</span>'
            f'<div style="padding: 12px 14px; border-radius: 12px; border: 1px solid rgba(242,237,231,0.14); font-size: 18px; font-weight: 600; animation: autofill 1.2s ease-in-out {d:.2f}s infinite">'
            f'<span style="display: block; width: fit-content; overflow: hidden; white-space: nowrap; animation: typeC .35s steps(18,end) {d:.2f}s both">{val}</span></div></div>')

def cursor(anim):
    return f'<span style="position: absolute; z-index: 5; {anim}"><svg width="46" height="46" viewBox="0 0 24 24" aria-hidden="true" style="filter: drop-shadow(0 6px 10px rgba(0,0,0,.7))"><path d="M4 2l16 9-7 2-3 7z" fill="#F2EDE7" stroke="#0A0908" stroke-width="1.4" stroke-linejoin="round"/></svg></span>'


# =====================================================================
# 2026-10-03 · VALOR · Qué debe tener un guion de anuncio que convierte
# =====================================================================
EXTRA += '''
@keyframes feedScroll{0%{transform:translateY(0)}100%{transform:translateY(-798px)}}
@keyframes swipeUp{0%{transform:translateY(70px);opacity:0}25%{opacity:1}100%{transform:translateY(-130px);opacity:0}}
@property --t{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes tcnt{from{--t:0}to{--t:3}}
.tc{counter-reset:t var(--t);animation:tcnt 3s steps(3,end) .25s both}
.tc::after{content:counter(t)}
@keyframes flyUp{0%{transform:translateY(410px);opacity:0}12%{opacity:1}88%{opacity:1}100%{transform:translateY(-130px);opacity:0}}
@keyframes dimLine{to{color:#6B635C}}
@keyframes strikeW{from{width:0}to{width:100%}}
@keyframes playPulse{0%,100%{transform:scale(1);box-shadow:0 0 0 0 rgba(255,106,26,.6)}50%{transform:scale(1.08);box-shadow:0 0 0 22px rgba(255,106,26,0)}}
@keyframes headX{from{left:0%}to{left:100%}}
@keyframes btnPulse{0%,100%{box-shadow:0 0 0 0 rgba(255,106,26,.7)}50%{box-shadow:0 0 0 18px rgba(255,106,26,0)}}
@keyframes cur4{0%{transform:translate(170px,190px)}100%{transform:translate(0,0)}}
@keyframes dotRun{0%{left:0%}45%,55%{left:50%}100%{left:100%}}
@keyframes bellShake{0%,100%{transform:rotate(0)}10%{transform:rotate(-16deg)}20%{transform:rotate(14deg)}30%{transform:rotate(-10deg)}40%{transform:rotate(6deg)}50%{transform:rotate(0)}}
'''
ICON.update({
    'video': '<rect x="2" y="5" width="15" height="14" rx="2"/><path d="M17 10l5-3v10l-5-3z"/>',
    'pen': '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
})

SHIM = '<div style="position: absolute; inset: 0; border-radius: 34px; overflow: hidden; pointer-events: none"><div style="position: absolute; top: -10%; bottom: -10%; left: 0; width: 22%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,210,170,0.07), rgba(255,255,255,0)); animation: shim 2.6s ease-in-out infinite"></div></div>'


def grey_post(h=250):
    return (f'<div style="flex: none; height: {h}px; border-radius: 20px; background: rgba(242,237,231,0.05); border: 1px solid rgba(242,237,231,0.08); padding: 14px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">'
            f'<div style="display: flex; align-items: center; gap: 10px"><span style="width: 30px; height: 30px; border-radius: 99px; background: rgba(242,237,231,0.14)"></span><span style="width: 110px; height: 10px; border-radius: 99px; background: rgba(242,237,231,0.14)"></span></div>'
            f'<div style="flex: 1; border-radius: 14px; background: linear-gradient(160deg, rgba(242,237,231,0.1), rgba(242,237,231,0.03))"></div></div>')



# =====================================================================
# 2026-10-05 · VALOR · Errores típicos al grabar anuncios con el móvil
# =====================================================================
EXTRA += '''
@keyframes camShake{0%,100%{transform:translate(0,0) rotate(0)}10%{transform:translate(-7px,4px) rotate(-1.2deg)}20%{transform:translate(6px,-5px) rotate(1deg)}30%{transform:translate(-5px,-3px) rotate(-.6deg)}40%{transform:translate(7px,5px) rotate(1.3deg)}50%{transform:translate(-4px,6px) rotate(-1deg)}60%{transform:translate(5px,-6px) rotate(.8deg)}70%{transform:translate(-6px,2px) rotate(-1.1deg)}80%{transform:translate(4px,4px) rotate(.6deg)}90%{transform:translate(-3px,-5px) rotate(-.4deg)}}
@keyframes focusP{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.12);opacity:.55}}
@keyframes warnIn{0%{opacity:0;transform:translateX(40px) scale(.9)}100%{opacity:1;transform:none}}
@keyframes warnGlow{0%,100%{border-color:rgba(255,106,26,0.45);box-shadow:0 0 0 0 rgba(255,106,26,0)}50%{border-color:rgba(255,106,26,1);box-shadow:0 0 34px -6px rgba(255,106,26,.9)}}
@keyframes waveJ{0%,100%{transform:scaleY(.25)}30%{transform:scaleY(1)}55%{transform:scaleY(.4)}80%{transform:scaleY(.85)}}
@keyframes flare{0%,100%{opacity:.75;transform:scale(1)}50%{opacity:1;transform:scale(1.15)}}
@keyframes rotUp{0%,30%{transform:rotate(-90deg)}55%,100%{transform:rotate(0deg)}}
@keyframes vidGrow{0%,30%{height:34%}55%,100%{height:100%}}
@keyframes barsOut{0%,30%{opacity:1}50%,100%{opacity:0}}
@keyframes arcSpin{0%,25%{transform:rotate(0)}55%,100%{transform:rotate(-90deg)}}
@keyframes wipe{0%,12%{clip-path:inset(0 100% 0 0)}70%,100%{clip-path:inset(0 0 0 0)}}
@keyframes wipeH{0%,12%{left:0%}70%,100%{left:100%}}
@keyframes sunMove{0%,20%{left:78%}60%,100%{left:10%}}
@keyframes turn{0%,20%{transform:scaleX(-1)}50%,100%{transform:scaleX(1)}}
@keyframes micGo{0%,25%{transform:translateX(0)}55%,100%{transform:translateX(-470px)}}
@keyframes noisyOut{0%,40%{opacity:1}55%,100%{opacity:0}}
@keyframes cleanIn{0%,45%{opacity:0}60%,100%{opacity:1}}
@keyframes lvl{0%,40%{width:22%;background:#6B635C}60%,100%{width:78%;background:linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A)}}
@keyframes echo{0%{transform:scale(.4);opacity:.8}100%{transform:scale(2.2);opacity:0}}
@keyframes echoStop{0%,45%{opacity:1}55%,100%{opacity:0}}
'''
ICON.update({
    'rotate': '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    'warn': '<path d="M12 3l10 18H2z"/><path d="M12 10v4M12 18h.01"/>',
    'cam': '<path d="M3 8a2 2 0 0 1 2-2h2l2-2h6l2 2h2a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><circle cx="12" cy="13" r="4"/>',
})


def person(body='#1A1512', size=220, lit=False):
    face = 'url(#gLit)' if lit else body
    grad = ('<defs><radialGradient id="gLit" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#FFD2AE"/><stop offset=".6" stop-color="#E39A68"/><stop offset="1" stop-color="#9A5A34"/></radialGradient></defs>' if lit else '')
    shirt = '#C84A0C' if lit else body
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" aria-hidden="true">{grad}'
            f'<circle cx="50" cy="36" r="19" fill="{face}"/>'
            f'<path d="M12 100c0-22 17-36 38-36s38 14 38 36z" fill="{shirt}"/></svg>')


def rec(top=20, left=20):
    return (f'<div style="position: absolute; top: {top}px; left: {left}px; z-index: 4; display: flex; align-items: center; gap: 8px; padding: 6px 12px; border-radius: 99px; background: rgba(10,9,8,0.7)">'
            f'<span style="width: 12px; height: 12px; border-radius: 99px; background: #FF3B1A; box-shadow: 0 0 10px #FF3B1A; animation: aBlink 1s steps(2,end) infinite"></span>'
            f'<span style="{MONO}; font-size: 15px; color: #F2EDE7">REC 00:0<span class="tc"></span></span></div>')


def thirds():
    return ('<div style="position: absolute; inset: 0; z-index: 2; pointer-events: none; background-image: linear-gradient(90deg, transparent 33%, rgba(242,237,231,0.16) 33%, rgba(242,237,231,0.16) calc(33% + 1px), transparent calc(33% + 1px), transparent 66%, rgba(242,237,231,0.16) 66%, rgba(242,237,231,0.16) calc(66% + 1px), transparent calc(66% + 1px)), linear-gradient(0deg, transparent 33%, rgba(242,237,231,0.16) 33%, rgba(242,237,231,0.16) calc(33% + 1px), transparent calc(33% + 1px), transparent 66%, rgba(242,237,231,0.16) 66%, rgba(242,237,231,0.16) calc(66% + 1px), transparent calc(66% + 1px))"></div>')


def jwave(n, h, color, w=8, gap=6, dur=0.7):
    out = []
    for i in range(n):
        hh = [0.5, 1.0, 0.35, 0.9, 0.6, 0.95, 0.3, 0.8, 0.55, 1.0, 0.4, 0.75][i % 12]
        out.append(f'<span style="width: {w}px; height: {int(h*hh)}px; border-radius: 99px; background: {color}; animation: waveJ {dur}s ease-in-out {-(i*0.13) % dur:.2f}s infinite"></span>')
    return f'<div style="display: flex; align-items: center; gap: {gap}px; height: {h}px">' + ''.join(out) + '</div>'


WINDOW_BG = 'radial-gradient(circle at 50% 38%, #FFF6EA 0%, #FFD9B0 22%, #E98A4B 46%, #3A1C0B 72%, #140D09 100%)'


# =====================================================================
# 2026-10-06 · VALOR · Cómo conseguir que el lead se presente a la cita
# =====================================================================
EXTRA += '''
@keyframes nowLine{from{top:0%}to{top:100%}}
@keyframes rowMiss{0%{border-color:rgba(255,106,26,0.8);background:rgba(255,106,26,0.12)}100%{border-color:rgba(242,237,231,0.06);background:rgba(242,237,231,0.015)}}
@keyframes nameGrey{to{color:#6B635C;text-decoration:line-through;text-decoration-color:rgba(255,106,26,.7)}}
@keyframes callRing{0%{transform:scale(1);opacity:.7}100%{transform:scale(2.3);opacity:0}}
@keyframes callShake{0%,100%{transform:rotate(0)}5%{transform:rotate(-14deg)}10%{transform:rotate(12deg)}15%{transform:rotate(-8deg)}20%{transform:rotate(0)}}
@keyframes travelX{from{left:0%}to{left:100%}}
@keyframes travelX2{0%{left:0%}40%,100%{left:100%}}
@keyframes heatDown{0%{width:100%;background:linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A)}100%{width:12%;background:linear-gradient(90deg,#4A4540,#6B635C,#9C938B)}}
@keyframes heatHold{0%,100%{width:96%;box-shadow:0 0 18px rgba(255,106,26,.6)}50%{width:100%;box-shadow:0 0 30px rgba(255,106,26,1)}}
@keyframes cellPass{0%{background:#FF6A1A;box-shadow:0 0 20px rgba(255,106,26,.9)}100%{background:rgba(242,237,231,0.08);box-shadow:none}}
@keyframes cellGo{to{background:#FF6A1A;box-shadow:0 0 22px rgba(255,106,26,.9)}}
@keyframes notifDrop{0%{opacity:0;transform:translateY(-50px) scale(.92)}100%{opacity:1;transform:none}}
@keyframes phaseOn{to{border-color:rgba(255,106,26,0.85);background:rgba(255,106,26,0.12);color:#F2EDE7;box-shadow:0 0 34px -10px rgba(255,106,26,.9)}}
@keyframes dotOn{to{background:#FF6A1A;border-color:#FF6A1A;box-shadow:0 0 0 6px rgba(255,106,26,.22),0 0 20px rgba(255,106,26,.9)}}
@keyframes railFill{from{height:0}to{height:100%}}
@keyframes btnTap{0%,100%{transform:scale(1)}50%{transform:scale(.92)}}
@keyframes btnWin{to{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A;box-shadow:0 0 30px rgba(255,106,26,.8)}}
@keyframes finger{0%{transform:translate(120px,140px);opacity:0}30%{opacity:1}100%{transform:translate(0,0);opacity:1}}
@property --hh{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes hhc{from{--hh:0}to{--hh:59}}
.hh{counter-reset:hh var(--hh);animation:hhc 3.6s linear .2s both}
.hh::after{content:'09:' counter(hh, decimal-leading-zero)}
@property --rs{syntax:'<integer>';inherits:false;initial-value:1}
@keyframes rsc{from{--rs:1}to{--rs:9}}
.rs{counter-reset:rs var(--rs);animation:rsc 3.6s steps(8,end) .2s both}
.rs::after{content:'00:0' counter(rs)}
'''
ICON.update({
    'whats': '<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/><path d="M9 9.5c.5 2 2 3.5 4 4l1.2-1.2 2 1-.6 1.8c-3.5.4-7.6-3.7-7.2-7.2l1.8-.6 1 2z"/>',
    'repeat': '<path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/>',
})

def chip(txt, col, bg, border, extra=''):
    return f'<span style="{MONO}; font-size: 15px; font-weight: 600; letter-spacing: 0.1em; color: {col}; padding: 7px 12px; border-radius: 99px; background: {bg}; border: 1px solid {border}; white-space: nowrap; {extra}">{txt}</span>'




# =====================================================================
# 2026-10-08 · VALOR · Remarketing: quien vio tu anuncio y no dejó datos
# =====================================================================
EXTRA += '''
@keyframes outUp{0%{transform:none;opacity:1}100%{transform:translateY(-115%);opacity:.2}}
@keyframes inUp{0%{transform:translateY(105%)}100%{transform:none}}
@keyframes swipeF{0%{transform:translateY(90px);opacity:0}20%{opacity:1}80%{opacity:1}100%{transform:translateY(-150px);opacity:0}}
@keyframes vprog{from{width:0}to{width:100%}}
@keyframes nodeAct{to{background:#FF6A1A;border-color:#FF6A1A;box-shadow:0 0 0 8px rgba(255,106,26,.2),0 0 30px rgba(255,106,26,.9)}}
@keyframes nodeTxt{to{color:#F2EDE7}}
@keyframes railDot{0%{top:0%;opacity:0}8%{opacity:1}92%{opacity:1}100%{top:100%;opacity:0}}
@keyframes railGrow{from{height:0}to{height:100%}}
@keyframes ghost{to{opacity:.5;filter:grayscale(1)}}
@keyframes dayLit{0%{background:rgba(242,237,231,0.06);color:#6B635C}15%{background:#FF6A1A;box-shadow:0 0 18px rgba(255,106,26,.9);color:#0A0908}100%{background:rgba(242,237,231,0.06);box-shadow:none;color:#6B635C}}
@keyframes blurOut{from{filter:blur(0) grayscale(0);opacity:1}to{filter:blur(2.5px) grayscale(1);opacity:.5}}
@keyframes curA{0%{transform:translate(520px,40px)}20%{transform:translate(0,0)}33%{transform:translate(0,0)}46%{transform:translate(0,98px)}58%{transform:translate(0,98px)}70%{transform:translate(0,196px)}74%{transform:translate(0,196px)}82%,100%{transform:translate(40px,294px)}}
@keyframes tOn{to{left:38px;background:#0A0908}}
@keyframes tTrack{to{background:#FF6A1A;box-shadow:0 0 22px rgba(255,106,26,.8)}}
@keyframes ringP{0%,100%{filter:drop-shadow(0 0 6px rgba(255,106,26,.6))}50%{filter:drop-shadow(0 0 18px rgba(255,106,26,1))}}
@property --au{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes auc{from{--au:0}to{--au:3}}
.au{counter-reset:au var(--au);animation:auc 2.6s steps(3,end) .7s both}
.au::after{content:counter(au) ' de 3'}
@keyframes car3{0%,22%{transform:translateX(0)}30%,55%{transform:translateX(-33.333%)}63%,100%{transform:translateX(-66.666%)}}
@keyframes pip1{0%,22%{background:#FF6A1A;width:34px}30%,100%{background:rgba(242,237,231,0.2);width:12px}}
@keyframes pip2{0%,22%{background:rgba(242,237,231,0.2);width:12px}30%,55%{background:#FF6A1A;width:34px}63%,100%{background:rgba(242,237,231,0.2);width:12px}}
@keyframes pip3{0%,55%{background:rgba(242,237,231,0.2);width:12px}63%,100%{background:#FF6A1A;width:34px}}
@keyframes arrowRun{0%{transform:translateX(-14px);opacity:.3}50%{opacity:1}100%{transform:translateX(14px);opacity:.3}}
@keyframes eyeBlink{0%,44%,52%,100%{transform:scaleY(1)}48%{transform:scaleY(.1)}}
'''
ICON.update({
    'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.6"/><path d="M16 14.2a5 5 0 0 1 6 4.8"/>',
    'quote': '<path d="M7 7h4v4c0 3-1.5 5-4 6M15 7h4v4c0 3-1.5 5-4 6"/>',
    'minus': '<path d="M5 12h14"/>',
    'hand': '<path d="M18 11V6a2 2 0 0 0-4 0v5M14 10V4a2 2 0 0 0-4 0v6M10 10.5V6a2 2 0 0 0-4 0v8a8 8 0 0 0 16 0v-3a2 2 0 0 0-4 0"/>',
})


def ad_header(tag=''):
    t = f'<span style="margin-left: auto">{tag}</span>' if tag else ''
    return (f'<div style="display: flex; align-items: center; gap: 10px; padding: 12px 14px">'
            f'<span style="width: 36px; height: 36px; border-radius: 99px; background: linear-gradient(135deg,#FFB27A,#FF6A1A); display: flex; align-items: center; justify-content: center; {BRIC}; font-size: 16px; color: #0A0908">TU</span>'
            f'<div style="display: flex; flex-direction: column"><span style="font-size: 17px; font-weight: 700">Tu negocio</span><span style="font-size: 13px; color: #9C938B">Publicidad</span></div>{t}</div>')



# =====================================================================
# 2026-10-09 · VALOR · Enviaste el presupuesto y no contesta
# =====================================================================
EXTRA += '''
@keyframes tickBlue{to{color:#FF6A1A}}
@keyframes typLoop{0%,15%{opacity:0;transform:translateY(8px)}25%,55%{opacity:1;transform:none}65%,100%{opacity:0;transform:translateY(-4px)}}
@property --dy{syntax:'<integer>';inherits:false;initial-value:2}
@keyframes dyc{from{--dy:2}to{--dy:6}}
.dy{counter-reset:dy var(--dy);animation:dyc 3.4s steps(4,end) .4s both}
.dy::after{content:counter(dy) ' días'}
@keyframes coolW{0%{width:100%;background:linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A)}100%{width:10%;background:linear-gradient(90deg,#4A4540,#6B635C,#9C938B)}}
@keyframes mailIn{0%{opacity:0;max-height:0;transform:translateY(-20px)}100%{opacity:1;max-height:80px;transform:none}}
@keyframes sinkGrey{to{opacity:.4;filter:grayscale(1)}}
@keyframes slotPick{to{background:#FF6A1A;color:#0A0908;border-color:#FF6A1A;box-shadow:0 0 28px rgba(255,106,26,.85)}}
@keyframes curB{0%{transform:translate(360px,260px)}55%,100%{transform:translate(0,0)}}
@keyframes cycleOpt{0%,100%{border-color:rgba(242,237,231,0.14);background:rgba(242,237,231,0.04);color:#B5ADA4}10%,28%{border-color:rgba(255,106,26,0.9);background:rgba(255,106,26,0.16);color:#F2EDE7;box-shadow:0 0 28px -6px rgba(255,106,26,.9)}38%{border-color:rgba(242,237,231,0.14);background:rgba(242,237,231,0.04);color:#B5ADA4;box-shadow:none}}
@keyframes envFly{0%{transform:translate(0,0) rotate(0) scale(1);opacity:1}100%{transform:translate(330px,40px) rotate(8deg) scale(.5);opacity:0}}
'''
ICON.update({
    'file': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
    'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>',
    'tag': '<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/>',
})


def bubble_me(txt, d, extra=''):
    return (f'<div style="align-self: flex-end; max-width: 78%; padding: 12px 16px; border-radius: 18px 18px 4px 18px; background: #3A2214; border: 1px solid rgba(255,106,26,.35); font-size: 19px; line-height: 1.3; animation: bubble .45s cubic-bezier(.2,.8,.2,1) {d:.2f}s both; {extra}">{txt}</div>')


def bubble_them(txt, d):
    return (f'<div style="align-self: flex-start; max-width: 78%; padding: 12px 16px; border-radius: 18px 18px 18px 4px; background: #24201D; border: 1px solid rgba(242,237,231,.1); font-size: 19px; line-height: 1.3; animation: bubble .45s cubic-bezier(.2,.8,.2,1) {d:.2f}s both">{txt}</div>')


def chat_head(name='Lead · Presupuesto'):
    return (f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-bottom: 1px solid rgba(242,237,231,0.08)">'
            f'<span style="width: 40px; height: 40px; border-radius: 99px; background: rgba(242,237,231,0.12); display: flex; align-items: center; justify-content: center">{ic("user", 22, "#B5ADA4", 2.2)}</span>'
            f'<div style="display: flex; flex-direction: column"><span style="font-size: 18px; font-weight: 700">{name}</span><span style="font-size: 13px; color: #9C938B">en línea</span></div>'
            f'<span style="margin-left: auto">{ic("whats", 24, "#FF6A1A", 2)}</span></div>')


# =====================================================================
# 2026-10-10 · VALOR · La ficha del lead en 4 campos antes de llamar
# =====================================================================
EXTRA += '''
@keyframes qBlink{0%,100%{border-color:rgba(242,237,231,0.1);background:rgba(242,237,231,0.03)}50%{border-color:rgba(255,106,26,0.85);background:rgba(255,106,26,0.1);box-shadow:0 0 26px -8px rgba(255,106,26,.9)}}
@keyframes qMark{0%,100%{transform:scale(1);opacity:.5}50%{transform:scale(1.25);opacity:1}}
@keyframes lensR{0%{transform:translate(0,0)}25%{transform:translate(520px,20px)}50%{transform:translate(480px,150px)}75%{transform:translate(60px,140px)}100%{transform:translate(0,0)}}
@keyframes flyDot{0%{left:0%;opacity:0}10%{opacity:1}90%{opacity:1}100%{left:100%;opacity:0}}
@keyframes fieldDone{to{border-color:rgba(255,106,26,0.7);background:rgba(255,106,26,0.08)}}
@keyframes caretB{0%,100%{opacity:1}50%{opacity:0}}
@keyframes slideUpIn{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
'''


def ficha_row(label, value, d=None, glow=None, extra=''):
    """Fila de la ficha. value=None -> '?' parpadeando."""
    if value is None:
        v = f'<span style="{BRIC}; font-size: 30px; color: #FF6A1A; animation: qMark 1.4s ease-in-out {glow or 0:.2f}s infinite">?</span>'
        anim = f'animation: qBlink 1.4s ease-in-out {glow or 0:.2f}s infinite'
    else:
        v = f'<span style="font-size: 20px; font-weight: 600; text-align: right">{value}</span>'
        anim = ''
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 14px 18px; border-radius: 16px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); {anim}; {extra}">'
            f'<span style="{MONO}; font-size: 15px; letter-spacing: 0.12em; color: #9C938B">{label}</span>{v}</div>')



# =====================================================================
# 2026-10-12 · VALOR · Las 5 fases del lead en el CRM
# =====================================================================
EXTRA += '''
@keyframes listScroll{from{transform:translateY(0)}to{transform:translateY(-576px)}}
@keyframes kMove{0%,12%{transform:translateX(0)}20%,32%{transform:translateX(174.8px)}40%,52%{transform:translateX(349.6px)}60%,72%{transform:translateX(524.4px)}80%,100%{transform:translateX(699.2px)}}
@keyframes colOn{to{border-color:rgba(255,106,26,0.55);background:rgba(255,106,26,0.06)}}
@keyframes pileShake{0%,100%{transform:rotate(0)}25%{transform:rotate(-1.5deg)}75%{transform:rotate(1.5deg)}}
@keyframes popIn{0%{opacity:0;transform:scale(.4)}70%{opacity:1;transform:scale(1.12)}100%{opacity:1;transform:scale(1)}}
'''
ICON.update({
    'kanban': '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18M15 3v18"/>',
})

LEADS = ['Clínica dental', 'Reformas Norte', 'Academia de inglés', 'Inmobiliaria', 'Gimnasio', 'Taller mecánico', 'Centro estético', 'Asesoría']


def list_row(name, i):
    q = f'<span style="{BRIC}; font-size: 26px; color: #FF6A1A; animation: qMark 1.4s ease-in-out {-(i*0.37) % 1.4:.2f}s infinite">?</span>'
    return (f'<div style="flex: none; height: 62px; box-sizing: border-box; display: grid; grid-template-columns: 1.6fr 1fr 1fr; align-items: center; gap: 12px; padding: 0 18px; border-radius: 14px; border: 1px solid rgba(242,237,231,0.08); background: rgba(242,237,231,0.03)">'
            f'<span style="display: flex; align-items: center; gap: 12px; font-size: 21px; font-weight: 600"><span style="width: 32px; height: 32px; border-radius: 99px; background: rgba(242,237,231,0.1); display: flex; align-items: center; justify-content: center">{ic("user", 18, "#9C938B", 2.2)}</span>{name}</span>'
            f'<span style="{MONO}; font-size: 20px; color: #6B635C; text-align: center">—</span>'
            f'<span style="text-align: center">{q}</span></div>')


# ---------- 01 GANCHO: el CRM convertido en una lista ----------
rows = ''.join(list_row(n, i) for i, n in enumerate(LEADS + LEADS))
S1 = f'''{h_static("Si tu CRM es una lista,", "pierdes leads sin verlo.", 92)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 26px; {CARD}; display: flex; flex-direction: column; gap: 14px; animation: fxFloat 4s ease-in-out infinite">
{SHIM}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("list", 22, "#9C938B", 2.2)}LEADS · 1 SOLA LISTA</span>{EJ}</div>
<div style="display: grid; grid-template-columns: 1.6fr 1fr 1fr; gap: 12px; padding: 0 18px; {MONO}; font-size: 14px; letter-spacing: 0.12em; color: #9C938B"><span>LEAD</span><span style="text-align: center">FASE</span><span style="text-align: center">SIGUIENTE PASO</span></div>
<div style="position: relative; height: 420px; overflow: hidden; -webkit-mask-image: linear-gradient(180deg, transparent 0, #000 12%, #000 82%, transparent 100%); mask-image: linear-gradient(180deg, transparent 0, #000 12%, #000 82%, transparent 100%)">
<div style="display: flex; flex-direction: column; gap: 10px; animation: listScroll 4s linear infinite">{rows}</div>
</div>
<div style="display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-radius: 16px; border: 1px dashed rgba(255,106,26,0.5); color: #FFB27A; font-size: 20px; font-weight: 600; animation: warnGlow 1.6s ease-in-out infinite">{ic("warn", 24, "#FF6A1A", 2.2)}Nadie sabe en qué punto está cada uno</div>
</div>
{sub("Las 5 fases que ordenan a tus leads.")}'''

# ---------- 02 Sin fases no sabes qué toca hoy ----------
pile = ''
for i, n in enumerate(LEADS[:5]):
    d = 0.2 + i * 0.3
    pile += (f'<div style="animation: leadDrop .5s cubic-bezier(.2,.8,.2,1) {d:.2f}s both"><div style="display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-radius: 14px; border: 1px solid rgba(242,237,231,0.1); background: #1E1A17; font-size: 20px; font-weight: 600; animation: pileShake 1.2s ease-in-out {d + 0.6 + i*0.1:.2f}s infinite">'
             f'{ic("user", 20, "#9C938B", 2.2)}{n}</div></div>')
opts = ''
for i, t in enumerate(['¿Le llamo?', '¿Le mando el presupuesto?', '¿Le confirmo la cita?']):
    opts += (f'<div style="display: flex; align-items: center; gap: 12px; padding: 18px 20px; border-radius: 16px; border: 1px solid rgba(242,237,231,0.14); font-size: 22px; font-weight: 600; animation: cycleOpt 2.4s ease-in-out {i*0.8:.2f}s infinite">'
             f'{ic("help", 24, "#FF6A1A", 2.2)}{t}</div>')
S2 = f'''{headline("Sin fases, no sabes", "qué toca con cada uno.", 92)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 28px; {CARD}; display: flex; flex-direction: column; gap: 18px; {TILT}">
{SHIM}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("cal", 22, "#9C938B", 2.2)}LUNES · 09:00</span>{EJ}</div>
<div style="display: flex; gap: 22px; align-items: stretch">
<div style="flex: none; width: 380px; padding: 16px; border-radius: 20px; border: 2px dashed rgba(242,237,231,0.14); display: flex; flex-direction: column; gap: 10px">
<span style="{MONO}; font-size: 14px; letter-spacing: 0.12em; color: #9C938B">TODOS JUNTOS</span>{pile}</div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 14px; justify-content: center">
<span style="{MONO}; font-size: 14px; letter-spacing: 0.12em; color: #9C938B">Y CADA DÍA, A OJO:</span>{opts}</div>
</div>
</div>
{sub("Unos se llaman dos veces y otros nunca.")}'''

# ---------- 03 Las 5 fases: tablero con una tarjeta que avanza ----------
PH = ['NUEVO', 'CONTACTADO', 'CITA', 'PROPUESTA', 'CERRADO']
cols = ''
for i, p in enumerate(PH):
    t = i * 0.8
    on = f'animation: colOn .35s ease-out {t:.2f}s both' if i else 'animation: colOn .01s linear 0s both'
    dot = f'animation: dotOn .35s ease-out {t:.2f}s both' if i else 'animation: dotOn .01s linear 0s both'
    ghosts = ''.join('<div style="height: 64px; border-radius: 12px; background: rgba(242,237,231,0.05); border: 1px solid rgba(242,237,231,0.07)"></div>' for _ in range(2 if i < 3 else 1))
    cols += (f'<div style="height: 380px; box-sizing: border-box; padding: 14px 10px; border-radius: 16px; border: 1px solid rgba(242,237,231,0.08); background: rgba(242,237,231,0.02); display: flex; flex-direction: column; gap: 10px; {on}">'
             f'<div style="display: flex; align-items: center; gap: 8px"><span style="flex: none; width: 12px; height: 12px; border-radius: 99px; border: 2px solid rgba(242,237,231,0.3); {dot}"></span>'
             f'<span style="{MONO}; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; color: #D9D1C8">{i+1}·{p}</span></div>'
             f'<div style="margin-top: auto; display: flex; flex-direction: column; gap: 10px">{ghosts}</div></div>')
mover = (f'<div style="position: absolute; top: 52px; left: 0; width: 164.8px; z-index: 4; animation: kMove 4s cubic-bezier(.6,0,.3,1) 0s both">'
         f'<div style="padding: 12px; box-sizing: border-box; border-radius: 14px; background: linear-gradient(160deg,#3A2214,#1E1A17); border: 1px solid rgba(255,106,26,0.8); box-shadow: 0 20px 40px -12px rgba(0,0,0,.8), 0 0 30px -6px rgba(255,106,26,.8); display: flex; flex-direction: column; gap: 8px; animation: upBob 1s ease-in-out infinite">'
         f'<span style="display: flex; align-items: center; gap: 8px; font-size: 17px; font-weight: 700">{ic("user", 18, "#FF6A1A", 2.4)}Clínica</span>'
         f'<span style="font-size: 14px; color: #B5ADA4">Lead de Meta</span>'
         f'<div style="height: 6px; border-radius: 99px; background: rgba(242,237,231,0.1); overflow: hidden"><div style="height: 100%; background: linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A); animation: fillW 4s cubic-bezier(.6,0,.3,1) both"></div></div></div></div>')
won = f'<span style="position: absolute; top: 200px; left: 712px; z-index: 5; animation: popIn .5s cubic-bezier(.2,.8,.2,1) 3.3s both">{chip("GANADO", "#0A0908", "#FF6A1A", "#FF6A1A", "box-shadow: 0 0 24px rgba(255,106,26,.9)")}</span>'
S3 = f'''{headline("Las 5 fases", "de cada lead.", 100)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 28px; {CARD}; display: flex; flex-direction: column; gap: 18px; {TILT}">
{SHIM}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("kanban", 22, "#9C938B", 2.2)}TABLERO DEL CRM</span>{EJ}</div>
<div style="position: relative; display: grid; grid-template-columns: repeat(5, 164.8px); gap: 10px">{cols}{mover}{won}</div>
</div>
{sub("Mueve la tarjeta cada vez que pasa algo.")}'''

# ---------- 04 Cada fase con su siguiente paso y fecha ----------
S4 = f'''{headline("Cada fase, con su", "siguiente paso y fecha.", 88)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 28px; {CARD}; display: flex; flex-direction: column; gap: 16px; {TILT}">
{SHIM}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("user", 22, "#9C938B", 2.2)}FICHA · CLÍNICA DENTAL</span>{EJ}</div>
<div style="display: flex; align-items: center; gap: 10px">{chip("1·NUEVO", "#6B635C", "transparent", "rgba(242,237,231,0.12)")}{chip("2·CONTACTADO", "#6B635C", "transparent", "rgba(242,237,231,0.12)")}<span style="animation: qPulse 1.6s ease-in-out infinite; border-radius: 99px">{chip("3·CITA", "#0A0908", "#FF6A1A", "#FF6A1A")}</span>{chip("4·PROPUESTA", "#6B635C", "transparent", "rgba(242,237,231,0.12)")}</div>
<div style="display: grid; grid-template-columns: 1.4fr 1fr; gap: 14px; padding: 18px; border-radius: 20px; border: 1px solid rgba(255,106,26,0.5); background: rgba(255,106,26,0.05); animation: glowPulse 1.8s ease-in-out infinite">
{field("SIGUIENTE PASO", "Confirmar cita por WhatsApp", 0.6)}
{field("FECHA", "Mañana · 10:00", 1.4)}
</div>
<div style="display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 16px 20px; border-radius: 16px; border: 1px solid rgba(255,106,26,0.45); animation: warnIn .5s ease-out 2.1s both, warnGlow 1.4s ease-in-out 2.6s infinite">
<span style="display: flex; align-items: center; gap: 12px; font-size: 21px; font-weight: 600"><span style="display: inline-flex; animation: bellShake 1.4s ease-in-out infinite">{ic("bell", 26, "#FF6A1A", 2.2)}</span>Reformas Norte · sin siguiente paso</span>
<span style="{MONO}; font-size: 14px; letter-spacing: 0.1em; color: #FFB27A">REVISAR HOY</span></div>
<div style="display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 16px 20px; border-radius: 16px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); animation: slideUpIn .5s ease-out 2.7s both">
<span style="display: flex; align-items: center; gap: 12px; font-size: 21px; font-weight: 600">{ic("x", 24, "#9C938B", 2.4)}Cerrado perdido</span>
<span style="animation: stamp .5s ease-out 3.1s both; display: inline-flex">{chip("MOTIVO: PRECIO", "#FFB27A", "rgba(255,106,26,0.1)", "rgba(255,106,26,0.6)")}</span></div>
</div>
{sub("Un lead sin siguiente paso se queda parado.")}'''

# ---------- 05 CTA ----------
checks = [('kanban', 'Nuevo, contactado, cita, propuesta, cerrado'), ('arrow', 'Mueve la tarjeta cuando pasa algo'), ('cal', 'Siguiente paso y fecha en cada lead'), ('tag', 'Perdido, siempre con su motivo')]
crows = ''
for i, (icn, t) in enumerate(checks):
    d = 0.5 + i * 0.45
    crows += (f'<div style="display: flex; align-items: center; gap: 18px; padding: 14px 20px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); animation: rowOn .5s ease-out {d:.2f}s both">'
              f'<span style="flex: none; width: 42px; height: 42px; border-radius: 12px; border: 2px solid rgba(242,237,231,0.25); display: flex; align-items: center; justify-content: center; animation: check .45s ease-out {d:.2f}s both">{ic("ok", 26, "#0A0908", 3.4)}</span>'
              f'<span style="flex: 1; font-size: 26px; font-weight: 600; text-align: left">{t}</span>{ic(icn, 30, "#FF6A1A", 2.2)}</div>')
S5 = f'''<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0 0 36px; {BRIC}; font-size: 80px; line-height: 1; letter-spacing: -0.045em; animation: aIn .8s cubic-bezier(.2,.8,.2,1) .1s both">Cada lead,<br><span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">en su fase.</span></p>
<div style="position: relative; width: 900px; box-sizing: border-box; padding: 26px; {CARD}; display: flex; flex-direction: column; gap: 12px; {TILT}">
{SHIM}
<span style="{LBL}; text-align: left">TU CRM · 5 FASES</span>
{crows}
</div>
<div style="position: relative; margin-top: 50px; animation: pop .7s cubic-bezier(.2,.8,.2,1) 2.3s both"><div style="animation: wob 4s ease-in-out infinite">
<div style="position: relative; overflow: hidden; padding: 30px 60px; border-radius: 34px; background: #FF6A1A; color: #0A0908; {BRIC}; font-size: 100px; line-height: 0.9; letter-spacing: -0.05em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 2s ease-in-out infinite">Síguenos<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.35), rgba(255,255,255,0)); animation: aShim 2s ease-in-out infinite"></div></div>
</div></div>
<p style="margin: 30px 0 0; font-family: 'Instrument Serif', serif; font-style: italic; font-size: 56px; line-height: 1.05; animation: aIn .8s cubic-bezier(.2,.8,.2,1) 2.6s both">para más tips de captación y ventas.</p>
</div>'''

for n, name, mid, title in [(1, 'Main', S1, '01'), (2, 'S2', S2, '02'), (3, 'S3', S3, '03'), (4, 'S4', S4, '04'), (5, 'S5', S5, '05')]:
    html = page(n, mid, title).replace('GUÁRDALO PARA TUS PRÓXIMAS CITAS', 'GUÁRDALO PARA ORDENAR TU CRM')
    open(os.path.join(SRC, f'{name}.dc.html'), 'w').write(html)
print('ok')
