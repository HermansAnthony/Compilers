from gen import CmmVisitor, CmmParser
from astNode import *

class astBuilder(CmmVisitor):
    def __init__(self, name):
        self.tree = None
        self.name = name


    def visitProgram(self, ctx: CmmParser.ProgramContext):
        # self.tree = TODO

    # Overloaded print function for the print function
    # Writes AST tree to a dot file
    def __repr__(self):
        print("A dot file with name ", self.name, " is created for the AST")
        # TODO insert real ast nodes in string version here
        astStringFormat = 'digraph G { "Hello" -> "World"}'
        # astStringFormat = str(self.tree)
        output = open(self.name, 'w')
        output.write(astStringFormat)
        output.close()

