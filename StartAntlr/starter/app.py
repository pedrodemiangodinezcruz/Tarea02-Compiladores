from antlr4 import *
from ArrayInitLexer import ArrayInitLexer
from ArrayInitListener import ArrayInitListener
from ArrayInitParser import ArrayInitParser
from CodeGen import ShortToUnicodeString
from antlr4.tree.Trees import Trees

import os

def main():
    inputt = FileStream("test.txt")
    lexer = ArrayInitLexer(inputt)
    tokens = CommonTokenStream(lexer)

    parser = ArrayInitParser(tokens)

    tree = parser.init() # begin parsing at init rule
    # print(Trees.toStringTree(tree, None, parser))

    walker = ParseTreeWalker()
    walker.walk(ShortToUnicodeString(), tree)
    print()


if __name__ == '__main__':
    main()