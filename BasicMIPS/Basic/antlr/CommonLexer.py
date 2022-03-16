# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\BasicMIPS\Basic\antlr\CommonLexer.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("!\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\r\n\2\r")
        buf.write("\2\16\2\16\3\3\6\3\22\n\3\r\3\16\3\23\3\4\5\4\27\n\4\3")
        buf.write("\4\3\4\3\5\6\5\34\n\5\r\5\16\5\35\3\5\3\5\2\2\6\3\3\5")
        buf.write("\4\7\5\t\6\3\2\5\4\2C\\c|\3\2\62;\3\2\"\"\2$\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\f\3\2\2\2\5\21")
        buf.write("\3\2\2\2\7\26\3\2\2\2\t\33\3\2\2\2\13\r\t\2\2\2\f\13\3")
        buf.write("\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\4\3")
        buf.write("\2\2\2\20\22\t\3\2\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21")
        buf.write("\3\2\2\2\23\24\3\2\2\2\24\6\3\2\2\2\25\27\7\17\2\2\26")
        buf.write("\25\3\2\2\2\26\27\3\2\2\2\27\30\3\2\2\2\30\31\7\f\2\2")
        buf.write("\31\b\3\2\2\2\32\34\t\4\2\2\33\32\3\2\2\2\34\35\3\2\2")
        buf.write("\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2\37 \b\5\2")
        buf.write("\2 \n\3\2\2\2\7\2\16\23\26\35\3\b\2\2")
        return buf.getvalue()


class CommonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INT = 2
    NEWLINE = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "NEWLINE", "WS" ]

    ruleNames = [ "ID", "INT", "NEWLINE", "WS" ]

    grammarFileName = "CommonLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


