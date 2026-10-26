#!/usr/bin/env python3
"""Imprime los posts del pack-01 de LinkedIn pendientes de programar en Metricool:
'### <id> <fecha>' + línea JSON para createScheduledPost (blogId 7288052, provider linkedin).
Uso desde la raíz del repo: python3 linkedin/lote_linkedin.py [AAAA-MM-DD de inicio]"""
import json, os, sys, subprocess, datetime as dt
P = 'linkedin/pack-01'
RAW = 'https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/main/' + P
hecho = set(open('linkedin/programados.txt').read().split()) if os.path.exists('linkedin/programados.txt') else set()
inicio = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else dt.date.today() + dt.timedelta(days=1)
dias, d = [], inicio
while len(dias) < 30:
    if d.weekday() < 5: dias.append(d)
    d += dt.timedelta(days=1)
for n, carpeta in enumerate(sorted(x for x in os.listdir(P) if x[:2].isdigit())):
    if carpeta in hecho: continue
    base = f'{P}/{carpeta}'
    fecha = f'{dias[n]}T13:00:00'
    info = {"autoPublish": True, "draft": False, "descendants": [], "firstCommentText": "", "hasNotReadNotes": False,
            "media": [], "mediaAltText": [], "providers": [{"network": "linkedin"}],
            "publicationDate": {"dateTime": fecha, "timezone": "Europe/Madrid"}, "shortener": False,
            "smartLinkData": {"ids": []}, "linkedinData": {"type": "post", "previewIncluded": False}}
    if os.path.exists(f'{base}/encuesta.json'):
        e = json.load(open(f'{base}/encuesta.json'))
        info['text'] = e['texto']
        info['linkedinData'] = {"type": "poll", "poll": {"question": e['pregunta'][:140], "options": [{"text": o[:30]} for o in e['opciones']], "settings": {"duration": "SEVEN_DAYS"}}}
    else:
        info['text'] = open(f'{base}/post.txt').read().strip()
        if os.path.isdir(f'{base}/paginas'):
            pags = sorted(os.listdir(f'{base}/paginas'), key=lambda s: int(s.split('-')[1].split('.')[0]))
            info['media'] = [f'{RAW}/{carpeta}/paginas/{p}' for p in pags]
            info['linkedinData'].update({"documentTitle": info['text'].split('\n')[0][:100], "publishImagesAsPDF": True})
        elif os.path.exists(f'{base}/imagen.png'):
            info['media'] = [f'{RAW}/{carpeta}/imagen.png']
    print(f'### {carpeta} {fecha}+01:00')
    print(json.dumps(info, ensure_ascii=False))
