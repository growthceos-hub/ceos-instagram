#!/usr/bin/env python3
"""Música para los reels (sin efectos de UI). Uso: music.py salida.wav DUR DROP [SEMILLA]
El estilo cambia con la semilla (SEMILLA % 5): 0 épica/trap · 1 house · 2 cinemática · 3 synthwave · 4 phonk.
Con semilla = hueco + día del año, los 5 reels de un mismo día llevan 5 estilos distintos."""
import sys, numpy as np, wave
from scipy.signal import butter, sosfilt, fftconvolve

OUT, DUR, DROP = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
SEED = int(sys.argv[4]) if len(sys.argv) > 4 else 0
SR = 44100
STYLE = ['epica', 'house', 'cine', 'synth', 'phonk'][SEED % 5]
BPM = {'epica': 102, 'house': 124, 'cine': 92, 'synth': 108, 'phonk': 140}[STYLE]
BEAT = 60 / BPM
N = int(SR * (DUR + 2.5))
t_all = np.arange(N) / SR
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(3 + SEED)


def add(sig, start, gain=1.0, pan=0.0):
    i = int(start * SR)
    if i >= N: return
    sig = sig[:N - i]
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    L[i:i + len(sig)] += sig * gain * l * 1.414
    R[i:i + len(sig)] += sig * gain * r * 1.414


def lp(x, f, order=2):
    return sosfilt(butter(order, min(f, SR / 2 - 100) / (SR / 2), 'low', output='sos'), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f / (SR / 2), 'high', output='sos'), x)


def saw(f, n, phase=0.0):
    t = np.arange(n) / SR
    return 2 * ((f * t + phase) % 1) - 1


def adsr(n, a=.005, d=.1, s=.7, r=.1):
    t = np.arange(n) / SR; T = n / SR
    e = np.where(t < a, t / a, np.where(t < a + d, 1 - (1 - s) * (t - a) / d, s))
    rel = np.clip((T - t) / r, 0, 1)
    return e * rel


def note(n): return 440 * 2 ** ((n - 69) / 12)

# acordes (MIDI): Am  F  C  G  — progresión épica
PROGS = [  # (acordes MIDI, raíces) — progresiones épicas
    ([[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]], [45, 41, 48, 43]),   # Am F C G
    ([[53, 57, 60], [55, 59, 62], [57, 60, 64], [57, 60, 64]], [41, 43, 45, 45]),   # F G Am Am
    ([[57, 60, 64], [55, 59, 62], [53, 57, 60], [52, 56, 59]], [45, 43, 41, 40]),   # Am G F E
    ([[50, 53, 57], [53, 57, 60], [48, 52, 55], [55, 59, 62]], [38, 41, 48, 43]),   # Dm F C G
    ([[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 56, 59]], [45, 41, 43, 40]),   # Am F G E
]
CH, ROOT = PROGS[(SEED // 5 + SEED) % len(PROGS)]
BAR = 4 * BEAT
nbars = int((DUR + 2) / BAR) + 1

# ---------- sidechain (bombeo) tras el drop
side = np.ones(N)
k = 0
while k * BEAT < DUR + 2:
    tb = k * BEAT
    if tb >= DROP:
        i = int(tb * SR); m = int(BEAT * SR)
        tt = np.arange(m) / SR
        depth = {'epica': .25, 'house': .12, 'cine': .8, 'synth': .45, 'phonk': .35}[STYLE]
        n = len(side[i:i + m])  # el último pulso puede salirse del final
        side[i:i + n] = np.minimum(side[i:i + n], (depth + (1 - depth) * np.clip(tt / (BEAT * .55), 0, 1) ** 1.5)[:n])
    k += 1

# ---------- SUPERSAW acordes
pad = np.zeros(N); padR = np.zeros(N)
for b in range(nbars):
    st = b * BAR; n = int(BAR * SR) + int(.3 * SR)
    chord = CH[b % 4]
    sl = np.zeros(n); sr_ = np.zeros(n)
    for m in chord + [chord[0] + 12]:
        for d, pn in [(-0.18, -.8), (-0.08, -.4), (0, 0), (0.08, .4), (0.18, .8)]:
            s = saw(note(m) * 2 ** (d / 12), n, rng.random())
            sl += s * (1 - pn) / 2; sr_ += s * (1 + pn) / 2
    env = adsr(n, .45 if STYLE == 'cine' else .02, .2, .85, .3)
    if st < DROP:  # intro: filtrado y subiendo
        cut = 500 + 2500 * (st / DROP) ** 2
        g = .028
    else:
        cut = {'epica': 5200, 'house': 4200, 'cine': 2300, 'synth': 3600, 'phonk': 1600}[STYLE]
        g = {'epica': .06, 'house': .05, 'cine': .075, 'synth': .055, 'phonk': .035}[STYLE]
    sl = lp(sl * env, cut, 2); sr_ = lp(sr_ * env, cut, 2)
    i = int(st * SR); e = min(N, i + n)
    pad[i:e] += sl[:e - i] * g; padR[i:e] += sr_[:e - i] * g
L += pad * side; R += padR * side

# ---------- BAJO según estilo
for b in range(nbars):
    f = note(ROOT[b % 4] - 12)
    after = b * BAR >= DROP
    if STYLE == 'phonk' and after:  # 808 largo con caída de tono
        for x, ln in [(0, 1.5), (1.5, 1.0), (2.5, 1.5)]:
            st = b * BAR + x * BEAT
            if st > DUR + .3: break
            n = int(ln * BEAT * SR); tt = np.arange(n) / SR
            fr = f * (1 + .5 * np.exp(-tt * 40))
            sig = np.tanh(2.5 * np.sin(2 * np.pi * np.cumsum(fr) / SR)) * adsr(n, .003, .3, .8, .08)
            add(sig, st, .30)
        continue
    if STYLE == 'cine':  # notas largas graves
        n = int(BAR * SR); tt = np.arange(n) / SR
        sig = (np.sin(2 * np.pi * f * tt) * .8 + lp(saw(f, n), 400) * .3) * adsr(n, .08, .3, .9, .3)
        add(sig, b * BAR, .30 if after else .16)
        continue
    if not after:
        pat = [0, 1, 2, 3]
    elif STYLE == 'house':
        pat = [.5, 1.5, 2.5, 3.5]
    elif STYLE == 'synth':
        pat = [k * .5 for k in range(8)]
    else:
        pat = [k * .5 for k in range(8)]
    step = BEAT / 2 if after else BEAT
    for k, x in enumerate(pat):
        st = b * BAR + x * BEAT
        if st > DUR + .3: break
        ff = f * (2 if (STYLE == 'synth' and after and k % 2) else 1)
        n = int(step * SR * .95)
        tt = np.arange(n) / SR
        sub = np.sin(2 * np.pi * ff * tt)
        gr = np.tanh(3 * lp(saw(ff * 2, n), 900))
        sig = (sub * .8 + gr * .25) * adsr(n, .004, .08, .8, .05)
        add(sig, st, .32 if after else .18)

# ---------- MELODÍA / ARPEGIO según estilo
def cowbell(n):
    tt = np.arange(n) / SR
    return (np.sign(np.sin(2 * np.pi * 540 * tt)) + np.sign(np.sin(2 * np.pi * 800 * tt))) * np.exp(-tt * 14) * .5
for b in range(nbars):
    chord = CH[b % 4]
    tones = [chord[0] + 12, chord[1] + 12, chord[2] + 12, chord[0] + 24, chord[2] + 12, chord[1] + 12, chord[0] + 24, chord[2] + 24]
    if STYLE == 'phonk':
        for k, x in enumerate([0, .75, 1.5, 2, 2.75, 3.5]):
            st = b * BAR + x * BEAT
            if st > DUR - .2: break
            n = int(.25 * SR); tt = np.arange(n) / SR
            f = note(tones[(k * 3 + b) % 8])
            s_ = hp(np.sign(np.sin(2 * np.pi * f * tt)) * .6 + cowbell(n) * .5, 300) * np.exp(-tt * 12)
            add(s_, st, (.075 if st >= DROP else .05), pan=(-.25 if k % 2 else .25))
        continue
    div = 2 if STYLE in ('house', 'cine') else 4
    for k in range(4 * div):
        st = b * BAR + k * BEAT / div
        if st > DUR - .2: break
        if STYLE == 'house' and k % 2 == 0 and st >= DROP:
            continue  # pluck en contratiempo
        f = note(tones[k % 8] - (12 if STYLE == 'cine' else 0))
        n = int(.22 * SR); tt = np.arange(n) / SR
        if STYLE == 'synth':
            s_ = np.sign(np.sin(2 * np.pi * f * tt)) * .7 + saw(f * 1.005, n) * .3
            cut = 3400
        elif STYLE == 'cine':
            s_ = saw(f, n) * .7 + saw(f * 1.004, n) * .3
            cut = 1800
        else:
            s_ = saw(f, n) * .6 + np.sign(np.sin(2 * np.pi * f * 1.003 * tt)) * .4
            cut = 2600
        dec = 9 if STYLE == 'cine' else 16
        s_ = lp(s_, cut if st >= DROP else 1400 + (cut - 1400) * st / DROP) * np.exp(-tt * dec)
        acc = 1.0 if k % 4 == 0 else .7
        add(s_, st, (.085 if st >= DROP else .05) * acc, pan=(-.35 if k % 2 else .35))

# ---------- BATERÍA
def kick():
    n = int(.45 * SR); tt = np.arange(n) / SR
    f = 42 + 130 * np.exp(-tt * 28)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 6.5)
    click = rng.standard_normal(n) * np.exp(-tt * 300) * .3
    return np.tanh(2.2 * (s + click))

def clap():
    n = int(.35 * SR); tt = np.arange(n) / SR
    nz = hp(rng.standard_normal(n), 900)
    e = np.exp(-tt * 18) + .6 * np.exp(-np.maximum(tt - .012, 0) * 30) * (tt > .012)
    body = np.sin(2 * np.pi * 190 * tt) * np.exp(-tt * 25) * .5
    return nz * e * .55 + body

def hat(open_=False):
    n = int((.18 if open_ else .05) * SR); tt = np.arange(n) / SR
    return hp(rng.standard_normal(n), 7000) * np.exp(-tt * (18 if open_ else 80))

def tom(f):
    n = int(.6 * SR); tt = np.arange(n) / SR
    fr = f + f * .8 * np.exp(-tt * 20)
    return np.tanh(1.8 * np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-tt * 5))

def snare_big():
    n = int(.5 * SR); tt = np.arange(n) / SR
    nz = hp(rng.standard_normal(n), 700) * np.exp(-tt * 9) * (tt < .32)
    return nz * .6 + np.sin(2 * np.pi * 180 * tt) * np.exp(-tt * 20) * .5

K, C, H, HO, SB = kick(), clap(), hat(), hat(True), snare_big()
b = 0
while b * BAR < DUR + .5:
    base = b * BAR
    after = base >= DROP
    def at(x): return base + x * BEAT
    if STYLE == 'epica':
        if after:
            for x in [0, 1.5, 2, 2.75]: add(K, at(x), .55)
            add(C, at(1), .38, .1); add(C, at(3), .38, -.1)
            for k in range(16): add(HO if k % 8 == 6 else H, at(k / 4), (.10 if k % 2 == 0 else .06), .3)
            if b % 2 == 1:
                for k in range(6): add(H, at(3.5 + k / 12), .07, .3)
        else:
            for x, f in [(0, 70), (1.5, 70), (2, 90), (3, 60), (3.5, 60)]:
                if at(x) < DROP - .05: add(tom(f), at(x), .12 + .2 * (at(x) / DROP) ** 2)
    elif STYLE == 'house':
        if after:
            for x in range(4): add(K, at(x), .6)
            add(C, at(1), .36, .1); add(C, at(3), .36, -.1)
            for x in range(4): add(HO, at(x + .5), .09, .3)
            for k in range(16): add(H, at(k / 4), .035, -.3)
        else:
            for x in range(4):
                if at(x) < DROP - .05: add(lp(K, 300 + 1500 * (at(x) / DROP) ** 2), at(x), .35)
    elif STYLE == 'cine':
        for x, f in [(0, 65), (.75, 65), (1.5, 85), (2, 65), (2.5, 85), (3, 55), (3.5, 55), (3.75, 55)]:
            if at(x) < DUR: add(tom(f), at(x), (.42 if after else .12 + .25 * (at(x) / DROP) ** 2))
        if after:
            add(K, at(0), .5); add(SB, at(2), .42)
            if b % 2 == 0:
                n = int(1.6 * SR); tt = np.arange(n) / SR
                bb = np.tanh(1.4 * lp(sum(saw(note(ROOT[b % 4] - 12 + o) * 2 ** (d / 12), n) for o in (0, 12) for d in (-.12, .12)), 600)) * np.exp(-tt * 2)
                add(bb, at(0), .12)
    elif STYLE == 'synth':
        if after:
            for x in [0, 2, 2.5]: add(K, at(x), .55)
            add(SB, at(1), .45, .05); add(SB, at(3), .45, -.05)
            for k in range(8): add(H, at(k / 2), .08, .3)
        else:
            for k in range(8):
                if at(k / 2) < DROP - .05: add(H, at(k / 2), .03 + .05 * at(k / 2) / DROP, .3)
    else:  # phonk: medio tiempo, caja en el 3
        if after:
            for x in [0, .75, 2.5, 3.25]: add(K, at(x), .6)
            add(C, at(2), .5)
            for k in range(16): add(H, at(k / 4), (.09 if k % 2 == 0 else .05), .3)
            for k in range(8): add(H, at(3.5 + k / 16), .05, -.3)
        else:
            for k in range(8):
                if at(k / 2) < DROP - .05: add(H, at(k / 2), .04, .3)
    b += 1
# redoble de caja antes del drop
n_roll = 16
for k in range(n_roll):
    st = DROP - BEAT * 2 + k * (BEAT * 2 / n_roll)
    add(C, st, .08 + .3 * (k / n_roll) ** 2, 0)

# ---------- RISER + IMPACTO en el drop
n = int(2.2 * SR); tt = np.arange(n) / SR
nz = rng.standard_normal(n)
riser = np.zeros(n)
for j, seg in enumerate(np.array_split(np.arange(n), 20)):
    f = 400 + 7000 * (j / 20) ** 2
    riser[seg] = hp(nz, f)[seg]
riser *= (tt / tt[-1]) ** 2 * .22
add(riser, DROP - 2.2, 1.0)
up = saw(1, n)  # dummy
sw = np.sin(2 * np.pi * np.cumsum(110 * 2 ** (tt / tt[-1] * 2)) / SR) * (tt / tt[-1]) ** 2 * .08
add(sw, DROP - 2.2)
# impacto "braam": saws graves + ruido + sub
n = int(3 * SR); tt = np.arange(n) / SR
br = sum(saw(note(33 + o) * 2 ** (d / 12), n) for o in (0, 12) for d in (-.15, 0, .15))
br = np.tanh(1.5 * lp(br, 700)) * np.exp(-tt * 1.3) * (1.0 if STYLE in ('epica', 'cine') else .45)
boom = np.sin(2 * np.pi * np.cumsum(30 + 60 * np.exp(-tt * 6)) / SR) * np.exp(-tt * 2.2)
add(br * .22 + boom * .5 + hp(rng.standard_normal(n), 2000) * np.exp(-tt * 9) * .12, DROP, 1.0)
# golpe final
n = int(2.4 * SR); tt = np.arange(n) / SR
fin = np.sin(2 * np.pi * np.cumsum(32 + 70 * np.exp(-tt * 7)) / SR) * np.exp(-tt * 2) * .5
fin += np.tanh(1.5 * lp(sum(saw(note(45 + o), n) for o in (0, 7, 12)), 1200)) * np.exp(-tt * 1.6) * .15
add(fin, DUR - 1.9, 1.0)

# ---------- REVERB global (placa sencilla)
irn = int(1.8 * SR); ti = np.arange(irn) / SR
irL = rng.standard_normal(irn) * np.exp(-ti * 3.2); irR = rng.standard_normal(irn) * np.exp(-ti * 3.2)
irL /= np.sqrt((irL ** 2).sum()); irR /= np.sqrt((irR ** 2).sum())
wetL = fftconvolve(hp(L, 250), irL)[:N]; wetR = fftconvolve(hp(R, 250), irR)[:N]
L = L + wetL * .22; R = R + wetR * .22

# ---------- master
mix = np.stack([L, R])
mix = hp(mix, 28)
fade_in = np.clip(t_all / .05, 0, 1); fade_out = np.clip((DUR + 0.4 - t_all) / 1.0, 0, 1)
mix *= fade_in * fade_out
mix = mix[:, :int((DUR + .3) * SR)]
mix = np.tanh(mix * 1.25) / np.tanh(1.25)
mix /= np.abs(mix).max() / 0.93
pcm = (mix.T * 32767).astype('<i2')
w = wave.open(OUT, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
print('music ok', STYLE, BPM, round(DUR, 2))
