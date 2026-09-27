#!/usr/bin/env python3
"""Renderiza un carrusel de 5 slides (.dc.html) a MP4 (4 s, 1080x1350) + JPG.

Uso: python3 toolkit/render.py <carpeta_con_slides> <carpeta_salida>
La carpeta de slides debe tener Main.dc.html, S2..S5.dc.html.
Requiere: pip install playwright && playwright install chromium; ffmpeg;
          npm i @fontsource/bricolage-grotesque @fontsource/instrument-sans
                @fontsource/instrument-serif @fontsource/jetbrains-mono  (en toolkit/)
"""
import asyncio, base64, os, re, shutil, subprocess, sys
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'node_modules/@fontsource/')
FPS, DUR = 30, 4.0
ORDER = [('Main', '01'), ('S2', '02'), ('S3', '03'), ('S4', '04'), ('S5', '05')]


def face(fam, path, w, st='normal'):
    b = base64.b64encode(open(D + path, 'rb').read()).decode()
    return "@font-face{font-family:'%s';src:url(data:font/woff2;base64,%s) format('woff2');font-weight:%s;font-style:%s}" % (fam, b, w, st)


FACES = ''.join(
    [face('Bricolage Grotesque', f'bricolage-grotesque/files/bricolage-grotesque-latin-{w}-normal.woff2', w) for w in (500, 700, 800)]
    + [face('Instrument Sans', f'instrument-sans/files/instrument-sans-latin-{w}-normal.woff2', w) for w in (400, 500, 600, 700)]
    + [face('JetBrains Mono', f'jetbrains-mono/files/jetbrains-mono-latin-{w}-normal.woff2', w) for w in (400, 500, 600)]
    + [face('Instrument Serif', 'instrument-serif/files/instrument-serif-latin-400-normal.woff2', 400),
       face('Instrument Serif', 'instrument-serif/files/instrument-serif-latin-400-italic.woff2', 400, 'italic')])
# Marca: BRAND=productions (variable de entorno) cambia nombre, @ y logo para @ceos.productions.
BRAND = os.environ.get('BRAND', 'growth')
_logo = os.path.join(HERE, 'brands', BRAND, 'logo.png')
if not os.path.exists(_logo):
    _logo = os.path.join(HERE, 'logo.png')
LOGO = 'data:image/png;base64,' + base64.b64encode(open(_logo, 'rb').read()).decode()


def prep(src):
    s = open(src).read()
    if BRAND == 'productions':
        s = s.replace('Ceos Growth', 'Ceos Productions').replace('@ceos.growth', '@ceos.productions')
        s = s.replace('#ceosgrowth', '#ceosproductions')
    s = s.replace('<script src="./support.js"></script>', '')
    s = re.sub(r'<script type="text/x-dc".*?</script>', '', s, flags=re.S)
    s = re.sub(r'<link href="https://fonts[^>]*>', '<style>' + FACES + '</style>', s)
    s = re.sub(r'/_blob/[0-9a-f]{32}', LOGO, s)
    for t in ('<x-dc>', '</x-dc>', '<helmet>', '</helmet>'):
        s = s.replace(t, '')
    return s


async def main(src_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        for name, num in ORDER:
            await pg.set_content(prep(os.path.join(src_dir, f'{name}.dc.html')), wait_until='load')
            await pg.evaluate('document.fonts.ready')
            fr = os.path.join(out_dir, f'_frames{num}')
            shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
            for i in range(int(FPS * DUR)):
                await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause();a.currentTime={i * 1000 / FPS}}})')
                await pg.screenshot(path=f'{fr}/{i:04d}.jpg', type='jpeg', quality=92)
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{fr}/%04d.jpg',
                            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart',
                            os.path.join(out_dir, f'{num}.mp4')], check=True)
            shutil.copy(f'{fr}/0100.jpg', os.path.join(out_dir, f'{num}.jpg'))
            shutil.rmtree(fr)
            print(num, 'ok')
        await b.close()
    lst = os.path.join(out_dir, '_l.txt')
    open(lst, 'w').write(''.join(f"file '{n}.mp4'\n" for _, n in ORDER))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy',
                    os.path.join(out_dir, 'video-completo.mp4')], check=True)
    os.remove(lst)


if __name__ == '__main__':
    asyncio.run(main(sys.argv[1], sys.argv[2]))
