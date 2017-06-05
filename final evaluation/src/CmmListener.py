# Generated from Cmm.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CmmParser import CmmParser
else:
    from CmmParser import CmmParser

# This class defines a complete listener for a parse tree produced by CmmParser.
class CmmListener(ParseTreeListener):

    # Enter a parse tree produced by CmmParser#program.
    def enterProgram(self, ctx:CmmParser.ProgramContext):
        pass

    # Exit a parse tree produced by CmmParser#program.
    def exitProgram(self, ctx:CmmParser.ProgramContext):
        pass


    # Enter a parse tree produced by CmmParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:CmmParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by CmmParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:CmmParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by CmmParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:CmmParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by CmmParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:CmmParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by CmmParser#parameterList.
    def enterParameterList(self, ctx:CmmParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CmmParser#parameterList.
    def exitParameterList(self, ctx:CmmParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CmmParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:CmmParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by CmmParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:CmmParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by CmmParser#declaration.
    def enterDeclaration(self, ctx:CmmParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CmmParser#declaration.
    def exitDeclaration(self, ctx:CmmParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CmmParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:CmmParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by CmmParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:CmmParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by CmmParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CmmParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CmmParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CmmParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CmmParser#initDeclarator.
    def enterInitDeclarator(self, ctx:CmmParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CmmParser#initDeclarator.
    def exitInitDeclarator(self, ctx:CmmParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by CmmParser#declarator.
    def enterDeclarator(self, ctx:CmmParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CmmParser#declarator.
    def exitDeclarator(self, ctx:CmmParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CmmParser#initializerList.
    def enterInitializerList(self, ctx:CmmParser.InitializerListContext):
        pass

    # Exit a parse tree produced by CmmParser#initializerList.
    def exitInitializerList(self, ctx:CmmParser.InitializerListContext):
        pass


    # Enter a parse tree produced by CmmParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CmmParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CmmParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CmmParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CmmParser#constant.
    def enterConstant(self, ctx:CmmParser.ConstantContext):
        pass

    # Exit a parse tree produced by CmmParser#constant.
    def exitConstant(self, ctx:CmmParser.ConstantContext):
        pass


    # Enter a parse tree produced by CmmParser#integerConstant.
    def enterIntegerConstant(self, ctx:CmmParser.IntegerConstantContext):
        pass

    # Exit a parse tree produced by CmmParser#integerConstant.
    def exitIntegerConstant(self, ctx:CmmParser.IntegerConstantContext):
        pass


    # Enter a parse tree produced by CmmParser#floatingConstant.
    def enterFloatingConstant(self, ctx:CmmParser.FloatingConstantContext):
        pass

    # Exit a parse tree produced by CmmParser#floatingConstant.
    def exitFloatingConstant(self, ctx:CmmParser.FloatingConstantContext):
        pass


    # Enter a parse tree produced by CmmParser#expression.
    def enterExpression(self, ctx:CmmParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CmmParser#expression.
    def exitExpression(self, ctx:CmmParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CmmParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:CmmParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by CmmParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:CmmParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by CmmParser#arrayExpression.
    def enterArrayExpression(self, ctx:CmmParser.ArrayExpressionContext):
        pass

    # Exit a parse tree produced by CmmParser#arrayExpression.
    def exitArrayExpression(self, ctx:CmmParser.ArrayExpressionContext):
        pass


    # Enter a parse tree produced by CmmParser#binaryOperator.
    def enterBinaryOperator(self, ctx:CmmParser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by CmmParser#binaryOperator.
    def exitBinaryOperator(self, ctx:CmmParser.BinaryOperatorContext):
        pass


    # Enter a parse tree produced by CmmParser#atomExpression.
    def enterAtomExpression(self, ctx:CmmParser.AtomExpressionContext):
        pass

    # Exit a parse tree produced by CmmParser#atomExpression.
    def exitAtomExpression(self, ctx:CmmParser.AtomExpressionContext):
        pass


    # Enter a parse tree produced by CmmParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:CmmParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by CmmParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:CmmParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by CmmParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:CmmParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by CmmParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:CmmParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by CmmParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:CmmParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by CmmParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:CmmParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by CmmParser#statement.
    def enterStatement(self, ctx:CmmParser.StatementContext):
        pass

    # Exit a parse tree produced by CmmParser#statement.
    def exitStatement(self, ctx:CmmParser.StatementContext):
        pass


    # Enter a parse tree produced by CmmParser#assignment.
    def enterAssignment(self, ctx:CmmParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CmmParser#assignment.
    def exitAssignment(self, ctx:CmmParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CmmParser#compoundStatement.
    def enterCompoundStatement(self, ctx:CmmParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CmmParser#compoundStatement.
    def exitCompoundStatement(self, ctx:CmmParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CmmParser#ifStatement.
    def enterIfStatement(self, ctx:CmmParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CmmParser#ifStatement.
    def exitIfStatement(self, ctx:CmmParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CmmParser#iterationStatement.
    def enterIterationStatement(self, ctx:CmmParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by CmmParser#iterationStatement.
    def exitIterationStatement(self, ctx:CmmParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by CmmParser#jumpStatement.
    def enterJumpStatement(self, ctx:CmmParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by CmmParser#jumpStatement.
    def exitJumpStatement(self, ctx:CmmParser.JumpStatementContext):
        pass


