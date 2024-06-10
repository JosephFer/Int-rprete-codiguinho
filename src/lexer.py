import ply.lex as lex

# Definición de tokens
tokens = [
    'T_IF', 'T_ELIF', 'T_ELSE', 'T_WHILE', 'T_FOR', 'T_IN', 'T_RANK', 'T_DO','T_BREAK', 'T_RETURN', 'T_PRINT',
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
t_T_PDERECHA = r'\('
t_T_PIZQUIERDA = r'\)'
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


content = """
	boolinho $variable = verda;
    darMole ($variable) {
		$variable = falso;
        imprime("hola");
    };
    
    faca $numero in rank(0, 10, 1){
		imprime("hola);
    };
    
    $i = 0;
    facaMole {
    	imprime($i);
        $i = $i + 1;
        } darMole($i < 5);

   """

lexer.input(content)
for token in lexer:
    print(f"Token: {token.type}, Valor: {token.value}, Línea: {token.lineno}")
