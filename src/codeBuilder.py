from astVisitor import AstVisitor
from astNode import *

# Overloaded Ast Visitor for semantic analysis and code generation.
class CodeBuilder(AstVisitor):
    def __init__(self, table):
        self.symbolTable = table
        # Current relative address
        self.currentOffset = 0
        # Intermediate code being generated
        self.code = ""

    def visitDeclarationNode(self, node:DeclarationNode):
        self.symbolTable.insertSymbol(node.getID(), node.getType())
        idType = node.declarationSpecifier.idType()
        # Generate expression and compare types
        exprType = self.visit(node.expression)

    def visitExpressionNode(self, node:ExpressionNode):
        # self.operator = operator
        # self.isPostfix = isPostfix
        # self.child = child
        exprType = ""
        if self.isPostfix():
            # Id++ or Id--
            exprType = self.visit(node.child)
            idType = "i"
            if "float" in exprType:
                idType = "r"
            if node.operator == "++":            
                code += "inc " + idType + "1"
            else:
                code += "dec " + idType + "1"
        else:
            # And expression
            # It can be before a:
            #   Identifier Ex. &a
            #   BinaryOperationNode with first element an identifier Ex. &a + 3
            if type(node.child) == IdentifierNode:
                item = self.symbolTable.lookupSymbol(node.child.getID())
                code += "ldc a " + item.address   
                return item.type + "*" 
            if type(node.child) == BinaryOperationNode
                if type(node.child.left) == IdentifierNode:
                    item = self.symbolTable.lookupSymbol(node.child.left.getID())
                    itemType = item.type + "*"                   
                    code += "ldc a " + item.address  
                    exprType = self.visit(node.child)
                    if exprType == 
                    return itemType 


        # Ex. exprType = int**
        return exprType

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        self.symbolTable.insertSymbol(node.getID()+"()", node.declarationSpecifier.getType(), parameters)
        # TODO enterscope with symbol table
        self.visit(node.functionBody)

    def visitForwardFunctionDeclarationNode(self, node:ForwardFunctionDeclarationNode):
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        self.symbolTable.insertSymbol(node.getID()+"()", node.declarationSpecifier.getType(), parameters)
        if node.declarationSpecifier:
            self.visit(node.declarationSpecifier)
        self.visit(node.identifier)
        if parameterList:
            self.visit(node.parameterList)

