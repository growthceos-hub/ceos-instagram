#!/usr/bin/env python3
"""Graba c2.html a MP4 1080x1920 a 30 fps (lógica de toolkit/render.py)."""
import asyncio, os, shutil, subprocess, sys
sys.path.insert(0, '/home/user/ceos-instagram/toolkit')
import render  # fuentes embebidas y logo
FPS, DUR = 30, 18.0

async def main(src, out_dir):
    from playwright.async_api import async_playwright
    s = render.prep(src)
    fr = os.path.join(out_dir, '_frames'); shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.set_content(s, wait_until='load'); await pg.evaluate('document.fonts.ready')
        only = os.environ.get('ONLY')
        idx = [int(x) for x in only.split(',')] if only else range(int(FPS * DUR))
        for i in idx:
            await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause();a.currentTime={i * 1000 / FPS}}})')
            await pg.screenshot(path=f'{fr}/{i:04d}.jpg', type='jpeg', quality=92)
        await b.close()
    if os.environ.get('ONLY'): print('frames en', fr); return
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{fr}/%04d.jpg',
                    '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-shortest',
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-c:a', 'aac', '-movflags', '+faststart',
                    os.path.join(out_dir, 'c2.mp4')], check=True)
    shutil.copy(f'{fr}/0000.jpg', os.path.join(out_dir, 'c2-fotograma0.jpg'))
    shutil.rmtree(fr)

asyncio.run(main(sys.argv[1], sys.argv[2]))
