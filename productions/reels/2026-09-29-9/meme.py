import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw, ImageFilter

BLUE, WHITE, RED, GREEN, YEL = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88), (255, 204, 0)
DARK, PANEL, MUT, NAVY, LINE = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66), (40, 52, 78)
SKY = (120, 180, 255)

S1, S2, PUNCH = 2.3, 4.5, 6.3


def tag(g, x, y, txt, bg, fg=WHITE, s=28, anchor='l'):
    f = F(800, s); w = f.getlength(txt)
    x0 = x if anchor == 'l' else (x - w - 36 if anchor == 'r' else x - (w + 36) / 2)
    g.rounded_rectangle((x0, y - s * .9, x0 + w + 36, y + s * .9), int(s * .9), fill=bg)
    g.text((x0 + 18, y), txt, font=f, fill=fg, anchor='lm')


class Almacenamiento:
    POV = 'POV: por fin te animas a grabarte a cámara'
    DUR, PUNCH, FOCUS = 8.0, PUNCH, (480, 500)
    SFX = ['pop@0.1', 'tick@0.7', 'tick@1.3', 'boom@2.3', 'ding@2.9', 'pop@3.5', 'tick@3.9',
           'pop@4.5', 'pop@4.8', 'pop@5.1', 'tick@5.6', 'boom@6.3']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        if t < S2:
            self.camera(im, g, min(t, S1 - .01) if t >= S1 else t)
            if t >= S1:
                im = self.alert(im, t)
        else:
            self.gallery(im, ImageDraw.Draw(im), t)
        g = ImageDraw.Draw(im)
        if S2 - .12 <= t < S2 + .18:
            q = (t - S2 + .12) / .3
            x = int(BW * (1.2 - 1.4 * q))
            g.rectangle((x, 0, x + 60, BH), fill=BLUE)
        if t >= self.PUNCH - .35:
            self.punch(im, t)
        return im

    # ---------------------------------------------------------- 1. visor de cámara
    def camera(self, im, g, t):
        # "escena": pared degradada + persona
        for y in range(0, BH, 8):
            c = int(28 + 30 * y / BH)
            g.rectangle((0, y, BW, y + 8), fill=(c - 10, c, c + 26))
        sway = 6 * math.sin(t * 2.4)
        cx = BW // 2 + sway
        g.ellipse((cx - 230, 640, cx + 230, 1120), fill=(30, 60, 120))           # torso
        g.ellipse((cx - 105, 360, cx + 105, 600), fill=(222, 184, 150))           # cara
        g.chord((cx - 115, 340, cx + 115, 520), 180, 360, fill=(52, 36, 28))      # pelo
        g.ellipse((cx - 55, 450, cx - 35, 470), fill=DARK); g.ellipse((cx + 35, 450, cx + 55, 470), fill=DARK)
        mo = 8 + 10 * abs(math.sin(t * 11))
        g.ellipse((cx - 30, 530 - mo / 2, cx + 30, 530 + mo / 2), fill=(120, 40, 40))
        # rejilla
        for i in (1, 2):
            g.line([(BW * i // 3, 110), (BW * i // 3, BH - 120)], fill=(255, 255, 255, 60), width=2)
            g.line([(0, 110 + (BH - 230) * i // 3), (BW, 110 + (BH - 230) * i // 3)], fill=(90, 100, 120), width=2)
        # cuadro de enfoque
        k = pop(t / .4); s = int(150 + 60 * (1 - k))
        fx, fy = cx, 480
        g.rectangle((fx - s, fy - s, fx + s, fy + s), outline=YEL, width=4)
        # barra superior
        g.rectangle((0, 0, BW, 110), fill=(0, 0, 0))
        tag(g, 40, 55, '4K · 60', (40, 44, 56), s=26)
        blink = RED if int(t * 3) % 2 == 0 else (120, 20, 20)
        secs = t * 3.1
        g.rounded_rectangle((BW // 2 - 110, 30, BW // 2 + 110, 80), 12, fill=RED)
        g.text((BW // 2, 55), f'00:00:{int(secs):02d}', font=F(800, 32), fill=WHITE, anchor='mm')
        g.rounded_rectangle((BW - 150, 38, BW - 70, 72), 8, outline=WHITE, width=3)
        g.rectangle((BW - 144, 44, BW - 76, 66), fill=GREEN)
        g.rectangle((BW - 68, 48, BW - 62, 62), fill=WHITE)
        # barra inferior
        g.rectangle((0, BH - 120, BW, BH), fill=(0, 0, 0))
        g.text((BW // 2 - 200, BH - 60), 'VÍDEO', font=F(800, 26), fill=YEL, anchor='mm')
        g.ellipse((BW // 2 - 50, BH - 110, BW // 2 + 50, BH - 10), outline=WHITE, width=5)
        g.rounded_rectangle((BW // 2 - 24, BH - 84, BW // 2 + 24, BH - 36), 8, fill=blink)
        # pensamientos
        if t > .6:
            kk = pop((t - .6) / .3)
            if kk > .1: tag(g, 40, 170, 'Hoy sí. Toma 1.', BLUE, s=max(2, int(32 * kk)))
        if t > 1.25:
            kk = pop((t - 1.25) / .3)
            if kk > .1: tag(g, BW - 40, 245, 'me está saliendo top', (20, 30, 60), s=max(2, int(30 * kk)), anchor='r')

    # ---------------------------------------------------------- 2. alerta + almacenamiento
    def alert(self, base, t):
        d = t - S1
        im = base.filter(ImageFilter.GaussianBlur(14))
        im = Image.blend(im, Image.new('RGB', (BW, BH), (0, 0, 0)), .45)
        g = ImageDraw.Draw(im)
        sh = 10 * math.sin(d * 60) * max(0, 1 - d / .35)
        k = pop(d / .3)
        w, h = int(720 * k), int(560 * k)
        x0, y0 = BW // 2 - w // 2 + sh, 170 + (560 - h) // 2
        if k > .05:
            g.rounded_rectangle((x0, y0, x0 + w, y0 + h), 36, fill=(242, 244, 248))
        if k > .9:
            cx = BW // 2 + sh
            # icono disco lleno
            g.ellipse((cx - 50, 205, cx + 50, 305), fill=RED)
            g.text((cx, 255), '!', font=F(800, 70), fill=WHITE, anchor='mm')
            g.text((cx, 360), 'Almacenamiento lleno', font=F(800, 46), fill=DARK, anchor='mm')
            g.text((cx, 425), 'No se puede grabar vídeo.', font=F(600, 30), fill=(70, 78, 96), anchor='mm')
            g.text((cx, 465), 'Libera espacio en Ajustes.', font=F(600, 30), fill=(70, 78, 96), anchor='mm')
            # barra de almacenamiento que se llena
            fill = min(1, .7 + .3 * ease((d - .4) / .9))
            bx0, bx1, by = cx - 300, cx + 300, 520
            g.rounded_rectangle((bx0, by, bx1, by + 44), 22, fill=(214, 220, 232))
            segs = [(.62, (255, 179, 0)), (.18, (52, 199, 89)), (.12, BLUE), (.08, (175, 82, 222))]
            x = bx0; tot = (bx1 - bx0) * fill
            acc = 0
            for frac, col in segs:
                ww = min(frac * (bx1 - bx0), max(0, tot - acc))
                if ww > 2: g.rectangle((x, by, x + ww, by + 44), fill=col)
                x += ww; acc += ww
            g.rounded_rectangle((bx0, by, bx1, by + 44), 22, outline=(242, 244, 248), width=4)
            used = 64 * fill
            g.text((cx, 600), f'{used:,.1f} de 64 GB usados'.replace('.', ','), font=F(800, 30),
                   fill=RED if fill > .99 else DARK, anchor='mm')
            g.line([(x0 + 20, 650), (x0 + w - 20, 650)], fill=(210, 214, 224), width=3)
            g.line([(cx, 650), (cx, 730)], fill=(210, 214, 224), width=3)
            g.text((cx - 180, 690), 'Ajustes', font=F(800, 34), fill=BLUE, anchor='mm')
            g.text((cx + 180, 690), 'OK', font=F(700, 34), fill=BLUE, anchor='mm')
            if d > 1.0:
                kk = pop((d - 1.0) / .3)
                if kk > .1: tag(g, BW // 2, 800, 'Fotos: 41 GB… ¿¿de qué??', RED, s=max(2, int(34 * kk)), anchor='c')
            if d > 1.6:
                kk = pop((d - 1.6) / .3)
                if kk > .1: tag(g, BW // 2, 890, 'vale, borro 4 cosas y grabo', BLUE, s=max(2, int(32 * kk)), anchor='c')
        return im

    # ---------------------------------------------------------- 3. galería
    def gallery(self, im, g, t):
        d = t - S2
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.text((40, 55), 'Galería', font=F(800, 42), fill=WHITE, anchor='lm')
        g.text((BW - 40, 55), 'Seleccionar', font=F(700, 28), fill=BLUE, anchor='rm')
        albums = [('Capturas', '4.312', (70, 90, 130)), ('Memes de WhatsApp', '2.877', (60, 120, 90)),
                  ('Vídeos concierto 2019', '96', (120, 60, 110)), ('"Hola a todos" (toma 1)', '238', (40, 80, 160)),
                  ('Fotos del gato', '5.104', (140, 100, 50)), ('Tickets y facturas', '612', (90, 90, 100))]
        for i, (name, n, col) in enumerate(albums):
            k = pop((d - i * .14) / .3)
            if k <= .05: continue
            c, r = i % 2, i // 2
            x0, y0 = 40 + c * 450, 140 + r * 250
            w, h = int(430 * k), int(230 * k)
            g.rounded_rectangle((x0, y0, x0 + w, y0 + h), 22, fill=col)
            if k > .9:
                # mini miniaturas
                for j in range(4):
                    g.rounded_rectangle((x0 + 20 + j * 100, y0 + 22, x0 + 105 + j * 100, y0 + 110), 10,
                                        fill=tuple(min(255, v + 30 + 12 * j) for v in col))
                g.text((x0 + 22, y0 + 150), name, font=F(800, 27), fill=WHITE, anchor='lm')
                g.text((x0 + 22, y0 + 192), n + ' elementos', font=F(600, 24), fill=(220, 226, 238), anchor='lm')
                # decisión: casi todo "no, que igual lo necesito"
                dec = [(1.0, 'NO'), (1.15, 'NO'), (1.3, 'NO'), (1.45, 'NO'), (1.6, 'NO'), (1.75, 'NO')][i]
                if d > dec[0]:
                    kk = pop((d - dec[0]) / .25)
                    if kk > .1:
                        tag(g, x0 + w - 14, y0 + 150, 'NO', RED, s=max(2, int(26 * kk)), anchor='r')
        if d > .9:
            kk = pop((d - .9) / .3)
            if kk > .1:
                g.rounded_rectangle((40, 900, BW - 40, 980), 40, fill=(34, 44, 66))
                g.text((BW // 2, 940), 'No, eso igual lo necesito…', font=F(800, int(34 * min(1, kk)) or 1),
                       fill=WHITE, anchor='mm')

    # ---------------------------------------------------------- remate
    def punch(self, im, t):
        kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
        cw, ch = int(440 * kk), int(456 * kk); cx, cy = self.FOCUS
        lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 28, fill=WHITE + (255,))
        im.paste(l, (0, 0), l)
        if kk > .85:
            g = ImageDraw.Draw(im)
            g.rounded_rectangle((cx - 150, cy - 205, cx + 150, cy - 163), 21, fill=BLUE)
            g.text((cx, cy - 184), '40 MIN DESPUÉS', font=F(800, 24), fill=WHITE, anchor='mm')
            g.text((cx, cy - 118), 'Borrado:', font=F(800, 36), fill=NAVY, anchor='mm')
            g.text((cx, cy - 66), '3 memes', font=F(800, 60), fill=NAVY, anchor='mm')
            g.text((cx, cy - 2), 'Liberado: 2 MB', font=F(700, 32), fill=(90, 100, 120), anchor='mm')
            g.line([(cx - 180, cy + 44), (cx + 180, cy + 44)], fill=(220, 226, 238), width=3)
            g.text((cx, cy + 100), 'Mañana grabo.', font=F(800, 50), fill=RED, anchor='mm')
            g.text((cx, cy + 165), '(spoiler: no)', font=F(700, 28), fill=(90, 100, 120), anchor='mm')


NEW = {'p-almacenamiento': Almacenamiento}
