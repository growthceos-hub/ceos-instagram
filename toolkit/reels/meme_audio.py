#!/usr/bin/env python3
"""Efectos de sonido para reels meme (sintetizados, sin samples con derechos). Sin música.
Uso: meme_audio.py salida.wav DUR eventos
eventos: "tipo@segundo,..." con tipo pop | tick | ding | boom | typing:dur | count:dur"""
import sys, numpy as np, wave

OUT, DUR = sys.argv[1], float(sys.argv[2])
EVENTS = sys.argv[3] if len(sys.argv) > 3 else ''
SR = 44100; N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N); rng = np.random.default_rng(7)


def put(sig, t, g=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N: return
    s = sig[:N - i] * g
    L[i:i + len(s)] += s * (1 - max(0, pan)); R[i:i + len(s)] += s * (1 + min(0, pan))


def tone(f, d, dec):
    t = np.arange(int(SR * d)) / SR
    return np.sin(2 * np.pi * f * t) * np.exp(-t * dec) + .3 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * dec * 3)


for ev in filter(None, EVENTS.split(',')):
    kind, at = ev.split('@'); at = float(at)
    if kind == 'pop':
        t = np.arange(int(SR * .12)) / SR; f = 500 + 900 * t / .12
        put(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30), at, .45)
    elif kind == 'tick':
        put(tone(1047, .3, 12), at, .3); put(tone(1568, .3, 12), at + .08, .3)
    elif kind == 'ding':
        put(tone(1319, .6, 7), at, .35); put(tone(988, .6, 7), at + .12, .35)
    elif kind == 'boom':
        t = np.arange(int(SR * 2.4)) / SR; f = 36 + 130 * np.exp(-t * 18)
        b = np.tanh(2.6 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.5))
        b += np.convolve(rng.standard_normal(len(t)), np.ones(40) / 40, 'same') * np.exp(-t * 25) * 1.5
        put(b, at, 1.0)
    elif kind.startswith('typing') or kind.startswith('count'):
        d = float(kind.split(':')[1]); x = at; typing = kind.startswith('typing')
        while x < at + d:
            k = int(SR * .02); t = np.arange(k) / SR
            s = rng.standard_normal(k) * np.exp(-t * 300) * .12 if typing else tone(2400, .03, 120) * .08
            put(s, x, 1, rng.uniform(-.3, .3)); x += rng.uniform(.07, .16) if typing else .06

mix = np.stack([L, R], 1); mix /= max(1e-9, np.abs(mix).max()) / .9
with wave.open(OUT, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype(np.int16).tobytes())
print('sfx ok', DUR)
