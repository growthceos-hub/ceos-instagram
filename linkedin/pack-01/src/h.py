# -*- coding: utf-8 -*-
"""Piezas HTML para las páginas del pack de LinkedIn (1080×1350)."""


def esc(t):
    return t


def ej(t="EJEMPLO"):
    return f'<span class="ej">{t}</span>'


def say(t):
    return f'<div class="say">«{t}»</div>'


def note(t):
    return f'<div class="note">{t}</div>'


def p(t, cls="txt"):
    return f'<p class="{cls}">{t}</p>'


def arr(items, cls=""):
    return f'<ul class="arr {cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def stat(big, label, cls=""):
    return f'<div class="stat {cls}"><div class="b">{big}</div><div class="l">{label}</div></div>'


def stats(*s, cols=None):
    cols = cols or len(s)
    return f'<div class="stats" style="grid-template-columns:repeat({cols},1fr)">' + "".join(s) + "</div>"


def card(title, body, cls=""):
    return f'<div class="card {cls}"><div class="ct">{title}</div><div class="cb">{body}</div></div>'


def pair(a, b):
    return f'<div class="pair">{a}{b}</div>'


def opts(question, items):
    """items: lista de (color, texto). color: v, a, r o ''."""
    li = "".join(f'<li><span class="dot {c}"></span>{t}</li>' for c, t in items)
    return f'<div class="q"><div class="qq">{question}</div><ul class="opts">{li}</ul></div>'


def big(n):
    return f'<div class="bignum">{n}</div>'


def chips(items):
    return '<div class="chips">' + "".join(f"<span>{x}</span>" for x in items) + "</div>"


def rows(items):
    """items: lista de (izquierda, derecha)."""
    return '<table class="rows">' + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in items) + "</table>"


# ---- páginas

def cover(kicker, title, sub="", foot=""):
    return dict(kind="cover", kicker=kicker, title=title, sub=sub, foot=foot)


def page(kicker, title, body, cls=""):
    return dict(kind="page", kicker=kicker, title=title, body=body, cls=cls)


def close(title, sub, cta="Escríbeme por privado"):
    return dict(kind="close", title=title, sub=sub, cta=cta)
