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
    gramaticavisitor.visit(tree) 
    #classe para visitar nós de GramaticaRegularVisitor
    # 1 - processar essa string tree e printar bonitinha a definição do autômato
    print("Lida pelo parser:")
    print(tree.toStringTree(recog=parser))

    print("\n--------------------")
    print("GRAMATICA REGULAR:\n")
    print("Símbolos terminais: ", gramaticavisitor.naoterminais)
    print("Símbolos não terminais: ", gramaticavisitor.terminais)
    print("Produções: ", gramaticavisitor.producoes)
    print("Símbolo inicial: ", gramaticavisitor.inicial)

    # 2 - fazer o tratamento de erros
    gramaticavisitor.error()    
    print("Novas produções: ", gramaticavisitor.producoes)
    
    print("\n--------------------")
    palavra = input("Entre com uma palavra: ")
    print("\n--------------------")
        
    gramatica = Gramatica()

    # Verifica se a palavra é válida para avaliação
    if(gramatica.aceitaEntrada(palavra, gramaticavisitor.terminais, gramaticavisitor.producoes)):
        #Verifica se a palavra pertence a GRD
        if(gramatica.validaEntrada(gramaticavisitor.inicial, '')):
            print("Palavra faz parte da gramática.")
        else:
            print("Palavra NÃO faz parte da gramática.")

if __name__ == '__main__':
    main(sys.argv)