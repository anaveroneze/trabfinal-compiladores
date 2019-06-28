# Generated from GramaticaRegular.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\5\5+\n\5\3\6\3\6\3\6\3\6\5\6\61\n\6\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\tG\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nP\n\n")
        buf.write("\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2M\2\24\3\2\2\2\4")
        buf.write("\36\3\2\2\2\6\"\3\2\2\2\b*\3\2\2\2\n\60\3\2\2\2\f\62\3")
        buf.write("\2\2\2\16\65\3\2\2\2\20F\3\2\2\2\22O\3\2\2\2\24\25\7\3")
        buf.write("\2\2\25\26\5\4\3\2\26\27\7\4\2\2\27\30\5\6\4\2\30\31\7")
        buf.write("\5\2\2\31\32\5\16\b\2\32\33\7\6\2\2\33\34\5\f\7\2\34\35")
        buf.write("\7\2\2\3\35\3\3\2\2\2\36\37\7\7\2\2\37 \5\b\5\2 !\7\b")
        buf.write("\2\2!\5\3\2\2\2\"#\7\7\2\2#$\5\n\6\2$%\7\b\2\2%\7\3\2")
        buf.write("\2\2&\'\7\20\2\2\'(\7\t\2\2(+\5\b\5\2)+\7\20\2\2*&\3\2")
        buf.write("\2\2*)\3\2\2\2+\t\3\2\2\2,-\7\21\2\2-.\7\t\2\2.\61\5\n")
        buf.write("\6\2/\61\7\21\2\2\60,\3\2\2\2\60/\3\2\2\2\61\13\3\2\2")
        buf.write("\2\62\63\7\n\2\2\63\64\7\20\2\2\64\r\3\2\2\2\65\66\7\7")
        buf.write("\2\2\66\67\5\20\t\2\678\7\b\2\28\17\3\2\2\29:\7\13\2\2")
        buf.write(":;\7\20\2\2;<\7\f\2\2<=\5\22\n\2=>\7\r\2\2>G\3\2\2\2?")
        buf.write("@\7\13\2\2@A\7\20\2\2AB\7\f\2\2BC\5\22\n\2CD\7\16\2\2")
        buf.write("DE\5\20\t\2EG\3\2\2\2F9\3\2\2\2F?\3\2\2\2G\21\3\2\2\2")
        buf.write("HI\7\21\2\2IJ\7\20\2\2JK\7\17\2\2KP\5\22\n\2LM\7\21\2")
        buf.write("\2MP\7\20\2\2NP\7\22\2\2OH\3\2\2\2OL\3\2\2\2ON\3\2\2\2")
        buf.write("P\23\3\2\2\2\6*\60FO")
        return buf.getvalue()


class GramaticaRegularParser ( Parser ):

    grammarFileName = "GramaticaRegular.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'V '", "'T '", "'P '", "'S '", "'= ['", 
                     "']'", "', '", "'= '", "'('", "'>'", "')'", "'), '", 
                     "'|'", "<INVALID>", "<INVALID>", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "VAR", "VAR_T", "VAZIO", 
                      "WS" ]

    RULE_gram = 0
    RULE_naoterminais = 1
    RULE_terminais = 2
    RULE_simbolos = 3
    RULE_simboloster = 4
    RULE_inicial = 5
    RULE_producoes = 6
    RULE_producao = 7
    RULE_transicao = 8

    ruleNames =  [ "gram", "naoterminais", "terminais", "simbolos", "simboloster", 
                   "inicial", "producoes", "producao", "transicao" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    VAR=14
    VAR_T=15
    VAZIO=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class GramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def naoterminais(self):
            return self.getTypedRuleContext(GramaticaRegularParser.NaoterminaisContext,0)


        def terminais(self):
            return self.getTypedRuleContext(GramaticaRegularParser.TerminaisContext,0)


        def producoes(self):
            return self.getTypedRuleContext(GramaticaRegularParser.ProducoesContext,0)


        def inicial(self):
            return self.getTypedRuleContext(GramaticaRegularParser.InicialContext,0)


        def EOF(self):
            return self.getToken(GramaticaRegularParser.EOF, 0)

        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_gram

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGram" ):
                return visitor.visitGram(self)
            else:
                return visitor.visitChildren(self)




    def gram(self):

        localctx = GramaticaRegularParser.GramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gram)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(GramaticaRegularParser.T__0)
            self.state = 19
            self.naoterminais()
            self.state = 20
            self.match(GramaticaRegularParser.T__1)
            self.state = 21
            self.terminais()
            self.state = 22
            self.match(GramaticaRegularParser.T__2)
            self.state = 23
            self.producoes()
            self.state = 24
            self.match(GramaticaRegularParser.T__3)
            self.state = 25
            self.inicial()
            self.state = 26
            self.match(GramaticaRegularParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NaoterminaisContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simbolos(self):
            return self.getTypedRuleContext(GramaticaRegularParser.SimbolosContext,0)


        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_naoterminais

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNaoterminais" ):
                return visitor.visitNaoterminais(self)
            else:
                return visitor.visitChildren(self)




    def naoterminais(self):

        localctx = GramaticaRegularParser.NaoterminaisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_naoterminais)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(GramaticaRegularParser.T__4)
            self.state = 29
            self.simbolos()
            self.state = 30
            self.match(GramaticaRegularParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminaisContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simboloster(self):
            return self.getTypedRuleContext(GramaticaRegularParser.SimbolosterContext,0)


        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_terminais

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminais" ):
                return visitor.visitTerminais(self)
            else:
                return visitor.visitChildren(self)




    def terminais(self):

        localctx = GramaticaRegularParser.TerminaisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_terminais)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(GramaticaRegularParser.T__4)
            self.state = 33
            self.simboloster()
            self.state = 34
            self.match(GramaticaRegularParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimbolosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GramaticaRegularParser.VAR, 0)

        def simbolos(self):
            return self.getTypedRuleContext(GramaticaRegularParser.SimbolosContext,0)


        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_simbolos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimbolos" ):
                return visitor.visitSimbolos(self)
            else:
                return visitor.visitChildren(self)




    def simbolos(self):

        localctx = GramaticaRegularParser.SimbolosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simbolos)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(GramaticaRegularParser.VAR)
                self.state = 37
                self.match(GramaticaRegularParser.T__6)
                self.state = 38
                self.simbolos()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(GramaticaRegularParser.VAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimbolosterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_T(self):
            return self.getToken(GramaticaRegularParser.VAR_T, 0)

        def simboloster(self):
            return self.getTypedRuleContext(GramaticaRegularParser.SimbolosterContext,0)


        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_simboloster

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimboloster" ):
                return visitor.visitSimboloster(self)
            else:
                return visitor.visitChildren(self)




    def simboloster(self):

        localctx = GramaticaRegularParser.SimbolosterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simboloster)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(GramaticaRegularParser.VAR_T)
                self.state = 43
                self.match(GramaticaRegularParser.T__6)
                self.state = 44
                self.simboloster()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(GramaticaRegularParser.VAR_T)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InicialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GramaticaRegularParser.VAR, 0)

        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_inicial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicial" ):
                return visitor.visitInicial(self)
            else:
                return visitor.visitChildren(self)




    def inicial(self):

        localctx = GramaticaRegularParser.InicialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inicial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(GramaticaRegularParser.T__7)
            self.state = 49
            self.match(GramaticaRegularParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProducoesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def producao(self):
            return self.getTypedRuleContext(GramaticaRegularParser.ProducaoContext,0)


        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_producoes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProducoes" ):
                return visitor.visitProducoes(self)
            else:
                return visitor.visitChildren(self)




    def producoes(self):

        localctx = GramaticaRegularParser.ProducoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_producoes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(GramaticaRegularParser.T__4)
            self.state = 52
            self.producao()
            self.state = 53
            self.match(GramaticaRegularParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProducaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GramaticaRegularParser.VAR, 0)

        def transicao(self):
            return self.getTypedRuleContext(GramaticaRegularParser.TransicaoContext,0)


        def producao(self):
            return self.getTypedRuleContext(GramaticaRegularParser.ProducaoContext,0)


        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_producao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProducao" ):
                return visitor.visitProducao(self)
            else:
                return visitor.visitChildren(self)




    def producao(self):

        localctx = GramaticaRegularParser.ProducaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_producao)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(GramaticaRegularParser.T__8)
                self.state = 56
                self.match(GramaticaRegularParser.VAR)
                self.state = 57
                self.match(GramaticaRegularParser.T__9)
                self.state = 58
                self.transicao()
                self.state = 59
                self.match(GramaticaRegularParser.T__10)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(GramaticaRegularParser.T__8)
                self.state = 62
                self.match(GramaticaRegularParser.VAR)
                self.state = 63
                self.match(GramaticaRegularParser.T__9)
                self.state = 64
                self.transicao()
                self.state = 65
                self.match(GramaticaRegularParser.T__11)
                self.state = 66
                self.producao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransicaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_T(self):
            return self.getToken(GramaticaRegularParser.VAR_T, 0)

        def VAR(self):
            return self.getToken(GramaticaRegularParser.VAR, 0)

        def transicao(self):
            return self.getTypedRuleContext(GramaticaRegularParser.TransicaoContext,0)


        def VAZIO(self):
            return self.getToken(GramaticaRegularParser.VAZIO, 0)

        def getRuleIndex(self):
            return GramaticaRegularParser.RULE_transicao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransicao" ):
                return visitor.visitTransicao(self)
            else:
                return visitor.visitChildren(self)




    def transicao(self):

        localctx = GramaticaRegularParser.TransicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_transicao)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(GramaticaRegularParser.VAR_T)
                self.state = 71
                self.match(GramaticaRegularParser.VAR)
                self.state = 72
                self.match(GramaticaRegularParser.T__12)
                self.state = 73
                self.transicao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(GramaticaRegularParser.VAR_T)
                self.state = 75
                self.match(GramaticaRegularParser.VAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.match(GramaticaRegularParser.VAZIO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





