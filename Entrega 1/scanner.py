import ply.lex as lex

# Lista de tokens basada en tu definición previa
tokens = [
    'IDENTIFIER', 'CTE_INT', 'CTE_FLOAT', 'CTE_STRING', 'ASSIGN',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'REL_OP',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'COMMA', 'SEMICOLON', 'COLON',
    'PROGRAM', 'MAIN', 'END', 'INT', 'FLOAT', 'VOID',
    'IF', 'ELSE', 'WHILE', 'DO', 'PRINT', 'VAR'
]

# Palabras reservadas
reserved = {
    'program': 'PROGRAM',
    'main': 'MAIN',
    'end': 'END',
    'int': 'INT',
    'float': 'FLOAT',
    'void': 'VOID',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'print': 'PRINT',
    'var': 'VAR'
}

# Definición de expresiones regulares
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_REL_OP = r'(==|!=|<|>)' 
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Constantes
def t_CTE_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f"Float value too large {t.value}")
        t.value = 0.0
    return t

def t_CTE_INT(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Integer value too large {t.value}")
        t.value = 0
    return t

t_CTE_STRING = r'"[^"]*"' # Simplificado: Asume que no hay comillas dobles dentro del string

# Contar líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabs
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()