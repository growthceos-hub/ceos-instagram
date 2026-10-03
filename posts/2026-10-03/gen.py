#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel 2026-10-03 (valor: qué debe tener un guion de anuncio que convierte)."""
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
        tail = f'<span style="align-self: center; {MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.GROWTH · GUÁRDALO PARA TU PRÓXIMA CAMPAÑA</span>'
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


# ---------- 01 GANCHO: el feed pasa rápido… y se para en tu anuncio ----------
hook_words = '¿Tu cocina se ha quedado vieja?'.split(' ')
hw = ''.join(f'<span style="display: inline-block; margin-right: 7px; animation: aIn .35s cubic-bezier(.2,.8,.2,1) {1.75 + i*0.16:.2f}s both">{w}</span>' for i, w in enumerate(hook_words))
ad_card = f'''<div style="flex: none; height: 420px; border-radius: 22px; position: relative; overflow: hidden; background: radial-gradient(circle at 30% 20%, #3A1C0B, #140D09 75%); border: 2px solid rgba(255,106,26,0.7); animation: cardWin 1.4s ease-in-out 1.6s infinite">
<div style="position: absolute; top: 14px; left: 14px; right: 14px; display: flex; align-items: center; justify-content: space-between">
<span style="display: flex; align-items: center; gap: 8px"><img src="{LOGO}" alt="" style="width: 30px; height: 30px"><span style="font-size: 15px; font-weight: 700">Tu anuncio</span></span>
<span style="{MONO}; font-size: 11px; letter-spacing: 0.1em; color: #FFB27A">PUBLICIDAD</span></div>
<div style="position: absolute; left: 50%; top: 42%; width: 74px; height: 74px; margin: -37px 0 0 -37px; border-radius: 99px; background: rgba(255,106,26,0.9); display: flex; align-items: center; justify-content: center; animation: playPulse 1.2s ease-in-out infinite">{ic("play", 34, "#0A0908", 2, "fill: #0A0908; margin-left: 5px")}</div>
<div style="position: absolute; left: 16px; right: 16px; bottom: 34px; {BRIC}; font-size: 30px; line-height: 1.02; letter-spacing: -0.03em; text-shadow: 0 4px 18px rgba(0,0,0,.8)">{hw}</div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 7px; background: rgba(242,237,231,0.14)"><div style="height: 100%; width: 100%; background: #FF6A1A; box-shadow: 0 0 14px #FF6A1A; animation: fillW 2.4s linear 1.6s both"></div></div>
</div>'''
feed = grey_post() + grey_post() + grey_post() + ad_card + grey_post()

S1 = f'''{h_static("Tu anuncio se juega", "en los primeros segundos.", 96)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; gap: 30px; align-items: stretch; animation: fxFloat 4s ease-in-out infinite">
{SHIM}
<div style="position: relative; flex: none; width: 340px; height: 590px; border-radius: 46px; background: radial-gradient(circle at 50% 0%, #2A160B, #0A0908 70%); border: 3px solid rgba(242,237,231,0.16); box-shadow: inset 0 0 0 8px #12100F, 0 40px 100px -30px rgba(0,0,0,.9); overflow: hidden">
<div style="position: absolute; top: 14px; left: 50%; margin-left: -45px; width: 90px; height: 24px; border-radius: 99px; background: #1E1A17; z-index: 3"></div>
<div style="position: absolute; top: 56px; left: 18px; right: 18px; display: flex; flex-direction: column; gap: 16px; animation: feedScroll 1.6s cubic-bezier(.45,.05,.2,1) 0s both">{feed}</div>
<span style="position: absolute; right: 40px; bottom: 90px; z-index: 4; animation: swipeUp .5s ease-out 0s 3 both">{ic("tap", 62, "#F2EDE7", 2, "filter: drop-shadow(0 6px 10px rgba(0,0,0,.8)); fill: rgba(10,9,8,.85)")}</span>
<span style="position: absolute; left: 50%; bottom: 14px; margin-left: -60px; width: 120px; height: 6px; border-radius: 99px; background: rgba(242,237,231,0.4); z-index: 3"></span>
</div>
<div style="position: relative; flex: 1; display: flex; flex-direction: column; align-items: center; gap: 26px">
<div style="align-self: stretch; display: flex; align-items: center; justify-content: space-between"><span style="{LBL}">EL SCROLL</span>{EJ}</div>
<div style="position: relative; width: 280px; height: 280px; margin-top: 8px">
<svg width="280" height="280" viewBox="0 0 280 280" aria-hidden="true" style="position: absolute; inset: 0; transform: rotate(-90deg)"><circle cx="140" cy="140" r="120" fill="none" stroke="rgba(242,237,231,0.1)" stroke-width="14"/><circle cx="140" cy="140" r="120" fill="none" stroke="#FF6A1A" stroke-width="14" stroke-linecap="round" stroke-dasharray="754" style="animation: sweep 4s linear both; filter: drop-shadow(0 0 12px rgba(255,106,26,.8))"/></svg>
<span style="position: absolute; inset: 22px; border-radius: 99px; border: 2px dashed rgba(242,237,231,0.12); animation: spinSlow 8s linear infinite"></span>
<div style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center">
<span style="{BRIC}; font-size: 120px; line-height: 0.9; letter-spacing: -0.05em; display: flex; align-items: baseline"><span class="tc"></span><span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; font-size: 64px; color: #FF6A1A; margin-left: 6px">s</span></span>
<span style="{MONO}; font-size: 14px; letter-spacing: 0.14em; color: #9C938B">PARA CONVENCER</span>
</div></div>
<div style="position: relative; width: 420px; height: 76px; border-radius: 20px; border: 1px solid rgba(242,237,231,0.12); background: rgba(242,237,231,0.03)">
{fade_seq([("PASA DE LARGO…", 0, 1.55, "#9C938B"), ("SE PARA A VERLO", 1.65, None, "#FF6A1A")]).replace("font-size: 40px", "font-size: 34px")}
</div>
<span style="{MONO}; font-size: 15px; letter-spacing: 0.12em; color: #9C938B; text-align: center; line-height: 1.5">SI EL GANCHO NO FRENA<br>EL DEDO, NADIE OYE EL RESTO</span>
</div>
</div>
{sub("Lo que dices al empezar decide si te escuchan.")}'''

# ---------- 02 PROBLEMA: empezar hablando de ti ----------
lines = ['Hola, somos Reformas López.', 'Llevamos años en el sector.', 'Somos líderes en calidad.', 'Tenemos el mejor equipo.']
lrows = ''
for i, t in enumerate(lines):
    d = 0.3 + i * 0.7
    lrows += (f'<div style="position: relative; display: flex; align-items: center; gap: 14px; padding: 14px 18px; border-radius: 16px; background: rgba(242,237,231,0.03); border: 1px solid rgba(242,237,231,0.08)">'
              f'<span style="{MONO}; font-size: 15px; color: #6B635C">0{i+1}</span>'
              f'<span style="position: relative; font-size: 27px; font-weight: 600; animation: dimLine .4s ease-out {d+0.55:.2f}s both"><span style="display: block; white-space: nowrap; animation: typeC .45s steps(24,end) {d:.2f}s both">{t}</span>'
              f'<span style="position: absolute; left: 0; top: 52%; height: 3px; background: #FF6A1A; border-radius: 99px; box-shadow: 0 0 10px rgba(255,106,26,.8); animation: strikeW .3s ease-out {d+0.55:.2f}s both"></span></span></div>')
flyers = ''
for i in range(4):
    flyers += f'<div style="position: absolute; left: 0; right: 0; top: 0; animation: flyUp 2.0s linear {-(i*0.5):.2f}s infinite">{grey_post(105)}</div>'

S2 = f'''{headline("Si hablas de ti,", "pasan de largo.", 104)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; gap: 28px; {TILT}">
<div style="flex: 1; display: flex; flex-direction: column; gap: 14px">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("pen", 22, "#9C938B", 2.2)}GUION TÍPICO</span>{EJ}</div>
{lrows}
<div style="margin-top: 6px; display: flex; align-items: center; gap: 12px; padding: 14px 18px; border-radius: 16px; background: rgba(242,237,231,0.95); color: #0A0908; animation: drop .6s cubic-bezier(.2,.8,.2,1) 3.1s both">{ic("x", 24, "#C84A0C", 3)}<span style="font-size: 21px; font-weight: 700">Todo sobre ti. Nada sobre él.</span></div>
</div>
<div style="flex: none; width: 250px; display: flex; flex-direction: column; align-items: center; gap: 14px">
<span style="{LBL}">SU FEED</span>
<div style="position: relative; width: 230px; height: 400px; border-radius: 28px; border: 2px solid rgba(242,237,231,0.14); overflow: hidden; padding: 0 12px; box-sizing: border-box">
<div style="position: relative; height: 100%">{flyers}</div>
<span style="position: absolute; right: 18px; bottom: 40px; animation: swipeUp .55s ease-out 0s infinite">{ic("tap", 50, "#F2EDE7", 2, "filter: drop-shadow(0 6px 10px rgba(0,0,0,.8)); fill: rgba(10,9,8,.85)")}</span>
</div>
<div style="padding: 10px 18px; border-radius: 12px; border: 3px solid #B5ADA4; color: #D9D1C8; {BRIC}; font-size: 28px; transform: rotate(-6deg); animation: stamp .5s cubic-bezier(.2,.8,.2,1) 2.9s both">SALTADO</div>
</div>
</div>
{sub("Al cliente le importa su problema, no tu empresa.")}'''

# ---------- 03 IDEA: las 4 partes del guion, línea de tiempo con cabezal ----------
parts = ['GANCHO', 'PROBLEMA', 'PRUEBA', 'QUÉ HACER']
segs = ''.join(f'<div style="height: 18px; border-radius: 99px; background: rgba(242,237,231,0.1); overflow: hidden"><div style="height: 100%; width: 100%; border-radius: 99px; background: linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A); box-shadow: 0 0 22px -2px rgba(255,106,26,.8); animation: fillW 1s linear {i*1.0:.2f}s both"></div></div>' for i in range(4))
labels = ''.join(
    f'<div style="display: flex; align-items: center; gap: 10px"><span style="flex: none; width: 34px; height: 34px; border-radius: 99px; background: rgba(242,237,231,0.08); display: flex; align-items: center; justify-content: center; {MONO}; font-size: 16px; font-weight: 600; animation: numOn .3s ease-out {i*1.0:.2f}s both">{i+1}</span>'
    f'<span style="{MONO}; font-size: 15px; letter-spacing: 0.08em; color: #D9D1C8">{p}</span></div>' for i, p in enumerate(parts))
subs = fade_seq([
    ('«¿Tu cocina se ha quedado vieja?»', 0, 0.95, '#F2EDE7'),
    ('«Reformar da miedo: obras, plazos…»', 1.0, 1.95, '#F2EDE7'),
    ('«Mira este antes y después.»', 2.0, 2.95, '#F2EDE7'),
    ('«Pide tu presupuesto aquí abajo.»', 3.0, None, '#FF6A1A'),
]).replace('font-size: 40px', 'font-size: 40px')

S3 = f'''{headline("Un guion que vende", "tiene 4 partes.", 100)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; flex-direction: column; gap: 24px; {TILT}">
{SHIM}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("video", 22, "#9C938B", 2.2)}TU VÍDEO, PARTE A PARTE</span>{EJ}</div>
<div style="position: relative; height: 300px; border-radius: 24px; overflow: hidden; background: radial-gradient(circle at 25% 30%, #3A1C0B, #120C09 70%); border: 1px solid rgba(255,106,26,0.35)">
<div style="position: absolute; left: 30px; top: 26px; width: 64px; height: 64px; border-radius: 99px; background: rgba(255,106,26,0.9); display: flex; align-items: center; justify-content: center; animation: playPulse 1.2s ease-in-out infinite">{ic("play", 28, "#0A0908", 2, "fill: #0A0908; margin-left: 4px")}</div>
<div style="position: absolute; right: 30px; top: 34px">{wavebars(14, 50, 7, 5)}</div>
<div style="position: absolute; left: 30px; right: 30px; top: 120px; height: 120px">{subs}</div>
</div>
<div style="position: relative; padding-top: 10px">
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px">{segs}</div>
<div style="position: absolute; top: 0; bottom: -8px; left: 0; right: 0; pointer-events: none"><div style="position: absolute; top: 0; bottom: 0; width: 4px; margin-left: -2px; border-radius: 99px; background: #F2EDE7; box-shadow: 0 0 16px #FF6A1A; animation: headX 4s linear both"></div></div>
</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px">{labels}</div>
</div>
{sub("Una idea por parte. Frases cortas, como hablas tú.")}'''

# ---------- 04 SOLUCIÓN: cierra diciendo qué hacer → toque → lead en el CRM ----------
S4 = f'''{headline("Termina diciendo", "qué tiene que hacer.", 98)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; gap: 28px; align-items: stretch; {TILT}">
<div style="position: relative; flex: none; width: 320px; height: 560px; border-radius: 44px; background: radial-gradient(circle at 50% 10%, #3A1C0B, #0A0908 70%); border: 3px solid rgba(242,237,231,0.16); box-shadow: inset 0 0 0 8px #12100F; overflow: hidden">
<div style="position: absolute; top: 14px; left: 50%; margin-left: -42px; width: 84px; height: 22px; border-radius: 99px; background: #1E1A17"></div>
<div style="position: absolute; top: 60px; left: 22px; right: 22px; display: flex; flex-direction: column; gap: 14px">
<span style="{MONO}; font-size: 12px; letter-spacing: 0.12em; color: #FFB27A">FINAL DEL ANUNCIO</span>
<div style="height: 170px; border-radius: 18px; background: linear-gradient(160deg, rgba(255,106,26,0.25), rgba(242,237,231,0.04)); display: flex; align-items: center; justify-content: center">{wavebars(12, 60, 7, 6)}</div>
<span style="{BRIC}; font-size: 30px; line-height: 1.02; letter-spacing: -0.03em">¿Cuánto costaría tu cocina?</span>
<span style="font-size: 19px; color: #B5ADA4">Pide tu presupuesto. Te llamamos hoy.</span>
</div>
<div style="position: absolute; left: 22px; right: 22px; bottom: 56px">
<div style="height: 66px; border-radius: 16px; background: #FF6A1A; color: #0A0908; font-weight: 700; font-size: 23px; display: flex; align-items: center; justify-content: center; gap: 10px; animation: btnPulse 1.1s ease-in-out infinite, press .25s ease-in-out 1.45s both">Pedir presupuesto{ic("arrow", 22, "#0A0908", 2.8)}</div>
<span style="position: absolute; left: 50%; top: 50%; width: 120px; height: 120px; margin: -60px 0 0 -60px; border-radius: 99px; border: 3px solid #FFB27A; animation: ripple .8s ease-out 1.5s both"></span>
{cursor("left: 62%; top: 26px; animation: cur4 1.1s cubic-bezier(.4,0,.2,1) .25s both")}
</div>
<span style="position: absolute; left: 50%; bottom: 14px; margin-left: -56px; width: 112px; height: 6px; border-radius: 99px; background: rgba(242,237,231,0.4)"></span>
</div>
<div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="{LBL}">TU CRM</span>{EJ}</div>
<div style="display: flex; align-items: center; gap: 14px; padding: 18px; border-radius: 20px; background: rgba(242,237,231,0.95); color: #0A0908; animation: drop .6s cubic-bezier(.2,.8,.2,1) 1.9s both">
<span style="flex: none; width: 50px; height: 50px; border-radius: 14px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; animation: bellShake 1.2s ease-in-out 2.4s infinite">{ic("bell", 28, "#0A0908", 2.4)}</span>
<div style="display: flex; flex-direction: column"><span style="font-size: 23px; font-weight: 700">Nuevo lead</span><span style="font-size: 17px; color: #4A4540">Pidió presupuesto desde el anuncio</span></div></div>
<div style="padding: 20px; border-radius: 20px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); display: flex; flex-direction: column; gap: 16px; animation: aIn .6s cubic-bezier(.2,.8,.2,1) 2.3s both">
<div style="display: flex; align-items: center; gap: 14px"><span style="flex: none; width: 50px; height: 50px; border-radius: 99px; background: linear-gradient(160deg,#FF8F45,#C84A0C); display: flex; align-items: center; justify-content: center; {BRIC}; font-size: 22px; color: #0A0908">M</span>
<div style="display: flex; flex-direction: column"><span style="font-size: 23px; font-weight: 700">Marta G.</span><span style="{MONO}; font-size: 13px; letter-spacing: 0.1em; color: #FFB27A">QUIERE PRESUPUESTO</span></div></div>
<div style="position: relative; height: 4px; margin: 18px 12px 6px; border-radius: 99px; background: rgba(242,237,231,0.12)">
<span style="position: absolute; left: 0; top: -9px; width: 22px; height: 22px; margin-left: -11px; border-radius: 99px; background: #FF6A1A"></span>
<span style="position: absolute; left: 50%; top: -9px; width: 22px; height: 22px; margin-left: -11px; border-radius: 99px; background: #2A2420; border: 2px solid rgba(255,106,26,0.6); box-sizing: border-box"></span>
<span style="position: absolute; left: 100%; top: -9px; width: 22px; height: 22px; margin-left: -11px; border-radius: 99px; background: #2A2420; border: 2px solid rgba(255,106,26,0.6); box-sizing: border-box"></span>
<span style="position: absolute; top: -6px; width: 16px; height: 16px; margin-left: -8px; border-radius: 99px; background: #FFB27A; box-shadow: 0 0 18px #FF6A1A, 0 0 6px #fff; animation: dotRun 1.6s ease-in-out 2.4s infinite both"></span>
</div>
<div style="display: flex; justify-content: space-between; {MONO}; font-size: 13px; letter-spacing: 0.08em; color: #9C938B"><span>NUEVO</span><span>LLAMAR</span><span>CITA</span></div>
</div>
<div style="display: flex; align-items: center; gap: 14px; padding: 18px 20px; border-radius: 20px; border: 1px solid rgba(255,106,26,0.5); background: rgba(255,106,26,0.08); animation: aIn .6s cubic-bezier(.2,.8,.2,1) 2.8s both, glowPulse 1.6s ease-in-out 3.2s infinite">
<span style="flex: none; width: 46px; height: 46px; border-radius: 12px; background: rgba(255,106,26,0.18); display: flex; align-items: center; justify-content: center">{ic("phone", 26, "#FF6A1A", 2.2)}</span>
<div style="flex: 1; display: flex; flex-direction: column"><span style="font-size: 22px; font-weight: 700">Siguiente paso: llamarla</span><span style="{MONO}; font-size: 13px; letter-spacing: 0.1em; color: #9C938B">TAREA CREADA</span></div>
<span style="padding: 8px 14px; border-radius: 99px; background: #FF6A1A; color: #0A0908; {MONO}; font-size: 15px; font-weight: 600; letter-spacing: 0.08em; animation: pulseDot 1.2s ease-in-out 3.2s infinite">HOY</span></div>
</div>
</div>
{sub("Un solo paso y claro: pedir, reservar o escribir.")}'''

# ---------- 05 CTA: checklist + Síguenos ----------
checks = [('target', 'Gancho en el primer segundo'), ('user', 'Su problema, no tu empresa'), ('ok', 'Una prueba: antes y después'), ('arrow', 'Dile qué tiene que hacer')]
crows = ''
for i, (icn, t) in enumerate(checks):
    d = 0.5 + i * 0.45
    crows += (f'<div style="display: flex; align-items: center; gap: 18px; padding: 14px 20px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); animation: rowOn .5s ease-out {d:.2f}s both">'
              f'<span style="flex: none; width: 42px; height: 42px; border-radius: 12px; border: 2px solid rgba(242,237,231,0.25); display: flex; align-items: center; justify-content: center; animation: check .45s ease-out {d:.2f}s both">{ic("ok", 26, "#0A0908", 3.4)}</span>'
              f'<span style="flex: 1; font-size: 28px; font-weight: 600; text-align: left">{t}</span>{ic(icn, 30, "#FF6A1A", 2.2)}</div>')

S5 = f'''<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0 0 36px; {BRIC}; font-size: 80px; line-height: 1; letter-spacing: -0.045em; animation: aIn .8s cubic-bezier(.2,.8,.2,1) .1s both">Tu guion, <span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">listo.</span></p>
<div style="position: relative; width: 900px; box-sizing: border-box; padding: 26px; {CARD}; display: flex; flex-direction: column; gap: 12px; {TILT}">
{SHIM}
<span style="{LBL}; text-align: left">CHECKLIST ANTES DE GRABAR</span>
{crows}
</div>
<div style="position: relative; margin-top: 60px; animation: pop .7s cubic-bezier(.2,.8,.2,1) 2.3s both"><div style="animation: wob 4s ease-in-out infinite">
<div style="position: relative; overflow: hidden; padding: 30px 60px; border-radius: 34px; background: #FF6A1A; color: #0A0908; {BRIC}; font-size: 100px; line-height: 0.9; letter-spacing: -0.05em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 2s ease-in-out infinite">Síguenos<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.35), rgba(255,255,255,0)); animation: aShim 2s ease-in-out infinite"></div></div>
</div></div>
<p style="margin: 32px 0 0; font-family: 'Instrument Serif', serif; font-style: italic; font-size: 56px; line-height: 1.05; animation: aIn .8s cubic-bezier(.2,.8,.2,1) 2.6s both">para más tips de captación y ventas.</p>
</div>'''

for n, name, mid, title in [(1, 'Main', S1, '01'), (2, 'S2', S2, '02'), (3, 'S3', S3, '03'), (4, 'S4', S4, '04'), (5, 'S5', S5, '05')]:
    open(os.path.join(SRC, f'{name}.dc.html'), 'w').write(page(n, mid, title))
print('ok')
