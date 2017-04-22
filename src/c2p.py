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
    # Initialize the lexer, tokenstream and the parser with the input
    lexer = CmmLexer(input) 
    stream = CommonTokenStream(lexer) 
    parser = CmmParser(stream)

    # Build the parse tree
    parseTree = parser.program()

    # Generate and visit the Abstract Syntax Tree
    visitor = astBuilder("AST")
    visitor.visit(parseTree)
    visitor.toDot(parseTree)

if __name__ == '__main__':
    main(sys.argv)
