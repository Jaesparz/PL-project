import ply.lex as lex

# Lista global para atrapar errores
errores_lexicos = []

# ==========================================
# PARTE DE TANIA
# ==========================================
reserved = {
    'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'do': 'DO',
    'end': 'END', 'def': 'DEF', 'return': 'RETURN', 'puts': 'PUTS',
    'gets': 'GETS', 'nil': 'NIL', 'false': 'FALSE', 'true': 'TRUE'
}

tokens_tania = [
    'MAS', 'MENOS', 'POR', 'DIVIDIDO', 'MODULO',
    'IGUAL_QUE', 'DIFERENTE', 'MAYOR_IGUAL', 'MENOR_IGUAL', 'MAYOR', 'MENOR',
    'ASIGNACION', 'AND', 'OR', 'NOT'
]

t_IGUAL_QUE = r'=='
t_DIFERENTE = r'!='
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_AND = r'&&'
t_OR = r'\|\|'

t_MAYOR = r'>'
t_MENOR = r'<'
t_NOT = r'!'
t_ASIGNACION = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_MODULO = r'%'

# ==========================================
# PARTE DE JOSUE
# ==========================================
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

# ==========================================
# PARTE DE GENESIS
# ==========================================
tokens_genesis = [
    'PAREN_IZQ', 'PAREN_DER', 'CORCHETE_IZQ', 'CORCHETE_DER', 
    'LLAVE_IZQ', 'LLAVE_DER', 'COMA', 'ASIGNACION_HASH', 'RANGO'
]

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

# ==========================================
# CONFIGURACIÓN GENERAL DE PLY
# ==========================================
tokens = tokens_tania + tokens_josue + tokens_genesis + list(reserved.values())

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    error_msg = f"Linea {t.lexer.lineno}: Caracter no valido '{t.value[0]}'"
    errores_lexicos.append(error_msg)
    t.lexer.skip(1)

# Construcción y exportación del analizador léxico
lexer = lex.lex()