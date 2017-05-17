from astNode import *
from CmmVisitor import CmmVisitor
from CmmParser import CmmParser

class AstBuilder(CmmVisitor):

    def visitChildren(self, node):
        result = self.defaultResult()
        n = node.getChildCount()
        if n == 1:
            return node.getChild(0).accept(self)
        result = []
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            if not childResult:
                continue
            if isinstance(childResult, list):
                result.extend(childResult)
            else:
                result.append(childResult)
        return result

    def visitProgram(self, ctx:CmmParser.ProgramContext):
        return ProgramNode(self.visitChildren(ctx))

    def visitExternalDeclaration(self, ctx:CmmParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)

    def visitFunctionDeclaration(self, ctx:CmmParser.FunctionDeclarationContext):
        declarationSpecifier = None
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.declarationSpecifier():
            declarationSpecifier = self.visit(ctx.declarationSpecifier())
        identifier = self.visitIdentifier(ctx.Identifier(), place)
        parameterListNode = None
        if ctx.parameterList():
            parameterListNode = self.visit(ctx.parameterList())
        if ctx.compoundStatement():
            functionBody = self.visit(ctx.compoundStatement())
            return FunctionDefinitionNode(declarationSpecifier, identifier, parameterListNode, functionBody, place)
        return ForwardFunctionDeclarationNode(declarationSpec, identifier, parameterListNode)

    def visitParameterList(self, ctx:CmmParser.ParameterListContext):
        paramDecls = [self.visit( ctx.parameterDeclaration() )]
        if ctx.parameterList():
            result = self.visit( ctx.parameterList() )
            paramDecls.extend(result.paramDecls)
        return ParameterListNode(paramDecls)

    def visitParameterDeclaration(self, ctx:CmmParser.ParameterDeclarationContext):
        declarationSpecifier = self.visit( ctx.declarationSpecifier() )
        result = self.visit( ctx.declarator() )
        idNode = result[-1]
        idNode.arrayExpressionList = list(reversed(result[:-1]))
        return ParameterDeclarationNode(declarationSpecifier, idNode)

    def visitDeclaration(self, ctx:CmmParser.DeclarationContext):
        declarationSpec = self.visit(ctx.declarationSpecifier())
        identifier, expression = self.visit(ctx.initDeclarator())
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        return DeclarationNode(declarationSpec, identifier, expression, place)

    def visitDeclarationSpecifier(self, ctx:CmmParser.DeclarationSpecifierContext):
        idType = ctx.typeSpecifier().getText()
        return DeclarationSpecifierNode(idType, len(ctx.Star()))

    def visitInitDeclarator(self, ctx:CmmParser.InitDeclaratorContext):
        result = self.visit( ctx.declarator() )
        idNode = result[-1]
        idNode.arrayExpressionList = list(reversed(result[:-1]))
        if ctx.expression() == None:
            return [idNode, None]
        return [idNode, self.visit(ctx.expression())]

    def visitDeclarator(self, ctx:CmmParser.DeclaratorContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.getChildCount() == 1:
            return [self.visitIdentifier(ctx.Identifier(), place)]
        resList = [self.visit( ctx.expression() )]
        resList.extend( self.visit(ctx.declarator()) )
        return resList

    def visitPrimaryExpression(self, ctx:CmmParser.PrimaryExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.Identifier():
            return self.visitIdentifier(ctx, place)
        return self.visit(ctx.constant())                            

    def visitIdentifier(self, ctx, place):
        return IdentifierNode(ctx.getText(), [], place)

    def visitConstant(self, ctx:CmmParser.ConstantContext):
        if ctx.Character():
            return CharacterConstantNode(ctx.getText())
        if ctx.String():
            # TODO String is recognized for printf and scanf
            return CharacterConstantNode(ctx.getText())
        return self.visitChildren(ctx)

    def visitIntegerConstant(self, ctx:CmmParser.IntegerConstantContext):
        return IntegerConstantNode(ctx.getText())

    def visitFloatingConstant(self, ctx:CmmParser.FloatingConstantContext):
        return FloatingConstantNode(ctx.getText())

    def visitExpression(self, ctx:CmmParser.ExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.Star():
            # Star+ (Identifier | arrayExpression)
            if ctx.Identifier():
                identifier =  self.visitIdentifier(ctx.Identifier(), place)
                return DereferenceExpressionNode(len(ctx.Star()), identifier)
            result = self.visit( ctx.arrayExpression() )
            idNode = result[-1]
            idNode.arrayExpressionList = list(reversed(result[:-1]))
            return DereferenceExpressionNode(len(ctx.Star()), idNode)
        if ctx.getChildCount() == 1:
            # arrayExpression | primaryExpression | functionCallExpression
            if ctx.arrayExpression():
                result = self.visit( ctx.arrayExpression() )
                idNode = result[-1]
                idNode.arrayExpressionList = list(reversed(result[:-1]))
                return idNode
            if ctx.primaryExpression():
                t = self.visit(ctx.primaryExpression())
                return t
            return self.visit(ctx.functionCallExpression())
        if ctx.getChildCount() == 2:
            if ctx.And():
                # And (Identifier | arrayExpression)
                if ctx.Identifier():
                    identifier =  self.visitIdentifier(ctx.Identifier(), place)
                    return ReferenceExpressionNode(identifier)
                result = self.visit( ctx.arrayExpression() )
                idNode = result[-1]
                idNode.arrayExpressionList = list(reversed(result[:-1]))
                return ReferenceExpressionNode(idNode)
            # (Identifier | arrayExpression) PlusPlus 
            # (Identifier | arrayExpression) MinusMinus
            if ctx.Identifier():
                return ExpressionNode(ctx.getChild(1).getText(), 
                    True, self.visitIdentifier(ctx.Identifier(), place))
            result = self.visit( ctx.arrayExpression() )
            idNode = result[-1]
            idNode.arrayExpressionList = list(reversed(result[:-1])) 
            return ExpressionNode(ctx.getChild(1).getText(), 
                True, idNode)          
        if ctx.getChildCount() == 3:
            # expression binaryOperator expression
            expr0 = self.visit( ctx.expression(0) )
            expr1 = self.visit( ctx.expression(1) ) 
            if isinstance(expr0, list): 
                # first expression is an array expression
                idNode = expr0[-1]
                idNode.arrayExpressionList = list(reversed(result[:-1]))
                return BinaryOperationNode( ctx.binaryOperator().getText(),
                    self.visit(idNode), expr1)                 
            return BinaryOperationNode(ctx.binaryOperator().getText(), expr0, expr1)

    def visitFunctionCallExpression(self, ctx:CmmParser.FunctionCallExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        identifier = self.visitIdentifier(ctx.Identifier(), place)
        argExprNode = None
        if ctx.argumentExpressionList():
            exprList = list(reversed( self.visit(ctx.argumentExpressionList()) ))
            argExprNode = ArgumentExpressionListNode(exprList)
        return FunctionCallNode(identifier, argExprNode, place)
      
    def visitArrayExpression(self, ctx:CmmParser.ArrayExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.Identifier() != None:
            idNode = self.visitIdentifier(ctx.Identifier(), place)
            return [idNode]
        resList = [self.visit(ctx.expression())]
        resList.extend(self.visit(ctx.arrayExpression()))
        return resList

    def visitArgumentExpressionList(self, ctx:CmmParser.ArgumentExpressionListContext):
        if ctx.argumentExpressionList():
            result = [self.visit(ctx.expression())]
            result.extend(self.visit(ctx.argumentExpressionList()))
            return result
        return [self.visit(ctx.expression())]

    def visitStatement(self, ctx:CmmParser.StatementContext):
        # (Identifier | arrayExpression) PlusPlus 
        # (Identifier | arrayExpression) MinusMinus
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.Identifier():
            return ExpressionNode(ctx.getChild(1).getText(), 
                True, self.visitIdentifier(ctx.Identifier(), place))
        if ctx.arrayExpression():
            result = self.visit( ctx.arrayExpression() )
            idNode = result[-1]
            idNode.arrayExpressionList = list(reversed(result[:-1])) 
            return ExpressionNode(ctx.getChild(1).getText(), 
                True, idNode)          
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx:CmmParser.AssignmentContext):
        result = self.visit( ctx.declarator() )
        idNode = result[-1]
        idNode.arrayExpressionList = list(reversed(result[:-1]))
        expression = self.visit( ctx.expression() )
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        return AssignmentNode(len(ctx.Star()), idNode, expression, place);

    def visitCompoundStatement(self, ctx:CmmParser.CompoundStatementContext):
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx:CmmParser.IfStatementContext):
        ifBody = self.visit(ctx.compoundStatement(0))
        elseBody = None
        if ctx.Else():
            elseBody = self.visit(ctx.compoundStatement(1))
        return IfStatementNode(self.visit(ctx.expression()), ifBody, elseBody)

    def visitIterationStatement(self, ctx:CmmParser.IterationStatementContext):
        if ctx.While():
            return IterationStatementNode("While", self.visit(ctx.expression(0)), None, None, self.visit(ctx.compoundStatement()))
        left = None
        middle1 = None
        middle2 = None
        right = self.visit(ctx.compoundStatement())
        if ctx.declaration():
            left = self.visit(ctx.declaration())
        if ctx.assignment():
            left = self.visit(ctx.assignment())
        if ctx.expression(0):
            middle1 = self.visit(ctx.expression(0))
        if ctx.expression(1):
            middle2 = self.visit(ctx.expression(1))
        return IterationStatementNode("For", left, middle1, middle2, right)

    def visitJumpStatement(self, ctx:CmmParser.JumpStatementContext):
        if ctx.Continue():
            return ContinueNode()
        if ctx.Break():
            return BreakNode()
        if ctx.expression():
            return ReturnNode(self.visit(ctx.expression()))    
        return ReturnNode(None)

