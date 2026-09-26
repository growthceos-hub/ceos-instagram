#!/usr/bin/env python3
"""Renderiza una historia (1080x1920, 5 s) a MP4 + JPG.
Uso: python3 toolkit/render_story.py <Historia.dc.html> <carpeta_salida>
"""
import asyncio, os, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import prep  # noqa: E402
from playwright.async_api import async_playwright

FPS = 30
DUR = float(os.environ.get('DUR', '5'))


async def main(src, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.set_content(prep(src), wait_until='load')
        await pg.evaluate('document.fonts.ready')
        fr = os.path.join(out_dir, '_frames_story')
        shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
        for i in range(int(FPS * DUR)):
            await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause();a.currentTime={i * 1000 / FPS}}})')
            await pg.screenshot(path=f'{fr}/{i:04d}.jpg', type='jpeg', quality=92)
        await b.close()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{fr}/%04d.jpg',
                    '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest',
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-c:a', 'aac', '-movflags', '+faststart',
                    os.path.join(out_dir, os.environ.get('NAME', 'historia') + '.mp4')], check=True)
    shutil.copy(f'{fr}/{int(FPS*DUR)-30:04d}.jpg', os.path.join(out_dir, os.environ.get('NAME', 'historia') + '.jpg'))
    if not os.environ.get('KEEP'): shutil.rmtree(fr)
    print('historia ok')


if __name__ == '__main__':
    asyncio.run(main(sys.argv[1], sys.argv[2]))
