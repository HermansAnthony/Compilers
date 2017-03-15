# Generated from SmallC.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SmallCParser import SmallCParser
else:
    from SmallCParser import SmallCParser

# This class defines a complete listener for a parse tree produced by SmallCParser.
class SmallCListener(ParseTreeListener):

    # Enter a parse tree produced by SmallCParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:SmallCParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:SmallCParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#genericSelection.
    def enterGenericSelection(self, ctx:SmallCParser.GenericSelectionContext):
        pass

    # Exit a parse tree produced by SmallCParser#genericSelection.
    def exitGenericSelection(self, ctx:SmallCParser.GenericSelectionContext):
        pass


    # Enter a parse tree produced by SmallCParser#genericAssocList.
    def enterGenericAssocList(self, ctx:SmallCParser.GenericAssocListContext):
        pass

    # Exit a parse tree produced by SmallCParser#genericAssocList.
    def exitGenericAssocList(self, ctx:SmallCParser.GenericAssocListContext):
        pass


    # Enter a parse tree produced by SmallCParser#genericAssociation.
    def enterGenericAssociation(self, ctx:SmallCParser.GenericAssociationContext):
        pass

    # Exit a parse tree produced by SmallCParser#genericAssociation.
    def exitGenericAssociation(self, ctx:SmallCParser.GenericAssociationContext):
        pass


    # Enter a parse tree produced by SmallCParser#postfixExpression.
    def enterPostfixExpression(self, ctx:SmallCParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#postfixExpression.
    def exitPostfixExpression(self, ctx:SmallCParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:SmallCParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by SmallCParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:SmallCParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by SmallCParser#unaryExpression.
    def enterUnaryExpression(self, ctx:SmallCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#unaryExpression.
    def exitUnaryExpression(self, ctx:SmallCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#unaryOperator.
    def enterUnaryOperator(self, ctx:SmallCParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by SmallCParser#unaryOperator.
    def exitUnaryOperator(self, ctx:SmallCParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by SmallCParser#castExpression.
    def enterCastExpression(self, ctx:SmallCParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#castExpression.
    def exitCastExpression(self, ctx:SmallCParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:SmallCParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:SmallCParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:SmallCParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:SmallCParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#shiftExpression.
    def enterShiftExpression(self, ctx:SmallCParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#shiftExpression.
    def exitShiftExpression(self, ctx:SmallCParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#relationalExpression.
    def enterRelationalExpression(self, ctx:SmallCParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#relationalExpression.
    def exitRelationalExpression(self, ctx:SmallCParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#equalityExpression.
    def enterEqualityExpression(self, ctx:SmallCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#equalityExpression.
    def exitEqualityExpression(self, ctx:SmallCParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#andExpression.
    def enterAndExpression(self, ctx:SmallCParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#andExpression.
    def exitAndExpression(self, ctx:SmallCParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:SmallCParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:SmallCParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:SmallCParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:SmallCParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:SmallCParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:SmallCParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:SmallCParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:SmallCParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:SmallCParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:SmallCParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:SmallCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:SmallCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:SmallCParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by SmallCParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:SmallCParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by SmallCParser#expression.
    def enterExpression(self, ctx:SmallCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#expression.
    def exitExpression(self, ctx:SmallCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#constantExpression.
    def enterConstantExpression(self, ctx:SmallCParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#constantExpression.
    def exitConstantExpression(self, ctx:SmallCParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#declaration.
    def enterDeclaration(self, ctx:SmallCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by SmallCParser#declaration.
    def exitDeclaration(self, ctx:SmallCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:SmallCParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by SmallCParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:SmallCParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by SmallCParser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx:SmallCParser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by SmallCParser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx:SmallCParser.DeclarationSpecifiers2Context):
        pass


    # Enter a parse tree produced by SmallCParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:SmallCParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:SmallCParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:SmallCParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by SmallCParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:SmallCParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by SmallCParser#initDeclarator.
    def enterInitDeclarator(self, ctx:SmallCParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by SmallCParser#initDeclarator.
    def exitInitDeclarator(self, ctx:SmallCParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by SmallCParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:SmallCParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:SmallCParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:SmallCParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:SmallCParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:SmallCParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:SmallCParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#structOrUnion.
    def enterStructOrUnion(self, ctx:SmallCParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by SmallCParser#structOrUnion.
    def exitStructOrUnion(self, ctx:SmallCParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by SmallCParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:SmallCParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by SmallCParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:SmallCParser.StructDeclarationListContext):
        pass


    # Enter a parse tree produced by SmallCParser#structDeclaration.
    def enterStructDeclaration(self, ctx:SmallCParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by SmallCParser#structDeclaration.
    def exitStructDeclaration(self, ctx:SmallCParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:SmallCParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by SmallCParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:SmallCParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by SmallCParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:SmallCParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by SmallCParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:SmallCParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by SmallCParser#structDeclarator.
    def enterStructDeclarator(self, ctx:SmallCParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by SmallCParser#structDeclarator.
    def exitStructDeclarator(self, ctx:SmallCParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by SmallCParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:SmallCParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:SmallCParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#enumeratorList.
    def enterEnumeratorList(self, ctx:SmallCParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by SmallCParser#enumeratorList.
    def exitEnumeratorList(self, ctx:SmallCParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by SmallCParser#enumerator.
    def enterEnumerator(self, ctx:SmallCParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by SmallCParser#enumerator.
    def exitEnumerator(self, ctx:SmallCParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by SmallCParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:SmallCParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by SmallCParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:SmallCParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by SmallCParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:SmallCParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:SmallCParser.AtomicTypeSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#typeQualifier.
    def enterTypeQualifier(self, ctx:SmallCParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#typeQualifier.
    def exitTypeQualifier(self, ctx:SmallCParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:SmallCParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:SmallCParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#alignmentSpecifier.
    def enterAlignmentSpecifier(self, ctx:SmallCParser.AlignmentSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#alignmentSpecifier.
    def exitAlignmentSpecifier(self, ctx:SmallCParser.AlignmentSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#declarator.
    def enterDeclarator(self, ctx:SmallCParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by SmallCParser#declarator.
    def exitDeclarator(self, ctx:SmallCParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by SmallCParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:SmallCParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by SmallCParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:SmallCParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by SmallCParser#gccDeclaratorExtension.
    def enterGccDeclaratorExtension(self, ctx:SmallCParser.GccDeclaratorExtensionContext):
        pass

    # Exit a parse tree produced by SmallCParser#gccDeclaratorExtension.
    def exitGccDeclaratorExtension(self, ctx:SmallCParser.GccDeclaratorExtensionContext):
        pass


    # Enter a parse tree produced by SmallCParser#gccAttributeSpecifier.
    def enterGccAttributeSpecifier(self, ctx:SmallCParser.GccAttributeSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#gccAttributeSpecifier.
    def exitGccAttributeSpecifier(self, ctx:SmallCParser.GccAttributeSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#gccAttributeList.
    def enterGccAttributeList(self, ctx:SmallCParser.GccAttributeListContext):
        pass

    # Exit a parse tree produced by SmallCParser#gccAttributeList.
    def exitGccAttributeList(self, ctx:SmallCParser.GccAttributeListContext):
        pass


    # Enter a parse tree produced by SmallCParser#gccAttribute.
    def enterGccAttribute(self, ctx:SmallCParser.GccAttributeContext):
        pass

    # Exit a parse tree produced by SmallCParser#gccAttribute.
    def exitGccAttribute(self, ctx:SmallCParser.GccAttributeContext):
        pass


    # Enter a parse tree produced by SmallCParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:SmallCParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by SmallCParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:SmallCParser.NestedParenthesesBlockContext):
        pass


    # Enter a parse tree produced by SmallCParser#pointer.
    def enterPointer(self, ctx:SmallCParser.PointerContext):
        pass

    # Exit a parse tree produced by SmallCParser#pointer.
    def exitPointer(self, ctx:SmallCParser.PointerContext):
        pass


    # Enter a parse tree produced by SmallCParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:SmallCParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by SmallCParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:SmallCParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by SmallCParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:SmallCParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by SmallCParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:SmallCParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by SmallCParser#parameterList.
    def enterParameterList(self, ctx:SmallCParser.ParameterListContext):
        pass

    # Exit a parse tree produced by SmallCParser#parameterList.
    def exitParameterList(self, ctx:SmallCParser.ParameterListContext):
        pass


    # Enter a parse tree produced by SmallCParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:SmallCParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by SmallCParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:SmallCParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#identifierList.
    def enterIdentifierList(self, ctx:SmallCParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by SmallCParser#identifierList.
    def exitIdentifierList(self, ctx:SmallCParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by SmallCParser#typeName.
    def enterTypeName(self, ctx:SmallCParser.TypeNameContext):
        pass

    # Exit a parse tree produced by SmallCParser#typeName.
    def exitTypeName(self, ctx:SmallCParser.TypeNameContext):
        pass


    # Enter a parse tree produced by SmallCParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:SmallCParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by SmallCParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:SmallCParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by SmallCParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:SmallCParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by SmallCParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:SmallCParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by SmallCParser#typedefName.
    def enterTypedefName(self, ctx:SmallCParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by SmallCParser#typedefName.
    def exitTypedefName(self, ctx:SmallCParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by SmallCParser#initializer.
    def enterInitializer(self, ctx:SmallCParser.InitializerContext):
        pass

    # Exit a parse tree produced by SmallCParser#initializer.
    def exitInitializer(self, ctx:SmallCParser.InitializerContext):
        pass


    # Enter a parse tree produced by SmallCParser#initializerList.
    def enterInitializerList(self, ctx:SmallCParser.InitializerListContext):
        pass

    # Exit a parse tree produced by SmallCParser#initializerList.
    def exitInitializerList(self, ctx:SmallCParser.InitializerListContext):
        pass


    # Enter a parse tree produced by SmallCParser#designation.
    def enterDesignation(self, ctx:SmallCParser.DesignationContext):
        pass

    # Exit a parse tree produced by SmallCParser#designation.
    def exitDesignation(self, ctx:SmallCParser.DesignationContext):
        pass


    # Enter a parse tree produced by SmallCParser#designatorList.
    def enterDesignatorList(self, ctx:SmallCParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by SmallCParser#designatorList.
    def exitDesignatorList(self, ctx:SmallCParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by SmallCParser#designator.
    def enterDesignator(self, ctx:SmallCParser.DesignatorContext):
        pass

    # Exit a parse tree produced by SmallCParser#designator.
    def exitDesignator(self, ctx:SmallCParser.DesignatorContext):
        pass


    # Enter a parse tree produced by SmallCParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:SmallCParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by SmallCParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:SmallCParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#statement.
    def enterStatement(self, ctx:SmallCParser.StatementContext):
        pass

    # Exit a parse tree produced by SmallCParser#statement.
    def exitStatement(self, ctx:SmallCParser.StatementContext):
        pass


    # Enter a parse tree produced by SmallCParser#labeledStatement.
    def enterLabeledStatement(self, ctx:SmallCParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by SmallCParser#labeledStatement.
    def exitLabeledStatement(self, ctx:SmallCParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by SmallCParser#compoundStatement.
    def enterCompoundStatement(self, ctx:SmallCParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by SmallCParser#compoundStatement.
    def exitCompoundStatement(self, ctx:SmallCParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by SmallCParser#blockItemList.
    def enterBlockItemList(self, ctx:SmallCParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by SmallCParser#blockItemList.
    def exitBlockItemList(self, ctx:SmallCParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by SmallCParser#blockItem.
    def enterBlockItem(self, ctx:SmallCParser.BlockItemContext):
        pass

    # Exit a parse tree produced by SmallCParser#blockItem.
    def exitBlockItem(self, ctx:SmallCParser.BlockItemContext):
        pass


    # Enter a parse tree produced by SmallCParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SmallCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SmallCParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SmallCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SmallCParser#selectionStatement.
    def enterSelectionStatement(self, ctx:SmallCParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by SmallCParser#selectionStatement.
    def exitSelectionStatement(self, ctx:SmallCParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by SmallCParser#iterationStatement.
    def enterIterationStatement(self, ctx:SmallCParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by SmallCParser#iterationStatement.
    def exitIterationStatement(self, ctx:SmallCParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by SmallCParser#jumpStatement.
    def enterJumpStatement(self, ctx:SmallCParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by SmallCParser#jumpStatement.
    def exitJumpStatement(self, ctx:SmallCParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by SmallCParser#compilationUnit.
    def enterCompilationUnit(self, ctx:SmallCParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by SmallCParser#compilationUnit.
    def exitCompilationUnit(self, ctx:SmallCParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by SmallCParser#translationUnit.
    def enterTranslationUnit(self, ctx:SmallCParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by SmallCParser#translationUnit.
    def exitTranslationUnit(self, ctx:SmallCParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by SmallCParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:SmallCParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by SmallCParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:SmallCParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SmallCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SmallCParser#declarationList.
    def enterDeclarationList(self, ctx:SmallCParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by SmallCParser#declarationList.
    def exitDeclarationList(self, ctx:SmallCParser.DeclarationListContext):
        pass


