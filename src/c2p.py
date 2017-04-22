import sys
from antlr4 import *
from CmmLexer import CmmLexer
from CmmParser import CmmParser
from astBuilder import astBuilder

def main(argv):
    print ("Main program:\n")
    if len(argv) < 3:
        print ("Specify a C program input file and a P program output file\n")
        return 0
    input = FileStream(argv[1])
    # Initiialize Lexer/Recognizer object with the input
    lexer = CmmLexer(input) 
    stream = CommonTokenStream(lexer) 
    parser = CmmParser(stream)
    tree = parser.program()
    visitor = astBuilder()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
