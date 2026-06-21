import ply.lex as lex
from datetime import datetime
import os
import glob  

# Importamos las partes de cada integrante
from lex_Tania import *
from lex_JosueEsparza import *
from lex_Genesis import *

errores_lexicos = []

# Unificamos todos los tokens
tokens = tokens_tania + tokens_josue + tokens_genesis + list(reserved.values())

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    error_msg = f"Linea {t.lexer.lineno}: Caracter no valido '{t.value[0]}'"
    errores_lexicos.append(error_msg)
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

def limpiar_logs_viejos():
    """Busca y elimina todos los archivos txt de logs anteriores para que no se acumulen"""
    archivos_viejos = glob.glob("lexico-*.txt")
    for archivo in archivos_viejos:
        try:
            os.remove(archivo)
        except Exception as e:
            pass

def analizar_y_generar_log(archivo_entrada, autor):
    global errores_lexicos
    errores_lexicos = []
    
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        data = f.read()
        
    # Validamos si el archivo está vacío 
    if len(data.strip()) == 0:
        print(f"⚠️ ADVERTENCIA: El archivo '{archivo_entrada}' está VACÍO. Pega el código y guarda (Ctrl+S).")
        
    lexer.lineno = 1 
    lexer.input(data)
    tokens_reconocidos = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_reconocidos.append(f"Linea {tok.lineno:02d} | Token: {tok.type:<15} | Lexema: {tok.value}")

    fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
    nombre_log = f"lexico-{autor}-{fecha_hora}.txt"
    
    with open(nombre_log, 'w', encoding='utf-8') as log:
        log.write(f"=== REPORTE DE ANALISIS LEXICO ===\n")
        log.write(f"Archivo analizado: {archivo_entrada}\n")
        log.write(f"Desarrollador: {autor}\n")
        log.write(f"Fecha de generacion: {fecha_hora}\n\n")
        
        log.write("--- TOKENS VALIDOS ---\n")
        if not tokens_reconocidos:
            log.write("(No se reconocio ningun token. El archivo fuente estaba vacio o sin guardar)\n")
        else:
            for t in tokens_reconocidos:
                log.write(t + "\n")
            
        log.write("\n--- ERRORES LEXICOS ---\n")
        if len(errores_lexicos) == 0:
            log.write("No se encontraron errores lexicos.\n")
        else:
            for e in errores_lexicos:
                log.write(e + "\n")
                
    print(f"Log generado con exito: {nombre_log}")

if __name__ == '__main__':
    limpiar_logs_viejos()
    print("Limpieza de logs anteriores completada.")

    #Generacion de logs
    if os.path.exists('algoritmo_josue.rb'):
        analizar_y_generar_log('algoritmo_josue.rb', 'JosueEsparza')
    if os.path.exists('algoritmo_genesis.rb'):
        analizar_y_generar_log('algoritmo_genesis.rb', 'GenesisMichilena')
    if os.path.exists('algoritmo_tania.rb'):
        analizar_y_generar_log('algoritmo_tania.rb', 'TaniaTorres')