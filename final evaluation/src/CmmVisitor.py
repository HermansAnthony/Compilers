# Generated from Cmm.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CmmParser import CmmParser
else:
    from CmmParser import CmmParser

# This class defines a complete generic visitor for a parse tree produced by CmmParser.

class CmmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CmmParser#program.
    def visitProgram(self, ctx:CmmParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx:CmmParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:CmmParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#parameterList.
    def visitParameterList(self, ctx:CmmParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:CmmParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#declaration.
    def visitDeclaration(self, ctx:CmmParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx:CmmParser.DeclarationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:CmmParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#initDeclarator.
    def visitInitDeclarator(self, ctx:CmmParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#declarator.
    def visitDeclarator(self, ctx:CmmParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#initializerList.
    def visitInitializerList(self, ctx:CmmParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CmmParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#constant.
    def visitConstant(self, ctx:CmmParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#integerConstant.
    def visitIntegerConstant(self, ctx:CmmParser.IntegerConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#floatingConstant.
    def visitFloatingConstant(self, ctx:CmmParser.FloatingConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#expression.
    def visitExpression(self, ctx:CmmParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:CmmParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#arrayExpression.
    def visitArrayExpression(self, ctx:CmmParser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#binaryOperator.
    def visitBinaryOperator(self, ctx:CmmParser.BinaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#atomExpression.
    def visitAtomExpression(self, ctx:CmmParser.AtomExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:CmmParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:CmmParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:CmmParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#statement.
    def visitStatement(self, ctx:CmmParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#assignment.
    def visitAssignment(self, ctx:CmmParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#compoundStatement.
    def visitCompoundStatement(self, ctx:CmmParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#ifStatement.
    def visitIfStatement(self, ctx:CmmParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#iterationStatement.
    def visitIterationStatement(self, ctx:CmmParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmmParser#jumpStatement.
    def visitJumpStatement(self, ctx:CmmParser.JumpStatementContext):
        return self.visitChildren(ctx)



del CmmParser