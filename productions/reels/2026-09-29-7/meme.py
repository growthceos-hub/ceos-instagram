import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN, YEL = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88), (255, 204, 0)
DARK, PANEL, MUT, NAVY, LINE = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66), (40, 52, 78)
SKY = (120, 180, 255)

REC_END = 2.1      # fin de la grabación
CMP_END = 4.3      # fin de la comparación
PUNCH = 6.3


def tag(g, x, y, txt, bg, fg=WHITE, s=28, anchor='l'):
    f = F(800, s); w = f.getlength(txt)
    x0 = x if anchor == 'l' else (x - w - 36 if anchor == 'r' else x - (w + 36) / 2)
    g.rounded_rectangle((x0, y - s * .9, x0 + w + 36, y + s * .9), int(s * .9), fill=bg)
    g.text((x0 + 18, y), txt, font=f, fill=fg, anchor='lm')


def wave(g, x0, x1, cy, t, amp, freq, col, width=10, gap=16, jitter=0.0, upto=None):
    n = int((x1 - x0) / gap)
    for i in range(n):
        x = x0 + i * gap
        if upto is not None and x > upto:
            col_i = LINE
        else:
            col_i = col
        a = amp * (.35 + .65 * abs(math.sin(i * freq + t * 7) * math.cos(i * .23 - t * 3)))
        a += jitter * amp * abs(math.sin(i * 2.7 + t * 31))
        a = max(6, min(a, amp * 1.25))
        g.rounded_rectangle((x - width / 2, cy - a, x + width / 2, cy + a), int(width / 2), fill=col_i)


class VozGrabada:
    POV = 'POV: escuchas tu voz grabada por primera vez'
    DUR, PUNCH, FOCUS = 8.0, PUNCH, (480, 500)
    SFX = ['pop@0.1', 'tick@0.6', 'tick@1.1', 'tick@1.6', 'pop@2.1', 'ding@2.6', 'pop@3.3', 'ding@3.7',
           'pop@4.3', 'typing:1.3@4.5', 'tick@5.9', 'boom@6.3']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        if t < REC_END:
            self.rec(im, g, t)
        elif t < CMP_END:
            self.compare(im, g, t)
        else:
            self.search(im, g, t)
        for tr in (REC_END, CMP_END):
            if tr - .12 <= t < tr + .18:
                q = (t - tr + .12) / .3
                x = int(BW * (1.2 - 1.4 * q))
                g.rectangle((x, 0, x + 60, BH), fill=BLUE)
        if t >= self.PUNCH - .35:
            self.punch(im, t)
        return im

    # ------------------------------------------------------------ 1. Grabadora
    def rec(self, im, g, t):
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.text((40, 55), 'Notas de voz', font=F(800, 40), fill=WHITE, anchor='lm')
        g.text((BW - 40, 55), 'Editar', font=F(700, 28), fill=BLUE, anchor='rm')
        # archivo
        g.text((BW // 2, 175), 'Presentación para la web', font=F(800, 40), fill=WHITE, anchor='mm')
        g.text((BW // 2, 225), 'Toma 1  ·  hoy', font=F(600, 26), fill=MUT, anchor='mm')
        # onda en vivo
        g.rounded_rectangle((40, 270, BW - 40, 560), 30, fill=PANEL)
        wave(g, 80, BW - 80, 415, t, 110, .55, BLUE, width=12, gap=20)
        g.line([(BW // 2, 285), (BW // 2, 545)], fill=RED, width=4)
        # contador
        secs = t * 4.2
        g.text((BW // 2, 612), f'00:{int(secs):02d},{int((secs % 1) * 100):02d}', font=F(800, 72), fill=WHITE, anchor='mm')
        # botón REC que late
        r = 62 + 6 * math.sin(t * 9)
        g.ellipse((BW // 2 - 82, 740 - 82, BW // 2 + 82, 740 + 82), outline=WHITE, width=6)
        g.rounded_rectangle((BW // 2 - r * .55, 740 - r * .55, BW // 2 + r * .55, 740 + r * .55), 14, fill=RED)
        # pastilla de grabación visible desde el fotograma 0
        blink = RED if int(t * 3) % 2 == 0 else (150, 30, 30)
        g.rounded_rectangle((BW // 2 - 140, 850, BW // 2 + 140, 900), 25, fill=(40, 16, 20))
        g.ellipse((BW // 2 - 118, 863, BW // 2 - 94, 887), fill=blink)
        g.text((BW // 2 - 78, 875), 'GRABANDO', font=F(800, 28), fill=WHITE, anchor='lm')
        # pensamientos
        if t > .5:
            k = pop((t - .5) / .3)
            if k > .1: tag(g, 50, 955, 'Esto va a quedar top', BLUE, s=max(2, int(28 * k)))
        if t > 1.2:
            k = pop((t - 1.2) / .3)
            if k > .1: tag(g, BW - 50, 955, 'voz de locutor, obvio', (34, 44, 66), s=max(2, int(28 * k)), anchor='r')

    # ------------------------------------------------------------ 2. Cabeza vs grabación
    def compare(self, im, g, t):
        d = t - REC_END
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.polygon([(BW // 2 - 250, 38), (BW // 2 - 250, 72), (BW // 2 - 222, 55)], fill=BLUE)
        g.text((BW // 2 + 20, 55), 'Reproduciendo · Toma 1', font=F(800, 34), fill=WHITE, anchor='mm')
        # panel 1: en tu cabeza
        g.rounded_rectangle((40, 140, BW - 40, 500), 30, fill=NAVY)
        g.text((80, 190), 'Tu voz en tu cabeza', font=F(800, 36), fill=WHITE, anchor='lm')
        tag(g, BW - 80, 190, 'grave · radio', BLUE, s=26, anchor='r')
        wave(g, 90, BW - 90, 340, t * .5, 95, .18, SKY, width=14, gap=22)
        g.text((BW // 2, 465), 'Tono: locutor de madrugada', font=F(700, 26), fill=SKY, anchor='mm')
        # panel 2: grabada
        k2 = pop((d - .5) / .3)
        if k2 > .05:
            g.rounded_rectangle((40, 530, BW - 40, 890), 30, fill=PANEL, outline=RED if d > 1.3 else LINE, width=4)
            g.text((80, 580), 'Tu voz grabada', font=F(800, 36), fill=WHITE, anchor='lm')
            if d > 1.0:
                kk = pop((d - 1.0) / .3)
                if kk > .1: tag(g, BW - 80, 580, '¿¿quién es??', RED, s=max(2, int(26 * kk)), anchor='r')
            playx = 90 + (BW - 180) * min(1, max(0, (d - .5) / 1.6))
            wave(g, 90, BW - 90, 730, t * 2.2, 60 * k2, 1.3, WHITE, width=8, gap=14, jitter=.8, upto=playx)
            g.line([(playx, 620), (playx, 840)], fill=RED, width=4)
            g.text((BW // 2, 860), 'Tono: ardilla con prisa', font=F(700, 26), fill=YEL, anchor='mm')
        # subtítulo de lo que se oye
        if d > 1.2:
            g.rectangle((0, 915, BW, BH), fill=DARK)
            txt = '«Hooola, eeeh… soy… bueno, que…»'
            n = int(len(txt) * min(1, (d - 1.2) / .7))
            g.text((BW // 2, 957), txt[:n], font=F(800, 34), fill=WHITE, anchor='mm')

    # ------------------------------------------------------------ 3. Búsqueda
    def search(self, im, g, t):
        d = t - CMP_END
        g.rectangle((0, 0, BW, BH), fill=(12, 18, 32))
        g.text((BW // 2, 120), 'Buscar', font=F(800, 64), fill=WHITE, anchor='mm')
        g.rounded_rectangle((40, 200, BW - 40, 290), 45, fill=WHITE)
        g.ellipse((80, 227, 116, 263), outline=MUT, width=5)
        g.line([(110, 257), (124, 271)], fill=MUT, width=5)
        q = 'por qué mi voz grabada suena así'
        n = int(len(q) * min(1, max(0, (d - .2) / 1.3)))
        g.text((145, 245), q[:n] + ('|' if int(t * 4) % 2 else ''), font=F(700, 32), fill=DARK, anchor='lm')
        sugg = ['¿los demás me oyen así de verdad?', 'cómo cambiar mi voz para siempre',
                'se puede grabar un vídeo sin hablar', 'voz de locutor en 5 minutos']
        for i, s in enumerate(sugg):
            k = pop((d - .5 - i * .28) / .3)
            if k <= .05: continue
            y = 350 + i * 118
            g.rounded_rectangle((40, y, BW - 40, y + 98), 22, fill=PANEL)
            g.ellipse((70, y + 32, 104, y + 66), outline=MUT, width=4)
            g.text((130, y + 49), s, font=F(700, int(32 * min(1, k)) or 1), fill=WHITE, anchor='lm')
            if i == 0 and d > 1.6:
                g.rounded_rectangle((40, y, BW - 40, y + 98), 22, outline=BLUE, width=6)
        # mano que duda
        if d > 1.6:
            k = pop((d - 1.6) / .3)
            if k > .1: tag(g, BW // 2, 880, 'Clic en la primera…', BLUE, s=max(2, int(34 * k)), anchor='c')

    # ------------------------------------------------------------ remate
    def punch(self, im, t):
        # el motor hace zoom x2 sobre FOCUS: todo cabe en 480x500 alrededor de (480, 500)
        kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
        cw, ch = int(440 * kk), int(456 * kk); cx, cy = self.FOCUS
        lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 28, fill=WHITE + (255,))
        im.paste(l, (0, 0), l)
        if kk > .85:
            g = ImageDraw.Draw(im)
            g.rounded_rectangle((cx - 165, cy - 205, cx + 165, cy - 163), 21, fill=BLUE)
            g.text((cx, cy - 184), 'RESPUESTA DESTACADA', font=F(800, 22), fill=WHITE, anchor='mm')
            g.text((cx, cy - 105), 'Sí.', font=F(800, 92), fill=NAVY, anchor='mm')
            g.text((cx, cy - 22), 'Los demás te oyen', font=F(800, 38), fill=NAVY, anchor='mm')
            g.text((cx, cy + 26), 'así', font=F(800, 38), fill=NAVY, anchor='mm')
            g.text((cx, cy + 80), 'desde siempre.', font=F(800, 42), fill=RED, anchor='mm')
            g.line([(cx - 180, cy + 128), (cx + 180, cy + 128)], fill=(220, 226, 238), width=3)
            g.text((cx, cy + 170), 'Todos. Todo este tiempo.', font=F(700, 26), fill=(90, 100, 120), anchor='mm')


NEW = {'p-voz-grabada': VozGrabada}
