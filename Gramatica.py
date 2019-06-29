
class Gramatica():

    palavra = None
    producoes = {}
    derivacao = ''
    terminais = ''
    inicial = None

    def aceitaEntrada(self, entrada, terminais, producoes):
        self.palavra = entrada

        if self.palavra.isalpha() == False:
            print("ERRO: Palavra inválida. Contém caracteres não alfanuméricos.")
            return 0
        
        for c in self.palavra:
            if c not in terminais:
                print("ERRO: Palavra inválida. Contém caracteres que não pertencem a lista de terminais.")
                return 0

        self.palavra = self.palavra + "$"
        self.producoes = producoes
        self.terminais = terminais
        return 1
    
    def busca_producao(self, inicial, entrada):
        #Verifica se a produção pode ser aplicada
        for prod in self.producoes:
            if prod.startswith('('+inicial+'>'):
                #Pega info da nova derivação
                empilha = prod[prod.find(">")+1:prod.find(")")]
                #Verifica se a derivação pode ser aplicada - se é prefixo da palavra 
                nova_prod = entrada[:-1] + empilha[:-1]
                if self.palavra.startswith(nova_prod):
                    #Verifica se elas vão ter o mesmo tamanho se o terminal deriva em #
                    # print("Palavra:", self.palavra, "\tProdução", entrada,"\t", inicial, " > ", empilha)
                    if len(self.palavra) != len(entrada):                        
                        if(empilha in self.terminais):
                            return empilha + '#'
                        else:
                            return empilha
                    elif (len(self.palavra) == len(entrada)) and (empilha == '#'):
                        return empilha

        #não encontrou nenhuma produção para aplicar
        return 0

    def validaEntrada(self, inicial, entrada):

        print("Palavra:", self.palavra, '\tInicial:', inicial, '\tProdução:', entrada,'\n')

        #caso de aceitação: percorreu toda a palavra, gerou uma producao terminando em terminal e são iguais... aceita!
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
            pos = len(entrada)-1 
            print("ERRO: posição", pos ,"da palavra - esperado:", self.palavra[pos-1], " encontrado:", entrada[pos-1])
            return 0

        return 0