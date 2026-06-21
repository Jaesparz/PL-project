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
