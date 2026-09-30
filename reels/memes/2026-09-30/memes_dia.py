"""Memes del día 2026-09-30: 20 reels POV nuevos (m01…m20). Motor: toolkit/reels/pov_reel.py."""
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


def lock_bg(hour='21:47', date='miércoles, 30 de septiembre'):
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


# ------------------------------------------------------------------ m01. OFERTA APROBADA EL LUNES (administrador de anuncios)
class OfertaLunes:
    POV = 'POV: tu anuncio de la oferta del fin de semana por fin se aprueba… el lunes'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    STEPS = [(0.0, 'Viernes 09:00', 'En revisión', (230, 160, 20)), (1.2, 'Viernes 18:30', 'En revisión', (230, 160, 20)),
             (2.0, 'Sábado 12:10', 'En revisión', (230, 160, 20)), (2.8, 'Domingo 21:45', 'En revisión', (230, 160, 20)),
             (3.7, 'Lunes 08:02', 'Activo', (49, 162, 76))]
    SFX = ['pop@0.3', 'tick@1.2', 'tick@2.0', 'tick@2.8', 'ding@3.7', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (240, 242, 245)); g = ImageDraw.Draw(im)
        day, st, col = [(d, s, c) for a, d, s, c in self.STEPS if t >= a][-1]
        appbar(g, 'Administrador de anuncios', 'Muebles del Arlanzón · Campañas')
        g.rounded_rectangle((30, 160, BW - 30, 560), 22, fill='white', outline=LINE, width=2)
        statusdot(g, 64, 210, st, col)
        if st == 'En revisión':
            ang = (t * 300) % 360; g.arc((BW - 110, 180, BW - 60, 230), ang, ang + 270, fill=col, width=6)
        g.text((64, 270), 'OFERTA FIN DE SEMANA -30 %', font=F(800, 40), fill=INK, anchor='lm')
        g.text((64, 330), 'Válida sábado y domingo', font=F(600, 30), fill=MUT, anchor='lm')
        g.line([(64, 390), (BW - 64, 390)], fill=LINE, width=2)
        g.text((64, 440), 'Estado actualizado', font=F(600, 28), fill=MUT, anchor='lm')
        k = pop((t - max(a for a, *_ in self.STEPS if t >= a)) / .3)
        g.text((64, 500), day, font=F(800, int(44 * min(1.15, max(.7, k)))), fill=INK, anchor='lm')
        g.rounded_rectangle((30, 600, BW - 30, 900), 22, fill='white', outline=LINE, width=2)
        g.text((64, 650), 'Calendario', font=F(700, 32), fill=INK, anchor='lm')
        for i, d in enumerate(['V', 'S', 'D', 'L']):
            x = 64 + i * 215; on = i in (1, 2)
            g.rounded_rectangle((x, 700, x + 190, 860), 18, fill=(255, 240, 230) if on else (244, 245, 247))
            g.text((x + 95, 750), d, font=F(800, 50), fill=(255, 106, 26) if on else MUT, anchor='mm')
            g.text((x + 95, 815), 'OFERTA' if on else ('hoy' if i == 3 and t >= 3.7 else ''), font=F(700, 24), fill=(255, 106, 26) if on else INK, anchor='mm')
        card(im, t, 5.0, 'La oferta del finde', 'Caducada', 'y el anuncio, activo y gastando', cy=600, big_size=76)
        tag(g)
        return im


# ------------------------------------------------------------------ m02. "QUE SE HAGA VIRAL" (WhatsApp)
class Viral(WAChat):
    POV = 'POV: el cliente quiere que su vídeo “se haga viral” para el viernes'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    NAME, LETTER, HOUR = 'Cliente (tienda de colchones)', 'T', '12:0'
    MSGS = [(0.3, 'in', 'Te paso el vídeo. Lo quiero viral para el viernes.'),
            (1.5, 'out', 'Vale. ¿Qué presupuesto le ponemos de anuncios?'),
            (3.0, 'in', 'Ninguno. Si es bueno se comparte solo, ¿no?')]
    TYPING = [(2.2, 2.9)]
    SFX = ['pop@0.3', 'pop@1.5', 'typing:0.7@2.2', 'pop@3.0', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im, g = self.base(t); y = self.bubbles(im, t)
        if t >= 3.9:
            k = ease((t - 3.9) / .3); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((36, y + 10, 560, y + 130), 22, fill=WA_IN + (A,))
            lg.rounded_rectangle((60, y + 30, 200, y + 110), 10, fill=(60, 70, 78, A))
            lg.polygon([(115, y + 50), (115, y + 90), (145, y + 70)], fill=(230, 230, 230, A))
            lg.text((220, y + 50), 'video_colchon_v1.mp4', font=F(600, 26), fill=WA_TXT + (A,))
            lg.text((220, y + 88), '0:48 · en horizontal', font=F(500, 24), fill=WA_GREY + (A,))
            im.paste(l, (0, 0), l)
        self.footer(g)
        card(im, t, 5.0, 'Presupuesto para hacerse viral', '0 €', 'y 48 segundos de colchón en horizontal', cy=600, big_size=110)
        return im


# ------------------------------------------------------------------ m03. NOMBRE DE OTRO CLIENTE (correo)
class OtroNombre:
    POV = 'POV: le das a enviar a la propuesta y ves que empieza con el nombre de otro cliente'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    BODY = 'Estimados Cocinas Pisuerga: como hablamos, os paso la propuesta…'
    SFX = ['pop@0.3', 'typing:1.4@0.6', 'tick@2.4', 'pop@3.0', 'boom@3.6', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill=(242, 246, 252)); g.text((40, 55), 'Mensaje nuevo', font=F(700, 34), fill=INK, anchor='lm')
        rows = [('Para', 'info@reformasduero.es'), ('Asunto', 'Propuesta Reformas Duero')]
        for i, (a, b) in enumerate(rows):
            y = 130 + i * 80; g.text((40, y + 30), a, font=F(600, 28), fill=MUT, anchor='lm'); g.text((170, y + 30), b, font=F(600, 30), fill=INK, anchor='lm')
            g.line([(40, y + 70), (BW - 40, y + 70)], fill=LINE, width=2)
        n = int(len(self.BODY) * min(1, max(0, (t - .6) / 1.4))); bf = F(500, 34)
        for j, s_ in enumerate(wrap(self.BODY[:n], bf, BW - 90)): g.text((40, 340 + j * 48), s_, font=bf, fill=INK)
        g.rounded_rectangle((40, 520, 420, 600), 14, fill=(240, 242, 245));         g.text((64, 560), 'Propuesta_Pisuerga.pdf', font=F(600, 26), fill=INK, anchor='lm')
        sent = t >= 2.4
        g.rounded_rectangle((40, 640, 280, 720), 40, fill=(160, 170, 185) if sent else (11, 87, 208))
        g.text((160, 680), 'Enviado' if sent else 'Enviar', font=F(700, 30), fill='white', anchor='mm')
        if 1.9 <= t < 2.6:
            l, lg = layer(); cursor(lg, 200, 690); im.paste(l, (0, 0), l)
        if t >= 3.0:
            k = ease((t - 3.0) / .3); l, lg = layer()
            lg.rounded_rectangle((34, 330, 700, 390), 10, outline=(230, 50, 50, int(255 * k)), width=6)
            im.paste(l, (0, 0), l)
        if t >= 3.6:
            g.rounded_rectangle((40, 780, BW - 40, 880), 18, fill=(50, 50, 54))
            g.text((70, 830), 'Mensaje enviado.', font=F(600, 30), fill='white', anchor='lm')
            g.text((BW - 70, 830), 'Deshacer (expirado)', font=F(700, 28), fill=(140, 180, 255), anchor='rm')
        card(im, t, 5.0, 'El cliente se llama', 'Duero', 'la propuesta dice Pisuerga', cy=600, big_size=100)
        return im


# ------------------------------------------------------------------ m04. ORIGEN: DESCONOCIDO (CRM)
class OrigenDesconocido:
    POV = 'POV: quieres saber de dónde vienen tus clientes y abres el CRM'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    ROWS = [(0.4, 'Cliente reforma cocina', '—'), (0.8, 'Cliente tejado', 'no sé'), (1.2, 'Cliente baño', 'otro'),
            (1.6, 'Cliente ventanas', '—'), (2.0, 'Cliente fachada', '“de por ahí”'), (2.4, 'Cliente garaje', 'el de antes')]
    SFX = [f'tick@{a}' for a, _, _ in ROWS] + ['pop@3.3', 'count:1.0@3.4', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (245, 247, 250)); g = ImageDraw.Draw(im)
        appbar(g, 'CRM · Clientes 2026', 'Filtro: todos', col=(52, 45, 90))
        g.text((60, 170), 'Nombre', font=F(700, 26), fill=MUT, anchor='lm'); g.text((620, 170), 'Origen', font=F(700, 26), fill=MUT, anchor='lm')
        for i, (ts, n, o) in enumerate(self.ROWS):
            if t < ts: continue
            y = 200 + i * 80; k = ease((t - ts) / .25); l, lg = layer(); A = int(255 * k)
            lg.rectangle((30, y, BW - 30, y + 72), fill=(255, 255, 255, A))
            lg.text((60, y + 36), n, font=F(600, 30), fill=INK + (A,), anchor='lm')
            lg.text((620, y + 36), o, font=F(700, 30), fill=(200, 60, 55, A), anchor='lm')
            im.paste(l, (0, 0), l)
        if t >= 3.3:
            g.rounded_rectangle((30, 700, BW - 30, 960), 22, fill='white', outline=LINE, width=2)
            g.text((64, 745), 'Informe de origen de clientes', font=F(700, 30), fill=INK, anchor='lm')
            k = ease((t - 3.4) / 1.0); g.rectangle((64, 800, BW - 64, 850), fill=(236, 238, 242))
            g.rectangle((64, 800, 64 + int((BW - 128) * k), 850), fill=(160, 165, 175))
            g.text((64, 905), 'Sin rellenar / “no sé”', font=F(700, 28), fill=MUT, anchor='lm')
        card(im, t, 5.0, 'Tu mejor canal de captación', '“No sé”', 'y le metes dinero igual', cy=600, big_size=90)
        tag(g)
        return im


NEW = {'m01-oferta-lunes': OfertaLunes, 'm02-viral': Viral, 'm03-otro-nombre': OtroNombre, 'm04-origen-crm': OrigenDesconocido}
