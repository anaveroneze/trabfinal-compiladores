
class Gramatica():

    palavra = None
    producoes = {}
    derivacao = ''
    terminais = ''
    inicial = None

    def aceitaEntrada(self, entrada, terminais, producoes):
        self.palavra = entrada

        # Verifica se a palavra de entrada tem caracteres que não são letras (necessário?)
        if self.palavra.isalpha() == False:
            print("ERRO: Palavra inválida. Não contém apenas letras.")
            return 0
        
        # Verifica se a palavra contém apenas caracteres definidos nos terminais
        for c in self.palavra:
            if c not in terminais:
                print("ERRO: Palavra inválida. Contém caracteres que não pertencem a lista de terminais.")
                return 0

        self.palavra = self.palavra + "$"
        self.producoes = producoes
        self.terminais = terminais
        return 1
    
    # Busca a produção, dentro da lista de produções, que pode ser aplicada no estado atual da derivação
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

        #Não encontrou nenhuma produção para aplicar
        return 0

    def validaEntrada(self, inicial, entrada):

        #Caso de aceitação: 
        #Percorreu toda a palavra, gerou uma produção terminando em símbolo terminal e palavras são iguais.
        if (inicial == '#') and (self.palavra[:-1] == entrada[:-1]):
            print("Palavra:", self.palavra, '\tGerada:', entrada)
            return 1

        empilha = self.busca_producao(inicial, entrada)
        #Imprime passo a passo os movimentos entre símbolos não terminais
        print("Palavra:", self.palavra, '\tGerada:', entrada, '\tInicial:', inicial,'\tDeriva em:', empilha)

        if(empilha):            
            #Desempilha não terminal
            entrada = entrada[:-1]
            #Empilha nova derivacao
            entrada = entrada + empilha
            #Define o novo símbolo não terminal
            inicial = empilha[-1:]
            
            #Palavra aceita!
            if(self.validaEntrada(inicial, entrada) == 1):
                return 1
        #Palavra inválida!
        else:
            pos = len(entrada)-1
            print("\nERRO: posição", pos ,"da palavra - esperado:", self.palavra[pos], " encontrado:", entrada[-1])
            return 0

        return 0