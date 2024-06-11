import lexer 
import Interpreter

def codigo(text):
    content = text
    print(content)

    ast = lexer.parse(text)
    interpreter = Interpreter.Interpreter()
    let = interpreter
    return let  

def main():
    data = '''
    $foo = 10;
    $bar = 20;
    $baz = $foo + $bar;
    imprime $baz;
    imprime "Hola, Mundo!";
    '''
 
    lexer.lexer.input(data)
 
    ast = lexer.parse(data)
 
    if ast:
        interpreter = Interpreter.Interpreter()
        interpreter.interpret(ast)
    
if __name__ == '__main__':
    let = main()
    print(let)