"""Memes del día 2026-10-04: 20 reels POV nuevos (m01…m20). Motor: toolkit/reels/pov_reel.py."""
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



# ------------------------------------------------------------------ base: chat de mensajes directos de Instagram
IG_OUT, IG_IN, IG_TXT, IG_MUT = (118, 72, 245), (38, 38, 40), (245, 245, 247), (150, 150, 155)


class IGChat:
    """Mensajes directos de Instagram: USER, MSGS [(t, 'in'|'out', texto)], TYPING, SEEN (t del 'Visto')."""
    USER, LETTER, MSGS, TYPING, SEEN = 'usuario', 'U', [], [], None

    def base(self, t):
        im = Image.new('RGB', (BW, BH), (0, 0, 0)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 140), fill=(12, 12, 14)); g.line([(0, 140), (BW, 140)], fill=(40, 40, 44), width=2)
        g.line([(52, 70), (36, 55), (52, 40)], fill=IG_TXT, width=5)
        g.ellipse((76, 28, 160, 112), fill=(200, 80, 120)); g.ellipse((80, 32, 156, 108), fill=(60, 60, 66))
        g.text((118, 70), self.LETTER, font=F(700, 36), fill='white', anchor='mm')
        g.text((184, 34), self.USER, font=F(700, 34), fill=IG_TXT)
        on = any(a <= t < b for a, b in self.TYPING)
        g.text((184, 80), 'Escribiendo...' if on else 'Activo ahora', font=F(500, 24), fill=IG_MUT)
        return im, g

    def bubbles(self, im, t, y=180):
        mf = F(500, 38)
        for m in self.MSGS:
            ts, side, text = m
            if t < ts: continue
            k = ease((t - ts) / .3); out = side == 'out'; dy = int((1 - k) * 26); a = int(255 * k)
            ls = []
            for para in text.split('\n'): ls += wrap(para, mf, 620)
            bw = max(140, max(mf.getlength(s) for s in ls) + 56); bh = len(ls) * 48 + 40
            x0 = BW - 30 - bw if out else 96; x1 = x0 + bw
            l, lg = layer()
            if not out:
                lg.ellipse((30, y + bh - 52 + dy, 82, y + bh + dy), fill=(60, 60, 66, a))
                lg.text((56, y + bh - 26 + dy), self.LETTER, font=F(700, 24), fill=(255, 255, 255, a), anchor='mm')
            lg.rounded_rectangle((x0, y + dy, x1, y + bh + dy), 30, fill=(IG_OUT if out else IG_IN) + (a,))
            for j, s in enumerate(ls): lg.text((x0 + 28, y + 18 + j * 48 + dy), s, font=mf, fill=IG_TXT + (a,))
            im.paste(l, (0, 0), l); y += bh + 14
            last_out = (x1, y)
        if self.SEEN and t >= self.SEEN and not any(t >= m[0] and m[1] == 'in' and m[0] > self.SEEN for m in self.MSGS):
            ImageDraw.Draw(im).text((BW - 34, y), 'Visto', font=F(500, 24), fill=IG_MUT, anchor='ra'); y += 40
        for a0, b0 in self.TYPING:
            if a0 <= t < b0:
                k = ease((t - a0) / .15) * ease((b0 - t) / .12); A = int(255 * k); l, lg = layer()
                lg.rounded_rectangle((96, y + 6, 236, y + 80), 30, fill=IG_IN + (A,))
                for n in range(3):
                    ph = max(0, math.sin(t * 7 - n * .9)); cx, cy = 132 + n * 34, y + 43 - int(ph * 8)
                    lg.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=IG_MUT + (int(A * (.55 + .45 * ph)),))
                im.paste(l, (0, 0), l)
        return y

    def footer(self, g):
        g.rounded_rectangle((24, BH - 100, BW - 24, BH - 24), 38, outline=(60, 60, 66), width=2, fill=(18, 18, 20))
        g.ellipse((40, BH - 90, 96, BH - 34), fill=(55, 151, 240))
        g.text((116, BH - 62), 'Enviar mensaje...', font=F(500, 32), fill=IG_MUT, anchor='lm')


# ------------------------------------------------------------------ m01. PRECIO ORIENTATIVO (WhatsApp)
class Orientativo(WAChat):
    POV = 'POV: el lead te pide “solo un precio orientativo” y le das el más ajustado que puedes'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    NAME, LETTER, HOUR = 'Lead (reforma de baño)', 'L', '19:1'
    MSGS = [(0.3, 'in', 'Hola, ¿me das un precio orientativo para reformar el baño?'),
            (1.3, 'out', 'Claro. Orientativo, desde 4.900 €'),
            (2.6, 'in', 'Uff, carísimo'),
            (3.5, 'in', 'Mi vecino lo hizo por 1.200')]
    TYPING = [(2.0, 2.55)]
    SFX = ['pop@0.3', 'pop@1.3', 'typing:0.5@2.0', 'pop@2.6', 'pop@3.5', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g)
        card(im, t, 5.0, 'Tiempo en decir “carísimo”', '3 s', 'y el baño del vecino sigue a medias', cy=560, big_size=130)
        tag(g, dark=True)
        return im


# ------------------------------------------------------------------ m02. DESCUENTO SIN PRECIO (WhatsApp)
class DescuentoSinPrecio(WAChat):
    POV = 'POV: el lead te pregunta cuánto descuento le haces y aún no sabe ni el precio'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    NAME, LETTER, HOUR = 'Lead (ventanas)', 'V', '17:4'
    MSGS = [(0.3, 'in', 'Hola, vengo del anuncio'),
            (1.1, 'out', '¡Hola! ¿Qué medidas tienen?'),
            (2.3, 'in', '¿Cuánto descuento me haces?'),
            (3.2, 'out', '¿Sobre qué precio?'),
            (4.2, 'in', 'Sobre el que me vayas a dar')]
    TYPING = [(1.7, 2.25), (3.6, 4.15)]
    SFX = ['pop@0.3', 'pop@1.1', 'typing:0.55@1.7', 'pop@2.3', 'pop@3.2', 'typing:0.55@3.6', 'pop@4.2', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g)
        card(im, t, 5.0, 'Precio que le has dado', 'Ninguno', 'y ya quiere un 20 % menos', cy=560, big_size=96)
        tag(g, dark=True)
        return im


# ------------------------------------------------------------------ m03. "INFO DE QUÉ" (mensajes directos de Instagram)
class InfoDeQue(IGChat):
    POV = 'POV: te escriben “info” por privado, les mandas toda la información y te contestan esto'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    USER, LETTER = 'usuario_8812', 'U'
    MSGS = [(0.3, 'in', 'info'),
            (1.0, 'out', '¡Hola! Te cuento: montamos tu campaña, grabamos los anuncios y te pasamos los leads al momento.'),
            (1.9, 'out', 'Precio: 290 €/mes, sin permanencia. ¿Te llamo mañana y lo vemos?'),
            (4.1, 'in', 'info de qué')]
    TYPING = [(3.1, 4.0)]
    SEEN = 2.6
    SFX = ['pop@0.3', 'pop@1.0', 'pop@1.9', 'tick@2.6', 'typing:0.9@3.1', 'pop@4.1', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g)
        card(im, t, 5.0, 'Lo que ha leído de tu mensaje', 'Nada', 'y le habías puesto hasta el precio', cy=560, big_size=110)
        tag(g, dark=True)
        return im


# ------------------------------------------------------------------ m04. NOTAS DEL CRM
class NotasCRM:
    POV = 'POV: lees las notas que ha dejado el comercial nuevo en cada lead del CRM'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    ROWS = [(0.5, 'Lead 1042 · Reforma integral', 'majo'), (1.1, 'Lead 1043 · Tejado', 'llamar'),
            (1.7, 'Lead 1044 · Cocina', 'el del perro'), (2.3, 'Lead 1045 · Baño', 'no sé'),
            (2.9, 'Lead 1046 · Fachada', 'dice que sí pero no'), (3.5, 'Lead 1047 · Ventanas', 'ojo'),
            (4.1, 'Lead 1048 · Suelo', 'ver')]
    SFX = ['pop@0.2'] + [f'tick@{r[0]}' for r in ROWS] + ['pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (245, 247, 250)); g = ImageDraw.Draw(im)
        appbar(g, 'CRM · Leads', 'Comercial: el nuevo · 7 leads esta semana', col=(23, 92, 84))
        g.rectangle((0, 130, BW, 190), fill=(232, 236, 240))
        g.text((40, 160), 'Lead', font=F(700, 26), fill=MUT, anchor='lm')
        g.text((600, 160), 'Notas', font=F(700, 26), fill=MUT, anchor='lm')
        for i, (ts, name, note) in enumerate(self.ROWS):
            y = 200 + i * 98
            g.rectangle((0, y, BW, y + 90), fill='white')
            g.text((40, y + 45), name, font=F(600, 28), fill=INK, anchor='lm')
            if t >= ts:
                k = ease((t - ts) / .25); l, lg = layer(); A = int(255 * k)
                lg.rounded_rectangle((585, y + 18, 585 + F(700, 28).getlength(note) + 30, y + 72), 12, fill=(255, 243, 205, A))
                lg.text((600, y + 45), note, font=F(700, 28), fill=(120, 80, 0, A), anchor='lm')
                im.paste(l, (0, 0), l)
            else:
                g.text((600, y + 45), '…', font=F(600, 28), fill=(190, 192, 196), anchor='lm')
        card(im, t, 5.0, 'Información útil en las notas', '0', 'pero el del perro era muy majo', cy=560, big_size=140)
        tag(g)
        return im


NEW = {'m01-orientativo': Orientativo, 'm02-descuento-sin-precio': DescuentoSinPrecio,
       'm03-info-de-que': InfoDeQue, 'm04-notas-crm': NotasCRM}
