"""Memes del día 2026-09-27: 20 reels POV nuevos (m01…m20). Motor: toolkit/reels/pov_reel.py."""
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


# ------------------------------------------------------------------ m01. EL LEAD QUE NO APARECE (calendario + videollamada)
class NoShow:
    POV = 'POV: el lead agenda la llamada él solito y a la hora de la reunión no aparece'
    DUR, PUNCH, FOCUS = 7.6, 5.9, (400, 110)
    SFX = ['pop@0.4', 'ding@1.2', 'pop@2.1', 'count:3.0@2.3', 'ding@5.2', 'boom@5.9']

    def draw(self, t):
        INK, MUT, LINE, BLU = (32, 33, 36), (95, 99, 104), (226, 228, 232), (26, 115, 232)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.text((40, 48), 'Calendario', font=F(700, 36), fill=INK, anchor='lm')
        g.text((BW - 40, 48), 'Martes, 10:00', font=F(600, 28), fill=MUT, anchor='rm')
        g.line([(0, 96), (BW, 96)], fill=LINE, width=2)
        for i, h in enumerate(['9:00', '10:00', '11:00', '12:00']):
            yy = 140 + i * 200; g.text((30, yy), h, font=F(500, 24), fill=MUT, anchor='lm'); g.line([(120, yy), (BW, yy)], fill=LINE, width=2)
        if t >= .4:
            k = pop((t - .4) / .35); A = 255; l, lg = layer()
            x0, y0, x1, y1 = 140, 340, BW - 30, 440
            lg.rounded_rectangle((x0, y0, x0 + int((x1 - x0) * min(1, k)), y1), 12, fill=(3, 155, 229, A))
            if k > .9:
                lg.text((x0 + 24, y0 + 28), 'Videollamada con lead (reserva web)', font=F(700, 28), fill='white', anchor='lm')
                lg.text((x0 + 24, y0 + 70), '10:00 – 10:30 · lo agendó él', font=F(500, 24), fill=(225, 240, 250), anchor='lm')
            im.paste(l, (0, 0), l)
        # línea de "ahora"
        ny = 330 + 60 * ease((t - .4) / 5)
        g.ellipse((114, ny - 9, 132, ny + 9), fill=(234, 67, 53)); g.line([(122, ny), (BW, ny)], fill=(234, 67, 53), width=3)
        if t >= 1.2: banner(im, t, 1.2, 'Calendario · ahora', 'Tu reunión empieza en 5 minutos', t1=2.0, icol=BLU, ich='31'[0])
        # sala de espera
        if t >= 2.1:
            k = ease((t - 2.1) / .35); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((60, 500, BW - 60, 930), 28, fill=(32, 33, 36, A))
            lg.ellipse((BW // 2 - 60, 540, BW // 2 + 60, 660), fill=(95, 99, 104, A))
            lg.text((BW // 2, 600), '?', font=F(800, 60), fill=(255, 255, 255, A), anchor='mm')
            lg.text((BW // 2, 710), 'Esperando a que se una el invitado…', font=F(600, 30), fill=(232, 234, 237, A), anchor='mm')
            sec = 0 if t < 2.3 else 25 * 60 * ease((t - 2.3) / 3.0) + 14
            lg.text((BW // 2, 800), timer(sec), font=F(800, 90), fill=(255, 255, 255, A), anchor='mm')
            lg.text((BW // 2, 880), 'Tú: con la camisa buena', font=F(500, 24), fill=(170, 174, 180, A), anchor='mm')
            im.paste(l, (0, 0), l)
        if t >= 5.2:
            banner(im, t, 5.2, 'WhatsApp · Lead (reserva web)', '“Uy, ¿era hoy? Es que se me ha liado”', icol=(37, 211, 102), ich='W',
                   sub='“Lo dejamos para otra semana mejor”')
        tag(g, y=BH - 30)
        return im


# ------------------------------------------------------------------ m02. PAGARTE EN VISIBILIDAD (WhatsApp)
class Visibilidad(WAChat):
    POV = 'POV: le pasas el presupuesto al cliente y te ofrece pagarte “en visibilidad”'
    DUR, PUNCH, FOCUS = 7.6, 5.7, (320, 750)
    NAME, LETTER, HOUR = 'Cliente (tienda de ropa)', 'T', '17:1'
    MSGS = [(0.3, 'out', 'Te paso el presupuesto: 1.900 € la campaña completa.'),
            (1.5, 'in', '¿Y si en vez de pagarte te etiqueto en mis historias?'),
            (3.3, 'in', 'Tengo 380 seguidores'),
            (4.9, 'in', 'Y casi todos son de mi familia')]
    TYPING = [(2.2, 3.2), (3.9, 4.8)]
    SFX = ['pop@0.3', 'pop@1.5', 'typing:1.0@2.2', 'pop@3.3', 'typing:0.9@3.9', 'pop@4.9', 'boom@5.7']

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g); return im


# ------------------------------------------------------------------ m03. LA APAGAS EL DÍA 2 (Administrador de anuncios)
class ApagaDia2:
    POV = 'POV: lanzas la campaña el lunes y el martes la apagas porque “no funciona”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 640)
    SFX = ['pop@0.3', 'tick@1.4', 'tick@2.6', 'pop@3.8', 'tick@4.4', 'pop@5.2', 'boom@5.8']

    def draw(self, t):
        BG, INK, MUT, LINE, BLU, GRN, YEL = (242, 244, 247), (28, 30, 33), (101, 103, 107), (221, 223, 226), (8, 102, 255), (49, 162, 76), (247, 185, 40)
        im = Image.new('RGB', (BW, BH), BG); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill='white'); g.line([(0, 110), (BW, 110)], fill=LINE, width=2)
        g.text((40, 55), 'Administrador de anuncios', font=F(700, 36), fill=INK, anchor='lm')
        g.rounded_rectangle((30, 140, BW - 30, 470), 18, fill='white', outline=LINE, width=2)
        on = t < 4.4
        tx, ty = 64, 180
        g.rounded_rectangle((tx, ty, tx + 84, ty + 46), 23, fill=BLU if on else (200, 202, 206))
        kx = tx + 60 if on else tx + 24; g.ellipse((kx - 19, ty + 4, kx + 19, ty + 42), fill='white')
        g.text((tx + 110, ty + 23), 'Captación leads — Octubre', font=F(700, 34), fill=INK, anchor='lm')
        if on:
            g.rounded_rectangle((64, 250, 330, 296), 23, fill=(255, 244, 214))
            g.text((197, 273), 'En aprendizaje', font=F(700, 26), fill=(160, 110, 0), anchor='mm')
        else:
            g.rounded_rectangle((64, 250, 300, 296), 23, fill=(236, 237, 240))
            g.text((182, 273), 'Desactivada', font=F(700, 26), fill=MUT, anchor='mm')
        day = 'Día 1 (lunes)' if t < 2.6 else 'Día 2 (martes)'
        g.text((BW - 64, 273), day, font=F(600, 26), fill=MUT, anchor='rm')
        for n, x in [('Resultados', 64), ('Gastado', 360), ('Conversiones', 640)]: g.text((x, 340), n, font=F(600, 26), fill=MUT)
        res = '0' if t < 1.4 else ('1' if t < 2.6 else '2')
        g.text((64, 380), res, font=F(800, 44), fill=INK)
        g.text((360, 380), eur(18.4 if t < 2.6 else 36.9), font=F(800, 44), fill=INK)
        g.text((640, 380), f'{res} / 50', font=F(800, 44), fill=(160, 110, 0) if on else MUT)
        # cursor que va al interruptor
        if 3.2 <= t < 5.2:
            k = ease((t - 3.2) / 1.0); bx, by = int(700 - (700 - (tx + 40)) * k), int(800 - (800 - (ty + 22)) * k)
            l, lg = layer()
            lg.polygon([(bx, by), (bx + 34, by + 12), (bx + 15, by + 18), (bx + 26, by + 44), (bx + 14, by + 49), (bx + 5, by + 22), (bx - 8, by + 34)],
                       fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
            if t < 4.4: lg.text((bx + 50, by + 40), '“esto no va”', font=F(700, 30), fill=(200, 40, 40, 255))
            im.paste(l, (0, 0), l)
        g.rounded_rectangle((30, 500, BW - 30, BH - 40), 18, fill='white', outline=LINE, width=2)
        g.text((64, 540), 'Lo que necesitaba la campaña:', font=F(700, 30), fill=INK)
        g.text((64, 600), 'unos días de datos para aprender', font=F(500, 28), fill=MUT)
        card(im, t, 5.2, 'Duración de la campaña', '36 horas', '“Es que los anuncios no funcionan”', cy=660, big_size=96)
        tag(g)
        return im


# ------------------------------------------------------------------ m04. EL HILO DE CORREO ETERNO (correo)
class HiloRe:
    POV = 'POV: el hilo de correo del presupuesto va por el mensaje 47 y el cliente pregunta esto'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 840)
    ROWS = [(0.5, 'Lo miro con calma y te digo'), (1.0, 'Adjunto versión 2 con cambios'), (1.5, 'A mi socio no le convence el azul'),
            (2.0, '¿Podemos hacer una llamada?'), (2.5, 'Vuelvo a adjuntar el PDF'), (3.0, 'Perdona, no me había llegado'),
            (3.5, 'Te reenvío lo de ayer'), (4.0, 'Te contesto la semana que viene')]
    SFX = ['pop@0.3'] + [f'tick@{r[0]}' for r in ROWS] + ['ding@5.0', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (32, 33, 36), (95, 99, 104), (232, 234, 237)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        n = 2 + sum(1 for ts, _ in self.ROWS if t >= ts) * 5 + (5 if t >= 5.0 else 0)
        n = min(n, 47)
        re = 'RE: ' * min(4, 1 + n // 12)
        g.rectangle((0, 0, BW, 150), fill=(246, 248, 252))
        subj = f'{re}FW: Presupuesto web'
        g.text((40, 50), subj, font=F(700, 34), fill=INK, anchor='lm')
        g.rounded_rectangle((40, 92, 290, 134), 21, fill=(232, 240, 254))
        g.text((165, 113), f'{n} mensajes', font=F(700, 24), fill=(26, 115, 232), anchor='mm')
        vis = [r for r in self.ROWS if t >= r[0]][-6:]
        for i, (ts, txt) in enumerate(vis):
            yy = 180 + i * 92; A = int(255 * ease((t - ts) / .25)); l, lg = layer()
            lg.ellipse((40, yy + 8, 100, yy + 68), fill=(189, 193, 198, A)); lg.text((70, yy + 38), 'C', font=F(700, 28), fill=(255, 255, 255, A), anchor='mm')
            lg.text((124, yy + 8), 'Cliente', font=F(700, 26), fill=INK + (A,))
            lg.text((124, yy + 44), txt, font=F(500, 26), fill=MUT + (A,))
            lg.line([(124, yy + 86), (BW, yy + 86)], fill=LINE + (A,), width=2)
            im.paste(l, (0, 0), l)
        if t >= 5.0:
            k = pop((t - 5.0) / .35); l, lg = layer(); yy = 780
            lg.rounded_rectangle((30, yy, BW - 30, yy + 130), 20, fill=(255, 244, 214, 255), outline=(247, 185, 40, 255), width=3)
            if k > .6:
                lg.text((64, yy + 22), 'Cliente · mensaje 47', font=F(700, 26), fill=INK + (255,))
                lg.text((64, yy + 64), '“Entonces… ¿al final cuánto costaba?”', font=F(800, 34), fill=(180, 40, 30, 255))
            im.paste(l, (0, 0), l)
        tag(g, y=BH - 30)
        return im



# ------------------------------------------------------------------ m05. EL DOMINIO CADUCADO (notificaciones del móvil)
class Dominio:
    POV = 'POV: tu campaña por fin arranca y el mismo día caduca el dominio de tu web'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    NOTIFS = [(0.4, (8, 102, 255), 'A', 'Administrador de anuncios', 'Tu campaña ya está publicada'),
              (1.4, (234, 67, 53), 'C', 'Correo', 'Recordatorio: renueva tu dominio'),
              (2.4, (8, 102, 255), 'A', 'Administrador de anuncios', '38 clics en el enlace'),
              (3.4, (234, 67, 53), 'C', 'Correo', 'Tu dominio ha caducado'),
              (4.4, (8, 102, 255), 'A', 'Administrador de anuncios', '214 clics en el enlace')]
    SFX = [f'ding@{n[0]}' for n in NOTIFS] + ['pop@5.2', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (18, 22, 40)); g = ImageDraw.Draw(im)
        for yy in range(BH):
            c = int(18 + 30 * yy / BH); g.line([(0, yy), (BW, yy)], fill=(c, c // 2 + 10, 40 + c))
        g.text((BW // 2, 70), 'lunes, 9 de octubre', font=F(600, 30), fill=(230, 230, 240), anchor='mm')
        g.text((BW // 2, 170), '10:14', font=F(800, 130), fill='white', anchor='mm')
        vis = [n for n in self.NOTIFS if t >= n[0]]
        for i, (ts, col, ch, app, txt) in enumerate(reversed(vis)):
            k = ease((t - ts) / .3); yy = 290 + i * 128 - int((1 - k) * 60); A = int(255 * k)
            l, lg = layer()
            lg.rounded_rectangle((40, yy, BW - 40, yy + 112), 26, fill=(245, 245, 250, int(225 * k)))
            lg.rounded_rectangle((66, yy + 26, 126, yy + 86), 14, fill=col + (A,))
            lg.text((96, yy + 56), ch, font=F(800, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((150, yy + 22), app, font=F(600, 24), fill=(90, 90, 100, A))
            lg.text((150, yy + 58), txt, font=F(700, 30), fill=((200, 30, 30) if 'caducado' in txt else (20, 20, 25)) + (A,))
            lg.text((BW - 70, yy + 22), 'ahora', font=F(500, 22), fill=(120, 120, 130, A), anchor='ra')
            im.paste(l, (0, 0), l)
        if t >= 5.2:
            kk = pop((t - 5.2) / .35); l, lg = layer(); cx, cy = BW // 2, 600; cw, ch_ = 820, 380
            sw, sh = int(cw * kk), int(ch_ * kk)
            lg.rounded_rectangle((cx - sw // 2, cy - sh // 2, cx + sw // 2, cy + sh // 2), 28, fill=(255, 255, 255, 255))
            if kk > .9:
                lg.text((cx, cy - 120), 'tunegocio-burgos.es', font=F(600, 32), fill=(95, 99, 104), anchor='mm')
                lg.text((cx, cy - 10), 'SE VENDE', font=F(800, 96), fill=(217, 48, 37), anchor='mm')
                lg.text((cx, cy + 100), 'Este dominio está disponible', font=F(600, 30), fill=(95, 99, 104), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g, dark=True)
        return im


# ------------------------------------------------------------------ m06. LA FICHA DE GOOGLE (buscador / mapas)
class FichaGoogle:
    POV = 'POV: un cliente te dice que no te encuentra en Google y buscas tu propio negocio'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (420, 700)
    Q = 'carpintería en burgos'
    SFX = ['typing:1.4@0.3', 'pop@2.0', 'tick@3.0', 'tick@3.6', 'pop@4.4', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE, BLU = (32, 33, 36), (95, 99, 104), (223, 225, 229), (26, 115, 232)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rounded_rectangle((30, 30, BW - 30, 110), 40, fill='white', outline=LINE, width=3)
        n = int(len(self.Q) * min(1, max(0, (t - .3) / 1.4)))
        q = self.Q[:n] + ('|' if t < 1.9 and int(t * 4) % 2 == 0 else '')
        g.text((80, 70), q, font=F(500, 32), fill=INK, anchor='lm')
        g.ellipse((BW - 90, 50, BW - 60, 80), outline=BLU, width=4); g.line([(BW - 64, 76), (BW - 52, 88)], fill=BLU, width=4)
        if t >= 2.0:
            k = ease((t - 2.0) / .35); l, lg = layer(); A = int(255 * k)
            lg.rectangle((0, 140, BW, 330), fill=(229, 227, 223, A))
            for i in range(6): lg.line([(0, 160 + i * 34), (BW, 140 + i * 40)], fill=(255, 255, 255, A), width=6)
            lg.ellipse((BW // 2 - 22, 200, BW // 2 + 22, 244), fill=(234, 67, 53, A))
            lg.text((40, 360), 'Carpintería Hermanos Duero', font=F(700, 40), fill=INK + (A,))
            lg.text((40, 420), '3,9', font=F(600, 28), fill=MUT + (A,))
            lg.text((260, 420), '(7) · Carpintería', font=F(500, 28), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
            if k > .5: stars(g, 90, 422, 4, size=26)
        rows = [(3.0, 'Web', 'no añadida'), (3.6, 'Teléfono', 'no disponible')]
        for i, (ts, a, b) in enumerate(rows):
            if t < ts: continue
            A = int(255 * ease((t - ts) / .25)); l, lg = layer(); yy = 490 + i * 70
            lg.text((40, yy), a, font=F(600, 30), fill=INK + (A,)); lg.text((260, yy), b, font=F(500, 30), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
        if t >= 4.4:
            k = pop((t - 4.4) / .35); l, lg = layer(); yy = 700
            w_ = int(620 * min(1.05, k))
            lg.rounded_rectangle((40, yy - 45, 40 + w_, yy + 45), 18, fill=(252, 232, 230, 255))
            if k > .8: lg.text((70, yy), 'Cerrado permanentemente', font=F(800, 40), fill=(197, 34, 31), anchor='lm')
            im.paste(l, (0, 0), l)
        if t >= 5.0:
            A = int(255 * ease((t - 5.0) / .3)); l, lg = layer()
            lg.rounded_rectangle((40, 800, BW - 40, 890), 18, fill=(255, 244, 214, A))
            lg.text((BW // 2, 845), 'Foto principal: la furgoneta de 2016', font=F(600, 30), fill=(120, 80, 0, A), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g, y=BH - 40)
        return im


# ------------------------------------------------------------------ m07. "MI BASE DE DATOS" (Excel)
class BaseDatos:
    POV = 'POV: el cliente te pasa “su base de datos de clientes” para hacer email marketing'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 830)
    ROWS = [('Mamá', 'mama@hotmail.con', 'NO ENVIAR'), ('Paco (bar)', '—', 'le debo 20 €'),
            ('Fontanero', 'ni idea', 'el bueno'), ('Yo', 'yo@miempresa.es', 'prueba'),
            ('Cliente 2011', 'se fue a Suiza', ''), ('Gestoría', 'no molestar', 'IMPORTANTE')]
    SFX = ['pop@0.3'] + [f'tick@{0.9 + i * .6:.1f}' for i in range(6)] + ['pop@4.9', 'boom@5.8']

    def draw(self, t):
        INK, LINE, HDR = (32, 33, 36), (212, 214, 218), (33, 115, 70)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 90), fill=HDR)
        g.text((40, 45), 'clientes_TODOS_definitivo(3).xlsx', font=F(700, 30), fill='white', anchor='lm')
        cols = [(30, 'Nombre'), (290, 'Email'), (660, 'Notas')]
        g.rectangle((0, 120, BW, 180), fill=(232, 240, 234))
        for x, n in cols: g.text((x, 150), n, font=F(700, 30), fill=INK, anchor='lm')
        for i in range(8): g.line([(0, 180 + i * 80), (BW, 180 + i * 80)], fill=LINE, width=2)
        for x in (270, 640): g.line([(x, 120), (x, 740)], fill=LINE, width=2)
        for i, row in enumerate(self.ROWS):
            ts = .9 + i * .6
            if t < ts: continue
            A = int(255 * ease((t - ts) / .25)); l, lg = layer(); yy = 220 + i * 80
            for j, ((x, _), v) in enumerate(zip(cols, row)):
                f = F(600 if j == 2 else 500, 28)
                lg.text((x, yy), v, font=f, fill=((200, 40, 40) if j == 2 else INK) + (A,), anchor='lm')
            im.paste(l, (0, 0), l)
        g.rectangle((0, 760, BW, 780), fill=(243, 243, 243))
        if t >= 4.9:
            k = pop((t - 4.9) / .35); l, lg = layer(); A = 255
            lg.rounded_rectangle((60, 790, BW - 60, 790 + int(110 * min(1, k))), 20, fill=(252, 232, 230, A))
            if k > .8:
                lg.text((BW // 2, 822), 'Total de contactos: 6', font=F(600, 28), fill=(120, 60, 60, A), anchor='mm')
                lg.text((BW // 2, 866), 'Emails válidos: 1 (el suyo)', font=F(800, 38), fill=(200, 30, 30, A), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g, y=BH - 40)
        return im


# ------------------------------------------------------------------ m08. EL TEXTO DEL ANUNCIO (editor de diseño)
class TextoLargo:
    POV = 'POV: el cliente te manda “el texto para el anuncio” y quiere que se lea todo'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 560)
    TXT = ('Somos una empresa familiar con más de 30 años de experiencia en reformas integrales, cocinas, baños, tejados, '
           'fontanería, electricidad, pintura, pladur, suelos, ventanas, puertas, persianas, toldos, mamparas, calefacción, '
           'aire acondicionado, jardinería y limpieza de fin de obra. Presupuesto sin compromiso. Trabajamos en Burgos y '
           'provincia, también fines de semana y festivos. Aparcamiento gratuito. Pregunte por nuestras ofertas de temporada. '
           'Aceptamos tarjeta, transferencia y efectivo. Horario de lunes a viernes de 8 a 14 y de 16 a 20, sábados de 9 a 13. ')
    SFX = ['pop@0.3', 'typing:3.8@0.8', 'pop@5.2', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (235, 236, 240)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 90), fill=(40, 44, 52))
        g.text((40, 45), 'anuncio_reformas.png', font=F(600, 28), fill='white', anchor='lm')
        X0, Y0, X1, Y1 = 150, 130, 810, 790
        g.rectangle((X0, Y0, X1, Y1), fill=(255, 250, 240))
        g.rectangle((X0, Y0, X1, Y0 + 110), fill=(255, 106, 26))
        g.text(((X0 + X1) // 2, Y0 + 55), 'REFORMAS', font=F(800, 54), fill='white', anchor='mm')
        k = ease((t - .8) / 3.8) if t >= .8 else 0
        size = int(46 - 36 * k); txt = (self.TXT * 3)[:int(40 + 1100 * k)]
        f = F(500, max(10, size)); ls = wrap(txt, f, X1 - X0 - 60); lh = int(max(10, size) * 1.25)
        for j, s in enumerate(ls):
            yy = Y0 + 140 + j * lh
            if yy > Y1 - 20: break
            g.text((X0 + 30, yy), s, font=f, fill=(50, 40, 30))
        g.rounded_rectangle((BW - 250, 110, BW - 20, 170), 12, fill='white')
        g.text((BW - 135, 140), f'Letra: {max(4, size if k < 1 else 4)} pt', font=F(700, 26), fill=(40, 44, 52), anchor='mm')
        cm = [(0.8, '“Pon esto, que es cortito”'), (2.6, '“Y los servicios, que no falte ninguno”'), (4.2, '“Y el horario, por si acaso”')]
        for ts, c in cm:
            if ts <= t < ts + 1.6:
                A = int(255 * ease((t - ts) / .25)); l, lg = layer(); yy = BH - 110
                lg.rounded_rectangle((60, yy - 36, BW - 60, yy + 36), 18, fill=(255, 235, 59, A))
                lg.text((BW // 2, yy), c, font=F(700, 30), fill=(30, 30, 30, A), anchor='mm')
                im.paste(l, (0, 0), l)
        card(im, t, 5.2, 'Tamaño de la letra', '4 pt', '“¿Y por qué no me llama nadie?”', cy=560, big_size=110)
        tag(g, y=BH - 30)
        return im



# ------------------------------------------------------------------ m09. "YO NO HE RELLENADO NADA" (llamada)
class NoRellene:
    POV = 'POV: por fin te coge el teléfono el lead del formulario y te suelta esto'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 860)
    SFX = ['typing:1.4@0.2', 'ding@1.8', 'pop@2.2', 'pop@3.6', 'pop@5.1', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (28, 30, 36)); g = ImageDraw.Draw(im)
        for yy in range(BH):
            c = int(22 + 26 * yy / BH); g.line([(0, yy), (BW, yy)], fill=(c, c + 4, c + 14))
        r = 80 + (8 * math.sin(t * 8) if t < 1.8 else 0)
        g.ellipse((BW // 2 - r, 150 - r, BW // 2 + r, 150 + r), fill=(99, 105, 120))
        g.text((BW // 2, 150), 'L', font=F(800, 70), fill='white', anchor='mm')
        g.text((BW // 2, 280), 'Lead formulario (cocina)', font=F(700, 40), fill='white', anchor='mm')
        st = 'llamando…' if t < 1.8 else timer(max(0, t - 1.8) * 2.2)
        g.text((BW // 2, 335), st, font=F(500, 30), fill=(180, 184, 195), anchor='mm')
        lines = [(2.2, 'out', '¡Hola! Te llamo por la info de cocinas que pediste'),
                 (3.6, 'in', '¿Yo? Yo no he rellenado nada'),
                 (4.6, 'in', 'Y no me llames más, ¿eh?')]
        y = 400
        for ts, side, txt in lines:
            if t < ts: continue
            k = ease((t - ts) / .3); A = int(255 * k); l, lg = layer(); out = side == 'out'
            f = F(600, 32); ls = wrap(txt, f, 640); bw = max(f.getlength(x) for x in ls) + 56; bh = len(ls) * 44 + 36
            x0 = BW - 50 - bw if out else 50
            lg.rounded_rectangle((x0, y, x0 + bw, y + bh), 24, fill=((52, 120, 246) if out else (60, 63, 72)) + (A,))
            for j, x in enumerate(ls): lg.text((x0 + 28, y + 18 + j * 44), x, font=f, fill=(255, 255, 255, A))
            im.paste(l, (0, 0), l); y += bh + 22
        if t < 5.1:
            for i, (lab, col) in enumerate([('silencio', (60, 63, 72)), ('altavoz', (60, 63, 72)), ('colgar', (235, 64, 52))]):
                cx = 230 + i * 250; g.ellipse((cx - 55, 830, cx + 55, 940), fill=col)
                g.text((cx, 885), lab, font=F(600, 20), fill='white', anchor='mm')
        card(im, t, 5.1, 'Formulario enviado por', 'ÉL MISMO', 'hace 20 minutos, con su nombre y su móvil', cy=870, big_size=76, ch=240, cw=880)
        tag(g, dark=True, y=BH - 20)
        return im


# ------------------------------------------------------------------ m10. LA FACTURA VENCIDA (panel de cobros)
class Vencida:
    POV = 'POV: reclamas la factura vencida y el cliente te contesta “la semana que viene sin falta”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    SFX = ['pop@0.3', 'ding@1.6', 'tick@2.8', 'tick@3.4', 'tick@4.0', 'ding@4.5', 'pop@5.2', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE, PUR = (26, 31, 54), (105, 115, 134), (227, 232, 238), (99, 91, 255)
        im = Image.new('RGB', (BW, BH), (246, 249, 252)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 100), fill='white'); g.line([(0, 100), (BW, 100)], fill=LINE, width=2)
        g.text((40, 50), 'Cobros · Facturas', font=F(700, 34), fill=INK, anchor='lm')
        days = 63 + int(28 * ease((t - 2.8) / 1.6)) if t >= 2.8 else 63
        rows = [('F-0231', 'Cliente A', '1.200,00 €', 'Pagada', (0, 135, 90), (215, 247, 232)),
                ('F-0232', 'Cliente B', '850,00 €', 'Pagada', (0, 135, 90), (215, 247, 232)),
                ('F-0233', 'Cliente C', '2.400,00 €', f'Vencida · {days} días', (205, 45, 60), (255, 231, 235))]
        for i, (n, c, a, st, col, bg) in enumerate(rows):
            yy = 140 + i * 110
            g.rounded_rectangle((30, yy, BW - 30, yy + 92), 14, fill='white', outline=LINE, width=2)
            g.text((60, yy + 30), n, font=F(700, 28), fill=INK, anchor='lm'); g.text((60, yy + 66), c, font=F(500, 24), fill=MUT, anchor='lm')
            g.text((380, yy + 46), a, font=F(700, 30), fill=INK, anchor='lm')
            w_ = F(700, 24).getlength(st) + 36
            g.rounded_rectangle((BW - 60 - w_, yy + 26, BW - 60, yy + 66), 20, fill=bg)
            g.text((BW - 60 - w_ / 2, yy + 46), st, font=F(700, 24), fill=col, anchor='mm')
        chips = [(2.8, '1 semana después'), (3.4, '2 semanas después'), (4.0, '4 semanas después')]
        for i, (ts, lab) in enumerate(chips):
            if t < ts: continue
            k = pop((t - ts) / .3); l, lg = layer(); cy = 520 + i * 80; w_ = int((F(600, 30).getlength(lab) + 70) * min(1, k))
            lg.rounded_rectangle((BW // 2 - w_ // 2, cy - 30, BW // 2 + w_ // 2, cy + 30), 16, fill=(226, 230, 240, 255))
            if k > .8: lg.text((BW // 2, cy), lab, font=F(600, 30), fill=MUT, anchor='mm')
            im.paste(l, (0, 0), l)
        banner(im, t, 1.6, 'WhatsApp · Cliente C', '“La semana que viene sin falta, de verdad”', t1=2.8)
        banner(im, t, 4.5, 'WhatsApp · Cliente C', '“¿Me reenvías la factura? No la encuentro”', t1=5.3)
        card(im, t, 5.2, 'Factura F-0233', f'{days} días', 'vencida “la semana que viene sin falta”', cy=600, big_size=100)
        tag(g, y=BH - 30)
        return im


# ------------------------------------------------------------------ m11. EL SEO A 49 € (extracto del banco)
class SeoBarato:
    POV = 'POV: sumas lo que llevas pagado por el “SEO a 49 € al mes” que te vendieron por teléfono'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 620)
    SFX = ['pop@0.3', 'count:3.6@0.8', 'pop@5.1', 'boom@5.8']
    MESES = ['oct 2026', 'sep 2026', 'ago 2026', 'jul 2026', 'jun 2026', 'may 2026', 'abr 2026', 'mar 2026']

    def draw(self, t):
        INK, MUT, LINE, RED_ = (25, 30, 40), (110, 118, 130), (230, 233, 238), (205, 45, 60)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 170), fill=(0, 70, 140))
        g.text((40, 50), 'Tu banco · Movimientos', font=F(700, 32), fill='white', anchor='lm')
        g.rounded_rectangle((40, 96, BW - 40, 150), 27, fill=(20, 95, 170))
        g.text((80, 123), 'Buscar: “SEO PACK”', font=F(600, 28), fill=(220, 232, 245), anchor='lm')
        k = ease((t - .8) / 3.6) if t >= .8 else 0
        n = int(36 * k)
        off = (n * 26) % 90
        for i in range(8):
            yy = 200 + i * 90 - off
            if yy < 175: continue
            mes = self.MESES[i % 8]
            g.text((40, yy + 20), 'SEO PACK BASIC · recibo', font=F(600, 28), fill=INK)
            g.text((40, yy + 56), mes, font=F(500, 22), fill=MUT)
            g.text((BW - 40, yy + 38), '-49,00 €', font=F(700, 30), fill=RED_, anchor='rm')
            g.line([(40, yy + 88), (BW - 40, yy + 88)], fill=LINE, width=2)
        g.rectangle((0, 830, BW, BH), fill=(246, 248, 251)); g.line([(0, 830), (BW, 830)], fill=LINE, width=2)
        g.text((40, 870), f'{max(1, n)} recibos encontrados', font=F(600, 28), fill=MUT)
        g.text((40, 920), 'Total:', font=F(700, 34), fill=INK)
        g.text((BW - 40, 930), '-' + eur(49 * max(1, n)), font=F(800, 44), fill=RED_, anchor='rm')
        card(im, t, 5.1, 'Total pagado en SEO', '1.764 €', 'Tu web en Google: página 9', cy=620, big_size=100)
        tag(g, y=BH - 20)
        return im


# ------------------------------------------------------------------ m12. EL GRUPO DE WHATSAPP (WhatsApp)
class Grupo(WAChat):
    POV = 'POV: creas un grupo de WhatsApp con el cliente “para ir más rápido” con la web'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 820)
    NAME, LETTER = 'Proyecto web nueva', 'P'
    SYS = [(0.4, 'Tú creaste el grupo'), (1.1, 'Cliente añadió a Su mujer'), (1.7, 'Cliente añadió a Su cuñado'),
           (2.3, 'Cliente añadió a El gestor'), (2.9, 'Cliente añadió a Primo (sabe de webs)'), (3.5, 'Cliente añadió a 9 personas más')]
    SFX = ['pop@0.4'] + [f'pop@{a}' for a, _ in SYS[1:]] + ['ding@4.2', 'pop@5.2', 'boom@5.8']

    def status(self, t):
        n = 2 + sum(1 for ts, _ in self.SYS[1:5] if t >= ts) + (9 if t >= 3.5 else 0)
        return f'Tú, Cliente y {n - 2} más' if n > 2 else 'Tú, Cliente', WA_GREY

    def draw(self, t):
        im, g = self.base(t)
        y = 190
        for ts, txt in self.SYS:
            if t < ts: continue
            k = ease((t - ts) / .25); A = int(255 * k); l, lg = layer(); f = F(500, 28); w_ = f.getlength(txt) + 50
            lg.rounded_rectangle((BW // 2 - w_ / 2, y, BW // 2 + w_ / 2, y + 54), 14, fill=(24, 34, 40, A))
            lg.text((BW // 2, y + 27), txt, font=f, fill=(170, 185, 195, A), anchor='mm')
            im.paste(l, (0, 0), l); y += 62
        if t >= 4.2:
            k = ease((t - 4.2) / .3); A = int(255 * k); l, lg = layer()
            lg.rounded_rectangle((36, y + 10, 700, y + 130), 22, fill=WA_IN + (A,))
            lg.text((64, y + 26), 'Su cuñado', font=F(700, 28), fill=(255, 138, 96, A))
            lg.text((64, y + 70), 'Yo el logo lo haría en verde', font=F(500, 36), fill=WA_TXT + (A,))
            im.paste(l, (0, 0), l)
        self.footer(g)
        card(im, t, 5.2, 'Participantes del grupo', '15', 'Opiniones sobre el logo: 15', cy=835, big_size=80, ch=240)
        return im


NEW = {'m01-no-aparece': NoShow, 'm02-visibilidad': Visibilidad, 'm03-apaga-dia-2': ApagaDia2, 'm04-hilo-47': HiloRe,
       'm05-dominio': Dominio, 'm06-ficha-google': FichaGoogle, 'm07-base-datos': BaseDatos, 'm08-texto-largo': TextoLargo,
       'm09-no-rellene': NoRellene, 'm10-factura-vencida': Vencida, 'm11-seo-barato': SeoBarato, 'm12-grupo-whatsapp': Grupo}
