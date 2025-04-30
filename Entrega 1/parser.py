
import ply.yacc as yacc
from scanner import tokens 

# --- Definición de Precedencia de Operadores ---
# Menor precedencia a mayor precedencia
precedence = (
    ('left', 'REL_OP'),          # Nivel más bajo: ==, !=, <, >
    ('left', 'PLUS', 'MINUS'),   # Nivel medio: +, -
    ('left', 'MULTIPLY', 'DIVIDE'), # Nivel más alto: *, /
)

# --- Reglas del Parser ---

# Estructura general del programa
def p_program(p):
    '''program : PROGRAM IDENTIFIER SEMICOLON vars_opt funcs_opt MAIN body END'''
    print("Programa válido")
    p[0] = ("program", p[2], p[4], p[5], p[7]) # Ejemplo simple de resultado

# Secciones opcionales
def p_vars_opt(p):
    '''vars_opt : vars
                | empty'''
    p[0] = p[1]

def p_funcs_opt(p):
    '''funcs_opt : funcs
                 | empty'''
    p[0] = p[1]

# Declaración de variables
def p_vars(p):
    '''vars : VAR var_declaration_list'''
    p[0] = ("vars", p[2])

def p_var_declaration_list(p):
    '''var_declaration_list : IDENTIFIER COLON type SEMICOLON var_declaration_list
                            | IDENTIFIER COLON type SEMICOLON'''
    # Construye una lista de tuplas (nombre, tipo)
    if len(p) == 6:
         p[0] = [(p[1], p[3])] + p[5]
    else: # Caso base (última o única declaración)
        p[0] = [(p[1], p[3])]

# Tipos de datos
def p_type(p):
    '''type : INT
            | FLOAT'''
    p[0] = p[1] # Solo retorna 'int' o 'float'

# Funciones (placeholder por ahora)
def p_funcs(p):
    '''funcs : empty''' # Expandir en el futuro
    p[0] = ("funcs", [])

# Cuerpo principal o de función
def p_body(p):
    '''body : LBRACE statement_list RBRACE'''
    p[0] = ("body", p[2])

# Lista de statements (puede estar vacía)
def p_statement_list(p):
    '''statement_list : statement statement_list
                      | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2] # Agrega el statement actual a la lista recursiva
    else:
        p[0] = [] # Lista vacía

# Tipos de statements (expandir con IF, WHILE, etc.)
def p_statement(p):
    '''statement : assign
                 | print_stmt
                 | if_stmt'''
              # | condition
             # | cycle
            # | f_call '''
    p[0] = p[1]

def p_if_stmt(p):
    '''if_stmt : IF LPAREN expresion RPAREN body'''
    p[0] = ('if', p[3], p[5])

# Asignación
def p_assign(p):
    '''assign : IDENTIFIER ASSIGN expresion SEMICOLON'''
    p[0] = ("assign", p[1], p[3])

# Escritura (Print)
def p_print_stmt(p):
    '''print_stmt : PRINT LPAREN expresion RPAREN SEMICOLON'''
    p[0] = ("print", p[3])

# --- GRAMÁTICA DE EXPRESIONES (Basada en tu PDF y usando precedencia) ---

def p_expresion(p):
    '''expresion : exp REL_OP exp
                 | exp'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3]) # Operador, Izquierda, Derecha
    else:
        p[0] = p[1]

def p_exp(p):
    '''exp : exp PLUS termino
           | exp MINUS termino
           | termino'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3]) # Operador, Izquierda, Derecha
    else:
        p[0] = p[1]

def p_termino(p):
    '''termino : termino MULTIPLY factor
               | termino DIVIDE factor
               | factor'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3]) # Operador, Izquierda, Derecha
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | PLUS constante
              | MINUS constante
              | constante
              | IDENTIFIER'''
    if len(p) == 4: # Paréntesis
        p[0] = p[2]
    elif len(p) == 3: # Signo opcional para constantes
        p[0] = (p[1], p[2]) # ('+', cte) o ('-', cte)
    else: # Constante sola o Identificador
        p[0] = p[1]

def p_constante(p):
    '''constante : CTE_INT
                 | CTE_FLOAT
                 | CTE_STRING'''
    p[0] = ('const', p[1]) # Marcar como constante con su valor

# Regla vacía (epsilon)
def p_empty(p):
    '''empty :'''
    p[0] = None # O [] dependiendo de cómo lo uses

# Manejo de errores de sintaxis


def p_error(p):
    if p:
        print(f"ERROR DE SINTAXIS: Token inesperado '{p.value}' (Tipo: {p.type}) en línea {p.lineno}")
    else:
        print("ERROR DE SINTAXIS: Fin inesperado del archivo (EOF)")
    raise SyntaxError  



# Construcción del parser
parser = yacc.yacc()