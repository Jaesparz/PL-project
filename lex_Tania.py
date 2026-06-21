# PARTE DE TANIA
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
# FIN DE PARTE DE TANIA
