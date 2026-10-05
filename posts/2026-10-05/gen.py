#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel 2026-10-05 (valor: errores típicos al grabar anuncios con el móvil)."""
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

# ---------- 01 GANCHO: visor de cámara que tiembla, contraluz y avisos ----------
warns = [('warn', 'TIEMBLA', 'Móvil en la mano'), ('sun', 'CONTRALUZ', 'Cara a oscuras'), ('mic', 'ECO', 'No se te entiende')]
wrows = ''
for i, (icn, t, s) in enumerate(warns):
    d = -0.6 + i * 0.6
    wrows += (f'<div style="display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 18px; border: 1px solid rgba(255,106,26,0.45); background: rgba(255,106,26,0.07); animation: warnIn .5s cubic-bezier(.2,.8,.2,1) {d:.2f}s both, warnGlow 1.4s ease-in-out {d+0.5:.2f}s infinite">'
              f'<span style="flex: none; width: 50px; height: 50px; border-radius: 14px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; animation: bellShake 1.4s ease-in-out {d+0.4:.2f}s infinite">{ic(icn, 28, "#0A0908", 2.4)}</span>'
              f'<div style="display: flex; flex-direction: column; gap: 2px"><span style="{MONO}; font-size: 19px; font-weight: 600; letter-spacing: 0.1em; color: #FFB27A">{t}</span><span style="font-size: 19px; color: #B5ADA4">{s}</span></div></div>')

S1 = f'''{h_static("Grabas con el móvil", "y se nota.", 92)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; gap: 30px; align-items: stretch; animation: fxFloat 4s ease-in-out infinite">
{SHIM}
<div style="position: relative; flex: none; width: 340px; height: 590px; border-radius: 46px; background: #0A0908; border: 3px solid rgba(242,237,231,0.16); box-shadow: inset 0 0 0 8px #12100F, 0 40px 100px -30px rgba(0,0,0,.9); overflow: hidden">
<div style="position: absolute; inset: 12px; border-radius: 36px; overflow: hidden">
<div style="position: absolute; inset: -24px; animation: camShake .55s linear infinite">
<div style="position: absolute; inset: 0; background: {WINDOW_BG}; animation: flare 1.6s ease-in-out infinite"></div>
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -150px; filter: blur(1.5px)">{person('#0E0B09', 300)}</div>
</div>
{thirds()}
{rec(22, 20)}
<span style="position: absolute; z-index: 3; left: 50%; top: 34%; width: 110px; height: 110px; margin: -55px 0 0 -55px; border: 3px solid #FFB27A; border-radius: 14px; animation: focusP .9s ease-in-out infinite"></span>
<div style="position: absolute; z-index: 4; left: 0; right: 0; bottom: 22px; display: flex; justify-content: center"><span style="width: 74px; height: 74px; border-radius: 99px; border: 5px solid #F2EDE7; box-sizing: border-box; display: flex; align-items: center; justify-content: center"><span style="width: 52px; height: 52px; border-radius: 99px; background: #FF3B1A; animation: aBlink 1s ease-in-out infinite"></span></span></div>
</div>
<div style="position: absolute; top: 18px; left: 50%; margin-left: -45px; width: 90px; height: 24px; border-radius: 99px; background: #1E1A17; z-index: 5"></div>
</div>
<div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 16px">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("cam", 22, "#9C938B", 2.2)}LO QUE SE VE</span>{EJ}</div>
{wrows}
<div style="margin-top: auto; padding: 16px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); display: flex; flex-direction: column; gap: 10px">
<span style="{MONO}; font-size: 14px; letter-spacing: 0.12em; color: #9C938B">AUDIO</span>
{jwave(18, 56, '#9C938B', 7, 6, 0.55)}
</div>
</div>
</div>
{sub("3 errores que hacen que tu anuncio parezca casero.")}'''

# ---------- 02 ERROR 1: grabar en horizontal ----------
S2 = f'''{headline("Error 1:", "grabar en horizontal.", 100)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; gap: 30px; align-items: center; {TILT}">
{SHIM}
<div style="position: relative; flex: 1; height: 560px; display: flex; flex-direction: column; align-items: center; gap: 18px">
<div style="align-self: stretch; display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("rotate", 22, "#9C938B", 2.2)}CÓMO LO GRABAS</span></div>
<div style="position: relative; flex: 1; width: 100%; display: flex; align-items: center; justify-content: center">
<span style="position: absolute; width: 380px; height: 380px; border-radius: 99px; border: 3px dashed rgba(255,106,26,0.35); animation: spinSlow 10s linear infinite"></span>
<span style="position: absolute; top: 18px; right: 30px; animation: arcSpin 4s cubic-bezier(.6,0,.3,1) both">{ic("rotate", 54, "#FF6A1A", 2.4, "filter: drop-shadow(0 0 10px rgba(255,106,26,.8))")}</span>
<div style="position: relative; width: 210px; height: 380px; border-radius: 34px; border: 3px solid rgba(242,237,231,0.2); background: #0A0908; box-shadow: inset 0 0 0 6px #12100F, 0 30px 80px -20px rgba(0,0,0,.9); overflow: hidden; animation: rotUp 4s cubic-bezier(.6,0,.3,1) both">
<div style="position: absolute; inset: 10px; border-radius: 26px; overflow: hidden; background: radial-gradient(circle at 50% 30%, #4A2412, #140D09 80%)">
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -110px">{person('#2A1A10', 220, True)}</div>
{rec(14, 12)}
</div></div>
</div>
</div>
<div style="flex: none; width: 2px; align-self: stretch; background: linear-gradient(180deg, transparent, rgba(242,237,231,0.14), transparent)"></div>
<div style="position: relative; flex: none; width: 330px; display: flex; flex-direction: column; align-items: center; gap: 18px">
<div style="align-self: stretch; display: flex; align-items: center; justify-content: space-between"><span style="{LBL}">CÓMO LO VE ÉL</span>{EJ}</div>
<div style="position: relative; width: 270px; height: 470px; border-radius: 38px; border: 3px solid rgba(242,237,231,0.16); background: #050404; box-shadow: inset 0 0 0 7px #12100F; overflow: hidden; display: flex; align-items: center; justify-content: center">
<div style="position: absolute; top: 12px; left: 50%; margin-left: -36px; width: 72px; height: 20px; border-radius: 99px; background: #1E1A17; z-index: 3"></div>
<div style="position: relative; width: 100%; overflow: hidden; background: radial-gradient(circle at 50% 30%, #4A2412, #140D09 80%); animation: vidGrow 4s cubic-bezier(.6,0,.3,1) both">
<div style="position: absolute; left: 50%; bottom: 0; margin-left: -80px">{person('#2A1A10', 160, True)}</div>
<div style="position: absolute; right: 12px; bottom: 16px">{wavebars(8, 34, 5, 4)}</div>
</div>
<span style="position: absolute; top: 60px; left: 0; right: 0; text-align: center; {MONO}; font-size: 15px; letter-spacing: 0.12em; color: #6B635C; animation: barsOut 4s linear both">BANDA NEGRA</span>
<span style="position: absolute; bottom: 60px; left: 0; right: 0; text-align: center; {MONO}; font-size: 15px; letter-spacing: 0.12em; color: #6B635C; animation: barsOut 4s linear both">BANDA NEGRA</span>
</div>
<div style="position: relative; width: 300px; height: 64px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.12); background: rgba(242,237,231,0.03)">
{fade_seq([("SE VE PEQUEÑO", 0, 1.9, "#9C938B"), ("PANTALLA ENTERA", 2.1, None, "#FF6A1A")]).replace("font-size: 40px", "font-size: 28px")}
</div>
</div>
</div>
{sub("En el móvil se ve en vertical: graba en 9:16.")}'''

# ---------- 03 ERROR 2: contraluz → antes / después con barrido ----------
S3 = f'''{headline("Error 2:", "la luz a tu espalda.", 100)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; flex-direction: column; gap: 22px; {TILT}">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("sun", 22, "#9C938B", 2.2)}ANTES / DESPUÉS</span>{EJ}</div>
<div style="position: relative; height: 420px; border-radius: 24px; overflow: hidden; border: 1px solid rgba(242,237,231,0.12)">
<div style="position: absolute; inset: 0; background: {WINDOW_BG}; animation: flare 1.8s ease-in-out infinite"></div>
<div style="position: absolute; left: 50%; bottom: -10px; margin-left: -160px">{person('#0E0B09', 320)}</div>
<span style="position: absolute; top: 18px; left: 18px; padding: 8px 14px; border-radius: 99px; background: rgba(10,9,8,0.75); {MONO}; font-size: 16px; letter-spacing: 0.12em; color: #F2EDE7">ANTES · VENTANA DETRÁS</span>
<div style="position: absolute; inset: 0; animation: wipe 4s cubic-bezier(.5,0,.3,1) both">
<div style="position: absolute; inset: 0; background: radial-gradient(circle at 50% 40%, #6A3A1E 0%, #2A1A10 55%, #120C09 100%)"></div>
<div style="position: absolute; inset: 0; background: linear-gradient(100deg, rgba(255,214,170,0.35), rgba(255,214,170,0) 55%)"></div>
<div style="position: absolute; left: 50%; bottom: -10px; margin-left: -160px">{person('#2A1A10', 320, True)}</div>
<span style="position: absolute; top: 18px; right: 18px; padding: 8px 14px; border-radius: 99px; background: #FF6A1A; {MONO}; font-size: 16px; font-weight: 600; letter-spacing: 0.12em; color: #0A0908">DESPUÉS · DE CARA A LA LUZ</span>
</div>
<div style="position: absolute; top: 0; bottom: 0; width: 4px; margin-left: -2px; background: #F2EDE7; box-shadow: 0 0 20px #FF6A1A; animation: wipeH 4s cubic-bezier(.5,0,.3,1) both">
<span style="position: absolute; top: 50%; left: 50%; width: 56px; height: 56px; margin: -28px 0 0 -28px; border-radius: 99px; background: #F2EDE7; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 30px rgba(255,106,26,.9)">{ic("arrow", 28, "#0A0908", 2.8)}</span></div>
</div>
<div style="position: relative; height: 86px; border-radius: 20px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03)">
<span style="position: absolute; top: 50%; margin: -26px 0 0 -26px; animation: sunMove 4s cubic-bezier(.5,0,.3,1) both">{ic("sun", 52, "#FFB27A", 2.4, "animation: spinSlow 6s linear infinite; filter: drop-shadow(0 0 12px rgba(255,178,122,.9))")}</span>
<span style="position: absolute; left: 50%; top: 50%; margin: -27px 0 0 -27px; width: 54px; height: 54px; border-radius: 99px; background: rgba(255,106,26,0.18); display: flex; align-items: center; justify-content: center"><span style="display: flex; animation: turn 4s cubic-bezier(.5,0,.3,1) both">{ic("user", 30, "#FF6A1A", 2.4)}</span></span>
<span style="position: absolute; right: 26px; top: 50%; margin-top: -11px; {MONO}; font-size: 16px; letter-spacing: 0.1em; color: #9C938B">MÓVIL</span>
</div>
</div>
{sub("Ponte de cara a la ventana: la luz, delante de ti.")}'''

# ---------- 04 ERROR 3: el audio ----------
echoes = ''.join(f'<span style="position: absolute; left: 50%; top: 50%; width: 120px; height: 120px; margin: -60px 0 0 -60px; border-radius: 99px; border: 2px solid rgba(181,173,164,0.5); animation: echo 1.4s ease-out {-(i*0.47):.2f}s infinite"></span>' for i in range(3))
S4 = f'''{headline("Error 3:", "que no se te oiga bien.", 92)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 30px; {CARD}; display: flex; flex-direction: column; gap: 22px; {TILT}">
{SHIM}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("mic", 22, "#9C938B", 2.2)}TU AUDIO</span>{EJ}</div>
<div style="position: relative; height: 190px; border-radius: 22px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03)">
<div style="position: absolute; left: 36px; top: 50%; margin-top: -60px; width: 120px; height: 120px; border-radius: 99px; background: linear-gradient(160deg,#FF8F45,#C84A0C); display: flex; align-items: center; justify-content: center">{ic("user", 60, "#0A0908", 2.4)}
<div style="position: absolute; inset: 0; animation: echoStop 4s linear both">{echoes}</div></div>
<div style="position: absolute; right: 50px; top: 50%; margin-top: -42px; width: 84px; height: 84px; border-radius: 99px; background: #F2EDE7; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 40px rgba(255,106,26,.7); animation: micGo 4s cubic-bezier(.6,0,.3,1) both">{ic("mic", 44, "#0A0908", 2.4)}</div>
<span style="position: absolute; left: 180px; right: 160px; top: 50%; height: 2px; border-top: 3px dashed rgba(242,237,231,0.18); animation: noisyOut 4s linear both"></span>
<span style="position: absolute; left: 0; right: 0; bottom: 14px; display: flex; justify-content: space-between; padding: 0 30px; {MONO}; font-size: 14px; letter-spacing: 0.12em; color: #6B635C"><span>TÚ</span><span>MICRO</span></span>
</div>
<div style="position: relative; height: 130px; border-radius: 22px; border: 1px solid rgba(242,237,231,0.1); background: rgba(10,9,8,0.6); overflow: hidden">
<div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; animation: noisyOut 4s linear both">{jwave(46, 96, '#6B635C', 8, 8, 0.35)}</div>
<div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; animation: cleanIn 4s linear both">{wavebars(46, 96, 8, 8, '#FF6A1A', 1.1)}</div>
</div>
<div style="display: flex; align-items: center; gap: 18px">
<span style="{MONO}; font-size: 15px; letter-spacing: 0.12em; color: #9C938B">NIVEL</span>
<div style="flex: 1; height: 16px; border-radius: 99px; background: rgba(242,237,231,0.1); overflow: hidden"><div style="height: 100%; border-radius: 99px; box-shadow: 0 0 20px rgba(255,106,26,.7); animation: lvl 4s cubic-bezier(.6,0,.3,1) both"></div></div>
<div style="position: relative; width: 330px; height: 56px; border-radius: 16px; border: 1px solid rgba(242,237,231,0.12); background: rgba(242,237,231,0.03)">
{fade_seq([("LEJOS: ECO Y RUIDO", 0, 2.0, "#9C938B"), ("CERCA: SE OYE CLARO", 2.2, None, "#FF6A1A")]).replace("font-size: 40px", "font-size: 24px")}
</div></div>
</div>
{sub("Micro de solapa o el móvil cerca, en un sitio sin eco.")}'''

# ---------- 05 CTA: checklist + Síguenos ----------
checks = [('rotate', 'Móvil en vertical'), ('sun', 'De cara a la luz'), ('mic', 'Micro cerca, sin eco'), ('cam', 'Móvil fijo, mira a la lente')]
crows = ''
for i, (icn, t) in enumerate(checks):
    d = 0.5 + i * 0.45
    crows += (f'<div style="display: flex; align-items: center; gap: 18px; padding: 14px 20px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); animation: rowOn .5s ease-out {d:.2f}s both">'
              f'<span style="flex: none; width: 42px; height: 42px; border-radius: 12px; border: 2px solid rgba(242,237,231,0.25); display: flex; align-items: center; justify-content: center; animation: check .45s ease-out {d:.2f}s both">{ic("ok", 26, "#0A0908", 3.4)}</span>'
              f'<span style="flex: 1; font-size: 28px; font-weight: 600; text-align: left">{t}</span>{ic(icn, 30, "#FF6A1A", 2.2)}</div>')

S5 = f'''<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0 0 36px; {BRIC}; font-size: 80px; line-height: 1; letter-spacing: -0.045em; animation: aIn .8s cubic-bezier(.2,.8,.2,1) .1s both">Antes de grabar, <span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">revisa.</span></p>
<div style="position: relative; width: 900px; box-sizing: border-box; padding: 26px; {CARD}; display: flex; flex-direction: column; gap: 12px; {TILT}">
{SHIM}
<span style="{LBL}; text-align: left">CHECKLIST DE GRABACIÓN</span>
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
