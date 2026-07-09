import tkinter as tk
from tkinter import messagebox

# Importamos las funciones de tu archivo tester.py
from tester import limpiar_logs_viejos, analizar_y_generar_log

def correr_algoritmos():
    try:
        # 1. Ejecutamos la misma lógica del tester
        limpiar_logs_viejos()
        analizar_y_generar_log('algoritmo_josue.rb', 'JosueEsparza')
        analizar_y_generar_log('algoritmo_genesis.rb', 'GenesisMichilena')
        analizar_y_generar_log('algoritmo_tania.rb', 'TaniaTorres')
        
        # 2. Mostramos la alerta emergente que pediste
        mensaje = (
            "¡Análisis ejecutado con éxito!\n"
            "Todos los logs se han guardado en la carpeta 'logs'.\n\n"
            "NOTA: Si desea testear algo diferente o cambiar algo de los algoritmos, "
            "por favor hágalo directamente en el archivo .rb respectivo y vuelva a presionar el botón."
        )
        messagebox.showinfo("Proceso Completado", mensaje)
        
    except Exception as e:
        messagebox.showerror("Error de Ejecución", f"Ocurrió un error: {str(e)}")


# CONFIGURACIÓN DE VENTANA

ventana = tk.Tk()
ventana.title("MiniRuby Analyzer - Compilador")
# Tamaño de la ventana
ventana.geometry("450x250")
ventana.configure(bg="#f4f4f9")

# Título Principal
lbl_titulo = tk.Label(
    ventana, 
    text="Analizador de MiniRuby", 
    font=("Helvetica", 16, "bold"), 
    bg="#f4f4f9", 
    fg="#333"
)
lbl_titulo.pack(pady=(20, 5))

# Subtítulo / Instrucción
lbl_instruccion = tk.Label(
    ventana, 
    text="Presione el botón para evaluar los códigos fuente\ny generar los reportes de las 3 fases.", 
    font=("Helvetica", 10), 
    bg="#f4f4f9", 
    fg="#666"
)
lbl_instruccion.pack(pady=(0, 20))

# Botón de Ejecución
btn_correr = tk.Button(
    ventana, 
    text="▶ CORRER ALGORITMOS", 
    font=("Helvetica", 12, "bold"), 
    bg="#4CAF50", 
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    relief=tk.FLAT,
    padx=20,
    pady=10,
    command=correr_algoritmos
)
btn_correr.pack()

# Footer
lbl_footer = tk.Label(
    ventana, 
    text="Fases: Léxico | Sintáctico | Semántico", 
    font=("Helvetica", 8, "italic"), 
    bg="#f4f4f9", 
    fg="#999"
)
lbl_footer.pack(side=tk.BOTTOM, pady=10)

# Iniciamos el bucle de la interfaz
ventana.mainloop()