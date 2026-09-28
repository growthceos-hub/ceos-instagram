import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88)
DARK, PANEL, MUT, NAVY = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66)


class CincoMinutos:
    POV = 'POV: el cliente dice “es un vídeo de 30 segundos, en 5 minutos lo tenemos”'
    DUR, PUNCH, FOCUS = 7.8, 5.9, (480, 430)
    LINES = [(0.0, '“Hola a todos, soy…”'), (0.9, '“Perdón, perdón, otra”'),
             (1.8, '“¿Cómo empezaba?”'), (2.6, '“Me he reído, otra”'),
             (3.3, '“¿Se me ve bien el pelo?”'), (4.0, '“Ahora sí: hola a tod–”')]
    SFX = ['tick@0.05', 'tick@0.9', 'tick@1.8', 'tick@2.6', 'count:2.2@3.3', 'pop@5.55', 'boom@5.9']

    def take(self, t):
        if t >= self.PUNCH: return 47
        x = min(1, t / self.PUNCH)
        return 1 + int(45 * x ** 2.4)

    def minutes(self, t):
        # tiempo real transcurrido (reloj del estudio): 10:00 → 13:12
        return int(192 * min(1, t / self.PUNCH) ** 2.1)

    def clapper(self, g, cx, cy, t, n):
        # claqueta azul/blanca; golpe al cambiar de toma
        x = min(1, t / self.PUNCH); rate = 1 + 45 * 2.4 * x ** 1.4 / self.PUNCH
        ph = (t * rate) % 1
        ang = 28 * (1 - ease(ph / .35)) if ph < .35 else 28 * ease((ph - .35) / .65) * .25
        w, h = 520, 300
        x0, y0 = cx - w // 2, cy - h // 2 + 40
        g.rounded_rectangle((x0, y0, x0 + w, y0 + h), 22, fill=(20, 26, 40), outline=WHITE, width=4)
        g.text((x0 + 30, y0 + 28), 'ESCENA', font=F(700, 26), fill=MUT)
        g.text((x0 + 30, y0 + 60), 'VÍDEO 30 s', font=F(800, 44), fill=WHITE)
        g.text((x0 + 30, y0 + 140), 'TOMA', font=F(700, 26), fill=MUT)
        col = RED if n >= 30 else (BLUE if n >= 10 else WHITE)
        g.text((x0 + 30, y0 + 168), f'{n}', font=F(800, 100), fill=col)
        g.text((x0 + w - 30, y0 + 140), 'DURACIÓN', font=F(700, 26), fill=MUT, anchor='ra')
        g.text((x0 + w - 30, y0 + 175), '0:30', font=F(800, 60), fill=WHITE, anchor='ra')
        # barra superior fija con franjas
        top = y0 - 60
        g.rectangle((x0, top, x0 + w, y0 - 6), fill=WHITE)
        for i in range(6):
            xs = x0 + i * 90
            g.polygon([(xs + 10, top), (xs + 55, top), (xs + 25, y0 - 6), (xs - 20, y0 - 6)], fill=NAVY)
        # palo que golpea (rotado desde la esquina izquierda)
        a = math.radians(-ang); px, py = x0, top - 6
        pts = [(0, -54), (w, -54), (w, 0), (0, 0)]
        rot = [(px + X * math.cos(a) - Y * math.sin(a), py + X * math.sin(a) + Y * math.cos(a)) for X, Y in pts]
        g.polygon(rot, fill=WHITE)
        for i in range(6):
            q = [(i * 90 + 10, -54), (i * 90 + 55, -54), (i * 90 + 25, 0), (i * 90 - 20, 0)]
            q = [(min(max(X, 0), w), Y) for X, Y in q]
            g.polygon([(px + X * math.cos(a) - Y * math.sin(a), py + X * math.sin(a) + Y * math.cos(a)) for X, Y in q], fill=BLUE)

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        # fondo de estudio azul
        for y in range(110, 720, 4):
            k = (y - 110) / 610
            g.rectangle((0, y, BW, y + 4), fill=(int(12 + 10 * k), int(28 + 16 * k), int(64 + 30 * (1 - k))))
        sw = 40 * math.sin(t * 1.3)
        g.ellipse((640 + sw, 150, 900 + sw, 410), fill=(28, 58, 124)); g.ellipse((690 + sw, 200, 850 + sw, 360), fill=(42, 82, 164))
        g.ellipse((40 - sw, 480, 220 - sw, 660), fill=(22, 46, 100))
        n = self.take(t)
        shake = 0
        if t < self.PUNCH:
            x = min(1, t / self.PUNCH); shake = int(6 * x * math.sin(t * 60))
        self.clapper(g, BW // 2 + shake, 380, t, n)
        # frase del cliente (subtítulo)
        if t < self.PUNCH - .2:
            ts, cur = [(a, b) for a, b in self.LINES if t >= a][-1]
            if t >= 4.6: cur = '“Una más y ya”'; ts = 4.6
            k = 1 if ts == 0 else ease((t - ts) / .2)
            l, lg = layer(); fnt = F(700, 42); tw = fnt.getlength(cur); y = 650 + int(18 * (1 - k))
            lg.rounded_rectangle((BW / 2 - tw / 2 - 26, y - 36, BW / 2 + tw / 2 + 26, y + 36), 18, fill=(0, 0, 0, int(180 * k)))
            lg.text((BW / 2, y), cur, font=fnt, fill=(255, 255, 255, int(255 * k)), anchor='mm')
            im.paste(l, (0, 0), l)
        # barra superior del visor
        g.rectangle((0, 0, BW, 110), fill=DARK)
        if int(t * 2.5) % 2 == 0 or t >= self.PUNCH: g.ellipse((36, 38, 70, 72), fill=RED)
        g.text((86, 55), 'REC', font=F(800, 34), fill=RED, anchor='lm')
        m = self.minutes(t); hh, mm = 10 + (m // 60), m % 60
        g.text((BW // 2, 55), f'{hh:02d}:{mm:02d}', font=F(800, 46), fill=WHITE, anchor='mm')
        g.text((BW - 40, 55), f'TOMA {n:02d}', font=F(800, 34), fill=BLUE if n < 30 else RED, anchor='rm')
        # panel inferior: plan vs realidad
        g.rectangle((0, 720, BW, BH), fill=PANEL); g.line([(0, 720), (BW, 720)], fill=(40, 52, 78), width=2)
        g.text((50, 770), 'PLAN DEL CLIENTE', font=F(700, 26), fill=MUT, anchor='lm')
        g.rounded_rectangle((50, 800, BW - 50, 840), 12, fill=(38, 46, 64))
        g.rounded_rectangle((50, 800, 50 + int((BW - 100) * 5 / 192), 840), 12, fill=GREEN)
        g.text((BW - 50, 770), '5 min', font=F(800, 30), fill=GREEN, anchor='rm')
        g.text((50, 890), 'REALIDAD', font=F(700, 26), fill=MUT, anchor='lm')
        g.rounded_rectangle((50, 920, BW - 50, 960), 12, fill=(38, 46, 64))
        fr = max(0.03, m / 192)
        g.rounded_rectangle((50, 920, 50 + int((BW - 100) * fr), 960), 12, fill=BLUE if m < 90 else RED)
        g.text((BW - 50, 890), f'{m // 60} h {m % 60:02d} min' if m >= 60 else f'{m} min', font=F(800, 30), fill=BLUE if m < 90 else RED, anchor='rm')
        # remate
        if t >= self.PUNCH - .35:
            kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
            cw, ch = int(430 * kk), int(420 * kk); cx, cy = 480, 430
            lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 32, fill=WHITE + (255,))
            if kk > .85:
                lg.rounded_rectangle((cx - 150, cy - 180, cx + 150, cy - 128), 26, fill=RED + (255,))
                lg.text((cx, cy - 154), 'TOMA 47 · 13:12', font=F(800, 28), fill=WHITE, anchor='mm')
                lg.text((cx, cy - 60), '3 h 12 min', font=F(800, 74), fill=RED, anchor='mm')
                lg.text((cx, cy + 20), 'para 30', font=F(800, 50), fill=NAVY, anchor='mm')
                lg.text((cx, cy + 76), 'segundos', font=F(800, 50), fill=NAVY, anchor='mm')
                lg.text((cx, cy + 150), '“¿Otra por si acaso?”', font=F(700, 30), fill=BLUE, anchor='mm')
            im.paste(l, (0, 0), l)
        return im


NEW = {'p-cinco-minutos': CincoMinutos}
