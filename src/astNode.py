nodeCounter = 0
def counter():
    global nodeCounter
    returnValue = nodeCounter
    nodeCounter += 1
    return str(returnValue)

class ASTNode:
    def accept(self, visitor):
        return

class ProgramNode(ASTNode):
    def __init__(self, children):
        self.children = children

    def accept(self, visitor):
        return visitor.visitProgramNode(self)

    # Writes AST tree to a dot file
    def toDot(self, name):
        #print("A dot file with name ", name, " was created.")
        astStringFormat = 'digraph G {\n'
        astStringFormat += str(self)
        astStringFormat += '}'
        output = open(name, 'w')
        output.write(astStringFormat)
        output.close()

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ' [label="Program"];\n'
        for child in self.children:
            returnValue += currentNode + ' -> ' + str(child)
        return returnValue

class StdioNode(ASTNode):
    def __init__(self):   
        pass

    def accept(self, visitor):
        return visitor.visitStdioNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ' [label="Include Stdio.h"];\n'
        return returnValue

class FunctionDefinitionNode(ASTNode):
    def __init__(self, declarationSpecifier, identifier, parameterList, functionBody, position):
        self.declarationSpecifier = declarationSpecifier
        self.identifier = identifier
        self.parameterList = parameterList
        self.functionBody = functionBody
        self.position = position

    def accept(self, visitor):
        return visitor.visitFunctionDefinitionNode(self)

    def getID(self):
        return self.identifier.getID()

    def getType(self):
        return self.declarationSpecifier.getType()

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        label = "Function"
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label="'+ label + '"];\n '
        if self.declarationSpecifier:
            returnValue += currentNode + '->' + str(self.declarationSpecifier)
        returnValue += currentNode + '->' + str(self.identifier)
        if self.parameterList:
            returnValue += currentNode + '->' + str(self.parameterList)
        body = counter()
        returnValue += currentNode + '->' + body + ';\n'
        returnValue += body + '[ label = "body"];\n'
        for declstat in self.functionBody:
            returnValue += body + '->' + str(declstat)
        return returnValue

class ParameterListNode(ASTNode):
    def __init__(self, paramDecls):
        self.paramDecls = paramDecls

    def accept(self, visitor):
        return visitor.visitParameterListNode(self)

    def getParams(self):
        params = list()
        if isinstance(self.paramDecls, list):
            params.extend(self.paramDecls)
        else:
            params.append(self.paramDecls)
        return params

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label="ParamList"];\n'
        if isinstance(self.paramDecls, list):
            for paramDecl in self.paramDecls:
                returnValue += currentNode + '->' + str(paramDecl)
        else:
            returnValue += currentNode + '->' + str(self.paramDecls)
        return returnValue

class ParameterDeclarationNode(ASTNode):
    def __init__(self, declarationSpecifier, declarator, position):
        self.declarationSpecifier = declarationSpecifier
        self.declarator = declarator
        self.position = position

    def accept(self, visitor):
        return visitor.visitParameterDeclarationNode(self)

    def getType(self):
        return self.declarationSpecifier.getType()

    def getID(self):
        return self.declarator.getID()

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label = "ParamDecl"];\n'
        returnValue += currentNode + '->' + str(self.declarationSpecifier)
        returnValue += currentNode + '->' + str(self.declarator)
        return returnValue

class InitializerListNode(ASTNode):
    def __init__(self, expressions):
        self.expressions = expressions

    def accept(self, visitor):
        return visitor.visitInitializerListNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label = "InitList"];\n'
        for expr in self.expressions:
            returnValue += currentNode + '->' + str(expr)
        return returnValue 

class DeclarationNode(ASTNode):
    def __init__(self, declarationSpecifier, identifier, expression, position):
        self.declarationSpecifier = declarationSpecifier
        self.identifier = identifier
        self.expression = expression
        self.position = position

    def accept(self, visitor):
        return visitor.visitDeclarationNode(self)

    def getType(self):
        return self.declarationSpecifier.getType()

    def getID(self):
        return self.identifier.getID()

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label="Decl" ];\n'
        returnValue += currentNode + '->' + str(self.declarationSpecifier)
        returnValue += currentNode + '->' + str(self.identifier)
        if self.expression:
            returnValue += currentNode + '->' + str(self.expression)
        return returnValue

class AssignmentNode(ASTNode):
    def __init__(self, dereferenceCount, identifier, expression, position):
        self.dereferenceCount = dereferenceCount
        self.identifier = identifier
        self.expression = expression
        self.position = position

    def accept(self, visitor):
        return visitor.visitAssignmentNode(self)

    def getID(self):
        return self.identifier.getID()

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        label = 'Assignment:\n'
        if self.dereferenceCount != 0: 
            label += str(self.dereferenceCount) + ' Dereferences'
        returnValue += currentNode + ' [label = "' + label + '"];\n'
        returnValue += currentNode + '->' + str(self.identifier)
        if self.expression:
            returnValue += currentNode + '->' + str(self.expression)
        return returnValue

class ForwardFunctionDeclarationNode(ASTNode):
    def __init__(self, declarationSpecifier, identifier, parameterList, position):
        self.declarationSpecifier = declarationSpecifier
        self.identifier = identifier
        self.parameterList = parameterList
        self.position = position

    def accept(self, visitor):
        return visitor.visitForwardFunctionDeclarationNode(self)

    def getID(self):
        return self.identifier.getID()

    def getType(self):
        return self.declarationSpecifier.getType()

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        label = "Function"
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label="'+ label + '"];\n '
        if self.declarationSpecifier:
            returnValue += currentNode + '->' + str(self.declarationSpecifier)
        returnValue += currentNode + '->' + str(self.identifier)
        if self.parameterList:
            returnValue += currentNode + '->' + str(self.parameterList)
        return returnValue

class IfStatementNode(ASTNode):
    def __init__(self, condition, ifBody, elseBody, position):
        self.condition = condition
        self.ifBody = ifBody
        self.elseBody = elseBody
        self.position = position

    def accept(self, visitor):
        return visitor.visitIfStatementNode(self)

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label = "Branch"];\n'
        conditionNode = counter()
        ifNode = counter()
        elseNode = counter()
        returnValue += currentNode + '->' + conditionNode + ';\n'
        returnValue += currentNode + '->' + ifNode + ';\n'
        returnValue += currentNode + '->' + elseNode + ';\n'
        returnValue += conditionNode + ' [label = "condition"];\n'
        returnValue += ifNode + ' [label = "ifBody"];\n'
        returnValue += elseNode + ' [label = "elseBody"];\n'
        returnValue += conditionNode + '->' + str(self.condition)
        if self.ifBody:
            for stat in self.ifBody:
                returnValue += ifNode + '->' + str(stat)
        if self.elseBody:
            for stat in self.elseBody:
                returnValue += elseNode + '->' + str(stat)
        return returnValue

class IterationStatementNode(ASTNode):
    def __init__(self, statementName, left, middle1, middle2, right, position):
        # condition, body
        # expression1, expression2, expression3, body
        # declaration, expression1, expression2, body
        self.statementName = statementName
        self.left = left
        self.middle1 = middle1
        self.middle2 = middle2
        self.right = right
        self.position = position

    def accept(self, visitor):
        return visitor.visitIterationStatementNode(self)

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[ label = "' + self.statementName + '"];\n'
        if self.left: returnValue += currentNode + '->'+ str(self.left)
        if self.middle1: returnValue += currentNode + '->' + str(self.middle1)
        if self.middle2: returnValue += currentNode + '->' + str(self.middle2)
        body = counter()
        returnValue += currentNode + '->' + body + ';\n'
        returnValue += body + '[ label = "body"];\n'
        for stat in self.right:
            returnValue += body + '->' + str(stat)
        return returnValue

class ReturnNode(ASTNode):
    def __init__(self, expressionNode, position):
        self.expressionNode = expressionNode
        self.position = position

    def accept(self, visitor):
        return visitor.visitReturnNode(self)

    def getPosition(self):
        return str(self.position)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="return"];\n'
        if str(self.expressionNode) != 'None': returnValue +=  currentNode + '->' + str(self.expressionNode)
        return returnValue

class ContinueNode(ASTNode):
    def __init__(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def accept(self, visitor):
        return visitor.visitContinueNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="continue"];\n'
        return returnValue

class BreakNode(ASTNode):
    def __init__(self, position):
        self.position = position

    def accept(self, visitor):
        return visitor.visitBreakNode(self)

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="break"];\n'
        return returnValue

class BinaryOperationNode(ASTNode):
    def __init__(self, operator, left, right, position):
        self.operator = operator
        self.left = left
        self.right = right
        self.position = position

    def accept(self, visitor):
        return visitor.visitBinaryOperationNode(self)

    def getPosition(self):
        return self.position

    def getOperator(self):
        return str(self.operator)

    def getType(self):
        returnValue = list()
        if isinstance(self.left, BinaryOperationNode): returnValue.extend(self.left.getType())
        if isinstance(self.left, IdentifierNode) or isinstance(self.left, FunctionCallNode): returnValue.append(self.left)
        # Characterconstantnode, integerconstantnode, floatingconstant node etc
        if not isinstance(self.left, BinaryOperationNode) and not isinstance(self.left, IdentifierNode) and not isinstance(self.left, FunctionCallNode):
            returnValue.append(self.left.getType())
        if isinstance(self.right, BinaryOperationNode): returnValue.extend(self.right.getType())
        if isinstance(self.right, IdentifierNode) or isinstance(self.right, FunctionCallNode): returnValue.append(self.right)
        # Characterconstantnode, integerconstantnode, floatingconstant node etc
        if not isinstance(self.right, BinaryOperationNode) and not isinstance(self.right, IdentifierNode) and not isinstance(self.right, FunctionCallNode):
            returnValue.append(self.right.getType())
        return returnValue


    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        label = 'BinaryOperation:' + self.operator
        returnValue += currentNode + ' [label = "'+ label + '"];\n'
        returnValue += currentNode + '->' + str(self.left)
        returnValue += currentNode + '->' + str(self.right)
        return returnValue

class ExpressionNode(ASTNode):
    def __init__(self, operator, isPostfix, child, position):
        self.operator = operator
        self.isPostfix = isPostfix
        self.child = child
        self.position = position

    def accept(self, visitor):
        return visitor.visitExpressionNode(self)

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        label = "Expression:" + self.operator
        returnValue += currentNode + ' [ label = "' + label + '"];\n'
        returnValue += currentNode + '->' + str(self.child)
        return returnValue     

class DereferenceExpressionNode(ASTNode):
    def __init__(self, derefCount, child, position):
        self.derefCount = derefCount
        self.child = child
        self.position = position

    def accept(self, visitor):
        return visitor.visitDereferenceExpressionNode(self)

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        label = "DerefExpression:\n"
        label += str(self.derefCount) + ' dereferences'
        returnValue += currentNode + ' [ label = "' + label + '"];\n'
        returnValue += currentNode + '->' + str(self.child)
        return returnValue    

class ReferenceExpressionNode(ASTNode):
    def __init__(self, child, position):
        self.child = child
        self.position = position

    def accept(self, visitor):
        return visitor.visitReferenceExpressionNode(self)

    def getID(self):
        return self.child.getID()

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        label = "ReferenceExpression:\n"
        returnValue += currentNode + ' [ label = "' + label + '"];\n'
        returnValue += currentNode + '->' + str(self.child)
        return returnValue   

class FunctionCallNode(ASTNode):
    def __init__(self, primaryExpression, argumentExpressionListNode, position):
        self.identifier = primaryExpression
        self.argumentExpressionListNode = argumentExpressionListNode
        self.position = position

    def accept(self, visitor):
        return visitor.visitFunctionCallNode(self)

    def getID(self):
        return self.identifier.getID()

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [ label = "FunctionCall"];\n'
        returnValue += currentNode + '->' + str(self.identifier)
        if self.argumentExpressionListNode:
            returnValue += currentNode + '->' + str(self.argumentExpressionListNode)
        return returnValue  

class ArgumentExpressionListNode(ASTNode):
    def __init__(self, argumentExprs):
        self.argumentExprs = argumentExprs

    def accept(self, visitor):
        return visitor.visitArgumentExpressionListNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [ label = "ArgExprList"];\n'
        if isinstance(self.argumentExprs, list):
            for expr in self.argumentExprs:
                returnValue += currentNode + '->' + str(expr)
        else:
            returnValue += currentNode + '->' + str(self.argumentExprs)
        return returnValue 

class IntegerConstantNode(ASTNode):
    def __init__(self, value, position):
        self.value = value
        self.position = position


    def accept(self, visitor):
        return visitor.visitIntegerConstantNode(self)

    def getType(self):
        return "i"

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n';
        returnValue += currentNode + '[label="Integer:\n ' + str(self.value) + '"];\n'
        return returnValue

class FloatingConstantNode(ASTNode):
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def accept(self, visitor):
        return visitor.visitFloatingConstantNode(self)

    def getType(self):
        return "r"

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n';
        returnValue += currentNode + '[label="Float:\n ' + str(self.value) + '"];\n'
        return returnValue

class CharacterConstantNode(ASTNode):
    def __init__(self, value, position):
        self.value = value
        self.position = position


    def accept(self, visitor):
        return visitor.visitCharacterConstantNode(self)

    def getType(self):
        return "c"

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="Character:\n ' + self.value + '"];\n'
        return returnValue

class StringConstantNode(ASTNode):
    def __init__(self, value, position):
        self.value = value + '\0'
        self.position = position

    def accept(self, visitor):
        return visitor.visitStringConstantNode(self)

    def getType(self):
        return "c"

    def getPosition(self):
        return self.position

    def __str__(self):
        tempValue = ""
        for character in self.value:
            if character == '"' or character == "\0": continue
            tempValue+=character
        currentNode = counter()
        returnValue = currentNode + ';\n';
        returnValue += currentNode + '[label="CString:\n ' + tempValue + '"];\n'
        return returnValue

class DeclarationSpecifierNode(ASTNode):
    def __init__(self, idType, pointerCount):
        self.idType = idType
        self.pointerCount = pointerCount

    def accept(self, visitor):
        return visitor.visitDeclarationSpecifierNode(self)

    def getType(self):
        idType = ""
        if self.idType == "int":
            idType = "i"
        elif self.idType == "float":
            idType = "r"
        elif self.idType == "char":
            idType = "c"
        return {'idType': idType, 
            'refCount': self.pointerCount}

    def __str__(self):
        currentNode = counter()
        label = 'DeclSpec:\n'
        if self.pointerCount != 0: 
            label += str(self.pointerCount) + ' pointers'
        label += str(self.idType)
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label = "' + label + '"];\n'
        return returnValue

class IdentifierNode(ASTNode):
    def __init__(self, identifier, arrayExpressionList, position):
        self.identifier = identifier
        self.arrayExpressionList = arrayExpressionList
        self.position = position

    def accept(self, visitor):
        return visitor.visitIdentifierNode(self)

    def getID(self):
        return str(self.identifier)

    def getPosition(self):
        return self.position

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="' +'Identifier:\n'+ str(self.identifier) + '"];\n'
        for expr in self.arrayExpressionList:
            returnValue += currentNode + '->' + str(expr)
        return returnValue
