from antlr4 import *
from DotDataListener import DotDataListener
from antlr.BasicLexer import BasicLexer
from antlr.BasicListener import BasicListener
from antlr.BasicParser import BasicParser
from EvalVisitor import EvalVisitor
from antlr4.tree.Trees import Trees
import sys

testNum = 4
inputfile = lambda x : f'in{x}.txt'
outputfile = lambda x : f'out{x}.asm'

def main():
    inputt = FileStream(inputfile(testNum))
    lexer = BasicLexer(inputt)
    tokens = CommonTokenStream(lexer)

    parser = BasicParser(tokens)

    tree = parser.prog() # begin parsing at prog rule
    print(Trees.toStringTree(tree, None, parser))

    # Open output file
    stdout = sys.stdout
    with open(outputfile(testNum), 'w') as f:
        sys.stdout = f

        # First, the walker should fetch all immediate assignments
        # And generate the .data segment
        dotData = DotDataListener()
        walker = ParseTreeWalker()
        walker.walk(dotData, tree)

        dataSegment = dotData.getDataSegment()

        # Then, we generate .text segment with the visitor 
        # (which can assume all labels are resolved)
        eval = EvalVisitor(dataSegment)
        eval.visit(tree)  # prints out all text segment

        sys.stdout = stdout
        f.close()

if __name__ == '__main__':
    main()