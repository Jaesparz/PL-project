from datetime import datetime
import os
import glob

def limpiar_logs_viejos():
    """Busca y elimina todos los archivos txt de logs anteriores para que no se acumulen"""
    archivos_viejos = glob.glob("lexico-*.txt")
    for archivo in archivos_viejos:
        try:
            os.remove(archivo)
        except Exception:
            pass


def generar_log(archivo_entrada, autor, tokens_reconocidos, errores_lexicos):
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