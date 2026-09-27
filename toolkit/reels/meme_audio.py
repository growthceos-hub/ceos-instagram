#!/usr/bin/env python3
"""Audio meme para reels POV (todo sintetizado, sin samples con derechos).
Uso: meme_audio.py salida.wav DUR CORTE [eventos]
- Base: marimba + pizzicato + palmas, alegre y botando (tipo "vídeo de meme").
- CORTE: en ese segundo la música se corta en seco con un golpe grave ("boom") y un zumbido.
- eventos: lista "tipo@segundo,..." con tipo pop | tick | typing:duración
"""
import sys, numpy as np, wave

OUT, DUR, CUT = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
EVENTS = sys.argv[4] if len(sys.argv) > 4 else ''
SR = 44100
N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)
BPM = 132; B = 60 / BPM


def put(sig, t, g=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N: return
    s = sig[:N - i] * g
    L[i:i + len(s)] += s * (1 - max(0, pan)); R[i:i + len(s)] += s * (1 + min(0, pan))


def hz(n): return 440 * 2 ** ((n - 69) / 12)


def marimba(n, d=.35):
    k = int(SR * d); t = np.arange(k) / SR; f = hz(n)
    return (np.sin(2 * np.pi * f * t) * np.exp(-t * 9) + .35 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 30)
            + .15 * np.sin(2 * np.pi * f * 10 * t) * np.exp(-t * 60))


def pizz(n, d=.25):
    k = int(SR * d); t = np.arange(k) / SR; f = hz(n)
    s = sum(np.sin(2 * np.pi * f * h * t) / h for h in (1, 2, 3, 4))
    return s * np.exp(-t * 14) * .6


def clap():
    k = int(SR * .15); t = np.arange(k) / SR
    nz = rng.standard_normal(k)
    env = np.exp(-t * 35) + .6 * np.exp(-np.maximum(0, t - .012) * 40) * (t > .012)
    return np.convolve(nz, np.ones(4) / 4, 'same') * env * .35


def hat():
    k = int(SR * .05); t = np.arange(k) / SR
    nz = rng.standard_normal(k); nz = nz - np.convolve(nz, np.ones(3) / 3, 'same')
    return nz * np.exp(-t * 90) * .25


def kick():
    k = int(SR * .25); t = np.arange(k) / SR
    f = 50 + 90 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 12) * .9


# progresión alegre: C  G  Am  F  (compás de 4 tiempos)
CH = [(48, [60, 64, 67]), (43, [59, 62, 67]), (45, [60, 64, 69]), (41, [60, 65, 69])]
MEL = [72, 76, 79, 76, 77, 76, 74, 72, 71, 74, 79, 74, 72, None, 76, 79,
       76, 72, 69, 72, 74, 72, 69, 67, 69, 72, 77, 76, 74, None, 72, None]
t = 0.0; step = 0
while t < CUT:
    bar = int(t / (4 * B)) % 4
    root, notes = CH[bar]
    s = step % 8
    if s % 2 == 0: put(pizz(root if s % 4 == 0 else root + 7), t, .9)
    if s in (0, 5): put(kick(), t, .8)
    if s in (2, 6): put(clap(), t, .9)
    put(hat(), t + B / 4, .6, .3 if s % 2 else -.3)
    if s in (1, 3, 6):
        for n in notes: put(marimba(n, .25), t, .18, -.2)
    m = MEL[step % len(MEL)]
    if m is not None and t > B * 4: put(marimba(m), t, .55, .15)
    t += B / 2; step += 1

# corte en seco: fundido de 20 ms en la música
cut_i = int(CUT * SR)
fade = int(.02 * SR)
env = np.ones(N); env[cut_i:cut_i + fade] = np.linspace(1, 0, min(fade, N - cut_i)); env[cut_i + fade:] = 0
L *= env; R *= env

# boom grave + cola
k = int(SR * 2.2); tt = np.arange(k) / SR
f = 38 + 120 * np.exp(-tt * 18)
boom = np.tanh(2.5 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.6))
boom += np.convolve(rng.standard_normal(k), np.ones(40) / 40, 'same') * np.exp(-tt * 25) * 1.5
put(boom, CUT, .95)
# zumbido de "silencio incómodo"
k = int(SR * max(.1, DUR - CUT - .4)); tt = np.arange(k) / SR
put(np.sin(2 * np.pi * 110 * tt) * .03 * np.minimum(1, tt / .5), CUT + .4, 1)

# efectos de chat (originales)
for ev in filter(None, EVENTS.split(',')):
    kind, at = ev.split('@'); at = float(at)
    if kind == 'pop':
        k = int(SR * .12); tt = np.arange(k) / SR
        f = 500 + 900 * (tt / .12)
        put(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 30) * .5, at, .8)
    elif kind == 'tick':
        for j, n in enumerate((84, 91)): put(marimba(n, .3), at + j * .08, .35)
    elif kind.startswith('typing'):
        d = float(kind.split(':')[1]); x = at
        while x < at + d:
            k = int(SR * .02); tt = np.arange(k) / SR
            put(rng.standard_normal(k) * np.exp(-tt * 300) * .12, x, 1, rng.uniform(-.3, .3))
            x += rng.uniform(.07, .16)

mix = np.stack([L, R], 1)
mix /= max(1e-9, np.abs(mix).max()) / .9
with wave.open(OUT, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype(np.int16).tobytes())
print('audio meme ok', DUR)
