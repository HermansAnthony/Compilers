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
        if self.symbolTable.insertSymbol(functionName+"()", functionType, parameters) == None: raise declarationException(functionName, functionType, True, node.getPosition())
        print(self.symbolTable)
        if functionName == "main":
            self.mainFunctionFound = True
            if functionType['idType'] != 'i':
                raise mainTypeException(node.getPosition())
        # Visit the function body
        self.symbolTable.createScope(functionName)
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
                    raise wrongReturnType(retType, functionType, node.getPosition())
                return

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        identifier = node.declarator
        exprList = identifier.arrayExpressionList
        if len(exprList) != 0 and len(exprList) != 1:
            # Raise exception int main(a[5][5]), one dimensional arrays only for now 
            pass 
        if self.symbolTable.insertSymbol(node.getID(), node.getType()) == None:
            raise declarationException(node.getID(), node.getType(), False, "TODO line")

    def visitAssignmentNode(self, node:AssignmentNode):
        # Compare types
        item = self.symbolTable.lookupSymbol(node.getID())
        if item == None: raise unknownVariable(node.getID(), node.getPosition())
        exprType = self.visit(node.expression)
        # *b = 5
        declType = copy.deepcopy(item.type)
        if node.dereferenceCount > 0:
            declType['refCount'] -= node.dereferenceCount
        if declType['refCount'] < 0:
            raise deReference(node.getPosition())
        # If exprType is a dict => extract type out of dict
        if isinstance(exprType, dict): exprType = exprType['idType']
        if exprType != declType['idType']:
            raise wrongType(exprType, declType['idType'], node.getPosition())

    def visitIfStatementNode(self, node:IfStatementNode):
        # Check if expression is boolean
        exprType = self.visit(node.condition)
        declType = {'idType': "b", 'refCount': 0}
        if exprType != declType:     
            raise wrongType(exprType, declType['idType'], "TODO fix line here")
        for declStat in node.ifBody:
            self.visit(declStat)
        for declStat in node.elseBody:
            self.visit(declStat)

    def visitIterationStatementNode(self, node:IterationStatementNode):
        if node.statementName == "While":
            # Check if while expression is boolean
            exprType = self.visit(node.left)
            declType = {'idType': "b", 'refCount': 0}
            if exprType != declType:     
                raise wrongType(exprType['idType'], declType['idType'], "TODO fix line here")
            # visit function body
            for declStat in node.right:
                self.visit(declStat)

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
        declType = node.getType()
        if node.expression:
            # Compare types
            exprType = self.visit(node.expression)
            if type(node.expression) == InitializerListNode:
                exprs = node.expression.expressions
                # Check if initialization list contains the same types
                curType = self.visit(exprs[0])
                for i in range(1,len(exprs)):
                    otherType = self.visit(exprs[i])
                    if curType != otherType:
                        raise wrongType(curType, otherType, "TODO fix line here")
                exprType = curType
            if exprType != declType:   
                raise wrongType(exprType, declType['idType'], node.getPosition())
        if self.symbolTable.insertSymbol(node.getID(), declType) == None:
            raise declarationException(node.getID(), 
                declType['idType'], False, node.getPosition())

    def visitBinaryOperationNode(self, node:BinaryOperationNode):
        exprTypeLeft = self.visit(node.left)
        exprTypeRight = self.visit(node.right)
        if (exprTypeRight['refCount'] > 0 or
            exprTypeLeft['refCount'] > 0):
            raise wrongOperation("add/subtract/mul or div", "an address", "TODO line")
        typeLeft = exprTypeLeft['idType']
        typeRight = exprTypeRight['idType']
        if (node.operator == "&&" and node.operator == "||"):
            if typeLeft == {'idType': "b", 'refCount': 0}:
                # TODO && and || do not have a boolean type
                raise wrongOperation("&& and ||", 
                    typeLeft, "TODO fix line here", typeRight)
            if typeLeft != typeRight:
                raise wrongOperation(str(node.operator),
                    typeLeft, "TODO fix line here", typeRight)
        if (node.operator != "+" and node.operator != "-" 
            and node.operator != "*" and node.operator != "/"):
            typeLeft = {'idType': "b", 'refCount': 0}
        return exprTypeLeft
            
    def visitExpressionNode(self, node:ExpressionNode):
        exprType = None
        if node.isPostfix:
            # Id++ or Id-- works for all types except for char
            # Get the type of the identifier
            exprType = self.visit(node.child)
            if exprType['idType'] == "c" and exprType['refCount'] == 0:
                # TODO use an actual error
                raise incrementError(exprType['idType'],"TODO add line")
        return exprType

    def visitDereferenceExpressionNode(self, node:DereferenceExpressionNode):
        item = self.symbolTable.lookupSymbol(node.child.getID())
        if item == None: raise unknownVariable(node.child.getID(), "ADD line")
        if item.type['refCount'] < node.derefCount:
            raise deReference(node.getPosition())
        # Decrease the reference count of the exprType
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] -= node.derefCount
        return exprType

    def visitReferenceExpressionNode(self, node:ReferenceExpressionNode):
        item = self.symbolTable.lookupSymbol(node.child.getID())
        if item == None: raise unknownVariable(node.child.getID(), "ADD line")
        # Increase the reference count of the exprType
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] += 1
        return exprType  

    def visitFunctionCallNode(self, node:FunctionCallNode):
        #self.visit(node.identifier)
        # self.visit(node.argumentExpressionListNode)
        item = self.symbolTable.lookupSymbol(node.getID() + "()")
        if item == None: raise unknownVariable(node.getID()+"()", node.getPosition(), True)
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
        if self.symbolTable.insertSymbol(node.getID(), node.getType()) == None:
            raise declarationException(node.getID(), node.getType(), False, "TODO line")
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
        if item == None: raise unknownVariable(node.getID(), node.getPosition())
        #for expression in node.arrayExpressionList:
        #    self.visit(expression)
        return item.type

    def visitForwardFunctionDeclarationNode(self, node:ForwardFunctionDeclarationNode):
        # Ignore forward function declarations for now
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        print(self.symbolTable)
        self.symbolTable.insertSymbol(node.getID()+"()", node.declarationSpecifier.getType(), parameters)
        print(self.symbolTable)
        if node.declarationSpecifier:
            self.visit(node.declarationSpecifier)
        self.visit(node.identifier)
        if parameterList:
            self.visit(node.parameterList)

