import sys
from antlr4 import *
from BasicErrorListener import BasicErrorListener
from CmmLexer import CmmLexer
from CmmParser import CmmParser
from astBuilder import AstBuilder

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

    parser._listeners.append(BasicErrorListener())
    # Build the parse tree
    parseTree = parser.program()

    # Generate and visit the Abstract Syntax Tree
    visitor = AstBuilder()
    ast = visitor.visit(parseTree)
    filename = str(argv[1])
    outputAST = "ast_output/" + (filename.split("/")[1]).split(".")[0] + ".dot"
    print(outputAST)
    ast.toDot(outputAST)

if __name__ == '__main__':
    main(sys.argv)
