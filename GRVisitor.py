from antlr4 import *
from GramaticaRegularParser import GramaticaRegularParser
from GramaticaRegularVisitor import GramaticaRegularVisitor

class GRVisitor(GramaticaRegularVisitor):

    naoterminais = []
    terminais = []
    producoes = []
    inicial = None
    erros = []

    # Visit a parse tree produced by GramaticaRegularParser#gram.
    def visitGram(self, ctx:GramaticaRegularParser.GramContext):
        # print("Iniciando a visita da gramática!")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#naoterminais.
    def visitNaoterminais(self, ctx:GramaticaRegularParser.NaoterminaisContext):
        self.naoterminais = ctx.simbolos().getText().replace(' ', '').split(',')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#terminais.
    def visitTerminais(self, ctx:GramaticaRegularParser.TerminaisContext):
        self.terminais = ctx.simboloster().getText().replace(' ', '').split(',')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#simbolos.
    def visitSimbolos(self, ctx:GramaticaRegularParser.SimbolosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#simboloster.
    def visitSimboloster(self, ctx:GramaticaRegularParser.SimbolosterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#inicial.
    def visitInicial(self, ctx:GramaticaRegularParser.InicialContext):
        self.inicial = ctx.VAR().getText()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#producoes.
    def visitProducoes(self, ctx:GramaticaRegularParser.ProducoesContext):
        self.producoes = ctx.producao().getText().replace(' ', '').split(',')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#producao.
    def visitProducao(self, ctx:GramaticaRegularParser.ProducaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#transicao.
    def visitTransicao(self, ctx:GramaticaRegularParser.TransicaoContext):
        return self.visitChildren(ctx)

    # Função para tratamento de erros da gramática
    def error(self):
        
        print("\n--------------------")
        
        # Símbolo inicial não é único, não está declarado na lista de não-terminais, não está declarado.
        if len(self.inicial) > 1:
            print("ERRO: Símbolo inicial", self.inicial, "não é um único caractere não-terminal.")
        if self.inicial not in self.naoterminais:
            print("ERRO: Símbolo inicial", self.inicial, "não declarado como não-terminal.")
        if self.inicial == None:
            print("ERRO: Nenhum símbolo inicial foi declarado.")

        # Simbolo duplicado na lista de terminais
        self.terminais.sort()
        for i in range(len(self.terminais)-1):
            if(self.terminais[i] == self.terminais[i+1]):
                print("ERRO: Símbolo ", self.terminais[i] ,"duplicado na lista de terminais.")
        
        # Simbolo duplicado na lista de não terminais
        self.naoterminais.sort()
        for i in range(len(self.naoterminais)-1):
            if(self.naoterminais[i] == self.naoterminais[i+1]):
                print("ERRO: Símbolo ", self.naoterminais[i] ,"duplicado na lista de não terminais.")
        
        
        #Separa todas produções separadas por pipe:
        bk_producoes = []
        bk_producoes = self.producoes
        self.producoes = []
        
        for producao in bk_producoes:
            if '|' not in producao: 
                self.producoes.append(producao)
            else:
                simb_esq = producao[producao.find("(")+1:producao.find(">")]
                P1 = ""
                for i in producao[producao.find(">")+1:producao.find(")")]:
                    if i == '|':
                        P = "(" + simb_esq + ">" + P1 + ")"
                        self.producoes.append(P)
                        P1 = ""
                    else:
                        P1 = P1+i
                P = "(" + simb_esq + ">" + P1 + ")"
                self.producoes.append(P)

        #Produção com simbolos não definidos
        for producao in self.producoes:
            simb_esq = producao[producao.find("(")+1:producao.find(">")]
            simb_dir = producao[producao.find(">")+1:producao.find(")")]

            if simb_esq not in self.naoterminais:
                print("ERRO: Símbolo ", simb_esq ,"a esquerda da produção não está definido nos não terminais.")
            
            for char in simb_dir:
                if (char not in self.terminais) and (char not in self.naoterminais) and (char != '#'):
                    print("ERRO: Símbolo ", char ,"a direita da produção não está definido.")
        