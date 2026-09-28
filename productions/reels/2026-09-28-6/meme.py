import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88)
DARK, PANEL, MUT, NAVY = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66)
SKIN, SHIRT = (236, 196, 160), (232, 238, 250)

# Postura = (codo_izq, mano_izq, codo_der, mano_der) relativos al centro del pecho (hombros en ±95, -150)
POSES = [
    ('¿Normal?',           ((-120, -40), (-125, 70), (120, -40), (125, 70))),
    ('¿En los bolsillos?', ((-150, -40), (-70, 55), (150, -40), (70, 55))),
    ('¿Cruzadas?',         ((-140, -30), (60, -60), (140, -30), (-60, -40))),
    ('¿En jarra?',         ((-200, -60), (-110, 20), (200, -60), (110, 20))),
    ('¿Señalo algo?',      ((-120, -40), (-125, 70), (190, -200), (260, -300))),
    ('¿Tipo charla TED?',  ((-150, 0), (-45, -40), (150, 0), (45, -40))),
    ('¿Rezo?',             ((-110, -10), (-10, -120), (110, -10), (10, -120))),
    ('¿Tiranosaurio?',     ((-105, -40), (-70, -60), (105, -40), (70, -60))),
]
FINAL = ('BARRERA DE FALTA', ((-95, 10), (15, 80), (95, 10), (-15, 80)))


class Manos:
    POV = 'POV: le das a REC y de repente no sabes qué hacer con las manos'
    DUR, PUNCH, FOCUS = 7.6, 5.9, (480, 430)
    TIMES = [0.0, 0.75, 1.45, 2.1, 2.7, 3.3, 3.95, 4.6]
    SFX = ['tick@0.05', 'tick@0.75', 'tick@1.45', 'tick@2.1', 'tick@2.7', 'tick@3.3',
           'tick@3.95', 'tick@4.6', 'pop@5.55', 'boom@5.9']

    def pose(self, t):
        seq = [(ts, p) for ts, p in zip(self.TIMES, POSES)] + [(5.35, FINAL)]
        i = max(k for k, (ts, _) in enumerate(seq) if t >= ts)
        lab, cur = seq[i][1]
        if i == 0: return lab, cur, 1
        prev = seq[i - 1][1][1]; k = ease((t - seq[i][0]) / .22)
        mix = tuple(tuple(a + (b - a) * k for a, b in zip(pa, pb)) for pa, pb in zip(prev, cur))
        return lab, mix, k

    def person(self, g, cx, cy, pose, t):
        # cuerpo
        g.rounded_rectangle((cx - 120, cy - 170, cx + 120, cy + 260), 70, fill=SHIRT)
        g.polygon([(cx - 40, cy - 170), (cx, cy - 120), (cx + 40, cy - 170)], fill=(200, 212, 235))
        # cabeza con cara de pánico
        hy = cy - 250 + 4 * math.sin(t * 9)
        g.rectangle((cx - 28, cy - 200, cx + 28, cy - 160), fill=SKIN)
        g.ellipse((cx - 85, hy - 95, cx + 85, hy + 85), fill=SKIN)
        g.chord((cx - 88, hy - 100, cx + 88, hy + 20), 180, 360, fill=(58, 40, 30))
        for dx in (-32, 32):
            g.ellipse((cx + dx - 14, hy - 8, cx + dx + 14, hy + 20), fill=WHITE)
            g.ellipse((cx + dx - 6 + 4 * math.sin(t * 7), hy - 1, cx + dx + 6 + 4 * math.sin(t * 7), hy + 13), fill=DARK)
        g.arc((cx - 26, hy + 34, cx + 26, hy + 60), 200, 340, fill=(120, 60, 50), width=6)
        # gota de sudor
        sy = hy - 20 + (t * 60) % 50
        g.ellipse((cx + 80, sy, cx + 100, sy + 28), fill=(140, 200, 255))
        # brazos
        (el, hl, er, hr) = pose
        for sx, e, h in ((-95, el, hl), (95, er, hr)):
            s = (cx + sx, cy - 140); E = (cx + e[0], cy + e[1]); H = (cx + h[0], cy + h[1])
            O = (120, 150, 205); SL = (198, 216, 248)
            g.line([s, E], fill=O, width=54); g.ellipse((E[0] - 27, E[1] - 27, E[0] + 27, E[1] + 27), fill=O)
            g.line([E, H], fill=O, width=48)
            g.line([s, E], fill=SL, width=44); g.ellipse((E[0] - 22, E[1] - 22, E[0] + 22, E[1] + 22), fill=SL)
            g.line([E, H], fill=SL, width=38)
            g.ellipse((H[0] - 30, H[1] - 30, H[0] + 30, H[1] + 30), fill=(170, 120, 90))
            g.ellipse((H[0] - 26, H[1] - 26, H[0] + 26, H[1] + 26), fill=SKIN)

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        # fondo de estudio: degradado azul + focos
        for y in range(110, 720, 4):
            k = (y - 110) / 610
            g.rectangle((0, y, BW, y + 4), fill=(int(14 + 8 * k), int(32 + 14 * k), int(78 + 20 * (1 - k))))
        sw = 30 * math.sin(t * 1.4)
        g.ellipse((40 + sw, 150, 260 + sw, 370), fill=(28, 60, 130)); g.ellipse((700 - sw, 420, 900 - sw, 620), fill=(24, 52, 116))
        lab, pose, k = self.pose(t)
        shake = int(5 * math.sin(t * 50)) if 4.6 <= t < self.PUNCH else 0
        self.person(g, BW // 2 + shake, 470, pose, t)
        # suelo / recorte
        g.rectangle((0, 700, BW, 720), fill=(10, 18, 40))
        # esquinas del visor + tercios
        for x in (BW // 3, 2 * BW // 3): g.line([(x, 120), (x, 710)], fill=(60, 90, 150), width=2)
        for (x, y, dx, dy) in ((40, 140, 1, 1), (BW - 40, 140, -1, 1), (40, 690, 1, -1), (BW - 40, 690, -1, -1)):
            g.line([(x, y), (x + 60 * dx, y)], fill=WHITE, width=5); g.line([(x, y), (x, y + 60 * dy)], fill=WHITE, width=5)
        # etiqueta de la postura (pastilla)
        if t < self.PUNCH - .3:
            fnt = F(800, 50); tw = fnt.getlength(lab)
            l, lg = layer(); y = 648 + int(22 * (1 - k)); a = int(255 * min(1, .3 + k))
            col = RED + (a,) if lab == FINAL[0] else BLUE + (a,)
            lg.rounded_rectangle((BW / 2 - tw / 2 - 30, y - 42, BW / 2 + tw / 2 + 30, y + 42), 42, fill=col)
            lg.text((BW / 2, y), lab, font=fnt, fill=(255, 255, 255, a), anchor='mm')
            im.paste(l, (0, 0), l)
        # barra superior del visor
        g.rectangle((0, 0, BW, 110), fill=DARK)
        if int(t * 2.5) % 2 == 0 or t >= self.PUNCH: g.ellipse((36, 38, 70, 72), fill=RED)
        g.text((86, 55), 'REC', font=F(800, 34), fill=RED, anchor='lm')
        g.text((BW // 2, 55), f'00:00:{int(t * 1.6):02d}', font=F(800, 44), fill=WHITE, anchor='mm')
        g.text((BW - 40, 55), '4K · 25p', font=F(700, 30), fill=MUT, anchor='rm')
        # panel inferior: teleprompter atascado
        g.rectangle((0, 720, BW, BH), fill=PANEL); g.line([(0, 720), (BW, 720)], fill=(40, 52, 78), width=2)
        g.text((50, 765), 'TELEPROMPTER', font=F(700, 26), fill=MUT, anchor='lm')
        n = sum(1 for ts in self.TIMES if t >= ts)
        g.text((BW - 50, 765), f'POSTURAS PROBADAS: {min(n, 8) + (1 if t >= 5.35 else 0)}', font=F(800, 26), fill=BLUE, anchor='rm')
        g.text((50, 840), '“Hola, soy…”', font=F(800, 60), fill=WHITE, anchor='lm')
        cur = F(800, 60).getlength('“Hola, soy…”') + 62
        if int(t * 3) % 2 == 0: g.rectangle((cur, 810, cur + 6, 872), fill=BLUE)
        g.text((50, 930), 'Frase 1 de 12  ·  aún en la primera', font=F(700, 30), fill=MUT, anchor='lm')
        # remate
        if t >= self.PUNCH - .35:
            kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
            cw, ch = int(560 * kk), int(430 * kk); cx, cy = 480, 430
            lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 32, fill=WHITE + (255,))
            if kk > .85:
                lg.rounded_rectangle((cx - 180, cy - 185, cx + 180, cy - 131), 27, fill=RED + (255,))
                lg.text((cx, cy - 158), 'POSTURA ELEGIDA', font=F(800, 30), fill=WHITE, anchor='mm')
                lg.text((cx, cy - 70), 'Barrera', font=F(800, 84), fill=NAVY, anchor='mm')
                lg.text((cx, cy + 20), 'de falta', font=F(800, 84), fill=BLUE, anchor='mm')
                lg.text((cx, cy + 120), '“¿Así queda natural?”', font=F(700, 36), fill=(80, 90, 110), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


NEW = {'p-manos': Manos}
