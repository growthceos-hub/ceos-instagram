"""Tanda extra 2026-09-27: 20 memes POV nuevos (x01…x20). Motor: toolkit/reels/pov_reel.py."""
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


# ------------------------------------------------------------------ x01. "YA LE LLAMÉ" (CRM)
class YaLeLlame:
    POV = 'POV: el comercial te jura que “ya le llamó” y abres el historial del lead en el CRM'
    DUR, PUNCH, FOCUS = 7.4, 5.6, (480, 820)
    SFX = ['pop@0.4', 'pop@1.4', 'tick@2.4', 'tick@3.1', 'tick@3.8', 'pop@4.8', 'boom@5.6']

    def draw(self, t):
        INK, MUT, LINE, BLU = (33, 37, 41), (108, 117, 125), (226, 230, 234), (61, 99, 221)
        im = Image.new('RGB', (BW, BH), (245, 247, 250)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 100), fill=(34, 40, 49))
        g.text((40, 50), 'CRM · Oportunidades', font=F(700, 32), fill='white', anchor='lm')
        g.rounded_rectangle((30, 130, BW - 30, 380), 18, fill='white', outline=LINE, width=2)
        g.ellipse((60, 165, 150, 255), fill=(255, 106, 26)); g.text((105, 210), 'RP', font=F(700, 34), fill='white', anchor='mm')
        g.text((175, 170), 'Reformas Pradera', font=F(700, 38), fill=INK)
        g.text((175, 222), 'Presupuesto cocina · 18.000 €', font=F(500, 28), fill=MUT)
        g.rounded_rectangle((60, 290, 380, 350), 14, fill=(232, 245, 237))
        g.text((220, 320), 'Estado: CONTACTADO', font=F(700, 26), fill=(34, 139, 84), anchor='mm')
        g.text((420, 320), 'Asignado: Comercial 2', font=F(500, 26), fill=MUT, anchor='lm')
        g.text((40, 420), 'Historial de actividad', font=F(700, 32), fill=INK)
        rows = [(1.4, 'Lead creado desde formulario', 'hace 19 días'),
                (2.4, 'Llamadas registradas: 0', ''), (3.1, 'Correos enviados: 0', ''), (3.8, 'WhatsApps: 0', '')]
        for i, (ts, txt, when) in enumerate(rows):
            if t < ts: continue
            k = ease((t - ts) / .3); A = int(255 * k); yy = 480 + i * 96; l, lg = layer()
            lg.rounded_rectangle((30, yy, BW - 30, yy + 80), 14, fill=(255, 255, 255, A))
            z = i > 0
            lg.ellipse((56, yy + 26, 84, yy + 54), fill=((220, 53, 69) if z else BLU) + (A,))
            lg.text((104, yy + 40), txt, font=F(600 if z else 500, 30), fill=((200, 45, 60) if z else INK) + (A,), anchor='lm')
            if when: lg.text((BW - 56, yy + 40), when, font=F(500, 24), fill=MUT + (A,), anchor='rm')
            im.paste(l, (0, 0), l)
        if t >= 4.8:
            k = pop((t - 4.8) / .35); l, lg = layer(); A = 255
            cx, cy = BW // 2, 895; w_, h_ = int(470 * k), int(130 * k)
            lg.rounded_rectangle((cx - w_ // 2, cy - h_ // 2, cx + w_ // 2, cy + h_ // 2), 20, fill=(20, 20, 22, 250))
            if k > .9:
                lg.text((cx, cy - 30), 'Nota del comercial:', font=F(600, 26), fill=GRY, anchor='mm')
                lg.text((cx, cy + 18), '“le llamé pero no lo apunté”', font=F(700, 28), fill=(255, 170, 130), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g, y=60 + 0, x=BW - 40, dark=True)
        return im


# ------------------------------------------------------------------ x02. LA WEB DE 2014 (navegador)
class Web2014:
    POV = 'POV: pagas anuncios para mandar la gente a la web que te hicieron en 2014'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (330, 250)
    SFX = ['tick@0.3', 'count:2.6@0.6', 'pop@3.4', 'pop@4.3', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (255, 255, 255)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 120), fill=(222, 225, 230))
        g.rounded_rectangle((24, 30, BW - 24, 90), 30, fill='white')
        g.text((60, 60), 'www.tunegocio-oficial-burgos.es/inicio.html', font=F(500, 26), fill=(80, 84, 90), anchor='lm')
        # barra de carga
        k = min(1, ease((t - .6) / 2.8)) if t >= .6 else 0
        g.rectangle((0, 118, int(BW * .92 * k), 124), fill=(26, 115, 232))
        # contenido que va apareciendo "a trozos"
        if t >= 1.2:
            g.rectangle((0, 124, BW, 260), fill=(0, 0, 128))
            g.text((BW // 2, 192), 'BIENVENIDOS A NUESTRA WEB', font=F(800, 46), fill=(255, 255, 0), anchor='mm')
        if t >= 1.9:
            g.rectangle((40, 290, 440, 590), fill=(210, 210, 210)); g.line([(40, 290), (440, 590)], fill=(150, 150, 150), width=4)
            g.line([(440, 290), (40, 590)], fill=(150, 150, 150), width=4)
            g.text((240, 620), 'imagen_no_disponible.jpg', font=F(500, 22), fill=(140, 140, 140), anchor='mm')
        if t >= 2.5:
            for i, s in enumerate(['Somos lideres en', 'el sector desde', 'hace muchos años.', 'Contactenos por fax.']):
                g.text((480, 300 + i * 56), s, font=F(600, 34), fill=(200, 0, 0) if i == 3 else (0, 0, 0))
        if t >= 3.0:
            g.rectangle((0, 700, BW, 790), fill=(240, 240, 240))
            g.text((BW // 2, 745), 'Visitante número: 000417', font=F(700, 34), fill=(0, 128, 0), anchor='mm')
            g.text((BW // 2, 840), 'Última actualización: 03/2014', font=F(500, 28), fill=(120, 120, 120), anchor='mm')
        if t >= 3.4:
            kk = pop((t - 3.4) / .3); l, lg = layer(); w_, h_ = int(760 * kk), int(250 * kk); cx, cy = BW // 2, 520
            lg.rectangle((cx - w_ // 2, cy - h_ // 2, cx + w_ // 2, cy + h_ // 2), fill=(236, 233, 216, 255), outline=(0, 0, 0, 255), width=3)
            if kk > .9:
                lg.rectangle((cx - w_ // 2, cy - h_ // 2, cx + w_ // 2, cy - h_ // 2 + 50), fill=(10, 36, 106, 255))
                lg.text((cx - w_ // 2 + 20, cy - h_ // 2 + 25), 'Aviso', font=F(700, 26), fill='white', anchor='lm')
                lg.text((cx, cy + 5), 'Esta página necesita un', font=F(600, 32), fill='black', anchor='mm')
                lg.text((cx, cy + 50), 'complemento para verse bien', font=F(600, 32), fill='black', anchor='mm')
            im.paste(l, (0, 0), l)
        if t >= 4.3:
            banner(im, t, 4.3, 'Administrador de anuncios · ahora', '312 clics · 0 contactos', icol=(8, 102, 255), ich='A')
        tag(g)
        return im


# ------------------------------------------------------------------ x03. EL LOGO MÁS GRANDE (editor de diseño)
class LogoGrande:
    POV = 'POV: el cliente revisa el anuncio y solo pide una cosa: “el logo un poquito más grande”'
    DUR, PUNCH, FOCUS = 7.6, 5.9, (480, 750)
    STEPS = [(1.4, 1.0), (2.6, 1.7), (3.8, 2.6), (5.0, 4.2)]
    SFX = ['pop@0.3', 'ding@1.4', 'ding@2.6', 'ding@3.8', 'ding@5.0', 'boom@5.9']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (235, 236, 240)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 90), fill=(40, 44, 52))
        g.text((40, 45), 'anuncio_cliente_v7_FINAL.png', font=F(600, 28), fill='white', anchor='lm')
        g.rounded_rectangle((BW - 200, 22, BW - 30, 68), 10, fill=(125, 42, 232))
        g.text((BW - 115, 45), 'Descargar', font=F(700, 24), fill='white', anchor='mm')
        # lienzo
        X0, Y0, X1, Y1 = 150, 140, 810, 900
        g.rectangle((X0, Y0, X1, Y1), fill=(250, 246, 240))
        g.rectangle((X0, Y0 + 420, X1, Y1), fill=(222, 200, 172))
        g.text((X0 + 40, Y0 + 460), 'COCINAS A MEDIDA', font=F(800, 44), fill=(60, 45, 30))
        g.text((X0 + 40, Y0 + 520), 'Diseño y montaje en Burgos', font=F(500, 30), fill=(90, 70, 50))
        g.rounded_rectangle((X0 + 40, Y0 + 610, X0 + 340, Y0 + 680), 14, fill=(60, 45, 30))
        g.text((X0 + 190, Y0 + 645), 'Pide presupuesto', font=F(700, 26), fill='white', anchor='mm')
        s = 1.0
        for ts, sc in self.STEPS:
            if t >= ts: s = sc if t >= ts + .35 else s + (sc - s) * pop((t - ts) / .35)
        # logo
        l, lg = layer(); r = int(70 * s); q = (s - 1) / 3.2; cx, cy = int(260 + 220 * q), int(250 + 180 * q)
        lg.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 106, 26, 255))
        lg.text((cx, cy), 'CM', font=F(800, max(20, int(52 * s))), fill='white', anchor='mm')
        m = Image.new('L', (BW, BH), 0); ImageDraw.Draw(m).rectangle((X0, Y0, X1, Y1), fill=255)
        l.putalpha(Image.composite(l.getchannel('A'), Image.new('L', (BW, BH), 0), m)); im.paste(l, (0, 0), l)
        # comentarios del cliente
        cm = [(1.4, '“Más grande el logo”'), (2.6, '“Un pelín más”'), (3.8, '“Que se vea desde lejos”'), (5.0, '“Perfecto. ¿Y el texto?”')]
        for ts, txt in cm:
            if ts <= t < ts + 1.15 or (ts == 5.0 and t >= ts):
                k = ease((t - ts) / .25); l2, lg2 = layer(); A = int(255 * k); yy = BH - 90
                lg2.rounded_rectangle((120, yy - 36, BW - 120, yy + 36), 18, fill=(255, 235, 59, A))
                lg2.text((BW // 2, yy), txt, font=F(700, 32), fill=(30, 30, 30, A), anchor='mm')
                im.paste(l2, (0, 0), l2)
        return im


# ------------------------------------------------------------------ x04. EL EXCEL DE LEADS BARATOS
class LeadsBaratos:
    POV = 'POV: abres el Excel de leads de la campaña que te dieron “a 1 € el lead”'
    DUR, PUNCH, FOCUS = 7.4, 5.6, (480, 820)
    ROWS = [('asdfgh', '666666666', 'a@a.com'), ('Mi casa', '123456789', 'no@tengo.es'),
            ('Pepito', '000000000', 'pepito@pepito'), ('JAJAJA', '999 99 99', 'hola'),
            ('.', '1', '.'), ('Info', 'no llamar', 'no.molestar@x.es')]
    SFX = ['pop@0.3'] + [f'tick@{0.9 + i * .6:.1f}' for i in range(6)] + ['boom@5.6']

    def draw(self, t):
        INK, LINE, HDR = (32, 33, 36), (212, 214, 218), (33, 115, 70)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 90), fill=HDR)
        g.text((40, 45), 'leads_campaña_barata.xlsx', font=F(700, 30), fill='white', anchor='lm')
        g.rectangle((0, 90, BW, 150), fill=(243, 243, 243))
        g.text((30, 120), 'fx', font=F(600, 26), fill=(120, 120, 120), anchor='lm')
        cols = [(70, 'Nombre'), (360, 'Teléfono'), (640, 'Email')]
        g.rectangle((0, 170, BW, 230), fill=(232, 240, 234))
        for x, n in cols: g.text((x, 200), n, font=F(700, 30), fill=INK, anchor='lm')
        for i in range(8): g.line([(0, 230 + i * 80), (BW, 230 + i * 80)], fill=LINE, width=2)
        for x in (340, 620): g.line([(x, 170), (x, 870)], fill=LINE, width=2)
        for i, row in enumerate(self.ROWS):
            ts = .9 + i * .6
            if t < ts: continue
            A = int(255 * ease((t - ts) / .25)); l, lg = layer(); yy = 270 + i * 80
            for (x, _), v in zip(cols, row):
                f = F(500, 28); vv = v if f.getlength(v) < 260 else v[:14] + '…'
                lg.text((x, yy), vv, font=f, fill=INK + (A,), anchor='lm')
            im.paste(l, (0, 0), l)
        if t >= 4.6:
            k = ease((t - 4.6) / .4); l, lg = layer(); A = int(255 * k)
            lg.rectangle((0, 780, BW, 860), fill=(252, 232, 230, A))
            lg.text((BW // 2, 820), 'Leads reales: 0', font=F(800, 44), fill=(200, 30, 30, A), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g)
        return im


# ------------------------------------------------------------------ x05. LA LLAMADA PERDIDA
class Perdida:
    POV = 'POV: llamas 4 veces al lead y te devuelve la llamada justo cuando entras en la ducha'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 280)
    SFX = ['pop@0.5', 'pop@1.2', 'pop@1.9', 'pop@2.6', 'tick@3.6', 'ding@4.4', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (240, 240, 245), (150, 150, 158), (44, 44, 48)
        im = Image.new('RGB', (BW, BH), (0, 0, 0)); g = ImageDraw.Draw(im)
        g.text((40, 40), 'Recientes', font=F(800, 54), fill=INK)
        g.text((BW - 40, 70), 'Editar', font=F(500, 32), fill=(10, 132, 255), anchor='rm')
        rows = [(0.5, 'Lead web (cocina)', 'Saliente · sin respuesta', '10:02'), (1.2, 'Lead web (cocina)', 'Saliente · sin respuesta', '12:15'),
                (1.9, 'Lead web (cocina)', 'Saliente · sin respuesta', '16:40'), (2.6, 'Lead web (cocina)', 'Saliente · sin respuesta', '19:05')]
        y = 150
        if t >= 4.4:
            rows = [(4.4, 'Lead web (cocina)', 'Llamada perdida · 1 tono', '21:37', True)] + rows
        for r in rows:
            ts, name, sub, hr = r[:4]; missed = len(r) > 4
            if t < ts: continue
            k = ease((t - ts) / .3); A = int(255 * k); l, lg = layer()
            lg.text((60, y + 20), name, font=F(700, 36), fill=((255, 69, 58) if missed else INK) + (A,))
            lg.text((60, y + 70), sub, font=F(500, 28), fill=MUT + (A,))
            lg.text((BW - 60, y + 42), hr, font=F(500, 30), fill=MUT + (A,), anchor='rm')
            lg.line([(60, y + 124), (BW, y + 124)], fill=LINE + (A,), width=2)
            im.paste(l, (0, 0), l); y += 130
        if 3.4 <= t < 4.4:
            k = ease((t - 3.4) / .3); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((200, 820, BW - 200, 900), 40, fill=(30, 30, 34, A))
            lg.text((BW // 2, 860), '21:36 · te metes a la ducha', font=F(600, 30), fill=(200, 200, 205, A), anchor='mm')
            im.paste(l, (0, 0), l)
        if t >= 4.4:
            banner(im, t, 4.4, 'Teléfono · ahora', 'Llamada perdida: Lead web (cocina)', t1=5.5, icol=(52, 199, 89), ich='T')
        if t >= 5.8:
            k = ease((t - 5.8) / .3); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((40, 284, BW - 40, 404), 24, fill=(20, 20, 22, A))
            lg.text((BW // 2, 325), 'Le devuelves la llamada', font=F(600, 28), fill=(200, 200, 205, A), anchor='mm')
            lg.text((BW // 2, 368), 'a los 3 min: APAGADO', font=F(800, 34), fill=(255, 120, 100, A), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


# ------------------------------------------------------------------ x06. LA RESEÑA
class Resena:
    POV = 'POV: pides reseña a 30 clientes contentos y la única que llega es de uno que nunca te compró'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (300, 660)
    SFX = ['pop@0.4', 'count:2.0@1.0', 'ding@3.6', 'pop@4.4', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (32, 33, 36), (95, 99, 104), (232, 234, 237)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.text((40, 40), 'Reformas del Arlanzón', font=F(700, 40), fill=INK)
        g.text((40, 100), 'Empresa de reformas · Burgos', font=F(500, 28), fill=MUT)
        g.text((40, 170), '4,9', font=F(800, 60), fill=INK); stars(g, 150, 185, 5, 34)
        g.text((380, 200), '(12 reseñas)', font=F(500, 28), fill=MUT, anchor='lm')
        g.line([(0, 270), (BW, 270)], fill=LINE, width=2)
        sent = int(30 * min(1, ease((t - 1.0) / 2.0))) if t >= 1 else 0
        g.rounded_rectangle((40, 300, BW - 40, 400), 18, fill=(232, 240, 254))
        g.text((70, 350), f'Enlace de reseña enviado a {sent} clientes', font=F(600, 30), fill=(26, 90, 200), anchor='lm')
        if t >= 3.6:
            k = ease((t - 3.6) / .35); l, lg = layer(); A = int(255 * k); yy = 440
            lg.rounded_rectangle((40, yy, BW - 40, yy + 380), 18, fill=(255, 255, 255, A), outline=LINE + (A,), width=2)
            lg.ellipse((70, yy + 30, 150, yy + 110), fill=(120, 120, 130, A))
            lg.text((110, yy + 70), 'U', font=F(700, 36), fill=(255, 255, 255, A), anchor='mm')
            lg.text((175, yy + 34), 'Usuario anónimo', font=F(700, 32), fill=INK + (A,))
            lg.text((175, yy + 80), 'Nueva · hace 1 min', font=F(500, 24), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
            if t >= 4.4:
                g2 = ImageDraw.Draw(im); stars(g2, 70, yy + 140, 1, 40)
                for j, s in enumerate(['“No he contratado nada con', 'ellos, pero no me gusta', 'el color del logo.”']):
                    g2.text((70, yy + 210 + j * 48), s, font=F(600, 32), fill=INK)
        tag(g)
        return im


# ------------------------------------------------------------------ x07. LA LLAMADA RÁPIDA (calendario)
class LlamadaRapida:
    POV = 'POV: el cliente te pide “una llamada rápida de 10 minutos, que solo es una duda”'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 700)
    SFX = ['pop@0.4', 'count:3.6@1.2', 'tick@3.2', 'tick@4.2', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (32, 33, 36), (112, 117, 122), (228, 230, 233)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.text((40, 36), 'Martes, 14', font=F(800, 44), fill=INK)
        g.text((BW - 40, 60), 'Calendario', font=F(500, 28), fill=MUT, anchor='rm')
        HY, HH = 150, 118   # 10:00 en y=150, 118 px por hora
        for i, h in enumerate(range(10, 17)):
            y = HY + i * HH; g.text((40, y), f'{h}:00', font=F(500, 26), fill=MUT, anchor='lm'); g.line([(140, y), (BW - 30, y)], fill=LINE, width=2)
        # llamada que se alarga
        end = 10 / 60 + (3.6 - 10 / 60) * ease((t - 1.2) / 4.0) if t >= 1.2 else 10 / 60
        a = ease((t - .4) / .3); l, lg = layer(); A = int(255 * a)
        y1 = HY + int(end * HH); red = end > 1
        lg.rounded_rectangle((160, HY + 2, BW - 40, max(HY + 60, y1)), 14, fill=((234, 67, 53) if red else (66, 133, 244)) + (A,))
        lg.text((190, HY + 30), '“Llamada rápida, 10 min”', font=F(700, 30), fill=(255, 255, 255, A), anchor='lm')
        mins = int(end * 60)
        if mins > 12: lg.text((190, min(y1 - 36, HY + 80)), f'Duración: {mins // 60} h {mins % 60:02d} min' if mins >= 60 else f'Duración: {mins} min', font=F(600, 26), fill=(255, 255, 255, A), anchor='lm')
        im.paste(l, (0, 0), l)
        # eventos que se van pisando
        evs = [(3.2, 1.0, 'Reunión con proveedor'), (4.2, 3.0, 'Comer')]
        for ts, st_, name in evs:
            yy = HY + int(st_ * HH); over = end >= st_
            col = (170, 172, 176) if over else (51, 168, 83)
            g.rounded_rectangle((200 if over else 160, yy + 4, BW - 40, yy + 60), 12, fill=col)
            g.text((230 if over else 190, yy + 32), name + (' (cancelado)' if over else ''), font=F(600, 26), fill='white', anchor='lm')
        if t >= 4.9:
            k = pop((t - 4.9) / .35); l, lg = layer(); w_, h_ = int(760 * k), int(120 * k); cx, cy = BW // 2, 700
            lg.rounded_rectangle((cx - w_ // 2, cy - h_ // 2, cx + w_ // 2, cy + h_ // 2), 24, fill=(20, 20, 22, 250))
            if k > .9: lg.text((cx, cy), '“Y ya la última duda…”', font=F(800, 36), fill=(255, 170, 130), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g)
        return im


# ------------------------------------------------------------------ x08. LA PRIMERA VENTA (pagos)
class PrimeraVenta:
    POV = 'POV: por fin entra la primera venta del lanzamiento y a los 4 minutos te llega esto'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (300, 380)
    SFX = ['ding@0.8', 'count:1.2@1.0', 'pop@2.4', 'tick@3.8', 'ding@4.4', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE, PUR = (26, 31, 54), (105, 115, 134), (227, 232, 238), (99, 91, 255)
        im = Image.new('RGB', (BW, BH), (246, 249, 252)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 100), fill='white'); g.line([(0, 100), (BW, 100)], fill=LINE, width=2)
        g.text((40, 50), 'Pagos · Resumen de hoy', font=F(700, 32), fill=INK, anchor='lm')
        g.rounded_rectangle((30, 130, BW - 30, 420), 18, fill='white', outline=LINE, width=2)
        g.text((64, 170), 'Ingresos de hoy', font=F(600, 28), fill=MUT)
        refunded = t >= 4.4
        v = 0 if t < 1.0 else 997 * min(1, ease((t - 1.0) / 1.0))
        if refunded: v = 0
        g.text((64, 220), eur(v), font=F(800, 90), fill=(200, 40, 50) if refunded else INK)
        if t >= 2.4 and not refunded:
            k = pop((t - 2.4) / .3); f = F(700, int(30 * k) or 1)
            g.rounded_rectangle((64, 340, 420, 392), 12, fill=(215, 247, 225)); g.text((242, 366), '¡PRIMERA VENTA!', font=f, fill=(20, 130, 60), anchor='mm')
        g.text((40, 470), 'Movimientos', font=F(700, 30), fill=INK)
        rows = [(0.8, 'Programa Arranca · Cliente nuevo', '+997,00 €', (20, 130, 60))]
        if refunded: rows.insert(0, (4.4, 'Reembolso: “no era lo que creía”', '−997,00 €', (200, 40, 50)))
        for i, (ts, name, amt, col) in enumerate(rows):
            if t < ts: continue
            A = int(255 * ease((t - ts) / .3)); l, lg = layer(); yy = 530 + i * 120
            lg.rounded_rectangle((30, yy, BW - 30, yy + 100), 14, fill=(255, 255, 255, A))
            nm = name if F(600, 26).getlength(name) < 600 else name[:36] + '…'
            lg.text((60, yy + 50), nm, font=F(600, 26), fill=INK + (A,), anchor='lm')
            lg.text((BW - 60, yy + 50), amt, font=F(800, 30), fill=col + (A,), anchor='rm')
            im.paste(l, (0, 0), l)
        if 3.8 <= t < 4.4:
            g.text((BW // 2, 900), 'ya estabas contándoselo a todo el mundo', font=F(600, 28), fill=MUT, anchor='mm')
        tag(g)
        return im


# ------------------------------------------------------------------ x09. 5 € AL DÍA (admin. de anuncios)
class CincoEuros:
    POV = 'POV: el cliente pone 5 € al día en anuncios y pregunta cuántos clientes le entran mañana'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (300, 800)
    SFX = ['typing:0.8@0.6', 'tick@1.6', 'ding@2.6', 'pop@4.0', 'boom@5.8']

    def draw(self, t):
        BG, INK, MUT, LINE, BLU = (242, 244, 247), (28, 30, 33), (101, 103, 107), (221, 223, 226), (8, 102, 255)
        im = Image.new('RGB', (BW, BH), BG); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill='white'); g.line([(0, 110), (BW, 110)], fill=LINE, width=2)
        g.text((40, 55), 'Presupuesto y calendario', font=F(700, 36), fill=INK, anchor='lm')
        g.rounded_rectangle((30, 140, BW - 30, 470), 18, fill='white', outline=LINE, width=2)
        g.text((64, 180), 'Presupuesto diario', font=F(600, 30), fill=MUT)
        full = '5,00'; n = int(len(full) * min(1, max(0, (t - .6) / .8)))
        g.rounded_rectangle((64, 230, BW - 64, 320), 12, fill='white', outline=BLU if t < 1.6 else LINE, width=3)
        g.text((94, 275), (full[:n] or '') + (' €' if n else ''), font=F(800, 46), fill=INK, anchor='lm')
        if t >= 1.6:
            g.rounded_rectangle((BW - 290, 380, BW - 64, 440), 12, fill=BLU)
            g.text((BW - 177, 410), 'Publicar', font=F(700, 28), fill='white', anchor='mm')
        if t >= 2.6:
            k = ease((t - 2.6) / .35); l, lg = layer(); A = int(255 * k); yy = 510
            lg.rounded_rectangle((30, yy, BW - 30, yy + 170), 18, fill=(255, 255, 255, A), outline=LINE + (A,), width=2)
            lg.text((64, yy + 30), 'Mensaje del cliente · ahora', font=F(500, 24), fill=MUT + (A,))
            lg.text((64, yy + 76), '“¿Mañana cuántos clientes me entran,', font=F(600, 30), fill=INK + (A,))
            lg.text((64, yy + 112), 'unos 50?”', font=F(600, 30), fill=INK + (A,))
            im.paste(l, (0, 0), l)
        if t >= 4.0:
            k = ease((t - 4.0) / .35); l, lg = layer(); A = int(255 * k); yy = 710
            lg.rounded_rectangle((30, yy, BW - 30, yy + 220), 18, fill=(255, 255, 255, A), outline=LINE + (A,), width=2)
            lg.text((64, yy + 34), 'Resultados diarios estimados', font=F(600, 28), fill=MUT + (A,))
            lg.text((64, yy + 90), 'Poco probable', font=F(800, 48), fill=(228, 30, 63, A))
            lg.text((64, yy + 158), 'Con este presupuesto la entrega será limitada', font=F(500, 24), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
        tag(g)
        return im


# ------------------------------------------------------------------ x10. EL AUDIO DE 7 MINUTOS (WhatsApp)
class AudioSiete(WAChat):
    POV = 'POV: le preguntas al cliente “¿te viene bien el martes?” y te manda un audio de 7 minutos'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 700)
    NAME, LETTER, HOUR = 'Cliente (reformas)', 'R', '17:4'
    FOCUS = (480, 700)
    MSGS = [(0.3, 'out', '¿Te viene bien el martes a las 10?'), (2.6, 'in', 'AUDIO:7:42')]
    TYPING = [(0.9, 2.5)]
    SFX = ['pop@0.3', 'typing:1.6@0.9', 'pop@2.6', 'count:2.0@3.2', 'boom@5.8']

    def status(self, t):
        if 0.9 <= t < 2.5: return 'grabando audio...', (0, 168, 132)
        return 'en línea', WA_GREY

    def draw(self, t):
        im, g = self.base(t); y = self.bubbles(im, t)
        if t >= 3.2:
            l, lg = layer(); k = min(1, (t - 3.2) / 2.0)
            lg.rounded_rectangle((36, y + 20, BW - 36, y + 60), 20, fill=(24, 34, 40, 255))
            lg.rounded_rectangle((36, y + 20, 36 + int((BW - 72) * k * .06 + 40), y + 60), 20, fill=(0, 168, 132, 255))
            lg.text((BW // 2, y + 40), f'escuchando… 0:{int(k * 25):02d} de 7:42', font=F(600, 24), fill=(200, 210, 215, 255), anchor='mm')
            im.paste(l, (0, 0), l)
        self.footer(g)
        card(im, t, 5.3, 'Resumen del audio', '“Sí”', 'minuto 7:38', cy=740, ch=280, big_size=110, col=(255, 170, 130))
        return im


# ------------------------------------------------------------------ x11. VIERNES 19:58 (correo)
class Viernes:
    POV = 'POV: viernes a las 19:58 y entra un correo del cliente con “URGENTE” en el asunto'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 760)
    SFX = ['tick@0.4', 'ding@1.2', 'pop@2.6', 'typing:1.6@2.9', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (32, 33, 36), (95, 99, 104), (232, 234, 237)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 110), fill=(246, 248, 252))
        g.text((40, 55), 'Viernes · 19:58', font=F(700, 34), fill=INK, anchor='lm')
        g.text((BW - 40, 55), 'cerrando portátil…', font=F(500, 26), fill=MUT, anchor='rm')
        mails = [('Tú', 'Enviado: “¡Buen finde a todos!”')]
        y = 150
        if t >= 1.2:
            k = ease((t - 1.2) / .35)
            g.rectangle((0, y - 10, BW, y + 110), fill=(253, 236, 234))
            g.ellipse((40, y + 4, 110, y + 74), fill=(217, 48, 37)); g.text((75, y + 39), 'C', font=F(700, 32), fill='white', anchor='mm')
            g.text((136, y), 'Cliente', font=F(800, 30), fill=INK)
            g.text((BW - 40, y + 4), '19:58', font=F(700, 24), fill=INK, anchor='ra')
            g.text((136, y + 46), 'URGENTE!!! cambio de todo', font=F(800, 28), fill=(200, 30, 30))
            y += 124
        for name, sub in mails:
            g.ellipse((40, y + 4, 110, y + 74), fill=(189, 193, 198)); g.text((75, y + 39), 'T', font=F(700, 32), fill='white', anchor='mm')
            g.text((136, y), name, font=F(500, 30), fill=INK); g.text((136, y + 46), sub, font=F(500, 26), fill=MUT)
            g.line([(136, y + 108), (BW, y + 108)], fill=LINE, width=2)
        if t >= 2.6:
            k = ease((t - 2.6) / .35); l, lg = layer(); A = int(255 * k); yy = 420
            lg.rounded_rectangle((30, yy, BW - 30, BH - 40), 18, fill=(250, 250, 251, A), outline=LINE + (A,), width=2)
            body = ['Hola!! Lo he estado pensando', 'y mejor cambiamos los colores,', 'el texto, las fotos y la oferta.', '', 'Lo necesito para el lunes a', 'primera hora. Gracias!!']
            n = int(sum(len(s) for s in body) * min(1, (t - 2.9) / 1.6)) if t >= 2.9 else 0
            for j, s in enumerate(body):
                vis = s[:max(0, n)]; n -= len(s)
                lg.text((70, yy + 40 + j * 54), vis, font=F(600, 32), fill=INK + (A,))
            lg.text((70, yy + 380), 'Enviado desde mi móvil', font=F(500, 24), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
        if t >= 5.0:
            k = pop((t - 5.0) / .35); l, lg = layer(); cx, cy = BW // 2, 850; w_, h_ = int(460 * k), int(150 * k)
            lg.rounded_rectangle((cx - w_ // 2, cy - h_ // 2, cx + w_ // 2, cy + h_ // 2), 22, fill=(20, 20, 22, 250))
            if k > .9:
                lg.text((cx, cy - 36), 'Tu fin de semana:', font=F(600, 30), fill=GRY, anchor='mm')
                lg.text((cx, cy + 22), 'CANCELADO', font=F(800, 52), fill=RED, anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g)
        return im


# ------------------------------------------------------------------ x12. LEADS DE MADRUGADA (notificaciones)
class Madrugada:
    POV = 'POV: la campaña te trae leads a las 3 de la mañana y tú les contestas a las 11'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (380, 800)
    SFX = ['pop@0.6', 'pop@1.2', 'pop@1.8', 'tick@2.8', 'count:1.0@3.0', 'ding@4.6', 'boom@5.8']

    def draw(self, t):
        night = t < 2.8
        im = Image.new('RGB', (BW, BH), (8, 10, 24) if night else (120, 170, 220)); g = ImageDraw.Draw(im)
        if night:
            hh = '03:12'
        else:
            k = min(1, (t - 2.8) / 1.2); m = int(3 * 60 + 12 + k * (11 * 60 - 3 * 60 - 12)); hh = f'{m // 60:02d}:{m % 60:02d}'
        g.text((BW // 2, 150), hh, font=F(800, 150), fill='white', anchor='mm')
        g.text((BW // 2, 270), 'domingo', font=F(500, 34), fill=(210, 215, 230), anchor='mm')
        notifs = [(0.6, 'Nuevo lead: Presupuesto baño'), (1.2, 'Nuevo lead: Reforma integral'), (1.8, 'Nuevo lead: Cocina completa')]
        for i, (ts, txt) in enumerate(notifs):
            if t < ts: continue
            k = ease((t - ts) / .3); A = int(255 * k); l, lg = layer(); yy = 340 + i * 132
            lg.rounded_rectangle((36, yy, BW - 36, yy + 116), 26, fill=(40, 40, 46, int(230 * k)))
            lg.rounded_rectangle((64, yy + 28, 124, yy + 88), 16, fill=(8, 102, 255, A)); lg.text((94, yy + 58), 'L', font=F(800, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((150, yy + 22), 'Formulario de anuncios · 03:1' + str(i), font=F(500, 22), fill=(180, 180, 186, A))
            lg.text((150, yy + 56), txt, font=F(700, 29), fill=(255, 255, 255, A))
            im.paste(l, (0, 0), l)
        if not night and t < 4.6:
            g.text((BW // 2, 800), 'desayuno, café, correo…', font=F(600, 32), fill='white', anchor='mm')
        if t >= 4.6:
            k = ease((t - 4.6) / .35); l, lg = layer(); A = int(255 * k); yy = 760
            lg.rounded_rectangle((36, yy, BW - 36, yy + 170), 26, fill=(255, 255, 255, int(245 * k)))
            lg.rounded_rectangle((64, yy + 30, 124, yy + 90), 16, fill=(37, 211, 102, A)); lg.text((94, yy + 60), 'W', font=F(800, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((150, yy + 24), 'Lead: Cocina completa · ahora', font=F(500, 24), fill=(100, 100, 106, A))
            lg.text((150, yy + 62), '“Gracias, ya lo he contratado', font=F(700, 30), fill=(30, 30, 30, A))
            lg.text((150, yy + 104), 'con otra que me llamó antes”', font=F(700, 30), fill=(30, 30, 30, A))
            im.paste(l, (0, 0), l)
        tag(g, dark=True)
        return im


# ------------------------------------------------------------------ x13. LAS SUSCRIPCIONES (banco)
class Suscripciones:
    POV = 'POV: revisas el banco y pagas 8 herramientas de marketing que no has abierto nunca'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 880)
    ITEMS = ['Programa de email marketing', 'CRM (plan Pro)', 'Programador de redes', 'Banco de fotos premium',
             'Curso “Vende en 7 días”', 'Herramienta de SEO', 'Constructor de webs', 'Plantillas de diseño']
    SFX = ['pop@0.3'] + [f'tick@{0.7 + i * .45:.2f}' for i in range(8)] + ['boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (25, 30, 40), (110, 116, 126), (230, 232, 236)
        im = Image.new('RGB', (BW, BH), (248, 249, 251)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 100), fill=(0, 72, 130))
        g.text((40, 50), 'Tu banco · Movimientos', font=F(700, 32), fill='white', anchor='lm')
        g.text((BW - 40, 50), 'Este mes', font=F(500, 26), fill=(200, 220, 240), anchor='rm')
        prices = [49, 79, 29, 25, 37, 99, 19, 12]
        for i, (name, p) in enumerate(zip(self.ITEMS, prices)):
            ts = .7 + i * .45
            if t < ts: continue
            A = int(255 * ease((t - ts) / .25)); l, lg = layer(); yy = 120 + i * 82
            lg.text((40, yy + 22), name, font=F(600, 29), fill=INK + (A,))
            lg.text((40, yy + 58), 'Último acceso: nunca', font=F(500, 22), fill=(200, 60, 55, A))
            lg.text((BW - 40, yy + 38), f'−{p},00 €', font=F(700, 30), fill=INK + (A,), anchor='rm')
            lg.line([(40, yy + 80), (BW - 40, yy + 80)], fill=LINE + (A,), width=2)
            im.paste(l, (0, 0), l)
        if t >= 4.6:
            k = ease((t - 4.6) / .35); l, lg = layer(); A = int(255 * k)
            lg.rectangle((0, 800, BW, BH), fill=(255, 238, 236, A))
            lg.text((BW // 2, 860), '−349 € al mes', font=F(800, 50), fill=(200, 40, 40, A), anchor='mm')
            lg.text((BW // 2, 930), 'Clientes que te han traído: 0', font=F(700, 28), fill=INK + (A,), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


# ------------------------------------------------------------------ x14. EL CRM VACÍO
class CrmVacio:
    POV = 'POV: pagaste el CRM más completo del mercado y el único contacto eres tú haciendo la prueba'
    DUR, PUNCH, FOCUS = 7.4, 5.6, (260, 400)
    SFX = ['pop@0.4', 'pop@0.8', 'pop@1.2', 'pop@1.6', 'tick@2.4', 'count:1.8@2.6', 'boom@5.6']

    def draw(self, t):
        INK, MUT, LINE = (30, 34, 40), (115, 120, 128), (225, 228, 233)
        im = Image.new('RGB', (BW, BH), (241, 243, 246)); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 100), fill=(255, 255, 255)); g.line([(0, 100), (BW, 100)], fill=LINE, width=2)
        g.text((40, 50), 'Embudo de ventas', font=F(800, 34), fill=INK, anchor='lm')
        g.text((BW - 40, 50), 'Plan Enterprise', font=F(600, 24), fill=(125, 42, 232), anchor='rm')
        cols = ['Nuevo', 'Contactado', 'Propuesta', 'Ganado']
        cw = (BW - 50) // 4
        for i, c in enumerate(cols):
            if t < .4 + i * .4: continue
            x0 = 10 + i * (cw + 10)
            g.rounded_rectangle((x0, 130, x0 + cw - 4, 900), 14, fill=(230, 233, 238))
            g.text((x0 + 16, 160), c, font=F(700, 26), fill=INK, anchor='lm')
            g.text((x0 + cw - 20, 160), '1' if i == 0 else '0', font=F(700, 24), fill=MUT, anchor='rm')
        if t >= 2.4:
            k = ease((t - 2.4) / .3); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((20, 200, 10 + cw - 14, 400), 12, fill=(255, 255, 255, A), outline=LINE + (A,), width=2)
            lg.text((36, 230), 'Prueba', font=F(700, 26), fill=INK + (A,))
            lg.text((36, 270), 'Yo mismo', font=F(600, 24), fill=MUT + (A,))
            lg.text((36, 310), 'prueba@', font=F(500, 22), fill=MUT + (A,))
            lg.text((36, 345), 'prueba.com', font=F(500, 22), fill=MUT + (A,))
            im.paste(l, (0, 0), l)
        # contador de automatizaciones configuradas
        if t >= 2.6:
            n = int(47 * min(1, ease((t - 2.6) / 1.8)))
            g.rounded_rectangle((20, 440, 500, 640), 18, fill='white', outline=LINE, width=2)
            g.text((46, 470), 'Automatizaciones', font=F(600, 26), fill=MUT)
            g.text((46, 510), str(n), font=F(800, 72), fill=INK)
            g.text((180, 550), 'para 1 contacto', font=F(700, 30), fill=(200, 60, 55))
        tag(g)
        return im


# ------------------------------------------------------------------ x15. EL PLAN DEL DOMINGO (Excel)
class PlanDomingo:
    POV = 'POV: el plan de ventas del año que hiciste en Excel un domingo por la noche'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 880)
    MONTHS = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio']
    SFX = ['pop@0.3'] + [f'tick@{0.8 + i * .45:.2f}' for i in range(7)] + ['pop@4.4', 'boom@5.8']

    def draw(self, t):
        INK, LINE, HDR = (32, 33, 36), (212, 214, 218), (33, 115, 70)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.rectangle((0, 0, BW, 90), fill=HDR)
        g.text((40, 45), 'plan_ventas_2026_ESTE_SÍ.xlsx', font=F(700, 30), fill='white', anchor='lm')
        g.rectangle((0, 110, BW, 170), fill=(232, 240, 234))
        g.text((60, 140), 'Mes', font=F(700, 30), fill=INK, anchor='lm'); g.text((480, 140), 'Ventas previstas', font=F(700, 30), fill=INK, anchor='lm')
        g.line([(440, 110), (440, 790)], fill=LINE, width=2)
        for i, m in enumerate(self.MONTHS):
            ts = .8 + i * .45; yy = 170 + i * 88
            g.line([(0, yy + 88), (BW, yy + 88)], fill=LINE, width=2)
            if t < ts: continue
            v = 5 * 2 ** i; A = int(255 * ease((t - ts) / .25)); l, lg = layer()
            lg.text((60, yy + 44), m, font=F(500, 30), fill=INK + (A,), anchor='lm')
            lg.text((480, yy + 44), f'{v} clientes', font=F(800 if i > 4 else 600, 32), fill=((34, 139, 84) if i > 3 else INK) + (A,), anchor='lm')
            im.paste(l, (0, 0), l)
        if t >= 4.4:
            k = ease((t - 4.4) / .35); l, lg = layer(); A = int(255 * k)
            lg.rectangle((0, 810, BW, 950), fill=(252, 232, 230, A))
            lg.text((BW // 2, 845), 'Enero (real):', font=F(600, 28), fill=(160, 30, 30, A), anchor='mm')
            lg.text((BW // 2, 905), '1 cliente (tu tío)', font=F(800, 44), fill=(200, 30, 30, A), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g, y=BH - 24)
        return im


# ------------------------------------------------------------------ x16. EL LEAD QUE TE VENDE (llamada entrante)
class LeadVende:
    POV = 'POV: por fin te llama un lead de la campaña… y es para venderte a ti una web nueva'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 750)
    SFX = ['ding@0.3', 'ding@1.0', 'ding@1.7', 'pop@2.4', 'typing:2.2@2.8', 'pop@5.0', 'boom@5.8']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (24, 28, 36)); g = ImageDraw.Draw(im)
        for yy in range(BH):
            c = int(24 + 30 * yy / BH); g.line([(0, yy), (BW, yy)], fill=(c, c + 6, c + 20))
        answered = t >= 2.4
        g.text((BW // 2, 90), 'en llamada 00:' + f'{int(max(0, t - 2.4)):02d}' if answered else 'llamada entrante…', font=F(500, 32), fill=(200, 205, 215), anchor='mm')
        r = 90 + (0 if answered else int(10 * abs(math.sin(t * 5))))
        g.ellipse((BW // 2 - r, 250 - r, BW // 2 + r, 250 + r), fill=(90, 100, 118))
        g.text((BW // 2, 250), 'L', font=F(800, 80), fill='white', anchor='mm')
        g.text((BW // 2, 400), 'Lead campaña reformas', font=F(700, 44), fill='white', anchor='mm')
        if not answered:
            for x, col, lab in ((250, (255, 59, 48), 'Rechazar'), (710, (52, 199, 89), 'Aceptar')):
                g.ellipse((x - 70, 780, x + 70, 920), fill=col); g.text((x, 950), lab, font=F(500, 26), fill='white', anchor='mm')
        else:
            lines = ['“Hola, ¿hablo con el responsable?', 'Le llamo porque he visto su', 'anuncio y su web se puede mejorar.', '¿Tiene 5 minutos?”']
            n = int(sum(len(s) for s in lines) * min(1, (t - 2.8) / 2.6)) if t >= 2.8 else 0
            l, lg = layer(); lg.rounded_rectangle((40, 500, BW - 40, 800), 22, fill=(255, 255, 255, 30))
            for j, s in enumerate(lines):
                lg.text((80, 540 + j * 60), s[:max(0, n)], font=F(600, 34), fill=(255, 255, 255, 255)); n -= len(s)
            im.paste(l, (0, 0), l)
            if t < 5.0: g.ellipse((BW // 2 - 70, 840, BW // 2 + 70, 980), fill=(255, 59, 48))
            else:
                k = pop((t - 5.0) / .35); l2, lg2 = layer(); cx, cy = BW // 2, 885; w_, h_ = int(460 * k), int(150 * k)
                lg2.rounded_rectangle((cx - w_ // 2, cy - h_ // 2, cx + w_ // 2, cy + h_ // 2), 22, fill=(12, 12, 14, 250))
                if k > .9:
                    lg2.text((cx, cy - 34), 'Único lead de la semana:', font=F(600, 28), fill=GRY, anchor='mm')
                    lg2.text((cx, cy + 22), 'un comercial', font=F(800, 46), fill=RED, anchor='mm')
                im.paste(l2, (0, 0), l2)
        return im


# ------------------------------------------------------------------ x17. "PRECIO?" (comentarios)
class Precio:
    POV = 'POV: tu anuncio tiene 64 comentarios diciendo “precio?” y cuando lo mandas nadie contesta'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 820)
    COMS = [('reformas_fan_22', 'precio?'), ('mari.burgos', 'Precio'), ('jlopez_88', 'info'),
            ('la_casa_de_ana', 'precio porfa'), ('usuario_31842', 'cuanto'), ('pilar.deco', 'PRECIO???')]
    SFX = ['pop@0.3'] + [f'pop@{0.8 + i * .4:.1f}' for i in range(6)] + ['typing:0.6@3.6', 'tick@4.4', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (20, 20, 22), (120, 122, 126), (232, 234, 236)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.text((BW // 2, 50), 'Comentarios (64)', font=F(700, 34), fill=INK, anchor='mm')
        g.line([(0, 100), (BW, 100)], fill=LINE, width=2)
        for i, (u, c) in enumerate(self.COMS):
            ts = .8 + i * .4
            if t < ts: continue
            A = int(255 * ease((t - ts) / .25)); l, lg = layer(); yy = 130 + i * 96
            lg.ellipse((40, yy, 104, yy + 64), fill=(200 - i * 15, 180, 150 + i * 10, A))
            lg.text((126, yy + 4), u, font=F(700, 26), fill=INK + (A,))
            lg.text((126, yy + 36), c, font=F(500, 30), fill=INK + (A,))
            im.paste(l, (0, 0), l)
        if t >= 3.6:
            k = ease((t - 3.6) / .3); l, lg = layer(); A = int(255 * k); yy = 720
            lg.rectangle((0, yy - 10, BW, BH), fill=(250, 250, 250, A))
            lg.text((40, yy + 10), 'Tú respondiste a los 64:', font=F(600, 26), fill=MUT + (A,))
            lg.text((40, yy + 50), '“¡Te lo mando por privado!”', font=F(700, 32), fill=INK + (A,))
            im.paste(l, (0, 0), l)
        if t >= 4.4:
            k = ease((t - 4.4) / .3); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((40, 830, BW - 40, 950), 20, fill=(20, 20, 22, A))
            lg.text((BW // 2, 870), 'Mensajes directos', font=F(600, 26), fill=GRY + (A,), anchor='mm')
            lg.text((BW // 2, 915), '64 vistos · 0 respuestas', font=F(800, 32), fill=RED + (A,), anchor='mm')
            im.paste(l, (0, 0), l)
        return im


# ------------------------------------------------------------------ x18. EL FORMULARIO ETERNO
class FormEterno:
    POV = 'POV: te quejas de que no entran leads y tu formulario tiene 23 preguntas'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 520)
    QS = [(0.4, 'Nombre y apellidos'), (1.3, 'DNI / CIF'), (2.2, '¿Cómo nos conoció? (mín. 200 caracteres)'), (3.1, 'Facturación de los últimos 3 años')]
    SFX = ['pop@0.4', 'pop@1.3', 'pop@2.2', 'pop@3.1', 'tick@4.2', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE, BLU = (30, 34, 40), (115, 120, 128), (220, 224, 230), (26, 115, 232)
        im = Image.new('RGB', (BW, BH), (243, 245, 248)); g = ImageDraw.Draw(im)
        g.rounded_rectangle((30, 30, BW - 30, BH - 30), 22, fill='white')
        g.text((70, 80), 'Pide tu presupuesto gratis', font=F(800, 40), fill=INK)
        cur = sum(1 for ts, _ in self.QS if t >= ts)
        g.text((70, 150), f'Pregunta {cur} de 23', font=F(600, 28), fill=MUT)
        g.rounded_rectangle((70, 196, BW - 70, 212), 8, fill=(230, 233, 238))
        g.rounded_rectangle((70, 196, 70 + int((BW - 140) * cur / 23), 212), 8, fill=BLU)
        for i, (ts, q) in enumerate(self.QS):
            if t < ts: continue
            A = int(255 * ease((t - ts) / .3)); l, lg = layer(); yy = 250 + i * 140
            lg.text((70, yy), q, font=F(700, 29), fill=INK + (A,))
            lg.rounded_rectangle((70, yy + 44, BW - 70, yy + 110), 12, outline=LINE + (A,), width=3)
            im.paste(l, (0, 0), l)
        if t >= 4.2:
            k = ease((t - 4.2) / .35); l, lg = layer(); A = int(255 * k)
            lg.rectangle((30, 250, BW - 30, BH - 30), fill=(255, 255, 255, int(235 * k)))
            lg.text((BW // 2, 470), 'El usuario ha cerrado', font=F(800, 40), fill=(200, 40, 50, A), anchor='mm')
            lg.text((BW // 2, 525), 'la página', font=F(800, 40), fill=(200, 40, 50, A), anchor='mm')
            lg.text((BW // 2, 585), 'en la pregunta 4', font=F(600, 32), fill=MUT + (A,), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g, y=BH - 60, x=BW - 60)
        return im


# ------------------------------------------------------------------ x19. QUIÉN VE TUS HISTORIAS
class Espectadores:
    POV = 'POV: miras quién ha visto tu historia y la mitad son tus competidores'
    DUR, PUNCH, FOCUS = 7.4, 5.6, (480, 830)
    USERS = [('reformas.la.competencia', 'R'), ('otra_empresa_de_cocinas', 'O'), ('tu.madre', 'T'),
             ('reformas.la.competencia.2', 'R'), ('el_de_la_nave_de_al_lado', 'E'), ('la.competencia.otra.vez', 'L')]
    SFX = ['pop@0.3', 'count:0.8@0.4'] + [f'tick@{1.0 + i * .5:.1f}' for i in range(6)] + ['boom@5.6']

    def draw(self, t):
        im = Image.new('RGB', (BW, BH), (18, 18, 20)); g = ImageDraw.Draw(im)
        v = int(41 * min(1, ease((t - .4) / .8)))
        g.text((40, 50), f'{v} visualizaciones', font=F(700, 36), fill='white', anchor='lm')
        g.line([(0, 110), (BW, 110)], fill=(50, 50, 55), width=2)
        for i, (u, c) in enumerate(self.USERS):
            ts = 1.0 + i * .5
            if t < ts: continue
            A = int(255 * ease((t - ts) / .25)); l, lg = layer(); yy = 140 + i * 100
            comp = u != 'tu.madre'
            lg.ellipse((40, yy, 110, yy + 70), outline=(255, 106, 26, A), width=4)
            lg.text((75, yy + 35), c, font=F(700, 30), fill=(255, 255, 255, A), anchor='mm')
            lg.text((135, yy + 35), u, font=F(600, 30), fill=(240, 240, 245, A), anchor='lm')
            if comp: lg.text((BW - 40, yy + 35), 'competencia', font=F(600, 22), fill=(255, 120, 100, A), anchor='rm')
            im.paste(l, (0, 0), l)
        if t >= 4.6:
            k = ease((t - 4.6) / .3); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((40, 780, BW - 40, 900), 22, fill=(40, 40, 44, A))
            lg.text((BW // 2, 820), 'Clientes que la han visto: 0', font=F(800, 28), fill=RED + (A,), anchor='mm')
            lg.text((BW // 2, 862), '(pero mañana te copian)', font=F(600, 24), fill=GRY + (A,), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g, dark=True)
        return im


# ------------------------------------------------------------------ x20. EL PRIMER ANUNCIO (actividad)
class PrimerAnuncio:
    POV = 'POV: publicas tu primer anuncio y todas las interacciones son de tu familia'
    DUR, PUNCH, FOCUS = 7.6, 5.8, (480, 830)
    ACT = [(0.6, 'A mamá le gustó tu publicación.'), (1.3, 'mamá comentó: “¡Qué bien te ha quedado!”'),
           (2.0, 'A tu tía le gustó tu publicación.'), (2.7, 'tu tía comentó: “¿Esto es lo tuyo?”'),
           (3.4, 'tu primo compartió tu publicación.'), (4.1, 'mamá comentó otra vez: “Guapo”')]
    SFX = [f'pop@{a}' for a, _ in ACT] + ['tick@4.8', 'boom@5.8']

    def draw(self, t):
        INK, MUT, LINE = (20, 20, 22), (120, 122, 126), (232, 234, 236)
        im = Image.new('RGB', (BW, BH), 'white'); g = ImageDraw.Draw(im)
        g.text((40, 50), 'Notificaciones', font=F(800, 40), fill=INK, anchor='lm')
        g.line([(0, 100), (BW, 100)], fill=LINE, width=2)
        g.text((40, 130), 'Hoy', font=F(700, 28), fill=INK)
        for i, (ts, txt) in enumerate(self.ACT):
            if t < ts: continue
            A = int(255 * ease((t - ts) / .25)); l, lg = layer(); yy = 190 + i * 96
            lg.ellipse((40, yy, 104, yy + 64), fill=(255, 190, 200, A) if 'mamá' in txt else (190, 210, 255, A))
            ls = wrap(txt, F(500, 28), 780)
            for j, s in enumerate(ls[:2]): lg.text((126, yy + 4 + j * 34), s, font=F(500, 28), fill=INK + (A,))
            im.paste(l, (0, 0), l)
        if t >= 4.8:
            k = ease((t - 4.8) / .3); l, lg = layer(); A = int(255 * k)
            lg.rounded_rectangle((40, 780, BW - 40, 900), 22, fill=(20, 20, 22, A))
            lg.text((BW // 2, 815), 'Mensajes de clientes', font=F(600, 26), fill=GRY + (A,), anchor='mm')
            lg.text((BW // 2, 860), '0 (mamá no cuenta)', font=F(800, 38), fill=RED + (A,), anchor='mm')
            im.paste(l, (0, 0), l)
        tag(g)
        return im


NEW = {'x01-ya-le-llame': YaLeLlame, 'x02-web-2014': Web2014, 'x03-logo-grande': LogoGrande,
       'x04-leads-baratos': LeadsBaratos, 'x05-llamada-perdida': Perdida, 'x06-resena': Resena,
       'x07-llamada-rapida': LlamadaRapida, 'x08-primera-venta': PrimeraVenta, 'x09-cinco-euros': CincoEuros,
       'x10-audio-7-min': AudioSiete, 'x11-viernes-urgente': Viernes, 'x12-leads-madrugada': Madrugada,
       'x13-suscripciones': Suscripciones, 'x14-crm-vacio': CrmVacio, 'x15-plan-domingo': PlanDomingo,
       'x16-lead-que-vende': LeadVende, 'x17-precio': Precio, 'x18-formulario-eterno': FormEterno,
       'x19-espectadores': Espectadores, 'x20-primer-anuncio': PrimerAnuncio}
