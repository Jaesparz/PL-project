# MiniRuby Analyzer - Compilador Completo
Este proyecto consiste en la implementación de un analizador léxico, sintáctico y semántico diseñado para procesar un subconjunto básico del lenguaje de programación Ruby. El repositorio contiene el compilador funcional capaz de escanear código fuente, estructurar lógicamente los componentes del lenguaje y validar su coherencia en un entorno con interfaz gráfica.

## Equipo de Desarrollo
* **Josué Esparza** (@Jaesparz)
* **Génesis Michilena** (@GenesisMichilena)
* **Tania Torres** (@camilytzh)

---

## Detalles de Implementación Técnica

El compilador fue desarrollado en Python 3 utilizando la biblioteca PLY (Python Lex-Yacc) para las herramientas de construcción.

### 1. Arquitectura Final del Proyecto
Para facilitar el uso del compilador, la arquitectura está definida por un sistema controlado por una Interfaz Gráfica de Usuario (GUI), manteniendo una estricta separación de responsabilidades en sus motores de análisis:
- **Interfaz Gráfica (GUI):** Desarrollada con Tkinter, actúa como un panel de control central y minimalista. Mediante el botón "CORRER ALGORITMOS", invoca internamente al compilador para que procese automáticamente los archivos fuente .rb en segundo plano.
- **Analizador Léxico:** Lee el código fuente y agrupa los caracteres en tokens válidos (palabras reservadas, identificadores, símbolos y delimitadores), identificando y aislando errores de escritura.
- **Analizador Sintáctico:** Módulo independiente implementado con yacc que evalúa estrictamente que la secuencia de tokens generada por el lexer cumpla con las reglas gramaticales (la estructura correcta de declaraciones, ciclos, funciones, etc.).
- **Analizador Semántico:** Componente separado encargado de garantizar la coherencia lógica del código. Utiliza una tabla de símbolos (tabla_simbolos) para gestionar la memoria y los contextos del programa, operando de manera independiente a la validación estructural.

### 2. Fases del análisis
1. **Análisis Léxico:** Valida que el texto pertenezca al vocabulario permitido de nuestro subconjunto de Ruby. Si detecta un símbolo desconocido (ej. caracteres ilegales), lo reporta y continúa el escaneo.
2. **Análisis Sintáctico:** Verifica que la secuencia de tokens cumpla con las reglas gramaticales. Valida la estructura correcta de:
Declaración de variables y asignaciones.
Expresiones aritméticas y lógicas (respetando la precedencia de operadores).
Estructuras de control (if, while, for) y sus cierres obligatorios con end.
Estructuras de datos complejas (Arreglos, Hashes y Rangos).
Declaración e invocación de funciones, así como la entrada/salida de datos (puts, gets).
3. **Análisis Semántico:** Garantiza la coherencia lógica del código validando reglas como:
Identificadores: Verifica que toda variable o función exista y haya sido declarada en la tabla de símbolos antes de ser invocada o utilizada en una operación.
Asignación de Tipo: Asegura que las constantes no sean modificadas tras su inicialización.

### 3. Implementación de los Algoritmos de Prueba (.rb)
Para validar el sistema completo, se diseñaron scripts de prueba nativos en Ruby (.rb) en la carpeta correspondiente. Estos algoritmos están diseñados para disparar errores específicos:
* **`algoritmo_josue.rb` (Simulador de Combate MMA):** Valida tipos de datos numéricos y booleanos, sentencias condicionales y ciclos iterativos.
* **`algoritmo_genesis.rb` (Control de Calificaciones):** Pone a prueba la estructura de Hashes, declaración de funciones con parámetros y operadores lógicos.
* **`algoritmo_tania.rb` (Iterador de Inventario):** Evalúa arreglos, rangos numéricos continuos y la interrupción de ciclos.
#### ***Nota: Cada archivo contiene errores intencionales comentados. Al descomentarlos, se dispararán las alertas léxicas, sintácticas o semánticas correspondientes para demostrar el manejo de excepciones del compilador*** 

### 4. Sistema de Retroalimentación y Logs
El panel gráfico mantiene el entorno visual limpio apoyándose en alertas emergentes (Pop-ups). Una vez que el motor finaliza el análisis de los archivos, el sistema muestra un cuadro de diálogo confirmando la ejecución.
Todos los resultados, incluyendo los tokens exitosos, advertencias de estructura y errores de lógica de las tres etapas, se empaquetan y exportan automáticamente en formato de texto plano dentro de la carpeta logs

---

## Requisitos y Ejecución

**Requisitos:**
* Python 3.x
* Biblioteca PLY (`pip install ply`)

**Ejecución:**

Desde la terminal, ejecuta el comando:
   ```bash
   python tester.py
