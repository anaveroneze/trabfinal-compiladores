# Generated from GramaticaRegular.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\17\6\17K\n\17\r\17")
        buf.write("\16\17L\3\20\6\20P\n\20\r\20\16\20Q\3\21\3\21\3\22\6\22")
        buf.write("W\n\22\r\22\16\22X\3\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23\3\2\5\3\2C\\\3\2c|\5\2\13\f\17\17\"\"\2^\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%")
        buf.write("\3\2\2\2\5(\3\2\2\2\7+\3\2\2\2\t.\3\2\2\2\13\61\3\2\2")
        buf.write("\2\r\65\3\2\2\2\17\67\3\2\2\2\21:\3\2\2\2\23=\3\2\2\2")
        buf.write("\25?\3\2\2\2\27A\3\2\2\2\31C\3\2\2\2\33G\3\2\2\2\35J\3")
        buf.write("\2\2\2\37O\3\2\2\2!S\3\2\2\2#V\3\2\2\2%&\7X\2\2&\'\7\"")
        buf.write("\2\2\'\4\3\2\2\2()\7V\2\2)*\7\"\2\2*\6\3\2\2\2+,\7R\2")
        buf.write("\2,-\7\"\2\2-\b\3\2\2\2./\7U\2\2/\60\7\"\2\2\60\n\3\2")
        buf.write("\2\2\61\62\7?\2\2\62\63\7\"\2\2\63\64\7]\2\2\64\f\3\2")
        buf.write("\2\2\65\66\7_\2\2\66\16\3\2\2\2\678\7.\2\289\7\"\2\29")
        buf.write("\20\3\2\2\2:;\7?\2\2;<\7\"\2\2<\22\3\2\2\2=>\7*\2\2>\24")
        buf.write("\3\2\2\2?@\7@\2\2@\26\3\2\2\2AB\7+\2\2B\30\3\2\2\2CD\7")
        buf.write("+\2\2DE\7.\2\2EF\7\"\2\2F\32\3\2\2\2GH\7~\2\2H\34\3\2")
        buf.write("\2\2IK\t\2\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2")
        buf.write("M\36\3\2\2\2NP\t\3\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2Q")
        buf.write("R\3\2\2\2R \3\2\2\2ST\7%\2\2T\"\3\2\2\2UW\t\4\2\2VU\3")
        buf.write("\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\b\22")
        buf.write("\2\2[$\3\2\2\2\6\2LQX\3\b\2\2")
        return buf.getvalue()


class GramaticaRegularLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    VAR = 14
    VAR_T = 15
    VAZIO = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'V '", "'T '", "'P '", "'S '", "'= ['", "']'", "', '", "'= '", 
            "'('", "'>'", "')'", "'), '", "'|'", "'#'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "VAR_T", "VAZIO", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "VAR", 
                  "VAR_T", "VAZIO", "WS" ]

    grammarFileName = "GramaticaRegular.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


