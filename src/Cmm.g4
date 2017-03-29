/**
 * Grammar for our Compilers project
 */
grammar Cmm;

// Start rule
program
    : primaryExpression
    | declaration
    | statement
    | externalDefinitions
;

// Primary expression part of the grammar
primaryExpression
    : identifier
    | constant
    | '(' expression ')'
;

// Identifier part of the grammar
identifier
    : NonDigit
    | identifier NonDigit
    | identifier Digit
;

identifierList
    : identifier
    | identifierList identifier
;

// Constant part of the grammar
constant
    : integerConstant
    | floatingConstant
    | characterConstant
;

integerConstant
    : decimalConstant
;

decimalConstant
    : NonZeroDigit
    | decimalConstant Digit
;

floatingConstant
    : decimalFloatingConstant
;

decimalFloatingConstant
    : fractionalConstant exponentPart?
    | digitSequence exponentPart
;

fractionalConstant
    : digitSequence? '.' digitSequence
    | digitSequence '.'
;

digitSequence
    : Digit
    | digitSequence Digit
;

exponentPart
    : 'e' Sign? digitSequence
    | 'E' Sign? digitSequence
;

Sign
    : '+'
    | '-'
;

characterConstant
    : '\'' cCharSequence '\''
;

cCharSequence
    : cChar
    | cCharSequence cChar
;

cChar
    : escapeSequence
    | '\''
    | '\n'
    | '\\'
;

escapeSequence
    : simpleEscapeSequence
;

simpleEscapeSequence
    : '\'' | '\"' | '\\' | '\b' | '\f' | '\n' | '\r' | '\t'
;

// End of the constant part of the grammar
// Expression part of the grammar

expression
    : assignmentExpression
    | expression ',' assignmentExpression
;

assignmentExpression
    : conditionalExpression
    | unaryExpression AssignmentOperator assignmentExpression
;

conditionalExpression
    : logicalORexpression
;

logicalORexpression
    : logicalANDexpression
    | logicalORexpression '||' logicalANDexpression
;

logicalANDexpression
    : inclusiveORexpression
    | logicalANDexpression '&&' inclusiveORexpression
;

inclusiveORexpression
    : exclusiveORexpression
    | inclusiveORexpression '|' exclusiveORexpression
;

exclusiveORexpression
    : andExpression
    | exclusiveORexpression '^' andExpression
;

andExpression
    : equalityExpression
    | andExpression '&' equalityExpression
;

equalityExpression
    : relationalExpression
    | equalityExpression '==' relationalExpression
    | equalityExpression '!=' relationalExpression
;

relationalExpression
    : additiveExpression
    | relationalExpression '<' shiftExpression
    | relationalExpression '>' shiftExpression
    | relationalExpression '<=' shiftExpression
    | relationalExpression '>=' shiftExpression
;

shiftExpression
    : additiveExpression
;

additiveExpression
    : multiplicativeExpression
    | additiveExpression '+' multiplicativeExpression
    | additiveExpression '-' multiplicativeExpression
;

multiplicativeExpression
    : unaryExpression
    | multiplicativeExpression '*' unaryExpression
    | multiplicativeExpression '/' unaryExpression
;

unaryExpression
    : postfixExpression
    | UnaryOperator unaryExpression
;

postfixExpression
    : primaryExpression
    | postfixExpression '[' expression ']'
    | postfixExpression '(' argumentExpressionList? ')'
;

argumentExpressionList
    : assignmentExpression
    | argumentExpressionList ',' assignmentExpression
;

constantExpression
    : conditionalExpression
;

// End of the expression part of the grammar

// Declaration part of the grammar
declaration
    : declarationSpecifiers
    | initDeclaratorList?
;

declarationSpecifiers
    : typeSpecifier declarationSpecifiers?
    | typeQualifier declarationSpecifiers?
;

typeSpecifier
    : Char | Int | Float | Void
;

typeQualifier
    : Const
;

initDeclaratorList
    : initDeclarator
    | initDeclaratorList ',' initDeclarator
;

initDeclarator
    : declarator
    | declarator '=' initializer
;

declarator
    : pointer? directDeclarator
;

pointer
    : '*' typeQualifierList?
    | '*' typeQualifierList? pointer
;

typeQualifierList
    : typeQualifier
    | typeQualifierList typeQualifier
;

directDeclarator
    : identifier
    | '(' declarator ')'
    | directDeclarator '[' typeQualifierList? assignmentExpression? ']'
    | directDeclarator '[' typeQualifierList? '*' ']'
    | directDeclarator '(' parameterTypeList ')'
    | directDeclarator '(' identifierList? ')'
;

parameterTypeList
    : parameterList
    | parameterList ',' '...'
;

parameterList
    : parameterDeclaration
    | parameterList ',' parameterDeclaration
;

parameterDeclaration
    : declarationSpecifiers declarator
    | declarationSpecifiers abstractDeclarator?
;

abstractDeclarator
    : pointer
    | pointer? directAbstractDeclarator
;

directAbstractDeclarator
    : '(' abstractDeclarator ')'
    | directAbstractDeclarator? '[' assignmentExpression? ']'
    | directAbstractDeclarator? '[' '*' ']'
    | directAbstractDeclarator? '(' parameterTypeList? ')'
    | '[' typeQualifierList? assignmentExpression? ']'
;

initializer
    : assignmentExpression
    | '{' initializerList '}'
    | '{' initializerList ',' '}'
;

initializerList
    : designation? initializer
    | initializerList ',' designation? initializer
;

designation
    : designatorList '='
;

designatorList
    : designator
    | designatorList designator
;

designator
    : '[' constantExpression ']'
    | '.' identifier
;


// End of the declaration part of the grammar

// Statement part of the grammar
statement
    : compoundStatement
    | expressionStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
;

compoundStatement
    : '{' blockItemList? '}'
;

blockItemList
    : blockItem
    | blockItemList blockItem
;

blockItem
    : declaration
    | statement
;

expressionStatement
    : expression? ';'
;

selectionStatement
    : 'if' '(' expression ')' statement
    | 'if' '(' expression ')' statement 'else' statement
;

iterationStatement
    : 'while' '(' expression ')' statement
    | 'for' '(' expression? ';' expression? ';' expression? ')' statement
    | 'for' '(' declaration expression? ';' expression? ')' statement
;

jumpStatement
    : 'continue' ';'
    | 'break' ';'
    | 'return' expression? ';'
;
// End of the statement part of the grammar

// External definition part of the grammar
externalDefinitions
    : translationUnit
    | externalDeclaration
    | functionDefinition
    | declarationList
;

translationUnit
    : externalDeclaration
    | translationUnit externalDeclaration
;

externalDeclaration
    : functionDefinition
    | declaration
;

functionDefinition
    : declarationSpecifiers declarator declarationList? compoundStatement
;

declarationList
    : declaration
    | declarationList declaration
;
// End of the external definition part of the grammar


// Terminals
NonDigit : [a-zA-Z_];
Digit : [0-9];
NonZeroDigit : [1-9];


AssignmentOperator : '=';
UnaryOperator : '&' | '*' | '+' | '-' | '!';

// Necessary types
Char : 'char';
Int : 'int';
Float : 'float';
Void : 'void';
Const : 'const';


WS : [ \t\n\r]+ -> skip ;
