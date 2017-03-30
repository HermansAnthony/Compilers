/**
 * Grammar for our Compilers project
 */
grammar Cmm;

// Start rule
program
    : translationUnit? EOF
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
    : fractionalConstant exponentPart?
    | digitSequence exponentPart
;

fractionalConstant
    : digitSequence? '.' digitSequence
    | digitSequence '.'
;

digitSequence
    : Digit+
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
    : '\'' cChar+ '\''
;

cChar
    : escapeSequence
    : ~['\\\r\n]
;

escapeSequence
    : '\'' | '\"' | '\\' | '\b' | '\f' | '\n' | '\r' | '\t'
;

// End of the constant part of the grammar
// Expression part of the grammar

expression
    : assignmentExpression
    | expression ',' assignmentExpression
;

assignmentExpression
    : logicalORexpression
    | unaryExpression AssignmentOperator assignmentExpression
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
    | relationalExpression '<' additiveExpression
    | relationalExpression '>' additiveExpression
    | relationalExpression '<=' additiveExpression
    | relationalExpression '>=' additiveExpression
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
    : '*' typeQualifier
    | '*' typeQualifier pointer
;

directDeclarator
    : identifier
    | '(' declarator ')'
    | directDeclarator '[' assignmentExpression? ']'
    | directDeclarator '(' parameterTypeList? ')'
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
;

initializer
    : assignmentExpression
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
translationUnit
    :   externalDeclaration
    |   translationUnit externalDeclaration
;

externalDeclaration
    : functionDefinition
    | declaration
;

functionDefinition
    : declarationSpecifiers declarator declaration* compoundStatement
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
