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
    | Include Less Stdio Greater
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
    | Identifier Assign expression
    | declarator Assign initializerList
;

declarator
    : Identifier
    | Identifier LeftBracket integerConstant RightBracket
;

initializerList
    : LeftBrace expression? (Comma expression)* RightBrace
;

// Primary expression part of the grammar
primaryExpression
    : Identifier
    | constant
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
    : additiveExpression
    | expression OrOr additiveExpression
    | expression AndAnd additiveExpression
    | expression Equal additiveExpression
    | expression NotEqual additiveExpression
    | expression Less additiveExpression
    | expression Greater additiveExpression
    | expression LessEqual additiveExpression
    | expression GreaterEqual additiveExpression
;

functionCallExpression
    : Identifier LeftParen argumentExpressionList? RightParen
;

arrayExpression
    : Identifier LeftBracket expression RightBracket
;

binaryOperator
    : OrOr | AndAnd | Equal | NotEqual | Less | Greater | LessEqual | GreaterEqual | Plus | Minus | Star | Div
;

atomExpression
    : primaryExpression
    | arrayExpression
    | functionCallExpression
    | (Identifier | arrayExpression)  PlusPlus
    | (Identifier | arrayExpression) MinusMinus
    | And (Identifier | arrayExpression)
    | Star+ (Identifier | arrayExpression)
    | LeftParen expression RightParen
;

multiplicativeExpression
    : atomExpression
    | multiplicativeExpression Star atomExpression
    | multiplicativeExpression Div atomExpression
;

additiveExpression
    : multiplicativeExpression
    | additiveExpression Plus multiplicativeExpression
    | additiveExpression Minus multiplicativeExpression
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
    | functionCallExpression Semicolon
    | (Identifier | arrayExpression)  PlusPlus Semicolon
    | (Identifier | arrayExpression)  MinusMinus Semicolon
    | assignment Semicolon
;

assignment
    : Star* (declarator|arrayExpression) Assign expression
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
    | For LeftParen declaration expression? Semicolon (expression|assignment)? RightParen compoundStatement
    | For LeftParen assignment? Semicolon expression? Semicolon (expression|assignment)? RightParen compoundStatement
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
Include : '#include';
Stdio : 'stdio.h';
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
