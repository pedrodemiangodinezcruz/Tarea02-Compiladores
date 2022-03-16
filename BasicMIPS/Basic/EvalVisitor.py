'''
Class that calls CodeGenerator API to generate necessary MIPS code for a Basic program file.
Multiple-operations on a single line are supported by the grammar, 
but not explicitly supported by this generator yet.
'''

from antlr.BasicVisitor import BasicVisitor
from antlr.BasicParser import BasicParser
from CodeGenerator import *

class EvalVisitor(BasicVisitor):
    memory = dict()

    def __init__(self, dataSegment) -> None:
        super().__init__()
        # Print the .data Segment
        DataSegment(dataSegment)

    def visitProg(self, ctx:BasicParser.ProgContext):
        printTexto()   
        return self.visitChildren(ctx)

    def visitAssign(self, ctx:BasicParser.AssignContext):
        # Triggered by initialization of values only.
        # Save (id:value) to internal memory
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())

        self.memory[id] = value
        return value
    
    def visitReassign(self, ctx:BasicParser.ReassignContext):
        # Print necessary MIPS code for computing and reassigning a variable
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        # Once expression computation is generated we can move the value to address
        generateReAssignment(id, value)
        self.memory[id] = value
        return value

    # Our language prints any expression
    def visitPrintExpr(self, ctx:BasicParser.PrintExprContext):
        value = self.visit(ctx.expr())  # returns literal value even if its label
        
        if isinstance(value, int):  # print immediate int
            printInti(value)
        else:
            # No Strings supported yet
            raise NotImplementedError
        return 0

    def visitId(self, ctx:BasicParser.IdContext):
        # If the id exists in memory return the value else return 0 (NULL)
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        else:
            return 0


    def visitINT(self, ctx:BasicParser.INTContext):
        return int(ctx.INT().getText())


    def visitMul(self, ctx:BasicParser.MulContext):
        # Should we print possible loadings of variables?
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        Mult(left, right)

        return left * right
    
    
    def visitDiv(self, ctx:BasicParser.DivContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        Div(left, right)

        return left // right


    def visitAdd(self, ctx:BasicParser.AddContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        Sum(left, right)

        return left + right
    
    
    def visitSub(self, ctx:BasicParser.SubContext):
        # Fetch left and right operands recursively
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
        # Evaluate condition
        condition = self.visit(ctx.boolExpr())
        if condition:
            return self.visit(ctx.stat())

    def visitIfelsestat(self, ctx:BasicParser.IfelsestatContext):
        condition = self.visit(ctx.boolExpr())
        if condition:
            return self.visit(ctx.stat(0))
        else:
            return self.visit(ctx.stat(1))
