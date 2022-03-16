# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\StartAntlr\starter\ArrayInit.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArrayInitParser import ArrayInitParser
else:
    from ArrayInitParser import ArrayInitParser

# This class defines a complete generic visitor for a parse tree produced by ArrayInitParser.

class ArrayInitVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArrayInitParser#init.
    def visitInit(self, ctx:ArrayInitParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArrayInitParser#value.
    def visitValue(self, ctx:ArrayInitParser.ValueContext):
        return self.visitChildren(ctx)



del ArrayInitParser