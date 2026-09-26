#!/usr/bin/env python3
"""Añade la capa de efectos "wow" a historias .dc.html (idempotente).
Uso: python3 toolkit/boost_story.py historia1.dc.html [historia2.dc.html ...]
"""
import random, re, sys

CSS = """
@keyframes fxOrbA{0%{transform:translate(0,0) scale(1)}50%{transform:translate(260px,380px) scale(1.25)}100%{transform:translate(0,0) scale(1)}}
@keyframes fxOrbB{0%{transform:translate(0,0) scale(1.1)}50%{transform:translate(-300px,-420px) scale(.85)}100%{transform:translate(0,0) scale(1.1)}}
@keyframes fxSpin{to{transform:rotate(360deg)}}
@keyframes fxSweep{0%{transform:translateX(-140%) rotate(18deg)}45%,100%{transform:translateX(160%) rotate(18deg)}}
@keyframes fxP{0%{transform:translateY(0) scale(.6);opacity:0}12%{opacity:1}85%{opacity:.9}100%{transform:translateY(-2100px) scale(1.2);opacity:0}}
@keyframes fxWord{from{opacity:0;transform:translateY(.55em) rotate(4deg) scale(.9);filter:blur(14px)}to{opacity:1;transform:none;filter:blur(0)}}
@keyframes fxTilt{from{opacity:0;transform:perspective(1600px) rotateX(28deg) translateY(120px) scale(.88);filter:blur(10px)}to{opacity:1;transform:perspective(1600px) rotateX(0) translateY(0) scale(1);filter:blur(0)}}
@keyframes fxFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-16px)}}
@keyframes fxPill{0%,100%{box-shadow:0 0 0 0 rgba(255,106,26,.6)}50%{box-shadow:0 0 0 12px rgba(255,106,26,0)}}
@keyframes fxGrid{from{background-position:0 0}to{background-position:0 180px}}
@keyframes fxFlash{0%{opacity:.55}100%{opacity:0}}
.fx-w{display:inline-block;animation:fxWord .9s cubic-bezier(.2,.8,.2,1) both}
"""


def particles(seed):
    rnd = random.Random(seed)
    out = []
    for _ in range(22):
        size = rnd.choice([6, 8, 10, 12, 16])
        left = rnd.randint(2, 98)
        dur = rnd.uniform(7, 13)
        delay = -rnd.uniform(0, dur)
        op = rnd.choice(['0.9', '0.7', '0.5'])
        out.append(f'<span style="position: absolute; left: {left}%; bottom: -40px; width: {size}px; height: {size}px; border-radius: 99px; '
                   f'background: rgba(255,{rnd.choice([106,140,178])},{rnd.choice([26,74,122])},{op}); box-shadow: 0 0 {size*2}px rgba(255,106,26,0.8); '
                   f'animation: fxP {dur:.1f}s linear {delay:.1f}s infinite"></span>')
    return ''.join(out)


def fx_layer(seed):
    return (
        '<div aria-hidden="true" style="position: absolute; inset: 0; overflow: hidden; pointer-events: none">'
        '<div style="position: absolute; left: 50%; top: 58%; width: 1700px; height: 1700px; margin: -850px 0 0 -850px; border-radius: 999px; '
        'background: conic-gradient(from 0deg, rgba(255,106,26,0) 0deg, rgba(255,106,26,0.16) 60deg, rgba(255,106,26,0) 140deg, rgba(255,178,122,0.1) 230deg, rgba(255,106,26,0) 320deg); '
        'animation: fxSpin 18s linear infinite"></div>'
        '<div style="position: absolute; left: -200px; top: 200px; width: 700px; height: 700px; border-radius: 999px; background: radial-gradient(circle, rgba(255,106,26,0.35), rgba(255,106,26,0) 65%); filter: blur(20px); animation: fxOrbA 11s ease-in-out infinite"></div>'
        '<div style="position: absolute; right: -240px; bottom: 120px; width: 800px; height: 800px; border-radius: 999px; background: radial-gradient(circle, rgba(255,140,60,0.28), rgba(255,106,26,0) 65%); filter: blur(24px); animation: fxOrbB 13s ease-in-out infinite"></div>'
        '<div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(242,237,231,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(242,237,231,0.045) 1px, transparent 1px); background-size: 90px 90px; animation: fxGrid 6s linear infinite; -webkit-mask-image: radial-gradient(circle at 50% 55%, #000 30%, transparent 75%); mask-image: radial-gradient(circle at 50% 55%, #000 30%, transparent 75%)"></div>'
        + particles(seed) +
        '<div style="position: absolute; top: -20%; bottom: -20%; left: 0; width: 38%; background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,200,160,0.10), rgba(255,255,255,0)); animation: fxSweep 5s ease-in-out 1.2s infinite"></div>'
        '<div style="position: absolute; inset: 0; background: radial-gradient(circle at 50% 40%, rgba(255,150,80,0.5), rgba(10,9,8,0) 60%); animation: fxFlash 1.2s ease-out both"></div>'
        '</div>'
    )


def words(html, start=0.15, step=0.07):
    """Envuelve cada palabra de texto en un span animado, respetando etiquetas."""
    parts = re.split(r'(<[^>]+>)', html)
    t = start
    out = []
    for p in parts:
        if p.startswith('<') or not p.strip():
            out.append(p)
            continue
        toks = re.split(r'(\s+)', p)
        for tok in toks:
            if not tok or tok.isspace():
                out.append(tok)
            else:
                out.append(f'<span class="fx-w" style="animation-delay: {t:.2f}s">{tok}</span>')
                t += step
    return ''.join(out)


def boost(path, seed):
    s = open(path).read()
    if 'fxSweep' in s:
        return
    s = s.replace('@media (prefers-reduced-motion', CSS + '@media (prefers-reduced-motion', 1)
    # capa de efectos justo después del div raíz
    m = re.search(r'<div style="width: 1080px; height: 1920px;[^"]*">\n', s)
    s = s[:m.end()] + fx_layer(seed) + '\n' + s[m.end():]
    # titular palabra a palabra
    hm = re.search(r'(<h[12][^>]*>)(.*?)(</h[12]>)', s, re.S)
    inner = words(hm.group(2))
    open_tag = re.sub(r'; animation: aIn[^";]*', '', hm.group(1))
    s = s[:hm.start()] + open_tag + inner + hm.group(3) + s[hm.end():]
    # el contenedor del titular ya no debe hacer blur a la vez
    s = s.replace('gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both', 'gap: 18px')
    # mockups: entrada 3D + flotación continua
    s = s.replace('animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both', 'animation: fxTilt 1.3s cubic-bezier(.2,.8,.2,1) .7s both, fxFloat 6s ease-in-out 2s infinite')
    s = s.replace('animation: aIn 1s cubic-bezier(.2,.8,.2,1) .5s both', 'animation: fxTilt 1.3s cubic-bezier(.2,.8,.2,1) .7s both, fxFloat 6s ease-in-out 2s infinite')
    # pastilla 0X / 05 con pulso
    s = s.replace('font-weight: 600; font-size: 24px; letter-spacing: 0.1em">0', 'font-weight: 600; font-size: 24px; letter-spacing: 0.1em; animation: fxPill 2s ease-out infinite">0', 1)
    open(path, 'w').write(s)
    print('boost', path)


if __name__ == '__main__':
    for i, p in enumerate(sys.argv[1:]):
        boost(p, i + 7)
