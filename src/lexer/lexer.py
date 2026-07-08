import ply.lex as lex
from lexer.errors import t_error

# ==========================
# PALABRAS RESERVADAS
# ==========================

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'end': 'END',
    'def': 'DEF',
    'return': 'RETURN',
    'puts': 'PUTS',
    'gets': 'GETS',
    'nil': 'NIL',
    'false': 'FALSE',
    'true': 'TRUE'
}

# ==========================
# TOKENS
# ==========================

tokens = [

    # PARTE DE TANIA
    'MAS', 'MENOS', 'POR', 'DIVIDIDO', 'MODULO',
    'IGUAL_QUE', 'DIFERENTE', 'MAYOR_IGUAL', 'MENOR_IGUAL',
    'MAYOR', 'MENOR',
    'ASIGNACION', 'AND', 'OR', 'NOT',

    # PARTE DE GENESIS
    'PAREN_IZQ', 'PAREN_DER',
    'CORCHETE_IZQ', 'CORCHETE_DER',
    'LLAVE_IZQ', 'LLAVE_DER',
    'COMA', 'ASIGNACION_HASH', 'RANGO',

    # PARTE DE JOSUE
    'CONSTANTE',
    'VARIABLE_LOCAL',
    'FLOAT',
    'INTEGER',
    'STRING'

] + list(reserved.values())

# ==========================
# REGLAS DE TANIA
# ==========================

t_IGUAL_QUE = r'=='
t_DIFERENTE = r'!='
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_AND = r'&&'
t_OR = r'||'

t_MAYOR = r'>'
t_MENOR = r'<'
t_NOT = r'!'
t_ASIGNACION = r'='
t_MAS = r'+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_MODULO = r'%'

# ==========================
# REGLAS DE GENESIS
# ==========================

t_PAREN_IZQ = r'\('
t_PAREN_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_COMA = r','
t_ASIGNACION_HASH = r'=>'
t_RANGO = r'\.\.'

def t_COMENTARIO_MULTILINEA(t):
    r'=begin[\s\S]*?=end'
    pass

def t_COMENTARIO_LINEA(t):
    r'\#.*'
    pass

# ==========================
# REGLAS DE JOSUE
# ==========================

def t_FLOAT(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^\\\n]|(\\.))*?"'
    return t

def t_CONSTANTE(t):
    r'[A-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'CONSTANTE')
    return t

def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_LOCAL')
    return t

# ==========================
# CONFIGURACIÓN DEL LEXER
# ==========================

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()