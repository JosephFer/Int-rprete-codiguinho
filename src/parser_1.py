import ply.yacc as yacc
from lexer import tokens, lexer

# Precedencia de operadores 
precedence = (
    ('left', 'T_SUMA', 'T_RESTA'),
    ('left', 'T_MULTIPLICACION', 'T_DIVISION'),
    ('left', 'T_MAYORQUE', 'T_MENORQUE', 'T_MAYOROIGUAL', 'T_MENOROIGUAL', 'T_IGUAL', 'T_DIFERENTE'),
    ('left', 'T_AND', 'T_OR'),
    ('right', 'T_NOT'),
)

# Definición de la gramática

def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : expression T_FINDELINEA
                 | assignment T_FINDELINEA
                 | declaration T_FINDELINEA
                 | conditional T_FINDELINEA
                 | loop_while T_FINDELINEA
                 | loop_for T_FINDELINEA
                 | loop_do_while T_FINDELINEA
                 | function_declaration T_FINDELINEA
                 | return_statement T_FINDELINEA
                 | break_statement T_FINDELINEA
                 | statement_print T_FINDELINEA'''
    p[0] = p[1]

def p_expression(p):
    '''expression : term
                  | expression T_SUMA term
                  | expression T_PDERECHA term
                  | expression T_PIZQUIERDA term
                  | expression T_RESTA term
                  | expression T_MULTIPLICACION term
                  | expression T_DIVISION term
                  | expression T_MAYORQUE expression
                  | expression T_MENORQUE expression
                  | expression T_MAYOROIGUAL expression
                  | expression T_MENOROIGUAL expression
                  | expression T_IGUAL expression
                  | expression T_DIFERENTE expression
                  | T_NOT expression
                  | expression T_AND expression
                  | expression T_OR expression'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = int(p[1]) * int(p[3])
    elif p[2] == '/':
        p[0] = int(p[1]) / int(p[3])
    
    elif len(p) == 4 and p[2] == '<':  # Verificar la longitud de p y la operación
        if p[1] < p[3]:
            p[0] = True
        else:
            p[0] = False
        
    elif len(p) == 4 and p[2] == '>':  
        if p[1] > p[3]:
            p[0] = True
        else:
            p[0] = False
    
    elif len(p) == 4 and p[2] == '<=':  
        if p[1] <= p[3]:
            p[0] = True
        else:
            p[0] = False
    
    elif len(p) == 4 and p[2] == '>=':  
        if p[1] >= p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == "AND":
        p[0] = p[1] and p[3]

    elif p[2] == "OR":
        p[0] = p[1] or p[3]
    elif p[2] == "NOT":
        p[0] =  p[1] is not p[3]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term(p):
    '''term : T_NUMERO
            | T_VARIABLE
            | T_TRUE
            | T_FALSE
            | T_STRING
            | rank_function'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : T_VARIABLE T_ASIGNACION expression'''
    p[0] = ('assign', p[1], p[3])

def p_declaration(p):
    '''declaration : T_ENTERO assignment
                   | T_FLOTANTE assignment
                   | T_BOOL assignment
                   | T_CADENA assignment
                   | T_ENTERO T_VARIABLE
                   | T_FLOTANTE T_VARIABLE
                   | T_BOOL T_VARIABLE
                   | T_CADENA T_VARIABLE'''
    p[0] = ('declare', p[1], p[2])

def p_conditional(p):
    '''conditional : T_IF T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA
                   | T_IF T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA T_ELSE T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA'''
    if len(p) == 8:
        p[0] = ('conditional', 'if', p[3], p[6])
    else:
        p[0] = ('conditional', 'if', p[3], p[6], 'else', p[10])


def p_loop_while(p):
    '''loop_while : T_WHILE T_PDERECHA expression T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA'''
    p[0] = ('loop', p[3], p[6])

def p_rank_function(p):
    '''rank_function : T_RANK T_PDERECHA expression T_COMA expression T_COMA expression T_PIZQUIERDA'''
    p[0] = ('rank', p[3], p[5], p[7])

def p_loop_for(p):
    '''loop_for : T_FOR T_VARIABLE T_IN rank_function T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA'''
    p[0] = ('for', p[2], p[4], p[6])

def p_loop_do_while(p):
    '''loop_do_while : T_DO T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA T_WHILE T_PDERECHA expression T_PIZQUIERDA'''
    p[0] = ('do-while', p[3], p[7])

def p_parameter_list(p):
    '''parameter_list : T_VARIABLE
                      | parameter_list T_COMA T_VARIABLE'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_function_declaration(p):
    '''function_declaration : T_FUNCION T_PDERECHA parameter_list T_PIZQUIERDA T_LLAVEIZQUIERDA statement_list T_LLAVEDERECHA'''
    p[0] = ('Funcion', p[3], p[6])

#ver
def p_return_statement(p):
    '''return_statement : T_RETURN expression
                        | T_RETURN'''
    if len(p) == 3:
        p[0] = ('return', p[2])
    else:
        p[0] = ('return', None)

def p_statement_print(p):
    '''statement_print : T_PRINT T_PDERECHA expression T_PIZQUIERDA'''
    p[0] = ('Imprimir', p[3])

#ver
def p_break_statement(p):
    '''break_statement : T_BREAK'''
    p[0] = 'break'

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")


# Construcción del parser
parser = yacc.yacc()

# Función para parsear el código
def parse_code(code):
    lexer.input(code)
    return parser.parse(code, lexer=lexer)

if __name__ == "__main__":
    content = """
    $x = 10;
    $a = 5;
    $c = $x + $a;
    imprime($c);
    """
    prueba = parse_code(content)
    print(prueba)