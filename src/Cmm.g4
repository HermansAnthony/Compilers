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
    | Semicolon
;

functionDefinition
    : declarationSpecifier? pointer? Identifier LeftParen parameterList? RightParen compoundStatement
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
    :   Const? typeSpecifier
;

typeSpecifier
    :   Void
    |   Char
    |   Int
    |   Float
;

initDeclarator
    : declarator
    | declarator Assign assignmentExpression
;

declarator
    : pointer? directDeclarator
;

directDeclarator
    : Identifier
    | directDeclarator LeftBracket assignmentExpression? RightBracket
;

pointer
    : Star
;

// Primary expression part of the grammar
primaryExpression
    : identifier
    | constant
    | LeftParen expression RightParen
;

// Identifier part of the grammar
identifier
    :   Nondigit (Nondigit | Digit)*
;

// Constant part of the grammar
constant
    : integerConstant
    | floatingConstant
    | characterConstant
;

integerConstant
    : NonzeroDigit Digit* | Zero
;

floatingConstant
    : NonzeroDigit+ Dot Digit+
;

characterConstant
    : Apostrophe Character+ Apostrophe
;

// Expression part of the grammar
expression
    : assignmentExpression
    | expression Comma assignmentExpression
;

assignmentExpression
    : binaryExpression
    | postfixExpression Assign assignmentExpression
;

binaryExpression 
    : postfixExpression binaryOperator expression
;

binaryOperator
    : OrOr | AndAnd | Or | Caret | And | Equal | NotEqual | Less | Greater | LessEqual | GreaterEqual | Plus | Minus | Star | Div
;

postfixExpression
    : primaryExpression
    | postfixExpression LeftBracket expression RightBracket
    | postfixExpression LeftParen argumentExpressionList? RightParen
;

argumentExpressionList
    : assignmentExpression
    | argumentExpressionList Comma assignmentExpression
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
    :   LeftBrace (declaration | statement)* RightBrace
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
    :   [ \t]+
        -> skip
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
For : 'for';
If : 'if';
Else : 'else';
While : 'while';
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
LeftShift : '<<';
RightShift : '>>';

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

Nondigit : [a-zA-Z_];
Digit : [0-9];
NonzeroDigit : [1-9];
Zero : '0';
Character : ~['\\\r\n];
Apostrophe : '\'';
