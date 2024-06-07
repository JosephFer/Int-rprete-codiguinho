
import src.lexer

def codigo(text):
    content = text
    print(content)

    #Lexer 
    lex = src.lexer.Lexer(content)

    tokens = lex.tokenizar()
    let = ""
    
    for token in tokens:
        let += "Lexema: " + token[0] + ' --> ' + "Token: " +token[1] + "\n"
        if token[1] == 'T_FINDELINEA':
            let += "\n"
    let += "\n"  
    return let   
