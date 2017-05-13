from SymbolTable import *
from astNode import *

class SymbolTableBuilder:
    def __init__(self, table=None):
        self.currentScope = 0
        self.symbolTable = table

    def build(self, node):
        print("Building the symbol table")
        for child in node.children:
            self.enterNode(child)
        print("Done building the symbol table")
        print(str(self.symbolTable))
        return self.symbolTable

    def enterNode(self, node):
        #process the node here
        print(type(node))
        print("test",node.identifier.identifier)
        pass

    def enterScope(self):
        self.symbolTable.beginScope()

    def leaveScope(self):
        self.symbolTable.endScope()
