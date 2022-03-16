# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\StartAntlr\Arith\antlr\Arith.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArithParser import ArithParser
else:
    from ArithParser import ArithParser

# This class defines a complete generic visitor for a parse tree produced by ArithParser.

class ArithVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithParser#prog.
    def visitProg(self, ctx:ArithParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#printExpr.
    def visitPrintExpr(self, ctx:ArithParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#assign.
    def visitAssign(self, ctx:ArithParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#blank.
    def visitBlank(self, ctx:ArithParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#Div.
    def visitDiv(self, ctx:ArithParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#Add.
    def visitAdd(self, ctx:ArithParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#Sub.
    def visitSub(self, ctx:ArithParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#parens.
    def visitParens(self, ctx:ArithParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#Mul.
    def visitMul(self, ctx:ArithParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#id.
    def visitId(self, ctx:ArithParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithParser#INT.
    def visitINT(self, ctx:ArithParser.INTContext):
        return self.visitChildren(ctx)



del ArithParser