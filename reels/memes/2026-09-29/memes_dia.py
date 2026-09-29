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



# ------------------------------------------------------------------ m05. CADUCA LA TARJETA (notificaciones)
class TarjetaCaducada:
    POV = 'POV: tus anuncios por fin traen clientes y justo ese día te caduca la tarjeta'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    LEADS = [0.3, 0.8, 1.3, 1.8]
    SFX = [f'ding@{a}' for a in LEADS] + ['boom@2.7', 'tick@3.6', 'tick@4.2', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        hh = '11:42' if t < 3.6 else ('16:10' if t < 4.2 else '21:30')
        im, g = lock_bg(hh)
        names = ['Reformas: baño completo', 'Presupuesto cocina', 'Cambio de ventanas', 'Tejado con goteras']
        for i, ts in enumerate(self.LEADS):
            if t < ts: continue
            k = ease((t - ts) / .3); A = int(255 * k); l, lg = layer(); yy = 290 + i * 112
            lg.rounded_rectangle((36, yy, BW - 36, yy + 98), 24, fill=(58, 62, 74, int(230 * k)))
            lg.rounded_rectangle((60, yy + 22, 114, yy + 76), 14, fill=(255, 106, 26, A))
            lg.text((87, yy + 49), 'L', font=F(800, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((136, yy + 16), 'Nuevo lead · Formulario de anuncios', font=F(500, 22), fill=(190, 192, 200, A))
            lg.text((136, yy + 48), names[i], font=F(700, 29), fill=(255, 255, 255, A))
            im.paste(l, (0, 0), l)
        if t >= 2.7:
            k = ease((t - 2.7) / .3); A = int(255 * k); l, lg = layer(); yy = 750
            lg.rounded_rectangle((36, yy, BW - 36, yy + 150), 24, fill=(120, 24, 24, int(240 * k)))
            lg.text((70, yy + 22), 'Plataforma de anuncios · ahora', font=F(500, 24), fill=(255, 200, 200, A))
            lg.text((70, yy + 58), 'Pago rechazado: tarjeta caducada.', font=F(800, 32), fill=(255, 255, 255, A))
            lg.text((70, yy + 102), 'Tus anuncios se han pausado.', font=F(600, 28), fill=(255, 220, 220, A))
            im.paste(l, (0, 0), l)
        card(im, t, 5.0, 'Caducidad de la tarjeta', '09/26', 'justo el mejor día del mes', cy=600, big_size=96)
        return im


# ------------------------------------------------------------------ m06. "YA TE HE HECHO LA TRANSFERENCIA" (app del banco)
class Transferencia:
    POV = 'POV: el cliente te dice “ya te he hecho la transferencia” un viernes a las 20:00'
    DUR, PUNCH, FOCUS = 7.8, 6.0, (480, 560)
    REFR = [0.8, 1.7, 2.6]
    SFX = ['pop@0.3'] + [f'tick@{a}' for a in REFR] + ['tick@3.4', 'ding@4.0', 'pop@5.2', 'boom@6.0']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (244, 246, 248)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 300), fill=(0, 72, 120))
        g.text((40, 50), 'Cuenta negocio', font=F(600, 30), fill=(200, 225, 245), anchor='lm')
        bal = '2.140,35 €' if t < 4.0 else '2.190,35 €'
        g.text((40, 130), bal, font=F(800, 76), fill='white', anchor='lm')
        day = 'Viernes 20:03' if t < 3.4 else 'Lunes 09:12'
        g.text((40, 225), day, font=F(600, 30), fill=(200, 225, 245), anchor='lm')
        spin = any(a <= t < a + .5 for a in self.REFR)
        if spin:
            ang = (t * 720) % 360; g.arc((BW - 120, 200, BW - 60, 260), ang, ang + 270, fill='white', width=6)
        g.text((40, 350), 'Movimientos', font=F(700, 34), fill=INK, anchor='lm')
        movs = [('Luz local', '-86,40 €', 'jueves'), ('Cuota autónomos', '-310,00 €', 'lunes'), ('Gestoría', '-60,50 €', 'lunes')]
        y = 410
        if t >= 4.0:
            k = ease((t - 4.0) / .35); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((30, y, BW - 30, y + 150), 18, fill=(230, 247, 236, A))
            lg.text((60, y + 38), 'Transferencia · Cliente (web)', font=F(700, 30), fill=INK + (A,), anchor='lm')
            lg.text((BW - 60, y + 38), '+50,00 €', font=F(800, 34), fill=(20, 140, 70, A), anchor='rm')
            lg.text((60, y + 92), 'Concepto: “a cuenta, el resto ya si eso”', font=F(600, 27), fill=MUT + (A,), anchor='lm')
            im.paste(l, (0, 0), l); y += 170
        elif t >= 0.8:
            g.text((BW // 2, y + 40), 'Sin movimientos nuevos', font=F(600, 28), fill=MUT, anchor='mm'); y += 90
        for n, v, d in movs:
            g.line([(30, y), (BW - 30, y)], fill=LINE, width=2)
            g.text((60, y + 45), n, font=F(600, 30), fill=INK, anchor='lm'); g.text((60, y + 85), d, font=F(500, 24), fill=MUT, anchor='lm')
            g.text((BW - 60, y + 55), v, font=F(700, 30), fill=INK, anchor='rm'); y += 120
        card(im, t, 5.2, 'Factura de 1.200 €', '50 €', 'y el concepto no ayuda', cy=560, big_size=100)
        tag(g)
        return im


# ------------------------------------------------------------------ m07. 1 ESTRELLA POR NO COGER EL DOMINGO (reseñas)
class ResenaDomingo:
    POV = 'POV: te dejan una reseña de una estrella por no coger el teléfono'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    TXT = 'Llamé tres veces y nadie contestó. Fatal servicio. Llamé el domingo a las 23:40.'
    SFX = ['pop@0.4', 'tick@0.9', 'typing:2.0@1.2', 'ding@3.6', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 250), fill=(248, 249, 250)); g.line([(0, 250), (BW, 250)], fill=LINE, width=2)
        g.text((40, 60), 'Fontanería Arlanza', font=F(800, 50), fill=INK, anchor='lm')
        g.text((40, 124), '4,8', font=F(700, 34), fill=INK, anchor='lm'); stars(g, 110, 108, 5)
        g.text((330, 124), '· Fontanero · Horario: L-V 8:00–19:00', font=F(500, 26), fill=MUT, anchor='lm')
        g.text((40, 196), 'Reseñas más recientes', font=F(700, 32), fill=INK, anchor='lm')
        if t >= 0.4:
            y = 300; g.ellipse((40, y, 110, y + 70), fill=(234, 67, 53)); g.text((75, y + 35), 'M', font=F(700, 32), fill='white', anchor='mm')
            g.text((130, y + 4), 'Manolo P.', font=F(700, 30), fill=INK); g.text((130, y + 44), 'hace un momento', font=F(500, 24), fill=MUT)
            stars(g, 40, y + 92, 1 if t >= 0.9 else 0, size=36)
            n = int(len(self.TXT) * min(1, max(0, (t - 1.2) / 2.0))); ft = F(600, 34)
            for j, s_ in enumerate(wrap(self.TXT[:n], ft, BW - 90)):
                g.text((40, y + 150 + j * 46), s_, font=ft, fill=INK)
            if t >= 3.6:
                k = ease((t - 3.6) / .3); l, lg = layer()
                lg.rounded_rectangle((30, y + 300, BW - 30, y + 380), 16, fill=(255, 235, 150, int(200 * k)))
                lg.text((BW // 2, y + 340), 'Horario: de lunes a viernes, 8:00–19:00', font=F(700, 30), fill=INK + (int(255 * k),), anchor='mm')
                im.paste(l, (0, 0), l)
        card(im, t, 5.0, 'Motivo de la estrella', '23:40', 'de un domingo', cy=600, big_size=100)
        tag(g)
        return im


# ------------------------------------------------------------------ m08. PREVISIÓN VS REALIDAD (Excel)
class Prevision:
    POV = 'POV: comparas la previsión de ventas que hiciste en enero con lo que ha pasado'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    ROWS = [('Enero', '10.000 €', '1.200 €'), ('Febrero', '15.000 €', '900 €'), ('Marzo', '20.000 €', '1.450 €'),
            ('Abril', '30.000 €', '1.100 €'), ('Mayo', '40.000 €', '1.600 €'), ('Junio', '50.000 €', '1.300 €')]
    SFX = [f'tick@{0.3 + i * .25:.2f}' for i in range(6)] + [f'pop@{2.2 + i * .3:.1f}' for i in range(6)] + ['pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill=(16, 124, 65)); g.text((40, 55), 'Previsión_ventas_2026.xlsx', font=F(700, 34), fill='white', anchor='lm')
        cols = [(0, 70), (70, 330), (330, 640), (640, BW)]; hdr = ['', 'A · Mes', 'B · Previsto', 'C · Real']
        y0, rh = 150, 96
        g.rectangle((0, y0, BW, y0 + 70), fill=(238, 240, 242))
        for (x0, x1), h in zip(cols, hdr): g.text(((x0 + x1) // 2, y0 + 35), h, font=F(700, 28), fill=MUT, anchor='mm')
        for i, (m, p, r) in enumerate(self.ROWS):
            y = y0 + 70 + i * rh
            g.text((35, y + rh // 2), str(i + 2), font=F(600, 24), fill=MUT, anchor='mm')
            if t >= 0.3 + i * .25:
                g.text((200, y + rh // 2), m, font=F(600, 32), fill=INK, anchor='mm')
                g.text((485, y + rh // 2), p, font=F(700, 34), fill=(16, 124, 65), anchor='mm')
            if t >= 2.2 + i * .3:
                g.rectangle((641, y + 1, BW, y + rh - 1), fill=(253, 226, 226))
                g.text((800, y + rh // 2), r, font=F(700, 34), fill=(200, 40, 40), anchor='mm')
        for i in range(8): g.line([(0, y0 + 70 + i * rh), (BW, y0 + 70 + i * rh)], fill=LINE, width=2)
        for x0, _ in cols[1:]: g.line([(x0, y0), (x0, y0 + 70 + 7 * rh)], fill=LINE, width=2)
        if t >= 4.1:
            y = y0 + 70 + 6 * rh; g.rectangle((0, y + 1, BW, y + rh), fill=(245, 245, 245))
            g.text((200, y + rh // 2), 'TOTAL', font=F(800, 32), fill=INK, anchor='mm')
            g.text((485, y + rh // 2), '165.000 €', font=F(800, 34), fill=INK, anchor='mm')
            g.text((800, y + rh // 2), '7.550 €', font=F(800, 34), fill=(200, 40, 40), anchor='mm')
        card(im, t, 5.0, 'Previsión cumplida', '4,6 %', 'pero qué bonito quedó el Excel', cy=560, big_size=100)
        tag(g)
        return im


# ------------------------------------------------------------------ m09. "HAZLO MÁS MODERNO" (editor de diseño)
class Moderno:
    POV = 'POV: el cliente quiere un anuncio “más moderno” y te manda su referencia'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    SFX = ['pop@0.3', 'ding@1.6', 'boom@2.7', 'pop@3.2', 'pop@3.6', 'pop@4.0', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (44, 46, 52)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 90), fill=(30, 31, 36)); g.text((30, 45), 'Editor de diseño · Anuncio_reformas.png', font=F(600, 28), fill=(220, 220, 225), anchor='lm')
        g.rectangle((0, 90, 110, BH), fill=(34, 35, 40))
        for i, lab in enumerate(['T', '▢', '◯', '★', '⌘']):
            g.rounded_rectangle((20, 120 + i * 100, 90, 190 + i * 100), 14, fill=(52, 54, 60))
            g.text((55, 155 + i * 100), lab if lab in 'T' else '·', font=F(700, 34), fill=(200, 200, 205), anchor='mm')
        X0, Y0, X1, Y1 = 170, 150, 900, 900
        if t < 2.7:
            g.rectangle((X0, Y0, X1, Y1), fill=(245, 241, 234))
            g.rectangle((X0, Y0, X1, Y0 + 380), fill=(210, 200, 185))
            g.text((X0 + 50, Y0 + 450), 'Tu baño nuevo,', font=F(800, 56), fill=(40, 40, 40))
            g.text((X0 + 50, Y0 + 520), 'sin sustos.', font=F(800, 56), fill=(40, 40, 40))
            g.rounded_rectangle((X0 + 50, Y0 + 630, X0 + 380, Y0 + 700), 35, fill=(40, 40, 40))
            g.text((X0 + 215, Y0 + 665), 'Pide presupuesto', font=F(700, 28), fill='white', anchor='mm')
            banner(im, t, 1.6, 'WhatsApp · Cliente (reformas)', '“Muy bonito, pero más moderno. Como este:”', t1=2.7, y=100)
        else:
            for yy in range(Y0, Y1):
                h = (yy - Y0) / (Y1 - Y0); c = (int(255 * (1 - h)), int(80 + 150 * abs(math.sin(h * 3))), int(255 * h))
                g.line([(X0, yy), (X1, yy)], fill=c)
            def outl(txt, xy, size, fill, rot=0, stroke=(0, 0, 0)):
                f = F(800, size); w = int(f.getlength(txt)) + 40
                s_ = Image.new('RGBA', (w, size + 40), (0, 0, 0, 0)); sg = ImageDraw.Draw(s_)
                sg.text((20, 20), txt, font=f, fill=fill, stroke_width=5, stroke_fill=stroke)
                s_ = s_.rotate(rot, expand=True, resample=Image.BICUBIC); im.paste(s_, xy, s_)
            if t >= 2.7: outl('¡¡¡OFERTA!!!', (X0 + 30, Y0 + 30), 90, (255, 240, 0), 8, (220, 0, 0))
            if t >= 3.2: outl('REFORMAS', (X0 + 60, Y0 + 260), 110, (0, 255, 120), -4, (120, 0, 160))
            if t >= 3.6: outl('¡¡LLAMA YA!!', (X0 + 120, Y0 + 470), 80, (255, 90, 200), 6, (0, 0, 180))
            if t >= 4.0:
                stars(g, X0 + 80, Y0 + 650, 5, size=70, on=(255, 215, 0))
                outl('Presupuesto GRATIS', (X0 + 60, Y0 + 740), 50, (255, 255, 255), -2, (255, 0, 0))
        card(im, t, 5.0, 'Idea de “moderno”', 'Año 2009', 'seis colores y tres sombras por palabra', cy=560, big_size=90)
        return im


# ------------------------------------------------------------------ m10. EL FORMULARIO "MÁS FÁCIL" (tabla de leads)
class FormularioBasura:
    POV = 'POV: quitas preguntas del formulario para que sea “más fácil” y miras los leads'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    ROWS = [('asdf', '123456789', 'a@a.com'), ('Prueba', '666', 'hola'), ('Juan', '600000000', 'nose@nose'),
            ('xd', '0', 'xd@xd.xd'), ('Pepe', '—', 'pepe'), ('ñññ', '111', 'ñ@ñ.ñ')]
    SFX = [f'ding@{0.3 + i * .4:.1f}' for i in range(6)] + ['boom@3.2', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (247, 248, 250)); g = ImageDraw.Draw(im)
        appbar(g, 'CRM · Leads nuevos', 'Formulario: “Pide info en 5 segundos”', col=(52, 44, 110))
        cols = [40, 250, 520]; y0 = 170
        for x, h in zip(cols, ['Nombre', 'Teléfono', 'Email']): g.text((x, y0), h, font=F(700, 28), fill=MUT, anchor='lm')
        g.line([(30, y0 + 30), (BW - 30, y0 + 30)], fill=LINE, width=2)
        for i, row in enumerate(self.ROWS):
            ts = 0.3 + i * .4
            if t < ts: continue
            k = ease((t - ts) / .25); y = y0 + 50 + i * 110 + int((1 - k) * 20); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((30, y, BW - 30, y + 96), 14, fill=(255, 255, 255, A), outline=LINE + (A,), width=2)
            for x, v in zip(cols, row): lg.text((x, y + 48), v, font=F(600, 32), fill=INK + (A,), anchor='lm')
            if t >= 3.2:
                lg.rounded_rectangle((BW - 190, y + 26, BW - 50, y + 70), 22, fill=(253, 226, 226, A))
                lg.text((BW - 120, y + 48), 'no válido', font=F(700, 22), fill=(200, 40, 40, A), anchor='mm')
            im.paste(l, (0, 0), l)
        card(im, t, 5.0, 'Leads que se pueden llamar', '0 de 6', 'pero qué barato sale cada lead', cy=560, big_size=96)
        tag(g)
        return im


# ------------------------------------------------------------------ m11. "UNA PREGUNTITA RÁPIDA" (WhatsApp)
class Preguntita(WAChat):
    POV = 'POV: un cliente te escribe “una preguntita rápida” el domingo por la mañana'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    NAME, LETTER, HOUR = 'Cliente (gimnasio)', 'G', '9:1'
    MSGS = [(0.3, 'in', '¡Hola! Una preguntita rápida'), (1.1, 'in', 'Bueno, son dos'),
            (1.8, 'in', 'Lo del logo y lo de la web'), (2.6, 'in', 'Y si podemos cambiar toda la campaña'),
            (3.6, 'in', 'Para hoy, a ser posible')]
    TYPING = [(3.0, 3.5)]
    SFX = ['pop@0.3', 'pop@1.1', 'pop@1.8', 'pop@2.6', 'typing:0.5@3.0', 'pop@3.6', 'pop@5.0', 'boom@5.8']

    def status(self, t):
        if any(a <= t < b for a, b in self.TYPING): return 'escribiendo...', (0, 168, 132)
        return 'domingo · en línea', WA_GREY

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g)
        card(im, t, 5.0, 'Domingo, 9:14', '“Rápida”', 'rehacer la campaña entera para hoy', cy=560, big_size=90)
        return im


# ------------------------------------------------------------------ m12. LOS LEADS EN SPAM (correo)
class SpamLeads:
    POV = 'POV: descubres que los leads de la web llevaban un mes llegando a la carpeta de spam'
    DUR, PUNCH, FOCUS = 7.8, 6.0, (480, 560)
    SFX = ['pop@0.3', 'tick@1.6', 'pop@2.0', 'count:1.4@2.2', 'pop@5.2', 'boom@6.0']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill=(242, 245, 250)); g.text((40, 55), 'Correo · contacto@', font=F(700, 34), fill=INK, anchor='lm')
        inspam = t >= 1.9
        g.rectangle((0, 110, 300, BH), fill=(246, 248, 252))
        for i, (lab, n) in enumerate([('Recibidos', '3'), ('Enviados', ''), ('Spam', str(int(214 * min(1, max(0, (t - 2.2) / 1.4)))) if inspam else '214')]):
            y = 150 + i * 90; sel = (i == 2) == inspam
            if sel: g.rounded_rectangle((12, y - 30, 290, y + 30), 30, fill=(211, 227, 253))
            g.text((40, y), lab, font=F(700 if sel else 500, 30), fill=INK, anchor='lm')
            if n: g.text((270, y), n, font=F(800, 28), fill=(200, 40, 40) if i == 2 else INK, anchor='rm')
        if t >= 1.0 and t < 1.9:
            k = ease((t - 1.0) / .6); l, lg = layer(); cursor(lg, int(600 - 400 * k), int(800 - 480 * k)); im.paste(l, (0, 0), l)
        if not inspam:
            for i, (who, sub) in enumerate([('Proveedor', 'Factura septiembre'), ('Gestoría', 'Recordatorio IVA'), ('Banco', 'Nuevas condiciones')]):
                y = 140 + i * 120; g.text((330, y + 20), who, font=F(700, 28), fill=INK); g.text((330, y + 60), sub, font=F(500, 26), fill=MUT)
                g.line([(320, y + 110), (BW, y + 110)], fill=LINE, width=2)
        else:
            dates = ['hoy', 'ayer', '27 sep', '26 sep', '24 sep', '21 sep', '15 sep']
            for i, d in enumerate(dates):
                ts = 2.0 + i * .18
                if t < ts: continue
                y = 130 + i * 118
                g.rectangle((300, y, BW, y + 110), fill=(255, 250, 240))
                g.text((330, y + 18), 'Formulario web', font=F(700, 28), fill=INK); g.text((BW - 30, y + 20), d, font=F(600, 24), fill=MUT, anchor='ra')
                g.text((330, y + 60), 'Nuevo lead: “quiero presupuesto”', font=F(600, 26), fill=(200, 40, 40))
                g.line([(300, y + 110), (BW, y + 110)], fill=LINE, width=2)
        card(im, t, 5.2, 'Leads en spam', '214', 'y tú culpando a los anuncios', cy=560, big_size=110)
        tag(g)
        return im

# ------------------------------------------------------------------ m13. LA REUNIÓN QUE SE MUEVE (calendario)
class ReunionMovida:
    POV = 'POV: el cliente mueve la reunión para revisar resultados por quinta vez'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    MOVES = [(0.3, 0, 10.0), (1.0, 1, 12.0), (1.7, 2, 9.0), (2.4, 3, 16.0), (3.1, 4, 8.5)]
    SFX = ['pop@0.3'] + [f'tick@{a}' for a, _, _ in MOVES[1:]] + ['ding@3.9', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.text((40, 50), 'Septiembre 2026', font=F(800, 40), fill=INK, anchor='lm')
        days = ['Lun 21', 'Mar 22', 'Mié 23', 'Jue 24', 'Vie 25']; X0, CW, Y0, HH = 100, 170, 110, 90
        for i, d in enumerate(days): g.text((X0 + i * CW + CW // 2, Y0 + 20), d, font=F(700, 26), fill=MUT, anchor='mm')
        for h in range(8, 18):
            y = Y0 + 60 + (h - 8) * HH; g.text((80, y), f'{h}:00', font=F(500, 22), fill=MUT, anchor='rm')
            g.line([(X0, y), (BW - 30, y)], fill=LINE, width=1)
        for i in range(6): g.line([(X0 + i * CW, Y0 + 50), (X0 + i * CW, BH - 20)], fill=LINE, width=1)
        n = sum(1 for a, _, _ in self.MOVES if t >= a)
        for j, (a, dcol, h) in enumerate(self.MOVES[:n]):
            y = Y0 + 60 + (h - 8) * HH; x = X0 + dcol * CW
            last = j == n - 1
            if last:
                k = ease((t - a) / .25); l, lg = layer()
                lg.rounded_rectangle((x + 6, y + 4, x + CW - 6, y + HH - 4), 12, fill=(26, 115, 232, int(255 * k)))
                lg.text((x + 16, y + 14), 'Revisión', font=F(700, 22), fill=(255, 255, 255, int(255 * k)))
                lg.text((x + 16, y + 44), 'resultados', font=F(600, 20), fill=(220, 235, 255, int(255 * k)))
                im.paste(l, (0, 0), l)
            else:
                g.rounded_rectangle((x + 6, y + 4, x + CW - 6, y + HH - 4), 12, outline=(180, 190, 205), width=3)
                g.line([(x + 14, y + HH // 2), (x + CW - 14, y + HH // 2)], fill=(180, 190, 205), width=3)
        if n > 1:
            g.rounded_rectangle((BW - 330, 26, BW - 30, 76), 25, fill=(253, 226, 226))
            g.text((BW - 180, 51), f'Reprogramada ({n - 1})', font=F(700, 26), fill=(200, 40, 40), anchor='mm')
        banner(im, t, 3.9, 'Calendario · Cliente (clínica)', 'Propone nueva fecha: “mejor la semana que viene”', y=820, icol=(26, 115, 232), ich='C')
        card(im, t, 5.0, 'Reunión de resultados', '5 cambios', 'y luego: “¿por qué no hay resultados?”', cy=560, big_size=86)
        return im


# ------------------------------------------------------------------ m14. "ME LO PIENSO" DESDE MARZO (ficha del CRM)
class Pensandolo:
    POV = 'POV: abres la ficha del cliente que “se lo está pensando”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    SFX = ['pop@0.3', 'pop@0.8', 'pop@1.3', 'pop@1.8', 'count:1.8@2.4', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (247, 248, 250)); g = ImageDraw.Draw(im)
        appbar(g, 'CRM · Ficha de oportunidad', col=(52, 44, 110))
        g.rounded_rectangle((30, 160, BW - 30, 960), 22, fill='white', outline=LINE, width=2)
        g.ellipse((60, 190, 160, 290), fill=(120, 110, 200)); g.text((110, 240), 'CS', font=F(800, 36), fill='white', anchor='mm')
        g.text((190, 215), 'Clínica Sanz', font=F(800, 42), fill=INK, anchor='lm'); g.text((190, 265), 'Oportunidad: anuncios + web', font=F(500, 28), fill=MUT, anchor='lm')
        rows = [(0.3, 'Etapa', 'Negociación'), (0.8, 'Último contacto', '14 de marzo'),
                (1.3, 'Nota', '“Me lo pienso y te digo”'), (1.8, 'Próxima tarea', '—')]
        for i, (ts, k_, v) in enumerate(rows):
            if t < ts: continue
            y = 340 + i * 100
            g.text((60, y), k_, font=F(600, 28), fill=MUT, anchor='lm'); g.text((380, y), v, font=F(700, 32), fill=INK, anchor='lm')
            g.line([(60, y + 45), (BW - 60, y + 45)], fill=LINE, width=1)
        if t >= 2.4:
            n = int(199 * ease(min(1, (t - 2.4) / 1.8)))
            g.rounded_rectangle((60, 760, BW - 60, 920), 18, fill=(255, 243, 224))
            g.text((90, 800), 'Días en “Negociación”', font=F(600, 28), fill=(160, 90, 0), anchor='lm')
            g.text((90, 870), str(n), font=F(800, 64), fill=(200, 100, 0), anchor='lm')
        card(im, t, 5.0, 'Días pensándolo', '199', 'y sigue en “Negociación”', cy=560, big_size=110)
        tag(g)
        return im


# ------------------------------------------------------------------ m15. TU WEB EN EL MÓVIL (ventanas emergentes)
class WebMovil:
    POV = 'POV: abres tu web desde el móvil por primera vez y buscas el botón de llamar'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    SFX = ['pop@0.3', 'pop@0.9', 'pop@1.5', 'pop@2.1', 'pop@2.7', 'pop@3.3', 'tick@4.1', 'tick@4.5', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 80), fill=(240, 240, 242)); g.rounded_rectangle((120, 18, BW - 120, 62), 22, fill='white')
        g.text((BW // 2, 40), 'reformasduero.es', font=F(500, 24), fill=MUT, anchor='mm')
        g.rectangle((0, 80, BW, 180), fill=(30, 50, 80)); g.text((40, 130), 'REFORMAS DUERO', font=F(800, 36), fill='white', anchor='lm')
        g.rectangle((0, 180, BW, 520), fill=(200, 190, 175)); g.text((40, 380), 'Reformas integrales', font=F(800, 54), fill='white', anchor='lm')
        g.rounded_rectangle((40, 560, 460, 650), 45, fill=(230, 90, 30)); g.text((250, 605), 'Llamar ahora', font=F(800, 34), fill='white', anchor='mm')
        def pop_(ts, box, fillc, lines, col=INK):
            if t < ts: return
            k = pop((t - ts) / .3)
            if k < .15: return
            x0, y0, x1, y1 = box; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            w, h = (x1 - x0) * k, (y1 - y0) * k; l, lg = layer()
            lg.rounded_rectangle((cx - w / 2 + 6, cy - h / 2 + 8, cx + w / 2 + 6, cy + h / 2 + 8), 20, fill=(0, 0, 0, 60))
            lg.rounded_rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), 20, fill=fillc)
            if k > .9:
                for j, (txt, sz) in enumerate(lines):
                    lg.text((x0 + 30, y0 + 30 + sum(l_[1] + 16 for l_ in lines[:j])), txt, font=F(700, sz), fill=col)
                lg.text((x1 - 30, y0 + 20), '×', font=F(700, 30), fill=(150, 150, 150), anchor='ra')
            im.paste(l, (0, 0), l)
        pop_(0.3, (0, 800, BW, 1000), (255, 255, 255), [('Usamos cookies para todo.', 30), ('Aceptar · Configurar · Leer 14 páginas', 26)])
        pop_(0.9, (520, 600, 930, 780), (37, 211, 102), [('¿Hablamos?', 34)], col=(255, 255, 255))
        pop_(1.5, (80, 420, 880, 720), (255, 250, 230), [('¡Suscríbete a la newsletter!', 36), ('y llévate un 5 % en nada', 28)])
        pop_(2.1, (40, 230, 700, 470), (230, 240, 255), [('Descarga el catálogo', 36), ('(PDF de 48 MB)', 28)])
        pop_(2.7, (260, 520, 920, 700), (255, 230, 240), [('¿Te vas ya?', 36), ('¡Espera, gira la ruleta!', 28)])
        pop_(3.3, (60, 540, 520, 660), (40, 40, 44), [('Valora tu experiencia', 30)], col=(255, 255, 255))
        if t >= 3.8:
            k = ease((t - 3.8) / .8); l, lg = layer(); cursor(lg, int(700 - 450 * k + 30 * math.sin(t * 9)), int(950 - 350 * k)); im.paste(l, (0, 0), l)
        card(im, t, 5.0, 'Botón de llamar', 'Perdido', 'debajo de seis ventanas emergentes', cy=560, big_size=96)
        return im


# ------------------------------------------------------------------ m16. PRESUPUESTO ABIERTO 9 VECES (notificaciones)
class AbiertoNueve:
    POV = 'POV: el cliente ha abierto tu presupuesto nueve veces y sigue sin contestar'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    TS = [0.3 + i * .45 for i in range(9)]
    SFX = [f'ding@{a:.2f}' for a in TS] + ['pop@5.0', 'boom@5.8']
    HOURS = ['lun 10:02', 'lun 10:05', 'lun 16:40', 'mar 08:15', 'mar 13:30', 'mar 22:47', 'mié 07:58', 'mié 12:03', 'hoy 18:21']

    def draw(self, t):
        im, g = lock_bg('18:21')
        n = sum(1 for a in self.TS if t >= a)
        for j in range(max(0, n - 5), n):
            i = j - max(0, n - 5); ts = self.TS[j]; k = ease((t - ts) / .3); A = int(255 * k); l, lg = layer()
            yy = 290 + (min(n, 5) - 1 - i) * 112
            lg.rounded_rectangle((36, yy, BW - 36, yy + 98), 24, fill=(58, 62, 74, int(230 * k)))
            lg.rounded_rectangle((60, yy + 22, 114, yy + 76), 14, fill=(66, 133, 244, A))
            lg.text((87, yy + 49), '@', font=F(800, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((136, yy + 16), f'Seguimiento de correo · {self.HOURS[j]}', font=F(500, 22), fill=(190, 192, 200, A))
            lg.text((136, yy + 48), 'Cliente ha abierto “Presupuesto.pdf”', font=F(700, 28), fill=(255, 255, 255, A))
            im.paste(l, (0, 0), l)
        if n:
            g.text((BW // 2, 900), f'Aperturas: {n}   ·   Respuestas: 0', font=F(700, 36), fill=(255, 190, 150), anchor='mm')
        card(im, t, 5.0, 'Veces que lo ha abierto', '9', 'respuestas: cero', cy=600, big_size=120)
        return im

# ------------------------------------------------------------------ m17. EL PROYECTO "DE UNA TARDE" (hoja de horas)
class HojaHoras:
    POV = 'POV: apuntas las horas del proyecto “sencillito, de una tarde”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    ROWS = [('Reunión inicial', '0,5 h', '3 h'), ('Diseño del anuncio', '1 h', '9 h'), ('“Un último retoque”', '0,5 h', '12 h'),
            ('Llamadas “rápidas”', '0,5 h', '7 h'), ('Textos', '1,5 h', '6 h')]
    SFX = [f'tick@{0.3 + i * .3:.1f}' for i in range(5)] + [f'pop@{2.1 + i * .35:.2f}' for i in range(5)] + ['boom@4.1', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill=(16, 124, 65)); g.text((40, 55), 'Horas_proyecto_anuncio.xlsx', font=F(700, 34), fill='white', anchor='lm')
        cols = [(0, 70), (70, 520), (520, 740), (740, BW)]; hdr = ['', 'A · Tarea', 'B · Estimado', 'C · Real']
        y0, rh = 150, 104
        g.rectangle((0, y0, BW, y0 + 70), fill=(238, 240, 242))
        for (x0, x1), h in zip(cols, hdr): g.text(((x0 + x1) // 2, y0 + 35), h, font=F(700, 26), fill=MUT, anchor='mm')
        for i, (m, e, r) in enumerate(self.ROWS):
            y = y0 + 70 + i * rh
            g.text((35, y + rh // 2), str(i + 2), font=F(600, 24), fill=MUT, anchor='mm')
            if t >= 0.3 + i * .3:
                g.text((95, y + rh // 2), m, font=F(600, 30), fill=INK, anchor='lm')
                g.text((630, y + rh // 2), e, font=F(700, 32), fill=(16, 124, 65), anchor='mm')
            if t >= 2.1 + i * .35:
                g.rectangle((741, y + 1, BW, y + rh - 1), fill=(253, 226, 226))
                g.text((850, y + rh // 2), r, font=F(800, 32), fill=(200, 40, 40), anchor='mm')
        for i in range(7): g.line([(0, y0 + 70 + i * rh), (BW, y0 + 70 + i * rh)], fill=LINE, width=2)
        for x0, _ in cols[1:]: g.line([(x0, y0), (x0, y0 + 70 + 6 * rh)], fill=LINE, width=2)
        if t >= 4.1:
            y = y0 + 70 + 5 * rh; g.rectangle((0, y + 1, BW, y + rh), fill=(245, 245, 245))
            g.text((95, y + rh // 2), 'TOTAL', font=F(800, 32), fill=INK, anchor='lm')
            g.text((630, y + rh // 2), '4 h', font=F(800, 32), fill=INK, anchor='mm')
            g.text((850, y + rh // 2), '37 h', font=F(800, 34), fill=(200, 40, 40), anchor='mm')
        card(im, t, 5.0, 'Proyecto “de una tarde”', '37 horas', 'cobrado como si fueran cuatro', cy=560, big_size=96)
        tag(g)
        return im


# ------------------------------------------------------------------ m18. "VENGO DE PARTE DE…" (WhatsApp)
class AmigoGratis(WAChat):
    POV = 'POV: un cliente te recomienda a un amigo y el amigo viene con sus propias condiciones'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    NAME, LETTER, HOUR = 'Javi (recomendado)', 'J', '17:3'
    MSGS = [(0.3, 'in', 'Hola, vengo de parte de Marta, tu clienta'), (1.2, 'in', 'Quiero lo mismo que tiene ella'),
            (2.2, 'out', '¡Genial! Te preparo el presupuesto hoy'),
            (3.6, 'in', 'Ah, ¿pero no era gratis por venir de su parte?')]
    TYPING = [(2.8, 3.5)]
    SFX = ['pop@0.3', 'pop@1.2', 'pop@2.2', 'typing:0.7@2.8', 'pop@3.6', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g)
        card(im, t, 5.0, 'Descuento por recomendación', '100 %', 'según él, claro', cy=600, big_size=110)
        return im


# ------------------------------------------------------------------ m19. EL LEAD QUE BUSCA TRABAJO (llamada)
class LeadCurriculum:
    POV = 'POV: por fin te llama un lead del anuncio y es para pedirte trabajo'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    LINES = [(0.8, 'in', 'Hola, os llamo por el anuncio.'), (1.9, 'out', '¡Genial! ¿Qué reforma necesitas?'),
             (3.1, 'in', 'No, no… ¿buscáis gente? Soy alicatador.'), (4.2, 'in', '¿Os mando el currículum?')]
    SFX = ['ding@0.2', 'ding@0.5'] + [f'pop@{a}' for a, _, _ in LINES] + ['pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (22, 26, 34)); g = ImageDraw.Draw(im)
        g.ellipse((BW // 2 - 80, 40, BW // 2 + 80, 200), fill=(90, 100, 120)); g.text((BW // 2, 120), 'L', font=F(800, 70), fill='white', anchor='mm')
        g.text((BW // 2, 250), 'Lead · Anuncio de reformas', font=F(700, 40), fill='white', anchor='mm')
        g.text((BW // 2, 305), timer(max(0, t - 0.6) * 3) if t >= 0.6 else 'llamando…', font=F(500, 32), fill=(170, 175, 185), anchor='mm')
        y = 370
        for ts, side, txt in self.LINES:
            if t < ts: continue
            k = ease((t - ts) / .3); l, lg = layer(); A = int(255 * k); f = F(600, 34)
            ls = wrap(txt, f, 620); w = max(f.getlength(x) for x in ls) + 60; h = len(ls) * 46 + 40
            x0 = 40 if side == 'in' else BW - 40 - w
            lg.rounded_rectangle((x0, y, x0 + w, y + h), 24, fill=((52, 58, 70) if side == 'in' else (0, 110, 90)) + (A,))
            for j, s_ in enumerate(ls): lg.text((x0 + 30, y + 20 + j * 46), s_, font=f, fill=(255, 255, 255, A))
            im.paste(l, (0, 0), l); y += h + 20
        for i, (lab, col) in enumerate([('Silenciar', (60, 66, 78)), ('Colgar', (235, 64, 52)), ('Altavoz', (60, 66, 78))]):
            x = 200 + i * 280; g.ellipse((x - 55, 850, x + 55, 960), fill=col)
            g.text((x, 905), lab[0], font=F(800, 36), fill='white', anchor='mm')
        card(im, t, 5.0, 'Lead del mes', 'Candidato', 'el anuncio funciona… para contratar', cy=560, big_size=90)
        return im


# ------------------------------------------------------------------ m20. EL PIN EN EL RÍO (mapa)
class PinRio:
    POV = 'POV: buscas tu negocio en el mapa y la chincheta está en mitad del río'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 640)
    SFX = ['typing:1.0@0.3', 'tick@1.4', 'boom@2.2', 'pop@3.2', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (236, 232, 224)); g = ImageDraw.Draw(im)
        for i in range(-2, 12):
            g.line([(i * 110, 0), (i * 110 + 300, BH)], fill='white', width=16)
            g.line([(0, i * 120), (BW, i * 120 - 180)], fill='white', width=12)
        for (x, y, w, h) in [(40, 700, 200, 150), (650, 150, 240, 180), (700, 760, 200, 180)]:
            g.rounded_rectangle((x, y, x + w, y + h), 20, fill=(200, 230, 190))
        pts = [(BW * (i / 40), 470 + 90 * math.sin(i / 40 * 5)) for i in range(41)]
        g.line(pts, fill=(160, 205, 245), width=130, joint='curve')
        g.text((190, 440), 'Río', font=F(600, 30), fill=(90, 140, 200), anchor='mm')
        g.rounded_rectangle((30, 30, BW - 30, 120), 45, fill='white', outline=LINE, width=2)
        q = 'Reformas Duero'; n = int(len(q) * min(1, max(0, (t - 0.3) / 1.0)))
        g.text((80, 75), q[:n] if t < 1.4 else q, font=F(600, 34), fill=INK, anchor='lm')
        if t >= 2.2:
            k = pop((t - 2.2) / .35); px, py = 520, int(470 + 90 * math.sin(520 / BW * 5)); yy = py - int((1 - min(1, k)) * 200)
            g.ellipse((px - 22, py - 8, px + 22, py + 8), fill=(120, 150, 180))
            g.pieslice((px - 45, yy - 130, px + 45, yy - 40), 180, 360, fill=(234, 67, 53))
            g.polygon([(px - 45, yy - 85), (px + 45, yy - 85), (px, yy)], fill=(234, 67, 53))
            g.ellipse((px - 16, yy - 101, px + 16, yy - 69), fill=(165, 30, 25))
        if t >= 3.2:
            k = ease((t - 3.2) / .35); l, lg = layer(); A = int(255 * k); yy = BH - int(260 * k)
            lg.rounded_rectangle((0, yy, BW, BH + 30), 30, fill=(255, 255, 255, A))
            lg.text((40, yy + 50), 'Reformas Duero', font=F(800, 40), fill=INK + (A,), anchor='lm')
            lg.text((40, yy + 110), 'Empresa de reformas · Abierto', font=F(500, 28), fill=MUT + (A,), anchor='lm')
            lg.text((40, yy + 170), 'Cómo llegar: 0 rutas disponibles', font=F(700, 30), fill=(200, 40, 40, A), anchor='lm')
            im.paste(l, (0, 0), l)
        card(im, t, 5.0, 'Tu negocio en el mapa', 'En el río', 'y te preguntas por qué no viene nadie', cy=745, ch=300, big_size=90)
        return im

NEW = {'m01-precio-amigo': PrecioAmigo, 'm02-publico-espana': PublicoEspana,
       'm03-carpeta-final': CarpetaFinal, 'm04-cinco-minutos': CincoMinutos,
       'm05-tarjeta-caducada': TarjetaCaducada, 'm06-transferencia': Transferencia,
       'm07-resena-domingo': ResenaDomingo, 'm08-prevision': Prevision,
       'm09-moderno': Moderno, 'm10-formulario-facil': FormularioBasura,
       'm11-preguntita': Preguntita, 'm12-spam-leads': SpamLeads,
       'm13-reunion-movida': ReunionMovida, 'm14-pensandolo': Pensandolo,
       'm15-web-movil': WebMovil, 'm16-abierto-nueve': AbiertoNueve,
       'm17-hoja-horas': HojaHoras, 'm18-amigo-gratis': AmigoGratis,
       'm19-lead-curriculum': LeadCurriculum, 'm20-pin-rio': PinRio}
