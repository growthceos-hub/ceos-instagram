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


NEW = {'m01-no-aparece': NoShow, 'm02-visibilidad': Visibilidad, 'm03-apaga-dia-2': ApagaDia2, 'm04-hilo-47': HiloRe}
