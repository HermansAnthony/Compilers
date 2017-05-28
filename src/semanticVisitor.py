from astVisitor import AstVisitor
from astNode import *
from Exceptions import *
import copy

# Overloaded Ast Visitor for semantic analysis.
class SemanticVisitor(AstVisitor):
    def __init__(self, table, code):
        self.symbolTable = table
        self.mainFunctionFound = False
        self.codeBuilder = code # refers to codeBuilder
        self.isInLoop = False

    def visitProgramNode(self, node:ProgramNode):
        # Check all global variables first (semantically)
        for child in node.children:
            if type(child) == DeclarationNode:
                self.visit(child)

        # Generate the main function and the global variables (code generation)
        self.codeBuilder.visit(node)

        # Further semantic analysis (non declaration nodes)
        for child in node.children:
            if type(child) != DeclarationNode:
                self.visit(child)
                # self.symbolTable.resetScopeCounter() # Return to global scope

        # No main function declared in file
        if not self.mainFunctionFound: raise mainException()

    def visitStdioNode(self, node:StdioNode):
        self.symbolTable.insertSymbol("printf()", 
            {'idType': "i", 'refCount': 0}, params=[]) 
        self.symbolTable.insertSymbol("scanf()", 
            {'idType': "i", 'refCount': 0}, params=[])    

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        # Insert function into symbol table
        parameters = list()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        functionName = node.getID()
        functionType = node.getType()
        # Check if there was a forward function declaration
        if not self.symbolTable.insertSymbol(functionName+"()", functionType, params=parameters):
            item = self.symbolTable.lookupSymbol(functionName+"()")
            if not item.isForwardDecl:
                raise declarationException(functionName, 
                    functionType, True, node.getPosition())
            # Check if parameter types match
            if len(parameters) != len(item.parameters):
                raise conflictingParameterLength(functionName, len(parameters), len(item.parameters), node.getPosition())
            for index, param in enumerate(parameters):
                paramType1 = param.getType()
                paramType2 = item.getType()
                if paramType1 != paramType2:
                    raise parameterTypeError(functionName, paramType1, paramType2, node.getPosition())

        # Don't allow redefinition of printf and scanf function
        if node.getID() == "printf" or node.getID() == "scanf": raise builtinLibraryFunction(node.getID(), node.getPosition())

        # Check for main function and if it has type integer
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

        # Generate the setup code for this function definition
        self.codeBuilder.visit(node)

        # Check if function has a return statement
        hasReturnStatement = False

        # Iterate the statements in the function body
        for declstat in node.functionBody:
            # Check if the return expression matches the returntype of the function
            if type(declstat) == ReturnNode:
                self.checkType(declstat.expressionNode, functionType['idType'], node.getPosition())
                hasReturnStatement = True

            print("Got class:",type(declstat))
            retType = None
            if type(declstat) == IfStatementNode or type(declstat) == IterationStatementNode:
                print("in here")
                retType = self.visit(declstat)

            if type(declstat) != IfStatementNode and type(declstat) != IterationStatementNode:
                retType = self.visit(declstat)
                self.codeBuilder.visit(declstat)

            # Calculate extreme pointer
            # retType = self.visit(declstat)

            # Compare type from return statement
            if retType and 'returnStat' in retType:
                retType.pop('returnStat')
                return

        if functionType['idType'] != '' and hasReturnStatement == False and functionName != "main":
            raise noReturnStatement(node.getPosition())

        # Implicit return statement for the function
        self.codeBuilder.implicitReturn()

        # End the function scope
        self.symbolTable.endScope()

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        identifier = node.declarator
        exprList = identifier.arrayExpressionList
        arraySize = 0
        if len(exprList) != 0:
            arraySize = int(exprList[0].value)
            if len(exprList) != 1:
                raise wrongArrayDimension(node.getID(), node.getPosition())

        if (self.symbolTable.insertSymbol(node.getID(), 
            node.getType(), arraySize=arraySize) == None):
                raise declarationException(node.getID(), 
                    node.getType(), False, node.getPosition())

    def visitAssignmentNode(self, node:AssignmentNode):
        # Compare types
        item = self.symbolTable.lookupSymbol(node.getID())
        if item == None: raise unknownVariable(node.getID(), node.getPosition())
        arrExprList = node.identifier.arrayExpressionList
        if item.arraySize:
            if len(arrExprList) == 0:
                raise wrongArrayDefinition(node.getPosition())
            if len(arrExprList) > 1:
                raise wrongArrayDimension(node.getID(), node.getPosition())

        exprType = self.visit(node.expression)

        # *b = 5
        declType = copy.deepcopy(item.type)
        if node.dereferenceCount > 0:
            declType['refCount'] -= node.dereferenceCount
        if declType['refCount'] < 0:
            raise deReference(node.getPosition())
        if exprType['idType'] != declType['idType']:
            raise wrongType(exprType['idType'], declType['idType'], node.getPosition())

    def visitIfStatementNode(self, node:IfStatementNode):
        # Check if expression is boolean
        exprType = self.visit(node.condition)
        declType = {'idType': "b", 'refCount': 0}
        if exprType != declType:     
            raise wrongType(exprType['idType'], declType['idType'], node.getPosition())
        # Code building for if-else
        labels = self.codeBuilder.visit(node)

        # If scope
        print("Before", self.symbolTable)
        self.symbolTable.createScope(labels[0])
        if node.ifBody != None: #Sem analysis
            for declStat in node.ifBody:
                print(type(declStat))
                self.visit(declStat)
        print("After",self.symbolTable)
        # Code generation
        self.codeBuilder.visitIfBody(node.ifBody, labels[0], labels[1])
        self.symbolTable.endScope()
        print("After last", self.symbolTable)

        # Else scope
        self.symbolTable.createScope(labels[1])
        if node.elseBody != None:  # Sem analysis
            for declStat in node.elseBody:
                self.visit(declStat)
        # Code generation
        self.codeBuilder.visitElseBody(node.elseBody, labels[0], labels[1])
        self.symbolTable.endScope()

    def visitIterationStatementNode(self, node:IterationStatementNode):
        self.isInLoop = True
        declType = {'idType': "b", 'refCount': 0}
        if node.statementName == "While":
            self.symbolTable.createScope("While_scope")
            # Check if while expression is boolean
            exprType = self.visit(node.left)
            if exprType != declType: raise conditionException(exprType['idType'], node.getPosition())
            # visit function body
            for declStat in node.right:
                self.visit(declStat)
        if node.statementName == "For":
            self.symbolTable.createScope("For_scope")
            # TODO forloop semantic checks
            # Check for loop
            if node.left == None and node.middle1 == None and node.middle2 == None:
                # For loop with no statements in the body
                if node.right == []:
                    self.isInLoop = False
                    return
                for declStat in node.right:
                    self.visit(declStat)
            # Check if initialization is valid
            if node.left != None:
                self.visit(node.left)

            # Check if condition is valid
            if node.middle1 != None:
                exprType = self.visit(node.middle1)
                if exprType != declType: raise conditionException(exprType['idType'], node.middle1.getPosition())

            # Check if updation is valid
            if node.middle2 != None:
                if type(node.middle2) == BinaryOperationNode:
                    if (node.middle2.getOperator() not in ["/","*","+","++","-","--","="]):
                        raise wrongForloop(node.middle2.getOperator(), node.middle2.getPosition())
                print(type(node.middle2))
                self.visit(node.middle2)

            # Execute body
            if node.right != None:
                for declStat in node.right:
                    self.visit(declStat)

        # Code generation
        self.codeBuilder.visit(node)

        # End scope of loop
        self.symbolTable.endScope()
        self.isInLoop = False

    def visitReturnNode(self, node:ReturnNode):
        # Return a expression(identifier, functioncall, binary operation etc)
        if node.expressionNode:
            exprType = self.visit(node.expressionNode)
            return exprType
        # Return nothing
        return {'returnStat': True, 'idType': None, 'refCount': 0}

    def visitBreakNode(self, node:BreakNode):
        if not self.isInLoop: raise outsideLoopException("break", node.getPosition())

    def visitContinueNode(self, node:ContinueNode):
        if not self.isInLoop: raise outsideLoopException("continue", node.getPosition())

    def visitDeclarationNode(self, node:DeclarationNode):
        declType = node.getType()
        arrExprList = node.identifier.arrayExpressionList
        arraySize = 0
        if len(arrExprList) > 0:
            arraySize = int(arrExprList[0].value)
            if len(arrExprList) > 1:
                raise wrongArrayDimension(node.getID(), node.getPosition())           
        if node.expression:
            # Compare types
            print("he")
            if isinstance(node.expression, list):
                for elem in node.expression:
                    # Check when index is an identifier:
                    # No reference to an existing variable => Throw unknownVariable exception
                    # Identifier has other type than integer => Throw wrongArrayIndexType exception
                    if type(elem) == IdentifierNode and node.expression.index(elem) != len(node.expression)-1:
                        if self.symbolTable.lookupSymbol(elem.getID()) == None:
                            raise unknownVariable(elem.getID(), elem.getPosition())
                        if self.symbolTable.lookupSymbol(elem.getID()).type['idType'] != 'i':
                            raise wrongArrayIndexType(self.symbolTable.lookupSymbol(elem.getID()).type['idType'], elem.getPosition())
                    if type(elem) == FloatingConstantNode or type(elem) == CharacterConstantNode or type(elem) == StringConstantNode:
                        raise wrongArrayIndexType(elem.getType(), elem.getPosition())
            if type(node.expression) == InitializerListNode:
                exprs = node.expression.expressions
                # Check if all elements in the initializer list are the same type as the declType
                for expr in exprs:
                    curType = self.visit(expr)
                    if curType != declType:
                        raise wrongType(curType['idType'], declType['idType'], expr.getPosition())
            if type(node.expression) == FunctionCallNode: self.visit(node.expression)
            self.checkType(node.expression, declType['idType'], node.getPosition())
        print('here')
        if self.symbolTable.insertSymbol(node.getID(), declType, arraySize=arraySize) == None:
            raise declarationException(node.getID(), 
                declType['idType'], False, node.getPosition())
        print("HALOO",self.symbolTable)

    def visitBinaryOperationNode(self, node:BinaryOperationNode):
        exprTypeLeft = self.visit(node.left)
        exprTypeRight = self.visit(node.right)
        if (exprTypeRight['refCount'] > 0 or
            exprTypeLeft['refCount'] > 0):
            raise wrongOperation("add/subtract/mul or div", "an address", node.getPosition())
        typeLeft = exprTypeLeft['idType']
        typeRight = exprTypeRight['idType']
        if (node.operator == "&&" or node.operator == "||"):
            if (typeLeft != {'idType': "b", 'refCount': 0} or 
                typeRight != {'idType': "b", 'refCount': 0}):
                raise wrongOperation("&& and ||", 
                    typeLeft, node.getPosition(), typeRight)
        if (node.operator != "+" and node.operator != "-" 
            and node.operator != "*" and node.operator != "/"):
            exprTypeLeft = {'idType': "b", 'refCount': 0}
        return exprTypeLeft
            
    def visitExpressionNode(self, node:ExpressionNode):
        exprType = None
        if node.isPostfix:
            item = self.symbolTable.lookupSymbol(node.child.getID(), node.child)
            if item == None: raise unknownVariable(node.child.getID(), node.getPosition())
            # Id++ or Id-- works for all types except for char 
            # TODO Test if it works for floats/addresses
            # Get the type of the identifier
            exprType = self.visit(node.child)
            if exprType['idType'] == "c" and exprType['refCount'] == 0:
                raise incrementError(exprType['idType'],node.getPosition())
        return exprType

    def visitDereferenceExpressionNode(self, node:DereferenceExpressionNode):
        item = self.symbolTable.lookupSymbol(node.child.getID(), node.child)
        if item == None: raise unknownVariable(node.child.getID(), node.getPosition())
        if item.type['refCount'] < node.derefCount:
            raise deReference(node.getPosition())
        # Decrease the reference count of the exprType
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] -= node.derefCount
        return exprType

    def visitReferenceExpressionNode(self, node:ReferenceExpressionNode):
        item = self.symbolTable.lookupSymbol(node.child.getID(), node.child)
        if item == None: raise unknownVariable(node.child.getID(), node.getPosition())
        # Increase the reference count of the exprType
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] += 1
        return exprType  

    def visitFunctionCallNode(self, node:FunctionCallNode):
        item = self.symbolTable.lookupSymbol(node.getID() + "()")
        if (node.getID() == "printf" or node.getID() == "scanf") and item == None:
            # Added specific exception for the inclusion of printf and scanf
            raise includeException(node.getID(), node.getPosition())
        if item == None: raise unknownVariable(node.getID()+"()", node.getPosition(), True)
        if node.getID() == "printf" or node.getID() == "scanf":
            # No arguments were provided
            if node.argumentExpressionListNode == None:
                raise conflictingArgumentLength(node.getID(), 0, 1, node.getPosition())

            # Handle included printf and scanf functions as inline code.
            args = node.argumentExpressionListNode.argumentExprs

            # Check if there are arguments present if the string contains % signs
            if len(args) == 1:
                # If first argument isn't a string constant node => raise error
                if type(args[0]) != StringConstantNode: raise requiredStringConstant(node.getID(), node.getPosition())
                firstArgument = args[0].value
                if self.countConversions(firstArgument) != 0:
                    raise conversionWarning(node.getID(), node.getPosition())


            argType = self.visit(args[0])
            # Check if first argument is a Char array
            if type(args[0]) != StringConstantNode:
                raise requiredStringConstant(node.getID(), node.getPosition())

            print(node.getID(),":",type(args[0]))
            # First Argument is a string literal
            argsIndex = 1
            stringLit = str(args[0].value)
            presentConversions = self.countConversions(stringLit)
            for index, char in enumerate(stringLit):
                if char == "%" and index+1 < len(stringLit):
                    if index != 0 and stringLit[index-1] == "%":
                        continue
                    tempType = self.visit(args[argsIndex])
                    if len(args) - 1 != presentConversions:
                        raise conflictingArgumentLength(node.getID(), len(args)-1, presentConversions, node.getPosition())


                    if node.getID() == "printf":
                        if type(args[argsIndex]) == IdentifierNode or \
                            type(args[argsIndex]) == StringConstantNode or \
                            type(args[argsIndex]) == FloatingConstantNode or \
                            type(args[argsIndex]) == CharacterConstantNode or \
                            type(args[argsIndex]) == IntegerConstantNode: continue
                        raise printfTypes(node.getPosition())

                    if type(args[argsIndex]) != IdentifierNode:
                        if node.getID() == "scanf":
                            if tempType['refCount'] != 1: raise onlyBasicTypes(node.getPosition())

                    nextChar = stringLit[index+1]
                    if (nextChar == "i" and tempType['idType'] == "i" or
                        nextChar == "d" and tempType['idType'] == "i" or
                        nextChar == "f" and tempType['idType'] == "r" or
                        nextChar == "c" and tempType['idType'] == "c" or
                        nextChar == "s" and (tempType['idType'] == "c" and "isArray" in tempType)):
                            if (nextChar == "s" and type(args[argsIndex]) != IdentifierNode): raise stringScanError(node.getPosition())
                            argsIndex += 1
                            continue
                    else:
                        raise wrongTypeCode(tempType['idType'], nextChar, node.getPosition())
            return {'idType': "i", 'refCount': 0}

        params = item.parameters # List of parameterDeclNode
        args = []
        if node.argumentExpressionListNode:
            args = node.argumentExpressionListNode.argumentExprs

        if len(params) != len(args):
            raise conflictingParameterLength(node.getID(), len(args), len(params), node.getPosition())
        for i in range(len(params)):
            paramType = params[i].getType()
            argType = self.visit(args[i])
            if argType != paramType:
                 raise parameterTypeError(node.getID(), argType['idType'], paramType['idType'], node.getPosition())
            # Type is an array while the parameter is not
            if len(item.parameters[i].declarator.arrayExpressionList) == 0:
                raise parameterTypeError(node.getID(), "array", argType['idType'], node.getPosition())
            paramArraySize = int(item.parameters[i].declarator.arrayExpressionList[0].value)
            argItem = None
            if type(args[i]) == IdentifierNode:
                argItem = self.symbolTable.lookupSymbol(args[i].getID(), args[i])
            if paramArraySize:
                if (type(args[i]) != IdentifierNode or not argItem.arraySize
                    or len(args[i].arrayExpressionList) != 0):
                    raise parameterTypeError(node.getID(), args[i].getType(), "array", node.getPosition())
            if argItem and paramArraySize != argItem.arraySize:
                raise conflictingArgumentLength(node.getID(), node.getPosition())
        return item.type    

    def visitIntegerConstantNode(self, node:IntegerConstantNode):
        return {'idType': "i", 'refCount': 0}

    def visitFloatingConstantNode(self, node:FloatingConstantNode):
        return {'idType': "r", 'refCount': 0}

    def visitCharacterConstantNode(self, node:CharacterConstantNode):
        return {'idType': "c", 'refCount': 0}

    def visitStringConstantNode(self, node:StringConstantNode):
        return {'idType': "c", 'refCount': 0, 'isArray': True}

    def visitDeclarationSpecifierNode(self, node:DeclarationSpecifierNode):
        pass   

    def visitIdentifierNode(self, node:IdentifierNode):
        item = self.symbolTable.lookupSymbol(node.getID())
        if item == None: raise unknownVariable(node.getID(), node.getPosition())
        if len(node.arrayExpressionList) > 0:        
            exprType = self.visit(node.arrayExpressionList[0])
            if exprType['idType'] != "i":
                raise wrongArrayIndexType(exprType['idType'], node.getPosition())
        return item.type

    def visitForwardFunctionDeclarationNode(self, node:ForwardFunctionDeclarationNode):
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        if not self.symbolTable.insertSymbol(node.getID()+"()", 
            node.declarationSpecifier.getType(), 
            params=parameters, isForwardDecl=True):
            knownType = self.symbolTable.lookupSymbol(node.getID()+"()").type['idType']
            raise declarationException(node.getID(), knownType, True, node.getPosition())

# ====[Helper methods]====

    # Check if declstat has the same type as correctType
    def checkType(self, declStat, correctType, position):
        if type(declStat) == IdentifierNode:
            if self.symbolTable.lookupSymbol(declStat.getID()) == None:
                raise unknownVariable(declStat.getID(), declStat.getPosition())
            retType = self.symbolTable.lookupSymbol(declStat.getID()).type['idType']
            if retType != correctType:
                raise wrongReturnType(retType, correctType, position)

        # If statement contains a function call
        elif type(declStat) == FunctionCallNode:
            if self.symbolTable.lookupSymbol(declStat.getID() + "()") == None:
                raise unknownVariable(declStat.getID() + "()", declStat.getPosition())
            retType = self.symbolTable.lookupSymbol(declStat.getID() + "()").type['idType']
            if retType != correctType:
                raise wrongReturnType(retType, correctType, position)

        # If statement is an expression
        elif type(declStat) == ExpressionNode and declStat.getType() != correctType:
            raise wrongReturnType(declStat.getType(), correctType, position)

        # If statement is a constant
        elif type(declStat) == CharacterConstantNode or type(declStat) == FloatingConstantNode or type(declStat) == IntegerConstantNode:
            if declStat.getType() != correctType:
                raise wrongReturnType(declStat.getType(), correctType, position)


        # Check if when the statement is a binary operation,
        # If all the types in the expression match the type
        elif type(declStat) == BinaryOperationNode:
            types = declStat.getType()
            for i in types:
                if type(i) == IdentifierNode:
                    if self.symbolTable.lookupSymbol(i.getID()) == None:
                        raise unknownVariable(i.getID(), i.getPosition())
                    i = self.symbolTable.lookupSymbol(i.getID()).type['idType']
                if type(i) == FunctionCallNode:
                    if self.symbolTable.lookupSymbol(i.getID()+"()") == None:
                        raise unknownVariable(i.getID()+"()", i.getPosition(), True)
                    i = self.symbolTable.lookupSymbol(i.getID() + "()").type['idType']
                if i != correctType:
                    raise wrongReturnExpression(i, correctType, position)

    # Count the % signs in the string literal
    def countConversions(self, stringLiteral):
        conversions = 0
        conversions += stringLiteral.count("%c")
        conversions += stringLiteral.count("%i")
        conversions += stringLiteral.count("%f")
        conversions += stringLiteral.count("%d")
        conversions += stringLiteral.count("%s")
        return conversions
