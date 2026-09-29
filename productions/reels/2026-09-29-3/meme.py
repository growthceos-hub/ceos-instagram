import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'toolkit', 'reels'))
from memes import F, ease, pop, layer, BW, BH
from PIL import Image, ImageDraw

BLUE, WHITE, RED, GREEN, YEL = (41, 121, 255), (255, 255, 255), (255, 59, 48), (48, 209, 88), (255, 204, 0)
DARK, PANEL, MUT, NAVY, LINE = (8, 12, 22), (16, 22, 36), (130, 142, 165), (14, 30, 66), (40, 52, 78)

CALL = 3.0      # entra la llamada
ANSWER = 4.9    # descuelgas (sin querer... o queriendo)
SCRIPT = ['GUION REEL v3', '', 'Hola a todos,', 'hoy os cuento 3 trucos', 'para grabaros a cámara',
          'sin parecer un robot.', '', 'Truco 1: mira al objetivo,', 'no a tu propia cara.', '',
          'Truco 2: habla un poco', 'más lento de lo normal.', '', 'Truco 3: sonríe antes', 'de empezar a hablar.']
SAID = 'Hola a todos, hoy os cuento 3 trucos para grabaros a cámara sin parecer un robot'.split()
ANS = '¿Sí, mamá? No, no, no estoy ocupado'.split()

# zonas
CAM = (30, 116, 470, 876)       # vista de la cámara (izquierda)
PH = (500, 110, 930, 940)       # móvil-teleprompter (derecha)


def tag(g, x, y, txt, bg, fg=WHITE, s=28, anchor='l'):
    f = F(800, s); w = f.getlength(txt)
    x0 = x if anchor == 'l' else (x - w - 36 if anchor == 'r' else x - (w + 36) / 2)
    g.rounded_rectangle((x0, y - s * .9, x0 + w + 36, y + s * .9), int(s * .9), fill=bg)
    g.text((x0 + 18, y), txt, font=f, fill=fg, anchor='lm')


class Teleprompter:
    POV = 'POV: usas las notas del móvil de teleprompter… y a mitad de toma te llama tu madre'
    DUR, PUNCH, FOCUS = 7.8, 6.4, (480, 490)
    SFX = ['pop@0.05', 'tick@0.8', 'tick@1.6', 'ding@2.1', 'boom@3.0', 'tick@3.3', 'tick@3.6', 'tick@3.9',
           'tick@4.2', 'tick@4.5', 'pop@4.9', 'typing:0.9@5.1', 'ding@5.6', 'boom@6.4']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), DARK); g = ImageDraw.Draw(im)
        self.topbar(g, t)
        self.camera(im, g, t)
        self.phone(im, g, t)
        self.bottom(g, t)
        if t >= self.PUNCH - .35:
            self.punch(im, t)
        return im

    # ------------------------------------------------------------ barra superior
    def topbar(self, g, t):
        g.rectangle((0, 0, BW, 92), fill=PANEL)
        if int(t * 2.5) % 2 == 0: g.ellipse((34, 28, 68, 62), fill=RED)
        g.text((82, 46), 'REC', font=F(800, 34), fill=RED, anchor='lm')
        secs = 41 + t
        g.text((BW // 2 - 20, 46), f'00:00:{int(secs):02d}:{int((secs % 1) * 25):02d}', font=F(700, 34), fill=WHITE, anchor='mm')
        g.rounded_rectangle((BW - 230, 24, BW - 34, 68), 22, fill=BLUE)
        g.text((BW - 132, 46), 'TOMA 12', font=F(800, 28), fill=WHITE, anchor='mm')

    # ------------------------------------------------------------ vista de cámara con la persona
    def camera(self, im, g, t):
        x0, y0, x1, y1 = CAM; w, h = x1 - x0, y1 - y0
        sc = Image.new('RGB', (w, h)); s = ImageDraw.Draw(sc)
        for y in range(h):
            k = y / h
            s.line([(0, y), (w, y)], fill=(int(24 + 20 * k), int(46 + 26 * k), int(96 + 40 * k)))
        # softbox de fondo que respira
        gl = 150 + int(30 * math.sin(t * 2))
        s.rounded_rectangle((w - 150, 60, w - 40, 250), 16, fill=(gl, gl + 20, 255))
        s.line([(w - 95, 250), (w - 95, 420)], fill=(90, 110, 150), width=6)
        s.ellipse((40, 90, 120, 170), fill=(60, 90, 160))
        # persona
        cx, cy = w // 2 - 10, 330 + 4 * math.sin(t * 3)
        shock = CALL <= t < ANSWER
        if shock:  # respingo
            cy -= 16 * math.exp(-(t - CALL) * 5) * abs(math.sin((t - CALL) * 30))
        s.rounded_rectangle((cx - 170, cy + 150, cx + 170, h + 80), 90, fill=(250, 250, 252))
        s.polygon([(cx - 40, cy + 150), (cx + 40, cy + 150), (cx, cy + 210)], fill=BLUE)
        s.rectangle((cx - 36, cy + 90, cx + 36, cy + 160), fill=(226, 184, 150))
        s.ellipse((cx - 92, cy - 112, cx + 92, cy + 112), fill=(236, 196, 160))
        s.chord((cx - 98, cy - 126, cx + 98, cy + 26), 180, 360, fill=(52, 36, 28))
        # ojos: miran al móvil (a la derecha) mientras leen, abiertos de golpe con la llamada
        look = 10 if not shock else 0
        blink = .9 < (t % 2.3) < 1.0 and not shock
        for ex in (-34, 34):
            if blink: s.line([(cx + ex - 12, cy + 4), (cx + ex + 12, cy + 4)], fill=DARK, width=5)
            elif shock:
                s.ellipse((cx + ex - 16, cy - 14, cx + ex + 16, cy + 18), fill=WHITE)
                s.ellipse((cx + ex - 7, cy - 5, cx + ex + 7, cy + 9), fill=DARK)
            else: s.ellipse((cx + ex - 10 + look, cy - 6, cx + ex + 10 + look, cy + 14), fill=DARK)
        by = -8 if shock else 0
        s.arc((cx - 52, cy - 44 + by, cx - 16, cy - 22 + by), 200, 340, fill=(52, 36, 28), width=5)
        s.arc((cx + 16, cy - 44 + by, cx + 52, cy - 22 + by), 200, 340, fill=(52, 36, 28), width=5)
        if shock:
            s.ellipse((cx - 18, cy + 46, cx + 18, cy + 84), fill=(150, 60, 60))
        else:
            m = abs(math.sin(t * 11)) * 16
            s.rounded_rectangle((cx - 26, cy + 52, cx + 26, cy + 58 + m), 10, fill=(150, 60, 60))
        # tras descolgar: móvil en la oreja
        if t >= ANSWER:
            k = ease((t - ANSWER) / .3)
            px = cx + 150 - int(50 * k)
            s.rounded_rectangle((px - 28, cy - 60, px + 28, cy + 60), 12, fill=(20, 22, 30), outline=(90, 100, 120), width=3)
            s.ellipse((px - 30, cy + 40, px + 30, cy + 110), fill=(236, 196, 160))
        im.paste(sc, (x0, y0))
        g.rounded_rectangle((x0 - 3, y0 - 3, x1 + 3, y1 + 3), 18, outline=LINE, width=4)
        # retícula de tercios + AF en la cara
        for i in (1, 2):
            g.line([(x0 + w * i // 3, y0), (x0 + w * i // 3, y1)], fill=(120, 140, 190), width=1)
            g.line([(x0, y0 + h * i // 3), (x1, y0 + h * i // 3)], fill=(120, 140, 190), width=1)
        fx, fy = x0 + cx, y0 + cy
        col = GREEN if not shock else YEL
        for (px, py, dx, dy) in [(fx - 110, fy - 130, 1, 1), (fx + 110, fy - 130, -1, 1), (fx - 110, fy + 130, 1, -1), (fx + 110, fy + 130, -1, -1)]:
            g.line([(px, py), (px + dx * 26, py)], fill=col, width=4); g.line([(px, py), (px, py + dy * 26)], fill=col, width=4)
        g.text((x0 + 18, y0 + 26), '4K 25p', font=F(800, 22), fill=WHITE, anchor='lm')
        # subtítulos de lo que dices
        if t < CALL:
            nw = min(len(SAID), int(t / .19) + 2); words = SAID[max(0, nw - 4):nw]
        elif t < ANSWER:
            words = ['…'] if t < CALL + .6 else ['¿¿Ahora??']
        else:
            nw = min(len(ANS), int((t - ANSWER) / .16) + 1); words = ANS[max(0, nw - 5):nw]
        line = ' '.join(words)
        f = F(800, 32)
        while f.getlength(line) > w - 40 and len(words) > 1:
            words = words[1:]; line = ' '.join(words)
        tw = f.getlength(line)
        g.rounded_rectangle((x0 + w / 2 - tw / 2 - 16, y1 - 88, x0 + w / 2 + tw / 2 + 16, y1 - 36), 12, fill=(0, 0, 0))
        g.text((x0 + w / 2, y1 - 62), line, font=f, fill=YEL if t >= ANSWER else WHITE, anchor='mm')
        # etiquetas
        if 1.9 <= t < CALL:
            k = pop((t - 1.9) / .3)
            if k > .1: tag(g, x0 + w // 2, y0 + 80, 'VA PERFECTA', GREEN, s=max(2, int(30 * k)), anchor='c')
        if t >= ANSWER + .5:
            k = pop((t - ANSWER - .5) / .3)
            if k > .1: tag(g, x0 + w // 2, y0 + 80, 'SIGUE GRABANDO', RED, s=max(2, int(30 * k)), anchor='c')

    # ------------------------------------------------------------ móvil-teleprompter
    def phone(self, im, g, t):
        x0, y0, x1, y1 = PH
        shake = 0
        if CALL <= t < ANSWER and int((t - CALL) / .3) % 2 == 0:
            shake = 7 * math.sin(t * 95)
        x0 += shake; x1 += shake
        g.rounded_rectangle((x0, y0, x1, y1), 56, fill=(24, 26, 34), outline=(90, 100, 124), width=4)
        sx0, sy0, sx1, sy1 = int(x0 + 16), y0 + 16, int(x1 - 16), y1 - 16
        sw, sh = sx1 - sx0, sy1 - sy0
        scr = Image.new('RGB', (sw, sh), (250, 250, 247)); s = ImageDraw.Draw(scr)
        # --- app de Notas con el guion en scroll
        s.text((24, 30), '9:41', font=F(700, 24), fill=(20, 20, 20), anchor='lm')
        s.text((sw - 24, 30), '41 %', font=F(700, 22), fill=(20, 20, 20), anchor='rm')
        s.text((24, 84), '‹ Notas', font=F(700, 28), fill=(230, 160, 0), anchor='lm')
        s.text((sw - 24, 84), 'OK', font=F(800, 28), fill=(230, 160, 0), anchor='rm')
        lh = 56; top = 130
        scroll = min(t, CALL) * 70
        cur_y = top + 250
        for i, ln in enumerate(SCRIPT):
            y = top + i * lh - scroll + 60
            if y < top - 10 or y > sh - 20: continue
            active = abs(y - cur_y) < lh / 2 and ln
            if active:
                s.rounded_rectangle((12, y - 26, sw - 12, y + 26), 12, fill=(214, 229, 255))
            fnt = F(800, 30) if i == 0 else F(700 if active else 600, 28)
            s.text((24, y), ln, font=fnt, fill=NAVY if active else (60, 60, 66), anchor='lm')
        # guía de lectura
        s.polygon([(0, cur_y - 14), (12, cur_y), (0, cur_y + 14)], fill=BLUE)
        # --- llamada entrante que tapa el guion
        if t >= CALL:
            k = ease((t - CALL) / .35)
            ov = Image.new('RGB', (sw, sh)); o = ImageDraw.Draw(ov)
            for y in range(sh):
                q = y / sh
                o.line([(0, y), (sw, y)], fill=(int(20 + 20 * q), int(40 + 30 * q), int(90 + 60 * q)))
            if t < ANSWER:
                o.text((sw // 2, 150), 'llamada de móvil…', font=F(600, 28), fill=(200, 210, 235), anchor='mm')
            else:
                d = t - ANSWER
                o.text((sw // 2, 150), f'00:{int(d):02d}', font=F(700, 30), fill=(200, 210, 235), anchor='mm')
            o.text((sw // 2, 220), 'Mamá', font=F(800, 66), fill=WHITE, anchor='mm')
            r = 92 + (8 * math.sin(t * 12) if t < ANSWER else 0)
            o.ellipse((sw // 2 - r, 330 - r, sw // 2 + r, 330 + r), fill=(120, 150, 210))
            o.text((sw // 2, 330), 'M', font=F(800, 90), fill=WHITE, anchor='mm')
            if t < ANSWER:
                o.text((sw // 2, 470), 'tercera llamada seguida', font=F(600, 24), fill=(200, 210, 235), anchor='mm')
                for bx, col, lab in ((sw // 2 - 105, RED, 'Rechazar'), (sw // 2 + 105, GREEN, 'Aceptar')):
                    rr = 52
                    if col == GREEN:
                        pr = rr + 18 * ((t * 1.6) % 1)
                        o.ellipse((bx - pr, 640 - pr, bx + pr, 640 + pr), outline=(120, 230, 150), width=3)
                    o.ellipse((bx - rr, 640 - rr, bx + rr, 640 + rr), fill=col)
                    o.rounded_rectangle((bx - 24, 630, bx + 24, 650), 8, fill=WHITE)
                    o.text((bx, 720), lab, font=F(700, 24), fill=WHITE, anchor='mm')
            else:
                for i, lab in enumerate(['silencio', 'teclado', 'altavoz']):
                    bx = sw // 2 + (i - 1) * 120
                    o.ellipse((bx - 42, 560 - 42, bx + 42, 560 + 42), fill=(70, 90, 140) if i != 2 else WHITE)
                    o.text((bx, 620), lab, font=F(600, 22), fill=WHITE, anchor='mm')
                o.ellipse((sw // 2 - 50, 710 - 50, sw // 2 + 50, 710 + 50), fill=RED)
                o.rounded_rectangle((sw // 2 - 24, 700, sw // 2 + 24, 720), 8, fill=WHITE)
            yoff = int(-sh * (1 - k))
            scr.paste(ov, (0, yoff))
            # anillo del toque al descolgar
            if ANSWER <= t < ANSWER + .4:
                q = (t - ANSWER) / .4; rr = int(50 + 120 * q)
                s.ellipse((sw // 2 + 105 - rr, 640 - rr, sw // 2 + 105 + rr, 640 + rr), outline=(255, 255, 255), width=max(1, int(8 * (1 - q))))
        mk = Image.new('L', (sw, sh), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, sw - 1, sh - 1), 42, fill=255)
        im.paste(scr, (sx0, sy0), mk)
        g.rounded_rectangle((sx0 + sw // 2 - 70, sy0 + 10, sx0 + sw // 2 + 70, sy0 + 44), 17, fill=(10, 10, 14))
        # ondas de vibración
        if CALL <= t < ANSWER:
            for i in range(3):
                q = ((t - CALL) * 2 + i / 3) % 1
                a = int(255 * (1 - q)); off = 10 + int(40 * q)
                l, lg = layer()
                lg.arc((x1 - 40 + off - 30, y0 + 150, x1 + off + 10, y0 + 300), -60, 60, fill=BLUE + (a,), width=5)
                im.paste(l, (0, 0), l)
            tag(g, (PH[0] + PH[2]) // 2, PH[1] + 44 + 110, '¡ESTÁS GRABANDO!', RED, s=26, anchor='c') if int(t * 4) % 2 else None

    # ------------------------------------------------------------ barra inferior
    def bottom(self, g, t):
        g.rectangle((0, 900, 490, BH), fill=DARK)
        if t < CALL:
            line = min(len(SCRIPT), 4 + int(t / .75))
            g.text((40, 948), f'Guion: línea {line}/15', font=F(700, 30), fill=MUT, anchor='lm')
        elif t < ANSWER:
            g.text((40, 948), 'Guion: tapado por Mamá', font=F(800, 30), fill=YEL, anchor='lm')
        else:
            g.text((40, 948), 'Guion: ya da igual', font=F(800, 30), fill=RED, anchor='lm')

    # ------------------------------------------------------------ remate
    def punch(self, im, t):
        kk = pop((t - (self.PUNCH - .35)) / .35); l, lg = layer()
        cw, ch = int(440 * kk), int(430 * kk); cx, cy = self.FOCUS
        lg.rounded_rectangle((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2), 32, fill=WHITE + (255,))
        if kk > .85:
            lg.rounded_rectangle((cx - 150, cy - 180, cx + 150, cy - 128), 26, fill=BLUE + (255,))
            lg.text((cx, cy - 154), 'TOMA 12 · EN 4K', font=F(800, 26), fill=WHITE, anchor='mm')
            lg.text((cx, cy - 70), '«No, mamá,', font=F(800, 50), fill=NAVY, anchor='mm')
            lg.text((cx, cy - 12), 'no estoy', font=F(800, 50), fill=NAVY, anchor='mm')
            lg.text((cx, cy + 46), 'ocupado»', font=F(800, 50), fill=NAVY, anchor='mm')
            lg.text((cx, cy + 120), 'guion leído: 0 %', font=F(800, 30), fill=BLUE, anchor='mm')
            lg.text((cx, cy + 165), 'modo avión: nunca', font=F(700, 24), fill=(90, 100, 120), anchor='mm')
        im.paste(l, (0, 0), l)


NEW = {'p-teleprompter-mama': Teleprompter}
