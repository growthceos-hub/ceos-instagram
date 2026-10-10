#!/usr/bin/env python3
"""Maqueta el Kit Primera Campaña de Ceos Growth en PDF.

Uso (sin argumentos):  python3 build.py
Lee los .md de la carpeta superior (no los modifica), escribe los HTML
intermedios en pdf/src/ y los PDF A4 en pdf/.

Requisitos: python-markdown (pip install --break-system-packages markdown),
beautifulsoup4, pypdf, playwright (Chromium en /opt/pw-browsers) y pdftotext.
"""
import base64
import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from bs4 import BeautifulSoup, NavigableString
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

HERE = Path(__file__).resolve().parent
KIT = HERE.parent
SRC = HERE / "src"
REPO = KIT.parent.parent
LOGO = REPO / "toolkit" / "logo.png"
FONTS = REPO / "toolkit" / "node_modules" / "@fontsource"

VERSION = "v1 · octubre 2026"
COPY = "© Ceos Growth, S.L. — uso personal del comprador"

DOCS = [
    dict(md="guia.md", out="01-guia-primera-campana.pdf", short="Guía",
         toc_levels=("h2", "h3"), part_breaks=True, toc_title="Índice"),
    dict(md="guiones.md", out="02-30-guiones.pdf", short="30 guiones",
         toc_levels=("h2", "card"), toc_title="Índice de guiones", toc_cols=2,
         cover_note="Un guion por página: ábrelo en el móvil mientras grabas."),
    dict(md="plantillas-canva.md", out="03-plantillas.pdf", short="Plantillas",
         toc_levels=("h2",), toc_title="Índice", canva=True,
         cover_note="Los enlaces a las plantillas editables de Canva se añadirán en la próxima actualización del kit."),
    dict(md="bump-guiones-extra-whatsapp.md", out="extra-guiones-temporada-y-whatsapp.pdf",
         short="Pack extra", toc_levels=("h2", "card", "h3"), toc_title="Índice", toc_cols=2),
]

# ---------------------------------------------------------------- Markdown

LIST = re.compile(r"^([-*+]|\d+\.) ")


def norm_md(text):
    """Adapta Markdown estilo GitHub a python-markdown (listas sin línea en
    blanco previa, sublistas con 2-3 espacios). Solo en memoria."""
    out, prev = [], "blank"
    for ln in text.split("\n"):
        if not ln.strip():
            out.append(ln); prev = "blank"; continue
        m = re.match(r"^( +)(\S.*)$", ln)
        if m:
            body = m.group(2)
            if LIST.match(body):
                out.append("    " + body); prev = "nested"; continue
            if prev in ("nested", "item"):
                out.append("")
            out.append("    " + body); prev = "indented_text"; continue
        if LIST.match(ln):
            if prev in ("text", "indented_text"):
                out.append("")
            out.append(ln); prev = "item"; continue
        out.append(ln); prev = "text"
    return "\n".join(out)


def strip_num(t):
    return re.sub(r"^(Parte\s+)?\d+\.\s*", "", t).strip()


ROW_KEYS = [("gancho", "gancho"), ("cuerpo", "cuerpo"), ("cta", "cta"),
            ("en pantalla", "pantalla"), ("por qué", "porque"), ("ojo", "ojo")]


def is_card(h3):
    ul = h3.find_next_sibling()
    if not ul or ul.name != "ul":
        return False
    s = ul.find("strong")
    return bool(s and s.get_text().lower().startswith("gancho"))


def transform(doc, body_html):
    soup = BeautifulSoup(body_html, "html.parser")
    meta = {"title": "", "kicker": "", "sub": ""}

    h1 = soup.find("h1")
    if h1:
        meta["title"] = h1.get_text().strip(); h1.decompose()
    # Lo que va antes del primer <hr>: línea de marca y subtítulo corto
    first_hr = soup.find("hr")
    pre = []
    for el in list(soup.children):
        if el is first_hr:
            break
        if getattr(el, "name", None):
            pre.append(el)
    ps = [e for e in pre if e.name == "p"]
    for p in ps:
        if "Ceos Growth" in p.get_text() and len(p.get_text()) < 120:
            meta["kicker"] = p.get_text().strip(); p.decompose()
    rest = [e for e in pre if not getattr(e, "decomposed", False) and e.parent is not None]
    if len(rest) == 1 and rest[0].name == "p" and len(rest[0].get_text()) < 260:
        meta["sub"] = rest[0].get_text().strip(); rest[0].decompose()
    for hr in soup.find_all("hr"):
        hr.decompose()

    # EJEMPLO como etiqueta naranja (en negrita o en texto plano)
    for s in soup.find_all("strong"):
        if re.fullmatch(r"EJEMPLO:?", s.get_text().strip()):
            s.name = "span"; s["class"] = "tag"; s.string = "EJEMPLO"
    for tn in list(soup.find_all(string=re.compile(r"\bEJEMPLO\b"))):
        if tn.parent.name == "span" and "tag" in (tn.parent.get("class") or []):
            continue
        parts = re.split(r"\bEJEMPLO:?", str(tn))
        new = []
        for i, part in enumerate(parts):
            if i:
                t = soup.new_tag("span", attrs={"class": "tag"}); t.string = "EJEMPLO"
                new.append(t)
            if part:
                new.append(NavigableString(part))
        for n in new:
            tn.insert_before(n)
        tn.extract()
    # Cajas de ejemplo
    for p in list(soup.find_all("p")):
        kids = [k for k in p.contents if not (isinstance(k, NavigableString) and not k.strip())]
        if not kids:
            continue
        first_tag = kids[0]
        starts = getattr(first_tag, "name", None) == "span" and "tag" in first_tag.get("class", [])
        last = kids[-1]
        ends = getattr(last, "name", None) == "span" and "tag" in last.get("class", []) and not starts
        nxt = p.find_next_sibling()
        if starts and p.parent.name in ("[document]", None) or (starts and p.parent is soup):
            box = soup.new_tag("div", attrs={"class": "ejemplo"})
            p.insert_before(box); box.append(p.extract())
            if nxt and nxt.name in ("blockquote", "ul", "ol") and p.get_text().strip().endswith(":"):
                box.append(nxt.extract())
        elif ends and nxt and nxt.name in ("blockquote", "ul", "ol"):
            last.extract()
            box = soup.new_tag("div", attrs={"class": "ejemplo"})
            lab = soup.new_tag("p"); t = soup.new_tag("span", attrs={"class": "tag"}); t.string = "EJEMPLO"
            lab.append(t); box.append(lab)
            nxt.insert_before(box); box.append(nxt.extract())

    # Tarjetas de guion
    cur_h2 = ""
    for el in list(soup.children):
        if getattr(el, "name", None) == "h2":
            cur_h2 = strip_num(el.get_text())
        if getattr(el, "name", None) == "h3" and is_card(el):
            ul = el.find_next_sibling()
            card = soup.new_tag("section", attrs={"class": "card"})
            m = re.match(r"^([A-Z]\d+)\.\s*(.*)$", el.get_text().strip())
            code, ttl = (m.group(1), m.group(2)) if m else ("", el.get_text().strip())
            card["data-toc"] = f"{code} · {ttl}" if code else ttl
            card["data-kicker"] = cur_h2
            head = BeautifulSoup(
                f'<header><div class="kick">{html.escape(cur_h2)}</div>'
                f'<div class="ct">{"<span class=code>"+html.escape(code)+"</span>" if code else ""}'
                f'<h3>{html.escape(ttl)}</h3></div></header>', "html.parser")
            card.append(head)
            for li in ul.find_all("li", recursive=False):
                s = li.find("strong")
                lab = s.get_text().strip().rstrip(":") if s else ""
                key = "otro"
                for k, v in ROW_KEYS:
                    if lab.lower().startswith(k):
                        key = v; break
                if s:
                    s.extract()
                row = soup.new_tag("div", attrs={"class": f"row {key}"})
                l = soup.new_tag("div", attrs={"class": "lbl"}); l.string = lab
                t = soup.new_tag("div", attrs={"class": "txt"})
                for c in list(li.contents):
                    t.append(c.extract())
                if t.contents and isinstance(t.contents[0], NavigableString):
                    t.contents[0].replace_with(t.contents[0].lstrip())
                row.append(l); row.append(t); card.append(row)
            el.insert_before(card); el.decompose(); ul.decompose()

    # Encabezados de sector que solo agrupan tarjetas: se quitan (van en la tarjeta)
    for h2 in list(soup.find_all("h2")):
        sib, only_cards, n = h2.find_next_sibling(), True, 0
        while sib and sib.name != "h2":
            if not (sib.name == "section" and "card" in sib.get("class", [])):
                only_cards = False; break
            n += 1; sib = sib.find_next_sibling()
        if only_cards and n:
            h2["class"] = "group"

    # Mensajes de WhatsApp: <p><strong>título</strong></p> + <blockquote>
    for p in list(soup.find_all("p")):
        kids = [k for k in p.contents if not (isinstance(k, NavigableString) and not k.strip())]
        nxt = p.find_next_sibling()
        if len(kids) == 1 and getattr(kids[0], "name", None) == "strong" and nxt is not None and nxt.name == "blockquote":
            m = re.match(r"^(\d+)\.\s*(.*)$", kids[0].get_text().strip())
            num, ttl = (m.group(1), m.group(2)) if m else ("", kids[0].get_text().strip())
            box = soup.new_tag("div", attrs={"class": "msg"})
            hd = BeautifulSoup(f'<div class="mh"><span class="num">{num}</span><span>{html.escape(ttl)}</span></div>', "html.parser")
            box.append(hd)
            bub = soup.new_tag("div", attrs={"class": "bubble"})
            for c in list(nxt.contents):
                bub.append(c.extract())
            box.append(bub)
            p.insert_before(box); p.decompose(); nxt.decompose()

    # Plantillas: cada "N. Nombre" en su bloque, con hueco para el enlace de Canva
    if doc.get("canva"):
        for h2 in list(soup.find_all("h2")):
            m = re.match(r"^(\d+)\.\s*(.*)$", h2.get_text().strip())
            if not m:
                continue
            sec = soup.new_tag("section", attrs={"class": "tpl"})
            h2.insert_before(sec)
            sibs = []
            s = h2.find_next_sibling()
            while s and s.name != "h2":
                sibs.append(s); s = s.find_next_sibling()
            h2.clear()
            h2.append(BeautifulSoup(f'<span class="code">{m.group(1)}</span>{html.escape(m.group(2))}', "html.parser"))
            sec.append(h2.extract())
            for s in sibs:
                sec.append(s.extract())
            sec.append(BeautifulSoup(
                '<div class="canva"><div class="lbl">Plantilla en Canva</div>'
                '<div>4:5 (1080 × 1350) · 9:16 (1080 × 1920)</div>'
                '<div class="pending">Enlace: se añadirá en la próxima actualización del kit</div></div>',
                "html.parser"))
        # Aviso general al inicio
        first = soup.find(True)
        if first is not None:
            first.insert_before(BeautifulSoup(
                '<div class="notice"><strong>Enlaces de Canva:</strong> las plantillas editables '
                'se añadirán en la próxima actualización del kit. Cada plantilla tiene un hueco '
                'reservado para su enlace. Mientras tanto, con esta especificación puedes montarlas tú en Canva.</div>',
                "html.parser"))

    # Partes de la guía en página nueva
    if doc.get("part_breaks"):
        for h2 in soup.find_all("h2"):
            if h2.get_text().startswith("Parte") or h2.get_text().startswith("Resumen"):
                h2["class"] = (h2.get("class") or []) + ["newpage"]

    # Títulos nunca solos al pie: título + primer bloque juntos
    for h in list(soup.find_all(["h2", "h3"])):
        if h.find_parent("section", class_="card") or h.find_parent("header"):
            continue
        if "group" in (h.get("class") or []):
            continue
        nxt = h.find_next_sibling()
        if nxt is None or (nxt.name in ("h2", "h3", "section")):
            continue
        keep = soup.new_tag("div", attrs={"class": "keep"})
        if "newpage" in (h.get("class") or []):
            keep["class"] = "keep newpage"
        h.insert_before(keep)
        keep.append(h.extract())
        # Si lo siguiente es otra cabecera (h3 tras h2) se arrastra también
        nx = nxt
        keep.append(nx.extract())
        if nx.name in ("h3",):
            n2 = keep.find_next_sibling()
            if n2 is not None and n2.name not in ("h2", "h3", "section"):
                keep.append(n2.extract())

    # Índice
    toc = []
    i = 0
    for el in soup.find_all(["h2", "h3", "section"]):
        kind = el.name
        if kind == "section":
            if "card" not in el.get("class", []):
                continue
            kind = "card"
            text = el["data-toc"]
            target = el
        else:
            if el.find_parent("section", class_="card"):
                continue
            text = el.get_text(" ").strip()
            target = el
        if kind not in doc["toc_levels"]:
            continue
        i += 1
        target["id"] = f"t{i}"
        mk = soup.new_tag("span", attrs={"class": "mk"}); mk.string = f"@@T{i}@@"
        target.insert(0, mk)
        toc.append((f"t{i}", kind, text))
    return str(soup), meta, toc


# ---------------------------------------------------------------- HTML

def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def font_css():
    faces = [("Bricolage Grotesque", "bricolage-grotesque", w, "normal") for w in (600, 700, 800)]
    faces += [("Instrument Sans", "instrument-sans", w, "normal") for w in (400, 500, 600, 700)]
    faces += [("Instrument Sans", "instrument-sans", 400, "italic")]
    css = []
    for fam, slug, w, st in faces:
        for sub, rng in (("latin", "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"),
                         ("latin-ext", "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")):
            f = FONTS / slug / "files" / f"{slug}-{sub}-{w}-{st}.woff2"
            if f.exists():
                css.append(f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};font-display:block;"
                           f"src:url(data:font/woff2;base64,{b64(f)}) format('woff2');unicode-range:{rng};}}")
    return "\n".join(css)


CSS = r"""
:root{--bg:#F7F3EE;--ink:#1A1714;--org:#FF6A1A;--mut:#6B625A;--line:#E2D9CE;--card:#FFFDFA;--soft:#FBE7DA;}
@page{size:A4;margin:20mm 0 20mm 0;}
main,.toc{padding:0 17mm;}
*{box-sizing:border-box;}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;background:var(--bg);color:var(--ink);
 font-family:'Instrument Sans','Inter','Segoe UI','Helvetica Neue',Arial,sans-serif;
 font-size:10.6pt;line-height:1.55;}
h1,h2,h3,.code,.kick,.toc h2,.cover .t{font-family:'Bricolage Grotesque','Instrument Sans','Arial Black',sans-serif;}
.mk{position:absolute;left:0;top:0;font-size:2px;color:#F7F3EE;line-height:1;white-space:nowrap;}
h2,h3{position:relative;}
/* Portada */
.cover{height:297mm;width:210mm;background:var(--ink);color:var(--bg);position:relative;overflow:hidden;
 padding:24mm 20mm;display:flex;flex-direction:column;break-after:page;}
.cover .bar{position:absolute;left:0;top:0;bottom:0;width:7mm;background:var(--org);}
.cover .logo{width:30mm;height:30mm;}
.cover .k{margin-top:auto;font-size:11pt;letter-spacing:.14em;text-transform:uppercase;color:var(--org);font-weight:700;}
.cover .t{font-size:38pt;line-height:1.02;font-weight:800;margin:6mm 0 7mm;letter-spacing:-.01em;}
.cover .s{font-size:13.5pt;line-height:1.45;color:#D9D0C6;max-width:150mm;}
.cover .n{margin-top:6mm;font-size:11pt;color:var(--bg);border-left:3px solid var(--org);padding-left:4mm;max-width:150mm;}
.cover .foot{margin-top:22mm;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid #3A332D;padding-top:5mm;font-size:10.5pt;}
.cover .foot b{font-family:'Bricolage Grotesque',sans-serif;font-size:13pt;}
.cover .ver{color:var(--org);font-weight:600;}
.cover .big{position:absolute;right:-28mm;top:40mm;width:150mm;opacity:.07;}
/* Índice */
.toc{break-after:page;}
.toc h2{font-size:24pt;margin:0 0 6mm;}
.toc ol{list-style:none;padding:0;margin:0;}
.toc.cols ol{column-count:2;column-gap:10mm;}
.toc li{display:flex;align-items:baseline;gap:2mm;padding:1mm 0;border-bottom:1px solid var(--line);break-inside:avoid;}
.toc li a{color:inherit;text-decoration:none;flex:1;}
.toc li .pg{font-variant-numeric:tabular-nums;font-weight:600;color:var(--org);}
.toc li.l-h2{font-weight:700;font-family:'Bricolage Grotesque',sans-serif;font-size:11pt;padding-top:2.2mm;border-bottom:2px solid var(--ink);}
.toc li.l-h3,.toc li.l-card{padding-left:5mm;font-size:9.6pt;}
.toc.cols li.l-h2{break-after:avoid;}
/* Texto */
h2{font-size:21pt;line-height:1.12;font-weight:800;margin:9mm 0 4mm;letter-spacing:-.01em;}
h2::before{content:"";display:block;width:14mm;height:2.2mm;background:var(--org);margin-bottom:4mm;border-radius:1mm;}
h3{font-size:13.5pt;line-height:1.25;font-weight:700;margin:7mm 0 2.5mm;}
.keep{break-inside:avoid;}
.newpage{break-before:page;}
.newpage>h2,.keep.newpage>h2,h2.newpage{margin-top:0;}
h2.group{break-before:page;font-size:0;margin:0;height:0;overflow:hidden;}
h2.group::before{display:none;}
p{margin:0 0 3mm;}
ul,ol{margin:0 0 3.5mm;padding-left:6mm;}
li{margin:0 0 1.3mm;}
li::marker{color:var(--org);font-weight:700;}
strong{font-weight:700;}
a{color:var(--org);}
blockquote{margin:0 0 3.5mm;padding:3mm 4.5mm;background:var(--card);border-left:3px solid var(--line);border-radius:2mm;}
blockquote p:last-child{margin-bottom:0;}
.tag{display:inline-block;background:var(--org);color:#fff;font-weight:700;font-size:7.6pt;letter-spacing:.08em;
 padding:.4mm 1.8mm;border-radius:1mm;margin-right:1.5mm;vertical-align:1px;line-height:1.5;}
.ejemplo{background:var(--soft);border:1px solid #F6C9AC;border-left:4px solid var(--org);border-radius:2.5mm;
 padding:3.5mm 4.5mm;margin:0 0 4mm;break-inside:avoid;}
.ejemplo p:last-child,.ejemplo ul:last-child,.ejemplo blockquote:last-child{margin-bottom:0;}
.ejemplo blockquote{background:rgba(255,255,255,.6);border-left-color:var(--org);}
table{width:100%;border-collapse:collapse;margin:1mm 0 5mm;font-size:9.8pt;break-inside:auto;}
thead{display:table-header-group;}
tr{break-inside:avoid;}
th{background:var(--ink);color:var(--bg);text-align:left;padding:2mm 3mm;font-weight:700;}
th:first-child{border-top-left-radius:2mm;} th:last-child{border-top-right-radius:2mm;}
td{padding:2mm 3mm;border-bottom:1px solid var(--line);vertical-align:top;}
tbody tr:nth-child(even) td{background:rgba(255,255,255,.55);}
td:first-child{font-weight:600;}
.notice{background:var(--ink);color:var(--bg);border-radius:2.5mm;padding:4mm 5mm;margin:0 0 6mm;}
.notice strong{color:var(--org);}
/* Tarjetas de guion: una por página, letra grande para leer en el móvil */
section.card{break-before:page;break-inside:avoid;}
section.card header{border-bottom:3px solid var(--ink);padding-bottom:4mm;margin-bottom:6mm;}
section.card .kick{font-size:10.5pt;text-transform:uppercase;letter-spacing:.12em;color:var(--org);font-weight:700;margin-bottom:2.5mm;}
section.card .ct{display:flex;align-items:center;gap:4mm;}
section.card .code{background:var(--org);color:#fff;font-weight:800;font-size:16pt;border-radius:2.5mm;padding:1.5mm 3.5mm;line-height:1.1;}
section.card h3{font-size:24pt;line-height:1.08;margin:0;font-weight:800;}
.row{margin:0 0 5.5mm;break-inside:avoid;}
.row .lbl{font-size:9.5pt;text-transform:uppercase;letter-spacing:.12em;font-weight:700;color:var(--mut);margin-bottom:1.5mm;}
.row .txt{font-size:16pt;line-height:1.42;}
.row.gancho{background:var(--ink);color:var(--bg);border-radius:3mm;padding:5mm 6mm;}
.row.gancho .lbl{color:var(--org);}
.row.gancho .txt{font-size:21pt;line-height:1.28;font-weight:600;}
.row.cta{background:var(--soft);border-left:5px solid var(--org);border-radius:2.5mm;padding:4mm 5mm;}
.row.cta .lbl{color:var(--org);}
.row.cta .txt{font-weight:600;}
.row.pantalla .txt,.row.porque .txt,.row.ojo .txt,.row.otro .txt{font-size:12.5pt;line-height:1.45;}
.row.pantalla,.row.porque,.row.ojo{border-top:1px solid var(--line);padding-top:3.5mm;margin-bottom:3.5mm;}
.row.ojo .lbl{color:var(--org);}
/* WhatsApp */
.msg{break-inside:avoid;margin:0 0 5mm;}
.msg .mh{display:flex;align-items:center;gap:2.5mm;font-weight:700;margin-bottom:1.8mm;}
.msg .num{display:inline-flex;align-items:center;justify-content:center;min-width:7mm;height:7mm;border-radius:50%;
 background:var(--org);color:#fff;font-family:'Bricolage Grotesque',sans-serif;font-size:10pt;}
.msg .bubble{background:#fff;border:1px solid var(--line);border-radius:1mm 4mm 4mm 4mm;padding:3.5mm 4.5mm;font-size:11.5pt;line-height:1.5;margin-left:9.5mm;}
.msg .bubble p{margin:0;}
/* Plantillas */
section.tpl{break-inside:auto;margin:0 0 4mm;padding-top:2mm;}
section.tpl>.keep>h2,section.tpl>h2{display:flex;align-items:center;gap:3.5mm;}
section.tpl h2::before{display:none;}
section.tpl h2 .code{background:var(--org);color:#fff;font-size:15pt;border-radius:2.5mm;padding:1mm 3mm;min-width:11mm;text-align:center;}
.canva{display:grid;grid-template-columns:auto 1fr;gap:1mm 5mm;border:1.5px dashed var(--org);border-radius:2.5mm;padding:3mm 4.5mm;margin:4mm 0 2mm;font-size:9.6pt;break-inside:avoid;}
.canva .lbl{font-weight:700;color:var(--org);text-transform:uppercase;letter-spacing:.08em;font-size:8.8pt;grid-row:span 2;align-self:center;}
.canva .pending{color:var(--mut);font-style:italic;}
"""


def page_html(doc, body, meta, toc, pages=None):
    logo = b64(LOGO)
    kicker = meta["kicker"] or "Ceos Growth · Kit Primera Campaña"
    note = doc.get("cover_note", "")
    cover = f"""
<div class="cover">
  <div class="bar"></div>
  <img class="big" src="data:image/png;base64,{logo}" alt="">
  <img class="logo" src="data:image/png;base64,{logo}" alt="Ceos Growth">
  <div class="k">{html.escape(kicker)}</div>
  <div class="t">{html.escape(meta['title'])}</div>
  {f'<div class="s">{html.escape(meta["sub"])}</div>' if meta['sub'] else ''}
  {f'<div class="n">{html.escape(note)}</div>' if note else ''}
  <div class="foot"><div><b>Ceos Growth · Burgos</b><br>{html.escape(COPY)}</div><div class="ver">{VERSION}</div></div>
</div>"""
    toc_html = ""
    if toc:
        items = []
        for tid, kind, text in toc:
            pg = str(pages.get(tid, "")) if pages else "00"
            items.append(f'<li class="l-{kind}"><a href="#{tid}">{html.escape(text)}</a><span class="pg">{pg}</span></li>')
        cls = "toc cols" if doc.get("toc_cols") == 2 else "toc"
        toc_html = f'<nav class="{cls}"><h2>{html.escape(doc["toc_title"])}</h2><ol>{"".join(items)}</ol></nav>'
    if pages is not None:
        body = re.sub(r'<span class="mk">@@T\d+@@</span>', "", body)
    head = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>{html.escape(meta['title'])} · Ceos Growth</title>
<style>{font_css()}{CSS}</style>"""
    cover_doc = head + "<style>@page{size:A4;margin:0;}</style></head><body>" + cover + "</body></html>"
    return head + f"</head><body>{toc_html}<main>{body}</main></body></html>", cover_doc


def header_footer(doc):
    base = ("<style>html,body{margin:0;padding:0;-webkit-print-color-adjust:exact;}</style>")
    style = ("width:100%;height:17mm;margin:0;background:#F7F3EE;"
             "font-family:'Instrument Sans',Arial,sans-serif;font-size:8pt;color:#6B625A;"
             "display:flex;justify-content:space-between;align-items:center;padding:0 17mm;box-sizing:border-box;")
    header = (f'{base}<div style="{style}align-items:flex-end;padding-bottom:5mm;">'
              f'<span>Ceos Growth · Kit Primera Campaña</span>'
              f'<span style="color:#FF6A1A;font-weight:700;">{html.escape(doc["short"])}</span></div>')
    footer = (f'{base}<div style="{style}align-items:flex-start;padding-top:5mm;">'
              f'<span>{html.escape(COPY)}</span>'
              f'<span style="font-weight:700;color:#1A1714;font-size:9pt;"><span class="pageNumber"></span>'
              f'<span style="color:#6B625A;font-weight:400;"> / <span class="totalPages"></span></span></span></div>')
    return header, footer


def render(page, html_path, pdf_path, doc):
    page.goto(html_path.as_uri())
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready")
    header, footer = header_footer(doc)
    page.pdf(path=str(pdf_path), format="A4", print_background=True, display_header_footer=True,
             header_template=header, footer_template=footer, prefer_css_page_size=True)


def marker_pages(pdf_path):
    txt = subprocess.run(["pdftotext", "-layout", str(pdf_path), "-"], capture_output=True, text=True).stdout
    pages = {}
    for n, ptxt in enumerate(txt.split("\f"), start=1):
        for m in re.finditer(r"@@T(\d+)@@", ptxt):
            pages.setdefault(f"t{m.group(1)}", n)
    return pages


def chromium_path():
    root = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    for c in sorted(root.glob("chromium-*/chrome-linux*/chrome")):
        return str(c)
    return None


def main():
    SRC.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception:
            browser = pw.chromium.launch(executable_path=chromium_path())
        page = browser.new_page()
        for doc in DOCS:
            md_text = (KIT / doc["md"]).read_text(encoding="utf-8")
            body = markdown.markdown(norm_md(md_text), extensions=["tables", "sane_lists"])
            body, meta, toc = transform(doc, body)
            html_path = SRC / (Path(doc["out"]).stem + ".html")
            pdf_path = HERE / doc["out"]
            stem = Path(doc["out"]).stem
            cover_path = SRC / (stem + "-portada.html")
            # Pasada 1: localizar en qué página cae cada entrada del índice
            body_html, cover_html = page_html(doc, body, meta, toc, None)
            html_path.write_text(body_html, encoding="utf-8")
            cover_path.write_text(cover_html, encoding="utf-8")
            with tempfile.TemporaryDirectory() as td:
                tmp = Path(td) / "p1.pdf"
                render(page, html_path, tmp, doc)
                pages = marker_pages(tmp)
                nxt_pg = None
                for tid, _, _ in reversed(toc):  # títulos de grupo ocultos: página de la tarjeta siguiente
                    if tid in pages:
                        nxt_pg = pages[tid]
                    elif nxt_pg:
                        pages[tid] = nxt_pg
                missing = [t for t, _, _ in toc if t not in pages]
                if missing:
                    print(f"  aviso: {len(missing)} entradas del índice sin página en {doc['out']}", file=sys.stderr)
                # Pasada 2: índice con números y sin marcadores
                body_html, _ = page_html(doc, body, meta, toc, pages)
                html_path.write_text(body_html, encoding="utf-8")
                body_pdf = Path(td) / "body.pdf"
                cover_pdf = Path(td) / "cover.pdf"
                render(page, html_path, body_pdf, doc)
                page.goto(cover_path.as_uri())
                page.evaluate("document.fonts.ready")
                page.pdf(path=str(cover_pdf), format="A4", print_background=True, prefer_css_page_size=True)
                w = PdfWriter()
                for f in (cover_pdf, body_pdf):
                    for pg in PdfReader(str(f)).pages:
                        w.add_page(pg)
                w.add_metadata({"/Title": meta["title"], "/Author": "Ceos Growth, S.L.",
                                "/Subject": "Kit Primera Campaña " + VERSION})
                w.compress_identical_objects() if hasattr(w, "compress_identical_objects") else None
                with open(pdf_path, "wb") as fh:
                    w.write(fh)
            n = len(PdfReader(str(pdf_path)).pages)
            print(f"{doc['out']}: {n} páginas (portada + {n-1}), {pdf_path.stat().st_size/1024:.0f} KB")
        browser.close()


if __name__ == "__main__":
    main()
