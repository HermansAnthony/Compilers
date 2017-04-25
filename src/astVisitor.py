from astNode import *

class AstVisitor():
    def visit(self, node:ASTNode):
        return node.accept(self)
 
    def visitProgramNode(self, node:ProgramNode):
        for child in node.children:
            self.visit(child)

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        if node.declarationSpecifier:
            self.visit(node.declarationSpecifier)
        self.visit(node.identifier)
        if parameterList:
            self.visit(node.parameterList)
        self.visit(node.functionBody)

    def visitParameterList(self, node:ParameterListNode):
        for paramDecl in node.paramDecls:
            self.visit(paramDecl)

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        self.visit(node.declarationSpecifier)
        self.visit(node.declarator)

    def visitDeclarationNode(self, node:DeclarationNode):
        self.visit(node.declarationSpecifier)
        self.visit(node.identifier)
        self.visit(node.expression)

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
        self.visit(node.expressionNode)

    def visitBreakNode(self, node:BreakNode):
        pass

    def visitContinueNode(self, node:ContinueNode):
        pass
    
    def visitBinaryOperationNode(self, node:BinaryOperationNode):
        self.visit(node.left)
        self.visit(node.right)

    def visitExpressionNode(self, node:ExpressionNode):
        self.visit(node.child)

    def visitFunctionCallNode(self, node:FunctionCallNode):
        self.visit(node.identifier)
        self.visit(node.argumentExpressionListNode)

    def visitArgumentExpressionListNode(self, node:ArgumentExpressionListNode):
        for expr in node.argumentExprs:
            self.visit(expr)

    def visitIntegerConstantNode(self, node:IntegerConstantNode):
        pass

    def visitFloatingConstantNode(self, node:FloatingConstantNode):
        pass

    def visitCharacterConstantNode(self, node:CharacterConstantNode):
        pass

    def visitDeclarationSpecifierNode(self, node:DeclarationSpecifierNode):
        pass

    def visitIdentifierNode(self, node:IdentifierNode):
        for expression in node.arrayExpressionList:
            self.visit(expression)     
  
     
