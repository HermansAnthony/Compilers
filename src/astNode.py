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
        print("idType: ", type(self.identifier))

    def accept(self, visitor):
        return visitor.visitDeclarationNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = str(currentNode) + ';\n'
        returnValue += str(currentNode) + ' [label="Decl" ];\n'
        returnValue += str(currentNode) + '->' + str(self.declarationSpecifier)
        returnValue += str(currentNode) + '->' + str(self.identifier)
        returnValue += str(currentNode) + '->' + str(self.expression)
        return returnValue

class IfStatementNode(ASTNode):
    def __init__(self, condition, ifBody, elseBody):
        self.condition = condition
        self.ifBody = ifBody
        self.elseBody = elseBody

    def accept(self, visitor):
        return visitor.visitIfStatementNode(self)

    def __str__(self):
        currentNode = str(counter())
        returnValue = currentNode + ';\n'
        returnValue += currentNode + ' [label = "Branch"];\n'
        conditionNode = str(counter())
        ifNode = str(counter())
        elseNode = str(counter())
        returnValue += currentNode + '->' + conditionNode + ';\n'
        returnValue += currentNode + '->' + ifNode + ';\n'
        returnValue += currentNode + '->' + elseNode + ';\n'
        returnValue += conditionNode + ' [label = "condition"];\n'
        returnValue += ifNode + ' [label = "ifBody"];\n'
        returnValue += elseNode + ' [label = "elseBody"];\n'
        for stat in self.ifBody:
            returnValue += ifNode + '->' + str(stat)
        for stat in self.elseBody:
            returnValue += elseNode + '->' + str(stat)
        # returnValue += conditionNode + '->' + str(self.condition)

        # print(self.condition)
        # print(self.elseBody)
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
        return "Iter"

class ReturnNode(ASTNode):
    def __init__(self, expressionNode):
        self.expressionNode = expressionNode

    def accept(self, visitor):
        return visitor.ReturnNode(self)

    def __str__(self):
        currentNode = str(counter())
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="return"];\n'
        returnValue +=  currentNode + '->' + str(self.expressionNode)
        return returnValue

class ContinueNode(ASTNode):
    def accept(self, visitor):
        return visitor.ContinueNode(self)

    def __str__(self):
        currentNode = str(counter())
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="continue"];\n'
        return returnValue

class BreakNode(ASTNode):
    def accept(self, visitor):
        return visitor.BreakNode(self)

    def __str__(self):
        currentNode = str(counter())
        returnValue = currentNode + ';\n'
        returnValue += currentNode + '[label="break"];\n'
        return returnValue

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
        currentNode = counter()
        returnValue = str(currentNode) + ';\n';
        returnValue += str(currentNode) + '[label="Integer:\n ' + str(self.value) + '"];\n'
        return returnValue

class FloatingConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.FloatingConstantNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = str(currentNode) + ';\n';
        returnValue += str(currentNode) + '[label="Float:\n ' + str(self.value) + '"];\n'
        return returnValue

class CharacterConstantNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.CharacterConstantNode(self)

    def __str__(self):
        currentNode = counter()
        returnValue = str(currentNode) + ';\n';
        returnValue += str(currentNode) + '[label="Character:\n ' + self.value + '"];\n'
        return returnValue

class DeclarationSpecifierNode(ASTNode):
    def __init__(self, isConstant, idType, hasPointer):
        self.isConstant = isConstant
        self.idType = idType
        self.hasPointer = hasPointer

    def accept(self, visitor):
        return visitor.DeclarationSpecifierNode(self)

    def __str__(self):
        # No need to create empty node
        # if not self.isConstant and not self.hasPointer: return ''
        currentNode = counter()
        label = 'DeclSpec:\n'
        if self.isConstant: label += 'const '
        if self.hasPointer: label += '*'
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
        currentNode = counter()
        returnValue = str(currentNode) + ';\n'
        returnValue += str(currentNode) + '[label="' +'Identifier:\n'+ str(self.identifier) + '"];\n'
        return returnValue
