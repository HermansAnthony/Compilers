from astVisitor import AstVisitor
from astNode import *
from Exceptions import *
import copy

# Overloaded Ast Visitor for semantic analysis.
class SemanticVisitor(AstVisitor):
    def __init__(self, table):
        self.symbolTable = table
        self.mainFunctionFound = False

    def visitProgramNode(self, node:ProgramNode):
        for child in node.children:
            self.visit(child)
        if not self.mainFunctionFound:
            raise mainException()
        self.symbolTable.resetScopeCounter()

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        # Insert function into symbol table
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        functionName = node.getID()
        functionType = node.getType()
        self.symbolTable.insertSymbol(functionName+"()", 
            functionType, parameters)
        if functionName == "main":
            self.mainFunctionFound = True
        # Visit the function body
        self.symbolTable.createScope()
        # Insert parameters into symbol table
        if node.parameterList:
            for paramDecl in node.parameterList.paramDecls:
                self.visit(paramDecl)
        for declstat in node.functionBody:
            # Calculate extreme pointer
            retType = self.visit(declstat)
            # Compare type from return statement
            if retType and 'returnStat' in retType:
                retType.pop('returnStat')
                if retType  != functionType:
                    # TODO Fix this so the error can occur
                    raise wrongReturnType(retType, functionType, "TODO add line here")
                return

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        self.symbolTable.insertSymbol(node.getID(), node.getType())

    def visitAssignmentNode(self, node:AssignmentNode):
        # Compare types
        item = self.symbolTable.lookupSymbol(node.getID())
        exprType = self.visit(node.expression)
        # *b = 5
        declType = copy.deepcopy(item.type)
        if node.dereferenceCount > 0:
            declType['refCount'] -= node.dereferenceCount
        if declType['refCount'] < 0:
            raise deReference("TODO add line")
        if exprType != declType:
            raise wrongType(exprType, declType, "TODO add line")

    def visitIfStatementNode(self, node:IfStatementNode):
        self.visit(node.condition)
        self.visit(node.ifBody)
        self.visit(node.elseBody)

    def visitIterationStatementNode(self, node:IterationStatementNode):
        if self.left:
            self.visit(node.left)
        if self.middle1:
            self.visit(node.middle1)
        if self.middle2:
            self.visit(node.middle2)
        if self.right:
            self.visit(node.right)

    def visitReturnNode(self, node:ReturnNode):
        if node.expressionNode:
            exprType = self.visit(node.expressionNode)
            return exprType
        return {'returnStat': True, 'idType': None, 'refCount': 0}

    def visitBreakNode(self, node:BreakNode):
        pass

    def visitContinueNode(self, node:ContinueNode):
        pass

    def visitDeclarationNode(self, node:DeclarationNode):
        # Compare types
        exprType = self.visit(node.expression)
        declType = node.getType()
        if exprType != declType:     
            raise wrongType(exprType, declType, "TODO fix line here")
        self.symbolTable.insertSymbol(node.getID(), declType)

    def visitBinaryOperationNode(self, node:BinaryOperationNode):
        exprTypeLeft = self.visit(node.left)
        exprTypeRight = self.visit(node.right)
        if (exprTypeRight['refCount'] > 0 or
            exprTypeLeft['refCount'] > 0):
            raise wrongOperation("add/subtract/mul or div", "an address", "TODO line")
        typeLeft = exprTypeLeft['idType']
        typeRight = exprTypeRight['idType']
        if typeLeft != typeRight:
            # TODO maybe more operations than only add?
            raise wrongType(typeLeft, "add", "TODO fix line here", typeRight)
        return typeLeft
            
    def visitExpressionNode(self, node:ExpressionNode):
        exprType = None
        if self.isPostfix():
            # Id++ or Id-- works for all types except for char
            # Get the type of the identifier
            exprType = self.visit(node.child)
            if exprType['idType'] == "c" and exprType['refCount'] == 0:
                # TODO use an actual error
                raise incrementError(exprType['idType'],"TODO add line")
        return exprType

    def visitDereferenceExpressionNode(self, node:DereferenceExpressionNode):
        item = self.symbolTable.lookupSymbol(node.child.getID())
        if item.type['refCount'] < node.derefCount:
            raise deReference("TODO add line")
        # Decrease the reference count of the exprType
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] -= node.derefCount
        return exprType

    def visitReferenceExpressionNode(self, node:ReferenceExpressionNode):
        item = self.symbolTable.lookupSymbol(node.child.getID())
        # Increase the reference count of the exprType
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] += 1
        return exprType  

    def visitFunctionCallNode(self, node:FunctionCallNode):
        #self.visit(node.identifier)
        # self.visit(node.argumentExpressionListNode)  
        item = self.symbolTable.lookupSymbol(node.getID()+"()")
        params = item.parameters # List of parameterDeclNode
        args = node.argumentExpressionListNode.argumentExprs
        if len(params) != len(args):
            raise parameterError(len(args), len(params), "TODO add line")
        for i in range(len(params)):
            paramType = params[i].getType()
            argType = self.visit(args[i])
            if argType != paramType:
                 raise parameterTypeError(argType, paramType, "TODO add line")
        return item.type

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        self.symbolTable.insertSymbol(node.getID(), node.getType())
        # Check if type is array to increase size     

    def visitIntegerConstantNode(self, node:IntegerConstantNode):
        return {'idType': "i", 'refCount': 0}

    def visitFloatingConstantNode(self, node:FloatingConstantNode):
        return {'idType': "r", 'refCount': 0}

    def visitCharacterConstantNode(self, node:CharacterConstantNode):
        return {'idType': "c", 'refCount': 0}

    def visitDeclarationSpecifierNode(self, node:DeclarationSpecifierNode):
        pass   

    def visitIdentifierNode(self, node:IdentifierNode):
        item = self.symbolTable.lookupSymbol(node.getID())
        #for expression in node.arrayExpressionList:
        #    self.visit(expression)
        return item.type



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

