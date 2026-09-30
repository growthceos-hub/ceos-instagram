import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN, YEL = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88), (255, 204, 0)
DARK, PANEL, MUT, NAVY = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66)
SKIN, HAIR, SHIRT, SHIRT2 = (222, 184, 150), (52, 36, 28), (236, 240, 248), (200, 208, 224)

S1, S2, PUNCH = 2.5, 4.5, 6.3
TAKES = [0.2 + i * 0.22 for i in range(10)]   # 10 tomas en ~2,2 s


def tag(g, x, y, txt, bg, fg=WHITE, s=28, anchor='l'):
    f = F(800, s); w = f.getlength(txt)
    x0 = x if anchor == 'l' else (x - w - 36 if anchor == 'r' else x - (w + 36) / 2)
    g.rounded_rectangle((x0, y - s * .9, x0 + w + 36, y + s * .9), int(s * .9), fill=bg)
    g.text((x0 + 18, y), txt, font=f, fill=fg, anchor='lm')
    return x0 + w + 36


def check(g, cx, cy, r, col=GREEN):
    g.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
    g.line([(cx - r * .45, cy), (cx - r * .1, cy + r * .38), (cx + r * .5, cy - r * .35)], fill=WHITE, width=max(2, int(r * .22)))


def person(g, cx, cy, sc, talk=0.0, label=True):
    """Persona hablando a cámara con camisa blanca… y la etiqueta asomando por el cuello."""
    # torso + camisa
    g.ellipse((cx - 170 * sc, cy + 95 * sc, cx + 170 * sc, cy + 470 * sc), fill=SHIRT)
    g.line([(cx, cy + 120 * sc), (cx, cy + 470 * sc)], fill=SHIRT2, width=max(1, int(4 * sc)))
    for k in range(3):
        by = cy + (170 + 70 * k) * sc
        g.ellipse((cx - 7 * sc, by - 7 * sc, cx + 7 * sc, by + 7 * sc), fill=SHIRT2)
    # cuello
    g.rectangle((cx - 28 * sc, cy + 58 * sc, cx + 28 * sc, cy + 115 * sc), fill=SKIN)
    # la etiqueta (asoma por detrás del cuello, a la derecha)
    if label:
        g.polygon([(cx + 22 * sc, cy + 92 * sc), (cx + 64 * sc, cy + 70 * sc), (cx + 76 * sc, cy + 98 * sc), (cx + 36 * sc, cy + 116 * sc)],
                  fill=WHITE, outline=(190, 196, 210))
    # solapas
    g.polygon([(cx - 60 * sc, cy + 95 * sc), (cx, cy + 128 * sc), (cx - 22 * sc, cy + 170 * sc), (cx - 78 * sc, cy + 120 * sc)], fill=WHITE, outline=SHIRT2)
    g.polygon([(cx + 60 * sc, cy + 95 * sc), (cx, cy + 128 * sc), (cx + 22 * sc, cy + 170 * sc), (cx + 78 * sc, cy + 120 * sc)], fill=WHITE, outline=SHIRT2)
    # cabeza
    g.ellipse((cx - 72 * sc, cy - 82 * sc, cx + 72 * sc, cy + 82 * sc), fill=SKIN)
    g.chord((cx - 80 * sc, cy - 98 * sc, cx + 80 * sc, cy + 22 * sc), 180, 360, fill=HAIR)
    g.ellipse((cx - 36 * sc, cy - 6 * sc, cx - 22 * sc, cy + 8 * sc), fill=DARK)
    g.ellipse((cx + 22 * sc, cy - 6 * sc, cx + 36 * sc, cy + 8 * sc), fill=DARK)
    m = (6 + 14 * abs(math.sin(talk * 11))) * sc
    g.ellipse((cx - 22 * sc, cy + 34 * sc, cx + 22 * sc, cy + 34 * sc + m), fill=(120, 40, 45))


def framed(im, box, sc, pcy, talk=0.0, bgc=(24, 36, 64), r=16):
    """Persona recortada dentro de una caja (monitor / miniatura)."""
    x0, y0, x1, y1 = [int(v) for v in box]
    w, h = x1 - x0, y1 - y0
    t_ = Image.new('RGB', (w, h), bgc); tg = ImageDraw.Draw(t_)
    person(tg, w / 2, pcy, sc, talk=talk)
    mk = Image.new('L', (w, h), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255)
    im.paste(t_, (x0, y0), mk)


class Etiqueta:
    POV = 'POV: grabas 10 tomas perfectas… y en todas se te ve la etiqueta de la camisa'
    DUR, PUNCH, FOCUS = 8.0, PUNCH, (480, 500)
    SFX = ['pop@0.1'] + [f'tick@{s:.2f}' for s in TAKES] + [
        'ding@2.35', 'pop@2.5', 'typing:0.9@2.7', 'ding@3.8', 'pop@4.5', 'pop@5.0',
        'tick@5.6', 'pop@5.9', 'boom@6.3']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK)
        if t < S1:
            self.viewer(im, ImageDraw.Draw(im), t)
        elif t < S2:
            self.edit(im, ImageDraw.Draw(im), t)
        else:
            self.chat(im, ImageDraw.Draw(im), t)
        g = ImageDraw.Draw(im)
        for S in (S1, S2):   # barrido azul de transición
            if S - .12 <= t < S + .18:
                q = (t - S + .12) / .3
                x = int(BW * (1.2 - 1.4 * q))
                g.rectangle((x, 0, x + 60, BH), fill=BLUE)
        if t >= self.PUNCH - .35:
            self.punch(im, t)
        return im

    # ---------------------------------------------------------- 1. visor: 10 tomas "perfectas"
    def viewer(self, im, g, t):
        for y in range(0, BH, 8):
            c = int(30 + 30 * y / BH)
            g.rectangle((0, y, BW, y + 8), fill=(c - 10, c + 4, c + 34))
        n = sum(1 for s in TAKES if t >= s)
        zoom = 1.0 + .06 * math.sin(t * 2.2)
        person(g, BW // 2 + 6 * math.sin(t * 2.6), 420, 1.75 * zoom, talk=t)
        for i in (1, 2):
            g.line([(BW * i // 3, 110), (BW * i // 3, BH - 120)], fill=(80, 92, 118), width=2)
            g.line([(0, 110 + (BH - 230) * i // 3), (BW, 110 + (BH - 230) * i // 3)], fill=(80, 92, 118), width=2)
        # marco de enfoque en la cara (verde = todo bien… supuestamente)
        k = pop(t / .4); s = int(125 + 40 * (1 - k))
        g.rectangle((BW // 2 - s, 420 - s, BW // 2 + s, 420 + s), outline=GREEN, width=4)
        # barra superior
        g.rectangle((0, 0, BW, 110), fill=(0, 0, 0))
        if int(t * 3) % 2 == 0: g.ellipse((40, 40, 70, 70), fill=RED)
        g.text((85, 55), 'REC', font=F(800, 30), fill=WHITE, anchor='lm')
        mm = int(t * 26)
        g.text((BW // 2, 55), f'00:{mm // 60:02d}:{mm % 60:02d}', font=F(800, 30), fill=WHITE, anchor='mm')
        tag(g, BW - 40, 55, '4K · 25p', BLUE, s=24, anchor='r')
        # contador de tomas gigante
        if n:
            kk = pop(min(1, (t - TAKES[n - 1]) / .12) * .6 + .4)
            f = F(800, int(64 * kk)); txt = f'TOMA {n}'
            w = f.getlength(txt) + 50
            g.rounded_rectangle((BW // 2 - w / 2, 140, BW // 2 + w / 2, 230), 45, fill=BLUE)
            g.text((BW // 2, 185), txt, font=f, fill=WHITE, anchor='mm')
        # sello de "perfecta" que salta en cada toma
        if n:
            d = t - TAKES[n - 1]
            kk = pop(d / .15)
            if kk > .1:
                sz = max(2, int(30 * kk))
                x1 = tag(g, 60, 790, '¡PERFECTA!', GREEN, fg=DARK, s=sz)
                check(g, x1 + 34, 790, int(24 * kk))
        # barra inferior: tomas buenas
        g.rectangle((0, BH - 120, BW, BH), fill=(0, 0, 0))
        for i in range(10):
            cx = 70 + i * 92
            if i < n: check(g, cx, BH - 60, 30)
            else: g.ellipse((cx - 30, BH - 90, cx + 30, BH - 30), outline=(70, 80, 100), width=4)

    # ---------------------------------------------------------- 2. montaje y exportación
    def edit(self, im, g, t):
        d = t - S1
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.text((40, 55), 'Montaje_final_DEFINITIVO.mp4', font=F(800, 34), fill=WHITE, anchor='lm')
        # monitor de previsualización
        framed(im, (120, 140, BW - 120, 560), 1.15 + .05 * math.sin(d * 3), 170, talk=t, r=20)
        g.rounded_rectangle((120, 140, BW - 120, 560), 20, outline=(60, 76, 110), width=4)
        # timeline con 10 clips
        g.rectangle((0, 600, BW, 780), fill=PANEL)
        for i in range(10):
            k = pop((d - i * .05) / .25)
            if k <= .05: continue
            x0 = 30 + i * 90; h = int(110 * k)
            g.rounded_rectangle((x0, 690 - h // 2, x0 + 84, 690 + h // 2), 10, fill=BLUE if i % 2 == 0 else (30, 90, 200))
            if k > .8: g.text((x0 + 42, 690), f'{i + 1}', font=F(800, 30), fill=WHITE, anchor='mm')
        ph = 30 + 900 * ease(d / 1.6)
        g.line([(ph, 610), (ph, 770)], fill=YEL, width=5)
        g.polygon([(ph - 12, 606), (ph + 12, 606), (ph, 624)], fill=YEL)
        # barra de exportación
        p = ease((d - .2) / 1.1)
        g.rounded_rectangle((60, 830, BW - 60, 880), 25, fill=(34, 44, 66))
        g.rounded_rectangle((60, 830, 60 + max(50, (BW - 120) * p), 880), 25, fill=GREEN if p >= 1 else BLUE)
        txt = 'EXPORTADO' if p >= 1 else f'Exportando… {int(p * 100)} %'
        g.text((BW // 2, 855), txt, font=F(800, 30), fill=WHITE, anchor='mm')
        if d > 1.35:
            kk = pop((d - 1.35) / .3)
            if kk > .1: tag(g, BW // 2, 945, 'Enviado al grupo para feedback', (34, 44, 66), s=max(2, int(30 * kk)), anchor='c')

    # ---------------------------------------------------------- 3. el grupo contesta
    def chat(self, im, g, t):
        d = t - S2
        g.rectangle((0, 0, BW, BH), fill=(12, 20, 38))
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.ellipse((40, 25, 100, 85), fill=BLUE)
        g.text((70, 55), 'A', font=F(800, 32), fill=WHITE, anchor='mm')
        g.text((125, 42), 'Amigos del cole', font=F(800, 32), fill=WHITE, anchor='lm')
        g.text((125, 78), 'escribiendo…' if d < 1.6 else 'en línea', font=F(600, 22), fill=GREEN, anchor='lm')
        # vídeo enviado (derecha)
        g.rounded_rectangle((BW - 430, 140, BW - 40, 420), 22, fill=BLUE)
        framed(im, (BW - 415, 155, BW - 55, 380), .8, 85)
        g.ellipse((BW - 395, 310, BW - 345, 360), fill=(0, 0, 0))
        g.polygon([(BW - 380, 322), (BW - 380, 348), (BW - 355, 335)], fill=WHITE)
        g.text((BW - 60, 400), '18:42', font=F(600, 20), fill=WHITE, anchor='rm')
        msgs = [(.25, '¡Qué bien hablas!', WHITE, DARK), (.75, 'Pero…', WHITE, DARK),
                (1.2, '¿qué es eso blanco del cuello?', WHITE, DARK)]
        y = 470
        for ts, txt, bg, fg in msgs:
            kk = pop((d - ts) / .28)
            if kk > .1:
                f = F(800 if ts > 1 else 700, max(2, int(34 * min(1, kk))))
                w = f.getlength(txt) + 50
                g.rounded_rectangle((40, y, 40 + w, y + 80), 24, fill=bg)
                g.text((65, y + 40), txt, font=f, fill=fg, anchor='lm')
            y += 100
        # círculo rojo sobre la etiqueta en la miniatura
        if d > 1.45:
            kk = pop((d - 1.45) / .3)
            cx, cy = BW - 235 + 40, 240 + 74
            r = int(42 * kk)
            if r > 3:
                g.ellipse((cx - r, cy - r, cx + r, cy + r), outline=RED, width=7)

    # ---------------------------------------------------------- remate
    def punch(self, im, t):
        kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
        lg.rectangle((0, 0, BW, BH), fill=(4, 8, 18, int(215 * min(1, max(0, kk)))))
        cw, ch = int(460 * kk), int(500 * kk); cx, cy = self.FOCUS
        lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 28, fill=WHITE + (255,))
        im.paste(l, (0, 0), l)
        if kk > .85:
            g = ImageDraw.Draw(im)
            g.rounded_rectangle((cx - 130, cy - 228, cx + 130, cy - 186), 21, fill=RED)
            g.text((cx, cy - 207), 'ZOOM x4', font=F(800, 26), fill=WHITE, anchor='mm')
            # etiqueta gigante
            g.polygon([(cx - 150, cy - 150), (cx + 140, cy - 165), (cx + 150, cy - 20), (cx - 140, cy - 5)],
                      fill=(248, 249, 252), outline=(180, 186, 200))
            g.text((cx, cy - 115), 'TALLA M', font=F(800, 40), fill=NAVY, anchor='mm')
            g.text((cx, cy - 65), 'Lavar a 30°', font=F(700, 28), fill=MUT, anchor='mm')
            g.line([(cx - 190, cy + 20), (cx + 190, cy + 20)], fill=(220, 226, 238), width=3)
            g.text((cx, cy + 80), 'En las 10.', font=F(800, 60), fill=RED, anchor='mm')
            g.text((cx, cy + 150), '(mañana se repite', font=F(700, 28), fill=(90, 100, 120), anchor='mm')
            g.text((cx, cy + 188), 'la grabación entera)', font=F(700, 28), fill=(90, 100, 120), anchor='mm')


NEW = {'p-etiqueta': Etiqueta}
