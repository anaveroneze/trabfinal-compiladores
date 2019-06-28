
class Gramatica():

    palavra = None
    producoes = []
    inicial = None

    def aceitaEntrada(self, entrada):
        self.palavra = entrada
        print(self.palavra)
        #SE PALAVRA TEM SIMBOLOS Q NAO PERTENCE AO ALFABETO, SE TA VAZIO
        return 1
    
    def validaEntrada(self, inicial, producoes):
        self.inicial = inicial
        print(self.inicial)
        self.producoes = producoes
        print(self.producoes)
        return 1