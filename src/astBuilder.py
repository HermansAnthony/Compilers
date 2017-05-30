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
        if ctx.Include():
            return StdioNode()
        return self.visitChildren(ctx)

    def visitFunctionDeclaration(self, ctx:CmmParser.FunctionDeclarationContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        declarationSpec = None
        if ctx.declarationSpecifier():
            declarationSpec = self.visit(ctx.declarationSpecifier())
        identifier = self.visitIdentifier(ctx.Identifier())
        parameterListNode = None
        if ctx.parameterList():
            parameterListNode = self.visit(ctx.parameterList())
            parameterListNode.paramDecls = list(reversed(parameterListNode.paramDecls))
        if ctx.compoundStatement():
            functionBody = self.visit(ctx.compoundStatement())
            return FunctionDefinitionNode(declarationSpec, identifier, parameterListNode, functionBody, place)
        return ForwardFunctionDeclarationNode(declarationSpec, identifier, parameterListNode, place)

    def visitParameterList(self, ctx:CmmParser.ParameterListContext):
        paramDecls = [self.visit( ctx.parameterDeclaration() )]
        if ctx.parameterList():
            result = self.visit( ctx.parameterList() )
            paramDecls.extend(result.paramDecls)
        return ParameterListNode(paramDecls)

    def visitParameterDeclaration(self, ctx:CmmParser.ParameterDeclarationContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        declarationSpecifier = self.visit( ctx.declarationSpecifier() )
        idNode = self.visit( ctx.declarator() )
        return ParameterDeclarationNode(declarationSpecifier, idNode, place)

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
        if ctx.Identifier():
            return [self.visitIdentifier(ctx.Identifier()), self.visit(ctx.expression())]
        idNode = self.visit( ctx.declarator() )
        if ctx.initializerList() == None:
            return [idNode, None]
        return [idNode, self.visit(ctx.initializerList())]

    def visitDeclarator(self, ctx:CmmParser.DeclaratorContext):
        idNode = self.visitIdentifier(ctx.Identifier())
        if ctx.getChildCount() == 4:
        	idNode.arrayExpressionList = [self.visit( ctx.integerConstant() )]
        return idNode

    def visitInitializerList(self, ctx:CmmParser.initializerList):
        exprs = []
        for expr in ctx.expression():
            exprs.append(self.visit(expr))
        if len(exprs) > 0:
            return InitializerListNode(exprs)
        return None

    def visitPrimaryExpression(self, ctx:CmmParser.PrimaryExpressionContext):
        if ctx.Identifier():
            return self.visitIdentifier(ctx)
        return self.visit(ctx.constant())                            

    def visitIdentifier(self, ctx):
        # Place is for semantic analysis (line-column position)
        place = ""
        if str(type(ctx)) == "<class 'antlr4.tree.Tree.TerminalNodeImpl'>":
            place += str(ctx.getSymbol().line) + ", position " + str(ctx.getSymbol().column)
        else:
            place += str(ctx.start.line) + ", position " + str(ctx.start.column)
        return IdentifierNode(ctx.getText(), [], place)

    def visitConstant(self, ctx:CmmParser.ConstantContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.Character():
            return CharacterConstantNode(ctx.getText(), place)
        if ctx.String():
            return StringConstantNode(ctx.getText(), place)
        return self.visitChildren(ctx)

    def visitIntegerConstant(self, ctx:CmmParser.IntegerConstantContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        return IntegerConstantNode(ctx.getText(), place)

    def visitFloatingConstant(self, ctx:CmmParser.FloatingConstantContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        return FloatingConstantNode(ctx.getText(), place)

    def visitExpression(self, ctx:CmmParser.ExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.additiveExpression() and ctx.getChildCount() == 1: return self.visit(ctx.additiveExpression())
        if ctx.getChildCount() == 3:
            expr0 = self.visit(ctx.expression())
            expr1 = self.visit(ctx.additiveExpression())
            if ctx.OrOr(): return BinaryOperationNode(ctx.OrOr().getText(), expr0, expr1, place)
            if ctx.AndAnd(): return BinaryOperationNode(ctx.AndAnd().getText(), expr0, expr1, place)
            if ctx.Equal(): return BinaryOperationNode(ctx.Equal().getText(), expr0, expr1, place)
            if ctx.NotEqual(): return BinaryOperationNode(ctx.NotEqual().getText(), expr0, expr1, place)
            if ctx.Less(): return BinaryOperationNode(ctx.Less().getText(), expr0, expr1, place)
            if ctx.Greater(): return BinaryOperationNode(ctx.Greater().getText(), expr0, expr1, place)
            if ctx.LessEqual(): return BinaryOperationNode(ctx.LessEqual().getText(), expr0, expr1, place)
            return BinaryOperationNode(ctx.GreaterEqual().getText(), expr0, expr1, place)
        return None

    def visitFunctionCallExpression(self, ctx:CmmParser.FunctionCallExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        identifier = self.visitIdentifier(ctx.Identifier())
        argExprNode = None
        if ctx.argumentExpressionList():
            exprList = list(reversed( self.visit(ctx.argumentExpressionList()) ))
            argExprNode = ArgumentExpressionListNode(exprList)
        return FunctionCallNode(identifier, argExprNode, place)
      
    def visitArrayExpression(self, ctx:CmmParser.ArrayExpressionContext):
        idNode = self.visitIdentifier(ctx.Identifier())
        if ctx.getChildCount() == 4:
            idNode.arrayExpressionList = [self.visit(ctx.expression())]
        return idNode

    def visitArgumentExpressionList(self, ctx:CmmParser.ArgumentExpressionListContext):
        if ctx.argumentExpressionList():
            result = [self.visit(ctx.expression())]
            result.extend(self.visit(ctx.argumentExpressionList()))
            return result
        return [self.visit(ctx.expression())]

    def visitAdditiveExpression(self, ctx:CmmParser.AdditiveExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        # multiplicativeExpression
        if ctx.getChildCount() == 1: return self.visit(ctx.multiplicativeExpression())
        if ctx.getChildCount() == 3:
            # additiveExpression Plus multiplicativeExpression
            # additiveExpression Minus multiplicativeExpression
            expr0 = self.visit(ctx.additiveExpression())
            expr1 = self.visit(ctx.multiplicativeExpression())
            if ctx.Plus(): return BinaryOperationNode(ctx.Plus().getText(), expr0, expr1, place)
            return BinaryOperationNode(ctx.Minus().getText(), expr0, expr1, place)
        return None

    def visitMultiplicativeExpression(self, ctx:CmmParser.MultiplicativeExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.getChildCount() == 1: return self.visit(ctx.atomExpression())
        if ctx.getChildCount() == 3:
            # multiplicativeExpression Star atomExpression
            # multiplicativeExpression Div atomExpression
            expr0 = self.visit(ctx.multiplicativeExpression())
            expr1 = self.visit(ctx.atomExpression())
            if ctx.Star(): return BinaryOperationNode(ctx.Star().getText(), expr0, expr1, place)
            return BinaryOperationNode(ctx.Div().getText(), expr0, expr1, place)
        return None

    def visitAtomExpression(self, ctx:CmmParser.AtomExpressionContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.getChildCount() == 1:
            if ctx.primaryExpression(): return self.visit(ctx.primaryExpression())
            if ctx.arrayExpression(): return self.visitArrayExpression(ctx.arrayExpression())
            if ctx.functionCallExpression(): return self.visitFunctionCallExpression(ctx.functionCallExpression())
        if ctx.getChildCount() == 2:
            if ctx.Star():
                # Star+ (Identifier | arrayExpression)
                if ctx.Identifier():
                    identifier =  self.visitIdentifier(ctx.Identifier())
                    return DereferenceExpressionNode(len(ctx.Star()), identifier, place)
                result = self.visit( ctx.arrayExpression() )
                idNode = result[-1]
                idNode.arrayExpressionList = list(reversed(result[:-1]))
                return DereferenceExpressionNode(len(ctx.Star()), idNode, place)

            if ctx.And():
                # And (Identifier | arrayExpression)
                if ctx.Identifier():
                    identifier =  self.visitIdentifier(ctx.Identifier())
                    return ReferenceExpressionNode(identifier, place)
                result = self.visit( ctx.arrayExpression() )
                idNode = result[-1]
                idNode.arrayExpressionList = list(reversed(result[:-1]))
                return ReferenceExpressionNode(idNode, place)

            # (Identifier | arrayExpression) PlusPlus
            # (Identifier | arrayExpression) MinusMinus
            if ctx.Identifier():
                return ExpressionNode(ctx.getChild(1).getText(), True, self.visitIdentifier(ctx.Identifier()), place)
            result = self.visit(ctx.arrayExpression())
            idNode = result[-1]
            idNode.arrayExpressionList = list(reversed(result[:-1]))
            return ExpressionNode(ctx.getChild(1).getText(), True, idNode, place)
        if ctx.getChildCount() == 3:
            # LeftParen expression RightParen
            return self.visitExpression(ctx.getChild(1))

    def visitStatement(self, ctx:CmmParser.StatementContext):
        # (Identifier | arrayExpression) PlusPlus 
        # (Identifier | arrayExpression) MinusMinus
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.Identifier():
            return ExpressionNode(ctx.getChild(1).getText(), 
                True, self.visitIdentifier(ctx.Identifier()), place)
        if ctx.arrayExpression():
            result = self.visit( ctx.arrayExpression() )
            idNode = result[-1]
            idNode.arrayExpressionList = list(reversed(result[:-1])) 
            return ExpressionNode(ctx.getChild(1).getText(), 
                True, idNode, place)
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx:CmmParser.AssignmentContext):
        idNode = self.visit( ctx.declarator() )
        expression = self.visit( ctx.expression() )
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        return AssignmentNode(len(ctx.Star()), idNode, expression, place)

    def visitCompoundStatement(self, ctx:CmmParser.CompoundStatementContext):
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx:CmmParser.IfStatementContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        ifBody = self.visit(ctx.compoundStatement(0))
        elseBody = None
        if ctx.Else():
            elseBody = self.visit(ctx.compoundStatement(1))
        return IfStatementNode(self.visit(ctx.expression()), ifBody, elseBody, place)

    def visitIterationStatement(self, ctx:CmmParser.IterationStatementContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.While():
            return IterationStatementNode("While", self.visit(ctx.expression(0)), None, None, self.visit(ctx.compoundStatement()), place)
        left = None
        middle1 = None
        middle2 = None
        right = self.visit(ctx.compoundStatement())
        if ctx.declaration():
            left = self.visit(ctx.declaration())
            if ctx.expression(0): middle1 = self.visit(ctx.expression(0))
            if ctx.expression(1): middle2 = self.visit(ctx.expression(1))
            if ctx.assignment(): middle2 = self.visit(ctx.assignment())

        if not ctx.declaration():
            if ctx.assignment(0): left = self.visit(ctx.assignment(0))
            if ctx.expression(0): middle1 = self.visit(ctx.expression(0))
            if ctx.expression(1): middle2 = self.visit(ctx.expression(1))
            if ctx.assignment(1): middle2 = self.visit(ctx.assignment())

        return IterationStatementNode("For", left, middle1, middle2, right, place)

    def visitJumpStatement(self, ctx:CmmParser.JumpStatementContext):
        # Place is for semantic analysis (line-column position)
        place = str(ctx.start.line) + ", position " + str(ctx.start.column)
        if ctx.Continue():
            return ContinueNode(place)
        if ctx.Break():
            return BreakNode(place)
        if ctx.expression():
            return ReturnNode(self.visit(ctx.expression()))    
        return ReturnNode(None)

