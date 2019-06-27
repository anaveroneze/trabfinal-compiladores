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


    def error(self):
        
        print("\n--------------------")
        print("ERROS:\n")
        
        # Símbolo inicial não é único, não está declarado na lista de não-terminais, não está declarado.
        if len(self.inicial) > 1:
            print("Símbolo inicial", self.inicial, "não é um único caractere não-terminal.")
        if self.inicial not in self.naoterminais:
            print("Símbolo inicial", self.inicial, "não declarado como não-terminal.")
        if self.inicial == None:
            print("Nenhum símbolo inicial foi declarado.")

        # Simbolo duplicado na lista de terminais
        
        # Simbolo duplicado na lista de não terminais


        # for producao in self.producoes:
        #     print(producao)
        