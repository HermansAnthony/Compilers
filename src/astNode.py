class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self, children):
        self.children = children

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
        returnValue = '1 [label="Program"];\n'
        for child in self.children:
            returnValue += '1 -> '
            returnValue += str(child) 
            returnValue += ';\n'
        return returnValue

class DeclarationNode(ASTNode):
    def __init__(self, declarationSpecifier, identifier, expression):
        self.declarationSpecifier = declarationSpecifier
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return "Decl"

class IfStatementNode(ASTNode):
    def __init__(self, condition, ifBody, elseBody):
        self.condition = condition
        self.ifBody = ifBody
        self.elseBody = elseBody

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

    def __str__(self):
        return "Iter"

class ReturnNode(ASTNode):
    def __init__(self, expressionNode):
        self.expressionNode = expressionNode

    def __str__(self):
        return "return"

class ContinueNode(ASTNode):
    def __str__(self):
        return "continue"
class BreakNode(ASTNode):
    def __str__(self):
        return "break"

class BinaryOperationNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        returnValue = str(self.operator) + ' -> ' + str(self.left) + ';'
        returnValue += str(self.operator) + ' -> ' + str(self.right) + ';'
        return returnValue

class ExpressionNode(ASTNode):
    def __init__(self, operator, isPostfix, child):
        self.operator = operator
        self.isPostfix = isPostfix
        self.child = child
    def __str__(self):
        return "expression"

class IntegerConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        returnValue = 'Integer:'
        returnValue += self.value
        return returnValue

class FloatingConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        returnValue = 'Float: '
        returnValue += self.value
        return returnValue
class CharacterConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        returnValue = 'Character: '
        returnValue += self.value
        return returnValue

class DeclarationSpecifierNode(ASTNode):
    def __init__(self, isConstant, idType, hasPointer):
        self.isConstant = isConstant
        self.idType = idType
        self.hasPointer = hasPointer

    def __str__(self):
        return "Decl"


class IdentifierNode(ASTNode):
    def __init__(self, identifier, arrayExpressionList):
        self.identifier = identifier
        self.arrayExpressionList = arrayExpressionList

    def __str__(self):
        return "ID"
