import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88)
DARK, PANEL, MUT, NAVY, LINE = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66), (40, 52, 78)

# (segundo, avatar, color, nombre, detalle)
VIEWS = [
    (0.0, 'M', (255, 120, 170), 'Mamá', 'le ha dado a me gusta'),
    (0.9, 'T', (255, 170, 60), 'Tía Mari', '"qué guapo sales hijo"'),
    (1.75, 'P', (90, 200, 250), 'Papá', 'desde el móvil de Mamá'),
    (2.6, 'P', (170, 130, 255), 'Tu primo', 'lo ha visto 1 segundo'),
    (3.45, 'T', (120, 140, 170), 'Tú', 'desde tu cuenta secundaria'),
    (4.3, 'M', (255, 120, 170), 'Mamá (otra vez)', 'lo ha compartido al grupo'),
]


class Familia:
    POV = 'POV: 3 horas editando tu reel… y las primeras visitas son de tu familia'
    DUR, PUNCH, FOCUS = 7.8, 6.0, (480, 470)
    SFX = ['pop@0.05', 'pop@0.9', 'pop@1.75', 'pop@2.6', 'pop@3.45', 'ding@4.3',
           'tick@5.2', 'tick@5.45', 'pop@5.65', 'boom@6.0']

    def n(self, t):
        return sum(1 for v in VIEWS if t >= v[0])

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        n = self.n(t)
        # ---- cabecera tipo "Estadísticas del reel"
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.line([(58, 75), (38, 55), (58, 35)], fill=WHITE, width=5)  # flecha atrás (arriba)
        g.text((BW // 2, 55), 'Estadísticas del reel', font=F(800, 40), fill=WHITE, anchor='mm')
        g.text((BW - 40, 55), f'hace {1 + int(t * 1.5)} min', font=F(700, 28), fill=MUT, anchor='rm')

        # ---- miniatura del reel con "timeline" de edición (3 h)
        tx, ty, tw, th = 40, 140, 250, 400
        for y in range(th):
            k = y / th
            g.line([(tx, ty + y), (tx + tw, ty + y)], fill=(int(20 + 30 * k), int(60 + 40 * k), int(150 + 80 * k)))
        mk = Image.new('L', (BW, BH), 255); ImageDraw.Draw(mk).rounded_rectangle((tx, ty, tx + tw, ty + th), 26, fill=0)
        bgc = Image.new('RGB', (BW, BH), DARK); cut = Image.new('L', (BW, BH), 0)
        ImageDraw.Draw(cut).rectangle((tx, ty, tx + tw, ty + th), fill=255)
        cut = Image.composite(cut, Image.new('L', (BW, BH), 0), mk)
        im.paste(bgc, (0, 0), cut); g = ImageDraw.Draw(im)
        # persona en la miniatura (silueta que respira)
        b = 4 * math.sin(t * 4)
        g.ellipse((tx + 85, ty + 120 + b, tx + 165, ty + 200 + b), fill=(236, 196, 160))
        g.rounded_rectangle((tx + 55, ty + 205 + b, tx + 195, ty + 330), 50, fill=(232, 238, 250))
        # play que late
        s = 1 + .08 * math.sin(t * 6); cx, cy = tx + tw // 2, ty + 70
        g.polygon([(cx - 18 * s, cy - 22 * s), (cx - 18 * s, cy + 22 * s), (cx + 24 * s, cy)], fill=WHITE)
        g.rounded_rectangle((tx + 14, ty + th - 58, tx + tw - 14, ty + th - 14), 22, fill=(8, 12, 22))
        g.text((tx + tw // 2, ty + th - 36), '3 h 12 min de edición', font=F(700, 20), fill=WHITE, anchor='mm')

        # ---- contador grande de reproducciones
        rx = 330
        g.text((rx, 150), 'REPRODUCCIONES', font=F(700, 28), fill=MUT)
        # el número "salta" al cambiar
        last = max([v[0] for v in VIEWS if t >= v[0]], default=-9)
        k = pop((t - last) / .3) if 0 < last and t - last < .3 else 1
        nf = F(800, int(190 * (0.8 + 0.2 * k)))
        g.text((rx, 280), str(n), font=nf, fill=WHITE, anchor='lm')
        g.text((rx + 10 + nf.getlength(str(n)) + 20, 300), 'visita' if n == 1 else 'visitas', font=F(700, 40), fill=BLUE, anchor='lm')
        # gráfica plana con latido
        gx0, gx1, gy = rx, BW - 40, 470
        g.rounded_rectangle((gx0, 390, gx1, 540), 22, fill=PANEL)
        g.text((gx0 + 24, 415), 'Alcance fuera de la familia', font=F(700, 24), fill=MUT, anchor='lm')
        pts = []
        prog = min(1, t / 5.6)
        for i in range(0, int(560 * prog) + 1, 8):
            x = gx0 + 24 + i
            y = gy + 30 - 3 * math.sin(i * .09 + t * 3)
            pts.append((x, y))
        if len(pts) > 1: g.line(pts, fill=BLUE, width=6)
        if pts: g.ellipse((pts[-1][0] - 9, pts[-1][1] - 9, pts[-1][0] + 9, pts[-1][1] + 9), fill=WHITE)
        g.text((gx1 - 24, 415), '0 %', font=F(800, 30), fill=RED, anchor='rm')

        # ---- lista "Quién lo ha visto" (desliza hacia arriba)
        g.rectangle((0, 570, BW, BH), fill=PANEL); g.line([(0, 570), (BW, 570)], fill=LINE, width=2)
        g.text((40, 612), 'QUIÉN LO HA VISTO', font=F(700, 26), fill=MUT, anchor='lm')
        g.text((BW - 40, 612), f'{n} de {n}: familia', font=F(800, 26), fill=BLUE, anchor='rm')
        RH, top = 96, 652
        vis = [v for v in VIEWS if t >= v[0]]
        # desplazamiento suave cuando hay más de 3 filas
        over = max(0, len(vis) - 3)
        if over:
            lk = ease((t - vis[-1][0]) / .35)
            off = (over - 1 + lk) * RH
        else:
            off = 0
        clip = Image.new('RGBA', (BW, BH), (0, 0, 0, 0)); cg = ImageDraw.Draw(clip)
        for i, (ts, ini, col, name, det) in enumerate(vis):
            kk = 1 if ts == 0 else ease((t - ts) / .3)
            y = top + i * RH - off + int((1 - kk) * 40); a = int(255 * kk)
            if y < top - RH or y > BH: continue
            cg.ellipse((40, y + 10, 116, y + 86), fill=col + (a,))
            cg.text((78, y + 48), ini, font=F(800, 36), fill=(255, 255, 255, a), anchor='mm')
            cg.text((140, y + 30), name, font=F(800, 38), fill=(255, 255, 255, a), anchor='lm')
            cg.text((140, y + 70), det, font=F(600, 26), fill=MUT + (a,), anchor='lm')
            if 'Mamá' in name:
                hx, hy = BW - 80, y + 48; hs = 1 + .15 * math.sin(t * 8)
                cg.ellipse((hx - 22 * hs, hy - 16 * hs, hx, hy + 6 * hs), fill=RED + (a,))
                cg.ellipse((hx, hy - 16 * hs, hx + 22 * hs, hy + 6 * hs), fill=RED + (a,))
                cg.polygon([(hx - 21 * hs, hy - 2), (hx + 21 * hs, hy - 2), (hx, hy + 24 * hs)], fill=RED + (a,))
        cm = Image.new('L', (BW, BH), 0); ImageDraw.Draw(cm).rectangle((0, 640, BW, BH), fill=255)
        clip.putalpha(Image.composite(clip.split()[3], Image.new('L', (BW, BH), 0), cm))
        im.paste(clip, (0, 0), clip)

        # ---- notificación antes del remate
        if 5.1 <= t < self.PUNCH:
            k = ease((t - 5.1) / .3); l, lg = layer(); y = int(-120 + 250 * k)
            lg.rounded_rectangle((40, y, BW - 40, y + 110), 28, fill=(245, 248, 255, 255))
            lg.ellipse((64, y + 22, 130, y + 88), fill=(255, 120, 170, 255))
            lg.text((97, y + 55), 'M', font=F(800, 32), fill=WHITE, anchor='mm')
            lg.text((150, y + 38), 'Mamá ha comentado:', font=F(800, 30), fill=NAVY, anchor='lm')
            lg.text((150, y + 78), '"¿Esto cómo se comparte por WhatsApp?"', font=F(600, 27), fill=(70, 80, 100), anchor='lm')
            im.paste(l, (0, 0), l)

        # ---- remate
        if t >= self.PUNCH - .35:
            kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
            cw, ch = int(540 * kk), int(430 * kk); cx, cy = 480, 470
            lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 32, fill=WHITE + (255,))
            if kk > .85:
                lg.rounded_rectangle((cx - 185, cy - 185, cx + 185, cy - 131), 27, fill=BLUE + (255,))
                lg.text((cx, cy - 158), 'TU AUDIENCIA REAL', font=F(800, 30), fill=WHITE, anchor='mm')
                lg.text((cx, cy - 65), 'Mamá', font=F(800, 110), fill=NAVY, anchor='mm')
                lg.text((cx, cy + 30), '(3 veces)', font=F(800, 76), fill=BLUE, anchor='mm')
                lg.text((cx, cy + 125), 'tu fan número 1', font=F(700, 36), fill=(80, 90, 110), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


NEW = {'p-familia': Familia}
