/**
 * Grammar for our Compiler project
 */
grammar Cmm;

// Start rule
program
    : externalDeclaration* EOF
;

externalDeclaration
    : functionDeclaration
    | declaration
;

functionDeclaration
    : declarationSpecifier Identifier LeftParen parameterList? RightParen compoundStatement
    | declarationSpecifier Identifier LeftParen parameterList? RightParen Semicolon 
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
;

declarationSpecifier
    :   typeSpecifier Star*
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
    | And (Identifier | arrayExpression)
    | Star+ (Identifier | arrayExpression)
    | (Identifier | arrayExpression)  PlusPlus
    | (Identifier | arrayExpression) MinusMinus
    | expression binaryOperator expression
;

functionCallExpression
    : Identifier LeftParen argumentExpressionList? RightParen
;

arrayExpression
    : Identifier
    | arrayExpression LeftBracket expression RightBracket
;

binaryOperator
    : OrOr | AndAnd | Or | Caret | And | Equal | NotEqual | Less | Greater | LessEqual | GreaterEqual | Plus | Minus | Star | Div
;

argumentExpressionList
    : expression
    | argumentExpressionList Comma expression
;

// Statement part of the grammar
statement
    : ifStatement
    | iterationStatement
    | jumpStatement
    | expression Semicolon
    | assignment Semicolon
;

assignment
    : Star* declarator Assign expression
;

compoundStatement
    : LeftBrace (declaration | statement)* RightBrace
;

ifStatement
    : If LeftParen expression RightParen compoundStatement
    | If LeftParen expression RightParen compoundStatement Else compoundStatement
;

iterationStatement
    : While LeftParen expression RightParen compoundStatement
    | For LeftParen (declaration|assignment)? Semicolon expression? Semicolon expression? RightParen compoundStatement
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
