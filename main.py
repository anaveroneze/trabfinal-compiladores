import sys
from antlr4 import *
from GramaticaRegularLexer import GramaticaRegularLexer
from GramaticaRegularParser import GramaticaRegularParser
from GRVisitor import GRVisitor
from Gramatica import Gramatica

def main(argv):
    entrada = FileStream(argv[1])
    lexer = GramaticaRegularLexer(entrada)
    stream = CommonTokenStream(lexer)
    parser = GramaticaRegularParser(stream)
    tree = parser.gram()

    gramaticavisitor = GRVisitor()
    gramaticavisitor.visit(tree) #classe para visitar nós de GramaticaRegularVisitor
    print("GRD lida pelo parser:")
    print(tree.toStringTree(recog=parser))

    #Definição da GRD de entrada
    print("\n--------------------")
    print("DEFINIÇÃO:\n")
    print("Símbolos não terminais: ", gramaticavisitor.naoterminais)
    print("Símbolos terminais: ", gramaticavisitor.terminais)
    print("Produções: ", gramaticavisitor.producoes)
    print("Símbolo inicial: ", gramaticavisitor.inicial)

    #Tratamento de erros sobre a gramática
    gramaticavisitor.error()    
    #Separa as produções para facilitar derivação
    print("Novo formato produções: ", gramaticavisitor.producoes)
    
    print("--------------------")
    palavra = input("Entre com uma palavra: ")
    print("\n--------------------")
        
    gramatica = Gramatica()

    # Verifica se a palavra é válida para avaliação
    if(gramatica.aceitaEntrada(palavra, gramaticavisitor.terminais, gramaticavisitor.producoes)):
        #Verifica se a palavra pertence a GRD
        if(gramatica.validaEntrada(gramaticavisitor.inicial, '')):
            print("\nPalavra faz parte da gramática.")
        else:
            print("\nPalavra NÃO faz parte da gramática.")

if __name__ == '__main__':
    main(sys.argv)