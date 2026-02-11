import re

TOKEN_SPEC = [
    ('COMMENT',  r'#.*'),
    ('KEYWORD',  r'\b(FROM|RUN|CMD|LABEL|EXPOSE|ENV|ADD|COPY|ENTRYPOINT|VOLUME|USER|WORKDIR|ARG|ONBUILD)\b'),
    ('STRING',   r'[a-zA-Z0-9.\-/:\$\[\]\", ]+'), 
    ('NEWLINE',  r'\n'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.'),
]

def tokenize(code):
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NEWLINE' or kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Caracter inesperado {value!r}')
        yield kind, value