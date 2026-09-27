"""Memes animados para reels POV. Cada meme define:
POV (texto), DUR, PUNCH (segundo del remate), FOCUS (x,y del zoom en la caja), SFX (lista de eventos) y draw(t) -> Image (W x H de la caja)."""
import os, math
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.environ.get('POV_FONTS', os.path.join(HERE, 'fonts'))
_fc = {}


def F(w, s):
    k = (w, s)
    if k not in _fc: _fc[k] = ImageFont.truetype(os.path.join(FONTS, f'M{w}.ttf'), s)
    return _fc[k]


BW, BH = 960, 1000


def ease(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3


def pop(x):  # entrada con rebote
    x = max(0, min(1, x)); return 1 + 2.2 * (x - 1) ** 3 + 1.2 * (x - 1) ** 2 if x < 1 else 1


def wrap(text, font, maxw):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if font.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    return lines


def layer():
    l = Image.new('RGBA', (BW, BH), (0, 0, 0, 0)); return l, ImageDraw.Draw(l)


def eur(v):
    s = f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return s + ' €'


# ------------------------------------------------------------------ 1. EN VISTO
class Visto:
    POV = 'POV: el lead que marcó “muy interesado” en el formulario cuando por fin le escribes'
    DUR, PUNCH, FOCUS = 7.6, 5.9, (330, 95)
    MSGS = [(0.3, 'Hola Laura, soy de Ceos Growth.'),
            (1.0, 'Vi que pediste info hace un rato. ¿Te llamo hoy o mañana?')]
    READ, TYPING = 1.9, [(2.3, 3.7), (4.1, 4.5), (4.9, 5.3)]
    SFX = ['pop@0.3', 'pop@1.0', 'tick@1.9', 'typing:1.4@2.3', 'typing:0.4@4.1', 'typing:0.4@4.9', 'boom@5.9']

    def status(self, t):
        if any(a <= t < b for a, b in self.TYPING): return 'escribiendo...', (0, 168, 132)
        if t >= self.PUNCH: return 'últ. vez hoy a las 11:42', (134, 150, 160)
        if t >= self.READ - .3: return 'en línea', (134, 150, 160)
        return 'toca para ver info', (134, 150, 160)

    def draw(self, t):
        GREY, BLUE, TXT, OUTB, INB = (134, 150, 160), (83, 189, 235), (233, 237, 239), (0, 92, 75), (32, 44, 51)
        im = Image.new('RGB', (BW, BH), (11, 20, 26)); g = ImageDraw.Draw(im)
        for yy in range(160, BH, 90):
            for xx in range((yy // 90 % 2) * 45, BW, 90): g.ellipse((xx, yy, xx + 6, yy + 6), fill=(17, 27, 33))
        g.rectangle((0, 0, BW, 150), fill=(31, 44, 52))
        g.line([(52, 75), (36, 60), (52, 45)], fill=TXT, width=5)
        g.ellipse((72, 32, 158, 118), fill=(106, 127, 138)); g.text((115, 75), 'L', font=F(700, 42), fill='white', anchor='mm')
        g.text((182, 34), 'Laura (formulario)', font=F(600, 38), fill=TXT)
        st, col = self.status(t); g.text((182, 86), st, font=F(500, 26), fill=col)
        y = 190; mf, sf = F(500, 40), F(500, 26)
        for i, (ts, text) in enumerate(self.MSGS):
            if t < ts: continue
            k = ease((t - ts) / .3); ls = wrap(text, mf, 600)
            bw = max(330, max(mf.getlength(l) for l in ls) + 60); bh = len(ls) * 52 + 64
            x1 = BW - 36; x0 = x1 - bw; dy = int((1 - k) * 30); a = int(255 * k)
            l, lg = layer()
            lg.rounded_rectangle((x0, y + dy, x1, y + bh + dy), 22, fill=OUTB + (a,))
            for j, s in enumerate(ls): lg.text((x0 + 28, y + 18 + j * 52 + dy), s, font=mf, fill=TXT + (a,))
            tt = f'11:3{4 + i}'; lg.text((x1 - 64 - sf.getlength(tt), y + bh - 42 + dy), tt, font=sf, fill=(170, 200, 190, a))
            tc = BLUE if t >= self.READ else GREY; bx, by = x1 - 56, y + bh - 30 + dy
            for o in (0, 12): lg.line([(bx + o, by + 4), (bx + o + 7, by + 11), (bx + o + 20, by - 4)], fill=tc + (a,), width=4)
            im.paste(l, (0, 0), l); y += bh + 18
        for a0, b0 in self.TYPING:
            if a0 <= t < b0:
                k = ease((t - a0) / .15) * ease((b0 - t) / .12); A = int(255 * k); l, lg = layer()
                lg.rounded_rectangle((36, y + 10, 196, y + 94), 22, fill=INB + (A,))
                for n in range(3):
                    ph = max(0, math.sin(t * 7 - n * .9)); cx, cy = 76 + n * 40, y + 52 - int(ph * 10)
                    lg.ellipse((cx - 9, cy - 9, cx + 9, cy + 9), fill=GREY + (int(A * (.55 + .45 * ph)),))
                im.paste(l, (0, 0), l)
        g.rounded_rectangle((24, BH - 104, BW - 128, BH - 24), 40, fill=INB)
        g.text((70, BH - 64), 'Mensaje', font=F(500, 34), fill=GREY, anchor='lm')
        g.ellipse((BW - 108, BH - 104, BW - 28, BH - 24), fill=(0, 168, 132))
        return im


# ------------------------------------------------------------------ 2. EL CUÑADO
class Cunado:
    POV = 'POV: dejaste que tu cuñado “que sabe de Facebook” te llevara los anuncios'
    DUR, PUNCH, FOCUS = 7.4, 5.6, (230, 385)
    SPEND = (0.6, 4.4, 1247.30)
    SFX = ['pop@0.2', 'count:3.8@0.6', 'tick@4.9', 'boom@5.6']

    def draw(self, t):
        BG, INK, MUT, LINE, BLU = (242, 244, 247), (28, 30, 33), (101, 103, 107), (221, 223, 226), (8, 102, 255)
        im = Image.new('RGB', (BW, BH), BG); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill='white'); g.line([(0, 110), (BW, 110)], fill=LINE, width=2)
        g.text((40, 55), 'Administrador de anuncios', font=F(700, 36), fill=INK, anchor='lm')
        g.rounded_rectangle((BW - 250, 30, BW - 40, 80), 10, fill=BLU)
        g.text((BW - 145, 55), '+ Crear', font=F(700, 28), fill='white', anchor='mm')
        # tarjeta campaña
        g.rounded_rectangle((30, 140, BW - 30, 520), 18, fill='white', outline=LINE, width=2)
        g.ellipse((64, 184, 84, 204), fill=(49, 162, 76))
        g.text((100, 194), 'Activa', font=F(600, 28), fill=(49, 162, 76), anchor='lm')
        g.text((64, 236), 'PROMO FINAL definitiva (2) - copia', font=F(700, 36), fill=INK)
        cols = [('Resultados', 64), ('Importe gastado', 330), ('Coste/resultado', 650)]
        for n, x in cols: g.text((x, 318), n, font=F(600, 26), fill=MUT)
        a, b, v = self.SPEND
        sp = v * ease((t - a) / (b - a)) if t >= a else 0
        g.text((330, 360), eur(sp), font=F(800, 44), fill=INK)
        res = '—' if t < 4.9 else '0'
        k = pop((t - 4.9) / .3) if t >= 4.9 else 1
        rf = F(800, int(44 * (1 + .6 * (k - 1) if t >= 4.9 else 1)))
        g.text((64, 360), res, font=F(800, 44) if res == '—' else rf, fill=(228, 30, 63) if res == '0' else INK)
        g.text((650, 360), '—', font=F(800, 44), fill=INK)
        g.line([(64, 440), (BW - 64, 440)], fill=LINE, width=2)
        g.text((64, 462), 'Actualizado hace 1 min', font=F(500, 24), fill=MUT)
        # segmentación
        g.rounded_rectangle((30, 550, BW - 30, BH - 40), 18, fill='white', outline=LINE, width=2)
        g.text((64, 590), 'Público', font=F(700, 32), fill=INK)
        rows = [('Ubicación', 'Toda España'), ('Edad', '18 – 65+'), ('Intereses', '“Negocios” y “Cosas”'),
                ('Anuncio', 'Foto del logo + “LLÁMANOS”'), ('Presupuesto', 'El que había')]
        for i, (kk, vv) in enumerate(rows):
            yy = 650 + i * 58; aa = ease((t - 1.2 - i * .45) / .3)
            if aa <= 0: continue
            l, lg = layer(); A = int(255 * aa)
            lg.text((64, yy), kk, font=F(500, 28), fill=MUT + (A,))
            lg.text((300, yy), vv, font=F(600, 28), fill=INK + (A,))
            im.paste(l, (0, 0), l)
        g.text((BW - 44, BH - 60), 'EJEMPLO', font=F(600, 20), fill=(170, 172, 176), anchor='rm')
        return im


# ------------------------------------------------------------------ 3. LA CUOTA
class Cuota:
    POV = 'POV: es día 1 y tu agencia te cobra la cuota aunque este mes no has vendido nada'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 690)
    SFX = ['ding@0.9', 'ding@2.4', 'pop@3.7', 'boom@5.8']

    def draw(self, t):
        BG, INK, MUT, LINE, RED = (255, 255, 255), (32, 33, 36), (95, 99, 104), (232, 234, 237), (217, 48, 37)
        im = Image.new('RGB', (BW, BH), BG); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 120), fill=(246, 248, 252))
        g.rounded_rectangle((30, 28, BW - 30, 92), 32, fill=(234, 241, 251))
        g.text((80, 60), 'Buscar en el correo', font=F(500, 30), fill=MUT, anchor='lm')
        g.text((40, 150), 'Recibidos', font=F(700, 30), fill=INK)
        mails = [('Proveedor luz', 'Tu factura de septiembre está disponible'),
                 ('Newsletter', '10 trucos para vender más (el 7 te sorprenderá)'),
                 ('Ayuntamiento', 'Recordatorio: tasa de basuras')]
        # nuevo correo de la agencia entra arriba
        k = ease((t - .9) / .35) if t >= .9 else 0
        top = 200
        rows = ([('Tu Agencia de Marketing', 'Factura mensual · Cuota octubre: 1.500 € · Cargo automático', True)] if k > 0 else []) + [(a, b, False) for a, b in mails]
        y = top - int(118 * (1 - k)) if k > 0 else top
        for name, sub, new in rows:
            if new: g.rectangle((0, y - 10, BW, y + 104), fill=(252, 244, 232))
            g.ellipse((40, y + 4, 110, y + 74), fill=(255, 106, 26) if new else (189, 193, 198))
            g.text((75, y + 39), name[0], font=F(700, 32), fill='white', anchor='mm')
            g.text((136, y), name, font=F(800 if new else 500, 30), fill=INK)
            g.text((BW - 40, y + 4), '09:00' if new else 'ayer', font=F(700 if new else 500, 24), fill=INK if new else MUT, anchor='ra')
            s = sub if F(500, 26).getlength(sub) < BW - 190 else sub[:44] + '…'
            g.text((136, y + 46), s, font=F(600 if new else 500, 26), fill=INK if new else MUT)
            y += 118
            g.line([(136, y - 12), (BW, y - 12)], fill=LINE, width=2)
        # notificación del banco
        if t >= 2.4:
            kk = ease((t - 2.4) / .3); l, lg = layer(); yy = int(-140 + 170 * kk)
            lg.rounded_rectangle((40, yy, BW - 40, yy + 120), 28, fill=(40, 40, 42, 245))
            lg.rounded_rectangle((70, yy + 30, 130, yy + 90), 14, fill=(26, 115, 232))
            lg.text((100, yy + 60), '€', font=F(800, 34), fill='white', anchor='mm')
            lg.text((156, yy + 22), 'Tu banco · ahora', font=F(500, 24), fill=(180, 180, 185))
            lg.text((156, yy + 58), 'Cargo de 1.500,00 € — Tu Agencia', font=F(700, 30), fill='white')
            im.paste(l, (0, 0), l)
        # tarjeta de ventas
        if t >= 3.7:
            kk = pop((t - 3.7) / .35); l, lg = layer()
            cw, ch = 760, 330; cx, cy = BW // 2, 690
            sw, sh = int(cw * kk), int(ch * kk)
            lg.rounded_rectangle((cx - sw // 2, cy - sh // 2, cx + sw // 2, cy + sh // 2), 28, fill=(20, 20, 22, 250))
            if kk > .9:
                lg.text((cx, cy - 100), 'Ventas de septiembre', font=F(600, 32), fill=(190, 190, 195), anchor='mm')
                lg.text((cx, cy + 10), '0', font=F(800, 150), fill=(255, 80, 80), anchor='mm')
                lg.text((cx, cy + 110), 'clientes nuevos', font=F(600, 30), fill=(190, 190, 195), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


MEMES = {'visto': Visto, 'cunado': Cunado, 'cuota': Cuota}
