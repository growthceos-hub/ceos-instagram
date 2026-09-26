#!/usr/bin/env python3
"""Piezas comunes de los reels de valor (estilo historias Ceos)."""
import os, sys





HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Reel</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;background:#0A0908}
@property --m{syntax:'<integer>';inherits:false;initial-value:0}
@property --s{syntax:'<integer>';inherits:false;initial-value:0}
@keyframes aLogo{0%,100%{filter:drop-shadow(0 0 8px rgba(255,106,26,.35))}50%{filter:drop-shadow(0 0 22px rgba(255,106,26,.8))}}
@keyframes aGlow{0%,100%{opacity:.8;transform:scale(1)}50%{opacity:1;transform:scale(1.06)}}
@keyframes aIn{from{opacity:0;transform:translateY(40px);filter:blur(10px)}to{opacity:1;transform:none;filter:blur(0)}}
@keyframes aPop{0%{opacity:0;transform:scale(.6)}60%{opacity:1;transform:scale(1.08)}100%{opacity:1;transform:scale(1)}}
@keyframes aPing{0%,100%{box-shadow:0 0 0 0 rgba(255,106,26,.55)}50%{box-shadow:0 0 0 18px rgba(255,106,26,0)}}
@keyframes aPingG{0%,100%{box-shadow:0 0 0 0 rgba(53,208,127,.55)}50%{box-shadow:0 0 0 18px rgba(53,208,127,0)}}
@keyframes aRing{0%{transform:scale(.8);opacity:.9}100%{transform:scale(1.9);opacity:0}}
@keyframes aFill{from{width:0}to{width:100%}}
@keyframes aNudge{0%,100%{transform:translateX(0)}50%{transform:translateX(12px)}}
@keyframes aBlue{0%,100%{stroke:#9C938B}}
@keyframes aTicks{from{stroke:#F2EDE7}to{stroke:#7FD3FF}}
@keyframes aSeen{0%,100%{opacity:.55}50%{opacity:1}}
@keyframes aMinK{from{--m:0}to{--m:4}}
@keyframes aSecK{from{--s:0}to{--s:59}}
@keyframes aArc{from{stroke-dashoffset:754}to{stroke-dashoffset:68}}
@keyframes aArcG{0%{stroke:#FF6A1A}100%{stroke:#35D07F}}
@keyframes aType{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes aDots{0%,100%{transform:translateY(0);opacity:.5}50%{transform:translateY(-8px);opacity:1}}
@keyframes aOnl{0%,78%{opacity:1}79%,97%{opacity:0}98%,100%{opacity:1}}
@keyframes aTyp{0%,78%{opacity:0}79%,96%{opacity:1}97%,100%{opacity:0}}
@keyframes aShow{from{opacity:0}to{opacity:1}}
@keyframes aHide{from{opacity:1}to{opacity:0}}
@keyframes aRail{from{height:0}to{height:100%}}
@keyframes aNode{0%{background:#12100F;border-color:rgba(242,237,231,.2);box-shadow:none;transform:scale(1)}50%{transform:scale(1.25)}100%{background:#FF6A1A;border-color:#FFB27A;box-shadow:0 0 30px rgba(255,106,26,.8);transform:scale(1)}}
@keyframes aRow{from{border-color:rgba(242,237,231,.1);background:rgba(18,16,15,.92)}to{border-color:rgba(255,106,26,.6);background:#1C130D}}
@keyframes aCheck{from{stroke-dashoffset:30}to{stroke-dashoffset:0}}
@keyframes aShine{0%{transform:translateX(-160%) skewX(-20deg)}55%,100%{transform:translateX(420%) skewX(-20deg)}}
@keyframes aBtn{0%,100%{transform:scale(1);box-shadow:0 20px 70px rgba(255,106,26,.45)}50%{transform:scale(1.03);box-shadow:0 20px 110px rgba(255,106,26,.75)}}
.mm{counter-reset:m var(--m) s var(--s)}
.mm::before{content:"0" counter(m) ":" counter(s,decimal-leading-zero)}
@media (prefers-reduced-motion:reduce){*{animation-duration:.01s!important;animation-iteration-count:1!important}}
</style>
</helmet>
<div style="width: 1080px; height: 1920px; box-sizing: border-box; padding: 240px 80px 330px; position: relative; overflow: hidden; background: #0A0908; color: #F2EDE7; font-family: 'Instrument Sans', sans-serif; display: flex; flex-direction: column; justify-content: space-between">
<div style="position: absolute; top: 600px; right: -500px; width: 1300px; height: 1300px; border-radius: 999px; background: radial-gradient(circle, rgba(255,106,26,0.3), rgba(255,106,26,0) 60%); animation: aGlow 5s ease-in-out infinite"></div>
"""

TAIL = """</div>
</x-dc>
</body>
</html>
"""

SER = "font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: #FF6A1A"
MONO = "font-family: 'JetBrains Mono', monospace"
BRIC = "font-family: 'Bricolage Grotesque', sans-serif"
CARD = "border-radius: 44px; background: rgba(18,16,15,0.92); border: 1px solid rgba(242,237,231,0.12); box-shadow: 0 60px 140px -40px rgba(0,0,0,0.9)"
TILT = "animation: aIn 1s cubic-bezier(.2,.8,.2,1) .4s both"
CHK = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#0A0908" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7" style="stroke-dasharray:30;animation: aCheck .4s ease-out {d}s both"></path></svg>'
TICKS = '<svg width="38" height="22" viewBox="0 0 40 24" aria-hidden="true"><path d="M2 13l7 7L22 5M16 18l2 2L35 3" fill="none" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" style="animation: aTicks .3s linear {d}s both"></path></svg>'


def header(i, dur):
    segs = ''
    for k in range(5):
        if k < i:
            fill = '<div style="height: 100%; width: 100%; background: #FF6A1A"></div>'
        elif k == i:
            fill = f'<div style="height: 100%; background: #FF6A1A; box-shadow: 0 0 12px #FF6A1A; animation: aFill {dur}s linear both"></div>'
        else:
            fill = ''
        segs += f'<div style="flex: 1; height: 8px; border-radius: 9px; background: rgba(242,237,231,0.14); overflow: hidden">{fill}</div>'
    return f"""<div style="position: relative; display: flex; flex-direction: column; gap: 26px">
<div style="display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; align-items: center; gap: 18px"><img src="/_blob/70b4b68a06f5599a991cdf05ef629fec" alt="Ceos Growth" style="width: 68px; height: 68px; display: block; animation: aLogo 5s ease-in-out infinite"><span style="{BRIC}; font-weight: 800; font-size: 36px; letter-spacing: -0.02em">Ceos Growth</span></div>
<span style="padding: 12px 22px; border-radius: 999px; background: #FF6A1A; color: #0A0908; {MONO}; font-weight: 600; font-size: 24px; letter-spacing: 0.1em">0{i+1} / 05</span>
</div>
<div style="display: flex; gap: 10px">{segs}</div>
</div>
"""


def title(label, html, size=112, tag='h2'):
    lab = f'<span style="{MONO}; font-size: 28px; letter-spacing: 0.14em; color: #FF6A1A">{label}</span>' if label else ''
    return f"""<div style="display: flex; flex-direction: column; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) .1s both">
{lab}<{tag} style="margin: 0; {BRIC}; font-weight: 800; font-size: {size}px; line-height: 0.94; letter-spacing: -0.055em">{html}</{tag}>
</div>
"""


def footer(txt, d=1.4):
    return f"""<div style="position: relative; display: flex; align-items: center; justify-content: center; gap: 18px; animation: aIn 1s cubic-bezier(.2,.8,.2,1) {d}s both">
<span style="{BRIC}; font-weight: 800; font-size: 46px; letter-spacing: -0.03em">{txt}</span>
<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#FF6A1A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; transform: rotate(90deg)"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>
</div>
"""


def mono_note(txt, d=1.2):
    return f'<p style="margin: 0; font-family: \'Instrument Serif\', serif; font-style: italic; font-size: 54px; line-height: 1.1; color: #D9D1C8; animation: aIn 1s cubic-bezier(.2,.8,.2,1) {d}s both">{txt}</p>\n'


def ej():
    return f'<span style="position: absolute; top: 26px; right: 30px; {MONO}; font-size: 20px; letter-spacing: 0.12em; color: #6B635C">EJEMPLO</span>'


