#!/usr/bin/env python3
"""Imprime las publicaciones pendientes de programar (subidas a GitHub y sin programar), con fecha y JSON listo."""
import json, os, subprocess, datetime as dt
import os as _o; R=_o.environ.get('REPO','/home/user/ceos-instagram'); F=_o.environ.get('FABRICA','/home/user/fabrica')
done=set(open(f'{F}/programados.txt').read().split()) if os.path.exists(f'{F}/programados.txt') else set()
sha=subprocess.check_output(['git','-C',R,'rev-parse','HEAD'],text=True).strip()
SLOT={'agencia':[('09:00',2,1),('15:00',2,2)],'webs':[('11:00',2,1),('17:30',2,2)],'ads':[('13:30',1,1)],'reels':[('19:30',1,1)],'metodo':[('21:30',1,1)]}
start=dt.date(2026,10,26)
def when(i):
    kind,n=i.rsplit('-',1); n=int(n)
    for hh,per,off in SLOT[kind]:
        if (n-off)%per==0: return start+dt.timedelta(days=(n-off)//per), hh
out=[]
for i in sorted(os.listdir(f'{R}/tiktok')):
    if i in done or not os.path.exists(f'{R}/tiktok/{i}/reel.mp4'): continue
    s=json.load(open(f'{R}/tiktok/{i}/spec.json')); t=s['tiktok']; d,hh=when(i)
    info={"autoPublish":True,"draft":False,"descendants":[],"firstCommentText":"","hasNotReadNotes":False,
      "media":[f"https://raw.githubusercontent.com/growthceos-hub/ceos-instagram/{sha}/tiktok/{i}/reel.mp4"],"mediaAltText":[],
      "providers":[{"network":"tiktok"}],"publicationDate":{"dateTime":f"{d}T{hh}:00","timezone":"Europe/Madrid"},
      "shortener":False,"smartLinkData":{"ids":[]},"text":t['text'],
      "tiktokData":{"disableComment":False,"disableDuet":False,"disableStitch":False,"privacyOption":"PUBLIC_TO_EVERYONE","commercialContentThirdParty":False,"commercialContentOwnBrand":True,"title":t['title'][:90],"autoAddMusic":False,"isAigc":True}}
    out.append((str(d)+hh,i,f"{d}T{hh}:00+01:00",json.dumps(info,ensure_ascii=False)))
for _,i,date,info in sorted(out): print(f"### {i} {date}\n{info}")
