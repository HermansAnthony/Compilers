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
    : declarationSpecifier? Star? identifier LeftParen parameterList? RightParen compoundStatement
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
    : declarationSpecifier initDeclarator? Semicolon
;

declarationSpecifier
    :   Const? typeSpecifier Star?
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
    : identifier
    | declarator LeftBracket expression? RightBracket
;

// Primary expression part of the grammar
primaryExpression
    : identifier
    | constant
    | LeftParen expression RightParen
;

// Identifier part of the grammar
identifier
    :   Nondigit (Nondigit | NonZeroDigit | ZeroDigit)*
;

// Constant part of the grammar
constant
    : integerConstant
    | floatingConstant
    | characterConstant
;

integerConstant
    : (Plus | Minus)? (NonZeroDigit | ZeroDigit)
    | (Plus | Minus)? NonZeroDigit (NonZeroDigit | ZeroDigit)+
;

floatingConstant
    : (Plus | Minus)? (NonZeroDigit | ZeroDigit)* Dot (NonZeroDigit | ZeroDigit)*
;

characterConstant
    : Apostrophe (Character | Nondigit)+ Apostrophe
;

// Expression part of the grammar
expression
    : postfixExpression
    | postfixExpression binaryOperator expression
;

binaryOperator
    : Assign | OrOr | AndAnd | Or | Caret | And | Equal | NotEqual | Less | Greater | LessEqual | GreaterEqual | Plus | Minus | Star | Div
;

postfixExpression
    : primaryExpression
    | postfixExpression LeftBracket expression RightBracket
    | postfixExpression LeftParen argumentExpressionList? RightParen
    | postfixExpression PlusPlus
    | postfixExpression MinusMinus
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
    | expression? Semicolon
;

compoundStatement
    : LeftBrace (declaration | statement)* RightBrace
;

ifStatement
    : If LeftParen expression RightParen statement
    | If LeftParen expression RightParen statement Else statement
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

NonZeroDigit : [1-9];
ZeroDigit : [0];
Nondigit : [a-zA-Z_];
Apostrophe : '\'';
Character : ~['\\\r\n];
