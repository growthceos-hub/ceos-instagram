#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel 2026-10-07 (valor: cómo reactivar los leads dormidos del CRM)."""
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
# 2026-10-07 · VALOR · Cómo reactivar los leads dormidos del CRM
# =====================================================================
EXTRA += '''
@keyframes wake{0%{border-color:rgba(242,237,231,0.06);background:rgba(242,237,231,0.015)}40%{border-color:rgba(255,106,26,1);background:rgba(255,106,26,0.2);box-shadow:0 0 40px -6px rgba(255,106,26,.9)}100%{border-color:rgba(255,106,26,0.6);background:rgba(255,106,26,0.09);box-shadow:0 0 22px -10px rgba(255,106,26,.7)}}
@keyframes unGrey{from{filter:grayscale(1);opacity:.42}to{filter:none;opacity:1}}
@keyframes zFloat{0%{transform:translate(0,6px) scale(.7);opacity:0}30%{opacity:.9}100%{transform:translate(14px,-30px) scale(1.1);opacity:0}}
@keyframes heatUp{0%{width:8%;background:linear-gradient(90deg,#4A4540,#6B635C,#9C938B)}100%{width:100%;background:linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A);box-shadow:0 0 22px rgba(255,106,26,.8)}}
@keyframes scanY{0%{top:0%;opacity:0}6%{opacity:1}94%{opacity:1}100%{top:100%;opacity:0}}
@property --rp{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes rpc{from{--rp:0}to{--rp:4}}
.rp{counter-reset:rp var(--rp);animation:rpc 2.8s steps(4,end) .6s both}
.rp::after{content:counter(rp)}
@keyframes kMove{0%{transform:translate(0,0) rotate(0)}38%{transform:translate(566px,24px) rotate(4deg)}50%{transform:translate(566px,24px) rotate(4deg)}58%{transform:translate(540px,24px) rotate(-3deg)}80%,100%{transform:translate(283px,0) rotate(0)}}
@keyframes colFlash{0%,100%{border-color:rgba(242,237,231,0.08);background:rgba(242,237,231,0.02)}50%{border-color:rgba(255,106,26,0.6);background:rgba(255,106,26,0.06)}}
@keyframes colDim{to{opacity:.35}}
@keyframes noGo{0%{opacity:0;transform:scale(2)}60%{opacity:1;transform:scale(.9)}100%{opacity:1;transform:scale(1)}}
@keyframes sortDrop{0%{transform:translate(0,0) scale(.85);opacity:0}12%{opacity:1;transform:translate(0,10px) scale(1)}45%{transform:translate(calc(var(--tx) * .35),90px)}88%{opacity:1}100%{transform:translate(var(--tx),260px) scale(.7);opacity:0}}
@keyframes stackIn{0%{opacity:0;transform:translateY(-20px) scale(.6)}70%{transform:translateY(3px) scale(1.06)}100%{opacity:1;transform:none}}
@keyframes bucketHit{0%{box-shadow:0 0 0 0 rgba(255,106,26,0);border-color:rgba(242,237,231,0.12)}30%{box-shadow:0 0 44px -6px rgba(255,106,26,.95);border-color:rgba(255,106,26,1)}100%{box-shadow:0 0 0 0 rgba(255,106,26,0);border-color:rgba(255,106,26,0.4)}}
@keyframes segHi{0%{background:rgba(255,106,26,0)}30%,70%{background:rgba(255,106,26,0.28)}100%{background:rgba(255,106,26,0)}}
'''
ICON.update({
    'zz': '<path d="M4 6h6l-6 7h6M13 12h7l-7 8h7"/>',
    'tag': '<path d="M20.6 13.4L13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    'coin': '<circle cx="12" cy="12" r="9"/><path d="M15 9.5a3 3 0 0 0-3-1.5c-1.7 0-3 .9-3 2s1.3 1.7 3 2 3 .9 3 2-1.3 2-3 2a3 3 0 0 1-3-1.5M12 6v2M12 16v2"/>',
    'hand': '<path d="M18 11V6a2 2 0 0 0-4 0v5M14 10V4a2 2 0 0 0-4 0v6M10 10.5V6a2 2 0 0 0-4 0v8a8 8 0 0 0 16 0v-3a2 2 0 0 0-4 0"/>',
})

def zz(delay_out):
    s = ''
    for k in range(3):
        s += f'<span style="position: absolute; left: {k*10}px; bottom: 0; {BRIC}; font-size: {16+k*5}px; color: #9C938B; animation: zFloat 1.5s ease-out {-k*0.5:.2f}s infinite">z</span>'
    return f'<span style="position: relative; flex: none; width: 40px; height: 36px; animation: fadeOut .25s ease-in {delay_out:.2f}s forwards">{s}</span>'

# ---------- 01 GANCHO: CRM con leads dormidos que se despiertan ----------
leads = [('Laura P.', 'Hace 2 meses'), ('Javier R.', 'Hace 3 meses'), ('Ana M.', 'Hace 5 meses'), ('Diego S.', 'Hace 6 meses')]
lrow = ''
for i, (n, ago) in enumerate(leads):
    t = 0.7 + i * 0.75
    lrow += (f'<div style="position: relative; display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.06); background: rgba(242,237,231,0.015); animation: wake .9s ease-out {t:.2f}s both">'
             f'<span style="flex: none; width: 46px; height: 46px; border-radius: 99px; background: rgba(255,106,26,0.18); display: flex; align-items: center; justify-content: center; animation: unGrey .5s ease-out {t:.2f}s both">{ic("user", 24, "#FFB27A", 2.2)}</span>'
             f'<div style="flex: 1; display: flex; flex-direction: column; gap: 2px; animation: unGrey .5s ease-out {t:.2f}s both"><span style="font-size: 25px; font-weight: 700">{n}</span><span style="{MONO}; font-size: 14px; letter-spacing: 0.06em; color: #9C938B">{ago.upper()}</span></div>'
             f'{zz(t)}'
             f'<span style="position: relative; flex: none; width: 168px; height: 36px">'
             f'<span style="position: absolute; right: 0; top: 0; animation: fadeOut .2s ease-in {t:.2f}s forwards">{chip("DORMIDO", "#B5ADA4", "rgba(242,237,231,0.05)", "rgba(242,237,231,0.2)")}</span>'
             f'<span style="position: absolute; right: 0; top: 0; animation: pop .5s cubic-bezier(.2,.8,.2,1) {t:.2f}s both">{chip("RESPONDE ✓", "#0A0908", "#FF6A1A", "#FF6A1A", "box-shadow: 0 0 22px rgba(255,106,26,.8)")}</span>'
             f'</span></div>')

msgs = [('Laura P.', '¡Hola! Sí, sigo con la idea.'), ('Javier R.', 'Ahora sí me viene bien.'), ('Ana M.', '¿Me llamas mañana?')]
nstack = ''
for i, (n, m) in enumerate(msgs):
    t = 0.95 + i * 0.75
    nstack += (f'<div style="padding: 12px 14px; border-radius: 18px; background: rgba(40,35,31,0.95); border: 1px solid rgba(242,237,231,0.1); box-shadow: 0 20px 40px -18px rgba(0,0,0,.9); display: flex; flex-direction: column; gap: 4px; animation: notifDrop .5s cubic-bezier(.2,.8,.2,1) {t:.2f}s both">'
               f'<div style="display: flex; align-items: center; gap: 8px"><span style="width: 24px; height: 24px; border-radius: 7px; background: #FF6A1A; display: flex; align-items: center; justify-content: center">{ic("whats", 15, "#0A0908", 2.6)}</span><span style="{MONO}; font-size: 12px; letter-spacing: 0.08em; color: #B5ADA4">WHATSAPP</span><span style="margin-left: auto; font-size: 12px; color: #9C938B">ahora</span></div>'
               f'<span style="font-size: 17px; font-weight: 700">{n}</span><span style="font-size: 16px; color: #D9D1C8; line-height: 1.25">{m}</span></div>')

S1 = f'''{h_static("Tus leads viejos", "aún pueden comprar.", 98)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 26px; {CARD}; display: flex; gap: 22px; align-items: stretch; animation: fxFloat 4s ease-in-out infinite">
{SHIM}
<div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 12px">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("zz", 22, "#9C938B", 2.2)}LEADS DORMIDOS · CRM</span>{EJ}</div>
<div style="position: relative; display: flex; flex-direction: column; gap: 10px">
<span style="position: absolute; z-index: 3; left: -10px; right: -10px; height: 3px; border-radius: 99px; background: linear-gradient(90deg, rgba(255,106,26,0), #FFB27A, rgba(255,106,26,0)); box-shadow: 0 0 22px rgba(255,106,26,1); animation: scanY 3.2s linear .45s both"></span>
{lrow}
</div>
<div style="margin-top: auto; display: flex; align-items: center; gap: 14px; padding: 14px 18px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03)">
<span style="{MONO}; font-size: 15px; letter-spacing: 0.12em; color: #9C938B">ACTIVOS</span>
<div style="flex: 1; height: 12px; border-radius: 99px; background: rgba(242,237,231,0.08); overflow: hidden"><div style="height: 100%; border-radius: 99px; animation: heatUp 3.2s ease-in-out .5s both"></div></div>
</div>
</div>
<div style="position: relative; flex: none; width: 270px; border-radius: 26px; border: 1px solid rgba(242,237,231,0.1); background: radial-gradient(circle at 30% 0%, #3A1C0B, rgba(10,9,8,0.7) 70%); display: flex; flex-direction: column; gap: 10px; padding: 18px 14px; overflow: hidden">
<div style="display: flex; align-items: center; gap: 12px; padding: 4px 4px 8px">
<span style="position: relative; width: 52px; height: 52px; border-radius: 16px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 30px rgba(255,106,26,.7)"><span style="display: flex; animation: bellShake 1.2s ease-in-out infinite">{ic("bell", 28, "#0A0908", 2.4)}</span>
<span style="position: absolute; inset: 0; border-radius: 16px; border: 2px solid rgba(255,106,26,.7); animation: callRing 1.4s ease-out infinite"></span></span>
<div style="display: flex; flex-direction: column"><span style="{MONO}; font-size: 13px; letter-spacing: 0.1em; color: #B5ADA4">RESPUESTAS</span><span style="{BRIC}; font-size: 44px; line-height: 1; letter-spacing: -0.03em; color: #FFB27A" class="rp"></span></div>
</div>
{nstack}
</div>
</div>
{sub("Cómo reactivar los leads que se quedaron dormidos en tu CRM.")}'''

# ---------- 02 "Ahora no" no es "no": tablero que casi lo tira a PERDIDO ----------
def col(title, flash='', extra=''):
    ph = ''.join(f'<div style="height: 64px; border-radius: 14px; background: rgba(242,237,231,0.04); border: 1px solid rgba(242,237,231,0.06)"></div>' for _ in range(2))
    return (f'<div style="position: relative; flex: 1; height: 440px; box-sizing: border-box; padding: 14px; border-radius: 22px; border: 1px solid rgba(242,237,231,0.08); background: rgba(242,237,231,0.02); display: flex; flex-direction: column; gap: 12px; {flash}">'
            f'<span style="{MONO}; font-size: 15px; letter-spacing: 0.12em; color: #B5ADA4; {extra}">{title}</span>'
            f'<div style="margin-top: auto; display: flex; flex-direction: column; gap: 10px">{ph}</div></div>')

kcard = f'''<div style="position: absolute; z-index: 4; left: 14px; top: 104px; width: 252px; animation: kMove 3.1s cubic-bezier(.45,.05,.3,1) .45s both">
<div style="position: relative; box-sizing: border-box; padding: 16px; border-radius: 18px; background: #24201C; border: 1px solid rgba(255,106,26,0.5); box-shadow: 0 30px 60px -20px rgba(0,0,0,.95); display: flex; flex-direction: column; gap: 10px; animation: glowPulse 1.3s ease-in-out 3.4s infinite">
<div style="display: flex; align-items: center; gap: 10px"><span style="width: 38px; height: 38px; border-radius: 99px; background: rgba(255,106,26,0.2); display: flex; align-items: center; justify-content: center">{ic("user", 20, "#FFB27A", 2.2)}</span><span style="font-size: 22px; font-weight: 700">Javier R.</span></div>
<span style="font-family: 'Instrument Serif', serif; font-style: italic; font-size: 24px; line-height: 1.1; color: #D9D1C8">«Ahora no me viene bien»</span>
<span style="position: relative; height: 34px">
<span style="position: absolute; left: 0; top: 0; animation: fadeOut .2s ease-in 2.75s forwards">{chip("AHORA NO", "#B5ADA4", "rgba(242,237,231,0.05)", "rgba(242,237,231,0.2)")}</span>
<span style="position: absolute; left: 0; top: 0; animation: pop .5s cubic-bezier(.2,.8,.2,1) 2.75s both">{chip("VOLVER A LLAMAR", "#0A0908", "#FF6A1A", "#FF6A1A", "box-shadow: 0 0 22px rgba(255,106,26,.8)")}</span>
</span>
</div>
</div>'''

kcursor = f'<span style="position: absolute; z-index: 6; left: 210px; top: 190px; animation: kMove 3.1s cubic-bezier(.45,.05,.3,1) .45s both, fadeOut .3s ease-in 3.2s forwards">{ic("hand", 50, "#F2EDE7", 2, "filter: drop-shadow(0 6px 12px rgba(0,0,0,.8)); fill: rgba(10,9,8,.6)")}</span>'

nogo = f'<span style="position: absolute; z-index: 7; right: 70px; top: 40px; width: 120px; height: 120px; border-radius: 99px; background: rgba(10,9,8,.85); border: 4px solid #FF6A1A; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 40px rgba(255,106,26,.8); opacity: 0; animation: noGo .4s cubic-bezier(.2,.8,.2,1) 1.6s both, fadeOut .3s ease-in 2.4s forwards">{ic("x", 64, "#FF6A1A", 3)}</span>'

S2 = f'''{headline("Un «ahora no»", "no es un no.", 104)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 28px; {CARD}; display: flex; flex-direction: column; gap: 18px; {TILT}">
{SHIM}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("list", 22, "#9C938B", 2.2)}TABLERO DE LEADS · CRM</span>{EJ}</div>
<div style="position: relative; display: flex; gap: 14px">
{col("EN CURSO")}
{col("MÁS ADELANTE", "animation: colFlash 1.2s ease-in-out 2.9s infinite", "color: #FFB27A")}
{col("PERDIDO", "animation: colFlash .6s ease-in-out 1.3s 2 both, colDim .4s ease-out 2.6s forwards")}
{kcard}
{kcursor}
{nogo}
</div>
</div>
{sub("Quizá no era su momento. No lo tires: apunta cuándo volver.")}'''

# ---------- 03 Etiqueta por qué no compró: leads que caen en su caja ----------
buckets = [('coin', 'PRECIO', 'Otra opción', -290), ('clock', 'NO ERA EL MOMENTO', 'Nueva fecha', 0), ('phoneoff', 'NO CONTESTÓ', 'Otro canal y hora', 290)]
drops = [(1, 'Momento', 0.3), (0, 'Precio', 0.6), (2, 'No contestó', 0.9), (1, 'Momento', 1.2), (2, 'No contestó', 1.5), (0, 'Precio', 1.8), (1, 'Momento', 2.1)]
pills = ''
arrivals = {0: [], 1: [], 2: []}
for b, txt, d in drops:
    tx = buckets[b][3]
    pills += (f'<span style="position: absolute; z-index: 4; left: 50%; top: 74px; margin-left: -95px; width: 190px; --tx: {tx}px; display: flex; align-items: center; gap: 8px; padding: 10px 14px; box-sizing: border-box; border-radius: 99px; background: #2A2420; border: 1px solid rgba(255,106,26,0.55); box-shadow: 0 16px 30px -12px rgba(0,0,0,.9); opacity: 0; animation: sortDrop 1.15s cubic-bezier(.4,0,.6,1) {d:.2f}s both">'
              f'<span style="flex: none; width: 28px; height: 28px; border-radius: 99px; background: rgba(255,106,26,0.25); display: flex; align-items: center; justify-content: center">{ic("tag", 16, "#FFB27A", 2.4)}</span><span style="font-size: 19px; font-weight: 700">{txt}</span></span>')
    arrivals[b].append(d + 1.0)

bhtml = ''
for b, (icn, lab, act, _) in enumerate(buckets):
    hits = ', '.join(f'bucketHit .7s ease-out {a:.2f}s' for a in arrivals[b])
    stack = ''.join(f'<span style="width: 100%; height: 22px; border-radius: 8px; background: linear-gradient(90deg,#C84A0C,#FF6A1A,#FFB27A); box-shadow: 0 0 16px rgba(255,106,26,.6); opacity: 0; animation: stackIn .4s cubic-bezier(.2,.8,.2,1) {a:.2f}s both"></span>' for a in arrivals[b])
    bhtml += (f'<div style="flex: 1; display: flex; flex-direction: column; gap: 12px; align-items: stretch">'
              f'<div style="position: relative; height: 250px; box-sizing: border-box; padding: 16px; border-radius: 22px; border: 2px solid rgba(242,237,231,0.12); border-top-style: dashed; background: rgba(242,237,231,0.025); display: flex; flex-direction: column; gap: 10px; animation: {hits} both">'
              f'<div style="display: flex; align-items: center; gap: 10px">{ic(icn, 26, "#FF6A1A", 2.2)}<span style="{MONO}; font-size: 14px; font-weight: 600; letter-spacing: 0.08em; color: #F2EDE7; line-height: 1.2">{lab}</span></div>'
              f'<div style="margin-top: auto; display: flex; flex-direction: column-reverse; gap: 8px">{stack}</div></div>'
              f'<div style="display: flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 10px; border-radius: 16px; background: rgba(255,106,26,0.08); border: 1px solid rgba(255,106,26,0.3)">{ic("arrow", 20, "#FFB27A", 2.6)}<span style="font-size: 20px; font-weight: 700; color: #FFB27A">{act}</span></div></div>')

S3 = f'''{headline("Etiqueta por qué", "no compró.", 104)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 28px; {CARD}; display: flex; flex-direction: column; gap: 16px; {TILT}">
{SHIM}
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("tag", 22, "#9C938B", 2.2)}MOTIVO · CAMPO EN EL CRM</span>{EJ}</div>
<div style="position: relative; height: 110px">
<div style="position: absolute; left: 50%; top: 0; margin-left: -120px; width: 240px; height: 64px; border-radius: 99px; border: 1px dashed rgba(242,237,231,0.25); display: flex; align-items: center; justify-content: center; gap: 10px; {MONO}; font-size: 15px; letter-spacing: 0.1em; color: #9C938B">{ic("filter", 20, "#9C938B", 2.2)}LEADS DORMIDOS</div>
{pills}
</div>
<div style="position: relative; display: flex; gap: 14px">{bhtml}</div>
</div>
{sub("Así, cuando vuelvas, sabes qué decirle a cada uno.")}'''

# ---------- 04 Mensaje corto con dos opciones: chat que se escribe + anatomía ----------
segs = [('Hola Laura,', 0.45, 0.45), ('hace unas semanas hablamos de tu reforma.', 0.95, 0.75), ('¿Te llamo esta semana o la que viene?', 1.8, 0.7)]
segh = ''
for txt, d, du in segs:
    segh += f'<span style="display: block; width: fit-content; border-radius: 6px; padding: 0 3px; margin: 0 -3px; animation: typeC {du:.2f}s steps(30,end) {d:.2f}s both, segHi 1s ease-out {d:.2f}s both">{txt}</span>'
parts = [('user', 'Su nombre', 0.45), ('chat', 'De qué hablasteis', 0.95), ('help', 'Pregunta con dos opciones', 1.8)]
prows = ''
for icn, t, d in parts:
    prows += (f'<div style="display: flex; align-items: center; gap: 14px; padding: 15px 16px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); animation: rowOn .4s ease-out {d:.2f}s both">'
              f'<span style="flex: none; width: 36px; height: 36px; border-radius: 10px; border: 2px solid rgba(242,237,231,0.25); display: flex; align-items: center; justify-content: center; animation: check .4s ease-out {d+0.2:.2f}s both">{ic("ok", 22, "#0A0908", 3.4)}</span>'
              f'<span style="flex: 1; font-size: 22px; font-weight: 600; line-height: 1.2">{t}</span>{ic(icn, 26, "#FF6A1A", 2.2)}</div>')

S4 = f'''{headline("Un mensaje corto", "y fácil de contestar.", 98)}
<div style="position: relative; width: 920px; box-sizing: border-box; padding: 28px; {CARD}; display: flex; gap: 26px; align-items: stretch; {TILT}">
{SHIM}
<div style="position: relative; flex: none; width: 400px; height: 560px; border-radius: 46px; background: #0A0908; border: 3px solid rgba(242,237,231,0.16); box-shadow: inset 0 0 0 8px #12100F, 0 40px 100px -30px rgba(0,0,0,.9); overflow: hidden">
<div style="position: absolute; inset: 12px; border-radius: 36px; overflow: hidden; background: #12100F; display: flex; flex-direction: column">
<div style="flex: none; display: flex; align-items: center; gap: 12px; padding: 44px 18px 14px; background: #1C1916; border-bottom: 1px solid rgba(242,237,231,0.06)">
<span style="width: 44px; height: 44px; border-radius: 99px; background: rgba(255,106,26,0.2); display: flex; align-items: center; justify-content: center">{ic("user", 24, "#FFB27A", 2.2)}</span>
<div style="display: flex; flex-direction: column"><span style="font-size: 20px; font-weight: 700">Laura P.</span><span style="position: relative; height: 18px; font-size: 14px; color: #9C938B"><span style="position: absolute; left: 0; white-space: nowrap; animation: fadeOut .2s ease-in 2.6s forwards">últ. vez hace semanas</span><span style="position: absolute; left: 0; white-space: nowrap; color: #FFB27A; animation: fadeIn .2s ease-out 2.6s both">escribiendo…</span></span></div>
</div>
<div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 12px; padding: 18px 16px">
<span style="align-self: center; {MONO}; font-size: 13px; letter-spacing: 0.1em; color: #9C938B; padding: 5px 12px; border-radius: 99px; background: rgba(242,237,231,0.06)">HOY</span>
<div style="align-self: flex-end; width: 300px; box-sizing: border-box; padding: 14px 16px; border-radius: 18px 18px 4px 18px; background: #3A2214; border: 1px solid rgba(255,106,26,0.35); font-size: 19px; line-height: 1.35; animation: bubble .4s ease-out .2s both">
{segh}
<span style="display: block; margin-top: 6px; text-align: right; font-size: 13px; color: #9C938B">10:02 <span style="animation: tick .3s ease-out 2.5s both">✓✓</span></span>
</div>
<div style="align-self: flex-start; display: flex; gap: 6px; padding: 14px 16px; border-radius: 18px 18px 18px 4px; background: #24201C; animation: bubble .3s ease-out 2.6s both, fadeOut .1s linear 3.15s forwards">
<span style="width: 9px; height: 9px; border-radius: 99px; background: #B5ADA4; animation: bounce .6s ease-in-out 0s infinite"></span><span style="width: 9px; height: 9px; border-radius: 99px; background: #B5ADA4; animation: bounce .6s ease-in-out .15s infinite"></span><span style="width: 9px; height: 9px; border-radius: 99px; background: #B5ADA4; animation: bounce .6s ease-in-out .3s infinite"></span>
</div>
<div style="position: absolute; left: 16px; top: 296px; max-width: 280px; padding: 12px 16px; border-radius: 18px 18px 18px 4px; background: #24201C; font-size: 19px; animation: bubble .35s ease-out 3.15s both">¡Esta semana mejor!</div>
</div>
</div>
<div style="position: absolute; top: 18px; left: 50%; margin-left: -45px; width: 90px; height: 24px; border-radius: 99px; background: #1E1A17; z-index: 5"></div>
</div>
<div style="position: relative; flex: 1; display: flex; flex-direction: column; gap: 14px">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="display: flex; align-items: center; gap: 10px; {LBL}">{ic("list", 22, "#9C938B", 2.2)}EL MENSAJE</span>{EJ}</div>
{prows}
<div style="margin-top: auto; padding: 16px 18px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); display: flex; flex-direction: column; gap: 12px">
<span style="{MONO}; font-size: 15px; letter-spacing: 0.12em; color: #9C938B">ESTADO EN EL CRM</span>
<span style="position: relative; height: 36px">
<span style="position: absolute; left: 0; top: 0; animation: fadeOut .2s ease-in 2.95s forwards">{chip("DORMIDO", "#B5ADA4", "rgba(242,237,231,0.05)", "rgba(242,237,231,0.2)")}</span>
<span style="position: absolute; left: 0; top: 0; animation: pop .5s cubic-bezier(.2,.8,.2,1) 2.95s both">{chip("REACTIVADO ✓", "#0A0908", "#FF6A1A", "#FF6A1A", "box-shadow: 0 0 26px rgba(255,106,26,.8)")}</span>
</span>
</div>
</div>
</div>
{sub("Que pueda contestar en un segundo, sin pensarlo.")}'''

# ---------- 05 CTA: checklist + Síguenos ----------
checks = [('filter', 'Filtra los leads dormidos'), ('tag', 'Etiqueta por qué no compró'), ('whats', 'Mensaje corto con dos opciones'), ('list', 'Apunta la respuesta en el CRM')]
crows = ''
for i, (icn, t) in enumerate(checks):
    d = 0.5 + i * 0.45
    crows += (f'<div style="display: flex; align-items: center; gap: 18px; padding: 14px 20px; border-radius: 18px; border: 1px solid rgba(242,237,231,0.1); background: rgba(242,237,231,0.03); animation: rowOn .5s ease-out {d:.2f}s both">'
              f'<span style="flex: none; width: 42px; height: 42px; border-radius: 12px; border: 2px solid rgba(242,237,231,0.25); display: flex; align-items: center; justify-content: center; animation: check .45s ease-out {d:.2f}s both">{ic("ok", 26, "#0A0908", 3.4)}</span>'
              f'<span style="flex: 1; font-size: 28px; font-weight: 600; text-align: left">{t}</span>{ic(icn, 30, "#FF6A1A", 2.2)}</div>')
S5 = f'''<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<p style="margin: 0 0 36px; {BRIC}; font-size: 80px; line-height: 1; letter-spacing: -0.045em; animation: aIn .8s cubic-bezier(.2,.8,.2,1) .1s both">Despierta tus<br><span style="font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A">leads dormidos.</span></p>
<div style="position: relative; width: 900px; box-sizing: border-box; padding: 26px; {CARD}; display: flex; flex-direction: column; gap: 12px; {TILT}">
{SHIM}
<span style="{LBL}; text-align: left">CHECKLIST PARA REACTIVAR</span>
{crows}
</div>
<div style="position: relative; margin-top: 50px; animation: pop .7s cubic-bezier(.2,.8,.2,1) 2.3s both"><div style="animation: wob 4s ease-in-out infinite">
<div style="position: relative; overflow: hidden; padding: 30px 60px; border-radius: 34px; background: #FF6A1A; color: #0A0908; {BRIC}; font-size: 100px; line-height: 0.9; letter-spacing: -0.05em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 2s ease-in-out infinite">Síguenos<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.35), rgba(255,255,255,0)); animation: aShim 2s ease-in-out infinite"></div></div>
</div></div>
<p style="margin: 30px 0 0; font-family: 'Instrument Serif', serif; font-style: italic; font-size: 56px; line-height: 1.05; animation: aIn .8s cubic-bezier(.2,.8,.2,1) 2.6s both">para más tips de captación y ventas.</p>
</div>'''

for n, name, mid, title in [(1, 'Main', S1, '01'), (2, 'S2', S2, '02'), (3, 'S3', S3, '03'), (4, 'S4', S4, '04'), (5, 'S5', S5, '05')]:
    html = page(n, mid, title).replace('GUÁRDALO PARA TUS PRÓXIMAS CITAS', 'GUÁRDALO PARA TU PRÓXIMA REACTIVACIÓN')
    open(os.path.join(SRC, f'{name}.dc.html'), 'w').write(html)
print('ok')
