import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw, ImageFilter

BLUE, WHITE, RED, GREEN, YEL = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88), (255, 204, 0)
DARK, PANEL, MUT, NAVY, LINE = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66), (40, 52, 78)

SW, SH = 880, 600          # tamaño de la escena "grabada"
REVIEW = 3.3               # empieza la revisión en el ordenador
WORDS = 'y así es como consigues que tu vídeo parezca de estudio. ¡Nos vemos!'.split()

PLANT = (690, 260)         # centro de la planta en la escena (donde se clava el enfoque)
FACE = (330, 250)


def _bg():
    im = Image.new('RGB', (SW, SH)); g = ImageDraw.Draw(im)
    for y in range(SH):
        k = y / SH
        g.line([(0, y), (SW, y)], fill=(int(206 - 40 * k), int(214 - 36 * k), int(230 - 30 * k)))
    # textura de pared (líneas finas: se ve la nitidez)
    for y in range(0, SH, 22):
        off = 0 if (y // 22) % 2 else 38
        g.line([(0, y), (SW, y)], fill=(178, 188, 208), width=1)
        for x in range(off, SW, 76):
            g.line([(x, y), (x, y + 22)], fill=(178, 188, 208), width=1)
    # cuadro con retícula fina
    g.rectangle((70, 60, 230, 200), fill=(250, 250, 252), outline=NAVY, width=6)
    for i in range(0, 140, 10):
        g.line([(82 + i, 72), (82 + i, 188)], fill=(120, 150, 210), width=1)
        g.line([(82, 72 + i), (218, 72 + i)], fill=(120, 150, 210), width=1)
    # estantería con libros
    g.rectangle((520, 400, 860, 414), fill=(90, 64, 44))
    x = 540
    for i, (w, h, c) in enumerate([(26, 90, (41, 121, 255)), (20, 76, (230, 230, 240)), (32, 98, (14, 30, 66)),
                                    (22, 70, (120, 160, 255)), (28, 86, (60, 70, 100)), (18, 64, (250, 250, 250))]):
        g.rectangle((x, 400 - h, x + w, 400), fill=c, outline=(20, 20, 30))
        g.line([(x + 4, 400 - h + 12), (x + w - 4, 400 - h + 12)], fill=(255, 255, 255), width=2)
        x += w + 4
    # planta (maceta + hojas con nervios)
    px, py = PLANT
    g.polygon([(px - 50, py + 80), (px + 50, py + 80), (px + 38, py + 140), (px - 38, py + 140)], fill=(245, 245, 250), outline=NAVY)
    g.line([(px - 46, py + 96), (px + 46, py + 96)], fill=BLUE, width=4)
    rnd = random.Random(7)
    for a in range(-80, 81, 20):
        r = math.radians(a - 90)
        L = 120 + rnd.randint(-15, 20)
        ex, ey = px + L * math.cos(r), py + 80 + L * math.sin(r)
        mx, my = (px + ex) / 2, (py + 80 + ey) / 2
        g.ellipse((mx - 26, my - 44, mx + 26, my + 44), fill=(34, 140, 70), outline=(10, 70, 30), width=2)
        g.line([(px, py + 80), (ex, ey)], fill=(12, 80, 36), width=2)
        for s in (-.2, .2):
            g.line([(mx, my), (mx + 22 * math.cos(r + 1.2 + s), my + 22 * math.sin(r + 1.2 + s))], fill=(160, 220, 170), width=1)
    return im


BG = None


def _person(t):
    l = Image.new('RGBA', (SW, SH), (0, 0, 0, 0)); g = ImageDraw.Draw(l)
    fx, fy = FACE
    br = 3 * math.sin(t * 3); fy += br
    g.rounded_rectangle((fx - 170, fy + 140, fx + 170, SH + 60), 90, fill=(41, 121, 255, 255))
    g.polygon([(fx - 40, fy + 140), (fx + 40, fy + 140), (fx, fy + 200)], fill=(255, 255, 255, 255))
    g.rectangle((fx - 36, fy + 80, fx + 36, fy + 150), fill=(226, 184, 150, 255))
    g.ellipse((fx - 90, fy - 110, fx + 90, fy + 110), fill=(236, 196, 160, 255))
    g.chord((fx - 96, fy - 124, fx + 96, fy + 30), 180, 360, fill=(60, 40, 30, 255))
    blink = (t % 2.4) < .12
    for ex in (-34, 34):
        if blink: g.line([(fx + ex - 12, fy + 5), (fx + ex + 12, fy + 5)], fill=DARK + (255,), width=5)
        else: g.ellipse((fx + ex - 10, fy - 5, fx + ex + 10, fy + 15), fill=DARK + (255,))
    g.arc((fx - 50, fy - 40, fx - 18, fy - 20), 200, 340, fill=(60, 40, 30, 255), width=5)
    g.arc((fx + 18, fy - 40, fx + 50, fy - 20), 200, 340, fill=(60, 40, 30, 255), width=5)
    talking = t < 2.6 or t > REVIEW + .4
    m = abs(math.sin(t * 11)) * 16 if talking else 2
    g.rounded_rectangle((fx - 26, fy + 52, fx + 26, fy + 58 + m), 10, fill=(150, 60, 60, 255))
    return l


def scene(t, blur_person, blur_bg):
    global BG
    if BG is None: BG = _bg()
    bg = BG.filter(ImageFilter.GaussianBlur(blur_bg)) if blur_bg > .2 else BG.copy()
    p = _person(t)
    if blur_person > .2: p = p.filter(ImageFilter.GaussianBlur(blur_person))
    bg.paste(p, (0, 0), p)
    return bg


def brackets(g, box, col, L=34, w=5):
    x0, y0, x1, y1 = box
    for (px, py, dx, dy) in [(x0, y0, 1, 1), (x1, y0, -1, 1), (x0, y1, 1, -1), (x1, y1, -1, -1)]:
        g.line([(px, py), (px + dx * L, py)], fill=col, width=w); g.line([(px, py), (px, py + dy * L)], fill=col, width=w)


def tag(g, x, y, txt, bg, fg=WHITE, s=30, anchor='l'):
    f = F(800, s); w = f.getlength(txt)
    x0 = x if anchor == 'l' else x - w - 36
    g.rounded_rectangle((x0, y - s * .9, x0 + w + 36, y + s * .9), int(s * .9), fill=bg)
    g.text((x0 + 18, y), txt, font=f, fill=fg, anchor='lm')


class Enfoque:
    POV = 'POV: la toma perfecta… y el enfoque estaba en la pared de detrás'
    DUR, PUNCH, FOCUS = 7.8, 6.2, (480, 470)
    SFX = ['pop@0.05', 'tick@0.7', 'tick@1.3', 'ding@2.0', 'tick@2.8', 'pop@3.3', 'typing:0.5@3.4',
           'boom@4.1', 'tick@4.8', 'ding@5.4', 'boom@6.2']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        if t < REVIEW:
            self.camera(im, g, t)
        else:
            self.editor(im, g, t)
        # flash de transición
        if REVIEW - .12 <= t < REVIEW + .18:
            a = 1 - abs(t - REVIEW) / .18
            l = Image.new('RGBA', (BW, BH), (255, 255, 255, int(255 * max(0, a)))); im.paste(l, (0, 0), l)
        if t >= self.PUNCH - .35:
            self.punch(im, t)
        return im

    # ---------------------------------------------------- fase 1: grabando en la cámara
    def camera(self, im, g, t):
        g.rectangle((0, 0, BW, 96), fill=PANEL)
        if int(t * 2.5) % 2 == 0 and t < 2.8: g.ellipse((36, 30, 70, 64), fill=RED)
        g.text((84, 48), 'REC' if t < 2.8 else 'STOP', font=F(800, 34), fill=RED if t < 2.8 else MUT, anchor='lm')
        secs = 58 + min(t, 2.8)
        g.text((BW // 2, 48), f'00:0{int(secs // 60)}:{int(secs % 60):02d}:{int((secs % 1) * 25):02d}', font=F(700, 34), fill=WHITE, anchor='mm')
        g.rounded_rectangle((BW - 250, 26, BW - 40, 70), 22, fill=BLUE)
        g.text((BW - 145, 48), 'TOMA 07', font=F(800, 28), fill=WHITE, anchor='mm')
        # cuerpo de cámara
        z = 1 + .04 * ease(t / REVIEW)
        cw, ch = int(860 * z), int(620 * z); cx, cy = BW // 2, 470
        g.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 46, fill=(28, 32, 42), outline=(60, 68, 88), width=3)
        lw, lh = int(640 * z), int(436 * z)
        lx, ly = cx - cw // 2 + int(30 * z), cy - lh // 2 - int(40 * z)
        sc = scene(t, 1.2, 1.2).resize((lw, lh), Image.LANCZOS)   # en la pantallita "se ve bien"
        im.paste(sc, (lx, ly))
        g.rectangle((lx - 3, ly - 3, lx + lw + 3, ly + lh + 3), outline=(0, 0, 0), width=4)
        # recuadro AF pequeñito (y verde) sobre la planta: la pista
        ax, ay = lx + PLANT[0] * lw / SW, ly + PLANT[1] * lh / SH
        brackets(g, (ax - 34, ay - 34, ax + 34, ay + 34), GREEN, L=12, w=3)
        g.text((lx + 16, ly + 22), 'AF-C', font=F(800, 22), fill=WHITE, anchor='lm')
        g.text((lx + lw - 16, ly + 22), '4K 25p', font=F(800, 22), fill=WHITE, anchor='rm')
        # botones a la derecha
        bx = lx + lw + int(80 * z)
        for i, lab in enumerate(['MENU', 'AF', 'ISO']):
            yy = ly + 40 + i * int(90 * z)
            g.ellipse((bx - 34, yy - 34, bx + 34, yy + 34), fill=(44, 50, 64), outline=(80, 90, 112), width=2)
            g.text((bx, yy), lab, font=F(700, 18), fill=MUT, anchor='mm')
        rr = int(46 * z); yy = ly + lh - 40
        g.ellipse((bx - rr, yy - rr, bx + rr, yy + rr), fill=(44, 50, 64), outline=(80, 90, 112), width=3)
        g.ellipse((bx - 22, yy - 22, bx + 22, yy + 22), fill=RED if t < 2.8 else (90, 30, 30))
        # subtítulo de lo que dices
        nw = min(len(WORDS), int(t / .2) + 3)
        line = ' '.join(WORDS[max(0, nw - 6):nw])
        g.text((cx, cy + ch // 2 - int(50 * z)), line, font=F(800, 36), fill=WHITE, anchor='mm')
        # sello
        if 2.0 <= t:
            k = pop((t - 2.0) / .3); s = int(44 * k)
            if s > 4:
                w = int(470 * k); h = int(84 * k); x0 = lx + lw // 2 - w // 2; y0 = ly + lh // 2 - h // 2
                g.rounded_rectangle((x0, y0, x0 + w, y0 + h), 22, fill=GREEN)
                g.text((x0 + w // 2, y0 + h // 2), '¡TOMA PERFECTA!', font=F(800, s), fill=WHITE, anchor='mm')
        # barra inferior
        g.rectangle((0, 900, BW, BH), fill=PANEL)
        msg = 'Guardado: TOMA_07.MP4' if t >= 2.8 else 'Grabando…  batería 84 %'
        g.text((40, 950), msg, font=F(700, 30), fill=GREEN if t >= 2.8 else MUT, anchor='lm')
        g.text((BW - 40, 950), 'nivel: estudio', font=F(800, 30), fill=WHITE, anchor='rm')

    # ---------------------------------------------------- fase 2: revisando en el ordenador al 100 %
    def editor(self, im, g, t):
        tt = t - REVIEW
        g.rectangle((0, 0, BW, 96), fill=PANEL)
        for i, c in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
            g.ellipse((36 + i * 36, 38, 58 + i * 36, 60), fill=c)
        g.text((170, 48), 'TOMA_07.MP4', font=F(800, 30), fill=WHITE, anchor='lm')
        zoom_lbl = '100 %' if tt > .5 else f'{int(25 + 75 * ease(tt / .5))} %'
        g.rounded_rectangle((BW - 200, 26, BW - 40, 70), 22, fill=BLUE)
        g.text((BW - 120, 48), 'ZOOM ' + zoom_lbl, font=F(800, 26), fill=WHITE, anchor='mm')
        # escena grande: tú borroso, la planta nítida (con zoom que se mueve)
        blur = 2 + 13 * ease((tt - .3) / .6)
        sc = scene(t, blur, 0)
        vx0, vy0, vw, vh = 40, 116, 880, 600
        # zoom lento hacia la cara y luego hacia la planta
        if tt < 1.7:
            z = 1 + .18 * ease(tt / 1.4); fx, fy = FACE
        else:
            z = 1.18 + .12 * ease((tt - 1.7) / .8); k = ease((tt - 1.7) / .7)
            fx, fy = FACE[0] + (PLANT[0] - FACE[0]) * k, FACE[1] + (PLANT[1] - FACE[1]) * k
        cw, ch = SW / z, SH / z
        x0 = min(max(0, fx - cw / 2), SW - cw); y0 = min(max(0, fy - ch / 2), SH - ch)
        crop = sc.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((vw, vh), Image.LANCZOS)
        im.paste(crop, (vx0, vy0))
        g.rectangle((vx0 - 2, vy0 - 2, vx0 + vw + 2, vy0 + vh + 2), outline=LINE, width=3)
        mp = lambda x, y: (vx0 + (x - x0) * z, vy0 + (y - y0) * z)
        # AF sobre la planta
        if tt > .8:
            px, py = mp(*PLANT)
            col = GREEN if int(t * 6) % 2 else WHITE
            r = 120 * z
            brackets(g, (px - r * .8, py - r * .6, min(px + r * .8, vx0 + vw - 14), min(py + r * 1.2, vy0 + vh - 14)), col, L=36, w=6)
            if tt > 1.0: tag(g, min(px + r * .8, vx0 + vw - 14), py - r * .6 - 40, 'AF: PLANTA', GREEN, s=30, anchor='r')
        # cara desenfocada
        if tt > .8:
            cx, cy = mp(*FACE)
            k = pop((tt - .8) / .3)
            if k > .1:
                tag(g, vx0 + 20, vy0 + vh - 44, 'TU CARA: DESENFOCADA', RED, s=int(30 * k) + 1)
        if tt > 2.1:
            px, py = mp(*PLANT)
            k = pop((tt - 2.1) / .3)
            if k > .1: tag(g, vx0 + vw - 20, vy0 + 44, 'cada hoja, en 4K', BLUE, s=int(28 * k) + 1, anchor='r')
        # timeline con cabezal
        g.rectangle((0, 740, BW, BH), fill=PANEL); g.line([(0, 740), (BW, 740)], fill=LINE, width=2)
        g.text((40, 782), 'VÍDEO', font=F(700, 24), fill=MUT, anchor='lm')
        g.text((BW - 40, 782), 'nitidez del sujeto', font=F(700, 24), fill=MUT, anchor='rm')
        for i in range(10):
            x = 40 + i * 88
            g.rounded_rectangle((x, 810, x + 82, 870), 8, fill=(30, 50, 96) if i % 2 else (38, 62, 120))
        # medidor de nitidez: planta vs tú
        prog = ease(tt / 1.2)
        g.text((40, 910), 'Planta', font=F(800, 28), fill=WHITE, anchor='lm')
        g.rounded_rectangle((170, 896, 560, 924), 14, fill=(30, 38, 56))
        g.rounded_rectangle((170, 896, 170 + int(390 * prog), 924), 14, fill=GREEN)
        g.text((40, 956), 'Tú', font=F(800, 28), fill=WHITE, anchor='lm')
        g.rounded_rectangle((170, 942, 560, 970), 14, fill=(30, 38, 56))
        g.rounded_rectangle((170, 942, 170 + max(28, int(390 * (1 - prog) * .9 + 12)), 970), 14, fill=RED)
        g.text((BW - 40, 910), '100 %', font=F(800, 30), fill=GREEN, anchor='rm')
        g.text((BW - 40, 956), f'{max(3, int(100 - 97 * prog))} %', font=F(800, 30), fill=RED, anchor='rm')
        hx = 40 + int(880 * min(1, tt / 2.9))
        g.line([(hx, 800), (hx, 880)], fill=WHITE, width=4)

    # ---------------------------------------------------- remate
    def punch(self, im, t):
        kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
        cw, ch = int(520 * kk), int(400 * kk); cx, cy = 480, 470
        lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 32, fill=WHITE + (255,))
        if kk > .85:
            lg.rounded_rectangle((cx - 140, cy - 170, cx + 140, cy - 120), 25, fill=BLUE + (255,))
            lg.text((cx, cy - 145), 'VEREDICTO', font=F(800, 26), fill=WHITE, anchor='mm')
            lg.text((cx, cy - 60), 'LA PLANTA', font=F(800, 66), fill=NAVY, anchor='mm')
            lg.text((cx, cy + 22), 'quedó de portada', font=F(800, 36), fill=BLUE, anchor='mm')
            lg.text((cx, cy + 100), 'tú, en modo acuarela', font=F(700, 28), fill=(80, 90, 110), anchor='mm')
        im.paste(l, (0, 0), l)


NEW = {'p-enfoque': Enfoque}
