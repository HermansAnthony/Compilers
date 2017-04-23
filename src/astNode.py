nodeCounter = 0
def counter():
    global nodeCounter
    returnValue = nodeCounter
    nodeCounter += 1
    return returnValue

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
        print("A dot file with name ", name, " was created.")
        astStringFormat = 'digraph G {\n'
        astStringFormat += str(self)
        astStringFormat += '}'
        output = open(name, 'w')
        output.write(astStringFormat)
        output.close()

    def __str__(self):
        currentNode = counter()
        returnValue = str(currentNode) + ' [label="Program"];\n'
        for child in self.children:
            returnValue += str(currentNode) + ' -> ' + str(child)
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
        label = "Decl-" + str(self.expression) + ":\n " + str(self.identifier)
        returnValue = str(currentNode) + ';\n'
        returnValue += str(currentNode) + ' [label="' + label + '" ];\n'
        return returnValue

class IfStatementNode(ASTNode):
    def __init__(self, condition, ifBody, elseBody):
        self.condition = condition
        self.ifBody = ifBody
        self.elseBody = elseBody

    def accept(self, visitor):
        return visitor.visitIfStatementNode(self)

    def __str__(self):
        return "IfElse"

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
        return "Iter"

class ReturnNode(ASTNode):
    def __init__(self, expressionNode):
        self.expressionNode = expressionNode

    def accept(self, visitor):
        return visitor.ReturnNode(self)

    def __str__(self):
        return "return"

class ContinueNode(ASTNode):
    def accept(self, visitor):
        return visitor.ContinueNode(self)

    def __str__(self):
        return "continue"

class BreakNode(ASTNode):
    def accept(self, visitor):
        return visitor.BreakNode(self)

    def __str__(self):
        return "break"

class BinaryOperationNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.BinaryOperationNode(self)

    def __str__(self):
        returnValue = str(self.operator) + ' -> ' + str(self.left) + ';'
        returnValue += str(self.operator) + ' -> ' + str(self.right) + ';'
        return returnValue

class ExpressionNode(ASTNode):
    def __init__(self, operator, isPostfix, child):
        self.operator = operator
        self.isPostfix = isPostfix
        self.child = child

    def accept(self, visitor):
        return visitor.ExpressionNode(self)

    def __str__(self):
        return "expression"

class IntegerConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.IntegerConstantNode(self)

    def __str__(self):
        returnValue = 'Integer'
        return returnValue

class FloatingConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.FloatingConstantNode(self)

    def __str__(self):
        returnValue = 'Float:'
        returnValue += self.value
        return returnValue

class CharacterConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.CharacterConstantNode(self)

    def __str__(self):
        returnValue = 'Character: '
        returnValue += self.value
        return returnValue

class DeclarationSpecifierNode(ASTNode):
    def __init__(self, isConstant, idType, hasPointer):
        self.isConstant = isConstant
        self.idType = idType
        self.hasPointer = hasPointer

    def accept(self, visitor):
        return visitor.DeclarationSpecifierNode(self)

    def __str__(self):
        currentNode = counter()
        label = ''
        if self.isConstant: label += 'const '
        if self.hasPointer: label += '*'
        print(self.idType)
        returnValue = str(currentNode) + ';\n'
        returnValue += str(currentNode) + ' [label = "' + label + '"];\n'
        return returnValue


class IdentifierNode(ASTNode):
    def __init__(self, identifier, arrayExpressionList):
        self.identifier = identifier
        self.arrayExpressionList = arrayExpressionList

    def accept(self, visitor):
        return visitor.IdentifierNode(self)

    def __str__(self):
        return self.identifier
