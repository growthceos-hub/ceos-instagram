import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88)
DARK, PANEL, MUT = (8, 12, 22), (16, 22, 36), (130, 142, 165)


def mic(g, cx, cy, s, col, crossed=False, w=5):
    g.rounded_rectangle((cx - s * .35, cy - s, cx + s * .35, cy + s * .15), int(s * .35), outline=col, width=w)
    g.arc((cx - s * .65, cy - s * .55, cx + s * .65, cy + s * .55), 20, 160, fill=col, width=w)
    g.line([(cx, cy + s * .55), (cx, cy + s * .85)], fill=col, width=w)
    g.line([(cx - s * .35, cy + s * .85), (cx + s * .35, cy + s * .85)], fill=col, width=w)
    if crossed: g.line([(cx - s * .8, cy - s), (cx + s * .8, cy + s * .9)], fill=col, width=w + 2)


class MicApagado:
    POV = 'POV: te sale la toma perfecta a la primera… y el micro estaba apagado'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 425)
    SFX = ['tick@0.0', 'pop@1.1', 'pop@2.2', 'ding@3.2', 'tick@4.2', 'pop@5.0', 'boom@5.8']
    SUBS = [(0.0, '…y ese es el secreto'), (1.1, 'que nadie te cuenta.'), (2.2, '¡Nos vemos en el próximo!')]
    STOP, PLAY, WARN = 3.2, 4.2, 5.0

    def person(self, g, t, talking):
        # fondo de estudio azul con viñeta
        for y in range(110, 760, 4):
            k = (y - 110) / 650
            g.rectangle((0, y, BW, y + 4), fill=(int(14 + 10 * k), int(32 + 18 * k), int(70 + 30 * (1 - k))))
        # luz de fondo (softbox)
        g.ellipse((600, 170, 900, 470), fill=(30, 62, 130))
        g.ellipse((660, 230, 840, 410), fill=(44, 86, 170))
        bob = 4 * math.sin(t * 5)
        cx, cy = 440, 400 + bob
        g.rounded_rectangle((cx - 230, cy + 150, cx + 230, 800), 120, fill=(22, 30, 48))  # hombros
        g.polygon([(cx - 60, cy + 150), (cx, cy + 250), (cx + 60, cy + 150)], fill=(230, 236, 245))  # camisa
        g.rectangle((cx - 40, cy + 90, cx + 40, cy + 160), fill=(214, 170, 140))  # cuello
        g.ellipse((cx - 110, cy - 150, cx + 110, cy + 120), fill=(226, 184, 152))  # cara
        g.chord((cx - 118, cy - 165, cx + 118, cy + 40), 180, 360, fill=(52, 38, 30))  # pelo
        g.ellipse((cx - 55, cy - 20, cx - 25, cy + 8), fill=(40, 30, 26)); g.ellipse((cx + 25, cy - 20, cx + 55, cy + 8), fill=(40, 30, 26))
        m = abs(math.sin(t * 14)) if talking else 0
        g.rounded_rectangle((cx - 38, cy + 50, cx + 38, cy + 58 + int(26 * m)), 14, fill=(120, 50, 50))
        # micro de solapa (el culpable)
        g.ellipse((cx + 70, cy + 180, cx + 94, cy + 204), fill=(20, 20, 24))
        # brackets de enfoque
        f = 1 + .04 * math.sin(t * 6); w, h = 170 * f, 190 * f; col = GREEN if t < self.STOP else WHITE
        for sx in (-1, 1):
            for sy in (-1, 1):
                x, y = cx + sx * w, cy - 15 + sy * h
                g.line([(x, y), (x - sx * 40, y)], fill=col, width=5); g.line([(x, y), (x, y - sy * 40)], fill=col, width=5)
        # tercios
        for x in (BW // 3, 2 * BW // 3): g.line([(x, 110), (x, 760)], fill=(255, 255, 255), width=1)
        for y in (110 + 650 // 3, 110 + 2 * 650 // 3): g.line([(0, y), (BW, y)], fill=(255, 255, 255), width=1)

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        talking = t < self.STOP
        self.person(g, t, talking)
        # barra superior
        g.rectangle((0, 0, BW, 110), fill=DARK)
        if t < self.STOP:
            if int(t * 2.5) % 2 == 0: g.ellipse((36, 38, 70, 72), fill=RED)
            g.text((86, 55), 'REC', font=F(800, 34), fill=RED, anchor='lm')
            secs = 221 + int(t * 24)
        elif t < self.PLAY:
            g.rectangle((38, 40, 68, 70), fill=WHITE); g.text((86, 55), 'STOP', font=F(800, 34), fill=WHITE, anchor='lm')
            secs = 221 + int(self.STOP * 24)
        else:
            g.polygon([(40, 36), (40, 74), (72, 55)], fill=BLUE); g.text((86, 55), 'PLAY', font=F(800, 34), fill=BLUE, anchor='lm')
            secs = int((t - self.PLAY) * 40)
        g.text((BW // 2, 55), f'00:{secs // 60:02d}:{secs % 60:02d}', font=F(700, 40), fill=WHITE, anchor='mm')
        g.text((BW - 150, 55), '4K 25p', font=F(700, 28), fill=MUT, anchor='rm')
        g.rounded_rectangle((BW - 124, 38, BW - 50, 72), 8, outline=WHITE, width=3)
        g.rectangle((BW - 118, 44, BW - 76, 66), fill=GREEN); g.rectangle((BW - 48, 48, BW - 42, 62), fill=WHITE)
        # subtítulo de lo que dice (grabando)
        if talking:
            cur = [s for ts, s in self.SUBS if t >= ts][-1]
            ts = [ts for ts, s in self.SUBS if t >= ts][-1]; k = 1 if ts == 0 else ease((t - ts) / .2)
            l, lg = layer(); fnt = F(700, 40); tw = fnt.getlength(cur)
            y = 680 + int(20 * (1 - k))
            lg.rounded_rectangle((BW / 2 - tw / 2 - 24, y - 34, BW / 2 + tw / 2 + 24, y + 34), 16, fill=(0, 0, 0, int(170 * k)))
            lg.text((BW / 2, y), cur, font=fnt, fill=(255, 255, 255, int(255 * k)), anchor='mm')
            im.paste(l, (0, 0), l)
        # panel inferior: audio
        g.rectangle((0, 760, BW, BH), fill=PANEL)
        g.line([(0, 760), (BW, 760)], fill=(40, 52, 78), width=2)
        mic(g, 70, 858, 34, MUT, crossed=t >= self.WARN, w=5)
        for i, ch in enumerate(('CH1', 'CH2')):
            y = 810 + i * 70
            g.text((130, y + 12), ch, font=F(700, 26), fill=MUT, anchor='lm')
            for b in range(19):
                x = 200 + b * 28
                g.rounded_rectangle((x, y, x + 20, y + 24), 4, fill=(38, 46, 64))
            g.text((BW - 40, y + 12), 'SIN SEÑAL', font=F(700, 26), fill=MUT, anchor='rm')
        # fogonazo + TOMA PERFECTA
        if self.STOP <= t < self.PLAY + .6:
            fl = max(0, 1 - (t - self.STOP) / .25)
            if fl > 0:
                l, lg = layer(); lg.rectangle((0, 110, BW, 760), fill=(255, 255, 255, int(200 * fl))); im.paste(l, (0, 0), l)
            kk = pop((t - self.STOP) / .35); out = 1 - ease((t - self.PLAY) / .5) if t > self.PLAY else 1
            l, lg = layer(); cw, ch = int(640 * kk), int(200 * kk); cx, cy = BW // 2, 400
            a = int(250 * out)
            lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 34, fill=(255, 255, 255, a))
            if kk > .85:
                lg.ellipse((cx - 280, cy - 44, cx - 192, cy + 44), fill=GREEN + (a,))
                lg.line([(cx - 258, cy + 2), (cx - 240, cy + 22), (cx - 212, cy - 18)], fill=(255, 255, 255, a), width=9)
                lg.text((cx - 170, cy - 30), 'TOMA 1', font=F(600, 30), fill=(90, 100, 120, a), anchor='lm')
                lg.text((cx - 170, cy + 18), '¡PERFECTA!', font=F(800, 58), fill=(10, 20, 40, a), anchor='lm')
            im.paste(l, (0, 0), l)
        # reproducción: sin audio
        if t >= self.PLAY:
            k = ease((t - self.PLAY) / .3)
            l, lg = layer()
            lg.ellipse((BW // 2 - 70, 330, BW // 2 + 70, 470), fill=(0, 0, 0, int(140 * k)))
            lg.polygon([(BW // 2 - 22, 360), (BW // 2 - 22, 440), (BW // 2 + 40, 400)], fill=(255, 255, 255, int(255 * k)))
            # onda plana
            lg.rounded_rectangle((60, 640, BW - 60, 730), 18, fill=(0, 0, 0, int(160 * k)))
            lg.line([(90, 685), (BW - 90, 685)], fill=(120, 130, 150, int(255 * k)), width=4)
            px = 90 + (BW - 180) * min(1, (t - self.PLAY) / 3)
            lg.line([(px, 652), (px, 718)], fill=BLUE + (int(255 * k),), width=5)
            lg.text((BW - 100, 660), 'AUDIO', font=F(700, 22), fill=(160, 170, 190, int(255 * k)), anchor='rm')
            im.paste(l, (0, 0), l)
        if t >= self.WARN:
            kk = pop((t - self.WARN) / .3); l, lg = layer()
            cw, ch = int(440 * kk), int(320 * kk); cx, cy = 480, 425
            lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 34, fill=RED + (252,))
            if kk > .85:
                mic(lg, cx, cy - 95, 38, WHITE, crossed=True, w=7)
                lg.text((cx, cy + 10), 'MICRO', font=F(800, 66), fill=WHITE, anchor='mm')
                lg.text((cx, cy + 72), 'APAGADO', font=F(800, 66), fill=WHITE, anchor='mm')
                lg.text((cx, cy + 128), '0 segundos de audio', font=F(600, 28), fill=(255, 225, 222), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


NEW = {'p-micro-apagado': MicApagado}
