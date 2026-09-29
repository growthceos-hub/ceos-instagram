"""Memes del día 2026-09-29: 20 reels POV nuevos (m01…m20). Motor: toolkit/reels/pov_reel.py."""
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


def lock_bg(hour='21:47', date='martes, 29 de septiembre'):
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


# ------------------------------------------------------------------ m01. PRECIO DE AMIGO (WhatsApp)
class PrecioAmigo(WAChat):
    POV = 'POV: alguien que conociste ayer en un evento te pide “precio de amigo”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    NAME, LETTER, HOUR = 'Carlos (evento de ayer)', 'C', '10:1'
    MSGS = [(0.3, 'in', '¡Buenas! Soy Carlos, el del networking de ayer.'),
            (1.3, 'in', 'Oye, lo de los anuncios… ¿me haces precio de amigo?'),
            (2.6, 'out', 'Claro. ¿Desde cuándo somos amigos?'),
            (4.0, 'in', 'Desde ayer, hombre. Si somos como hermanos.')]
    TYPING = [(3.1, 3.9)]
    SFX = ['pop@0.3', 'pop@1.3', 'pop@2.6', 'typing:0.8@3.1', 'pop@4.0', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g)
        card(im, t, 5.0, 'Tiempo de amistad', '14 horas', 'y ya quiere la mitad de precio', cy=600)
        return im


# ------------------------------------------------------------------ m02. PÚBLICO: TODA ESPAÑA (administrador de anuncios)
class PublicoEspana:
    POV = 'POV: abres la campaña de la peluquería de barrio que montó la agencia anterior'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    ROWS = [(0.4, 'Ubicación', 'España (todo el país)'), (1.2, 'Edad', '18 – 65+'),
            (2.0, 'Intereses', 'Pelo, calvicie, tractores'), (2.8, 'Idioma', 'Todos')]
    SFX = ['pop@0.4', 'pop@1.2', 'pop@2.0', 'pop@2.8', 'count:1.0@3.5', 'pop@4.8', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (240, 242, 245)); g = ImageDraw.Draw(im)
        appbar(g, 'Administrador de anuncios', 'Peluquería del barrio · Conjunto de anuncios 1')
        g.rounded_rectangle((30, 160, BW - 30, 640), 22, fill='white', outline=LINE, width=2)
        g.text((64, 200), 'Público', font=F(800, 38), fill=INK, anchor='lm')
        for i, (ts, k_, v) in enumerate(self.ROWS):
            if t < ts: continue
            k = ease((t - ts) / .3); y = 250 + i * 95; l, lg = layer(); A = int(255 * k)
            lg.text((64, y + 30), k_, font=F(600, 30), fill=MUT + (A,), anchor='lm')
            lg.rounded_rectangle((320, y, BW - 64, y + 62), 14, fill=(231, 243, 255, A))
            lg.text((344, y + 31), v, font=F(700, 31), fill=(20, 80, 160, A), anchor='lm')
            im.paste(l, (0, 0), l)
        if t >= 3.5:
            k = min(1, (t - 3.5) / 1.0); n = int(31_400_000 * ease(k))
            g.rounded_rectangle((30, 670, BW - 30, 960), 22, fill='white', outline=LINE, width=2)
            g.text((64, 715), 'Tamaño estimado del público', font=F(600, 30), fill=MUT, anchor='lm')
            g.text((64, 800), f'{n:,}'.replace(',', '.') + ' personas', font=F(800, 60), fill=INK, anchor='lm')
            g.rectangle((64, 860, BW - 64, 876), fill=(230, 232, 236)); g.rectangle((BW - 110, 860, BW - 64, 876), fill=(230, 60, 60))
            g.text((64, 910), 'Presupuesto: 5 € al día', font=F(600, 28), fill=MUT, anchor='lm')
        card(im, t, 4.8, 'Público de la peluquería', '31,4 M', 'para un local de cuatro sillas', cy=560)
        tag(g)
        return im


# ------------------------------------------------------------------ m03. SEIS "FINAL" (explorador de archivos)
class CarpetaFinal:
    POV = 'POV: vas a mandar el presupuesto definitivo y en la carpeta hay seis “final”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    FILES = [(0.3, 'presupuesto.pdf', '3 mar'), (0.8, 'presupuesto_final.pdf', '5 mar'),
             (1.3, 'presupuesto_final_v2.pdf', '12 mar'), (1.8, 'presupuesto_FINAL_bueno.pdf', '2 abr'),
             (2.3, 'presupuesto_final_ahora_si.pdf', '20 may'), (2.8, 'presupuesto_final_NO_TOCAR.pdf', '28 sep'),
             (3.3, 'presupuesto_final_v2 (copia).pdf', 'hoy')]
    SFX = [f'tick@{a}' for a, _, _ in FILES] + ['pop@4.2', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (250, 250, 251)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 120), fill=(236, 237, 240)); g.line([(0, 120), (BW, 120)], fill=LINE, width=2)
        for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]): g.ellipse((34 + i * 40, 46, 60 + i * 40, 72), fill=c)
        g.text((170, 60), 'Presupuestos  ›  Reformas Duero', font=F(700, 32), fill=INK, anchor='lm')
        g.text((60, 160), 'Nombre', font=F(600, 26), fill=MUT, anchor='lm'); g.text((BW - 60, 160), 'Modificado', font=F(600, 26), fill=MUT, anchor='rm')
        g.line([(40, 190), (BW - 40, 190)], fill=LINE, width=2)
        for i, (ts, n, d) in enumerate(self.FILES):
            if t < ts: continue
            k = ease((t - ts) / .25); y = 205 + i * 100 + int((1 - k) * 20); l, lg = layer(); A = int(255 * k)
            if t >= 4.2 and i == 5: lg.rounded_rectangle((30, y - 6, BW - 30, y + 84), 14, fill=(214, 230, 255, A))
            lg.rounded_rectangle((56, y + 10, 104, y + 70), 6, fill=(229, 57, 53, A)); lg.text((80, y + 40), 'PDF', font=F(800, 16), fill=(255, 255, 255, A), anchor='mm')
            lg.text((126, y + 40), n, font=F(600, 32), fill=INK + (A,), anchor='lm')
            lg.text((BW - 60, y + 40), d, font=F(500, 28), fill=MUT + (A,), anchor='rm')
            im.paste(l, (0, 0), l)
        if t >= 3.9:
            k = ease((t - 3.9) / .6); l, lg = layer(); cursor(lg, int(700 - 150 * k), int(990 - 250 * k)); im.paste(l, (0, 0), l)
        card(im, t, 5.0, 'Versión definitiva', '¿Cuál?', 'la “NO TOCAR” la tocaste ayer', cy=600)
        return im


# ------------------------------------------------------------------ m04. "TE LLAMO EN 5 MINUTOS" (pantalla bloqueada)
class CincoMinutos:
    POV = 'POV: el lead te dice “te llamo yo en cinco minutos”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    STEPS = [(0.0, '10:05', 'martes, 29 de septiembre'), (1.7, '10:10', 'martes, 29 de septiembre'),
             (2.4, '13:40', 'martes, 29 de septiembre'), (3.0, '19:55', 'martes, 29 de septiembre'),
             (3.6, '09:00', 'miércoles, 30 de septiembre'), (4.1, '09:00', 'jueves, 1 de octubre'),
             (4.6, '09:00', 'viernes, 2 de octubre')]
    SFX = ['ding@0.3'] + [f'tick@{a}' for a, _, _ in STEPS[1:]] + ['pop@5.1', 'boom@5.8']

    def draw(self, t):
        hh, dd = [(h, d) for a, h, d in self.STEPS if t >= a][-1]
        im, g = lock_bg(hh, dd)
        banner(im, t, 0.3, 'WhatsApp · Lead (reforma de baño)', '“Te llamo yo en cinco minutos, ¿vale?”', y=300, sub='martes 10:05')
        if t >= 1.7:
            g.text((BW // 2, 540), 'Llamadas perdidas: 0', font=F(700, 40), fill=(255, 190, 150), anchor='mm')
            g.text((BW // 2, 600), 'Mensajes nuevos: 0', font=F(700, 40), fill=(255, 190, 150), anchor='mm')
        card(im, t, 5.1, '“Cinco minutos”', '3 días', 'y el móvil sin sonar', cy=620, big_size=100)
        return im


NEW = {'m01-precio-amigo': PrecioAmigo, 'm02-publico-espana': PublicoEspana,
       'm03-carpeta-final': CarpetaFinal, 'm04-cinco-minutos': CincoMinutos}
