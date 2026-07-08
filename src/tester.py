import os
import glob
from datetime import datetime

# Rutas absolutas para evitar el error de "File not found"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Importamos las herramientas de nuestros dos archivos unificados
from lexer.lexer import lexer, errores_lexicos
from parser import sintactico

def limpiar_logs_viejos():
    """Busca y elimina todos los archivos txt de logs anteriores en la carpeta logs"""
    ruta_logs = os.path.join(BASE_DIR, 'logs', "*.txt")
    archivos_viejos = glob.glob(ruta_logs)
    for archivo in archivos_viejos:
        try:
            os.remove(archivo)
        except Exception:
            pass

def analizar_y_generar_log(archivo_entrada, autor):
    # 1. Limpiamos errores anteriores para que no se mezclen los reportes
    errores_lexicos.clear()
    sintactico.errores_sintacticos.clear()
    
    ruta_archivo = os.path.join(BASE_DIR, 'algoritmos', archivo_entrada)
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontro el archivo '{ruta_archivo}'")
        return
        
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        data = f.read()
        
    if len(data.strip()) == 0:
        print(f"ADVERTENCIA: El archivo '{archivo_entrada}' esta VACIO.")
        return
        
    # ==================================
    # FASE 1: ANÁLISIS LÉXICO
    # ==================================
    lexer.lineno = 1 
    lexer.input(data)
    tokens_reconocidos = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_reconocidos.append(f"Linea {tok.lineno:02d} | Token: {tok.type:<15} | Lexema: {tok.value}")

    # ==================================
    # FASE 2: ANÁLISIS SINTÁCTICO
    # ==================================
    # Reiniciamos la línea del lexer a 1 antes de pasárselo al parser
    lexer.lineno = 1 
    sintactico.parser.parse(data, lexer=lexer)

    # ==================================
    # FASE 3: GENERACIÓN DE LOGS
    # ==================================
    fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
    
    # Nos aseguramos de que la carpeta 'logs' exista
    carpeta_logs = os.path.join(BASE_DIR, 'logs')
    os.makedirs(carpeta_logs, exist_ok=True)
    
    # ------------------
    # Guardar Log Léxico
    # ------------------
    nombre_log_lex = f"lexico-{autor}-{fecha_hora}.txt"
    ruta_guardado_lex = os.path.join(carpeta_logs, nombre_log_lex)
    
    with open(ruta_guardado_lex, 'w', encoding='utf-8') as log_l:
        log_l.write(f"=== REPORTE DE ANALISIS LEXICO ===\n")
        log_l.write(f"Archivo analizado: {archivo_entrada}\n")
        log_l.write(f"Desarrollador: {autor}\n")
        log_l.write(f"Fecha de generacion: {fecha_hora}\n\n")
        log_l.write("--- TOKENS VALIDOS ---\n")
        if not tokens_reconocidos:
            log_l.write("(No se reconocio ningun token. El archivo fuente estaba vacio o sin guardar)\n")
        else:
            for t in tokens_reconocidos:
                log_l.write(t + "\n")
        log_l.write("\n--- ERRORES LEXICOS ---\n")
        if len(errores_lexicos) == 0:
            log_l.write("No se encontraron errores lexicos.\n")
        else:
            for e in errores_lexicos:
                log_l.write(e + "\n")
                
    print(f"Log lexico generado: {nombre_log_lex}")

    # ----------------------
    # Guardar Log Sintáctico
    # ----------------------
    nombre_log_sint = f"sintactico-{autor}-{fecha_hora}.txt"
    ruta_guardado_sint = os.path.join(carpeta_logs, nombre_log_sint)
    
    with open(ruta_guardado_sint, 'w', encoding='utf-8') as log_s:
        log_s.write(f"=== REPORTE DE ANALISIS SINTACTICO ===\n")
        log_s.write(f"Archivo analizado: {archivo_entrada}\n")
        log_s.write(f"Desarrollador: {autor}\n")
        log_s.write(f"Fecha de generacion: {fecha_hora}\n\n")
        log_s.write("--- RESULTADO DEL ANALISIS ---\n")
        if len(sintactico.errores_sintacticos) == 0:
            log_s.write("El codigo cumple con toda la sintaxis documentada. Ningun error encontrado.\n")
        else:
            log_s.write(f"Se encontraron {len(sintactico.errores_sintacticos)} errores de sintaxis:\n\n")
            for e in sintactico.errores_sintacticos:
                log_s.write(e + "\n")
                
    print(f"Log sintactico generado: {nombre_log_sint}")


if __name__ == '__main__':
    limpiar_logs_viejos()
    print("Limpieza de logs anteriores completada.\n")

    # Ejecutamos las validaciones
    analizar_y_generar_log('algoritmo_josue.rb', 'JosueEsparza')
    print("-" * 40)
    analizar_y_generar_log('algoritmo_genesis.rb', 'GenesisMichilena')
    print("-" * 40)
    analizar_y_generar_log('algoritmo_tania.rb', 'TaniaTorres')