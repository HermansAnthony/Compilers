from astVisitor import AstVisitor
from astNode import *
import copy

class Code():
    code = ""
    def newline(line):
        code += line + "\n"

    def getCode():
        return code

# Overloaded Ast Visitor for semantic analysis and code generation.
class CodeBuilder(AstVisitor):
    def __init__(self, table):
        self.symbolTable = table
        # Current relative address
        self.currentOffset = 0
        # Intermediate code being generated
        self.code = Code

    def visitDeclarationNode(self, node:DeclarationNode):
        self.symbolTable.insertSymbol(node.getID(), node.getType())
        idType = node.declarationSpecifier.idType()
        # Generate expression and compare types
        # exprType is a dictionary with idType and refCount
        exprType = self.visit(node.expression)

    def visitExpressionNode(self, node:ExpressionNode):
        exprType = None
        if self.isPostfix():
            # Id++ or Id-- works for all types
            exprType = self.visit(node.child)
            item = self.symbolTable.lookupSymbol(node.child.getID())
            address = item.address
            idType = "i"
            if "float" in exprType:
                idType = "r"
            # load lvalue  
            code.newline("lod T nestingdiff offset")
            if node.operator == "++":
                code.newline("inc " + idType + "1")
            else:
                code.newline("dec " + idType + "1")
            # store lvalue
            code.newline("str T nestingdiff offset")
        return exprType

    def visitDereferenceExpressionNode(self, node:DereferenceExpressionNode):
        # Rule: Star+ expression
        # int *a = *b
        # int a = ***b + 3
        # int a = *b[2] + 3
        # TODO array support
        item = self.symbolTable.lookupSymbol(node.child.getID())
        if item.type['refCount'] < node.derefCount:
            # Raise too many dereferences error
            pass
        idType = "a"
        if item.type['refCount'] == node.derefCount:
            idType = item.type['idType']
        address = item.address
        code.newline("ldc a " + address)
        for i in range(node.derefCount-1):
            code.newline("ind a")
        code.newline("ind " + idType)
        # Leave dereferenced lvalue on top of stack
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] -= node.derefCount
        return exprType

    def visitReferenceExpressionNode(self, node:ReferenceExpressionNode):
        # int *a = &b + 3
        # int *a = &b[1] + 3
        # TODO array support
        item = self.symbolTable.lookupSymbol(node.child.getID())
        code.newline("ldc a " + item.address)
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] += 1
        return exprType    

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        functionName = node.getID()
        self.symbolTable.insertSymbol(functionName+"()", node.declarationSpecifier.getType(), parameters)
        # Enter the scope
        self.symbolTable.beginScope()
        self.visit(node.functionBody)
        # Generate procedure label
        code.newline(functionName + ":")
        code.newline("")
        self.symbolTable.endScope() 

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

