from astNode import *
from CmmVisitor import CmmVisitor
from CmmParser import CmmParser

class astBuilder(CmmVisitor):
    #def __init__(self, name):
    #    self.tree = None
    #    self.name = name

    def visitProgram(self, ctx:CmmParser.ProgramContext):
        return ProgramNode(self.visitChildren(ctx))

    def visitExternalDeclaration(self, ctx:CmmParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)

    def visitFunctionDefinition(self, ctx:CmmParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)

    def visitParameterList(self, ctx:CmmParser.ParameterListContext):
        return self.visitChildren(ctx)

    def visitParameterDeclaration(self, ctx:CmmParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)

    def visitDeclaration(self, ctx:CmmParser.DeclarationContext):
        declarationSpec = self.visit(ctx.declarationSpecifier())
        identifier, expression = self.visit(ctx.initDeclarator())
        return DeclarationNode(declarationSpec, identifier, expression)

    def visitDeclarationSpecifier(self, ctx:CmmParser.DeclarationSpecifierContext):
        isConstant = ctx.Const() != None
        idType = ctx.typeSpecifier().getText()
        hasPointer = ctx.Star() != None
        return DeclarationSpecifierNode(isConstant, idType, hasPointer)

    def visitInitDeclarator(self, ctx:CmmParser.InitDeclaratorContext):
        return [self.visit(ctx.declarator()), self.visit(ctx.expression())]

    def visitDeclarator(self, ctx:CmmParser.DeclaratorContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        # If the declarator is an array element.
        # Recursively fill the arrayExpressionList
        node = self.visit( ctx.declarator() )
        node.arrayExpressionList.append( self.visit(ctx.expression()) )    
        return node

    def visitPrimaryExpression(self, ctx:CmmParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)

    def visitIdentifier(self, ctx:CmmParser.IdentifierContext):
        return IdentifierNode(self.visit( ctx.identifier() ), [])

    def visitConstant(self, ctx:CmmParser.ConstantContext):
        return self.visitChildren(ctx)

    def visitIntegerConstant(self, ctx:CmmParser.IntegerConstantContext):
        return IntegerConstantNode(ctx.getText())

    def visitFloatingConstant(self, ctx:CmmParser.FloatingConstantContext):
        return FloatingConstantNode(ctx.getText())

    def visitCharacterConstant(self, ctx:CmmParser.CharacterConstantContext):
        return CharacterConstantNode(ctx.getText())

    def visitExpression(self, ctx:CmmParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOperationNode( ctx.binaryOperator().getText(), self.visit( ctx.postfixExpression() ), self.visit( ctx.expression() ) )        

    def visitPostfixExpression(self, ctx:CmmParser.PostfixExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        if ctx.getChildCount() == 2:
            return PostfixExpressionNode(ctx.getChild(1).getText(), self.visit( ctx.primaryExpression() ))
        node = self.visit( ctx.postfixExpression() )
        if isinstance(node, IdentifierNode):
            node.arrayExpressionList.append( self.visit(ctx.expression()) )
        else:
            print("Semantic Error: Cannot select array index on a constant expression.")
        return node

    def visitArgumentExpressionList(self, ctx:CmmParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx:CmmParser.StatementContext):
        return self.visitChildren(ctx)

    def visitCompoundStatement(self, ctx:CmmParser.CompoundStatementContext):
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx:CmmParser.IfStatementContext):
        return self.visitChildren(ctx)

    def visitIterationStatement(self, ctx:CmmParser.IterationStatementContext):
        return self.visitChildren(ctx)

    def visitJumpStatement(self, ctx:CmmParser.JumpStatementContext):
        return self.visitChildren(ctx)

    # Overloaded print function for the print function
    # Writes AST tree to a dot file
    def __repr__(self):
        print("A dot file with name ", self.name, " is created for the AST")
        # TODO insert real ast nodes in string version here
        astStringFormat = 'digraph G { "Hello" -> "World"}'
        # astStringFormat = str(self.tree)
        output = open(self.name, 'w')
        output.write(astStringFormat)
        output.close()

