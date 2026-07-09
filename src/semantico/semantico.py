import ply.yacc as yacc
from lexer.lexer import tokens

errores_semanticos = []
tabla_simbolos = {}

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
    pass

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


# SEMÁNTICA: REGISTRO DE VARIABLES

def p_asignacion(p):
    '''asignacion : VARIABLE_LOCAL ASIGNACION expresion
                  | CONSTANTE ASIGNACION expresion
                  | VARIABLE_LOCAL ASIGNACION estructura_datos'''
    # Se guarda la variable en la tabla de símbolos al asignarle un valor
    tabla_simbolos[p[1]] = True

def p_entrada(p):
    '''entrada : VARIABLE_LOCAL ASIGNACION GETS'''
    tabla_simbolos[p[1]] = True



def p_marcar_var(p):
    '''marcar_var : VARIABLE_LOCAL'''
    tabla_simbolos[p[1]] = True
    p[0] = p[1]


# SEMÁNTICA: VALIDACIÓN DE USO

def p_expresion_valor_variable(p):
    '''expresion : VARIABLE_LOCAL'''
    nombre_var = p[1]
    # Verificamos si la variable existe en nuestra tabla antes de usarse
    if nombre_var not in tabla_simbolos:
        errores_semanticos.append(f"Linea {p.lineno(1)}: Error Semantico - La variable '{nombre_var}' no ha sido declarada antes de usarse.")
    p[0] = nombre_var

def p_expresion_valor_constante(p):
    '''expresion : CONSTANTE'''
    nombre_const = p[1]
    if nombre_const not in tabla_simbolos:
        errores_semanticos.append(f"Linea {p.lineno(1)}: Error Semantico - La constante '{nombre_const}' no ha sido inicializada.")
    p[0] = nombre_const


# RESTO DE LA GRAMÁTICA

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

#PARTE DE TANIA

def p_expresion_unaria(p):
    '''expresion : NOT expresion'''
    pass

def p_expresion_agrupada(p):
    '''expresion : PAREN_IZQ expresion PAREN_DER'''
    pass

def p_expresion_valor_primitivo(p):
    '''expresion : INTEGER
                 | FLOAT
                 | STRING
                 | TRUE
                 | FALSE
                 | NIL'''
    pass

def p_estructura_datos(p):
    '''estructura_datos : arreglo
                        | hash
                        | rango'''
    pass

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


#PARTE DE GENESIS

def p_rango(p):
    '''rango : INTEGER RANGO INTEGER'''
    pass

def p_estructura_control(p):
    '''estructura_control : IF expresion declaraciones END
                          | IF expresion declaraciones ELSE declaraciones END
                          | WHILE expresion DO declaraciones END
                          | WHILE expresion declaraciones END
                          | FOR marcar_var IN rango declaraciones END'''
    pass

def p_parametro(p):
    '''parametro : VARIABLE_LOCAL'''
    tabla_simbolos[p[1]] = True
    p[0] = p[1]

def p_parametros(p):
    '''parametros : parametro
                  | parametro COMA parametros'''
    pass

def p_parametros_opt(p):
    '''parametros_opt : parametros
                      | empty'''
    pass


def p_declaracion_funcion(p):
    '''declaracion_funcion : DEF marcar_var PAREN_IZQ parametros_opt PAREN_DER declaraciones END
                           | DEF marcar_var declaraciones END'''
    pass

def p_llamada_funcion(p):
    '''llamada_funcion : VARIABLE_LOCAL PAREN_IZQ elementos_opt PAREN_DER
                       | RETURN expresion'''
    pass

def p_impresion(p):
    '''impresion : PUTS expresion'''
    pass

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    # Los errores de estructura ya los atrapa el sintáctico. Aquí solo evaluamos semántica.
    pass

parser = yacc.yacc()