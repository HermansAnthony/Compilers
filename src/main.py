import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from SmallCLexer import SmallCLexer
from SmallCParser import SmallCParser

def main(argv):
    input = FileStream(argv[1])
    # Initiialize Lexer/Recognizer object with the input
    lexer = SmallCLexer(input) 
    # Initialize the stream of tokens
    # populated when parser.expr() is called using the Lexer.
    stream = CommonTokenStream(lexer) 
    # Initialize the parser.
    parser = SmallCParser(stream)
    tree = parser.primaryExpression()
    print(Trees.toStringTree(tree, None, parser))


if __name__ == '__main__':
    main(sys.argv)
