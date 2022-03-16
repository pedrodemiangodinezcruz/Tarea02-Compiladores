
from antlr.BasicListener import BasicListener
from antlr.BasicParser import BasicParser

class DotDataListener(BasicListener):
    initial_values = dict() 

    # Nodo ID al INT
    def exitAssign(self, ctx:BasicParser.AssignContext):
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())
        if id not in self.initial_values:
            self.initial_values[id] = value
    
    def exitReassign(self, ctx:BasicParser.ReassignContext):
        id = ctx.ID().getText()
        if id not in self.initial_values:
            self.initial_values[id] = None
    
    def getDataSegment(self):
        return self.initial_values
