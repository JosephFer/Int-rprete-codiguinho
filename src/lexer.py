import re

class Lexer(object):
    def __init__(self, sourceCode):
        self.sourceCode = sourceCode
        self.tokens = [ 
          #palabras resevadas
          ('T_IF', r'ifisinho'),
          ('T_ELIF', r'elifsinho'),
          ('T_ELSE', r'elsinho'),
          ('T_WHILE', r'darMole'),
          ('T_BREAK', r'daStop'),
          ('T_RETURN', r'volte'),
          ('T_PRINT', r'imprime'),

          #tipos de datos, 
          ('T_ENTERO', r'intnho'),
          ('T_FLOTANTE', r'floatinho'),
          ('T_BOOL', r'boolinho'),
          ('T_CADENA', r'stringho'),
          ('T_TRUE', r'VERDA'),
          ('T_FALSE', r'FALSO'),
          ('T_VARIABLE', r'\$[a-zA-Z0-9_]+'),
          ('T_NUMERO', r"\d+"),

          #Operadores matemáticos 
          ('T_SUMA', r'\+'),
          ('T_RESTA', r'\-'),
          ('T_MULTIPLICACION', r'\*'),
          ('T_DIVISION', r"/"),
          
          #operadores logicos
          ('T_AND', r'&&'),
          ('T_OR', r'\|\|'),
          ('T_NOT', r'![a-zA-Z0-9_]+'),

          #Simbologia del lenguaje
          ('T_MAYORQUE', r'>'),
          ('T_MENORQUE', r'<'),
          ('T_MAYOROIGUAL', r'>='),
          ('T_MENOROIGUAL', r'<='),
          ('T_DIFERENTE', r'!='),
          ('T_IGUAL', r'=='),
          ('T_FINDELINEA', r';'),
          ('T_LLAVEDERECHA', r'{'),
          ('T_LLAVEIZQUIERDA', r'}'),
          ('T_PDERECHA', r'\('),
          ('T_PIZQUIERDA', r'\)'),          
          #
          ('T_ASIGNACION', r'=')
        ]

    def tokenizar(self):
        tokensEncontrados = []
        palabras = re.findall(r'\$\w+|\w+|\S', self.sourceCode)
        
        for palabra in palabras:
            for token, patron in self.tokens:
                if re.fullmatch(patron, palabra):
                    tokensEncontrados.append((palabra, token))
                    break
            else:
                # Si ninguna expresión regular coincide con la palabra, la consideramos un token desconocido
                tokensEncontrados.append((palabra, 'T_DESCONOCIDO'))

        
        return tokensEncontrados
