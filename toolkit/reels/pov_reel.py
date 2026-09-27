#!/usr/bin/env python3
"""Reel formato viral de Ceos Growth: fondo negro, cabecera tipo tweet, texto POV y clip en caja redondeada.
Uso: pov_reel.py salida_dir "texto POV" [clip.mp4]
Sin clip, genera un clip animado de chat (lead que deja en visto)."""
import os, sys, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.environ.get('POV_FONTS', os.path.join(HERE, 'fonts'))
F = lambda w, s: ImageFont.truetype(os.path.join(FONTS, f'M{w}.ttf'), s)
W, H, FPS = 1080, 1920, 30
OUT, POV = sys.argv[1], sys.argv[2]
CLIP = sys.argv[3] if len(sys.argv) > 3 else None
os.makedirs(OUT, exist_ok=True)
TMP = os.path.join(OUT, '_tmp'); os.makedirs(TMP, exist_ok=True)


def wrap(text, font, maxw):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if font.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    return lines


# ---------- plantilla (fondo) ----------
M = 60
bg = Image.new('RGB', (W, H), 'black')
d = ImageDraw.Draw(bg)
pov_f = F(500, 50)
lines = wrap(POV, pov_f, W - 2 * M)
LH = 66
BOX_W = W - 2 * M
BOX_H = 1000
block = 130 + 40 + len(lines) * LH + 40 + BOX_H
y0 = (H - block) // 2 - 20
# avatar
av = 118
logo = Image.open(os.path.join(os.path.dirname(HERE), 'logo.png')).convert('RGBA').resize((av, av), Image.LANCZOS)
circ = Image.new('RGBA', (av, av), (20, 18, 16, 255))
circ.alpha_composite(logo)
mask = Image.new('L', (av, av), 0); ImageDraw.Draw(mask).ellipse((0, 0, av - 1, av - 1), fill=255)
bg.paste(circ, (M, y0 + 6), mask)
nx = M + av + 26
name_f = F(700, 44)
d.text((nx, y0 + 16), 'Ceos Growth', font=name_f, fill='white')
# check azul
cx = nx + name_f.getlength('Ceos Growth') + 16; cy = y0 + 22
d.ellipse((cx, cy, cx + 38, cy + 38), fill=(29, 155, 240))
d.line([(cx + 10, cy + 20), (cx + 17, cy + 27), (cx + 29, cy + 12)], fill='white', width=5, joint='curve')
d.text((nx, y0 + 72), '@ceos.growth', font=F(500, 36), fill=(139, 139, 139))
ty = y0 + 130 + 40
for i, ln in enumerate(lines):
    d.text((M, ty + i * LH), ln, font=pov_f, fill='white')
BOX_Y = ty + len(lines) * LH + 40
BOX = (M, BOX_Y, M + BOX_W, BOX_Y + BOX_H)
bg.save(os.path.join(TMP, 'bg.png'))
boxmask = Image.new('L', (BOX_W, BOX_H), 0)
ImageDraw.Draw(boxmask).rounded_rectangle((0, 0, BOX_W - 1, BOX_H - 1), 40, fill=255)

# ---------- clip de chat ----------
C_BG, BAR, OUTB, INB = (11, 20, 26), (31, 44, 52), (0, 92, 75), (32, 44, 51)
GREY, BLUE, TXT = (134, 150, 160), (83, 189, 235), (233, 237, 239)
DUR = 10.0
MSGS = [(0.7, 'Hola Laura, soy de Ceos Growth.'),
        (1.7, 'Vi que pediste info hace un rato. ¿Te llamo hoy o mañana?')]
READ_T = 3.3
TYPING = [(4.0, 6.0), (7.0, 7.9)]
LAST_SEEN_T = 8.6
msg_f, small_f = F(500, 40), F(500, 26)


def ease(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3


def status(t):
    if any(a <= t < b for a, b in TYPING): return 'escribiendo...', (0, 168, 132)
    if t >= LAST_SEEN_T: return 'últ. vez hoy a las 11:42', GREY
    if t >= READ_T - .4: return 'en línea', GREY
    return 'toca para ver info', GREY


def chat_frame(t):
    im = Image.new('RGB', (BOX_W, BOX_H), C_BG)
    g = ImageDraw.Draw(im)
    # patrón suave
    for yy in range(160, BOX_H, 90):
        for xx in range((yy // 90 % 2) * 45, BOX_W, 90):
            g.ellipse((xx, yy, xx + 6, yy + 6), fill=(17, 27, 33))
    g.rectangle((0, 0, BOX_W, 150), fill=BAR)
    g.line([(52, 75), (36, 60), (52, 45)], fill=TXT, width=5)
    g.ellipse((72, 32, 158, 118), fill=(106, 127, 138))
    g.text((115, 75), 'L', font=F(700, 42), fill='white', anchor='mm')
    g.text((182, 34), 'Laura (formulario)', font=F(600, 38), fill=TXT)
    st, col = status(t)
    g.text((182, 86), st, font=small_f, fill=col)
    # burbujas
    y = 190
    for i, (ts, text) in enumerate(MSGS):
        if t < ts: continue
        k = ease((t - ts) / .35)
        ls = wrap(text, msg_f, 600)
        bw = max(msg_f.getlength(l) for l in ls) + 60
        bw = max(bw, 330)
        bh = len(ls) * 52 + 64
        x1 = BOX_W - 36; x0 = x1 - bw
        dy = int((1 - k) * 30)
        layer = Image.new('RGBA', (BOX_W, BOX_H), (0, 0, 0, 0))
        lg = ImageDraw.Draw(layer)
        a = int(255 * k)
        lg.rounded_rectangle((x0, y + dy, x1, y + bh + dy), 22, fill=OUTB + (a,))
        for j, l in enumerate(ls):
            lg.text((x0 + 28, y + 18 + j * 52 + dy), l, font=msg_f, fill=TXT + (a,))
        # hora + ticks
        tt = '11:3' + str(4 + i)
        tx = x1 - 64 - small_f.getlength(tt)
        lg.text((tx, y + bh - 42 + dy), tt, font=small_f, fill=(170, 200, 190, a))
        tc = BLUE if t >= READ_T else GREY
        bx, by = x1 - 56, y + bh - 30 + dy
        for o in (0, 12):
            lg.line([(bx + o, by + 4), (bx + o + 7, by + 11), (bx + o + 20, by - 4)], fill=tc + (a,), width=4)
        im.paste(layer, (0, 0), layer)
        y += bh + 18
    # burbuja escribiendo
    for a0, b0 in TYPING:
        if a0 <= t < b0:
            k = ease((t - a0) / .25) * ease((b0 - t) / .2)
            layer = Image.new('RGBA', (BOX_W, BOX_H), (0, 0, 0, 0))
            lg = ImageDraw.Draw(layer)
            A = int(255 * k)
            lg.rounded_rectangle((36, y + 10, 196, y + 94), 22, fill=INB + (A,))
            for n in range(3):
                ph = math.sin((t * 6) - n * .9)
                r = 9; cxx = 76 + n * 40; cyy = y + 52 - int(max(0, ph) * 10)
                lg.ellipse((cxx - r, cyy - r, cxx + r, cyy + r), fill=GREY + (int(A * (.55 + .45 * max(0, ph))),))
            im.paste(layer, (0, 0), layer)
    # barra de escribir
    g.rounded_rectangle((24, BOX_H - 104, BOX_W - 128, BOX_H - 24), 40, fill=INB)
    g.text((70, BOX_H - 64), 'Mensaje', font=F(500, 34), fill=GREY, anchor='lm')
    g.ellipse((BOX_W - 108, BOX_H - 104, BOX_W - 28, BOX_H - 24), fill=(0, 168, 132))
    # micro-zoom de cámara al quedar "en visto" para darle ritmo
    z = 1 + .05 * ease((t - LAST_SEEN_T) / .6) if t >= LAST_SEEN_T else 1 + .012 * math.sin(t * .8)
    if z != 1:
        zw, zh = int(BOX_W * z), int(BOX_H * z)
        big = im.resize((zw, zh), Image.LANCZOS)
        ox, oy = (zw - BOX_W) // 2, int((zh - BOX_H) * .35)
        im = big.crop((ox, oy, ox + BOX_W, oy + BOX_H))
    return im


frames_dir = os.path.join(TMP, 'f'); os.makedirs(frames_dir, exist_ok=True)
if CLIP:
    # clip real: recorte a la caja
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', CLIP, '-t', '30', '-vf',
                    f'scale={BOX_W}:{BOX_H}:force_original_aspect_ratio=increase,crop={BOX_W}:{BOX_H},fps={FPS}',
                    os.path.join(frames_dir, 'c%04d.png')], check=True)
    clips = sorted(f for f in os.listdir(frames_dir) if f.startswith('c'))
    N = len(clips)
else:
    N = int(DUR * FPS)
for i in range(N):
    fr = bg.copy()
    c = Image.open(os.path.join(frames_dir, clips[i])) if CLIP else chat_frame(i / FPS)
    fr.paste(c.convert('RGB'), BOX[:2], boxmask)
    fr.save(os.path.join(frames_dir, f'{i:04d}.png'))
    if i in (int(2.5 * FPS), int(5 * FPS), N - 1):
        fr.resize((540, 960)).save(os.path.join(TMP, f'check{i}.jpg'), quality=85)
    if i == int(5 * FPS):
        fr.save(os.path.join(OUT, 'portada.jpg'), quality=92)

dur = N / FPS
wav = os.path.join(TMP, 'm.wav')
music = os.path.join(HERE, 'music.py')
has_music = subprocess.run([sys.executable, music, wav, str(dur), '3.3', os.environ.get('SEED', '4')]).returncode == 0
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', os.path.join(frames_dir, '%04d.png')]
if CLIP and not has_music:
    cmd += ['-i', CLIP, '-map', '0:v', '-map', '1:a?']
elif has_music:
    cmd += ['-i', wav, '-map', '0:v', '-map', '1:a', '-af', f'afade=t=out:st={dur-1}:d=1,volume=0.8']
cmd += ['-t', str(dur), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium',
        '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', os.path.join(OUT, 'reel.mp4')]
subprocess.run(cmd, check=True)
print('OK', os.path.join(OUT, 'reel.mp4'), f'{dur:.1f}s')
