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

class FunctionDefinitionNode(ASTNode):
    def __init__(self, declarationSpecifier, hasPointer, identifier, parameterList, functionBody):
        self.declarationSpecifier = declarationSpecifier
        # TODO hasPointer
        self.hasPointer = hasPointer
        self.identifier = identifier
        self.parameterList = parameterList
        self.functionBody = functionBody

    def accept(self, visitor):
        return visitor.visitFunctionDefinitionNode(self)

    def __str__(self):
        currentNode = counter()
        label = "Function"
        if self.hasPointer: label += '*'
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
        for stat in self.functionBody:
            returnValue += body + '->' + str(stat)
        return returnValue

class ParameterListNode(ASTNode):
    def __init__(self, paramDecls):
        self.paramDecls = paramDecls

    def accept(self, visitor):
        return visitor.visitParameterListNode(self)

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
    def __init__(self, declarationSpecifier, declarator):
        self.declarationSpecifier = declarationSpecifier
        self.declarator = declarator

    def accept(self, visitor):
        return visitor.visitParameterDeclarationNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label = "ParamDecl"];\n'
        returnValue += currentNode + '->' + str(self.declarationSpecifier)
        returnValue += currentNode + '->' + str(self.declarator)
        return returnValue

class DeclarationNode(ASTNode):
    def __init__(self, declarationSpecifier, identifier, expression):
        self.declarationSpecifier = declarationSpecifier
        self.identifier = identifier
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitDeclarationNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label="Decl" ];\n'
        returnValue += currentNode + '->' + str(self.declarationSpecifier)
        returnValue += currentNode + '->' + str(self.identifier)
        if self.expression:
            returnValue += currentNode + '->' + str(self.expression)
        return returnValue

class ForwardFunctionDeclarationNode(ASTNode):
    def __init__(self, declarationSpecifier, hasPointer, identifier, parameterList):
        self.declarationSpecifier = declarationSpecifier
        # TODO hasPointer
        self.hasPointer = hasPointer
        self.identifier = identifier
        self.parameterList = parameterList

    def accept(self, visitor):
        return visitor.visitForwardFunctionDeclarationNode(self)

    def __str__(self):
        currentNode = counter()
        label = "Function"
        if self.hasPointer: label += '*'
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label="'+ label + '"];\n '
        if self.declarationSpecifier:
            returnValue += currentNode + '->' + str(self.declarationSpecifier)
        returnValue += currentNode + '->' + str(self.identifier)
        if self.parameterList:
            returnValue += currentNode + '->' + str(self.parameterList)
        return returnValue

class IfStatementNode(ASTNode):
    def __init__(self, condition, ifBody, elseBody):
        self.condition = condition
        self.ifBody = ifBody
        self.elseBody = elseBody

    def accept(self, visitor):
        return visitor.visitIfStatementNode(self)

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
        for stat in self.ifBody:
            returnValue += ifNode + '->' + str(stat)
        for stat in self.elseBody:
            returnValue += elseNode + '->' + str(stat)
        return returnValue

class IterationStatementNode(ASTNode):
    def __init__(self, statementName, left, middle1, middle2, right):
        # condition, body
        # expression1, expression2, expression3, body
        # declaration, expression1, expression2, body
        self.statementName = statementName
        self.left = left
        self.middle1 = middle1
        self.middle2 = middle2
        self.right = right

    def accept(self, visitor):
        return visitor.visitIterationStatementNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[ label = "' + self.statementName + '"];\n'
        returnValue += currentNode + '->'+ str(self.left)
        if self.middle1 != None: returnValue += currentNode + '->' + str(self.middle1)
        if self.middle2 != None: returnValue += currentNode + '->' + str(self.middle2)
        body = counter()
        returnValue += currentNode + '->' + body + ';\n'
        returnValue += body + '[ label = "body"];\n'
        for stat in self.right:
            returnValue += body + '->' + str(stat)
        return returnValue

class ReturnNode(ASTNode):
    def __init__(self, expressionNode):
        self.expressionNode = expressionNode

    def accept(self, visitor):
        return visitor.visitReturnNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="return"];\n'
        if str(self.expressionNode) != 'None': returnValue +=  currentNode + '->' + str(self.expressionNode)
        return returnValue

class ContinueNode(ASTNode):
    def accept(self, visitor):
        return visitor.visitContinueNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="continue"];\n'
        return returnValue

class BreakNode(ASTNode):
    def accept(self, visitor):
        return visitor.visitBreakNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="break"];\n'
        return returnValue

class BinaryOperationNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinaryOperationNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        label = 'BinaryOperation:' + self.operator
        returnValue += currentNode + ' [label = "'+ label + '"];\n'
        returnValue += currentNode + '->' + str(self.left)
        returnValue += currentNode + '->' + str(self.right)
        return returnValue

class ExpressionNode(ASTNode):
    def __init__(self, operator, isPostfix, child):
        self.operator = operator
        self.isPostfix = isPostfix
        self.child = child

    def accept(self, visitor):
        return visitor.visitExpressionNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        label = "Expression:" + self.operator
        returnValue += currentNode + ' [ label = "' + label + '"];\n'
        returnValue += currentNode + '->' + str(self.child)
        return returnValue

class FunctionCallNode(ASTNode):
    def __init__(self, primaryExpression, argumentExpressionListNode):
        self.identifier = primaryExpression
        self.argumentExpressionListNode = argumentExpressionListNode

    def accept(self, visitor):
        return visitor.visitFunctionCallNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [ label = "FunctionCall"];\n'
        # TODO
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
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitIntegerConstantNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n';
        returnValue += currentNode + '[label="Integer:\n ' + str(self.value) + '"];\n'
        return returnValue

class FloatingConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitFloatingConstantNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n';
        returnValue += currentNode + '[label="Float:\n ' + str(self.value) + '"];\n'
        return returnValue

class CharacterConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitCharacterConstantNode(self)

    def __str__(self):
        if "\"" in self.value:
            # TODO
            return ""
        currentNode = counter()
        returnValue = currentNode + ';\n';
        returnValue += currentNode + '[label="Character:\n ' + self.value + '"];\n'
        return returnValue

class DeclarationSpecifierNode(ASTNode):
    def __init__(self, isConstant, idType, hasPointer):
        self.isConstant = isConstant
        self.idType = idType
        self.hasPointer = hasPointer

    def accept(self, visitor):
        return visitor.visitDeclarationSpecifierNode(self)

    def __str__(self):
        currentNode = counter()
        label = 'DeclSpec:\n'
        if self.isConstant: label += 'const '
        if self.hasPointer: label += '*'
        label += str(self.idType)
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label = "' + label + '"];\n'
        return returnValue

class IdentifierNode(ASTNode):
    def __init__(self, identifier, arrayExpressionList):
        self.identifier = identifier
        self.arrayExpressionList = arrayExpressionList

    def accept(self, visitor):
        return visitor.visitIdentifierNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="' +'Identifier:\n'+ str(self.identifier) + '"];\n'
        for expr in self.arrayExpressionList:
            returnValue += currentNode + '->' + str(expr)
        return returnValue
