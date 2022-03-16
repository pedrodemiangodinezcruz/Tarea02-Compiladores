# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\BasicMIPS\Basic\antlr\Basic.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete generic visitor for a parse tree produced by BasicParser.

class BasicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasicParser#prog.
    def visitProg(self, ctx:BasicParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#if.
    def visitIf(self, ctx:BasicParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#ifelse.
    def visitIfelse(self, ctx:BasicParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#printExpr.
    def visitPrintExpr(self, ctx:BasicParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#assign.
    def visitAssign(self, ctx:BasicParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#reassign.
    def visitReassign(self, ctx:BasicParser.ReassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#blank.
    def visitBlank(self, ctx:BasicParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#ifstat.
    def visitIfstat(self, ctx:BasicParser.IfstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#ifelsestat.
    def visitIfelsestat(self, ctx:BasicParser.IfelsestatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Div.
    def visitDiv(self, ctx:BasicParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Add.
    def visitAdd(self, ctx:BasicParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Sub.
    def visitSub(self, ctx:BasicParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#parens.
    def visitParens(self, ctx:BasicParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Mul.
    def visitMul(self, ctx:BasicParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#id.
    def visitId(self, ctx:BasicParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#INT.
    def visitINT(self, ctx:BasicParser.INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Not.
    def visitNot(self, ctx:BasicParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#LessThan.
    def visitLessThan(self, ctx:BasicParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Or.
    def visitOr(self, ctx:BasicParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#GreaterThan.
    def visitGreaterThan(self, ctx:BasicParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#And.
    def visitAnd(self, ctx:BasicParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#True.
    def visitTrue(self, ctx:BasicParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#False.
    def visitFalse(self, ctx:BasicParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#IsEqual.
    def visitIsEqual(self, ctx:BasicParser.IsEqualContext):
        return self.visitChildren(ctx)



del BasicParser