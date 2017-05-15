from astVisitor import AstVisitor
from astNode import *
import copy

class Code():
    code = ""
    maxOffset = 0

    def newline(self, line):
        code += line + "\n"

    def newblock(self, other)
        self.code += other.code

# Overloaded Ast Visitor for semantic analysis and code generation.
class CodeBuilder(AstVisitor):
    def __init__(self, table):
        self.symbolTable = table
        # Intermediate code being generated
        self.code = Code()
        # Function body intermediate code
        self.functionBodyCode = None

    def visitDeclarationNode(self, node:DeclarationNode):
        declType = node.getType()
        item = self.symbolTable.insertSymbol(node.getID(), declType)
        # Generate expression and compare types
        # exprType is a dictionary with idType and refCount
        exprType = self.visit(node.expression)

        code.newline("str " + decltype['idType'] + "0"

    def visitBinaryOperationNode(self, node:BinaryOperationNode):
        self.visit(node.left)
        self.visit(node.right)

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

    def visitFunctionCallNode(self, node:FunctionCallNode):
        self.visit(node.identifier)
        self.visit(node.argumentExpressionListNode)  

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        # Insert function into symbol table
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        functionName = node.getID()
        self.symbolTable.insertSymbol(functionName+"()", 
            node.declarationSpecifier.getType(), parameters)

        self.symbolTable.beginScope()
        # Generate procedure label
        code.newline(functionName + ":")
        
        # Calculate the length of the static section of the stack frame
        # 5 organizational cells after MP
        staticLength = 5    
        for paramDecl in node.parameterList.paramDecls:
            self.visit(paramDecl)
            staticLength += 1
        for declstat in self.functionBody:
            if type(declstat) == DeclarationNode:
                staticLength += 1
        # Calculate the value of the extreme stack pointer
        functionBodyCode = Code()
        for declstat in self.functionBody:
            self.visit(declstat)
        maxOffset = functionBodyCode.maxOffset
        
        # Set the stack pointer and EP
        code.newline("ent " + maxOffset + " " + staticLength)

        code.newblock(functionBodyCode)
        self.symbolTable.endScope() 

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        self.symbolTable.insertSymbol(node.getID(), node.getType())
        # Check if type is array to increase size        

    def visitIdentifierNode(self, node:IdentifierNode):
        idType = {'idType': idType, 'refCount': 0}
        for expression in node.arrayExpressionList:
            self.visit(expression)




    def visitForwardFunctionDeclarationNode(self, node:ForwardFunctionDeclarationNode):
        # Ignore forward function declarations for now
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        self.symbolTable.insertSymbol(node.getID()+"()", node.declarationSpecifier.getType(), parameters)
        if node.declarationSpecifier:
            self.visit(node.declarationSpecifier)
        self.visit(node.identifier)
        if parameterList:
            self.visit(node.parameterList)

