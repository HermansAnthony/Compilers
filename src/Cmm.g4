/**
 * Grammar for our Compiler project
 */
grammar Cmm;

// Start rule
program
    : externalDeclaration* EOF
;

externalDeclaration
    : functionDefinition
    | declaration
;

functionDefinition
// TODO Pointer
    : declarationSpecifier Star? Identifier LeftParen parameterList? RightParen compoundStatement
;

parameterList
    : parameterDeclaration
    | parameterList Comma parameterDeclaration
;

parameterDeclaration
    : declarationSpecifier declarator
;

// Declaration part of the grammar
declaration
    : declarationSpecifier initDeclarator Semicolon
    | declarationSpecifier Star? Identifier LeftParen parameterList? RightParen Semicolon
;

declarationSpecifier
    :   Const? typeSpecifier? Star*
;

typeSpecifier
    :   Void
    |   Char
    |   Int
    |   Float
;

initDeclarator
    : declarator
    | declarator Assign expression
;

declarator
    : Identifier
    | declarator LeftBracket expression RightBracket
;

// Primary expression part of the grammar
primaryExpression
    : Identifier
    | constant
//    | LeftParen expression RightParen
;

// Constant part of the grammar
constant
    : integerConstant
    | floatingConstant
    | Character
    | String
;

integerConstant
    : (Plus | Minus)? (NonZeroDigit | ZeroDigit)
    | (Plus | Minus)? NonZeroDigit (NonZeroDigit | ZeroDigit)+
;

floatingConstant
    : (Plus | Minus)? (NonZeroDigit | ZeroDigit)* Dot (NonZeroDigit | ZeroDigit)*
;

// Expression part of the grammar
expression
    : primaryExpression
    | arrayExpression
    | functionCallExpression
    | And expression
    | Identifier PlusPlus
    | Identifier MinusMinus
    | (primaryExpression | arrayExpression | functionCallExpression) binaryOperator expression
;

functionCallExpression
    : Identifier LeftParen argumentExpressionList? RightParen
;

arrayExpression
    : Identifier
    | arrayExpression LeftBracket expression RightBracket
;

binaryOperator
    : Assign | OrOr | AndAnd | Or | Caret | And | Equal | NotEqual | Less | Greater | LessEqual | GreaterEqual | Plus | Minus | Star | Div
;

argumentExpressionList
    : expression
    | argumentExpressionList Comma expression
;

// Statement part of the grammar
statement
    : compoundStatement
    | ifStatement
    | iterationStatement
    | jumpStatement
    | expression Semicolon
;

compoundStatement
    : LeftBrace (declaration | statement)* RightBrace
;

ifStatement
    : If LeftParen expression RightParen compoundStatement
    | If LeftParen expression RightParen compoundStatement Else compoundStatement
;

iterationStatement
    : While LeftParen expression RightParen statement
    | For LeftParen expression? Semicolon expression? Semicolon expression? RightParen statement
    | For LeftParen declaration expression? Semicolon expression? RightParen statement
;

jumpStatement
    : Continue Semicolon
    | Break Semicolon
    | Return expression? Semicolon
;

// Skip Part of the grammar
WS
    :   [ \t]+ -> skip
;

Newline
    : ('\r' '\n'? | '\n') -> skip
;

BlockComment
    : '/*' .*? '*/' -> skip
;

LineComment
    : '//' ~[\r\n]* -> skip
;

// Tokens
Apostrophe : '\'';
Character : Apostrophe . Apostrophe;
String : '"' (~('"') | '\\"')* '"';
Const : 'const';
Void : 'void';
Int : 'int';
Float : 'float';
Char : 'char';
If : 'if';
Else : 'else';
While : 'while';
For : 'for';
Break : 'break';
Continue : 'continue';
Return : 'return';

Identifier
    :   Nondigit (Nondigit | NonZeroDigit | ZeroDigit)*
;

NonZeroDigit : [1-9];
ZeroDigit : [0];
Nondigit : [a-zA-Z_];

LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';

Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';

Plus : '+';
PlusPlus : '++';
Minus : '-';
MinusMinus : '--';
Star : '*';
Div : '/';
Mod : '%';

And : '&';
Or : '|';
AndAnd : '&&';
OrOr : '||';
Caret : '^';
Not : '!';
Tilde : '~';

Question : '?';
Colon : ':';
Semicolon : ';';
Comma : ',';

Assign : '=';

Equal : '==';
NotEqual : '!=';

Arrow : '->';
Dot : '.';

Pound : '#';
