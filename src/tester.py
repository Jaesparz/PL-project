import os
import glob
from datetime import datetime

# Obtenemos la ruta absoluta de la carpeta 'src'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Importamos el lexer y la lista de errores desde nuestro archivo unificado
from lexer.lexer import lexer, errores_lexicos

def limpiar_logs_viejos():
    """Busca y elimina todos los archivos txt de logs anteriores en la carpeta logs"""
    ruta_logs = os.path.join(BASE_DIR, 'logs', "lexico-*.txt")
    archivos_viejos = glob.glob(ruta_logs)
    for archivo in archivos_viejos:
        try:
            os.remove(archivo)
        except Exception:
            pass

def analizar_y_generar_log(archivo_entrada, autor):
    # 1. Limpiamos los errores de la ejecución anterior
    errores_lexicos.clear()
    
    # 2. Buscamos el archivo en la carpeta 'algoritmos'
    ruta_archivo = os.path.join(BASE_DIR, 'algoritmos', archivo_entrada)
    
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontro el archivo '{ruta_archivo}'")
        return
        
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        data = f.read()
        
    if len(data.strip()) == 0:
        print(f"ADVERTENCIA: El archivo '{archivo_entrada}' esta VACIO.")
        return
        
    # 3. Ejecutamos el lexer
    lexer.lineno = 1 
    lexer.input(data)
    tokens_reconocidos = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_reconocidos.append(f"Linea {tok.lineno:02d} | Token: {tok.type:<15} | Lexema: {tok.value}")

    # 4. Generamos el reporte en la carpeta 'logs'
    fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
    nombre_log = f"lexico-{autor}-{fecha_hora}.txt"
    ruta_guardado = os.path.join(BASE_DIR, 'logs', nombre_log)
    
    with open(ruta_guardado, 'w', encoding='utf-8') as log:
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
                
    print(f"Log generado con exito en src/logs/: {nombre_log}")

if __name__ == '__main__':
    limpiar_logs_viejos()
    print("Limpieza de logs anteriores completada.")

    # Generacion de logs
    analizar_y_generar_log('algoritmo_josue.rb', 'JosueEsparza')
    analizar_y_generar_log('algoritmo_genesis.rb', 'GenesisMichilena')
    analizar_y_generar_log('algoritmo_tania.rb', 'TaniaTorres')