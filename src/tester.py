import os

import ply.lex as lex

from lexer.lexer import *
from logs.logger import limpiar_logs_viejos, generar_log
from lexer.errors import errores_lexicos

# Unificamos todos los tokens
tokens = tokens_tania + tokens_josue + tokens_genesis + list(reserved.values())

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Construcción del analizador léxico
lexer = lex.lex()


def analizar_y_generar_log(archivo_entrada, autor):

    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        data = f.read()

    # Validamos si el archivo está vacío
    if len(data.strip()) == 0:
        print(f"ADVERTENCIA: El archivo '{archivo_entrada}' está VACÍO. Pega el código y guarda (Ctrl+S).")

    lexer.lineno = 1
    lexer.input(data)

    tokens_reconocidos = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_reconocidos.append(
            f"Linea {tok.lineno:02d} | Token: {tok.type:<15} | Lexema: {tok.value}"
        )

    generar_log(
        archivo_entrada,
        autor,
        tokens_reconocidos,
        errores_lexicos
    )


if __name__ == '__main__':
    limpiar_logs_viejos()
    print("Limpieza de logs anteriores completada.")

    # Generación de logs
    if os.path.exists('algoritmo_josue.rb'):
        analizar_y_generar_log('algoritmo_josue.rb', 'JosueEsparza')

    if os.path.exists('algoritmo_genesis.rb'):
        analizar_y_generar_log('algoritmo_genesis.rb', 'GenesisMichilena')

    if os.path.exists('algoritmo_tania.rb'):
        analizar_y_generar_log('algoritmo_tania.rb', 'TaniaTorres')