#!/usr/bin/env python3
"""Genera las escenas (.dc.html) de un reel de valor a partir de un spec JSON.

Uso: python3 toolkit/reels/gen_reel.py spec.json carpeta_src

Spec:
{
  "scenes": [
    {"kind": "hook", "title": "¿Tus leads<br>te dejan <em>en visto?</em>", "mock": {...}, "footer": "3 pasos para recuperarlos", "dur": 5},
    {"kind": "step", "label": "PASO 1", "title": "...", "mock": {...}, "note": "Texto <b>resaltado</b>", "dur": 6},
    ...,
    {"kind": "cta", "label": "RESUMEN", "title": "...", "items": ["...", "...", "..."], "button": "Síguenos para más tips", "dur": 6}
  ]
}
<em>..</em> en títulos = cursiva naranja. <b>..</b> en notas = color crema.
Tipos de mock: chat, timer, timeline, checklist, ad, form, compare, bars, script (ver funciones m_*).
Todos los datos de ejemplo llevan la etiqueta EJEMPLO. Nunca inventar estadísticas reales.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from components import HEAD, TAIL, SER, MONO, BRIC, CARD, TILT, CHK, TICKS, header, title, footer, mono_note, ej  # noqa: E402

EXTRA_CSS = """@keyframes aGrowW{from{width:0}}
@keyframes aHi{from{background:transparent;color:#6B635C}to{background:rgba(255,106,26,.14);color:#F2EDE7}}
@keyframes aStrike{from{width:0}to{width:100%}}
@keyframes aMedia{0%{background-position:0% 50%}100%{background-position:100% 50%}}
"""
HEAD2 = HEAD.replace('@media (prefers-reduced-motion', EXTRA_CSS + '@media (prefers-reduced-motion', 1)


def ttl(html):
    return re.sub(r'<em>(.*?)</em>', lambda m: f'<span style="{SER}">{m.group(1)}</span>', html)


def nt(html):
    return re.sub(r'<b>(.*?)</b>', r'<span style="color: #F2EDE7">\1</span>', html)


def av(letter, size=72):
    return (f'<span style="flex-shrink: 0; width: {size}px; height: {size}px; border-radius: 99px; background: linear-gradient(135deg,#FF6A1A,#FFB27A); '
            f'display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: {size//2}px; color: #0A0908">{letter}</span>')


def ico_ok(d, size=60, dark=True):
    return (f'<span style="flex-shrink: 0; width: {size}px; height: {size}px; border-radius: 99px; background: #FF6A1A; display: flex; align-items: center; '
            f'justify-content: center; box-shadow: 0 0 24px rgba(255,106,26,.6)">{CHK.format(d=d)}</span>')


# ---------------- MOCKUPS ----------------
def m_chat(m):
    """{"type":"chat","name":"Laura","msgs":[{"from":"out","lines":["Hola...","¿Te va...?"]},{"from":"in","text":"..."}]}"""
    t = 1.2
    body = ''
    for msg in m['msgs']:
        if msg['from'] == 'out':
            lines = msg.get('lines') or [msg['text']]
            spans = ''
            tt = t + .3
            for ln in lines:
                dur = max(.5, len(ln) * .045)
                spans += f'<span style="display: block; white-space: nowrap; animation: aType {dur:.2f}s steps({max(8, len(ln))}, end) {tt:.2f}s both">{ln}</span>'
                tt += dur + .1
            body += (f'<div style="align-self: flex-end; max-width: 86%; padding: 26px 30px; border-radius: 30px 30px 8px 30px; background: linear-gradient(135deg,#FF6A1A,#FF8F45); '
                     f'color: #0A0908; font-size: 32px; font-weight: 600; line-height: 1.32; animation: aPop .5s cubic-bezier(.2,.8,.2,1) {t:.2f}s both">{spans}'
                     f'<div style="display: flex; justify-content: flex-end; align-items: center; gap: 8px; {MONO}; font-size: 20px; margin-top: 8px; animation: aShow .2s linear {tt:.2f}s both">'
                     f'{msg.get("time", "")} {TICKS.format(d=tt + .4)}</div></div>')
            t = tt + .7
        else:
            body += (f'<div style="align-self: flex-start; max-width: 86%; padding: 26px 30px; border-radius: 30px 30px 30px 8px; background: #26221F; font-size: 32px; '
                     f'font-weight: 600; line-height: 1.32; transform-origin: 0 100%; animation: aPop .5s cubic-bezier(.2,.8,.2,1) {t:.2f}s both">{msg["text"]}'
                     f'<div style="{MONO}; font-size: 20px; color: #9C938B; margin-top: 8px">{msg.get("time", "")}</div></div>')
            t += 1.1
    return (f'<div style="position: relative; {CARD}; overflow: hidden; {TILT}">'
            f'<div style="display: flex; align-items: center; gap: 20px; padding: 28px 36px; background: #171412; border-bottom: 1px solid rgba(242,237,231,0.08)">{av(m.get("name", "L")[0], 66)}'
            f'<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 32px; font-weight: 700">{m.get("name", "Lead")}</span>'
            f'<span style="{MONO}; font-size: 20px; color: #35D07F">EN LÍNEA</span></div><span style="margin-left: auto; {MONO}; font-size: 20px; letter-spacing: 0.12em; color: #6B635C">EJEMPLO</span></div>'
            f'<div style="padding: 40px 36px 46px; display: flex; flex-direction: column; gap: 24px">{body}</div></div>')


def m_timer(m):
    """{"type":"timer","head":"Nuevo lead · Meta","sub":"TIEMPO DE RESPUESTA","secs":272,"side":"Llamas mientras<br>aún se acuerda<br>de ti","badge":"✓ CONECTADA"}"""
    secs = int(m.get('secs', 272))
    mins = secs // 60
    rem = secs % 60
    cyc = 3.2 / max(1, secs / 60)  # duración de un ciclo de 60 s simulados
    it = secs / 60
    frac = min(0.91, secs / 300)
    return f"""<div style="position: relative; {CARD}; padding: 50px 44px; display: flex; flex-direction: column; gap: 40px; {TILT}">{ej()}
<div style="display: flex; align-items: center; gap: 22px"><span style="flex-shrink: 0; width: 72px; height: 72px; border-radius: 20px; background: #FF6A1A; display: flex; align-items: center; justify-content: center; animation: aPing 1.6s ease-out infinite"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path></svg></span><div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 36px; font-weight: 700">{m.get('head', 'Nuevo lead')}</span><span style="{MONO}; font-size: 22px; color: #9C938B">{m.get('sub', '')}</span></div></div>
<div style="display: flex; align-items: center; gap: 46px">
<div style="position: relative; width: 280px; height: 280px; flex-shrink: 0">
<svg width="280" height="280" viewBox="0 0 280 280" style="position: absolute; inset: 0; transform: rotate(-90deg)" aria-hidden="true"><circle cx="140" cy="140" r="120" fill="none" stroke="#1E1A17" stroke-width="20"></circle><circle cx="140" cy="140" r="120" fill="none" stroke="#FF6A1A" stroke-width="20" stroke-linecap="round" stroke-dasharray="754" style="--end: {754 * (1 - frac):.0f}; animation: aArc 3.2s cubic-bezier(.3,.1,.3,1) 1.1s both, aArcG .3s linear 4.3s both"></circle></svg>
<span class="mm" style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 72px; letter-spacing: -0.04em; font-variant-numeric: tabular-nums; animation-name: aMinK, aSecK; animation-duration: {cyc * mins:.3f}s, {cyc:.3f}s; animation-timing-function: steps({max(1, mins)}, end), linear; animation-delay: 1.1s, 1.1s; animation-iteration-count: 1, {it:.3f}; animation-fill-mode: both, both"></span>
</div>
<div style="display: flex; flex-direction: column; gap: 22px"><span style="{BRIC}; font-weight: 700; font-size: 42px; line-height: 1.1; letter-spacing: -0.02em">{m.get('side', '')}</span>
<span style="align-self: flex-start; display: flex; align-items: center; gap: 12px; padding: 14px 22px; border-radius: 16px; background: rgba(53,208,127,0.14); color: #35D07F; {MONO}; font-weight: 600; font-size: 24px; letter-spacing: 0.06em; animation: aPop .6s cubic-bezier(.2,.8,.2,1) 4.4s both, aPingG 1.6s ease-out 5s infinite">{m.get('badge', '✓ HECHO')}</span></div>
</div>
</div>""".replace('@@', '')


def m_timeline(m):
    """{"type":"timeline","rows":[{"n":"1","d":"DÍA 1","t":"...","s":"..."}, ...]}"""
    rows = m['rows']
    out = f'<div style="position: relative; display: flex; flex-direction: column; gap: 30px; padding-left: 120px; {TILT}">'
    out += '<div style="position: absolute; left: 41px; top: 50px; bottom: 50px; width: 6px; border-radius: 9px; background: rgba(242,237,231,0.1)"><div style="width: 100%; border-radius: 9px; background: linear-gradient(#FF6A1A,#FFB27A); box-shadow: 0 0 18px #FF6A1A; animation: aRail 2.6s cubic-bezier(.4,0,.2,1) 1.3s both"></div></div>'
    for i, r in enumerate(rows):
        dl = 1.3 + i * 1.2
        out += (f'<div style="position: relative; {CARD}; padding: 34px 40px; display: flex; flex-direction: column; gap: 8px; animation: aIn .7s cubic-bezier(.2,.8,.2,1) {dl - .3:.1f}s both, aRow .4s ease-out {dl:.1f}s both">'
                f'<span style="position: absolute; left: -110px; top: 50%; margin-top: -36px; width: 64px; height: 64px; border-radius: 99px; border: 4px solid rgba(242,237,231,0.2); background: #12100F; display: flex; align-items: center; justify-content: center; {BRIC}; font-weight: 800; font-size: 30px; animation: aNode .5s ease-out {dl:.1f}s both">{r.get("n", i + 1)}</span>'
                f'<span style="{MONO}; font-size: 24px; letter-spacing: 0.14em; color: #FF6A1A">{r.get("d", "")}</span><span style="{BRIC}; font-weight: 800; font-size: 42px; letter-spacing: -0.03em">{r["t"]}</span>'
                + (f'<span style="font-size: 28px; color: #9C938B">{r["s"]}</span>' if r.get('s') else '') + '</div>')
    return out + '</div>'


def m_checklist(m, start=1.0):
    """{"type":"checklist","items":["...","..."]}"""
    out = f'<div style="display: flex; flex-direction: column; gap: 22px; {TILT}">'
    for i, t in enumerate(m['items']):
        dl = start + i * .45
        out += (f'<div style="display: flex; align-items: center; gap: 26px; padding: 30px 36px; border-radius: 30px; background: rgba(18,16,15,0.92); border: 1px solid rgba(255,106,26,0.35); '
                f'animation: aIn .6s cubic-bezier(.2,.8,.2,1) {dl:.2f}s both">{ico_ok(dl + .3)}<span style="{BRIC}; font-weight: 700; font-size: 40px; letter-spacing: -0.02em; line-height: 1.1">{t}</span></div>')
    return out + '</div>'


def m_ad(m):
    """{"type":"ad","brand":"Tu negocio","copy":"...","media":"TEXTO GRANDE DEL VÍDEO","headline":"...","cta":"Más información","tags":["GANCHO 0–3 s", ...]}"""
    tags = ''.join(f'<span style="padding: 10px 18px; border-radius: 99px; border: 1px solid rgba(255,106,26,.6); background: rgba(255,106,26,.12); {MONO}; font-size: 20px; letter-spacing: .08em; color: #FFB27A; animation: aPop .5s cubic-bezier(.2,.8,.2,1) {2.4 + i * .5:.1f}s both">{t}</span>'
                   for i, t in enumerate(m.get('tags', [])))
    return f"""<div style="position: relative; {CARD}; overflow: hidden; {TILT}">
<div style="display: flex; align-items: center; gap: 18px; padding: 26px 30px">{av(m.get('brand', 'T')[0], 60)}<div style="display: flex; flex-direction: column"><span style="font-size: 28px; font-weight: 700">{m.get('brand', 'Tu negocio')}</span><span style="font-size: 20px; color: #9C938B">Publicidad</span></div><span style="margin-left: auto; {MONO}; font-size: 20px; letter-spacing: 0.12em; color: #6B635C">EJEMPLO</span></div>
<div style="padding: 0 30px 20px; font-size: 26px; color: #D9D1C8; line-height: 1.3">{m.get('copy', '')}</div>
<div style="height: 380px; background: linear-gradient(120deg,#2A1408,#FF6A1A,#3A1A0A,#FF8F45); background-size: 300% 300%; animation: aMedia 6s ease-in-out infinite alternate; display: flex; align-items: center; justify-content: center; padding: 30px; box-sizing: border-box; text-align: center">
<span style="{BRIC}; font-weight: 800; font-size: 60px; line-height: 1; letter-spacing: -0.04em; color: #0A0908; animation: aPop .6s cubic-bezier(.2,.8,.2,1) 1.4s both">{m.get('media', '')}</span></div>
<div style="display: flex; align-items: center; justify-content: space-between; gap: 20px; padding: 24px 30px; background: #171412"><span style="{BRIC}; font-weight: 700; font-size: 30px">{m.get('headline', '')}</span><span style="flex-shrink: 0; padding: 14px 22px; border-radius: 12px; background: #F2EDE7; color: #0A0908; font-weight: 700; font-size: 24px">{m.get('cta', 'Más información')}</span></div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 14px; margin-top: -30px">{tags}</div>"""


def m_form(m):
    """{"type":"form","title":"Formulario de Meta","fields":[{"q":"...","a":"..."}],"badge":"✓ LEAD CUALIFICADO"}"""
    out = f'<div style="position: relative; {CARD}; padding: 44px 40px; display: flex; flex-direction: column; gap: 26px; {TILT}">{ej()}'
    out += f'<span style="{BRIC}; font-weight: 800; font-size: 38px">{m.get("title", "Formulario")}</span>'
    t = 1.3
    for f in m['fields']:
        a = f['a']
        dur = max(.5, len(a) * .05)
        out += (f'<div style="display: flex; flex-direction: column; gap: 10px; animation: aIn .5s ease-out {t - .3:.2f}s both"><span style="font-size: 26px; color: #9C938B">{f["q"]}</span>'
                f'<div style="padding: 22px 26px; border-radius: 18px; border: 2px solid rgba(255,106,26,.5); background: #171412; font-size: 32px; font-weight: 600"><span style="display: inline-block; white-space: nowrap; animation: aType {dur:.2f}s steps({max(6, len(a))}, end) {t:.2f}s both">{a}</span></div></div>')
        t += dur + .35
    if m.get('badge'):
        out += f'<span style="align-self: flex-start; padding: 14px 22px; border-radius: 16px; background: rgba(53,208,127,0.14); color: #35D07F; {MONO}; font-weight: 600; font-size: 24px; letter-spacing: 0.06em; animation: aPop .6s cubic-bezier(.2,.8,.2,1) {t + .1:.2f}s both, aPingG 1.6s ease-out {t + .7:.2f}s infinite">{m["badge"]}</span>'
    return out + '</div>'


def m_compare(m):
    """{"type":"compare","bad_t":"Así no","bad":["..."],"good_t":"Así sí","good":["..."]}"""
    def col(t, items, good, start):
        rows = ''
        for i, it in enumerate(items):
            dl = start + i * .4
            mark = ico_ok(dl + .2, 48) if good else (f'<span style="flex-shrink: 0; width: 48px; height: 48px; border-radius: 99px; background: #2A2623; display: flex; align-items: center; justify-content: center; color: #9C938B; font-size: 28px; font-weight: 800">✕</span>')
            strike = '' if good else f'<span style="position: absolute; left: 0; top: 52%; height: 3px; background: #9C938B; animation: aStrike .4s ease-out {dl + .5:.2f}s both"></span>'
            rows += (f'<div style="display: flex; align-items: center; gap: 20px; animation: aIn .5s ease-out {dl:.2f}s both">{mark}'
                     f'<span style="position: relative; font-size: 32px; font-weight: 600; color: {"#F2EDE7" if good else "#9C938B"}">{it}{strike}</span></div>')
        border = 'rgba(255,106,26,.55)' if good else 'rgba(242,237,231,.1)'
        return (f'<div style="position: relative; border-radius: 36px; background: rgba(18,16,15,0.92); border: 1px solid {border}; padding: 34px 36px; display: flex; flex-direction: column; gap: 20px">'
                f'<span style="{MONO}; font-size: 24px; letter-spacing: .14em; color: {"#FF6A1A" if good else "#9C938B"}">{t}</span>{rows}</div>')
    return (f'<div style="display: flex; flex-direction: column; gap: 24px; {TILT}">'
            + col(m.get('bad_t', 'ASÍ NO'), m['bad'], False, 1.2) + col(m.get('good_t', 'ASÍ SÍ'), m['good'], True, 1.4 + .4 * len(m['bad'])) + '</div>')


def m_bars(m):
    """{"type":"bars","title":"...","items":[{"label":"...","value":80,"hi":true}]}"""
    out = f'<div style="position: relative; {CARD}; padding: 44px 40px; display: flex; flex-direction: column; gap: 30px; {TILT}">{ej()}'
    out += f'<span style="{BRIC}; font-weight: 800; font-size: 36px">{m.get("title", "")}</span>'
    for i, it in enumerate(m['items']):
        dl = 1.2 + i * .35
        col = 'linear-gradient(90deg,#FF6A1A,#FFB27A)' if it.get('hi') else '#3A342F'
        out += (f'<div style="display: flex; flex-direction: column; gap: 10px"><span style="font-size: 28px; font-weight: 600; color: {"#F2EDE7" if it.get("hi") else "#9C938B"}">{it["label"]}</span>'
                f'<div style="height: 34px; border-radius: 99px; background: #1E1A17; overflow: hidden"><div style="height: 100%; width: {it["value"]}%; border-radius: 99px; background: {col}; '
                f'{"box-shadow: 0 0 20px rgba(255,106,26,.6);" if it.get("hi") else ""} animation: aGrowW 1.4s cubic-bezier(.2,.8,.2,1) {dl:.2f}s both"></div></div></div>')
    return out + '</div>'


def m_script(m):
    """{"type":"script","title":"Guion de apertura","lines":["...","...","..."]}"""
    out = f'<div style="position: relative; {CARD}; padding: 44px 40px; display: flex; flex-direction: column; gap: 18px; {TILT}">{ej()}'
    out += f'<span style="{MONO}; font-size: 22px; letter-spacing: .14em; color: #FF6A1A">{m.get("title", "GUION")}</span>'
    for i, ln in enumerate(m['lines']):
        dl = 1.3 + i * 1.1
        out += (f'<div style="display: flex; gap: 20px; align-items: flex-start; padding: 22px 24px; border-radius: 20px; color: #6B635C; animation: aHi .4s ease-out {dl:.2f}s both">'
                f'<span style="{MONO}; font-size: 24px; color: #FF6A1A; padding-top: 6px">0{i + 1}</span><span style="font-size: 34px; font-weight: 600; line-height: 1.3">{ln}</span></div>')
    return out + '</div>'


MOCKS = {k[2:]: v for k, v in globals().items() if k.startswith('m_')}


def scene(i, sc):
    dur = sc.get('dur', 6.0)
    s = header(i, dur)
    kind = sc.get('kind', 'step')
    if kind == 'cta':
        s += '<div style="position: relative; display: flex; flex-direction: column; gap: 56px">\n'
        s += title(sc.get('label', 'RESUMEN'), ttl(sc['title']), sc.get('size', 104))
        s += m_checklist({'items': sc['items']})
        s += '</div>\n'
        s += f"""<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 28px; animation: aPop .7s cubic-bezier(.2,.8,.2,1) 2.3s both">
<div style="position: relative; overflow: hidden; width: 100%; box-sizing: border-box; text-align: center; padding: 44px; border-radius: 40px; background: linear-gradient(135deg,#FF6A1A,#FF8F45); color: #0A0908; {BRIC}; font-weight: 800; font-size: {sc.get('button_size', 62)}px; letter-spacing: -0.03em; animation: aBtn 1.6s ease-in-out 3s infinite">{sc.get('button', 'Síguenos para más tips')}<div style="position: absolute; top: -40%; left: 0; width: 160px; height: 180%; background: linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.6),rgba(255,255,255,0)); animation: aShine 2s ease-in-out 3s infinite"></div></div>
<span style="{MONO}; font-size: 30px; letter-spacing: 0.16em; color: #FF6A1A">@CEOS.GROWTH</span>
</div>
"""
        return s, dur
    gap = 70 if kind == 'hook' else 60
    s += f'<div style="position: relative; display: flex; flex-direction: column; gap: {gap}px">\n'
    s += title(sc.get('label', ''), ttl(sc['title']), sc.get('size', 150 if kind == 'hook' else 112), 'h1' if kind == 'hook' else 'h2')
    if sc.get('mock'):
        s += MOCKS[sc['mock']['type']](sc['mock']) + '\n'
    s += '</div>\n'
    if kind == 'hook':
        s += footer(sc.get('footer', 'Te lo explico en 3 pasos'), 2.4)
    elif sc.get('note'):
        s += mono_note(nt(sc['note']), 1.4)
    return s, dur


def main(spec_path, out):
    spec = json.load(open(spec_path))
    os.makedirs(out, exist_ok=True)
    durs = []
    for i, sc in enumerate(spec['scenes']):
        body, dur = scene(i, sc)
        open(os.path.join(out, f'R{i + 1}.dc.html'), 'w').write(HEAD2 + body + TAIL)
        durs.append(dur)
    json.dump(durs, open(os.path.join(out, 'durs.json'), 'w'))
    print('escenas', len(durs), durs)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
