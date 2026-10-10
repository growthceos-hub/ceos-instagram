import re
LIST = re.compile(r'^([-*+]|\d+\.) ')

def norm(t):
    """Adapta el Markdown (estilo GitHub) a python-markdown sin tocar el .md."""
    out = []
    prev = 'blank'  # blank | text | item | nested | indented_text
    for ln in t.split('\n'):
        if not ln.strip():
            out.append(ln); prev = 'blank'; continue
        m = re.match(r'^( +)(\S.*)$', ln)
        if m:
            body = m.group(2)
            if LIST.match(body):
                out.append('    ' + body); prev = 'nested'; continue
            if prev in ('nested', 'item'):
                out.append(''); out.append('    ' + body); prev = 'indented_text'; continue
            out.append('    ' + body); prev = 'indented_text'; continue
        if LIST.match(ln):
            if prev in ('text', 'indented_text'):
                out.append('')
            out.append(ln); prev = 'item'; continue
        out.append(ln); prev = 'text'
    return '\n'.join(out)
