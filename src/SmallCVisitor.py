# Generated from SmallC.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SmallCParser import SmallCParser
else:
    from SmallCParser import SmallCParser

# This class defines a complete generic visitor for a parse tree produced by SmallCParser.

class SmallCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SmallCParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:SmallCParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#genericSelection.
    def visitGenericSelection(self, ctx:SmallCParser.GenericSelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#genericAssocList.
    def visitGenericAssocList(self, ctx:SmallCParser.GenericAssocListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#genericAssociation.
    def visitGenericAssociation(self, ctx:SmallCParser.GenericAssociationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#postfixExpression.
    def visitPostfixExpression(self, ctx:SmallCParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:SmallCParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#unaryExpression.
    def visitUnaryExpression(self, ctx:SmallCParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#unaryOperator.
    def visitUnaryOperator(self, ctx:SmallCParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#castExpression.
    def visitCastExpression(self, ctx:SmallCParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:SmallCParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:SmallCParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#shiftExpression.
    def visitShiftExpression(self, ctx:SmallCParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#relationalExpression.
    def visitRelationalExpression(self, ctx:SmallCParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#equalityExpression.
    def visitEqualityExpression(self, ctx:SmallCParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#andExpression.
    def visitAndExpression(self, ctx:SmallCParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:SmallCParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:SmallCParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:SmallCParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:SmallCParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:SmallCParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:SmallCParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:SmallCParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#expression.
    def visitExpression(self, ctx:SmallCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#constantExpression.
    def visitConstantExpression(self, ctx:SmallCParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#declaration.
    def visitDeclaration(self, ctx:SmallCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#declarationSpecifiers.
    def visitDeclarationSpecifiers(self, ctx:SmallCParser.DeclarationSpecifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#declarationSpecifiers2.
    def visitDeclarationSpecifiers2(self, ctx:SmallCParser.DeclarationSpecifiers2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx:SmallCParser.DeclarationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:SmallCParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#initDeclarator.
    def visitInitDeclarator(self, ctx:SmallCParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:SmallCParser.StorageClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:SmallCParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx:SmallCParser.StructOrUnionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#structOrUnion.
    def visitStructOrUnion(self, ctx:SmallCParser.StructOrUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#structDeclarationList.
    def visitStructDeclarationList(self, ctx:SmallCParser.StructDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#structDeclaration.
    def visitStructDeclaration(self, ctx:SmallCParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx:SmallCParser.SpecifierQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#structDeclaratorList.
    def visitStructDeclaratorList(self, ctx:SmallCParser.StructDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#structDeclarator.
    def visitStructDeclarator(self, ctx:SmallCParser.StructDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:SmallCParser.EnumSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#enumeratorList.
    def visitEnumeratorList(self, ctx:SmallCParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#enumerator.
    def visitEnumerator(self, ctx:SmallCParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#enumerationConstant.
    def visitEnumerationConstant(self, ctx:SmallCParser.EnumerationConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#atomicTypeSpecifier.
    def visitAtomicTypeSpecifier(self, ctx:SmallCParser.AtomicTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#typeQualifier.
    def visitTypeQualifier(self, ctx:SmallCParser.TypeQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx:SmallCParser.FunctionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#alignmentSpecifier.
    def visitAlignmentSpecifier(self, ctx:SmallCParser.AlignmentSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#declarator.
    def visitDeclarator(self, ctx:SmallCParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#directDeclarator.
    def visitDirectDeclarator(self, ctx:SmallCParser.DirectDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#gccDeclaratorExtension.
    def visitGccDeclaratorExtension(self, ctx:SmallCParser.GccDeclaratorExtensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#gccAttributeSpecifier.
    def visitGccAttributeSpecifier(self, ctx:SmallCParser.GccAttributeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#gccAttributeList.
    def visitGccAttributeList(self, ctx:SmallCParser.GccAttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#gccAttribute.
    def visitGccAttribute(self, ctx:SmallCParser.GccAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#nestedParenthesesBlock.
    def visitNestedParenthesesBlock(self, ctx:SmallCParser.NestedParenthesesBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#pointer.
    def visitPointer(self, ctx:SmallCParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#typeQualifierList.
    def visitTypeQualifierList(self, ctx:SmallCParser.TypeQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:SmallCParser.ParameterTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#parameterList.
    def visitParameterList(self, ctx:SmallCParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:SmallCParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#identifierList.
    def visitIdentifierList(self, ctx:SmallCParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#typeName.
    def visitTypeName(self, ctx:SmallCParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:SmallCParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#directAbstractDeclarator.
    def visitDirectAbstractDeclarator(self, ctx:SmallCParser.DirectAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#typedefName.
    def visitTypedefName(self, ctx:SmallCParser.TypedefNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#initializer.
    def visitInitializer(self, ctx:SmallCParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#initializerList.
    def visitInitializerList(self, ctx:SmallCParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#designation.
    def visitDesignation(self, ctx:SmallCParser.DesignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#designatorList.
    def visitDesignatorList(self, ctx:SmallCParser.DesignatorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#designator.
    def visitDesignator(self, ctx:SmallCParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx:SmallCParser.StaticAssertDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#statement.
    def visitStatement(self, ctx:SmallCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#labeledStatement.
    def visitLabeledStatement(self, ctx:SmallCParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#compoundStatement.
    def visitCompoundStatement(self, ctx:SmallCParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#blockItemList.
    def visitBlockItemList(self, ctx:SmallCParser.BlockItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#blockItem.
    def visitBlockItem(self, ctx:SmallCParser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#expressionStatement.
    def visitExpressionStatement(self, ctx:SmallCParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#selectionStatement.
    def visitSelectionStatement(self, ctx:SmallCParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#iterationStatement.
    def visitIterationStatement(self, ctx:SmallCParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#jumpStatement.
    def visitJumpStatement(self, ctx:SmallCParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#compilationUnit.
    def visitCompilationUnit(self, ctx:SmallCParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#translationUnit.
    def visitTranslationUnit(self, ctx:SmallCParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx:SmallCParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#declarationList.
    def visitDeclarationList(self, ctx:SmallCParser.DeclarationListContext):
        return self.visitChildren(ctx)



del SmallCParser