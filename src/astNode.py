class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self, *children):
        self.children = children

class DeclarationNode(ASTNode):
    def __init__(self, declarationSpecifier, identifier, expression):
        self.declarationSpecifier = declarationSpecifier
        self.identifier = identifier
        self.expression = expression

class IfStatementNode(ASTNode):
    def __init__(self, condition, ifBody, elseBody):
        self.condition = condition
        self.ifBody = ifBody
        self.elseBody = elseBody

class IterationStatementNode(ASTNode):
    def __init__(self, left, middle1, middle2, right):
        # condition, body
        # expression1, expression2, expression3, body
        # declaration, expression1, expression2, body
        self.left = left
        self.middle1 = middle1
        self.middle2 = middle2
        self.right = right

class ReturnNode(ASTNode):
    def __init__(self, expressionNode):
        self.expressionNode = expressionNode

class ContinueNode(ASTNode):
    pass
class BreakNode(ASTNode):
    pass

class BinaryOperationNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class PostfixExpressionNode(ASTNode):
    def __init__(self, postfix, child):
        self.postfix = postfix
        self.child = child

class IntegerConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

class FloatingConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

class CharacterConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

class DeclarationSpecifierNode(ASTNode):
    def __init__(self, isConstant, idType, hasPointer):
        self.isConstant = isConstant
        self.idType = idType
        self.hasPointer = hasPointer

class IdentifierNode(ASTNode):
    def __init__(self, identifier, arrayExpressionList):
        self.identifier = identifier
        self.arrayExpressionList = arrayExpressionList
