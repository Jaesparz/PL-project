import ply.yacc as yacc

# Importamos los tokens directamente de nuestro lexer unificado
from lexer.lexer import tokens

errores_sintacticos = []

# Precedencia de operadores para agrupar multiplicaciones y divisiones primero
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUAL_QUE', 'DIFERENTE'),
    ('left', 'MAYOR_IGUAL', 'MENOR_IGUAL', 'MAYOR', 'MENOR'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),
    ('right', 'NOT'),
)

#PARTE DE JOSUE

def p_programa(p):
    '''programa : declaraciones'''
    p[0] = p[1]

def p_declaraciones(p):
    '''declaraciones : declaraciones instruccion
                     | instruccion'''
    pass

def p_instruccion(p):
    '''instruccion : asignacion
                   | estructura_control
                   | declaracion_funcion
                   | llamada_funcion
                   | impresion
                   | entrada
                   | expresion'''
    pass

def p_asignacion(p):
    '''asignacion : VARIABLE_LOCAL ASIGNACION expresion
                  | CONSTANTE ASIGNACION expresion
                  | VARIABLE_LOCAL ASIGNACION estructura_datos'''
    pass

def p_expresion_binaria(p):
    '''expresion : expresion MAS expresion
                 | expresion MENOS expresion
                 | expresion POR expresion
                 | expresion DIVIDIDO expresion
                 | expresion MODULO expresion
                 | expresion IGUAL_QUE expresion
                 | expresion DIFERENTE expresion
                 | expresion MAYOR_IGUAL expresion
                 | expresion MENOR_IGUAL expresion
                 | expresion MAYOR expresion
                 | expresion MENOR expresion
                 | expresion AND expresion
                 | expresion OR expresion'''
    pass


def p_expresion_unaria(p):
    '''expresion : NOT expresion'''
    pass

def p_expresion_agrupada(p):
    '''expresion : PAREN_IZQ expresion PAREN_DER'''
    pass

def p_expresion_valor(p):
    '''expresion : INTEGER
                 | FLOAT
                 | STRING
                 | TRUE
                 | FALSE
                 | NIL
                 | VARIABLE_LOCAL
                 | CONSTANTE'''
    pass

def p_estructura_datos(p):
    '''estructura_datos : arreglo
                        | hash
                        | rango'''
    pass
    


#PARTE DE TANIA

def p_arreglo(p):
    '''arreglo : CORCHETE_IZQ elementos_opt CORCHETE_DER'''
    pass

def p_elementos_opt(p):
    '''elementos_opt : elementos
                     | empty'''
    pass

def p_elementos(p):
    '''elementos : expresion
                 | expresion COMA elementos'''
    pass

def p_hash(p):
    '''hash : LLAVE_IZQ pares_opt LLAVE_DER'''
    pass

def p_pares_opt(p):
    '''pares_opt : pares
                 | empty'''
    pass


def p_pares(p):
    '''pares : STRING ASIGNACION_HASH expresion
             | STRING ASIGNACION_HASH expresion COMA pares'''
    pass

def p_rango(p):
    '''rango : INTEGER RANGO INTEGER'''
    pass

def p_estructura_control(p):
    '''estructura_control : IF expresion declaraciones END
                          | IF expresion declaraciones ELSE declaraciones END
                          | WHILE expresion DO declaraciones END
                          | WHILE expresion declaraciones END
                          | FOR VARIABLE_LOCAL IN rango declaraciones END'''
    pass

def p_declaracion_funcion(p):
    '''declaracion_funcion : DEF VARIABLE_LOCAL PAREN_IZQ parametros_opt PAREN_DER declaraciones END
                           | DEF VARIABLE_LOCAL declaraciones END'''
    pass


#PARTE DE GENESIS


def p_parametros_opt(p):
    '''parametros_opt : parametros
                      | empty'''
    pass

def p_parametros(p):
    '''parametros : VARIABLE_LOCAL
                  | VARIABLE_LOCAL COMA parametros'''
    pass

def p_llamada_funcion(p):
    '''llamada_funcion : VARIABLE_LOCAL PAREN_IZQ elementos_opt PAREN_DER
                       | RETURN expresion'''
    pass

def p_impresion(p):
    '''impresion : PUTS expresion'''
    pass

def p_entrada(p):
    '''entrada : VARIABLE_LOCAL ASIGNACION GETS'''
    pass

def p_empty(p):
    '''empty :'''
    pass

# Manejo de errores enfocado estrictamente en las líneas
def p_error(p):
    if p:
        error_msg = f"Linea {p.lineno}: Error sintactico de estructura cerca de '{p.value}'"
    else:
        error_msg = "Error Sintactico: Fin de archivo inesperado (probablemente falto cerrar un 'end' o un bloque)."
    errores_sintacticos.append(error_msg)

parser = yacc.yacc()