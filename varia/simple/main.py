import sys
from antlr4 import *
from MyGrammarLexer import MyGrammarLexer
from MyGrammarParser import MyGrammarParser

# Changes
from MyGrammarListener import MyGrammarListener
from MyGrammarVisitor import MyGrammarVisitor

# Subclass of generated listener class
class KeyPrinter(MyGrammarListener):
    def exitKey(self, ctx):
        print("Oh, a key!")

# Subclass of generated visitor class
class visitorPrinter(MyGrammarVisitor):
    def temp(self, ctx):
        print("Good job")

def main(argv):
    # Run first java -jar [antlr jar file] -Dlanguage=Python3 [grammar file] -visitor
    # python3 main.py [input txt file]

    if len(argv) < 2:
        print ("Not enough files given")
        return
    input = FileStream(argv[1])
    lexer = MyGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)

    # Start rule refers to rule in mygrammar.g4
    tree = parser.startRule()

    # Subclass of listener
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
