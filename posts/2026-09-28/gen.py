#!/usr/bin/env python3
"""Genera los 5 .dc.html del carrusel 2026-09-28 (valor: seguimiento a un lead que no contesta)."""
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
            f'<span style="font-family: \'Instrument Serif\', serif; font-style: italic; font-weight: 400; color: #FF6A1A">{b}</span></h2>')


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
        tail = f'<span style="align-self: center; {MONO}; font-size: 22px; letter-spacing: 0.12em; color: #9C938B">@CEOS.GROWTH · GUÁRDALO PARA TU PRÓXIMO LEAD</span>'
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


# ---------- 01 GANCHO: móvil llamando + intentos + respuesta ----------
def attempt(icon, label, status, st_color, delay, good=False):
    border = 'rgba(255,106,26,0.7)' if good else 'rgba(242,237,231,0.1)'
    bg = 'rgba(255,106,26,0.12)' if good else 'rgba(242,237,231,0.03)'
    glow = '; box-shadow: 0 0 40px -6px rgba(255,106,26,0.7)' if good else ''
    icbg = '#FF6A1A' if good else 'rgba(242,237,231,0.08)'
    icc = '#0A0908' if good else '#F2EDE7'
    return f'''<div style="display: flex; align-items: center; gap: 16px; padding: 16px 18px; border-radius: 20px; border: 1px solid {border}; background: {bg}{glow}; animation: rowIn .6s cubic-bezier(.2,.8,.2,1) {delay}s both">
<span style="flex: none; width: 50px; height: 50px; border-radius: 14px; background: {icbg}; display: flex; align-items: center; justify-content: center">{ic(icon, 24, icc)}</span>
<div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 25px; font-weight: 600">{label}</span><span style="{MONO}; font-size: 17px; letter-spacing: 0.06em; color: {st_color}">{status}</span></div>
</div>'''


s1_card = f'''<div style="position: relative; width: 920px; box-sizing: border-box; padding: 34px; {CARD}; display: flex; gap: 34px; {TILT}">
<div style="flex: 1; display: flex; flex-direction: column; gap: 16px">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="{MONO}; font-size: 19px; letter-spacing: 0.14em; color: #9C938B">SEGUIMIENTO</span>{EJ}</div>
<span style="{BRIC}; font-size: 40px; letter-spacing: -0.03em">Marta G.</span>
{attempt('phone', 'Llamada 10:00', 'SIN RESPUESTA', '#9C938B', 0.6)}
{attempt('chat', 'WhatsApp 10:05', 'ENVIADO ✓✓', '#B5ADA4', 1.3)}
{attempt('phone', 'Llamada 17:30', 'CONTESTA', '#FFB27A', 2.2, True)}
</div>
<div style="position: relative; flex: none; width: 300px; height: 520px; border-radius: 44px; background: #0A0908; border: 3px solid rgba(242,237,231,0.16); box-shadow: inset 0 0 0 8px #12100F; overflow: hidden; display: flex; flex-direction: column; align-items: center; padding-top: 70px; box-sizing: border-box">
<div style="position: absolute; top: 14px; left: 50%; margin-left: -45px; width: 90px; height: 24px; border-radius: 99px; background: #1E1A17"></div>
<span style="{MONO}; font-size: 16px; letter-spacing: 0.14em; color: #9C938B">LLAMANDO…</span>
<div style="position: relative; margin-top: 40px; width: 120px; height: 120px">
<span style="position: absolute; inset: 0; border-radius: 99px; border: 3px solid rgba(255,106,26,0.8); animation: ring 1.3s ease-out infinite"></span>
<span style="position: absolute; inset: 0; border-radius: 99px; border: 3px solid rgba(255,106,26,0.8); animation: ring 1.3s ease-out .65s infinite"></span>
<div style="position: absolute; inset: 0; border-radius: 99px; background: linear-gradient(160deg, #FF8F45, #C84A0C); display: flex; align-items: center; justify-content: center; {BRIC}; font-size: 48px; color: #0A0908">M</div>
</div>
<span style="margin-top: 26px; font-size: 28px; font-weight: 700">Marta G.</span>
<div style="margin-top: 70px; width: 84px; height: 84px; border-radius: 99px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 40px rgba(255,106,26,.7); animation: shake .9s ease-in-out infinite">{ic('phone', 38, '#0A0908', 2.6)}</div>
<div style="position: absolute; left: 14px; right: 14px; top: 46px; padding: 16px 16px; border-radius: 20px; background: rgba(242,237,231,0.96); color: #0A0908; box-shadow: 0 20px 40px -10px rgba(0,0,0,.8); animation: drop .7s cubic-bezier(.2,.8,.2,1) 2.5s both">
<div style="display: flex; align-items: center; gap: 8px; {MONO}; font-size: 13px; letter-spacing: 0.1em; color: #6B635C">{ic('chat', 16, '#C84A0C', 2.6)}WHATSAPP · AHORA</div>
<div style="margin-top: 6px; font-size: 20px; font-weight: 600; line-height: 1.25">Marta: ¡Ahora sí puedo! ¿Me llamas?</div>
</div>
</div>
<div style="position: absolute; left: 34px; bottom: -32px; display: inline-flex; align-items: center; gap: 12px; padding: 16px 26px; border-radius: 999px; background: #F2EDE7; color: #0A0908; font-weight: 700; font-size: 26px; box-shadow: 0 20px 60px -10px rgba(255,106,26,0.7); animation: pop .6s cubic-bezier(.2,.8,.2,1) 3.1s both"><span style="width: 30px; height: 30px; border-radius: 99px; background: #FF6A1A; display: flex; align-items: center; justify-content: center">{ic('cal', 18, '#0A0908', 2.8)}</span>Cita agendada</div>
<div style="position: absolute; left: 100px; bottom: -70px; width: 200px; height: 200px; border-radius: 999px; border: 3px solid rgba(255,106,26,0.8); pointer-events: none; animation: burst .9s ease-out 3.1s both"></div>
</div>'''

S1 = headline('Tu lead no contesta.', 'No está perdido.', 108) + '\n' + s1_card

# ---------- 02 PROBLEMA: el lead se enfría ----------
days = ''.join(f'<div style="flex: 1; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; {MONO}; font-size: 18px; font-weight: 600; color: rgba(10,9,8,0.8); animation: dayOff .5s ease-out {0.6 + i * 0.34:.2f}s both">D{i + 1}</div>' for i in range(7))
s2_card = f'''<div style="position: relative; width: 920px; box-sizing: border-box; padding: 36px 38px; {CARD}; display: flex; flex-direction: column; gap: 28px; {TILT}">
<div style="display: flex; align-items: center; gap: 18px">
<div style="width: 70px; height: 70px; border-radius: 99px; background: linear-gradient(160deg, #FF8F45, #C84A0C); display: flex; align-items: center; justify-content: center; {BRIC}; font-size: 32px; color: #0A0908; animation: greyOut 2.4s linear .6s both">C</div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 30px; font-weight: 700">Carlos R. · lead nuevo</span><span style="display: inline-flex; align-items: center; gap: 8px; {MONO}; font-size: 18px; color: #9C938B">{ic('phone', 18, '#9C938B')} 1 LLAMADA · SIN RESPUESTA</span></div>
{EJ}
</div>
<div style="display: flex; align-items: flex-end; justify-content: space-between">
<div style="display: flex; flex-direction: column; gap: 10px"><span style="{MONO}; font-size: 19px; letter-spacing: 0.14em; color: #9C938B">DÍAS SIN CONTACTO</span>
<div style="position: relative; height: 34px; font-size: 28px; font-weight: 700"><span style="position: absolute; left: 0; display: inline-flex; align-items: center; gap: 8px; color: #FF8F45; white-space: nowrap; animation: fadeOut .4s ease 2.2s both">{ic('flame', 26, '#FF6A1A')} Interesado</span><span style="position: absolute; left: 0; white-space: nowrap; color: #9C938B; animation: fadeIn .4s ease 2.3s both">Se ha olvidado de ti</span></div></div>
<span class="dc" style="{BRIC}; font-size: 150px; line-height: 0.8; letter-spacing: -0.05em; color: #F2EDE7"></span>
</div>
<div style="position: relative; height: 16px; border-radius: 99px; background: rgba(242,237,231,0.08); overflow: hidden"><div style="position: absolute; left: 0; top: 0; bottom: 0; border-radius: 99px; animation: cool 2.6s ease-in .5s both"></div><div style="position: absolute; top: 0; bottom: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.35), rgba(255,255,255,0)); animation: shim 1.4s linear infinite"></div></div>
<div style="display: flex; gap: 10px">{days}</div>
<div style="position: absolute; left: 270px; bottom: 26px; padding: 12px 26px; border: 5px solid #FF6A1A; border-radius: 14px; {BRIC}; font-size: 46px; letter-spacing: -0.02em; color: #FF6A1A; background: rgba(10,9,8,0.85); animation: stamp .5s cubic-bezier(.2,.8,.2,1) 3.1s both">LEAD FRÍO</div>
</div>'''
S2 = headline('Una llamada', 'no es seguimiento.', 108) + '\n' + sub('Si lo dejas ahí, el lead se enfría y acaba comprando a otro.') + '\n' + s2_card

# ---------- 03 CANAL Y HORA: timeline con punto que viaja ----------
steps3 = [('phone', 'Llamada', 'Mañana · 10:00'), ('chat', 'WhatsApp corto', 'A los 5 min'), ('phone', 'Llamada', 'Tarde · 17:30'), ('mic', 'Audio de voz', 'Día siguiente')]
rows = ''
for i, (icn, name, when) in enumerate(steps3):
    d = 0.5 + i * 0.7
    last = i == 3
    rows += f'''<div style="position: relative; height: 94px; box-sizing: border-box; display: flex; align-items: center; gap: 22px; padding: 0 22px 0 88px; border-radius: 22px; border: 1px solid rgba(242,237,231,0.1); animation: rowOn .35s ease-out {d:.2f}s both">
<span style="position: absolute; left: 22px; width: 50px; height: 50px; border-radius: 99px; display: flex; align-items: center; justify-content: center; animation: icoOn .35s ease-out {d:.2f}s both">{ic(icn, 24)}</span>
<span style="flex: 1; font-size: 30px; font-weight: 700; animation: txtOn .35s ease-out {d:.2f}s both">{name}</span>
<span style="{MONO}; font-size: 20px; letter-spacing: 0.06em; color: #B5ADA4">{when}</span>
{f'<span style="position: absolute; right: 22px; top: -18px; display: inline-flex; align-items: center; gap: 8px; padding: 8px 16px; border-radius: 99px; background: #F2EDE7; color: #0A0908; font-weight: 700; font-size: 20px; animation: pop .5s cubic-bezier(.2,.8,.2,1) 3.0s both">{ic("ok", 16, "#0A0908", 3.2)}Responde</span>' if last else ''}
</div>'''
s3_card = f'''<div style="position: relative; width: 920px; box-sizing: border-box; padding: 34px 38px 38px; {CARD}; display: flex; flex-direction: column; gap: 22px; {TILT}">
<div style="display: flex; align-items: center; justify-content: space-between"><span style="{MONO}; font-size: 19px; letter-spacing: 0.14em; color: #9C938B">SECUENCIA DE SEGUIMIENTO</span>{EJ}</div>
<div style="position: relative; display: flex; flex-direction: column; gap: 18px">
<div style="position: absolute; left: 46px; top: 47px; height: 336px; width: 2px; background: rgba(255,106,26,0.25)"></div>
{rows}
<div style="position: absolute; left: 39px; width: 16px; height: 16px; margin-top: -8px; border-radius: 99px; background: #FFB27A; box-shadow: 0 0 22px 4px rgba(255,106,26,0.9); z-index: 2; animation: travel 2.1s linear .5s both"></div>
</div>
</div>'''
S3 = headline('Cambia de canal', 'y de hora.', 108) + '\n' + sub('No insistas igual: llamada, WhatsApp, audio… en distintos momentos del día.') + '\n' + s3_card

# ---------- 04 MENSAJE: chat que se escribe ----------
Q = '¿Hoy a las 17:00 o mañana a las 10:00?'
s4_card = f'''<div style="position: relative; width: 920px; box-sizing: border-box; {CARD}; overflow: hidden; display: flex; flex-direction: column; {TILT}">
<div style="display: flex; align-items: center; gap: 16px; padding: 22px 30px; background: rgba(242,237,231,0.04); border-bottom: 1px solid rgba(242,237,231,0.08)">
<div style="width: 56px; height: 56px; border-radius: 99px; background: linear-gradient(160deg, #FF8F45, #C84A0C); display: flex; align-items: center; justify-content: center; {BRIC}; font-size: 26px; color: #0A0908">M</div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 26px; font-weight: 700">Marta G.</span><span style="{MONO}; font-size: 16px; color: #FFB27A">en línea</span></div>{EJ}
</div>
<div style="position: relative; height: 470px; padding: 26px 30px; box-sizing: border-box; display: flex; flex-direction: column; gap: 16px">
<div style="align-self: flex-end; max-width: 640px; padding: 18px 22px; border-radius: 24px 24px 6px 24px; background: #FF6A1A; color: #0A0908; font-size: 26px; font-weight: 600; line-height: 1.3; animation: pop .5s cubic-bezier(.2,.8,.2,1) .4s both">Hola Marta, soy Álex. Te llamé por tu presupuesto.</div>
<div style="align-self: flex-end; max-width: 640px; padding: 18px 22px; border-radius: 24px 24px 6px 24px; background: #FF6A1A; color: #0A0908; font-size: 26px; font-weight: 700; line-height: 1.3; animation: pop .5s cubic-bezier(.2,.8,.2,1) 1.95s both">{Q} <span style="font-size: 18px; color: rgba(10,9,8,0.6)">✓✓</span></div>
<div style="align-self: flex-start; display: flex; gap: 8px; padding: 20px 22px; border-radius: 24px 24px 24px 6px; background: rgba(242,237,231,0.1); animation: fadeIn .2s 2.3s both, fadeOut .2s 2.85s forwards"><span style="width: 10px; height: 10px; border-radius: 99px; background: #F2EDE7; animation: bounce .6s ease-in-out infinite"></span><span style="width: 10px; height: 10px; border-radius: 99px; background: #F2EDE7; animation: bounce .6s ease-in-out .15s infinite"></span><span style="width: 10px; height: 10px; border-radius: 99px; background: #F2EDE7; animation: bounce .6s ease-in-out .3s infinite"></span></div>
<div style="position: absolute; left: 30px; top: 232px; max-width: 560px; padding: 18px 22px; border-radius: 24px 24px 24px 6px; background: #F2EDE7; color: #0A0908; font-size: 26px; font-weight: 600; line-height: 1.3; animation: pop .5s cubic-bezier(.2,.8,.2,1) 2.9s both">Mañana a las 10, perfecto.</div>
<div style="position: absolute; left: 30px; top: 318px; display: inline-flex; align-items: center; gap: 10px; padding: 12px 20px; border-radius: 99px; border: 1px solid rgba(255,106,26,0.6); background: rgba(255,106,26,0.12); font-size: 22px; font-weight: 700; color: #FFB27A; animation: pop .5s cubic-bezier(.2,.8,.2,1) 3.3s both">{ic('cal', 20, '#FFB27A')}Cita guardada en el CRM</div>
</div>
<div style="display: flex; align-items: center; gap: 16px; padding: 18px 24px; border-top: 1px solid rgba(242,237,231,0.08)">
<div style="flex: 1; height: 60px; border-radius: 99px; background: rgba(242,237,231,0.06); display: flex; align-items: center; padding: 0 24px; overflow: hidden">
<div style="position: relative; animation: fadeOut .1s linear 1.9s forwards"><div style="overflow: hidden; white-space: nowrap; font-size: 24px; width: 0; border-right: 2px solid #FF6A1A; padding-right: 2px; animation: type 1.1s steps(38, end) .8s both">{Q}</div></div>
</div>
<div style="width: 60px; height: 60px; border-radius: 99px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 24px rgba(255,106,26,.6)"><svg width="26" height="26" viewBox="0 0 24 24" fill="#0A0908" aria-hidden="true"><path d="M3 20l18-8L3 4v6l12 2-12 2z"/></svg></div>
</div>
</div>'''
S4 = headline('Mensaje corto,', 'pregunta fácil.', 108) + '\n' + sub('Dale dos opciones: que responderte le cueste un segundo.') + '\n' + s4_card

# ---------- 05 CTA: checklist + Síguenos ----------
items = ['No lo des por perdido a la primera', 'Alterna llamada, WhatsApp y audio', 'Prueba otra hora del día', 'Pregunta con dos opciones', 'Apunta cada intento en el CRM']
chk = ''
for i, t in enumerate(items):
    d = 0.4 + i * 0.4
    chk += f'''<div style="display: flex; align-items: center; gap: 20px; animation: rowIn .5s cubic-bezier(.2,.8,.2,1) {d - 0.2:.2f}s both">
<span style="flex: none; width: 40px; height: 40px; border-radius: 12px; border: 2px solid rgba(242,237,231,0.25); display: flex; align-items: center; justify-content: center; animation: check .4s ease-out {d:.2f}s both"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="stroke-dasharray: 30; animation: draw .35s ease-out {d + 0.1:.2f}s both"><path d="M5 12l5 5L20 7"/></svg></span>
<span style="font-size: 32px; font-weight: 600; animation: txtOn .4s ease-out {d:.2f}s both">{t}</span>
</div>'''
S5 = f'''<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 0">
<div style="width: 920px; box-sizing: border-box; padding: 34px 40px; {CARD}; display: flex; flex-direction: column; gap: 20px; text-align: left; {TILT}">
<span style="{MONO}; font-size: 19px; letter-spacing: 0.14em; color: #9C938B">CHECKLIST · LEAD QUE NO CONTESTA</span>
{chk}
</div>
<p style="margin: 64px 0 0; {BRIC}; font-size: 60px; line-height: 1.02; letter-spacing: -0.04em; animation: aIn .8s cubic-bezier(.2,.8,.2,1) 2.3s both">¿Te ha servido?</p>
<div style="position: relative; margin-top: 30px; animation: pop .7s cubic-bezier(.2,.8,.2,1) 2.6s both"><div style="animation: wob 4s ease-in-out infinite">
<div style="position: relative; overflow: hidden; padding: 30px 60px; border-radius: 34px; background: #FF6A1A; color: #0A0908; {BRIC}; font-size: 100px; line-height: 0.9; letter-spacing: -0.05em; box-shadow: inset 0 -8px 0 rgba(0,0,0,0.18), 0 40px 120px -20px rgba(255,106,26,0.8); animation: aBreathe 2s ease-in-out infinite">Síguenos<div style="position: absolute; top: 0; bottom: 0; left: 0; width: 20%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.35), rgba(255,255,255,0)); animation: aShim 2s ease-in-out infinite"></div></div>
</div></div>
<p style="margin: 40px 0 0; font-family: 'Instrument Serif', serif; font-style: italic; font-size: 54px; line-height: 1.05; animation: aIn .8s cubic-bezier(.2,.8,.2,1) 2.9s both">para más tips de captación y ventas.</p>
</div>'''

for n, name, mid, title in [(1, 'Main', S1, '01'), (2, 'S2', S2, '02'), (3, 'S3', S3, '03'), (4, 'S4', S4, '04'), (5, 'S5', S5, '05')]:
    open(os.path.join(SRC, f'{name}.dc.html'), 'w').write(page(n, mid, title))
print('ok')
