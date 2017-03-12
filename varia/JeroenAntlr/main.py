import sys
from antlr4 import *
from LambdaLexer import LambdaLexer
from LambdaParser import LambdaParser
from CustomLambdaListener import CustomListener

def main(argv):
    input = FileStream(argv[1])
    lexer = LambdaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LambdaParser(stream)
    tree = parser.expr()

    printer = CustomListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
