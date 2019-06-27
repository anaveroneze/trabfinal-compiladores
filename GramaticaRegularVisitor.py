# Generated from GramaticaRegular.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaRegularParser import GramaticaRegularParser
else:
    from GramaticaRegularParser import GramaticaRegularParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaRegularParser.

class GramaticaRegularVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaRegularParser#gram.
    def visitGram(self, ctx:GramaticaRegularParser.GramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#naoterminais.
    def visitNaoterminais(self, ctx:GramaticaRegularParser.NaoterminaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#terminais.
    def visitTerminais(self, ctx:GramaticaRegularParser.TerminaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#simbolos.
    def visitSimbolos(self, ctx:GramaticaRegularParser.SimbolosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#simboloster.
    def visitSimboloster(self, ctx:GramaticaRegularParser.SimbolosterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#inicial.
    def visitInicial(self, ctx:GramaticaRegularParser.InicialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#producoes.
    def visitProducoes(self, ctx:GramaticaRegularParser.ProducoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#producao.
    def visitProducao(self, ctx:GramaticaRegularParser.ProducaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaRegularParser#transicao.
    def visitTransicao(self, ctx:GramaticaRegularParser.TransicaoContext):
        return self.visitChildren(ctx)



del GramaticaRegularParser