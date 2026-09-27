#!/usr/bin/env python3
"""Reel meme de Ceos Growth: fondo negro, cabecera tipo tweet, texto POV y clip en caja redondeada.
Uso: pov_reel.py salida_dir MEME [clip.mp4] [texto POV]
MEME = nombre en memes.py (visto, cunado, cuota) o "clip" para usar un vídeo propio (entonces hace falta texto POV).
Sin música: solo efectos (pop, ding, boom...). La música comercial se añade en la app al publicar."""
import os, sys, subprocess, math
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from memes import MEMES, F, wrap, ease, BW, BH
# Memes nuevos del día: MEMES_FILE=ruta/a/memes_dia.py (define clases y un dict NEW = {'nombre': Clase})
if os.environ.get('MEMES_FILE'):
    import importlib.util
    _sp = importlib.util.spec_from_file_location('memes_dia', os.environ['MEMES_FILE'])
    _m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
    MEMES.update(_m.NEW)

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, M = 1080, 1920, 30, 60
OUT, KIND = sys.argv[1], sys.argv[2]
CLIP = sys.argv[3] if KIND == 'clip' else None
meme = None if CLIP else MEMES[KIND]()
POV = sys.argv[4] if CLIP else (sys.argv[3] if len(sys.argv) > 3 else meme.POV)
TMP = os.path.join(OUT, '_tmp'); FR = os.path.join(TMP, 'f'); os.makedirs(FR, exist_ok=True)

# ---------- plantilla ----------
bg = Image.new('RGB', (W, H), 'black'); d = ImageDraw.Draw(bg)
pf = F(500, 50); lines = wrap(POV, pf, W - 2 * M); LH = 66
y0 = (H - (170 + len(lines) * LH + 40 + BH)) // 2 - 20
av = 118
# Marca: BRAND=productions -> cabecera "Ceos Productions" / @ceos.productions con su logo.
BRAND = os.environ.get('BRAND', 'growth')
BNAME, BHANDLE = ('Ceos Productions', '@ceos.productions') if BRAND == 'productions' else ('Ceos Growth', '@ceos.growth')
_lg = os.path.join(os.path.dirname(HERE), 'brands', BRAND, 'logo.png')
if not os.path.exists(_lg): _lg = os.path.join(os.path.dirname(HERE), 'logo.png')
logo = Image.open(_lg).convert('RGBA').resize((av, av), Image.LANCZOS)
circ = Image.new('RGBA', (av, av), (20, 18, 16, 255)); circ.alpha_composite(logo)
mk = Image.new('L', (av, av), 0); ImageDraw.Draw(mk).ellipse((0, 0, av - 1, av - 1), fill=255)
bg.paste(circ, (M, y0 + 6), mk)
nx = M + av + 26; nf = F(700, 44)
d.text((nx, y0 + 16), BNAME, font=nf, fill='white')
cx = nx + nf.getlength(BNAME) + 16; cy = y0 + 22
d.ellipse((cx, cy, cx + 38, cy + 38), fill=(29, 155, 240))
d.line([(cx + 10, cy + 20), (cx + 17, cy + 27), (cx + 29, cy + 12)], fill='white', width=5, joint='curve')
d.text((nx, y0 + 72), BHANDLE, font=F(500, 36), fill=(139, 139, 139))
ty = y0 + 170
for i, ln in enumerate(lines): d.text((M, ty + i * LH), ln, font=pf, fill='white')
BOX = (M, ty + len(lines) * LH + 40)
bmask = Image.new('L', (BW, BH), 0); ImageDraw.Draw(bmask).rounded_rectangle((0, 0, BW - 1, BH - 1), 40, fill=255)


def punch(im, t):
    """Remate meme: zoom de golpe al detalle + temblor + gris."""
    P = meme.PUNCH
    if t < P:
        z = 1 + .012 * math.sin(t * .8)
        big = im.resize((int(BW * z), int(BH * z)), Image.LANCZOS)
        ox, oy = (big.width - BW) // 2, int((big.height - BH) * .35)
        return big.crop((ox, oy, ox + BW, oy + BH))
    k = ease((t - P) / .1); z = 1 + 1.0 * k
    cw, ch = BW / z, BH / z; fx, fy = meme.FOCUS
    sh = 20 * math.exp(-(t - P) * 6); fx += sh * math.sin(t * 90); fy += sh * math.cos(t * 77)
    x0 = min(max(0, fx - cw / 2), BW - cw); y0_ = min(max(0, fy - ch / 2), BH - ch)
    im = im.crop((int(x0), int(y0_), int(x0 + cw), int(y0_ + ch))).resize((BW, BH), Image.LANCZOS)
    return Image.blend(im, im.convert('L').convert('RGB'), .65 * k)


if CLIP:
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', CLIP, '-t', '30', '-vf',
                    f'scale={BW}:{BH}:force_original_aspect_ratio=increase,crop={BW}:{BH},fps={FPS}',
                    os.path.join(FR, 'c%04d.png')], check=True)
    clips = sorted(f for f in os.listdir(FR) if f.startswith('c')); N = len(clips)
else:
    N = int(meme.DUR * FPS)
checks = {int(N * .3), int((meme.PUNCH - .3) * FPS) if meme else N // 2, N - 1}
for i in range(N):
    t = i / FPS
    c = Image.open(os.path.join(FR, clips[i])).convert('RGB') if CLIP else punch(meme.draw(t), t)
    fr = bg.copy(); fr.paste(c, BOX, bmask); fr.save(os.path.join(FR, f'{i:04d}.png'))
    if i in checks: fr.resize((540, 960)).save(os.path.join(TMP, f'check{i}.jpg'), quality=85)
    if i == int(N * .3): fr.save(os.path.join(OUT, 'portada.jpg'), quality=92)

dur = N / FPS
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', os.path.join(FR, '%04d.png')]
if CLIP:
    cmd += ['-i', CLIP, '-map', '0:v', '-map', '1:a?']
else:
    wav = os.path.join(TMP, 'sfx.wav')
    subprocess.run([sys.executable, os.path.join(HERE, 'meme_audio.py'), wav, str(dur), ','.join(meme.SFX)], check=True)
    cmd += ['-i', wav, '-map', '0:v', '-map', '1:a']
cmd += ['-t', str(dur), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium',
        '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', os.path.join(OUT, 'reel.mp4')]
subprocess.run(cmd, check=True)
print('OK', os.path.join(OUT, 'reel.mp4'), f'{dur:.1f}s')
