
class Gramatica():

    palavra = None
    producoes = {}
    derivacao = ''
    inicial = None

    def aceitaEntrada(self, entrada, terminais, producoes):
        self.palavra = entrada

        if self.palavra.isalpha() == False:
            return 0
        
        for c in self.palavra:
            if c not in terminais:
                return 0

        self.palavra = self.palavra + "$"
        self.producoes = producoes

        return 1
    
    def busca_producao(self, inicial, entrada):
        #Verifica se a produção pode ser aplicada
        for prod in self.producoes:
            if prod.startswith('('+inicial+'>'):
                #Pega info da nova derivação
                empilha = prod[prod.find(">")+1:prod.find(")")]
                #Verifica se a derivação pode ser aplicada - se é prefixo da palavra 
                if self.palavra.startswith(entrada[:-1] + empilha[:-1]):
                    return empilha

        #não encontrou nenhuma produção para aplicar
        return 0

    def validaEntrada(self, inicial, entrada):

        print("Palavra:", self.palavra, '\tInicial:', inicial, '\tEntrada:', entrada,'\n')

        #caso de aceitação: percorreu toda a palavra
        if (inicial == '#') and (self.palavra[:-1] == entrada[:-1]):
            return 1

        empilha = self.busca_producao(inicial, entrada)

        if(empilha):            
            #Desempilha não terminal antigo
            entrada = entrada[:-1]
            # print("Derivação antes:", entrada)

            #Empilha novo não terminal
            entrada = entrada + empilha
            inicial = empilha[-1:]
            # print("Novo inicial:", inicial)
            # print("Derivação depois:", entrada)

            if(self.validaEntrada(inicial, entrada) == 1):
                return 1

        else:
            return 0


        # if(self.validaEntrada(inicial, entrada))
        # while()
        # self.inicial = inicial
        # print(self.inicial)
        # self.producoes = producoes
        # print(self.producoes)
        return 0