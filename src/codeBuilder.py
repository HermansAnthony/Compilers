from astVisitor import AstVisitor
from astNode import *

# Overloaded Ast Visitor to configure the symbolTable
class CodeBuilder(AstVisitor):
    def __init__(self, table):
        self.symbolTable = table
        self.currentScope = 0

    def visitDeclarationNode(self, node:DeclarationNode):
        self.symbolTable.insertSymbol(node.getID(), node.getType())

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        self.symbolTable.insertSymbol(node.getID(), node.declarationSpecifier.getType(), parameters)

        # self.visit(node.functionBody)
