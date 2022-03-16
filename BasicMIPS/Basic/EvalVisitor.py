'''
Clase que llama a la API "CodeGenerator" para generar el código MIPS 
'''

from antlr.BasicVisitor import BasicVisitor
from antlr.BasicParser import BasicParser
from CodeGenerator import *

class EvalVisitor(BasicVisitor):
    memory = dict()

    def __init__(self, dataSegment) -> None:
        super().__init__()
        # Imprimir el data segment
        DataSegment(dataSegment)

    def visitProg(self, ctx:BasicParser.ProgContext):
        printTexto()   
        return self.visitChildren(ctx)

    def visitAssign(self, ctx:BasicParser.AssignContext):
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())

        self.memory[id] = value
        return value
    
    def visitReassign(self, ctx:BasicParser.ReassignContext):
        # Imprimir codigo MIPS
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        # Mover el valor a la dirección
        generateReAssignment(id, value)
        self.memory[id] = value
        return value

    def visitPrintExpr(self, ctx:BasicParser.PrintExprContext):
        value = self.visit(ctx.expr())  
        
        if isinstance(value, int):  
            printInti(value)
        else:
            raise NotImplementedError
        return 0


    def visitINT(self, ctx:BasicParser.INTContext):
        return int(ctx.INT().getText())


    def visitMul(self, ctx:BasicParser.MulContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        Mult(left, right)

        return left * right
    
    
    def visitDiv(self, ctx:BasicParser.DivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        Div(left, right)

        return left // right


    def visitAdd(self, ctx:BasicParser.AddContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        Sum(left, right)

        return left + right
    
    
    def visitSub(self, ctx:BasicParser.SubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        Rest(left, right)

        return left - right
    

    def visitParens(self, ctx:BasicParser.ParensContext):
        return self.visit(ctx.expr())

    
    def visitAnd(self, ctx:BasicParser.AndContext):
        left = self.visit(ctx.boolExpr(0))
        right = self.visit(ctx.boolExpr(1))
        
        return left and right

    def visitOr(self, ctx:BasicParser.OrContext):
        left = self.visit(ctx.boolExpr(0))
        right = self.visit(ctx.boolExpr(1))
        
        return left or right
    
    def visitNot(self, ctx:BasicParser.NotContext):
        return not self.visit(ctx.boolExpr())


    def visitLessThan(self, ctx:BasicParser.LessThanContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return left < right
    
    def visitGreaterThan(self, ctx:BasicParser.GreaterThanContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return left > right

    def visitIsEqual(self, ctx:BasicParser.IsEqualContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        return left == right

    def visitTrue(self, ctx:BasicParser.TrueContext):
        return True
    
    def visitFalse(self, ctx:BasicParser.FalseContext):
        return False


    def visitIfstat(self, ctx:BasicParser.IfstatContext):
        condition = self.visit(ctx.boolExpr())
        if condition:
            return self.visit(ctx.stat())

    def visitIfelsestat(self, ctx:BasicParser.IfelsestatContext):
        condition = self.visit(ctx.boolExpr())
        if condition:
            return self.visit(ctx.stat(0))
        else:
            return self.visit(ctx.stat(1))
