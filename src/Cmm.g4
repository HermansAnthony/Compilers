/**
 * Grammar for our Compilers project
 */
grammar Cmm;

// Tokens
Auto : 'auto';
Break : 'break';
Case : 'case';
Char : 'char';
Const : 'const';
Continue : 'continue';
Default : 'default';
Do : 'do';
Double : 'double';
Else : 'else';
Enum : 'enum';
Extern : 'extern';
Float : 'float';
For : 'for';
Goto : 'goto';
If : 'if';
Inline : 'inline';
Int : 'int';
Long : 'long';
Register : 'register';
Restrict : 'restrict';
Return : 'return';
Short : 'short';
Signed : 'signed';
Sizeof : 'sizeof';
Static : 'static';
Struct : 'struct';
Switch : 'switch';
Typedef : 'typedef';
Union : 'union';
Unsigned : 'unsigned';
Void : 'void';
Volatile : 'volatile';
While : 'while';

Alignas : '_Alignas';
Alignof : '_Alignof';
Atomic : '_Atomic';
Bool : '_Bool';
Complex : '_Complex';
Generic : '_Generic';
Imaginary : '_Imaginary';
Noreturn : '_Noreturn';
StaticAssert : '_Static_assert';
ThreadLocal : '_Thread_local';

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
Semi : ';';
Comma : ',';

Assign : '=';
StarAssign : '*=';
DivAssign : '/=';
ModAssign : '%=';
PlusAssign : '+=';
MinusAssign : '-=';
LeftShiftAssign : '<<=';
RightShiftAssign : '>>=';
AndAssign : '&=';
XorAssign : '^=';
OrAssign : '|=';

Equal : '==';
NotEqual : '!=';

Arrow : '->';
Dot : '.';
Ellipsis : '...';

// Start rule
program
    : externalDeclaration* EOF
;

externalDeclaration
    : functionDefinition
    | declaration
    | ';'
;

functionDefinition
    : declarationSpecifier? declarator declaration* compoundStatement
;

// Primary expression part of the grammar
primaryExpression
    : Identifier
    | Constant
    | '(' expression ')'
;

fragment
Nondigit : [a-zA-Z_];
fragment
Digit : [0-9];
fragment
NonzeroDigit : [1-9];

// Identifier part of the grammar
Identifier
    :   Nondigit (Nondigit | Digit)*
;

// Constant part of the grammar
Constant
    : IntegerConstant
    | FloatingConstant
    | CharacterConstant
;

fragment
IntegerConstant
    : DecimalConstant
;

fragment
DecimalConstant
    :   NonzeroDigit Digit* | '0'
;

fragment
FloatingConstant
    : FractionalConstant ExponentPart?
    | DigitSequence ExponentPart
;

fragment
FractionalConstant
    : DigitSequence? '.' DigitSequence
    | DigitSequence '.'
;

fragment
DigitSequence
    : Digit+
;

fragment
ExponentPart
    : 'e' Sign? DigitSequence
    | 'E' Sign? DigitSequence
;

fragment
Sign
    : '+'
    | '-'
;

fragment
CharacterConstant
    : '\'' CChar+ '\''
;

fragment
CChar
    :   ~['\\\r\n]
    |   EscapeSequence
;

fragment
EscapeSequence
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
    | unaryExpression assignmentOperator assignmentExpression
;

assignmentOperator
    :   '='
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
    | unaryOperator unaryExpression
;

unaryOperator : '&' | '*' | '+' | '-' | '!';

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
    : declarationSpecifier initDeclarator? ';'
;

declarationSpecifier
    :   typeQualifier? typeSpecifier
;

typeSpecifier
    :   ('void'
    |   'char'
    |   'int'
    |   'float')
;

typeQualifier
    :   'const'
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
    : Identifier
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
    : declarationSpecifier declarator
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
    :   '{' (declaration | statement)* '}'
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

WS
    :   [ \t]+
        -> skip
;

Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
;

BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;

