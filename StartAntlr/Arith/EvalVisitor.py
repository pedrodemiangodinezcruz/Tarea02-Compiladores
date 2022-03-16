from antlr.ArithVisitor import ArithVisitor
from antlr.ArithParser import ArithParser

class EvalVisitor(ArithVisitor):
    memory = dict()

    def visitAssign(self, ctx:ArithParser.AssignContext):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        
        return value


    def visitPrintExpr(self, ctx:ArithParser.PrintExprContext):
        # Like in Clojure, print evaluated expressions
        value = self.visit(ctx.expr())  # evaluate expr child
        print(value)
        return 0
    

    def visitId(self, ctx:ArithParser.IdContext):
        # If the id exists in memory return the value else return 0 (NULL)
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        else:
            return 0


    def visitINT(self, ctx:ArithParser.INTContext):
        return int(ctx.INT().getText())


    def visitMul(self, ctx:ArithParser.MulContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left * right
    
    
    def visitDiv(self, ctx:ArithParser.DivContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left // right


    def visitAdd(self, ctx:ArithParser.AddContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left + right
    
    
    def visitSub(self, ctx:ArithParser.SubContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left - right
    

    def visitParens(self, ctx:ArithParser.ParensContext):
        return self.visit(ctx.expr())
