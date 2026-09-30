import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw, ImageFilter

BLUE, WHITE, RED, GREEN, YEL = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88), (255, 204, 0)
DARK, PANEL, MUT, NAVY, LINE = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66), (40, 52, 78)
SKIN, HAIR, SHIRT = (222, 184, 150), (52, 36, 28), (30, 60, 120)

S1, S2, PUNCH = 2.4, 4.6, 6.3
SHOTS = [0.25 + i * 0.036 for i in range(60)]   # 60 disparos en ~2,1 s


def tag(g, x, y, txt, bg, fg=WHITE, s=28, anchor='l'):
    f = F(800, s); w = f.getlength(txt)
    x0 = x if anchor == 'l' else (x - w - 36 if anchor == 'r' else x - (w + 36) / 2)
    g.rounded_rectangle((x0, y - s * .9, x0 + w + 36, y + s * .9), int(s * .9), fill=bg)
    g.text((x0 + 18, y), txt, font=f, fill=fg, anchor='lm')


def face(g, cx, cy, sc, var=0, bg=None):
    """Persona posando. var cambia un pelín la pose (casi nada: es el chiste)."""
    tilt = [0, 2, -2, 1, -1, 3][var % 6] * sc
    smile = [10, 12, 9, 11, 13, 10][var % 6] * sc
    g.ellipse((cx - 150 * sc, cy + 92 * sc, cx + 150 * sc, cy + 420 * sc), fill=SHIRT)
    g.rectangle((cx - 26 * sc, cy + 60 * sc, cx + 26 * sc, cy + 110 * sc), fill=SKIN)
    g.ellipse((cx - 70 * sc + tilt, cy - 80 * sc, cx + 70 * sc + tilt, cy + 80 * sc), fill=SKIN)
    g.chord((cx - 78 * sc + tilt, cy - 95 * sc, cx + 78 * sc + tilt, cy + 25 * sc), 180, 360, fill=HAIR)
    ex = cx + tilt
    g.ellipse((ex - 36 * sc, cy - 6 * sc, ex - 22 * sc, cy + 8 * sc), fill=DARK)
    g.ellipse((ex + 22 * sc, cy - 6 * sc, ex + 36 * sc, cy + 8 * sc), fill=DARK)
    g.arc((ex - 28 * sc, cy + 20 * sc - smile, ex + 28 * sc, cy + 42 * sc + smile), 20, 160,
          fill=(150, 50, 50), width=max(2, int(6 * sc)))


def thumb(im, box, sc, var, bgc=(48, 58, 86), r=0):
    x0, y0, x1, y1 = [int(v) for v in box]
    w, h = x1 - x0, y1 - y0
    if w < 4 or h < 4: return
    t = Image.new('RGB', (w, h), bgc); tg = ImageDraw.Draw(t)
    face(tg, w / 2, h * .42, sc, var=var)
    mk = Image.new('L', (w, h), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255)
    im.paste(t, (x0, y0), mk)


class FotoPerfil:
    POV = 'POV: te haces 60 fotos para la foto de perfil… y acabas eligiendo la primera'
    DUR, PUNCH, FOCUS = 8.0, PUNCH, (480, 500)
    SFX = ['pop@0.1'] + [f'tick@{SHOTS[i]:.2f}' for i in range(0, 60, 6)] + [
        'ding@2.2', 'pop@2.4', 'pop@2.9', 'pop@3.4', 'tick@3.9', 'pop@4.3',
        'pop@4.6', 'tick@5.0', 'tick@5.4', 'pop@5.8', 'boom@6.3']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK)
        if t < S1:
            self.camera(im, ImageDraw.Draw(im), t)
        elif t < S2:
            self.gallery(im, ImageDraw.Draw(im), t)
        else:
            self.compare(im, ImageDraw.Draw(im), t)
        g = ImageDraw.Draw(im)
        for S in (S1, S2):   # barrido azul de transición
            if S - .12 <= t < S + .18:
                q = (t - S + .12) / .3
                x = int(BW * (1.2 - 1.4 * q))
                g.rectangle((x, 0, x + 60, BH), fill=BLUE)
        if t >= self.PUNCH - .35:
            self.punch(im, t)
        return im

    # ---------------------------------------------------------- 1. cámara en ráfaga
    def camera(self, im, g, t):
        for y in range(0, BH, 8):
            c = int(34 + 34 * y / BH)
            g.rectangle((0, y, BW, y + 8), fill=(c - 12, c, c + 30))
        n = sum(1 for s in SHOTS if t >= s)
        sway = 5 * math.sin(t * 3)
        face(g, BW // 2 + sway, 450, 2.0, var=n)
        # rejilla
        for i in (1, 2):
            g.line([(BW * i // 3, 110), (BW * i // 3, BH - 130)], fill=(90, 100, 120), width=2)
            g.line([(0, 110 + (BH - 240) * i // 3), (BW, 110 + (BH - 240) * i // 3)], fill=(90, 100, 120), width=2)
        k = pop(t / .4); s = int(130 + 50 * (1 - k))
        g.rectangle((BW // 2 - s - 30, 450 - s - 30, BW // 2 + s + 30, 450 + s + 30), outline=YEL, width=4)
        # barra superior
        g.rectangle((0, 0, BW, 110), fill=(0, 0, 0))
        tag(g, 40, 55, 'RETRATO', (40, 44, 56), fg=YEL, s=26)
        tag(g, BW - 40, 55, 'RÁFAGA', BLUE, s=26, anchor='r')
        # contador gigante de fotos
        if n:
            kk = pop(min(1, (t - SHOTS[n - 1]) / .08) * .6 + .4)
            f = F(800, int(64 * kk))
            txt = f'FOTO {n}'
            w = f.getlength(txt) + 50
            g.rounded_rectangle((BW // 2 - w / 2, 150, BW // 2 + w / 2, 240), 45, fill=RED if n >= 60 else (0, 0, 0))
            g.text((BW // 2, 195), txt, font=f, fill=WHITE, anchor='mm')
        # barra inferior con miniatura de la última
        g.rectangle((0, BH - 130, BW, BH), fill=(0, 0, 0))
        g.rounded_rectangle((50, BH - 105, 130, BH - 25), 12, fill=(60, 70, 96))
        if n: thumb(im, (50, BH - 105, 130, BH - 25), .22, n, r=12)
        g.ellipse((BW // 2 - 52, BH - 117, BW // 2 + 52, BH - 13), outline=WHITE, width=6)
        pressed = n and (t - SHOTS[n - 1]) < .02
        r = 38 if pressed else 44
        g.ellipse((BW // 2 - r, BH - 65 - r, BW // 2 + r, BH - 65 + r), fill=WHITE)
        g.text((BW - 90, BH - 65), 'FOTO', font=F(800, 26), fill=YEL, anchor='mm')
        # flash de cada disparo
        for s in SHOTS:
            if 0 <= t - s < .03:
                l, lg = layer(); lg.rectangle((0, 0, BW, BH), fill=(255, 255, 255, 90)); im.paste(l, (0, 0), l)
                break
        g = ImageDraw.Draw(im)
        for ts, txt, y, bgc, anc in [(.7, 'una más…', 300, BLUE, 'l'), (1.35, 'ahora con media sonrisa', 370, (20, 30, 60), 'r'),
                                     (1.95, 'la última, lo juro', 440, BLUE, 'l')]:
            if t > ts:
                kk = pop((t - ts) / .3)
                if kk > .1:
                    tag(g, 40 if anc == 'l' else BW - 40, y, txt, bgc, s=max(2, int(32 * kk)), anchor=anc)

    # ---------------------------------------------------------- 2. galería: 60 casi iguales
    def gallery(self, im, g, t):
        d = t - S1
        top = 120
        scroll = 520 * ease((d - .9) / 1.1)
        cols, cw = 4, BW // 4
        for i in range(24):
            c, r = i % cols, i // cols
            x0, y0 = c * cw + 3, top + r * cw + 3 - scroll
            if y0 > BH or y0 + cw < top: continue
            k = pop((d - i * .025) / .25)
            if k <= .05: continue
            sz = int((cw - 6) * k)
            ox, oy = x0 + (cw - 6 - sz) // 2, y0 + (cw - 6 - sz) // 2
            thumb(im, (ox, oy, ox + sz, oy + sz), .5 * sz / (cw - 6), i, bgc=(48 + (i % 3) * 3, 58, 86))
        # cabecera
        g.rectangle((0, 0, BW, top), fill=PANEL)
        g.text((40, 60), 'Recientes', font=F(800, 42), fill=WHITE, anchor='lm')
        n = min(60, int(60 * ease(d / .8)))
        tag(g, BW - 40, 60, f'{n} fotos · hace 2 min', (34, 44, 66), s=26, anchor='r')
        # marcas de indecisión
        if d > .45:
            kk = pop((d - .45) / .3)
            if kk > .1:
                g.rounded_rectangle((40, 830, BW - 40, 920), 45, fill=(34, 44, 66))
                g.text((BW // 2, 875), '“En la 14 salgo mejor… ¿o era la 15?”', font=F(800, max(2, int(32 * min(1, kk)))),
                       fill=WHITE, anchor='mm')
        if d > 1.3:
            kk = pop((d - 1.3) / .3)
            if kk > .1: tag(g, BW // 2, 960, 'Selecciona 12 finalistas', BLUE, s=max(2, int(32 * kk)), anchor='c')

    # ---------------------------------------------------------- 3. cara a cara de finalistas
    def compare(self, im, g, t):
        d = t - S2
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.text((BW // 2, 55), 'FINAL · ronda 7', font=F(800, 40), fill=WHITE, anchor='mm')
        pairs = [(14, 37), (37, 52), (52, 9)]
        idx = min(2, int(d / .6))
        a, b = pairs[idx]
        kk = pop(((d - idx * .6) / .25))
        for j, (num, x) in enumerate([(a, 250), (b, 710)]):
            sh = 0 if kk >= 1 else (1 - kk) * (-80 if j == 0 else 80)
            x0 = x - 210 + sh
            thumb(im, (x0, 170, x0 + 420, 650), 1.2, num, r=26)
            tag(g, x0 + 210, 610, f'FOTO {num}', BLUE if j == 0 else (20, 30, 60), s=30, anchor='c')
        g.text((BW // 2, 410), 'VS', font=F(800, 60), fill=YEL, anchor='mm')
        # la gota que colma: el amigo
        if d > .3:
            k2 = pop((d - .3) / .3)
            if k2 > .1:
                g.rounded_rectangle((40, 700, BW - 40, 800), 30, fill=(242, 244, 248))
                g.text((70, 750), 'Tú, al grupo:', font=F(800, max(2, int(30 * min(1, k2)))), fill=BLUE, anchor='lm')
                g.text((320, 750), '¿cuál os gusta más?', font=F(600, max(2, int(30 * min(1, k2)))), fill=DARK, anchor='lm')
        if d > 1.0:
            k3 = pop((d - 1.0) / .3)
            if k3 > .1:
                g.rounded_rectangle((40, 830, BW - 40, 930), 30, fill=(34, 44, 66))
                g.text((70, 880), 'Grupo:', font=F(800, max(2, int(30 * min(1, k3)))), fill=GREEN, anchor='lm')
                g.text((210, 880), '“son la misma foto”', font=F(700, max(2, int(32 * min(1, k3)))), fill=WHITE, anchor='lm')

    # ---------------------------------------------------------- remate
    def punch(self, im, t):
        kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
        lg.rectangle((0, 0, BW, BH), fill=(4, 8, 18, int(215 * min(1, max(0, kk)))))
        cw, ch = int(440 * kk), int(456 * kk); cx, cy = self.FOCUS
        lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 28, fill=WHITE + (255,))
        im.paste(l, (0, 0), l)
        if kk > .85:
            g = ImageDraw.Draw(im)
            g.rounded_rectangle((cx - 150, cy - 205, cx + 150, cy - 163), 21, fill=BLUE)
            g.text((cx, cy - 184), '2 HORAS DESPUÉS', font=F(800, 24), fill=WHITE, anchor='mm')
            thumb(im, (cx - 175, cy - 145, cx - 60, cy - 30), .32, 1, r=18)
            g.text((cx - 40, cy - 110), 'Foto de perfil:', font=F(700, 26), fill=(90, 100, 120), anchor='lm')
            g.text((cx - 40, cy - 62), 'FOTO 1', font=F(800, 52), fill=NAVY, anchor='lm')
            g.line([(cx - 180, cy + 5), (cx + 180, cy + 5)], fill=(220, 226, 238), width=3)
            g.text((cx, cy + 62), 'La primera.', font=F(800, 54), fill=RED, anchor='mm')
            g.text((cx, cy + 125), '(las otras 59, a la', font=F(700, 28), fill=(90, 100, 120), anchor='mm')
            g.text((cx, cy + 162), 'papelera… mañana)', font=F(700, 28), fill=(90, 100, 120), anchor='mm')


NEW = {'p-fotoperfil': FotoPerfil}
