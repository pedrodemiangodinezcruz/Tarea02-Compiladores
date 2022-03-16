# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\BasicMIPS\Basic\antlr\Basic.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete listener for a parse tree produced by BasicParser.
class BasicListener(ParseTreeListener):

    # Enter a parse tree produced by BasicParser#prog.
    def enterProg(self, ctx:BasicParser.ProgContext):
        pass

    # Exit a parse tree produced by BasicParser#prog.
    def exitProg(self, ctx:BasicParser.ProgContext):
        pass


    # Enter a parse tree produced by BasicParser#if.
    def enterIf(self, ctx:BasicParser.IfContext):
        pass

    # Exit a parse tree produced by BasicParser#if.
    def exitIf(self, ctx:BasicParser.IfContext):
        pass


    # Enter a parse tree produced by BasicParser#ifelse.
    def enterIfelse(self, ctx:BasicParser.IfelseContext):
        pass

    # Exit a parse tree produced by BasicParser#ifelse.
    def exitIfelse(self, ctx:BasicParser.IfelseContext):
        pass


    # Enter a parse tree produced by BasicParser#printExpr.
    def enterPrintExpr(self, ctx:BasicParser.PrintExprContext):
        pass

    # Exit a parse tree produced by BasicParser#printExpr.
    def exitPrintExpr(self, ctx:BasicParser.PrintExprContext):
        pass


    # Enter a parse tree produced by BasicParser#assign.
    def enterAssign(self, ctx:BasicParser.AssignContext):
        pass

    # Exit a parse tree produced by BasicParser#assign.
    def exitAssign(self, ctx:BasicParser.AssignContext):
        pass


    # Enter a parse tree produced by BasicParser#reassign.
    def enterReassign(self, ctx:BasicParser.ReassignContext):
        pass

    # Exit a parse tree produced by BasicParser#reassign.
    def exitReassign(self, ctx:BasicParser.ReassignContext):
        pass


    # Enter a parse tree produced by BasicParser#blank.
    def enterBlank(self, ctx:BasicParser.BlankContext):
        pass

    # Exit a parse tree produced by BasicParser#blank.
    def exitBlank(self, ctx:BasicParser.BlankContext):
        pass


    # Enter a parse tree produced by BasicParser#ifstat.
    def enterIfstat(self, ctx:BasicParser.IfstatContext):
        pass

    # Exit a parse tree produced by BasicParser#ifstat.
    def exitIfstat(self, ctx:BasicParser.IfstatContext):
        pass


    # Enter a parse tree produced by BasicParser#ifelsestat.
    def enterIfelsestat(self, ctx:BasicParser.IfelsestatContext):
        pass

    # Exit a parse tree produced by BasicParser#ifelsestat.
    def exitIfelsestat(self, ctx:BasicParser.IfelsestatContext):
        pass


    # Enter a parse tree produced by BasicParser#Div.
    def enterDiv(self, ctx:BasicParser.DivContext):
        pass

    # Exit a parse tree produced by BasicParser#Div.
    def exitDiv(self, ctx:BasicParser.DivContext):
        pass


    # Enter a parse tree produced by BasicParser#Add.
    def enterAdd(self, ctx:BasicParser.AddContext):
        pass

    # Exit a parse tree produced by BasicParser#Add.
    def exitAdd(self, ctx:BasicParser.AddContext):
        pass


    # Enter a parse tree produced by BasicParser#Sub.
    def enterSub(self, ctx:BasicParser.SubContext):
        pass

    # Exit a parse tree produced by BasicParser#Sub.
    def exitSub(self, ctx:BasicParser.SubContext):
        pass


    # Enter a parse tree produced by BasicParser#parens.
    def enterParens(self, ctx:BasicParser.ParensContext):
        pass

    # Exit a parse tree produced by BasicParser#parens.
    def exitParens(self, ctx:BasicParser.ParensContext):
        pass


    # Enter a parse tree produced by BasicParser#Mul.
    def enterMul(self, ctx:BasicParser.MulContext):
        pass

    # Exit a parse tree produced by BasicParser#Mul.
    def exitMul(self, ctx:BasicParser.MulContext):
        pass


    # Enter a parse tree produced by BasicParser#id.
    def enterId(self, ctx:BasicParser.IdContext):
        pass

    # Exit a parse tree produced by BasicParser#id.
    def exitId(self, ctx:BasicParser.IdContext):
        pass


    # Enter a parse tree produced by BasicParser#INT.
    def enterINT(self, ctx:BasicParser.INTContext):
        pass

    # Exit a parse tree produced by BasicParser#INT.
    def exitINT(self, ctx:BasicParser.INTContext):
        pass


    # Enter a parse tree produced by BasicParser#Not.
    def enterNot(self, ctx:BasicParser.NotContext):
        pass

    # Exit a parse tree produced by BasicParser#Not.
    def exitNot(self, ctx:BasicParser.NotContext):
        pass


    # Enter a parse tree produced by BasicParser#LessThan.
    def enterLessThan(self, ctx:BasicParser.LessThanContext):
        pass

    # Exit a parse tree produced by BasicParser#LessThan.
    def exitLessThan(self, ctx:BasicParser.LessThanContext):
        pass


    # Enter a parse tree produced by BasicParser#Or.
    def enterOr(self, ctx:BasicParser.OrContext):
        pass

    # Exit a parse tree produced by BasicParser#Or.
    def exitOr(self, ctx:BasicParser.OrContext):
        pass


    # Enter a parse tree produced by BasicParser#GreaterThan.
    def enterGreaterThan(self, ctx:BasicParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by BasicParser#GreaterThan.
    def exitGreaterThan(self, ctx:BasicParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by BasicParser#And.
    def enterAnd(self, ctx:BasicParser.AndContext):
        pass

    # Exit a parse tree produced by BasicParser#And.
    def exitAnd(self, ctx:BasicParser.AndContext):
        pass


    # Enter a parse tree produced by BasicParser#True.
    def enterTrue(self, ctx:BasicParser.TrueContext):
        pass

    # Exit a parse tree produced by BasicParser#True.
    def exitTrue(self, ctx:BasicParser.TrueContext):
        pass


    # Enter a parse tree produced by BasicParser#False.
    def enterFalse(self, ctx:BasicParser.FalseContext):
        pass

    # Exit a parse tree produced by BasicParser#False.
    def exitFalse(self, ctx:BasicParser.FalseContext):
        pass


    # Enter a parse tree produced by BasicParser#IsEqual.
    def enterIsEqual(self, ctx:BasicParser.IsEqualContext):
        pass

    # Exit a parse tree produced by BasicParser#IsEqual.
    def exitIsEqual(self, ctx:BasicParser.IsEqualContext):
        pass



del BasicParser