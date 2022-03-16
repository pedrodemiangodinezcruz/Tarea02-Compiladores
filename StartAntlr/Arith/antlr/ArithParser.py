# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\StartAntlr\Arith\antlr\Arith.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\5\4 \n\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4.\n\4\f\4\16\4\61\13\4\3")
        buf.write("\4\2\3\6\5\2\4\6\2\2\28\2\t\3\2\2\2\4\26\3\2\2\2\6\37")
        buf.write("\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2")
        buf.write("\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\16\5\6\4\2\16\17\7\f\2")
        buf.write("\2\17\27\3\2\2\2\20\21\7\n\2\2\21\22\7\3\2\2\22\23\5\6")
        buf.write("\4\2\23\24\7\f\2\2\24\27\3\2\2\2\25\27\7\f\2\2\26\r\3")
        buf.write("\2\2\2\26\20\3\2\2\2\26\25\3\2\2\2\27\5\3\2\2\2\30\31")
        buf.write("\b\4\1\2\31 \7\13\2\2\32 \7\n\2\2\33\34\7\4\2\2\34\35")
        buf.write("\5\6\4\2\35\36\7\5\2\2\36 \3\2\2\2\37\30\3\2\2\2\37\32")
        buf.write("\3\2\2\2\37\33\3\2\2\2 /\3\2\2\2!\"\f\t\2\2\"#\7\6\2\2")
        buf.write("#.\5\6\4\n$%\f\b\2\2%&\7\7\2\2&.\5\6\4\t\'(\f\7\2\2()")
        buf.write("\7\b\2\2).\5\6\4\b*+\f\6\2\2+,\7\t\2\2,.\5\6\4\7-!\3\2")
        buf.write("\2\2-$\3\2\2\2-\'\3\2\2\2-*\3\2\2\2.\61\3\2\2\2/-\3\2")
        buf.write("\2\2/\60\3\2\2\2\60\7\3\2\2\2\61/\3\2\2\2\7\13\26\37-")
        buf.write("/")
        return buf.getvalue()


class ArithParser ( Parser ):

    grammarFileName = "Arith.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'*'", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MUL", "DIV", "ADD", "SUB", "ID", "INT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    ID=8
    INT=9
    NEWLINE=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithParser.StatContext)
            else:
                return self.getTypedRuleContext(ArithParser.StatContext,i)


        def getRuleIndex(self):
            return ArithParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ArithParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArithParser.T__1) | (1 << ArithParser.ID) | (1 << ArithParser.INT) | (1 << ArithParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(ArithParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(ArithParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArithParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ArithParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(ArithParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = ArithParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ArithParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(ArithParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = ArithParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(ArithParser.ID)
                self.state = 15
                self.match(ArithParser.T__0)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(ArithParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = ArithParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(ArithParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithParser.ExprContext,i)

        def DIV(self):
            return self.getToken(ArithParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithParser.ExprContext,i)

        def ADD(self):
            return self.getToken(ArithParser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithParser.ExprContext,i)

        def SUB(self):
            return self.getToken(ArithParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ArithParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ArithParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ArithParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterINT" ):
                listener.enterINT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitINT" ):
                listener.exitINT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ArithParser.INT]:
                localctx = ArithParser.INTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(ArithParser.INT)
                pass
            elif token in [ArithParser.ID]:
                localctx = ArithParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(ArithParser.ID)
                pass
            elif token in [ArithParser.T__1]:
                localctx = ArithParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(ArithParser.T__1)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(ArithParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 43
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ArithParser.MulContext(self, ArithParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 32
                        self.match(ArithParser.MUL)
                        self.state = 33
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ArithParser.DivContext(self, ArithParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 35
                        self.match(ArithParser.DIV)
                        self.state = 36
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = ArithParser.AddContext(self, ArithParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 38
                        self.match(ArithParser.ADD)
                        self.state = 39
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = ArithParser.SubContext(self, ArithParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        self.match(ArithParser.SUB)
                        self.state = 42
                        self.expr(5)
                        pass

             
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




