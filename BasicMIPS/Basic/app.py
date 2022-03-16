from antlr4 import *
from DotDataListener import DotDataListener
from antlr.BasicLexer import BasicLexer
from antlr.BasicListener import BasicListener
from antlr.BasicParser import BasicParser
from EvalVisitor import EvalVisitor
from antlr4.tree.Trees import Trees
import sys

test = 4
inputfile = lambda x : f'in{x}.txt'
outputfile = lambda x : f'out{x}.asm'

def main():
    inputt = FileStream(inputfile(test))
    lexer = BasicLexer(inputt)
    tokens = CommonTokenStream(lexer)

    parser = BasicParser(tokens)

    tree = parser.prog() 
    print(Trees.toStringTree(tree, None, parser))

    # Escribir archivo output
    stdout = sys.stdout
    with open(outputfile(test), 'w') as f:
        sys.stdout = f

    
        dotData = DotDataListener()
        walker = ParseTreeWalker()
        walker.walk(dotData, tree)

        dataSegment = dotData.getDataSegment()

        # Genera .text segment con el visitor
        eval = EvalVisitor(dataSegment)
        eval.visit(tree)  # print del texto

        sys.stdout = stdout
        f.close()

if __name__ == '__main__':
    main()