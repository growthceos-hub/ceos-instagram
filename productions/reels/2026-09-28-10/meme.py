import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88)
DARK, PANEL, MUT, NAVY, LINE = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66), (40, 52, 78)

WORDS = 'Y el secreto para que tu vídeo enganche desde el primer segundo es muy sencillo:'.split()
DRILL = 3.5  # empieza el taladro


class Taladro:
    POV = 'POV: por fin te sale la toma buena… y el vecino empieza a taladrar'
    DUR, PUNCH, FOCUS = 7.8, 6.1, (480, 470)
    SFX = ['pop@0.05', 'tick@0.6', 'tick@1.2', 'ding@1.6', 'tick@2.4', 'tick@3.0',
           'count:1.6@3.5', 'boom@3.55', 'ding@5.0', 'tick@5.6', 'boom@6.1']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        drill = t >= DRILL
        rnd = random.Random(int(t * 30))
        sx = sy = 0
        if drill and t < self.PUNCH:
            sx, sy = rnd.randint(-9, 9), rnd.randint(-7, 7)

        # ---------- barra superior del visor
        g.rectangle((0, 0, BW, 96), fill=PANEL)
        if int(t * 2.5) % 2 == 0:
            g.ellipse((36, 30, 70, 64), fill=RED)
        g.text((84, 48), 'REC', font=F(800, 34), fill=RED, anchor='lm')
        secs = 42 + t
        g.text((BW // 2, 48), f'00:0{int(secs // 60)}:{int(secs % 60):02d}:{int((secs % 1) * 25):02d}',
               font=F(700, 34), fill=WHITE, anchor='mm')
        g.rounded_rectangle((BW - 250, 26, BW - 40, 70), 22, fill=BLUE)
        g.text((BW - 145, 48), 'TOMA 47', font=F(800, 28), fill=WHITE, anchor='mm')

        # ---------- imagen del visor (escena)
        vx0, vy0, vx1, vy1 = 40 + sx, 120 + sy, 740 + sx, 720 + sy
        for y in range(vy0, vy1):
            k = (y - vy0) / (vy1 - vy0)
            c = (int(18 + 20 * k), int(40 + 30 * k), int(95 + 70 * k))
            if drill and t < self.PUNCH and rnd.random() < .02:
                c = (60, 70, 110)
            g.line([(vx0, y), (vx1, y)], fill=c)
        # luz de fondo (bokeh)
        for i, (bx, by, r) in enumerate([(120, 200, 40), (650, 190, 55), (600, 330, 30), (160, 380, 26)]):
            a = .5 + .5 * math.sin(t * 2 + i)
            col = (int(60 + 60 * a), int(100 + 60 * a), 220)
            g.ellipse((vx0 + bx - r, vy0 + by - r - 120 + 120, vx0 + bx + r, vy0 + by + r), fill=col)
        # persona hablando
        cx = (vx0 + vx1) // 2
        br = 3 * math.sin(t * 3)
        tilt = 0
        if drill and t < self.PUNCH:
            tilt = 10 * math.sin(t * 40)
        g.rounded_rectangle((cx - 170, vy0 + 390 + br, cx + 170, vy1 + 40), 90, fill=(232, 238, 250))
        g.rectangle((cx - 40, vy0 + 330 + br, cx + 40, vy0 + 400 + br), fill=(226, 184, 150))
        hx, hy = cx + tilt, vy0 + 250 + br
        g.ellipse((hx - 95, hy - 115, hx + 95, hy + 115), fill=(236, 196, 160))
        g.chord((hx - 100, hy - 128, hx + 100, hy + 40), 180, 360, fill=(60, 40, 30))
        # ojos
        if drill and t < self.PUNCH:
            g.ellipse((hx - 52, hy - 12, hx - 18, hy + 22), fill=WHITE); g.ellipse((hx + 18, hy - 12, hx + 52, hy + 22), fill=WHITE)
            g.ellipse((hx - 40, hy, hx - 30, hy + 10), fill=DARK); g.ellipse((hx + 30, hy, hx + 40, hy + 10), fill=DARK)
            g.ellipse((hx - 26, hy + 48, hx + 26, hy + 92), fill=(120, 40, 40))  # boca abierta
        else:
            blink = (t % 2.3) < .12
            for ex in (-35, 35):
                if blink: g.line([(hx + ex - 12, hy + 5), (hx + ex + 12, hy + 5)], fill=DARK, width=5)
                else: g.ellipse((hx + ex - 10, hy - 5, hx + ex + 10, hy + 15), fill=DARK)
            m = abs(math.sin(t * 11)) * 16
            g.rounded_rectangle((hx - 28, hy + 58, hx + 28, hy + 64 + m), 10, fill=(150, 60, 60))
        # rejilla de tercios + corchetes de enfoque
        for i in (1, 2):
            x = vx0 + (vx1 - vx0) * i // 3; y = vy0 + (vy1 - vy0) * i // 3
            g.line([(x, vy0), (x, vy1)], fill=(255, 255, 255), width=1)
            g.line([(vx0, y), (vx1, y)], fill=(255, 255, 255), width=1)
        fc = GREEN if not drill else (RED if int(t * 8) % 2 else WHITE)
        fx0, fy0, fx1, fy1 = hx - 130, hy - 150, hx + 130, hy + 150
        L = 36
        for (px, py, dx, dy) in [(fx0, fy0, 1, 1), (fx1, fy0, -1, 1), (fx0, fy1, 1, -1), (fx1, fy1, -1, -1)]:
            g.line([(px, py), (px + dx * L, py)], fill=fc, width=5); g.line([(px, py), (px, py + dy * L)], fill=fc, width=5)
        # subtítulo de lo que dice
        nw = min(len(WORDS), int(t / 0.25) + 3) if not drill else int((DRILL) / .25) + 3
        line = ' '.join(WORDS[:nw])
        font = F(700, 30)
        words = line.split(); rows, cur = [], ''
        for w in words:
            tr = (cur + ' ' + w).strip()
            if font.getlength(tr) > (vx1 - vx0 - 80): rows.append(cur); cur = w
            else: cur = tr
        rows.append(cur); rows = rows[-2:]
        if drill and t < self.PUNCH:
            rows = [rows[-1] + ' BRRRRR—']
        for i, r in enumerate(rows):
            y = vy1 - 110 + i * 44
            w = font.getlength(r)
            g.rounded_rectangle((cx - w / 2 - 16, y - 20, cx + w / 2 + 16, y + 22), 10, fill=(0, 0, 0))
            g.text((cx, y), r, font=font, fill=WHITE, anchor='mm')
        # sello "¡ESTA ES LA BUENA!"
        if 1.6 <= t < DRILL:
            k = pop((t - 1.6) / .3)
            s = int(34 * k)
            if s > 4:
                g.rounded_rectangle((vx0 + 24, vy0 + 22, vx0 + 24 + int(360 * k), vy0 + 22 + int(64 * k)), 18, fill=GREEN)
                g.text((vx0 + 24 + int(180 * k), vy0 + 22 + int(32 * k)), '¡ESTA ES LA BUENA!', font=F(800, s), fill=WHITE, anchor='mm')
        if drill and t < self.PUNCH:
            g.rounded_rectangle((vx0 + 24, vy0 + 22, vx0 + 384, vy0 + 86), 18, fill=RED)
            g.text((vx0 + 204, vy0 + 54), 'AUDIO ARRUINADO', font=F(800, 32), fill=WHITE, anchor='mm')
            # onomatopeya
            k = ease((t - DRILL) / .25)
            bf = F(800, int(118 * k) + 1)
            txt = 'BRRRRRRR'
            ox = 8 * math.sin(t * 60)
            g.text((cx + ox + 4, vy0 + 195 + 4), txt, font=bf, fill=DARK, anchor='mm')
            g.text((cx + ox, vy0 + 195), txt, font=bf, fill=(255, 214, 10), anchor='mm')

        # ---------- vúmetro (derecha)
        mx0 = 770
        g.rounded_rectangle((mx0, 120, BW - 40, 720), 22, fill=PANEL)
        g.text(((mx0 + BW - 40) // 2, 150), 'AUDIO', font=F(800, 24), fill=MUT, anchor='mm')
        for ch in range(2):
            bx = mx0 + 34 + ch * 60
            if drill and t < self.PUNCH:
                lvl = .95 + .05 * rnd.random()
            else:
                lvl = .35 + .25 * abs(math.sin(t * 7 + ch)) + .08 * rnd.random()
            nseg = 22
            for s in range(nseg):
                y1 = 690 - s * 23
                on = s / nseg < lvl
                col = GREEN if s < 14 else ((255, 204, 0) if s < 18 else RED)
                g.rectangle((bx, y1 - 18, bx + 44, y1), fill=col if on else (30, 38, 56))
        if drill and t < self.PUNCH and int(t * 8) % 2:
            g.rounded_rectangle((mx0 + 14, 170, BW - 54, 214), 12, fill=RED)
            g.text(((mx0 + BW - 40) // 2, 192), 'CLIP', font=F(800, 28), fill=WHITE, anchor='mm')

        # ---------- panel inferior: forma de onda
        g.rectangle((0, 750, BW, BH), fill=PANEL); g.line([(0, 750), (BW, 750)], fill=LINE, width=2)
        g.text((40, 790), 'PISTA DE VOZ', font=F(700, 26), fill=MUT, anchor='lm')
        st = 'limpia' if not drill else 'taladro del 3º B'
        g.text((BW - 40, 790), st, font=F(800, 26), fill=GREEN if not drill else RED, anchor='rm')
        prog = min(1, t / self.PUNCH)
        x0, x1, ym = 40, BW - 40, 895
        xe = int(x0 + (x1 - x0) * prog)
        xd = int(x0 + (x1 - x0) * DRILL / self.PUNCH)
        for x in range(x0, xe, 6):
            if x < xd:
                a = 18 + 30 * abs(math.sin(x * .07)) * abs(math.sin(x * .013 + 1))
                col = BLUE
            else:
                a = 78; col = RED
            g.line([(x, ym - a), (x, ym + a)], fill=col, width=4)
        g.line([(xe, 815), (xe, 975)], fill=WHITE, width=3)

        # ---------- notificación antes del remate
        if 5.0 <= t < self.PUNCH:
            k = ease((t - 5.0) / .3); l, lg = layer(); y = int(-130 + 260 * k)
            lg.rounded_rectangle((40, y, BW - 40, y + 116), 28, fill=(245, 248, 255, 255))
            lg.ellipse((64, y + 24, 132, y + 92), fill=(255, 170, 60, 255))
            lg.text((98, y + 58), '3B', font=F(800, 28), fill=WHITE, anchor='mm')
            lg.text((152, y + 40), 'Vecino del 3º B', font=F(800, 30), fill=NAVY, anchor='lm')
            lg.text((152, y + 82), '"Perdona, son solo 5 minutitos ;)"', font=F(600, 28), fill=(70, 80, 100), anchor='lm')
            im.paste(l, (0, 0), l)

        # ---------- remate
        if t >= self.PUNCH - .35:
            kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
            cw, ch = int(500 * kk), int(400 * kk); cx2, cy2 = 480, 470
            lg.rounded_rectangle((cx2 - cw // 2, cy2 - ch // 2, cx2 + cw // 2, cy2 + ch // 2), 32, fill=WHITE + (255,))
            if kk > .85:
                lg.rounded_rectangle((cx2 - 150, cy2 - 170, cx2 + 150, cy2 - 120), 27, fill=BLUE + (255,))
                lg.text((cx2, cy2 - 145), 'CLAQUETA', font=F(800, 28), fill=WHITE, anchor='mm')
                lg.text((cx2, cy2 - 55), 'TOMA 48', font=F(800, 88), fill=NAVY, anchor='mm')
                lg.text((cx2, cy2 + 30), 'desde el principio', font=F(800, 40), fill=BLUE, anchor='mm')
                lg.text((cx2, cy2 + 105), 'y el vecino, a por el 2º agujero', font=F(700, 25), fill=(80, 90, 110), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


NEW = {'p-taladro': Taladro}
