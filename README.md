# MiniRuby Analyzer - Componente Léxico
Este proyecto consiste en la implementación de un analizador léxico, sintáctico y semántico diseñado para procesar un subconjunto básico del lenguaje de programación **Ruby**. Actualmente, el repositorio contiene el primer avance del proyecto correspondiente a la fase del **Analizador Léxico**, capaz de escanear código fuente, identificar tokens válidos y reportar errores en la sintaxis de los caracteres.

## Equipo de Desarrollo
* **Josué Esparza** (@Jaesparz)
* **Génesis Michilena** (@GenesisMichilena)
* **Tania Torres** (@camilytzh)

---

## Detalles de Implementación Técnica

El analizador léxico fue desarrollado en **Python 3** utilizando la biblioteca **PLY (Python Lex-Yacc)**. La implementación se basa en el reconocimiento de patrones mediante **expresiones regulares (Regex)** para clasificar cadenas de texto en tokens significativos para el lenguaje Ruby.

### 1. Arquitectura Modular del Lexer
Para optimizar el desarrollo colaborativo y evitar conflictos de control de versiones, el reconocimiento de tokens se dividió en tres módulos:
* **`josue_lex.py`:** Implementa reglas léxicas para los **Identificadores** (variables locales y constantes) y **Tipos de Datos Primitivos** (números enteros, flotantes y cadenas de texto).
* **`tania_lex.py`:** Define el diccionario de **Palabras Reservadas** (`if`, `while`, `def`, `puts`, etc.) y las expresiones regulares para todos los **Operadores** (aritméticos, lógicos, de asignación y relacionales).
* **`genesis_lex.py`:** Configura el reconocimiento de **Delimitadores** (paréntesis, llaves, corchetes, comas, rangos) y define las reglas para ignorar los **Comentarios** (unilínea y multilínea).

### 2. Implementación de los Algoritmos de Prueba (.rb)
Para validar el analizador, se diseñaron tres scripts de prueba nativos en Ruby (`.rb`). La implementación de estos algoritmos siguió directrices estrictas:
* **Cobertura de Tokens:** Cada archivo fue estructurado lógicamente para abarcar la mayor cantidad de componentes del lenguaje asignados a cada integrante (ciclos, hashes, rangos, comparaciones lógicas).
* **Inyección de Errores Intencionales:** Para probar el mecanismo de excepciones del analizador (`t_error`), cada archivo implementa deliberadamente un símbolo ajeno a nuestro subconjunto de Ruby.
    * **`algoritmo_josue.rb` (Simulador de Combate MMA):** Simula la estamina en un combate. *Error inyectado:* Símbolo `@` (Línea 10).
    * **`algoritmo_genesis.rb` (Control de Calificaciones):** Evalúa el estado de aprobación mediante diccionarios y funciones. *Error inyectado:* Símbolo `?` (Línea 7).
    * **`algoritmo_tania.rb` (Iterador de Inventario):** Búsquedas en arreglos usando ciclos y rangos. *Error inyectado:* Símbolo `$` (Línea 8).

### 3. Motor de Análisis y Generación de Logs (`tester.py`)
El archivo `tester.py` no solo ensambla el lexer unificado importando los tres módulos anteriores, sino que actúa como un entorno de pruebas automatizado. Su funcionamiento interno es el siguiente:

1. **Limpieza de Entorno:** Utiliza la librería `glob` y el módulo `os` para buscar y eliminar dinámicamente cualquier archivo `lexico-*.txt` generado en ejecuciones anteriores, garantizando que no se acumule basura en el repositorio.
2. **Validación de Integridad:** Antes de analizar, lee el archivo `.rb`. Si el archivo está vacío (ej. no se guardaron los cambios en el editor), lanza una advertencia en consola y detiene la creación de falsos positivos.
3. **Escaneo de Tokens (`lexer.input`):** El código fuente se introduce en el motor de PLY. Un bucle `while` itera sobre `lexer.token()` para extraer secuencialmente cada componente validado, guardándolo en una lista temporal junto con su número de línea.
4. **Manejo de Excepciones:** Si durante el escaneo se encuentra un carácter no definido en las Regex, se dispara la función `t_error()`, la cual guarda el mensaje de error en una variable global (`errores_lexicos`) y fuerza al lexer a saltar ese carácter para que el programa no colapse (`t.lexer.skip(1)`).
5. **Escritura del Log:** Utilizando el módulo `datetime`, se genera un nombre de archivo único (`lexico-[Nombre]-[Fecha]-[Hora].txt`). El script abre este archivo en modo escritura (`'w'`) y formatea los arrays de tokens válidos y errores atrapados en un reporte de texto plano legible.

---

## Requisitos y Ejecución

**Requisitos:**
* Python 3.x
* Biblioteca PLY (`pip install ply`)

**Ejecución:**

Desde la terminal, ejecuta el comando:
   ```bash
   python tester.py
