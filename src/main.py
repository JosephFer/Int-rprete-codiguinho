from lexer import lexer
from parser_1 import parser
from Interpreter import Interpreter


def main():
    # Código de ejemplo en codiguinho
    code = """
    $a = 1;
    $b = 2;
    $c = $a + $b;
    imprime($c);
    """

    # Tokenización y parseo
    lexer.input(code)
    ast = parser.parse(code, lexer=lexer)
    
    # Interpretación del AST
    interpreter = Interpreter()
    interpreter.interpret(ast)

if __name__ == "__main__":
    main()


