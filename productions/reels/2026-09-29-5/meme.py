import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN, YEL = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88), (255, 204, 0)
DARK, PANEL, MUT, NAVY, LINE = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66), (40, 52, 78)
SKIN, SKIN2, HAIR = (236, 196, 160), (214, 170, 132), (52, 36, 28)

CHAT_END = 1.9     # fin del chat
GAL_END = 3.9      # fin de la galería
PUNCH = 6.3


def tag(g, x, y, txt, bg, fg=WHITE, s=28, anchor='l'):
    f = F(800, s); w = f.getlength(txt)
    x0 = x if anchor == 'l' else (x - w - 36 if anchor == 'r' else x - (w + 36) / 2)
    g.rounded_rectangle((x0, y - s * .9, x0 + w + 36, y + s * .9), int(s * .9), fill=bg)
    g.text((x0 + 18, y), txt, font=f, fill=fg, anchor='lm')


def person(s, cx, cy, sc, suit, extra=None, face=True, eyes_closed=False, t=0):
    """Figura de busto: cabeza en (cx, cy), escala sc."""
    r = 60 * sc
    s.rounded_rectangle((cx - 120 * sc, cy + 95 * sc, cx + 120 * sc, cy + 520 * sc), int(70 * sc), fill=suit)
    s.polygon([(cx - 30 * sc, cy + 95 * sc), (cx + 30 * sc, cy + 95 * sc), (cx, cy + 170 * sc)], fill=WHITE)
    s.rectangle((cx - 26 * sc, cy + 55 * sc, cx + 26 * sc, cy + 105 * sc), fill=SKIN2)
    s.ellipse((cx - r, cy - r * 1.15, cx + r, cy + r * 1.15), fill=SKIN)
    if extra == 'hair':
        s.chord((cx - r * 1.05, cy - r * 1.3, cx + r * 1.05, cy + r * .3), 180, 360, fill=HAIR)
    elif extra == 'long':
        s.chord((cx - r * 1.15, cy - r * 1.3, cx + r * 1.15, cy + r * .5), 180, 360, fill=(120, 70, 40))
        s.rectangle((cx - r * 1.15, cy - r * .1, cx - r * .8, cy + r * 1.4), fill=(120, 70, 40))
        s.rectangle((cx + r * .8, cy - r * .1, cx + r * 1.15, cy + r * 1.4), fill=(120, 70, 40))
    elif extra == 'bald':
        s.arc((cx - r, cy - r * 1.15, cx + r, cy + r * 1.15), 150, 210, fill=HAIR, width=int(8 * sc))
        s.arc((cx - r, cy - r * 1.15, cx + r, cy + r * 1.15), 330, 30, fill=HAIR, width=int(8 * sc))
    for ex in (-22, 22):
        if eyes_closed:
            s.arc((cx + ex * sc - 10 * sc, cy - 8 * sc, cx + ex * sc + 10 * sc, cy + 8 * sc), 20, 160, fill=DARK, width=max(2, int(4 * sc)))
        else:
            s.ellipse((cx + ex * sc - 7 * sc, cy - 7 * sc, cx + ex * sc + 7 * sc, cy + 7 * sc), fill=DARK)
    s.arc((cx - 26 * sc, cy + 14 * sc, cx + 26 * sc, cy + 44 * sc), 10, 170, fill=(150, 60, 60), width=max(2, int(6 * sc)))


def wedding(w, h, t):
    """La foto de la boda (2019): tú en el centro, el primo abrazándote, copa, corbata en la cabeza."""
    im = Image.new('RGB', (w, h)); s = ImageDraw.Draw(im)
    for y in range(h):
        k = y / h
        s.line([(0, y), (w, y)], fill=(int(255 - 60 * k), int(214 - 70 * k), int(160 - 60 * k)))
    # guirnalda de bombillas
    for i in range(14):
        x = i * w / 13; y = 60 + 30 * math.sin(i * .9)
        on = (i + int(t * 6)) % 3 != 0
        s.ellipse((x - 11, y - 11, x + 11, y + 11), fill=(255, 240, 170) if on else (200, 170, 110))
    s.line([(i * w / 13, 60 + 30 * math.sin(i * .9)) for i in range(14)], fill=(90, 70, 50), width=3)
    # tarta al fondo
    s.rectangle((w * .80, h * .32, w * .95, h * .52), fill=WHITE)
    s.rectangle((w * .83, h * .22, w * .92, h * .32), fill=(250, 245, 240))
    # personas: primo (izq), tú (centro), tía (dcha)
    cx = w // 2
    person(s, w * .19, h * .40, 1.0, (70, 40, 110), 'bald', eyes_closed=True)
    person(s, w * .81, h * .42, .95, (200, 60, 110), 'long')
    person(s, cx, h * .38, 1.15, (30, 38, 60), 'hair')
    # corbata atada a la cabeza
    s.rectangle((cx - 72, h * .38 - 88, cx + 72, h * .38 - 70), fill=RED)
    s.polygon([(cx + 66, h * .38 - 84), (cx + 120, h * .38 - 110), (cx + 110, h * .38 - 60)], fill=RED)
    # brazo del primo sobre tu hombro, con mano
    s.line([(w * .19 + 90, h * .40 + 170), (cx - 60, h * .38 + 150), (cx + 60, h * .38 + 140)], fill=(70, 40, 110), width=52)
    s.ellipse((cx + 40, h * .38 + 112, cx + 104, h * .38 + 172), fill=SKIN)
    # copa de cava levantada
    gx, gy = cx - 150, h * .38 + 40
    s.polygon([(gx - 24, gy - 70), (gx + 24, gy - 70), (gx + 8, gy + 10), (gx - 8, gy + 10)], fill=(255, 236, 150))
    s.line([(gx, gy + 10), (gx, gy + 60)], fill=(230, 230, 240), width=6)
    s.ellipse((gx - 30, gy + 44, gx + 30, gy + 76), fill=SKIN)
    # flash quemado
    s.ellipse((cx + 150, h * .20, cx + 260, h * .30), fill=(255, 255, 240))
    s.text((w - 20, h - 24), '15/06/2019', font=F(700, 30), fill=(255, 150, 60), anchor='rm')
    return im


def pixelate(im, k):
    w, h = im.size
    f = max(1, int(1 + 26 * k))
    return im.resize((max(1, w // f), max(1, h // f)), Image.BILINEAR).resize((w, h), Image.NEAREST)


class FotoWeb:
    POV = 'POV: te piden una foto profesional para la web… y solo tienes fotos de bodas'
    DUR, PUNCH, FOCUS = 7.8, PUNCH, (480, 500)
    SFX = ['pop@0.1', 'typing:0.5@0.35', 'ding@0.9', 'ding@1.4', 'pop@1.7', 'tick@2.2', 'tick@2.6', 'tick@3.0',
           'tick@3.4', 'pop@3.6', 'tick@4.3', 'tick@4.8', 'tick@5.3', 'tick@5.8', 'boom@6.3']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        if t < CHAT_END:
            self.chat(im, g, t)
        elif t < GAL_END:
            self.gallery(im, g, t)
        else:
            self.crop(im, g, t)
        # transición de barrido entre pantallas
        for tr in (CHAT_END, GAL_END):
            if tr - .12 <= t < tr + .18:
                q = (t - tr + .12) / .3
                x = int(BW * (1.2 - 1.4 * q))
                g.rectangle((x, 0, x + 60, BH), fill=BLUE)
        if t >= self.PUNCH - .35:
            self.punch(im, t)
        return im

    # ------------------------------------------------------------ 1. WhatsApp
    def chat(self, im, g, t):
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.ellipse((30, 22, 96, 88), fill=BLUE)
        g.text((63, 55), 'W', font=F(800, 36), fill=WHITE, anchor='mm')
        g.text((116, 40), 'Web nueva (proveedor)', font=F(800, 32), fill=WHITE, anchor='lm')
        st = 'escribiendo…' if .45 <= t < .95 else 'en línea'
        g.text((116, 78), st, font=F(600, 24), fill=GREEN if st != 'en línea' else MUT, anchor='lm')
        y = 170

        def bubble(y, lines, t0, mine=False, sz=44):
            k = pop((t - t0) / .3)
            if k <= .05: return y
            f = F(700, int(sz * min(1, k)) or 1)
            wmax = max(f.getlength(l) for l in lines)
            bw, bh = wmax + 60, len(lines) * sz * 1.35 + 44
            x0 = BW - 40 - bw if mine else 40
            g.rounded_rectangle((x0, y, x0 + bw, y + bh), 28, fill=BLUE if mine else (34, 44, 66))
            for i, l in enumerate(lines):
                g.text((x0 + 30, y + 22 + i * sz * 1.35), l, font=f, fill=WHITE, anchor='lt')
            g.text((x0 + bw - 18, y + bh - 14), '16:3' + str(int(t0 * 3) % 10) + (' ✓✓' if mine else ''), font=F(600, 18), fill=(190, 205, 235), anchor='rb')
            return y + bh + 26

        y = bubble(y, ['Para la sección "Equipo"', 'necesitamos tu foto'], -.5)
        y = bubble(y, ['Profesional, de estudio,', 'buena calidad. Para hoy'], .95)
        y = bubble(y, ['¡Claro! Tengo mil,', 'ahora te la paso'], 1.7, mine=True)
        # tecleo
        if .45 <= t < .95:
            g.rounded_rectangle((40, y, 170, y + 70), 30, fill=(34, 44, 66))
            for i in range(3):
                a = .5 + .5 * math.sin(t * 12 - i)
                g.ellipse((70 + i * 30 - 9, y + 35 - 9 - 6 * a, 70 + i * 30 + 9, y + 35 + 9 - 6 * a), fill=(200, 210, 235))
        g.rounded_rectangle((30, BH - 100, BW - 130, BH - 30), 35, fill=PANEL)
        g.text((64, BH - 65), 'Mensaje', font=F(600, 28), fill=MUT, anchor='lm')
        g.ellipse((BW - 110, BH - 100, BW - 40, BH - 30), fill=BLUE)

    # ------------------------------------------------------------ 2. Galería
    def gallery(self, im, g, t):
        d = t - CHAT_END
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.text((40, 55), 'Galería', font=F(800, 40), fill=WHITE, anchor='lm')
        g.rounded_rectangle((BW - 330, 30, BW - 40, 80), 25, fill=(34, 44, 66))
        g.text((BW - 310, 55), '🔍 "foto seria"', font=F(600, 26), fill=MUT, anchor='lm')
        labels = ['Boda primo', 'Selfie coche', 'Nochevieja', 'Playa 2016', 'Cena empresa', 'Boda Marta',
                  'Disfraz', 'Con gafas sol', 'Bautizo', 'Boda amigos', 'Feria', 'Selfie espejo',
                  'Carnet 2011', 'Boda primo', 'Barbacoa', 'Boda (otra)']
        cols, cw = 3, 290; gap = 20
        scroll = min(d, 1.6) ** 1.2 * 420
        sel = 13
        for i, lab in enumerate(labels):
            r, c = divmod(i, cols)
            x0 = 30 + c * (cw + gap); y0 = 130 + r * (cw + gap) - scroll
            if y0 > BH or y0 + cw < 110: continue
            hue = [(255, 190, 150), (120, 170, 230), (60, 40, 120), (255, 220, 120), (200, 90, 90), (250, 200, 210)][i % 6]
            th = Image.new('RGB', (cw, cw), hue); s = ImageDraw.Draw(th)
            s.ellipse((cw * .3, cw * .18, cw * .7, cw * .6), fill=SKIN)
            s.rounded_rectangle((cw * .18, cw * .6, cw * .82, cw * 1.2), 40, fill=(30, 38, 60) if 'Boda' in lab else (90, 100, 130))
            if 'gafas' in lab or 'Playa' in lab:
                s.rectangle((cw * .34, cw * .33, cw * .66, cw * .40), fill=DARK)
            if 'Boda' in lab:
                s.ellipse((cw * .72, cw * .1, cw * .9, cw * .28), fill=(255, 240, 170))
            im.paste(th, (int(x0), int(y0)))
            g.rounded_rectangle((x0 + 10, y0 + cw - 50, x0 + 10 + F(700, 22).getlength(lab) + 24, y0 + cw - 12), 14, fill=(0, 0, 0))
            g.text((x0 + 22, y0 + cw - 31), lab, font=F(700, 22), fill=WHITE, anchor='lm')
            if i == sel and d > 1.5:
                k = pop((d - 1.5) / .25)
                g.rounded_rectangle((x0 - 6, y0 - 6, x0 + cw + 6, y0 + cw + 6), 14, outline=BLUE, width=max(1, int(10 * k)))
                g.ellipse((x0 + cw - 60, y0 + 14, x0 + cw - 14, y0 + 60), fill=BLUE)
                g.line([(x0 + cw - 50, y0 + 38), (x0 + cw - 40, y0 + 48), (x0 + cw - 24, y0 + 26)], fill=WHITE, width=5)
        g.rectangle((0, 0, BW, 110), fill=PANEL)
        g.text((40, 55), 'Galería', font=F(800, 40), fill=WHITE, anchor='lm')
        g.rounded_rectangle((BW - 330, 30, BW - 40, 80), 25, fill=(34, 44, 66))
        g.text((BW - 310, 55), 'Buscar: "foto seria"', font=F(600, 24), fill=MUT, anchor='lm')
        # resultado de búsqueda
        g.rectangle((0, BH - 90, BW, BH), fill=PANEL)
        g.text((BW // 2, BH - 45), '0 resultados para "foto seria"  ·  38 bodas', font=F(800, 28), fill=YEL, anchor='mm')

    # ------------------------------------------------------------ 3. Recortar
    def crop(self, im, g, t):
        d = t - GAL_END
        g.rectangle((0, 0, BW, 100), fill=PANEL)
        g.text((40, 50), 'Cancelar', font=F(700, 28), fill=MUT, anchor='lm')
        g.text((BW // 2, 50), 'Recortar', font=F(800, 34), fill=WHITE, anchor='mm')
        g.text((BW - 40, 50), 'Listo', font=F(800, 28), fill=BLUE, anchor='rm')
        PW, PH0 = 900, 740
        photo = wedding(PW, PH0, t)
        # recorte que se cierra sobre tu cara
        k = ease(min(1, d / 2.0))
        full = (0, 0, PW, PH0)
        cx, cy = PW // 2 + 10, int(PH0 * .38) + 40
        tgt = (cx - 150, cy - 170, cx + 150, cy + 170)
        box = tuple(full[i] + (tgt[i] - full[i]) * k for i in range(4))
        # la vista se amplía al recorte y se pixela
        crop = photo.crop(tuple(int(v) for v in box))
        bw, bh = box[2] - box[0], box[3] - box[1]
        scale = min(PW / bw, PH0 / bh)
        vw, vh = int(bw * scale), int(bh * scale)
        view = crop.resize((vw, vh), Image.BILINEAR)
        view = pixelate(view, max(0, (k - .35) / .65))
        ox, oy = 30 + (PW - vw) // 2, 120 + (PH0 - vh) // 2
        im.paste(view, (ox, oy))
        # marco de recorte con esquinas
        g.rectangle((ox, oy, ox + vw, oy + vh), outline=WHITE, width=3)
        for i in (1, 2):
            g.line([(ox + vw * i // 3, oy), (ox + vw * i // 3, oy + vh)], fill=(255, 255, 255), width=1)
            g.line([(ox, oy + vh * i // 3), (ox + vw, oy + vh * i // 3)], fill=(255, 255, 255), width=1)
        L = 44
        for (px, py, dx, dy) in [(ox, oy, 1, 1), (ox + vw, oy, -1, 1), (ox, oy + vh, 1, -1), (ox + vw, oy + vh, -1, -1)]:
            g.line([(px, py), (px + dx * L, py)], fill=WHITE, width=9); g.line([(px, py), (px, py + dy * L)], fill=WHITE, width=9)
        # barra inferior: zoom + calidad
        zoom = int(100 + 700 * k)
        g.rectangle((0, 880, BW, BH), fill=DARK)
        g.text((40, 930), f'Zoom {zoom} %', font=F(800, 36), fill=WHITE, anchor='lm')
        q = 'nítida' if k < .35 else ('regular' if k < .7 else 'patata')
        tag(g, BW - 40, 930, f'Calidad: {q}', GREEN if k < .35 else (YEL if k < .7 else RED), s=30, anchor='r')
        g.rounded_rectangle((40, 968, BW - 40, 980), 6, fill=LINE)
        g.rounded_rectangle((40, 968, 40 + (BW - 80) * k, 980), 6, fill=BLUE)
        # avisos que van saltando
        if 1.0 <= d < 2.4:
            kk = pop((d - 1.0) / .3)
            if kk > .1: tag(g, 60, 160, 'Quitar la copa…', (0, 0, 0), s=max(2, int(30 * kk)))
        if 1.6 <= d < 2.4:
            kk = pop((d - 1.6) / .3)
            if kk > .1: tag(g, BW - 60, 230, '¿y la mano del primo?', RED, s=max(2, int(30 * kk)), anchor='r')

    # ------------------------------------------------------------ remate
    def punch(self, im, t):
        kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
        cw, ch = int(500 * kk), int(560 * kk); cx, cy = self.FOCUS
        lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 32, fill=WHITE + (255,))
        im.paste(l, (0, 0), l)
        if kk > .85:
            g = ImageDraw.Draw(im)
            g.rounded_rectangle((cx - 170, cy - 250, cx + 170, cy - 200), 25, fill=BLUE)
            g.text((cx, cy - 225), 'WEB · NUESTRO EQUIPO', font=F(800, 24), fill=WHITE, anchor='mm')
            # avatar redondo pixelado con la mano del primo
            photo = wedding(900, 740, t)
            fc = photo.crop((290, 120, 630, 460)).resize((220, 220))
            fc = pixelate(fc, .2)
            mk = Image.new('L', (220, 220), 0); ImageDraw.Draw(mk).ellipse((0, 0, 219, 219), fill=255)
            im.paste(fc, (cx - 110, cy - 185), mk)
            g.ellipse((cx - 112, cy - 187, cx + 112, cy + 37), outline=BLUE, width=6)
            g.text((cx, cy + 84), '«Foto profesional»', font=F(800, 42), fill=NAVY, anchor='mm')
            g.text((cx, cy + 140), 'mano del primo: incluida', font=F(800, 30), fill=RED, anchor='mm')
            g.text((cx, cy + 182), 'corbata en la cabeza: a medias', font=F(700, 22), fill=(90, 100, 120), anchor='mm')
            g.text((cx, cy + 216), 'resolución: 180 px', font=F(700, 22), fill=(90, 100, 120), anchor='mm')


NEW = {'p-foto-web-bodas': FotoWeb}
