errores_lexicos = []

def t_error(t):
    error_msg = f"Linea {t.lexer.lineno}: Caracter no valido '{t.value[0]}'"
    errores_lexicos.append(error_msg)
    t.lexer.skip(1)