"""Memes del día 2026-10-01: 20 reels POV nuevos (m01…m20). Motor: toolkit/reels/pov_reel.py."""
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


def lock_bg(hour='21:47', date='jueves, 1 de octubre'):
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



# ------------------------------------------------------------------ m01. "COMO EL DE LA TELE" (WhatsApp)
class AnuncioTele(WAChat):
    POV = 'POV: el cliente quiere un anuncio “como los de la tele” y te dice su presupuesto'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    NAME, LETTER, HOUR = 'Cliente (cerrajería)', 'C', '10:1'
    MSGS = [(0.3, 'in', 'Quiero un anuncio de los buenos, como los de la tele. Con actores, dron y todo.'),
            (1.6, 'out', 'Me encanta. ¿Con qué presupuesto contamos?'),
            (3.1, 'in', '50 €. Y si sobra algo, lo ponemos en anuncios.')]
    TYPING = [(2.3, 3.0)]
    SFX = ['pop@0.3', 'pop@1.6', 'typing:0.7@2.3', 'pop@3.1', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im, g = self.base(t); self.bubbles(im, t); self.footer(g)
        card(im, t, 5.0, 'Presupuesto para actores y dron', '50 €', 'y que sobre para anuncios', cy=600, big_size=120)
        return im


# ------------------------------------------------------------------ m02. FASE DE APRENDIZAJE (administrador de anuncios)
class Aprendizaje:
    POV = 'POV: la campaña está en fase de aprendizaje y el cliente entra cada día a “mejorarla”'
    DUR, PUNCH, FOCUS = 7.8, 6.0, (480, 600)
    EDITS = [(0.9, 'Lunes', 'Cambia la foto'), (1.8, 'Martes', 'Sube el presupuesto'), (2.7, 'Miércoles', 'Cambia el texto'),
             (3.6, 'Jueves', 'Lo baja otra vez'), (4.5, 'Viernes', 'Nuevo público')]
    SFX = ['pop@0.3'] + [f'tick@{a}' for a, *_ in EDITS] + ['pop@5.2', 'boom@6.0']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (240, 242, 245)); g = ImageDraw.Draw(im)
        appbar(g, 'Administrador de anuncios', 'Reformas Castilla · Conjunto de anuncios')
        g.rounded_rectangle((30, 160, BW - 30, 420), 22, fill='white', outline=LINE, width=2)
        done = sum(1 for a, *_ in self.EDITS if t >= a)
        statusdot(g, 64, 210, 'Aprendizaje' if done < 3 else 'Aprendizaje limitado', (230, 160, 20) if done < 3 else (217, 48, 37))
        g.text((64, 270), 'Resultados para salir del aprendizaje', font=F(600, 28), fill=MUT, anchor='lm')
        prog = [0, 12, 18, 4, 9, 2][done] if t >= .3 else 0
        g.rounded_rectangle((64, 310, BW - 64, 350), 20, fill=(236, 238, 242))
        g.rounded_rectangle((64, 310, 64 + int((BW - 128) * prog / 50), 350), 20, fill=(8, 102, 255))
        g.text((BW - 64, 385), f'{prog} / 50', font=F(700, 28), fill=INK, anchor='rm')
        g.text((64, 385), 'Se reinicia con cada cambio importante', font=F(500, 24), fill=MUT, anchor='lm')
        g.text((64, 460), 'Historial de cambios', font=F(700, 32), fill=INK, anchor='lm')
        for i, (ts, d, txt) in enumerate(self.EDITS):
            if t < ts: continue
            y = 500 + i * 86; k = ease((t - ts) / .25); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((30, y, BW - 30, y + 74), 16, fill=(255, 255, 255, A))
            lg.text((64, y + 37), d, font=F(700, 28), fill=INK + (A,), anchor='lm')
            lg.text((290, y + 37), txt, font=F(600, 28), fill=MUT + (A,), anchor='lm')
            lg.text((BW - 64, y + 37), 'Cliente', font=F(600, 24), fill=(217, 48, 37, A), anchor='rm')
            im.paste(l, (0, 0), l)
        card(im, t, 5.2, 'Días que lleva aprendiendo', '23', 'y el que no aprende es otro', cy=600, big_size=130)
        tag(g)
        return im


# ------------------------------------------------------------------ m03. "MÁNDAMELO EN WORD" (correo)
class EnWord:
    POV = 'POV: mandas el presupuesto en PDF y el cliente te lo pide en Word “para cambiar un par de cosas”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    SFX = ['pop@0.4', 'ding@1.6', 'pop@3.2', 'tick@4.2', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill=(242, 246, 252)); g.text((40, 55), 'Re: Presupuesto web', font=F(700, 34), fill=INK, anchor='lm')
        if t >= .4:
            g.ellipse((40, 140, 110, 210), fill=(255, 106, 26)); g.text((75, 175), 'C', font=F(800, 32), fill='white', anchor='mm')
            g.text((130, 150), 'Ceos Growth', font=F(700, 30), fill=INK); g.text((BW - 40, 154), '09:12', font=F(500, 24), fill=MUT, anchor='ra')
            g.text((130, 192), 'Te adjunto el presupuesto. Cualquier duda, me dices.', font=F(500, 26), fill=MUT)
            g.rounded_rectangle((130, 240, 520, 310), 12, fill=(252, 235, 233)); g.text((160, 275), 'PDF  Presupuesto.pdf', font=F(700, 26), fill=(200, 50, 40), anchor='lm')
        g.line([(40, 340), (BW - 40, 340)], fill=LINE, width=2)
        if t >= 1.6:
            k = ease((t - 1.6) / .3); l, lg = layer(); A = int(255 * k)
            lg.ellipse((40, 370, 110, 440), fill=(52, 120, 200, A)); lg.text((75, 405), 'R', font=F(800, 32), fill=(255, 255, 255, A), anchor='mm')
            lg.text((130, 380), 'Cliente (Restaurante El Puente)', font=F(700, 30), fill=INK + (A,)); lg.text((BW - 40, 384), '09:14', font=F(500, 24), fill=MUT + (A,), anchor='ra')
            bf = F(500, 32)
            for j, s_ in enumerate(wrap('¿Me lo puedes pasar en Word? Es para cambiar un par de cosillas.', bf, BW - 180)):
                lg.text((130, 440 + j * 46), s_, font=bf, fill=INK + (A,))
            im.paste(l, (0, 0), l)
        if t >= 3.2:
            g.rounded_rectangle((40, 600, BW - 40, 900), 18, fill=(246, 247, 249), outline=LINE, width=2)
            g.text((70, 640), 'Cambios del cliente', font=F(700, 28), fill=INK, anchor='lm')
            for j, (ts, s_) in enumerate([(3.2, 'Precio: de 2.400 € a 800 €'), (3.7, 'Plazo: de 6 semanas a “el lunes”'), (4.2, 'Pagos: de 50 % al inicio a “ya veremos”')]):
                if t >= ts: g.text((70, 700 + j * 62), s_, font=F(600, 30), fill=(200, 50, 40), anchor='lm')
        card(im, t, 5.0, 'Un par de cosillas', 'Todo', 'menos el logo', cy=600, big_size=120)
        tag(g)
        return im


# ------------------------------------------------------------------ m04. ROAS #¡DIV/0! (Excel)
class DivCero:
    POV = 'POV: le pides al comercial cuánto te cuesta cada cita de la campaña y abre su Excel'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 600)
    ROWS = [('Gasto en anuncios', '600 €'), ('Clics', '1.240'), ('Leads', '38'), ('Llamadas hechas', '0'), ('Citas', '0')]
    SFX = ['pop@0.3', 'tick@0.8', 'tick@1.3', 'tick@1.8', 'tick@2.3', 'tick@2.8', 'typing:1.0@3.3', 'boom@4.5', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 90), fill=(16, 124, 65)); g.text((40, 45), 'citas_campaña_comercial.xlsx', font=F(700, 32), fill='white', anchor='lm')
        g.rectangle((0, 90, BW, 160), fill=(243, 243, 243))
        g.text((40, 125), 'fx', font=F(700, 28), fill=MUT, anchor='lm')
        n = int(len('=B1/B5') * min(1, max(0, (t - 3.3) / 1.0)))
        g.text((100, 125), '=B1/B5'[:n] if t >= 3.3 else '', font=F(600, 30), fill=INK, anchor='lm')
        g.rectangle((0, 160, 70, BH), fill=(243, 243, 243)); g.rectangle((0, 160, BW, 210), fill=(243, 243, 243))
        g.text((300, 185), 'A', font=F(600, 24), fill=MUT, anchor='mm'); g.text((760, 185), 'B', font=F(600, 24), fill=MUT, anchor='mm')
        for i in range(9):
            y = 210 + i * 80; g.line([(0, y + 80), (BW, y + 80)], fill=LINE, width=2); g.text((35, y + 40), str(i + 1), font=F(600, 24), fill=MUT, anchor='mm')
        g.line([(560, 160), (560, BH)], fill=LINE, width=2); g.line([(70, 160), (70, BH)], fill=LINE, width=2)
        for i, (a, b) in enumerate(self.ROWS):
            if t < .8 + i * .5: continue
            y = 210 + i * 80
            g.text((90, y + 40), a, font=F(600, 30), fill=INK, anchor='lm')
            g.text((BW - 40, y + 40), b, font=F(700, 30), fill=(200, 50, 40) if b == '0' else INK, anchor='rm')
        y = 210 + 6 * 80
        g.text((90, y + 40), 'Coste por cita', font=F(800, 30), fill=INK, anchor='lm')
        g.rectangle((560, y, BW, y + 80), outline=(16, 124, 65), width=4)
        if t >= 4.5:
            k = pop((t - 4.5) / .3); g.text((BW - 40, y + 40), '#¡DIV/0!', font=F(800, int(34 * max(.6, min(1.2, k)))), fill=(200, 50, 40), anchor='rm')
        card(im, t, 5.0, 'Coste por cita', '#¡DIV/0!', '38 leads y ninguna llamada', cy=600, big_size=80)
        tag(g)
        return im


NEW = {'m01-anuncio-tele': AnuncioTele, 'm02-aprendizaje': Aprendizaje, 'm03-en-word': EnWord, 'm04-div-cero': DivCero}
