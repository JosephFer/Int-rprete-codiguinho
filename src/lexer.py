import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = [
    'T_IF', 'T_ELIF', 'T_ELSE', 'T_WHILE', 'T_FOR', 'T_IN', 'T_RANK', 'T_DO', 'T_BREAK', 'T_RETURN', 'T_PRINT',
    'T_ENTERO', 'T_FLOTANTE', 'T_BOOL', 'T_CADENA', 'T_TRUE', 'T_FALSE',
    'T_VARIABLE', 'T_NUMERO', 'T_SUMA', 'T_RESTA', 'T_MULTIPLICACION', 'T_DIVISION',
    'T_AND', 'T_OR', 'T_NOT', 'T_MAYORQUE', 'T_MENORQUE', 'T_MAYOROIGUAL', 'T_MENOROIGUAL',
    'T_DIFERENTE', 'T_IGUAL', 'T_ASIGNACION', 'T_COMA', 'T_FINDELINEA', 'T_LLAVEDERECHA',
    'T_LLAVEIZQUIERDA', 'T_PDERECHA', 'T_PIZQUIERDA', 'T_STRING', 'T_FUNCION'
]

# Definición de las expresiones regulares para los tokens
t_T_IF = r'ifisinho'
t_T_ELIF = r'elifsinho'
t_T_ELSE = r'elsinho'
t_T_WHILE = r'darMole'
t_T_FOR = r'faca'
t_T_IN = r'in'
t_T_RANK = r'rank'
t_T_DO = r'facaMole'
t_T_BREAK = r'daStop'
t_T_RETURN = r'volte'
t_T_PRINT = r'imprime'
t_T_ENTERO = r'intnho'
t_T_FLOTANTE = r'floatinho'
t_T_BOOL = r'boolinho'
t_T_CADENA = r'stringho'
t_T_TRUE = r'verda'
t_T_FALSE = r'falso'
t_T_VARIABLE = r'\$[a-zA-Z0-9_]+'
t_T_NUMERO = r'\d+'
t_T_SUMA = r'\+'
t_T_RESTA = r'-'
t_T_MULTIPLICACION = r'\*'
t_T_DIVISION = r'/'
t_T_AND = r'AND'
t_T_OR = r'OR'
t_T_NOT = r'NOT'
t_T_MAYORQUE = r'>'
t_T_MENORQUE = r'<'
t_T_MAYOROIGUAL = r'>='
t_T_MENOROIGUAL = r'<='
t_T_DIFERENTE = r'!='
t_T_IGUAL = r'=='
t_T_ASIGNACION = r'='
t_T_COMA = r','
t_T_FINDELINEA = r';'
t_T_LLAVEDERECHA = r'}'
t_T_LLAVEIZQUIERDA = r'{'
t_T_PDERECHA = r'\)'
t_T_PIZQUIERDA = r'\('
t_T_STRING = r'\".*?\"'
t_T_FUNCION = r'\#[a-zA-Z_][a-zA-Z0-9_]*'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Definición del parser
precedence = (
    ('left', 'T_OR'),
    ('left', 'T_AND'),
    ('left', 'T_NOT'),
    ('left', 'T_MAYORQUE', 'T_MENORQUE', 'T_MAYOROIGUAL', 'T_MENOROIGUAL', 'T_IGUAL', 'T_DIFERENTE'),
    ('left', 'T_SUMA', 'T_RESTA'),
    ('left', 'T_MULTIPLICACION', 'T_DIVISION'),
)

def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assign_statement
                 | print_statement
                 | if_statement
                 | while_statement
                 | for_statement
                 | do_while_statement
                 | function_definition
                 | function_call'''
    p[0] = p[1]

def p_assign_statement(p):
    '''assign_statement : T_VARIABLE T_ASIGNACION expression T_FINDELINEA'''
    p[0] = ('assign', p[1], p[3])

def p_print_statement(p):
    '''print_statement : T_PRINT expression T_FINDELINEA'''
    p[0] = ('Imprimir', p[2])

def p_if_statement(p):
    '''if_statement : T_IF T_PIZQUIERDA expression T_PDERECHA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA else_clause'''
    p[0] = ('if', p[3], p[6], p[8])

def p_else_clause(p):
    '''else_clause : T_ELIF T_PIZQUIERDA expression T_PDERECHA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA else_clause
                   | T_ELSE T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA
                   | empty'''
    if len(p) == 8:
        p[0] = ('elif', p[3], p[6], p[8])
    elif len(p) == 5:
        p[0] = ('else', p[3])
    else:
        p[0] = None

def p_while_statement(p):
    '''while_statement : T_WHILE T_PIZQUIERDA expression T_PDERECHA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA'''
    p[0] = ('while', p[3], p[6])

def p_for_statement(p):
    '''for_statement : T_FOR T_PIZQUIERDA assign_statement expression T_FINDELINEA assign_statement T_PDERECHA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA'''
    p[0] = ('for', p[3], p[4], p[6], p[9])

def p_do_while_statement(p):
    '''do_while_statement : T_DO T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA T_WHILE T_PIZQUIERDA expression T_PDERECHA T_FINDELINEA'''
    p[0] = ('do_while', p[3], p[7])

def p_function_definition(p):
    '''function_definition : T_FUNCION T_VARIABLE T_PIZQUIERDA parameters T_PDERECHA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA'''
    p[0] = ('function', p[2], p[4], p[7])

def p_function_call(p):
    '''function_call : T_VARIABLE T_PIZQUIERDA arguments T_PDERECHA T_FINDELINEA'''
    p[0] = ('function_call', p[1], p[3])

def p_parameters(p):
    '''parameters : T_VARIABLE
                  | parameters T_COMA T_VARIABLE
                  | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = []

def p_arguments(p):
    '''arguments : expression
                 | arguments T_COMA expression
                 | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = []

def p_expression_binop(p):
    '''expression : expression T_SUMA expression
                  | expression T_RESTA expression
                  | expression T_MULTIPLICACION expression
                  | expression T_DIVISION expression
                  | expression T_MAYORQUE expression
                  | expression T_MENORQUE expression
                  | expression T_MAYOROIGUAL expression
                  | expression T_MENOROIGUAL expression
                  | expression T_IGUAL expression
                  | expression T_DIFERENTE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_number(p):
    '''expression : T_NUMERO'''
    p[0] = ('Num', int(p[1]))

def p_expression_variable(p):
    '''expression : T_VARIABLE'''
    p[0] = ('Var', p[1])

def p_expression_string(p):
    '''expression : T_STRING'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def parse(data):
    return parser.parse(data)

