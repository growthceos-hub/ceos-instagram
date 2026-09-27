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


# ------------------------------------------------------------------ 4. EL SOCIO
class Socio:
    POV = 'POV: enviaste el presupuesto y el cliente lleva 3 semanas “hablándolo con su socio”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 790)
    MSGS = [(0.4, 'out', 'Te paso el presupuesto con todo lo que hablamos.'),
            (1.3, 'in', 'Genial. Lo hablo con mi socio y te digo algo')]
    TYPING = [(2.0, 2.6)]
    CHIPS = [(2.9, 'MIÉRCOLES'), (3.6, 'VIERNES'), (4.3, '12 NOV'), (5.0, '3 SEMANAS DESPUÉS')]
    SFX = ['pop@0.4', 'pop@1.3', 'typing:0.6@2.0', 'ding@2.9', 'ding@3.6', 'ding@4.3', 'tick@5.0', 'boom@5.8']

    def status(self, t):
        if any(a <= t < b for a, b in self.TYPING): return 'escribiendo...', (0, 168, 132)
        if t >= self.PUNCH: return 'últ. vez hace 3 semanas', (134, 150, 160)
        if t < 2.9: return 'en línea', (134, 150, 160)
        return 'toca para ver info', (134, 150, 160)

    def draw(self, t):
        GREY, BLUE, TXT, OUTB, INB = (134, 150, 160), (83, 189, 235), (233, 237, 239), (0, 92, 75), (32, 44, 51)
        im = Image.new('RGB', (BW, BH), (11, 20, 26)); g = ImageDraw.Draw(im)
        for yy in range(160, BH, 90):
            for xx in range((yy // 90 % 2) * 45, BW, 90): g.ellipse((xx, yy, xx + 6, yy + 6), fill=(17, 27, 33))
        g.rectangle((0, 0, BW, 150), fill=(31, 44, 52))
        g.line([(52, 75), (36, 60), (52, 45)], fill=TXT, width=5)
        g.ellipse((72, 32, 158, 118), fill=(106, 127, 138)); g.text((115, 75), 'C', font=F(700, 42), fill='white', anchor='mm')
        g.text((182, 34), 'Carlos (presupuesto)', font=F(600, 38), fill=TXT)
        st, col = self.status(t); g.text((182, 86), st, font=F(500, 26), fill=col)
        y = 190; mf, sf = F(500, 40), F(500, 26)
        for i, (ts, side, text) in enumerate(self.MSGS):
            if t < ts: continue
            k = ease((t - ts) / .3); ls = wrap(text, mf, 600)
            bw = max(330, max(mf.getlength(l) for l in ls) + 60); bh = len(ls) * 52 + 64
            out = side == 'out'
            x0 = BW - 36 - bw if out else 36; x1 = x0 + bw
            dy = int((1 - k) * 30); a = int(255 * k)
            l, lg = layer()
            lg.rounded_rectangle((x0, y + dy, x1, y + bh + dy), 22, fill=(OUTB if out else INB) + (a,))
            for j, s in enumerate(ls): lg.text((x0 + 28, y + 18 + j * 52 + dy), s, font=mf, fill=TXT + (a,))
            tt = f'10:1{2 + i}'; lg.text((x1 - (64 if out else 28) - sf.getlength(tt), y + bh - 42 + dy), tt, font=sf, fill=(170, 200, 190, a))
            if out:
                bx, by = x1 - 56, y + bh - 30 + dy
                for o in (0, 12): lg.line([(bx + o, by + 4), (bx + o + 7, by + 11), (bx + o + 20, by - 4)], fill=BLUE + (a,), width=4)
            im.paste(l, (0, 0), l); y += bh + 18
        for a0, b0 in self.TYPING:
            if a0 <= t < b0:
                k = ease((t - a0) / .15) * ease((b0 - t) / .12); A = int(255 * k); l, lg = layer()
                lg.rounded_rectangle((36, y + 10, 196, y + 94), 22, fill=INB + (A,))
                for n in range(3):
                    ph = max(0, math.sin(t * 7 - n * .9)); cx, cy = 76 + n * 40, y + 52 - int(ph * 10)
                    lg.ellipse((cx - 9, cy - 9, cx + 9, cy + 9), fill=GREY + (int(A * (.55 + .45 * ph)),))
                im.paste(l, (0, 0), l)
        cy0 = y + 36
        cf = F(600, 30)
        for i, (ts, label) in enumerate(self.CHIPS):
            if t < ts: continue
            k = pop((t - ts) / .3)
            wch = cf.getlength(label) + 70
            l, lg = layer()
            sw, sh = int(wch * min(1, k)), int(60 * min(1, k))
            cx = BW // 2; cyy = cy0 + i * 76 + 30
            lg.rounded_rectangle((cx - sw // 2, cyy - sh // 2, cx + sw // 2, cyy + sh // 2), 16, fill=(24, 34, 40, 255))
            if k > .8:
                big = i == len(self.CHIPS) - 1
                lg.text((cx, cyy), label, font=F(700 if big else 600, 30), fill=(255, 138, 96) if big else (140, 155, 165), anchor='mm')
            im.paste(l, (0, 0), l)
        g.rounded_rectangle((24, BH - 104, BW - 128, BH - 24), 40, fill=INB)
        g.text((70, BH - 64), 'Mensaje', font=F(500, 34), fill=GREY, anchor='lm')
        g.ellipse((BW - 108, BH - 104, BW - 28, BH - 24), fill=(0, 168, 132))
        return im


# ------------------------------------------------------------------ 5. EL SORTEO
class Sorteo:
    POV = 'POV: hiciste un sorteo para “ganar visibilidad” y ganaste 2.000 seguidores que solo querían el iPhone'
    DUR, PUNCH, FOCUS = 7.6, 5.6, (480, 600)
    NOTIFS = [(1.2, 'maria.sorteos_23 empezó a seguirte'), (2.0, 'todo_gratis_es empezó a seguirte'),
              (2.8, 'regalos.y.sorteos comentó: HECHO'), (3.6, 'juanlu_88 empezó a seguirte')]
    SFX = ['count:3.8@0.8'] + [f'pop@{a}' for a, _ in NOTIFS] + ['pop@5.2', 'boom@5.6']

    def draw(self, t):
        INK, MUT, LINE, ORG = (28, 30, 33), (120, 122, 126), (228, 230, 233), (255, 106, 26)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.text((40, 40), 'mimueble_burgos', font=F(700, 40), fill=INK)
        g.line([(0, 110), (BW, 110)], fill=LINE, width=2)
        g.ellipse((40, 150, 230, 340), outline=ORG, width=6)
        g.ellipse((56, 166, 214, 324), fill=(235, 237, 240))
        g.text((135, 245), 'M', font=F(800, 70), fill=(160, 163, 168), anchor='mm')
        foll = 2410 + (4893 - 2410) * ease((t - .8) / 3.8)
        stats = [('214', 'publicaciones', 340), ('{:,}'.format(int(foll)).replace(',', '.'), 'seguidores', 570), ('512', 'seguidos', 810)]
        for v, lab, x in stats:
            g.text((x, 200), v, font=F(800, 46), fill=INK, anchor='mm')
            g.text((x, 252), lab, font=F(500, 26), fill=MUT, anchor='mm')
        g.rounded_rectangle((40, 380, BW - 40, 452), 14, fill=(239, 241, 244))
        g.text((BW // 2, 416), 'Editar perfil', font=F(600, 30), fill=INK, anchor='mm')
        g.rounded_rectangle((40, 480, BW - 40, 560), 14, fill=(255, 240, 230))
        g.text((70, 520), 'SORTEO iPhone: sigue, comenta y comparte', font=F(700, 29), fill=ORG, anchor='lm')
        gy = 600
        for r in range(2):
            for c in range(3):
                x0 = c * (BW // 3) + 4; y0_ = gy + r * (BW // 3) + 4
                g.rectangle((x0, y0_, x0 + BW // 3 - 8, y0_ + BW // 3 - 8), fill=(226, 228, 232))
        for i, (ts, txt) in enumerate(self.NOTIFS):
            if not (ts <= t < ts + 1.5): continue
            k = ease((t - ts) / .3) * ease((ts + 1.5 - t) / .3)
            l, lg = layer(); yy = int(-120 + 150 * k); A = int(255 * min(1, k * 2))
            lg.rounded_rectangle((40, yy, BW - 40, yy + 100), 24, fill=(38, 38, 40, min(245, A)))
            lg.ellipse((66, yy + 24, 118, yy + 76), fill=ORG + (A,))
            lg.text((92, yy + 50), txt[0].upper(), font=F(700, 28), fill=(255, 255, 255, A), anchor='mm')
            lg.text((140, yy + 22), 'Instagram · ahora', font=F(500, 22), fill=(175, 175, 180, A))
            lg.text((140, yy + 54), txt, font=F(600, 28), fill=(255, 255, 255, A))
            im.paste(l, (0, 0), l)
        if t >= 5.2:
            kk = pop((t - 5.2) / .35); l, lg = layer()
            cw, ch = 780, 360; cx, cy = BW // 2, 600
            sw, sh = int(cw * kk), int(ch * kk)
            lg.rounded_rectangle((cx - sw // 2, cy - sh // 2, cx + sw // 2, cy + sh // 2), 28, fill=(20, 20, 22, 250))
            if kk > .9:
                lg.text((cx, cy - 110), 'Un mes después', font=F(600, 30), fill=(190, 190, 195), anchor='mm')
                lg.text((cx, cy - 10), 'Ventas: 0', font=F(800, 80), fill=(255, 80, 80), anchor='mm')
                lg.text((cx, cy + 105), 'y -2.390 seguidores', font=F(600, 28), fill=(190, 190, 195), anchor='mm')
            im.paste(l, (0, 0), l)
        g.text((BW - 44, BH - 40), 'EJEMPLO', font=F(600, 20), fill=(170, 172, 176), anchor='rm')
        return im


# ------------------------------------------------------------------ 6. EL INFORME
class Informe:
    POV = 'POV: tu agencia te presenta el informe del mes y sube todo menos las ventas'
    DUR, PUNCH, FOCUS = 7.6, 5.7, (320, 830)
    ROWS = [(0.8, 'Impresiones', 124500, '+41 %'), (1.8, 'Alcance', 46200, '+28 %'), (2.8, 'Interacciones', 3870, '+32 %')]
    SFX = ['pop@0.8', 'count:0.7@0.8', 'pop@1.8', 'count:0.7@1.8', 'pop@2.8', 'count:0.7@2.8', 'tick@4.2', 'boom@5.7']

    def draw(self, t):
        INK, MUT, LINE, GRN = (30, 32, 35), (110, 112, 117), (226, 228, 232), (34, 154, 84)
        im = Image.new('RGB', (BW, BH), (246, 247, 249)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 96), fill=(58, 60, 64))
        g.text((40, 48), 'informe_octubre_FINAL_v3.pdf', font=F(600, 30), fill=(235, 235, 238), anchor='lm')
        g.text((BW - 40, 48), '1 / 14', font=F(500, 26), fill=(180, 180, 185), anchor='rm')
        g.rounded_rectangle((30, 126, BW - 30, BH - 30), 18, fill='white', outline=LINE, width=2)
        g.text((70, 180), 'Informe mensual — Octubre', font=F(800, 44), fill=INK)
        g.text((70, 244), 'Preparado por tu agencia de siempre', font=F(500, 28), fill=MUT)
        g.line([(70, 300), (BW - 70, 300)], fill=LINE, width=2)
        for i, (ts, lab, val, pct) in enumerate(self.ROWS):
            if t < ts: continue
            k = ease((t - ts) / .35); yy = 340 + i * 150; A = int(255 * k)
            v = int(val * min(1, ease((t - ts) / .8)))
            l, lg = layer()
            lg.text((70, yy), lab, font=F(600, 30), fill=MUT + (A,))
            lg.text((70, yy + 42), '{:,}'.format(v).replace(',', '.'), font=F(800, 64), fill=INK + (A,))
            lg.polygon([(BW - 250, yy + 78), (BW - 226, yy + 46), (BW - 202, yy + 78)], fill=GRN + (A,))
            lg.text((BW - 186, yy + 62), pct, font=F(800, 40), fill=GRN + (A,), anchor='lm')
            im.paste(l, (0, 0), l)
        if t >= 4.2:
            k = ease((t - 4.2) / .35); A = int(255 * k); l, lg = layer()
            yy = 790
            lg.line([(70, yy - 24), (BW - 70, yy - 24)], fill=LINE + (A,), width=2)
            lg.text((70, yy), 'Ventas atribuidas', font=F(600, 30), fill=MUT + (A,))
            lg.text((70, yy + 42), '—', font=F(800, 64), fill=(200, 60, 55, A))
            lg.text((250, yy + 66), '(dato no disponible)', font=F(500, 26), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
        g.text((BW - 60, BH - 60), 'EJEMPLO', font=F(600, 20), fill=(170, 172, 176), anchor='rm')
        return im


MEMES.update({'socio': Socio, 'sorteo': Sorteo, 'informe': Informe})


# ------------------------------------------------------------------ 7. LA TORRE (jenga)
class Torre:
    POV = 'POV: tu socio entra al Administrador de anuncios “solo a ajustar una cosita” en la campaña que funciona'
    DUR, PUNCH, FOCUS = 8.2, 6.1, (480, 500)
    SLIDE = (2.2, 4.0)   # el bloque sale
    FALL = 5.0           # colapso
    SFX = ['pop@1.5', 'count:1.8@2.2', 'tick@4.1', 'boom@5.0', 'pop@6.0']
    ROWS = ['LA CUENTA', 'EL PÍXEL', 'CAMPAÑA QUE VENDE', 'CPL 8 €', 'LA PUJA',
            'LEADS CADA DÍA', 'AGENDA DEL CLOSER', 'VENTAS', 'TU NÓMINA']
    PULL = 4  # LA PUJA

    def __init__(self):
        import random
        r = random.Random(11)
        self.phys = [(r.uniform(-140, 140), r.uniform(-60, 40), r.uniform(-2.8, 2.8)) for _ in self.ROWS]

    def block(self, label, w=430, h=64, hot=False):
        im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); g = ImageDraw.Draw(im)
        g.rounded_rectangle((0, 0, w - 1, h - 1), 12, fill=(255, 106, 26) if hot else (242, 237, 231),
                            outline=(200, 80, 15) if hot else (210, 202, 192), width=3)
        g.text((w // 2, h // 2), label, font=F(700, 27), fill='white' if hot else (60, 52, 45), anchor='mm')
        return im

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (16, 14, 13)); g = ImageDraw.Draw(im)
        g.rectangle((0, 880, BW, BH), fill=(28, 24, 21))
        g.line([(0, 880), (BW, 880)], fill=(45, 39, 34), width=3)
        n = len(self.ROWS); bh = 64; base = 872
        # balanceo: suave al inicio, brutal antes de caer
        amp = 3 + (0 if t < self.SLIDE[1] else 14 * ease((t - self.SLIDE[1]) / (self.FALL - self.SLIDE[1])))
        for i, label in enumerate(self.ROWS):
            hot = i == self.PULL
            y = base - (i + 1) * (bh + 4)
            x = BW // 2 - 215
            rot, extra = 0, 0
            if t < self.FALL:
                sway = amp * math.sin(t * 2.4 + i * .55) * (i / n + .2)
                x += sway
                if hot and t >= self.SLIDE[0]:
                    k = ease((t - self.SLIDE[0]) / (self.SLIDE[1] - self.SLIDE[0]))
                    extra = 400 * k; rot = -6 * k
            else:
                dt = t - self.FALL
                vx, vy, om = self.phys[i]
                if hot: vx += 300
                grav = 2500
                x += vx * dt
                y = y + vy * dt + .5 * grav * dt * dt
                rot = math.degrees(om * dt)
                yl = base - bh + 4
                if y > yl - (i % 3) * 26: y = yl - (i % 3) * 26  # se apilan en el suelo
                if hot: x += 400; rot -= 6
            spr = self.block(label, hot=hot)
            if rot: spr = spr.rotate(rot, expand=True, resample=Image.BICUBIC)
            im.paste(spr, (int(x + extra), int(y)), spr)
        # cursor/mano sobre el bloque
        if 1.4 <= t < self.SLIDE[1] + .2:
            k = ease((t - 1.4) / .4)
            bx = BW // 2 + 190 + (400 * ease((t - self.SLIDE[0]) / (self.SLIDE[1] - self.SLIDE[0])) if t >= self.SLIDE[0] else 0)
            by = base - (self.PULL + 1) * (bh + 4) + 30
            l, lg = layer(); A = int(255 * k)
            lg.polygon([(bx, by), (bx + 34, by + 12), (bx + 15, by + 18), (bx + 26, by + 44),
                        (bx + 14, by + 49), (bx + 5, by + 22), (bx - 8, by + 34)], fill=(255, 255, 255, A), outline=(0, 0, 0, A))
            lg.text((min(bx - 16, BW - 30), by - 12), '"solo una cosita"', font=F(600, 26), fill=(255, 170, 130, A), anchor='ra')
            im.paste(l, (0, 0), l)
        # tarjeta final
        if t >= 6.0:
            kk = pop((t - 6.0) / .35); l, lg = layer()
            cw, ch = 780, 340; cx, cy = BW // 2, 500
            sw, sh = int(cw * kk), int(ch * kk)
            lg.rounded_rectangle((cx - sw // 2, cy - sh // 2, cx + sw // 2, cy + sh // 2), 28, fill=(20, 20, 22, 250))
            if kk > .9:
                lg.text((cx, cy - 105), '“Solo era una cosita”', font=F(600, 32), fill=(190, 190, 195), anchor='mm')
                lg.text((cx, cy - 5), 'CPL: x4', font=F(800, 88), fill=(255, 80, 80), anchor='mm')
                lg.text((cx, cy + 100), 'LA CAMPAÑA NO SE TOCA', font=F(700, 30), fill=(255, 170, 130), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


MEMES['torre'] = Torre
