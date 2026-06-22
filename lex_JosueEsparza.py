# PARTE DE JOSUE
from lex_Tania import reserved

tokens_josue = [
    'CONSTANTE', 'VARIABLE_LOCAL', 'FLOAT', 'INTEGER', 'STRING'
]

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_CONSTANTE(t):
    r'[A-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'CONSTANTE')
    return t

def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_LOCAL')
    return t
# FIN DE PARTE DE JOSUE