
from ArrayInitListener import ArrayInitListener
from ArrayInitParser import ArrayInitParser

class ShortToUnicodeString(ArrayInitListener):
    # Enter a parse tree produced by ArrayInitParser#init.
    def enterInit(self, ctx:ArrayInitParser.InitContext):
        print('"', end='')

    # Exit a parse tree produced by ArrayInitParser#init.
    def exitInit(self, ctx:ArrayInitParser.InitContext):
        print('"', end='')


    # Enter a parse tree produced by ArrayInitParser#value.
    def enterValue(self, ctx:ArrayInitParser.ValueContext):
        if ctx.INT() is not None:
            value = int(ctx.INT().getText())
            hexval = format(value, '04x')
            print(f"\\u{hexval}", end='')


    # Exit a parse tree produced by ArrayInitParser#value.
    def exitValue(self, ctx:ArrayInitParser.ValueContext):
        pass
