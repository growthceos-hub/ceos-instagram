#!/usr/bin/env python3
"""Construye un reel completo: spec JSON -> escenas -> efectos -> render -> transiciones -> música.

Uso (desde la raíz del repo):
  python3 toolkit/reels/build_reel.py reels/AAAA-MM-DD-N/spec.json reels/AAAA-MM-DD-N [SEMILLA_MUSICA]
Genera en la carpeta: src/R1..R5.dc.html, reel.mp4 y portada.jpg.
"""
import json, os, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TK = os.path.join(ROOT, 'toolkit')
XF = 0.35  # duración de cada transición


def run(cmd, env=None):
    subprocess.run(cmd, check=True, env={**os.environ, **(env or {})})


def main(spec, out, seed=0):
    src = os.path.join(out, 'src')
    shutil.rmtree(src, ignore_errors=True)
    run(['python3', os.path.join(TK, 'reels/gen_reel.py'), spec, src])
    files = sorted(f for f in os.listdir(src) if f.endswith('.dc.html'))
    run(['python3', os.path.join(TK, 'boost_story.py')] + [os.path.join(src, f) for f in files])
    durs = json.load(open(os.path.join(src, 'durs.json')))
    tmp = os.path.join(out, '_tmp')
    shutil.rmtree(tmp, ignore_errors=True)

    def render(i):
        run(['python3', os.path.join(TK, 'render_story.py'), os.path.join(src, files[i]), os.path.join(tmp, str(i))],
            env={'DUR': str(durs[i]), 'NAME': 'S'})
        return os.path.join(tmp, str(i), 'S.mp4')

    with ThreadPoolExecutor(5) as ex:
        clips = list(ex.map(render, range(len(files))))

    total = sum(durs) - XF * (len(durs) - 1)
    drop = durs[0] - XF
    wav = os.path.join(tmp, 'music.wav')
    run(['python3', os.path.join(TK, 'reels/music.py'), wav, f'{total:.2f}', f'{drop:.2f}', str(seed)])

    fc, prev, off = [], '0:v', 0.0
    for i in range(1, len(clips)):
        off += durs[i - 1] - XF
        lab = f'x{i}'
        fc.append(f'[{prev}][{i}:v]xfade=transition=zoomin:duration={XF}:offset={off:.2f}[{lab}]')
        prev = lab
    fc.append(f'[{prev}]format=yuv420p[v]')
    fc.append(f'[{len(clips)}:a]loudnorm=I=-13:TP=-1:LRA=9[au]')
    cmd = ['ffmpeg', '-v', 'error', '-y']
    for c in clips:
        cmd += ['-i', c]
    cmd += ['-i', wav, '-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[au]',
            '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-c:a', 'aac', '-b:a', '256k', '-ar', '44100',
            '-shortest', '-movflags', '+faststart', os.path.join(out, 'reel.mp4')]
    run(cmd)
    run(['ffmpeg', '-v', 'error', '-y', '-ss', '3', '-i', os.path.join(out, 'reel.mp4'), '-frames:v', '1', '-q:v', '3', os.path.join(out, 'portada.jpg')])
    # fotogramas de revisión (mitad de cada escena)
    t = 0.0
    for i, d in enumerate(durs):
        run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t + d * .8:.2f}', '-i', os.path.join(out, 'reel.mp4'), '-frames:v', '1', '-vf', 'scale=540:-1',
             os.path.join(tmp, f'check{i + 1}.jpg')])
        t += d - XF
    print('reel ok', os.path.join(out, 'reel.mp4'), f'{total:.1f}s', '· revisa', tmp + '/check*.jpg')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 0)
