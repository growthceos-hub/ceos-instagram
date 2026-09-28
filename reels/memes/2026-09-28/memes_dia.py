"""Memes del día 2026-09-28: 20 reels POV nuevos (m01…m20). Motor: toolkit/reels/pov_reel.py."""
import os, sys, math
sys.path.insert(0, 'toolkit/reels')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import *  # noqa
from memes import F, BW, BH, ease, pop, wrap, layer, eur
from PIL import Image, ImageDraw

RED, GRY = (255, 80, 80), (190, 190, 195)
WA_GREY, WA_BLUE, WA_TXT, WA_OUT, WA_IN = (134, 150, 160), (83, 189, 235), (233, 237, 239), (0, 92, 75), (32, 44, 51)


def tag(g, x=BW - 44, y=BH - 40, dark=False):
    g.text((x, y), 'EJEMPLO', font=F(600, 20), fill=(110, 112, 116) if dark else (170, 172, 176), anchor='rm')


def card(im, t, t0, top, big, sub, cy=560, big_size=84, col=RED, cw=800, ch=360):
    """Tarjeta final oscura con entrada de rebote."""
    if t < t0: return
    kk = pop((t - t0) / .35); l, lg = layer(); cx = BW // 2
    sw, sh = int(cw * kk), int(ch * kk)
    lg.rounded_rectangle((cx - sw // 2, cy - sh // 2, cx + sw // 2, cy + sh // 2), 28, fill=(20, 20, 22, 250))
    if kk > .9:
        lg.text((cx, cy - ch * .31), top, font=F(600, 32), fill=GRY, anchor='mm')
        lg.text((cx, cy), big, font=F(800, big_size), fill=col, anchor='mm')
        lg.text((cx, cy + ch * .31), sub, font=F(600, 30), fill=GRY, anchor='mm')
    im.paste(l, (0, 0), l)


def banner(im, t, t0, app, text, t1=None, y=30, icol=(37, 211, 102), ich='W', sub=None):
    """Notificación del móvil que baja desde arriba (t1 = cuándo se va)."""
    if t < t0 or (t1 and t >= t1): return
    k = ease((t - t0) / .3) * (ease((t1 - t) / .3) if t1 else 1)
    l, lg = layer(); h = 150 if sub else 120; yy = int(y - (h + 40) * (1 - k)); A = int(255 * min(1, k * 2))
    lg.rounded_rectangle((36, yy, BW - 36, yy + h), 28, fill=(40, 40, 44, min(248, A)))
    lg.rounded_rectangle((64, yy + 30, 124, yy + 90), 16, fill=icol + (A,))
    lg.text((94, yy + 60), ich, font=F(800, 32), fill=(255, 255, 255, A), anchor='mm')
    lg.text((150, yy + 22), app, font=F(500, 24), fill=(180, 180, 185, A))
    tf = F(700, 29); s = text if tf.getlength(text) < BW - 220 else wrap(text, tf, BW - 220)[0] + '…'
    lg.text((150, yy + 58), s, font=tf, fill=(255, 255, 255, A))
    if sub: lg.text((150, yy + 100), sub, font=F(500, 26), fill=(200, 200, 205, A))
    im.paste(l, (0, 0), l)


def stars(g, x, y, n, size=30, on=(251, 188, 4), off=(218, 220, 224)):
    for i in range(5):
        cx, cy = x + i * (size + 8) + size / 2, y + size / 2; pts = []
        for j in range(10):
            r = size / 2 if j % 2 == 0 else size / 4.6; a = -math.pi / 2 + j * math.pi / 5
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        g.polygon(pts, fill=on if i < n else off)


def check2(lg, bx, by, col, a=255):
    for o in (0, 12): lg.line([(bx + o, by + 4), (bx + o + 7, by + 11), (bx + o + 20, by - 4)], fill=col + (a,), width=4)


class WAChat:
    """Base de chat de WhatsApp: NAME, LETTER, MSGS [(t, 'in'|'out', texto)], TYPING, status(t)."""
    NAME, LETTER, MSGS, TYPING, HOUR = 'Cliente', 'C', [], [], '18:0'

    def status(self, t):
        if any(a <= t < b for a, b in self.TYPING): return 'escribiendo...', (0, 168, 132)
        return 'en línea', WA_GREY

    def base(self, t):
        im = Image.new('RGB', (BW, BH), (11, 20, 26)); g = ImageDraw.Draw(im)
        for yy in range(160, BH, 90):
            for xx in range((yy // 90 % 2) * 45, BW, 90): g.ellipse((xx, yy, xx + 6, yy + 6), fill=(17, 27, 33))
        g.rectangle((0, 0, BW, 150), fill=(31, 44, 52))
        g.line([(52, 75), (36, 60), (52, 45)], fill=WA_TXT, width=5)
        g.ellipse((72, 32, 158, 118), fill=(106, 127, 138)); g.text((115, 75), self.LETTER, font=F(700, 42), fill='white', anchor='mm')
        g.text((182, 34), self.NAME, font=F(600, 38), fill=WA_TXT)
        st, col = self.status(t); g.text((182, 86), st, font=F(500, 26), fill=col)
        return im, g

    def bubbles(self, im, t, y=190):
        mf, sf = F(500, 40), F(500, 26)
        for i, m in enumerate(self.MSGS):
            ts, side, text = m[:3]
            if t < ts: continue
            k = ease((t - ts) / .3); out = side == 'out'; dy = int((1 - k) * 30); a = int(255 * k)
            l, lg = layer()
            if text.startswith('AUDIO:'):
                dur = text[6:]; bw, bh = 640, 130
                x0 = BW - 36 - bw if out else 36; x1 = x0 + bw
                lg.rounded_rectangle((x0, y + dy, x1, y + bh + dy), 22, fill=(WA_OUT if out else WA_IN) + (a,))
                lg.polygon([(x0 + 40, y + 31 + dy), (x0 + 40, y + 79 + dy), (x0 + 80, y + 55 + dy)], fill=WA_TXT + (a,))
                for n in range(34):
                    hh = 6 + int(22 * abs(math.sin(n * 1.7) * math.cos(n * .45)))
                    xx = x0 + 110 + n * 13
                    lg.line([(xx, y + 50 - hh * .8 + dy), (xx, y + 50 + hh * .8 + dy)], fill=(160, 180, 185, a), width=6)
                lg.text((x0 + 110, y + bh - 12 + dy), dur, font=F(600, 26), fill=(170, 200, 190, a), anchor='ls')
                bh_ = bh
            else:
                ls = wrap(text, mf, 600)
                bw = max(330, max(mf.getlength(s) for s in ls) + 60); bh_ = len(ls) * 52 + 64
                x0 = BW - 36 - bw if out else 36; x1 = x0 + bw
                lg.rounded_rectangle((x0, y + dy, x1, y + bh_ + dy), 22, fill=(WA_OUT if out else WA_IN) + (a,))
                for j, s in enumerate(ls): lg.text((x0 + 28, y + 18 + j * 52 + dy), s, font=mf, fill=WA_TXT + (a,))
            tt = f'{self.HOUR}{2 + i}'
            lg.text((x1 - (64 if out else 28) - sf.getlength(tt), y + bh_ - 42 + dy), tt, font=sf, fill=(170, 200, 190, a))
            if out: check2(lg, x1 - 56, y + bh_ - 30 + dy, WA_BLUE, a)
            im.paste(l, (0, 0), l); y += bh_ + 18
        for a0, b0 in self.TYPING:
            if a0 <= t < b0:
                k = ease((t - a0) / .15) * ease((b0 - t) / .12); A = int(255 * k); l, lg = layer()
                lg.rounded_rectangle((36, y + 10, 196, y + 94), 22, fill=WA_IN + (A,))
                for n in range(3):
                    ph = max(0, math.sin(t * 7 - n * .9)); cx, cy = 76 + n * 40, y + 52 - int(ph * 10)
                    lg.ellipse((cx - 9, cy - 9, cx + 9, cy + 9), fill=WA_GREY + (int(A * (.55 + .45 * ph)),))
                im.paste(l, (0, 0), l)
        return y

    def footer(self, g):
        g.rounded_rectangle((24, BH - 104, BW - 128, BH - 24), 40, fill=WA_IN)
        g.text((70, BH - 64), 'Mensaje', font=F(500, 34), fill=WA_GREY, anchor='lm')
        g.ellipse((BW - 108, BH - 104, BW - 28, BH - 24), fill=(0, 168, 132))



def timer(sec):
    return f'{int(sec // 60):02d}:{int(sec % 60):02d}'

def stamp(im, t, t0, text, cx, cy, col=(230, 50, 50), size=46, rot=-8):
    """Sello rojo que cae con rebote."""
    if t < t0: return
    k = pop((t - t0) / .3); f = F(800, size)
    w = int(f.getlength(text) + 60); h = size + 44
    s = Image.new('RGBA', (w + 10, h + 10), (0, 0, 0, 0)); sg = ImageDraw.Draw(s)
    sg.rounded_rectangle((5, 5, w + 5, h + 5), 14, outline=col + (255,), width=7, fill=(255, 255, 255, 215))
    sg.text((w // 2 + 5, h // 2 + 5), text, font=f, fill=col + (255,), anchor='mm')
    sc = max(.05, 1 + 1.2 * (1 - min(1, k))) if k < 1 else 1
    s = s.resize((max(1, int(s.width * sc)), max(1, int(s.height * sc))), Image.LANCZOS).rotate(rot, expand=True, resample=Image.BICUBIC)
    im.paste(s, (int(cx - s.width / 2), int(cy - s.height / 2)), s)


def cursor(lg, bx, by, A=255):
    lg.polygon([(bx, by), (bx + 34, by + 12), (bx + 15, by + 18), (bx + 26, by + 44), (bx + 14, by + 49), (bx + 5, by + 22), (bx - 8, by + 34)],
               fill=(255, 255, 255, A), outline=(0, 0, 0, A))


def lock_bg(hour='21:47', date='lunes, 28 de septiembre'):
    im = Image.new('RGB', (BW, BH), (18, 22, 34)); g = ImageDraw.Draw(im)
    for yy in range(BH):
        c = int(18 + 30 * yy / BH); g.line([(0, yy), (BW, yy)], fill=(c, c - 4, c + 22))
    g.text((BW // 2, 60), date, font=F(600, 30), fill=(220, 222, 230), anchor='mm')
    g.text((BW // 2, 170), hour, font=F(800, 150), fill='white', anchor='mm')
    return im, g


# ------------------------------------------------------------------ m01. EL DESCUENTO QUE SE COME TODO (WhatsApp)
class Descuento(WAChat):
    POV = 'POV: le pasas el presupuesto al cliente y empieza a quitar partidas “para abaratar”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    NAME, LETTER, HOUR = 'Cliente (reforma de cocinas)', 'R', '12:0'
    MSGS = [(0.3, 'out', 'Te paso el presupuesto: anuncios + web + seguimiento.'),
            (1.5, 'in', '¿Y si quitamos los anuncios?'),
            (2.9, 'in', '¿Y la web la dejamos para otro año?'),
            (4.3, 'in', 'Vale, ¿y cuánto sale lo que queda?')]
    TYPING = [(2.0, 2.8), (3.5, 4.2)]
    SFX = ['pop@0.3', 'pop@1.5', 'typing:0.8@2.0', 'pop@2.9', 'typing:0.7@3.5', 'pop@4.3', 'pop@5.2', 'boom@5.8']

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g)
        card(im, t, 5.2, 'Lo que queda', 'Nada', 'y quiere vender el doble', cy=560)
        return im


# ------------------------------------------------------------------ m02. 5 LEADS, EL MISMO SEÑOR (notificaciones)
class MismoLead:
    POV = 'POV: te entran 5 leads en un minuto y es el mismo señor dándole a “enviar”'
    DUR, PUNCH, FOCUS = 7.6, 5.7, (480, 560)
    TS = [0.5, 1.1, 1.7, 2.3, 2.9]
    SFX = [f'ding@{a}' for a in TS] + ['tick@3.9', 'pop@4.9', 'boom@5.7']

    def draw(self, t):
        im, g = lock_bg()
        for i, ts in enumerate(self.TS):
            if t < ts: continue
            k = ease((t - ts) / .3); A = int(255 * k); l, lg = layer()
            yy = 290 + i * 128 + int((1 - k) * -40)
            lg.rounded_rectangle((36, yy, BW - 36, yy + 112), 26, fill=(58, 62, 74, int(230 * k)))
            lg.rounded_rectangle((60, yy + 26, 120, yy + 86), 14, fill=(255, 106, 26, A))
            lg.text((90, yy + 56), 'L', font=F(800, 32), fill=(255, 255, 255, A), anchor='mm')
            lg.text((144, yy + 18), f'Nuevo lead · Formulario web · 21:4{6 + i // 3}', font=F(500, 23), fill=(190, 192, 200, A))
            lg.text((144, yy + 54), 'Antonio G. — “Quiero información”', font=F(700, 29), fill=(255, 255, 255, A))
            im.paste(l, (0, 0), l)
        if t >= 3.9:
            stamp(im, t, 3.9, 'MISMO TELÉFONO', BW // 2, 545, size=52)
        card(im, t, 4.9, 'Leads reales', '1', 'y muy insistente', cy=560, big_size=110)
        tag(g, dark=True)
        return im


# ------------------------------------------------------------------ m03. LA RESEÑA EN LA FICHA DE OTRO (reseñas)
class ResenaAjena:
    POV = 'POV: tu mejor cliente por fin te deja 5 estrellas… en la ficha de tu competencia'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 190)
    SFX = ['pop@0.3', 'pop@1.2', 'ding@2.6', 'ding@3.8', 'pop@4.9', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (32, 33, 36), (95, 99, 104), (228, 230, 233)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 290), fill=(248, 249, 250)); g.line([(0, 290), (BW, 290)], fill=LINE, width=2)
        g.text((40, 60), 'Reformas Castilla', font=F(800, 50), fill=INK, anchor='lm')
        g.text((40, 124), '4,1', font=F(700, 34), fill=INK, anchor='lm'); stars(g, 110, 108, 4)
        g.text((330, 124), '· Empresa de reformas · Burgos', font=F(500, 28), fill=MUT, anchor='lm')
        g.rounded_rectangle((40, 180, 330, 244), 32, fill=(232, 240, 254))
        g.text((185, 212), 'Escribir reseña', font=F(700, 28), fill=(26, 115, 232), anchor='mm')
        g.text((40, 340), 'Reseñas más recientes', font=F(700, 32), fill=INK)
        revs = [(0.3, 'Marisa L.', 4, 'Cumplieron plazos. Bien.', 'hace 2 semanas'),
                (1.2, 'J. Ortega', 3, 'Correcto, aunque algo caros.', 'hace 1 mes')]
        y = 400
        if t >= 2.6:
            k = ease((t - 2.6) / .35); l, lg = layer(); A = int(255 * k)
            lg.rectangle((0, y - 14, BW, y + 206), fill=(255, 248, 225, A))
            lg.ellipse((40, y, 110, y + 70), fill=(52, 168, 83, A)); lg.text((75, y + 35), 'P', font=F(700, 32), fill=(255, 255, 255, A), anchor='mm')
            lg.text((130, y + 4), 'Pedro R. (tu cliente de 3 años)', font=F(700, 30), fill=INK + (A,))
            lg.text((130, y + 44), 'hace un momento', font=F(500, 24), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
            if k > .5: stars(g, 40, y + 92, 5, size=34)
            ft = F(600, 30)
            for j, s in enumerate(wrap('¡Trabajo impecable! Os recomiendo a todo el mundo, un 10.', ft, BW - 90)):
                g.text((40, y + 140 + j * 40), s, font=ft, fill=INK)
            y += 250
        for ts, n, s_, txt, when in revs:
            if t < ts: continue
            g.ellipse((40, y, 110, y + 70), fill=(189, 193, 198)); g.text((75, y + 35), n[0], font=F(700, 32), fill='white', anchor='mm')
            g.text((130, y + 4), n, font=F(700, 30), fill=INK); g.text((130, y + 44), when, font=F(500, 24), fill=MUT)
            stars(g, 40, y + 92, s_, size=30); g.text((40, y + 140), txt, font=F(500, 30), fill=INK)
            y += 210
        banner(im, t, 3.8, 'WhatsApp · Pedro R.', '“¡Ya te he dejado las 5 estrellas en Google! 😊”', t1=5.0)
        stamp(im, t, 4.9, 'NO ES TU FICHA', BW // 2, 175, size=40, rot=-5)
        tag(g)
        return im


# ------------------------------------------------------------------ m04. EL NÚMERO DESCONOCIDO (llamada perdida + buzón)
class Desconocido:
    POV = 'POV: no coges un número desconocido porque “seguro que es spam” y era un cliente de verdad'
    DUR, PUNCH, FOCUS = 7.8, 6.0, (480, 790)
    SFX = ['ding@0.3', 'ding@1.0', 'ding@1.7', 'tick@2.4', 'pop@3.0', 'pop@4.0', 'typing:1.2@4.2', 'boom@6.0']

    def draw(self, t):
        if t < 2.8:
            im, g = lock_bg('10:12')
            ph = (t * 1.6) % 1
            for r in (0, .5):
                rr = 90 + 110 * ((ph + r) % 1); A = int(120 * (1 - (ph + r) % 1))
                l, lg = layer(); lg.ellipse((BW // 2 - rr, 470 - rr, BW // 2 + rr, 470 + rr), outline=(255, 255, 255, A), width=4); im.paste(l, (0, 0), l)
            g.ellipse((BW // 2 - 90, 380, BW // 2 + 90, 560), fill=(110, 114, 126)); g.text((BW // 2, 470), '?', font=F(800, 90), fill='white', anchor='mm')
            g.text((BW // 2, 640), 'Número desconocido', font=F(700, 50), fill='white', anchor='mm')
            g.text((BW // 2, 700), 'llamada entrante…', font=F(500, 30), fill=(200, 202, 210), anchor='mm')
            for x, col, lab in [(250, (235, 64, 52), 'Rechazar'), (710, (52, 199, 89), 'Aceptar')]:
                g.ellipse((x - 70, 780, x + 70, 920), fill=col); g.text((x, 950), lab, font=F(600, 28), fill='white', anchor='mm')
            if t >= 1.4:
                k = ease((t - 1.4) / .9); l, lg = layer(); cursor(lg, int(600 - 350 * k), int(1000 - 150 * k)); im.paste(l, (0, 0), l)
                g.text((BW // 2, 290), '“Será spam”', font=F(700, 40), fill=(255, 190, 150), anchor='mm')
            return im
        INK, MUT, LINE, RED_ = (28, 28, 30), (120, 120, 126), (228, 228, 232), (235, 64, 52)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.text((40, 70), 'Recientes', font=F(800, 50), fill=INK, anchor='lm')
        rows = [('Número desconocido', 'móvil · perdida', '10:12', True), ('Proveedor azulejos', 'móvil', 'ayer', False), ('Gestoría', 'fijo', 'ayer', False)]
        for i, (n, s, h, red) in enumerate(rows):
            yy = 150 + i * 100
            g.text((40, yy), n, font=F(700, 34), fill=RED_ if red else INK); g.text((40, yy + 44), s, font=F(500, 24), fill=MUT)
            g.text((BW - 40, yy + 20), h, font=F(500, 28), fill=MUT, anchor='rm'); g.line([(40, yy + 88), (BW, yy + 88)], fill=LINE, width=2)
        if t >= 3.0:
            k = ease((t - 3.0) / .35); l, lg = layer(); A = int(255 * k); y0 = 480 + int((1 - k) * 40)
            lg.rounded_rectangle((36, y0, BW - 36, y0 + 470), 26, fill=(242, 242, 247, A))
            lg.text((70, y0 + 40), 'Buzón de voz · 0:38', font=F(700, 32), fill=INK + (A,), anchor='lm')
            lg.text((70, y0 + 86), 'Transcripción', font=F(500, 24), fill=MUT + (A,), anchor='lm')
            im.paste(l, (0, 0), l)
            txt = '“Hola, os llamo para reformar la nave entera, lo quería empezar ya…'
            ft = F(600, 32); n = int(len(txt) * min(1, max(0, (t - 4.0) / 1.2)))
            for j, s in enumerate(wrap(txt[:n], ft, BW - 150)) if n else []:
                g.text((70, 610 + j * 44), s, font=ft, fill=INK)
            if t >= 5.4:
                kk = pop((t - 5.4) / .3); f = F(800, int(44 * max(.3, kk)))
                g.text((480, 760), 'bueno, pruebo', font=f, fill=RED_, anchor='mm')
                g.text((480, 816), 'con otra empresa”', font=f, fill=RED_, anchor='mm')
        tag(g)
        return im



# ------------------------------------------------------------------ m05. SOBRA UN CERO (app del banco + presupuesto diario)
class SobraCero:
    POV = 'POV: configuras la campaña “a 10 € al día” y el banco te avisa de que eran 100'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 830)
    DAYS = [(0.6, 'Lunes'), (1.3, 'Martes'), (2.0, 'Miércoles'), (2.7, 'Jueves')]
    SFX = [f'ding@{a}' for a, _ in DAYS] + ['count:2.6@0.6', 'pop@3.6', 'tick@4.4', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE, RED_ = (25, 28, 36), (110, 116, 128), (229, 232, 238), (220, 50, 50)
        im = Image.new('RGB', (BW, BH), (243, 245, 249)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 250), fill=(18, 60, 130))
        g.text((40, 50), 'Mi cuenta · Movimientos', font=F(600, 30), fill=(200, 215, 240), anchor='lm')
        n = sum(1 for a, _ in self.DAYS if t >= a); bal = 1240 - 100 * n
        if 0.6 <= t < 3.4: bal = 1240 - 400 * ease((t - .6) / 2.6)
        g.text((40, 140), eur(bal), font=F(800, 80), fill='white', anchor='lm')
        g.text((40, 210), 'Saldo disponible', font=F(500, 26), fill=(200, 215, 240), anchor='lm')
        for i, (ts, d) in enumerate(self.DAYS):
            if t < ts: continue
            k = ease((t - ts) / .3); yy = 280 + i * 104; A = int(255 * k); l, lg = layer()
            lg.rounded_rectangle((30, yy, BW - 30, yy + 90), 18, fill=(255, 255, 255, A))
            lg.ellipse((52, yy + 18, 106, yy + 72), fill=(8, 102, 255, A)); lg.text((79, yy + 45), 'A', font=F(800, 28), fill=(255, 255, 255, A), anchor='mm')
            lg.text((126, yy + 16), 'Plataforma de anuncios', font=F(700, 30), fill=INK + (A,))
            lg.text((126, yy + 54), d, font=F(500, 24), fill=MUT + (A,))
            lg.text((BW - 56, yy + 45), '-100,00 €', font=F(800, 34), fill=RED_ + (A,), anchor='rm')
            im.paste(l, (0, 0), l)
        if t >= 3.6:
            k = ease((t - 3.6) / .35); l, lg = layer(); A = int(255 * k); y0 = 745 + int((1 - k) * 60)
            lg.rounded_rectangle((30, y0 - 40, BW - 30, y0 + 250), 22, fill=(255, 255, 255, A), outline=LINE + (A,), width=2)
            lg.text((64, y0), 'Configuración del conjunto de anuncios', font=F(600, 26), fill=MUT + (A,))
            lg.text((64, y0 + 44), 'Presupuesto diario', font=F(700, 32), fill=INK + (A,))
            lg.rounded_rectangle((64, y0 + 100, BW - 64, y0 + 200), 14, outline=(8, 102, 255, A), width=3)
            lg.text((480, y0 + 150), '100,00 €', font=F(800, 56), fill=INK + (A,), anchor='mm')
            im.paste(l, (0, 0), l)
        if 4.4 <= t < 5.4:
            k = ease((t - 4.4) / .5); l, lg = layer(); cursor(lg, int(700 - 150 * k), int(1000 - 100 * k)); im.paste(l, (0, 0), l)
        stamp(im, t, 5.0, 'SOBRA UN CERO', 480, 770, size=38, rot=-6)
        tag(g)
        return im


# ------------------------------------------------------------------ m06. CLIENTES POTENCIALES SIN TELÉFONO (Excel)
class SinTelefono:
    POV = 'POV: te pasan la lista de “clientes potenciales” y la columna del teléfono está vacía'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    ROWS = [('Construcciones Ruiz', 'muy interesado'), ('Talleres Sanz', 'le conoce mi primo'), ('Clínica Dental Sol', 'llamar (buscar nº)'),
            ('Hostal El Arco', 'sale en Google creo'), ('Muebles Duero', 'me dijo que sí'), ('Gimnasio Forma', 'en verano mejor'),
            ('Asesoría Núñez', 'no sé el nombre'), ('Pastelería Mayor', '¿cerró?')]
    SFX = ['pop@0.3'] + [f'tick@{0.6 + i * .35:.2f}' for i in range(8)] + ['pop@3.8', 'pop@5.1', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE, GRN = (32, 33, 36), (95, 99, 104), (218, 220, 224), (16, 124, 65)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 84), fill=GRN); g.text((30, 42), 'clientes_potenciales_BUENO.xlsx', font=F(700, 30), fill='white', anchor='lm')
        g.rectangle((0, 84, BW, 150), fill=(248, 249, 250)); g.text((30, 117), 'fx', font=F(700, 28), fill=MUT, anchor='lm')
        g.text((90, 117), '' if t < 3.8 else '=C2:C9   (todo vacío)', font=F(600, 28), fill=INK, anchor='lm')
        cols = [(0, 60, ''), (60, 370, 'Nombre'), (370, 560, 'Teléfono'), (560, BW, 'Notas')]
        y0, rh = 150, 72
        g.rectangle((0, y0, BW, y0 + 56), fill=(241, 243, 244))
        for x0, x1, name in cols:
            g.text(((x0 + x1) // 2, y0 + 28), name, font=F(700, 26), fill=INK, anchor='mm'); g.line([(x1, y0), (x1, BH)], fill=LINE, width=2)
        for i in range(12):
            yy = y0 + 56 + i * rh; g.line([(0, yy + rh), (BW, yy + rh)], fill=LINE, width=2)
            g.text((30, yy + rh // 2), str(i + 2), font=F(500, 22), fill=MUT, anchor='mm')
            if i < len(self.ROWS) and t >= 0.6 + i * .35:
                n, nota = self.ROWS[i]
                g.text((72, yy + rh // 2), n, font=F(600, 25), fill=INK, anchor='lm')
                g.text((574, yy + rh // 2), nota, font=F(500, 24), fill=INK, anchor='lm')
        if t >= 3.8:
            k = ease((t - 3.8) / .3); l, lg = layer(); A = int(255 * k)
            lg.rectangle((370, y0 + 56, 560, y0 + 56 + 8 * rh), fill=(255, 80, 80, int(50 * k)), outline=(220, 40, 40, A), width=5)
            im.paste(l, (0, 0), l)
        card(im, t, 5.1, 'Teléfonos en la lista', '0 de 8', '“pero están muy interesados”', cy=560, big_size=90)
        tag(g)
        return im


# ------------------------------------------------------------------ m07. EL ÚLTIMO CAMBIO (carpeta de diseños)
class UltimoCambio:
    POV = 'POV: el cliente pide “un último cambio” en el anuncio'
    DUR, PUNCH, FOCUS = 7.6, 5.9, (480, 580)
    FILES = [(0.3, 'anuncio_final.png'), (0.9, 'anuncio_final2.png'), (1.5, 'anuncio_final_bueno.png'),
             (2.1, 'anuncio_FINAL_de_verdad.png'), (2.7, 'anuncio_final_ESTE_SI.png'), (3.3, 'anuncio_final_v14 (2).png')]
    SFX = [f'pop@{a}' for a, _ in FILES] + ['ding@4.2', 'pop@5.2', 'boom@5.9']

    def draw(self, t):
        INK, MUT, LINE = (30, 32, 36), (110, 112, 118), (226, 228, 232)
        im = Image.new('RGB', (BW, BH), (250, 250, 252)); g = ImageDraw.Draw(im)
        g.text((40, 60), 'Mis diseños › Cliente reformas', font=F(700, 34), fill=INK, anchor='lm')
        g.line([(0, 110), (BW, 110)], fill=LINE, width=2)
        cols = [(0, 0, 0), (255, 106, 26), (26, 115, 232), (52, 168, 83), (234, 67, 53), (160, 90, 220), (240, 180, 20)]
        for i, (ts, name) in enumerate(self.FILES):
            if t < ts: continue
            k = pop((t - ts) / .3); c, r = i % 2, i // 2
            x0, y0 = 40 + c * 450, 140 + r * 270; w, h = 430, 250
            l, lg = layer(); s = max(.05, min(1.1, k))
            cx, cy = x0 + w // 2, y0 + h // 2; ww, hh = int(w * s / 2), int(h * s / 2)
            lg.rounded_rectangle((cx - ww, cy - hh, cx + ww, cy + hh), 16, fill=(255, 255, 255, 255), outline=LINE + (255,), width=2)
            if k > .8:
                lg.rounded_rectangle((x0 + 16, y0 + 16, x0 + w - 16, y0 + 170), 10, fill=cols[i + 1] + (255,))
                lg.text((x0 + w // 2, y0 + 93), 'OFERTA', font=F(800, 44 + i * 4), fill=(255, 255, 255, 255), anchor='mm')
                f = F(600, 22); nm = name if f.getlength(name) < w - 30 else name[:26] + '…'
                lg.text((x0 + 16, y0 + 206), nm, font=f, fill=INK + (255,), anchor='lm')
            im.paste(l, (0, 0), l)
        banner(im, t, 4.2, 'WhatsApp · Cliente reformas', '“¿Y si volvemos a la primera versión?”', t1=5.3)
        card(im, t, 5.2, 'Tras 14 “últimos cambios”', 'La v1', 'era la buena', cy=580, big_size=100)
        return im


# ------------------------------------------------------------------ m08. EL CAMPO PRESUPUESTO (respuestas del formulario)
class CampoPresupuesto:
    POV = 'POV: añades al formulario “¿qué presupuesto tienes?” para filtrar a los curiosos'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    ANS = [(0.7, 'Poco'), (1.3, 'El mínimo'), (1.9, 'Depende de lo que cueste'), (2.5, '0'), (3.1, 'jajaja'), (3.7, '¿No era gratis?')]
    SFX = [f'pop@{a}' for a, _ in ANS] + ['pop@5.1', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE, PUR = (32, 33, 36), (95, 99, 104), (218, 220, 224), (103, 58, 183)
        im = Image.new('RGB', (BW, BH), (240, 235, 248)); g = ImageDraw.Draw(im)
        g.rounded_rectangle((30, 30, BW - 30, 200), 18, fill='white'); g.rectangle((30, 30, BW - 30, 44), fill=PUR)
        g.text((64, 96), 'Solicitud de presupuesto', font=F(800, 38), fill=INK, anchor='lm')
        n = sum(1 for a, _ in self.ANS if t >= a)
        g.text((64, 156), f'Respuestas ({n})', font=F(600, 28), fill=PUR, anchor='lm')
        g.rounded_rectangle((30, 220, BW - 30, BH - 30), 18, fill='white')
        g.text((64, 270), '¿Qué presupuesto tienes para marketing?', font=F(700, 30), fill=INK, anchor='lm')
        for i, (ts, a) in enumerate(self.ANS):
            if t < ts: continue
            k = ease((t - ts) / .3); yy = 320 + i * 104; A = int(255 * k); l, lg = layer()
            lg.rounded_rectangle((64, yy, BW - 64, yy + 86), 12, fill=(247, 248, 250, A), outline=LINE + (A,), width=2)
            lg.text((96, yy + 43), a, font=F(600, 34), fill=INK + (A,), anchor='lm')
            im.paste(l, (0, 0), l)
        card(im, t, 5.1, 'Curiosos filtrados', '0', 'pero ahora son sinceros', cy=560, big_size=120)
        tag(g)
        return im



# ------------------------------------------------------------------ m09. RECARGAR PAGOS (panel de pagos)
class Recargar:
    POV = 'POV: es el día del lanzamiento y recargas el panel de pagos cada tres minutos'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    SFX = [f'tick@{0.4 + i * .5:.1f}' for i in range(9)] + ['pop@5.1', 'boom@5.8']

    def draw(self, t):
        BG, INK, MUT, LINE, PUR = (246, 249, 252), (26, 31, 54), (105, 115, 134), (227, 232, 238), (99, 91, 255)
        im = Image.new('RGB', (BW, BH), BG); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 100), fill='white'); g.line([(0, 100), (BW, 100)], fill=LINE, width=2)
        g.text((40, 50), 'Pagos · Lanzamiento del curso', font=F(700, 32), fill=INK, anchor='lm')
        n = sum(1 for i in range(9) if t >= .4 + i * .5)
        spin = (t * 400) % 360
        cx, cy = BW - 70, 50
        l, lg = layer(); lg.arc((cx - 24, cy - 24, cx + 24, cy + 24), spin, spin + 270, fill=PUR + (255,), width=6); im.paste(l, (0, 0), l)
        g.rounded_rectangle((30, 130, BW - 30, 470), 20, fill='white', outline=LINE, width=2)
        g.text((64, 170), 'Ventas de hoy', font=F(600, 28), fill=MUT)
        g.text((64, 220), '0,00 €', font=F(800, 90), fill=INK)
        for x in range(64, BW - 64, 8): g.line([(x, 420), (x + 4, 420)], fill=(190, 196, 210), width=3)
        g.text((64, 434), '00:00', font=F(500, 22), fill=MUT); g.text((BW - 64, 434), 'ahora', font=F(500, 22), fill=MUT, anchor='ra')
        g.rounded_rectangle((30, 500, BW - 30, BH - 30), 20, fill='white', outline=LINE, width=2)
        g.text((64, 540), 'Actividad', font=F(700, 30), fill=INK)
        base_h = 20
        for i in range(min(n, 6)):
            yy = 600 + i * 58
            g.text((64, yy), f'Actualizado · 20:{base_h + (n - i) * 3:02d}', font=F(500, 27), fill=MUT)
            g.text((BW - 64, yy), 'sin pagos nuevos', font=F(600, 27), fill=INK, anchor='ra')
        g.rounded_rectangle((BW - 330, 540, BW - 64, 584), 22, fill=(237, 235, 255))
        g.text((BW - 197, 562), f'Recargas: {n * 5 + 2}', font=F(700, 24), fill=PUR, anchor='mm')
        card(im, t, 5.1, 'Veces que has recargado', '47', 'ventas nuevas: 0', cy=560, big_size=120)
        tag(g)
        return im


# ------------------------------------------------------------------ m10. HOLA {NOMBRE} (correo)
class HolaNombre:
    POV = 'POV: mandas la newsletter a toda tu base de datos y sale “Hola {nombre}”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    REPL = [(2.4, 'Re: Hola {nombre}', '¿Quién es {nombre}? Yo soy Luis.'), (3.1, 'Re: Hola {nombre}', 'Jajaja qué profesional todo'),
            (3.8, 'Re: Hola {nombre}', 'Hola {tu_empresa}, date de baja tú.')]
    SFX = ['pop@0.3', 'tick@1.4', 'ding@2.4', 'ding@3.1', 'ding@3.8', 'pop@5.1', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (32, 33, 36), (95, 99, 104), (232, 234, 237)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 100), fill=(246, 248, 252)); g.text((40, 50), 'Enviados', font=F(700, 34), fill=INK, anchor='lm')
        g.rounded_rectangle((30, 120, BW - 30, 460), 18, fill=(250, 250, 252), outline=LINE, width=2)
        g.text((64, 160), 'Asunto: ¡Novedades de octubre!', font=F(700, 30), fill=INK)
        g.text((64, 206), 'Para: toda la lista · enviado', font=F(500, 24), fill=MUT)
        body = 'Hola {nombre}, sabemos que te encanta {producto_favorito}…'
        n = int(len(body) * min(1, max(0, (t - .3) / 1.0)))
        ft = F(600, 34)
        for j, s_ in enumerate(wrap(body[:n], ft, BW - 140)):
            g.text((64, 270 + j * 48), s_, font=ft, fill=INK)
        if t >= 1.4:
            k = ease((t - 1.4) / .3)
            l, lg = layer(); lg.rounded_rectangle((64, 400, 64 + int(300 * k), 440), 20, fill=(52, 168, 83, 255))
            if k > .8: lg.text((214, 420), 'Enviado', font=F(700, 24), fill=(255, 255, 255, 255), anchor='mm')
            im.paste(l, (0, 0), l)
        g.text((40, 500), 'Recibidos', font=F(700, 30), fill=INK)
        for i, (ts, sub, txt) in enumerate(self.REPL):
            if t < ts: continue
            k = ease((t - ts) / .3); yy = 550 + i * 130; A = int(255 * k); l, lg = layer()
            lg.rectangle((0, yy - 6, BW, yy + 114), fill=(252, 244, 232, A))
            lg.ellipse((40, yy + 10, 100, yy + 70), fill=(189, 193, 198, A)); lg.text((70, yy + 40), 'R', font=F(700, 28), fill=(255, 255, 255, A), anchor='mm')
            lg.text((124, yy + 6), sub, font=F(800, 28), fill=INK + (A,))
            lg.text((124, yy + 50), txt, font=F(500, 27), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
        card(im, t, 5.1, 'Suscriptores que se llaman', '{nombre}', 'todos, al parecer', cy=560, big_size=80)
        tag(g)
        return im


# ------------------------------------------------------------------ m11. EL ANUNCIO "PRUEBA NO PUBLICAR" (Administrador de anuncios)
class PruebaNoPublicar:
    POV = 'POV: tu mejor anuncio del mes es el que subiste por error sin terminar'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 640)
    SFX = ['pop@0.4', 'pop@1.2', 'pop@2.3', 'count:1.4@2.5', 'pop@4.4', 'boom@5.8']

    def draw(self, t):
        BG, INK, MUT, LINE, GRN = (242, 244, 247), (28, 30, 33), (101, 103, 107), (221, 223, 226), (49, 162, 76)
        im = Image.new('RGB', (BW, BH), BG); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill='white'); g.line([(0, 110), (BW, 110)], fill=LINE, width=2)
        g.text((40, 55), 'Administrador de anuncios · Anuncios', font=F(700, 32), fill=INK, anchor='lm')
        g.text((210, 150), 'Anuncio', font=F(600, 24), fill=MUT, anchor='lm'); g.text((BW - 50, 150), 'Coste por lead', font=F(600, 24), fill=MUT, anchor='rm')
        rows = [(0.4, 'Vídeo corporativo (3 días de rodaje)', 38.20, (40, 60, 90), 'VÍDEO'),
                (1.2, 'Carrusel revisado por todo el equipo', 27.90, (255, 106, 26), '1/5'),
                (2.3, 'prueba NO PUBLICAR', 3.10, (200, 200, 205), 'TEXTO AQUÍ')]
        for i, (ts, name, cpl, col, th) in enumerate(rows):
            if t < ts: continue
            k = ease((t - ts) / .3); yy = 190 + i * 170 + (i == 2) * 60; A = int(255 * k); l, lg = layer()
            win = i == 2 and t >= 4.4
            lg.rounded_rectangle((30, yy, BW - 30, yy + 150), 16, fill=(255, 255, 255, A), outline=(GRN if win else LINE) + (A,), width=5 if win else 2)
            lg.rounded_rectangle((50, yy + 20, 180, yy + 130), 10, fill=col + (A,))
            lg.text((115, yy + 75), th, font=F(700, 18 if len(th) > 5 else 26), fill=(255, 255, 255, A) if i < 2 else (120, 120, 126, A), anchor='mm')
            f = F(700, 27); nm = name if f.getlength(name) < 500 else wrap(name, f, 500)[0] + '…'
            lg.text((210, yy + 50), nm, font=f, fill=INK + (A,), anchor='lm')
            lg.text((210, yy + 98), 'Activo' if i < 2 else 'Activo (sin querer)', font=F(500, 24), fill=(GRN if i < 2 else (200, 120, 0)) + (A,), anchor='lm')
            v = cpl if i < 2 else 3.10 + (60 - 3.10) * (1 - ease((t - 2.5) / 1.4))
            lg.text((BW - 56, yy + 75), eur(v), font=F(800, 38), fill=(GRN if win else INK) + (A,), anchor='rm')
            im.paste(l, (0, 0), l)
        stamp(im, t, 4.4, 'EL MEJOR DEL MES', 480, 800, col=(49, 162, 76), size=38, rot=-4)
        tag(g)
        return im


# ------------------------------------------------------------------ m12. EL MISMO CLIENTE CINCO VECES (CRM)
class Duplicados:
    POV = 'POV: abres el CRM para llamar a un cliente y está guardado cinco veces'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    RES = [(1.5, 'Paco Fontanería', 'sin teléfono'), (1.9, 'paco fontaneria 2', 'móvil antiguo'), (2.3, 'Paco (NO LLAMAR)', '¿por qué?'),
           (2.7, 'Paco el bueno', 'creado por: nadie'), (3.1, 'PACO FONTANERO NUEVO', 'duplicado de duplicado')]
    SFX = ['typing:0.9@0.3'] + [f'pop@{a}' for a, _, _ in RES] + ['pop@5.1', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE, GRN = (38, 41, 44), (110, 116, 122), (226, 229, 232), (38, 140, 90)
        im = Image.new('RGB', (BW, BH), (247, 248, 249)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 100), fill=(34, 40, 49)); g.text((40, 50), 'CRM · Contactos', font=F(700, 32), fill='white', anchor='lm')
        g.rounded_rectangle((30, 130, BW - 30, 210), 16, fill='white', outline=GRN, width=3)
        q = 'Paco'[:int(4 * min(1, max(0, (t - .3) / .9)))]
        g.text((70, 170), '🔍' if False else 'Buscar:', font=F(600, 30), fill=MUT, anchor='lm')
        g.text((200, 170), q + ('|' if int(t * 3) % 2 else ''), font=F(700, 32), fill=INK, anchor='lm')
        n = sum(1 for a, _, _ in self.RES if t >= a)
        if n: g.text((40, 250), f'{n} resultados', font=F(600, 26), fill=MUT, anchor='lm')
        for i, (ts, name, note) in enumerate(self.RES):
            if t < ts: continue
            k = ease((t - ts) / .3); yy = 290 + i * 128; A = int(255 * k); l, lg = layer()
            lg.rounded_rectangle((30, yy, BW - 30, yy + 112), 14, fill=(255, 255, 255, A), outline=LINE + (A,), width=2)
            lg.ellipse((52, yy + 26, 112, yy + 86), fill=(120, 140, 160, A)); lg.text((82, yy + 56), 'P', font=F(700, 28), fill=(255, 255, 255, A), anchor='mm')
            lg.text((134, yy + 22), name, font=F(700, 32), fill=INK + (A,))
            lg.text((134, yy + 66), note, font=F(500, 25), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
        card(im, t, 5.1, 'Clientes reales', '1', 'y nadie sabe cuál es el bueno', cy=560, big_size=120)
        tag(g)
        return im


NEW = {'m01-descuento': Descuento, 'm02-mismo-lead': MismoLead, 'm03-resena-ajena': ResenaAjena, 'm04-desconocido': Desconocido,
       'm05-sobra-cero': SobraCero, 'm06-sin-telefono': SinTelefono, 'm07-ultimo-cambio': UltimoCambio, 'm08-campo-presupuesto': CampoPresupuesto,
       'm09-recargar': Recargar, 'm10-hola-nombre': HolaNombre, 'm11-prueba-no-publicar': PruebaNoPublicar, 'm12-duplicados': Duplicados}
