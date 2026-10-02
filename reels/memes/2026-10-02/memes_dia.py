"""Memes del día 2026-10-02: 20 reels POV nuevos (m01…m20). Motor: toolkit/reels/pov_reel.py."""
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


def card(im, t, t0, top, big, sub, cy=560, big_size=84, col=RED, cw=470, ch=340, cx=BW // 2):
    """Tarjeta final compacta (cabe entera en el zoom del remate) con fondo atenuado."""
    if t < t0: return
    kk = pop((t - t0) / .35); l, lg = layer()
    lg.rectangle((0, 0, BW, BH), fill=(0, 0, 0, int(120 * min(1, (t - t0) / .25))))
    sw, sh = int(cw * kk), int(ch * kk)
    lg.rounded_rectangle((cx - sw // 2, cy - sh // 2, cx + sw // 2, cy + sh // 2), 28, fill=(20, 20, 22, 255))
    if kk > .9:
        tf = F(600, 28)
        while tf.getlength(top) > cw - 40 and tf.size > 18: tf = F(600, tf.size - 2)
        lg.text((cx, cy - ch * .34), top, font=tf, fill=GRY, anchor='mm')
        bf = F(800, big_size)
        while bf.getlength(big) > cw - 40 and bf.size > 30: bf = F(800, bf.size - 4)
        lg.text((cx, cy - ch * .04), big, font=bf, fill=col, anchor='mm')
        sf = F(600, 26); ls = wrap(sub, sf, cw - 50)[:2]
        for j, s_ in enumerate(ls):
            lg.text((cx, cy + ch * .27 + (j - (len(ls) - 1) / 2) * 34), s_, font=sf, fill=GRY, anchor='mm')
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


def lock_bg(hour='21:47', date='viernes, 2 de octubre'):
    im = Image.new('RGB', (BW, BH), (18, 22, 34)); g = ImageDraw.Draw(im)
    for yy in range(BH):
        c = int(18 + 30 * yy / BH); g.line([(0, yy), (BW, yy)], fill=(c, c - 4, c + 22))
    g.text((BW // 2, 60), date, font=F(600, 30), fill=(220, 222, 230), anchor='mm')
    g.text((BW // 2, 170), hour, font=F(800, 150), fill='white', anchor='mm')
    return im, g


INK, MUT, LINE = (32, 33, 36), (95, 99, 104), (228, 230, 233)


def appbar(g, title, sub=None, col=(28, 43, 66)):
    g.rectangle((0, 0, BW, 130), fill=col)
    g.text((40, 44 if sub else 65), title, font=F(700, 38), fill='white', anchor='lm')
    if sub: g.text((40, 94), sub, font=F(500, 26), fill=(190, 200, 215), anchor='lm')


BLU = (8, 102, 255)


def statusdot(g, x, y, label, col):
    g.ellipse((x, y - 10, x + 20, y + 10), fill=col); g.text((x + 32, y), label, font=F(600, 28), fill=col, anchor='lm')



# ------------------------------------------------------------------ m01. SUBES PRECIOS (notificaciones del móvil)
class SubesPrecios:
    POV = 'POV: subes los precios un 10 % y llevas una semana sin dormir esperando que se vayan todos'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    NOTIS = [(0.9, 'Cliente (clínica dental)', 'Vale, perfecto'), (1.7, 'Cliente (taller)', 'Ok, sin problema'),
             (2.5, 'Cliente (gimnasio)', 'Lógico, todo sube'), (3.3, 'Cliente (inmobiliaria)', '¿Te pago ya la de octubre?')]
    SFX = ['pop@0.3', 'ding@0.9', 'ding@1.7', 'ding@2.5', 'ding@3.3', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im, g = lock_bg('08:03')
        if t >= .3:
            k = ease((t - .3) / .3); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((36, 290, BW - 36, 390), 24, fill=(60, 60, 66, int(220 * k)))
            lg.text((70, 340), 'Correo enviado: “Nuevas tarifas desde octubre”', font=F(600, 28), fill=(230, 230, 235, A), anchor='lm')
            im.paste(l, (0, 0), l)
        for i, (ts, app, txt) in enumerate(self.NOTIS):
            if t < ts: continue
            y = 410 + i * 136; k = ease((t - ts) / .3); l, lg = layer(); A = int(255 * k); dy = int((1 - k) * -30)
            lg.rounded_rectangle((36, y + dy, BW - 36, y + 120 + dy), 26, fill=(44, 44, 50, int(240 * k)))
            lg.rounded_rectangle((60, y + 30 + dy, 120, y + 90 + dy), 16, fill=(37, 211, 102, A))
            lg.text((90, y + 60 + dy), 'W', font=F(800, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((146, y + 22 + dy), app, font=F(500, 24), fill=(180, 180, 185, A))
            lg.text((146, y + 58 + dy), txt, font=F(700, 32), fill=(255, 255, 255, A))
            im.paste(l, (0, 0), l)
        card(im, t, 5.0, 'Clientes que se han ido', '0', 'y tú con ojeras desde el lunes', cy=600, big_size=140)
        g = ImageDraw.Draw(im); tag(g, dark=True)
        return im


# ------------------------------------------------------------------ m02. OFERTA 24 H (panel de pagos)
class Oferta24h:
    POV = 'POV: lanzas una oferta “solo 24 horas” y miras el panel de pagos durante todo el día'
    DUR, PUNCH, FOCUS = 7.8, 6.0, (480, 600)
    HOURS = [(0.6, '09:00', None), (1.2, '13:00', None), (1.8, '17:00', None), (2.4, '21:00', None),
             (3.1, '23:57', 'Pago recibido · 197,00 €'), (3.5, '23:58', 'Pago recibido · 197,00 €'),
             (3.9, '23:59', 'Pago recibido · 197,00 €'), (4.3, '23:59', 'Pago recibido · 197,00 €')]
    SFX = ['pop@0.3', 'tick@0.6', 'tick@1.2', 'tick@1.8', 'tick@2.4', 'ding@3.1', 'ding@3.5', 'ding@3.9', 'ding@4.3', 'pop@5.2', 'boom@6.0']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (246, 248, 250)); g = ImageDraw.Draw(im)
        appbar(g, 'Pagos', 'Oferta 24 h · Curso de ventas', col=(50, 40, 120))
        g.rounded_rectangle((30, 160, BW - 30, 300), 22, fill='white', outline=LINE, width=2)
        g.text((64, 200), 'Ingresos de hoy', font=F(600, 28), fill=MUT, anchor='lm')
        n = sum(1 for ts, _, p in self.HOURS if p and t >= ts)
        g.text((64, 255), eur(197 * n), font=F(800, 50), fill=INK, anchor='lm')
        for i, (ts, h, p) in enumerate(self.HOURS):
            if t < ts: continue
            y = 320 + i * 78; k = ease((t - ts) / .25); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((30, y, BW - 30, y + 66), 14, fill=(255, 255, 255, A))
            lg.text((64, y + 33), h, font=F(700, 28), fill=INK + (A,), anchor='lm')
            lg.text((200, y + 33), p or 'Sin pagos', font=F(600, 28), fill=((0, 140, 80) if p else (160, 162, 168)) + (A,), anchor='lm')
            im.paste(l, (0, 0), l)
        card(im, t, 5.2, 'Hora de la primera venta', '23:57', 'y tú ya escribiendo el correo de “gracias igualmente”', cy=600, big_size=110)
        tag(g)
        return im


# ------------------------------------------------------------------ m03. "SIN PRISA" (bandeja de correo)
class SinPrisa:
    POV = 'POV: el cliente te pide un cambio en la web y te dice “sin prisa, cuando puedas”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    MAILS = [(0.4, '10:02', 'Cambio en la web', 'Sin prisa, cuando puedas', False),
             (1.4, '10:41', 'Re: Cambio en la web', '¿Cómo lo llevas?', False),
             (2.3, '11:15', 'Re: Re: Cambio en la web', '¿Lo tienes ya?', True),
             (3.2, '11:30', 'Te he llamado', 'Tienes 3 llamadas perdidas mías', True),
             (4.1, '11:32', 'Re: Re: Re: Cambio', 'Es que lo necesito para ya', True)]
    SFX = ['pop@0.4', 'ding@1.4', 'ding@2.3', 'ding@3.2', 'ding@4.1', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill=(242, 246, 252)); g.text((40, 55), 'Recibidos', font=F(700, 38), fill=INK, anchor='lm')
        unread = sum(1 for m in self.MAILS if t >= m[0])
        g.text((BW - 40, 55), f'{unread} sin leer' if unread else '', font=F(600, 26), fill=(200, 50, 40), anchor='rm')
        for i, (ts, h, subj, prev, bold) in enumerate(reversed(self.MAILS)):
            pass
        shown = [m for m in self.MAILS if t >= m[0]][::-1]
        for i, (ts, h, subj, prev, bold) in enumerate(shown):
            y = 130 + i * 160; k = ease((t - ts) / .3); l, lg = layer(); A = int(255 * k)
            lg.ellipse((40, y + 30, 110, y + 100), fill=(52, 120, 200, A)); lg.text((75, y + 65), 'R', font=F(800, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((135, y + 26), 'Cliente (Restaurante La Plaza)', font=F(700, 28), fill=INK + (A,))
            lg.text((BW - 40, y + 30), h, font=F(600, 24), fill=MUT + (A,), anchor='ra')
            lg.text((135, y + 66), subj, font=F(700 if bold else 600, 28), fill=INK + (A,))
            lg.text((135, y + 104), prev, font=F(500, 26), fill=((200, 50, 40) if bold else MUT) + (A,))
            lg.line([(40, y + 150), (BW - 40, y + 150)], fill=LINE + (A,), width=2)
            im.paste(l, (0, 0), l)
        card(im, t, 5.0, '“Sin prisa” ha durado', '90 min', 'cinco correos y tres llamadas', cy=600, big_size=110)
        tag(g)
        return im


# ------------------------------------------------------------------ m04. MÓVIL EN EL COCHE (llamadas perdidas)
class MovilCoche:
    POV = 'POV: el lead lleva 3 semanas sin cogerte el teléfono y te dejas el móvil 20 minutos en el coche'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    CALLS = [(0.6, '12:01'), (1.1, '12:04'), (1.6, '12:07'), (2.1, '12:11'), (2.6, '12:15'), (3.1, '12:19')]
    SFX = ['pop@0.3', 'tick@0.6', 'tick@1.1', 'tick@1.6', 'tick@2.1', 'tick@2.6', 'tick@3.1', 'ding@3.8', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (250, 250, 252)); g = ImageDraw.Draw(im)
        g.text((40, 60), 'Recientes', font=F(800, 46), fill=INK, anchor='lm')
        g.rounded_rectangle((BW - 290, 34, BW - 40, 88), 27, fill=(232, 234, 238))
        g.text((BW - 165, 61), 'Perdidas', font=F(700, 26), fill=INK, anchor='mm')
        for i, (ts, h) in enumerate(self.CALLS):
            if t < ts: continue
            y = 120 + i * 108; k = ease((t - ts) / .25); l, lg = layer(); A = int(255 * k)
            lg.ellipse((40, y + 20, 108, y + 88), fill=(150, 160, 175, A)); lg.text((74, y + 54), 'L', font=F(800, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((132, y + 24), 'Lead (reforma de cocina)', font=F(700, 32), fill=(217, 48, 37, A))
            lg.text((132, y + 66), 'Llamada perdida · móvil', font=F(500, 24), fill=MUT + (A,))
            lg.text((BW - 40, y + 54), h, font=F(600, 28), fill=MUT + (A,), anchor='rm')
            lg.line([(132, y + 104), (BW - 40, y + 104)], fill=LINE + (A,), width=2)
            im.paste(l, (0, 0), l)
        banner(im, t, 3.8, 'WhatsApp', 'Lead (reforma de cocina)', t1=None, y=790, sub='Bueno, ya veo que no te interesa')
        card(im, t, 5.0, 'Llamadas perdidas en 20 min', '6', 'del lead que no contestaba nunca', cy=600, big_size=140)
        tag(g)
        return im


NEW = {'m01-subes-precios': SubesPrecios, 'm02-oferta-24h': Oferta24h, 'm03-sin-prisa': SinPrisa, 'm04-movil-coche': MovilCoche}
